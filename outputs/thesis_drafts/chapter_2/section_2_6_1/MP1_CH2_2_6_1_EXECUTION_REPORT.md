# Báo cáo thực thi §2.6.1

TASK_ID: MP1-CH2-2.6.1-RESEARCH-THESIS-DRAFT  
STATUS: PARTIAL_WITH_FINDINGS  
MODE: INDEPENDENT_SECTION_DRAFT_WITH_SOURCE_VERIFICATION  
WORKSPACE: /home/khanh/projects/mechanical-research-agents  
BRANCH: main  
HEAD: e66bb2f2339006e763cd60687cfc24680b945d97  
Ngày ghi báo cáo: 2026-10-19T13:48:59+07:00  
FINAL_SELF_REVIEW_DECISION: ACCEPTED_WITH_DOCUMENTED_LIMITATIONS  
REVIEW_AUTHORITY: SELF_REVIEW  
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE.

Đã biên soạn và kiểm tra nội dung, truy xuất nguồn và cấu trúc DOCX. Còn thiếu kết xuất trực quan do môi trường không có Word/LibreOffice. Vì vậy trạng thái thực thi giữ PARTIAL_WITH_FINDINGS, dù tự rà soát khoa học và truy xuất cho phép chấp nhận bản thảo có giới hạn. Không gọi đây là nghiệm thu độc lập.

## Pre-flight và nguồn chuẩn

Repository root/branch/HEAD được đọc trực tiếp, không checkout/merge/reset/pull. Working tree ban đầu có hai tệp tracked thay đổi thuộc báo cáo Phase 6 và nhiều đầu vào untracked của người dùng. Nhiệm vụ không sửa các tệp đó. So sánh git status trước/sau ngoài thư mục đích cho kết quả giống nhau; diff tracked không có tệp mới do nhiệm vụ tạo.

Đã đọc bảy tệp dự án theo thứ tự AGENTS.md. Chúng mô tả lịch sử nhiều nhánh nghiên cứu; task hiện tại chỉ soạn §2.6.1 cho MP1 theo WEP và yêu cầu người dùng, không chạy quy trình novelty audit, không sửa trạng thái nghiên cứu.

Writing Evidence Pack sử dụng là `data/MP1_WRITING_EVIDENCE_FINAL/`. Chín đầu vào bắt buộc đã đọc:

- `data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md`
- `data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv`
- `data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv`
- `data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md`
- `data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv`
- `data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv`
- `data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md`
- `data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md`
- `data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md`

Đọc thêm `10_EXECUTION_REPORT.md`, `12_R3_CHANGELOG.md`, registry/các hồ sơ Evidence liên quan khi kiểm tra phiên bản và provenance. Các brief/readiness R3 trong thư mục người dùng trùng nội dung bản trong worktree `mp1-writing-evidence-r1`. P3 và WP-E không nằm trong working tree main này; chúng hiện diện ở worktree nguồn trên và đã được đọc tại chỗ, không chép vào corpus hoặc thay thế baseline.

READINESS_2_6_1: EVIDENCE_READY, theo Writing Brief và readiness R3. Đây là readiness của nội dung tổng hợp có giới hạn, không là xác nhận novelty hoặc tính áp dụng trực tiếp MP1. Bốn nguồn lõi của brief: M09-E04, M11-E03, M14-E01, M18-E06. Sáu nguồn bổ trợ từ chính corpus canonical hoàn thành các nội dung TiNi, trượt giữa dây, SMA→áp suất và phương pháp đo mà hai bullet yêu cầu; không mở rộng corpus.

## Dàn ý gốc, tiêu đề và ánh xạ

PDF canonical: `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf`. Đã mở trực tiếp trang vật lý 14 và quan sát ảnh trang. Đối chiếu DOCX dàn ý `literature review/LR-FORMATED-rewrite-outline-de-xuat.docx` cho cùng hai bullet. PDF `literature review/LR-FORMATED.pdf` là bản chương cũ, không dùng thay dàn ý canonical. Không suy bullet từ tên file.

