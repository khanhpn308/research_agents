# Đánh giá mức liên quan của Ye et al. (2024) đối với dự án M1

## Kết luận quyết định

- **Có cần thêm (add/ingest) PDF không? — Không.** Tệp người dùng chỉ ra đã có trong corpus xác minh với `paper_id: 53d328abaa`, thuộc vòng `D1-V008`, trạng thái `included` và `ingestion_status: complete`.
- **Có nên dùng để suy luận không? — Có, nhưng chỉ như prior work cơ học lân cận và mẫu phương pháp đánh giá mô hình.** Không dùng nó làm định luật tiếp xúc trực tiếp cho dầm kẹt lớp chân không.
- **Có cần mở vòng xác minh mới chỉ vì tệp này không? — Không.** Bài đã được kiểm tra toàn văn trong `D1-V008`; kết luận khi đó là `SURVIVES_FINAL_TARGET`, tức bài là mối đe dọa gần nhưng không phủ kín đóng góp còn lại của P1.
- **Mức ưu tiên đọc hiện tại — Trung bình/tham khảo.** Ưu tiên trước mắt vẫn là tái dựng chính xác M1 của Zhang và đóng băng mô hình tham chiếu toàn lớp R.

## Nhận dạng và trạng thái bằng chứng

**[VERIFIED FULL TEXT]**

- Huawen Ye, Zhihao Fen, Jianxi He, và Jialin Deng (2024), *Analytical Solution for Bending Deformation of Steel–Concrete Composite Beams Considering Nonlinear Interfacial Slip*.
- *Journal of Structural Engineering*, 150(6), 04024058.
- DOI: `10.1061/JSENDH.STENG-13096`.
- PDF có 11 trang.
- SHA-256 của tệp người dùng, bản thứ hai trong thư mục Downloads và bản đã đăng ký trong dự án đều giống nhau:
  `53d328abaad573cca78c06c352a0e3d12ccff148a7597ff3947273297608e210`.

Do đó, nhập lại tệp sẽ chỉ tạo bản trùng, không bổ sung bằng chứng mới.

## Bài báo thực sự đóng góp điều gì?

### 1. Một mô hình dầm rút gọn có trượt liên diện phi tuyến

**[VERIFIED FULL TEXT — PDF pp. 1, 4–5]** Bài xây dựng nghiệm giải tích dạng đóng cho dầm liên hợp thép–bê tông có tương tác cắt không hoàn toàn. Mô hình kết hợp:

- lý thuyết dầm Euler–Bernoulli;
- nguyên lý thế năng cực tiểu và phương pháp biến phân;
- chuỗi lượng giác;
- quan hệ tải cắt–độ trượt phi tuyến của đinh chống cắt;
- công thức độ cứng uốn hữu hiệu có xét trượt liên diện.

Giá trị đối với dự án: đây là ví dụ rõ về cách biến một kết cấu có tương tác liên diện thành mô hình dầm rút gọn với biến trượt và các đại lượng đầu ra có thể kiểm chứng.

### 2. Một mẫu so sánh giải tích – phần tử hữu hạn – thí nghiệm

**[VERIFIED FULL TEXT — PDF pp. 6–9]** Bài so sánh nghiệm giải tích với bốn dầm thí nghiệm đã công bố và với mô hình phần tử hữu hạn ba chiều dùng phần tử rời rạc cho đinh chống cắt. Các đầu ra gồm:

- độ võng;
- phân bố trượt liên diện;
- biến dạng uốn theo chiều cao tiết diện.

Bài báo cáo các sai khác quan sát được như khoảng 3% đối với độ võng giải tích–thí nghiệm, tối đa 5% đối với FE–thí nghiệm, dưới 8% đối với biến dạng và không quá 0,02 mm đối với một so sánh độ trượt ở tải thấp.

Giá trị đối với dự án: các đầu ra này gợi ý một cấu trúc kiểm chứng cho M1–R–E. Tuy nhiên, các con số trên **không phải** ngưỡng chấp nhận được tuyên bố trước và không được sao chép thành tolerance của dự án hiện tại.

### 3. Một ví dụ về cơ chế bị bỏ qua làm mô hình mất hiệu lực

**[VERIFIED FULL TEXT — PDF pp. 9–10]** Vì nghiệm giải tích bỏ qua biến dạng cắt ngang, ảnh hưởng của cắt làm độ võng tăng tới khoảng 20% tại `L/H = 5`; tác giả khuyến nghị mô hình cho dầm tương đối mảnh với `L/H >= 10`.

Giá trị đối với dự án: đây là ví dụ hữu ích cho logic

`giả thiết rút gọn → cơ chế bị bỏ qua → sai số đầu ra tăng → miền áp dụng bị giới hạn`.

Nó nhắc dự án phải kiểm tra xem tỷ số nhịp/chiều dày và biến dạng cắt có phải biến gây nhiễu hoặc điều kiện bảo vệ cho M1 hay không. **Không tự động thêm `L/H` vào ma trận thí nghiệm** trước khi tái dựng giả thiết của Zhang và kiểm tra phạm vi hình học dự kiến.

## Bài báo không đóng góp được điều gì cho M1?

