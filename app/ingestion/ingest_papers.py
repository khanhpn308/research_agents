import argparse
import hashlib
import json
from pathlib import Path

from app.ingestion.paper_extractor import (
    extract_paper,
)
from app.ingestion.pdf_loader import (
    load_pdf,
)
from app.ingestion.registry import (
    get_ingestion_candidates,
    load_registry,
    mark_ingestion_complete,
    mark_ingestion_failed,
    mark_ingestion_started,
    resolve_pdf_path,
)


EVIDENCE_DIR = Path(
    "data/evidence"
)


def file_sha256(
    path: Path,
) -> str:

    hasher = hashlib.sha256()

    with path.open("rb") as file:

        while chunk := file.read(
            1024 * 1024
        ):
            hasher.update(
                chunk
            )

    return hasher.hexdigest()


def safe_output_name(
    pdf_path: Path,
) -> str:

    digest = file_sha256(
        pdf_path
    )[:10]

    return (
        f"{pdf_path.stem}_{digest}.json"
    )


def verify_registered_hash(
    paper_entry: dict,
    pdf_path: Path,
) -> str:

    actual_hash = file_sha256(
        pdf_path
    )

    registered_hash = str(
        paper_entry.get(
            "pdf_sha256",
            "",
        )
    ).strip()

    if (
        registered_hash
        and actual_hash
        != registered_hash
    ):
        raise RuntimeError(
            "PDF hash does not match "
            "paper_registry.json.\n\n"
            f"Paper: {pdf_path}\n"
            f"Registry: {registered_hash}\n"
            f"Actual:   {actual_hash}\n\n"
            "The PDF may have changed after "
            "registration. Run:\n"
            "python -m "
            "app.ingestion.init_corpus_storage"
        )

    return actual_hash


def ingest_one(
    paper_entry: dict,
    *,
    force: bool = False,
) -> None:

    paper_id = paper_entry[
        "paper_id"
    ]

    pdf_path = resolve_pdf_path(
        paper_entry
    )

    EVIDENCE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    pdf_hash = verify_registered_hash(
        paper_entry,
        pdf_path,
    )

    output_path = (
        EVIDENCE_DIR
        / safe_output_name(
            pdf_path
        )
    )

    # --------------------------------------------------------
    # Existing evidence
    # --------------------------------------------------------

    if (
        output_path.exists()
        and not force
    ):

        print(
            f"[SKIP] {pdf_path.name}"
        )

        print(
            "       evidence already exists"
        )

        # Registry may be stale even though
        # evidence is already present.
        mark_ingestion_complete(
            paper_id,
            output_path,
        )

        return

    # --------------------------------------------------------
    # Start ingestion
    # --------------------------------------------------------

    mark_ingestion_started(
        paper_id
    )

    try:

        print(
            f"\n[LOAD] {pdf_path.name}"
        )

        print(
            f"       paper_id={paper_id}"
        )

        print(
            "       source_type="
            f"{paper_entry.get('source_type')}"
        )

        if paper_entry.get(
            "verification_id"
        ):
            print(
                "       verification_id="
                f"{paper_entry['verification_id']}"
            )

        paper = load_pdf(
            pdf_path
        )

        print(
            f"       pages={paper['page_count']}, "
            f"chars={paper['char_count']:,}"
        )

        print(
            "[GEMINI] extracting evidence..."
        )

        result = extract_paper(
            paper
        )

        # ----------------------------------------------------
        # Preserve old evidence structure.
        #
        # Extra provenance fields are added under source,
        # but existing consumers can continue using:
        #
        # source / model / usage / paper
        # ----------------------------------------------------

        record = {
            "source": {
                "paper_id":
                    paper_id,

                "filename":
                    paper["filename"],

                "sha256":
                    pdf_hash,

                "page_count":
                    paper["page_count"],

                "char_count":
                    paper["char_count"],

                "source_type":
                    paper_entry.get(
                        "source_type"
                    ),

                "verification_id":
                    paper_entry.get(
                        "verification_id"
                    ),
            },

            "model":
                result["model"],

            "usage":
                result["usage"],

            "paper":
                result["extracted"],
        }

        # ----------------------------------------------------
        # Write atomically
        # ----------------------------------------------------

        temp_path = output_path.with_suffix(
            ".json.tmp"
        )

        with temp_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                record,
                file,
                indent=2,
                ensure_ascii=False,
            )

        temp_path.replace(
            output_path
        )

        # ----------------------------------------------------
        # Registry success
        # ----------------------------------------------------

        mark_ingestion_complete(
            paper_id,
            output_path,
        )

        print(
            f"[SAVED] {output_path}"
        )

        print(
            "[TOKENS] "
            f"{result['usage']['total_tokens']:,}"
        )

        print(
            f"[COMPLETE] {paper_id}"
        )

    except Exception as exc:

        mark_ingestion_failed(
            paper_id,
            str(exc),
        )

        print(
            f"[FAILED] {paper_id}"
        )

        print(
            f"         {exc}"
        )

        raise


def select_papers(
    *,
    force: bool,
) -> list[dict]:

    registry = load_registry()

    if not force:

        return get_ingestion_candidates(
            registry
        )

    # --force means:
    # re-run ALL included papers,
    # including papers already complete.
    #
    # Excluded/pending-screening papers
    # are still never processed.

    selected = []

    for paper in registry["papers"]:

        if (
            paper.get(
                "screening_status"
            )
            != "included"
        ):
            continue

        selected.append(
            paper
        )

    return selected


def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Ingest included papers from "
            "paper_registry.json."
        )
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help=(
            "Maximum number of eligible "
            "papers to ingest."
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Reprocess all included papers, "
            "even if evidence already exists."
        ),
    )

    args = parser.parse_args()

    papers = select_papers(
        force=args.force
    )

    if args.limit is not None:

        if args.limit < 1:
            raise RuntimeError(
                "--limit must be >= 1."
            )

        papers = papers[
            :args.limit
        ]

    print(
        "[INGESTION MODE] "
        + (
            "FORCE"
            if args.force
            else "INCREMENTAL"
        )
    )

    print(
        "[ELIGIBLE PAPERS] "
        f"{len(papers)}"
    )

    # No eligible papers is NOT an error.
    # This is the normal state when corpus
    # is already fully ingested.

    if not papers:

        print(
            "[NOTHING TO DO] "
            "No included + pending papers."
        )

        return

    success_count = 0

    for paper_entry in papers:

        ingest_one(
            paper_entry,
            force=args.force,
        )

        success_count += 1

    print()
    print(
        "[INGESTION COMPLETE]"
    )

    print(
        f"[PROCESSED] {success_count}"
    )


if __name__ == "__main__":
    main()