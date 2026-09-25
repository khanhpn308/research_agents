# MP1 Stage 1 Packet Matrix (Hồ sơ 11 Gói Bằng chứng Stage 1)

> **Commit:** `af9e7a5`  
> **Source Directory:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/`  
> **Total Packets:** 11  

## 1. Bảng Tổng hợp 11 Gói Bằng chứng Stage 1

| Packet ID | Giai đoạn Lịch sử | Claims Ảnh hưởng | Targets Ảnh hưởng | Papers Cốt lõi | Trạng thái Bằng chứng | Liên kết Phê bình (Stage 2) | Liên kết Khắc phục (Stage 3) |
|:---:|---|:---:|:---:|---|:---:|:---:|:---:|
| **W01** | Stage 1 (Mechanics Trace Packets) | C1, C2, C3, C4, C5, C6, C7, C8 | T1, T2 | `240fbf6022`, `182d854610`, `3aa8790db0`, `2cd907e77a`... | established | G01, G02 | W02, W03 |
| **W02** | Stage 1 (Mechanics Trace Packets) | C1, C2 | None | `240fbf6022`, `182d854610`, `3aa8790db0` | established | G01, G02 | W02 |
| **W03** | Stage 1 (Mechanics Trace Packets) | C3 | T1 | `2cd907e77a`, `7ce492505d`, `99fe24da8b`, `d3b3b6963f` | established | G01, G03 | W02, W03 |
| **W04** | Stage 1 (Mechanics Trace Packets) | C4, C8 | T2 | `bbe88a0c04`, `c6a31066f8`, `de64029540`, `55457a97c6` | established | G02, G09 | W02, W03 |
| **W05** | Stage 1 (Mechanics Trace Packets) | C5, C6, C7 | T1, T2, T3 | `240fbf6022`, `182d854610`, `2cd907e77a`, `c6a31066f8`... | open_in_corpus_only | G01, G02, G03, G10 | W03, W05, W06 |
| **W06** | Stage 1 (Mechanics Trace Packets) | C5, C7 | T1 | `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`... | closed_by_full_text | G05, G06 | W04 |
| **W07** | Stage 1 (Mechanics Trace Packets) | C6 | T2 | `ccdc1bb980`, `aaad9c248c`, `53200aa0c6`, `fac21c950e` | open_in_current_full_text_set | G02, G09, G10 | W05, W08 |
| **W08** | Stage 1 (Mechanics Trace Packets) | C7 | T3 | `d9966f2f5e`, `53200aa0c6`, `98fee47c04`, `e8462758c3`... | substantially_preempted | G03, G05, G11 | W04, W06, W07 |
| **W09** | Stage 1 (Mechanics Trace Packets) | C7 | T1, T3 | `fac21c950e` | closed_for_axial_cable_kinematics | G07 | W10 |
| **W10** | Stage 1 (Mechanics Trace Packets) | C7 | T3 | `2f7fcf2f8f` | parameter_substitution_risk_high | G06, G08, G10 | W07, W09, W10 |
| **W11** | Stage 1 (Mechanics Trace Packets) | C1, C2, C3, C4, C5, C6, C7, C8 | T1, T2, T3 | `00414aac4b`, `fac21c950e`, `40760daa02`, `2f7fcf2f8f`... | stop_condition_unmet | G10, G11 | W01, W11 |

## 2. Chi tiết Từng Gói Bằng chứng

### Gói W01: W01_ORIGINAL_ARCHITECTURE_AND_V001_DECISION.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W01_ORIGINAL_ARCHITECTURE_AND_V001_DECISION.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Tái dựng kiến trúc thiết bị ban đầu từ đề xuất của mentor, phân tích nguyên nhân sụp đổ tính mới ở cấp độ linh kiện trong MP1-V001, và xác định tiền đề chuyển dịch sang mechanics core.
- **Khẳng định ảnh hưởng:** C1, C2, C3, C4, C5, C6, C7, C8 | **Mục tiêu:** T1, T2 | **Giả thuyết:** H0a
- **Mô hình / Phương pháp:** Phân tích cấu trúc hệ thống (subsystem functional decomposition) chia tách cơ cấu jamming, vật liệu thông minh, nguồn áp suất tích hợp và cơ cấu bơm vi mô.
- **Thực nghiệm thảo luận:** Đối soát các hệ thống robot mềm và cơ cấu thay đổi độ cứng thực nghiệm trong y sinh và robot đeo (exoskeletons).
- **Kết luận xác thực:** Sự kết hợp linh kiện cấp thiết bị (wire jamming + SMA + micropump tích hợp) hoàn toàn không có tính mới khoa học; bị tiền nhiệm bởi hàng loạt nghiên cứu từ 2013-2024.
- **Kết luận suy diễn:** Hướng nghiên cứu duy nhất có thể bảo vệ được là đi sâu vào cơ học bản chất (friction, phase transformation, variable normal pressure) thay vì phối hợp linh kiện.
- **Vấn đề chưa giải quyết:** Chưa làm rõ ranh giới giữa việc sụp đổ tính mới linh kiện và việc phát biểu một bài toán cơ học tiếp xúc mới thực sự.
- **Diễn giải bị thay thế:** Từng kỳ vọng việc tích hợp bơm vi mô SMA với cơ cấu jamming dây tạo nên một hệ thống robot mềm mới toàn diện.
- **Diễn giải đã sửa đổi:** Toàn bộ cấu trúc thiết bị C1-C4 và C8 đã bị đóng; chỉ chuyển dịch sang nghiên cứu lõi cơ học (C5-C7, T1-T3) với tư cách một giả thuyết cơ học.
- **Trạng thái & Độ tin cậy:** `established` | `high`
- **Xuất xứ (Provenance):** `W01_ORIGINAL_ARCHITECTURE_AND_V001_DECISION.md#L1-L286`

