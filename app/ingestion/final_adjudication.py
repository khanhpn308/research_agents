import json
import os
from pathlib import Path

from app.providers.codex_provider import call_codex


CANDIDATE_PATH = Path(
    "outputs/candidate_directions.json"
)

CRITIQUE_PATH = Path(
    "outputs/direction_critique.json"
)

RAW_OUTPUT_PATH = Path(
    "outputs/final_adjudication_raw.json"
)

OUTPUT_PATH = Path(
    "outputs/final_adjudication.json"
)

MARKDOWN_PATH = Path(
    "outputs/final_adjudication.md"
)


# ============================================================
# UTILITIES
# ============================================================


def load_json(
    path: Path,
) -> dict:

    if not path.exists():
        raise RuntimeError(
            f"Missing required file: {path}"
        )

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def make_strict_schema(
    schema,
):
    """
    Recursively enforce OpenAI Structured Output rules.
    """

    if isinstance(schema, dict):

        if schema.get("type") == "object":

            schema[
                "additionalProperties"
            ] = False

            properties = schema.get(
                "properties",
                {},
            )

            schema[
                "required"
            ] = list(
                properties.keys()
            )

        for value in schema.values():
            make_strict_schema(
                value
            )

    elif isinstance(schema, list):

        for value in schema:
            make_strict_schema(
                value
            )

    return schema


# ============================================================
# LOAD DECISION PACKAGE
# ============================================================


def load_decision_package() -> dict:

    candidate_data = load_json(
        CANDIDATE_PATH
    )

    critique_data = load_json(
        CRITIQUE_PATH
    )

    candidate_analysis = (
        candidate_data.get(
            "analysis",
            candidate_data,
        )
    )

    critique = (
        critique_data.get(
            "critique",
            critique_data,
        )
    )

    directions = candidate_analysis.get(
        "candidate_directions",
        [],
    )

    shortlist = critique.get(
        "shortlist",
        [],
    )

    if not directions:
        raise RuntimeError(
            "No candidate directions found."
        )

    if not shortlist:
        raise RuntimeError(
            "Critic shortlist is empty."
        )

    # Current expected shortlist: D1, D2.
    shortlisted = []

    for direction in directions:

        direction_id = str(
            direction.get(
                "direction_id",
                "",
            )
        ).strip()

        if direction_id in shortlist:
            shortlisted.append(
                direction
            )

    if len(shortlisted) < 2:
        raise RuntimeError(
            "Final adjudication requires "
            "at least two shortlisted directions."
        )

    # Only include critique records for shortlisted directions.
    review_map = {}

    for review in critique.get(
        "direction_reviews",
        [],
    ):

        direction_id = str(
            review.get(
                "direction_id",
                "",
            )
        ).strip()

        if direction_id in shortlist:

            review_map[
                direction_id
            ] = review

    shortlisted_reviews = [
        review_map[direction_id]
        for direction_id in shortlist
        if direction_id in review_map
    ]

    return {
        "shortlist":
            shortlist,

        "shortlisted_directions":
            shortlisted,

        "critic_reviews":
            shortlisted_reviews,

        "researcher_provisional_recommendation":
            candidate_analysis.get(
                "provisional_recommendation",
                "",
            ),

        "critic_recommendation":
            critique.get(
                "recommended_for_submission",
                "",
            ),

        "critic_recommendation_rationale":
            critique.get(
                "recommendation_rationale",
                "",
            ),

        "critic_novelty_status":
            critique.get(
                "novelty_status",
                "",
            ),

        "external_search_priorities":
            critique.get(
                "external_search_priorities",
                [],
            ),
    }


# ============================================================
# OUTPUT SCHEMA
# ============================================================


