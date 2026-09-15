import argparse
import hashlib
import json
import os
from pathlib import Path

from app.providers.antigravity_provider import (
    call_antigravity,
)


BATCH_DIR = Path(
    "outputs/reasoning_batches"
)

MANIFEST_PATH = (
    BATCH_DIR / "manifest.json"
)

OUTPUT_DIR = Path(
    "outputs/batch_syntheses"
)


def sha256_file(
    path: Path,
) -> str:

    hasher = hashlib.sha256()

    with path.open("rb") as file:
        while chunk := file.read(
            1024 * 1024
        ):
            hasher.update(chunk)

    return hasher.hexdigest()


def load_json(
    path: Path,
) -> dict:

    if not path.exists():
        raise RuntimeError(
            f"Missing file: {path}"
        )

    try:
        return json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Invalid JSON: {path}"
        ) from exc


def build_schema() -> dict:

    return {
        "type": "object",

        "properties": {

            "batch_id": {
                "type": "string",
            },

            "research_domains": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "mechanisms": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "modeling_approaches": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },

            "established_findings": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {
                        "finding": {
                            "type": "string",
                        },

                        "paper_ids": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },

                        "strength": {
                            "type": "string",
                            "enum": [
                                "strong",
                                "moderate",
                                "weak",
                            ],
                        },
                    },

                    "required": [
                        "finding",
                        "paper_ids",
                        "strength",
                    ],
                },
            },

            "limitations_across_papers": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {
                        "limitation": {
                            "type": "string",
                        },

                        "paper_ids": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },
                    },

                    "required": [
                        "limitation",
                        "paper_ids",
                    ],
                },
            },

            "contradictions": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {
                        "issue": {
                            "type": "string",
                        },

                        "paper_ids": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },

                        "interpretation": {
                            "type": "string",
                        },
                    },

                    "required": [
                        "issue",
                        "paper_ids",
                        "interpretation",
                    ],
                },
            },

            "candidate_gaps": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {

                        "gap": {
                            "type": "string",
                        },

                        "supporting_paper_ids": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },

                        "why_it_may_be_a_gap": {
                            "type": "string",
                        },

                        "closure_risk": {
                            "type": "string",
                            "enum": [
                                "low",
                                "medium",
                                "high",
                            ],
                        },

                        "external_verification_needed": {
                            "type": "boolean",
                        },
                    },

                    "required": [
                        "gap",
                        "supporting_paper_ids",
                        "why_it_may_be_a_gap",
                        "closure_risk",
                        "external_verification_needed",
                    ],
                },
            },

            "candidate_research_questions": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {

                        "question": {
                            "type": "string",
                        },

                        "related_gap": {
                            "type": "string",
                        },

                        "measurable": {
                            "type": "boolean",
                        },

                        "main_variables": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },
                    },

                    "required": [
                        "question",
                        "related_gap",
                        "measurable",
                        "main_variables",
                    ],
                },
            },

            "promising_research_directions": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {

                        "direction": {
                            "type": "string",
                        },

                        "rationale": {
                            "type": "string",
                        },

                        "paper_ids": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },

                        "novelty_status": {
                            "type": "string",
                            "enum": [
                                "unverified",
                                "partially_supported",
                                "unlikely",
                            ],
                        },

                        "msc_feasibility": {
                            "type": "string",
                            "enum": [
                                "high",
                                "medium",
                                "low",
                            ],
                        },
                    },

                    "required": [
                        "direction",
                        "rationale",
                        "paper_ids",
                        "novelty_status",
                        "msc_feasibility",
                    ],
                },
            },

            "priority_papers": {
                "type": "array",

                "items": {
                    "type": "object",

                    "properties": {
                        "paper_id": {
                            "type": "string",
                        },

                        "reason": {
                            "type": "string",
                        },
                    },

                    "required": [
                        "paper_id",
                        "reason",
                    ],
                },
            },

            "unresolved_questions": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
        },

        "required": [
            "batch_id",
            "research_domains",
            "mechanisms",
            "modeling_approaches",
            "established_findings",
            "limitations_across_papers",
            "contradictions",
            "candidate_gaps",
            "candidate_research_questions",
            "promising_research_directions",
            "priority_papers",
            "unresolved_questions",
        ],
    }


def synthesize_batch(
    batch_path: Path,
    *,
    model: str,
) -> tuple[dict, dict]:

    batch = load_json(
        batch_path
    )

    batch_id = batch.get(
        "batch_id",
        batch_path.stem,
    )

    prompt = f"""
You are a senior research analyst in
Mechanical Engineering and Soft Robotics.

You are performing an intermediate
evidence synthesis.

The input contains scientific evidence
extracted from a SMALL BATCH of papers.

Your job is NOT to declare novelty.

Your job is to identify:

- what is already established,
- what mechanisms are being studied,
- what modeling approaches are used,
- recurring limitations,
- conflicting findings,
- plausible candidate research gaps,
- measurable research questions,
- promising directions for MSc research.

CRITICAL RULES:

1. Use ONLY the supplied batch evidence.

2. Never invent:
   - papers,
   - authors,
   - DOI values,
   - numerical results,
   - methods,
   - conclusions.

3. Every scientific claim that depends
   on a paper must preserve paper_id.

4. A missing method in these papers does
   NOT prove a global research gap.

5. Treat every novelty claim as
   UNVERIFIED until broader literature
   searching is completed.

6. Distinguish:
   - established finding,
   - limitation,
   - candidate gap,
   - research direction.

7. Do not convert authors' future work
   automatically into a research gap.

8. Prefer mechanically meaningful
   questions involving:
   - stiffness,
   - force,
   - deformation,
   - hysteresis,
   - response time,
   - geometry,
   - material behavior,
   - actuator behavior,
   - mechanics modeling,
   - experimental validation.

9. Consider MSc feasibility:
   whether the direction could reasonably
   lead to modeling + prototype/experiment
   + quantitative validation.

10. Do not favor an idea just because
    several papers mention it.

BATCH DATA:

{json.dumps(
    batch,
    ensure_ascii=False,
    indent=2,
)}
""".strip()

    result = call_antigravity(
        model=model,
        prompt=prompt,
        json_schema=build_schema(),
    )

    raw_content = (
        result.get(
            "content",
            "",
        )
        or ""
    ).strip()

    if not raw_content:
        raise RuntimeError(
            f"{batch_id}: model "
            "returned empty content."
        )

    try:
        synthesis = json.loads(
            raw_content
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{batch_id}: model "
            "returned invalid JSON.\n\n"
            f"{raw_content[:3000]}"
        ) from exc

    synthesis[
        "batch_id"
    ] = batch_id

    return synthesis, result


