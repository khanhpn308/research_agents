# W02: Đánh giá Vững chắc và Giới hạn Hiệu lực của C1–C4 (C1–C4 Robust Closures vs Overclaim)

**Worker ID:** W02  
**Mục tiêu:** Rà soát, xác thực tính vững chắc của các phán quyết đóng (closures) đối với các khẳng định kiến trúc cấp thiết bị C1–C4, đồng thời thiết lập các giới hạn hiệu lực (residual caveats) nghiêm ngặt để tránh việc diễn giải quá phạm vi (overclaim).  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Tổng quan Đánh giá C1–C4

Trong giai đoạn phân rã kiến trúc ban đầu từ đề xuất của Mentor (thiết bị biến đổi độ cứng tích hợp piston/áp suất dương và bó dây NiTi), bốn khẳng định cấp hệ thống C1–C4 đã bị tiền nhiệm đóng hoàn toàn ở mức nguyên lý hoạt động. Đánh giá của Astra (mục 3) xác nhận việc đóng C1–C4 là hoàn toàn chính xác và có cơ sở vững chắc từ bằng chứng thực nghiệm. Tuy nhiên, việc đóng này cần phải đi kèm các giới hạn hiệu lực cụ thể để không tạo ra kết luận bao biện hoặc khái quát hóa quá mức.

---

## 2. Chi tiết Đánh giá từng Khẳng định và Giới hạn Hiệu lực

### 2.1. C1: Khẳng định tính mới về Kẹt bó dây/sợi (Wire/Fiber Jamming)
- **Tuyên bố gốc:** Khẳng định việc sử dụng hiện tượng kẹt giữa các sợi hoặc dây kim loại song song/bện để thay đổi độ cứng uốn là một cơ chế mới chưa từng có.
- **Phán quyết:** `CLOSED` / `PREEMPTED`.
- **Bằng chứng tiền nhiệm then chốt:**
  - Bai et al. (2022, DOI: 10.3390/app12073582): Thiết bị truyền động mềm có thể tháo rời với khả năng điều chỉnh độ cứng dựa trên kẹt dây kim loại (wire jamming).
  - Liu et al. (2021, DOI: 10.1109/LRA.2021.3097255): Cơ cấu kẹt dây cho ngón tay robot mềm.
  - Zhang & Yao et al. (2026, DOI: 10.5194/ms-17-481-2026): Chuỗi đa hướng biến đổi độ cứng dựa trên kẹt sợi áp suất dương (positive-pressure fiber jamming).
- **Lý do đóng:** Nguyên lý tăng độ cứng uốn thông qua việc tăng lực ma sát pháp tuyến giữa các sợi/dây khi bị bao bọc và chịu tải giam giữ đã được thiết lập thực nghiệm và giải tích tường minh.
- **Giới hạn hiệu lực (Residual Caveat):** Việc đóng C1 không đồng nghĩa với việc mọi tổ hợp hình học bó dây, đường kính, bước xoắn hay vật liệu đều đã được thử nghiệm toàn diện. Tuy nhiên, theo nguyên tắc cốt lõi của đề tài, việc chỉ thay đổi vật liệu từ thép/nylon sang NiTi hay đổi tiết diện mà không làm phát sinh câu hỏi cơ học mới thì **không cấu thành tính mới khoa học (scientific novelty)**.

---

### 2.2. C2: Khẳng định tính mới về Cơ cấu Kẹt Áp suất Dương (Positive-Pressure Jamming)
- **Tuyên bố gốc:** Cơ chế tăng độ cứng bằng cách cấp áp suất dương vào màng bao bên ngoài (positive confinement pressure) để ép các phần tử kẹt là nguyên lý hoàn toàn mới so với kẹt chân không truyền thống (vacuum jamming).
- **Phán quyết:** `CLOSED` / `PREEMPTED`.
- **Bằng chứng tiền nhiệm then chốt:**
  - Zhang & Yao et al. (2026, DOI: 10.5194/ms-17-481-2026): Cung cấp mô hình giải tích và thực nghiệm toàn diện về kẹt sợi dưới áp suất dương bên trong ống đàn hồi.
  - Huynh et al. (2022, DOI: 10.20965/jrm.2022.p0466): Cấu trúc biến đổi độ cứng dựa trên áp suất dương ứng dụng cho robot mặc đeo (wearable robots).
- **Lý do đóng:** Áp suất dương như một phương tiện tạo áp lực giam giữ hướng kính lên các phần tử ma sát đã được tiền nhiệm phân tích chi tiết cả về mặt phân bố áp suất lẫn khả năng chịu mô-men uốn.
- **Giới hạn hiệu lực (Residual Caveat):** Sự khác biệt giữa áp suất dương màng và áp suất thủy tĩnh hay áp suất do piston cơ học tác động lên đầu bó dây chỉ là sự thay đổi về phương thức cấp tải biên, không làm thay đổi định luật ma sát Coulomb tiếp xúc cơ bản ($F_{\text{fric}} \le \mu N$).

