# Tự rà soát bảy cổng, mục 2.1.2

## Cổng 1. Dàn ý và phạm vi

STATUS: PASS
METHOD: Đối chiếu trang 10, B01–B03; đọc DOCX
EVIDENCE: Chỉ có mục 2.1.2
COUNTS: 1 đề mục; 8 đoạn nội dung
FINDINGS: Chỉ có mục 2.1.2
SEVERITY: LOW
UNRESOLVED: Không có
FINAL_DECISION: PASS

## Cổng 2. Trung thực phương pháp

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Đối chiếu giao thức với log thi hành
EVIDENCE: Đã tách từ vựng trong giao thức khỏi các lượt tìm GV-001 và nhánh MP1-V002 đã ghi nhận; không nhận đã áp dụng bộ lọc
COUNTS: 15 nhánh; 2 nền tảng tìm kiếm ghi nhận trong GV-001
FINDINGS: Đã tách từ vựng trong giao thức khỏi các lượt tìm GV-001 và nhánh MP1-V002 đã ghi nhận; không nhận đã áp dụng bộ lọc
SEVERITY: DOCUMENTED_LIMITATION
UNRESOLVED: Chưa có phép nối đầy đủ từ truy vấn đến từng bài
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Cổng 3. Nguồn và anchor

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Đọc hồ sơ nguồn và mã băm; kiểm XPath, khoảng ký tự Unicode và độ phủ toàn bộ đoạn trong DOCX
EVIDENCE: M01 có định vị tranh chấp nên không trích dẫn; 259 chuỗi khóa và 258 nhóm định danh đã đối soát theo DOI hoặc nhan đề
COUNTS: 33 hàng truy vết theo câu/mệnh đề; 0 vị trí chưa khớp; phủ đủ 8/8 đoạn
FINDINGS: M01 có định vị tranh chấp nên không trích dẫn; 259 chuỗi khóa và 258 nhóm định danh đã đối soát theo DOI hoặc nhan đề
SEVERITY: DOCUMENTED_LIMITATION
UNRESOLVED: Thiếu chuỗi truy vấn chính xác của từng nhánh
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Cổng 4. Nhất quán khoa học

STATUS: PASS
METHOD: Đọc P3, §2.1.1 và §§2.2–2.6
EVIDENCE: Không khẳng định cơ chế mới
COUNTS: Giữ nguyên trạng thái G00/H0a/H0b/H1
FINDINGS: Không khẳng định cơ chế mới
SEVERITY: LOW
UNRESOLVED: Năm quyết định con người còn mở
FINAL_DECISION: PASS

## Cổng 5. Tiêu chí chọn nguồn

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Đối chiếu sàng lọc siêu dữ liệu với giao thức
EVIDENCE: Phân biệt loại khỏi đợt truy vết với không trích dẫn
COUNTS: Ba nhóm 12/85/81; một ví dụ nêu tên; quan sát 34 bài tạp chí và năm loại nguồn khác
FINDINGS: Phân biệt loại khỏi đợt truy vết với không trích dẫn
SEVERITY: DOCUMENTED_LIMITATION
UNRESOLVED: Tiêu chí cho toàn tập đọc chỉ là diễn giải hồi cứu
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Cổng 6. Viết và hiển thị

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Mở lại DOCX bằng python-docx, kiểm ZIP; xuất PDF bằng LibreOffice và xem cả hai ảnh trang
EVIDENCE: Kiểu chữ và trang Word đã áp dụng
COUNTS: 8 đoạn; 0 trích dẫn; 0 bảng; đã xem 2 trang A4
FINDINGS: Kiểu chữ và trang Word đã áp dụng
SEVERITY: DOCUMENTED_LIMITATION
UNRESOLVED: Microsoft Word NOT_VERIFIED
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Cổng 7. Gói và bất biến

STATUS: PASS
METHOD: ROOT kiểm danh mục SHA-256, diff Git, biên nhận UTC và phạm vi mười tệp
EVIDENCE: 973 tệp được bảo vệ không đổi; giữ nguyên 387 tệp bẩn có sẵn; đã xác nhận giao nhau giữa hai nhánh A/B
COUNTS: Tổng cộng 10 tệp đầu ra mới, A=5; giao nhau 199.224118 giây
FINDINGS: Diff Git của tệp theo dõi và vùng chuẩn bị commit không đổi; bản thảo nền khớp từng byte
SEVERITY: LOW
UNRESOLVED: Vẫn cần nghiệm thu độc lập
FINAL_DECISION: PASS

