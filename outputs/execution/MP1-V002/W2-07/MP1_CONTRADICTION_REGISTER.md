# Sổ bộ Mâu thuẫn và Điểm Bất đồng (MP1 Contradiction Register)

> **Tệp chính tắc:** `MP1_CONTRADICTION_REGISTER.json`  
> **Tổng số mâu thuẫn:** 8 contradictions (4 workflow, 4 evidence)  
> **Nguyên tắc:** Bảo toàn tuyệt đối mọi điểm mâu thuẫn lịch sử và thực nghiệm; nghiêm cấm hòa giải ngầm.

## 1. Bảng Tổng hợp Mâu thuẫn

| Mã Mâu thuẫn (ID) | Phân loại | Mức độ | Trạng thái Xử lý | Tóm tắt Bất đồng |
|:---:|---|:---:|:---:|---|
| **CONTRA-WF-01** | `WORKFLOW_INVENTORY_DISCREPANCY` | `HIGH` | `CURRENT_RESOLVED` | 10 bài báo toàn văn (Stage 1) vs 13 bài báo vs 16 bài báo toàn văn chính tắ... |
| **CONTRA-WF-02** | `WORKFLOW_SEMANTIC_CONFLICT` | `CRITICAL` | `CURRENT_RESOLVED` | Xung đột ngữ nghĩa giữa 'established' (đã xác lập) và 'insufficient' (chưa ... |
| **CONTRA-WF-03** | `WORKFLOW_STOP_CONDITION_CONFLICT` | `HIGH` | `CURRENT_RESOLVED` | Khẳng định khoảng trống chắc chắn vs thừa nhận điều kiện dừng chưa đạt.... |
| **CONTRA-WF-04** | `GOVERNANCE_TOPIC_STATUS_AMBIGUITY` | `MEDIUM` | `CURRENT_RESOLVED` | Ứng viên dự phòng đang kiểm chứng đe dọa vs đề tài luận văn chính thức đã p... |
| **CONTRA-EV-01** | `EVIDENCE_DATA_FACTUAL_ERROR` | `CRITICAL` | `CURRENT_RESOLVED` | S2a thực chất là cáp thép ST49 thuần trượt ma sát; S1a mới là cáp NiTi7 như... |
| **CONTRA-EV-02** | `EVIDENCE_MECHANICS_CONCEPT_OVERCLAIM` | `CRITICAL` | `CURRENT_RESOLVED` | Áp suất chủ động là nguyên lý cơ học mới vs áp suất chủ động là điều kiện b... |
| **CONTRA-EV-03** | `EVIDENCE_KINEMATIC_THEORY_OVEREXTENSION` | `HIGH` | `CURRENT_RESOLVED` | Sai số do giả thiết động học thanh xoắn Costello bỏ qua uốn/xoắn cục bộ vs ... |
| **CONTRA-EV-04** | `EVIDENCE_PARAMETER_CONFOUNDING_IN_MODEL_FIT` | `HIGH` | `PARTIALLY_RESOLVED` | Khớp số liệu tự do bằng bù trừ tham số vs nhận diện nhân quả đơn nhất của m... |

## 2. Chi tiết Từng Mâu thuẫn

### Mâu thuẫn CONTRA-WF-01: WORKFLOW_INVENTORY_DISCREPANCY (HIGH)
- **Nguồn A:** docs/project/MP1-V002_CURRENT_HANDOFF.md (commit bf0b79a) và W01-W11 packets (commit af9e7a5)
- **Nguồn B:** outputs/verification/MP1-V002/verification_matrix.json (commit 8ccfa3c) và W01 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Báo cáo giai đoạn đầu Stage 1 ghi nhận 10 bài báo toàn văn, trong khi ma trận trên đĩa có 13 bài và ma trận canonical tại HEAD có đúng 16 bài báo.
- **Điểm khác biệt:** 10 bài báo toàn văn (Stage 1) vs 13 bài báo vs 16 bài báo toàn văn chính tắc.
- **Diễn giải hiện tại:** Số lượng bài báo phát triển tự nhiên qua các giai đoạn: Stage 1 khởi đầu với 10 bài, mở rộng lên 13 bài trên đĩa, và tại HEAD Stage 3 có đúng 16 bài báo toàn văn chính tắc.
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `False`
- **Bất định còn lại:** Không còn bất định; 16 bài báo toàn văn là cơ sở pháp lý duy nhất.
- **Xuất xứ:** `outputs/execution/MP1-V002/W2-06/W2_06_CONTRADICTION_CANDIDATES.json#CONTRA-01`

---
### Mâu thuẫn CONTRA-WF-02: WORKFLOW_SEMANTIC_CONFLICT (CRITICAL)
- **Nguồn A:** outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json dòng 237-241 (commit 8ccfa3c)
- **Nguồn B:** docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md (commit 8ccfa3c) và W07 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Tệp Audit JSON ghi nhận 'niti_requires_distinct_constitutive_contact_coupling = true' với evidence_status = 'established', trong khi Astra và W10 kết luận bằng chứng là 'insufficient'.
- **Điểm khác biệt:** Xung đột ngữ nghĩa giữa 'established' (đã xác lập) và 'insufficient' (chưa đủ bằng chứng).
- **Diễn giải hiện tại:** Nhãn 'established' trong JSON bắt nguồn từ việc bác bỏ mô-đun đàn hồi hằng số H0a; đối với H1 thì bằng chứng hoàn toàn chưa đủ ('insufficient') và H0b chưa bị bác bỏ.
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `True`
- **Bất định còn lại:** Cần kiểm tra đối chứng thực nghiệm giữa H0b và H1.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G01,G11`

---
### Mâu thuẫn CONTRA-WF-03: WORKFLOW_STOP_CONDITION_CONFLICT (HIGH)
- **Nguồn A:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W11_CITATION_COVERAGE_AND_SOURCE_INTEGRITY.md (commit af9e7a5)
- **Nguồn B:** outputs/verification/MP1-V002/citation_coverage.json (commit 8ccfa3c) và W11 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Lời văn tổng hợp ban đầu tuyên bố khoảng trống đã được chứng minh vì không tìm thấy bài báo nào trong tập rà soát, trong khi registry ghi stop_condition_satisfied = false.
- **Điểm khác biệt:** Khẳng định khoảng trống chắc chắn vs thừa nhận điều kiện dừng chưa đạt.
- **Diễn giải hiện tại:** Thừa nhận minh bạch điều kiện dừng chưa đạt; khoảng trống đề xuất chỉ là một giả thuyết còn sống sót tạm thời (PROVISIONALLY SURVIVING HYPOTHESIS).
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `False`
- **Bất định còn lại:** Các nhánh trích dẫn sâu hơn có thể tiếp tục thu hẹp giả thuyết.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G10`

---
### Mâu thuẫn CONTRA-WF-04: GOVERNANCE_TOPIC_STATUS_AMBIGUITY (MEDIUM)
- **Nguồn A:** docs/project/MP1-V002_CURRENT_HANDOFF.md (commit bf0b79a)
- **Nguồn B:** outputs/verification/D1-V001/direction_verification.json và AGENTS.md
- **Bối cảnh lịch sử:** Một số văn bản diễn đạt như thể MP1 đã được chính thức phê duyệt làm đề tài luận văn thay thế D1, trong khi theo quy chế nó mới chỉ là một ứng viên dự phòng đang được thẩm tra đe dọa.
- **Điểm khác biệt:** Ứng viên dự phòng đang kiểm chứng đe dọa vs đề tài luận văn chính thức đã phê duyệt.
- **Diễn giải hiện tại:** MP1 chỉ là ứng viên dự phòng (provisional pivot candidate); quyền quyết định chọn làm đề tài chính thức thuộc về supervisor sau khi hoàn tất toàn bộ quy trình kiểm toán đe dọa.
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `True`
- **Bất định còn lại:** Phụ thuộc vào quyết định của supervisor tại mốc human sign-off.
- **Xuất xứ:** `outputs/execution/MP1-V002/W2-01/W2_01_CONTRADICTION_CANDIDATES.json#CONTRA-06`

---
### Mâu thuẫn CONTRA-EV-01: EVIDENCE_DATA_FACTUAL_ERROR (CRITICAL)
- **Nguồn A:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W08_T3_TRANSFORMATION_CONTACT_COUPLING.md (commit af9e7a5)
- **Nguồn B:** papers/verification/MP1-V002/A1-2015.pdf Table 4 (Carboni 2015) và W04 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Packet W08 khẳng định cấu hình S2a trong bài báo của Carboni 2015 là bằng chứng thực nghiệm về chuyển pha siêu đàn hồi NiTi dưới uốn thuần.
- **Điểm khác biệt:** S2a thực chất là cáp thép ST49 thuần trượt ma sát; S1a mới là cáp NiTi7 nhưng chịu tải kéo-uốn kết hợp.
- **Diễn giải hiện tại:** Đính chính 100% dữ liệu thực tế: S2a là cáp thép ST49; hiện tượng trễ thắt trên S1a gắn liền với lực kéo hình học lớn; văn hiến vẫn thiếu dữ liệu thực nghiệm về uốn thuần NiTi.
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `True`
- **Bất định còn lại:** Thiếu dữ liệu thực nghiệm về uốn thuần bó dây NiTi không có lực kéo.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G05, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W04_T1_REAUDIT_CARBONI_CORRECTION.md`

---
### Mâu thuẫn CONTRA-EV-02: EVIDENCE_MECHANICS_CONCEPT_OVERCLAIM (CRITICAL)
- **Nguồn A:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W07_T2_ACTIVE_CONFINEMENT_PRESSURE.md (commit af9e7a5)
- **Nguồn B:** docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md (commit 8ccfa3c) và W05 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Packet W07 phân loại áp suất P3 là một nhánh cơ học mới có khả năng tạo ra tính mới khoa học độc lập.
- **Điểm khác biệt:** Áp suất chủ động là nguyên lý cơ học mới vs áp suất chủ động là điều kiện biên biến thiên theo thời gian.
- **Diễn giải hiện tại:** Hạ cấp P3: Phương trình vi phân tiếp xúc hiện hữu tự nhiên tiếp nhận p(t); P3 là giao thức điều khiển thực nghiệm (boundary condition).
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `False`
- **Bất định còn lại:** Trễ truyền áp động học chất lưu qua màng đàn hồi khi tần số cao.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G02, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W05_T2_MECHANICS_P1_P2_P3_TEST.md`

---
### Mâu thuẫn CONTRA-EV-03: EVIDENCE_KINEMATIC_THEORY_OVEREXTENSION (HIGH)
- **Nguồn A:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W09_REEDLUNN_2013_DEEP_AUDIT.md (commit af9e7a5)
- **Nguồn B:** docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md (commit 8ccfa3c) và W10 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Packet W09 dùng sự sai lệch của mô hình Costello ở lớp ngoài cáp 1x27 trong Reedlunn 2013 để lập luận rằng lý thuyết tiếp xúc-chuyển pha hiện hữu đã sụp đổ.
- **Điểm khác biệt:** Sai số do giả thiết động học thanh xoắn Costello bỏ qua uốn/xoắn cục bộ vs thiếu hụt luật cơ học cấu thành tiếp xúc.
- **Diễn giải hiện tại:** Áp dụng nguyên tắc trích dẫn bảo thủ: Sai số trong Reedlunn thuần túy là giới hạn động học của cáp xoắn góc dốc; không liên quan đến bó dây song song thẳng.
- **Trạng thái xử lý:** `CURRENT_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `False`
- **Bất định còn lại:** Không còn rủi ro suy diễn sai lệch.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G07, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W10_REEDLUNN_FANG_CONSERVATIVE_REMEDIATION.md`

---
### Mâu thuẫn CONTRA-EV-04: EVIDENCE_PARAMETER_CONFOUNDING_IN_MODEL_FIT (HIGH)
- **Nguồn A:** outputs/reports/MP1_MECHANICS_TRACE_PACKETS_2026-09-25/W10_FANG_2019_PARAMETER_SUBSTITUTION.md (commit af9e7a5)
- **Nguồn B:** docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md (commit 8ccfa3c) và W09 Remediation (commit 3a216d6)
- **Bối cảnh lịch sử:** Mô hình uốn bó dây có nguy cơ thả nổi đồng thời hệ số ma sát mu và tỷ lệ truyền áp alpha_trans, dẫn đến việc nhiều bộ tham số khác nhau cùng cho ra một đường cong uốn giống hệt nhau.
- **Điểm khác biệt:** Khớp số liệu tự do bằng bù trừ tham số vs nhận diện nhân quả đơn nhất của mô hình vật lý.
- **Diễn giải hiện tại:** Ban hành Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Bắt buộc đo độc lập mu và tỷ lệ truyền áp trước khi mô phỏng uốn; cấm thả nổi tham số để ép khớp.
- **Trạng thái xử lý:** `PARTIALLY_RESOLVED`
- **Đơn vị chịu trách nhiệm:** `W2-07-12 / final synthesis auditor`
- **Khóa phán quyết:** `False` | **Cần người duyệt:** `True`
- **Bất định còn lại:** Cần kiểm chứng bằng thực nghiệm đo đạc độc lập để khẳng định tính khả thi của Locked Calibration.
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G08, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W09_MODEL_VALIDATION_CREDIBILITY.md`

---
