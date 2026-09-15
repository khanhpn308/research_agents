import csv
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from app.ingestion.citation_identity import compare_authors
from app.ingestion.normalize_citation_exports import (
    DEFAULT_CANDIDATES_PATH,
    DEFAULT_OUTPUT_DIR,
    DISCOVERY_STATUS,
    compare_with_existing,
    flag_fuzzy_titles,
    known_threat_records,
    load_existing_metadata,
    merge_metadata_records,
    normalize_doi,
    normalize_title,
    parse_csv_export,
    parse_ris_export,
    record_from_values,
    run_normalization,
    validate_round_paths,
)
from app.ingestion.screen_search_candidates import (
    ALLOWED_RECOMMENDATIONS,
    recommend,
    run_screening,
    validate_screening_paths,
)


def make_record(
    *, title: str, doi: str = "", year: str = "2025", authors: list[str] | None = None,
    source: str = "test.csv", index: int = 1, source_database: str = "test",
    citation_count: str = "", citation_label: str = "Citations", file_sha256: str = "",
    file_path: str = "",
) -> dict:
    record = record_from_values(
        title=title, doi=doi, year=year, authors=["S. Zhang"] if authors is None else authors, abstract="",
        keywords=[], publication="Journal", url="https://example.test/record", file_path="",
        source_path=Path(source), source_format="csv", record_index=index,
        source_hash=f"export-hash-{source}", source_database=source_database,
        cited_seed="Narang 2018", query="forward citations", citation_count=citation_count,
        citation_count_label=citation_label, record_identifier=str(index),
        raw_metadata={"Unknown Field": "preserved", "Citations": citation_count},
    )
    record["file_sha256"] = file_sha256
    record["file_path"] = file_path
    return record


class DoiNormalizationTests(unittest.TestCase):
    def test_all_audited_doi_forms(self) -> None:
        expected = "10.5194/ms-16-821-2025"
        values = [
            "https://doi.org/10.5194/ms-16-821-2025",
            "http://dx.doi.org/10.5194/ms-16-821-2025",
            "doi:10.5194/ms-16-821-2025",
            "DOI: 10.5194/MS-16-821-2025",
            "10.5194/ms-16-821-2025.",
        ]
        for value in values:
            with self.subTest(value=value):
                self.assertEqual(normalize_doi(value), expected)

    def test_resolver_query_and_fragment_are_removed(self) -> None:
        self.assertEqual(normalize_doi("https://doi.org/10.5194/MS-16-821-2025?foo=bar#frag"),
                         "10.5194/ms-16-821-2025")

    def test_bare_doi_query_fragment_and_legal_punctuation_are_preserved(self) -> None:
        self.assertEqual(normalize_doi("10.1000/a?foo=bar#part"), "10.1000/a?foo=bar#part")
        self.assertEqual(normalize_doi("10.1000/abc;:@+$,!_~*'"), "10.1000/abc;:@+$,!_~*'")

    def test_balanced_parentheses_and_suffix_punctuation_are_preserved(self) -> None:
        self.assertEqual(normalize_doi("10.1000/abc(def)"), "10.1000/abc(def)")
        self.assertEqual(normalize_doi("10.1000/abc;"), "10.1000/abc;")

    def test_malformed_dois_are_rejected(self) -> None:
        for value in ("", "11.1000/abc", "10.123", "https://example.org/10.1000/abc", "10.x/abc"):
            with self.subTest(value=value):
                self.assertEqual(normalize_doi(value), "")


