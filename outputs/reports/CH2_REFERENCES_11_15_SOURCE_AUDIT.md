# Tiếp nối audit: tài liệu tham khảo [11]–[15]

**Phạm vi:** tiếp tục cùng bản nháp và master traceability. Locator và excerpt/anchor được chuyển từ CSV; đây là dấu vết sẵn có để đối chiếu, không phải xác nhận độc lập từng câu từ PDF.

| Ref | Nguồn | DOI/ID | Claim/anchor duy nhất | PDF đóng gói |
|---:|---|---|---:|---|
| [11] | S. Zhang, J. Yao, W. Zhao & C. Wei (2025), “A continuum-based model for a layer jamming beam” | 10.5194/ms-16-821-2025 | 7 | `11_2025-A continuum-based model for a layer jamming beam.pdf` |
| [12] | F. Caro & M. G. Carmichael (2024), “A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics” | 10.3390/act13020064 | 6 | `12_A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf` |
| [13] | Y. Zhang, Q. Feng, G. Wang & R. Xu (2021), “Analytical model for the bending of parallel wire cables considering interactions among wires” | 10.1016/j.ijmecsci.2020.106192 | 3 | `13_2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf` |
| [14] | Joint Committee for Guides in Metrology (2008), “Evaluation of measurement data — Guide to the expression of uncertainty in measurement” | JCGM 100:2008 | 11 | `14_M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf` |
| [15] | Y. Fan, B. Yi & D. Liu (2024), “An overview of stiffening approaches for continuum robots” | 10.1016/j.rcim.2024.102811 | 7 | `15_M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf` |

## [11] S. Zhang, J. Yao, W. Zhao & C. Wei (2025), “A continuum-based model for a layer jamming beam”

**CH2-S2-R0076-A01 — mục 2.2.2.** Zhang và cộng sự dùng tương tự đàn dẻo để mô tả môi trường layer jamming có trượt, nên chữ “dẻo” trong cách quy giản đó không chứng minh dây TiNi bị biến dạng dẻo [11].

- **Locator PDF trong trace:** §2, continuum stress-state discussion. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “there is no slipping between sheets”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S2-R0079-A01 — mục 2.2.2.** Trạng thái tiếp xúc còn phụ thuộc đường tải: mô hình liên tục của Zhang và cộng sự phân biệt tăng tải, trượt tại giới hạn và dỡ tải, rồi giải đáp ứng theo gia số [11].

