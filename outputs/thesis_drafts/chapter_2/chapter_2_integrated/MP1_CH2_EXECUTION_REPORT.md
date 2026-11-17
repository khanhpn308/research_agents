Ghi chú hiện hành: hotfix đã tự kiểm với giới hạn; xem HOTFIX ADDENDUM ở cuối tệp. Mọi trạng thái ở báo cáo tích hợp cũ là lịch sử trước hotfix.

# Báo cáo thực hiện tích hợp toàn Chương 2

TASK_ID: MP1-CH2-FULL-CHAPTER-INTEGRATION

STATUS: PARTIAL_WITH_FINDINGS

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED

EXECUTION_PLAN_APPROVAL: APPROVED

CONTENT_PATCH_APPROVAL: PENDING

## Trạng thái bằng chứng

VERIFIED FULL TEXT là trạng thái nguồn được kế thừa, không phải chứng nhận tái đọc toàn bộ PDF trong phiên tiếp tục. METADATA ONLY giữ nguyên mức bằng chứng. INFERENCE và PROPOSAL tiếp tục là suy luận và đề xuất. Kiểm mới trong phiên này gồm đối chiếu record nguồn, XPath/offset, coverage văn bản, OOXML, citation và hash. Hồ sơ thị giác là review của phiên trước, được liên kết bằng hash với DOCX/PDF hiện tại. Không xem lại 101 ảnh trong phiên này.

## Kết quả

```json
{
  "TASK_ID": "MP1-CH2-FULL-CHAPTER-INTEGRATION",
  "STATUS": "PARTIAL_WITH_FINDINGS",
  "WORKSPACE": "/home/khanh/projects/mechanical-research-agents",
  "BRANCH": "main",
  "HEAD": "e66bb2f2339006e763cd60687cfc24680b945d97",
  "ROOT_MODEL_REQUESTED": "GPT-6.1 Sol High",
  "ROOT_MODEL_ACTUAL": "NOT_VERIFIABLE_FROM_RUNTIME",
  "WORKERS_USED": 3,
  "WORKER_MODELS_ACTUAL": "Historical spawn configurations: gpt-6-sol/medium ×2; gpt-6-luna/medium ×1. Runtime backend not independently verified.",
  "REVIEW_AUTHORITY": "SELF_REVIEW_ONLY",
  "INDEPENDENT_ACCEPTANCE": "REQUIRED_NOT_PERFORMED",
  "HUMAN_APPROVAL": "PENDING",
  "OFFICIAL_OUTLINE": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
  "OUTLINE_SHA256": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
  "OUTLINE_COVERAGE": "65 reviewed: 52 COVERED; 10 COVERED_WITH_BOUNDARY; 3 PARTIAL_EDITORIAL",
  "SOURCE_SECTIONS": [
    "2.1",
    "2.2",
    "2.3",
    "2.4",
    "2.5",
    "2.6"
  ],
  "INPUT_BASELINES_VERIFIED": "6/6",
  "INPUT_PACKAGES_READ": "42 files in six packages; prior content review inherited; reopened for current checks as required",
  "INPUT_BODY_PARAGRAPHS": 510,
  "OUTPUT_BODY_PARAGRAPHS": 468,
  "INPUT_ALL_XML_PARAGRAPHS": 2171,
  "OUTPUT_ALL_XML_PARAGRAPHS": 2129,
  "NON_BIBLIOGRAPHIC_TOP_LEVEL_PARAGRAPHS_BEFORE_AFTER": "435/435; excludes two added headings",
  "INPUT_CLAIM_RECORDS": 913,
  "ORIGINAL_CLAIMS_MAPPED": 913,
  "OUTPUT_TRACE_RECORDS": 2859,
  "SOURCE_CLAIM_COVERAGE": "913/913 actual source records, exact original JSON; 0 final text-character coverage gaps. Does not certify primary-paper claim validity.",
  "UNEXPLAINED_CLAIM_LOSS": "0 according to preserved source/record accounting; source-level semantics not independently re-adjudicated",
  "UNAPPROVED_SCIENTIFIC_CHANGES": 0,
  "SCIENTIFIC_CLAIM_PROMOTION": 0,
  "SOURCE_CITATIONS_TOTAL": 783,
  "SOURCE_CITATION_GROUPS": 758,
  "SOURCE_LOCAL_REFERENCE_ENTRIES": 69,
  "SOURCE_UNIQUE_REFERENCES": 30,
  "OUTPUT_CITATION_OCCURRENCES": 783,
  "OUTPUT_CITATION_GROUPS": 778,
  "OUTPUT_REFERENCE_ENTRIES": 30,
  "GLOBAL_RENUMBERING_ENTRIES": 69,
  "DUPLICATE_REFERENCES_REMOVED": 39,
  "MISSING_REFERENCES": 0,
  "ORPHAN_REFERENCES": 0,
  "DOI_CONFLICTS": 0,
  "CROWLEY_RESOLUTION_STATUS": "RESOLVED_IN_CHAPTER_ONLY; chapter [19]; pp. 5477–5482",
  "INPUT_FIGURES": 1,
  "OUTPUT_FIGURES": 1,
  "INPUT_TABLES": 21,
  "OUTPUT_TABLES": 21,
  "INPUT_OMML_EQUATIONS": 19,
  "OUTPUT_OMML_EQUATIONS": 19,
  "CAPTIONS_VERIFIED": 19,
  "CROSS_REFERENCES_VERIFIED": 25,
  "MEDIA_RELATIONSHIP_STATUS": "PASS: 0 dangling relationships; media hash preserved; 421 bookmark pairs",
  "INPUT_TERMINOLOGY_RECORDS": 313,
  "OUTPUT_MASTER_TERMINOLOGY_RECORDS": 313,
  "TERMINOLOGY_CONFLICTS": 0,
  "TERMINOLOGY_ALIAS_RESOLUTIONS": 9,
  "P3_STATUS_PRESERVATION": "PRESERVED",
  "RQ_MAPPING_STATUS": "PROVISIONAL_MANY_TO_MANY",
  "HUMAN_DECISIONS_PENDING": 5,
  "DOCX_SHA256": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
  "DOCX_ZIP_XML_STATUS": "PASS;ZIPCRC;16XML/relsparts;14relationshiptargets",
  "WORD_RENDER_VALIDATION": "Inherited LibreOffice 24.2.7.2 with Math review; exact DOCX/PDF/PNG hashes verified; no new rendering",
  "RENDERED_PAGES": 101,
  "PAGES_VISUALLY_REVIEWED": 101,
  "MICROSOFT_WORD_VALIDATION": "NOT_VERIFIED",
  "BASELINES_UNCHANGED": true,
  "SOURCE_PACKAGES_UNCHANGED": "42/42 hashes match protected manifest",
  "WEP_P3_REGISTRY_UNCHANGED": true,
  "PROTECTED_FILES_CHECKED": 3080,
  "GIT_CHANGE_SCOPE": "Only four new Markdown reports; five existing chapter outputs and all pre-existing work unchanged",
  "P1_P2_UNRESOLVED": 1,
  "OTHER_OPEN_FINDINGS": 14,
  "DOCUMENTED_LIMITATIONS": "School policy; provisional RQ mapping; five scientific human decisions; inherited source locator/version/unit boundaries; anchor granularity; Microsoft Word not verified; glossary placement; restored renderer runtime not validated; 85 immutable crosswalk rows retain pre-review pending status",
  "FILES_CREATED": [
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_UNRESOLVED_ISSUES.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_7_GATE_REVIEW.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_EXECUTION_REPORT.md"
  ],
  "COMMIT_STATUS": "NOT_PERFORMED",
  "PUSH_STATUS": "NOT_PERFORMED",
  "FINAL_SELF_REVIEW_DECISION": "SELF_REVIEW_ONLY; PARTIAL_WITH_FINDINGS; Gate 1 remains PARTIAL",
  "NEXT_ACTION": "AUTHOR_REVIEW_OF_COVERAGE_PROPOSAL; THEN INDEPENDENT_FULL_CHAPTER_ACCEPTANCE",
  "EXECUTION_PLAN_APPROVAL": "APPROVED",
  "CONTENT_PATCH_APPROVAL": "PENDING",
  "RESUME_WORKERS_USED": 0,
  "RESUME_PAGES_VISUALLY_REVIEWED": 0,
  "FILES_CREATED_IN_RESUME": [
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_UNRESOLVED_ISSUES.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_7_GATE_REVIEW.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_EXECUTION_REPORT.md"
  ],
  "CROSS_REFERENCE_OCCURRENCES_OUTSIDE_CAPTION_PARAGRAPHS": 8,
  "SCIENTIFIC_CHANGES": 0,
  "SCIENTIFIC_CHANGES_IN_RESUME": 0,
  "EDITORIAL_CHANGES": {
    "historical_citation_paragraphs": 469,
    "historical_heading_text_labels": 10,
    "historical_metadata_corrections": 5,
    "historical_term_alias_labels": 9,
    "historical_auxiliary_heading_levels": 33,
    "resume_docx_edits": 0
  },
  "STRUCTURAL_CHANGES": {
    "historical_new_headings": 2,
    "historical_bibliography_entries": "69→30",
    "resume_structural_edits": 0
  },
  "GATE_1": "PARTIAL",
  "GATE_2": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_3": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_4": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_5": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_6": "PASS_WITH_DOCUMENTED_LIMITATIONS",
  "GATE_7": "PASS"
}
```
## Kết luận và bước tiếp theo

Đủ chín deliverable sau kiểm đóng gói. Gate 1 còn PARTIAL nên toàn nhiệm vụ giữ PARTIAL_WITH_FINDINGS. Đề xuất sửa nằm trong COVERAGE_PATCH_PROPOSAL.md và chưa được áp dụng. Chỉ sau phê duyệt nội dung cụ thể mới sửa DOCX/CSV. Nghiệm thu độc lập chưa thực hiện.

## Quy ước đếm và thẩm quyền

783 là lượt dẫn từng identity, không phải số nhóm ngoặc. Tách list/range làm 758 nhóm thành 778 nhưng giữ 783 lượt. 913 là record nguồn; 2.859 là row mapping/support/structure, không phải số claim độc lập. 510→468 paragraph thân và 2.171→2.129 paragraph toàn XML được giải thích bởi dedup thư mục cùng hai heading mới. Số worker và cấu hình trong báo cáo thuộc phiên trước; phiên tiếp tục không chạy worker. Không xác nhận backend mô hình từ tên cấu hình spawn.

## Kiểm mới

```json
{
  "status": "PASS",
  "pdf_page_selfchecks": "PASS",
  "original_record_set_equal": true,
  "original_record_json_equal": true,
  "input_records": 913,
  "trace_rows": 2859,
  "source_and_final_anchor_checks": 5716,
  "terminology_original_json_equal": true,
  "terminology_records": 313,
  "source_paragraph_manifest_complete": true,
  "preservation_paragraphs": 2171,
  "final_text_coverage_gaps": [],
  "covered_text_characters": 284215,
  "overlapping_text_characters": 153359,
  "overlap_boundary": "Repeated support and structural records are expected; no duplicate chapter_claim_id allowed.",
  "archive_only_records": [
    "CH2-S4-R0013-A01",
    "CH2-S4-R0092-A01",
    "CH2-S4-R0093-A01",
    "CH2-S4-R0094-A01",
    "CH2-S4-R0095-A01"
  ],
  "record_kind_counts": {
    "SCIENTIFIC_CLAIM": 931,
    "STRUCTURAL_RECORD": 1923,
    "ARCHIVAL_SUPPORT_ONLY": 5
  },
  "anchor_granularity_counts": {
    "SOURCE_EXACT_ANCHOR": 637,
    "PARAGRAPH_OR_TABLE_SCOPE": 75,
    "TABLE_ROW_SCOPE": 48,
    "PARAGRAPH_SCOPE": 136,
    "ARCHIVAL_SUPPORT_ONLY": 5,
    "SUBSECTION_SCOPE": 9,
    "PARAGRAPH_OR_EQUATION_SCOPE": 95,
    "WHOLE_PARAGRAPH": 1852,
    "NEW_STRUCTURE": 2
  },
  "immutable_outputs_verified": 5,
  "qa_exactly_matches_checkpoint": true,
  "visual_reviews_inherited": 101,
  "visual_images_hash_checked": 101,
  "images_viewed_in_resume": 0,
  "new_render_performed": false,
  "microsoft_word_validation": "NOT_VERIFIED",
  "omml_exact_c14n_source_final_checks": 19,
  "inherited_crosswalk_visual_statuses": {
    "PENDING_FINAL_RENDER_REVIEW": 85
  },
  "crosswalk_status_boundary": "The immutable CSV predates final visual review. The 7-gate report links the later inherited review evidence without rewriting CSV status."
}
```
## Bản đầu vào và source package

```json
[
  {
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATED.docx",
    "expected": "fe4fd16fbb93bcdf39708740fb90dd120563825c57ce86bd9cf36e35f841d4dd",
    "actual": "fe4fd16fbb93bcdf39708740fb90dd120563825c57ce86bd9cf36e35f841d4dd",
    "match": true
  },
  {
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATED.docx",
    "expected": "701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34",
    "actual": "701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34",
    "match": true
  },
  {
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx",
    "expected": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "actual": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "match": true
  },
  {
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx",
    "expected": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "actual": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "match": true
  },
  {
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx",
    "expected": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "actual": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "match": true
  },
  {
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx",
    "expected": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
    "actual": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
    "match": true
  },
  {
    "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf",
    "actual": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
    "expected": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
    "match": true
  }
]
```
```json
[
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_7_GATE_REVIEW.md",
    "size": 14106,
    "sha256": "d47f43eb002cebc545c4432fa4ee8245c8a78127a905e8cd8aec44211ce2867c",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_CITATION_RENUMBERING_MAP.csv",
    "size": 4451,
    "sha256": "11118450c5d744b4ae1bc7e6b39a2c74679fe13051d91e1e1b345712b0da747e",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_EXECUTION_REPORT.md",
    "size": 224319,
    "sha256": "de5781e750a45b538c9c9f744293f94da8b0b2706c512e31217cf3b66940cb5e",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATED.docx",
    "size": 45928,
    "sha256": "fe4fd16fbb93bcdf39708740fb90dd120563825c57ce86bd9cf36e35f841d4dd",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATION_CHANGELOG.md",
    "size": 115482,
    "sha256": "c45f8c5320d14f56dcb54bc654e92608cd1d58ab5fc7a9eeed652a62f6921919",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_SOURCE_TRACEABILITY.csv",
    "size": 628061,
    "sha256": "035115773105e34fe363cf1ce5e201c9ddd765e886a4a17af4de42273e8a667d",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.1",
    "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_TERMINOLOGY.csv",
    "size": 37937,
    "sha256": "3b989e27e2ffd2079aed8ee2591f1ca9632747c3811b5b01f7a7601808a4a728",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_7_GATE_REVIEW.md",
    "size": 24089,
    "sha256": "cd9b63c933e07b4bbc1dd02dd5f469af449e49a5515fa226d2b5861ebfd8a4b2",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_CITATION_RENUMBERING_MAP.csv",
    "size": 136888,
    "sha256": "d04856f4e81d291a5188d2e1182fb92d1ef396b8dd85113a66ea2e3693c823e7",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_EXECUTION_REPORT.md",
    "size": 58384,
    "sha256": "fa80bfc44be924c594bcda9514f290e74f558dd7b49dfe1a9ffcd190a05bb095",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATED.docx",
    "size": 209809,
    "sha256": "701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATION_CHANGELOG.md",
    "size": 54286,
    "sha256": "df3bca80e0b37fa66beeb63c3a059be3149b117405d5862dff846c0134022351",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_SOURCE_TRACEABILITY.csv",
    "size": 1057651,
    "sha256": "a72802cc636d3c7705113cf24eec47282ebd35051f6ca9216a4d61c67510735e",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.2",
    "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_TERMINOLOGY.csv",
    "size": 86101,
    "sha256": "f529dfcb8ebf58db07112c4b17154760a08714a6bac165fc0503b4e06c736693",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md",
    "size": 4704,
    "sha256": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv",
    "size": 9497,
    "sha256": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md",
    "size": 4151,
    "sha256": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx",
    "size": 58978,
    "sha256": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md",
    "size": 4236,
    "sha256": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv",
    "size": 38990,
    "sha256": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.3",
    "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv",
    "size": 15535,
    "sha256": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md",
    "size": 16640,
    "sha256": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv",
    "size": 1162,
    "sha256": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md",
    "size": 18585,
    "sha256": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx",
    "size": 74271,
    "sha256": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md",
    "size": 41245,
    "sha256": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv",
    "size": 579138,
    "sha256": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.4",
    "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv",
    "size": 201384,
    "sha256": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md",
    "size": 6022,
    "sha256": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv",
    "size": 1398,
    "sha256": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md",
    "size": 6249,
    "sha256": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx",
    "size": 73464,
    "sha256": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md",
    "size": 12440,
    "sha256": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv",
    "size": 227542,
    "sha256": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.5",
    "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv",
    "size": 26469,
    "sha256": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md",
    "size": 25220,
    "sha256": "b066121b47c37197b10d2bed2fa9709d5688d4973b5d13e23121c7bbf6ed275a",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv",
    "size": 463359,
    "sha256": "019d4780f896a73b3b85400675d394dcfdda1c13e8404d7a0ff9723db4887944",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md",
    "size": 64768,
    "sha256": "de894a4c00089ca73f15076e06fdba9870b86231e236f7a7add802e9f701a2d6",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx",
    "size": 63899,
    "sha256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md",
    "size": 243288,
    "sha256": "15fc8d6380b20bff447626adff74034251ab633c548dea0893a836d7f0f28fc0",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv",
    "size": 10512100,
    "sha256": "987fb13dda00f2d62abb4da346f2c6da7e3cbd3857749edc3f72725b59049a13",
    "protection": "READ_ONLY_UNCHANGED"
  },
  {
    "source_section": "2.6",
    "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv",
    "size": 409304,
    "sha256": "ec725c4206ac2854febc16f7ddb882802c1d71e53037792dd6ad6383869bca09",
    "protection": "READ_ONLY_UNCHANGED"
  }
]
```
## Crowley và metadata

Crowley chapter [19] dùng 5477–5482 theo PDF M11 được kiểm ở phiên trước. Bốn xung đột tên tác giả cũng được giải quyết từ PDF trang đầu. Changelog và global map giữ before/after cùng provenance đầy đủ. Không sửa sáu baseline.

## Môi trường và đường dẫn

```json
{
  "checkpoint": "/home/khanh/mp1-checkpoints/MP1-CH2-20261021-190846",
  "historical_scratch": "/tmp/mp1-ch2-full-integration",
  "working_artifacts": "/home/khanh/mp1-work/MP1-CH2-RESUME-20261021/artifacts",
  "restoration_note": "Initial dereferencing copy failed on dangling runtime symlinks; repaired only working copy, preserving literal symlink targets. Rendering runtime not validated.",
  "dangling_runtime_symlinks": [
    "artifacts/lo-root/etc/fonts/conf.d/30-opensymbol.conf",
    "artifacts/lo-root/etc/libreoffice/registry/math.xcd",
    "artifacts/lo-root/etc/libreoffice/registry/oo-ldap.xcd.sample",
    "artifacts/lo-root/etc/libreoffice/registry/oo-ad-ldap.xcd.sample",
    "artifacts/lo-root/usr/share/doc/libgpgmepp6t64/changelog.Debian.gz",
    "artifacts/lo-root/usr/share/doc/libharfbuzz-icu0/changelog.Debian.gz",
    "artifacts/lo-root/usr/lib/libreoffice/share/registry",
    "artifacts/lo-root/usr/lib/libreoffice/share/psprint/psprint.conf",
    "artifacts/lo-root/usr/lib/libreoffice/share/uno_packages/cache",
    "artifacts/lo-root/usr/lib/libreoffice/share/prereg/bundled"
  ]
}
```
## Bảo toàn và phạm vi Git

3.080 file trong protected manifest được kiểm lại trước đóng gói. Git HEAD/diff/cached khớp checkpoint. Chỉ bốn Markdown mới được phép thêm vào thư mục deliverable; DOCX và bốn CSV giữ byte. Không thay scientific state, registry hoặc lịch sử verification. Không commit/push.

```json
{
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv": "cddfb0ec94f1eb1e05f0504991895caa6b5d11e03a139a656f16cb980c985f35",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv": "4f8291bcdea8280972dd2274a31aef294d4304f25f69e109f819aa7290064554",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv": "0bb36acb7fc6e9b5c04c548627f0211ef50295f0c6e9212bdc3c591bd698dcb7",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv": "e62dbbfa7e96015c78cedf78ade7a61f72887da589c431c3912e150e657319c5"
}
```
### Git có trước phiên tiếp tục

```text
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
?? .agents/skills.json
?? data/LR-FORMATED-rewrite.docx
?? data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md
?? data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md
?? "data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt"
?? "data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt"
?? "data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt"
?? "data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt"
?? data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt
?? "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt"
?? data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt
?? data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt
?? "data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt"
?? data/chap1-2_citations/MANIFEST.json
?? data/chap1-2_citations/README.md
?? docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md
?? docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md
?? docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md
?? docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md
?? docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx
?? docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx
?? "docs/project/almost done/LR-FORMATED.docx"
?? docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md
?? docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md
?? "literature review/LR-FORMATED-rewrite-outline-de-xuat.docx"
?? "literature review/LR-FORMATED-rewrite.docx"
?? "literature review/LR-FORMATED.docx"
?? "literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md"
?? "literature review/ma-tran-tong-quan-tai-lieu.docx"
?? "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json"
?? "literature review/~$-FORMATED-rewrite.docx"
?? "literature review/~$-FORMATED.docx"
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png
?? outputs/literature/LR_CITATION_MATRIX_2026-10-14.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv
?? outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv
?? outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md
?? outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json
?? outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json
?? outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv
?? outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv
?? outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv
```

### Diff có trước

```diff
diff --git a/outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py b/outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
index 20fa8b9..c5c8a32 100644
--- a/outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
+++ b/outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
@@ -34,21 +34,21 @@ def replace_paragraph(prefix, text):
     items[hits[0]] = ('p', (text, []))
 
 replace_paragraph('Chương này xây dựng',
-    'Chương này tổng hợp cơ sở khoa học cho việc đặc trưng hóa ứng xử uốn phụ thuộc áp suất của một bó dây TiNi có cấu hình xác định. Hai thành phần cần được phân biệt là kết cấu chịu uốn và nguồn áp suất dẫn động bằng hợp kim nhớ hình dạng (shape memory alloy, SMA). Phạm vi tổng quan gồm cơ chế giam giữ, tiếp xúc và ma sát, đặc tính nhiệt–cơ của TiNi, cùng các mô hình có thể dùng làm đối chứng. Nguồn lò xo SMA–piston được xem xét ở mức nhiệm vụ hỗ trợ và tích hợp; đáp ứng kết cấu vẫn có thể được khảo sát bằng nguồn áp suất bên ngoài.')
+    'Chương này tổng hợp cơ sở khoa học cho việc đặc trưng hóa ứng xử uốn phụ thuộc áp suất của một bó dây TiNi có cấu hình xác định. Hai thành phần cần được phân biệt là kết cấu chịu uốn và nguồn áp suất dẫn động bằng hợp kim nhớ hình dạng (shape memory alloy, SMA). Phạm vi tổng quan gồm các cơ chế biến đổi độ cứng (hiệu ứng kẹt hạt, hiệu ứng kẹt lớp và kẹt sợi), tiếp xúc và ma sát, đặc tính nhiệt–cơ của TiNi, cùng các mô hình có thể dùng làm đối chứng. Nguồn lò xo SMA–piston được xem xét ở mức nhiệm vụ hỗ trợ và tích hợp; đáp ứng kết cấu vẫn có thể được khảo sát bằng nguồn áp suất bên ngoài.')
 replace_paragraph('Mạch lập luận được tổ chức',
     'Tổng quan được tổ chức theo quan hệ giữa kích thích, đường truyền lực và đại lượng quan sát. Các kết quả thực nghiệm được diễn giải trong phạm vi vật liệu, hình học, tải và điều kiện biên của từng nghiên cứu. Mô hình hoặc phép thử trên hệ tương tự cung cấp cơ sở tham chiếu, nhưng không thay thế cho kiểm chứng trên bó TiNi. Cách tiếp cận này giúp phân biệt điều đã được thiết lập trong các kiến trúc liên quan với vấn đề cần nhận dạng hoặc đặc trưng hóa riêng cho MP1-R.')
 replace_paragraph('Phần cuối chương tổng hợp',
     'Phần cuối chương kết nối chuỗi từ áp suất đến đáp ứng uốn và xác định giới hạn suy luận tại mỗi mắt xích. Trọng tâm là ánh xạ từ phản lực hướng tâm đến lực pháp tuyến tiếp xúc (contact normal force) cục bộ tại tiếp diện dây–dây (wire–wire) và dây–ống bao (wire–sleeve). Từ đó, chương dẫn đến một câu hỏi nghiên cứu chính và hai câu hỏi phụ, đồng thời giữ các cách giải thích vật liệu, tiếp xúc thông thường và tương tác bổ sung như những khả năng cần phân biệt bằng quan sát.')
 replace_paragraph('Trong các kết cấu biến đổi',
-    'Trong các kết cấu biến đổi độ cứng, giam giữ có thể hạn chế chuyển động tương đối của nhiều phần tử thông qua bao mềm, môi trường hạt hoặc lực ép cơ học. Ứng xử dính–trượt (stick–slip) thay đổi đáp ứng chịu tải của toàn cụm, nhưng đường truyền tải pháp tuyến phụ thuộc cách bố trí từng kiến trúc [1], [3], [4]. Vì vậy, sự thay đổi lực–độ võng hoặc mô men–độ cong không tự nó xác định lực tiếp xúc cục bộ hay tiếp diện chi phối.')
+    'Trong các kết cấu biến đổi độ cứng, hiệu ứng kẹt (jamming) giúp hạn chế chuyển động tương đối của nhiều phần tử thông qua bao mềm, sự đông đặc vật liệu hạt (granular jamming) hoặc lực ép cơ học. Ứng xử dính–trượt (stick–slip) thay đổi đáp ứng chịu tải của toàn cụm, nhưng đường truyền tải pháp tuyến phụ thuộc cách bố trí từng kiến trúc [1], [3], [4]. Vì vậy, sự thay đổi lực–độ võng hoặc mô men–độ cong không tự nó xác định lực tiếp xúc cục bộ hay tiếp diện chi phối.')
 replace_paragraph('Tổng quan của Caro',
-    'Caro và Carmichael phân loại các cơ chế thay đổi độ cứng của kết cấu giam giữ nhiều lớp, gồm ma sát, cản trở chuyển động bằng hình học và những cơ chế khác [2]. Phạm vi bài tổng quan tập trung vào cấu trúc lớp; nó không bao quát các hệ hạt hoặc sợi. Nguồn này hữu ích để định vị cơ chế và thuật ngữ, còn các mệnh đề về thí nghiệm hay mô hình cụ thể cần dựa trên nghiên cứu gốc. Sự phân biệt này tránh dùng một tổng quan lớp làm bằng chứng lặp lại độc lập cho bó dây.')
+    'Caro và Carmichael phân loại các cơ chế thay đổi độ cứng của kết cấu kẹt lớp (hiệu ứng kẹt lớp - laminar/layer jamming), gồm ma sát, cản trở chuyển động bằng hình học và những cơ chế khác [2]. Phạm vi bài tổng quan tập trung vào cấu trúc lớp; nó không bao quát các hệ hạt hoặc sợi. Nguồn này hữu ích để định vị cơ chế và thuật ngữ, còn các mệnh đề về thí nghiệm hay mô hình cụ thể cần dựa trên nghiên cứu gốc. Sự phân biệt này tránh dùng một tổng quan lớp làm bằng chứng lặp lại độc lập cho bó dây.')
 replace_paragraph('Liu và cộng sự trình bày',
-    'Các thí nghiệm trên hệ hạt của Liu và cộng sự bổ sung một đường giam giữ khác với bao hút chân không của Bai và cộng sự: áp suất dương được dùng để điều chỉnh đáp ứng của cụm hạt–túi [3]. Đối chiếu hai hệ cho thấy áp suất dương và hút chân không đều có thể đi kèm thay đổi ứng xử uốn, nhưng vật liệu phần tử, hướng phản lực và độ mềm bao khác nhau [1], [3]. Bằng chứng vì vậy xác lập hiệu ứng trong từng kiến trúc, chứ không xác lập một quan hệ áp suất–độ cứng phổ quát cho bó TiNi.')
+    'Các thí nghiệm trên hệ hạt của Liu và cộng sự bổ sung một cơ chế kẹt hạt (hiệu ứng kẹt hạt - granular jamming) bằng áp suất dương, khác với bao hút chân không của Bai và cộng sự: áp suất dương được dùng để điều chỉnh sự đông đặc vật liệu hạt và đáp ứng của cụm hạt–túi [3]. Đối chiếu hai hệ cho thấy áp suất dương và hút chân không đều có thể đi kèm thay đổi ứng xử uốn, nhưng vật liệu phần tử, hướng phản lực và độ mềm bao khác nhau [1], [3]. Bằng chứng vì vậy xác lập hiệu ứng trong từng kiến trúc, chứ không xác lập một quan hệ áp suất–độ cứng phổ quát cho bó TiNi.')
 replace_paragraph('Zhang và Yao xây dựng',
     'So với môi trường hạt, chuỗi sợi nylon chịu áp suất dương của Zhang và Yao gần hơn với MP1-R về câu hỏi cơ học nhiều phần tử. Công trình kết hợp mô hình các nhánh dính, trượt một phần và trượt hoàn toàn với thí nghiệm uốn; độ nhạy theo áp suất khác nhau giữa các nhánh [4]. Tuy nhiên, chuỗi dùng sợi nylon, các phần liên kết cứng và túi bơm phồng, trong khi MP1-R dùng bó TiNi với đường phản lực và tiếp diện chưa được đồng nhất. Một phần tham số được nhận dạng từ đáp ứng tổng thể. Do đó, cách phân nhánh là cơ sở tham chiếu phù hợp, còn hệ số truyền áp suất và lực tiếp xúc không được chuyển trực tiếp sang cấu hình mới.')
 replace_paragraph('Zhang, Yao, Zhao',
-    'Mô hình liên tục của Zhang, Yao, Zhao và Wei xét dầm nhiều lớp polyvinyl chloride (PVC) dưới hút chân không, thay vì sợi chịu áp suất dương [5]. Mô hình dùng ngưỡng ma sát để mô tả vùng dính–trượt và được đối chiếu với phần tử hữu hạn cùng đáp ứng toàn cục của mẫu. Hạn chế liên quan đến ứng suất pháp tuyến ngang, hiệu ứng đầu mút và vùng trượt ở biến dạng lớn cho thấy mức đơn giản hóa đường tiếp xúc ảnh hưởng khả năng dự đoán. Công trình này cung cấp tương tự lý thuyết–cơ học cho MP1-R; nó không xác nhận bó TiNi, giam giữ sợi áp suất dương hoặc lực pháp tuyến cục bộ của hệ đề xuất.')
+    'Mô hình liên tục của Zhang, Yao, Zhao và Wei xét dầm kẹt lớp (hiệu ứng kẹt lớp - layer jamming beam) bằng các lớp polyvinyl chloride (PVC) dưới hút chân không, thay vì sợi chịu áp suất dương [5]. Mô hình dùng ngưỡng ma sát để mô tả vùng dính–trượt và được đối chiếu với phần tử hữu hạn cùng đáp ứng toàn cục của mẫu. Hạn chế liên quan đến ứng suất pháp tuyến ngang, hiệu ứng đầu mút và vùng trượt ở biến dạng lớn cho thấy mức đơn giản hóa đường tiếp xúc ảnh hưởng khả năng dự đoán. Công trình này cung cấp tương tự lý thuyết–cơ học cho MP1-R; nó không xác nhận bó TiNi, hiệu ứng kẹt sợi dưới áp suất dương hoặc lực pháp tuyến cục bộ của hệ đề xuất.')
 replace_paragraph('Tại một tiếp diện',
     'Trong mô hình ma sát kiểu Coulomb, độ lớn lực tiếp tuyến bị giới hạn bởi tích của lực pháp tuyến với hệ số ma sát. Cách biểu diễn này được dùng trong mô hình sợi và dầm nhiều lớp đã khảo sát [4], [5]. Đối với một tiếp diện quy ước i, giới hạn tối thiểu được viết là:')
 for i, (k, v) in enumerate(items):
@@ -88,9 +88,9 @@ replace_paragraph('Phase 4 đánh giá',
 replace_paragraph('Ba trạng thái giả thuyết',
     'Ba cách giải thích được giữ để đánh giá trong MP1-R. H0a-R xem đáp ứng có thể được giải thích chủ yếu bởi trạng thái nhiệt–cơ của TiNi. H0b-R xem tiếp xúc, ma sát, dính–trượt, điều kiện biên và mô hình vật liệu có xét chuyển pha là đủ trong nguyên tắc, không cần luật cấu thành mới. H1-R chỉ được xem xét có điều kiện: một tương tác áp suất–tiếp xúc–vật liệu bổ sung phải được nhận dạng và cần thiết về dự đoán sau khi các cách giải thích đơn giản hơn cùng ảnh hưởng gây nhiễu đã được giới hạn.')
 replace_paragraph('Huynh và cộng sự tích hợp',
-    'Huynh và cộng sự tích hợp vi bơm với bộ chấp hành mềm có phần giam giữ để chuyển độ cứng [17]. Trong kiến trúc này, hút chân không phục vụ giam giữ, còn áp suất dương phục vụ uốn; hai chức năng không được đánh đồng. Kết quả cung cấp tiền lệ tích hợp nguồn áp suất và kết cấu, nhưng việc hiệu chuẩn nguồn tách rời cũng giới hạn suy luận áp suất ngay tại cụm. Nó không xác nhận miền vận hành của lò xo–piston hoặc đáp ứng bó TiNi của MP1-R.')
+    'Huynh và cộng sự tích hợp vi bơm với bộ chấp hành mềm có khoang kẹt hạt (particle jamming) để chuyển độ cứng [17]. Trong kiến trúc này, hút chân không phục vụ tạo hiệu ứng kẹt hạt (sự đông đặc vật liệu hạt), còn áp suất dương phục vụ uốn; hai chức năng không được đánh đồng. Kết quả cung cấp tiền lệ tích hợp nguồn áp suất và kết cấu, nhưng việc hiệu chuẩn nguồn tách rời cũng giới hạn suy luận áp suất ngay tại cụm. Nó không xác nhận miền vận hành của lò xo–piston hoặc đáp ứng bó TiNi của MP1-R.')
 replace_paragraph('Các bằng chứng đã thẩm định cung cấp nhiều lớp',
-    'Các mô hình hiện có khác nhau ở phần cơ học chúng giữ lại. Mô hình sợi nylon áp suất dương và mô hình dầm lớp PVC mô tả nhánh hoặc vùng dính–trượt nhưng có đường giam giữ khác nhau [4], [5]. Mô hình cáp thép cung cấp giới hạn độ cứng trong điều kiện hình học và biên đã định [8], còn các mô hình cáp SMA xét chuyển pha với mức mô tả tiếp xúc khác nhau [9], [12], [15]. Như vậy, đã có các thành phần cơ học thích hợp cho mô hình đối chứng; sự tồn tại của chúng chưa đồng nghĩa khả năng dự đoán được kiểm chứng cho bó TiNi chịu áp suất.')
+    'Các mô hình hiện có khác nhau ở phần cơ học chúng giữ lại. Mô hình sợi nylon áp suất dương (kẹt sợi) và mô hình dầm kẹt lớp PVC (hiệu ứng kẹt lớp) mô tả nhánh hoặc vùng dính–trượt nhưng có cơ chế tạo kẹt và đường truyền lực khác nhau [4], [5]. Mô hình cáp thép cung cấp giới hạn độ cứng trong điều kiện hình học và biên đã định [8], còn các mô hình cáp SMA xét chuyển pha với mức mô tả tiếp xúc khác nhau [9], [12], [15]. Như vậy, đã có các thành phần cơ học thích hợp cho mô hình đối chứng; sự tồn tại của chúng chưa đồng nghĩa khả năng dự đoán được kiểm chứng cho bó TiNi chịu áp suất.')
 replace_paragraph('Chuỗi nhân quả làm khung',
     'Chuỗi cơ học làm khung cho MP1-R gồm: áp suất chất lưu → đáp ứng màng hoặc vỏ → phản lực hướng tâm → lực pháp tuyến cục bộ → giới hạn lực ma sát → trạng thái trượt → đáp ứng uốn. Các hệ áp suất dương cung cấp bằng chứng về kích thích và đáp ứng toàn cục [3], [4]; các mô hình cáp và lớp bổ sung cơ sở cho giới hạn trượt và độ cứng [5], [8]. Việc nối các phần này thành chuỗi hoàn chỉnh của MP1-R vẫn cần những giả thiết truyền tải và quan sát riêng, như được giới hạn trong Bảng 2.3.')
 replace_paragraph('Phase 5 không phê duyệt',
@@ -106,7 +106,7 @@ replace_paragraph('Vì vậy, tiêu đề',
 replace_paragraph('Đóng góp chính được giới hạn',
     'Đóng góp chính là đặc trưng hóa định lượng đáp ứng uốn phụ thuộc áp suất của bó TiNi đã định với mô hình đối chứng thông thường được khóa. Nhận dạng tiếp diện, trượt cục bộ và kiểm tra khả năng dự đoán là các đóng góp thứ cấp; xác nhận nguồn SMA–piston và tích hợp là nhiệm vụ hỗ trợ. Hạng tử tương tác bổ sung chỉ là mở rộng có điều kiện, phụ thuộc phần dư lặp lại cùng bằng chứng nhận dạng và cải thiện dự đoán trên dữ liệu giữ lại.')
 anchor=next(i for i,(k,v) in enumerate(items) if k=='p' and v[0].startswith('Chuỗi cơ học làm khung'))
-items.insert(anchor,('p',('Những kết quả đã được thiết lập cần được giữ trong miền kiểm chứng của chúng: giam giữ làm thay đổi đáp ứng uốn ở các hệ sợi và hạt đã thử [1], [3], [4]; trạng thái trượt tạo các giới hạn hoặc nhánh đáp ứng ở cáp thép và kết cấu nhiều lớp [5], [8]; TiNi có đáp ứng nhạy trạng thái trong các phép kéo đã khảo sát [10], [11]; và dẫn động SMA–chất lỏng đã có tiền lệ [16]. Các mô hình tiếp xúc có xét vật liệu chuyển pha cũng đã tồn tại [9], [15]. Từ các kết quả này có thể xây dựng đối chứng và phép so sánh, nhưng khả năng chuyển sang một đường phản lực mới chỉ được hỗ trợ ở mức phụ thuộc kiến trúc.',[])))
+items.insert(anchor,('p',('Những kết quả đã được thiết lập cần được giữ trong miền kiểm chứng của chúng: hiệu ứng kẹt (jamming) làm thay đổi đáp ứng uốn ở các hệ kẹt sợi và kẹt hạt đã thử [1], [3], [4]; trạng thái trượt tạo các giới hạn hoặc nhánh đáp ứng ở cáp thép và kết cấu kẹt lớp [5], [8]; TiNi có đáp ứng nhạy trạng thái trong các phép kéo đã khảo sát [10], [11]; và dẫn động SMA–chất lỏng đã có tiền lệ [16]. Các mô hình tiếp xúc có xét vật liệu chuyển pha cũng đã tồn tại [9], [15]. Từ các kết quả này có thể xây dựng đối chứng và phép so sánh, nhưng khả năng chuyển sang một đường phản lực mới chỉ được hỗ trợ ở mức phụ thuộc kiến trúc.',[])))
 
 # Use consistent Vietnamese terms after their definitions.
 translations = {
diff --git a/outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md b/outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
index 58b5492..5c5396d 100644
--- a/outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
+++ b/outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
@@ -2,31 +2,31 @@
 
 ## 2.1. Giới thiệu chương
 
-Chương này tổng hợp cơ sở khoa học cho việc đặc trưng hóa ứng xử uốn phụ thuộc áp suất của một bó dây TiNi có cấu hình xác định. Hai thành phần cần được phân biệt là kết cấu chịu uốn và nguồn áp suất dẫn động bằng hợp kim nhớ hình dạng (shape memory alloy, SMA). Phạm vi tổng quan gồm cơ chế giam giữ, tiếp xúc và ma sát, đặc tính nhiệt–cơ của TiNi, cùng các mô hình có thể dùng làm đối chứng. Nguồn lò xo SMA–piston được xem xét ở mức nhiệm vụ hỗ trợ và tích hợp; đáp ứng kết cấu vẫn có thể được khảo sát bằng nguồn áp suất bên ngoài.
+Chương này tổng hợp cơ sở khoa học cho việc đặc trưng hóa ứng xử uốn phụ thuộc áp suất của một bó dây TiNi có cấu hình xác định. Hai thành phần cần được phân biệt là kết cấu chịu uốn và nguồn áp suất dẫn động bằng hợp kim nhớ hình dạng (shape memory alloy, SMA). Phạm vi tổng quan gồm các cơ chế biến đổi độ cứng (hiệu ứng kẹt hạt, hiệu ứng kẹt lớp và kẹt sợi), tiếp xúc và ma sát, đặc tính nhiệt–cơ của TiNi, cùng các mô hình có thể dùng làm đối chứng. Nguồn lò xo SMA–piston được xem xét ở mức nhiệm vụ hỗ trợ và tích hợp; đáp ứng kết cấu vẫn có thể được khảo sát bằng nguồn áp suất bên ngoài.
 
 Tổng quan được tổ chức theo quan hệ giữa kích thích, đường truyền lực và đại lượng quan sát. Các kết quả thực nghiệm được diễn giải trong phạm vi vật liệu, hình học, tải và điều kiện biên của từng nghiên cứu. Mô hình hoặc phép thử trên hệ tương tự cung cấp cơ sở tham chiếu, nhưng không thay thế cho kiểm chứng trên bó TiNi. Cách tiếp cận này giúp phân biệt điều đã được thiết lập trong các kiến trúc liên quan với vấn đề cần nhận dạng hoặc đặc trưng hóa riêng cho MP1-R.
 
 Phần cuối chương kết nối chuỗi từ áp suất đến đáp ứng uốn và xác định giới hạn suy luận tại mỗi mắt xích. Trọng tâm là ánh xạ từ phản lực hướng tâm đến lực pháp tuyến tiếp xúc (contact normal force) cục bộ tại tiếp diện dây–dây (wire–wire) và dây–ống bao (wire–sleeve). Từ đó, chương dẫn đến một câu hỏi nghiên cứu chính và hai câu hỏi phụ, đồng thời giữ các cách giải thích vật liệu, tiếp xúc thông thường và tương tác bổ sung như những khả năng cần phân biệt bằng quan sát.
 
-## 2.2. Cơ chế thay đổi độ cứng dựa trên giam giữ và áp suất
+## 2.2. Cơ chế thay đổi độ cứng dựa trên hiệu ứng kẹt (jamming) và áp suất
 
-Trong các kết cấu biến đổi độ cứng, giam giữ có thể hạn chế chuyển động tương đối của nhiều phần tử thông qua bao mềm, môi trường hạt hoặc lực ép cơ học. Ứng xử dính–trượt (stick–slip) thay đổi đáp ứng chịu tải của toàn cụm, nhưng đường truyền tải pháp tuyến phụ thuộc cách bố trí từng kiến trúc [1]–[3]. Vì vậy, sự thay đổi lực–độ võng hoặc mô men–độ cong không tự nó xác định lực tiếp xúc cục bộ hay tiếp diện chi phối.
+Trong các kết cấu biến đổi độ cứng, hiệu ứng kẹt (jamming) giúp hạn chế chuyển động tương đối của nhiều phần tử thông qua bao mềm, sự đông đặc vật liệu hạt (granular jamming) hoặc lực ép cơ học. Ứng xử dính–trượt (stick–slip) thay đổi đáp ứng chịu tải của toàn cụm, nhưng đường truyền tải pháp tuyến phụ thuộc cách bố trí từng kiến trúc [1]–[3]. Vì vậy, sự thay đổi lực–độ võng hoặc mô men–độ cong không tự nó xác định lực tiếp xúc cục bộ hay tiếp diện chi phối.
 
-Bai và cộng sự đã khảo sát bộ chấp hành mềm dùng bó dây hoặc sợi không kim loại trong một bao kín, với so sánh trạng thái hút chân không và nhả giam giữ. Công trình này cho thấy ma sát giữa các phần tử có thể làm thay đổi khả năng chịu uốn và xoắn của một kiến trúc wire-jamming [1]. Tuy nhiên, vật liệu, bao bọc và đường tải của nghiên cứu khác với bó dây TiNi chịu áp suất hướng ra ngoài; lực giữa các sợi, lực màng và ảnh hưởng của sắp xếp phần tử không được tách độc lập. Vì vậy, nguồn này thiết lập khả năng điều chỉnh độ cứng theo kiến trúc, chứ không cung cấp hệ số chuyển áp suất–lực cho MP1-R.
+Bai và cộng sự đã khảo sát bộ chấp hành mềm dùng bó dây hoặc sợi không kim loại trong một bao kín, với so sánh trạng thái hút chân không (trạng thái kẹt - jammed) và nhả kẹt (unjammed). Công trình này cho thấy ma sát giữa các phần tử có thể làm thay đổi khả năng chịu uốn và xoắn của một kiến trúc kẹt sợi (wire-jamming) [1]. Tuy nhiên, vật liệu, bao bọc và đường tải của nghiên cứu khác với bó dây TiNi chịu áp suất hướng ra ngoài; lực giữa các sợi, lực màng và ảnh hưởng của sắp xếp phần tử không được tách độc lập. Vì vậy, nguồn này thiết lập khả năng điều chỉnh độ cứng theo kiến trúc, chứ không cung cấp hệ số chuyển áp suất–lực cho MP1-R.
 
-Caro và Carmichael phân loại các cơ chế thay đổi độ cứng của kết cấu giam giữ nhiều lớp, gồm ma sát, cản trở chuyển động bằng hình học và những cơ chế khác [4]. Phạm vi bài tổng quan tập trung vào cấu trúc lớp; nó không bao quát các hệ hạt hoặc sợi. Nguồn này hữu ích để định vị cơ chế và thuật ngữ, còn các mệnh đề về thí nghiệm hay mô hình cụ thể cần dựa trên nghiên cứu gốc. Sự phân biệt này tránh dùng một tổng quan lớp làm bằng chứng lặp lại độc lập cho bó dây.
+Caro và Carmichael phân loại các cơ chế thay đổi độ cứng của kết cấu kẹt lớp (hiệu ứng kẹt lớp - laminar/layer jamming), gồm ma sát, cản trở chuyển động bằng hình học và những cơ chế khác [4]. Phạm vi bài tổng quan tập trung vào cấu trúc lớp; nó không bao quát các hệ hạt hoặc sợi. Nguồn này hữu ích để định vị cơ chế và thuật ngữ, còn các mệnh đề về thí nghiệm hay mô hình cụ thể cần dựa trên nghiên cứu gốc. Sự phân biệt này tránh dùng một tổng quan lớp làm bằng chứng lặp lại độc lập cho bó dây.
 
-Các thí nghiệm trên hệ hạt của Liu và cộng sự bổ sung một đường giam giữ khác với bao hút chân không của Bai và cộng sự: áp suất dương được dùng để điều chỉnh đáp ứng của cụm hạt–túi [2]. Đối chiếu hai hệ cho thấy áp suất dương và hút chân không đều có thể đi kèm thay đổi ứng xử uốn, nhưng vật liệu phần tử, hướng phản lực và độ mềm bao khác nhau [1], [2]. Bằng chứng vì vậy xác lập hiệu ứng trong từng kiến trúc, chứ không xác lập một quan hệ áp suất–độ cứng phổ quát cho bó TiNi.
+Các thí nghiệm trên hệ hạt của Liu và cộng sự bổ sung một cơ chế kẹt hạt (hiệu ứng kẹt hạt - granular jamming) bằng áp suất dương, khác với bao hút chân không của Bai và cộng sự: áp suất dương được dùng để điều chỉnh sự đông đặc vật liệu hạt và đáp ứng của cụm hạt–túi [2]. Đối chiếu hai hệ cho thấy áp suất dương và hút chân không đều có thể đi kèm thay đổi ứng xử uốn, nhưng vật liệu phần tử, hướng phản lực và độ mềm bao khác nhau [1], [2]. Bằng chứng vì vậy xác lập hiệu ứng trong từng kiến trúc, chứ không xác lập một quan hệ áp suất–độ cứng phổ quát cho bó TiNi.
 
 So với môi trường hạt, chuỗi sợi nylon chịu áp suất dương của Zhang và Yao gần hơn với MP1-R về câu hỏi cơ học nhiều phần tử. Công trình kết hợp mô hình các nhánh dính, trượt một phần và trượt hoàn toàn với thí nghiệm uốn; độ nhạy theo áp suất khác nhau giữa các nhánh [3]. Tuy nhiên, chuỗi dùng sợi nylon, các phần liên kết cứng và túi bơm phồng, trong khi MP1-R dùng bó TiNi với đường phản lực và tiếp diện chưa được đồng nhất. Một phần tham số được nhận dạng từ đáp ứng tổng thể. Do đó, cách phân nhánh là cơ sở tham chiếu phù hợp, còn hệ số truyền áp suất và lực tiếp xúc không được chuyển trực tiếp sang cấu hình mới.
 
-Mô hình liên tục của Zhang, Yao, Zhao và Wei xét dầm nhiều lớp polyvinyl chloride (PVC) dưới hút chân không, thay vì sợi chịu áp suất dương [5]. Mô hình dùng ngưỡng ma sát để mô tả vùng dính–trượt và được đối chiếu với phần tử hữu hạn cùng đáp ứng toàn cục của mẫu. Hạn chế liên quan đến ứng suất pháp tuyến ngang, hiệu ứng đầu mút và vùng trượt ở biến dạng lớn cho thấy mức đơn giản hóa đường tiếp xúc ảnh hưởng khả năng dự đoán. Công trình này cung cấp tương tự lý thuyết–cơ học cho MP1-R; nó không xác nhận bó TiNi, giam giữ sợi áp suất dương hoặc lực pháp tuyến cục bộ của hệ đề xuất.
+Mô hình liên tục của Zhang, Yao, Zhao và Wei xét dầm kẹt lớp (hiệu ứng kẹt lớp - layer jamming beam) bằng các lớp polyvinyl chloride (PVC) dưới hút chân không, thay vì sợi chịu áp suất dương [5]. Mô hình dùng ngưỡng ma sát để mô tả vùng dính–trượt và được đối chiếu với phần tử hữu hạn cùng đáp ứng toàn cục của mẫu. Hạn chế liên quan đến ứng suất pháp tuyến ngang, hiệu ứng đầu mút và vùng trượt ở biến dạng lớn cho thấy mức đơn giản hóa đường tiếp xúc ảnh hưởng khả năng dự đoán. Công trình này cung cấp tương tự lý thuyết–cơ học cho MP1-R; nó không xác nhận bó TiNi, hiệu ứng kẹt sợi dưới áp suất dương hoặc lực pháp tuyến cục bộ của hệ đề xuất.
 
-Bảng 2.1. So sánh các đường truyền giam giữ trong các kiến trúc đã được thẩm định
-Kiến trúc | Tác nhân giam giữ | Đáp ứng chính | Giới hạn khi chuyển sang MP1-R
+Bảng 2.1. So sánh các đường truyền lực và hiệu ứng kẹt (jamming) trong các kiến trúc đã được thẩm định
+Kiến trúc | Tác nhân kích hoạt kẹt (jamming) | Đáp ứng chính | Giới hạn khi chuyển sang MP1-R
 Bó dây/sợi không kim loại [1] | Hút chân không qua bao mềm | Lực–độ võng, mô men–góc xoắn | Không phải TiNi; tiếp diện và lực màng chưa tách độc lập
-Giam giữ hạt [2] | Áp suất dương làm nén môi trường hạt | Uốn của cụm hạt–túi | Lực hạt–biên và độ mềm túi phụ thuộc kiến trúc
-Giam giữ sợi [3] | Túi bơm phồng áp suất dương và thành phản lực | Nhánh dính–trượt và tải tới hạn | Tham số hiệu dụng và phản lực cục bộ chưa được đo độc lập
+Hiệu ứng kẹt hạt (Granular Jamming) [2] | Áp suất dương làm nén môi trường hạt | Uốn của cụm hạt–túi | Lực hạt–biên và độ mềm túi phụ thuộc kiến trúc
+Hiệu ứng kẹt sợi (Fiber Jamming) [3] | Túi bơm phồng áp suất dương và thành phản lực | Nhánh dính–trượt và tải tới hạn | Tham số hiệu dụng và phản lực cục bộ chưa được đo độc lập
 Layer-jamming liên tục [5] | Hút chân không giữa các lớp PVC | Ứng suất, vùng trượt và tải–độ võng | Tương tự cơ học; không phải bó sợi áp suất dương hoặc TiNi
 MP1-R | Áp suất gần mẫu và phản lực hướng tâm dự kiến | Mô men–độ cong, trượt cục bộ và phụ thuộc trạng thái TiNi | Ánh xạ áp suất–phản lực–lực pháp tuyến chưa được xác định
 Các kết quả được diễn giải trong phạm vi từng kiến trúc gốc; riêng mô hình lớp PVC là tương tự lý thuyết–cơ học. Dòng MP1-R mô tả miền cần kiểm chứng, không phải kết quả đã có.
@@ -43,7 +43,7 @@ Trong đó Fₜ,ᵢ là lực tiếp tuyến tại tiếp diện i, Nᵢ là l
 
 Trong mô hình sợi áp suất dương, Zhang và Yao giới hạn lực cắt hoặc ngưỡng trượt bằng một tham số liên quan đến áp suất, nhưng phản lực thành và tiếp diện sợi–thành vẫn là một phần của giả thiết kiến trúc [3]. Vì vậy, kết quả của họ phù hợp với diễn giải “áp suất có thể điều kiện hóa khả năng trượt” trong hệ đã xác định. Nó không chứng minh rằng mọi cấu hình bó dây đều có cùng phân bố N, cũng không chứng minh ma sát là cơ chế duy nhất của mọi nhánh uốn.
 
-Trong mô hình layer-jamming liên tục, Zhang và cộng sự phân biệt ứng suất pháp tuyến dọc trục với ứng suất cắt giữa các lớp, dùng ngưỡng ma sát phụ thuộc tích μp để mô tả vùng trượt [5]. Cách mô tả này hữu ích cho MP1-R ở cấp độ mô hình: một mô hình đối chứng có thể cần các trạng thái dính, trượt một phần và trượt hoàn toàn. Tuy nhiên, p trong mô hình PVC là áp suất giam giữ của kiến trúc đó; nó không phải phép đo trực tiếp N của một tiếp diện dây–dây hoặc dây–ống bao trong bó TiNi.
+Trong mô hình kẹt lớp (layer jamming) liên tục, Zhang và cộng sự phân biệt ứng suất pháp tuyến dọc trục với ứng suất cắt giữa các lớp, dùng ngưỡng ma sát phụ thuộc tích μp để mô tả vùng trượt [5]. Cách mô tả này hữu ích cho MP1-R ở cấp độ mô hình: một mô hình đối chứng có thể cần các trạng thái dính, trượt một phần và trượt hoàn toàn. Tuy nhiên, p trong mô hình PVC là áp suất nén ép kẹt (confining/jamming pressure) của kiến trúc kẹt lớp đó; nó không phải phép đo trực tiếp N của một tiếp diện dây–dây hoặc dây–ống bao trong bó TiNi.
 
 Ở dây cáp thép ngắn, Barsi, Carboni và Lacarbonara xây dựng mô hình cơ học và đối chiếu các giới hạn độ cứng bằng thí nghiệm uốn [6]. Khác với các mô hình áp suất của sợi và lớp, đường tải ở đây chịu ảnh hưởng của hình học cáp và điều kiện đầu mút, còn trạng thái trượt được dùng để xác định các giới hạn đáp ứng [3], [5], [6]. Kết quả tạo cơ sở cho một mô hình đối chứng về độ cứng, nhưng không cung cấp luật đầy đủ cho vòng trễ hoặc phân bố áp suất–tiếp xúc của MP1-R.
 
@@ -100,7 +100,7 @@ Hệ quả phương pháp là mô hình đối chứng phải được khóa tr
 
 SMA dùng để dẫn động nguồn áp suất là một vấn đề khác với TiNi dùng làm phần tử chịu lực. Pierce và Mascaro đã trình bày một bơm chất lỏng được dẫn động bởi dây SMA, trong đó chuyển vị của bộ chấp hành được liên kết với động lực nhiệt–lưu chất và thể tích dịch chuyển [14]. Nguồn này thiết lập tiền lệ SMA–chất lỏng, nhưng kiến trúc bơm và điều kiện làm mát không phải nguồn áp suất lò xo–piston của MP1-R.
 
-Huynh và cộng sự tích hợp vi bơm với bộ chấp hành mềm có phần giam giữ để chuyển độ cứng [18]. Trong kiến trúc này, hút chân không phục vụ giam giữ, còn áp suất dương phục vụ uốn; hai chức năng không được đánh đồng. Kết quả cung cấp tiền lệ tích hợp nguồn áp suất và kết cấu, nhưng việc hiệu chuẩn nguồn tách rời cũng giới hạn suy luận áp suất ngay tại cụm. Nó không xác nhận miền vận hành của lò xo–piston hoặc đáp ứng bó TiNi của MP1-R.
+Huynh và cộng sự tích hợp vi bơm với bộ chấp hành mềm có khoang kẹt hạt (particle jamming) để chuyển độ cứng [18]. Trong kiến trúc này, hút chân không phục vụ tạo hiệu ứng kẹt hạt (sự đông đặc vật liệu hạt), còn áp suất dương phục vụ uốn; hai chức năng không được đánh đồng. Kết quả cung cấp tiền lệ tích hợp nguồn áp suất và kết cấu, nhưng việc hiệu chuẩn nguồn tách rời cũng giới hạn suy luận áp suất ngay tại cụm. Nó không xác nhận miền vận hành của lò xo–piston hoặc đáp ứng bó TiNi của MP1-R.
 
 Jeon và cộng sự cung cấp thêm một ví dụ trong đó SMA thay đổi lực ép tại tiếp diện dây–cao su [10]. Trong trường hợp đó, SMA là bộ điều biến ma sát của cơ cấu robot, không phải bằng chứng rằng dây kết cấu đã chuyển pha theo cùng lịch sử nhiệt. MP1-R vì vậy phải ghi riêng nhiệt độ, lực–hành trình, tốc độ đáp ứng và lịch sử của lò xo SMA; không được dùng kết quả của lò xo làm đại diện trực tiếp cho trạng thái của dây TiNi.
 
@@ -114,7 +114,7 @@ Khi hai bench được so sánh ở áp suất, nhiệt độ, tải, lịch s
 
 ## 2.9. Các mô hình cơ học hiện có và vai trò của mô hình đối chứng
 
-Các mô hình hiện có khác nhau ở phần cơ học chúng giữ lại. Mô hình sợi nylon áp suất dương và mô hình dầm lớp PVC mô tả nhánh hoặc vùng dính–trượt nhưng có đường giam giữ khác nhau [3], [5]. Mô hình cáp thép cung cấp giới hạn độ cứng trong điều kiện hình học và biên đã định [6], còn các mô hình cáp SMA xét chuyển pha với mức mô tả tiếp xúc khác nhau [7], [15], [17]. Như vậy, đã có các thành phần cơ học thích hợp cho mô hình đối chứng; sự tồn tại của chúng chưa đồng nghĩa khả năng dự đoán được kiểm chứng cho bó TiNi chịu áp suất.
+Các mô hình hiện có khác nhau ở phần cơ học chúng giữ lại. Mô hình sợi nylon áp suất dương (kẹt sợi) và mô hình dầm kẹt lớp PVC (hiệu ứng kẹt lớp) mô tả nhánh hoặc vùng dính–trượt nhưng có cơ chế tạo kẹt và đường truyền lực khác nhau [3], [5]. Mô hình cáp thép cung cấp giới hạn độ cứng trong điều kiện hình học và biên đã định [6], còn các mô hình cáp SMA xét chuyển pha với mức mô tả tiếp xúc khác nhau [7], [15], [17]. Như vậy, đã có các thành phần cơ học thích hợp cho mô hình đối chứng; sự tồn tại của chúng chưa đồng nghĩa khả năng dự đoán được kiểm chứng cho bó TiNi chịu áp suất.
 
 Các mô hình này không có cùng phạm vi. Chúng khác về vật liệu, số phần tử, cách tạo áp suất, điều kiện đầu mút, định nghĩa độ cứng, và mức độ quan sát lực tiếp xúc. Do đó, MP1-R không nên trộn các tham số của chúng thành một “mô hình chuẩn” duy nhất. Mô hình đối chứng cần được khóa với một cấu trúc rõ ràng: biến vào là áp suất gần mẫu, nhiệt độ, lịch sử tải và hình học; đầu ra là đường M–κ hoặc chỉ số độ cứng đã khai báo; tham số được nhận dạng trên tập hiệu chuẩn; đánh giá cuối cùng dùng đường tải dành riêng và bất định đo.
 
@@ -122,7 +122,7 @@ Một quy trình như vậy phân biệt hiệu chỉnh với kiểm chứng. N
 
 ## 2.10. Tổng hợp bằng chứng và giới hạn suy luận
 
-Những kết quả đã được thiết lập cần được giữ trong miền kiểm chứng của chúng: giam giữ làm thay đổi đáp ứng uốn ở các hệ sợi và hạt đã thử [1]–[3]; trạng thái trượt tạo các giới hạn hoặc nhánh đáp ứng ở cáp thép và kết cấu nhiều lớp [5], [6]; TiNi có đáp ứng nhạy trạng thái trong các phép kéo đã khảo sát [12], [13]; và dẫn động SMA–chất lỏng đã có tiền lệ [14]. Các mô hình tiếp xúc có xét vật liệu chuyển pha cũng đã tồn tại [7], [17]. Từ các kết quả này có thể xây dựng đối chứng và phép so sánh, nhưng khả năng chuyển sang một đường phản lực mới chỉ được hỗ trợ ở mức phụ thuộc kiến trúc.
+Những kết quả đã được thiết lập cần được giữ trong miền kiểm chứng của chúng: hiệu ứng kẹt (jamming) làm thay đổi đáp ứng uốn ở các hệ kẹt sợi và kẹt hạt đã thử [1]–[3]; trạng thái trượt tạo các giới hạn hoặc nhánh đáp ứng ở cáp thép và kết cấu kẹt lớp [5], [6]; TiNi có đáp ứng nhạy trạng thái trong các phép kéo đã khảo sát [12], [13]; và dẫn động SMA–chất lỏng đã có tiền lệ [14]. Các mô hình tiếp xúc có xét vật liệu chuyển pha cũng đã tồn tại [7], [17]. Từ các kết quả này có thể xây dựng đối chứng và phép so sánh, nhưng khả năng chuyển sang một đường phản lực mới chỉ được hỗ trợ ở mức phụ thuộc kiến trúc.
 
 Chuỗi cơ học làm khung cho MP1-R gồm: áp suất chất lưu → đáp ứng màng hoặc vỏ → phản lực hướng tâm → lực pháp tuyến cục bộ → giới hạn lực ma sát → trạng thái trượt → đáp ứng uốn. Các hệ áp suất dương cung cấp bằng chứng về kích thích và đáp ứng toàn cục [2], [3]; các mô hình cáp và lớp bổ sung cơ sở cho giới hạn trượt và độ cứng [5], [6]. Việc nối các phần này thành chuỗi hoàn chỉnh của MP1-R vẫn cần những giả thiết truyền tải và quan sát riêng, như được giới hạn trong Bảng 2.3.
 
```

### Diff --cached có trước

```diff
```
## Protected manifest gốc

```json
{
  "requirements.txt": "dd51d73f26c921cacad3f4160d23ec5317335fa0c068f87ed890a812c7c86210",
  "README.md": "4c6fb74eebf72a9f93ca48b0cfd5042f0a62cbe265a4b0f3d8bd7e7c800f913a",
  ".gitignore": "3998232ca7f581fe989d3b2afc63fd2271df929666203b568a219f5743d4a4d0",
  ".env": "e927d0d5202c34d6923cc422f83ee144ab0d2d17292684f0e82ad63053c01081",
  "scratch_search_s2.py": "94d33d488d139865fd6f41c6b40dda324e39b378274c779535790380b2a812cb",
  "AGENTS.md": "bf6bd863326f85f1f77eeccaec10928439555b939a6701fd5134aec0a7abcd00",
  "docs/README.md": "ee87dd76eaf983521550499cc5662f64f331347cf0fab89af4cbe5cc285a5fc2",
  "outputs/gap_search_plan.md": "1fb6e2e8c96d6310b5d4e2b2b409e674dd35555ac68c2e414867d71cd0bb7146",
  "outputs/candidate_directions.md": "c9c168e6183992c10d6dfffb0f9f06db4278ec41cb4ee77027c2e69d13aee3af",
  "outputs/gap_verification.json": "70874c9af6da2eee31522c71c878d6e32b097532dc90502d1cf86d2e8195b652",
  "outputs/final_adjudication.md": "5d9e7e4794d2ff9aaf27605f44bb67007da3a8d9c4d715ef42932caa6ed76435",
  "outputs/corpus_synthesis.json": "49b4b30e0d915f1d549d141fed38ff97af2d5819bbb6db7fbb280f961e21cb92",
  "outputs/final_adjudication_raw.json": "42cdf52af49bd4cd18c9b1f7e3ff1d2d49243dab23df8c03db052a9d442f50c0",
  "outputs/direction_critique.json": "5872464efa0be33dda7f778846e289611a50753138dd55245ea3166ac88747ab",
  "outputs/candidate_directions.json": "e35c84f802cf20845f1f8c3fb6f469f3aa7c9fa2a4950bfd1f3e67b42321368f",
  "outputs/direction_critique.md": "1ec90c8c05be70e07303ed0917c5ad707c96c961ae8bf1c386769d4123a6452b",
  "outputs/literature_matrix.json": "869346a03b1d8a294c7519e667ea51ff3434ff5bae529120e994d5c8e54c31c3",
  "outputs/candidate_directions_raw.json": "a34318e45622331cdda806549753b9766a0de37a694721ac7cb27330d2c449f0",
  "outputs/final_adjudication.json": "660481b703d702168582d8d0badba23edc88ac053c757e4c99b2230c2b364fb4",
  "outputs/gap_search_plan.json": "274da85205027a56b40b282a45aa8e72b0a9d07e8bac8fa83eede644c6cbc29b",
  "outputs/direction_critique_raw.json": "4418c7cbe61a2f4e24d8816f82fa1f3c3723f584b1e19e0ecd15c5b11e8c594b",
  "prompts/critic.md": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "prompts/researcher.md": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "prompts/literature.md": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "prompts/judge.md": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "data/LR-FORMATED-rewrite.docx": "7bff33afc673816984cbe417bcf513e2fbafd9243301de3aa37ff57c4102eee5",
  "data/paper_registry.json.bak-before-dedup-D1V003": "7e24efdbf540d227e33fb58e797cd3ea94f4ae65fc6819240e8f8ff0bfc6f491",
  "data/paper_registry.json": "6e1c92f5c305f1cd29b8514dbfa0a847f1fbb1a1c10a3da953cea16c00caa5da",
  "literature review/MP1_WRITING_EVIDENCE_FINAL.zip": "d33cbdddda00f38e63c2bbec38658d4c13f183b026f2442a361f2fbc2ea141af",
  "literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx": "e41e3638abfd27d3c7b7f60c538cbecf719651d22fa8efd27da8ee2b4b52ef26",
  "literature review/Telling a Research Story Writing a Literature Review (Christine B. Feak, John M..pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/LR-FORMATED-rewrite.docx": "ee5b700f8dc6701eea44dd4679519049fa95d45a299b39ed411a58793ca3652d",
  "literature review/ma-tran-tong-quan-tai-lieu.docx": "ead3fb5c00004f7444545d622760430673a7bd787c84df456d8239ad4823bfc9",
  "literature review/~$-FORMATED-rewrite.docx": "9e62bab38175dd43e2235fd8e880726f73509c57fb3f36fce2c7a0b3776f0dd2",
  "literature review/~WRL2785.tmp": "f4049fbc37d790430e030a3a951eeb484814526c1f5f5b56df8dbb05ddabaf74",
  "literature review/ma-tran-tong-quan-tai-lieu.docx:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0",
  "literature review/LR-FORMATED.docx": "d61c30a5973f3bd2f0314bcb3df253fe1707ad4dedfeb2bf1f76a5d895eb8a1c",
  "literature review/LR-FORMATED.pdf": "e0a0893a6f6f1d92881e9e3fdc5f85f3058edbbdb2c76d16756d95dbcc2ee99c",
  "literature review/MP1_WRITING_EVIDENCE_FINAL.zip:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/~$-FORMATED.docx": "84e28127f73d6d6e2ef9b1d4a7838978fc4dc03cb00b586b7ff687a3c39828f3",
  "literature review/LR-FORMATED-rewrite-outline-de-xuat.docx": "3053b2649293ac1841de835a15687392beef1648a5de26faf6f78b5b3d78b0e4",
  ".agents/skills.json": "5a932ffcd3c3c31ebb6d0353d8a381a1f5cb3d470ab372309097a16c73e89acb",
  "tests/test_citation_export_infrastructure.py": "4d9ab8f0eeb3cac1548ad4808b78a695f9ab020f008c222c009ab08fd2dcf767",
  "tests/test_codex_provider.py": "68ed966eb49086b6ed044323c3655b2bbcef434467666e158d6097f105a38ff5",
  "tests/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "app/graph.py": "7885d401a3f49e351e394a1f2d5ea58f97194241aadd3f3165b215d873b87413",
  "app/budget.py": "e30aa0f5ab8b68f68459ef918e11af73c2d3e9720cd1378caa979ee7a3aeca64",
  "app/main.py": "1fdda7edccf9b3f99e7f41accf9d1f95a6381ae69158ac7d9ff1321247e13574",
  "app/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "app/state.py": "6fefed95e0768ee9d131d7189e138a9e684d3f010b3b2ada74149f20cc5e6d8a",
  "app/accounting.py": "ff88d17293186eda1196a570c2f9d4bf9f211b3f2892044d6e037e532c0c268b",
  "scripts/annotate_paper_pdf.py": "b11caa73b12ee392437cc4548b7728256512a3bedf2345c07a14ffd4300844d2",
  "scripts/build_w2_06_orchestrator.py": "0ef5b643685e76434fe947ad81586334b54285d2b9c3984755bfb209badaa40b",
  "scripts/append_framework_to_docx.py": "62eb16ce90c84b8e01b7e3aeb7c3fbc7214a73223662febc9a7fc9a9ba7d2ea2",
  "scripts/report_helpers.py": "2b3342a947809389fb3675dedef04874d4874d4278dc151d4a6b1fb10d626463",
  "scripts/generate_w2_06_data.py": "8113fde6f500465d4184a43e8d85c97fcd8d5535333b7323f0205a53d447be4b",
  "scripts/build_w2_07_orchestrator.py": "ba3cbe54120a359adc547c031f7d37f3637ccd7f302f9c543053d3546950970d",
  "scripts/make_crosswalk_and_contra.py": "918e2272ac4801f065976a35b87c240c2bb88bb37e137bcedd48710f4d778190",
  "scripts/build_mp1_mentor_report.py": "4843a9beaee78b625526685c790ddcd23f29552d0c8664ebf5817b83acea5ed8",
  "scripts/make_w2_08_k_tests.py": "bcc991f377b7b1ea434f55e687606777d9a3405f912e226df3051296e634031a",
  "scripts/make_packets.py": "c329ac5e49bf1966884d77cebd27c5d9a81f56c309aeaa1c2681fc8611f09c3f",
  "scripts/generate_diagram.py": "e60bc287412f4f77ca461a1700e357420e96e28b83eb411208c934614c94e600",
  "scripts/convert_mp1_to_docx.py": "ce222a9503510d411f25438fa163c55c8826828ae6e74f0027fa2d03acbc047e",
  "scripts/make_remediations.py": "34fa450ee573546413481542ae9b0fd8cd8111fa74548c3e9d1da002d785394a",
  "scripts/build_w2_08_orchestrator.py": "1464ab71baf36afb4cf9ff0258919fa782fc0bfa5d126b768a59ebf776af7dc2",
  "scripts/chat_ai.py": "d1f4dabeab16b1b537d631dc30acb8f610a2d531e4c4bc4739c1a5f99baab108",
  "scripts/convert_report_to_docx.py": "12cec00375dc013729c258ce82bc76c4592c8df9660e54019d6e225d2d53e760",
  "scripts/build_final_mentor_report.py": "1e02df8e9c9fe7117c81f6be06135fd77daabdfb3c486219517a8b696054e892",
  "scripts/build_w2_06_complete.py": "c5d33e41b5767a18dd8152221acdaf671dc44f991a24cf2b95b1b194e28f2afa",
  "scripts/test_docx_builder.py": "a444469bf1a456351171eabad6eedca648d086f481692206742ea16bd77dfd37",
  "scripts/generate_mentor_report.py": "7b5a3c098abf4bc4e223f1ff7a0e4c5ae621564cfe39dfe60fc086d47bd6c6e1",
  "scripts/generate_mp1_evidence_matrix.py": "f7f7e5b6007d2c1d3c9f31836870100aec5dab32107e48f12a11d571d4937b77",
  "scripts/batch_annotate_mp1.py": "ca482b738de829b51d8cb67d49c949c72499b3725d99cea76115d0c209c10e42",
  "scripts/make_w2_07_candidate_and_threats.py": "263dd05322cc19745dfd8ed85ef9f6f042f383b6a4f277afda933c9e457d6c2c",
  "scripts/make_w2_07_contradictions_and_provenance.py": "7d23c0d73e22433c455e86ab3f8744f5320c480e706905f573adfb2bcc99c2d3",
  "scripts/make_w2_07_non_novelty.py": "9046e039afc0c79d2363f4cb295cbd9ed2cc461cdc9ee17ab2992ae148dcfac8",
  "scripts/wsl_antigravity_bridge.py": "b019e07fd40f0a07c6355116873f7131e918bc8da72d0269253323857b323f1d",
  "scripts/make_critiques.py": "d61433177ed7ac18f46a4d8467e31154c9f26b1399cfb61021b163575c899cba",
  "docs/literature/MP1_R_PHASE_5_RESEARCH_GAP_AND_CONTRIBUTION_ADJUDICATION_2026-10-02.md": "253629f4e5811b5ca184415b7a0acb403dd9025238c8249f86bcde74d7af29e2",
  "docs/literature/MP1_R_PHASE_2_DEEP_SEARCH_AND_CORPUS_MAP_2026-10-02.md": "f60d89fcabbd5028ff92464b18fb469fdd909168888b170853f2ab0a3dd042b1",
  "docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md": "98cb37bc018a42fd5682964606a3ba0d66f43176c8d132778abcea2b5d3f1d2b",
  "docs/literature/PDF_ANNOTATION_REPORT_2013_PUMP.md": "576548af10cc8409286e3d050c71269033aea24cb85661d6ad63ebd29d7efac3",
  "docs/literature/MP1_R_PHASE_2_ERRATA_S18_S20_2026-10-02.md": "97421ffa94a78835a8724e564877dc9753e0a8c9d7550d29dfcad8eebb77ebd6",
  "docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md": "4dd71b45f52a0e5bb18f92c3a76064aa4e395bc4a9feee19f827d6f463140f08",
  "docs/literature/THESIS_READING_LIST_CURRENT_VI.md": "ce5b9d62da5efab09c702f2948565cf3ba901c36fff2f71a317eb5cd53a64f57",
  "docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md": "e5650636b3c8858394b619bf3f06386b65a9827bdf8e73d18f777144d57d6f7c",
  "docs/literature/MP1_R_PHASE_4_CROSS_STUDY_SYNTHESIS_A_GEMINI_2026-10-02.md": "d05459d657f90365f8465e9b3fa893cca1f72c8afa3cd1bb2aaf86558245f0d3",
  "docs/literature/MP1_BULK_ANNOTATION_REPORT.md": "a72a2528b017b892d91ac10bdfb43013a11c2e0d92c8fc2a30d9d8e034b67c2b",
  "docs/literature/MP1_R_PHASE_4_CROSS_STUDY_SYNTHESIS_B_GPT_2026-10-02.md": "4a5793ef4e7df3d62b898d729cc1be7e1d60d738926b0faeabd985a65b75949d",
  "docs/literature/LITERATURE_STRATEGY.md": "2a4853e7228c66273916db8e129ff2a42d76b76bae418e7f6e368ff644cd32f6",
  "docs/literature/MP1_R_PHASE_6_CHAPTER_2_DRAFTING_REPORT_2026-10-02.md": "29b65bcd2d8050f3a70c3e76ee3eed8bd845a47a8c3decb67d695c08097329ce",
  "docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md": "a948bd201fda61b29de142e40a95606cf47a7c83d05c2a81e7683db371e9453c",
  "docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md": "ca00e83f44803666f8ab7509ed585264cf88a1b980eac1be722e6c84af8c4195",
  "docs/learning/EVIDENCE_JSON_FRAMEWORK_GUIDE_VI.md": "f6b5a693936d2b50712114dc8518eb62c36e0f794e5e8bee265d7d8020b1772e",
  "docs/learning/CURRENT_RESEARCH_DIRECTION_TUTORIAL.md": "0fc9a203f1c09da57953dce55e5f7a3b48497bb9c31f91f8ec57b633a131d98e",
  "docs/learning/ZHANG_CONTINUUM_PAPERS_READING_GUIDE_VI.md": "db6358858352e5f2ef7f663000b2c45cb337e4a2257708ef945eee38db88095a",
  "docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx": "833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b",
  "docs/project/POST_D1_V009_RESEARCH_ROADMAP_VI.md": "43f43d17db00ac68917cccd23ebf1e4cfc4e9b61b569b85e711a1d5d7c9eaf2b",
  "docs/project/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_2026-10-02.md": "5b3ee8e1032de8909b0146ad3a1f826ad31a3f10fc9308107117d4424325d136",
  "docs/project/MP1_CHAPTERS_1_2_WORKING_DRAFT_2026-09-29_VI.md": "8ff36e2327b4a6de2f43a051a805646b648c91a7ff1d2e75e46ec552709bdeaa",
  "docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45",
  "docs/project/RESEARCH_STATE.md": "f302c37003601a20de6c148b5c84a6824618df4bcc9c34e5d09797ab3b1f3296",
  "docs/project/MP1_CLAIM_EVIDENCE_REPORT_TUTOR.md": "6136c4d4433675d471953f5683d9a82beff4b2a11749bec037f7318c9bec3587",
  "docs/project/MP1_MENTOR_FEEDBACK_RESCOPE_2026-09-29_VI.md": "8eadfc48b2d1b64443543f11c9993b538ecad3b9b90afdda80c07ea41f4c4a9c",
  "docs/project/PROJECT_HANDOFF_CURRENT.md": "b84cde745e54b6b7ab83fe7da67d8e31f4ca7c38533a2f2bd81dd16673658423",
  "docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45",
  "docs/project/MP1_CHAPTER_1_2_WRITING_PLAN_VI.md": "682554cc75d871bc050cc37bf478b2107356be67d0729c1771b05273a60355cd",
  "docs/project/MP1_THESIS_OUTLINE_AND_RESEARCH_MASTER_PROMPT_VI.md": "21ab597f5875bb2683913a9645bcbdca668186040789aa6a3e797173d8e94352",
  "docs/project/MP1_MENTOR_PIVOT_TUTOR.md": "df5a7edb7c71ebb8b20f9144164eed515c1f8811472bd9e61c396399fecc32be",
  "docs/project/POST_D1_V009_RESEARCH_ROADMAP.md": "d0aa08b8c7a42aa196d71ba65c63b619808452aa84922d19cf4a11e5717c2554",
  "docs/project/RESEARCH_LOG.md": "7cd88db0b06ee2a8ef01896412a469b0447dd83b7fbc8e8b21a8e3ce692cd575",
  "docs/project/research_state.json": "70b17fda40524a9e1c81231d6d969048cff5bcf0fc33052dffd85f75eaf58c67",
  "docs/project/CURRENT_EXECUTION_SNAPSHOT.md": "f2a673fe397f879ba1c5fc1dcc55649855c2c876c430490e28e4a4519f813fa9",
  "docs/project/MP1-V002_CURRENT_HANDOFF.md": "fe48c78ff4e7d4437c17dcc044caf98e8df963349b01853968c3235ec7a2d025",
  "docs/project/NEXT_SESSION_START_HERE.md": "f2ec58cbffef9b90c8d3c8640309f30ae1d42014cc1bd5b75b5a14f5ad635ace",
  "docs/project/MP1_MENTOR_PIVOT_CURRENT.md": "9eb6cd362729d7aa1ea6b0094c21f753b3c0f011d69b7c112aa4deedfd1df3f8",
  "docs/project/MENTOR_PIVOT_STATUS.md": "b73c248cef5214fcae49261ae2506830d298922eeed10299976d407317bc9f7f",
  "docs/project/MP1_STATUS_AND_NEXT_STEPS_VI.md": "1a9b89f55d2ead283631215e300833928eb8c9bf97b85599fa594028ac043341",
  "docs/vocabularies/README.md": "ac25e61b8c8c0ec88f579b2002156b511b575be454cfda2a66b3ab0e543b8987",
  "docs/vocabularies/21-09-2026.md": "a548145d6a90999fed380ccfe072c22b48e41e0234de8c73fa3ca80e1a572b56",
  "docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md": "a0f15375f50caae6857fb2a865709186e4d37f17f923b66cb480182f060f41f7",
  "docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md": "f53f896801113150bd83e84d6c68dd542804fc65a619ae34fd568e7f7c276a99",
  "docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md": "271a15428e5c265e98dbc86bc7c924291e3911e3d592b3ba6d98f5712b510fcb",
  "docs/reports/MP1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.md": "5dbc563cb7028ce8cce94a746122636d3fd0b87abf364a5285992bce6a1d2adf",
  "docs/reports/MP1_CITATION_COMPLIANCE_REPORT.md": "790eb32de83f705b32fa4e84037bcde72034d16e7698c3288e1a0810ec7fb64b",
  "docs/reports/D1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.docx": "7bb4e70ed9a22954c482d7437143fd0112765d2cd7b11e4be6235e2308d244d5",
  "docs/reports/MP1_MENTOR_NARROWING_REPORT_2026-09-26.md": "79726226bdb95e05f26c6f498c18d940b6c0c8af1750ab4e15253578c5e4fe17",
  "docs/reports/D1_MENTOR_RESEARCH_NARROWING_REPORT.docx": "6c7e6c03ef055f49bd51bf613e87158e9d3d5c8e2e24686ad8079edba09ed984",
  "docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md": "af57cc6a53c38ea430b4369d6afe7df86f61956d3320d7ce3977f957f5de3145",
  "docs/reports/D1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.md": "d767c51b3456fa7643205c7fdf65cfac9a71614bd582fdf1947d1d20f54fce61",
  "docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md": "ea0c1794cfdcb86ddf375f3529edc052b371c06c9caa23d8ce32395cf829484a",
  "docs/reports/D1_CITATION_COMPLIANCE_REPORT.md": "3647302e5cd490806a82eff663a71ca4bad0022d5bf2e850989582db6f1c2625",
  "docs/reports/MP1.docx": "492fcb11cd35f3f16d73c8e92576f9869a99d6edf373b13b7e8330393448479a",
  "docs/reports/MP1_MENTOR_NARROWING_REPORT_2026-09-26.docx": "5445a557dbf65c61528ac8ad682ffbcff9ff65b23a2f0666dcfb8a7d6f4f0fb0",
  "docs/reports/MP1_MENTOR_RESEARCH_NARROWING_REPORT_2026-09-26.docx": "681b22749518897bdb82f9cb90cfc2de5302c5227df2baf5b61f5f8f4c700bba",
  "docs/reports/D1_MENTOR_RESEARCH_NARROWING_REPORT.md": "372ad663be8a811f17bbe17fe6023d9317e001339a6722af691f9bebe5ba619f",
  "docs/reports/MP1_Matrix_paper.xlsx": "be204ad3029984cb6ad15379925f90c44ff9d5c6c4a8ae5b5e3e0810e844ff01",
  "docs/reports/D1_FROM_54_PAPERS_TO_FALSIFICATION_SEARCH_VI.md": "fee718bb458caea0f47ba931955c3b14c58b05397dee147e9279a062f2989937",
  "docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md": "2d26d9cbd7883442428585de82b53b320f28a275937f94d724097a61723ac166",
  "docs/operations/KNOWN_ISSUES.md": "ae4db17709c0d7f5af82746c5a51aee6be03cb7d1513335e68d91212e3f1bfcb",
  "docs/research_design/M1_RESEARCH_ARCHITECTURE.md": "7bddda804bfafcc55011cd90c3a9983a245ba069868c61bb5b8c5a13b5b77f17",
  "docs/research_design/EXACT_MODEL_SELECTION.md": "9b9d85255d0c2f6b9a0a7b522af9c10cd93ef8befdbff242a730dbf8e2f90981",
  "docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md": "db8d8b6f81723b8fdeeed72dd2747b7b2c72dd7c04caff42cc98f0e76e164dc7",
  "docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md": "6b2e210b46791bf990075dc4d4e3ea58c266722aa418be39827ebf38d01de156",
  "docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md": "5f72a12e1052cda57e6f7e9d57a6f6e2311b118f6b0c49c24bf7a40cd253e30e",
  "docs/protocols/D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md": "b6d69e7ed922562ffaf91042fd450f3ac5fb64b32007a4604a4fa59050154476",
  "docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md": "cbdd30f5b35dc487d38b6182cb74eb7dfee95a23025b1654b4ab2607513d859c",
  "docs/protocols/D1-V003_LITERATURE_AUDIT_PLAN.md": "2078e6e9997c01d9c19ecd1f66d143bcebe55714454942c012d66ba8acf9b999",
  "docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md": "a4022362286cde0c6a5764ab0cea7e7c37449bec54059b3e56a592d43d1e0173",
  "docs/protocols/D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md": "25dd679749a9a164a3297e0aeb773f5e818835c553d8b276da7c0d9a3149c574",
  "docs/literature/paper_assessments/YE_2024_PROJECT_RELEVANCE_VI.md": "04dfdb37b8137a51b549e6a416368e0f8bffdebe3b6ad6649b7b87e604a0f3eb",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/source_bundle.json": "23b198df73c98fa6cf89bbe03a81c48a3a2e48194c48a6b1946f96ebd0d8640b",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/paper-card.md": "b0e0e9a043be9b42adf5ccb2fa938a748ac7eb3cfb0d099ee67f673ce0d90e0c",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/audit-report.json": "5890257ca3c326fa4da9d1448650fcb2e70bdaaa0e3548c296f21512c803aa86",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-002.png": "a290a96bf1ca30a5b3ea2afabce4ae12a0569b776e084901a17288cc3fc3c211",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-010.png": "5afc5f0fbd64c618a8621ea8f6781904b46eee7f15b1b83ccddf4074678bcfd2",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-009.png": "2efb47c35fc6646b7aca05f2a107a2dc5c34e25ddaf72876c3bc2b2a184f5eae",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-001.png": "1d0756a27d8a7af2258a0e991cc76d2c2a097b9a0b571a7d4e8ef9c2904652a5",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-003.png": "be037131c4878e48fbead3a80ac7b501a34ddf6e9a1e1e4e5271f295e9e87c8e",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-005.png": "985ecdb2779b3e8ebcae6b19b8e9667508be4edeea3a01394e332a443fe7e647",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-006.png": "5337a360f54baa1f9249d8fb9b03c87052652eb7f1fac2e7ceb8e8ab4bced8e4",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-007.png": "c52366447df9ed885b1eca3461b0916ccf3c50746083bf8fdc9a08c20c579f99",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-004.png": "0b3e4cb9d9bd61cd99db094541841ad580ea0515625a21c8ad3c0ef3a9d10db6",
  "docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-008.png": "a69cd9d2b372f471ff595337abc27c3937427dd79e60ee7ad7c9c247f8fd3b94",
  "docs/project/almost done/LR-FORMATED.docx": "a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c",
  "docs/reports/figures/mp1_narrative_narrowing_diagram.png": "c7da4dc36877f1695b2afe5932e252f6bcbf8bb8bfb36abc690ab9493313f3e4",
  "outputs/research_runs/latest.json": "351f82121eda0ad70d6f108d9c47d2df8f88c6ba86c6ede17dd61fbbf803a768",
  "outputs/research_runs/run_20260913T164606Z.json": "96cdbd67d4fc639fe4ed20aaa7ac998ba1d21f54c059b2d63adb76e0ee2645f3",
  "outputs/research_runs/run_20260913T165853Z_recovered.json": "351f82121eda0ad70d6f108d9c47d2df8f88c6ba86c6ede17dd61fbbf803a768",
  "outputs/research_runs/run_20260913T163800Z.json": "73a0e0bcf06a7f4ab480898f6f7dde79914b0797f85448cf81ac5803638c5811",
  "outputs/literature/LR_CITATION_MATRIX_2026-10-14.md": "2bb833a7bbb3dc0d77521e81ca68445af0d4b455e099994ff2acde9e7c1aab2a",
  "outputs/reasoning_batches/batch_008.json": "62e07a328e756e89946afb7fe54f74ec10275486639de2058baca6cc98b7f292",
  "outputs/reasoning_batches/batch_007.json": "b2cd0110247eb6a43e87a0424d50c651133301df52544ada2c31b5f2bcb8bfbe",
  "outputs/reasoning_batches/batch_006.json": "f94e15cabad57af787ad89b83daea121df1d344318b3e4b426f38e95b57325b7",
  "outputs/reasoning_batches/batch_009.json": "5989f37ddcceac81180510463a71f462ecaa80f3fc4bac796cced965a22e665e",
  "outputs/reasoning_batches/batch_003.json": "056865e78abec0b4f9daaabe05bcfecfba83b815b71c6ed7c78aaceca92802c4",
  "outputs/reasoning_batches/batch_005.json": "9a4e0d046dde4f4f0312f013eccf30bd44cd231d3497c51488d03819360f1bd5",
  "outputs/reasoning_batches/batch_002.json": "d55839f6a22fd62e43e48c5c3c261e5eb1658e56bfe8c436e5f60c093b0e3c06",
  "outputs/reasoning_batches/manifest.json": "616e2fb8b03e0eff44724394ffc78aa06e150a1b51eba01ddfa7937b52be6b53",
  "outputs/reasoning_batches/batch_004.json": "50f9879e652cabc72219cd97a04aa91ffa5f71e16b246cfa44d465d4ca9dee71",
  "outputs/reasoning_batches/batch_001.json": "7c14d35074f721193615236d61ab77865d9150c0c73323f82abf818ec3389052",
  "outputs/batch_syntheses/B003.json": "c92214360b06eb9ae4c1867f38c6ffa1388bb0e0a00d07966817c8349cf8619a",
  "outputs/batch_syntheses/B005.json": "42568f3d6ac852fa1a62ffad6cc7036e77c60283153663ff4feff156841bb688",
  "outputs/batch_syntheses/B006.json": "376a34f5359cf223764bd8e999cb47d2b115a0f6c8a55d889ff17b80cc0c4f93",
  "outputs/batch_syntheses/B008.json": "043f17c471ea819b7a42053b712b2e8ccfd5d4fb3a43e2c3ac46ff5cc808e9e9",
  "outputs/batch_syntheses/B007.json": "f6b6b29179345fad86357de8e027431f7d1decdf04e5a6901afdcb268d382096",
  "outputs/batch_syntheses/B004.json": "898a25455ed1a91a60a6bcc9327eaa3d0bf5c2451c6c48359771501dae58e08c",
  "outputs/batch_syntheses/B001.json": "48c54ea0cb60dc8a1ee7b733cc6e23eb9fa9e9cb4b7aebed1a5c51c6352e9e8f",
  "outputs/batch_syntheses/manifest.json": "0977b3660b9cab5acfb20ea12cf321847cc56bf9c9e5cccadf3a98cc5cf6a39b",
  "outputs/batch_syntheses/B009.json": "1a88a43429877e6e6b523ba053c7c6b28c7393877b5082ab7b698f36f67b8b4f",
  "outputs/batch_syntheses/B002.json": "9a5d0b8461849184017dd163dcae80020da5a9fdf6acb45eca8b8360d3773946",
  "outputs/plans/D1_ARTIFACT_OWNERSHIP_QA_V6.json": "71cf54f2e486e9a8b972994d4692ca454b54b6bbda8d3bcd9d9f04fbccdd1190",
  "outputs/plans/D1_V3_REAUDIT_FINDING_REGISTER.json": "20befbd206810b65cb4cf999e0c7c28204edd0a0e3b9c99f7e8cf520ca03a7de",
  "outputs/plans/D1_HARD_GATE_MATRIX.md": "ddac38b9842e8cb284c24bbb9b4632aeab63694d9390be35092fc7b96fd9b3e3",
  "outputs/plans/D1_HARD_GATE_ROUTING_QA.json": "debd7e57fd34453197b7477a9cf5a60c4c13a86a9ea9863164b7fe6dd6e270e5",
  "outputs/plans/D1_V3_TO_V4_REMEDIATION_MATRIX.md": "02f1fe3073102b3b2b420b6cb7b2d543192b6d1ac66df7a8422448e8c866610f",
  "outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json": "3bef4fb970e65913196e9772e22384dd5e7d040373afdef378eac78f81ac5b45",
  "outputs/plans/MP1_R_PHASE_4_PHASE_5_HANDOFF_A_GEMINI_2026-10-02.json": "ab5e1a362cc64d1d089ceb9bce59a985d25b548ebb4a3e247072b1fca839cb22",
  "outputs/plans/D1_ARTIFACT_OWNERSHIP_MATRIX.json": "e9c73abb4a1d5bcfb0dc4e2c5942484d805c113dcfb699e36d88034543298a8b",
  "outputs/plans/D1_REVISION_ROUTING_MATRIX_V6.json": "1f2cfadac0646796828be853b92219ba43dda58d7c1f5056cdc5938471ff119b",
  "outputs/plans/D1_ARTIFACT_OWNERSHIP_MATRIX_V6.json": "4a856be1ea9464087212d1971c69bc7629ab9711c5a6633a625b8d3a577b5493",
  "outputs/plans/D1_MASTER_PLAN_REAUDIT_V5.md": "830a42dd59d588c10817a55657985bdebe2e135209d9753ebba9d5fa38935f6e",
  "outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json": "a5e7efaa88155129f27eec425caf7b83521c600e4c41d491932198aab0d8c6ed",
  "outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json": "dc5f3a96b1bfe7a22f2ce79b2cea399af4255ef879548bca40f1da5e4d10ecfd",
  "outputs/plans/D1_V4_TO_V5_REMEDIATION_MATRIX.md": "8faf291b42c79b424bf1c73e8f29a9bb277d564a0dfc8cbac66f39bed4233402",
  "outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json": "4c43ba1f67921c857f0ab50190e227b1ad7221f6a9b6f0a15f5af9ca1c7ff0e8",
  "outputs/plans/MP1_R_PHASE_4_PHASE_5_HANDOFF_B_GPT_2026-10-02.json": "dcf11b693b0f4080fdfc07d949f2085b34b925aa3cf0fd75e90fbc30095e3194",
  "outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V6.md": "16600bd1bb28e7ac1c62e806b801d4ae1ac67cba28e7f14554a711294c98eb58",
  "outputs/plans/D1_V5_TO_V6_REMEDIATION_MATRIX.md": "9311c63ad699b3e891bd3355cf53096d4a475c67685507ac09da0faf8740609a",
  "outputs/plans/D1_WORKER_EXECUTION_READINESS_MATRIX_V5.json": "092ca39ec4e1d534be51fbc554524b01f479a661f6e2e953c8414237014275d5",
  "outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V5.md": "a73c19f385f26c5e927b30112cd4f89b43367538057854b04c5def16f0f44580",
  "outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V2.md": "a4797f765a5bd7c5561707238b9a9bf1420df8f2ba0a1438d66d93d8f114bd34",
  "outputs/plans/D1_MASTER_PLAN_AUDIT_V1.md": "eb41cce404be164e61866ef80dcf87f1a8e1ab2b3aa8c24e03705a55929824c7",
  "outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json": "5a5bc1912919a022e37f5a544be7aec25880523ded14ae4b0455125a1ac045ae",
  "outputs/plans/MP1_R_PHASE_6_DRAFT_METRICS.json": "f2da89e79c614fc42c01b5366a7b2aa60e10bc6b0c9308fe9491d25b49c82046",
  "outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN.md": "4170a2607b7685ec94643b1feb610b7ce698dcd245ba449ea30cd5ea9c8989e2",
  "outputs/plans/D1_V2_TO_V3_REMEDIATION_MATRIX.md": "a6cb8208858118b1f344388ad755fe401e92a6f934067b13b4c7deec34be1a2d",
  "outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json": "e6690ef5f0b214935e493597ecce089f780ed198f22fcc12346ce50f7759f558",
  "outputs/plans/D1_MASTER_PLAN_REAUDIT_V6.md": "8fa073d6f022a3876d0d86fb647d557b14e689d131907f0c3fb539b534e1abb8",
  "outputs/plans/MP1_R_PHASE_4_BLINDNESS_RECEIPT_A_GEMINI_2026-10-02.json": "c43bfb6535a4ad18789bd4a6ced119cd6286eff6c126ab30d542b41ae974cc55",
  "outputs/plans/D1_MASTER_PLAN_REMEDIATION_CHECKLIST_V1.md": "99fe0218e664b9344ab2d6fe51de8beb71f6f5c2a02b3f1c8dc14246a36af240",
  "outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V4.md": "d431901cb7203a15930759d7da37c95de170a2f988d7c6f6b151a2b353af7286",
  "outputs/plans/D1_MASTER_PLAN_REAUDIT_V2.md": "61a4a89ce1c97c59e6ac2df8d1a39138afa33717a7229eac5e323dd536aabe6d",
  "outputs/plans/D1_HARD_GATE_MATRIX_V6.md": "d844d84bb9f705508ba9d8518233529a360ac9979bcb4e69aa4693948a4c1e92",
  "outputs/plans/MP1_R_PHASE_4_RECONCILIATION_MATRIX_2026-10-02.json": "b68e2c8ce983bca053fb497a2ce71b5805c9e157211d9ba0aabf9e0604931b34",
  "outputs/plans/D1_V5_REAUDIT_FINDING_REGISTER.json": "ce6a95e335485908041aef2cc8462f865657f0682d95b509805cf426f787efb8",
  "outputs/plans/D1_WORKER_FAILURE_ROUTING_MATRIX.json": "f36535ccb1c03b293344f53867bc1473e193d32ec666bfcf7105114b98fef6de",
  "outputs/plans/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_2026-10-02.json": "96ee61e6c385b9a5029b5f9e2a6bed4b8e2dd09e95eace43afa97719eb401aff",
  "outputs/plans/D1_V4_TO_V5_REMEDIATION_MATRIX.json": "65c475b79e3f58d97b0d0df62e4d3c3943e11fd807a6db249483d3b34efec53e",
  "outputs/plans/D1_V2_TO_V3_REMEDIATION_MATRIX.json": "9451ee566d22179ca7c2aa82837bd1c4f1b22dfb956f431fa62a74fc436d9da4",
  "outputs/plans/D1_REVISION_ROUTING_MATRIX_V5.json": "936c8798f007e870746fdc0023f55c2890935fd71b67b464a1391fc6b1225623",
  "outputs/plans/D1_HARD_GATE_MATRIX.json": "ccd4cf47d1dbbc37544cc45c3745da801cb90b2c53d6d280c029c323f78a55d0",
  "outputs/plans/D1_WORKER_EXECUTION_READINESS_MATRIX_V6.json": "5ca890c1e6f8faf0a903093dda54a91703ed120a1bbfa4a1e3ef436e3537b9ac",
  "outputs/plans/D1_V5_TO_V6_REMEDIATION_MATRIX.json": "6977bb2f2516f072403818846738c7eb9a7bd8d4f0175f8235a2c2ad7ebe36d5",
  "outputs/plans/MP1_R_CH1_CH2_EVIDENCE_MATRIX_2026-09-29.json": "890c28fab896569dc1a60b28d6b6c45792be78a837bfe57cf08487b1f26d24a0",
  "outputs/plans/D1_WORKER_EXECUTION_READINESS_MATRIX.json": "6c59c74d70ea6d2a5428ecc8554acb446a38697c5b90fc13bffd98163c4c98fa",
  "outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json": "cd99c169e1f925756746d0e49422d30fd325b7c5ffb9191175bbf8a8970a2f3e",
  "outputs/plans/D1_WORKER_ROUTING_HARD_GATE_QA.json": "da59de9f1b4150f49825a3dc7bcb160962d693d410387371d1bdab664a98efc9",
  "outputs/plans/D1_MASTER_PLAN_REAUDIT_V4.md": "82fe4dbe67430a2099f1df5acec83f487c7e7b5f3e22cc80dc7e56e0ff7559b0",
  "outputs/plans/MP1_R_PHASE_4_RECONCILED_PHASE_5_HANDOFF_2026-10-02.json": "550ac4394043f6fb9b1920fdba702751864acd3eb2325c2486bb673c65c67f5b",
  "outputs/plans/MP1_R_PHASE_3_PHASE_4_HANDOFF_2026-10-02.json": "d47c33316e92397f0c4a0ba0512562fb8e06665f41bfe0b56471d415a81a854b",
  "outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json": "c3ea4d1eddc144cf8474746c0eed87262b1a4298589ff01ddfe181f8bf968cd2",
  "outputs/plans/MP1_R_PHASE_5_GAP_CONTRIBUTION_REGISTER_2026-10-02.json": "19bfbcf4994d6e224a979599702764e4af6cc04e8fa0a297879159d01f591c1b",
  "outputs/plans/D1_PLAN_PACKAGE_MANIFEST_V5.json": "d375ba3686b515d0b078928f842dcd9ed5674d863d9e0f98e78c1e35765ed73e",
  "outputs/plans/D1_MASTER_PLAN_REAUDIT_V3.md": "22a413a738efd383b67a831b76eab3a58ac3a862b850b1a29aba600aa43ee728",
  "outputs/plans/D1_PLAN_PACKAGE_MANIFEST.json": "c1f1d658992bb8d87b277b4f461797f4da93a446ba2598af46ee9b748ee0cb20",
  "outputs/plans/D1_HARD_GATE_MATRIX_V6.json": "04cf35148c03a7693e347fc5761f3fe9f5d2b91aedd20092cb3026ae468f2cb0",
  "outputs/plans/D1_V3_TO_V4_REMEDIATION_MATRIX.json": "615d2ff6be5ab2c6a673c621ef7430a5059a7ff44316f50a94eaae15e34d4dfe",
  "outputs/plans/D1_V2_REAUDIT_FINDING_REGISTER.json": "9451ee566d22179ca7c2aa82837bd1c4f1b22dfb956f431fa62a74fc436d9da4",
  "outputs/plans/MP1_R_PHASE_5_PHASE_6_HANDOFF_2026-10-02.json": "f3281e23e46e1c4d8700e955bfd95bf23969a72f30bb699bd534a6e3091fdefd",
  "outputs/plans/D1_PLAN_PACKAGE_MANIFEST_V6.json": "a5ad58bd46e73e9f63ba143ee70f27ce522246fa129294f21a86ae7e76aad9f5",
  "outputs/plans/MP1_R_PHASE_6_PHASE_7_HANDOFF_2026-10-02.json": "0ff3f12759c2ce6ee43eae51076c74098107153844413fee8a120a2708876943",
  "outputs/plans/D1_HARD_GATE_ROUTING_QA_V6.json": "3e4ea8babff3edb3f578c4f79abaae2d66c6b760d00f9f6d27e1b04301a7b2fa",
  "outputs/plans/D1_V4_REAUDIT_FINDING_REGISTER.json": "b79438a6e5c4d50c9677610ca3b175e4cdca0b518efed742f18bfac676c8f48d",
  "outputs/plans/D1_REVISION_ROUTING_MATRIX.json": "821829ba4d66d7497ab0690f43218167fe07464256d49fad2d68b1fdcd1bd22c",
  "outputs/plans/D1_M1_NOVELTY_RECONSTRUCTION_PLAN_V3.md": "947b41571afdca55bf2ec5f3e908ee940ab536d560586796ab611160b921964d",
  "outputs/plans/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_2026-10-02.json": "8d196c0ea66f6553d2ad36815f1d3e86963b0c16868bdbd402b7388ed18698ea",
  "outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json": "86bd644523dafbd66c4a887fdbcd4127f82986aa9d366d5c16b21255a7e56800",
  "outputs/discovery_snapshot/literature_matrix_54papers.json": "869346a03b1d8a294c7519e667ea51ff3434ff5bae529120e994d5c8e54c31c3",
  "outputs/discovery_snapshot/direction_critique.json": "5872464efa0be33dda7f778846e289611a50753138dd55245ea3166ac88747ab",
  "outputs/discovery_snapshot/candidate_directions.json": "e35c84f802cf20845f1f8c3fb6f469f3aa7c9fa2a4950bfd1f3e67b42321368f",
  "outputs/discovery_snapshot/final_adjudication.json": "660481b703d702168582d8d0badba23edc88ac053c757e4c99b2230c2b364fb4",
  "outputs/reports/MP1_EVIDENCE_EXTRACTION_MATRIX.xlsx": "e8c96976dd0c8f47634bfd4ca086c7dd330560f54f4cb4eb525c4137006af92b",
  "outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md": "25462069e0667a67ce680d3fbb3c6879a8d7959a8da3973e9a289706c9638ab3",
  "outputs/search_queries/wos_queries.txt": "c4ec0ef0345b1eefa98037d610b7bfc9b2f4b95be8dd9f8ace4f9ec076b9ed15",
  "outputs/search_queries/scopus_queries.txt": "95730af4f8fe9b90a40f19239dd0bb0297b43e4eaa5f00a9140e30f539345b60",
  "outputs/search_queries/scholar_queries.txt": "2594ae0c1e533416f8eb93397214df2981ee386c8dd19c4fea33680ed6095742",
  "outputs/search_queries/database_queries.json": "760199dec5387d08436bcea3fd5df671f758c01807878a2ba1d6880a502ea9ce",
  "outputs/search_results/search_log.json": "6073d650714cede97000816b1347d93901768146c9b59fe5fd5b49f13d483098",
  "outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION_raw.json": "9271ecdbf3f56791b2a646b7fd684891feee05ce4f6639c1f4d1a6236efe5408",
  "outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.json": "67d9b268ae0ca245ec09c9fb60852da33a581beab701a7e653483a606fe899e1",
  "outputs/final_direction_lock/FINAL_DIRECTION_ADJUDICATION.md": "d520a057d712753f255d503cc7b2353323d3adc14cd2cc8219bf1d919bae808a",
  "outputs/d1_execution/V4/W03/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W03/W03_EXECUTION_RECEIPT.json": "3dc3a4dd01cd4fbab22bd3540221991385fee02fce3a76dbe999f7680848ef35",
  "outputs/d1_execution/V4/W03/D1_HISTORICAL_STATE_REGISTER.json": "06b90156fb58ed7ad31869350599ed71b4d5c3c64e864eb6179c1086ffc7e0ee",
  "outputs/d1_execution/V4/W04/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W04/D1_CLAIM_EVOLUTION_MATRIX_DRAFT.json": "ba0fa8369d59c333698b57392a042efb4010f792e3137fad1e95574a558597b7",
  "outputs/d1_execution/V4/W04/W04_EXECUTION_RECEIPT.json": "2c5cffaf205bacf9c124727359447264578b5654079975993bd69167e56c784c",
  "outputs/d1_execution/V4/W09/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W09/D1_PAPER_EVIDENCE_PACKETS.jsonl": "39c1405ca85004d9cbafcc0905ea7e37726b29fd203d67c17ff0711b3096edb9",
  "outputs/d1_execution/V4/W09/D1_CLAIM_EVOLUTION_MATRIX.json": "84e806848a780d7121be1b5318bb6ac6fbc559d93fa0b2835eb0e748dba90cd6",
  "outputs/d1_execution/V4/W09/D1_NOVELTY_CANDIDATE_REGISTER.json": "ff4ff1174298dc58f7b715335e3ad866c78fad9dbdb80e305822094fa8ed7afc",
  "outputs/d1_execution/V4/W09/D1_NON_NOVELTY_REGISTER.json": "f832008d2dced4a2a7a71c5303d6f35383f75fe9f9159cea0a95eb73709dba02",
  "outputs/d1_execution/V4/W07/W07_EXECUTION_RECEIPT.json": "ba16f5b3c4e095d110b3254cd7e73a74ac89aaba5ba378c638fc903ed5660cfd",
  "outputs/d1_execution/V4/W07/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W07/D1_PAPER_EVIDENCE_SHARD_W07.jsonl": "11f7b31bfccc7b898f737d3754b6fed27d7bcbb556e6264357534ce33f6808e7",
  "outputs/d1_execution/V4/W08/W08_EXECUTION_RECEIPT.json": "4e7af17707fce950489181212feb0e29c94ea403416590680b77beb3575d39da",
  "outputs/d1_execution/V4/W08/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W08/D1_PAPER_EVIDENCE_SHARD_W08.jsonl": "8ed054dfbb61949c458a3f77fc6dd7f00c4b99d69a875888bbe105a63fde4252",
  "outputs/d1_execution/V4/W02/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W02/D1_ROUND_COVERAGE.json": "94f10b174d9ff264fec7ad81f7e31454c8f7605eb5215a72e5fc5ab03ebc2e49",
  "outputs/d1_execution/V4/W02/D1_EVIDENCE_INVENTORY.json": "6e186da6789cba920e9b17fe3cf641582714100f803623385216e15d10403c0c",
  "outputs/d1_execution/V4/W02/W02_EXECUTION_RECEIPT.json": "9f6ee78e8e425fe6453b88de53cfec2332a5ea00b1c0e467fc62c46e8ccf95ff",
  "outputs/d1_execution/V4/W12/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W11/D1_HG06_U2_STATE.json": "5d691116fe45cb2e4dd7e9d09ac9cac5961a13f74c12a855759a28088c61e342",
  "outputs/d1_execution/V4/W11/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W11/D1_T2_WANG2026_REVIEW_ROUTING.json": "7be5b23d3b97201afcbe9d5d73a4f3190589ed852372db1cac99ae99a7e24420",
  "outputs/d1_execution/V4/W11/D1_PROVENANCE_QA.json": "7477ec5460ef49ab9a7d7aed4162026eee08e5a68dbfaa08d62837ce1bae05f0",
  "outputs/d1_execution/V4/W11/D1_CONTRADICTION_REGISTER.json": "4fe0d99f4b6fd0ad37e9829bb9d7c12ce4565d84694258d898b30dee1b317eff",
  "outputs/d1_execution/V4/W11/D1_HG06_U1_ANALYSIS.md": "52793db1b9cc3ba31ca69f9e617eacf529098f812250531fc25af174b17796b8",
  "outputs/d1_execution/V4/W11/D1_THRESHOLD_FREEZE_REGISTER.json": "8b3bd1bcec1ea34e446fb6f0cd573c71c05de7da4f14cd1be9e639812cc81819",
  "outputs/d1_execution/V4/W11/D1_HG06_U1_STATE.json": "f4c96bab5c512b1872f9ac05b828de8ac662ac83d0e9f924e75f31e013909337",
  "outputs/d1_execution/V4/W11/D1_HUMAN_REVIEW_CLEARANCE.json": "381f2998d2826b0a79bcc6a3f2187cc67d0bf8cacb189bb496c15881ae12acae",
  "outputs/d1_execution/V4/W11/D1_T2_WANG2026_PROVENANCE_REVIEW.json": "ab4125cb6a07dcd892095fbdb90b58ccb18cf06f96cf888f3c18b74b79886c1d",
  "outputs/d1_execution/V4/W11/D1_HG06_U2_REFERENCE_OUTPUT_LOCK.md": "cd4f1aa2bbe79b183f8faa8dc256d0756815a7ae19eec5680648ed207091cc2f",
  "outputs/d1_execution/V4/W01/repository_manifest.json": "714dba7fb6501d53fd4f5c0759ad28bf9247aa445960e79be47aa51de928bab8",
  "outputs/d1_execution/V4/W01/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W01/scope_lock.json": "edae90ff33b2930250987a187318f3a7aba49b62c54c12caa93c883d4a38bb39",
  "outputs/d1_execution/V4/W01/W01_EXECUTION_RECEIPT.json": "026a83bb283686dfd46a39301b8dede98bd5d1400dd154671f0dda1b0e514856",
  "outputs/d1_execution/V4/W01/plan_hash_record.json": "9dd95d8e263af472c1702b4f65f9e1e8e488d31a52aca87d85d3d6f69e745def",
  "outputs/d1_execution/V4/W05/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W05/W05_EXECUTION_RECEIPT.json": "816f43e51574813be2cb7af0e9bba26928d8f2faeec4f7fdc1fc0914ab3849c3",
  "outputs/d1_execution/V4/W05/D1_PAPER_EVIDENCE_SHARD_W05.jsonl": "74d5be6913563531b74973468e8e2d9535958c4b4097936dd208e1a73e31188d",
  "outputs/d1_execution/V4/S09/D1_K_CRITERIA_REGISTER.json": "8ba82beee1f5650e314011536f36aff51300583e28e827feaa607f52de9206a1",
  "outputs/d1_execution/V4/W06/D1_PAPER_EVIDENCE_SHARD_W06.jsonl": "37fd93ca93b2d8dcc26a4cffd04117857a5e3f1bd35eef5409e0ea73a070bdb2",
  "outputs/d1_execution/V4/W06/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W06/W06_EXECUTION_RECEIPT.json": "1f3efb17f7fd4b83398bf8baddb26874359a9e61a2dd8d6268aa7534a4b9b85d",
  "outputs/d1_execution/V4/W10/D1_UNRESOLVED_THREAT_REGISTER.json": "6bdd9de4175f319c52d93b13579e985c338eae73b35d903d63c6fa1f1f0c9c1f",
  "outputs/d1_execution/V4/W10/D1_T2_WANG2026_THREAT_RECONCILIATION.json": "4f3e27343398fc3a3f9ae54dab8a5f7bbc39dca409e02b9581a23a1f0b8946fc",
  "outputs/d1_execution/V4/W10/D1_PRIOR_ART_THREAT_MATRIX.json": "07583010236ad8c7f08879b73c77b5ac1f0ac58ad328c0c286dfbc64ccf7ecda",
  "outputs/d1_execution/V4/W10/.gitkeep": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "outputs/d1_execution/V4/W10/D1_SEARCH_DECISION_LOG.json": "73a648df81ae4b78abe4e74e56a4b2a65310dbb68c8fafcd25700617748e5fe0",
  "outputs/d1_execution/V4/W10/D1_T2_WANG2026_FULLTEXT_AUDIT.json": "4eb344d689622250782fa23c188e044877b8a2c0d1d87b1a49005c3f293538bd",
  "outputs/d1_execution/V4/W10/D1_PRIOR_ART_FAMILY_COVERAGE.json": "4c2bac14d6f1bdef07fac8274c40b056713d13ff0f2eef62ca3adffc62474bbe",
  "outputs/d1_execution/V4/W10/D1_T2_WANG2026_FULLTEXT_AUDIT.md": "3ed5f0599fa14cdf8d1c1d060014b62540cdac2a937a405a970134dea603a80f",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6",
  "outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8",
  "outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682",
  "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd",
  "outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24",
  "outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003",
  "outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1",
  "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c",
  "outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b",
  "outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e",
  "outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513",
  "outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40",
  "outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b",
  "outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da",
  "outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7",
  "outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880",
  "outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d",
  "outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca",
  "outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9",
  "outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c",
  "outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee",
  "outputs/verification/MP1-V002/README.md": "2f7fb55c524a6ac3f635bbf933dcce0e989829a30f976504468a2f7f0ab0413d",
  "outputs/verification/MP1-V002/FINAL_ADJUDICATION.md": "15c036c0eebb669727ffee45db30290101f99f0a8b90b903709ec2aa4c307ea1",
  "outputs/verification/MP1-V002/verification_matrix.md": "9bdaa566a0b6907706ed5fad5a9aadbc48afe53394f811580c1a43a5de3966cd",
  "outputs/verification/MP1-V002/FINAL_ADJUDICATION.json": "535eb2f4906804356a5573488b3d2bffa1f4527e48b3970488c9b501e5cc7ac3",
  "outputs/verification/MP1-V002/FINAL_ADJUDICATION_raw.json": "85c0c950c0351f7c1dc451f9c258ac5236fb1350a97b7af2cb5f830d131aa425",
  "outputs/verification/MP1-V002/citation_coverage.json": "c04f4d70eb560b71b907e4e3158a27a427d9e5248150d2d72738f7c8a5af6b7b",
  "outputs/verification/MP1-V002/CITATION_COVERAGE_STATUS.md": "db55e2e19aa8ec817d6d9c4d3850beed9bde38dd32ec4728bd20da5412390c10",
  "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.md": "42de9bedbed6ce74660fe200b0aaee62b92e675f1fdf99ee6369a88ef303e4b2",
  "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT_raw.json": "9aa2ca14b0a219b6183dedd3fb0ce277a18f5406560f88e7a65c740fc5dbca71",
  "outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json": "2a7062fc2ef72d7d0ad49ed102d1ac6d24e1c45fed7440bb89e57d8cc1eb8e7d",
  "outputs/verification/MP1-V002/verification_matrix.json": "85f7858ca0ac7e0a8bbc23bb97076d1c56b22b71f38bcc0f15012b1f39bb9445",
  "outputs/verification/D1-V002/adversarial_evidence_synthesis.md": "3a40860317c608e11b733485c16615b007ed30bb433dfea7465828e6eacee49a",
  "outputs/verification/D1-V002/verification_matrix.md": "ba20d25db1d99b8ae07784c55c4bef39d32f25c79e424ca696a17156d61e8026",
  "outputs/verification/D1-V002/verification_matrix.json": "2d8d0fdef3c8649631827717ab1d67cf262fa4dbd717f63e56aa7388806d3db1",
  "outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.md": "62df858b6d83f8a861d8fe792d431937e4481f930b85cf0da6465e1240fe83cd",
  "outputs/verification/D1-V006/verification_matrix.md": "66141980beea51680c86166d4370332c67c12bfeb40fd47fc16fd15df600c7e8",
  "outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT.json": "1ec49efca8eba6e59e487fef08c89b59c3990d8050b126535657edcb53ac2166",
  "outputs/verification/D1-V006/C03_ADVERSARIAL_AUDIT_raw.json": "f2d189d7f64e8c81350f7fc08200395cf22fe28ef1a1c13a9c319993a5dcb1e4",
  "outputs/verification/D1-V006/verification_matrix.json": "97816a1f23cc73ec22dcf005387e6f79c337778a83c3086f959a9b553a4542df",
  "outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT.md": "7cb693f83227b26a4efe96d678b92e2ae21eed7bd16d20e3475d42152bb33ebb",
  "outputs/verification/D1-V007/C04_SEMANTIC_CORRECTION.md": "0c3a8ddc186edd1884ce9329f5a2053a55198087d2df269234d83503149bc0ac",
  "outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT_raw.json": "c6ea654a59dfafa6c32eca9454d5954d3554cc01050297ee92b7e4b1895f2e6a",
  "outputs/verification/D1-V007/verification_matrix.md": "1905b38a81039426f5de1bd67e328963654809bf29e615dd4f1c12c875581e07",
  "outputs/verification/D1-V007/C04_ADVERSARIAL_AUDIT.json": "6c5e5cabbde641cc827bb7561248d41f1e01b256290c78105225ff2e07d79ec1",
  "outputs/verification/D1-V007/verification_matrix.json": "9365810ca0c310855a92d087c219c6e3e98639770b7df3162d11ba8f17bd3666",
  "outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT.json": "8f443316487072f5a1233089c72cca5b86bfa302bce49571ac82539cfe7c367a",
  "outputs/verification/D1-V005/verification_matrix.md": "fa339ec8e30d36fc732e22bc78115788d21d0b1e4ce74841b49622664c1cef9e",
  "outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT.md": "1f6805181ab9850f2dd613d940d6305dbbffd46495208291ab1c0a3180fa1df2",
  "outputs/verification/D1-V005/C02_ADVERSARIAL_AUDIT_raw.json": "0215e6b9331a156a8ae1c513d5ac2a3685bb326a656179f38220b0f14c283710",
  "outputs/verification/D1-V005/verification_matrix.json": "6e60ab14d04a49b9c73876327ba5c1b97ebd0b557e8a0eef441a0c72db300ba8",
  "outputs/verification/MP1-V001/README.md": "9697786fb8d9f165161f542d3ba1eeea6942965b51811fe30798fe58ee935482",
  "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md": "e2df3784a88bc23f5bf543ef6eaeefcf59a5c8c1e794f03590eed33e955dfd77",
  "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json": "0f7d8dfc4aae78139a483a9132b54e2eb1ada0a69304f96c3f1b0e2c197a7e81",
  "outputs/verification/MP1-V001/verification_matrix.md": "04a84528187ec22a0427a0ed1a6e8b3d10c335f8ebac02dd5536742a5c89d4fc",
  "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT_raw.json": "e43e2654d8b3fd3813936bb9f87b28d884129269effabf9fcef9ace14dce0e47",
  "outputs/verification/MP1-V001/verification_matrix.json": "84c3499d5318fd952466f5ec27d9c09fa5e03a001f9170e943d3e2fe9d4839d0",
  "outputs/verification/D1-V001/direction_verification.md": "44849a8f501a62cab7d5461241581b812626d11ac57d8666c0c39cb1da924aff",
  "outputs/verification/D1-V001/verification_matrix.md": "936119535a92ea94e7be0e1055d876c97dd3799c754f252be90835e709a9a423",
  "outputs/verification/D1-V001/verification_prompt.txt": "97b3895e666ccd87d0f144723bb0e62e564abb04b34b6e128c49a4c658a7ae80",
  "outputs/verification/D1-V001/direction_verification_raw.json": "a3f5ba23c856b79dd686ed7b580c2f99882c61ab955de1984cd4b8c4898a581e",
  "outputs/verification/D1-V001/verification_matrix.json": "9e9d9471ac9488aea6e668be4b29c92d7d8a3291c80531f8abcf13500a0817bd",
  "outputs/verification/D1-V001/direction_verification.json": "1a39bfdecd7a6bc7001a258f81756aededc1e15b5ee68cedc8af5cea046ec731",
  "outputs/verification/D1-V009/README.md": "e80727b6695a89000b0047175f5f07808b668d4d8dc7f5eeffd2a475177aabd7",
  "outputs/verification/D1-V009/verification_matrix.md": "245e95ce438a9dab058aa2deb0793d74580510ea629be6f21356cd33290dc32e",
  "outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT_raw.json": "c3afcfe07c7f41073a17982512cc4effc0cfa2037e8a9f64ccacc6002cf90a8c",
  "outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md": "2c46f66fac2cbe002c7288d848633b64da8220019d5517297bd6001a93351256",
  "outputs/verification/D1-V009/verification_matrix.json": "c3fcde1131039130bbaeca8a0884b814023fea6a3c6a7883ac1ec5b8a7aa44d1",
  "outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json": "6cb12372d216ed471bdaba91aaa2568061046e660696b00fec91e78dc059b474",
  "outputs/verification/D1-V003/cross_round_adversarial_synthesis.json": "43f5b700b7b84b5986cf3ed33914f27063ae7ea3f983fc683d3a415607a54017",
  "outputs/verification/D1-V003/D1-V003_SEARCH_LOG.md": "d2b7134e8028265b270db95a043612fe34a7d4f8946b4479f1a1ad734cfecd6d",
  "outputs/verification/D1-V003/semantic_scholar_results.json": "701a4dd98da4c6166e5491b39e9d209692e09d3a7ce7c6190c1089cb4166c814",
  "outputs/verification/D1-V003/D1-V003_EVIDENCE_MATRIX.md": "3c170e4e189c84f70ee0ed2f847edb1e1884413cee28d57e93a164c004f4af79",
  "outputs/verification/D1-V003/verification_matrix.md": "21a99d8436f439316b3f70ee829fb3f04212b084f9f4acf00136a2478184e0ea",
  "outputs/verification/D1-V003/D1-V003_LITERATURE_AUDIT.md": "0161d22efb42c4109ab35ef6efe41ed81c0eaeef7028298191957867efe89318",
  "outputs/verification/D1-V003/ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md": "4b45b781437cc7c21c843b28161305505c372e1f9a88a1b5df3d04c8d4a2752a",
  "outputs/verification/D1-V003/cross_round_adversarial_synthesis_raw.json": "00dd14cddeeeb02cb3b8de9fe71bf0e6a1401d1b90cb08da92183743340e4233",
  "outputs/verification/D1-V003/FAN_2026_MODEL_AUDIT.md": "a9b1ab01681064462f1cf2787e4d480061bf3f7adc8bc1f6b520c662b3da921f",
  "outputs/verification/D1-V003/verification_matrix.json": "759b9683bc97eb240abfb39557a1ff439a5fc82cc966393c6c9ff8fcccad44a6",
  "outputs/verification/D1-V003/cross_round_adversarial_synthesis.md": "e3e13dd5d8f53a5d22007e148396f6a580c7fb974aee4b85a90744e1ff4636ef",
  "outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT.md": "8a65916af364637eb1d427a74a88c9526713609289a8bbad95a3fc7a39b6f6e9",
  "outputs/verification/D1-V004/verification_matrix.md": "1742d5139b06686ca9f3aa3e5cb68a4470456f7abdbbf9c399e57fce5f0da895",
  "outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT.json": "f1e56ea84df8add3d5b280ad6d223cf9d0a6732cc4e59d76cd01c148cc1940ec",
  "outputs/verification/D1-V004/C01_ADVERSARIAL_AUDIT_raw.json": "ce7e51f584c72d91a59a33129c5e2d9c45cf59464003906180250c7450d498a0",
  "outputs/verification/D1-V004/verification_matrix.json": "288be9887ba174d7a8687a73e134f08ecd6ce9217b94620807da08ceb26167ed",
  "outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json": "b888cfe083888aa0b2859ee97046f60e2c4d505cc4882f258fd29e305f28cd3a",
  "outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT_raw.json": "d80701a81e43d01052641e2efa3609fc866b727cb2c4f3eccfee9bfa608f21ab",
  "outputs/verification/D1-V008/verification_matrix.md": "fd5265da272d647a1addb2b68aa607f08c4bb2102ea4e2b32b2490a4907c4b3b",
  "outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md": "b4fb4021c5dc48ef1d75ae9d5eaa913d658a5a612c269268b33a60366b691a51",
  "outputs/verification/D1-V008/verification_matrix.json": "2ea246ae302c6cf0b91575f1b4db177d189e608991136d3b05cbf45d26d5b178",
  "outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.json": "fa68da135d655e2992cba00a0f5d04addffd1c055adcfdcbb46b8e870036696b",
  "outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.csv": "206501aa0485177b9df2860a306719bc75425caf68944b09ea286c40aec7f4db",
  "outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv": "3bbd5519a54ea9aee4654a47961d5f7ff0ae6b74edaa5546b2f8826ed943f5f5",
  "outputs/verification/MP1-V002/citation_screening_13paper_chase/METADATA_SCREENING.json": "f8c29110ccc714795a6d24137cc59bf1c288ac5899817b69a397c0a876136afa",
  "outputs/verification/MP1-V002/citation_screening_13paper_chase/METADATA_SCREENING.csv": "d5255874bbd9889d25eef9d03e4c6a07231f3b31cef0a34a2f81b95cd9577dfc",
  "outputs/verification/MP1-V002/citation_screening_13paper_chase/FULL_TEXT_SHORTLIST.csv": "685b5bb8c5583ab9f305d3ec816488c9545f12d707a5caaf1d0c9ff57961c5aa",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090308Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090308Z/source_manifest.json": "08179aaa559d5e8ebf5416cd8252480bace18aaf34d2661c46ee30b29daaad9a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090308Z/prompt.txt": "68fa0c4dc019dfa24430705801c35429c40fd2183863e6bcad5939129d424a4a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114158Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114158Z/source_manifest.json": "925cdf395cc2721667b51125a921eb9f3a6d7f0b086abd686ee7466c7a19659b",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114158Z/prompt.txt": "ef36f26e00c8df1e648dd528ac8850deba9ddfa454b6590aecc6de08f977ea78",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114158Z/raw_model_output.json": "8220c745b9b6f7ec5cf573da8fed0b96afa0e97269c65ecb4860490eed585234",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114158Z/TARGETED_THREAT_AUDIT.md": "dd6b8637c4f3de329564eee4838e205f5c132aca5b08d62cefc143e44d081008",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114158Z/TARGETED_THREAT_AUDIT.json": "a224914fb560eafd17ada2e7cfdef7d7ab29229277c9ce51c9c16a38a537d758",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114150Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114150Z/source_manifest.json": "11a9a6b40d959983f77e603770459637e41704a082a4c48fa1fb9b694ee51de2",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T114150Z/prompt.txt": "ef36f26e00c8df1e648dd528ac8850deba9ddfa454b6590aecc6de08f977ea78",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063712Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063712Z/source_manifest.json": "fab6350e5114d77831f430bfd509452ece0d08ec3f729691b01ee444f4e5d212",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063712Z/prompt.txt": "0e897364ef20a2df31b078e9a215c34e62f03560ff02c4f997426e656767156a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171206Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171206Z/source_manifest.json": "34c7cb988f2c645ef022b0c730c0619850ae031dc7ac619cf782311c6499d329",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171206Z/prompt.txt": "fe82310cc838332f90679904c425039d62aaedc2ca02a346f5cbd01532538d3c",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T064146Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T064146Z/source_manifest.json": "064efd1615d07629f7d4eb285bd757c0473869629a84ed6b3680822a74a1d94f",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T064146Z/prompt.txt": "0e897364ef20a2df31b078e9a215c34e62f03560ff02c4f997426e656767156a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T064146Z/raw_model_output.json": "86ab5e407e1d1feb12e4324c16b2991c311b47c2dcbdd764dabd4c95bd31c4a3",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T064146Z/TARGETED_THREAT_AUDIT.md": "fd51f62e832ebfc8a0101a2444024538486163c909268a9547321da116b60f52",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T064146Z/TARGETED_THREAT_AUDIT.json": "91a5d150c346345533573ed67197bf96ff3fcddd1606114dcf9e05551d6a6602",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063658Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063658Z/source_manifest.json": "d2e6513a716b5add1022b5057bc342fd7892fb2fb0904391fcd4de441ef4bf41",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063658Z/prompt.txt": "0e897364ef20a2df31b078e9a215c34e62f03560ff02c4f997426e656767156a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063737Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063737Z/source_manifest.json": "163172d8b6e62d1c6522f2172d4f08b7afa62171b76ebd3d44ecd1c80a603a92",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T063737Z/prompt.txt": "0e897364ef20a2df31b078e9a215c34e62f03560ff02c4f997426e656767156a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090319Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090319Z/source_manifest.json": "9cb2c7306a60b76d0640926a952cc28e182baa96f93ceca75c72f3a47307914e",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090319Z/prompt.txt": "68fa0c4dc019dfa24430705801c35429c40fd2183863e6bcad5939129d424a4a",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090319Z/raw_model_output.json": "9aa2ca14b0a219b6183dedd3fb0ce277a18f5406560f88e7a65c740fc5dbca71",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090319Z/TARGETED_THREAT_AUDIT.md": "42de9bedbed6ce74660fe200b0aaee62b92e675f1fdf99ee6369a88ef303e4b2",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260925T090319Z/TARGETED_THREAT_AUDIT.json": "2a7062fc2ef72d7d0ad49ed102d1ac6d24e1c45fed7440bb89e57d8cc1eb8e7d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171216Z/output_schema.json": "febdbc5ba269193242fe647c5603d6deaefd5dad2a4dbdbc344e2d5fdce35d3d",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171216Z/source_manifest.json": "9b316bdfc231c2f6eb3b1cf398da51d48da91230b8509a052e53a66ae8633fa7",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171216Z/prompt.txt": "fe82310cc838332f90679904c425039d62aaedc2ca02a346f5cbd01532538d3c",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171216Z/raw_model_output.json": "776b4cad359ed73cb98c55761f6a0f6400f4ecb8acb8ca5bce7460ad1d93e6a6",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171216Z/TARGETED_THREAT_AUDIT.md": "0c849bb884ac6947a984e5c2f7a0d89e00600a6d065fdfb250a58146a690bb18",
  "outputs/verification/MP1-V002/targeted_threat_runs/20260924T171216Z/TARGETED_THREAT_AUDIT.json": "74ccb9fd219c1691fbfad70a2943e54efe1448d6eb6cb8ea0bba7b888d1006c1",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093041Z/output_schema.json": "b4989b347342b63e880ef05a8385d2339572d65573e4f2a9d4d760b26e8551f1",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093041Z/source_manifest.json": "8a87fd9b55188cb237f6e276492bc1ee5f8db92aa2c587afba6bda31a7fd6300",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093041Z/prompt.txt": "eeed7744d8bf4ebc7f0193e3297a200ab5eba8fc0efb37b12f556a8a24fc0c07",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093414Z/output_schema.json": "b4989b347342b63e880ef05a8385d2339572d65573e4f2a9d4d760b26e8551f1",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093414Z/source_manifest.json": "92e5f2ad3a6722c9f959cf7f0f3364589f60a813d24cc33bccce33e49088b6f6",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093414Z/FINAL_ADJUDICATION.md": "15c036c0eebb669727ffee45db30290101f99f0a8b90b903709ec2aa4c307ea1",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093414Z/FINAL_ADJUDICATION.json": "535eb2f4906804356a5573488b3d2bffa1f4527e48b3970488c9b501e5cc7ac3",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093414Z/prompt.txt": "eeed7744d8bf4ebc7f0193e3297a200ab5eba8fc0efb37b12f556a8a24fc0c07",
  "outputs/verification/MP1-V002/final_adjudication_runs/20260925T093414Z/raw_model_output.json": "85c0c950c0351f7c1dc451f9c258ac5236fb1350a97b7af2cb5f830d131aa425",
  "outputs/verification/D1-V002/_snapshot/adversarial_evidence_synthesis.md": "3a40860317c608e11b733485c16615b007ed30bb433dfea7465828e6eacee49a",
  "outputs/verification/D1-V002/_snapshot/verification_matrix.md": "ba20d25db1d99b8ae07784c55c4bef39d32f25c79e424ca696a17156d61e8026",
  "outputs/verification/D1-V002/_snapshot/verification_matrix.json": "2d8d0fdef3c8649631827717ab1d67cf262fa4dbd717f63e56aa7388806d3db1",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T044004Z/output_schema.json": "563ba0e0e989074680bb596173f96fe4de6aaf2d463bc1ce37e278518874f09e",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T044004Z/source_manifest.json": "68c16b43fa9cbda864a2d72e085084fadaf4b1479189af5ddf1544ed3fc7aee6",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T044004Z/prompt.txt": "e17662ec370fe088464b8f6e4dc7eb657c43bd328457269e4b44b0577e422454",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050234Z/output_schema.json": "563ba0e0e989074680bb596173f96fe4de6aaf2d463bc1ce37e278518874f09e",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050234Z/source_manifest.json": "1db0842a42f71319237a0e45e6da41ebe345af005777175a400598a3da9ecbdc",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050234Z/prompt.txt": "0e496c02c1b52aa912784628d843613b87ac9b23c352a88dbc9475f9e27a79d1",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T044149Z/output_schema.json": "563ba0e0e989074680bb596173f96fe4de6aaf2d463bc1ce37e278518874f09e",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T044149Z/source_manifest.json": "c4f3bd97d4fd8bc47cc9ab2c797d0ad175d5533c7725902086d6d2b91bd54618",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T044149Z/prompt.txt": "e17662ec370fe088464b8f6e4dc7eb657c43bd328457269e4b44b0577e422454",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050247Z/C03_ADVERSARIAL_AUDIT.md": "62df858b6d83f8a861d8fe792d431937e4481f930b85cf0da6465e1240fe83cd",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050247Z/output_schema.json": "563ba0e0e989074680bb596173f96fe4de6aaf2d463bc1ce37e278518874f09e",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050247Z/source_manifest.json": "4608086f7180ef8f61161898a17005ca5d5056362b04d2e493e7751f87da52fa",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050247Z/C03_ADVERSARIAL_AUDIT.json": "1ec49efca8eba6e59e487fef08c89b59c3990d8050b126535657edcb53ac2166",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050247Z/prompt.txt": "0e496c02c1b52aa912784628d843613b87ac9b23c352a88dbc9475f9e27a79d1",
  "outputs/verification/D1-V006/c03_adversarial_runs/20260918T050247Z/raw_model_output.json": "f2d189d7f64e8c81350f7fc08200395cf22fe28ef1a1c13a9c319993a5dcb1e4",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T062523Z/C04_ADVERSARIAL_AUDIT.md": "9f155c29ba20e95e36cbc5dcd9f94ed82fc7a7f8830c62045cfb9393ed705c7a",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T062523Z/output_schema.json": "0a15bba4824d6d515ddbe3155438fcb56bb731e74e04d6fa4141451fc6a67b63",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T062523Z/source_manifest.json": "ed1109e5159a6461ff935d5a769f522c52de70d764e3650572838b99d43e38e3",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T062523Z/C04_ADVERSARIAL_AUDIT.json": "b039c710ea9e76d0f5a4fa8e125b14c339b707e4dccf7e58892fcc891c7c541d",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T062523Z/prompt.txt": "7d4c8da4a2d591bcd147c7d413d80edf1f0c87260b297630cf9d5bed6c50f8cd",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T062523Z/raw_model_output.json": "cccd4f8a534e7ce0bbdad51a8637f57a5b7bd01bed3ed92844b7da4954ce1507",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T081007Z/C04_ADVERSARIAL_AUDIT.md": "7cb693f83227b26a4efe96d678b92e2ae21eed7bd16d20e3475d42152bb33ebb",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T081007Z/output_schema.json": "0a15bba4824d6d515ddbe3155438fcb56bb731e74e04d6fa4141451fc6a67b63",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T081007Z/source_manifest.json": "7d1f007e20218e6dc894ea65ce547430d2090964bdeebb6f3efe8b929d4a22a3",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T081007Z/C04_ADVERSARIAL_AUDIT.json": "6c5e5cabbde641cc827bb7561248d41f1e01b256290c78105225ff2e07d79ec1",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T081007Z/prompt.txt": "dec70f84171cab8729babffb3e894633fb3c798e3d8210770794f9f7e3e503c0",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T081007Z/raw_model_output.json": "c6ea654a59dfafa6c32eca9454d5954d3554cc01050297ee92b7e4b1895f2e6a",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T080701Z/output_schema.json": "0a15bba4824d6d515ddbe3155438fcb56bb731e74e04d6fa4141451fc6a67b63",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T080701Z/source_manifest.json": "aaba73d75b6672e93388378d4ba4b5a48dff1ba4ff7171f072e1dfcc37a72adf",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T080701Z/prompt.txt": "dec70f84171cab8729babffb3e894633fb3c798e3d8210770794f9f7e3e503c0",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T061959Z/output_schema.json": "0a15bba4824d6d515ddbe3155438fcb56bb731e74e04d6fa4141451fc6a67b63",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T061959Z/source_manifest.json": "7f36c60fdcfe1d233edffdd1c09ede3475da3698e99434bc4b3f00d24d66e5e7",
  "outputs/verification/D1-V007/c04_adversarial_runs/20260918T061959Z/prompt.txt": "7d4c8da4a2d591bcd147c7d413d80edf1f0c87260b297630cf9d5bed6c50f8cd",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200835Z/C02_ADVERSARIAL_AUDIT.json": "8f443316487072f5a1233089c72cca5b86bfa302bce49571ac82539cfe7c367a",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200835Z/output_schema.json": "2044f310450f00ff646daa4cf60253e629ab9f544d83b16b37437f14f688deca",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200835Z/source_manifest.json": "77f8761416dc19f1e7955da05bd94dad63c6d542b371ffd8de8b7874ca857ecb",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200835Z/C02_ADVERSARIAL_AUDIT.md": "1f6805181ab9850f2dd613d940d6305dbbffd46495208291ab1c0a3180fa1df2",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200835Z/prompt.txt": "332f32dd0148130d52f750bf1da24f24c1abb6facf3124e46543397aebe0a724",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200835Z/raw_model_output.json": "0215e6b9331a156a8ae1c513d5ac2a3685bb326a656179f38220b0f14c283710",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200538Z/output_schema.json": "2044f310450f00ff646daa4cf60253e629ab9f544d83b16b37437f14f688deca",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200538Z/source_manifest.json": "939b0d8f8eb4589bbe072b3b7bcbaf1ffe18ff97502678a3568021271559dda9",
  "outputs/verification/D1-V005/c02_adversarial_runs/20260917T200538Z/prompt.txt": "332f32dd0148130d52f750bf1da24f24c1abb6facf3124e46543397aebe0a724",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055150Z/output_schema.json": "fa69b0cd6c303a9a8456833f11c41c68df4da5cf86caec6464eb3c941c4a76f1",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055150Z/source_manifest.json": "09aafc81cb93df50f67fa53cb98291ca82e0e9beaa436ed088552e2c73fb23db",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055150Z/CORE_PRIOR_ART_AUDIT.md": "e2df3784a88bc23f5bf543ef6eaeefcf59a5c8c1e794f03590eed33e955dfd77",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055150Z/CORE_PRIOR_ART_AUDIT.json": "0f7d8dfc4aae78139a483a9132b54e2eb1ada0a69304f96c3f1b0e2c197a7e81",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055150Z/prompt.txt": "6f19f518151d058fcbd7260f0c830f26029d866722d7de7c94a77f225eaeeff0",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055150Z/raw_model_output.json": "e43e2654d8b3fd3813936bb9f87b28d884129269effabf9fcef9ace14dce0e47",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055140Z/output_schema.json": "fa69b0cd6c303a9a8456833f11c41c68df4da5cf86caec6464eb3c941c4a76f1",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055140Z/source_manifest.json": "fdd9e4614d1e0d82522ffd88c49865e202cb66d935339bb176f9cb1b072478e9",
  "outputs/verification/MP1-V001/core_prior_art_runs/20260922T055140Z/prompt.txt": "6f19f518151d058fcbd7260f0c830f26029d866722d7de7c94a77f225eaeeff0",
  "outputs/verification/D1-V009/late_found_runs/20260920T045915Z/output_schema.json": "942a0155a7c6a75f8d85d6c7d271e795aa1c11929a7a20a97885ca9642cbafda",
  "outputs/verification/D1-V009/late_found_runs/20260920T045915Z/source_manifest.json": "8a172b5ea01d2efe1403118f79c664f3e3bb03dc09d3ed0d7246c007ffc6bcef",
  "outputs/verification/D1-V009/late_found_runs/20260920T045915Z/prompt.txt": "ae6517f3501a10da58a2e3d562696f83d5c3c3f83d21db85a4a908d0b9225362",
  "outputs/verification/D1-V009/late_found_runs/20260920T045915Z/raw_model_output.json": "c3afcfe07c7f41073a17982512cc4effc0cfa2037e8a9f64ccacc6002cf90a8c",
  "outputs/verification/D1-V009/late_found_runs/20260920T045915Z/LATE_FOUND_ADJACENT_AUDIT.md": "2c46f66fac2cbe002c7288d848633b64da8220019d5517297bd6001a93351256",
  "outputs/verification/D1-V009/late_found_runs/20260920T045915Z/LATE_FOUND_ADJACENT_AUDIT.json": "6cb12372d216ed471bdaba91aaa2568061046e660696b00fec91e78dc059b474",
  "outputs/verification/D1-V009/late_found_runs/20260920T045905Z/output_schema.json": "942a0155a7c6a75f8d85d6c7d271e795aa1c11929a7a20a97885ca9642cbafda",
  "outputs/verification/D1-V009/late_found_runs/20260920T045905Z/source_manifest.json": "f3af11905a0ec644b77b8c5eca21b45ca2297b2654daee0ec8813b87f0b42f8a",
  "outputs/verification/D1-V009/late_found_runs/20260920T045905Z/prompt.txt": "ae6517f3501a10da58a2e3d562696f83d5c3c3f83d21db85a4a908d0b9225362",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152345Z/cross_round_adversarial_synthesis.json": "43f5b700b7b84b5986cf3ed33914f27063ae7ea3f983fc683d3a415607a54017",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152345Z/output_schema.json": "bce6e3b03dea9f397601e9621dac0f752e1fb5e856b309bb9a46c3dc703f72f4",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152345Z/source_manifest.json": "5a75f70b435824a3cfaef370878b8b8e4591e3cfd75ada186388063d557081c6",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152345Z/prompt.txt": "55269cb1658508ae894611bb14a2ace127e87105a96aa3baa7534c9a528712da",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152345Z/raw_model_output.json": "00dd14cddeeeb02cb3b8de9fe71bf0e6a1401d1b90cb08da92183743340e4233",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152345Z/cross_round_adversarial_synthesis.md": "e3e13dd5d8f53a5d22007e148396f6a580c7fb974aee4b85a90744e1ff4636ef",
  "outputs/verification/D1-V003/cross_round_runs/20260917T150834Z/output_schema.json": "bce6e3b03dea9f397601e9621dac0f752e1fb5e856b309bb9a46c3dc703f72f4",
  "outputs/verification/D1-V003/cross_round_runs/20260917T150834Z/source_manifest.json": "218b9f3fc8ea0640e8be69ad096b668d4812b2a96850fecd8118b7e6d77ca91c",
  "outputs/verification/D1-V003/cross_round_runs/20260917T150834Z/prompt.txt": "55269cb1658508ae894611bb14a2ace127e87105a96aa3baa7534c9a528712da",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152229Z/output_schema.json": "bce6e3b03dea9f397601e9621dac0f752e1fb5e856b309bb9a46c3dc703f72f4",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152229Z/source_manifest.json": "b5840b9b1203fa37d7d178bddd2497933a693d7badeccd11dee555db75343827",
  "outputs/verification/D1-V003/cross_round_runs/20260917T152229Z/prompt.txt": "55269cb1658508ae894611bb14a2ace127e87105a96aa3baa7534c9a528712da",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183827Z/output_schema.json": "b8ab655caa3de9b194999be209ff5c8aa0c28d5ff8e93ddf3c93fe2397227230",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183827Z/source_manifest.json": "f97d3e1be025b2b34880d2db8efe3a2d4e1e75b47d7e96c2802858de0425732c",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183827Z/C01_ADVERSARIAL_AUDIT.md": "8a65916af364637eb1d427a74a88c9526713609289a8bbad95a3fc7a39b6f6e9",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183827Z/C01_ADVERSARIAL_AUDIT.json": "f1e56ea84df8add3d5b280ad6d223cf9d0a6732cc4e59d76cd01c148cc1940ec",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183827Z/prompt.txt": "d6c8212621abae5809fb6f06ff833f5810b377d5dd2e63f29e25ce4e48ddc7ad",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183827Z/raw_model_output.json": "ce7e51f584c72d91a59a33129c5e2d9c45cf59464003906180250c7450d498a0",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183650Z/output_schema.json": "b8ab655caa3de9b194999be209ff5c8aa0c28d5ff8e93ddf3c93fe2397227230",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183650Z/source_manifest.json": "d96d736b807d7ba5db6ed48f409da01fc3935a42873fd02bc3eb910bd955c6d4",
  "outputs/verification/D1-V004/c01_adversarial_runs/20260917T183650Z/prompt.txt": "d6c8212621abae5809fb6f06ff833f5810b377d5dd2e63f29e25ce4e48ddc7ad",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T083907Z/output_schema.json": "c78aa6e2c43547644e8c2832bbbc885ed69e50f84183ac7a3dc9fc0767ca3476",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T083907Z/source_manifest.json": "b124796802d781b532c93346ba83707688c48cc14ffd2fcd50cad326b84f02d1",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T083907Z/prompt.txt": "ae2ac99aa0dc68c912d707262149c64414fdeade26d9a0371d41cebe3d8dfb44",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T084134Z/output_schema.json": "c78aa6e2c43547644e8c2832bbbc885ed69e50f84183ac7a3dc9fc0767ca3476",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T084134Z/source_manifest.json": "409493694e69d1848100558776b34ea6ec4f7367c1d5af4dfefd58829f3bf339",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T084134Z/FINAL_NAMED_TARGET_AUDIT.json": "b888cfe083888aa0b2859ee97046f60e2c4d505cc4882f258fd29e305f28cd3a",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T084134Z/prompt.txt": "ae2ac99aa0dc68c912d707262149c64414fdeade26d9a0371d41cebe3d8dfb44",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T084134Z/raw_model_output.json": "d80701a81e43d01052641e2efa3609fc866b727cb2c4f3eccfee9bfa608f21ab",
  "outputs/verification/D1-V008/final_named_target_runs/20260918T084134Z/FINAL_NAMED_TARGET_AUDIT.md": "b4fb4021c5dc48ef1d75ae9d5eaa913d658a5a612c269268b33a60366b691a51",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py": "d7e2b3eb9c9cb70dcf9ec6bcd4291edd683bce4220b172177a3ec0271543aed4",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt": "29ee1cd95525b8e187408d9588156039a1b3f635e9a608dd3c43a9a9167ef147",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt": "7f694619b4377fc61b1a00fe3435945651983296b8c5e83f47f971734f70bc2f",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt": "3f86f47c7a279935989a13297c5f17eaa4a5b5c819ca1935ca96513265d6b895",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt": "356de27f1e83ccb27a37f1ffd9be9321ca7887db1288d45c1adc1a5cf83ca1e9",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py": "cd0bd1d5437f2e3f2f43a13d0e55abb9c3fe583bb4637256fa62314431603320",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py": "d12846bf434cae00cdd88aa4907ab1b498b419cb600ca1500d11b470bb7fb416",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt": "4c6b07960eec03bee4baf0582065e2cd5c3cdcaed357ee7a66c42d71e79b09a5",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt": "b6e8d5f5195364f3c9fbbedfde63460bc3beac3706bd9929e5aec1d06b3bef55",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt": "7a5b5bed75fe60dc1eb36eec69f5e19c4ab5a3a9e7a1fb69b107f6e4aa61a71a",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt": "0938ee9bef68cc3f7f8231129e6e383871065c16595b8d46f12331326e6b1942",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt": "f83f01d5c89461a62c290e1238bdba1d0be5d566a4d10162849a72cee905c610",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt": "9045945be238ffc81d121d178485e1fcb5bf478e0b8f6b8492c0e9dc6a7a4936",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt": "f47ba51263ffb69505356db6455a781730d7d01ab48bfdb214e793b1d434b6cb",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt": "02f77f8e301d4045d31e7fcd579badd261c34ef8148a96519b3bb88d36f74f41",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt": "982911acc87b715ead5ddcafa25f73f50937f92276417358c99ae1bbb9f4b11f",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt": "a1fafc05606f28715e59d86fc646c5151f28501dda722056b60ffbfb289b4b63",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt": "e661bd66ac3bc591d25d133ce7b5185f9290fafa2121a4ccff4c22be44ff9057",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt": "6640478481b84b7c5aa93656f82e646bf333ead8ba6afa5c612a14e93397dbb0",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json": "fc09e94857f1dae49ba360d749a72483513a380ea08427ed4b87620c7830a750",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py": "0106dbcd0cc378824724a1b5acec9e287387372aebc7a2566ca6cd13fca648a3",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt": "d614f809da314316213905d05e8242736841de9f01cecaf04ec9b6fe61291c2d",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json": "45bfdd81445f9ad3c95f1fc50bb4bc9140b25d0b422ac91f23e6565074a834c3",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt": "5e36642dbc07e11c2c93dfa8c50e0c33efdf80d677fa8dc98ab1f1e8d0014d8c",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip": "6f40ffb40b5fbc3aaa381d20f28c12b87f39111faf877e046aff27326eb97de1",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png": "35ed651167faff4e3aa4efd2a8fc56c8adc91e2ca81eb17a05cd27a23b2979be",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png": "db5a71d9a613da2e51976c5a80f7a6b9e94237506c5b2bd4b07971d69947145c",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png": "e6d0f7e7de7fb3922397919cb5949365433f63fe78b5bbdd92c0d689d037eead",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png": "0ce4fa6d45c23b437747406f90f8f62ddb640ef4cb44c0faa02cbaba1ac4d175",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png": "9e9634334a7019114182b8ff182ae197d38ec13498d3b5d936dec9b5fd3b61ec",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png": "8080514df725ffb4dee57fe6caad48ae52a6cb5c108d2cdfed3d48317cbd740c",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/03_S03_HIGHLIGHTED.pdf": "050cfd250a9a69ae8d9ee05d6256c09cfaeff86d823813329ba42183d1745899",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/12_S05a_HIGHLIGHTED.pdf": "a4e33627271ec920f8087c8859d060eda2da44266a42e20d2a13bdee13f3fbeb",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/17_S12_HIGHLIGHTED.pdf": "06eca6451e9f7216f792f25c967488d03e0f0208d894cd2318cd6f735c2b914c",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/15_S07_HIGHLIGHTED.pdf": "320e60ed721e5c3958c8fcc7aad6b5a5a597f85af208eb1faa8b251899a76d43",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/01_S01_HIGHLIGHTED.pdf": "7a1ec6cea0c208afb8b20f4c133d7ba82bd45ca61818b7980d6f58ee73c68614",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/07_V-W02_HIGHLIGHTED.pdf": "c4d4c8f0ddcf0153ed76bab8734bdda8c2c999130bded6a1ce6dfe278da66b04",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/16_S11_HIGHLIGHTED.pdf": "f3a57e04af12bc5857ef7ded15d738e5a3b37ad644c4d470124bd36e87e137ff",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/10_S04_HIGHLIGHTED.pdf": "5fc7489435d30929e13618fd6a50e7900fdfa1d4f17ae2b33aded499530dd41e",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/09_S17_HIGHLIGHTED.pdf": "565aef36b778d40002a34bbb2d4e37d37550b7d9989c799d86fa74384cd2179a",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/08_S13_HIGHLIGHTED.pdf": "12f2c804973dce36be604a88f2f58c016550c6c05161db26a9b72eb79ffcd667",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/13_S05b_HIGHLIGHTED.pdf": "693371640d2e44adb1396189475040703e0c6ddf0944966b30db57fd86fec42e",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/06_S06_HIGHLIGHTED.pdf": "51842107d265f973957f9631315c838aa0f8f3edcae8e2e8366e41fdf40360bd",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/18_S10_HIGHLIGHTED.pdf": "794f85ea599086819ddfc18185cb868d608d73630d56d0d6716dae0c51c4ed6e",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/05_S18_HIGHLIGHTED.pdf": "da6a4d0f3b10bce4376425275d64c48f3d62c4fcc395bf4bec9674d65c860d76",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/04_S15_HIGHLIGHTED.pdf": "628736655bfbf7871679019026828548325bd9a90fc4d824963f86f130cfc8ce",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/14_S09_HIGHLIGHTED.pdf": "c31858dae95b4e9601988f2d9ba25d69b95b4b388e0932e611d5fe3df71b19fb",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/02_S02_HIGHLIGHTED.pdf": "bba1aa6651c62d2f1060e73850de3ab0ea2d42f229f96eaab487c3f1f9e63ee2",
  "outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf/11_S22_HIGHLIGHTED.pdf": "db56da5f359375d2cc930979e529ab206849abb69de4c17b83da5b8376bcd32b",
  "outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md": "72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128",
  "outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv": "f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc",
  "outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md": "d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19",
  "outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx": "35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5",
  "outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv": "ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7",
  "outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx": "38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d",
  "outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md": "bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db",
  "outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv": "7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630",
  "outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv": "735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223",
  "outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md": "7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_CITATION_RENUMBERING_MAP.csv": "d04856f4e81d291a5188d2e1182fb92d1ef396b8dd85113a66ea2e3693c823e7",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_EXECUTION_REPORT.md": "fa80bfc44be924c594bcda9514f290e74f558dd7b49dfe1a9ffcd190a05bb095",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATED.docx": "701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATION_CHANGELOG.md": "df3bca80e0b37fa66beeb63c3a059be3149b117405d5862dff846c0134022351",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_TERMINOLOGY.csv": "f529dfcb8ebf58db07112c4b17154760a08714a6bac165fc0503b4e06c736693",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_SOURCE_TRACEABILITY.csv": "a72802cc636d3c7705113cf24eec47282ebd35051f6ca9216a4d61c67510735e",
  "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_7_GATE_REVIEW.md": "cd9b63c933e07b4bbc1dd02dd5f469af449e49a5515fa226d2b5861ebfd8a4b2",
  "outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv": "5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b",
  "outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx": "8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da",
  "outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv": "c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169",
  "outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md": "d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52",
  "outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md": "c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d",
  "outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md": "91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7",
  "outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv": "08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649",
  "outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv": "f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f",
  "outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md": "402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb",
  "outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx": "6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0",
  "outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx": "024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1",
  "outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md": "256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0",
  "outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv": "8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec",
  "outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv": "baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b",
  "outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md": "ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2",
  "outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md": "675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff",
  "outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx": "0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376",
  "outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv": "49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550",
  "outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv": "a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7",
  "outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md": "543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9",
  "outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md": "1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a",
  "outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv": "d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91",
  "outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx": "a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4",
  "outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md": "9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b",
  "outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv": "dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_EXECUTION_REPORT.md": "de5781e750a45b538c9c9f744293f94da8b0b2706c512e31217cf3b66940cb5e",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_CITATION_RENUMBERING_MAP.csv": "11118450c5d744b4ae1bc7e6b39a2c74679fe13051d91e1e1b345712b0da747e",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATION_CHANGELOG.md": "c45f8c5320d14f56dcb54bc654e92608cd1d58ab5fc7a9eeed652a62f6921919",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_SOURCE_TRACEABILITY.csv": "035115773105e34fe363cf1ce5e201c9ddd765e886a4a17af4de42273e8a667d",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATED.docx": "fe4fd16fbb93bcdf39708740fb90dd120563825c57ce86bd9cf36e35f841d4dd",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_TERMINOLOGY.csv": "3b989e27e2ffd2079aed8ee2591f1ca9632747c3811b5b01f7a7601808a4a728",
  "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_7_GATE_REVIEW.md": "d47f43eb002cebc545c4432fa4ee8245c8a78127a905e8cd8aec44211ce2867c",
  "outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
  "outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv": "636a5acb7514ccd8309a6e786280252847bdbd5c6674264069866a772429275b",
  "outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md": "93abadee17152b5e6eef625915ea7b828ee54f69124335a2de215e11b62ae65a",
  "outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md": "efc42a239b43168aa4f24fe938892cc7969bf062827e92103e3587dc0379bf2d",
  "outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv": "346ffdf77c8e5b60680d7fb57ee9992765a7112de12673a4328ce3c8149a64f5",
  "outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_DRAFT.docx": "ed872c97025bdabc64b6efe79d83e1f80c0c72a021655b3401f90be16a327104",
  "outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_7_GATE_REVIEW.md": "d13a195c661a35102fd05bf84cf70b30249b6f98dc6460d94e6acbace7b034bb",
  "outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_TERMINOLOGY.csv": "4ee360f4f4af6586bbb79ea889ce1e33137399446d0d53e59c4a860500fd7dd2",
  "outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_EXECUTION_REPORT.md": "587899d88c7de77f303b2adad8aaaaf74fbdf7975347b2e3ba10790bfbda4dfc",
  "outputs/thesis_drafts/chapter_2/section_2_1_2/MP1_CH2_2_1_2_SOURCE_TRACEABILITY.csv": "ce5ddfff3e21feb71c970331f630042d444946e3356bdeb243c7501b3dbb271c",
  "outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_EXECUTION_REPORT.md": "fa14b05f8e7abedbbad2275643d8cb4737eea5ea4eff985c3b0e0c7598d0f857",
  "outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_SOURCE_TRACEABILITY.csv": "514418c27bdeaef445dfe9d0ec965c74ec3ad8323756ef99ef4718929f4479e0",
  "outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_TERMINOLOGY.csv": "53b4a03d93d41b04bbebf3c8ff4a2a8d526d2834eee2ce510ead0c65733d44ae",
  "outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_7_GATE_REVIEW.md": "37ae7ff62e9f728c474404c580b68dd9069b1fddc395681d80e9deb7fd6a7765",
  "outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_DRAFT.docx": "3b9cb65a0a2566d9ed44af6fd2e3c3d9c5891f5cf2d82b423f40bdaad8ac69ce",
  "outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md": "932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4",
  "outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv": "aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5",
  "outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx": "2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2",
  "outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md": "cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832",
  "outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv": "4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
  "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv": "ec725c4206ac2854febc16f7ddb882802c1d71e53037792dd6ad6383869bca09",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md": "b066121b47c37197b10d2bed2fa9709d5688d4973b5d13e23121c7bbf6ed275a",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv": "987fb13dda00f2d62abb4da346f2c6da7e3cbd3857749edc3f72725b59049a13",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md": "de894a4c00089ca73f15076e06fdba9870b86231e236f7a7add802e9f701a2d6",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md": "15fc8d6380b20bff447626adff74034251ab633c548dea0893a836d7f0f28fc0",
  "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv": "019d4780f896a73b3b85400675d394dcfdda1c13e8404d7a0ff9723db4887944",
  "outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md": "1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd",
  "outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv": "3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13",
  "outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv": "badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d",
  "outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md": "5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9",
  "outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
  "outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md": "557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531",
  "outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md": "757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4",
  "outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx": "1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563",
  "outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv": "d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76",
  "outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv": "c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5",
  "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2",
  "outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_EXECUTION_REPORT.md": "932c4309af5fa2350e3c6b7939895d1fef110ef61b24e77bca21b2129b5734ac",
  "outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_7_GATE_REVIEW.md": "5093e45ec9b15d8a19d037041f8e1c54e5456fd3ef70809d8feee33df17caa6f",
  "outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_TERMINOLOGY.csv": "b18046be7a681701704748b9459e518824d7906258a4ace925b7b020255a101e",
  "outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_DRAFT.docx": "c1b3571740bd20774e83fd88fab68bf0daf385ece04e7c0ed05d8f58ca12f5f5",
  "outputs/thesis_drafts/chapter_2/section_2_1_1/MP1_CH2_2_1_1_SOURCE_TRACEABILITY.csv": "cdc8064fe6b7340f879a746c3d6b8a7601d581f5e1568940d07d038223df7ec2",
  "outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_SOURCE_TRACEABILITY.csv": "a2de82be07c23a8347a29c6c8175d24981313eba835ba9b20c0131f018dc315e",
  "outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_7_GATE_REVIEW.md": "55aa3552084df3721f17a8e92c316cd893a0b1f588fa241141d1e7421e787881",
  "outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_DRAFT.docx": "5a529e4b33c889af9f7ac773bb962dad33a2a40de6356907a14da320a402fbf4",
  "outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_TERMINOLOGY.csv": "5efb3c9665cae07a28d64ee5246dbc66722b5df312a1d6417fd800e6d86f1807",
  "outputs/thesis_drafts/chapter_2/section_2_1_3/MP1_CH2_2_1_3_EXECUTION_REPORT.md": "8eaf2537b0cf161eba637105228e54c75c5ecfeb2a0bfc72399ddaeed05ee10f",
  "outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv": "0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc",
  "outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv": "de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3",
  "outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md": "86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7",
  "outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md": "eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648",
  "outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx": "9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead",
  "outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv": "e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61",
  "outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md": "31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97",
  "outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx": "a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d",
  "outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md": "78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec",
  "outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv": "3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b",
  "outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md": "e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d",
  "outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63",
  "outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237",
  "outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md": "c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866",
  "outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv": "ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd",
  "outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_SOURCE_TRACEABILITY.csv": "a44b71543c67007dd68da633e167b502efe50971ee44cbb8f11a4a6ba09ca95a",
  "outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_TERMINOLOGY.csv": "173ed29d9cd6fe71a88f834f89211eed7d7aebb0562fe236d68bed309884353c",
  "outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_DRAFT.docx": "aa67a00f47b99425afd9fe6ff2451dfe655af69d933b51a5c1cfbd97dfc82633",
  "outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_7_GATE_REVIEW.md": "829b97c08ba38ce59a754e3ffb6f2b8360886df1831a4d0a8e8bab75ed0502eb",
  "outputs/thesis_drafts/chapter_2/section_2_2_2/MP1_CH2_2_2_2_EXECUTION_REPORT.md": "dce059e88785531f6b5a0c9c2a97cd8ac44be7ef4df2a62146f9e3ddae33b06c",
  "outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_TERMINOLOGY.csv": "25bc782f7adb4b14f0531ab77be4d29642e18ba1b574f258491b51174c26113e",
  "outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_EXECUTION_REPORT.md": "9e6dba4acad36a783ec250ec703cb2c62b210492c7346c2dc6b42abc625c08cc",
  "outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx": "9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba",
  "outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv": "c57f02dd60264c9c7689211783a5ca51171abe6e479ca93d519c0a0464b0e0f4",
  "outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_7_GATE_REVIEW.md": "3c5a8a85b77c3dd685c6c50b0b757603910710f4dc7b5bd52c367961f7d7ffcf",
  "outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_7_GATE_REVIEW.md": "71835341eb8341818336b4fcc1e66be45929cefce303abf45b0973a28259a710",
  "outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_DRAFT.docx": "4d9d1136e7d3f690b11576e13c3af0dd4b872f7c4b4cf20e95e49c0ee664d598",
  "outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_TERMINOLOGY.csv": "471c346896b423a0b33687c188a04f0e9b43bdca4c1664a213463640792512d4",
  "outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_EXECUTION_REPORT.md": "52038547c0db16be2e96fe0eaa7be04511daf83883b595a440264392d77394f1",
  "outputs/thesis_drafts/chapter_2/section_2_1_4/MP1_CH2_2_1_4_SOURCE_TRACEABILITY.csv": "862395d594ebc05da2cf923d7098ebfde2c545372e8da42a31dfd13f847f8ec3",
  "outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv": "ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f",
  "outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md": "4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba",
  "outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md": "b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622",
  "outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx": "7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb",
  "outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv": "287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0",
  "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed",
  "outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx": "8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7",
  "outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md": "a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817",
  "outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md": "945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea",
  "outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv": "336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84",
  "outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv": "6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c",
  "outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97",
  "outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e",
  "outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a",
  "outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c",
  "outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca",
  "outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md": "c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10",
  "outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv": "4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa",
  "outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx": "a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4",
  "outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md": "15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1",
  "outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv": "a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463",
  "outputs/execution/MP1-V002/MP1_EXECUTION_KICKOFF_V2.md": "26a2a5d50f3967564fdc9b4690f8dcd2e2e6b5a1027c5594a628a1732a0ac57a",
  "outputs/execution/D1/D1_EXECUTION_KICKOFF_V6.md": "09bbccb7971ae197c4d9e0b54d4cf794be3e89de79472ffb2beb3694fab24440",
  "outputs/execution/D1/D1_EXECUTION_PREFLIGHT_V6.json": "b0b3fd7da9c6c675b727ea258e4f8376097f278b880daec122232673af9c99da",
  "outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.md": "9a5fc38a5052db588c871bf68026942a880683db5bd7d4898995158c042356b8",
  "outputs/execution/MP1-V002/W2-02/W2_02_CONTRADICTION_CANDIDATES.json": "dbed35258ac3167d988f1d8c7ce997445d9e6cccdb66fb64a60d120ef35b33d0",
  "outputs/execution/MP1-V002/W2-02/MP1_MECHANICS_PIVOT_MAP.json": "53ace14bc9ca36dcaaa8714d9c977e725f02bd22003ee2794a033cc00d209248",
  "outputs/execution/MP1-V002/W2-02/W2_02_C1_C8_CLAIM_REPORT.md": "af641a75883e48295c0be38908f658d7a8139f5978684ccd999c6afe70871b04",
  "outputs/execution/MP1-V002/W2-02/MP1_C1_C8_CLAIM_MATRIX.json": "1fdb65329328f9528b637b72a1b4a2a5544b4d4b3da9480e660b851ac64aa412",
  "outputs/execution/MP1-V002/W2-02/W2_02_SOURCE_MANIFEST.json": "41a955f5bb85f83ca848bb7c73c34f88117dd7367b98a1937587bc679d38c46c",
  "outputs/execution/MP1-V002/W2-07/MP1_NOVELTY_CANDIDATE_REGISTER.md": "06a8a407e5bff9b949f83beff18204f7fd1bac41442c669a2eb832a2fa925175",
  "outputs/execution/MP1-V002/W2-07/MP1_NON_NOVELTY_REGISTER.json": "78ac83ca8a25ba7dd1182a47dde4532d75114e8806a957611baefd147229ae7f",
  "outputs/execution/MP1-V002/W2-07/MP1_CONTRADICTION_REGISTER.md": "7f0f3258cfc942ab3f1abe844a8bb7382b452c8b459314e57297c88b4352d0ee",
  "outputs/execution/MP1-V002/W2-07/MP1_NON_NOVELTY_REGISTER.md": "40acc8f187a25be5a5156906765cd304c98a6c2e3d94277701002fad50937979",
  "outputs/execution/MP1-V002/W2-07/W2_07_REGISTER_QA_REPORT.md": "2b23ea3206f227afd483feeda63e919f4e9e31ede3110215611dd63ded17e572",
  "outputs/execution/MP1-V002/W2-07/MP1_UNRESOLVED_THREAT_REGISTER.md": "330529cebc8ff6fd457ec977d1c780f240d6f1a4c59f1687fe3573ca25101b22",
  "outputs/execution/MP1-V002/W2-07/MP1_PROVENANCE_QA.json": "6b8abfec740a34f521a74594c06b9c737d024dd4147342a7174da8b57fbd0d58",
  "outputs/execution/MP1-V002/W2-07/MP1_UNRESOLVED_THREAT_REGISTER.json": "31f51af5608786e5d466a36421fc7a589503d9fb7214f52744b6a041256ca970",
  "outputs/execution/MP1-V002/W2-07/MP1_PROVENANCE_QA.md": "5cc4d8953a24c43640c50da7c0fb90cc6316bae89eef081570a8f721d073033d",
  "outputs/execution/MP1-V002/W2-07/MP1_NOVELTY_CANDIDATE_REGISTER.json": "87309dbbf9ad74ae8d2f72e496a3e051c9bf8f872e26c74b9399935928bcc767",
  "outputs/execution/MP1-V002/W2-07/W2_07_SOURCE_MANIFEST.json": "6241ed158ed5ca3f12c1d72aeffa6faced8d4e3d4f6b2d828423b67864429328",
  "outputs/execution/MP1-V002/W2-07/MP1_CONTRADICTION_REGISTER.json": "1875f7583689d67fab67e390717a29d03ed68c9c7f2d3aefc81c099ca06bf150",
  "outputs/execution/MP1-V002/W2-05/W2_05_SOURCE_MANIFEST.json": "d99d4cb4965307d69cc38c12e75073595a732f13333c6f78a8143b0f688f0982",
  "outputs/execution/MP1-V002/W2-05/W2_05_RAW_UNIQUE_RECONCILIATION.json": "9eda48f9edf33c6c8d3494f452e7402e8e8aea31f0dfe42f6c3dca3ef40f1821",
  "outputs/execution/MP1-V002/W2-05/MP1_CITATION_BRANCH_TABLE.json": "579bf6c1a547a6a2fe0c84f65daaeb7675ab0c22748f433286fd246db49d4292",
  "outputs/execution/MP1-V002/W2-05/W2_05_CITATION_PROVENANCE_REPORT.md": "53ed91d3d0e8a8e872144e1eaf609d9b1007acf3aa6b6b8126640425c8bdd9ed",
  "outputs/execution/MP1-V002/W2-05/MP1_CITATION_BRANCH_TABLE.md": "335651b4bc51efb922082a16eb913b50359ae6a2b2525619cb0658089fdb1c23",
  "outputs/execution/MP1-V002/W2-05/W2_05_CONTRADICTION_CANDIDATES.json": "8f6f05c86ede74edaca68ae03d23383015d9cea000bfc27e5c7067cb09ccafdf",
  "outputs/execution/MP1-V002/W2-05/MP1_CITATION_PROVENANCE_MAP.json": "6eaea4535906a988d8a91189f50812ab8aab89f14c25686c7d163c42b20cd307",
  "outputs/execution/MP1-V002/W2-08/W2_08_KILL_GATE_REPORT.md": "6aa3ce16f45dfcb6ff0da2b6b4d5efb6079fa3a419003221ccb6bb293fb5f235",
  "outputs/execution/MP1-V002/W2-08/W2_08_CONTRADICTION_CANDIDATES.json": "1875f7583689d67fab67e390717a29d03ed68c9c7f2d3aefc81c099ca06bf150",
  "outputs/execution/MP1-V002/W2-08/MP1_KILL_GATE_DECISION.json": "280b3c9a7c85eb6145301552dbeb8ee9add9d196ecbe3b40d7f9ed9565bd312a",
  "outputs/execution/MP1-V002/W2-08/MP1_KILL_TEST_MATRIX.json": "19b9e5b464fd12e7167e22a2246ca2514fc001d202f82cbcf3f88bd6f22a6e6a",
  "outputs/execution/MP1-V002/W2-08/W2_08_SOURCE_MANIFEST.json": "9f7cef62994211d845335ee70e533846b9aefd66faf6583f52b9cb1abb683b21",
  "outputs/execution/MP1-V002/W2-08/MP1_KILL_TEST_MATRIX.md": "16b8f901eb9d9b2fd4aa84feb68d2da2cb629a01f8799422e86f4d74aa324569",
  "outputs/execution/MP1-V002/W2-08/MP1_KILL_GATE_DECISION.md": "0f1c061af369055d16121c5f6d04d06a56d79288f50a7e975071dba105e77d76",
  "outputs/execution/MP1-V002/W2-08/W2_08_BLOCKING_THREATS.json": "12ccbbfbb1039e6b8ea7134901077ecb8c7740686cecc0fbe9a28ebf030f64a7",
  "outputs/execution/MP1-V002/W2-06/MP1_STAGE1_PACKET_MATRIX.md": "a7fd1098ce21941228bd5677746d34a4e2cb58b7e48bcc1e5438dabf117863ec",
  "outputs/execution/MP1-V002/W2-06/MP1_W01_W11_REMEDIATION_MATRIX.json": "7820257d5d19bc3322ce777a66ad0d92b7b76e71496013b2b7a430597e62ff78",
  "outputs/execution/MP1-V002/W2-06/MP1_W01_W11_REMEDIATION_MATRIX.md": "c2bc41dc3fda9deb3d98df1cb82427c000542a7f9e301e50b83ba0fcf89febe4",
  "outputs/execution/MP1-V002/W2-06/MP1_STAGE_G_W_CROSSWALK.json": "9769d94b9f37188222c84dc8e838d3f8501549aa899a0592b5d2313b0c84dc53",
  "outputs/execution/MP1-V002/W2-06/MP1_G01_G12_CRITIQUE_MATRIX.json": "a678bf8b793fd03d2d6cc4dff66eadb973a6d486a0409b46bc72baac216f52f3",
  "outputs/execution/MP1-V002/W2-06/W2_06_STAGE_G_W_CROSSWALK_REPORT.md": "219de8366bb709a1d1929de225391998d9b86a5970a4e7e078d0b91f71eabb84",
  "outputs/execution/MP1-V002/W2-06/MP1_G01_G12_CRITIQUE_MATRIX.md": "05d5f4de7b5742286cb653df83d8018a38b493c2d818bc8065c71f568f8246b8",
  "outputs/execution/MP1-V002/W2-06/W2_06_CONTRADICTION_CANDIDATES.json": "c2deda49f49500b0aaf7b30768fcca4668522c206f58c0e0572b1fde1a6fcb62",
  "outputs/execution/MP1-V002/W2-06/MP1_STAGE1_PACKET_MATRIX.json": "3391ad231e9f7428293a050b372d06bb31fc87335d46528062fb69c4d4225048",
  "outputs/execution/MP1-V002/W2-06/W2_06_SOURCE_MANIFEST.json": "ee75bed4802e8ffa138eef052a02b9d81053738c53e970c562b07f97ae9cb70e",
  "outputs/execution/MP1-V002/W2-09/MP1_RED_TEAM_CHALLENGE_REGISTER.json": "2de77fecf37550077869a9f2895607efb021a22b0fdc958b9ca2c8e31fb2ee92",
  "outputs/execution/MP1-V002/W2-09/W2_09_SOURCE_MANIFEST.json": "8e57a0c40e3ac0e2718d8aa2279be23eb09bd430c7b4e8c659e2011990361b80",
  "outputs/execution/MP1-V002/W2-09/W2_09_ASTRA_RED_TEAM_REPORT.md": "e90a2271310293ce506e6f02c9185f860eb91bbf64bbaf22f74c9612c4743f88",
  "outputs/execution/MP1-V002/W2-04/W2_04_16_PAPER_ROLE_REPORT.md": "c0b6ab9c2ce72c39b163c94028154b4a5795941f8652460de86973d57d2ec9e3",
  "outputs/execution/MP1-V002/W2-04/W2_04_SOURCE_MANIFEST.json": "50b64837d025349b5d87c1522c91accf6902c5dafcb44afeb5df685576c5f279",
  "outputs/execution/MP1-V002/W2-04/W2_04_CONTRADICTION_CANDIDATES.json": "871eae02180e7a0c2eacce5f58cdffd2d2e281dc97e177b85971b9790bc9c391",
  "outputs/execution/MP1-V002/W2-04/W2_04_PROVENANCE_GAPS.json": "65189e6623799d1d28b21f54661c981f604a1081d6630ea1c49d5e65c4f5a37d",
  "outputs/execution/MP1-V002/W2-04/MP1_16_PAPER_CLAIM_CROSSWALK.json": "95f90b1b8ab84a9f42786aeef528062afd6c0cc0790aed1ed769f486373920ec",
  "outputs/execution/MP1-V002/W2-04/MP1_16_PAPER_ROLE_MATRIX.json": "53af87f04ddf1c19dcd98110c6101fb244aeff0eb088348cf0357e7d728ee63d",
  "outputs/execution/MP1-V002/W2-04/MP1_16_PAPER_ROLE_MATRIX.md": "5c58b462bcbedb98cf39fc8f7ed617de71b5ec759746be83e929fd23eda6cc89",
  "outputs/execution/MP1-V002/W2-03/W2_03_CONTRADICTION_CANDIDATES.json": "a8bc8e0e29e73750c6d78be5c9575a7bfcb61523243e017f3b7667027cfad3a6",
  "outputs/execution/MP1-V002/W2-03/MP1_COEXISTENCE_IDENTIFIABILITY_MAP.json": "c54fa6d035ceba27c7ec7e142cb918fad8ef18669eb77efbdf27ae05c4ff2741",
  "outputs/execution/MP1-V002/W2-03/W2_03_SOURCE_MANIFEST.json": "ffc90dceb472ed2010f54756f695229f6d6fe1e4e2dfcc5440e0903166a0b377",
  "outputs/execution/MP1-V002/W2-03/MP1_T1_T2_T3_TARGET_MATRIX.json": "ce750e153fdac262b9ff2169fe4c9a2d5266790b07c6738fe8540ad09d38ffb2",
  "outputs/execution/MP1-V002/W2-03/MP1_H0a_H0b_H1_HYPOTHESIS_MATRIX.json": "1e6a0343e91f2d8ec219190d47514d2c12f67721293fdce1da65b3e6cce83b4d",
  "outputs/execution/MP1-V002/W2-03/W2_03_TARGET_HYPOTHESIS_REPORT.md": "094a879dc1b892c7c3dffd46fb099a5920e941b8bc7fd68a1ea4f43249fa466e",
  "outputs/execution/MP1-V002/W2-03/MP1_H0a_H0b_H1_HYPOTHESIS_MATRIX.md": "4ffc87951bc91f913f24c78d6989e1c8fa71a0581aecf217781fb31a720b3ee7",
  "outputs/execution/MP1-V002/W2-03/MP1_PARAMETER_SUBSTITUTION_RECONSTRUCTION.json": "1e1eaaaa61cc655d67a70b9fad6bb8793e69b0a32a51788003acf8d25f3b3550",
  "outputs/execution/MP1-V002/W2-03/MP1_T1_T2_T3_TARGET_MATRIX.md": "7015df458650e03526be45d4df49d14a16e8489bafc1394d647a6c547f66cf13",
  "outputs/execution/MP1-V002/W2/MP1_W02_K1_K9_RECONCILED_MATRIX.json": "101a121e74fd0a8997a12eb441069e7c23e1dc7aeda457a23e29c78e4117d3ad",
  "outputs/execution/MP1-V002/W2/MP1_W02_HANDOFF.md": "504c36a4ce34670291897598c18600c513e416fa39b2051f7019717ed991c2b7",
  "outputs/execution/MP1-V002/W2/MP1_W02_BLOCKING_GAP_REGISTER.json": "2a8f4f138574b50a6a45302688dd8b12819658f89b5ff87b365f1540242f2c59",
  "outputs/execution/MP1-V002/W2/MP1_W02_FINAL_SYNTHESIS.md": "9cba3ce0bd0180f9e40b962ffe4b95a1e1cc1825dfbad54467bcce6bf66467e6",
  "outputs/execution/MP1-V002/W2/MP1_W02_CLAIM_TARGET_HYPOTHESIS_MATRIX.json": "396cba81d02078a7210f02d43f0e3c3fa89c8dd54a6151c53113f87aaa28c870",
  "outputs/execution/MP1-V002/W2/MP1_W02_CONTRADICTION_RECONCILIATION.json": "d0972db5a277fb6477eab00894045e3a8f2d301f25c2aab464cf2217f6d6e8bc",
  "outputs/execution/MP1-V002/W2/MP1_W02_SOURCE_MANIFEST.json": "f868488fbb2f1e73e1a8b0dc44bb0cac931a2a4f0aa77ec33572b11f7cdebf56",
  "outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json": "39f197611fd738f36abcdf7bd18783cbb1ee79af47e1509a4f8dcb10019f5060",
  "outputs/execution/MP1-V002/W2-01/MP1_HISTORICAL_STATE_REGISTER.md": "75b6cf4ffdcc5370b2978891ca0c1deac2fc04e3db4ea0d97a363ce1033ed810",
  "outputs/execution/MP1-V002/W2-01/MP1_HISTORICAL_STATE_REGISTER.json": "c296bdb901ee573240fe7bef2b93c7e26ecbc7d74e4a0bab21ee7389129dd0aa",
  "outputs/execution/MP1-V002/W2-01/W2_01_STATE_HISTORY_REPORT.md": "d656a7f7106c739d524e40e0e63c90e69aa5a5d008e61bfebf899f928d841e1f",
  "outputs/execution/MP1-V002/W2-01/MP1_HISTORICAL_TRANSITIONS.json": "4baedd1e4bfe403dd5fcf6650beebd486e503f53db83a68c5e8efc3954829559",
  "outputs/execution/MP1-V002/W2-01/W2_01_SOURCE_MANIFEST.json": "dcc0a8ea411a4343573a7fa48d62579a380083d2e23c5dada901e9bbdcc32655",
  "outputs/execution/MP1-V002/W2-01/W2_01_CONTRADICTION_CANDIDATES.json": "db01371bdf8a428cb7dac728e719d21b7635de7d2e641e5d8cb40676efef6e1b",
  "outputs/execution/MP1-V002/WR1/MP1_WR1_EXECUTION_GRAPH.json": "79bf335c2dbaf036cdae02f547ef8b87e579f240ee9cdc1da92f0cf617347402",
  "outputs/execution/MP1-V002/WR1/MP1_WR1_HANDOFF.md": "d684f5ababadf970afc60cae35f319b33309cec629280b2f4904f1309cb74888",
  "outputs/execution/MP1-V002/WR1/MP1_WR1_WORKFLOW_RECONCILIATION.md": "d44268c7e18644fb7eb22a48311fd23ad3415e57c5ddea9562e2046a99a8528d",
  "outputs/execution/MP1-V002/WR1/MP1_WR1_FINAL_STATE.json": "74cd2de7d92ce076091243f32b6e2560c9f03068888791c5cd47888a44a2d455",
  "outputs/execution/MP1-V002/WR1/MP1_WR1_STAGE_GATE_REGISTER.json": "6bef40f9c794b420bd83314315a7808252298e2b1262aca8ef85ef90d4594ba7",
  "outputs/execution/MP1-V002/WR1/MP1_WR1_GAP_ROUTING_MATRIX.json": "1deb537cce2510e8b6c87413af04234057244ab734f86f0f634ff8ff8336cbe9",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-01/worker_report.md": "c7b894f7c5d86f3c96aab417463a284c7390554807103d1c33ed1b53d6865f08",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-01/worker_result.json": "11a184338bd38fa233812d593594183907e91ccdbf30a5b5966a75572f48004c",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-09/worker_report.md": "a5de3db3968284a0d45b363b6c618bef977a8036878598b891d5fb1194b9453a",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-09/worker_result.json": "55a76b8c8eaff3718db806a907b01277e92e5c3bbffa032d0c722d96c2cbe5d9",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-04/worker_report.md": "150f5a2b255b5ca893877c777c5f95c25d9d57df76e7d116b1c4a136f09f5bd9",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-04/worker_result.json": "a8ce75a6dafed84270e80484ef1357771c2cf2a4aecd335e82f3f374c74b9329",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-11/worker_report.md": "ed90f86961210e5b7952f465e37e2e00d5940fd6d308be8a3d34693d0b16e047",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-11/worker_result.json": "7cc099f254ed71c8096dac233edccd2b24dce0990c27c140f014a3c524262bb8",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-05/worker_report.md": "95b7f260a738f944d8af54b9c6ff824e60f50249fcb3ef7998527b0f931d45c8",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-05/worker_result.json": "ca9ba37f42adc5939339da788d2c3650e4bf9417a66462a008e55ad2f1181c15",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-10/worker_report.md": "9e2edda1dc944cd0c2324cb054373a3e780322ffb9e753ce968ca82eb846f9ac",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-10/worker_result.json": "09118f2783057d64e98c73b573ddd3848144f6c254da1724391b3538de653980",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-07/worker_report.md": "3fb669d538373fdb2212413406da71f553c3646fd8740f49f9a0f1e8a0bb9536",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-07/worker_result.json": "4e7f3307c4d3e9562c4465812eb08a36ab3ff31ff9c0d0440f57203882bf1a51",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-12/worker_report.md": "27ca6b79c81e30054b3ff3e7d85505b2bbbff5825ad79bbcac96c8801774e372",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-12/worker_result.json": "fa95c2f5688ecfe29f107df15f365c45253dca73ee331b2ad7e447a3d026fd3f",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-02/worker_report.md": "e78f2c10c899d291acef057b289f184541748dc1798dafbf5edaa9c0956ba142",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-02/worker_result.json": "851a975d8deecfe3be4c3f7dc17908d733f82645c2cc7ccda690971aa88041b2",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-03/worker_report.md": "e1cf45a0f069f5b29c7e61cb4d4117dcc435ff0d86822cfe1cd6534fc2075b15",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-03/worker_result.json": "5ec3f48c2b4164fcc10292c14cce2dbaebc50184ed7201913b788ad1b193ed78",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-08/worker_report.md": "73df3277d8ad2edf0f8da73f82996917ff45cb92e3537f98e6fdec11275859bd",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-08/worker_result.json": "a4bbe83a630e394d77e4b2ad31a0dd3624783218c77cca441b655ac1afc3f91d",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-06/worker_report.md": "faf6badcc28860832ce7a847d47d9c00d49e3d58dc75dc47e16a8f8c657a90f1",
  "outputs/execution/MP1-V002/W2-02/workers/W2-02-06/worker_result.json": "3eefd970f5b5cc07fab82ad926eec2e6109afb56126839127e1f80c40ae7ef2d",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-08/worker_report.md": "b4bfbc63ea99c3b7f9c137c4a1fbe66a7de6abe986b528b75f19f01663a5b7a0",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-08/worker_result.json": "022b2222afeee053fb9c80b72e00a35c5130320a44069330e85a07da72aeed2b",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-06/worker_report.md": "eb3bde9c6eb2f12d4336c6ca89ac49f6d072df056fa289ee1bd0b8db6d5998c9",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-06/worker_result.json": "82e8a331228776ec74802bc7390d2c1730afed5cfc696c24ce5affb5926446f3",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-11/worker_report.md": "7e6b5fa431a1482f9584890038d05ea528e38ca2770ec882f76e3b1bd1573cf1",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-11/worker_result.json": "f0bffadb64c672ef726de4963c91ad651df5b5d4107c13b122e8d2cfbac4f877",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-05/worker_report.md": "f0c1d15ddbe2dec6d5cbf4f2feda8c8db736ee60d19de19d9feb5ed1fcc2397f",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-05/worker_result.json": "fa42814d64062af2b61f3ddb1e972b6e4fd766c7c1d3671f55d955842e09667b",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-02/worker_report.md": "09cd0c0e328a22aabdeb4d06256d57dfdddaa1ceb938af2f509250e5c62eb71c",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-02/worker_result.json": "6d601f2fcd3c4614eb1ffe7739623f8a2bda2b07434712006a75bef2117d1ee6",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-07/worker_report.md": "533ab998c8331566ad0650ba3d1847d14e11b222aeca81545acc2179cd869f52",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-07/worker_result.json": "474f094b860861f0d4c5adb5c253766d907cb07357afa418ab63aa6711c5643d",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-04/worker_report.md": "a9a8405dc8efc1bfa7b316810a4126d5100eb22e7a524e7f2eb76a67e6d052fb",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-04/worker_result.json": "210e3af1dc1cea6e5c0eb838b2f984116b28984bcc9b86d52689fb679912595f",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-01/worker_report.md": "dfbcfabe79fd070805099a96cc284df0a9ef8e2d3b0ed4943b3fc7e4e6fb1467",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-01/worker_result.json": "d7f62b38d12939171b3c28cbd5c7361f9d24a70ad39f8936f1f3336c17fbc725",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-09/worker_report.md": "5aa2835b26a27fe20f0d6c92cd69dbe009a2827b1cff096cbfc96a52d1b1dc3c",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-09/worker_result.json": "5a91154c56b09886a4c1edd1f8776aa90e3e928c72c3d060b2f5b86474621797",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-03/worker_report.md": "85723c975c8ac947a7cd8ae4bcc34d1db9dbe4be4b4e67bec5a6f1c8f030839c",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-03/worker_result.json": "0ef081545580a487673f85baea0907e35dadbdb68a0587b705b28e78c98134fe",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-12/worker_report.md": "7631530ec69c75358e5b9a728f1f23c7c43c93f0db9c81880bded4c0de2ddffd",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-12/worker_result.json": "257c6d4c79a96edc47935a511622ae3b6bbe1dae95f506a25526e00d34e71032",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-10/worker_report.md": "54dab7887568dd0cb301a83fa45406995725ec463ba9417b5d2cc48446fa0df8",
  "outputs/execution/MP1-V002/W2-07/workers/W2-07-10/worker_result.json": "ed508a9a94c2150f251a111c0f06c07d93d6b7368b5368dd6a58392d74201995",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-05/worker_report.md": "623cf32b9d70b140b05dd50584c51d9380df8863590c7252fc40a9417c114c73",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-05/worker_result.json": "d1380bc97c9a60708080bd079b1e537a7650912e3cca0421d051ab5e823dbb3d",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-06/worker_report.md": "678b536f7f72d86c70289257837cc1185626c35a4f00cfd7a9db6a989edef72c",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-06/worker_result.json": "dfaf54b2aab76c33546dc4973e064ea3c75bf31eb9e080adbfe7f416a6307aa7",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-12/worker_report.md": "268e1c338ba0cd6758b2b56c0cf8e768ee1e285230fdda6b22f856de820b8d03",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-12/worker_result.json": "5027adf2b01e182e3a8053bb78c0eaf247da651033ec44ec8f8d972f4b00b4c5",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-10/worker_report.md": "9964e94703fdb6029fe01c8bb778095c90b833354f9fa66b4ba86429614f32c5",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-10/worker_result.json": "1bebc4570e1042d488c8bd64a9647cd30ceaad2a2a1a0e6876097c9a92cbad09",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-02/worker_report.md": "7c05d2216b0500d3f9f97e36a7c9d309dbe5149b49172c629c6c6b415d0b536a",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-02/worker_result.json": "3452b62f7d90ed6aadee851caafb2efc3b6fd710ab90c2b9ee017eadaa6edaca",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-11/worker_report.md": "c93243dd585bd1032b5cb51016266ed24c455c9416b29ca6fec4604c10655e5e",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-11/worker_result.json": "4593214b11d5bdf74adf16691938864734d8d7e5988533e1d57402aab7bf056b",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-09/worker_report.md": "5047a1ef381473fd18cecb6051c74b9e826454c616f342514422bb2fd94eb0c7",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-09/worker_result.json": "b1486f011354e00bf851ee49ad1694ec2e888a03fbf21b43e2193651b82caf51",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-08/worker_report.md": "c6c8d430bc576c0b26816a50a94b59d15dd1e6aa5530a7e3187240e03110cd98",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-08/worker_result.json": "dec5e95d91e8c642fb02ca5ca017b28ecba7494bdc85bbf470eedee8eb2f5ef5",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-04/worker_report.md": "3f0d786fa452addc5060dafa36f5f1fc11d5b3c745daa0aff47173f4dc8f0a94",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-04/worker_result.json": "4200366341e828b987b2e7f80a355d9cdd34157e7a8932c63659f1ffe08d6d4b",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-03/worker_report.md": "be7abfede4b8316da835422c3609f31f55739bc14d741285e7d3512683a89b62",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-03/worker_result.json": "d773ece1d38c9c7ec363528dd88d76cfb81fdfcf83bfd5e1f79f11c5052c0856",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-01/worker_report.md": "0166bb5232802169adeae5ce6ee55c70af203fede843a29428fafdc43135c396",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-01/worker_result.json": "758a723c41bfe423e898ca09bdadf44bae55313e559cf30c9cdfe4c6edf574bb",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-07/worker_report.md": "5084cffdb00c019d11b12258ffb7f4b4b2be76b6a97a434e50e08571dd19778a",
  "outputs/execution/MP1-V002/W2-05/workers/W2-05-07/worker_result.json": "b591f16b8dafbba6fbe164e86ad2c1d48719ecf9878d47c253c4ea6d3874c499",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-03/worker_report.md": "96740c00af5f57c03b4d6def5ea2a38d146f98f967827859aae19f197b557a53",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-03/worker_result.json": "9d40cdb50832b827a0cfaf20ad25125af565eef2325458821e98e108513fabee",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-07/worker_report.md": "cbdc7efd79914daccd8a3ac347796ad9de482f0bb3e989cfbba94c9389edfe7a",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-07/worker_result.json": "fc9644b4636b16e2d76cf84a933b4c0edcd2104d243ffaccd4c03b8b1260b025",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-04/worker_report.md": "0bc991ead9059a421bf162c08f452984c8e590fa913f1f0e7ec17dfb50c5059e",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-04/worker_result.json": "004acfa7cbbcabd8de827a640ee6c0190ecc4dcb7a39987e0ffdc0516bdba061",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-09/worker_report.md": "23298614de6df8a4f51a53315904861645d48b2b1a4cba6e51ff3b419f0faafc",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-09/worker_result.json": "8677db38369de1ca8ae0207e38a89d50c136cdd23fce15efb29f05e778372e16",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-06/worker_report.md": "6ac0363222e4d1bec18c8ed44fa5a85842746ca659902133383f69f8f1339677",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-06/worker_result.json": "60b3854e653be7ee7c80f5a966d191a967d908a443c33f53d92ef42579b989d7",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-05/worker_report.md": "4a4d2089e8a8ddee0c8a5bb82ed6c95e23876b7eabf87bd0852b8d4316bb6f07",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-05/worker_result.json": "4741b0bdfe7b7b81ba4d71bfaf4a6b569e33a7eec165134568d801a209a5769c",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-11/worker_report.md": "aa4b2663c88dc2579d5dae550e932d6a05b690b66980572f37afa97428474bf7",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-11/worker_result.json": "6129021ce7c1d3973c4a817b0a0567da7c1976c04887f3bc6d35bf3df066ac91",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-12/worker_report.md": "4c76d8aa2e180223eb31f0c814671eb7c06ff382979cf191be32574cc85be395",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-12/worker_result.json": "a875aa7863fafde7bec18bbe504e5372978ae903bb4a1057b44db86b0c9b70b4",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-02/worker_report.md": "acc0080939649a5ec9f8377c710106f999382f67e94b8f438de6d909fd2fb68e",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-02/worker_result.json": "927416812f55aad9eb1c06395d760e4a4801981740e52898f511cde33ef79f8e",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-10/worker_report.md": "564e968a5679f2de109936c6d650d75d687dae7f74cfb999b4dfb3802952743c",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-10/worker_result.json": "d0916b81c00a55d93bcacd5735a4954835823c4004f79184c3b0f0e2c272f6ae",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-01/worker_report.md": "5802f708bfaeee526cafe07e76b5dcbd1dfcac36a1cfa1943bf1609fb8403072",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-01/worker_result.json": "0f2f2488dd65235b08ed2f01ed7f06aa9098167247e50190768bc6dfbb21c465",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-08/worker_report.md": "c229331db0662418731c786beb08623700e7597bf594f5f3b611e05eb782eb3e",
  "outputs/execution/MP1-V002/W2-08/workers/W2-08-08/worker_result.json": "30a56311a3b54508d5b9f9d483a0bef134012df37e6ee959cefb7237f52b1199",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-09/worker_report.md": "757f988679c7fb448f59575c6154b30790c0f461d7e78a875f02e79fd23f7587",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-09/worker_result.json": "45e63c8d32dc0ae0eb9c71bd392988ab558e9d5c86f9e751ae6714f61fb257f8",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-10/worker_report.md": "50783886d63a5f8a05bb3cf1268fb98fe66a2449698503598d2765a58a62092e",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-10/worker_result.json": "4442736eab968971fdc5321ea088f3262ad28c9167a9f41f86eca03b25fb77ea",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-01/worker_report.md": "8b3d71bb361846a9ed9e137099dde504bb8e1a1063bdce2d25cac6b690e3f2f2",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-01/worker_result.json": "10397eb93a8660416e64c5a45ace1f09d19e58324a1a1d7022921bdde76b0974",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-05/worker_report.md": "957172bb4a26fd16001dc6f098c99468df0a022c88c630ee7eb381590819a842",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-05/worker_result.json": "2f8549758ad30112fe24ed407bd6b456928fbf084991db8a7eb38ea66c82e39a",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-12/worker_report.md": "30e611d2ef782bd8b719c96a5daa1374e8e34898009ad0dcdaafd268d7f26bc6",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-12/worker_result.json": "cf16f9c34a4a288818beb74120984cd795cb335a15ae16d06b2ad8594e9411e1",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-04/worker_report.md": "5bc34494768419c34516004540b3fc05a210e00cf1da253941413a89d05c4b53",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-04/worker_result.json": "41a3fd815787eb88845681c93f5a5a1af6bd70c70ad413bed45f521a51db2235",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-02/worker_report.md": "04d7770d1a88209e5725e4fc334454a9faf18bdfddd241e85d23af250cc3e9a6",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-02/worker_result.json": "db8e82cb769cdae55f7530166ca64d123aef5ad27d63548507f0511beb309efc",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-07/worker_report.md": "1455405b362ab94ea9b0ac5ced2eefc4cad0b85cf9bad59229ac33fb03e41a5d",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-07/worker_result.json": "2b31a182d1bac5aa5bbd0225c76ed594db49475e3effd8a428b158ab8c970f8e",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-06/worker_report.md": "c526dcbcf644e4b09ba6da1c8b7746a45c082db5dc0c8097b7630121570dfaa9",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-06/worker_result.json": "9950aab4a11cd85224cfa4e5d557794df85ee5807974383b2dd80595a0a2b18f",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-11/worker_report.md": "c5f199c4507b17faff4efeb6032ca9ed6925eecab2ad66285f8fd9bf44ef206c",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-11/worker_result.json": "cd5bb3ffe2b77a8551032572fa0e8e8d519996d85c7e107cc556bb9288f664d6",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-08/worker_report.md": "353dbcbe5fd8e746ecbcd854bda74743c0afbf7ca40442fba337d17f4f7eede3",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-08/worker_result.json": "2f7dccaf424e4cd881680a01bba30ae2a532124a7a479760f542cda28b01b4ec",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-03/worker_report.md": "3d9fbcacd0507ecf14cefa1962f401b810a356d893f284ab66dec4a45cb120b5",
  "outputs/execution/MP1-V002/W2-06/workers/W2-06-03/worker_result.json": "a89fabc57d348d0e262484671b41e940022bc051d45ac87a59cbe7d92c98042a",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-11/worker_report.md": "4f0005e185392bfd686301b3fecba3206950f0e7315ee5e617cee7eec2f403a7",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-11/worker_result.json": "80d3b57c91f35fdedd8093a0beb6f6de4b837ee70e169fd1c301985963a7bea5",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-04/worker_report.md": "7134027e2e4843e8691e81553dbf2d7aaef9fa503ae4f101169401f8ca893fd5",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-04/worker_result.json": "9380497d874ed023ea6347fcf19454ee84f996f98a96479512ec6876a0ddaf33",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-08/worker_report.md": "0e2bde42e522bb5bb05a68eae5b81f4234428ef6b92b5dba4a6528b5dd57dcda",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-08/worker_result.json": "5488f503a4fec24d4b245f72cd46ed6f5e8d4c2d7cb03fcc201332c2bd1b501b",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-02/worker_report.md": "3286d99df83e32b1df6448958b8822f9ea5e0abe6af01087cc39c776cf4d313f",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-02/worker_result.json": "d68cb54849401216223f03d8855afb117a5b65febdbf375be5964e0dea60be56",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-10/worker_report.md": "b4d939b6d0ed4a32950e08c03ef35aadb811b8243727011960180d27d481fa28",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-10/worker_result.json": "64a6eddb294e6887793bbe408dc725862789ac825d889857bba4c8f671a1d55d",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-05/worker_report.md": "7107e5fbe972351b7c3b1cb5504ef10245885bc7142bcebc76643a8433c0fe3f",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-05/worker_result.json": "6c8ce317558d02698b2366b7836a7eba919f9d91f614df15646e2d8d3137dc25",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-09/worker_report.md": "b7a69ff2e7f363b14fb74fb232bce345212293b9a8adbf37170e4c9c05e2d5c8",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-09/worker_result.json": "f5dfd9ab68879fc0c756e915e2682e2867dc980d28c5cdc5e8c2ac19eab73252",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-03/worker_report.md": "1ad452350035d33f83102bfc120e4baf9366d5e0ab9c7d7338ef3530b26a0bd2",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-03/worker_result.json": "b43c8e50a1b7099d076cedbed9f81a21f4a5e8537e857135120577f6b79749b5",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-01/worker_report.md": "7a43ceb4f3da4005af55748159bffcc8d74cc7172def25994c74aa374d82f765",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-01/worker_result.json": "bc35b1552c16f98b76dababc7e309a0a23166d18cb9823107fab7b5dc2944327",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-06/worker_report.md": "acfef17bf8300f76c01c7da9ab2b58ca240f579c2d973d521226048c21c01aff",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-06/worker_result.json": "fe576f7412c5a13f7241bc89215ea4eaed75b8a55c99c97c286a6c5b4d918d9b",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-12/worker_report.md": "3ea484c032913a895c0d8a80694297c89d896a4f6f0d6950bb0525d6bdd3c6b6",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-12/worker_result.json": "5894555cb7f9075c6d700ad8043688d651c8ab9075a5b1761e5b71b83c988131",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-07/worker_report.md": "5a251247fecd176470aa532322264c9fa695584541a1d697b5b425b026799fba",
  "outputs/execution/MP1-V002/W2-04/workers/W2-04-07/worker_result.json": "33448f626e72722648eb74373aa035e4da9f543aa81b1fe86bdab4536999b61d",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-06/worker_report.md": "ddf25f148d0cffb1e871f5447588cbfaac377960b6b6707d7ed8351bf6936876",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-06/worker_result.json": "bf0d63c9e8dbeb9e67ea8d24a2f67cd2953f054e73a622672afa0578fa60945d",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-12/worker_report.md": "463bdbc9eb7c24133252175d92320c761ef92bac5b897d679893a391990d2217",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-12/worker_result.json": "756d01a308f3128fe02ebbb5718d0e604e257e92abaf661853657f8149a22382",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-04/worker_report.md": "4ef0d5ddf710f43468e00930ac5e47e211486e282e5f8b3410facf948cca7221",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-04/worker_result.json": "059a178b5f39736c8669e21093599b42e0d84faae89850fecd6cfcd42503a88e",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-09/worker_report.md": "808e7d36f5bd4482b0cb6732046829f13911c1c8e802ea52103ff8fc5167d7c8",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-09/worker_result.json": "dd6aa0e7840767e667667e6c8c6496e24c1a0d43dacc2fdbb2d91846f90f5b03",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-05/worker_report.md": "0ed6bab546eef8d29c252d524f5b0be129852f5edda635ee03ebd8e86b810040",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-05/worker_result.json": "2ff098d0e2260eb98c641d8f8b703bafe9f048c677a4e5ca053b8fadded04a01",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-02/worker_report.md": "5746379af571340d69b6756f5af170a760bdff973db4d6756c2fe0a9c9a4dc4e",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-02/worker_result.json": "e2aba9fb50a7f32086f9990cfd6110dd228437449661db958a39241205cf0aef",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-07/worker_report.md": "800eebb36b7ab87a91497cf0f4d5f169e55cafd618487e5594ef64f45d9b62c4",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-07/worker_result.json": "1f10a5719f33629ff8ddf9e224123fea544f2d0f61d7a93119a722b24f3ef19a",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-01/worker_report.md": "ac635e2154b7198649bab37232f74897def7d56a518f842f9e807522c23c31f1",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-01/worker_result.json": "299d502d2fde0ad70a63f3c31dd6086c78c986de480f08e7ee1d1dcdfd0070ab",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-11/worker_report.md": "8508ea1b07145b1af68b4a85c6e9ab1bfd4179def1d21f84d4af6a1c8d55783c",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-11/worker_result.json": "33694e19fe1b8de49111de55253a57408af631adae3e26cdf755ba6ebab2e696",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-10/worker_report.md": "1f129e1ab4a3fc55afd30444d9b896ea4497efa325db45a430a37f1af5405096",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-10/worker_result.json": "ef9cd4fc9013e5c80457306bdabebcf9d0b2525de69bb17d403bcf9ee20d8682",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-08/worker_report.md": "1cafd7cadf0b133063cea486b1a6d4c2370113b387156487e724d57a4fe72dbd",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-08/worker_result.json": "1e1eaaaa61cc655d67a70b9fad6bb8793e69b0a32a51788003acf8d25f3b3550",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-03/worker_report.md": "90f75054d0b33dffd101801a18696d72827feb65329d07f48735fa099dcaf3da",
  "outputs/execution/MP1-V002/W2-03/workers/W2-03-03/worker_result.json": "24a72e3deae2408c016ea540419f22f07dc9e1aab0f80696ac3bf9d444bc9063",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_SPECIMEN_AND_APPARATUS_SPEC.json": "9051fd9df923a2e98c044efab371850f37869528ed3898f7362f74321844bce8",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_COEXISTENCE_ANALYSIS.md": "d2ca64923da871e37b233cf2aaa574db05bcbf49e1c2675889e11749e4ea849f",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_STOP_AND_PASS_GATE_REGISTER.json": "c56ac6220d67c727e7f322d53dc67cce1c688c825bd54266ec656a37011a0867",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_TEST_MATRIX.json": "f42bdc1fd694b7b704fddbe0aaec282320efd661a443cea6b727b5e63819d3b0",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_RECEIPT.json": "30f2a559cf887b7f0e3518ac473e3d8b473ffd36d15533979c3f1a806866c4b7",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_PREPARATION_HANDOFF.md": "aa31292e6729f338965057238ada07527c71218e63a2d75f6a04d7729345696e",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_TARGETED_RETRIEVAL_TRIGGER.json": "5c75551ed5e9634dd8635e6ab2ab55ec1179c43a5f3eb4aee79a41b75a2cc1d9",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_MEASUREMENT_CHANNEL_MATRIX.json": "7b3274aa11687ad677b6315772b30114a468ffaf1bc3a053f7b5fe6bde80a141",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_UNCERTAINTY_PLAN.json": "9e8af58fdb140b495aa057b68719969b8b2de9f3105fc42216bb893079423f6e",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_PILOT_PROTOCOL.md": "8d216dd6ace48358f4e6e19c4a3cae068759b44beaec773b4a573d428c820a66",
  "outputs/execution/MP1-V002/WR1/S02/MP1_S02_DATA_SCHEMA.json": "984569590888288a0e40262ec5bd29a6d591078bdb361265a56215cc0683689e",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_HANDOFF.md": "8d459a64355316f3bf89b3fcf3550f042262ef7b9eeeafa3d50d4ec733ce60d4",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_H0B_MODEL_SPECIFICATION.md": "9f5964ecbec7df945049ae8177ca27a349d23d436242121ca1942a1e134c7e8c",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_CALIBRATION_VALIDATION_PARTITION.json": "a09fc42f2ec5c717d15dc8b0ea319ef18c6491dfc53ea310c8db6ad3f73b065b",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_OBSERVABLE_SIGNATURE_REGISTER.json": "860406d982feacd1fef5dcaba56567f60f2b2cd11d630aef9e441f67037f3847",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_FORMULATION_CROSSWALK.json": "c19cf25c6f86bdc2650971861d1b3262f65e06d6020d680f2cdad1989fe05cef",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_TARGETED_RETRIEVAL_TRIGGER.json": "03e5f32ca2549befcbeb3661a33a8f0cd6963181682e919382738a4b121b977d",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_H0B_MODEL_SPECIFICATION.json": "24ab496f36f33c85397ac412ed6e182324cb40024ce5f48b25711a8fd81818fd",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_APPLICABILITY_AND_ASSUMPTION_REGISTER.json": "da50614531b73181593e59d6245e73bca4daf45f9b96e02bb9f6019d7a8f1994",
  "outputs/execution/MP1-V002/WR1/S01/MP1_S01_EXECUTION_RECEIPT.json": "bdfadb739515c45789ceb882c1ce346a92ebe179bd2eefafea3d84bb87c040c3",
  "outputs/reports/MP1_MENTOR_RESCOPE_2026-09-29/mentor_paper_pdf_preflight.json": "a4cf559fbc5f76752d92e784807205cf43daa5d10b9b94ca714396d7097000eb",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/formatting_and_content_validation.json": "67db1547e493342e79573a2df8a9a0d0a08d35990f0fb0422f489b913269460c",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/validate_chapter2.py": "619d9fce72ae8b1ffa1a4db605b78e8d17f25ab0bbc59aec304ff65a137e264d",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py": "d82086830d47d966856159e60eda1a083a65476353c5e3842866b464fcdbfad6",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/input_manifest.json": "089f7a7aed1a574b072c67e2ee3129ba5e7f7c435a2e9c82689fde291ae69a1f",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_content_inventory.json": "75a854e7da9302f6d175604e98828fe108fe50e3ccd4d111a567042031524b81",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/finalize_phase6.py": "5c3e87219a2519ec775e026323bf5b8d36b71388f0b980e026f9c4b2140948dd",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_evidence_map.json": "f9af5a4ec807660e57c249cb44b8a5b02b2917c20002c9c5bfbbcde0e0f3badb",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/build_result.json": "320affae2ac3dcf83fd9d1b4d2a435d1220f9cfcf6ea4294d5b6ca4ce402748a",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md": "7c2154b025b7f260d3f4414c58e684e1a3e1289270be9e298a33557030025acf",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S12_fulltext.txt": "618215bb289c847446fa742a70a0cc45b0eedb49631e0f8f09beb986c644b482",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S16_crossref.json": "20ace82e1023694d7b35a43ef4b784b708d2673c9fcd380da0882c2b6fc39336",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S11_fulltext.txt": "97c9ad52bec5120741c4eead51c9deddeb060dd7a68e721a303d10265c87ca7e",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S04_fulltext.txt": "209f1d573da8c2f208b51a362fca6671222482034218f033aa79b79096eecd22",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S05a_fulltext.txt": "7f33fc83546fdb69de55884c8a3aa2aad2df9cc36a1d3f421ac0705b7ce8cfb4",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S19_crossref.json": "abb3602039e6e9619be66eabd9faf3899f4aa57ae6396f215f327c14b45c902b",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S02_fulltext.txt": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S13_fulltext.txt": "eb93a83e5572b62ed7d9d520d788846ea5ed0f7044f0304177f83ba0d52a9a79",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S20_crossref_response.txt": "ae8462e3af85ca7577aaa97ff22a194f9dfd7fada58cf4944b53d2fdfa7b1f92",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S15_web_access_receipt.json": "8286027acae782c0267ee7a3cc92496f9d68d869a9387eca41a5cc4598f54968",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S01_fulltext.txt": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S10_fulltext.txt": "3cae32fa01f7217c7cca586367cdddda95447b07ffc41ea8836f9deb9407dedd",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S07_fulltext.txt": "c82a85fb554dfe0629d549476dec708e19b85b4316c6f3587987beffc1626349",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S17_fulltext.pdf": "2bab22985b624b976248b4c26abfdb77cac2ac33e7075b644ded098f2b8790b0",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S06_fulltext.txt": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S03_fulltext.txt": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/source_provenance.json": "5f5364491d3d85571abd43420e00e908c4b33c7b8b7dc4658f7fbe2052878fe7",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/validation_receipt.json": "9358fe2a3faa2db61de92de6aa9c4dfaf8f162fa17af3f7bf4ea6e95cd1d410c",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/W02_VAHIDI_fulltext.txt": "c326bc34bac72c858eef3c29cbc2d2eb2c40fc4ee7d443af469681fbf1f59bbf",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S05b_fulltext.txt": "e3ef58b42198c013790c0148b83cc4e29d6a6ecd8d4756c979e7fe17f3640b1b",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S09_fulltext.txt": "5c9f48d840ac46b6bdc05a4e2128382adec9b5cc4e7b7e7fe838cadc561b6bba",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S18_crossref.json": "df52108ed6b7cf79a9d3221403d227f63e3fadf6b4276e603d39570eefde4dc2",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S04_Fig1_page.png": "53254ea51f83daec93ec9e1309ed5efd43d8d2fa64244d1340e3839b98f78c36",
  "outputs/reports/MP1_R_PHASE_3_2026-10-02/S17_fulltext.txt": "977df9ad8b5983811dc2e75f2b1f223ff1a3c652413a2ba2169407a19dc8d0c1",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/PRE_REMEDIATION_MP1_R_PHASE_3_PHASE_4_HANDOFF_2026-10-02.json": "740c60390f53ee34d9888c1d54f1ac69849f28f42dc4f4857ba0363d3ff741ef",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/bounded_consistency_after.json": "ace76ba40e58b3e0b4f3b9b84928f95eca981af38189349a7b7f2e56231c2b67",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/bounded_consistency_before.json": "9e62dd9fd7d4cd318c4e1c8e55f5525c65dde733fad0340f5a1a616c0ee6f9d3",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/PRE_REMEDIATION_MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md": "e1ea7a20f40bae858978f2d2b9223e3ea5ec9f9870e0b46691430100c85f88a6",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/S18_fulltext.txt": "e638b578d3315c2f2ed153955cec0596ac232a182fe7f832ddafff6f5558a23b",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/source_provenance.json": "c4eae67f306d597d13094ba923223f60aa878c0be6b1e37dbc4389c45610543e",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/validation_receipt.json": "91e4f86f12846fb216443c6e9c0cbb08fc5cc163bd886bcd4d124eedb28bed96",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/bounded_consistency_hits.txt": "d48e433b1d7d6d0b06d835ef9528d16068810d44fb2dbcae211ef743a1b629cf",
  "outputs/reports/MP1_R_PHASE_3_REMEDIATION_2026-10-02/S22_fulltext.txt": "a13660b0570ef8e39dd0c4dfd53a638b0ff9a15f0f618d5d9a42fee62cfc64cf",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json": "45d74f31bb450ea97bf235c690bf08f83cd1829fcc64a2cde5df4ca7f2d52347",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py": "ac39da773a40c472040b723bc79649c01b913b6b4b0eb53dbe4b15da0cb8b21e",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json": "d72596925b96f026fdc73f37c2fdf870f30733cce5a27e916877e3c700be4c1d",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json": "38e8809b3de36209ac614c684f57331ce6e8d38e742cfb5105a46fc11dc56120",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W09_MODEL_VALIDATION_CREDIBILITY.md": "55877a76ee13c7e91ca048266024b6cce82f279777c8f4b17a11fae28fc843f1",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W03_C5_C8_BOUNDARY_REPAIR.md": "8f7f3cc8bb0e17ee764f6b1c21490f595844d13ed9e43851b2d7ddcbf3c6df49",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md": "c09b7e4ef11bf8c2a81a7de772d72562756570e27da6fdfe4d83dca46356c729",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md": "f8e81f26be3712589459dc3a44df5a7e3165c3cfa23d80eeb2f575e6ae348f83",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W01_STATE_RECONCILIATION.md": "ee5f9046a653d98e4c63f0d79584388fa78f1fd38bf998b949759a6aa5461c09",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W04_T1_REAUDIT_CARBONI_CORRECTION.md": "ae45620d3ca45c2be4a28191d19888a6ee7c8f9273920e4040b6ad64905d03c7",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md": "72b60374e6e14ac46319dac5ed1b14b1ff6891bdc108fed19a1bb3f3ab59b772",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W11_CITATION_COVERAGE_QA.md": "49e9843196354f11b25642dc7ac3c32a0b7903280509dd67a5bfdcfe7df99839",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md": "5e7c04b76808f153507d1f9b0ae1aecc1a245a55b818908236d55d44790cb693",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W10_REEDLUNN_FANG_CONSERVATIVE_REMEDIATION.md": "c43d1c65f7f51fd84d6b8631702f15e97b69ebd61581893ee866e38f18c2709f",
  "outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md": "91cf400ae2571260b6211f41efb0032c89a72530d8b93bccad812e8ccd0083a7",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md": "ca6b2ebe771e8b73f7c042ca8028111345c6ab9d36ad31ccdf347af0e0435579",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md": "e49e7fc09e1d1fd4ab9de825699ea3cb75380b37a775acec6d79849257e9a2fc",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md": "bc6de6ceaf2e8e8683ac975f6e584389d94d5760aa18c6299226b5fb5e6d8068",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W03_C3_SMA_JAMMING_LINEAGE.md": "318b3cab0a381ff8eb560dc770ebcbdfeebf011f2f13274d929b185ff0b8e586",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/ASTRA_HANDOFF.md": "56eca52c92e778c1e7185413cd6dcd9b268af85fb9f7a82698158739c6057c41",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W05_C5_C6_C7_V001_BOUNDARY.md": "831a43fd7ee838e336fdc9da0d24026eb346990bff3612d42938cbcfd43f88df",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W01_ORIGINAL_ARCHITECTURE_AND_V001_DECISION.md": "d507ddd9bcc13797a4103ee6277a73e4e8ae41fb973acabc7821034d2f624904",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md": "9824cc6f6e99fb9d84e53bff26d5882c192ccfcdd8aef82a5d4034472b2a7842",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md": "a4164a52601fefd81f21cad53c30d183d28b1babdc7c0607721345fed80967fe",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W02_C1_C2_EVIDENCE.md": "7757a2ca1281d711b5f3e60171ffaab975296a198ad723dfabf14c7c8002f081",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md": "944921d7824e4de003f6e1661d25aedd2bc2f38ec874c9f9850de6e7484daacc",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/00_PACKET_MANIFEST.md": "58fcd5943222ad2a910bff62f2afec0cba34e7510ab5373b24472a17418bc594",
  "outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md": "174bcaebbbdfe5f3c84dea47160859ce2c1df3ecf33bf23df207714909bac53e",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/checkpoint_backup/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json": "e411aa2171c1b012aa373f3cde849ebf6890a36f3c22899205a77145c5a1792f",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/checkpoint_backup/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx": "7f64ad482f2913a0445b3a2bec99a945667eaef1516dd21d0e2d23597e8022bc",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/checkpoint_backup/MP1_R_PHASE_6_DRAFT_METRICS.json": "fb44d1e370a2d08d68dbfbef56d6cda8c44804aaa05dc71da87223ef5fec3db4",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/checkpoint_backup/generate_mp1_ch2_pre_resume.py": "37341d1f0df676e49535094775bb1bee4d353e341569bdc7c0792484744a56cf",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/checkpoint_backup/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_2026-10-02.json": "7256578c9aea3b3add01b0c9b5c865ba668c734cab5eaad623d146e9997129b0",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/conclusion-16.png": "d1b3b915dc64c7bfbd0d626bbdc9d102eb0f1eab24c8e95703ce72dfa8c10716",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-11.png": "f704f9f9c9f994b3b7976338883078873ec0ff49b5b986922bfc10bdc94b8665",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-15.png": "a2fecf85ebbb70ace4166f8079f7eb107233dda182124d5107f4020c967a768b",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-14.png": "a3c551470589b025e00f4d22008c16427d64fd0a40ba8822fb637768ad85285e",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-17.png": "dc7c0eee349e9e14416313af277dc7887391a476c41962bfd8b033cfa201ea50",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-09.png": "ef775615c7fd5c8fa7521801c069e192322d12b127c553aa5ccedad65311bb3a",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-03.png": "9910f9ca9801c4fa182d953c0518ef5ffcaa8e318b3bb20e7add9cb4c49229a6",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-18.png": "641c62a8cb8274ffe2983c91f1f8ff6a6f535f4e82d050a994f060a34300ddb2",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/chapter2_rendered.txt": "8bfbb4c13c7d50a145110462389317a681a25410a608e5c22d7ef46c1f4e5f69",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/contact_sheet_1.png": "8033b911cbe9c9a0090fd19611006cf707db5a452a8dba8ca20ff8ca549150a3",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-07.png": "6f775086aa66696bd6df7af72126de4fe821e40aab8ef80ca45f659cfb4c359e",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-01.png": "e014771b04859727b1e1747a14ee10c3b92524f9b8062c7c51aa1f767e12f6cb",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-03.png": "9910f9ca9801c4fa182d953c0518ef5ffcaa8e318b3bb20e7add9cb4c49229a6",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-16.png": "76b6f07910a1ed43e0ef2e87047edd48318c463ecd16c83f1e632bb4bb02b980",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-01.png": "1e2917928b44607a242b1528540d5bbaeaf0538efa42ecd565d3b2a9d33cd8ae",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-02.png": "f3c2163c7ecf0b5fa24e86f64393ebe8a440e0cd9526f3ba2c5f46e9cd9ad943",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-15.png": "6c32a5204570d0a893e475a1fe26e2fc25296b0c9c8eced3d682568016b86938",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-06.png": "86c97b2ef84ee9f407c6213558d92575562a57909d1b69d0c29d94203061b37a",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-17.png": "331366029aef0bb3fd75c974006fb8f7d37c2eb192469843c15e82e88a92e119",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-13.png": "14ab4418ba90d89c66b6b1b046308639339b7be759a317afd9b049cb60130732",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-10.png": "b24e8addf492505affabdda89cadb76f8bbdf2c27143375441bfdde6b1791461",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-11.png": "2c4a34771dd64b0732764b792029b8072eb50c75051fcb5b5ec69f1ce4eeec15",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-16.png": "88589afb4a6fbce035d12bea3cf12ea5b880e37efdbf1636523a912e48a018b7",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final_contact_sheet_4.png": "1dfb453fd5c8d46150e2beeed67cb48c1e7a66ed67fa8abffa8d8cee2bfd7929",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-04.png": "c8872b9eb42f70782e024102e3bea4e3a94662b70f9f66a97012a52f7fbf9aac",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-19.png": "574f5f189be717625050efd3bff24b133253a84c038c59c8c7f0f0931b40018f",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-09.png": "34345ec34f60570de5651bb6d011b0cb404b281d7cbf620af358889e07b86a2a",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-13.png": "bcede93f70bc54009f7ca1b18b22e3b278ce485ec0747683b1d831b7c9748d71",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-08.png": "9d2477abb6a40fb05a3295a09e44ce658959074356b39105f3ed1e05dec67c62",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-equation-04.png": "724f932d005f586229fbb7081df6a6844c6f23511e8d9a5de9778b79bc0942ac",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/contact_sheet_3.png": "cb05e15b9f818d767713a432513ed87c984499e4d018daa776a310d9a37c6c15",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/equation-04.png": "2958ab88a286338a47375f8f8ae299a0aa3c03da01313aa31b7bcd60617a7ca5",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/render.log": "4fcb5a95f97cb1d132f6a8fb10e44598ac9d17a9765463dde6b68d6b2170a9a7",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-02.png": "f3c2163c7ecf0b5fa24e86f64393ebe8a440e0cd9526f3ba2c5f46e9cd9ad943",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final_contact_sheet_3.png": "3d3ea83a0e090fe6e33a8a38bfda8645a0faeff7ce057b73c413ae982d309026",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final_contact_sheet_1.png": "692fa5c831f6d76e39341c177acf384b65ccb1d46495622ce14acd3b9cd0628c",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-12.png": "253eca49599f8846251543b5d8cabb18cf10f147313ae8948f12e32863802a7c",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-12.png": "d8d2a15219d0ead5a05a06f0ecca4dbae650373b26938ba8f9d6a6af4d15b8ba",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-14.png": "8e4e09225921b0f8e850ec6ecee45caf621a42157eeb200605d034e88af94666",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final_contact_sheet_2.png": "d1b413169c1fba62e6ad995630ea85605edc23aae3f362630fb20649dcf0b89e",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-18.png": "f1848ed1aba5fa43f17295c4dffaab598a86db8f17b215c1dbb5fd0ea67f16c1",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-06.png": "27135bb8f288a8741deb8cc3bb9f7573e6df51f079f0f507dc8fb5ef97c44570",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/conclusion-15.png": "b7c8ab8e6b087e1c068de9d2df7e5bc30134ff11fd379df95e96ac71cfb610d1",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-04.png": "a859cbc7cad33e2a1da7c44d83f18d299f57857aa3040bd8be00c816b302ee43",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-08.png": "9d2477abb6a40fb05a3295a09e44ce658959074356b39105f3ed1e05dec67c62",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-10.png": "3f9ec8de684bfa2c7e891724bfd3b66f613445449ff80945861d06a081fecd86",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-07.png": "e1f716299ab082f5b6d038256c2fcf1a9a63bcf2ac151f7e9a57cfc58e3c2ea6",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/page-05.png": "7a2bc14ed391d5d703e7e31e0532173fe606b57984fd3cff9ec22aaef1535373",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/final-page-05.png": "7a2bc14ed391d5d703e7e31e0532173fe606b57984fd3cff9ec22aaef1535373",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/contact_sheet_2.png": "27cdb505c10c4ea77f42d9a06978d0efe98aeb9ed667805f6b9e631a3b71c9aa",
  "outputs/reports/MP1_R_PHASE_6_2026-10-02/render/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.pdf": "a9532a09b1d199cd72026a7c6a130dff9a6002d2285ab09da2493a9411f10a29",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json": "c93b664692e0e539895548d87e7ac1d50689eb09654841c89f45bb5b2d0fde7c",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json": "2058beabf11fbafc397818f2bc533cd6b70d4ca8fc94a9e57630b8845b2c34a9",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json": "d88f96fd0dc2781302fc91ecdd5575c4609ee1f002bbf1c65b44d7be43a7af0f",
  "outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json": "96fd249c10471dd90ed45041388c8700ff583a777a8307c6fd6dc9bba9f6e31b",
  "outputs/search_results/D1-V002/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
  "outputs/final_direction_lock/runs/20260925T094047Z/output_schema.json": "c048053d31b17ec6362948e66f969c1fcb4b88d5562bcdf28e9d2cb3c6c5e16c",
  "outputs/final_direction_lock/runs/20260925T094047Z/source_manifest.json": "4e07c0bde26bd5ed70650a07883ef7ea228c93e643e6030c1a17a3df26c716b1",
  "outputs/final_direction_lock/runs/20260925T094047Z/prompt.txt": "87a7e476e6f1c3076ab7eab86e3a79fa48e30d54bdf70976bdc0e71bf566cffd",
  "outputs/final_direction_lock/runs/20260925T094054Z/output_schema.json": "c048053d31b17ec6362948e66f969c1fcb4b88d5562bcdf28e9d2cb3c6c5e16c",
  "outputs/final_direction_lock/runs/20260925T094054Z/source_manifest.json": "953ce88f4714872e02bd8a4f768bf6f1b6f8ec8ac4b37a4ecb2a5f4ec8b56a8b",
  "outputs/final_direction_lock/runs/20260925T094054Z/FINAL_DIRECTION_ADJUDICATION.json": "67d9b268ae0ca245ec09c9fb60852da33a581beab701a7e653483a606fe899e1",
  "outputs/final_direction_lock/runs/20260925T094054Z/FINAL_DIRECTION_ADJUDICATION.md": "d520a057d712753f255d503cc7b2353323d3adc14cd2cc8219bf1d919bae808a",
  "outputs/final_direction_lock/runs/20260925T094054Z/prompt.txt": "87a7e476e6f1c3076ab7eab86e3a79fa48e30d54bdf70976bdc0e71bf566cffd",
  "outputs/final_direction_lock/runs/20260925T094054Z/raw_model_output.json": "9271ecdbf3f56791b2a646b7fd684891feee05ce4f6639c1f4d1a6236efe5408",
  "prompts/MP1-V002/MP1_E1_W2_09_ASTRA_HIGH_RED_TEAM_PROMPT.md": "9a68e69060b0e6801ef0bca2dca51ecf9b321baaceb841794a08d247edfb52c7",
  "data/evidence/2016-Friction Characteristics of CFRP Plates in Contact with_79d1adc34c.json": "c0a7e4971f7a1d2a30e2560714fdc77aeb0295bdd4facad2fa7cb7a9af16029f",
  "data/evidence/1993-BENDING STRESS ENHANCEMENT IN MATERIALS_66fcf766cb.json": "e2af2f3a9e2f3a1c89ad47c80f760c8dfca57784e2bc276dfc28a89c40a7e64c",
  "data/evidence/TRIGGER_A_Lightweight_Universal_Jamming_Gripper_fo_64a83322f3.json": "a3b6c02bb14523e2cddd889368d0f26ac78ee2fca11d2b894764b5a292d45100",
  "data/evidence/2016-INFLUENCE OF SLIP EFFECT ON BENDING CHARACTERISTICS OF FRICTIONAL LAMINATED BEAMS_47fe4949dc.json": "d250c578907b579d9c9facf215c2170de793dcade9ce289965a89fda9656d447",
  "data/evidence/2008-Composite beam–columns with interlayer slip—Approximate analysis_d87b4ad44d.json": "36e630e0cfd7b179f05f53c35a615210f1eb9cfc5c30f07c0b8beda77361e446",
  "data/evidence/2026-The global-local mechanical behaviors of multilayered structure and_ca46dc062d.json": "850139a1a6dcc0c34d2c8c9aff56d3c4881121b929e015435f7bc2a87d7cbad3",
  "data/evidence/2018-Bending Stiffness of Parallel Wire Cables_9c2773e4cd.json": "f21c105eb3e96d0f93ec936e0881019c699d04ec0c400d23e435ed7c88799153",
  "data/evidence/2022-A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes_a300a3b714.json": "f70e5e1c24828e03650bc444f4562ba32cc54d5459c2054cd8fb159a100c1b7a",
  "data/evidence/2024-Modeling of Stick-Slip Contact Mechanics Based on Improved Continuous-Scale Fractal-Discrete Iwan Model_8daa38176d.json": "2e2f7d31236896bd11bcc04933e0318f869608af344abaff85963fb0a045e1cf",
  "data/evidence/2021-Experimental validation of the applicability of effective spring boundary conditions for modelling damaged interfaces in laminate structures_444793969c.json": "202cfbfc61d6c36d3fbac3f48c37e8734e3bc7b0cefaa2670b4a946988db3afd",
  "data/evidence/2021_Bio-Inspired Soft Grippers Based on Impactive Gripping_e66f8bda11.json": "31f57f68f88ae689fb8100812d0f14ed26bc1dfd7cfebe60cdc0de3a2960909d",
  "data/evidence/2023-A Single-Variable Zigzag Approach to Model Imperfect Interfaces in Layered Beams_a9cd14eca9.json": "b8886c67e49886b7c8e406bf32445091ad918a9e28957aad9c9eefb001f99325",
  "data/evidence/2019-Mechanism research of slip effect between frictional laminated beams_ee464a718b.json": "c595d03f5651b384c078b59a76c26c7e344c755e40280ca8c8bb8e993ab81e7e",
  "data/evidence/2018-A_Soft_Robotic_Gripper_With_Gecko-Inspired_Adhesive_dfe07593dc.json": "15a5a24d25c3504114a6ff98ce6293b46302dcf72fba9f4d60ecbc9442f2ae3e",
  "data/evidence/2020_Soft Humanoid Hands with Large Grasping Force Enable by flexible Hybrid Pneumatic Actuators_2404868fbc.json": "f452557f681e85f6b84c8451181f5a60cd231fde65d7e126818fffdcf8e07f9a",
  "data/evidence/2019-Long Shape Memory Alloy Tendonbased Soft Robotic Actuators and Implementation as a soft Gripper_4dac06062a.json": "4c2d74965ca7c7a86f34c358db3e2745d1a795e0fd2f327bcfff6756c7f4173e",
  "data/evidence/frontiers-Soft Manipulators and Grippers- A Review-2016_877d9ba31a.json": "e3f56ba7cf5779d98072c57aa367dcb3b5f2c49a937aeabc06aa301d55a99618",
  "data/evidence/2007-Exact static analysis of partially composite beams and beam-columns_eeb0863c0d.json": "33c63f0d7a9bbb0dc13933fdc8410bd7fb4a7d8289e5e273849f14aa611fb4df",
  "data/evidence/2018-Soft Robotics Gripper_ccc528bd6a.json": "0539b2d0b4928d94e5f049b12083e6b898f01d88096867527c38b44d73094ae9",
  "data/evidence/2026-A novel frictional contact correction transfer matrix method for bolted vibration systems_20cee2210a.json": "bf53944f8e7314af0e8d48b0388c29afeae58699e517c553a2f8eb5800a8e9ed",
  "data/evidence/2018-Mechanically Versatile Soft Machines through Laminar_5f7ccd7357.json": "a6c10b9b89385a9e2cbfb71cb3da1ec60053bea0aca78b6687b1251536b32151",
  "data/evidence/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/evidence/2009-A simplified analysis method for composite beams with interlayer slip_aa091ea74d.json": "89a80a5767282ae6c81d7caff746c6b59a3a06a1e08482c93ff8fcad061758a4",
  "data/evidence/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/evidence/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/evidence/2022-IEEE Optimizing_Out-of-Plane_Stiffness_for_Soft_Grippers_e6deb76ed3.json": "e9a2e36da74265fc33b271aeec986dcbaec66f155c8c622b9789031dd2547f3c",
  "data/evidence/2018-Variable_Stiffness_Robotic_Hand_for_Stable_Grasp_and_Flexible_Handling_2938670820.json": "e0522561949afb5dbccc29a2d36e06b04525d57ba77f383eeddd007e3dd56d7f",
  "data/evidence/2025-Slip-mediated axisymmetric bending of multilayered structures with_bdeedc2731.json": "82fb5f6991b41fd9ad67c047ccd42e585635210dd43fb6f3e9feddba23263c9f",
  "data/evidence/2024-IEEE-Design_and_Implementation_of_a_Magnetic_Coupling_Based_Segmented_Bend_Angle_Sensor_for_a_Soft_Robotic_Gripper_fe95a2f245.json": "9a887743e037ea2aadd15632661706d078ede3088e6a8aef11d785eed4ecbe1e",
  "data/evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/evidence/2025-Flexible N-layer composite beam-column elements with interlayer partial interaction imperfectio_8a4d5de33a.json": "258a001ad36e45e14ec03af8e641d3dde056049d34aab8f74ae5c49c9d5665d5",
  "data/evidence/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json": "a7001486bea663c834ad1089ede1000d0d58db8f301fa6149acbf667e622f570",
  "data/evidence/Soft_robotics_gripper_technology_in_medical_surger_ca52258155.json": "f4491a28394c65c27028993dc934495fcf2ea4609dd8e40662d1f27a56fb9b6a",
  "data/evidence/1998-A rational model for the degree of interaction in composite beams with flexible shear connector_a28d4f1668.json": "bc8e7b22df22f75f450517649b782a8bb76a78ddade94ef57226f0978cab990c",
  "data/evidence/Mech Cohesive Frict Material - 1999 - Adhikary - Modelling the large deformation_d75a3e82bc.json": "c95d5c7de50a1368564efc847fffa5e634fe011f18583065cf2b385f86241678",
  "data/evidence/2022-Equivalent dynamic model of multilayered structures with imperfect interfaces_0f1b512cee.json": "8ff3061d5616e0ba03f694956e560e441de62eecbaac9625382ac6e9aae0f912",
  "data/evidence/2014-Assessment and correction of theories for multilayered_33ea203427.json": "78064b09e13df6f534afcf7e106a95d57f09fd9f7263f38458dd3b99e5afc341",
  "data/evidence/2026-A coupled electromagnetic-mechanical model for high temperature_6bdb4151e2.json": "c97535539589b4b6ecac0aa967dc8e07fe00dd2cc10ab65ff6a9960d184efb77",
  "data/evidence/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation_652e62758f.json": "8aed18b4290ba7b4ca9fd3da1e4958cca921aae2f6ea93de5652ad7f3149b01d",
  "data/evidence/2025-Theoretical, experimental, and numerical simulation studies on interface slip in steel-concrete_fb057ab3b2.json": "2abab9bf794d3746678699fb66dc2daa7fa5bd2ad56da3ee0f62b3a7613dfe85",
  "data/evidence/2022-A_Dexterous_Soft_Robotic_Hand_for_Delicate_In-Hand_Manipulation_f6a95d9bb0.json": "e830bd49956b17716021532a60ea9c65081fc3fedd051558fb9b68f151c6fa83",
  "data/evidence/2018-Modeling of grasping force for a soft robotic gripper with variable stiffness_e3ce477955.json": "d5bc9281712a0f7232efd07d0e969fe9437a0ea629ede83d23b2b04159279402",
  "data/evidence/Design_and_Experimental_Validation_of_a_Soft_Shape_95d531dfcd.json": "6db6474916432cee11631ff236e2b106005c34ccf548457e9996a0e4ce318543",
  "data/evidence/2008-Locking problems in the partial interaction analysis of multi-layered_2ad029e62c.json": "e059db178d6db6559a244b084eb1d2fc273a2982ee5051edbc78f118aaac7f7c",
  "data/evidence/2006-Time analysis of composite beams with partial interaction using available modelling techniques A comparative study_a577a30ffd.json": "4015c9dddea2b4b318b0c9023e4b69109b0ead12a083a0887bf2f76f85f5a601",
  "data/evidence/2010-Analytical and numerical analysis of multilayered beams with interlayer slip_14958e37b2.json": "f66547e1ce4ac7e3e800c2ec35599c8f3cbcf99e56b344662633017db6f4d4f4",
  "data/evidence/2018-Soft actuator with stiffness and shape modulation Using 3D-printed Conductive Polylactic Acid Material_6a92ae2d88.json": "db489cd8dbd14fd1d7aba2e67db723aafc9a14bf4ca127b809cd25aaf13f829e",
  "data/evidence/2015-Transition from stick to slip in Hertzian contact with_ac9973e89e.json": "7b18bcb0e5bf25b218744ab961cad31ad2f38ddc6e2c8be5c01fe2196466a842",
  "data/evidence/2022-Snake_Robot_Gripper_Module_for_Search_and_Rescue_in_Narrow_Spaces_fa47e75f9a.json": "290ee8c09cbee5a28742228992c79f2b630a8dee523346827fcc637eafef2a81",
  "data/evidence/2026-A global-local homogenization model for hierarchical chiral_1502d9c1c6.json": "0ad9c9f8d66b788153d13909dc0bcd328a72ac09d0723e9201e2b69b55cfa958",
  "data/evidence/2013-Exact finite elements for multilayered composite beam-columns with partial interaction_c9bf5cb21f.json": "54171298cabad8b0898711aaedcf12400accc9e8f0db7a9f8369c20134e8d90a",
  "data/evidence/2024-Messina-A_novel_friction_model_for_steel-polymer_interfaces_13e407003a.json": "c19d9d3629f955565021fc5bba829be560a4d46b98c4cda5318058d72d9a5928",
  "data/evidence/2026-Critical state model for superconductivity features and_a32f8501d6.json": "79fd6d829d76951b27740e34a882dc824a845f4f18020fa67bea29e2c4eaccd9",
  "data/evidence/2026-Stick-slip friction model for soft-hard joints under preload degradation_02d3360815.json": "6b243d846091c460ff42a7835cb2539e42c61d3d37bccc0ea034bcae513d8dd2",
  "data/evidence/A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics_f5f31ef249.json": "b7b470c8626ffdf66cc15187e8f88d91a0cf57bd59a6689187736422f5effefa",
  "data/evidence/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/evidence/1990-The deformation of composite beams with discrete flexible connection_99721ae369.json": "8e54b44d9b0889d77dcd362d634538311b4c41beec2365c752c82e409b5936ce",
  "data/evidence/1998-A relative gradient theory for layered materials_2f85ad579a.json": "8bf550f4b60deef8df9acd0035ca43b17ee28b283d8e3c97eef157c554e86dce",
  "data/evidence/Stiffness-Tuneable Segment for Continuum Soft Robots_7366c065fa.json": "a5958b4859f1aa314a0fac2b571012e5b9fa96a77c22c46ca1c0da003ab5cecc",
  "data/evidence/Design_and_Analysis_of_a_Novel_Tri-layer_Granular__b19f76572d.json": "ac5e28f3242b3b72a71483062cf3dc29ba48d065e5e5f9f0b3e152f6fbb7fa71",
  "data/evidence/1974-The dependence of shear lag on partial interaction in composite beams_8a6d33e527.json": "0b6126f54086b40d089a4dfc0589f5b49abff50809c3037c888920a37c6aba12",
  "data/evidence/2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology_cb423f09c9.json": "caee18369d4f6ee95373a78634dc059288f9a8d1d9d8d1ad4c58a0d1ef17d97c",
  "data/evidence/2023-IEEE A_Novel_Variable_Stiffness_and_Tunable_Bending_Shape_Soft_Robotic_Finger_Based_on_Thermoresponsive_Polymers_7eddb5d92e.json": "4a05a6c30b40ed1f214fe0f24cae52c316ae38b0349566d71bed90ddf8ae4cb6",
  "data/evidence/2017-Soft_Robotic_Grippers_Based_on_Particle_Transmission_75ecb1291a.json": "637075d87a13b6c9b3b5dc244ea031c65955fee369f7ae37d218086771d9ddd7",
  "data/evidence/2023-IEEE Highly_Shape-Adaptable_Honeycomb_Gripper_Using_Orthotropic_Surface_Tension_12e15c130a.json": "40732e1ef19bae39c2f4adcd49eb2e128c6e27b387aeffb85e47bdc3f4d6b421",
  "data/evidence/2023-Adv Materials Technologies-A 3D Printing‐Enabled Artificially Innervated Smart Soft Gripper with Variable_a1a03d9a89.json": "6b6be1775c6066edc6ed00244b8772e83f0edb7f7f6922505de1b1fe95651864",
  "data/evidence/2025-Fretting wear modeling of bolted joint interface with microscopic roughness usin_7b85aadc84.json": "588567280e85e964c2fb7330d6d51af0ab051a6e35c5a444539a6494bcbcb0f3",
  "data/evidence/1993-Bending stress enhancement-Part II-Unlayered shear-weak model_f00d886124.json": "8fb9b5c0a76229c1dc20a212deab6fd33b845089a451fa0190c2561a03d0bdc3",
  "data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json": "fb60cab5e885476b334d5c18d08c6b3f8fe81ec07f692f0cbb9f4e1b320b7ecb",
  "data/evidence/Analysis_of_Contact_Force_and_Shape_Change_on_Gras_3a6c7298b6.json": "01bb391f507f640c7f95deef959a8c463a31a393c4be94f123664afa9803eff8",
  "data/evidence/Adv Materials Technologies - 2020 - Chen - Smart Soft Actuators and Grippers Enabled by Self‐Powered Tribo‐Skins_0003e35369.json": "3a2ac6fb9641b89477998df72c6188308b97ff17a0df1734f6c049f81289c419",
  "data/evidence/2022-IEEE-Tendon-Driven_Soft_Robotic_Gripper_for_Blackberry_Harvesting_d3382c226e.json": "d7390b736b629a5b2238dcabe98ae8a5286f710f4383b788c78eae2f86edd59a",
  "data/evidence/2020-Novel dynamic model for calculating the equivalent Young’s_2d30a68b71.json": "aaa0ec55e60b62fe188429be38948cd79b865292743237858d784097a22c928b",
  "data/evidence/2021-A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure_afe2a3a310.json": "5ff2b58b0763a999244a3f169575d083d976a370cd0b7155f68151338e889ad3",
  "data/evidence/2017-yang Novel variable-Stiffness Robotic Fingers with Built-In Position Feedback_96aec3bae3.json": "fbd1a6441e5428ccd3ac4cfbf2f3fd8a492c7ab92104167100e17e6b5e24c8db",
  "data/evidence/2007-Analytical Solution of Two-Layer Beam Taking into account Interlayer Slip and Shear Deformation_f5bba53ef2.json": "4889d5cb1eae40b22fff31478c03c69f68c52a826e6ed626eed0a56f72652520",
  "data/evidence/2023-IEEE Underactuated_Robotic_Gripper_With_Fiber-Optic_Force_Sensing_Tendons_d6e4cf1d14.json": "8ebe9cbe5d5fa370eb8522627cc49d9559a898d9d9d97c59294df4f3478096f5",
  "data/evidence/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/evidence/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/evidence/2017_wang-SMA based Soft Gripper with VS for compliant and Effective Gasping _4bf6ae90e0.json": "deab12e611172894daa2cdf47dff3b91ef1dbcb9eae8330c46fd6f9d8d893f86",
  "data/evidence/An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints_ac542457be.json": "c173f203d9b1df80e53259d1ad9088749dda4d2ca08fe61c02dbdd476eeb5de0",
  "data/evidence/Design_and_Automatic_Fabrication_of_Novel_Bio-Inspired_Soft_Smart_Robotic_Hands_182f1c9f23.json": "16ab383ec36eb3749e11b5da0e65a08143d2c8b49eea6fa52abdbb34625f718c",
  "data/evidence/universal_gripper_ece56d39a8.json": "021183d1c12c4141485e214078badb4d4fe9248450d3c44c43fcddcdbb008a02",
  "data/evidence/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/evidence/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/evidence/2021-Analytical model for the bending of parallel wire cables considering interactions among wires__ecdac261_ecdac26196.json": "9ac62e7fbad2d4efd4954a04c38bdd79bf361cbd8abb4546e27c3389f20d847c",
  "data/evidence/Soft robotic grippers A review on technologies, materials, and applications _fdd30f539d.json": "1377f4a6cb708d582c94fc21eefe5876583e5a7d21b6a708992dc5e9a6500dd0",
  "data/evidence/2023-Modelling tangential friction considering contact pressure distribution of rough surfaces_8ce1db3bca.json": "4a08eee6e3ec5bfa4586674ce82b447c7aa05ff5678350d4678bd200440a660f",
  "data/evidence/2022-A barrier method for frictional contact on embedded interfaces_202fd05d8f.json": "bee1f2e34e22c631767fde5777508b104b0d39e44fa35b8c637a1fed1b48b6ab",
  "data/evidence/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/evidence/2021-Soft robotic fabric gripper with gecko adhesion and variable stiffness_4eab68eb44.json": "c98c1a59702fb75557b5f0ab86e799fa259880a98b90b6bfe81d349fd15b918c",
  "data/evidence/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/evidence/2024-Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots_56d058a34a.json": "c3428181750de55758b3e30a5b68662085e5965af367daf605cfbe56f3ac2c30",
  "data/evidence/2023-IEEE Optimal_Design_of_a_Highly_Self-Adaptive_Gripper_with_Multi-Phalange_Compliant_Fingers_for_Grasping_Irregularly_Shaped_Objects_79059ca07c.json": "5cbcba7524c0552b012e28a81b666b88e26bd0d885a6fdf978f5d12ad26dee72",
  "data/evidence/2023-IEEE TIE-A Soft Variable Stiffness Hand With an integrated actuating cooling system_db0ccb7d74.json": "8595fd1fef5fe6d6ac1d523bec355c2de4ad2875605707dd3231446b8fcd1747",
  "data/evidence/2018-A homogenized structural model for shear deformable composites_8113666e96.json": "80f317b05d2aee6447acc0c1ac7a40e8b06770b765f2080d7553f1ce21903f3a",
  "data/evidence/Stiffness Change for Reconfiguration of_dc9ad29f75.json": "a8d142838d775476ae323435d7d213fdcd57bea98f7cb54d43aa6a50127e1827",
  "data/evidence/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/evidence/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/evidence/2023-IEEE RAL Design_Modeling_and_Experiments_of_a_Variable_Stiffness_Soft_Robotic_Glove_for_Stroke_Patients_With_Clenched_Fist_Deformity_dbe0e69179.json": "7384841ea0f28030a488662e715deb04997e61bd9ddee136791912364e0e385e",
  "data/evidence/2026-Chen-Design Characteristics of Continuum Robots Based on TSA Variable Stiffness Method_6723402e32.json": "86762d2c2b691a877f2e9c70c53614f102c5c0d8dd615af3d3f9f77fa2c39934",
  "data/evidence/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/evidence/2024-IEEE-A_Human_Finger-Inspired_Shape-Locking_Pneumatic_Gripper_Enabled_by_Folding_Laminar_Jamming_Structure_5bdf50c599.json": "b75dc8adde0b8d319ec708b4ae4a32f748f4bf2cd0ae2dee5d3d990353cc7ae1",
  "data/evidence/2022-A_Soft_Robot_With_Variable_Stiffness_Multidirectional_Grasping_Based_on_a_Folded_Plate_Mechanism_and_Particle_Jamming_9036ba0b60.json": "0f8457724567d3dbfc34604450f1c9655304ef0108acbf030d79c2f6a88dffd8",
  "data/evidence/A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation_6583ae5919.json": "1d911ad4b024f1d1d5f09efffc2a9ab9921e0d1b6d86819cc021eedaec5546d3",
  "data/evidence/2023-IEEE A_Palm-Shape_Variable-Stiffness_Gripper_Based_on_3D-Printed_Fabric_Jamming_39520ca4cd.json": "069f3af53aeac5cb0b8596ed479a784c3a98da4a3714cbd66ae7cb27d64546d1",
  "data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/evidence/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/evidence/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/evidence/2014-The existence of a critical length scale in regularised friction_7c3aac183e.json": "dabcbd09f5caeec4b75fc8fd206391e923427f1300b644c8fad0cc1200565d03",
  "data/evidence/Universal_Jamming_Gripper_Experimental_Analysis_on_f17bc7cbcc.json": "a10a9cdc272963bc34fed7c0d7e5c6ba3a7d9d57a140c9a722654e0d5fc89bfd",
  "data/evidence/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/evidence/2023-IEEE Single-Motor_Robotic_Gripper_With_Three_Functional_Modes_for_Grasping_in_Confined_Spaces_6f076ab4d4.json": "98b350bbbc464dc07b2950b6a6edfc22c1184647b06ab75eab18014608c773de",
  "data/evidence/2018-A_Variable_Stiffness_Robotic_Gripper_Based_on_Structure-Controlled_Principle (1)_5aedfd2730.json": "22c42d03dad3d91cd982f39b7799221187dade1230b91acc3d395c45e7fa99e6",
  "data/evidence/2021-Analytical model for the bending of parallel wire cables considering interactions among wires_c4531c66c9.json": "b842ee30907e9d7dd2e84a0f02aaa6e9383e36eab330ac1813f9057000646902",
  "data/evidence/Soft Robotics for Chemists_de5329b2fb.json": "961bc863580e0f6a4c493397f0da9ea5d24994d73926b181306c32a372b08034",
  "data/evidence/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/evidence/2020-A novel design of SMA based soft robotic gripper with variable stiffness_4c30fda873.json": "a49a98431f72ad926f4d2521a82c9bc37937a7b90c1d5781b9e8e4e31176d8e6",
  "data/evidence/2024-An analytic solution for bending of multilayered structures with_bd5af3e26d.json": "dc064e4a87c197d883b4589bd9587ec0b0a2838dd8145b0b3466426afe2559ad",
  "data/evidence/2024-Ye-Analytical Solution for Bending Deformation of Steel-Concrete Composite Beams Considering Nonlinear Interfacial Slip_53d328abaa.json": "0d58585a7d09e29196ed8d7a6582a57beef37032432240a513baeaad015b516d",
  "data/evidence/Influence of boundary conditions on the response of_4994f7ed3f.json": "1abad0bfc95d724c3ccdab6d53f01ec9bbb771b438cf2edbf7d0afb3486e5128",
  "data/evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/evidence/2016-Derivation of the exact stiffness matrix of shear-deformable multi-layered beam element in partial interaction_bdf95f0602.json": "964cf59ff0f6c54662ed8242803711079e12e3068632be09ac5a07ab3d34cca0",
  "data/evidence/2026-Laminated Partially-Composite Plate Theory_71c8d5e2c7.json": "1543d55fb14822ade8cbb4063fe58134e7e39098ca2dfc7e8113c0beb84593c0",
  "data/evidence/A Novel Model for Layer Jamming-based Continuum Robots_b573b2ab6b.json": "87c6298f12ed504ac84571b0bce91e2259451b599ebe6b49e6c4fffbc046ab5f",
  "data/evidence/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/evidence/2013-Analysis of Composite Beams with Incomplete Interaction I_f8e8c7b1a4.json": "93383a73f953862ae089b9da7c56b87f29d5995bc767dec22338ed85b166e9c5",
  "data/evidence/2024-A_Novel_Hybrid_Variable_Stiffness_Mechanism_Synergistic_Integration_of_Layer_Jamming_and_Shape_Memory_Polymer_f28f2201b8.json": "4c9bba7cc9decd992df39b7d2c1321d7b5c36ad7bdd61d45f72a22550f92a088",
  "data/evidence/2002-Steel and concrete composite beams with flexible_d0699583ac.json": "2eff6465480631264ee5e68ea44642cf4c11d6ef625f671c574c59f0bad973a9",
  "data/evidence/Decoupling_Control_of_a_Multi-Segment_Hybrid-Actuated_Soft_Origami_Continuum_Robot_Through_Variable_Stiffness_8d3b7d72a6.json": "7c62494edbeff66a4148234bb1d46be5b3e22d4a7571e060c958a25e3cbd372e",
  "data/evidence/2022-IEEE Modeling_of_Fluidic_Prestressed_Composite_Actuators_With_Application_to_Soft_Robotic_Grippers_b62675b62a.json": "5a81d9b1d4bc9a68ae39d79a4255f4f6433b786a560881e7d3ee3adeb34d5c78",
  "data/evidence/2021-flexible seft-power multifunctional sensor for stiffness-tunable soft robotic gripper by multimaterial 3D printing_3317077510.json": "2e92de5c3da620588f786300c177ec90777331a168a4fa215af16ad0d4688ca7",
  "data/evidence/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/evidence/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/evidence/Winandetal2026JournalofAdhesion_923285b103.json": "2a56349071fb1be37592a2aabb3ba77b20b74231649d64bb607a1481434a6887",
  "data/evidence/2022-IEEE Soft_Exoskeleton_With_Fully_Actuated_Thumb_Movements_for_Grasping_Assistance_57f85eb161.json": "d90dc009ae8800a857db8c2bdaf40ae52a1cdad22290a393e3a5667dd7beb732",
  "data/evidence/2025-Analysis and modeling of nonlinear_1337634c62.json": "7d0b2837a7b61f9233fb603974a29f62e1a6d541486c7645c9145f6fda491b1c",
  "data/evidence/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/evidence/2026-Thickness Gradient Design Enhances Bending Performance of_7f93ab3253.json": "5c4e4bfd13aff9568ebc3476ad3cca2d4654e2af1b650151165fa2727f3f3747",
  "data/evidence/2022-IEEE Elongatable_Gripper_Fingers_With_Integrated_Stretchable_Tactile_Sensors_for_Underactuated_Grasping_and_Dexterous_Manipulation_a2fce8b2df.json": "57c687ab6bc0ff79c28bd433bc26e25c4cc0fd437fcfdd8d129395481b89bf24",
  "data/evidence/2023-Advanced Intelligent Systems - Wang - A Bioinspired Gripper with Sequential Motion and Mutable Posture Enabled by_a1917fa859.json": "91de003c1bb4b03971112bd4a8793a91b3ffad002e349630c359a9c2fe39221c",
  "data/evidence/2022-IEEE A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology_26fb5818d6.json": "6c9bd4a29aa7ebc1de223a245fdabab4ebe9e72f75b1cec19601769dcb51b5fe",
  "data/evidence/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming_1f05cf83bc.json": "c5a1863adc8ea5df1bdd4d36eb8f62a037b6967e975f434d3b7efd3666071005",
  "data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/evidence/Design_of_Telescopic_Soft_Gripper_for_Mangosteen_H_7a12d36a65.json": "4fd458f0028daf1f31f43f08c8531fe836371e3bfa18c674ef8bfa511b1ea726",
  "data/evidence/2019-Flexible Fingers Based on Shape Memory Alloy Actuated Modules_63719eca8e.json": "1fa381de81298c79573bb46637a38b6d2df9a797024f2b0024359d5a8cfff10e",
  "data/evidence/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/evidence/2024-A_Soft_Finger_With_Tensile_Variable_Stiffness_Based_on_the_Cross-Sliding_Jamming_Mechanism_269d15b830.json": "4cad56d51a2248a4381cdfe8710eebb0b10a220473504467316722dfebd31af1",
  "data/evidence/2025-Toward a deeper understanding of layer jamming structures_7cb387b88d.json": "8197883e287ecaf45815a9b4db7654647155a42e3d7304507d232911d269acb1",
  "data/important_paper/2025-Zhang-Continuum modeling for layer jamming structures.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/important_paper/2025-Zhang-A continuum-based model for a layer jamming beam.pdf": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
  "data/important_paper/2025-Zhang-Toward-a-deeper-understanding-of-layer-jamming-structures.pdf": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
  "data/important_paper/2025-Zhang-Continuum modeling for layer jamming structures.pdf": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
  "data/important_paper/2025-Zhang-A continuum-based model for a layer jamming beam.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/important_paper/2025-Zhang-Toward-a-deeper-understanding-of-layer-jamming-structures.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
  "data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
  "data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
  "data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
  "data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
  "data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
  "data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
  "data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
  "data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
  "data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
  "data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
  "data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
  "data/test_papers/2024-IEEE-Design_and_Implementation_of_a_Magnetic_Coupling_Based_Segmented_Bend_Angle_Sensor_for_a_Soft_Robotic_Gripper.pdf": "fe95a2f245396f7c18e4afa035a52e3282774bb396e81015cecb42126e9dc143",
  "data/test_papers/2024-IEEE-A_Human_Finger-Inspired_Shape-Locking_Pneumatic_Gripper_Enabled_by_Folding_Laminar_Jamming_Structure.pdf": "5bdf50c59986430fea7771145cf86a0bf561285d1ed9e69fc4a9ffda11a27fb3",
  "data/test_papers/2024-A_Novel_Hybrid_Variable_Stiffness_Mechanism_Synergistic_Integration_of_Layer_Jamming_and_Shape_Memory_Polymer.pdf": "f28f2201b842e34e4aaca74620031a99d7f70033c125d45092c5e0713be5d5e4",
  "data/test_papers/2024-A_Soft_Finger_With_Tensile_Variable_Stiffness_Based_on_the_Cross-Sliding_Jamming_Mechanism.pdf": "269d15b83031841b76c965c392ef26e325ac938b50859569989ba9d496a4bc64",
  "data/test_papers/Adv Materials Technologies - 2020 - Chen - Smart Soft Actuators and Grippers Enabled by Self‐Powered Tribo‐Skins.pdf": "0003e353698504c4c21a05471925ef6feb4dccfdcdf4da534b2c5d7876d620d8",
  "data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
  "data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
  "data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
  "data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
  "data/chap1-2_citations/README.md": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c",
  "data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7",
  "data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
  "data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
  "data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/chap1-2_citations/M37__2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/chap1-2_citations/M30__A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
  "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d",
  "data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
  "data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03",
  "data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f",
  "data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
  "data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
  "data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837",
  "data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
  "data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2",
  "data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
  "data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
  "data/chap1-2_citations/MANIFEST.json": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda",
  "data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac",
  "data/chap1-2_citations/M32__2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a",
  "data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
  "data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
  "data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
  "data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0",
  "data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a",
  "data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db",
  "data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7",
  "data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1",
  "data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
  "data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
  "data/inbox/2024-IEEE-A_Human_Finger-Inspired_Shape-Locking_Pneumatic_Gripper_Enabled_by_Folding_Laminar_Jamming_Structure.pdf": "5bdf50c59986430fea7771145cf86a0bf561285d1ed9e69fc4a9ffda11a27fb3",
  "data/inbox/2024-A_Novel_Hybrid_Variable_Stiffness_Mechanism_Synergistic_Integration_of_Layer_Jamming_and_Shape_Memory_Polymer.pdf": "f28f2201b842e34e4aaca74620031a99d7f70033c125d45092c5e0713be5d5e4",
  "data/inbox/2026-Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/2026-Multilayer jamming-reinforced inflatable systems for rapidly deployable lightweight construction.pdf": "f77bc7b7d605e57e4bb7e11e468223ce7f670dc4e06072fd1ed99bb27062c5ca",
  "data/inbox/2018-Mechanically Versatile Soft Machines through Laminar.pdf": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
  "data/inbox/2024-Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots.pdf": "56d058a34a4d9708da644187fd8bd519eca480f77398e1922f89225af06f2846",
  "data/chap 2/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "68313a669b1065543fb904b48002bba91e734048e32b29e59cfc5ca43061fee6",
  "data/chap 2/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/chap 2/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/chap 2/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/README.md": "d0c0bfa985e46651788583bce56fd41a599c1a65b30af4d5420629b961470c9a",
  "data/papers/seed/2024-IEEE-Design_and_Implementation_of_a_Magnetic_Coupling_Based_Segmented_Bend_Angle_Sensor_for_a_Soft_Robotic_Gripper.pdf": "fe95a2f245396f7c18e4afa035a52e3282774bb396e81015cecb42126e9dc143",
  "data/papers/seed/Design_and_Experimental_Validation_of_a_Soft_Shape.pdf": "95d531dfcda5d5b8bff9ef2db4d1c827acba441ffa59e0a6e7e95162d3d80498",
  "data/papers/seed/2023-Advanced Intelligent Systems - Wang - A Bioinspired Gripper with Sequential Motion and Mutable Posture Enabled by.pdf": "a1917fa859af7887d372bac53820f07d89240a806432fec24ff69af2ddca9226",
  "data/papers/seed/2024-IEEE-A_Human_Finger-Inspired_Shape-Locking_Pneumatic_Gripper_Enabled_by_Folding_Laminar_Jamming_Structure.pdf": "5bdf50c59986430fea7771145cf86a0bf561285d1ed9e69fc4a9ffda11a27fb3",
  "data/papers/seed/2018-A_Variable_Stiffness_Robotic_Gripper_Based_on_Structure-Controlled_Principle (1).pdf": "5aedfd2730a760571b1728ca94a496da295b04d1e4294385161e5c720a9b663f",
  "data/papers/seed/2023-Adv Materials Technologies-A 3D Printing‐Enabled Artificially Innervated Smart Soft Gripper with Variable.pdf": "a1a03d9a899785d80ec11cc135746edb2cf6e3314a42f21c41d2e7defabd3b31",
  "data/papers/seed/2017-yang Novel variable-Stiffness Robotic Fingers with Built-In Position Feedback.pdf": "96aec3bae337a02fadf9a73c1961839840a21e769650aa8e647e190eb3e6b033",
  "data/papers/seed/2019-Long Shape Memory Alloy Tendonbased Soft Robotic Actuators and Implementation as a soft Gripper.pdf": "4dac06062a7e0423e08f7abf4a1d21540f0b0a78baeb8c16410826e67d874653",
  "data/papers/seed/2022-Snake_Robot_Gripper_Module_for_Search_and_Rescue_in_Narrow_Spaces.pdf": "fa47e75f9a3944933c7bf1daf7e0106585ff5e6c1af0b3dbd6a419c122730750",
  "data/papers/seed/2017_wang-SMA based Soft Gripper with VS for compliant and Effective Gasping .pdf": "4bf6ae90e073116a7d6983e905180618d4131bc9faa45474815cc3a94364cb34",
  "data/papers/seed/2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
  "data/papers/seed/2024-A_Novel_Hybrid_Variable_Stiffness_Mechanism_Synergistic_Integration_of_Layer_Jamming_and_Shape_Memory_Polymer.pdf": "f28f2201b842e34e4aaca74620031a99d7f70033c125d45092c5e0713be5d5e4",
  "data/papers/seed/TRIGGER_A_Lightweight_Universal_Jamming_Gripper_fo.pdf": "64a83322f39288f81e086439087e58af2a70e8f6ffdd136fb9b618374e351032",
  "data/papers/seed/2023-IEEE RAL Design_Modeling_and_Experiments_of_a_Variable_Stiffness_Soft_Robotic_Glove_for_Stroke_Patients_With_Clenched_Fist_Deformity.pdf": "dbe0e69179543b5591331e94fecfce0055fae770625804346396febb8e5fe52d",
  "data/papers/seed/Soft robotic grippers A review on technologies, materials, and applications .pdf": "fdd30f539d5f40a7e2fa686ee4bc4752fe2994b0d43b30ef811cfd85a9dc1feb",
  "data/papers/seed/2018-A_Soft_Robotic_Gripper_With_Gecko-Inspired_Adhesive.pdf": "dfe07593dc7c8c4f4b117f63692a4d99eb374a95ee6c39ea24f63b08fbacd6f2",
  "data/papers/seed/2020_Soft Humanoid Hands with Large Grasping Force Enable by flexible Hybrid Pneumatic Actuators.pdf": "2404868fbcf089f7f9f1f99cdbb2e90ccd8c813a2b31ecee5925bc73f795d895",
  "data/papers/seed/2022-A_Soft_Robot_With_Variable_Stiffness_Multidirectional_Grasping_Based_on_a_Folded_Plate_Mechanism_and_Particle_Jamming.pdf": "9036ba0b602aac27714918fd7d46d2a05f31fd0b7ddc432e4a6794a8bbd39d0c",
  "data/papers/seed/2023-IEEE Underactuated_Robotic_Gripper_With_Fiber-Optic_Force_Sensing_Tendons.pdf": "d6e4cf1d1430d039921e7a1a62b7eadb84440873b822631db4154725bde7d0d0",
  "data/papers/seed/2023-IEEE TIE-A Soft Variable Stiffness Hand With an integrated actuating cooling system.pdf": "db0ccb7d747060737405a88490f0ccb0b523946d1e179bcc5f3d5cf0dea170c5",
  "data/papers/seed/2020-A novel design of SMA based soft robotic gripper with variable stiffness.pdf": "4c30fda873ba94d65ea2b7715092eff6bd90783616cc9d13bc5def40b93811cc",
  "data/papers/seed/2022-IEEE-Tendon-Driven_Soft_Robotic_Gripper_for_Blackberry_Harvesting.pdf": "d3382c226ed8da906c5ef527b48ee1f9ffb2905f815d11c2abb38dd296cd77a4",
  "data/papers/seed/2023-IEEE Single-Motor_Robotic_Gripper_With_Three_Functional_Modes_for_Grasping_in_Confined_Spaces.pdf": "6f076ab4d44fa2964a04e94fcb4bd853e48134506974ac5179af80174f134e91",
  "data/papers/seed/Winandetal2026JournalofAdhesion.pdf": "923285b1030cd95d520efbb4ba046d5820a56b65b06d3da36f832a114061e12d",
  "data/papers/seed/2017-Soft_Robotic_Grippers_Based_on_Particle_Transmission.pdf": "75ecb1291a52e43e441ff1d93d5eaa9fb978a02a390a556be105bd811e08a058",
  "data/papers/seed/2019-Flexible Fingers Based on Shape Memory Alloy Actuated Modules.pdf": "63719eca8ee064423e6c68b391e96a81c332e2917cecde8c156309c447b92cc0",
  "data/papers/seed/2022-IEEE Soft_Exoskeleton_With_Fully_Actuated_Thumb_Movements_for_Grasping_Assistance.pdf": "57f85eb1619cbf18199b186109ca5a7241f655cf0e1427a6d37035503595b55b",
  "data/papers/seed/2022-A_Dexterous_Soft_Robotic_Hand_for_Delicate_In-Hand_Manipulation.pdf": "f6a95d9bb0a0ddc928cb229d553ec5686b991c7124becc79a44c4215a85cf01e",
  "data/papers/seed/2018-Soft Robotics Gripper.pdf": "ccc528bd6ab419eac1ba2b6d3e7a77d72169fc9c5a7c16e9654ccfac2c30c5aa",
  "data/papers/seed/Design_of_Telescopic_Soft_Gripper_for_Mangosteen_H.pdf": "7a12d36a652cac83bdfe5e7889f17722c9a8388ac7efbc41e1162fc9d8dce851",
  "data/papers/seed/Design_and_Analysis_of_a_Novel_Tri-layer_Granular_.pdf": "b19f76572d23669fbb005ee782fe988adc8d9ec196083b51fe359ef2380bec06",
  "data/papers/seed/2018-Soft actuator with stiffness and shape modulation Using 3D-printed Conductive Polylactic Acid Material.pdf": "6a92ae2d88a02a93eab1acea6c8590968762c83b090f1317e80cc0abbdb6d592",
  "data/papers/seed/2023-IEEE A_Palm-Shape_Variable-Stiffness_Gripper_Based_on_3D-Printed_Fabric_Jamming.pdf": "39520ca4cd41c36fd63fafdc71190e9edabb01869b99d808d9512ff3936e9709",
  "data/papers/seed/2022-IEEE A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": "26fb5818d63492ff43092a997908d595fe5c9fb0804dfaaf231a4b562f9e83d5",
  "data/papers/seed/Soft_robotics_gripper_technology_in_medical_surger.pdf": "ca522581558e9c9399cf3ec3b711f45fced77a2b4422f5758bdd10fc51d2fbc8",
  "data/papers/seed/Analysis_of_Contact_Force_and_Shape_Change_on_Gras.pdf": "3a6c7298b69b5f4c9dcfc9e23f1200521bed1b85f4eac2ab85718b927d0df18a",
  "data/papers/seed/Design_and_Automatic_Fabrication_of_Novel_Bio-Inspired_Soft_Smart_Robotic_Hands.pdf": "182f1c9f23cb838c0e9b19f3cd9b1ef31af0a1053f4c8ce911cdd688d3573510",
  "data/papers/seed/2023-IEEE Optimal_Design_of_a_Highly_Self-Adaptive_Gripper_with_Multi-Phalange_Compliant_Fingers_for_Grasping_Irregularly_Shaped_Objects.pdf": "79059ca07c7638b933ffd4fd167d29b57e0c82ff35cb738b67f6b124c529c619",
  "data/papers/seed/2018-Variable_Stiffness_Robotic_Hand_for_Stable_Grasp_and_Flexible_Handling.pdf": "293867082056d29a1a486437b9dacee97c9ae479841ae288b425be4700f2e5c9",
  "data/papers/seed/2021-Soft robotic fabric gripper with gecko adhesion and variable stiffness.pdf": "4eab68eb44e6bf14ae1b90f7678b9ab869d03e1a178ed552ae89e33a460c90ba",
  "data/papers/seed/2022-IEEE Modeling_of_Fluidic_Prestressed_Composite_Actuators_With_Application_to_Soft_Robotic_Grippers.pdf": "b62675b62a85edfb30611b347e5cff6ce93364d0156d83624d7c9157cc99972d",
  "data/papers/seed/2022-IEEE Elongatable_Gripper_Fingers_With_Integrated_Stretchable_Tactile_Sensors_for_Underactuated_Grasping_and_Dexterous_Manipulation.pdf": "a2fce8b2df24f2a5db0373fd6f1a58cae2fd0bb1c8bc14d741e6d54cebf2eb52",
  "data/papers/seed/2022-IEEE Optimizing_Out-of-Plane_Stiffness_for_Soft_Grippers.pdf": "e6deb76ed36807e3728f403f98826f7f8e208d64fc4664e7115bbeb429c3c600",
  "data/papers/seed/universal_gripper.pdf": "ece56d39a84b4d574135dff7e544010a4a37670d69f3ef24f8be29c852c4c499",
  "data/papers/seed/2018-Modeling of grasping force for a soft robotic gripper with variable stiffness.pdf": "e3ce477955d22f1819d4d565392c86342305c9ab84c9e72038d3f8c98945e57e",
  "data/papers/seed/Universal_Jamming_Gripper_Experimental_Analysis_on.pdf": "f17bc7cbcc674273467156588470d1acb892ccfdf3e787ef87e0ab7685c895b9",
  "data/papers/seed/Soft Robotics for Chemists.pdf": "de5329b2fb2f4acbe29b92df139354595fea3c6a9671220abbe39b913d5f7a86",
  "data/papers/seed/2023-IEEE Highly_Shape-Adaptable_Honeycomb_Gripper_Using_Orthotropic_Surface_Tension.pdf": "12e15c130a2e8e9831977a2e22e0633f6c926afbfd86dda7db2fdee84f254b15",
  "data/papers/seed/2021_Bio-Inspired Soft Grippers Based on Impactive Gripping.pdf": "e66f8bda116d07c06ce75b5da1f0e3d19d3236da00c49f0a3b53ac81f67db2f4",
  "data/papers/seed/frontiers-Soft Manipulators and Grippers- A Review-2016.pdf": "877d9ba31a9c1f0c2756963cc4cba54afbe0a4068a0faea9fca66f0eab3f17c9",
  "data/papers/seed/2023-IEEE A_Novel_Variable_Stiffness_and_Tunable_Bending_Shape_Soft_Robotic_Finger_Based_on_Thermoresponsive_Polymers.pdf": "7eddb5d92e4056643faa07c8ad0f813a176e0bc1e68cac39a40bab5cf71186e0",
  "data/papers/seed/2024-A_Soft_Finger_With_Tensile_Variable_Stiffness_Based_on_the_Cross-Sliding_Jamming_Mechanism.pdf": "269d15b83031841b76c965c392ef26e325ac938b50859569989ba9d496a4bc64",
  "data/papers/seed/2021-flexible seft-power multifunctional sensor for stiffness-tunable soft robotic gripper by multimaterial 3D printing.pdf": "3317077510942fb5b1cc7983e7122bafbd0e9c77c65a2eb267aedf4e398e72d3",
  "data/papers/seed/Adv Materials Technologies - 2020 - Chen - Smart Soft Actuators and Grippers Enabled by Self‐Powered Tribo‐Skins.pdf": "0003e353698504c4c21a05471925ef6feb4dccfdcdf4da534b2c5d7876d620d8",
  "data/papers/verification/MP1-V002/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/papers/verification/MP1-V002/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/papers/verification/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/papers/verification/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/papers/verification/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/papers/verification/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/papers/verification/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/papers/verification/D1-V002/2025-Continuum modeling for layer jamming structures.pdf": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
  "data/papers/verification/D1-V002/2025-A continuum-based model for a layer jamming beam.pdf": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
  "data/papers/verification/D1-V002/2025-Analysis and modeling of nonlinear.pdf": "1337634c62b96ae26ef3eb359df3952c7f08fee5a3ea63073c3fba297f59aea0",
  "data/papers/verification/D1-V002/2025-Toward a deeper understanding of layer jamming structures.pdf": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
  "data/papers/verification/D1-V006/2025-Fretting wear modeling of bolted joint interface with microscopic roughness usin.pdf": "7b85aadc8442d6303a845e49cf9c6d600d5251bcb686c64f1b17800e32447748",
  "data/papers/verification/D1-V006/2021-Experimental validation of the applicability of effective spring boundary conditions for modelling damaged interfaces in laminate structures.pdf": "444793969ce84ac1aaeff20392223d937823af720a6c8bece396e54873fd6f00",
  "data/papers/verification/D1-V006/2023-Modelling tangential friction considering contact pressure distribution of rough surfaces.pdf": "8ce1db3bcaf57b9b9d49c5eb1dfac4d3f6ab56ecf464bd873e83963062b70b9a",
  "data/papers/verification/D1-V006/2023-A Single-Variable Zigzag Approach to Model Imperfect Interfaces in Layered Beams.pdf": "a9cd14eca91ccf42144f882606bfb6f5adf04f81fb8f247e03e0abcb3e232728",
  "data/papers/verification/D1-V006/2024-Modeling of Stick-Slip Contact Mechanics Based on Improved Continuous-Scale Fractal-Discrete Iwan Model.pdf": "8daa38176da0c1b854d0e3700076de4382ee494b218f748ab127d0609f5faf39",
  "data/papers/verification/D1-V006/2024-Messina-A_novel_friction_model_for_steel-polymer_interfaces.pdf": "13e407003a5cfc4e64c361644addb6b25ef336fc5ab3bc8b6444b5184bcab69d",
  "data/papers/verification/D1-V006/2022-A barrier method for frictional contact on embedded interfaces.pdf": "202fd05d8fc96f98073992974a1af9cd1788d39a1769c9e1eba3edafce425406",
  "data/papers/verification/D1-V006/2016-Friction Characteristics of CFRP Plates in Contact with.pdf": "79d1adc34c4620d5e0a79cf7286915126017895cfff8a02d018c2e34ded5c628",
  "data/papers/verification/D1-V006/2015-Transition from stick to slip in Hertzian contact with.pdf": "ac9973e89efbbbb81d82fd21d38e41130b3b469917a720d6b1c98ecab31352fb",
  "data/papers/verification/D1-V006/2021-A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure.pdf": "afe2a3a310b81624fc3c0507fd3e88d5bd33b788d681ef1e7418847fa258d431",
  "data/papers/verification/D1-V006/2026-Stick-slip friction model for soft-hard joints under preload degradation.pdf": "02d3360815cf4a511c3ceedd7229975ef878f7e2c803282dc986f0277d899934",
  "data/papers/verification/D1-V006/2014-The existence of a critical length scale in regularised friction.pdf": "7c3aac183e08eb2f6f4d0e0765784b8287071f8c2938b9d18e3c2f6b28a0c5f4",
  "data/papers/verification/D1-V006/2022-A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes.pdf": "a300a3b71448d2044dec2fcf2f92214def360f0fd89761eae5d4a9ae1a8c2e5e",
  "data/papers/verification/D1-V006/2025-Theoretical, experimental, and numerical simulation studies on interface slip in steel-concrete.pdf": "fb057ab3b2337b544768f770e84c726bb3e4f3604802985a158290a020d341f9",
  "data/papers/verification/D1-V006/2026-A novel frictional contact correction transfer matrix method for bolted vibration systems.pdf": "20cee2210ada19720a2aa47d8c1a9de8f955d1bb73b96e91d57e8bb72d54b0c7",
  "data/papers/verification/D1-V006/2026-The global-local mechanical behaviors of multilayered structure and.pdf": "ca46dc062d14b70162b118fcaee0ad30231a6a7d09acfa4f177b5a7d12e44eee",
  "data/papers/verification/D1-V007/2026-A global-local homogenization model for hierarchical chiral.pdf": "1502d9c1c60841eb6c1bdd7c885d0a39c42871a85a7b54627463df6758d29847",
  "data/papers/verification/D1-V007/2026-A coupled electromagnetic-mechanical model for high temperature.pdf": "6bdb4151e255b35e0c37e129c135f3e540daef2b7c04334bbe2c05648122dd0f",
  "data/papers/verification/D1-V007/2026-Critical state model for superconductivity features and.pdf": "a32f8501d6835ed4fe58c55c092c206f4b97ab984d499f6ad6eb9c536e9cf609",
  "data/papers/verification/D1-V005/2016-Derivation of the exact stiffness matrix of shear-deformable multi-layered beam element in partial interaction.pdf": "bdf95f06027484b2b512ad9ad4c75712b1b0150775b2f02946b55c69d87c368f",
  "data/papers/verification/D1-V005/2007-Analytical Solution of Two-Layer Beam Taking into account Interlayer Slip and Shear Deformation.pdf": "f5bba53ef26fba82fd15cd77fb2747952132d7414a9a3af0b23e41efef1a2a5c",
  "data/papers/verification/D1-V005/2002-Steel and concrete composite beams with flexible.pdf": "d0699583ac70b7885a5005d60f905c578d8c8fd7352d192105518deea4691fbe",
  "data/papers/verification/D1-V005/2013-Exact finite elements for multilayered composite beam-columns with partial interaction.pdf": "c9bf5cb21f42b0e704ab206253bfb9a713f50b9e242646bf80ab9cf3d4f90f77",
  "data/papers/verification/D1-V005/1974-The dependence of shear lag on partial interaction in composite beams.pdf": "8a6d33e5275a76bdf6b18219589e88a88a5f75b8d247b6d1248b71d1d6db880b",
  "data/papers/verification/D1-V005/1998-A rational model for the degree of interaction in composite beams with flexible shear connector.pdf": "a28d4f16682f48d1a73608691767942d4bd9a95c171a1a44be51024643f152ce",
  "data/papers/verification/D1-V005/1990-The deformation of composite beams with discrete flexible connection.pdf": "99721ae36938f6f5d6cb1512022de056983854f3744c62b6d27ceeb950c0e932",
  "data/papers/verification/D1-V005/2025-Flexible N-layer composite beam-column elements with interlayer partial interaction imperfectio.pdf": "8a4d5de33a0c1f35257ccffa6a82bd5c9f026dc4ea45897e514b71cc4833c6b2",
  "data/papers/verification/D1-V005/2006-Time analysis of composite beams with partial interaction using available modelling techniques A comparative study.pdf": "a577a30ffda18b192aeb732577402a6da296af2b561ec88d421048b9b369fa0f",
  "data/papers/verification/D1-V005/2008-Composite beam–columns with interlayer slip—Approximate analysis.pdf": "d87b4ad44dc939484403061415baee3429b26c1af37a2cb124df357602017b7a",
  "data/papers/verification/D1-V005/2008-Locking problems in the partial interaction analysis of multi-layered.pdf": "2ad029e62c20c7581f0a210fb66badf66e564e7feb82a3f924320411299e62d6",
  "data/papers/verification/D1-V005/2026-Laminated Partially-Composite Plate Theory.pdf": "71c8d5e2c7acbfa3061de9ebd415eee009564eee31434ccdfb77fbd40708d9ef",
  "data/papers/verification/D1-V005/2010-Analytical and numerical analysis of multilayered beams with interlayer slip.pdf": "14958e37b2d6118fa074a83f7ae8c3c1ca37aaba3cbad2d8ebfb5bbaa964f400",
  "data/papers/verification/D1-V005/2009-A simplified analysis method for composite beams with interlayer slip.pdf": "aa091ea74d07c5da4076bf121c2906d81e27a071df79867b1efdff0a7f9a1189",
  "data/papers/verification/D1-V005/2013-Analysis of Composite Beams with Incomplete Interaction I.pdf": "f8e8c7b1a40c638ad9be438c64febcfcd93a616f092856b037705bd36bf06dcb",
  "data/papers/verification/D1-V005/2007-Exact static analysis of partially composite beams and beam-columns.pdf": "eeb0863c0d2a2732bdda7c0cef32ea55573ed9b394375e71badced4628ad075d",
  "data/papers/verification/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/papers/verification/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/papers/verification/MP1-V001/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/papers/verification/MP1-V001/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/papers/verification/MP1-V001/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/papers/verification/D1-V001/2018-Mechanically Versatile Soft Machines through Laminar.pdf": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
  "data/papers/verification/D1-V001/2024-Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots.pdf": "56d058a34a4d9708da644187fd8bd519eca480f77398e1922f89225af06f2846",
  "data/papers/verification/D1-V001/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
  "data/papers/verification/D1-V009/Mech Cohesive Frict Material - 1999 - Adhikary - Modelling the large deformation.pdf": "d75a3e82bc5a373bb44d8e6238341438910aa6ffa1cbcc03c4b7b2cc85c0a5fb",
  "data/papers/verification/D1-V003/A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
  "data/papers/verification/D1-V003/2026-Chen-Design Characteristics of Continuum Robots Based on TSA Variable Stiffness Method.pdf": "6723402e32ddc8d146483dadcf3fe1c35e671e0f25aa22abeebe4dd860a3034b",
  "data/papers/verification/D1-V003/Decoupling_Control_of_a_Multi-Segment_Hybrid-Actuated_Soft_Origami_Continuum_Robot_Through_Variable_Stiffness.pdf": "8d3b7d72a678fca2df5ddb5d9603a93518eb398584a51a0fb0219e71a96b62b4",
  "data/papers/verification/D1-V003/Stiffness Change for Reconfiguration of.pdf": "dc9ad29f753d760eb4da07276315790cc07a85a531e5196bdb6b2d9716a17862",
  "data/papers/verification/D1-V003/Stiffness-Tuneable Segment for Continuum Soft Robots.pdf": "7366c065fa1e83eb2aa1e4b1ec9b69c8933d1d51cff3e1b6e2bb365aedfc8fb2",
  "data/papers/verification/D1-V003/A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
  "data/papers/verification/D1-V003/An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
  "data/papers/verification/D1-V003/A Novel Model for Layer Jamming-based Continuum Robots.pdf": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
  "data/papers/verification/D1-V003/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
  "data/papers/verification/D1-V004/1998-A relative gradient theory for layered materials.pdf": "2f85ad579a309c4c4bebcf638f0ca18558b046d6bcb35f20ba1cedd456c57ed2",
  "data/papers/verification/D1-V004/2018-A homogenized structural model for shear deformable composites.pdf": "8113666e962127039ddfec102e4bea849b5290077935e2d5d188a9cd46361305",
  "data/papers/verification/D1-V004/2025-Slip-mediated axisymmetric bending of multilayered structures with.pdf": "bdeedc2731e96976b82e73f23908fe40d660ca8d62c59ffcf12d6e7fe80c2769",
  "data/papers/verification/D1-V004/2016-INFLUENCE OF SLIP EFFECT ON BENDING CHARACTERISTICS OF FRICTIONAL LAMINATED BEAMS.pdf": "47fe4949dc7ad5ba6d7fdfaba2d4bfe4411468518d5a9cbec20c5299e214a31a",
  "data/papers/verification/D1-V004/2019-Mechanism research of slip effect between frictional laminated beams.pdf": "ee464a718b132e023b502c6bf396bc5b810e88e03980bd71f6dd9c9cc8c70a15",
  "data/papers/verification/D1-V004/2018-Bending Stiffness of Parallel Wire Cables.pdf": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
  "data/papers/verification/D1-V004/2024-An analytic solution for bending of multilayered structures with.pdf": "bd5af3e26decf56c75116e0ade5f247dd736f1df312db7e1dec9aac746355b9d",
  "data/papers/verification/D1-V004/2026-Thickness Gradient Design Enhances Bending Performance of.pdf": "7f93ab3253623c56962e13961ff66109212a7f5518e56a96e53f2f02eb61553f",
  "data/papers/verification/D1-V004/2020-Novel dynamic model for calculating the equivalent Young’s.pdf": "2d30a68b714e06a8442050923e62515199331836c282c1a04dd1cf8462a3a86c",
  "data/papers/verification/D1-V004/2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf": "c4531c66c9c312a37f235e5355f617b14d52da5fca9cdd82376adef931b1ba52",
  "data/papers/verification/D1-V004/1993-BENDING STRESS ENHANCEMENT IN MATERIALS.pdf": "66fcf766cb5039e18d54b0199494f6f32dd64293a07e1286f08c043dbe9c5b83",
  "data/papers/verification/D1-V004/2014-Assessment and correction of theories for multilayered.pdf": "33ea2034277aeb985f8c378b2972aa9040a91d6d7f90a4d3f62071b21efd7e55",
  "data/papers/verification/D1-V004/Influence of boundary conditions on the response of.pdf": "4994f7ed3ffc624981b57094552501da15888615a81994a8a36a11ae12301c52",
  "data/papers/verification/D1-V004/2021-Analytical model for the bending of parallel wire cables considering interactions among wires__ecdac261.pdf": "ecdac26196d469aa888159e2e6479170c05fe54f559565b5335752d03233af75",
  "data/papers/verification/D1-V004/1993-Bending stress enhancement-Part II-Unlayered shear-weak model.pdf": "f00d886124e51a93d169fa8a43c5f9edac85b1cfbcd3ca0b4a958f702d02b521",
  "data/papers/verification/D1-V004/2022-Equivalent dynamic model of multilayered structures with imperfect interfaces.pdf": "0f1b512cee959a3daf8635dde3aeed6c4d3c6dd17e5aabef1248032eb09e4771",
  "data/papers/verification/D1-V008/2024-Ye-Analytical Solution for Bending Deformation of Steel-Concrete Composite Beams Considering Nonlinear Interfacial Slip.pdf": "53d328abaad573cca78c06c352a0e3d12ccff148a7597ff3947273297608e210",
  "data/inbox/verification_pending/2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
  "data/inbox/_already_added/2024-IEEE-Design_and_Implementation_of_a_Magnetic_Coupling_Based_Segmented_Bend_Angle_Sensor_for_a_Soft_Robotic_Gripper.pdf": "fe95a2f245396f7c18e4afa035a52e3282774bb396e81015cecb42126e9dc143",
  "data/inbox/_already_added/Design_and_Experimental_Validation_of_a_Soft_Shape.pdf": "95d531dfcda5d5b8bff9ef2db4d1c827acba441ffa59e0a6e7e95162d3d80498",
  "data/inbox/_already_added/2023-Advanced Intelligent Systems - Wang - A Bioinspired Gripper with Sequential Motion and Mutable Posture Enabled by.pdf": "a1917fa859af7887d372bac53820f07d89240a806432fec24ff69af2ddca9226",
  "data/inbox/_already_added/2024-IEEE-A_Human_Finger-Inspired_Shape-Locking_Pneumatic_Gripper_Enabled_by_Folding_Laminar_Jamming_Structure.pdf": "5bdf50c59986430fea7771145cf86a0bf561285d1ed9e69fc4a9ffda11a27fb3",
  "data/inbox/_already_added/2018-A_Variable_Stiffness_Robotic_Gripper_Based_on_Structure-Controlled_Principle (1).pdf": "5aedfd2730a760571b1728ca94a496da295b04d1e4294385161e5c720a9b663f",
  "data/inbox/_already_added/2023-Adv Materials Technologies-A 3D Printing‐Enabled Artificially Innervated Smart Soft Gripper with Variable.pdf": "a1a03d9a899785d80ec11cc135746edb2cf6e3314a42f21c41d2e7defabd3b31",
  "data/inbox/_already_added/2017-yang Novel variable-Stiffness Robotic Fingers with Built-In Position Feedback.pdf": "96aec3bae337a02fadf9a73c1961839840a21e769650aa8e647e190eb3e6b033",
  "data/inbox/_already_added/2019-Long Shape Memory Alloy Tendonbased Soft Robotic Actuators and Implementation as a soft Gripper.pdf": "4dac06062a7e0423e08f7abf4a1d21540f0b0a78baeb8c16410826e67d874653",
  "data/inbox/_already_added/2022-Snake_Robot_Gripper_Module_for_Search_and_Rescue_in_Narrow_Spaces.pdf": "fa47e75f9a3944933c7bf1daf7e0106585ff5e6c1af0b3dbd6a419c122730750",
  "data/inbox/_already_added/2017_wang-SMA based Soft Gripper with VS for compliant and Effective Gasping .pdf": "4bf6ae90e073116a7d6983e905180618d4131bc9faa45474815cc3a94364cb34",
  "data/inbox/_already_added/2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
  "data/inbox/_already_added/2024-A_Novel_Hybrid_Variable_Stiffness_Mechanism_Synergistic_Integration_of_Layer_Jamming_and_Shape_Memory_Polymer.pdf": "f28f2201b842e34e4aaca74620031a99d7f70033c125d45092c5e0713be5d5e4",
  "data/inbox/_already_added/TRIGGER_A_Lightweight_Universal_Jamming_Gripper_fo.pdf": "64a83322f39288f81e086439087e58af2a70e8f6ffdd136fb9b618374e351032",
  "data/inbox/_already_added/2023-IEEE RAL Design_Modeling_and_Experiments_of_a_Variable_Stiffness_Soft_Robotic_Glove_for_Stroke_Patients_With_Clenched_Fist_Deformity.pdf": "dbe0e69179543b5591331e94fecfce0055fae770625804346396febb8e5fe52d",
  "data/inbox/_already_added/Soft robotic grippers A review on technologies, materials, and applications .pdf": "fdd30f539d5f40a7e2fa686ee4bc4752fe2994b0d43b30ef811cfd85a9dc1feb",
  "data/inbox/_already_added/2018-A_Soft_Robotic_Gripper_With_Gecko-Inspired_Adhesive.pdf": "dfe07593dc7c8c4f4b117f63692a4d99eb374a95ee6c39ea24f63b08fbacd6f2",
  "data/inbox/_already_added/2020_Soft Humanoid Hands with Large Grasping Force Enable by flexible Hybrid Pneumatic Actuators.pdf": "2404868fbcf089f7f9f1f99cdbb2e90ccd8c813a2b31ecee5925bc73f795d895",
  "data/inbox/_already_added/2022-A_Soft_Robot_With_Variable_Stiffness_Multidirectional_Grasping_Based_on_a_Folded_Plate_Mechanism_and_Particle_Jamming.pdf": "9036ba0b602aac27714918fd7d46d2a05f31fd0b7ddc432e4a6794a8bbd39d0c",
  "data/inbox/_already_added/2023-IEEE Underactuated_Robotic_Gripper_With_Fiber-Optic_Force_Sensing_Tendons.pdf": "d6e4cf1d1430d039921e7a1a62b7eadb84440873b822631db4154725bde7d0d0",
  "data/inbox/_already_added/2023-IEEE TIE-A Soft Variable Stiffness Hand With an integrated actuating cooling system.pdf": "db0ccb7d747060737405a88490f0ccb0b523946d1e179bcc5f3d5cf0dea170c5",
  "data/inbox/_already_added/2020-A novel design of SMA based soft robotic gripper with variable stiffness.pdf": "4c30fda873ba94d65ea2b7715092eff6bd90783616cc9d13bc5def40b93811cc",
  "data/inbox/_already_added/2022-IEEE-Tendon-Driven_Soft_Robotic_Gripper_for_Blackberry_Harvesting.pdf": "d3382c226ed8da906c5ef527b48ee1f9ffb2905f815d11c2abb38dd296cd77a4",
  "data/inbox/_already_added/2023-IEEE Single-Motor_Robotic_Gripper_With_Three_Functional_Modes_for_Grasping_in_Confined_Spaces.pdf": "6f076ab4d44fa2964a04e94fcb4bd853e48134506974ac5179af80174f134e91",
  "data/inbox/_already_added/Winandetal2026JournalofAdhesion.pdf": "923285b1030cd95d520efbb4ba046d5820a56b65b06d3da36f832a114061e12d",
  "data/inbox/_already_added/2017-Soft_Robotic_Grippers_Based_on_Particle_Transmission.pdf": "75ecb1291a52e43e441ff1d93d5eaa9fb978a02a390a556be105bd811e08a058",
  "data/inbox/_already_added/2019-Flexible Fingers Based on Shape Memory Alloy Actuated Modules.pdf": "63719eca8ee064423e6c68b391e96a81c332e2917cecde8c156309c447b92cc0",
  "data/inbox/_already_added/2022-IEEE Soft_Exoskeleton_With_Fully_Actuated_Thumb_Movements_for_Grasping_Assistance.pdf": "57f85eb1619cbf18199b186109ca5a7241f655cf0e1427a6d37035503595b55b",
  "data/inbox/_already_added/2022-A_Dexterous_Soft_Robotic_Hand_for_Delicate_In-Hand_Manipulation.pdf": "f6a95d9bb0a0ddc928cb229d553ec5686b991c7124becc79a44c4215a85cf01e",
  "data/inbox/_already_added/2018-Soft Robotics Gripper.pdf": "ccc528bd6ab419eac1ba2b6d3e7a77d72169fc9c5a7c16e9654ccfac2c30c5aa",
  "data/inbox/_already_added/Design_of_Telescopic_Soft_Gripper_for_Mangosteen_H.pdf": "7a12d36a652cac83bdfe5e7889f17722c9a8388ac7efbc41e1162fc9d8dce851",
  "data/inbox/_already_added/Design_and_Analysis_of_a_Novel_Tri-layer_Granular_.pdf": "b19f76572d23669fbb005ee782fe988adc8d9ec196083b51fe359ef2380bec06",
  "data/inbox/_already_added/2018-Soft actuator with stiffness and shape modulation Using 3D-printed Conductive Polylactic Acid Material.pdf": "6a92ae2d88a02a93eab1acea6c8590968762c83b090f1317e80cc0abbdb6d592",
  "data/inbox/_already_added/2023-IEEE A_Palm-Shape_Variable-Stiffness_Gripper_Based_on_3D-Printed_Fabric_Jamming.pdf": "39520ca4cd41c36fd63fafdc71190e9edabb01869b99d808d9512ff3936e9709",
  "data/inbox/_already_added/2022-IEEE A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": "26fb5818d63492ff43092a997908d595fe5c9fb0804dfaaf231a4b562f9e83d5",
  "data/inbox/_already_added/Soft_robotics_gripper_technology_in_medical_surger.pdf": "ca522581558e9c9399cf3ec3b711f45fced77a2b4422f5758bdd10fc51d2fbc8",
  "data/inbox/_already_added/Analysis_of_Contact_Force_and_Shape_Change_on_Gras.pdf": "3a6c7298b69b5f4c9dcfc9e23f1200521bed1b85f4eac2ab85718b927d0df18a",
  "data/inbox/_already_added/Design_and_Automatic_Fabrication_of_Novel_Bio-Inspired_Soft_Smart_Robotic_Hands.pdf": "182f1c9f23cb838c0e9b19f3cd9b1ef31af0a1053f4c8ce911cdd688d3573510",
  "data/inbox/_already_added/2023-IEEE Optimal_Design_of_a_Highly_Self-Adaptive_Gripper_with_Multi-Phalange_Compliant_Fingers_for_Grasping_Irregularly_Shaped_Objects.pdf": "79059ca07c7638b933ffd4fd167d29b57e0c82ff35cb738b67f6b124c529c619",
  "data/inbox/_already_added/2018-Variable_Stiffness_Robotic_Hand_for_Stable_Grasp_and_Flexible_Handling.pdf": "293867082056d29a1a486437b9dacee97c9ae479841ae288b425be4700f2e5c9",
  "data/inbox/_already_added/2021-Soft robotic fabric gripper with gecko adhesion and variable stiffness.pdf": "4eab68eb44e6bf14ae1b90f7678b9ab869d03e1a178ed552ae89e33a460c90ba",
  "data/inbox/_already_added/2022-IEEE Modeling_of_Fluidic_Prestressed_Composite_Actuators_With_Application_to_Soft_Robotic_Grippers.pdf": "b62675b62a85edfb30611b347e5cff6ce93364d0156d83624d7c9157cc99972d",
  "data/inbox/_already_added/2022-IEEE Elongatable_Gripper_Fingers_With_Integrated_Stretchable_Tactile_Sensors_for_Underactuated_Grasping_and_Dexterous_Manipulation.pdf": "a2fce8b2df24f2a5db0373fd6f1a58cae2fd0bb1c8bc14d741e6d54cebf2eb52",
  "data/inbox/_already_added/2022-IEEE Optimizing_Out-of-Plane_Stiffness_for_Soft_Grippers.pdf": "e6deb76ed36807e3728f403f98826f7f8e208d64fc4664e7115bbeb429c3c600",
  "data/inbox/_already_added/universal_gripper.pdf": "ece56d39a84b4d574135dff7e544010a4a37670d69f3ef24f8be29c852c4c499",
  "data/inbox/_already_added/2018-Modeling of grasping force for a soft robotic gripper with variable stiffness.pdf": "e3ce477955d22f1819d4d565392c86342305c9ab84c9e72038d3f8c98945e57e",
  "data/inbox/_already_added/Universal_Jamming_Gripper_Experimental_Analysis_on.pdf": "f17bc7cbcc674273467156588470d1acb892ccfdf3e787ef87e0ab7685c895b9",
  "data/inbox/_already_added/Soft Robotics for Chemists.pdf": "de5329b2fb2f4acbe29b92df139354595fea3c6a9671220abbe39b913d5f7a86",
  "data/inbox/_already_added/2023-IEEE Highly_Shape-Adaptable_Honeycomb_Gripper_Using_Orthotropic_Surface_Tension.pdf": "12e15c130a2e8e9831977a2e22e0633f6c926afbfd86dda7db2fdee84f254b15",
  "data/inbox/_already_added/2021_Bio-Inspired Soft Grippers Based on Impactive Gripping.pdf": "e66f8bda116d07c06ce75b5da1f0e3d19d3236da00c49f0a3b53ac81f67db2f4",
  "data/inbox/_already_added/frontiers-Soft Manipulators and Grippers- A Review-2016.pdf": "877d9ba31a9c1f0c2756963cc4cba54afbe0a4068a0faea9fca66f0eab3f17c9",
  "data/inbox/_already_added/2023-IEEE A_Novel_Variable_Stiffness_and_Tunable_Bending_Shape_Soft_Robotic_Finger_Based_on_Thermoresponsive_Polymers.pdf": "7eddb5d92e4056643faa07c8ad0f813a176e0bc1e68cac39a40bab5cf71186e0",
  "data/inbox/_already_added/2024-A_Soft_Finger_With_Tensile_Variable_Stiffness_Based_on_the_Cross-Sliding_Jamming_Mechanism.pdf": "269d15b83031841b76c965c392ef26e325ac938b50859569989ba9d496a4bc64",
  "data/inbox/_already_added/2021-flexible seft-power multifunctional sensor for stiffness-tunable soft robotic gripper by multimaterial 3D printing.pdf": "3317077510942fb5b1cc7983e7122bafbd0e9c77c65a2eb267aedf4e398e72d3",
  "data/inbox/_already_added/Adv Materials Technologies - 2020 - Chen - Smart Soft Actuators and Grippers Enabled by Self‐Powered Tribo‐Skins.pdf": "0003e353698504c4c21a05471925ef6feb4dccfdcdf4da534b2c5d7876d620d8",
  "data/inbox/verification_pending/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/inbox/verification_pending/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/inbox/verification_pending/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/inbox/verification_pending/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/inbox/verification_pending/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/inbox/verification_pending/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/inbox/verification_pending/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/inbox/verification_pending/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/inbox/verification_pending/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/inbox/verification_pending/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/inbox/verification_pending/MP1-V002/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/inbox/verification_pending/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/inbox/verification_pending/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/inbox/verification_pending/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/inbox/verification_pending/MP1-V002/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/inbox/verification_pending/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/inbox/verification_pending/D1-V002/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
  "data/inbox/verification_pending/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/inbox/verification_pending/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/inbox/verification_pending/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/inbox/verification_pending/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/inbox/verification_pending/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/inbox/verification_pending/MP1-V001/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/inbox/verification_pending/MP1-V001/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/inbox/verification_pending/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/inbox/verification_pending/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/inbox/verification_pending/MP1-V001/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/inbox/verification_pending/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/inbox/verification_pending/D1-V009/Mech Cohesive Frict Material - 1999 - Adhikary - Modelling the large deformation.pdf": "d75a3e82bc5a373bb44d8e6238341438910aa6ffa1cbcc03c4b7b2cc85c0a5fb",
  "data/inbox/verification_pending/D1-V002/selected/2025-Toward a deeper understanding of layer jamming structures.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V002/selected/2025-Continuum modeling for layer jamming structures.pdf": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
  "data/inbox/verification_pending/D1-V002/selected/2025-A continuum-based model for a layer jamming beam.pdf": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
  "data/inbox/verification_pending/D1-V002/selected/2025-A continuum-based model for a layer jamming beam.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V002/selected/2025-Analysis and modeling of nonlinear.pdf": "1337634c62b96ae26ef3eb359df3952c7f08fee5a3ea63073c3fba297f59aea0",
  "data/inbox/verification_pending/D1-V002/selected/2025-Toward a deeper understanding of layer jamming structures.pdf": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
  "data/inbox/verification_pending/D1-V002/selected/2025-Continuum modeling for layer jamming structures.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2025-Fretting wear modeling of bolted joint interface with microscopic roughness usin.pdf": "7b85aadc8442d6303a845e49cf9c6d600d5251bcb686c64f1b17800e32447748",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2021-Experimental validation of the applicability of effective spring boundary conditions for modelling damaged interfaces in laminate structures.pdf": "444793969ce84ac1aaeff20392223d937823af720a6c8bece396e54873fd6f00",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2023-Modelling tangential friction considering contact pressure distribution of rough surfaces.pdf": "8ce1db3bcaf57b9b9d49c5eb1dfac4d3f6ab56ecf464bd873e83963062b70b9a",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2023-A Single-Variable Zigzag Approach to Model Imperfect Interfaces in Layered Beams.pdf": "a9cd14eca91ccf42144f882606bfb6f5adf04f81fb8f247e03e0abcb3e232728",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/Earthq Engng Struct Dyn - 2024 - Messina - A novel friction model for steel﹑ol.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2024-Modeling of Stick-Slip Contact Mechanics Based on Improved Continuous-Scale Fractal-Discrete Iwan Model.pdf": "8daa38176da0c1b854d0e3700076de4382ee494b218f748ab127d0609f5faf39",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2024-Messina-A_novel_friction_model_for_steel-polymer_interfaces.pdf": "13e407003a5cfc4e64c361644addb6b25ef336fc5ab3bc8b6444b5184bcab69d",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/Anovel friction model for steel-polymer interfaces in.pdf": "13e407003a5cfc4e64c361644addb6b25ef336fc5ab3bc8b6444b5184bcab69d",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2022-A barrier method for frictional contact on embedded interfaces.pdf": "202fd05d8fc96f98073992974a1af9cd1788d39a1769c9e1eba3edafce425406",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2016-Friction Characteristics of CFRP Plates in Contact with.pdf": "79d1adc34c4620d5e0a79cf7286915126017895cfff8a02d018c2e34ded5c628",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2015-Transition from stick to slip in Hertzian contact with.pdf": "ac9973e89efbbbb81d82fd21d38e41130b3b469917a720d6b1c98ecab31352fb",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2021-A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure.pdf": "afe2a3a310b81624fc3c0507fd3e88d5bd33b788d681ef1e7418847fa258d431",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2026-Stick-slip friction model for soft-hard joints under preload degradation.pdf": "02d3360815cf4a511c3ceedd7229975ef878f7e2c803282dc986f0277d899934",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2014-The existence of a critical length scale in regularised friction.pdf": "7c3aac183e08eb2f6f4d0e0765784b8287071f8c2938b9d18e3c2f6b28a0c5f4",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2022-A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes.pdf": "a300a3b71448d2044dec2fcf2f92214def360f0fd89761eae5d4a9ae1a8c2e5e",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2025-Theoretical, experimental, and numerical simulation studies on interface slip in steel-concrete.pdf": "fb057ab3b2337b544768f770e84c726bb3e4f3604802985a158290a020d341f9",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2026-A novel frictional contact correction transfer matrix method for bolted vibration systems.pdf": "20cee2210ada19720a2aa47d8c1a9de8f955d1bb73b96e91d57e8bb72d54b0c7",
  "data/inbox/verification_pending/D1-V006/C03_imperfect_interface/2026-The global-local mechanical behaviors of multilayered structure and.pdf": "ca46dc062d14b70162b118fcaee0ad30231a6a7d09acfa4f177b5a7d12e44eee",
  "data/inbox/verification_pending/D1-V007/C04_forward_citations/2026-A global-local homogenization model for hierarchical chiral.pdf": "1502d9c1c60841eb6c1bdd7c885d0a39c42871a85a7b54627463df6758d29847",
  "data/inbox/verification_pending/D1-V007/C04_forward_citations/2026-A coupled electromagnetic-mechanical model for high temperature.pdf": "6bdb4151e255b35e0c37e129c135f3e540daef2b7c04334bbe2c05648122dd0f",
  "data/inbox/verification_pending/D1-V007/C04_forward_citations/2026-A coupled electromagnetic-mechanical model for high temperature.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V007/C04_forward_citations/2026-Critical state model for superconductivity features and.pdf": "a32f8501d6835ed4fe58c55c092c206f4b97ab984d499f6ad6eb9c536e9cf609",
  "data/inbox/verification_pending/D1-V007/C04_forward_citations/2026-Critical state model for superconductivity features and.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V007/C04_forward_citations/2026-A global-local homogenization model for hierarchical chiral.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2016-Derivation of the exact stiffness matrix of shear-deformable multi-layered beam element in partial interaction.pdf": "bdf95f06027484b2b512ad9ad4c75712b1b0150775b2f02946b55c69d87c368f",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2007-Analytical Solution of Two-Layer Beam Taking into account Interlayer Slip and Shear Deformation.pdf": "f5bba53ef26fba82fd15cd77fb2747952132d7414a9a3af0b23e41efef1a2a5c",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2002-Steel and concrete composite beams with flexible.pdf": "d0699583ac70b7885a5005d60f905c578d8c8fd7352d192105518deea4691fbe",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2013-Exact finite elements for multilayered composite beam-columns with partial interaction.pdf": "c9bf5cb21f42b0e704ab206253bfb9a713f50b9e242646bf80ab9cf3d4f90f77",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/1974-The dependence of shear lag on partial interaction in composite beams.pdf": "8a6d33e5275a76bdf6b18219589e88a88a5f75b8d247b6d1248b71d1d6db880b",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/1998-A rational model for the degree of interaction in composite beams with flexible shear connector.pdf": "a28d4f16682f48d1a73608691767942d4bd9a95c171a1a44be51024643f152ce",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/1990-The deformation of composite beams with discrete flexible connection.pdf": "99721ae36938f6f5d6cb1512022de056983854f3744c62b6d27ceeb950c0e932",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2025-Flexible N-layer composite beam-column elements with interlayer partial interaction imperfectio.pdf": "8a4d5de33a0c1f35257ccffa6a82bd5c9f026dc4ea45897e514b71cc4833c6b2",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2006-Time analysis of composite beams with partial interaction using available modelling techniques A comparative study.pdf": "a577a30ffda18b192aeb732577402a6da296af2b561ec88d421048b9b369fa0f",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2008-Composite beam–columns with interlayer slip—Approximate analysis.pdf": "d87b4ad44dc939484403061415baee3429b26c1af37a2cb124df357602017b7a",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2008-Locking problems in the partial interaction analysis of multi-layered.pdf": "2ad029e62c20c7581f0a210fb66badf66e564e7feb82a3f924320411299e62d6",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2026-Laminated Partially-Composite Plate Theory.pdf": "71c8d5e2c7acbfa3061de9ebd415eee009564eee31434ccdfb77fbd40708d9ef",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2010-Analytical and numerical analysis of multilayered beams with interlayer slip.pdf": "14958e37b2d6118fa074a83f7ae8c3c1ca37aaba3cbad2d8ebfb5bbaa964f400",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2009-A simplified analysis method for composite beams with interlayer slip.pdf": "aa091ea74d07c5da4076bf121c2906d81e27a071df79867b1efdff0a7f9a1189",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2013-Analysis of Composite Beams with Incomplete Interaction I.pdf": "f8e8c7b1a40c638ad9be438c64febcfcd93a616f092856b037705bd36bf06dcb",
  "data/inbox/verification_pending/D1-V005/C02_partial_interaction/2007-Exact static analysis of partially composite beams and beam-columns.pdf": "eeb0863c0d2a2732bdda7c0cef32ea55573ed9b394375e71badced4628ad075d",
  "data/inbox/verification_pending/D1-V003/citation_maps/2026-Cheng-Review-Variable-Stiffness-Continuum-Robots.pdf": "006dfd43f56ca5bdb43c49e2427ae14f4dcbe4f24ee9d38b7cff24210dd57d18",
  "data/inbox/verification_pending/D1-V003/citation_maps/2026-Cheng-Review-Variable-Stiffness-Continuum-Robots.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V003/selected/2026-Modeling_Control_and_Stiffness_Regulation_of_Layer_Jamming-Based_Continuum_Robots.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V003/selected/2025-Toward a deeper understanding of layer jamming structures.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V003/selected/2026-Chen-Design Characteristics of Continuum Robots Based on TSA Variable Stiffness Method.pdf": "6723402e32ddc8d146483dadcf3fe1c35e671e0f25aa22abeebe4dd860a3034b",
  "data/inbox/verification_pending/D1-V003/selected/2025-Zhang-Toward-a-deeper-understanding-of-layer-jamming-structures.pdf": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
  "data/inbox/verification_pending/D1-V003/selected/2026-Chen-Design Characteristics of Continuum Robots Based on TSA Variable Stiffness Method.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V003/selected/2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
  "data/inbox/verification_pending/D1-V003/scopus_A01/A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
  "data/inbox/verification_pending/D1-V003/scopus_A01/Decoupling_Control_of_a_Multi-Segment_Hybrid-Actuated_Soft_Origami_Continuum_Robot_Through_Variable_Stiffness.pdf": "8d3b7d72a678fca2df5ddb5d9603a93518eb398584a51a0fb0219e71a96b62b4",
  "data/inbox/verification_pending/D1-V003/scopus_A01/Modeling_Control_and_Stiffness_Regulation_of_Layer_Jamming-Based_Continuum_Robots.pdf": "48c9dabde1c5c06d78f21c388c4ad713ee325a5a724d7e4cf9e2ab845c3515ae",
  "data/inbox/verification_pending/D1-V003/scopus_A01/Stiffness Change for Reconfiguration of.pdf": "dc9ad29f753d760eb4da07276315790cc07a85a531e5196bdb6b2d9716a17862",
  "data/inbox/verification_pending/D1-V003/scopus_A01/Stiffness-Tuneable Segment for Continuum Soft Robots.pdf": "7366c065fa1e83eb2aa1e4b1ec9b69c8933d1d51cff3e1b6e2bb365aedfc8fb2",
  "data/inbox/verification_pending/D1-V003/scopus_A01/A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
  "data/inbox/verification_pending/D1-V003/scopus_A01/An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
  "data/inbox/verification_pending/D1-V003/scopus_A01/A Novel Model for Layer Jamming-based Continuum Robots.pdf": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/1992-BENDING STRESS ENHANCEMENT IN MATERIALS.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/1998-A relative gradient theory for layered materials.pdf": "2f85ad579a309c4c4bebcf638f0ca18558b046d6bcb35f20ba1cedd456c57ed2",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2018-A homogenized structural model for shear deformable composites.pdf": "8113666e962127039ddfec102e4bea849b5290077935e2d5d188a9cd46361305",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2018-A homogenized structural model for shear deformable composites.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2025-Slip-mediated axisymmetric bending of multilayered structures with.pdf": "bdeedc2731e96976b82e73f23908fe40d660ca8d62c59ffcf12d6e7fe80c2769",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2014-Assessment and correction of theories for multilayered.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2025-Slip-mediated axisymmetric bending of multilayered structures with.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2022-Equivalent dynamic model of multilayered structures with imperfect interfaces.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2016-INFLUENCE OF SLIP EFFECT ON BENDING CHARACTERISTICS OF FRICTIONAL LAMINATED BEAMS.pdf": "47fe4949dc7ad5ba6d7fdfaba2d4bfe4411468518d5a9cbec20c5299e214a31a",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/1998-A relative gradient theory for layered materials.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2019-Mechanism research of slip effect between frictional laminated beams.pdf": "ee464a718b132e023b502c6bf396bc5b810e88e03980bd71f6dd9c9cc8c70a15",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2018-Bending Stiffness of Parallel Wire Cables.pdf": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2024-An analytic solution for bending of multilayered structures with.pdf": "bd5af3e26decf56c75116e0ade5f247dd736f1df312db7e1dec9aac746355b9d",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/Influence of boundary conditions on the response of.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2026-Thickness Gradient Design Enhances Bending Performance of.pdf": "7f93ab3253623c56962e13961ff66109212a7f5518e56a96e53f2f02eb61553f",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2021-Analytical model for the bending of parallel wire cables considering.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2024-An analytic solution for bending of multilayered structures with.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2018-Bending Stiffness of Parallel Wire Cables.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2020-Novel dynamic model for calculating the equivalent Young’s.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2020-Novel dynamic model for calculating the equivalent Young’s.pdf": "2d30a68b714e06a8442050923e62515199331836c282c1a04dd1cf8462a3a86c",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2026-Thickness Gradient Design Enhances Bending Performance of.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf": "ecdac26196d469aa888159e2e6479170c05fe54f559565b5335752d03233af75",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/1993-BENDING STRESS ENHANCEMENT IN MATERIALS.pdf": "66fcf766cb5039e18d54b0199494f6f32dd64293a07e1286f08c043dbe9c5b83",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2014-Assessment and correction of theories for multilayered.pdf": "33ea2034277aeb985f8c378b2972aa9040a91d6d7f90a4d3f62071b21efd7e55",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2019-Mechanism research of slip effect between frictional laminated beams.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/Influence of boundary conditions on the response of.pdf": "4994f7ed3ffc624981b57094552501da15888615a81994a8a36a11ae12301c52",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/1993-Bending stress enhancement-Part II-Unlayered shear-weak model.pdf": "f00d886124e51a93d169fa8a43c5f9edac85b1cfbcd3ca0b4a958f702d02b521",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/1993-BENDING STRESS ENHANCEMENT IN MATERIALS.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/inbox/verification_pending/D1-V004/C01_frictional_layers/2022-Equivalent dynamic model of multilayered structures with imperfect interfaces.pdf": "0f1b512cee959a3daf8635dde3aeed6c4d3c6dd17e5aabef1248032eb09e4771",
  "data/inbox/verification_pending/D1-V008/C04_named_target/2024-Ye-Analytical Solution for Bending Deformation of Steel-Concrete Composite Beams Considering Nonlinear Interfacial Slip.pdf": "53d328abaad573cca78c06c352a0e3d12ccff148a7597ff3947273297608e210",
  "data/inbox/_already_added/D1-V003_duplicates/Modeling_Control_and_Stiffness_Regulation_of_Layer_Jamming-Based_Continuum_Robots_48c9dabde1.json": "123e2a00340b0880b73bc6d21d6e501a7771b66cab42402c970d11fbd8d00e80",
  "data/inbox/_already_added/D1-V003_duplicates/Modeling_Control_and_Stiffness_Regulation_of_Layer_Jamming-Based_Continuum_Robots.pdf": "48c9dabde1c5c06d78f21c388c4ad713ee325a5a724d7e4cf9e2ab845c3515ae",
  "data/inbox/_already_added/D1-V003_scopus_A01/2025-Zhang-Continuum modeling for layer jamming structures.pdf": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
  "data/inbox/_already_added/D1-V003_scopus_A01/A-continuumbased-model-for-a-layer-jamming-beam_2025_Copernicus-Publications.pdf": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
  "data/search_exports/D1-V002/round_manifest.json": "d7d6aa048b4fce582eb0a6f1f25c50442f1445985a101fdefa8b6d0c9ef1294d",
  "data/search_exports/MP1-V002/new_13paper_chase/forward/F07.csv": "24ecf4bbe20ad5cdbb6bbd28fbbdb6b68ae400a63b85df11aa050c477803ebab",
  "data/search_exports/MP1-V002/new_13paper_chase/forward/F12.csv": "f16c115edcf90832f021524a7aec05539ef7f64dd0ebbb71e3389d3157b8163d",
  "data/search_exports/MP1-V002/new_13paper_chase/forward/F11.csv": "d56693ca56d141b1ad73135564b62ca7c684f43072cad1c344b9f3613d00f6a9",
  "data/search_exports/MP1-V002/new_13paper_chase/forward/F08.csv": "371dcb1cba466c4f0727d59e4d21ef5d891d537acdcb3951f133f347d5cd8c88",
  "data/search_exports/MP1-V002/new_13paper_chase/forward/F10.csv": "ff1d4a211e8dd41862b9868917fd814aa34ef792cf7e0349de9829a0a17ec661",
  "data/search_exports/MP1-V002/new_13paper_chase/forward/F09.csv": "27b9c8465e7be5beabff13b1c7013369dce377674d2dfb2bd180a449409b508d",
  "data/search_exports/MP1-V002/new_13paper_chase/backward/B09.csv": "46d2b934385d6d1eb4ab81eab5f1d2b8cc70f915ee8caa530817120a6f4db631",
  "data/search_exports/MP1-V002/new_13paper_chase/backward/B10.csv": "2b7dd29dba0f4f88bc436abc327ec92ac017f42e3f1b1a356ddeaf153ddb944e",
  "data/search_exports/MP1-V002/raw/forward/F08.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/forward/F12.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/forward/F09.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/forward/F11.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/forward/F02.csv": "68947b68f211151f236910a82bf69c3d8a96ef6a471b9ca06dfa94552848b684",
  "data/search_exports/MP1-V002/raw/forward/F07.csv": "24ecf4bbe20ad5cdbb6bbd28fbbdb6b68ae400a63b85df11aa050c477803ebab",
  "data/search_exports/MP1-V002/raw/forward/F01.csv": "77c6fb3c6191b63bac5e31e250d65057cec6b51b07fb2518281f2e485be11322",
  "data/search_exports/MP1-V002/raw/forward/F12.csv": "f16c115edcf90832f021524a7aec05539ef7f64dd0ebbb71e3389d3157b8163d",
  "data/search_exports/MP1-V002/raw/forward/F13.txt": "b306b068c251a04af61532a49488d7256d5a6841dbb6f9e0d72564d877cd8a2b",
  "data/search_exports/MP1-V002/raw/forward/F05_matsumoto_researchgate.txt": "eea26aae64e887677a45900de1f874c5a425e5d5308331579de4f9808466ac3d",
  "data/search_exports/MP1-V002/raw/forward/F10.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/forward/F07.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/forward/F04.csv": "d85f2d2b2232b852d1e307fa9a8ac53498de9e1c8cc8df3331ff582f3d45e19b",
  "data/search_exports/MP1-V002/raw/forward/F11.csv": "d56693ca56d141b1ad73135564b62ca7c684f43072cad1c344b9f3613d00f6a9",
  "data/search_exports/MP1-V002/raw/forward/F08.csv": "371dcb1cba466c4f0727d59e4d21ef5d891d537acdcb3951f133f347d5cd8c88",
  "data/search_exports/MP1-V002/raw/forward/F10.csv": "ff1d4a211e8dd41862b9868917fd814aa34ef792cf7e0349de9829a0a17ec661",
  "data/search_exports/MP1-V002/raw/forward/F09.csv": "27b9c8465e7be5beabff13b1c7013369dce377674d2dfb2bd180a449409b508d",
  "data/search_exports/MP1-V002/raw/forward/F06_wang_zero.txt": "8a88a38af1d326e88bcb073480241ce341f2255ee01d4ec4b23e0e1f1c51c0ac",
  "data/search_exports/MP1-V002/raw/forward/F03_zhang_yao_zero.txt": "26563d7cf2641315b75f1154c95a3f803b6a40d171a64441e718764d96a2573d",
  "data/search_exports/MP1-V002/raw/backward/B11_kang2020.csv": "a06b7834f73b82900ba6360f811facaca9436e531fd607a55cbd6f0a8fd66546",
  "data/search_exports/MP1-V002/raw/backward/B05.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B02.csv": "c599a076234d65364265c457aa9e078ec7736f90d9da28dab30cf7e154311ea4",
  "data/search_exports/MP1-V002/raw/backward/B04.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B02.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B03.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B05.csv": "74a89ffefa5c659450b7708f49324f5b2b050f8de06057569b2debc7fbb27b31",
  "data/search_exports/MP1-V002/raw/backward/B10.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B09.csv": "46d2b934385d6d1eb4ab81eab5f1d2b8cc70f915ee8caa530817120a6f4db631",
  "data/search_exports/MP1-V002/raw/backward/B10.csv": "2b7dd29dba0f4f88bc436abc327ec92ac017f42e3f1b1a356ddeaf153ddb944e",
  "data/search_exports/MP1-V002/raw/backward/B11_kang2020.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B12_barsi.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B09.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/MP1-V002/raw/backward/B01.csv": "b41a60c3738233d93849b56c79b36dd3e13af35257dcda6b6e7a8f3ce53d5031",
  "data/search_exports/MP1-V002/raw/backward/B12_barsi.csv": "d341a396ec2dda021f10301a5dd7b6e3f8ce9eb4d434ad10c3aeff177101a381",
  "data/search_exports/MP1-V002/raw/backward/B06_silva_publisher_references.txt": "be462bc2e220526811e0ba144574d1abe21d9418b60399c7fca72d8c89ef375c",
  "data/search_exports/MP1-V002/raw/backward/B04.csv": "3dc18066b1e11d4902f19c04367e24de9268c8ede27a9817e33283cfa0329233",
  "data/search_exports/MP1-V002/raw/backward/B03.csv": "36f7a62dc099c010453de9da5820439915674e53ddeb6beb52a7b970ef7cd34b",
  "data/search_exports/MP1-V002/raw/backward/B01.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/D1-V002/raw/.gitkeep": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
  "data/search_exports/D1-V005/scopus/C02/C02-R3.csv": "73c4d704adab9034275b5bff1668032dc92b794a5ff2b4761375dcf4203482be",
  "data/search_exports/D1-V005/scopus/C02/C02-R1-2.csv": "9ff70aa5abfc45678bb9dc2b708335621ecffc31e4d5c0591970fbc76aeef179",
  "data/search_exports/D1-V005/scopus/C02/C02-R2.csv": "53b2839b4220bd667a106e5edf12170036f91d29ac8bf003026db3f4c201a37c",
  "data/search_exports/D1-V005/scopus/C02/C02-R4.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/D1-V005/scopus/C02/C02-R1-2.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/D1-V005/scopus/C02/C02-R1-1.csv": "bbbdda7cf5b0cad634859bb256cfa848cc33862d4750d1c5253b75586fcda308",
  "data/search_exports/D1-V005/scopus/C02/C02-R3.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/D1-V005/scopus/C02/C02-R2.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/D1-V005/scopus/C02/C02-R1-1.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "data/search_exports/D1-V005/scopus/C02/C02-R4.csv": "c4b2de7a99c264d40c3fa1b9db95e48df68965d76244a7075611e323aa180490",
  "data/final/MP1/README.md": "036588c3c273642e9f3c105c0a58bf9f29a2539f25ba344bb6737ed1f7875745",
  "data/final/MP1/MP1_EVIDENCE_EXTRACTION_MATRIX.xlsx": "e8c96976dd0c8f47634bfd4ca086c7dd330560f54f4cb4eb525c4137006af92b",
  "data/final/MP1/manifest.json": "8053a43dfb85d6ee7c35cb995b21efb99faac729e0e15d8d83549b48055ba45b",
  "data/final/MP1/annotated/A2-2023-Superelasticity SMA cables and its simplified FE model_annotated.pdf": "0e6c41754b067956bec8349912cd3634d24ff45df4386929020dd09a2b614974",
  "data/final/MP1/annotated/2025-A new mechanical model of short wire ropes Theory and experimental_annotated.pdf": "688940afb124b119d6331dce32184b341076828dde67daf443f1b8dd42690a97",
  "data/final/MP1/annotated/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_annotated.pdf": "c8440a01b2f0b994155ea02af61e76b4c2ea41d1a5859c9d4297d61e37579f4a",
  "data/final/MP1/annotated/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_annotated.pdf": "935b25db65ec8b8ed1d023b28fa8896ea6bf6dc7582a26ff951039d513cbdb15",
  "data/final/MP1/annotated/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_annotated.pdf": "f9238cf57f389f513b6bc61c20f686436fee5dca1f5c9143c3aa5879de14b61d",
  "data/final/MP1/annotated/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_annotated.pdf": "d1e99630096e91fdc4a721b0ee39ff0b6d65d79cc0d69faffb7e7c088914242c",
  "data/final/MP1/annotated/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_annotated.pdf": "615f0a508013c110bcf05c95616766589896ac33115c058355765989653421a0",
  "data/final/MP1/annotated/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_annotated.pdf": "f2f4e2d97beaf19d67c83c1f5aad8f5ffe075d60a751ad1eea0fdf788baca9e7",
  "data/final/MP1/annotated/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_annotated.pdf": "93e2fbfdfc4401a11a5c56a215d6cf82108379643c3476c760629fbb3ab2a7ec",
  "data/final/MP1/annotated/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_annotated.pdf": "5addce512f16ff5d4b71aeffff6bae95fa9c86608b1265ad8f9086ff26bfa4b8",
  "data/final/MP1/annotated/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_annotated.pdf": "69f74982cfaceab4028fe3daeeb084bbd30ec3c0d6ddd13bb7381bb6739fdb72",
  "data/final/MP1/annotated/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_annotated.pdf": "eb867e283c0e574128ce76407ea46f7caaca09420f674036fef128d4b794fdff",
  "data/final/MP1/annotated/A5-Cable vibration considering internal friction_annotated.pdf": "9e4baf770dc79b6ba8e6daad683155996bef23ccfa6b2421ac3f94c3f790f3f9",
  "data/final/MP1/annotated/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_annotated.pdf": "2b910f865781a68b8ee0174c3dc20231b08901330cf4e6639d8e4509e4de0e81",
  "data/final/MP1/annotated/annotation_manifest.json": "2c1e27725209b1ce92cd58285c73c6f3dee09700ae2f9e707777850d6d5b7325",
  "data/final/MP1/annotated/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_annotated.pdf": "14897fe0ee0048d05ae8dfb5afe8df798dbdb902c4faea7a3e1a9c8d385143cd",
  "data/final/MP1/annotated/A3-2022-Mechanical response of single and double-helix_annotated.pdf": "8a15439b954f8b938fb38e359e6e3e625a033ec75a811eb1fe5ea24db535d4c8",
  "data/final/MP1/annotated/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_annotated.pdf": "0c6a511e92d5556cbfc1b4796c86df628cd1e311d975913726fdb9d8ce0f8615",
  "data/final/MP1/annotated/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_annotated.pdf": "f470c4ea02611439dae1cc7621c40bc6dd6c1144aa8fceaeee5c9a159377d8e0",
  "data/final/MP1/annotated/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_annotated.pdf": "e1ed3ad98103b2646151e1bdfe4778bf6f4b888766c1b21b532e107b564e664f",
  "data/final/MP1/annotated/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_annotated.pdf": "3ae33da86574172cbfe471437ea5d0c0d0b008670a42e7f006cbbebf928a8fba",
  "data/final/MP1/annotated/A1-2015-Hysteresis of Multiconfiguration Assemblies of_annotated.pdf": "f68c568a94901e6b61f60ddfc43ab00e4c3c7bee6433511fe9fd06ba43aa81f6",
  "data/final/MP1/annotated/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _annotated.pdf": "4208587a9dceb44354dc8a722ab6e5b76713042061701b41905d96c1e898d3cf",
  "data/final/MP1/annotated/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_annotated.pdf": "62ebf6f804b50c7ff26164560ec5bca2b088d054be124d91fab8f9e2bf6b0b58",
  "data/final/MP1/annotated/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_annotated.pdf": "6228dceebe323ecd29510565369a1d3533a7ce39516e4fa625d8e191806611ca",
  "data/final/MP1/annotated/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_annotated.pdf": "a9b4ec1387584d1b162ad23b31d45048731d3bf31fcc7ccc10727077145d4916",
  "data/final/MP1/annotated/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_annotated.pdf": "0547cb4fc9e97e767b8938cec7ceb5ee11b2c0cc14e73c673c3c8f147df5419a",
  "data/final/MP1/annotated/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_annotated.pdf": "19cb4cf8fefff0bfb3e36568c5b60d219c4b8a652d21a8c543bc17352f06f645",
  "data/final/MP1/05_remediation/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/05_remediation/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/05_remediation/README.md": "1c0d22722ac857a5b0dd2f62e89a3ecb7fa456901c86c784d6888ba103033616",
  "data/final/MP1/05_remediation/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/05_remediation/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/05_remediation/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/05_remediation/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/05_remediation/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/05_remediation/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/05_remediation/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/05_remediation/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/05_remediation/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/05_remediation/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/05_remediation/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/05_remediation/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/05_remediation/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/05_remediation/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/05_remediation/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/05_remediation/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/05_remediation/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/05_remediation/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/05_remediation/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/05_remediation/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/05_remediation/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/05_remediation/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/05_remediation/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/05_remediation/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/05_remediation/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/05_remediation/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/05_remediation/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/05_remediation/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/05_remediation/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/05_remediation/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/05_remediation/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/05_remediation/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/05_remediation/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/05_remediation/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/05_remediation/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/05_remediation/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/05_remediation/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/05_remediation/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/05_remediation/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/05_remediation/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/05_remediation/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/05_remediation/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/04_astra_critique/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/04_astra_critique/README.md": "fe645168789ccb8122383703dd4b7a19f2503bbe9dc0d8723f6738bc75ba6e40",
  "data/final/MP1/04_astra_critique/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/04_astra_critique/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/04_astra_critique/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/04_astra_critique/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/04_astra_critique/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/04_astra_critique/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/04_astra_critique/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/04_astra_critique/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/04_astra_critique/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/04_astra_critique/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/04_astra_critique/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/04_astra_critique/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/04_astra_critique/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/04_astra_critique/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/04_astra_critique/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/04_astra_critique/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/04_astra_critique/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/04_astra_critique/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/04_astra_critique/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/04_astra_critique/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/04_astra_critique/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/04_astra_critique/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/04_astra_critique/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/04_astra_critique/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/04_astra_critique/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/04_astra_critique/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/04_astra_critique/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/03_trace_packets/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/03_trace_packets/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/03_trace_packets/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/03_trace_packets/README.md": "8f97fba754d2dc9046fd612995ebae9711a338de5dbd91e3cd50b9a0840be28f",
  "data/final/MP1/03_trace_packets/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/03_trace_packets/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/03_trace_packets/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/03_trace_packets/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/03_trace_packets/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/03_trace_packets/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/03_trace_packets/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/03_trace_packets/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/03_trace_packets/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/03_trace_packets/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/03_trace_packets/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/03_trace_packets/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/03_trace_packets/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/03_trace_packets/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/03_trace_packets/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/03_trace_packets/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/03_trace_packets/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/03_trace_packets/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/03_trace_packets/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/03_trace_packets/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/03_trace_packets/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/03_trace_packets/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/03_trace_packets/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/03_trace_packets/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/03_trace_packets/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/03_trace_packets/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/03_trace_packets/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/03_trace_packets/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/03_trace_packets/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/03_trace_packets/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/03_trace_packets/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/03_trace_packets/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/03_trace_packets/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/03_trace_packets/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/03_trace_packets/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/03_trace_packets/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/03_trace_packets/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/03_trace_packets/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/03_trace_packets/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/03_trace_packets/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/03_trace_packets/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/03_trace_packets/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/03_trace_packets/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/03_trace_packets/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/03_trace_packets/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/08_current_reports/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/08_current_reports/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/08_current_reports/2013_extracted_text.txt": "8e2d89d9ebae738ade5f53fd2fd881ef862a628e7137addf81480bee424cfdfa",
  "data/final/MP1/08_current_reports/README.md": "42ab1c89c768ec17d3e27f781141d15eb08c5fd2cc782c1c6ac472a29ed9ae7b",
  "data/final/MP1/08_current_reports/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/08_current_reports/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/08_current_reports/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/08_current_reports/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/08_current_reports/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/08_current_reports/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/08_current_reports/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/08_current_reports/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/08_current_reports/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/08_current_reports/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/08_current_reports/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/08_current_reports/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/08_current_reports/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/08_current_reports/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/08_current_reports/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/08_current_reports/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/08_current_reports/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/08_current_reports/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/08_current_reports/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/08_current_reports/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/08_current_reports/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/08_current_reports/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/08_current_reports/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/08_current_reports/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/08_current_reports/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/08_current_reports/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/08_current_reports/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/08_current_reports/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/08_current_reports/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/08_current_reports/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/08_current_reports/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/08_current_reports/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/08_current_reports/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/08_current_reports/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/08_current_reports/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/08_current_reports/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/08_current_reports/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/08_current_reports/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/08_current_reports/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/08_current_reports/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/08_current_reports/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/08_current_reports/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/08_current_reports/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/08_current_reports/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/MP1-V002/canonical/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/MP1-V002/canonical/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/MP1-V002/canonical/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V002/canonical/README.md": "418f051ad8ad0c7e42d3a94e99dcc62760445104a6bc9de84b56b5ad1b486cb0",
  "data/final/MP1/MP1-V002/canonical/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/MP1-V002/canonical/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/MP1-V002/canonical/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/MP1-V002/canonical/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/MP1-V002/canonical/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V002/canonical/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/MP1-V002/canonical/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V002/canonical/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/MP1-V002/canonical/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V002/canonical/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/MP1-V002/canonical/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V002/canonical/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/MP1-V002/canonical/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/MP1-V002/canonical/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/MP1-V002/canonical/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/MP1-V002/canonical/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/MP1-V002/canonical/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V002/canonical/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/MP1-V002/canonical/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/MP1-V002/canonical/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/MP1-V002/canonical/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/MP1-V002/canonical/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/MP1-V002/canonical/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/MP1-V002/canonical/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/MP1-V002/canonical/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/MP1-V002/canonical/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V002/canonical/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/MP1-V002/canonical/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/MP1-V002/canonical/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/MP1-V002/canonical/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/MP1-V002/canonical/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/MP1-V002/canonical/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V002/canonical/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V002/canonical/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/MP1-V002/canonical/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V002/canonical/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/MP1-V002/canonical/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/MP1-V002/canonical/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/MP1-V002/canonical/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/MP1-V002/canonical/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V002/canonical/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/README.md": "a796b952d3d03012c86a5dff2fa2c31719a4146305a2d02c3dc6b0fb9b01eaa3",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V002/runs/20260924T114158Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/README.md": "ea94201478f5ec1a23fa6d3b73c46dc23b9602f61179a608a97d11afd4ecb6db",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V002/runs/20260925T064146Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/README.md": "5278d026af8a3228134ec207b3c8a3cf34e5896fe10c99791fbe3b1705e76df1",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V002/runs/20260925T093414Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/README.md": "82676afcffc2e749762f6063c665e4215b9fccdbd49f481f8e5cf5db31f567fe",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V002/runs/20260925T090319Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/README.md": "f17e9e7c64ef4715a5218a14f72100284886a265608a895ba0a1f290502345e8",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V002/runs/20260924T171216Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/07_WR1/S02/README.md": "4052a4461dae671b1cf1c9d5da6dbc70fcddec73646496d0084d6444a61389e0",
  "data/final/MP1/07_WR1/S02/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/07_WR1/S02/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/07_WR1/routing/README.md": "2fd78e2a182be1e14f5685125671ffd89baed7e7cde97d2714dcea7dbf29e160",
  "data/final/MP1/07_WR1/routing/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/07_WR1/routing/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/07_WR1/routing/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/07_WR1/routing/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/07_WR1/routing/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/07_WR1/routing/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/07_WR1/routing/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/07_WR1/routing/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/07_WR1/routing/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/07_WR1/routing/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/07_WR1/S01/README.md": "b49c4611a6b23c24481008cf0266153964fdd4294b6246b6d1377f01038f34de",
  "data/final/MP1/07_WR1/S01/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/07_WR1/S01/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/07_WR1/S01/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/07_WR1/S01/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/07_WR1/S01/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/07_WR1/S01/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/07_WR1/S01/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/07_WR1/S01/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/07_WR1/S01/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/07_WR1/S01/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/MP1-V001/canonical/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V001/canonical/README.md": "493cdc5aa1a0f6eb207c5d244cb2482770c3054abf6385df37817e0bdd46f3af",
  "data/final/MP1/MP1-V001/canonical/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V001/canonical/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V001/canonical/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V001/canonical/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V001/canonical/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V001/canonical/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V001/canonical/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V001/canonical/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V001/canonical/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V001/canonical/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V001/canonical/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V001/canonical/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V001/canonical/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V001/canonical/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V001/canonical/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V001/canonical/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V001/canonical/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V001/canonical/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V001/canonical/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V001/canonical/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V001/canonical/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/README.md": "2484f43b033ba66c17868b364ab762606368c0ccd421c205cd8d1f34dd7b33e0",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/MP1-V001/runs/20260922T055150Z/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/06_W02/W2-02/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-02/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-02/README.md": "8f6ef50d61454af26ae2ffcb48bb2938adc5df6f8ae98cf1d8a24d287ca0dde3",
  "data/final/MP1/06_W02/W2-02/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/06_W02/W2-02/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-02/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-02/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/06_W02/W2-02/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/06_W02/W2-02/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-02/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/06_W02/W2-02/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-02/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/06_W02/W2-02/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-02/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/06_W02/W2-02/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-02/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-02/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/06_W02/W2-02/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-02/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-02/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/06_W02/W2-02/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/06_W02/W2-02/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-02/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-02/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-02/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/06_W02/W2-02/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-02/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-02/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-02/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-02/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/06_W02/W2-02/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-02/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-02/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/06_W02/W2-02/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-02/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-02/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/06_W02/W2-02/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-02/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/06_W02/W2-02/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-02/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-02/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/06_W02/W2-02/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/06_W02/W2-02/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-02/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/06_W02/W2-02/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/06_W02/W2-07/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-07/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-07/README.md": "6c67e33289f6a575e2327dae5baa23d2343f79de29b5c7e62d04b38928e756e0",
  "data/final/MP1/06_W02/W2-07/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-07/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/06_W02/W2-07/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-07/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-07/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/06_W02/W2-07/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/06_W02/W2-07/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-07/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/06_W02/W2-07/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-07/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/06_W02/W2-07/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2-07/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-07/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/06_W02/W2-07/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-07/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-07/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/06_W02/W2-07/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-07/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-07/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-07/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-07/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-07/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-07/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/06_W02/W2-07/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-07/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-07/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-07/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-07/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-07/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-07/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/06_W02/W2-07/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-07/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-07/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2-07/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-07/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/06_W02/W2-07/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-07/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-07/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/06_W02/W2-07/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/06_W02/W2-07/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-07/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/06_W02/W2-07/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/06_W02/W2-05/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-05/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-05/README.md": "1f556c055f32daef62f33d0b8301a90b19c913863e23d51f852d8cf56075df7c",
  "data/final/MP1/06_W02/W2-05/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-05/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-05/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-05/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/06_W02/W2-05/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-05/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/06_W02/W2-05/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/06_W02/W2-05/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-05/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/06_W02/W2-05/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2-05/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-05/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/06_W02/W2-05/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-05/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-05/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-05/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-05/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/06_W02/W2-05/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-05/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/06_W02/W2-05/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-05/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-05/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-05/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-05/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-05/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-05/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-05/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-05/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-05/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/06_W02/W2-05/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-05/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-05/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2-05/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/06_W02/W2-05/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-05/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/06_W02/W2-05/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-05/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-05/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/06_W02/W2-05/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/06_W02/W2-05/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-08/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/06_W02/W2-08/README.md": "0d66ef36ec852172a3586594cf867618c7696acb1181c764d7ce2348ecd54936",
  "data/final/MP1/06_W02/W2-08/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-08/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-08/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/06_W02/W2-08/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-08/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-08/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-08/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-08/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-08/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-08/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-08/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-08/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-08/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-08/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-08/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-08/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-08/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-08/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-08/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-08/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-08/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-06/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/06_W02/W2-06/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-06/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-06/README.md": "cc21670c7ee3abe1d5ad8a816f4565df47e24e3d894ecd044fb0a4159588b97e",
  "data/final/MP1/06_W02/W2-06/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/06_W02/W2-06/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-06/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/06_W02/W2-06/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-06/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-06/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/06_W02/W2-06/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/06_W02/W2-06/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/06_W02/W2-06/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-06/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/06_W02/W2-06/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/06_W02/W2-06/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-06/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/06_W02/W2-06/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2-06/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-06/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "d3b3b6963f6db95a7f1715b4aae26d7fc4309ddee186e7858bd74e86151c5bba",
  "data/final/MP1/06_W02/W2-06/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-06/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-06/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/06_W02/W2-06/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-06/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-06/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/06_W02/W2-06/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/06_W02/W2-06/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-06/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/06_W02/W2-06/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-06/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-06/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-06/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/06_W02/W2-06/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-06/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-06/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-06/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-06/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/06_W02/W2-06/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-06/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/06_W02/W2-06/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-06/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/06_W02/W2-06/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-06/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-06/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2-06/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/06_W02/W2-06/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-06/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json": "b46699d0e772885229291ab3f1a1e8bc3440115850a3769ecea813bc2d0a47cb",
  "data/final/MP1/06_W02/W2-06/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-06/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-06/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf": "99fe24da8b41e8f4aa75bd0fba43f3cba0d6ef7621d800d45f7d3eabba4b7592",
  "data/final/MP1/06_W02/W2-06/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json": "9f2f6e599cf23d41b6307ee491ed8f3d856a6d15eb24d4c144576a304aa62f07",
  "data/final/MP1/06_W02/W2-06/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-06/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/06_W02/W2-06/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/06_W02/W2-09/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/06_W02/W2-09/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-09/README.md": "57965906af6559111ad10f3b125716b9edb8d04f0e2df5b69ff23331294685c1",
  "data/final/MP1/06_W02/W2-09/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/06_W02/W2-09/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-09/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json": "6fb8b2acd83b1f53e7941b461b2bbb37e4624720d5aaaa8c664860eddd789a90",
  "data/final/MP1/06_W02/W2-09/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-09/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-09/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/06_W02/W2-09/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/06_W02/W2-09/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-09/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/06_W02/W2-09/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-09/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/06_W02/W2-09/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2-09/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-09/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-09/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-09/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "data/final/MP1/06_W02/W2-09/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-09/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-09/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/06_W02/W2-09/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/06_W02/W2-09/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-09/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/06_W02/W2-09/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-09/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-09/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-09/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-09/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-09/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-09/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-09/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/06_W02/W2-09/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-09/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/06_W02/W2-09/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-09/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-09/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-09/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2-09/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/06_W02/W2-09/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-09/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-09/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-09/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/06_W02/W2-09/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/06_W02/W2-04/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/06_W02/W2-04/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-04/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-04/README.md": "387e08f9dffba9d857e24456194add7ceb926c3c6607348923fa2ac17cd21f33",
  "data/final/MP1/06_W02/W2-04/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/06_W02/W2-04/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-04/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-04/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-04/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/06_W02/W2-04/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-04/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/06_W02/W2-04/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-04/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2-04/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-04/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-04/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-04/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-04/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-04/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/06_W02/W2-04/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/06_W02/W2-04/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-04/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/06_W02/W2-04/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-04/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-04/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-04/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-04/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-04/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-04/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-04/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/06_W02/W2-04/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-04/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/06_W02/W2-04/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-04/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-04/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-04/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2-04/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/06_W02/W2-04/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-04/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-04/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-04/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-03/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-03/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-03/README.md": "27fb33f7d2833a1b4dccca00a92f52bd8224e658b13595a5070a2dcdcb43c5a9",
  "data/final/MP1/06_W02/W2-03/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/06_W02/W2-03/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-03/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2-03/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-03/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-03/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-03/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-03/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-03/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-03/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-03/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2-03/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-03/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-03/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-03/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-03/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-03/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/06_W02/W2-03/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-03/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-03/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-03/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-03/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf": "9e15094d685bf8ee21ad0b5fa9e67b3fccb0a33dc2ef5d7c9cbd47d6eca26d89",
  "data/final/MP1/06_W02/W2/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2/README.md": "7c5f030e179574e1efb8d31938d3980d611faf9d6be2b288be41e890a40beece",
  "data/final/MP1/06_W02/W2/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "data/final/MP1/06_W02/W2/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "data/final/MP1/06_W02/W2/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "data/final/MP1/06_W02/W2/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json": "23e54891153ca0d9ad4d11b99744c991700990513ff2d4c56b198f7de826008d",
  "data/final/MP1/06_W02/W2/A2-2023-Superelasticity SMA cables and its simplified FE model_9e15094d68.json": "a8eb999c9d62627c4e43a31174e5ef57e0bd9222b815258186f1c20f85e92ac4",
  "data/final/MP1/06_W02/W2/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf": "7f3f45407f507d3afacef392a99869a274865a8f0575e2fb5e9f7217202b462f",
  "data/final/MP1/06_W02/W2/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/06_W02/W2/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "data/final/MP1/06_W02/W2/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/06_W02/W2/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation_7f3f45407f.json": "d1acfb37ba1dc62f7c0fbce35422a7ff930ae5746710e58f3ac4520ebeadfb82",
  "data/final/MP1/06_W02/W2/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments_e8462758c3.json": "aeccd1af9e38827876245e0b07133abbee811fcc987fb94cbb074d633f8666de",
  "data/final/MP1/06_W02/W2/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses_fac21c950e.json": "6a02d4ca1f55e54d0f5695fbcfd996b10cbb31ebe2ca8fc132d08e1208ac79d6",
  "data/final/MP1/06_W02/W2/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json": "432483b6472032a9c6a4cac72ee4bfdd79f07d38cfd41f7d1644e8382c42daf8",
  "data/final/MP1/06_W02/W2/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/06_W02/W2/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments_00414aac4b.json": "c479fea3843f41a465d1e42ec5f402ba592584f3e02582b3ef13ec3abb774347",
  "data/final/MP1/06_W02/W2/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/06_W02/W2/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "data/final/MP1/06_W02/W2/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/06_W02/W2/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "data/final/MP1/06_W02/W2-01/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "data/final/MP1/06_W02/W2-01/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "data/final/MP1/06_W02/W2-01/README.md": "c4c4ed574059abb4630183cf8318b804bfe53fffe6fb4023099438b5cfadc732",
  "data/final/MP1/06_W02/W2-01/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application_2f7fcf2f8f.json": "187dfe2082fdae174ee021f7da5b31972f363f809aae1e0fa6bc19c910fd3e03",
  "data/final/MP1/06_W02/W2-01/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments_40760daa02.json": "82f5baf48bfdb3376d7004a1df386fd58ec2cf90d992a69f32d8f58db6b50326",
  "data/final/MP1/06_W02/W2-01/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "data/final/MP1/06_W02/W2-01/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf": "c6a31066f8e708594fe87ab5f0e8a072cfdab840f81917017db0371d72c48d1c",
  "data/final/MP1/06_W02/W2-01/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf": "6dd1ca94d1a4bef674d5382f74bc6ef6e1444e86cbfa870836db459ff056dcc2",
  "data/final/MP1/06_W02/W2-01/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf": "98fee47c04dc25f6d590e9a5481b901a96588395fe1678e3273ddf2fe9f64827",
  "data/final/MP1/06_W02/W2-01/2025-A new mechanical model of short wire ropes Theory and experimental_9f4295be23.json": "c58bd9a7385cbe6a0269938d456ec518a746139490746c32ad5c3f179c986b9f",
  "data/final/MP1/06_W02/W2-01/A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "data/final/MP1/06_W02/W2-01/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf": "ccdc1bb980abdaab2d8a3d7b2cc088ac7b5855f9137bef5c93a6a8d96fb70667",
  "data/final/MP1/06_W02/W2-01/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy _56793dea9b.json": "243a6b842a1e3fb2ff4c5c25560147955ffd918cccccc28c6531d13a9b1fa427",
  "data/final/MP1/06_W02/W2-01/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json": "7d7fb683184f9802261c999d1c99b3a25f70238067c46f7e615b66d3109d56de",
  "data/final/MP1/06_W02/W2-01/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes_1c81b2d35c.json": "26e6de12bd262db4d7b85d434f64286514d07f810b55afa3376f3febd5b3a7f5",
  "data/final/MP1/06_W02/W2-01/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf": "2f7fcf2f8f3fa43fc28f176f436243ed577e970f2caeaf2f4302c10b130c9248",
  "data/final/MP1/06_W02/W2-01/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf": "d9966f2f5e9d44133bbeccb28d897ec4d4998308c9fcce9a8987029dc27926d2",
  "data/final/MP1/06_W02/W2-01/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings_6dd1ca94d1.json": "e1ab8baa391c624da12a27236ef2986cb9b88dfc91dc95e27b751f97c46bfea1",
  "data/final/MP1/06_W02/W2-01/A5-Cable vibration considering internal friction_aaad9c248c.json": "94978d0e70230607ab0074f281cacf4ca3281781494688184846c732f6ed33ff",
  "data/final/MP1/06_W02/W2-01/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json": "14ca022a77698b7ac09f302c2859a1f9eecd5870de112c202a7be0bf51457568",
  "data/final/MP1/06_W02/W2-01/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable_ccdc1bb980.json": "d76cf94bc9c52c314012ba0c29819d50706c78dedd506dcb9b098b1f48a7ff46",
  "data/final/MP1/06_W02/W2-01/A1-2015-Hysteresis of Multiconfiguration Assemblies of_d9966f2f5e.json": "428225882756769b672ef4fc1893ee0572aac86966557a5f4cabcba118694686",
  "data/final/MP1/06_W02/W2-01/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "data/final/MP1/06_W02/W2-01/A3-2022-Mechanical response of single and double-helix_53200aa0c6.json": "9217adeec8be7c970fa86775d19678c914fa6677c2237e7541ad27d73255925c",
  "data/final/MP1/06_W02/W2-01/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "data/final/MP1/06_W02/W2-01/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json": "677f03b1ed3a3ade455726e5742fc06be0a3c42989e47cded5d46e3a12d2ed3b",
  "data/final/MP1/06_W02/W2-01/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "data/final/MP1/06_W02/W2-01/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "data/final/MP1/06_W02/W2-01/A4-2021-Nonlinear vibration isolation via a nitinol wire rope_98fee47c04.json": "b440a0aa8c996782b1f1d34d4966ae085f935d4c45ad2705bcc2d995abd0a69a",
  "data/final/MP1/06_W02/W2-01/A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "data/final/MP1/06_W02/W2-01/2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "data/final/MP1/06_W02/W2-01/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json": "a9e6624d5884c4a65bf905baa504b88c8851dd7ec2c39418fa04c037bdcf5a1f",
  "data/final/MP1/06_W02/W2-01/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json": "1cd6afddf50c717e281f3168d3e4376c96332b81a3eb34d7f37733ae938a28bd",
  "data/final/MP1/06_W02/W2-01/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json": "e1b89a145fb2213937bc43faf03808dbe469309e2c109c51129dca6d1642042a",
  "data/final/MP1/06_W02/W2-01/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
  "literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
  "literature review/new citation/10.2024-Caro-A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
  "literature review/new citation/3.2023-Russo-Continuum Robots  An Overview.pdf": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
  "literature review/new citation/4.2021-Li-Current Trends and Prospects in Compliant Continuum Robots A Survey.pdf": "338056376b3e25d6dac13994570610571142ef24213bed3807dd32bdf1390016",
  "literature review/new citation/7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
  "literature review/new citation/2026-Zhang-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "literature review/new citation/2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
  "literature review/new citation/6.2022-Dupont-Continuum_Robots_for_Medical_Interventions.pdf": "905b1cb1a5d192bf0b4d9feef9324d99144ee062309a50cc1ceda20d7435dd7a",
  "literature review/new citation/9.2011-mahvash-Stiffness Control of Surgical Continuum Manipulators.pdf": "72249375e9a21db6ed500f9b3eb837a82baa5fb542de5705f2f9e8dc26fbba32",
  "literature review/new citation/8.2020-jiang-A variable‐stiffness continuum manipulators by an SMA‐based sheath in minimally invasive surgery.pdf": "fc4cd87202f5c612de3c0b3fd7c6097c20e8786e9eda88bc717e89ca8648c381",
  "literature review/new citation/1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
  "literature review/new citation/5.2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json": "36b7b49ff64b8602b226910cf453300d20b48c06fdfa60ecfdca159144cb4dfc",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json": "d52c08d9e0e1c88aaacff3dbfb10cca36c7d697f35b1f5e82d1fad878e352435",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md": "553565b7b2ed845b9dee0498e33e76945774b3624c68965c697aeaf5ab201131",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json": "4dd795268add05f98f77e0a65d054f36b93f0f079bba8e39d77d4f9c2d5d4e0c",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json": "037ad67fd0750c2506b21a1d39866fa996889e5e40005f81ac0fbd9bc79aea84",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json": "8796514d2cafbc94867d0ee87da7c3211f45d3a466eceace54c79dca14465f51",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip": "d2128a711f4c3a2be4bb0841415f532413c462a0aeafed0b3321d7f3713194b3",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md": "4c1e0e93c9b1dcabc6a17eeebb80f113a1689019fd664f0399497a13236a7d9f",
  "literature review/new citation/2.Độ mềm dẻo giúp tiếp cận không gian hẹp, tiếp xúc an toàn/2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
  "literature review/new citation/2.Độ mềm dẻo giúp tiếp cận không gian hẹp, tiếp xúc an toàn/2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
  "literature review/new citation/2.Độ mềm dẻo giúp tiếp cận không gian hẹp, tiếp xúc an toàn/2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/2.Độ mềm dẻo giúp tiếp cận không gian hẹp, tiếp xúc an toàn/2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/5.Nhu cầu phát triển variable stiffness/2021-Li-Current Trends and Prospects in Compliant Continuum Robots A Survey.pdf": "338056376b3e25d6dac13994570610571142ef24213bed3807dd32bdf1390016",
  "literature review/new citation/5.Nhu cầu phát triển variable stiffness/2021-Li-Current Trends and Prospects in Compliant Continuum Robots A Survey.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/3.Độ mềm dẻo dẫn đến hạn chế về độ cứng và chịu tải/3.2023-Russo-Continuum Robots  An Overview.pdf": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
  "literature review/new citation/3.Độ mềm dẻo dẫn đến hạn chế về độ cứng và chịu tải/2024-Fan-An overview of stiffening approaches for continuum robots.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/3.Độ mềm dẻo dẫn đến hạn chế về độ cứng và chịu tải/2024-Fan-An overview of stiffening approaches for continuum robots.pdf": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
  "literature review/new citation/3.Độ mềm dẻo dẫn đến hạn chế về độ cứng và chịu tải/3.2023-Russo-Continuum Robots  An Overview.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/1.Giới thiệu cấu tạo và đặc tính Continuum Robotics/2023-Russo-Continuum Robots  An Overview.pdf": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
  "literature review/new citation/1.Giới thiệu cấu tạo và đặc tính Continuum Robotics/2023-Russo-Continuum Robots  An Overview.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/1.Giới thiệu cấu tạo và đặc tính Continuum Robotics/2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
  "literature review/new citation/1.Giới thiệu cấu tạo và đặc tính Continuum Robotics/2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/6.Tăng độ cứng bằng ma sát giữa các sợi/2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/6.Tăng độ cứng bằng ma sát giữa các sợi/2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json": "c26a9c15561b3f9c58d175f4197e074b7a833faa9533cf6f9240f302cea497a2",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[1]_Russo_2023_TRACED.pdf": "58bd7c54cc7c2bd67e4e239464341a805b0f823beccf72d23311fb89e5c5b7d6",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[4]_Dupont_2022_TRACED.pdf": "738647681749abfc42345060b3f287cb50b61cc7911bd8ee9d003850b78d045d",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[5]_Lin_2024_TRACED.pdf": "c3ac71b0488882030c1fc262abe471405b04e3d7d2934c684dcd006ee9aed0a6",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[7]_Fan_2024_TRACED.pdf": "2f0d6e60d3897058d271046d6a9e1d151871164025c64d19eef7550a971bf39c",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[3]_Burgner_Kahrs_2015_TRACED.pdf": "a7ea7a578002fb0884595cb13f181c16d86c70218e0b01ea9ad2cfb65a3f9908",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[6]_Li_Hao_2021_TRACED.pdf": "73706baf59995cdc15e51d3b09b8a6a8fc7e6e1e6c092780998008729ca5addc",
  "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/[2]_Mahvash_Dupont_2011_TRACED.pdf": "ac3a3e4331c708b655e22eb3189bf4e06bc6d146afef11097bf63f348330e4f0",
  "literature review/new citation/4.Cần ổn định vị trí và truyền lực trong thao tác/2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
  "literature review/new citation/4.Cần ổn định vị trí và truyền lực trong thao tác/2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/4.Cần ổn định vị trí và truyền lực trong thao tác/2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/4.Cần ổn định vị trí và truyền lực trong thao tác/2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
  "literature review/new citation/7.Sử dụng SMA trong cơ cấu thay đổi độ cứng/2020-jiang-A variable‐stiffness continuum manipulators by an SMA‐based sheath in minimally invasive surgery.pdf:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "literature review/new citation/7.Sử dụng SMA trong cơ cấu thay đổi độ cứng/2020-jiang-A variable‐stiffness continuum manipulators by an SMA‐based sheath in minimally invasive surgery.pdf": "fc4cd87202f5c612de3c0b3fd7c6097c20e8786e9eda88bc717e89ca8648c381",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/Avariable stiffness omnidirectional chain based on.pdf": "050cfd250a9a69ae8d9ee05d6256c09cfaeff86d823813329ba42183d1745899",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/12_S05a_HIGHLIGHTED.pdf": "a4e33627271ec920f8087c8859d060eda2da44266a42e20d2a13bdee13f3fbeb",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/Detachable Soft Actuators with Tunable Stiffness Based on.pdf": "7a1ec6cea0c208afb8b20f4c133d7ba82bd45ca61818b7980d6f58ee73c68614",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/15_S07_HIGHLIGHTED.pdf": "320e60ed721e5c3958c8fcc7aad6b5a5a597f85af208eb1faa8b251899a76d43",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/07_V-W02_HIGHLIGHTED.pdf": "c4d4c8f0ddcf0153ed76bab8734bdda8c2c999130bded6a1ce6dfe278da66b04",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/10_S04_HIGHLIGHTED.pdf": "5fc7489435d30929e13618fd6a50e7900fdfa1d4f17ae2b33aded499530dd41e",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/09_S17_HIGHLIGHTED.pdf": "565aef36b778d40002a34bbb2d4e37d37550b7d9989c799d86fa74384cd2179a",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/08_S13_HIGHLIGHTED.pdf": "12f2c804973dce36be604a88f2f58c016550c6c05161db26a9b72eb79ffcd667",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/Nonlinear Vibration Absorber with Pinched Hysteresis.pdf": "f3a57e04af12bc5857ef7ded15d738e5a3b37ad644c4d470124bd36e87e137ff",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/13_S05b_HIGHLIGHTED.pdf": "693371640d2e44adb1396189475040703e0c6ddf0944966b30db57fd86fec42e",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/06_S06_HIGHLIGHTED.pdf": "51842107d265f973957f9631315c838aa0f8f3edcae8e2e8366e41fdf40360bd",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/14_S09_HIGHLIGHTED.pdf": "c31858dae95b4e9601988f2d9ba25d69b95b4b388e0932e611d5fe3df71b19fb",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/11_S22_HIGHLIGHTED.pdf": "db56da5f359375d2cc930979e529ab206849abb69de4c17b83da5b8376bcd32b",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/A continuum-based model for a layer jamming beam.pdf": "da6a4d0f3b10bce4376425275d64c48f3d62c4fcc395bf4bec9674d65c860d76",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/Soft actuator with switchable stiffness using a micropump-activated .pdf": "794f85ea599086819ddfc18185cb868d608d73630d56d0d6716dae0c51c4ed6e",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/A Positive Pressure Jamming Based Variable Stiffness.pdf": "bba1aa6651c62d2f1060e73850de3ab0ea2d42f229f96eaab487c3f1f9e63ee2",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/Experimental-Numerical Assessment of Mechanical Behavior of.pdf": "06eca6451e9f7216f792f25c967488d03e0f0208d894cd2318cd6f735c2b914c",
  "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf/A Review of Mechanisms to Vary the Stiffness of Laminar.pdf": "628736655bfbf7871679019026828548325bd9a90fc4d824963f86f130cfc8ce",
  "app/nodes/save_run.py": "24522b5f75dbe63831f75474ebe15c6b692d478cc2cbec9d503e6b15d319cda4",
  "app/nodes/researcher.py": "9a7fabe1acc0aa642a43406664eb60729ef982724cf0225076e5ed9cf1c59fa9",
  "app/nodes/corpus_loader.py": "293c0494b058d85626e4e6c0e3e63d0175c88166766b40d204d0a0e7b2877600",
  "app/nodes/approval.py": "14b10ceda6ec7bee76fbb2347609fd60f8d33f0d17be962bae9eab7b8e156e35",
  "app/nodes/judge.py": "056f83c51f0ecd8e757c5c99db3f355c64bf8ab52698d8a4e37bb28c78eb582d",
  "app/nodes/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "app/nodes/critic.py": "39418dab2481bdf5a3cebd2bb4917220954d279a4a066e5bfdceb25ce0a11b9c",
  "app/nodes/literature.py": "db8e3a86cb9aefbf1bb47a6d32cdb84eab16dcbf111dc0ff14400cbb957e7e68",
  "app/models/gateway.py": "bae0b6141ee41bf2a58cf04aad81fb8956a2178f851f4157c9b9a26d40c2e676",
  "app/models/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "app/providers/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "app/providers/antigravity_provider.py": "47e53c4af80c35a4f33f02f85cd75f75ef0710f5cd3f0a831c85d6964d2d4b55",
  "app/providers/codex_provider.py": "8d57450a2c714477545f908d21972726e07ae419f9f715b366c67bf04e7f4f9e",
  "app/ingestion/init_search_log.py": "97f3a17ce1b109e2e8ecc3bfead4e7ec37dda2c1dc755c5a7bc79c8fefbc1203",
  "app/ingestion/pdf_loader.py": "2630419d91c162ae3ef4d423897e55857b68333a4623cf4930ec2abaf8e69fd2",
  "app/ingestion/critique_directions.py": "5eedc257b63a6a12467134ca239ccb737bcf40a9ccee10442a8471f6384edd84",
  "app/ingestion/final_cross_direction_adjudication.py": "bff24b3c012e6289e4d7115f420f29eb79195e2cb647e19d6bb90f895228c61e",
  "app/ingestion/screen_search_candidates.py": "b0b297116b8361154355753acaca7a9dfa152bfe764016a309fd2cd016e3cc47",
  "app/ingestion/citation_identity.py": "19a0da22de1d0cafc297e82dfc5be1b471b32d127d0c2795003a7160a9879a78",
  "app/ingestion/mp1_v002_screen_citation_metadata.py": "2ff8cd622fdcd308b0fc9790f1b568253864927db1f54894f22d29d9ca2af4ee",
  "app/ingestion/synthesize_corpus.py": "4c263bf1964bc16183d027051bd039165886eeb8355ef499b4fb6cc9154858a0",
  "app/ingestion/build_reasoning_batches.py": "a384a7de8a8cd9c223037f5ffa2d15a67b8240454270e162a8c2f1cdf6b74d0c",
  "app/ingestion/candidate_directions.py": "9310f3fc3037f3addbd4bf89e70e13e018b4a4d59fa32f618b8dc82b4386b12a",
  "app/ingestion/cross_round_adversarial_synthesis.py": "e02f6c6ab02bdd97e27b03d618acc3edc2a5534b8cfa452770624bcffd834dc2",
  "app/ingestion/d1_v008_final_named_target_audit.py": "a09d1f07e871dacffe8830155d8b0a04cfc0b7cd2d87f5cfb269a1ac3c65159c",
  "app/ingestion/mp1_v002_final_adjudication.py": "a88d9de01443f738a26127cdd00287772775baa69639fd4c581becfb7283b8f6",
  "app/ingestion/add_paper.py": "9903862f6f2f24521798e8f92b9aa82dd7b73ee12658739841c5a3d2cf6d6206",
  "app/ingestion/d1_v005_c02_adversarial_audit.py": "f88693fd9c67dbf477d51b3d791ac52c150fa2b6bf99a276071484b1d5967f52",
  "app/ingestion/mp1_v001_core_prior_art_audit.py": "3bd55681201cbc8a5d154eb589d15f50e6badec4ddcaee90cd7aa0d1eb79a051",
  "app/ingestion/screen_paper.py": "745e55de59733d7bb3727adaab274ef0033fbe6cd88026cc09c778414e128a29",
  "app/ingestion/normalize_citation_exports.py": "d541551958eae3080314424d40bdfef8de2e3b94b3842490171ee0e3b0d1acb3",
  "app/ingestion/build_matrix.py": "ae2cd1f7d63618c21fb14622bdbbe2ef199c554c58e9ee5bd8ae44ff49892c08",
  "app/ingestion/__init__.py": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "app/ingestion/mp1_v002_targeted_threat_audit.py": "6c493969f6de090f0b804c5d3d39296ac0d2b2760d4a27cf42c9c3275dbb8ff3",
  "app/ingestion/record_search.py": "4e6dbcb2b5b9a8af38ca18731c5e5858a818735e74eba4f6062a8bb2e60c724c",
  "app/ingestion/ingest_papers.py": "8cf7e7d45a2b9ddcf3b7dbae19c10d3d33be102c2b008c8b4dbda7b84deb74d1",
  "app/ingestion/d1_v009_late_found_adjacent_audit.py": "95c51ea4ab3beac5bf9f4bacbb2757bfcf9988ee21ebba96201911f534ff6fc4",
  "app/ingestion/final_adjudication.py": "e7b15652d8bbbee16fb6a56c7c8be5dec044c4a98067051360ea07ad23adf6b3",
  "app/ingestion/synthesize_reasoning_batches.py": "b5191d5a4c51871af1e79bafd4c2a3d6c602db7d359ac74489a799d1cfba2860",
  "app/ingestion/build_search_plan.py": "91f377c27a0a7a9a32841559df8d83d186b23d60bbc838ca8c24b0435e7fefc8",
  "app/ingestion/citation_parsers.py": "28d8a3365b9b8d5d4feb564049be651e323bbfb239ee9c999971648cf7525b0f",
  "app/ingestion/mp1_v002_citation_coverage.py": "2a1a83d421db7ae054c4961ce0f5d966cefc3047dea54eedeeac18b32f7d6dc3",
  "app/ingestion/build_gap_verification.py": "a48f4b4c4cc4b2f6af04747d62a01cefeeb216f0410c063c931cdf2d1ae4b285",
  "app/ingestion/paper_extractor.py": "bf781f492984ea1ef2b31c2aaeed0f4c9922633484dc87fd8feb32e4acc001d3",
  "app/ingestion/corpus_status.py": "f03d7044a594fb3654ce30d292d1f2115f1878ebe95b5e1f705406e0a748a56d",
  "app/ingestion/d1_v006_c03_adversarial_audit.py": "f78d5efddc14063d49f5d686877c4b1f376e4aaa1d3f51fede17cfcbb98f8a45",
  "app/ingestion/build_verification_matrix.py": "b21ba757edb2d013b04fd30daf548fed2fd8cefe72d8a18a57b7faf4daf2a909",
  "app/ingestion/validate_evidence.py": "51518f02c30f2e22e62b4d04b23e08f2b1168aa7d37ff7243ab4b7e7890d9843",
  "app/ingestion/verify_direction.py": "66c50878123727e55f8989f45513a16e2e2c373ad8d8de95d950a640b70cde83",
  "app/ingestion/init_corpus_storage.py": "bd77d23b9a420cf2df91b23b4af50575a95bd4aca2e36b71cdb5dcdbe8141bbf",
  "app/ingestion/d1_v007_c04_adversarial_audit.py": "eda595abf7af2f5554b977700df87a2b0eef16dbf2dc02d001c010d08d7a8846",
  "app/ingestion/d1_v004_c01_adversarial_audit.py": "05b9c99083ebefff6b463a67f1fae81b9d718cee24ba2bab9749d5e1f4a4ce0c",
  "app/ingestion/recover_critique.py": "eaa7e695cde86ff51db2ebf1665bc259d924e8c81539df648b6728040332723c",
  "app/ingestion/build_database_queries.py": "a6c97f8bd3389e736afa32830f4e94873ae5462c23772969696fa691a32767c6",
  "app/ingestion/registry.py": "c5a3047cbac6f4993561deec69cb2f5296700f17ba27e615c1a4d72002cfaa91",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/05_CROSS_STUDY_COMPARISONS.md": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/03_CHAPTER_2_WRITING_BRIEFS.md": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/10_EXECUTION_REPORT.md": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/11_CHAPTER_2_READINESS_GATE.md": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/12_R3_CHANGELOG.md": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/09_COVERAGE_AND_READINESS_REPORT.md": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/02_SECTION_SOURCE_MATRIX.csv": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/04_CHAPTER_1_WRITING_BRIEFS.md": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/07_CITATION_AND_REFERENCE_CROSSWALK.csv": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/01_OUTLINE_BULLET_CROSSWALK.csv": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/AGENT_PROMPT.md": "91e1fdebe210f01236c0f64f6b9c5bb49fff0fc855967f8a7b45ed470f8e3284",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.json": "55e15a0425dbde3ec3eb54c1e1a769c52717f03ca5d16c5fdfa8ab326d8217cd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.md": "45542951080f66859241e7ee3c9666b7d22df2348d3236e7560f59aef955f605",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_SECTION_INDEX.csv": "ac0a8bf828c9e69362112c6d8282f9de25cb3616ee36fd0448d741dccba59633",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json": "15d7889dcd3d755a866507569b1b97efd8c2de01d6aff4eeb07498042f729cae"
}
```
## Hồ sơ tái kiểm

Checkpoint gốc bất biến. scratch/resume_manifest.json giữ hash và mapping đường dẫn. validation/audit_final_readonly.py chỉ ghi kết quả kiểm vào scratch. validation/resume_validate.py kiểm tập record, neo, coverage và pdf_page. validation/final_package_checks.json ghi phép kiểm cuối sau khi xuất bốn báo cáo.

## Chín deliverable

1. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx`
2. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv`
3. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv`
4. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv`
5. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv`
6. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md`
7. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_UNRESOLVED_ISSUES.md`
8. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_7_GATE_REVIEW.md`
9. `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_EXECUTION_REPORT.md`


# HOTFIX ADDENDUM — MP1-CH2-FULL-INTEGRATION-GATE1-HOTFIX

TASK_ID: MP1-CH2-FULL-INTEGRATION-GATE1-HOTFIX

STATUS: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED

| Trường | Giá trị |
|---|---|
| TASK_ID | MP1-CH2-FULL-INTEGRATION-GATE1-HOTFIX |
| STATUS | HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS |
| BASELINE_DOCX_SHA256 | 9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269 |
| BASELINE_SHA256_VERIFIED | YES |
| NEW_CHAPTER_DOCX_SHA256 | 72a9409fa22f1d838b3e756d35255a91300b23c442ea4f5f36b8e9f2d5f59cb9 |
| NEW_APPENDIX_DOCX_SHA256 | ecde6516319f24708f18a6eeda830f145b8c74edd5c76f654b1303fe4ee4e1ad |
| PATCH_223 | APPLIED; nối một câu, giữ nguyên paragraph |
| PATCH_244 | APPLIED; nối một câu, giữ nguyên paragraph |
| PATCH_233 | APPLIED; paragraph ngay sau bảng2.3.3 |
| PATCH_253 | APPLIED; paragraph sau neo§2.5.3 |
| APPROVED_PATCHES_APPLIED | 4 |
| EDITORIAL_CLAIMS_ADDED | 4 |
| SCIENTIFIC_SOURCE_FACTS_CHANGED | 0 |
| GLOSSARY_OPTION | OPTION_B_APPROVED |
| GLOSSARY_TABLES_MOVED | 5 |
| GLOSSARY_ROWS_PRESERVED | 286/286;976/976 ô exact text/raw/C14N |
| GLOSSARY_TEXT_HASHES | {"GLOSSARY-1": "cb21cc3e882ff5ba2bf9d4cb00e750e51a6bd4bd8be7e16909e6c7a61a579ccd", "GLOSSARY-2": "986f5e735072b8b9108efd64a837db0f4cd67797e0a4e0af9e1ae56343b739bd", "GLOSSARY-3": "65a94d2552a14194e6ded77ef0728a9e1f2c9b999c10d5a69f8931c0f06a832f", "GLOSSARY-4": "a4986dbd4ce31c2d510e9a5936124569cd75b71a569232b35636c7b67151c60b", "GLOSSARY-5": "5c8f7c6e24edc642ef3052e605f8f3c49c92aaf6018c3f7c3a36bf43bd978c03"} |
| GLOSSARY_XML_HASHES | {"GLOSSARY-1": "0efc157726d6e1186c9eb8cceda8d679a388915f8788517ed1048ba38081160c", "GLOSSARY-2": "3e29f88f39fb73a362c8b24d74b5ff02f5bebe031da48352d4fe0231903443e5", "GLOSSARY-3": "7ea8f63b10ea1b55cf7b1bebfed65864bf522f9daded181c7b92af5e698de00d", "GLOSSARY-4": "9cbdc3aacc20be7a326b51d1a9a13fb6f5a1fb5be836568dc64a7041e694b3de", "GLOSSARY-5": "5cac2b866a6068b64769967ce9126abcd9d65a44836ab6324d54943a164fdc18"} |
| GLOSSARY_LEADINS_MOVED | 8 lead-in được chỉ định+2 caption kế thừa A.1/A.2; tất cả C14N exact |
| CHAPTER_TABLES_BEFORE_AFTER | 21→16; glossary5→0; other16→16 |
| APPENDIX_TABLES | 5 |
| FIGURES_BEFORE_AFTER | 1→1 |
| OMML_BEFORE_AFTER | 19→19 |
| ORIGINAL_RECORDS_ACCOUNTED_FOR | 913/913; original_record_json nguyên vẹn |
| UPDATED_TRACE_ROWS | 2935 |
| UPDATED_ANCHORS_RESOLVED | 5792/5792=2857 source+2935 target; unresolved0 |
| CHAPTER_COVERAGE | 223222 ký tự w:t được map;0 gap;1578 trace row |
| APPENDIX_COVERAGE | 71902 ký tự w:t được map;0 gap;1357 trace row |
| TERMINOLOGY_RECORDS_ACCOUNTED_FOR | 313/313;32 chapter/281 appendix;14 section-scope có giới hạn rõ |
| CITATION_IDENTITY_MAPPING | 783/783 original;328 chapter+455 appendix; thêm30 lượt dẫn chỉ mục=485 appendix;69 lineage row giữ;30 shared identities |
| CHAPTER_REFERENCES | 30 |
| APPENDIX_REFERENCES | 30 |
| MISSING_REFERENCES | 0 |
| ORPHAN_REFERENCES | 0 |
| OFFICIAL_BULLETS_BEFORE_AFTER | 52 COVERED/10 COVERED_WITH_BOUNDARY/3 PARTIAL_EDITORIAL →53/12/0;NOT_COVERED0 |
| GROUP_SYNTHESIS_AUDIT | 17/17 có paragraph tổng hợp;13 COVERED/4 COVERED_WITH_BOUNDARY; bốn bảng hỗ trợ đi sau phần lập luận |
| OUTLINE_FINDING_STATUS | CH2-OUTLINE-01=RESOLVED trong SELF_REVIEW_ONLY |
| RENDERED_CHAPTER_PAGES | 73 |
| RENDERED_APPENDIX_PAGES | 32 |
| CHAPTER_PAGES_VISUALLY_REVIEWED | 73/73 |
| APPENDIX_PAGES_VISUALLY_REVIEWED | 32/32; ROOT cũng xem lại đủ32 |
| ZIP_XML_VALIDATION | PASS; CRC và16 XML/rels part mỗi DOCX |
| RELATIONSHIP_VALIDATION | PASS;14 chapter/13 appendix;0 dangling; bookmark278/143, không trùng |
| MICROSOFT_WORD_VALIDATION | NOT_VERIFIED |
| GATE_1 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_2 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_3 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_4 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_5 | PASS |
| GATE_6 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_7 | PASS |
| BASELINES_UNCHANGED | YES;6/6 canonical SHA khớp |
| SOURCE_PACKAGES_UNCHANGED | YES;42/42 file |
| WEP_P3_REGISTRY_UNCHANGED | YES;hash toàn bộ input cùng3080 protected/30 external được đối chiếu |
| GIT_CHANGE_SCOPE | Chỉ9 deliverable tại chapter_2_integrated và1 appendix staging mới; tracked/cached diff sẵn có giữ nguyên. |
| P1_P2_UNRESOLVED | 0 trong tự kiểm hotfix; independent acceptance vẫn chờ |
| DOCUMENTED_LIMITATIONS | ["Microsoft Word chưa được chạy; MICROSOFT_WORD_VALIDATION=NOT_VERIFIED. LibreOffice24.2.7.2 với Math là công cụ kết xuất.", "Bốn nhóm§2.3.1/2.3.2/2.3.4/2.3.5 có đoạn tổng hợp cuối phần lập luận và bảng hỗ trợ theo sau. Root phân xử đủ nội dung; cách hiểu vị trí được ghi rõ để nghiệm thu độc lập. Không lấy caption hoặc bảng thay paragraph.", "Chỉ tự kiểm. Trạng thái VERIFIED FULL TEXT/METADATA ONLY của nguồn được kế thừa theo lineage, không phải tuyên bố tái đọc toàn bộ PDF. Bốn claim mới là AUTHOR_METHOD_SYNTHESIS và INFERENCE/PROPOSAL.", "Chính sách trích dẫn của trường, ánh xạ RQ tạm thời và năm quyết định khoa học vẫn mở. H0b chưa bị bác bỏ, H1 chưa đủ bằng chứng.", "Mười bốn record thuật ngữ§2.1 chỉ có mapping cấp phạm vi§2.1; định nghĩa nguyên gốc vẫn nằm trong original_record_json. Không tạo bảng thuật ngữ giả hoặc neo một câu không tồn tại.", "Khoảng trắng kế thừa ở trang39 và cỡ chữ chưa đều trong Bảng2.5.2 trang47 vẫn được ghi làP3. Các đối tượng không bị cắt; không sửa style ngoài phạm vi hotfix.", "Nhãn A.1/A.2 và ghi chú nguồn được giữ nguyên trong staging như lịch sử; chưa gán số phụ lục chính thức. Chỉ mục nguồn bổ sung30 lượt dẫn cấu trúc, không bổ sung nguồn khoa học.", "Backend không cung cấp chứng cứ xác minh model thực tế. Cấu hình lời gọi worker được ghi nhận: gpt-6-sol/medium ×1, gpt-6-luna/medium ×2; đây không phải xác nhận backend. Root được yêu cầu GPT-6.1 Sol High, không suy model thực tế từ yêu cầu."] |
| FILES_MODIFIED | ["outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_EXECUTION_REPORT.md", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_UNRESOLVED_ISSUES.md", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_7_GATE_REVIEW.md", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv", "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv"] |
| FILE_CREATED | outputs/thesis_drafts/chapter_2/appendix_terminology_staging/MP1_THESIS_TERMINOLOGY_APPENDIX_STAGING.docx |
| COMMIT_STATUS | NOT_PERFORMED |
| PUSH_STATUS | NOT_PERFORMED |
| FINAL_SELF_REVIEW_DECISION | SELF_REVIEW_ONLY |
| NEXT_ACTION | AWAIT_INDEPENDENT_FULL_CHAPTER_HOTFIX_ACCEPTANCE |
| ROOT_MODEL_ACTUAL | NOT_VERIFIABLE_FROM_BACKEND |
| WORKER_MODELS_ACTUAL | NOT_VERIFIABLE_FROM_BACKEND |
| WORKER_CALL_CONFIGURATIONS | gpt-6-sol/medium ×1;gpt-6-luna/medium ×2 |
| REVIEW_AUTHORITY | SELF_REVIEW_ONLY |
| INDEPENDENT_ACCEPTANCE | REQUIRED_NOT_PERFORMED |
| APPENDIX_DOCUMENT_STATUS | DRAFT_APPENDIX_STAGING;NOT_FINAL_THESIS_APPENDIX;NOT_ASSIGNED_APPENDIX_NUMBER |

## Kiểm đếm sau hotfix

```json
{
  "glossary": {
    "tables": 5,
    "rows": 286,
    "cells_exact": 976,
    "all_cell_text_raw_and_c14n_exact": true,
    "all_leadins_c14n_exact": true,
    "leadins": 10,
    "original_leadins": 8,
    "additional_captions_moved": 2
  },
  "scientific_preservation": {
    "original_paragraphs_tables_checked": 2150,
    "changed_existing_paragraphs": [
      "/w:document/w:body/w:p[81]",
      "/w:document/w:body/w:p[217]"
    ],
    "added_editorial_claims": 4,
    "source_scientific_facts_changed": 0,
    "omml_c14n_exact": 19,
    "figure_xml_exact": true,
    "chapter_other_package_parts_byte_exact": true,
    "media_hashes": {
      "word/media/section2_image1.png": "26db28e4b1ff2d51a4be4f140dbf082ef8817301e7cfcbc9d955177409784b8f"
    }
  },
  "original_source_records": {
    "input_records": 913,
    "accounted_for": 913,
    "original_json_equal": true,
    "original_trace_rows_preserved": 2859,
    "trace_rows": 2935,
    "record_kinds": {
      "SCIENTIFIC_CLAIM": 931,
      "STRUCTURAL_RECORD": 1995,
      "ARCHIVAL_SUPPORT_ONLY": 5,
      "NEW_EDITORIAL_CLAIM": 4
    },
    "target_document_rows": {
      "CHAPTER_DOCX": 1578,
      "APPENDIX_STAGING_DOCX": 1357
    }
  },
  "anchors": {
    "source_checks": 2857,
    "target_checks": 2935,
    "total": 5792,
    "unresolved": 0,
    "rebuild_method": "OBJECT_LINEAGE_AND_EXACT_TEXT_RELOCATION; OFFSETS_REFOUND; REOPENED_TARGET_DOCUMENTS"
  },
  "coverage": {
    "CHAPTER_DOCX": {
      "covered_characters": 223222,
      "uncovered_characters": 0,
      "unresolved_anchors": 0
    },
    "APPENDIX_STAGING_DOCX": {
      "covered_characters": 71902,
      "uncovered_characters": 0,
      "unresolved_anchors": 0
    }
  },
  "terminology": {
    "records": 313,
    "original_fields_and_json_preserved": true,
    "target_documents": {
      "CHAPTER_DOCX": 32,
      "APPENDIX_STAGING_DOCX": 281
    },
    "section_scope_only": 14
  },
  "citations": {
    "original_identity_occurrences": 783,
    "original_accounted_for": 783,
    "chapter_occurrences": 328,
    "appendix_occurrences": 485,
    "appendix_original_occurrences": 455,
    "appendix_new_structural_index_occurrences": 30,
    "chapter_references": 30,
    "appendix_references": 30,
    "shared_reference_identities": 30,
    "glossary_source_identities": 29,
    "additional_appendix_style_source_identity": "IEEE_REFERENCE_GUIDE_2025; ĐÃ CÓ TRONG BASELINE",
    "missing_references": 0,
    "orphan_references": 0,
    "numbering_conflicts": 0,
    "first_citation_order": {
      "CHAPTER_DOCX": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30
      ],
      "APPENDIX_STAGING_DOCX": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30
      ]
    },
    "crowley_metadata_preserved": true
  },
  "objects": {
    "crosswalk_rows": 86,
    "old_rows_preserved": 85,
    "new_cross_reference_rows": 1,
    "packages": {
      "CHAPTER_DOCX": {
        "zip_crc": "PASS",
        "xml_parts": 16,
        "relationships": 14,
        "bookmarks": 278,
        "dangling_relationships": 0,
        "duplicate_bookmark_ids": 0,
        "fields": 0,
        "hyperlinks": 0,
        "footnotes_endnotes": 0,
        "tables": 16,
        "figures": 1,
        "omml": 19,
        "sha256": "72a9409fa22f1d838b3e756d35255a91300b23c442ea4f5f36b8e9f2d5f59cb9"
      },
      "APPENDIX_STAGING_DOCX": {
        "zip_crc": "PASS",
        "xml_parts": 16,
        "relationships": 13,
        "bookmarks": 143,
        "dangling_relationships": 0,
        "duplicate_bookmark_ids": 0,
        "fields": 0,
        "hyperlinks": 0,
        "footnotes_endnotes": 0,
        "tables": 5,
        "figures": 0,
        "omml": 0,
        "sha256": "ecde6516319f24708f18a6eeda830f145b8c74edd5c76f654b1303fe4ee4e1ad"
      }
    }
  },
  "status": "PASS"
}
```

## Bảy Gate hiện hành

```json
[
  {
    "GATE": "G1",
    "STATUS": "PASS_WITH_DOCUMENTED_LIMITATIONS",
    "METHOD": "Đọc lại65 bullet cùng paragraph/table thực tế sau hotfix; kiểm17 nhóm; phân xử lại chỗ kết đoạn và bốn patch; kiểm không còn glossary/heading phụ trong chapter.",
    "EVIDENCE": "outline-review-input.json; outline-self-review.json; outline-placement-recheck.json; outline-root-adjudication.json; nội dung chi tiết ngay dưới.",
    "COUNTS": "53 COVERED;12 COVERED_WITH_BOUNDARY;0 PARTIAL_EDITORIAL;0 NOT_COVERED;17 nhóm có tổng hợp;0 glossary trong chapter.",
    "FINDINGS": "Đủ nội dung theo cách hiểu cuối phần lập luận. Bốn bảng hỗ trợ theo sau synthesis được giữ. Không có P2 còn mở trong tự kiểm.",
    "SEVERITY": "P3 về ranh giới diễn giải; không P2",
    "UNRESOLVED": "Nghiệm thu độc lập chưa thực hiện; chính sách trường và quyết định khoa học vẫn mở.",
    "FINAL_DECISION": "Đạt tự kiểm với giới hạn; CH2-OUTLINE-01=RESOLVED trong phạm vi tự kiểm."
  },
  {
    "GATE": "G2",
    "STATUS": "PASS_WITH_DOCUMENTED_LIMITATIONS",
    "METHOD": "Đối chiếu mọi paragraph/table trước/sau bằng văn bản và C14N; kiểm prefix XML hai paragraph nối câu; hai paragraph mới đúng nguyên văn duyệt; so sánh P3 và hash nguồn.",
    "EVIDENCE": "structural-validation.json::scientific_preservation; node-relocation-manifest.json; patches.json; bảng trạng thái khoa học dưới.",
    "COUNTS": "4 claim biên tập mới;0 source fact thay đổi;2 paragraph nối câu,2 paragraph chèn;0 nội dung gốc bị mất.",
    "FINDINGS": "AUTHOR_METHOD_SYNTHESIS/INFERENCE/PROPOSAL; không chọn topology, truyền áp, tham số, metric hoặc Bench; không nâng H1 hay bác H0b.",
    "SEVERITY": "P3 kế thừa",
    "UNRESOLVED": "Năm quyết định khoa học; không tái đọc toàn bộ PDF sơ cấp.",
    "FINAL_DECISION": "Bảo toàn ý nghĩa khoa học trong phạm vi biên tập đã duyệt."
  },
  {
    "GATE": "G3",
    "STATUS": "PASS_WITH_DOCUMENTED_LIMITATIONS",
    "METHOD": "Đọc lại6 source CSV/DOCX, so tập913 khóa và original_record_json; lần theo native XML object sang đích thật; tìm lại span bằng văn bản/thứ tự xuất hiện rồi reopen kiểm offset; union coverage mọi ký tự w:t.",
    "EVIDENCE": "Hai cột target_document/target_anchor_container trong master; structural-validation.json::anchors/coverage; source support mới trong editorial_supports_json.",
    "COUNTS": "913/913 original record;2935 trace row;2857 source+2935 target=5792 neo exact;1578 row chapter/1357 row appendix;0 gap.",
    "FINDINGS": "2859 row gốc giữ; thêm4 NEW_EDITORIAL_CLAIM và72 STRUCTURAL_RECORD. Giữ5 ARCHIVAL_SUPPORT_ONLY. 14 thuật ngữ§2.1 chỉ có section-scope mapping, không bịa neo literal.",
    "SEVERITY": "P3 về độ hạt bằng chứng kế thừa",
    "UNRESOLVED": "0 unresolved anchor;0 unexplained claim loss; mức neo nguồn rộng vẫn giữ rõ.",
    "FINAL_DECISION": "Đạt đối soát hai tài liệu; không đồng nghĩa mọi claim được tái xác minh ở cấp câu PDF."
  },
  {
    "GATE": "G4",
    "STATUS": "PASS_WITH_DOCUMENTED_LIMITATIONS",
    "METHOD": "Đọc citation từ Word ngoài bibliography, kiểm source identity, thứ tự xuất hiện1–30, từng lineage/token/span ở cả hai đích; kiểm canonical DOI và metadata Crowley.",
    "EVIDENCE": "MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv; structural-validation.json::citations; appendix-index-map.json.",
    "COUNTS": "328 chapter;485 appendix=455 original+30 chỉ mục;783/783 original accounted;30 reference mỗi đích;30 shared identity;0 missing/orphan/conflict.",
    "FINDINGS": "Giữ nguyên số dẫn trong ô để C14N bảng nguyên vẹn. Chỉ mục định danh của phụ lục mở đầu thứ tự số tạm; map số bằng nhau được xác minh theo identity, không suy từ số. IEEE guide đã có ở baseline.",
    "SEVERITY": "P3 về chính sách trường chưa xác minh",
    "UNRESOLVED": "School policy giữ mở; numbering phụ lục tạm thời, chờ tích hợp luận văn.",
    "FINAL_DECISION": "Đạt toàn vẹn citation/reference; không thêm nguồn khoa học."
  },
  {
    "GATE": "G5",
    "STATUS": "PASS",
    "METHOD": "So toàn bộ976 cell text/raw/C14N,286 hàng, table geometry/merged/header flags/native OOXML và10 đoạn dẫn/caption; so19OMML,figure XML/media hash; kiểm bookmarks và cross reference ở hai tệp.",
    "EVIDENCE": "Manifest glossary trong changelog; crosswalk86 row; structural-validation.json::objects/glossary; ảnh các trang công thức.",
    "COUNTS": "21→16 bảng chapter;5 appendix;286 hàng;1→1 hình;19→19OMML;278 bookmark chapter+143 appendix;0 dangling/duplicate.",
    "FINDINGS": "Không có field/hyperlink/footnote/endnote cần chuyển quan hệ trong các bảng. Không có cross-reference trỏ sang bookmark đã chuyển. A.1/A.2 là nhãn kế thừa.",
    "SEVERITY": "NONE trong toàn vẹn đối tượng",
    "UNRESOLVED": "Chính sách numbering cuối cùng chưa được chọn; nội dung đối tượng không bị đổi.",
    "FINAL_DECISION": "Đạt bảo toàn đối tượng native và quan hệ."
  },
  {
    "GATE": "G6",
    "STATUS": "PASS_WITH_DOCUMENTED_LIMITATIONS",
    "METHOD": "Đóng ZIP, tính hash, CRC/XML/relationship; runtime LibreOffice bản sao được sửa8 symlink/fundamentalrc và đường dữ liệu liblangtag, Math hoạt động; render mới2 DOCX; xem riêng từng105 trang150dpi, kiểm thêm19OMML và crop header6.",
    "EVIDENCE": "render-manifest.json; visual-reviewed-final.json; visual-appendix-root-001-032.json; visual-chapter-critical-root.json; hai findingP3 dưới.",
    "COUNTS": "73/73 trang chapter;32/32 appendix;16 XML/rels part mỗi tệp;14/13 relationship;0 dangling.",
    "FINDINGS": "Khoảng trắng trang39 và font một số ô bảng trang47 kế thừa, đọc được. Finding thiếu header5/6/19 không được xác nhận sau ROOT xem lại. Không sử dụng QA cũ như QA mới.",
    "SEVERITY": "P3",
    "UNRESOLVED": "MICROSOFT_WORD_VALIDATION=NOT_VERIFIED; hai hạn chế trình bày kế thừa.",
    "FINAL_DECISION": "Đạt kết xuất và rà từng trang trong LibreOffice; không cấp xác nhận Microsoft Word."
  },
  {
    "GATE": "G7",
    "STATUS": "PASS",
    "METHOD": "Hash toàn bộ23407 input file,3080 protected file và42 file source package; Git branch/HEAD/diff/cached; kiểm tập file cho phép trước/sau xuất.",
    "EVIDENCE": "all-input-hashes.json; immutability-prepublish.json; immutability-final.json; final-package-check.json; git-status/diff/cached snapshot.",
    "COUNTS": "6 canonical baseline;42 package file;30 protected file ngoài repo;9 deliverable sửa+1 DOCX mới được phép.",
    "FINDINGS": "Giữ pre-existing work; scientific state/registry không đổi; không đổi branch; không commit/push.",
    "SEVERITY": "NONE",
    "UNRESOLVED": "Independent acceptance chưa thực hiện.",
    "FINAL_DECISION": "Đạt bất biến và đóng gói trong phạm vi được duyệt."
  }
]
```

## Phân xử65 bullet và17 nhóm

```json
{
  "counts": {
    "COVERED": 53,
    "COVERED_WITH_BOUNDARY": 12
  },
  "group_counts": {
    "COVERED": 13,
    "COVERED_WITH_BOUNDARY": 4
  },
  "boundary": "Độ bao phủ nội dung khác xác minh khoa học. Cuối nhóm được kiểm ở đoạn tổng hợp cuối phần lập luận; bảng hỗ trợ có thể theo sau. Không yêu cầu tạo thêm paragraph ngoài bốn patch đã duyệt."
}
```
## Bằng chứng thị giác mới

| Tài liệu | SHA-256 DOCX | SHA-256 PDF mới | Số trang đã xem |
|---|---|---|---|
| CHAPTER_DOCX | 72a9409fa22f1d838b3e756d35255a91300b23c442ea4f5f36b8e9f2d5f59cb9 | 5ac4b2cdef6c1565baecb101be43be6b72d24ee8462ce286bb1b3cf170160c2b | 73/73 |
| APPENDIX_STAGING_DOCX | ecde6516319f24708f18a6eeda830f145b8c74edd5c76f654b1303fe4ee4e1ad | 2e988070f51ff096036e11083ed3bd697ce9582e42660ddc1935422b91662802 | 32/32 |

```json
[
  {
    "id": "CH2-HF-QA-01",
    "document": "CHAPTER_DOCX",
    "page": 39,
    "severity": "P3",
    "status": "DOCUMENTED_LIMITATION",
    "finding": "Khoảng trắng lớn ở cuối§2.4.4.",
    "disposition": "ROOT xác nhận do blank paragraph pre-hotfix p218 có pageBreakBefore kế thừa. Không thêm page break; nội dung và định dạng baseline được giữ. Không clipping hoặc mất luận cứ."
  },
  {
    "id": "CH2-HF-QA-02",
    "document": "CHAPTER_DOCX",
    "page": 47,
    "severity": "P3",
    "status": "DOCUMENTED_LIMITATION",
    "finding": "Cỡ chữ một số ô Bảng2.5.2 không đồng đều.",
    "disposition": "ROOT xác nhận bảng đọc được, không cắt ô. XML bảng khớp baseline nguyên vẹn; chuẩn hóa style nằm ngoài bốn patch được duyệt."
  },
  {
    "id": "CH2-HF-QA-03",
    "document": "APPENDIX_STAGING_DOCX",
    "page": "5;6;19",
    "severity": "NONE",
    "status": "NOT_REPRODUCED_AFTER_ROOT_RECHECK",
    "finding": "Worker báo thiếu header lặp.",
    "disposition": "ROOT xem cả32 trang và crop riêng đầu trang6. Cả5/6/19 có header hiện rõ; PNG/hash trùng manifest. Giữ finding cũ và recheck worker để đối chiếu; không sửa bảng để chữa finding không được xác nhận.",
    "evidence": "appendix-page006-header-root.png"
  }
]
```
## Bất biến và phạm vi Git

```json
{
  "status": "PASS",
  "input_files_checked": 23407,
  "protected_files_checked": 3080,
  "external_protected_files_checked": 30,
  "changes": [],
  "source_packages": [
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_7_GATE_REVIEW.md",
      "sha256": "d47f43eb002cebc545c4432fa4ee8245c8a78127a905e8cd8aec44211ce2867c"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_CITATION_RENUMBERING_MAP.csv",
      "sha256": "11118450c5d744b4ae1bc7e6b39a2c74679fe13051d91e1e1b345712b0da747e"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_EXECUTION_REPORT.md",
      "sha256": "de5781e750a45b538c9c9f744293f94da8b0b2706c512e31217cf3b66940cb5e"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATED.docx",
      "sha256": "fe4fd16fbb93bcdf39708740fb90dd120563825c57ce86bd9cf36e35f841d4dd"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_INTEGRATION_CHANGELOG.md",
      "sha256": "c45f8c5320d14f56dcb54bc654e92608cd1d58ab5fc7a9eeed652a62f6921919"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_SOURCE_TRACEABILITY.csv",
      "sha256": "035115773105e34fe363cf1ce5e201c9ddd765e886a4a17af4de42273e8a667d"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_1_integrated/MP1_CH2_2_1_MASTER_TERMINOLOGY.csv",
      "sha256": "3b989e27e2ffd2079aed8ee2591f1ca9632747c3811b5b01f7a7601808a4a728"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_7_GATE_REVIEW.md",
      "sha256": "cd9b63c933e07b4bbc1dd02dd5f469af449e49a5515fa226d2b5861ebfd8a4b2"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_CITATION_RENUMBERING_MAP.csv",
      "sha256": "d04856f4e81d291a5188d2e1182fb92d1ef396b8dd85113a66ea2e3693c823e7"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_EXECUTION_REPORT.md",
      "sha256": "fa80bfc44be924c594bcda9514f290e74f558dd7b49dfe1a9ffcd190a05bb095"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATED.docx",
      "sha256": "701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_INTEGRATION_CHANGELOG.md",
      "sha256": "df3bca80e0b37fa66beeb63c3a059be3149b117405d5862dff846c0134022351"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_SOURCE_TRACEABILITY.csv",
      "sha256": "a72802cc636d3c7705113cf24eec47282ebd35051f6ca9216a4d61c67510735e"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_2_integrated/MP1_CH2_2_2_MASTER_TERMINOLOGY.csv",
      "sha256": "f529dfcb8ebf58db07112c4b17154760a08714a6bac165fc0503b4e06c736693"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md",
      "sha256": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv",
      "sha256": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md",
      "sha256": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx",
      "sha256": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md",
      "sha256": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv",
      "sha256": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv",
      "sha256": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md",
      "sha256": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv",
      "sha256": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md",
      "sha256": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx",
      "sha256": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md",
      "sha256": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv",
      "sha256": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv",
      "sha256": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md",
      "sha256": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv",
      "sha256": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md",
      "sha256": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx",
      "sha256": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md",
      "sha256": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv",
      "sha256": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv",
      "sha256": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md",
      "sha256": "b066121b47c37197b10d2bed2fa9709d5688d4973b5d13e23121c7bbf6ed275a"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv",
      "sha256": "019d4780f896a73b3b85400675d394dcfdda1c13e8404d7a0ff9723db4887944"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md",
      "sha256": "de894a4c00089ca73f15076e06fdba9870b86231e236f7a7add802e9f701a2d6"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx",
      "sha256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md",
      "sha256": "15fc8d6380b20bff447626adff74034251ab633c548dea0893a836d7f0f28fc0"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv",
      "sha256": "987fb13dda00f2d62abb4da346f2c6da7e3cbd3857749edc3f72725b59049a13"
    },
    {
      "path": "outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv",
      "sha256": "ec725c4206ac2854febc16f7ddb882802c1d71e53037792dd6ad6383869bca09"
    }
  ],
  "branch": "main",
  "head": "e66bb2f2339006e763cd60687cfc24680b945d97",
  "tracked_and_cached_diff_unchanged": true
}
```

## Giới hạn và điểm dừng

- Microsoft Word chưa được chạy; MICROSOFT_WORD_VALIDATION=NOT_VERIFIED. LibreOffice24.2.7.2 với Math là công cụ kết xuất.
- Bốn nhóm§2.3.1/2.3.2/2.3.4/2.3.5 có đoạn tổng hợp cuối phần lập luận và bảng hỗ trợ theo sau. Root phân xử đủ nội dung; cách hiểu vị trí được ghi rõ để nghiệm thu độc lập. Không lấy caption hoặc bảng thay paragraph.
- Chỉ tự kiểm. Trạng thái VERIFIED FULL TEXT/METADATA ONLY của nguồn được kế thừa theo lineage, không phải tuyên bố tái đọc toàn bộ PDF. Bốn claim mới là AUTHOR_METHOD_SYNTHESIS và INFERENCE/PROPOSAL.
- Chính sách trích dẫn của trường, ánh xạ RQ tạm thời và năm quyết định khoa học vẫn mở. H0b chưa bị bác bỏ, H1 chưa đủ bằng chứng.
- Mười bốn record thuật ngữ§2.1 chỉ có mapping cấp phạm vi§2.1; định nghĩa nguyên gốc vẫn nằm trong original_record_json. Không tạo bảng thuật ngữ giả hoặc neo một câu không tồn tại.
- Khoảng trắng kế thừa ở trang39 và cỡ chữ chưa đều trong Bảng2.5.2 trang47 vẫn được ghi làP3. Các đối tượng không bị cắt; không sửa style ngoài phạm vi hotfix.
- Nhãn A.1/A.2 và ghi chú nguồn được giữ nguyên trong staging như lịch sử; chưa gán số phụ lục chính thức. Chỉ mục nguồn bổ sung30 lượt dẫn cấu trúc, không bổ sung nguồn khoa học.
- Backend không cung cấp chứng cứ xác minh model thực tế. Cấu hình lời gọi worker được ghi nhận: gpt-6-sol/medium ×1, gpt-6-luna/medium ×2; đây không phải xác nhận backend. Root được yêu cầu GPT-6.1 Sol High, không suy model thực tế từ yêu cầu.

FINAL_SELF_REVIEW_DECISION: SELF_REVIEW_ONLY

NEXT_ACTION: AWAIT_INDEPENDENT_FULL_CHAPTER_HOTFIX_ACCEPTANCE


## Kiểm package sau xuất hotfix

Đã mở lại9 deliverable và1 phụ lục. Kết quả cuối ghi ở scratch và tóm tắt tại đây.

```json
{
  "status": "PASS",
  "branch": "main",
  "head": "e66bb2f2339006e763cd60687cfc24680b945d97",
  "all_preexisting_input_files_checked": 23407,
  "all_unchanged_outside_scope": true,
  "source_packages_unchanged": 42,
  "canonical_baselines_unchanged": 6,
  "protected_external_files_unchanged": 30,
  "wep_p3_registry_unchanged": true,
  "modified": [
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_7_GATE_REVIEW.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_EXECUTION_REPORT.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_UNRESOLVED_ISSUES.md"
  ],
  "created": [
    "outputs/thesis_drafts/chapter_2/appendix_terminology_staging/MP1_THESIS_TERMINOLOGY_APPENDIX_STAGING.docx"
  ],
  "tracked_and_cached_diff_unchanged": true,
  "git_status_added_paths": [
    "?? outputs/thesis_drafts/chapter_2/appendix_terminology_staging/MP1_THESIS_TERMINOLOGY_APPENDIX_STAGING.docx"
  ],
  "original_records": 913,
  "trace_rows": 2935,
  "terminology": 313,
  "citation_map_rows": 69,
  "object_crosswalk_rows": 86,
  "mandatory_execution_fields": 63,
  "nine_deliverables_reopened": true,
  "appendix_reopened": true,
  "no_qa_files_in_output_directories": true,
  "no_commit": true,
  "no_push": true,
  "independent_acceptance": "REQUIRED_NOT_PERFORMED"
}
```
