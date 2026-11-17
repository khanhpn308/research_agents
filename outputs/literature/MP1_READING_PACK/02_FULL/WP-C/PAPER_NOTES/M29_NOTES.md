# M29 — Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables

- **Canonical PDF:** `data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf`
- **SHA-256:** `56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61`
- **Identity:** Kang, Wang, Zhou, and Xue, 2020; Journal of Mechanical Engineering (机械工程学报), Vol. 56, No. 14, pp. 65–72; DOI: `10.3901/JME.2020.14.065`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C2.4; C2.4.1; C2.4.2; C2.5.5
- **Evidence records:** M29-E01; M29-E03; M29-E04; M29-E06

---

## A. Section objective

Bài báo song ngữ Trung–Anh dẫn xuất thuật toán phần tử hữu hạn số gia (incremental FEM) cho cáp hợp kim nhớ hình siêu đàn hồi 7×7 trong Abaqus/UMAT; khảo sát ảnh hưởng của bước xoắn (pitch) và vùng tập trung ứng suất tiếp xúc giữa các tao dây.

## B. Concept and terminology notes

Incremental SMA constitutive law; shape-memory factor; UMAT subroutine; 7×7 superelastic cable; frictionless smooth contact; outer strand pitch; forward/reverse martensitic transformation; stress concentration.

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M29-E01 (p. 1, Abstract, NOT_APPLICABLE):** The Chinese/English abstract states that coupled material/contact nonlinearities motivate an incremental SMA constitutive FE method in ABAQUS. Anchor: “很难建立描述形状记忆合金(Shape memory alloy，SMA)超弹性缆索力学行为的理论模型”. Status: `VERIFIED_FULL_TEXT`.
- **M29-E03 (p. 3, Constitutive formulation, Eqs. (1)–(12)):** The incremental strain decomposition and shape-memory-factor constitutive update are implemented as a UMAT with phase-dependent elastic modulus. Anchor: “dεij = dεijtr + dεijth + dεije”. Status: `VERIFIED_FULL_TEXT`.
- **M29-E04 (p. 4, Validation, Figs. 3–8; Tables 1–2):** For simplified cross-sections, simulated core-strand start/finish stresses are about 486.5/518.9 MPa (configuration a) and 493.7/526.1 MPa (b), within roughly 1.5–4.1% for forward-start/finish comparisons; reverse values show larger errors. Anchor: “martensitic transformation start and finish stresses”. Status: `VERIFIED_FULL_TEXT`.
- **M29-E06 (p. 6, Parametric analysis, Figs. 11–13):** Contact regions between core and outer strands concentrate stress; increasing outer pitch from 40 to 50/60 mm lowers nominal stress, transformation stresses and initial moduli. Anchor: “frictionless smooth contact was assumed”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Phương trình phân rã ten-sơ biến dạng số gia và cập nhật ứng suất Eqs. (1)–(12); Figs. 1–2 (hình học mặt cắt 7×7 và lưới phần tử); Figs. 3–8 và Tables 1–2 (so sánh ngưỡng chuyển pha với số liệu thực nghiệm y văn); Figs. 11–13 (phân bố ứng suất tiếp xúc và quét tham số bước xoắn 40, 50, 60 mm).

## E. Experimental and quantitative findings

Không có thí nghiệm vật lý mới; mô hình số 3-D cáp 7×7 gồm 49 sợi (đường kính sợi 0.885 mm, chiều dài cáp 20 mm) ở 25 °C được kiểm chứng đối chiếu với dữ liệu kéo đơn trục của Mas et al.; các đầu cáp gắn đồ gá cứng hình trụ.

Mô phỏng tao lõi tái hiện các ngưỡng ứng suất chuyển pha thuận (start/finish) với sai số 1.5–4.1% so với thực nghiệm, nhưng sai số lớn hơn ở giai đoạn chuyển pha nghịch kết thúc [M29-E04]. Khi tăng bước xoắn tao ngoài từ 40 mm lên 50 mm và 60 mm, ứng suất danh nghĩa tổng thể, ứng suất khởi đầu chuyển pha và mô đun đàn hồi ban đầu đều suy giảm [M29-E06].

## F. Cross-paper comparisons

- **So sánh với M25 (Vahidi et al. 2021) và M28 (Narjabadifam et al. 2024):**
  - Cả ba bài báo cùng xây dựng mô hình số 3-D trong Abaqus cho cáp xoắn 7×7 SMA. Điểm khác biệt cốt lõi là M29 giả định **tiếp xúc trơn không ma sát (frictionless smooth contact)**, trong khi M25 và M28 đưa vào ma sát Coulomb tiếp tuyến ($\mu = 0.1–0.5$). Việc đối chiếu chứng minh rằng giả thiết không ma sát của M29 làm đánh giá thấp đáng kể khả năng chịu tải và triệt tiêu thành phần tiêu tán năng lượng do ma sát giữa các sợi.
- **So sánh với M23 (Zhang et al. 2021):**
  - M29 giải quyết phi tuyến vật liệu chuyển pha SMA bằng thuật toán số gia UMAT trong khi bỏ qua ma sát tiếp xúc; M23 giải quyết ma sát trượt tiếp xúc giữa các sợi bằng phương pháp giải tích không gian trạng thái trong khi giả định vật liệu đàn hồi tuyến tính đơn giản.
