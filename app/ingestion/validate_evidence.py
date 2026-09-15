import json
from pathlib import Path


EVIDENCE_DIR = Path("data/evidence")


def validate_record(path: Path) -> list[str]:
    errors: list[str] = []

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        record = json.load(file)

    source = record.get("source", {})
    paper = record.get("paper", {})

    page_count = source.get(
        "page_count",
        0,
    )

    required_fields = [
        "title",
        "authors",
        "year",
        "doi",
        "research_problem",
        "research_objective",
        "robot_type",
        "stiffness_mechanism",
        "actuation",
        "modeling_methods",
        "experimental_setup",
        "main_results",
        "limitations_stated_by_authors",
        "limitations_inferred",
        "future_work",
        "evidence_relevant_to_topic",
        "possible_gap_implications",
        "confidence",
    ]

    for field in required_fields:
        if field not in paper:
            errors.append(
                f"Missing field: {field}"
            )

    for index, evidence in enumerate(
        paper.get(
            "evidence_relevant_to_topic",
            [],
        ),
        start=1,
    ):
        pages = evidence.get(
            "page_numbers",
            [],
        )

        if not pages:
            errors.append(
                f"Evidence {index}: "
                "no page provenance"
            )

        for page in pages:
            if (
                not isinstance(page, int)
                or page < 1
                or page > page_count
            ):
                errors.append(
                    f"Evidence {index}: "
                    f"invalid page {page}"
                )

    confidence = paper.get(
        "confidence"
    )

    if confidence not in {
        "low",
        "medium",
        "high",
    }:
        errors.append(
            "Invalid confidence value"
        )

    return errors


def main() -> None:
    files = sorted(
        EVIDENCE_DIR.glob("*.json")
    )

    if not files:
        raise RuntimeError(
            "No evidence JSON files found."
        )

    for path in files:
        errors = validate_record(path)

        if errors:
            print(
                f"\n[FAIL] {path.name}"
            )

            for error in errors:
                print(
                    f"  - {error}"
                )

        else:
            print(
                f"[PASS] {path.name}"
            )


if __name__ == "__main__":
    main()