## Rà soát chéo đã xử lý

A01–A05 đã sửa ở Word, bảng truy vết và báo cáo. Việc gộp khóa DOI với bản ghi cùng nhan đề trong 312 bản ghi cho 258 định danh; vấn đề này đã được giải thích trong báo cáo và không còn là sai lệch đếm. Kết luận chấp nhận độc lập vẫn chưa có.

## Kết luận tự rà soát

COMPLETED_WITH_DOCUMENTED_LIMITATIONS. ROOT đã xác minh bản PDF, bất biến đầu vào, phạm vi mười tệp và thực thi song song; hai nghiệm thu độc lập vẫn chưa thực hiện.


# HOTFIX ADDENDUM — MP1-CH2-2.1.2-B03-EXCLUDED-SOURCE-IDENTIFICATION-HOTFIX

Phần này là kết quả mới nhất cho hotfix, bổ sung cho lịch sử tự rà soát phía trên. Không thay thế nghiệm thu độc lập.

TASK_ID: MP1-CH2-2.1.2-B03-EXCLUDED-SOURCE-IDENTIFICATION-HOTFIX
STATUS: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
INDEPENDENT_REVIEW_STATUS_RECEIVED: MINOR_REVISION_REQUIRED
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING

## HOTFIX GATE 1. Dàn ý

STATUS: PASS
METHOD: Đọc trực tiếp outline PDF đúng hash, trang vật lý 10/22; đối chiếu B03 và so sánh Word trước/sau.
EVIDENCE: B03 yêu cầu nhận diện nguồn bị loại cùng lý do; P07 hiện nêu nhan đề tiếng Anh đúng thành phần title. B01/B02 và mọi đoạn khác giữ nguyên.
COUNTS: 3 bullet; 1 câu sửa; 8 đoạn giữ.
FINDINGS: B03 có ví dụ nhận diện được; không phát sinh phương pháp tìm kiếm hay danh sách loại trừ mới.
SEVERITY: NONE
UNRESOLVED: Không có finding về outline trong hotfix.
FINAL_DECISION: PASS

## HOTFIX GATE 2. Trung thực phương pháp

STATUS: PASS
METHOD: Đọc bản ghi CSV gốc và đối chiếu diễn đạt loại ở mức metadata với C024/C025.
EVIDENCE: recommendation=EXCLUDE; metadata_only=True; scientific_evidence=False; human_review_required=True. Lý do chỉ nói metadata chưa cho thấy mối đe dọa T1/T2/T3.
COUNTS: 1 bản ghi gốc; 0 quyết định loại mới; 0 đánh giá toàn văn mới.
FINDINGS: Không chuyển metadata screening thành phán quyết nội dung toàn văn hoặc loại khỏi mọi mục đích tổng quan.
SEVERITY: NONE
UNRESOLVED: Giới hạn metadata-only được giữ; tác vụ không kiểm bài toàn văn.
FINAL_DECISION: PASS

## HOTFIX GATE 3. Nguồn và truy vết

STATUS: PASS
METHOD: Kiểm schema CSV, candidate duy nhất, SHA-256, số hàng; parse XML DOCX, XPath container và offsets Unicode của 33 records.
EVIDENCE: Source CSV hash 206501aa0485177b9df2860a306719bc75425caf68944b09ea286c40aec7f4db; bản ghi dữ liệu số 99, dòng vật lý 100. C023 có nhan đề và provenance; C024/C025 chỉ đổi offsets.
COUNTS: 33/33 anchors; 0 trùng ID; 0 anchor lỗi; 8/8 đoạn phủ 100% ký tự không trắng; 0 overlap/gap.
FINDINGS: Phần tiếng Anh khớp chính xác đầu trường title song ngữ; không tạo Evidence ID hoặc sửa registry.
SEVERITY: NONE
UNRESOLVED: Không có lỗi anchor trong phạm vi hotfix.
FINAL_DECISION: PASS

