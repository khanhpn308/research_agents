# Worker W2-03-03: Target T2 Reconstruction Report

> **Worker:** W2-03-03  
> **Target:** T2 — Positive-pressure confinement of metallic/NiTi wire bundle  
> **Trạng thái:** `COMPLETE` | **Phán quyết cuối cùng:** `NARROWED_TO_EXPERIMENTAL_BC`  

## 1. Bản chất và Mục tiêu Khoa học của Target T2
Target T2 kiểm tra xem việc sử dụng áp suất dương giam giữ $p$ tác động lên bó dây kim loại để tăng lực pháp tuyến tiếp xúc và biến đổi độ cứng uốn có phải là một nguyên lý cơ học mới hay không.

## 2. Bằng chứng và Quá trình Tái cấu trúc (Remediation)
- **Tjahjanto et al. (2017, `ccdc1bb980`):** Áp dụng áp suất tiếp xúc hướng kính 0.2 MPa lên cáp động ngầm dưới biển, chứng minh lực nén hướng kính làm tăng giới hạn ma sát trượt và thay đổi độ cứng uốn.
- **Phê bình của Astra (G02) và Đính chính W05 (CONTRA-05):**
  - Trong phương trình vi phân cân bằng của dầm và cơ học tiếp xúc Coulomb, áp suất giam giữ $p(t)$ xuất hiện thuần túy như một **điều kiện biên về ứng suất bề mặt (traction boundary condition)**: $\mathbf{\sigma} \cdot \mathbf{n} = -p(t) \mathbf{n}$.
  - Các công thức vi phân tiếp xúc hiện hữu hoàn toàn chấp nhận $p(t)$ là hàm biến thiên theo thời gian mà không cần thay đổi bất kỳ phương trình cơ bản nào.
  - Việc điều khiển áp suất động học trong thí nghiệm là một **giao thức điều khiển thực nghiệm (experimental protocol / boundary condition)**, không thể được coi là một "nguyên lý cơ học cấu thành mới".

## 3. Trạng thái Hiện tại
Target T2 bị đóng ở tư cách là một tuyên bố tính mới về cơ học (`CLOSED_AS_MECHANICS_NOVELTY`), chỉ còn tồn tại dưới dạng một điều kiện biên thực nghiệm cho bài toán uốn dầm.
