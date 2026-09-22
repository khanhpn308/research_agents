from __future__ import annotations

import argparse
import json
import os
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

VERIFICATION_ID = "MP1-V001"
MIN_PAPERS = 8

OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
RUNS_DIR = OUT_DIR / "core_prior_art_runs"
CURRENT_MATRIX = OUT_DIR / "verification_matrix.json"
PLAN_PATH = ROOT / "docs" / "protocols" / "MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md"

CANONICAL_JSON = OUT_DIR / "CORE_PRIOR_ART_AUDIT.json"
CANONICAL_MD = OUT_DIR / "CORE_PRIOR_ART_AUDIT.md"
CANONICAL_RAW = OUT_DIR / "CORE_PRIOR_ART_AUDIT_raw.json"

STATUS_ENUM = [
    "KILL_MP1",
    "PIVOT_TO_MECHANICS_CORE",
    "SURVIVES_CORE_CORPUS",
    "INCONCLUSIVE",
]

CLAIM_STATUS_ENUM = [
    "closed",
    "substantially_preempted",
    "open_in_supplied_corpus",
    "uncertain",
]

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "candidate_architecture",
        "executive_summary",
        "claim_audit",
        "closest_prior_art",
        "fatal_conflicts",
        "remaining_mechanics_core",
        "implementation_only_risk",
        "targeted_followup",
        "recommended_next_action",
    ],
    "properties": {
        "status": {"type": "string", "enum": STATUS_ENUM},
        "confidence": {
            "type": "string",
            "enum": ["low", "medium", "high"],
        },
        "candidate_architecture": {"type": "string"},
        "executive_summary": {"type": "string"},
        "claim_audit": {
            "type": "array",
            "minItems": 8,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "claim_id",
                    "claim",
                    "status",
                    "assessment",
                    "evidence_paper_ids",
                ],
                "properties": {
                    "claim_id": {"type": "string"},
                    "claim": {"type": "string"},
                    "status": {
                        "type": "string",
                        "enum": CLAIM_STATUS_ENUM,
                    },
                    "assessment": {"type": "string"},
                    "evidence_paper_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
            },
        },
        "closest_prior_art": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "paper_id",
                    "title",
                    "doi",
                    "overlap",
                    "critical_difference",
                    "threat_level",
                ],
                "properties": {
                    "paper_id": {"type": "string"},
                    "title": {"type": "string"},
                    "doi": {"type": "string"},
                    "overlap": {"type": "string"},
                    "critical_difference": {"type": "string"},
                    "threat_level": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "fatal"],
                    },
                },
            },
        },
        "fatal_conflicts": {
            "type": "array",
            "items": {"type": "string"},
        },
        "remaining_mechanics_core": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "niti_as_jamming_medium",
                "positive_pressure_niti_bundle",
                "coupled_superelastic_friction_mechanics",
                "scientifically_defensible",
                "assessment",
            ],
            "properties": {
                "niti_as_jamming_medium": {"type": "boolean"},
                "positive_pressure_niti_bundle": {"type": "boolean"},
                "coupled_superelastic_friction_mechanics": {"type": "boolean"},
                "scientifically_defensible": {"type": "boolean"},
                "assessment": {"type": "string"},
            },
        },
        "implementation_only_risk": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "sma_syringe_only_difference",
                "risk_level",
                "assessment",
            ],
            "properties": {
                "sma_syringe_only_difference": {"type": "boolean"},
                "risk_level": {
                    "type": "string",
                    "enum": ["low", "medium", "high"],
                },
                "assessment": {"type": "string"},
            },
        },
        "targeted_followup": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "required",
                "targets",
                "named_sources",
                "reopen_broad_search",
            ],
            "properties": {
                "required": {"type": "boolean"},
                "targets": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "named_sources": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "reopen_broad_search": {"type": "boolean"},
            },
        },
        "recommended_next_action": {"type": "string"},
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def source_metadata(path: Path, role: str) -> dict[str, Any]:
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
        "role": role,
    }


