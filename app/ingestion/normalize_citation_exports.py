"""Normalize citation exports for the isolated D1-V002 metadata round.

This CLI handles bibliographic metadata only. It never registers or ingests a
paper, and its output must not be treated as scientific evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from app.ingestion.citation_identity import (
    DISCOVERY_STATUS,
    flag_fuzzy_titles,
    merge_metadata_records,
    metadata_compatible,
    normalize_author,
    normalize_doi,
    normalize_title,
    normalize_year,
    split_multi_value,
)
from app.ingestion.citation_parsers import (
    parse_csv_export as _parse_csv_export,
    parse_ris_export as _parse_ris_export,
    record_from_values as _record_from_values,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY_PATH = REPOSITORY_ROOT / "data/paper_registry.json"
DEFAULT_EVIDENCE_DIR = REPOSITORY_ROOT / "data/evidence"
DEFAULT_INPUT_DIR = REPOSITORY_ROOT / "data/search_exports/D1-V002/raw"
DEFAULT_OUTPUT_DIR = REPOSITORY_ROOT / "outputs/search_results/D1-V002"
DEFAULT_MANIFEST_PATH = REPOSITORY_ROOT / "data/search_exports/D1-V002/round_manifest.json"
DEFAULT_CANDIDATES_PATH = DEFAULT_OUTPUT_DIR / "normalized_candidates.json"

ROUND_ID = "D1-V002"
SUBJECT_DIRECTION_ID = "P1"
SUBJECT_TITLE = "Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams"
BASELINE_VERIFICATION_ID = "D1-V001"

KNOWN_THREATS = (
    {"title": "A continuum-based model for a layer jamming beam", "year": "2025",
     "doi": "10.5194/ms-16-821-2025", "authors": ["Zhang et al."]},
    {"title": "Toward a deeper understanding of layer jamming structures", "year": "2025",
     "doi": "10.1007/s11465-025-0843-5", "authors": ["Zhang et al."]},
    {"title": "Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots",
     "year": "2026", "doi": "10.1109/TCST.2026.3690756",
     "authors": ["Yeman Fan", "Bowen Yi", "Dikai Liu"]},
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


# Keep these public wrappers for existing callers and tests.
def record_from_values(**kwargs) -> dict:
    return _record_from_values(sha256_file=sha256_file, **kwargs)


def parse_csv_export(path: Path) -> list[dict]:
    return _parse_csv_export(path, sha256_file)


def parse_ris_export(path: Path) -> list[dict]:
    return _parse_ris_export(path, sha256_file)


def parse_export(path: Path) -> list[dict]:
    suffix = path.suffix.casefold()
    if suffix == ".csv":
        return parse_csv_export(path)
    if suffix == ".ris":
        return parse_ris_export(path)
    raise RuntimeError(f"Unsupported citation export: {path}")


def known_threat_records() -> list[dict]:
    return [
        record_from_values(
            title=threat["title"], doi=threat["doi"], year=threat["year"],
            authors=list(threat["authors"]), abstract="", keywords=[], url="", file_path="",
            source_path=None, source_format="known_threat", record_index=index,
            source_hash="", source_database="known threats",
            record_identifier=f"known-threat-{index}", raw_metadata=dict(threat),
        )
        for index, threat in enumerate(KNOWN_THREATS, start=1)
    ]


def load_existing_metadata(registry_path: Path, evidence_dir: Path) -> list[dict]:
    """Load registry metadata, then fill missing fields from evidence records."""
    by_paper_id: dict[str, dict] = {}
    if registry_path.exists():
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        for paper in registry.get("papers", []):
            paper_id = str(paper.get("paper_id", ""))
            by_paper_id[paper_id] = {
                "paper_id": paper_id, "title": str(paper.get("title", "") or ""),
                "doi": str(paper.get("doi", "") or ""), "year": normalize_year(paper.get("year")),
                "authors": list(paper.get("authors", []) or []),
                "pdf_sha256": str(paper.get("pdf_sha256", "") or ""),
                "source_type": str(paper.get("source_type", "") or ""),
                "verification_id": paper.get("verification_id"),
            }
    if evidence_dir.exists():
        for path in sorted(evidence_dir.glob("*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            source, paper = data.get("source", {}) or {}, data.get("paper", {}) or {}
            paper_id = str(source.get("paper_id", "") or "")
            if not paper_id:
                continue
            current = by_paper_id.setdefault(paper_id, {"paper_id": paper_id})
            current["title"] = paper.get("title") or current.get("title", "")
            current["doi"] = paper.get("doi") or current.get("doi", "")
            current["year"] = normalize_year(paper.get("year") or current.get("year"))
            current["authors"] = paper.get("authors", []) or current.get("authors", [])
            current["pdf_sha256"] = source.get("sha256") or current.get("pdf_sha256", "")
            current["source_type"] = source.get("source_type") or current.get("source_type", "")
            current["verification_id"] = source.get("verification_id") or current.get("verification_id")
    result = []
    for item in by_paper_id.values():
        item["normalized_title"] = normalize_title(item.get("title"))
        item["normalized_doi"] = normalize_doi(item.get("doi"))
        result.append(item)
    return sorted(result, key=lambda item: item.get("paper_id", ""))


def compare_with_existing(candidates: list[dict], existing: list[dict]) -> None:
    for candidate in candidates:
        matches = []
        candidate_hashes = {
            variant.get("sha256", "") for variant in candidate.get("file_variants", [])
            if variant.get("sha256")
        }
        if candidate.get("file_sha256"):
            candidate_hashes.add(candidate["file_sha256"])
        for paper in existing:
            match_type = ""
            review_required = False
            if candidate.get("normalized_doi") and candidate["normalized_doi"] == paper.get("normalized_doi"):
                match_type = "exact_normalized_doi"
            elif paper.get("pdf_sha256") and paper["pdf_sha256"] in candidate_hashes:
                match_type = "exact_file_sha256"
            elif candidate.get("normalized_title") and candidate["normalized_title"] == paper.get("normalized_title"):
                match_type = "probable_normalized_title"
                review_required = True
            if match_type:
                matches.append({
                    "match_type": match_type, "requires_human_review": review_required,
                    "metadata_comparison": {"fully_compatible": metadata_compatible(candidate, paper)},
                    "paper_id": paper.get("paper_id", ""), "title": paper.get("title", ""),
                    "doi": paper.get("doi", ""), "source_type": paper.get("source_type", ""),
                    "verification_id": paper.get("verification_id"),
                })
        candidate["existing_corpus_matches"] = sorted(matches, key=lambda item: (item["paper_id"], item["match_type"]))


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)


def write_candidates_csv(path: Path, candidates: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "candidate_id", "title", "normalized_title", "doi", "normalized_doi", "year", "authors",
        "keywords", "status", "metadata_only", "scientific_evidence", "provenance_count",
        "existing_match_count", "identity_conflict_count", "probable_duplicate_group_count",
        "fuzzy_review_count",
    ]
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for candidate in candidates:
            writer.writerow({
                **{field: candidate.get(field, "") for field in fields},
                "authors": "; ".join(candidate["authors"]), "keywords": "; ".join(candidate["keywords"]),
                "provenance_count": len(candidate["provenance"]),
                "existing_match_count": len(candidate["existing_corpus_matches"]),
                "identity_conflict_count": len(candidate["identity_conflicts"]),
                "probable_duplicate_group_count": len(candidate["probable_duplicate_groups"]),
                "fuzzy_review_count": len(candidate["fuzzy_title_review"]),
            })
    temporary.replace(path)


def _lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def validate_round_paths(
    *, input_dir: Path, output_dir: Path, manifest_path: Path,
    repository_root: Path = REPOSITORY_ROOT,
) -> None:
    """Require exact lexical paths and reject every symlink escape/component."""
    root = repository_root.resolve()
    expected = {
        "input": root / "data/search_exports/D1-V002/raw",
        "output": root / "outputs/search_results/D1-V002",
        "manifest": root / "data/search_exports/D1-V002/round_manifest.json",
    }
    supplied = {
        "input": _lexical_absolute(input_dir), "output": _lexical_absolute(output_dir),
        "manifest": _lexical_absolute(manifest_path),
    }
    for name, path in supplied.items():
        if path != expected[name]:
            raise RuntimeError(f"D1-V002 {name} path must be exactly {expected[name]}; got {path}.")
        if path.resolve(strict=False) != expected[name]:
            raise RuntimeError(f"D1-V002 {name} path contains a symlink or escapes the repository.")


def require_round_output_dir(output_dir: Path) -> None:
    """Compatibility wrapper implementing the production-safe check."""
    validate_round_paths(input_dir=DEFAULT_INPUT_DIR, output_dir=output_dir, manifest_path=DEFAULT_MANIFEST_PATH)


def validate_manifest_identity(manifest_path: Path) -> None:
    if not manifest_path.exists():
        return
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read D1-V002 round manifest: {manifest_path}") from exc
    required = {
        "verification_id": ROUND_ID, "subject_direction_id": SUBJECT_DIRECTION_ID,
        "subject_title": SUBJECT_TITLE, "baseline_verification_id": BASELINE_VERIFICATION_ID,
    }
    if any(manifest.get(key) != value for key, value in required.items()):
        raise RuntimeError("Round manifest identity does not match D1-V002 / P1 / D1-V001 baseline.")


def update_manifest(manifest_path: Path, export_paths: list[Path], repository_root: Path = REPOSITORY_ROOT) -> None:
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {
            "schema_version": 1, "verification_id": ROUND_ID,
            "subject_direction_id": SUBJECT_DIRECTION_ID, "subject_title": SUBJECT_TITLE,
            "baseline_verification_id": BASELINE_VERIFICATION_ID, "created_at_utc": utc_now(),
            "input_export_provenance": [], "hashes": {},
        }
    validate_manifest_identity(manifest_path)
    exports, hashes = [], {}
    for path in export_paths:
        digest = sha256_file(path)
        relative = path.relative_to(repository_root).as_posix()
        exports.append({"path": relative, "format": path.suffix.casefold().lstrip("."), "sha256": digest,
                        "byte_size": path.stat().st_size})
        hashes[relative] = digest
    manifest["input_export_provenance"] = exports
    manifest["hashes"] = hashes
    atomic_json(manifest_path, manifest)


def run_normalization(
    *, verification_id: str, input_dir: Path, output_dir: Path, manifest_path: Path,
    registry_path: Path = DEFAULT_REGISTRY_PATH, evidence_dir: Path = DEFAULT_EVIDENCE_DIR,
    include_known_threats: bool = True, enforce_production_paths: bool = True,
) -> dict:
    if verification_id != ROUND_ID:
        raise RuntimeError(f"This implementation is isolated to {ROUND_ID}.")
    if enforce_production_paths:
        validate_round_paths(input_dir=input_dir, output_dir=output_dir, manifest_path=manifest_path)
    validate_manifest_identity(manifest_path)
    export_paths = sorted(
        (path for path in input_dir.rglob("*") if path.is_file() and path.suffix.casefold() in {".csv", ".ris"}),
        key=lambda path: path.as_posix(),
    ) if input_dir.exists() else []
    if enforce_production_paths:
        raw_root = input_dir.resolve()
        for path in export_paths:
            if path.resolve() != path.absolute() or raw_root not in path.resolve().parents:
                raise RuntimeError(f"Citation export must be a non-symlinked file inside {raw_root}: {path}")
    records = [record for path in export_paths for record in parse_export(path)]
    if include_known_threats:
        records.extend(known_threat_records())
    candidates, duplicate_events = merge_metadata_records(records)
    compare_with_existing(candidates, load_existing_metadata(registry_path, evidence_dir))
    flag_fuzzy_titles(candidates)
    candidates.sort(key=lambda item: (-int(item["year"] or 0), item["normalized_title"], item["candidate_id"]))
    payload = {
        "schema_version": 2, "verification_id": ROUND_ID, "subject_direction_id": SUBJECT_DIRECTION_ID,
        "subject_title": SUBJECT_TITLE, "baseline_verification_id": BASELINE_VERIFICATION_ID,
        "generated_at_utc": utc_now(),
        "notice": "Metadata relevance is not scientific evidence. No candidate is verified by this output.",
        "candidate_count": len(candidates), "candidates": candidates,
    }
    report = {
        "schema_version": 2, "verification_id": ROUND_ID, "raw_record_count": len(records),
        "candidate_count": len(candidates),
        "merged_group_count": sum(1 for event in duplicate_events if event["type"] in {"exact_normalized_doi", "exact_file_sha256"}),
        "review_event_count": sum(1 for event in duplicate_events if event.get("requires_human_review")),
        "deduplication_events": duplicate_events,
        "identity_conflicts": [{"candidate_id": item["candidate_id"], "conflicts": item["identity_conflicts"]}
                               for item in candidates if item["identity_conflicts"]],
        "probable_duplicate_groups": [event for event in duplicate_events if event["type"] == "probable_duplicate_same_title"],
        "fuzzy_title_review": [{"candidate_id": item["candidate_id"], "matches": item["fuzzy_title_review"]}
                               for item in candidates if item["fuzzy_title_review"]],
        "existing_corpus_matches": [{"candidate_id": item["candidate_id"], "matches": item["existing_corpus_matches"]}
                                    for item in candidates if item["existing_corpus_matches"]],
        "automatic_fuzzy_merging": False,
    }
    atomic_json(output_dir / "normalized_candidates.json", payload)
    write_candidates_csv(output_dir / "normalized_candidates.csv", candidates)
    atomic_json(output_dir / "deduplication_report.json", report)
    update_manifest(manifest_path, export_paths, REPOSITORY_ROOT if enforce_production_paths else input_dir.parents[3])
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize CSV/RIS citation metadata for D1-V002 without registering papers.")
    parser.add_argument("--verification-id", required=True)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    args = parser.parse_args()
    payload = run_normalization(
        verification_id=args.verification_id, input_dir=args.input_dir,
        output_dir=args.output_dir, manifest_path=args.manifest,
    )
    print(f"[ROUND] {payload['verification_id']} (scientific subject: {payload['subject_direction_id']})")
    print(f"[METADATA CANDIDATES] {payload['candidate_count']}")
    print("[NOTICE] Metadata relevance is not scientific evidence; no registry entries were created.")


if __name__ == "__main__":
    main()
