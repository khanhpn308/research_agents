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
OUT_DIR = ROOT / "outputs" / "verification" / "D1-V007"
RUNS_DIR = OUT_DIR / "c04_adversarial_runs"

REGISTRY_PATH = ROOT / "data" / "paper_registry.json"
CURRENT_MATRIX = OUT_DIR / "verification_matrix.json"
PRIOR_C03 = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V006"
    / "C03_ADVERSARIAL_AUDIT.json"
)

FOCAL_PAPER_ID = "ca46dc062d"
EXPECTED_FORWARD_CITATIONS = 3
MISSING_NAMED_TARGET_DOI = "10.1061/JSENDH.STENG-13096"

CANONICAL_JSON = OUT_DIR / "C04_ADVERSARIAL_AUDIT.json"
CANONICAL_MD = OUT_DIR / "C04_ADVERSARIAL_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "C04_ADVERSARIAL_AUDIT_raw.json"

STATUS_ENUM = [
    "FALSIFIED",
    "SURVIVES_REVISED_SCOPE",
    "FORWARD_CITATION_BRANCH_CLOSED_NO_KILL",
    "INCONCLUSIVE_MISSING_TARGET",
]
THREAT_ENUM = ["low", "medium", "high", "fatal"]
EVIDENCE_ENUM = ["VERIFIED_FULL_TEXT", "INFERENCE"]
TRANSFER_ENUM = ["direct", "partial", "weak", "not_demonstrated"]
ROLE_ENUM = [
    "direct_mechanical_extension",
    "adjacent_method_extension",
    "application_or_context_citation",
    "other",
]


SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "current_p1",
        "executive_summary",
        "citation_closure",
        "paper_audits",
        "four_link_chain_audit",
        "kill_test",
        "strongest_threats",
        "surviving_gap",
        "stop_search_decision",
        "final_novelty_lock_allowed",
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
        "citation_closure": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "focal_paper_id",
                "focal_paper_title",
                "expected_current_forward_citations",
                "audited_forward_citations",
                "all_current_forward_citations_audited",
                "target_doi_10_1061_present_in_current_round",
                "missing_named_targets",
                "closure_statement",
            ],
            "properties": {
                "focal_paper_id": {"type": "string"},
                "focal_paper_title": {"type": "string"},
                "expected_current_forward_citations": {"type": "integer"},
                "audited_forward_citations": {"type": "integer"},
                "all_current_forward_citations_audited": {"type": "boolean"},
                "target_doi_10_1061_present_in_current_round": {
                    "type": "boolean"
                },
                "missing_named_targets": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "closure_statement": {"type": "string"},
            },
        },
        "paper_audits": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "paper_id",
                    "title",
                    "evidence_status",
                    "citation_role",
                    "threat_to_p1",
                    "uses_focal_mechanical_model",
                    "pressure_or_preload_role",
                    "friction_or_slip_role",
                    "continuum_or_reduced_model",
                    "discrete_or_interface_resolved_reference",
                    "quantitative_model_form_error",
                    "predeclared_acceptance_tolerance",
                    "tolerance_defined_validity_boundary",
                    "experiment_crosses_boundary",
                    "vacuum_layer_jamming_transferability",
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
                    "citation_role": {
                        "type": "string",
                        "enum": ROLE_ENUM,
                    },
                    "threat_to_p1": {
                        "type": "string",
                        "enum": THREAT_ENUM,
                    },
                    "uses_focal_mechanical_model": {"type": "boolean"},
                    "pressure_or_preload_role": {"type": "string"},
                    "friction_or_slip_role": {"type": "string"},
                    "continuum_or_reduced_model": {"type": "string"},
                    "discrete_or_interface_resolved_reference": {
                        "type": "string"
                    },
                    "quantitative_model_form_error": {"type": "string"},
                    "predeclared_acceptance_tolerance": {"type": "string"},
                    "tolerance_defined_validity_boundary": {"type": "string"},
                    "experiment_crosses_boundary": {"type": "string"},
                    "vacuum_layer_jamming_transferability": {
                        "type": "string",
                        "enum": TRANSFER_ENUM,
                    },
                    "what_it_proves": {"type": "string"},
                    "what_it_does_not_prove": {"type": "string"},
                },
            },
        },
        "four_link_chain_audit": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "pressure_preload_to_friction_slip",
                "friction_slip_to_continuum_discrete_discrepancy",
                "discrepancy_to_predeclared_tolerance",
                "tolerance_to_experimentally_validated_breakdown_boundary",
                "vacuum_to_contact_pressure_mapping",
                "layer_separation_or_pressure_redistribution",
                "chain_complete",
                "chain_assessment",
            ],
            "properties": {
                "pressure_preload_to_friction_slip": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["supported", "evidence"],
                    "properties": {
                        "supported": {"type": "boolean"},
                        "evidence": {"type": "string"},
                    },
                },
                "friction_slip_to_continuum_discrete_discrepancy": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["supported", "evidence"],
                    "properties": {
                        "supported": {"type": "boolean"},
                        "evidence": {"type": "string"},
                    },
                },
                "discrepancy_to_predeclared_tolerance": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["supported", "evidence"],
                    "properties": {
                        "supported": {"type": "boolean"},
                        "evidence": {"type": "string"},
                    },
                },
                "tolerance_to_experimentally_validated_breakdown_boundary": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["supported", "evidence"],
                    "properties": {
                        "supported": {"type": "boolean"},
                        "evidence": {"type": "string"},
                    },
                },
                "vacuum_to_contact_pressure_mapping": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["supported", "evidence"],
                    "properties": {
                        "supported": {"type": "boolean"},
                        "evidence": {"type": "string"},
                    },
                },
                "layer_separation_or_pressure_redistribution": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["supported", "evidence"],
                    "properties": {
                        "supported": {"type": "boolean"},
                        "evidence": {"type": "string"},
                    },
                },
                "chain_complete": {"type": "boolean"},
                "chain_assessment": {"type": "string"},
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
        "stop_search_decision": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "focal_forward_citation_branch_closed",
                "target_doi_audit_complete",
                "additional_high_threat_named_target_remaining",
                "stop_broad_search",
                "decision_rationale",
            ],
            "properties": {
                "focal_forward_citation_branch_closed": {"type": "boolean"},
                "target_doi_audit_complete": {"type": "boolean"},
                "additional_high_threat_named_target_remaining": {
                    "type": "boolean"
                },
                "stop_broad_search": {"type": "boolean"},
                "decision_rationale": {"type": "string"},
            },
        },
        "final_novelty_lock_allowed": {"type": "boolean"},
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def registry_papers() -> list[dict[str, Any]]:
    registry = load_json(REGISTRY_PATH)
    return registry.get("papers", []) if isinstance(registry, dict) else registry


def collect_round_evidence() -> list[Path]:
    selected: list[dict[str, Any]] = []

    for paper in registry_papers():
        if paper.get("source_type") != "verification":
            continue
        if paper.get("verification_id") != "D1-V007":
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
        key=lambda item: (
            str(item.get("filename", "")).lower(),
            str(item.get("paper_id", "")),
        )
    )

    paths: list[Path] = []
    for paper in selected:
        rel = paper.get("evidence_file")
        if not rel:
            raise RuntimeError(
                f"{paper.get('paper_id')}: evidence_file missing"
            )
        path = ROOT / "data" / str(rel)
        if not path.exists():
            raise RuntimeError(f"Evidence file not found: {path}")
        paths.append(path)

    if len(paths) != EXPECTED_FORWARD_CITATIONS:
        raise RuntimeError(
            "D1-V007 must contain exactly "
            f"{EXPECTED_FORWARD_CITATIONS} included forward-citation papers; "
            f"found {len(paths)}."
        )

    return paths


