# Kiến trúc nghiên cứu M1

> **Trạng thái:** Kiến trúc làm việc sau khi đã chọn chính xác mô hình  
> **Mô hình rút gọn được chọn:** M1 — Zhang và cộng sự, *A continuum-based model for a layer jamming beam*  
> **DOI:** 10.5194/ms-16-821-2025  
> **paper_id:** 95646b2cfc  
> **Trạng thái bằng chứng:** ĐÃ XÁC MINH TOÀN VĂN
>
> Tài liệu này cố định kiến trúc luận văn hiện tại sau khi quy trình phản biện–bác bỏ từ literature đã đạt điều kiện dừng và cho phép khóa tạm thời tính mới. Tài liệu dùng để định hướng giai đoạn tiếp theo: chọn mô hình tham chiếu, khóa câu hỏi nghiên cứu, xác định ngưỡng sai số chấp nhận được, triển khai mô hình và thiết kế thí nghiệm.

---

## 1. Tiền đề nghiên cứu hiện đang được triển khai

Tiền đề nghiên cứu còn tồn tại sau các vòng kiểm chứng là:

> Với một mô hình rút gọn/liên tục cụ thể cho dầm kẹt lớp chân không dưới uốn phẳng quasi-static, xác định trước các ngưỡng sai số chấp nhận được theo từng đầu ra của mô hình, sau đó xác định bằng thực nghiệm các biên hiệu lực/phá vỡ khi so với một mô hình tham chiếu full-layer có phân giải interface, đồng thời biểu diễn rõ ảnh hưởng của áp suất tiếp xúc do chân không tạo ra, sự tiến triển của ma sát/trượt và, khi cần, sự phân bố lại áp suất hoặc tách lớp.

Vòng adversarial audit cuối cùng kết luận rằng:

- hướng nghiên cứu đã chọn vẫn sống sót sau kiểm tra đối với mục tiêu được nêu đích danh cuối cùng;
- không có nguồn nào trong tập bằng chứng thỏa toàn bộ chuỗi điều kiện để bác bỏ hướng nghiên cứu;
- nhánh forward citation đang xét đã được đóng;
- DOI có mức đe dọa cao cuối cùng đã được audit từ toàn văn đã xác minh;
- không còn mục tiêu đe dọa cao cụ thể nào khác được nêu đích danh;
- nên dừng việc tìm kiếm literature theo diện rộng;
- cho phép khóa tạm thời tính mới để chuyển sang triển khai luận văn.

Việc khóa này là **tạm thời để triển khai luận văn**, không phải tuyên bố tuyệt đối rằng trên thế giới không tồn tại bất kỳ công trình trùng lặp nào.

---

# 2. Mô hình rút gọn M — ĐÃ KHÓA

## M = mô hình continuum cho dầm layer-jamming của Zhang và cộng sự

~~~text
REDUCED MODEL M =
Zhang et al.
"A continuum-based model for a layer jamming beam"
DOI: 10.5194/ms-16-821-2025
paper_id: 95646b2cfc
~~~

### Vì sao chọn M1

M1 được chọn vì nó đã hoạt động ở đúng cấp độ kết cấu mà P1 hiện tại yêu cầu:

~~~math
\text{áp suất chân không + ma sát + tải dầm}
\rightarrow
\text{trạng thái jam/trượt}
\rightarrow
\text{đáp ứng kết cấu của dầm}
~~~

Các năng lực của M1 đã được xác minh gồm:

- biểu diễn dầm layer-jamming có chiều cao hữu hạn như một continuum;
- điều kiện trượt Coulomb tường minh;
- các trạng thái jammed / trượt một phần / trượt hoàn toàn;
- biên trượt trên tiết diện;
- phân bố ứng suất bên trong;
- các ngưỡng trượt tới hạn;
- đáp ứng tải–độ võng của dầm;
- so sánh với FEA có số lớp hữu hạn;
- so sánh với thí nghiệm trên dầm thực.

Các quan hệ chi phối đã được xác minh gồm:

~~~math
\tau(y,Q)
=
\frac{3}{2}\frac{Q}{A}
\left(
1-\frac{4y^2}{h^2}
\right)
~~~

~~~math
|\tau|=\mu p
~~~

