# Báo cáo thực thi — §2.6.2

TASK_ID: MP1-CH2-2.6.2-RESEARCH-THESIS-DRAFT
STATUS: COMPLETED_WITH_DOCUMENTED_LIMITATIONS
EXECUTION_DATE: 2026-10-19 (Asia/Bangkok)
WORKSPACE: /home/khanh/projects/mechanical-research-agents
BRANCH: main
HEAD: e66bb2f2339006e763cd60687cfc24680b945d97

ROOT_MODEL_REQUESTED: GPT-6.1 Sol High
ROOT_MODEL_ACTUAL: NOT_EXPOSED
WORKER_MODELS_REQUESTED: Sol Medium hoặc Luna tùy nhiệm vụ
WORKER_MODELS_ACTUAL: NOT_VERIFIED_BACKEND; dispatch selectors gpt-6.1-sol/medium và gpt-6-luna/medium đã được chỉ định, không là telemetry xác nhận backend.
REVIEW_AUTHORITY: SELF_REVIEW
INDEPENDENT_ACCEPTANCE: NOT_YET_PERFORMED
FINAL_SELF_REVIEW_DECISION: ACCEPTED_WITH_DOCUMENTED_LIMITATIONS
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE

## Phạm vi hoàn thành và bảo toàn

Chỉ biên soạn §2.6.2 tiếng Việt,16 đoạn khoa học, bảng thuật ngữ và tài liệu tham khảo. Không tạo §2.6.3/§2.6.4, không tích hợp §2.6, không thay WEP/P3/WP-E/registry hoặc accepted baselines. Không commit, push, PR, checkout, merge, reset hoặc pull. Các giới hạn khoa học được giữ có điều kiện; bản thảo không chứng minh tính mới, tham số hoặc mô hình MP1.

Read-only ở đây được kiểm bằng nội dung SHA-256; không gọi chmod/touch/ghi/tái xuất input. Thời gian truy cập atime không được snapshot nên INPUT_ATIME_PRESERVATION: NOT_VERIFIED (đọc có thể chịu chính sách filesystem); không khẳng định kiểm metadata chưa đo.

## WORKERS_USED

| Agent | Công việc thực tế | Dispatch selector | Kết quả thực tế |
|---|---|---|---|
| sources_jamming | WorkerA: M13/M31/M34; lượt WorkerE: dự thảo theo ROOT synthesis | gpt-6.1-sol / medium | A hoàn thành. LượtE báo lỗi quota; có tệp dự thảo tạm hoàn chỉnh nhưng không báo lượtE thành công. ROOT đọc, sửa, phê duyệt và hoàn tất bản cuối. |
| sources_models | WorkerB: M15/M16; đối kiểm ROOT synthesis | gpt-6.1-sol / medium | Hoàn thành, có hai chỉnh độ chính xác nhỏ đã xử lý; không finding khoa học chặn. |
| sources_sma | WorkerC: M18/M22/M26; WorkerF: thuật ngữ | gpt-6.1-sol / medium | Gói xác minh và11thuật ngữ được ROOT xét/điều chỉnh. |
| bounded_qa | WorkerH: kiểm CSV/citation/glossary/XML/ranh giới trong cùng phiên | gpt-6-luna / medium | Hoàn thành0findings; không kiểm lại PDF hay visual. |
| ROOT | Preflight; M38/M28; adjudication; kiểm nguồn quyết định; sửa dự thảo; CSV; Word; render; Gate/final | backend NOT_EXPOSED | Không có WorkerG riêng; ROOT dựng DOCX từ nội dung đã phê duyệt. |

Không có worker bỏ phiếu quyết định khoa học; ROOT đối chứng gốc. Các worker đọc nguồn và QA vẫn thuộc SELF_REVIEW cùng phiên, không được gọi independent acceptance. Skills đã áp dụng: academic-paper, academic-humanizer, unslop, ponytail; workflow người dùng có quyền ưu tiên về phạm vi/corpus/đúng5outputs.

## PRE_FLIGHT / WEP_FILES_READ

Đã đọc context theo thứ tự AGENTS: docs/README.md; docs/project/PROJECT_HANDOFF_CURRENT.md; RESEARCH_STATE.md; research_state.json; RESEARCH_LOG.md; docs/literature/LITERATURE_STRATEGY.md; docs/operations/KNOWN_ISSUES.md. Không thay trạng thái nghiên cứu P1 theo các tài liệu đó.

Chín WEP bắt buộc tại data/MP1_WRITING_EVIDENCE_FINAL/ đã đọc (đặc biệt brief riêng §2.6.2):

- 03_CHAPTER_2_WRITING_BRIEFS.md
- 01_OUTLINE_BULLET_CROSSWALK.csv
- 02_SECTION_SOURCE_MATRIX.csv
- 05_CROSS_STUDY_COMPARISONS.md
- 06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
- 07_CITATION_AND_REFERENCE_CROSSWALK.csv
- 08_UNRESOLVED_AND_HUMAN_DECISIONS.md
- 09_COVERAGE_AND_READINESS_REPORT.md
- 11_CHAPTER_2_READINESS_GATE.md

Đã truy registry/provenance, JSONL canonical WP-A/WP-B/WP-C/WP-D/Pilot, EquationNotes WP-B và ghi chú nguồn có liên quan. Các record trùng Evidence ID chỉ hợp nhất khi danh tính/nội dung gốc nhất quán; không cấpID mới.

P3/WP-E canonical đã đọc ở worktree /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/: 03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md; P3_GAP_ADJUDICATION.md; P3_DECISION_REPORT.md; 03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md; 02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md; WP_E_ASSUMPTIONS_LIMITATIONS.md. Định nghĩa H0b được đọc từ reconciliation nguyên bản, không dựng lại từ trí nhớ.

## ORIGINAL_OUTLINE_FILE / OUTLINE_BULLETS / READINESS_STATUS

ORIGINAL_OUTLINE_FILE: /home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf
OUTLINE_BULLETS: 3
READINESS_STATUS: BOUNDED_WRITING_READY

SCOPE-01: tiêu đề gốc “2.6.2. Điều còn bất định đối với cấu hình nghiên cứu”; tiêu đề làm việc được user yêu cầu “2.6.2. Những vấn đề hoặc giới hạn còn chưa được giải quyết”. Đổi tên theo ủy quyền nhưng giữ3bullet và phạm vi gốc. Crosswalk ghi page14 cho cả3; đọc trực tiếp PDF cho thấy B01 ở14, B02/B03 ở15. Không sửa Crosswalk/WEP.

| Bullet | Trang PDF vật lý | Nội dung nguyên bản | Câu hỏi bắt buộc | Bằng chứng | Nhóm giới hạn | Vị trí Word |
|---|---:|---|---|---|---|---|
| B01 | 14 | Interface chi phối chưa được khóa; áp suất tại nguồn chưa được chứng minh là normal traction hữu hiệu. | Giao diện nào đã được đo/mô hình hóa, và áp suất được liên hệ với tải pháp tuyến tới đâu? | M13-E04/E06; M15-E02/E05; M16-E02/E05; M31-E06/E08; M34-E02/E04/E07/E09; M38-E02/E03/E04 | SOURCE_LIMITATION; APPLICABILITY_LIMITATION; IDENTIFIABILITY_LIMITATION; MODEL_ASSUMPTION_SIMPLIFICATION; PENDING_HUMAN_DECISION | P02–P04, P11–P13, P15 |
| B02 | 15 | Chưa biết H0b có dự đoán được response pressure-dependent khi transformation, contact và sleeve cùng hoạt động trong miền thí nghiệm hay không. | Điều kiện của mô hình và dữ liệu kiểm tra cho phép đánh giá điều gì khi chuyển sang TiNi có giam giữ? | M15-E03; M16-E03/E04/E05/E06/E07; M18-E01/E02/E06/E07; M22-E01/E02/E03/E04; M26-E01/E03/E04/E05/E07; P3_HYPOTHESIS_RECONCILIATION.md | APPLICABILITY_LIMITATION; IDENTIFIABILITY_LIMITATION; EXPERIMENTAL_COVERAGE_LIMITATION; MODEL_ASSUMPTION_SIMPLIFICATION; PENDING_HUMAN_DECISION | P04–P10, P13–P15 |
| B03 | 15 | Chưa có cơ sở để khẳng định cơ chế mới hoặc universal novelty. | Giới hạn chuyển giao có cho phép suy ra cơ chế mới hoặc tính mới tuyệt đối hay không? | M13-E01/E06; tổng hợp các nguồn bổ sung; P3/WP-E/WEP cho phạm vi nội bộ | EXPERIMENTAL_COVERAGE_LIMITATION; APPLICABILITY_LIMITATION; DOCUMENT_COVERAGE | P01–P02, P14, P16 |

