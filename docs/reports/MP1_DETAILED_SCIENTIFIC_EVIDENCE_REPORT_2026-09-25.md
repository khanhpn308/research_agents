# Báo cáo Bằng chứng Khoa học Chi tiết về Kiểm chứng Hướng Nghiên cứu MP1 (MP1 Detailed Scientific Evidence & Novelty-Audit Report)

**Mã xác thực:** MP1-V002-STAGE3-FINAL  
**Ngày báo cáo:** 2026-09-25  
**Mô hình thực hiện:** Gemini 3.8 Flash High (Stage 3 Remediation Engine)  
**Tập tài liệu kiểm chứng:** 16 bài báo toàn văn tại commit HEAD (`outputs/verification/MP1-V002/verification_matrix.json`)  
**Bằng chứng đối soát:** `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`, Báo cáo phản biện Astra `docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`, và 11 báo cáo worker rà soát `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/` (W01–W11).

---

## Mục lục 24 Chương

1. Bối cảnh, mục tiêu và phạm vi kiểm chứng
2. Lịch sử tiến hóa từ ý tưởng Mentor đến MP1
3. Hiện trạng repository và Reconciliation ở HEAD
4. Phân rã kiến trúc ban đầu và Đánh giá C1–C4
5. Đánh giá biên cơ học C5–C8
6. Đánh giá mối đe dọa T1: Dây NiTi tiếp xúc và ma sát nội
7. Đánh giá mối đe dọa T2: Áp suất giam giữ và Phân loại P1/P2/P3
8. Đánh giá mối đe dọa T3: Ghép cặp chuyển pha, ma sát và độ cứng uốn
9. Phân tích sâu sai sót thực tế cấu hình Carboni 2014 (S2a vs S1a) và Khắc phục
10. Phân tích bài toán kiểm chứng thay thế tham số H0a, H0b và H1
11. Giải quyết xung đột trạng thái Audit JSON (established vs insufficient)
12. Phân tích miền cùng tồn tại của chuyển pha Martensite và trượt giữa các dây
13. Đánh giá khả năng nhận diện thực nghiệm của các cơ chế
14. Định nghĩa và phân loại đại lượng đo độ cứng uốn
15. Đánh giá mô hình hóa: Khả năng nhận diện mô hình và hiện tượng bù trừ tham số
16. Phân cấp độ tin cậy mô hình: Từ khớp đường cong đến chứng minh nhân quả
17. Phân tích bảo thủ về Reedlunn 2013: Góc xoắn, rút gọn động học và tiếp xúc hướng kính
18. Phân tích bảo thủ về Fang 2019: Mô hình vĩ mô tương đương và nguy cơ tiền nhiệm
19. Trạng thái phủ sóng trích dẫn (Citation Coverage Status: Backward & Forward)
20. Ma trận khắc phục phê bình Astra (Astra Critique Remediation Matrix G01–G12)
21. Mechanics Core còn sống sót tạm thời và Giới hạn hiệu lực
22. Tiêu chí bác bỏ dứt điểm (Definitive Kill Criteria)
23. Kế hoạch kiểm chứng và Thực nghiệm phân biệt tối thiểu
24. Kết luận khoa học và Khuyến nghị chiến lược cho Luận văn

---

## Chương 1: Bối cảnh, Mục tiêu và Phạm vi Kiểm chứng (Context, Objective & Scope)

`[AUDIT VERDICT]` Quy trình kiểm chứng khoa học độc lập (scientific novelty-audit pipeline) được thiết lập nhằm rà soát và đánh giá mức độ mới, tính khả thi và độ vững chắc của đề tài nghiên cứu Thạc sĩ kỹ thuật cơ khí trong lĩnh vực robot mềm và biến đổi độ cứng (variable stiffness soft robotics).

Nguyên tắc nghiên cứu bất di bất dịch của quy trình là: **"KHÔNG BẢO VỆ Ý TƯỞNG HIỆN TẠI. HÃY CỐ GẮNG BÁC BỎ NÓ BẰNG CÁC CÔNG TRÌNH TIỀN NHIỆM GẦN NHẤT" (DO NOT DEFEND THE CURRENT IDEA. TRY TO FALSIFY IT USING THE CLOSEST PRIOR WORK)**. Theo nguyên tắc này, các yếu tố sau đây **không được coi là tính mới khoa học (scientific novelty)** nếu đứng riêng lẻ:
- Thay đổi vật liệu (ví dụ: thay thép, nylon bằng hợp kim nhớ hình NiTi);
- Thay đổi hình học (ví dụ: thay tiết diện tròn bằng chữ nhật, thay đổi số lượng dây);
- Nền tảng robot hoặc thiết bị thí nghiệm khác biệt;
- Tăng mật độ điểm đo hoặc mở rộng dải áp suất;
- Mô phỏng phần tử hữu hạn (FEA) nhiều hơn;
- Tinh chỉnh các tham số thực nghiệm (curve fitting).

Mục tiêu của báo cáo Stage 3 này là:
1. Tiếp thu và kiểm chứng 12 phê bình khoa học sắc bén (G01–G12) của GPT-5.6 Astra (`docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md`);
2. Đối soát trực tiếp từng phê bình với toàn bộ 16 bài báo toàn văn PDF trong kho lưu trữ kiểm chứng `data/papers/verification/MP1-V002/`;
3. Sửa chữa toàn bộ các lỗi dữ liệu thực tế, các tuyên bố quá mức (overclaims) và trạng thái trễ (stale state);
4. Tái cấu trúc bài toán khoa học lõi (mechanics core) thành một bài toán kiểm chứng giả thuyết chặt chẽ, loại bỏ hoàn toàn các khoảng trống nghiên cứu giả tạo (false research gaps).

---

## Chương 2: Lịch sử Tiến hóa từ Ý tưởng Mentor đến MP1 (Evolution History from Mentor Idea to MP1)

`[INFERENCE]` Ý tưởng ban đầu do Mentor đề xuất xuất phát từ góc độ tích hợp kỹ thuật hệ thống (engineering integration):
> *"Chế tạo một cơ cấu ngón tay hoặc khâu chấp hành robot mềm có khả năng biến đổi độ cứng cao, sử dụng một bó dây hợp kim nhớ hình NiTi đặt trong buồng kín, được giam giữ bằng áp suất dương sinh ra từ một cơ cấu xi lanh/piston thu nhỏ tích hợp trực tiếp trên thân robot."*

Khi đưa ý tưởng này vào quy trình kiểm chứng độc lập (V001 và V002), đề tài đã trải qua 3 giai đoạn tiến hóa mang tính sống còn:

1. **Giai đoạn 1 — Bác bỏ Tính mới Kiến trúc Thiết bị (Device-level Rejection):**
   Quy trình phân rã chức năng đã chỉ ra rằng toàn bộ các thành phần của ý tưởng Mentor (kẹt dây, kẹt áp suất dương, kết hợp SMA với jamming, và nguồn áp suất nhỏ gọn) đều đã bị các công trình tiền nhiệm từ 2021–2026 chiếm lĩnh hoàn toàn ở mức nguyên lý hoạt động. Không tồn tại tính mới ở cấp độ lắp ghép thiết bị.