- **So sánh với M26/M27 (Reedlunn et al. 2013):**
  - M29 mô phỏng số cấu hình cáp 7×7 dựa trên các giả thiết hình học lý tưởng; M27 chứng minh bằng thực nghiệm rằng tương tác tiếp xúc thực tế giữa các sợi tạo ra biến dạng dập lõm và ảnh hưởng mạnh đến quá trình chuyển pha.

## G. Limitations and counterevidence

1. **Giả thiết tiếp xúc trơn không ma sát [M29-E06]:** Tác giả nêu rõ: "frictionless smooth contact was assumed". Đây là counterevidence quan trọng đối với việc đơn giản hóa bài toán tiếp xúc; việc bỏ qua ma sát không thể mô tả được sự truyền lực cắt tiếp tuyến và hiện tượng tiêu tán năng lượng do trượt.
2. **Sai số giai đoạn chuyển pha nghịch [M29-E04]:** Mô hình dự báo kém chính xác hơn ở pha dỡ tải (reverse transformation finish), phản ánh giới hạn của luật cấu tạo số gia khi dỡ tải phi tuyến.
3. **Mặt cắt hình học đơn giản hóa:** Mô hình giả định các sợi tròn tiếp xúc hình học lý tưởng, chưa xét đến biến dạng méo hình học trong quá trình bện cáp.
4. **Chiều dài mẫu mô phỏng rất ngắn (20 mm):** Do hạn chế tài nguyên tính toán, mô hình chỉ mô phỏng đoạn ngắn 20 mm, chịu ảnh hưởng lớn từ điều kiện biên ngàm cứng ở hai đầu.

## H. Relevance to MP1

- **Công thức cấu tạo số gia UMAT cho TiNi (C2.4, C2.4.1, C2.4.2, C2.5.5):** Cung cấp hệ phương trình cấu tạo số gia chi tiết Eqs. (1)–(12) mô tả chuyển pha thuận và nghịch của vật liệu NiTi siêu đàn hồi, là tài liệu tham khảo giá trị nếu MP1 xây dựng chương trình tính toán số cho sợi TiNi.
- **Counterevidence chống lại giả thiết bỏ qua ma sát:** Bằng chứng trong M29-E06 cho thấy nếu bỏ qua ma sát tiếp xúc, mô hình không thể phản ánh đúng sự thay đổi độ cứng của hệ đa sợi. Điều này khẳng định ma sát tiếp xúc điều khiển bởi áp suất dương trong MP1 là yếu tố quyết định và không thể bỏ qua trong mô hình hóa.
- **Vùng tập trung ứng suất tiếp xúc:** Chỉ ra rằng các điểm tiếp xúc giữa các sợi là nguồn tập trung ứng suất cục bộ, có thể thúc đẩy chuyển pha martensite sớm hơn tại bề mặt tiếp xúc so với lõi sợi.

## I. Reading route

1. **Sec. 1 (pp. 1–3):** Đọc kỹ thuật toán cấu tạo số gia của hợp kim nhớ hình, định nghĩa biến dạng chuyển pha và quy tắc cập nhật ứng suất Eqs. (1)–(12).
2. **Sec. 2 (pp. 3–5, Figs. 1–8, Tables 1–2):** Khảo sát cấu trúc hình học 7×7, phân tích kết quả mô phỏng tao lõi và bảng sai số so với thực nghiệm Mas et al.
3. **Sec. 3 (pp. 5–7, Figs. 11–13):** Xem phân tích phân bố ứng suất tiếp xúc giữa các tao dây và đồ thị khảo sát ảnh hưởng của bước xoắn (pitch sweep).
4. **Sec. 4 (pp. 7–8):** Đọc phần kết luận để nắm rõ các nhận định về tập trung ứng suất tiếp xúc và giới hạn của mô hình không ma sát.

## J. Questions for human writing

1. **Tích hợp quan hệ cấu tạo TiNi vào mô hình dầm (C2.4.1, C2.5):** Phương trình cấu tạo số gia của M29 có thể được giản lược thành quan hệ mô đun hiệu dụng $E(\epsilon)$ để đưa vào phương trình vi phân uốn dầm trong Chương 2 hay không?
2. **Vai trò của ma sát tiếp xúc (C2.4.2):** Kết quả của M29 cho thấy việc bỏ qua ma sát tiếp xúc làm sai lệch độ cứng cáp; trong MP1, việc đưa thêm áp suất nén chủ động từ piston sẽ làm tăng vai trò của lực cắt tiếp xúc lên mức độ nào so với trường hợp M29?
3. **Hiện tượng tập trung ứng suất tại điểm tiếp xúc (C2.4.1):** Ứng suất tiếp xúc cục bộ giữa các sợi TiNi tròn dưới áp suất piston có làm xuất hiện các dải martensite cục bộ tại bề mặt tiếp xúc trước khi toàn bộ tiết diện sợi bị biến dạng uốn không?

## K. Unresolved evidence

1. Các phương trình cấu tạo trong văn bản tiếng Trung cần được đối chiếu kiểm tra cẩn thận trước khi trích dẫn ký hiệu toán học vào luận văn.
2. Số trang in (`printed_page`) trong P0 là `NOT_REPORTED`; các định vị sử dụng số trang vật lý của file PDF 8 trang.
