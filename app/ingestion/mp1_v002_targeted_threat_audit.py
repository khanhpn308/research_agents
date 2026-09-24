from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import Any

from app.ingestion.cross_round_adversarial_synthesis import (
    read_text,
    run_codex,
    sha256_bytes,
    sha256_file,
    timestamp_id,
    utc_now,
)

ROOT = Path(__file__).resolve().parents[2]
VERIFICATION_ID = "MP1-V002"
MIN_PAPERS = 8
OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
RUNS_DIR = OUT_DIR / "targeted_threat_runs"
MATRIX = OUT_DIR / "verification_matrix.json"
PROTOCOL = ROOT / "docs" / "protocols" / "MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md"
V001 = ROOT / "outputs" / "verification" / "MP1-V001" / "CORE_PRIOR_ART_AUDIT.json"
CANONICAL_JSON = OUT_DIR / "TARGETED_THREAT_AUDIT.json"
CANONICAL_MD = OUT_DIR / "TARGETED_THREAT_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "TARGETED_THREAT_AUDIT_raw.json"

STATUS = [
    "FALSIFIED",
    "SUBSTANTIALLY_NARROWED",
    "SURVIVES_CURRENT_FULL_TEXT_SET",
    "INCONCLUSIVE",
]
TARGET_STATUS = [
    "closed_by_full_text",
    "substantially_preempted",
    "open_in_current_full_text_set",
    "uncertain",
]

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status", "confidence", "executive_summary", "target_audit",
        "paper_threat_assessments", "narrowed_mechanics_core",
        "parameter_substitution_test", "citation_chase_plan",
        "recommended_next_action",
    ],
    "properties": {
        "status": {"type": "string", "enum": STATUS},
        "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
        "executive_summary": {"type": "string"},
        "target_audit": {
            "type": "array", "minItems": 3, "maxItems": 3,
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["target_id", "target", "status", "assessment", "evidence_paper_ids", "missing_mechanics"],
                "properties": {
                    "target_id": {"type": "string"},
                    "target": {"type": "string"},
                    "status": {"type": "string", "enum": TARGET_STATUS},
                    "assessment": {"type": "string"},
                    "evidence_paper_ids": {"type": "array", "items": {"type": "string"}},
                    "missing_mechanics": {"type": "array", "items": {"type": "string"}},
                },
            },
        },
        "paper_threat_assessments": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["paper_id", "title", "doi", "target_ids", "threat_level", "what_it_establishes", "what_it_does_not_establish", "backward_citation_priority"],
                "properties": {
                    "paper_id": {"type": "string"},
                    "title": {"type": "string"},
                    "doi": {"type": "string"},
                    "target_ids": {"type": "array", "items": {"type": "string"}},
                    "threat_level": {"type": "string", "enum": ["low", "medium", "high", "fatal"]},
                    "what_it_establishes": {"type": "string"},
                    "what_it_does_not_establish": {"type": "string"},
                    "backward_citation_priority": {"type": "string", "enum": ["none", "low", "medium", "high"]},
                },
            },
        },
        "narrowed_mechanics_core": {
            "type": "object", "additionalProperties": False,
            "required": [
                "niti_interwire_friction_prior_art_exists",
                "niti_phase_transformation_plus_interwire_friction_prior_art_exists",
                "pressure_controlled_niti_bundle_established",
                "pressure_dependent_bending_stiffness_established_for_niti_bundle",
                "survives_current_full_text_set",
                "provisional_surviving_question",
                "assessment",
            ],
            "properties": {
                "niti_interwire_friction_prior_art_exists": {"type": "boolean"},
                "niti_phase_transformation_plus_interwire_friction_prior_art_exists": {"type": "boolean"},
                "pressure_controlled_niti_bundle_established": {"type": "boolean"},
                "pressure_dependent_bending_stiffness_established_for_niti_bundle": {"type": "boolean"},
                "survives_current_full_text_set": {"type": "boolean"},
                "provisional_surviving_question": {"type": "string"},
                "assessment": {"type": "string"},
            },
        },
        "parameter_substitution_test": {
            "type": "object", "additionalProperties": False,
            "required": ["existing_elastic_fiber_model_appears_sufficient", "niti_requires_distinct_constitutive_contact_coupling", "evidence_status", "assessment"],
            "properties": {
                "existing_elastic_fiber_model_appears_sufficient": {"type": "boolean"},
                "niti_requires_distinct_constitutive_contact_coupling": {"type": "boolean"},
                "evidence_status": {"type": "string", "enum": ["established", "not_established", "conflicting", "insufficient"]},
                "assessment": {"type": "string"},
            },
        },
        "citation_chase_plan": {
            "type": "object", "additionalProperties": False,
            "required": ["required", "backward_priority_paper_ids", "forward_core_anchor_dois", "named_high_threat_sources", "stop_condition_satisfied", "rationale"],
            "properties": {
                "required": {"type": "boolean"},
                "backward_priority_paper_ids": {"type": "array", "items": {"type": "string"}},
                "forward_core_anchor_dois": {"type": "array", "items": {"type": "string"}},
                "named_high_threat_sources": {"type": "array", "items": {"type": "string"}},
                "stop_condition_satisfied": {"type": "boolean"},
                "rationale": {"type": "string"},
            },
        },
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def meta(path: Path, role: str) -> dict[str, Any]:
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
        "role": role,
    }


