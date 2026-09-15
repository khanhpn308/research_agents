import json
import os
import shutil
import subprocess
import tempfile
from typing import TypedDict


class CodexResult(TypedDict):
    content: str
    model: str

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    cached_input_tokens: int
    reasoning_output_tokens: int

    cost_usd: float


# ============================================================
# CODEX JSONL PARSER
# ============================================================


def _read_jsonl_events(
    stdout: str,
) -> list[dict]:

    events = []

    for line in stdout.splitlines():

        line = line.strip()

        if not line:
            continue

        try:
            event = json.loads(
                line
            )

        except json.JSONDecodeError:
            continue

        if isinstance(
            event,
            dict,
        ):
            events.append(
                event
            )

    return events


# ============================================================
# CODEX PROVIDER
# ============================================================


def call_codex(
    *,
    model: str,
    reasoning_effort: str,
    prompt: str,
    json_schema: dict | None = None,
) -> CodexResult:

    # --------------------------------------------------------
    # Validate Codex CLI
    # --------------------------------------------------------

    codex_path = shutil.which(
        "codex"
    )

    if not codex_path:
        raise RuntimeError(
            "Codex CLI was not found in PATH."
        )

    if not model:
        raise RuntimeError(
            "No Codex model was configured."
        )

    if not prompt.strip():
        raise RuntimeError(
            "Codex prompt is empty."
        )

    # --------------------------------------------------------
    # Timeout
    # --------------------------------------------------------

    timeout_seconds = int(
        os.getenv(
            "CODEX_TIMEOUT_SECONDS",
            "300",
        )
    )

    # --------------------------------------------------------
    # Temporary isolated workspace
    # --------------------------------------------------------

    with tempfile.TemporaryDirectory(
        prefix="codex-research-"
    ) as workdir:

        output_path = os.path.join(
            workdir,
            "last_message.txt",
        )

        # ----------------------------------------------------
        # Base command
        # ----------------------------------------------------

        command = [
            codex_path,
            "exec",

            "--skip-git-repo-check",

            "--ephemeral",

            "--sandbox",
            "read-only",

            "--model",
            model,

            "--config",
            (
                "model_reasoning_effort="
                f'"{reasoning_effort}"'
            ),

            "--json",

            "--output-last-message",
            output_path,
        ]

        # ----------------------------------------------------
        # Optional structured output schema
        # ----------------------------------------------------

        if json_schema is not None:

            schema_path = os.path.join(
                workdir,
                "output_schema.json",
            )

            with open(
                schema_path,
                "w",
                encoding="utf-8",
            ) as file:

                json.dump(
                    json_schema,
                    file,
                    ensure_ascii=False,
                    indent=2,
                )

            command.extend(
                [
                    "--output-schema",
                    schema_path,
                ]
            )

        # ----------------------------------------------------
        # IMPORTANT:
        #
        # DO NOT put the prompt in argv:
        #
        #     command.append(prompt)
        #
        # Large literature prompts can exceed Linux ARG_MAX
        # / per-argument limits and cause:
        #
        #     OSError: [Errno 7]
        #     Argument list too long
        #
        # "-" tells `codex exec` to read the prompt
        # from stdin instead.
        # ----------------------------------------------------

        command.append(
            "-"
        )

        # ----------------------------------------------------
        # Run Codex
        #
        # The entire prompt is transmitted through stdin.
        # It is therefore NOT part of the OS argument list.
        # ----------------------------------------------------

        try:

            process = subprocess.run(
                command,
                cwd=workdir,

                input=prompt,

                capture_output=True,
                text=True,

                timeout=timeout_seconds,

                check=False,
            )

        except subprocess.TimeoutExpired as exc:

            raise RuntimeError(
                "Codex execution timed out after "
                f"{timeout_seconds} seconds."
            ) from exc

        except OSError as exc:

            raise RuntimeError(
                "Failed to start Codex CLI.\n\n"
                f"{type(exc).__name__}: {exc}"
            ) from exc

        # ----------------------------------------------------
        # CLI failure
        # ----------------------------------------------------

        if process.returncode != 0:

            raise RuntimeError(
                "Codex execution failed.\n\n"

                f"Return code: "
                f"{process.returncode}\n\n"

                f"STDOUT:\n"
                f"{process.stdout[:4000]}\n\n"

                f"STDERR:\n"
                f"{process.stderr[:4000]}"
            )

        # ----------------------------------------------------
        # Read final model output
        # ----------------------------------------------------

        if not os.path.exists(
            output_path
        ):
            raise RuntimeError(
                "Codex did not create the "
                "last-message output file."
            )

        with open(
            output_path,
            "r",
            encoding="utf-8",
        ) as file:

            content = (
                file.read()
                .strip()
            )

        if not content:

            raise RuntimeError(
                "Codex completed successfully "
                "but returned empty content."
            )

    # ========================================================
    # USAGE ACCOUNTING
    # ========================================================

    events = _read_jsonl_events(
        process.stdout
    )

    usage = {}

    # There may theoretically be more than one completed
    # event. Use the latest one containing usage information.
    for event in events:

        if (
            event.get("type")
            == "turn.completed"
        ):

            event_usage = event.get(
                "usage",
                {},
            ) or {}

            if event_usage:
                usage = event_usage

    prompt_tokens = int(
        usage.get(
            "input_tokens",
            0,
        )
        or 0
    )

    completion_tokens = int(
        usage.get(
            "output_tokens",
            0,
        )
        or 0
    )

    cached_input_tokens = int(
        usage.get(
            "cached_input_tokens",
            0,
        )
        or 0
    )

    reasoning_output_tokens = int(
        usage.get(
            "reasoning_output_tokens",
            0,
        )
        or 0
    )

    # Prefer provider-reported total if available.
    provider_total_tokens = int(
        usage.get(
            "total_tokens",
            0,
        )
        or 0
    )

    if provider_total_tokens > 0:

        total_tokens = (
            provider_total_tokens
        )

    else:

        total_tokens = (
            prompt_tokens
            + completion_tokens
        )

    # ========================================================
    # RESULT
    # ========================================================

    return {
        "content":
            content,

        "model":
            model,

        "prompt_tokens":
            prompt_tokens,

        "completion_tokens":
            completion_tokens,

        "total_tokens":
            total_tokens,

        "cached_input_tokens":
            cached_input_tokens,

        "reasoning_output_tokens":
            reasoning_output_tokens,

        # We are using ChatGPT / Codex subscription quota,
        # not pay-per-token API billing.
        "cost_usd":
            0.0,
    }