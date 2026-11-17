# MP1_CH2_2_4_1 — Bảy cổng chấp nhận

## Phạm vi và bằng chứng
Bốn PDF gốc M25–M28 đã được mở và đối chiếu với Writing Evidence Pack. Các locator trong báo cáo dùng số trang vật lý của PDF. M25 có trang bìa vật lý p.1; bài báo bắt đầu ở p.2. M27 có 37 trang vật lý; các ghi chú cũ ghi số trang khác đã không được dùng.

## Gate 1 — Tuân thủ dàn ý: PARTIAL WITH FINDINGS
- B01 được xử lý: nhiệt độ, ứng suất, lịch sử tải, tốc độ, chuyển pha, mô đun và vòng trễ đều được nêu.
- B01 được giới hạn đúng: M26/M27 là kéo gần đẳng nhiệt; không có cơ sở để viết định luật tốc độ hoặc tính không phụ thuộc nhiệt độ.
- B02 được xử lý: không đưa phương trình hay tham số SMA vào vì MP1 chưa chọn mô hình cấu thành; lý do được ghi rõ trong bản thảo.
- Vật liệu được nối với câu hỏi MP1 qua phân biệt đáp ứng vật liệu–kết cấu và khả năng nhận dạng nguyên nhân.
- Không viết sang §2.4.2; chỉ có một đoạn chuyển tiếp.
- Lý do chưa PASS: độ bao phủ trực tiếp cho ảnh hưởng tổng quát của rate và temperature còn giới hạn.

## Gate 2 — Truy xuất claim: PASS
- 20 dòng claim trong CSV; 14 claim source-grounded, 3 inference, 2 author proposal và 1 document-coverage record.
- Mỗi claim nguồn có Paper ID, Evidence ID và locator PDF vật lý.
- M25/M26/M27/M28 được giữ riêng theo loại bằng chứng và observable.
- Không đưa hằng số vật liệu, nhiệt độ chuyển pha hay định luật tốc độ của MP1.

## Gate 3 — Kiểm tra PDF gốc: PASS
- M25: mô hình Souza–Abaqus/UMAT, tiếp xúc dây và kiểm chứng bằng dữ liệu kéo đã công bố; SME là mô phỏng.
- M26: hai cấu trúc cáp, điều kiện kéo gần đẳng nhiệt, DIC/IR, chu kỳ và giới hạn.
- M27: topology 7×7 và 1×27 đã dùng theo bản hiệu chỉnh; đáp ứng thành phần và phép trừ lớp được đánh dấu đúng.
- M28: thí nghiệm thép tách khỏi NiTi FE; El Centro của NiTi được ghi là mô phỏng.

## Gate 4 — Tổng hợp liên nghiên cứu: PASS
M26/M27 được so sánh theo trục cáp hoàn chỉnh–thành phần; M25 dùng để minh họa ghép mô hình vật liệu–tiếp xúc; M28 dùng để chỉ rõ biên thực nghiệm–số. Tension, FE force–displacement và bending rigidity không bị gộp.

## Gate 5 — Giả định và giới hạn cơ học: PASS
Austenit/martensit, siêu đàn hồi/nhớ hình, mô đun vật liệu/độ cứng kết cấu, vòng trễ chuyển pha/vòng trễ ma sát, tải kéo/uốn và trạng thái vận hành MP1 được tách rõ. Không có luật cấu thành mới, không có tuyên bố mới lạ.

## Gate 6 — Toàn vẹn trích dẫn: PASS
Bốn tài liệu được trích trong thân bài và danh mục; DOI, tác giả, năm và tiêu đề được đối chiếu với PDF/registry. Citation mapping theo thứ tự xuất hiện đầu tiên là [1] Reedlunn Phần I, [2] Vahidi, [3] Reedlunn Phần II, [4] Narjabadifam. M25 được ghi là xuất bản trực tuyến 2021 và có ghi chú số phát hành 2022 để giải quyết khác biệt tên tệp.

