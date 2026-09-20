from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]

OUT_DIR = ROOT / "outputs" / "verification" / "D1-V003"

RUNS_DIR = OUT_DIR / "cross_round_runs"

CANONICAL_JSON = OUT_DIR / "cross_round_adversarial_synthesis.json"
CANONICAL_MD = OUT_DIR / "cross_round_adversarial_synthesis.md"
CANONICAL_RAW = OUT_DIR / "cross_round_adversarial_synthesis_raw.json"

CURRENT_MATRIX = (
    OUT_DIR / "verification_matrix.json"
)


# ---------------------------------------------------------------------
# INPUT SOURCES
# ---------------------------------------------------------------------

CORE_INPUTS = [
    ROOT
    / "outputs"
    / "verification"
    / "D1-V001"
    / "direction_verification.json",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V001"
    / "verification_matrix.json",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V002"
    / "verification_matrix.json",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V002"
    / "adversarial_evidence_synthesis.md",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "verification_matrix.json",
]


OPTIONAL_INPUTS = [
    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "FAN_2026_MODEL_AUDIT.md",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "D1-V003_EVIDENCE_MATRIX.md",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "D1-V003_LITERATURE_AUDIT.md",

    ROOT
    / "outputs"
    / "verification"
    / "D1-V003"
    / "D1-V003_SEARCH_LOG.md",

    ROOT
    / "docs"
    / "protocols"
    / "D1-V003_LITERATURE_AUDIT_PLAN.md",

    ROOT
    / "docs"
    / "protocols"
    / "D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md",

    ROOT
    / "docs"
    / "research_design"
    / "LAYER_JAMMING_MODEL_COMPARISON.md",

    ROOT
    / "docs"
    / "project"
    / "RESEARCH_STATE.md",

    ROOT
    / "docs"
    / "project"
    / "RESEARCH_LOG.md",
]


# ---------------------------------------------------------------------
# STRICT OUTPUT SCHEMA
# ---------------------------------------------------------------------

SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "confidence",
        "current_p1",
        "executive_summary",
        "model_families",
        "strongest_falsifying_evidence",
        "strongest_surviving_evidence",
        "evidence_gap_matrix",
        "fatal_novelty_conflicts",
        "unresolved_questions",
        "track_c_requirements",
        "search_stop_condition",
        "final_verdict_allowed",
        "recommended_next_action",
    ],
    "properties": {
        "status": {
            "type": "string",
            "enum": [
                "FALSIFIED",
                "SUBSTANTIALLY_NARROWED",
                "SURVIVES_WITH_REVISED_SCOPE",
                "SURVIVES_SO_FAR",
            ],
        },
        "confidence": {
            "type": "string",
            "enum": [
                "low",
                "medium",
                "high",
            ],
        },
        "current_p1": {
            "type": "string",
        },
        "executive_summary": {
            "type": "string",
        },
        "model_families": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "family",
                    "papers",
                    "model_type",
                    "what_is_established",
                    "what_is_not_established",
                    "threat_to_p1",
                ],
                "properties": {
                    "family": {
                        "type": "string",
                    },
                    "papers": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "model_type": {
                        "type": "string",
                    },
                    "what_is_established": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "what_is_not_established": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                    "threat_to_p1": {
                        "type": "string",
                        "enum": [
                            "low",
                            "medium",
                            "high",
                            "fatal",
                        ],
                    },
                },
            },
        },
        "strongest_falsifying_evidence": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "claim",
                    "source",
                    "evidence_status",
                    "what_it_proves",
                    "what_it_does_not_prove",
                ],
                "properties": {
                    "claim": {
                        "type": "string",
                    },
                    "source": {
                        "type": "string",
                    },
                    "evidence_status": {
                        "type": "string",
                        "enum": [
                            "VERIFIED_FULL_TEXT",
                            "METADATA_ONLY",
                            "INFERENCE",
                        ],
                    },
                    "what_it_proves": {
                        "type": "string",
                    },
                    "what_it_does_not_prove": {
                        "type": "string",
                    },
                },
            },
        },
        "strongest_surviving_evidence": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "gap",
                    "source_basis",
                    "evidence_status",
                    "why_it_survives",
                    "remaining_uncertainty",
                ],
                "properties": {
                    "gap": {
                        "type": "string",
                    },
                    "source_basis": {
                        "type": "string",
                    },
                    "evidence_status": {
                        "type": "string",
                        "enum": [
                            "VERIFIED_FULL_TEXT",
                            "METADATA_ONLY",
                            "INFERENCE",
                        ],
                    },
                    "why_it_survives": {
                        "type": "string",
                    },
                    "remaining_uncertainty": {
                        "type": "string",
                    },
                },
            },
        },
        "evidence_gap_matrix": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "finite_layer_count_scaling",
                "explicit_interlayer_slip",
                "independent_layer_count_variation",
                "pressure_dependence",
                "curvature_dependence",
                "bending_stiffness_prediction",
                "experimental_validation",
                "quantitative_prediction_error",
                "continuum_vs_discrete_validation",
                "tolerance_defined_validity_domain",
                "breakdown_boundary",
            ],
            "properties": {
                key: {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "status",
                        "evidence",
                        "interpretation",
                    ],
                    "properties": {
                        "status": {
                            "type": "string",
                            "enum": [
                                "PRESENT",
                                "PARTIAL",
                                "ABSENT",
                                "UNKNOWN",
                            ],
                        },
                        "evidence": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                        },
                        "interpretation": {
                            "type": "string",
                        },
                    },
                }
                for key in [
                    "finite_layer_count_scaling",
                    "explicit_interlayer_slip",
                    "independent_layer_count_variation",
                    "pressure_dependence",
                    "curvature_dependence",
                    "bending_stiffness_prediction",
                    "experimental_validation",
                    "quantitative_prediction_error",
                    "continuum_vs_discrete_validation",
                    "tolerance_defined_validity_domain",
                    "breakdown_boundary",
                ]
            },
        },
        "fatal_novelty_conflicts": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "unresolved_questions": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "track_c_requirements": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "search_target",
                    "why_it_matters",
                    "falsification_condition",
                    "suggested_queries",
                ],
                "properties": {
                    "search_target": {
                        "type": "string",
                    },
                    "why_it_matters": {
                        "type": "string",
                    },
                    "falsification_condition": {
                        "type": "string",
                    },
                    "suggested_queries": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                },
            },
        },
        "search_stop_condition": {
            "type": "string",
        },
        "final_verdict_allowed": {
            "type": "boolean",
        },
        "recommended_next_action": {
            "type": "string",
        },
    },
}


# ---------------------------------------------------------------------
# UTILITIES
# ---------------------------------------------------------------------

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def read_text(path: Path) -> str:
    return path.read_text(
        encoding="utf-8",
        errors="replace",
    )


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def timestamp_id() -> str:
    return utc_now().strftime(
        "%Y%m%dT%H%M%SZ"
    )


def source_metadata(
    path: Path,
    current_matrix_mtime: float,
) -> dict[str, Any]:

    stat = path.stat()

    stale_relative_to_current_matrix = (
        path != CURRENT_MATRIX
        and stat.st_mtime < current_matrix_mtime
        and "D1-V003" in str(path)
    )

    role = (
        "PRIOR_OR_POTENTIALLY_STALE_CONTEXT"
        if stale_relative_to_current_matrix
        else "CURRENT_OR_HISTORICAL_EVIDENCE"
    )

    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256_file(path),
        "size_bytes": stat.st_size,
        "mtime_utc": datetime.fromtimestamp(
            stat.st_mtime,
            tz=timezone.utc,
        ).isoformat(),
        "role": role,
    }


def collect_inputs() -> tuple[
    list[Path],
    list[Path],
]:

    missing_core = [
        path
        for path in CORE_INPUTS
        if not path.exists()
    ]

    if missing_core:
        print(
            "[ERROR] Missing required inputs:",
            file=sys.stderr,
        )

        for path in missing_core:
            print(
                f"  - {path.relative_to(ROOT)}",
                file=sys.stderr,
            )

        raise SystemExit(2)

    optional_present = [
        path
        for path in OPTIONAL_INPUTS
        if path.exists()
    ]

    optional_missing = [
        path
        for path in OPTIONAL_INPUTS
        if not path.exists()
    ]

    if optional_missing:
        print(
            "[WARN] Optional inputs not found:"
        )

        for path in optional_missing:
            print(
                f"  - {path.relative_to(ROOT)}"
            )

    return CORE_INPUTS, optional_present


