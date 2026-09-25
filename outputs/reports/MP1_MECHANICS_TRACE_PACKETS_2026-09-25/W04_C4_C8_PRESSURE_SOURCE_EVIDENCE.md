# W04 — Bằng chứng Kiểm chứng Nguồn Áp suất Tích hợp và Cơ cấu Piston SMA (C4 & C8)

## 1. Mục tiêu (Mission)

Thẩm tra chi tiết bằng chứng toàn văn đối với hai phát biểu liên quan đến nguồn tạo áp suất:
- **C4:** Nguồn áp suất tích hợp/nhỏ gọn (onboard/compact pressure source) cho jamming là mới.
- **C8:** Cơ cấu xi-lanh/piston dẫn động bằng SMA chuyên dụng để cấp áp suất nghẽn (SMA-driven syringe/piston powering jamming pressure) là mới.

Nhiệm vụ trọng tâm:
1. Tổng hợp tài liệu tiền nhiệm về bơm vi mô tích hợp (integrated micropump), nghẽn hạt bằng piston cơ khí (piston-jamming), và bơm dẫn động bằng hợp kim nhớ hình SMA (SMA robotic pumps / micropumps).
2. Xác định rõ cấu hình topo chính xác nào còn thiếu trong tài liệu tiền nhiệm.
3. Giải thích logic thẩm tra: vì sao C4 bị đóng hoàn toàn (`closed`), trong khi C8 được phân loại là bị đón đầu thực chất (`substantially_preempted`) thay vì đóng trực tiếp.
4. Phân tích rủi ro thay thế cơ cấu chấp hành (actuator-substitution risk) và vì sao C8 không thể đóng vai trò đóng góp khoa học độc lập của luận văn.

## 2. Các tệp chuẩn đã đọc (Canonical files read)

- `docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `data/evidence/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json`
- `data/evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json`
- `data/evidence/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json`
- `data/evidence/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json`
- `papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`
- `papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf`
- `papers/verification/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf`
- `papers/verification/MP1-V001/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf`

## 3. Trạng thái có thẩm quyền hiện tại (Current authoritative status)

- **C4 (Onboard/compact pressure source):** `closed` [AUDIT VERDICT] (nguồn: `CORE_PRIOR_ART_AUDIT.json`)
- **C8 (SMA-driven syringe/piston):** `substantially_preempted` [AUDIT VERDICT] (nguồn: `CORE_PRIOR_ART_AUDIT.json`)
- **Độ tin cậy:** `high` [AUDIT VERDICT]

## 4. Bảng bằng chứng (Evidence table)

| Evidence ID | Claim/Target | Paper | DOI | paper_id | Page(s) | Evidence type | Finding |
|---|---|---|---|---|---|---|---|
| W04-E01 | C4 | Huynh et al. 2022 | 10.1016/j.sna.2022.113449 | bbe88a0c04 | 1, 6–8, 10 | Experimental / Design | Bơm vi mô ECF dẻo gắn trực tiếp trên robot mềm, tạo áp suất $\pm 55\text{ kPa}$, nghẽn $-50\text{ kPa}$ tăng cứng 5.5 lần; C4 CLOSED. |
| W04-E02 | C4 | Wang et al. 2024 | 10.1108/IR-11-2023-0305 | c6a31066f8 | 1, 5, 8 | Experimental / Design | Cụm động cơ + trục vít bi + piston nhỏ gọn ép hạt jamming $150\text{ N}$, tăng cứng 6–25 lần; C4 CLOSED. |
| W04-E03 | C8 | Pierce & Mascaro 2013 | 10.1109/TMECH.2012.2211032 | de64029540 | 1, 3, 8–10 | Experimental / Modeling | Bơm robot màng dẻo dẫn động bởi dây SMA ướt, lưu lượng $66\text{ mL/min}$, tỷ số thể tích ra/vào 2.1; tiền nhiệm bơm SMA. |
| W04-E04 | C8 | Kotb et al. 2021 | 10.3390/mi12050520 | 55457a97c6 | 1, 3–6, 12–13 | Experimental / Modeling | Bơm vi mô vỏ nang đàn hồi dẫn động bằng lò xo SMA, hành trình $5.6\text{ mm}$, cột áp tĩnh $14\text{ kPa}$, lưu lượng $2524\ \mu\text{L/min}$. |

## 5. Hồ sơ bằng chứng chi tiết (Detailed evidence records)

### EVIDENCE W04-E01

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C4 — An onboard/compact pressure source for jamming is novel.

**Paper title:** *Soft actuator with switchable stiffness using a micropump-activated jamming system*

**Authors:** Van Hoang Huynh, Duc Dung Nguyen, Dinh Tuan Nguyen, Doyoung Byun, Ho-Sang Jung, Hyouk Ryeol Choi

**Year:** 2022

**DOI:** `10.1016/j.sna.2022.113449`

**paper_id:** `bbe88a0c04`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system_bbe88a0c04.json`