Số bullet thực tế: **2**. Tên gốc: **2.6.1. Điều đã có cơ sở**. Tên được người dùng yêu cầu và dùng trong Word: **2.6.1. Những kết quả đã được thiết lập trong nghiên cứu trước**. SCOPE-01 ghi nhận thay đổi tên theo ủy quyền trực tiếp; Brief và Crosswalk không bất đồng về hai bullet.

Nguyên văn nội dung hướng dẫn của PDF/WEP:

1. **2.6.1-B01:** “Jamming, positive pressure, frictional locking, TiNi transformation, inter-wire slip và SMA-to-pressure actuation đều có prior art ở các architecture khác nhau.”
2. **2.6.1-B02:** “Một số mô hình homogenized, stick–slip hoặc contact-aware đã được validation trong phạm vi riêng của chúng.”

Ánh xạ khoa học: B01 → các cơ chế đã có bằng chứng trong hệ nguồn → P02–P04/P06–P07/P09–P12 → M09/M11/M14/M17/M22/M26/M31/M34. B02 → phạm vi mô hình và cấp đối chiếu → P05–P08/P13–P14 → M18/M17/M22 và M38 cho phương pháp đo. P15 chỉ tổng hợp phần có thể kế thừa và chuyển một câu sang §2.6.2. Bảng mapping đầy đủ ở Gate 1; từng câu có outline_bullet và địa chỉ Word trong CSV.

## Baseline được nhận diện và bảo toàn

Ba baseline tích hợp được xác định chính xác:

- `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx`
- `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx`
- `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx`

Đọc cả ba Word, bảng thuật ngữ/traceability và báo cáo tích hợp liên quan; không chọn lại draft tiểu mục cũ làm baseline. Baseline 2.4 mang hash sau remediation dàn trang R1. Baseline 2.5 nhận diện đủ 5 tiểu mục, 98 dòng master traceability, 67 thuật ngữ, 21 mappings, 12 DOI, 15 OMML, 5 bảng khoa học và 1 glossary theo kiểm kê thực bên dưới. Các báo cáo gốc 2.3/2.4 có trạng thái PARTIAL_WITH_FINDINGS; không tự nâng các trạng thái ấy dù người dùng chỉ định chúng là accepted inputs. §2.5 giữ trạng thái BASELINE_ACCEPTED_WITH_MINOR_ERRATA theo yêu cầu và hồ sơ. Không sửa hai minor errata đã biết.

21 tệp trong ba thư mục baseline và tổng cộng 237 tệp đầu vào/hỗ trợ có SHA-256 trước/sau. Cả 237 khớp. Các hash dưới đây là kiểm tra byte nội dung; không tuyên bố kiểm tra hoặc phục hồi access-time của filesystem.

| Baseline/input đã nhận diện | SHA-256 trước | SHA-256 sau | Kết quả |
|---|---|---|---|
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md` | `84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed` | `84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv` | `eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99` | `eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md` | `e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e` | `e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx` | `bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec` | `bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md` | `25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034` | `25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv` | `54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0` | `54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv` | `65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be` | `65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md` | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv` | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md` | `09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc` | `09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx` | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md` | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv` | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv` | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md` | `b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d` | `b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv` | `a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5` | `a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md` | `3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2` | `3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx` | `cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc` | `cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md` | `d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5` | `d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv` | `229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1` | `229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1` | Không đổi |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv` | `70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff` | `70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff` | Không đổi |

P3/WP-E/dàn ý đọc trực tiếp ở worktree nguồn, các tệp đã sử dụng:

| Đường dẫn | SHA-256 trước | SHA-256 sau |
|---|---|---|
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf` | `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e` | `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md` | `631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e` | `631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md` | `5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3` | `5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md` | `cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda` | `cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md` | `e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9` | `e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md` | `2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90` | `2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md` | `f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3` | `f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3` |

Không tái kết xuất, chuẩn hóa, di chuyển hoặc sửa các baseline. Kết luận liên quan được dùng để giữ ranh giới giữa mô đun, độ cứng uốn, ma sát, trạng thái TiNi, đường truyền áp suất, hiệu chuẩn và kiểm chứng; không chép dài văn xuôi.

## Mô hình và phân công thực tế

ROOT_MODEL_REQUESTED: GPT-6.1 Sol High.  
ROOT_MODEL_ACTUAL: NOT_EXPOSED. Môi trường chỉ mô tả Codex dựa trên GPT-6; không có telemetry xác nhận biến thể/effort backend, không suy tên requested là actual.  
WORKER_MODELS_REQUESTED: Sol Medium hoặc Luna theo vai trò.  
WORKER_MODELS_ACTUAL: NOT_VERIFIED_BACKEND. Giá trị dispatch trực tiếp được ghi nhận: `gpt-6.1-sol`, `medium` cho ba source workers; `gpt-6-luna`, `medium` cho QA. Công cụ nhận task không cung cấp telemetry backend/model token/runtime.  
UNIQUE_WORKERS_USED: 4. Không dùng 8 worker riêng; tái sử dụng 3 worker có ngữ cảnh và thêm 1 QA worker, không ghi đồng thời một tệp cuối.

| Worker thực sự chạy | Giai đoạn/vai trò | Giá trị gửi công cụ | Đầu ra và phạm vi |
|---|---|---|---|
| sources_jamming | A nguồn M09/M11/M14; E soạn tiếng Việt sau ROOT duyệt | gpt-6.1-sol, medium | Packet nguồn;15 đoạn và 73 claim units đề xuất. ROOT biên tập thành 70 đơn vị thân. |
| sources_models | B nguồn M17/M18/M22; rà synthesis; G dựng Word | gpt-6.1-sol, medium | Packet nguồn; phát hiện giới hạn mô hình; dựng DOCX từ nội dung đã duyệt. Dùng lại Sol Medium cho G thay vì mở worker Luna riêng. |
| sources_sma | C nguồn M26/M31/M34/M38; F thuật ngữ | gpt-6.1-sol, medium | Packet nguồn;14 thuật ngữ; xác nhận secondary-local pagination M26. |
| bounded_qa | H QA tĩnh có giới hạn | gpt-6-luna, medium | Đối chiếu 15 đoạn,70 anchor thân,14 hàng glossary,84 locator,10 references;0 finding tĩnh còn mở. |

ROOT tự đọc PDF và phê duyệt nguồn, vai trò, kết luận, suy luận và chuyển giao; sau đó đọc lại toàn Word và sửa điểm cần thiết. Bản QA đầu dùng bộ phân tích sai 4 cột và bỏ ngắt dòng XML nên báo glossary không khớp; ROOT xác minh bằng python-docx đúng 3 cột và yêu cầu chạy lại. Bản QA cuối khớp 14/14. Không coi kết quả đa số worker là quyết định khoa học. Chỉ ROOT ghi năm deliverable cuối. Nội dung tạm và script kiểm tra được dọn khỏi vùng tạm khi hoàn tất; mọi finding quan trọng/provenance cần lưu đã chuyển vào CSV và hai báo cáo.

## Nguồn, PDF và phạm vi xác minh

10 Paper IDs dùng trong manuscript =9 bài journal và 1 hướng dẫn đo lường JCGM. Không phải yêu cầu trích đủ 39 nguồn. Tổng số PDF có kiểm tra trực tiếp: **11**, gồm 10 PDF làm nguồn nội dung và M28 chỉ hỗ trợ metadata M26. M28 không là reference thứ 11 hoặc một thí nghiệm bổ sung cho lập luận. Không có PDF được chọn nào không mở được. PDF dàn ý được kiểm tra riêng, không cộng vào số 11 PDF khoa học/metadata.

DIRECT_PDF_VERIFIED nghĩa là nội dung/trang được sử dụng đã đối chiếu PDF trong nhiệm vụ này; không nghĩa toàn bộ mọi trang của bài đã được tái kiểm định. SOURCE_NOTE_REPORTED và AGENT_REPORTED_PDF_VERIFIED là hai cấp thấp hơn, không được dùng để giả đã kiểm tra trực tiếp. ROOT đã đọc lại các trang quan trọng và xác nhận nội dung dùng; trường verification_provenance và accepted_evidence_locators giữ chi tiết. Không dựa Internet hoặc metadata-only để khẳng định kết quả cơ học. Không tìm tài liệu mới, không mở rộng corpus.

| Citation | Paper ID | PDF canonical | Evidence IDs dùng | Trang PDF vật lý kiểm tra liên quan | SHA-256 |
|---|---|---|---|---|---|
| 1 | M09 | `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf` | M09-E04 | 9, 10, 11 | `240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5` |
| 2 | M11 | `data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf` | M11-E01, M11-E03 | 2, 4, 5 | `cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827` |
| 3 | M14 | `data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf` | M14-E01, M14-E03, M14-E04, M14-E05 | 1, 5, 6, 7, 8, 9, 10 | `6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807` |
| 4 | M18 | `data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf` | M18-E01, M18-E03, M18-E06, M18-E07 | 1, 2, 3, 6, 7, 8 | `95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd` |
| 5 | M17 | `data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf` | M17-E01, M17-E02, M17-E04, M17-E05 | 2, 3, 4, 5 | `652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee` |
| 6 | M22 | `data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf` | M22-E01, M22-E02, M22-E04, M22-E05 | 1, 2, 3, 4, 5, 6, 7 | `9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe` |
| 7 | M26 | `data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf` | M26-E01, M26-E03, M26-E07 | 1, 4, 8, 15, 16, 17 | `00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9` |
| 8 | M31 | `data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf` | M31-E01, M31-E07 | 2, 3, 6 | `65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03` |
| 9 | M34 | `data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf` | M34-E02, M34-E09 | 1, 3, 12 | `55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782` |
| 10 | M38 | `data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf` | M38-E02, M38-E03, M38-E04 | 20, 21, 31, 33, 35, 36 | `41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c` |

CSV giữ riêng phần nguồn hỗ trợ, phần suy luận tác giả, điều kiện, giới hạn, locator gốc và locator kiểm tra lại; các JSON là dữ liệu có thể parse. Danh tính 10 nguồn được đối chiếu bằng nội dung PDF, không chỉ cú pháp DOI. Không có nhãn INDEPENDENTLY_VALIDATED được gán cho mẫu MP1 hoặc các so sánh mà nguồn không đủ bằng chứng tách dữ liệu.

Các hiệu chỉnh/loại bỏ quan trọng:

- M09: áp dương tạo uốn và chân không tạo kẹt là hai ngõ khác nhau; bỏ số 145/87 kPa vì không cần cho lập luận, không đảo dấu áp.
- M11: Fig.6 c/e là kéo vật khỏi kẹp; Fig.6 d là lực–chuyển vị ngón. Giữ 5 lần/mức,80 N tại 241,3 kPa; không dùng so mGrip 2,4 lần hoặc cặp khối lượng/lực bất nhất trong nguồn.
- M14: E 03 giả thiết đồng nhất/Hooke/chuyển vị nhỏ/uốn thuần ở PDF 5/in 130257. E 04 ghi nhầm transverse cho một bộ số axial; nhiệm vụ không dùng bộ số đó. Discussion PDF 9–10 nói chưa tính được độ cứng hiệu dụng định lượng do D khó xác định; không nâng thành validation định lượng.
- M18: Fig.7 ở PDF 8/in 828;20 tấmPVC và 60 kPa. Dải±1 σkhông là 95%CI; không có dữ liệu để xác nhận held-out validation. Thí nghiệm này tách khỏi cấu hình FEA trong cùng bài; không trộn thông số của hai bộ.
- M22: DOI đầy đủ `10.1061/(ASCE)ST.1943-541X.0002171` đọc từ PDF 1, thay phần registry bị cụt trong bản ghi mới. k hiệu chuẩn trên dữ liệuChen, không áp suất piston. Giữ original metadata/record trong CSV.
- M26: proof không có phân trang cuối; tập 50/tr.3009–3026 được xác nhận trong M28 PDF 19, bibliography mục 14. Issue không được suy ra. Các kết luận kéo gần đẳng nhiệt và lịch sử chu trình không thành định luật uốn hoặc tốc độ/nhiệt phổ quát.
- M31: ma sát dây–cao su và độ cứng từ lực–chuyển vị, không nhận dạng lực pháp tuyến cục bộ dây–dây.
- M34: lò xoNiTi và vỏsilicone tạo áp suất đầu ra; không piston MP1. Không chuyển cột áp tĩnh thành ứng suất tiếp xúc.
- M38: locator trang in đã từng bị coi như trang vật lý; sửa trong CSV nhiệm vụ, giữ bản gốc. Mô hình phép đo là Eq.(1), khôngEq.(4). M38 được phân loại phương pháp, không thực nghiệm.
- Không sử dụng M13 Eq.(4),M19,M23 Eq.(15)hoặc nhóm phương trình M33; không âm thầm sửa phương trình nguồn nào.

## Số liệu thực tế của năm tệp

| Trường | Giá trị | Cấp xác nhận |
|---|---|---|
| Bullet dàn ý |2|DIRECTLY_VERIFIED|
| Đoạn thân khoa học |15|DIRECTLY_VERIFIED|
| Từ thân theo tách khoảng trắng |2236|DIRECTLY_VERIFIED, không phải đếm hình thái tiếng Việt|
| Paper IDs trong manuscript |10|DIRECTLY_VERIFIED|
| PDF kiểm tra trực tiếp |11=10 nội dung+1 metadata|DIRECTLY_VERIFIED|
| PDF được chọn nhưng không kiểm tra được |0|DIRECTLY_VERIFIED|
| Evidence IDs duy nhất |29|DIRECTLY_VERIFIED|
| Claim records |84=70 thân+14 glossary|DIRECTLY_VERIFIED|
| SOURCE_GROUNDED_CLAIM |33|DIRECTLY_VERIFIED|
| INFERENCE |50|DIRECTLY_VERIFIED|
| DOCUMENT_COVERAGE |1|DIRECTLY_VERIFIED, không là kết quả khoa học|
| AUTHOR_PROPOSAL/AUTHOR_DERIVATION/PENDING_HUMAN_DECISION/P3_INTERNAL_DEFINITION |0/0/0/0|DIRECTLY_VERIFIED|
| Thuật ngữ CSV / Word |14/14|DIRECTLY_VERIFIED theo từng danh tính/nghĩa/ngữ cảnh/nguồn|
| References |10|DIRECTLY_VERIFIED|
| DOI duy nhất |9|DIRECTLY_VERIFIED,M38 không cóDOI|
| Citation occurrences đã mở dải |51=27 thân+24 glossary|DIRECTLY_VERIFIED, không đếm nhãn bibliography|
| Token citation ngoặc số nguyên dạng |44|DIRECTLY_VERIFIED|
| Bảng khoa học / glossary / tổng bảng |0/1/1|DIRECTLY_VERIFIED|
| Hình / phương trình OMML |0/0|DIRECTLY_VERIFIED|
| Trang sau render |NOT_AVAILABLE|Không kết xuất, không ước lượng|
| DOCX ZIP/XML |VALID|DIRECTLY_VERIFIED|
| Word visual render |NOT_VERIFIED|Không có bộ render|
| Microsoft Word / LibreOffice đã chạy |Không/Không|DIRECTLY_VERIFIED cho môi trường nhiệm vụ|
| Đầu vào/hỗ trợ checksum không đổi |237/237|DIRECTLY_VERIFIED|
| Tệp baseline tích hợp hash không đổi |21/21, gồm 3 DOCX|DIRECTLY_VERIFIED|

Phân bố evidence_class đa nhãn theo 84 dòng, không là số thí nghiệm độc lập:

- NOT_APPLICABLE: 1
- EXPERIMENTALLY_DEMONSTRATED: 58
- COMPARATOR_ONLY: 47
- MODEL_DERIVED: 55
- CALIBRATION_SUPPORTED: 6
- NUMERICALLY_DEMONSTRATED: 3
- INDEPENDENTLY_VALIDATED:0; REVIEW_SYNTHESIS:0. Không có bài review dùng thay primary evidence. M38 là hướng dẫn phương pháp với MODEL_DERIVED cho quan hệ toán học/đánh giá bất định, source_role=METHODOLOGY.

Các nhãn không xếp hạng độ tin cậy. Một dòng suy luận có thể viện dẫn nhiều loại bằng chứng; class mô tả thành phần nguồn, không chứng minh toàn suy luận đã được đo. Bản ghi gốc được giữ trong accepted_evidence_lookup; các giới hạn/corrections được lưu riêng, không ghi đè Evidence Records.

## Bảy Gate và findings còn mở

GATE_1: PASS_WITH_DOCUMENTED_LIMITATIONS  
GATE_2: PASS  
GATE_3: PASS_WITH_DOCUMENTED_LIMITATIONS  
GATE_4: PASS  
GATE_5: PASS_WITH_DOCUMENTED_LIMITATIONS  
GATE_6: PASS_WITH_DOCUMENTED_LIMITATIONS  
GATE_7: PARTIAL_WITH_FINDINGS  

1. **RENDER-01, chưa xác minh trình bày:** Không có bộ render. Chưa xem từng trang; chưa biết tổng trang; chưa xác minh cắt chữ/tràn bảng/trang trắng. Native table flags và ZIP/XML không thay thế visual PASS. Cần kiểm định bằng Word/renderer trước nghiệm thu trình bày.
2. **META-01, giới hạn metadata:** Các trường issue không có trong nguồn đã kiểm tra được bỏ, không đoán. Pagination M26 dựa bibliography nội bộ của M28, không giả PDF proof có metadata xuất bản cuối.
3. **SCOPE-01, tên mục:** Tên mở rộng do người dùng yêu cầu; hai bullet vẫn giữ tên và nội dung gốc trong mapping.
4. **Giới hạn chuyển giao hợp lệ:** Không nguồn nào trực tiếp kiểm chứng cấu hình MP1. Các giá trị, quan hệ và cận của hệ khác không được coi đã áp dụng MP1. Không có lỗi khoa học trọng yếu chưa xử lý được phát hiện trong phạm vi tự rà soát; kết luận này không thay nghiệm thu độc lập.

Không cần thêm nguồn Internet để hoàn thành nhiệm vụ trong ranh giới hiện tại. Nếu người kiểm định yêu cầu xác nhận issue hoặc metadata xuất bản cuối trực tiếp từ nhà xuất bản, cần một nhiệm vụ bổ sung có phạm vi được phê duyệt; nhiệm vụ này không tự thay corpus.

## Quyết định vẫn thuộc con người

Không chốt năm nhóm: hình học/giao diện; lực pháp tuyến cục bộ/proxy; miền nhiệt độ/pha/lịch sử tải TiNi; đại lượng độ cứng chính và bất định; phạm vi kiểm chứng SMA–piston. Các quyết định này không bị dùng làm kết quả của §2.6.1. Không đóng băng Bench A/B. Đã đọc P3: H0b=NOT_FALSIFIED_LIVE_COMPETITOR; H1=INSUFFICIENT_EVIDENCE; G00 đóng; G01–G08 chỉ là câu hỏi có điều kiện. Không sửa trạng thái nào và không đưa các mã ấy vào Word.

## Giao nộp và regression

Đúng năm final deliverables:

- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md`
- `/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md`

