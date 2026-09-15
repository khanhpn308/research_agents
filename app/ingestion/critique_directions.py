import json
import os
from pathlib import Path

from app.providers.antigravity_provider import (
    call_antigravity,
)


INPUT_PATH = Path(
    "outputs/candidate_directions.json"
)

BATCH_DIR = Path(
    "outputs/batch_syntheses"
)

RAW_OUTPUT_PATH = Path(
    "outputs/direction_critique_raw.json"
)

OUTPUT_PATH = Path(
    "outputs/direction_critique.json"
)

MARKDOWN_PATH = Path(
    "outputs/direction_critique.md"
)


VALID_VERDICTS = {
    "retain",
    "revise",
    "reject",
}

VALID_RISKS = {
    "low",
    "medium",
    "high",
}


def load_json(
    path: Path,
) -> dict:

    if not path.exists():
        raise RuntimeError(
            f"Missing file: {path}"
        )

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def load_candidate_analysis() -> dict:

    data = load_json(
        INPUT_PATH
    )

    # Current candidate_directions output
    # normally stores reasoning under "analysis".
    analysis = data.get(
        "analysis",
        data,
    )

    directions = analysis.get(
        "candidate_directions",
        [],
    )

    if not directions:
        raise RuntimeError(
            "No candidate_directions found."
        )

    return analysis


def load_batch_syntheses() -> list[dict]:

    if not BATCH_DIR.exists():
        raise RuntimeError(
            f"Missing directory: {BATCH_DIR}"
        )

    results = []

    for path in sorted(
        BATCH_DIR.glob("B*.json")
    ):

        data = load_json(
            path
        )

        synthesis = data.get(
            "synthesis",
            data,
        )

        results.append(
            {
                "source_file":
                    path.name,
                "synthesis":
                    synthesis,
            }
        )

    if not results:
        raise RuntimeError(
            "No batch synthesis files found."
        )

    return results


def build_schema() -> dict:

    review_schema = {
        "type": "object",
        "properties": {
            "direction_id": {
                "type": "string",
            },
            "scientific_gap_risk": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                ],
            },
            "novelty_risk": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                ],
            },
            "methodology_risk": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                ],
            },
            "msc_feasibility": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                ],
            },
            "publication_potential": {
                "type": "string",
                "enum": [
                    "low",
                    "medium",
                    "high",
                ],
            },
            "scientific_strengths": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "major_concerns": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "possible_prior_closure": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "missing_evidence": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "falsification_tests": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "recommended_revision": {
                "type": "string",
            },
            "verdict": {
                "type": "string",
                "enum": [
                    "retain",
                    "revise",
                    "reject",
                ],
            },
        },
        "required": [
            "direction_id",
            "scientific_gap_risk",
            "novelty_risk",
            "methodology_risk",
            "msc_feasibility",
            "publication_potential",
            "scientific_strengths",
            "major_concerns",
            "possible_prior_closure",
            "missing_evidence",
            "falsification_tests",
            "recommended_revision",
            "verdict",
        ],
        "additionalProperties": False,
    }

    schema = {
        "type": "object",
        "properties": {
            "overall_assessment": {
                "type": "string",
            },
            "direction_reviews": {
                "type": "array",
                "items":
                    review_schema,
            },
            "shortlist": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "recommended_for_submission": {
                "type": "string",
            },
            "recommendation_rationale": {
                "type": "string",
            },
            "external_search_priorities": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
            "novelty_status": {
                "type": "string",
            },
        },
        "required": [
            "overall_assessment",
            "direction_reviews",
            "shortlist",
            "recommended_for_submission",
            "recommendation_rationale",
            "external_search_priorities",
            "novelty_status",
        ],
        "additionalProperties": False,
    }

    return schema


def normalize_id(
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
        for direction_id in valid_ids
        if direction_id.lower()
        in lower
    ]

    if len(matches) == 1:
        return matches[0]

    raise RuntimeError(
        "Could not map direction ID.\n"
        f"Value: {value!r}\n"
        f"Valid IDs: {valid_ids}"
    )


