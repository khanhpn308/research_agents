import hashlib
import json
from pathlib import Path

from app.state import ResearchState


MATRIX_PATH = Path(
    "outputs/literature_matrix.json"
)

SYNTHESIS_PATH = Path(
    "outputs/corpus_synthesis.json"
)


def sha256_text(
    text: str,
) -> str:

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def corpus_loader_node(
    state: ResearchState,
) -> dict:

    if not MATRIX_PATH.exists():
        raise RuntimeError(
            "literature_matrix.json not found. "
            "Run:\n"
            "python -m app.ingestion.build_matrix"
        )

    if not SYNTHESIS_PATH.exists():
        raise RuntimeError(
            "corpus_synthesis.json not found. "
            "Run:\n"
            "python -m app.ingestion.synthesize_corpus"
        )

    matrix_text = MATRIX_PATH.read_text(
        encoding="utf-8"
    )

    synthesis_text = SYNTHESIS_PATH.read_text(
        encoding="utf-8"
    )

    matrix_hash = sha256_text(
        matrix_text
    )

    matrix = json.loads(
        matrix_text
    )

    synthesis_record = json.loads(
        synthesis_text
    )

    synthesis_hash = synthesis_record.get(
        "source_matrix_sha256",
        "",
    )

    if synthesis_hash != matrix_hash:
        raise RuntimeError(
            "Corpus synthesis is stale.\n"
            "The literature matrix has changed.\n\n"
            "Run:\n"
            "python -m app.ingestion.synthesize_corpus"
        )

    synthesis = synthesis_record.get(
        "synthesis",
        {},
    )

    if not synthesis:
        raise RuntimeError(
            "No synthesis object found in "
            "corpus_synthesis.json."
        )

    paper_index = []

    for paper in matrix.get(
        "papers",
        [],
    ):
        paper_index.append(
            {
                "paper_id":
                    paper["paper_id"],

                "title":
                    paper["title"],

                "year":
                    paper["year"],

                "doi":
                    paper["doi"],

                "robot_type":
                    paper["robot_type"],

                "has_stiffness_mechanism":
                    paper[
                        "has_stiffness_mechanism"
                    ],
            }
        )

    relevant_paper_ids = set()

    for gap in synthesis.get(
        "candidate_gap_signals",
        [],
    ):

        relevant_paper_ids.update(
            gap.get(
                "supporting_paper_ids",
                [],
            )
        )

        relevant_paper_ids.update(
            gap.get(
                "counterevidence_paper_ids",
                [],
            )
        )

    candidate_evidence = []

    for claim in matrix.get(
        "evidence_claims",
        [],
    ):

        if (
            claim.get("paper_id")
            in relevant_paper_ids
        ):
            candidate_evidence.append(
                claim
            )

    return {
        "corpus_synthesis":
            synthesis,

        "paper_index":
            paper_index,

        "candidate_evidence":
            candidate_evidence,

        "corpus_matrix_sha256":
            matrix_hash,
    }