---
### Gói W02: W02_C1_C2_EVIDENCE.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W02_C1_C2_EVIDENCE.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra toàn diện tính mới của cơ chế wire jamming (C1) và positive-pressure jamming (C2) trong robot mềm.
- **Khẳng định ảnh hưởng:** C1, C2 | **Mục tiêu:**  | **Giả thuyết:** H0a
- **Mô hình / Phương pháp:** Mô hình dầm Euler-Bernoulli có trượt ma sát Coulomb giữa các sợi; mô hình nén dương màng đàn hồi.
- **Thực nghiệm thảo luận:** Thử nghiệm uốn 3 điểm trên dầm dây thép và dầm sợi nylon chịu áp suất dương từ 0 đến 250 kPa; đo lực uốn vĩ mô.
- **Kết luận xác thực:** C1 và C2 hoàn toàn bị đóng (closed by full text). Bai et al. 2022 chứng minh thay đổi độ cứng 15 lần với bó dây thép; Liu et al. 2021 dùng áp suất dương trong đồ gá đeo; Zhang & Yao 2026 lập mô hình sợi nylon chi tiết.
- **Kết luận suy diễn:** Mô hình sợi đàn hồi của Zhang & Yao 2026 có thể được mở rộng sang sợi siêu đàn hồi NiTi hay không là một câu hỏi mở.
- **Vấn đề chưa giải quyết:** Khả năng mô hình đàn hồi hiện có mở rộng sang vật liệu có biến dạng phi tuyến và biến đổi pha.
- **Diễn giải bị thay thế:** Cho rằng wire jamming dưới áp suất dương là một nguyên lý hoạt động mới mẻ chưa được mô hình hóa.
- **Diễn giải đã sửa đổi:** C1 và C2 đóng 100%; không được phép đưa vào novelty claim của luận văn.
- **Trạng thái & Độ tin cậy:** `established` | `high`
- **Xuất xứ (Provenance):** `W02_C1_C2_EVIDENCE.md#L1-L261`

