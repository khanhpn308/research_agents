# M07 — Mechanically Versatile Soft Machines through Laminar Jamming

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.1.2, C1.2, C1.2.2, C2.2, C2.2.2, C2.2.3, C2.3, C2.3.2, C2.5, C2.5.2, C2.5.3, C2.6.

## B. Concept and terminology notes
Primary laminar-jamming mechanics paper: derives a two-layer analytical elastica with spatially propagating slip, validates against FE and experiments, and demonstrates shape locking and variable kinematics.

- Paper ID: `M07`; DOI/identifier: `10.1002/adfm.201707136`.
- Canonical PDF: `data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf`
- SHA-256: `5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M07-E01 — p. 2, Introduction / Fig. 1, Fig. 1
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “layers are cohesive only until a critical force”
- **Original finding:** When vacuum is on, layers are cohesive only until a critical force; above it longitudinal shear stress causes slip and lowers stiffness.
- **Diễn giải kỹ thuật:** Cấu trúc có miền tiền-trượt, chuyển tiếp và trượt hoàn toàn; ngưỡng phụ thuộc tải, ma sát và áp suất nên không thể đồng nhất trạng thái hút chân không với một độ cứng duy nhất.
- **Điều kiện:** `{"layers": "copy paper stack", "pressure": "vacuum 0–71 kPa in tests", "loading": "bending; transverse force"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.2.2, C2.3.2, C2.5.1

### M07-E02 — p. 3, Analytical model, Fig. 2; SI Governing Equations
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “the slipped region initiates at the clamped end”
- **Original finding:** The two-layer elastica predicts the slipped region initiating at the clamped end and growing toward the free end as load increases; two-layer FE corroborated predicted slip regions.
- **Diễn giải kỹ thuật:** Mô hình giải tích dùng điều kiện biên kẹp–tự do và ma sát Coulomb để dự đoán biên trượt; FE chỉ là đối chiếu của cấu hình hai lớp.
- **Điều kiện:** `{"model": "two-layer elastica; Coulomb friction", "boundary": "clamped-free", "validation": "two-layer FE"}`
- **Validation/limitation:** `{"validation": "two-layer FE", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.1, C2.5.2, C2.5.5

### M07-E03 — p. 4, Experiments / Fig. 3, Fig. 3
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “Effect of Number of Layers”
- **Original finding:** Force–deflection behavior varies with layer count, vacuum pressure and coefficient of friction; experiments include 5, 10, 15 and 20 layers and pressure 0, 24, 47 and 71 kPa.
- **Diễn giải kỹ thuật:** Kết quả định lượng là force–deflection của giấy copy trong điều kiện thí nghiệm cụ thể; không suy ra trực tiếp constitutive law của mọi vật liệu lớp.
- **Điều kiện:** `{"layers": "5,10,15,20", "pressure": "0,24,47,71 kPa", "friction": "0.25,0.50,0.75", "measurement": "force-deflection"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.3.4, C2.5.3

### M07-E04 — p. 7, Conclusion, Conclusion
- **Type/role:** `AUTHOR_INTERPRETATION` / `COUNTEREVIDENCE`
- **Anchor:** “nonlinear structural”
- **Original finding:** Laminar jamming bridges compliant and rigid behavior through shape locking and variable kinematics, but the stiffness is nonlinear and slip-dependent.
- **Diễn giải kỹ thuật:** Đây là kết luận chức năng của tác giả; nó không chứng minh mô hình liên tục cho beam nhiều lớp.
- **Điều kiện:** `{"validation": "experiments and FE", "limitation": "nonlinear slip"}`
- **Validation/limitation:** `{"validation": "experiments and FE", "limitations": "nonlinear slip"}`
- **Target sections:** C2.3.5, C2.6.1, C2.6.2

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
