import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path(
    "data/paper_registry.json"
)

EVIDENCE_DIR = Path(
    "data/evidence"
)

OUTPUT_ROOT = Path(
    "outputs/verification"
)


def load_json(
    path: Path,
) -> dict:

    return json.loads(
        path.read_text(
            encoding="utf-8",
        )
    )


def save_json(
    path: Path,
    data: dict,
) -> None:

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def sha256_text(
    text: str,
) -> str:

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def find_evidence_file(
    paper_id: str,
) -> Path:

    matches = sorted(
        EVIDENCE_DIR.glob(
            f"*_{paper_id}.json"
        )
    )

    if not matches:
        raise RuntimeError(
            "Evidence file not found for "
            f"paper_id={paper_id}"
        )

    if len(matches) > 1:
        raise RuntimeError(
            "Multiple evidence files found for "
            f"paper_id={paper_id}:\n"
            + "\n".join(
                str(path)
                for path in matches
            )
        )

    return matches[0]


def normalize_list(
    value: Any,
) -> list:

    if value is None:
        return []

    if isinstance(
        value,
        list,
    ):
        return value

    return [value]


def markdown_value(
    value: Any,
) -> str:

    if value is None:
        return ""

    if isinstance(
        value,
        str,
    ):
        return value.strip()

    if isinstance(
        value,
        (
            int,
            float,
            bool,
        ),
    ):
        return str(value)

    return json.dumps(
        value,
        ensure_ascii=False,
    )


def append_section(
    lines: list[str],
    title: str,
    value: Any,
) -> None:

    items = normalize_list(
        value
    )

    if not items:
        return

    lines.append(
        f"### {title}"
    )
    lines.append("")

    for item in items:

        text = markdown_value(
            item
        )

        if text:
            lines.append(
                f"- {text}"
            )

    lines.append("")


def build_markdown(
    matrix: dict,
) -> str:

    lines: list[str] = []

    lines.append(
        "# Verification Matrix"
    )
    lines.append("")

    lines.append(
        f"**Verification ID:** "
        f"{matrix['verification_id']}"
    )

    lines.append(
        f"**Paper count:** "
        f"{matrix['paper_count']}"
    )

    lines.append(
        f"**Purpose:** "
        f"{matrix['purpose']}"
    )

    lines.append("")

    lines.append(
        "## Verification Papers"
    )
    lines.append("")

    for index, record in enumerate(
        matrix["papers"],
        start=1,
    ):

        paper = record[
            "evidence"
        ].get(
            "paper",
            {},
        )

        title = (
            paper.get("title")
            or record.get("filename")
            or record["paper_id"]
        )

        year = paper.get(
            "year",
            "",
        )

        lines.append(
            f"## V{index:02d} — {title}"
        )
        lines.append("")

        lines.append(
            f"- **paper_id:** "
            f"`{record['paper_id']}`"
        )

        lines.append(
            f"- **year:** {year}"
        )

        lines.append(
            f"- **doi:** "
            f"{paper.get('doi', '')}"
        )

        lines.append(
            f"- **source_type:** "
            f"{record['source_type']}"
        )

        lines.append(
            f"- **verification_id:** "
            f"{record['verification_id']}"
        )

        lines.append(
            f"- **screening_status:** "
            f"{record['screening_status']}"
        )

        lines.append(
            f"- **screening_reason:** "
            f"{record.get('screening_reason', '')}"
        )

        lines.append("")

        append_section(
            lines,
            "Robot / Structure Type",
            paper.get(
                "robot_type"
            ),
        )

        append_section(
            lines,
            "Stiffness Mechanism",
            paper.get(
                "stiffness_mechanism"
            ),
        )

        append_section(
            lines,
            "Actuation",
            paper.get(
                "actuation"
            ),
        )

        append_section(
            lines,
            "Modeling Methods",
            paper.get(
                "modeling_methods"
            ),
        )

        append_section(
            lines,
            "Performance Metrics",
            paper.get(
                "performance_metrics"
            ),
        )

        append_section(
            lines,
            "Evidence Claims",
            paper.get(
                "evidence_claims"
            ),
        )

        append_section(
            lines,
            "Limitations",
            paper.get(
                "limitations"
            ),
        )

        append_section(
            lines,
            "Future Work",
            paper.get(
                "future_work"
            ),
        )

        append_section(
            lines,
            "Gap Implications",
            paper.get(
                "gap_implications"
            ),
        )

    return "\n".join(
        lines
    ).strip() + "\n"