# ---------------------------------------------------------------------
# PROMPT
# ---------------------------------------------------------------------

def build_prompt(
    sources: list[Path],
    source_meta: list[dict[str, Any]],
) -> str:

    blocks: list[str] = []

    metadata_by_path = {
        item["path"]: item
        for item in source_meta
    }

    for path in sources:

        relative = str(
            path.relative_to(ROOT)
        )

        meta = metadata_by_path[relative]

        blocks.append(
            "\n".join(
                [
                    "",
                    "=" * 100,
                    f"SOURCE: {relative}",
                    f"SHA256: {meta['sha256']}",
                    f"ROLE: {meta['role']}",
                    "=" * 100,
                    "",
                    read_text(path),
                    "",
                ]
            )
        )

    evidence_bundle = "\n".join(blocks)

    return f"""
You are performing an adversarial cross-round scientific evidence
synthesis for an MSc research project in layer jamming, variable
stiffness, soft robotics, and continuum mechanics.

This is NOT a literature-summary task.

Your job is to try to falsify the current research premise.

======================================================================
CURRENT RESEARCH PREMISE
======================================================================

The current provisional direction is approximately:

"Quantitative validity/breakdown mapping of established continuum or
homogenized layer-jamming models relative to discrete mechanics and
experiment, with particular attention to finite layer count, vacuum
pressure, curvature, interlayer slip, and bending stiffness."

Earlier wording included:

"Validity Limits of a Homogenized Slip Model for High-Layer-Count
Vacuum-Jammed Beams."

The wording is provisional and MUST be revised if the evidence requires
it.

======================================================================
IMPORTANT PROJECT STATE
======================================================================

The evidence has been accumulated through three verification rounds:

D1-V001:
Initial external falsification.

D1-V002:
Direct novelty attack using foundational and closest layer-jamming
mechanics literature.

D1-V003:
New full-text evidence, including Fan/Yi-family modeling papers,
Zhang-family audits, direct layer-jamming papers, and search planning.

D1-V003 currently contains 9 unique verification papers after duplicate
removal.

Track C — adjacent solid mechanics — is NOT yet complete.

Therefore:

A final universal novelty claim is NOT allowed unless the existing
evidence already falsifies the direction.

If the direction has not been falsified, the strongest positive status
allowed at this stage is:

SURVIVES_SO_FAR

or:

SURVIVES_WITH_REVISED_SCOPE

======================================================================
CENTRAL FALSIFICATION QUESTION
======================================================================

Has prior literature already established a quantitative
validity/breakdown map for established continuum or homogenized
layer-jamming models relative to discrete mechanics and/or experiment?

Specifically determine whether prior work already maps model prediction
error as a function of one or more of:

- finite layer count,
- vacuum pressure,
- curvature,
- explicit interlayer slip,
- frictional state,
- bending stiffness,
- boundary conditions,

and whether it uses that error to establish a defined validity domain or
breakdown boundary.

======================================================================
CRITICAL DISTINCTIONS
======================================================================

You MUST preserve these distinctions:

model validation
!=
validity mapping

agreement with experiment
!=
defined model validity boundary

slip transition
!=
model breakdown boundary

many layers
!=
finite-layer-count validity criterion

continuum-vs-FEA comparison
!=
continuum-vs-discrete-interface validation

fitted effective stiffness
!=
mechanistic validation of homogenization

pressure-stiffness correlation
!=
validity-domain mapping

a paper mentioning an effect
!=
a paper quantifying a predictive error boundary

======================================================================
MODEL-FAMILY COMPARISON
======================================================================

Explicitly compare at least:

1. FAN / YI FAMILY

Potentially includes:
- Fan 2022
- Yi 2024
- Fan 2026

Possible characteristics:
- Euler-Bernoulli formulation
- energy-based models
- LuGre friction
- dynamic/control models
- stiffness regulation

Determine from the supplied evidence what is actually supported.

2. CARUSO / ZHANG FAMILY

Potentially includes:
- Caruso 2023
- Zhang continuum beam work
- Zhang deeper-understanding work
- continuum constitutive/RVE work

Possible characteristics:
- partial/full slip
- continuum mechanics
- homogenization
- elastoplastic formulation
- large deformation
- experimental validation

Again, use only what the supplied evidence supports.

======================================================================
EVIDENCE DISCIPLINE
======================================================================

Every important statement must be classifiable as:

VERIFIED_FULL_TEXT
METADATA_ONLY
INFERENCE

Do not infer detailed scientific results from titles, citation counts,
keywords, or metadata.

If evidence is ambiguous, use UNKNOWN or explicitly state the ambiguity.

Do not convert:

"No qualifying evidence was found"

into:

"No such paper exists."

Track C is incomplete.

Negative evidence must therefore be treated cautiously.

======================================================================
STALE CONTEXT RULE
======================================================================

Some D1-V003 documents may predate the current 9-paper verification
matrix.

Sources marked:

PRIOR_OR_POTENTIALLY_STALE_CONTEXT

may be used for historical reasoning, search design, or previously
identified threats.

They must NOT override newer full-text verification evidence.

The current D1-V003 verification_matrix.json is authoritative for the
present verification corpus.

======================================================================
EVIDENCE GAP MATRIX
======================================================================

For every dimension classify:

PRESENT
PARTIAL
ABSENT
UNKNOWN

Dimensions:

- finite-layer-count scaling
- explicit interlayer slip
- independent layer-count variation
- pressure dependence
- curvature dependence
- bending-stiffness prediction
- experimental validation
- quantitative prediction error
- continuum-vs-discrete validation
- tolerance-defined validity domain
- breakdown boundary

"PRESENT" requires meaningful direct evidence.

"ABSENT" means absent from the supplied qualifying evidence,
NOT absent from all literature.

======================================================================
VERDICT RULES
======================================================================

FALSIFIED

Use only if prior evidence already solves the essential research problem
under sufficiently comparable conditions.

SUBSTANTIALLY_NARROWED

Use if major parts of P1 are already solved and only a materially
smaller question remains.

SURVIVES_WITH_REVISED_SCOPE

Use if the original P1 is too broad but a clearly defined narrower gap
remains.

SURVIVES_SO_FAR

Use only if no fatal conflict is found in the current evidence but Track
C or other key verification remains incomplete.

Do NOT use "PROVEN NOVEL".

======================================================================
TRACK C
======================================================================

If P1 is not already falsified, define exactly what adjacent-mechanics
literature must be searched next.

Consider:

- partial-interaction beams,
- layered beams,
- laminated beams,
- frictional interfaces,
- shear-slip beam theories,
- composite beams with imperfect interaction,
- multi-leaf springs,
- multilayer frictional beams,
- finite-layer homogenization,
- discrete-to-continuum transition,
- asymptotic homogenization,
- micropolar or generalized continuum theories where relevant.

For each Track C target provide:

- what to search,
- why it threatens P1,
- what finding would falsify/narrow P1,
- concrete Scopus-style search queries.

======================================================================
FINAL-VERDICT RULE
======================================================================

Unless P1 is already falsified by existing full-text evidence:

final_verdict_allowed MUST be false

because Track C remains incomplete.

======================================================================
SOURCE MANIFEST
======================================================================

{json.dumps(source_meta, ensure_ascii=False, indent=2)}

======================================================================
SOURCE CONTENT
======================================================================

{evidence_bundle}

======================================================================
OUTPUT
======================================================================

Return ONLY a JSON object conforming exactly to the supplied JSON schema.

Do not add Markdown fences.

Do not add commentary outside the JSON.
""".strip()


