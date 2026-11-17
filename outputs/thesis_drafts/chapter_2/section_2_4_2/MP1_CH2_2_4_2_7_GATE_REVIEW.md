# §2.4.2 — Rà soát bảy cổng chấp nhận

TASK_ID: MP1-CH2-2.4.2-RESEARCH-THESIS-DRAFT  
STATUS: PARTIAL_WITH_FINDINGS  
Phạm vi: bản thảo Thạc sĩ định hướng nghiên cứu, Kỹ thuật Cơ khí, HCMUT–VNU-HCM; chỉ §2.4.2.

## Gate 1 — Tuân thủ dàn ý: PARTIAL

- B01: đã tổng hợp cơ học cáp, trượt giữa dây/lớp, vòng trễ uốn, mô hình dầm phân lớp, dầm dây cong có biến dạng riêng và FE tiếp xúc. M24 cho bằng chứng vòng trễ thực nghiệm; mô hình của nó chỉ ước lượng độ cứng nhánh, chưa dự đoán trọn vòng trễ.
- B02: phân biệt bó dây thẳng, mô hình cáp dây song song, cáp xoắn một/nhiều tao, bện và hệ có bao. Không áp số dây hay mặt tiếp xúc của cáp nguồn cho MP1.
- PARTIAL phản ánh phạm vi bằng chứng: bốn nguồn không có nghiên cứu chuyên biệt về bện hoặc bao chủ động tương đương MP1; phần phân biệt này là định nghĩa hình học/biên tập. Ghi nhận tác dụng vỏ bảo vệ trong M22/M23 không thành một kiểm chứng độc lập của sleeve.
- Không triển khai mô hình cận MP1 của §2.5.2, phương pháp đo của §2.5.3 hoặc nội dung §2.4.3. Chỉ có đoạn chuyển tiếp tới SMA điều biến ma sát.

## Gate 2 — Truy xuất nguồn: PASS

- CSV có 34 bản ghi: 24 SOURCE_GROUNDED_CLAIM, 6 INFERENCE, 2 AUTHOR_PROPOSAL, 2 DOCUMENT_COVERAGE. Đây không phải 34 phát hiện khoa học độc lập.
- Mỗi luận điểm nguồn có DOI, tiêu đề, Paper ID, Evidence ID hiện hữu, PDF gốc, SHA-256, trang vật lý, mục/hình/phương trình được kiểm tra, loại bằng chứng, điều kiện/giả thiết, đại lượng và phạm vi kiểm chứng.
- A01→M22-E01; A02→M23-E02; A03→M24-E01; A04→M25-E02 đã đối chiếu đúng Source Matrix. Các record bổ sung nằm trong cùng bốn bài, không thay nguồn hay tạo Evidence ID mới.
- Vai trò trực tiếp chỉ áp dụng cho cơ học của hệ nguồn. Suy luận áp dụng cho MP1 được tách riêng khỏi kết quả nguồn và yêu cầu nhận dạng của tác giả.
- Record C33 ghi trạng thái đơn vị M23; C34 ghi phạm vi tài liệu, không tính là phát hiện. C31/C32 là đề xuất/đoạn chuyển tiếp.

## Gate 3 — PDF gốc: PASS, có phát hiện sai khác

- Bốn canonical PDF được mở, trích xuất và đọc các trang liên quan. M22 có 9 trang; M23 có 15; M24 có 13; M25 có 15 gồm bìa. Locator trong CSV là trang vật lý đã đối chiếu lại, không mặc nhiên kế thừa ghi chú cũ.
- M22: pp.2–3 giả thiết/tiếp xúc lớp; pp.5–7 dữ liệu hiệu chỉnh, nghiệm giới hạn, ảnh hưởng vỏ bảo vệ; p.9 tài liệu Chen.
- M23: pp.2–3 Figs.1–2 chuyển tiết diện; pp.3–5 ứng suất phẳng/quan hệ lớp; pp.7–9 dữ liệu Chen; pp.10–13 trường cục bộ; p.15 nguồn dữ liệu. Fig.13 ở p.9, Table2 ở p.10, Eq.26 ở p.7; không dùng locator sai từ ghi chú.
- M24: pp.3–5 động học; pp.5–7 thiết bị và vòng trễ; pp.8–11 hình học/đối chiếu; p.12 kết luận. R1=61 dây, R2=7×19=133 dây, khác các giá trị sai trong ghi chú. Bài có giới hạn mô hình và không khẳng định dự báo toàn vòng trễ.
- M25: p.1 bìa metadata; pp.3–5 hình học, Souza/UMAT, tiếp xúc và biên kéo; pp.5–6 thảo luận đối chiếu, đồ thị ở các trang tiếp theo. Không có thí nghiệm uốn mới.
- Không đưa phương trình nguồn vào DOCX. Đơn vị chưa rõ của k_i không được sửa, tính toán hoặc gán lại. Số dây/tao, tần số 0,2 Hz của M24 và đơn vị độ dốc đã đối chiếu với nguồn trước khi dùng.

