# M08 — Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition

## A. Section objective
Trích xuất DEEP/TARGETED theo P1 cho các section: C1.1, C1.1.3, C1.2, C1.2.1, C2.3, C2.3.2, C2.3.3, C2.3.4, C2.3.5.

## B. Concept and terminology notes
Fiber-jamming surgical manipulator study with silicone modules and interlocking fibers; compares materials, surface finish and layouts using force, bending and shape-locking tests.

- Paper ID: `M08`; DOI/identifier: `10.3389/frobt.2019.00012`.
- Canonical PDF: `data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf`
- SHA-256: `7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933`
- Identity: `FULL_TEXT_VERIFIED`; physical page indexing starts at 1; printed page is `NOT_REPORTED` where not stable.

## C. Evidence with precise source locators

### M08-E01 — p. 4, Design / Fig. 2, Fig. 2
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “central channel hosts the fibers”
- **Original finding:** Module A is 50 mm long and 14.5 mm in external diameter; Module B retains a central lumen and uses an interlocking comb-like fiber arrangement.
- **Diễn giải kỹ thuật:** Hệ là fiber jamming trong module silicone; contact topology là fiber–fiber/interlocking comb, không phải wire–sleeve hay layer jamming.
- **Điều kiện:** `{"geometry": "Module A 50 mm x 14.5 mm; Module B central lumen", "material": "silicone; fibers", "interface": "interlocking comb"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C1.2.1, C2.3.2

### M08-E02 — p. 5, Table 1 / material comparison, Table 1
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “Stiffness variation”
- **Original finding:** At 0.1 bar, maximum force and stiffness variation depend strongly on fiber material and surface finish; reported stiffness variation includes +43% to +377.5% across tested combinations.
- **Diễn giải kỹ thuật:** Số liệu là giá trị trung bình ± độ phân tán của các cấu hình vật liệu cụ thể; không tách riêng được đóng góp ma sát và hình học từ bảng này.
- **Điều kiện:** `{"pressure": "0.1 bar", "materials": "PTFE, PVC, nylon, silicone, waxed cotton, leather", "output": "Fmax; stiffness variation"}`
- **Validation/limitation:** `{"validation": "NOT_REPORTED", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.3.2, C2.5.3

### M08-E03 — p. 7, Experimental methods / Fig. 5–6, Fig. 5; Fig. 6
- **Type/role:** `AUTHOR_RESULT` / `PRIMARY_EVIDENCE`
- **Anchor:** “measured the resistive force”
- **Original finding:** A robotic force sensor measured resistive force in rest and bent configurations; maximum force was compared across tests.
- **Diễn giải kỹ thuật:** Biến đo là force tại điểm tác dụng; điều kiện tải và hình học test được giữ cố định theo setup, nhưng không phải validation độc lập của mô hình vật lý tổng quát.
- **Điều kiện:** `{"measurement": "resistive force", "loading": "rest and bent", "validation": "module-level experiments"}`
- **Validation/limitation:** `{"validation": "module-level experiments", "limitations": "NOT_REPORTED"}`
- **Target sections:** C2.5.3

### M08-E04 — p. 10, Discussion / limitations, NOT_APPLICABLE
- **Type/role:** `COUNTEREVIDENCE` / `COUNTEREVIDENCE`
- **Anchor:** “significant reduction on flexibility and dexterity”
- **Original finding:** Adding fibers improves stiffening but reduces flexibility/dexterity; Module B bends mainly in one direction and the technology needs real-environment surgical testing and manufacturing standardization.
- **Diễn giải kỹ thuật:** Tác giả nêu trade-off stiffness–dexterity và thiếu kiểm chứng trong môi trường phẫu thuật; đây là giới hạn áp dụng rõ ràng.
- **Điều kiện:** `{"limitation": "reduced flexibility; one-direction bending; manual fabrication", "validation": "no real surgical environment"}`
- **Validation/limitation:** `{"validation": "no real surgical environment", "limitations": "reduced flexibility; one-direction bending; manual fabrication"}`
- **Target sections:** C2.3.5, C2.6.2

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
