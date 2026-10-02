# D1: Từ 54 paper đến tìm kiếm tài liệu phản bác

> **Ngày ghi chép:** 26/09/2026.  
> **Phạm vi:** Lưu lại phần giải thích trong hội thoại về quá trình hình thành D1 và các nhóm truy vấn tìm prior art. Đây không phải adjudication novelty mới. Các trạng thái hiện tại bên dưới phản ánh lần kiểm tra repository ngày 26/09/2026.

Từ **54 paper**, quy trình đi theo chuỗi: **đề xuất các câu hỏi nghiên cứu → phản biện từng câu hỏi → chọn D1 có điều kiện → tìm những công trình có thể đã trả lời D1 → thu hẹp hoặc đổi câu hỏi theo bằng chứng**.

Điểm cần phân biệt là: 54 paper ban đầu dùng để **sinh giả thuyết nghiên cứu**. Chúng chưa đủ để kết luận một hướng có tính mới.

## 1. Từ 54 paper, repository đã đề xuất năm hướng

Các paper được trích xuất evidence, tổng hợp qua các batch, rồi hình thành năm candidate sau:

| Hướng | Nội dung được đề xuất ban đầu | Câu hỏi cơ học chính |
|---|---|---|
| **D1** | Ma sát, biến dạng vênh và suy giảm độ cứng theo chu kỳ trong layer-jamming chân không | Áp suất, số lớp và số chu kỳ ảnh hưởng thế nào tới ma sát, trượt, độ cứng và hysteresis? |
| **D2** | Cơ học layer-jamming dùng áp suất dương dưới tải uốn | Áp suất bơm, số lớp và độ mềm của khung quyết định độ cứng và tải bắt đầu trượt thế nào? |
| **D3** | Làm mát cưỡng bức cho ngón tay mềm biến đổi độ cứng bằng chuyển pha | Lưu lượng làm mát và hình học kênh ảnh hưởng thế nào tới nhiệt độ, thời gian phục hồi độ cứng và độ cong? |
| **D4** | Tương tác màng–hạt và ma sát bề mặt trong granular-jamming gripper | Tỷ lệ chiều dày màng/kích thước hạt ảnh hưởng thế nào tới độ gợn bề mặt, ma sát và lực giữ? |
| **D5** | Mô hình biến dạng cắt cho actuator composite có ứng suất trước và gân | Bổ sung biến dạng cắt có cải thiện dự đoán độ cong, độ cứng và lực đầu ngón so với mô hình cũ không? |

Cả năm đều được ghi nhận là **`novelty_confidence = unverified`**. Thứ tự xếp hạng ban đầu là D1 → D2 → D3 → D4 → D5. [Nguồn: candidate directions](../../outputs/discovery_snapshot/candidate_directions.json).

## 2. Phản biện nội bộ giữ D1 và D2 để xét tiếp

Critic đề nghị:

- **D1: revise** — bỏ các claim quá rộng về wear dài hạn, fatigue và đo warping bên trong envelope.
- **D2: revise** — nghi ngờ việc giải thích saturation độ cứng có đủ đóng góp khoa học hay không.
- **D3–D5: reject trong vòng lựa chọn này** — vì các lo ngại về trùng lặp, phạm vi, mô hình hoặc khả năng thực nghiệm.

Đây là **đánh giá của vòng discovery**, không phải kết luận đã kiểm chứng toàn bộ literature rằng D3–D5 không thể nghiên cứu.

Sau adjudication, D1 được chọn với confidence `medium`, dưới tên:

> **Modeling and Experimental Characterization of Interlayer Slip and Bending Stiffness in Vacuum Layer-Jamming Beams**

Tức là D1 đã thu hẹp từ “ma sát + warping + suy giảm theo chu kỳ” xuống **trượt giữa các lớp và đáp ứng uốn**. [Nguồn: final discovery adjudication](../../outputs/discovery_snapshot/final_adjudication.json).

## 3. Bước tìm tài liệu bác bỏ đầu tiên: đã có người mô hình hóa pressure–slip–stiffness chưa?

Claim cần tấn công lúc này là:

> Có thể còn khoảng trống trong mô hình dự đoán quan hệ áp suất chân không → ma sát → trượt giữa các lớp → độ cứng uốn, kèm thực nghiệm.

Nhóm từ khóa tương ứng:

```text
("layer jamming" OR "laminar jamming")
AND ("partial interaction" OR "shear lag" OR "interlayer slip" OR "beam model")
```

Các truy vấn ngắn bổ sung:

```text
"layer jamming beam" model
"layer jamming beam" slip
"layer jamming" "partial slip"
"layer jamming" "progressive slip"
"layer jamming" hysteresis
```

**Vì sao tìm như vậy?** Nếu một paper đã có mô hình trượt, dự đoán stiffness và kiểm chứng bằng thí nghiệm, thì phần cốt lõi của D1 có thể đã được giải quyết.

D1-V001 kiểm tra toàn văn Narang 2018, Caruso 2023 và Atakuru 2024. Kết luận là:

> **`PIVOT`, confidence `high`.**

Narang và Caruso đã bao phủ nhiều nội dung mà D1 định làm: pressure–friction–slip, các giai đoạn trượt, đáp ứng lực–độ võng và experimental validation. Vì vậy, chỉ làm lại với vật liệu khác, thêm mức áp suất hoặc thêm phép đo không đủ bảo vệ claim ban đầu. [Nguồn: D1-V001](../../outputs/verification/D1-V001/direction_verification.json).

## 4. Sau khi D1 ban đầu bị bác bỏ, câu hỏi chuyển sang continuum và giới hạn hiệu lực

Pivot tạm thời mang tên:

> **Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams**

Lúc này phải tìm để bác bỏ hai khả năng:

1. Mô hình continuum/homogenized cho layer-jamming **đã tồn tại chưa**?
2. Người ta **đã xác định giới hạn chính xác của nó chưa**?

Nhóm từ khóa thứ hai:

```text
"layer jamming" "continuum model"
"layer jamming" homogenization
"layer jamming" "equivalent model"
"layer jamming" "reduced-order model"
"layer jamming" constitutive model
"laminar jamming" continuum
"layer jamming" "high layer count"
```

Repository còn yêu cầu truy **forward citations** của hai nguồn nền:

```text
Narang 2018: 10.1002/adfm.201707136
Caruso 2023: 10.1016/j.ijmecsci.2023.108325
```

Forward citation nghĩa là xem **những bài xuất bản sau đã trích dẫn paper nền và phát triển tiếp điều gì**. Nó giúp tìm hậu duệ trực tiếp mà truy vấn từ khóa có thể bỏ sót.

Các vòng sau đã đưa vào những đe dọa quan trọng:

- Zhang — *A continuum-based model for a layer jamming beam*.
- Zhang — *Toward a deeper understanding of layer jamming structures*.
- Zhang — *Continuum modeling for layer jamming structures*.
- Fan — *Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots*.

Hệ quả: **“xây dựng continuum model cho layer-jamming” không còn là claim để bảo vệ.** Câu hỏi phải chuyển sang đánh giá giới hạn của một mô hình đã có. [Chiến lược tìm kiếm](../literature/LITERATURE_STRATEGY.md).

## 5. Tiếp tục tìm để bác bỏ: giới hạn của mô hình đã được nghiên cứu chưa?

Khi continuum đã tồn tại, truy vấn phải chuyển từ “có mô hình không?” sang “mô hình đúng đến đâu?”:

```text
"layer jamming" "model validity"
"layer jamming" "model limitation"
"layer jamming" "large deformation"
"layer jamming" boundary effects
"layer jamming" contact pressure
```

Đồng thời truy citation của ba DOI Zhang:

```text
10.5194/ms-16-821-2025
10.1007/s11465-025-0843-5
10.1016/j.taml.2025.100633
```

Khi đọc paper, cần phân biệt:

| Paper thể hiện điều gì? | Ý nghĩa với D1 |
|---|---|
| Có continuum model | Bác bỏ claim “mô hình continuum chưa tồn tại” |
| Mô hình khớp vài thí nghiệm | Cho thấy đã có validation ở những điều kiện đó |
| Sai số tăng khi thay số lớp hoặc tải | Đã có bằng chứng về giới hạn hoặc xu hướng sai số |
| Xác định miền đạt/không đạt theo tiêu chí sai số, kiểm tra bằng reference và experiment | Đe dọa trực tiếp câu hỏi validity/breakdown hiện tại |

Không được coi ba hàng đầu tự động chứng minh hàng cuối. Nhưng cũng không được bỏ qua chúng chỉ vì paper không dùng chữ “validity domain”.

