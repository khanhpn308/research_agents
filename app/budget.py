import os

from app.state import ResearchState


def check_budget(
    state: ResearchState,
    role: str,
) -> None:

    max_tokens = int(
    os.getenv(
        "MAX_TOTAL_TOKENS_PER_RUN",
        "200000",
        )
    )

    current_tokens = state.get(
    "total_tokens",
    0,
    )

    max_calls = int(
        os.getenv(
            "MAX_MODEL_CALLS_PER_RUN",
            "8",
        )
    )

    max_judge_calls = int(
        os.getenv(
            "MAX_JUDGE_CALLS_PER_RUN",
            "1",
        )
    )

    max_cost = float(
        os.getenv(
            "MAX_RUN_COST_USD",
            "1.00",
        )
    )

    current_calls = state.get(
        "model_calls",
        0,
    )

    current_judge_calls = state.get(
        "judge_calls",
        0,
    )

    current_cost = state.get(
        "estimated_cost_usd",
        0.0,
    )

    if current_tokens >= max_tokens:
        raise RuntimeError(
            "TOKEN BUDGET EXCEEDED: "
            f"{current_tokens:,} / "
            f"{max_tokens:,}"
    )
    
    if current_calls >= max_calls:
        raise RuntimeError(
            "MODEL CALL BUDGET EXCEEDED: "
            f"{current_calls}/{max_calls}"
        )

    if current_cost >= max_cost:
        raise RuntimeError(
            "COST BUDGET EXCEEDED: "
            f"${current_cost:.4f} / "
            f"${max_cost:.4f}"
        )

    if (
        role == "judge"
        and current_judge_calls
        >= max_judge_calls
    ):
        raise RuntimeError(
            "JUDGE CALL LIMIT EXCEEDED: "
            f"{current_judge_calls}/"
            f"{max_judge_calls}"
        )