và

~~~math
Q_{\mathrm{slip}}
=
\frac{2}{3}\mu p A
~~~

trong đó:

- \(Q\): lực cắt bên trong;
- \(A=bh\): diện tích tiết diện dầm;
- \(b\): bề rộng dầm;
- \(h\): tổng chiều cao chồng lớp;
- \(y\): tọa độ theo chiều dày;
- \(\mu\): hệ số ma sát giữa các lớp;
- \(p\): áp suất chân không/áp suất ép giữ.

---

# 3. Phép rút gọn khoa học nào đang được kiểm tra?

Xấp xỉ trung tâm trong M1 là:

~~~math
\text{dầm nhiều lớp rời rạc với số lớp hữu hạn}
\rightarrow
\text{dầm continuum với biểu diễn jam/trượt liên tục}
~~~

Vì vậy, luận văn **không** chủ yếu hỏi liệu có thể xây dựng một mô hình continuum hay không. Việc đó đã được thực hiện.

Luận văn hỏi:

> **Trong điều kiện nào xấp xỉ continuum này vẫn đủ chính xác, và từ điều kiện nào nó không còn đủ chính xác khi so với một mô hình tham chiếu nhiều lớp có độ trung thực cao hơn và với thực nghiệm?**

Đây là bài toán về **giới hạn hiệu lực của mô hình**.

---

# 4. Kiến trúc mô hình tham chiếu

## 4.1 Mô hình tham chiếu chính R — khóa tạm thời

~~~text
PRIMARY REFERENCE R =
mô hình phần tử hữu hạn full-layer với tiếp xúc tường minh
~~~

Mô hình tham chiếu có độ trung thực cao dự kiến phải giữ lại càng nhiều càng tốt các cơ chế rời rạc đã bị M1 đơn giản hóa:

- mỗi lớp vật lý được mô hình riêng;
- từng interface được mô hình tường minh;
- tiếp xúc theo phương pháp tuyến;
- ma sát Coulomb;
- sự tiến triển stick/slip;
- số lớp hữu hạn;
- sự phân bố lại áp suất tiếp xúc cục bộ;
- khả năng tách/lift-off khi có cơ sở vật lý;
- cùng hình học dầm và điều kiện biên dùng để so sánh với M1.

### Vì sao đây là mô hình tham chiếu được ưu tiên

M1 loại bỏ các interface rời rạc bằng cách thay chúng bằng một xấp xỉ continuum. Vì vậy một mô hình tham chiếu hữu ích phải khôi phục lại các interface đó:

~~~math
M:
\text{xấp xỉ continuum}
~~~

so với

~~~math
R:
\text{các lớp hữu hạn rời rạc + tiếp xúc ma sát tường minh}
~~~

Mô hình tham chiếu phải được xem là **mô hình số có độ trung thực cao hơn để so sánh**, không mặc định là chân lý vật lý tuyệt đối.

Các giả định, độ nhạy lưới, formulation tiếp xúc, hành vi hội tụ và tham số vật liệu của chính R cũng phải được ghi chép và kiểm chứng.

---

## 4.2 Mô hình tham chiếu phụ

~~~text
SECONDARY REFERENCE =
Caruso et al. (2023)
"Layer jamming: Modeling and experimental validation"
paper_id: 652e62758f
~~~

Vai trò:

- benchmark cơ học phân tích/rời rạc;
- kiểm tra độc lập quá trình trượt tiến triển tại các interface;
- hỗ trợ xác minh các ngưỡng chuyển trạng thái trượt;
- hỗ trợ debug phần triển khai M1 và mô hình FE full-layer.

Caruso 2023 không nên thay thế mô hình FE full-layer chính nếu mục tiêu luận văn là xây dựng bản đồ validity/breakdown ở cấp kết cấu với cơ học tiếp xúc tường minh.

---

# 5. Các đầu ra chính — khóa tạm thời

Bước triển khai đầu tiên nên tập trung vào một số ít đầu ra thỏa bốn điều kiện:

1. M1 có thể dự đoán;
2. có thể trích xuất từ mô hình tham chiếu;
3. có thể đo bằng thực nghiệm;
4. liên quan trực tiếp đến đáp ứng kết cấu.

## O1 — Độ võng của dầm