def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Build a verification-only literature "
            "matrix for one verification task."
        )
    )

    parser.add_argument(
        "--verification-id",
        required=True,
        help=(
            "Verification task ID, "
            "for example D1-V001."
        ),
    )

    args = parser.parse_args()

    verification_id = (
        args.verification_id.strip()
    )

    if not verification_id:
        raise RuntimeError(
            "verification_id cannot be empty."
        )

    if not REGISTRY_PATH.exists():
        raise RuntimeError(
            f"Registry not found: "
            f"{REGISTRY_PATH}"
        )

    registry = load_json(
        REGISTRY_PATH
    )

    papers = registry.get(
        "papers",
        [],
    )

    selected = []

    for paper in papers:

        if (
            paper.get("source_type")
            != "verification"
        ):
            continue

        if (
            paper.get("verification_id")
            != verification_id
        ):
            continue

        screening_status = paper.get(
            "screening_status"
        )

    # Excluded papers remain in the registry for provenance,
    # but must not enter the scientific verification matrix.
        if screening_status == "excluded":
            continue

    # Pending / uncertain papers indicate an unfinished
    # verification round and should not be silently ignored.
        if screening_status != "included":
            raise RuntimeError(
                f"{paper.get('paper_id')}: "
                "verification paper screening is unresolved "
                f"(screening_status={screening_status!r})."
            )

        selected.append(
            paper
        )

    if not selected:
        raise RuntimeError(
            "No verification papers found for "
            f"{verification_id}"
        )

    selected.sort(
        key=lambda item: (
            str(
                item.get(
                    "filename",
                    "",
                )
            ).lower(),
            str(
                item.get(
                    "paper_id",
                    "",
                )
            ),
        )
    )

    records = []

    for registry_record in selected:

        paper_id = str(
            registry_record[
                "paper_id"
            ]
        )

        screening_status = (
            registry_record.get(
                "screening_status"
            )
        )

        ingestion_status = (
            registry_record.get(
                "ingestion_status"
            )
        )

        evidence_status = (
            registry_record.get(
                "evidence_status"
            )
        )

        if screening_status != "included":
            raise RuntimeError(
                f"{paper_id}: "
                "verification paper is not included "
                f"(screening_status="
                f"{screening_status!r})."
            )

        if ingestion_status != "complete":
            raise RuntimeError(
                f"{paper_id}: "
                "verification paper is not complete "
                f"(ingestion_status="
                f"{ingestion_status!r})."
            )

        if evidence_status != "present":
            raise RuntimeError(
                f"{paper_id}: "
                "verification evidence is not present "
                f"(evidence_status="
                f"{evidence_status!r})."
            )

        evidence_path = (
            find_evidence_file(
                paper_id
            )
        )

        evidence = load_json(
            evidence_path
        )

        records.append(
            {
                "paper_id":
                    paper_id,

                "filename":
                    registry_record.get(
                        "filename",
                        "",
                    ),

                "path":
                    registry_record.get(
                        "path",
                        "",
                    ),

                "source_type":
                    registry_record.get(
                        "source_type",
                        "",
                    ),

                "verification_id":
                    registry_record.get(
                        "verification_id",
                        "",
                    ),

                "screening_status":
                    screening_status,

                "screening_reason":
                    registry_record.get(
                        "screening_reason",
                        registry_record.get(
                            "reason",
                            "",
                        ),
                    ),

                "ingestion_status":
                    ingestion_status,

                "evidence_status":
                    evidence_status,

                "evidence_file":
                    str(
                        evidence_path
                    ),

                # Keep the complete extracted
                # evidence record.
                #
                # Do NOT aggressively compress
                # verification evidence here.
                # The next adversarial reasoning
                # step needs the original claims,
                # limitations and provenance.
                "evidence":
                    evidence,
            }
        )

    matrix = {
        "schema_version": 1,

        "verification_id":
            verification_id,

        "created_at":
            datetime.now(
                timezone.utc
            ).isoformat(),

        "purpose": (
            "Independent adversarial literature "
            "verification of an existing research "
            "direction. Verification papers must "
            "be used to challenge, narrow, pivot, "
            "or reject the direction rather than "
            "to confirm it by default."
        ),

        "paper_count":
            len(records),

        "papers":
            records,
    }

    canonical = json.dumps(
        matrix,
        ensure_ascii=False,
        sort_keys=True,
        separators=(
            ",",
            ":",
        ),
    )

    matrix[
        "matrix_sha256"
    ] = sha256_text(
        canonical
    )

    output_dir = (
        OUTPUT_ROOT
        / verification_id
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    json_path = (
        output_dir
        / "verification_matrix.json"
    )

    markdown_path = (
        output_dir
        / "verification_matrix.md"
    )

    save_json(
        json_path,
        matrix,
    )

    markdown = build_markdown(
        matrix
    )

    markdown_path.write_text(
        markdown,
        encoding="utf-8",
    )

    print(
        f"[VERIFICATION] "
        f"{verification_id}"
    )

    print(
        f"[PAPERS] "
        f"{len(records)}"
    )

    print(
        "[PAPER IDS]"
    )

    for record in records:
        print(
            " -",
            record["paper_id"],
            "|",
            record["filename"],
        )

    print(
        f"[MATRIX SHA256] "
        f"{matrix['matrix_sha256'][:16]}"
    )

    print(
        f"[SAVED] "
        f"{json_path}"
    )

    print(
        f"[SAVED] "
        f"{markdown_path}"
    )


if __name__ == "__main__":
    main()