2. **Giai đoạn 2 — Rút lui Chiến lược về Bài toán Cơ học Tiếp xúc Lõi (Mechanics Core Pivot):**
   Để cứu vãn giá trị khoa học của đề tài, nhóm nghiên cứu đã rút lui khỏi tuyên bố chế tạo thiết bị và định hình lại thành hướng nghiên cứu **MP1**: *"Nghiên cứu cơ học uốn của bó dây siêu đàn hồi NiTi chịu áp suất giam giữ chủ động, tập trung vào sự ghép cặp giữa chuyển pha Martensite và hiện tượng dính - trượt (stick-slip) giữa các dây"*.
3. **Giai đoạn 3 — Phản biện Nghiêm ngặt từ Astra và Tái Kiểm chứng Stage 3 (Adversarial Critique & Remediation):**
   Phản biện của Astra đã chỉ rõ rằng ngay cả khi đã rút về mechanics core, MP1 vẫn có nguy cơ sụp đổ nếu:
   - Coi việc điều khiển áp suất thay đổi ($p(t)$) là một nguyên lý cơ học mới;
   - Không chứng minh được sự cùng tồn tại của chuyển pha và trượt ma sát trong miền vận hành;
   - Dùng mô hình thay thế đàn hồi đơn giản (H0a) làm "bù nhìn rơm" để tự nhận H1 là mới trong khi khung lý thuyết cấu thành NiTi hiện hữu (H0b) chưa bị bác bỏ;
   - Nhầm lẫn dữ liệu uốn vĩ mô với bằng chứng nhân quả vi mô.

---

## Chương 3: Hiện trạng Repository và Reconciliation ở HEAD (Repository Current State & HEAD Reconciliation)

`[COVERAGE FACT]` Đối soát tại commit HEAD (`fc99a3e693fa13c11ba53b397796548af3656b2b`), kho dữ liệu kiểm chứng chính thức bao gồm **16 bài báo toàn văn PDF** được nạp đầy đủ trong `outputs/verification/MP1-V002/verification_matrix.json` và được kiểm định trong `outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json`.

Bảng tổng hợp 16 bài báo kiểm chứng:

| STT | Paper ID | Tác giả & Năm | Nhan đề & Tạp chí | Trọng tâm Cơ học Liên quan MP1 | Trạng thái Bằng chứng |
|:---:|:---:|:---|:---|:---|:---:|
| 1 | `00414aac4b` | Reedlunn et al. (2013) | *Superelastic shape memory alloy cables Part I – Isothermal tension experiments* (IJSS) | Thí nghiệm kéo đẳng nhiệt cáp NiTi 7x7 và 1x27; baseline thềm chuyển pha. | `[VERIFIED FULL TEXT]` |
| 2 | `fac21c950e` | Reedlunn et al. (2013) | *Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses* (IJSS) | Phân rã cấu phần, tương tác tiếp xúc hướng kính, khuyết tật do chế tạo bện cáp. | `[VERIFIED FULL TEXT]` |
| 3 | `40760daa02` | Carboni & Lacarbonara (2016) | *Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments* (ASCE JEM) | Thiết bị dập tắt dao động dùng cáp NiTi/thép; trễ thắt (pinched hysteresis) do phục hồi đàn hồi + ma sát. | `[VERIFIED FULL TEXT]` |
| 4 | `2f7fcf2f8f` | Fang et al. (2019) | *Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application* (Eng. Struct.) | Mô hình dầm sợi phi tuyến (OpenSees) cho trễ kéo cáp NiTi; mô hình tương đương vĩ mô. | `[VERIFIED FULL TEXT]` |
| 5 | `7f3f45407f` | Ting-Long et al. (2021) | *Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation* (MSSP) | Đáp ứng động học và nhận diện tham số bộ cách ly cáp thép xoắn dưới ma sát trượt. | `[VERIFIED FULL TEXT]` |
| 6 | `1c81b2d35c` | Falcetelli et al. (2024) | *Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes* (Exp. Mech.) | Thí nghiệm đối đầu trực tiếp cáp thép vs cáp NiTi; so sánh trượt ma sát thuần túy vs trượt + siêu đàn hồi. | `[VERIFIED FULL TEXT]` |
| 7 | `9f4295be23` | Barsi, Carboni, Lacarbonara (2025) | *A new mechanical model of short wire ropes: Theory and experimental validation* (Eng. Struct.) | Mô hình dầm biến dạng cắt với biến dạng riêng (eigenstrains); tính toán cận trên/dưới độ cứng uốn. | `[VERIFIED FULL TEXT]` |
| 8 | `56793dea9b` | Kang et al. (2020) | *Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables* (JME) | Mô hình FEA Abaqus UMAT kết hợp biến thiên mô-đun khi chuyển pha và tiếp xúc ma sát 3D giữa các dây. | `[VERIFIED FULL TEXT]` |
| 9 | `d9966f2f5e` | Carboni et al. (2015) | *Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands* (ASCE JEM) | Thí nghiệm và nhận diện trễ đa cấu hình (S1a: NiTi7 kéo-uốn; S2a: ST49 thép uốn). | `[VERIFIED FULL TEXT]` |
| 10 | `9e15094d68` | Niu et al. (2023) | *Superelasticity SMA cables and its simplified FE model* (Structures) | Mô hình số phần tử hữu hạn đơn giản hóa cho cáp SMA siêu đàn hồi. | `[VERIFIED FULL TEXT]` |
| 11 | `53200aa0c6` | Vahidi et al. (2022) | *Mechanical response of single and double-helix SMA wire ropes* (MAMS) | Mô hình Abaqus UMAT 3D đầy đủ: Luật Auricchio ghép tiếp xúc ma sát Coulomb ($\mu = 0.115$). | `[VERIFIED FULL TEXT]` |
| 12 | `98fee47c04` | de Paula et al. (2021) | *Nonlinear vibration isolation via a nitinol wire rope* (JSV) | Cách ly dao động phi tuyến dùng cáp Nitinol; phân tích tiêu tán trễ. | `[VERIFIED FULL TEXT]` |
| 13 | `aaad9c248c` | Xin Liu (2013) | *Cable Vibration Considering Internal Friction* (PhD Thesis, Univ. of Houston) | Mô hình ma sát nội do áp suất hướng kính giữa các lớp dây ($P_i$); tính toán độ cứng chống uốn. | `[VERIFIED FULL TEXT]` |
| 14 | `ccdc1bb980` | Tjahjanto et al. (2017) | *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable* (OMAE) | Uốn cáp ngầm dưới áp suất hướng kính ngoài, lực căng và trượt dính dốc loxodromic. | `[VERIFIED FULL TEXT]` |
| 15 | `e8462758c3` | Liu et al. (2026) | *High damping capacity with a wide temperature window in braided NiTi microfilaments* (Mater. Lett.) | Vi sợi NiTi bện: tương tác giữa chuyển pha cục bộ và trượt vi mô (micro-slip) tiếp xúc. | `[VERIFIED FULL TEXT]` |
| 16 | `6dd1ca94d1` | Silva et al. (2022) | *NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings* (Sensors) | Vi cáp NiTi: tự gia nhiệt ma sát (frictional self-heating) làm dịch ứng suất chuyển pha Clausius-Clapeyron. | `[VERIFIED FULL TEXT]` |

