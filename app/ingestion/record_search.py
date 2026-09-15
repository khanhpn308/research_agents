import argparse
import json
from datetime import date
from pathlib import Path


LOG_PATH = Path(
    "outputs/search_results/search_log.json"
)


def main() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--id",
        required=True,
    )

    parser.add_argument(
        "--db",
        required=True,
        choices=[
            "scopus",
            "wos",
            "scholar",
        ],
    )

    parser.add_argument(
        "--count",
        required=True,
        type=int,
    )

    parser.add_argument(
        "--notes",
        default="",
    )

    args = parser.parse_args()

    if not LOG_PATH.exists():
        raise RuntimeError(
            "search_log.json not found."
        )

    data = json.loads(
        LOG_PATH.read_text(
            encoding="utf-8"
        )
    )

    target = None

    for search in data["searches"]:
        if (
            search["verification_id"]
            == args.id
        ):
            target = search
            break

    if target is None:
        raise RuntimeError(
            f"Unknown verification ID: "
            f"{args.id}"
        )

    db = target["databases"][
        args.db
    ]

    db["searched"] = True

    db["search_date"] = (
        date.today().isoformat()
    )

    db["result_count"] = (
        args.count
    )

    db["notes"] = (
        args.notes
    )

    LOG_PATH.write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        f"[UPDATED] {args.id}"
    )

    print(
        f"[DATABASE] {args.db}"
    )

    print(
        f"[RESULTS] {args.count}"
    )

    print(
        f"[SAVED] {LOG_PATH}"
    )


if __name__ == "__main__":
    main()