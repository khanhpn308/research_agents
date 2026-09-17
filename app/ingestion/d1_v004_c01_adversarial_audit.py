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
OUT_DIR = ROOT / "outputs" / "verification" / "D1-V004"
RUNS_DIR = OUT_DIR / "c01_adversarial_runs"

REGISTRY_PATH = ROOT / "data" / "paper_registry.json"
CURRENT_MATRIX = OUT_DIR / "verification_matrix.json"
PRIOR_SYNTHESIS = (
    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "cross_round_adversarial_synthesis.json"
)

CANONICAL_JSON = OUT_DIR / "C01_ADVERSARIAL_AUDIT.json"
CANONICAL_MD = OUT_DIR / "C01_ADVERSARIAL_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "C01_ADVERSARIAL_AUDIT_raw.json"


THREAT_ENUM = ["low", "medium", "high", "fatal"]
STATUS_ENUM = [
    "FALSIFIED",
    "SUBSTANTIALLY_NARROWED",
    "NO_KILL_BUT_HIGH_THREAT",
    "NO_TRANSFERABLE_KILL_FOUND",
]
EVIDENCE_ENUM = ["VERIFIED_FULL_TEXT", "INFERENCE"]


SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "current_p1",
        "executive_summary",
        "paper_audits",
        "part_i_part_ii_assessment",
        "kill_test",
        "strongest_threats",
        "surviving_gap",
        "c02_search_needed",
        "c02_search_rationale",
        "final_project_novelty_verdict_allowed",
        "recommended_next_action",
    ],
    "properties": {
        "status": {
            "type": "string",
            "enum": STATUS_ENUM,
        },
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
                    "discrete_or_interface_resolved_representation",
                    "continuum_or_equivalent_representation",
                    "interface_or_slip_law",
                    "governing_parameters",
                    "quantitative_error_evidence",
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
                    "discrete_or_interface_resolved_representation": {
                        "type": "string"
                    },
                    "continuum_or_equivalent_representation": {
                        "type": "string"
                    },
                    "interface_or_slip_law": {"type": "string"},
                    "governing_parameters": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "quantitative_error_evidence": {"type": "string"},
                    "declared_tolerance": {"type": "string"},
                    "validity_domain": {"type": "string"},
                    "breakdown_boundary": {"type": "string"},
                    "transferability_to_vacuum_layer_jamming": {
                        "type": "string"
                    },
                    "what_it_proves": {"type": "string"},
                    "what_it_does_not_prove": {"type": "string"},
                },
            },
        },
        "part_i_part_ii_assessment": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "part_i_discrete_model",
                "part_ii_continuum_model",
                "finite_n_quantitative_comparison",
                "asymptotic_convergence",
                "declared_acceptance_tolerance",
                "tolerance_defined_breakdown_boundary",
                "transferability_to_vacuum_layer_jamming",
                "evidence_refs",
                "assessment",
            ],
            "properties": {
                "part_i_discrete_model": {"type": "string"},
                "part_ii_continuum_model": {"type": "string"},
                "finite_n_quantitative_comparison": {"type": "boolean"},
                "asymptotic_convergence": {"type": "boolean"},
                "declared_acceptance_tolerance": {"type": "boolean"},
                "tolerance_defined_breakdown_boundary": {"type": "boolean"},
                "transferability_to_vacuum_layer_jamming": {
                    "type": "string",
                    "enum": [
                        "direct",
                        "partial",
                        "weak",
                        "not_demonstrated",
                    ],
                },
                "evidence_refs": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "assessment": {"type": "string"},
            },
        },
        "kill_test": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "equivalent_or_continuum_model",
                "interface_resolving_reference",
                "quantitative_mechanics_error",
                "finite_layer_or_parameter_sweep",
                "declared_acceptance_tolerance",
                "tolerance_defined_validity_domain",
                "validated_breakdown_boundary",
                "transferable_without_new_mechanics",
                "kill_condition_met",
                "evidence_summary",
            ],
            "properties": {
                "equivalent_or_continuum_model": {"type": "boolean"},
                "interface_resolving_reference": {"type": "boolean"},
                "quantitative_mechanics_error": {"type": "boolean"},
                "finite_layer_or_parameter_sweep": {"type": "boolean"},
                "declared_acceptance_tolerance": {"type": "boolean"},
                "tolerance_defined_validity_domain": {"type": "boolean"},
                "validated_breakdown_boundary": {"type": "boolean"},
                "transferable_without_new_mechanics": {"type": "boolean"},
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
                    "threat": {
                        "type": "string",
                        "enum": THREAT_ENUM,
                    },
                    "why_it_matters": {"type": "string"},
                    "remaining_gap": {"type": "string"},
                },
            },
        },
        "surviving_gap": {"type": "string"},
        "c02_search_needed": {"type": "boolean"},
        "c02_search_rationale": {"type": "string"},
        "final_project_novelty_verdict_allowed": {"type": "boolean"},
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_d1_v004_evidence() -> list[Path]:
    registry = load_json(REGISTRY_PATH)
    papers = registry.get("papers", []) if isinstance(registry, dict) else registry

    selected: list[dict[str, Any]] = []

    for paper in papers:
        if paper.get("source_type") != "verification":
            continue
        if paper.get("verification_id") != "D1-V004":
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

    evidence_paths: list[Path] = []
    seen: set[Path] = set()

    for paper in selected:
        rel = paper.get("evidence_file")
        if not rel:
            raise RuntimeError(
                f"{paper.get('paper_id')}: evidence_file is missing"
            )
        path = ROOT / "data" / str(rel)
        if not path.exists():
            raise RuntimeError(
                f"{paper.get('paper_id')}: evidence file not found: {path}"
            )
        if path in seen:
            continue
        seen.add(path)
        evidence_paths.append(path)

    if not evidence_paths:
        raise RuntimeError("No included D1-V004 evidence files found.")

    return evidence_paths


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

    for path in [PRIOR_SYNTHESIS, CURRENT_MATRIX, *evidence_paths]:
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
You are performing the D1-V004 / Track-C01 adversarial scientific audit
for an MSc research project on layer jamming and continuum-model validity.