Tệp `TARGETED_THREAT_AUDIT.json` tại HEAD xác nhận:
- `paper_count`: 16;
- `final_v002_verdict`: `False` (MP1-V002 không vượt qua kiểm chứng như một hướng nghiên cứu mới trọn vẹn);
- `survives_current_full_text_set`: `True` (chỉ sống sót tạm thời dưới dạng câu hỏi cơ học hẹp về áp suất giam giữ);
- `stop_condition_satisfied`: `False` (chưa thỏa điều kiện dừng tra cứu).

---

## Chương 4: Phân rã Kiến trúc Ban đầu và Đánh giá C1–C4 (Architectural Decomposition & Audit of C1–C4)

`[AUDIT VERDICT]` Bốn khẳng định cấp thiết bị C1–C4 đã bị đóng dứt điểm (`CLOSED` / `PREEMPTED`) bởi các công trình tiền nhiệm trực tiếp:

1. **C1 (Wire Jamming):** Tuyên bố việc tăng độ cứng uốn bằng cách kẹt các sợi/dây kim loại là mới -> **BỊ BÁC BỎ**.
   - Bai et al. (2022, DOI: 10.3390/app12073582) và Liu et al. (2021, DOI: 10.1109/LRA.2021.3097255) đã chứng minh tường minh nguyên lý kẹt dây kim loại điều chỉnh độ cứng.
   - *Residual Caveat:* Việc thay đổi vật liệu sang NiTi hay đổi bước xoắn không tự tạo ra tính mới khoa học nếu không làm phát sinh câu hỏi cơ học mới.
2. **C2 (Positive-Pressure Jamming):** Tuyên bố dùng áp suất dương để kẹt sợi thay cho hút chân không là mới -> **BỊ BÁC BỎ**.
   - Zhang & Yao et al. (2026, DOI: 10.5194/ms-17-481-2026) và Huynh et al. (2022, DOI: 10.20965/jrm.2022.p0466) đã phát triển đầy đủ mô hình và thực nghiệm kẹt sợi dưới áp suất dương.
   - *Residual Caveat:* Áp suất dương chỉ là phương tiện tạo tải pháp tuyến biên ($N \propto p$), tuân thủ định luật Coulomb cơ bản.
3. **C3 (SMA + Jamming Coexistence):** Tuyên bố việc tích hợp SMA và jamming trong cùng một kết cấu là mới -> **BỊ BÁC BỎ**.
   - Takashima et al. (2021, DOI: 10.1299/mej.24-00130; 2022, DOI: 10.1108/IR-11-2023-0305) đã tích hợp dây SMA làm lõi dẫn động bên trong môi trường kẹt hạt/tấm.
   - *Residual Caveat:* Trong Takashima, SMA là actuator riêng biệt, không tự đóng vai trò mạng ma sát. Tuy nhiên, khẳng định cấp hệ thống "SMA + Jamming cùng xuất hiện" đã bị đóng hoàn toàn.
4. **C4 (Compact Pressure Source):** Tuyên bố tích hợp bộ tạo áp suất mini tại chỗ là mới -> **BỊ BÁC BỎ**.
   - Huynh et al. (2022) tích hợp bơm ECF mini; Wang et al. (2024, DOI: 10.1016/j.birob.2024.100163) tích hợp cơ cấu piston jamming trên tay robot mềm.
   - *Residual Caveat:* Tích hợp cơ khí nhỏ gọn là bài toán kỹ thuật (engineering implementation), không phải nguyên lý cơ học mới.

---

## Chương 5: Đánh giá Biên Cơ học C5–C8 (Boundary Audit of C5–C8)

`[ASTRA CRITIQUE]` Bốn khẳng định biên cơ học C5–C8 được hiệu chỉnh ranh giới chặt chẽ theo phê bình của Astra nhằm loại bỏ các khoảng trống giả tạo:

1. **C5 (NiTi as Friction Medium):** Ranh giới cũ gán nhãn `open` là sai lệch. Trong V002, việc dây NiTi đóng vai trò mạng ma sát trượt đã bị đóng (`CLOSED` bởi T1). Việc đổi tên từ "cáp xoắn" (cable) sang "bó dây song song" (bundle) không tạo ra cơ học mới vì cùng chịu chi phối bởi định luật tiếp xúc Coulomb.
2. **C6 (Active Confinement as Distinct Problem):** Trạng thái `open_in_current_full_text_set` chỉ là mô tả kho dữ liệu hiện tại, không phải kết luận khoa học. Áp suất giam giữ chủ động ($P_3$) chỉ là một điều kiện biên tải trọng ngoài biến thiên theo thời gian ($p(t)$), không phải một lớp lý thuyết mới.
3. **C7 (Coupled NiTi-Slip-Pressure-Stiffness Domain):** Ngụy biện "chưa xuất hiện đồng thời trong cùng một bài báo". Luật cấu thành NiTi đã biết + định luật tiếp xúc Coulomb đã biết tự động sinh ra phân bố ứng suất và trượt thông qua cân bằng động học. C7 chỉ tồn tại dưới dạng một giả thuyết kiểm chứng (hypothesis testing), không phải miền cơ học đã chứng minh mới.
4. **C8 (SMA Syringe/Piston Jamming):** Duy trì phán quyết `SUBSTANTIALLY_PREEMPTED`. Sự kết hợp các chi tiết chức năng đã biết là giải pháp thiết kế cơ khí, không cấu thành đóng góp khoa học cơ bản.

---

## Chương 6: Đánh giá Mối Đe dọa T1: Dây NiTi Tiếp xúc và Ma sát Nội (Threat Audit T1)

`[VERIFIED FULL TEXT]` Mối đe dọa T1 nhắm vào khẳng định: "Chưa có nghiên cứu nào xem xét dây NiTi như một tập hợp có tiếp xúc, ma sát và chuyển động trượt tương đối nội tại".

Phán quyết: **ĐÓNG HOÀN TOÀN (`CLOSED` / `PREEMPTED`)**.

Bằng chứng thực nghiệm và giải tích toàn văn xác lập vững chắc:
1. **Vahidi et al. (2022, `53200aa0c6`):** Thiết lập mô hình FEA 3D chi tiết (185.300 phần tử) cho cáp NiTi 1x27 và 7x7; giải thuật tiếp xúc bề mặt - bề mặt thực (true surface-to-surface) với ma sát Coulomb ($\mu = 0.115$), chứng minh ma sát giữa các dây làm tiêu tán năng lượng trượt và phân bố lại ứng suất.
2. **Kang et al. (2020, `56793dea9b`):** Xây dựng chương trình con Abaqus UMAT giải quyết đồng thời sự thay đổi mô-đun đàn hồi khi chuyển pha và tương tác tiếp xúc ma sát giữa các dây NiTi khi chịu tải.
3. **Reedlunn et al. (2013 Part II, `fac21c950e`):** Sử dụng ảnh SEM (Hình 8) phát hiện các vết lõm tiếp xúc cơ học giữa các lớp dây NiTi do áp lực khi bện cáp, chứng minh ứng suất tiếp xúc kích hoạt mầm chuyển pha cục bộ.
4. **Silva et al. (2022, `6dd1ca94d1`):** Chứng minh ma sát trượt giữa các vi sợi NiTi sinh nhiệt (self-heating), làm dịch chuyển ứng suất chuyển pha theo Clausius-Clapeyron.
5. **Falcetelli et al. (2024, `1c81b2d35c`):** Thử nghiệm so sánh trực tiếp cáp thép vs cáp NiTi dưới tải trọng chu kỳ, phân tách rõ ràng sự khác biệt giữa trượt ma sát thuần túy và trượt kết hợp siêu đàn hồi.

