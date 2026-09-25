# W03 — Kiểm chứng Chuyên sâu Dòng Nghiên cứu SMA Kết hợp Jamming (C3)

## 1. Mục tiêu (Mission)

Thẩm tra chuyên sâu toàn văn (deep full-text audit) phát biểu C3:
> "Kết hợp SMA và jamming trong cùng một thiết bị biến đổi độ cứng (variable-stiffness device) là mới."

Nhiệm vụ trọng tâm:
1. Phân tích tường minh sự tiến hóa của dòng nghiên cứu Takashima (Takashima lineage: 2022, 2024, 2026) và Matsumoto et al. (2024).
2. Phân biệt rạch ròi hai khái niệm bản chất:
   - **SMA tồn tại bên trong thiết bị jamming** (*SMA exists inside jamming device*);
   - **Bản thân các dây NiTi là môi trường nghẽn ma sát** (*NiTi wires themselves are the jamming medium*).
3. Trích xuất đầy đủ: cấu trúc hình học, vai trò của SMA, vai trò của nghẽn hạt (granular jamming), nguồn áp suất, 4 trạng thái độ cứng, thiết lập thực nghiệm, số liệu định lượng và số trang kiểm chứng.
4. Làm rõ vì sao C3 bị đóng (`closed`) và điều gì còn lại mở cho bài toán cơ học tiếp xúc của MP1.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `data/evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json`
- `data/evidence/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json`
- `data/evidence/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json`
- `data/evidence/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json`
- `papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf`
- `papers/verification/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf`
- `papers/verification/MP1-V001/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf`
- `papers/verification/MP1-V001/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf`

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **C3 (SMA + jamming in same device):** `closed` [AUDIT VERDICT] (nguồn: `CORE_PRIOR_ART_AUDIT.json`)
- **Độ tin cậy:** `high` [AUDIT VERDICT]

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Claim/Target | Paper | DOI | paper_id | Page(s) | Evidence type | Finding |
|---|---|---|---|---|---|---|---|
| W03-E01 | C3 | Takashima et al. 2022 | 10.20965/jrm.2022.p0466 | 2cd907e77a | 1–3, 5–8, 10 | Experimental / Prototype | Đề xuất cơ cấu tích hợp 4 dây NiTi SMA và bã cà phê; tạo 4 trạng thái độ cứng; giữ tải chết 2 kg; C3 CLOSED. |
| W03-E02 | C3 | Matsumoto et al. 2024 | 10.1299/mej.24-00130 | 7ce492505d | 1–3, 5, 8–10 | Experimental | Khảo sát biến đổi pha R của dây Ti-Ni trong cơ cấu jamming; tốc độ phục hồi đạt 2.5 mm/s; huấn luyện chu kỳ giảm dẻo. |
| W03-E03 | C3 | Takashima et al. 2024 | 10.20965/jrm.2024.p0470 | 99fe24da8b | 1–3, 5–7 | Experimental / Prototype | Đánh giá chuyển động biến dạng và cố định hình dạng bằng khuôn ngoài kết hợp dây SMA phục hồi. |
| W03-E04 | C3 | Takashima et al. 2026 | 10.20965/jrm.2026.p0646 | d3b3b6963f | 1–3, 5–8, 10 | Experimental / Robotics | Hệ thống hai tay robot gắp thả tự động; mang tải 990 g (651% tự trọng); chu kỳ bền >500 lần; khuôn đổi trong 4.7 s. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W03-E01

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C3 — SMA and jamming in the same variable-stiffness device is novel.

**Paper title:** *Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon*

**Authors:** Kazuto Takashima, Toshiki Imazawa, Hiroki Cho

**Year:** 2022

**DOI:** `10.20965/jrm.2022.p0466`

