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

OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
RUNS_DIR = OUT_DIR / "final_adjudication_runs"

PROTOCOL = ROOT / "docs" / "protocols" / "MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md"
V001 = ROOT / "outputs" / "verification" / "MP1-V001" / "CORE_PRIOR_ART_AUDIT.json"
MATRIX = OUT_DIR / "verification_matrix.json"
INTERIM_AUDIT = OUT_DIR / "TARGETED_THREAT_AUDIT.json"
COVERAGE = OUT_DIR / "citation_coverage.json"
PROJECT_STATE = ROOT / "docs" / "project" / "MP1_MENTOR_PIVOT_CURRENT.md"

CANONICAL_JSON = OUT_DIR / "FINAL_ADJUDICATION.json"
CANONICAL_MD = OUT_DIR / "FINAL_ADJUDICATION.md"
CANONICAL_RAW = OUT_DIR / "FINAL_ADJUDICATION_raw.json"

OUTCOMES = [
    "FALSIFIED",
    "SUBSTANTIALLY_NARROWED",
    "SURVIVES_TARGETED_CITATION_CHASE",
    "INCONCLUSIVE",
]

READINESS = [
    "READY_FOR_CROSS_DIRECTION_COMPARISON",
    "READY_WITH_TITLE_REFINEMENT",
    "NOT_READY",
    "DROP_MP1",
]

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "protocol_outcome",
        "confidence",
        "executive_summary",
        "citation_coverage_closed",
        "direct_kill_found",
        "surviving_contribution",
        "what_is_not_novel",
        "what_remains_unestablished",
        "final_research_question",
        "scientific_hypothesis",
        "model_discrimination_plan",
        "experimental_scope",
        "msc_topic_readiness",
        "requires_cross_direction_comparison_with_d1_m1",
        "topic_lock_rationale",
        "title_draft_en",
        "title_draft_vi",
        "remaining_pre_execution_checks",
        "astra_escalation_required",
        "astra_escalation_reason",
        "recommended_next_action",
    ],
    "properties": {
        "protocol_outcome": {
            "type": "string",
            "enum": OUTCOMES,
        },
        "confidence": {
            "type": "string",
            "enum": ["low", "medium", "high"],
        },
        "executive_summary": {"type": "string"},
        "citation_coverage_closed": {"type": "boolean"},
        "direct_kill_found": {"type": "boolean"},
        "surviving_contribution": {"type": "string"},
        "what_is_not_novel": {
            "type": "array",
            "items": {"type": "string"},
        },
        "what_remains_unestablished": {
            "type": "array",
            "items": {"type": "string"},
        },
        "final_research_question": {"type": "string"},
        "scientific_hypothesis": {"type": "string"},
        "model_discrimination_plan": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "baseline_model",
                "transformation_aware_model",
                "comparison_domain",
                "falsification_logic",
            ],
            "properties": {
                "baseline_model": {"type": "string"},
                "transformation_aware_model": {"type": "string"},
                "comparison_domain": {"type": "string"},
                "falsification_logic": {"type": "string"},
            },
        },
        "experimental_scope": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "independent_variables",
                "dependent_variables",
                "control_variables",
                "minimum_measurements",
            ],
            "properties": {
                "independent_variables": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "dependent_variables": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "control_variables": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "minimum_measurements": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        },
        "msc_topic_readiness": {
            "type": "string",
            "enum": READINESS,
        },
        "requires_cross_direction_comparison_with_d1_m1": {
            "type": "boolean",
        },
        "topic_lock_rationale": {"type": "string"},
        "title_draft_en": {"type": "string"},
        "title_draft_vi": {"type": "string"},
        "remaining_pre_execution_checks": {
            "type": "array",
            "items": {"type": "string"},
        },
        "astra_escalation_required": {"type": "boolean"},
        "astra_escalation_reason": {"type": "string"},
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


