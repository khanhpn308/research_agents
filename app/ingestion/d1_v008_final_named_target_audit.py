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

VERIFICATION_ID = "D1-V008"
TARGET_DOI = "10.1061/JSENDH.STENG-13096"
TARGET_PAPER_ID = "53d328abaa"

OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
RUNS_DIR = OUT_DIR / "final_named_target_runs"

REGISTRY_PATH = ROOT / "data" / "paper_registry.json"
CURRENT_MATRIX = OUT_DIR / "verification_matrix.json"

PRIOR_C04 = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V007"
    / "C04_ADVERSARIAL_AUDIT.json"
)

SEMANTIC_CORRECTION = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V007"
    / "C04_SEMANTIC_CORRECTION.md"
)

CANONICAL_JSON = OUT_DIR / "FINAL_NAMED_TARGET_AUDIT.json"
CANONICAL_MD = OUT_DIR / "FINAL_NAMED_TARGET_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "FINAL_NAMED_TARGET_AUDIT_raw.json"

STATUS_ENUM = [
    "FALSIFIED",
    "SURVIVES_FINAL_TARGET",
    "SURVIVES_REVISED_SCOPE",
    "INCONCLUSIVE",
]

THREAT_ENUM = ["low", "medium", "high", "fatal"]
BOUNDARY_ENUM = [
    "not_present",
    "physical_assumption_limit",
    "post_hoc_applicability_limit",
    "tolerance_defined_model_form_validity_boundary",
    "other",
]

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "current_p1",
        "target_identity",
        "executive_summary",
        "target_audit",
        "observed_error_interpretation",
        "lh_boundary_analysis",
        "kill_test",
        "new_named_threats",
        "stop_search_decision",
        "final_surviving_contribution",
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
                "doi",
                "paper_id",
                "title",
                "verified_full_text",
            ],
            "properties": {
                "doi": {"type": "string"},
                "paper_id": {"type": "string"},
                "title": {"type": "string"},
                "verified_full_text": {"type": "boolean"},
            },
        },
        "executive_summary": {"type": "string"},
        "target_audit": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "explicit_nonlinear_interfacial_slip",
                "pressure_or_preload_controls_contact_state",
                "named_reduced_or_continuum_model",
                "interface_resolved_or_discrete_reference",
                "quantitative_model_form_error",
                "predeclared_acceptance_tolerance",
                "predeclared_tolerance_evidence",
                "tolerance_defined_breakdown_boundary",
                "experiments_intentionally_cross_boundary",
                "vacuum_specific_contact_mechanics",
                "transferable_to_vacuum_layer_jamming_without_new_mechanics",
                "threat_to_p1",
                "what_it_proves",
                "what_it_does_not_prove",
            ],
            "properties": {
                "explicit_nonlinear_interfacial_slip": {"type": "boolean"},
                "pressure_or_preload_controls_contact_state": {"type": "boolean"},
                "named_reduced_or_continuum_model": {"type": "boolean"},
                "interface_resolved_or_discrete_reference": {"type": "boolean"},
                "quantitative_model_form_error": {"type": "boolean"},
                "predeclared_acceptance_tolerance": {"type": "boolean"},
                "predeclared_tolerance_evidence": {"type": "string"},
                "tolerance_defined_breakdown_boundary": {"type": "boolean"},
                "experiments_intentionally_cross_boundary": {"type": "boolean"},
                "vacuum_specific_contact_mechanics": {"type": "boolean"},
                "transferable_to_vacuum_layer_jamming_without_new_mechanics": {
                    "type": "boolean"
                },
                "threat_to_p1": {
                    "type": "string",
                    "enum": THREAT_ENUM,
                },
                "what_it_proves": {"type": "string"},
                "what_it_does_not_prove": {"type": "string"},
            },
        },
        "observed_error_interpretation": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "analytical_deflection_3_percent",
                "fe_deflection_5_percent",
                "bending_strain_8_percent",
                "slip_difference_0_02_mm",
                "lh5_deflection_effect_20_percent",
                "are_any_predeclared_acceptance_tolerances",
                "assessment",
            ],
            "properties": {
                "analytical_deflection_3_percent": {"type": "string"},
                "fe_deflection_5_percent": {"type": "string"},
                "bending_strain_8_percent": {"type": "string"},
                "slip_difference_0_02_mm": {"type": "string"},
                "lh5_deflection_effect_20_percent": {"type": "string"},
                "are_any_predeclared_acceptance_tolerances": {
                    "type": "boolean"
                },
                "assessment": {"type": "string"},
            },
        },
        "lh_boundary_analysis": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "lh_ge_10_statement_present",
                "boundary_type",
                "source_basis",
                "derived_from_predeclared_model_form_tolerance",
                "validated_by_experiments_on_both_sides",
                "relevance_to_p1",
            ],
            "properties": {
                "lh_ge_10_statement_present": {"type": "boolean"},
                "boundary_type": {
                    "type": "string",
                    "enum": BOUNDARY_ENUM,
                },
                "source_basis": {"type": "string"},
                "derived_from_predeclared_model_form_tolerance": {
                    "type": "boolean"
                },
                "validated_by_experiments_on_both_sides": {
                    "type": "boolean"
                },
                "relevance_to_p1": {"type": "string"},
            },
        },
        "kill_test": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "pressure_or_preload_controls_contact",
                "friction_or_slip_is_explicit",
                "named_reduced_or_continuum_model",
                "interface_resolved_or_discrete_reference",
                "quantitative_model_form_error",
                "predeclared_acceptance_tolerance",
                "tolerance_defined_breakdown_boundary",
                "experiment_tests_both_sides_of_boundary",
                "transferable_to_vacuum_layer_jamming_without_new_mechanics",
                "kill_condition_met",
                "evidence_summary",
            ],
            "properties": {
                "pressure_or_preload_controls_contact": {"type": "boolean"},
                "friction_or_slip_is_explicit": {"type": "boolean"},
                "named_reduced_or_continuum_model": {"type": "boolean"},
                "interface_resolved_or_discrete_reference": {"type": "boolean"},
                "quantitative_model_form_error": {"type": "boolean"},
                "predeclared_acceptance_tolerance": {"type": "boolean"},
                "tolerance_defined_breakdown_boundary": {"type": "boolean"},
                "experiment_tests_both_sides_of_boundary": {"type": "boolean"},
                "transferable_to_vacuum_layer_jamming_without_new_mechanics": {
                    "type": "boolean"
                },
                "kill_condition_met": {"type": "boolean"},
                "evidence_summary": {"type": "string"},
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
                    "explicitly_named_in_supplied_evidence": {
                        "type": "boolean"
                    },
                    "requires_targeted_full_text_audit": {
                        "type": "boolean"
                    },
                },
            },
        },
        "stop_search_decision": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "prior_forward_citation_branch_closed",
                "target_doi_audit_complete",
                "additional_high_threat_named_target_remaining",
                "broad_search_should_stop",
                "final_novelty_lock_allowed",
                "decision_rationale",
            ],
            "properties": {
                "prior_forward_citation_branch_closed": {"type": "boolean"},
                "target_doi_audit_complete": {"type": "boolean"},
                "additional_high_threat_named_target_remaining": {
                    "type": "boolean"
                },
                "broad_search_should_stop": {"type": "boolean"},
                "final_novelty_lock_allowed": {"type": "boolean"},
                "decision_rationale": {"type": "string"},
            },
        },
        "final_surviving_contribution": {"type": "string"},
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def registry_papers() -> list[dict[str, Any]]:
    data = load_json(REGISTRY_PATH)
    return data.get("papers", []) if isinstance(data, dict) else data


