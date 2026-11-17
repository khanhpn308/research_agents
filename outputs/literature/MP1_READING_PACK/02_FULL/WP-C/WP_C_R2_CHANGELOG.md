# WP-C R2 CHANGELOG — NOTES CONSISTENCY & SCIENTIFIC CORRECTION

TASK_ID: MP1-LR-P2-WP-C-R2  
ACTION: TARGETED_NOTES_CLEANUP  
DATE: 2026-10-15  

---

### Change 1: M23_NOTES.md — Scientific Correction of Slip Model Comparison with M35
- **Paper ID:** M23
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md`
- **Section:** F. Cross-paper comparisons
- **Before:**
  ```markdown
  | M35 (Liu thesis) | M35 dùng curvature-dependent EI cho cáp helical dao động; M23 giải tĩnh cho bó song song — cả hai đều dùng threshold slip nhưng cơ chế khác |
  ```
- **After:**
  ```markdown
  | M35 (Xin Liu 2004) | M35 mô hình hóa dao động cáp xoắn với luật ma sát khô Coulomb có ngưỡng kích hoạt trượt phụ thuộc áp suất pháp tuyến giữa các lớp (τ_crit = μ_s * p_rad), dẫn đến độ cứng uốn phi tuyến phụ thuộc độ cong (EI(κ)) và phản ứng hai pha dao động. Ngược lại, M23 áp dụng cho uốn tĩnh của bó dây song song với luật trượt giao diện tuyến tính liên tục (F = k * Δu) không có ngưỡng kích hoạt (không có Coulomb threshold); trượt xuất hiện liên tục tỉ lệ với lực cắt, và độ cứng chuyển tiếp liên tục theo thông số slip rigidity k. |
  ```
- **Reason:** Sửa nhận định khoa học sai. M23 dùng liên kết trượt tuyến tính thuần túy (linear slip rigidity $k$ [MPa]), không có ngưỡng trượt Coulomb ($\tau_{crit} = \mu \sigma_n$). M35 mới là mô hình có ngưỡng ma sát Coulomb theo áp suất hướng tâm $p_{rad}$.
- **Supporting Evidence ID / PDF locator:** M23-E06 (PDF p. 2, Sec. 2.1), M23-E04 (PDF p. 5, Eq. 15); M35-E16 (PDF p. 16, Eq./Fig. 3.x).
- **Change category:** `SCIENTIFIC_CONSISTENCY`

---

### Change 2: M23_NOTES.md — Source Role Clarification
- **Paper ID:** M23
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md`
- **Section:** H. Relevance to MP1
- **Before:**
  ```markdown
  **Vai trò chính:** COUNTEREVIDENCE cho mô hình hóa bó dây TiNi.
  ```
- **After:**
  ```markdown
  **Phân loại vai trò nguồn (Source Role Clarification):**
  - **REFERENCE_MODEL:** M23 cung cấp khung giải tích tham chiếu chuẩn mực cho độ cứng uốn và hai cận độ cứng (EI_min full-slip đến EI_max no-slip) của bó dây song song thông qua chuyển đổi dầm phân lớp và phương pháp không gian trạng thái (state space method). Cấu trúc bó dây song song trong M23 có sự tương đồng hình học cao nhất với bó dây TiNi thẳng trong MP1.
  - **SUPPORTING_EVIDENCE:** Bằng chứng giải tích và thực nghiệm cho thấy sự tồn tại của quy luật phân bố slip dạng hàm mũ (Eq. 28) và sự chuyển tiếp độ cứng uốn tương đương (EBSC γ) theo khả năng chống trượt giữa các dây (Fig. 13).
  - **COUNTEREVIDENCE (phản biện các giả thiết đơn giản hóa):**
    1. Phản bác giả thiết dầm đồng nhất: M23 chứng minh trực tiếp rằng giả thiết tiết diện phẳng của lý thuyết dầm cổ điển chỉ đúng trên từng lớp dây riêng lẻ chứ không đúng trên toàn bộ tiết diện bó dây [M23-E08, M23-E10].
    2. Phản bác giả thiết độ cứng không đổi: M23 chứng minh bó dây không chịu kéo dọc có quan hệ lực–độ võng dạng bilinear rõ rệt [M23-E05], trong đó độ cứng không cố định ở EI_max hay EI_min.
  - **LIMITATION (ranh giới chuyển giao sang MP1):**
    - M23 dùng dây thép đàn hồi tuyến tính, trong khi MP1 dùng dây hợp kim nhớ hình TiNi siêu đàn hồi có chuyển pha austenite <-> martensite.
    - M23 dùng luật trượt tuyến tính với k là tham số tự do, trong khi MP1 điều khiển ma sát tiếp xúc thông qua áp suất dương thực tế sinh ra từ piston dẫn động bằng lò xo SMA.
  - **AGENT_INFERENCE:** Để áp dụng cho MP1, cần kết hợp khung không gian trạng thái của M23 với quan hệ tiếp xúc ma sát phụ thuộc áp suất piston k(p) hoặc ngưỡng Coulomb τ_crit(p) = μ * σ_n(p), đồng thời tích hợp mô đun đàn hồi hiệu dụng phụ thuộc biến dạng của TiNi.
  ```
