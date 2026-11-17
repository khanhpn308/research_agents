# M20 — Continuum modeling for layer jamming structures

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.3, C2.3, C2.3.3, C2.3.5, C2.5, C2.5.1, C2.5.4, C2.5.5, C2.6.

## B. Concept and terminology notes
2026 continuum elastoplastic constitutive model for LJS from average-field RVE homogenization; defines macroscopic slip/yield criterion and validates with periodic-boundary Abaqus simulations under three loading paths.

- Paper ID: `M20`; DOI/identifier: `10.1016/j.taml.2025.100633`.
- Canonical PDF: `data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf`
- SHA-256: `a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M20-E01 — p. 1, Abstract / introduction, Abstract
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “elastoplastic constitutive”
- **Original finding:** The paper proposes a continuum elastoplastic constitutive model capturing jamming and slipping states with analytical yield criteria and dissipated energy density.
- **Diễn giải kỹ thuật:** Đây là đe dọa trực tiếp P1: continuum constitutive model cho LJS đã được công bố trong corpus.
- **Điều kiện:** `{"model": "continuum elastoplastic; average-field RVE", "states": "jamming and slipping", "validation": "Abaqus periodic-boundary simulations"}`
- **Validation/limitation:** `{"validation": "Abaqus periodic-boundary simulations", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.3.5, C2.5.5, C2.6.3

### M20-E02 — p. 3, RVE formulation, Eqs. (1)–(10)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “average”
- **Original finding:** The RVE uses first-order displacement modes, linear elastic layered material and volume-averaged microscopic stress to obtain continuous macroscopic stress.
- **Diễn giải kỹ thuật:** Homogenization is explicit and based on RVE assumptions; it is not a direct experiment and uses linear-elastic layer material in the presented formulation.
- **Điều kiện:** `{"equations": "displacement modes; strain; σ̄=1/V∫σdV", "assumptions": "RVE; first-order modes; linear elastic layers"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.4, C2.5.5

### M20-E03 — p. 4, Slip criterion, Eq. (18)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “boundary in macro”
- **Original finding:** Macroscopic slip occurs when sqrt(σ̄13²+σ̄23²) ≥ μ(p−σ̄33), defining a yield-like boundary in macroscopic stress space.
- **Diễn giải kỹ thuật:** Mô hình liên kết shear, normal stress, friction coefficient và hydrostatic pressure ở cấp continuum.
- **Điều kiện:** `{"equation": "sqrt(σ̄13²+σ̄23²) ≥ μ(p−σ̄33)", "parameters": "μ; p; macroscopic stresses", "state": "yield/slip boundary"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.5

### M20-E04 — p. 6, Numerical validation, Fig. 5–6
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “slightly lower than the”
- **Original finding:** Periodic-boundary Abaqus RVE simulations cover uniaxial shear loading/unloading; theoretical and numerical stress–strain and energy trends agree, with numerical stiffness about 0.888 GPa in the reported case.
- **Diễn giải kỹ thuật:** Đây là numerical validation, không phải experimental validation; slight deviations in dissipation energy/stress magnitudes remain.
- **Điều kiện:** `{"FEA": "Abaqus; periodic boundary", "loading": "shear loading/unloading", "quantitative": "numerical stiffness 0.888 GPa"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.4, C2.6.2

### M20-E05 — p. 7, Multidirectional and coupled loading, Fig. 7–8
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “stress path re-enters the jamming”
- **Original finding:** Multi-directional shear and coupled shear-normal loading track the predicted yield boundary and show increased interlayer slip during normal unloading; slight deviations remain.
- **Diễn giải kỹ thuật:** Model covers loading paths beyond one-dimensional beam bending, but validation is numerical RVE-level.
- **Điều kiện:** `{"loading": "multi-directional shear; coupled normal/shear", "output": "yield surface; dissipation", "validation": "FEA vs theory"}`
- **Validation/limitation:** `{"validation": "FEA vs theory", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.5

### M20-E06 — p. 8, Limitations, Conclusion
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “direct experimental methods”
- **Original finding:** The paper notes lack of effective direct experimental methods for probing the constitutive model and reports slight deviations in dissipation energy and stress magnitudes.
- **Diễn giải kỹ thuật:** Đây là unresolved evidence gap: constitutive model is a direct prior, but its experimental transfer to high-layer-count vacuum beams remains unverified in this source.
- **Điều kiện:** `{"limitation": "no direct experiment; numerical RVE only", "status": "experimental transfer NOT_VERIFIED"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "no direct experiment; numerical RVE only"}`
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
