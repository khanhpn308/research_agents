import json
from pathlib import Path


EVIDENCE_DIR = Path("data/evidence")
OUTPUT_DIR = Path("outputs")
OUTPUT_PATH = OUTPUT_DIR / "literature_matrix.json"


def load_records() -> list[dict]:
    records = []

    for path in sorted(EVIDENCE_DIR.glob("*.json")):
        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            records.append(
                json.load(file)
            )

    if not records:
        raise RuntimeError(
            "No evidence JSON files found."
        )

    return records


def build_matrix(
    records: list[dict],
) -> dict:

    papers = []
    evidence_claims = []
    limitations = []
    future_work = []
    gap_implications = []

    total_tokens = 0

    for record in records:
        source = record["source"]
        paper = record["paper"]
        usage = record.get("usage", {})

        paper_id = source["sha256"][:10]

        total_tokens += int(
            usage.get("total_tokens", 0) or 0
        )

        papers.append(
            {
                "paper_id": paper_id,
                "title": paper["title"],
                "authors": paper["authors"],
                "year": paper["year"],
                "doi": paper["doi"],
                "robot_type":
                    paper["robot_type"],
                "stiffness_mechanism":
                    paper["stiffness_mechanism"],
                "actuation":
                    paper["actuation"],
                "modeling_methods":
                    paper["modeling_methods"],
                "performance_metrics":
                    paper["performance_metrics"],
                "confidence":
                    paper["confidence"],
                "has_stiffness_mechanism":
                    bool(
                        paper[
                            "stiffness_mechanism"
                        ]
                    ),
            }
        )

        for evidence in paper[
            "evidence_relevant_to_topic"
        ]:
            evidence_claims.append(
                {
                    "paper_id": paper_id,
                    "title":
                        paper["title"],
                    "doi":
                        paper["doi"],
                    "claim":
                        evidence["claim"],
                    "evidence_type":
                        evidence[
                            "evidence_type"
                        ],
                    "page_numbers":
                        evidence[
                            "page_numbers"
                        ],
                }
            )

        for item in paper[
            "limitations_stated_by_authors"
        ]:
            limitations.append(
                {
                    "paper_id": paper_id,
                    "source_type":
                        "author_stated",
                    "text": item,
                }
            )

        for item in paper[
            "limitations_inferred"
        ]:
            limitations.append(
                {
                    "paper_id": paper_id,
                    "source_type":
                        "model_inferred",
                    "text": item,
                }
            )

        for item in paper["future_work"]:
            future_work.append(
                {
                    "paper_id": paper_id,
                    "text": item,
                }
            )

        for item in paper[
            "possible_gap_implications"
        ]:
            gap_implications.append(
                {
                    "paper_id": paper_id,
                    "status":
                        "unverified_implication",
                    "text": item,
                }
            )

    return {
        "corpus_summary": {
            "paper_count":
                len(papers),
            "evidence_claim_count":
                len(evidence_claims),
            "total_extraction_tokens":
                total_tokens,
        },
        "papers": papers,
        "evidence_claims":
            evidence_claims,
        "limitations":
            limitations,
        "future_work":
            future_work,
        "gap_implications":
            gap_implications,
    }


def main() -> None:
    records = load_records()

    matrix = build_matrix(
        records
    )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            matrix,
            file,
            indent=2,
            ensure_ascii=False,
        )

    summary = matrix[
        "corpus_summary"
    ]

    print(
        f"[PAPERS] "
        f"{summary['paper_count']}"
    )

    print(
        f"[CLAIMS] "
        f"{summary['evidence_claim_count']}"
    )

    print(
        f"[TOKENS] "
        f"{summary['total_extraction_tokens']:,}"
    )

    print(
        f"[SAVED] {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()