## Gate 7 — Chất lượng văn phong và DOCX: PARTIAL
Bản thảo hoàn toàn bằng tiếng Việt, dùng thuật ngữ cơ học nhất quán, đã định nghĩa DIC, IR, gần tĩnh (quasi-static), đoạn nằm ngang (plateau), FE và UMAT khi cần, có bảng Word-native, tài liệu tham khảo và phụ lục thuật ngữ bốn cột. Không có Paper ID/Evidence ID trong phần văn bản luận văn. Kiểm tra XML và cấu trúc bảng đã thực hiện. LibreOffice/soffice không có sẵn, nên `WORD_RENDER_VALIDATION: NOT_VERIFIED`; số trang, trang trắng và bố cục trực quan chưa được xác nhận.

## Phân biệt các nguồn vòng trễ
M26/M27 cho thấy vòng trễ và biến dạng dư trong kéo NiTi, nhưng không tách hoàn toàn đóng góp vật liệu khỏi kiến trúc. M25 giải đồng thời SMA và contact/friction nên không nhận dạng riêng hai nguồn. M28 có vòng trễ NiTi là đầu ra FE và vòng trễ thép chịu ảnh hưởng tiếp xúc, hình học và sai số thí nghiệm.

## Bao phủ B01 về nhiệt độ và tốc độ
Trạng thái nhiệt độ và vai trò của tốc độ được giải thích theo bằng chứng gần đẳng nhiệt và theo dõi nhiệt độ; phần tổng quát hóa bị đánh dấu giới hạn. Không có hệ số nhiệt, nhiệt độ chuyển pha hoặc định luật tốc độ nào được chuyển sang MP1.

## Biện minh lựa chọn phương trình
Không chèn phương trình. M25 có phương trình Souza trong nguồn, nhưng MP1 chưa sử dụng mô hình đó; chép lại sẽ vượt B02 và tạo ấn tượng về một luật cấu thành đã được chấp nhận.

## Kết quả bảy cổng
**PARTIAL_WITH_FINDINGS** — Gate 1 PARTIAL do giới hạn trực tiếp của bằng chứng nhiệt độ/tốc độ và Gate 7 PARTIAL vì chưa thể kết xuất kiểm tra trực quan trong môi trường hiện tại. Đây là trạng thái chấp nhận có giới hạn, không phải xác nhận trạng thái vận hành hay tuyên bố novelty.


## R1 — Targeted hotfix verification
- Citation order follows first appearance: [1] M26, [2] M25, [3] M27, [4] M28; comparison table and bibliography use the same mapping.
- All 15 terminology records were reviewed individually. Source IDs now reflect direct support or editorial synthesis; no new Evidence ID or fifth paper was added.
- The opening capitalization, final paragraph, DIC/IR definitions, near-isothermal wording, quasi-static translation and plateau wording were corrected without changing scientific findings.
- Claim counts remain separate: 14 SOURCE_GROUNDED, 3 INFERENCE, 2 AUTHOR_PROPOSAL, 1 DOCUMENT_COVERAGE; 20 records are not reported as 20 independent findings.

## R2 — Hai hiệu chỉnh cục bộ
- Đã đặt `keep_together=True` (`w:keepLines`) cho toàn bộ đoạn tài liệu [4]; nội dung tài liệu, lề trang, kiểu chữ, bảng và số trích dẫn không đổi.
- Đã thay cụm từ UMAT thành “chương trình con vật liệu do người dùng định nghĩa (UMAT)”.
- So sánh XML trước–sau xác nhận chỉ hai thay đổi trên trong DOCX; mọi phần khác trong gói DOCX giữ nguyên. Không thêm claim khoa học.
- Kiểm tra đạt: bốn DOI và thứ tự xuất hiện [1] M26, [2] M25, [3] M27, [4] M28; 20 bản ghi truy xuất; 15 thuật ngữ; topology M27 và phân biệt thí nghiệm thép/mô phỏng NiTi M28; ZIP, hàng tiêu đề lặp và hàng bảng không tách trang.
- Người dùng báo diagnostic render xác nhận tài liệu [4] nằm trọn trang 4 và giữ bố cục bốn trang. Phiên R2 không có renderer để kiểm tra độc lập: `WORD_RENDER_VALIDATION: NOT_VERIFIED`.
- Gate 1: PARTIAL; Gate 7: PARTIAL; kết quả chung: PARTIAL_WITH_FINDINGS.
