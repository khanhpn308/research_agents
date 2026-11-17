# M35 — Cable Vibration Considering Internal Friction

- **Canonical PDF:** `data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf`
- **SHA-256:** `aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800`
- **Identity:** Xin Liu, 2004; Master of Science Thesis, University of Hawai'i at Manoa; DOI/identifier: `N/A — luận văn thạc sĩ`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C2.4; C2.4.2; C2.5; C2.5.3
- **Evidence records:** M35-E11; M35-E16; M35-E37; M35-E53

---

## A. Section objective

Luận văn Thạc sĩ phát triển mô hình dao động liên tục 1-D cho cáp xoắn nhiều lớp có xét đến độ cứng uốn phụ thuộc độ cong $EI(\kappa)$ do hiện tượng trượt ma sát khô Coulomb giữa các lớp dây; đo đạc áp suất tiếp xúc hướng tâm bằng thí nghiệm đẩy trượt (push-out test) và kiểm chứng mô hình với dữ liệu dao động cưỡng bức công bố trong y văn.

## B. Concept and terminology notes

Continuum cable; curvature-dependent flexural rigidity ($EI(\kappa)$); interlayer radial contact pressure ($p_{rad}$); static/kinetic dry friction; slip threshold; internal frictional damping; two-phase dynamic response (damped vs undamped).

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M35-E11 (p. 11, Introduction/summary, NOT_APPLICABLE):** The thesis develops a 1-D continuum vibration model with curvature-dependent EI and dry-friction slip between helical layers. Anchor: “relative wire slippage between adjacent helical layers causes large, nonlinear variations in flexural rigidity”. Status: `VERIFIED_FULL_TEXT`.
- **M35-E16 (p. 16, Theory, Eq./Fig. 3.x):** The model uses a curvature–flexural-rigidity relation with slip thresholds set by interlayer pressure/friction; kinetic friction is neglected. Anchor: “interlayer radial pressure governs the onset of wire slip”. Status: `VERIFIED_FULL_TEXT`.
- **M35-E37 (p. 37, Numerical results, Figs. 4.x–5.x; Newmark scheme):** Free vibration shows amplitude decay while curvature exceeds the slip threshold, then a low-amplitude regime with little additional friction loss; Newmark β=0.25, γ=0.5 is used. Anchor: “damped phase with decaying amplitude and an undamped phase”. Status: `VERIFIED_FULL_TEXT`.
- **M35-E53 (p. 53, Validation/experiments, Figs. 5.4–5.5; push-out test):** Measured interlayer pressures are approximately 0.475 N/mm² (layers 1–2) and 0.053 N/mm² (layers 2–3); modeled endpoint histories agree with cited forced-vibration data within about 10%, while loop area is smaller. Anchor: “within 10%”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Phương trình đạo hàm riêng chuyển động bậc 4 pp. 13–20; mô hình phần tử hữu hạn Hermite bậc 5 và tích phân Newmark pp. 22–29; Figs. 4.1–5.5; bảng kết quả thí nghiệm đẩy đo áp suất tiếp xúc pp. 58–66.

## E. Experimental and quantitative findings

Thí nghiệm đẩy trượt (push-out test) trên máy Instron 4206 (tải trọng 500 N, tốc độ 1 in/min) đo áp suất pháp tuyến giữa các lớp dây; mô phỏng cáp nhịp 1 m hai đầu tựa đơn giản và cáp công xôn 0.3 m; đối chiếu đáp ứng dao động với dữ liệu thực nghiệm đo đạc công bố.

Áp suất tiếp xúc đo được giữa lớp 1 và lớp 2 là ~0.475 N/mm², giữa lớp 2 và lớp 3 là ~0.053 N/mm² [M35-E53]. Biên độ dao động đầu mút mô phỏng khớp với dữ liệu thực nghiệm trong phạm vi sai số ~10% [M35-E53].

## F. Cross-paper comparisons

- **So sánh với M23 (Zhang et al. 2021) — Phân biệt bản chất tiếp xúc:**
  - *Luật tiếp xúc & Ngưỡng trượt:* M35 sử dụng luật ma sát khô Coulomb với **ngưỡng trượt tới hạn** xác định bởi lực pháp tuyến giữa các lớp ($\tau_{crit} = \mu_s p_{rad}$). Dây chỉ trượt khi độ cong vượt ngưỡng $\kappa > \kappa_{cr}$, tạo nên đáp ứng chuyển pha rõ rệt giữa dầm không trượt ($EI_{max}$) và dầm trượt một phần ($EI(\kappa)$). Ngược lại, M23 sử dụng luật trượt tuyến tính liên tục ($F = k \cdot \Delta u$) **không có ngưỡng kích hoạt** (không có Coulomb threshold); độ trượt xuất hiện ngay khi có lực cắt và độ cứng chuyển tiếp liên tục theo $k$.
  - *Cấu hình cơ học:* M35 khảo sát dao động động lực học của cáp xoắn helical (chịu áp suất hướng tâm do lực kéo xoắn), trong khi M23 giải bài toán uốn tĩnh 2-D của bó dây thẳng song song.
- **So sánh với M24 (Barsi et al. 2025):**
  - M35 xây dựng quan hệ $EI(\kappa)$ biến thiên liên tục trên cơ sở áp suất tiếp xúc đo bằng thực nghiệm push-out; M24 thiết lập hai cận cứng rời rạc (partial-stick và full-slip) thông qua biến dạng riêng eigenstrain.
