# W03: Sửa chữa Ranh giới Cơ học C5–C8 (C5–C8 Boundary Repair)

**Worker ID:** W03  
**Mục tiêu:** Khắc phục tình trạng xác định ranh giới cơ học mập mờ, giải quyết các lỗ hổng do Astra chỉ ra tại C5, C6, C7 và C8; ngăn chặn việc tạo ra "khoảng trống nghiên cứu giả" (false gap) bằng cách phân biệt rõ giữa mô tả kho dữ liệu hiện tại và kết luận khoa học bản chất.  
**Ngày thực hiện:** 2026-09-25  

---

## 1. Vấn đề cốt lõi tại Ranh giới C5–C8

Trong các báo cáo trước, một số khẳng định cơ học (C5, C6, C7) được gán nhãn `open` hoặc `open_in_current_full_text_set`. Tuy nhiên, như Astra đã chỉ ra rất sắc bén trong phê bình mục 4:
- Việc duy trì nhãn `open` cho C5 mà không nêu rõ bối cảnh lịch sử sẽ tạo ra một khoảng trống giả tạo, bởi vì hành vi ma sát của dây NiTi đã bị đe dọa trực tiếp bởi T1.
- Đối với C6 và T2, trạng thái `open_in_current_full_text_set` chỉ là một phát biểu mô tả trạng thái thư mục (corpus description), hoàn toàn không đủ để trở thành một kết luận khoa học (scientific conclusion) rằng bài toán áp suất giam giữ là một lớp lý thuyết cơ học mới.
- Đối với C7, việc 4 yếu tố (NiTi, trượt ma sát, áp suất, độ cứng) chưa từng xuất hiện đồng thời trong cùng một bài báo không phải là bằng chứng cho thấy giữa chúng tồn tại một cơ chế ghép cặp tương tác mới chưa giải quyết.

Worker W03 tiến hành sửa chữa tường minh ranh giới cơ học cho từng khẳng định này.

---

## 2. Chi tiết Sửa chữa Ranh giới cho từng Khẳng định

### 2.1. Khắc phục C5: Dây NiTi đóng vai trò là Môi trường Tiếp xúc Ma sát (NiTi as Friction Medium)
- **Tình trạng trước đây:** Được coi là "mở" (open) trong V001 do các bài báo V001 chỉ tập trung vào sợi thép, carbon hoặc nylon.
- **Lỗ hổng khoa học:** Duy trì nhãn `open` trong V002 là sai lệch, bởi vì tập tài liệu V002 (đặc biệt là Vahidi 2022, Carboni 2015, Reedlunn 2013, Falcetelli 2024, Silva 2022) đã nghiên cứu sâu rộng tương tác tiếp xúc và ma sát trượt nội tại giữa các dây NiTi.
- **Sửa chữa ranh giới (Boundary Repair):**
  - Khẳng định rộng: *"Dây NiTi có thể trượt và tiêu tán năng lượng qua ma sát tiếp xúc"* -> **ĐÃ BỊ TIỀN NHIỆM ĐÓNG HOÀN TOÀN** (`CLOSED` bởi T1).
  - Khẳng định hẹp chỉ được phép tồn tại nếu chỉ ra được một đại lượng động học hoặc cơ chế tiếp xúc chưa từng được mô tả. Việc chỉ đổi tên từ "cáp xoắn" (twisted cable/wire rope) sang "bó dây thẳng/song song" (straight/parallel wire bundle) **không tạo ra cơ học mới**, vì cả hai đều chịu sự chi phối của cùng một mạng lưới tiếp xúc (contact network) và định luật ma sát trượt Coulomb giữa các mặt trụ ($F_{\text{fric}} \le \mu N$).

---

### 2.2. Khắc phục C6 / T2: Áp suất Giam giữ Chủ động (Active Confinement) là Bài toán Cơ học Riêng
- **Tình trạng trước đây:** Đánh giá là `open_in_current_full_text_set`, từ đó suy đoán rằng "áp suất giam giữ chủ động tạo ra một miền cơ học mới".
- **Lỗ hổng khoa học:** Nhầm lẫn giữa **giao thức điều khiển thực nghiệm** (protocol) và **nguyên lý cơ học** (mechanics). Ba mức phân loại áp suất P1, P2, P3:
  - $P_1$: Áp suất thụ động từ quá trình chế tạo / xoắn cáp (passive manufacturing preload).
  - $P_2$: Áp suất cố định do tải ngoài được áp đặt trước (fixed external preload).
  - $P_3$: Áp suất giam giữ chủ động được điều khiển thay đổi độc lập với biến dạng uốn ($p(t)$).