class TitleAndAuthorNormalizationTests(unittest.TestCase):
    def test_unicode_case_whitespace_and_dash_variants(self) -> None:
        self.assertEqual(normalize_title("  A Continuum–Based\nModel. "), "a continuum-based model")
        self.assertEqual(normalize_title("CAFE\u0301—beam"), normalize_title("CAFÉ-beam"))

    def test_technical_identity_bearing_notation_is_preserved(self) -> None:
        different_pairs = [
            ("A-B layer-jamming model", "A B layer jamming model"),
            ("N+1 versus N-1 layers", "N-1 versus N+1 layers"),
            ("CO₂ and χ² stiffness", "CO2 and X2 stiffness"),
            ("α/β slip-response", "α-β slip response"),
        ]
        for left, right in different_pairs:
            with self.subTest(left=left, right=right):
                self.assertNotEqual(normalize_title(left), normalize_title(right))
        key = normalize_title("(α+β)/χ² = N−1")
        for token in ("(", "+", ")", "/", "χ²", "=", "-"):
            self.assertIn(token, key)

    def test_common_author_forms_compare_compatibly(self) -> None:
        forms = (["Zhang, Shuai"], ["Shuai Zhang"], ["Zhang S."], ["S. Zhang"])
        for left in forms:
            for right in forms:
                self.assertEqual(compare_authors(left, right), "compatible")
        self.assertEqual(compare_authors([], ["S. Zhang"]), "uncertain")
        self.assertEqual(compare_authors(["S. Zhang"], ["A. Smith"]), "incompatible")


