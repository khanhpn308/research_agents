from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VERIFICATION_ID = "MP1-V002"
OUT_DIR = ROOT / "outputs" / "verification" / VERIFICATION_ID
AUDIT_PATH = OUT_DIR / "TARGETED_THREAT_AUDIT.json"
MATRIX_PATH = OUT_DIR / "verification_matrix.json"
COVERAGE_PATH = OUT_DIR / "citation_coverage.json"
STATUS_MD = OUT_DIR / "CITATION_COVERAGE_STATUS.md"

# Metadata for the protocol anchors that may not be present in the
# MP1-V002 full-text matrix. Required forward directions are NOT
# hard-coded here; they are read dynamically from the latest audit.
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

# Historical screening provenance that predates the dynamic coverage tracker.
# These entries are restored ONLY when the referenced provenance file exists.
# This prevents a tracker reset from forcing already-completed branches to be
# screened again, while preserving an auditable source for every restored state.
HISTORICAL_COVERAGE: dict[tuple[str, str], dict[str, Any]] = {
    ("doi:10.1061/(asce)em.1943-7889.0000852", "backward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-24",
        "records_screened": 57,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B01.csv"],
        "notes": "Restored from B01 citation export and completed metadata/full-text screening.",
    },
    ("doi:10.1061/(asce)em.1943-7889.0001072", "backward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-25",
        "records_screened": 34,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B09.csv"],
        "notes": "Restored from B09 citation export and 13-paper chase screening; candidates were human-reviewed and promoted when warranted.",
    },
    ("doi:10.1080/15376494.2021.1955313", "backward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-24",
        "records_screened": 33,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B02.csv"],
        "notes": "Restored from B02 citation export and completed metadata/full-text screening.",
    },
    ("paper:aaad9c248c", "backward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 4,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B03.csv"],
        "notes": "Restored from B03 citation export; no unresolved high-threat source remained.",
    },
    ("paper:ccdc1bb980", "backward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 9,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B04.csv"],
        "notes": "Restored from B04 citation export; no unresolved high-threat source remained.",
    },
    ("doi:10.1016/j.matlet.2026.141544", "backward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 10,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B05.csv"],
        "notes": "Restored from B05 citation export; no unresolved high-threat source remained.",
    },
    ("doi:10.3390/s22208045", "backward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-24",
        "records_screened": 22,
        "source_paths": ["data/search_exports/MP1-V002/raw/backward/B06_silva_publisher_references.txt"],
        "notes": "Restored from B06 publisher-reference provenance; candidates were resolved by full text.",
    },
    ("doi:10.1016/j.ijsolstr.2013.03.015", "backward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-25",
        "records_screened": 11,
        "source_paths": [
            "data/search_exports/MP1-V002/raw/backward/B08.csv",
            "data/search_exports/MP1-V002/raw/backward/B08_reedlunn_references.csv",
            "data/search_exports/MP1-V002/raw/backward/B08_reedlunn_publisher_references.txt",
        ],
        "notes": "Restore only if B08 provenance has been saved; screening yielded Reedlunn Part I.",
    },
    ("doi:10.3390/app12073582", "forward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-24",
        "records_screened": 14,
        "source_paths": ["data/search_exports/MP1-V002/raw/forward/F01.csv"],
        "notes": "Restored from F01 forward-citation export and completed metadata screening.",
    },
    ("doi:10.1109/lra.2021.3097255", "forward"): {
        "status": "screened_candidates_found",
        "search_date": "2026-09-24",
        "records_screened": 51,
        "source_paths": ["data/search_exports/MP1-V002/raw/forward/F02.csv"],
        "notes": "Restored from F02 forward-citation export and completed metadata screening.",
    },
    ("doi:10.5194/ms-17-481-2026", "forward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 0,
        "source_paths": ["data/search_exports/MP1-V002/raw/forward/F03_zhang_yao_zero.txt"],
        "notes": "Restored from zero-result Scopus provenance at the recorded cutoff.",
    },
    ("doi:10.20965/jrm.2022.p0466", "forward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 9,
        "source_paths": ["data/search_exports/MP1-V002/raw/forward/F04.csv"],
        "notes": "Restored from F04 forward-citation export; no unresolved high-threat source remained.",
    },
    ("doi:10.1299/mej.24-00130", "forward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 1,
        "source_paths": ["data/search_exports/MP1-V002/raw/forward/F05_matsumoto_researchgate.txt"],
        "notes": "Restored from F05 provenance; the one citing paper was resolved as KEEP_METADATA.",
    },
    ("doi:10.1108/ir-11-2023-0305", "forward"): {
        "status": "screened_no_high_threat",
        "search_date": "2026-09-24",
        "records_screened": 0,
        "source_paths": ["data/search_exports/MP1-V002/raw/forward/F06_wang_zero.txt"],
        "notes": "Restored from zero-result Scopus provenance at the recorded cutoff.",
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_doi(value: Any) -> str:
    doi = str(value or "").strip()
    if doi.lower().startswith("https://doi.org/"):
        doi = doi[len("https://doi.org/"):]
    if doi.lower().startswith("http://doi.org/"):
        doi = doi[len("http://doi.org/"):]
    if doi.lower().startswith("doi:"):
        doi = doi[4:].strip()
    return doi.lower()


def doi_key(value: Any) -> str:
    doi = normalize_doi(value)
    if not doi:
        raise RuntimeError("Cannot build DOI anchor key from an empty DOI.")
    return f"doi:{doi}"


def normalize_title_text(value: Any) -> str:
    text = str(value or "").casefold()
    text = text.replace("–", " ").replace("—", " ").replace("−", " ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def significant_title_tokens(value: Any) -> set[str]:
    stop = {
        "a", "an", "and", "of", "the", "in", "on", "for", "to",
        "with", "via", "using", "part", "parts", "i", "ii", "et", "al",
    }
    return {
        token
        for token in normalize_title_text(value).split()
        if len(token) >= 3 and token not in stop
    }


def named_source_matches_title(source: str, title: str) -> bool:
    source_norm = normalize_title_text(source)
    title_norm = normalize_title_text(title)

    if not source_norm or not title_norm:
        return False

    if len(title_norm) >= 20 and title_norm in source_norm:
        return True

    # Audit-generated named sources often use shortened family titles
    # (e.g. "Parts I and II"). Use conservative token overlap so these
    # resolve to full-text matrix papers without fuzzy free-form matching.
    source_tokens = significant_title_tokens(source_norm)
    title_tokens = significant_title_tokens(title_norm)
    if not source_tokens or not title_tokens:
        return False

    shared = source_tokens & title_tokens
    shorter = min(len(source_tokens), len(title_tokens))

    return len(shared) >= 4 and (len(shared) / shorter) >= 0.60


def historical_direction(
    anchor_key: str,
    direction_name: str,
) -> dict[str, Any] | None:
    item = HISTORICAL_COVERAGE.get(
        (anchor_key.strip().lower(), direction_name)
    )
    if not item:
        return None

    existing_paths = [
        ROOT / path
        for path in item.get("source_paths", [])
        if (ROOT / path).exists()
    ]
    if not existing_paths:
        return None

    return {
        "status": item["status"],
        "database": "Scopus",
        "search_date": item["search_date"],
        "records_screened": item["records_screened"],
        "included_candidate_ids": [],
        "unresolved_high_threat_sources": [],
        "notes": (
            item["notes"]
            + " Provenance: "
            + ", ".join(str(path.relative_to(ROOT)) for path in existing_paths)
        ),
    }


def split_named_threats_by_matrix(
    named_sources: list[str],
    matrix: dict[str, Any],
) -> tuple[list[str], list[str]]:
    """Separate already-audited V002 sources from genuinely unresolved named threats."""
    identities: list[tuple[str, str]] = []
    for paper in matrix.get("papers", []):
        evidence = paper.get("evidence", {}).get("paper", {})
        title = str(
            evidence.get("title")
            or paper.get("filename")
            or ""
        ).strip().casefold()
        doi = normalize_doi(evidence.get("doi"))
        identities.append((title, doi))

    resolved: list[str] = []
    unresolved: list[str] = []

    for source in named_sources:
        token = str(source).strip()
        folded = token.casefold()
        matched = False

        for title, doi in identities:
            if doi and doi in folded:
                matched = True
                break
            if title and named_source_matches_title(token, title):
                matched = True
                break

        if matched:
            resolved.append(token)
        else:
            unresolved.append(token)

    return resolved, unresolved


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


def merge_direction(
    fresh: dict[str, Any],
    previous: dict[str, Any] | None,
) -> dict[str, Any]:
    """Preserve prior screening provenance while updating requirement state."""
    if not previous:
        return fresh

    required = bool(fresh.get("required"))

    # Preserve only known coverage fields. The current audit controls whether
    # the direction is required; historical screening metadata remains useful.
    merged = {
        **fresh,
        "required": required,
        "status": previous.get("status", fresh["status"]),
        "database": previous.get("database", fresh["database"]),
        "search_date": previous.get("search_date", fresh["search_date"]),
        "records_screened": previous.get(
            "records_screened",
            fresh["records_screened"],
        ),
        "included_candidate_ids": list(
            previous.get(
                "included_candidate_ids",
                fresh["included_candidate_ids"],
            )
        ),
        "unresolved_high_threat_sources": list(
            previous.get(
                "unresolved_high_threat_sources",
                fresh["unresolved_high_threat_sources"],
            )
        ),
        "notes": previous.get("notes", fresh["notes"]),
    }

    if merged["status"] not in ALLOWED:
        # Do not silently carry invalid legacy values into the new tracker.
        merged["status"] = "not_screened"

    return merged


def build_previous_index(
    previous: dict[str, Any] | None,
) -> dict[str, dict[str, Any]]:
    if not previous:
        return {}

    index: dict[str, dict[str, Any]] = {}
    for anchor in previous.get("anchors", []):
        key = str(anchor.get("anchor_key") or "").strip().lower()
        if key:
            index[key] = anchor
    return index


def matrix_identity_maps(
    matrix: dict[str, Any],
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    by_id: dict[str, dict[str, Any]] = {}
    by_doi: dict[str, dict[str, Any]] = {}

    for p in matrix.get("papers", []):
        evidence = p.get("evidence", {}).get("paper", {})
        pid = str(p.get("paper_id") or "").strip()
        title = str(
            evidence.get("title")
            or p.get("filename")
            or ""
        ).strip()
        doi = str(evidence.get("doi") or "").strip()

        item = {
            "paper_id": pid,
            "title": title,
            "doi": doi,
        }

        if pid:
            by_id[pid] = item

        doi_norm = normalize_doi(doi)
        if doi_norm:
            by_doi[doi_norm] = item

    return by_id, by_doi


def core_metadata_by_doi() -> dict[str, dict[str, Any]]:
    return {
        normalize_doi(item["doi"]): item
        for item in CORE_ANCHORS
    }


def upsert_anchor(
    anchors: list[dict[str, Any]],
    positions: dict[str, int],
    *,
    anchor_key: str,
    paper_id: str,
    title: str,
    doi: str,
    target_ids: list[str],
    role: str,
    backward_required: bool,
    forward_required: bool,
) -> None:
    key = anchor_key.strip().lower()

    if key in positions:
        anchor = anchors[positions[key]]

        # The same paper may be required in both directions. Merge rather than
        # dropping one requirement because of DOI de-duplication.
        anchor["backward"]["required"] = (
            anchor["backward"]["required"]
            or backward_required
        )
        anchor["forward"]["required"] = (
            anchor["forward"]["required"]
            or forward_required
        )

        if not anchor.get("paper_id") and paper_id:
            anchor["paper_id"] = paper_id
        if not anchor.get("title") and title:
            anchor["title"] = title
        if not anchor.get("doi") and doi:
            anchor["doi"] = doi

        existing_targets = list(anchor.get("target_ids", []))
        for target_id in target_ids:
            if target_id not in existing_targets:
                existing_targets.append(target_id)
        anchor["target_ids"] = existing_targets

        roles = set(str(anchor.get("role") or "").split("+"))
        roles.add(role)
        anchor["role"] = "+".join(sorted(x for x in roles if x))
        return

    positions[key] = len(anchors)
    anchors.append({
        "anchor_key": key,
        "paper_id": paper_id,
        "title": title,
        "doi": doi,
        "target_ids": list(target_ids),
        "role": role,
        "backward": direction(backward_required),
        "forward": direction(forward_required),
    })


def init_payload(
    previous: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not AUDIT_PATH.exists():
        raise RuntimeError(
            "TARGETED_THREAT_AUDIT.json not found. "
            "Run the interim V002 audit first."
        )

    audit = load_json(AUDIT_PATH)
    matrix = load_json(MATRIX_PATH)

    if matrix.get("verification_id") != VERIFICATION_ID:
        raise RuntimeError("V002 matrix identity mismatch.")

    plan = audit.get("citation_chase_plan", {})
    by_id, by_doi = matrix_identity_maps(matrix)
    core_by_doi = core_metadata_by_doi()

    anchors: list[dict[str, Any]] = []
    positions: dict[str, int] = {}

    # ------------------------------------------------------------
    # Forward coverage comes from the CURRENT audit, not a static list.
    # ------------------------------------------------------------
    for doi_raw in plan.get("forward_core_anchor_dois", []):
        doi = str(doi_raw or "").strip()
        doi_norm = normalize_doi(doi)
        if not doi_norm:
            raise RuntimeError(
                "Audit contains an empty forward_core_anchor_doi."
            )

        matrix_item = by_doi.get(doi_norm)
        core_item = core_by_doi.get(doi_norm)

        title = ""
        paper_id = ""
        target_ids: list[str] = []
        role = "audit_forward_anchor"

        if matrix_item:
            title = matrix_item["title"]
            paper_id = matrix_item["paper_id"]
            role = "v002_full_text_forward_anchor"

        if core_item:
            if not title:
                title = str(core_item.get("title") or "")
            target_ids = list(core_item.get("target_ids", []))
            if not matrix_item:
                role = "core_protocol_anchor"

        if not title:
            # The DOI itself remains a valid auditable anchor even when the
            # matrix lacks bibliographic metadata.
            title = f"DOI {doi}"

        upsert_anchor(
            anchors,
            positions,
            anchor_key=f"doi:{doi_norm}",
            paper_id=paper_id,
            title=title,
            doi=doi,
            target_ids=target_ids,
            role=role,
            backward_required=False,
            forward_required=True,
        )

    # ------------------------------------------------------------
    # Backward coverage also comes from the CURRENT audit.
    # ------------------------------------------------------------
    for pid_raw in plan.get("backward_priority_paper_ids", []):
        pid = str(pid_raw or "").strip()

        if pid not in by_id:
            raise RuntimeError(
                f"Audit names unknown V002 paper_id: {pid}"
            )

        p = by_id[pid]
        doi_norm = normalize_doi(p["doi"])
        key = (
            f"doi:{doi_norm}"
            if doi_norm
            else f"paper:{pid}"
        )

        upsert_anchor(
            anchors,
            positions,
            anchor_key=key,
            paper_id=pid,
            title=p["title"],
            doi=p["doi"],
            target_ids=[],
            role="v002_high_threat_backward_anchor",
            backward_required=True,
            forward_required=False,
        )

    # ------------------------------------------------------------
    # Preserve previously completed provenance for matching anchors.
    # New requirements start as not_screened.
    # ------------------------------------------------------------
    previous_index = build_previous_index(previous)

    for anchor in anchors:
        old = previous_index.get(
            str(anchor["anchor_key"]).lower()
        )

        anchor["backward"] = merge_direction(
            anchor["backward"],
            old.get("backward") if old else None,
        )
        anchor["forward"] = merge_direction(
            anchor["forward"],
            old.get("forward") if old else None,
        )

        # If the tracker was previously reset to not_screened, recover only
        # branches backed by concrete repository provenance.
        for direction_name in ["backward", "forward"]:
            d = anchor[direction_name]
            if not d.get("required") or d.get("status") in SCREENED:
                continue

            restored = historical_direction(
                str(anchor["anchor_key"]),
                direction_name,
            )
            if restored:
                d.update(restored)

    resolved_named, unresolved_named = split_named_threats_by_matrix(
        list(plan.get("named_high_threat_sources", [])),
        matrix,
    )

    return {
        "schema_version": 2,
        "verification_id": VERIFICATION_ID,
        "purpose": (
            "Document protocol-bounded backward/forward citation screening. "
            "This is coverage evidence, not scientific evidence."
        ),
        "search_cutoff_date": (
            str(previous.get("search_cutoff_date") or "")
            if previous
            else ""
        ),
        "anchors": anchors,
        "resolved_named_high_threat_sources": resolved_named,
        "unresolved_named_high_threat_sources": unresolved_named,
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
        raise RuntimeError(
            "citation_coverage.json verification_id mismatch."
        )

    issues: list[str] = []
    all_required = True
    unresolved = list(
        payload.get(
            "unresolved_named_high_threat_sources",
            [],
        )
    )

    for anchor in payload.get("anchors", []):
        name = (
            anchor.get("title")
            or anchor.get("anchor_key")
        )

        for direction_name in ["backward", "forward"]:
            d = anchor.get(direction_name, {})
            status = d.get("status")

            if status not in ALLOWED:
                raise RuntimeError(
                    f"{name} {direction_name}: "
                    f"invalid status {status!r}."
                )

            if not d.get("required"):
                continue

            if status not in SCREENED:
                all_required = False
                issues.append(
                    f"NOT SCREENED: "
                    f"{name} [{direction_name}]"
                )

            if status in SCREENED:
                if not str(
                    d.get("search_date", "")
                ).strip():
                    issues.append(
                        f"MISSING search_date: "
                        f"{name} [{direction_name}]"
                    )
                    all_required = False

                if int(
                    d.get("records_screened", 0)
                ) < 0:
                    raise RuntimeError(
                        "records_screened cannot be negative."
                    )

            for item in d.get(
                "unresolved_high_threat_sources",
                [],
            ):
                unresolved.append(str(item))

    no_unresolved = (
        len([
            x
            for x in unresolved
            if str(x).strip()
        ])
        == 0
    )

    satisfied = (
        all_required
        and no_unresolved
    )

    payload["stop_condition"] = {
        "all_required_directions_screened":
            all_required,
        "no_unresolved_high_threat_source":
            no_unresolved,
        "satisfied":
            satisfied,
    }

    if not no_unresolved:
        issues.append(
            "UNRESOLVED HIGH-THREAT SOURCES remain."
        )

    return satisfied, issues


def required_direction_counts(
    payload: dict[str, Any],
) -> tuple[int, int]:
    backward = 0
    forward = 0

    for anchor in payload.get("anchors", []):
        if anchor.get("backward", {}).get("required"):
            backward += 1
        if anchor.get("forward", {}).get("required"):
            forward += 1

    return backward, forward


def render_md(
    payload: dict[str, Any],
    issues: list[str],
) -> str:
    stop = payload["stop_condition"]
    backward_count, forward_count = (
        required_direction_counts(payload)
    )

    lines = [
        "# MP1-V002 Citation Coverage Status",
        "",
        f"- **Search cutoff date:** "
        f"{payload.get('search_cutoff_date') or 'NOT SET'}",
        f"- **Required backward directions:** "
        f"{backward_count}",
        f"- **Required forward directions:** "
        f"{forward_count}",
        f"- **Total required directions:** "
        f"{backward_count + forward_count}",
        f"- **All required directions screened:** "
        f"{stop['all_required_directions_screened']}",
        f"- **No unresolved high-threat source:** "
        f"{stop['no_unresolved_high_threat_source']}",
        f"- **Stop condition satisfied:** "
        f"{stop['satisfied']}",
        "",
        "## Coverage",
        "",
        "| Anchor | Role | Backward | Forward |",
        "|---|---|---|---|",
    ]

    for a in payload.get("anchors", []):
        b = a["backward"]
        f = a["forward"]
        btxt = (
            b["status"]
            if b["required"]
            else "not required"
        )
        ftxt = (
            f["status"]
            if f["required"]
            else "not required"
        )

        lines.append(
            f"| {a['title']} | "
            f"{a['role']} | "
            f"{btxt} | {ftxt} |"
        )

    lines += [
        "",
        "## Open issues",
        "",
    ]

    lines += (
        [f"- {x}" for x in issues]
        or ["- None."]
    )

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
        description=(
            "Initialize/check MP1-V002 citation coverage."
        )
    )
    parser.add_argument(
        "--init",
        action="store_true",
    )
    parser.add_argument(
        "--check",
        action="store_true",
    )
    parser.add_argument(
        "--force",
        action="store_true",
    )
    args = parser.parse_args()

    if args.init == args.check:
        raise RuntimeError(
            "Choose exactly one of --init or --check."
        )

    OUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    if args.init:
        if (
            COVERAGE_PATH.exists()
            and not args.force
        ):
            raise RuntimeError(
                f"Coverage file already exists: "
                f"{COVERAGE_PATH}. "
                "Use --force only intentionally."
            )

        previous = (
            load_json(COVERAGE_PATH)
            if COVERAGE_PATH.exists()
            else None
        )

        payload = init_payload(
            previous=previous,
        )

        _, issues = validate_and_update(
            payload
        )

        COVERAGE_PATH.write_text(
            json.dumps(
                payload,
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        STATUS_MD.write_text(
            render_md(
                payload,
                issues,
            ),
            encoding="utf-8",
        )

        backward_count, forward_count = (
            required_direction_counts(payload)
        )

        print(
            f"[INITIALIZED] "
            f"{COVERAGE_PATH.relative_to(ROOT)}"
        )
        print(
            "[REQUIRED DIRECTIONS] "
            f"backward={backward_count} "
            f"forward={forward_count} "
            f"total={backward_count + forward_count}"
        )
        print(
            "[PRESERVED PREVIOUS COVERAGE] "
            + ("yes" if previous else "no")
        )

        restored_count = sum(
            1
            for anchor in payload.get("anchors", [])
            for direction_name in ["backward", "forward"]
            if anchor.get(direction_name, {}).get("required")
            and anchor.get(direction_name, {}).get("status") in SCREENED
        )
        print(
            f"[SCREENED DIRECTIONS PRESENT] {restored_count}"
        )
        print(
            f"[STATUS] "
            f"{STATUS_MD.relative_to(ROOT)}"
        )
        return

    if not COVERAGE_PATH.exists():
        raise RuntimeError(
            "citation_coverage.json not found. "
            "Run --init first."
        )

    payload = load_json(
        COVERAGE_PATH
    )

    satisfied, issues = validate_and_update(
        payload
    )

    COVERAGE_PATH.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    STATUS_MD.write_text(
        render_md(
            payload,
            issues,
        ),
        encoding="utf-8",
    )

    print(
        f"[STOP CONDITION] "
        f"{'SATISFIED' if satisfied else 'OPEN'}"
    )
    print(
        f"[OPEN ISSUES] {len(issues)}"
    )

    for issue in issues:
        print(f"- {issue}")

    print(
        f"[SAVED] "
        f"{STATUS_MD.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