def validate_inputs() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    required = [
        PROTOCOL,
        V001,
        MATRIX,
        INTERIM_AUDIT,
        COVERAGE,
        PROJECT_STATE,
    ]
    for path in required:
        if not path.exists():
            raise RuntimeError(f"Required input not found: {path}")

    matrix = load_json(MATRIX)
    audit = load_json(INTERIM_AUDIT)
    coverage = load_json(COVERAGE)

    if matrix.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("Verification matrix ID mismatch.")

    if int(matrix.get("paper_count", 0)) < 1:
        raise RuntimeError("V002 matrix is empty.")

    for paper in matrix.get("papers", []):
        if (
            paper.get("screening_status") != "included"
            or paper.get("ingestion_status") != "complete"
            or paper.get("evidence_status") != "present"
        ):
            raise RuntimeError(
                f"{paper.get('paper_id')}: incomplete V002 evidence state."
            )

    stop = coverage.get("stop_condition", {})
    if not stop.get("all_required_directions_screened"):
        raise RuntimeError(
            "Citation coverage is not closed: "
            "all_required_directions_screened=false."
        )
    if not stop.get("no_unresolved_high_threat_source"):
        raise RuntimeError(
            "Citation coverage is not closed: "
            "unresolved high-threat sources remain."
        )
    if not stop.get("satisfied"):
        raise RuntimeError(
            "Citation coverage stop condition is not satisfied."
        )

    return matrix, audit, coverage


def build_prompt(sources: list[dict[str, Any]]) -> str:
    ordered = [
        PROTOCOL,
        PROJECT_STATE,
        V001,
        MATRIX,
        INTERIM_AUDIT,
        COVERAGE,
    ]

    blocks: list[str] = []
    for path in ordered:
        rel = str(path.relative_to(ROOT))
        item = next(x for x in sources if x["path"] == rel)
        blocks += [
            "=" * 100,
            f"SOURCE: {rel}",
            f"SHA256: {item['sha256']}",
            f"ROLE: {item['role']}",
            "=" * 100,
            read_text(path),
            "",
        ]

    bundle = "\n".join(blocks)

    return f"""
You are the FINAL SCIENTIFIC ADJUDICATOR for MP1-V002, a Mechanical
Engineering MSc research-direction falsification workflow.

This is NOT an interim literature summary.

The targeted full-text matrix is complete for the current V002 round and the
protocol-bounded backward/forward citation chase has reached its documented
stop condition.

Use ONLY the supplied repository sources for scientific claims.

======================================================================
CORE DECISION
======================================================================

Issue one final V002 protocol outcome:

- FALSIFIED
- SUBSTANTIALLY_NARROWED
- SURVIVES_TARGETED_CITATION_CHASE
- INCONCLUSIVE

Absence of a direct kill is NOT proof of universal novelty.

SURVIVES_TARGETED_CITATION_CHASE means only:
the defined adversarial V002 search protocol is closed, no direct kill was
found within that protocol, and a narrowly formulated mechanics contribution
remains defensible enough to advance to research design / cross-direction
comparison.

======================================================================
STRICT SCIENTIFIC BOUNDARIES
======================================================================

Do NOT treat any of the following as novel contributions:

- NiTi material substitution by itself;
- wire/fiber jamming by itself;
- positive-pressure jamming by itself;
- SMA plus jamming in the same device;
- NiTi wire-rope friction/contact/hysteresis by itself;
- NiTi phase transformation plus inter-wire friction by itself;
- passive helix/contact pressure;
- manufacturing preload;
- fixed radial preload;
- generic damping or seismic-device behavior.

The remaining candidate contribution, if it survives, must be substantially
narrower:

actively varied radial/transverse confinement pressure as an independent
variable applied to a NiTi wire bundle under bending, with pressure-dependent
normal contact, stick/partial-slip/full-slip transitions, transformation
distribution, hysteresis and tangent/effective bending stiffness.

======================================================================
PARAMETER-SUBSTITUTION / MODEL-DISCRIMINATION RULE
======================================================================

The supplied interim audit may establish that a constant elastic modulus plus
friction-coefficient substitution is inadequate for transformation-active NiTi.

Do NOT convert that into a claim that a brand-new constitutive model is
automatically required.

The proposed MSc study must compare at least:

1. an established elastic-wire/fiber pressure/contact baseline; and
2. an established transformation-aware NiTi constitutive/contact formulation.

The contribution survives scientifically only if controlled pressure/curvature
data reveal a material, measurable discrepancy that cannot be explained by
ordinary calibrated effective parameters within the declared operating domain.

======================================================================
TOPIC-LOCK RULE
======================================================================

D1/M1 is still preserved as an alternative direction.

This V002 adjudication evaluates whether MP1 is internally ready to ADVANCE,
not whether MP1 automatically defeats D1/M1.

Therefore:
- if MP1 survives with a concrete falsifiable mechanics question, set
  requires_cross_direction_comparison_with_d1_m1=true;
- do not claim the MSc topic is finally locked until that comparison is done;
- if MP1 is falsified, recommend dropping MP1 and retaining the preserved
  alternative;
- if evidence is inconclusive, do not invent another broad search.

======================================================================
TITLE RULE
======================================================================

Provide a conservative working title in English and Vietnamese only if the
direction remains viable.

Avoid "novel", "first", "unprecedented", or claims that active-pressure NiTi
mechanics has been universally proven absent from literature.

Prefer terms such as:
- modeling;
- experimental characterization;
- pressure-controlled;
- bending mechanics;
- stick-slip;
- superelastic NiTi wire bundle.

======================================================================
ASTRA ESCALATION
======================================================================

Astra is expensive.

Set astra_escalation_required=true only if:
- the final protocol outcome remains genuinely ambiguous;
- a fatal logical contradiction exists between full-text evidence and coverage;
- or MP1 vs the preserved D1/M1 cannot later be compared without an additional
  high-cost scientific critique.

Do NOT request Astra for drafting, formatting, summarization, or routine
literature work.

======================================================================
OUTPUT DISCIPLINE
======================================================================

Return ONLY one JSON object matching the supplied schema.

SOURCE BUNDLE
{bundle}
""".strip()


