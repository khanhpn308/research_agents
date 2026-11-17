# M27 — Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses

- **Canonical PDF:** `data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf`
- **SHA-256:** `fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284`
- **Identity:** Reedlunn, Daly, and Shaw, 2013; International Journal of Solids and Structures, Vol. 50, pp. 3022–3044; DOI: `10.1016/j.ijsolstr.2013.03.015`
- **Extraction status:** `NEW_FULL_TEXT`
- **Mapped sections:** C2.4; C2.4.1; C2.4.2; C2.5.5
- **Evidence records:** M27-E02; M27-E08; M27-E13; M27-E24; M27-E16

---

## A. Section objective

Nghiên cứu thực nghiệm phân rã cấu trúc phân cấp (hierarchical subcomponents) của cáp siêu đàn hồi NiTi 7×7 và 1×27 dưới tải kéo chậm đẳng nhiệt; sử dụng đồng thời đo trường chuyển vị số (DIC), đo nhiệt độ hồng ngoại (IR), đo mômen phản lực và phương pháp trừ đáp ứng (response subtraction) để cô lập đóng góp cơ học và trình tự chuyển pha của từng lớp dây.

## B. Concept and terminology notes

7×7 right regular lay; 1×27 alternating lay; hierarchical subcomponents (core wire, 1×7, 1×19, full cable); transformation fronts; DIC/IR thermography; reaction torque; layer response subtraction; manufacturing indentations; distributed localization.

## C. Evidence with precise source locators

All claims below are `AUTHOR_RESULT` or `COUNTEREVIDENCE` and are anchored to the canonical PDF physical pages. The package records in `EVIDENCE_RECORDS.jsonl` carry the claim-level provenance.

- **M27-E02 (p. 2, Abstract, NOT_APPLICABLE):** Hierarchical subcomponents of 7×7 and 1×27 superelastic NiTi cables were tested; 7×7 components behave close to parallel wires, while 1×27 becomes more compliant with added layers. Anchor: “force-elongation responses of the core wire, 1×7 core strand and full 7×7 cable were similar”. Status: `VERIFIED_FULL_TEXT`.
- **M27-E08 (p. 8, Sec. 3, Figs. 2–4):** For 7×7 components, loading plateau stress decreases only slightly from about 517 MPa (core wire) to 506 MPa (1×7 strand); transformation fronts propagate. Anchor: “slight decrease in transformation force plateaus”. Status: `VERIFIED_FULL_TEXT`.
- **M27-E13 (p. 13, Sec. 4, Figs. 5–10):** Adding outer layers to 1×27 reduces secant modulus (about 23.7 to 7.3 GPa) and raises failure strain to roughly 40%; fronts are absent and localization is distributed around manufacturing indentations. Anchor: “no propagating transformation fronts”. Status: `VERIFIED_FULL_TEXT`.
- **M27-E24 (p. 24, Sec. 5, Figs. 13–20):** Subcomponent subtraction identifies layer contributions; R+→M+ initiation occurs at approximately 2.2% (layer B), 6.0% (C), and 8.8% (D). Anchor: “inner layers transform prior to outer layers”. Status: `VERIFIED_FULL_TEXT`.
- **M27-E16 (p. 16, Analytical comparison, Eq./Fig. 8–10):** Simple uniaxial predictions work for shallow-helix 1×7 but overpredict plateau stress for steeper 1×6 because local wire bending/twisting are omitted. Anchor: “local bending and twisting are omitted”. Status: `VERIFIED_FULL_TEXT`.

## D. Important equations and figures

Mô hình giải tích quan hệ góc xoắn–ứng suất thềm/mômen xoắn và kiểm tra số Biot đẳng nhiệt; Figs. 2–4 (đáp ứng kéo và ảnh nhiệt 7×7); Figs. 5–10 (đáp ứng kéo và vết lõm chế tạo SEM 1×27); Figs. 13–20 (kết quả phương pháp trừ tách lớp); Tables 1–4.

## E. Experimental and quantitative findings

