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
OUT_DIR = ROOT / "outputs" / "verification" / "D1-V006"
RUNS_DIR = OUT_DIR / "c03_adversarial_runs"

REGISTRY_PATH = ROOT / "data" / "paper_registry.json"
CURRENT_MATRIX = OUT_DIR / "verification_matrix.json"
PRIOR_C02 = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V005"
    / "C02_ADVERSARIAL_AUDIT.json"
)

CANONICAL_JSON = OUT_DIR / "C03_ADVERSARIAL_AUDIT.json"
CANONICAL_MD = OUT_DIR / "C03_ADVERSARIAL_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "C03_ADVERSARIAL_AUDIT_raw.json"

STATUS_ENUM = [
    "FALSIFIED",
    "SUBSTANTIALLY_NARROWED",
    "NO_KILL_BUT_HIGH_THREAT",
    "NO_TRANSFERABLE_KILL_FOUND",
]
THREAT_ENUM = ["low", "medium", "high", "fatal"]
EVIDENCE_ENUM = ["VERIFIED_FULL_TEXT", "INFERENCE"]
CRITERION_ENUM = [
    "none",
    "numerical_convergence",
    "physical_transition",
    "design_rule",
    "model_validity",
    "unclear",
]
TRANSFER_ENUM = ["direct", "partial", "weak", "not_demonstrated"]


SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "current_p1",
        "executive_summary",
        "paper_audits",
        "high_threat_criterion_audit",
        "kill_test",
        "strongest_threats",
        "surviving_gap",
        "c04_search_needed",
        "c04_search_rationale",
        "final_project_novelty_verdict_allowed",
        "recommended_next_action",
    ],
    "properties": {
        "status": {"type": "string", "enum": STATUS_ENUM},
        "confidence": {
            "type": "string",
            "enum": ["low", "medium", "high"],
        },
        "current_p1": {"type": "string"},
        "executive_summary": {"type": "string"},
        "paper_audits": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "paper_id",
                    "title",
                    "evidence_status",
                    "threat_to_p1",
                    "physical_analogue",
                    "interface_or_connection_model",
                    "reduced_or_equivalent_model",
                    "governing_parameters",
                    "normal_contact_pressure_role",
                    "friction_law_or_capacity",
                    "stick_slip_mechanism",
                    "contact_redistribution",
                    "reference_model",
                    "experimental_validation",
                    "quantitative_error_evidence",
                    "criterion_or_threshold",
                    "criterion_type",
                    "declared_tolerance",
                    "validity_domain",
                    "breakdown_boundary",
                    "transferability_to_vacuum_layer_jamming",
                    "what_it_proves",
                    "what_it_does_not_prove",
                ],
                "properties": {
                    "paper_id": {"type": "string"},
                    "title": {"type": "string"},
                    "evidence_status": {
                        "type": "string",
                        "enum": EVIDENCE_ENUM,
                    },
                    "threat_to_p1": {
                        "type": "string",
                        "enum": THREAT_ENUM,
                    },
                    "physical_analogue": {"type": "string"},
                    "interface_or_connection_model": {"type": "string"},
                    "reduced_or_equivalent_model": {"type": "string"},
                    "governing_parameters": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "normal_contact_pressure_role": {"type": "string"},
                    "friction_law_or_capacity": {"type": "string"},
                    "stick_slip_mechanism": {"type": "string"},
                    "contact_redistribution": {"type": "string"},
                    "reference_model": {"type": "string"},
                    "experimental_validation": {"type": "string"},
                    "quantitative_error_evidence": {"type": "string"},
                    "criterion_or_threshold": {"type": "string"},
                    "criterion_type": {
                        "type": "string",
                        "enum": CRITERION_ENUM,
                    },
                    "declared_tolerance": {"type": "string"},
                    "validity_domain": {"type": "string"},
                    "breakdown_boundary": {"type": "string"},
                    "transferability_to_vacuum_layer_jamming": {
                        "type": "string",
                        "enum": TRANSFER_ENUM,
                    },
                    "what_it_proves": {"type": "string"},
                    "what_it_does_not_prove": {"type": "string"},
                },
            },
        },
        "high_threat_criterion_audit": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "source",
                    "criterion",
                    "criterion_type",
                    "is_predeclared_tolerance_based",
                    "is_model_form_validity_boundary",
                    "is_only_numerical_or_design_criterion",
                    "transferability",
                    "assessment",
                ],
                "properties": {
                    "source": {"type": "string"},
                    "criterion": {"type": "string"},
                    "criterion_type": {
                        "type": "string",
                        "enum": CRITERION_ENUM,
                    },
                    "is_predeclared_tolerance_based": {"type": "boolean"},
                    "is_model_form_validity_boundary": {"type": "boolean"},
                    "is_only_numerical_or_design_criterion": {"type": "boolean"},
                    "transferability": {
                        "type": "string",
                        "enum": TRANSFER_ENUM,
                    },
                    "assessment": {"type": "string"},
                },
            },
        },
        "kill_test": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "named_reduced_or_equivalent_model",
                "interface_resolving_or_exact_reference",
                "governing_interaction_parameter",
                "quantitative_model_form_error",
                "finite_parameter_or_discreteness_sweep",
                "predeclared_acceptance_tolerance",
                "tolerance_defined_validity_domain",
                "validated_breakdown_boundary",
                "transferable_to_pressure_dependent_friction_without_new_mechanics",
                "kill_condition_met",
                "evidence_summary",
            ],
            "properties": {
                "named_reduced_or_equivalent_model": {"type": "boolean"},
                "interface_resolving_or_exact_reference": {"type": "boolean"},
                "governing_interaction_parameter": {"type": "boolean"},
                "quantitative_model_form_error": {"type": "boolean"},
                "finite_parameter_or_discreteness_sweep": {"type": "boolean"},
                "predeclared_acceptance_tolerance": {"type": "boolean"},
                "tolerance_defined_validity_domain": {"type": "boolean"},
                "validated_breakdown_boundary": {"type": "boolean"},
                "transferable_to_pressure_dependent_friction_without_new_mechanics": {
                    "type": "boolean"
                },
                "kill_condition_met": {"type": "boolean"},
                "evidence_summary": {"type": "string"},
            },
        },
        "strongest_threats": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "source",
                    "threat",
                    "why_it_matters",
                    "remaining_gap",
                ],
                "properties": {
                    "source": {"type": "string"},
                    "threat": {"type": "string", "enum": THREAT_ENUM},
                    "why_it_matters": {"type": "string"},
                    "remaining_gap": {"type": "string"},
                },
            },
        },
        "surviving_gap": {"type": "string"},
        "c04_search_needed": {"type": "boolean"},
        "c04_search_rationale": {"type": "string"},
        "final_project_novelty_verdict_allowed": {"type": "boolean"},
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_evidence() -> list[Path]:
    registry = load_json(REGISTRY_PATH)
    papers = registry.get("papers", []) if isinstance(registry, dict) else registry

    selected: list[dict[str, Any]] = []
    for paper in papers:
        if paper.get("source_type") != "verification":
            continue
        if paper.get("verification_id") != "D1-V006":
            continue
        if paper.get("screening_status") == "excluded":
            continue
        if paper.get("screening_status") != "included":
            raise RuntimeError(
                f"{paper.get('paper_id')}: unresolved screening_status="
                f"{paper.get('screening_status')!r}"
            )
        if paper.get("ingestion_status") != "complete":
            raise RuntimeError(
                f"{paper.get('paper_id')}: ingestion_status="
                f"{paper.get('ingestion_status')!r}"
            )
        if paper.get("evidence_status") != "present":
            raise RuntimeError(
                f"{paper.get('paper_id')}: evidence_status="
                f"{paper.get('evidence_status')!r}"
            )
        selected.append(paper)

    selected.sort(
        key=lambda x: (
            str(x.get("filename", "")).lower(),
            str(x.get("paper_id", "")),
        )
    )

    paths: list[Path] = []
    seen: set[Path] = set()
    for paper in selected:
        rel = paper.get("evidence_file")
        if not rel:
            raise RuntimeError(f"{paper.get('paper_id')}: evidence_file missing")
        path = ROOT / "data" / str(rel)
        if not path.exists():
            raise RuntimeError(f"Evidence file not found: {path}")
        if path in seen:
            continue
        seen.add(path)
        paths.append(path)

    if not paths:
        raise RuntimeError("No included D1-V006 evidence files found.")

    return paths


