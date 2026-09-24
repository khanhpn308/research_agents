from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VERIFICATION_ID = "MP1-V002"
OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
AUDIT_PATH = OUT_DIR / "TARGETED_THREAT_AUDIT.json"
MATRIX_PATH = OUT_DIR / "verification_matrix.json"
COVERAGE_PATH = OUT_DIR / "citation_coverage.json"
STATUS_MD = OUT_DIR / "CITATION_COVERAGE_STATUS.md"

CORE_ANCHORS = [
    {
        "anchor_key": "doi:10.3390/app12073582",
        "title": "Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming",
        "doi": "10.3390/app12073582",
        "target_ids": ["T1"],
    },
    {
        "anchor_key": "doi:10.1109/lra.2021.3097255",
        "title": "A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots",
        "doi": "10.1109/LRA.2021.3097255",
        "target_ids": ["T2"],
    },
    {
        "anchor_key": "doi:10.5194/ms-17-481-2026",
        "title": "A variable stiffness omnidirectional chain based on positive-pressure fiber jamming",
        "doi": "10.5194/ms-17-481-2026",
        "target_ids": ["T1", "T2", "T3"],
    },
    {
        "anchor_key": "doi:10.20965/jrm.2022.p0466",
        "title": "Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon",
        "doi": "10.20965/jrm.2022.p0466",
        "target_ids": ["T3"],
    },
    {
        "anchor_key": "doi:10.1299/mej.24-00130",
        "title": "Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon",
        "doi": "10.1299/mej.24-00130",
        "target_ids": ["T3"],
    },
    {
        "anchor_key": "doi:10.1108/ir-11-2023-0305",
        "title": "Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm",
        "doi": "10.1108/IR-11-2023-0305",
        "target_ids": ["T3"],
    },
]