def target_evidence_path() -> Path:
    matches = [
        p
        for p in registry_papers()
        if p.get("paper_id") == TARGET_PAPER_ID
        and p.get("verification_id") == VERIFICATION_ID
        and p.get("source_type") == "verification"
    ]

    if len(matches) != 1:
        raise RuntimeError(
            f"Expected exactly one {VERIFICATION_ID} registry record for "
            f"{TARGET_PAPER_ID}; found {len(matches)}."
        )

    paper = matches[0]

    if paper.get("screening_status") != "included":
        raise RuntimeError(
            f"{TARGET_PAPER_ID}: screening_status="
            f"{paper.get('screening_status')!r}"
        )

    if paper.get("ingestion_status") != "complete":
        raise RuntimeError(
            f"{TARGET_PAPER_ID}: ingestion_status="
            f"{paper.get('ingestion_status')!r}"
        )

    if paper.get("evidence_status") != "present":
        raise RuntimeError(
            f"{TARGET_PAPER_ID}: evidence_status="
            f"{paper.get('evidence_status')!r}"
        )

    rel = paper.get("evidence_file")
    if not rel:
        raise RuntimeError(f"{TARGET_PAPER_ID}: evidence_file missing.")

    path = ROOT / "data" / str(rel)
    if not path.exists():
        raise RuntimeError(f"Target evidence file not found: {path}")

    return path