def source_metadata(path: Path, role: str) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256_file(path),
        "size_bytes": stat.st_size,
        "role": role,
    }


def build_prompt(
    evidence_paths: list[Path],
    source_meta: list[dict[str, Any]],
) -> str:
    blocks: list[str] = []
    for path in [PRIOR_C02, CURRENT_MATRIX, *evidence_paths]:
        rel = str(path.relative_to(ROOT))
        meta = next(x for x in source_meta if x["path"] == rel)
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
You are performing the D1-V006 / Track-C03 adversarial scientific audit
for an MSc research project on vacuum layer jamming and continuum-model
validity.

This is a FALSIFICATION task, not a literature-summary task.

Use ONLY the supplied source bundle for scientific claims. The D1-V006
evidence JSON files were extracted from locally held full texts. Do not
invent equations, thresholds, experiments, or transferability.

======================================================================
SURVIVING P1 AFTER C02
======================================================================

The current provisional premise is:

"For one specified reduced/continuum vacuum-layer-jamming beam model
under quasi-static planar bending, establish output-specific,
PREDECLARED acceptance tolerances and experimentally validated
validity/breakdown boundaries against an interface-resolving reference,
with vacuum pressure controlling normal contact, Coulomb friction
capacity, stick-slip evolution, and possible contact redistribution."

C01 and C02 already established that the following ARE NOT sufficient
novelty by themselves:

- continuum or equivalent representations;
- interfacial slip models;
- effective/equivalent EI;
- interaction parameters;
- transfer/interaction length concepts;
- finite layer or connector sweeps;
- exact-versus-approximate comparison;
- numerical convergence studies;
- criteria for neglecting partial interaction;
- generic model-versus-experiment agreement.

The residual scientific question is much narrower.

======================================================================
C03 QUESTION
======================================================================

Does shear-lag, imperfect-interface, frictional-contact, multilayer,
flexible-pipe, joint-contact, or related adjacent mechanics ALREADY
provide a framework transferable to vacuum layer jamming that connects:

normal/contact pressure or preload
    ->
friction capacity
    ->
stick / partial slip / gross slip
    ->
reduced or continuum representation
    ->
interface-resolving / discrete / full-layer reference
    ->
quantitative MODEL-FORM prediction error
    ->
PREDECLARED acceptance tolerance
    ->
validity domain / breakdown boundary?

If such a framework already exists and transfers without materially new
mechanics, P1 may be falsified.

======================================================================
MANDATORY DISTINCTIONS
======================================================================

Do NOT collapse these concepts:

critical physical length scale
!=
reduced-model validity boundary

stick-to-slip transition
!=
continuum-model breakdown

friction coefficient versus pressure relation
!=
validated model-form applicability criterion

normal pressure effect
!=
vacuum-pressure layer-jamming validity framework

mesh convergence tolerance
!=
physical model-form acceptance tolerance

solver/contact convergence
!=
continuum validity

experimentally fitted parameters
!=
independent model validation

agreement with FEM
!=
validity map unless model-form error is quantified over parameter space

reported percentage error
!=
PREDECLARED acceptance threshold

effective spring/interface model
!=
validated breakdown boundary

dynamic hysteresis model
!=
quasi-static planar-bending validity without demonstrated transferability

same mathematical ingredients
!=
same scientific problem

different application domain alone
!=
novelty

analogy
!=
transferability

======================================================================
HIGH-THREAT FAMILIES
======================================================================

Audit especially carefully:

1. full-layered flexible-pipe models with initial contact pressure;
2. reduced helix/contact models benchmarked against full-layer models;
3. multilayer continuum models with explicit Coulomb contact;
4. models coupling tangential friction to contact-pressure distribution;
5. equivalent-thin-layer models for frictional interfaces;
6. preload-dependent stick-slip joint models;
7. imperfect-interface effective spring models with experimental
   applicability validation;
8. critical-length friction/contact formulations;
9. layered-beam reduced models allowing interfacial sliding.

For each source determine whether it supplies:

- normal/contact pressure dependence;
- Coulomb or related friction law;
- stick/partial-slip/gross-slip transition;
- contact redistribution;
- a reduced/continuum model;
- an explicit/discrete/interface-resolving reference;
- independent experiments;
- quantitative model-form error;
- a finite parameter sweep;
- a predeclared tolerance;
- a tolerance-defined validity domain;
- an experimentally supported breakdown boundary.

