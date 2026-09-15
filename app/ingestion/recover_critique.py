import json
from datetime import datetime, timezone
from pathlib import Path

from app.nodes.corpus_loader import (
    corpus_loader_node,
)
from app.nodes.critic import critic_node


RUN_DIR = Path(
    "outputs/research_runs"
)

LATEST_PATH = (
    RUN_DIR / "latest.json"
)


def main() -> None:

    if not LATEST_PATH.exists():
        raise RuntimeError(
            "latest.json not found."
        )

    run = json.loads(
        LATEST_PATH.read_text(
            encoding="utf-8"
        )
    )

    proposal = str(
        run.get(
            "research_proposal",
            "",
        )
    ).strip()

    if not proposal:
        raise RuntimeError(
            "Saved research proposal is empty."
        )

    if "[DRY_RUN]" in proposal:
        raise RuntimeError(
            "Saved proposal is DRY_RUN."
        )

    # --------------------------------------------------------
    # Reconstruct minimum state required by critic_node
    # --------------------------------------------------------

    state = {
        "task":
            run["task"],

        "research_proposal":
            proposal,

        "model_calls": 0,
        "judge_calls": 0,

        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,

        "estimated_cost_usd": 0.0,
    }

    # Load corpus locally.
    # No AI/model call happens here.
    state.update(
        corpus_loader_node(
            state
        )
    )

    print(
        "[CRITIC] Running Gemini "
        "critic only..."
    )

    # --------------------------------------------------------
    # Run ONLY critic
    # --------------------------------------------------------

    result = critic_node(
        state
    )

    critique = str(
        result.get(
            "critique",
            "",
        )
    ).strip()

    if not critique:
        raise RuntimeError(
            "Recovered critique is empty."
        )

    try:
        parsed_critique = json.loads(
            critique
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Recovered critique is not "
            "valid JSON."
        ) from exc

    new_risk = result[
        "risk_level"
    ]

    # --------------------------------------------------------
    # Update saved run
    # --------------------------------------------------------

    timestamp = datetime.now(
        timezone.utc
    ).strftime(
        "%Y%m%dT%H%M%SZ"
    )

    run["critique"] = json.dumps(
        parsed_critique,
        indent=2,
        ensure_ascii=False,
    )

    run["risk_level"] = (
        new_risk
    )

    # Previous human decision was made
    # using an invalid/empty critique.
    run["human_decision"] = None

    run["critique_recovery"] = {
        "timestamp_utc":
            timestamp,

        "reason":
            "Previous critic output was empty.",
    }

    # --------------------------------------------------------
    # Add recovered critic usage
    # --------------------------------------------------------

    usage = run.setdefault(
        "usage",
        {},
    )

    usage["model_calls"] = (
        int(
            usage.get(
                "model_calls",
                0,
            )
        )
        + int(
            result.get(
                "model_calls",
                0,
            )
        )
    )

    usage["prompt_tokens"] = (
        int(
            usage.get(
                "prompt_tokens",
                0,
            )
        )
        + int(
            result.get(
                "prompt_tokens",
                0,
            )
        )
    )

    usage["completion_tokens"] = (
        int(
            usage.get(
                "completion_tokens",
                0,
            )
        )
        + int(
            result.get(
                "completion_tokens",
                0,
            )
        )
    )

    usage["total_tokens"] = (
        int(
            usage.get(
                "total_tokens",
                0,
            )
        )
        + int(
            result.get(
                "total_tokens",
                0,
            )
        )
    )

    # --------------------------------------------------------
    # Save recovered run
    # --------------------------------------------------------

    recovered_path = (
        RUN_DIR
        / f"run_{timestamp}_recovered.json"
    )

    text = json.dumps(
        run,
        indent=2,
        ensure_ascii=False,
    )

    recovered_path.write_text(
        text,
        encoding="utf-8",
    )

    LATEST_PATH.write_text(
        text,
        encoding="utf-8",
    )

    print(
        f"[RISK] {new_risk}"
    )

    print(
        "[CRITIQUE FIELDS] "
        f"{len(parsed_critique)}"
    )

    print(
        "[CRITIC TOKENS] "
        f"{result.get('total_tokens', 0):,}"
    )

    print(
        f"[SAVED] {recovered_path}"
    )

    print(
        f"[UPDATED] {LATEST_PATH}"
    )


if __name__ == "__main__":
    main()