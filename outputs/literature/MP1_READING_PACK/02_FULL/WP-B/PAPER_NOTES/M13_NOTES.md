# M13 — A variable stiffness omnidirectional chain based on positive-pressure fiber jamming

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.2, C2.3.4, C2.3.5, C2.5.1, C2.5.3, C2.6.

## B. Concept and terminology notes
2026 positive-pressure fiber-jamming chain paper with explicit mechanics states, pressure-dependent transition loads, equivalent moment of inertia, and three-point-bending validation from 0–300 kPa.

- Paper ID: `M13`; DOI/identifier: `10.5194/ms-17-481-2026`.
- Canonical PDF: `data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`
- SHA-256: `3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M13-E01 — p. 1, Abstract / Introduction, Abstract
- **Type/role:** `AUTHOR_RESULT` / `COUNTEREVIDENCE`
- **Anchor:** “intrinsic pressure limitation (∼ 1 atm)”
- **Original finding:** The VSOC uses an inflatable bladder to compact a fiber bundle in a rigid chain link, extending operation beyond the approximately 1-atm vacuum limit.
- **Diễn giải kỹ thuật:** Đây là prior art gần về positive-pressure jamming nhưng fiber bundle + rigid chain link, không phải vacuum layer-jamming beam.
- **Điều kiện:** `{"pressure": "0–300 kPa tested", "material": "fiber bundle; inflatable bladder; rigid chain link", "scope": "chain bending"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2, C2.3.2, C2.3.4

### M13-E02 — p. 3, 2 Mechanics analysis, Eqs. (1)–(3)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “QJ = kµp”
- **Original finding:** Jamming and slipping thresholds follow τmax(Q)=μp, QJ=kμp and QS=Aμp, linking transition loads to friction coefficient, pressure and geometry.
- **Diễn giải kỹ thuật:** Ngưỡng chuyển trạng thái được mô hình hóa bằng frictional shear capacity; p là jamming pressure trong mô hình, không tự động là source pressure.
- **Điều kiện:** `{"equations": "τmax=μp; QJ=kμp; QS=Aμp", "parameters": "μ, p, geometry k,A", "states": "jamming, transition, slipping"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.2

### M13-E03 — p. 5, 2.2 Equivalent bending stiffness, Eq. (11)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “phenomenological model compactly represents”
- **Original finding:** Equivalent inertia Ieq is piecewise: IJ below QJ, a quadratic transition between QJ and QS, and IS above QS.
- **Diễn giải kỹ thuật:** Mô hình dùng một quan hệ phenomenological cho miền chuyển tiếp; không phải homogenization liên tục đã được chứng minh cho mọi layer count.
- **Điều kiện:** `{"equation": "piecewise Ieq(Q)", "states": "jammed/transition/slipping", "assumption": "quadratic transition"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.3, C2.5.5

### M13-E04 — p. 7, 4 Experimental methods, Fig. 4–5
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “systematic experimental investigation was conducted”
- **Original finding:** Three-point bending tests cover shaft and lateral bending, pressures 0–300 kPa, five repeats per pressure/mode; critical loads are identified by piecewise linear regression.
- **Diễn giải kỹ thuật:** Validation là prototype-level với một fiber type/diameter/count; regression identifies critical loads from global F–δ.
- **Điều kiện:** `{"pressure": "0–300 kPa", "repeats": "5", "loading": "three-point bending; shaft/lateral", "identification": "piecewise linear regression"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.5.4

### M13-E05 — p. 10, Results / Fig. 6, Fig. 6
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “0.4475”
- **Original finding:** Critical loads and slipping-state inertia increase approximately linearly with pressure, while jammed-state inertia is comparatively insensitive; lateral-mode fit for QJ has R²=0.4475.
- **Diễn giải kỹ thuật:** Có bằng chứng định lượng pressure dependence và một fit yếu ở lateral mode; không được mô tả là validation hoàn hảo.
- **Điều kiện:** `{"pressure": "0–300 kPa", "quantitative": "lateral QJ fit R²=0.4475", "outputs": "QJ, QS, IJ, IS"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.2

### M13-E06 — p. 11, Limitations, Conclusion / limitations
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “single VSOC prototype”
- **Original finding:** The quadratic transition relation is phenomenological and validation is restricted to a single prototype with one fiber type, diameter and count; friction and pressure transmission variability remain.
- **Diễn giải kỹ thuật:** Đây là counterevidence trực tiếp về khả năng tổng quát hóa và identifiability của model.
- **Điều kiện:** `{"limitation": "single prototype; one fiber type/diameter/count; nonuniform pressure; stick-slip", "status": "generalization not established"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "single prototype; one fiber type/diameter/count; nonuniform pressure; stick-slip"}`
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
