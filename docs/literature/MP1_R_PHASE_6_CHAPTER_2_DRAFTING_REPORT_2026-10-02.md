# MP1-R — Phase 6: Báo cáo soạn thảo Chương 2 có kiểm soát bằng chứng

## Trạng thái phát hành

`READY_FOR_PHASE_7_CLAIM_CITATION_AUDIT`

Bản Chương 2 bằng tiếng Việt đã được tạo thành DOCX Office Open XML thực, có thể chỉnh sửa. Đây là bản thảo để Phase 7 kiểm toán claim–citation; kiểm toán độc lập chưa được thực hiện.

## 1. Đầu vào, quyền hạn và điểm tiếp tục

Đã đọc bốn đầu vào theo thứ tự quy định của lượt Phase 6 ban đầu; phiên tiếp tục sử dụng checkpoint và kiểm tra lại các ranh giới cần thiết:

1. `outputs/plans/MP1_R_PHASE_5_PHASE_6_HANDOFF_2026-10-02.json` — quyền hạn duy nhất của Phase 5 cho Phase 6;
2. `docs/literature/MP1_R_PHASE_5_RESEARCH_GAP_AND_CONTRIBUTION_ADJUDICATION_2026-10-02.md`;
3. `docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md`;
4. `docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md`.

Hash của bốn đầu vào được lưu tại `outputs/reports/MP1_R_PHASE_6_2026-10-02/input_manifest.json`; kiểm tra cuối xác nhận các tệp này không bị sửa. Không dùng bản Working Draft Chương 1–2, A_GEMINI/B_GPT hoặc D1/M1 làm mẫu lời văn. Bản nháp trước khi tạm dừng được bảo tồn riêng trong thư mục `checkpoint_backup` của lượt này.

## 2. Skill và cách áp dụng

Đã áp dụng `$academic-paper` phiên bản 3.3.1, từ `/home/khanh/.codex/skills/academic-paper/SKILL.md`, cho kiến trúc chương, lập bản đồ bằng chứng, lập luận claim–evidence, tổng hợp so sánh, tích hợp trích dẫn và tự kiểm tra chất lượng lời văn.

MODE full được giới hạn bởi chỉ dẫn entry giữa pipeline của người dùng: không chạy lại discovery, gap adjudication, peer review hay Phase 7. Bộ soạn DOCX dùng `python-docx`/OOXML trực tiếp vì Pandoc không có trong môi trường; tài liệu dùng cấu trúc Word thực cho đoạn, heading, bảng, field số trang và phương trình OMML. Script `check_acronyms.py` không có trong bộ skill đã cài; kiểm tra thuật ngữ và chữ viết tắt được thực hiện trong nội dung, thay vì báo một lượt kiểm tra script không tồn tại.

## 3. Corpus và mở lại nguồn

Chương sử dụng 17 Source ID đã được phê duyệt, tương ứng 18 công bố/tài liệu tham khảo vì S05 gồm hai bài riêng. Tìm kiếm văn liệu rộng: **0**. Nguồn mới thêm: **0**. Truy vấn văn liệu bên ngoài: **0**.

Có **14** nguồn được mở đối chiếu qua văn bản gốc đã lưu trong kho, chủ yếu trang đầu và header trang, để kiểm tra thông tin thư mục. Log chi tiết: `outputs/plans/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_2026-10-02.json`. Đó là S01, S02, S03, S04, S05a, S06, S07, S09, S10, S11, S12, S13, S17 và V-W02. S05b, S15, S18 và S22 sử dụng thông tin đã được thẩm định trong kho; không mở lại toàn văn các nguồn này.

Thông tin thư mục đã được sửa ở bản tạm, gồm các tên viết tắt tác giả không đúng, tạp chí của S17, tập/mã bài của một số công bố và trang đã được xác minh. S18 giữ đúng danh tính và vai trò tương tự dầm lớp PVC dưới hút chân không. V-W02 được trích dẫn theo bản online năm 2021 đã xác minh trên trang nhà xuất bản trong bản lưu, thay vì đoán năm/số tập của bản in. Những sửa chữa này không đổi trạng thái giả thuyết hoặc phạm vi đóng góp được phê duyệt.

