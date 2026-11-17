# M09 — Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.2, C2.3.5, C2.5.1, C2.5.3, C2.6.

## B. Concept and terminology notes
Wire/fiber-jamming actuator with kraft rope, hemp rope or nylon wire in an HDPE envelope; reports bending/torsional tests, pressure response and applications.

- Paper ID: `M09`; DOI/identifier: `10.3390/app12073582`.
- Canonical PDF: `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`
- SHA-256: `240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M09-E01 — p. 4, 2.2 Design, Fig. 2
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “choose inextensible materials”
- **Original finding:** The jamming media are inextensible kraft rope, hemp rope or nylon wire; layout and diameter affect compression, local rearrangement and gradient effects.
- **Diễn giải kỹ thuật:** Đây là wire/rope jamming trong envelope HDPE; không nên gộp với laminar sheet jamming.
- **Điều kiện:** `{"material": "kraft, hemp, nylon", "envelope": "HDPE", "geometry": "rectangular/circular layouts", "interface": "wire-wire and envelope"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.1, C2.3.2

### M09-E02 — p. 8, 3.1 Characterization, Fig. 4
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “the force sensor moves at a slow speed”
- **Original finding:** Three-point bending and torsion tests compare force/deflection and torque/rotation under vacuum; the test uses wire length 140–150 mm and thickness d=6 mm in representative plots.
- **Diễn giải kỹ thuật:** Độ cứng được suy ra từ force/deflection hoặc torque/angle ở tốc độ chậm; đây là system-level stiffness.
- **Điều kiện:** `{"pressure": "0 to −85 kPa in tests", "geometry": "wire length 140–150 mm; d=6 mm", "measurement": "force-deflection; torque-rotation"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3

### M09-E03 — p. 9, Conceptual regimes, Fig. 4g
- **Type/role:** `AUTHOR_INTERPRETATION` / `PRIMARY_EVIDENCE`
- **Anchor:** “the wires start to slip”
- **Original finding:** The jammed response is described as pre-slip (cohesive wires), transition (nonlinear slip onset), and post-slip/full-slip (slow linear increase).
- **Diễn giải kỹ thuật:** Phân vùng stick–transition–full slip được tác giả mô tả định tính từ đường force–deflection; không phải phép đo local slip trực tiếp.
- **Điều kiện:** `{"model": "three response regimes", "loading": "bending", "observable": "force-deflection"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.3

### M09-E04 — p. 10, Application / Fig. 5, Fig. 5
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “remarkably enhanced”
- **Original finding:** At 90° bending, assembled actuator requires 145 kPa positive actuation versus about 87 kPa for the actuator alone; switching vacuum from 0 to −85 kPa markedly increases bending stiffness.
- **Diễn giải kỹ thuật:** Áp suất dương của actuator và chân không của wire-jamming là hai biến khác nhau; không được gọi chúng là cùng một áp suất tiếp xúc.
- **Điều kiện:** `{"positive_pressure": "145 vs 87 kPa at 90°", "vacuum": "0 to −85 kPa", "application": "gripper; wearable glove"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.2, C2.3.4, C2.6.1

### M09-E05 — p. 11, Application results, Fig. 5h
- **Type/role:** `AUTHOR_RESULT` / `SUPPORTING_EVIDENCE`
- **Anchor:** “grasping mass of the soft gripper is increased by two times”
- **Original finding:** The soft gripper maximum grasping mass approximately doubles when vacuum changes from 0 to −85 kPa; glove lifting over 10,000 g is reported.
- **Diễn giải kỹ thuật:** Kết quả tải là của prototype ứng dụng với điều kiện áp suất dương/âm nêu trong caption; không phải validation constitutive.
- **Điều kiện:** `{"vacuum": "0 to −85 kPa", "output": "grasping mass; glove load", "uncertainty": "NOT_REPORTED"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.6.1

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
