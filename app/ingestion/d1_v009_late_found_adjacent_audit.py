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

VERIFICATION_ID = "D1-V009"
EXPECTED_TITLE_FRAGMENT = "modelling the large deformations in stratified media"

OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
RUNS_DIR = OUT_DIR / "late_found_runs"

REGISTRY_PATH = ROOT / "data" / "paper_registry.json"
CURRENT_MATRIX = OUT_DIR / "verification_matrix.json"

PRIOR_FINAL_AUDIT = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V008"
    / "FINAL_NAMED_TARGET_AUDIT.json"
)

SEMANTIC_CORRECTION = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V007"
    / "C04_SEMANTIC_CORRECTION.md"
)

PLAN_PATH = (
    ROOT
    / "docs"
    / "protocols"
    / "D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md"
)

CANONICAL_JSON = OUT_DIR / "LATE_FOUND_ADJACENT_AUDIT.json"
CANONICAL_MD = OUT_DIR / "LATE_FOUND_ADJACENT_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "LATE_FOUND_ADJACENT_AUDIT_raw.json"

STATUS_ENUM = [
    "FALSIFIES_FINAL_P1",
    "SUBSTANTIALLY_NARROWS_FINAL_P1",
    "SURVIVES_LATE_FOUND_TARGET",
    "INCONCLUSIVE",
]

THREAT_ENUM = ["low", "medium", "high", "fatal"]

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "current_p1",
        "target_identity",
        "executive_summary",
        "mechanics_overlap",
        "kill_test",
        "what_it_proves",
        "what_it_does_not_prove",
        "effect_on_final_claims",
        "new_named_threats",
        "lock_decision",
        "recommended_next_action",
    ],
    "properties": {
        "status": {"type": "string", "enum": STATUS_ENUM},
        "confidence": {
            "type": "string",
            "enum": ["low", "medium", "high"],
        },
        "current_p1": {"type": "string"},
        "target_identity": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "paper_id",
                "title",
                "year",
                "doi",
                "verified_full_text",
            ],
            "properties": {
                "paper_id": {"type": "string"},
                "title": {"type": "string"},
                "year": {"type": ["string", "integer", "null"]},
                "doi": {"type": "string"},
                "verified_full_text": {"type": "boolean"},
            },
        },
        "executive_summary": {"type": "string"},
        "mechanics_overlap": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "equivalent_or_smeared_continuum",
                "cosserat_or_generalized_continuum",
                "large_deformation",
                "layer_bending_stiffness",
                "frictional_or_plastic_interface_slip",
                "interface_opening_or_separation",
                "finite_element_implementation",
                "quantitative_validation",
                "assessment",
            ],
            "properties": {
                "equivalent_or_smeared_continuum": {"type": "boolean"},
                "cosserat_or_generalized_continuum": {"type": "boolean"},
                "large_deformation": {"type": "boolean"},
                "layer_bending_stiffness": {"type": "boolean"},
                "frictional_or_plastic_interface_slip": {"type": "boolean"},
                "interface_opening_or_separation": {"type": "boolean"},
                "finite_element_implementation": {"type": "boolean"},
                "quantitative_validation": {"type": "boolean"},
                "assessment": {"type": "string"},
            },
        },
        "kill_test": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "named_reduced_or_continuum_model",
                "interface_resolved_or_discrete_reference",
                "quantitative_model_form_error",
                "finite_parameter_or_discreteness_sweep",
                "predeclared_acceptance_tolerance",
                "tolerance_defined_breakdown_boundary",
                "experiment_tests_both_sides_of_boundary",
                "vacuum_specific_contact_mechanics",
                "transferable_to_vacuum_layer_jamming_without_new_mechanics",
                "kill_condition_met",
                "evidence_summary",
            ],
            "properties": {
                "named_reduced_or_continuum_model": {"type": "boolean"},
                "interface_resolved_or_discrete_reference": {"type": "boolean"},
                "quantitative_model_form_error": {"type": "boolean"},
                "finite_parameter_or_discreteness_sweep": {"type": "boolean"},
                "predeclared_acceptance_tolerance": {"type": "boolean"},
                "tolerance_defined_breakdown_boundary": {"type": "boolean"},
                "experiment_tests_both_sides_of_boundary": {"type": "boolean"},
                "vacuum_specific_contact_mechanics": {"type": "boolean"},
                "transferable_to_vacuum_layer_jamming_without_new_mechanics": {
                    "type": "boolean"
                },
                "kill_condition_met": {"type": "boolean"},
                "evidence_summary": {"type": "string"},
            },
        },
        "what_it_proves": {
            "type": "array",
            "items": {"type": "string"},
        },
        "what_it_does_not_prove": {
            "type": "array",
            "items": {"type": "string"},
        },
        "effect_on_final_claims": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "claims_no_longer_safe",
                "claims_still_defensible",
                "scope_change_required",
                "assessment",
            ],
            "properties": {
                "claims_no_longer_safe": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "claims_still_defensible": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "scope_change_required": {"type": "boolean"},
                "assessment": {"type": "string"},
            },
        },
        "new_named_threats": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "identifier",
                    "why_high_threat",
                    "explicitly_named_in_supplied_evidence",
                    "requires_targeted_full_text_audit",
                ],
                "properties": {
                    "identifier": {"type": "string"},
                    "why_high_threat": {"type": "string"},
                    "explicitly_named_in_supplied_evidence": {"type": "boolean"},
                    "requires_targeted_full_text_audit": {"type": "boolean"},
                },
            },
        },
        "lock_decision": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "final_novelty_lock_survives",
                "reopen_broad_search",
                "targeted_followup_required",
                "threat_to_final_p1",
                "rationale",
            ],
            "properties": {
                "final_novelty_lock_survives": {"type": "boolean"},
                "reopen_broad_search": {"type": "boolean"},
                "targeted_followup_required": {"type": "boolean"},
                "threat_to_final_p1": {
                    "type": "string",
                    "enum": THREAT_ENUM,
                },
                "rationale": {"type": "string"},
            },
        },
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def registry_papers() -> list[dict[str, Any]]:
    registry = load_json(REGISTRY_PATH)
    if isinstance(registry, dict):
        return registry.get("papers", [])
    if isinstance(registry, list):
        return registry
    raise RuntimeError("Unsupported registry format.")


