import os
from typing import TypedDict

from dotenv import load_dotenv
from litellm import completion, completion_cost


load_dotenv()


ROLE_MODEL_ENV = {
    "bulk": "BULK_MODEL",
    "research": "RESEARCH_MODEL",
    "critic": "CRITIC_MODEL",
    "judge": "JUDGE_MODEL",
}


class ModelResult(TypedDict):
    content: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    cost_usd: float


def is_dry_run() -> bool:
    return os.getenv(
        "DRY_RUN",
        "true",
    ).lower() == "true"


def call_model(
    role: str,
    system_prompt: str,
    user_prompt: str,
) -> ModelResult:

    if role not in ROLE_MODEL_ENV:
        raise ValueError(
            f"Unknown model role: {role}"
        )

    model_env = ROLE_MODEL_ENV[role]

    model = os.getenv(
        model_env,
        "",
    ).strip()

    # -----------------------------------
    # DRY RUN
    # -----------------------------------
    if is_dry_run():
        return {
            "content": (
                f"[DRY_RUN]\n"
                f"ROLE={role}\n"
                f"MODEL_ENV={model_env}\n\n"
                f"SYSTEM:\n"
                f"{system_prompt}\n\n"
                f"USER INPUT:\n"
                f"{user_prompt[:1000]}"
            ),
            "model": model or model_env,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "cost_usd": 0.0,
        }

    # -----------------------------------
    # LIVE MODE
    # -----------------------------------
    if not model or model == "...":
        raise RuntimeError(
            f"{model_env} has not been configured."
        )

    response = completion(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    content = (
        response.choices[0]
        .message
        .content
        or ""
    )

    usage = getattr(
        response,
        "usage",
        None,
    )

    prompt_tokens = int(
        getattr(
            usage,
            "prompt_tokens",
            0,
        )
        or 0
    )

    completion_tokens = int(
        getattr(
            usage,
            "completion_tokens",
            0,
        )
        or 0
    )

    total_tokens = int(
        getattr(
            usage,
            "total_tokens",
            prompt_tokens + completion_tokens,
        )
        or 0
    )

    # LiteLLM cost calculator.
    # Fail safely if the model is not yet
    # present in LiteLLM's pricing database.
    try:
        cost_usd = float(
            completion_cost(
                completion_response=response
            )
            or 0.0
        )
    except Exception:
        cost_usd = 0.0

    return {
        "content": content,
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "cost_usd": cost_usd,
    }