def build_schema() -> dict:

    schema = {
        "type": "object",

        "properties": {

            "selected_direction": {
                "type": "string",
            },

            "decision": {
                "type": "string",
                "enum": [
                    "select",
                    "select_with_revision",
                    "insufficient_confidence",
                ],
            },

            "confidence": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                ],
            },

            "final_title_en": {
                "type": "string",
            },

            "final_title_vi": {
                "type": "string",
            },

            "concise_problem_statement": {
                "type": "string",
            },

            "research_objective": {
                "type": "string",
            },

            "preliminary_research_question": {
                "type": "string",
            },

            "scientific_hypothesis": {
                "type": "string",
            },

            "independent_variables": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "dependent_variables": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "control_variables": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "performance_metrics": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "scope": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "expected_contribution": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "why_selected_over_alternative": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "msc_feasibility_assessment": {
                "type": "string",
            },

            "publication_path": {
                "type": "string",
            },

            "fatal_flaws_checked": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "unresolved_novelty_risks": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "searches_required_after_submission": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "submission_rationale": {
                "type": "string",
            },

            "astra_escalation_required": {
                "type": "boolean",
            },

            "astra_escalation_reason": {
                "type": "string",
            },
        },
    }

    return make_strict_schema(
        schema
    )


# ============================================================
# PROMPT
# ============================================================


def build_prompt(
    package: dict,
) -> str:

    return f"""
You are the FINAL SENIOR RESEARCH ADJUDICATOR
for a Mechanical Engineering MSc research project.

The project concerns soft robotics,
variable-stiffness structures,
jamming mechanisms, mechanics,
modeling, and experimental validation.

This is NOT a literature extraction task.

The literature corpus has already been processed
through the following pipeline:

54 papers
→ evidence extraction
→ 9 literature reasoning batches
→ batch synthesis
→ GPT-5.6 Sol research reasoning
→ 5 candidate directions
→ Gemini adversarial review
→ shortlist

You now receive ONLY the compressed decision
package for the shortlisted directions.

Your task is to make the final provisional
decision for an MSc topic submission deadline.

The title submitted now may later be refined.


============================================================
DECISION PACKAGE
============================================================

{json.dumps(
    package,
    ensure_ascii=False,
    indent=2,
)}


============================================================
YOUR ROLE
============================================================

Independently compare the shortlisted directions.

Do NOT automatically preserve the previous
GPT-5.6 Sol recommendation.

Do NOT automatically agree with Gemini.

Re-evaluate both directions from first principles.


Evaluate:

1. Scientific importance.

2. Whether the problem represents a genuine
   mechanics / scientific question rather than
   only an implementation exercise.

3. Whether a clear causal or constitutive
   mechanism can be investigated.

4. Whether the research question can be
   falsified experimentally.

5. Whether independent and dependent variables
   are identifiable.

6. Whether the work can realistically be
   completed by an MSc student.

7. Whether modeling and experiments can be
   coherently connected.

8. Whether suitable experimental measurements
   can reasonably be obtained.

9. Whether the expected contribution could
   plausibly support a WoS/Scopus journal paper.

10. Whether the direction is overly broad.

11. Whether the direction is overly narrow
    or device-specific.

12. Whether major confounders threaten the
    scientific interpretation.

13. Whether the contribution could collapse
    into simple parameter fitting.

14. Whether a simpler existing mechanical model
    could already explain the target phenomenon.

15. Whether the proposed title overclaims novelty.


============================================================
NOVELTY RULE
============================================================

The current corpus is NOT equivalent to a
systematic Scopus/Web of Science novelty search.

Therefore:

- Never state that novelty is proven.
- Never state that no prior work exists.
- Treat novelty as provisional.
- Explicitly list what must still be searched.
- Prefer wording such as "investigation",
  "modeling", "characterization",
  "experimental validation", etc.
- Avoid title language such as "novel",
  "first", "unprecedented", unless verified later.


============================================================
TITLE REQUIREMENT
============================================================

Produce a defensible submission title in:

1. English
2. Vietnamese

The title should be specific enough to define the
mechanical problem but flexible enough to survive
later refinement after literature verification.

Avoid unnecessarily locking the thesis into a
specific constitutive law or experimental method
unless strongly justified.


============================================================
ASTRA ESCALATION RULE
============================================================

Set astra_escalation_required = true ONLY if:

- D1 and D2 remain scientifically near-equivalent,
- confidence in the selected direction is low,
- a fatal unresolved flaw exists,
- the critic and researcher evidence cannot be
  reconciled,
- or the available evidence is insufficient for
  a defensible provisional selection.

Otherwise set it to false.

Do not request Astra simply because external
novelty verification remains incomplete.
That verification is expected after submission.


============================================================
DECISION STANDARD
============================================================

For tomorrow's submission, optimize for:

scientific defensibility
+ mechanical rigor
+ experimental falsifiability
+ MSc feasibility
+ publication potential

NOT for maximum apparent novelty.

Return only the structured result required by
the output schema.
""".strip()


