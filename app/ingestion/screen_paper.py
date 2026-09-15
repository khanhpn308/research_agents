import argparse

from app.ingestion.registry import (
    find_paper,
    load_registry,
    save_registry,
    utc_now,
)


VALID_DECISIONS = {
    "include",
    "exclude",
    "uncertain",
}


def apply_decision(
    paper: dict,
    decision: str,
    reason: str,
) -> None:

    if decision == "include":

        paper["screening_status"] = (
            "included"
        )

        # If evidence already exists,
        # preserve the completed state.
        if (
            paper.get(
                "evidence_status"
            )
            == "present"
        ):
            paper["ingestion_status"] = (
                "complete"
            )

        else:
            paper["ingestion_status"] = (
                "pending"
            )

    elif decision == "exclude":

        paper["screening_status"] = (
            "excluded"
        )

        # Excluded papers must never
        # enter automatic ingestion.
        paper["ingestion_status"] = (
            "not_eligible"
        )

    elif decision == "uncertain":

        paper["screening_status"] = (
            "uncertain"
        )

        # Require human/full-text review
        # before model ingestion.
        paper["ingestion_status"] = (
            "not_eligible"
        )

    else:
        raise RuntimeError(
            f"Unsupported decision: "
            f"{decision}"
        )

    paper["screening_reason"] = (
        reason
    )

    paper["screened_at_utc"] = (
        utc_now()
    )

    paper["updated_at_utc"] = (
        utc_now()
    )


def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Record a screening decision "
            "for a registered research paper."
        )
    )

    parser.add_argument(
        "--id",
        required=True,
        help="paper_id from paper_registry.json",
    )

    parser.add_argument(
        "--decision",
        required=True,
        choices=sorted(
            VALID_DECISIONS
        ),
    )

    parser.add_argument(
        "--reason",
        required=True,
        help=(
            "Scientific reason for the "
            "screening decision."
        ),
    )

    args = parser.parse_args()

    registry = load_registry()

    paper = find_paper(
        args.id,
        registry,
    )

    old_status = paper.get(
        "screening_status"
    )

    old_ingestion = paper.get(
        "ingestion_status"
    )

    apply_decision(
        paper,
        args.decision,
        args.reason,
    )

    save_registry(
        registry
    )

    print(
        "[SCREENING UPDATED]"
    )

    print(
        "paper_id:",
        paper["paper_id"],
    )

    print(
        "filename:",
        paper["filename"],
    )

    print(
        "source_type:",
        paper.get(
            "source_type"
        ),
    )

    print(
        "verification_id:",
        paper.get(
            "verification_id"
        ),
    )

    print(
        "screening:",
        f"{old_status}"
        " -> "
        f"{paper['screening_status']}",
    )

    print(
        "ingestion:",
        f"{old_ingestion}"
        " -> "
        f"{paper['ingestion_status']}",
    )

    print(
        "reason:",
        paper["screening_reason"],
    )


if __name__ == "__main__":
    main()