SCREENED = {"screened_no_high_threat", "screened_candidates_found"}
ALLOWED = SCREENED | {"not_screened"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def direction(required: bool) -> dict[str, Any]:
    return {
        "required": required,
        "status": "not_screened",
        "database": "Scopus",
        "search_date": "",
        "records_screened": 0,
        "included_candidate_ids": [],
        "unresolved_high_threat_sources": [],
        "notes": "",
    }


def init_payload() -> dict[str, Any]:
    if not AUDIT_PATH.exists():
        raise RuntimeError(
            "TARGETED_THREAT_AUDIT.json not found. Run the interim V002 audit first."
        )
    audit = load_json(AUDIT_PATH)
    matrix = load_json(MATRIX_PATH)
    if matrix.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("V002 matrix identity mismatch.")

    by_id: dict[str, dict[str, Any]] = {}
    for p in matrix.get("papers", []):
        evidence = p.get("evidence", {}).get("paper", {})
        by_id[str(p.get("paper_id"))] = {
            "paper_id": str(p.get("paper_id")),
            "title": str(evidence.get("title") or p.get("filename") or ""),
            "doi": str(evidence.get("doi") or ""),
        }

    anchors: list[dict[str, Any]] = []
    seen: set[str] = set()

    for item in CORE_ANCHORS:
        key = item["anchor_key"]
        seen.add(key)
        anchors.append({
            **item,
            "paper_id": "",
            "role": "core_protocol_anchor",
            "backward": direction(True),
            "forward": direction(True),
        })

    plan = audit.get("citation_chase_plan", {})
    for pid_raw in plan.get("backward_priority_paper_ids", []):
        pid = str(pid_raw)
        if pid not in by_id:
            raise RuntimeError(f"Audit names unknown V002 paper_id: {pid}")
        p = by_id[pid]
        doi_norm = p["doi"].strip().lower()
        key = f"doi:{doi_norm}" if doi_norm else f"paper:{pid}"
        if key in seen:
            continue
        seen.add(key)
        anchors.append({
            "anchor_key": key,
            "paper_id": pid,
            "title": p["title"],
            "doi": p["doi"],
            "target_ids": [],
            "role": "v002_high_threat_backward_anchor",
            "backward": direction(True),
            "forward": direction(False),
        })

    return {
        "schema_version": 1,
        "verification_id": VERIFICATION_ID,
        "purpose": (
            "Document protocol-bounded backward/forward citation screening. "
            "This is coverage evidence, not scientific evidence."
        ),
        "search_cutoff_date": "",
        "anchors": anchors,
        "unresolved_named_high_threat_sources": list(
            plan.get("named_high_threat_sources", [])
        ),
        "stop_condition": {
            "all_required_directions_screened": False,
            "no_unresolved_high_threat_source": False,
            "satisfied": False,
        },
    }


def validate_and_update(
    payload: dict[str, Any],
) -> tuple[bool, list[str]]:
    if payload.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("citation_coverage.json verification_id mismatch.")

    issues: list[str] = []
    all_required = True
    unresolved = list(
        payload.get("unresolved_named_high_threat_sources", [])
    )

    for anchor in payload.get("anchors", []):
        name = anchor.get("title") or anchor.get("anchor_key")
        for direction_name in ["backward", "forward"]:
            d = anchor.get(direction_name, {})
            status = d.get("status")
            if status not in ALLOWED:
                raise RuntimeError(
                    f"{name} {direction_name}: invalid status {status!r}."
                )
            if not d.get("required"):
                continue

            if status not in SCREENED:
                all_required = False
                issues.append(
                    f"NOT SCREENED: {name} [{direction_name}]"
                )

            if status in SCREENED:
                if not str(d.get("search_date", "")).strip():
                    issues.append(
                        f"MISSING search_date: {name} [{direction_name}]"
                    )
                    all_required = False
                if int(d.get("records_screened", 0)) < 0:
                    raise RuntimeError(
                        "records_screened cannot be negative."
                    )

            for item in d.get(
                "unresolved_high_threat_sources", []
            ):
                unresolved.append(str(item))

    no_unresolved = (
        len([x for x in unresolved if str(x).strip()]) == 0
    )
    satisfied = all_required and no_unresolved

    payload["stop_condition"] = {
        "all_required_directions_screened": all_required,
        "no_unresolved_high_threat_source": no_unresolved,
        "satisfied": satisfied,
    }

    if not no_unresolved:
        issues.append("UNRESOLVED HIGH-THREAT SOURCES remain.")

    return satisfied, issues


def render_md(
    payload: dict[str, Any],
    issues: list[str],
) -> str:
    stop = payload["stop_condition"]
    lines = [
        "# MP1-V002 Citation Coverage Status",
        "",
        f"- **Search cutoff date:** "
        f"{payload.get('search_cutoff_date') or 'NOT SET'}",
        f"- **All required directions screened:** "
        f"{stop['all_required_directions_screened']}",
        f"- **No unresolved high-threat source:** "
        f"{stop['no_unresolved_high_threat_source']}",
        f"- **Stop condition satisfied:** {stop['satisfied']}",
        "",
        "## Coverage",
        "",
        "| Anchor | Role | Backward | Forward |",
        "|---|---|---|---|",
    ]

    for a in payload.get("anchors", []):
        b = a["backward"]
        f = a["forward"]
        btxt = b["status"] if b["required"] else "not required"
        ftxt = f["status"] if f["required"] else "not required"
        lines.append(
            f"| {a['title']} | {a['role']} | {btxt} | {ftxt} |"
        )

    lines += ["", "## Open issues", ""]
    lines += [f"- {x}" for x in issues] or ["- None."]
    lines += [
        "",
        "## Rule",
        "",
        (
            "A true stop condition is protocol closure only; "
            "it is not proof that no overlapping paper exists anywhere."
        ),
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize/check MP1-V002 citation coverage."
    )
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if args.init == args.check:
        raise RuntimeError(
            "Choose exactly one of --init or --check."
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.init:
        if COVERAGE_PATH.exists() and not args.force:
            raise RuntimeError(
                f"Coverage file already exists: {COVERAGE_PATH}. "
                "Use --force only intentionally."
            )
        payload = init_payload()
        COVERAGE_PATH.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        _, issues = validate_and_update(payload)
        STATUS_MD.write_text(
            render_md(payload, issues),
            encoding="utf-8",
        )
        print(
            f"[INITIALIZED] {COVERAGE_PATH.relative_to(ROOT)}"
        )
        print(f"[STATUS] {STATUS_MD.relative_to(ROOT)}")
        return

    if not COVERAGE_PATH.exists():
        raise RuntimeError(
            "citation_coverage.json not found. Run --init first."
        )

    payload = load_json(COVERAGE_PATH)
    satisfied, issues = validate_and_update(payload)

    COVERAGE_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    STATUS_MD.write_text(
        render_md(payload, issues),
        encoding="utf-8",
    )

    print(
        f"[STOP CONDITION] "
        f"{'SATISFIED' if satisfied else 'OPEN'}"
    )
    print(f"[OPEN ISSUES] {len(issues)}")
    for issue in issues:
        print(f"- {issue}")
    print(f"[SAVED] {STATUS_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
