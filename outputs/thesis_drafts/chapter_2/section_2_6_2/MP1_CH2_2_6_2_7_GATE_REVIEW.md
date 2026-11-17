# Tự kiểm tra bảy Gate — §2.6.2

TASK_ID: MP1-CH2-2.6.2-RESEARCH-THESIS-DRAFT
REVIEW_AUTHORITY: SELF_REVIEW
INDEPENDENT_ACCEPTANCE: NOT_YET_PERFORMED
FINAL_SELF_REVIEW_DECISION: ACCEPTED_WITH_DOCUMENTED_LIMITATIONS

Các Gate dưới đây áp dụng cho đúng bản Word có SHA-256 `fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63`. PASS không có nghĩa quan hệ riêng của MP1 đã được chứng minh.

## Phạm vi và ánh xạ dàn ý

ORIGINAL_OUTLINE_FILE: `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf`

| Bullet | Trang PDF vật lý | Nội dung nguyên bản | Câu hỏi bắt buộc | Bằng chứng | Nhóm giới hạn | Vị trí Word |
|---|---:|---|---|---|---|---|
| B01 | 14 | Interface chi phối chưa được khóa; áp suất tại nguồn chưa được chứng minh là normal traction hữu hiệu. | Giao diện nào đã được đo/mô hình hóa, và áp suất được liên hệ với tải pháp tuyến tới đâu? | M13-E04/E06; M15-E02/E05; M16-E02/E05; M31-E06/E08; M34-E02/E04/E07/E09; M38-E02/E03/E04 | SOURCE_LIMITATION; APPLICABILITY_LIMITATION; IDENTIFIABILITY_LIMITATION; MODEL_ASSUMPTION_SIMPLIFICATION; PENDING_HUMAN_DECISION | P02–P04, P11–P13, P15 |
| B02 | 15 | Chưa biết H0b có dự đoán được response pressure-dependent khi transformation, contact và sleeve cùng hoạt động trong miền thí nghiệm hay không. | Điều kiện của mô hình và dữ liệu kiểm tra cho phép đánh giá điều gì khi chuyển sang TiNi có giam giữ? | M15-E03; M16-E03/E04/E05/E06/E07; M18-E01/E02/E06/E07; M22-E01/E02/E03/E04; M26-E01/E03/E04/E05/E07; P3_HYPOTHESIS_RECONCILIATION.md | APPLICABILITY_LIMITATION; IDENTIFIABILITY_LIMITATION; EXPERIMENTAL_COVERAGE_LIMITATION; MODEL_ASSUMPTION_SIMPLIFICATION; PENDING_HUMAN_DECISION | P04–P10, P13–P15 |
| B03 | 15 | Chưa có cơ sở để khẳng định cơ chế mới hoặc universal novelty. | Giới hạn chuyển giao có cho phép suy ra cơ chế mới hoặc tính mới tuyệt đối hay không? | M13-E01/E06; tổng hợp các nguồn bổ sung; P3/WP-E/WEP cho phạm vi nội bộ | EXPERIMENTAL_COVERAGE_LIMITATION; APPLICABILITY_LIMITATION; DOCUMENT_COVERAGE | P01–P02, P14, P16 |

Pxx dùng riêng trong hồ sơ QA; Word không chứa mã đoạn. P01–P16 tương ứng paragraph[1]–[16] theo chỉ số0-based, title=0. Citation cục bộ, có thể renumber khi tích hợp, không thay baseline.

## GATE 1 — ORIGINAL OUTLINE COMPLIANCE

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
SEVERITY: DOCUMENTED_LIMITATION; không P1/P2

METHOD: Đọc PDF dàn ý bằng trích xuất và ảnh trang14–15; đối chiếu chín WEP bắt buộc; đọc toàn bộ16 đoạn Word và mapping CSV.

EVIDENCE: PDF canonical nêu ở bảng dưới; DOCX paragraph[1]–[16], title=paragraph[0]; cột outline_bullet và integrated_document_location trong CSV.

CHECKLIST:

- [x] Tên và số mục đúng tên làm việc người dùng yêu cầu; SCOPE-01 giải thích khác biệt với tiêu đề gốc.
- [x] Đọc trực tiếp PDF dàn ý trang vật lý14–15, riêng §2.6.2; đúng3 bullet B01–B03, không tạo bullet từ axis.
- [x] Đối chiếu Writing Brief riêng, Crosswalk, Source Matrix và readiness BOUNDED_WRITING_READY.
- [x] Có mapping bullet → câu hỏi → evidence → loại giới hạn → Pxx/đoạn Word; không bỏ bullet bắt buộc.
- [x] Kế thừa kết quả §2.6.1 và kết luận §§2.3–2.5, không lặp dài hoặc sửa baseline.
- [x] Phân biệt giới hạn nguồn, giới hạn chuyển giao, giới hạn nhận dạng, phạm vi dữ liệu, giả thiết và quyết định nội bộ.
- [x] B03 được triển khai bằng giới hạn suy luận novelty; không viết §2.6.3/§2.6.4, chỉ câu chuyển tiếp cuối.
- [x] Kết quả nguồn khác suy luận tác giả; yêu cầu chưa đủ bằng chứng được giới hạn trong corpus/miền nguồn.

FINDINGS: Đủ3 bullet. SCOPE-01: tên gốc “Điều còn bất định đối với cấu hình nghiên cứu”, tên mới do người dùng ủy quyền. Crosswalk ghi14 cho cả3 nhưng B02/B03 thực ở15; chỉ correction trong đầu ra mới, không sửa canonical.

UNRESOLVED: Giới hạn readiness và đổi tên/locator được giải trình; không có thiếu bullet.

## GATE 2 — SCIENTIFIC CLAIM TRACEABILITY

STATUS: PASS
SEVERITY: NONE

METHOD: Phân tích CSV bằng csv.DictReader; truy Evidence ID trong EVIDENCE_RECORDS.jsonl; đối chiếu từng anchor với đoạn/ô Word; ROOT đọc và WorkerH kiểm tra độc lập vai trò QA trong cùng phiên.

EVIDENCE: CSV72 hàng và schema kế thừa; DOCX16 đoạn/11 hàng glossary; kết quả staticQA72/72 và11/11 đã được ghi trong ExecutionReport.

CHECKLIST:

- [x] 72/72 record có anchor/vị trí chính xác; 61 đơn vị thân bài và11 định nghĩa glossary, kiểm tra nội dung chứ không chỉ số dòng.
- [x] Paper ID,41 Evidence ID thực tồn tại trong JSONL canonical; không tạo Evidence ID hoặc dùng P3 thay journal.
- [x] Đường dẫn PDF, SHA-256, trang vật lý và trang in, locator kiểm tra trực tiếp được giữ cùng record gốc.
- [x] Vai trò DIRECT_SUPPORT cho kết quả của chính nguồn; COMPARATOR cho suy luận chuyển giao; M38 METHODOLOGY; nội bộ CONTEXT_ONLY.
- [x] Giới hạn do nguồn nói rõ khác suy từ phương pháp; suy luận giữ category INFERENCE, không gán thành kết quả thực nghiệm.
- [x] limitation_category, limitation_basis, scope_of_negative_claim đều có giá trị/NOT_APPLICABLE; negative claim có miền.
- [x] Không suy vắng mặt trong một bài thành vắng mặt toàn ngành; không suy thiếu phép đo thành bất khả nhận dạng.
- [x] Không dùng review như primary experiment; tập nội dung không dùng bài review để thay bằng chứng nguồn gốc.
- [x] Không biến comparator thành direct MP1 proof; không đồng nhất hiệu chuẩn với kiểm chứng dự đoán độc lập.
- [x] DOCUMENT_COVERAGE không tính là kết quả khoa học; ba pending records không tính là research gaps.
- [x] Không AUTHOR_DERIVATION/AUTHOR_PROPOSAL hoặc mapping giả; record không được dùng không báo là đã dùng.
- [x] Kết luận nhiều nguồn giữ từng thành phần hỗ trợ, record gốc và gói đối chiếu trực tiếp trong CSV.