| Số IEEE | Source ID / công bố | Giới hạn sử dụng |
|---|---|---|
| 1 | S01 | Retain Phase 3 source-specific restrictions |
| 2 | S02 | Retain Phase 3 source-specific restrictions |
| 3 | S03 | Retain Phase 3 source-specific restrictions |
| 4 | S15 | secondary laminar review context; excludes fiber/particle coverage |
| 5 | S18 | vacuum PVC layer-jamming mechanistic analogue only |
| 6 | S06 | Retain Phase 3 source-specific restrictions |
| 7 | V-W02 | published numerical cable paper; 2021 online version cited |
| 8 | S13 | Retain Phase 3 source-specific restrictions |
| 9 | S17 | metric-definition/context only |
| 10 | S04 | Retain Phase 3 source-specific restrictions |
| 11 | S22 | Retain Phase 3 source-specific restrictions |
| 12 | S05 (S05a) | Retain Phase 3 source-specific restrictions |
| 13 | S05 (S05b) | Retain Phase 3 source-specific restrictions |
| 14 | S09 | Retain Phase 3 source-specific restrictions |
| 15 | S07 | transformation-aware FE; frictionless/simplified contact |
| 16 | S11 | Retain Phase 3 source-specific restrictions |
| 17 | S12 | steel experiments; SMA numerical only |
| 18 | S10 | Retain Phase 3 source-specific restrictions |

## 4. Bản đồ bằng chứng và kiến trúc chương

Bản đồ từng mục được lưu trước khi dựng bản sửa tại `outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_evidence_map.json`. Mỗi mục có mục đích, claims, nguồn, sức mạnh theo RP, so sánh, tương phản, giới hạn, liên hệ MP1-R và điều không được tuyên bố. Lời văn và bảng đã được lưu thêm trong inventory có thể tái dựng; Markdown phụ trợ phục vụ kiểm tra, còn DOCX là sản phẩm chính.

- 2.1. Giới thiệu chương
- 2.2. Cơ chế thay đổi độ cứng dựa trên giam giữ và áp suất
- 2.3. Cơ học tiếp xúc, ma sát và dính–trượt trong kết cấu nhiều phần tử
- 2.4. Nhận dạng tương tác dây–dây và dây–ống bao
- 2.5. Đặc tính nhiệt–cơ của TiNi trong kết cấu dây
- 2.6. Phân biệt cơ chế vật liệu và cơ chế tiếp xúc
- 2.7. SMA như nguồn dẫn động tạo áp suất
- 2.8. Tách nguồn kích thích và đáp ứng kết cấu
- 2.9. Các mô hình cơ học hiện có và vai trò của mô hình đối chứng
- 2.10. Tổng hợp bằng chứng và giới hạn suy luận
- 2.11. Những vấn đề chưa được xác định và nhu cầu đặc trưng hóa cho MP1-R
- 2.12. Định hướng nghiên cứu của luận văn

Bốn bảng so sánh lần lượt trình bày kiến trúc giam giữ, định nghĩa metric, trạng thái từng mắt xích và phân loại nhu cầu còn lại. Một phương trình Coulomb được soạn bằng OMML có thể chỉnh sửa; mọi ký hiệu được giải thích. Không sử dụng hình ngoài hoặc hình sao chép. Các bảng là bảng Word, có header lặp lại khi sang trang.

## 5. Quyết định tổng hợp và chất lượng lời văn

