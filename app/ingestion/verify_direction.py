import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from app.providers.codex_provider import call_codex


load_dotenv()


DISCOVERY_SNAPSHOT_DIR = Path(
    "outputs/discovery_snapshot"
)

VERIFICATION_ROOT = Path(
    "outputs/verification"
)


def load_json(
    path: Path,
) -> dict:

    if not path.exists():
        raise RuntimeError(
            f"File not found: {path}"
        )

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


def build_schema() -> dict:

    citation_schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "paper_id": {
                "type": "string",
            },
            "title": {
                "type": "string",
            },
            "doi": {
                "type": "string",
            },
            "year": {
                "type": "string",
            },
            "reason": {
                "type": "string",
            },
        },
        "required": [
            "paper_id",
            "title",
            "doi",
            "year",
            "reason",
        ],
    }

    claim_schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "claim_id": {
                "type": "string",
            },
            "claim": {
                "type": "string",
            },
            "status": {
                "type": "string",
                "enum": [
                    "already_solved",
                    "partially_solved",
                    "still_open",
                    "unsupported",
                    "uncertain",
                ],
            },
            "assessment": {
                "type": "string",
            },
            "evidence": {
                "type": "array",
                "items": citation_schema,
            },
        },
        "required": [
            "claim_id",
            "claim",
            "status",
            "assessment",
            "evidence",
        ],
    }

    gap_schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "gap_id": {
                "type": "string",
            },
            "gap": {
                "type": "string",
            },
            "why_open": {
                "type": "string",
            },
            "research_value": {
                "type": "string",
            },
            "feasibility": {
                "type": "string",
                "enum": [
                    "high",
                    "medium",
                    "low",
                    "unknown",
                ],
            },
            "supporting_evidence": {
                "type": "array",
                "items": citation_schema,
            },
        },
        "required": [
            "gap_id",
            "gap",
            "why_open",
            "research_value",
            "feasibility",
            "supporting_evidence",
        ],
    }

    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "direction_id": {
                "type": "string",
            },

            "verification_id": {
                "type": "string",
            },

            "previous_title": {
                "type": "string",
            },

            "previous_decision": {
                "type": "string",
            },

            "verification_verdict": {
                "type": "string",
                "enum": [
                    "KEEP",
                    "NARROW",
                    "PIVOT",
                    "REJECT",
                ],
            },

            "confidence": {
                "type": "string",
                "enum": [
                    "high",
                    "medium",
                    "low",
                ],
            },

            "executive_assessment": {
                "type": "string",
            },

            "claim_audit": {
                "type": "array",
                "items": claim_schema,
            },

            "closest_prior_work": {
                "type": "array",
                "items": citation_schema,
            },

            "fatal_novelty_conflicts": {
                "type": "array",
                "items": citation_schema,
            },

            "remaining_open_gaps": {
                "type": "array",
                "items": gap_schema,
            },

            "recommended_title": {
                "type": "string",
            },

            "recommended_research_question": {
                "type": "string",
            },

            "recommended_contribution": {
                "type": "string",
            },

            "what_not_to_claim": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "required_next_evidence": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "stop_condition": {
                "type": "string",
            },
        },

        "required": [
            "direction_id",
            "verification_id",
            "previous_title",
            "previous_decision",
            "verification_verdict",
            "confidence",
            "executive_assessment",
            "claim_audit",
            "closest_prior_work",
            "fatal_novelty_conflicts",
            "remaining_open_gaps",
            "recommended_title",
            "recommended_research_question",
            "recommended_contribution",
            "what_not_to_claim",
            "required_next_evidence",
            "stop_condition",
        ],
    }


def compact_verification_matrix(
    matrix: dict,
) -> dict:

    papers = []

    for record in matrix.get(
        "papers",
        [],
    ):

        evidence_record = (
            record.get(
                "evidence",
                {},
            )
            or {}
        )

        paper = (
            evidence_record.get(
                "paper",
                {},
            )
            or {}
        )

        papers.append(
            {
                "paper_id":
                    record.get(
                        "paper_id",
                        "",
                    ),

                "filename":
                    record.get(
                        "filename",
                        "",
                    ),

                "title":
                    paper.get(
                        "title",
                        "",
                    ),

                "authors":
                    paper.get(
                        "authors",
                        [],
                    ),

                "year":
                    paper.get(
                        "year",
                        "",
                    ),

                "doi":
                    paper.get(
                        "doi",
                        "",
                    ),

                "robot_type":
                    paper.get(
                        "robot_type",
                        [],
                    ),

                "stiffness_mechanism":
                    paper.get(
                        "stiffness_mechanism",
                        [],
                    ),

                "actuation":
                    paper.get(
                        "actuation",
                        [],
                    ),

                "modeling_methods":
                    paper.get(
                        "modeling_methods",
                        [],
                    ),

                "performance_metrics":
                    paper.get(
                        "performance_metrics",
                        [],
                    ),

                "evidence_claims":
                    paper.get(
                        "evidence_claims",
                        [],
                    ),

                "limitations":
                    paper.get(
                        "limitations",
                        [],
                    ),

                "future_work":
                    paper.get(
                        "future_work",
                        [],
                    ),

                "gap_implications":
                    paper.get(
                        "gap_implications",
                        [],
                    ),
            }
        )

    return {
        "verification_id":
            matrix.get(
                "verification_id",
                "",
            ),

        "paper_count":
            matrix.get(
                "paper_count",
                len(papers),
            ),

        "papers":
            papers,
    }