## Gate 4 — Tổng hợp liên nghiên cứu: PASS

So sánh được xây dựng quanh mức mô tả: hàng dây→dầm lớp của M22; đàn hồi hai chiều/biến trạng thái của M23; dầm dây cong và các chế độ động học của M24; hình học tiếp xúc ba chiều có SMA của M25. Bảng 2.4.2 giữ riêng vật liệu, hình học, tải/đại lượng và cơ sở kiểm chứng. Tái sử dụng Chen được nói rõ; độ chi tiết FE không bị dùng làm chứng cứ tự động về độ chính xác cao hơn.

## Gate 5 — Giả thiết cơ học và chuyển mô hình: PASS

- Tách E (vật liệu), EI (cấp tiết diện) và độ dốc lực–chuyển vị (cấp mẫu/đồ gá). Không so sánh trực tiếp các đại lượng khác thứ nguyên.
- Trượt lớp là biến hiệu dụng, không phải trường vi trượt đo được tại tiếp xúc dây tròn. Trượt không đồng nhất với dẻo vật liệu.
- Trạng thái partial stick của M24 là giả thiết biến dạng riêng, khác partial slip tổng quát. Không nhập ngưỡng dính–trượt từ kiến trúc khác.
- Kéo kiểm chứng trong M25 không thay cho uốn. Vòng trễ có thể chứa nhiều cơ chế; mô hình giới hạn và đường tổng thể không nhận dạng duy nhất lực tiếp xúc hoặc tiêu tán ma sát.
- Áp suất nguồn, lực pháp tuyến, ứng suất tiếp xúc và sức kháng ma sát giữ riêng. Không đưa luật áp suất→ma sát mới.
- Hình thái dây–dây/dây–bao, bố trí xếp dây, trạng thái TiNi, biên và đại lượng uốn MP1 còn phải xác định; không chọn cơ chế trội hay tuyên bố novelty.

## Gate 6 — Citation và metadata: PASS

Ánh xạ chuẩn: [1] M22 DOI 10.1061/(ASCE)ST.1943-541X.0002171; [2] M23 DOI 10.1016/j.ijmecsci.2020.106192; [3] M24 DOI 10.1016/j.engstruct.2024.119217; [4] M25 DOI 10.1080/15376494.2021.1955313.

Số trích dẫn được gán theo danh tính nguồn, kiểm tra trong thứ tự phần tử Word (gồm bảng), không thay số không giới hạn. Bốn tài liệu đều được dùng; tác giả theo đúng thứ tự PDF. M23 ghi tập194/2021 và ngày online11/11/2020. M24 là Engineering Structures323/2025, online03/11/2024. M25 ghi phiên bản online03/08/2021 trong đúng tạp chí Mechanics of Advanced Materials and Structures; không tự thêm tập/trang/năm số phát hành từ tên tệp2022. Thuật ngữ biên tập không được gán nguồn giả.

## Gate 7 — Văn phong và DOCX: PARTIAL

Văn xuôi tiếng Việt theo chuyên ngành Cơ khí, dùng nhất quán trượt tại giao diện, dính, độ cứng uốn EI, độ cứng kết cấu, biến dạng riêng, hiệu chỉnh/kiểm chứng. Các chữ viết tắt SMA, FE, UMAT được giải thích; UMAT là chương trình con vật liệu, không phải mô đun Young. Không có Paper ID, Evidence ID, mã kiểm tra hay nhật ký PDF trong bản thảo. Có bảng so sánh Word-native và phụ lục thuật ngữ 26 mục với nguồn riêng/nhãn biên tập.

Cấu trúc ZIP/XML, A4/TNR, bảng có tiêu đề lặp và hàng không tách trang, mỗi tài liệu tham khảo giữ cùng đoạn được kiểm tra tĩnh. Kiểm tra tĩnh không chứng minh số trang, khả năng đọc thực tế, hàng mồ côi hay không có trang trắng. Không có LibreOffice/soffice/pandoc hoặc renderer DOCX được cung cấp; `WORD_RENDER_VALIDATION: NOT_VERIFIED`. Gate 7 giữ PARTIAL cho phần bố cục chưa được nhìn trực tiếp.

## Phát hiện riêng về hình học và topology

