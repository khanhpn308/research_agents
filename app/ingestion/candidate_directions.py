import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from app.providers.codex_provider import call_codex


load_dotenv()


BATCH_SYNTHESIS_DIR = Path(
    "outputs/batch_syntheses"
)

REASONING_BATCH_DIR = Path(
    "outputs/reasoning_batches"
)

OUTPUT_PATH = Path(
    "outputs/candidate_directions.json"
)

MARKDOWN_PATH = Path(
    "outputs/candidate_directions.md"
)


# ============================================================
# BASIC UTILITIES
# ============================================================


def read_json(
    path: Path,
) -> dict:

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def canonical_json(
    data: Any,
) -> str:

    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def sha256_text(
    text: str,
) -> str:

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


# ============================================================
# LOAD 9 BATCH SYNTHESES
# ============================================================


def load_batch_syntheses() -> list[dict]:

    files = sorted(
        BATCH_SYNTHESIS_DIR.glob(
            "B*.json"
        )
    )

    if len(files) != 9:
        raise RuntimeError(
            "Expected exactly 9 batch "
            f"syntheses, found {len(files)}."
        )

    syntheses = []

    for path in files:

        data = read_json(
            path
        )

        synthesis = data.get(
            "synthesis"
        )

        if not isinstance(
            synthesis,
            dict,
        ):
            raise RuntimeError(
                f"{path} does not contain "
                "a valid synthesis object."
            )

        syntheses.append(
            synthesis
        )

    return syntheses


# ============================================================
# FIND PAPER METADATA RECURSIVELY
# ============================================================


def find_paper_records(
    value: Any,
) -> list[dict]:

    records = []

    if isinstance(
        value,
        dict,
    ):

        if (
            "paper_id" in value
            and "title" in value
        ):
            records.append(
                value
            )

        for child in value.values():
            records.extend(
                find_paper_records(
                    child
                )
            )

    elif isinstance(
        value,
        list,
    ):

        for child in value:
            records.extend(
                find_paper_records(
                    child
                )
            )

    return records


def load_paper_catalog() -> list[dict]:

    files = sorted(
        REASONING_BATCH_DIR.glob(
            "batch_*.json"
        )
    )

    if not files:
        raise RuntimeError(
            "No reasoning batch files found."
        )

    papers_by_id = {}

    for path in files:

        data = read_json(
            path
        )

        records = find_paper_records(
            data
        )

        for record in records:

            paper_id = str(
                record.get(
                    "paper_id",
                    "",
                )
            ).strip()

            if not paper_id:
                continue

            if paper_id in papers_by_id:
                continue

            papers_by_id[
                paper_id
            ] = {
                "paper_id":
                    paper_id,

                "title":
                    record.get(
                        "title",
                        "",
                    ),

                "authors":
                    record.get(
                        "authors",
                        [],
                    ),

                "year":
                    record.get(
                        "year",
                    ),

                "doi":
                    record.get(
                        "doi",
                        "",
                    ),
            }

    if not papers_by_id:
        raise RuntimeError(
            "Could not recover paper IDs "
            "from reasoning batches."
        )

    return sorted(
        papers_by_id.values(),
        key=lambda x: x["paper_id"],
    )


# ============================================================
# CODEX OUTPUT SCHEMA
# ============================================================

def make_strict_schema(
    schema,
):
    """
    Recursively convert a JSON schema into the
    strict object form required by OpenAI
    Structured Outputs.

    Every object must:
    - set additionalProperties=False
    - explicitly require all declared properties
    """

    if isinstance(
        schema,
        dict,
    ):

        if (
            schema.get("type")
            == "object"
        ):

            schema[
                "additionalProperties"
            ] = False

            properties = schema.get(
                "properties",
                {},
            )

            if properties:
                schema["required"] = list(
                    properties.keys()
                )

        for value in schema.values():
            make_strict_schema(
                value
            )

    elif isinstance(
        schema,
        list,
    ):

        for value in schema:
            make_strict_schema(
                value
            )

    return schema

