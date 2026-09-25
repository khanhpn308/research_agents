# Báo cáo Tái cấu trúc Lịch sử và Dòng dõi Khoa học MP1 (MP1 State & Scientific Lineage Reconstruction Report)

> **Mã công việc:** `MP1-E1-W2-01`  
> **Vai trò:** MP1 Worker W2-01 (Chế độ Read-Only State/History Reconstruction)  
> **Mô hình thực hiện:** Gemini 3.8 Flash (Reasoning Effort: HIGH)  
> **Thời điểm tái cấu trúc:** 2026-09-25  
> **Phạm vi khóa (Scope Lock):** Chỉ thực hiện tái cấu trúc trạng thái lịch sử dựa trên tài liệu lưu trữ và Git history. Không tìm kiếm tài liệu mới; không phán quyết tính mới; không so sánh MP1 với D1 ngoài việc ghi nhận quyết định canonical đã có; không sửa đổi các tệp nguồn lịch sử.

---

## Tóm tắt Điều hành (Executive Summary)

Báo cáo này tái cấu trúc toàn diện và trung thực tiến trình tiến hóa khoa học của hướng nghiên cứu **MP1** (xuất phát từ ý tưởng đề xuất của Mentor) từ thời điểm khởi xướng (2026-09-22) qua hai vòng kiểm chứng độc lập `MP1-V001` và `MP1-V002`, đợt phản biện đối kháng của GPT-5.6 Astra, chương trình khắc phục Stage 3, đóng phủ sóng trích dẫn Stage 4 (15/15 nhánh), thẩm định cuối cùng Stage 5 (`SURVIVES_TARGETED_CITATION_CHASE`), và phán quyết liên hướng Stage 6 (`D1_M1` được chọn có điều kiện; MP1 được lưu trữ như một phương án thay thế có giá trị khoa học).

Mọi chuyển tiếp trạng thái đều được neo vào **mã Git commit chính xác** được truy xuất từ lịch sử repository, tuân thủ nguyên tắc **State-at-Time** (phản ánh đúng nhận thức và bằng chứng tại từng thời điểm lịch sử, không viết lại quá khứ bằng nhận thức hiện tại).

---

## 1. Trả lời 16 Câu hỏi Lịch sử Cốt lõi (Questions A–P)

### A. Ý tưởng Đề xuất Ban đầu của Mentor (Mentor Proposal)
- **Thời điểm:** Phase 10 (2026-09-22 10:52:38 +0700 | Commit `0fdbf89fea7f1cd18c64db93c1029c5e499e5a9f`).
- **Nội dung đề xuất:** Một khâu chấp hành hoặc ngón tay robot mềm biến đổi độ cứng uốn dựa trên:
  ```text
  bó dây hợp kim nhớ hình NiTi siêu đàn hồi
  + giam giữ bằng áp suất dương
  + hiện tượng kẹt ma sát giữa các sợi dây (inter-wire jamming)
  + nguồn áp suất xi lanh/piston thu nhỏ dẫn động bằng SMA tích hợp
  ```
- **Quyết định phương pháp luận:** Không chấp nhận hoặc bác bỏ theo trực giác. Mở MP1 như một hướng nghiên cứu thay thế chịu kiểm chứng đối kháng độc lập theo nguyên tắc: *"Do not defend the current idea. Try to falsify it using closest prior work"*. Giữ nguyên D1/M1 làm hướng baseline.

### B. Phân rã Khẳng định Ban đầu C1–C8 (Initial Claim Decomposition)
- **Thời điểm:** Phase 10/11 (2026-09-22 10:52:41 +0700 | Commit `2e3a1a5d399c8bfc52c4ba5d0e926c9117891d79`).
- **Phân rã thành 8 claims:**
  - **C1:** Kẹt sợi/dây kim loại tạo biến đổi độ cứng là mới.
  - **C2:** Kẹt bằng áp suất dương là mới.
  - **C3:** Kết hợp SMA và jamming trong cùng thiết bị là mới.
  - **C4:** Nguồn áp suất tích hợp/nhỏ gọn là mới.
  - **C5:** Dây NiTi siêu đàn hồi tự thân làm môi trường ma sát trượt.
  - **C6:** Áp suất dương trực tiếp giam giữ bó dây NiTi.
  - **C7:** Ghép cặp siêu đàn hồi NiTi, trượt ma sát, áp suất và độ cứng uốn.
  - **C8:** Cơ cấu xi lanh/piston SMA cấp áp suất kẹt là đóng góp khoa học mới.

