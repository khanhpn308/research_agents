import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


DATA_DIR = Path("data")

LEGACY_DIR = DATA_DIR / "test_papers"

PAPERS_DIR = DATA_DIR / "papers"

SEED_DIR = PAPERS_DIR / "seed"

VERIFICATION_DIR = (
    PAPERS_DIR / "verification"
)

EXCLUDED_DIR = (
    PAPERS_DIR / "excluded"
)

EVIDENCE_DIR = (
    DATA_DIR / "evidence"
)

REGISTRY_PATH = (
    DATA_DIR / "paper_registry.json"
)


HEX_CHARS = set(
    "0123456789abcdef"
)


def utc_now() -> str:

    return datetime.now(
        timezone.utc
    ).isoformat()


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


def looks_like_paper_id(
    value: str,
) -> bool:

    value = value.lower()

    return (
        len(value) == 10
        and all(
            char in HEX_CHARS
            for char in value
        )
    )


def find_evidence_file(
    pdf_path: Path,
) -> Path | None:

    candidates = sorted(
        EVIDENCE_DIR.glob(
            f"{pdf_path.stem}_*.json"
        )
    )

    if not candidates:
        return None

    return candidates[0]


def recover_paper_id(
    pdf_path: Path,
    pdf_sha256: str,
) -> str:

    evidence_path = find_evidence_file(
        pdf_path
    )

    if evidence_path is not None:

        suffix = (
            evidence_path.stem
            .rsplit("_", 1)[-1]
            .lower()
        )

        if looks_like_paper_id(
            suffix
        ):
            return suffix

    # New papers that have not yet
    # been ingested receive a stable
    # content-based ID.
    return pdf_sha256[:10]


def read_evidence_metadata(
    evidence_path: Path | None,
) -> dict:

    if evidence_path is None:
        return {}

    try:

        data = json.loads(
            evidence_path.read_text(
                encoding="utf-8"
            )
        )

    except (
        json.JSONDecodeError,
        OSError,
    ):
        return {}

    paper = data.get(
        "paper",
        {}
    )

    if not isinstance(
        paper,
        dict,
    ):
        paper = {}

    return {
        "title":
            paper.get(
                "title",
                "",
            )
            or data.get(
                "title",
                "",
            ),

        "doi":
            paper.get(
                "doi",
                "",
            )
            or data.get(
                "doi",
                "",
            ),

        "year":
            paper.get(
                "year",
                None,
            )
            or data.get(
                "year",
                None,
            ),
    }


def migrate_legacy_seed() -> None:

    if not LEGACY_DIR.exists():
        print(
            "[LEGACY] "
            "data/test_papers not found."
        )
        return

    pdfs = sorted(
        LEGACY_DIR.glob(
            "*.pdf"
        )
    )

    print(
        f"[LEGACY PDFS] {len(pdfs)}"
    )

    for source in pdfs:

        target = (
            SEED_DIR
            / source.name
        )

        if target.exists():

            source_hash = (
                sha256_file(
                    source
                )
            )

            target_hash = (
                sha256_file(
                    target
                )
            )

            if (
                source_hash
                == target_hash
            ):
                print(
                    "[SKIP COPY] "
                    f"{source.name}"
                )
                continue

            target = (
                SEED_DIR
                / (
                    f"{source.stem}"
                    f"__{source_hash[:8]}"
                    f"{source.suffix}"
                )
            )

        shutil.copy2(
            source,
            target,
        )

        print(
            "[COPIED] "
            f"{source.name}"
        )


def classify_path(
    pdf_path: Path,
) -> tuple[str, str | None]:

    try:

        pdf_path.relative_to(
            SEED_DIR
        )

        return (
            "seed",
            None,
        )

    except ValueError:
        pass

    try:

        relative = (
            pdf_path.relative_to(
                VERIFICATION_DIR
            )
        )

        parts = relative.parts

        verification_id = (
            parts[0]
            if len(parts) > 1
            else None
        )

        return (
            "verification",
            verification_id,
        )

    except ValueError:
        pass

    try:

        pdf_path.relative_to(
            EXCLUDED_DIR
        )

        return (
            "excluded",
            None,
        )

    except ValueError:
        pass

    return (
        "unknown",
        None,
    )


def default_screening_status(
    source_type: str,
) -> str:

    if source_type == "seed":
        return "included"

    if source_type == "excluded":
        return "excluded"

    return "pending"


def default_screening_reason(
    source_type: str,
) -> str:

    if source_type == "seed":
        return (
            "Initial seed corpus migrated "
            "from legacy test_papers."
        )

    if source_type == "excluded":
        return (
            "Stored in excluded corpus."
        )

    return ""


def load_existing_registry() -> dict:

    if not REGISTRY_PATH.exists():
        return {}

    try:

        registry = json.loads(
            REGISTRY_PATH.read_text(
                encoding="utf-8"
            )
        )

    except json.JSONDecodeError:
        return {}

    by_hash = {}

    for paper in registry.get(
        "papers",
        [],
    ):

        pdf_hash = paper.get(
            "pdf_sha256"
        )

        if pdf_hash:
            by_hash[pdf_hash] = paper

    return by_hash