**paper_id:** `2cd907e77a`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon_2cd907e77a.json`

**Original PDF:** `papers/verification/MP1-V001/2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf`

**Page(s) / Section:** Trang 1, 2, 3, 5, 6, 7, 8, 10; Section 2 (Concept and Structure), Section 3 (Experiments).

**Evidence type:** Experimental prototype and characterization.

### Thiết lập cơ học (Mechanical setup)
- Kết cấu thân nối biến đổi độ cứng (variable-stiffness link): Tác giả chế tạo hai nguyên mẫu:
  - Nguyên mẫu 1 (Prototype 1): Tấm polymer nhớ hình (SMP sheets) đặt ở tâm màng silicone chứa bã cà phê (coffee grounds).
  - Nguyên mẫu 2 (Prototype 2): Bốn dây hợp kim nhớ hình NiTi SMA tròn (đường kính $1.0\text{ mm}$) đặt đối xứng dọc theo chiều dài liên kết, bọc trong màng cao su chứa bã cà phê (pp. 2, 3).
- Vai trò của SMA: Đóng vai trò bộ xương chịu tải (structural backbone) và bộ phận sinh lực phục hồi hình dạng ban đầu khi được nung nóng bằng dòng điện Joule.
- Vai trò của Jamming: Khối bã cà phê chịu áp suất hút chân không (dưới $-90\text{ kPa}$) sẽ chuyển pha từ trạng thái lỏng linh hoạt sang trạng thái rắn đặc khít, khóa chặt hình dạng biến dạng uốn bất kỳ mà không cần duy trì nguồn nhiệt (pp. 1, 2).

### Mô hình / lý thuyết (Model / theory)
- Khái niệm 4 trạng thái độ cứng rời rạc (four stiffness states, pp. 2, 3):
  1. **Trạng thái 1 (Mềm nhất):** Hạt unjammed (áp suất khí quyển) + SMA ở pha Martensite (nhiệt độ phòng) $\rightarrow$ Khớp mềm dẻo, dễ biến dạng theo vật thể.
  2. **Trạng thái 2:** Hạt unjammed + SMA ở pha Austenite (nung nóng trên $A_f$) $\rightarrow$ Độ cứng trung bình thấp, lực phục hồi đưa liên kết về hình dạng thẳng ban đầu.
  3. **Trạng thái 3:** Hạt jammed (hút chân không) + SMA ở pha Martensite $\rightarrow$ Độ cứng cao, cố định hình dạng thụ động không tốn năng lượng nhiệt.
  4. **Trạng thái 4 (Cứng nhất):** Hạt jammed + SMA ở pha Austenite $\rightarrow$ Độ cứng cực đại, khả năng chịu tải va đập và tải tĩnh cao nhất.

### Phương pháp thí nghiệm (Experimental method)
- Thí nghiệm uốn tĩnh cantilever tip loading: đo lực kháng uốn và biến dạng trong cả hai phương đứng và ngang (pp. 5, 6).
- Thử nghiệm duy trì tải chết (dead load): treo tải $2\text{ kg}$ ở đầu ngọn dầm trong 1 giờ để kiểm tra độ từ biến (creep) (pp. 7, 8).
- Thử nghiệm phục hồi hình dạng và uốn lặp chu kỳ 10 lần (pp. 7, 8).
- Thử nghiệm ứng dụng gắp 5 vật thể thực tế có hình học đa dạng (cờ-lê, lò xo, bút, nắp bình xịt) (pp. 9, 10).

### Kết quả định lượng (Quantitative results)
- Nguyên mẫu 2 (dùng dây SMA) có độ cứng cao hơn đáng kể so với Nguyên mẫu 1 (dùng SMP); ở trạng thái unjammed, độ cứng khớp với dự báo mô hình dầm martensite là $0.13\text{ N/mm}$ (p. 5).
- Cả hai nguyên mẫu khắc phục hoàn toàn nhược điểm võng do tự trọng (self-weight sag) của các tay máy nghẽn hạt truyền thống, có khả năng tự giữ thẳng theo phương ngang khi unjammed (pp. 5, 6, 10).
- Dây SMA giúp phục hồi hình dạng với thời gian chỉ bằng $0.24$ lần (nhanh hơn gấp 4 lần) so với dùng tấm SMP (pp. 7, 8).
- Giữ vững tải trọng $2\text{ kg}$ ở đầu ngọn trong 1 giờ với độ võng bổ sung không đáng kể sau biến dạng đàn hồi ban đầu, chứng minh độ khóa hình dạng xuất sắc (pp. 7, 8).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh trực tiếp rằng ý tưởng tích hợp SMA và jamming trong cùng một thiết bị biến đổi độ cứng đã được công bố từ năm 2022, giải quyết trọn vẹn cả bài toán 4 mức độ cứng và phục hồi hình dạng.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Trong bài báo này, các hạt bã cà phê là môi trường nghẽn duy nhất tạo ma sát.
- **Bốn dây NiTi SMA hoàn toàn không trượt ma sát lên nhau**; chúng hoạt động độc lập như 4 thanh dầm uốn đặt cách xa nhau trong nền hạt. Do đó, paper này không hề nghiên cứu sự nghẽn ma sát nội tại của chính bó dây NiTi (NiTi inter-wire jamming).

### Ý nghĩa đối với MP1 (Relevance to MP1)
Khẳng định chắc chắn C3 đã bị đóng ở cấp độ tổ hợp hệ thống (device-level combination). Bất kỳ nỗ lực nào tuyên bố tính mới từ việc "kết hợp SMA với jamming" đều sẽ bị các phản biện viện dẫn Takashima 2022 để bác bỏ ngay lập tức.

---

### EVIDENCE W03-E02

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C3 — Ti-Ni SMA phase behavior in jamming mechanisms.

**Paper title:** *Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon*

**Authors:** Naoki Matsumoto, Hiroki Cho, Kazuto Takashima, Hidetaka Suzuki

**Year:** 2024

**DOI:** `10.1299/mej.24-00130`

**paper_id:** `7ce492505d`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon_7ce492505d.json`