---
### Gói W03: W03_C3_SMA_JAMMING_LINEAGE.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W03_C3_SMA_JAMMING_LINEAGE.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Kiểm chứng chuyên sâu dòng nghiên cứu tích hợp SMA và Jamming (C3) của nhóm Takashima (2022-2024) và Matsumoto (2024).
- **Khẳng định ảnh hưởng:** C3 | **Mục tiêu:** T1 | **Giả thuyết:** H0a
- **Mô hình / Phương pháp:** Kích hoạt nhiệt dây SMA trong môi trường hạt jamming hoặc tấm jamming để điều khiển độ cứng và biến dạng hình học.
- **Thực nghiệm thảo luận:** Tay gắp mềm biến đổi độ cứng kết hợp dây nhiệt SMA và hạt jamming chân không; cơ cấu ngón tay uốn chủ động.
- **Kết luận xác thực:** C3 bị đón đầu thực chất (substantially preempted). Dây SMA được dùng rộng rãi để làm khung trợ lực hoặc kích hoạt biến dạng cho cơ cấu jamming.
- **Kết luận suy diễn:** Các công trình của Takashima dùng dây SMA làm actuator nhiệt hoặc cốt nâng đỡ trong hạt, không phải bó dây NiTi tự trượt ma sát với nhau.
- **Vấn đề chưa giải quyết:** Phân biệt rõ ràng giữa cơ cấu SMA phát nhiệt uốn chủ động và cơ cấu bó dây NiTi siêu đàn hồi tự kẹt ma sát thụ động.
- **Diễn giải bị thay thế:** Cho rằng việc đặt dây SMA vào trong cấu trúc jamming tự nó tạo nên tính mới kiến trúc.
- **Diễn giải đã sửa đổi:** C3 bị đón đầu ở cấp hệ thống; chỉ có bài toán ma sát trượt nội tại giữa các dây NiTi siêu đàn hồi là có thể còn khác biệt về cơ học.
- **Trạng thái & Độ tin cậy:** `established` | `high`
- **Xuất xứ (Provenance):** `W03_C3_SMA_JAMMING_LINEAGE.md#L1-L235`

---
### Gói W04: W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra nguồn áp suất tích hợp trên thân (C4) và cơ cấu piston/bơm vi mô SMA (C8).
- **Khẳng định ảnh hưởng:** C4, C8 | **Mục tiêu:** T2 | **Giả thuyết:** H0a
- **Mô hình / Phương pháp:** Bơm vi mô chất lỏng điện liên hợp (ECF), bơm giãn nở nhiệt chất lỏng-khí, và bơm màng/piston dẫn động bằng dây SMA.
- **Thực nghiệm thảo luận:** Đo áp suất đầu ra và lưu lượng của bơm vi mô tích hợp trong cơ cấu chấp hành mềm và thiết bị phân phối thuốc vi mô.
- **Kết luận xác thực:** C4 và C8 hoàn toàn bị đóng / đón đầu thực chất. Bơm vi mô ECF (Huynh 2022), bơm nhiệt vi lưu (Wang 2024), và bơm màng SMA (Pierce 2013, Kotb 2021) đã được phát triển sâu sắc.
- **Kết luận suy diễn:** C8 chỉ là sự thay thế cơ cấu chấp hành (actuator substitution), mang rủi ro bị bác bỏ rất cao nếu coi là đóng góp khoa học chính.
- **Vấn đề chưa giải quyết:** Khả năng đáp ứng tần số và tổn hao nhiệt khi tích hợp bơm thu nhỏ vào thân robot mềm.
- **Diễn giải bị thay thế:** Xem nguồn bơm tích hợp SMA là một trụ cột novel của đề tài luận văn.
- **Diễn giải đã sửa đổi:** Loại bỏ hoàn toàn C4 và C8 khỏi trọng tâm nghiên cứu; áp suất chỉ được xem như điều kiện biên điều khiển $p(t)$.
- **Trạng thái & Độ tin cậy:** `established` | `high`
- **Xuất xứ (Provenance):** `W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md#L1-L299`

---
### Gói W05: W05_C5_C6_C7_V001_BOUNDARY.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W05_C5_C6_C7_V001_BOUNDARY.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Xác định ranh giới thẩm tra của C5, C6, C7 sau MP1-V001 và sự hình thành của Mechanics Core.
- **Khẳng định ảnh hưởng:** C5, C6, C7 | **Mục tiêu:** T1, T2, T3 | **Giả thuyết:** H0a, H1
- **Mô hình / Phương pháp:** Ma trận giao thoa 3 trục: (1) Siêu đàn hồi/chuyển pha NiTi x (2) Trượt ma sát giữa các dây x (3) Áp suất giam giữ chủ động.
- **Thực nghiệm thảo luận:** Rà soát toàn bộ 11 bài báo trong tập V001 để tìm xem có bài báo nào giao thoa cả 3 trục hay không.
- **Kết luận xác thực:** Trong phạm vi 11 bài báo V001, không có công trình nào chứa cả 3 thành phần này cùng lúc.
- **Kết luận suy diễn:** Hình thành đề xuất Mechanics Core dựa trên giao điểm 3 trục này và coi đây là khoảng trống khoa học tiềm năng.
- **Vấn đề chưa giải quyết:** Việc một giao điểm 'mở trong 11 bài báo V001' không đồng nghĩa với việc nó là khoảng trống mở trong toàn bộ nền khoa học cơ học.
- **Diễn giải bị thay thế:** Nhận định giao điểm 3 trục là novel một cách mặc nhiên chỉ dựa trên ma trận rà soát V001.
- **Diễn giải đã sửa đổi:** Cần kiểm tra kỹ lưỡng với văn hiến cơ học cáp dây truyền thống (wire rope mechanics) trước khi khẳng định tính mới.
- **Trạng thái & Độ tin cậy:** `open_in_corpus_only` | `medium`
- **Xuất xứ (Provenance):** `W05_C5_C6_C7_V001_BOUNDARY.md#L1-L160`

