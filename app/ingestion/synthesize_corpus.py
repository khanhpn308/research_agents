import hashlib
import json
import os
from pathlib import Path

from app.providers.antigravity_provider import (
    call_antigravity,
)


MATRIX_PATH = Path(
    "outputs/literature_matrix.json"
)

OUTPUT_PATH = Path(
    "outputs/corpus_synthesis.json"
)


SYNTHESIS_SCHEMA = {
    "type": "object",
    "properties": {
        "corpus_scope": {
            "type": "string",
        },
        "core_paper_ids": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "adjacent_paper_ids": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "evidence_clusters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "theme": {
                        "type": "string",
                    },
                    "paper_ids": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "synthesis": {
                        "type": "string",
                    },
                    "consensus_level": {
                        "type": "string",
                        "enum": [
                            "low",
                            "medium",
                            "high",
                        ],
                    },
                    "supporting_claims": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                },
                "required": [
                    "theme",
                    "paper_ids",
                    "synthesis",
                    "consensus_level",
                    "supporting_claims",
                ],
                "additionalProperties": False,
            },
        },
        "cross_paper_patterns": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "contradictions_or_tensions": {
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
                "additionalProperties": False,
            },
        },
        "missing_evidence": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "candidate_gap_signals": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "candidate_gap": {
                        "type": "string",
                    },
                    "supporting_paper_ids": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "counterevidence_paper_ids": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "signal_strength": {
                        "type": "string",
                        "enum": [
                            "weak",
                            "moderate",
                            "strong_within_corpus",
                        ],
                    },
                    "why_it_might_be_a_gap": {
                        "type": "string",
                    },
                    "why_it_might_not_be_a_gap": {
                        "type": "string",
                    },
                    "verification_needed": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                },
                "required": [
                    "candidate_gap",
                    "supporting_paper_ids",
                    "counterevidence_paper_ids",
                    "signal_strength",
                    "why_it_might_be_a_gap",
                    "why_it_might_not_be_a_gap",
                    "verification_needed",
                ],
                "additionalProperties": False,
            },
        },
        "corpus_limitations": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "recommended_next_searches": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
    },
    "required": [
        "corpus_scope",
        "core_paper_ids",
        "adjacent_paper_ids",
        "evidence_clusters",
        "cross_paper_patterns",
        "contradictions_or_tensions",
        "missing_evidence",
        "candidate_gap_signals",
        "corpus_limitations",
        "recommended_next_searches",
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

    if not MATRIX_PATH.exists():
        raise RuntimeError(
            "literature_matrix.json not found."
        )

    matrix_text = MATRIX_PATH.read_text(
        encoding="utf-8"
    )

    matrix_hash = sha256_text(
        matrix_text
    )

    # Cache protection.
    if OUTPUT_PATH.exists():
        try:
            existing = json.loads(
                OUTPUT_PATH.read_text(
                    encoding="utf-8"
                )
            )

            if (
                existing.get(
                    "source_matrix_sha256"
                )
                == matrix_hash
            ):
                print(
                    "[SKIP] Corpus synthesis "
                    "already matches current matrix."
                )
                return

        except json.JSONDecodeError:
            pass

    matrix = json.loads(
        matrix_text
    )

    model = os.getenv(
        "GEMINI_SYNTHESIS_MODEL",
        "gemini-3.8-flash-high",
    ).strip()

    prompt = f"""
You are conducting CORPUS-ONLY scientific
literature synthesis for a Mechanical
Engineering MSc research project.

The research domain includes:
- soft robotics
- soft grippers
- continuum robots
- variable stiffness
- jamming mechanisms
- mechanics and modeling
- sensing where relevant

You are given a structured literature matrix
derived from scientific papers.

STRICT EVIDENCE RULES:

1. Use ONLY the supplied corpus.

2. Do not introduce external papers,
   citations, authors, mechanisms, or results.

3. Do not claim novelty.

4. A candidate gap is only a SIGNAL that
   requires external verification.

5. "author_stated" limitations carry stronger
   evidential status than "model_inferred"
   limitations.

6. "unverified_implication" entries are
   hypotheses, not established facts.

7. Preserve paper_id provenance.

8. Separate CORE papers directly studying
   variable stiffness/jamming from ADJACENT
   papers mainly concerning sensing,
   proprioception, or related enabling
   technologies.

9. Do not infer that a soft finger or gripper
   is a continuum robot unless the corpus
   explicitly supports that classification.

10. A missing topic in this five-paper corpus
    does NOT mean the topic is absent from
    the wider literature.

11. When multiple papers support a pattern,
    identify all relevant paper_ids.

12. When evidence conflicts, preserve the
    disagreement rather than forcing
    consensus.

Your tasks:

A. Define the scope of this corpus.

B. Separate core and adjacent papers.

C. Cluster evidence into technical themes.

D. Identify cross-paper patterns.

E. Identify contradictions or tensions.

F. Identify what this corpus does NOT
   establish.

G. Generate candidate research-gap SIGNALS.

For each candidate gap signal:
- explain why it might represent a gap;
- explain why it might NOT represent a gap;
- provide supporting paper IDs;
- provide counterevidence paper IDs;
- state what literature must be searched next
  before the gap can be accepted.

H. Recommend focused literature searches
   needed to falsify the candidate gaps.

LITERATURE MATRIX:

{json.dumps(
    matrix,
    ensure_ascii=False,
)}
""".strip()

    result = call_antigravity(
        model=model,
        prompt=prompt,
        json_schema=SYNTHESIS_SCHEMA,
    )

    try:
        synthesis = json.loads(
            result["content"]
        )
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Invalid corpus synthesis JSON."
        ) from exc

    output = {
        "source_matrix_sha256":
            matrix_hash,

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

        "synthesis":
            synthesis,
    }

    OUTPUT_PATH.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        f"[MODEL] {result['model']}"
    )

    print(
        "[TOKENS] "
        f"{result['total_tokens']:,}"
    )

    print(
        "[GAP SIGNALS] "
        f"{len(synthesis['candidate_gap_signals'])}"
    )

    print(
        f"[SAVED] {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()