def build_schema() -> dict:

    direction_schema = {
        "type": "object",

        "properties": {

            "direction_id": {
                "type": "string",
            },

            "title_en": {
                "type": "string",
            },

            "title_vi": {
                "type": "string",
            },

            "research_problem": {
                "type": "string",
            },

            "candidate_gap": {
                "type": "string",
            },

            "research_question": {
                "type": "string",
            },

            "mechanism_scope": {
                "type": "string",
            },

            "modeling_approach": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "experimental_validation": {
                "type": "array",
                "items": {
                    "type": "string",
                },
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

            "supporting_paper_ids": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "supporting_evidence_summary": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "novelty_uncertainties": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "falsification_conditions": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "main_risks": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "msc_feasibility": {
                "type": "string",
                "enum": [
                    "high",
                    "medium",
                    "low",
                ],
            },

            "msc_feasibility_reason": {
                "type": "string",
            },

            "novelty_confidence": {
                "type": "string",
                "enum": [
                    "high",
                    "medium",
                    "low",
                    "unverified",
                ],
            },

            "why_worth_investigating": {
                "type": "string",
            },
        },

        "required": [
            "direction_id",
            "title_en",
            "title_vi",
            "research_problem",
            "candidate_gap",
            "research_question",
            "mechanism_scope",
            "modeling_approach",
            "experimental_validation",
            "independent_variables",
            "dependent_variables",
            "control_variables",
            "performance_metrics",
            "supporting_paper_ids",
            "supporting_evidence_summary",
            "novelty_uncertainties",
            "falsification_conditions",
            "main_risks",
            "msc_feasibility",
            "msc_feasibility_reason",
            "novelty_confidence",
            "why_worth_investigating",
        ],
    }

    schema = {
        "type": "object",

        "properties": {

            "corpus_assessment": {
                "type": "string",
            },

            "cross_batch_consensus": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "cross_batch_conflicts": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "candidate_directions": {
                "type": "array",
                "minItems": 3,
                "maxItems": 5,
                "items":
                    direction_schema,
            },

            "ranking": {
                "type": "array",
                "items": {
                    "type": "object",

                    "properties": {

                        "direction_id": {
                            "type":
                                "string",
                        },

                        "rank": {
                            "type":
                                "integer",
                        },

                        "reason": {
                            "type":
                                "string",
                        },
                    },

                    "required": [
                        "direction_id",
                        "rank",
                        "reason",
                    ],
                },
            },

            "provisional_recommendation": {
                "type": "string",
            },

            "recommendation_reason": {
                "type": "string",
            },

            "critical_missing_literature": {
                "type": "array",
                "items": {
                    "type":
                        "string",
                },
            },

            "next_validation_steps": {
                "type": "array",
                "items": {
                    "type":
                        "string",
                },
            },
        },

        "required": [
            "corpus_assessment",
            "cross_batch_consensus",
            "cross_batch_conflicts",
            "candidate_directions",
            "ranking",
            "provisional_recommendation",
            "recommendation_reason",
            "critical_missing_literature",
            "next_validation_steps",
        ],
    }
    return make_strict_schema(
    schema
)


# ============================================================
# PROMPT
# ============================================================


def build_prompt(
    syntheses: list[dict],
    paper_catalog: list[dict],
) -> str:

    return f"""
You are the senior research reasoning agent
for an MSc Mechanical Engineering project.

Domain focus:

- soft robotics
- soft grippers
- continuum robots
- variable stiffness
- jamming
- tendon-driven systems
- smart materials
- mechanics
- constitutive modeling
- experimental validation


YOUR TASK

Perform CROSS-BATCH reasoning over nine
independently synthesized literature batches.

The goal is NOT to generate as many research
ideas as possible.

The goal is to reduce the available evidence
to only 3-5 scientifically defensible candidate
research directions suitable for an MSc thesis.


VERY IMPORTANT

The student needs to submit a provisional
research topic very soon.

However, scientific rigor must not be sacrificed.

A provisional topic may later be refined,
but it must be:

1. grounded in the supplied literature,
2. mechanically meaningful,
3. experimentally testable,
4. feasible for an MSc project,
5. sufficiently specific to guide further
   literature verification,
6. not falsely presented as novel.


EVIDENCE RULES

You may use ONLY the information contained in:

- the supplied batch syntheses,
- the supplied paper catalog.

Do not invent:

- papers,
- authors,
- DOI numbers,
- experimental findings,
- literature gaps,
- novelty claims.

A statement such as:

"the literature proves nobody has done X"

is NOT acceptable unless the supplied evidence
actually establishes it.

Instead use language such as:

"the current corpus suggests...",
"this remains a candidate gap...",
"novelty requires external verification..."


SOURCE TRACEABILITY

Every candidate direction must include
supporting_paper_ids.

Those IDs MUST exist in the supplied
paper catalog.

Do not invent paper IDs.


CROSS-BATCH REASONING

Look for repeated patterns across batches.

Distinguish:

A. Established evidence
B. Repeated limitations
C. Candidate gaps
D. Contradictions between papers
E. Engineering implementation problems
F. Genuine scientific/modeling questions


Especially reject or downgrade directions where:

- the apparent gap is simply poor engineering,
- the contribution is only parameter tuning,
- an existing simpler model may already solve it,
- the proposed variables cannot be measured,
- validation would require unrealistic equipment,
- the mechanism scope is too broad,
- novelty depends entirely on the absence of papers
  not represented in this corpus.


MECHANICAL ENGINEERING PRIORITY

Prefer directions containing a defensible
mechanics contribution such as:

- stiffness modeling,
- constitutive relationships,
- deformation mechanics,
- force transmission,
- hysteresis,
- friction,
- contact,
- strain-energy behavior,
- dynamic response,
- variable-stiffness transitions,
- model-experiment validation.

Do not prioritize a direction merely because
it sounds technologically impressive.


MSc FEASIBILITY

Assess whether each direction could reasonably
be executed through some combination of:

- analytical modeling,
- MATLAB simulation,
- SolidWorks design,
- finite-element modeling where justified,
- prototype fabrication,
- benchtop mechanical experiments,
- force/displacement measurement,
- stiffness characterization.

Avoid requiring highly specialized facilities
unless clearly justified.


RESEARCH QUESTION QUALITY

Each research question should identify,
as far as possible:

- physical system,
- independent variable(s),
- measurable response(s),
- comparison/baseline,
- operating conditions,
- falsifiable outcome.


TITLE RULES

Generate both:

title_en
title_vi

The titles are PROVISIONAL thesis titles.

They should:

- sound academically professional,
- be broad enough to survive later refinement,
- not claim unverified novelty,
- avoid phrases such as
  "novel",
  "first ever",
  "breakthrough"
  unless conclusively established.

Prefer titles such as:

"Modeling and Experimental Investigation of..."

"Design and Mechanical Characterization of..."

"Investigation of..."

rather than overstated novelty claims.


IMPORTANT DISTINCTION

A candidate gap is NOT an accepted research gap.

Novelty must remain marked as uncertain
until external database verification has been
performed against Scopus / Web of Science /
Google Scholar and relevant citation chains.


============================================================
PAPER CATALOG
============================================================

{json.dumps(
    paper_catalog,
    indent=2,
    ensure_ascii=False,
)}


============================================================
NINE BATCH SYNTHESES
============================================================

{json.dumps(
    syntheses,
    indent=2,
    ensure_ascii=False,
)}


Produce 3-5 candidate directions.

Rank them.

Your ranking should emphasize:

1. scientific significance,
2. evidence support,
3. mechanical-engineering depth,
4. testability,
5. MSc feasibility,
6. risk that prior work already closes the gap.

The provisional recommendation is NOT a final
novelty determination.

It will subsequently be challenged by an
independent adversarial reviewer.
""".strip()


# ============================================================
# VALIDATION
# ============================================================


def validate_output(
    output: dict,
    valid_paper_ids: set[str],
) -> None:

    directions = output.get(
        "candidate_directions",
        []
    )

    if not (
        3 <= len(directions) <= 5
    ):
        raise RuntimeError(
            "Expected 3-5 candidate "
            "directions."
        )

    direction_ids = []

    for direction in directions:

        direction_id = str(
            direction.get(
                "direction_id",
                "",
            )
        ).strip()

        if not direction_id:
            raise RuntimeError(
                "A candidate direction "
                "has no direction_id."
            )

        direction_ids.append(
            direction_id
        )

        paper_ids = direction.get(
            "supporting_paper_ids",
            []
        )

        if not paper_ids:
            raise RuntimeError(
                f"{direction_id} has no "
                "supporting paper IDs."
            )

        invalid_ids = [
            paper_id
            for paper_id in paper_ids
            if paper_id
            not in valid_paper_ids
        ]

        if invalid_ids:
            raise RuntimeError(
                f"{direction_id} contains "
                "invented or unknown paper IDs: "
                f"{invalid_ids}"
            )

    if len(
        set(direction_ids)
    ) != len(direction_ids):
        raise RuntimeError(
            "Duplicate direction IDs found."
        )

        # ========================================================
    # NORMALIZE PROVISIONAL RECOMMENDATION
    # ========================================================

    recommendation = str(
        output.get(
            "provisional_recommendation",
            "",
        )
        or ""
    ).strip()

    valid_direction_ids = set(
        direction_ids
    )

    # --------------------------------------------------------
    # Case 1:
    # Model already returned a clean direction ID.
    #
    # Example:
    #     D1
    # --------------------------------------------------------

    if recommendation in valid_direction_ids:
        return

    # --------------------------------------------------------
    # Case 2:
    # Model embedded the direction ID inside a longer string.
    #
    # Examples:
    #     "D2 — Modeling and Experimental..."
    #     "Recommended direction: D2"
    # --------------------------------------------------------

    recommendation_lower = (
        recommendation.lower()
    )

    matched_ids = [
        direction_id
        for direction_id
        in direction_ids
        if (
            direction_id.lower()
            in recommendation_lower
        )
    ]

    if len(matched_ids) == 1:

        output[
            "provisional_recommendation"
        ] = matched_ids[0]

        return

    # --------------------------------------------------------
    # Case 3:
    # Model returned the title instead of the ID.
    #
    # Try exact matching against English/Vietnamese title.
    # --------------------------------------------------------

    for direction in directions:

        direction_id = str(
            direction.get(
                "direction_id",
                "",
            )
        ).strip()

        title_en = str(
            direction.get(
                "title_en",
                "",
            )
            or ""
        ).strip()

        title_vi = str(
            direction.get(
                "title_vi",
                "",
            )
            or ""
        ).strip()

        if (
            recommendation
            and (
                recommendation_lower
                == title_en.lower()
                or
                recommendation_lower
                == title_vi.lower()
            )
        ):

            output[
                "provisional_recommendation"
            ] = direction_id

            return

    # --------------------------------------------------------
    # Case 4:
    # Use ranking ONLY if the model itself explicitly ranked
    # one valid direction as rank 1.
    #
    # This is not inventing a recommendation:
    # it recovers the model's own top-ranked candidate.
    # --------------------------------------------------------

    ranking = output.get(
        "ranking",
        [],
    )

    rank_one = []

    if isinstance(
        ranking,
        list,
    ):

        for item in ranking:

            if not isinstance(
                item,
                dict,
            ):
                continue

            direction_id = str(
                item.get(
                    "direction_id",
                    "",
                )
            ).strip()

            rank = item.get(
                "rank"
            )

            if (
                direction_id
                in valid_direction_ids
                and rank == 1
            ):

                rank_one.append(
                    direction_id
                )

    if len(rank_one) == 1:

        output[
            "provisional_recommendation"
        ] = rank_one[0]

        return

    # --------------------------------------------------------
    # Fail closed.
    #
    # We do NOT guess a recommendation if the output cannot
    # be mapped reliably.
    # --------------------------------------------------------

    raise RuntimeError(
        "Could not reliably map "
        "provisional_recommendation "
        "to a valid direction_id.\n\n"
        f"Raw recommendation: "
        f"{recommendation!r}\n"
        f"Valid direction IDs: "
        f"{direction_ids}\n"
        f"Rank-1 candidates: "
        f"{rank_one}"
    )


# ============================================================
# MARKDOWN REPORT
# ============================================================


def write_markdown(
    output: dict,
) -> None:

    lines = [
        "# Candidate Research Directions",
        "",
        "## Corpus Assessment",
        "",
        output.get(
            "corpus_assessment",
            "",
        ),
        "",
    ]

    directions = output.get(
        "candidate_directions",
        []
    )

    for direction in directions:

        lines.extend(
            [
                (
                    "## "
                    f"{direction['direction_id']} — "
                    f"{direction['title_en']}"
                ),
                "",
                (
                    "**Vietnamese title:** "
                    f"{direction['title_vi']}"
                ),
                "",
                "### Research problem",
                "",
                direction[
                    "research_problem"
                ],
                "",
                "### Candidate gap",
                "",
                direction[
                    "candidate_gap"
                ],
                "",
                "### Research question",
                "",
                direction[
                    "research_question"
                ],
                "",
                (
                    "**MSc feasibility:** "
                    f"{direction['msc_feasibility']}"
                ),
                "",
                direction[
                    "msc_feasibility_reason"
                ],
                "",
                (
                    "**Novelty confidence:** "
                    f"{direction['novelty_confidence']}"
                ),
                "",
                "### Supporting papers",
                "",
            ]
        )

        for paper_id in direction[
            "supporting_paper_ids"
        ]:
            lines.append(
                f"- `{paper_id}`"
            )

        lines.extend(
            [
                "",
                "### Main risks",
                "",
            ]
        )

        for risk in direction[
            "main_risks"
        ]:
            lines.append(
                f"- {risk}"
            )

        lines.append("")

    lines.extend(
        [
            "## Provisional Recommendation",
            "",
            (
                "**"
                f"{output['provisional_recommendation']}"
                "**"
            ),
            "",
            output[
                "recommendation_reason"
            ],
            "",
            (
                "> This recommendation is "
                "provisional. Novelty has not "
                "yet been established by an "
                "external database search."
            ),
            "",
        ]
    )

    MARKDOWN_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )


# ============================================================
# MAIN
# ============================================================


def main() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--force",
        action="store_true",
    )

    args = parser.parse_args()

    model = os.getenv(
        "CODEX_RESEARCH_MODEL",
        "gpt-5.6-sol",
    ).strip()

    reasoning_effort = os.getenv(
        "CODEX_RESEARCH_EFFORT",
        "high",
    ).strip()

    syntheses = load_batch_syntheses()

    paper_catalog = load_paper_catalog()

    valid_paper_ids = {
        paper["paper_id"]
        for paper in paper_catalog
    }

    source_payload = {
        "model":
            model,

        "reasoning_effort":
            reasoning_effort,

        "paper_catalog":
            paper_catalog,

        "batch_syntheses":
            syntheses,
    }

    source_sha256 = sha256_text(
        canonical_json(
            source_payload
        )
    )

    if (
        OUTPUT_PATH.exists()
        and not args.force
    ):

        existing = read_json(
            OUTPUT_PATH
        )

        if (
            existing.get(
                "source_sha256"
            )
            == source_sha256
        ):
            print(
                "[SKIP] Candidate directions "
                "already match current inputs."
            )

            return

    print(
        f"[MODEL] {model}"
    )

    print(
        f"[REASONING] {reasoning_effort}"
    )

    print(
        f"[BATCHES] {len(syntheses)}"
    )

    print(
        f"[PAPERS] {len(paper_catalog)}"
    )

    prompt = build_prompt(
        syntheses,
        paper_catalog,
    )

    print(
        "[CODEX] Running cross-batch "
        "research reasoning..."
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
            "GPT-5.6 Sol returned empty "
            "cross-batch reasoning output."
        )
    raw_output_path = Path(
    "outputs/candidate_directions_raw.json"
    )

    raw_output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    raw_output_path.write_text(
        raw_content,
        encoding="utf-8",
    )

    print(
        f"[RAW SAVED] {raw_output_path}"
    )
    try:
        reasoning = json.loads(
            raw_content
        )
    

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "GPT-5.6 Sol returned "
            "invalid JSON.\n\n"
            f"{raw_content[:4000]}"
        ) from exc

    validate_output(
        reasoning,
        valid_paper_ids,
    )

    record = {
        "source_sha256":
            source_sha256,

        "model":
            result.get(
                "model",
                model,
            ),

        "reasoning_effort":
            reasoning_effort,

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

        "analysis":
            reasoning,
    }

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_PATH.write_text(
        json.dumps(
            record,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    write_markdown(
        reasoning
    )

    print()
    print("=" * 60)
    print("[CROSS-BATCH REASONING COMPLETE]")

    print(
        "[DIRECTIONS] "
        f"{len(reasoning['candidate_directions'])}"
    )

    print(
        "[RECOMMENDED] "
        f"{reasoning['provisional_recommendation']}"
    )

    print(
        "[TOKENS] "
        f"{result.get('total_tokens', 0):,}"
    )

    print(
        f"[SAVED] {OUTPUT_PATH}"
    )

    print(
        f"[SAVED] {MARKDOWN_PATH}"
    )


if __name__ == "__main__":
    main()