Tên “miền thí nghiệm” trong bullet gốc là câu hỏi nội bộ; draft không coi miền nhiệt/pha/tải hay thiết kế MP1 đã được chốt. Các axis chỉ phục vụ đối chiếu, không biến thành bảy tiểu mục hoặc các kết luận bắt buộc.

## BASELINE_PATHS và nhận diện

Đã đọc bốn DOCX tích hợp/độc lập và các CSV/review liên quan. §2.6.1 có checksum trùng user báo cáo; năm deliverables được bảo toàn riêng dưới đây. Độc lập nghiệm thu §2.6.1 với documented limitations và render6trang ở phiên ngoài là USER_REPORTED, không phải kết quả kiểm độc lập mới trong tác vụ này. Metadata thiếu, đối chứng chọn lọc và MicrosoftWord NOT_VERIFIED của baseline không được nâng mức. §2.5 giữ nguyên hai minorerrata: locatorT015/T016 và cụm lặp “cấu hình tiếp xúc tiếp xúc”.

BASELINE_SHA256_BEFORE / BASELINE_SHA256_AFTER: bảng dưới đếm26file, mỗi file tính lại từ bytes sau tác vụ, không chỉ đọc hash cũ.

| BASELINE_PATH | SHA-256 BEFORE | SHA-256 AFTER |
|---|---|---|
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx | bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec | bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv | 65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be | 65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md | 25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034 | 25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md | e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e | e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv | eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99 | eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv | 54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0 | 54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md | 84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed | 84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md | 09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc | 09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv | 3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23 | 3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md | 0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d | 0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md | 751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70 | 751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv | eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534 | eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx | d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea | d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv | d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49 | d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv | a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5 | a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md | b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d | b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv | 229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1 | 229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx | cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc | cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv | 70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff | 70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md | d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5 | d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md | 3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2 | 3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md | 03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97 | 03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97 |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx | 983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e | 983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv | bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a | bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv | b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c | b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c |
| /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md | 0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca | 0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca |

BASELINES_UNCHANGED: YES (26/26)
INPUT_SUPPORT_FILES_UNCHANGED: YES (241/241; gồm PDF, readingpack, WEP, P3/WP-E và các file hỗ trợ, không đồng nghĩa241file đều được đọc nội dung).

## SOURCE_PAPERS / VERIFIED_PDFS / EVIDENCE_IDS

SOURCE_PAPERS: 9 (M13,M15,M16,M18,M22,M26,M31,M34,M38; gồm7journal,1conference,1hướng dẫn phương pháp)
VERIFIED_PDFS: 10 (9PDF nội dung + M28 chỉ kiểm paginationM26)
UNVERIFIED_PDFS: 0 trong tập nguồn được dùng; không kiểm toàn39PDF của corpus.
EVIDENCE_IDS: 41

Bốn nguồn lõi theo SourceMatrix/Brief là M13-E05,M15-E03,M16-E03,M18-E02. Chỉ bổ sung nội bộ corpus các nguồn thực cần cho đối chiếu. M28 không được tính thành reference nội dung, không có claim cơ học dựa trên M28. Không tìm kiếm tài liệu mới trên Internet hay thay corpus. Network dùng tải renderer, không dùng bổ sung chứng cứ khoa học.

Mức xác minh: bảng metadata/locator và phần nguồn trong CSV được nhóm đọc trực tiếpPDF, ROOT trực tiếp kiểm những diễn giải quyết định, M38 vàM28. SOURCE_WORKER/AGENT_REPORTED về việc kiểm nguồn không có nghĩa ROOT tái đọc toàn bộ mọi trang. CSV có verification_provenance, direct packet và original record; inference không biến thành kết luận nguyên văn. Báo cáo này không chứng nhận toàn bộ phương trình/tính toán hoặc mọi kết luận của bài.

| Số trích dẫn | Paper | PDF canonical | SHA-256 | Cơ sở metadata / giới hạn |
|---:|---|---|---|---|
| 1 | M13 | data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf | 3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f | Ordered authors/title/year/DOI from PDF first page; journal/volume and endpoint pages verified in PDF; title/year/DOI/path/hash agree with canonical registry. |
| 2 | M15 | data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf | b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63 | Physical PDF p1 author/title/header/DOI; final physical page for page range. |
| 3 | M16 | data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf | 1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a | Physical PDF p1 author/title/header/DOI; final physical page for page range. |
| 4 | M18 | data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf | 95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd | Danh tính từ first page canonicalPDF; chi tiết gói kiểm trong source_identity_metadata của CSV. |
| 5 | M22 | data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf | 9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe | Danh tính từ first page canonicalPDF; chi tiết gói kiểm trong source_identity_metadata của CSV. |
| 6 | M26 | data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf | 00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9 | Danh tính từ first page canonicalPDF; chi tiết gói kiểm trong source_identity_metadata của CSV. |
| 7 | M31 | data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf | 65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03 | Ordered authors/title/year/DOI from PDF first page; journal/volume and endpoint pages verified in PDF; title/year/DOI/path/hash agree with canonical registry. |
| 8 | M34 | data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf | 55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782 | Ordered authors/title/year/DOI from PDF first page; journal/volume and endpoint pages verified in PDF; title/year/DOI/path/hash agree with canonical registry. |
| 9 | M38 | data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf | 41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c | Danh tính từ first page canonicalPDF; chi tiết gói kiểm trong source_identity_metadata của CSV. |

Danh sách Evidence IDs thực dùng: M13-E01, M13-E03, M13-E04, M13-E05, M13-E06, M15-E01, M15-E02, M15-E03, M15-E05, M16-E01, M16-E02, M16-E03, M16-E04, M16-E05, M16-E06, M16-E07, M18-E01, M18-E02, M18-E03, M18-E06, M18-E07, M22-E01, M22-E02, M22-E03, M22-E04, M26-E01, M26-E03, M26-E04, M26-E05, M26-E07, M31-E01, M31-E06, M31-E08, M34-E02, M34-E04, M34-E07, M34-E08, M34-E09, M38-E02, M38-E03, M38-E04.

## SOURCE_CORRECTIONS_AND_COUNTEREVIDENCE