---
### Gói W06: W06_T1_NITI_CONTACT_FRICTION.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra chuyên sâu Mục tiêu T1: Cơ học tiếp xúc và ma sát trượt giữa các dây NiTi đã bị tiền nhiệm hay chưa.
- **Khẳng định ảnh hưởng:** C5, C7 | **Mục tiêu:** T1 | **Giả thuyết:** H0a
- **Mô hình / Phương pháp:** Mô phỏng phần tử hữu hạn 3D (Abaqus UMAT), luật tiếp xúc ma sát Coulomb/Hertz, mô hình trễ tiếp xúc Bouc-Wen.
- **Thực nghiệm thảo luận:** Thử nghiệm kéo chu kỳ và uốn chu kỳ trên cáp và tao dây NiTi; đo hệ số ma sát giữa các sợi dây NiTi ($\mu = 0.18 - 0.22$).
- **Kết luận xác thực:** Mục tiêu T1 chính thức bị đóng bằng toàn văn (closed by full text). Vahidi 2022 và Carboni 2015 đã mô hình hóa và đo đạc đầy đủ ma sát tiếp xúc giữa các dây NiTi.
- **Kết luận suy diễn:** Không thể tuyên bố tính mới về mặt hiện tượng ma sát dây NiTi đơn thuần.
- **Vấn đề chưa giải quyết:** Sự phụ thuộc của hệ số ma sát $\mu$ vào trạng thái pha (Austenite vs Martensite) và ứng suất tiếp xúc pháp tuyến lớn.
- **Diễn giải bị thay thế:** Nghi ngờ ma sát tiếp xúc giữa các dây NiTi chưa được nghiên cứu trong cơ học.
- **Diễn giải đã sửa đổi:** Xác nhận T1 đã đóng hoàn toàn; loại bỏ T1 khỏi danh mục các khoảng trống mở.
- **Trạng thái & Độ tin cậy:** `closed_by_full_text` | `high`
- **Xuất xứ (Provenance):** `W06_T1_NITI_CONTACT_FRICTION.md#L1-L339`

---
### Gói W07: W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra ranh giới Mục tiêu T2: Áp suất giam giữ chủ động (Active Confinement Pressure) và sự phân loại P1/P2/P3.
- **Khẳng định ảnh hưởng:** C6 | **Mục tiêu:** T2 | **Giả thuyết:** H0b, H1
- **Mô hình / Phương pháp:** Lý thuyết uốn dầm cáp dưới áp suất ngoài; phân loại áp suất P1 (tiếp xúc thụ động do hình học), P2 (áp suất cố định/thủy tĩnh), P3 (áp suất chủ động biến thiên $p(t)$).
- **Thực nghiệm thảo luận:** Cáp ngầm biển chịu áp suất thủy tĩnh (Tjahjanto 2017); cáp chịu kéo dọc trục sinh lực nén hướng tâm (Xin Liu 2004).
- **Kết luận xác thực:** T2 mở trong tập tài liệu toàn văn hiện tại (open in current full-text set). Các nghiên cứu truyền thống chỉ xét P1 và P2, chưa nghiên cứu sâu P3 trong dầm uốn biến dạng lớn.
- **Kết luận suy diễn:** Xem P3 như một lớp cơ học mới có khả năng tạo ra tính mới khoa học độc lập.
- **Vấn đề chưa giải quyết:** P3 là một quy luật cơ học mới hay thực chất chỉ là một điều kiện biên biến thiên theo thời gian trong phương trình vi phân tiếp xúc hiện hữu.
- **Diễn giải bị thay thế:** Nhận định áp suất chủ động P3 tạo ra một nhánh cơ học mới chưa từng có phương trình.
- **Diễn giải đã sửa đổi:** Hạ cấp P3 thành giao thức điều khiển thực nghiệm (experimental protocol/boundary condition); phương trình vi phân hiện hữu tiếp nhận tự nhiên $p(t)$.
- **Trạng thái & Độ tin cậy:** `open_in_current_full_text_set` | `medium`
- **Xuất xứ (Provenance):** `W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md#L1-L199`

