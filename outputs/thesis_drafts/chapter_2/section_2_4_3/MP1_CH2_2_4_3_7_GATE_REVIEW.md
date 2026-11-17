# §2.4.3 — Rà soát bảy cổng chấp nhận

TASK_ID: MP1-CH2-2.4.3-RESEARCH-THESIS-DRAFT  
SESSION_ROLE: INDEPENDENT_ROOT_A  
STATUS: PARTIAL_WITH_FINDINGS

## Phạm vi chấp nhận

Đây là rà soát bản thảo nghiên cứu Thạc sĩ Kỹ thuật Cơ khí, Khoa Cơ khí, HCMUT–VNU-HCM. Chấp nhận tuân thủ dàn ý và diễn giải có giới hạn không đồng nghĩa mọi mắt xích cơ học đã được đo. Phần chưa xác minh khoa học được ghi là giới hạn nguồn; phần bố cục chưa nhìn trực tiếp được ghi riêng, không tạo kết quả render giả.

## Gate 1 — Tuân thủ dàn ý: PASS trong phạm vi tổng hợp có giới hạn

- B01: xác định giao diện dây ngoại vi–ống cao su trong Jeon; phân biệt lõi TPU và ống cao su riêng. Takashima là kẹt hạt kết hợp phục hồi; Matsumoto là so sánh phục hồi vật liệu/thiết bị, không được gán cùng giao diện Jeon.
- B02: đã phân tích gia nhiệt/làm nguội, siết hướng kính, lực hồi phục/lực pháp tuyến, trễ nhiệt–cơ/tiếp xúc, vận tốc/mức phục hồi và khả năng nhận dạng từ đại lượng tổng thể.
- B03: các tiền lệ SMA điều biến ma sát và hỗ trợ kẹt được thừa nhận; thay bộ chấp hành/vật liệu không tự chứng minh đóng góp khoa học mới.
- Không có nội dung hoặc phương trình tạo áp/piston của §2.4.4. Đoạn cuối chỉ chuyển tiếp sang việc tổng quan tạo và truyền áp suất.
- PASS là trạng thái đầy đủ của nội dung tổng hợp yêu cầu, không nâng bằng chứng lực pháp tuyến, hysteresis hoặc pha MP1 lên mức đã xác minh.

## Gate 2 — Truy xuất luận điểm: PASS

CSV có30 bản ghi:21 SOURCE_GROUNDED_CLAIM,5 INFERENCE,2 AUTHOR_PROPOSAL,2 DOCUMENT_COVERAGE. Không gọi30 dòng là30 phát hiện khoa học độc lập.

Bốn ánh xạ gốc đã giữ nguyên: A01→M31-E01;A02→M32-E06;A03→M37-E04;A04→M31-E02. Các Evidence ID bổ sung đều hiện hữu trong WP-D và thuộc đúng ba PDF. Mỗi dòng nguồn có đường dẫn PDF/SHA256/DOI/tiêu đề/năm, locator vật lý đã kiểm tra, provenance dòng JSONL cũ, điều kiện, giả thiết, đại lượng quan sát/suy ra và giới hạn. Lực kéo và nhiệt độ được tách khỏi lực siết/tải pháp tuyến suy luận; tương quan hồi phục không bị ghi thành quy luật nhân quả.

Các yêu cầu nhận dạng MP1 và ranh giới novelty/chuyển tiếp ở C27–C28 là AUTHOR_PROPOSAL, không có nguồn đo MP1 giả. C29–C30 chỉ là hồ sơ lựa chọn phương trình/phạm vi. Các suy luận C22–C26 được ghi rõ khác kết quả nguồn.

## Gate 3 — PDF gốc: PASS, có sai khác được đối chiếu

- M31:8 trang, pp.2–3 Fig.1/Sec.II xác nhận cấu trúc; pp.5–6 Fig.4/5, TablesI–II đo trượt/uốn; p.7 TableIII và Sec.IV.C/V đối chiếu/mặt hạn chế. Một dây được kéo5mm tại10mm/phút, mười lần mỗi cấu hình/trạng thái; số lần lặp có trong p.5 mặc dù E06 cũ ghi không nêu. Lực pháp tuyến và lực siết lò xo chưa được đo riêng.
- M32:12 trang; pp.2–4 Figs.2–6/Table1 phân biệt hai nguyên mẫu. Eq.(1) tại p.5 được kiểm tra hình thức/thứ nguyên và phép thế SMA tại p.8. Fig.15/phục hồi ở p.7; Figs.16–19 ở p.8. Không gộp số liệu33lần của SMP cho SMA; không dùng Tg của SMP cho dây SMA.
- M37:10 trang; p.3 Table1/DSC; p.4 quy trình0,5V/theo dõi đầu dây; pp.5–6 định nghĩa/so sánh/Figs.7–8; pp.7–9 thử thiết bị và luyện chu kỳ. Phân biệt dữ liệu chuyển vị với vận tốc khớp và diễn giải của tác giả. Nguồn khác nhau ở Af/nhà sản xuất/xử lý nhiệt.
- Không tìm bài mới, không số hóa đồ thị hoặc chuyển các giá trị ước lượng bằng mắt thành số chính xác. Các hình được xem phục vụ kiểm tra, không sao chép vào bản thảo.

