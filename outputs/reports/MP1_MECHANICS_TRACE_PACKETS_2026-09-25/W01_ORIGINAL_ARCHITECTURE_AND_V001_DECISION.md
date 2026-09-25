# W01 — Tái dựng kiến trúc Mentor ban đầu và Quyết định MP1-V001

## 1. Mục tiêu (Mission)

Tái dựng đầy đủ, có thể kiểm chứng toàn bộ chuỗi logic từ kiến trúc ban đầu do mentor đề xuất (mentor architecture) qua 8 phát biểu (claims C1–C8), thiết kế kiểm chứng phản biện (falsification design) của vòng MP1-V001, và nguyên nhân cốt lõi dẫn đến phán quyết `PIVOT_TO_MECHANICS_CORE`. Gói bằng chứng này làm rõ vì sao tính mới ở cấp độ tích hợp linh kiện (component-combination novelty) sụp đổ hoàn toàn và điều gì còn lại để dự án chuyển hướng sang bài toán cơ học tiếp xúc ma sát ghép cặp (coupled contact-friction mechanics core).

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/project/MENTOR_PIVOT_STATUS.md`
- `docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md`
- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`
- `outputs/verification/MP1-V001/verification_matrix.json`

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **Vòng thẩm tra:** MP1-V001
- **Phán quyết tổng thể:** `PIVOT_TO_MECHANICS_CORE` [AUDIT VERDICT]
- **Độ tin cậy:** `high` [AUDIT VERDICT]
- **Kiến trúc ứng viên (Candidate architecture):**
  > Bó dây kim loại / NiTi siêu đàn hồi chịu áp suất giam giữ dương (positive-pressure confinement), tạo hiện tượng nghẽn ma sát giữa các dây (inter-wire frictional jamming), thay đổi độ cứng uốn (variable bending stiffness), kết hợp nguồn tạo áp suất nhỏ gọn tùy chọn bằng piston/xi-lanh dẫn động bởi SMA (compact SMA-driven syringe/piston pressure source).

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Claim/Target | Paper | DOI | paper_id | Page(s) | Evidence type | Finding |
|---|---|---|---|---|---|---|---|
| W01-E01 | C1: Wire/fiber jamming novelty | Bai et al. 2022; Zhang & Yao 2026 | 10.3390/app12073582; 10.5194/ms-17-481-2026 | 240fbf6022; 3aa8790db0 | Bai: 8; Zhang: 1, 9–11 | Experimental / Analytical | Wire/fiber jamming thay đổi độ cứng uốn đã được hiện thực hóa và mô hình hóa; C1 CLOSED. |
| W01-E02 | C2: Positive-pressure jamming novelty | Liu et al. 2021; Zhang & Yao 2026 | 10.1109/LRA.2021.3097255; 10.5194/ms-17-481-2026 | 182d854610; 3aa8790db0 | Liu: 1, 4; Zhang: 1, 3–4 | Experimental / Analytical | Áp suất dương để nghẽn hạt (granular) và nghẽn sợi (fiber) đạt dải áp suất cao đã có; C2 CLOSED. |
| W01-E03 | C3: SMA + jamming in same device | Takashima lineage (2022–2026); Matsumoto 2024 | 10.20965/jrm.2022.p0466; 10.1299/mej.24-00130 | 2cd907e77a; 7ce492505d; 99fe24da8b; d3b3b6963f | Takashima: 1–3, 5; Matsumoto: 1, 5 | Experimental / Prototype | Tích hợp SMA và jamming trong cùng cơ cấu thay đổi độ cứng đã có dòng phát triển 4 bài báo; C3 CLOSED. |
| W01-E04 | C4: Onboard/compact pressure source | Huynh et al. 2022; Wang et al. 2024 | 10.1016/j.sna.2022.113449; 10.1108/IR-11-2023-0305 | bbe88a0c04; c6a31066f8 | Huynh: 1, 7–8; Wang: 1, 5–8 | Experimental / Design | Bơm vi mô (micropump) tích hợp và cơ cấu piston vít-me nhỏ gọn cấp áp suất nghẽn đã có; C4 CLOSED. |
| W01-E05 | C5: NiTi wires as jamming medium | Bai 2022; Takashima 2022; Wang 2024; Zhang 2026 | Various | 240fbf6022; 2cd907e77a; c6a31066f8; 3aa8790db0 | Diverse | Boundary audit | Chưa có bài báo nào trong tập V001 dùng dây NiTi làm môi trường tự trượt ma sát trực tiếp; C5 OPEN trong tập tài liệu. |
| W01-E06 | C6: Positive pressure on NiTi bundle | Liu 2021; Zhang & Yao 2026 | 10.1109/LRA.2021.3097255; 10.5194/ms-17-481-2026 | 182d854610; 3aa8790db0 | Diverse | Boundary audit | Chưa có bài nào dùng áp suất dương giam giữ trực tiếp bó dây NiTi; C6 OPEN trong tập tài liệu. |
| W01-E07 | C7: Coupled NiTi-friction-pressure-stiffness | Zhang 2026; Takashima 2022; Matsumoto 2024; Wang 2024 | Various | 3aa8790db0; 2cd907e77a; 7ce492505d; c6a31066f8 | Diverse | Boundary audit | Chưa bài nào ghép cặp đồng thời cả 4 yếu tố: siêu đàn hồi NiTi, trượt ma sát giữa các dây, áp suất giam giữ, và độ cứng uốn; C7 OPEN. |
| W01-E08 | C8: SMA-driven syringe/piston for jamming | Pierce & Mascaro 2013; Kotb 2021; Huynh 2022; Wang 2024 | 10.1109/TMECH.2012.2211032; 10.3390/mi12050520 | de64029540; 55457a97c6; bbe88a0c04; c6a31066f8 | Pierce: 9–10; Kotb: 1, 12 | Experimental / Theoretical | Bơm SMA và piston jamming đã có; tích hợp cụ thể là thay thế cơ cấu chấp hành (actuator substitution); SUBSTANTIALLY_PREEMPTED. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W01-E01

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [VERIFIED PAPER FACT]

