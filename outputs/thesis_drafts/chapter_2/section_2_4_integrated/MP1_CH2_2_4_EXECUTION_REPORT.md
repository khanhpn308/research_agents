# Báo cáo thực thi tích hợp mục 2.4

TASK_ID: MP1-CH2-2.4-INTEGRATION-AND-CONSISTENCY-REVIEW  
STATUS: PARTIAL_WITH_FINDINGS  
TARGET_SECTION: 2.4 — TiNi, ma sát bó dây và nguồn tạo áp  
DRAFT_LANGUAGE: VIETNAMESE_ONLY, trừ tên xuất bản và thuật ngữ Anh cần thiết  
ACADEMIC_CONTEXT: HCMUT–VNU-HCM, Khoa Cơ khí, Thạc sĩ Kỹ thuật Cơ khí, định hướng nghiên cứu chuyên sâu  
ROOT_MODEL_REQUESTED: GPT-6.1 SOL HIGH  
ROOT_MODEL_ACTUAL: NOT_EXPOSED; không có chứng thực biến thể mô hình hoặc effort thực chạy  
WORKERS_SPAWNED: 6 (A khoa học, B trích dẫn, C thuật ngữ, D truy xuất, E DOCX, F QA độc lập)  
WORKER_MODELS_ACTUAL: NOT_INDEPENDENTLY_VERIFIED; tham số đã gửi: A/B/C/F gpt-6.1-sol medium; D/E gpt-6-luna medium  
INPUT_FILES_VERIFIED: 20/20  
BASELINE_HASHES_RECORDED: 20/20 trong Integration Changelog  
BASELINE_FILES_MODIFIED: 0; thêm 193 tệp hỗ trợ không đổi hash  
INPUT_ACCEPTANCE_STATES: 2.4.1/2.4.2/2.4.3/2.4.4 đều PARTIAL_WITH_FINDINGS; không nâng trạng thái gốc  
SUBSECTIONS_INTEGRATED: 4/4  
ORIGINAL_TRACEABILITY_RECORDS: 123  
INTEGRATED_TRACEABILITY_RECORDS: 123  
SOURCE_GROUNDED_CLAIMS: 79  
INFERENCE_CLAIMS: 28  
AUTHOR_PROPOSALS: 9  
DOCUMENT_COVERAGE_RECORDS: 7  
TOTAL_TRACEABILITY_RECORDS: 123  
TECHNICAL_CLAIMS_BY_CATEGORY: SOURCE_GROUNDED_CLAIM=78; INFERENCE=27; AUTHOR_PROPOSAL=9; DOCUMENT_COVERAGE=0; loại metadata 1 và ghi chú glossary 1 khỏi số kỹ thuật, giữ nhãn gốc  
ORIGINAL_REFERENCE_MAPPINGS: 14  
UNIQUE_REFERENCES: 13  
DUPLICATE_REFERENCES_REMOVED: 1  
CITATION_MAP_CLOSURE: PASS  
GLOSSARY_STALE_CITATIONS: 0  
FIRST_APPEARANCE_CITATIONS: PASS; [1] đến [13] trong thứ tự XML thân và bảng  
ORIGINAL_TERMINOLOGY_ENTRIES: 93  
UNIQUE_TERMINOLOGY_ENTRIES: 88  
TERMINOLOGY_CONFLICTS_RESOLVED: 5 cặp trùng nghĩa gộp; 1 sửa hiệu chuẩn/kiểm chứng ở thân; 2 ô Nguồn biên tập bỏ quy nguồn từ ví dụ; phân biệt cơ học hợp lệ giữ riêng; đơn vị k_i không giải quyết  
SCIENTIFIC_TABLES: 4  
GLOSSARY_TABLES: 1  
EDITABLE_OMML_EQUATIONS: 1  
EQUATION_INTEGRITY: PASS; cấu trúc OMML/chữ Q_out ≥ Q_in và tính chỉnh sửa được giữ; R1 thêm m:nor cho hai nhãn chỉ số để tương thích LibreOffice, nên XML đích không còn byte-identical với baseline; không đổi ý nghĩa hoặc nguồn M33  
TABLE_CAPTION_INTEGRITY: PASS_STATIC; 5 caption duy nhất  
SCIENTIFIC_CONTRADICTIONS: 0 mâu thuẫn vật lý mới còn mở trong phần hợp nhất; 1 bất nhất thuật ngữ đã sửa; metadata M25 quyết định theo PDF  
REDUNDANCIES_RESOLVED: 3 phần giải thích lặp; không bỏ hàng hoặc bảng khoa học  
MP1_UNRESOLVED_DECISIONS: topology; trạng thái pha/nhiệt; môi chất; đường truyền áp; tiếp xúc/lực pháp tuyến; ma sát; đại lượng uốn; nhận dạng và kiểm chứng  
GATE_1: PARTIAL_WITH_FINDINGS, bảo lưu giới hạn bao phủ nguồn  
GATE_2: PASS trong phạm vi tích hợp  
GATE_3: PASS có giới hạn kế thừa và phương trình thực sự giữ  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS  
GATE_7: PARTIAL_WITH_FINDINGS, LibreOffice visual PASS; MS Word chưa kiểm tra  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
BASELINE_IMMUTABILITY: PASS  
CITATION_MAPPING_CLOSURE: PASS  
TRACEABILITY_COMPLETENESS: PASS  
GLOSSARY_CITATION_CLOSURE: PASS  
SCIENTIFIC_CONTENT_PRESERVED: PASS, đối với bản thảo và hồ sơ gốc  
WORD_RENDER_VALIDATION: PARTIAL_LIBREOFFICE_VERIFIED_MS_WORD_NOT_VERIFIED  
INDEPENDENT_DOCUMENT_QA: PASS_STATIC_BOUNDED  
INTEGRATED_DOCX_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx  
TRACEABILITY_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv  
TERMINOLOGY_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv  
CITATION_MAP_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv  
CHANGELOG_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md  
QA_REPORT_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md  
EXECUTION_REPORT_PATH: outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md  
UNRESOLVED_LIMITATIONS: k_i M23; nhiệt/rate; nguồn chuyên biệt; metadata issue M25; giả định M33/M34; không có renderer; không nhận dạng MP1 từ đại lượng tổng thể  
NEXT_ACTION: Rà từng trang trong Word hoặc renderer tương thích; không viết 2.5 hoặc tiếp tục nghiên cứu ngoài phạm vi  

