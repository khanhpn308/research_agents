# Tiếp nối audit: tài liệu tham khảo [21]–[25]

**Phạm vi:** claim trong bản nháp gắn [21]–[25], theo master traceability. Locator và excerpt/anchor là dấu vết đã lưu để mở PDF; chưa xác nhận độc lập từng câu bằng cách đọc lại PDF trong lượt này.

| Ref | Nguồn | DOI | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [21] | S. Vahidi, J. Arghavani, E. Choi & A. Ostadrahimi (2022), “Mechanical response of single and double-helix SMA wire ropes” | 10.1080/15376494.2021.1955313 | 9 | `21_A3-2022-Mechanical response of single and double-helix.pdf` |
| [22] | B. Reedlunn, S. Daly & J. Shaw (2013), “Superelastic shape memory alloy cables: Part II – Subcomponent isothermal responses” | 10.1016/j.ijsolstr.2013.03.015 | 4 | `22_2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf` |
| [23] | P. Narjabadifam et al. (2024), “Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes” | 10.3390/buildings14061567 | 2 | `23_2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf` |
| [24] | F. Barsi, B. Carboni & W. Lacarbonara (2025), “A new mechanical model of short wire ropes: Theory and experimental validation” | 10.1016/j.engstruct.2024.119217 | 15 | `24_2025-A new mechanical model of short wire ropes Theory and experimental.pdf` |
| [25] | K. Takashima, T. Imazawa & H. Cho (2022), “Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon” | 10.20965/jrm.2022.p0466 | 4 | `25_2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf` |

## [21] S. Vahidi, J. Arghavani, E. Choi & A. Ostadrahimi (2022), “Mechanical response of single and double-helix SMA wire ropes”

**CH2-S4-R0002-A01 — mục 2.4.1.** Siêu đàn hồi là khả năng thu hồi biến dạng lớn trong một chu trình tải–dỡ tải gần đẳng nhiệt nhờ chuyển pha do ứng suất, thường đi kèm vòng trễ cơ học. Hiệu ứng nhớ hình liên quan đến việc biến dạng được tạo ở trạng thái martensit và được phục hồi khi gia nhiệt qua miền chuyển pha. Hai hiện tượng có cùng nền tảng chuyển pha nhưng không thể dùng thay thế cho nhau. Trong nghiên cứu của Vahidi và cộng sự, trường hợp siêu đàn hồi được mô phỏng ở nhiệt độ trên nhiệt độ kết thúc austenit, còn trường hợp nhớ hình được mô phỏng bằng gia nhiệt sau khi tạo biến dạng ở nhiệt độ thấp hơn miền bắt đầu austenit [21, tr. 6–8]. Đây là điều kiện của mô hình nguồn, không phải bằng chứng rằng bó dây MP1 sẽ luôn làm việc trong một trong hai miền đó.

- **Locator PDF trong trace:** physical PDF pp.3–4, Introduction/model description. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0041-A01 — mục 2.4.2.** Vahidi và cộng sự [21] mô tả tường minh hình học xoắn và tiếp xúc giữa các bề mặt bằng mô hình FE. Mô hình có tương tác pháp tuyến và tiếp tuyến giữa các bề mặt, với hệ số ma sát được chỉ định. Với vật liệu SMA, tác giả dùng mô hình hiện tượng học Souza ba chiều trong Abaqus thông qua UMAT. Các hệ số ma sát và điều kiện tiếp xúc là đầu vào của bài toán nguồn; chúng chưa phải các tham số được nhận dạng cho bó TiNi của MP1.

- **Locator PDF trong trace:** Physical PDF M25:3,5; Sec.2; Sec.4.2; Souza model; UMAT implementation prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0042-A01 — mục 2.4.2.** Vahidi và cộng sự [21] mô tả tường minh hình học xoắn và tiếp xúc giữa các bề mặt bằng mô hình FE. Mô hình có tương tác pháp tuyến và tiếp tuyến giữa các bề mặt, với hệ số ma sát được chỉ định. Với vật liệu SMA, tác giả dùng mô hình hiện tượng học Souza ba chiều trong Abaqus thông qua UMAT. Các hệ số ma sát và điều kiện tiếp xúc là đầu vào của bài toán nguồn; chúng chưa phải các tham số được nhận dạng cho bó TiNi của MP1.