# ---------------------------------------------------------------------
# CODEX CALL
# ---------------------------------------------------------------------

def run_codex(
    prompt: str,
    schema_path: Path,
    raw_output_path: Path,
    model: str,
    effort: str,
) -> None:

    cmd = [
        "codex",
        "exec",
        "--model",
        model,
        "-c",
        f'model_reasoning_effort="{effort}"',
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(raw_output_path),
        "-",
    ]

    env = os.environ.copy()


    print(
        "[MODEL]",
        model,
    )
    print(
        "[EFFORT]",
        effort,
    )

    proc = subprocess.run(
        cmd,
        input=prompt,
        text=True,
        cwd=ROOT,
        env=env,
    )

    if proc.returncode != 0:
        raise RuntimeError(
            "Codex execution failed with "
            f"exit code {proc.returncode}."
        )

    if not raw_output_path.exists():
        raise RuntimeError(
            "Codex completed but did not create "
            "the expected output file."
        )


# ---------------------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------------------

def validate_output_shape(
    data: dict[str, Any],
) -> None:

    required = set(
        SCHEMA["required"]
    )

    missing = required - set(data)

    if missing:
        raise RuntimeError(
            "Model output missing required keys: "
            + ", ".join(sorted(missing))
        )

    valid_statuses = {
        "FALSIFIED",
        "SUBSTANTIALLY_NARROWED",
        "SURVIVES_WITH_REVISED_SCOPE",
        "SURVIVES_SO_FAR",
    }

    if data["status"] not in valid_statuses:
        raise RuntimeError(
            "Invalid synthesis status: "
            f"{data['status']}"
        )

    if (
        data["status"] != "FALSIFIED"
        and data["final_verdict_allowed"] is True
    ):
        raise RuntimeError(
            "Scientific guardrail violation: "
            "final_verdict_allowed=true while "
            "Track C remains incomplete."
        )


