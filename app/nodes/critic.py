import json
import os

from app.accounting import accounting_patch
from app.budget import check_budget
from app.models.gateway import call_model
from app.providers.antigravity_provider import (
    call_antigravity,
)
from app.state import ResearchState


VALID_RISK_LEVELS = {
    "low",
    "medium",
    "high",
}


def critic_node(
    state: ResearchState,
) -> dict:

    check_budget(
        state,
        role="critic",
    )

    task = state["task"]

    corpus_synthesis = state.get(
        "corpus_synthesis",
        {},
    )

    paper_index = state.get(
        "paper_index",
        [],
    )

    candidate_evidence = state.get(
        "candidate_evidence",
        [],
    )

    proposal = state.get(
        "research_proposal",
        "",
    )

    live_gemini = (
        os.getenv(
            "LIVE_GEMINI_CRITIC",
            "false",
        ).lower()
        == "true"
    )

    # ========================================================
    # LIVE GEMINI CRITIC
    # ========================================================

    if live_gemini:

        model = os.getenv(
            "GEMINI_CRITIC_MODEL",
            "gemini-3.8-flash-high",
        ).strip()

        critic_schema = {
            "type": "object",
            "properties": {
                "risk_level": {
                    "type": "string",
                    "enum": [
                        "low",
                        "medium",
                        "high",
                    ],
                },
                "reviewer_summary": {
                    "type": "string",
                },
                "gap_validity_concerns": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "evidence_weaknesses": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "research_question_issues": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "methodology_risks": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "confounders": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "falsification_targets": {
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
            },
            "required": [
                "risk_level",
                "reviewer_summary",
                "gap_validity_concerns",
                "evidence_weaknesses",
                "research_question_issues",
                "methodology_risks",
                "confounders",
                "falsification_targets",
                "required_next_evidence",
            ],
            "additionalProperties": False,
        }

        prompt = f"""
You are an adversarial Q1 journal reviewer
specializing in Mechanical Engineering,
Soft Robotics, continuum robots,
variable stiffness, mechanics, modeling,
and experimental validation.

Your responsibility is NOT to improve
or defend the proposal.

Your responsibility is to try to
falsify it.

ORIGINAL RESEARCH TASK:

{task}


VERIFIED CORPUS SYNTHESIS:

{json.dumps(
    corpus_synthesis,
    ensure_ascii=False,
    indent=2,
)}


PAPER INDEX:

{json.dumps(
    paper_index,
    ensure_ascii=False,
    indent=2,
)}


SOURCE-TRACEABLE EVIDENCE:

{json.dumps(
    candidate_evidence,
    ensure_ascii=False,
    indent=2,
)}


RESEARCHER PROPOSAL:

{proposal}


Critically evaluate the proposal.

You must investigate the following:

1. Could the proposed research gap
   already have been closed?

2. Is the candidate gap actually a
   scientific gap, or merely an
   engineering implementation challenge?

3. Is the research question measurable
   and falsifiable?

4. Does the proposed methodology
   logically answer the research question?

5. Are important physical mechanisms,
   variables, or confounders missing?

6. Could a simpler existing model
   explain the same observations?

7. Could apparent improvements arise
   from calibration, overfitting,
   parameter tuning, or measurement error?

8. Are the claimed contributions
   genuinely distinct from incremental
   parameter refinement?

9. What evidence would falsify the
   proposed research direction?

10. What evidence must be collected
    before this candidate gap should
    be accepted for MSc research?


IMPORTANT RULES:

- Do not invent papers, authors,
  citations, DOI numbers, or experiments.

- Distinguish clearly between:
  "not supported by current evidence"
  and
  "known to be false".

- Treat all novelty claims as unverified.

- Be adversarial, but technically fair.

- Prefer rejecting a weak gap over
  protecting the researcher's idea.

- Return the complete critique directly
  in the structured response.

- Do not create files, reports,
  artifacts, or file links.

- Keep each array concise:
  maximum 5 items per array.

- Each item should contain only the
  information needed to evaluate or
  falsify the candidate gap.


Assign risk as follows:

LOW:
The gap is reasonably well supported,
testable, and internally aligned.
Only normal validation work remains.

MEDIUM:
The direction is plausible but important
literature, modeling, or experimental
evidence is still missing.

HIGH:
The gap may already be closed,
the RQ is poorly testable,
the methodology cannot answer it,
or major assumptions threaten the
validity of the whole direction.
""".strip()

        result = call_antigravity(
            model=model,
            prompt=prompt,
            json_schema=critic_schema,
        )

        # ----------------------------------------------------
        # Validate Gemini output
        # ----------------------------------------------------

        raw_content = (
            result.get(
                "content",
                "",
            )
            or ""
        ).strip()

        if not raw_content:
            raise RuntimeError(
                "Gemini Critic returned EMPTY output.\n"
                "The run must not continue because "
                "risk cannot be determined reliably."
            )

        try:
            parsed = json.loads(
                raw_content
            )

        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "Gemini Critic returned invalid JSON.\n\n"
                f"Raw output:\n{raw_content[:3000]}"
            ) from exc

        risk = str(
            parsed.get(
                "risk_level",
                "",
            )
        ).lower()

        if risk not in VALID_RISK_LEVELS:
            raise RuntimeError(
                "Gemini Critic returned an invalid "
                f"risk level: {risk!r}"
            )

        result["content"] = json.dumps(
            parsed,
            indent=2,
            ensure_ascii=False,
        )

    # ========================================================
    # DRY-RUN / FALLBACK CRITIC
    # ========================================================

    else:

        result = call_model(
            role="critic",

            system_prompt=(
                "You are an adversarial Q1 "
                "journal reviewer in Mechanical "
                "Engineering and Soft Robotics. "
                "Your job is to find weaknesses "
                "rather than agree with the "
                "proposed research direction."
            ),

            user_prompt=(
                "Evaluate this proposal "
                "critically.\n\n"
                f"{proposal}\n\n"
                "Check whether the research gap "
                "may already be closed, whether "
                "the research question is "
                "measurable, whether the "
                "contribution is incremental, "
                "and whether the methodology "
                "can answer the question."
            ),
        )

        risk = os.getenv(
            "DRY_RUN_RISK",
            "high",
        ).lower()

        if risk not in VALID_RISK_LEVELS:
            risk = "high"

    # ========================================================
    # NODE OUTPUT
    # ========================================================

    return {
        "critique":
            result["content"],

        "risk_level":
            risk,

        **accounting_patch(
            state,
            result,
        ),
    }