"""Normalize citation exports for one isolated verification round.

This module handles bibliographic metadata only. It never registers papers,
ingests PDFs, or makes scientific novelty judgments.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY_PATH = REPOSITORY_ROOT / "data/paper_registry.json"
DEFAULT_EVIDENCE_DIR = REPOSITORY_ROOT / "data/evidence"

ROUND_ID = "D1-V002"
SUBJECT_DIRECTION_ID = "P1"
SUBJECT_TITLE = (
    "Validity Limits of a Homogenized Slip Model for "
    "High-Layer-Count Vacuum-Jammed Beams"
)
BASELINE_VERIFICATION_ID = "D1-V001"
DISCOVERY_STATUS = "discovered but not yet verified"

KNOWN_THREATS = (
    {
        "title": "A continuum-based model for a layer jamming beam",
        "year": "2025",
        "doi": "10.5194/ms-16-821-2025",
        "authors": ["Zhang et al."],
    },
    {
        "title": "Toward a deeper understanding of layer jamming structures",
        "year": "2025",
        "doi": "10.1007/s11465-025-0843-5",
        "authors": ["Zhang et al."],
    },
    {
        "title": (
            "Modeling, Control, and Stiffness Regulation of Layer "
            "Jamming-Based Continuum Robots"
        ),
        "year": "2026",
        "doi": "10.1109/TCST.2026.3690756",
        "authors": ["Yeman Fan", "Bowen Yi", "Dikai Liu"],
    },
)

CSV_ALIASES = {
    "title": ("title", "document title", "article title", "ti"),
    "doi": ("doi", "digital object identifier", "di"),
    "year": ("year", "publication year", "py"),
    "authors": ("authors", "author", "author(s)", "au"),
    "abstract": ("abstract", "ab"),
    "keywords": ("keywords", "author keywords", "keyword", "kw"),
    "url": ("url", "link", "source url", "ur"),
    "file_path": ("file", "file path", "file_path", "pdf", "pdf path"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_doi(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).strip().lower()
    text = re.sub(r"^doi\s*:\s*", "", text)
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    text = text.split("?", 1)[0].split("#", 1)[0]
    return text.strip().rstrip(".,;:)")


def normalize_title(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    text = re.sub(r"[‐‑‒–—−]", "-", text)
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


def normalize_author(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


def split_multi_value(value: Any) -> list[str]:
    if isinstance(value, list):
        values = value
    else:
        values = re.split(r"\s*[;|]\s*", str(value or ""))
    return [str(item).strip() for item in values if str(item).strip()]


def normalize_year(value: Any) -> str:
    match = re.search(r"(?:19|20)\d{2}", str(value or ""))
    return match.group(0) if match else ""


def compatible_years(left: str, right: str) -> bool:
    return not left or not right or left == right


def author_tokens(authors: Iterable[str]) -> set[str]:
    tokens: set[str] = set()
    for author in authors:
        normalized = normalize_author(author)
        parts = normalized.split()
        if parts:
            tokens.add(parts[-1])
    return tokens


def compatible_authors(left: list[str], right: list[str]) -> bool:
    left_tokens = author_tokens(left)
    right_tokens = author_tokens(right)
    if not left_tokens or not right_tokens:
        return True
    return bool(left_tokens & right_tokens)


def metadata_compatible(left: dict, right: dict) -> bool:
    return compatible_years(left.get("year", ""), right.get("year", "")) and compatible_authors(
        left.get("authors", []), right.get("authors", [])
    )


def _lookup(row: dict[str, Any], field: str) -> str:
    lowered = {str(key).strip().casefold(): value for key, value in row.items()}
    for alias in CSV_ALIASES[field]:
        value = lowered.get(alias.casefold())
        if value not in (None, ""):
            return str(value).strip()
    return ""


def _actual_file_hash(raw_path: str, source_path: Path) -> tuple[str, str]:
    if not raw_path:
        return "", ""
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = source_path.parent / candidate
    try:
        resolved = candidate.resolve()
    except OSError:
        return "", str(candidate)
    if not resolved.is_file():
        return "", str(resolved)
    return sha256_file(resolved), str(resolved)


def record_from_values(
    *,
    title: str,
    doi: str,
    year: str,
    authors: list[str],
    abstract: str,
    keywords: list[str],
    url: str,
    file_path: str,
    source_path: Path | None,
    source_format: str,
    record_index: int,
    source_hash: str,
) -> dict:
    actual_hash = ""
    resolved_file = ""
    if source_path is not None:
        actual_hash, resolved_file = _actual_file_hash(file_path, source_path)
    return {
        "title": title.strip(),
        "normalized_title": normalize_title(title),
        "doi": doi.strip(),
        "normalized_doi": normalize_doi(doi),
        "year": normalize_year(year),
        "authors": authors,
        "abstract": abstract.strip(),
        "keywords": keywords,
        "url": url.strip(),
        "file_path": resolved_file,
        "file_sha256": actual_hash,
        "provenance": {
            "source_file": str(source_path) if source_path else "known_threats",
            "source_format": source_format,
            "source_file_sha256": source_hash,
            "record_index": record_index,
        },
    }


def parse_csv_export(path: Path) -> list[dict]:
    source_hash = sha256_file(path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise RuntimeError(f"CSV has no header: {path}")
        records = []
        for index, row in enumerate(reader, start=1):
            records.append(
                record_from_values(
                    title=_lookup(row, "title"),
                    doi=_lookup(row, "doi"),
                    year=_lookup(row, "year"),
                    authors=split_multi_value(_lookup(row, "authors")),
                    abstract=_lookup(row, "abstract"),
                    keywords=split_multi_value(_lookup(row, "keywords")),
                    url=_lookup(row, "url"),
                    file_path=_lookup(row, "file_path"),
                    source_path=path,
                    source_format="csv",
                    record_index=index,
                    source_hash=source_hash,
                )
            )
    return records


def _ris_entries(path: Path) -> list[dict[str, list[str]]]:
    entries: list[dict[str, list[str]]] = []
    current: dict[str, list[str]] = {}
    last_tag = ""
    for raw_line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        match = re.match(r"^([A-Z0-9]{2})\s{0,2}-\s?(.*)$", raw_line)
        if match:
            tag, value = match.groups()
            if tag == "TY" and current:
                entries.append(current)
                current = {}
            current.setdefault(tag, []).append(value.strip())
            last_tag = tag
            if tag == "ER":
                entries.append(current)
                current = {}
                last_tag = ""
        elif raw_line.startswith((" ", "\t")) and last_tag and current.get(last_tag):
            current[last_tag][-1] = f"{current[last_tag][-1]} {raw_line.strip()}".strip()
    if current:
        entries.append(current)
    return entries


def _first(entry: dict[str, list[str]], *tags: str) -> str:
    for tag in tags:
        values = entry.get(tag, [])
        if values:
            return values[0]
    return ""


def parse_ris_export(path: Path) -> list[dict]:
    source_hash = sha256_file(path)
    records = []
    for index, entry in enumerate(_ris_entries(path), start=1):
        records.append(
            record_from_values(
                title=_first(entry, "TI", "T1", "CT"),
                doi=_first(entry, "DO", "DI"),
                year=_first(entry, "PY", "Y1", "DA"),
                authors=entry.get("AU", []) + entry.get("A1", []),
                abstract=_first(entry, "AB", "N2"),
                keywords=entry.get("KW", []),
                url=_first(entry, "UR", "L1"),
                file_path=_first(entry, "L1", "L2"),
                source_path=path,
                source_format="ris",
                record_index=index,
                source_hash=source_hash,
            )
        )
    return records


def parse_export(path: Path) -> list[dict]:
    suffix = path.suffix.casefold()
    if suffix == ".csv":
        return parse_csv_export(path)
    if suffix == ".ris":
        return parse_ris_export(path)
    raise RuntimeError(f"Unsupported citation export: {path}")


def known_threat_records() -> list[dict]:
    records = []
    for index, threat in enumerate(KNOWN_THREATS, start=1):
        records.append(
            record_from_values(
                title=threat["title"],
                doi=threat["doi"],
                year=threat["year"],
                authors=list(threat["authors"]),
                abstract="",
                keywords=[],
                url="",
                file_path="",
                source_path=None,
                source_format="known_threat",
                record_index=index,
                source_hash="",
            )
        )
    return records


def _merge_unique(left: list[str], right: list[str]) -> list[str]:
    result = list(left)
    seen = {normalize_title(item) for item in result}
    for item in right:
        key = normalize_title(item)
        if key and key not in seen:
            result.append(item)
            seen.add(key)
    return result


def merge_record(candidate: dict, record: dict, reason: str) -> None:
    if len(record.get("title", "")) > len(candidate.get("title", "")):
        candidate["title"] = record["title"]
    for field in ("doi", "normalized_doi", "year", "abstract", "url", "file_path", "file_sha256"):
        if not candidate.get(field) and record.get(field):
            candidate[field] = record[field]
    candidate["normalized_title"] = normalize_title(candidate.get("title", ""))
    candidate["authors"] = _merge_unique(candidate.get("authors", []), record.get("authors", []))
    candidate["keywords"] = _merge_unique(candidate.get("keywords", []), record.get("keywords", []))
    candidate["provenance"].append(record["provenance"])
    candidate["merge_reasons"].append(reason)


def candidate_from_record(record: dict, sequence: int) -> dict:
    identity = record["normalized_doi"] or f"{record['normalized_title']}|{record['year']}"
    stable = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12]
    return {
        "candidate_id": f"D1V002-{stable}",
        "title": record["title"],
        "normalized_title": record["normalized_title"],
        "doi": record["doi"],
        "normalized_doi": record["normalized_doi"],
        "year": record["year"],
        "authors": list(record["authors"]),
        "abstract": record["abstract"],
        "keywords": list(record["keywords"]),
        "url": record["url"],
        "file_path": record["file_path"],
        "file_sha256": record["file_sha256"],
        "provenance": [record["provenance"]],
        "merge_reasons": [],
        "identity_conflicts": [],
        "existing_corpus_matches": [],
        "fuzzy_title_review": [],
        "status": DISCOVERY_STATUS,
        "metadata_only": True,
        "scientific_evidence": False,
        "sequence": sequence,
    }


def merge_metadata_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    candidates: list[dict] = []
    duplicate_events: list[dict] = []
    for record in records:
        if not record["normalized_title"] and not record["normalized_doi"]:
            duplicate_events.append({"type": "invalid_metadata", "provenance": record["provenance"]})
            continue
        match = None
        reason = ""
        if record["normalized_doi"]:
            match = next(
                (item for item in candidates if item["normalized_doi"] == record["normalized_doi"]),
                None,
            )
            if match:
                reason = "exact_normalized_doi"
        if match is None and record["normalized_title"]:
            same_title = [item for item in candidates if item["normalized_title"] == record["normalized_title"]]
            for item in same_title:
                if item["normalized_doi"] and record["normalized_doi"] and item["normalized_doi"] != record["normalized_doi"]:
                    item["identity_conflicts"].append(
                        {"type": "same_title_conflicting_doi", "other_doi": record["normalized_doi"], "provenance": record["provenance"]}
                    )
                    continue
                if metadata_compatible(item, record):
                    match = item
                    reason = "exact_normalized_title_compatible_metadata"
                    break
        if match is None and record["file_sha256"]:
            match = next(
                (item for item in candidates if item["file_sha256"] == record["file_sha256"]),
                None,
            )
            if match:
                reason = "exact_file_sha256"
        if match is None:
            new_candidate = candidate_from_record(record, len(candidates) + 1)
            for item in candidates:
                if (
                    new_candidate["normalized_title"]
                    and new_candidate["normalized_title"] == item["normalized_title"]
                    and new_candidate["normalized_doi"]
                    and item["normalized_doi"]
                    and new_candidate["normalized_doi"] != item["normalized_doi"]
                ):
                    new_candidate["identity_conflicts"].append(
                        {
                            "type": "same_title_conflicting_doi",
                            "other_doi": item["normalized_doi"],
                            "provenance": item["provenance"][0],
                        }
                    )
            candidates.append(new_candidate)
            continue
        if (
            reason == "exact_normalized_doi"
            and match["normalized_title"]
            and record["normalized_title"]
            and match["normalized_title"] != record["normalized_title"]
        ):
            match["identity_conflicts"].append(
                {"type": "same_doi_conflicting_title", "other_title": record["title"], "provenance": record["provenance"]}
            )
        merge_record(match, record, reason)
        duplicate_events.append(
            {"type": reason, "candidate_id": match["candidate_id"], "provenance": record["provenance"]}
        )
    return candidates, duplicate_events


def load_existing_metadata(registry_path: Path, evidence_dir: Path) -> list[dict]:
    by_paper_id: dict[str, dict] = {}
    if registry_path.exists():
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        for paper in registry.get("papers", []):
            paper_id = str(paper.get("paper_id", ""))
            by_paper_id[paper_id] = {
                "paper_id": paper_id,
                "title": str(paper.get("title", "") or ""),
                "doi": str(paper.get("doi", "") or ""),
                "year": normalize_year(paper.get("year")),
                "authors": [],
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
            source = data.get("source", {}) or {}
            paper = data.get("paper", {}) or {}
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
    return result


def compare_with_existing(candidates: list[dict], existing: list[dict]) -> None:
    for candidate in candidates:
        for paper in existing:
            match_type = ""
            if candidate["normalized_doi"] and candidate["normalized_doi"] == paper["normalized_doi"]:
                match_type = "exact_normalized_doi"
            elif (
                candidate["normalized_title"]
                and candidate["normalized_title"] == paper["normalized_title"]
                and metadata_compatible(candidate, paper)
            ):
                match_type = "exact_normalized_title_compatible_metadata"
            elif candidate["file_sha256"] and candidate["file_sha256"] == paper.get("pdf_sha256"):
                match_type = "exact_file_sha256"
            if match_type:
                candidate["existing_corpus_matches"].append(
                    {
                        "match_type": match_type,
                        "paper_id": paper.get("paper_id", ""),
                        "title": paper.get("title", ""),
                        "doi": paper.get("doi", ""),
                        "source_type": paper.get("source_type", ""),
                        "verification_id": paper.get("verification_id"),
                    }
                )


def flag_fuzzy_titles(candidates: list[dict], threshold: float = 0.90) -> None:
    for index, left in enumerate(candidates):
        for right in candidates[index + 1 :]:
            if not left["normalized_title"] or not right["normalized_title"]:
                continue
            if left["normalized_title"] == right["normalized_title"]:
                continue
            ratio = SequenceMatcher(None, left["normalized_title"], right["normalized_title"]).ratio()
            if ratio >= threshold:
                left["fuzzy_title_review"].append(
                    {"candidate_id": right["candidate_id"], "title": right["title"], "similarity": round(ratio, 4)}
                )
                right["fuzzy_title_review"].append(
                    {"candidate_id": left["candidate_id"], "title": left["title"], "similarity": round(ratio, 4)}
                )


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)


def write_candidates_csv(path: Path, candidates: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    fields = [
        "candidate_id", "title", "normalized_title", "doi", "normalized_doi", "year",
        "authors", "keywords", "status", "metadata_only", "scientific_evidence",
        "provenance_count", "existing_match_count", "identity_conflict_count", "fuzzy_review_count",
    ]
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for candidate in candidates:
            writer.writerow(
                {
                    **{field: candidate.get(field, "") for field in fields},
                    "authors": "; ".join(candidate["authors"]),
                    "keywords": "; ".join(candidate["keywords"]),
                    "provenance_count": len(candidate["provenance"]),
                    "existing_match_count": len(candidate["existing_corpus_matches"]),
                    "identity_conflict_count": len(candidate["identity_conflicts"]),
                    "fuzzy_review_count": len(candidate["fuzzy_title_review"]),
                }
            )
    temporary.replace(path)


def update_manifest(manifest_path: Path, export_paths: list[Path]) -> None:
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {
            "schema_version": 1,
            "verification_id": ROUND_ID,
            "subject_direction_id": SUBJECT_DIRECTION_ID,
            "subject_title": SUBJECT_TITLE,
            "baseline_verification_id": BASELINE_VERIFICATION_ID,
            "created_at_utc": utc_now(),
            "input_export_provenance": [],
            "hashes": {},
        }
    if manifest.get("verification_id") != ROUND_ID or manifest.get("subject_direction_id") != SUBJECT_DIRECTION_ID:
        raise RuntimeError("Round manifest identity does not match D1-V002 / P1.")
    exports = []
    hashes = {}
    for path in export_paths:
        digest = sha256_file(path)
        exports.append({"path": str(path), "format": path.suffix.casefold().lstrip("."), "sha256": digest})
        hashes[str(path)] = digest
    manifest["input_export_provenance"] = exports
    manifest["hashes"] = hashes
    atomic_json(manifest_path, manifest)


def require_round_output_dir(output_dir: Path) -> None:
    if output_dir.name != ROUND_ID or output_dir.parent.name != "search_results":
        raise RuntimeError(
            "D1-V002 normalization outputs must be isolated under "
            "outputs/search_results/D1-V002 (or an equivalent test root)."
        )


def run_normalization(
    *,
    verification_id: str,
    input_dir: Path,
    output_dir: Path,
    manifest_path: Path,
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    evidence_dir: Path = DEFAULT_EVIDENCE_DIR,
    include_known_threats: bool = True,
) -> dict:
    if verification_id != ROUND_ID:
        raise RuntimeError(f"This implementation is isolated to {ROUND_ID}.")
    require_round_output_dir(output_dir)
    export_paths = sorted(
        path for path in input_dir.rglob("*") if path.is_file() and path.suffix.casefold() in {".csv", ".ris"}
    ) if input_dir.exists() else []
    records: list[dict] = []
    for path in export_paths:
        records.extend(parse_export(path))
    if include_known_threats:
        records.extend(known_threat_records())
    candidates, duplicate_events = merge_metadata_records(records)
    compare_with_existing(candidates, load_existing_metadata(registry_path, evidence_dir))
    flag_fuzzy_titles(candidates)
    candidates.sort(key=lambda item: (item["year"], item["normalized_title"], item["candidate_id"]), reverse=True)
    payload = {
        "schema_version": 1,
        "verification_id": ROUND_ID,
        "subject_direction_id": SUBJECT_DIRECTION_ID,
        "subject_title": SUBJECT_TITLE,
        "baseline_verification_id": BASELINE_VERIFICATION_ID,
        "generated_at_utc": utc_now(),
        "notice": "Metadata relevance is not scientific evidence. No candidate is verified by this output.",
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    report = {
        "schema_version": 1,
        "verification_id": ROUND_ID,
        "raw_record_count": len(records),
        "candidate_count": len(candidates),
        "merged_record_count": len(duplicate_events),
        "duplicate_events": duplicate_events,
        "identity_conflicts": [
            {"candidate_id": item["candidate_id"], "conflicts": item["identity_conflicts"]}
            for item in candidates if item["identity_conflicts"]
        ],
        "fuzzy_title_review": [
            {"candidate_id": item["candidate_id"], "matches": item["fuzzy_title_review"]}
            for item in candidates if item["fuzzy_title_review"]
        ],
        "existing_corpus_matches": [
            {"candidate_id": item["candidate_id"], "matches": item["existing_corpus_matches"]}
            for item in candidates if item["existing_corpus_matches"]
        ],
        "automatic_fuzzy_merging": False,
    }
    atomic_json(output_dir / "normalized_candidates.json", payload)
    write_candidates_csv(output_dir / "normalized_candidates.csv", candidates)
    atomic_json(output_dir / "deduplication_report.json", report)
    update_manifest(manifest_path, export_paths)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize CSV/RIS citation metadata for D1-V002 without registering papers.")
    parser.add_argument("--verification-id", required=True)
    parser.add_argument("--input-dir", type=Path, default=Path("data/search_exports/D1-V002/raw"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/search_results/D1-V002"))
    parser.add_argument("--manifest", type=Path, default=Path("data/search_exports/D1-V002/round_manifest.json"))
    args = parser.parse_args()
    payload = run_normalization(
        verification_id=args.verification_id,
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        manifest_path=args.manifest,
    )
    print(f"[ROUND] {payload['verification_id']} (scientific subject: {payload['subject_direction_id']})")
    print(f"[METADATA CANDIDATES] {payload['candidate_count']}")
    print("[NOTICE] Metadata relevance is not scientific evidence; no registry entries were created.")


if __name__ == "__main__":
    main()
