# Kiểm tra bảy cổng chấp nhận §2.4.4

TASK_ID: MP1-CH2-2.4.4-RESEARCH-THESIS-DRAFT  
Ngày hoàn tất: 18/10/2026, Asia/Bangkok  
Vai trò quyết định khoa học: ROOT B  
Kết quả: **PARTIAL_WITH_FINDINGS**  
WORD_RENDER_VALIDATION: **NOT_VERIFIED**

Phạm vi là một mục tổng quan của luận văn Thạc sĩ Kỹ thuật Cơ khí, định hướng nghiên cứu chuyên sâu, Khoa Cơ khí, Trường Đại học Bách khoa, Đại học Quốc gia Thành phố Hồ Chí Minh. Ba PDF do dự án cung cấp là cơ sở kiểm tra. Không thực hiện tìm kiếm tài liệu mới. Bản thảo không xác lập thiết kế piston, môi chất, hình học kín, thông số phớt hoặc quy trình Bench B.

## Quy ước bằng chứng và chấp nhận

`VERIFIED FULL TEXT` chỉ việc đã đối chiếu nhận định với PDF gốc và locator được ghi; không có nghĩa mọi kết quả của bài báo đã được tái lập. `INFERENCE` là diễn giải xuyên kiến trúc hoặc định nghĩa cơ học biên tập. `AUTHOR_PROPOSAL` là yêu cầu thông tin cần có trong nghiên cứu tương lai. `DOCUMENT_COVERAGE` chỉ kiểm tra đề cương. Không dùng metadata để thay cho kiểm tra cơ chế hoặc phương trình. Các trường metadata được đối chiếu trang đầu PDF và registry địa phương, không tra cơ sở dữ liệu ngoài.

| Cổng | Quyết định ROOT | Bằng chứng và giới hạn |
|---|---|---|
| 1. Tuân thủ đề cương | PASS, có giới hạn nguồn | B01 bao phủ ba kiến trúc tạo áp; B02 bao phủ lực, hành trình, nhiệt độ, thể tích, ma sát phớt, độ mềm, rò, quá độ và nguội. Yếu tố không được đo riêng được ghi là yếu tố kỹ thuật cần xét. Không viết §2.4.3, §2.5 hoặc thiết kế Bench B. |
| 2. Truy xuất nhận định | PASS trong phạm vi kiểm tra | 39 dòng có loại nhận định, vai trò, locator, biến/đơn vị, điều kiện và giới hạn chuyển giao. Bốn Evidence ID được giữ đúng ánh xạ. Các dòng đề cương không tính như kết quả nghiên cứu. Những nhận định kỹ thuật biên tập không giả nhận locator như dữ liệu thực nghiệm. |
| 3. PDF và phương trình | PASS trong phạm vi được nêu | Ba PDF gốc được mở; ROOT kiểm tra ảnh trang 3 của M33 và các dạng (1)–(4). Chỉ (1) vào DOCX. Không mở rộng trạng thái kiểm chứng sang các nhóm phương trình khác. Các số dùng trong bản thảo được đối chiếu phần kết quả gốc. |
| 4. Tổng hợp khoa học | PASS | So sánh cùng trục cơ học: kích hoạt, biên chuyển động, đường truyền lực/áp suất, đại lượng đo/dự báo và miền áp dụng. Bảng phân biệt ECF, SMA ướt và lò xo NiTi–vỏ silicone; phần sau phân tích điều kiện chung và giới hạn. |
| 5. Giới hạn cơ học | PASS | Tách ba cấp áp suất/tiếp xúc, lực với áp suất, lưu lượng với áp suất, hành trình tự do với chịu tải, lực khóa với điểm làm việc. Không suy hệ số ma sát hoặc đường áp suất–độ cứng MP1; topology, môi chất, nhiệt và quy trình còn mở. |
| 6. Trích dẫn và metadata | PASS, hòa giải năm xuất bản | Ba DOI tương ứng ba danh tính duy nhất, xuất hiện theo [1], [2], [3]; mọi tài liệu được dẫn. M33 dùng số báo 2013 và giữ ngày online 20/8/2012. Không sửa WEP/registry. |
| 7. Tiếng Việt và Word | PARTIAL | Nội dung khoa học tiếng Việt, thuật ngữ đã duyệt; bảng và phương trình Word sửa được; ZIP/XML đạt các kiểm tra nêu dưới. Chưa xác minh độ dễ đọc trên từng trang, trang trắng hoặc mục thuật ngữ đơn lẻ vì không có bộ kết xuất Word. |