**Original PDF:** `papers/verification/MP1-V001/2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf`

**Page(s) / Section:** Trang 1, 2, 3, 5, 6, 8, 9, 10; Section 2 (Material Characteristics), Section 3 (Recovery Speed Analysis), Section 4 (Device Implementation).

**Evidence type:** Material characterization and prototype validation.

### Thiết lập cơ học (Mechanical setup)
Nghiên cứu sâu về dây Ti-Ni SMA tích hợp trong cơ cấu biến đổi độ cứng bằng nghẽn hạt (coffee grounds). Khảo sát ảnh hưởng của xử lý nhiệt tạo biến đổi pha trung gian R-phase (R-phase transformation) lên tốc độ và lực phục hồi hình dạng khi ngắt chân không unjamming.

### Mô hình / lý thuyết (Model / theory)
- Tốc độ phục hồi hình dạng được dẫn xuất phụ thuộc vào ứng suất phục hồi ban đầu $\sigma_A$ và độ cứng tiếp tuyến trong quá trình phục hồi nghịch $E_{A2}$, trong đó $E_{A2}$ đóng vai trò chi phối áp đảo (pp. 5, 6, 10).
- Huấn luyện cơ học siêu đàn hồi (cyclic training) 50 chu kỳ ở biến dạng 3% tại 353 K nhằm triệt tiêu biến dạng dẻo tích lũy (plastic strain).

### Phương pháp thí nghiệm (Experimental method)
- Thí nghiệm kéo tĩnh và đo nhiệt sai biệt (DSC) trên các mẫu dây Ti-Ni xử lý nhiệt khác nhau (773 K trong 0.3 ks so với dây thương mại Nilaco) (pp. 2, 3).
- Đo vận tốc phục hồi góc uốn và hành trình đầu ngọn bằng camera tốc độ cao khi đốt nóng bằng dòng điện (pp. 5, 6).

### Kết quả định lượng (Quantitative results)
- Dây SMA có chuyển pha R-phase đạt vận tốc phục hồi $\sim 2.4 - 2.5\text{ mm/s}$, vượt trội so với dây không có R-phase ($\sim 0.6 - 1.3\text{ mm/s}$) (pp. 1, 5, 6).
- Huấn luyện cơ học làm giảm biến dạng dẻo dư từ $0.37\%$ xuống còn $0.03\%$ (giảm hơn 10 lần), giúp cơ cấu phục hồi hình dạng gần như hoàn hảo mà không làm suy giảm ứng suất phục hồi (pp. 1, 8, 9, 10).

### Bằng chứng này chứng minh điều gì (What this proves)
Cho thấy cộng đồng nghiên cứu đã đi sâu đến cấp độ luyện kim vi cấu trúc và động học chuyển pha (R-phase kinetics) của dây NiTi bên trong các cơ cấu biến đổi độ cứng bằng jamming.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Không có ma sát tiếp xúc giữa các dây NiTi; cơ chế jamming vẫn là nghẽn hạt bã cà phê.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Khẳng định một lần nữa rằng hành vi pha của NiTi bên trong robot jamming đã có lịch sử nghiên cứu thực nghiệm chi tiết.

---

### EVIDENCE W03-E03 & W03-E04

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C3 — Dòng tiến hóa ứng dụng của hệ thống Takashima (2024–2026).

**Paper title(s):**
1. *Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon* (Takashima et al. 2024, paper_id: `99fe24da8b`, DOI: `10.20965/jrm.2024.p0470`).
2. *Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon* (Takashima et al. 2026, paper_id: `d3b3b6963f`, DOI: `https://doi.org/10.20965/jrm.2026.p0646`).

**Verification round:** MP1-V001

**Evidence JSON:**
- `data/evidence/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon_99fe24da8b.json`
- `data/evidence/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon_d3b3b6963f.json`