~~~math
w
~~~

Đại lượng so sánh được đề xuất:

~~~math
e_w
=
\frac{|w_M-w_R|}
{|w_R|}
~~~

Vì sao quan trọng:

- là đáp ứng kết cấu trực tiếp;
- dễ lấy từ mô phỏng;
- tương đối dễ đo bằng thực nghiệm;
- trực quan khi trình bày với mentor;
- phù hợp để xây dựng validity map.

---

## O2 — Độ cứng uốn hiệu dụng

~~~math
K
~~~

hoặc độ cứng chống uốn hiệu dụng tương đương:

~~~math
EI_{\mathrm{eff}}
~~~

Đại lượng so sánh được đề xuất:

~~~math
e_K
=
\frac{|K_M-K_R|}
{|K_R|}
~~~

Vì sao quan trọng:

- thay đổi độ cứng là chức năng trung tâm của layer jamming;
- suy giảm độ cứng phản ánh quá trình chuyển từ jammed sang slipping;
- hữu ích để so sánh các vùng vận hành theo áp suất và số lớp.

---

## O3 — Tải chuyển trạng thái trượt

Một đại lượng ứng viên là:

~~~math
Q_{\mathrm{slip}}
~~~

hoặc tải ngoài tương ứng tại thời điểm bắt đầu trượt.

Đại lượng so sánh được đề xuất:

~~~math
e_Q
=
\frac{|Q_{\mathrm{slip},M}-Q_{\mathrm{slip},R}|}
{|Q_{\mathrm{slip},R}|}
~~~

Vì sao quan trọng:

- kiểm tra liệu M1 có dự đoán đúng cơ chế chuyển trạng thái hay không;
- mang tính cơ chế hơn so với chỉ nhìn độ võng;
- liên hệ trực tiếp với điều kiện trượt Coulomb.

### Các đầu ra phụ có thể xem xét sau

Không nên nâng các đại lượng sau thành đầu ra chính trước khi phần triển khai cơ bản ổn định:

- độ rộng/vị trí vùng trượt \(y_s\);
- trượt cục bộ tại interface;
- phân bố áp suất tiếp xúc;
- năng lượng tiêu tán;
- diện tích vòng trễ;
- trường ứng suất cục bộ.

Các đại lượng này có thể hữu ích để giải thích *vì sao* M1 thất bại sau khi validity map chính đã được thiết lập.

---

# 6. Các biến gây breakdown chính — khóa tạm thời

Nghiên cứu validity đầu tiên nên tránh một không gian tham số có số chiều quá lớn.

Ba biến breakdown ban đầu là:

## B1 — Số lớp hữu hạn

~~~math
n
~~~

### Lý do khoa học

M1 dựa trên xấp xỉ continuum của một cấu trúc nhiều lớp.

Vì vậy số lớp hữu hạn là một trong những biến trực tiếp nhất để kiểm tra hiệu lực của xấp xỉ continuum.

Giả thuyết làm việc:

~~~math
n \uparrow
\quad\Rightarrow\quad
\text{chồng lớp rời rạc tiến gần hành vi continuum}
~~~

nhưng điều này phải được kiểm tra, không được mặc định là đúng.

Các câu hỏi tiềm năng:

- Có tồn tại một \(n\) tối thiểu mà từ đó sai số độ võng luôn nằm trong giới hạn chấp nhận được không?
- \(n\) cần thiết có phụ thuộc vào áp suất không?
- \(n\) cần thiết có tăng khi tiến gần trạng thái partial/full slip không?

---

## B2 — Áp suất chân không

~~~math
p
~~~

### Lý do khoa học

Áp suất chân không trực tiếp kiểm soát khả năng ma sát trong lý tưởng hóa của M1:

~~~math
|\tau|_{\max}
=
\mu p
~~~

Do đó áp suất ảnh hưởng đến:

- thời điểm bắt đầu trượt;
- kích thước vùng jammed/slipping;
- độ cứng hiệu dụng;
- đáp ứng kết cấu.

Các cơ chế breakdown tiềm năng gồm:

- áp suất tiếp xúc không đồng đều;
- phân bố lại áp suất do biến dạng;
- mất tiếp xúc cục bộ;
- sai khác giữa \(p\) lý tưởng và áp suất thực tại interface.

