# M19 — Toward a deeper understanding of layer jamming structures

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C2.3, C2.3.4, C2.3.5, C2.5, C2.5.1, C2.5.2, C2.5.3, C2.5.4, C2.6.

## B. Concept and terminology notes
2025 beam-stack LJS model using stress distributions, slip-region coordinate ys, friction threshold μp and incremental stress history; validated on straight/curved beams and cyclic hysteresis.

- Paper ID: `M19`; DOI/identifier: `10.1007/s11465-025-0843-5`.
- Canonical PDF: `data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf`
- SHA-256: `7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M19-E01 — p. 3, 2 Numerical stress analysis, Fig. 3
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “A uniform pressure”
- **Original finding:** FEA of simply supported 5/10/25-layer beams with E=0.3 GPa, μ=0.5, p=0.1 MPa shows stress and stress-increment patterns across jamming/sliding regions.
- **Diễn giải kỹ thuật:** Mô hình dùng discrete layer count and FEA stress fields; assumptions include chosen E, μ and pressure, not measured constitutive values.
- **Điều kiện:** `{"layers": "5,10,25", "E": "0.3 GPa", "μ": "0.5", "p": "0.1 MPa", "FEA": "Abaqus CPS4R"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.2

### M19-E02 — p. 6, 3 Stress distribution, Eqs. (1)–(7)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “τ = sign(Q)μp”
- **Original finding:** The model represents linear normal stress in jamming regions and friction shear τ=sign(Q)μp in sliding regions; the sliding coordinate ys and stress increments determine state pattern.
- **Diễn giải kỹ thuật:** Đây là state-dependent layer model gần với full-layer mechanics hơn homogenized beam; axial force N is explicitly omitted for bending focus.
- **Điều kiện:** `{"equations": "σ distributions; τ=sign(Q)μp; state criterion Eq.7", "assumptions": "small deformation; axial force omitted for bending"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.2

### M19-E03 — p. 8, 3.2–3.3 equations, Eqs. (11)–(25)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “Tracking stress increments provides a”
- **Original finding:** Moment/shear balance determines kσ,kτ, critical Qcr and iterative curvature increment Δθ; the algorithm updates state as load changes.
- **Diễn giải kỹ thuật:** Mô hình theo dõi lịch sử stress increment và propagation of slip, vượt qua mô tả chỉ bằng hai cận độ cứng.
- **Điều kiện:** `{"equations": "kσ; kσ′; Qcr; Δθ", "method": "iterative algorithm", "scope": "straight/curved beam"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.5

### M19-E04 — p. 11, 4 Experimental verification, Fig. 6–7
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “to cyclic loading, with deflections alternating”
- **Original finding:** PVC-sheet beams (150 mm x 20 mm x 5.1 mm, 0.3-mm layers) were tested at hydrostatic pressures 40,70,100 kPa; simply supported cyclic tests alternate ±3 mm for five cycles.
- **Diễn giải kỹ thuật:** Validation gồm load–deflection, curved geometry and hysteresis; stiffness is differential quotient ΔF/Δw.
- **Điều kiện:** `{"material": "PVC sheets in polyethylene bag", "geometry": "150x20x5.1 mm; 0.3 mm layers", "pressure": "40,70,100 kPa", "cycles": "5; ±3 mm"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.5.4

### M19-E05 — p. 13, Results, Fig. 7
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “robust correlation”
- **Original finding:** Model predictions correlate with experiments for pressure, layer thickness, curved beams and hysteresis; critical load increases with pressure and stiffness decreases as slip progresses.
- **Diễn giải kỹ thuật:** Tác giả báo robust correlation trong phạm vi specimen/tests; chưa phải independent validation ngoài cùng cấu hình.
- **Điều kiện:** `{"outputs": "critical load; stiffness; hysteresis", "scope": "straight, semicircular, quarter-circular"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.1

### M19-E06 — p. 14, Limitations / interpretation, Conclusion
- **Type/role:** `AUTHOR_INTERPRETATION` / `COUNTEREVIDENCE`
- **Anchor:** “how stiffness decreases as slip progresses”
- **Original finding:** The model predicts gradual stiffness change rather than abrupt transitions and attributes hysteresis area to frictional dissipation.
- **Diễn giải kỹ thuật:** Đây là một mô hình layer-aware mới trong corpus; phải ghi rõ nguồn là 2025 và các giả thiết/miền kiểm chứng.
- **Điều kiện:** `{"limitation": "model approximation; frictional hysteresis", "validation": "beam bending tests"}`
- **Validation/limitation:** `{"validation": "beam bending tests", "limitations": "model approximation; frictional hysteresis"}`
- **Target sections:** C2.5.5, C2.6.2

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