---
### Gói W08: W08_T3_TRANSFORMATION_CONTACT_COUPLING.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra Mục tiêu T3: Sự ghép cặp chuyển pha và tiếp xúc ma sát dây NiTi; kiểm tra mức độ đón đầu của văn hiến.
- **Khẳng định ảnh hưởng:** C7 | **Mục tiêu:** T3 | **Giả thuyết:** H0b, H1
- **Mô hình / Phương pháp:** Mô hình cấu thành nhiệt-cơ ghép cặp tiếp xúc; mô hình trễ thắt (pinched hysteresis) kết hợp siêu đàn hồi và ma sát Bouc-Wen.
- **Thực nghiệm thảo luận:** Thử nghiệm uốn và kéo chu kỳ trên tao dây cáp; quan sát hiện tượng suy giảm chu kỳ và trễ năng lượng.
- **Kết luận xác thực:** Mục tiêu T3 bị đón đầu thực chất (substantially preempted). Các mô hình ghép cặp siêu đàn hồi và ma sát đã được nghiên cứu sâu trong giảm chấn công trình và hàng không.
- **Kết luận suy diễn:** Gán nhầm rằng cấu hình S2a của Carboni 2015 chứng minh chuyển pha siêu đàn hồi trong uốn thuần.
- **Vấn đề chưa giải quyết:** Sai sót dữ liệu thực tế: Cấu hình S2a trong Carboni 2015 thực chất là cáp thép thuần ma sát ST49; S1a mới là cáp NiTi chịu kéo-uốn kết hợp.
- **Diễn giải bị thay thế:** Sử dụng S2a làm bằng chứng cho rằng chuyển pha uốn thuần đã được thực nghiệm chứng minh.
- **Diễn giải đã sửa đổi:** Đính chính triệt để sai sót S2a; chỉ ra rằng Carboni 2015 chỉ thử nghiệm kéo-uốn kết hợp trên S1a, chưa chứng minh uốn thuần.
- **Trạng thái & Độ tin cậy:** `substantially_preempted` | `medium_low`
- **Xuất xứ (Provenance):** `W08_T3_TRANSFORMATION_CONTACT_COUPLING.md#L1-L157`

---
### Gói W09: W09_REEDLUNN_2013_DEEP_AUDIT.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra toàn văn chuyên sâu Reedlunn et al. 2013 (Part II), phân tích cơ chế chuyển pha từng lớp và giới hạn động học Costello.
- **Khẳng định ảnh hưởng:** C7 | **Mục tiêu:** T1, T3 | **Giả thuyết:** H0b, H1
- **Mô hình / Phương pháp:** Lý thuyết cáp xoắn Costello kết hợp luật cấu thành siêu đàn hồi 1D có biến dạng trượt xuyên tâm và đo quang học.
- **Thực nghiệm thảo luận:** Kéo đẳng nhiệt cáp $7\times 7$ và $1\times 27$ NiTi trong bể chất lỏng kiểm soát nhiệt độ; chụp ảnh bề mặt xác định vùng chuyển pha.
- **Kết luận xác thực:** Reedlunn 2013 chứng minh quá trình chuyển pha diễn ra tuần tự từng lớp từ trong ra ngoài; cho thấy áp lực tiếp xúc hướng tâm làm thay đổi ứng suất kích hoạt chuyển pha.
- **Kết luận suy diễn:** Cho rằng việc mô hình Costello thất bại ở lớp ngoài cáp $1\times 27$ chứng minh sự thiếu hụt của lý thuyết tiếp xúc-chuyển pha tổng quát.
- **Vấn đề chưa giải quyết:** Diễn giải quá mức (overclaim) sai số động học cáp xoắn dốc Costello thành sự thất bại của luật cấu thành trong bó dây robot thẳng.
- **Diễn giải bị thay thế:** Dùng sự sai lệch của mô hình Costello trong Reedlunn để làm căn cứ khẳng định cần một phương trình ghép cặp mới.
- **Diễn giải đã sửa đổi:** Thừa nhận sự sai lệch của Reedlunn thuần túy do giả thiết động học thanh xoắn góc lớn bỏ qua uốn/xoắn cục bộ; không suy diễn cho bó dây thẳng.
- **Trạng thái & Độ tin cậy:** `closed_for_axial_cable_kinematics` | `high`
- **Xuất xứ (Provenance):** `W09_REEDLUNN_2013_DEEP_AUDIT.md#L1-L146`

