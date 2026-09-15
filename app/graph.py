from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from app.nodes.approval import approval_node
from app.nodes.corpus_loader import corpus_loader_node
from app.nodes.critic import critic_node
from app.nodes.judge import judge_node
from app.nodes.researcher import researcher_node
from app.nodes.save_run import save_run_node
from app.state import ResearchState


def route_after_critic(
    state: ResearchState,
):
    if state.get("risk_level") == "high":
        return "approval"

    return "save_run"


def route_after_approval(
    state: ResearchState,
):
    if (
        state.get("human_decision")
        == "approved"
    ):
        return "judge"

    return "save_run"


builder = StateGraph(
    ResearchState
)


# ============================================================
# NODES
# ============================================================

builder.add_node(
    "corpus_loader",
    corpus_loader_node,
)

builder.add_node(
    "researcher",
    researcher_node,
)

builder.add_node(
    "critic",
    critic_node,
)

builder.add_node(
    "approval",
    approval_node,
)

builder.add_node(
    "judge",
    judge_node,
)

builder.add_node(
    "save_run",
    save_run_node,
)


# ============================================================
# EDGES
# ============================================================

builder.add_edge(
    START,
    "corpus_loader",
)

builder.add_edge(
    "corpus_loader",
    "researcher",
)

builder.add_edge(
    "researcher",
    "critic",
)

builder.add_conditional_edges(
    "critic",
    route_after_critic,
)

builder.add_conditional_edges(
    "approval",
    route_after_approval,
)

builder.add_edge(
    "judge",
    "save_run",
)

builder.add_edge(
    "save_run",
    END,
)


# ============================================================
# CHECKPOINTER
# ============================================================

checkpointer = InMemorySaver()

research_graph = builder.compile(
    checkpointer=checkpointer
)