import json
from datetime import datetime, timezone
from pathlib import Path


DATA_DIR = Path("data")

REGISTRY_PATH = (
    DATA_DIR / "paper_registry.json"
)


def utc_now() -> str:
    return datetime.now(
        timezone.utc
    ).isoformat()


def load_registry() -> dict:

    if not REGISTRY_PATH.exists():
        raise RuntimeError(
            "paper_registry.json not found.\n"
            "Run:\n"
            "python -m "
            "app.ingestion.init_corpus_storage"
        )

    try:
        registry = json.loads(
            REGISTRY_PATH.read_text(
                encoding="utf-8"
            )
        )

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "paper_registry.json "
            "contains invalid JSON."
        ) from exc

    if not isinstance(
        registry.get("papers"),
        list,
    ):
        raise RuntimeError(
            "Invalid paper registry: "
            "'papers' must be a list."
        )

    return registry


def save_registry(
    registry: dict,
) -> None:

    registry["updated_at_utc"] = (
        utc_now()
    )

    registry["paper_count"] = len(
        registry.get(
            "papers",
            [],
        )
    )

    REGISTRY_PATH.write_text(
        json.dumps(
            registry,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def resolve_pdf_path(
    paper: dict,
) -> Path:

    relative_path = paper.get(
        "relative_path",
        "",
    )

    if not relative_path:
        raise RuntimeError(
            "Paper has no relative_path: "
            f"{paper.get('paper_id')}"
        )

    path = (
        DATA_DIR / relative_path
    )

    if not path.exists():
        raise RuntimeError(
            "Registered PDF does not exist:\n"
            f"{path}"
        )

    return path


def get_ingestion_candidates(
    registry: dict | None = None,
) -> list[dict]:

    if registry is None:
        registry = load_registry()

    candidates = []

    for paper in registry["papers"]:

        if (
            paper.get(
                "screening_status"
            )
            != "included"
        ):
            continue

        if (
            paper.get(
                "ingestion_status"
            )
            != "pending"
        ):
            continue

        candidates.append(
            paper
        )

    return candidates


def find_paper(
    paper_id: str,
    registry: dict | None = None,
) -> dict:

    if registry is None:
        registry = load_registry()

    for paper in registry["papers"]:

        if (
            paper.get("paper_id")
            == paper_id
        ):
            return paper

    raise RuntimeError(
        "Unknown paper_id: "
        f"{paper_id}"
    )


def mark_ingestion_started(
    paper_id: str,
) -> None:

    registry = load_registry()

    paper = find_paper(
        paper_id,
        registry,
    )

    paper["ingestion_status"] = (
        "processing"
    )

    paper["updated_at_utc"] = (
        utc_now()
    )

    save_registry(
        registry
    )


def mark_ingestion_complete(
    paper_id: str,
    evidence_path: Path,
) -> None:

    registry = load_registry()

    paper = find_paper(
        paper_id,
        registry,
    )

    try:
        relative_evidence = str(
            evidence_path.relative_to(
                DATA_DIR
            )
        )

    except ValueError:
        relative_evidence = str(
            evidence_path
        )

    paper["ingestion_status"] = (
        "complete"
    )

    paper["evidence_status"] = (
        "present"
    )

    paper["evidence_file"] = (
        relative_evidence
    )

    paper["updated_at_utc"] = (
        utc_now()
    )

    paper.pop(
        "ingestion_error",
        None,
    )

    save_registry(
        registry
    )


def mark_ingestion_failed(
    paper_id: str,
    error: str,
) -> None:

    registry = load_registry()

    paper = find_paper(
        paper_id,
        registry,
    )

    paper["ingestion_status"] = (
        "failed"
    )

    paper["ingestion_error"] = (
        str(error)
    )

    paper["updated_at_utc"] = (
        utc_now()
    )

    save_registry(
        registry
    )


def reset_failed_ingestion(
    paper_id: str,
) -> None:

    registry = load_registry()

    paper = find_paper(
        paper_id,
        registry,
    )

    if (
        paper.get(
            "ingestion_status"
        )
        != "failed"
    ):
        return

    paper["ingestion_status"] = (
        "pending"
    )

    paper.pop(
        "ingestion_error",
        None,
    )

    paper["updated_at_utc"] = (
        utc_now()
    )

    save_registry(
        registry
    )