# Worker W2-03-08: Parameter-Substitution and Model-Credibility Report

> **Worker:** W2-03-08  
> **Nhiệm vụ:** Kiểm định thay thế tham số, phân cấp độ tin cậy mô hình 5 tầng, phân tích hiện tượng bù trừ tham số và rà soát Reedlunn 2013 / Fang 2019  
> **Trạng thái:** `COMPLETE`  

## 1. Phân cấp Độ Tin cậy Mô hình 5 Tầng (5-Level Hierarchy)
1. **Tầng 1 (Formulation):** Thiết lập phương trình vi phân và điều kiện biên.
2. **Tầng 2 (Verification):** Kiểm chứng thuật toán số, độ hội tụ và bảo toàn năng lượng.
3. **Tầng 3 (Calibration):** Khớp đường cong thực nghiệm bằng cách tinh chỉnh tham số tự do (nguy cơ bù trừ cao).
4. **Tầng 4 (Validation):** Dự đoán dải tải uốn mới với **bộ tham số bị khóa hoàn toàn** (frozen parameters).
5. **Tầng 5 (Identification):** Đo đạc độc lập biến trạng thái vi mô (phần thể tích pha $\xi$, độ trượt tương đối $\Delta u_t$).

## 2. Rà soát Bảo thủ Reedlunn 2013 và Fang 2019
- **Reedlunn et al. (2013):** Mô hình Costello thất bại ở góc xoắn dốc ($>20^\circ$) do bỏ qua uốn/xoắn cục bộ trong động học cáp; cấu trúc góc xoắn nông rất gần với dây thẳng. Vết lõm SEM là khuyết tật chế tạo, không phải hư hại do vận hành.
- **Fang et al. (2019):** Mô hình OpenSees vĩ mô tương đương (Steel02 + Self-centering) tái tạo hoàn hảo trễ kéo cáp mà không cần giải tiếp xúc vi mô. Fang chỉ thử kéo; mô hình dầm sợi là trụ cầu bê tông 1.4 m. Mối đe dọa thực sự: nếu mô hình vĩ mô dự đoán tốt độ cứng với chi phí rẻ hơn, mô hình tiếp xúc vi mô phức tạp sẽ mất giá trị gia tăng.

## 3. Hiện tượng Bù trừ Tham số (Parameter Confounding)
- Trong dữ liệu uốn vĩ mô $M-\kappa$, thực nghiệm chỉ ràng buộc được tích số $(\mu \cdot \alpha_{\text{trans}} \cdot p)$.
- Nguy cơ tính kép độ mềm (double-counting compliance) xuất hiện khi đo độ mềm bó dây rồi lại đưa vào mô hình phần tử hữu hạn đã mô phỏng chi tiết trượt.
