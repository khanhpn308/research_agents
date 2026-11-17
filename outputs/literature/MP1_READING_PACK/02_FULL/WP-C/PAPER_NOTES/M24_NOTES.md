# M24 — A new mechanical model of short wire ropes: Theory and experimental validation

- **Canonical PDF:** `data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf`
- **SHA-256:** `9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6`
- **Identity:** Barsi, Carboni, and Lacarbonara, 2025; Engineering Structures, Vol. 322, 119217; DOI: `10.1016/j.engstruct.2024.119217`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C1.2.1; C2.4; C2.4.2; C2.5; C2.5.5
- **Evidence records:** M24-E01; M24-E04; M24-E05; M24-E10

---

## A. Section objective

Mô hình cấu tạo giải tích liên tục cho dây cáp thép ngắn uốn thuần túy; xác định cận trên và cận dưới của độ cứng uốn dựa trên biến dạng riêng (eigenstrain) tương ứng với các trạng thái trượt tiếp xúc (stick, partial-stick, full-slip), được kiểm chứng qua thí nghiệm uốn tĩnh chu kỳ trên máy MTS 810 và số liệu kéo–xoắn trong y văn.

## B. Concept and terminology notes

Short wire rope; shear-deformable / Timoshenko beam; eigenstrain; perfect stick, partial stick, and full slip states; bending stiffness bounds; axial–torsional coupling; kinematic constraint.

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M24-E01 (p. 1, Abstract, NOT_APPLICABLE):** The paper presents a constitutive model for short steel wire ropes with upper/lower bending-stiffness bounds and experimental validation. Anchor: “The model aims to predict the lower and upper bounds of the bending stiffness”. Status: `VERIFIED_FULL_TEXT`.
- **M24-E04 (p. 4, Sec. 2.2, Eqs. (11), (18), (22)–(24)):** Wire strain measures contain an eigenstrain term; three kinematic states (perfect stick, partial stick, full slip) are used to represent relative sliding. Anchor: “perfect stick state, the partial stick state and the full slip state”. Status: `VERIFIED_FULL_TEXT`.
- **M24-E05 (p. 5, Sec. 3, Fig. 2–4; Table 1):** Two series of short steel ropes were tested in displacement-controlled pure bending at 0.2 Hz; cycles and lengths were varied. Anchor: “A quasi-static experimental campaign was performed”. Status: `VERIFIED_FULL_TEXT`.
- **M24-E10 (p. 10, Sec. 4.1–4.2, Figs. 9–11; Tables 3–6):** The full-slip state predicts minimum stiffness and the partial-stick state predicts maximum stiffness over the tested lengths; perfect-stick overestimates the maximum. Anchor: “full slip state and experimental confidence region”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Phương trình cân bằng dầm Timoshenko Eqs. (1)–(2); quan hệ biến dạng dầm/sợi và biến dạng riêng eigenstrain Eqs. (6)–(11); ma trận cấu tạo tiết diện Eq. (18); biểu thức xác định các cận độ cứng uốn Eqs. (22)–(24). Figs. 1–11; Tables 1–6.

## E. Experimental and quantitative findings

Cơ cấu thí nghiệm uốn thuần túy gắn trên máy MTS 810; mẫu cáp thép AISI 304 hai họ R1 (dây đơn 1x19, chiều dài 10–20 cm) và R2 (bó 7 tao 7x7, chiều dài 7.5–27.5 cm); gia tải kiểm soát chuyển vị ở tần số 0.2 Hz; độ cứng uốn được trích xuất từ chu kỳ thứ 7.

Trạng thái full-slip dự báo cận dưới độ cứng với sai số 1–37% so với thực nghiệm; trạng thái partial-stick dự báo cận trên với sai số 7.2–31.9% [M24-E10]. Trạng thái perfect-stick đánh giá quá cao độ cứng thực tế xấp xỉ một bậc độ lớn (~10 lần) [M24-E10].

## F. Cross-paper comparisons

- **So sánh với M22 (Zhang et al. 2018) và M23 (Zhang et al. 2021):**
  - M24 khảo sát cáp xoắn ngắn (short helical wire rope) sử dụng dầm Timoshenko có biến dạng trượt và đưa vào khái niệm biến dạng riêng (eigenstrain) để thiết lập các cận độ cứng uốn rời rạc (bounds).
  - Ngược lại, M22/M23 nghiên cứu bó dây thẳng song song (parallel wire cables) chuyển đổi sang dầm phân lớp giải tích với liên kết trượt đàn hồi tuyến tính $k$.
  - M24 chứng minh giả thiết perfect-stick làm sai lệch độ cứng nghiêm trọng, trong khi partial-stick mô tả đúng cận trên thực tế; M23 chỉ ra rằng bó cáp không có lực kéo dọc chuyển tiếp mượt mà dạng bilinear qua các mức $k$.
- **So sánh với M36 (Carboni & Lacarbonara 2016):**
  - Cùng đồng tác giả Carboni và Lacarbonara: M24 là mô hình cơ học tiếp xúc cấu tạo vi mô (constitutive bounds) cho uốn thuần túy, trong khi M36 dùng mô hình hiện tượng học Bouc–Wen để khớp vòng lặp trễ pinched hysteresis cho cáp uốn kết hợp NiTi–thép.