## HOTFIX GATE 4. Nhất quán khoa học

STATUS: PASS
METHOD: So sánh mọi paragraph và từng record trace trước/sau; kiểm phần ZIP ngoài document.xml.
EVIDENCE: P01–P06, P08 và heading giữ nguyên XML; C024/C025 giữ nguyên câu; các ZIP parts khác giữ bytes.
COUNTS: 1 câu thêm nhận diện; 0 claim khoa học mới; 0 thay đổi giả thuyết/nghiên cứu.
FINDINGS: Không đổi thống kê, ngày, database, bộ lọc, tiêu chí hồi cứu hoặc P3; không có novelty claim mới.
SEVERITY: NONE
UNRESOLVED: Các quyết định nghiên cứu còn mở giữ nguyên, không thuộc thẩm quyền hotfix.
FINAL_DECISION: PASS

## HOTFIX GATE 5. Khắc phục B03

STATUS: PASS
METHOD: Đối chiếu finding P2 với câu C023 sau sửa và hàng screening gốc.
EVIDENCE: Nhận diện bằng nhan đề đầy đủ tiếng Anh; giải thích đúng EXCLUDE ở bước nhan đề/tóm tắt và phạm vi T1–T3.
COUNTS: 1 finding P2 được xử lý; 0 P1/P2 còn hoạt động trong tự rà soát hotfix.
FINDINGS: P2 B03_EXCLUDED_SOURCE_IDENTIFICATION được xử lý trong SELF_REVIEW_ONLY, chờ nghiệm thu độc lập.
SEVERITY: NONE
UNRESOLVED: Independent hotfix acceptance chưa thực hiện; không tự cấp acceptance.
FINAL_DECISION: PASS

## HOTFIX GATE 6. DOCX và hiển thị

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Kiểm ZIP CRC/XML, Normal/Heading styles, lề/font; LibreOffice 24.2.7.2 kết xuất DOCX đúng hash; ROOT xem tất cả trang PNG.
EVIDENCE: Hai trang A4; P07 ở trang 2, tên tiếng Anh in nghiêng, xuống dòng bình thường; không mất dấu/tràn/cắt. Các paragraph properties ngoài câu sửa giữ nguyên.
COUNTS: 2/2 trang đã xem; 0 bảng/hình/OMML mới; 0 references.
FINDINGS: Lần chạy đầu LibreOffice khởi tạo profile trả 81; lần chạy lại cùng profile trả 0, tạo PDF hợp lệ. Không cài ứng dụng vào hệ thống.
SEVERITY: DOCUMENTED_LIMITATION
UNRESOLVED: MICROSOFT_WORD_VALIDATION=NOT_VERIFIED; đã kiểm bằng LibreOffice, không xác nhận hiển thị Microsoft Word.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## HOTFIX GATE 7. Bất biến và gói

STATUS: PASS
METHOD: Đối chiếu hash trước/sau của manifest hợp nhất, git status/diff/cached; kiểm đúng năm tên tệp và prefix lịch sử báo cáo.
EVIDENCE: 614 tệp ngoài bốn tệp được phép giữ bytes, gồm terminology, §2.1.3, §2.1.1, §§2.2–2.6, WEP/P3/registry. Git status, tracked diff và cached diff giống trước.
COUNTS: 5 deliverables; 4 tệp thay đổi được phép; 397 tệp modified/untracked có sẵn được ghi nhận, 393 ngoài scope hotfix giữ nguyên.
FINDINGS: Không tạo deliverable mới; báo cáo chỉ append; script/PDF/PNG/runtime ở scratch; không stage/commit/push.
SEVERITY: NONE
UNRESOLVED: Không có thay đổi ngoài phạm vi được phép.
FINAL_DECISION: PASS

P2_FINDING_STATUS: RESOLVED_IN_SELF_REVIEW_PENDING_INDEPENDENT_ACCEPTANCE
P1_P2_UNRESOLVED_IN_HOTFIX: 0
FINAL_SELF_REVIEW_DECISION: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS
NEXT_ACTION: AWAIT_INDEPENDENT_HOTFIX_ACCEPTANCE
