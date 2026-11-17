# M11 — A 3D Printed Soft Robotic Gripper With a Variable Stiffness Enabled by a Novel Positive Pressure Layer Jamming Technology

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.3, C2.3.4, C2.5.3, C2.6.

## B. Concept and terminology notes
Multi-material 3D-printed soft gripper using positive-pressure layer jamming; compares pressure-dependent stiffness and pull-out capacity.

- Paper ID: `M11`; DOI/identifier: `10.1109/LRA.2022.3157448`.
- Canonical PDF: `data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf`
- SHA-256: `cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M11-E01 — p. 2, Introduction / design principle, Fig. 1
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “performance potential”
- **Original finding:** Positive pressure is applied to a jamming bag so the layers are compressed by a pressure above atmospheric limitation; the design places layers on the inside radius in tension to avoid buckling.
- **Diễn giải kỹ thuật:** Nguồn áp suất dương và lớp hạn chế là phần của contact topology; payload increase không tự chứng minh mô hình continuum.
- **Điều kiện:** `{"geometry": "curved gripper finger; layers on inside radius", "material": "PETG; TPU", "pressure": "positive jamming pressure"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.1, C2.3.3, C2.3.4

### M11-E02 — p. 4, Stiffness test, Fig. 6a–b
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “gripper stiffness is roughly saturated”
- **Original finding:** Five trials per pressure, 6 mm deflection; stiffness roughly saturates by 10 psi (69.0 kPa), while 45 psi (310.3 kPa) shows no distinct slip over 6 mm.
- **Diễn giải kỹ thuật:** Force–displacement is measured at finger level; “no distinct slip” is an observable in this test range, not proof of no interlayer slip.
- **Điều kiện:** `{"pressure": "10 psi=69.0 kPa; 45 psi=310.3 kPa", "deflection": "6 mm", "repeats": "5"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.3

### M11-E03 — p. 5, Pull-out test, Fig. 6c–e
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “pull-out force increases above 12.5 psi”
- **Original finding:** Pull-out force rises above 12.5 psi (86.2 kPa) and payload capacity saturates near 35 psi (241.3 kPa); the reported design gives a 2.4x increase versus the cited commercial reference under different test-method provenance.
- **Diễn giải kỹ thuật:** Số liệu pull-out phụ thuộc gripper, object, pressure and protocol; comparison with commercial mGrip has unknown methodology.
- **Điều kiện:** `{"pressure": "12.5–35 psi (86.2–241.3 kPa)", "repeats": "5", "output": "pull-out force; payload"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.1

### M11-E04 — p. 6, Conclusion / limitations, Conclusion
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “future work could be done to improve the robustness”
- **Original finding:** Multi-material printing enables integrated airtight geometry, but process robustness and more complex geometry remain future work.
- **Diễn giải kỹ thuật:** Giới hạn chế tạo và chưa có full constitutive validation giới hạn khả năng dùng bài này để suy ra model beam nhiều lớp.
- **Điều kiện:** `{"limitation": "printing robustness; geometry complexity", "validation": "gripper-level"}`
- **Validation/limitation:** `{"validation": "gripper-level", "limitations": "printing robustness; geometry complexity"}`
- **Target sections:** C2.6.2

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
