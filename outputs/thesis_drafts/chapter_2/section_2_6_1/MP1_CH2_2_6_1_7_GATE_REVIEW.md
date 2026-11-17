# Kiểm tra bảy Gate cho tiểu mục 2.6.1

TASK_ID: MP1-CH2-2.6.1-RESEARCH-THESIS-DRAFT  
REVIEW_AUTHORITY: SELF_REVIEW, gồm ROOT và worker QA trong cùng phiên. Không phải INDEPENDENT_CHATGPT_ACCEPTANCE.  
FINAL_SELF_REVIEW_DECISION: ACCEPTED_WITH_DOCUMENTED_LIMITATIONS  
EXECUTION_STATUS: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED

Bản thảo được chấp nhận có giới hạn ở cấp tự rà soát nội dung, truy xuất và cấu trúc Word. Gate 7 còn thiếu kiểm tra trực quan; không khẳng định dàn trang đã đạt. Không có lỗi khoa học trọng yếu được phát hiện trong phạm vi kiểm tra này. Nghiệm thu độc lập còn chờ người dùng chuyển năm tệp cho người kiểm định bên ngoài phiên.

Địa chỉ Word trong CSV dùng chỉ số từ 0: paragraph[0] là tiêu đề; paragraph[1]–[15] là P01–P15. Glossary là table[0], row[0] là đầu bảng, row[1]–[14] là thuật ngữ, cell[1] chứa định nghĩa và ngữ cảnh. Pxx chỉ là tên dùng trong báo cáo, không xuất hiện trong luận văn. Có 70 bản ghi ở thân, 14 bản ghi glossary; không phải 84 phát hiện độc lập.

## Gate 1 — Tuân thủ dàn ý gốc

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS  
Phương pháp: đọc trực tiếp PDF dàn ý canonical trang vật lý 14 và DOCX dàn ý; đối chiếu hai dòng 2.6.1 trong Crosswalk, Writing Brief, Source Matrix và bản Word cuối.  
Bằng chứng: bảng ánh xạ dưới đây; 15 đoạn thân; dòng outline_bullet trong CSV.  
Finding: tên ngắn trong dàn ý/WEP là “Điều đã có cơ sở”; tên dài trong Word là đúng TARGET_SECTION do người dùng trực tiếp yêu cầu. Đây là thay đổi tên được ủy quyền, không tự tạo bullet hoặc chuyển phạm vi. Hai bullet nguyên gốc khớp PDF/WEP.  
Ưu tiên: giới hạn biên tập đã ghi nhận, không có lỗi thiếu bullet.

- [x] Tên và số 2.6.1 đúng yêu cầu hiện tại; khác biệt tên gốc được ghi nhận công khai.
- [x] Phạm vi đúng tổng hợp kết quả đã được thiết lập; readiness EVIDENCE_READY giữ nguyên.
- [x] B01 được bao phủ: jamming, áp dương, khóa ma sát, chuyển pha TiNi, trượt giữa dây, SMA tạo lực/áp trên các kiến trúc khác nhau.
- [x] B02 được bao phủ: mô hình liên tục, mô hình lớp có trượt và mô hình tương tác dây có miền đối chiếu riêng.
- [x] Có ánh xạ bullet → yêu cầu → lập luận → bằng chứng → vị trí Word.
- [x] Trình tự theo bốn nguồn lõi M09 → M11 → M14 → M18, sau đó bổ sung từ corpus cho hai bullet.
- [x] Không chép đoạn dài từ §§2.3–2.5; nội dung được tổng hợp lại theo kết quả và phạm vi kế thừa.
- [x] Không viết thay §2.6.2, §2.6.3 hoặc §2.6.4; chỉ một câu chuyển ngắn cuối P15.
- [x] Phân biệt kết quả công bố với suy luận tác giả trong CSV và cách diễn đạt.
- [x] Các yêu cầu chưa kiểm tra được, nhất là render, được ghi tại Gate 7.