def build_prompt(matrix_path: Path, source_meta: list[dict[str, Any]]) -> str:
    bundle_parts: list[str] = []

    for path in [PLAN_PATH, matrix_path]:
        rel = str(path.relative_to(ROOT))
        meta = next(item for item in source_meta if item["path"] == rel)
        bundle_parts.extend(
            [
                "=" * 100,
                f"SOURCE: {rel}",
                f"SHA256: {meta['sha256']}",
                f"ROLE: {meta['role']}",
                "=" * 100,
                read_text(path),
                "",
            ]
        )

    bundle = "\n".join(bundle_parts)

    return f"""
You are performing MP1-V001, an adversarial CORE PRIOR-ART audit for a
mentor-proposed MSc research direction.

This is a falsification task. Do not defend the candidate.

Use ONLY the supplied source bundle for scientific claims. The verification
matrix contains evidence extracted from locally held full-text PDFs.

CANDIDATE ARCHITECTURE

superelastic NiTi / metal wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional compact SMA-driven syringe/piston pressure source

AUDIT EXACTLY THESE CLAIMS

C1 Wire/fiber jamming for variable stiffness is novel.
C2 Positive-pressure jamming for variable stiffness is novel.
C3 SMA and jamming in the same variable-stiffness device is novel.
C4 An onboard/compact pressure source for jamming is novel.
C5 Superelastic NiTi wires themselves as the frictional jamming medium remain open.
C6 Positive-pressure confinement of a superelastic NiTi wire bundle remains open.
C7 Coupling among NiTi superelastic response, inter-wire slip/friction,
   pressure and bending stiffness remains open.
C8 SMA-driven syringe/piston specifically powering jamming pressure remains open.

STRICT DISTINCTIONS

- NiTi wires present in a jamming robot does NOT prove NiTi wires are the
  jamming medium.
- NiTi tendons/backbones around granular jamming are NOT NiTi wire jamming.
- Mechanical axial piston compression of particles is NOT automatically
  positive fluid-pressure confinement of a wire bundle.
- Existence of SMA pumps means an SMA-driven syringe may be only an actuator
  substitution unless the supplied evidence supports a new mechanics question.
- Material substitution alone is not sufficient scientific novelty.
- Absence in this corpus is NOT proof of universal novelty.

STATUS RULES

KILL_MP1:
The supplied corpus directly/substantially closes the core C5-C7 mechanics,
or leaves only implementation substitution without a defensible scientific
mechanics question.

PIVOT_TO_MECHANICS_CORE:
The broad architecture is heavily pre-empted, but a narrower C5-C7 mechanics
question remains defensible and requires targeted citation chasing.

SURVIVES_CORE_CORPUS:
No fatal prior art is established for C5-C7 in the supplied corpus. This still
does not prove novelty; targeted citation chasing is required.

INCONCLUSIVE:
Evidence extraction or corpus coverage is insufficient to decide.

SEARCH RULE

Do not recommend broad searching. If follow-up is needed, specify only targeted
backward/forward citation chasing for T1/T2/T3 and identify named anchors when
supported by the supplied corpus.

SOURCE BUNDLE

{bundle}
""".strip()


def validate_result(result: dict[str, Any]) -> None:
    missing = set(SCHEMA["required"]) - set(result)
    if missing:
        raise RuntimeError(
            "Model output missing required keys: "
            + ", ".join(sorted(missing))
        )

    claims = {item.get("claim_id"): item for item in result["claim_audit"]}
    expected = {f"C{i}" for i in range(1, 9)}
    if set(claims) != expected:
        raise RuntimeError(
            "claim_audit must contain exactly C1..C8; got "
            + ", ".join(sorted(str(x) for x in claims))
        )

    if result["status"] == "KILL_MP1":
        core = result["remaining_mechanics_core"]
        if core["scientifically_defensible"]:
            raise RuntimeError(
                "KILL_MP1 cannot coexist with a scientifically defensible "
                "remaining mechanics core."
            )