## Kiểm kê và chấp nhận baseline

Đã mở đủ 20 đầu vào và đọc bốn báo cáo bảy cổng cùng bốn báo cáo thực thi trước chỉnh sửa. Bảng đường dẫn/hash 20 tệp được lưu đầy đủ trong [nhật ký tích hợp](MP1_CH2_2_4_INTEGRATION_CHANGELOG.md). Không bỏ nguồn hoặc sửa tệp chung. 193 tệp hỗ trợ trong WEP, PDF chuẩn, reading pack và baseline 2.3 cũng được kiểm tra hash không đổi.

| Tiểu mục | Chấp nhận ghi trong hồ sơ gốc | Giới hạn được giữ |
|---|---|---|
| 2.4.1 | PARTIAL_WITH_FINDINGS; cổng 1 và 7 PARTIAL; bản R2 | Cơ sở soạn thảo được chấp nhận có giới hạn nhiệt độ/tốc độ; kéo gần đẳng nhiệt không xác lập luật nhiệt/tốc độ hay trạng thái MP1. Render độc lập chưa xác minh. |
| 2.4.2 | PARTIAL_WITH_FINDINGS; cổng 1 và 7 PARTIAL | Bện/bao được phân biệt theo hình học, không có kiểm chứng chuyên biệt; M22/M23 cùng tuyến Chen; đơn vị k_i M23 chưa xác minh; cáp thép/cáp xoắn không là MP1. |
| 2.4.3 | PARTIAL_WITH_FINDINGS; cổng 1–6 PASS có giới hạn, cổng 7 PARTIAL | Hồ sơ ghi nhận rà soát DOCX độc lập; giao diện dây–cao su, lực kéo không tách tải pháp tuyến/hệ số ma sát; không suy pha R của MP1. |
| 2.4.4 | PARTIAL_WITH_FINDINGS; cổng 1–6 PASS trong phạm vi nêu, cổng 7 PARTIAL | Theo đúng hồ sơ thực tế, chấp nhận nội dung tổng quan có giới hạn; không giả định người dùng đã rà Word độc lập. (1)–(4) nguồn đã được hồ sơ kiểm tra có giới hạn, chỉ (1) trong DOCX. Nhóm phương trình nhiệt khác không được nâng trạng thái. |