**Claim / Target:** C1 — Wire/fiber jamming để thay đổi độ cứng uốn (variable stiffness) là mới.

**Trạng thái thẩm tra:** `closed`

**Paper title(s):**
1. *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming* (Bai et al. 2022, paper_id: `240fbf6022`, DOI: `10.3390/app12073582`)
2. *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming* (Zhang & Yao 2026, paper_id: `3aa8790db0`, DOI: `10.5194/ms-17-481-2026`)

**Verification round:** MP1-V001

**Evidence JSON:**
- `data/evidence/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming_240fbf6022.json`
- `data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json`

**Original PDF:**
- `papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`
- `papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`

**Page(s) / Section:** Bai et al. p. 8; Zhang & Yao pp. 1, 9–11.

**Evidence type:** Experimental and analytical modeling.

### Thiết lập cơ học (Mechanical setup)
Bai et al. sắp xếp các bó dây sợi (kraft rope, hemp rope, nylon wire) trong khoang chân không dọc theo thân cơ cấu chấp hành mềm. Zhang & Yao sắp xếp 700 sợi nylon (đường kính 0.4 mm) trong khoang mắt xích in 3D kèm bóng khí nén dẹt bên trong.

### Mô hình / lý thuyết (Model / theory)
Bai et al. dùng lý thuyết dầm Euler–Bernoulli mô tả trạng thái tự do (các dầm độc lập) và trạng thái nghẽn (dầm composite nguyên khối). Zhang & Yao xây dựng khung lý thuyết 3 trạng thái: nghẽn hoàn toàn (jammed), chuyển tiếp (transition), và trượt hoàn toàn (slipping), dựa trên phân bố ứng suất cắt parabol và ma sát Coulomb.

### Phương pháp thí nghiệm (Experimental method)
Bai et al. thí nghiệm uốn công-xôn ở các mức áp suất chân không từ 0 đến -85 kPa. Zhang & Yao thí nghiệm uốn 3 điểm (three-point bending) với áp suất dương từ 0 đến 300 kPa.