- M13: đã có nguyên mẫu nylon dùng áp dương và phép thử uốn; không gọi áp dương là cơ chế chưa từng được chứng minh. Một nguyên mẫu/loại/đường kính/số sợi là giới hạn tổng quát hóa, không phủ nhận các lần lặp điều kiện. Quan hệ bậc hai vùng chuyển tiếp là phenomenological; E từ uốn tại0kPa là hiệu dụng, chưa độc lập đo vật liệu. R²=0.4475 ởPDF10/in490 là hồi quy ngưỡng lực cắt bắt đầu trượt theo áp suất khi uốn ngang, không là sai số toàn mô hình; không đưa số này vào draft vì không cần thiết.
- M13 Eq.(4): PDF3/in483 và WP_B_EQUATION_NOTES.md đã đọc. NOTE B-06/B-07 không bao phủEq4; note có applicability trực tiếpMP1 và SHA không khớp. SHA ghi cho PDF trong note=3aa8790db0be1b0586e379d7ec4fe9be2a6d7139174f74d081ec352e0085a676; canonicalPDFSHA=3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f. Biểu thức quán tính ởEq4 mang dạng mômen bậc nhất nên giữ cảnh báo thứ nguyên. Không sao chép/tự sửa/phát sinh phương trình hoặc dùng lỗi này để bác bỏ toàn mô hình; không là claim được dùng trong manuscript.
- M15/M16 Proposition1: locator đúngPDF4/in12730 vàPDF6/in2224, khác locator gốc trong record. Stability là cục bộ gần manifold, áp chân không hằng/strictlypositive magnitude và sau khi lực gân bằng0. Tăng áp làm trạng thái gần tập cân bằng theo diễn giải nguồn; không nói đã chứng minh miền hút nở đơn điệu hoặc ổn định toàn cục.
- M15/M16: M16 đã mở rộng ánh xạ áp phi tuyến và đàn hồi phụ thuộc áp, xử lý một phần giới hạn tuyến tính của M15. uP>0 là độ lớn chân không/áp âm tương đối khí quyển, không nguồn áp dươngMP1. M15Fig3 PDF5 dùng5lớp tới80kPa, không2lớp tới40 như record cũ. M16 fit/điều khiển độ cứng dùng2lớp0–40kPa; khóa hình5lớp tới80 là nhóm riêng. Đường nét đứt3.7315uP+154.2731 là comparator tuyến tính cũ, không hồi quy mới. Có thí nghiệm sau nhận dạng, không chỉ lý thuyết; cùng tuyến tác giả không là replication độc lập.
- M16metadata: PDF là bản phân trang IEEE TCST34(5),2219–2233,2026; không ghi advance-online chưa phân trang. Không sửa registry.
- M18: liên tục hóa ở tổng chiều cao cố định, lớp mỏng và số lớp đủ lớn; nhận xét xấp xỉ10lớp trong đối chiếuFEA có giới hạn hình học, không ngưỡng số dâyMP1. Giới hạn đầu dầm/fullslip và bỏ ứng suất pháp theo chiều dày là đối chiếu trường vớiFEA; thí nghiệmPVC cantilever về lực–độvõng là một loại bằng chứng khác. Có model và experimentalcomparison, không phủ nhận đóng góp.
- M22: có interwire slip; lớp chữ nhật/độ cong và độ võng chung/không tách ngang-đứng là lý tưởng hóa. k khớp trên dữ liệu cáp thépChen chịu kéo và uốn, gộp áo cáp/Poisson, không là mu thuần hoặc k(piston). DOI đầy đủ từ firstpagePDF:10.1061/(ASCE)ST.1943-541X.0002171, khác DOI bị cắt trong hồ sơ canonical.
- M26: đã có DSC/DIC/IR và tải chu trình, không chỉ đường toàn cục. Hai cấu trúc khác cả vật liệu và hình học; kéo gần đẳng nhiệt nhiệt độ phòng không tự chuyển sang uốn có giam giữ. Bảnproofcanonical có xxx ởvolume/pages; pagination50,3009–3026 được đối chiếu tại M28PDF19, bibliography ref14, không đoán issue. Đây là correction có nguồn trong corpus, chưa đối chiếu finalpublisherPDF.
- M31: có kéo riêng một dây trongcao su để đo ma sát (PDF5–6;5mm,10mm/min,10lần lặp), là phản chứng với phát biểu mọi nghiên cứu chỉ đo đáp ứng uốn toàn cục. Không suy số đo lực ấy là trường pháp tuyến hoặc ma sát dây–dâyTiNi. PDF7/in6588 nêu sai số gần đúng cung tròn khi uốn lớn và ma sát có thể đổi trong cùng pha danh định.
- M34: đã có đo áp tĩnh/flow/displacement. Mô hình thiết kế bỏ ảnh hưởng fluid tại điểm dừng đầu-cuối với100%A/M, không toàn bộ bài bỏ dynamics. Lòxo-vỏsilicone không là pistonMP1. Không tạo định luật hoặc kích thước piston.
- M38: trang vật lý20–21/in8–9 mô hình phép đo Eq1, khôngEq4như record cũ; PDF31/in19 Eq10,PDF33/in21 Eq13,PDF35/in23 Eq18,PDF36/in24coverage. Chỉ dùng khung đo lường/bất định, không sao chép phương trình và không gọi là thực nghiệmMP1.

Những correction trên chỉ nằm trong output mới. source_identity_metadata, canonical_locator_original, accepted_evidence_lookup giữ thông tin cũ; accepted_evidence_locators giữ gói đối chiếu và lý do mới. Tên source_A/B/C.json trong gói là nhãn lịch sử của tệp tạm, nội dung liên quan đã được nhúng trong CSV; không cần tệp tạm để truy chứng cứ.

## ACTUAL_COUNTS

Các số đếm từ DOCX/CSV cuối và parsing chương trình, DIRECTLY_VERIFIED. prose_words là đếm token tách khoảng trắng, không số từ ngôn ngữ học tiếng Việt.

| Trường | Giá trị |
|---|---:|
| PROSE_PARAGRAPHS | 16 |
| PROSE_WHITESPACE_TOKENS | 2322 |
| CLAIM_RECORDS | 72 |
| BODY_CLAIM_RECORDS | 61 |
| GLOSSARY_DEFINITION_RECORDS | 11 |
| LIMITATION_RECORDS | 46 |
| SCIENTIFIC_LIMITATION_RECORDS | 43 |
| PENDING_CHOICE_RECORDS | 3 |
| TERMINOLOGY_ENTRIES | 11 |
| GLOSSARY_ENTRIES | 11 |
| REFERENCES | 9 |
| UNIQUE_DOIS | 8 |
| CITATION_OCCURRENCES | 36 |
| BODY_CITATION_OCCURRENCES | 17 |
| GLOSSARY_CITATION_OCCURRENCES | 19 |
| SCIENTIFIC_TABLES | 0 |
| GLOSSARY_TABLES | 1 |
| FIGURES | 0 |
| OMML_EQUATIONS | 0 |

CLAIM_CATEGORY_COUNTS:

```json
{
  "DOCUMENT_COVERAGE": 4,
  "SOURCE_GROUNDED_CLAIM": 25,
  "INFERENCE": 39,
  "P3_INTERNAL_DEFINITION": 1,
  "PENDING_HUMAN_DECISION": 3
}
```

AUTHOR_PROPOSAL: 0; AUTHOR_DERIVATION: 0. SOURCE_GROUNDED_CLAIM chỉ trực tiếp mô tả nguồn;39INFERENCE gồm11định nghĩa/ngữ cảnh tổng hợp trong glossary.

LIMITATION_CATEGORY_COUNTS (đa nhãn, chỉ các claim giới hạn thân bài):

```json
{
  "EXPERIMENTAL_COVERAGE_LIMITATION": 10,
  "MODEL_ASSUMPTION_SIMPLIFICATION": 12,
  "SOURCE_LIMITATION": 4,
  "IDENTIFIABILITY_LIMITATION": 12,
  "APPLICABILITY_LIMITATION": 18,
  "PENDING_HUMAN_DECISION": 3
}
```

LIMITATION_BASIS_COUNTS (đa nhãn):

```json
{
  "LIMITATION_EXPLICITLY_STATED": 12,
  "LIMITATION_FROM_METHOD": 14,
  "CROSS_STUDY_INFERENCE": 14,
  "NOT_ESTABLISHED_IN_REVIEWED_CORPUS": 3,
  "HUMAN_DECISION_PENDING": 3
}
```

46record giới hạn gồm43 phân tích cơ học/phạm vi/giả thiết và3record pending; không phải46vấn đề độc lập, không phải46researchgaps. Năm nhóm quyết định được gộp trong3record, không mất nhóm. Tổng đa nhãn có thể lớn hơn46. DOCUMENT_COVERAGE và glossary không tính thành kết quả nghiên cứu mới. Không gắn nhãn independentvalidation cho các thành phần chỉfit.

EVIDENCE_CLASS_COUNTS (record đa nhãn; bao gồm component của inference và glossary, không đếm là thử nghiệm mới):

```json
{
  "NOT_APPLICABLE": 8,
  "EXPERIMENTALLY_DEMONSTRATED": 36,
  "CALIBRATION_SUPPORTED": 22,
  "MODEL_DERIVED": 46,
  "COMPARATOR_ONLY": 37,
  "NUMERICALLY_DEMONSTRATED": 11
}
```

