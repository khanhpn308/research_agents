import argparse
import hashlib
import shutil
from pathlib import Path

from app.ingestion.registry import (
    load_registry,
    save_registry,
    utc_now,
)


DATA_DIR = Path("data")

PAPERS_DIR = (
    DATA_DIR / "papers"
)

SEED_DIR = (
    PAPERS_DIR / "seed"
)

VERIFICATION_DIR = (
    PAPERS_DIR / "verification"
)

EXCLUDED_DIR = (
    PAPERS_DIR / "excluded"
)


VALID_STATUSES = {
    "included",
    "pending",
    "excluded",
}


def sha256_file(
    path: Path,
) -> str:

    digest = hashlib.sha256()

    with path.open("rb") as handle:

        while True:

            chunk = handle.read(
                1024 * 1024
            )

            if not chunk:
                break

            digest.update(
                chunk
            )

    return digest.hexdigest()


def find_duplicate(
    registry: dict,
    pdf_sha256: str,
) -> dict | None:

    for paper in registry["papers"]:

        if (
            paper.get("pdf_sha256")
            == pdf_sha256
        ):
            return paper

    return None


def choose_destination(
    source_type: str,
    verification_id: str | None,
) -> Path:

    if source_type == "seed":

        return SEED_DIR

    if source_type == "verification":

        if not verification_id:
            raise RuntimeError(
                "--verification-id is required "
                "when --type verification is used."
            )

        return (
            VERIFICATION_DIR
            / verification_id
        )

    if source_type == "excluded":

        return EXCLUDED_DIR

    raise RuntimeError(
        f"Unsupported source type: "
        f"{source_type}"
    )


def default_status(
    source_type: str,
) -> str:

    if source_type == "seed":
        return "included"

    if source_type == "excluded":
        return "excluded"

    # Verification papers should normally
    # be screened before ingestion.
    return "pending"


def safe_target_path(
    source: Path,
    destination: Path,
    pdf_hash: str,
) -> Path:

    target = (
        destination
        / source.name
    )

    if not target.exists():
        return target

    existing_hash = sha256_file(
        target
    )

    if existing_hash == pdf_hash:
        return target

    return (
        destination
        / (
            f"{source.stem}"
            f"__{pdf_hash[:8]}"
            f"{source.suffix}"
        )
    )


def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Add a PDF to the production "
            "research corpus."
        )
    )

    parser.add_argument(
        "pdf",
        help="Path to PDF file.",
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=[
            "seed",
            "verification",
            "excluded",
        ],
    )

    parser.add_argument(
        "--verification-id",
        default=None,
        help=(
            "Example: GV-001. Required "
            "for verification papers."
        ),
    )

    parser.add_argument(
        "--status",
        choices=sorted(
            VALID_STATUSES
        ),
        default=None,
        help=(
            "Screening status. Defaults to "
            "included for seed, pending for "
            "verification, excluded for "
            "excluded papers."
        ),
    )

    parser.add_argument(
        "--reason",
        default="",
        help="Screening/provenance note.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Validate and show what would "
            "happen without changing files."
        ),
    )

    args = parser.parse_args()

    source = Path(
        args.pdf
    ).expanduser().resolve()

    if not source.exists():
        raise RuntimeError(
            f"File not found:\n{source}"
        )

    if not source.is_file():
        raise RuntimeError(
            f"Not a file:\n{source}"
        )

    if (
        source.suffix.lower()
        != ".pdf"
    ):
        raise RuntimeError(
            "Only PDF files are supported."
        )

    if (
        args.type
        == "verification"
        and not args.verification_id
    ):
        raise RuntimeError(
            "--verification-id is required "
            "for verification papers."
        )

    if (
        args.type
        != "verification"
        and args.verification_id
    ):
        raise RuntimeError(
            "--verification-id may only be "
            "used with --type verification."
        )

    screening_status = (
        args.status
        or default_status(
            args.type
        )
    )

    # Safety rule:
    # excluded storage should never become
    # ingestion-eligible.
    if args.type == "excluded":
        screening_status = "excluded"

    pdf_hash = sha256_file(
        source
    )

    paper_id = (
        pdf_hash[:10]
    )

    registry = load_registry()

    duplicate = find_duplicate(
        registry,
        pdf_hash,
    )

    if duplicate is not None:

        print(
            "[DUPLICATE]"
        )

        print(
            "paper_id:",
            duplicate["paper_id"],
        )

        print(
            "existing:",
            duplicate["relative_path"],
        )

        print(
            "filename:",
            duplicate["filename"],
        )

        print(
            "No new registry entry created."
        )

        return

    destination = choose_destination(
        args.type,
        args.verification_id,
    )

    destination.mkdir(
        parents=True,
        exist_ok=True,
    )

    target = safe_target_path(
        source,
        destination,
        pdf_hash,
    )

    relative_path = str(
        target.relative_to(
            DATA_DIR
        )
    )

    if args.dry_run:

        print(
            "[DRY RUN]"
        )

        print(
            f"paper_id: {paper_id}"
        )

        print(
            f"source: {source}"
        )

        print(
            f"target: {target}"
        )

        print(
            f"type: {args.type}"
        )

        print(
            "verification_id:",
            args.verification_id,
        )

        print(
            "screening_status:",
            screening_status,
        )

        return

    shutil.copy2(
        source,
        target,
    )

    timestamp = utc_now()

    entry = {
        "paper_id":
            paper_id,

        "filename":
            target.name,

        "relative_path":
            relative_path,

        "pdf_sha256":
            pdf_hash,

        "file_size_bytes":
            target.stat().st_size,

        "title":
            "",

        "doi":
            "",

        "year":
            None,

        "source_type":
            args.type,

        "verification_id":
            args.verification_id,

        "screening_status":
            screening_status,

        "screening_reason":
            args.reason,

        "ingestion_status":
            (
                "pending"
                if screening_status
                == "included"
                else "not_eligible"
            ),

        "evidence_status":
            "missing",

        "evidence_file":
            None,

        "added_at_utc":
            timestamp,

        "updated_at_utc":
            timestamp,

        "duplicate_paths":
            [],
    }

    registry["papers"].append(
        entry
    )

    save_registry(
        registry
    )

    print(
        "[ADDED]"
    )

    print(
        f"paper_id: {paper_id}"
    )

    print(
        f"path: {relative_path}"
    )

    print(
        f"type: {args.type}"
    )

    print(
        "verification_id:",
        args.verification_id,
    )

    print(
        "screening_status:",
        screening_status,
    )

    print(
        "ingestion_status:",
        entry["ingestion_status"],
    )


if __name__ == "__main__":
    main()