# ---------------------------------------------------------------------
# MARKDOWN RENDERING
# ---------------------------------------------------------------------

def render_markdown(
    data: dict[str, Any],
    manifest: list[dict[str, Any]],
    bundle_sha256: str,
) -> str:

    lines: list[str] = []

    lines.append(
        "# D1-V003 Cross-Round Adversarial Synthesis"
    )
    lines.append("")

    lines.append(
        f"- **Status:** {data['status']}"
    )
    lines.append(
        f"- **Confidence:** {data['confidence']}"
    )
    lines.append(
        f"- **Final verdict allowed:** "
        f"{data['final_verdict_allowed']}"
    )
    lines.append(
        f"- **Evidence bundle SHA256:** "
        f"`{bundle_sha256}`"
    )
    lines.append("")

    lines.append(
        "## Current P1"
    )
    lines.append("")
    lines.append(
        data["current_p1"]
    )
    lines.append("")

    lines.append(
        "## Executive summary"
    )
    lines.append("")
    lines.append(
        data["executive_summary"]
    )
    lines.append("")

    lines.append(
        "## Model families"
    )
    lines.append("")

    for family in data["model_families"]:
        lines.append(
            f"### {family['family']}"
        )
        lines.append("")
        lines.append(
            f"**Model type:** "
            f"{family['model_type']}"
        )
        lines.append("")
        lines.append(
            f"**Threat to P1:** "
            f"{family['threat_to_p1']}"
        )
        lines.append("")

        lines.append(
            "**Papers:**"
        )

        for item in family["papers"]:
            lines.append(
                f"- {item}"
            )

        lines.append("")
        lines.append(
            "**Established:**"
        )

        for item in family["what_is_established"]:
            lines.append(
                f"- {item}"
            )

        lines.append("")
        lines.append(
            "**Not established:**"
        )

        for item in family["what_is_not_established"]:
            lines.append(
                f"- {item}"
            )

        lines.append("")

    lines.append(
        "## Strongest falsifying evidence"
    )
    lines.append("")

    for item in data[
        "strongest_falsifying_evidence"
    ]:
        lines.append(
            f"- **{item['claim']}**"
        )
        lines.append(
            f"  - Source: {item['source']}"
        )
        lines.append(
            f"  - Evidence: "
            f"{item['evidence_status']}"
        )
        lines.append(
            f"  - Proves: "
            f"{item['what_it_proves']}"
        )
        lines.append(
            f"  - Does not prove: "
            f"{item['what_it_does_not_prove']}"
        )

    lines.append("")

    lines.append(
        "## Strongest surviving evidence"
    )
    lines.append("")

    for item in data[
        "strongest_surviving_evidence"
    ]:
        lines.append(
            f"- **{item['gap']}**"
        )
        lines.append(
            f"  - Basis: "
            f"{item['source_basis']}"
        )
        lines.append(
            f"  - Evidence: "
            f"{item['evidence_status']}"
        )
        lines.append(
            f"  - Why it survives: "
            f"{item['why_it_survives']}"
        )
        lines.append(
            f"  - Uncertainty: "
            f"{item['remaining_uncertainty']}"
        )

    lines.append("")

    lines.append(
        "## Evidence-gap matrix"
    )
    lines.append("")

    lines.append(
        "| Dimension | Status | Interpretation |"
    )
    lines.append(
        "|---|---|---|"
    )

    for key, value in data[
        "evidence_gap_matrix"
    ].items():
        lines.append(
            f"| {key} | "
            f"{value['status']} | "
            f"{value['interpretation']} |"
        )

    lines.append("")

    lines.append(
        "## Fatal novelty conflicts"
    )
    lines.append("")

    if data["fatal_novelty_conflicts"]:
        for item in data[
            "fatal_novelty_conflicts"
        ]:
            lines.append(
                f"- {item}"
            )
    else:
        lines.append(
            "- None established in the supplied evidence."
        )

    lines.append("")

    lines.append(
        "## Unresolved questions"
    )
    lines.append("")

    for item in data[
        "unresolved_questions"
    ]:
        lines.append(
            f"- {item}"
        )

    lines.append("")

    lines.append(
        "## Track C requirements"
    )
    lines.append("")

    for item in data[
        "track_c_requirements"
    ]:
        lines.append(
            f"### {item['search_target']}"
        )
        lines.append("")
        lines.append(
            f"**Why it matters:** "
            f"{item['why_it_matters']}"
        )
        lines.append("")
        lines.append(
            f"**Falsification condition:** "
            f"{item['falsification_condition']}"
        )
        lines.append("")
        lines.append(
            "**Suggested queries:**"
        )

        for query in item[
            "suggested_queries"
        ]:
            lines.append(
                f"- `{query}`"
            )

        lines.append("")

    lines.append(
        "## Search stop condition"
    )
    lines.append("")
    lines.append(
        data["search_stop_condition"]
    )
    lines.append("")

    lines.append(
        "## Recommended next action"
    )
    lines.append("")
    lines.append(
        data["recommended_next_action"]
    )
    lines.append("")

    lines.append(
        "## Evidence provenance"
    )
    lines.append("")

    for item in manifest:
        lines.append(
            f"- `{item['path']}`"
        )
        lines.append(
            f"  - role: "
            f"{item['role']}"
        )
        lines.append(
            f"  - sha256: "
            f"`{item['sha256']}`"
        )

    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------