def source_metadata(path: Path, role: str) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256_file(path),
        "size_bytes": stat.st_size,
        "role": role,
    }


def build_prompt(
    target_evidence: Path,
    source_meta: list[dict[str, Any]],
) -> str:
    ordered_sources = [
        PRIOR_C04,
        SEMANTIC_CORRECTION,
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
You are performing D1-V008, the FINAL NAMED-TARGET adversarial audit
for a proposed MSc research direction on validity limits of a specified
reduced/continuum vacuum-layer-jamming beam model.

This is a FALSIFICATION task, not a paper-summary task.

Use ONLY the supplied source bundle for scientific claims. The D1-V008
paper has locally held verified full text represented by its evidence
JSON. Do not invent equations, thresholds, experiments, transferability,
citation relationships, or novelty.

======================================================================
CURRENT P1
======================================================================

The surviving premise is intentionally narrow:

"For ONE specified reduced/continuum vacuum-layer-jamming beam model
under quasi-static planar bending, define output-specific PREDECLARED
model-form acceptance tolerances and determine experimentally validated
validity/breakdown boundaries against an interface-resolving/full-layer
reference, while explicitly accounting for vacuum-pressure-controlled
normal contact, friction/slip evolution, and where necessary pressure
redistribution or layer separation."

The prior C04 audit closed the currently identified forward-citation
branch of focal paper ca46dc062d without satisfying the kill condition.
It left exactly one specifically named high-threat target unaudited:

DOI {TARGET_DOI}

D1-V008 contains that target.

======================================================================
TARGET IDENTITY
======================================================================

Expected paper_id: {TARGET_PAPER_ID}
Expected DOI: {TARGET_DOI}

The target is:
"Analytical Solution for Bending Deformation of Steel-Concrete
Composite Beams Considering Nonlinear Interfacial Slip" (2024).

Audit this paper as a high-threat adjacent mechanics paper. Do not
downgrade it merely because it is a civil-engineering application.
Equally, do not treat mathematical similarity as direct mechanical
transferability to vacuum layer jamming.

======================================================================
STRICT SEMANTIC RULE: PREDECLARED
======================================================================

PREDECLARED means the model-form acceptance tolerance was fixed a priori
BEFORE the relevant validation/error results were inspected.

An explicit, adopted, observed, recommended, or post-hoc percentage is
NOT sufficient.

Specifically:
- an observed 3% analytical-vs-experimental deflection difference is
  not automatically a predeclared tolerance;
- an observed maximum 5% FE-vs-experimental difference is not
  automatically a predeclared tolerance;
- an observed <8% bending-strain discrepancy is not automatically a
  predeclared tolerance;
- an observed <=0.02 mm slip difference is not automatically a
  predeclared tolerance;
- a 20% shear-deformation effect at L/H=5 is not automatically a
  predeclared tolerance;
- a statement that the analytical solution is suitable for L/H>=10 is
  not automatically a tolerance-defined MODEL-FORM validity boundary.

Only set predeclared_acceptance_tolerance=true if the supplied evidence
explicitly establishes that a criterion was fixed before validation or
error inspection. If that temporal ordering is absent, set it false and
state "not established" in the evidence field.

======================================================================
MODEL-FORM ERROR RULE
======================================================================

Distinguish carefully among:

A. experiment-vs-model disagreement;
B. FE-vs-experiment disagreement;
C. analytical-model-vs-FE disagreement caused by a known omitted
   mechanism such as shear deformation;
D. reduced/continuum-vs-interface-resolved or full-layer MODEL-FORM
   discrepancy.

P1 specifically requires a validity/breakdown map for a chosen reduced
model against an interface-resolving/full-layer reference.

Do not upgrade A, B, or generic C into D unless the supplied evidence
supports that interpretation.

======================================================================
L/H >= 10 RULE
======================================================================

The target evidence reports that shear-deformation influence increases
as L/H decreases, reaches about 20% in deflection at L/H=5, and states
that the analytical solution is suitable for relatively slender beams
with L/H>=10.

Audit this result carefully.

You must determine whether L/H>=10 is:

- a physical/theory-assumption applicability limit;
- a post-hoc applicability recommendation;
- or a tolerance-defined model-form validity boundary.

To count as the P1 boundary, it must be tied to a PREDECLARED model-form
acceptance tolerance and then experimentally tested on both accepted and
rejected sides. Similarity alone is insufficient.

======================================================================
VACUUM-LAYER-JAMMING TRANSFER RULE
======================================================================

Audit whether the target actually contains mechanics transferable to
vacuum layer jamming WITHOUT a materially new mechanics contribution.

The target evidence must be checked for:

- vacuum pressure controlling interlayer normal contact;
- distributed normal-contact-pressure field;
- Coulomb/frictional stick/partial-slip/gross-slip evolution;
- pressure redistribution under bending;
- local separation/lift-off;
- many-layer contact rather than two-component steel-concrete action;
- an interface-resolving/full-layer reference appropriate to jamming.

If the paper neglects interface friction, uses headed-stud connector
load-slip behavior, smears discrete stud action into a fictitious
interlayer, or otherwise lacks vacuum/contact-pressure mechanics, do not
claim direct transferability.

======================================================================
FINAL KILL CONDITION
======================================================================

kill_condition_met may be TRUE only if the supplied evidence,
individually or together with the already-audited prior C04 evidence,
establishes ALL of the following in a framework transferable to vacuum
layer jamming without a materially new mechanics contribution:

1. pressure/preload controls the relevant contact state;
2. friction/slip is explicit;
3. a named reduced/continuum model exists;
4. an interface-resolved/discrete/full-layer reference exists;
5. quantitative MODEL-FORM error is evaluated over the relevant space;
6. a PREDECLARED acceptance tolerance is used;
7. that tolerance defines a validity/breakdown boundary;
8. experiments intentionally sample BOTH sides of the boundary;
9. transfer to vacuum layer jamming requires no materially new
   vacuum-to-pressure, pressure-redistribution, separation, or
   friction/contact mechanics.

If even ONE item is not established, kill_condition_met MUST be false.

======================================================================
STOP-SEARCH / FINAL-LOCK RULE
======================================================================

This round exists to decide whether the literature-falsification search
can stop.

The prior C04 output is authoritative for the fact that the current
focal forward-citation branch was closed at that search date.

Set target_doi_audit_complete=true only if the D1-V008 verified-full-text
evidence is the expected DOI {TARGET_DOI}.

Broad exploratory searching should STOP if:
- the prior forward-citation branch is closed;
- this target DOI is now audited from verified full text;
- kill_condition_met is false; and
- the supplied target does not explicitly identify another SPECIFIC
  high-threat paper/source that appears capable of satisfying the
  missing P1 kill-chain elements.

Do NOT reopen broad searching merely because the target has references.

A new named threat may keep final lock open only if it is specifically
identified in the supplied evidence and there is a concrete reason it
could satisfy missing kill-chain links. Generic "more literature may
exist" is not enough.

final_novelty_lock_allowed may be true only when:
- target_doi_audit_complete=true;
- prior_forward_citation_branch_closed=true;
- additional_high_threat_named_target_remaining=false;
- kill_condition_met=false.

Final novelty lock does NOT mean "no paper anywhere can ever overlap."
It means the defined adversarial search protocol has reached its
documented stop condition and the surviving contribution may now be
frozen provisionally for thesis execution.

======================================================================
OUTPUT DISCIPLINE
======================================================================

Return ONLY one JSON object conforming exactly to the supplied schema.

Do not add Markdown fences.
Do not add commentary outside the JSON.

======================================================================
SOURCE BUNDLE
======================================================================

{bundle}
"""


def validate_result(result: dict[str, Any]) -> None:
    ident = result.get("target_identity", {})

    if ident.get("doi", "").lower() != TARGET_DOI.lower():
        raise RuntimeError(
            "target_identity.doi does not match expected target DOI."
        )

    if ident.get("paper_id") != TARGET_PAPER_ID:
        raise RuntimeError(
            "target_identity.paper_id does not match expected paper_id."
        )

    if ident.get("verified_full_text") is not True:
        raise RuntimeError(
            "Target must be audited as verified full text in D1-V008."
        )

    audit = result.get("target_audit", {})
    kill = result.get("kill_test", {})

    consistency_pairs = [
        (
            "predeclared_acceptance_tolerance",
            audit.get("predeclared_acceptance_tolerance"),
            kill.get("predeclared_acceptance_tolerance"),
        ),
        (
            "tolerance_defined_breakdown_boundary",
            audit.get("tolerance_defined_breakdown_boundary"),
            kill.get("tolerance_defined_breakdown_boundary"),
        ),
        (
            "experiments_intentionally_cross_boundary",
            audit.get("experiments_intentionally_cross_boundary"),
            kill.get("experiment_tests_both_sides_of_boundary"),
        ),
        (
            "transferable_to_vacuum_layer_jamming_without_new_mechanics",
            audit.get(
                "transferable_to_vacuum_layer_jamming_without_new_mechanics"
            ),
            kill.get(
                "transferable_to_vacuum_layer_jamming_without_new_mechanics"
            ),
        ),
    ]

    mismatches = [
        name
        for name, left, right in consistency_pairs
        if left is not right
    ]

    if mismatches:
        raise RuntimeError(
            "Target-audit/kill-test inconsistency: "
            + ", ".join(mismatches)
        )

    required_kill_fields = [
        "pressure_or_preload_controls_contact",
        "friction_or_slip_is_explicit",
        "named_reduced_or_continuum_model",
        "interface_resolved_or_discrete_reference",
        "quantitative_model_form_error",
        "predeclared_acceptance_tolerance",
        "tolerance_defined_breakdown_boundary",
        "experiment_tests_both_sides_of_boundary",
        "transferable_to_vacuum_layer_jamming_without_new_mechanics",
    ]

    if kill.get("kill_condition_met"):
        missing = [
            key
            for key in required_kill_fields
            if kill.get(key) is not True
        ]
        if missing:
            raise RuntimeError(
                "kill_condition_met=True but required fields are false: "
                + ", ".join(missing)
            )

    stop = result.get("stop_search_decision", {})

    if stop.get("target_doi_audit_complete") is not True:
        raise RuntimeError(
            "D1-V008 contains the verified target DOI; "
            "target_doi_audit_complete must be true."
        )

    if stop.get("final_novelty_lock_allowed"):
        if stop.get("prior_forward_citation_branch_closed") is not True:
            raise RuntimeError(
                "Final lock requires prior forward-citation closure."
            )
        if stop.get("additional_high_threat_named_target_remaining"):
            raise RuntimeError(
                "Final lock cannot coexist with a named high-threat target."
            )
        if kill.get("kill_condition_met"):
            raise RuntimeError(
                "Final lock cannot be allowed when P1 is falsified."
            )

    if (
        result.get("status") == "FALSIFIED"
        and kill.get("kill_condition_met") is not True
    ):
        raise RuntimeError(
            "status=FALSIFIED requires kill_condition_met=true."
        )


def render_markdown(
    result: dict[str, Any],
    manifest: list[dict[str, Any]],
    bundle_sha256: str,
) -> str:
    ident = result["target_identity"]
    audit = result["target_audit"]
    lh = result["lh_boundary_analysis"]
    stop = result["stop_search_decision"]

    lines = [
        "# D1-V008 Final Named-Target Adversarial Audit",
        "",
        f"- **Status:** {result['status']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Bundle SHA256:** {bundle_sha256}",
        f"- **Kill condition met:** "
        f"{result['kill_test']['kill_condition_met']}",
        f"- **Final novelty lock allowed:** "
        f"{stop['final_novelty_lock_allowed']}",
        "",
        "## Current P1",
        "",
        result["current_p1"],
        "",
        "## Target identity",
        "",
        f"- DOI: {ident['doi']}",
        f"- paper_id: {ident['paper_id']}",
        f"- Title: {ident['title']}",
        f"- Verified full text: {ident['verified_full_text']}",
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## Target audit",
        "",
    ]

    for key, value in audit.items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            "## Observed-error interpretation",
            "",
        ]
    )

    for key, value in result["observed_error_interpretation"].items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            "## L/H boundary analysis",
            "",
        ]
    )

    for key, value in lh.items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            "## Kill test",
            "",
        ]
    )

    for key, value in result["kill_test"].items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
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
                    f"- Explicitly named: "
                    f"{item['explicitly_named_in_supplied_evidence']}",
                    f"- Requires full-text audit: "
                    f"{item['requires_targeted_full_text_audit']}",
                    "",
                ]
            )
    else:
        lines.append("None.")

    lines.extend(
        [
            "",
            "## Stop-search decision",
            "",
        ]
    )

    for key, value in stop.items():
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            "## Final surviving contribution",
            "",
            result["final_surviving_contribution"],
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
            f"- `{item['role']}` — `{item['path']}` — "
            f"SHA256 `{item['sha256']}`"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Final targeted D1-V008 audit of DOI "
            f"{TARGET_DOI} against surviving P1."
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
        PRIOR_C04,
        SEMANTIC_CORRECTION,
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

    papers = matrix.get("papers", [])
    if not papers or papers[0].get("paper_id") != TARGET_PAPER_ID:
        raise RuntimeError(
            f"{VERIFICATION_ID} matrix does not contain target "
            f"{TARGET_PAPER_ID}."
        )

    doi = (
        papers[0]
        .get("evidence", {})
        .get("paper", {})
        .get("doi", "")
    )

    if doi.lower() != TARGET_DOI.lower():
        raise RuntimeError(
            f"{VERIFICATION_ID} DOI mismatch: {doi!r}"
        )

    target_evidence = target_evidence_path()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    source_meta = [
        source_metadata(PRIOR_C04, "PRIOR_C04_CANONICAL_RESULT"),
        source_metadata(
            SEMANTIC_CORRECTION,
            "PREDECLARED_TOLERANCE_SEMANTIC_GUARDRAIL",
        ),
        source_metadata(CURRENT_MATRIX, "CURRENT_D1_V008_MATRIX"),
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
    result_json_path = run_dir / "FINAL_NAMED_TARGET_AUDIT.json"
    result_md_path = run_dir / "FINAL_NAMED_TARGET_AUDIT.md"

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
                "target_doi": TARGET_DOI,
                "target_paper_id": TARGET_PAPER_ID,
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
    print(f"[TARGET DOI] {TARGET_DOI}")
    print(f"[TARGET PAPER] {TARGET_PAPER_ID}")
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
            "Canonical D1-V008 audit already exists. Use --force only if "
            "you intentionally want to replace it."
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
        "target_doi": TARGET_DOI,
        "target_paper_id": TARGET_PAPER_ID,
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

    stop = result["stop_search_decision"]

    print(f"[STATUS] {result['status']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(
        f"[KILL CONDITION MET] "
        f"{result['kill_test']['kill_condition_met']}"
    )
    print(
        f"[TARGET DOI AUDIT COMPLETE] "
        f"{stop['target_doi_audit_complete']}"
    )
    print(
        f"[BROAD SEARCH SHOULD STOP] "
        f"{stop['broad_search_should_stop']}"
    )
    print(
        f"[FINAL NOVELTY LOCK ALLOWED] "
        f"{stop['final_novelty_lock_allowed']}"
    )
    print("[SAVED]", result_json_path.relative_to(ROOT))
    print("[SAVED]", result_md_path.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_JSON.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
