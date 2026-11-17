# M12 — Soft actuator with switchable stiffness using a micropump-activated jamming system

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.3, C2.3.4, C2.4, C2.4.4, C2.5.3, C2.6.

## B. Concept and terminology notes
Granular-jamming soft actuator with embedded bidirectional electro-conjugate-fluid micropump; negative pressure jams particles and positive pressure bends the actuator.

- Paper ID: `M12`; DOI/identifier: `10.1016/j.sna.2022.113449`.
- Canonical PDF: `data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`
- SHA-256: `bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M12-E01 — p. 3, Concept / Fig. 2–3, Fig. 2
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “granular jamming by negative pressure of ECF jet flow”
- **Original finding:** The actuator combines negative ECF pressure for granular jamming and positive ECF pressure for bending in the same PDMS body.
- **Diễn giải kỹ thuật:** Hai đường áp suất có vai trò khác nhau: negative pressure điều biến frictional jamming, positive pressure tạo biến dạng actuator.
- **Điều kiện:** `{"material": "PDMS; aluminium oxide particles; flexible ECF micropump", "pressure": "negative for jamming; positive for bending", "geometry": "24 x 8 x 6 mm actuator"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.1, C1.2.2, C2.3.3, C2.4.4

### M12-E02 — p. 8, Stiffness experiment, Fig. 10–11
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “When the negative pressure increased, the bending force increased”
- **Original finding:** Micropump output reaches 55 kPa and 140 mm³/s; at 3 mm displacement bending force increases from 0.134 N to 0.743 N at −50 kPa, a 5.5x increment.
- **Diễn giải kỹ thuật:** Độ cứng được đánh giá bằng bending force tại 3 mm; pressure đo ngoài/không hoàn toàn tại buồng tích hợp.
- **Điều kiện:** `{"pressure": "up to 55 kPa pump; −50 kPa jamming", "flow": "140 mm³/s", "force": "0.134 to 0.743 N at 3 mm", "output": "5.5x force increment"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.5.4

### M12-E03 — p. 9, Load and bending, Fig. 12–13
- **Type/role:** `AUTHOR_RESULT` / `SUPPORTING_EVIDENCE`
- **Anchor:** “soft actuator carried the mass 5.2 times its weight”
- **Original finding:** At 2.5 kV the actuator carried 5.2 times its own weight; positive pressure up to about 50 kPa produced a maximum bending angle of 16° and tip displacement about 7 mm.
- **Diễn giải kỹ thuật:** Kết quả actuator-level; không nên đồng nhất với beam bending stiffness hoặc local normal traction.
- **Điều kiện:** `{"voltage": "2.5 kV; 1.1–2.45 kV", "positive_pressure": "up to +50 kPa", "output": "5.2x self-weight; 16°; 7 mm"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.4.4, C2.6.1

### M12-E04 — p. 7, Measurement limitation, Sec. 4.1
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “We cannot measure the output pressure and flow rate”
- **Original finding:** The assembled device could not directly measure output pressure and flow rate because of integrated design; voltage-to-pressure relation was characterized separately.
- **Diễn giải kỹ thuật:** Đây là giới hạn provenance quan trọng: source pressure và pressure trong chamber không được đo đồng thời trực tiếp.
- **Điều kiện:** `{"limitation": "no direct pressure/flow measurement in assembled actuator", "validation": "separate pump characterization"}`
- **Validation/limitation:** `{"validation": "separate pump characterization", "limitations": "no direct pressure/flow measurement in assembled actuator"}`
- **Target sections:** C1.2.2, C2.6.2

## D. Important equations and figures
Các locator quan trọng được liệt kê trong `EQUATION_REGISTRY.md` và `FIGURE_TABLE_REGISTRY.md`; không tự số hóa đồ thị. Phương trình chỉ được chép dưới dạng ký hiệu có trong PDF, còn biến đổi của agent không được ghi là phương trình gốc.

## E. Experimental and quantitative findings
Các giá trị định lượng chỉ áp dụng trong điều kiện đã ghi ở từng Evidence Record; không chuyển force–displacement cấp hệ thành constitutive law vật liệu.

## F. Cross-paper comparisons
So sánh với các paper khác chỉ là mapping cơ chế/model level trong P1; không dùng paper này đơn độc để khẳng định novelty.

## G. Limitations and counterevidence
Giữ nguyên các mục `COUNTEREVIDENCE` và phân biệt calibration với independent validation.

## H. Relevance to MP1
Paper cung cấp bằng chứng cho các section Chương 1–2 nêu trên, đặc biệt ranh giới giữa pressure source, contact friction, slip state và model level.

## I. Reading route
Đọc abstract/introduction → figure/model locator → experimental setup → results → conclusion/limitations; đối chiếu trực tiếp PDF tại các trang đã ghi.

## J. Questions for human writing
- Đại lượng stiffness nào đang được đo và ở boundary condition nào?
- Pressure là source pressure hay local normal traction?
- Kết quả là author result, interpretation hay agent inference?

## K. Unresolved evidence
Printed-page convention và các chi tiết không được source báo cáo giữ `NOT_REPORTED`; không suy diễn ngoài miền validation.