M22/M23 dùng mô hình dây song song không có góc xoắn, nhưng không đủ thông tin trong hai bài để xác nhận độc lập toàn bộ chế tạo của mẫu Chen. Vỏ bảo vệ góp vào sức cản hiệu dụng. M24 có một tao61 dây và7tao×19dây, không phải các cấu hình1×19/7×7 trong ghi chú cũ. M25 có SMA1×27 và7×7; thép1×37 chỉ là bài toán đối chiếu số. Braid/sleeve được phân biệt theo hình học và điều kiện biên, không có số liệu chuyên biệt bị tạo ra.

## M22/M23 và tính độc lập của bằng chứng

M22 pp.5–7 và p.9 dùng Chen2015. M23 p.7 và tài liệu [38]/[57] p.15 nhận lại hiệu chỉnh M22 và cùng bộ Chen. `DEPENDENCE_IDENTIFIED: SHARED_CHEN_DATA_AND_CALIBRATION`; `EVIDENCE_INDEPENDENCE: NOT_ESTABLISHED`. Hai lời giải có đóng góp khác nhau nhưng không được đếm thành hai thí nghiệm lặp độc lập. Chưa đọc PDF Chen gốc, không bổ sung mô tả thiết bị ngoài thông tin hai bài.

## M23 C-04 — đơn vị chưa xác minh

Eq.(15), physical p.5: `UNVERIFIED_UNITS_EQUATION_TEXT_VERIFIED`. Giữ trạng thái này theo WEP08 mặc dù ghi chú phương trình cũ từng gán MPa. Không chép Eq.(15), không gán đơn vị k_i, không tính dự báo MP1 và không đồng nhất k_i với M22 k. Việc M23 tái sử dụng quan hệ hiệu chỉnh không giải quyết được kiểm tra thứ nguyên của mọi ký hiệu trong ma trận.

## Cận uốn, trượt và vòng trễ

M24 lấy độ dốc nhánh tăng tải/đầu nhánh dỡ tải từ vòng lực–chuyển vị, đơn vị kN/mm. Full slip gần mức thấp; partial stick gần mức cao; perfect stick đánh giá quá cao. Đây là ước lượng của mô hình tuyến tính, không phải cận bao chắc chắn cho mọi cấu trúc. M24 p.12 nêu chưa dự đoán toàn vòng trễ và tải kết hợp uốn–kéo. Số liệu phần trăm sai số Table6 có bất nhất số học (hàng R1 đầu), nên không được dùng để tuyên bố độ chính xác định lượng trong bản thảo.

M25 ghép SMA và tiếp xúc có ma sát nhưng PDF không nêu tên Coulomb/penalty, khác nhãn trong ghi chú đã chấp nhận. Bản thảo chỉ nói về hệ số ma sát được chỉ định và tiếp xúc pháp tuyến/tiếp tuyến; không đưa ra kết luận về luật tiếp xúc đã được nhận dạng.

## Quyết định về phương trình và hình

Không có phương trình cần thiết để thực hiện mục tiêu tổng hợp. Các biểu thức k, k_i và cận nguồn chưa được chọn cho MP1; ký hiệu E, EI, K chỉ dùng để phân biệt đại lượng. Không có phương trình nên không phát sinh yêu cầu OMML. Không sao chép hình nguồn. Sơ đồ tự vẽ có thể hữu ích ở bước biên tập sau, nhưng phải phân biệt tiết diện quy đổi với tiếp xúc thật và không quyết định topology MP1.

## Kết quả chấp nhận

GATE_1: PARTIAL  
GATE_2: PASS  
GATE_3: PASS (sai khác ghi chú đã đối chiếu và ghi nhận)  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS  
GATE_7: PARTIAL  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED

Giới hạn khoa học và kiểm tra bố cục được giữ độc lập. Không có quyết định về pha TiNi, topology, luật ma sát, mô hình cận MP1 hay tính mới.

## QA độc lập và kiểm tra sau hiệu chỉnh

Worker QA xác nhận mapping citation trong thứ tự Word gồm bảng, bốn DOI/author order, số bản ghi/thuật ngữ, định nghĩa glossary và không có ID nội bộ. Phát hiện bảng vượt vùng văn bản1–2twip do làm tròn đã được ROOT sửa: cả hai tblGrid/tblW/tcW hiện có tổng9298twip, đúng vùng văn bản A4 sau lề2,3cm. Văn bản, font và các giả thiết cơ học không đổi. Kiểm tra lại xác nhận body12pt, caption10pt, bảng8,5pt, TNR;32/32 hàng có cantSplit;2 đầu bảng lặp;4 reference keepLines. QA cấu trúc đạt sau hiệu chỉnh; bố cục trực quan vẫn NOT_VERIFIED.