### Kết quả định lượng (Quantitative results)
- Bai et al. (p. 8): Bó dây kraft 8 mm tăng độ cứng uốn gần 7 lần (đạt 0.89 N/mm ở độ võng 15 mm) khi chuyển từ 0 kPa sang -85 kPa.
- Zhang & Yao (pp. 9–11): Lực cắt chuyển tiếp và độ cứng trạng thái trượt tăng tuyến tính với áp suất giam giữ từ 0 đến 300 kPa.

### Bằng chứng này chứng minh điều gì (What this proves)
Hiện tượng nghẽn ma sát giữa các sợi/dây (wire/fiber jamming) để điều chỉnh độ cứng uốn đã được chứng minh thực nghiệm và mô hình hóa giải tích đầy đủ. Claim C1 không còn tính mới.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Các bài báo này không sử dụng dây hợp kim nhớ hình NiTi siêu đàn hồi và không giải quyết bài toán ghép cặp chuyển pha cơ học trong bó dây.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Đóng hoàn toàn claim rộng về "wire jamming for variable stiffness".

---

### EVIDENCE W01-E02

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [VERIFIED PAPER FACT]

**Claim / Target:** C2 — Positive-pressure jamming để thay đổi độ cứng uốn là mới.

**Trạng thái thẩm tra:** `closed`

**Paper title(s):**
1. *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots* (Liu et al. 2021, paper_id: `182d854610`, DOI: `10.1109/LRA.2021.3097255`)
2. *A variable stiffness omnidirectional chain based on positive-pressure fiber jamming* (Zhang & Yao 2026, paper_id: `3aa8790db0`, DOI: `10.5194/ms-17-481-2026`)

**Verification round:** MP1-V001

**Evidence JSON:**
- `data/evidence/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots_182d854610.json`
- `data/evidence/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming_3aa8790db0.json`

**Original PDF:**
- `papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`
- `papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf`

**Page(s) / Section:** Liu et al. pp. 1, 4; Zhang & Yao pp. 1, 3–4.

**Evidence type:** Experimental and analytical.

### Thiết lập cơ học (Mechanical setup)
Liu et al. dùng bóng khí trung tâm bên trong lớp vỏ vải bọc hạt (granular chamber) để tạo áp suất nén hướng tâm ra ngoài. Zhang & Yao dùng bóng khí dẹt bên dưới bó sợi trong khoang cứng.

### Mô hình / lý thuyết (Model / theory)
Liu et al. lập mô hình dầm Euler–Bernoulli tiết diện vành khuyên và quan hệ mô-đun đàn hồi tương đương theo lực nén tiếp xúc trung bình. Zhang & Yao xây dựng mô hình cân bằng công - năng lượng với ma sát Coulomb phụ thuộc áp suất dương.

### Phương pháp thí nghiệm (Experimental method)
Liu et al. uốn công-xôn ở dải áp suất tương đối từ 68 kPa đến 172 kPa. Zhang et al. uốn 3 điểm từ 0 đến 300 kPa.

### Kết quả định lượng (Quantitative results)
- Liu et al. (pp. 1, 4): Độ cứng uốn tăng từ 0.69 N/mm lên 4.02 N/mm (tăng xấp xỉ 5.83 lần, [DERIVATION]: 4.02 / 0.69 = 5.826) khi áp suất tăng từ 68/69 kPa lên 172 kPa, tuyến tính với áp suất ($R^2 > 0.99$).
- Zhang & Yao (p. 1): Khắc phục hoàn toàn giới hạn 1 atm (100 kPa) của hút chân không, đạt áp suất làm việc 300 kPa.

### Bằng chứng này chứng minh điều gì (What this proves)
Áp suất dương dùng để nén chặt môi trường ma sát (hạt hoặc sợi) nhằm thay đổi độ cứng đã tồn tại rõ ràng trong tài liệu tiền nhiệm. Claim C2 không còn tính mới.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Không áp dụng trực tiếp lên bó dây kim loại hay vật liệu có hiệu ứng chuyển pha như NiTi.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Loại bỏ khả năng xác lập tính mới ở mức "positive-pressure jamming".