def find_final_adjudication() -> Path:

    candidates = [
        DISCOVERY_SNAPSHOT_DIR
        / "final_adjudication.json",

        Path(
            "outputs/final_adjudication.json"
        ),
    ]

    for path in candidates:
        if path.exists():
            return path

    raise RuntimeError(
        "Could not find final_adjudication.json."
    )


def build_prompt(
    *,
    adjudication: dict,
    verification: dict,
) -> str:

    adjudication_text = json.dumps(
        adjudication,
        ensure_ascii=False,
        indent=2,
    )

    verification_text = json.dumps(
        verification,
        ensure_ascii=False,
        indent=2,
    )

    return f"""
You are performing an adversarial novelty audit of
an already-proposed mechanical-engineering research
direction.

Your objective is NOT to defend the direction.

Your objective is to determine whether independent
prior literature closes, weakens, narrows, redirects,
or leaves open the proposed research gap.

Use only the supplied evidence.

Do not invent papers, results, equations, limitations,
DOIs, or novelty claims.

Treat the previous AI recommendation as a hypothesis,
not as authoritative evidence.

A proposed research direction must be rejected or
narrowed if the supplied prior work has already
substantially solved its central scientific problem.

A difference in implementation, geometry, material,
robot platform, or experimental apparatus alone is
NOT sufficient novelty unless it creates a defensible
new mechanics question.

Distinguish carefully between:

1. phenomenon already known;
2. analytical/modeling framework already known;
3. experimental validation already done;
4. parameter regime not yet tested;
5. model assumption known to fail;
6. genuine unresolved mechanics question.

For every important judgment, cite the supplied
paper_id and bibliographic identity.

Possible final verdicts:

KEEP
- the central scientific gap survives verification.

NARROW
- the broad direction overlaps prior work, but a
  specific unresolved subproblem remains.

PIVOT
- the original core gap is largely closed, but the
  evidence reveals a materially different and more
  defensible research direction.

REJECT
- the proposed scientific contribution is already
  substantially solved and no defensible nearby gap
  is supported by the supplied evidence.

Be conservative about novelty.

If the evidence set is too small to establish novelty,
say so explicitly and list the exact next evidence
needed.

Previous discovery/adjudication:

{adjudication_text}

Independent verification corpus:

{verification_text}
""".strip()