- **Locator PDF trong trace:** Physical PDF M25:4–5; Secs.4.1–4.2; Surface-to-surface contact prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0043-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M25:4–6; Secs.4.1–5.2; Table2; Figs.5,8–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0044-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M25:4–5; Sec.4;Sec.4.2; Implicit solver and contact/mesh discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0048-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M22:3; M23:3; M24:12; M25:5–6; Hysteresis synthesis; Model assumptions and limitations. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S4-R0050-A01 — mục 2.4.2.** Phạm vi đối chiếu của [21] chủ yếu là kéo dọc trục. Một đầu mẫu bị ràng buộc, đầu còn lại nhận chuyển vị hoặc tải tham chiếu chỉ theo phương trục. Mẫu thép 1×37 được so sánh với kết quả FE đã công bố; các đường kéo của mẫu SMA 1×27 và 7×7 được đối chiếu với thí nghiệm Reedlunn đã công bố, với các tham số vật liệu được kế thừa. Công trình không thực hiện thí nghiệm mới và không cung cấp kiểm chứng uốn. Việc mô tả riêng hình học xoắn, tiếp xúc và ứng xử vật liệu giúp khảo sát một bài toán chi tiết hơn, nhưng mức độ chi tiết cùng chi phí tính toán không tự chứng minh khả năng dự báo tốt hơn cho bài toán khác. Khi biến đổi vật liệu và tương tác tiếp xúc cùng xuất hiện trong kết quả tổng thể, kết quả đó cũng chưa cho phép tách duy nhất phần trễ do vật liệu và phần trễ do ma sát.

- **Locator PDF trong trace:** Physical PDF M23:3–6; M25:4–6; Model-dimensionality comparison; 2D elasticity vs3D FE. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S6-R0171-A01 — mục 2.6.3.** Về mô tả vật liệu và tiếp xúc, Vahidi và cộng sự đã kết hợp mô hình chuyển pha SMA với tiếp xúc ma sát giữa các dây trong mô phỏng phần tử hữu hạn cáp xoắn chịu kéo [21].

