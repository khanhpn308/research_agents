# M28 — Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes

- **Canonical PDF:** `data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf`
- **SHA-256:** `1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65`
- **Identity:** Narjabadifam et al., 2024; Buildings, Vol. 14, No. 6, 1567; DOI: `10.3390/buildings14061567`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C2.4; C2.4.1; C2.4.2; C2.5.5
- **Evidence records:** M28-E01; M28-E10; M28-E15; M28-E16

---

## A. Section objective

Đánh giá kết hợp thực nghiệm và mô phỏng số Abaqus về ứng xử cơ học của cáp thép tự chế tạo trong phòng thí nghiệm và mở rộng mô phỏng cho cáp hợp kim nhớ hình NiTi dưới tải trọng kéo chu kỳ và kích động động đất El Centro.

## B. Concept and terminology notes

Laboratory-made steel/NiTi ropes; Abaqus 3-D solid C3D8R elements; surface-to-surface hard contact; penalty friction ($\mu = 0.5$); kinematic coupling; cyclic tension; scaled El Centro seismic excitation; flag-shaped superelastic recovery.

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M28-E01 (p. 1, Abstract, NOT_APPLICABLE):** The paper compares laboratory steel-rope tests with ABAQUS models and numerically evaluates NiTi rope response under cyclic and El Centro excitation. Anchor: “validation of all numerical simulations is undertaken against the experimentally observed behaviors”. Status: `VERIFIED_FULL_TEXT`.
- **M28-E10 (p. 10, Sec. 2.3–2.4, Figs. 8–13):** 3-D C3D8R solid models with hard normal contact and penalty friction (mu=0.5) were used; end nodes are kinematically coupled to axial reference points. Anchor: “ABAQUS FE software”. Status: `VERIFIED_FULL_TEXT`.
- **M28-E15 (p. 15, Results, Figs. 17–19; Table 9):** Simulated SMA peak forces at 8 mm are about 365 N (single wire), 1.09 kN (1×3), 2.40 kN (1×7), 6.01 kN (1×19), 8.1 kN (1×27), and 14 kN (7×7); unloading recovers deformation. Anchor: “SMA peak tensile force at 8 mm displacement”. Status: `VERIFIED_FULL_TEXT`.
- **M28-E16 (p. 16, Results/Conclusions, Fig. 20; El Centro table):** Increasing the helix angle of SMA wire ropes results in reduced stress and increased strain under the scaled El Centro case. Anchor: “increasing the helix angle of SMA wire ropes”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Mô hình phần tử hữu hạn 3-D và thông số tiếp xúc pp. 9–13; Figs. 8–13 (lưới phần tử, điều kiện biên và so sánh thực nghiệm cáp thép); Figs. 17–19 và Table 9 (đáp ứng lực kéo chu kỳ của cáp NiTi từ 1x1 đến 7x7); Fig. 20 và bảng kết quả kích động El Centro; Tables 8–11.

## E. Experimental and quantitative findings

Thực nghiệm kéo chu kỳ và thử nghiệm bàn rung ở tần số 0.1 Hz cho các mẫu cáp thép tự bện; mô phỏng số cáp NiTi ở tần số 0.01 Hz với kích thước sợi đường kính 1.0 mm; kích động động đất El Centro (độ lớn 6.9, PGA điều chỉnh 0.281g và 0.6g).

Lực kéo đỉnh mô phỏng của cáp NiTi ở độ dịch chuyển 8 mm tăng dần theo quy mô cấu trúc: sợi đơn 365 N, 1×3 đạt 1.09 kN, 1×7 đạt 2.40 kN, 1×19 đạt 6.01 kN, 1×27 đạt 8.1 kN, và 7×7 đạt 14 kN [M28-E15]. Khi tăng góc xoắn của cáp NiTi, mức ứng suất thềm chuyển pha giảm đi và biến dạng thềm tăng lên dưới kích động El Centro [M28-E16].

## F. Cross-paper comparisons

- **So sánh với M25 (Vahidi et al. 2021) và M29 (Kang et al. 2020):**
  - Cả ba nghiên cứu đều xây dựng mô hình phần tử hữu hạn 3-D trong Abaqus cho cáp xoắn SMA. M28 sử dụng mô hình tiếp xúc phạt (penalty friction) với hệ số ma sát $\mu = 0.5$ đã được đối chiếu với thí nghiệm kéo cáp thép; trong khi M29 giả định không ma sát và M25 dùng UMAT Souza. Kết quả M28 khẳng định sự cần thiết của ma sát tiếp xúc để mô tả chính xác phản lực tổng thể.
- **So sánh với M36 (Carboni & Lacarbonara 2016):**
  - M36 thực hiện thử nghiệm bàn rung thực tế cho thiết bị giảm chấn uốn dùng cáp NiTi–thép; trong khi phần địa chấn và phản ứng động của cáp NiTi trong M28 chỉ dừng lại ở mô phỏng số thuần túy (chưa có thử nghiệm bàn rung thực tế cho mẫu NiTi).