---

## B3 — Mức độ uốn

Các biến điều khiển ứng viên:

~~~math
P
~~~

hoặc

~~~math
\kappa
~~~

trong đó \(P\) là tải ngang tác dụng và \(\kappa\) là độ cong của dầm.

### Lý do khoa học

Khi mức độ uốn tăng, cấu trúc có thể lần lượt đi qua:

~~~text
jammed hoàn toàn
→ trượt một phần
→ trượt tiến triển
→ gần/trượt hoàn toàn
~~~

Mô hình continuum có nhiều khả năng bộc lộ giới hạn dạng mô hình quanh các vùng chuyển trạng thái này và ở biến dạng lớn.

Việc chọn chính xác giữa tải \(P\), độ cong \(\kappa\), độ võng chuẩn hóa hoặc một đại lượng không thứ nguyên khác chỉ nên được khóa sau khi M1 được tái dựng đầy đủ và mô hình tham chiếu đã được xác định rõ.

---

# 7. Câu hỏi nghiên cứu ban đầu

## Tiếng Anh

> **Under what combinations of finite layer count, vacuum pressure, and bending severity does the Zhang et al. continuum layer-jamming beam model remain within predeclared output-specific model-form error tolerances relative to an explicit full-layer frictional-contact reference and physical experiments?**

## Tiếng Việt

> **Trong phạm vi nào của số lớp hữu hạn, áp suất chân không và mức độ uốn, mô hình continuum cho dầm layer-jamming của Zhang và cộng sự vẫn duy trì sai số mô hình trong các giới hạn chấp nhận được đã định trước khi so với mô hình full-layer có tiếp xúc–ma sát tường minh và thực nghiệm?**

Câu hỏi này vẫn là **câu hỏi nghiên cứu làm việc**. Chỉ nên khóa chính thức sau khi formulation chính xác của mô hình tham chiếu, các đầu ra và định nghĩa tham số đã được khóa.

---

# 8. Giả thuyết ban đầu có thể bị bác bỏ

> Khi số lớp tăng, M1 nhìn chung sẽ tiến gần hơn đến mô hình tham chiếu nhiều lớp hữu hạn; tuy nhiên sai số dạng mô hình được kỳ vọng sẽ tăng khi số lớp nhỏ, mức độ uốn/trượt lớn hơn và trong các điều kiện mà sự phân bố lại áp suất tiếp xúc theo phương pháp tuyến hoặc sự tách lớp trở nên quan trọng.

Đây là **giả thuyết cần được kiểm tra và có thể bị bác bỏ**, không phải kết luận.

Luận văn vẫn có giá trị khoa học ngay cả khi một hoặc nhiều phần của giả thuyết này bị bác bỏ.

---

# 9. Chỉ số sai số và ngưỡng chấp nhận được định trước

## 9.1 Chỉ số sai số

Tối thiểu gồm:

~~~math
e_w
=
\frac{|w_M-w_R|}
{|w_R|}
~~~

~~~math
e_K
=
\frac{|K_M-K_R|}
{|K_R|}
~~~

~~~math
e_Q
=
\frac{|Q_{\mathrm{slip},M}-Q_{\mathrm{slip},R}|}
{|Q_{\mathrm{slip},R}|}
~~~

Có thể cần dùng chỉ số chuẩn hóa khác hoặc sai số tuyệt đối khi mẫu số tiến gần 0.

## 9.2 Quy tắc đối với tolerance định trước

Một tolerance chỉ được xem là **định trước** nếu nó được cố định trước khi xem validity/error map cuối cùng.

Do đó workflow phải là:

~~~text
xác định đầu ra
→ xác định chỉ số sai số
→ biện minh cho tolerance
→ khóa tolerance
→ chạy validation cuối
→ phân loại VALID / INVALID
~~~

Không phải:

~~~text
chạy validation
→ xem sai số
→ chọn một tolerance thuận tiện sau đó
~~~

Không được chọn một giá trị như 5% chỉ vì một paper khác đã dùng 5%.

Các tolerance cuối cùng nên được biện minh dựa trên một hoặc nhiều yếu tố:

- mức độ liên quan về kỹ thuật;
- độ không đảm bảo của phép đo thực nghiệm;
- độ không đảm bảo của mô hình số/mô hình tham chiếu;
- mục đích sử dụng dự kiến của mô hình;
- độ nhạy của quyết định kỹ thuật đối với sai số dự đoán.

---

# 10. Khái niệm validity map

Với mỗi điểm vận hành:

~~~math
\mathbf{x}
=
\{n,p,\text{mức độ uốn},\ldots\}
~~~

tính một hoặc nhiều sai số đầu ra:

~~~math
e_w(\mathbf{x}),
\quad
e_K(\mathbf{x}),
\quad
e_Q(\mathbf{x})
~~~

Sau đó phân loại theo các tolerance đã định trước:

~~~math
e_i(\mathbf{x})
\le
\varepsilon_i
\quad\Rightarrow\quad
\text{VALID đối với đầu ra }i
~~~

và

~~~math
e_i(\mathbf{x})
>
\varepsilon_i
\quad\Rightarrow\quad
\text{INVALID đối với đầu ra }i
~~~

Một hệ quả quan trọng là validity của mô hình có thể **phụ thuộc vào từng đầu ra**.

Ví dụ, cùng một điểm vận hành có thể:

~~~text
VALID đối với độ võng
INVALID đối với tải chuyển trạng thái trượt
~~~

Do đó luận văn không nên nói về một biên hiệu lực duy nhất cho mọi đại lượng, trừ khi bằng chứng thực sự hỗ trợ kết luận đó.

---

# 11. Cấp bậc validation dự kiến

~~~text
Cấp 1
Tái tạo các kết quả phân tích của M1

        ↓

Cấp 2
Xác minh phần triển khai bằng các case đã công bố của M1

        ↓

Cấp 3
Xây dựng và xác minh mô hình FE full-layer tường minh R

        ↓

Cấp 4
Tạo các model-form error map:
M1 so với R

        ↓

Cấp 5
Chọn trước các điểm thí nghiệm ở cả hai phía
của biên validity/breakdown dự đoán

        ↓

Cấp 6
Thực hiện thí nghiệm vật lý

        ↓

Cấp 7
Đánh giá xem biên dự đoán có còn tồn tại
sau kiểm chứng thực nghiệm hay không
~~~

Thí nghiệm **không** nên chỉ kiểm tra một vài điểm thuận tiện mà mô hình đã có vẻ chính xác.

Ít nhất một phần các điểm thí nghiệm phải chủ động kiểm tra:

~~~text
vùng dự đoán VALID
VÀ
vùng dự đoán INVALID
~~~

---

# 12. Kiến trúc luận văn hiện tại dưới dạng một sơ đồ

~~~text
KHÔNG GIAN ĐẦU VÀO
n, p, mức độ uốn, hình học, μ, điều kiện biên
        │
        ├─────────────────────────────┐
        │                             │
        ▼                             ▼
M1: mô hình continuum Zhang     R: mô hình FE full-layer
        │                             │
        ▼                             ▼
     dự đoán                    đầu ra tham chiếu
        │                             │
        └──────────────┬──────────────┘
                       ▼
                 CHỈ SỐ SAI SỐ
                ew, eK, eQ, ...
                       │
                       ▼
           TOLERANCE ĐỊNH TRƯỚC
             εw, εK, εQ, ...
                       │
                       ▼
              BẢN ĐỒ VALID / INVALID
                       │
                       ▼
               THÍ NGHIỆM VẬT LÝ
          ở cả hai phía của biên
                       │
                       ▼
      VALIDITY MAP ĐƯỢC KIỂM CHỨNG
               BẰNG THỰC NGHIỆM
~~~

---

# 13. Các mục đã khóa và còn tạm thời

## Đã khóa

~~~text
HƯỚNG NGHIÊN CỨU =
giới hạn hiệu lực của mô hình dầm vacuum layer-jamming

MÔ HÌNH RÚT GỌN M =
mô hình continuum beam của Zhang và cộng sự
DOI 10.5194/ms-16-821-2025

ĐỐI TƯỢNG NGHIÊN CỨU CHUNG =
các biên validity/breakdown của M1
~~~

## Tạm thời — vẫn phải khóa tiếp