| Bullet gốc | Yêu cầu khoa học | Luận điểm / bằng chứng | Vị trí Word |
|---|---|---|---|
| 2.6.1-B01 | Các cơ chế đã có tiền lệ trong các kiến trúc khác nhau | Áp tạo chuyển động và áp tạo kẹt M09; áp dương kẹt lớp M11; phụ thuộc cấu hình M14; trượt M17/M22; TiNi M26; SMA siết M31 và tạo áp M34 | P02–P04, P06–P07, P09–P12; tổng hợp P15 |
| 2.6.1-B02 | Mô hình đã được đối chiếu trong phạm vi riêng | M18 so với thí nghiệm PVC; M17 lớp rời rạc và so số/thử; M22 hiệu chuẩn tham số; phân biệt cấp kiểm tra; GUM hỗ trợ phương pháp đo | P05–P08, P13–P14; tổng hợp P15 |

Các bullet nguyên văn và provenance phiên bản được lưu trong Execution Report. Không suy luận thêm một bullet thứ ba từ các axis nội bộ.

## Gate 2 — Truy xuất luận điểm

STATUS: PASS  
Phương pháp: ROOT đọc lại toàn bộ Word; assert từng anchor của 70 bản ghi thân và 14 bản ghi glossary. Đọc CSV bằng csv.DictReader; đối chiếu 29 Evidence IDs với hồ sơ JSONL canonical, hash PDF và packet kiểm tra nguồn. Worker QA kiểm tra lại ánh xạ.  
Bằng chứng: SOURCE_TRACEABILITY.csv có 84 dòng, 33 SOURCE_GROUNDED_CLAIM, 50 INFERENCE và 1 DOCUMENT_COVERAGE; mọi locator đã truy được đến đoạn hoặc ô bảng.  
Finding: không có anchor/ID bị thiếu trong phạm vi kiểm tra. Bản ghi glossary là định nghĩa tổng hợp, được phân loại INFERENCE thay vì giả là định nghĩa trích nguyên văn.  
Ưu tiên: không còn lỗi tĩnh được phát hiện.

- [x] Mỗi khẳng định kỹ thuật có nguồn hoặc nhãn INFERENCE hợp lệ; P01 chỉ là DOCUMENT_COVERAGE.
- [x] Paper ID/Evidence ID có thật và khớp danh tính; không phát minh ID mới.
- [x] Đường PDF, SHA-256, trang vật lý, trang in và locator cụ thể được giữ trong từng bản ghi.
- [x] DIRECT_SUPPORT chỉ hỗ trợ phát hiện trong hệ nguồn; đối chiếu sang MP1 mang COMPARATOR hoặc suy luận có điều kiện.
- [x] Không dùng review để thay thực nghiệm primary; không có bài review trong tập trích dùng. GUM là METHODOLOGY.
- [x] Không có AUTHOR_DERIVATION hoặc P3_INTERNAL_DEFINITION được dùng như kết quả journal; hai loại này bằng 0.
- [x] CSV khớp Word; 70/70 anchor thân và 14/14 anchor ô bảng khớp nội dung thực.
- [x] Các câu tổng hợp nhiều nguồn giữ riêng finding, điều kiện, locator và provenance của từng Evidence ID trong các trường JSON.
- [x] Không đếm claim bị loại trong packet worker như claim đã dùng. Không đếm DOCUMENT_COVERAGE như kết quả khoa học.
- [x] Không phát hiện fabricated mapping; giữ locator gốc song song locator đã kiểm tra lại, không sửa hồ sơ canonical.

Nhãn evidence_class mô tả bản chất nguyên liệu nguồn. Với INFERENCE, nhãn EXPERIMENTALLY_DEMONSTRATED không biến chính suy luận tác giả thành một kết quả đã đo. M38 dùng MODEL_DERIVED cho mô hình phép đo/truyền bất định, source_role=METHODOLOGY; không gọi GUM là thực nghiệm, bài review hay kiểm chứng MP1.