- So sánh theo vật liệu, đường áp suất/phản lực, tiếp diện, điều kiện biên, phép đo và giả thiết mô hình; không gộp hệ hạt, sợi nylon, cáp thép và lớp PVC thành phép lặp lại trên TiNi.
- Phân biệt tồn tại ma sát, lực pháp tuyến đã biết, tiếp diện chi phối và phân rã vòng trễ; không dùng uốn toàn cục để chứng minh cả bốn.
- Giữ riêng độ dốc F–δ, độ cứng tiếp tuyến/cát tuyến M–κ, tổn hao DMA và công vòng trễ; nêu điều kiện của công trên đơn vị chiều dài khi dùng M–κ.
- Tách phép thử TiNi thực nghiệm với mô phỏng SMA, cáp chịu kéo với bó chịu uốn và SMA dẫn động với TiNi chịu lực.
- Đặt hiệu chuẩn, khóa mô hình và kiểm tra trên dữ liệu giữ lại trước mọi giả thuyết về luật bổ sung; sai lệch của một giản lược không bác bỏ toàn bộ cơ học thông thường.
- Dùng tiếng Việt học thuật; giải thích SMA, siêu đàn hồi, dính–trượt, DIC, DMA và nhận dạng hệ thống; dùng nhất quán “lực cản”, “ống bao” và “tiếp diện”.
- Mỗi đoạn có chức năng lập luận hoặc tổng hợp; giới hạn chuyển giao bằng chứng được gắn với hệ được khảo sát. Loại các nhãn RP/GAP/Phase và trạng thái tiếng Anh khỏi lời văn luận văn.

## 6. Ranh giới khoa học được bảo toàn

| Nội dung | Trạng thái |
|---|---|
| Khoảng trống tri thức khoa học được tuyên bố | 0 |
| Nhu cầu đặc trưng hóa thực nghiệm | 2 |
| Yêu cầu nhận dạng hệ thống | 5 |
| Xác nhận kỹ thuật / tích hợp | 1 / 1 |
| H0a-R | PLAUSIBLE |
| H0b-R | PLAUSIBLE |
| H1-R | NOT_YET_DISTINGUISHABLE |
| H1 cần cho thành công luận văn | NO |
| Luật cấu thành mới được tuyên bố | NO |

Đóng góp chính vẫn là đặc trưng hóa định lượng ứng xử uốn phụ thuộc áp suất của bó TiNi đã định với mô hình đối chứng thông thường được khóa. PRQ01, SRQ01 và SRQ02 được chuyển thành lời văn tiếng Việt ở mục 2.12, không thêm câu hỏi chính. Xác nhận nguồn và tích hợp là nhiệm vụ hỗ trợ; hạng tử tương tác bổ sung chỉ là mở rộng có điều kiện.

Mắt xích yếu nhất giữ nguyên: **radial reaction → local wire–wire / wire–sleeve contact normal forces**. Bảng 2.3 diễn đạt tự nhiên mức phụ thuộc mô hình, suy luận, chưa thiết lập và được hỗ trợ một phần; không nâng các mức đó thành xác nhận toàn chuỗi trên MP1-R.

## 7. Trích dẫn và truy xuất

Có **121** lần xuất hiện trích dẫn trong thân chương, bảng và ghi chú; một [n] hoặc một dải [n]–[m] tính là một lần, còn [n], [m] tính hai. Có 126 token số ngoặc vuông nếu đếm riêng hai đầu dải. Danh mục gồm **18** mục, đánh số theo lần xuất hiện đầu tiên; đã kiểm tra theo thứ tự OOXML thật, bao gồm các ô bảng. Không có tài liệu mồ côi, số trích dẫn mồ côi, DOI trùng hoặc trích dẫn tác giả–năm.

Register `outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json` chứa **84** đơn vị claim ở mức đoạn, hàng bảng, ghi chú và phương trình. Mỗi đơn vị ghi nguồn/công bố, số IEEE, trạng thái bằng chứng, loại trực tiếp/tổng hợp/tương tự/suy luận, RP, GAP/CONTRIB và ranh giới lời văn. Claims về phạm vi dự án dẫn về handoff Phase 5; định nghĩa phương trình và bảng metric có ghi nguồn kế thừa từ đoạn dẫn hoặc ghi chú. Trạng thái `DRAFT_TIME_CHECKED_PHASE7_PENDING` không phải chứng nhận đã hoàn thành Phase 7.

## 8. Thông tin thư mục còn giới hạn

