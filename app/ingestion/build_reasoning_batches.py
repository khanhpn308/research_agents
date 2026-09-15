import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


MATRIX_PATH = Path(
    "outputs/literature_matrix.json"
)

OUTPUT_DIR = Path(
    "outputs/reasoning_batches"
)


# ============================================================
# PAPER FIELDS
# ============================================================

PAPER_FIELDS = [
    # Identity / citation
    "paper_id",
    "title",
    "authors",
    "year",
    "doi",

    # Scientific content
    "robot_type",
    "stiffness_mechanism",
    "actuation",
    "modeling_methods",
    "performance_metrics",
    "confidence",
]


LINKED_COLLECTIONS = [
    "evidence_claims",
    "limitations",
    "future_work",
    "gap_implications",
]


# ============================================================
# HELPERS
# ============================================================

def file_sha256(
    path: Path,
) -> str:

    hasher = hashlib.sha256()

    with path.open("rb") as file:
        while chunk := file.read(
            1024 * 1024
        ):
            hasher.update(chunk)

    return hasher.hexdigest()


def load_matrix() -> dict:

    if not MATRIX_PATH.exists():
        raise RuntimeError(
            "Missing literature matrix:\n"
            f"{MATRIX_PATH}"
        )

    try:
        return json.loads(
            MATRIX_PATH.read_text(
                encoding="utf-8"
            )
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "literature_matrix.json "
            "contains invalid JSON."
        ) from exc


def index_records_by_paper(
    records: list[Any],
) -> tuple[
    dict[str, list[dict]],
    list[Any],
]:

    index: dict[
        str,
        list[dict],
    ] = defaultdict(list)

    unlinked: list[Any] = []

    for record in records:

        if not isinstance(
            record,
            dict,
        ):
            unlinked.append(record)
            continue

        paper_id = str(
            record.get(
                "paper_id",
                "",
            )
            or ""
        ).strip()

        if not paper_id:
            unlinked.append(record)
            continue

        index[paper_id].append(
            record
        )

    return (
        dict(index),
        unlinked,
    )


def compact_paper(
    paper: dict,
    indexes: dict[
        str,
        dict[str, list[dict]],
    ],
) -> dict:

    paper_id = str(
        paper.get(
            "paper_id",
            "",
        )
        or ""
    ).strip()

    if not paper_id:
        raise RuntimeError(
            "Paper without paper_id "
            "found in matrix."
        )

    compact = {}

    for field in PAPER_FIELDS:
        compact[field] = (
            paper.get(field)
        )

    # --------------------------------------------------------
    # SOURCE-TRACEABLE RECORDS
    # --------------------------------------------------------

    compact[
        "evidence_claims"
    ] = indexes[
        "evidence_claims"
    ].get(
        paper_id,
        [],
    )

    compact[
        "limitations"
    ] = indexes[
        "limitations"
    ].get(
        paper_id,
        [],
    )

    compact[
        "future_work"
    ] = indexes[
        "future_work"
    ].get(
        paper_id,
        [],
    )

    compact[
        "gap_implications"
    ] = indexes[
        "gap_implications"
    ].get(
        paper_id,
        [],
    )

    return compact


def chunk_list(
    values: list,
    size: int,
) -> list[list]:

    return [
        values[i:i + size]
        for i in range(
            0,
            len(values),
            size,
        )
    ]


# ============================================================
# MAIN
# ============================================================