## Gate 3 — Đối chiếu PDF, hình, bảng và phương trình nguồn

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS  
Phương pháp: ba worker kiểm tra nguồn bằng trích xuất trực tiếp và quan sát trang khi cần; ROOT mở PDF canonical và đọc lại các trang quan trọng, đối chiếu câu dùng trong Word. Kiểm tra 10 PDF nguồn được dùng và thêm PDF M28 chỉ để xác nhận phân trang M26 trong bibliography của M28. Không tuyên bố đã đọc từng trang của toàn bộ 39 PDF.  
Bằng chứng: accepted_evidence_locators, canonical_locator_original, verified_physical_page và verified_printed_page trong CSV; bảng kiểm tra nguồn ở Execution Report.  
Finding: các chi tiết định lượng giữ lại được kiểm tra: M09 0 đến −85 kPa; M11 năm lần/mức, khoảng 80 N ở 241,3 kPa; M14 lưới áp/tư thế/số chồng lấn; M18 20 tấm PVC, 60 kPa, dải ±1 độ lệch chuẩn. Không chép số liệu so hiệu suất mGrip hoặc bộ số M14 gán nhầm phương.  
Ưu tiên: không có lỗi khoa học trọng yếu được giữ trong bản thảo; giới hạn nguồn được bảo toàn.

- [x] Các giá trị và xu hướng thực nghiệm trong Word có kiểm tra trang PDF gốc.
- [x] Định nghĩa đại lượng, đơn vị, cấu hình, vật liệu, áp suất và điều kiện tải được kiểm tra ở các trang gốc tương ứng.
- [x] Mô hình dầm M14 được gọi là đối chiếu xu hướng định tính; không thành validation định lượng.
- [x] M18 Fig.7 là so với thí nghiệm PVC dưới 60 kPa; dải ±1 σ không thành khoảng tin cậy 95% hoặc kiểm chứng độc lập.
- [x] M17 phân biệt kết quả mô hình về trình tự trượt với đại lượng lực–độ võng đo được.
- [x] M22 k được khớp dữ liệu Chen đã công bố; không gọi là thí nghiệm mới hay predictive validation độc lập.
- [x] M26 giữ thử kéo gần đẳng nhiệt/nhiệt độ phòng, hai cấu trúc và trạng thái vật liệu khác nhau; không suy luật nhiệt/rate phổ quát.
- [x] M31 giao diện dây–cao su; M34 vỏ silicone biến dạng, không phải piston MP1.
- [x] Số lần lặp chỉ nêu khi nguồn cung cấp; không bổ sung n của M18 hoặc suy kiểm định thống kê chưa báo cáo.
- [x] Hiệu chuẩn, đối chiếu số và so thí nghiệm được giữ khác nhau; nguồn không chứng minh held-out testing thì không gắn INDEPENDENTLY_VALIDATED.
- [x] Trang vật lý/trang in được tách; M38 được sửa locator trong CSV mới.
- [x] Phương trình đưa vào Word: NOT_APPLICABLE, 0 OMML. Không có kiểm tra thứ nguyên của phương trình MP1 tự tạo vì không tạo phương trình.
- [x] Hình nguồn đưa vào Word: NOT_APPLICABLE, 0 hình. Không có vấn đề attribution/sao chép hình.
- [x] Bảng khoa học hoặc bảng nguồn đưa vào Word: NOT_APPLICABLE; glossary là bảng thuật ngữ tổng hợp, không bảng dữ liệu thực nghiệm.
- [x] M13 không được dùng, nên Eq.(4) bất nhất không được chép hoặc sửa; các equation anomaly M19/M23/M33 cũng không được tái sử dụng.

