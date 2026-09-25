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
OUT_DIR = ROOT / "outputs" / "final_direction_lock"
RUNS_DIR = OUT_DIR / "runs"

D1_HANDOFF = ROOT / "docs" / "project" / "PROJECT_HANDOFF_CURRENT.md"
D1_V008 = ROOT / "outputs" / "verification" / "D1-V008" / "FINAL_NAMED_TARGET_AUDIT.json"
D1_V009 = ROOT / "outputs" / "verification" / "D1-V009" / "LATE_FOUND_ADJACENT_AUDIT.json"
D1_ARCH = ROOT / "docs" / "research_design" / "M1_RESEARCH_ARCHITECTURE_VI.md"

MP1_FINAL = ROOT / "outputs" / "verification" / "MP1-V002" / "FINAL_ADJUDICATION.json"
MP1_COVERAGE = ROOT / "outputs" / "verification" / "MP1-V002" / "citation_coverage.json"

CANONICAL_JSON = OUT_DIR / "FINAL_DIRECTION_ADJUDICATION.json"
CANONICAL_MD = OUT_DIR / "FINAL_DIRECTION_ADJUDICATION.md"
CANONICAL_RAW = OUT_DIR / "FINAL_DIRECTION_ADJUDICATION_raw.json"

SELECTION = ["D1_M1", "MP1", "INSUFFICIENT_CONFIDENCE"]

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "selected_direction",
        "decision",
        "confidence",
        "executive_summary",
        "d1_m1_assessment",
        "mp1_assessment",
        "direct_comparison",
        "fatal_risks",
        "selection_rationale",
        "final_title_en",
        "final_title_vi",
        "final_research_question",
        "scientific_hypothesis",
        "immediate_next_gate",
        "astra_escalation_required",
        "astra_escalation_reason",
    ],
    "properties": {
        "selected_direction": {
            "type": "string",
            "enum": SELECTION,
        },
        "decision": {
            "type": "string",
            "enum": [
                "LOCK_DIRECTION",
                "LOCK_WITH_FEASIBILITY_GATE",
                "INSUFFICIENT_CONFIDENCE",
            ],
        },
        "confidence": {
            "type": "string",
            "enum": ["low", "medium", "high"],
        },
        "executive_summary": {"type": "string"},
        "d1_m1_assessment": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "scientific_question",
                "novelty_position",
                "modeling_readiness",
                "experimental_readiness",
                "identifiability",
                "execution_risk",
                "publication_logic",
                "remaining_unknowns",
            ],
            "properties": {
                "scientific_question": {"type": "string"},
                "novelty_position": {"type": "string"},
                "modeling_readiness": {"type": "string"},
                "experimental_readiness": {"type": "string"},
                "identifiability": {"type": "string"},
                "execution_risk": {"type": "string"},
                "publication_logic": {"type": "string"},
                "remaining_unknowns": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        },
        "mp1_assessment": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "scientific_question",
                "novelty_position",
                "modeling_readiness",
                "experimental_readiness",
                "identifiability",
                "execution_risk",
                "publication_logic",
                "remaining_unknowns",
            ],
            "properties": {
                "scientific_question": {"type": "string"},
                "novelty_position": {"type": "string"},
                "modeling_readiness": {"type": "string"},
                "experimental_readiness": {"type": "string"},
                "identifiability": {"type": "string"},
                "execution_risk": {"type": "string"},
                "publication_logic": {"type": "string"},
                "remaining_unknowns": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        },
        "direct_comparison": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "criterion",
                    "d1_m1",
                    "mp1",
                    "decision_relevance",
                ],
                "properties": {
                    "criterion": {"type": "string"},
                    "d1_m1": {"type": "string"},
                    "mp1": {"type": "string"},
                    "decision_relevance": {"type": "string"},
                },
            },
        },
        "fatal_risks": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "direction",
                    "risk",
                    "kill_or_pivot_condition",
                ],
                "properties": {
                    "direction": {
                        "type": "string",
                        "enum": ["D1_M1", "MP1"],
                    },
                    "risk": {"type": "string"},
                    "kill_or_pivot_condition": {"type": "string"},
                },
            },
        },
        "selection_rationale": {"type": "string"},
        "final_title_en": {"type": "string"},
        "final_title_vi": {"type": "string"},
        "final_research_question": {"type": "string"},
        "scientific_hypothesis": {"type": "string"},
        "immediate_next_gate": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "name",
                "objective",
                "pass_condition",
                "fail_condition",
                "required_outputs",
            ],
            "properties": {
                "name": {"type": "string"},
                "objective": {"type": "string"},
                "pass_condition": {"type": "string"},
                "fail_condition": {"type": "string"},
                "required_outputs": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        },
        "astra_escalation_required": {"type": "boolean"},
        "astra_escalation_reason": {"type": "string"},
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