def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Build traceable reasoning "
            "batches from literature matrix."
        )
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=6,
        help=(
            "Number of papers per "
            "reasoning batch."
        ),
    )

    args = parser.parse_args()

    if args.batch_size < 1:
        raise RuntimeError(
            "--batch-size must be >= 1"
        )

    matrix = load_matrix()

    papers = matrix.get(
        "papers",
        [],
    )

    if not isinstance(
        papers,
        list,
    ):
        raise RuntimeError(
            "matrix['papers'] "
            "must be a list."
        )

    if not papers:
        raise RuntimeError(
            "No papers found in matrix."
        )

    # ========================================================
    # BUILD SOURCE INDEXES
    # ========================================================

    indexes: dict[
        str,
        dict[str, list[dict]],
    ] = {}

    unlinked_records: dict[
        str,
        list[Any],
    ] = {}

    for collection in (
        LINKED_COLLECTIONS
    ):

        records = matrix.get(
            collection,
            [],
        )

        if not isinstance(
            records,
            list,
        ):
            records = []

        (
            index,
            unlinked,
        ) = index_records_by_paper(
            records
        )

        indexes[
            collection
        ] = index

        unlinked_records[
            collection
        ] = unlinked

    # ========================================================
    # BUILD COMPACT PAPERS
    # ========================================================

    compact_papers = []

    seen_ids = set()

    for paper in papers:

        if not isinstance(
            paper,
            dict,
        ):
            continue

        compact = compact_paper(
            paper,
            indexes,
        )

        paper_id = compact[
            "paper_id"
        ]

        if paper_id in seen_ids:
            raise RuntimeError(
                "Duplicate paper_id "
                f"found: {paper_id}"
            )

        seen_ids.add(
            paper_id
        )

        compact_papers.append(
            compact
        )

    # ========================================================
    # SORT
    # ========================================================

    def sort_key(
        paper: dict,
    ) -> tuple:

        year = paper.get(
            "year"
        )

        try:
            year_value = int(year)
        except (
            TypeError,
            ValueError,
        ):
            year_value = 0

        title = str(
            paper.get(
                "title",
                "",
            )
            or ""
        )

        return (
            year_value,
            title.lower(),
        )

    compact_papers.sort(
        key=sort_key
    )

    # ========================================================
    # WRITE BATCHES
    # ========================================================

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Remove stale batch JSON files.
    for old_file in (
        OUTPUT_DIR.glob(
            "batch_*.json"
        )
    ):
        old_file.unlink()

    matrix_hash = file_sha256(
        MATRIX_PATH
    )

    batches = chunk_list(
        compact_papers,
        args.batch_size,
    )

    manifest_batches = []

    for index, batch in enumerate(
        batches,
        start=1,
    ):

        batch_id = (
            f"B{index:03d}"
        )

        batch_payload = {
            "schema_version": 1,

            "batch_id":
                batch_id,

            "source_matrix":
                str(MATRIX_PATH),

            "matrix_sha256":
                matrix_hash,

            "paper_count":
                len(batch),

            "paper_ids": [
                paper["paper_id"]
                for paper in batch
            ],

            "papers":
                batch,
        }

        output_path = (
            OUTPUT_DIR
            / f"batch_{index:03d}.json"
        )

        output_text = json.dumps(
            batch_payload,
            indent=2,
            ensure_ascii=False,
        )

        output_path.write_text(
            output_text,
            encoding="utf-8",
        )

        char_count = len(
            output_text
        )

        approx_tokens = int(
            char_count / 4
        )

        manifest_batches.append(
            {
                "batch_id":
                    batch_id,

                "file":
                    str(output_path),

                "paper_count":
                    len(batch),

                "paper_ids": [
                    paper[
                        "paper_id"
                    ]
                    for paper in batch
                ],

                "characters":
                    char_count,

                "approx_tokens":
                    approx_tokens,
            }
        )

        print(
            f"[BATCH] {batch_id}"
            f" | papers={len(batch)}"
            f" | chars={char_count:,}"
            f" | approx_tokens="
            f"{approx_tokens:,}"
        )

    # ========================================================
    # MANIFEST
    # ========================================================

    manifest = {
        "schema_version": 1,

        "source_matrix":
            str(MATRIX_PATH),

        "matrix_sha256":
            matrix_hash,

        "total_papers":
            len(
                compact_papers
            ),

        "batch_size":
            args.batch_size,

        "batch_count":
            len(batches),

        "batches":
            manifest_batches,

        "unlinked_records": {
            key: len(value)
            for key, value
            in unlinked_records.items()
        },
    }

    manifest_path = (
        OUTPUT_DIR
        / "manifest.json"
    )

    manifest_path.write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print()
    print(
        "[DONE]"
    )

    print(
        f"[PAPERS] "
        f"{len(compact_papers)}"
    )

    print(
        f"[BATCHES] "
        f"{len(batches)}"
    )

    print(
        f"[BATCH SIZE] "
        f"{args.batch_size}"
    )

    print(
        f"[MATRIX SHA256] "
        f"{matrix_hash[:16]}"
    )

    print(
        f"[MANIFEST] "
        f"{manifest_path}"
    )

    print()

    print(
        "[UNLINKED RECORDS]"
    )

    for (
        collection,
        records,
    ) in unlinked_records.items():

        print(
            f"  {collection}: "
            f"{len(records)}"
        )


if __name__ == "__main__":
    main()