- **S05a/S05b:** giữ tên tác giả, tiêu đề, tạp chí, năm và DOI đã xác minh; số tập/trang bản in chưa được thiết lập trong phiên bản kho đã dùng nên được bỏ trống.
- **S11:** giữ mã bài 04016023 và DOI đã xác minh; không suy đoán tập/số.
- **V-W02:** dùng bản online ngày 03-08-2021 đã xác minh; không suy đoán năm/trang của bản in từ tên tệp hoặc DOI.

Các giới hạn này được ghi trước phát hành. Không có xung đột bằng chứng nội bộ ngăn cản lập luận bảo thủ; Phase 7 cần kiểm tra độ đầy đủ của các trường thư mục và sự phù hợp claim–citation.

## 9. Kiểm tra Word và hiển thị

DOCX đã được mở lại bằng `python-docx`, kiểm tra XML trong gói OOXML, rồi mở và kết xuất bằng LibreOffice 24.2.7.2 với font Times New Roman thực. Microsoft Word không có trong môi trường; không tuyên bố đã chạy ứng dụng đó. Đã xem bản xem trước toàn trang và các trang công thức/kết luận sau sửa. Bản riêng có **19 trang**, số trang tự động từ 1 ở đầu trang, giữa.

| Kiểm tra | Kết quả |
|---|---|
| valid_ooxml_package | PASS |
| docx_opens_python_docx | PASS |
| A4 | PASS |
| margins | PASS |
| body_font_Times_New_Roman | PASS |
| body_font_13pt | PASS |
| body_line_spacing_1_5 | PASS |
| body_justified | PASS |
| first_line_indent_1cm | PASS |
| Vietnamese_language | PASS |
| page_number_top_center | PASS |
| page_number_start_1 | PASS |
| heading_hierarchy | PASS |
| chapter_heading | PASS |
| editable_tables | PASS |
| editable_equation | PASS |
| no_rasterized_content | PASS |
| references_heading | PASS |
| IEEE_first_appearance_order | PASS |
| reference_number_match | PASS |
| no_orphan_references_or_citations | PASS |
| no_author_year_citations | PASS |
| no_internal_registry_ids | PASS |
| no_excluded_source_citations | PASS |
| no_unconditional_novelty_language | PASS |
| no_literature_discovery | PASS |
| source_IDs_resolve | PASS |
| claim_register_complete | PASS |
| claim_reference_mapping | PASS |
| no_duplicate_bibliographic_DOI | PASS |
| S18_correct_identity | PASS |
| source_reopen_log_count | PASS |
| Phase3_to_5_inputs_immutable | PASS |
| S15_restriction_recorded | PASS |
| S17_restriction_recorded | PASS |
| S18_restriction_recorded | PASS |
| office_renderer_opened | PASS |
| Kiểm tra trực quan | PASS |

Thông số áp dụng: A4; thân Times New Roman 13 pt; dãn dòng 1,5; căn đều; thụt đầu dòng 1 cm; lề trên/dưới/trái/phải 3/3/3,5/2 cm. Sai khác dưới 0,003 cm do làm tròn twip được chấp nhận. Heading chương 16 pt đậm, chữ hoa, căn giữa; heading mục 13 pt đậm, màu đen. Font bảng/ghi chú 11–12 pt để bảo đảm đọc được; bảng vẫn chỉnh sửa được. Phương trình có delimiter và chỉ số OMML thực, đã kiểm tra hiển thị.

Kết quả kiểm tra chi tiết: `outputs/reports/MP1_R_PHASE_6_2026-10-02/formatting_and_content_validation.json`. Bộ dựng và script kiểm tra được lưu cùng thư mục để phục vụ tái lập.

## 10. Sản phẩm và handoff

- DOCX: `docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx`
- Claim traceability: `outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json`
- Reopen log: `outputs/plans/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_2026-10-02.json`
- Handoff: `outputs/plans/MP1_R_PHASE_6_PHASE_7_HANDOFF_2026-10-02.json`

Không có kết quả thí nghiệm MP1-R được tạo hoặc suy diễn. Phase 6 kết thúc tại việc soạn thảo và tự kiểm tra; bước kế tiếp là kiểm toán claim–citation độc lập theo handoff. Chưa thực hiện Phase 7, peer review, Chương 1 hoặc Chương 3.
