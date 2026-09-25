# Worker W2-08-04: K3 Kill Test Report

> **Worker:** W2-08-04  
> **Test ID:** `K3`  
> **Verdict:** `UNRESOLVED`  
> **Blocking:** `True`  
> **Human Review Required:** `True`  

## 1. Câu hỏi Kiểm toán và Điều kiện Loại bỏ (Kill Condition)
- **Câu hỏi:** Liệu phương án thực nghiệm đề xuất có thể phân biệt độc lập và đơn nhất giữa ma sát trượt, chuyển pha, tái phân bố tiếp xúc, biến dạng nhiệt, biến dạng dư ban đầu, hình học và lịch sử chu kỳ hay không?
- **Điều kiện loại bỏ:** Nhiều cơ chế vật lý khác nhau vẫn đồng dạng quan sát (observationally equivalent) trong phạm vi độ không đảm bảo đo; đường cong mô-men - độ cong vĩ mô M - kappa không thể phân tách cơ chế.

## 2. Kết quả Đánh giá Thực tế
- **Bằng chứng & Phương pháp:** Phân tích khả năng nhận diện thực nghiệm (Identifiability Analysis): Kiểm tra tính duy nhất của việc giải bài toán ngược (inverse problem) từ dữ liệu thực nghiệm để truy nguyên các thông số cấu thành.
- **Kết quả quan sát:** Đo đạc vĩ mô thuần túy (M - kappa hoặc F - delta) bị KILL hoàn toàn vì hiện tượng mềm hóa vĩ mô bị gây ra bởi nhiều cơ chế tích hợp. Khả năng nhận diện chỉ có thể cứu vãn được nếu triển khai thành công hệ thống cảm biến cục bộ đa kênh (DIC + FBG + IR).
- **Điều đã được xác lập:** Xác lập giới hạn toán học: Dữ liệu tích phân vĩ mô không có tính nhận diện đơn nhất; cấm dùng dữ liệu vĩ mô để kết luận cơ chế.
- **Điều chưa được xác lập:** Chưa chế tạo và thử nghiệm thành công đồ gá đo cục bộ tích hợp cảm biến quang FBG trong bó dây bọc kín dưới áp suất.
- **Bất định còn lại:** Thách thức kỹ thuật thực nghiệm cực lớn trong việc đo đạc bên trong vỏ màng kín chứa khí áp suất cao.
- **Trạng thái & Độ tin cậy:** `macroscopic_killed_local_unresolved` | `high`
- **Xuất xứ:** `docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md#G04, outputs/reports/MP1_REMEDIATION_WORKERS_2026-09-25/W08_EXPERIMENTAL_IDENTIFIABILITY.md`
