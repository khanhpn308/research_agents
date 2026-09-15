import json
from datetime import datetime, timezone
from pathlib import Path

from app.state import ResearchState


OUTPUT_DIR = Path(
    "outputs/research_runs"
)


def save_run_node(
    state: ResearchState,
) -> dict:

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now(
        timezone.utc
    ).strftime(
        "%Y%m%dT%H%M%SZ"
    )

    record = {
        "timestamp_utc":
            timestamp,

        "task":
            state.get("task"),

        "corpus_matrix_sha256":
            state.get(
                "corpus_matrix_sha256"
            ),

        "research_proposal":
            state.get(
                "research_proposal"
            ),

        "critique":
            state.get(
                "critique"
            ),

        "risk_level":
            state.get(
                "risk_level"
            ),

        "human_decision":
            state.get(
                "human_decision"
            ),

        "usage": {
            "model_calls":
                state.get(
                    "model_calls",
                    0,
                ),

            "judge_calls":
                state.get(
                    "judge_calls",
                    0,
                ),

            "prompt_tokens":
                state.get(
                    "prompt_tokens",
                    0,
                ),

            "completion_tokens":
                state.get(
                    "completion_tokens",
                    0,
                ),

            "total_tokens":
                state.get(
                    "total_tokens",
                    0,
                ),
        },
    }

    run_path = (
        OUTPUT_DIR
        / f"run_{timestamp}.json"
    )

    latest_path = (
        OUTPUT_DIR
        / "latest.json"
    )

    text = json.dumps(
        record,
        indent=2,
        ensure_ascii=False,
    )

    run_path.write_text(
        text,
        encoding="utf-8",
    )

    latest_path.write_text(
        text,
        encoding="utf-8",
    )

    print(
        f"[RUN SAVED] {run_path}"
    )

    return {}