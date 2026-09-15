import hashlib
import json
import os
from pathlib import Path

from app.providers.antigravity_provider import (
    call_antigravity,
)


INPUT_PATH = Path(
    "outputs/gap_search_plan.json"
)

OUTPUT_DIR = Path(
    "outputs/search_queries"
)

OUTPUT_JSON = (
    OUTPUT_DIR
    / "database_queries.json"
)

SCOPUS_PATH = (
    OUTPUT_DIR
    / "scopus_queries.txt"
)

WOS_PATH = (
    OUTPUT_DIR
    / "wos_queries.txt"
)

SCHOLAR_PATH = (
    OUTPUT_DIR
    / "scholar_queries.txt"
)


QUERY_SCHEMA = {
    "type": "object",
    "properties": {
        "queries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "verification_id": {
                        "type": "string",
                    },
                    "priority": {
                        "type": "string",
                    },
                    "search_objective": {
                        "type": "string",
                    },
                    "concept_blocks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "concept": {
                                    "type": "string",
                                },
                                "terms": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                    },
                                },
                            },
                            "required": [
                                "concept",
                                "terms",
                            ],
                            "additionalProperties": False,
                        },
                    },
                    "scopus_query": {
                        "type": "string",
                    },
                    "wos_query": {
                        "type": "string",
                    },
                    "scholar_query": {
                        "type": "string",
                    },
                    "gap_closing_evidence": {
                        "type": "string",
                    },
                    "screening_focus": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "notes": {
                        "type": "string",
                    },
                },
                "required": [
                    "verification_id",
                    "priority",
                    "search_objective",
                    "concept_blocks",
                    "scopus_query",
                    "wos_query",
                    "scholar_query",
                    "gap_closing_evidence",
                    "screening_focus",
                    "notes",
                ],
                "additionalProperties": False,
            },
        },
    },
    "required": [
        "queries",
    ],
    "additionalProperties": False,
}


