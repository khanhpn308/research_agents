from langgraph.types import Command

from app.graph import research_graph


def print_result(result: dict):
    print("\n" + "=" * 70)
    print("FINAL RESEARCH STATE")
    print("=" * 70)

    print(f"Task: {result.get('task')}")
    print(f"Risk level: {result.get('risk_level')}")
    print(f"Human decision: {result.get('human_decision')}")


    print("\n--- Literature ---")
    print(result.get("literature_summary", ""))

    print("\n--- Research Proposal ---")
    print(result.get("research_proposal", ""))

    print("\n--- Critique ---")
    print(result.get("critique", ""))

    if result.get("judge_result"):
        print("\n--- Judge Result ---")
        print(result["judge_result"])
    
    print(
        f"Model calls: "
        f"{result.get('model_calls', 0)}"
    )

    print(
        f"Judge calls: "
        f"{result.get('judge_calls', 0)}"
    )
    print("\n--- Usage / Cost ---")
    print(
        f"Prompt tokens: "
        f"{result.get('prompt_tokens', 0):,}"
    )

    print(
        f"Completion tokens: "
        f"{result.get('completion_tokens', 0):,}"
    )

    print(
        f"Total tokens: "
        f"{result.get('total_tokens', 0):,}"
    )

    print(
        "Estimated cost: "
        f"${result.get('estimated_cost_usd', 0.0):.6f}"
    )


def main():
    initial_state = {
        "task": (
            "Evaluate possible research opportunities involving "
            "variable stiffness in continuum robots for "
            "Mechanical Engineering research."
        ),
        "model_calls": 0,
        "judge_calls": 0,
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "estimated_cost_usd": 0.0,
    }

    config = {
        "configurable": {
            "thread_id": "research-test-001"
        }
    }

    result = research_graph.invoke(
        initial_state,
        config=config,
    )

    if "__interrupt__" in result:
        print("\n" + "=" * 70)
        print("HUMAN APPROVAL REQUIRED")
        print("=" * 70)

        for item in result["__interrupt__"]:
            print(item.value)

        choice = input(
            "\nAuthorize GPT-6 Astra? [yes/no]: "
        )

        result = research_graph.invoke(
            Command(resume=choice),
            config=config,
        )

    print_result(result)


if __name__ == "__main__":
    main()