### C. Kết quả Vòng Kiểm chứng MP1-V001 (MP1-V001 Findings)
- **Thời điểm:** Phase 11 (2026-09-22 16:00:18 +0700 | Commit `1a5e1f20072cf7fe0e969feb1ab868a20138c1d7`).
- **Tập bằng chứng:** Ma trận 10 bài báo toàn văn PDF (`outputs/verification/MP1-V001/verification_matrix.json`).
- **Phán quyết:** `PIVOT_TO_MECHANICS_CORE` với độ tin cậy cao (`confidence = high`).
  - C1: `closed` bởi Bai et al. (2022) và Zhang & Yao (2026).
  - C2: `closed` bởi Liu et al. (2021) và Zhang & Yao (2026).
  - C3: `closed` bởi dòng công trình Takashima (2010–2015) và Matsumoto et al. (2022).
  - C4: `closed` bởi bơm vi mô tích hợp Huynh et al. (2022) và piston động cơ Wang et al. (2024).
  - C8: `substantially_preempted` (thay thế bộ chấp hành bơm, không tạo nguyên lý cơ học mới).
  - C5, C6, C7: `open_in_supplied_corpus`.

### D. Mất đi và Thu hẹp Tính mới Cấp Kiến trúc Rộng (Loss/Narrowing of Broad Architecture Novelty)
- **Hệ quả của V001:** Toàn bộ tính mới ở cấp độ tích hợp thiết bị (device-level combination) bị xóa bỏ. Việc ghép dây kim loại + áp suất dương + bơm nhỏ gọn không thể đứng vững trước các công bố 2021–2026.
- **Bài học phương pháp luận:** Khác biệt về tổ hợp linh kiện không tự tạo ra tính mới khoa học nếu không làm phát sinh câu hỏi cơ học mới chưa từng được giải quyết.

### E. Quyết định Chuyển hướng sang Cơ học Tiếp xúc Lõi (Decision to Pivot to Mechanics Core)
- **Cơ sở quyết định:** Thay vì bảo vệ ý tưởng thiết bị, đề tài rút lui chiến lược về câu hỏi cơ học tiếp xúc: *Liệu sự tương tác giữa áp suất giam giữ, hiện tượng trượt ma sát giữa các dây và phản ứng siêu đàn hồi của NiTi có tạo ra đáp ứng uốn và trễ mà các mô hình tiếp xúc hiện hữu không dự đoán được hay không?*

### F. Định nghĩa Ba Mục tiêu T1, T2, T3 (Definition of Targets T1 / T2 / T3)
- **Thời điểm:** Phase 12/13 (2026-09-22 10:52:43 +0700 | Commit `8494d02ff7c1c57184ab5770baf006bc79d4ddbb`).
- **T1:** Dây NiTi tiếp xúc và trượt ma sát tương đối tạo độ cứng uốn.
- **T2:** Áp suất dương ngoài nén hướng kính bó dây kim loại/NiTi, làm đổi lực pháp tuyến và độ cứng uốn.
- **T3:** Ghép cặp phản ứng siêu đàn hồi NiTi với tiếp xúc/trượt, áp suất giam giữ, trễ và độ cứng.
- **Phép thử tiêu diệt (Parameter-Substitution Kill Test):** Nếu chỉ cần thay thế tham số vật liệu NiTi vào khung lý thuyết sợi đàn hồi tiếp xúc đã biết là đủ dự đoán đáp ứng, mechanics core của MP1 bị bác bỏ.

### G. Thiết lập Vòng Kiểm chứng MP1-V002 (Creation of MP1-V002)
- **Mục tiêu:** Không quay lại tìm kiếm diện rộng; chuyển sang quy trình tra cứu trích dẫn có mục tiêu (targeted citation chasing) xuôi và ngược quanh các anchor papers trong lĩnh vực cáp kim loại, cáp ngầm và cáp NiTi.

