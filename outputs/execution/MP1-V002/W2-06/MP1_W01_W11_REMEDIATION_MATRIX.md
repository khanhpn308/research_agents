# MP1 Remediation Worker Matrix (Ma trận Khắc phục W01–W11 Stage 3)

> **Commit:** `3a216d6`  
> **Source Directory:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/`  
> **Synthesis Document:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md`  
> **Total Workers:** 11  

## 1. Bảng Tổng hợp 11 Workers Khắc phục Stage 3

| Worker ID | Claims Sửa chữa | Targets Sửa chữa | Phê bình Liên quan | Trạng thái Bằng chứng | Độ tin cậy | Câu hỏi / Nhiệm vụ Chính |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **W01** | C1, C2, C3, C4, C5, C6, C7, C8 | T1, T2, T3 | G10, G11 | `reconciled_at_head` | `high` | Làm thế nào để đồng bộ và đối soát hiện trạng bằng chứng tại commit HEAD so với ... |
| **W02** | C1, C2, C3, C4 | T1, T2 | G01, G02 | `firmly_closed_with_strict_bounds` | `high` | Làm thế nào để xác lập tính vững chắc của các phán quyết đóng đối với C1–C4 và n... |
| **W03** | C5, C6, C7, C8 | T1, T2, T3 | G01, G03, G05 | `boundary_repaired_and_debiased` | `high` | Làm thế nào để sửa chữa ranh giới cơ học C5–C8, loại bỏ các lập luận tạo khoảng ... |
| **W04** | C5, C7 | T1, T3 | G05 | `factual_error_repaired` | `high` | Làm thế nào để tái kiểm chứng Mục tiêu T1 và đính chính triệt để sai sót thực tế... |
| **W05** | C6 | T2 | G02, G09 | `p3_reclassified_as_boundary_condition` | `high` | Làm thế nào để kiểm chứng xem các phương trình vi phân tiếp xúc dầm hiện hữu có ... |
| **W06** | C7 | T3 | G03 | `coexistence_domain_bounded` | `high` | Làm thế nào để phân tích định lượng điều kiện vật lý cần thiết để hiện tượng chu... |
| **W07** | C7 | T3 | G01, G07, G11 | `hypotheses_restructured_and_reconciled` | `high` | Làm thế nào để tái cấu trúc hệ thống giả thuyết H0/H1 thành 3 tầng chặt chẽ và h... |
| **W08** | C6, C7 | T2, T3 | G04, G09, G12 | `identifiability_bounds_formalized` | `high` | Làm thế nào để xác định giới hạn nhận diện thực nghiệm (identifiability limits),... |
| **W09** | C7 | T1, T2, T3 | G06, G08 | `model_credibility_hierarchy_established` | `high` | Làm thế nào để xây dựng thang bậc độ tin cậy mô hình và giải quyết hiện tượng bù... |
| **W10** | C7 | T3 | G07, G08 | `conservative_interpretation_enforced` | `high` | Làm thế nào để diễn giải bảo thủ các kết quả của Reedlunn et al. (2013) và Fang ... |
| **W11** | C1, C2, C3, C4, C5, C6, C7, C8 | T1, T2, T3 | G10, G11 | `stop_condition_transparently_acknowledged` | `high` | Làm thế nào để đánh giá khách quan trạng thái bao phủ trích dẫn, xử lý việc chưa... |

## 2. Chi tiết Từng Worker Khắc phục

### Worker W01
- **Câu hỏi / Mục tiêu:** Làm thế nào để đồng bộ và đối soát hiện trạng bằng chứng tại commit HEAD so với các packet Stage 1, khắc phục độ trễ trạng thái (stale state) và định lượng chính xác tập bài báo kiểm chứng MP1-V002?
- **Tệp nguồn đầu vào:** outputs/verification/MP1-V002/verification_matrix.json (commit 8ccfa3c), outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json (commit 8ccfa3c), outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/00_PACKET_MANIFEST.md (commit af9e7a5)
- **Claims & Targets sửa chữa:** Claims: C1, C2, C3, C4, C5, C6, C7, C8 | Targets: T1, T2, T3 | Hypotheses: H0a, H0b, H1
- **Phê bình liên quan:** G10, G11
- **Bằng chứng tạo ra:** Đối soát thành công 16 bài báo toàn văn chính tắc trên đĩa tại HEAD, lập bảng ánh xạ sự phát triển từ 10 bài ban đầu lên 13 bài và hoàn thiện 16 bài.
- **Kết quả đạt được:** Khắc phục triệt để độ trễ trạng thái; xác lập con số 16 bài báo toàn văn chính tắc là cơ sở đối soát của Stage 3; làm rõ trạng thái dừng trích dẫn chưa đạt.
- **Bất định còn lại:** Nhánh trích dẫn ngược B11 và B12 cần được hoàn tất đầy đủ ở các bước kiểm toán tiếp theo.
- **Diễn giải đã sửa đổi:** Hòa giải rõ ràng sự khác biệt giữa các tài liệu lịch sử; loại bỏ mọi giả định vội vàng về việc đóng tập bằng chứng.
- **Trạng thái & Độ tin cậy:** `reconciled_at_head` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W01_STATE_RECONCILIATION.md#L1-L180`