## Điều phối và mô hình thực tế

| Worker | Vai trò có giới hạn | Tham số mô hình/effort gửi công cụ | Điều kiện chạy |
|---|---|---|---|
| science | Nhất quán, chồng lặp, đề xuất năm sửa; ROOT duyệt sáu sửa tổng cộng | gpt-6.1-sol, medium | A/B/C song song trong ba slot worker. |
| citations | Định danh, toàn bộ token, metadata và M33(1) | gpt-6.1-sol, medium | Cùng pha phân tích; đầu ra chỉ tạm. |
| terminology | 93 bản ghi, 88 nghĩa và quy nguồn riêng | gpt-6.1-sol, medium | Cùng pha phân tích; ROOT chuẩn hóa và duyệt. |
| traceability | Kiểm kê/phân loại 123 hồ sơ | gpt-6-luna, medium | Sau khi một slot trống; ROOT sửa ánh xạ theo nội dung thay vì citation chung. |
| docx_build | Dựng Word bằng deepcopy XML, áp sửa đã duyệt | gpt-6-luna, medium | Sau ROOT duyệt khoa học, citation và thuật ngữ; chỉ worker này ghi DOCX. |
| integration_qa | Kiểm tra độc lập sau dựng, chỉ đọc | gpt-6.1-sol, medium | Sau DOCX và các sổ tích hợp; ROOT giữ quyết định cuối. |

Không có telemetry xác nhận mô hình backend hay thời gian/token, nên không tạo runtime statistics. ROOT được môi trường mô tả chung là Codex dựa trên GPT-6; không suy đó là chứng thực GPT-6.1 Sol High. Các mô hình trong bảng là giá trị truyền lúc gọi công cụ. Giới hạn đồng thời thực tế bốn agent gồm ROOT được tuân thủ. Không có worker sửa chung một tệp cuối.

## Kết quả khoa học và bảo toàn

Chuỗi lập luận nối TiNi với kiến trúc/contact, SMA điều biến tiếp xúc và truyền áp suất. Sáu sửa được duyệt không thêm kết quả: ba rút lặp, hiệu chuẩn→kiểm chứng, áp suất buồng phía piston và nhắc lại topology/lay đã có hồ sơ. Không viết lại toàn bộ, không thêm mô hình MP1, H1, tham số, thiết kế thí nghiệm hay tuyên bố tính mới. Mọi giả định và giới hạn quan trọng còn trong thân/CSV/báo cáo.

123 hồ sơ gốc còn nguyên, gồm 79 theo nguồn, 28 suy luận, 9 đề xuất, 7 bao phủ. Đây không phải 123 phát hiện độc lập. Có 107 ánh xạ nội dung, 2 ánh xạ cốt lõi kèm chi tiết ở hồ sơ, 5 hồ sơ vốn chỉ hỗ trợ kiểm toán, 7 phạm vi, 1 metadata, 1 glossary. Metadata 244-C14 và giải thích glossary 244-C35 không tính trong 114 hồ sơ kỹ thuật (78/27/9). Địa chỉ Word được ghi theo phần tử từ 0; không bịa số trang. Toàn trường gốc giữ trong original_record_json, thêm lookup canonical Evidence ID khi trường provenance gốc thiếu.

14 ánh xạ citation còn đủ, 13 DOI duy nhất; M25 gộp một lần lặp. Tất cả nguồn dùng trong thân, bảng và bibliography. Thứ tự lần đầu [1]–[13] đúng kể cả bảng. Mọi ô glossary, kể cả định nghĩa/ngữ cảnh, dùng số mới. 93 thuật ngữ gốc được bảo toàn qua 88 mục với năm cặp gộp; không gộp các đại lượng khác nghĩa cơ học.

Giữ bốn bảng khoa học (5×6, 5×6, 4×6, 4×6), một glossary 89×5 gồm tiêu đề, năm caption duy nhất, 107 hàng không tách và đầu bảng lặp. Không có hình nguồn sao chép. Một phương trình OMML Q_out ≥ Q_in được giữ nguyên XML và dấu/chỉ số, nguồn M33(1), nay [12], trang in 538. Hai Q có đơn vị lưu lượng, không thành luật áp suất; các phương trình khác không được tự đưa lại. Metadata dùng M25 online 2021 và M33 issue 2013/online 2012.

## Kiểm tra tĩnh, kiểm tra độc lập và kết xuất

