# Hướng dẫn đọc ba bài Zhang về continuum layer jamming

## 1. Mục tiêu

Tài liệu này giúp đọc và phân biệt ba bài của Zhang và cộng sự đang có trong thư mục Google Drive của dự án. Mục tiêu trước mắt không phải là thuộc mọi phương trình, mà là xác định:

1. mỗi bài giải quyết câu hỏi nào;
2. mô hình hoạt động ở cấp độ nào;
3. đầu vào, đầu ra và giả thiết chính là gì;
4. bài nào là mô hình M1 được chọn cho luận văn;
5. những phần nào cần đọc kỹ để tái dựng M1;
6. những phần nào chỉ cần đọc chọn lọc để hiểu bối cảnh và tránh nhầm mô hình.

## 2. Trạng thái bằng chứng và nguồn

Ba nguồn dưới đây đều đã được truy cập ở dạng toàn văn PDF. Các mô tả nội dung trong tài liệu này được đánh dấu là `VERIFIED FULL TEXT` khi dựa trực tiếp trên toàn văn hoặc evidence extraction đã lưu trong repository.

| Nhãn trong hướng dẫn | Bài báo | DOI | Vai trò |
|---|---|---|---|
| **Bài A / M1** | Zhang et al., *A continuum-based model for a layer jamming beam* | `10.5194/ms-16-821-2025` | Mô hình dầm liên tục được chọn làm mô hình rút gọn M1 của luận văn |
| **Bài B** | Zhang et al., *Toward a deeper understanding of layer jamming structures* | `10.1007/s11465-025-0843-5` | Mô hình cơ học dầm mở rộng cho dầm thẳng/cong, biến dạng lớn và tải chu kỳ |
| **Bài C / M2** | Zhang et al., *Continuum modeling for layer jamming structures* | `10.1016/j.taml.2025.100633` | Mô hình cấu thành elastoplastic continuum dựa trên RVE và average-field; không phải M1 |

Lưu ý năm xuất bản của Bài C: DOI và ngày online thuộc năm 2025, nhưng số tạp chí là *Theoretical and Applied Mechanics Letters* 16 (2026), article 100633. Khi trích dẫn phải lấy năm theo định dạng thư mục chính thức của tạp chí hoặc cơ sở dữ liệu được chọn, không suy ra chỉ từ tên file.

Nguồn Drive:

- [Bài A / M1](https://drive.google.com/file/d/1tfjVt88P9XpIvDNxqSBXbDBiRdOxQyBG/view)
- [Bài B](https://drive.google.com/file/d/1Syg5aERCz9NYxCRGydoadhyaALATqWyY/view)
- [Bài C / M2](https://drive.google.com/file/d/1hGfNmu79ayVjU9ppG7q3sgTogPtf0P6j/view)

Evidence files trong repository:

- `data/evidence/2025-A continuum-based model for a layer jamming beam_95646b2cfc.json`
- `data/evidence/2025-Toward a deeper understanding of layer jamming structures_7cb387b88d.json`
- `data/evidence/2025-Continuum modeling for layer jamming structures_a792efc445.json`

## 3. Bản đồ khái niệm của ba bài

```text
Bài A / M1 — cấp kết cấu dầm
{p, mu, hình học dầm, tải}
→ trường ứng suất + vùng jammed/slipping
→ lực/moment nội + độ võng dầm

Bài B — cấp kết cấu dầm mở rộng
{p, mu, chiều dày lớp, hình học thẳng/cong, lịch sử tải}
→ ứng suất và gia số ứng suất
→ trượt tiến triển + độ cứng + biến dạng lớn + hysteresis

Bài C / M2 — cấp vật liệu/RVE
{trạng thái ứng suất/biến dạng vĩ mô, p, mu, tính chất lớp}
→ quan hệ cấu thành elastoplastic + yield/slip surface
→ ứng suất, trượt dẻo và năng lượng tiêu tán
→ cần được nhúng vào một structural solver nếu muốn dự đoán cả dầm
```

Sai lầm cần tránh:

```text
M1 != M2
```

M1 là mô hình kết cấu dầm. M2 là mô hình cấu thành vật liệu tương đương. Hai bài sử dụng ngôn ngữ continuum và elastoplastic giống nhau nhưng không thể thay thế trực tiếp cho nhau.

## 4. Tóm tắt Bài A — mô hình M1

### 4.1 Câu hỏi của bài

`VERIFIED FULL TEXT`

Bài A hỏi liệu một chồng nhiều lớp mỏng có thể được thay bằng một môi trường liên tục để mô tả ứng suất, trạng thái trượt và biến dạng của dầm layer-jamming hay không. Xấp xỉ trung tâm là cho chiều dày mỗi lớp tiến tới nhỏ so với tổng chiều cao dầm, trong khi số lớp trở nên lớn và các trường cơ học theo chiều cao được xem là liên tục.

### 4.2 Nội dung cơ học chính

`VERIFIED FULL TEXT`

- Mô hình dựa trên cơ học dầm kiểu Euler–Bernoulli và trạng thái ứng suất phẳng.
- Khả năng chống trượt được lý tưởng hóa bằng ma sát Coulomb với giới hạn liên quan đến `mu p`.
- Tiết diện được phân loại thành full jamming, half/partial slipping và full slipping.
- Mô hình dự đoán phân bố ứng suất trượt, ứng suất dọc, biên vùng jammed/slipping, các ngưỡng lực cắt và đáp ứng tải–độ võng.
- Một công thức cốt lõi cho ứng suất trượt trong trạng thái chưa trượt có dạng

  ```math
  \tau(y,Q)=\frac{3}{2}\frac{Q}{A}\left(1-\frac{4y^2}{h^2}\right).
  ```

- Điều kiện bắt đầu chạm giới hạn ma sát được lý tưởng hóa bởi

  ```math
  |\tau|=\mu p,
  ```

  dẫn đến ngưỡng lực cắt bắt đầu trượt được báo cáo là

  ```math
  Q_{\mathrm{slip}}=\frac{2}{3}\mu p A.
  ```

### 4.3 Kiểm chứng mà bài đã thực hiện

`VERIFIED FULL TEXT`

- So sánh trường ứng suất với FEA hữu hạn lớp cho các cấu hình 10 và 25 lớp.
- Thí nghiệm tải–độ võng trên dầm công-xôn PVC 20 lớp ở áp suất 60 kPa.
- Kết quả cho thấy phù hợp tốt ở các trường hợp được kiểm tra, đặc biệt đối với đáp ứng toàn cục, vùng xa biên ràng buộc và điều kiện partial slip.

### 4.4 Giới hạn quan trọng

`VERIFIED FULL TEXT`

- Bỏ qua ứng suất pháp liên lớp do biến dạng sinh ra trong mô hình giải tích.
- Không biểu diễn chính xác hiệu ứng gần đầu tự do và gần ràng buộc.
- Có sai khác lớn hơn khi tải cực đoan dẫn đến full slip.
- Giả định continuum làm mất tính rời rạc của từng lớp/interface.
- Ma sát Coulomb dùng hệ số không đổi.

`INTERPRETATION`

Phát biểu rằng continuum có hiệu quả với khoảng `n >= 10` xuất phát từ các trường hợp FEA cụ thể của bài. Không được biến nó thành quy luật phổ quát cho mọi vật liệu, hình học, áp suất, điều kiện biên và đại lượng đầu ra. Đây chính là một trong các điểm cần kiểm tra trong luận văn.

### 4.5 Vai trò đối với luận văn

Đây là bài phải đọc sâu nhất vì nó định nghĩa M1. Sau quá trình đọc, người nghiên cứu phải có khả năng tự giải thích và triển khai chuỗi:

```text
giả định continuum
→ cân bằng dầm và trường ứng suất
→ điều kiện Coulomb
→ biên vùng trượt
→ nội lực/moment
→ độ cong và độ võng
→ so sánh với R và E
```

## 5. Tóm tắt Bài B — cơ học dầm mở rộng

### 5.1 Câu hỏi của bài

`VERIFIED FULL TEXT`

Bài B phát triển một mô hình cơ học cho beam-stack LJS nhằm mô tả trượt tiến triển, biến dạng của dầm thẳng và dầm cong, ảnh hưởng của áp suất và chiều dày lớp, cùng đáp ứng dưới tải chu kỳ.

### 5.2 Nội dung chính

`VERIFIED FULL TEXT`

- Phân tích phân bố ứng suất và gia số ứng suất trong quá trình uốn.
- Sử dụng biên vùng trượt liên tục để mô tả full jamming, half jamming/partial slip và full sliding.
- Xây dựng phương trình chi phối biến dạng và thuật toán gia tăng để xử lý biến dạng lớn và lịch sử tải không đơn điệu.
- Xây dựng moment quán tính tương đương thay đổi khi vùng trượt phát triển.
- Mô tả năng lượng tiêu tán do ma sát thông qua vòng trễ tải–độ võng.

### 5.3 Kiểm chứng

`VERIFIED FULL TEXT`

- Thí nghiệm dầm thẳng và dầm cong.
- Các mức áp suất được báo cáo gồm 40, 70 và 100 kPa.
- Các chiều dày lớp được kiểm tra gồm 0.3, 0.5 và 1.0 mm.
- Có tải đơn điệu và tải chu kỳ; thí nghiệm chu kỳ được dùng để quan sát hysteresis.

### 5.4 Kết quả và giới hạn đáng chú ý

`VERIFIED FULL TEXT`

- Tải bắt đầu trượt tăng theo áp suất giữ.
- Chiều dày lớp có ít ảnh hưởng lên độ cứng ban đầu trước trượt nhưng ảnh hưởng đáng kể lên độ cứng sau khi trượt phát triển.
- Dầm cong có thể giảm độ cứng trơn hơn dầm thẳng khi trượt tiến triển.
- Mô hình có xu hướng dự đoán quá cao tải tới hạn, nhất là ở áp suất thấp và lớp mỏng.
- Phân bố áp suất thực không hoàn toàn đồng đều do sai lệch chế tạo.
- Năng lượng tiêu tán lý thuyết nhỏ hơn kết quả thí nghiệm.
- Các tham số vật liệu/ma sát có phần được hiệu chỉnh từ đáp ứng mẫu, làm tăng nguy cơ lẫn giữa lỗi tham số và lỗi dạng mô hình.

### 5.5 Vai trò đối với luận văn

Bài B là nguồn quan trọng để:

- hiểu cơ học slip progression và thuật toán gia tăng;
- nhận diện các điều kiện có thể làm M1 hỏng;
- thiết kế các phép thử pressure/thickness/curvature/cyclic nếu sau này cần;
- tránh tuyên bố rằng các hiện tượng pressure-dependent slip, large deformation hoặc hysteresis chưa từng được mô hình hóa.

Bài B không thay đổi quyết định hiện tại rằng M1 của luận văn là Bài A.

## 6. Tóm tắt Bài C — mô hình cấu thành M2

### 6.1 Câu hỏi của bài

`VERIFIED FULL TEXT`

Bài C không bắt đầu từ phương trình cân bằng của một dầm cụ thể. Nó bắt đầu từ một representative volume element (RVE) gồm hai lớp và interface, sau đó dùng average-field để xây dựng quan hệ cấu thành continuum elastoplastic ở cấp vĩ mô.

### 6.2 Nội dung chính

`VERIFIED FULL TEXT`

- Xây dựng trường chuyển vị xấp xỉ bậc nhất trong RVE.
- Lấy trung bình thể tích và tích phân biên để liên hệ trường vi mô với ứng suất/biến dạng vĩ mô.
- Xây dựng yield/slip condition trong không gian ứng suất, phụ thuộc vào shear stress, normal squeezing stress, áp suất và hệ số ma sát.
- Mô tả jammed state như vùng đàn hồi và slipping state như đáp ứng elastoplastic có trượt dư.
- Dự đoán ứng suất vĩ mô, trượt dẻo, tangent stiffness và năng lượng tiêu tán.

### 6.3 Kiểm chứng

`VERIFIED FULL TEXT`

- Dùng mô hình FEA RVE 3D với periodic boundary conditions.
- Kiểm tra tải shear một phương, shear nhiều phương và tải ghép shear–normal.
- Có sai khác định lượng giữa lý thuyết và FEA về độ cứng shear đàn hồi, biên yield và năng lượng tiêu tán.
- Không có thí nghiệm vật lý trong bài; chính tác giả nêu nhu cầu kiểm chứng ở cấp kết cấu trong tương lai.

### 6.4 Vai trò đối với luận văn

M2 giúp hiểu:

- cách chuyển từ interface vi mô sang một luật vật liệu vĩ mô;
- ý nghĩa của elastoplastic analogy và yield surface;
- ảnh hưởng của tải ghép shear–normal;
- một hướng mô hình khác nếu sau này cần mở rộng khỏi dầm 2D.

M2 không trực tiếp cho quan hệ tải–độ võng của cả dầm. Muốn dùng M2 ở cấp kết cấu phải nhúng luật cấu thành vào một beam/shell/solid solver. Vì vậy không nên đọc các phương trình của M2 rồi ghép trực tiếp vào M1.

## 7. So sánh nhanh

| Tiêu chí | Bài A / M1 | Bài B | Bài C / M2 |
|---|---|---|---|
| Cấp mô hình | Kết cấu dầm | Kết cấu dầm mở rộng | Vật liệu/RVE |
| Hình học đích | Dầm layer-jamming | Dầm thẳng và cong | Cấu hình LJS tổng quát ở cấp constitutive |
| Cơ chế trượt | Biên jammed/slipping liên tục trên tiết diện | Trượt tiến triển và gia số ứng suất | Yield/slip surface trong không gian ứng suất |
| Đầu ra trực tiếp | Ứng suất, biên trượt, nội lực, độ võng | Độ cứng, biến dạng lớn, tải tới hạn, hysteresis | Stress update, tangent stiffness, plastic slip, energy density |
| FEA | Full-layer beam comparison | Beam FEA hỗ trợ xây dựng/kiểm tra cơ học | Periodic discrete-contact RVE |
| Thí nghiệm | Có, phạm vi hẹp | Có, nhiều điều kiện hơn | Không |
| Vai trò hiện tại | Mô hình M cần đánh giá | Companion mechanics/context | Mô hình thay thế ở cấp khác; không phải M1 |

## 8. Có cần đọc từng câu từng chữ không?

Không nên đọc tuyến tính từng câu ngay từ đầu. Cách đó dễ gây quá tải ký hiệu và không giúp phân biệt câu hỏi khoa học của từng bài. Nên đọc theo nhiều vòng.

### 8.1 Chiến lược tổng thể: đọc kết hợp, không đọc tuần tự từng bài

Không áp dụng cách:

```text
Bài A: Vòng 1 → 2 → 3 → 4 → 5
→ Bài B: Vòng 1 → 2 → 3 → 4 → 5
→ Bài C: Vòng 1 → 2 → 3 → 4 → 5
```

Thay vào đó, sử dụng chiến lược kết hợp:

```text
Giai đoạn 1
Vòng 1 cho cả Bài A, Bài B và Bài C
→ dựng bản đồ ba bài và tránh nhầm M1 với M2

Giai đoạn 2
Vòng 2 → Vòng 5 cho Bài A / M1
→ hiểu và tái dựng đầy đủ mô hình được chọn

Giai đoạn 3
Đọc chọn lọc Bài B
→ bổ sung cơ học biến dạng lớn, dầm cong, tải chu kỳ và các sai khác thực nghiệm

Giai đoạn 4
Đọc chọn lọc Bài C / M2
→ hiểu cấp constitutive/RVE; chưa tái dựng toàn bộ tensor nếu luận văn chưa cần
```

Lý do phải đọc Vòng 1 của cả ba bài trước là các bài dùng nhiều thuật ngữ giống nhau như continuum, elastoplastic, jamming và slipping nhưng hoạt động ở các cấp mô hình khác nhau. Nếu đọc sâu ngay một bài mà chưa có bản đồ chung, người đọc dễ ghép nhầm phương trình của mô hình dầm M1 với quan hệ cấu thành RVE của M2.

Mức độ đọc yêu cầu hiện tại:

| Bài | Vòng đọc yêu cầu | Độ sâu |
|---|---|---|
| Bài A / M1 | Đủ Vòng 1–5 | Đọc sâu; phải giải thích và tái dựng được mô hình |
| Bài B | Vòng 1, sau đó chọn lọc Vòng 2, 4 và 5 | Tập trung phần bổ sung hoặc đe dọa giả định M1; chỉ tái dựng phương trình thật sự liên quan |
| Bài C / M2 | Vòng 1–2 ở cấp khái niệm; Vòng 4–5 ở cấp giới hạn và vai trò | Hoãn tái dựng tensor/Vòng 3 đầy đủ trừ khi quyết định triển khai M2 |

### 8.2 Trình tự thực hiện cụ thể

#### Giai đoạn 1 — Vòng 1 cho cả ba bài

Đọc theo thứ tự:

```text
Bài A / M1
→ Bài B
→ Bài C / M2
```

Với mỗi bài, chỉ đọc abstract, hình đầu tiên và caption, đoạn cuối Introduction, tiêu đề các section và Conclusion. Sau đó viết đúng một câu:

```text
đầu vào → cấp/loại mô hình → đầu ra
```

Chỉ chuyển sang Giai đoạn 2 khi đã phân biệt được:

- Bài A là mô hình kết cấu dầm M1;
- Bài B là mô hình cơ học dầm mở rộng;
- Bài C là mô hình cấu thành continuum dựa trên RVE.

#### Giai đoạn 2 — Hoàn thành Vòng 2–5 cho M1

Thực hiện theo thứ tự:

```text
cơ chế vật lý và giả định
→ hệ tọa độ và ký hiệu
→ chuỗi phương trình cốt lõi
→ quan hệ tải–độ võng
→ FEA và thí nghiệm
→ giới hạn và cơ chế breakdown
```

Không chuyển sang công thức độ võng nếu chưa giải thích được chuỗi:

```text
tau(y,Q) → |tau| = mu p → Q_slip → y_s
```

#### Giai đoạn 3 — Đọc chọn lọc Bài B

Sau khi đã nắm M1, tập trung vào:

- stress increment;
- sliding-boundary approximation;
- equivalent moment of inertia;
- incremental algorithm;
- straight-versus-curved beams;
- pressure/thickness/cyclic experiments;
- các vị trí mô hình lệch thí nghiệm.

Không cần tái dựng mọi phương trình của Bài B. Chỉ đọc sâu phần giúp giải thích, mở rộng hoặc phản biện M1.

#### Giai đoạn 4 — Đọc chọn lọc Bài C / M2

Trước mắt chỉ cần trả lời được:

- RVE là gì?
- Average-field chuyển thông tin vi mô thành đại lượng vĩ mô như thế nào?
- Jamming và slipping được biểu diễn như elastic và plastic ra sao?
- Yield surface phụ thuộc shear và normal stress như thế nào?
- Vì sao M2 cần structural solver trước khi có thể dự đoán độ võng của dầm?

Chỉ thực hiện Vòng 3 đầy đủ và đọc sâu phép suy diễn tensor nếu nghiên cứu sau này thực sự triển khai M2 hoặc một constitutive solid model.

### Vòng 1 — Bản đồ bài báo, khoảng 15–25 phút mỗi bài

Chỉ đọc:

1. tiêu đề;
2. abstract;
3. hình đầu tiên và caption;
4. câu cuối Introduction nêu mục tiêu;
5. toàn bộ Conclusion;
6. lướt tiêu đề các section.

Sau vòng này, phải trả lời được bằng một câu:

> Bài này biến đầu vào nào thành đầu ra nào, bằng cấp mô hình nào?

### Vòng 2 — Logic vật lý, chưa sa vào biến đổi toán

Đọc kỹ:

- hình học và hệ tọa độ;
- cơ chế áp suất tạo lực ép;
- điều kiện ma sát Coulomb;
- định nghĩa jammed/partial/full slip;
- các giả định;
- luồng tính toán từ tải tới đáp ứng.

Ở vòng này, tạo một bảng ký hiệu nhưng chưa cần tự suy diễn mọi phương trình.

### Vòng 3 — Tái dựng toán học

Chỉ thực hiện sâu với Bài A trước. Với mỗi phương trình quan trọng, ghi:

1. phương trình đến từ cân bằng, quan hệ vật liệu hay giả định nào;
2. mỗi ký hiệu và đơn vị;
3. điều kiện áp dụng;
4. đầu vào và đầu ra;
5. phương trình trước đó cần dùng;
6. cơ chế nào bị bỏ qua;
7. cách kiểm tra dimension/unit;
8. cách kiểm tra limiting case.

Không chép phương trình một cách cơ học. Nếu chưa giải thích được bằng lời thì chưa được xem là đã hiểu.

### Vòng 4 — Đọc phần validation như một người phản biện

Với mỗi hình so sánh lý thuyết–FEA–thí nghiệm, hỏi:

- tham số nào đã được fit và tham số nào đo độc lập?
- đây là calibration hay validation?
- có bao nhiêu layer count, pressure và load case?
- sai số được báo cáo bằng metric nào?
- có uncertainty/error bar không?
- kết quả tốt ở một đại lượng có chứng minh tốt ở đại lượng khác không?
- những điểm gần biên, full slip hoặc pressure thấp có bị loại khỏi kết luận không?

### Vòng 5 — Đọc để phục vụ luận văn

Đánh dấu mỗi nội dung bằng một trong bốn nhãn:

- `USE`: cần dùng trực tiếp để triển khai M1;
- `CHECK`: cần kiểm chứng lại từ phương trình/hình;
- `LIMIT`: giả định hoặc giới hạn có thể gây breakdown;
- `NOT CORE`: thú vị nhưng chưa cần cho câu hỏi luận văn.

## 9. Thứ tự đọc được khuyến nghị

### Bước 1 — Đọc Bài A / M1 trước

Đây là bài bắt buộc đọc sâu. Thứ tự trong bài:

```text
Abstract và Conclusion
→ hình học, tọa độ và giả định continuum
→ ứng suất trượt và điều kiện Coulomb
→ ba trạng thái tiết diện và biên vùng trượt
→ cân bằng/nội lực/moment
→ quan hệ biến dạng và độ võng
→ FEA và thí nghiệm
→ limitations
```

Mục tiêu hoàn thành: tự vẽ được sơ đồ input–calculation–output của M1 và giải thích được tại sao `Q_slip` phụ thuộc vào `mu`, `p` và diện tích tiết diện.

### Bước 2 — Đọc chọn lọc Bài B

Không cần đọc lại từng câu của phần giới thiệu chung. Tập trung vào:

- stress increment;
- sliding-boundary approximation;
- equivalent moment of inertia;
- incremental algorithm;
- straight-versus-curved comparison;
- pressure/thickness/cyclic experiments;
- các chỗ lý thuyết và thí nghiệm lệch nhau.

### Bước 3 — Đọc Bài C sau cùng

Lần đầu chỉ cần hiểu:

- RVE là gì;
- average-field làm gì;
- jamming/slipping được diễn giải như elastic/plastic ra sao;
- yield surface phụ thuộc normal stress thế nào;
- tại sao mô hình này chưa trực tiếp tạo ra load–deflection curve của dầm.

Chỉ đọc kỹ toàn bộ phép suy diễn tensor khi luận văn thật sự cần triển khai M2 hoặc một constitutive solid model. Hiện tại đó không phải nhiệm vụ chính.

## 10. Mẫu ghi chú cho mỗi đoạn/phương trình

```text
Bài / DOI:
Trang và vị trí:
Nhãn: USE | CHECK | LIMIT | NOT CORE

Tác giả đang khẳng định gì?
Bằng chứng là: lý thuyết | FEA | thí nghiệm | suy luận

Phương trình/hình:
Ký hiệu và đơn vị:
Nguồn gốc vật lý/toán học:
Giả định cần để phương trình đúng:

Diễn giải bằng lời của tôi:
Điểm tôi chưa hiểu:
Nguy cơ đối với M1:
Liên hệ với R hoặc E:
```

Luôn tách rõ nội dung tác giả nói và suy luận cá nhân. Không tô màu một câu là “đúng” chỉ vì nó xuất hiện trong bài báo.

## 11. Kế hoạch đọc thực tế đầu tiên

### Phiên 1

- Đọc Vòng 1 của cả ba bài.
- Viết ba câu, mỗi bài một câu, theo mẫu “input → model → output”.
- Không xử lý tensor hoặc thuật toán gia tăng.

### Phiên 2

- Quay lại Bài A.
- Vẽ hệ tọa độ và tiết diện.
- Lập bảng ký hiệu `s, y, b, h, p, mu, N, Q, M, sigma, tau, y_s`.
- Giải thích bằng lời cơ chế full jamming → partial slip → full slip.

### Phiên 3

- Tái dựng chuỗi `tau(y,Q) → |tau| = mu p → Q_slip → y_s`.
- Kiểm tra đơn vị và limiting cases.
- Chưa chuyển sang công thức độ võng nếu chuỗi này chưa rõ.

### Phiên 4

- Đọc phần deformation/load–deflection của M1.
- Đọc lại các hình FEA và thí nghiệm như một người phản biện.
- Liệt kê ít nhất ba lý do khiến M1 và R có thể khác nhau.

### Phiên 5 trở đi

- Dùng Bài B để hiểu incremental/large-deformation/cyclic mechanics.
- Dùng Bài C để hiểu constitutive/RVE language khi đã nắm chắc M1.

## 12. Các guardrail khoa học

1. Ba bài đã có FEA và/hoặc thí nghiệm; không được viết rằng các mô hình chưa từng được kiểm chứng.
2. Khoảng trống còn sống là bản đồ validity/breakdown có hệ thống với tolerance theo từng output, không phải việc “kiểm chứng M1 lần đầu”.
3. `n >= 10` không phải quy luật phổ quát cho mọi bài toán.
4. R là tham chiếu có độ trung thực cao hơn, không phải chân lý.
5. Sai khác M1–R chưa tự động là model-form error của M1; phải loại trừ lỗi lưới, contact formulation, tham số và điều kiện biên của R.
6. Không trộn phương trình của M1 và M2 nếu chưa thiết lập ánh xạ cấp mô hình một cách rõ ràng.
7. Không mở rộng parameter space chỉ vì Bài B hoặc Bài C có thêm biến. Trọng tâm hiện tại vẫn là tái dựng M1.

## 13. Câu hỏi tự kiểm tra sau khi đọc vòng đầu

1. Vì sao M1 được gọi là continuum model dù hệ thật gồm các lớp rời rạc?
2. Biên `y_s` là biên vật lý giữa hai lớp hay một biên liên tục tương đương?
3. Áp suất `p` đi vào điều kiện bắt đầu trượt bằng cơ chế nào?
4. Tại sao kết quả tải–độ võng phù hợp không đủ để chứng minh trường ứng suất cục bộ đúng?
5. Bài B thêm điều gì mà M1 chưa tập trung xử lý?
6. Vì sao M2 không trực tiếp dự đoán độ võng của một dầm nếu chưa có structural solver?
7. Điều gì phải được chứng minh trước khi gọi R là “higher fidelity” cho một output cụ thể?

## 14. Kết luận thực hành

Không đọc cả ba bài từng câu từng chữ theo thứ tự từ trang 1 đến trang cuối. Đọc cả ba ở mức bản đồ trước, sau đó đọc sâu M1 theo cơ chế và chuỗi phương trình. Bài B được dùng để mở rộng và phản biện cơ học dầm; Bài C được dùng để hiểu cấp cấu thành/RVE và không phải ưu tiên triển khai hiện tại. Việc đọc chỉ hoàn thành khi người nghiên cứu có thể giải thích mô hình bằng lời, dựng lại chuỗi phương trình cốt lõi, chỉ ra giả định, và nói rõ loại bằng chứng nào hỗ trợ từng kết luận.