def target_registry_record() -> dict[str, Any]:
    matches = [
        paper
        for paper in registry_papers()
        if paper.get("source_type") == "verification"
        and paper.get("verification_id") == VERIFICATION_ID
        and paper.get("screening_status") != "excluded"
    ]

    if len(matches) != 1:
        raise RuntimeError(
            f"{VERIFICATION_ID} must contain exactly one non-excluded paper; "
            f"found {len(matches)}."
        )

    paper = matches[0]

    if paper.get("screening_status") != "included":
        raise RuntimeError(
            f"{paper.get('paper_id')}: screening_status="
            f"{paper.get('screening_status')!r}; expected 'included'."
        )

    if paper.get("ingestion_status") != "complete":
        raise RuntimeError(
            f"{paper.get('paper_id')}: ingestion_status="
            f"{paper.get('ingestion_status')!r}; expected 'complete'."
        )

    if paper.get("evidence_status") != "present":
        raise RuntimeError(
            f"{paper.get('paper_id')}: evidence_status="
            f"{paper.get('evidence_status')!r}; expected 'present'."
        )

    return paper


def target_evidence_path(paper: dict[str, Any]) -> Path:
    rel = paper.get("evidence_file")
    if not rel:
        raise RuntimeError(f"{paper.get('paper_id')}: evidence_file missing.")

    path = ROOT / "data" / str(rel)
    if not path.exists():
        raise RuntimeError(f"Evidence file not found: {path}")

    return path


def source_metadata(path: Path, role: str) -> dict[str, Any]:
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
        "role": role,
    }


