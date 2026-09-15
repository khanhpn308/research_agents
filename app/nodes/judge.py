from app.accounting import accounting_patch
from app.budget import check_budget
from app.models.gateway import call_model
from app.state import ResearchState


def judge_node(
    state: ResearchState
) -> dict:

    # Judge has the strongest budget guard.
    check_budget(
        state,
        role="judge",
    )

    result = call_model(
        role="judge",
        system_prompt=(
            "You are the senior research "
            "adjudicator for a Mechanical "
            "Engineering research project. "
            "Evaluate disagreements between "
            "the researcher and the adversarial "
            "reviewer."
        ),
        user_prompt=(
            f"Research task:\n"
            f"{state['task']}\n\n"

            "Research proposal:\n"
            f"{state.get('research_proposal', '')}"
            "\n\n"

            "Adversarial critique:\n"
            f"{state.get('critique', '')}\n\n"

            "Determine whether the proposal "
            "should be:\n"
            "ACCEPTED FOR FURTHER RESEARCH,\n"
            "REVISED,\n"
            "or REJECTED.\n\n"

            "Explain the evidence and uncertainty."
        ),
    )

    return {
        "judge_result":
            result["content"],

        **accounting_patch(
            state,
            result,
            is_judge=True,
        ),
    }