**Original PDF:** `papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`

**Page(s) / Section:** Trang 1, 6, 7, 8, 10; Section 2 (Design and Working Principle), Section 3 (Fabrication), Section 4 (Experimental Results).

**Evidence type:** Design, fabrication, and experimental demonstration.

### Thiết lập cơ học (Mechanical setup)
- Tích hợp trực tiếp một bơm vi mô dẻo hai chiều dựa trên hiệu ứng chất lỏng điện liên hợp (bidirectional flexible Electro-Conjugate Fluid — ECF micropump) gắn thẳng vào thân cơ cấu chấp hành mềm Pneu-Nets (pp. 1, 2, 3).
- Khoang nghẽn chứa các hạt nhôm oxit ($\text{Al}_2\text{O}_3$) kích thước $20\ \mu\text{m}$.
- Chế độ hoạt động kép (dual-mode operation): bơm tạo áp suất dương làm phồng khoang uốn chủ động, hoặc tạo áp suất âm (hút chân không) để kích hoạt nghẽn hạt thay đổi độ cứng (pp. 1, 10).

### Mô hình / lý thuyết (Model / theory)
- Dòng chảy phản lực ECF sinh ra từ cặp vi điện cực không đối xứng dưới điện áp cao ($2.5\text{ kV}$), biến đổi năng lượng điện trực tiếp thành áp suất thủy tĩnh mà không cần các chi tiết chuyển động cơ học (p. 4).

### Phương pháp thí nghiệm (Experimental method)
- Đo áp suất tĩnh và lưu lượng không tải của bơm vi mô trên mạch in dẻo polyimide (pp. 6, 7).
- Đo lực uốn đầu ngọn tại độ võng $3\text{ mm}$ ở trạng thái không nghẽn ($0\text{ kPa}$) và trạng thái nghẽn ($-50\text{ kPa}$) (pp. 7, 8).
- Thử nghiệm mang tải trọng tĩnh $130\text{ g}$ ở đầu ngọn (p. 8).

### Kết quả định lượng (Quantitative results)
- Bơm vi mô tạo áp suất tĩnh tối đa $\pm 55\text{ kPa}$ và lưu lượng không tải $140\text{ mm}^3/\text{s}$ ở điện áp $2.5\text{ kV}$ (pp. 1, 6, 7).
- Dưới áp suất chân không $-50\text{ kPa}$, lực kháng uốn đầu ngọn tại độ võng $3\text{ mm}$ tăng từ $0.134\text{ N}$ lên $0.743\text{ N}$, tương đương **độ cứng tăng gấp 5.5 lần** so với trạng thái tự do (pp. 1, 7, 8).
- Cơ cấu sau khi nghẽn giữ được quả cân $130\text{ g}$ (gấp **5.2 lần tự trọng** $25\text{ g}$ của toàn bộ cơ cấu), và nhả tải ngay khi ngắt điện áp (p. 8).

### Bằng chứng này chứng minh điều gì (What this proves)
Chứng minh rằng giải pháp nhúng trực tiếp nguồn áp suất kích thước nhỏ gọn (onboard flexible micropump) vào cơ cấu robot mềm để điều khiển nghẽn hạt đã được chế tạo và vận hành thành công. Claim C4 không còn tính mới.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Bơm ECF đòi hỏi nguồn điện áp cao ($2.5\text{ kV}$) và bình chứa chất lỏng ngoài, chưa hoàn toàn không dây (untethered).
- Không sử dụng piston cơ khí hay dây SMA để tạo áp suất.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Đóng hoàn toàn tính mới của ý tưởng "tích hợp bơm nhỏ gọn trên robot để tạo jamming".

---

### EVIDENCE W04-E02

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C4 (Compact pressure source) và C8 (Piston-jamming prior art).

**Paper title:** *Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm*

**Authors:** Tianlei Wang, Fei Ding, Zhenxing Sun

**Year:** 2024

**DOI:** `10.1108/IR-11-2023-0305`