**Original PDF:**
- `papers/verification/MP1-V001/2024-Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon.pdf`
- `papers/verification/MP1-V001/2026-Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon.pdf`

**Page(s) / Section:**
- Takashima 2024: pp. 1, 2, 3, 5, 6, 7.
- Takashima 2026: pp. 1, 2, 3, 5, 6, 7, 8, 9, 10.

**Evidence type:** Robotic system integration and operational benchmarking.

### Tiến trình dòng nghiên cứu (Lineage progression)
1. **Takashima et al. 2022:** Xác lập nguyên lý cơ cấu lai (hybrid concept), 4 trạng thái độ cứng, giải quyết bài toán võng do tự trọng.
2. **Matsumoto et al. 2024:** Tối ưu hóa luyện kim pha R-phase cho dây SMA để tăng tốc độ phục hồi lên 2.5 lần và triệt tiêu biến dạng dẻo tích lũy.
3. **Takashima et al. 2024:** Đưa vào phương pháp ép khuôn định hình ngoài (mold pressing) để định hình tiết diện thân nối ăn khớp với vật thể, tăng diện tích tiếp xúc truyền tải.
4. **Takashima et al. 2026:** Tự động hóa hoàn toàn hệ thống với hai cánh tay robot công nghiệp (Dobot Magician); Tay I mang thân nối biến đổi độ cứng, Tay II xoay cụm đa khuôn (multi-mold) tự động.
   - Trọng lượng cơ cấu: $152\text{ g}$ (chứa 4 dây NiTi đường kính $1.0\text{ mm}$, điện trở $0.46\ \Omega$, và $26\text{ g}$ bã cà phê).
   - Tải trọng nâng thành công: $990\text{ g}$, tương đương **$651\%$ trọng lượng bản thân thân nối** (pp. 1, 7, 8).
   - Thời gian đổi khuôn tự động giảm $94\%$ xuống còn $4.7\text{ s}$ (pp. 1, 5, 6).
   - Duy trì độ ổn định hình học qua hơn **500 chu kỳ gắp thả liên tục** (p. 8).

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Sự khác biệt bản chất bắt buộc phải ghi nhận (Mandatory Distinction):**
  - **Dòng Takashima (Prior art đã giải quyết):**  
    $$\text{Dây NiTi} = \text{Cốt chịu lực / Truyền động nhiệt phục hồi} \quad \text{đặt trong} \quad \text{Nghẽn hạt (Granular Jamming)}$$
    $\rightarrow$ Không có ma sát tiếp xúc giữa các dây NiTi.
  - **Kiến trúc MP1 (Khoảng mở cơ học):**  
    $$\text{Bản thân các dây NiTi siêu đàn hồi} = \text{Môi trường nghẽn ma sát trực tiếp (Inter-wire Frictional Jamming)}$$
    $\rightarrow$ Các dây NiTi tự nén ép, tiếp xúc và trượt dính–trượt lên nhau dưới áp suất giam giữ chủ động.
- **Phán quyết thẩm tra (Audit Verdict):**  
  [AUDIT VERDICT] Claim C3 ("SMA and jamming in the same device is novel") bị **`closed` hoàn toàn** do sự tồn tại của dòng nghiên cứu Takashima 2022–2026.
- **Suy luận khoa học (Worker Inference):**  
  [INFERENCE] MP1 không được phép biện hộ tính mới bằng việc "robot của tôi có cả SMA lẫn jamming". Điểm khác biệt duy nhất có thể bảo vệ được là: dây NiTi trong MP1 chính là các phần tử ma sát tạo nghẽn, và bài toán cần giải quyết là cơ học trượt tương đối giữa các dây chuyển pha dưới áp suất ngoài.

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Dòng Takashima hoàn toàn không đo đạc lực ma sát tiếp xúc giữa dây kim loại với dây kim loại.
- Không có bất kỳ mô hình cơ học vi mô (micro-mechanical contact model) nào về tương tác tiếp xúc nhiều vật thể (multi-body contact) giữa các sợi dây trong các công trình này.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Trong bài Takashima et al. 2026 hoặc 2022, liệu có bất kỳ sự tiếp xúc cục bộ nào giữa 4 dây NiTi khi thân nối bị uốn ở góc lớn (ví dụ uốn $90^\circ$ hoặc biến dạng tiết diện sâu do khuôn ép) hay các dây luôn được ngăn cách bởi lớp hạt cà phê?
2. Có thể trích xuất được bất kỳ dữ liệu nào về hệ số ma sát giữa màng silicone/hạt cà phê với bề mặt dây NiTi từ các bài báo này để làm thông số tham chiếu hay không?

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