def validate_output(
    result: dict,
    candidate_analysis: dict,
) -> None:

    directions = candidate_analysis[
        "candidate_directions"
    ]

    valid_ids = [
        str(
            direction[
                "direction_id"
            ]
        ).strip()
        for direction
        in directions
    ]

    reviews = result.get(
        "direction_reviews",
        [],
    )

    if not isinstance(
        reviews,
        list,
    ):
        raise RuntimeError(
            "direction_reviews must "
            "be a list."
        )

    seen = set()

    for review in reviews:

        direction_id = normalize_id(
            review.get(
                "direction_id",
                "",
            ),
            valid_ids,
        )

        review[
            "direction_id"
        ] = direction_id

        if direction_id in seen:
            raise RuntimeError(
                "Duplicate critique for "
                f"{direction_id}"
            )

        seen.add(
            direction_id
        )

        verdict = review.get(
            "verdict"
        )

        if verdict not in VALID_VERDICTS:
            raise RuntimeError(
                f"Invalid verdict: {verdict}"
            )

        for key in [
            "scientific_gap_risk",
            "novelty_risk",
            "methodology_risk",
        ]:

            if (
                review.get(key)
                not in VALID_RISKS
            ):
                raise RuntimeError(
                    f"Invalid {key}: "
                    f"{review.get(key)!r}"
                )

    missing = (
        set(valid_ids)
        - seen
    )

    if missing:
        raise RuntimeError(
            "Gemini did not review all "
            "candidate directions.\n"
            f"Missing: {sorted(missing)}"
        )

    shortlist = result.get(
        "shortlist",
        [],
    )

    normalized_shortlist = []

    for value in shortlist:

        direction_id = normalize_id(
            value,
            valid_ids,
        )

        if (
            direction_id
            not in normalized_shortlist
        ):
            normalized_shortlist.append(
                direction_id
            )

    if not normalized_shortlist:
        raise RuntimeError(
            "Critic produced an empty "
            "shortlist."
        )

    result[
        "shortlist"
    ] = normalized_shortlist

    result[
        "recommended_for_submission"
    ] = normalize_id(
        result.get(
            "recommended_for_submission",
            "",
        ),
        valid_ids,
    )

    if (
        result[
            "recommended_for_submission"
        ]
        not in normalized_shortlist
    ):
        raise RuntimeError(
            "Recommended direction is "
            "not in the shortlist."
        )


def build_prompt(
    candidate_analysis: dict,
    batch_syntheses: list[dict],
) -> str:

    return f"""
You are the adversarial research critic
for a Mechanical Engineering MSc project.

The domain is primarily:
- soft robotics
- soft grippers
- variable stiffness
- jamming mechanisms
- continuum / compliant mechanics
- modeling
- experimental validation

A GPT-5.6 Sol research agent has already
synthesized the literature corpus and
proposed five candidate research directions.

Your job is NOT to agree with that agent.

Your job is to independently attack and
stress-test every candidate direction.


============================================================
CANDIDATE RESEARCH ANALYSIS
============================================================

{json.dumps(
    candidate_analysis,
    ensure_ascii=False,
    indent=2,
)}


============================================================
SOURCE BATCH SYNTHESES
============================================================

{json.dumps(
    batch_syntheses,
    ensure_ascii=False,
    indent=2,
)}


============================================================
REVIEW TASK
============================================================

Review EVERY candidate direction.

For each direction, determine:

1. Is the proposed gap actually a
   scientific research gap?

2. Could it merely be an engineering
   implementation or parameter-tuning
   exercise?

3. Could the apparent gap already have
   been addressed by prior literature?

4. Is the research question mechanically
   meaningful and falsifiable?

5. Are the proposed dependent variables
   measurable?

6. Are important confounders or
   constitutive mechanisms missing?

7. Could a simpler mechanical model
   plausibly explain the same phenomenon?

8. Is the experimental program realistic
   for an MSc student?

9. Does the work have a plausible path
   toward a WoS/Scopus journal paper?

10. What observation would falsify the
    proposed contribution?


============================================================
IMPORTANT SCIENTIFIC RULES
============================================================

Do NOT invent:
- papers
- DOI numbers
- citations
- authors
- experiments
- numerical results

Use only the supplied corpus evidence.

If the supplied corpus does NOT establish
novelty, state that explicitly.

Distinguish carefully between:

"the corpus does not show this"

and:

"the literature has established this is false"

These are not equivalent.

Novelty must remain UNVERIFIED until an
external Scopus / Web of Science / Scholar
search is performed.

Be adversarial but technically fair.

Do not preserve an idea merely because
GPT-5.6 Sol recommended it.

Reject weak directions if justified.

Prefer a narrower, mechanically rigorous,
experimentally falsifiable MSc project
over a broad or fashionable topic.


============================================================
SHORTLIST
============================================================

After reviewing all candidates:

- shortlist only the strongest 1-2
  directions if possible
- select one provisional direction for
  tomorrow's MSc topic submission
- explain why
- identify the external searches that
  must still be performed before novelty
  can be claimed

The submitted title may later be revised,
so scientific defensibility and feasibility
are more important than perfect final wording.
""".strip()


