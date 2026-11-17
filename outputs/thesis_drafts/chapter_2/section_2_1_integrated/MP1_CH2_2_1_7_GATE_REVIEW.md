# Hồ sơ bảy gate tự rà soát §2.1

TASK_ID: MP1-CH2-2.1-INTEGRATION
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING

STATUS: COMPLETED_WITH_DOCUMENTED_LIMITATIONS

## Phạm vi xác nhận

Đây là kiểm tra tích hợp các baseline được người dùng chỉ định. Không tìm tài liệu mới, không đánh giá lại toàn bộ bằng chứng sơ cấp và không phân xử nghiệm thu độc lập. Giá trị “PASS” chỉ áp dụng tiêu chí của gate trong phạm vi tích hợp.

## Gate 1

STATUS: PASS

METHOD: Đọc trang vật lý 10–11/22 của outline; parse heading và nội dung final DOCX.

EVIDENCE: Dàn ý đúng hash; 11 dòng đối chiếu bên dưới; XPath heading p[1],p[2],p[9],p[18],p[28].

COUNTS: 11/11 bullet; bốn tiểu mục; 0 heading ngoài phạm vi.

FINDINGS: Nội dung các bullet được đề cập với giới hạn có hồ sơ; không coi 11/11 là đã khôi phục đầy đủ lịch sử tìm kiếm.

SEVERITY: NONE

UNRESOLVED: Không có lệch dàn ý.

FINAL_DECISION: Đạt cấu trúc trong phạm vi tác vụ.

## Gate 2

STATUS: PASS

METHOD: So nguyên văn từng container và từng claim; đối chiếu sáu tệp P3 canonical.

EVIDENCE: Master trace 136 bản ghi kế thừa có original_row_json; changelog đầy đủ; p[7],p[8],p[24],p[25],p[33],p[37].

COUNTS: 136/136 claims; 0 scientific change; 0 evidence promotion; 5 quyết định còn mở.

FINDINGS: Giữ H0a/H0b/H1; không phát sinh khoa học mới. Corpus và phương pháp được kế thừa nguyên giới hạn; không tái audit 39 PDF.

SEVERITY: NONE

UNRESOLVED: Năm quyết định và mapping RQ chưa phê duyệt là giới hạn được bảo toàn, không phải lỗi tích hợp.

FINAL_DECISION: Đạt bảo toàn nội dung; không cấp xác nhận khoa học mới.

## Gate 3

STATUS: PASS

METHOD: Đọc bốn tiểu mục liên tục; kiểm ba cặp chuyển tiếp và mở đầu §2.2; đối chiếu có mục tiêu §§2.2–2.6.

EVIDENCE: Changelog: các bảng chuyển tiếp, chín nhóm lặp và đối chiếu baselines.

COUNTS: 3 cặp trong §2.1; 1 chuyển tiếp tới §2.2; 9 nhóm lặp; 0 cắt câu.

FINDINGS: Purpose → Selection → Extraction → Appraisal phù hợp; các lần nhắc lại có vai trò khác nhau. NO_MATERIAL_REDUNDANCY_FOUND.

SEVERITY: NONE

UNRESOLVED: OOS-01 là khác biệt thư mục ngoài §2.1, mức P3, không sửa.

FINAL_DECISION: Đạt mạch lập luận; không cần câu nối mới.

## Gate 4

STATUS: PASS

METHOD: Parse final DOCX, resolve từng XPath trước rồi kiểm Unicode offsets; kiểm mọi ký tự khác khoảng trắng, ID, category, ô bảng/caption và bibliography.

EVIDENCE: Master trace 144 hàng; 72 paragraph containers; source_path_check có 136/136 đường dẫn/hash gốc khớp; 136 original_row_json bảo toàn.

COUNTS: 144 resolved; 0 unresolved; 0 duplicate IDs; 0 gaps; 0 overlaps; 0 unexplained source claims; 14879 ký tự khác khoảng trắng.

FINDINGS: 136 claims gốc + 8 bản ghi cấu trúc/thư mục bổ sung, không gán 8 bản ghi mới thành phát hiện khoa học. Ba nhan đề/bibliography khoa học trước không có claim_id gốc được bổ sung rõ origin.

