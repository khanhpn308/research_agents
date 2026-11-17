# M14 — A Novel Continuum Robot With Stiffness Variation Capability Using Layer Jamming: Design, Modeling, and Validation

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.4, C2.5, C2.5.2, C2.5.3, C2.6.

## B. Concept and terminology notes
OctRobot-I continuum robot with woven layer-jamming sheath; Euler–Bernoulli equivalent-beam models cover four static loading cases and experiments vary overlap, angle and vacuum.

- Paper ID: `M14`; DOI/identifier: `10.1109/ACCESS.2022.3228775`.
- Canonical PDF: `data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf`
- SHA-256: `6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M14-E01 — p. 1, Abstract / design, Abstract; Fig. 1
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “experiments are conducted with two types of layer jamming sheaths”
- **Original finding:** OctRobot-I provides transverse and axial stiffness variation; tests use overlap n=3,5, vacuum 0,25,50,75 kPa and bending angles 0°,90°,180°.
- **Diễn giải kỹ thuật:** Robot-level prior art đã dùng layer-jamming sheath và equivalent beam; các biến áp suất/hình học được khảo sát trực tiếp.
- **Điều kiện:** `{"robot": "OctRobot-I; two sections", "layers": "n=3,5 overlap", "vacuum": "0,25,50,75 kPa", "angles": "0°,90°,180°"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.1, C2.3.4, C2.6.1

### M14-E02 — p. 5, Jamming geometry, Eqs. (1)–(3)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “overlap numbers (n) can be achieved”
- **Original finding:** Overlap number n=(2L+H)/dpitch and pitch bounds determine sheath geometry and length change during bending.
- **Diễn giải kỹ thuật:** Hình học sheath được tham số hóa bằng pitch/overlap; đây là mô hình thiết kế chứ không phải constitutive law của interface.
- **Điều kiện:** `{"equations": "n=(2L+H)/dpitch; pitch bounds; Δl=±25β", "geometry": "flaps, nylon wire, pitch"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.3.4, C2.5.5

### M14-E03 — p. 6, Equivalent beam model, Eqs. (5)–(12)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “The equivalent beam is homogeneous”
- **Original finding:** Maxwell–Mohr/Euler–Bernoulli equivalent-beam assumptions treat the beam as homogeneous, small-displacement and pure bending; axial case includes Euler buckling threshold Fcr=π²D/l².
- **Diễn giải kỹ thuật:** Các giả thiết homogenized beam được nêu rõ; chúng giới hạn miền áp dụng khi slip, shear hoặc large deformation chi phối.
- **Điều kiện:** `{"model": "Euler–Bernoulli; homogeneous equivalent beam", "assumptions": "small displacement; pure bending", "equation": "Fcr=π²D/l²"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.2, C2.5.5

### M14-E04 — p. 8, Experiments / Figs. 8–10, Fig. 8–10
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “maximum resisting force is 62.6N”
- **Original finding:** At 0° and 75 kPa maximum resisting force is 62.6 N (n=3) and 65.6 N (n=5); at 180° and 75 kPa values are 1.9 and 2.4 N. Transverse stiffness at 180° rises from 92.9/106.7 N/m at 0 kPa to 192.4/249.7 N/m at 75 kPa for n=3/5.
- **Diễn giải kỹ thuật:** Độ cứng phụ thuộc góc, overlap và vacuum; cùng pressure không cho cùng response do overlap/contact state thay đổi.
- **Điều kiện:** `{"vacuum": "0–75 kPa", "outputs": "force; N/m stiffness", "angles": "0°,90°,180°", "n": "3,5"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.6.1

### M14-E05 — p. 10, Limitations / conclusion, Conclusion
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “Effective stiffness modelling”
- **Original finding:** Effective flexural rigidity calculation and improved modeling of friction/mechanical error are left for future work; the model captures changing tendency rather than full contact detail.
- **Diễn giải kỹ thuật:** Tác giả thừa nhận hạn chế mô hình hóa ma sát và cơ cấu; không coi equivalent-beam result là full-layer reference.
- **Điều kiện:** `{"limitation": "friction; mechanical error; effective rigidity future work", "validation": "static prototype tests"}`
- **Validation/limitation:** `{"validation": "static prototype tests", "limitations": "friction; mechanical error; effective rigidity future work"}`
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
