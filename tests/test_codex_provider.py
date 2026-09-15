from app.providers.codex_provider import (
    call_codex,
)


schema = {
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
        },
        "message": {
            "type": "string",
        },
    },
    "required": [
        "status",
        "message",
    ],
    "additionalProperties": False,
}


result = call_codex(
    model="gpt-5.6-sol",
    reasoning_effort="high",
    prompt=(
        "Return status PASS and "
        "message CODEX_PROVIDER_OK."
    ),
    json_schema=schema,
)


print(
    "Content:",
    result["content"],
)

print(
    "Prompt tokens:",
    result["prompt_tokens"],
)

print(
    "Completion tokens:",
    result["completion_tokens"],
)

print(
    "Total tokens:",
    result["total_tokens"],
)

print(
    "Reasoning tokens:",
    result[
        "reasoning_output_tokens"
    ],
)