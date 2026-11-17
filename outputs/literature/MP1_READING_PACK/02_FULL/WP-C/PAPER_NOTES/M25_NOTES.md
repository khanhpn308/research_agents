# M25 — Mechanical response of single and double-helix SMA wire ropes

- **Canonical PDF:** `data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf`
- **SHA-256:** `53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a`
- **Identity:** Vahidi, Arghavani, Choi, and Ostadrahimi, 2021; Mechanics Based Design of Structures and Machines; DOI: `10.1080/15376494.2021.1955313`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C2.4; C2.4.1; C2.4.2; C2.5; C2.5.5
- **Evidence records:** M25-E02; M25-E04; M25-E06; M25-E11

---

## A. Section objective

Mô phỏng phần tử hữu hạn 3-D ngầm định (implicit FE) trong Abaqus/UMAT cho cáp hợp kim nhớ hình (SMA) cấu trúc xoắn đơn 1×27 và xoắn kép 7×7; khảo sát đồng thời phi tuyến vật liệu chuyển pha siêu đàn hồi/hiệu ứng nhớ hình và phi tuyến tiếp xúc ma sát giữa các sợi; tối ưu hóa năng lượng riêng theo góc xoắn và đường kính dây.

## B. Concept and terminology notes

SMA superelasticity; shape memory effect (SME); single helix 1×27; double helix 7×7; UMAT; Souza–Auricchio model; Coulomb contact/friction; helix angle; normal/shear contact stress; reaction torque; response surface methodology.

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M25-E02 (p. 3, Introduction / model description, Fig. 1–3):** The study uses implicit Abaqus FE with a 3-D phenomenological SMA constitutive model and explicit interwire contact/friction for single- and double-helix ropes. Anchor: “Due to the convoluted geometry and interwire contact status within a cable”. Status: `VERIFIED_FULL_TEXT`.
- **M25-E04 (p. 4, Sec. 2–3, Fig. 3; Eqs. (1)–(6)):** Helix geometry and lay direction govern normal/shear stress and torque distributions; shear sign follows lay direction. Anchor: “helix angle”. Status: `VERIFIED_FULL_TEXT`.
- **M25-E06 (p. 6, Validation, Table/Figs. 5–10):** SMA rope simulations reproduce published experimental trends with average normal/shear stress deviations of about 20–25%. Anchor: “matching experimental stress-strain trends”. Status: `VERIFIED_FULL_TEXT`.
- **M25-E11 (p. 11, Optimization, Table 6; response surface):** The response-surface analysis reports higher specific energy for larger wire diameter and smaller helix angle. Anchor: “specific energy increases with larger wire diameter and smaller helix angle”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Mô hình cấu tạo SMA vi phân Souza–Auricchio và quan hệ hình học xoắn ốc pp. 3–6; Figs. 1–3 (sơ đồ mặt cắt và góc xoắn); Figs. 5–10 (đối chiếu ứng suất–biến dạng mô phỏng với thực nghiệm y văn); Figs. 11–14 và Tables 5–6 (tối ưu hóa năng lượng riêng).

## E. Experimental and quantitative findings

Không có thí nghiệm vật lý độc lập mới; mô hình số được kiểm chứng đối chiếu với dữ liệu thực nghiệm kéo cáp NiTi của Reedlunn et al. (2013) và Stanova et al. (2011) ở 25 °C siêu đàn hồi và phục hồi nhiệt nhớ hình.

Mô hình tái hiện tốt xu hướng định tính nhưng có độ lệch trung bình từ 20% đến 25% về mức ứng suất pháp tuyến và ứng suất cắt [M25-E06]. Tối ưu hóa bề mặt đáp ứng (32 ca tính toán FE) chỉ ra rằng năng lượng riêng đạt cực đại khi tăng đường kính sợi ($D = 0.38$ mm) và giảm góc xoắn ($\phi = 54.9^\circ$) [M25-E11].

## F. Cross-paper comparisons

- **So sánh với M26/M27 (Reedlunn et al. 2013):**
  - M26/M27 cung cấp bộ dữ liệu thực nghiệm kéo đẳng nhiệt của cáp NiTi 7×7 và 1×27; M25 sử dụng chính dữ liệu này để làm chuẩn kiểm chứng (benchmark) cho mô hình FE 3-D tiếp xúc có ma sát. Sự so sánh chứng minh rằng mô hình FE có thể tái hiện trình tự chuyển pha giữa các lớp nhưng sai số ứng suất 20–25% vẫn tồn tại do lý tưởng hóa điều kiện kẹp ngàm và bỏ qua bất đối xứng kéo–nén của vật liệu NiTi.
- **So sánh với M29 (Kang et al. 2020):**
  - Cả hai đều xây dựng UMAT trong Abaqus cho cáp SMA 7×7; tuy nhiên M25 đưa vào tương tác tiếp xúc mặt–mặt có ma sát Coulomb, trong khi M29 giả thiết tiếp xúc trơn không ma sát (frictionless). Việc so sánh làm rõ rằng bỏ qua ma sát (như M29) sẽ đánh giá thấp ứng suất danh nghĩa và độ cứng cáp.