def render_markdown(
    result: dict[str, Any],
    manifest: list[dict[str, Any]],
    bundle_sha256: str,
) -> str:
    lines = [
        "# MP1-V001 Core Prior-Art Audit",
        "",
        f"- **Status:** {result['status']}",
        f"- **Confidence:** {result['confidence']}",
        f"- **Bundle SHA256:** {bundle_sha256}",
        "",
        "## Candidate architecture",
        "",
        result["candidate_architecture"],
        "",
        "## Executive summary",
        "",
        result["executive_summary"],
        "",
        "## Claim audit",
        "",
    ]

    for item in result["claim_audit"]:
        lines.extend(
            [
                f"### {item['claim_id']} — {item['status']}",
                "",
                f"**Claim:** {item['claim']}",
                "",
                item["assessment"],
                "",
                "**Evidence paper_ids:** "
                + (", ".join(item["evidence_paper_ids"]) or "none"),
                "",
            ]
        )

    lines.extend(["## Closest prior art", ""])
    for item in result["closest_prior_art"]:
        lines.extend(
            [
                f"### {item['title']}",
                "",
                f"- paper_id: {item['paper_id']}",
                f"- DOI: {item['doi']}",
                f"- Threat: {item['threat_level']}",
                f"- Overlap: {item['overlap']}",
                f"- Critical difference: {item['critical_difference']}",
                "",
            ]
        )

    lines.extend(["## Fatal conflicts", ""])
    if result["fatal_conflicts"]:
        for item in result["fatal_conflicts"]:
            lines.append(f"- {item}")
    else:
        lines.append("- None established in the supplied corpus.")

    core = result["remaining_mechanics_core"]
    lines.extend(["", "## Remaining mechanics core", ""])
    for key, value in core.items():
        lines.append(f"- **{key}:** {value}")

    risk = result["implementation_only_risk"]
    lines.extend(["", "## Implementation-only novelty risk", ""])
    for key, value in risk.items():
        lines.append(f"- **{key}:** {value}")

    follow = result["targeted_followup"]
    lines.extend(["", "## Targeted follow-up", ""])
    for key, value in follow.items():
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
        description="MP1-V001 core prior-art adversarial audit."
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

    for required in [CURRENT_MATRIX, PLAN_PATH]:
        if not required.exists():
            raise RuntimeError(f"Required input not found: {required}")

    matrix = load_json(CURRENT_MATRIX)
    if matrix.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("Verification matrix ID mismatch.")

    paper_count = int(matrix.get("paper_count", 0))
    if paper_count < MIN_PAPERS:
        raise RuntimeError(
            f"{VERIFICATION_ID} requires at least {MIN_PAPERS} included, "
            f"ingested papers; found {paper_count}."
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    source_meta = [
        source_metadata(PLAN_PATH, "AUDIT_PROTOCOL"),
        source_metadata(CURRENT_MATRIX, "FULL_TEXT_EVIDENCE_MATRIX"),
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
    result_json_path = run_dir / "CORE_PRIOR_ART_AUDIT.json"
    result_md_path = run_dir / "CORE_PRIOR_ART_AUDIT.md"

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
                "paper_count": paper_count,
                "bundle_sha256": bundle_sha256,
                "sources": source_meta,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    prompt = build_prompt(CURRENT_MATRIX, source_meta)
    prompt_path.write_text(prompt + "\n", encoding="utf-8")

    print(f"[VERIFICATION] {VERIFICATION_ID}")
    print(f"[PAPERS] {paper_count}")
    print(f"[RUN] {run_id}")
    print(f"[BUNDLE SHA256] {bundle_sha256}")
    print(f"[PROMPT] {prompt_path.relative_to(ROOT)}")

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
            "Use --force only for an intentional replacement."
        )

    model_result = run_codex(
        prompt=prompt,
        schema=SCHEMA,
        model=args.model,
        reasoning_effort=args.effort,
    )

    raw_path.write_text(
        json.dumps(model_result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    result = model_result.get("content")
    if isinstance(result, str):
        result = json.loads(result)
    if not isinstance(result, dict):
        raise RuntimeError("Codex result content is not a JSON object.")

    validate_result(result)

    result_json_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    result_md_path.write_text(
        render_markdown(result, source_meta, bundle_sha256),
        encoding="utf-8",
    )

    CANONICAL_JSON.write_text(
        result_json_path.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    CANONICAL_MD.write_text(
        result_md_path.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    CANONICAL_RAW.write_text(
        raw_path.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    print(f"[STATUS] {result['status']}")
    print(f"[CONFIDENCE] {result['confidence']}")
    print(f"[SAVED] {CANONICAL_JSON.relative_to(ROOT)}")
    print(f"[SAVED] {CANONICAL_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