Thí nghiệm kéo đơn trục kiểm soát chuyển vị chậm ở điều kiện gần đẳng nhiệt (18–22 °C, tốc độ biến dạng $10^{-5}$ s$^{-1}$ cho 7×7 và $10^{-4}$ s$^{-1}$ cho 1×27); đồ gá kẹp khía nhám chống xoay cứng; chiều dài đo hữu ích ~50 mm; quan sát nhiệt độ bề mặt bằng camera hồng ngoại FLIR và trường biến dạng bằng DIC.

Đối với cấu hình 7×7, ứng suất thềm tải giảm rất ít từ 517 MPa (sợi lõi) xuống 506 MPa (tao 1×7) và cáp đầy đủ, có các dải chuyển pha lan truyền rõ rệt [M27-E08]. Ngược lại, cấu hình 1×27 suy giảm mô đun cát tuyến từ 23.7 GPa (sợi lõi) xuống 7.3 GPa (cáp đầy đủ) và tăng biến dạng đứt lên ~40% do các vết dập lõm chế tạo triệt tiêu mặt chuyển pha cục bộ [M27-E13]. Phương pháp trừ đáp ứng xác định trình tự chuyển pha martensite từ trong ra ngoài: lớp B khởi đầu ở ~2.2%, lớp C ở ~6.0%, lớp D ở ~8.8% biến dạng cáp [M27-E24].

## F. Cross-paper comparisons

- **So sánh với M26 (Reedlunn et al. 2013 - Part I):**
  - M26 thiết lập hành vi kéo đẳng nhiệt vĩ mô của toàn bộ sợi cáp hoàn chỉnh; M27 đi sâu giải phẫu cơ học phân cấp bằng cách bóc tách từng tao, từng lớp và đo lường độc lập, từ đó chứng minh nguồn gốc của tính mềm dẻo và năng lượng tiêu tán.
- **So sánh với M23 (Zhang et al. 2021):**
  - M27 cung cấp một quan sát vật lý rất quan trọng đối với M23: Cấu trúc 7×7 có góc xoắn nhỏ hành xử gần như tương đương với một tập hợp các sợi dây song song (parallel wires), củng cố tính hợp lý của mô hình dầm phân lớp song song trong M23. Tuy nhiên, M27 cũng chỉ ra rằng với cấu trúc đa lớp xoắn ngược chiều (như 1×27), tương tác chèn ép và vết dập lõm giữa các lớp làm thay đổi hoàn toàn cơ chế biến dạng, điều mà mô hình dầm song song trơn nhẵn của M23 không thể nắm bắt.
- **So sánh với M25 (Vahidi et al. 2021) và M29 (Kang et al. 2020):**
  - M27 là nguồn thực nghiệm gốc cung cấp đường cong lực–biến dạng, mômen phản lực và trường nhiệt thực tế mà M25 và M29 sử dụng để hiệu chỉnh và kiểm chứng mô hình phần tử hữu hạn.

## G. Limitations and counterevidence

1. **Hiện tượng đứt mẫu tại đầu kẹp ngàm [M27-E13]:** Ứng suất tập trung và khía nhám của đồ gá kẹp đầu mút khiến sợi thường bị đứt sớm tại ngàm, làm đánh giá thấp độ dẻo thực tế của sợi.
2. **Khuếch đại sai số trong phương pháp trừ đáp ứng [M27-E24]:** Việc lấy hiệu lực đo giữa các cấu phần phụ thuộc (response subtraction) làm tăng độ nhạy với sai số đo lực và giả định lý tưởng rằng các lớp trong không bị thay đổi trạng thái tiếp xúc khi thêm lớp ngoài.
3. **Phạm vi tải trọng kéo đơn trục [M27-E02]:** Toàn bộ bài báo chỉ khảo sát tải kéo dọc trục có khống chế góc xoay; không khảo sát tải uốn ngang hay đo độ cứng uốn trực tiếp.
4. **Counterevidence đối với mô hình đơn trục giản lược [M27-E16]:** Chứng minh rằng giả thiết kéo một trục thuần túy hoàn toàn thất bại khi góc xoắn lớn (như tao 1×6) do bỏ qua biến dạng uốn và xoắn cục bộ của từng sợi dây.

