# M21 — An Underactuated Variable Stiffness Continuum Robot With Multi-Layer Jamming Spherical Joints

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.4, C2.5.3, C2.6.

## B. Concept and terminology notes
2026 multi-layer jamming spherical joints and underactuated continuum robot using positive-pressure airbags; derives friction torque and validates stiffness, switching time, endurance and grasping.

- Paper ID: `M21`; DOI/identifier: `10.1109/TASE.2026.3673298`.
- Canonical PDF: `data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf`
- SHA-256: `ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M21-E01 — p. 1, Abstract / Fig. 1, Fig. 1
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “multi-layer frictional interactions within jamming structures”
- **Original finding:** The MLJSJ robot uses segmented spherical joints with positive-pressure airbag actuation; four serial segments each contain four joints and stiffness is modulated by dedicated airbags.
- **Diễn giải kỹ thuật:** Đây là spherical-joint multi-layer jamming and positive pressure; topology khác beam nhưng là prior art component-level.
- **Điều kiện:** `{"robot": "4 serial segments; 4 joints/segment", "pressure": "positive airbag", "interface": "multi-layer spherical joints"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2, C1.2.1, C2.3.4

### M21-E02 — p. 4, Mechanics model, Eqs. (1)–(4)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “uniformly distributed across the jamming surfaces”
- **Original finding:** Assuming pressure is uniformly distributed toward the spherical center, the paper integrates friction force to obtain locking torque and stiffness for the spherical joint.
- **Diễn giải kỹ thuật:** Giả thiết phân bố pressure đều và hình học cầu; không áp dụng trực tiếp cho beam layers.
- **Điều kiện:** `{"equations": "surface element dS; pressure component; friction torque", "assumption": "uniform pressure toward sphere center", "scope": "spherical joint"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.2

### M21-E03 — p. 6, Experiments / Fig. 6, Fig. 6
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “as the optimal operational limit”
- **Original finding:** The setup measures force–displacement, stiffness versus airbag pressure, endurance, switching time and hysteresis; operational limit 300 kPa is selected due to seal damage above it.
- **Diễn giải kỹ thuật:** Nguồn nêu rõ pressure ceiling is a seal/material limit, not a universal contact-pressure law.
- **Điều kiện:** `{"pressure": "up to 300 kPa operational", "outputs": "stiffness; switching time; hysteresis; endurance", "limitation": "seal damage above 300 kPa"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "seal damage above 300 kPa"}`
- **Target sections:** C2.3.4, C2.5.3, C2.6.2

### M21-E04 — p. 7, Results, Fig. 6
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “All recorded transition durations”
- **Original finding:** Stiffness switching times are 0.07–0.43 s across pressure spectrum; the reported peak segment stiffness is 1403.03 N/m with stiffness ratio 35.85.
- **Diễn giải kỹ thuật:** Đây là system-level quantitative performance của spherical joint, không phải beam constitutive validation.
- **Điều kiện:** `{"switching": "0.07–0.43 s", "stiffness": "1403.03 N/m peak; ratio 35.85", "test": "pressure transitions"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.1

### M21-E05 — p. 9, Durability, Fig. 6(i)
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “stiffness decreased by approximately 89 N/m”
- **Original finding:** After 1000 cycles at 200 kPa, stiffness decreases by approximately 89 N/m (3.6%), attributed to wear-induced friction-coefficient reduction.
- **Diễn giải kỹ thuật:** Độ bền cho thấy friction interface evolves with cycling; model calibration at one cycle cannot be assumed invariant.
- **Điều kiện:** `{"pressure": "200 kPa", "cycles": "1000", "loss": "89 N/m; 3.6%", "cause": "wear/reduced friction"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.2

### M21-E06 — p. 11, Conclusion / grasping, Fig. 8
- **Type/role:** `AUTHOR_RESULT` / `SUPPORTING_EVIDENCE`
- **Anchor:** “grasp a 50 g weight”
- **Original finding:** The integrated robot navigates obstacles and grasps a 50 g weight in a constrained environment; performance is demonstrated at robot level.
- **Diễn giải kỹ thuật:** Application-level validation does not isolate jamming constitutive behavior.
- **Điều kiện:** `{"payload": "50 g", "task": "obstacle avoidance and grasping", "validation": "integrated robot"}`
- **Validation/limitation:** `{"validation": "integrated robot", "limitations": "NOT_REPORTED"}`
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