def validate_result(
    result: dict[str, Any],
    coverage: dict[str, Any],
) -> None:
    missing = set(SCHEMA["required"]) - set(result)
    if missing:
        raise RuntimeError(
            "Missing output keys: " + ", ".join(sorted(missing))
        )

    stop = coverage["stop_condition"]
    if not result["citation_coverage_closed"]:
        raise RuntimeError(
            "Final adjudication must acknowledge closed citation coverage."
        )
    if not stop["satisfied"]:
        raise RuntimeError(
            "Coverage source contradicts final adjudication."
        )

    outcome = result["protocol_outcome"]
    if outcome == "FALSIFIED" and not result["direct_kill_found"]:
        raise RuntimeError(
            "FALSIFIED requires direct_kill_found=true."
        )

    if outcome == "SURVIVES_TARGETED_CITATION_CHASE":
        if result["direct_kill_found"]:
            raise RuntimeError(
                "SURVIVES_TARGETED_CITATION_CHASE conflicts with a direct kill."
            )
        if not result["requires_cross_direction_comparison_with_d1_m1"]:
            raise RuntimeError(
                "A surviving MP1 must still be compared with preserved D1/M1."
            )

    if result["msc_topic_readiness"] == "DROP_MP1" and outcome == "SURVIVES_TARGETED_CITATION_CHASE":
        raise RuntimeError(
            "DROP_MP1 conflicts with SURVIVES_TARGETED_CITATION_CHASE."
        )