Phần khoa học và cấu trúc tĩnh của cổng 7 đạt yêu cầu kiểm tra hiện có. Quyết định PARTIAL bảo lưu các yêu cầu trình bày cần nhìn trang thực. Chấp nhận kết xuất được báo riêng, không suy từ việc ZIP/XML hợp lệ.

## Phê duyệt lập luận trước khi soạn

ROOT duyệt chuỗi lập luận trước lượt viết: bắt đầu bằng các bước chuyển đổi nhiệt–cơ–lưu chất; dùng Huynh để tách chức năng áp suất; dùng Pierce–Mascaro cho dòng duy trì và điều kiện khả thi; dùng Kotb–Elgamal–Serry cho tương tác lực của lò xo với vỏ; sau đó so sánh trên cùng cơ sở lực/hành trình/thể tích/áp suất. Phần cuối chỉ nêu các nhu cầu nhận dạng và kiểm chứng độc lập, không chốt phần cứng hay suy tính mới. Khi hòa giải báo cáo worker, ROOT giữ M33-E01 cho kiến trúc/kết quả, M33-E02 cho §III.A và (1)–(4), bất kể tiêu đề phân nhóm rộng của báo cáo làm việc.

## Kiểm toán M12: áp suất âm và dương

**Nguồn:** Huy Hoang Huynh, Dong Han, Kazuhiro Yoshida, Michael De Volder, Joon-wan Kim, *Soft actuator with switchable stiffness using a micropump-activated jamming system*, Sensors and Actuators A: Physical, 338, 113449, 2022. DOI: [10.1016/j.sna.2022.113449](https://doi.org/10.1016/j.sna.2022.113449).

**PDF gốc:** `data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf`. Evidence gốc M12-E01: trang vật lý 3, khái niệm, Hình 2–3. Kiểm tra bổ sung cơ chế ở trang 2–4 và đo lường ở trang 6–9. Worker nhìn ảnh các trang 1, 2, 3, 7, 8, 9; ROOT nhìn ảnh trang 3. Tài liệu đã được trích văn bản toàn bộ để định vị.

`SOURCE_REPORTED`: ECF tạo dòng bằng điện trường qua điện cực; cơ cấu PDMS chứa hạt nhôm oxit. Áp suất âm dùng cho kẹt hạt; áp suất dương làm phồng để uốn. Đây không phải bơm SMA. Nguồn không chứng minh hai chức năng được điều khiển độc lập đồng thời ở một độ cong cố định.

Áp suất của vi bơm được khảo sát riêng với phép thử không dòng; lưu lượng ở điều kiện không tải là phép thử khác, không phải hai cực đại đồng thời. §4.2 và Hình 11, trang 7–8, báo lực 0,134→0,743 N tại độ dịch 3 mm, tốc độ 0,5 mm/s, mức áp suất danh định −50 kPa. Áp suất trong cơ cấu đã lắp không được đo trực tiếp; các nhãn được gán từ đặc tính bơm riêng. Vì vậy bản thảo không gọi đây là phép đo áp suất tại khoang tích hợp hay định luật tiếp xúc.

**Khác biệt cần giữ:** abstract trang 1 ghép mức ±55 kPa với kết quả, trong khi phần thử và kết luận dùng ±50 kPa; khả năng bơm riêng xấp xỉ 55 kPa. Bản thảo chọn số của phép thử thân bài và giữ sai biệt ở hồ sơ này. Tỷ số 5,5 là tỷ số lực tại cùng độ dịch, không phải E hoặc EI đã nhận dạng. Mốc áp suất và cấu hình cổng tham chiếu cảm biến chưa được mô tả đầy đủ; không chuyển nhãn âm sang áp suất tuyệt đối. Kênh PDMS giãn và bất đối xứng hai chiều được nêu ở §4.1, trang 6–7. Không gán dữ liệu nhiệt/chuyển pha SMA cho ECF.

## Kiểm toán M33: cơ cấu, phương trình và thứ nguyên

**Nguồn:** Matthew D. Pierce, Stephen A. Mascaro, *A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump*, IEEE/ASME Transactions on Mechatronics, 18(2), 536–546, tháng 4/2013. DOI: [10.1109/TMECH.2012.2211032](https://doi.org/10.1109/TMECH.2012.2211032).

**PDF gốc:** `data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf`. M33-E01: trang vật lý 1, trang in 536, abstract/§I; M33-E02: trang vật lý 3, trang in 538, §III.A, (1)–(4). Worker đọc văn bản trang 1–10, nhìn ảnh trang 2, 3, 8, 10. ROOT độc lập nhìn ảnh trang 3 và 10, kiểm tra văn bản các phần khái niệm, khả thi và kết quả. Metadata trang đầu và trang cuối xác nhận dải trang 536–546. Trong DOCX, locator trích dẫn M33 dùng trang in, còn CSV ghi trang vật lý.

**Kiến trúc:** dây SMA trong ống mềm có chất lưu trao đổi nhiệt trực tiếp. Nước nóng/lạnh được định tuyến qua cơ cấu, xả về bể áp thấp, rồi bơm lại vào bình tích áp nhờ buồng bơm và van một chiều. Hai hệ nóng/lạnh dùng đòn bẩy chung. Nguồn gọi đây là bơm màng thể tích kiểu tịnh tiến; mô hình cũng có biến vị trí/diện tích piston. Giữ cả hai mô tả không có nghĩa thiết bị tương đương piston MP1. Hệ cần cấp nhiệt và quản lý phía lạnh, có trợ nhiệt Joule và van điều khiển; hồi tiếp dòng không đồng nghĩa tự chủ năng lượng.

### Bản gốc của (1)–(4), đã kiểm tra trực tiếp

Các số dưới đây là số phương trình của bài báo, không phải số luận văn.

| Phương trình nguồn, trang vật lý 3 | Đại lượng và vai trò | Kiểm tra thứ nguyên | Quyết định đưa vào DOCX |
|---|---|---|---|
| (1) `Q_out ≥ Q_in` | So lưu lượng bơm ra với lưu lượng dùng để duy trì cơ cấu SMA nội bộ. | Hai vế m³/s trên cùng cơ sở thời gian. | Có, một OMML sửa được, giữ dấu ≥ và chỉ số dưới. |
| (2) `Q_out = (N_p σ A_w ε L)/(P C t_f)` | Biểu thức khả thi theo công/công suất SMA, áp suất bình tích và thời gian. | Tử Pa·m²·m = J; mẫu Pa·s; kết quả m³/s. | Bỏ, quá đặc thù cấu hình và không cần cho lập luận. |
| (3) `Q_in = (N A_f L)/t_f` | Lưu lượng cần đưa qua các cơ cấu SMA ướt theo hình học/thời gian. | m²·m/s = m³/s. | Bỏ, định nghĩa dòng duy trì đã đủ. |
| (4) `A_f/A_w ≤ (N_p σ ε)/(N C P)` | Ràng buộc diện tích từ (1)–(3) với đại lượng dương; điều kiện cần. | Hai vế không thứ nguyên; σ/P là tỷ số áp suất. | Bỏ, không phải quan hệ áp suất–ma sát và không phải điều kiện đủ. |

`A_w` là tiết diện dây, `A_f` là tiết diện dòng trong cơ cấu, đơn vị m²; `N_p` là số cơ cấu đang co, `N` là tổng số cơ cấu, không thứ nguyên; `σ` là cường độ chấp hành của dây SMA, Pa; `ε` là biến dạng dây, không thứ nguyên; `L` là chiều dài cơ cấu, m; `P` là áp suất bình tích, Pa; `t_f` là thời gian lan truyền chất lưu, s; `t_b` là thời gian co, s; `C=t_b/t_f>1` là tỷ số thời gian. Đơn vị SI ở đây là kiểm tra nhất quán của ROOT, không phải số đo mới.

**Điều kiện và diễn giải:** phân tích khả thi dựa trên hình học, sức chấp hành và thời gian của hệ SMA ướt. Sự chuyển từ công lý tưởng sang lưu lượng trong (2) chưa chứa một hiệu suất đã đo hoặc đường bơm nhận dạng. Nguồn về sau nêu giả định co đầy đủ và không mất thể tích khi tính cực đại ở (11), trang vật lý 4; không tự động gán giá trị cực đại này cho vận hành thực. Tác giả nói ràng buộc diện tích chưa đủ bảo đảm toàn hệ hoạt động: còn yêu cầu nhiệt, thời gian và tổn thất. Không có phương trình nào trong bốn phương trình xác định phân bố tải pháp tuyến của mẫu.

`Q_out` được hiểu là đầu ra trước khi trừ phần dùng nội bộ theo cấu trúc hồi tiếp và định nghĩa nguồn; diễn giải “toàn phần/thuần” được ghi riêng là `INFERENCE` trong CSV. `Q_in` không phải lưu lượng hút thông thường của một buồng bơm độc lập. Dấu bằng cho phép phần dư bằng không; để cấp phần dư dương cần lớn hơn nghiêm ngặt. Không đồng nhất 66 mL/phút với `Q_out`, không suy các dòng thành phần chưa được công bố và không coi tỷ số 2,1 là hiệu suất.

**Bằng chứng thực nghiệm tương ứng:** trang vật lý 9, trang in 544, nêu cực đại 0,88 khi chỉ dùng chất lưu và 1,54 khi trợ điện trước bước bổ sung nhiệt liên tục. Trang vật lý 10, trang in 545, §V.C/Hình 12–13, báo 2,1 với cơ cấu 40 cm, thời gian dòng 1,5 s, trợ điện và bổ sung nhiệt vào bình nóng; 66 mL/phút là khả năng thuần do tác giả báo cáo cho cấu hình điện đó. Không thấy dụng cụ/độ không đảm bảo riêng cho giá trị 66 trong phần được kiểm tra. Các phép thử toàn hệ không phải nhận dạng thực nghiệm độc lập từng vế của (2)–(4).

Bảng II cho bối cảnh cơ sở 15 kPa ở bình tích, 88 °C nước nóng và 25 °C nước lạnh, nhưng kết quả cực đại sau bổ sung nhiệt không tái khai báo riêng đầy đủ nhiệt độ/áp suất thực. Bản thảo không gán 88 °C cho cực đại 2,1. Mốc gauge/absolute và vị trí cảm biến chưa rõ trong các đoạn khảo sát; không đưa một giá trị bình tích thành áp suất tại mẫu. Không dùng hằng số thời gian nguồn cho MP1.

**Giới hạn nhóm phương trình:** chỉ (1)–(4) được ROOT kiểm tra mục tiêu ở lần này; các nhóm khác không mang trạng thái kiểm chứng tự động. Worker ghi nhận một dấu hiệu ngoài phạm vi: mẫu số (8) trên trang 3 không có hệ số 4 trong khi (9) có `4 k_f Nu`. Đây là sai biệt hệ số đại số có thể quan sát, không phải sai thứ nguyên của (1)–(4); không sửa ngầm, không dùng hay tuyên bố đã kiểm toán toàn nhóm nhiệt.

**Metadata:** trang 1 ghi date of publication 20/8/2012, current version 10/1/2013; đầu trang ghi số tháng 4/2013. DOI chứa 2012 và registry/WEP dùng 2012, nhưng năm số báo là 2013. Bản thảo dùng 2013 cùng ghi chú ngày online; không suy năm từ tên tệp hay DOI, không sửa dữ liệu chung.

## Kiểm toán M34 và so sánh với M33

**Nguồn:** Youssef Kotb, Islam Elgamal, Mohamed Serry, *Shape Memory Alloy Capsule Micropump for Drug Delivery Applications*, Micromachines, 12, 520, 2021. DOI: [10.3390/mi12050520](https://doi.org/10.3390/mi12050520).

**PDF gốc:** `data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf`. M34-E02: trang vật lý 3, §§2.1–2.2, Hình 1. Đối chiếu thêm trang 4–5 cho giả định và vỏ, trang 8–12 cho phép thử và nhiệt; worker nhìn ảnh trang 3, ROOT nhìn ảnh trang 3 và kiểm tra văn bản trang 12.

Lò xo NiTi gia nhiệt Joule cuốn trên vỏ mềm. Gia nhiệt làm co và đẩy lưu chất qua van; ngắt điện/làm nguội cho vỏ tạo lực hồi, kéo giãn lò xo và nạp lại. Nguồn quy áp suất nén cực đại cho chênh lực giữa cuộn austenit và vỏ, nhưng không định nghĩa phương trình chênh lực có dấu. Việc coi lực cuộn thắng lực vỏ là diễn giải chiều nén, không phải công thức mới của nguồn. Tại giao điểm đường lực–chuyển vị, các lực bằng nhau theo mô tả cân bằng; không áp chênh lực khác không vào chính điểm ấy và không coi chênh lực hằng số.

Mô hình §3 chỉ cần hai đầu hành trình, giả định pha đầu mút 100%, bỏ ảnh hưởng lưu chất ở hai đầu tĩnh và dùng đường silicone đo thực nghiệm, gần tuyến tính trong miền làm việc. Các giả định này không chứng minh bỏ tải lưu chất trong toàn bộ lúc nén. Hình 1 là sơ đồ nguyên lý lực–chuyển vị; số đo/đặc tính mô hình ở phần sau có vai trò khác. Không sao chép hình hay phương trình lò xo vào luận văn.

§5.5, trang 12, Hình 12: bơm ba vòng có thể tích đẩy mục tiêu 43 mm³, dòng cực đại 790 mA, áp suất cột áp tĩnh báo cáo 6,5 kPa theo chu kỳ. Bản thảo không gọi đây là áp tại tiếp xúc; không tự chỉ định vị trí cảm biến, mốc áp hay nhận dạng chất lưu thử là nước. Mức 14 kPa/7,1 W của abstract không cần cho lập luận nên không đưa vào bản thảo.

**Khác M33:** SMA ướt trao đổi nhiệt bằng dòng nóng/lạnh, thông qua đòn bẩy tới buồng bơm; capsule dùng lò xo NiTi gia nhiệt điện và chính vỏ mềm hồi vị. Chỉ so sánh được chức năng chuyển lực/hành trình/thể tích, không cộng gộp lưu lượng hoặc so hiệu suất như cùng tải. Cả hai đều không kiểm chứng piston MP1.

## Lực–hành trình–nhiệt độ và ba cấp áp suất

Hành trình tự do, lực khóa khi chặn chuyển vị và hành trình chịu tải là định nghĩa biên tập, không giả nhận là ba phép đo nguồn đã thực hiện cho MP1. Cực đại lực và hành trình không tự đồng thời khả dụng. Với piston giả định, đổi chênh áp thành lực cần diện tích hữu hiệu, hai phía áp suất, lực hồi/cản và giả định gần tĩnh; thể tích quét hình học chưa đồng nhất thể tích đến mẫu. Không tạo phương trình MP1 mới.

Tách áp suất nguồn/buồng tạo áp, áp suất tại mẫu và ứng suất tiếp xúc pháp tuyến. Ứng suất tiếp xúc có đơn vị Pa nhưng khác lực pháp tuyến N; còn phụ thuộc hình học giao diện, diện tích thực và phản lực. Không suy duy nhất tải cục bộ hoặc hệ số ma sát không thứ nguyên từ áp suất toàn cục/đường uốn. Độ dốc lực–độ võng N/m khác EI N·m². Nhiệt của SMA tạo áp và trạng thái vật liệu bó TiNi chịu uốn là hai vấn đề riêng. Trễ nhiệt/chuyển pha không đồng nhất trễ ma sát, thời gian chuyển pha không đồng nhất đáp ứng dòng/áp suất.

## Phớt, độ mềm, rò rỉ và quá độ chưa xác định

| Yếu tố | Vai trò bằng chứng | Điều không được khẳng định |
|---|---|---|
| Độ mềm kênh PDMS và khác biệt hai chiều bơm | SOURCE_REPORTED, M12 §4.1, trang 6–7 | Không phải compliance MP1 đã nhận dạng. |
| Độ mềm vỏ silicone | SOURCE_REPORTED, M34 §3, trang 4–5; đặc tính đo và xấp xỉ tuyến tính trong miền làm việc | Không phải thành buồng cứng; không cố định ở mọi biến dạng. |
| Áp suất bình tích, cấp dòng, trao đổi nhiệt | SOURCE_REPORTED, M33 §III, trang 3; kết quả trang 9–10 | Không cung cấp chu kỳ vận hành MP1. |
| Làm nguội và đánh đổi hành trình/lưu lượng | SOURCE_REPORTED, M34 §5.2, trang 9–10 | Không gán hằng số nhiệt/áp suất hoặc bảo đảm tăng làm nguội luôn tăng đầu ra. |
| Van lá tiền ép hạn chế rò | SOURCE_REPORTED về nguyên lý thiết kế, M34 §2.3, trang 4 | Không có suất rò định lượng hay hệ số phớt piston. Thể tích chết không phải độ kín. |
| Ma sát phớt, độ rơ, hành trình mất | ENGINEERING_CONSIDERATION | Phụ thuộc cấu hình tương lai; chưa được đo cho MP1 trong ba nguồn. |
| Nén được của lưu chất, rò hệ, sức cản đường dẫn, tích trữ thể tích và quá độ áp suất | ENGINEERING_CONSIDERATION | Không ấn định môi chất, hệ số, đường truyền hoặc thời hằng chưa có dữ liệu. |

Nhu cầu xem xét nhiệt/điện, lực/hành trình, vị trí đo áp, độ kín/độ mềm và đáp ứng uốn là `AUTHOR_PROPOSAL`, không phải protocol được duyệt. Hiệu chuẩn phép đo khác hiệu chỉnh mô hình; kiểm chứng độc lập cần dữ liệu không tham gia hiệu chỉnh cùng miền áp dụng và bất định. Không chọn cảm biến, tiết diện piston, phớt hay bộ điều áp.

## Trích dẫn, thuật ngữ và kiểm tra Word

Thứ tự xuất hiện [1] Huynh, [2] Pierce–Mascaro, [3] Kotb–Elgamal–Serry. Có đúng ba mục tài liệu tham khảo, ba DOI duy nhất, cả ba đều được dùng trong phần văn bản và bảng. Các thuật ngữ nguồn trong phụ lục có dẫn tương ứng; định nghĩa kỹ thuật chung được ghi “Tổng hợp biên soạn”, không gán thành phát biểu nguyên văn của nguồn. Có 30 mục, toàn bộ nhãn tiếng Việt xuất hiện trong phần văn bản đã duyệt. CSV giữ locator đầy đủ và trạng thái duyệt. Tiếng Anh chỉ ở cột song ngữ được yêu cầu, tên nguồn và ký hiệu/viết tắt khoa học.

DOCX là ZIP hợp lệ, A4 dọc 11906×16838 twip, lề 2,3 cm. Times New Roman, thân 12 pt, tiêu đề chính Heading 1 14 pt, tiêu đề phụ Heading 2 12 pt; bảng 9,5 pt. Hai bảng Word gốc gồm bảng so sánh 6 cột, 4 hàng và phụ lục 5 cột, 31 hàng. Cả 35 hàng có cantSplit; hai hàng tiêu đề lặp; chú thích bảng đặt trước bảng. Một OMML chứa hai cấu trúc chỉ số dưới, giữ dấu ≥; định nghĩa và glossary có chỉ số Word gốc. Ba đoạn tham khảo giữ nguyên đoạn; có trường số trang. Chỉ một ngắt trang chủ động trước phụ lục; không phát hiện chuỗi ngắt trang chủ động trùng. Không có Paper ID/Evidence ID hay mã quy trình trong nội dung DOCX.

Các kiểm tra trên **không xác nhận** số trang thực, trang trắng do phân trang, tràn bảng hoặc một mục thuật ngữ đứng riêng. Không có `libreoffice`/`soffice` trong môi trường; `pdftoppm` chỉ có thể đọc PDF đã kết xuất và không thay thế bộ kết xuất DOCX. Không cài thêm phần mềm để giả tạo trạng thái PASS. Không tuyên bố đúng mẫu chính thức HCMUT khi chưa có template chính thức.

## QA độc lập và xử lý phát hiện

Worker QA đối chiếu lại ảnh M33 trang vật lý3, M34 trang3 và M12 trang8, cùng bản thảo, thuật ngữ và ZIP/XML. Kết quả nội dung/cấu trúc tĩnh không còn phát hiện bắt buộc phải sửa trong phạm vi này. Hai điểm hồ sơ được xử lý cụ thể:

1. Đề xuất đảo Evidence ID của phương trình và kết quả M33 bị ROOT bác bỏ với trạng thái `REJECTED_CANONICAL_RECORD_AUTHORITY`. Nguyên nhân là tiêu đề phân nhóm trong báo cáo tạm M33 đã đảo nhãn. JSONL gốc `WP-D/EVIDENCE_RECORDS.jsonl`, dòng17–18, và ma trận mục2.4.4-A02/A04 xác nhận E01 là kiến trúc/abstract/kết quả trang1, E02 là phương trình trang3. QA đã đọc lại các nguồn có thẩm quyền và rút phát hiện. CSV giữ ánh xạ đúng; không sửa record gốc theo tiêu đề worker.
2. Góp ý locator tổng hợp lặp được chấp nhận. Cột `accepted_record_locator` đã đổi thành locator riêng của từng Evidence Record, loại bỏ bản sao do cùng gói WP-D. Cột trang/locator được kiểm tra trực tiếp ghi rõ các trang mở rộng. Hai loại locator không bị gộp thành cùng một provenance. Nhãn nguồn trong phụ lục Word dùng trang in của M33, không mang ghi chú kiểm tra PDF nội bộ.

ROOT kiểm tra lại phiên bản cuối sau các chỉnh sửa này. Worker QA không có quyền sửa DOCX; từng lượt tạo/chỉnh DOCX đều tuần tự. Chấp nhận nội dung không mở rộng sang hiệu năng hay phương trình chưa được kiểm tra.

## Kết luận chấp nhận của ROOT

Chấp nhận nội dung như một bản thảo tổng quan có giới hạn bằng chứng. Không có sai sót khoa học trọng yếu chưa xử lý trong phạm vi nguồn đã kiểm tra. Sáu cổng đầu PASS; cổng 7 PARTIAL vì yêu cầu nhìn từng trang chưa được xác minh. Cần mở/kết xuất DOCX và rà từng trang, đặc biệt bảng sáu cột và phụ lục thuật ngữ, trước khi nâng trạng thái trình bày. Không cần tìm kiếm thêm tài liệu hoặc thay đổi khoa học MP1 để hoàn tất bước bố cục này.