### H. Thu thập Bài báo Toàn văn và Ma trận Bằng chứng (Full-Text Evidence Matrix Evolution)
- **Giai đoạn 8 bài (Phase 14, commit `e9685a6`):** Thu thập ban đầu 8 bài (Carboni 2015/2016, Vahidi 2022, Ting-Long 2021, Falcetelli 2024, Xin Liu 2013, Tjahjanto 2017, de Paula 2021). Kết quả: T1 đóng, T2 mở, T3 bị đón đầu phần lớn.
- **Giai đoạn 10 bài (Phase 16–18, commit `5bb0c90`):** Sàng lọc 187 trích dẫn, phát hiện 0 kill trực tiếp, nâng cấp 2 bài kiểm tra thay thế tham số: Reedlunn et al. (2013, Part II) và Fang et al. (2019). Kết quả thử nghiệm thay thế tham số: `insufficient`.
- **Giai đoạn 16 bài (Phase 22, commit `8ccfa3c`):** Bổ sung đầy đủ 16 bài báo toàn văn PDF, khóa ma trận chính thức tại commit HEAD.

### I. Trích xuất Các Gói Bằng chứng Giai đoạn 1 (Stage 1 Mechanics Trace Packets)
- **Thời điểm:** Phase 22 Stage 1 (2026-09-25 15:28:00 +0700 | Commit `af9e7a59b101ac68334eadc9ede33b1b48236622`).
- **Nội dung:** Gemini Flash xây dựng 11 gói trích xuất cơ học chuyên sâu (W01–W11) truy vết từng tuyên bố khoa học với các đoạn trích từ tệp PDF gốc, thiết lập hồ sơ bàn giao sang Astra.

### J. Phản biện Khoa học Đối kháng Astra G01–G12 (Stage 2 Astra Adversarial Critique)
- **Thời điểm:** Phase 22 Stage 2 (2026-09-25 16:06:18 +0700 | Commit `8ccfa3c31d19dde1c87f5653b401fd2afb5d786d`).
- **Kết quả:** GPT-5.6 Astra nêu 12 lỗ hổng nghiêm trọng G01–G12:
  - Bác bỏ mô-đun hằng không chứng minh cần lý thuyết mới (G01);
  - Áp suất chủ động P3 chỉ là điều kiện biên (G02);
  - Chưa chứng minh miền cùng tồn tại chuyển pha + trượt (G03);
  - Đường cong uốn vĩ mô không nhận diện riêng được cơ chế (G04);
  - Gói W08 gán sai cấu hình cáp thép S2a của Carboni thành NiTi (G05);
  - Đánh đồng mô hình toán, khớp số liệu và kiểm chứng nhân quả (G06);
  - Dùng sai số rút gọn động học của Reedlunn quá mức (G07);
  - Nguy cơ bù trừ tham số khi khớp trễ uốn theo Fang 2019 (G08);
  - Chưa kiểm chứng truyền áp buồng sang lực pháp tuyến tiếp xúc (G09);
  - Chưa đạt điều kiện dừng trích dẫn (G10);
  - Xung đột trạng thái giữa Audit JSON (`established`) và handoff (`insufficient`) (G11);
  - Chưa chuẩn hóa định nghĩa độ cứng uốn (G12).

### K. Chương trình Khắc phục Khoa học Giai đoạn 3 (Stage 3 W01–W11 Remediation)
- **Thời điểm:** Phase 22 Stage 3 (2026-09-25 16:29:55 +0700 | Commit `3a216d680b6e5d4c263121afee0577ac86e530ac`).
- **Thực thi:** Gemini hoàn tất 11 báo cáo khắc phục W01–W11, ma trận đối soát G01–G12, và báo cáo khoa học 24 chương (`MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md`). Tiếp thu 100% phản biện của Astra, không che giấu bất kỳ điểm yếu nào.

### L. Tái Cấu trúc Ba Tầng Giả thuyết H0a / H0b / H1 (Restructuring of H0a, H0b, H1)
- **Sửa chữa cốt lõi:**
  - **$H_{0a}$ (Naive Elastic Substitution):** Thay thế mô-đun đàn hồi bằng một hằng số $E = \text{const}$. **BỊ BÁC BỎ (`REFUTED`)** trong miền có chuyển pha siêu đàn hồi.
  - **$H_{0b}$ (Existing Transformation-Aware NiTi Constitutive + Coulomb Contact):** Sử dụng các mô hình cấu thành NiTi phi tuyến hiện hữu (Auricchio, Graesser-Cozzarelli) ghép với tiếp xúc ma sát Coulomb dưới áp suất biến thiên $p(t)$. **CHƯA BỊ BÁC BỎ (`NOT FALSIFIED`)**. Đây là đối thủ khoa học mạnh nhất của MP1.
  - **$H_1$ (Novel Distinct Constitutive-Contact Coupling):** Khẳng định bắt buộc phải có một định luật cơ học vi mô hoàn toàn mới. **CHƯA ĐỦ BẰNG CHỨNG (`INSUFFICIENT EVIDENCE`)**. Không được suy diễn từ việc $H_{0a}$ thất bại sang kết luận $H_1$ đúng.

