import json
import os

from app.accounting import accounting_patch
from app.budget import check_budget
from app.models.gateway import call_model
from app.providers.codex_provider import call_codex
from app.state import ResearchState


def researcher_node(
    state: ResearchState,
) -> dict:

    check_budget(
        state,
        role="research",
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

    if not corpus_synthesis:
        raise RuntimeError(
            "Researcher received no corpus synthesis."
        )

    if not paper_index:
        raise RuntimeError(
            "Researcher received no paper index."
        )

    live_codex = (
        os.getenv(
            "LIVE_CODEX_RESEARCH",
            "false",
        ).lower()
        == "true"
    )

    if live_codex:

        model = os.getenv(
            "CODEX_RESEARCH_MODEL",
            "gpt-5.6-sol",
        ).strip()

        effort = os.getenv(
            "CODEX_RESEARCH_EFFORT",
            "high",
        ).strip()

        researcher_schema = {
            "type": "object",
            "properties": {
                "selected_gap_signal": {
                    "type": "string",
                },
                "selected_supporting_paper_ids": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "selected_counterevidence_paper_ids": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "research_problem": {
                    "type": "string",
                },
                "candidate_gap": {
                    "type": "string",
                },
                "gap_status": {
                    "type": "string",
                    "enum": [
                        "unverified",
                        "partially_supported",
                        "not_supported",
                    ],
                },
                "gap_evidence": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "paper_id": {
                                "type": "string",
                            },
                            "doi": {
                                "type": "string",
                            },
                            "page_numbers": {
                                "type": "array",
                                "items": {
                                    "type": "integer",
                                },
                            },
                            "evidence_type": {
                                "type": "string",
                            },
                            "claim": {
                                "type": "string",
                            },
                        },
                        "required": [
                            "paper_id",
                            "doi",
                            "page_numbers",
                            "evidence_type",
                            "claim",
                        ],
                        "additionalProperties": False,
                    },
                },
                "gap_uncertainties": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "research_question": {
                    "type": "string",
                },
                "proposed_contribution": {
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
                "falsification_checks": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "required_external_searches": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
                "research_readiness": {
                    "type": "string",
                    "enum": [
                        "not_ready",
                        "needs_gap_verification",
                        "ready_for_preliminary_design",
                    ],
                },
            },
            "required": [
                "selected_gap_signal",
                "selected_supporting_paper_ids",
                "selected_counterevidence_paper_ids",
                "research_problem",
                "candidate_gap",
                "gap_status",
                "gap_evidence",
                "gap_uncertainties",
                "research_question",
                "proposed_contribution",
                "independent_variables",
                "dependent_variables",
                "control_variables",
                "performance_metrics",
                "falsification_checks",
                "required_external_searches",
                "research_readiness",
            ],
            "additionalProperties": False,
        }

        prompt = f"""
You are the senior Mechanical Engineering
researcher in a research-intensive MSc project.

RESEARCH TASK:

{task}


CORPUS SYNTHESIS:

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


STRICT SCIENTIFIC RULES:

1. Use ONLY the supplied corpus as evidence.

2. You may reason from the evidence, but do not
   introduce external literature as if it had
   been reviewed.

3. A five-paper corpus cannot establish global
   novelty.

4. "Candidate gap signal" does NOT mean a
   verified research gap.

5. Preserve paper_id, DOI, page number, and
   evidence type when using evidence.

6. Prefer author-supported evidence over
   model-inferred implications.

7. Do not convert an absence from this corpus
   into "no prior work exists".

8. Separate:
   evidence,
   inference,
   uncertainty,
   and external verification needs.

9. Select ONE strongest candidate gap signal,
   not several unrelated directions.

10. The final RQ must be narrow, measurable,
    falsifiable, and experimentally feasible.

11. Maintain alignment:

research problem
→ candidate gap
→ research question
→ variables
→ metrics
→ falsification tests.

12. If the corpus is insufficient, explicitly
    mark the research direction as not ready.

Your tasks:

A. Select the strongest candidate gap signal.

B. Identify supporting and counterevidence.

C. Formulate a defensible research problem.

D. Formulate the candidate gap WITHOUT claiming
   novelty.

E. Assign gap status:
   - unverified
   - partially_supported
   - not_supported

F. Construct one measurable research question.

G. Define variables and performance metrics.

H. Define falsification checks.

I. Specify the exact external literature
   searches required to determine whether the
   candidate gap is actually open.

J. Assign research readiness:
   - not_ready
   - needs_gap_verification
   - ready_for_preliminary_design
""".strip()

        result = call_codex(
            model=model,
            reasoning_effort=effort,
            prompt=prompt,
            json_schema=researcher_schema,
        )

        try:
            parsed = json.loads(
                result["content"]
            )

            result["content"] = json.dumps(
                parsed,
                indent=2,
                ensure_ascii=False,
            )

        except json.JSONDecodeError:
            pass

    else:

        result = call_model(
            role="research",
            system_prompt=(
                "You are a senior Mechanical "
                "Engineering researcher."
            ),
            user_prompt=(
                "Analyze the supplied corpus "
                "and formulate a candidate "
                "research direction."
            ),
        )

    return {
        "research_proposal":
            result["content"],

        **accounting_patch(
            state,
            result,
        ),
    }