---

## Chương 7: Đánh giá Mối Đe dọa T2: Áp suất Giam giữ và Phân loại P1/P2/P3 (Threat Audit T2)

`[AUDIT VERDICT]` Mối đe dọa T2 phân tích ba mức áp suất giam giữ tác động lên bó dây:
- **P1 (Áp suất chế tạo thụ động):** Sinh ra do bện/xoắn cáp (preforming). Đã được phân tích chi tiết trong Reedlunn 2013 và luận án của Xin Liu (2013, `aaad9c248c`), trong đó áp suất hướng kính $P_i$ quyết định lực ma sát nội và khả năng dập tắt dao động.
- **P2 (Áp suất biên ngoài cố định):** Áp suất ngoài được áp đặt trước và giữ không đổi trong suốt chu trình uốn. Đã được thiết lập trong Tjahjanto et al. (2017, `ccdc1bb980`) cho cáp ngầm chịu áp suất hướng kính ngoài kết hợp uốn dính - trượt, và trong Zhang & Yao (2026) cho bó sợi kẹt.
- **P3 (Áp suất giam giữ chủ động biến thiên $p(t)$):** Áp suất buồng thay đổi độc lập với biến dạng uốn trong cùng một lịch sử tải.

`[INFERENCE]` **Kiểm chứng Cơ học:** Các phương trình cơ học tiếp xúc vi phân:
$$\Phi = \|\mathbf{f}_t\| - \mu f_n \le 0, \quad f_n(t) = \mathcal{K}_{\text{geom}} \cdot p(t)$$
hoàn toàn tự nhiên tiếp nhận lịch sử tải $p(t)$ mà không cần thay đổi bất kỳ định luật vật lý nào. Các thuật toán tiếp xúc phần tử hữu hạn chuẩn (penalty / Lagrange multipliers) tự động xử lý $p(t)$ ở từng gia số thời gian. Do đó, P3 chỉ là một **giao thức điều khiển thực nghiệm**, không phải là một nguyên lý cơ học mới.

---

## Chương 8: Đánh giá Mối Đe dọa T3: Ghép cặp Chuyển pha, Ma sát và Độ cứng Uốn (Threat Audit T3)

`[AUDIT VERDICT]` Mối đe dọa T3 nhắm vào sự kết hợp giữa chuyển pha siêu đàn hồi NiTi, tiếp xúc ma sát và độ cứng uốn.

Phán quyết: **TIỀN NHIỆM ĐÃ CHIẾM LĨNH ĐÁNG KỂ (`SUBSTANTIALLY PREEMPTED`)**.

Bằng chứng toàn văn:
- Vahidi et al. (2022) đã ghép thành công luật chuyển pha Auricchio với tiếp xúc ma sát 3D trong phần mềm thương mại chuẩn.
- Barsi, Carboni, Lacarbonara (2025, `9f4295be23`) đã thiết lập mô hình giải tích dầm biến dạng cắt với biến dạng riêng (eigenstrains) để tính toán chính xác hai cận trên và cận dưới của độ cứng uốn (stick bound và slip bound) cho cáp chịu uốn chu kỳ.
- Carboni & Lacarbonara (2016, `40760daa02`) đã xây dựng mô hình trễ thắt kết hợp phục hồi đàn hồi phi tuyến và ma sát trượt.

---

## Chương 9: Phân tích Sâu Sai sót Thực tế Cấu hình Carboni 2014 (S2a vs S1a) và Khắc phục (Carboni Configuration Correction)

`[VERIFIED FULL TEXT]` Trong báo cáo rà soát Stage 1 (packet W08), có một sai sót sự thật nghiêm trọng khi khẳng định rằng: *"Cấu hình S2a trong nghiên cứu của Carboni et al. (2014/2015, `d9966f2f5e`) đã chứng minh chuyển pha siêu đàn hồi của dây NiTi dưới uốn thuần túy"*.

Astra đã phát hiện ra lỗ hổng này trong phê bình G05. Kiểm tra trực tiếp tệp PDF `A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf` tại Trang 9–10 và Bảng 4 (**Table 4**):

```text
Table 4. List of Considered Device Configurations:
- S1a: PSG = NiTi7 (8 ropes of length 56 mm), SSG = none.
- S2a: PSG = ST49 (steel wire rope, 49 wires, length 100 mm), SSG = none.
- S3a: PSG = NiTi19 (length 80 mm), SSG = NiTi1 (length 103 mm).
- S3b: PSG = ST49 (length 100 mm), SSG = NiTi7 (length 63 mm).
- S3c: PSG = ST49 (length 100 mm), SSG = NiTi1 (length 63 mm).
```

Trích dẫn nguyên văn từ văn bản của tác giả (Trang 9, cột 2):
1. **Về S2a:**
   > *"a steel wire rope formed by 1 + 6 strands, each made of 1 + 6 wires for a total number of 49 wires and a diameter equal to 6.0 mm (ST49)... The restoring force assumed for the identification of Assembly S2a is obtained using Eq. (15), with r = 1, in which the hysteretic force z is governed by the evolution law of the BW model given by Eq. (1)."*
   -> **Sự thật khoa học:** Cấu hình **S2a hoàn toàn là cáp thép (ST49)**, nhận diện bằng mô hình Bouc-Wen (BW) thuần ma sát, hoàn toàn không có dây NiTi và không có chuyển pha Martensite!
2. **Về S1a:**
   > *"In Fig. 13, the hysteretic cycles for Configuration S1a and the associated identifications are shown... The Nitinol strands are subjected to a tension-bending state of stress. This stress state determines the phase transitions in the individual Nitinol wires... The pinching is caused by the return to the austenitic phase toward the end of the unloading branches."*
   -> **Sự thật khoa học:** Cấu hình chứa cáp NiTi là **S1a**, nhưng chịu trạng thái ứng suất **kéo - uốn kết hợp (tension-bending)** do cơ cấu ngàm khóa dịch chuyển ngang sinh ra hiệu ứng kéo căng hình học lớn. Chuyển pha xảy ra do lực kéo căng này, không phải uốn thuần túy!

**Khắc phục dứt điểm:** Loại bỏ 100% suy luận sai lệch về S2a. Ghi nhận chính xác: Tiền nhiệm Carboni 2015 chỉ chứng minh trễ thắt của NiTi dưới tải kéo - uốn kết hợp có kéo căng hình học lớn, chưa từng chứng minh chuyển pha xảy ra dưới uốn thuần túy với biến dạng nhỏ.

---

## Chương 10: Phân tích Bài toán Kiểm chứng Thay thế Tham số H0a, H0b và H1 (Parameter Substitution Test)

`[INFERENCE]` Tiếp thu phê bình G01 của Astra, bài toán thay thế tham số được cấu trúc lại thành 3 giả thuyết lồng nhau rõ ràng:

1. **H0a — Naive Elastic Substitution:**
   - Thay thế dây NiTi bằng dầm đàn hồi tuyến tính đơn giản có mô-đun không đổi $E = E_{\text{eff}} = \text{const}$ và hệ số ma sát $\mu$ vào mô hình kẹt sợi hiện hữu.
   - **Đánh giá:** Bị bác bỏ hoàn toàn (`REFUTED` / `established`). Vật liệu siêu đàn hồi NiTi có thềm ứng suất chuyển pha, suy giảm mô-đun từ $E_A \approx 60\,\text{GPa}$ xuống $E_M \approx 25\,\text{GPa}$, bất đối xứng kéo - nén và trễ phục hồi; một hằng số $E_{\text{eff}}$ không thể tái tạo được hành vi này khi vượt ngưỡng chuyển pha.