**paper_id:** `c6a31066f8`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm_c6a31066f8.json`

**Original PDF:** `papers/verification/MP1-V001/2024-Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm.pdf`

**Page(s) / Section:** Trang 1, 5, 6, 7, 8; Section 2 (Design of Jamming System), Section 4 (Experiments).

**Evidence type:** Mechanism design and experimental benchmarking.

### Thiết lập cơ học (Mechanical setup)
- Cơ cấu nén hạt dạng piston cơ khí (piston-like particle jamming): Một động cơ DC mini kết hợp cụm trục vít - đai ốc bi (ball screw) điều khiển chuyển động tịnh tiến của đĩa piston bên trong buồng nghẽn hạt của cánh tay robot mềm đa phân đoạn (pp. 1, 2, 5).
- Các dây chằng siêu đàn hồi NiTi (superelastic NiTi tendons) được bố trí chạy dọc xung quanh lõi nghẽn hạt để kéo uốn phân đoạn cánh tay (p. 5).

### Mô hình / lý thuyết (Model / theory)
- Lực nén dọc trục của piston $F_{\text{piston}}$ nén trực tiếp lên môi trường hạt, tạo áp suất tiếp xúc nội tại nén chặt các hạt mà không cần màng hút chân không hay máy nén khí cồng kềnh (p. 2).

### Phương pháp thí nghiệm (Experimental method)
- Đo lực ép của piston (lên tới $150\text{ N}$) và phản lực uốn ngang, uốn bên, và xoắn của phân đoạn cánh tay robot (pp. 5, 6, 7).
- So sánh tỷ số tăng độ cứng (stiffening ratio) với các công nghệ nghẽn chân không và nghẽn lai khác (p. 8).

### Kết quả định lượng (Quantitative results)
- Cơ cấu piston tạo lực nén lên hạt lên tới $150\text{ N}$ (pp. 1, 8).
- Tỷ số tăng cứng uốn đạt từ $6$ đến trên **25 lần**, vượt trội hoàn toàn so với nghẽn hạt bằng chân không thông thường (chỉ đạt $\sim 3.35$ lần) và nghẽn lai ($\sim 5.5 - 7$ lần) (p. 8).
- Nâng cao đáng kể khả năng kháng xoắn của cánh tay robot khi uốn nghiêng (pp. 5, 8).

### Bằng chứng này chứng minh điều gì (What this proves)
1. C4 bị đóng: Cơ cấu nén áp suất kiểu piston nhỏ gọn tích hợp trực tiếp trên robot đã tồn tại.
2. C8 bị đe dọa nặng nề: Nguyên lý "dùng piston cơ học nén môi trường jamming để thay đổi độ cứng" đã được hiện thực hóa với hiệu năng tăng cứng rất cao ($\times 25$).

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
- Piston được dẫn động bằng động cơ điện quay và trục vít me bi, không phải dẫn động bằng dây SMA co rút nhiệt.
- Môi trường nghẽn là hạt (particles), không phải bó dây NiTi tự nghẽn.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Ý tưởng dùng piston để nén jamming không còn mới; nếu MP1 thay động cơ vít me bằng dây SMA, sự khác biệt chỉ nằm ở linh kiện dẫn động.

---

### EVIDENCE W04-E03

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C8 — SMA-driven pumping prior art.

**Paper title:** *A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump*

**Authors:** Matthew D. Pierce, Stephen A. Mascaro

**Year:** 2013

**DOI:** `10.1109/TMECH.2012.2211032`

**paper_id:** `de64029540`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json`

**Original PDF:** `papers/verification/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf`

**Page(s) / Section:** Trang 1, 3, 4, 8, 9, 10; Section II (System Concept), Section V (Experimental Results).

**Evidence type:** Theoretical thermodynamics and experimental fluidic pumping.

### Thiết lập cơ học (Mechanical setup)
- Bơm robot tự dẫn động lấy cảm hứng sinh học (wet SMA actuated pump): Dây SMA được bọc bên trong ống mềm chứa chất lỏng, cho phép đối lưu cưỡng bức nhiệt - thủy lực để làm mát và gia nhiệt nhanh (p. 1).
- Chuyển động co rút của dây SMA khi nung nóng tạo áp lực nén dòng chất lỏng qua van một chiều.

### Mô hình / lý thuyết (Model / theory)
- Mô hình đồ thị liên kết năng lượng (energy bond graphs) và đối lưu nhiệt rời rạc hóa kết hợp quan hệ cơ học biến đổi pha của SMA (pp. 4, 5).
- Hiệu suất nhiệt động lực học lý thuyết đạt cực đại $3.4\%$ dựa trên công riêng và ẩn nhiệt biến thái pha (pp. 4, 5).

