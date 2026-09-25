# Worker W2-03-09: Transformation / Slip Coexistence Report

> **Worker:** W2-03-09  
> **Nhiệm vụ:** Tái hiện điều kiện vật lý và miền cùng tồn tại (Coexistence Domain) giữa trượt ma sát và chuyển pha siêu đàn hồi NiTi  
> **Trạng thái:** `COMPLETE`  

## 1. Ba Miền Cơ học Riêng biệt
1. **Miền I (Full Stick — `NEITHER`):** $\kappa < \kappa_{\text{slip}}(p)$ và $\varepsilon < \varepsilon_{\text{Ms}}$. Bó dây dính hoàn toàn, ứng xử như dầm đàn hồi đặc.
2. **Miền II (Trượt thuần túy — `SLIP_ONLY`):** $\kappa_{\text{slip}}(p) \le \kappa < \kappa_{\text{tr}}$.
   - Các dây trượt qua nhau làm thay đổi độ cứng uốn.
   - Tuy nhiên, biến dạng cực đại $\varepsilon < \varepsilon_{\text{Ms}} \approx 0.75\%$.
   - NiTi **hoàn toàn ở pha Austenite đàn hồi tuyến tính**, không có chuyển pha Martensite!
   - **Mô hình đàn hồi sơ đẳng H0a hoàn toàn dự đoán được miền này.** Tính mới cơ học bị triệt tiêu hoàn toàn nếu thiết bị chỉ hoạt động ở miền này.
3. **Miền III (Cùng tồn tại — `COEXISTENCE`):** $\kappa \ge \kappa_{\text{tr}}$.
   - Trượt ma sát và chuyển pha Martensite cùng đồng thời diễn ra.
   - Đòi hỏi độ cong uốn cực lớn (uốn góc gập sâu với bán kính uốn nhỏ) hoặc phải có lực kéo dọc trục đáng kể.

## 2. Nguy cơ Sụp đổ Thiết kế của MP1
Trong các ứng dụng robot mềm thông thường (uốn cong mềm dẻo với góc uốn vừa phải, biến dạng dưới 0.75%), toàn bộ hoạt động chỉ diễn ra trong Miền II (`SLIP_ONLY`), biến đề tài thành bài toán kẹt dây đàn hồi cổ điển.