2. **H0b — Khung lý thuyết NiTi Cấu thành – Tiếp xúc Hiện hữu:**
   - Áp dụng các luật cấu thành siêu đàn hồi NiTi hiện hữu (Auricchio-Petrini 3D, Graesser-Cozzarelli 1D) kết hợp với cơ học tiếp xúc Coulomb tiêu chuẩn và điều kiện biên áp suất biến thiên $p(t)$.
   - **Đánh giá:** Chưa bị bác bỏ (`NOT FALSIFIED` / `PLAUSIBLE`). Các công trình Vahidi 2022, Kang 2020, Carboni 2016, Barsi 2025 chứng minh khung lý thuyết này hoàn toàn khả thi và chưa từng thất bại trong việc mô phỏng bó dây NiTi.
3. **H1 — Lý thuyết Ghép cặp Vi mô Mới Vượt ngoài H0b:**
   - Khẳng định cần một phương trình ghép cặp vi mô mới giữa áp suất cục bộ và động học chuyển pha.
   - **Đánh giá:** Chưa có bằng chứng khoa học hỗ trợ (`INSUFFICIENT EVIDENCE`).

---

## Chương 11: Giải quyết Xung đột Trạng thái Audit JSON (Resolution of Audit JSON State Discrepancy)

`[AUDIT VERDICT]` Trong tệp `TARGETED_THREAT_AUDIT.json` (dòng 237–241), trường `parameter_substitution_test` ghi nhận:
```json
"existing_elastic_fiber_model_appears_sufficient": false,
"niti_requires_distinct_constitutive_contact_coupling": true,
"evidence_status": "established"
```
Trong khi đó, báo cáo phản biện của Astra kết luận rằng trạng thái bằng chứng đối với việc đòi hỏi một coupling mới là `insufficient`.

`[INFERENCE]` **Giải quyết xung đột:**
1. Bảo toàn nguyên trạng tệp `TARGETED_THREAT_AUDIT.json` để giữ toàn vẹn lịch sử lưu trữ (provenance preservation).
2. Làm rõ nội hàm: Từ khóa `established` trong tệp JSON được tạo ra nhằm khẳng định việc **bác bỏ mô hình thay thế đàn hồi đơn giản H0a** (khẳng định rằng không thể xem NiTi như sợi nylon/thép đàn hồi tuyến tính đơn giản).
3. Tuy nhiên, khi xét trên bài toán cạnh tranh giữa **H0b và H1**, trạng thái thực tế của bằng chứng là **`insufficient`** (hoàn toàn chưa có bằng chứng thực nghiệm nào chứng minh H0b thất bại để đòi hỏi H1).
4. Báo cáo chính thức xác nhận: Không được dùng nhãn `established` của việc bác bỏ H0a để ngụy biện rằng H1 đã được chứng minh.

---

## Chương 12: Phân tích Miền Cùng Tồn tại của Chuyển pha Martensite và Trượt giữa các Dây (Coexistence Domain Analysis)

`[INFERENCE]` Phân tích định lượng cơ học (W06) giải quyết triệt để phê bình G03:

Xét bó dây NiTi uốn vĩ mô với độ cong $\kappa$ dưới áp suất giam giữ $p$:
- **Ngưỡng trượt ma sát giữa các dây (Slip Onset):**
  $$\kappa_{\text{slip}}(p) \propto \frac{\mu \, p}{E_A \, d}$$
  tỷ lệ thuận với áp suất giam giữ $p$.
- **Ngưỡng kích hoạt chuyển pha Martensite (Transformation Onset):**
  Xảy ra khi biến dạng thớ ngoài cùng vượt ngưỡng $\varepsilon_{\text{Ms}} \approx 0.75\% - 1.0\%$:
  - Khi dính hoàn toàn (Full Stick): $\kappa_{\text{tr}}^{\text{stick}} = \varepsilon_{\text{Ms}} / R_b$.
  - Khi trượt hoàn toàn (Full Slip): $\kappa_{\text{tr}}^{\text{slip}} = \varepsilon_{\text{Ms}} / (d/2)$.

Vì bán kính bó dây $R_b$ lớn hơn nhiều bán kính sợi đơn $d/2$ ($R_b \gg d/2$), không gian trạng thái bị phân rã:
1. **Miền Biến dạng Nhỏ ($\kappa_{\text{slip}} \le \kappa < \kappa_{\text{tr}}$):**
   Các dây trượt qua nhau nhưng biến dạng từng sợi nhỏ hơn $0.75\%$. Toàn bộ dây NiTi **hoàn toàn ở pha Austenite đàn hồi ($E = E_A = \text{const}$)**. Không có chuyển pha, không có siêu đàn hồi. Hệ thống thoái hóa về bài toán **kẹt dây đàn hồi (elastic wire jamming)** truyền thống. Mô hình H0a hoàn toàn đủ dùng!
2. **Miền Áp suất Rất Lớn ($p \to p_{\text{max}}$):**
   Bó dây bị khóa dính hoàn toàn (full stick). Biến dạng tăng nhanh và chuyển pha xảy ra nhưng các dây không trượt qua nhau. Hệ thống hành xử như một **dầm siêu đàn hồi liền khối**. Không có sự tương tác giữa chuyển pha và trượt ma sát!
3. **Miền Cùng Tồn Tại Thực sự (Coexistence Domain):**
   Chỉ xuất hiện khi độ cong uốn cực lớn (uốn gập góc sâu) HOẶC có lực kéo căng dọc trục đáng kể (như cấu hình S1a của Carboni). Nếu robot mềm chỉ vận hành ở góc uốn vừa phải, bài toán hoàn toàn không kích hoạt cơ chế ghép cặp NiTi.

---

## Chương 13: Đánh giá Khả năng Nhận diện Thực nghiệm của các Cơ chế (Experimental Identifiability)

`[ASTRA CRITIQUE]` Tiếp thu phê bình G04 và G09 của Astra:
1. **Sự Bất khả thi từ Dữ liệu Uốn Vĩ mô Đơn độc:**
   Một đường cong mô-men – góc uốn ($M - \theta$) vĩ mô không thể phân biệt được hiện tượng giảm độ cứng (softening) là do:
   - Trượt ma sát Coulomb giữa các dây;
   - Chuyển pha siêu đàn hồi của NiTi;
   - Biến dạng bẹp tiết diện bó dây (cross-sectional ovalization);
   - Sự lún trượt đàn dẻo tại ngàm kẹp (grip compliance).
2. **Chuỗi Truyền Áp suất Giam giữ (Pressure Transmission Chain):**
   Áp suất buồng $p$ bị suy hao qua ứng suất vòng của màng đàn hồi ($\sigma_{\theta,\text{mem}}$) và bị che chắn bởi hiệu ứng vòm (arching effect) trong bó dây ngẫu nhiên. Nếu không đo trực tiếp lực nén pháp tuyến $f_n$, sai số truyền áp sẽ bị ngụy trang thành sai số của luật cấu thành NiTi.