def validate_inputs() -> None:
    required = [
        D1_HANDOFF,
        D1_V008,
        D1_V009,
        D1_ARCH,
        MP1_FINAL,
        MP1_COVERAGE,
    ]
    for path in required:
        if not path.exists():
            raise RuntimeError(f"Required input not found: {path}")

    d1_v008 = load_json(D1_V008)
    d1_v009 = load_json(D1_V009)
    mp1 = load_json(MP1_FINAL)
    coverage = load_json(MP1_COVERAGE)

    if not d1_v008.get("stop_search_decision", {}).get("final_novelty_lock_allowed"):
        raise RuntimeError("D1/M1 does not have final novelty-lock permission.")

    if not d1_v009.get("lock_decision", {}).get("final_novelty_lock_survives"):
        raise RuntimeError("D1-V009 does not preserve the D1/M1 novelty lock.")

    if mp1.get("protocol_outcome") != "SURVIVES_TARGETED_CITATION_CHASE":
        raise RuntimeError(
            "MP1 is not ready for cross-direction comparison: "
            f"{mp1.get('protocol_outcome')!r}"
        )

    if not mp1.get("requires_cross_direction_comparison_with_d1_m1"):
        raise RuntimeError("MP1 final adjudication did not request cross-direction comparison.")

    if not coverage.get("stop_condition", {}).get("satisfied"):
        raise RuntimeError("MP1 citation coverage is not closed.")