This is a FALSIFICATION task, not a literature-summary task.

Use ONLY the supplied source bundle for scientific claims. The D1-V004
evidence JSON files were extracted from locally held full texts. Do not
invent equations, thresholds, validation results, or transferability that
are not supported by those sources.

======================================================================
CURRENT P1 TO ATTACK
======================================================================

The surviving provisional premise is approximately:

"Quantitative validity/breakdown mapping of an established continuum or
homogenized layer-jamming beam model relative to an interface-resolving
reference and experiment, using a declared prediction-error tolerance to
identify where the continuum approximation becomes unacceptable."

The scope is intentionally narrower than "develop a continuum model".
Existing layer-jamming continuum models, slip models, pressure effects,
curvature effects, bending-stiffness prediction, and experimental
validation are already known and must NOT be claimed as novel by
 themselves.

======================================================================
C01 QUESTION
======================================================================

Do the supplied adjacent-solid-mechanics papers already provide a
transferable framework that eliminates the scientific novelty of P1?

In particular, determine whether prior work already contains ALL of the
following in a form transferable to vacuum layer-jamming beams without
substantial new mechanics:

1. a named continuum/equivalent/homogenized representation;
2. a genuine interface-resolving or finite-layer reference;
3. a quantitative mechanics-error measure between the two;
4. a finite-layer-count and/or relevant parameter sweep;
5. a declared acceptance tolerance, not merely reported error;
6. a tolerance-defined validity domain;
7. a validated breakdown boundary;
8. transferability to pressure-dependent frictional layer jamming without
   introducing materially new coupling or constitutive mechanics.

Only if these conditions are collectively established may
kill_condition_met be true and status be FALSIFIED.

======================================================================
CRITICAL DISTINCTIONS
======================================================================

Preserve these distinctions rigorously:

quantitative error
!=
declared acceptance tolerance

asymptotic convergence as n -> infinity
!=
finite-n validity boundary

model vs FEM agreement
!=
continuum-vs-discrete validity mapping

known limitation
!=
tolerance-defined breakdown criterion

dimensionless parameter
!=
validated validity criterion

boundary-layer mismatch
!=
a mapped breakdown boundary unless error and acceptance criteria are
explicitly connected

analogy to layer jamming
!=
demonstrated transferability

======================================================================
MANDATORY PART-I / PART-II TEST
======================================================================

Audit these two papers as a coupled pair:

- Part I: slipping-layers discrete model;
- Part II: unlayered shear-weak continuum model.

Determine specifically whether Part II supplies only:

A) asymptotic convergence and finite-n quantitative comparison,

or whether it also supplies:

B) a declared tolerance that converts finite-n error into a validated
   validity domain / breakdown boundary.

Do not infer B from A.

======================================================================
PAPER-BY-PAPER AUDIT
======================================================================

Audit EVERY included D1-V004 paper exactly once. For each paper identify:

- physical analogue;
- discrete/interface-resolved representation;
- continuum/equivalent representation;
- interface/slip/friction law;
- governing dimensionless or scale parameters, if actually supported;
- quantitative error evidence;
- declared tolerance, if any;
- validity domain, if any;
- breakdown boundary, if any;
- transferability to vacuum layer jamming;
- what the evidence proves;
- what it does NOT prove;
- threat level to P1.

