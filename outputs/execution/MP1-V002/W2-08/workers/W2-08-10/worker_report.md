# Worker W2-08-10: K9 Kill Test Report

> **Worker:** W2-08-10  
> **Test ID:** `K9`  
> **Verdict:** `UNRESOLVED`  
> **Blocking:** `True`  
> **Human Review Required:** `True`  

## 1. Câu hỏi Kiểm toán và Điều kiện Loại bỏ (Kill Condition)
- **Câu hỏi:** Liệu sự thay đổi độ cứng và trễ năng lượng có thể được quy kết một cách đơn nhất cho cơ chế đề xuất hay bị gây nhiễu bởi các hiệu ứng phụ (nhiệt độ, ma sát thuần, hình học, lịch sử tải)?
- **Điều kiện loại bỏ:** Cơ chế ghép cặp đề xuất không thể phân biệt được với trễ ma sát thông thường, trễ nhiệt độ do nhiệt tiềm ẩn chuyển pha, hoặc biến dạng hình học trong phạm vi độ không đảm bảo đo.

## 2. Kết quả Đánh giá Thực tế
- **Bằng chứng & Phương pháp:** Phân tích trễ cơ-nhiệt (Thermomechanical Hysteresis Analysis): So sánh công tiêu tán do ma sát Coulomb W_fric với năng lượng tiêu tán do trễ chuyển pha W_phase và trao đổi nhiệt môi trường.
- **Kết quả quan sát:** Đã chuẩn hóa 3 định nghĩa toán học riêng biệt cho độ cứng uốn để tránh mơ hồ. Tuy nhiên, việc phân tách trễ chuyển pha siêu đàn hồi khỏi trễ ma sát Coulomb trong chu kỳ uốn là rất khó khăn nếu không kiểm soát chặt chẽ nhiệt độ và tốc độ gia tải (phải tải chậm quasi-static < 0.05 Hz hoặc dùng ảnh nhiệt hồng ngoại đồng bộ).
- **Điều đã được xác lập:** Đã chuẩn hóa các đại lượng đo độ cứng uốn và xác định các nguồn gây nhiễu năng lượng trễ.
- **Điều chưa được xác lập:** Chưa có thiết kế thí nghiệm kiểm soát nhiệt độ đồng bộ trong quá trình đo trễ uốn.
- **Bất định còn lại:** Hiệu ứng tự gia nhiệt làm biến đổi cơ tính trong quá trình robot uốn lặp lại ở tần số cao.
- **Trạng thái & Độ tin cậy:** `hysteresis_definitions_formalized_observability_unresolved` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G12, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`