M38 có offset trang in/vật lý: §4.1 ở PDF 20–21/in 8–9; Eq.(10) PDF 31/in 19; Eq.(13) PDF 33/in 21; Eq.(18) PDF 35/in 23. WEP/Evidence gốc ghi Eq.(4) cho mô hình phép đo, trong PDF là Eq.(1). Chỉ locator trong CSV nhiệm vụ được hiệu chỉnh; nguồn gốc vẫn giữ nguyên để kiểm toán. Đơn vị/định nghĩa của mô hình phép đo được đọc để diễn giải văn xuôi, không chèn các công thức ấy vào Word.

## Gate 4 — Tổng hợp liên nghiên cứu

STATUS: PASS  
Phương pháp: ROOT rà chuỗi lập luận P02–P15, tìm các câu nối giữa kiến trúc, mô hình và đại lượng; đối chiếu Cross-study Comparisons của WEP và WP-E.  
Bằng chứng: P04 đặt ba kiến trúc cạnh nhau; P06–P08 nối mô hình lớp/liên tục/cáp; P09–P10 nối vật liệu và tiếp xúc; P11–P12 nối hai cách chấp hành SMA; P13–P15 tổng hợp cách kế thừa.  
Finding: có đối chiếu liên nghiên cứu; không tính các hồ sơ dùng lại thành thực nghiệm độc lập.  
Ưu tiên: không còn lỗi được phát hiện.

- [x] Có luận điểm tổng hợp theo cơ chế và cấp mô tả, không chỉ lần lượt tóm tắt các bài.
- [x] Đối chiếu kiến trúc, vật liệu, hình học và đường truyền áp suất tại P02–P04, P09, P11–P12.
- [x] Giữ điều kiện tải/ngàm/cáp chịu kéo khi diễn giải kết quả mô hình và đo.
- [x] Phân biệt lực giữ vật, độ cứng lực–độ võng, độ cứng uốn và mô đun vật liệu tại P03/P13/glossary.
- [x] Đối chiếu giả thiết mô hình lớp, môi trường liên tục và tương tác dây tại P06–P08.
- [x] Phân biệt thực nghiệm, kết quả mô hình, đối chiếu FEA và hiệu chuẩn.
- [x] Không gọi khớp tham số là kiểm chứng độc lập.
- [x] Nêu nội dung có thể kế thừa cho MP1, không chuyển nguyên tham số hay các cận của cấu hình khác.
- [x] Không so sánh đại lượng khác thứ nguyên như tương đương; không xếp hạng công nghệ.
- [x] Không xem M17/M18 pilot reuse hoặc dữ liệu Chen dùng lại như lần tái lập độc lập.
- [x] Không gộp những dữ liệu khác cấu hình để tính giá trị chung; không cộng các ID thành cỡ mẫu.

## Gate 5 — Giả thiết, giới hạn cơ học và ranh giới khoa học

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS  
Phương pháp: ROOT kiểm tra các ranh giới người dùng quy định tại P05–P15 và từng định nghĩa glossary; đọc P3 canonical để bảo toàn trạng thái dù không đưa giả thuyết vào thân.  
Bằng chứng: P06/P07/P09/P10/P12/P13; CSV assumptions/limits; P3 và WP-E read-only.  
Finding: chưa có bằng chứng trực tiếp trên cấu hình MP1; đây là giới hạn chuyển giao hợp lệ, không phải lý do dựng một khoảng trống mới.  
Ưu tiên: giới hạn khoa học phải giữ khi tích hợp.