class DeduplicationTests(unittest.TestCase):
    def test_same_doi_formatting_merges_three_provenances_without_summing_counts(self) -> None:
        records = [
            make_record(title="  LAYER–JAMMING   MODEL. ", doi="10.1000/ABC", source="google_scholar.csv",
                        source_database="Google Scholar", citation_count="21", citation_label="Cited by"),
            make_record(title="Layer-jamming model", doi="https://doi.org/10.1000/abc", source="scopus.csv",
                        source_database="Scopus", citation_count="18", citation_label="Cites", index=2),
            make_record(title="Layer-jamming model", doi="DOI: 10.1000/ABC", source="wos.csv",
                        source_database="Web of Science", citation_count="16", citation_label="Times Cited", index=3),
        ]
        candidates, events = merge_metadata_records(records)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(len(candidates[0]["provenance"]), 3)
        self.assertEqual({p["source_database"] for p in candidates[0]["provenance"]},
                         {"Google Scholar", "Scopus", "Web of Science"})
        self.assertEqual({p["citation_count_as_supplied"] for p in candidates[0]["provenance"]}, {"21", "18", "16"})
        self.assertEqual({p["citation_count_label"] for p in candidates[0]["provenance"]}, {"Cited by", "Cites", "Times Cited"})
        self.assertEqual(sum(event["type"] == "exact_normalized_doi" for event in events), 1)

    def test_missing_doi_same_title_is_review_group_not_merge(self) -> None:
        records = [
            make_record(title="Layer-jamming Beam Mechanics", authors=["Zhang, Shuai"]),
            make_record(title="Layer-jamming Beam Mechanics", authors=["S. Zhang"], index=2),
        ]
        candidates, events = merge_metadata_records(records)
        self.assertEqual(len(candidates), 2)
        group = next(event for event in events if event["type"] == "probable_duplicate_same_title")
        self.assertTrue(group["requires_human_review"])
        self.assertEqual(group["comparisons"][0]["authors"], "compatible")

    def test_missing_or_incompatible_author_year_never_auto_merges(self) -> None:
        records = [
            make_record(title="Same title", authors=[], year=""),
            make_record(title="Same title", authors=["A. Smith"], year="2024", index=2),
            make_record(title="Same title", authors=["S. Zhang"], year="2025", index=3),
        ]
        candidates, _ = merge_metadata_records(records)
        self.assertEqual(len(candidates), 3)

    def test_same_title_different_doi_is_conflict_not_merge(self) -> None:
        candidates, events = merge_metadata_records([
            make_record(title="Same title", doi="10.1000/one"),
            make_record(title="Same title", doi="10.1000/two", index=2),
        ])
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(candidate["requires_human_review"] for candidate in candidates))
        self.assertTrue(any(event["type"] == "same_title_conflicting_doi" for event in events))

    def test_same_doi_conflicting_title_and_year_are_flagged(self) -> None:
        candidates, _ = merge_metadata_records([
            make_record(title="Continuum beam", doi="10.1000/same", year="2025"),
            make_record(title="Different work", doi="10.1000/same", year="2026", index=2),
        ])
        self.assertEqual(len(candidates), 2)
        for candidate in candidates:
            types = {item["type"] for item in candidate["identity_conflicts"]}
            self.assertEqual(types, {"same_doi_conflicting_title", "same_doi_conflicting_year"})
            self.assertTrue(candidate["requires_human_review"])

    def test_same_doi_uncertain_authors_requires_review_not_merge(self) -> None:
        candidates, events = merge_metadata_records([
            make_record(title="Same work", doi="10.1000/author", authors=[]),
            make_record(title="Same work", doi="10.1000/author", authors=["S. Zhang"], index=2),
        ])
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(candidate["requires_human_review"] for candidate in candidates))
        self.assertTrue(any(event["type"] == "same_doi_bibliographic_conflict" for event in events))
        self.assertTrue(all(
            any(conflict["type"] == "same_doi_uncertain_authors" for conflict in candidate["identity_conflicts"])
            for candidate in candidates
        ))

    def test_same_doi_preserves_multiple_pdf_variants(self) -> None:
        candidates, _ = merge_metadata_records([
            make_record(title="Same work", doi="10.1000/same", file_sha256="a" * 64, file_path="a.pdf"),
            make_record(title="Same work", doi="10.1000/same", file_sha256="b" * 64, file_path="b.pdf", index=2),
        ])
        self.assertEqual(len(candidates), 1)
        self.assertEqual({item["sha256"] for item in candidates[0]["file_variants"]}, {"a" * 64, "b" * 64})

    def test_same_hash_conflicting_identity_is_never_silently_merged(self) -> None:
        digest = "c" * 64
        candidates, events = merge_metadata_records([
            make_record(title="First work", doi="10.1000/one", file_sha256=digest),
            make_record(title="Second work", doi="10.1000/two", file_sha256=digest, index=2),
        ])
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(candidate["requires_human_review"] for candidate in candidates))
        self.assertTrue(any(event["type"] == "same_file_hash_conflicting_metadata" for event in events))

    def test_input_order_does_not_change_identity(self) -> None:
        records = [
            make_record(title="Same work", doi="10.1000/order", source="b.csv", index=2),
            make_record(title="Same work", doi="10.1000/order", source="a.csv", index=1),
            make_record(title="No DOI", source="c.csv", index=3),
        ]
        forward, _ = merge_metadata_records(records)
        reverse, _ = merge_metadata_records(list(reversed(records)))
        self.assertEqual(json.dumps(forward, sort_keys=True), json.dumps(reverse, sort_keys=True))

    def test_fuzzy_title_never_automatically_merges(self) -> None:
        candidates, _ = merge_metadata_records([
            make_record(title="A continuum based model for a layer jamming beam"),
            make_record(title="A continuum based model of a layer jamming beam", index=2),
        ])
        flag_fuzzy_titles(candidates)
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(candidate["fuzzy_title_review"] for candidate in candidates))


