from langgraph.types import interrupt

from app.state import ResearchState


def approval_node(state: ResearchState) -> dict:
    decision = interrupt(
        {
            "message": "HIGH-RISK RESEARCH DECISION",
            "risk_level": state.get("risk_level"),
            "question": (
                "Authorize the expensive senior judge model "
                "(GPT-6 Astra)?"
            ),
            "options": {
                "yes": "Authorize Astra",
                "no": "Stop without Astra",
            },
        }
    )

    normalized = str(decision).strip().lower()

    if normalized in {"y", "yes", "approve"}:
        return {"human_decision": "approved"}

    return {"human_decision": "rejected"}