### M. Quy trình Tra cứu Trích dẫn Có Mục tiêu (Targeted Citation Chase Execution)
- **Các nhánh tra cứu:** Thực hiện qua Scopus API và sàng lọc thủ công trên 15 hướng trích dẫn có mục tiêu quanh các bài báo tiền nhiệm trực tiếp (Bai 2022, Liu 2021, Zhang & Yao 2026, Takashima, Matsumoto, Wang 2024, Carboni 2015/2016, Vahidi 2022, Kang 2020, Silva 2022, Barsi 2025, Xin Liu 2013, Tjahjanto 2017).

### N. Xử lý và Đóng Hai Nhánh Cuối B11 và B12 (B11 / B12 Closure)
- **Thời điểm:** Phase 23 (2026-09-25 16:17:32 - 16:27:35 +0700 | Commits `14444e5`, `313cdf2`).
- **Nội dung:**
  - B11: Sàng lọc 22 tài liệu trích dẫn ngược của Kang et al. (2020, DOI: `10.3901/JME.2020.14.065`).
  - B12: Sàng lọc 46 tài liệu trích dẫn ngược của Barsi, Carboni & Lacarbonara (2024/2025, DOI: `10.1016/j.engstruct.2024.119217`).
  - Tổng số bản ghi thô: 68 bản ghi (67 bản ghi duy nhất).
  - Kết quả: Không phát hiện bất kỳ công trình nào công bố chuỗi cơ học uốn bó dây NiTi dưới áp suất giam giữ chủ động biến thiên.

### O. Hoàn thành Phủ sóng Trích dẫn 15/15 (Citation Coverage Reaching 15/15)
- **Chỉ số bao phủ canonical:**
  - Trích dẫn ngược (backward): `9/9` hướng đã duyệt.
  - Trích dẫn xuôi (forward): `6/6` hướng đã duyệt.
  - Tổng số hướng: `15/15` hướng hoàn thành (`100%`).
  - `all_required_directions_screened = true`.
  - `no_unresolved_high_threat_source = true`.
  - `stop_condition.satisfied = true`.
  - `search_cutoff_date = 2026-09-25`.
- **Nguyên tắc khoa học:** Thỏa mãn điều kiện dừng trích dẫn là một sự hoàn tất trong phạm vi giao thức (protocol closure), không phải là bằng chứng toán học chứng minh không tồn tại tài liệu trùng lặp ở bất kỳ đâu trên thế giới.

### P. Phán quyết Thẩm định Cuối cùng MP1-V002 (Final MP1-V002 Adjudication)
- **Thời điểm:** Phase 24 (2026-09-25 16:36:09 +0700 | Commit `73b635433237f2682accd4b7799c566fe1e80871`).
- **Mô hình thẩm định:** GPT-6 Sol High (Run ID: `20260925T093414Z`).
- **Kết quả:**
  ```text
  protocol_outcome           = SURVIVES_TARGETED_CITATION_CHASE
  confidence                 = high
  direct_kill_found          = false
  citation_coverage_closed   = true
  msc_topic_readiness        = READY_FOR_CROSS_DIRECTION_COMPARISON
  astra_escalation_required  = false
  ```
- **Ý nghĩa phán quyết:** MP1 sống sót trong phạm vi giao thức V002 như một câu hỏi phân biệt mô hình hẹp ($H_{0b}$ vs $H_1$). Đủ điều kiện đưa vào so sánh đối đầu với baseline D1/M1.

---

## 2. So sánh Trạng thái tại Thời điểm vs Trạng thái Chuẩn hóa Hiện tại (State-at-Time vs Canonical)