ROOT validator riêng đối chiếu 82 phần tử và 186 đoạn/ô với baseline hoặc sáu đoạn đã duyệt; so cả danh tính nguồn và locator theo từng occurrence. ZIP/XML mở lại được; các bảng nằm trong 9071 twip vùng chữ thực; run chỉ số dưới lời định nghĩa và OMML không mất sau renumber. Ba CSV mở lại đủ 123/88/14 dòng. Hash 20 đầu vào và 193 hỗ trợ không đổi. Bảy tệp cuối được mở lại, kiểm tra không rỗng và phần bắt buộc sau đóng QA.

QA độc lập sau dựng: PASS_STATIC_BOUNDED. R1 đã render bằng LibreOffice 24.2.7 và kiểm tra trực quan các bảng, glossary và equation; Microsoft Word chưa chạy. Chi tiết nằm trong [báo cáo bảy cổng](MP1_CH2_2_4_7_GATE_REVIEW.md), được phân biệt với xác minh nguồn nguyên thủy. Cổng 1 giữ hạn chế nguồn; cổng 7 còn giới hạn cross-renderer. Kết quả chung PARTIAL_WITH_FINDINGS.

## Bảy tệp giao nộp và dấu vết

| Tệp cuối | Bytes | SHA-256 |
|---|---:|---|
| [MP1_CH2_2_4_INTEGRATED.docx](MP1_CH2_2_4_INTEGRATED.docx) | 74271 | `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea` |
| [MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv](MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv) | 579138 | `d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49` |
| [MP1_CH2_2_4_MASTER_TERMINOLOGY.csv](MP1_CH2_2_4_MASTER_TERMINOLOGY.csv) | 201384 | `eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534` |
| [MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv](MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv) | 1162 | `3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23` |
| [MP1_CH2_2_4_INTEGRATION_CHANGELOG.md](MP1_CH2_2_4_INTEGRATION_CHANGELOG.md) | 41245 | `0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d` |
| [MP1_CH2_2_4_7_GATE_REVIEW.md](MP1_CH2_2_4_7_GATE_REVIEW.md) | 16640 | `751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70` |


Báo cáo thực thi là tệp thứ bảy, không tự ghi hash của chính nó. Script/phân tích tạm không phải deliverable cuối và nằm ngoài thư mục đích. Không commit, push, đổi nhánh hoặc sửa trạng thái/registry.

## Giới hạn và bước tiếp theo

- Đây là trạng thái trước remediation R1. R1 đã render bằng LibreOffice 24.2.7 và kiểm tra các trang bảng/glossary/equation; Microsoft Word vẫn chưa chạy. Kiểm tra Word riêng vẫn còn cần thiết.
- Đơn vị k_i ở phương trình (15) của M23 giữ `UNVERIFIED_UNITS_EQUATION_TEXT_VERIFIED`; không gán đơn vị, không sử dụng phương trình hay đồng nhất với k của M22.
- Giới hạn nhiệt độ/tốc độ của M26/M27; kéo khác uốn; thí nghiệm thép khác mô phỏng NiTi; hiệu chỉnh và dữ liệu Chen được dùng lại không thành kiểm chứng độc lập.
- M31 đo tiếp xúc dây–cao su; M32 tách nguyên mẫu SMP/SMA; M37 chưa tách độc lập pha R, nguồn dây, xử lý nhiệt và Af. Bất nhất nhãn xử lý nhiệt M37 và tiêu chí tỷ số phục hồi M32 không được tự giải quyết.
- M12 là ECF, áp âm tạo kẹt hạt còn áp dương tạo uốn; nhãn áp từ bơm riêng không thành áp khoang đo trực tiếp. M33 là bơm SMA ướt; M34 là cuộn SMA–vỏ mềm, không tự thành piston MP1.
- M33 chỉ có (1) được giữ và kiểm tra lại trong lần tích hợp. Giới hạn và dấu hiệu sai khác hệ số ở nhóm (8)/(9) đã ghi trong hồ sơ gốc vẫn ngoài phạm vi sử dụng; không tuyên bố toàn bộ phương trình M33 đã xác minh.
- Năm số báo 2022 của M25 chưa được PDF cung cấp xác nhận; bản tích hợp dùng trực tuyến 03/08/2021, không suy năm từ tên tệp.
- Topology dây–dây/dây–bao, môi chất, miền pha/nhiệt của dây chịu tải và SMA chấp hành, đường truyền áp suất, thông số phớt/rò/độ mềm, tải pháp tuyến cục bộ, hệ số ma sát, đại lượng uốn và khả năng nhận dạng MP1 vẫn mở. Không có luật áp suất–tiếp xúc–độ cứng hoặc kết luận tính mới/H1 mới.

