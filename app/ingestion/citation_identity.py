"""Conservative bibliographic normalization and identity comparison.

The functions in this module operate on metadata only.  They deliberately
prefer a human-review group over an automatic merge when identity is not
anchored by a normalized DOI or a non-conflicting local-file hash.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit


DISCOVERY_STATUS = "discovered but not yet verified"
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
RESOLVER_HOSTS = {"doi.org", "www.doi.org", "dx.doi.org", "www.dx.doi.org"}
_DASH_TRANSLATION = str.maketrans({
    "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-", "\u2014": "-", "\u2212": "-"
})


def _strip_terminal_citation_period(text: str) -> str:
    """Remove one prose/citation full stop, never a run of DOI punctuation."""
    if text.endswith(".") and not text.endswith("..") and len(text) > 1:
        return text[:-1]
    return text


def normalize_doi(value: Any) -> str:
    """Return a conservative canonical DOI, or an empty string if malformed.

    Query and fragment components are removed only for recognized DOI resolver
    URLs.  For a bare DOI they are valid suffix characters and are preserved.
    """
    text = unicodedata.normalize("NFC", str(value or "")).strip()
    text = re.sub(r"^doi\s*:\s*", "", text, flags=re.IGNORECASE)

    parsed = urlsplit(text)
    if parsed.scheme.casefold() in {"http", "https"} and parsed.hostname and parsed.hostname.casefold() in RESOLVER_HOSTS:
        text = unquote(parsed.path.lstrip("/"))
    elif parsed.scheme or parsed.netloc:
        return ""

    # Angle brackets are common citation wrappers and cannot be part of a DOI
    # because DOI syntax excludes whitespace but otherwise remains permissive.
    if text.startswith("<") and text.endswith(">"):
        text = text[1:-1].strip()
    text = _strip_terminal_citation_period(text.strip())
    canonical = text.casefold()
    return canonical if DOI_RE.fullmatch(canonical) else ""


def normalize_title(value: Any) -> str:
    """Build a preservation-oriented exact-title identity key."""
    text = unicodedata.normalize("NFC", str(value or "")).strip()
    text = text.translate(_DASH_TRANSLATION).casefold()
    # Strip only obvious whole-title citation punctuation. Internal notation,
    # punctuation, Greek letters, and Unicode sub/superscripts remain intact.
    if len(text) >= 2 and (text[0], text[-1]) in {('"', '"'), ("'", "'"), ("“", "”"), ("‘", "’")}:
        text = text[1:-1].strip()
    text = _strip_terminal_citation_period(text)
    return " ".join(text.split())


def normalize_author(value: Any) -> str:
    text = unicodedata.normalize("NFC", str(value or "")).casefold().strip()
    text = re.sub(r"\bet\s+al\.?$", "", text).strip()
    text = re.sub(r"[^\w,]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


def split_multi_value(value: Any) -> list[str]:
    if isinstance(value, list):
        values = value
    else:
        values = re.split(r"\s*[;|]\s*", str(value or ""))
    return [str(item).strip() for item in values if str(item).strip()]


def normalize_year(value: Any) -> str:
    match = re.search(r"(?:19|20)\d{2}", str(value or ""))
    return match.group(0) if match else ""


def author_identity(value: str) -> tuple[str, str]:
    """Return a best-effort (family-name, first-initial) identity tuple."""
    normalized = normalize_author(value)
    if not normalized:
        return "", ""
    if "," in normalized:
        family, given = (part.strip() for part in normalized.split(",", 1))
        return family, given[:1]
    parts = normalized.replace(",", " ").split()
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    first, last = parts[0], parts[-1]
    # "Zhang S." uses a trailing initial; "S. Zhang" uses a leading initial.
    if len(last) == 1 and len(first) > 1:
        return first, last
    return last, first[:1]


def compare_authors(left: Iterable[str], right: Iterable[str]) -> str:
    """Return compatible, incompatible, or uncertain."""
    left_ids = [author_identity(item) for item in left]
    right_ids = [author_identity(item) for item in right]
    left_ids = [item for item in left_ids if item[0]]
    right_ids = [item for item in right_ids if item[0]]
    if not left_ids or not right_ids:
        return "uncertain"
    common_families = {family for family, _ in left_ids} & {family for family, _ in right_ids}
    if not common_families:
        return "incompatible"
    for family in common_families:
        left_initials = {initial for fam, initial in left_ids if fam == family and initial}
        right_initials = {initial for fam, initial in right_ids if fam == family and initial}
        if not left_initials or not right_initials or left_initials & right_initials:
            return "compatible"
    return "uncertain"


def compare_years(left: str, right: str) -> str:
    if not left or not right:
        return "uncertain"
    return "compatible" if left == right else "incompatible"


def metadata_comparison(left: dict, right: dict) -> dict[str, str]:
    return {
        "year": compare_years(str(left.get("year", "")), str(right.get("year", ""))),
        "authors": compare_authors(left.get("authors", []), right.get("authors", [])),
    }


def metadata_compatible(left: dict, right: dict) -> bool:
    comparison = metadata_comparison(left, right)
    return all(value == "compatible" for value in comparison.values())


def _stable_jsonish(value: Any) -> str:
    if isinstance(value, dict):
        return "{" + ",".join(f"{key}:{_stable_jsonish(value[key])}" for key in sorted(value)) + "}"
    if isinstance(value, list):
        return "[" + ",".join(_stable_jsonish(item) for item in value) + "]"
    return repr(value)


def _record_key(record: dict) -> tuple[str, ...]:
    provenance = record.get("provenance", {})
    return (
        record.get("normalized_doi", ""), record.get("normalized_title", ""),
        record.get("year", ""), record.get("file_sha256", ""),
        provenance.get("source_database", ""), provenance.get("source_file", ""),
        provenance.get("source_file_sha256", ""), str(provenance.get("record_identifier", "")),
        _stable_jsonish(provenance.get("raw_metadata", {})),
    )


def _merge_unique(values: Iterable[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for item in values:
        key = unicodedata.normalize("NFC", str(item)).casefold().strip()
        if key and key not in seen:
            result.append(str(item))
            seen.add(key)
    return sorted(result, key=lambda item: (item.casefold(), item))


def _material_doi_conflicts(records: list[dict]) -> list[dict]:
    conflicts: list[dict] = []
    titles = defaultdict(list)
    years = defaultdict(list)
    for record in records:
        if record.get("normalized_title"):
            titles[record["normalized_title"]].append(record)
        if record.get("year"):
            years[record["year"]].append(record)
    if len(titles) > 1:
        conflicts.append({"type": "same_doi_conflicting_title", "values": sorted(titles)})
    if len(years) > 1:
        conflicts.append({"type": "same_doi_conflicting_year", "values": sorted(years)})
    return conflicts


def _hash_pair_conflicts(left: dict, right: dict) -> list[str]:
    conflicts: list[str] = []
    if left.get("normalized_doi") and right.get("normalized_doi") and left["normalized_doi"] != right["normalized_doi"]:
        conflicts.append("doi")
    if left.get("normalized_title") and right.get("normalized_title") and left["normalized_title"] != right["normalized_title"]:
        conflicts.append("title")
    if left.get("year") and right.get("year") and left["year"] != right["year"]:
        conflicts.append("year")
    if compare_authors(left.get("authors", []), right.get("authors", [])) == "incompatible":
        conflicts.append("authors")
    return conflicts


def _candidate_from_cluster(records: list[dict]) -> dict:
    records = sorted(records, key=_record_key)
    dois = sorted({record["normalized_doi"] for record in records if record.get("normalized_doi")})
    titles = sorted({record["normalized_title"] for record in records if record.get("normalized_title")})
    years = sorted({record["year"] for record in records if record.get("year")})
    title_variants = sorted({record.get("title", "") for record in records if record.get("title")}, key=lambda x: (-len(x), x.casefold(), x))
    doi_variants = sorted({record.get("doi", "") for record in records if record.get("doi")}, key=str.casefold)
    provenance = sorted((record["provenance"] for record in records), key=_stable_jsonish)
    identity_basis = dois[0] if len(dois) == 1 else repr([_record_key(record) for record in records])
    stable = hashlib.sha256(identity_basis.encode("utf-8")).hexdigest()[:12]
    file_variants: list[dict] = []
    seen_variants: set[tuple[str, str]] = set()
    for record in records:
        if record.get("file_sha256") or record.get("file_path"):
            key = (record.get("file_sha256", ""), record.get("file_path", ""))
            if key not in seen_variants:
                file_variants.append({
                    "sha256": key[0], "path": key[1],
                    "source_file": record.get("provenance", {}).get("source_file", ""),
                    "record_identifier": record.get("provenance", {}).get("record_identifier", ""),
                })
                seen_variants.add(key)
    conflicts = _material_doi_conflicts(records) if len(dois) == 1 else []
    return {
        "candidate_id": f"D1V002-{stable}",
        "title": title_variants[0] if title_variants else "",
        "title_variants": title_variants,
        "normalized_title": titles[0] if len(titles) == 1 else normalize_title(title_variants[0] if title_variants else ""),
        "doi": doi_variants[0] if doi_variants else "",
        "doi_variants": doi_variants,
        "normalized_doi": dois[0] if len(dois) == 1 else "",
        "year": years[0] if len(years) == 1 else (years[0] if years else ""),
        "year_variants": years,
        "authors": _merge_unique(author for record in records for author in record.get("authors", [])),
        "abstract": max((record.get("abstract", "") for record in records), key=lambda x: (len(x), x), default=""),
        "keywords": _merge_unique(keyword for record in records for keyword in record.get("keywords", [])),
        "publication": max((record.get("publication", "") for record in records), key=lambda x: (len(x), x), default=""),
        "url": min((record.get("url", "") for record in records if record.get("url")), default=""),
        "file_path": file_variants[0]["path"] if len(file_variants) == 1 else "",
        "file_sha256": file_variants[0]["sha256"] if len(file_variants) == 1 else "",
        "file_variants": file_variants,
        "provenance": provenance,
        "merge_reasons": (["exact_normalized_doi"] if len(records) > 1 and len(dois) == 1 and all(record.get("normalized_doi") == dois[0] for record in records) else ["exact_file_sha256"] if len(records) > 1 else []),
        "identity_conflicts": conflicts,
        "probable_duplicate_groups": [],
        "existing_corpus_matches": [],
        "fuzzy_title_review": [],
        "requires_human_review": bool(conflicts),
        "status": DISCOVERY_STATUS,
        "metadata_only": True,
        "scientific_evidence": False,
    }


def merge_metadata_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Merge only strong identities and flag all weaker relations for review."""
    valid = sorted(
        [record for record in records if record.get("normalized_title") or record.get("normalized_doi")],
        key=_record_key,
    )
    invalid = [record for record in records if not record.get("normalized_title") and not record.get("normalized_doi")]
    parent = list(range(len(valid)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[max(left_root, right_root)] = min(left_root, right_root)

    doi_groups: dict[str, list[int]] = defaultdict(list)
    hash_groups: dict[str, list[int]] = defaultdict(list)
    for index, record in enumerate(valid):
        if record.get("normalized_doi"):
            doi_groups[record["normalized_doi"]].append(index)
        if record.get("file_sha256"):
            hash_groups[record["file_sha256"]].append(index)
    doi_record_conflicts: list[dict] = []
    for doi, indexes in sorted(doi_groups.items()):
        titles = {valid[index]["normalized_title"] for index in indexes if valid[index].get("normalized_title")}
        years = {valid[index]["year"] for index in indexes if valid[index].get("year")}
        author_issues = []
        for position, left in enumerate(indexes):
            for right in indexes[position + 1:]:
                comparison = compare_authors(valid[left].get("authors", []), valid[right].get("authors", []))
                if comparison != "compatible":
                    author_issues.append(comparison)
        if len(titles) <= 1 and len(years) <= 1 and not author_issues:
            for index in indexes[1:]:
                union(indexes[0], index)
            continue
        doi_record_conflicts.append({
            "type": "same_doi_bibliographic_conflict", "normalized_doi": doi,
            "titles": sorted(titles), "years": sorted(years),
            "author_comparisons_requiring_review": sorted(set(author_issues)),
            "requires_human_review": True,
        })
        # Preserve safe duplicate subgroups without allowing a missing field to
        # bridge two contradictory bibliographic records.
        subgroups: dict[tuple[str, str], list[int]] = defaultdict(list)
        for index in indexes:
            record = valid[index]
            subgroups[(record.get("normalized_title", ""), record.get("year", ""))].append(index)
        for (title, _year), subgroup in subgroups.items():
            if not title:
                continue
            for position, left in enumerate(subgroup):
                for right in subgroup[position + 1:]:
                    if compare_authors(valid[left].get("authors", []), valid[right].get("authors", [])) == "compatible":
                        union(left, right)
    hash_conflicts: list[dict] = []
    for digest, indexes in hash_groups.items():
        group_conflicts: list[dict] = []
        for pos, left in enumerate(indexes):
            for right in indexes[pos + 1:]:
                fields = _hash_pair_conflicts(valid[left], valid[right])
                if fields:
                    group_conflicts.append({"left": left, "right": right, "fields": fields})
        if group_conflicts:
            hash_conflicts.append({
                "type": "same_file_hash_conflicting_metadata", "sha256": digest,
                "fields": sorted({field for conflict in group_conflicts for field in conflict["fields"]}),
            })
        else:
            for index in indexes[1:]:
                union(indexes[0], index)

    clusters: dict[int, list[dict]] = defaultdict(list)
    for index, record in enumerate(valid):
        clusters[find(index)].append(record)
    candidates = [_candidate_from_cluster(cluster) for _, cluster in sorted(clusters.items())]
    candidates.sort(key=lambda item: item["candidate_id"])
    duplicate_candidate_ids: dict[str, list[dict]] = defaultdict(list)
    for candidate in candidates:
        duplicate_candidate_ids[candidate["candidate_id"]].append(candidate)
    for candidate_id, group in duplicate_candidate_ids.items():
        if len(group) < 2:
            continue
        for candidate in group:
            basis = _stable_jsonish({
                "candidate_id": candidate_id, "title": candidate["normalized_title"],
                "year": candidate["year"], "provenance": candidate["provenance"],
            })
            candidate["candidate_id"] = f"D1V002-{hashlib.sha256(basis.encode('utf-8')).hexdigest()[:12]}"
    candidates.sort(key=lambda item: item["candidate_id"])
    events: list[dict] = [
        {"type": "invalid_metadata", "provenance": record.get("provenance", {})}
        for record in invalid
    ]
    for candidate in candidates:
        if len(candidate["provenance"]) > 1:
            events.append({
                "type": candidate["merge_reasons"][0],
                "candidate_id": candidate["candidate_id"],
                "occurrence_count": len(candidate["provenance"]),
            })

    # Same exact title is never enough to merge. It creates a deterministic
    # review group regardless of author/year completeness.
    title_groups: dict[str, list[dict]] = defaultdict(list)
    for candidate in candidates:
        if candidate.get("normalized_title"):
            title_groups[candidate["normalized_title"]].append(candidate)
    review_group_number = 0
    for title, group in sorted(title_groups.items()):
        if len(group) < 2:
            continue
        review_group_number += 1
        group_id = f"title-review-{review_group_number:04d}"
        dois = {item["normalized_doi"] for item in group if item.get("normalized_doi")}
        group_type = "same_title_conflicting_doi" if len(dois) > 1 else "probable_duplicate_same_title"
        comparisons = []
        for pos, left in enumerate(group):
            for right in group[pos + 1:]:
                comparisons.append({
                    "left_candidate_id": left["candidate_id"],
                    "right_candidate_id": right["candidate_id"],
                    **metadata_comparison(left, right),
                })
        event = {"type": group_type, "group_id": group_id, "normalized_title": title,
                 "candidate_ids": sorted(item["candidate_id"] for item in group), "comparisons": comparisons,
                 "requires_human_review": True}
        events.append(event)
        for candidate in group:
            candidate["probable_duplicate_groups"].append(group_id)
            candidate["requires_human_review"] = True
            if group_type == "same_title_conflicting_doi":
                candidate["identity_conflicts"].append({"type": group_type, "group_id": group_id, "dois": sorted(dois)})

    for conflict in hash_conflicts:
        events.append({**conflict, "requires_human_review": True})
        for candidate in candidates:
            if any(variant.get("sha256") == conflict["sha256"] for variant in candidate["file_variants"]):
                candidate["identity_conflicts"].append(conflict)
                candidate["requires_human_review"] = True
    for conflict in doi_record_conflicts:
        events.append(conflict)
        for candidate in candidates:
            if candidate.get("normalized_doi") == conflict["normalized_doi"]:
                if len(conflict["titles"]) > 1:
                    candidate["identity_conflicts"].append({
                        "type": "same_doi_conflicting_title", "values": conflict["titles"],
                    })
                if len(conflict["years"]) > 1:
                    candidate["identity_conflicts"].append({
                        "type": "same_doi_conflicting_year", "values": conflict["years"],
                    })
                for comparison in conflict["author_comparisons_requiring_review"]:
                    candidate["identity_conflicts"].append({
                        "type": f"same_doi_{comparison}_authors",
                    })
                candidate["requires_human_review"] = True
    return candidates, events


def flag_fuzzy_titles(candidates: list[dict], threshold: float = 0.90) -> None:
    for index, left in enumerate(candidates):
        for right in candidates[index + 1:]:
            if not left.get("normalized_title") or not right.get("normalized_title"):
                continue
            if left["normalized_title"] == right["normalized_title"]:
                continue
            ratio = SequenceMatcher(None, left["normalized_title"], right["normalized_title"]).ratio()
            if ratio >= threshold:
                left["fuzzy_title_review"].append({"candidate_id": right["candidate_id"], "title": right["title"], "similarity": round(ratio, 4)})
                right["fuzzy_title_review"].append({"candidate_id": left["candidate_id"], "title": left["title"], "similarity": round(ratio, 4)})
