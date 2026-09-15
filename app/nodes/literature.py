import os

from app.accounting import accounting_patch
from app.budget import check_budget
from app.models.gateway import call_model
from app.providers.antigravity_provider import (
    call_antigravity,
)
from app.state import ResearchState


def literature_node(
    state: ResearchState,
) -> dict:

    check_budget(
        state,
        role="bulk",
    )

    task = state["task"]

    live_gemini = (
        os.getenv(
            "LIVE_GEMINI_BULK",
            "false",
        ).lower()
        == "true"
    )

    if live_gemini:

        model = os.getenv(
            "GEMINI_BULK_MODEL",
            "",
        ).strip()

        prompt = f"""
You are a literature research assistant
for Mechanical Engineering research.

Research area:
soft robotics, continuum robots,
variable stiffness, mechanics,
modeling, and experimental research.

Research task:
{task}

Your job is to identify:

1. Relevant literature themes
2. Existing approaches
3. Important evidence
4. Limitations in current approaches
5. Candidate research gaps
6. What evidence would be required
   before claiming that a gap is novel

Do not invent papers, citations,
authors, DOI numbers, or evidence.

Do not claim novelty unless supported
by actual literature evidence.

This is an exploratory literature
analysis, not a final novelty claim.

Return the complete analysis directly
in the structured response.

Do not create files, reports, artifacts,
or file links.

Do not refer the user to another document.
""".strip()

        literature_schema = {
            "type": "object",
            "properties": {
                "literature_themes": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "existing_approaches": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "evidence": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "limitations": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "candidate_gaps": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "novelty_evidence_needed": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "uncertainties": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": [
                "literature_themes",
                "existing_approaches",
                "evidence",
                "limitations",
                "candidate_gaps",
                "novelty_evidence_needed",
                "uncertainties",
            ],
        }

        result = call_antigravity(
            model=model,
            prompt=prompt,
            json_schema=literature_schema,
        )

    else:

        result = call_model(
            role="bulk",
            system_prompt=(
                "You are a literature research "
                "assistant for Mechanical "
                "Engineering research. Extract "
                "evidence carefully and do not "
                "invent sources."
            ),
            user_prompt=(
                "Analyze the following research "
                "task.\n\n"
                f"{task}\n\n"
                "Identify relevant literature "
                "themes, evidence, limitations, "
                "and candidate research gaps."
            ),
        )

    return {
        "literature_summary": result["content"],
        **accounting_patch(
            state,
            result,
        ),
    }