def build_prompt(
    target_evidence: Path,
    source_meta: list[dict[str, Any]],
) -> str:
    ordered_sources = [
        PRIOR_FINAL_AUDIT,
        SEMANTIC_CORRECTION,
        PLAN_PATH,
        CURRENT_MATRIX,
        target_evidence,
    ]

    blocks: list[str] = []

    for path in ordered_sources:
        rel = str(path.relative_to(ROOT))
        meta = next(item for item in source_meta if item["path"] == rel)
        blocks.append(
            "\n".join(
                [
                    "",
                    "=" * 100,
                    f"SOURCE: {rel}",
                    f"SHA256: {meta['sha256']}",
                    f"ROLE: {meta['role']}",
                    "=" * 100,
                    "",
                    read_text(path),
                    "",
                ]
            )
        )

    bundle = "\n".join(blocks)

    return f"""
You are performing D1-V009, a POST-LOCK LATE-FOUND ADJACENT-MECHANICS
adversarial audit for an MSc research project on vacuum layer jamming.

This is a FALSIFICATION task. Do not defend the current project.

Use ONLY the supplied source bundle for scientific claims. The target
paper evidence was extracted from a locally held full-text PDF. Do not
invent equations, experiments, DOI metadata, thresholds, chronology, or
transferability.

CURRENT SURVIVING P1

For one specified reduced/continuum vacuum-layer-jamming beam model
under quasi-static planar bending, define output-specific PREDECLARED
model-form acceptance tolerances and determine experimentally validated
validity/breakdown boundaries against an interface-resolving/full-layer
reference, while explicitly accounting for vacuum-pressure-controlled
normal contact, friction/slip evolution, and, where necessary, pressure
redistribution or layer separation.

The prior D1-V008 audit allowed a provisional final novelty lock and
stopped broad searching. D1-V009 exists because a relevant older paper
was discovered after that stop condition.

Do NOT assume the lock survives. Test it.

TARGET ROLE

The target is Adhikary, Mühlhaus, and Dyskin (1999),
"Modelling the large deformations in stratified media—the Cosserat
continuum approach."

Audit whether it establishes:
- an equivalent or smeared continuum for layered media;
- generalized/Cosserat kinematics;
- bending stiffness via couple stresses;
- large deformation;
- elastic/plastic frictional interface slip;
- interface opening/separation;
- finite-element implementation;
- quantitative verification.

These are questions, not assumptions.

STRICT SEMANTIC GUARDRAILS

1. PREDECLARED means fixed before the relevant validation/model-error
   results were inspected, with that temporal ordering supported by the
   supplied evidence.

2. An observed percentage error is NOT automatically a predeclared
   acceptance tolerance.

3. A physical threshold such as buckling onset, yielding, opening,
   delamination, or a load fraction at which geometric nonlinearity
   becomes important is NOT automatically a tolerance-defined
   model-form validity boundary.

4. Agreement between a continuum FE model and an analytical limiting
   solution is verification of that formulation/case. It is NOT
   automatically a reduced-continuum-versus-explicit-interface
   model-form error study.

5. Prior experimental photographs or external experiments cited for
   physical context are NOT automatically experiments validating the
   proposed continuum model.

6. Do NOT call a parameter sweep a finite-layer/discreteness validity
   sweep unless it actually varies the relevant discreteness or a
   parameter used to test reduced-model validity against a stronger
   reference.

7. Do NOT infer direct transferability to vacuum layer jamming merely
   because Coulomb or Mohr-Coulomb friction appears.

PRIMARY QUESTIONS

A. What mechanics precedent does the paper establish?
B. Which broad novelty claims are no longer safe after considering it?
C. Does it contain an interface-resolving/discrete reference against
   which its continuum approximation is quantitatively benchmarked?
D. Does it compute model-form error over layer count/discreteness,
   pressure/preload, deformation, or another governing parameter?
E. Does it use an output-specific PREDECLARED acceptance tolerance to
   classify a validity domain?
F. Does it experimentally test points intentionally chosen on both
   accepted and rejected sides of that tolerance-defined boundary?
G. Does its interface/contact law transfer to vacuum layer jamming
   without materially new mechanics for vacuum-generated normal contact,
   pressure redistribution, friction/slip evolution, and possible
   separation?
H. Does it name a concrete high-threat source requiring targeted audit?

KILL CONDITION

A kill requires the supplied evidence to establish:
- named reduced/continuum layered model;
- interface-resolving/discrete reference;
- quantitative model-form discrepancy;
- finite parameter/discreteness sweep relevant to validity;
- predeclared output-specific acceptance tolerance;
- tolerance-defined validity/breakdown boundary;
- experiment intentionally sampling both sides of that boundary;
- transferability to vacuum layer jamming without materially new contact
  mechanics.

If the complete chain is not established, kill_condition_met MUST be
false.

STATUS RULES

FALSIFIES_FINAL_P1:
The target closes the substantive surviving contribution.

SUBSTANTIALLY_NARROWS_FINAL_P1:
The target removes a major piece of the surviving contribution or
requires a material scope/title/RQ revision, but does not fully kill it.

SURVIVES_LATE_FOUND_TARGET:
The target is important theoretical precedent but final P1 remains
materially intact.

INCONCLUSIVE:
The supplied evidence is insufficient to decide.

SEARCH DECISION

Do NOT reopen broad searching merely because the target has a long
reference list. Set targeted_followup_required=true only when a concrete
named source or specific unresolved evidentiary issue is identified.

SOURCE BUNDLE

{bundle}
"""


