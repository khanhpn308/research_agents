from app.models.gateway import ModelResult
from app.state import ResearchState


def accounting_patch(
    state: ResearchState,
    result: ModelResult,
    *,
    is_judge: bool = False,
) -> dict:

    return {
        "model_calls":
            state.get("model_calls", 0) + 1,

        "judge_calls":
            state.get("judge_calls", 0)
            + (1 if is_judge else 0),

        "prompt_tokens":
            state.get("prompt_tokens", 0)
            + result["prompt_tokens"],

        "completion_tokens":
            state.get("completion_tokens", 0)
            + result["completion_tokens"],

        "total_tokens":
            state.get("total_tokens", 0)
            + result["total_tokens"],

        "estimated_cost_usd":
            state.get("estimated_cost_usd", 0.0)
            + result["cost_usd"],
    }