def build_prompt(sources: list[dict[str, Any]]) -> str:
    ordered = [
        D1_HANDOFF,
        D1_V008,
        D1_V009,
        D1_ARCH,
        MP1_FINAL,
        MP1_COVERAGE,
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
You are the FINAL CROSS-DIRECTION SCIENTIFIC ADJUDICATOR for a Mechanical
Engineering MSc research project.

Two directions have independently survived adversarial novelty/falsification
workflows. Your job is to select which direction should become the MSc thesis
direction, or declare insufficient confidence.

This is a DECISION task, not a literature-summary task.

Use ONLY the supplied repository sources for scientific claims.

======================================================================
DIRECTION A — D1/M1
======================================================================

Current object:
quantitative validity / breakdown assessment of one specified continuum
vacuum-layer-jamming beam model (Zhang et al. M1) against a higher-fidelity
full-layer frictional-contact reference and physical experiments.

The novelty position is NOT invention of continuum mechanics, layer-jamming
mechanics, frictional slip, Cosserat theory, or FE contact.

The surviving contribution is the quantitative, output-specific validity /
breakdown framework with predeclared tolerances and deliberate experiment
sampling on both sides of the predicted boundary.

D1/M1 has passed D1-V008 final named-target closure and D1-V009 late-found
adjacent threat audit.

======================================================================
DIRECTION B — MP1
======================================================================

Current object:
pressure-controlled bending mechanics of a superelastic NiTi wire bundle.

The novelty position is NOT NiTi substitution, wire jamming, SMA+jamming,
NiTi inter-wire friction, NiTi hysteresis, or passive cable contact.

The surviving contribution is model discrimination and experimental
characterization under independently varied radial/transverse confinement
pressure, with stick/partial-slip/full-slip transitions and possible
transformation-mediated effects.

MP1-V002 citation coverage is closed and the final outcome is
SURVIVES_TARGETED_CITATION_CHASE.

======================================================================
DECISION CRITERIA
======================================================================

Compare the directions on:

1. clarity of the scientific question;
2. maturity of the novelty/falsification lock;
3. existence of a concrete baseline model;
4. existence of a concrete higher-fidelity/reference model;
5. ability to define independent and dependent variables cleanly;
6. parameter identifiability;
7. experimental measurability;
8. experimental apparatus complexity;
9. likelihood of reaching the critical physical regime;
10. model-discrimination strength;
11. risk of collapsing into parameter fitting;
12. risk of a negative result becoming scientifically weak;
13. MSc time and implementation burden;
14. reproducibility;
15. publication logic for a WoS/Scopus journal;
16. dependence on specialized instrumentation or difficult material state control;
17. degree to which a null/negative result remains publishable;
18. remaining fatal unknowns.

Do NOT select a direction because it appears more fashionable or more novel.

Do NOT reward complexity by itself.

Prefer the direction that best balances:
scientific defensibility
+ falsifiability
+ execution feasibility
+ interpretable negative results
+ publication potential.

======================================================================
SPECIAL GUARDRAILS
======================================================================

For D1/M1:
- do not treat predeclared tolerance alone as scientific novelty;
- judge whether the validity/breakdown map plus physical explanation and
  experiment constitute a coherent mechanics contribution;
- account for the fact that exact R, outputs, tolerances and experiment are
  not yet fully frozen.

For MP1:
- active pressure is an experimental control protocol, not automatically a
  new mechanics law;
- H0b (existing transformation-aware NiTi constitutive + Coulomb contact)
  remains plausible;
- a distinct coupling contribution is killed if H0b predicts the data within
  the declared domain;
- judge the practical risk that slip and stress-induced transformation do not
  coexist in an accessible bending/pressure domain;
- judge the measurement burden for phase/transformation and inter-wire slip.

======================================================================
DECISION OUTPUT
======================================================================

selected_direction must be:
- D1_M1
- MP1
- INSUFFICIENT_CONFIDENCE

If one direction is clearly better for MSc execution, use LOCK_DIRECTION.

If a direction is preferred but must pass one concrete feasibility test before
irreversible commitment, use LOCK_WITH_FEASIBILITY_GATE and define exactly
one immediate gate.

If evidence cannot support a defensible choice, use INSUFFICIENT_CONFIDENCE.

The final title, research question and hypothesis must correspond to the
selected direction. If insufficient confidence, leave them conservative and
state what must be resolved.

======================================================================
ASTRA RULE
======================================================================

Astra is expensive.

Request Astra only if the supplied evidence leaves a genuine close scientific
tradeoff or contradiction that GPT-6 Sol cannot defensibly resolve.

Do not request Astra for drafting, formatting, literature extraction, or
routine planning.

Return ONLY one JSON object matching the supplied schema.

SOURCE BUNDLE
{bundle}
""".strip()


def validate_result(result: dict[str, Any]) -> None:
    missing = set(SCHEMA["required"]) - set(result)
    if missing:
        raise RuntimeError("Missing output keys: " + ", ".join(sorted(missing)))

    selected = result["selected_direction"]
    decision = result["decision"]

    if selected == "INSUFFICIENT_CONFIDENCE":
        if decision != "INSUFFICIENT_CONFIDENCE":
            raise RuntimeError(
                "INSUFFICIENT_CONFIDENCE selection requires matching decision."
            )
    elif decision == "INSUFFICIENT_CONFIDENCE":
        raise RuntimeError(
            "A concrete selected direction cannot use INSUFFICIENT_CONFIDENCE decision."
        )

    if result["confidence"] == "low" and not result["astra_escalation_required"]:
        raise RuntimeError(
            "Low-confidence final direction decision must request Astra escalation."
        )


def render_md(
    result: dict[str, Any],
    sources: list[dict[str, Any]],
    bundle_sha: str,
) -> str:
    lines = [
        "# Final Cross-Direction MSc Adjudication",
        "",
        f"- **Selected direction:** {result['selected_direction']}",
        f"- **Decision:** {result['decision']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Astra escalation:** {result['astra_escalation_required']}",
        f"- **Bundle SHA256:** {bundle_sha}",
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## D1/M1 assessment",
        "",
    ]
    for k, v in result["d1_m1_assessment"].items():
        if isinstance(v, list):
            lines.append(f"### {k}")
            lines += [f"- {x}" for x in v] or ["- None."]
        else:
            lines.append(f"- **{k}:** {v}")
    lines += ["", "## MP1 assessment", ""]
    for k, v in result["mp1_assessment"].items():
        if isinstance(v, list):
            lines.append(f"### {k}")
            lines += [f"- {x}" for x in v] or ["- None."]
        else:
            lines.append(f"- **{k}:** {v}")

    lines += ["", "## Direct comparison", ""]
    lines += [
        "| Criterion | D1/M1 | MP1 | Decision relevance |",
        "|---|---|---|---|",
    ]
    for x in result["direct_comparison"]:
        lines.append(
            f"| {x['criterion']} | {x['d1_m1']} | {x['mp1']} | "
            f"{x['decision_relevance']} |"
        )

    lines += ["", "## Fatal risks", ""]
    for x in result["fatal_risks"]:
        lines += [
            f"### {x['direction']}",
            f"- **Risk:** {x['risk']}",
            f"- **Kill/pivot condition:** {x['kill_or_pivot_condition']}",
            "",
        ]

    lines += [
        "## Selection rationale",
        "",
        result["selection_rationale"],
        "",
        "## Final working title",
        "",
        f"**English:** {result['final_title_en']}",
        "",
        f"**Vietnamese:** {result['final_title_vi']}",
        "",
        "## Final research question",
        "",
        result["final_research_question"],
        "",
        "## Scientific hypothesis",
        "",
        result["scientific_hypothesis"],
        "",
        "## Immediate next gate",
        "",
    ]
    for k, v in result["immediate_next_gate"].items():
        if isinstance(v, list):
            lines.append(f"### {k}")
            lines += [f"- {x}" for x in v] or ["- None."]
        else:
            lines.append(f"- **{k}:** {v}")

    lines += [
        "",
        "## Astra escalation",
        "",
        f"- **Required:** {result['astra_escalation_required']}",
        f"- **Reason:** {result['astra_escalation_reason']}",
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
        description="Final D1/M1 vs MP1 MSc direction adjudication."
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

    validate_inputs()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    sources = [
        meta(D1_HANDOFF, "D1_CURRENT_HANDOFF"),
        meta(D1_V008, "D1_FINAL_NAMED_TARGET_AUDIT"),
        meta(D1_V009, "D1_LATE_FOUND_TARGET_AUDIT"),
        meta(D1_ARCH, "D1_M1_RESEARCH_ARCHITECTURE"),
        meta(MP1_FINAL, "MP1_FINAL_ADJUDICATION"),
        meta(MP1_COVERAGE, "MP1_CITATION_COVERAGE_CLOSURE"),
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
    result_json = run_dir / "FINAL_DIRECTION_ADJUDICATION.json"
    result_md = run_dir / "FINAL_DIRECTION_ADJUDICATION.md"

    schema_path.write_text(
        json.dumps(SCHEMA, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest_path.write_text(
        json.dumps(
            {
                "run_id": run_id,
                "created_at_utc": utc_now().isoformat(),
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

    print("[FINAL CROSS-DIRECTION ADJUDICATION]")
    print("[D1/M1] novelty lock survived D1-V009")
    print("[MP1] V002 targeted citation chase survived")
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

    validate_result(result)

    result["_provenance"] = {
        "run_id": run_id,
        "created_at_utc": utc_now().isoformat(),
        "evidence_bundle_sha256": bundle_sha,
        "model": args.model,
        "effort": args.effort,
        "final_direction_lock_run": True,
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

    print(f"[SELECTED] {result['selected_direction']}")
    print(f"[DECISION] {result['decision']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(f"[ASTRA REQUIRED] {result['astra_escalation_required']}")
    print(f"[SAVED] {CANONICAL_JSON.relative_to(ROOT)}")
    print(f"[SAVED] {CANONICAL_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