---

### EVIDENCE W01-E03

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [VERIFIED PAPER FACT]

**Claim / Target:** C3 — Kết hợp SMA và jamming trong cùng một thiết bị biến đổi độ cứng là mới.

**Trạng thái thẩm tra:** `closed`

**Paper title(s):** Dòng nghiên cứu Takashima (Takashima et al. 2022, 2024, 2026; Matsumoto et al. 2024). Đại diện chính:
*Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon* (Takashima et al. 2022, paper_id: `2cd907e77a`, DOI: `10.20965/jrm.2022.p0466`).

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json`

**Original PDF:** `papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf`

**Page(s) / Section:** pp. 1, 2, 3, 5, 8, 10.

**Evidence type:** Experimental prototype and characterization.

### Thiết lập cơ học (Mechanical setup)
Bốn dây NiTi SMA (đường kính 1.0 mm) đóng vai trò khung đỡ (backbone) và phục hồi hình dạng, bọc trong màng silicone chứa bã cà phê (coarse coffee grounds) làm môi trường nghẽn hạt (granular jamming).

### Mô hình / lý thuyết (Model / theory)
Kết hợp trạng thái nhiệt của SMA (pha martensite mềm ở nhiệt độ phòng, pha austenite cứng khi nung nóng bằng dòng điện) với trạng thái áp suất hút chân không của nghẽn hạt.

### Phương pháp thí nghiệm (Experimental method)
Đo độ cứng uốn ở 4 trạng thái kết hợp: (Unjammed + Martensite), (Unjammed + Austenite), (Jammed + Martensite), (Jammed + Austenite).

### Kết quả định lượng (Quantitative results)
Tạo ra 4 mức độ cứng riêng biệt; dây SMA giúp cơ cấu tự nâng trọng lượng bản thân khi unjammed (khắc phục nhược điểm võng do tự trọng của jamming hạt truyền thống) và phục hồi hình dạng nhanh hơn 4 lần so với dùng polymer nhớ hình (SMP).

### Bằng chứng này chứng minh điều gì (What this proves)
Ý tưởng đưa cả SMA và jamming vào trong cùng một kết cấu biến đổi độ cứng đã có tiền nhiệm trực tiếp với 4 bài báo công bố từ 2022 đến 2026. Claim C3 bị đóng.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Trong hệ thống của Takashima, các dây NiTi chỉ là lõi dẫn động/phục hồi hình dạng đặt chìm trong hạt, **không phải là các phần tử tự tiếp xúc và trượt ma sát lên nhau để tạo nghẽn**.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Phải phân biệt rạch ròi giữa: "SMA có mặt trong robot jamming" (đã có prior art) với "bản thân các dây NiTi là môi trường nghẽn ma sát" (hướng đi của MP1).

---

### EVIDENCE W01-E04

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [VERIFIED PAPER FACT]

**Claim / Target:** C4 — Nguồn áp suất tích hợp/nhỏ gọn (onboard/compact pressure source) cho jamming là mới.

**Trạng thái thẩm tra:** `closed`

**Paper title(s):**
1. *Soft actuator with switchable stiffness using a micropump-activated jamming system* (Huynh et al. 2022, paper_id: `bbe88a0c04`, DOI: `10.1016/j.sna.2022.113449`)
2. *Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm* (Wang et al. 2024, paper_id: `c6a31066f8`, DOI: `10.1108/IR-11-2023-0305`)

**Verification round:** MP1-V001

**Evidence JSON:**
- `data/evidence/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json`
- `data/evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json`

**Original PDF:**
- `papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`
- `papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf`

**Page(s) / Section:** Huynh et al. pp. 1, 6–8; Wang et al. pp. 1, 5–8.

**Evidence type:** Experimental prototype demonstration.

### Thiết lập cơ học (Mechanical setup)
- Huynh et al.: Tích hợp bơm vi mô chất lỏng điện liên hợp (ECF micropump) hai chiều dẻo gắn trực tiếp trên thân cơ cấu chấp hành mềm.
- Wang et al.: Động cơ bước mini kết hợp cơ cấu trục vít - đai ốc bi (ball screw) đẩy piston ép hạt cơ học bên trong cánh tay robot mềm.

### Mô hình / lý thuyết (Model / theory)
- Huynh: Bơm ECF tạo áp suất tĩnh thủy tĩnh hai chiều $\pm 55\text{ kPa}$ điều khiển bởi điện trường cao áp ($2.5\text{ kV}$).
- Wang: Chuyển động quay của động cơ chuyển thành lực nén dọc trục của piston lên khối hạt jamming (lên tới $150\text{ N}$).

### Phương pháp thí nghiệm (Experimental method)
- Huynh: Đo lực kháng uốn đầu ngọn (tip force) và góc uốn tự do.
- Wang: Thí nghiệm uốn tĩnh và động trên cánh tay robot đa phân đoạn.

### Kết quả định lượng (Quantitative results)
- Huynh et al. (pp. 7–8): Áp suất chân không $-50\text{ kPa}$ từ bơm vi mô làm tăng lực kháng uốn từ $0.134\text{ N}$ lên $0.743\text{ N}$ tại độ võng $3\text{ mm}$ (tăng độ cứng $5.5$ lần), mang được tải $130\text{ g}$ (gấp $5.2$ lần tự trọng $25\text{ g}$).
- Wang et al. (p. 8): Tỷ số tăng cứng đạt từ $6$ đến trên $25$ lần với lực nén $150\text{ N}$.

### Bằng chứng này chứng minh điều gì (What this proves)
Các giải pháp nguồn áp suất hoặc cơ cấu nén nhỏ gọn, tích hợp sẵn trên robot để tạo trạng thái nghẽn đã được công bố dưới nhiều dạng (bơm vi mô ECF, piston cơ khí). Claim C4 bị đóng ở cấp độ ý tưởng nguồn áp suất nhỏ gọn.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Các công trình này không dùng cơ cấu piston xi-lanh dẫn động bằng dây SMA nén thủy tĩnh lên bó dây kim loại.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Việc chỉ đưa một nguồn bơm/áp suất nhỏ gọn vào hệ thống không thể đứng độc lập như một đóng góp khoa học chính.

---

### EVIDENCE W01-E05 / W01-E06 / W01-E07 / W01-E08

**Phân loại (Classification):** [AUDIT VERDICT] kết hợp [INFERENCE]

**Claim / Target:** C5, C6, C7 (Vùng mở trong V001) và C8 (Bị đón đầu thực chất).

**Trạng thái thẩm tra:**
- C5: `open_in_supplied_corpus`
- C6: `open_in_supplied_corpus`
- C7: `open_in_supplied_corpus`
- C8: `substantially_preempted`

**Audit source:** `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`, mục `claim_audit`.

**Tóm tắt lập luận của Audit:**
1. **C5 & C6:** Không bài báo nào trong số 11 bài của V001 cho thấy bó dây NiTi siêu đàn hồi tự nó chịu áp suất nén dương để trượt ma sát nghẽn. Tuy nhiên, việc thay đổi vật liệu từ nylon sang NiTi đơn thuần không tạo nên tính mới khoa học nếu không kéo theo một bài toán cơ học mới.
2. **C7:** Ghép cặp đa trường (siêu đàn hồi NiTi $\times$ trượt ma sát giữa các dây $\times$ áp suất giam giữ $\times$ độ cứng uốn) hoàn toàn chưa có trong tập dữ liệu. Đây là giả thuyết khoa học duy nhất có tiềm năng phòng thủ được.
3. **C8:** Bơm dẫn động bằng SMA (Pierce & Mascaro 2013, paper_id: `de64029540`; Kotb et al. 2021, paper_id: `55457a97c6`) và nghẽn bằng piston (Wang 2024, paper_id: `c6a31066f8`) đã tồn tại. Việc lắp SMA vào piston ép jamming chỉ là thay thế linh kiện dẫn động (actuator substitution), không có hiện tượng cơ học mới phát sinh nếu xét riêng nguồn ép.

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Sự sụp đổ của tính mới cấp độ tổ hợp linh kiện (Architecture-level novelty collapse):**  
  [AUDIT VERDICT] Vòng MP1-V001 đã chứng minh không thể bảo vệ tính mới của ý tưởng mentor bằng cách kết hợp cơ học thuần túy: wire jamming đã có (Bai 2022), positive-pressure jamming đã có (Liu 2021, Zhang 2026), SMA + jamming đã có (Takashima 2022–2026), nguồn áp suất onboard đã có (Huynh 2022, Wang 2024), và bơm SMA đã có (Pierce 2013, Kotb 2021).
- **Lý do dẫn tới phán quyết `PIVOT_TO_MECHANICS_CORE`:**  
  [INFERENCE] Nếu loại bỏ các thành phần đã biết, phần duy nhất chưa bị tài liệu tiền nhiệm giải quyết là bài toán cơ học: *Dưới áp suất giam giữ dương thay đổi chủ động, ứng xử chuyển pha của NiTi tương tác với ma sát tiếp xúc giữa các dây như thế nào để chi phối quá trình dính–trượt (stick-slip) và độ cứng uốn?* Do đó, MP1 buộc phải từ bỏ việc tự xưng là "thiết bị/robot mới" và chuyển trọng tâm sang giải quyết câu hỏi cơ học cốt lõi (mechanics core).

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Vòng MP1-V001 mới chỉ xem xét tập 11 bài báo hạt nhân ban đầu. Việc C5, C6, C7 ở trạng thái `open_in_supplied_corpus` chỉ là kết quả bị chặn bởi tập tài liệu (protocol-bounded finding), tuyệt đối không phải bằng chứng chứng minh tính mới phổ quát (universal novelty).
- Chưa kiểm tra các nhánh tài liệu chuyên sâu về cáp bện NiTi (NiTi wire ropes/cables) trong cơ học kết cấu và kỹ thuật giảm chấn.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Kiểm tra lại xem trong 11 bài báo của MP1-V001 có bất kỳ chi tiết tiềm ẩn nào về việc dây NiTi đóng vai trò bề mặt tiếp xúc ma sát trực tiếp chịu áp suất hay không (đặc biệt là bài Wang et al. 2024 khi các dây chằng NiTi chạy quanh lõi hạt).
2. Đánh giá tính xác đáng của việc phân loại C8 là `substantially_preempted` thay vì `closed` hoàn toàn: liệu có bất kỳ sự ghép cặp nhiệt - cơ - thủy lực phi tuyến nào giữa bơm SMA và buồng nghẽn có thể tạo ra đóng góp khoa học hay không?

## 9. Danh mục kiểm tra xác minh gói bằng chứng (Packet verification checklist)

- [x] Tiêu đề bài báo được xác minh nguyên văn tiếng Anh (paper title verified)
- [x] Tác giả và năm xuất bản được đối chiếu (authors/year verified)
- [x] DOI được xác minh từ tệp bằng chứng (DOI verified)
- [x] Mã định danh bài báo paper_id khớp chính xác với registry (paper_id verified)
- [x] Đường dẫn tệp evidence JSON được xác minh tồn tại trên đĩa (evidence JSON path verified)
- [x] Đường dẫn tệp PDF gốc được đối chiếu (PDF path verified)
- [x] Các số liệu định lượng có số trang kiểm chứng (quantitative claims page-verified)
- [x] Các cơ chế cơ học có số trang kiểm chứng (mechanical claims page-verified)
- [x] Phán quyết audit được phân biệt rõ với sự kiện bài báo (audit verdict separated from paper fact)
- [x] Các nhận định suy luận được gắn nhãn [INFERENCE] / [DERIVATION] rõ ràng (inference explicitly labelled)
- [x] Mục “What it does NOT prove” được điền đầy đủ cho từng nguồn (What it does NOT prove completed)
- [x] Các điểm chưa giải quyết hoặc giới hạn được công khai minh bạch (unresolved issues disclosed)