- **Locator PDF trong trace:** {"M25-E02": ["§2 Souza constitutive model; §4.1–4.2"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0172-A01 — mục 2.6.3.** Công trình đối chiếu với thí nghiệm đã công bố và sử dụng tham số vật liệu kế thừa [21].

- **Locator PDF trong trace:** {"M25-E06": ["§5.1–5.2; Figs.8,12; Table3"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.


## [22] B. Reedlunn, S. Daly & J. Shaw (2013), “Superelastic shape memory alloy cables: Part II – Subcomponent isothermal responses”

**CH2-S4-R0007-A01 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** physical PDF pp.2–7, Abstract/Secs. 1–3. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0008-A02 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** physical PDF pp.12–14 and 34, Sec. 4/Conclusions. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0009-A01 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** physical PDF p.18, analytical comparison. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0017-A01 — mục 2.4.1.** Bằng chứng phân cấp của nghiên cứu thành phần của Reedlunn và cộng sự làm rõ giới hạn này. Với 7×7, dây lõi, tao lõi 1×7 và cáp đầy đủ có đáp ứng kéo chuẩn hóa khá gần nhau do các góc xoắn nông; với 1×27, việc thêm các lớp góc xoắn sâu làm cáp mềm hơn và làm biến đổi cách chuyển pha phân bố trong cấu trúc [22, tr. 2, 7–14, 33–34]. Nghiên cứu thành phần của Reedlunn và cộng sự cũng cho thấy mô hình kéo một trục đơn giản có thể đánh giá quá cao ứng suất của đoạn nằm ngang (plateau) của một thành phần khi bỏ qua uốn và xoắn cục bộ [22, p. 18]. Vì thế, kết quả kéo của hai nghiên cứu của Reedlunn và cộng sự cung cấp bằng chứng về tương tác giữa vật liệu và kiến trúc cáp, nhưng không phải phép đo trực tiếp độ cứng uốn của bó dây thẳng MP1.

- **Locator PDF trong trace:** cross-study synthesis, physical PDFs cited above. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.


## [23] P. Narjabadifam et al. (2024), “Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes”

**CH2-S4-R0014-A01 — mục 2.4.1.** Nhiệt độ và tốc độ cần được tách khỏi nhau khi diễn giải. Nhiệt độ xác định pha ổn định và ứng suất chuyển pha; tốc độ tải quyết định mức độ trao đổi nhiệt trong quá trình biến dạng và có thể làm thay đổi nhiệt độ cục bộ. Hai nghiên cứu của Reedlunn và cộng sự theo dõi nhiệt độ và chọn tốc độ thấp để giữ điều kiện gần đẳng nhiệt, còn nghiên cứu của Vahidi và cộng sự dùng các đường cong vật liệu và nhiệt độ quy định trong mô phỏng. Nghiên cứu của Narjabadifam và cộng sự mô phỏng tải hình sin và kích động El Centro cho dây SMA nhưng không thực hiện phép thử NiTi độc lập, không quét nhiệt độ và không nhận dạng một định luật tốc độ [23, tr. 10–18]. Do đó, trong MP1, ảnh hưởng của nhiệt độ và tốc độ chỉ có thể được tách khi miền nhiệt–cơ và cách đo được quy định rõ; hiện tại chưa có cơ sở để gán một hệ số nhiệt hoặc hệ số tốc độ cho bó dây.

- **Locator PDF trong trace:** physical PDF pp.15–18, Secs. 3.1–3.3/Figs. 17–19. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0018-A01 — mục 2.4.1.** Nhiệt độ và tốc độ cần được tách khỏi nhau khi diễn giải. Nhiệt độ xác định pha ổn định và ứng suất chuyển pha; tốc độ tải quyết định mức độ trao đổi nhiệt trong quá trình biến dạng và có thể làm thay đổi nhiệt độ cục bộ. Hai nghiên cứu của Reedlunn và cộng sự theo dõi nhiệt độ và chọn tốc độ thấp để giữ điều kiện gần đẳng nhiệt, còn nghiên cứu của Vahidi và cộng sự dùng các đường cong vật liệu và nhiệt độ quy định trong mô phỏng. Nghiên cứu của Narjabadifam và cộng sự mô phỏng tải hình sin và kích động El Centro cho dây SMA nhưng không thực hiện phép thử NiTi độc lập, không quét nhiệt độ và không nhận dạng một định luật tốc độ [23, tr. 10–18]. Do đó, trong MP1, ảnh hưởng của nhiệt độ và tốc độ chỉ có thể được tách khi miền nhiệt–cơ và cách đo được quy định rõ; hiện tại chưa có cơ sở để gán một hệ số nhiệt hoặc hệ số tốc độ cho bó dây.

- **Locator PDF trong trace:** MP1 implication stated in prose. **Trạng thái trace:** `PROPOSAL`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.


## [24] F. Barsi, B. Carboni & W. Lacarbonara (2025), “A new mechanical model of short wire ropes: Theory and experimental validation”

**CH2-S4-R0031-A01 — mục 2.4.2.** Barsi và cộng sự [24] tiếp cận cáp xoắn ngắn bằng mô hình dầm Timoshenko tuyến tính có xét biến dạng cắt. Từng dây được mô tả như một dầm có trục cong; biến dạng riêng, hay eigenstrain, được đưa vào để giải phóng phần biến dạng của dây do độ cong gây ra theo giả thiết của từng trạng thái liên kết. Tác giả gán cùng một chế độ cho tất cả các dây trong một lần tính. Bởi vậy, các trạng thái dính hoàn toàn, dính một phần và trượt hoàn toàn là những giả thiết để đánh giá đáp ứng tương ứng. Mô hình không cập nhật diễn biến chuyển đổi giữa dính và trượt trên từng mặt tiếp xúc trong một chu kỳ tải.

- **Locator PDF trong trace:** Physical PDF M24:3–5; Secs.2–2.3; Eqs.6,11,12,18 (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0032-A01 — mục 2.4.2.** Khái niệm trượt phải gắn với cấp mô tả đang dùng. Trong mô hình lớp của bó dây song song, trượt được biểu diễn bằng chênh lệch chuyển vị dọc trục giữa các lớp tương đương. Với tiếp xúc giữa những dây cong trong cáp xoắn, trượt cục bộ là chuyển động tương đối theo phương tiếp tuyến tại mặt tiếp xúc. Chênh lệch chuyển vị giữa hai lớp quy đổi không cung cấp đầy đủ trường trượt trên bề mặt tiếp xúc của các dây tròn. Cũng cần phân biệt trạng thái dính, khi liên kết động học đang xét không cho phép trượt; trạng thái trượt một phần, khi chỉ một số mặt tiếp xúc hoặc một số vùng trượt; và trạng thái trượt hoàn toàn theo định nghĩa của từng mô hình. Trượt hoàn toàn không có nghĩa là mọi lực tương tác đều biến mất. Những trạng thái này mô tả quan hệ chuyển động giữa các thành phần, không đồng nghĩa với biến dạng dẻo của vật liệu dây. Đặc biệt, trạng thái dính một phần (partial stick) trong [24] là một giả thiết động học cụ thể, không phải tỷ lệ diện tích bám đo được và cũng không phải lời giải cho trượt vi mô cục bộ. Vì thế, không thể gán cùng một ngưỡng vật lý cho các trạng thái mang tên gần nhau trong các mô hình khác nhau.

- **Locator PDF trong trace:** Physical PDF M24:4–5; Sec.2.2; Eqs.11–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0032-A02 — mục 2.4.2.** Barsi và cộng sự [24] tiếp cận cáp xoắn ngắn bằng mô hình dầm Timoshenko tuyến tính có xét biến dạng cắt. Từng dây được mô tả như một dầm có trục cong; biến dạng riêng, hay eigenstrain, được đưa vào để giải phóng phần biến dạng của dây do độ cong gây ra theo giả thiết của từng trạng thái liên kết. Tác giả gán cùng một chế độ cho tất cả các dây trong một lần tính. Bởi vậy, các trạng thái dính hoàn toàn, dính một phần và trượt hoàn toàn là những giả thiết để đánh giá đáp ứng tương ứng. Mô hình không cập nhật diễn biến chuyển đổi giữa dính và trượt trên từng mặt tiếp xúc trong một chu kỳ tải.

- **Locator PDF trong trace:** Physical PDF M24:4–5; Sec.2.2; Eqs.11–12. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0033-A01 — mục 2.4.2.** Barsi và cộng sự [24] tiếp cận cáp xoắn ngắn bằng mô hình dầm Timoshenko tuyến tính có xét biến dạng cắt. Từng dây được mô tả như một dầm có trục cong; biến dạng riêng, hay eigenstrain, được đưa vào để giải phóng phần biến dạng của dây do độ cong gây ra theo giả thiết của từng trạng thái liên kết. Tác giả gán cùng một chế độ cho tất cả các dây trong một lần tính. Bởi vậy, các trạng thái dính hoàn toàn, dính một phần và trượt hoàn toàn là những giả thiết để đánh giá đáp ứng tương ứng. Mô hình không cập nhật diễn biến chuyển đổi giữa dính và trượt trên từng mặt tiếp xúc trong một chu kỳ tải.

- **Locator PDF trong trace:** Physical PDF M24:5; Sec.2.3; Eq.18 and following prose. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0034-A01 — mục 2.4.2.** Khác với hai mô hình lớp, [24] có thí nghiệm riêng trên các mẫu cáp thép. Tác giả thực hiện uốn gần tĩnh theo điều khiển chuyển vị ở 0,2 Hz, giữ không cho hai đầu quay và dùng cơ cấu trượt ngang để giảm sự kéo giãn mẫu. Điều kiện này không phải thí nghiệm uốn thuần túy cổ điển với mô men không đổi. Vòng trễ uốn được ghi nhận qua quan hệ lực và chuyển vị đầu mẫu. Độ dốc nhánh tăng tải thấp hơn độ dốc ở đoạn đầu nhánh dỡ tải, tạo ra hai mức độ cứng nhánh được khớp từ dữ liệu, có đơn vị kN/mm. Các độ dốc đó không phải EI của tiết diện và cũng không phải một độ cứng cát tuyến đại diện cho toàn bộ vòng trễ.

- **Locator PDF trong trace:** Physical PDF M24:5–7; Secs.3–3.1; Figs.3–5. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0035-A01 — mục 2.4.2.** Khác với hai mô hình lớp, [24] có thí nghiệm riêng trên các mẫu cáp thép. Tác giả thực hiện uốn gần tĩnh theo điều khiển chuyển vị ở 0,2 Hz, giữ không cho hai đầu quay và dùng cơ cấu trượt ngang để giảm sự kéo giãn mẫu. Điều kiện này không phải thí nghiệm uốn thuần túy cổ điển với mô men không đổi. Vòng trễ uốn được ghi nhận qua quan hệ lực và chuyển vị đầu mẫu. Độ dốc nhánh tăng tải thấp hơn độ dốc ở đoạn đầu nhánh dỡ tải, tạo ra hai mức độ cứng nhánh được khớp từ dữ liệu, có đơn vị kN/mm. Các độ dốc đó không phải EI của tiết diện và cũng không phải một độ cứng cát tuyến đại diện cho toàn bộ vòng trễ.

- **Locator PDF trong trace:** Physical PDF M24:6–8; Sec.3.1; Sec.4; Fig.4b; Eq.21 (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0036-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:8–11; Secs.4.1–4.3; Figs.9,11. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0037-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:9,11; Secs.4.2–4.3; Fig.11; discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0038-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:11–12; Sec.5; Sec.6 Conclusions; Table7; conclusions. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0039-A01 — mục 2.4.2.** Trong đối chiếu của [24], giả thiết trượt hoàn toàn xấp xỉ mức độ cứng nhánh đo thấp hơn, còn giả thiết dính một phần gần mức độ cứng nhánh cao hơn; giả thiết dính hoàn toàn dự báo độ cứng cao quá mức rõ rệt. Cách so sánh này cho thấy tác dụng của giả thiết liên kết đối với độ cứng kết cấu. Tuy nhiên, các mức tính toán chỉ là những ước lượng theo mô hình, chưa phải các cận toán học bảo đảm cho mọi bó dây; một số ước lượng vẫn nằm ngoài khoảng đo. Ảnh hưởng của đầu mẫu và bước xoắn nổi rõ nhất đối với các đoạn cáp ngắn. Tác giả đo hình học và cho biết không hiệu chỉnh các tham số vật lý bằng cách khớp mô hình với thí nghiệm. Dữ liệu kéo và xoắn của Utting và Jones được dùng thêm cho một đối chiếu bên ngoài riêng. Dù mô hình đối chiếu được các mức độ cứng nhánh, nó chưa dự báo toàn bộ vòng trễ hoặc năng lượng tiêu tán trong chu kỳ; phần mở rộng này được tác giả để lại trong kết luận.

- **Locator PDF trong trace:** Physical PDF M24:12; Sec.6 Conclusions; Final paragraph. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0046-A01 — mục 2.4.2.** Khái niệm trượt phải gắn với cấp mô tả đang dùng. Trong mô hình lớp của bó dây song song, trượt được biểu diễn bằng chênh lệch chuyển vị dọc trục giữa các lớp tương đương. Với tiếp xúc giữa những dây cong trong cáp xoắn, trượt cục bộ là chuyển động tương đối theo phương tiếp tuyến tại mặt tiếp xúc. Chênh lệch chuyển vị giữa hai lớp quy đổi không cung cấp đầy đủ trường trượt trên bề mặt tiếp xúc của các dây tròn. Cũng cần phân biệt trạng thái dính, khi liên kết động học đang xét không cho phép trượt; trạng thái trượt một phần, khi chỉ một số mặt tiếp xúc hoặc một số vùng trượt; và trạng thái trượt hoàn toàn theo định nghĩa của từng mô hình. Trượt hoàn toàn không có nghĩa là mọi lực tương tác đều biến mất. Những trạng thái này mô tả quan hệ chuyển động giữa các thành phần, không đồng nghĩa với biến dạng dẻo của vật liệu dây. Đặc biệt, trạng thái dính một phần (partial stick) trong [24] là một giả thiết động học cụ thể, không phải tỷ lệ diện tích bám đo được và cũng không phải lời giải cho trượt vi mô cục bộ. Vì thế, không thể gán cùng một ngưỡng vật lý cho các trạng thái mang tên gần nhau trong các mô hình khác nhau.

- **Locator PDF trong trace:** Physical PDF M22:2–3; M23:10–13; M24:4–5; Slip-definition comparison; Source definitions compared. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Vai trò tổng hợp, đề xuất hoặc bao phủ theo loại hồ sơ; các nguồn nền không phải phép đo MP1.

**CH2-S5-R0020-A01 — mục §2.5.2.** Trong tài liệu về dây thép ngắn, Barsi, Carboni và Lacarbonara xây dựng mô hình dầm biến dạng cắt cho dây đơn và dây nhiều tao, với ba giả thuyết động học perfect-stick, partial-stick và full-slip. Nguồn đặt các trạng thái giới hạn vào hai phía của đáp ứng uốn và đối chiếu độ cứng cực đại, cực tiểu với thí nghiệm trên hai họ dây thép. Đây là tiền lệ gần nhất cho việc dùng trạng thái tiếp xúc để tạo giá trị tham chiếu, nhưng vật liệu, cấu trúc xoắn, chiều dài và đại lượng độ cứng của nguồn khác với bó dây TiNi MP1 [24].

- **Locator PDF trong trace:** Abstract; Secs.2–6; Figs.9–11; Table 6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Không chuyển số liệu sang TiNi; kN/mm khác B N·m².

**CH2-S5-R0021-A01 — mục §2.5.2.** Nghiên cứu của Barsi, Carboni và Lacarbonara cho thấy sự khác nhau này không chỉ là cách đặt tên. Trong mô hình của nguồn, full-slip làm các dây không còn đóng góp biến dạng cắt dây trong uốn, còn partial-stick vẫn tạo một trạng thái trung gian; ma trận quan hệ cấu thành chỉ giữ cùng dạng khi mọi dây được giả định ở cùng một trạng thái. Thí nghiệm uốn gần tĩnh trên dây R1 một tao và R2 bảy tao cho thấy full-slip dự đoán gần cận dưới, trong khi partial-stick phù hợp hơn với cận trên thực nghiệm; perfect-stick cho giá trị lớn hơn đáng kể. Vì độ cứng nguồn được biểu diễn bằng độ dốc lực–chuyển vị (kN/mm), không được đồng nhất trực tiếp với độ cứng uốn B có đơn vị N·m² [24].

- **Locator PDF trong trace:** Sec.2.2 Eq.(12), Eqs.(22–24), Discussion. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Mixed-state local response không được mô tả bằng một matrix đồng nhất.

**CH2-S5-R0022-A01 — mục §2.5.2.** Nghiên cứu của Barsi, Carboni và Lacarbonara cho thấy sự khác nhau này không chỉ là cách đặt tên. Trong mô hình của nguồn, full-slip làm các dây không còn đóng góp biến dạng cắt dây trong uốn, còn partial-stick vẫn tạo một trạng thái trung gian; ma trận quan hệ cấu thành chỉ giữ cùng dạng khi mọi dây được giả định ở cùng một trạng thái. Thí nghiệm uốn gần tĩnh trên dây R1 một tao và R2 bảy tao cho thấy full-slip dự đoán gần cận dưới, trong khi partial-stick phù hợp hơn với cận trên thực nghiệm; perfect-stick cho giá trị lớn hơn đáng kể. Vì độ cứng nguồn được biểu diễn bằng độ dốc lực–chuyển vị (kN/mm), không được đồng nhất trực tiếp với độ cứng uốn B có đơn vị N·m² [24].

- **Locator PDF trong trace:** Figs.9–11; Table 6; Sec.6. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Sai số phụ thuộc chiều dài/kẹp; biến dạng hình học tăng ở biên độ lớn.

**CH2-S5-R0034-A01 — mục §2.5.2.** Nghiên cứu của Barsi, Carboni và Lacarbonara cho thấy sự khác nhau này không chỉ là cách đặt tên. Trong mô hình của nguồn, full-slip làm các dây không còn đóng góp biến dạng cắt dây trong uốn, còn partial-stick vẫn tạo một trạng thái trung gian; ma trận quan hệ cấu thành chỉ giữ cùng dạng khi mọi dây được giả định ở cùng một trạng thái. Thí nghiệm uốn gần tĩnh trên dây R1 một tao và R2 bảy tao cho thấy full-slip dự đoán gần cận dưới, trong khi partial-stick phù hợp hơn với cận trên thực nghiệm; perfect-stick cho giá trị lớn hơn đáng kể. Vì độ cứng nguồn được biểu diễn bằng độ dốc lực–chuyển vị (kN/mm), không được đồng nhất trực tiếp với độ cứng uốn B có đơn vị N·m² [24].

- **Locator PDF trong trace:** State definitions and limits. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** No local full-decoupling measurement.


## [25] K. Takashima, T. Imazawa & H. Cho (2022), “Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon”

**CH2-S4-R0067-A02 — mục 2.4.3.** Takashima và cộng sự [25] đánh giá đáp ứng công xôn bằng tải tập trung và độ dốc tuyến tính của quan hệ lực với độ võng, với chiều dài làm việc 50 mm. Độ cứng đo được tăng khi hút khí; bài báo nêu mức áp suất dưới −90 kPa nhưng không xác định rõ mốc tham chiếu của giá trị này. Áp suất trong túi không phải phép đo phân bố tải pháp tuyến tại các tiếp xúc giữa hạt. Ở trạng thái chưa kẹt, biến dạng cục bộ của màng ngoài cũng tham gia vào chuyển vị, nên độ dốc đo được không đại diện riêng cho mô đun của dây. Ước lượng dầm tuyến tính bằng cách cộng đóng góp của các phần tử trong bài báo là một đối chiếu cơ học sơ bộ, chưa phải định luật ma sát cục bộ. Các chu trình chuyển động lặp lại cho thấy ảnh hưởng của lịch sử và độ trễ, nhưng không tách riêng được đóng góp của vật liệu nhớ hình, trượt tiếp xúc, màng và sự sắp xếp hạt [25].

- **Locator PDF trong trace:** M32:3–4; Secs.2.2.1–2.2.2; Table1;construction text. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0068-A01 — mục 2.4.3.** Takashima và cộng sự [25] đánh giá đáp ứng công xôn bằng tải tập trung và độ dốc tuyến tính của quan hệ lực với độ võng, với chiều dài làm việc 50 mm. Độ cứng đo được tăng khi hút khí; bài báo nêu mức áp suất dưới −90 kPa nhưng không xác định rõ mốc tham chiếu của giá trị này. Áp suất trong túi không phải phép đo phân bố tải pháp tuyến tại các tiếp xúc giữa hạt. Ở trạng thái chưa kẹt, biến dạng cục bộ của màng ngoài cũng tham gia vào chuyển vị, nên độ dốc đo được không đại diện riêng cho mô đun của dây. Ước lượng dầm tuyến tính bằng cách cộng đóng góp của các phần tử trong bài báo là một đối chiếu cơ học sơ bộ, chưa phải định luật ma sát cục bộ. Các chu trình chuyển động lặp lại cho thấy ảnh hưởng của lịch sử và độ trễ, nhưng không tách riêng được đóng góp của vật liệu nhớ hình, trượt tiếp xúc, màng và sự sắp xếp hạt [25].

- **Locator PDF trong trace:** M32:4–5,8; Secs.2.3.2;3.1.2;3.2.2; Eq.1;Figs.16–17. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0069-A01 — mục 2.4.3.** Trong điều kiện của [25], nguyên mẫu SMA phục hồi nhanh hơn nguyên mẫu SMP nhưng chưa trở lại hoàn toàn hình dạng ban đầu. So sánh này gắn với hai kết cấu và hai loại vật liệu khác nhau nên chưa cho phép quy chênh lệch thời gian hoàn toàn cho bản chất SMA. Tác giả đề xuất phân bố cà phê không đồng đều là một nguyên nhân của phục hồi chưa hoàn toàn; đây là cách giải thích được đề xuất, chưa phải nguyên nhân duy nhất đã được đo và tách biệt. Kết quả này đặt ra một phân biệt cơ học cần giữ khi đánh giá cơ cấu điều biến ma sát: thời gian phục hồi ngắn và mức phục hồi lớn không phải cùng một tiêu chí.

- **Locator PDF trong trace:** M32:7–8; Secs.3.2.1–3.2.2; Figs.15–17. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0070-A01 — mục 2.4.3.** Takashima và cộng sự [25] đánh giá đáp ứng công xôn bằng tải tập trung và độ dốc tuyến tính của quan hệ lực với độ võng, với chiều dài làm việc 50 mm. Độ cứng đo được tăng khi hút khí; bài báo nêu mức áp suất dưới −90 kPa nhưng không xác định rõ mốc tham chiếu của giá trị này. Áp suất trong túi không phải phép đo phân bố tải pháp tuyến tại các tiếp xúc giữa hạt. Ở trạng thái chưa kẹt, biến dạng cục bộ của màng ngoài cũng tham gia vào chuyển vị, nên độ dốc đo được không đại diện riêng cho mô đun của dây. Ước lượng dầm tuyến tính bằng cách cộng đóng góp của các phần tử trong bài báo là một đối chiếu cơ học sơ bộ, chưa phải định luật ma sát cục bộ. Các chu trình chuyển động lặp lại cho thấy ảnh hưởng của lịch sử và độ trễ, nhưng không tách riêng được đóng góp của vật liệu nhớ hình, trượt tiếp xúc, màng và sự sắp xếp hạt [25].

- **Locator PDF trong trace:** M32:7–9; Secs.3.1.2;3.2.2–3.3.1; Figs.13,18–19. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

## Nhận xét audit [21]–[25]

- **[21] Vahidi et al.** Nguồn mô phỏng cáp xoắn SMA bằng mô hình vật liệu chuyển pha và tiếp xúc ma sát, nhưng đối chiếu chính chủ yếu là kéo dọc trục; không xem đó là kiểm chứng uốn bó dây MP1.
- **[22] Reedlunn et al., Part II.** Là nghiên cứu phản ứng đẳng nhiệt của các tiểu cấu phần cáp; kết quả phụ thuộc cấu trúc cáp và cấp cấu phần. Các diễn giải tổng hợp giữa Part I/II được trace phân loại inference, không phải một kết quả đơn nguồn.
- **[23] Narjabadifam et al.** Trace gắn một claim về tác động nhiệt/tốc độ và một implication đề xuất; cần giữ tách phần đo của nguồn khỏi suy luận ứng dụng cho MP1.
- **[24] Barsi et al.** Đây là nguồn gần về mô hình cơ học cáp ngắn và các giả thuyết perfect-stick/partial-stick/full-slip, kèm thử uốn riêng. Kết quả gắn với mẫu cáp thép, điều kiện biên và mô hình Timoshenko của bài; không tự động chuyển thành mô hình bó TiNi.
- **[25] Takashima et al.** Nguồn về link biến độ cứng có vật liệu nhớ hình và jamming transition; trace ghi chú áp suất dưới −90 kPa nhưng mốc tham chiếu không rõ, cần giữ bất định đó khi dùng số liệu.
- Cả năm PDF có trong thư mục tích hợp. Một số locator nêu physical PDF page, còn mã Mxx hoặc tên mục không phải số trang in; khi đối chiếu trực tiếp cần ghi đồng thời trang PDF và trang in nếu khác nhau. Excerpt trong phần này chưa được xác nhận mới trên PDF.


---