SEVERITY: NONE

UNRESOLVED: Không có thiếu neo hoặc claim loss; trạng thái nguồn gốc được giữ, không nâng thành xác minh mới PDF.

FINAL_DECISION: Đạt truy vết trong phạm vi tích hợp.

## Gate 5

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Đếm trực tiếp citations/references của cả bốn Word; đối soát identity, thứ tự xuất hiện, map và selected pages hướng dẫn IEEE.

EVIDENCE: Citation map 4 hàng; scientific identity từ DOCX/CSV; IEEE PDF hash 947dad6b67c60500e32960a5a3345824e8efa57a7ef4daa9f2448fa13360d66b, trang vật lý 1,4,13 đã đọc.

COUNTS: Before 3+0+0+1=4 citations, 3+0+0+1=4 references; after 4/4; 0 missing/orphan/duplicates/conflicts.

FINDINGS: LOCAL_1→INTEGRATED_1, LOCAL_2→2, LOCAL_3→3 tại §2.1.1; IEEE LOCAL_1→4 tại §2.1.4. Không có source mới.

SEVERITY: DOCUMENTED_LIMITATION

UNRESOLVED: SCHOOL_POLICY=NOT_VERIFIED; IEEE theo AUTHOR_APPROVED_STYLE_DECISION. Không xác minh lại tính áp dụng quy định trường.

FINAL_DECISION: Đạt namespace và liên kết citation/reference; giữ giới hạn chính sách trường.

## Gate 6

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: ZIP CRC; parse toàn bộ XML parts; kiểm style, A4/lề/font/line spacing; LibreOffice render PDF; xem trực quan từng trang PNG cuối.

EVIDENCE: 16 XML/rels parts parse; DOCX hash fe4fd16fbb93bcdf39708740fb90dd120563825c57ce86bd9cf36e35f841d4dd; bảng native 3×10; glyph bounds PDF; nhật ký trực quan bên dưới.

COUNTS: 7 rendered; 7/7 visually reviewed; 1 table; 0 figures; 0 OMML; toàn bộ glyphs 12 pt.

FINDINGS: Không thấy tràn lề, lỗi dấu, cắt chữ, mất hàng, trang trắng hoặc heading mồ côi. Bảng chia trang 4–5, header lặp và nội dung đọc được. Caption trước bảng, source note sau bảng được giữ.

SEVERITY: DOCUMENTED_LIMITATION

UNRESOLVED: MICROSOFT_WORD_VALIDATION=NOT_VERIFIED; không được gọi là Word native application PASS.

FINAL_DECISION: Đạt kiểm tra OOXML và LibreOffice với giới hạn ứng dụng đã ghi.

## Gate 7

STATUS: PASS

METHOD: Tính lại input/protected manifest và toàn bộ tệp repo có sẵn; đối chiếu git status/diff/cached; đọc lại đúng bảy deliverables.

EVIDENCE: Manifest đầu/cuối trong execution report; 20 source files, 9 accepted DOCX; 612 protected entries; 2043 repo files so bytes/hash.

COUNTS: 20/20 source files bất biến; 9/9 DOCX đúng hash; 0 thay đổi tệp có sẵn; 7 tệp mới trong đúng một thư mục.

FINDINGS: Pre-existing 402 dòng status bảo toàn; không sửa WEP/P3/registry; không commit/push; không giả independent acceptance.

SEVERITY: NONE

UNRESOLVED: Human approval và nghiệm thu độc lập tiếp tục chờ.

FINAL_DECISION: Đạt gói tự rà soát; chưa phải baseline được nghiệm thu.

## Đối chiếu 11 bullet chính thức

Dàn ý: `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf`; SHA-256 `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e`. Đọc trang vật lý 10–11/22. XPath rút gọn bên dưới nằm dưới `/w:document/w:body/`.

