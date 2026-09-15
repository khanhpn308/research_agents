"""CSV/RIS parsing with occurrence-level provenance preservation."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlsplit

from app.ingestion.citation_identity import compare_authors, normalize_author, normalize_doi, normalize_title, normalize_year, split_multi_value


CSV_ALIASES = {
    "title": ("title", "document title", "article title", "ti"),
    "doi": ("doi", "digital object identifier", "di"),
    "doi_link": ("doi link", "doi url"),
    "year": ("year", "publication year", "publication date", "py"),
    "authors": ("authors", "author", "author(s)", "author full names", "authors full name", "au"),
    "abstract": ("abstract", "description", "ab"),
    "keywords": ("keywords", "author keywords", "index keywords", "keyword", "kw"),
    "publication": ("source title", "publication", "journal", "publication name", "publication title", "source", "journal title"),
    "url": ("url", "link", "source url", "articleurl", "article url", "record url", "ur"),
    "file_path": ("file", "file path", "file_path", "pdf", "pdf path", "local file"),
    "citation_count": (
        "cited by", "times cited", "times cited, all databases", "times cited, wos core",
        "times cited, wos core collection", "cites", "citations", "citation count", "tc",
    ),
    "source_database": ("database", "source database", "export source", "database name"),
    "cited_seed": ("cited seed", "seed paper", "forward citation seed"),
    "query": ("query", "search query"),
    "record_identifier": ("eid", "ut", "accession number", "record id", "result number", "cluster id"),
}


def _key(value: Any) -> str:
    return " ".join(str(value or "").strip().casefold().replace("_", " ").split())


def _lookup(row: dict[str, Any], field: str) -> tuple[str, str]:
    mapped = {_key(key): (str(key), value) for key, value in row.items()}
    for alias in CSV_ALIASES[field]:
        hit = mapped.get(_key(alias))
        if hit and hit[1] not in (None, ""):
            return str(hit[1]).strip(), hit[0]
    return "", ""


def infer_source_database(path: Path) -> str:
    token = _key(path.stem).replace(" ", "_")
    if "scopus" in token:
        return "Scopus"
    if any(item in token for item in ("web_of_science", "webofscience", "wos")):
        return "Web of Science"
    if any(item in token for item in ("google_scholar", "googlescholar", "scholar")):
        return "Google Scholar"
    if any(item in token for item in ("publish_or_perish", "publishorperish", "pop")):
        return "Publish or Perish"
    return ""


def _is_remote_url(value: str) -> bool:
    parsed = urlsplit(value.strip())
    return parsed.scheme.casefold() in {"http", "https"} and bool(parsed.netloc)


def _actual_file(raw_path: str, source_path: Path, sha256_file: Callable[[Path], str]) -> tuple[str, str]:
    if not raw_path or _is_remote_url(raw_path):
        return "", ""
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = source_path.parent / candidate
    try:
        resolved = candidate.resolve()
    except OSError:
        return "", str(candidate)
    if not resolved.is_file():
        return "", str(resolved)
    return sha256_file(resolved), str(resolved)


def record_from_values(
    *, title: str, doi: str, year: str, authors: list[str], abstract: str,
    keywords: list[str], url: str, file_path: str, source_path: Path | None,
    source_format: str, record_index: int, source_hash: str,
    sha256_file: Callable[[Path], str], publication: str = "",
    source_database: str = "", cited_seed: str = "", query: str = "",
    citation_count: str = "", citation_count_label: str = "",
    record_identifier: str = "", raw_metadata: dict[str, Any] | None = None,
    document_type: str = "",
) -> dict:
    actual_hash = ""
    resolved_file = ""
    if source_path is not None:
        actual_hash, resolved_file = _actual_file(file_path, source_path, sha256_file)
    supplied_doi = doi.strip()
    provenance = {
        "source_database": source_database or (infer_source_database(source_path) if source_path else "known threats"),
        "cited_seed": cited_seed,
        "source_file": str(source_path) if source_path else "known_threats",
        "source_file_sha256": source_hash,
        "source_format": source_format,
        "record_identifier": record_identifier or str(record_index),
        "record_index": record_index,
        "query": query,
        "publication": publication.strip(),
        "url": url.strip(),
        "doi_as_supplied": supplied_doi,
        "citation_count_as_supplied": citation_count,
        "citation_count_label": citation_count_label,
        "year_as_supplied": str(year or "").strip(),
        "raw_metadata": raw_metadata or {},
    }
    return {
        "title": title.strip(), "normalized_title": normalize_title(title),
        "doi": supplied_doi, "normalized_doi": normalize_doi(supplied_doi),
        "year": normalize_year(year), "authors": [item.strip() for item in authors if item.strip()],
        "abstract": abstract.strip(), "keywords": [item.strip() for item in keywords if item.strip()],
        "publication": publication.strip(), "document_type": document_type.strip(),
        "url": url.strip(), "file_path": resolved_file, "file_sha256": actual_hash,
        "provenance": provenance,
    }


def parse_csv_export(path: Path, sha256_file: Callable[[Path], str]) -> list[dict]:
    source_hash = sha256_file(path)
    records: list[dict] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise RuntimeError(f"CSV has no header: {path}")
        for index, row in enumerate(reader, start=1):
            values = {field: _lookup(row, field) for field in CSV_ALIASES}
            doi = values["doi"][0]
            if not doi and values["doi_link"][0]:
                doi = values["doi_link"][0]
            url = values["url"][0] or values["doi_link"][0]
            records.append(record_from_values(
                title=values["title"][0], doi=doi, year=values["year"][0],
                authors=split_multi_value(values["authors"][0]), abstract=values["abstract"][0],
                keywords=split_multi_value(values["keywords"][0]), publication=values["publication"][0],
                url=url, file_path=values["file_path"][0], source_path=path, source_format="csv",
                record_index=index, source_hash=source_hash, sha256_file=sha256_file,
                source_database=values["source_database"][0], cited_seed=values["cited_seed"][0],
                query=values["query"][0], citation_count=values["citation_count"][0],
                citation_count_label=values["citation_count"][1], record_identifier=values["record_identifier"][0],
                raw_metadata={str(key): value for key, value in row.items()},
            ))
    return records


def _ris_entries(path: Path) -> list[dict[str, list[str]]]:
    entries: list[dict[str, list[str]]] = []
    current: dict[str, list[str]] = {}
    last_tag = ""
    for raw_line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        match = re.match(r"^([A-Z0-9]{2})\s{0,2}-\s?(.*)$", raw_line)
        if match:
            tag, value = match.groups()
            if tag == "TY" and current:
                entries.append(current)
                current = {}
            current.setdefault(tag, []).append(value.strip())
            last_tag = tag
            if tag == "ER":
                entries.append(current)
                current = {}
                last_tag = ""
        elif raw_line.startswith((" ", "\t")) and last_tag and current.get(last_tag):
            current[last_tag][-1] = f"{current[last_tag][-1]} {raw_line.strip()}".strip()
    if current:
        entries.append(current)
    return entries


def _first(entry: dict[str, list[str]], *tags: str) -> str:
    for tag in tags:
        if entry.get(tag):
            return entry[tag][0]
    return ""


def _unique_authors(entry: dict[str, list[str]]) -> list[str]:
    authors: list[str] = []
    seen: set[str] = set()
    primary = entry.get("AU", [])
    alternate = entry.get("A1", [])
    for author in primary:
        key = normalize_author(author)
        if key and key not in seen:
            authors.append(author)
            seen.add(key)
    for index, author in enumerate(alternate):
        key = normalize_author(author)
        same_position = index < len(primary) and compare_authors([primary[index]], [author]) == "compatible"
        if key and key not in seen and not same_position:
            authors.append(author)
            seen.add(key)
    return authors


def parse_ris_export(path: Path, sha256_file: Callable[[Path], str]) -> list[dict]:
    source_hash = sha256_file(path)
    records: list[dict] = []
    for index, entry in enumerate(_ris_entries(path), start=1):
        url = _first(entry, "UR")
        link = _first(entry, "L1", "L2")
        if not url and _is_remote_url(link):
            url = link
        local_file = "" if _is_remote_url(link) else link
        publication = _first(entry, "JO", "JF", "T2")
        citation_count = _first(entry, "TC")
        records.append(record_from_values(
            title=_first(entry, "TI", "T1", "CT"), doi=_first(entry, "DO", "DI"),
            year=_first(entry, "PY", "Y1", "DA"), authors=_unique_authors(entry),
            abstract=_first(entry, "AB", "N2"), keywords=entry.get("KW", []),
            publication=publication, url=url, file_path=local_file, source_path=path,
            source_format="ris", record_index=index, source_hash=source_hash, sha256_file=sha256_file,
            citation_count=citation_count, citation_count_label="TC" if citation_count else "",
            record_identifier=_first(entry, "ID", "AN", "UT"), raw_metadata=entry,
            document_type=_first(entry, "TY"),
        ))
    return records