---
### Gói W10: W10_FANG_2019_PARAMETER_SUBSTITUTION.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra sâu Fang et al. 2019 và đánh giá rủi ro của phép thử thay thế tham số (parameter-substitution risk).
- **Khẳng định ảnh hưởng:** C7 | **Mục tiêu:** T3 | **Giả thuyết:** H0a, H0b, H1
- **Mô hình / Phương pháp:** Phần tử thanh dầm OpenSees với mặt cắt sợi siêu đàn hồi và lò xo phi tuyến tự định tâm song song; mô hình suy giảm chu kỳ.
- **Thực nghiệm thảo luận:** Kéo chu kỳ và uốn-cắt trên cơ cấu giảm chấn cáp NiTi; khớp đường cong trễ dạng cờ và sự trơn mượt chuyển pha.
- **Kết luận xác thực:** Mô hình rút gọn của Fang 2019 tái hiện rất tốt hình dạng đường cong trễ vĩ mô bằng cách tinh chỉnh tham số hiện tượng học mà không cần giải phương trình tiếp xúc vi mô.
- **Kết luận suy diễn:** Rủi ro thay thế tham số là cực kỳ nghiêm trọng: một mô hình hiện tượng học hiện có có thể khớp đường cong mà không cần lý thuyết mới.
- **Vấn đề chưa giải quyết:** Phép khớp đường cong vĩ mô không chứng minh được tính nhân quả vật lý; hiện tượng bù trừ giữa ma sát và độ cứng.
- **Diễn giải bị thay thế:** Coi kết quả kiểm tra thay thế tham số là chưa kết luận dứt điểm (insufficient).
- **Diễn giải đã sửa đổi:** Xác nhận H0b (mô hình phi tuyến hiện có) chưa bị bác bỏ; các mô hình hiện tượng học khớp số liệu rất tốt; H1 đòi hỏi bằng chứng nhân quả cục bộ.
- **Trạng thái & Độ tin cậy:** `parameter_substitution_risk_high` | `high`
- **Xuất xứ (Provenance):** `W10_FANG_2019_PARAMETER_SUBSTITUTION.md#L1-L149`

---
### Gói W11: W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md
- **Tệp nguồn:** `outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md` (Commit `af9e7a5`)
- **Câu hỏi trả lời:** Thẩm tra độ bao phủ trích dẫn và tính toàn vẹn của cơ sở dữ liệu nguồn, đánh giá điều kiện dừng tìm kiếm.
- **Khẳng định ảnh hưởng:** C1, C2, C3, C4, C5, C6, C7, C8 | **Mục tiêu:** T1, T2, T3 | **Giả thuyết:** H0a, H0b, H1
- **Mô hình / Phương pháp:** Kiểm toán đồ thị trích dẫn ngược (B01-B08/B12) và trích dẫn xuôi (F01-F06); sàng lọc 178 ứng viên theo tiêu chí bao gồm/loại trừ.
- **Thực nghiệm thảo luận:** Đối soát số lượng bài báo toàn văn (10 vs 13 vs 16) và trạng thái dừng trích dẫn trên ma trận kiểm chứng.
- **Kết luận xác thực:** Đã sàng lọc 178 ứng viên; 16 bài báo toàn văn chính tắc; điều kiện dừng chưa đạt (`stop_condition_satisfied = false`); ngày cắt tìm kiếm chưa thiết lập.
- **Kết luận suy diễn:** Không tìm thấy bài báo trong tập 178 bài không tương đương với việc bài toán chưa từng được giải trong toàn bộ nền khoa học.
- **Vấn đề chưa giải quyết:** Xung đột giữa việc tuyên bố 'đã xác lập khoảng trống' trong báo cáo và cờ `stop_condition_satisfied = false` trong registry.
- **Diễn giải bị thay thế:** Từng kết luận như thể khoảng trống cơ học đã được xác lập chắc chắn 100%.
- **Diễn giải đã sửa đổi:** Minh bạch hóa rằng khoảng trống chỉ là một giả thuyết còn sống sót tạm thời (PROVISIONALLY SURVIVING HYPOTHESIS).
- **Trạng thái & Độ tin cậy:** `stop_condition_unmet` | `high`
- **Xuất xứ (Provenance):** `W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md#L1-L218`

---
