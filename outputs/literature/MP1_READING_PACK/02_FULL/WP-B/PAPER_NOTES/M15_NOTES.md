# M15 — A Novel Model for Layer Jamming-based Continuum Robots

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2.3, C1.4, C1.4.2, C2.5, C2.5.1, C2.5.3, C2.6.

## B. Concept and terminology notes
ICRA 2024 control-oriented dynamic model for LJ continuum robots using energy-based port-Hamiltonian formulation and LuGre friction; proves shape-locking and pressure-dependent stiffness.

- Paper ID: `M15`; DOI/identifier: `10.1109/ICRA57147.2024.10610912`.
- Canonical PDF: `data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf`
- SHA-256: `b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M15-E01 — p. 1, Abstract / Fig. 1, Fig. 1
- **Type/role:** `AUTHOR_RESULT` / `COUNTEREVIDENCE`
- **Anchor:** “energy-based model that is integrated with the LuGre frictional model”
- **Original finding:** The paper proposes an energy-based model integrated with LuGre friction and validates it with OctRobot-I experiments for shape locking and adjustable stiffness.
- **Diễn giải kỹ thuật:** Đây là prior art mô hình động control-oriented cho LJ continuum robot, trực tiếp làm suy yếu claim rằng chỉ có homogenized static model.
- **Điều kiện:** `{"model": "port-Hamiltonian + LuGre", "system": "tendon-driven LJ continuum robot", "validation": "OctRobot-I experiments"}`
- **Validation/limitation:** `{"validation": "OctRobot-I experiments", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.3, C1.4, C2.5.1

### M15-E02 — p. 2, II.A–II.C model, Eqs. (1)–(14)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “when the pressure uP = 0”
- **Original finding:** The Hamiltonian combines kinetic/potential energy with pressure-dependent virtual-bristle energy; pressure enters the friction subsystem and is an additional input.
- **Diễn giải kỹ thuật:** Mô hình gắn pressure với friction state, không xem pressure chỉ là hệ số scale của độ cứng.
- **Điều kiện:** `{"equations": "H(q,p), Hz(z,uP), LuGre state", "inputs": "tendon u and vacuum uP", "assumptions": "uniform pressure; constant air mass; stated LuGre conditions"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.3

### M15-E03 — p. 3, Proposition 1 / shape locking, Proposition 1; Eqs. (20)–(32)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “a large pressure value”
- **Original finding:** The model theoretically establishes shape-locking invariance/stability under pressure and gives an open-loop stiffness relation increasing with vacuum pressure.
- **Diễn giải kỹ thuật:** Đây là kết quả lý thuyết trong miền giả thiết của model; shape locking phụ thuộc equilibrium manifold và initial condition.
- **Điều kiện:** `{"model": "local asymptotic stability; manifold M", "pressure": "uP>0", "limitation": "local/neighborhood conditions"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "local/neighborhood conditions"}`
- **Target sections:** C2.5.1, C2.5.3, C2.6.2

### M15-E04 — p. 6, Experiments / Figs. 4–7, Fig. 4; Fig. 6; Fig. 7
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “vacuum to uP = 30 kPa”
- **Original finding:** Shape-locking experiment uses vacuum −30 kPa after driving to 60°; open-loop stiffness experiments use two-layer sheath and pressures up to 40 kPa, repeated three times.
- **Diễn giải kỹ thuật:** Validation kết hợp shape locking và transverse stiffness; không phải independent full-layer contact validation.
- **Điều kiện:** `{"pressure": "−30 kPa shape locking; up to 40 kPa stiffness", "repeats": "3 for stiffness", "platform": "OctRobot-I"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.5.4

### M15-E05 — p. 7, Limitations / scope, Conclusion
- **Type/role:** `AUTHOR_INTERPRETATION` / `COUNTEREVIDENCE`
- **Anchor:** “control-oriented model”
- **Original finding:** The model is designed for control and relies on identified friction/pressure functions; experiments specialize to a single-section prototype and bounded pressure range.
- **Diễn giải kỹ thuật:** Giới hạn nhận dạng và platform-specific cần được giữ khi dùng làm prior art.
- **Điều kiện:** `{"limitation": "identified functions; single platform; bounded range", "validation": "prototype experiments"}`
- **Validation/limitation:** `{"validation": "prototype experiments", "limitations": "identified functions; single platform; bounded range"}`
- **Target sections:** C2.6.2, C2.6.3

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