FINDINGS: 72 record gồm25 SOURCE_GROUNDED_CLAIM,39 INFERENCE,4 DOCUMENT_COVERAGE,1 P3_INTERNAL_DEFINITION,3 PENDING_HUMAN_DECISION. 46 record giới hạn thân bài gồm43 phân tích khoa học và3 lựa chọn; glossary không tăng số giới hạn.

UNRESOLVED: Không finding về mapping. “DIRECT_PDF_VERIFIED” chỉ cho thành phần nguồn trực tiếp; inference có trạng thái INFERENCE_WITH_DIRECT_PDF_VERIFIED_INGREDIENTS.

## GATE 3 — ORIGINAL PDF, TABLE, FIGURE AND EQUATION VERIFICATION

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
SEVERITY: DOCUMENTED_LIMITATION; không P1 còn mở

METHOD: SourceWorkersA/B/C đọc nguồn theo nhóm; ROOT kiểm tra các locator và diễn giải quyết định, tự đọc nguồn phương pháp M38 và metadata M28. Giữ gói xác minh từng EID trong CSV.

EVIDENCE: CSV accepted_evidence_locators/source_supported_information/canonical_locator_original/locator_correction_note; hồ sơ correction trong ExecutionReport; bản PDF canonical có SHA trong từng record.

CHECKLIST:

- [x] Chín PDF nội dung và một PDF M28 chỉ để kiểm tra metadata M26 đã mở/đọc trực tiếp; không nguồn nội dung chưa kiểm tra.
- [x] Đối chiếu Methods/model assumptions/setup/results/conclusion có liên quan, không chỉ tìm mục Limitations.
- [x] Ghi trang PDF vật lý riêng trang in, điều kiện tải, hình học, vật liệu, pha khi có, đại lượng và đơn vị.
- [x] Phân biệt kết quả thực nghiệm, mô hình, nghiệm số/FEA, khớp tham số và phép thử sau nhận dạng.
- [x] Đối chiếu lặp thử khi liên quan: một nguyên mẫu M13 vẫn có lặp điều kiện; M31 có phép đo ma sát riêng, không phủ nhận.
- [x] Không tạo số thống kê, số lần lặp hoặc kết luận bất định mà nguồn không hỗ trợ; không so số R² với sai số mô hình.
- [x] M15 Proposition1 ởPDF4/in12730, M16 Proposition1 ởPDF6/in2224 được sửa locator trong CSV mới.
- [x] M15 năm lớp tới80kPa khác miền M16 hai lớp0–40kPa; M16 có nhóm khóa hình năm lớp tới80kPa riêng.
- [x] uP>0 của mô hình chân không là độ lớn áp âm, không áp dương của MP1; số đo áp bladder không là trường pháp tuyến.
- [x] M18 trường trượt so FEA khác thí nghiệm lực–độ võng; M22 tham số chống trượt gộp khác hệ số ma sát thuần.
- [x] M13 Eq.(4) và Equation Notes được đối chiếu; không sao chép, tự sửa hoặc dùng anomaly để bác bỏ toàn mô hình.
- [x] NOT_APPLICABLE: phương trình/hình/bảng dữ liệu nguồn được tái tạo trong Word=0; không miễn kiểm tra claim văn xuôi.
- [x] Không thực hiện lại toàn bộ chứng minh toán học hoặc tái tính số liệu nguồn; giới hạn này được ghi rõ.

FINDINGS: Đã xử lý những locator/điều kiện thử sai của hồ sơ kế thừa và giữ nguyên record gốc. M13 EquationNotes không bao phủEq4 và SHA trong note không khớp; không dùng phương trình. Không nâng độ phù hợp hồi quy thành validation.

UNRESOLVED: Kiểm tra có giới hạn vào thành phần hỗ trợ claim, không chứng nhận lại toàn bài hoặc toàn bộ39PDF; independent external review chưa diễn ra.

## GATE 4 — CROSS-STUDY SYNTHESIS

STATUS: PASS
SEVERITY: NONE