- [x] E khác EI/B và K; K giữ quy ước độ dốc hoặc F/δ theo nguồn, không tự quy đổi sang B.
- [x] Áp suất nguồn, áp suất tại mẫu và ứng suất pháp tuyến cục bộ khác nhau.
- [x] Giới hạn sức kháng ma sát khác lực/ứng suất ma sát thực tế.
- [x] Trượt hoàn toàn không có nghĩa ma sát bằng 0 hoặc các dây MP1 uốn độc lập.
- [x] Không có câu suy perfect stick cục bộ thành tiết diện liên hợp hoàn toàn.
- [x] Vòng trễ toàn cục không tự xác định cơ chế/vị trí tiêu tán.
- [x] TiNi giữ nhiệt độ, pha và lịch sử tải; không suy định luật tốc độ rộng từ thử gần đẳng nhiệt.
- [x] Các cận của nguồn vẫn phụ thuộc giả thiết, không coi là cận đã chứng minh áp dụng MP1.
- [x] Không tuyên bố tham số MP1 đã nhận dạng hoặc cơ cấu SMA–piston đã kiểm chứng.
- [x] Không tuyên bố bác bỏ H0b, chứng minh H1 hoặc tính mới tuyệt đối.
- [x] Không đưa giả thuyết nội bộ vào văn xuôi. H0b=NOT_FALSIFIED_LIVE_COMPETITOR và H1=INSUFFICIENT_EVIDENCE giữ nguyên trong báo cáo.
- [x] Không chốt năm pending human decisions hoặc thiết kế Bench A/B.
- [x] Không mở lại G00 hoặc biến G01–G08 thành novelty proof; không thay scientific/registry state.

## Gate 6 — Trích dẫn và thư mục

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS  
Phương pháp: kiểm tra nhan đề, thứ tự tác giả, năm, DOI, thông tin xuất bản trên trang đầu/cuối PDF; đối chiếu registry; quét citation theo thứ tự XML thân và bảng; so từng reference với danh tính nguồn.  
Bằng chứng: 10 references, 9 DOI duy nhất; số cục bộ [1]–[10] xuất hiện lần đầu đúng thứ tự. 51 lượt gọi nguồn sau mở dải, gồm 27 ở thân và 24 ở glossary; 44 token ngoặc số nguyên dạng. Không tính 10 nhãn đầu bibliography vào citation occurrences.  
Finding: M22 DOI bị cụt trong registry được phục hồi đúng theo PDF; M26 là bản proof, tập 50/tr.3009–3026 được xác nhận qua mục 14 bibliography M28, PDF 19. Không suy số kỳ còn thiếu.  
Ưu tiên: giới hạn metadata được ghi nhận; không có reference sai danh tính được phát hiện.

- [x] Tên và thứ tự tác giả khớp PDF; nhan đề, tên tạp chí, năm và DOI khớp danh tính.
- [x] Volume/issue/pages/article number được đưa vào khi có bằng chứng; không đoán issue của M09/M26/M34 hoặc các tạp chí không ghi số kỳ.
- [x] M26 final pagination có provenance secondary-local rõ; không giả là đọc từ proof M26.
- [x] M38 là tài liệu JCGM 100:2008, tác giả tổ chức, không bịa DOI/journal.
- [x] Định dạng số cục bộ như các bản thảo độc lập; không sửa numbering baseline hoặc tự tích hợp toàn Chương 2.
- [x] Thứ tự xuất hiện đầu tiên [1]–[10] đúng trong Word.
- [x] Tất cả citation thân và glossary có reference; không reference thừa hoặc nguồn lặp thành hai mục.
- [x] Citation trong bảng khoa học/caption nguồn/lời giải thích phương trình: NOT_APPLICABLE vì không có các đối tượng đó. Caption glossary không chứa dữ liệu cần trích mới.
- [x] Glossary khớp nguồn theo từng hàng, không chỉ cùng số lượng.
- [x] Không có Paper ID, Evidence ID, P3_CANONICAL hoặc số citation cũ trong manuscript.
- [x] Phải renumber khi tích hợp §2.6 nếu số chung khác; không thực hiện trong nhiệm vụ này.

## Gate 7 — Tiếng Việt cơ khí và Word

