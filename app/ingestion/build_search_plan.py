import json
from pathlib import Path


INPUT_PATH = Path(
    "outputs/gap_verification.json"
)

OUTPUT_PATH = Path(
    "outputs/gap_search_plan.json"
)

MARKDOWN_PATH = Path(
    "outputs/gap_search_plan.md"
)


SEARCH_CATEGORIES = {
    "gap_closure_search",
    "gap_validity",
}

SCREENING_CATEGORIES = {
    "critic_falsification",
    "gap_falsification",
    "missing_evidence",
}

METHODOLOGY_CATEGORIES = {
    "methodology_validation",
}


def main() -> None:

    if not INPUT_PATH.exists():
        raise RuntimeError(
            "gap_verification.json not found."
        )

    data = json.loads(
        INPUT_PATH.read_text(
            encoding="utf-8"
        )
    )

    tasks = data.get(
        "verification_tasks",
        [],
    )

    searches = []
    screening = []
    methodology = []

    for task in tasks:

        category = task.get(
            "category",
            "",
        )

        if category in SEARCH_CATEGORIES:
            searches.append(task)

        elif category in SCREENING_CATEGORIES:
            screening.append(task)

        elif category in METHODOLOGY_CATEGORIES:
            methodology.append(task)

        else:
            screening.append(task)

    output = {
        "candidate_gap":
            data.get(
                "candidate_gap",
                "",
            ),

        "research_question":
            data.get(
                "research_question",
                "",
            ),

        "research_readiness":
            data.get(
                "research_readiness",
                "",
            ),

        "literature_searches":
            searches,

        "screening_criteria":
            screening,

        "methodology_checks":
            methodology,

        "summary": {
            "literature_searches":
                len(searches),

            "screening_criteria":
                len(screening),

            "methodology_checks":
                len(methodology),
        },
    }

    OUTPUT_PATH.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    lines = []

    lines.append(
        "# Gap Verification Search Plan"
    )

    lines.append("")
    lines.append(
        "## Candidate Gap"
    )
    lines.append("")
    lines.append(
        output["candidate_gap"]
    )

    lines.append("")
    lines.append(
        "## Research Question"
    )
    lines.append("")
    lines.append(
        output["research_question"]
    )

    lines.append("")
    lines.append(
        "# A. Literature Searches"
    )
    lines.append("")

    for index, task in enumerate(
        searches,
        start=1,
    ):
        lines.append(
            f"## Search {index}"
        )

        lines.append("")
        lines.append(
            f"**Priority:** "
            f"{task['priority']}"
        )

        lines.append("")
        lines.append(
            "**Search seed:**"
        )

        lines.append("")
        lines.append(
            task["search_seed"]
        )

        lines.append("")
        lines.append(
            "**Purpose:**"
        )

        lines.append("")
        lines.append(
            task["purpose"]
        )

        lines.append("")
        lines.append(
            "**Decision rule:**"
        )

        lines.append("")
        lines.append(
            task["decision_rule"]
        )

        lines.append("")

    lines.append(
        "# B. Paper Screening Criteria"
    )

    lines.append("")

    for task in screening:
        lines.append(
            f"- [{task['priority']}] "
            f"{task['search_seed']}"
        )

    lines.append("")
    lines.append(
        "# C. Methodology / Experiment Checks"
    )
    lines.append("")

    for task in methodology:
        lines.append(
            f"- [{task['priority']}] "
            f"{task['search_seed']}"
        )

    MARKDOWN_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print(
        "[SEARCHES]",
        len(searches),
    )

    print(
        "[SCREENING]",
        len(screening),
    )

    print(
        "[METHODOLOGY]",
        len(methodology),
    )

    print(
        f"[SAVED] {OUTPUT_PATH}"
    )

    print(
        f"[SAVED] {MARKDOWN_PATH}"
    )


if __name__ == "__main__":
    main()