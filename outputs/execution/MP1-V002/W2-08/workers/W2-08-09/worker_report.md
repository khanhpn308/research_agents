# Worker W2-08-09: K8 Kill Test Report

> **Worker:** W2-08-09  
> **Test ID:** `K8`  
> **Verdict:** `PARTIAL_OVERLAP`  
> **Blocking:** `True`  
> **Human Review Required:** `True`  

## 1. Câu hỏi Kiểm toán và Điều kiện Loại bỏ (Kill Condition)
- **Câu hỏi:** Các tham số của mô hình có được đo lường độc lập và khóa chặt trước khi kiểm chứng hay không, hay mô hình chỉ khớp được số liệu nhờ vào việc thả nổi và bù trừ tham số tự do?
- **Điều kiện loại bỏ:** Ứng viên chỉ vượt trội hơn H0b nhờ vào việc hiệu chỉnh tự do các tham số (over-fitting), bù trừ giữa hệ số ma sát mu và tỷ lệ truyền áp alpha_trans, hoặc rò rỉ dữ liệu kiểm chứng vào quá trình cân chỉnh tham số.

## 2. Kết quả Đánh giá Thực tế
- **Bằng chứng & Phương pháp:** Phân tích bù trừ tham số (Parameter Confounding Analysis): Khảo sát tích số mu * alpha_trans trong phương trình lực cản trượt F_cap = mu * alpha_trans * p; kiểm tra tính duy nhất của nghiệm.
- **Kết quả quan sát:** Stage 3 W09 đã ban hành Quy tắc Khóa tham số tuyệt đối (Locked Calibration Rule): Cấm thả nổi tham số ma sát và truyền áp để ép khớp đường cong uốn; toàn bộ tham số phải đo độc lập ngoài bài toán bó dây. Tuy nhiên, đây mới là quy tắc phương pháp luận trên văn bản, chưa có dữ liệu thực nghiệm thực tế để chứng minh quy tắc này được thực thi thành công.
- **Điều đã được xác lập:** Đã thiết lập khung kiểm soát phương pháp luận nghiêm ngặt ngăn chặn hiện tượng bù trừ tham số và rò rỉ dữ liệu.
- **Điều chưa được xác lập:** Chưa thực hiện chiến dịch đo lường thực nghiệm độc lập các tham số vật liệu và ma sát.
- **Bất định còn lại:** Độ nhạy và lan truyền sai số đo đạc từ các thử nghiệm độc lập vào mô hình uốn tổng thể.
- **Trạng thái & Độ tin cậy:** `locked_calibration_rule_mandated_pending_data` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G08, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W09_MODEL_VALIDATION_CREDIBILITY.md`