Mở/kết xuất bản DOCX và rà từng trang khi có Word hoặc công cụ tương thích. Dừng ở mục 2.4 và đúng bảy tệp; không tự thực thi §2.5.


## Layout remediation R1 — 18/10/2026

The selected final DOCX is the `candidate_nor.docx` layout candidate from the isolated remediation workspace. This update changes presentation only.

- Scientific tables 2.4.1–2.4.4: four native six-column tables retained, fixed 9071-twip width, non-equal column widths, Times New Roman 8.5 pt, left aligned, zero paragraph indents/spacing, space wrapping, repeated headers and non-splitting rows. LibreOffice visual review of rendered table pages 3, 7, 10 and 13 found no clipping or mid-word line breaks.
- Glossary: 88 entries retained in a three-column native Word table across seven rendered pages. English/Vietnamese terms share column 1, full definition/context share column 2, and source attribution remains column 3. First, continuation and last glossary pages were inspected; headers repeat and no clipping was seen.
- M33 equation: the mathematical text remains `Q_out ≥ Q_in`, editable OMML with one `m:sSub` per subscript. The selected candidate adds only `<m:nor/>` to the `out` and `in` subscript-label runs. The source inequality, variables, attribution and definitions are unchanged.
- Rendering: isolated LibreOffice 24.2.7 rendered the baseline at 29 A4 pages and the remediation candidate at 23 A4 pages. The baseline and layout-only/Cambria candidates retained the malformed red right subscript; the selected candidate rendered both subscripts correctly. Microsoft Word was not run, so Word-specific rendering is unverified. The Cambria candidate was not selected because Cambria Math is unavailable on this host and did not fix the LibreOffice defect.
- Preservation: 101 body paragraphs, four scientific table cell sets, 88 glossary entries, 13 DOI references, 14 mappings and all three CSVs were checked against the remediation baseline. The original seven deliverables and 20 input/support hash sets remain unchanged except for this authorized replacement of the integrated DOCX.

Final DOCX SHA-256: `d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea`.

## Final report fields — layout remediation R1

TASK_ID: MP1-CH2-2.4-INTEGRATION-LAYOUT-REMEDIATION-R1  
STATUS: PARTIAL_WITH_FINDINGS  
SCIENTIFIC_CONTENT_PRESERVED: PASS  
SCIENCE_TABLES: 4/4 retained, cell text and citations preserved  
MID_WORD_WRAPPING: PASS in inspected LibreOffice pages 3, 7, 10 and 13  
GLOSSARY_TERMS: 88/88 retained  
GLOSSARY_LAYOUT: PASS in inspected LibreOffice rendering, three columns, seven pages  
GLOSSARY_CITATIONS: PASS, source cells and contextual citations preserved  
M33_EQUATION_CORRECTNESS: PASS, Q_out ≥ Q_in unchanged  
M33_EQUATION_EDITABILITY: PASS, one editable OMML object  
M33_RENDER_COMPATIBILITY: PASS in LibreOffice with m:nor; Microsoft Word unverified  
REFERENCES: 13 DOI references retained  
CITATION_MAPPING: 14 mappings retained  
TRACEABILITY_RECORDS: 123 retained  
BASELINE_IMMUTABILITY: PASS for original inputs and support hashes; authorized integrated DOCX replacement only  
GATE_1: PARTIAL_WITH_FINDINGS  
GATE_2: PASS  
GATE_3: PASS with intentional OMML compatibility adjustment  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS  
GATE_7: PARTIAL_WITH_FINDINGS, LibreOffice visual review complete and Word unverified  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: PARTIAL_LIBREOFFICE_VERIFIED_MS_WORD_NOT_VERIFIED  
FILES_CHANGED: Integrated DOCX plus this execution report, seven-gate review and integration changelog; CSV registers unchanged  
UNRESOLVED_LIMITATIONS: Microsoft Word rendering, plus all scientific limitations recorded in the original integration baseline  
NEXT_ACTION: Manual Microsoft Word rendering check if required; stop at §2.4 and do not proceed to §2.5