def validate_result(result: dict[str, Any]) -> None:
    missing = set(SCHEMA["required"]) - set(result)
    if missing:
        raise RuntimeError(
            "Model output missing required keys: "
            + ", ".join(sorted(missing))
        )

    if result["status"] not in STATUS_ENUM:
        raise RuntimeError(f"Invalid status: {result['status']!r}")

    kill = result["kill_test"]["kill_condition_met"]

    if result["status"] == "FALSIFIES_FINAL_P1" and not kill:
        raise RuntimeError(
            "Scientific guardrail violation: FALSIFIES_FINAL_P1 "
            "requires kill_condition_met=true."
        )

    if kill and result["lock_decision"]["final_novelty_lock_survives"]:
        raise RuntimeError(
            "Scientific guardrail violation: a satisfied kill condition "
            "cannot preserve the final novelty lock."
        )


def render_markdown(
    result: dict[str, Any],
    manifest: list[dict[str, Any]],
    bundle_sha256: str,
) -> str:
    ident = result["target_identity"]
    overlap = result["mechanics_overlap"]
    kill = result["kill_test"]
    effects = result["effect_on_final_claims"]
    lock = result["lock_decision"]

    lines: list[str] = [
        "# D1-V009 Late-Found Adjacent-Mechanics Audit",
        "",
        f"- **Status:** {result['status']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Bundle SHA256:** {bundle_sha256}",
        f"- **Kill condition met:** {kill['kill_condition_met']}",
        f"- **Final novelty lock survives:** "
        f"{lock['final_novelty_lock_survives']}",
        "",
        "## Current P1",
        "",
        result["current_p1"],
        "",
        "## Target identity",
        "",
        f"- paper_id: {ident['paper_id']}",
        f"- Title: {ident['title']}",
        f"- Year: {ident['year']}",
        f"- DOI: {ident['doi']}",
        f"- Verified full text: {ident['verified_full_text']}",
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## Mechanics overlap",
        "",
    ]

    for key, value in overlap.items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(["", "## Kill test", ""])
    for key, value in kill.items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(["", "## What the paper proves", ""])
    for item in result["what_it_proves"]:
        lines.append(f"- {item}")

    lines.extend(["", "## What the paper does NOT prove", ""])
    for item in result["what_it_does_not_prove"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Effect on final claims", ""])
    lines.extend(["### Claims no longer safe", ""])

    if effects["claims_no_longer_safe"]:
        for item in effects["claims_no_longer_safe"]:
            lines.append(f"- {item}")
    else:
        lines.append("- None established.")

    lines.extend(["", "### Claims still defensible", ""])

    if effects["claims_still_defensible"]:
        for item in effects["claims_still_defensible"]:
            lines.append(f"- {item}")
    else:
        lines.append("- None established.")

    lines.extend(
        [
            "",
            f"- **Scope change required:** {effects['scope_change_required']}",
            f"- **Assessment:** {effects['assessment']}",
            "",
            "## New named threats",
            "",
        ]
    )

    if result["new_named_threats"]:
        for item in result["new_named_threats"]:
            lines.extend(
                [
                    f"### {item['identifier']}",
                    "",
                    f"- Why high threat: {item['why_high_threat']}",
                    f"- Explicitly named in supplied evidence: "
                    f"{item['explicitly_named_in_supplied_evidence']}",
                    f"- Requires targeted full-text audit: "
                    f"{item['requires_targeted_full_text_audit']}",
                    "",
                ]
            )
    else:
        lines.append("None.")

    lines.extend(["", "## Lock decision", ""])
    for key, value in lock.items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            "## Recommended next action",
            "",
            result["recommended_next_action"],
            "",
            "## Provenance",
            "",
        ]
    )

    for item in manifest:
        lines.append(
            f"- {item['role']} — {item['path']} — SHA256 {item['sha256']}"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "D1-V009 post-lock late-found adjacent-mechanics "
            "adversarial audit."
        )
    )
    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help="Build run directory, schema, manifest, and prompt only.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace canonical latest outputs after a successful run.",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("CODEX_RESEARCH_MODEL", ""),
    )
    parser.add_argument(
        "--effort",
        default=os.getenv("CODEX_RESEARCH_EFFORT", "high"),
        choices=["low", "medium", "high", "xhigh"],
    )
    args = parser.parse_args()

    for required in [
        REGISTRY_PATH,
        CURRENT_MATRIX,
        PRIOR_FINAL_AUDIT,
        SEMANTIC_CORRECTION,
        PLAN_PATH,
    ]:
        if not required.exists():
            raise RuntimeError(f"Required input not found: {required}")

    matrix = load_json(CURRENT_MATRIX)

    if matrix.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("Current verification matrix ID mismatch.")

    if matrix.get("paper_count") != 1:
        raise RuntimeError(
            f"{VERIFICATION_ID} must contain exactly one paper."
        )

    paper = target_registry_record()
    paper_id = str(paper.get("paper_id", ""))

    matrix_papers = matrix.get("papers", [])
    if not matrix_papers or matrix_papers[0].get("paper_id") != paper_id:
        raise RuntimeError(
            f"{VERIFICATION_ID} matrix paper does not match registry."
        )

    target_evidence = target_evidence_path(paper)

    evidence_text = read_text(target_evidence).lower()
    if EXPECTED_TITLE_FRAGMENT not in evidence_text:
        raise RuntimeError(
            "D1-V009 target evidence does not contain the expected "
            "Adhikary 1999 title fragment. Refusing to audit the wrong paper."
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    source_meta = [
        source_metadata(
            PRIOR_FINAL_AUDIT,
            "PRIOR_D1_V008_FINAL_AUDIT",
        ),
        source_metadata(
            SEMANTIC_CORRECTION,
            "PREDECLARED_TOLERANCE_SEMANTIC_GUARDRAIL",
        ),
        source_metadata(
            PLAN_PATH,
            "D1_V009_AUDIT_PROTOCOL",
        ),
        source_metadata(
            CURRENT_MATRIX,
            "CURRENT_D1_V009_MATRIX",
        ),
        source_metadata(
            target_evidence,
            "TARGET_VERIFIED_FULL_TEXT_EVIDENCE",
        ),
    ]

    bundle_hash_input = "\n".join(
        f"{item['path']}:{item['sha256']}"
        for item in source_meta
    ).encode("utf-8")

    bundle_sha256 = sha256_bytes(bundle_hash_input)

    run_id = timestamp_id()
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    schema_path = run_dir / "output_schema.json"
    manifest_path = run_dir / "source_manifest.json"
    prompt_path = run_dir / "prompt.txt"
    raw_path = run_dir / "raw_model_output.json"
    result_json_path = run_dir / "LATE_FOUND_ADJACENT_AUDIT.json"
    result_md_path = run_dir / "LATE_FOUND_ADJACENT_AUDIT.md"

    schema_path.write_text(
        json.dumps(SCHEMA, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    manifest_path.write_text(
        json.dumps(
            {
                "run_id": run_id,
                "created_at_utc": utc_now().isoformat(),
                "verification_id": VERIFICATION_ID,
                "target_paper_id": paper_id,
                "evidence_bundle_sha256": bundle_sha256,
                "sources": source_meta,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    prompt = build_prompt(
        target_evidence=target_evidence,
        source_meta=source_meta,
    )
    prompt_path.write_text(prompt, encoding="utf-8")

    print(f"[RUN] {run_id}")
    print(f"[VERIFICATION] {VERIFICATION_ID}")
    print(f"[TARGET PAPER] {paper_id}")
    print(f"[SOURCES] {len(source_meta)}")
    print(f"[BUNDLE SHA256] {bundle_sha256}")
    print(f"[PROMPT CHARS] {len(prompt):,}")
    print(f"[RUN DIR] {run_dir.relative_to(ROOT)}")

    if args.prepare_only:
        print("[PREPARE ONLY] Model call skipped.")
        return

    if not args.model:
        raise RuntimeError(
            "No Codex model configured. Set CODEX_RESEARCH_MODEL in .env "
            "or pass --model."
        )

    if CANONICAL_JSON.exists() and not args.force:
        raise RuntimeError(
            "Canonical D1-V009 audit already exists. Use --force only "
            "if you intentionally want to replace it."
        )

    run_codex(
        prompt=prompt,
        schema_path=schema_path,
        raw_output_path=raw_path,
        model=args.model,
        effort=args.effort,
    )

    raw_text = read_text(raw_path).strip()

    try:
        result = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Model output is not valid JSON.") from exc

    if not isinstance(result, dict):
        raise RuntimeError("Model output must be a JSON object.")

    validate_result(result)

    result["_provenance"] = {
        "run_id": run_id,
        "created_at_utc": utc_now().isoformat(),
        "verification_id": VERIFICATION_ID,
        "target_paper_id": paper_id,
        "evidence_bundle_sha256": bundle_sha256,
        "model": args.model,
        "effort": args.effort,
    }

    result_json_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    markdown = render_markdown(
        result=result,
        manifest=source_meta,
        bundle_sha256=bundle_sha256,
    )
    result_md_path.write_text(markdown, encoding="utf-8")

    shutil.copy2(result_json_path, CANONICAL_JSON)
    shutil.copy2(result_md_path, CANONICAL_MD)
    shutil.copy2(raw_path, CANONICAL_RAW)

    lock = result["lock_decision"]

    print(f"[STATUS] {result['status']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(
        f"[KILL CONDITION MET] "
        f"{result['kill_test']['kill_condition_met']}"
    )
    print(
        f"[FINAL NOVELTY LOCK SURVIVES] "
        f"{lock['final_novelty_lock_survives']}"
    )
    print(
        f"[REOPEN BROAD SEARCH] "
        f"{lock['reopen_broad_search']}"
    )
    print(
        f"[TARGETED FOLLOWUP REQUIRED] "
        f"{lock['targeted_followup_required']}"
    )
    print("[SAVED]", result_json_path.relative_to(ROOT))
    print("[SAVED]", result_md_path.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_JSON.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