| Bullet | Nội dung chính thức | Vị trí tích hợp | Kết quả |
|---|---|---|---|
| 2.1.1-B01 | Giải thích vì sao tổng quan tập trung vào pressure-controlled friction, wire/fiber jamming, TiNi bundle mechanics, contact modeling và validation. | p[3]–[7] | Được đề cập, giữ giới hạn baseline. |
| 2.1.1-B02 | Liên kết từng nhóm tài liệu với RQ1–RQ5 thay vì trình bày lịch sử chung của soft robotics. | p[3]–[8] | Được đề cập, giữ giới hạn baseline. |
| 2.1.2-B01 | Ghi rõ từ khóa, nguồn tìm kiếm, khoảng thời gian thực tế, ngôn ngữ, loại ấn phẩm và cách xử lý bài chỉ có metadata. | p[11]–[13], p[15], p[17] | Được đề cập, giữ giới hạn baseline. |
| 2.1.2-B02 | Đưa vào các nghiên cứu có mechanics/model/validation liên quan; loại hoặc để riêng các bài chỉ trình diễn ứng dụng, controller hoặc vật liệu không liên quan. | p[10], p[14]–[15] | Được đề cập, giữ giới hạn baseline. |
| 2.1.2-B03 | Nêu các nguồn bị loại và lý do nếu người đọc có thể kỳ vọng chúng xuất hiện. | p[16] | Được đề cập, giữ giới hạn baseline. |
| 2.1.3-B01 | Mỗi nguồn được ghi theo cơ chế, hình học, vật liệu, pressure/load input, model, observables, validation, limitation và relevance. | p[19]–[21]; tbl[1] tr[1]–tr[10] | Được đề cập, giữ giới hạn baseline. |
| 2.1.3-B02 | Nhóm chính theo câu hỏi và cơ chế; dùng chronology bên trong nhóm khi cần giải thích sự phát triển. | p[22] | Được đề cập, giữ giới hạn baseline. |
| 2.1.3-B03 | Cuối mỗi nhóm phải có synthesis paragraph nêu điểm thống nhất, điểm mâu thuẫn và hệ quả cho MP1-R. | p[23]–[25] | Được đề cập, giữ giới hạn baseline. |
| 2.1.4-B01 | Phân biệt VERIFIED FULL TEXT, METADATA ONLY và INFERENCE/PROPOSAL trong ghi chú làm việc. | p[29]–[33] | Được đề cập, giữ giới hạn baseline. |
| 2.1.4-B02 | Chọn một chuẩn trích dẫn duy nhất theo quy định của trường; bảo đảm mọi citation có reference tương ứng. | p[34]–[35]; p[38]–[42] | Được đề cập, giữ giới hạn baseline. |
| 2.1.4-B03 | Không dùng khoảng trống trong kết quả tìm kiếm để tuyên bố universal novelty. | p[36]–[37] | Được đề cập, giữ giới hạn baseline. |

B01 §2.1.2 nêu rõ các bộ lọc và lịch sử chưa có hồ sơ, không bịa giá trị để lấp bullet. B01 §2.1.3 là quy tắc khung, không xác lập mọi paper có đủ chín trường. B02 §2.1.4 dùng IEEE theo quyết định tác giả; mức áp dụng quy định trường chưa xác minh.

## Trạng thái khoa học được bảo toàn

| Đối tượng | Trạng thái |
|---|---|
| H0a | REFUTED_IN_TRANSFORMATION_REGIME |
| H0b | NOT_FALSIFIED_LIVE_COMPETITOR |
| H1 | INSUFFICIENT_EVIDENCE |
| G00 | CLOSED_AS_GENERAL_MECHANISM; chuyển giao MP1 vẫn mở |
| G01–G08 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE; câu hỏi có điều kiện, không đổi trạng thái |
| G09 | PROJECT_PREREQUISITE, không phải literature gap |
| G10 | NOT_ESTABLISHED |
| G11 | PROHIBITED CLAIM; không universal novelty |
| RQ mapping | PROVISIONAL_MANY_TO_MANY; HUMAN_DECISION_PENDING |
| Ma trận | MATRIX_SCHEMA_STATUS=PARTIAL; FULL_NINE_FIELD_COVERAGE=NOT_ESTABLISHED |