---
### Worker W02
- **Câu hỏi / Mục tiêu:** Làm thế nào để xác lập tính vững chắc của các phán quyết đóng đối với C1–C4 và ngăn chặn việc diễn giải quá phạm vi (overclaim)?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W01_ORIGINAL_ARCHITECTURE_AND_V001_DECISION.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W02_C1_C2_EVIDENCE.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W03_C3_SMA_JAMMING_LINEAGE.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md
- **Claims & Targets sửa chữa:** Claims: C1, C2, C3, C4 | Targets: T1, T2 | Hypotheses: H0a
- **Phê bình liên quan:** G01, G02
- **Bằng chứng tạo ra:** Bảng tổng hợp đối soát khẳng định tính vững chắc của các phán quyết: C1 (wire jamming) đóng bởi Bai 2022; C2 (áp suất dương) đóng bởi Liu 2021; C3 (SMA jamming) đón đầu bởi Takashima; C4 (nguồn áp suất) đóng bởi Huynh 2022 và Wang 2024.
- **Kết quả đạt được:** Xác nhận 100% phán quyết đóng các khẳng định kiến trúc cấp thiết bị; khóa chặt không cho phép mở lại hay tuyên bố tính mới trên C1–C4.
- **Bất định còn lại:** Không có tính bất định về việc đóng C1–C4; câu hỏi mở duy nhất là hành vi cơ học vi mô của vật liệu trong cơ cấu.
- **Diễn giải đã sửa đổi:** C1–C4 hoàn toàn không có tính mới khoa học; mọi nỗ lực bảo vệ tính mới cấp thiết bị đều bị bác bỏ.
- **Trạng thái & Độ tin cậy:** `firmly_closed_with_strict_bounds` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W02_C1_C4_ROBUST_CLOSURES.md#L1-L150`

---
### Worker W03
- **Câu hỏi / Mục tiêu:** Làm thế nào để sửa chữa ranh giới cơ học C5–C8, loại bỏ các lập luận tạo khoảng trống giả (false gap rhetoric), và phân biệt giữa giới hạn kho dữ liệu và tính mới bản chất?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W05_C5_C6_C7_V001_BOUNDARY.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W04_C4_C8_PRESSURE_SOURCE_EVIDENCE.md, docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
- **Claims & Targets sửa chữa:** Claims: C5, C6, C7, C8 | Targets: T1, T2, T3 | Hypotheses: H0a, H0b, H1
- **Phê bình liên quan:** G01, G03, G05
- **Bằng chứng tạo ra:** Tái định nghĩa ranh giới cơ học: C5 (ma sát trượt NiTi) đã bị đón đầu một phần; C6 (áp suất giam giữ) chuyển thành điều kiện biên; C7 (ghép cặp) chỉ có ý nghĩa nếu chứng minh được vùng cùng tồn tại; C8 loại bỏ hoàn toàn.
- **Kết quả đạt được:** Xóa bỏ thuật ngữ tạo khoảng trống giả; chuyển từ 'đã tìm thấy khoảng trống' sang 'thiết lập giả thuyết kiểm chứng có điều kiện'.
- **Bất định còn lại:** Khả năng tồn tại các công trình tương tự trong cơ học kết cấu hàng hải hoặc địa kỹ thuật chưa được sàng lọc.
- **Diễn giải đã sửa đổi:** Sự vắng mặt trong tập V001 là giới hạn của tập tài liệu ban đầu, không phải bằng chứng về tính mới phổ quát.
- **Trạng thái & Độ tin cậy:** `boundary_repaired_and_debiased` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W03_C5_C8_BOUNDARY_REPAIR.md#L1-L145`

