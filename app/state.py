from typing import Literal, TypedDict


RiskLevel = Literal["low", "medium", "high"]


class ResearchState(TypedDict, total=False):
    # Input
    task: str

    # Research outputs
    literature_summary: str
    research_proposal: str
    critique: str
    judge_result: str

    # Routing
    risk_level: RiskLevel
    human_decision: str

    # Usage accounting
    model_calls: int
    judge_calls: int

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    estimated_cost_usd: float

    # Corpus
    corpus_synthesis: dict
    paper_index: list[dict]
    candidate_evidence: list[dict]
    corpus_matrix_sha256: str