## Gate 4 — Tổng hợp liên nghiên cứu: PASS

Bản thảo so sánh các mắt xích đo được: Jeon có lực trượt một dây bên cạnh uốn toàn thân và nhiệt độ lò xo; Takashima có hút khí, công xôn và phục hồi trong môi trường hạt; Matsumoto có hồi phục dây tự do và thiết bị với mẫu vật liệu khác nhau. Bảng2.4.3 có3dòng nguồn/6cột, không xếp hạng số liệu không tương đương. Chênh lệch thời gian không được quy riêng cho SMA khi hình học và điều kiện nhiệt khác nhau. M32/M37 cùng tuyến thiết bị kẹt hạt không bị đếm thành hai kiểm chứng độc lập của luật ma sát Jeon.

## Gate 5 — Giới hạn cơ học: PASS

Đã giữ riêng:

- Chuyển vị/lực hồi phục SMA, lực siết, lực pháp tuyến, ứng suất pháp tuyến cục bộ, lực ma sát, hệ số ma sát và giới hạn lực ma sát truyền được.
- Độ dốc lực–độ võng, EI suy ra từ công xôn và mô đun Young E; vận tốc phục hồi và độ cứng uốn.
- Kích thích nhiệt/điện, thời gian làm nóng/nguội, vòng trễ vật liệu, vòng trễ tiếp xúc và biến dạng dư. Không gọi mọi vòng trễ là dẻo.
- Nhiệt độ bộ chấp hành với nhiệt độ bó TiNi chịu tải. Truyền nhiệt chưa được đặc trưng chỉ là biến gây nhiễu cần xét, không là hiệu ứng đã đo trong MP1.
- Giao diện dây–ống cao su và dây–dây; áp suất hút trong túi với tải pháp tuyến tại giao diện. Không có luật áp suất–độ cứng hoặc SMA–ma sát phổ quát.

Hình thái tiếp xúc, packing, vật liệu, miền nhiệt/pha, observable uốn và cơ chế trội MP1 vẫn chưa quyết định. Không có thí nghiệm mới, kết luận tính mới, thông số tiếp xúc hoặc thiết kế cơ cấu được thêm.

## Gate 6 — Citation và metadata: PASS

Ánh xạ chuẩn theo lần xuất hiện đầu tiên: [1]Jeon/M31, [2]Takashima/M32, [3]Matsumoto/M37. Kiểm tra bao gồm bảng khoa học và glossary trong thứ tự XML Word. Ba tài liệu đều được trích; mọi citation số đều có mục tương ứng; glossary giữ nguồn riêng hoặc nhãn biên tập, không mang số cũ của các mục trước.

- [1] H.Jeon,Q.N.Le,S.Jeong,S.Jang,H.Jung,H.Chang,H.J.Pandya,Y.Kim; IEEE Robotics and Automation Letters7(3),6582–6589,2022; DOI10.1109/LRA.2022.3174363. Thứ tự Jung trước Chang đã kiểm tra ở PDFp.1.
- [2] K.Takashima,T.Imazawa,H.Cho; Journal of Robotics and Mechatronics34(2),466–477,2022; DOI10.20965/jrm.2022.p0466.
- [3] N.Matsumoto,H.Cho,K.Takashima,H.Suzuki; Mechanical Engineering Journal11(6),bài24-00130,2024; DOI10.1299/mej.24-00130. Không tạo dải trang tạp chí không có trong PDF.

## Gate 7 — Văn phong Thạc sĩ và tài liệu: PARTIAL ở phần bố cục trực quan

Văn xuôi tiếng Việt, các thuật ngữ Anh/viết tắt được giải thích khi cần. Đã sửa lỗi TiNiT trong bản nháp, định nghĩa TPU/SMA/SMP/DSC/Af và thống nhất phục hồi, độ cứng kết cấu, EI, luyện chu kỳ. Thuật ngữ nhiệt trễ được tách giữa thời gian đáp ứng và vòng trễ theo đường tải. Không có ID paper/evidence, mã WEP/QA hay nhật ký PDF trong thân bài. Glossary22mục nguồn riêng/biên tập, là phụ lục biên tập chứ không mặc định thành phần luận văn nộp.

Đạt kiểm tra tĩnh về ZIP/XML, Unicode, A4/TNR, bảng Word-native, header lặp, hàng không tách và reference giữ cả đoạn. Nội dung và bảng được đối chiếu với bản ROOT duyệt. Khả năng đọc thực tế, trang trắng, chia trang và glossary mồ côi cần render mới xác nhận được. Không có renderer DOCX khả dụng; WORD_RENDER_VALIDATION: NOT_VERIFIED. Đây là khoảng trống kiểm tra trực quan, không phải lỗi khoa học đã phát hiện.

## Phân tích riêng — lực siết và dữ liệu ma sát