If a requested item is not supported by the evidence, say so explicitly.

======================================================================
STATUS RULES
======================================================================

FALSIFIED:
C01 itself establishes the complete transferable kill condition above.

SUBSTANTIALLY_NARROWED:
Adjacent mechanics already supplies a major portion of the validity
framework, such that P1 must be narrowed to genuinely layer-jamming-
specific coupling, variables, or validation not present there.

NO_KILL_BUT_HIGH_THREAT:
Strong analogues and quantitative comparisons exist, but no complete
transferable tolerance-defined breakdown framework is established.

NO_TRANSFERABLE_KILL_FOUND:
The supplied C01 literature does not establish a serious transferable
threat beyond general analogy.

Because only C01 has been audited, final_project_novelty_verdict_allowed
MUST be false in all cases. A FALSIFIED C01 verdict may reject the current
P1, but it does not establish a final alternative thesis direction.

If status is not FALSIFIED, state whether C02 partial/incomplete-
interaction literature must be searched next.

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
            "Scientific guardrail violation: C01 cannot authorize a final "
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
    kill_components = [
        kill["equivalent_or_continuum_model"],
        kill["interface_resolving_reference"],
        kill["quantitative_mechanics_error"],
        kill["finite_layer_or_parameter_sweep"],
        kill["declared_acceptance_tolerance"],
        kill["tolerance_defined_validity_domain"],
        kill["validated_breakdown_boundary"],
        kill["transferable_without_new_mechanics"],
    ]

    if kill["kill_condition_met"] and not all(kill_components):
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
        "# D1-V004 C01 Adversarial Audit",
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
        "## Part I / Part II assessment",
        "",
        result["part_i_part_ii_assessment"]["assessment"],
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
            "## Strongest threats",
            "",
        ]
    )

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
                f"- Threat to P1: **{item['threat_to_p1']}**",
                f"- Physical analogue: {item['physical_analogue']}",
                f"- Discrete/interface reference: "
                f"{item['discrete_or_interface_resolved_representation']}",
                f"- Continuum/equivalent representation: "
                f"{item['continuum_or_equivalent_representation']}",
                f"- Interface/slip law: {item['interface_or_slip_law']}",
                f"- Quantitative error: {item['quantitative_error_evidence']}",
                f"- Declared tolerance: {item['declared_tolerance']}",
                f"- Validity domain: {item['validity_domain']}",
                f"- Breakdown boundary: {item['breakdown_boundary']}",
                f"- Transferability: "
                f"{item['transferability_to_vacuum_layer_jamming']}",
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
            "## C02 decision",
            "",
            f"- **C02 search needed:** {result['c02_search_needed']}",
            f"- {result['c02_search_rationale']}",
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
        description="D1-V004 Track-C01 adversarial audit."
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

    for path in [REGISTRY_PATH, CURRENT_MATRIX, PRIOR_SYNTHESIS]:
        if not path.exists():
            raise RuntimeError(f"Required input not found: {path}")

    evidence_paths = collect_d1_v004_evidence()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    source_meta = [
        source_metadata(PRIOR_SYNTHESIS, "PRIOR_CROSS_ROUND_CONTEXT"),
        source_metadata(CURRENT_MATRIX, "CURRENT_C01_MATRIX"),
    ] + [
        source_metadata(path, "CURRENT_C01_VERIFIED_FULL_TEXT_EVIDENCE")
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
    result_json_path = run_dir / "C01_ADVERSARIAL_AUDIT.json"
    result_md_path = run_dir / "C01_ADVERSARIAL_AUDIT.md"

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
    print(f"[D1-V004 VERIFIED PAPERS] {len(evidence_paths)}")
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
            "Canonical C01 audit already exists. Use --force only if you "
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
    markdown = render_markdown(result, source_meta, bundle_sha256)
    result_md_path.write_text(markdown, encoding="utf-8")

    shutil.copy2(result_json_path, CANONICAL_JSON)
    shutil.copy2(result_md_path, CANONICAL_MD)
    shutil.copy2(raw_path, CANONICAL_RAW)

    print(f"[STATUS] {result['status']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(f"[KILL CONDITION MET] {result['kill_test']['kill_condition_met']}")
    print(f"[C02 SEARCH NEEDED] {result['c02_search_needed']}")
    print("[SAVED]", result_json_path.relative_to(ROOT))
    print("[SAVED]", result_md_path.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_JSON.relative_to(ROOT))
    print("[UPDATED]", CANONICAL_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