## 6. Vì sao phải tìm sang cơ học lân cận?

Một bài về **composite beams, laminated beams hoặc flexible pipes** có thể đã giải quyết cùng bài toán cơ học, dù không gọi hệ đó là “layer jamming”.

Do đó D1-V004–V009 mở rộng sang các nhóm sau:

| Nhóm cần kiểm tra | Truy vấn tiêu biểu | Nội dung có thể bác bỏ D1 |
|---|---|---|
| Partial interaction | `"partial interaction" "multilayer beam" "interlayer slip"` | Quy luật chuyển từ các lớp trượt riêng sang làm việc liên hợp |
| Laminated beams | `"laminated beam" "imperfect interface" bending` | Mô hình rút gọn có interface không hoàn hảo |
| Frictional layered beams | `"frictional layered beam" continuum error` | So sánh continuum với các lớp có ma sát |
| Multi-leaf springs | `"multi-leaf spring" "interleaf friction" model` | Trượt tiến triển, hysteresis và mô hình tương đương của chồng lá |
| Shear-lag | `"shear lag" "imperfect interface" "error estimate"` | Chiều dài truyền lực và điều kiện mô hình xấp xỉ đủ chính xác |
| Homogenization | `"layered beam" homogenization "Coulomb friction"` | Cơ sở chuyển từ interface rời rạc sang continuum |
| Discrete-to-continuum | `"multilayer beam" "continuum limit" "convergence rate"` | Sai số hoặc điều kiện hội tụ theo số lớp |
| Contact và pressure | `"layered" "contact pressure" friction "reduced model"` | Pressure redistribution và giới hạn của giả định contact |
| Generalized continuum | `"layered" Cosserat friction bending` | Những cơ chế layered-continuum đã tồn tại từ trước |

Sau lượt tìm theo **cơ chế**, protocol bổ sung các từ khóa đánh giá:

```text
"prediction error"
"error bound"
"range of validity"
"applicability"
"validity domain"
"breakdown"
tolerance
convergence
```

Không ghép tất cả vào một truy vấn ngay từ đầu, vì sẽ dễ bỏ sót paper quan trọng. [Nguồn: validity-gap search protocol](../protocols/D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md).

Các audit này gặp những tiền nhiệm mạnh như Faella về tiêu chí bỏ qua partial interaction, Wang `ca46dc062d` về continuum–discrete error/applicability boundary, và Adhikary về Cosserat continuum có slip/opening. Vì thế, ngay cả **“so sánh hai mô hình rồi đặt ngưỡng sai số” cũng không được mặc định là mới**.

## 7. Qua từng lượt bác bỏ, D1 hiện đã thu hẹp thành gì?

Chuỗi chuyển hướng có thể đọc như sau:

```text
54 paper → 5 candidate

D1: friction + warping + cyclic degradation
        ↓ phản biện phạm vi và khả năng nhận diện
D1: interlayer slip + bending stiffness
        ↓ Narang / Caruso đã bao phủ phần lớn
P1: continuum/homogenized model và validity limits
        ↓ Zhang đã có continuum và validation
Đánh giá validity/breakdown của một mô hình cụ thể
        ↓ cơ học lân cận đã có error criteria và applicability studies
M1 cụ thể + reference R đáng tin cậy + experiment độc lập
→ kiểm tra miền chính xác theo từng đầu ra
→ giải thích sai lệch bằng contact/slip mechanics
```

## 8. Ngay lúc này, bước tìm tài liệu tiếp theo là gì?

Hiện không cần quay lại tìm rộng với “soft robot variable stiffness”. W10 đã xác định một nguồn cụ thể còn thiếu full-text audit:

```text
10.1016/j.matdes.2026.116573
```

Việc cần làm là lấy đúng full text và kiểm tra xem paper này đã thực hiện phần nào của **model → reference → experiment → error/breakdown assessment**. Metadata và abstract hiện chưa đủ để đóng đe dọa đó. [Unresolved threat register](../../outputs/d1_execution/V4/W10/D1_UNRESOLVED_THREAT_REGISTER.json).

Các chuỗi tìm ở trên lấy từ chiến lược và protocol trong repository. **Một query được ghi trong kế hoạch không tự chứng minh nó đã được chạy**, và chưa thể gán mỗi paper cho một query cụ thể nếu thiếu raw export/search provenance. Đó cũng là phần workflow tái dựng lịch sử đang phải kiểm tra.