## DOCX_ZIP_XML_STATUS / WORD_RENDER_VALIDATION

DOCX_ZIP_XML_STATUS: VALID
WORD_RENDER_VALIDATION: PASS_LIBREOFFICE_VISUAL
MICROSOFT_WORD_VALIDATION: NOT_VERIFIED
RENDERED_PAGES: 6
RENDERER: LibreOffice24.2.7.2 420(Build:2), headless

Ban đầu không có renderer hệ thống; tải52góiapt chính choLO (95,194,284bytes) và phụ trợ chẩn đoánstrace, giải nén/config riêng trong thư mục tạm, không cài hay đổi hệ thống/input. Dùng font TimesNewRoman thực được fc-match xác nhận. Cảnh báo javaldx không cản chuyển đổi; process kết thúc0 và PDF có6trang. Các file renderer/PDF/PNG chỉ là tạm và được dọn, không là deliverablethứ6.

Bản đầu dư một trang do đoạn cuối tràn; ROOT rút ngắn câu mở đầu/kết thúc trùng ý, không thay nguồn/kết luận, render lại bản cuối6trang rồi chạy lại QA liên quan. Không tạoR2/R3 hoặc thay baseline.

ROOT đã xem đủ6trang của bảnPDF cuối. Visual review trực tiếp:

```json
{
  "reviewer": "ROOT",
  "authority": "SELF_REVIEW",
  "renderer": "LibreOffice 24.2.7.2 420(Build:2)",
  "docx_sha256": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63",
  "pdf_sha256": "8d603e188fe7a74ad38857317c59fd3f8818098d2428f37c0f9d82c78e911cd1",
  "pages": 6,
  "status": "PASS_LIBREOFFICE_VISUAL",
  "microsoft_word": "NOT_VERIFIED",
  "observations": {
    "1": "Title and prose legible; margins and continuation to page2 intact.",
    "2": "Prose and citations legible; continuation to page3 intact.",
    "3": "End of scientific prose and short transition to section2.6.3; no next section drafted.",
    "4": "Native glossary title/caption/table fit; rows intact.",
    "5": "Glossary continues with repeated header and two intact final rows. Space below is intentional before references pagebreak.",
    "6": "All nine references visible and legible; no cropped DOI or symbols."
  },
  "blank_pages": 0,
  "clipped_text": 0,
  "overflown_tables": 0,
  "lost_symbols_observed": 0
}
```

DOCX có một nativeglossarytable3cột,12hàng gồmheader, headerlặp, không chia hàng; cỡchữglossary10pt, prose12pt, A4/lề/giãn dòng theo mẫu. Không header/footerparts/cover/statusmetadata. Sáu trang bố cục:1–3thân;4–5glossary;6references. Khoảng trắng cuối trang5 là hệ quả giữ hàng và bắt đầu references ởtrang mới, không là trang trắng bất thường.

## BOUNDED_QA_STATIC_ARCHIVE

Báo cáo WorkerH đầy đủ dưới đây là staticQA cùng phiên; sau lượt đó ROOT chỉ thay đường dẫn provenance nội bộ authorcoverage từ tệp tạm sang mụcROOT_SCIENTIFIC_ADJUDICATION_ARCHIVE trong báo cáo này. Nội dung Word/hash/anchor không thay; finalvalidation chạy lại cả72mapping.

```json
{
  "status": "SELF_REVIEW",
  "review_type": "static bounded QA",
  "scope": "Static bounded QA only. Root owns source/PDF science verification; visual rendering is handled separately.",
  "counts": {
    "zip_xml_valid": true,
    "docx_sha256": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63",
    "word_paragraphs_total": 29,
    "body_paragraphs_expected_actual": {
      "expected": 16,
      "actual": 16
    },
    "body_anchor_units_expected_actual": {
      "expected": 61,
      "actual": 61
    },
    "body_paragraphs_exact_match": true,
    "body_anchor_units_verified": 61,
    "glossary_table_count": 1,
    "glossary_rows_actual": 11,
    "glossary_rows_exact": 11,
    "trace_rows": 72,
    "trace_locators_exact": 72,
    "trace_body_units_covered_once": true,
    "claim_category_actual": {
      "DOCUMENT_COVERAGE": 4,
      "SOURCE_GROUNDED_CLAIM": 25,
      "INFERENCE": 39,
      "P3_INTERNAL_DEFINITION": 1,
      "PENDING_HUMAN_DECISION": 3
    },
    "claim_category_expected_stats": {
      "DOCUMENT_COVERAGE": 4,
      "SOURCE_GROUNDED_CLAIM": 25,
      "INFERENCE": 39,
      "P3_INTERNAL_DEFINITION": 1,
      "PENDING_HUMAN_DECISION": 3
    },
    "body_claim_records_actual": 61,
    "glossary_claim_records_actual": 11,
    "limitation_records": 46,
    "scientific_limitation_records": 43,
    "pending_human_decision_limitation_records": 3,
    "limitation_category_multilabel_actual": {
      "EXPERIMENTAL_COVERAGE_LIMITATION": 10,
      "MODEL_ASSUMPTION_SIMPLIFICATION": 12,
      "SOURCE_LIMITATION": 4,
      "IDENTIFIABILITY_LIMITATION": 12,
      "APPLICABILITY_LIMITATION": 18,
      "PENDING_HUMAN_DECISION": 3
    },
    "limitation_category_multilabel_expected": {
      "EXPERIMENTAL_COVERAGE_LIMITATION": 10,
      "MODEL_ASSUMPTION_SIMPLIFICATION": 12,
      "SOURCE_LIMITATION": 4,
      "IDENTIFIABILITY_LIMITATION": 12,
      "APPLICABILITY_LIMITATION": 18,
      "PENDING_HUMAN_DECISION": 3
    },
    "limitation_basis_multilabel_actual": {
      "LIMITATION_EXPLICITLY_STATED": 12,
      "LIMITATION_FROM_METHOD": 14,
      "CROSS_STUDY_INFERENCE": 14,
      "NOT_ESTABLISHED_IN_REVIEWED_CORPUS": 3,
      "HUMAN_DECISION_PENDING": 3
    },
    "limitation_basis_multilabel_expected": {
      "LIMITATION_EXPLICITLY_STATED": 12,
      "LIMITATION_FROM_METHOD": 14,
      "CROSS_STUDY_INFERENCE": 14,
      "NOT_ESTABLISHED_IN_REVIEWED_CORPUS": 3,
      "HUMAN_DECISION_PENDING": 3
    },
    "glossary_rows_counted_as_limitation": 0,
    "mandatory_limitation_fields_present": {
      "limitation_category": true,
      "limitation_basis": true,
      "scope_of_negative_claim": true
    },
    "mandatory_limitation_fields_nonempty_all_rows": {
      "limitation_category": 72,
      "limitation_basis": 72,
      "scope_of_negative_claim": 72
    },
    "evidence_ids_referenced": 41,
    "evidence_ids_all_exist_in_checked_map": true,
    "internal_P3_and_pending_records": 4,
    "internal_only_records_have_no_journal_paper_eid_doi": true,
    "pending_human_decisions_not_scientific_gaps": true,
    "canonical_inherited_header_fields_present": {
      "source_section": true,
      "original_claim_id": true,
      "integrated_claim_id": true,
      "integrated_document_location": true,
      "claim_category": true,
      "claim_summary": true,
      "paper_id": true,
      "evidence_id": true,
      "canonical_doi": true,
      "source_locator": true,
      "source_role": true,
      "verification_status": true,
      "retention_status": true,
      "original_record_json": true,
      "accepted_evidence_lookup": true
    },
    "canonical_three_limitation_fields": [
      "limitation_category",
      "limitation_basis",
      "scope_of_negative_claim"
    ],
    "citation_first_appearance_body_then_glossary": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "body_citation_numbers": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "glossary_citation_numbers": [
      1,
      2,
      3,
      4,
      5,
      6,
      8,
      9
    ],
    "bibliography_reference_entries": 9,
    "reference_metadata_entries": 9,
    "references_author_title_doi_match": 9,
    "unique_dois_nonempty": 8,
    "references_without_doi": 1,
    "citation_occurrences_body_table": 36,
    "forbidden_internal_markers": 0,
    "next_section_heading_count": 0,
    "final_sentence_next_section_reference_only": true,
    "omml_equations": 0,
    "drawings_or_figures": 0,
    "header_footer_parts": [],
    "page_size_twips": {
      "width": "11906",
      "height": "16838"
    },
    "body_typography_default": {
      "font": "Times New Roman",
      "size_half_points": "24",
      "run_mismatch_count": 0
    },
    "native_table_layout": [
      {
        "rows": 12,
        "header_repeat": true,
        "all_rows_no_split": true,
        "layout": [
          "fixed"
        ],
        "grid_widths_twips": [
          "2551",
          "5386",
          "1134"
        ]
      }
    ],
    "bounded_language_review": {
      "absolute_or_novelty_term_occurrences": 10,
      "review": "Manual read of all 16 approved paragraphs. Negative claims are bounded to named sources, conditions, measured quantities, and transfer to MP1; pending decisions remain explicitly author choices. P14 keeps the ordinary TiNi/pressure/contact comparator open and does not claim impossibility or novelty. P06 distinguishes calibration data from post-identification tests and independent prediction. No P3 status transition is asserted."
    },
    "p3_status_change_claimed": false,
    "visual_rendering_checked": false,
    "scope": "Static bounded QA only. Root owns source/PDF science verification; visual rendering is handled separately.",
    "selected_stats_match": {
      "prose_paragraphs": true,
      "claim_records": true,
      "body_claim_records": true,
      "glossary_claim_records": true,
      "limitation_records": true,
      "glossary_entries": true,
      "references": true,
      "unique_dois": true,
      "evidence_ids": true
    },
    "terminology_csv_rows": 11,
    "candidate_docx_sha256_matches_stats": true
  },
  "findings": [],
  "limitations": [
    "No visual rendering was inspected by this worker; root handles isolated LibreOffice rendering.",
    "No independent PDF/source corpus re-verification was performed; root states the scientific source verification is complete.",
    "The linguistic review is bounded to claims, scope, calibration/validation, novelty/impossibility framing, and pending decision status; it is not an independent scientific adjudication."
  ]
}
```