- **So sánh với M23 (Zhang et al. 2021):**
  - M25 mô hình hóa cáp xoắn với áp suất tiếp xúc nội tại sinh ra từ lực căng kéo dọc trục làm xoắn siết các sợi; M23 mô hình hóa bó dây song song uốn tĩnh với lực tương tác giao diện tuyến tính.

## G. Limitations and counterevidence

1. **Sai số mô hình hóa 20–25% [M25-E06]:** Độ lệch đáng kể so với thực nghiệm phản ánh giới hạn của việc giả định ma sát Coulomb đồng nhất và bỏ qua biến dạng dập lõm cục bộ trong quá trình chế tạo.
2. **Chi phí tính toán mô phỏng phi tuyến 3-D lớn [M25-E02]:** Việc giải đồng thời phi tuyến chuyển pha SMA và bài toán tiếp xúc mặt–mặt trong Abaqus/Standard đòi hỏi tài nguyên tính toán rất cao, khó áp dụng cho bài toán điều khiển thời gian thực.
3. **Lý tưởng hóa ngàm xoay và điều kiện biên [M25-E04]:** Giả định ngàm cứng không quay, bỏ qua sự trượt tương đối tại đồ gá kẹp đầu cáp.
4. **Không có thí nghiệm vật lý mới:** Nghiên cứu thuần túy là mô phỏng số dựa trên dữ liệu công bố từ nguồn thứ ba.

## H. Relevance to MP1

- **Hiểu rõ tương tác giữa ma sát và chuyển pha siêu đàn hồi (C2.4, C2.4.1, C2.4.2, C2.5, C2.5.5):** M25 chứng minh rõ ràng rằng trong bó sợi NiTi, lực ma sát tiếp xúc làm thay đổi đáng kể mức ứng suất khởi đầu và kết thúc chuyển pha martensite.
- **Lợi thế của bó dây thẳng so với cáp xoắn:** Trong cáp xoắn (M25), lực kéo sinh ra mômen xoắn phản lực và ứng suất cắt không mong muốn; trong khi MP1 sử dụng bó dây thẳng song song, tiếp xúc ma sát được tạo ra chủ động bằng piston nén ngoài, tránh được hiện tượng tự xoắn phức tạp này.
- **Cơ sở tham khảo mô phỏng số:** Cung cấp thông số vật liệu Souza–Auricchio cho NiTi và kinh nghiệm thiết lập tiếp xúc penalty/Coulomb trong Abaqus nếu MP1 triển khai mô phỏng FEA.

## I. Reading route

1. **Sec. 1 & Sec. 2.1 (pp. 1–3):** Nắm bối cảnh mô hình hóa tiếp xúc đa sợi SMA và các phương trình cấu tạo Souza–Auricchio.
2. **Sec. 2.2–2.3 (pp. 3–4, Figs. 1–3):** Khảo sát cấu trúc hình học cáp 1×27 và 7×7, định nghĩa góc xoắn và thiết lập bài toán tiếp xúc mặt–mặt.
3. **Sec. 3 (pp. 4–6, Eqs. (1)–(6)):** Nắm quan hệ giữa góc xoắn, phân bố ứng suất pháp tuyến/cắt và mômen xoắn phản lực.
4. **Sec. 4 (pp. 6–9, Figs. 5–10):** Xem phân tích đối chiếu với dữ liệu thực nghiệm Reedlunn và phân tích nguyên nhân sai số 20–25%.
5. **Sec. 5 (pp. 10–12, Table 6):** Xem quy trình tối ưu hóa bề mặt đáp ứng cho năng lượng tiêu tán riêng.

## J. Questions for human writing

1. **Mô hình tiếp xúc giữa các sợi TiNi (C2.4.2, C2.5):** Khi mô phỏng số bó dây TiNi của MP1, có cần thiết phải sử dụng mô hình tiếp xúc mặt–mặt 3-D chi tiết như M25 hay có thể dùng mô hình dầm phân lớp tương đương (như M23) kết hợp ma sát Coulomb?
2. **Ảnh hưởng của chuyển pha lên lực ma sát (C2.4.1):** Sự thay đổi thể tích/mô đun đàn hồi khi TiNi chuyển từ austenite sang martensite có làm thay đổi đáng kể áp suất tiếp xúc danh nghĩa do piston tạo ra hay không?
3. **Độ tin cậy của mô phỏng số (C2.5.5):** M25 ghi nhận sai số 20–25% ngay cả khi dùng mô hình 3-D đầy đủ; điều này đặt ra yêu cầu kiểm chứng thực nghiệm độc lập như thế nào cho MP1?

## K. Unresolved evidence

1. Dữ liệu thực nghiệm kiểm chứng trong M25 là tải kéo dọc trục của cáp xoắn; chưa có số liệu kiểm chứng mô phỏng uốn cho bó dây SMA.
2. Số trang in (`printed_page`) trong P0 là `NOT_REPORTED`; các định vị sử dụng số trang vật lý của file PDF 13 trang.
