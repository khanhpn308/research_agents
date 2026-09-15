import json
from pathlib import Path


RUN_PATH = Path(
    "outputs/research_runs/latest.json"
)

OUTPUT_PATH = Path(
    "outputs/gap_verification.json"
)


def parse_structured_output(
    value: str,
    *,
    field_name: str,
) -> dict:

    if not value:
        raise RuntimeError(
            f"{field_name} is empty."
        )

    if "[DRY_RUN]" in value:
        raise RuntimeError(
            f"{field_name} contains DRY_RUN data.\n"
            "Run the real Researcher/Critic pipeline "
            "before building gap verification."
        )

    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{field_name} is not valid JSON."
        ) from exc

    if not isinstance(parsed, dict):
        raise RuntimeError(
            f"{field_name} must contain "
            "a JSON object."
        )

    return parsed


def normalize(
    text: str,
) -> str:

    return " ".join(
        text.lower().split()
    )


def main() -> None:

    if not RUN_PATH.exists():
        raise RuntimeError(
            "No saved research run found.\n"
            "Expected:\n"
            "outputs/research_runs/latest.json"
        )

    run = json.loads(
        RUN_PATH.read_text(
            encoding="utf-8"
        )
    )

    proposal = parse_structured_output(
        run.get(
            "research_proposal",
            "",
        ),
        field_name="research_proposal",
    )

    critique = parse_structured_output(
        run.get(
            "critique",
            "",
        ),
        field_name="critique",
    )

    tasks: list[dict] = []
    seen: set[str] = set()

    def add_task(
        *,
        priority: str,
        category: str,
        source: str,
        search_seed: str,
        purpose: str,
        decision_rule: str,
    ) -> None:

        text = search_seed.strip()

        if not text:
            return

        key = normalize(text)

        if key in seen:
            return

        seen.add(key)

        tasks.append(
            {
                "verification_id":
                    f"GV-{len(tasks) + 1:03d}",

                "priority":
                    priority,

                "category":
                    category,

                "source":
                    source,

                "search_seed":
                    text,

                "purpose":
                    purpose,

                "decision_rule":
                    decision_rule,

                "status":
                    "pending",
            }
        )

    # --------------------------------------------------------
    # 1. Searches explicitly requested by Researcher
    # --------------------------------------------------------

    for item in proposal.get(
        "required_external_searches",
        [],
    ):
        add_task(
            priority="critical",
            category="gap_closure_search",
            source="researcher",
            search_seed=item,
            purpose=(
                "Search for prior work that may "
                "already address or close the "
                "candidate research gap."
            ),
            decision_rule=(
                "If equivalent prior work already "
                "solves the same technical problem "
                "under comparable conditions, the "
                "candidate gap must be revised or "
                "rejected."
            ),
        )

    # --------------------------------------------------------
    # 2. Researcher falsification tests
    # --------------------------------------------------------

    for item in proposal.get(
        "falsification_checks",
        [],
    ):
        add_task(
            priority="critical",
            category="gap_falsification",
            source="researcher",
            search_seed=item,
            purpose=(
                "Attempt to falsify the proposed "
                "research direction rather than "
                "confirm it."
            ),
            decision_rule=(
                "Evidence satisfying this "
                "falsification condition weakens "
                "or invalidates the candidate gap."
            ),
        )

    # --------------------------------------------------------
    # 3. Critic falsification targets
    # --------------------------------------------------------

    for item in critique.get(
        "falsification_targets",
        [],
    ):
        add_task(
            priority="critical",
            category="critic_falsification",
            source="critic",
            search_seed=item,
            purpose=(
                "Test the strongest adversarial "
                "objection raised by the critic."
            ),
            decision_rule=(
                "If published evidence supports "
                "the critic's objection, the "
                "candidate gap cannot yet be "
                "accepted."
            ),
        )

    # --------------------------------------------------------
    # 4. Critic requests for missing evidence
    # --------------------------------------------------------

    for item in critique.get(
        "required_next_evidence",
        [],
    ):
        add_task(
            priority="high",
            category="missing_evidence",
            source="critic",
            search_seed=item,
            purpose=(
                "Acquire evidence currently "
                "missing from the corpus."
            ),
            decision_rule=(
                "The research direction remains "
                "unverified until this evidence "
                "has been reviewed."
            ),
        )

    # --------------------------------------------------------
    # 5. Gap validity concerns
    # --------------------------------------------------------

    for item in critique.get(
        "gap_validity_concerns",
        [],
    ):
        add_task(
            priority="high",
            category="gap_validity",
            source="critic",
            search_seed=item,
            purpose=(
                "Determine whether the apparent "
                "gap is genuinely scientific or "
                "only an implementation issue."
            ),
            decision_rule=(
                "If the concern is already resolved "
                "by established literature, revise "
                "or reject the gap."
            ),
        )

    # --------------------------------------------------------
    # 6. Methodology risks
    # --------------------------------------------------------

    for item in critique.get(
        "methodology_risks",
        [],
    ):
        add_task(
            priority="medium",
            category="methodology_validation",
            source="critic",
            search_seed=item,
            purpose=(
                "Check whether the proposed "
                "methodology is physically and "
                "experimentally defensible."
            ),
            decision_rule=(
                "If the methodology cannot test "
                "the research question reliably, "
                "the RQ or methodology must be "
                "revised."
            ),
        )

    output = {
        "source_run_timestamp":
            run.get("timestamp_utc"),

        "corpus_matrix_sha256":
            run.get(
                "corpus_matrix_sha256"
            ),

        "risk_level":
            run.get("risk_level"),

        "candidate_gap":
            proposal.get(
                "candidate_gap",
                "",
            ),

        "gap_status":
            proposal.get(
                "gap_status",
                "",
            ),

        "research_question":
            proposal.get(
                "research_question",
                "",
            ),

        "research_readiness":
            proposal.get(
                "research_readiness",
                "",
            ),

        "queue_summary": {
            "total_tasks":
                len(tasks),

            "critical":
                sum(
                    task["priority"]
                    == "critical"
                    for task in tasks
                ),

            "high":
                sum(
                    task["priority"]
                    == "high"
                    for task in tasks
                ),

            "medium":
                sum(
                    task["priority"]
                    == "medium"
                    for task in tasks
                ),
        },

        "verification_tasks":
            tasks,
    }

    OUTPUT_PATH.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        f"[TASKS] {len(tasks)}"
    )

    print(
        "[CRITICAL] "
        f"{output['queue_summary']['critical']}"
    )

    print(
        "[HIGH] "
        f"{output['queue_summary']['high']}"
    )

    print(
        "[MEDIUM] "
        f"{output['queue_summary']['medium']}"
    )

    print(
        f"[SAVED] {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()