## SEVEN_GATE_RESULT

| Gate | Status |
|---|---|
| GATE_1 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_2 | PASS |
| GATE_3 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_4 | PASS |
| GATE_5 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_6 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| GATE_7 | PASS_WITH_DOCUMENTED_LIMITATIONS |

Checklist/method/evidence/findings/severity/unresolved cụ thể trong MP1_CH2_2_6_2_7_GATE_REVIEW.md, không copyPASS từ baseline.

## UNRESOLVED_FINDINGS

- P1: NONE identified trong phạm vi self-review; P2: NONE identified. Không hàm ý không thể còn lỗi chưa phát hiện.
- DOC/SCOPE: giữ khác biệt tên theo ủy quyền và correction trang của outline/canonicallocators, không sửa hồ sơ gốc.
- META: issue không được xác minh thì không ghi; M26pagination crosscheck từ nguồn trong corpus, chưa kiểm publisher-finalmetadata ngoài corpus.
- SOURCE: đối chứng những phần phục vụ claim; không thực hiện lại toàn bộproof, rawdata hoặc39PDF, không có independentexternalrecheck của toàn bộ nguồn trong task.
- RENDER: MicrosoftWord NOT_VERIFIED; LO6trang đã xem; bố cục có thể thay ở ứng dụng/font khác.
- APPLICABILITY: không có dữ liệu MP1 để khẳng định quan hệ áp–ma sát–uốn, tính nhận dạng hoặc quy luật riêng đã được kiểm chứng.
- METADATA_PRESERVATION: hash nội dung input không đổi; atime không đo nên không tuyên bố toàn bộ metadata bất biến.

## PENDING_HUMAN_DECISIONS

1. Hình học bó dây, topology và giao diện tiếp xúc chi phối.
2. Cách biểu diễn/đo hoặc suy tải pháp tuyến cục bộ.
3. Miền nhiệt độ, pha, tốc độ và lịch sử tải TiNi.
4. Đại lượng độ cứng chính và mô hình bất định/quan sát.
5. Phạm vi đóng góp/kiểm chứng SMA–piston.

Không chốt năm lựa chọn, không đóng băngBenchA/BenchB. H0b=NOT_FALSIFIED_LIVE_COMPETITOR; H1=INSUFFICIENT_EVIDENCE. G00đãđóng, G01–G08giữcóđiềukiện; không thay P3 hoặc dùng vấn đề nội bộ làm noveltyproof.

## FILES_CREATED

- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md
- /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md

Đúng5finaldeliverables, khôngPDF/ảnh/scriptphụ trong thư mục cuối. Những nội dung provenance cần giữ được nhúng trong haiCSV và báo cáo này, không chỉ để ởterminal. Citation cục bộ[1]–[9] có thể renumber khi tích hợp §2.6 theo chính sách sau, không tự renumber bất kỳbaseline nào.

## GIT_CHANGE_SCOPE / COMMIT_STATUS / PUSH_STATUS

Trước tác vụ có338dònggitstatus. Hai trackedmodifications đã có sẵn: outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py và chapter2_readable_draft.md; không sửa. Toàn bộ untracked có sẵn được bảo toàn; snapshottrước bên dưới để phân biệt5filemới.

GIT_CHANGE_SCOPE: ONLY_FIVE_NEW_SECTION_2_6_2_FILES; đối chiếu gitstatus sau khi loại đúng5path mới phải khớp nguyên snapshot trước. Khôngcheckout/merge/reset/pull/stage/commit/push/PR.
COMMIT_STATUS: NOT_PERFORMED
PUSH_STATUS: NOT_PERFORMED

