import json
from pathlib import Path


QUERY_PATH = Path(
    "outputs/search_queries/database_queries.json"
)

OUTPUT_PATH = Path(
    "outputs/search_results/search_log.json"
)


def main() -> None:

    if not QUERY_PATH.exists():
        raise RuntimeError(
            "database_queries.json not found."
        )

    source = json.loads(
        QUERY_PATH.read_text(
            encoding="utf-8"
        )
    )

    queries = source.get(
        "queries",
        [],
    )

    searches = []

    for item in queries:
        searches.append(
            {
                "verification_id":
                    item["verification_id"],

                "priority":
                    item["priority"],

                "search_objective":
                    item["search_objective"],

                "gap_closing_evidence":
                    item["gap_closing_evidence"],

                "databases": {
                    "scopus": {
                        "query":
                            item["scopus_query"],

                        "searched":
                            False,

                        "search_date":
                            None,

                        "result_count":
                            None,

                        "notes":
                            "",
                    },

                    "wos": {
                        "query":
                            item["wos_query"],

                        "searched":
                            False,

                        "search_date":
                            None,

                        "result_count":
                            None,

                        "notes":
                            "",
                    },

                    "scholar": {
                        "query":
                            item["scholar_query"],

                        "searched":
                            False,

                        "search_date":
                            None,

                        "result_count":
                            None,

                        "notes":
                            "",
                    },
                },

                "candidate_papers": [],

                "status":
                    "pending",
            }
        )

    output = {
        "source_query_model":
            source.get("model"),

        "searches":
            searches,

        "screening_decisions": {
            "include":
                "Paper directly addresses the "
                "verification question.",

            "exclude":
                "Paper does not provide evidence "
                "relevant to the verification "
                "question.",

            "uncertain":
                "Full text or deeper screening "
                "is required.",
        },
    }

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_PATH.write_text(
        json.dumps(
            output,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        f"[SEARCH TASKS] {len(searches)}"
    )

    print(
        f"[SAVED] {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()