Đã mở lại DOCX sau dựng, toàn bộ CSV và hai báo cáo; kiểm tra tệp không rỗng, các phần bắt buộc, anchor luận điểm, glossary, DOI/citation và cấu trúc bảng. Không tạo R2/R3 hoặc tệp final thứ sáu. Không có báo cáo khoa học quan trọng chỉ nằm trong chat hay vùng tạm.

BASELINES_UNCHANGED:YES, 21/21 baseline và 237/237 đầu vào/hỗ trợ khớp SHA-256 trước/sau. Không sửa hai minor errata 2.5. Không sửa dữ liệu/trạng thái nghiên cứu, registry hoặc lịch sử verification. Không viết §2.6.2 trở đi, không tích hợp toàn §2.6, không sửa Chương 2 đã có. Không checkout/merge/reset/pull, không commit, push hoặc tạo PR.

FILES_CREATED:5. Các kiểm tra liên quan đã được chạy lại sau chỉnh anchor glossary, giãn dòng 1.15 và ghi rõ 60 kPa của M18 là độ lớn áp suất chân không theo PDF3. ROOT kiểm tra lại đầy đủ anchor sau sửa này. Nội dung khoa học, glossary và citations giữ khớp. Tất cả kết quả ở đây là SELF_REVIEW.

NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE.


## Manifest bảo toàn đầy đủ của 237 đầu vào/hỗ trợ

Bảng rút gọn này bổ sung các bảng baseline ở trên. Cột SHA-256 áp dụng cho cả trước và sau vì từng cặp đã được so bằng nhau; không dùng một hash mới sau tác vụ để giả làm hash trước. Danh sách được lấy từ snapshot trước soạn thảo.

| Tệp | SHA-256 trước = sau |
|---|---|
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md` | `84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed` |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv` | `eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99` |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md` | `e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e` |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx` | `bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec` |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md` | `25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034` |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv` | `54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0` |
| `outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv` | `65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md` | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv` | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md` | `09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx` | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md` | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv` | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` |
| `outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv` | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md` | `b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv` | `a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md` | `3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx` | `cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md` | `d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv` | `229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1` |
| `outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv` | `70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff` |
| `data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv` | `75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008` |
| `data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv` | `5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c` |
| `data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md` | `6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c` |
| `data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md` | `2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8` |
| `data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md` | `adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f` |
| `data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv` | `f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0` |
| `data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv` | `1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c` |
| `data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md` | `999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c` |
| `data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md` | `0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519` |
| `data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md` | `65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd` |
| `data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md` | `8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3` |
| `data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md` | `bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd` |
| `data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier` | `b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe` |
| `data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf` | `5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0` |
| `data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf` | `d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b` |
| `data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf` | `51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2` |
| `data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf` | `52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12` |
| `data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf` | `90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7` |
| `data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf` | `f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b` |
| `data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf` | `5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5` |
| `data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt` | `f75d24bd867f9b5f9ac749f607f43f6c657f57d95517f3a7258127dac8f82db7` |
| `data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf` | `7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933` |
| `data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt` | `32cbdee2a368ec60d02d949c36791624d4de4106778945b9ac95cd190af41db1` |
| `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf` | `240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5` |
| `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt` | `1dfbf70b8365b16c562a680abb50a7fee23727fb80038425397f7b67a14df8db` |
| `data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf` | `182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58` |
| `data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt` | `413bafe43781995cd50eb6463126f7dbe0c52c8951ed0a7cab8a1009ec9245ac` |
| `data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf` | `cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827` |
| `data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt` | `5b3cbae0cb08f21b907c572a04df5a36312b08cc4c9e9701440ddbceb3421d8f` |
| `data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf` | `bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf` |
| `data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf` | `3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f` |
| `data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt` | `ab0ded96e50c6d61565b8529fe0b2b58d95e720344599f9494d5bbf1df60ad6d` |
| `data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf` | `6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807` |
| `data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt` | `1fbd2bb1fe12bf775f2c82229ab5f3a692d255fc86dc4dc60f32aea4c2676837` |
| `data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf` | `b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63` |
| `data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf` | `1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a` |
| `data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf` | `652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee` |
| `data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt` | `89fede501f2cd30bff4b6532d7ba4584556f8434738a67a4416d3caef3c473a7` |
| `data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf` | `95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd` |
| `data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf` | `7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a` |
| `data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf` | `a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a` |
| `data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf` | `ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752` |
| `data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf` | `9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe` |
| `data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf` | `1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a` |
| `data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf` | `9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6` |
| `data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt` | `db8972c2950ff381e7abb7122dfd9ddc7a85cd972426933be2bd816e22fb3de2` |
| `data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf` | `53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a` |
| `data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf` | `00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9` |
| `data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf` | `fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284` |
| `data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf` | `1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65` |
| `data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf` | `56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61` |
| `data/chap1-2_citations/M30__A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf` | `e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f` |
| `data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf` | `65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03` |
| `data/chap1-2_citations/M32__2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf` | `2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b` |
| `data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf` | `de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac` |
| `data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf` | `55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782` |
| `data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf` | `aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800` |
| `data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf` | `40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3` |
| `data/chap1-2_citations/M37__2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf` | `7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08` |
| `data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf` | `41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c` |
| `data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf` | `24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a` |
| `data/chap1-2_citations/MANIFEST.json` | `9d3c70e3a1f267c51fb87a77f504f6eb2e0d99d3dbd2ccc14b557aad9e017eda` |
| `data/chap1-2_citations/README.md` | `a82bd095dbbd8ec46c5576bec7f3870bc86d64f7748a7767d6a7306993eb4f7c` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md` | `bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv` | `942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md` | `12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md` | `5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md` | `c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md` | `0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406` |
| `outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json` | `0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md` | `cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md` | `6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json` | `0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json` | `0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md` | `e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md` | `b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv` | `fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9` |
| `outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md` | `9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv` | `3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md` | `5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv` | `2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md` | `1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md` | `6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md` | `c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md` | `a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037` |
| `outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md` | `227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md` | `607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv` | `7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl` | `a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md` | `17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md` | `49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md` | `d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md` | `24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md` | `59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md` | `86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md` | `2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md` | `da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md` | `7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md` | `76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md` | `f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md` | `7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md` | `67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md` | `99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip` | `fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md` | `9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv` | `b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl` | `9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md` | `c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md` | `ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md` | `9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md` | `24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md` | `7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md` | `c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md` | `fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md` | `d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md` | `6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md` | `37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md` | `6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md` | `58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md` | `2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md` | `77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md` | `4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md` | `561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md` | `b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md` | `0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md` | `99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md` | `34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json` | `19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md` | `5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip` | `fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md` | `78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv` | `237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv` | `7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl` | `a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md` | `485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md` | `8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md` | `3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md` | `1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md` | `0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md` | `287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md` | `0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md` | `f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md` | `fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md` | `5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md` | `31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md` | `2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md` | `0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md` | `98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md` | `3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md` | `fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md` | `65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md` | `4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip` | `ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md` | `880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv` | `b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl` | `ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md` | `4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md` | `fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md` | `ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md` | `2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json` | `eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md` | `a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md` | `a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md` | `d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md` | `613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md` | `4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md` | `4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6` |
| `outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip` | `9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md` | `3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv` | `ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl` | `e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md` | `26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md` | `a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv` | `245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md` | `56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md` | `6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md` | `809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md` | `e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md` | `f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md` | `bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md` | `e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md` | `ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md` | `a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682` |
| `outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md` | `71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md` | `cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_SOURCE_MAP.csv` | `2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_P3_HANDOFF.md` | `bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md` | `5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md` | `631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv` | `235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_MODEL_APPLICABILITY_MATRIX.csv` | `06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv` | `9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md` | `e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md` | `f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md` | `f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md` | `61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md` | `2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md` | `09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv` | `894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md` | `5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md` | `4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md` | `a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md` | `cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55` |
| `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf` | `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e` |
| `/home/khanh/projects/mechanical-research-agents/literature review/LR-FORMATED-rewrite-outline-de-xuat.docx` | `3053b2649293ac1841de835a15687392beef1648a5de26faf6f78b5b3d78b0e4` |