<details><summary>Git status preflight nguyên trạng</summary>

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
```

</details>

## ROOT_SCIENTIFIC_ADJUDICATION_ARCHIVE

Đây là quyết định soạn thảo của ROOT lưu để thay tệp tạm root_synthesis.md; không phải nguồn journal. Bản tổng hợp trước khi viết giữ đầy đủ dưới đây. Một số dự định đã được tinh giản ở bản cuối:11thuậtngữ,16đoạn,khôngR²địnhlượng trongthân. Bản Word/CSV cuối là trạng thái sử dụng thực tế.

# ROOT phê duyệt tổng hợp §2.6.2

Tiêu đề Word theo yêu cầu: **2.6.2. Những vấn đề hoặc giới hạn còn chưa được giải quyết**. Tiêu đề gốc PDF/WEP: **Điều còn bất định đối với cấu hình nghiên cứu**. Đây là đổi tên được ủy quyền trực tiếp, giữ nguyên ba bullet. PDF canonical đã đọc/quan sát trang14–15. Crosswalk ghi cả ba ở14 là locator chưa đầy đủ: B01 ở14; B02/B03 ở15.

B01 nguyên văn: Interface chi phối chưa được khóa; áp suất tại nguồn chưa được chứng minh là normal traction hữu hiệu.
B02 nguyên văn: Chưa biết H0b có dự đoán được response pressure-dependent khi transformation, contact và sleeve cùng hoạt động trong miền thí nghiệm hay không.
B03 nguyên văn: Chưa có cơ sở để khẳng định cơ chế mới hoặc universal novelty.

Readiness: BOUNDED_WRITING_READY, không nâng thành fully established scientific knowledge. Ba bullet là ranh giới nội dung, không được gọi tám mã G là tám kết quả.

## Nguồn và vai trò

Chỉ dùng chín nguồn nội dung M13, M15, M16, M18, M22, M26, M31, M34, M38. Bốn nguồn đầu là lõi brief, giữ thứ tự xuất hiện này. Sáu nguồn từ §2.6.1 không tự động bắt buộc: chỉ chọn M18/M22/M26/M31/M34/M38 thực sự cần cho giới hạn. Không dùng M09/M11/M14/M17 để kéo dài bản thảo. M28 chỉ metadata M26, không reference nội dung. M38 là hướng dẫn phương pháp, không thực nghiệm.

Citation cục bộ: [1]M13 [2]M15 [3]M16 [4]M18 [5]M22 [6]M26 [7]M31 [8]M34 [9]M38. P3 và WEP là nguồn quản lý định nghĩa/decision nội bộ, không biến thành journal. Chỉ các câu phạm vi/giả thuyết/quyết định trong phần cuối mới cần mapping nội bộ; không bắt nguồn journal gánh định nghĩa H0b.

Phân loại giới hạn cần dùng trong CSV: SOURCE_LIMITATION, APPLICABILITY_LIMITATION, IDENTIFIABILITY_LIMITATION, EXPERIMENTAL_COVERAGE_LIMITATION, MODEL_ASSUMPTION_SIMPLIFICATION, PENDING_HUMAN_DECISION. Cơ sở: LIMITATION_EXPLICITLY_STATED, LIMITATION_FROM_METHOD, CROSS_STUDY_INFERENCE, NOT_ESTABLISHED_IN_REVIEWED_CORPUS, HUMAN_DECISION_PENDING. Đây không phải thang xếp hạng. Suy từ phương pháp vẫn là INFERENCE nếu kết luận giới hạn do người viết rút ra; câu trực tiếp mô tả giả thiết đã viết trong Methods có thể SOURCE_GROUNDED_CLAIM. Không lẫn category và source role.

## Chuỗi lập luận được phép triển khai

Soạn 15–17 đoạn liên tục khoảng 1800–2400 từ tách khoảng trắng, không tiểu đề axis, không bảng khoa học/hình/phương trình. Có glossary3cột khoảng12thuật ngữ sau thân và references. Bản thảo chỉ tiếng Việt, ngoại lệ tên riêng, ký hiệu và tên xuất bản/thuật ngữ glossary. Không đưa Pxx/ID/tag/workflow vào Word.

P01. Chuyển tiếp ngắn từ kết quả đã có cơ sở sang miền áp dụng. Tuyên bố phạm vi do tác giả, DOCUMENT_COVERAGE; không lặp kết quả §2.6.1. Đừng cho nguồn xuất hiện sớm sai citation order.

P02. M13 [1], E05/E06. Áp dương kẹt sợi đã được thử, vì vậy không coi bản thân cơ chế ép bằng áp dương là hoàn toàn bỏ ngỏ. Giới hạn trực tiếp là một loại mẫu/đường kính/số sợi; quan hệ bậc hai trong vùng chuyển tiếp là gần đúng hiện tượng luận (E03/E06). Có thể nêu R²=0,4475 của hồi quy ngưỡng lực cắt bắt đầu trượt theo áp suất ở chế độ uốn ngang, nhưng nếu không có giá trị lập luận thì bỏ khỏi thân và giữ report. Không đổi R² thành sai số hay phán quyết toàn mô hình. Các cơ chế ngẫu nhiên stick-slip/truyền áp không đều/packing chỉ là nguyên nhân khả dĩ do nguồn đề xuất, không được đo tách để khẳng định nguyên nhân.

P03. M13 E04/E06. Đã đo lực–độ võng và áp bladder; môđunE được xác định hiệu dụng từ uốn tại0kPa, không phải đo vật liệu độc lập. Những đại lượng được suy từ slope vàE này không tự là đo môđun riêng hoặc trường pháp tuyến cục bộ. Phân biệt p_source/p_specimen/local traction; không tuyên bố nguyên lý không thể suy lực. Cái chưa được chứng minh là ánh xạ chuyển giao tới cấu hình MP1, không phải phủ nhận số đo áp suất của nguồn.

P04. M15 [2] và M16 [3], E02/E05 và E02/E05. M15 giả thiết quan hệ tỷ lệ áp suất–tải pháp tuyến gộp và đàn hồi không phụ thuộc áp. M16 đã thay bằng hàm tác động áp suất đơn điệu chưa biết và cho phép hệ số đàn hồi phụ thuộc áp; nhận dạng trên dữ liệu của nền tảng nguồn. Ghi nhận đây là xử lý một phần giới hạn trước, không nói chưa ai xét tính phi tuyến áp suất. Cả hai vẫn dùng mô tả gộp và áp suất phân bố đều theo giả thiết, không đo trường lực tại mọi giao diện dây MP1. uP>0 trong hai bài là độ lớn chân không tương ứng áp âm, không áp dương củaMP1.

P05. M15-E03 / M16-E03. Khóa hình và ổn định tiệm cận của tập cân bằng được xét cục bộ, không input gân, áp suất chân không hằng và dưới giả thiết nguồn. Áp suất lớn hơn được luận giải là đưa trạng thái ban đầu gần tập cân bằng; KHÔNG gọi là chứng minh miền hút nở đơn điệu hay ổn định toàn cục. Các kết quả không tự là định luật B(p) của bó dây TiNi hoặc giữ hình dưới tải bất kỳ. Không chép mệnh đề/phương trình.

P06. M16 E04/E05/E06/E07. Có thí nghiệm khóa hình và điều khiển sau nhận dạng, không được nói mô hình chỉ lý thuyết. Tách phép đo độ cứng ngang đầu mút/quan hệ cân bằng dùng hiệu chuẩn khỏi phép kiểm tra điều khiển. Hai lớp0–40kPa cho fit/regulation khác nhóm khóa hình5lớpđến80kPa; không gộp để mở rộng miền fit. M15/M16 chung tuyến phát triển nên không tính là replication độc lập. Phần giữ lại choMP1 là yêu cầu rõ phạm vi và loại dữ liệu; không cần protocol cuối.

P07. M18 [4], E01/E02. Mô hình liên tục xử lý nhiều lớp, là đóng góp bổ sung phương pháp chứ không thiếu mô hình homogenized. Điều kiện lớp mỏng so chiều cao toàn dầm, giữ chiều cao và nhiều lớp; n xấp xỉ10trởlên là quan sát/điều kiện trong so sánhFEA nguồn, không ngưỡng số dâyMP1. Có thể viết bằng chữ, không chèn phương trình.

P08. M18 E07/E06. Giới hạn được nguồn nói rõ là gần đầu dầm, vùng trượt lớn, sai khác vùng trượt khi bỏ thành phần ứng suất pháp theo chiều dày. Đây là đối chiếu vớiFEA, không gọi là đo trường cục bộ thực nghiệm. Thực nghiệm côngxônPVC có đường lực–độvõngphù hợp là bằng chứng bổ sung cần thừa nhận; không đủ xác nhận mọi trường ứng suất/miền tiếp xúc. Phân biệt full slip không là zero friction và không chứng minh dâyMP1 uốn độc lập; perfectstickcụcbộ không tự thành tiết diện liên hợp hoàn toàn. Chỉ nhắc ranh giới cần cho suy luận, không liệt kê cảnh báo.

P09. M22 [5], E01/E02/E04. Mô hình cáp dây song song đã xét trượt, không gọi tất cả mô hình bỏ qua tương tác. Lý tưởng hóa thành lớp chữ nhật, độ cong/độ võng chung, không tách theo phương ngang/đứng. Tham số chốngtrượt k được khớp từ dữ liệuChen dưới tải kéo và uốn; có đóng góp áo cáp/Poisson theo nguồn. Không gọi tham số gộp ấy là hệ số ma sát vật liệu thuần hoặc luật k(piston). Tách so sánh nghiệm số/hiệu chuẩn/dự đoán độc lập. Không tuyên bố các cận đó đã áp dụngMP1.

P10. M26 [6], E01/E03/E04/E05/E07. Có DSC và trường biến dạng/nhiệt cùng thử kéo gần đẳng nhiệt, chu trình; ghi nhận nguồn đã quan sát vật liệu chứ không chỉ lực–độgiãn. Hai cấu trúc đồng thời khác vật liệu/góc xoắn nên không tách riêng nguyên nhân do hình học; không suy mọi phi tuyến do ma sát hay chuyển pha riêng. Giới hạn chuyển giao từ kéo chậm nhiệt độ phòng sang uốn có giam giữ không là bất khả. Độ trễ và lịch sử tải được giữ; không lấy extrapolated asymptotes làm đo bền lâu; không cần giá trị định lượng.

P11. M31 [7], E06/E01/E08. Thí nghiệm riêng kéo một dây trongốngcao su đã đo ma sát tách khỏi thử uốn; phản chứng cho mệnh đề mọi nghiên cứu chỉ cóFdelta. Nhưng lựcma sát tổng thể tại giao diện dây–cao su không tự cho phân bố pháp tuyến hoặc hệ số ma sát dây–dâyTiNi. SMAởđây siết tiếp xúc trực tiếp, không cơ cấu piston. Nếu không cần biếnnhiệt/tốcđộthuậnlợi thì không kể sốliệuthermal cooling.

P12. M34 [8], E02/E04/E07/E09. Đã đo áp suất tĩnh và đáp ứng bơm, không nói chưacótiềnlệSMAtạoáp. Môhình thiết kế cực trị giới hạn100%A/M ởđiểmđầu/cuối và bỏhiệuứngdịchởđiểmdừng; nguồn vẫn cóthử độnglực/lưulượng riêng, vì vậy không nói toàn bộbàibỏqua quáđộ. Cấu hình lòxo–vỏsilicone không pistontrượtMP1; ápđầurakhác pháp tuyến cục bộ. Giới hạn kếthừa có điều kiện, không thiết kếpistonhoặcchọnthôngsố.

P13. M38 [9] E02/E03/E04 + M13/M16/M22. Giới hạn nhận dạng phải gắn với đại lượng đo và môhìnhphépđo: độ dốc lực–độvõngK, độ cứnguốnB/EI vàE khác; môhìnhphépđo/bấtđịnhđầu vào/tươngquan theoGUM. Hiệu chuẩn hiệu dụng đủ cho dự đoán toàncục trongmiền hẹp không đồng nghĩa tách duy nhất tham sốcục bộ. Không tuyên bố bất khả nhậndạng về nguyên lý, khôngcho cảm biến/độphângiải/ngưỡng cuối cùng. GUMchỉMETHODOLOGY, không thực nghiệmMP1. Không lặp địnhnghĩa dài §2.5.

P14. B02. Những giới hạn trên chưa đủ để kết luận mô hình kế thừa quan hệ cấu thànhTiNi vàtiếpxúc/ma sát thông thườngkhôngthểdựđoán đápứngMP1; cũngchưaphảixácnhậnnóđãđược kiểmchứng. CáchdiễnđạtnàytươngứngH0b livecompetitor trongP3, khôngnóilàkếtquảjournal. Nếu địnhnghĩa đối chứng đượcnhắclại thìclaimcategory=P3_INTERNAL_DEFINITION, sourceRoleCONTEXT_ONLY, sourcepathP3chínhxác, EID/PaperIDjournalđểtrống. Trạngthái chưa phânbiệt trongMP1 gắn NOT_ESTABLISHED_IN_REVIEWED_CORPUS với scope rõ là các nguồn đối chiếu vàP3; khôngglobalabsence. Khôngđòi hỏi luật cấu thành mới.

P15. B01/B02: pendinghuman decisions khôngliteraturegap. Hìnhhọc/giaodiện, biểu diễn lực pháp tuyến; miền nhiệt/pha/lịch sử tải; đại lượng độ cứng/bất định và phạm viSMA–piston vẫn là lựa chọn của đềtài. Ghi nhưchưaquyếtđịnh, khôngtựchốt; sourceP3/WEP categoryPENDING_HUMAN_DECISION với căn cứHUMAN_DECISION_PENDING; khôngbắtjournalchứngminhtrạngtháinộibộ. KhôngnêutênBenchA/B trongmanuscript, khôngthiếtkếprotocol.

P16. B03: thiếu căn cứ chuyển giao không chứng minh cơ chếmới/tínhmớituyệtđối; các phươngpháp đãbổsungcho nhau trong miền của chúng. Tách ba thứ: nguồn công bố giới hạn; người viết suy ranh giới chuyển giao; lựa chọnMP1 cònmở. Đoạn kếtngắnchuyển §2.6.3, khôngphátbiểumộtgapđãxácnhận hoặc tiêuchíthửcuốicùng.

## Kiểm tra đã phê duyệt

Root đọc trực tiếp trang10–11M13, trang4M15, trang6M16, trang2/8M18 và trang giả thiết/kếtquả các nguồn bổ trợ. Các packet source_A/B/C chứa record gốc và correction. ROOT phê duyệt các correction quan trọng: M15Prop1PDF4; M16Prop1PDF6; điều kiệnthử5lớp/80kPaM15 khác2lớp/40kPaM16; ýnghĩaápđưa gần manifold thayvì nởmiềnhút. Khôngdùng các lỗi in phươngtrình làm bằngchứng bácbỏtoànmôhình.

M13EquationNotes không bao phủEq4 và cóSHA/applicabilitykhôngkhớpPDF; chỉgiữcảnhbáotrongreport,khôngcopy/cải biênEq4. KhôngphươngtrìnhđượcchènvàoWord, khôngtạo luậtghépMP1. P3readcanonical: H0bNOT_FALSIFIED_LIVE_COMPETITOR,H1INSUFFICIENT_EVIDENCE,G00đóng,G01–G08cóđiềukiện.


## INPUT_SHA256_MANIFEST_BEFORE_AFTER

241 file/support được snapshot trước và tính lại sau. Mỗi phần tử chứa before/after; một số Zone.Identifier là filephụ Windows, không tính thành nguồn học thuật hoặc file đã đọc. Baseline26file tách riêng ở trên.

```json
{
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx": {
    "before": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "after": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv": {
    "before": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be",
    "after": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md": {
    "before": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034",
    "after": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md": {
    "before": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e",
    "after": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv": {
    "before": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99",
    "after": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv": {
    "before": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0",
    "after": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md": {
    "before": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed",
    "after": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md": {
    "before": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc",
    "after": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv": {
    "before": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23",
    "after": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md": {
    "before": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d",
    "after": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md": {
    "before": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70",
    "after": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv": {
    "before": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534",
    "after": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx": {
    "before": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "after": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv": {
    "before": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49",
    "after": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv": {
    "before": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5",
    "after": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md": {
    "before": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d",
    "after": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv": {
    "before": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1",
    "after": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx": {
    "before": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "after": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv": {
    "before": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff",
    "after": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md": {
    "before": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5",
    "after": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md": {
    "before": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2",
    "after": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md": {
    "before": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97",
    "after": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx": {
    "before": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e",
    "after": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv": {
    "before": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a",
    "after": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv": {
    "before": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c",
    "after": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md": {
    "before": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca",
    "after": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": {
    "before": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
    "after": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md": {
    "before": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
    "after": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md": {
    "before": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
    "after": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md": {
    "before": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
    "after": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md": {
    "before": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
    "after": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md": {
    "before": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
    "after": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md": {
    "before": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
    "after": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv": {
    "before": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
    "after": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md": {
    "before": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
    "after": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": {
    "before": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
    "after": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv": {
    "before": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
    "after": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier": {
    "before": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
    "after": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv": {
    "before": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
    "after": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf": {
    "before": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
    "after": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": {
    "before": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
    "after": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf": {
    "before": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
    "after": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": {
    "before": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
    "after": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf": {
    "before": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
    "after": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf": {
    "before": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
    "after": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf": {
    "before": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
    "after": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/README.md": {
    "before": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c",
    "after": "a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt": {
    "before": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7",
    "after": "89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf": {
    "before": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
    "after": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf": {
    "before": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
    "after": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": {
    "before": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
    "after": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M37__2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": {
    "before": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
    "after": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M30__A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": {
    "before": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
    "after": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf": {
    "before": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
    "after": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt": {
    "before": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d",
    "after": "ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": {
    "before": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
    "after": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf": {
    "before": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
    "after": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf": {
    "before": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03",
    "after": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt": {
    "before": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f",
    "after": "5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf": {
    "before": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
    "after": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf": {
    "before": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
    "after": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt": {
    "before": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837",
    "after": "1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": {
    "before": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
    "after": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": {
    "before": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
    "after": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": {
    "before": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
    "after": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf": {
    "before": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
    "after": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf": {
    "before": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
    "after": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt": {
    "before": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2",
    "after": "db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": {
    "before": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
    "after": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": {
    "before": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
    "after": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": {
    "before": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
    "after": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf": {
    "before": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
    "after": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/MANIFEST.json": {
    "before": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda",
    "after": "9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt": {
    "before": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac",
    "after": "413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M32__2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": {
    "before": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
    "after": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": {
    "before": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
    "after": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf": {
    "before": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a",
    "after": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf": {
    "before": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
    "after": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": {
    "before": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
    "after": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": {
    "before": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
    "after": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf": {
    "before": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
    "after": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf": {
    "before": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0",
    "after": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": {
    "before": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
    "after": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf": {
    "before": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a",
    "after": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt": {
    "before": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db",
    "after": "1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt": {
    "before": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7",
    "after": "f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt": {
    "before": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1",
    "after": "32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": {
    "before": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
    "after": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b"
  },
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": {
    "before": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
    "after": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json": {
    "before": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06",
    "after": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md": {
    "before": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406",
    "after": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md": {
    "before": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79",
    "after": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md": {
    "before": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2",
    "after": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md": {
    "before": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2",
    "after": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv": {
    "before": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6",
    "after": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md": {
    "before": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8",
    "after": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md": {
    "before": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682",
    "after": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv": {
    "before": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd",
    "after": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md": {
    "before": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24",
    "after": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md": {
    "before": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003",
    "after": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md": {
    "before": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1",
    "after": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl": {
    "before": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c",
    "after": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md": {
    "before": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b",
    "after": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv": {
    "before": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e",
    "after": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md": {
    "before": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513",
    "after": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md": {
    "before": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40",
    "after": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md": {
    "before": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b",
    "after": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md": {
    "before": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8",
    "after": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip": {
    "before": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4",
    "after": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip": {
    "before": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e",
    "after": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip": {
    "before": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c",
    "after": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip": {
    "before": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14",
    "after": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md": {
    "before": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7",
    "after": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md": {
    "before": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38",
    "after": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md": {
    "before": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e",
    "after": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json": {
    "before": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1",
    "after": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md": {
    "before": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5",
    "after": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv": {
    "before": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9",
    "after": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md": {
    "before": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da",
    "after": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json": {
    "before": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7",
    "after": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md": {
    "before": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880",
    "after": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md": {
    "before": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d",
    "after": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md": {
    "before": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca",
    "after": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md": {
    "before": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9",
    "after": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md": {
    "before": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8",
    "after": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md": {
    "before": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d",
    "after": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv": {
    "before": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34",
    "after": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md": {
    "before": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907",
    "after": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md": {
    "before": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101",
    "after": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md": {
    "before": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1",
    "after": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl": {
    "before": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba",
    "after": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md": {
    "before": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a",
    "after": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md": {
    "before": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996",
    "after": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md": {
    "before": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d",
    "after": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md": {
    "before": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba",
    "after": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json": {
    "before": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6",
    "after": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md": {
    "before": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213",
    "after": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv": {
    "before": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be",
    "after": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md": {
    "before": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1",
    "after": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md": {
    "before": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda",
    "after": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl": {
    "before": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033",
    "after": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md": {
    "before": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09",
    "after": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md": {
    "before": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087",
    "after": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md": {
    "before": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65",
    "after": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md": {
    "before": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a",
    "after": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md": {
    "before": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a",
    "after": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md": {
    "before": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02",
    "after": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md": {
    "before": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca",
    "after": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md": {
    "before": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037",
    "after": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md": {
    "before": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72",
    "after": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv": {
    "before": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23",
    "after": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv": {
    "before": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9",
    "after": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md": {
    "before": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e",
    "after": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md": {
    "before": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0",
    "after": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv": {
    "before": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2",
    "after": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md": {
    "before": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6",
    "after": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md": {
    "before": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2",
    "after": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json": {
    "before": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3",
    "after": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl": {
    "before": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd",
    "after": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md": {
    "before": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09",
    "after": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md": {
    "before": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79",
    "after": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md": {
    "before": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2",
    "after": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md": {
    "before": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7",
    "after": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv": {
    "before": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7",
    "after": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md": {
    "before": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6",
    "after": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv": {
    "before": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0",
    "after": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md": {
    "before": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753",
    "after": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md": {
    "before": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05",
    "after": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl": {
    "before": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2",
    "after": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md": {
    "before": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed",
    "after": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md": {
    "before": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894",
    "after": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md": {
    "before": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c",
    "after": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md": {
    "before": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109",
    "after": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md": {
    "before": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059",
    "after": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md": {
    "before": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c",
    "after": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md": {
    "before": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864",
    "after": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md": {
    "before": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d",
    "after": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md": {
    "before": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a",
    "after": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md": {
    "before": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f",
    "after": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md": {
    "before": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde",
    "after": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md": {
    "before": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a",
    "after": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md": {
    "before": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80",
    "after": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md": {
    "before": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46",
    "after": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md": {
    "before": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad",
    "after": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md": {
    "before": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160",
    "after": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md": {
    "before": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d",
    "after": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md": {
    "before": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844",
    "after": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md": {
    "before": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11",
    "after": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md": {
    "before": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930",
    "after": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md": {
    "before": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad",
    "after": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md": {
    "before": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf",
    "after": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md": {
    "before": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec",
    "after": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md": {
    "before": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d",
    "after": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md": {
    "before": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2",
    "after": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md": {
    "before": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8",
    "after": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md": {
    "before": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24",
    "after": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md": {
    "before": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf",
    "after": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md": {
    "before": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f",
    "after": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md": {
    "before": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195",
    "after": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md": {
    "before": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034",
    "after": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md": {
    "before": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a",
    "after": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md": {
    "before": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151",
    "after": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md": {
    "before": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284",
    "after": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md": {
    "before": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c",
    "after": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md": {
    "before": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8",
    "after": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md": {
    "before": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344",
    "after": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md": {
    "before": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8",
    "after": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md": {
    "before": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a",
    "after": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md": {
    "before": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c",
    "after": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c"
  },
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md": {
    "before": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee",
    "after": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md": {
    "before": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda",
    "after": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_SOURCE_MAP.csv": {
    "before": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959",
    "after": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_P3_HANDOFF.md": {
    "before": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c",
    "after": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md": {
    "before": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3",
    "after": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md": {
    "before": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e",
    "after": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv": {
    "before": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25",
    "after": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_MODEL_APPLICABILITY_MATRIX.csv": {
    "before": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a",
    "after": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv": {
    "before": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011",
    "after": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md": {
    "before": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9",
    "after": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md": {
    "before": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3",
    "after": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md": {
    "before": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1",
    "after": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md": {
    "before": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58",
    "after": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md": {
    "before": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90",
    "after": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md": {
    "before": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f",
    "after": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv": {
    "before": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201",
    "after": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md": {
    "before": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33",
    "after": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md": {
    "before": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d",
    "after": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md": {
    "before": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5",
    "after": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md": {
    "before": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55",
    "after": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55"
  },
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf": {
    "before": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
    "after": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e"
  }
}
```

## FINAL_REGRESSION_RESULT

Đã mở lại cả5file; DOCX/CSV/glossary/citation và metadata/provenance kiểm theo nội dung, không chỉ count. Mọi sourcePDFpath/EID tồn tại. Input241hash và26baselinehash không đổi. Word0internalmarkers,0nextsectionheadings; chỉthamchiếu§2.6.3cuốicùng. Chínhxác5file khôngrỗng. Gitstatusngoàiphạmvikhớpsnapshotpreflight. Khôngcommit/push.

Giới hạn kiểm tra: SELF_REVIEW, không nghiệm thu độc lập, không MicrosoftWord validation, không tái chứng minh toàn bộ39nguồn. Kết quả là bản thảo dùng để chuyển cho người kiểm định ngoài phiên.

FINAL_SELF_REVIEW_DECISION: ACCEPTED_WITH_DOCUMENTED_LIMITATIONS
REVIEW_AUTHORITY: SELF_REVIEW
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE
