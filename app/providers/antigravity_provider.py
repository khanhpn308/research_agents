import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import TypedDict

from dotenv import load_dotenv


load_dotenv()


class AntigravityResult(TypedDict):
    content: str
    model: str

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    thinking_tokens: int
    cache_read_tokens: int

    conversation_id: str
    cost_usd: float


def _parse_json_output(
    stdout: str,
) -> dict:

    text = stdout.strip()

    if not text:
        raise RuntimeError(
            "Antigravity returned empty stdout."
        )

    # Normal case:
    # stdout is pure JSON.
    try:
        return json.loads(text)

    except json.JSONDecodeError:
        pass

    # Fallback:
    # Antigravity may occasionally emit
    # extra text before/after the JSON object.
    start = text.find("{")
    end = text.rfind("}")

    if (
        start != -1
        and end > start
    ):

        candidate = text[
            start:end + 1
        ]

        try:
            return json.loads(
                candidate
            )

        except json.JSONDecodeError:
            pass

    raise RuntimeError(
        "Could not parse Antigravity "
        "JSON output.\n\n"
        f"Raw output:\n{text[:3000]}"
    )


def call_antigravity(
    *,
    model: str,
    prompt: str,
    json_schema: dict | None = None,
) -> AntigravityResult:

    # ==========================================
    # Locate CLI
    # ==========================================

    agy_path = shutil.which(
        "agy"
    )

    if not agy_path:
        raise RuntimeError(
            "Antigravity CLI 'agy' "
            "was not found in PATH."
        )

    if not model:
        raise RuntimeError(
            "No Antigravity model "
            "was configured."
        )

    if not prompt.strip():
        raise RuntimeError(
            "Antigravity prompt is empty."
        )

    # ==========================================
    # Timeout
    # ==========================================

    timeout_seconds = int(
        os.getenv(
            "ANTIGRAVITY_TIMEOUT_SECONDS",
            "180",
        )
    )

    # ==========================================
    # Isolated temporary workspace
    # ==========================================
    #
    # We intentionally execute Antigravity
    # outside the research repository.
    #
    # This prevents the agent from automatically
    # inspecting or modifying source-code files.
    # ==========================================

    with tempfile.TemporaryDirectory(
        prefix="agy-research-"
    ) as workdir:

        workdir_path = Path(
            workdir
        )

        # ======================================
        # IMPORTANT:
        # DO NOT put the prompt in argv.
        #
        # OLD:
        #
        #   agy -p "<huge prompt>"
        #
        # Large papers can exceed Linux's
        # per-argument size limit.
        #
        # NEW:
        #
        #   prompt -> STDIN
        #
        # --input-format text tells agy to
        # read the prompt from stdin.
        # ======================================

        command = [
            agy_path,

            "--input-format",
            "text",

            "--model",
            model,

            "--output-format",
            "json",

            "--sandbox",
        ]

        # ======================================
        # Optional structured-output schema
        # ======================================
        #
        # Instead of putting a potentially large
        # JSON schema directly into argv,
        # store it in the temporary directory and
        # give agy the file path.
        # ======================================

        if json_schema is not None:

            schema_path = (
                workdir_path
                / "output_schema.json"
            )

            schema_path.write_text(
                json.dumps(
                    json_schema,
                    indent=2,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            command.extend(
                [
                    "--json-schema",
                    str(schema_path),
                ]
            )

        # ======================================
        # Execute
        # ======================================
        #
        # prompt is sent through stdin here.
        #
        # This is the key fix for:
        #
        # OSError:
        # [Errno 7] Argument list too long
        # ======================================

        try:

            process = subprocess.run(
                command,

                input=prompt,

                cwd=workdir,

                capture_output=True,

                text=True,

                timeout=timeout_seconds,

                check=False,
            )

        except subprocess.TimeoutExpired as exc:

            raise RuntimeError(
                "Antigravity execution "
                f"timed out after "
                f"{timeout_seconds} seconds."
            ) from exc

        except OSError as exc:

            raise RuntimeError(
                "Could not start "
                "Antigravity CLI.\n\n"
                f"Executable: {agy_path}\n"
                f"Error: {exc}"
            ) from exc

    # ==========================================
    # Process-level failure
    # ==========================================

    if process.returncode != 0:

        raise RuntimeError(
            "Antigravity execution failed."
            "\n\n"
            f"Return code: "
            f"{process.returncode}"
            "\n\n"
            f"STDOUT:\n"
            f"{process.stdout[:3000]}"
            "\n\n"
            f"STDERR:\n"
            f"{process.stderr[:3000]}"
        )

    # ==========================================
    # Parse JSON envelope
    # ==========================================

    payload = _parse_json_output(
        process.stdout
    )

    # ==========================================
    # Validate status
    # ==========================================

    status = str(
        payload.get(
            "status",
            "",
        )
    ).upper()

    if (
        status
        and status != "SUCCESS"
    ):

        raise RuntimeError(
            "Antigravity returned "
            "a non-success status: "
            f"{status}\n\n"
            f"Response:\n"
            f"{str(payload.get('response', ''))[:3000]}"
        )

    # ==========================================
    # Extract content
    # ==========================================

    structured_output = (
        payload.get(
            "structured_output"
        )
    )

    if structured_output is not None:

        content = json.dumps(
            structured_output,
            indent=2,
            ensure_ascii=False,
        )

    else:

        content = str(
            payload.get(
                "response",
                "",
            )
        ).strip()

    if not content:
        raise RuntimeError(
            "Antigravity completed successfully "
            "but returned empty content."
        )

    # ==========================================
    # Usage
    # ==========================================

    usage = payload.get(
        "usage",
        {},
    ) or {}

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

    total_tokens = int(
        usage.get(
            "total_tokens",
            0,
        )
        or (
            prompt_tokens
            + completion_tokens
        )
    )

    thinking_tokens = int(
        usage.get(
            "thinking_tokens",
            0,
        )
        or 0
    )

    cache_read_tokens = int(
        usage.get(
            "cache_read_tokens",
            0,
        )
        or 0
    )

    # ==========================================
    # Return normalized provider result
    # ==========================================

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

        "thinking_tokens":
            thinking_tokens,

        "cache_read_tokens":
            cache_read_tokens,

        "conversation_id":
            str(
                payload.get(
                    "conversation_id",
                    "",
                )
            ),

        # Antigravity is currently being used
        # through subscription quota rather than
        # pay-per-token API billing in this
        # research workflow.
        "cost_usd":
            0.0,
    }