- **So sánh với M23 (Zhang et al. 2021):**
  - M28 mô phỏng số chi tiết từng sợi 3-D (solid elements) với chi phí tính toán lớn cho cáp xoắn; M23 giải bài toán uốn giải tích nhanh và gọn bằng phương pháp dầm phân lớp tương đương cho bó dây song song.

## G. Limitations and counterevidence

1. **Ứng xử địa chấn của cáp NiTi chưa được kiểm chứng thực nghiệm [M28-E01]:** Toàn bộ số liệu về đáp ứng động lực học của cáp NiTi dưới kích động El Centro đều là kết quả mô phỏng phần mềm Abaqus, không có thí nghiệm bàn rung trực tiếp trên mẫu cáp NiTi vật lý.
2. **Kích động đơn lẻ [M28-E16]:** Chỉ sử dụng một sóng địa chấn El Centro duy nhất được co dãn biên độ, chưa đánh giá tính tổng quát với các phổ kích động khác nhau.
3. **Giả thiết góc xoắn đồng đều lý tưởng hóa:** Các mẫu cáp tự bện thủ công trong phòng thí nghiệm có độ bất đồng đều về góc xoắn và lực căng ban đầu giữa các sợi, gây trượt đầu kẹp trong một số thí nghiệm cáp thép.
4. **Không khảo sát tải uốn ngang:** Bài báo chỉ khảo sát tải kéo dọc trục thuần túy và dao động kéo dãn.

## H. Relevance to MP1

- **Thông số tiếp xúc ma sát tham khảo (C2.4, C2.4.1, C2.4.2, C2.5.5):** Cung cấp hệ số ma sát phạt $\mu = 0.5$ cho tiếp xúc giữa các sợi kim loại/NiTi trong Abaqus, là giá trị tham chiếu tin cậy nếu MP1 xây dựng mô hình FEA mô phỏng bó dây.
- **Quan hệ giữa lực và số lượng sợi (M28-E15):** Bằng chứng định lượng cho thấy lực phục hồi siêu đàn hồi tỷ lệ thuận gần như tuyến tính với số lượng sợi dây trong bó, nhưng hiệu suất trên mỗi sợi giảm nhẹ khi quy mô bó tăng do phân bố tải không hoàn toàn đồng đều giữa các lớp sợi.
- **Ranh giới công nghệ:** M28 nghiên cứu cáp xoắn chịu kéo; MP1 nghiên cứu bó dây thẳng chịu uốn dưới áp suất nén chủ động.

## I. Reading route

1. **Sec. 1 (pp. 1–3):** Nắm tổng quan về ứng dụng cáp hợp kim nhớ hình trong giảm chấn công trình.
2. **Sec. 2.1–2.2 (pp. 3–8):** Xem quy trình chế tạo mẫu cáp tự bện thủ công trong phòng thí nghiệm và thiết bị thử nghiệm kéo chu kỳ.
3. **Sec. 2.3–2.4 (pp. 8–13, Figs. 8–13):** Khảo sát phương pháp xây dựng mô hình phần tử hữu hạn 3-D Abaqus, định nghĩa tiếp xúc phạt $\mu = 0.5$ và liên kết kinematic coupling.
4. **Sec. 3.1 (pp. 13–15, Figs. 17–19, Table 9):** Đọc kỹ kết quả mô phỏng cáp NiTi từ 1x1 đến 7x7 và bảng thông số lực đỉnh.
5. **Sec. 3.2 & Sec. 4 (pp. 15–18, Fig. 20):** Khảo sát ảnh hưởng của góc xoắn cáp dưới kích động động đất El Centro và các kết luận chính.

## J. Questions for human writing

1. **Hiệu chỉnh thông số ma sát tiếp xúc (C2.4.2, C2.5):** Hệ số ma sát $\mu = 0.5$ được M28 hiệu chỉnh cho tiếp xúc giữa các sợi thép/NiTi có thể dùng làm giá trị xấp xỉ ban đầu cho ma sát tiếp xúc giữa các sợi TiNi trong MP1 hay không?
2. **Sự phân bố lực không đều giữa các sợi (C2.4.2):** Trong bó dây TiNi nhiều sợi của MP1, sự giảm nhẹ hiệu suất lực trên từng sợi khi tăng quy mô bó (như bảng Table 9 trong M28 chỉ ra) có ảnh hưởng như thế nào đến độ cứng uốn hiệu dụng?
3. **Mô phỏng 3-D so với mô hình giải tích (C2.5.5):** Khi nào luận văn cần xây dựng mô hình số 3-D chi tiết (kiểu M28) và khi nào mô hình dầm liên tục/dầm phân lớp (kiểu M23/M24) là đủ để dự báo đặc tính uốn của cơ cấu?

## K. Unresolved evidence

1. Dữ liệu siêu đàn hồi của cáp NiTi trong M28 hoàn toàn là số liệu mô phỏng phần mềm; cần cẩn trọng khi trích dẫn làm bằng chứng kiểm chứng độc lập.
2. Số trang in (`printed_page`) trong P0 là `NOT_REPORTED`; các định vị sử dụng số trang vật lý của file PDF 21 trang.