Năm quyết định còn mở: topology tiếp xúc; truyền áp suất tới tải pháp tuyến; miền nhiệt/pha/tốc độ/lịch sử TiNi; metric độ cứng và bất định; phạm vi SMA–piston/Bench B. Chưa coi các quyết định này là đóng góp đã xác minh.

## Nhật ký kiểm trực quan

| Trang | Nội dung kiểm | Kết quả quan sát |
|---|---|---|
| 1 | Heading cha/con, nội dung 2.1.1, ba citations khoa học | Đúng thứ bậc; Unicode và citations đọc được; đoạn tiếp qua trang sau bình thường. |
| 2 | Cuối 2.1.1, heading 2.1.2, lịch sử và số liệu truy vết | Không orphan heading; 15/312/258/54/39 được giữ đúng văn bản. |
| 3 | Screening exclusion, nhan đề italic, giới hạn lịch sử, đầu 2.1.3 | Nhan đề đầy đủ/in nghiêng; không mất nhận diện nguồn bị loại; heading có đoạn theo sau. |
| 4 | Quy tắc ma trận, calibration/validation, caption, đầu bảng | Caption đi cùng header và hàng Cơ chế; chữ 12 pt; không tách hàng. |
| 5 | Phần còn lại bảng, source note, đầu 2.1.4 | Header lặp; đủ các hàng Hình học đến Liên quan, không mất ô; source note và heading đọc được. |
| 6 | Các trạng thái, IEEE [4], novelty, H0a/H0b/H1 | Không nhầm [4] với [1]; không mất dấu/ký tự; nội dung đủ. |
| 7 | Danh mục duy nhất gồm [1]–[4] | Bốn entries hiện đủ, DOI/URL có xuống dòng tự nhiên; không clipping hoặc trang trắng. |

Chỉ số hình học PDF theo ký tự khác khoảng trắng, đơn vị pt, không tính trailing spaces:

```json
[
  {
    "page": 1,
    "nonspace_bounds": [
      85.1500015258789,
      79.35877990722656,
      538.2221069335938,
      748.792724609375
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPS-BoldMT",
      "TimesNewRomanPSMT"
    ]
  },
  {
    "page": 2,
    "nonspace_bounds": [
      85.1500015258789,
      71.35877990722656,
      538.1502075195312,
      661.5427856445312
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPS-BoldMT",
      "TimesNewRomanPSMT"
    ]
  },
  {
    "page": 3,
    "nonspace_bounds": [
      85.1500015258789,
      71.35877990722656,
      538.3660888671875,
      671.3927612304688
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPS-BoldMT",
      "TimesNewRomanPS-ItalicMT",
      "TimesNewRomanPSMT"
    ]
  },
  {
    "page": 4,
    "nonspace_bounds": [
      85.1500015258789,
      71.35877990722656,
      538.1018676757812,
      748.792724609375
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPSMT"
    ]
  },
  {
    "page": 5,
    "nonspace_bounds": [
      85.1500015258789,
      71.85877990722656,
      538.3299560546875,
      760.792724609375
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPS-BoldMT",
      "TimesNewRomanPSMT"
    ]
  },
  {
    "page": 6,
    "nonspace_bounds": [
      85.1500015258789,
      71.35877990722656,
      538.1380615234375,
      722.9427490234375
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPSMT"
    ]
  },
  {
    "page": 7,
    "nonspace_bounds": [
      85.1500015258789,
      71.35877990722656,
      536.0021362304688,
      308.6927795410156
    ],
    "font_sizes": [
      12.0
    ],
    "fonts": [
      "TimesNewRomanPS-BoldMT",
      "TimesNewRomanPS-ItalicMT",
      "TimesNewRomanPSMT"
    ]
  }
]
```
## Kết luận tự rà soát

P1_P2_UNRESOLVED_IN_SCOPE: 0
OUT_OF_SCOPE_FINDINGS: 1, OOS-01 mức P3
FINAL_SELF_REVIEW_DECISION: SELF_REVIEW_ONLY
NEXT_ACTION: AWAIT_INDEPENDENT_SECTION_2_1_INTEGRATION_ACCEPTANCE

Chưa có independent acceptance hoặc human approval cho bản tích hợp.
