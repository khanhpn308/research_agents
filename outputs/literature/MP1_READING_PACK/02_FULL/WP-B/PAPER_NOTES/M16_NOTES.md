# M16 — Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.3, C1.4, C2.3, C2.3.4, C2.5, C2.5.1, C2.5.3, C2.5.4, C2.6.

## B. Concept and terminology notes
2026 extension of the LJ continuum model: port-Hamiltonian/LuGre dynamics, pressure as control input, shape-locking analysis, parameter identification and closed-loop position/stiffness control.

- Paper ID: `M16`; DOI/identifier: `10.1109/TCST.2026.3690756`.
- Canonical PDF: `data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf`
- SHA-256: `1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M16-E01 — p. 1, Abstract / introduction, Abstract
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “models rely on static or quasi-static”
- **Original finding:** The paper states most prior LJ continuum models are static or quasi-static and proposes a control-oriented dynamical model integrating energy-based mechanics and LuGre friction.
- **Diễn giải kỹ thuật:** Đây là counterevidence mới nhất trong corpus đối với giả định rằng mô hình động/constitutive liên quan chưa có.
- **Điều kiện:** `{"model": "dynamical port-Hamiltonian + LuGre", "scope": "LJ continuum robot", "year": "2026"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.3, C2.3, C2.5.5

### M16-E02 — p. 2, II model assumptions, Eqs. (1)–(15)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “adjusted in real time and viewed as an additional input”
- **Original finding:** The model uses piecewise-constant-curvature kinematics, pressure-dependent parameters and a LuGre friction state; pressure uP is an additional nonnegative input and functions are identified.
- **Diễn giải kỹ thuật:** Mô hình vẫn là reduced-order/control-oriented với giả thiết PCC và hàm cần nhận dạng; không phải full contact FE.
- **Điều kiện:** `{"assumptions": "PCC; smooth pressure function; LuGre friction", "inputs": "tendon u; vacuum uP", "parameters": "αi, φ(uP), σi"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.4

### M16-E03 — p. 4, Proposition 1, Proposition 1; Fig. 3
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “local asymptotic stability of the manifold”
- **Original finding:** Theoretical results characterize an equilibrium manifold and local asymptotic stability for shape locking; larger pressure can enlarge the relevant attraction neighborhood.
- **Diễn giải kỹ thuật:** Kết quả stability là local và conditional on model assumptions; không nên dùng để khẳng định universal physical law.
- **Điều kiện:** `{"result": "local asymptotic stability", "pressure": "uP>0", "scope": "equilibrium manifold"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.6.2

### M16-E04 — p. 11, Open-loop validation, Fig. 7
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “increasing the vacuum pressure”
- **Original finding:** Two-layer sheath experiments show transverse stiffness increasing with vacuum; fitted comparison uses KT=3.7315uP+154.2731.
- **Diễn giải kỹ thuật:** Fit là platform-specific và được so với prior model; pressure is gauge vacuum, not local normal traction.
- **Điều kiện:** `{"layers": "2", "pressure": "0–40 kPa", "equation": "KT=3.7315uP+154.2731", "repeats": "3"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.5.4

### M16-E05 — p. 12, Parameter identification, Fig. 8; Eq. (49)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “we identified the key parameters”
- **Original finding:** Parameters c1=−0.0015, c2=0.0890, c3=1.7056, α1=1.0227 and c4=110.9847, c5=29.1067 are identified from repeated equilibrium/stiffness data.
- **Diễn giải kỹ thuật:** Đây là calibration/identification, không phải independent validation; cần giữ distinction này khi dùng trong P1.
- **Điều kiện:** `{"parameters": "c1,c2,c3,α1,c4,c5", "method": "optimization and fit", "repeats": "3 per pressure in key experiments"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.4, C2.6.2

### M16-E06 — p. 13, Closed-loop control, Fig. 9–10; Table I–II
- **Type/role:** `AUTHOR_RESULT` / `COUNTEREVIDENCE`
- **Anchor:** “simultaneously regulate both the robot”
- **Original finding:** Closed-loop experiments regulate configuration and stiffness at vacuum 0–40 kPa; transient stages were under 15 s and contributions of γ and α2 were reported.
- **Diễn giải kỹ thuật:** Kết quả closed-loop chứng minh khả năng điều khiển của reduced model, không phải xác minh contact mechanics độc lập.
- **Điều kiện:** `{"pressure": "0,10,20,30,40 kPa", "output": "configuration/stiffness; steady-state errors", "duration": "transient <15 s"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.1

### M16-E07 — p. 14, Conclusion / limitation, Conclusion
- **Type/role:** `AUTHOR_INTERPRETATION` / `COUNTEREVIDENCE`
- **Anchor:** “LuGre frictional model”
- **Original finding:** The article presents a successful control-oriented model and experiments but does not claim full-layer constitutive identification; functions remain platform/parameter dependent.
- **Diễn giải kỹ thuật:** Giới hạn này ngăn việc suy ra rằng mọi high-layer-count beam đã được mô hình hóa đầy đủ.
- **Điều kiện:** `{"limitation": "reduced order; identified functions; platform-specific", "validation": "closed-loop prototype"}`
- **Validation/limitation:** `{"validation": "closed-loop prototype", "limitations": "reduced order; identified functions; platform-specific"}`
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