**[VERIFIED FULL TEXT — PDF p. 2; D1-V008 audit]** Cơ chế của Ye et al. là tải–trượt của các đinh chống cắt nối hai cấu kiện thép–bê tông. Bài giả thiết bỏ qua ma sát liên diện, uplift và biến dạng cắt trong nghiệm giải tích; mô hình FE cũng bỏ qua ma sát liên diện.

Vì vậy, bài không cung cấp trực tiếp:

- quan hệ từ áp suất chân không đến áp lực pháp tuyến giữa các lớp;
- tiếp xúc Coulomb phân bố và chuyển trạng thái stick/partial slip/full slip;
- tương tác của nhiều lớp mỏng;
- tái phân bố áp suất tiếp xúc;
- tách lớp/lift-off;
- mô hình tham chiếu toàn lớp phù hợp riêng cho layer jamming;
- biên hợp lệ được định nghĩa bằng tolerance đầu ra đã tuyên bố trước;
- thí nghiệm chủ động đi qua cả phía hợp lệ và mất hiệu lực của biên đó.

Do đó, không được chuyển nguyên xi phương trình tải–trượt của đinh chống cắt sang M1 hoặc R. Một phép chuyển như vậy cần một lập luận cơ học và hiệu chuẩn mới, chứ không chỉ đổi vật liệu hoặc hình học.

## Vai trò nên gán trong luận văn và quá trình suy luận

| Vai trò | Quyết định | Cách dùng |
|---|---:|---|
| Nguồn vật lý cốt lõi cho layer jamming | Không | Không dùng làm luật tiếp xúc chân không hoặc ma sát giữa lớp |
| Prior work về partial interaction/nonlinear slip | Có | Dùng trong tổng quan mô hình dầm có trượt liên diện |
| Mẫu xây dựng mô hình rút gọn | Có | Học cách nối giả thiết, biến trượt, độ cứng hữu hiệu và đầu ra |
| Mẫu thiết kế đánh giá M1–R–E | Có điều kiện | Học cấu trúc so sánh, nhưng phải tuyên bố tolerance trước khi xem sai số |
| Bằng chứng về validity boundary của M1 Zhang | Không | `L/H >= 10` chỉ là giới hạn của mô hình Ye, không phải biên của M1 |
| Mối đe dọa novelty | Đã xử lý | Đã được audit toàn văn trong `D1-V008`; không cần vòng mới |

## Cách đọc tiết kiệm thời gian

Không cần đọc từng chữ ngay lúc này. Đọc có mục tiêu theo thứ tự:

1. **PDF p. 1:** abstract, câu hỏi nghiên cứu và đóng góp.
2. **PDF p. 2:** toàn bộ giả thiết; đánh dấu các cơ chế bị loại bỏ.
3. **PDF pp. 4–5:** cấu trúc nghiệm, biến trượt và độ cứng uốn hữu hiệu.
4. **PDF pp. 6–9:** cách so sánh với thí nghiệm/FE và các đầu ra đánh giá.
5. **PDF pp. 9–10:** nghiên cứu `L/H`, ảnh hưởng biến dạng cắt và giới hạn áp dụng.

Khi ghi chú, tách ba cột: `có thể chuyển về mặt phương pháp`, `không thể chuyển về mặt vật lý`, và `câu hỏi cần kiểm tra cho M1`.

## Hành động đề xuất

1. Không chạy lại `add_paper` và không tạo bản ghi registry mới.
2. Khi cần suy luận, dùng bản và evidence hiện có của `paper_id 53d328abaa`.
3. Giữ bài trong nhóm **adjacent mechanics / partial interaction**, không đưa vào nhóm nguồn cốt lõi định nghĩa vật lý M1 hoặc R.
4. Sau khi hoàn tất tái dựng M1, kiểm tra riêng liệu Zhang có bỏ qua biến dạng cắt hay không; chỉ khi đó mới quyết định có đưa `L/H` vào điều kiện miền khảo sát.

## Provenance

- [PDF đã đăng ký](../../../data/papers/verification/D1-V008/2024-Ye-Analytical%20Solution%20for%20Bending%20Deformation%20of%20Steel-Concrete%20Composite%20Beams%20Considering%20Nonlinear%20Interfacial%20Slip.pdf)
- [Evidence toàn văn đã trích xuất](../../../data/evidence/2024-Ye-Analytical%20Solution%20for%20Bending%20Deformation%20of%20Steel-Concrete%20Composite%20Beams%20Considering%20Nonlinear%20Interfacial%20Slip_53d328abaa.json)
- [D1-V008 final named-target audit](../../../outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.md)
- [D1-V008 verification matrix](../../../outputs/verification/D1-V008/verification_matrix.json)

## Khoảng trống bằng chứng còn lại

- Đánh giá này không tái kiểm chứng độc lập các thí nghiệm gốc mà Ye et al. lấy từ Yu et al. (2003) và Huang et al. (2018).
- Chưa quyết định `L/H` có phải biến bắt buộc của thiết kế M1–R–E; quyết định đó phụ thuộc vào quá trình tái dựng phương trình và giả thiết của Zhang.
- Kết luận `không cần add` chỉ áp dụng cho đúng PDF có SHA-256 nêu trên. Supplement, correction hoặc phiên bản khác có nội dung mới phải được kiểm tra riêng.