def focal_evidence_path() -> Path:
    matches = [
        p for p in registry_papers()
        if p.get("paper_id") == FOCAL_PAPER_ID
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected exactly one focal registry record for "
            f"{FOCAL_PAPER_ID}; found {len(matches)}."
        )

    paper = matches[0]
    rel = paper.get("evidence_file")
    if not rel:
        raise RuntimeError(
            f"Focal paper {FOCAL_PAPER_ID}: evidence_file missing."
        )

    path = ROOT / "data" / str(rel)
    if not path.exists():
        raise RuntimeError(f"Focal evidence file not found: {path}")

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
    round_evidence: list[Path],
    focal_evidence: Path,
    source_meta: list[dict[str, Any]],
) -> str:
    ordered_sources = [
        PRIOR_C03,
        focal_evidence,
        CURRENT_MATRIX,
        *round_evidence,
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
You are performing D1-V007 / C04, a targeted adversarial
FORWARD-CITATION CLOSURE audit for an MSc research project on vacuum
layer jamming and reduced/continuum model validity.

This is a FALSIFICATION task. It is NOT a generic paper summary.

Use ONLY the supplied source bundle for scientific claims. Evidence JSON
files marked as verified full text were extracted from locally held
papers. Do not invent equations, thresholds, experiments, DOI metadata,
citation relationships, or transferability.

======================================================================
CURRENT SURVIVING P1 AFTER C03
======================================================================

The provisional surviving premise is now intentionally narrow:

"For ONE specified reduced/continuum vacuum-layer-jamming beam model
under quasi-static planar bending, define output-specific PREDECLARED
model-form acceptance tolerances and determine experimentally validated
validity/breakdown boundaries against an interface-resolving/full-layer
reference, while explicitly accounting for vacuum-pressure-controlled
normal contact, friction/slip evolution, and where necessary pressure
redistribution or layer separation."

C03 substantially narrowed P1.

C03 already found that the focal paper {FOCAL_PAPER_ID},
"The global-local mechanical behaviors of multilayered structure and
applications to superconducting coils", already provides much of the
generic framework:

- a multilayer continuum/homogenized mechanical model;
- explicit Coulomb friction/contact mechanics;
- a discrete contact reference;
- finite layer-count/deformation sweeps;
- quantitative model-form error;
- a 5 percent displacement-error threshold;
- a resulting layer-count-dependent permissible-deformation domain;
- multilayer bending and coil experiments.

IMPORTANT SEMANTIC CORRECTION FOR THIS RUN:

The supplied focal-paper evidence establishes an EXPLICIT / ADOPTED
5 percent applicability threshold. It does NOT establish that the
5 percent threshold was PREDECLARED a priori before validation or
before inspecting model-form errors.

For this audit, PREDECLARED has a strict meaning:
the acceptance criterion must have been fixed before the relevant
validation/error results were examined, and that temporal ordering must
be explicitly supported by the supplied source evidence.

Therefore:
- do NOT infer "predeclared" merely because a paper uses an explicit
  threshold;
- do NOT infer "predeclared" from words such as applicability,
  criterion, permissible error, target error, or 5 percent threshold;
- if the source only states that a threshold was used, adopted, or
  applied, classify predeclared acceptance tolerance as NOT ESTABLISHED;
- unless the source explicitly supports prior declaration, set
  kill_test.predeclared_acceptance_tolerance = false and
  four_link_chain_audit.discrepancy_to_predeclared_tolerance.supported
  = false.

Therefore the following claims ARE NOT novel by themselves:

- proposing a continuum/homogenized multilayer model;
- comparing continuum and discrete contact models;
- plotting quantitative prediction error;
- sweeping layer count or deformation;
- defining a generic 5 percent applicability criterion;
- experimentally validating overall response away from a breakdown
  boundary.

The residual question is much narrower.

======================================================================
C04 PURPOSE
======================================================================

Audit ALL {EXPECTED_FORWARD_CITATIONS} currently identified forward
citations of focal paper {FOCAL_PAPER_ID}.

Determine whether these descendants close the remaining chain:

pressure / preload
    ->
normal-contact state
    ->
friction capacity and stick / partial-slip / gross-slip evolution
    ->
reduced or continuum prediction
    ->
interface-resolving / discrete / full-layer reference
    ->
quantitative MODEL-FORM discrepancy
    ->
PREDECLARED acceptance tolerance
    ->
tolerance-defined breakdown boundary
    ->
EXPERIMENTS intentionally sampling both sides of that boundary.

Also determine whether the descendants supply the missing
vacuum-specific transfer mechanics:

vacuum pressure
    ->
normal-contact-pressure field
    ->
possible pressure redistribution / local separation
    ->
friction/slip evolution
    ->
model-form validity loss.

The central question is NOT:
"Are these papers sophisticated?"

The central question IS:
"Do these papers remove the need for a new scientific contribution in
vacuum-layer-jamming model-validity mapping?"

======================================================================
MANDATORY PAPER-BY-PAPER CLASSIFICATION
======================================================================

Audit EVERY D1-V007 forward-citation paper exactly once.

For each paper classify its citation role as exactly one of:

1. direct_mechanical_extension
   The paper actually uses, extends, tests, or materially develops the
   focal multilayer mechanical model.

2. adjacent_method_extension
   The paper extends a related homogenization/global-local/contact
   method, but the governing mechanics or geometry are materially
   different.

3. application_or_context_citation
   The focal paper is cited only for geometry, application background,
   coil configuration, contextual motivation, or another non-killing
   purpose.

4. other

For each paper explicitly audit:

- whether it uses the focal mechanical model;
- pressure/preload role;
- friction/slip role;
- reduced/continuum representation;
- discrete/interface-resolving reference;
- quantitative MODEL-FORM error;
- PREDECLARED acceptance tolerance;
- tolerance-defined validity boundary;
- whether experiments deliberately test points on BOTH sides of the
  predicted boundary;
- transferability to vacuum layer jamming;
- what it proves;
- what it does not prove;
- threat level to P1.

If a feature is absent, state that it is absent.
Do not upgrade general model agreement into a validity-boundary test.

======================================================================
FOUR-LINK CHAIN -- MUST BE ANSWERED EXPLICITLY
======================================================================

You must separately decide whether the supplied evidence supports each
of these links:

LINK 1
pressure/preload -> friction/slip

LINK 2
friction/slip -> continuum-versus-discrete MODEL-FORM discrepancy

LINK 3
model-form discrepancy -> PREDECLARED acceptance tolerance

LINK 4
predeclared tolerance -> experimentally validated breakdown boundary,
with experiments intentionally sampling both sides of the boundary.

Then separately audit:

LINK 5
vacuum pressure -> spatial normal-contact-pressure field

LINK 6
pressure redistribution and/or local layer separation -> change in the
validity boundary.

A physical slip threshold is NOT a model-validity boundary.

A reported post-hoc percentage error is NOT a predeclared acceptance
tolerance.

Experimental agreement at a few operating points is NOT experimental
validation of a breakdown boundary.

A mathematical or algorithmic analogy is NOT mechanical transferability.

A superconducting-coil application is NOT automatically transferable to
vacuum layer jamming.

======================================================================
C04 KILL CONDITION
======================================================================

kill_condition_met may be TRUE only if the supplied evidence,
individually or collectively, establishes ALL of the following in a
framework transferable to vacuum layer jamming without a materially new
mechanics contribution:

1. pressure or preload controls the relevant contact state;
2. friction/slip is explicit;
3. a named reduced/continuum model exists;
4. an interface-resolved/discrete/full-layer reference exists;
5. quantitative MODEL-FORM error is evaluated over the relevant
   parameter space;
6. a PREDECLARED acceptance tolerance is used for model validity;
   STRICT RULE: an explicit/adopted threshold is insufficient. The
   source must explicitly support that the tolerance was fixed a priori
   before the relevant validation/error evidence was inspected.
7. that tolerance defines a breakdown/validity boundary;
8. experiments deliberately sample BOTH sides of that boundary;
9. transfer from the demonstrated system to vacuum layer jamming does
   not require new vacuum-to-pressure, pressure-redistribution,
   separation, or friction/contact mechanics.

If even ONE required element is not established, kill_condition_met
must be FALSE.

In particular, for the current focal evidence, the existence of the
5 percent displacement-error threshold alone MUST NOT satisfy item 6.
Treat item 6 as false unless another supplied verified-full-text source
explicitly establishes prior declaration of the acceptance tolerance.

======================================================================
FORWARD-CITATION CLOSURE
======================================================================

Scopus currently reports exactly {EXPECTED_FORWARD_CITATIONS} forward
citations for focal paper {FOCAL_PAPER_ID}, and D1-V007 is intended to
contain those {EXPECTED_FORWARD_CITATIONS} full-text papers.

If all three supplied D1-V007 papers correspond to the complete current
forward-citation set, then
all_current_forward_citations_audited = true
and
focal_forward_citation_branch_closed = true
FOR THE CURRENT SEARCH DATE.

Do not interpret this as proof that no future citation can appear.

======================================================================
KNOWN OUTSTANDING NAMED TARGET
======================================================================

A separate high-threat named target remains outside this forward-citation
branch unless it is actually present in the supplied D1-V007 evidence:

DOI {MISSING_NAMED_TARGET_DOI}

If that DOI is not represented by a verified full-text paper in the
current source bundle:

- target_doi_10_1061_present_in_current_round = false;
- target_doi_audit_complete = false;
- include the DOI in missing_named_targets;
- final_novelty_lock_allowed = false.

Do NOT treat completion of the three forward citations as completion of
the entire C04 falsification round while this named target remains
unaudited.

======================================================================
STOP-SEARCH RULE
======================================================================

The purpose is to STOP broad searching, not to generate endless C05,
C06, C07 rounds.

If the focal forward-citation branch is fully audited and no kill is
found, broad exploratory search should normally stop.

However final novelty lock is allowed only when:

- the focal forward-citation branch is closed for the current search;
- the named DOI {MISSING_NAMED_TARGET_DOI} has been audited or a
  documented full-text-unavailable decision has been made;
- no other specifically named high-threat target remains;
- the surviving P1 is written narrowly around model-form validity rather
  than generic model development.

If the named DOI remains unaudited, recommend ONLY that targeted action.
Do not recommend another broad keyword sweep.

======================================================================
OUTPUT DISCIPLINE
======================================================================

Return ONLY one JSON object conforming exactly to the supplied JSON
schema.

For paper_audits:
- include exactly {EXPECTED_FORWARD_CITATIONS} records;
- each D1-V007 paper must appear exactly once;
- use VERIFIED_FULL_TEXT when grounded in supplied evidence JSON;
- do not include the focal paper itself as a D1-V007 paper audit.

For citation_closure:
- focal_paper_id must be {FOCAL_PAPER_ID};
- expected_current_forward_citations must be
  {EXPECTED_FORWARD_CITATIONS};
- audited_forward_citations must equal the number actually audited.

Do not claim final novelty merely because no killer appears in these
three descendants.

======================================================================
SOURCE BUNDLE
======================================================================

{bundle}
"""


def validate_result(
    result: dict[str, Any],
    expected_papers: int,
) -> None:
    audits = result.get("paper_audits")
    if not isinstance(audits, list):
        raise RuntimeError("paper_audits must be a list.")
    if len(audits) != expected_papers:
        raise RuntimeError(
            f"Expected {expected_papers} paper audits; found {len(audits)}."
        )

    ids = [item.get("paper_id") for item in audits]
    if len(set(ids)) != len(ids):
        raise RuntimeError("paper_audits contains duplicate paper_id values.")

    closure = result.get("citation_closure", {})
    if closure.get("focal_paper_id") != FOCAL_PAPER_ID:
        raise RuntimeError(
            "citation_closure.focal_paper_id does not match focal paper."
        )
    if (
        closure.get("expected_current_forward_citations")
        != EXPECTED_FORWARD_CITATIONS
    ):
        raise RuntimeError(
            "citation_closure.expected_current_forward_citations mismatch."
        )
    if closure.get("audited_forward_citations") != expected_papers:
        raise RuntimeError(
            "citation_closure.audited_forward_citations mismatch."
        )

    kill = result.get("kill_test", {})
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
            key for key in required_kill_fields
            if kill.get(key) is not True
        ]
        if missing:
            raise RuntimeError(
                "kill_condition_met=True but required kill fields are false: "
                + ", ".join(missing)
            )

    stop = result.get("stop_search_decision", {})
    if result.get("final_novelty_lock_allowed"):
        if not stop.get("focal_forward_citation_branch_closed"):
            raise RuntimeError(
                "Final novelty lock cannot be allowed before forward-citation "
                "closure."
            )
        if not stop.get("target_doi_audit_complete"):
            raise RuntimeError(
                "Final novelty lock cannot be allowed while named DOI target "
                "is unaudited."
            )
        if stop.get("additional_high_threat_named_target_remaining"):
            raise RuntimeError(
                "Final novelty lock cannot be allowed with a named high-threat "
                "target remaining."
            )


def render_markdown(
    result: dict[str, Any],
    manifest: list[dict[str, Any]],
    bundle_sha256: str,
) -> str:
    closure = result["citation_closure"]
    stop = result["stop_search_decision"]

    lines = [
        "# D1-V007 C04 Adversarial Forward-Citation Audit",
        "",
        f"- **Status:** {result['status']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Bundle SHA256:** {bundle_sha256}",
        f"- **Kill condition met:** "
        f"{result['kill_test']['kill_condition_met']}",
        f"- **Final novelty lock allowed:** "
        f"{result['final_novelty_lock_allowed']}",
        "",
        "## Current P1",
        "",
        result["current_p1"],
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## Forward-citation closure",
        "",
        f"- Focal paper: {closure['focal_paper_id']} — "
        f"{closure['focal_paper_title']}",
        f"- Expected current forward citations: "
        f"{closure['expected_current_forward_citations']}",
        f"- Audited forward citations: "
        f"{closure['audited_forward_citations']}",
        f"- All current forward citations audited: "
        f"{closure['all_current_forward_citations_audited']}",
        f"- Named DOI present in this round: "
        f"{closure['target_doi_10_1061_present_in_current_round']}",
        f"- Missing named targets: "
        f"{', '.join(closure['missing_named_targets']) or 'None'}",
        "",
        closure["closure_statement"],
        "",
        "## Four-link chain audit",
        "",
    ]

    chain = result["four_link_chain_audit"]
    chain_keys = [
        "pressure_preload_to_friction_slip",
        "friction_slip_to_continuum_discrete_discrepancy",
        "discrepancy_to_predeclared_tolerance",
        "tolerance_to_experimentally_validated_breakdown_boundary",
        "vacuum_to_contact_pressure_mapping",
        "layer_separation_or_pressure_redistribution",
    ]
    for key in chain_keys:
        item = chain[key]
        lines.extend(
            [
                f"### {key}",
                "",
                f"- Supported: **{item['supported']}**",
                f"- Evidence: {item['evidence']}",
                "",
            ]
        )

    lines.extend(
        [
            f"- **Complete chain:** {chain['chain_complete']}",
            "",
            chain["chain_assessment"],
            "",
            "## Kill test",
            "",
        ]
    )

    for key, value in result["kill_test"].items():
        if key == "evidence_summary":
            continue
        lines.append(f"- **{key}:** {value}")

    lines.extend(
        [
            "",
            result["kill_test"]["evidence_summary"],
            "",
            "## Paper-by-paper audit",
            "",
        ]
    )

    for item in result["paper_audits"]:
        lines.extend(
            [
                f"### {item['paper_id']} — {item['title']}",
                "",
                f"- Evidence: {item['evidence_status']}",
                f"- Citation role: **{item['citation_role']}**",
                f"- Threat: **{item['threat_to_p1']}**",
                f"- Uses focal mechanical model: "
                f"{item['uses_focal_mechanical_model']}",
                f"- Pressure/preload: {item['pressure_or_preload_role']}",
                f"- Friction/slip: {item['friction_or_slip_role']}",
                f"- Continuum/reduced model: "
                f"{item['continuum_or_reduced_model']}",
                f"- Discrete/reference model: "
                f"{item['discrete_or_interface_resolved_reference']}",
                f"- Quantitative model-form error: "
                f"{item['quantitative_model_form_error']}",
                f"- Predeclared tolerance: "
                f"{item['predeclared_acceptance_tolerance']}",
                f"- Validity boundary: "
                f"{item['tolerance_defined_validity_boundary']}",
                f"- Experiment crosses boundary: "
                f"{item['experiment_crosses_boundary']}",
                f"- Vacuum transferability: "
                f"{item['vacuum_layer_jamming_transferability']}",
                f"- Proves: {item['what_it_proves']}",
                f"- Does not prove: {item['what_it_does_not_prove']}",
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

    lines.extend(
        [
            "## Surviving gap",
            "",
            result["surviving_gap"],
            "",
            "## Stop-search decision",
            "",
            f"- Forward-citation branch closed: "
            f"{stop['focal_forward_citation_branch_closed']}",
            f"- Named DOI audit complete: "
            f"{stop['target_doi_audit_complete']}",
            f"- Additional named high-threat target remaining: "
            f"{stop['additional_high_threat_named_target_remaining']}",
            f"- Stop broad search: {stop['stop_broad_search']}",
            "",
            stop["decision_rationale"],
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
            f"- {item['path']} — {item['role']} — {item['sha256']}"
        )

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="D1-V007 C04 targeted adversarial forward-citation audit."
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

    for required_path in [REGISTRY_PATH, CURRENT_MATRIX, PRIOR_C03]:
        if not required_path.exists():
            raise RuntimeError(f"Required input not found: {required_path}")

    round_evidence = collect_round_evidence()
    focal_evidence = focal_evidence_path()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    source_meta = [
        source_metadata(PRIOR_C03, "PRIOR_C03_ADVERSARIAL_RESULT"),
        source_metadata(focal_evidence, "FOCAL_VERIFIED_FULL_TEXT_EVIDENCE"),
        source_metadata(CURRENT_MATRIX, "CURRENT_C04_MATRIX"),
    ] + [
        source_metadata(
            evidence_path,
            "CURRENT_C04_FORWARD_CITATION_VERIFIED_FULL_TEXT_EVIDENCE",
        )
        for evidence_path in round_evidence
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
    result_json_path = run_dir / "C04_ADVERSARIAL_AUDIT.json"
    result_md_path = run_dir / "C04_ADVERSARIAL_AUDIT.md"

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
                "included_forward_citation_evidence_files": len(
                    round_evidence
                ),
                "focal_paper_id": FOCAL_PAPER_ID,
                "expected_current_forward_citations": (
                    EXPECTED_FORWARD_CITATIONS
                ),
                "known_outstanding_named_target_doi": (
                    MISSING_NAMED_TARGET_DOI
                ),
                "sources": source_meta,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    prompt = build_prompt(
        round_evidence=round_evidence,
        focal_evidence=focal_evidence,
        source_meta=source_meta,
    )
    prompt_path.write_text(prompt, encoding="utf-8")

    print(f"[RUN] {run_id}")
    print(f"[D1-V007 FORWARD-CITATION PAPERS] {len(round_evidence)}")
    print(f"[FOCAL PAPER] {FOCAL_PAPER_ID}")
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
            "Canonical C04 audit already exists. Use --force only if you "
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

    validate_result(result, expected_papers=len(round_evidence))

    result["_provenance"] = {
        "run_id": run_id,
        "created_at_utc": utc_now().isoformat(),
        "evidence_bundle_sha256": bundle_sha256,
        "model": args.model,
        "effort": args.effort,
        "included_forward_citation_evidence_files": len(round_evidence),
        "focal_paper_id": FOCAL_PAPER_ID,
        "known_outstanding_named_target_doi": MISSING_NAMED_TARGET_DOI,
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
    print(
        "[FORWARD CITATION BRANCH CLOSED] "
        f"{result['stop_search_decision']['focal_forward_citation_branch_closed']}"
    )
    print(
        "[TARGET DOI AUDIT COMPLETE] "
        f"{result['stop_search_decision']['target_doi_audit_complete']}"
    )
    print(
        "[KILL CONDITION MET] "
        f"{result['kill_test']['kill_condition_met']}"
    )
    print(
        "[FINAL NOVELTY LOCK ALLOWED] "
        f"{result['final_novelty_lock_allowed']}"
    )
    print("[SAVED]", result_json_path.relative_to(ROOT))
    print("[SAVED]", result_md_path.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_JSON.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