class ParserAndExistingCorpusTests(unittest.TestCase):
    def test_realistic_csv_aliases_and_unknown_columns_are_preserved(self) -> None:
        variants = [
            ("Source title", "Cited by", "ArticleURL", "Author Full Names"),
            ("Publication", "Times Cited", "DOI Link", "Authors"),
            ("Journal", "Cites", "URL", "Author(s)"),
            ("Publication Name", "Citations", "Link", "Author"),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, (publication, citations, url, authors) in enumerate(variants):
                path = root / f"scopus_{index}.csv"
                headers = ["Title", "DOI", "Publication Year", publication, citations, url, authors, "Custom Field"]
                with path.open("w", encoding="utf-8", newline="") as handle:
                    writer = csv.DictWriter(handle, fieldnames=headers)
                    writer.writeheader()
                    writer.writerow({"Title": "A model", "DOI": "10.1000/csv", "Publication Year": "2025",
                                     publication: "Mechanism Science", citations: "7",
                                     url: "https://example.test/article", authors: "S. Zhang; A. Li",
                                     "Custom Field": "keep me"})
                record = parse_csv_export(path)[0]
                self.assertEqual(record["publication"], "Mechanism Science")
                self.assertEqual(record["provenance"]["citation_count_as_supplied"], "7")
                self.assertEqual(record["provenance"]["citation_count_label"], citations)
                self.assertEqual(record["provenance"]["raw_metadata"]["Custom Field"], "keep me")
                self.assertEqual(record["provenance"]["source_database"], "Scopus")

    def test_file_hash_exists_only_for_an_actual_local_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            actual = root / "paper.pdf"
            actual.write_bytes(b"synthetic-not-a-real-paper")
            export = root / "export.csv"
            with export.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["Title", "File Path"])
                writer.writeheader()
                writer.writerow({"Title": "Actual file", "File Path": "paper.pdf"})
                writer.writerow({"Title": "Missing file", "File Path": "missing.pdf"})
            records = parse_csv_export(export)
        self.assertEqual(records[0]["file_sha256"], hashlib.sha256(b"synthetic-not-a-real-paper").hexdigest())
        self.assertEqual(records[1]["file_sha256"], "")

    def test_ris_fields_author_dedup_and_remote_link(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "wos_export.ris"
            path.write_text(
                "TY  - JOUR\nT1  - A layer-jamming model\nAU  - Zhang, Shuai\nAU  - Zhang, Song\n"
                "A1  - Shuai Zhang\nA1  - Song Zhang\n"
                "Y1  - 2025/01/01\nDO  - 10.1000/RIS\nL1  - https://example.test/paper.pdf\n"
                "JO  - Journal A\nJF  - Journal Full Name\nT2  - Fallback Journal\nER  -\n",
                encoding="utf-8",
            )
            record = parse_ris_export(path)[0]
        self.assertEqual(record["normalized_doi"], "10.1000/ris")
        self.assertEqual(record["publication"], "Journal A")
        self.assertEqual(record["authors"], ["Zhang, Shuai", "Zhang, Song"])
        self.assertEqual(record["url"], "https://example.test/paper.pdf")
        self.assertEqual(record["file_path"], "")
        self.assertEqual(record["provenance"]["raw_metadata"]["JF"], ["Journal Full Name"])

    def test_registry_blank_doi_is_filled_from_evidence_for_matching(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            registry = root / "paper_registry.json"
            evidence = root / "evidence"
            evidence.mkdir()
            registry.write_text(json.dumps({"papers": [{"paper_id": "P-1", "title": "", "doi": ""}]}), encoding="utf-8")
            (evidence / "P-1.json").write_text(json.dumps({
                "source": {"paper_id": "P-1", "sha256": "d" * 64},
                "paper": {"title": "Evidence title", "doi": "10.1000/evidence", "year": 2025,
                          "authors": ["S. Zhang"]},
            }), encoding="utf-8")
            existing = load_existing_metadata(registry, evidence)
            candidates, _ = merge_metadata_records([make_record(title="Other formatting", doi="10.1000/EVIDENCE")])
            compare_with_existing(candidates, existing)
        self.assertEqual(candidates[0]["existing_corpus_matches"][0]["paper_id"], "P-1")
        self.assertEqual(candidates[0]["existing_corpus_matches"][0]["match_type"], "exact_normalized_doi")


class ScreeningTests(unittest.TestCase):
    def test_all_known_threats_are_available_and_not_below_uncertain(self) -> None:
        records = known_threat_records()
        self.assertEqual({record["normalized_doi"] for record in records}, {
            "10.5194/ms-16-821-2025", "10.1007/s11465-025-0843-5", "10.1109/tcst.2026.3690756",
        })
        candidates, _ = merge_metadata_records(records)
        for candidate in candidates:
            result = recommend(candidate)
            self.assertIn(result["recommendation"], {"include", "uncertain"})
            self.assertTrue(result["known_threat"])
            self.assertEqual(result["candidate_status"], DISCOVERY_STATUS)
            self.assertFalse(result["scientific_evidence"])

    def test_layer_jamming_title_alone_is_not_include(self) -> None:
        candidate, _ = merge_metadata_records([make_record(title="Layer jamming structures")])
        self.assertEqual(recommend(candidate[0])["recommendation"], "uncertain")

    def test_incomplete_metadata_is_uncertain_not_excluded(self) -> None:
        candidate, _ = merge_metadata_records([make_record(title="Some unrelated mechanical topic")])
        result = recommend(candidate[0])
        self.assertEqual(result["recommendation"], "uncertain")
        self.assertFalse(result["metadata_complete_for_screening"])
        self.assertEqual(result["screening_confidence"], "low")

    def test_vocabulary_and_allowed_recommendations(self) -> None:
        title = ("Layer jamming continuum formulation with homogenization, effective representation, "
                 "constitutive formulation, reduced-order macroscopic partial interaction, interlayer slip, "
                 "friction, shear-lag, layer-count scaling, model validity and breakdown limits")
        candidate, _ = merge_metadata_records([make_record(title=title)])
        result = recommend(candidate[0])
        self.assertEqual(result["recommendation"], "include")
        self.assertTrue({"layer_jamming", "reduced_representation", "slip_friction", "layer_scaling", "validity_limits"}
                        <= set(result["matched_concepts"]))
        self.assertEqual(ALLOWED_RECOMMENDATIONS, {"include", "uncertain", "deprioritize", "exclude"})


class IsolationAndMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        self.raw = self.root / "data/search_exports/D1-V002/raw"
        self.output = self.root / "outputs/search_results/D1-V002"
        self.manifest = self.root / "data/search_exports/D1-V002/round_manifest.json"
        self.registry = self.root / "data/paper_registry.json"
        self.evidence = self.root / "data/evidence"
        self.raw.mkdir(parents=True)
        self.output.mkdir(parents=True)
        self.evidence.mkdir(parents=True)
        self.registry.parent.mkdir(parents=True, exist_ok=True)
        self.registry.write_text(json.dumps({"schema_version": 1, "papers": []}), encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _run_synthetic(self) -> tuple[dict, dict]:
        export = self.raw / "google_scholar.csv"
        with export.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["Title", "DOI", "Year", "Authors", "Cited by"])
            writer.writeheader()
            writer.writerow({"Title": "A continuum-based model for a layer jamming beam",
                             "DOI": "10.5194/ms-16-821-2025", "Year": "2025",
                             "Authors": "Zhang, Shuai", "Cited by": "3"})
        registry_before = hashlib.sha256(self.registry.read_bytes()).hexdigest()
        export_before = hashlib.sha256(export.read_bytes()).hexdigest()
        payload = run_normalization(
            verification_id="D1-V002", input_dir=self.raw, output_dir=self.output,
            manifest_path=self.manifest, registry_path=self.registry, evidence_dir=self.evidence,
            enforce_production_paths=False,
        )
        screened = run_screening(
            verification_id="D1-V002", candidates_path=self.output / "normalized_candidates.json",
            output_dir=self.output, enforce_production_paths=False,
        )
        self.assertEqual(hashlib.sha256(self.registry.read_bytes()).hexdigest(), registry_before)
        self.assertEqual(hashlib.sha256(export.read_bytes()).hexdigest(), export_before)
        return payload, screened

    def test_output_isolation_known_threat_status_and_registry_protection(self) -> None:
        payload, screened = self._run_synthetic()
        self.assertEqual(set(path.name for path in self.output.iterdir()), {
            "normalized_candidates.json", "normalized_candidates.csv", "deduplication_report.json",
            "metadata_screening_recommendations.json", "metadata_screening_recommendations.csv",
        })
        self.assertFalse((self.root / "outputs/search_results/normalized_candidates.json").exists())
        self.assertFalse((self.root / "outputs/verification/D1-V001").exists())
        self.assertFalse((self.root / "outputs/discovery_snapshot").exists())
        threat = next(item for item in payload["candidates"] if item["normalized_doi"] == "10.5194/ms-16-821-2025")
        self.assertEqual(threat["status"], DISCOVERY_STATUS)
        self.assertGreaterEqual(len(threat["provenance"]), 2)
        self.assertTrue(all(item["recommendation"] in ALLOWED_RECOMMENDATIONS for item in screened["recommendations"]))
        self.assertTrue(all(item["metadata_only"] and not item["scientific_evidence"] for item in screened["recommendations"]))

    def test_exact_path_confinement_and_historical_protection(self) -> None:
        validate_round_paths(input_dir=self.raw, output_dir=self.output, manifest_path=self.manifest,
                             repository_root=self.root)
        bad_paths = [
            (self.raw, self.root / "outputs/search_results", self.manifest),
            (self.raw, self.root / "outputs/verification/D1-V001", self.manifest),
            (self.raw, self.root / "outputs/discovery_snapshot/D1-V002", self.manifest),
            (self.raw, self.output, self.root / "data/search_exports/D1-V001/round_manifest.json"),
            (self.root.parent / "outside/raw", self.output, self.manifest),
        ]
        for raw, output, manifest in bad_paths:
            with self.subTest(output=output, manifest=manifest):
                with self.assertRaises(RuntimeError):
                    validate_round_paths(input_dir=raw, output_dir=output, manifest_path=manifest,
                                         repository_root=self.root)

    def test_production_screening_candidate_path_is_exact(self) -> None:
        validate_screening_paths(candidates_path=DEFAULT_CANDIDATES_PATH, output_dir=DEFAULT_OUTPUT_DIR)
        with self.assertRaises(RuntimeError):
            validate_screening_paths(
                candidates_path=DEFAULT_CANDIDATES_PATH.parent.parent / "D1-V001/normalized_candidates.json",
                output_dir=DEFAULT_OUTPUT_DIR,
            )

    def test_symlink_escape_is_rejected(self) -> None:
        escape = self.root / "escape"
        escape.mkdir()
        self.output.rmdir()
        os.symlink(escape, self.output, target_is_directory=True)
        with self.assertRaises(RuntimeError):
            validate_round_paths(input_dir=self.raw, output_dir=self.output, manifest_path=self.manifest,
                                 repository_root=self.root)

    def test_wrong_round_rejected_without_writes(self) -> None:
        with self.assertRaises(RuntimeError):
            run_normalization(
                verification_id="D1-V001", input_dir=self.raw, output_dir=self.output,
                manifest_path=self.manifest, registry_path=self.registry, evidence_dir=self.evidence,
                enforce_production_paths=False,
            )
        self.assertEqual(list(self.output.iterdir()), [])

    def test_wrong_manifest_identity_is_rejected_before_outputs(self) -> None:
        self.manifest.write_text(json.dumps({
            "verification_id": "D1-V001", "subject_direction_id": "D1",
            "subject_title": "historical", "baseline_verification_id": "none",
        }), encoding="utf-8")
        with self.assertRaises(RuntimeError):
            run_normalization(
                verification_id="D1-V002", input_dir=self.raw, output_dir=self.output,
                manifest_path=self.manifest, registry_path=self.registry, evidence_dir=self.evidence,
                enforce_production_paths=False,
            )
        self.assertEqual(list(self.output.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