3. **Yêu cầu Đo đạc Cục bộ Bắt buộc:**
   Để nhận diện cơ chế, thực nghiệm bắt buộc phải trang bị:
   - Đo biến dạng quang học (DIC) hoặc sợi quang FBG đo độ cong cục bộ;
   - Camera nhiệt hồng ngoại (chuyển pha tỏa/thu nhiệt $\Delta H_{\text{tr}}$, ma sát chỉ sinh nhiệt đơn chiều);
   - Cảm biến dịch chuyển vi mô (LVDT) đo trực tiếp độ trượt tương đối tại đầu dây tự do.

---

## Chương 14: Định nghĩa và Phân loại Đại lượng Đo Độ cứng Uốn (Bending Stiffness Observables)

`[ASTRA CRITIQUE]` Khắc phục phê bình G12, báo cáo chuẩn hóa 3 định nghĩa toán học riêng biệt cho độ cứng uốn:

1. **Độ cứng Uốn Tiếp tuyến (Tangent Bending Stiffness):**
   $$D_{\text{tan}}(\kappa, p, \text{history}) = \left.\frac{\partial M}{\partial \kappa}\right|_{p = \text{const}}$$
   Phụ thuộc nghiêm ngặt vào nhánh tải (loading) hay dỡ tải (unloading). Giảm mạnh khi bắt đầu trượt hoặc bắt đầu chuyển pha.
2. **Độ cứng Uốn Cát tuyến (Secant Bending Stiffness):**
   $$D_{\text{sec}}(\kappa, p) = \frac{M(\kappa, p) - M_0}{\kappa - \kappa_0}$$
   Đo khả năng kháng uốn trung bình tại một góc uốn cực đại; làm mịn các điểm kỳ dị dính - trượt cục bộ.
3. **Độ cứng Uốn Động học Chu kỳ Nhỏ (Dynamic / Storage Stiffness):**
   $$D_{\text{dyn}}(\kappa_0, p, \omega) = \frac{\Delta M}{\Delta \kappa} \cos(\delta)$$
   Đo bằng dao động nhỏ xung quanh trạng thái uốn tĩnh $\kappa_0$. Vì biên độ nhỏ, các dây có thể ở trạng thái dính vi mô (micro-stick), khiến $D_{\text{dyn}}$ tiệm cận cận trên độ cứng (stick bound) ngay cả khi hệ vĩ mô đã trượt.

Mọi công bố thực nghiệm bắt buộc phải chỉ rõ loại độ cứng, nhánh tải, nhiệt độ môi trường và lịch sử biến dạng trước đó.

---

## Chương 15: Đánh giá Mô hình hóa: Khả năng Nhận diện Mô hình và Hiện tượng Bù trừ Tham số (Model Identifiability & Parameter Confounding)

`[ASTRA CRITIQUE]` Phân tích chi tiết phê bình G08:
- Trong bài toán uốn bó dây có ma sát:
  $$F_{\text{cap}} = \mu f_n = \mu (\alpha_{\text{trans}} p \cdot d + f_{n,0})$$
  Mô-men trượt vĩ mô $M_{\text{slip}}$ chỉ tỷ lệ với tích số $(\mu \cdot \alpha_{\text{trans}} \cdot p)$.
- Phép khớp đường cong uốn vĩ mô $M - \kappa$ chỉ ràng buộc được tích số $(\mu \cdot \alpha_{\text{trans}})$, hoàn toàn không thể phân tách độc lập hệ số ma sát $\mu$ và hệ số truyền áp $\alpha_{\text{trans}}$.
- Thêm vào đó, mô-đun đàn hồi tương đương $E_{\text{eff}}$, độ cứng phạt tiếp xúc $k_{\text{pen}}$, và biến dạng dự ứng suất ban đầu có thể bù trừ lẫn nhau, cho phép nhiều bộ tham số sai lệch vật lý cùng tạo ra một đường cong khớp hoàn hảo ($R^2 > 0.99$).
- Cảnh báo bẫy **"Tính kép độ mềm" (Double-counting compliance)**: Lấy mô-đun tương đương đo từ bó dây (đã chứa độ mềm do trượt) gán ngược vào mô hình FEA chi tiết từng sợi sẽ làm sai lệch hoàn toàn kết quả mô phỏng.

---

## Chương 16: Phân cấp Độ Tin cậy Mô hình: Từ Khớp Đường cong đến Chứng minh Nhân quả (Hierarchy of Model Credibility)

`[ASTRA CRITIQUE]` Khắc phục phê bình G06, thiết lập Thang bậc 5 tầng về độ tin cậy mô hình:

- **Tầng 1 (Model Formulation):** Thiết lập hệ phương trình vi phân và điều kiện biên.
- **Tầng 2 (Numerical Verification):** Kiểm chứng thuật toán số, độ hội tụ lưới và bảo toàn năng lượng.
- **Tầng 3 (Parameter Calibration / Curve Fitting):** Tinh chỉnh tham số tự do để khớp một đường cong thực nghiệm đã biết (chưa có giá trị chứng minh vật lý).
- **Tầng 4 (Experimental Validation with Locked Parameters):** Khóa cứng toàn bộ tham số đã đo độc lập, dự đoán đáp ứng trên các đường tải biến thiên MỚI chưa từng dùng để hiệu chỉnh.
- **Tầng 5 (Causal Mechanism Identification):** Đo đạc trực tiếp các biến trạng thái nội vi mô (độ trượt, phần thể tích Martensite $\xi$, nhiệt độ) và xác nhận trùng khớp với dự đoán của mô hình.

Mô hình kiểm chứng MP1 bắt buộc phải đạt tối thiểu **Tầng 4** để có giá trị khoa học.

---

## Chương 17: Phân tích Bảo thủ về Reedlunn 2013 (Conservative Analysis of Reedlunn 2013)

`[VERIFIED FULL TEXT]` Khắc phục phê bình G07 của Astra đối với Reedlunn et al. (2013, `00414aac4b`, `fac21c950e`):
1. **Nguyên nhân Sai số:** Reedlunn kiểm tra tải kéo đơn trục trên cáp xoắn 1x27; sự sai lệch của mô hình giải tích ở các lớp dây ngoài xuất phát từ việc **bỏ qua uốn và xoắn cục bộ của từng sợi dây** trong động học rút gọn Costello, không phải do thất bại của lý thuyết tiếp xúc hay cấu thành NiTi.
2. **Góc Xoắn Nông vs Bó Dây Thẳng:** Cáp có góc xoắn nông (7x7) có đáp ứng kéo chuẩn hóa rất gần với dây đơn. Việc lấy sự thất bại ở góc xoắn dốc để suy diễn rằng bó dây thẳng của robot mềm bắt buộc phải có cơ chế ghép cặp mới là một ngụy biện ngoại suy sai lầm.
3. **Vết Lõm Tiếp xúc (SEM Fig. 8):** Là khuyết tật hình học tạo ra từ quá trình chế tạo bện cáp ban đầu, không phải hư hại do điều khiển áp suất vận hành.

---

## Chương 18: Phân tích Bảo thủ về Fang 2019: Mô hình Vĩ mô Tương đương và Nguy cơ Tiền nhiệm (Conservative Analysis of Fang 2019)