### Phương pháp thí nghiệm (Experimental method)
- Đo tỷ số thể tích chất lỏng bơm ra so với thể tích kích hoạt (volumetric output-to-input ratio) dưới các điều kiện nung nóng bình tích áp (accumulator) và xung dòng điện Joule hỗ trợ ($4.5\text{ A}$ trong $1\text{ s}$) (pp. 8, 9).

### Kết quả định lượng (Quantitative results)
- Đạt lưu lượng chất lỏng dương thực $66\text{ mL/min}$, cao hơn hai bậc độ lớn so với các bơm vi mô SMA trước đó (p. 1).
- Tỷ số thể tích đầu ra trên đầu vào đạt cực đại $2.1$ khi kết hợp gia nhiệt liên tục và xung dòng điện (pp. 9, 10).
- Áp suất tĩnh cơ sở của bình tích áp đạt $15\text{ kPa}$ (p. 8).

### Bằng chứng này chứng minh điều gì (What this proves)
Dây SMA đã được sử dụng từ lâu (2013) để chế tạo bơm tạo áp suất chất lỏng dòng chảy dương cho các hệ thống robot.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Bơm này được dùng để tuần hoàn chất lỏng thủy lực truyền động, không cấp áp suất nén buồng nghẽn ma sát (jamming chamber).

### Ý nghĩa đối với MP1 (Relevance to MP1)
Chứng minh nguyên lý "dùng SMA để bơm tạo áp suất chất lỏng" đã là công nghệ tiền nhiệm kinh điển.

---

### EVIDENCE W04-E04

**Phân loại (Classification):** [VERIFIED PAPER FACT]

**Claim / Target:** C8 — SMA micropump prior art.

**Paper title:** *Shape Memory Alloy Capsule Micropump for Drug Delivery Applications*

**Authors:** Youssef Kotb, Islam Elgamal, Mohamed Serry

**Year:** 2021

**DOI:** `10.3390/mi12050520`

**paper_id:** `55457a97c6`

**Verification round:** MP1-V001

**Evidence JSON:** `data/evidence/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications_55457a97c6.json`

**Original PDF:** `papers/verification/MP1-V001/2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf`

**Page(s) / Section:** Trang 1, 3, 4, 5, 6, 12, 13; Section 2 (Design and Modeling), Section 4 (Testing).

**Evidence type:** Analytical modeling and experimental microfluidics.

### Thiết lập cơ học (Mechanical setup)
- Bơm vi mô dạng viên nang (capsule micropump) tích hợp lò xo NiTi SMA nén giãn dọc trục đặt trong vỏ silicone đàn hồi Ecoflex 00-30 kèm các van kiểm tra lá lật (bicuspid check valves) in 3D (pp. 1, 3, 4).
- Chuyển động co giãn dọc trục của lò xo SMA khi cấp dòng điện nén buồng chất lỏng tạo áp suất đẩy chất lỏng ra ngoài.

### Mô hình / lý thuyết (Model / theory)
- Mô hình hai trạng thái nhiệt - cơ kết hợp phương trình cấu thành Brinson của SMA và độ cứng phi tuyến của vỏ bọc silicone để xác định hành trình và ranh giới biến dạng dẻo (pp. 4, 5, 6).

### Phương pháp thí nghiệm (Experimental method)
- Đo hành trình dịch chuyển, lưu lượng thể tích, và cột áp tĩnh dưới các mức dòng điện kích hoạt từ $790\text{ mA}$ đến $1.9\text{ A}$ (pp. 10, 12).

### Kết quả định lượng (Quantitative results)
- Hành trình tối đa đạt $5.6\text{ mm}$ (tỷ số độ võng $27\%$), vận tốc kích hoạt lên tới $11\text{ mm/s}$ (pp. 1, 12).
- Cột áp tĩnh cực đại đạt $14\text{ kPa}$ ($105\text{ mmHg}$) và lưu lượng đỉnh $2524\ \mu\text{L/min}$ ở công suất $7.1\text{ W}$ (pp. 1, 12, 13).
- Chế độ điều khiển công tắc hành trình ở dòng $790\text{ mA}$ duy trì ổn định $43\text{ mm}^3$ mỗi hành trình với áp suất tĩnh $6.5\text{ kPa}$ (p. 12).

### Bằng chứng này chứng minh điều gì (What this proves)
Cơ cấu lò xo SMA nén đẩy thể tích chất lỏng tạo áp suất thủy tĩnh theo hành trình tuyến tính (tương đương xi-lanh/piston thu nhỏ) đã được công bố và mô hình hóa chi tiết.