def render_markdown(
    result: dict,
) -> str:

    lines: list[str] = []

    lines.append(
        "# Direction Verification"
    )
    lines.append("")

    lines.append(
        f"**Direction:** "
        f"{result['direction_id']}"
    )

    lines.append(
        f"**Verification round:** "
        f"{result['verification_id']}"
    )

    lines.append(
        f"**Verdict:** "
        f"{result['verification_verdict']}"
    )

    lines.append(
        f"**Confidence:** "
        f"{result['confidence']}"
    )

    lines.append("")

    lines.append(
        "## Executive Assessment"
    )
    lines.append("")

    lines.append(
        result[
            "executive_assessment"
        ]
    )

    lines.append("")

    lines.append(
        "## Claim Audit"
    )
    lines.append("")

    for claim in result[
        "claim_audit"
    ]:

        lines.append(
            f"### {claim['claim_id']} — "
            f"{claim['status']}"
        )
        lines.append("")

        lines.append(
            f"**Claim:** "
            f"{claim['claim']}"
        )
        lines.append("")

        lines.append(
            claim[
                "assessment"
            ]
        )
        lines.append("")

        for evidence in claim[
            "evidence"
        ]:

            lines.append(
                "- "
                f"`{evidence['paper_id']}` — "
                f"{evidence['title']} "
                f"({evidence['year']}) — "
                f"{evidence['reason']}"
            )

        lines.append("")

    lines.append(
        "## Closest Prior Work"
    )
    lines.append("")

    for paper in result[
        "closest_prior_work"
    ]:

        lines.append(
            "- "
            f"`{paper['paper_id']}` — "
            f"{paper['title']} "
            f"({paper['year']}) — "
            f"{paper['reason']}"
        )

    lines.append("")

    lines.append(
        "## Fatal Novelty Conflicts"
    )
    lines.append("")

    if result[
        "fatal_novelty_conflicts"
    ]:

        for paper in result[
            "fatal_novelty_conflicts"
        ]:

            lines.append(
                "- "
                f"`{paper['paper_id']}` — "
                f"{paper['title']} — "
                f"{paper['reason']}"
            )

    else:
        lines.append(
            "No fatal conflict established "
            "from the current verification set."
        )

    lines.append("")

    lines.append(
        "## Remaining Open Gaps"
    )
    lines.append("")

    for gap in result[
        "remaining_open_gaps"
    ]:

        lines.append(
            f"### {gap['gap_id']}"
        )
        lines.append("")

        lines.append(
            gap[
                "gap"
            ]
        )
        lines.append("")

        lines.append(
            f"**Why open:** "
            f"{gap['why_open']}"
        )

        lines.append(
            f"**Research value:** "
            f"{gap['research_value']}"
        )

        lines.append(
            f"**Feasibility:** "
            f"{gap['feasibility']}"
        )

        lines.append("")

    lines.append(
        "## Recommended Revision"
    )
    lines.append("")

    lines.append(
        f"**Title:** "
        f"{result['recommended_title']}"
    )
    lines.append("")

    lines.append(
        f"**Research question:** "
        f"{result['recommended_research_question']}"
    )
    lines.append("")

    lines.append(
        f"**Contribution:** "
        f"{result['recommended_contribution']}"
    )
    lines.append("")

    lines.append(
        "## What Must Not Be Claimed"
    )
    lines.append("")

    for item in result[
        "what_not_to_claim"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.append("")

    lines.append(
        "## Required Next Evidence"
    )
    lines.append("")

    for item in result[
        "required_next_evidence"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.append("")

    lines.append(
        "## Stop Condition"
    )
    lines.append("")

    lines.append(
        result[
            "stop_condition"
        ]
    )

    lines.append("")

    return "\n".join(
        lines
    )


def main() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--verification-id",
        required=True,
    )

    args = parser.parse_args()

    verification_id = (
        args.verification_id.strip()
    )

    matrix_path = (
        VERIFICATION_ROOT
        / verification_id
        / "verification_matrix.json"
    )

    matrix = load_json(
        matrix_path
    )

    adjudication_path = (
        find_final_adjudication()
    )

    adjudication = load_json(
        adjudication_path
    )

    compact_matrix = (
        compact_verification_matrix(
            matrix
        )
    )

    model = os.getenv(
        "CODEX_RESEARCH_MODEL",
        "gpt-5.6-sol",
    ).strip()

    reasoning_effort = os.getenv(
        "CODEX_RESEARCH_EFFORT",
        "high",
    ).strip()

    schema = build_schema()

    prompt = build_prompt(
        adjudication=adjudication,
        verification=compact_matrix,
    )

    output_dir = (
        VERIFICATION_ROOT
        / verification_id
    )

    prompt_path = (
        output_dir
        / "verification_prompt.txt"
    )

    prompt_path.write_text(
        prompt,
        encoding="utf-8",
    )

    print(
        f"[VERIFICATION] "
        f"{verification_id}"
    )

    print(
        f"[MODEL] {model}"
    )

    print(
        f"[REASONING] "
        f"{reasoning_effort}"
    )

    print(
        f"[PAPERS] "
        f"{compact_matrix['paper_count']}"
    )

    print(
        "[CODEX] Running adversarial "
        "direction verification..."
    )

    result = call_codex(
        model=model,
        reasoning_effort=reasoning_effort,
        prompt=prompt,
        json_schema=schema,
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
            "Codex returned empty "
            "verification output."
        )

    raw_path = (
        output_dir
        / "direction_verification_raw.json"
    )

    raw_path.write_text(
        raw_content,
        encoding="utf-8",
    )

    try:
        verification_result = (
            json.loads(
                raw_content
            )
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Codex returned invalid JSON.\n\n"
            f"{raw_content[:4000]}"
        ) from exc

    verification_result[
        "_metadata"
    ] = {
        "generated_at":
            datetime.now(
                timezone.utc
            ).isoformat(),

        "model":
            result.get(
                "model",
                model,
            ),

        "reasoning_effort":
            reasoning_effort,

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

        "verification_matrix":
            str(
                matrix_path
            ),

        "discovery_adjudication":
            str(
                adjudication_path
            ),
    }

    json_path = (
        output_dir
        / "direction_verification.json"
    )

    md_path = (
        output_dir
        / "direction_verification.md"
    )

    save_json(
        json_path,
        verification_result,
    )

    md_path.write_text(
        render_markdown(
            verification_result
        ),
        encoding="utf-8",
    )

    print()
    print(
        "=" * 60
    )

    print(
        "[DIRECTION VERIFICATION COMPLETE]"
    )

    print(
        "[VERDICT]",
        verification_result[
            "verification_verdict"
        ],
    )

    print(
        "[CONFIDENCE]",
        verification_result[
            "confidence"
        ],
    )

    print(
        "[TITLE]",
        verification_result[
            "recommended_title"
        ],
    )

    print(
        "[TOKENS]",
        result.get(
            "total_tokens",
            0,
        ),
    )

    print(
        f"[SAVED] {json_path}"
    )

    print(
        f"[SAVED] {md_path}"
    )


if __name__ == "__main__":
    main()