def main() -> None:

    parser = argparse.ArgumentParser(
        description=(
            "Cross-round adversarial synthesis for "
            "D1-V001 + D1-V002 + D1-V003."
        )
    )

    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help=(
            "Build manifest, prompt, and JSON schema "
            "without calling Codex."
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Allow canonical latest outputs to be replaced "
            "after a successful run."
        ),
    )

    parser.add_argument(
        "--model",
        default=os.getenv(
            "CODEX_RESEARCH_MODEL",
            "",
        ),
        help=(
            "Codex model. Defaults to "
            "CODEX_RESEARCH_MODEL."
        ),
    )

    parser.add_argument(
        "--effort",
        default=os.getenv(
            "CODEX_RESEARCH_EFFORT",
            "high",
        ),
        choices=[
            "low",
            "medium",
            "high",
            "xhigh",
        ],
    )

    args = parser.parse_args()

    OUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    RUNS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    if not CURRENT_MATRIX.exists():
        raise RuntimeError(
            "Current D1-V003 verification matrix "
            "does not exist."
        )

    current_matrix_mtime = (
        CURRENT_MATRIX.stat().st_mtime
    )

    core, optional = collect_inputs()

    sources = core + optional

    manifest = [
        source_metadata(
            path,
            current_matrix_mtime,
        )
        for path in sources
    ]

    bundle_hash_input = "\n".join(
        f"{item['path']}:{item['sha256']}"
        for item in manifest
    ).encode("utf-8")

    bundle_sha256 = sha256_bytes(
        bundle_hash_input
    )

    run_id = timestamp_id()

    run_dir = (
        RUNS_DIR
        / run_id
    )

    run_dir.mkdir(
        parents=True,
        exist_ok=False,
    )

    schema_path = (
        run_dir
        / "output_schema.json"
    )

    manifest_path = (
        run_dir
        / "source_manifest.json"
    )

    prompt_path = (
        run_dir
        / "prompt.txt"
    )

    raw_path = (
        run_dir
        / "raw_model_output.json"
    )

    result_json_path = (
        run_dir
        / "cross_round_adversarial_synthesis.json"
    )

    result_md_path = (
        run_dir
        / "cross_round_adversarial_synthesis.md"
    )

    schema_path.write_text(
        json.dumps(
            SCHEMA,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    manifest_path.write_text(
        json.dumps(
            {
                "run_id": run_id,
                "created_at_utc": (
                    utc_now().isoformat()
                ),
                "evidence_bundle_sha256": (
                    bundle_sha256
                ),
                "sources": manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    prompt = build_prompt(
        sources,
        manifest,
    )

    prompt_path.write_text(
        prompt,
        encoding="utf-8",
    )

    print(
        f"[RUN] {run_id}"
    )
    print(
        f"[SOURCES] {len(sources)}"
    )
    print(
        f"[BUNDLE SHA256] {bundle_sha256}"
    )
    print(
        f"[PROMPT CHARS] {len(prompt):,}"
    )
    print(
        f"[RUN DIR] {run_dir.relative_to(ROOT)}"
    )

    stale = [
        item
        for item in manifest
        if (
            item["role"]
            == "PRIOR_OR_POTENTIALLY_STALE_CONTEXT"
        )
    ]

    if stale:
        print(
            f"[STALE/PRIOR CONTEXT] {len(stale)}"
        )

        for item in stale:
            print(
                f"  - {item['path']}"
            )

    if args.prepare_only:
        print(
            "[PREPARE ONLY] Model call skipped."
        )
        return

    if not args.model:
        raise RuntimeError(
            "No Codex model configured.\n"
            "Set CODEX_RESEARCH_MODEL in .env "
            "or pass --model."
        )

    if (
        CANONICAL_JSON.exists()
        and not args.force
    ):
        raise RuntimeError(
            "Canonical synthesis output already exists.\n"
            "The timestamped run has been prepared safely.\n"
            "Use --force only if you intentionally want "
            "to replace the canonical latest output."
        )

    run_codex(
        prompt=prompt,
        schema_path=schema_path,
        raw_output_path=raw_path,
        model=args.model,
        effort=args.effort,
    )

    raw_text = read_text(
        raw_path
    ).strip()

    try:
        result = json.loads(
            raw_text
        )
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Model output is not valid JSON."
        ) from exc

    if not isinstance(
        result,
        dict,
    ):
        raise RuntimeError(
            "Model output must be a JSON object."
        )

    validate_output_shape(
        result
    )

    result["_provenance"] = {
        "run_id": run_id,
        "created_at_utc": (
            utc_now().isoformat()
        ),
        "evidence_bundle_sha256": (
            bundle_sha256
        ),
        "model": args.model,
        "effort": args.effort,
    }

    result_json_path.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    markdown = render_markdown(
        result,
        manifest,
        bundle_sha256,
    )

    result_md_path.write_text(
        markdown,
        encoding="utf-8",
    )

    # Canonical latest outputs are updated only after:
    # 1. successful model call
    # 2. valid JSON
    # 3. scientific guardrail validation
    shutil.copy2(
        result_json_path,
        CANONICAL_JSON,
    )

    shutil.copy2(
        result_md_path,
        CANONICAL_MD,
    )

    shutil.copy2(
        raw_path,
        CANONICAL_RAW,
    )

    print(
        f"[STATUS] {result['status']}"
    )
    print(
        f"[CONFIDENCE] {result['confidence']}"
    )
    print(
        f"[FINAL VERDICT ALLOWED] "
        f"{result['final_verdict_allowed']}"
    )

    print(
        "[SAVED]",
        result_json_path.relative_to(ROOT),
    )
    print(
        "[SAVED]",
        result_md_path.relative_to(ROOT),
    )
    print(
        "[UPDATED]",
        CANONICAL_JSON.relative_to(ROOT),
    )
    print(
        "[UPDATED]",
        CANONICAL_MD.relative_to(ROOT),
    )


if __name__ == "__main__":
    main()