# ============================================================
# NORMALIZATION / VALIDATION
# ============================================================


def normalize_direction_id(
    value: str,
    valid_ids: list[str],
) -> str:

    text = str(
        value
        or ""
    ).strip()

    if text in valid_ids:
        return text

    lower = text.lower()

    matches = [
        direction_id
        for direction_id
        in valid_ids
        if direction_id.lower()
        in lower
    ]

    if len(matches) == 1:
        return matches[0]

    raise RuntimeError(
        "Could not map selected_direction "
        "to a shortlisted direction.\n"
        f"Value: {value!r}\n"
        f"Valid IDs: {valid_ids}"
    )


def validate_output(
    adjudication: dict,
    package: dict,
) -> None:

    valid_ids = [
        str(x).strip()
        for x in package[
            "shortlist"
        ]
    ]

    adjudication[
        "selected_direction"
    ] = normalize_direction_id(
        adjudication.get(
            "selected_direction",
            "",
        ),
        valid_ids,
    )

    decision = adjudication.get(
        "decision"
    )

    if decision not in {
        "select",
        "select_with_revision",
        "insufficient_confidence",
    }:
        raise RuntimeError(
            f"Invalid decision: {decision!r}"
        )

    confidence = adjudication.get(
        "confidence"
    )

    if confidence not in {
        "low",
        "medium",
        "high",
    }:
        raise RuntimeError(
            "Invalid confidence value: "
            f"{confidence!r}"
        )

    if (
        decision
        == "insufficient_confidence"
        and not adjudication.get(
            "astra_escalation_required"
        )
    ):
        raise RuntimeError(
            "Decision is insufficient_confidence "
            "but Astra escalation was not requested."
        )

    for key in [
        "final_title_en",
        "final_title_vi",
        "concise_problem_statement",
        "research_objective",
        "preliminary_research_question",
        "submission_rationale",
    ]:

        value = str(
            adjudication.get(
                key,
                "",
            )
            or ""
        ).strip()

        if not value:
            raise RuntimeError(
                f"Required field is empty: {key}"
            )


# ============================================================
# MARKDOWN
# ============================================================