## H. Relevance to MP1

- **Bằng chứng về trình tự chuyển pha theo lớp (C2.4, C2.4.1, C2.4.2, C2.5.5):** Phương pháp bóc tách trong M27-E24 chứng minh rõ ràng rằng trong một bó dây NiTi, các sợi không chuyển pha đồng thời mà diễn ra tuần tự từng lớp tùy theo mức biến dạng cục bộ. Trong MP1, khi bó dây TiNi chịu uốn, gradient biến dạng theo chiều cao tiết diện cũng sẽ gây ra sự chuyển pha tuần tự tương tự.
- **Ưu điểm của bó dây song song trong MP1:** Kết quả M27 cho thấy bó dây song song tránh được sự suy giảm mô đun nghiêm trọng (từ 23.7 xuống 7.3 GPa) và hư hỏng dập lõm cục bộ vốn có ở cáp xoắn nhiều lớp.
- **Kỹ thuật thực nghiệm tham khảo:** Cung cấp phương pháp luận kết hợp đo trường biến dạng DIC và ảnh nhiệt hồng ngoại để theo dõi sự lan truyền mặt chuyển pha martensite trên sợi NiTi.

## I. Reading route

1. **Sec. 1 & Sec. 2 (pp. 1–5):** Nắm cấu trúc phân cấp của mẫu thử 7×7 và 1×27, đồ gá kẹp không xoay và kỹ thuật đo đồng thời lực, mômen xoắn, DIC và IR.
2. **Sec. 3 (pp. 5–8, Figs. 2–4):** Khảo sát kết quả thực nghiệm của các cấu phần 7×7 và quan sát sự lan truyền mặt chuyển pha martensite.
3. **Sec. 4 (pp. 8–13, Figs. 5–10):** Đọc phân tích sự biến mất của mặt chuyển pha trong cáp 1×27 do biến dạng phân tán quanh các vết lõm chế tạo (ảnh SEM Fig. 6).
4. **Sec. 4.3 (pp. 14–17, Figs. 8–10):** Xem phân tích phản biện (counterevidence) đối với mô hình kéo đơn trục khi bỏ qua uốn/xoắn cục bộ của sợi.
5. **Sec. 5 (pp. 17–24, Figs. 13–20):** Đọc kỹ phương pháp trừ đáp ứng để hiểu cách tách biệt đóng góp lực và mômen của từng lớp dây riêng biệt.

## J. Questions for human writing

1. **Chuyển pha tuần tự trong bó dây uốn (C2.4.1, C2.5):** Khi bó dây TiNi của MP1 chịu uốn thuần túy, các sợi ở lớp ngoài cùng (biến dạng uốn lớn nhất) chuyển pha trước trong khi các sợi ở gần trục trung hòa vẫn ở pha austenite; điều này ảnh hưởng thế nào đến sự phân bố lực ma sát tiếp xúc giữa các lớp?
2. **So sánh bó dây song song với cáp xoắn (C2.4.2):** Luận văn có thể trích dẫn M27 như một luận điểm ủng hộ việc lựa chọn cấu hình bó dây song song thẳng trong MP1 nhằm duy trì mô đun cao và tránh sự phá hủy do dập lõm tiếp xúc giữa các sợi chéo nhau?
3. **Ảnh hưởng nhiệt trong quá trình tải (C2.4.1):** Trong thí nghiệm uốn của MP1, tốc độ biến dạng uốn cần được khống chế ở mức nào để đảm bảo điều kiện gần đẳng nhiệt và tránh hiện tượng tự gia nhiệt làm biến dạng thềm chuyển pha như M27 đã phân tích?

## K. Unresolved evidence

1. Dữ liệu thực nghiệm của M27 là tải kéo dọc trục có khống chế góc xoay; chưa có số liệu đo đạc trực tiếp về mômen uốn và độ cứng uốn của các cấu phần phân cấp này.
2. Số trang in (`printed_page`) trong P0 là `NOT_REPORTED`; các định vị sử dụng số trang vật lý của file PDF 23 trang.