---
### Worker W04
- **Câu hỏi / Mục tiêu:** Làm thế nào để tái kiểm chứng Mục tiêu T1 và đính chính triệt để sai sót thực tế về cấu hình S2a của Carboni et al. (2015) theo phê bình G05?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md, papers/verification/MP1-V002/A1-2015.pdf (Carboni et al. 2015, d9966f2f5e)
- **Claims & Targets sửa chữa:** Claims: C5, C7 | Targets: T1, T3 | Hypotheses: H0b, H1
- **Phê bình liên quan:** G05
- **Bằng chứng tạo ra:** Trích xuất trực tiếp Bảng 4 và các trang 9–10 trong Carboni 2015 PDF: S2a = ST49 (cáp thép 49 sợi, thuần trượt ma sát); S1a = NiTi7 (7 sợi NiTi chịu kéo-uốn kết hợp).
- **Kết quả đạt được:** Sửa chữa 100% sai sót dữ liệu thực tế; xóa bỏ nhận định sai rằng Carboni đã chứng minh chuyển pha dưới uốn thuần; xác định S1a chỉ chứng minh kéo-uốn kết hợp.
- **Bất định còn lại:** Hành vi uốn thuần túy của bó dây NiTi không có lực kéo căng dọc trục vẫn chưa có dữ liệu thực nghiệm trực tiếp trong văn hiến.
- **Diễn giải đã sửa đổi:** S2a là cáp thép; hiện tượng trễ thắt trên S1a gắn liền với lực kéo hình học lớn; không thể suy diễn cho uốn thuần tự do.
- **Trạng thái & Độ tin cậy:** `factual_error_repaired` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W04_T1_REAUDIT_CARBONI_CORRECTION.md#L1-L160`

---
### Worker W05
- **Câu hỏi / Mục tiêu:** Làm thế nào để kiểm chứng xem các phương trình vi phân tiếp xúc dầm hiện hữu có thể tự nhiên tiếp nhận lịch sử áp suất biến thiên p(t) mà không cần phương trình mới hay không?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md, papers/verification/MP1-V002/2017-Submarine Cable Bending Mechanics_ccdc1bb980.pdf (Tjahjanto 2017), papers/verification/MP1-V002/2004-Internal Friction of Cables_aaad9c248c.pdf (Xin Liu 2004)
- **Claims & Targets sửa chữa:** Claims: C6 | Targets: T2 | Hypotheses: H0b, H1
- **Phê bình liên quan:** G02, G09
- **Bằng chứng tạo ra:** Chứng minh toán học rằng phương trình cân bằng tiếp xúc vi phân dq/dx = -mu * fn(p) tiếp nhận p = p(t) một cách tự nhiên trong công thức gia số tải; không xuất hiện số hạng vi phân mới đối với thời gian nếu bỏ qua quán tính chất lưu.
- **Kết quả đạt được:** Hạ cấp dứt điểm P3: P1/P2/P3 là phân loại giao thức điều khiển thực nghiệm (boundary conditions), không phải ba lớp lý thuyết cơ học riêng biệt.
- **Bất định còn lại:** Ảnh hưởng động học trễ của áp suất qua màng nhớt đàn hồi khi tần số biến thiên áp suất cao.
- **Diễn giải đã sửa đổi:** Áp suất chủ động p(t) là một điều kiện biên ngoại vi; không tạo ra một định luật cơ học mới.
- **Trạng thái & Độ tin cậy:** `p3_reclassified_as_boundary_condition` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md#L1-L155`

---
### Worker W06
- **Câu hỏi / Mục tiêu:** Làm thế nào để phân tích định lượng điều kiện vật lý cần thiết để hiện tượng chuyển pha siêu đàn hồi và trượt ma sát giữa các dây cùng kích hoạt trong bó dây NiTi chịu uốn?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W06_T1_NITI_CONTACT_FRICTION.md
- **Claims & Targets sửa chữa:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Phê bình liên quan:** G03
- **Bằng chứng tạo ra:** Phân tích cơ học dầm nhiều sợi: Ngưỡng trượt ma sát kappa_slip = 2 mu p / (E A h); ngưỡng bắt đầu chuyển pha kappa_tr = 2 sigma_tr / (E_A D_bundle). Tính toán cho thấy ở biến dạng nhỏ epsilon < 0.75%, NiTi thuần đàn hồi Austenite và chỉ có trượt ma sát thông thường.
- **Kết quả đạt được:** Thiết lập điều kiện cần cho Miền Cùng Tồn Tại (Coexistence Domain): Chỉ khi dầm bị uốn cong sâu vượt quá kappa_tr hoặc có kéo căng dọc trục thì chuyển pha và trượt mới tương tác; ở biến dạng nhỏ bài toán thoái hóa về dầm đàn hồi thông thường.
- **Bất định còn lại:** Sự phân bố ứng suất tiếp xúc không đều giữa các sợi bên trong và bên ngoài làm chuyển pha xảy ra cục bộ từng sợi.
- **Diễn giải đã sửa đổi:** Cơ chế ghép cặp không tồn tại phổ quát mà phụ thuộc chặt chẽ vào biên độ tải trọng uốn.
- **Trạng thái & Độ tin cậy:** `coexistence_domain_bounded` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W06_T3_TRANSFORMATION_SLIP_COEXISTENCE.md#L1-L170`