======================================================================
PAPER-BY-PAPER AUDIT
======================================================================

Audit EVERY included D1-V006 paper exactly once.

For each paper identify:

- physical analogue;
- interface/contact representation;
- reduced/equivalent representation;
- governing parameters;
- role of normal/contact pressure;
- friction law or friction capacity;
- stick/partial-slip/gross-slip mechanism;
- contact redistribution, if any;
- reference model;
- experiment, if present;
- quantitative MODEL-FORM error evidence;
- criterion or threshold;
- criterion type;
- declared tolerance;
- validity domain;
- breakdown boundary;
- transferability to vacuum layer jamming;
- what the paper actually proves;
- what it does NOT prove;
- threat level to P1.

If the evidence does not support an item, say so explicitly.
Do not infer unsupported transferability.

======================================================================
C03 KILL CONDITION
======================================================================

kill_condition_met may be true ONLY if the supplied C03 corpus
collectively establishes ALL of the following in a framework
transferable to vacuum layer jamming without materially new mechanics:

1. a named reduced/equivalent/continuum model;
2. an explicit, discrete, full-layer, exact, or interface-resolving
   reference;
3. a governing interaction/contact/friction parameter;
4. quantitative MODEL-FORM error between reduced and reference models;
5. a finite parameter/discreteness/pressure sweep;
6. a PREDECLARED model-form acceptance tolerance;
7. a tolerance-defined validity domain;
8. a validated breakdown boundary;
9. explicit pressure/preload-dependent frictional coupling transferable
   to vacuum-driven normal contact and layer slip without adding a new
   constitutive/contact framework.

If ANY component is absent, kill_condition_met MUST be false.

A physical stick-slip threshold is NOT item 8 unless it is explicitly
linked to failure of the reduced model under item 6.

A numerical convergence threshold is NOT item 6.

======================================================================
STATUS RULES
======================================================================

FALSIFIED:
The supplied C03 evidence closes the remaining P1 gap through the
complete transferable kill condition.

SUBSTANTIALLY_NARROWED:
C03 supplies one or more previously missing core elements and forces
P1 to become narrower, but the complete kill condition is absent.

NO_KILL_BUT_HIGH_THREAT:
Strong pressure/friction/contact analogues exist and threaten P1, but
one or more scientifically nontrivial transfer or validity components
remain unresolved.

NO_TRANSFERABLE_KILL_FOUND:
No supplied C03 framework satisfies enough of the transferable chain to
invalidate the surviving P1.

IMPORTANT:

One previously identified high-threat paper is now available in the
D1-V006 verified full-text evidence bundle and MUST be audited like the
other included papers:

- DOI 10.1002/eqe.4128 — A novel friction model for steel-polymer
  interfaces in sliding seismic isolation bearings.

One previously identified high-threat paper is still unavailable:

- DOI 10.1061/JSENDH.STENG-13096

Therefore final_project_novelty_verdict_allowed MUST remain false in
this run, even if P1 survives.

Set c04_search_needed=true ONLY if the supplied evidence reveals a
specific unresolved literature family or mechanism that could still
materially falsify P1.

Do NOT request another broad literature search merely because novelty
can never be absolutely proven.

======================================================================
SOURCE MANIFEST
======================================================================

{json.dumps(source_meta, ensure_ascii=False, indent=2)}

======================================================================
SOURCE CONTENT
======================================================================

{bundle}

======================================================================
OUTPUT
======================================================================

