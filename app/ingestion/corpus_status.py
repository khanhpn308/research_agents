from collections import Counter

from app.ingestion.registry import (
    load_registry,
)


def count_by(
    papers: list[dict],
    field: str,
) -> Counter:

    return Counter(
        str(
            paper.get(
                field,
                "unknown",
            )
        )
        for paper in papers
    )


def print_section(
    title: str,
    counter: Counter,
) -> None:

    print()
    print(title)
    print("-" * len(title))

    if not counter:
        print("none")
        return

    for key in sorted(
        counter.keys()
    ):
        print(
            f"{key:<20} "
            f"{counter[key]:>5}"
        )


def main() -> None:

    registry = load_registry()

    papers = registry.get(
        "papers",
        [],
    )

    total = len(
        papers
    )

    screening = count_by(
        papers,
        "screening_status",
    )

    ingestion = count_by(
        papers,
        "ingestion_status",
    )

    evidence = count_by(
        papers,
        "evidence_status",
    )

    source_types = count_by(
        papers,
        "source_type",
    )

    verification_papers = [
        paper
        for paper in papers
        if paper.get(
            "source_type"
        )
        == "verification"
    ]

    verification_ids = count_by(
        verification_papers,
        "verification_id",
    )

    included = screening.get(
        "included",
        0,
    )

    pending_screening = (
        screening.get(
            "pending",
            0,
        )
    )

    uncertain = screening.get(
        "uncertain",
        0,
    )

    excluded = screening.get(
        "excluded",
        0,
    )

    complete = ingestion.get(
        "complete",
        0,
    )

    pending_ingestion = (
        ingestion.get(
            "pending",
            0,
        )
    )

    processing = ingestion.get(
        "processing",
        0,
    )

    failed = ingestion.get(
        "failed",
        0,
    )

    not_eligible = ingestion.get(
        "not_eligible",
        0,
    )

    evidence_present = (
        evidence.get(
            "present",
            0,
        )
    )

    evidence_missing = (
        evidence.get(
            "missing",
            0,
        )
    )

    print()
    print(
        "=" * 56
    )

    print(
        "MECHANICAL RESEARCH CORPUS STATUS"
    )

    print(
        "=" * 56
    )

    print(
        f"Schema version: "
        f"{registry.get('schema_version')}"
    )

    print(
        f"Total papers:   {total}"
    )

    print()

    print(
        "SCREENING"
    )

    print(
        f"  Included:          "
        f"{included}"
    )

    print(
        f"  Pending screening: "
        f"{pending_screening}"
    )

    print(
        f"  Uncertain:         "
        f"{uncertain}"
    )

    print(
        f"  Excluded:          "
        f"{excluded}"
    )

    print()

    print(
        "INGESTION"
    )

    print(
        f"  Complete:          "
        f"{complete}"
    )

    print(
        f"  Pending ingestion: "
        f"{pending_ingestion}"
    )

    print(
        f"  Processing:        "
        f"{processing}"
    )

    print(
        f"  Failed:            "
        f"{failed}"
    )

    print(
        f"  Not eligible:      "
        f"{not_eligible}"
    )

    print()

    print(
        "EVIDENCE"
    )

    print(
        f"  Present:           "
        f"{evidence_present}"
    )

    print(
        f"  Missing:           "
        f"{evidence_missing}"
    )

    print_section(
        "SOURCE TYPES",
        source_types,
    )

    if verification_papers:

        print_section(
            "VERIFICATION TASKS",
            verification_ids,
        )

    # --------------------------------------------------
    # Consistency checks
    # --------------------------------------------------

    warnings = []

    for paper in papers:

        paper_id = paper.get(
            "paper_id",
            "unknown",
        )

        screening_status = (
            paper.get(
                "screening_status"
            )
        )

        ingestion_status = (
            paper.get(
                "ingestion_status"
            )
        )

        evidence_status = (
            paper.get(
                "evidence_status"
            )
        )

        if (
            screening_status
            == "excluded"
            and ingestion_status
            == "pending"
        ):
            warnings.append(
                f"{paper_id}: excluded "
                "but pending ingestion"
            )

        if (
            ingestion_status
            == "complete"
            and evidence_status
            != "present"
        ):
            warnings.append(
                f"{paper_id}: ingestion "
                "complete but evidence missing"
            )

        if (
            evidence_status
            == "present"
            and not paper.get(
                "evidence_file"
            )
        ):
            warnings.append(
                f"{paper_id}: evidence marked "
                "present but evidence_file empty"
            )

    print()

    print(
        "CONSISTENCY"
    )

    if warnings:

        print(
            f"  WARNINGS: "
            f"{len(warnings)}"
        )

        for warning in warnings:

            print(
                f"  - {warning}"
            )

    else:

        print(
            "  PASS"
        )

    print(
        "=" * 56
    )


if __name__ == "__main__":
    main()