- **Reason:** Khắc phục việc gắn nhãn đơn chiều M23 là "COUNTEREVIDENCE". Phân biệt rành mạch 5 bình diện: Reference Model, Supporting Evidence, Counterevidence, Limitation và Agent Inference theo chuẩn P2.
- **Supporting Evidence ID / PDF locator:** M23-E01, M23-E05, M23-E06, M23-E07, M23-E08, M23-E09, M23-E10 (PDF pp. 1, 2, 7, 8, 9, 12, 13).
- **Change category:** `SOURCE_ROLE_CLARIFICATION`

---

### Change 3: M35_NOTES.md — Bibliographic Metadata Correction
- **Paper ID:** M35
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md`
- **Section:** Header metadata (Identity)
- **Before:**
  ```markdown
  - **Identity:** `X. Liu, None; DOI/identifier: `N/A — luận văn thạc sĩ`
  ```
- **After:**
  ```markdown
  - **Identity:** Xin Liu, 2004; Master of Science Thesis, University of Hawai'i at Manoa; DOI/identifier: `N/A — luận văn thạc sĩ`
  ```
- **Reason:** Loại bỏ chuỗi "None" phát sinh do lỗi format rỗng trong template cũ; điền đầy đủ tên tác giả đã xác minh (Xin Liu), năm hoàn thành luận văn (August 2004) và cơ sở đào tạo (University of Hawai'i at Manoa) trực tiếp từ trang bìa PDF.
- **Supporting Evidence ID / PDF locator:** M35 canonical PDF trang 1–3 (Title page: "A Thesis Submitted to the Graduate Division of the University of Hawai'i ... August 2004 By Xin Liu").
- **Change category:** `METADATA_CORRECTION`

---

### Change 4: M35_NOTES.md — Removal of Obsolete M23 Blocked Status & Scientific Expansion
- **Paper ID:** M35
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md`
- **Section:** F. Cross-paper comparisons, H. Relevance, I. Reading route, J. Questions
- **Before:**
  ```markdown
  ## F. Cross-paper comparisons
  This paper should be compared with M22/Pilot and M26/Pilot only on the shared observable and architecture stated in the records. M23 remains blocked. The main comparison axes are contact topology, helix/layer architecture, slip state, constitutive model level, validation independence, and measured quantity.
  [Kèm các câu hỏi và reading route dạng template chung chung]
  ```
- **After:**
  ```markdown
  ## F. Cross-paper comparisons
  - So sánh với M23 (Zhang et al. 2021) — Phân biệt bản chất tiếp xúc:
    + Luật tiếp xúc & Ngưỡng trượt: M35 sử dụng luật ma sát khô Coulomb với ngưỡng trượt tới hạn xác định bởi lực pháp tuyến giữa các lớp (τ_crit = μ_s * p_rad). Dây chỉ trượt khi độ cong vượt ngưỡng κ > κ_cr, tạo nên đáp ứng chuyển pha rõ rệt giữa dầm không trượt (EI_max) và dầm trượt một phần (EI(κ)). Ngược lại, M23 sử dụng luật trượt tuyến tính liên tục (F = k * Δu) không có ngưỡng kích hoạt; trượt xuất hiện liên tục tỉ lệ với lực cắt, và độ cứng chuyển tiếp liên tục theo k.
    + Cấu hình cơ học: M35 khảo sát dao động động lực học của cáp xoắn helical (áp suất hướng tâm do lực kéo xoắn), trong khi M23 giải bài toán uốn tĩnh 2-D của bó dây thẳng song song.
  - So sánh với M24 (Barsi et al. 2025): M35 dùng hàm EI(κ) liên tục từ áp suất push-out; M24 dùng cận rời rạc eigenstrain.
  - So sánh với M36 (Carboni & Lacarbonara 2016): M35 giải thích tiêu tán bằng tiếp xúc vi mô; M36 dùng mô hình hiện tượng học vĩ mô Bouc–Wen.
  [Kèm reading route và câu hỏi luận văn cụ thể định hướng cho Chương 1–2]
  ```
- **Reason:** Xóa bỏ tuyên bố lỗi thời "M23 remains blocked"; phân biệt chi tiết cơ chế tiếp xúc giữa M35 và M23; loại bỏ nội dung template chung chung và bổ sung lộ trình đọc cùng câu hỏi nghiên cứu cụ thể.
- **Supporting Evidence ID / PDF locator:** M35-E11, M35-E16, M35-E37, M35-E53 (PDF pp. 11, 16, 37, 53); M23-E04, M23-E06 (PDF pp. 2, 5).
- **Change category:** `OBSOLETE_STATUS`, `SCIENTIFIC_CONSISTENCY`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 5: M36_NOTES.md — Bibliographic DOI Correction & Expansion
- **Paper ID:** M36
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md`
- **Section:** Header metadata (Identity), F, H, I, J
- **Before:**
  ```markdown
  - **Identity:** `Carboni and Lacarbonara, 2016; DOI/identifier: `10.1061/(ASCE`
  ## F. Cross-paper comparisons
  This paper should be compared with M22/Pilot and M26/Pilot only on the shared observable and architecture stated in the records. M23 remains blocked. The main comparison axes are contact topology, helix/layer architecture, slip state, constitutive model level, validation independence, and measured quantity.
  ```
- **After:**
  ```markdown
  - **Identity:** Biagio Carboni and Walter Lacarbonara, 2016; Journal of Engineering Mechanics, Vol. 142, No. 5, 04016016; DOI: `10.1061/(ASCE)EM.1943-7889.0001072`
  ## F. Cross-paper comparisons
  - So sánh với M24 (Barsi, Carboni, Lacarbonara 2025): Cùng nhóm tác giả. M24 đi sâu vào cấu tạo vi mô (constitutive bounds) cho uốn thuần túy; M36 dùng mô hình hiện tượng học Bouc–Wen mô tả pinched hysteresis cho giảm chấn công trình.
  - So sánh với M28 (Narjabadifam et al. 2024): M36 làm thử nghiệm vật lý thực tế trên bàn rung cho TMD cáp NiTi–thép; M28 mô phỏng số cáp NiTi.
  - So sánh với M23 (Zhang et al. 2021): M23 giải uốn tĩnh không trễ bằng liên kết tuyến tính; M36 khảo sát uốn chu kỳ biên độ lớn với pinched hysteresis do kết hợp siêu đàn hồi NiTi và ma sát.
  [Kèm reading route và câu hỏi luận văn cụ thể]
  ```
- **Reason:** Khôi phục DOI đầy đủ bị cắt cụt do lỗi regex cũ; bổ sung tên tạp chí, tập, số; xóa "M23 remains blocked"; thay thế template bằng so sánh chi tiết giữa các bài báo cùng tác giả hoặc cùng chủ đề.
- **Supporting Evidence ID / PDF locator:** M36 canonical PDF trang 1 (DOI in dưới Abstract: "DOI: 10.1061/(ASCE)EM.1943-7889.0001072"); M36-E01, M36-E04, M36-E10, M36-E19 (PDF pp. 1, 4, 10, 19).
- **Change category:** `METADATA_CORRECTION`, `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 6: M24_NOTES.md — Remove Obsolete M23 Status & Template Cleanup
- **Paper ID:** M24
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md`
- **Section:** F. Cross-paper comparisons, H, I, J
- **Before:**
  Chứa câu "M23 remains blocked" và đoạn template "This paper should be compared with M22/Pilot and M26/Pilot only...".
- **After:**
  So sánh đối chiếu trực tiếp với M22/M23 (dầm Timoshenko eigenstrain bounds cho cáp xoắn vs dầm phân lớp plane stress cho bó song song; cảnh báo perfect-stick đánh giá quá cao độ cứng x10 lần), so sánh với M36 (mô hình vi mô vs hiện tượng học) và M26/M27 (uốn thép vs kéo SMA). Lộ trình đọc chỉ rõ Sec. 2.1–2.2 (pp. 3–5), Sec. 2.4 (p. 5), Sec. 3 (pp. 5–6), Sec. 4.1–4.2 (pp. 9–11).
- **Reason:** Xóa bỏ trạng thái lỗi thời của M23; loại bỏ template rỗng; gắn kết chặt chẽ với phát hiện thực nghiệm M24-E10 (perfect stick overestimates stiffness by order of magnitude).
- **Supporting Evidence ID / PDF locator:** M24-E01, M24-E04, M24-E05, M24-E10 (PDF pp. 1, 4, 5, 10).
- **Change category:** `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 7: M25_NOTES.md — Remove Obsolete M23 Status & Template Cleanup
- **Paper ID:** M25
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md`
- **Section:** F. Cross-paper comparisons, H, I, J
- **Before:**
  Chứa câu "M23 remains blocked" và đoạn template so sánh chung chung.
- **After:**
  So sánh đối chiếu chi tiết với M26/M27 (dùng dữ liệu thực nghiệm Reedlunn để làm benchmark mô phỏng Abaqus FE; giải thích nguồn gốc sai số 20–25%), so sánh với M29 (ma sát Coulomb vs giả thiết không ma sát), so sánh với M23 (áp suất do lực kéo xoắn vs bó song song). Lộ trình đọc dẫn đến Sec. 2.1–2.2 (pp. 3–4), Sec. 3 (pp. 4–6), Sec. 4 (pp. 6–9), Sec. 5 (pp. 10–12).
- **Reason:** Xóa bỏ trạng thái lỗi thời của M23; thay template bằng phân tích tương tác giữa ma sát và chuyển pha siêu đàn hồi dựa trên bằng chứng M25-E02, M25-E04, M25-E06, M25-E11.
- **Supporting Evidence ID / PDF locator:** M25-E02, M25-E04, M25-E06, M25-E11 (PDF pp. 3, 4, 6, 11).
- **Change category:** `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 8: M27_NOTES.md — Remove Obsolete M23 Status & Template Cleanup
- **Paper ID:** M27
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md`
- **Section:** F. Cross-paper comparisons, H, I, J
- **Before:**
  Chứa câu "M23 remains blocked" và đoạn template so sánh chung chung.
- **After:**
  So sánh đối chiếu sâu với M26 (phân tích vĩ mô vs giải phẫu phân cấp subcomponents), so sánh với M23 (tao 7x7 góc xoắn nhỏ hành xử tương tự bó song song; cảnh báo về vết dập lõm chế tạo và suy giảm mô đun trong cáp nhiều lớp), so sánh với M25/M29. Lộ trình đọc dẫn đến Sec. 2 (pp. 3–5), Sec. 3 (pp. 5–8), Sec. 4 (pp. 8–13), Sec. 4.3 (pp. 14–17), Sec. 5 (pp. 17–24).
- **Reason:** Xóa bỏ trạng thái lỗi thời của M23; loại bỏ template; làm nổi bật bằng chứng thực nghiệm về chuyển pha tuần tự theo lớp và ưu điểm của bó song song thẳng trong MP1.
- **Supporting Evidence ID / PDF locator:** M27-E02, M27-E08, M27-E13, M27-E24, M27-E16 (PDF pp. 2, 8, 13, 24, 16).
- **Change category:** `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 9: M28_NOTES.md — Remove Obsolete M23 Status & Template Cleanup
- **Paper ID:** M28
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md`
- **Section:** F. Cross-paper comparisons, H, I, J
- **Before:**
  Chứa câu "M23 remains blocked" và đoạn template so sánh chung chung.
- **After:**
  So sánh đối chiếu với M25/M29 (tiếp xúc phạt penalty friction μ=0.5 vs không ma sát), so sánh với M36 (thực nghiệm bàn rung TMD thực tế vs mô phỏng số địa chấn thuần túy), so sánh với M23 (mô hình 3D Abaqus tốn kém vs giải tích dầm phân lớp nhanh gọn). Lộ trình đọc chỉ rõ Sec. 2.1–2.2 (pp. 3–8), Sec. 2.3–2.4 (pp. 8–13), Sec. 3.1 (pp. 13–15), Sec. 3.2 (pp. 15–18).
- **Reason:** Xóa bỏ trạng thái lỗi thời của M23; loại bỏ template; cung cấp thông số tham khảo μ=0.5 cho mô hình tiếp xúc penalty và phân tích quy mô lực theo số sợi.
- **Supporting Evidence ID / PDF locator:** M28-E01, M28-E10, M28-E15, M28-E16 (PDF pp. 1, 10, 15, 16).
- **Change category:** `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 10: M29_NOTES.md — Remove Obsolete M23 Status & Template Cleanup
- **Paper ID:** M29
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md`
- **Section:** F. Cross-paper comparisons, H, I, J
- **Before:**
  Chứa câu "M23 remains blocked" và đoạn template so sánh chung chung.
- **After:**
  So sánh đối chiếu với M25/M28 (chỉ rõ hậu quả đánh giá thấp độ cứng khi giả định không ma sát), so sánh với M23 (thuật toán số gia UMAT cho SMA vs giải tích trượt tiếp xúc cho thép), so sánh với M27. Lộ trình đọc dẫn đến Sec. 1 (pp. 1–3), Sec. 2 (pp. 3–5), Sec. 3 (pp. 5–7), Sec. 4 (pp. 7–8).
- **Reason:** Xóa bỏ trạng thái lỗi thời của M23; loại bỏ template; nhấn mạnh phản biện khoa học (counterevidence) đối với giả thiết tiếp xúc trơn không ma sát và ý nghĩa đối với ma sát điều khiển áp suất trong MP1.
- **Supporting Evidence ID / PDF locator:** M29-E01, M29-E03, M29-E04, M29-E06 (PDF pp. 1, 3, 4, 6).
- **Change category:** `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 11: M30_NOTES.md — Remove Obsolete M23 Status & Template Cleanup
- **Paper ID:** M30
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md`
- **Section:** F. Cross-paper comparisons, H, I, J
- **Before:**
  Chứa câu "M23 remains blocked" và đoạn template so sánh chung chung.
- **After:**
  So sánh đối chiếu với M26/M27 (dao động kéo điều hòa vi mô DMA vs kéo tĩnh biến dạng lớn), so sánh với M36 (giảm chấn vi mô trong cấu trúc bện vs giảm chấn vĩ mô TMD), so sánh với M23 (vi trượt cục bộ tại giao điểm tiếp xúc vs trượt dầm vĩ mô). Lộ trình đọc dẫn đến Sec. 1 (pp. 1–2), Sec. 2 (pp. 2–3), Sec. 3 (pp. 3–4), Sec. 4 (p. 4).
- **Reason:** Xóa bỏ trạng thái lỗi thời của M23; loại bỏ template; làm nổi bật phát hiện khoa học M30-E05 về sự triệt tiêu vi trượt khi bị ép quá chặt (80 ppi), định hướng cho thiết kế vùng áp suất tối ưu của piston trong MP1.
- **Supporting Evidence ID / PDF locator:** M30-E01, M30-E02, M30-E04, M30-E05 (PDF pp. 1, 2, 4).
- **Change category:** `OBSOLETE_STATUS`, `TEMPLATE_REMOVAL`, `READING_ROUTE_IMPROVEMENT`

---

### Change 12: M22_NOTES.md & M26_NOTES.md — Reference Stub Path Clarification
- **Paper ID:** M22, M26
- **File path:** `outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md`, `M26_NOTES.md`
- **Section:** Header metadata (Pilot evidence IDs), F
- **Before:**
  ```markdown
  - **Pilot evidence IDs:** see `EVIDENCE_INDEX.csv`
  ```
- **After:**
  ```markdown
  - **Pilot evidence IDs:** see `outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv` (M22-E01 to M22-E06 / M26-E01 to M26-E07) and `PACKAGE_COVERAGE_REPORT.md`
  ```
- **Reason:** Làm rõ đường dẫn index của Pilot, tránh nhầm lẫn với `EVIDENCE_INDEX.csv` của WP-C vốn đã được chuẩn hóa để chỉ index 43 records nội bộ của WP-C. Bổ sung quan hệ định hướng với M23 (M22 làm nền tảng dầm Euler cho dầm 2D M23) và M27 (M26 làm nền tảng kéo vĩ mô cho phân rã subcomponents M27).
- **Supporting Evidence ID / PDF locator:** Pilot R1 verification report.
- **Change category:** `SOURCE_ROLE_CLARIFICATION`, `READING_ROUTE_IMPROVEMENT`