def sha256_text(
    text: str,
) -> str:

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def main() -> None:

    if not INPUT_PATH.exists():
        raise RuntimeError(
            "gap_search_plan.json not found."
        )

    source_text = INPUT_PATH.read_text(
        encoding="utf-8"
    )

    source_hash = sha256_text(
        source_text
    )

    plan = json.loads(
        source_text
    )

    searches = plan.get(
        "literature_searches",
        [],
    )

    if not searches:
        raise RuntimeError(
            "No literature searches found."
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------------
    # Cache
    # --------------------------------------------------------

    if OUTPUT_JSON.exists():

        try:
            existing = json.loads(
                OUTPUT_JSON.read_text(
                    encoding="utf-8"
                )
            )

            if (
                existing.get(
                    "source_search_plan_sha256"
                )
                == source_hash
            ):
                print(
                    "[SKIP] Database queries "
                    "already match current "
                    "search plan."
                )
                return

        except json.JSONDecodeError:
            pass

    # --------------------------------------------------------
    # Prepare compact input
    # --------------------------------------------------------

    search_input = []

    for task in searches:

        search_input.append(
            {
                "verification_id":
                    task.get(
                        "verification_id",
                        "",
                    ),

                "priority":
                    task.get(
                        "priority",
                        "",
                    ),

                "search_seed":
                    task.get(
                        "search_seed",
                        "",
                    ),

                "purpose":
                    task.get(
                        "purpose",
                        "",
                    ),

                "decision_rule":
                    task.get(
                        "decision_rule",
                        "",
                    ),
            }
        )

    model = os.getenv(
        "GEMINI_QUERY_MODEL",
        "gemini-3.8-flash-medium",
    ).strip()

    prompt = f"""
You are a scientific database search-query
compiler for Mechanical Engineering and
Soft Robotics research.

You are NOT performing the literature review.

You are converting an existing GAP
VERIFICATION PLAN into reproducible database
search queries.

Research databases:

1. Scopus
2. Web of Science Core Collection
3. Google Scholar


STRICT RULES:

1. Preserve the scientific intent of each
   verification task.

2. The goal is to FIND PRIOR WORK THAT COULD
   CLOSE OR WEAKEN THE CANDIDATE GAP.

3. Do not bias queries toward confirming the
   proposed research direction.

4. Do not invent papers, authors, DOI numbers,
   journals, or findings.

5. Convert prose statements into searchable
   technical concepts.

6. Include reasonable synonyms where useful,
   but avoid excessive query expansion.

7. Keep each query narrow enough to be
   screenable.

8. Do not assume that:
   soft gripper = continuum robot.

9. Scopus syntax:

   TITLE-ABS-KEY(
       ...
   )

10. Web of Science syntax:

   TS=(
       ...
   )

11. Google Scholar queries must be shorter
    because Scholar handles complex Boolean
    expressions poorly.

12. Do not add publication year restrictions
    yet.

13. Do not add document-type restrictions yet.

14. Search terms should emphasize mechanisms,
    models, physical phenomena, and validation
    relevant to each verification question.

15. For each query, state what kind of result
    would threaten or close the candidate gap.

16. Preserve verification_id exactly.

17. Generate exactly ONE primary Scopus query,
    ONE primary WoS query, and ONE Scholar
    query for each verification task.


GAP VERIFICATION SEARCH TASKS:

{json.dumps(
    search_input,
    indent=2,
    ensure_ascii=False,
)}
""".strip()

    result = call_antigravity(
        model=model,
        prompt=prompt,
        json_schema=QUERY_SCHEMA,
    )

    raw = (
        result.get(
            "content",
            "",
        )
        or ""
    ).strip()

    if not raw:
        raise RuntimeError(
            "Query compiler returned "
            "empty output."
        )

    try:
        compiled = json.loads(
            raw
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Query compiler returned "
            "invalid JSON."
        ) from exc

    queries = compiled.get(
        "queries",
        [],
    )

    if len(queries) != len(searches):
        raise RuntimeError(
            "Query count mismatch.\n"
            f"Expected: {len(searches)}\n"
            f"Received: {len(queries)}"
        )

    # --------------------------------------------------------
    # Validate IDs
    # --------------------------------------------------------

    expected_ids = {
        item.get(
            "verification_id"
        )
        for item in searches
    }

    returned_ids = {
        item.get(
            "verification_id"
        )
        for item in queries
    }

    if expected_ids != returned_ids:
        raise RuntimeError(
            "Verification IDs do not match "
            "the original search plan."
        )

    # --------------------------------------------------------
    # Save JSON
    # --------------------------------------------------------

    output = {
        "source_search_plan_sha256":
            source_hash,

        "model":
            result["model"],

        "usage": {
            "prompt_tokens":
                result["prompt_tokens"],

            "completion_tokens":
                result["completion_tokens"],

            "total_tokens":
                result["total_tokens"],

            "thinking_tokens":
                result["thinking_tokens"],

            "cache_read_tokens":
                result["cache_read_tokens"],
        },

        "queries":
            queries,
    }

    OUTPUT_JSON.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Human-readable database files
    # --------------------------------------------------------

    scopus_lines = []
    wos_lines = []
    scholar_lines = []

    for index, query in enumerate(
        queries,
        start=1,
    ):

        header = (
            f"SEARCH {index} | "
            f"{query['verification_id']} | "
            f"{query['priority']}"
        )

        scopus_lines.extend(
            [
                "=" * 80,
                header,
                "",
                query["search_objective"],
                "",
                query["scopus_query"],
                "",
                "Gap-closing evidence:",
                query[
                    "gap_closing_evidence"
                ],
                "",
            ]
        )

        wos_lines.extend(
            [
                "=" * 80,
                header,
                "",
                query["search_objective"],
                "",
                query["wos_query"],
                "",
                "Gap-closing evidence:",
                query[
                    "gap_closing_evidence"
                ],
                "",
            ]
        )

        scholar_lines.extend(
            [
                "=" * 80,
                header,
                "",
                query["search_objective"],
                "",
                query["scholar_query"],
                "",
                "Gap-closing evidence:",
                query[
                    "gap_closing_evidence"
                ],
                "",
            ]
        )

    SCOPUS_PATH.write_text(
        "\n".join(
            scopus_lines
        ),
        encoding="utf-8",
    )

    WOS_PATH.write_text(
        "\n".join(
            wos_lines
        ),
        encoding="utf-8",
    )

    SCHOLAR_PATH.write_text(
        "\n".join(
            scholar_lines
        ),
        encoding="utf-8",
    )

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print(
        f"[MODEL] {result['model']}"
    )

    print(
        "[QUERIES] "
        f"{len(queries)}"
    )

    print(
        "[TOKENS] "
        f"{result['total_tokens']:,}"
    )

    print(
        f"[SAVED] {OUTPUT_JSON}"
    )

    print(
        f"[SAVED] {SCOPUS_PATH}"
    )

    print(
        f"[SAVED] {WOS_PATH}"
    )

    print(
        f"[SAVED] {SCHOLAR_PATH}"
    )


if __name__ == "__main__":
    main()