~~~text
MÔ HÌNH THAM CHIẾU CHÍNH R =
mô hình FE full-layer với tiếp xúc tường minh
(formulation chính xác chưa khóa)

MÔ HÌNH THAM CHIẾU PHỤ =
Caruso 2023 — cơ học rời rạc

ĐẦU RA CHÍNH =
1. độ võng
2. độ cứng uốn
3. tải chuyển trạng thái trượt

BIẾN BREAKDOWN CHÍNH =
1. số lớp
2. áp suất chân không
3. mức độ uốn

CÂU HỎI NGHIÊN CỨU =
mới ở phiên bản làm việc

GIẢ THUYẾT =
mới ở phiên bản làm việc

NGƯỠNG SAI SỐ =
chưa xác định
~~~

---

# 14. Các nhiệm vụ tiếp theo ngay lập tức

Công việc tiếp theo nên thực hiện theo thứ tự:

1. **Tái dựng M1 hoàn chỉnh**
   - mọi phương trình chi phối;
   - mọi state/variable;
   - toàn bộ giả định;
   - mọi chế độ tải;
   - thuật toán số/incremental;
   - các case validation đã công bố.

2. **Khóa mô hình tham chiếu R chính xác**
   - phần mềm / solver;
   - số chiều;
   - loại phần tử;
   - cách biểu diễn từng lớp;
   - formulation tiếp xúc;
   - luật ma sát;
   - cách áp dụng áp suất;
   - điều kiện biên;
   - protocol hội tụ lưới.

3. **Khóa các đầu ra chính**
   - xác nhận \(w\), \(K\) và tải chuyển trạng thái trượt đều có thể trích xuất từ cả M và R.

4. **Khóa không gian tham số**
   - xác định các giá trị/phạm vi ứng viên cho \(n\), \(p\) và mức độ uốn.

5. **Xác định chỉ số sai số và tolerance**
   - trước khi chạy validation cuối cùng.

6. **Chỉ sau đó mới bắt đầu tạo validity map cuối cùng.**

---

# 15. Hệ quả đối với kế hoạch học 80/20

Vì M1 đã được chọn, việc học kiến thức nền phải được dẫn dắt bởi chính các phương trình và nhu cầu triển khai M1.

Chuỗi kiến thức 80/20 đầu tiên dự kiến là:

~~~text
Cơ học dầm Euler–Bernoulli
        ↓
mô men uốn / lực cắt / độ cong
        ↓
phân bố ứng suất cắt trên tiết diện
        ↓
ma sát Coulomb
        ↓
stick / partial slip / full slip
        ↓
xấp xỉ continuum cho dầm nhiều lớp
        ↓
nghiệm dầm phi tuyến theo từng bước tải
        ↓
cơ học tiếp xúc cần cho mô hình tham chiếu R
        ↓
validation bằng phần tử hữu hạn
~~~

**Không** học toàn bộ các lĩnh vực continuum mechanics, FEM, contact mechanics hoặc soft robotics trước khi tái dựng M1.

Chỉ học từng khái niệm khi nó cần thiết để hiểu, triển khai, phản biện hoặc kiểm chứng một phần cụ thể của mô hình đã chọn.

---

# 16. Nguồn gốc bằng chứng

Kiến trúc này được xây dựng dựa trên trạng thái hiện tại của repository, đặc biệt là:

- docs/research_design/EXACT_MODEL_SELECTION.md
- data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json
- data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json
- docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md
- outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json

### Phân biệt giữa bằng chứng và suy luận

- Các phát biểu về những gì M1 có thể dự đoán, cơ học chi phối, giả định, các so sánh số đã có và các thí nghiệm trước đây được rút ra từ bằng chứng đã xác minh trong repository.
- Việc chọn các đầu ra chính, biến breakdown chính, kiến trúc mô hình tham chiếu, giả thuyết và cấp bậc validation là **quyết định thiết kế nghiên cứu / tổng hợp**, không phải kết luận do Zhang và cộng sự đưa ra.
- Formulation chính xác của mô hình FE tham chiếu, các giá trị tolerance, thiết kế thí nghiệm và phạm vi tham số cuối cùng vẫn chưa được giải quyết và không được trình bày như những sự thật đã được xác minh.