def build_registry() -> dict:

    previous = (
        load_existing_registry()
    )

    pdf_paths = []

    pdf_paths.extend(
        sorted(
            SEED_DIR.rglob(
                "*.pdf"
            )
        )
    )

    pdf_paths.extend(
        sorted(
            VERIFICATION_DIR.rglob(
                "*.pdf"
            )
        )
    )

    pdf_paths.extend(
        sorted(
            EXCLUDED_DIR.rglob(
                "*.pdf"
            )
        )
    )

    papers_by_hash = {}

    duplicate_count = 0

    for pdf_path in pdf_paths:

        pdf_hash = sha256_file(
            pdf_path
        )

        relative_path = str(
            pdf_path.relative_to(
                DATA_DIR
            )
        )

        # --------------------------------
        # Duplicate PDF
        # --------------------------------

        if pdf_hash in papers_by_hash:

            duplicate_count += 1

            existing = (
                papers_by_hash[
                    pdf_hash
                ]
            )

            duplicates = (
                existing.setdefault(
                    "duplicate_paths",
                    [],
                )
            )

            if (
                relative_path
                not in duplicates
            ):
                duplicates.append(
                    relative_path
                )

            continue

        source_type, verification_id = (
            classify_path(
                pdf_path
            )
        )

        evidence_path = (
            find_evidence_file(
                pdf_path
            )
        )

        metadata = (
            read_evidence_metadata(
                evidence_path
            )
        )

        paper_id = (
            recover_paper_id(
                pdf_path,
                pdf_hash,
            )
        )

        old = previous.get(
            pdf_hash,
            {},
        )

        entry = {
            "paper_id":
                old.get(
                    "paper_id",
                    paper_id,
                ),

            "filename":
                pdf_path.name,

            "relative_path":
                relative_path,

            "pdf_sha256":
                pdf_hash,

            "file_size_bytes":
                pdf_path.stat().st_size,

            "title":
                metadata.get(
                    "title",
                    "",
                )
                or old.get(
                    "title",
                    "",
                ),

            "doi":
                metadata.get(
                    "doi",
                    "",
                )
                or old.get(
                    "doi",
                    "",
                ),

            "year":
                metadata.get(
                    "year",
                    None,
                )
                or old.get(
                    "year",
                    None,
                ),

            "source_type":
                source_type,

            "verification_id":
                verification_id,

            "screening_status":
                old.get(
                    "screening_status",
                    default_screening_status(
                        source_type
                    ),
                ),

            "screening_reason":
                old.get(
                    "screening_reason",
                    default_screening_reason(
                        source_type
                    ),
                ),

            "ingestion_status":
                (
                    "complete"
                    if evidence_path
                    else "pending"
                ),

            "evidence_status":
                (
                    "present"
                    if evidence_path
                    else "missing"
                ),

            "evidence_file":
                (
                    str(
                        evidence_path
                        .relative_to(
                            DATA_DIR
                        )
                    )
                    if evidence_path
                    else None
                ),

            "added_at_utc":
                old.get(
                    "added_at_utc",
                    utc_now(),
                ),

            "updated_at_utc":
                utc_now(),

            "duplicate_paths":
                old.get(
                    "duplicate_paths",
                    [],
                ),
        }

        papers_by_hash[
            pdf_hash
        ] = entry

    papers = sorted(
        papers_by_hash.values(),
        key=lambda item: (
            item["source_type"],
            item["filename"],
        ),
    )

    return {
        "schema_version": 1,

        "updated_at_utc":
            utc_now(),

        "paper_count":
            len(papers),

        "duplicate_count":
            duplicate_count,

        "papers":
            papers,
    }


def main() -> None:

    SEED_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    VERIFICATION_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    EXCLUDED_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    EVIDENCE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Copy old 5-paper corpus.
    # DO NOT delete legacy folder yet.
    migrate_legacy_seed()

    registry = build_registry()

    REGISTRY_PATH.write_text(
        json.dumps(
            registry,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    papers = registry["papers"]

    seed_count = sum(
        paper["source_type"]
        == "seed"
        for paper in papers
    )

    verification_count = sum(
        paper["source_type"]
        == "verification"
        for paper in papers
    )

    excluded_count = sum(
        paper["source_type"]
        == "excluded"
        for paper in papers
    )

    evidence_count = sum(
        paper["evidence_status"]
        == "present"
        for paper in papers
    )

    print()
    print(
        "[CORPUS STORAGE INITIALIZED]"
    )

    print(
        f"[PAPERS] {len(papers)}"
    )

    print(
        f"[SEED] {seed_count}"
    )

    print(
        "[VERIFICATION] "
        f"{verification_count}"
    )

    print(
        f"[EXCLUDED] {excluded_count}"
    )

    print(
        "[EVIDENCE PRESENT] "
        f"{evidence_count}"
    )

    print(
        "[DUPLICATES] "
        f"{registry['duplicate_count']}"
    )

    print(
        f"[REGISTRY] {REGISTRY_PATH}"
    )


if __name__ == "__main__":
    main()