- **So sánh với M26/M27 (Reedlunn et al. 2013):**
  - M24 nghiên cứu cáp thép dưới tải uốn thuần túy; M26/M27 nghiên cứu cáp siêu đàn hồi NiTi dưới tải kéo dọc trục.

## G. Limitations and counterevidence

1. **Giả thiết cùng trạng thái trượt đồng thời [M24-E04]:** Mô hình cận trên và cận dưới giả định toàn bộ các sợi trong mặt cắt cùng ở một trạng thái động học (cùng full-slip hoặc cùng partial-stick), bỏ qua sự trượt cục bộ không đồng đều giữa các lớp dây.
2. **Không mô tả hình dạng vòng lặp trễ [M24-E10]:** Mô hình chỉ tính toán hai cận độ cứng uốn tuyến tính hóa (secant stiffness bounds), không dự báo diện tích tiêu tán năng lượng hay hình dạng vòng lặp lực–chuyển vị.
3. **Hiệu ứng kẹp mẫu cáp ngắn [M24-E05]:** Chiều dài mẫu thử rất ngắn (7.5–27.5 cm) khiến độ cứng đo được nhạy cảm với điều kiện kẹp ngàm và độ chặt của kẹp ở hai đầu.
4. **Phạm vi vật liệu thép đàn hồi tuyến tính [M24-E01]:** Chưa xét đến tính phi tuyến siêu đàn hồi hay hiện tượng chuyển pha của hợp kim nhớ hình.

## H. Relevance to MP1

- **Cơ sở cho việc xác định cận độ cứng uốn (C1.2.1, C2.4, C2.4.2, C2.5, C2.5.5):** Cung cấp khung lý thuyết dầm Timoshenko với biến dạng riêng eigenstrain để tính toán cận dưới (full-slip) và cận trên (partial-stick) cho bó dây chịu uốn.
- **Counterevidence quan trọng đối với giả thiết ngàm dính (Perfect stick):** Bằng chứng thực nghiệm định lượng trong M24-E10 chỉ ra rằng việc coi bó dây bị khóa hoàn toàn (perfect stick) sẽ dẫn đến đánh giá quá cao độ cứng uốn tới ~10 lần. Đây là cơ sở khoa học để MP1 xây dựng mô hình cận trên sát thực tế hơn cho bó dây TiNi khi bị ép bởi piston lò xo SMA.
- **Khác biệt cấu trúc:** M24 nghiên cứu cáp xoắn helical có ghép nối uốn–xoắn–kéo tự nhiên; MP1 nghiên cứu bó dây TiNi thẳng song song chịu nén ma sát chủ động từ bên ngoài.

## I. Reading route

1. **Sec. 1 & Sec. 2.1 (pp. 1–3):** Nắm bối cảnh cáp ngắn chịu uốn và hệ phương trình cân bằng dầm Timoshenko Eqs. (1)–(2).
2. **Sec. 2.2 (pp. 4–5):** Đọc kỹ định nghĩa biến dạng sợi và khái niệm biến dạng riêng eigenstrain biểu diễn các trạng thái trượt Eqs. (6)–(18).
3. **Sec. 2.4 (pp. 5):** Khảo sát các công thức giải tích xác định cận độ cứng uốn Eqs. (22)–(24).
4. **Sec. 3 (pp. 5–6, Figs. 2–4):** Xem cơ cấu gá uốn thuần túy trên máy MTS 810 và cách khử lực kéo dọc trục bằng bàn trượt ngang tự do.
5. **Sec. 4.1–4.2 (pp. 9–11, Figs. 9–11, Tables 3–6):** Đọc kỹ phần so sánh các cận mô hình với dải tin cậy thực nghiệm và bảng sai số định lượng.

## J. Questions for human writing

1. **Lựa chọn cận trên cho độ cứng uốn (C2.5.1, C2.5.5):** Khi thiết lập cận trên cho độ cứng uốn của bó dây TiNi dưới áp suất nén cực đại của piston SMA, nên dùng cận partial-stick (theo nguyên lý M24) hay cận no-slip dầm đồng nhất (như M23)?
2. **Ảnh hưởng của biến dạng trượt cắt (C2.5.2):** Với tỉ lệ đường kính trên chiều dài ($D/L$) của bó dây TiNi trong MP1, hiệu ứng biến dạng trượt cắt kiểu dầm Timoshenko (như M24 xem xét) có ý nghĩa đáng kể so với dầm Euler–Bernoulli không?
3. **Mô hình hóa trạng thái trượt cục bộ (C2.4.2):** Khái niệm biến dạng riêng eigenstrain trong M24 có thể được kết hợp với áp suất nén ngoài $p$ để mô tả sự chuyển tiếp trượt trong bó dây TiNi như thế nào?

## K. Unresolved evidence

1. M24 thực hiện trên cáp thép xoắn; chưa có số liệu kiểm chứng độc lập cho bó dây hợp kim nhớ hình TiNi thẳng.
2. Số trang in (`printed_page`) trong P0 là `NOT_REPORTED`; các định vị sử dụng số trang vật lý của file PDF 12 trang.