def main() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--force",
        action="store_true",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    manifest = load_json(
        MANIFEST_PATH
    )

    model = (
        os.getenv(
            "GEMINI_BATCH_MODEL",
            "",
        ).strip()
        or
        os.getenv(
            "GEMINI_BULK_MODEL",
            "gemini-3.8-flash-medium",
        ).strip()
    )

    if not model:
        raise RuntimeError(
            "No Gemini batch model configured."
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    batches = manifest.get(
        "batches",
        [],
    )

    if args.limit is not None:
        batches = batches[
            :args.limit
        ]

    print(
        f"[MODEL] {model}"
    )

    print(
        f"[BATCHES] {len(batches)}"
    )

    print()

    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_tokens = 0

    completed = []

    for item in batches:

        batch_id = item[
            "batch_id"
        ]

        batch_path = Path(
            item["file"]
        )

        output_path = (
            OUTPUT_DIR
            / f"{batch_id}.json"
        )

        batch_hash = sha256_file(
            batch_path
        )

        # -----------------------------------------
        # Incremental skip
        # -----------------------------------------

        if (
            output_path.exists()
            and not args.force
        ):

            try:
                existing = load_json(
                    output_path
                )

                if (
                    existing.get(
                        "source_batch_sha256"
                    )
                    == batch_hash
                ):
                    print(
                        f"[SKIP] {batch_id}"
                    )

                    completed.append(
                        {
                            "batch_id":
                                batch_id,
                            "file":
                                str(
                                    output_path
                                ),
                            "source_batch_sha256":
                                batch_hash,
                        }
                    )

                    continue

            except Exception:
                pass

        print(
            f"[SYNTHESIZE] {batch_id}"
        )

        synthesis, result = (
            synthesize_batch(
                batch_path,
                model=model,
            )
        )

        record = {
            "schema_version": 1,

            "batch_id":
                batch_id,

            "source_batch":
                str(batch_path),

            "source_batch_sha256":
                batch_hash,

            "model":
                result.get(
                    "model",
                    model,
                ),

            "usage": {
                "prompt_tokens":
                    result.get(
                        "prompt_tokens",
                        0,
                    ),

                "completion_tokens":
                    result.get(
                        "completion_tokens",
                        0,
                    ),

                "total_tokens":
                    result.get(
                        "total_tokens",
                        0,
                    ),

                "thinking_tokens":
                    result.get(
                        "thinking_tokens",
                        0,
                    ),

                "cache_read_tokens":
                    result.get(
                        "cache_read_tokens",
                        0,
                    ),
            },

            "synthesis":
                synthesis,
        }

        output_path.write_text(
            json.dumps(
                record,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        usage = record[
            "usage"
        ]

        total_prompt_tokens += (
            usage[
                "prompt_tokens"
            ]
        )

        total_completion_tokens += (
            usage[
                "completion_tokens"
            ]
        )

        total_tokens += (
            usage[
                "total_tokens"
            ]
        )

        completed.append(
            {
                "batch_id":
                    batch_id,

                "file":
                    str(
                        output_path
                    ),

                "source_batch_sha256":
                    batch_hash,
            }
        )

        print(
            f"[SAVED] {output_path}"
        )

        print(
            "[TOKENS] "
            f"{usage['total_tokens']:,}"
        )

        print()

    output_manifest = {
        "schema_version": 1,

        "source_manifest":
            str(
                MANIFEST_PATH
            ),

        "source_matrix_sha256":
            manifest.get(
                "matrix_sha256"
            ),

        "model":
            model,

        "batch_count":
            len(completed),

        "batches":
            completed,

        "usage_this_run": {
            "prompt_tokens":
                total_prompt_tokens,

            "completion_tokens":
                total_completion_tokens,

            "total_tokens":
                total_tokens,
        },
    }

    manifest_output_path = (
        OUTPUT_DIR
        / "manifest.json"
    )

    manifest_output_path.write_text(
        json.dumps(
            output_manifest,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        "=" * 60
    )

    print(
        "[DONE]"
    )

    print(
        f"[COMPLETED] "
        f"{len(completed)}"
    )

    print(
        "[TOKENS THIS RUN] "
        f"{total_tokens:,}"
    )

    print(
        f"[MANIFEST] "
        f"{manifest_output_path}"
    )


if __name__ == "__main__":
    main()