---
### Worker W07
- **Câu hỏi / Mục tiêu:** Làm thế nào để tái cấu trúc hệ thống giả thuyết H0/H1 thành 3 tầng chặt chẽ và hòa giải xung đột trạng thái giữa Audit JSON và báo cáo tổng hợp?
- **Tệp nguồn đầu vào:** outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json (commit 8ccfa3c), outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md, docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
- **Claims & Targets sửa chữa:** Claims: C7 | Targets: T3 | Hypotheses: H0a, H0b, H1
- **Phê bình liên quan:** G01, G07, G11
- **Bằng chứng tạo ra:** Tách H0 thành: H0a (thay thế mô-đun đàn hồi hằng số), H0b (khung lý thuyết NiTi cấu thành phi tuyến + tiếp xúc Coulomb hiện hữu), và H1 (lý thuyết ghép cặp vi mô mới). Phân tích nguồn gốc nhãn 'established' trong JSON.
- **Kết quả đạt được:** Hòa giải thành công: Bác bỏ H0a là 'established'; nhưng H0b chưa bị bác bỏ ('not falsified') và H1 là 'insufficient'. Loại bỏ hoàn toàn sự mâu thuẫn giữa JSON và narrative.
- **Bất định còn lại:** Cần thiết kế thí nghiệm đối chứng có khả năng phân biệt dứt điểm giữa dự đoán của H0b và H1.
- **Diễn giải đã sửa đổi:** Bác bỏ mô hình đàn hồi sơ đẳng H0a không phải là bằng chứng ủng hộ H1.
- **Trạng thái & Độ tin cậy:** `hypotheses_restructured_and_reconciled` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W07_PARAMETER_SUBSTITUTION_H0_H1.md#L1-L175`

---
### Worker W08
- **Câu hỏi / Mục tiêu:** Làm thế nào để xác định giới hạn nhận diện thực nghiệm (identifiability limits), phân tách cơ chế bị chồng lấn trong dữ liệu uốn vĩ mô, và chuẩn hóa định nghĩa độ cứng uốn?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md, docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
- **Claims & Targets sửa chữa:** Claims: C6, C7 | Targets: T2, T3 | Hypotheses: H1
- **Phê bình liên quan:** G04, G09, G12
- **Bằng chứng tạo ra:** Phân tích chuỗi nhận diện thực nghiệm: (1) Đường cong M-kappa vĩ mô không có tính nhận diện đơn nhất; (2) Chuỗi truyền áp suất p -> f_n chịu hiệu ứng vòm (arching); (3) Chuẩn hóa 3 công thức toán học cho D_tan, D_sec, D_dyn.
- **Kết quả đạt được:** Thiết lập yêu cầu bắt buộc: Phải dùng cảm biến cục bộ (DIC, FBG, ảnh nhiệt) để đo trực tiếp trượt và biến dạng sợi; cấm dùng dữ liệu uốn vĩ mô để tuyên bố cơ chế mới.
- **Bất định còn lại:** Khó khăn trong việc tích hợp cảm biến đo quang FBG vào bên trong bó dây bọc kín dưới áp suất cao.
- **Diễn giải đã sửa đổi:** Hiện tượng mềm hóa uốn vĩ mô có thể do nhiều nguyên nhân cơ học gây ra; không thể gán đơn nhất cho cơ chế NiTi.
- **Trạng thái & Độ tin cậy:** `identifiability_bounds_formalized` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md#L1-L165`