METHOD: ROOT adjudication tổng hợp/counterevidence, sourceModels countercheck, đọc toàn16 đoạn và nguồn đối ứng; đối chiếu cấu trúc P02–P13 với kết luận P14–P16.

EVIDENCE: DOCX P02–P06 đối chiếu áp suất/mô hình; P07–P12 kiến trúc và nguồn bổ sung; P13 đo lường; P14–P16 phạm vi suy luận.

CHECKLIST:

- [x] Văn xuôi tổng hợp liên nghiên cứu theo vấn đề, không liệt kê từng bài như hồ sơ tóm tắt.
- [x] Phân biệt kiến trúc kẹt sợi nylon áp dương, kẹt lớp chân không, cáp thép song song, cáp TiNi kéo, siết SMA và micropump.
- [x] Đối chiếu hình học, vật liệu, tải, điều kiện biên, đại lượng quan sát và giả thiết mô hình.
- [x] M16 xử lý một phần giới hạn M15 bằng tác động áp phi tuyến/đàn hồi phụ thuộc áp; không tạo khoảng trống đã được xử lý.
- [x] M18 đã có mô hình liên tục nhiều lớp; M22 đã có tương tác/trượt dây; không tuyên bố toàn bộ mô hình bỏ qua các yếu tố này.
- [x] M31 có đo ma sát tách riêng thử uốn; M26 có DSC/DIC/IR và chu trình; M34 có đo áp suất và thử động, ghi nhận phản chứng.
- [x] Phân biệt kiểm tra điều khiển sau nhận dạng với độc lập dự đoán; M15/M16 chung tuyến phát triển không tính replication độc lập.
- [x] Không gộp dữ liệu khác mẫu/miền áp để mở rộng validation; không so đại lượng khác thứ nguyên như tương đương.
- [x] Không xếp hạng công nghệ thiếu tiêu chí chung; không suy thiếu bằng chứng thành novelty.
- [x] Giới hạn chuyển giao gắn câu hỏi MP1 nhưng không trình bày như quan hệ đã kiểm chứng trên MP1.

FINDINGS: Có ghi nhận nguồn giải quyết một phần giới hạn nguồn trước. Chuỗi lập luận xoay quanh miền kiểm chứng và quan sát, giữ giá trị đóng góp của nguồn.

UNRESOLVED: Không finding cần sửa; phạm vi corpus và chuyển giao tiếp tục là giới hạn hợp lệ.

## GATE 5 — MECHANICAL ASSUMPTIONS AND SCIENTIFIC BOUNDARIES

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
SEVERITY: DOCUMENTED_LIMITATION

METHOD: ROOT đọc lại ranh giới cơ học trong DOCX/CSV, P3 reconciliation canonical và WEP08; kiểm tra ngôn ngữ không thể/đã chứng minh/nhận dạng/novelty với ngữ cảnh.

EVIDENCE: P03–P15, glossary T02/T05/T06/T07/T08/T09/T10/T11 và các record nội bộ không có journal EID/DOI.

CHECKLIST:

- [x] E khác B/EI; K không tự động bằng B/EI, đổi đại lượng cần mô hình tải/hình học/biên.
- [x] Áp suất nguồn, áp suất tại mẫu và ứng suất pháp tuyến cục bộ là ba cấp khác nhau; không giả ánh xạ duy nhất đã có.
- [x] Lực ma sát thực tế khác ngưỡng ma sát; trượt hoàn toàn không là ma sát bằng0 hoặc dây MP1 uốn độc lập.
- [x] Dính cục bộ không tự là tiết diện liên hợp hoàn toàn; cận độ cứng nguồn không tự áp dụng MP1.
- [x] Vòng trễ toàn cục không nhận dạng duy nhất nguồn tiêu tán; TiNi phụ thuộc pha/nhiệt/tốc độ/lịch sử tải trong điều kiện nguồn.
- [x] Calibration khác independent predictive validation; fit tốt chưa chứng minh tham số cục bộ duy nhất.
- [x] Không phát biểu bất khả nhận dạng về nguyên lý nếu thiếu phân tích; không tuyên bố tham số MP1 đã nhận dạng.
- [x] Giả thiết lớp mỏng/độ cong chung/tiếp xúc duy trì/áp đều/ổn định cục bộ được bảo toàn, không lược bỏ khi chuyển giao.
- [x] Không tự chọn hình học/giao diện, proxy pháp tuyến, miền nhiệt/pha/tải, đại lượng chính/bất định hoặc phạm vi SMA–piston.
- [x] Không thiết kế piston/BenchA/BenchB hoặc protocol cuối; không viết §2.6.3/§2.6.4.
- [x] H0b giữ NOT_FALSIFIED_LIVE_COMPETITOR; H1 giữ INSUFFICIENT_EVIDENCE, theo P3 nguyên bản.
- [x] Không tuyên bố luật cấu thành mới, novelty tuyệt đối, bác bỏ H0b hoặc chứng minh H1.
- [x] G00 giữ đóng; G01–G08 giữ điều kiện, không làm bằng chứng novelty; pending human decisions không là khoảng trống tài liệu.

FINDINGS: Giới hạn được trình bày theo miền nguồn; mô hình TiNi/chuyển pha/tiếp xúc thông thường vẫn là đối chứng còn mở. Không có quyết định thiết kế nào được chốt.

UNRESOLVED: Năm nhóm quyết định của người nghiên cứu và khả năng chuyển giao MP1 còn mở có chủ đích; không là lỗi của draft.

## GATE 6 — CITATION AND BIBLIOGRAPHY

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
SEVERITY: DOCUMENTED_LIMITATION; không lỗi citation P1

METHOD: Đọc first/final pages từng PDF và registry, đối chiếu bibliography từ Word với metadata trong CSV; parse tất cả citations, thứ tự và DOI; M28 chỉ đối chiếu paginationM26.

EVIDENCE: Word references[1]–[9]; source_identity_metadata từng record; bảng metadata/correction trong ExecutionReport; không thay registry.

CHECKLIST:

- [x] Chín danh tính canonical: tác giả và thứ tự, tiêu đề, nơi công bố, năm, tập/số khi kiểm tra được, trang/article number và DOI.
- [x] M22 DOI đầy đủ lấy từ PDF thay giá trị canonical bị cắt; original metadata vẫn giữ và correction có provenance.
- [x] M16 dùng bản phân trang34(5),2219–2233 năm2026, không giữ nhầm advance-online chưa phân trang.
- [x] M26 bản proof có xxx; volume50/pages3009–3026 đối chiếu ở M28 canonicalPDF19, bibliography ref14; không đoán issue.
- [x] M38 là JCGM100:2008, tác giả cơ quan; không bịa DOI. Số tạp chí không xác minh không tự bổ sung.
- [x] Citation cục bộ[1]–[9] theo lần xuất hiện đầu, không sửa hệ đánh số baseline.
- [x] 17 occurrence thân+19 glossary=36, đã kiểm toàn bộ bracket; không tính nhãn bibliography thành citation.
- [x] Citation prose và glossary đều có reference; không reference thừa/trùng, không canonical bị tạo hai mục.
- [x] Caption glossary không có dữ liệu nguồn riêng; bảng khoa học/hình/phương trình=0 nên citation tại đó NOT_APPLICABLE.
- [x] Không PaperID/EvidenceID/P3_CANONICAL/TaskID/status trong Word; không số citation cũ sai.
- [x] DOI được kiểm danh tính qua PDF và canonical registry, không chỉ kiểm cú pháp; không mở corpus/Internet mới để thay nguồn.

FINDINGS: 9references,8DOI duy nhất, M38 không DOI đúng loại nguồn. Sửa cục bộM22/M16/M26 có provenance. Metadata một số issue không được canonicalPDF xác nhận nên bỏ trống, không phỏng đoán.

UNRESOLVED: Không xác minh issueM26/M34 ngoài corpus; M26pagination là crosscheck trong corpus, không publisher-finalPDF hoặc Crossref mới. Đây là giới hạn bibliographic được ghi rõ.