M31 có phép đo trực tiếp lực kéo trượt một dây; không được viết rằng nguồn chỉ đo độ cứng tổng. Tuy vậy, việc đo lực kéo không tách được lực pháp tuyến và hệ số ma sát; không có bản đồ traction hoặc đặc trưng lực phục hồi theo nhiệt độ của riêng lò xo. Đỉnh lực trong5mm kéo không tự là giới hạn sức kháng cho mọi lịch sử/tải. Truyền lực từ lò xo qua ống đến tám dây là ràng buộc kiến trúc của nguồn, không được gán cho MP1.

## Phân tích riêng — nguyên mẫu, pha R và phục hồi

M32 tách hai tấm SMP khỏi bốn dây SMA1mm; chiều dài công xôn50mm khác chiều dài toàn màng100mm. Phục hồi nhanh hơn nhưng chưa hoàn toàn; phân bố cà phê không đều là một giải thích của tác giả, chưa được đo như nguyên nhân duy nhất. Tỷ lệ0,24 không được dùng vì tiêu chí thời gian chưa rõ và không tái dựng trực tiếp từ các ảnh mốc. CaptionFig.19 ghi belowTg cho SMA là bất nhất của nguồn, không biến thành tính chất vật liệu trong luận văn.

M37 có hai mẫu Furukawa cóR với Af334K, mẫu Furukawa khôngR cóAf330K và Nilaco khôngR cóAf347K. So sánh không tách độc lập nhà sản xuất/xử lý nhiệt/Af. Table1 ghi773K–1,2ks cho mẫu khôngR, trong khi Figs.7–8/phần chữ ghi723K–1,2ks; không tự sửa hoặc chọn một nhãn để dùng trong bản thảo. Vận tốc là độ dốc khớp chuyển vị–thời gian cấp điện đến50mm, không là vận tốc tức thời hay động học nội tại thuần túy. Thiết bị nhanh hơn có thể vẫn thiếu10mm phục hồi; luyện chu kỳ cải thiện mức trở về mà vận tốc ít đổi. Không suy pha R tồn tại trong MP1.

## Phương trình, hình và phạm vi

M32 Eq.(1) đã được kiểm tra; đơn vị độ dốc là N/mm và phép thế nguồn nhất quán sau đổi GPa→N/mm². Không dùng phương trình vì nó chỉ là ước lượng công xôn, không phải luật ma sát và chưa được chọn cho MP1. M31 mô hình công–năng lượng chỉ trình bày ở mức giả thiết. EQUATIONS:0; FIGURES:0. Không có ảnh công thức hoặc vấn đề OMML. Bảng so sánh do tác giả tổng hợp từ nguồn; không tái sử dụng hình xuất bản.

## Quyết định cuối

GATE_1: PASS (tuân thủ tổng hợp có giới hạn)  
GATE_2: PASS  
GATE_3: PASS (sai khác ghi chú/nguồn được ghi rõ)  
GATE_4: PASS  
GATE_5: PASS  
GATE_6: PASS  
GATE_7: PARTIAL (chưa kiểm tra trực quan)  
SEVEN_GATE_RESULT: PARTIAL_WITH_FINDINGS  
WORD_RENDER_VALIDATION: NOT_VERIFIED

Giới hạn chưa giải quyết: force/traction cục bộ, phân rã hysteresis, miền pha/nhiệt/tiếp xúc MP1, tiêu chí recoveryratioM32 và nhãn xử lý nhiệt M37. Những giới hạn này không được che bằng kết quả dàn ý PASS.

## Đóng kiểm tra cuối bởi ROOT

QA độc lập đã đối chiếu cả năm tệp, bản nội dung được duyệt và ba báo cáo PDF; không phát hiện lỗi nội dung, trích dẫn, metadata, truy xuất hoặc glossary. ROOT kiểm tra lại sau khi bổ sung cột section_id và làm rõ đại lượng suy ra trong CSV: vẫn giữ 30 bản ghi (21 nguồn, 5 suy luận, 2 đề xuất, 2 phạm vi), 22 thuật ngữ, 20 Evidence ID hiện hữu và bốn ánh xạ bắt buộc.

Đã mở lại DOCX, đối chiếu nguyên văn nội dung/bảng/tài liệu tham khảo/glossary với bản duyệt; ZIP hợp lệ, thứ tự citation [1]–[2]–[3], ba DOI đóng kín. Hai bảng Word-native có tổng độ rộng 9298 twip mỗi bảng; header lặp và 27 hàng không tách; ba tài liệu tham khảo giữ trọn đoạn. Thân bài Times New Roman 12 pt; bảng 8,5 pt; heading 14 pt; caption và tài liệu tham khảo 10 pt.

Kiểm tra SHA256 của 28 đầu vào đã ghi nhận xác nhận không thay đổi. Gói cuối gồm đúng năm tệp, được mở lại và đối chiếu checksum sau khi lưu vào thư mục §2.4.3. Không có nội dung khoa học mới phát sinh ở bước này.

Không có trình kết xuất Word khả dụng: chưa xác minh trực quan chia trang, trang trắng, cắt bảng hoặc hàng glossary mồ côi. GATE_7: PARTIAL; WORD_RENDER_VALIDATION: NOT_VERIFIED.
