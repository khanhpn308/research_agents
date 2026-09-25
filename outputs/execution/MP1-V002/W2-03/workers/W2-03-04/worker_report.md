# Worker W2-03-04: Target T3 Reconstruction Report

> **Worker:** W2-03-04  
> **Target:** T3 — Coupled NiTi superelasticity + wire friction/jamming  
> **Trạng thái:** `COMPLETE` | **Phán quyết cuối cùng:** `REFORMULATED_TO_MODEL_DISCRIMINATION`  

## 1. Bản chất và Mục tiêu Khoa học của Target T3
Target T3 là trọng tâm của bước chuyển cơ học MP1: xem xét liệu sự tương tác giữa chuyển pha siêu đàn hồi của NiTi, ma sát trượt giữa các dây và áp suất giam giữ có đòi hỏi một quy luật cấu thành mới hay không.

## 2. Bằng chứng và Phản biện Astra
- **Carboni & Lacarbonara (2016, `40760daa02`):** Chứng minh thực nghiệm rằng sự kết hợp giữa ma sát trượt và chuyển pha NiTi tạo ra hiện tượng trễ thắt (pinched hysteresis) và độ cứng phụ thuộc biên độ dao động.
- **Vahidi et al. (2022, `53200aa0c6`):** Sử dụng mô hình Auricchio hiện hữu kết hợp ma sát Coulomb trong Abaqus tái tạo chính xác đáp ứng vòng trễ của cáp NiTi.
- **Astra Critique (G01, G03) & Remediation:**
  - T3 không thể được dùng để trực tiếp tuyên bố "đã chứng minh tính mới của cơ chế".
  - Việc bác bỏ mô hình dầm đàn hồi đơn giản (H0a) không đồng nghĩa với việc cần một luật ghép cặp mới (H1).
  - T3 được tái cấu trúc thành một bài toán phân biệt mô hình (model discrimination): *Liệu khung lý thuyết cấu thành NiTi hiện hữu kết hợp cơ học tiếp xúc (H0b) có đủ khả năng dự đoán đáp ứng của bó dây dưới áp suất biến thiên hay không?*