- **So sánh với M36 (Carboni & Lacarbonara 2016):**
  - M35 dùng mô hình giải tích tiếp xúc vi mô (micro-mechanical contact pressure) để giải thích sự tiêu tán dao động do trượt giữa các lớp; M36 dùng mô hình vĩ mô hiện tượng học (phenomenological Bouc–Wen) để mô tả vòng lặp trễ pinched hysteresis của cáp kết hợp dây NiTi và thép.

## G. Limitations and counterevidence

1. **Giả thiết bỏ qua ma sát động [M35-E16]:** Mô hình chỉ dùng hệ số ma sát tĩnh $\mu_s \approx 0.74$, bỏ qua ma sát động $\mu_k \approx 0.57$, dẫn đến đánh giá thấp diện tích vòng lặp năng lượng tiêu tán thực tế.
2. **Xấp xỉ diện tích tiếp xúc [M35-E53]:** Áp suất pháp tuyến được nội suy từ thí nghiệm đẩy trượt push-out phá hủy, giả định diện tích tiếp xúc trụ đồng nhất, bỏ qua tiếp xúc thực tế dạng đường/điểm giữa các sợi dây xoắn.
3. **Phạm vi biến dạng nhỏ [M35-E11]:** Bỏ qua ghép nối uốn–xoắn–kéo dọc trục và hiệu ứng hình học phi tuyến góc quay lớn.
4. **Phụ thuộc phần mềm thương mại:** Hàm độ cứng uốn $EI(\kappa)$ sử dụng dữ liệu đầu vào tính toán từ phần mềm chuyên dụng CableCAD chứ không xuất phát hoàn toàn từ nghiệm giải tích đóng.

## H. Relevance to MP1

- **Cơ sở tiền đề cho cơ chế điều khiển độ cứng (C2.4, C2.4.2, C2.5, C2.5.3):** M35 là một bằng chứng nghiên cứu trực tiếp chứng minh rằng áp suất pháp tuyến tại mặt tiếp xúc ($p_{rad}$) quyết định ngưỡng bắt đầu trượt ma sát giữa các sợi dây, từ đó điều khiển sự thay đổi độ cứng uốn hiệu dụng $EI$.
- **Khác biệt quan trọng với MP1:** Trong M35, áp suất tiếp xúc là hằng số thụ động sinh ra từ lực căng xoắn của cáp helical; trong khi ở MP1, áp suất tiếp xúc là biến điều khiển chủ động sinh ra từ piston dẫn động bằng lò xo SMA tác dụng lên bó dây TiNi thẳng.
- **Ý nghĩa đối với mô hình hóa:** Cung cấp tiền lệ về phương trình dầm có $EI$ phụ thuộc độ cong và áp suất tiếp xúc để tham khảo xây dựng mô hình cơ học trong Chương 2.

## I. Reading route

1. **Chapter 1 (pp. 1–4):** Đọc phần tổng quan và phát biểu bài toán để hiểu nguồn gốc sự suy giảm độ cứng uốn phi tuyến do trượt giữa các lớp dây xoắn.
2. **Chapter 2 (pp. 5–9):** Nắm các giả thiết cơ bản và phương trình chuyển động vi phân bậc 4 của cáp có xét ma sát trong.
3. **Chapter 3 (pp. 10–19, Figs. 3.1–3.4):** Đọc kỹ phần dẫn xuất mô hình uốn ma sát (Sec. 3.2), khái niệm áp suất tiếp xúc hướng tâm và quan hệ $EI(\kappa)$.
4. **Chapter 4 & 5 (pp. 37–55, Figs. 4.1–5.5):** Xem kết quả mô phỏng tích phân Newmark mô tả hai pha dao động (có dập tắt ma sát và không dập tắt), phương pháp thí nghiệm đẩy trượt push-out đo áp suất và đối chiếu với thực nghiệm dao động cưỡng bức.

## J. Questions for human writing

1. **Xây dựng quan hệ trượt phụ thuộc áp suất (C2.4.2, C2.5.3):** Trong M35, áp suất $p_{rad}$ được xác định từ cấu trúc xoắn của cáp; trong MP1, quan hệ $p_{contact}(p_{piston})$ giữa áp suất buồng khí piston và áp suất nén lên bó dây TiNi được thiết lập như thế nào để đưa vào điều kiện ngưỡng trượt Coulomb?
2. **Hiện tượng suy giảm độ cứng hai pha (C2.5.3):** Dưới tác dụng của tải trọng uốn, bó dây TiNi của MP1 có xuất hiện ngưỡng chuyển tiếp độ cong rõ rệt như $\kappa_{cr}$ trong M35 trước khi trượt ma sát diễn ra hay không?
3. **Mô hình hóa tiêu tán năng lượng (C2.4, C2.5):** Khi mô tả dao động hoặc uốn chu kỳ của bó dây TiNi trong Chương 2, việc sử dụng luật trượt ma sát Coulomb với áp suất điều khiển (kiểu M35) có ưu thế gì so với mô hình trượt tuyến tính (kiểu M23)?

## K. Unresolved evidence

1. Bản số hóa PDF của luận văn có một số hạn chế về hiển thị ký tự toán học ở các trang lý thuyết; các công thức trích dẫn trực tiếp vào luận văn cần được đối chiếu thị giác cẩn trọng.
2. Áp suất pháp tuyến trong M35 thu được từ thí nghiệm push-out trên mẫu cáp thép xoắn; không thể áp dụng trực tiếp giá trị này cho bó dây TiNi thẳng của MP1.
