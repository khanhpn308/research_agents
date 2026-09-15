import json
import os

from app.ingestion.pdf_loader import LoadedPaper
from app.providers.antigravity_provider import (
    call_antigravity,
)


PAPER_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
        },
        "authors": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "year": {
            "type": "string",
        },
        "doi": {
            "type": "string",
        },
        "research_problem": {
            "type": "string",
        },
        "research_objective": {
            "type": "string",
        },
        "robot_type": {
            "type": "string",
        },
        "stiffness_mechanism": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "actuation": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "modeling_methods": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "constitutive_assumptions": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "experimental_setup": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "independent_variables": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "dependent_variables": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "control_variables": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "performance_metrics": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "main_results": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "limitations_stated_by_authors": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "limitations_inferred": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "future_work": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "evidence_relevant_to_topic": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {
                        "type": "string",
                    },
                    "page_numbers": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                        },
                    },
                    "evidence_type": {
                        "type": "string",
                    },
                },
                "required": [
                    "claim",
                    "page_numbers",
                    "evidence_type",
                ],
                "additionalProperties": False,
            },
        },
        "possible_gap_implications": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "confidence": {
            "type": "string",
            "enum": [
                "low",
                "medium",
                "high",
            ],
        },
    },
    "required": [
        "title",
        "authors",
        "year",
        "doi",
        "research_problem",
        "research_objective",
        "robot_type",
        "stiffness_mechanism",
        "actuation",
        "modeling_methods",
        "constitutive_assumptions",
        "experimental_setup",
        "independent_variables",
        "dependent_variables",
        "control_variables",
        "performance_metrics",
        "main_results",
        "limitations_stated_by_authors",
        "limitations_inferred",
        "future_work",
        "evidence_relevant_to_topic",
        "possible_gap_implications",
        "confidence",
    ],
    "additionalProperties": False,
}


def extract_paper(
    paper: LoadedPaper,
) -> dict:

    model = os.getenv(
        "GEMINI_PAPER_MODEL",
        os.getenv(
            "GEMINI_BULK_MODEL",
            "gemini-3.8-flash-medium",
        ),
    ).strip()

    max_chars = int(
        os.getenv(
            "MAX_PAPER_CHARS",
            "210000",
        )
    )

    if paper["char_count"] > max_chars:
        raise RuntimeError(
            f"{paper['filename']} contains "
            f"{paper['char_count']:,} characters, "
            f"which exceeds MAX_PAPER_CHARS="
            f"{max_chars:,}. "
            "Do not silently truncate scientific "
            "papers. Chunking will be implemented "
            "for large papers."
        )

    prompt = f"""
You are extracting evidence from ONE
scientific paper for a Mechanical Engineering
research project.

Research domain:
- soft robotics
- soft grippers
- continuum robots
- variable stiffness
- mechanical modeling
- experimental mechanics

SOURCE FILE:
{paper["filename"]}

The complete machine-readable paper text is
provided below with explicit PAGE markers.

STRICT RULES:

1. Use ONLY information present in this paper.

2. Do not use your general knowledge as evidence.

3. Do not invent citations, DOI numbers,
   authors, measurements, mechanisms,
   experiments, or conclusions.

4. If information is not found, return an
   empty string or empty list as appropriate.

5. Clearly distinguish:
   - limitations explicitly stated by authors
   - limitations inferred by you

6. A possible research-gap implication is NOT
   proof of novelty.

7. For evidence relevant to the research topic,
   provide the supporting page number(s).

8. Paraphrase evidence. Do not fabricate
   quotations.

9. Do not claim that no prior work exists
   based on this single paper.

10. Preserve uncertainty.

11. Classification fields such as robot_type,
    stiffness_mechanism, and actuation must use
    terminology explicitly supported by the paper.

12. Do not classify a device as a continuum robot,
    soft gripper, catheter, manipulator, or another
    robot class unless the paper itself supports
    that classification.

13. Keep model interpretation separate from
    source-reported facts.

PAPER TEXT:

{paper["text"]}
""".strip()

    result = call_antigravity(
        model=model,
        prompt=prompt,
        json_schema=PAPER_SCHEMA,
    )

    try:
        extracted = json.loads(
            result["content"]
        )
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Gemini returned invalid structured "
            "paper extraction."
        ) from exc

    return {
        "extracted": extracted,
        "model": result["model"],
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
    }