def build_prompt(sources: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for path in [PROTOCOL, V001, MATRIX]:
        rel = str(path.relative_to(ROOT))
        item = next(x for x in sources if x["path"] == rel)
        parts += ["=" * 100, f"SOURCE: {rel}", f"SHA256: {item['sha256']}", f"ROLE: {item['role']}", "=" * 100, read_text(path), ""]
    bundle = "\n".join(parts)
    return f"""
You are performing MP1-V002, an INTERIM TARGETED-THREAT audit for a proposed
MSc research direction using a superelastic NiTi wire bundle.

This is a FALSIFICATION task. Use ONLY the supplied source bundle for
scientific claims. The V002 matrix represents locally held full-text evidence.

This is NOT the final citation-chase verdict unless the supplied full texts
DIRECTLY falsify the mechanics core. The status SURVIVES_TARGETED_CITATION_CHASE
is intentionally unavailable because backward/forward citation coverage is not
closed yet.

AUDIT EXACTLY:
T1 — NiTi/Nitinol wires themselves form a contacting/slipping frictional bundle
     whose structural stiffness depends on inter-wire interaction.
T2 — externally applied positive/confining pressure radially/transversely
     compresses a metallic/NiTi bundle, changes normal force/friction, and
     changes structural stiffness.
T3 — NiTi superelastic/phase-transformation response is coupled with inter-wire
     contact/slip/friction, confinement pressure, hysteresis and structural
     stiffness.

STRICT DISTINCTIONS:
- NiTi wire-rope friction is relevant but is NOT automatically pressure-controlled jamming.
- Geometric helix contact, axial-load-induced contact pressure, manufacturing preload,
  or passive internal pressure are NOT an actively varied confinement-pressure control variable.
- A paper can close NiTi + friction + hysteresis while leaving pressure-controlled
  NiTi bundle mechanics open.
- Bending damping/hysteresis is not automatically variable stiffness.
- Material substitution alone is not novelty.
- Do not assert that NiTi requires a new coupled model unless the supplied evidence
  shows mechanics beyond simply substituting modulus/friction parameters.
- A thesis/dissertation is valid prior-mechanics evidence if its extracted full text supports the claim.

STATUS RULES:
FALSIFIED — direct prior art closes the surviving mechanics core or shows it reduces
             to established mechanics without a material new coupling.
SUBSTANTIALLY_NARROWED — major parts of T1/T3 are closed, but a narrower actively
                         pressure-controlled NiTi contact/slip/stiffness question remains.
SURVIVES_CURRENT_FULL_TEXT_SET — no direct kill in this matrix; citation chasing remains mandatory.
INCONCLUSIVE — evidence quality/coverage is insufficient.

If status is not FALSIFIED, citation_chase_plan.required MUST be true and
stop_condition_satisfied MUST be false. Select high-priority V002 paper_ids for
BACKWARD citation chasing and preserve relevant core anchor DOIs for FORWARD chasing.
Do not recommend broad keyword searching.

Return ONLY one JSON object matching the supplied schema.

SOURCE BUNDLE
{bundle}
""".strip()


def validate_result(result: dict[str, Any], matrix: dict[str, Any]) -> None:
    missing = set(SCHEMA["required"]) - set(result)
    if missing:
        raise RuntimeError("Missing output keys: " + ", ".join(sorted(missing)))
    targets = {x.get("target_id") for x in result["target_audit"]}
    if targets != {"T1", "T2", "T3"}:
        raise RuntimeError("target_audit must contain exactly T1, T2, T3.")
    matrix_ids = {str(x.get("paper_id", "")) for x in matrix.get("papers", [])}
    used = {pid for x in result["target_audit"] for pid in x.get("evidence_paper_ids", [])}
    unknown = used - matrix_ids
    if unknown:
        raise RuntimeError("Unknown V002 paper_ids in result: " + ", ".join(sorted(unknown)))
    plan = result["citation_chase_plan"]
    if result["status"] != "FALSIFIED":
        if not plan["required"] or plan["stop_condition_satisfied"]:
            raise RuntimeError("Non-falsified interim result must require open citation chasing.")
    if result["status"] == "FALSIFIED" and result["narrowed_mechanics_core"]["survives_current_full_text_set"]:
        raise RuntimeError("FALSIFIED conflicts with survives_current_full_text_set=true.")


def render_md(result: dict[str, Any], sources: list[dict[str, Any]], bundle_sha: str) -> str:
    lines = [
        "# MP1-V002 Interim Targeted-Threat Audit", "",
        f"- **Status:** {result['status']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Bundle SHA256:** {bundle_sha}", "",
        "## Executive summary", "", result["executive_summary"], "",
        "## Target audit", "",
    ]
    for x in result["target_audit"]:
        lines += [
            f"### {x['target_id']} — {x['status']}", "",
            x["assessment"], "",
            "**Evidence paper_ids:** " + (", ".join(x["evidence_paper_ids"]) or "none"), "",
            "**Missing mechanics:**",
        ]
        lines += [f"- {v}" for v in x["missing_mechanics"]] or ["- None."]
        lines.append("")
    lines += ["## Paper threat assessments", ""]
    for x in result["paper_threat_assessments"]:
        lines += [
            f"### {x['title']}", "",
            f"- paper_id: {x['paper_id']}", f"- DOI: {x['doi']}",
            f"- Targets: {', '.join(x['target_ids']) or 'none'}",
            f"- Threat: {x['threat_level']}",
            f"- Backward-citation priority: {x['backward_citation_priority']}",
            f"- Establishes: {x['what_it_establishes']}",
            f"- Does not establish: {x['what_it_does_not_establish']}", "",
        ]
    lines += ["## Narrowed mechanics core", ""]
    lines += [f"- **{k}:** {v}" for k, v in result["narrowed_mechanics_core"].items()]
    lines += ["", "## Parameter-substitution test", ""]
    lines += [f"- **{k}:** {v}" for k, v in result["parameter_substitution_test"].items()]
    lines += ["", "## Citation-chase plan", ""]
    lines += [f"- **{k}:** {v}" for k, v in result["citation_chase_plan"].items()]
    lines += ["", "## Recommended next action", "", result["recommended_next_action"], "", "## Provenance", ""]
    lines += [f"- {x['role']} — {x['path']} — SHA256 {x['sha256']}" for x in sources]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="MP1-V002 interim targeted-threat audit.")
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--model", default=os.getenv("CODEX_RESEARCH_MODEL", "").strip())
    parser.add_argument("--effort", default=os.getenv("CODEX_RESEARCH_EFFORT", "high").strip(), choices=["low", "medium", "high", "xhigh"])
    args = parser.parse_args()

    for path in [MATRIX, PROTOCOL, V001]:
        if not path.exists():
            raise RuntimeError(f"Required input not found: {path}")
    matrix = load_json(MATRIX)
    if matrix.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("Verification matrix ID mismatch.")
    if int(matrix.get("paper_count", 0)) < MIN_PAPERS:
        raise RuntimeError(f"{VERIFICATION_ID} requires at least {MIN_PAPERS} papers.")
    for p in matrix.get("papers", []):
        if p.get("screening_status") != "included" or p.get("ingestion_status") != "complete" or p.get("evidence_status") != "present":
            raise RuntimeError(f"{p.get('paper_id')}: incomplete V002 evidence state.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    sources = [meta(PROTOCOL, "V002_PROTOCOL"), meta(V001, "V001_BASELINE_AUDIT"), meta(MATRIX, "V002_FULL_TEXT_EVIDENCE_MATRIX")]
    bundle_sha = sha256_bytes("\n".join(f"{x['path']}:{x['sha256']}" for x in sources).encode("utf-8"))
    run_id = timestamp_id()
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    schema_path = run_dir / "output_schema.json"
    manifest_path = run_dir / "source_manifest.json"
    prompt_path = run_dir / "prompt.txt"
    raw_path = run_dir / "raw_model_output.json"
    result_json = run_dir / "TARGETED_THREAT_AUDIT.json"
    result_md = run_dir / "TARGETED_THREAT_AUDIT.md"

    schema_path.write_text(json.dumps(SCHEMA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_path.write_text(json.dumps({
        "run_id": run_id, "created_at_utc": utc_now().isoformat(),
        "verification_id": VERIFICATION_ID, "paper_count": matrix["paper_count"],
        "bundle_sha256": bundle_sha, "sources": sources,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    prompt = build_prompt(sources)
    prompt_path.write_text(prompt + "\n", encoding="utf-8")

    print(f"[VERIFICATION] {VERIFICATION_ID}")
    print(f"[PAPERS] {matrix['paper_count']}")
    print(f"[RUN] {run_id}")
    print(f"[BUNDLE SHA256] {bundle_sha}")
    if args.prepare_only:
        print("[PREPARE ONLY] PASS")
        return
    if not args.model:
        raise RuntimeError("CODEX_RESEARCH_MODEL is empty. Source .env or pass --model.")
    if CANONICAL_JSON.exists() and not args.force:
        raise RuntimeError(f"Canonical output already exists: {CANONICAL_JSON}. Use --force only intentionally.")

    run_codex(prompt=prompt, schema_path=schema_path, raw_output_path=raw_path, model=args.model, effort=args.effort)
    try:
        result = json.loads(read_text(raw_path).strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError("Model output is not valid JSON.") from exc
    if not isinstance(result, dict):
        raise RuntimeError("Model output must be a JSON object.")
    validate_result(result, matrix)
    result["_provenance"] = {
        "run_id": run_id, "created_at_utc": utc_now().isoformat(),
        "verification_id": VERIFICATION_ID, "paper_count": matrix["paper_count"],
        "evidence_bundle_sha256": bundle_sha, "model": args.model,
        "effort": args.effort, "final_v002_verdict": False,
    }
    result_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result_md.write_text(render_md(result, sources, bundle_sha), encoding="utf-8")
    shutil.copy2(result_json, CANONICAL_JSON)
    shutil.copy2(result_md, CANONICAL_MD)
    shutil.copy2(raw_path, CANONICAL_RAW)
    print(f"[STATUS] {result['status']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(f"[SAVED] {CANONICAL_JSON.relative_to(ROOT)}")
    print(f"[SAVED] {CANONICAL_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