### Bằng chứng này KHÔNG chứng minh điều gì (What this does NOT prove)
Bơm này được thiết kế để phân phối thuốc y tế, không nối vào buồng nghẽn ma sát biến đổi độ cứng.

### Ý nghĩa đối với MP1 (Relevance to MP1)
Củng cố nền tảng tiền nhiệm cho cơ cấu piston/xi-lanh màng nén dẫn động bằng SMA.

## 6. Kết luận về claim/target (Claim/target conclusion)

- **Cấu hình topo chính xác còn thiếu (The missing exact topology):**  
  [INFERENCE] Trong toàn bộ tập tài liệu, chưa từng có bài báo nào lắp ráp chính xác sơ đồ mạch:
  $$\text{Dây/Lò xo SMA} \longrightarrow \text{Cơ cấu piston/xi-lanh} \longrightarrow \text{Tạo áp suất thủy tĩnh dương} \longrightarrow \text{Giam giữ nén chặt bó dây kim loại/NiTi}$$
- **Vì sao C4 bị `closed` hoàn toàn?**  
  [AUDIT VERDICT] C4 là một phát biểu rộng về "nguồn áp suất nhỏ gọn/tích hợp cho jamming". Huynh et al. 2022 (bơm vi mô dẻo ECF tích hợp) và Wang et al. 2024 (cụm piston vít me tích hợp) đã giải quyết trực tiếp việc đưa nguồn tạo áp suất nhỏ gọn lên thân robot để kích hoạt jamming. Do đó, tính mới ở cấp độ ý tưởng này bị đóng hoàn toàn.
- **Vì sao C8 là `substantially_preempted` thay vì `closed` trực tiếp?**  
  [AUDIT VERDICT] C8 chỉ định một giải pháp cấu hình cụ thể: "xi-lanh/piston dẫn động bằng SMA chuyên cấp áp suất nghẽn". Do cụm liên kết cụ thể này chưa xuất hiện nguyên văn từng từ trong tài liệu, nó không bị bác bỏ trực tiếp kiểu `closed_by_full_text`. Tuy nhiên, vì cả 3 khối thành phần cấu tạo đều đã có tiền nhiệm sâu:
  1. Bơm SMA tạo áp lực chất lỏng đã có (Pierce 2013, Kotb 2021);
  2. Bơm nhỏ gọn gắn trên robot jamming đã có (Huynh 2022);
  3. Cơ cấu piston nén tạo jamming đã có (Wang 2024);
  nên C8 bị phân loại là `substantially_preempted`.
- **Rủi ro thay thế cơ cấu chấp hành (Actuator-substitution risk):**  
  [INFERENCE] Nếu tác giả chỉ thay thế động cơ bước của Wang bằng dây SMA của Kotb hay Pierce để đẩy piston ép jamming, thì đây thuần túy là bài toán kỹ thuật ghép nối linh kiện thay thế (engineering component substitution). Nó không làm phát sinh bất kỳ một câu hỏi cơ học mới nào về bản chất biến dạng hay ma sát, do đó **không đủ tư cách để gánh vác tính mới khoa học cho một luận văn thạc sĩ**.

## 7. Khoảng trống bằng chứng (Evidence gaps)

- Áp suất tạo ra bởi các bơm SMA hiện tại còn tương đối thấp ($14 - 15\text{ kPa}$ trong Kotb 2021 và Pierce 2013), trong khi nghẽn sợi hiệu quả đòi hỏi dải áp suất từ $100\text{ kPa}$ đến $300\text{ kPa}$ (như trong Zhang & Yao 2026). Chưa có tài liệu nào chứng minh một bơm piston SMA mini có thể tạo và duy trì áp suất $300\text{ kPa}$ trong điều kiện chu kỳ bền thực tế.
- Tốc độ đáp ứng nhiệt của SMA (chu kỳ gia nhiệt và làm mát) là một nút thắt cổ chai về động học chưa được giải quyết trong các nghiên cứu tích hợp jamming.

## 8. Các câu hỏi Astra cần kiểm tra lại (Questions Astra should re-check)

1. Liệu có bất kỳ hiệu ứng ghép cặp nhiệt - thủy lực - cơ học (thermo-hydro-mechanical coupling) đặc biệt nào xảy ra khi áp suất phản hồi từ bó dây chuyển pha tác động ngược lại hành trình piston của SMA hay không?
2. Astra cần tái thẩm tra xem việc từ chối C8 như một đóng góp khoa học chính có bỏ sót giá trị sáng chế tiềm năng ở khía cạnh thiết kế tích hợp cơ điện tử hay không.

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