| Khía cạnh Khoa học | Trạng thái tại Thời điểm Lịch sử (State-at-Time) | Trạng thái Chuẩn hóa Hiện tại tại HEAD (Current Canonical) | Lý do Thay đổi / Hiệu chỉnh |
|:---|:---|:---|:---|
| **Cấp độ Tính mới** | **Giai đoạn S01:** Tính mới ở cấp độ lắp ghép hệ thống thiết bị (wire jamming + positive pressure + SMA piston). | Tính mới cấp thiết bị bị bác bỏ hoàn toàn; chỉ còn câu hỏi phân biệt mô hình tiếp xúc uốn dưới áp suất giam giữ. | Các công trình tiền nhiệm 2021–2026 (Bai, Liu, Zhang-Yao, Takashima, Huynh, Wang) đã chiếm lĩnh toàn bộ nguyên lý thiết bị. |
| **Bản chất Áp suất P3** | **Giai đoạn S05/S06:** Áp suất chủ động biến thiên $P_3$ được coi là một nguyên lý cơ học mới làm phát sinh tính mới. | Áp suất chủ động chỉ là một điều kiện biên điều khiển thực nghiệm (boundary condition / protocol). | Phương trình tiếp xúc Coulomb vi phân trong y văn hiện hữu (Xin Liu, Tjahjanto, Barsi) tự nhiên tiếp nhận $p(t)$ mà không cần luật vật lý mới. |
| **Phép thử Thay thế Tham số** | **Giai đoạn S05/S08:** Khung nhị phân $H_0$ (thay thế tham số) vs $H_1$ (luật ghép cặp mới). | Khung 3 tầng: $H_{0a}$ (mô-đun hằng: Bác bỏ); $H_{0b}$ (mô hình NiTi + tiếp xúc hiện hữu: Chưa bị bác bỏ); $H_1$ (Chưa đủ bằng chứng). | Astra chỉ ra việc bác bỏ $H_{0a}$ không có nghĩa $H_1$ đúng; $H_{0b}$ là đối thủ chính chưa bị loại. |
| **Dữ liệu Thực tế Carboni 2015** | **Giai đoạn S09 (Packet W08):** Khẳng định cấu hình S2a chứng minh chuyển pha NiTi dưới uốn thuần túy. | Đính chính: S2a là cáp thép ST49 thuần ma sát; S1a mới là cáp NiTi7 chịu ứng suất kéo-uốn kết hợp. | Kiểm tra trực tiếp Bảng 4 tệp PDF Carboni 2015 theo phản biện Astra G05. Suy luận sai bị loại bỏ hoàn toàn. |
| **Quy mô Ma trận Toàn văn** | **Giai đoạn S06:** 8 bài báo.<br>**Giai đoạn S08:** 10 bài báo. | **16 bài báo toàn văn PDF** được nạp và phân tích đầy đủ tại commit HEAD. | Mở rộng tài liệu có kiểm soát để giải quyết dứt điểm các lỗ hổng đối kháng của Astra và bao phủ các dòng cáp ngầm, bện vi sợi. |
| **Điều kiện Dừng Trích dẫn** | **Giai đoạn S12 (Stage 3 report):** `stop_condition_satisfied = false`, B11 và B12 chưa đóng. | `stop_condition.satisfied = true`, `15/15` hướng hoàn thành, `search_cutoff_date = 2026-09-25`. | Giai đoạn 4 đã hoàn tất việc sàng lọc 68 bản ghi của B11 và B12 trước khi chạy final adjudication. |
| **Định vị Đề tài Luận văn** | **Giai đoạn S14:** MP1 sẵn sàng cho nghiên cứu thực nghiệm luận văn Thạc sĩ (`msc_topic_readiness = READY`). | **D1/M1 được chọn có điều kiện** (`LOCK_WITH_FEASIBILITY_GATE`); MP1 được lưu trữ như một **viable alternative** không hoạt động. | Phán quyết liên hướng đánh giá D1/M1 có rủi ro thực thi thấp hơn, câu hỏi rõ ràng hơn, và kết quả phủ định vẫn có giá trị khoa học cao. |

---

## 3. Quản trị Bất đồng và Mâu thuẫn Dữ liệu Lịch sử (Contradiction Candidates)

Đã nhận diện và ghi nhận 6 mâu thuẫn dữ liệu lịch sử trong `W2_01_CONTRADICTION_CANDIDATES.json`:

1. **`CONTRA-01` (Quy mô ma trận 10 vs 13 vs 16 bài):** Mâu thuẫn giữa handoff cũ và snapshot trên đĩa trong Stage 2. Đã hòa giải tại Stage 3: Khóa chính thức 16 bài tại commit HEAD (`8ccfa3c`).
2. **`CONTRA-02` (Nhãn thay thế tham số `established` vs `insufficient`):** Tệp audit JSON ghi `established` trong khi handoff ghi `insufficient`. Đã hòa giải: `established` áp dụng cho việc bác bỏ $H_{0a}$; trạng thái giữa $H_{0b}$ và $H_1$ là `insufficient`.
3. **`CONTRA-03` (Cấu hình Carboni 2015 S2a vs S1a):** W08 gán sai S2a là NiTi uốn thuần. Đã hòa giải: S2a là cáp thép ST49; S1a là NiTi7 kéo-uốn. Tuyên bố sai bị bóc tách khỏi chuỗi chứng minh.
4. **`CONTRA-04` (Trạng thái điều kiện dừng trích dẫn `false` vs `true`):** Báo cáo Stage 3 ghi `false` do viết trước khi duyệt B11/B12; tệp canonical JSON ghi `true` do viết sau Stage 4. Canonical JSON có quyền ưu tiên cao hơn narrative text cũ.
5. **`CONTRA-05` (Bản chất áp suất chủ động P3):** Từ "nguyên lý cơ học mới" chuyển thành "điều kiện biên tải trọng ngoài". Bỏ hoàn toàn tuyên bố tính mới dựa trên việc điều khiển áp suất.
6. **`CONTRA-06` (Định vị đề tài MP1):** Từ "đề tài ứng viên sẵn sàng thực thi" chuyển thành "phương án thay thế có giá trị khoa học được lưu trữ". Quyết định liên hướng ưu tiên D1/M1 vì lý do quản trị rủi ro luận văn.

---

## 4. Xác nhận Chất lượng và Tuân thủ Quy trình (QA Verification)

- [x] **Toàn bộ các giai đoạn chính của MP1 được tái hiện đầy đủ:** Từ đề xuất của mentor đến phân rã C1–C8, V001, rút về mechanics core, V002, trace packets, phản biện Astra, khắc phục Stage 3, đóng trích dẫn Stage 4, final adjudication Stage 5, và so sánh liên hướng Stage 6.
- [x] **Mọi chuyển tiếp trạng thái đều có provenance:** 15 chuyển tiếp đều có tệp nguồn, nguyên nhân kích hoạt và kết quả khoa học.
- [x] **Mã Git commit chính xác được ghi nhận:** 100% các trạng thái S01–S16 và chuyển tiếp T01–T15 đều có commit hash cụ thể, không sử dụng commit giả mạo hay nhãn UNKNOWN không cần thiết.
- [x] **Phân tách rành mạch trạng thái tại thời điểm và canonical:** Tuân thủ nghiêm ngặt quy tắc State-at-Time.
- [x] **Các diễn giải bị thay thế và được hiệu chỉnh được ghi nhận minh bạch.**
- [x] **Không đưa ra kết luận tính mới chủ quan:** Tuyệt đối không tuyên bố "MP1 là mới" hay "MP1 vượt trội hơn D1".
- [x] **Không mở lại tìm kiếm tài liệu:** Tuân thủ quy định đóng tìm kiếm diện rộng.
- [x] **Không sửa đổi tệp nguồn lịch sử:** Mọi hoạt động ghi nhận chỉ diễn ra trong thư mục worker `outputs/execution/MP1-V002/W2-01/`.

---

## 5. Danh mục Tệp Đầu ra của Worker W2-01

Các tệp sau đã được tạo lập đầy đủ tại `outputs/execution/MP1-V002/W2-01/`:

1. `W2_01_STATE_HISTORY_REPORT.md` (Báo cáo tổng kết toàn diện này).
2. `MP1_HISTORICAL_STATE_REGISTER.json` (Sổ đăng ký 16 trạng thái máy đọc được kèm commit IDs).
3. `MP1_HISTORICAL_STATE_REGISTER.md` (Phiên bản Markdown chi tiết cho người đọc).
4. `MP1_HISTORICAL_TRANSITIONS.json` (Sổ đăng ký 15 bước chuyển tiếp lịch sử có cấu trúc).
5. `W2_01_CONTRADICTION_CANDIDATES.json` (Danh mục 6 điểm mâu thuẫn lịch sử và giải pháp xử lý).
6. `W2_01_SOURCE_MANIFEST.json` (Bảng kê khai nguồn tài liệu và cam kết truy xuất).