- **Sửa chữa ranh giới (Boundary Repair):**
  - $P_1, P_2, P_3$ chỉ mô tả cách thức sinh ra hoặc kiểm soát tải trọng biên; chúng **không tự xác định ba lớp lý thuyết cơ học khác nhau**.
  - Phương trình ma sát Coulomb cục bộ tại điểm tiếp xúc:
    $$f_t \le \mu f_n$$
    trong đó lực pháp tuyến $f_n$ là một hàm phụ thuộc vào áp suất giam giữ $p$ và hình học bó dây: $f_n = \mathcal{G}(p, \mathbf{x})$.
  - Một phương trình cân bằng tiếp xúc cơ học đã biết hoàn toàn có khả năng tiếp nhận một điều kiện biên áp suất biến thiên theo thời gian $p(t)$ mà **không đòi hỏi bất kỳ phương trình cơ học mới nào**.
  - Do đó, C6/T2 không được tuyên bố là một "lớp lý thuyết mới", mà chỉ là một **điều kiện biên tải trọng biến thiên cần kiểm tra tính hợp lệ của mô hình hiện hữu**.

---

### 2.3. Khắc phục C7: Ghép cặp NiTi – Trượt ma sát – Áp suất – Biến thiên Độ cứng
- **Tình trạng trước đây:** Được mô tả như một "miền cơ học chưa được giải quyết" (unresolved coupled mechanics domain).
- **Lỗ hổng khoa học:** Ngụy biện "chưa xuất hiện cùng nhau" (conjunction fallacy). Việc một bài báo chưa ghép 4 từ khóa trên không chứng minh rằng các định luật hiện hữu thất bại khi kết hợp chúng.
- **Sửa chữa ranh giới (Boundary Repair):**
  - **Giả thuyết cạnh tranh tối thiểu (Alternative Explanation):** Một mô hình kết hợp bao gồm:
    1. Luật cấu thành siêu đàn hồi NiTi đã biết (như mô hình Auricchio-Petrini hoặc Graesser-Cozzarelli);
    2. Định luật tiếp xúc dính - trượt Coulomb đã biết với lực pháp tuyến phụ thuộc áp suất ($N = \mathcal{F}(p)$);
    3. Phương trình cân bằng động học dầm/thanh phi tuyến hình học.
    Hệ thống này **tự động sinh ra** sự phân bố lại ứng suất, ngưỡng trượt phụ thuộc áp suất và độ cứng uốn biến thiên theo lịch sử tải uốn mà không cần thêm bất kỳ một số hạng tương tác vi mô huyền bí nào.
  - Vì vậy, C7 chỉ được phép tồn tại dưới dạng một **bài toán kiểm chứng giả thuyết (hypothesis testing)**: Liệu mô hình ghép tiêu chuẩn nói trên có dự đoán được hành vi uốn hay không? Trạng thái khoa học chính xác của C7 là `PROVISIONALLY SURVIVING HYPOTHESIS`, không phải là `PROVEN NOVEL DOMAIN`.

---

### 2.4. Khắc phục C8: Tích hợp SMA Syringe/Piston kết hợp Jamming
- **Tình trạng trước đây:** Gán nhãn `substantially_preempted`.
- **Lỗ hổng khoa học:** Dù kết luận tiền nhiệm chiếm lĩnh là đúng, các diễn đạt cũ đôi khi gây hiểu lầm rằng toàn bộ thiết kế chi tiết cụ thể đã bị sao chép nguyên xi.
- **Sửa chữa ranh giới (Boundary Repair):**
  - Khẳng định chính xác: Các thành phần chức năng cơ sở gồm bộ truyền động SMA (SMA wire/spring actuator), cơ cấu piston nén môi trường kẹt (piston jamming) và cơ chế biến đổi độ cứng đều đã có tiền nhiệm trực tiếp (Wang 2024, Huynh 2022, Takashima 2021).
  - Sự kết hợp cơ học của các chi tiết này là một **giải pháp thiết kế kỹ thuật (engineering implementation)** chứ không phải một đóng góp khoa học cơ bản (scientific contribution). Do đó C8 giữ nguyên phán quyết `SUBSTANTIALLY_PREEMPTED`.

---

## 3. Kết luận của Worker W03

Bằng việc sửa chữa ranh giới cơ học cho C5–C8:
1. Đã loại bỏ hoàn toàn các khoảng trống nghiên cứu giả tạo do đổi tên thiết bị hoặc do thiếu vắng tổ hợp từ khóa.
2. Xác định rõ ràng: Áp suất chủ động ($P_3$) chỉ là một điều kiện biên tải trọng, không phải là một nguyên lý vật lý mới.
3. Rút gọn trọng tâm duy nhất có thể bảo vệ được của đề tài về bài toán: Đánh giá khả năng dự đoán của các mô hình cơ học cấu thành - tiếp xúc hiện hữu khi áp đặt điều kiện biên áp suất giam giữ thay đổi.