def render_markdown(
    result: dict,
) -> str:

    lines = [
        "# Final MSc Research Direction Adjudication",
        "",
        "## Decision",
        "",
        (
            "**Selected direction:** "
            + result[
                "selected_direction"
            ]
        ),
        "",
        (
            "**Decision:** "
            + result[
                "decision"
            ]
        ),
        "",
        (
            "**Confidence:** "
            + result[
                "confidence"
            ]
        ),
        "",
        "## Proposed Thesis Title",
        "",
        "### English",
        "",
        result[
            "final_title_en"
        ],
        "",
        "### Vietnamese",
        "",
        result[
            "final_title_vi"
        ],
        "",
        "## Problem Statement",
        "",
        result[
            "concise_problem_statement"
        ],
        "",
        "## Research Objective",
        "",
        result[
            "research_objective"
        ],
        "",
        "## Preliminary Research Question",
        "",
        result[
            "preliminary_research_question"
        ],
        "",
        "## Scientific Hypothesis",
        "",
        result[
            "scientific_hypothesis"
        ],
        "",
        "## Why This Direction",
        "",
    ]

    for item in result[
        "why_selected_over_alternative"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.extend(
        [
            "",
            "## Expected Contribution",
            "",
        ]
    )

    for item in result[
        "expected_contribution"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.extend(
        [
            "",
            "## MSc Feasibility",
            "",
            result[
                "msc_feasibility_assessment"
            ],
            "",
            "## Publication Path",
            "",
            result[
                "publication_path"
            ],
            "",
            "## Unresolved Novelty Risks",
            "",
        ]
    )

    for item in result[
        "unresolved_novelty_risks"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.extend(
        [
            "",
            "## Required Searches After Submission",
            "",
        ]
    )

    for item in result[
        "searches_required_after_submission"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.extend(
        [
            "",
            "## Submission Rationale",
            "",
            result[
                "submission_rationale"
            ],
            "",
            "## Astra Escalation",
            "",
            (
                "**Required:** "
                + str(
                    result[
                        "astra_escalation_required"
                    ]
                )
            ),
            "",
            result[
                "astra_escalation_reason"
            ],
            "",
        ]
    )

    return "\n".join(
        lines
    )


# ============================================================
# MAIN
# ============================================================


def main() -> None:

    package = load_decision_package()

    print(
        "[SHORTLIST]",
        ", ".join(
            package[
                "shortlist"
            ]
        ),
    )

    print(
        "[SOL PREVIOUS]",
        package[
            "researcher_provisional_recommendation"
        ],
    )

    print(
        "[GEMINI CRITIC]",
        package[
            "critic_recommendation"
        ],
    )

    model = os.getenv(
        "CODEX_RESEARCH_MODEL",
        "gpt-5.6-sol",
    ).strip()

    reasoning_effort = os.getenv(
        "CODEX_RESEARCH_EFFORT",
        "high",
    ).strip()

    print(
        "[MODEL]",
        model,
    )

    print(
        "[REASONING]",
        reasoning_effort,
    )

    prompt = build_prompt(
        package
    )

    print(
        "[CODEX] Final adjudication running..."
    )

    result = call_codex(
        model=model,
        reasoning_effort=reasoning_effort,
        prompt=prompt,
        json_schema=build_schema(),
    )

    raw_content = (
        result.get(
            "content",
            "",
        )
        or ""
    ).strip()

    if not raw_content:
        raise RuntimeError(
            "Final adjudication returned "
            "empty output."
        )

    # Save expensive Sol output BEFORE parsing.
    RAW_OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    RAW_OUTPUT_PATH.write_text(
        raw_content,
        encoding="utf-8",
    )

    print(
        "[RAW SAVED]",
        RAW_OUTPUT_PATH,
    )

    try:

        adjudication = json.loads(
            raw_content
        )

    except json.JSONDecodeError as exc:

        raise RuntimeError(
            "Final adjudication returned "
            "invalid JSON.\n\n"
            f"{raw_content[:4000]}"
        ) from exc

    validate_output(
        adjudication,
        package,
    )

    output = {
        "model":
            result[
                "model"
            ],

        "usage": {
            "prompt_tokens":
                result.get(
                    "prompt_tokens",
                    0,
                ),

            "completion_tokens":
                result.get(
                    "completion_tokens",
                    0,
                ),

            "total_tokens":
                result.get(
                    "total_tokens",
                    0,
                ),

            "cached_input_tokens":
                result.get(
                    "cached_input_tokens",
                    0,
                ),

            "reasoning_output_tokens":
                result.get(
                    "reasoning_output_tokens",
                    0,
                ),
        },

        "decision_package":
            package,

        "adjudication":
            adjudication,
    }

    OUTPUT_PATH.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    MARKDOWN_PATH.write_text(
        render_markdown(
            adjudication
        ),
        encoding="utf-8",
    )

    print()
    print(
        "=" * 60
    )

    print(
        "[FINAL ADJUDICATION COMPLETE]"
    )

    print(
        "[SELECTED]",
        adjudication[
            "selected_direction"
        ],
    )

    print(
        "[DECISION]",
        adjudication[
            "decision"
        ],
    )

    print(
        "[CONFIDENCE]",
        adjudication[
            "confidence"
        ],
    )

    print(
        "[ASTRA REQUIRED]",
        adjudication[
            "astra_escalation_required"
        ],
    )

    print()
    print(
        "[TITLE EN]",
        adjudication[
            "final_title_en"
        ],
    )

    print(
        "[TITLE VI]",
        adjudication[
            "final_title_vi"
        ],
    )

    print()
    print(
        "[TOKENS]",
        f"{result.get('total_tokens', 0):,}",
    )

    print(
        "[SAVED]",
        OUTPUT_PATH,
    )

    print(
        "[SAVED]",
        MARKDOWN_PATH,
    )


if __name__ == "__main__":
    main()