`[VERIFIED FULL TEXT]` Khắc phục triệt để các nhận định về Fang et al. (2019, `2f7fcf2f8f`):
1. **Đính chính Sự thật về Mô hình Cầu RC:**
   Fang et al. chỉ thử nghiệm kéo cáp NiTi. Phần mô phỏng "phần tử dầm sợi phi tuyến" ở cuối bài báo là dành cho **trụ cầu bê tông cốt thép (RC bridge pier)** đường kính 1.4 m; các đoạn cáp NiTi chỉ đóng vai trò thanh giằng chịu kéo chống động đất. Fang **chưa từng mô phỏng hay thử nghiệm uốn cáp NiTi dưới áp suất**.
2. **Mối Đe dọa từ Mô hình Tương đương Vĩ mô (Macromodel Threat):**
   Mô hình phần tử sợi của Fang (kết hợp các vùng sợi gán vật liệu Steel02 và Self-centering) tái tạo xuất sắc toàn bộ chu trình trễ kéo của cáp NiTi mà không cần resolve tiếp xúc vi mô. Nếu một mô hình vĩ mô tương đương gọn nhẹ có thể dự đoán độ cứng uốn dưới áp suất thay đổi, thì việc xây dựng mô hình tiếp xúc vi mô phức tạp sẽ mất đi ý nghĩa ứng dụng thực tiễn.

---

## Chương 19: Trạng thái Phủ sóng Trích dẫn (Citation Coverage Status: Backward & Forward)

`[COVERAGE FACT]` Báo cáo tình trạng phủ sóng trích dẫn từ `outputs/verification/MP1-V002/citation_coverage.json`:
- **Tổng số hướng bắt buộc:** 15 hướng (9 backward, 6 forward);
- **Tất cả các hướng đã sàng lọc:** `False`;
- **Điều kiện dừng được thỏa mãn (Stop condition satisfied):** `False`.

Hai nhánh trích dẫn ngược trọng yếu chưa đóng chính thức trong audit JSON:
1. Nhánh B11: Kang et al. (2020, `56793dea9b` - mô hình Abaqus UMAT cho cáp NiTi có ma sát tiếp xúc);
2. Nhánh B12: Barsi, Carboni, Lacarbonara (2025, `9f4295be23` - mô hình dầm biến dạng cắt tính cận trên/dưới độ cứng uốn cáp).

`[AUDIT VERDICT]` Việc chưa đạt điều kiện dừng là **BLOCKING đối với tuyên bố rằng đã hoàn tất tìm kiếm tiền nhiệm toàn cầu**. Không được phép tuyên bố tính mới tuyệt đối. Đề tài chỉ được trình bày như một giả thuyết sống sót tạm thời trong tập dữ liệu hữu hạn đã kiểm tra.

---

## Chương 20: Ma trận Khắc phục Phê bình Astra (Astra Critique Remediation Matrix G01–G12)

Bảng tổng hợp đối soát 12 lỗ hổng (tóm lược từ ma trận chi tiết tại `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`):

| ID | Mức độ | Lỗ hổng Trọng yếu | Phân loại | Hành động Khắc phục Chính |
|:---:|:---:|:---|:---:|:---|
| **G01** | CRITICAL | H0 định nghĩa không nhất quán | `VERIFIED` | Tách 3 tầng: H0a (bị bác bỏ), H0b (chưa bị bác bỏ), H1 (chưa có bằng chứng). |
| **G02** | CRITICAL | P3 bị coi là cơ chế mới do áp suất điều chỉnh được | `VERIFIED` | Hạ cấp P3 thành giao thức điều khiển biên; phương trình hiện hữu tự nhận $p(t)$. |
| **G03** | CRITICAL | Chưa chứng minh chuyển pha và trượt cùng tồn tại | `VERIFIED` | Xác định điều kiện cần cho Coexistence Domain; nhận diện nguy cơ thoái hóa về H0a. |
| **G04** | CRITICAL | Đường cong uốn vĩ mô không nhận diện riêng được cơ chế | `VERIFIED` | Cấm suy luận cơ chế từ đường cong $M-\theta$; bắt buộc đo DIC, FBG, ảnh nhiệt. |
| **G05** | HIGH | Packet W08 gán sai chuyển pha uốn thuần cho S2a Carboni | `VERIFIED` | Đính chính 100%: S2a là cáp thép (ST49); S1a mới là NiTi chịu kéo-uốn kết hợp. |
| **G06** | HIGH | Đánh đồng tồn tại mô hình, khớp số liệu và validation | `VERIFIED` | Thiết lập Thang bậc 5 tầng về độ tin cậy mô hình; yêu cầu locked parameters. |
| **G07** | HIGH | Dùng kết quả Reedlunn 2013 vượt quá phạm vi | `VERIFIED` | Hiệu chỉnh bảo thủ: Sai số do rút gọn động học cáp xoắn dốc, không áp cho bó thẳng. |
| **G08** | HIGH | Bù trừ tham số trong phép khớp uốn $(\mu \cdot \alpha_{\text{trans}})$ | `VERIFIED` | Quy tắc khóa tham số độc lập; cảnh báo bẫy tính kép độ mềm. |
| **G09** | HIGH | Ánh xạ áp suất buồng $p \to f_n$ chưa kiểm chứng | `VERIFIED` | Phân tích tổn thất qua màng và hiệu ứng vòm; yêu cầu hiệu chuẩn độc lập $f_n$. |
| **G10** | HIGH | Chưa thỏa stop condition nhưng nói quá về khoảng trống | `VERIFIED` | Minh bạch hóa stop condition = false; chuyển sang giả thuyết sống sót tạm thời. |
| **G11** | HIGH | Xung đột nhãn `established` trong audit JSON | `VERIFIED` | Hòa giải: `established` áp dụng cho việc bác bỏ H0a; đối với H1 là `insufficient`. |
| **G12** | MEDIUM | Độ cứng uốn chưa định nghĩa theo lịch sử tải | `VERIFIED` | Chuẩn hóa 3 định nghĩa toán học: độ cứng tiếp tuyến, cát tuyến và động học. |

---

## Chương 21: Mechanics Core còn Sống sót Tạm thời và Giới hạn Hiệu lực (Provisional Surviving Mechanics Core & Validity Limits)

`[AUDIT VERDICT]` Sau khi rà soát và loại bỏ toàn bộ các tuyên bố quá mức, câu hỏi cơ học duy nhất còn sống sót tạm thời của đề tài được phát biểu như sau:

> **"Dưới điều kiện áp suất giam giữ hướng kính/ngang biến thiên độc lập ($p(t)$), các quá trình chuyển tiếp dính – trượt một phần – trượt toàn phần, sự phân bố chuyển pha siêu đàn hồi và độ cứng uốn tiếp tuyến của bó dây NiTi có thể được dự đoán chính xác bởi khung lý thuyết NiTi cấu thành – tiếp xúc Coulomb hiện hữu (H0b) với các tham số đo độc lập hay không; và nếu thất bại thì cơ chế vi mô nào chịu trách nhiệm cho sự sai lệch đó?"**

