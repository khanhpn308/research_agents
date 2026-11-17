# MP1-CH2-2.3.2 — Bảy cổng nghiệm thu

**TASK_ID:** MP1-CH2-2.3.2-RESEARCH-THESIS-DRAFT  
**Phạm vi:** Chương 2, Mục 2.3.2. Kẹt dây/sợi  
**Bối cảnh:** HCMUT–VNU-HCM, Khoa Cơ khí, Thạc sĩ Kỹ thuật Cơ khí định hướng nghiên cứu  
**Ngày kiểm tra:** 2026-10-17 (Asia/Bangkok)

## Gate 1 — Tuân thủ dàn ý: PASS

- B01 được đáp ứng bằng tổng hợp hình học, bố trí phần tử, giao diện ma sát, trạng thái dính–trượt và các phép đo lực–độ võng, mô men–góc hoặc uốn ba điểm.
- B02 được đáp ứng bằng so sánh vật liệu, packing, bao, áp suất, điều kiện biên và đại lượng đo; giới hạn chuyển sang bó TiNi được ghi rõ.
- Nội dung nối từ Mục 2.3.1 nhưng không lặp lại taxonomy tổng quát.
- Đoạn cuối chuyển tiếp sang Mục 2.3.3.

## Gate 2 — Truy vết phát biểu kỹ thuật: PASS

- CSV có 9 technical claims và 1 bản ghi `DOCUMENT_COVERAGE`, cùng Paper ID, Evidence ID, PDF locator, support role và giới hạn chuyển giao.
- M08/M09 được đánh dấu `DIRECT_SUPPORT` hoặc `DIRECT_SUPPORT_WITH_LIMITS`.
- M07/M13 được đánh dấu `COMPARATOR`.
- Hai claim kỹ thuật tổng hợp được đánh dấu `INFERENCE`; C10 không còn là claim khoa học và được phân loại `DOCUMENT_COVERAGE`.
- Không có claim về topology dây–dây hoặc dây–bao của MP1 và không có claim novelty.

## Gate 3 — Kiểm chứng PDF gốc: PASS

Đã kiểm tra PDF gốc và đối chiếu lại locator:

- M08: PDF p.4, Fig. 2, Module A/B, 50 mm × 14,5 mm, lòng rỗng trung tâm của Module B và dạng lược liên kết.
- M09: PDF p.4–6, vật liệu kraft/hemp/nylon, dây khoảng 1 mm, bố trí chữ nhật/tròn, chân không, mô hình ở §2.2 p.5 và bao HDPE ở phần chế tạo p.6.
- M09 có sai lệch locator trong WEP: WEP ghi §2.2 ở p.4, nhưng PDF gốc cho thấy p.4 là §2.1 và §2.2 bắt đầu ở p.5; sai lệch này được ghi rõ trong traceability.
- M07: PDF p.2, Fig. 1, trạng thái tiền-trượt, chuyển tiếp và trượt hoàn toàn của laminar jamming.
- M13: PDF p.1, Abstract/Introduction, bladder–fiber bundle–rigid chain link, mô hình trạng thái và thử uốn 0–300 kPa.

## Gate 4 — Tổng hợp liên công trình: PASS

- M08 và M09 được so sánh theo hình học, packing, vật liệu, bao và giao diện.
- M07 chỉ được dùng làm comparator laminar cho cơ chế dính–trượt.
- M13 chỉ được dùng làm comparator áp suất dương và mô hình độ cứng phụ thuộc áp suất.
- Bảng so sánh là bảng tổng hợp mới, có caption “Bảng 2.3.2. So sánh các kiến trúc kẹt dây/sợi và nguồn đối chiếu”, không sao chép hình nguồn.
- Prose phân biệt observables toàn hệ với lực tiếp xúc cục bộ.

## Gate 5 — Giả định và giới hạn cơ học: PASS

- Không đồng nhất áp suất nguồn với lực tiếp xúc pháp tuyến.
- Không chuyển ngưỡng trượt, pressure range, stiffness hoặc mô hình của M07/M13 sang MP1.
- Không đồng nhất độ cứng hệ với mô đun Young.
- Không đồng nhất chuyển pha TiNi với trượt ma sát.
- Khác biệt vật liệu, packing, bao, biên và đường truyền áp suất được nêu rõ.

## Gate 6 — Toàn vẹn citation: PASS

- Citation [1]–[4] có mục tài liệu tham khảo tương ứng.
- Bốn DOI, tiêu đề, tác giả, năm và nguồn xuất bản được đối chiếu với PDF/registry.
- Không có reference ngoài bốn nguồn được ánh xạ.
- Số citation là tạm thời cho bản thảo độc lập.

## Gate 7 — Văn phong thạc sĩ, tiếng Việt và thuật ngữ: PASS

- Thân bài và bảng so sánh dùng tiếng Việt; tiếng Anh chỉ giữ trong ngoặc hoặc tên bài báo/thuật ngữ glossary.
- Glossary có 12 thuật ngữ thực sự xuất hiện và được trình bày trong bảng 6 cột dễ đọc; mã xác minh và giới hạn chi tiết được giữ trong TERMINOLOGY.csv.
- Các thuật ngữ có trạng thái xác minh và giới hạn diễn giải.
- Không có Evidence ID, agent note hoặc tuyên bố novelty trong thân DOCX.

## Kiểm tra cấu trúc DOCX

- A4, Word-native tables, 6 đoạn thân bài, 2 bảng.
- Hàng tiêu đề bảng lặp lại và các hàng đặt `cantSplit`.
- Các run trong bảng được đặt Times New Roman 8.5 pt tường minh.
- Có page break trước phụ lục glossary.
- ZIP integrity và mở lại DOCX đạt.


## Final targeted hotfix validation

- Câu locator M09 đã được xóa khỏi thân bài; thông tin p.4/p.5/p.6 vẫn giữ trong SOURCE_TRACEABILITY.csv và phần Gate 3 này.
- Paper IDs M07–M13 đã được thay bằng tên tác giả trong các đoạn văn, nhãn bảng và phụ lục DOCX; các ID vẫn giữ nguyên trong traceability.
- Bảng M09 nay tách rõ phép thử lực–độ võng khi uốn và mô men–góc khi xoắn, không so sánh trực tiếp trị số khác thứ nguyên.
- C10 được phân loại `DOCUMENT_COVERAGE`; technical-claim count còn 9.

## Giới hạn còn lại

- Không có LibreOffice, soffice hoặc renderer DOCX trong môi trường. Vì vậy `WORD_RENDER_VALIDATION: NOT_VERIFIED`; chưa thể xác nhận trực quan tràn bảng, số trang hoặc ngắt dòng sau render.
- M09 locator mismatch được bảo tồn thay vì âm thầm sửa Writing Evidence Pack.
- Các kết quả M08/M09/M13 vẫn là bằng chứng architecture-specific; không xác nhận mô hình tiếp xúc của MP1.

## Final acceptance

**SEVEN_GATE_RESULT: PASS_ALL_7_GATES**  
**OVERALL_STATUS: PARTIAL_WITH_FINDINGS** do render trực quan chưa thể thực hiện.