- **Locator PDF trong trace:** §2, loading/yielding/unloading discussion. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE`.
- **Excerpt/anchor đã lưu:** “must be solved incrementally”
- **Ranh giới/ghi chú:** No transfer of layer/fiber/cable thresholds or constitutive parameters to MP1

**CH2-S3-R0047-A01 — mục Abstract;Sec.2;Secs.4–5.** Zhang và cộng sự đi xa hơn về mức mô hình hóa khi coi chồng lớp như một môi trường liên tục trong giới hạn lớp mỏng vô hạn, với δ/h nhỏ và số lớp đủ lớn; bài báo nêu miền thực hành xấp xỉ từ khoảng 10 lớp trở lên dựa trên đối chiếu phần tử hữu hạn [11]. Mô hình liên tục mô tả ứng suất pháp, ứng suất cắt và các trạng thái kẹt, trượt một phần, trượt hoàn toàn; kết quả được so sánh với phần tử hữu hạn cho các mẫu 10 và 25 lớp, rồi với thí nghiệm dầm PVC 20 lớp ở 60 kPa. Tuy nhiên, chính phần kiểm chứng cho thấy sai lệch gần biên, trong vùng trượt lớn và khi ảnh hưởng hình học cong hoặc ứng suất pháp không còn phù hợp với giả thiết liên tục. Độ phù hợp của biến dạng toàn cục trong một cấu hình không đồng nghĩa với việc mô hình đã nhận dạng đúng lực tiếp xúc cục bộ hoặc có thể chuyển sang bó dây TiNi.

- **Locator PDF trong trace:** Fig.1;Fig.6–7. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Giả thiết δ/h nhỏ, n lớn; vật liệu, hình học và tải riêng của LJS.

**CH2-S3-R0048-A01 — mục Secs.4–6.** Zhang và cộng sự đi xa hơn về mức mô hình hóa khi coi chồng lớp như một môi trường liên tục trong giới hạn lớp mỏng vô hạn, với δ/h nhỏ và số lớp đủ lớn; bài báo nêu miền thực hành xấp xỉ từ khoảng 10 lớp trở lên dựa trên đối chiếu phần tử hữu hạn [11]. Mô hình liên tục mô tả ứng suất pháp, ứng suất cắt và các trạng thái kẹt, trượt một phần, trượt hoàn toàn; kết quả được so sánh với phần tử hữu hạn cho các mẫu 10 và 25 lớp, rồi với thí nghiệm dầm PVC 20 lớp ở 60 kPa. Tuy nhiên, chính phần kiểm chứng cho thấy sai lệch gần biên, trong vùng trượt lớn và khi ảnh hưởng hình học cong hoặc ứng suất pháp không còn phù hợp với giả thiết liên tục. Độ phù hợp của biến dạng toàn cục trong một cấu hình không đồng nghĩa với việc mô hình đã nhận dạng đúng lực tiếp xúc cục bộ hoặc có thể chuyển sang bó dây TiNi.

- **Locator PDF trong trace:** Figs.6–7. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Độ phù hợp biến dạng toàn cục không nhận dạng local traction.

**CH2-S6-R0017-A01 — mục 2.6.1.** Một mức đối chiếu khác được báo cáo trong mô hình liên tục cho dầm kẹt lớp của Zhang và cộng sự [11].

- **Locator PDF trong trace:** {"M18-E01": "Abstract; Sections 1–2", "M18-E06": "Section 5; Fig. 7a–b"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “infinitely many thin layers; analytical curve lies entirely within the 1σ interval”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0107-A01 — mục 2.6.2.** Ở một cấp mô tả khác, mô hình liên tục của Zhang và cộng sự đã biểu diễn biến dạng và ứng suất trong dầm kẹt lớp có nhiều lớp mỏng [11].

- **Locator PDF trong trace:** {"M18-E01": ["Abstract; Abstract; direct page/anchor controls"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “while the total height h remains constant”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0111-A01 — mục 2.6.2.** Chính nguồn cũng chỉ ra sai khác gần đầu dầm và khi vùng trượt lớn; bỏ qua thành phần ứng suất pháp theo chiều dày làm mô hình dự đoán vùng trượt rộng hơn trong một số đối chiếu số [11].

- **Locator PDF trong trace:** {"M18-E07": ["Sec. 5–6 limitations; Fig. 6; Conclusions; direct page/anchor controls"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “CLJM’s neglect of normal stress along the y axis”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.


## [12] F. Caro & M. G. Carmichael (2024), “A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics”

**CH2-S2-R0122-A01 — mục 2.2.3.** Trong kẹt lớp bằng chân không mà Caro và Carmichael tổng hợp, bơm hạ áp suất trong buồng kín bao quanh các lớp, còn áp suất khí quyển nén buồng và chồng lớp [12].

- **Locator PDF trong trace:** §3.1.3 Vacuum Pressure. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “atmospheric pressure compresses the chamber”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S3-R0010-A06 — mục Classification context; Section 2; Section 2.2; Design.** Họ kiến trúc kẹt cơ họcKẹt lớp/tấmCác lá hoặc tấm mỏng chuyển giữa trạng thái cùng chịu uốn và trạng thái trượt tương đối.Cơ cấu khóa phụ thuộc kiến trúc, gồm chân không hoặc cơ cấu khác.Không chuyển trực tiếp đáp ứng của tấm sang bó dây.[12]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0022-A01 — mục 3.1.3 Vacuum Pressure Jamming.** Trong phần tổng quan của Caro và Carmichael, cấu hình kẹt lớp/tấm dưới chân không (vacuum layer jamming) là một chồng lớp vật liệu mềm được đặt trong một khoang kín khí; khi không khí được hút ra, áp suất khí quyển ép chồng lớp lại và làm tăng sức kháng ma sát đối với trượt giữa các lớp [12]. Cơ chế này minh họa rõ vai trò của tiếp xúc phân bố trên toàn chồng lớp: độ cứng tăng lên nhờ hạn chế trượt tương đối giữa các lớp, chứ không phải vì áp suất chân không tự nó là một đại lượng cơ học cục bộ đã biết. Mô tả của nguồn cung cấp cơ sở cho một mô hình lớp tiếp xúc có biến dạng và ma sát, nhưng không đưa ra luật địa phương đầy đủ nối áp suất nguồn với lực pháp tuyến, sự khởi phát hư hỏng hay phân bố trượt trong từng vùng.

- **Locator PDF trong trace:** Fig. 3c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M06 là review-level synthesis tại locator này; không báo cáo local normal-pressure field, slip localization hoặc failure criterion.

**CH2-S3-R0022-A02 — mục 3.1.3 Vacuum Pressure Jamming.** Caro và Carmichael [12] — kẹt lớp/tấm chân khôngChồng lớp mềm trong khoang kín khí; tiếp xúc lớp–lớp.Hút khí tạo chênh áp; áp suất khí quyển ép khoang và chồng lớp.Sức kháng ma sát đối với trượt giữa lớp tăng, hạn chế chuyển vị tương đối và tăng độ cứng uốn.Nguồn xác nhận cơ chế khóa; không báo cáo phân bố lực pháp tuyến cục bộ hay tiêu chuẩn hư hỏng trong mô tả nguồn này.Không chuyển trực tiếp sang topology dây hoặc bó TiNi.

- **Locator PDF trong trace:** Fig. 3c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M06 là review-level synthesis tại locator này; không báo cáo local normal-pressure field, slip localization hoặc failure criterion.

**CH2-S3-R0031-A01 — mục 3.1.3 Vacuum Pressure Jamming.** Trong cơ cấu kẹt lớp chân không, tổng quan của Caro và Carmichael mô tả một chồng lớp mềm nằm trong khoang kín khí. Khi hút khí, áp suất khí quyển ép khoang và chồng lớp, làm tăng tương tác ma sát giữa các lớp [12]. Cách mô tả này xác định đúng chuỗi cơ học ở mức kiến trúc, nhưng không cung cấp trường áp suất cục bộ theo chiều dày hay phân bố lực pháp tuyến tại từng giao diện. Do đó, áp suất chân không được dùng như biến kích hoạt của cấu hình, không được đồng nhất với một áp suất tiếp xúc đồng đều.

- **Locator PDF trong trace:** Fig.3c. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Review-level synthesis; không báo cáo trường áp suất cục bộ.

**CH2-S6-R0157-A01 — mục 2.6.3.** Sự thay đổi truyền lực do giam giữ và trượt tiếp xúc đã có cơ sở trong các hệ được nghiên cứu trước; tổng quan về kẹt lớp của Caro và Carmichael mô tả sự chuyển tiếp giữa các miền trước trượt và trượt khi chịu tải [12].

- **Locator PDF trong trace:** {"M06-E04": ["6. Limitations of Lock/Unlock Mechanisms; 6. Limitations of Lock/Unlock Mechanisms, continued; 1. Introduction"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “limitations are inherent; transition from the pre-slip regime; excludes other forms of jamming”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.


## [13] Y. Zhang, Q. Feng, G. Wang & R. Xu (2021), “Analytical model for the bending of parallel wire cables considering interactions among wires”

**CH2-S2-R0154-A01 — mục 2.2.3.** Mô hình cáp của Zhang và cộng sự giả thiết lực tương tác tỷ lệ với trượt, đồng thời thừa nhận tương tác thực phức tạp hơn và cần hiệu chuẩn thực nghiệm [13].

- **Locator PDF trong trace:** §2.1 continuation, before §2.2. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “much more complicated than the linear assumption”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S4-R0025-A01 — mục 2.4.2.** Zhang và cộng sự năm 2021 [13] mở rộng mô tả sang bài toán hai chiều trong trạng thái ứng suất phẳng, giải đồng thời chuyển vị, ứng suất và trượt giữa các lớp bằng phương pháp không gian trạng thái. Các hàng dây vẫn được quy đổi theo chiều cao và diện tích. Khi chuyển sang lớp tương đương có bề rộng đơn vị, tác giả điều chỉnh mô đun theo bề rộng quy đổi. Mô đun của lớp tương đương trong bước này là tham số của phép quy đổi, không phải một giá trị mô đun Young mới đo trên vật liệu dây. Mô hình cho phép khảo sát trường cơ học bên trong sâu hơn quan hệ lực và chuyển vị tổng thể, nhưng phép giảm chiều vẫn không phân giải hình dạng thật của tiếp xúc dây tròn, sự thay đổi xếp chặt theo tiết diện hay trường ngoài mặt phẳng.

- **Locator PDF trong trace:** Physical PDF M23:2–3; Secs.2.1–2.2; Figs.1–2. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.

**CH2-S4-R0026-A01 — mục 2.4.2.** Zhang và cộng sự năm 2021 [13] mở rộng mô tả sang bài toán hai chiều trong trạng thái ứng suất phẳng, giải đồng thời chuyển vị, ứng suất và trượt giữa các lớp bằng phương pháp không gian trạng thái. Các hàng dây vẫn được quy đổi theo chiều cao và diện tích. Khi chuyển sang lớp tương đương có bề rộng đơn vị, tác giả điều chỉnh mô đun theo bề rộng quy đổi. Mô đun của lớp tương đương trong bước này là tham số của phép quy đổi, không phải một giá trị mô đun Young mới đo trên vật liệu dây. Mô hình cho phép khảo sát trường cơ học bên trong sâu hơn quan hệ lực và chuyển vị tổng thể, nhưng phép giảm chiều vẫn không phân giải hình dạng thật của tiếp xúc dây tròn, sự thay đổi xếp chặt theo tiết diện hay trường ngoài mặt phẳng.

- **Locator PDF trong trace:** Physical PDF M23:3–5; Secs.2.1–2.2; Figs.4–5; state and interface matrices (not reproduced). **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Nguồn trực tiếp cho nhận định/kiến trúc hoặc mô hình được nêu trong claim gốc; chỉ là đối chiếu khi chuyển sang MP1, không là kiểm chứng MP1.


## [14] Joint Committee for Guides in Metrology (2008), “Evaluation of measurement data — Guide to the expression of uncertainty in measurement”

**CH2-S2-R0158-A01 — mục 2.2.3.** GUM mô tả kết quả đo thông qua quan hệ giữa đại lượng cần đo và các đại lượng đầu vào [14].

- **Locator PDF trong trace:** §4.1.1, Eq. (1). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “Modelling the measurement”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0180-A01 — mục 2.2.3.** Độ phân tán giữa các lần lặp chỉ phản ánh một phần thông tin về độ không đảm bảo; GUM còn xét hiệu chỉnh, độ phân giải, các đại lượng ảnh hưởng và giả thiết của phương pháp [14].

- **Locator PDF trong trace:** §3.3.2, sources of uncertainty. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “variations in repeated observations”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0181-A01 — mục 2.2.3.** Sai số không đồng nghĩa với độ không đảm bảo [14].

- **Locator PDF trong trace:** §3.2.2, Note 2. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “They are not”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0182-A01 — mục 2.2.3.** Độ không đảm bảo mở rộng U được lập từ độ không đảm bảo chuẩn kết hợp và hệ số phủ đã nêu [14].

- **Locator PDF trong trace:** §3.3.6–3.3.7. **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “coverage factor”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S2-R0183-A01 — mục 2.2.3.** Các đại lượng dẫn xuất dùng chung kênh đầu vào không tự độc lập; hiệp phương sai có ý nghĩa phải được xét trong mô hình đo [14].

- **Locator PDF trong trace:** §5.2.1–5.2.2, Eq. (13). **Trạng thái trace:** `SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified`.
- **Excerpt/anchor đã lưu:** “Correlated input quantities”
- **Ranh giới/ghi chú:** Không suy traction cục bộ chỉ từ áp suất nguồn hoặc đáp ứng toàn cục.

**CH2-S6-R0062-A01 — mục 2.6.1.** Hướng dẫn GUM cung cấp nền tảng phương pháp để tổ chức các phép suy ra đại lượng như vậy [14].

- **Locator PDF trong trace:** {"M38-E02": "§4.1.1–4.1.5; Eqs. (1)–(2)"}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “a measurand Y is not measured directly”
- **Ranh giới/ghi chú:** DIRECT_SUPPORT chỉ cho kết quả trong hệ nguồn; chuyển sang MP1 là đối chiếu/suy luận, không trực tiếp kiểm chứng MP1.

**CH2-S6-R0132-A01 — mục 2.6.2.** Theo hướng dẫn GUM, cần nhận diện mô hình phép đo, các đầu vào và ảnh hưởng đáng kể; khi đầu vào tương quan, phép lan truyền độ không đảm bảo phải tính đến hiệp phương sai [14].

- **Locator PDF trong trace:** {"M38-E02": ["§4.1.1–4.1.5; Eqs.(1)–(2)"], "M38-E03": ["§5.1.2 Eq.(10); §5.2.2 Eq.(13)"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “measurand Y is represented as a function of input quantities; combined standard uncertainty”
- **Ranh giới/ghi chú:** Nguồn journal hỗ trợ điều kiện/kết quả của chính hệ nguồn. Giới hạn do phương pháp/chuyển giao là suy luận, không direct proof MP1.

**CH2-S6-R0192-A01 — mục 2.6.3.** GUM yêu cầu xác định mô hình phép đo, các đầu vào và ảnh hưởng đáng kể, đồng thời giữ đóng góp của hiệp phương sai khi đầu vào tương quan; khoảng bất định mở rộng còn cần hệ số phủ và cách diễn giải thích hợp [14].

- **Locator PDF trong trace:** {"M38-E02": ["§4.1.1–4.1.3; Eq.(1) is not reproduced"], "M38-E03": ["§5.1.2; §5.2.2; Eqs.(10)/(13) not reproduced"], "M38-E04": ["§6.2.1–6.3.3; Eq.(18) not reproduced"]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Excerpt/anchor đã lưu:** “functional relationship; correlated; coverage factor”
- **Ranh giới/ghi chú:** Vai trò theo claim: source finding của chính hệ nguồn khác comparator/đặt câu hỏi MP1. P3 là định nghĩa/quyết định nội bộ, không kết quả journal.

**CH2-S6-R0228-A01 — mục 2.6.4.** Theo GUM, độ lặp lại gắn với các phép đo liên tiếp của cùng đại lượng trong những điều kiện đo giống nhau; đánh giá dưới điều kiện thay đổi cần khai báo những điều kiện đã thay đổi [14].

- **Locator PDF trong trace:** {"M38-E01":[{"physical_pages":[13],"printed_pages":["1"],"exact_locator":"§1 Scope","anchor":"general rules"},{"physical_pages":[47],"printed_pages":["35"],"exact_locator":"Annex B.2.15–B.2.16","anchor":"same conditions of measurement","ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD":true}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

**CH2-S6-R0231-A01 — mục 2.6.4.** GUM yêu cầu mô hình phép đo thể hiện các đại lượng đầu vào có liên quan và xem xét tương quan khi truyền độ không đảm bảo đo [14].

- **Locator PDF trong trace:** {"M38-E02":[{"physical_pages":[20,21],"printed_pages":["8","9"],"exact_locator":"§4.1.1–4.1.3 model of measurement; Eq.(1)","anchor":"mathematical model"},{"physical_pages":[14],"printed_pages":["2"],"exact_locator":"§2.2.3 uncertainty definition","ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD":true}],"M38-E03":[{"physical_pages":[31,33],"printed_pages":["19","21"],"exact_locator":"§5.1.2 and §5.2.2 covariance/correlated inputs","anchor":"correlated"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.

**CH2-S6-R0251-A01 — mục 2.6.4.** Mô hình phép đo cần cho biết áp suất, lực, chuyển vị và độ cong tham gia vào kết quả nào, đầu vào nào được đo hay suy ra, cùng các tương quan đáng kể nếu có [14].

- **Locator PDF trong trace:** {"M38-E02":[{"physical_pages":[20,21],"printed_pages":["8","9"],"exact_locator":"§4.1.1–4.1.3 model of measurement; Eq.(1)","anchor":"mathematical model"},{"physical_pages":[14],"printed_pages":["2"],"exact_locator":"§2.2.3 uncertainty definition","ADDITIONAL_FRAGMENT_NOT_IN_ORIGINAL_RECORD":true}],"M38-E03":[{"physical_pages":[31,33],"printed_pages":["19","21"],"exact_locator":"§5.1.2 and §5.2.2 covariance/correlated inputs","anchor":"correlated"}]}. **Trạng thái trace:** `DIRECT_PDF_VERIFIED`.
- **Tóm tắt/ghi chú nguồn đã lưu:** “CSV chỉ lưu finding tóm tắt, không lưu quote anchor.”
- **Ranh giới/ghi chú:** Vai trò áp dụng cho claim: kết quả của hệ nguồn; comparator cho MP1; GUM là phương pháp. Nguồn nội bộ chỉ yêu cầu/định nghĩa, không kết quả journal.


## [15] Y. Fan, B. Yi & D. Liu (2024), “An overview of stiffening approaches for continuum robots”

**CH2-S3-R0001-A01 — mục Abstract / Introduction; classification context.** Trong robot mềm và robot liên tục, điều chỉnh độ cứng là thay đổi khả năng chống lại biến dạng trong khi vẫn duy trì một mức độ mềm dẻo cần thiết cho chuyển động. Ở tầng nguyên lý cấp cao, các tổng quan phân biệt những cách tạo lực đối kháng, thay đổi tính chất vật liệu, và thay đổi ràng buộc hoặc cấu hình cơ khí [15]. Ở tầng kiến trúc, các cơ chế kẹt cơ học (jamming) được phân chia theo môi trường tiếp xúc như sợi, dây, lớp/tấm hoặc hạt. Vì vậy, khóa bằng ma sát là một cơ chế ràng buộc có thể xuất hiện trong nhiều kiến trúc, chứ không phải một nhóm đồng cấp loại trừ các kiến trúc kẹt cơ học. Đối với bó dây TiNi, vật liệu dây, hình thái tiếp xúc, đường truyền tải nén và trạng thái biến dạng của từng dây cần được xem xét riêng.

- **Locator PDF trong trace:** Fig. 1; Table 1 context. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** M05 cung cấp taxonomy cấp hệ thống; việc tách tầng nguyên lý khỏi kiến trúc jamming là tổng hợp biên tập.

**CH2-S3-R0010-A01 — mục Classification context; Section 2; Section 2.2; Design.** Trong robot mềm và robot liên tục, điều chỉnh độ cứng là thay đổi khả năng chống lại biến dạng trong khi vẫn duy trì một mức độ mềm dẻo cần thiết cho chuyển động. Ở tầng nguyên lý cấp cao, các tổng quan phân biệt những cách tạo lực đối kháng, thay đổi tính chất vật liệu, và thay đổi ràng buộc hoặc cấu hình cơ khí [15]. Ở tầng kiến trúc, các cơ chế kẹt cơ học (jamming) được phân chia theo môi trường tiếp xúc như sợi, dây, lớp/tấm hoặc hạt. Vì vậy, khóa bằng ma sát là một cơ chế ràng buộc có thể xuất hiện trong nhiều kiến trúc, chứ không phải một nhóm đồng cấp loại trừ các kiến trúc kẹt cơ học. Đối với bó dây TiNi, vật liệu dây, hình thái tiếp xúc, đường truyền tải nén và trạng thái biến dạng của từng dây cần được xem xét riêng.

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0010-A02 — mục Classification context; Section 2; Section 2.2; Design.** Nguyên lý cấp caoTạo lực đối khángCơ cấu hoặc cơ cấu chấp hành tạo lực chống lại tải ngoài.Gân kéo (tendon), truyền động chất lưu (fluidic) hoặc cơ cấu tương tự.Không xác định giao diện tiếp xúc của bó TiNi.[15]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S3-R0010-A03 — mục Classification context; Section 2; Section 2.2; Design.** Nguyên lý cấp caoVật liệu đáp ứng nhiệtThay đổi trạng thái hoặc đặc tính vật liệu để thay đổi độ cứng của kết cấu.Gia nhiệt và làm nguội.Động học nhiệt và trạng thái TiNi của MP1 chưa được xác định ở đây.[15]

- **Locator PDF trong trace:** Fig. 1/Table 1 context; Fig. 2; Fig. 2; Fig. 1. **Trạng thái trace:** `INFERENCE`.
- **Ranh giới/ghi chú:** Bảng là tổng hợp biên tập; các nguồn không tuyên bố cùng một sơ đồ hai tầng cho MP1.

**CH2-S5-R0079-A01 — mục §2.5.5.** Nguồn tổng quan của Fan và cộng sự phân loại kẹt sợi (fibre/filament jamming) theo cơ chế hình thái: các sợi xếp dọc trục trong vỏ kín khí, độ cứng hiệu dụng thay đổi khi ma sát giữa các sợi thay đổi dưới tác dụng hút chân không. Bài báo đặt cơ chế này cạnh kẹt hạt, kẹt lớp và các dạng lai; Hình 5(g) và Bảng 4 mô tả vị trí của kẹt sợi trong hệ phân loại [15]. Giá trị của nguồn đối với MP1 là xác định không gian kiến trúc và cơ chế ở cấp độ khái quát. Đây không phải là mô hình dự đoán lực pháp tuyến cục bộ, cũng không cung cấp một quan hệ đã kiểm chứng giữa áp suất nguồn và lực tiếp xúc trong bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.10, Sec. 3.3.1, Fig. 5(g); Table 4 p.11. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** No local normal-force law or MP1 contact topology

**CH2-S5-R0080-A01 — mục §2.5.5.** Nguồn tổng quan của Fan và cộng sự phân loại kẹt sợi (fibre/filament jamming) theo cơ chế hình thái: các sợi xếp dọc trục trong vỏ kín khí, độ cứng hiệu dụng thay đổi khi ma sát giữa các sợi thay đổi dưới tác dụng hút chân không. Bài báo đặt cơ chế này cạnh kẹt hạt, kẹt lớp và các dạng lai; Hình 5(g) và Bảng 4 mô tả vị trí của kẹt sợi trong hệ phân loại [15]. Giá trị của nguồn đối với MP1 là xác định không gian kiến trúc và cơ chế ở cấp độ khái quát. Đây không phải là mô hình dự đoán lực pháp tuyến cục bộ, cũng không cung cấp một quan hệ đã kiểm chứng giữa áp suất nguồn và lực tiếp xúc trong bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.10–11, Sec. 3.3.1 and Table 4. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Cannot validate MP1 model accuracy

**CH2-S5-R0098-A01 — mục §2.5.5.** Nguồn tổng quan của Fan và cộng sự phân loại kẹt sợi (fibre/filament jamming) theo cơ chế hình thái: các sợi xếp dọc trục trong vỏ kín khí, độ cứng hiệu dụng thay đổi khi ma sát giữa các sợi thay đổi dưới tác dụng hút chân không. Bài báo đặt cơ chế này cạnh kẹt hạt, kẹt lớp và các dạng lai; Hình 5(g) và Bảng 4 mô tả vị trí của kẹt sợi trong hệ phân loại [15]. Giá trị của nguồn đối với MP1 là xác định không gian kiến trúc và cơ chế ở cấp độ khái quát. Đây không phải là mô hình dự đoán lực pháp tuyến cục bộ, cũng không cung cấp một quan hệ đã kiểm chứng giữa áp suất nguồn và lực tiếp xúc trong bó dây TiNi.

- **Locator PDF trong trace:** PDF physical p.10–11; locator issue record. **Trạng thái trace:** `VERIFIED_FULL_TEXT`.
- **Ranh giới/ghi chú:** Legacy locator retained only in provenance, not manuscript

## Nhận xét audit [11]–[15]

- **[11] Zhang et al. (2025)** là nguồn gần nhất trong nhóm này với các claim về continuum layer-jamming; trace dẫn tới phần mô hình, trạng thái tăng tải/trượt/dỡ tải và các đối chiếu/giới hạn. Các ý về giả thiết lớp mỏng, số lớp, sai khác biên và vùng trượt cần được đối chiếu nguyên văn trước khi dùng để kết luận phạm vi hiệu lực.
- **[12] Caro & Carmichael** là bài tổng quan; các claim dùng nó cho cơ chế chân không và phân loại là evidence cấp review, không phải xác minh độc lập các kết quả nghiên cứu gốc.
- **[13] Zhang et al. (2021)** hỗ trợ mô hình cáp nhiều dây có tương tác/trượt, nhưng mô hình và hiệu chuẩn của bài cần được giữ đúng phạm vi; `k` không được đồng nhất với hệ số ma sát Coulomb hoặc áp suất tiếp xúc.
- **[14] GUM** là chuẩn hướng dẫn đo lường. Trace có cả trang vật lý và trang in ở một số dòng; phải phân biệt hai hệ số trang khi đối chiếu. Đây không phải bằng chứng cơ học cho cấu hình MP1.
- **[15] Fan et al.** là tổng quan phân loại phương pháp tăng cứng; hữu ích cho phân loại và thuật ngữ, không phải bằng chứng thực nghiệm cụ thể cho bó dây TiNi.
- Năm PDF có trong thư mục đóng gói. Trace cho [11], [12], [13], [15] thường chỉ rõ mục/hình; riêng một số claim [14] ghi physical page và printed page. Phần này vẫn chưa tái trích xuất nguyên văn từng claim từ PDF, nên excerpt giữ trạng thái “locator/anchor trong trace” như hai phần trước.


---