---
### Worker W09
- **Câu hỏi / Mục tiêu:** Làm thế nào để xây dựng thang bậc độ tin cậy mô hình và giải quyết hiện tượng bù trừ tham số (parameter confounding) trong bài toán khớp uốn?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md, docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
- **Claims & Targets sửa chữa:** Claims: C7 | Targets: T1, T2, T3 | Hypotheses: H0b, H1
- **Phê bình liên quan:** G06, G08
- **Bằng chứng tạo ra:** Xây dựng Thang bậc 5 tầng: T1 (Formulation) -> T2 (Verification số) -> T3 (Calibration khớp đường cong) -> T4 (Validation với tham số bị khóa) -> T5 (Nhận diện nhân quả). Phân tích tích số mu * alpha_trans.
- **Kết quả đạt được:** Ban hành Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Cấm thả nổi tham số ma sát và truyền lực để ép khớp đường cong uốn; yêu cầu kiểm tra tính duy nhất của nghiệm.
- **Bất định còn lại:** Mức độ nhạy của mô hình đối với sai số đo đạc thực nghiệm các tham số vật liệu độc lập.
- **Diễn giải đã sửa đổi:** Khớp đường cong thực nghiệm chỉ đạt Tầng 3; một mô hình chỉ có giá trị khoa học kiểm chứng khi đạt Tầng 4 và Tầng 5.
- **Trạng thái & Độ tin cậy:** `model_credibility_hierarchy_established` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W09_MODEL_VALIDATION_CREDIBILITY.md#L1-L185`

---
### Worker W10
- **Câu hỏi / Mục tiêu:** Làm thế nào để diễn giải bảo thủ các kết quả của Reedlunn et al. (2013) và Fang et al. (2019), ngăn chặn việc suy diễn sai lệch phạm vi cơ học?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md, outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md, docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
- **Claims & Targets sửa chữa:** Claims: C7 | Targets: T3 | Hypotheses: H0b, H1
- **Phê bình liên quan:** G07, G08
- **Bằng chứng tạo ra:** Phân tích giới hạn động học trong Reedlunn: Thất bại của mô hình Costello xuất phát từ góc xoắn dốc ở lớp ngoài cáp 1x27 bỏ qua uốn/xoắn cục bộ. Phân tích mô hình sợi Fang: OpenSees bỏ qua ma sát tiếp xúc vi mô cục bộ.
- **Kết quả đạt được:** Khắc phục triệt để các suy diễn quá đà: Không dùng lỗi động học của cáp xoắn để biện hộ cho nhu cầu lý thuyết bó dây thẳng; thừa nhận khả năng mô phỏng vĩ mô tốt của mô hình sợi OpenSees.
- **Bất định còn lại:** Khả năng mở rộng mô hình sợi OpenSees sang bài toán có áp suất pháp tuyến biến thiên lớn.
- **Diễn giải đã sửa đổi:** Cả hai công trình đều có phạm vi hiệu lực riêng biệt; không được bóp méo kết quả của tác giả tiền nhiệm để tạo khoảng trống nghiên cứu giả.
- **Trạng thái & Độ tin cậy:** `conservative_interpretation_enforced` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W10_REEDLUNN_FANG_CONSERVATIVE_REMEDIATION.md#L1-L150`

---
### Worker W11
- **Câu hỏi / Mục tiêu:** Làm thế nào để đánh giá khách quan trạng thái bao phủ trích dẫn, xử lý việc chưa đạt điều kiện dừng tìm kiếm, và bảo toàn tính toàn vẹn dữ liệu nguồn?
- **Tệp nguồn đầu vào:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md, outputs/verification/MP1-V002/citation_coverage.json (commit 8ccfa3c), docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md
- **Claims & Targets sửa chữa:** Claims: C1, C2, C3, C4, C5, C6, C7, C8 | Targets: T1, T2, T3 | Hypotheses: H0a, H0b, H1
- **Phê bình liên quan:** G10, G11
- **Bằng chứng tạo ra:** Đối soát 15 hướng trích dẫn bắt buộc; xác nhận điều kiện dừng chưa thỏa mãn (stop_condition_satisfied = false); thiết lập cơ chế ghi nhận tính mới thận trọng.
- **Kết quả đạt được:** Chuyển toàn bộ các phát biểu về 'khoảng trống nghiên cứu' thành 'giả thuyết còn sống sót tạm thời' (PROVISIONALLY SURVIVING HYPOTHESIS); nghiêm cấm kết luận tính mới tuyệt đối.
- **Bất định còn lại:** Các nhánh trích dẫn sâu hơn có thể tiếp tục thu hẹp hoặc bác bỏ giả thuyết còn lại.
- **Diễn giải đã sửa đổi:** Tính mới chỉ có giá trị tương đối trong phạm vi tập bằng chứng đã khảo sát; quy trình kiểm chứng phải mở và sẵn sàng bị phản biện.
- **Trạng thái & Độ tin cậy:** `stop_condition_transparently_acknowledged` | `high`
- **Xuất xứ:** `outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W11_CITATION_COVERAGE_QA.md#L1-L140`

---