---

### 2.3. C3: Khẳng định tính mới về Sự kết hợp giữa Hợp kim nhớ hình (SMA) và Hiện tượng Kẹt (Jamming)
- **Tuyên bố gốc:** Việc tích hợp đồng thời vật liệu SMA và cơ chế jamming trong cùng một kết cấu biến đổi độ cứng là một ý tưởng chưa từng xuất hiện.
- **Phán quyết:** `CLOSED` / `PREEMPTED`.
- **Bằng chứng tiền nhiệm then chốt:**
  - Takashima et al. (2021, DOI: 10.1299/mej.24-00130): Khâu biến đổi độ cứng và biến dạng sử dụng vật liệu nhớ hình và hiện tượng chuyển tiếp kẹt (Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon).
  - Takashima et al. (2022, DOI: 10.1108/IR-11-2023-0305): Ảnh hưởng của pha R lên tốc độ phục hồi hình dạng của dây Ti-Ni cho cơ cấu biến đổi độ cứng dùng jamming.
- **Lý do đóng:** Khái niệm kết hợp chức năng (co-existence) của dây SMA và môi trường kẹt trong cùng một thiết bị chấp hành mềm đã được dòng nghiên cứu của Takashima hiện thực hóa.
- **Giới hạn hiệu lực (Residual Caveat):** Trong các nghiên cứu của Takashima, dây SMA đóng vai trò là lõi dẫn động/phục hồi hình dạng (actuator backbone) được nhúng bên trong môi trường kẹt hạt (granular jamming) hoặc kẹt tấm (layer jamming). Điều này **không tương đương về mặt cơ học** với việc các dây NiTi tự đóng vai trò là mạng lưới tiếp xúc ma sát trượt (friction contact network). Do đó:
  - Khẳng định cấp thiết bị "SMA + Jamming cùng xuất hiện trong một hệ thống" là **ĐÓNG HOÀN TOÀN**.
  - Khẳng định cấp cơ học "SMA tự tạo ra mạng tiếp xúc trượt nhạy áp suất" không thuộc C3 mà phải được chuyển giao sang kiểm chứng tại C5/T1.

---

### 2.4. C4: Khẳng định tính mới về Nguồn áp suất Tích hợp/Gọn nhẹ (Compact/On-board Pressure Source)
- **Tuyên bố gốc:** Tích hợp bộ tạo áp suất nhỏ gọn (như bơm điện hóa lỏng ECF hoặc cơ cấu piston thu nhỏ) để kích hoạt biến đổi độ cứng tại chỗ là giải pháp mới.
- **Phán quyết:** `CLOSED` / `PREEMPTED`.
- **Bằng chứng tiền nhiệm then chốt:**
  - Huynh et al. (2022, DOI: 10.20965/jrm.2022.p0466): Tích hợp bơm ECF (electro-conjugate fluid) mini để tạo áp suất giam giữ cục bộ.
  - Wang et al. (2024, DOI: 10.1016/j.birob.2024.100163): Cơ chế kẹt hạt dạng piston (piston-like particle jamming) dùng truyền động xi lanh tích hợp trên cánh tay robot mềm.
- **Lý do đóng:** Việc thu nhỏ và tích hợp nguồn áp lực thủy lực/khí nén/piston vào kết cấu robot mềm là một bài toán kỹ thuật hệ thống (engineering integration), không chứa đựng nguyên lý cơ học vật liệu mới.
- **Giới hạn hiệu lực (Residual Caveat):** Thuật ngữ "tích hợp/gọn nhẹ" (compact/on-board) không được thổi phồng thành "hệ thống hoàn toàn tự chủ năng lượng, không dây hoặc không cần bình chứa" (untethered self-contained system). Đánh giá tiền nhiệm chỉ áp dụng cho nguyên lý tạo áp suất tại chỗ, không phủ định các cải tiến gia công cơ khí cụ thể.

---

## 3. Kết luận của Worker W02

1. Bốn khẳng định C1, C2, C3, C4 tiếp tục được giữ nguyên trạng thái đóng vững chắc (`CLOSED`). Mọi nỗ lực tìm kiếm tính mới ở tầng tích hợp thiết bị (device-level integration) hoặc ghép nối các thành phần chức năng đã biết đều bị tiền nhiệm bác bỏ.
2. Việc rời bỏ các claim kiến trúc C1–C4 để co cụm vào bài toán cơ học tiếp xúc lõi (mechanics core) là một quyết định hoàn toàn đúng đắn về mặt phương pháp luận khoa học.
3. Tuy nhiên, việc đóng C1–C4 không tự động chứng minh phần cơ học còn lại (C5–C8, T1–T3) là mới; phần cơ học này bắt buộc phải chịu sự kiểm chứng độc lập và khắt khe tại các worker tiếp theo.
