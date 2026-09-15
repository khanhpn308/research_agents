import csv
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from app.ingestion.normalize_citation_exports import (
    DISCOVERY_STATUS,
    flag_fuzzy_titles,
    merge_metadata_records,
    normalize_doi,
    normalize_title,
    parse_ris_export,
    record_from_values,
    run_normalization,
)
from app.ingestion.screen_search_candidates import run_screening


def make_record(
    *,
    title: str,
    doi: str = "",
    year: str = "2025",
    authors: list[str] | None = None,
    source: str = "test.csv",
    index: int = 1,
) -> dict:
    return record_from_values(
        title=title,
        doi=doi,
        year=year,
        authors=authors or ["A. Zhang"],
        abstract="",
        keywords=[],
        url="",
        file_path="",
        source_path=Path(source),
        source_format="csv",
        record_index=index,
        source_hash="abc123",
    )


class NormalizationTests(unittest.TestCase):
    def test_doi_normalization(self) -> None:
        self.assertEqual(
            normalize_doi(" DOI: https://doi.org/10.5194/MS-16-821-2025. "),
            "10.5194/ms-16-821-2025",
        )

    def test_title_normalization(self) -> None:
        self.assertEqual(
            normalize_title("  A Continuum–Based Model: for a Layer-Jamming Beam! "),
            "a continuum based model for a layer jamming beam",
        )

    def test_exact_doi_duplicates_merge_and_preserve_provenance(self) -> None:
        records = [
            make_record(title="First title", doi="10.1000/ABC", source="scopus.csv", index=1),
            make_record(title="First Title", doi="https://doi.org/10.1000/abc", source="wos.ris", index=2),
        ]
        candidates, events = merge_metadata_records(records)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(len(candidates[0]["provenance"]), 2)
        self.assertEqual(candidates[0]["merge_reasons"], ["exact_normalized_doi"])
        self.assertEqual(len(events), 1)

    def test_same_normalized_title_without_doi_merges_when_metadata_compatible(self) -> None:
        records = [
            make_record(title="Layer-Jamming Beam Mechanics", authors=["Y. Zhang"]),
            make_record(title="Layer jamming beam mechanics", authors=["Yeman Zhang"], index=2),
        ]
        candidates, _ = merge_metadata_records(records)
        self.assertEqual(len(candidates), 1)
        self.assertIn("exact_normalized_title_compatible_metadata", candidates[0]["merge_reasons"])

    def test_conflicting_doi_and_title_cases_are_flagged(self) -> None:
        same_doi = [
            make_record(title="Continuum layer jamming", doi="10.1000/same"),
            make_record(title="Unrelated conflicting title", doi="10.1000/same", index=2),
        ]
        candidates, _ = merge_metadata_records(same_doi)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["identity_conflicts"][0]["type"], "same_doi_conflicting_title")

        same_title = [
            make_record(title="Same title", doi="10.1000/one"),
            make_record(title="Same title", doi="10.1000/two", index=2),
        ]
        candidates, _ = merge_metadata_records(same_title)
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(item["identity_conflicts"] for item in candidates))

    def test_fuzzy_titles_are_flagged_but_not_merged(self) -> None:
        records = [
            make_record(title="A continuum based model for a layer jamming beam"),
            make_record(title="A continuum based model of a layer jamming beam", index=2),
        ]
        candidates, _ = merge_metadata_records(records)
        flag_fuzzy_titles(candidates)
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(item["fuzzy_title_review"] for item in candidates))

    def test_ris_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "export.ris"
            path.write_text(
                "TY  - JOUR\nTI  - A layer jamming model\nAU  - Zhang, A.\nPY  - 2025\n"
                "DO  - 10.1000/RIS\nER  -\n",
                encoding="utf-8",
            )
            records = parse_ris_export(path)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["normalized_doi"], "10.1000/ris")


class IsolationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.raw = self.root / "data/search_exports/D1-V002/raw"
        self.output = self.root / "outputs/search_results/D1-V002"
        self.manifest = self.root / "data/search_exports/D1-V002/round_manifest.json"
        self.registry = self.root / "data/paper_registry.json"
        self.evidence = self.root / "data/evidence"
        self.raw.mkdir(parents=True)
        self.output.mkdir(parents=True)
        self.evidence.mkdir(parents=True)
        self.registry.parent.mkdir(parents=True, exist_ok=True)
        self.registry.write_text(
            json.dumps({"schema_version": 1, "paper_count": 0, "papers": []}),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_provenance_registry_protection_and_output_isolation(self) -> None:
        export = self.raw / "citations.csv"
        with export.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["Title", "DOI", "Year", "Authors"])
            writer.writeheader()
            writer.writerow(
                {
                    "Title": "A continuum-based model for a layer jamming beam",
                    "DOI": "10.5194/ms-16-821-2025",
                    "Year": "2025",
                    "Authors": "Zhang, A.",
                }
            )
        registry_before = hashlib.sha256(self.registry.read_bytes()).hexdigest()
        export_before = hashlib.sha256(export.read_bytes()).hexdigest()
        payload = run_normalization(
            verification_id="D1-V002",
            input_dir=self.raw,
            output_dir=self.output,
            manifest_path=self.manifest,
            registry_path=self.registry,
            evidence_dir=self.evidence,
        )
        self.assertEqual(hashlib.sha256(self.registry.read_bytes()).hexdigest(), registry_before)
        self.assertEqual(hashlib.sha256(export.read_bytes()).hexdigest(), export_before)
        self.assertTrue((self.output / "normalized_candidates.json").exists())
        self.assertTrue((self.output / "normalized_candidates.csv").exists())
        self.assertTrue((self.output / "deduplication_report.json").exists())
        self.assertFalse((self.root / "outputs/search_results/normalized_candidates.json").exists())
        threat = next(item for item in payload["candidates"] if item["normalized_doi"] == "10.5194/ms-16-821-2025")
        self.assertEqual(threat["status"], DISCOVERY_STATUS)
        self.assertFalse(threat["scientific_evidence"])
        self.assertGreaterEqual(len(threat["provenance"]), 2)

        screened = run_screening(
            verification_id="D1-V002",
            candidates_path=self.output / "normalized_candidates.json",
            output_dir=self.output,
        )
        self.assertEqual(hashlib.sha256(self.registry.read_bytes()).hexdigest(), registry_before)
        self.assertTrue(all(item["human_approval_required"] for item in screened["recommendations"]))
        self.assertTrue(all(not item["scientific_evidence"] for item in screened["recommendations"]))

    def test_wrong_round_or_global_output_is_rejected(self) -> None:
        with self.assertRaises(RuntimeError):
            run_normalization(
                verification_id="D1-V001",
                input_dir=self.raw,
                output_dir=self.output,
                manifest_path=self.manifest,
                registry_path=self.registry,
                evidence_dir=self.evidence,
            )
        with self.assertRaises(RuntimeError):
            run_normalization(
                verification_id="D1-V002",
                input_dir=self.raw,
                output_dir=self.root / "outputs/search_results",
                manifest_path=self.manifest,
                registry_path=self.registry,
                evidence_dir=self.evidence,
            )


if __name__ == "__main__":
    unittest.main()