STATUS: PARTIAL_WITH_FINDINGS  
Phương pháp: ROOT đọc lại 15 đoạn và toàn bộ 14 hàng glossary/10 references bằng python-docx; QA worker đối chiếu nội dung; mở ZIP và parse các part XML bằng lxml; kiểm tra styles, bảng và nhãn. Không có LibreOffice/soffice hoặc Microsoft Word khả dụng.  
Bằng chứng: 15/15 đoạn, 70/70 câu/đơn vị thân, 14/14 glossary, 84/84 locator, 10/10 references khớp; ZIP/XML_VALID. SHA-256 DOCX cuối: `983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e`.  
Finding mở: RENDER-01, chưa kiểm tra trực quan ngắt trang, bảng có tràn/cắt chữ không, references hoặc trang trắng.  
Ưu tiên: bắt buộc kiểm tra dàn trang trước nghiệm thu trình bày; không phải lỗi khoa học đã quan sát.

- [x] Văn xuôi khoa học tiếng Việt; tên tác giả/thuật ngữ Anh trong glossary/nhan đề reference được giữ theo yêu cầu.
- [x] Mỗi đoạn có luận điểm; bỏ câu quảng bá và cách diễn đạt cường điệu; không chép dài baseline.
- [x] Giữ thuật ngữ §2.5: hiệu chuẩn mô hình, kiểm chứng mô hình; khác biệt hiệu chỉnh/hiệu chuẩn ở baseline cũ được ghi nhận trong provenance thuật ngữ.
- [x] Không có workflow, Task ID, machine status hoặc mã nguồn trong thân Word/glossary.
- [x] A 4, lề trên/dưới 2.5 cm, trái 3 cm/phải 2 cm; Times New Roman 12 pt prose và heading 12 pt đậm.
- [x] Giãn dòng 1.15 theo Normal của baseline tích hợp §2.5; glossary 10 pt, căn trái.
- [x] Không trang bìa riêng, header/footer biên tập hoặc metadata workflow.
- [x] OMML chỉnh sửa/hiển thị: NOT_APPLICABLE, số công thức 0.
- [x] Một glossary native Word table,3 cột, 15 hàng gồm header; header lặp, hàng không tách; tblLayout=fixed, grid 4.5/9.5/2 cm trong vùng chữ 16 cm.
- [x] Caption glossary giữ cùng đối tượng kế tiếp; references có hanging indent và keep_together. Các cờ XML không được gọi là visual PASS.
- [x] Glossary và CSV khớp đủ danh tính, nghĩa, ngữ cảnh và nguồn.
- [x] DOCX ZIP/XML hợp lệ, mở lại được; không thiếu đối tượng nội dung theo kiểm tra văn bản.

- [ ] Render DOCX bằng Word hoặc công cụ tương thích: NOT_VERIFIED, không có bộ render.
- [ ] Xem từng trang, kiểm tra tràn/cắt chữ/ký hiệu/ngắt caption/reference/trang trắng: NOT_VERIFIED.
- [ ] Tổng số trang sau render: NOT_AVAILABLE.

Không dùng số trang lưu sẵn trong docProps hoặc ước lượng để thay cho kết xuất. Không tuyên bố Microsoft Word hoặc LibreOffice đã kiểm tra tệp này.

## Kết quả và hành động còn lại

| Gate | Status |
|---|---|
| 1 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| 2 | PASS |
| 3 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| 4 | PASS |
| 5 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| 6 | PASS_WITH_DOCUMENTED_LIMITATIONS |
| 7 | PARTIAL_WITH_FINDINGS |

Không có lỗi khoa học trọng yếu đang mở được phát hiện. RENDER-01 là thiếu xác minh trình bày. META-01 bảo lưu metadata kỳ không có bằng chứng và nguồn thứ cấp nội bộ cho phân trang M26. SCOPE-01 ghi tên mở rộng theo yêu cầu thay tên ngắn trong dàn ý. Các giới hạn chuyển giao sang MP1 được bảo toàn, không biến thành khoảng trống mới. Không yêu cầu sửa baseline hoặc viết phần tiếp.

NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE. Người kiểm định tiếp theo cần mở/render Word và xem từng trang; kiểm định khoa học độc lập không được thay bằng báo cáo SELF_REVIEW này.
