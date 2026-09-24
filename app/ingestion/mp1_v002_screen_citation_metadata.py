"""Metadata-only triage for MP1-V002 citation-chasing exports.

This module reads Scopus CSV exports under data/search_exports/MP1-V002/raw,
deduplicates records, assigns deterministic threat-oriented triage labels, and
writes review artifacts. It never modifies the paper registry and never treats
metadata as scientific evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
ROUND_ID = "MP1-V002"
DEFAULT_INPUT_DIR = ROOT / "data" / "search_exports" / ROUND_ID / "raw"
DEFAULT_OUTPUT_DIR = ROOT / "outputs" / "verification" / ROUND_ID / "citation_screening"

ALLOWED = {
    "POTENTIAL_KILL_PAPER",
    "GET_FULL_TEXT",
    "KEEP_METADATA",
    "EXCLUDE",
    "UNCERTAIN",
}

FIELD_ALIASES = {
    "title": ["Title", "Document Title", "Article Title"],
    "abstract": ["Abstract", "Description"],
    "doi": ["DOI", "Doi"],
    "year": ["Year", "Publication Year"],
    "authors": ["Authors", "Author(s)"],
    "source": ["Source title", "Source Title", "Publication Name"],
    "author_keywords": ["Author Keywords", "Author keywords"],
    "index_keywords": ["Index Keywords", "Keywords Plus"],
}

PATTERNS = {
    "niti_sma": [
        r"\bniti\b", r"\bnitinol\b", r"\bshape memory alloy\b", r"\bsuperelastic\b",
    ],
    "wire_bundle": [
        r"\bwire(?: |-)?bundle\b", r"\bwire rope\b", r"\bstrand(?:s)?\b",
        r"\bcable(?:s)?\b", r"\bmicro[- ]?cable(?:s)?\b", r"\bmicrofilament(?:s)?\b",
        r"\bbraid(?:ed|ing)?\b", r"\bmetallic (?:wire|fiber)",
    ],
    "contact_friction": [
        r"\binter[- ]?wire\b", r"\binterfilament\b", r"\bcontact\b",
        r"\bfriction(?:al)?\b", r"\bstick[- ]?slip\b", r"\bslip(?:ping)?\b",
        r"\bsliding\b",
    ],
    "pressure_control": [
        r"\bconfin(?:e|ed|ement|ing)\b", r"\bradial pressure\b",
        r"\btransverse pressure\b", r"\bexternal pressure\b",
        r"\bpositive pressure\b", r"\bpressure[- ]controlled\b",
        r"\bradial compression\b", r"\btransverse compression\b",
        r"\bcompressive preload\b", r"\bpreload\b", r"\bnormal force\b",
    ],
    "bending_stiffness": [
        r"\bbending\b", r"\bflexural\b", r"\bstiffness\b", r"\brigidity\b",
        r"\bcurvature\b", r"\bmoment[- ]curvature\b",
    ],
    "phase_hysteresis": [
        r"\bmartensit(?:e|ic)\b", r"\bphase transformation\b",
        r"\bsuperelastic(?:ity)?\b", r"\bhysteresis\b", r"\bdamping\b",
        r"\benergy dissipation\b",
    ],
    "jamming": [
        r"\bjamming\b", r"\bfrictional stiffening\b", r"\blocking\b",
    ],
    "active_pressure_signal": [
        r"\bvariable pressure\b", r"\bpressure (?:was|is|were) varied\b",
        r"\bpressure range\b", r"\bpressure levels?\b", r"\bapplied pressure\b",
        r"\binflatable bladder\b", r"\bpressur(?:ize|ized|ization)\b",
    ],
}


def norm_space(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def norm_title(value: str) -> str:
    value = norm_space(value).casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def norm_doi(value: str) -> str:
    value = norm_space(value).casefold()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    value = re.sub(r"^doi:\s*", "", value)
    return value.strip().rstrip(".,;)")


def first(row: dict[str, Any], aliases: list[str]) -> str:
    for key in aliases:
        if key in row and norm_space(row[key]):
            return norm_space(row[key])
    return ""


def parse_csv(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for n, row in enumerate(reader, start=2):
            item = {name: first(row, aliases) for name, aliases in FIELD_ALIASES.items()}
            item["doi"] = norm_doi(item["doi"])
            item["branch_file"] = path.relative_to(DEFAULT_INPUT_DIR).as_posix()
            item["source_line"] = n
            out.append(item)
    return out


def matched(text: str) -> list[str]:
    low = text.casefold()
    return [
        name for name, patterns in PATTERNS.items()
        if any(re.search(p, low) for p in patterns)
    ]


def classify(item: dict[str, Any]) -> dict[str, Any]:
    text = " ".join([
        item.get("title", ""),
        item.get("abstract", ""),
        item.get("author_keywords", ""),
        item.get("index_keywords", ""),
    ])
    concepts = set(matched(text))
    metadata_complete = bool(item.get("abstract") or item.get("author_keywords") or item.get("index_keywords"))

    material_bundle = "wire_bundle" in concepts
    niti = "niti_sma" in concepts
    contact = "contact_friction" in concepts
    pressure = "pressure_control" in concepts
    active_pressure = "active_pressure_signal" in concepts
    bending = "bending_stiffness" in concepts
    phase = "phase_hysteresis" in concepts
    jamming = "jamming" in concepts

    # Deliberately conservative: metadata can only flag potential kill papers.
    if material_bundle and contact and pressure and bending and (niti or active_pressure):
        rec = "POTENTIAL_KILL_PAPER"
        reason = (
            "Metadata combines a wire/cable bundle, contact/friction/slip, pressure/confinement, "
            "and structural stiffness/bending; full text is required to determine whether pressure "
            "is actively varied and whether the mechanism directly threatens T2/T3."
        )
        score = 100
    elif (
        (niti and material_bundle and contact and (bending or phase))
        or (material_bundle and pressure and bending)
        or (jamming and pressure and bending)
        or (niti and material_bundle and pressure)
    ):
        rec = "GET_FULL_TEXT"
        reason = (
            "Metadata shows a strong T1/T2/T3 mechanics connection but does not establish a direct kill. "
            "Full text is needed to classify pressure as passive, fixed preload, or actively controlled."
        )
        score = 70
    elif (
        (material_bundle and (contact or bending or pressure))
        or (niti and (contact or phase or bending))
        or (jamming and (pressure or bending))
    ):
        rec = "KEEP_METADATA"
        reason = (
            "Metadata is adjacent to the surviving mechanics question but does not show the full "
            "pressure-contact-stiffness coupling."
        )
        score = 40
    elif not metadata_complete:
        rec = "UNCERTAIN"
        reason = "Metadata is incomplete; title alone is insufficient for confident exclusion."
        score = 20
    else:
        rec = "EXCLUDE"
        reason = "Metadata does not show a concrete T1/T2/T3 mechanics threat."
        score = 0

    return {
        "recommendation": rec,
        "rank_score": score,
        "matched_concepts": sorted(concepts),
        "reason": reason,
        "metadata_only": True,
        "scientific_evidence": False,
        "human_review_required": True,
    }


def merge_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in records:
        doi = item.get("doi", "")
        title_key = norm_title(item.get("title", ""))
        key = f"doi:{doi}" if doi else f"title:{title_key}"
        groups[key].append(item)

    merged: list[dict[str, Any]] = []
    for key, items in groups.items():
        base = max(items, key=lambda x: len(x.get("abstract", ""))).copy()
        branches = sorted({x["branch_file"] for x in items})
        lines = sorted({f"{x['branch_file']}:{x['source_line']}" for x in items})
        base["branch_files"] = branches
        base["source_locations"] = lines
        base["duplicate_count"] = len(items) - 1
        base["candidate_id"] = hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]
        base.update(classify(base))
        merged.append(base)

    merged.sort(
        key=lambda x: (
            -int(x["rank_score"]),
            -(int(x["year"]) if str(x.get("year", "")).isdigit() else 0),
            x.get("title", "").casefold(),
        )
    )
    return merged


def write_csv(path: Path, items: list[dict[str, Any]]) -> None:
    fields = [
        "candidate_id", "recommendation", "rank_score", "title", "year", "doi",
        "authors", "source", "matched_concepts", "branch_files", "duplicate_count",
        "reason", "human_review_required", "metadata_only", "scientific_evidence",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in items:
            row = {k: item.get(k, "") for k in fields}
            row["matched_concepts"] = "; ".join(item.get("matched_concepts", []))
            row["branch_files"] = "; ".join(item.get("branch_files", []))
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Screen MP1-V002 citation metadata.")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()
    if not input_dir.exists():
        raise RuntimeError(f"Input directory not found: {input_dir}")

    csv_paths = sorted(input_dir.rglob("*.csv"))
    if not csv_paths:
        raise RuntimeError(f"No CSV exports found under {input_dir}")

    records: list[dict[str, Any]] = []
    for path in csv_paths:
        records.extend(parse_csv(path))

    candidates = merge_records(records)
    output_dir.mkdir(parents=True, exist_ok=True)

    counts = {label: 0 for label in sorted(ALLOWED)}
    for item in candidates:
        counts[item["recommendation"]] += 1

    payload = {
        "schema_version": 1,
        "verification_id": ROUND_ID,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "notice": (
            "Metadata-only triage. Recommendations are not scientific evidence, do not prove novelty, "
            "and do not modify the registry. Human review is mandatory before obtaining/registering full text."
        ),
        "input_csv_count": len(csv_paths),
        "raw_record_count": len(records),
        "deduplicated_candidate_count": len(candidates),
        "recommendation_counts": counts,
        "candidates": candidates,
    }

    (output_dir / "METADATA_SCREENING.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_csv(output_dir / "METADATA_SCREENING.csv", candidates)

    shortlist = [
        x for x in candidates
        if x["recommendation"] in {"POTENTIAL_KILL_PAPER", "GET_FULL_TEXT"}
    ]
    write_csv(output_dir / "FULL_TEXT_SHORTLIST.csv", shortlist)

    print(f"[ROUND] {ROUND_ID}")
    print(f"[CSV EXPORTS] {len(csv_paths)}")
    print(f"[RAW RECORDS] {len(records)}")
    print(f"[DEDUP CANDIDATES] {len(candidates)}")
    for label in ["POTENTIAL_KILL_PAPER", "GET_FULL_TEXT", "KEEP_METADATA", "UNCERTAIN", "EXCLUDE"]:
        print(f"[{label}] {counts[label]}")
    print(f"[SHORTLIST] {len(shortlist)}")
    print(f"[SAVED] {(output_dir / 'METADATA_SCREENING.csv').relative_to(ROOT)}")
    print(f"[SAVED] {(output_dir / 'FULL_TEXT_SHORTLIST.csv').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