Return ONLY one JSON object conforming exactly to the supplied schema.
Do not add Markdown fences or commentary outside the JSON.
""".strip()


def validate_result(result: dict[str, Any], expected_papers: int) -> None:
    missing = set(SCHEMA["required"]) - set(result)
    if missing:
        raise RuntimeError(
            "Model output missing required keys: " + ", ".join(sorted(missing))
        )

    if result["status"] not in STATUS_ENUM:
        raise RuntimeError(f"Invalid status: {result['status']}")

    if result["final_project_novelty_verdict_allowed"] is not False:
        raise RuntimeError(
            "Scientific guardrail violation: C03 cannot authorize a final "
            "project novelty verdict."
        )

    audits = result["paper_audits"]
    if len(audits) != expected_papers:
        raise RuntimeError(
            f"Expected {expected_papers} paper audits, got {len(audits)}."
        )

    ids = [x.get("paper_id") for x in audits]
    if len(ids) != len(set(ids)):
        raise RuntimeError("paper_audits contains duplicate paper_id values.")

    kill = result["kill_test"]
    required = [
        kill["named_reduced_or_equivalent_model"],
        kill["interface_resolving_or_exact_reference"],
        kill["governing_interaction_parameter"],
        kill["quantitative_model_form_error"],
        kill["finite_parameter_or_discreteness_sweep"],
        kill["predeclared_acceptance_tolerance"],
        kill["tolerance_defined_validity_domain"],
        kill["validated_breakdown_boundary"],
        kill["transferable_to_pressure_dependent_friction_without_new_mechanics"],
    ]

    if kill["kill_condition_met"] and not all(required):
        raise RuntimeError(
            "Scientific guardrail violation: kill_condition_met=true but "
            "one or more mandatory kill components are false."
        )

    if result["status"] == "FALSIFIED" and not kill["kill_condition_met"]:
        raise RuntimeError(
            "Scientific guardrail violation: status=FALSIFIED without a "
            "complete kill condition."
        )

    if result["status"] != "FALSIFIED" and kill["kill_condition_met"]:
        raise RuntimeError(
            "Scientific guardrail violation: complete kill condition but "
            "status is not FALSIFIED."
        )


def render_markdown(
    result: dict[str, Any],
    manifest: list[dict[str, Any]],
    bundle_sha256: str,
) -> str:
    lines: list[str] = [
        "# D1-V006 C03 Adversarial Audit",
        "",
        f"- **Status:** {result['status']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Evidence bundle SHA256:** `{bundle_sha256}`",
        f"- **Final project novelty verdict allowed:** "
        f"{result['final_project_novelty_verdict_allowed']}",
        "",
        "## Current P1",
        "",
        result["current_p1"],
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## Kill test",
        "",
    ]

    for key, value in result["kill_test"].items():
        if key == "evidence_summary":
            continue
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            result["kill_test"]["evidence_summary"],
            "",
            "## High-threat criterion audit",
            "",
        ]
    )

    for item in result["high_threat_criterion_audit"]:
        lines.extend(
            [
                f"### {item['source']}",
                "",
                f"- Criterion: {item['criterion']}",
                f"- Type: **{item['criterion_type']}**",
                f"- Predeclared tolerance based: {item['is_predeclared_tolerance_based']}",
                f"- Model-form validity boundary: {item['is_model_form_validity_boundary']}",
                f"- Only numerical/design criterion: {item['is_only_numerical_or_design_criterion']}",
                f"- Transferability: {item['transferability']}",
                f"- Assessment: {item['assessment']}",
                "",
            ]
        )

    lines.extend(["## Strongest threats", ""])
    for item in result["strongest_threats"]:
        lines.extend(
            [
                f"### {item['source']}",
                "",
                f"- Threat: **{item['threat']}**",
                f"- Why it matters: {item['why_it_matters']}",
                f"- Remaining gap: {item['remaining_gap']}",
                "",
            ]
        )

    lines.extend(["## Paper-by-paper audit", ""])
    for item in result["paper_audits"]:
        lines.extend(
            [
                f"### {item['paper_id']} — {item['title']}",
                "",
                f"- Evidence: {item['evidence_status']}",
                f"- Threat: **{item['threat_to_p1']}**",
                f"- Physical analogue: {item['physical_analogue']}",
                f"- Interface/connection model: {item['interface_or_connection_model']}",
                f"- Reduced/equivalent model: {item['reduced_or_equivalent_model']}",
                f"- Normal/contact pressure role: {item['normal_contact_pressure_role']}",
                f"- Friction law/capacity: {item['friction_law_or_capacity']}",
                f"- Stick-slip mechanism: {item['stick_slip_mechanism']}",
                f"- Contact redistribution: {item['contact_redistribution']}",
                f"- Reference model: {item['reference_model']}",
                f"- Experimental validation: {item['experimental_validation']}",
                f"- Quantitative error: {item['quantitative_error_evidence']}",
                f"- Criterion: {item['criterion_or_threshold']}",
                f"- Criterion type: {item['criterion_type']}",
                f"- Declared tolerance: {item['declared_tolerance']}",
                f"- Validity domain: {item['validity_domain']}",
                f"- Breakdown boundary: {item['breakdown_boundary']}",
                f"- Transferability: {item['transferability_to_vacuum_layer_jamming']}",
                f"- Proves: {item['what_it_proves']}",
                f"- Does not prove: {item['what_it_does_not_prove']}",
                "",
            ]
        )
        if item["governing_parameters"]:
            lines.append("**Governing parameters:**")
            for parameter in item["governing_parameters"]:
                lines.append(f"- {parameter}")
            lines.append("")

    lines.extend(
        [
            "## Surviving gap",
            "",
            result["surviving_gap"],
            "",
            "## C04 decision",
            "",
            f"- **C04 search needed:** {result['c04_search_needed']}",
            f"- {result['c04_search_rationale']}",
            "",
            "## Recommended next action",
            "",
            result["recommended_next_action"],
            "",
            "## Evidence provenance",
            "",
        ]
    )

    for item in manifest:
        lines.append(
            f"- `{item['path']}` — {item['role']} — `{item['sha256']}`"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="D1-V006 Track-C03 adversarial audit."
    )
    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help="Prepare manifest, prompt, and schema without calling Codex.",
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

    for path in [REGISTRY_PATH, CURRENT_MATRIX, PRIOR_C02]:
        if not path.exists():
            raise RuntimeError(f"Required input not found: {path}")

    evidence_paths = collect_evidence()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    source_meta = [
        source_metadata(PRIOR_C02, "PRIOR_C02_ADVERSARIAL_RESULT"),
        source_metadata(CURRENT_MATRIX, "CURRENT_C03_MATRIX"),
    ] + [
        source_metadata(path, "CURRENT_C03_VERIFIED_FULL_TEXT_EVIDENCE")
        for path in evidence_paths
    ]

    bundle_hash_input = "\n".join(
        f"{item['path']}:{item['sha256']}" for item in source_meta
    ).encode("utf-8")
    bundle_sha256 = sha256_bytes(bundle_hash_input)

    run_id = timestamp_id()
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    schema_path = run_dir / "output_schema.json"
    manifest_path = run_dir / "source_manifest.json"
    prompt_path = run_dir / "prompt.txt"
    raw_path = run_dir / "raw_model_output.json"
    result_json_path = run_dir / "C03_ADVERSARIAL_AUDIT.json"
    result_md_path = run_dir / "C03_ADVERSARIAL_AUDIT.md"

    schema_path.write_text(
        json.dumps(SCHEMA, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest_path.write_text(
        json.dumps(
            {
                "run_id": run_id,
                "created_at_utc": utc_now().isoformat(),
                "evidence_bundle_sha256": bundle_sha256,
                "included_evidence_files": len(evidence_paths),
                "sources": source_meta,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    prompt = build_prompt(evidence_paths, source_meta)
    prompt_path.write_text(prompt, encoding="utf-8")

    print(f"[RUN] {run_id}")
    print(f"[D1-V006 VERIFIED PAPERS] {len(evidence_paths)}")
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
            "Canonical C03 audit already exists. Use --force only if you "
            "intentionally want to replace it."
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

    validate_result(result, expected_papers=len(evidence_paths))

    result["_provenance"] = {
        "run_id": run_id,
        "created_at_utc": utc_now().isoformat(),
        "evidence_bundle_sha256": bundle_sha256,
        "model": args.model,
        "effort": args.effort,
        "included_evidence_files": len(evidence_paths),
    }

    result_json_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    result_md_path.write_text(
        render_markdown(result, source_meta, bundle_sha256),
        encoding="utf-8",
    )

    shutil.copy2(result_json_path, CANONICAL_JSON)
    shutil.copy2(result_md_path, CANONICAL_MD)
    shutil.copy2(raw_path, CANONICAL_RAW)

    print(f"[STATUS] {result['status']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(f"[KILL CONDITION MET] {result['kill_test']['kill_condition_met']}")
    print(f"[C04 SEARCH NEEDED] {result['c04_search_needed']}")
    print("[SAVED]", result_json_path.relative_to(ROOT))
    print("[SAVED]", result_md_path.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_JSON.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
