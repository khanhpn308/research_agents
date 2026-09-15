"""Recommend metadata-level screening decisions for D1-V002.

Recommendations are deterministic triage aids. This module never reads or
writes the paper registry and never treats metadata as scientific evidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from app.ingestion.normalize_citation_exports import (
    DEFAULT_CANDIDATES_PATH,
    DEFAULT_INPUT_DIR,
    DEFAULT_MANIFEST_PATH,
    DEFAULT_OUTPUT_DIR,
    DISCOVERY_STATUS,
    ROUND_ID,
    SUBJECT_DIRECTION_ID,
    SUBJECT_TITLE,
    validate_round_paths,
)


ALLOWED_RECOMMENDATIONS = {"include", "uncertain", "deprioritize", "exclude"}

CONCEPTS = {
    "layer_jamming": (r"\blayer[ -]?jamming\b", r"\blaminar[ -]?jamming\b", r"\bsheet[ -]?jamming\b"),
    "reduced_representation": (
        r"\bcontinuum(?:-based)? (?:model|formulation|representation)",
        r"\bcontinuum formulation", r"\bhomogeni[sz](?:ed|ation|ing)?\b",
        r"\bequivalent (?:model|representation)", r"\beffective (?:model|representation)",
        r"\breduced[ -]?order\b", r"\bconstitutive (?:model|formulation)",
        r"\bmacroscopic (?:model|formulation|representation)",
    ),
    "multilayer_mechanics": (r"\bmultilayer\b", r"\bmulti-layer\b", r"\blaminated beam\b", r"\blayered beam\b"),
    "slip_friction": (
        r"\binterlayer[ -]?slip\b", r"\bpartial interaction\b", r"\bprogressive slip\b",
        r"\bfriction(?:al)?\b", r"\bshear[ -]?lag\b",
    ),
    "layer_scaling": (
        r"\blayer[ -]?count(?: scaling)?\b", r"\bnumber of layers\b",
        r"\bhigh[ -]?layer[ -]?count\b", r"\blayer(?:ed)? scaling\b",
    ),
    "bending_stiffness": (r"\bbending\b", r"\bflexural\b", r"\bstiffness\b", r"\bbeam\b"),
    "validity_limits": (
        r"\bmodel validity\b", r"\bvalidity limits?\b", r"\bbreakdown limits?\b",
        r"\bbreakdown\b", r"\blimitation", r"\bmodel error\b", r"\bfail(?:ure|s)?\b",
    ),
    "validation": (r"\bexperimental", r"\bvalidation\b", r"\bfinite element", r"\bnumerical"),
    "application_control": (r"\bcontrol(?:ler)?\b", r"\bapplication\b", r"\bgripper\b", r"\bcontinuum robot"),
}

KNOWN_THREAT_DOIS = {
    "10.5194/ms-16-821-2025",
    "10.1007/s11465-025-0843-5",
    "10.1109/tcst.2026.3690756",
}


def _matched_concepts(text: str) -> list[str]:
    lowered = text.casefold()
    return [name for name, patterns in CONCEPTS.items() if any(re.search(pattern, lowered) for pattern in patterns)]


def recommend(candidate: dict) -> dict:
    text = " ".join(
        [candidate.get("title", ""), candidate.get("abstract", ""), " ".join(candidate.get("keywords", []))]
    )
    matched = _matched_concepts(text)
    metadata_complete = bool(candidate.get("abstract", "").strip() or candidate.get("keywords", []))
    is_known_threat = candidate.get("normalized_doi", "").casefold() in KNOWN_THREAT_DOIS
    direct = "layer_jamming" in matched
    representation = "reduced_representation" in matched
    mechanics = bool({"multilayer_mechanics", "slip_friction", "layer_scaling", "bending_stiffness"} & set(matched))
    limits_or_validation = bool({"validity_limits", "validation"} & set(matched))
    score = (
        4 * direct
        + 4 * representation
        + 2 * mechanics
        + 2 * limits_or_validation
        + int("slip_friction" in matched)
        + int("layer_scaling" in matched)
    )
    if candidate.get("identity_conflicts"):
        recommendation = "uncertain"
        reason = "Bibliographic identity conflict requires human resolution before relevance screening."
    elif direct and representation and mechanics:
        recommendation = "include"
        reason = "Metadata directly combines layer jamming, a reduced/continuum representation, and relevant mechanics."
    elif direct and representation:
        recommendation = "include"
        reason = "Metadata directly combines layer jamming with a reduced/continuum modeling concept; full text is required."
    elif direct and (mechanics or limits_or_validation):
        recommendation = "uncertain"
        reason = "Metadata is relevant to layer-jamming mechanics but does not establish the required representation or scope."
    elif mechanics and representation:
        recommendation = "deprioritize"
        reason = "Metadata concerns adjacent reduced multilayer mechanics without explicit layer/laminar jamming."
    elif direct and "application_control" in matched:
        recommendation = "deprioritize"
        reason = "Metadata appears application/control-led and does not yet show a new jamming-mechanics model."
    elif direct:
        recommendation = "uncertain"
        reason = "Layer-jamming identity alone does not establish relevance to P1's model/mechanics question."
    elif not metadata_complete:
        recommendation = "uncertain"
        reason = "Metadata is too incomplete for definitive exclusion; abstract, keywords, or full text are needed."
    else:
        recommendation = "exclude"
        reason = "Metadata does not show material relevance to the P1 verification question."
    if is_known_threat and recommendation in {"deprioritize", "exclude"}:
        recommendation = "uncertain"
        reason = "Known P1 threat retained for full-text review; incomplete metadata cannot justify deprioritization or exclusion."
    assert recommendation in ALLOWED_RECOMMENDATIONS
    screening_confidence = "low" if not metadata_complete or candidate.get("identity_conflicts") else "medium"
    return {
        "candidate_id": candidate.get("candidate_id", ""),
        "title": candidate.get("title", ""),
        "doi": candidate.get("normalized_doi", ""),
        "year": candidate.get("year", ""),
        "recommendation": recommendation,
        "rank_score": score,
        "matched_concepts": matched,
        "reason": reason,
        "candidate_status": DISCOVERY_STATUS,
        "metadata_only": True,
        "scientific_evidence": False,
        "human_approval_required": True,
        "metadata_complete_for_screening": metadata_complete,
        "known_threat": is_known_threat,
        "screening_confidence": screening_confidence,
    }


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)


def write_csv(path: Path, recommendations: list[dict]) -> None:
    fields = [
        "candidate_id", "title", "doi", "year", "recommendation", "rank_score",
        "matched_concepts", "reason", "candidate_status", "metadata_only",
        "scientific_evidence", "human_approval_required",
        "metadata_complete_for_screening", "known_threat",
        "screening_confidence",
    ]
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in recommendations:
            row = dict(item)
            row["matched_concepts"] = "; ".join(item["matched_concepts"])
            writer.writerow(row)
    temporary.replace(path)


def validate_screening_paths(*, candidates_path: Path, output_dir: Path) -> None:
    validate_round_paths(
        input_dir=DEFAULT_INPUT_DIR, output_dir=output_dir,
        manifest_path=DEFAULT_MANIFEST_PATH,
    )
    if candidates_path.absolute() != DEFAULT_CANDIDATES_PATH:
        raise RuntimeError(f"D1-V002 candidates path must be exactly {DEFAULT_CANDIDATES_PATH}.")
    if candidates_path.resolve(strict=False) != DEFAULT_CANDIDATES_PATH:
        raise RuntimeError("D1-V002 candidates path contains a symlink or escapes the repository.")


def run_screening(
    *, verification_id: str, candidates_path: Path, output_dir: Path,
    enforce_production_paths: bool = True,
) -> dict:
    if verification_id != ROUND_ID:
        raise RuntimeError(f"This implementation is isolated to {ROUND_ID}.")
    if enforce_production_paths:
        validate_screening_paths(candidates_path=candidates_path, output_dir=output_dir)
    data = json.loads(candidates_path.read_text(encoding="utf-8"))
    if data.get("verification_id") != ROUND_ID or data.get("subject_direction_id") != SUBJECT_DIRECTION_ID:
        raise RuntimeError("Candidate ledger is not for D1-V002 / P1.")
    recommendations = [recommend(candidate) for candidate in data.get("candidates", [])]
    recommendations.sort(key=lambda item: (-item["rank_score"], item["title"].casefold(), item["candidate_id"]))
    payload = {
        "schema_version": 1,
        "verification_id": ROUND_ID,
        "subject_direction_id": SUBJECT_DIRECTION_ID,
        "subject_title": SUBJECT_TITLE,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "notice": (
            "Recommendations are metadata-only triage. Metadata relevance is not scientific evidence, "
            "and no paper is verified or approved for the corpus by this output."
        ),
        "allowed_recommendations": sorted(ALLOWED_RECOMMENDATIONS),
        "recommendation_count": len(recommendations),
        "recommendations": recommendations,
    }
    atomic_json(output_dir / "metadata_screening_recommendations.json", payload)
    write_csv(output_dir / "metadata_screening_recommendations.csv", recommendations)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate recommendation-only metadata screening for P1 / D1-V002.")
    parser.add_argument("--verification-id", required=True)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    payload = run_screening(
        verification_id=args.verification_id,
        candidates_path=args.candidates,
        output_dir=args.output_dir,
    )
    print(f"[ROUND] {payload['verification_id']} (scientific subject: {payload['subject_direction_id']})")
    print(f"[RECOMMENDATIONS] {payload['recommendation_count']}")
    print("[NOTICE] Recommendations only; metadata is not scientific evidence and the registry was not modified.")


if __name__ == "__main__":
    main()