def render_markdown(
    result: dict,
) -> str:

    lines = [
        "# Adversarial Review of Candidate Research Directions",
        "",
        "## Overall Assessment",
        "",
        result[
            "overall_assessment"
        ],
        "",
    ]

    for review in result[
        "direction_reviews"
    ]:

        lines.extend(
            [
                (
                    "## "
                    + review[
                        "direction_id"
                    ]
                ),
                "",
                (
                    "**Scientific gap risk:** "
                    + review[
                        "scientific_gap_risk"
                    ]
                ),
                "",
                (
                    "**Novelty risk:** "
                    + review[
                        "novelty_risk"
                    ]
                ),
                "",
                (
                    "**Methodology risk:** "
                    + review[
                        "methodology_risk"
                    ]
                ),
                "",
                (
                    "**MSc feasibility:** "
                    + review[
                        "msc_feasibility"
                    ]
                ),
                "",
                (
                    "**Publication potential:** "
                    + review[
                        "publication_potential"
                    ]
                ),
                "",
                (
                    "**Verdict:** "
                    + review[
                        "verdict"
                    ]
                ),
                "",
                "### Scientific strengths",
                "",
            ]
        )

        for item in review[
            "scientific_strengths"
        ]:
            lines.append(
                f"- {item}"
            )

        lines.extend(
            [
                "",
                "### Major concerns",
                "",
            ]
        )

        for item in review[
            "major_concerns"
        ]:
            lines.append(
                f"- {item}"
            )

        lines.extend(
            [
                "",
                "### Missing evidence",
                "",
            ]
        )

        for item in review[
            "missing_evidence"
        ]:
            lines.append(
                f"- {item}"
            )

        lines.extend(
            [
                "",
                "### Recommended revision",
                "",
                review[
                    "recommended_revision"
                ],
                "",
            ]
        )

    lines.extend(
        [
            "# Shortlist",
            "",
        ]
    )

    for direction_id in result[
        "shortlist"
    ]:
        lines.append(
            f"- **{direction_id}**"
        )

    lines.extend(
        [
            "",
            "# Provisional Recommendation",
            "",
            (
                "**"
                + result[
                    "recommended_for_submission"
                ]
                + "**"
            ),
            "",
            result[
                "recommendation_rationale"
            ],
            "",
            "## Novelty Status",
            "",
            result[
                "novelty_status"
            ],
            "",
            "## Required External Searches",
            "",
        ]
    )

    for item in result[
        "external_search_priorities"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.append("")

    return "\n".join(
        lines
    )


def main() -> None:

    candidate_analysis = (
        load_candidate_analysis()
    )

    batch_syntheses = (
        load_batch_syntheses()
    )

    directions = candidate_analysis[
        "candidate_directions"
    ]

    print(
        "[DIRECTIONS]",
        len(directions),
    )

    print(
        "[BATCHES]",
        len(batch_syntheses),
    )

    model = os.getenv(
        "GEMINI_CRITIC_MODEL",
        "gemini-3.8-flash-high",
    ).strip()

    print(
        "[MODEL]",
        model,
    )

    prompt = build_prompt(
        candidate_analysis,
        batch_syntheses,
    )

    print(
        "[GEMINI CRITIC] "
        "Adversarial review running..."
    )

    result = call_antigravity(
        model=model,
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
            "Gemini critic returned "
            "empty output."
        )

    # Save expensive model output
    # BEFORE parsing and validation.
    RAW_OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    RAW_OUTPUT_PATH.write_text(
        raw_content,
        encoding="utf-8",
    )

    print(
        f"[RAW SAVED] "
        f"{RAW_OUTPUT_PATH}"
    )

    try:

        critique = json.loads(
            raw_content
        )

    except json.JSONDecodeError as exc:

        raise RuntimeError(
            "Gemini critic returned "
            "invalid JSON.\n\n"
            f"{raw_content[:4000]}"
        ) from exc

    validate_output(
        critique,
        candidate_analysis,
    )

    OUTPUT_PATH.write_text(
        json.dumps(
            {
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
                },
                "critique":
                    critique,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    MARKDOWN_PATH.write_text(
        render_markdown(
            critique
        ),
        encoding="utf-8",
    )

    print()
    print(
        "=" * 60
    )
    print(
        "[ADVERSARIAL REVIEW COMPLETE]"
    )

    print(
        "[SHORTLIST]",
        ", ".join(
            critique[
                "shortlist"
            ]
        ),
    )

    print(
        "[RECOMMENDED]",
        critique[
            "recommended_for_submission"
        ],
    )

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