## GATE 7 — VIETNAMESE MECHANICAL ENGINEERING WRITING AND WORD QA

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
SEVERITY: DOCUMENTED_LIMITATION

METHOD: WorkerH static boundedQA và ROOT đọc lại Word/XML; render LO ra PDF, raster từng trang rồi ROOT quan sát6ảnh cuối. QA H có0findings, không tự nhận kiểm PDF hay visual.

EVIDENCE: Word6trang render; paragraph1–16; table0 rows1–11; XML VALID; hash DOCX/PDF và quan sát từng trang trong ExecutionReport.

CHECKLIST:

- [x] Đọc16 đoạn tiếng Việt chuyên ngành, lập luận liên tục, không khẩu hiệu/quảng bá/cường điệu hoặc lặp dài phần trước.
- [x] 11 thuật ngữ có định nghĩa, ngữ cảnh và nguồn; Word/CSV khớp theo danh tính, nghĩa và citation.
- [x] TimesNewRoman12pt prose; A4; lề trên/dưới2.5cm,trái3cm,phải2cm; giãn dòng1.15 và heading nhất quán.
- [x] Không trang bìa riêng, machine metadata/TaskID/status/workflow trong thân, header/footer cũ hoặc phần tiếp theo.
- [x] Bảng glossary Word bản địa3cột; caption đi cùng; fixedwidth/header lặp/no-splitrows; không tràn lề.
- [x] OMML/hình/bảng khoa học=0: NOT_APPLICABLE cho khả năng chỉnh sửa/hiển thị phương trình và caption hình.
- [x] Tài liệu tham khảo hangingindent và keepTogether, cả9entry không bị tách bất hợp lý.
- [x] ZIPCRC và toàn XML parse hợp lệ; mở lại DOCX bằng python-docx, đối chiếu anchors và glossary đầy đủ.
- [x] Render bằng LibreOffice24.2.7.2 trong môi trường tạm, font TimesNewRoman có sẵn; không render baseline.
- [x] ROOT đã xem từng trang1–6 của PDF ứng với đúng SHA DOCX cuối, không trang trắng/cắt chữ/mất ký hiệu/tràn bảng.
- [x] Trang5 chỉ chứa phần glossary tiếp do không tách hàng và references sang trang mới; khoảng trắng có chủ đích, không trang trắng lỗi.
- [x] MicrosoftWord validation NOT_VERIFIED; không gọi ZIP/XML là visualPASS hoặc LO là kiểm tra MicrosoftWord.

FINDINGS: Bản cuối6trang: thân1–3,glossary4–5,reference6. Không lỗi hiển thị quan sát được. Có sự khác nhau giữa Word editability/XML, visualLO và MSWord chưa kiểm.

UNRESOLVED: MicrosoftWord NOT_VERIFIED; không nghiệm thu độc lập, layout có thể khác nếu đổi ứng dụng/font.

## Giới hạn còn lại và kết luận

- Không P1/P2 chưa xử lý được tìm thấy trong phạm vi self-review. Không dùng kết quả này thay nghiệm thu độc lập.
- LOCATOR-01/SCOPE-01: lỗi trang dàn ý và khác biệt tên được giải trình, input giữ nguyên.
- META-01: issue không được kiểm tra thì không đoán; M26pagination có đối chứng trong corpus, chưa đối chiếu publisher-finalmetadata ngoài corpus.
- SOURCE-01: verification giới hạn vào các phần hỗ trợ luận điểm, không tái chứng minh toàn bộ các bài hoặc kiểm39PDF.
- APPLICABILITY-01: giả thiết và miền kiểm chứng nguồn chưa tự áp dụng cho MP1; năm nhóm quyết định vẫn mở.
- RENDER-01: LibreOffice visualPASS6trang; MicrosoftWord NOT_VERIFIED.

BASELINES_UNCHANGED: YES (26 baseline/support files; rộng hơn241 input/support files giữ nguyên SHA-256).
COMMIT_STATUS: NOT_PERFORMED
PUSH_STATUS: NOT_PERFORMED
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE
