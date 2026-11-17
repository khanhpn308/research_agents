# M10 — A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.2, C1.2.1, C2.3, C2.3.3, C2.3.4, C2.5.3, C2.6.

## B. Concept and terminology notes
Positive-pressure granular jamming (PPJ) uses an inflatable bladder inside a nonstretchable sleeve; force is transmitted to granules and friction locks the structure.

- Paper ID: `M10`; DOI/identifier: `10.1109/LRA.2021.3097255`.
- Canonical PDF: `data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`
- SHA-256: `182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M10-E01 — p. 2, Design / Fig. 1, Fig. 1
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “squeeze air into a rubber bladder”
- **Original finding:** The PPJ unit embeds a pneumatic rubber bladder in granular medium inside a fabric sleeve; bladder expansion compresses granules and stiffens the unit.
- **Diễn giải kỹ thuật:** Cơ chế là positive-pressure granular jamming, với pressure path qua bladder–granules–sleeve; khác vacuum layer-jamming.
- **Điều kiện:** `{"geometry": "26 mm diameter, 50 mm length prototype", "material": "rubber bladder; SMP granules; fabric sleeve", "pressure": "positive air"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.1, C2.3.3, C2.3.4

### M10-E02 — p. 5, Model derivation, Eq. (3)–(5)
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “equivalent Young’s modulus of PPJ can be expressed”
- **Original finding:** The paper proposes E=C/(D²−d²), K=3πC(D²+d²)/(64L³), and a stiffness-to-mass expression for the annular PPJ geometry.
- **Diễn giải kỹ thuật:** Đây là quan hệ bán thực nghiệm theo hình học D,d,L và hệ số C phụ thuộc vật liệu/áp suất; không phải định luật vật liệu độc lập.
- **Điều kiện:** `{"equations": "E=C/(D²−d²); K=3πC(D²+d²)/(64L³)", "geometry": "outer D; inner d; length L", "assumption": "annular geometry; C fixed for comparison"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.5

### M10-E03 — p. 4, Parameter study, Fig. 6–8; Table I
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “mean values of 8 times repeated tests”
- **Original finding:** Eight specimens with D=26,29,32,35 mm and d=10 or 15 mm were tested at 103 kPa relative input; mean curves use eight repeats and 95% confidence intervals.
- **Diễn giải kỹ thuật:** Các kết quả định lượng gắn với PPJ granular and test repeatability; equivalent Young’s modulus is an effective parameter.
- **Điều kiện:** `{"pressure": "103 kPa relative", "D": "26,29,32,35 mm", "d": "10,15 mm", "repeats": "8; 95% CI"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3, C2.5.4

### M10-E04 — p. 7, Limitations, Conclusion / future work
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “Though more tests are need to verify state transition time”
- **Original finding:** Sandpaper friction pads may wear; transition times need more tests; bladder and granule distribution require redesign.
- **Diễn giải kỹ thuật:** Tác giả chưa xác minh đầy đủ tốc độ chuyển trạng thái và độ bền lâu dài; các claim về faster response vẫn là tiềm năng.
- **Điều kiện:** `{"limitation": "wear; unverified transition time; granule distribution", "validation": "application-level"}`
- **Validation/limitation:** `{"validation": "application-level", "limitations": "wear; unverified transition time; granule distribution"}`
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