### Giới hạn Hiệu lực Nghiêm ngặt (Validity Limits):
1. **Không phải Tính mới Vật liệu:** Không được viện dẫn việc "dùng hợp kim NiTi thay thép" làm đóng góp khoa học.
2. **Không phải Tính mới Thiết bị:** Không được khẳng định kiến trúc ngón tay hay bộ truyền động piston là mới.
3. **Phụ thuộc Miền Biến dạng:** Giả thuyết chỉ có ý nghĩa nếu thực nghiệm kích hoạt được Miền Cùng Tồn Tại (Coexistence Domain: uốn gập sâu hoặc có lực kéo dọc trục đồng thời). Nếu biến dạng uốn nhỏ dưới 0.75%, câu hỏi cơ học tự động thoái hóa về bài toán kẹt dây đàn hồi đã biết.

---

## Chương 22: Tiêu chí Bác bỏ Dứt điểm (Definitive Kill Criteria)

`[AUDIT VERDICT]` Đề tài MP1 sẽ bị **BÁC BỎ HOÀN TOÀN (`REJECT` / `KILL`)** nếu xảy ra bất kỳ một trong 6 điều kiện sau:

1. **Khung lý thuyết H0b dự đoán thành công:** Nếu mô hình FEA hoặc giải tích hiện hữu (kết hợp luật NiTi Auricchio/Graesser và ma sát Coulomb) với các tham số đo độc lập dự đoán được mô-men uốn và độ cứng uốn trong dải dung sai thực nghiệm mà không cần hiệu chỉnh lại tham số.
2. **Miền vận hành thực tế không kích hoạt chuyển pha:** Nếu đo đạc nhiệt độ và biến dạng cục bộ cho thấy trong suốt dải uốn của ngón tay robot, dây NiTi hoàn toàn ở pha Austenite đàn hồi ($E = E_A$). Khi đó bài toán thoái hóa 100% về kẹt sợi đàn hồi H0a.
3. **Phát hiện công trình tiền nhiệm tương đương:** Nếu quy trình tra cứu trích dẫn ngược (B11, B12) tìm thấy một công trình trong ngành cơ học cáp đã giải quyết chính xác bài toán uốn dưới áp suất thay đổi trên bó dây kim loại siêu đàn hồi.
4. **Sai lệch mô hình biến mất sau khi sửa điều kiện biên:** Nếu sự sai khác giữa mô phỏng và thực nghiệm được giải quyết hoàn toàn bằng việc hiệu chuẩn lại lực kéo ngàm, độ cứng màng bao cao su hoặc hình học bó dây mà không cần đổi luật vật liệu.
5. **Mô hình vĩ mô tương đương kiểu Fang đạt độ chính xác tương đương:** Nếu một macromodel đơn giản dự đoán được toàn bộ đáp ứng cần thiết cho điều khiển robot, làm triệt tiêu giá trị gia tăng của việc nghiên cứu tiếp xúc vi mô.
6. **Không thể nhận diện cơ chế do nhiễu thực nghiệm:** Nếu độ không đảm bảo đo (measurement uncertainty) của ma sát và áp lực vòm lớn hơn độ biến thiên độ cứng dự kiến do chuyển pha gây ra.

---

## Chương 23: Kế hoạch Kiểm chứng và Thực nghiệm Phân biệt Tối thiểu (Minimum Decisive Experiment)

`[INFERENCE]` Để thực hiện kiểm chứng khách quan câu hỏi cơ học còn lại, kế hoạch thực nghiệm phân biệt tối thiểu bắt buộc phải gồm 4 giai đoạn:

```
GIAI ĐOẠN 1: Hiệu chuẩn Độc lập (Locked Calibration)
├── Đo tham số NiTi (E_A, E_M, σ_Ms, σ_Mf, σ_As, σ_Af) trên dây đơn.
├── Đo hệ số ma sát μ trên tiếp xúc 2 dây chéo dưới tải pháp tuyến f_n.
└── Hiệu chuẩn truyền áp p -> f_n qua màng bao đàn hồi.
                         │
                         ▼
GIAI ĐOẠN 2: Thí nghiệm Uốn Phân biệt Cơ chế (Discrimination Test)
├── Cố định độ cong κ, thay đổi áp suất p(t) (Kiểm tra phản ứng trượt thuần túy).
├── Cố định áp suất p, uốn chu kỳ κ(t) (Kiểm tra trễ và chuyển pha).
└── Đo đồng thời: Mô-men M, ảnh nhiệt hồng ngoại, biến dạng FBG, và trượt đầu dây.
                         │
                         ▼
GIAI ĐOẠN 3: Đối chứng Dự đoán Mô hình H0b (Forward Prediction)
├── Chạy mô hình H0b với tham số ĐÃ KHÓA từ Giai đoạn 1.
└── So sánh sai số dự đoán |M_pred - M_exp| với dải không chắc chắn đo đạc.
                         │
                         ▼
GIAI ĐOẠN 4: Ra Quyết định Khoa học (Final Verdict)
├── Sai số nằm trong dải dung sai -> XÁC NHẬN H0b (H1 BỊ BÁC BỎ).
└── Sai số vượt dải dung sai có tính lặp lại -> ĐIỀU TRA H1.
```

---

## Chương 24: Kết luận Khoa học và Khuyến nghị Chiến lược cho Luận văn (Strategic Recommendations for Thesis)

`[AUDIT VERDICT]` 

### 1. Kết luận Khoa học Tổng kết
- Đề tài ban đầu của Mentor về "chế tạo ngón tay robot kẹt dây NiTi áp suất dương tích hợp piston" **không còn tính mới ở cấp độ kiến trúc thiết bị**. Mọi nỗ lực bảo vệ tính mới bằng cách thay đổi hình học, vật liệu hay tích hợp linh kiện đều đã bị tiền nhiệm chiếm lĩnh (`PREEMPTED`).
- Việc chuyển dịch sang bài toán cơ học tiếp xúc NiTi chịu áp suất giam giữ là một bước đi hợp lý, nhưng đề tài **chưa chứng minh được sự cần thiết của một lý thuyết cơ học mới (H1)**. Khung lý thuyết hiện hữu kết hợp cấu thành NiTi và ma sát tiếp xúc (H0b) vẫn là giả thuyết cạnh tranh mạnh nhất và chưa bị bác bỏ.

### 2. Khuyến nghị Chiến lược cho Học viên Thạc sĩ
1. **Định vị lại Đề tài Luận văn từ "Sáng chế Thiết bị" sang "Cơ học Thực nghiệm Đối chứng":**
   Tên đề tài nên chuyển thành:
   > *"Đánh giá giới hạn dự đoán của mô hình cấu thành – tiếp xúc hiện hữu cho bó dây hợp kim nhớ hình NiTi chịu uốn dưới áp suất giam giữ thay đổi"*
   (Validity Limits of Established Constitutive-Contact Frameworks for Superelastic NiTi Wire Bundles under Variable Confinement Bending).
2. **Giá trị Khoa học của Luận văn:**
   - Một luận văn Thạc sĩ thực hiện nghiêm ngặt quy trình kiểm chứng thực nghiệm đối đầu, chứng minh rằng mô hình H0b là **đủ** hoặc chỉ ra chính xác giới hạn mà H0b **thất bại** là một công trình khoa học có giá trị xuất bản cao tại các tạp chí cơ học thực nghiệm uy tín (như *Experimental Mechanics*, *Smart Materials and Structures*, hoặc *Mechanisms and Machine Theory*).
   - Tuyệt đối tránh việc đưa ra các tuyên bố tính mới phóng đại để không bị hội đồng phản biện bác bỏ dựa trên các công trình tiền nhiệm từ 2013–2026 đã nêu trong báo cáo này.