def render_md(
    result: dict[str, Any],
    sources: list[dict[str, Any]],
    bundle_sha: str,
) -> str:
    lines = [
        "# MP1-V002 Final Adjudication",
        "",
        f"- **Protocol outcome:** {result['protocol_outcome']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Citation coverage closed:** {result['citation_coverage_closed']}",
        f"- **Direct kill found:** {result['direct_kill_found']}",
        f"- **MSc topic readiness:** {result['msc_topic_readiness']}",
        f"- **Bundle SHA256:** {bundle_sha}",
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## Surviving contribution",
        "",
        result["surviving_contribution"],
        "",
        "## What is not novel",
        "",
    ]
    lines += [f"- {x}" for x in result["what_is_not_novel"]] or ["- None."]
    lines += [
        "",
        "## What remains unestablished",
        "",
    ]
    lines += [f"- {x}" for x in result["what_remains_unestablished"]] or ["- None."]
    lines += [
        "",
        "## Final research question",
        "",
        result["final_research_question"],
        "",
        "## Scientific hypothesis",
        "",
        result["scientific_hypothesis"],
        "",
        "## Model-discrimination plan",
        "",
    ]
    for k, v in result["model_discrimination_plan"].items():
        lines.append(f"- **{k}:** {v}")
    lines += [
        "",
        "## Experimental scope",
        "",
    ]
    for k, v in result["experimental_scope"].items():
        lines.append(f"### {k}")
        lines.append("")
        if isinstance(v, list):
            lines += [f"- {x}" for x in v] or ["- None."]
        else:
            lines.append(str(v))
        lines.append("")
    lines += [
        "## Topic-lock rationale",
        "",
        result["topic_lock_rationale"],
        "",
        "## Working title",
        "",
        f"**English:** {result['title_draft_en']}",
        "",
        f"**Vietnamese:** {result['title_draft_vi']}",
        "",
        "## Remaining pre-execution checks",
        "",
    ]
    lines += [f"- {x}" for x in result["remaining_pre_execution_checks"]] or ["- None."]
    lines += [
        "",
        "## Astra escalation",
        "",
        f"- **Required:** {result['astra_escalation_required']}",
        f"- **Reason:** {result['astra_escalation_reason']}",
        "",
        "## Recommended next action",
        "",
        result["recommended_next_action"],
        "",
        "## Provenance",
        "",
    ]
    lines += [
        f"- {x['role']} — {x['path']} — SHA256 {x['sha256']}"
        for x in sources
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Final MP1-V002 protocol adjudication."
    )
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--model",
        default=os.getenv("CODEX_RESEARCH_MODEL", "").strip(),
    )
    parser.add_argument(
        "--effort",
        default=os.getenv("CODEX_RESEARCH_EFFORT", "high").strip(),
        choices=["low", "medium", "high", "xhigh"],
    )
    args = parser.parse_args()

    matrix, audit, coverage = validate_inputs()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    sources = [
        meta(PROTOCOL, "V002_PROTOCOL"),
        meta(PROJECT_STATE, "MP1_PROJECT_STATE"),
        meta(V001, "V001_BASELINE_AUDIT"),
        meta(MATRIX, "V002_16_PAPER_FULL_TEXT_MATRIX"),
        meta(INTERIM_AUDIT, "V002_INTERIM_TARGETED_THREAT_AUDIT"),
        meta(COVERAGE, "V002_CITATION_COVERAGE_CLOSURE"),
    ]

    bundle_sha = sha256_bytes(
        "\n".join(
            f"{x['path']}:{x['sha256']}"
            for x in sources
        ).encode("utf-8")
    )

    run_id = timestamp_id()
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    schema_path = run_dir / "output_schema.json"
    manifest_path = run_dir / "source_manifest.json"
    prompt_path = run_dir / "prompt.txt"
    raw_path = run_dir / "raw_model_output.json"
    result_json = run_dir / "FINAL_ADJUDICATION.json"
    result_md = run_dir / "FINAL_ADJUDICATION.md"

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
                "paper_count": matrix["paper_count"],
                "interim_status": audit.get("status"),
                "citation_stop_condition": coverage["stop_condition"],
                "bundle_sha256": bundle_sha,
                "sources": sources,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    prompt = build_prompt(sources)
    prompt_path.write_text(prompt + "\n", encoding="utf-8")

    print(f"[VERIFICATION] {VERIFICATION_ID}")
    print(f"[PAPERS] {matrix['paper_count']}")
    print("[CITATION COVERAGE] SATISFIED")
    print(f"[RUN] {run_id}")
    print(f"[BUNDLE SHA256] {bundle_sha}")

    if args.prepare_only:
        print("[PREPARE ONLY] PASS")
        return

    if not args.model:
        raise RuntimeError(
            "CODEX_RESEARCH_MODEL is empty. Source .env or pass --model."
        )

    if CANONICAL_JSON.exists() and not args.force:
        raise RuntimeError(
            f"Canonical output already exists: {CANONICAL_JSON}. "
            "Use --force only intentionally."
        )

    run_codex(
        prompt=prompt,
        schema_path=schema_path,
        raw_output_path=raw_path,
        model=args.model,
        effort=args.effort,
    )

    try:
        result = json.loads(read_text(raw_path).strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError("Model output is not valid JSON.") from exc

    if not isinstance(result, dict):
        raise RuntimeError("Model output must be a JSON object.")

    validate_result(result, coverage)

    result["_provenance"] = {
        "run_id": run_id,
        "created_at_utc": utc_now().isoformat(),
        "verification_id": VERIFICATION_ID,
        "paper_count": matrix["paper_count"],
        "evidence_bundle_sha256": bundle_sha,
        "model": args.model,
        "effort": args.effort,
        "final_v002_verdict": True,
    }

    result_json.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    result_md.write_text(
        render_md(result, sources, bundle_sha),
        encoding="utf-8",
    )

    shutil.copy2(result_json, CANONICAL_JSON)
    shutil.copy2(result_md, CANONICAL_MD)
    shutil.copy2(raw_path, CANONICAL_RAW)

    print(f"[OUTCOME] {result['protocol_outcome']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(f"[TOPIC READINESS] {result['msc_topic_readiness']}")
    print(
        "[CROSS-DIRECTION COMPARISON] "
        + str(result["requires_cross_direction_comparison_with_d1_m1"])
    )
    print(f"[ASTRA REQUIRED] {result['astra_escalation_required']}")
    print(f"[SAVED] {CANONICAL_JSON.relative_to(ROOT)}")
    print(f"[SAVED] {CANONICAL_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
