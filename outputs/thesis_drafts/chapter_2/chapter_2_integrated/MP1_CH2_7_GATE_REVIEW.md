# Bảy Gate sau hotfix, hồ sơ hiện hành

TASK_ID: MP1-CH2-FULL-INTEGRATION-GATE1-HOTFIX

STATUS: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED

Các phần hiện hành dưới đây thay thế trạng thái trước hotfix cho đúng hai DOCX có hash đã ghi. Hồ sơ trước hotfix được giữ nguyên ở cuối tệp để bảo toàn lịch sử. Không cấp nghiệm thu độc lập.

| Tài liệu | SHA-256 DOCX | SHA-256 PDF mới | Số trang đã xem |
|---|---|---|---|
| CHAPTER_DOCX | 72a9409fa22f1d838b3e756d35255a91300b23c442ea4f5f36b8e9f2d5f59cb9 | 5ac4b2cdef6c1565baecb101be43be6b72d24ee8462ce286bb1b3cf170160c2b | 73/73 |
| APPENDIX_STAGING_DOCX | ecde6516319f24708f18a6eeda830f145b8c74edd5c76f654b1303fe4ee4e1ad | 2e988070f51ff096036e11083ed3bd697ce9582e42660ddc1935422b91662802 | 32/32 |

## G1

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đọc lại65 bullet cùng paragraph/table thực tế sau hotfix; kiểm17 nhóm; phân xử lại chỗ kết đoạn và bốn patch; kiểm không còn glossary/heading phụ trong chapter. |
| EVIDENCE | outline-review-input.json; outline-self-review.json; outline-placement-recheck.json; outline-root-adjudication.json; nội dung chi tiết ngay dưới. |
| COUNTS | 53 COVERED;12 COVERED_WITH_BOUNDARY;0 PARTIAL_EDITORIAL;0 NOT_COVERED;17 nhóm có tổng hợp;0 glossary trong chapter. |
| FINDINGS | Đủ nội dung theo cách hiểu cuối phần lập luận. Bốn bảng hỗ trợ theo sau synthesis được giữ. Không có P2 còn mở trong tự kiểm. |
| SEVERITY | P3 về ranh giới diễn giải; không P2 |
| UNRESOLVED | Nghiệm thu độc lập chưa thực hiện; chính sách trường và quyết định khoa học vẫn mở. |
| FINAL_DECISION | Đạt tự kiểm với giới hạn; CH2-OUTLINE-01=RESOLVED trong phạm vi tự kiểm. |

## G2

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đối chiếu mọi paragraph/table trước/sau bằng văn bản và C14N; kiểm prefix XML hai paragraph nối câu; hai paragraph mới đúng nguyên văn duyệt; so sánh P3 và hash nguồn. |
| EVIDENCE | structural-validation.json::scientific_preservation; node-relocation-manifest.json; patches.json; bảng trạng thái khoa học dưới. |
| COUNTS | 4 claim biên tập mới;0 source fact thay đổi;2 paragraph nối câu,2 paragraph chèn;0 nội dung gốc bị mất. |
| FINDINGS | AUTHOR_METHOD_SYNTHESIS/INFERENCE/PROPOSAL; không chọn topology, truyền áp, tham số, metric hoặc Bench; không nâng H1 hay bác H0b. |
| SEVERITY | P3 kế thừa |
| UNRESOLVED | Năm quyết định khoa học; không tái đọc toàn bộ PDF sơ cấp. |
| FINAL_DECISION | Bảo toàn ý nghĩa khoa học trong phạm vi biên tập đã duyệt. |

## G3

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đọc lại6 source CSV/DOCX, so tập913 khóa và original_record_json; lần theo native XML object sang đích thật; tìm lại span bằng văn bản/thứ tự xuất hiện rồi reopen kiểm offset; union coverage mọi ký tự w:t. |
| EVIDENCE | Hai cột target_document/target_anchor_container trong master; structural-validation.json::anchors/coverage; source support mới trong editorial_supports_json. |
| COUNTS | 913/913 original record;2935 trace row;2857 source+2935 target=5792 neo exact;1578 row chapter/1357 row appendix;0 gap. |
| FINDINGS | 2859 row gốc giữ; thêm4 NEW_EDITORIAL_CLAIM và72 STRUCTURAL_RECORD. Giữ5 ARCHIVAL_SUPPORT_ONLY. 14 thuật ngữ§2.1 chỉ có section-scope mapping, không bịa neo literal. |
| SEVERITY | P3 về độ hạt bằng chứng kế thừa |
| UNRESOLVED | 0 unresolved anchor;0 unexplained claim loss; mức neo nguồn rộng vẫn giữ rõ. |
| FINAL_DECISION | Đạt đối soát hai tài liệu; không đồng nghĩa mọi claim được tái xác minh ở cấp câu PDF. |

## G4

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đọc citation từ Word ngoài bibliography, kiểm source identity, thứ tự xuất hiện1–30, từng lineage/token/span ở cả hai đích; kiểm canonical DOI và metadata Crowley. |
| EVIDENCE | MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv; structural-validation.json::citations; appendix-index-map.json. |
| COUNTS | 328 chapter;485 appendix=455 original+30 chỉ mục;783/783 original accounted;30 reference mỗi đích;30 shared identity;0 missing/orphan/conflict. |
| FINDINGS | Giữ nguyên số dẫn trong ô để C14N bảng nguyên vẹn. Chỉ mục định danh của phụ lục mở đầu thứ tự số tạm; map số bằng nhau được xác minh theo identity, không suy từ số. IEEE guide đã có ở baseline. |
| SEVERITY | P3 về chính sách trường chưa xác minh |
| UNRESOLVED | School policy giữ mở; numbering phụ lục tạm thời, chờ tích hợp luận văn. |
| FINAL_DECISION | Đạt toàn vẹn citation/reference; không thêm nguồn khoa học. |

## G5

| Trường | Giá trị |
|---|---|
| STATUS | PASS |
| METHOD | So toàn bộ976 cell text/raw/C14N,286 hàng, table geometry/merged/header flags/native OOXML và10 đoạn dẫn/caption; so19OMML,figure XML/media hash; kiểm bookmarks và cross reference ở hai tệp. |
| EVIDENCE | Manifest glossary trong changelog; crosswalk86 row; structural-validation.json::objects/glossary; ảnh các trang công thức. |
| COUNTS | 21→16 bảng chapter;5 appendix;286 hàng;1→1 hình;19→19OMML;278 bookmark chapter+143 appendix;0 dangling/duplicate. |
| FINDINGS | Không có field/hyperlink/footnote/endnote cần chuyển quan hệ trong các bảng. Không có cross-reference trỏ sang bookmark đã chuyển. A.1/A.2 là nhãn kế thừa. |
| SEVERITY | NONE trong toàn vẹn đối tượng |
| UNRESOLVED | Chính sách numbering cuối cùng chưa được chọn; nội dung đối tượng không bị đổi. |
| FINAL_DECISION | Đạt bảo toàn đối tượng native và quan hệ. |

## G6

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đóng ZIP, tính hash, CRC/XML/relationship; runtime LibreOffice bản sao được sửa8 symlink/fundamentalrc và đường dữ liệu liblangtag, Math hoạt động; render mới2 DOCX; xem riêng từng105 trang150dpi, kiểm thêm19OMML và crop header6. |
| EVIDENCE | render-manifest.json; visual-reviewed-final.json; visual-appendix-root-001-032.json; visual-chapter-critical-root.json; hai findingP3 dưới. |
| COUNTS | 73/73 trang chapter;32/32 appendix;16 XML/rels part mỗi tệp;14/13 relationship;0 dangling. |
| FINDINGS | Khoảng trắng trang39 và font một số ô bảng trang47 kế thừa, đọc được. Finding thiếu header5/6/19 không được xác nhận sau ROOT xem lại. Không sử dụng QA cũ như QA mới. |
| SEVERITY | P3 |
| UNRESOLVED | MICROSOFT_WORD_VALIDATION=NOT_VERIFIED; hai hạn chế trình bày kế thừa. |
| FINAL_DECISION | Đạt kết xuất và rà từng trang trong LibreOffice; không cấp xác nhận Microsoft Word. |

## G7

| Trường | Giá trị |
|---|---|
| STATUS | PASS |
| METHOD | Hash toàn bộ23407 input file,3080 protected file và42 file source package; Git branch/HEAD/diff/cached; kiểm tập file cho phép trước/sau xuất. |
| EVIDENCE | all-input-hashes.json; immutability-prepublish.json; immutability-final.json; final-package-check.json; git-status/diff/cached snapshot. |
| COUNTS | 6 canonical baseline;42 package file;30 protected file ngoài repo;9 deliverable sửa+1 DOCX mới được phép. |
| FINDINGS | Giữ pre-existing work; scientific state/registry không đổi; không đổi branch; không commit/push. |
| SEVERITY | NONE |
| UNRESOLVED | Independent acceptance chưa thực hiện. |
| FINAL_DECISION | Đạt bất biến và đóng gói trong phạm vi được duyệt. |

## Đối chiếu65 bullet sau hotfix

| ID | Bullet chính thức | Trước | Sau | Neo thực tế | Phân xử |
|---|---|---|---|---|---|
| 2.1.1.1 | Giải thích vì sao tổng quan tập trung vào pressure-controlled friction, wire/fiber jamming, TiNi bundle mechanics, contact modeling và validation. | COVERED | COVERED | /w:document/w:body/w:p[4]; /w:document/w:body/w:p[5]; /w:document/w:body/w:p[6]; /w:document/w:body/w:p[7]; /w:document/w:body/w:p[8] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.1.2 | Liên kết từng nhóm tài liệu với RQ1–RQ5 thay vì trình bày lịch sử chung của soft robotics. | COVERED | COVERED | /w:document/w:body/w:p[5]; /w:document/w:body/w:p[6]; /w:document/w:body/w:p[7]; /w:document/w:body/w:p[8]; /w:document/w:body/w:p[9] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.2.1 | Ghi rõ từ khóa, nguồn tìm kiếm, khoảng thời gian thực tế, ngôn ngữ, loại ấn phẩm và cách xử lý bài chỉ có metadata. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[12]; /w:document/w:body/w:p[13]; /w:document/w:body/w:p[14]; /w:document/w:body/w:p[15]; /w:document/w:body/w:p[16]; /w:document/w:body/w:p[17]; /w:document/w:body/w:p[18] | Có nhóm từ khóa, nguồn, mốc thời gian, loại bản ghi và xử lý metadata; hồ sơ nói rõ không phục hồi được chuỗi truy vấn và bộ lọc lịch sử, nên độ tái lập tìm kiếm còn giới hạn. |
| 2.1.2.2 | Đưa vào các nghiên cứu có mechanics/model/validation liên quan; loại hoặc để riêng các bài chỉ trình diễn ứng dụng, controller hoặc vật liệu không liên quan. | COVERED | COVERED | /w:document/w:body/w:p[11]; /w:document/w:body/w:p[15]; /w:document/w:body/w:p[16] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.2.3 | Nêu các nguồn bị loại và lý do nếu người đọc có thể kỳ vọng chúng xuất hiện. | COVERED | COVERED | /w:document/w:body/w:p[17]; /w:document/w:body/w:p[18] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.3.1 | Mỗi nguồn được ghi theo cơ chế, hình học, vật liệu, pressure/load input, model, observables, validation, limitation và relevance. | COVERED | COVERED | /w:document/w:body/w:p[20]; /w:document/w:body/w:p[21]; /w:document/w:body/w:p[22]; /w:document/w:body/w:p[27]; /w:document/w:body/w:tbl[1]; /w:document/w:body/w:p[28] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.3.2 | Nhóm chính theo câu hỏi và cơ chế; dùng chronology bên trong nhóm khi cần giải thích sự phát triển. | COVERED | COVERED | /w:document/w:body/w:p[23] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.3.3 | Cuối mỗi nhóm phải có synthesis paragraph nêu điểm thống nhất, điểm mâu thuẫn và hệ quả cho MP1-R. | PARTIAL_EDITORIAL | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[24]; /w:document/w:body/w:p[25]; /w:document/w:body/w:p[26]; /w:document/w:body/w:p[81]; /w:document/w:body/w:p[214] | Đủ17 nhóm có đoạn tổng hợp ở cuối phần lập luận. Bốn nhóm2.3.1/2.3.2/2.3.4/2.3.5 có bảng hỗ trợ đi sau; bảng/caption không thay thế paragraph. Root kiểm nội dung điểm chung, ranh giới đối chiếu và hệ quảMP1, chấp nhận cách bố trí cuối phần lập luận. Không bịa mâu thuẫn thực nghiệm khi thiếu so sánh đồng điều kiện. Cách hiểu vị trí này được ghi để nghiệm thu độc lập. |
| 2.1.4.1 | Phân biệt VERIFIED FULL TEXT, METADATA ONLY và INFERENCE/PROPOSAL trong ghi chú làm việc. | COVERED | COVERED | /w:document/w:body/w:p[30]; /w:document/w:body/w:p[31]; /w:document/w:body/w:p[32]; /w:document/w:body/w:p[33]; /w:document/w:body/w:p[34] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.1.4.2 | Chọn một chuẩn trích dẫn duy nhất theo quy định của trường; bảo đảm mọi citation có reference tương ứng. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[35]; /w:document/w:body/w:p[36] | Bản thảo dùng một chuẩn IEEE và nối trích dẫn với danh mục; quy định riêng của trường/chương trình vẫn cần xác nhận trước nộp. |
| 2.1.4.3 | Không dùng khoảng trống trong kết quả tìm kiếm để tuyên bố universal novelty. | COVERED | COVERED | /w:document/w:body/w:p[37]; /w:document/w:body/w:p[38] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.1.1 | Định nghĩa vật thể, dầm tương đương, độ cứng vật liệu, độ cứng uốn và độ cứng đầu công tác. | COVERED | COVERED | /w:document/w:body/w:p[41]; /w:document/w:body/w:p[42]; /w:document/w:body/w:p[43]; /w:document/w:body/w:p[44]; /w:document/w:body/w:p[45]; /w:document/w:body/w:p[46]; /w:document/w:body/w:p[47]; /w:document/w:body/w:p[48]; /w:document/w:body/w:p[49] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.1.2 | Giải thích điều kiện khi dùng mô hình dầm và khi chuyển động tương đối giữa các phần tử làm mô hình dầm đơn không còn đủ. | COVERED | COVERED | /w:document/w:body/w:p[50]; /w:document/w:body/w:p[51]; /w:document/w:body/w:p[52]; /w:document/w:body/w:p[53]; /w:document/w:body/w:p[54] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.2.1 | Phân biệt trạng thái jamming ở cấp kết cấu với stick ở cấp tiếp xúc. | COVERED | COVERED | /w:document/w:body/w:p[56]; /w:document/w:body/w:p[57]; /w:document/w:body/w:p[58] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.2.2 | Định nghĩa partial slip và full slip theo chuyển vị tương đối, không gán chúng trực tiếp cho biến dạng dẻo của dây. | COVERED | COVERED | /w:document/w:body/w:p[59]; /w:document/w:body/w:p[60] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.2.3 | Giải thích vai trò của lịch sử tải, tải đảo chiều và vòng trễ. | COVERED | COVERED | /w:document/w:body/w:p[61]; /w:document/w:body/w:p[62]; /w:document/w:body/w:p[63] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.3.1 | Đặt áp suất là input hoặc traction boundary, không đồng nhất ngay với lực pháp tuyến giữa một cặp dây. | COVERED | COVERED | /w:document/w:body/w:p[65]; /w:document/w:body/w:p[66]; /w:document/w:body/w:p[67]; /w:document/w:body/w:p[68]; /w:document/w:body/w:p[69] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.3.2 | Đưa sơ đồ truyền lực từ nguồn áp suất, màng hoặc ống bao, mạng tiếp xúc đến response M–κ. | COVERED | COVERED | /w:document/w:body/w:p[71]; /w:document/w:body/w:p[72]; /w:document/w:body/w:p[73]; /w:document/w:body/w:p[74] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.2.3.3 | Chỉ ra biến nào đo trực tiếp, biến nào là proxy và biến nào cần calibration. | COVERED | COVERED | /w:document/w:body/w:p[77]; /w:document/w:body/w:p[78]; /w:document/w:body/w:tbl[2]; /w:document/w:body/w:p[79]; /w:document/w:body/w:p[80] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.1.1 | Tóm tắt các nhóm tạo lực đối kháng, vật liệu nhạy nhiệt, khóa ma sát, thay đổi cấu hình và jamming. | COVERED | COVERED | /w:document/w:body/w:p[84]; /w:document/w:body/w:p[85]; /w:document/w:body/w:p[86]; /w:document/w:body/w:p[87]; /w:document/w:body/w:p[88] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.1.2 | Dùng bảng so sánh ngắn, không dành nhiều trang cho cơ chế không liên quan trực tiếp đến bó dây TiNi. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[89]; /w:document/w:body/w:tbl[3]; /w:document/w:body/w:p[90] | Có bảng so sánh ngắn và đoạn nối cơ học tới MP1; mức độ cô đọng vẫn là lựa chọn biên tập. |
| 2.3.2.1 | Tổng hợp hình học bó sợi, cơ chế tăng lực ma sát, trạng thái dính–trượt và các phép đo uốn. | COVERED | COVERED | /w:document/w:body/w:p[92]; /w:document/w:body/w:p[93]; /w:document/w:body/w:p[94]; /w:document/w:body/w:p[95]; /w:document/w:body/w:p[96] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.2.2 | Đối chiếu những mô hình và kết quả có thể chuyển sang bó TiNi, đồng thời ghi rõ khác biệt vật liệu, packing và biên. | COVERED | COVERED | /w:document/w:body/w:p[96]; /w:document/w:body/w:p[97]; /w:document/w:body/w:p[98] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.3.1 | Giải thích nguyên lý chung của khóa chuyển vị tương đối. | COVERED | COVERED | /w:document/w:body/w:p[100]; /w:document/w:body/w:p[101]; /w:document/w:body/w:p[102]; /w:document/w:body/w:p[103]; /w:document/w:body/w:p[104] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.3.2 | Chỉ ra khác biệt topology tiếp xúc, truyền áp suất và failure mode; không dùng tương đồng tên gọi để chuyển mô hình trực tiếp. | PARTIAL_EDITORIAL | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[101]; /w:document/w:body/w:p[102]; /w:document/w:body/w:p[103]; /w:document/w:body/w:p[104]; /w:document/w:body/w:p[105]; /w:document/w:body/w:p[106]; /w:document/w:body/w:tbl[5]; /w:document/w:body/w:p[107] | Đoạn sau Bảng 2.3.3 nay nêu khác biệt topology, đường truyền áp và phân biệt trượt lớp được báo cáo với failure mode chưa được xác định ở các kiến trúc còn lại. Chưa có tiêu chuẩn hư hỏng định lượng chung; giới hạn này được nói rõ, không giả lập mâu thuẫn hoặc ngưỡng cho MP1. |
| 2.3.4.1 | Tổng hợp các công trình pressure-dependent, gồm cả prior art gần năm 2025–2026 nếu đã được kiểm tra toàn văn. | COVERED | COVERED | /w:document/w:body/w:p[109]; /w:document/w:body/w:p[110]; /w:document/w:body/w:p[111]; /w:document/w:body/w:p[112]; /w:document/w:body/w:p[113]; /w:document/w:body/w:p[114]; /w:document/w:body/w:p[115]; /w:document/w:body/w:p[116]; /w:document/w:body/w:p[117]; /w:document/w:body/w:p[118]; /w:document/w:body/w:p[119] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.4.2 | Phân biệt pressure source, pressure at specimen, threshold load, stiffness trong từng miền và trạng thái trượt. | COVERED | COVERED | /w:document/w:body/w:p[109]; /w:document/w:body/w:p[110]; /w:document/w:body/w:p[111]; /w:document/w:body/w:p[112]; /w:document/w:body/w:p[113]; /w:document/w:body/w:p[114]; /w:document/w:body/w:p[115]; /w:document/w:body/w:p[116]; /w:document/w:body/w:p[117]; /w:document/w:body/w:p[118]; /w:document/w:body/w:p[119]; /w:document/w:body/w:p[120]; /w:document/w:body/w:p[121] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.4.3 | Kết luận rõ positive pressure, fiber bundle, state-transition model và bending validation đã có tiền lệ ở architecture khác; đây là ranh giới prior art cho MP1-R. | COVERED | COVERED | /w:document/w:body/w:p[119]; /w:document/w:body/w:p[120] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.5.1 | Chốt điều gì đã được xác lập về cơ chế và điều gì còn phụ thuộc hình học, contact topology, membrane/sleeve và cách đo. | COVERED | COVERED | /w:document/w:body/w:p[123]; /w:document/w:body/w:p[124]; /w:document/w:body/w:p[125]; /w:document/w:body/w:p[126]; /w:document/w:body/w:p[127]; /w:document/w:body/w:p[128]; /w:document/w:body/w:p[130]; /w:document/w:body/w:p[131] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.3.5.2 | Chuyển sang câu hỏi hẹp hơn về TiNi, pressure transfer và khả năng nhận dạng. | COVERED | COVERED | /w:document/w:body/w:p[129]; /w:document/w:body/w:p[130] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.1.1 | Giải thích vai trò của nhiệt độ, ứng suất, lịch sử tải, rate và chuyển pha đối với mô đun và vòng trễ. | COVERED | COVERED | /w:document/w:body/w:p[134]; /w:document/w:body/w:p[135]; /w:document/w:body/w:p[136]; /w:document/w:body/w:p[137]; /w:document/w:body/w:p[138]; /w:document/w:body/w:p[139]; /w:document/w:body/w:p[140]; /w:document/w:body/w:p[141]; /w:document/w:body/w:p[142]; /w:document/w:body/w:p[143]; /w:document/w:body/w:p[146]; /w:document/w:body/w:p[147] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.1.2 | Chỉ đưa các phương trình hoặc tham số thật sự dùng trong mô hình của luận văn; định nghĩa mọi ký hiệu ngay sau phương trình. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[141]; /w:document/w:body/w:p[143]; /w:document/w:body/w:p[147] | Chỉ giữ phương trình/đại lượng cần cho cơ sở nguồn; chưa bịa mô hình cấu thành cuối cho MP1. |
| 2.4.2.1 | Tổng hợp prior art về wire rope, inter-wire slip, bending hysteresis và mô hình biến dạng riêng hoặc contact. | COVERED | COVERED | /w:document/w:body/w:p[149]; /w:document/w:body/w:p[150]; /w:document/w:body/w:p[151]; /w:document/w:body/w:p[152]; /w:document/w:body/w:p[153]; /w:document/w:body/w:p[154]; /w:document/w:body/w:p[155]; /w:document/w:body/w:p[156]; /w:document/w:body/w:p[157]; /w:document/w:body/w:p[158]; /w:document/w:body/w:p[159]; /w:document/w:body/w:p[160]; /w:document/w:body/w:p[161]; /w:document/w:body/w:p[162]; /w:document/w:body/w:p[163] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.2.2 | Phân biệt bó dây thẳng, cáp xoắn, braid và cấu hình có sleeve; không chuyển kết luận giữa chúng nếu chưa kiểm tra hình học. | COVERED | COVERED | /w:document/w:body/w:p[150]; /w:document/w:body/w:p[151]; /w:document/w:body/w:p[152]; /w:document/w:body/w:p[165]; /w:document/w:body/w:p[166] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.3.1 | Đặt các cơ cấu SMA-controlled friction vào đúng interface đã công bố, ví dụ wire– sleeve hoặc wire–tube. | COVERED | COVERED | /w:document/w:body/w:p[168]; /w:document/w:body/w:p[169]; /w:document/w:body/w:p[170]; /w:document/w:body/w:p[171] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.3.2 | Đánh giá giới hạn heating/cooling, lực siết, hysteresis và khả năng tách hiệu ứng vật liệu khỏi hiệu ứng tiếp xúc. | COVERED | COVERED | /w:document/w:body/w:p[172]; /w:document/w:body/w:p[173]; /w:document/w:body/w:p[174]; /w:document/w:body/w:p[175]; /w:document/w:body/w:p[176]; /w:document/w:body/w:p[177] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.3.3 | Không coi thay actuator hoặc vật liệu là novelty độc lập. | COVERED | COVERED | /w:document/w:body/w:tbl[10]; /w:document/w:body/w:p[179]; /w:document/w:body/w:p[180]; /w:document/w:body/w:p[181] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.4.1 | Tổng hợp tiền lệ SMA tạo chuyển vị hoặc áp suất qua piston, pump hoặc chamber. | COVERED | COVERED | /w:document/w:body/w:p[184]; /w:document/w:body/w:p[185]; /w:document/w:body/w:p[186]; /w:document/w:body/w:p[187]; /w:document/w:body/w:p[188]; /w:document/w:body/w:p[189]; /w:document/w:body/w:p[190]; /w:document/w:body/w:p[191]; /w:document/w:body/w:p[192]; /w:document/w:body/w:p[193]; /w:document/w:body/w:p[194]; /w:document/w:body/w:p[195]; /w:document/w:body/w:p[196]; /w:document/w:body/w:p[197]; /w:document/w:body/w:p[198] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.4.4.2 | Phân tích force–stroke–temperature–volume, seal friction, compliance, leakage, pressure transient và cooling. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[201]; /w:document/w:body/w:p[202]; /w:document/w:body/w:p[203]; /w:document/w:body/w:p[204]; /w:document/w:body/w:p[205]; /w:document/w:body/w:p[206]; /w:document/w:body/w:p[207]; /w:document/w:body/w:p[208]; /w:document/w:body/w:p[209] | Có phân tích có điều kiện về lực, hành trình, nhiệt, thể tích, phớt, compliance, rò, transient và cooling; chưa phải dữ liệu piston MP1. |
| 2.4.4.3 | Kết luận rằng Bench B cần được đặc trưng như một hệ nguồn áp trước khi quy kết response của bó dây. | COVERED | COVERED | /w:document/w:body/w:p[210]; /w:document/w:body/w:p[211]; /w:document/w:body/w:p[212]; /w:document/w:body/w:p[213]; /w:document/w:body/w:p[214] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.1.1 | Nêu điều kiện ma sát tĩnh, ma sát động, lực pháp tuyến và ứng suất tiếp tuyến. | COVERED | COVERED | /w:document/w:body/w:p[220]; /w:document/w:body/w:p[221]; /w:document/w:body/w:p[222]; /w:document/w:body/w:p[223]; /w:document/w:body/w:p[224]; /w:document/w:body/w:p[225]; /w:document/w:body/w:p[226]; /w:document/w:body/w:p[235]; /w:document/w:body/w:p[236]; /w:document/w:body/w:p[237]; /w:document/w:body/w:p[238]; /w:document/w:body/w:p[239]; /w:document/w:body/w:p[240]; /w:document/w:body/w:p[241]; /w:document/w:body/w:p[242]; /w:document/w:body/w:p[243] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.1.2 | Chỉ rõ các giả định về hệ số ma sát, phân bố contact, biến dạng nhỏ hoặc lớn và lịch sử tải. | COVERED | COVERED | /w:document/w:body/w:p[228]; /w:document/w:body/w:p[229]; /w:document/w:body/w:p[230]; /w:document/w:body/w:p[231]; /w:document/w:body/w:p[232]; /w:document/w:body/w:p[247]; /w:document/w:body/w:p[248]; /w:document/w:body/w:p[249] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.1.3 | Không đồng nhất full slip với các sợi uốn hoàn toàn độc lập nếu sleeve hoặc ma sát động vẫn tồn tại. | COVERED | COVERED | /w:document/w:body/w:p[232]; /w:document/w:body/w:p[249]; /w:document/w:body/w:p[252] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.2.1 | Xây dựng cận các sợi uốn độc lập và cận tiết diện liên kết chống trượt lý tưởng. | COVERED | COVERED | /w:document/w:body/w:p[254]; /w:document/w:body/w:p[255]; /w:document/w:body/w:p[256]; /w:document/w:body/w:p[257]; /w:document/w:body/w:p[258]; /w:document/w:body/w:p[259]; /w:document/w:body/w:p[260]; /w:document/w:body/w:p[261]; /w:document/w:body/w:p[262]; /w:document/w:body/w:p[263]; /w:document/w:body/w:p[264]; /w:document/w:body/w:p[265]; /w:document/w:body/w:p[266]; /w:document/w:body/w:p[267]; /w:document/w:body/w:p[268]; /w:document/w:body/w:p[269]; /w:document/w:body/w:p[270]; /w:document/w:body/w:p[271] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.2.2 | Ghi rõ giả thiết tuyến tính, hình học, trục trung hòa, điều kiện biên và khi nào các cận không còn kẹp được dữ liệu. | COVERED | COVERED | /w:document/w:body/w:p[257]; /w:document/w:body/w:p[258]; /w:document/w:body/w:p[259]; /w:document/w:body/w:p[260]; /w:document/w:body/w:p[261]; /w:document/w:body/w:p[262]; /w:document/w:body/w:p[263]; /w:document/w:body/w:p[264]; /w:document/w:body/w:p[265]; /w:document/w:body/w:p[266]; /w:document/w:body/w:p[267]; /w:document/w:body/w:p[268]; /w:document/w:body/w:p[269]; /w:document/w:body/w:p[270]; /w:document/w:body/w:p[271]; /w:document/w:body/w:p[277]; /w:document/w:body/w:p[278]; /w:document/w:body/w:p[279]; /w:document/w:body/w:p[280]; /w:document/w:body/w:p[281]; /w:document/w:body/w:tbl[13] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.2.3 | Dùng các cận như baseline, không gọi chúng là mô hình hoàn chỉnh của mẫu thật. | COVERED | COVERED | /w:document/w:body/w:p[282]; /w:document/w:body/w:p[283]; /w:document/w:body/w:p[284] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.3.1 | Định nghĩa độ cứng tiếp tuyến, cát tuyến, ngưỡng trượt, biến dạng còn lại và diện tích vòng trễ. | COVERED | COVERED | /w:document/w:body/w:p[288]; /w:document/w:body/w:p[289]; /w:document/w:body/w:p[290]; /w:document/w:body/w:p[291]; /w:document/w:body/w:p[292]; /w:document/w:body/w:p[293]; /w:document/w:body/w:p[294]; /w:document/w:body/w:p[295]; /w:document/w:body/w:p[296]; /w:document/w:body/w:p[297]; /w:document/w:body/w:p[298]; /w:document/w:body/w:p[299]; /w:document/w:body/w:p[300]; /w:document/w:body/w:p[301]; /w:document/w:body/w:p[302]; /w:document/w:body/w:p[303]; /w:document/w:body/w:p[304]; /w:document/w:body/w:p[305]; /w:document/w:body/w:p[306]; /w:document/w:body/w:p[307]; /w:document/w:body/w:p[308]; /w:document/w:body/w:p[309]; /w:document/w:body/w:p[310]; /w:document/w:body/w:p[311] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.3.2 | Liên hệ từng metric với đường tải, tải dỡ, tốc độ, dwell và chiều dài mẫu. | PARTIAL_EDITORIAL | COVERED | /w:document/w:body/w:p[298]; /w:document/w:body/w:p[299]; /w:document/w:body/w:p[300]; /w:document/w:body/w:p[301]; /w:document/w:body/w:p[302]; /w:document/w:body/w:p[303]; /w:document/w:body/w:p[313]; /w:document/w:body/w:p[314]; /w:document/w:body/w:p[315]; /w:document/w:body/w:p[316]; /w:document/w:body/w:p[317]; /w:document/w:body/w:tbl[14]; /w:document/w:body/w:p[318]; /w:document/w:body/w:p[319]; /w:document/w:body/w:p[321]; /w:document/w:body/w:p[320] | Đoạn hotfix gắn từng nhóm metric với nhánh tải, khoảng đo, tốc độ/lịch sử, chiều dài, mốc dỡ tải và thời gian chờ theo mức liên quan; đoạn cũng giới hạn vòng M–κ tại một tiết diện so với công toàn mẫu. Chưa chọn quy trình thử MP1. |
| 2.5.3.3 | Phân biệt công tiêu tán đo ở mức kết cấu với cơ chế tiêu tán tại một interface. | COVERED | COVERED | /w:document/w:body/w:p[305]; /w:document/w:body/w:p[306]; /w:document/w:body/w:p[307]; /w:document/w:body/w:p[308]; /w:document/w:body/w:p[309]; /w:document/w:body/w:p[310]; /w:document/w:body/w:p[311]; /w:document/w:body/w:p[321] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.4.1 | Phân tích parameter compensation giữa mô đun TiNi, hệ số ma sát, lực pháp tuyến, sleeve compliance và điều kiện gá. | COVERED | COVERED | /w:document/w:body/w:p[324]; /w:document/w:body/w:p[327]; /w:document/w:body/w:p[328]; /w:document/w:body/w:p[329]; /w:document/w:body/w:p[330] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.4.2 | Chỉ ra các phép đo bổ sung hoặc mẫu đối chứng cần thiết để tách wire–wire khỏi wire–sleeve. | COVERED | COVERED | /w:document/w:body/w:p[335]; /w:document/w:body/w:p[336]; /w:document/w:body/w:p[337]; /w:document/w:body/w:p[343]; /w:document/w:body/w:p[344]; /w:document/w:body/w:p[345]; /w:document/w:body/w:p[346] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.4.3 | Đưa uncertainty, repeatability và detection threshold vào tiêu chí đánh giá model. | COVERED | COVERED | /w:document/w:body/w:p[338]; /w:document/w:body/w:p[339]; /w:document/w:body/w:p[340]; /w:document/w:body/w:p[341]; /w:document/w:body/w:p[342]; /w:document/w:body/w:p[344]; /w:document/w:body/w:p[345]; /w:document/w:body/w:p[346]; /w:document/w:body/w:p[347]; /w:document/w:body/w:p[348] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.5.1 | So sánh analytical beam, homogenized/reduced-order, FE/contact và thực nghiệm theo khả năng mô tả, chi phí, tham số cần đo và nguy cơ overfitting. | COVERED | COVERED | /w:document/w:body/w:p[350]; /w:document/w:body/w:p[351]; /w:document/w:body/w:p[352]; /w:document/w:body/w:p[353]; /w:document/w:body/w:p[354]; /w:document/w:body/w:p[355]; /w:document/w:body/w:p[356]; /w:document/w:body/w:p[357]; /w:document/w:body/w:p[358]; /w:document/w:body/w:p[359]; /w:document/w:body/w:p[360]; /w:document/w:body/w:tbl[16]; /w:document/w:body/w:p[361]; /w:document/w:body/w:p[362] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.5.2 | Nêu phương pháp nào dùng để dự đoán, phương pháp nào chỉ dùng làm cận hoặc diễn giải. | COVERED | COVERED | /w:document/w:body/w:p[352]; /w:document/w:body/w:p[353]; /w:document/w:body/w:p[354]; /w:document/w:body/w:p[355]; /w:document/w:body/w:p[356]; /w:document/w:body/w:p[357]; /w:document/w:body/w:p[358]; /w:document/w:body/w:p[359]; /w:document/w:body/w:p[360]; /w:document/w:body/w:tbl[16]; /w:document/w:body/w:p[361]; /w:document/w:body/w:p[362]; /w:document/w:body/w:p[364]; /w:document/w:body/w:p[365] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.5.5.3 | Đặt H0b làm baseline phải được kiểm tra trước khi đề xuất H1. | COVERED | COVERED | /w:document/w:body/w:p[363]; /w:document/w:body/w:p[364]; /w:document/w:body/w:p[365] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.6.1.1 | Jamming, positive pressure, frictional locking, TiNi transformation, inter-wire slip và SMA-to-pressure actuation đều có prior art ở các architecture khác nhau. | COVERED | COVERED | /w:document/w:body/w:p[369]; /w:document/w:body/w:p[370]; /w:document/w:body/w:p[371]; /w:document/w:body/w:p[372]; /w:document/w:body/w:p[373]; /w:document/w:body/w:p[374]; /w:document/w:body/w:p[375]; /w:document/w:body/w:p[376]; /w:document/w:body/w:p[377]; /w:document/w:body/w:p[378]; /w:document/w:body/w:p[379]; /w:document/w:body/w:p[380]; /w:document/w:body/w:p[383] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.6.1.2 | Một số mô hình homogenized, stick–slip hoặc contact-aware đã được validation trong phạm vi riêng của chúng. | COVERED | COVERED | /w:document/w:body/w:p[375]; /w:document/w:body/w:p[376]; /w:document/w:body/w:p[377]; /w:document/w:body/w:p[378]; /w:document/w:body/w:p[383] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.6.2.1 | Interface chi phối chưa được khóa; áp suất tại nguồn chưa được chứng minh là normal traction hữu hiệu. | COVERED | COVERED | /w:document/w:body/w:p[385]; /w:document/w:body/w:p[386]; /w:document/w:body/w:p[387]; /w:document/w:body/w:p[397]; /w:document/w:body/w:p[398]; /w:document/w:body/w:p[399]; /w:document/w:body/w:p[400] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.6.2.2 | Chưa biết H0b có dự đoán được response pressure-dependent khi transformation, contact và sleeve cùng hoạt động trong miền thí nghiệm hay không. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[398]; /w:document/w:body/w:p[399]; /w:document/w:body/w:p[400] | Nội dung được trình bày như câu hỏi, khoảng trống làm việc hoặc điều kiện handoff có thể kiểm tra; chưa khẳng định kết quả, tính mới hay khóa thiết kế. |
| 2.6.2.3 | Chưa có cơ sở để khẳng định cơ chế mới hoặc universal novelty. | COVERED | COVERED | /w:document/w:body/w:p[400] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.6.3.1 | Khoảng trống làm việc là xây dựng và kiểm tra bản đồ interface-specific giữa áp suất gần mẫu, trạng thái tiếp xúc, đáp ứng M–κ và sai lệch mô hình trong miền bất định đã khai báo. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[402]; /w:document/w:body/w:p[403]; /w:document/w:body/w:p[404]; /w:document/w:body/w:p[405]; /w:document/w:body/w:p[406]; /w:document/w:body/w:p[407]; /w:document/w:body/w:p[408]; /w:document/w:body/w:p[409]; /w:document/w:body/w:p[410]; /w:document/w:body/w:p[411]; /w:document/w:body/w:p[413]; /w:document/w:body/w:p[414] | Nội dung được trình bày như câu hỏi, khoảng trống làm việc hoặc điều kiện handoff có thể kiểm tra; chưa khẳng định kết quả, tính mới hay khóa thiết kế. |
| 2.6.3.2 | Đóng góp được chấp nhận nếu nghiên cứu phân biệt được cơ chế hoặc chỉ ra giới hạn của mô hình hiện hữu; kết quả không có hiệu ứng vượt bất định cũng được báo cáo như một kết luận thu hẹp. | COVERED | COVERED | /w:document/w:body/w:p[409]; /w:document/w:body/w:p[410]; /w:document/w:body/w:p[411]; /w:document/w:body/w:p[412]; /w:document/w:body/w:p[413]; /w:document/w:body/w:p[414] | Đã đối chiếu nội dung yêu cầu với các đoạn tại anchor hiện hành trong DOCX; đây là đánh giá độ phủ văn bản, không phải xác minh độc lập tài liệu nguồn. |
| 2.6.4.1 | Bench A phải xác định pressure-only response, repeatability, pressure-transfer proxy và các metric M–κ. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[416]; /w:document/w:body/w:p[417]; /w:document/w:body/w:p[418]; /w:document/w:body/w:p[419]; /w:document/w:body/w:p[420]; /w:document/w:body/w:p[421] | Nội dung được trình bày như câu hỏi, khoảng trống làm việc hoặc điều kiện handoff có thể kiểm tra; chưa khẳng định kết quả, tính mới hay khóa thiết kế. |
| 2.6.4.2 | Bench B phải xác định response của SMA–piston độc lập và so sánh với Bench A ở cùng áp suất gần mẫu. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[422]; /w:document/w:body/w:p[423]; /w:document/w:body/w:p[424]; /w:document/w:body/w:p[425] | Nội dung được trình bày như câu hỏi, khoảng trống làm việc hoặc điều kiện handoff có thể kiểm tra; chưa khẳng định kết quả, tính mới hay khóa thiết kế. |
| 2.6.4.3 | Chỉ chuyển sang phần tích hợp khi geometry, interface, sensor placement, uncertainty và stop criteria đã được khóa. | COVERED_WITH_BOUNDARY | COVERED_WITH_BOUNDARY | /w:document/w:body/w:p[426]; /w:document/w:body/w:p[427]; /w:document/w:body/w:p[428]; /w:document/w:body/w:p[429] | Nội dung được trình bày như câu hỏi, khoảng trống làm việc hoặc điều kiện handoff có thể kiểm tra; chưa khẳng định kết quả, tính mới hay khóa thiết kế. |

## Tổng hợp17 nhóm thực tế

Không dùng số đếm cũ để kết luận. END_PARAGRAPH là paragraph cuối phần lập luận, khác caption hoặc dòng quy nguồn. Các đoạn kết liên tiếp được đọc như một khối tổng hợp; bảng đi sau cung cấp đối chiếu hỗ trợ.

```json
[
  {
    "GROUP_ID": "2.2.1",
    "GROUP_TITLE": "2.2.1. Robot continuum và các đại lượng độ cứng",
    "SOURCE_SECTION": "2.2.1",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[54]",
      "text": "Bởi vậy, đại lượng độ cứng chính của bó dây TiNi phải được chọn theo câu hỏi nghiên cứu, còn quan hệ giữa E, B hoặc EI và K chỉ được xác lập qua một mô hình có điều kiện áp dụng rõ ràng. Độ cứng biểu kiến có thể đồng thời phản ánh vật liệu, hình học, tiếp xúc và điều kiện gá; lựa chọn giữa dầm hiệu dụng và mô tả nhiều phần tử cần dựa trên mục tiêu dự đoán cùng phạm vi kiểm chứng. Trên cơ sở phân biệt các cấp đại lượng này, mục tiếp theo làm rõ thuật ngữ kẹt cơ học, khóa bằng ma sát và trượt.",
      "group_last_element_xpath": "/w:document/w:body/w:p[54]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Dầm tương đương giúp mô tả đáp ứng toàn cục trong miền đã kiểm chứng.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Dầm đơn không cho trường trượt và tiếp xúc riêng; đây là giới hạn mức mô tả, không phải kết quả thực nghiệm mâu thuẫn.",
    "MP1_IMPLICATION": "Chọn E, B/EI hoặc K theo câu hỏi và xác định mức chi tiết trước khi dự đoán.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[53]",
        "exact_text": "Do đó, mô tả đường lực–chuyển vị đã quan sát, dự đoán một điều kiện tải mới và quy kết cơ chế cục bộ là những mục tiêu khác nhau. Một đường cong tổng thể phù hợp chưa đủ để xác định duy nhất sự phân bố tiếp xúc và trượt bên trong, vì mô hình có thể gộp chúng vào tham số hiệu dụng [8]. Với MP1, cần giữ riêng biến dạng từng dây, chuyển vị tương đối, truyền lực qua tiếp xúc, ràng buộc hình học và biến dạng của ống bao hoặc gá nếu có; mức chi tiết cần giữ phụ thuộc đầu ra muốn dự đoán.",
        "trace_ids": [
          "CH2-S2-R0036-A01",
          "CH2-S2-R0037-A01",
          "CH2-S2-R0038-A01",
          "CH2-PRES-0087"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.2.2",
    "GROUP_TITLE": "2.2.2. Jamming, frictional locking và slip",
    "SOURCE_SECTION": "2.2.2",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[63]",
      "text": "Đối với MP1, giao diện chi phối là dây–dây, dây–ống bao hay cả hai vẫn chờ quyết định hình học và đường truyền lực. Thay đổi độ cứng lực–chuyển vị K chỉ là quan sát toàn cục, chưa chứng minh giao diện nào đã trượt hoặc cho phép chọn hệ số ma sát và ngưỡng trượt. Bước tiếp theo là phân biệt áp suất cấp với tải pháp tuyến tại tiếp xúc, trước khi dùng ma sát để giải thích đáp ứng của bó dây.",
      "group_last_element_xpath": "/w:document/w:body/w:p[63]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Kẹt là trạng thái cấp kết cấu; dính và trượt là trạng thái giao diện.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Vòng trễ có thể đến từ ma sát hoặc chuyển pha TiNi; các nguồn khác cấp đo, chưa có mâu thuẫn trực tiếp.",
    "MP1_IMPLICATION": "Xác định giao diện chi phối và lịch sử tải trước khi suy cơ chế từ K.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[63]",
        "exact_text": "Đối với MP1, giao diện chi phối là dây–dây, dây–ống bao hay cả hai vẫn chờ quyết định hình học và đường truyền lực. Thay đổi độ cứng lực–chuyển vị K chỉ là quan sát toàn cục, chưa chứng minh giao diện nào đã trượt hoặc cho phép chọn hệ số ma sát và ngưỡng trượt. Bước tiếp theo là phân biệt áp suất cấp với tải pháp tuyến tại tiếp xúc, trước khi dùng ma sát để giải thích đáp ứng của bó dây.",
        "trace_ids": [
          "CH2-S2-R0085-A01",
          "CH2-S2-R0086-A01",
          "CH2-S2-R0087-A01",
          "CH2-PRES-0097"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M17-E01",
            "locator": "Fig. 1 caption",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE"
          },
          {
            "paper_or_evidence_id": "M17-E01",
            "locator": "Fig. 1 caption",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE"
          },
          {
            "paper_or_evidence_id": "M17-E01",
            "locator": "Fig. 1 caption",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE"
          }
        ]
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.2.3",
    "GROUP_TITLE": "2.2.3. Áp suất cấp và lực pháp tuyến",
    "SOURCE_SECTION": "2.2.3",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[81]",
      "text": "Như vậy, có thể mô tả áp suất như đầu vào hoặc điều kiện biên khi vị trí đo, mặt chịu tải và quy ước áp suất đã rõ, nhưng tiếp xúc cục bộ và đáp ứng M–κ vẫn phụ thuộc cấu hình cùng mô hình truyền tải. Đối với MP1, cần giữ rõ giao diện, đại lượng đo hay suy ra, giả thiết và miền độ không đảm bảo trước khi phát biểu quan hệ áp suất–tiếp xúc. Sự phân biệt này đặt cơ sở cho phân loại các kiến trúc jamming ở mục 2.3, chưa chốt luật tiếp xúc hoặc quy trình thí nghiệm. Các tài liệu được đối chiếu ở đây làm rõ những cấp đại lượng và phương pháp đo khác nhau, nhưng chưa cung cấp phép so sánh đồng điều kiện để xác nhận một quan hệ truyền lực chung hoặc kết luận về mâu thuẫn thực nghiệm trực tiếp.",
      "group_last_element_xpath": "/w:document/w:body/w:p[81]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Áp suất là đầu vào hoặc điều kiện biên khi mặt và vị trí đo rõ.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Áp suất nguồn, áp suất gần mẫu và traction cục bộ khác cấp; không có so sánh đồng điều kiện để xác nhận mâu thuẫn thực nghiệm.",
    "MP1_IMPLICATION": "Giữ riêng đại lượng đo, đại lượng suy ra, giao diện và bất định.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[79]",
        "exact_text": "Kết quả nhận dạng phải giữ riêng với đo trực tiếp: Zhang và Yao suy hệ số ma sát hiệu dụng từ quan hệ tải chuyển trạng thái–áp suất trong mô hình của họ [1]. Tác giả cũng nêu truyền áp suất không đều và nén cục bộ do túi phồng cùng trạng thái xếp bó là các nguyên nhân khả dĩ của biến thiên tải bắt đầu trượt [1]. Các nguyên nhân này là khả năng cần khảo sát, không phải từng cơ chế đã được tách và xác nhận bằng phép đo traction.",
        "trace_ids": [
          "CH2-S2-R0177-A01",
          "CH2-S2-R0178-A01",
          "CH2-S2-R0179-A01",
          "CH2-PRES-0131"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID",
            "locator": "§5.1, parameter identification",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          },
          {
            "paper_or_evidence_id": "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID",
            "locator": "§5.2, paragraph below Fig. 6",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          },
          {
            "paper_or_evidence_id": "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID",
            "locator": "§5.2, paragraph below Fig. 6",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[80]",
        "exact_text": "Độ phân tán giữa các lần lặp chỉ phản ánh một phần thông tin về độ không đảm bảo; GUM còn xét hiệu chỉnh, độ phân giải, các đại lượng ảnh hưởng và giả thiết của phương pháp [14]. Sai số không đồng nghĩa với độ không đảm bảo [14]. Độ không đảm bảo mở rộng U được lập từ độ không đảm bảo chuẩn kết hợp và hệ số phủ đã nêu [14]. Các đại lượng dẫn xuất dùng chung kênh đầu vào không tự độc lập; hiệp phương sai có ý nghĩa phải được xét trong mô hình đo [14]. Hiệu chuẩn trên dữ liệu dùng nhận dạng chưa phải kiểm chứng dự báo độc lập, và tương quan áp suất–đáp ứng chưa đủ xác định nguyên nhân tiếp xúc.",
        "trace_ids": [
          "CH2-S2-R0180-A01",
          "CH2-S2-R0181-A01",
          "CH2-S2-R0182-A01",
          "CH2-S2-R0183-A01",
          "CH2-S2-R0184-A01",
          "CH2-PRES-0132"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID",
            "locator": "§3.3.2, sources of uncertainty",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          },
          {
            "paper_or_evidence_id": "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID",
            "locator": "§3.2.2, Note 2",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          },
          {
            "paper_or_evidence_id": "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID",
            "locator": "§3.3.6–3.3.7",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          },
          {
            "paper_or_evidence_id": "M38-E03",
            "locator": "§5.2.1–5.2.2, Eq. (13)",
            "verification_status": "SOURCE_VERIFIED_SELECTED_PASSAGE; anchor verified"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[81]",
        "exact_text": "Như vậy, có thể mô tả áp suất như đầu vào hoặc điều kiện biên khi vị trí đo, mặt chịu tải và quy ước áp suất đã rõ, nhưng tiếp xúc cục bộ và đáp ứng M–κ vẫn phụ thuộc cấu hình cùng mô hình truyền tải. Đối với MP1, cần giữ rõ giao diện, đại lượng đo hay suy ra, giả thiết và miền độ không đảm bảo trước khi phát biểu quan hệ áp suất–tiếp xúc. Sự phân biệt này đặt cơ sở cho phân loại các kiến trúc jamming ở mục 2.3, chưa chốt luật tiếp xúc hoặc quy trình thí nghiệm.",
        "trace_ids": [
          "CH2-S2-R0185-A01",
          "CH2-S2-R0186-A01",
          "CH2-S2-R0187-A01",
          "CH2-PRES-0133"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.3.1",
    "GROUP_TITLE": "2.3.1. Phân loại cơ chế",
    "SOURCE_SECTION": "2.3.1",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[88]",
      "text": "Nhìn trên cùng một trục cơ học, các nguyên lý cấp cao và các kiến trúc kẹt cơ học đều làm thay đổi khả năng chống biến dạng bằng cách thay đổi lực đối kháng, tính chất vật liệu hoặc mức độ ràng buộc giữa các phần tử. Tuy nhiên, hình học môi trường tiếp xúc, điều kiện biên, cách tạo lực nén và đại lượng đo quyết định khả năng chuyển giao mô hình hoặc kết quả. Bốn nguồn được kiểm chứng ở đây không xác nhận hình thái tiếp xúc dây–dây hay dây–bao của bó TiNi và không thiết lập quan hệ áp suất nguồn–lực pháp tuyến cho MP1. Vì vậy, Mục 2.3.2 sẽ phân tích sâu hơn các kiến trúc kẹt dây và kẹt sợi, trong đó hình thái kết nối và trạng thái trượt của bó TiNi vẫn phải được xác định bằng bằng chứng riêng.",
      "placement": "Đoạn tổng hợp cuối phần lập luận, bảng hỗ trợ theo sau."
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Các nguyên lý cùng thay đổi sức kháng biến dạng; đoạn nêu rõ các cách tạo lực, thay đổi vật liệu và ràng buộc.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Hình học tiếp xúc, biên, lực nén và đại lượng đo khác nhau. Không có phép so sánh đồng điều kiện để khẳng định mâu thuẫn thực nghiệm.",
    "MP1_IMPLICATION": "Yêu cầu xác định riêng topology dây–dây/dây–bao và trạng thái trượt cho MP1.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[89]",
        "exact_text": "Nhìn trên cùng một trục cơ học, các nguyên lý cấp cao và các kiến trúc kẹt cơ học đều làm thay đổi khả năng chống biến dạng bằng cách thay đổi lực đối kháng, tính chất vật liệu hoặc mức độ ràng buộc giữa các phần tử. Tuy nhiên, hình học môi trường tiếp xúc, điều kiện biên, cách tạo lực nén và đại lượng đo quyết định khả năng chuyển giao mô hình hoặc kết quả. Bốn nguồn được kiểm chứng ở đây không xác nhận hình thái tiếp xúc dây–dây hay dây–bao của bó TiNi và không thiết lập quan hệ áp suất nguồn–lực pháp tuyến cho MP1. Vì vậy, Mục 2.3.2 sẽ phân tích sâu hơn các kiến trúc kẹt dây và kẹt sợi, trong đó hình thái kết nối và trạng thái trượt của bó TiNi vẫn phải được xác định bằng bằng chứng riêng.",
        "trace_ids": [
          "CH2-S3-R0008-A01",
          "CH2-S3-R0009-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M05-E02;M06-E01;M09-E01;M10-E01",
            "locator": "Fig. 5(g)/Table 4; Fig. 2; Fig. 2; Fig. 1",
            "verification_status": "INFERENCE"
          },
          {
            "paper_or_evidence_id": "M05-E02;M06-E01;M09-E01;M10-E01",
            "locator": "Respective figures/tables",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[91]",
        "exact_text": "Nguồn: tổng hợp từ các tài liệu [12], [15], [16], [17] trong danh mục tài liệu tham khảo của mục này.",
        "trace_ids": [
          "CH2-PRES-0300"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED_WITH_BOUNDARY",
    "UNRESOLVED": "Không thiếu synthesis thực chất; cách bố trí trước bảng hỗ trợ chờ người nghiệm thu độc lập xác nhận. Không có mâu thuẫn đồng điều kiện được tự suy ra.",
    "PRE_HOTFIX_REVIEW_FINDING": "PARTIAL_EDITORIAL"
  },
  {
    "GROUP_ID": "2.3.2",
    "GROUP_TITLE": "2.3.2. Wire/fiber jamming",
    "SOURCE_SECTION": "2.3.2",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[97]",
      "text": "Khả năng chuyển giao sang bó dây TiNi phải được xem xét riêng theo vật liệu và chuyển pha của dây, cách xếp phần tử, hình thái tiếp xúc dây–dây hoặc dây–bao, độ mềm của bao, điều kiện biên, đường truyền áp suất và đại lượng đo. Một đường lực–độ võng hoặc mô men–góc có thể cho thấy đáp ứng toàn hệ thay đổi, nhưng tự nó không phân biệt được thay đổi vật liệu, hình học, lực pháp tuyến và trượt tại giao diện. Do đó, Brancadoro và cộng sự cùng Bai và cộng sự cung cấp bằng chứng trực tiếp cho các biến hình học, vật liệu và giao diện của kiến trúc dây/sợi; Narang và cộng sự cùng Zhang và Yao chỉ đặt ranh giới so sánh về trạng thái dính–trượt, áp suất và mô hình giảm bậc. Các giới hạn này dẫn sang Mục 2.3.3, nơi các kiến trúc kẹt lớp/tấm và kẹt hạt được dùng làm nhóm so sánh theo hình thái tiếp xúc và đường truyền áp suất.",
      "placement": "Đoạn tổng hợp cuối phần lập luận, bảng hỗ trợ theo sau."
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Các kiến trúc dây/sợi cho thấy ghép nối tiếp xúc và trạng thái dính–trượt chi phối đáp ứng uốn; đoạn trước đoạn kết đối chiếu rõ nguồn gần và nguồn tương tự.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Bó sợi áp suất dương, bó dây chân không và chồng lớp khác hình học, vật liệu, biên, áp suất và metric; đoạn phân loại nguồn trực tiếp với nguồn chỉ dùng làm ranh giới. Chưa có mâu thuẫn đồng điều kiện.",
    "MP1_IMPLICATION": "Đoạn kết yêu cầu kiểm riêng TiNi, packing, dây–dây/dây–bao, màng, biên, truyền áp và đại lượng đo.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[98]",
        "exact_text": "Khả năng chuyển giao sang bó dây TiNi phải được xem xét riêng theo vật liệu và chuyển pha của dây, cách xếp phần tử, hình thái tiếp xúc dây–dây hoặc dây–bao, độ mềm của bao, điều kiện biên, đường truyền áp suất và đại lượng đo. Một đường lực–độ võng hoặc mô men–góc có thể cho thấy đáp ứng toàn hệ thay đổi, nhưng tự nó không phân biệt được thay đổi vật liệu, hình học, lực pháp tuyến và trượt tại giao diện. Do đó, Brancadoro và cộng sự cùng Bai và cộng sự cung cấp bằng chứng trực tiếp cho các biến hình học, vật liệu và giao diện của kiến trúc dây/sợi; Narang và cộng sự cùng Zhang và Yao chỉ đặt ranh giới so sánh về trạng thái dính–trượt, áp suất và mô hình giảm bậc. Các giới hạn này dẫn sang Mục 2.3.3, nơi các kiến trúc kẹt lớp/tấm và kẹt hạt được dùng làm nhóm so sánh theo hình thái tiếp xúc và đường truyền áp suất.",
        "trace_ids": [
          "CH2-S3-R0019-A01",
          "CH2-S3-R0020-A06"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M07-E01;M08-E01;M09-E01;M13-E01",
            "locator": "Respective figures/abstract",
            "verification_status": "INFERENCE"
          },
          {
            "paper_or_evidence_id": "M07-E01;M08-E01;M09-E01;M13-E01",
            "locator": "Respective figures/abstract",
            "verification_status": "NOT_APPLICABLE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:tbl[5]",
        "exact_text": "Nghiên cứuBố trí dây/sợi; vật liệu và baoTiếp xúc và tảiĐường kích hoạt/áp suấtĐại lượng uốn hoặc quan sátGiới hạn khi liên hệ với MP1Brancadoro và cộng sự [18]Mô-đun silicone; sợi bông phủ sáp (waxed cotton) dạng lược liên kết. Mô-đun A không giữ lòng rỗng; Mô-đun B giữ lòng rỗng 4,5 mm.Tiếp xúc sợi–sợi; mô-đun thẳng và cong.Buồng sợi hút chân không; nguồn không báo cáo lực tiếp xúc cục bộ.Lực cản ở trạng thái thẳng và cong; đánh giá khả năng thay đổi độ cứng của mô-đun.Không phải bó dây TiNi; hình thái lược, silicone và điều kiện biên khác.Bai và cộng sự [16]Dây kraft, gai dầu hoặc nylon khoảng 1 mm trong bao HDPE kín khí; tiết diện chữ nhật hoặc tròn.Dây–dây và dây–bao; uốn và xoắn; cách xếp phần tử ảnh hưởng tái sắp xếp.Chân không; bao HDPE kín khí được hàn kín trong cấu trúc chữ nhật.Lực–độ võng khi uốn và mô men–góc khi xoắn; Nguồn dùng hai phép thử riêng cho uốn và xoắn; không so sánh trực tiếp trị số của hai đại lượng này.Vật liệu, đường kính, bao và mô hình không tương đương bó dây TiNi.Narang và cộng sự [9] — nguồn so sánhChồng lá/tấm giấy trong bao kín khí; không phải môi trường dây/sợi.Tiếp xúc lớp–lớp; lực cắt dọc và trượt khi vượt tải tới hạn.Chân không tạo chênh áp; trạng thái tiền-trượt, chuyển tiếp và trượt hoàn toàn.Độ cứng uốn thay đổi theo trạng thái trượt; không cùng đại lượng quan sát với mọi mẫu dây/sợi.Chỉ dùng để so sánh dính–trượt và điều kiện biên; không chuyển ngưỡng trượt sang MP1.Zhang và Yao [1] — nguồn so sánhBó sợi trong bóng tạo áp suất dương và mắt xích cứng.Tiếp xúc sợi trong cấu trúc bị ràng buộc; thử uốn ba điểm.Áp suất dương; thử 0–300 kPa trong nguyên mẫu của bài báo.Tải tới hạn và độ cứng trên các nhánh kẹt/chuyển tiếp/trượt; mô hình tham số hiệu dụng.Không phải dây TiNi; bóng tạo áp suất, mắt xích cứng, áp suất dương và tham số hiệu chỉnh khác MP1.",
        "trace_ids": [],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED_WITH_BOUNDARY",
    "UNRESOLVED": "Không thiếu synthesis thực chất; cách bố trí trước bảng hỗ trợ chờ người nghiệm thu độc lập xác nhận. Không có mâu thuẫn đồng điều kiện được tự suy ra.",
    "PRE_HOTFIX_REVIEW_FINDING": "PARTIAL_EDITORIAL"
  },
  {
    "GROUP_ID": "2.3.3",
    "GROUP_TITLE": "2.3.3. Layer/laminar và granular jamming như nhóm so sánh",
    "SOURCE_SECTION": "2.3.3",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[107]",
      "text": "Bảng 2.3.3 cho thấy các kiến trúc kẹt lớp và kẹt hạt khác nhau về mạng tiếp xúc, đường truyền tải và điều kiện giam giữ. Trượt giữa các lớp được ghi nhận là một cơ chế giới hạn trong cấu hình của Crowley và cộng sự, trong khi các trường hợp còn lại chủ yếu cung cấp thông tin về cơ chế giam giữ và giới hạn diễn giải. Các dữ liệu được tổng hợp chưa thiết lập một tiêu chuẩn hư hỏng định lượng chung cho bốn cấu hình. Vì vậy, cần phân biệt chuyển trạng thái đã được báo cáo, cơ chế hư hỏng và thông tin chưa được xác định, thay vì chuyển trực tiếp một ngưỡng hư hỏng sang bó dây TiNi.",
      "group_last_element_xpath": "/w:document/w:body/w:p[107]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Giam giữ và tiếp xúc hạn chế chuyển động tương đối, có thể tăng sức kháng uốn.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Topology, đường áp và failure/transition khác nhau; chỉ Crowley có trượt lớp được nêu như cơ chế giới hạn trong đoạn tổng hợp. Chưa có chuẩn hư hỏng chung hoặc mâu thuẫn định lượng.",
    "MP1_IMPLICATION": "Không chuyển ngưỡng hư hỏng hay luật lớp/hạt trực tiếp sang MP1.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[106]",
        "exact_text": "So sánh bốn cấu hình cho thấy giới hạn chuyển giao nằm ở ít nhất sáu yếu tố liên kết: hình thái tiếp xúc của phần tử chịu tải, môi trường truyền áp hoặc truyền lực, mức độ giam giữ, đường đi của áp suất, tập đại lượng quan sát và dạng hư hỏng hoặc chuyển trạng thái. Các nghiên cứu trước chứng minh rằng tiếp xúc bị giam giữ có thể điều biến độ cứng, nhưng không chứng minh một luật vật liệu duy nhất cho mọi tổ hợp lớp, hạt, màng và khung. Vì vậy, các bằng chứng này chưa xác lập hình thái tiếp xúc, luật vật liệu hay tính mới của MP1; chúng chỉ đặt ra nhu cầu kiểm tra mô hình trượt đồng nhất trong cấu hình mục tiêu và miền tải tương ứng. Mục 2.3.4 sẽ phân tích riêng các công trình kẹt dưới áp suất dương và các miền chuyển trạng thái, thay vì gộp các cấu hình khác nhau thành một cơ chế tương đương.",
        "trace_ids": [
          "CH2-S3-R0026-A01",
          "CH2-S3-R0027-A06",
          "CH2-S3-R0028-A01",
          "CH2-S3-R0029-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M06-E02;M10-E01;M11-E01;M12-E01",
            "locator": "Respective figures",
            "verification_status": "INFERENCE"
          },
          {
            "paper_or_evidence_id": "M06-E02;M10-E01;M11-E01;M12-E01",
            "locator": "Respective figures",
            "verification_status": "NOT_APPLICABLE"
          },
          {
            "paper_or_evidence_id": "M06-E02;M10-E01;M11-E01;M12-E01",
            "locator": "Respective figures",
            "verification_status": "NOT_APPLICABLE"
          },
          {
            "paper_or_evidence_id": "M06-E02;M10-E01;M11-E01;M12-E01",
            "locator": "Respective figures",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:tbl[6]",
        "exact_text": "Nghiên cứu/cấu trúcMôi trường tiếp xúcPhương thức tạo tảiCơ chế hạn chế chuyển vịChuyển tiếp hoặc giới hạn được báo cáoGiới hạn đối chiếu với MP1Caro và Carmichael [12] — kẹt lớp/tấm chân khôngChồng lớp mềm trong khoang kín khí; tiếp xúc lớp–lớp.Hút khí tạo chênh áp; áp suất khí quyển ép khoang và chồng lớp.Sức kháng ma sát đối với trượt giữa lớp tăng, hạn chế chuyển vị tương đối và tăng độ cứng uốn.Nguồn xác nhận cơ chế khóa; không báo cáo phân bố lực pháp tuyến cục bộ hay tiêu chuẩn hư hỏng trong mô tả nguồn này.Không chuyển trực tiếp sang topology dây hoặc bó TiNi.Crowley và cộng sự [19] — kẹt lớp/tấm áp suất dươngLớp Mylar trong khung PETG phân đoạn, túi TPU và thân gripper.Túi bơm phồng ép lớp vào khung cứng; lớp nằm về phía trong vùng cong.Tăng lực nén và ma sát giữa lớp; bố trí lớp chịu kéo để giảm xu hướng oằn.Trượt giữa lớp vẫn là cơ chế giới hạn/chuyển tiếp; kết quả phụ thuộc cấu hình gripper.Không phải dầm layer-jamming tổng quát; không chuyển trực tiếp sang MP1.Liu và cộng sự [17] — kẹt hạt áp suất dươngBóng cao su, hạt SMP bao quanh bóng và ống vải không co giãn.Áp suất dương làm bóng phồng; lực truyền qua hạt đến ống bao.Mạng tiếp xúc hạt–hạt và hạt–biên bị nén, làm tăng sức kháng của cụm.Tải uốn bên ngoài tạo độ võng công xôn; mạng hạt và biên giam giữ chi phối độ cứng; đáp ứng phụ thuộc phân bố hạt, mức nạp và độ mềm bóng.Không chuyển mô hình hạt–bao hoặc kích thước mẫu sang MP1.Huynh và cộng sự [20] — cơ cấu kép kẹt hạt/uốnHạt Al₂O₃ trong khoang PDMS; vi bơm chất lưu điện liên hợp tạo hai nhánh áp suất.Áp suất âm tạo kẹt hạt; áp suất dương làm Pneu-Net cong.Hai đường áp suất có vai trò cơ học khác nhau trong cùng thân PDMS.Áp suất tích hợp và đáp ứng hệ phụ thuộc hiệu chuẩn vi bơm; không phải luật vật liệu chung.Không chuyển hành vi vi bơm hoặc áp suất hai nhánh sang piston SMA của MP1.",
        "trace_ids": [],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.3.4",
    "GROUP_TITLE": "2.3.4. Positive-pressure jamming và các miền trạng thái",
    "SOURCE_SECTION": "2.3.4",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[120]",
      "text": "Như vậy, bằng chứng hiện có cho phép dùng các công trình trên làm chuẩn đối chiếu về đường truyền áp suất, tải tới hạn và miền trượt, nhưng không cho phép xem p, Q_J, Q_S hoặc độ cứng của một kiến trúc là các đại lượng trực tiếp của kiến trúc khác. Phần tiếp theo sẽ tổng hợp các tiêu chí so sánh giữa mô hình, phép đo và kiểm chứng trong nhóm nghiên cứu kẹt.",
      "placement": "Đoạn tổng hợp cuối phần lập luận, bảng hỗ trợ theo sau."
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Đoạn tổng hợp nêu áp suất dương ở hạt và bó sợi, cùng các miền chuyển trạng thái và kiểm chứng uốn đã có tiền lệ.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Đoạn nêu không gộp quan hệ áp suất–độ cứng do topology và giả thiết khác; p, Q_J, Q_S và độ cứng không cùng định nghĩa. Không có mâu thuẫn đồng điều kiện được xác nhận.",
    "MP1_IMPLICATION": "Đoạn yêu cầu kiểm riêng vật liệu TiNi, packing, interface, nhiệt, biên và metric; không suy ra luật hoặc tính mới.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[120]",
        "exact_text": "Như vậy, bằng chứng hiện có cho phép dùng các công trình trên làm chuẩn đối chiếu về đường truyền áp suất, tải tới hạn và miền trượt, nhưng không cho phép xem p, Q_J, Q_S hoặc độ cứng của một kiến trúc là các đại lượng trực tiếp của kiến trúc khác. Phần tiếp theo sẽ tổng hợp các tiêu chí so sánh giữa mô hình, phép đo và kiểm chứng trong nhóm nghiên cứu kẹt.",
        "trace_ids": [
          "CH2-S3-R0040-A02",
          "CH2-S3-R0042-A02"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M06-E02;M07-E03;M10-E01;M13-E06",
            "locator": "Fig.3c;Fig.3;Fig.1;Conclusion",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:tbl[7]",
        "exact_text": "Nghiên cứu / kiến trúcMôi trường và đường truyền áp suấtĐại lượng đoMiền trạng thái / mô hìnhBằng chứng kiểm chứngGiới hạn đối chiếu với MP1Kẹt lớp chân không [12], [9]Lớp mềm trong khoang kín; khí quyển nén chồng lớp khi hút chân không.Uốn ba điểm; lực–độ võng; tải tới hạn.Trước trượt, chuyển tiếp, trượt hoàn toàn; mô hình dầm và FE.N = 5–20; 0–71 kPa chân không; R² nhỏ nhất 0,9879 trong tập đã báo cáo [9].Áp suất âm; không có trường áp suất cục bộ; chưa chứng minh ngoại suy số lớp cao.Kẹt hạt áp suất dương [17]Bóng cao su → hạt SMP → ống vải không giãn.Công xôn; lực–chuyển vị; độ cứng trong 1 mm đầu.Đáp ứng cấp hệ thống; không có luật tiếp xúc cục bộ.69–172 kPa áp suất dư; đo lặp và khoảng tin cậy.Không đo lực tiếp xúc; ảnh hưởng đồng thời của bóng, mạng hạt và hình học.Kẹt sợi áp suất dương [1]Bóng polyethylene nén bó 700 sợi nylon trong mắt xích cứng.Uốn ba điểm; Q_J, Q_S; độ cứng theo miền.Q < Q_J: kẹt; Q_J–Q_S: chuyển tiếp; Q > Q_S: trượt hoàn toàn.0–300 kPa; 5 lần lặp; μ = 0,3665; R²(Q_S–p) = 0,817.Một nguyên mẫu; p là áp suất hiệu dụng; quan hệ chuyển tiếp hiện tượng học; truyền áp suất không đều.",
        "trace_ids": [],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED_WITH_BOUNDARY",
    "UNRESOLVED": "Không thiếu synthesis thực chất; cách bố trí trước bảng hỗ trợ chờ người nghiệm thu độc lập xác nhận. Không có mâu thuẫn đồng điều kiện được tự suy ra.",
    "PRE_HOTFIX_REVIEW_FINDING": "PARTIAL_EDITORIAL"
  },
  {
    "GROUP_ID": "2.3.5",
    "GROUP_TITLE": "2.3.5. Synthesis của nhóm jamming",
    "SOURCE_SECTION": "2.3.5",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[130]",
      "text": "Như vậy, các công trình trước đã xác lập nguyên lý kẹt, các kiến trúc áp suất và nhiều cách mô hình hóa–đo lường, nhưng mỗi kết luận vẫn gắn với hình thái kết nối, màng hoặc bao, biên, tải và đại lượng quan sát cụ thể. Giới hạn đó dẫn tự nhiên sang mục 2.4, nơi cần xét riêng tính chất TiNi, cơ học tiếp xúc trong bó dây và cơ chế SMA tạo hoặc điều biến áp suất.",
      "placement": "Đoạn tổng hợp cuối phần lập luận, bảng hỗ trợ theo sau."
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Đoạn kết nêu nguyên lý kẹt, các kiến trúc áp suất và mô hình/đo lường đã được xác lập trong miền riêng.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Hình thái kết nối, bao, biên, tải và metric khác nhau; đoạn trước đó phân biệt E, EI, K, áp suất nguồn và traction. Không có mâu thuẫn cùng điều kiện được chứng minh.",
    "MP1_IMPLICATION": "Đoạn trước đoạn kết yêu cầu nhận dạng giao diện, bao, đường piston–tiếp xúc, trạng thái TiNi và đại lượng uốn cho MP1.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[128]",
        "exact_text": "Do đó, các đại lượng được báo cáo phải được giữ riêng. Mô đun Young E là tham số vật liệu, còn độ cứng uốn thường liên quan đến EI hoặc độ dốc lực–độ võng trong một điều kiện biên cụ thể. Tỷ số độ cứng, tải tới hạn, mô men–độ cong và lực–độ võng không phải là cùng một đại lượng đo. Tham số được hiệu chỉnh từ dữ liệu không đồng nghĩa với tham số được đo độc lập; sự phù hợp giữa mô hình và phần tử hữu hạn cũng không thay thế kiểm chứng thực nghiệm. Hơn nữa, áp suất nguồn, áp suất gần mẫu và lực pháp tuyến cục bộ là các biến khác nhau, nên một đáp ứng toàn hệ không đủ để nhận dạng riêng trạng thái tiếp xúc hoặc lực ma sát tại từng giao diện.",
        "trace_ids": [
          "CH2-S3-R0051-A01",
          "CH2-S3-R0054-A06"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M17-E05;M18-E01;M06-E03;M07-E04",
            "locator": "Fig.4;Abstract;Table1;Conclusion",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[129]",
        "exact_text": "Đối với MP1, phần tổng hợp này chuyển câu hỏi sang khả năng nhận dạng của một hệ bó dây TiNi cụ thể. Cần xác định bằng thực nghiệm hình thái kết nối dây–dây hoặc dây–bao, cách xếp phần tử, độ mềm của màng hoặc ống bao, đường truyền từ cơ cấu piston đến tải tiếp xúc, điều kiện biên và đại lượng uốn có thể đo. Đồng thời, phải tách ảnh hưởng của mô đun và chuyển pha TiNi khỏi thay đổi do ma sát hoặc trượt; việc nhận dạng tham số chỉ có ý nghĩa khi các đại lượng quan sát và miền tải đủ phân biệt. Đây là các yêu cầu kiểm chứng của hệ nghiên cứu, không phải kết quả đã được xác nhận hay tuyên bố tính mới.",
        "trace_ids": [
          "CH2-S3-R0052-A01",
          "CH2-S3-R0054-A07",
          "CH2-S3-R0055-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M08-E01;M09-E01;M10-E01;M13-E06",
            "locator": "Fig.2;Fig.2;Fig.1/Fig.6;Conclusion",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[130]",
        "exact_text": "Như vậy, các công trình trước đã xác lập nguyên lý kẹt, các kiến trúc áp suất và nhiều cách mô hình hóa–đo lường, nhưng mỗi kết luận vẫn gắn với hình thái kết nối, màng hoặc bao, biên, tải và đại lượng quan sát cụ thể. Giới hạn đó dẫn tự nhiên sang mục 2.4, nơi cần xét riêng tính chất TiNi, cơ học tiếp xúc trong bó dây và cơ chế SMA tạo hoặc điều biến áp suất.",
        "trace_ids": [
          "CH2-S3-R0053-A01",
          "CH2-S3-R0054-A08",
          "CH2-S3-R0055-A02"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M08-E01;M09-E01;M10-E01;M13-E01",
            "locator": "Respective figures/abstract",
            "verification_status": "NOT_APPLICABLE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:tbl[8]",
        "exact_text": "Nhóm cơ chếTiếp xúc và giam giữĐại lượng đánh giáMô hình / kiểm chứngGiới hạn liên hệ với MP1Dây / sợi [16], [18], [1]Bó phần tử mảnh; dây–dây hoặc dây–bao; bao và cách xếp phần tử chi phối ghép nối.Lực–độ võng, mô men–góc hoặc độ cứng cấp mô-đun.Thực nghiệm và mô hình theo kiến trúc cụ thể.Không xác định hình thái kết nối bó TiNi; đại lượng quan sát và vật liệu khác nhau.Lớp / tấm [12], [9], [10], [11]Lớp–lớp trong màng kín; số lớp, ma sát và biên đỡ ảnh hưởng trượt.Lực–độ võng, tải tới hạn, năng lượng tiêu tán, tỷ số độ cứng.Giải tích, FE và thí nghiệm trong miền giới hạn; có sai lệch ở tải/độ võng lớn.Không chuyển trực tiếp E, EI, ngưỡng trượt hoặc mô hình liên tục sang bó dây.Hạt [17]Mạng hạt–hạt và hạt–biên; bóng khí và ống bao; biên giam giữ truyền tải.Lực–chuyển vị và độ cứng hiệu dụng theo áp suất.Đáp ứng cấp hệ; lực tiếp xúc cục bộ thường không được đo.Áp suất nguồn không phải lực pháp tuyến; hình thái kết nối liên tục của bó dây không tương đương.Tổng hợp mô hìnhMỗi mô hình chọn mức rời rạc, hiệu dụng hoặc liên tục và một đại lượng quan sát riêng.E, EI, độ dốc lực–độ võng, tỷ số độ cứng và tải tới hạn.Hiệu chỉnh tham số, FE–thí nghiệm và kiểm chứng có phạm vi khác nhau.Cần thiết kế phép đo để nhận dạng truyền áp suất và tham số bó TiNi.",
        "trace_ids": [],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED_WITH_BOUNDARY",
    "UNRESOLVED": "Không thiếu synthesis thực chất; cách bố trí trước bảng hỗ trợ chờ người nghiệm thu độc lập xác nhận. Không có mâu thuẫn đồng điều kiện được tự suy ra.",
    "PRE_HOTFIX_REVIEW_FINDING": "PARTIAL_EDITORIAL"
  },
  {
    "GROUP_ID": "2.4.1",
    "GROUP_TITLE": "2.4.1. Chuyển pha và siêu đàn hồi của TiNi",
    "SOURCE_SECTION": "2.4.1",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[147]",
      "text": "Bốn nguồn không cung cấp đủ cơ sở để lựa chọn một mô hình cấu thành cụ thể cho MP1. Tính áp dụng của mô hình phải được xác định theo trạng thái vật liệu, bộ tham số đã nhận dạng và điều kiện tải–nhiệt tương ứng; vì vậy, mục này chỉ giữ mô tả định tính và không đưa thêm phương trình. Trên cơ sở đó, việc dự đoán đáp ứng uốn của bó dây cần xem xét hình học dây, giao diện giữa các dây, bao hoặc ống giam giữ và khả năng chuyển vị tương đối giữa các phần tử ở mục 2.4.2.",
      "group_last_element_xpath": "/w:document/w:body/w:p[147]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "TiNi thay đổi đáp ứng theo trạng thái pha, nhiệt và lịch sử tải.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Cáp 7×7 và 1×27, kéo và uốn, không đồng điều kiện; khác đáp ứng không tự là mâu thuẫn.",
    "MP1_IMPLICATION": "Chưa chọn luật cấu thành MP1; cần xác định trạng thái vật liệu và tham số.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[150]",
        "exact_text": "Bốn nguồn không cung cấp đủ cơ sở để lựa chọn một mô hình cấu thành cụ thể cho MP1. Tính áp dụng của mô hình phải được xác định theo trạng thái vật liệu, bộ tham số đã nhận dạng và điều kiện tải–nhiệt tương ứng; vì vậy, mục này chỉ giữ mô tả định tính và không đưa thêm phương trình. Trên cơ sở đó, việc dự đoán đáp ứng uốn của bó dây cần xem xét hình học dây, giao diện giữa các dây, bao hoặc ống giam giữ và khả năng chuyển vị tương đối giữa các phần tử ở mục 2.4.2.",
        "trace_ids": [
          "CH2-S4-R0020-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "—",
            "locator": "transition paragraph",
            "verification_status": "PROPOSAL"
          }
        ]
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.4.2",
    "GROUP_TITLE": "2.4.2. Bó dây, cáp và chuyển vị tương đối",
    "SOURCE_SECTION": "2.4.2",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[166]",
      "text": "Các nghiên cứu trên cung cấp những mức mô tả khác nhau, gồm sức cản trượt tương đương giữa lớp, giả thiết liên kết trong cáp xoắn và tiếp xúc bề mặt trong mô hình FE có vật liệu SMA. Chúng chưa xác lập cấu trúc ưu tiên cho MP1 và chưa cung cấp một quy luật áp suất dẫn đến ma sát có thể chuyển trực tiếp sang MP1. Khi kế thừa, cần giữ riêng ứng suất tiếp xúc với nguồn tạo áp suất, cũng như phân biệt hiệu chỉnh mô hình từ dữ liệu với kiểm chứng mô hình bằng các đáp ứng đo trong miền áp dụng. Từ cơ sở cơ học của bó dây có tiếp xúc này, mục 2.4.3 xem xét cách tác động của SMA làm thay đổi một mặt tiếp xúc ma sát được xác định rõ.",
      "group_last_element_xpath": "/w:document/w:body/w:p[166]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Mô hình lớp, cáp xoắn và FE đều mô tả tương tác/trượt ở cấp khác nhau.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Hình học tiếp xúc, vật liệu, biến kiểm chứng khác; không thể suy mâu thuẫn giữa các kết quả khác cấp.",
    "MP1_IMPLICATION": "Mô tả cấu trúc thực và tách nguồn áp khỏi ứng suất tiếp xúc trước khi chọn mô hình.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[169]",
        "exact_text": "Các nghiên cứu trên cung cấp những mức mô tả khác nhau, gồm sức cản trượt tương đương giữa lớp, giả thiết liên kết trong cáp xoắn và tiếp xúc bề mặt trong mô hình FE có vật liệu SMA. Chúng chưa xác lập cấu trúc ưu tiên cho MP1 và chưa cung cấp một quy luật áp suất dẫn đến ma sát có thể chuyển trực tiếp sang MP1. Khi kế thừa, cần giữ riêng ứng suất tiếp xúc với nguồn tạo áp suất, cũng như phân biệt hiệu chỉnh mô hình từ dữ liệu với kiểm chứng mô hình bằng các đáp ứng đo trong miền áp dụng. Từ cơ sở cơ học của bó dây có tiếp xúc này, mục 2.4.3 xem xét cách tác động của SMA làm thay đổi một mặt tiếp xúc ma sát được xác định rõ.",
        "trace_ids": [
          "CH2-S4-R0049-A02",
          "CH2-S4-R0052-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M22-E04;M23-E08;M24-E10;M25-E06",
            "locator": "Physical PDF M22:5–7; M23:12–13; M24:9–12; M25:5–6; MP1 applicability synthesis; No new model",
            "verification_status": "INFERENCE"
          }
        ]
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.4.3",
    "GROUP_TITLE": "2.4.3. SMA điều biến ma sát",
    "SOURCE_SECTION": "2.4.3",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[181]",
      "text": "Các công bố [7], [25], [26] xác lập rằng điều biến ma sát bằng tác dụng nhiệt của SMA và kết hợp SMA với cơ chế kẹt đã có tiền lệ. Thay loại bộ chấp hành hoặc vật liệu vì thế chưa đủ để xác lập đóng góp cơ học mới của MP1. Câu hỏi còn phải giải quyết là đường truyền từ đầu ra SMA đến tải tiếp xúc và đáp ứng chịu uốn của cấu trúc đang xét. Nếu đường truyền đó có khâu tạo áp suất, áp suất trong buồng phía piston vẫn cần được phân biệt với tải pháp tuyến cục bộ. Cơ sở cho việc đánh giá khâu tạo và truyền áp suất được xem xét tiếp ở mục 2.4.4.",
      "group_last_element_xpath": "/w:document/w:body/w:p[181]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "SMA điều biến ma sát hoặc ghép với jamming đã có tiền lệ.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Tiếp xúc dây–cao su, hạt và phục hồi vật liệu khác chức năng; chưa có phép so sánh đồng điều kiện.",
    "MP1_IMPLICATION": "Xác định mặt chịu tác động và đường lực từ SMA đến uốn, không nhận thay bộ chấp hành là tính mới.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[184]",
        "exact_text": "Các công bố [7], [25], [26] xác lập rằng điều biến ma sát bằng tác dụng nhiệt của SMA và kết hợp SMA với cơ chế kẹt đã có tiền lệ. Thay loại bộ chấp hành hoặc vật liệu vì thế chưa đủ để xác lập đóng góp cơ học mới của MP1. Câu hỏi còn phải giải quyết là đường truyền từ đầu ra SMA đến tải tiếp xúc và đáp ứng chịu uốn của cấu trúc đang xét. Nếu đường truyền đó có khâu tạo áp suất, áp suất trong buồng phía piston vẫn cần được phân biệt với tải pháp tuyến cục bộ. Cơ sở cho việc đánh giá khâu tạo và truyền áp suất được xem xét tiếp ở mục 2.4.4.",
        "trace_ids": [
          "CH2-S4-R0082-A01"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.4.4",
    "GROUP_TITLE": "2.4.4. SMA–piston và truyền áp suất",
    "SOURCE_SECTION": "2.4.4",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[214]",
      "text": "Các tiền lệ đã cho thấy khả năng ghép lực, hành trình và lưu chất bằng SMA trong những thiết bị cụ thể; vi bơm ECF bổ sung một ví dụ về hai chức năng áp suất khác nhau [3], [20], [27]. Chúng chưa kiểm chứng trọn chuỗi SMA–piston, áp suất tại mẫu, tải tiếp xúc, ma sát và độ cứng uốn của MP1. Vì thế, phần cơ sở tiếp theo cần liên hệ các mô hình tiếp xúc với đại lượng uốn có thể quan sát, rồi mới đặt yêu cầu nhận dạng và kiểm chứng cho hệ thực. Tạo áp suất dương bằng SMA không tự tạo thành một kết luận về tính mới. Điểm chung của các tiền lệ nằm ở chức năng tạo tác động lên lưu chất, trong khi cơ cấu tạo áp, đường truyền tải và điều kiện đánh giá khác nhau; vì vậy chưa có cơ sở so sánh trực tiếp hiệu năng các thiết bị này hay suy ra tính tương đương giữa Bench A và Bench B.",
      "group_last_element_xpath": "/w:document/w:body/w:p[214]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "SMA có thể tạo lực, hành trình và tác động lên lưu chất trong thiết bị nguồn.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Cơ cấu, đường tải và phép đánh giá khác nhau; chưa có so sánh hiệu năng trực tiếp hay tương đương Bench A/B.",
    "MP1_IMPLICATION": "Đặc trưng riêng nguồn và truyền áp trước khi quy đáp ứng cho bó dây.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[214]",
        "exact_text": "Cần phân biệt áp suất nguồn hoặc áp suất buồng tạo áp, áp suất tại mẫu và ứng suất tiếp xúc pháp tuyến tại giao diện dây–dây hoặc dây–bao. Hai áp suất chất lưu có thể khác nhau khi tồn tại dòng, tổn thất và tích trữ thể tích; sự bằng nhau chỉ có thể xét dưới điều kiện cân bằng và đường truyền đã xác định. Ứng suất tiếp xúc pháp tuyến có đơn vị Pa nhưng là lực bề mặt cục bộ, khác lực pháp tuyến có đơn vị N. Phân bố này còn phụ thuộc hình thái tiếp xúc, diện tích thực và phản lực biên. Một số đo áp suất toàn cục chưa xác định duy nhất phân bố ấy hay hệ số ma sát không thứ nguyên. Đường lực–độ võng toàn hệ cũng không cung cấp đủ thông tin để suy ngược duy nhất các tải tiếp xúc.",
        "trace_ids": [
          "CH2-S4-R0112-A01",
          "CH2-S4-R0113-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M12-E01;M33-E01;M34-E02",
            "locator": "M12 §4; M33 §III.A; M34 §2.2/§5.5",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[215]",
        "exact_text": "Dấu âm hoặc dương cần được hiểu so với một mốc áp suất được chỉ rõ. Ở công trình Huynh, các nhãn âm/dương phân biệt hút tạo kẹt với bơm làm phồng; chúng không phải bằng chứng về áp suất tuyệt đối đo trong buồng [20, tr. 6–8]. Trong phân tích của Pierce và Mascaro, biến áp suất thuộc bình tích áp [27, tr. 538]. Các kết quả này không tự xác lập giá trị áp suất tại mẫu TiNi hoặc tải pháp tuyến trên từng tiếp xúc.",
        "trace_ids": [
          "CH2-S4-R0114-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M12-E01;M33-E01;M34-E02",
            "locator": "M12 Figs9–11; M33 Eq4/TableII; M34 Fig12",
            "verification_status": "INFERENCE"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[216]",
        "exact_text": "Để đánh giá một nguồn SMA–piston trong tương lai, luận văn đề xuất xem xét riêng đầu vào điện hoặc nhiệt và nhiệt độ SMA, lực cùng hành trình chịu tải, áp suất với vị trí lấy áp, độ kín và độ mềm hệ, chu kỳ nóng–nguội, rồi đáp ứng cơ học của mẫu. Đây là yêu cầu về thông tin cần có, chưa phải quy trình thực nghiệm được phê duyệt. Hiệu chuẩn phép đo, hiệu chỉnh tham số mô hình và kiểm chứng độc lập phải được phân biệt. Kiểm chứng cần dùng dữ liệu không tham gia hiệu chỉnh, đồng thời khai báo miền tải, trạng thái nhiệt và độ không đảm bảo đo; việc giữ lại dữ liệu tự nó chưa đủ xác nhận cơ chế tiếp xúc.",
        "trace_ids": [
          "CH2-S4-R0115-A01",
          "CH2-S4-R0117-A01"
        ],
        "original_sources": []
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[217]",
        "exact_text": "Các tiền lệ đã cho thấy khả năng ghép lực, hành trình và lưu chất bằng SMA trong những thiết bị cụ thể; vi bơm ECF bổ sung một ví dụ về hai chức năng áp suất khác nhau [3], [20], [27]. Chúng chưa kiểm chứng trọn chuỗi SMA–piston, áp suất tại mẫu, tải tiếp xúc, ma sát và độ cứng uốn của MP1. Vì thế, phần cơ sở tiếp theo cần liên hệ các mô hình tiếp xúc với đại lượng uốn có thể quan sát, rồi mới đặt yêu cầu nhận dạng và kiểm chứng cho hệ thực. Tạo áp suất dương bằng SMA không tự tạo thành một kết luận về tính mới.",
        "trace_ids": [
          "CH2-S4-R0118-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M12-E01;M33-E01;M34-E02",
            "locator": "Các cơ chế và miền kiểm chứng đã nêu",
            "verification_status": "INFERENCE"
          }
        ]
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.5.1",
    "GROUP_TITLE": "2.5.1. Coulomb và chuyển tiếp stick–partial slip–full slip",
    "SOURCE_SECTION": "2.5.1",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[252]",
      "text": "Các giới hạn dính và trượt vì thế chỉ nên được dùng như các giả định biên để xây dựng những cận độ cứng tham chiếu trong mục 2.5.2. Cận full-stick cần giả định rõ dây được ghép như thế nào; cận full-slip cần nêu rõ phần tử nào còn truyền ma sát, sleeve và điều kiện biên có được bỏ qua hay không. Hai cận đó là cấu trúc tham chiếu phụ thuộc hình học và topology, không phải các cận đã đo của MP1. Mục 2.5.2 sẽ xây dựng khung so sánh ở mức đó mà không biến các giả định dính–trượt thành kết luận thực nghiệm cho bó dây TiNi.",
      "group_last_element_xpath": "/w:document/w:body/w:p[252]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Giới hạn Coulomb và trạng thái dính/trượt đều phụ thuộc giao diện và định nghĩa.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Full slip khác nhau giữa lớp, dây và sợi; không phải kết quả cơ học đồng điều kiện mâu thuẫn.",
    "MP1_IMPLICATION": "Dùng full-stick/full-slip làm giả định tham chiếu có điều kiện, không là kết quả đo MP1.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[258]",
        "exact_text": "Các giới hạn dính và trượt vì thế chỉ nên được dùng như các giả định biên để xây dựng những cận độ cứng tham chiếu trong mục 2.5.2. Cận full-stick cần giả định rõ dây được ghép như thế nào; cận full-slip cần nêu rõ phần tử nào còn truyền ma sát, sleeve và điều kiện biên có được bỏ qua hay không. Hai cận đó là cấu trúc tham chiếu phụ thuộc hình học và topology, không phải các cận đã đo của MP1. Mục 2.5.2 sẽ xây dựng khung so sánh ở mức đó mà không biến các giả định dính–trượt thành kết luận thực nghiệm cho bó dây TiNi.",
        "trace_ids": [
          "CH2-S5-R0016-A01"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.5.2",
    "GROUP_TITLE": "2.5.2. Hai cận độ cứng tham chiếu",
    "SOURCE_SECTION": "2.5.2",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[284]",
      "text": "Mục 2.5.2 không khẳng định rằng độ cứng đo được của MP1 luôn nằm giữa hai giá trị tham chiếu. Hai mốc này chỉ có thể được tính lại sau khi hình học, trạng thái vật liệu, luật tiếp xúc và đại lượng quan sát được phê duyệt. Bước tiếp theo là xác định đại lượng độ cứng vận hành, nhánh tải–dỡ tải và cách so sánh với M–κ hoặc F–δ; các vấn đề đó được chuyển sang mục 2.5.3.",
      "group_last_element_xpath": "/w:document/w:body/w:p[284]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Hai cận lý tưởng giúp tạo mốc kiểm tra cơ học.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Biên hình học, trạng thái TiNi và tiếp xúc có thể phá điều kiện kẹp dữ liệu; không có mâu thuẫn đồng điều kiện được xác nhận.",
    "MP1_IMPLICATION": "Chỉ tính cận sau khi khóa hình học, trạng thái và đại lượng uốn.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[290]",
        "exact_text": "Mục 2.5.2 không khẳng định rằng độ cứng đo được của MP1 luôn nằm giữa hai giá trị tham chiếu. Hai mốc này chỉ có thể được tính lại sau khi hình học, trạng thái vật liệu, luật tiếp xúc và đại lượng quan sát được phê duyệt. Bước tiếp theo là xác định đại lượng độ cứng vận hành, nhánh tải–dỡ tải và cách so sánh với M–κ hoặc F–δ; các vấn đề đó được chuyển sang mục 2.5.3.",
        "trace_ids": [
          "CH2-S5-R0038-A01"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.5.3",
    "GROUP_TITLE": "2.5.3. M–κ, stiffness và vòng trễ",
    "SOURCE_SECTION": "2.5.3",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[322]",
      "text": "Mục 2.5.4 sẽ tiếp nhận các định nghĩa đại lượng và quy ước nhánh sau khi được lựa chọn, rồi xem xét cách nhận dạng tham số và bất định. Phần này chỉ xác lập điều kiện để một đại lượng có ý nghĩa cơ học, không biến một tỷ lệ hoặc độ dốc của nghiên cứu khác thành luật đo cho bó dây TiNi.",
      "group_last_element_xpath": "/w:document/w:body/w:p[322]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Metric độ cứng, ngưỡng và vòng trễ cần gắn với cấu hình thử.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Nguồn dùng nhánh, chiều dài và đại lượng khác; không có thang độ cứng chung hay mâu thuẫn trực tiếp.",
    "MP1_IMPLICATION": "Khai báo chiều dài, tải–dỡ, tốc độ, dwell và quy tắc tính cho từng metric.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[319]",
        "exact_text": "Bốn nghiên cứu cho thấy chỉ tiêu độ cứng luôn đi cùng cấu hình thử. Nghiên cứu của Narang và cộng sự dùng lực–độ võng của chồng lớp giấy và thay đổi số lớp, chân không hoặc hệ số ma sát mô hình. Nghiên cứu của Brancadoro và cộng sự báo cáo tỷ lệ lực cực đại giữa trạng thái kẹt và không kẹt trong bảng vật liệu; Bai và cộng sự đo cả uốn và xoắn trên cơ cấu kẹt dây; Liu và cộng sự dùng độ dốc lực–độ võng ở 1 mm đầu hành trình để nhận dạng độ cứng và mô đun Young tương đương. Các số liệu này không tạo một thang độ cứng chung.",
        "trace_ids": [
          "CH2-S5-R0053-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "M07-E03;M08-E02;M09-E02;M10-E03",
            "locator": "Cross-study synthesis",
            "verification_status": "VERIFIED_FULL_TEXT"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[325]",
        "exact_text": "Đối với MP1, các chỉ tiêu có thể xem xét gồm độ dốc M–κ, độ dốc lực–độ võng, độ dốc tiếp tuyến hoặc cát tuyến, tỷ lệ thay đổi độ cứng, tải ngưỡng trượt, biến dạng còn lại và công vòng trễ. Mục này không chọn chỉ tiêu chính thức. Mỗi lựa chọn sẽ cần khai báo chiều dài mẫu, hình học và sơ đồ tải, nhánh tải hoặc dỡ tải, khoảng tính độ dốc, tốc độ, thời gian chờ, nhiệt độ và quy ước chu kỳ.",
        "trace_ids": [
          "CH2-S5-R0054-A01",
          "CH2-S5-R0055-A01"
        ],
        "original_sources": []
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[326]",
        "exact_text": "Một đại lượng toàn cục chỉ có thể liên hệ với cơ chế giao diện sau khi đường truyền lực và cấu hình tiếp xúc được xác định. Không được suy ra áp suất nguồn bằng tải pháp tuyến cục bộ, không được suy ra hệ số ma sát từ diện tích vòng lực–độ võng, và không được gộp trễ vật liệu TiNi với trễ ma sát nếu chưa có phép tách cơ chế. Vì thế, khả năng so sánh giữa MP1 và các nguồn trên bị giới hạn bởi sự khác nhau về vật liệu, chiều dài, áp suất, sơ đồ tải và đại lượng quan sát.",
        "trace_ids": [
          "CH2-PRES-1591"
        ],
        "original_sources": []
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[327]",
        "exact_text": "Mục 2.5.4 sẽ tiếp nhận các định nghĩa đại lượng và quy ước nhánh sau khi được lựa chọn, rồi xem xét cách nhận dạng tham số và bất định. Phần này chỉ xác lập điều kiện để một đại lượng có ý nghĩa cơ học, không biến một tỷ lệ hoặc độ dốc của nghiên cứu khác thành luật đo cho bó dây TiNi.",
        "trace_ids": [
          "CH2-S5-R0056-A01"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.5.4",
    "GROUP_TITLE": "2.5.4. Nhận dạng và bất định",
    "SOURCE_SECTION": "2.5.4",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[348]",
      "text": "Các nghiên cứu đã công bố cho thấy có thể dùng lực–độ võng, hồi quy điểm gãy, độ cứng ngang hoặc khóa hình dạng để đánh giá đáp ứng kết cấu của cơ cấu kẹt. Chúng cũng cho thấy các tham số hiệu dụng có thể phù hợp tốt với một nguyên mẫu trong một miền tải. Tuy nhiên, khả năng nhận dạng tham số vật lý phụ thuộc vào thông tin độc lập về áp suất tại mẫu, ứng suất tiếp xúc pháp tuyến, vật liệu, ống bao, đồ gá và trạng thái tiếp xúc. Vì vậy, tiêu chí đánh giá mô hình MP1 phải đồng thời ghi rõ độ lặp lại, bất định đo lường, sai lệch mô hình và ngưỡng phát hiện; độ phù hợp của một đường cong toàn cục không đủ để khẳng định duy nhất về cơ chế dây–dây hoặc dây–ống bao.",
      "group_last_element_xpath": "/w:document/w:body/w:p[348]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Dữ liệu kết cấu có thể khớp tham số hiệu dụng trong miền nguồn.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Khớp toàn cục không nhận dạng riêng dây–dây, dây–bao, áp suất và vật liệu; đây là ranh giới suy luận.",
    "MP1_IMPLICATION": "Yêu cầu quan sát độc lập, độ lặp, bất định, sai lệch và ngưỡng phát hiện.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[353]",
        "exact_text": "Các nghiên cứu đã công bố cho thấy có thể dùng lực–độ võng, hồi quy điểm gãy, độ cứng ngang hoặc khóa hình dạng để đánh giá đáp ứng kết cấu của cơ cấu kẹt. Chúng cũng cho thấy các tham số hiệu dụng có thể phù hợp tốt với một nguyên mẫu trong một miền tải. Tuy nhiên, khả năng nhận dạng tham số vật lý phụ thuộc vào thông tin độc lập về áp suất tại mẫu, ứng suất tiếp xúc pháp tuyến, vật liệu, ống bao, đồ gá và trạng thái tiếp xúc. Vì vậy, tiêu chí đánh giá mô hình MP1 phải đồng thời ghi rõ độ lặp lại, bất định đo lường, sai lệch mô hình và ngưỡng phát hiện; độ phù hợp của một đường cong toàn cục không đủ để khẳng định duy nhất về cơ chế dây–dây hoặc dây–ống bao.",
        "trace_ids": [
          "CH2-PRES-1643"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  },
  {
    "GROUP_ID": "2.5.5",
    "GROUP_TITLE": "2.5.5. So sánh các nhóm phương pháp",
    "SOURCE_SECTION": "2.5.5",
    "END_PARAGRAPH": {
      "xpath": "/w:document/w:body/w:p[366]",
      "text": "Các quyết định về số dây, đường kính, cách bố trí dây, tiếp xúc dây–dây hay dây–ống bao, trạng thái nhiệt của TiNi, đại lượng uốn chính và quy tắc bất định vẫn thuộc về người nghiên cứu. Chưa thể chọn mô hình cuối cùng hoặc quy trình thí nghiệm chỉ từ bốn nguồn so sánh. Sau khi các quyết định đó được chốt, §2.6 có thể tổng hợp những năng lực đã được thiết lập, các giới hạn còn lại và các câu hỏi nghiên cứu mà phương pháp được chọn phải trả lời.",
      "group_last_element_xpath": "/w:document/w:body/w:p[366]",
      "group_last_element_type": "p"
    },
    "SYNTHESIS_PRESENT": true,
    "COMMON_FINDINGS": "Mô hình giải tích, giảm bậc và FE có ích ở cấp chi tiết, phép đo và chi phí khác nhau.",
    "DISAGREEMENTS_OR_COMPARISON_BOUNDARIES": "Hiệu chuẩn, đối chiếu FE và kiểm chứng thực nghiệm khác chức năng; khác kết quả không tự là mâu thuẫn.",
    "MP1_IMPLICATION": "Kiểm H0b trước H1 và chờ quyết định hình học, giao diện, metric, bất định.",
    "SOURCE_SUPPORT": [
      {
        "chapter_xpath": "/w:document/w:body/w:p[368]",
        "exact_text": "Trong bối cảnh MP1, H0b là mô hình đối chứng cạnh tranh cần được kiểm tra trước khi đề xuất H1. Theo định nghĩa đã được chấp nhận, H0b kết hợp mô hình cấu thành TiNi có xét chuyển pha với tiếp xúc Coulomb thông thường, xem áp suất giam giữ p(t) là điều kiện biên ngoài và khóa các tham số vật liệu, ma sát và truyền áp suất bằng các phép hiệu chuẩn độc lập. Trạng thái hiện tại của H0b là chưa bị bác bỏ; chưa có phép dự đoán tiến tới trên đường dữ liệu giữ lại của bó dây MP1 để chứng minh nó đủ hoặc không đủ.",
        "trace_ids": [
          "CH2-S5-R0093-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "P3_CANONICAL",
            "locator": "outputs/execution/MP1-V002/W2-03/MP1_H0a_H0b_H1_HYPOTHESIS_MATRIX.md",
            "verification_status": "VERIFIED_REPOSITORY_RECORD"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[369]",
        "exact_text": "Logic kiểm tra vì vậy phải tuần tự: xác định hình học và cấu hình tiếp xúc; khai báo trạng thái vật liệu và lịch sử tải; chọn đại lượng đầu ra đo được; khóa H0b trên dữ liệu hiệu chuẩn được phê duyệt; giữ nguyên tham số khi dự đoán các đường áp suất–độ cong chưa dùng; rồi so sánh sai lệch với bất định đo và các quan sát cục bộ. Chỉ một phần dư có tính lặp lại, vượt bất định và còn tồn tại sau khi đã kiểm tra cách bố trí dây, biên, nhiệt độ, đường truyền áp suất và sai số đo mới tạo cơ sở có điều kiện để mở H1. H1 ở đây là giả thuyết về một luật ghép cấu thành–tiếp xúc mới giữa động học chuyển pha và ma sát dính–trượt; nó hiện chưa đủ bằng chứng và không phải điều kiện bắt buộc để luận văn có kết quả hợp lệ.",
        "trace_ids": [
          "CH2-S5-R0092-A01",
          "CH2-S5-R0094-A01"
        ],
        "original_sources": [
          {
            "paper_or_evidence_id": "P3_CANONICAL",
            "locator": "outputs/execution/MP1-V002/W2-03/MP1_H0a_H0b_H1_HYPOTHESIS_MATRIX.md",
            "verification_status": "VERIFIED_REPOSITORY_RECORD"
          }
        ]
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[370]",
        "exact_text": "Một mô hình H0b dự đoán tốt trong miền đã định vẫn là kết quả khoa học về miền hiệu lực của cơ học hiện hữu. Ngược lại, mô hình H0b không phù hợp trên một đường khớp đơn lẻ không đủ để yêu cầu luật mới, vì sai lệch có thể do tham số bị bù trừ, cấu hình tiếp xúc chưa đúng, áp suất không được truyền như giả định, hoặc đại lượng quan sát không tương ứng với đại lượng mô hình. Trình tự này cũng ngăn việc đồng nhất mô hình mô tả với mô hình dự đoán, và ngăn việc gọi một mô hình FE phức tạp là chính xác hơn chỉ vì nó có nhiều biến vật lý hơn.",
        "trace_ids": [
          "CH2-PRES-1690"
        ],
        "original_sources": []
      },
      {
        "chapter_xpath": "/w:document/w:body/w:p[371]",
        "exact_text": "Các quyết định về số dây, đường kính, cách bố trí dây, tiếp xúc dây–dây hay dây–ống bao, trạng thái nhiệt của TiNi, đại lượng uốn chính và quy tắc bất định vẫn thuộc về người nghiên cứu. Chưa thể chọn mô hình cuối cùng hoặc quy trình thí nghiệm chỉ từ bốn nguồn so sánh. Sau khi các quyết định đó được chốt, §2.6 có thể tổng hợp những năng lực đã được thiết lập, các giới hạn còn lại và các câu hỏi nghiên cứu mà phương pháp được chọn phải trả lời.",
        "trace_ids": [
          "CH2-S5-R0096-A01"
        ],
        "original_sources": []
      }
    ],
    "STATUS": "COVERED",
    "UNRESOLVED": "Không thấy đối chiếu đồng điều kiện cho mâu thuẫn thực nghiệm trực tiếp; giữ ranh giới so sánh và không suy ra mâu thuẫn."
  }
]
```
## Trạng thái khoa học được bảo toàn

```json
{
  "H0a": "REFUTED_IN_TRANSFORMATION_REGIME",
  "H0b": "NOT_FALSIFIED_LIVE_COMPETITOR",
  "H1": "INSUFFICIENT_EVIDENCE",
  "G00": "CLOSED_AS_GENERAL_MECHANISM",
  "G01–G08": "Giữ toàn bộ trạng thái và điều kiện nguồn; không tái phân xử",
  "G09": "PROJECT_PREREQUISITE",
  "G10": "NOT_ESTABLISHED",
  "G11": "NO_UNIVERSAL_NOVELTY_CLAIM",
  "RQ_MAPPING": "PROVISIONAL_MANY_TO_MANY",
  "HUMAN_DECISIONS_PENDING": 5,
  "SCIENTIFIC_SOURCE_FACTS_CHANGED": 0
}
```
## Kết xuất và review từng trang mới

| Đích | Trang | Đã xem | Trạng thái | Quan sát | SHA-256 PNG |
|---|---|---|---|---|---|
| CHAPTER_DOCX | 1 | True | PASS | Tiêu đề chương và §2.1.1 rõ; thân bài, citation và Unicode không cắt. | 9ce6378f653268396eeb3d9c707e20c1e4f39866180ddab4cfd2380532435a7c |
| CHAPTER_DOCX | 2 | True | PASS | Chuyển trang §2.1.1–2.1.2 hợp lý; đoạn văn đọc được. | 275b522c9d235e4629e65ad554bd735f0d38595d3dcad9a24e3ba14f87d3d145 |
| CHAPTER_DOCX | 3 | True | PASS | Nội dung tiêu chí và heading §2.1.3 rõ; chữ nghiêng tên nguồn còn nguyên. | ef4fba92eb1f5403a2f8d4567a9cbb233993594e73523bf1b2c11eadb2f47474 |
| CHAPTER_DOCX | 4 | True | PASS | Khối nguyên tắc tổng hợp rõ; không tràn lề. | cd4f6b822605802b23a8bd741b86e795f2dbc4bee1cc9dba1d09e32a09c3516b |
| CHAPTER_DOCX | 5 | True | PASS | Bảng 2.1.3 đủ ba cột; ghi nguồn và heading tiếp theo rõ. | 60919abdbb02b5a82eea4d04e3b774bc7b627c9f126f30b4c5bc4744bbb09ab5 |
| CHAPTER_DOCX | 6 | True | PASS | Trạng thái bằng chứng, số dẫn [4] và đoạn cuối không bị cắt. | c2f260435449833e4f58cc6439edd2ff890cc29efcf14a8b2f8838bd7217eb46 |
| CHAPTER_DOCX | 7 | True | PASS | Heading §2.2–2.2.1 và ký hiệu/số mũ rõ. | 58c54609ffe747ec3efa9cd3f67be6b7f8b0800f3f2adf635da9511b1f3a56c4 |
| CHAPTER_DOCX | 8 | True | PASS | Các đại lượng cơ học và đoạn tổng hợp hiển thị đủ; đoạn tiếp sang trang9. | 90b003fa5896851738b50b99bd8177ff165780093248ca44a122ec1a99635fee |
| CHAPTER_DOCX | 9 | True | PASS | Phần kết §2.2.1 và §2.2.2 rõ; ký hiệu κ và phạm vi trượt đọc được. | 43f62c2ffd180d15b0696320762bdefa95875dac51d92778280192a4c366ec5c |
| CHAPTER_DOCX | 10 | True | PASS | Kết §2.2.2 và heading §2.2.3 rõ; không mất dòng ở mép trang. | 9171cfce9772e0b845f7a68e8b3c510a9be3706e924b9990b854bb7c16d85fda |
| CHAPTER_DOCX | 11 | True | PASS_WITH_DOCUMENTED_LIMITATIONS | Đoạn truyền áp suất đầy đủ; khoảng trắng lớn phía dưới do hình được giữ cùng khối ở trang12, không có mất nội dung. | 96e276e88f567e26859f536432ed864d99220739bbe6464d8f5f326950c00175 |
| CHAPTER_DOCX | 12 | True | PASS | Hình 2.2.3-1 đủ hai mạch, mọi nhãn/mũi tên và caption; không cắt hình. | d6ae5eb190db83b624fc7c59d2ab0ce03eae0d2a3e6ce9a847e50427710416aa |
| CHAPTER_DOCX | 13 | True | PASS | Bảng 2.2.3-1 đọc được; đoạn tổng hợp tiếp trang14, không mất dòng. | 8687c5c5fddcdb5f271de1d9039c95ee7d669589dc7618d8c6adbc4d78d3269f |
| CHAPTER_DOCX | 14 | True | PASS | Câu hotfix223 xuất hiện đúng ở cuối đoạn tổng hợp; chuyển §2.3 rõ; không còn bảng glossary. | fbdb011266e60c9e60e6f9093c01b757791d093cec8d0afd5b60b6182486a08f |
| CHAPTER_DOCX | 15 | True | PASS | Bảng 2.3.1 sáu cột rõ, tiếp sang trang16. | e4899ec7b5e81fbe5415cf8e8d4534123c63e08989da97ceabf023be2207d4ba |
| CHAPTER_DOCX | 16 | True | PASS | Header bảng 2.3.1 lặp lại; kết bảng và nguồn rõ; heading §2.3.2 đi cùng nội dung. | d4e0a6e1b853713915487b175fde7ba5df669dc178c2b00360890a83ca601b9e |
| CHAPTER_DOCX | 17 | True | PASS_WITH_DOCUMENTED_LIMITATIONS | Các paragraph kết nhóm2.3.2 đọc được; khoảng trống để bảng kế tiếp giữ cấu trúc. | 48bb6ea30066254d66b07bfd56e8ecb83d9f5bd193be37a8c6002ec13db456b8 |
| CHAPTER_DOCX | 18 | True | PASS | Bảng2.3.2 đủ sáu cột, không tràn trang; heading và phần mở §2.3.3 rõ. | 3ed80eb46a5b7a1d6e2c951a42318853438e20c87e9a26cbad4372b2c9771e3b |
| CHAPTER_DOCX | 19 | True | PASS | Bốn kiến trúc và đoạn so sánh trước bảng2.3.3 hiển thị đầy đủ. | aa590b32bf352db50037a0cd74ab10e65fe879156782b4ff17e34a1b442d308a |
| CHAPTER_DOCX | 20 | True | PASS | Bảng2.3.3 năm hàng đủ sáu cột; đoạn hotfix233 nằm ngay sau bảng, phân biệt chuyển trạng thái và hư hỏng rõ; heading2.3.4 không đơn độc. | 8f10fa317be2707511187e18042253c8cb55cfc3143ad9ca6cad31f28378f049 |
| CHAPTER_DOCX | 21 | True | PASS | Chữ và ba phương trình hiển thị rõ; không thấy nội dung bị cắt ở mép trang. | b746994eeddccceeacbc66c1f2267c18065cad4f9dd91d4355f1521671b7f090 |
| CHAPTER_DOCX | 22 | True | PASS | Bảng 2.3.4 bắt đầu ở cuối trang; tiêu đề và hàng đầu đủ nội dung, lưới bảng rõ. | 3ee0e72bcb26dfa26a60bf4da123068c10cbebb134d8d20c03fe49cc32f93534 |
| CHAPTER_DOCX | 23 | True | PASS | Bảng 2.3.4 tiếp tục với hàng tiêu đề lặp lại; nội dung không bị cắt, heading 2.3.5 tách rõ. | 7140cf78fca3f56936153210ae33a1adadd9ca0f9eb5ed280e964adfcb666fe0 |
| CHAPTER_DOCX | 24 | True | PASS | Bảng 2.3.5 mở đầu với tiêu đề căn giữa; header và hai hàng hiển thị đầy đủ. | 6efca7e134ebc09feae35e2c74c5b74464371db1005016487dcfcc6bd4bcf961 |
| CHAPTER_DOCX | 25 | True | PASS | Bảng 2.3.5 tiếp tục với header lặp; kết thúc bảng trước heading 2.4, không thấy chữ tràn ô. | 49de76c09278309f287cea207ac7f41ba3bb2bb90dc0577009dc344e044884c3 |
| CHAPTER_DOCX | 26 | True | PASS | Văn bản liên tục, đoạn cuối chuyển sang trang kế hợp lý; không thấy ký tự hoặc công thức bị cắt. | 63e56d917e2ab0ea72ad4fdb0d89c85aeae0f696c3b775089420c64dd9d443ab |
| CHAPTER_DOCX | 27 | True | PASS | Bảng 2.4.1 cùng caption và các hàng đọc được; kết thúc bảng và đoạn văn không chồng lấn. | be2cc521e7064ce17b2090658fedae7c26b512c547b25f4e6d91f5c90ddcdca1 |
| CHAPTER_DOCX | 28 | True | PASS | Các heading mục 2.4.2 và đoạn văn rõ; lề và khoảng cách nhất quán. | b30f43cbc4d4ed4d74ca617ac9b2f67312e69ecc4aca067124ca83609c523fca |
| CHAPTER_DOCX | 29 | True | PASS | Văn bản nhiều đoạn nhưng còn đủ lề; không thấy dòng bị cắt hoặc tràn. | b9fa64b3634234a8f6cc8dce52543d844afbd2b0e63d20dc52418c61d89f72de |
| CHAPTER_DOCX | 30 | True | PASS | Văn bản mục 2.4.2 tiếp tục liền mạch; không phát hiện lỗi bố cục. | 89c529ede892f73fc564ea806083602d25f345838e72f289db0028753ed71420 |
| CHAPTER_DOCX | 31 | True | PASS | Bảng 2.4.2 hiện đủ tiêu đề và các hàng; chữ nhỏ hơn thân bài nhưng đọc được ở ảnh 150 dpi. | 2b93f891b6ed1623c0f659d1c17498353fff56c5cedd65c022d4da14ddea44cd |
| CHAPTER_DOCX | 32 | True | PASS | Heading 2.4.3 bắt đầu sau đoạn chuyển mục; thân bài hiển thị đầy đủ. | 31f34450bb7024618ffdd9747d6601dacce82a7114952739d6a109e303168341 |
| CHAPTER_DOCX | 33 | True | PASS | Văn bản và dẫn chiếu liên tục, không thấy ngắt trang bất thường hay nội dung cụt. | a5cffc30acfe4b71d75dff775debbc908f3ada210ae8986ca9b7c3f8fe3f1554 |
| CHAPTER_DOCX | 34 | True | PASS | Bảng 2.4.3 có caption, header và ba hàng rõ; đoạn sau bảng không chồng lấn. | ed103e31f37e4a31652292be5d41db008de917a584e6c94840caca9aaa04ff65 |
| CHAPTER_DOCX | 35 | True | PASS | Heading 2.4.4 và các heading phụ phân cấp dễ nhận biết; không thấy chữ bị cắt. | df0970446f6e19a42d4712cace3582f7f9e1550e30fddcd49aa1e1466a444fd4 |
| CHAPTER_DOCX | 36 | True | PASS | Phương trình Q_out ≥ Q_in hiển thị đủ, chỉ số phụ đọc được; phần văn bản giải thích rõ. | e22188f474577d46d04534766c387880f0983273a205ec425f1230b62ba77601 |
| CHAPTER_DOCX | 37 | True | PASS | Bảng 2.4.4 có viền và các hàng trọn vẹn; cỡ chữ trong ô đọc được. | 76394d6e65502ce27cb2f7d7189b8f4ecd525a142a584216a7ff48c924fd1408 |
| CHAPTER_DOCX | 38 | True | PASS | Các đoạn và heading phụ bố trí rõ; không thấy công thức hoặc văn bản bị cắt. | 888dcc8c19d8d5ac41047c03af0db6b838f1cef85473de35e4b7b27d75faa67b |
| CHAPTER_DOCX | 39 | True | PASS_WITH_DOCUMENTED_LIMITATIONS | Trang chỉ có hai đoạn ở phần trên, khoảng trắng chiếm phần lớn trang. Đây là trang kết mục 2.4.4 trước mục 2.5; cần xem lại ngắt trang/độ đầy trang. | 68c42f6f5d84521824d9e738629485f492ef5ba4f509cc6beb84130c233b103d |
| CHAPTER_DOCX | 40 | True | PASS | Mục 2.5 bắt đầu rõ. Hai bất đẳng thức Coulomb và số phương trình hiển thị đầy đủ, không bị cắt. | 587f1210a279062e65258ca04492e460bb2816dcb2ccfe68bcbb2f30ed478583 |
| CHAPTER_DOCX | 41 | True | PASS | Văn bản nhiều đoạn liên tục; heading phụ ở gần cuối trang còn đủ khoảng cách và không bị cụt. | 583b7eff27b2f062800008054325eeb7c3808ef52a2bb691ec6af559935cdff3 |
| CHAPTER_DOCX | 42 | True | PASS | Ba phương trình (2.5.1-3) đến (2.5.1-5) hiện đầy đủ; ký hiệu chỉ số và dấu toán nhìn rõ. | ba357798fb47d06bbdf9e0517db12f0f400414f4be93b555e442adbab15740a1 |
| CHAPTER_DOCX | 43 | True | PASS | Bảng 2.5.1 có caption/header; các hàng và phần văn bản tiếp theo hiển thị trọn vẹn. | f6d7ed953ca5ef2de984eb02d86e97f69066c0e3ec6439144a1499b4930a8673 |
| CHAPTER_DOCX | 44 | True | PASS | Heading 2.5.2 và các tiểu mục rõ; không thấy lỗi cắt chữ hay khoảng trắng bất thường. | c883fe2bd0bf04ba855b7fac38b6a8993665531dec8cabf18643abad03190dde |
| CHAPTER_DOCX | 45 | True | PASS | Các phương trình tham chiếu (2.5.2-1)–(2.5.2-4) hiển thị đủ, gồm tổng và chỉ số; đoạn giải thích trọn vẹn. | 07daaf96212d87786341af9a2e900886df6614279d1488a1b0d779e718de2091 |
| CHAPTER_DOCX | 46 | True | PASS | Heading phụ và các đoạn văn rõ; không thấy ngắt dòng hoặc cắt nội dung bất thường. | 44751402074f4073d4d2d0ddfbc1723a6f2106704c3bb263af8dcc3bc12808b4 |
| CHAPTER_DOCX | 47 | True | PASS_WITH_DOCUMENTED_LIMITATIONS | Bảng 2.5.2 có cỡ chữ không đồng đều rõ rệt giữa các ô: một số ô/hàng dùng chữ lớn hơn hẳn các ô kế cận, làm hàng cao và bảng khó quét. Xác nhận thêm trên crop 2×; cần chuẩn hóa định dạng ô bảng. | 19198aa08a1367ec21e42ad285c06e2eb78476568096236fa48ea9b31f00df37 |
| CHAPTER_DOCX | 48 | True | PASS | Heading 2.5.3 rõ; các công thức (2.5.3-1)–(2.5.3-4) hiển thị đủ. Chỉ số dưới/trên và số công thức rõ ở ảnh trang và crop 2×. | 2cce656ce9fad62f9efa493662536746f49f305bbc2fd181d2b800083d7fef3c |
| CHAPTER_DOCX | 49 | True | PASS | Công thức vòng trễ (2.5.3-5), (2.5.3-6) đủ ký hiệu tích phân, giới hạn và số; đoạn văn tiếp tục liền mạch. | 574d24ac454ffeac6b4eb254880dccc86386ae8ae147c9504fbd79e58a28b83a |
| CHAPTER_DOCX | 50 | True | PASS | Bảng 2.5.3 bắt đầu cùng caption; tiêu đề cột và các hàng đầu hiển thị, chữ nhỏ nhưng đọc được. | a521e75d02b4ba5c4e89b2223f9235779e64af2bdec103dc1dd58484c252f1d9 |
| CHAPTER_DOCX | 51 | True | PASS | Bảng 2.5.3 tiếp tục với hàng tiêu đề lặp; kết thúc trước heading phụ, không thấy nội dung tràn ô. | b8487b6954170c1513fd0988f2e3c76cd09c5127f10e5d12c0c5de723284b4b8 |
| CHAPTER_DOCX | 52 | True | PASS | Các đoạn văn và heading phụ rõ; không có công thức hoặc chữ bị cắt. | f797c37af89fb58b059a30a6e1853686a3a6617833c9aba0691e5a19be45fd0f |
| CHAPTER_DOCX | 53 | True | PASS | Bảng 2.5.4 có lưới, caption và bốn hàng đủ nội dung; heading sau bảng không đè lên bảng. | 71817dd455fb6f9f5cc74b408cc085ff6575ecb924706a5c26a71be0b852a893 |
| CHAPTER_DOCX | 54 | True | PASS | Văn bản liên tục qua trang; heading phụ và các đoạn dưới không bị chia hoặc cắt bất thường. | 25b2710ec62dc43a15822c6d5603ef4bc868842cc2c8bdfa9fdac417fa463e34 |
| CHAPTER_DOCX | 55 | True | PASS | Heading “Kết luận của mục” và nội dung theo sau rõ; đoạn kết tiếp tục tự nhiên sang trang 56. | 51a6f4cb63fb6201a10012e5dd9473c521f7bb9e0ec5a103486b51e499288aad |
| CHAPTER_DOCX | 56 | True | PASS | Heading 2.5.5 bắt đầu rõ; thân bài dày nhưng còn lề và không thấy dòng bị cắt. | 0b76f917b1ce50654b5ef18dfdf7ab3919805809fd3563036ce1b4e93fba1d43 |
| CHAPTER_DOCX | 57 | True | PASS | Văn bản nhiều đoạn liên tục; đoạn cuối tiếp trang 58, không thấy lỗi dàn trang. | f855f78b3f6b08904cbc2d94d11b1e80d989fea7762dc5a07c6b2c0c690d360f |
| CHAPTER_DOCX | 58 | True | PASS | Bảng 2.5.5 có caption và hàng tiêu đề; các mục phương pháp đọc được, bảng kết thúc trước đoạn giải thích. | 0c9c650075d592e003a4c5ce20354b62aaa4e58779351198d342bdeab4579799 |
| CHAPTER_DOCX | 59 | True | PASS | Heading 2.6 và 2.6.1 phân cấp rõ; nội dung mục mới tiếp tục xuống trang sau. | 7dc91570d97f396ed1f61109e41ddc947f5081b2b8a476ce1f0d4de94167a8cf |
| CHAPTER_DOCX | 60 | True | PASS | Các đoạn văn phủ trang đều; không thấy bảng/công thức hoặc ngắt trang lỗi. | fe1444b12163002a9772054a1f4d5bc23ba21725f71fe2e0c3581f74ef2f25e4 |
| CHAPTER_DOCX | 61 | True | PASS | Văn bản liên tục, khoảng cách đoạn ổn định; không thấy chữ bị cắt. | 67f4e05d7854ddb7a0538b2c10df7a8fbb65d2a685451a870b4a8db27a6b1316 |
| CHAPTER_DOCX | 62 | True | PASS | Heading 2.6.2 xuất hiện gần cuối trang với nội dung bên dưới; còn đủ khoảng trống chân trang. | 65fe0493b0591e5122076cb3f237a24e924d654ee8682b978c40990e83e2066f |
| CHAPTER_DOCX | 63 | True | PASS | Các đoạn phân tích liên tục, không có yếu tố đồ họa hay phương trình bị lỗi hiển thị. | 3e157864e32b30cc19138decbea3ecee4c7e066b94c1dbfdaad4c9e1cadce298 |
| CHAPTER_DOCX | 64 | True | PASS | Văn bản dày nhưng không tràn lề; đoạn cuối tiếp tục tự nhiên sang trang 65. | 27137ff24668839875b0f016b5dfae3a424ca4598dea8787dcd6a3dc05b89646 |
| CHAPTER_DOCX | 65 | True | PASS | Heading 2.6.3 rõ; các đoạn văn và đoạn chuyển mục không bị chồng lấn. | ca8ea0e2c0b994e8d9b0065d7245bf48ba5ea8064525b1971a06c250c4ec9389 |
| CHAPTER_DOCX | 66 | True | PASS | Văn bản liền mạch, lề trên/dưới hợp lý; không thấy ngắt dòng hoặc cắt nội dung bất thường. | d4ae33b66bc810acb44d4e4da0f9b34c7f53eab41507248927c5865541efba62 |
| CHAPTER_DOCX | 67 | True | PASS | Các đoạn kết thúc 2.6.3 bố trí trọn vẹn; heading 2.6.4 bắt đầu ở trang kế tiếp hợp lý. | 2dd845d87e28010190287427f8eaa16642050916ed95acbfc55d7a1bfc782e32 |
| CHAPTER_DOCX | 68 | True | PASS | Heading 2.6.4 và các đoạn văn rõ; không thấy ký tự hoặc dòng bị cắt. | d2969ea24c96db13f43fc99e72b45a0b5ddf7e1bdea177829854d1e8e38ed806 |
| CHAPTER_DOCX | 69 | True | PASS | Văn bản mục 2.6.4 kết thúc trong phần dưới trang, vẫn đủ lề; không thấy lỗi trình bày. | c1f4b2dea3d2e45bf635e21f62e96d5b131040835ed2681f85030ea5dda63887 |
| CHAPTER_DOCX | 70 | True | PASS | Trang kết thúc phần nội dung với bốn đoạn ở nửa trên; khoảng trắng dưới lớn do bibliography mở trang kế tiếp. Ngắt phần rõ, không phải nội dung bị cắt. | ed8cf23d8d61eb82da24df51609566c982fe8319c487ac206302898052579165 |
| CHAPTER_DOCX | 71 | True | PASS | Bibliography bắt đầu bằng heading rõ; mục [1]–[12] đầy đủ. URL mục [4] tự xuống dòng nhưng không bị cắt. | 0489614ded89cdcf158fddad110f5357ed7d6b2a9378500107e1dfd8e352ab3d |
| CHAPTER_DOCX | 72 | True | PASS | Các mục tham khảo [13]–[24] nối tiếp tuần tự, xuống dòng hợp lý; DOI còn đủ trong khổ trang. | 22295a0152883b63f147c7c74a3ee80b823e18b766675dd4545fc0ad5cea7f99 |
| CHAPTER_DOCX | 73 | True | PASS | Các mục [25]–[30] kết thúc danh mục; DOI cuối hiển thị đầy đủ, khoảng trắng chân trang còn lại bình thường. | ff9028989c210b44f64e6033e03a14e26f851e536cbb731c063a32b345a52040 |
| APPENDIX_STAGING_DOCX | 1 | True | PASS | Tiêu đề staging và chỉ mục nguồn[1]–[22] rõ; trang này chưa có bảng. | 86e869315a9fe74a0dd9aaa5c20006a7d91785779a407e84e959f7fd25430771 |
| APPENDIX_STAGING_DOCX | 2 | True | PASS | Chỉ mục[23]–[30], Nhóm1 và đầu bảng§2.2 rõ. | a85c87d27eb699757c5c2d94fdad4539286c643a8e98d4d486e7db4da05a1ba3 |
| APPENDIX_STAGING_DOCX | 3 | True | PASS | Bảng§2.2 tiếp diễn; header lặp, các ô EI/E/K và ký hiệu đọc được. | af08ca95115ba2fa7af8b9146afe514b934f8e009e6be027642dc09151ced108 |
| APPENDIX_STAGING_DOCX | 4 | True | PASS | Bảng§2.2 tiếp diễn; header lặp, không cắt các hàng trượt/lịch sử. | e8701647ba1620ad87ba53415d6cbbd73593be71d4a9d58f98e237080ceaa8a7 |
| APPENDIX_STAGING_DOCX | 5 | True | PASS | Header ba cột hiển thị; hàng Global hysteresis đến Measurement model trọn. | e295eef34d0a02dca1e290b859e182d1add9118847391bb39ab4da95cfcc7767 |
| APPENDIX_STAGING_DOCX | 6 | True | PASS | Header ba cột hiển thị rõ, xác nhận lại crop đầu trang; Nhóm2 và đầu bảngA.1 đi cùng nhau. | 35d8d3a7748d4a022df3fc2d59bd3fab470fca66a202d7945274019ac779839d |
| APPENDIX_STAGING_DOCX | 7 | True | PASS | BảngA.1 năm cột, header lặp; các kiến trúc riêng biệt còn nguyên. | 5ffac96c773713f1f72d17c93f0efa3e35a06ce5dde31507a75c3eee41dea284 |
| APPENDIX_STAGING_DOCX | 8 | True | PASS | BảngA.1 tiếp diễn, header lặp; không mất hàng hoặc chữ. | a2839ce8d2144cae058347149570e81dbf66b94f2831f7cd95a2055d993efd31 |
| APPENDIX_STAGING_DOCX | 9 | True | PASS | BảngA.1 tiếp diễn; nguồn và các khái niệm topology/pressure đọc được. | 2fd231f17d12243efd2f63c6e1a897a4f80a9326338072859a585f2d417b86ea |
| APPENDIX_STAGING_DOCX | 10 | True | PASS | BảngA.1 tiếp diễn; header lặp; các hàng confinement/pressure đủ. | 2e2235132027288e70cbd063cd5036427b28b4c850d6c5745fef1edb41af48d6 |
| APPENDIX_STAGING_DOCX | 11 | True | PASS | BảngA.1 tiếp diễn; chỉ số và ngưỡngQ_J/Q_S đọc được. | c0dc5d8963da39f6fc5440321b8218b3158b540817a7cea5e27044035f341b7e |
| APPENDIX_STAGING_DOCX | 12 | True | PASS | BảngA.1 tiếp diễn; header lặp; các hàng model/measurement đủ. | 382167fb374c79787258bbcaddb3dc8c94f8dc050cacdaef96f4a071d33bc69e |
| APPENDIX_STAGING_DOCX | 13 | True | PASS | BảngA.1 kết thúc với evidence independence; không cắt hàng. | e0e2ca575892b4e3a90c7c55b887a7535c903632f4d7b1e0fee96bf7f267cd05 |
| APPENDIX_STAGING_DOCX | 14 | True | PASS | Nhóm3 và captionA.2 rõ; bảng ba cột không viền theo baseline, header hiện. | e0b97334e7249a1ee94b1261e6b83c420374a3ac283517a9a2f4cec6c94c675f |
| APPENDIX_STAGING_DOCX | 15 | True | PASS | BảngA.2 tiếp diễn; header và các định nghĩa nguồn rõ. | 95bab0f0e899c64ea2e122da602447d57d44a750bbe1883fd88d1991b7415ed6 |
| APPENDIX_STAGING_DOCX | 16 | True | PASS | BảngA.2 tiếp diễn; header lặp; các trạng thái trượt và công thức trong ô đọc được. | cbfb9ce066d5bd49c4ff6ff1cee0dbc8241cc2a579b4cf0a90cc6d6f94227832 |
| APPENDIX_STAGING_DOCX | 17 | True | PASS | BảngA.2 tiếp diễn; header lặp; sức kháng/traction và nguồn rõ. | ffb2150cba119dedf9b644d69566f7c2bd46f0a276c859b9923ee31aaded00c9 |
| APPENDIX_STAGING_DOCX | 18 | True | PASS | BảngA.2 tiếp diễn; header lặp; thermal/history và nguồn không bị cắt. | 0510918bb438cc64efd2ad532d9e16fa99f9fccb258b06c2261cceddc2ce8478 |
| APPENDIX_STAGING_DOCX | 19 | True | PASS | Header English/Tiếng Việt, Định nghĩa và ngữ cảnh, Nguồn hiện rõ; finding thiếu header không được xác nhận. | f923176468d632468536dcf0f5de2a08a487337e9087d8a3167df904a011290c |
| APPENDIX_STAGING_DOCX | 20 | True | PASS | BảngA.2 tiếp diễn; header lặp; Qout/Qin và nguồn rõ. | 1d1e693ec87646cc631cdbbe06f589d6599439939090eeb96b6d92f07b50f253 |
| APPENDIX_STAGING_DOCX | 21 | True | PASS | Cuối bảngA.2 và Nhóm4; bảng§2.5 bắt đầu cùng header; không cắt. | 0a9dcb289c8516c5562a9802ece62a5a449334f050905ab66b1b2a0288d8051a |
| APPENDIX_STAGING_DOCX | 22 | True | PASS | Bảng§2.5 tiếp diễn với header lặp; chữ nhỏ theo baseline còn đọc được. | 5f32832fd6ff5040cb35f0a43f4f7e870c818d5184094c759ad19d9acf73a477 |
| APPENDIX_STAGING_DOCX | 23 | True | PASS | Bảng§2.5 tiếp diễn; header lặp, ký hiệu công liên hợp và nguồn rõ. | 3cb9cc4fdb29d79c296382b62c2a7775831e9eb8d3b967e59139f25c5fbf2e1c |
| APPENDIX_STAGING_DOCX | 24 | True | PASS | Bảng§2.5 tiếp diễn; header lặp; các hàng uncertainty và mô hình đủ. | 98fd7d4773315cd2953859a854dd71e3c7391bd154403943c36279f66f7358d1 |
| APPENDIX_STAGING_DOCX | 25 | True | PASS | Cuối bảng§2.5, Nhóm5 và đầu bảng§2.6 rõ; không mất ngữ cảnh từng nguồn. | 4289f2f0d0d81794f820369b62bc2652b93d9c72033848d8d290f3ccc9ace1b5 |
| APPENDIX_STAGING_DOCX | 26 | True | PASS | Bảng§2.6 tiếp diễn; header lặp; các dòng nhiều ngữ cảnh giữ nguyên. | d1ed37fcc76de1b48256e4b48888ee0207a60fc9ded333ef1cd6c6e89c17adf5 |
| APPENDIX_STAGING_DOCX | 27 | True | PASS | Bảng§2.6 tiếp diễn; hàng Measurement uncertainty dài giữ trong trang; header hiện. | 5c529c86110add1eb7daf40e18ddeb74d48045d55294d33da620a48145b7ea2b |
| APPENDIX_STAGING_DOCX | 28 | True | PASS | Bảng§2.6 tiếp diễn; header lặp; nguồn và trạng thái validation đọc được. | c71adaa42da232e2851c3962229c368694c5e7ae7573f74db1fa0d351eb81f4a |
| APPENDIX_STAGING_DOCX | 29 | True | PASS | Bảng§2.6 tiếp diễn; header lặp; các điều kiện so sánh đọc được. | 8452c540926c0604c0d84769e7c47d205851c71755e2af4a0dadb7241d8aa983 |
| APPENDIX_STAGING_DOCX | 30 | True | PASS | Cuối bảng§2.6 và đầu bibliography[1]–[8] rõ; số dẫn tạm được giải thích. | d327167be5b0d5f9d3d0251422c295c2115ab77e140b849a029ea4f8378a8d42 |
| APPENDIX_STAGING_DOCX | 31 | True | PASS | Bibliography[9]–[21] đầy đủ; Crowley5477–5482 và DOI đúng; không cắt. | 4b17a6b6bc9504ed45aa1fb3662dffbefdf89bd7d0c0073282dedd6644dcf603 |
| APPENDIX_STAGING_DOCX | 32 | True | PASS | Bibliography[22]–[30] đủ; DOI có xuống dòng nhưng không mất chữ. | 16c7df58c4bc5520b3ae2121332f07c8c6dce2f36443be8b35d4e91df3127c76 |

## Phân xử finding thị giác

```json
[
  {
    "id": "CH2-HF-QA-01",
    "document": "CHAPTER_DOCX",
    "page": 39,
    "severity": "P3",
    "status": "DOCUMENTED_LIMITATION",
    "finding": "Khoảng trắng lớn ở cuối§2.4.4.",
    "disposition": "ROOT xác nhận do blank paragraph pre-hotfix p218 có pageBreakBefore kế thừa. Không thêm page break; nội dung và định dạng baseline được giữ. Không clipping hoặc mất luận cứ."
  },
  {
    "id": "CH2-HF-QA-02",
    "document": "CHAPTER_DOCX",
    "page": 47,
    "severity": "P3",
    "status": "DOCUMENTED_LIMITATION",
    "finding": "Cỡ chữ một số ô Bảng2.5.2 không đồng đều.",
    "disposition": "ROOT xác nhận bảng đọc được, không cắt ô. XML bảng khớp baseline nguyên vẹn; chuẩn hóa style nằm ngoài bốn patch được duyệt."
  },
  {
    "id": "CH2-HF-QA-03",
    "document": "APPENDIX_STAGING_DOCX",
    "page": "5;6;19",
    "severity": "NONE",
    "status": "NOT_REPRODUCED_AFTER_ROOT_RECHECK",
    "finding": "Worker báo thiếu header lặp.",
    "disposition": "ROOT xem cả32 trang và crop riêng đầu trang6. Cả5/6/19 có header hiện rõ; PNG/hash trùng manifest. Giữ finding cũ và recheck worker để đối chiếu; không sửa bảng để chữa finding không được xác nhận.",
    "evidence": "appendix-page006-header-root.png"
  }
]
```

## Phương pháp và giới hạn

- Microsoft Word chưa được chạy; MICROSOFT_WORD_VALIDATION=NOT_VERIFIED. LibreOffice24.2.7.2 với Math là công cụ kết xuất.
- Bốn nhóm§2.3.1/2.3.2/2.3.4/2.3.5 có đoạn tổng hợp cuối phần lập luận và bảng hỗ trợ theo sau. Root phân xử đủ nội dung; cách hiểu vị trí được ghi rõ để nghiệm thu độc lập. Không lấy caption hoặc bảng thay paragraph.
- Chỉ tự kiểm. Trạng thái VERIFIED FULL TEXT/METADATA ONLY của nguồn được kế thừa theo lineage, không phải tuyên bố tái đọc toàn bộ PDF. Bốn claim mới là AUTHOR_METHOD_SYNTHESIS và INFERENCE/PROPOSAL.
- Chính sách trích dẫn của trường, ánh xạ RQ tạm thời và năm quyết định khoa học vẫn mở. H0b chưa bị bác bỏ, H1 chưa đủ bằng chứng.
- Mười bốn record thuật ngữ§2.1 chỉ có mapping cấp phạm vi§2.1; định nghĩa nguyên gốc vẫn nằm trong original_record_json. Không tạo bảng thuật ngữ giả hoặc neo một câu không tồn tại.
- Khoảng trắng kế thừa ở trang39 và cỡ chữ chưa đều trong Bảng2.5.2 trang47 vẫn được ghi làP3. Các đối tượng không bị cắt; không sửa style ngoài phạm vi hotfix.
- Nhãn A.1/A.2 và ghi chú nguồn được giữ nguyên trong staging như lịch sử; chưa gán số phụ lục chính thức. Chỉ mục nguồn bổ sung30 lượt dẫn cấu trúc, không bổ sung nguồn khoa học.
- Backend không cung cấp chứng cứ xác minh model thực tế. Cấu hình lời gọi worker được ghi nhận: gpt-6-sol/medium ×1, gpt-6-luna/medium ×2; đây không phải xác nhận backend. Root được yêu cầu GPT-6.1 Sol High, không suy model thực tế từ yêu cầu.

## Hồ sơ trước hotfix, giữ nguyên lịch sử

Mọi số đếm/STATUS/PENDING bên dưới thuộc DOCX baseline trước hotfix, không phải kết quả hiện hành.

# Bảy gate tự rà soát toàn Chương 2

TASK_ID: MP1-CH2-FULL-CHAPTER-INTEGRATION

STATUS: PARTIAL_WITH_FINDINGS

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED

EXECUTION_PLAN_APPROVAL: APPROVED

CONTENT_PATCH_APPROVAL: PENDING

## Trạng thái bằng chứng

VERIFIED FULL TEXT là trạng thái nguồn được kế thừa, không phải chứng nhận tái đọc toàn bộ PDF trong phiên tiếp tục. METADATA ONLY giữ nguyên mức bằng chứng. INFERENCE và PROPOSAL tiếp tục là suy luận và đề xuất. Kiểm mới trong phiên này gồm đối chiếu record nguồn, XPath/offset, coverage văn bản, OOXML, citation và hash. Hồ sơ thị giác là review của phiên trước, được liên kết bằng hash với DOCX/PDF hiện tại. Không xem lại 101 ảnh trong phiên này.

## Gate 1. Dàn ý chính thức

| Trường | Giá trị |
|---|---|
| STATUS | PARTIAL |
| METHOD | Đối chiếu 31 heading và 65 bullet; giữ phân xử cuối cùng trong checkpoint |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 52 COVERED, 10 COVERED_WITH_BOUNDARY, 3 PARTIAL_EDITORIAL |
| FINDINGS | CH2-OUTLINE-01: ba bullet và vị trí năm bảng thuật ngữ |
| SEVERITY | P2 |
| UNRESOLVED | CH2-OUTLINE-01 |
| FINAL_DECISION | PARTIAL |

## Gate 2. Bảo toàn khoa học

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đối chiếu manifest với XML nguồn/đích; kiểm OMML riêng; P3 status là quyết định khoa học kế thừa |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 2.171 paragraph; 19 OMML; 0 thay đổi DOCX trong phiên tiếp tục |
| FINDINGS | Năm human decisions và RQ mapping giữ mở; không tái adjudicate toàn văn |
| SEVERITY | P3 |
| UNRESOLVED | Giới hạn nêu trong findings |
| FINAL_DECISION | PASS_WITH_DOCUMENTED_LIMITATIONS |

## Gate 3. Nguồn và claim

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đối chiếu tập khóa record nguồn, exact JSON, XPath/offset và union coverage của ký tự w:t |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 913 record; 2.859 trace row; 5.716 neo; 0 gap ký tự |
| FINDINGS | 637 row neo exact kế thừa; các scope rộng và 5 archive-only được phân biệt |
| SEVERITY | P3 |
| UNRESOLVED | Giới hạn nêu trong findings |
| FINAL_DECISION | PASS_WITH_DOCUMENTED_LIMITATIONS |

## Gate 4. Citation và reference

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đọc Word XML và kiểm first-citation order, identity và lineage |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 783 lượt dẫn; 69→30 reference; 0 missing/orphan/numbering conflict |
| FINDINGS | Crowley đã phân xử trong chapter; school policy chưa xác minh; metadata audit kế thừa |
| SEVERITY | P3 |
| UNRESOLVED | Giới hạn nêu trong findings |
| FINAL_DECISION | PASS_WITH_DOCUMENTED_LIMITATIONS |

## Gate 5. Đối tượng kỹ thuật

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | Đối chiếu media hash; kiểm mới 19 OMML C14N; kiểm số lượng/relationships/caption |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 1 hình; 21 bảng; 19 OMML; 19 caption; 25 lượt nhãn, gồm 8 ngoài caption |
| FINDINGS | Giữ numbering cục bộ, A.1/A.2; 85 row CSV giữ trạng thái trước review, được đối soát bằng hồ sơ 101 trang trong báo cáo này |
| SEVERITY | P3 |
| UNRESOLVED | Giới hạn nêu trong findings |
| FINAL_DECISION | PASS_WITH_DOCUMENTED_LIMITATIONS |

## Gate 6. Word và thị giác

| Trường | Giá trị |
|---|---|
| STATUS | PASS_WITH_DOCUMENTED_LIMITATIONS |
| METHOD | ZIP CRC/XML, relationships và hash DOCX/PDF/PNG; gắn review cũ từng trang |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 16 XML/rels part; 14 relationship; 101/101 review cũ và hash PNG |
| FINDINGS | Không xem lại ảnh trong phiên này; Microsoft Word NOT_VERIFIED; runtime có symlink mất đích |
| SEVERITY | P3 |
| UNRESOLVED | Giới hạn nêu trong findings |
| FINAL_DECISION | PASS_WITH_DOCUMENTED_LIMITATIONS |

## Gate 7. Baseline và package

| Trường | Giá trị |
|---|---|
| STATUS | PASS |
| METHOD | Protected SHA-256; Git HEAD/diff/cached; đủ chín file không rỗng và section/field bắt buộc |
| EVIDENCE | /home/khanh/mp1-work/MP1-CH2-RESUME-20261021/validation/resume_checks.json; QA kế thừa và kiểm mới đính kèm |
| COUNTS | 3.080 protected file; 42 file package; 5 đầu ra cũ bất biến; 9 deliverable sau kiểm |
| FINDINGS | Không commit/push; không cấp independent acceptance |
| SEVERITY | NONE |
| UNRESOLVED | NONE within packaging scope |
| FINAL_DECISION | PASS |

## Crosswalk 65 bullet

Bản review trước ghi 13 partial. Phân xử cuối giữ 3 PARTIAL_EDITORIAL và chuyển 10 sang COVERED_WITH_BOUNDARY, có lý do trong hồ sơ gốc. Không coi các mục có giới hạn là bằng chứng mới.

| ID | Bullet gốc | Trạng thái | Locator nguồn | XPath đích |
|---|---|---|---|---|
| 2.1.1.1 | Giải thích vì sao tổng quan tập trung vào pressure-controlled friction, wire/fiber jamming, TiNi bundle mechanics, contact modeling và validation. | ĐÃ BAO PHỦ | section-1.txt body[3-7] | /w:document/w:body/w:p[4]; /w:document/w:body/w:p[5]; /w:document/w:body/w:p[6]; /w:document/w:body/w:p[7]; /w:document/w:body/w:p[8] |
| 2.1.1.2 | Liên kết từng nhóm tài liệu với RQ1–RQ5 thay vì trình bày lịch sử chung của soft robotics. | ĐÃ BAO PHỦ | section-1.txt body[4-8] | /w:document/w:body/w:p[5]; /w:document/w:body/w:p[6]; /w:document/w:body/w:p[7]; /w:document/w:body/w:p[8]; /w:document/w:body/w:p[9] |
| 2.1.2.1 | Ghi rõ từ khóa, nguồn tìm kiếm, khoảng thời gian thực tế, ngôn ngữ, loại ấn phẩm và cách xử lý bài chỉ có metadata. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-1.txt body[11-17] | /w:document/w:body/w:p[12]; /w:document/w:body/w:p[13]; /w:document/w:body/w:p[14]; /w:document/w:body/w:p[15]; /w:document/w:body/w:p[16]; /w:document/w:body/w:p[17]; /w:document/w:body/w:p[18] |
| 2.1.2.2 | Đưa vào các nghiên cứu có mechanics/model/validation liên quan; loại hoặc để riêng các bài chỉ trình diễn ứng dụng, controller hoặc vật liệu không liên quan. | ĐÃ BAO PHỦ | section-1.txt body[10,14-15] | /w:document/w:body/w:p[11]; /w:document/w:body/w:p[15]; /w:document/w:body/w:p[16] |
| 2.1.2.3 | Nêu các nguồn bị loại và lý do nếu người đọc có thể kỳ vọng chúng xuất hiện. | ĐÃ BAO PHỦ | section-1.txt body[16-17] | /w:document/w:body/w:p[17]; /w:document/w:body/w:p[18] |
| 2.1.3.1 | Mỗi nguồn được ghi theo cơ chế, hình học, vật liệu, pressure/load input, model, observables, validation, limitation và relevance. | ĐÃ BAO PHỦ | section-1.txt body[19-21,26-28] | /w:document/w:body/w:p[20]; /w:document/w:body/w:p[21]; /w:document/w:body/w:p[22]; /w:document/w:body/w:p[27]; /w:document/w:body/w:tbl[1]; /w:document/w:body/w:p[28] |
| 2.1.3.2 | Nhóm chính theo câu hỏi và cơ chế; dùng chronology bên trong nhóm khi cần giải thích sự phát triển. | ĐÃ BAO PHỦ | section-1.txt body[22] | /w:document/w:body/w:p[23] |
| 2.1.3.3 | Cuối mỗi nhóm phải có synthesis paragraph nêu điểm thống nhất, điểm mâu thuẫn và hệ quả cho MP1-R. | MỘT PHẦN, CHỜ BIÊN TẬP | section-1.txt body[23-25] | /w:document/w:body/w:p[24]; /w:document/w:body/w:p[25]; /w:document/w:body/w:p[26] |
| 2.1.4.1 | Phân biệt VERIFIED FULL TEXT, METADATA ONLY và INFERENCE/PROPOSAL trong ghi chú làm việc. | ĐÃ BAO PHỦ | section-1.txt body[30-34] | /w:document/w:body/w:p[30]; /w:document/w:body/w:p[31]; /w:document/w:body/w:p[32]; /w:document/w:body/w:p[33]; /w:document/w:body/w:p[34] |
| 2.1.4.2 | Chọn một chuẩn trích dẫn duy nhất theo quy định của trường; bảo đảm mọi citation có reference tương ứng. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-1.txt body[35-36] | /w:document/w:body/w:p[35]; /w:document/w:body/w:p[36] |
| 2.1.4.3 | Không dùng khoảng trống trong kết quả tìm kiếm để tuyên bố universal novelty. | ĐÃ BAO PHỦ | section-1.txt body[37-38] | /w:document/w:body/w:p[37]; /w:document/w:body/w:p[38] |
| 2.2.1.1 | Định nghĩa vật thể, dầm tương đương, độ cứng vật liệu, độ cứng uốn và độ cứng đầu công tác. | ĐÃ BAO PHỦ | section-2.txt body[3-11] | /w:document/w:body/w:p[41]; /w:document/w:body/w:p[42]; /w:document/w:body/w:p[43]; /w:document/w:body/w:p[44]; /w:document/w:body/w:p[45]; /w:document/w:body/w:p[46]; /w:document/w:body/w:p[47]; /w:document/w:body/w:p[48]; /w:document/w:body/w:p[49] |
| 2.2.1.2 | Giải thích điều kiện khi dùng mô hình dầm và khi chuyển động tương đối giữa các phần tử làm mô hình dầm đơn không còn đủ. | ĐÃ BAO PHỦ | section-2.txt body[12-16] | /w:document/w:body/w:p[50]; /w:document/w:body/w:p[51]; /w:document/w:body/w:p[52]; /w:document/w:body/w:p[53]; /w:document/w:body/w:p[54] |
| 2.2.2.1 | Phân biệt trạng thái jamming ở cấp kết cấu với stick ở cấp tiếp xúc. | ĐÃ BAO PHỦ | section-2.txt body[18-20] | /w:document/w:body/w:p[56]; /w:document/w:body/w:p[57]; /w:document/w:body/w:p[58] |
| 2.2.2.2 | Định nghĩa partial slip và full slip theo chuyển vị tương đối, không gán chúng trực tiếp cho biến dạng dẻo của dây. | ĐÃ BAO PHỦ | section-2.txt body[21-22] | /w:document/w:body/w:p[59]; /w:document/w:body/w:p[60] |
| 2.2.2.3 | Giải thích vai trò của lịch sử tải, tải đảo chiều và vòng trễ. | ĐÃ BAO PHỦ | section-2.txt body[23-25] | /w:document/w:body/w:p[61]; /w:document/w:body/w:p[62]; /w:document/w:body/w:p[63] |
| 2.2.3.1 | Đặt áp suất là input hoặc traction boundary, không đồng nhất ngay với lực pháp tuyến giữa một cặp dây. | ĐÃ BAO PHỦ | section-2.txt body[27-31] | /w:document/w:body/w:p[65]; /w:document/w:body/w:p[66]; /w:document/w:body/w:p[67]; /w:document/w:body/w:p[68]; /w:document/w:body/w:p[69] |
| 2.2.3.2 | Đưa sơ đồ truyền lực từ nguồn áp suất, màng hoặc ống bao, mạng tiếp xúc đến response M–κ. | ĐÃ BAO PHỦ | section-2.txt body[33-36] | /w:document/w:body/w:p[71]; /w:document/w:body/w:p[72]; /w:document/w:body/w:p[73]; /w:document/w:body/w:p[74] |
| 2.2.3.3 | Chỉ ra biến nào đo trực tiếp, biến nào là proxy và biến nào cần calibration. | ĐÃ BAO PHỦ | section-2.txt body[39-43] | /w:document/w:body/w:p[77]; /w:document/w:body/w:p[78]; /w:document/w:body/w:tbl[2]; /w:document/w:body/w:p[79]; /w:document/w:body/w:p[80] |
| 2.3.1.1 | Tóm tắt các nhóm tạo lực đối kháng, vật liệu nhạy nhiệt, khóa ma sát, thay đổi cấu hình và jamming. | ĐÃ BAO PHỦ | section-3.txt body[2-6] | /w:document/w:body/w:p[85]; /w:document/w:body/w:p[86]; /w:document/w:body/w:p[87]; /w:document/w:body/w:p[88]; /w:document/w:body/w:p[89] |
| 2.3.1.2 | Dùng bảng so sánh ngắn, không dành nhiều trang cho cơ chế không liên quan trực tiếp đến bó dây TiNi. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-3.txt body[7-9] | /w:document/w:body/w:p[90]; /w:document/w:body/w:tbl[4]; /w:document/w:body/w:p[91] |
| 2.3.2.1 | Tổng hợp hình học bó sợi, cơ chế tăng lực ma sát, trạng thái dính–trượt và các phép đo uốn. | ĐÃ BAO PHỦ | section-3.txt body[11-15] | /w:document/w:body/w:p[93]; /w:document/w:body/w:p[94]; /w:document/w:body/w:p[95]; /w:document/w:body/w:p[96]; /w:document/w:body/w:p[97] |
| 2.3.2.2 | Đối chiếu những mô hình và kết quả có thể chuyển sang bó TiNi, đồng thời ghi rõ khác biệt vật liệu, packing và biên. | ĐÃ BAO PHỦ | section-3.txt body[15-17] | /w:document/w:body/w:p[97]; /w:document/w:body/w:p[98]; /w:document/w:body/w:p[99] |
| 2.3.3.1 | Giải thích nguyên lý chung của khóa chuyển vị tương đối. | ĐÃ BAO PHỦ | section-3.txt body[20-24] | /w:document/w:body/w:p[101]; /w:document/w:body/w:p[102]; /w:document/w:body/w:p[103]; /w:document/w:body/w:p[104]; /w:document/w:body/w:p[105] |
| 2.3.3.2 | Chỉ ra khác biệt topology tiếp xúc, truyền áp suất và failure mode; không dùng tương đồng tên gọi để chuyển mô hình trực tiếp. | MỘT PHẦN, CHỜ BIÊN TẬP | section-3.txt body[21-26] | /w:document/w:body/w:p[102]; /w:document/w:body/w:p[103]; /w:document/w:body/w:p[104]; /w:document/w:body/w:p[105]; /w:document/w:body/w:p[106]; /w:document/w:body/w:p[107] |
| 2.3.4.1 | Tổng hợp các công trình pressure-dependent, gồm cả prior art gần năm 2025–2026 nếu đã được kiểm tra toàn văn. | ĐÃ BAO PHỦ | section-3.txt body[29-39] | /w:document/w:body/w:p[109]; /w:document/w:body/w:p[110]; /w:document/w:body/w:p[111]; /w:document/w:body/w:p[112]; /w:document/w:body/w:p[113]; /w:document/w:body/w:p[114]; /w:document/w:body/w:p[115]; /w:document/w:body/w:p[116]; /w:document/w:body/w:p[117]; /w:document/w:body/w:p[118]; /w:document/w:body/w:p[119] |
| 2.3.4.2 | Phân biệt pressure source, pressure at specimen, threshold load, stiffness trong từng miền và trạng thái trượt. | ĐÃ BAO PHỦ | section-3.txt body[29-41] | /w:document/w:body/w:p[109]; /w:document/w:body/w:p[110]; /w:document/w:body/w:p[111]; /w:document/w:body/w:p[112]; /w:document/w:body/w:p[113]; /w:document/w:body/w:p[114]; /w:document/w:body/w:p[115]; /w:document/w:body/w:p[116]; /w:document/w:body/w:p[117]; /w:document/w:body/w:p[118]; /w:document/w:body/w:p[119]; /w:document/w:body/w:p[120]; /w:document/w:body/w:p[121] |
| 2.3.4.3 | Kết luận rõ positive pressure, fiber bundle, state-transition model và bending validation đã có tiền lệ ở architecture khác; đây là ranh giới prior art cho MP1-R. | ĐÃ BAO PHỦ | section-3.txt body[39-40] | /w:document/w:body/w:p[119]; /w:document/w:body/w:p[120] |
| 2.3.5.1 | Chốt điều gì đã được xác lập về cơ chế và điều gì còn phụ thuộc hình học, contact topology, membrane/sleeve và cách đo. | ĐÃ BAO PHỦ | section-3.txt body[44-49,51-52] | /w:document/w:body/w:p[123]; /w:document/w:body/w:p[124]; /w:document/w:body/w:p[125]; /w:document/w:body/w:p[126]; /w:document/w:body/w:p[127]; /w:document/w:body/w:p[128]; /w:document/w:body/w:p[130]; /w:document/w:body/w:p[131] |
| 2.3.5.2 | Chuyển sang câu hỏi hẹp hơn về TiNi, pressure transfer và khả năng nhận dạng. | ĐÃ BAO PHỦ | section-3.txt body[50-51] | /w:document/w:body/w:p[129]; /w:document/w:body/w:p[130] |
| 2.4.1.1 | Giải thích vai trò của nhiệt độ, ứng suất, lịch sử tải, rate và chuyển pha đối với mô đun và vòng trễ. | ĐÃ BAO PHỦ | section-4.txt body[3-12,16-17] | /w:document/w:body/w:p[137]; /w:document/w:body/w:p[138]; /w:document/w:body/w:p[139]; /w:document/w:body/w:p[140]; /w:document/w:body/w:p[141]; /w:document/w:body/w:p[142]; /w:document/w:body/w:p[143]; /w:document/w:body/w:p[144]; /w:document/w:body/w:p[145]; /w:document/w:body/w:p[146]; /w:document/w:body/w:p[149]; /w:document/w:body/w:p[150] |
| 2.4.1.2 | Chỉ đưa các phương trình hoặc tham số thật sự dùng trong mô hình của luận văn; định nghĩa mọi ký hiệu ngay sau phương trình. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-4.txt body[10,12,17] | /w:document/w:body/w:p[144]; /w:document/w:body/w:p[146]; /w:document/w:body/w:p[150] |
| 2.4.2.1 | Tổng hợp prior art về wire rope, inter-wire slip, bending hysteresis và mô hình biến dạng riêng hoặc contact. | ĐÃ BAO PHỦ | section-4.txt body[19-33] | /w:document/w:body/w:p[152]; /w:document/w:body/w:p[153]; /w:document/w:body/w:p[154]; /w:document/w:body/w:p[155]; /w:document/w:body/w:p[156]; /w:document/w:body/w:p[157]; /w:document/w:body/w:p[158]; /w:document/w:body/w:p[159]; /w:document/w:body/w:p[160]; /w:document/w:body/w:p[161]; /w:document/w:body/w:p[162]; /w:document/w:body/w:p[163]; /w:document/w:body/w:p[164]; /w:document/w:body/w:p[165]; /w:document/w:body/w:p[166] |
| 2.4.2.2 | Phân biệt bó dây thẳng, cáp xoắn, braid và cấu hình có sleeve; không chuyển kết luận giữa chúng nếu chưa kiểm tra hình học. | ĐÃ BAO PHỦ | section-4.txt body[20-22,36-37] | /w:document/w:body/w:p[153]; /w:document/w:body/w:p[154]; /w:document/w:body/w:p[155]; /w:document/w:body/w:p[168]; /w:document/w:body/w:p[169] |
| 2.4.3.1 | Đặt các cơ cấu SMA-controlled friction vào đúng interface đã công bố, ví dụ wire– sleeve hoặc wire–tube. | ĐÃ BAO PHỦ | section-4.txt body[39-42] | /w:document/w:body/w:p[171]; /w:document/w:body/w:p[172]; /w:document/w:body/w:p[173]; /w:document/w:body/w:p[174] |
| 2.4.3.2 | Đánh giá giới hạn heating/cooling, lực siết, hysteresis và khả năng tách hiệu ứng vật liệu khỏi hiệu ứng tiếp xúc. | ĐÃ BAO PHỦ | section-4.txt body[43-48] | /w:document/w:body/w:p[175]; /w:document/w:body/w:p[176]; /w:document/w:body/w:p[177]; /w:document/w:body/w:p[178]; /w:document/w:body/w:p[179]; /w:document/w:body/w:p[180] |
| 2.4.3.3 | Không coi thay actuator hoặc vật liệu là novelty độc lập. | ĐÃ BAO PHỦ | section-4.txt body[50-53] | /w:document/w:body/w:tbl[12]; /w:document/w:body/w:p[182]; /w:document/w:body/w:p[183]; /w:document/w:body/w:p[184] |
| 2.4.4.1 | Tổng hợp tiền lệ SMA tạo chuyển vị hoặc áp suất qua piston, pump hoặc chamber. | ĐÃ BAO PHỦ | section-4.txt body[56-70] | /w:document/w:body/w:p[187]; /w:document/w:body/w:p[188]; /w:document/w:body/w:p[189]; /w:document/w:body/w:p[190]; /w:document/w:body/w:p[191]; /w:document/w:body/w:p[192]; /w:document/w:body/w:p[193]; /w:document/w:body/w:p[194]; /w:document/w:body/w:p[195]; /w:document/w:body/w:p[196]; /w:document/w:body/w:p[197]; /w:document/w:body/w:p[198]; /w:document/w:body/w:p[199]; /w:document/w:body/w:p[200]; /w:document/w:body/w:p[201] |
| 2.4.4.2 | Phân tích force–stroke–temperature–volume, seal friction, compliance, leakage, pressure transient và cooling. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-4.txt body[74-82] | /w:document/w:body/w:p[204]; /w:document/w:body/w:p[205]; /w:document/w:body/w:p[206]; /w:document/w:body/w:p[207]; /w:document/w:body/w:p[208]; /w:document/w:body/w:p[209]; /w:document/w:body/w:p[210]; /w:document/w:body/w:p[211]; /w:document/w:body/w:p[212] |
| 2.4.4.3 | Kết luận rằng Bench B cần được đặc trưng như một hệ nguồn áp trước khi quy kết response của bó dây. | ĐÃ BAO PHỦ | section-4.txt body[83-87] | /w:document/w:body/w:p[213]; /w:document/w:body/w:p[214]; /w:document/w:body/w:p[215]; /w:document/w:body/w:p[216]; /w:document/w:body/w:p[217] |
| 2.5.1.1 | Nêu điều kiện ma sát tĩnh, ma sát động, lực pháp tuyến và ứng suất tiếp tuyến. | ĐÃ BAO PHỦ | section-5.txt body[5-11,20-28] | /w:document/w:body/w:p[226]; /w:document/w:body/w:p[227]; /w:document/w:body/w:p[228]; /w:document/w:body/w:p[229]; /w:document/w:body/w:p[230]; /w:document/w:body/w:p[231]; /w:document/w:body/w:p[232]; /w:document/w:body/w:p[241]; /w:document/w:body/w:p[242]; /w:document/w:body/w:p[243]; /w:document/w:body/w:p[244]; /w:document/w:body/w:p[245]; /w:document/w:body/w:p[246]; /w:document/w:body/w:p[247]; /w:document/w:body/w:p[248]; /w:document/w:body/w:p[249] |
| 2.5.1.2 | Chỉ rõ các giả định về hệ số ma sát, phân bố contact, biến dạng nhỏ hoặc lớn và lịch sử tải. | ĐÃ BAO PHỦ | section-5.txt body[13-17,33-35] | /w:document/w:body/w:p[234]; /w:document/w:body/w:p[235]; /w:document/w:body/w:p[236]; /w:document/w:body/w:p[237]; /w:document/w:body/w:p[238]; /w:document/w:body/w:p[253]; /w:document/w:body/w:p[254]; /w:document/w:body/w:p[255] |
| 2.5.1.3 | Không đồng nhất full slip với các sợi uốn hoàn toàn độc lập nếu sleeve hoặc ma sát động vẫn tồn tại. | ĐÃ BAO PHỦ | section-5.txt body[17,35,38] | /w:document/w:body/w:p[238]; /w:document/w:body/w:p[255]; /w:document/w:body/w:p[258] |
| 2.5.2.1 | Xây dựng cận các sợi uốn độc lập và cận tiết diện liên kết chống trượt lý tưởng. | ĐÃ BAO PHỦ | section-5.txt body[40-57] | /w:document/w:body/w:p[260]; /w:document/w:body/w:p[261]; /w:document/w:body/w:p[262]; /w:document/w:body/w:p[263]; /w:document/w:body/w:p[264]; /w:document/w:body/w:p[265]; /w:document/w:body/w:p[266]; /w:document/w:body/w:p[267]; /w:document/w:body/w:p[268]; /w:document/w:body/w:p[269]; /w:document/w:body/w:p[270]; /w:document/w:body/w:p[271]; /w:document/w:body/w:p[272]; /w:document/w:body/w:p[273]; /w:document/w:body/w:p[274]; /w:document/w:body/w:p[275]; /w:document/w:body/w:p[276]; /w:document/w:body/w:p[277] |
| 2.5.2.2 | Ghi rõ giả thiết tuyến tính, hình học, trục trung hòa, điều kiện biên và khi nào các cận không còn kẹp được dữ liệu. | ĐÃ BAO PHỦ | section-5.txt body[43-57,63-68] | /w:document/w:body/w:p[263]; /w:document/w:body/w:p[264]; /w:document/w:body/w:p[265]; /w:document/w:body/w:p[266]; /w:document/w:body/w:p[267]; /w:document/w:body/w:p[268]; /w:document/w:body/w:p[269]; /w:document/w:body/w:p[270]; /w:document/w:body/w:p[271]; /w:document/w:body/w:p[272]; /w:document/w:body/w:p[273]; /w:document/w:body/w:p[274]; /w:document/w:body/w:p[275]; /w:document/w:body/w:p[276]; /w:document/w:body/w:p[277]; /w:document/w:body/w:p[283]; /w:document/w:body/w:p[284]; /w:document/w:body/w:p[285]; /w:document/w:body/w:p[286]; /w:document/w:body/w:p[287]; /w:document/w:body/w:tbl[16] |
| 2.5.2.3 | Dùng các cận như baseline, không gọi chúng là mô hình hoàn chỉnh của mẫu thật. | ĐÃ BAO PHỦ | section-5.txt body[69-71] | /w:document/w:body/w:p[288]; /w:document/w:body/w:p[289]; /w:document/w:body/w:p[290] |
| 2.5.3.1 | Định nghĩa độ cứng tiếp tuyến, cát tuyến, ngưỡng trượt, biến dạng còn lại và diện tích vòng trễ. | ĐÃ BAO PHỦ | section-5.txt body[75-98] | /w:document/w:body/w:p[294]; /w:document/w:body/w:p[295]; /w:document/w:body/w:p[296]; /w:document/w:body/w:p[297]; /w:document/w:body/w:p[298]; /w:document/w:body/w:p[299]; /w:document/w:body/w:p[300]; /w:document/w:body/w:p[301]; /w:document/w:body/w:p[302]; /w:document/w:body/w:p[303]; /w:document/w:body/w:p[304]; /w:document/w:body/w:p[305]; /w:document/w:body/w:p[306]; /w:document/w:body/w:p[307]; /w:document/w:body/w:p[308]; /w:document/w:body/w:p[309]; /w:document/w:body/w:p[310]; /w:document/w:body/w:p[311]; /w:document/w:body/w:p[312]; /w:document/w:body/w:p[313]; /w:document/w:body/w:p[314]; /w:document/w:body/w:p[315]; /w:document/w:body/w:p[316]; /w:document/w:body/w:p[317] |
| 2.5.3.2 | Liên hệ từng metric với đường tải, tải dỡ, tốc độ, dwell và chiều dài mẫu. | MỘT PHẦN, CHỜ BIÊN TẬP | section-5.txt body[85-90,100-108] | /w:document/w:body/w:p[304]; /w:document/w:body/w:p[305]; /w:document/w:body/w:p[306]; /w:document/w:body/w:p[307]; /w:document/w:body/w:p[308]; /w:document/w:body/w:p[309]; /w:document/w:body/w:p[319]; /w:document/w:body/w:p[320]; /w:document/w:body/w:p[321]; /w:document/w:body/w:p[322]; /w:document/w:body/w:p[323]; /w:document/w:body/w:tbl[17]; /w:document/w:body/w:p[324]; /w:document/w:body/w:p[325]; /w:document/w:body/w:p[326] |
| 2.5.3.3 | Phân biệt công tiêu tán đo ở mức kết cấu với cơ chế tiêu tán tại một interface. | ĐÃ BAO PHỦ | section-5.txt body[92-98,108] | /w:document/w:body/w:p[311]; /w:document/w:body/w:p[312]; /w:document/w:body/w:p[313]; /w:document/w:body/w:p[314]; /w:document/w:body/w:p[315]; /w:document/w:body/w:p[316]; /w:document/w:body/w:p[317]; /w:document/w:body/w:p[326] |
| 2.5.4.1 | Phân tích parameter compensation giữa mô đun TiNi, hệ số ma sát, lực pháp tuyến, sleeve compliance và điều kiện gá. | ĐÃ BAO PHỦ | section-5.txt body[111,114-117] | /w:document/w:body/w:p[329]; /w:document/w:body/w:p[332]; /w:document/w:body/w:p[333]; /w:document/w:body/w:p[334]; /w:document/w:body/w:p[335] |
| 2.5.4.2 | Chỉ ra các phép đo bổ sung hoặc mẫu đối chứng cần thiết để tách wire–wire khỏi wire–sleeve. | ĐÃ BAO PHỦ | section-5.txt body[123-125,131-134] | /w:document/w:body/w:p[340]; /w:document/w:body/w:p[341]; /w:document/w:body/w:p[342]; /w:document/w:body/w:p[348]; /w:document/w:body/w:p[349]; /w:document/w:body/w:p[350]; /w:document/w:body/w:p[351] |
| 2.5.4.3 | Đưa uncertainty, repeatability và detection threshold vào tiêu chí đánh giá model. | ĐÃ BAO PHỦ | section-5.txt body[126-130,132-136] | /w:document/w:body/w:p[343]; /w:document/w:body/w:p[344]; /w:document/w:body/w:p[345]; /w:document/w:body/w:p[346]; /w:document/w:body/w:p[347]; /w:document/w:body/w:p[349]; /w:document/w:body/w:p[350]; /w:document/w:body/w:p[351]; /w:document/w:body/w:p[352]; /w:document/w:body/w:p[353] |
| 2.5.5.1 | So sánh analytical beam, homogenized/reduced-order, FE/contact và thực nghiệm theo khả năng mô tả, chi phí, tham số cần đo và nguy cơ overfitting. | ĐÃ BAO PHỦ | section-5.txt body[138-151] | /w:document/w:body/w:p[355]; /w:document/w:body/w:p[356]; /w:document/w:body/w:p[357]; /w:document/w:body/w:p[358]; /w:document/w:body/w:p[359]; /w:document/w:body/w:p[360]; /w:document/w:body/w:p[361]; /w:document/w:body/w:p[362]; /w:document/w:body/w:p[363]; /w:document/w:body/w:p[364]; /w:document/w:body/w:p[365]; /w:document/w:body/w:tbl[19]; /w:document/w:body/w:p[366]; /w:document/w:body/w:p[367] |
| 2.5.5.2 | Nêu phương pháp nào dùng để dự đoán, phương pháp nào chỉ dùng làm cận hoặc diễn giải. | ĐÃ BAO PHỦ | section-5.txt body[140-151,153-154] | /w:document/w:body/w:p[357]; /w:document/w:body/w:p[358]; /w:document/w:body/w:p[359]; /w:document/w:body/w:p[360]; /w:document/w:body/w:p[361]; /w:document/w:body/w:p[362]; /w:document/w:body/w:p[363]; /w:document/w:body/w:p[364]; /w:document/w:body/w:p[365]; /w:document/w:body/w:tbl[19]; /w:document/w:body/w:p[366]; /w:document/w:body/w:p[367]; /w:document/w:body/w:p[369]; /w:document/w:body/w:p[370] |
| 2.5.5.3 | Đặt H0b làm baseline phải được kiểm tra trước khi đề xuất H1. | ĐÃ BAO PHỦ | section-5.txt body[152-154] | /w:document/w:body/w:p[368]; /w:document/w:body/w:p[369]; /w:document/w:body/w:p[370] |
| 2.6.1.1 | Jamming, positive pressure, frictional locking, TiNi transformation, inter-wire slip và SMA-to-pressure actuation đều có prior art ở các architecture khác nhau. | ĐÃ BAO PHỦ | section-6.txt body[3-14,17] | /w:document/w:body/w:p[376]; /w:document/w:body/w:p[377]; /w:document/w:body/w:p[378]; /w:document/w:body/w:p[379]; /w:document/w:body/w:p[380]; /w:document/w:body/w:p[381]; /w:document/w:body/w:p[382]; /w:document/w:body/w:p[383]; /w:document/w:body/w:p[384]; /w:document/w:body/w:p[385]; /w:document/w:body/w:p[386]; /w:document/w:body/w:p[387]; /w:document/w:body/w:p[390] |
| 2.6.1.2 | Một số mô hình homogenized, stick–slip hoặc contact-aware đã được validation trong phạm vi riêng của chúng. | ĐÃ BAO PHỦ | section-6.txt body[9-12,17] | /w:document/w:body/w:p[382]; /w:document/w:body/w:p[383]; /w:document/w:body/w:p[384]; /w:document/w:body/w:p[385]; /w:document/w:body/w:p[390] |
| 2.6.2.1 | Interface chi phối chưa được khóa; áp suất tại nguồn chưa được chứng minh là normal traction hữu hiệu. | ĐÃ BAO PHỦ | section-6.txt body[19-21,31-34] | /w:document/w:body/w:p[392]; /w:document/w:body/w:p[393]; /w:document/w:body/w:p[394]; /w:document/w:body/w:p[404]; /w:document/w:body/w:p[405]; /w:document/w:body/w:p[406]; /w:document/w:body/w:p[407] |
| 2.6.2.2 | Chưa biết H0b có dự đoán được response pressure-dependent khi transformation, contact và sleeve cùng hoạt động trong miền thí nghiệm hay không. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-6.txt body[32-34] | /w:document/w:body/w:p[405]; /w:document/w:body/w:p[406]; /w:document/w:body/w:p[407] |
| 2.6.2.3 | Chưa có cơ sở để khẳng định cơ chế mới hoặc universal novelty. | ĐÃ BAO PHỦ | section-6.txt body[34] | /w:document/w:body/w:p[407] |
| 2.6.3.1 | Khoảng trống làm việc là xây dựng và kiểm tra bản đồ interface-specific giữa áp suất gần mẫu, trạng thái tiếp xúc, đáp ứng M–κ và sai lệch mô hình trong miền bất định đã khai báo. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-6.txt body[36-45,47-48] | /w:document/w:body/w:p[409]; /w:document/w:body/w:p[410]; /w:document/w:body/w:p[411]; /w:document/w:body/w:p[412]; /w:document/w:body/w:p[413]; /w:document/w:body/w:p[414]; /w:document/w:body/w:p[415]; /w:document/w:body/w:p[416]; /w:document/w:body/w:p[417]; /w:document/w:body/w:p[418]; /w:document/w:body/w:p[420]; /w:document/w:body/w:p[421] |
| 2.6.3.2 | Đóng góp được chấp nhận nếu nghiên cứu phân biệt được cơ chế hoặc chỉ ra giới hạn của mô hình hiện hữu; kết quả không có hiệu ứng vượt bất định cũng được báo cáo như một kết luận thu hẹp. | ĐÃ BAO PHỦ | section-6.txt body[43-48] | /w:document/w:body/w:p[416]; /w:document/w:body/w:p[417]; /w:document/w:body/w:p[418]; /w:document/w:body/w:p[419]; /w:document/w:body/w:p[420]; /w:document/w:body/w:p[421] |
| 2.6.4.1 | Bench A phải xác định pressure-only response, repeatability, pressure-transfer proxy và các metric M–κ. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-6.txt body[50-55] | /w:document/w:body/w:p[423]; /w:document/w:body/w:p[424]; /w:document/w:body/w:p[425]; /w:document/w:body/w:p[426]; /w:document/w:body/w:p[427]; /w:document/w:body/w:p[428] |
| 2.6.4.2 | Bench B phải xác định response của SMA–piston độc lập và so sánh với Bench A ở cùng áp suất gần mẫu. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-6.txt body[56-59] | /w:document/w:body/w:p[429]; /w:document/w:body/w:p[430]; /w:document/w:body/w:p[431]; /w:document/w:body/w:p[432] |
| 2.6.4.3 | Chỉ chuyển sang phần tích hợp khi geometry, interface, sensor placement, uncertainty và stop criteria đã được khóa. | ĐÃ BAO PHỦ VỚI GIỚI HẠN | section-6.txt body[60-63] | /w:document/w:body/w:p[433]; /w:document/w:body/w:p[434]; /w:document/w:body/w:p[435]; /w:document/w:body/w:p[436] |

## Heading chính thức

| ID | Tên |
|---|---|
| 2.1 | Phạm vi và phương pháp tổng quan |
| 2.1.1 | Mục đích của chương tổng quan |
| 2.1.2 | Tiêu chí tìm kiếm, đưa vào và loại ra |
| 2.1.3 | Ma trận trích xuất và nguyên tắc nhóm |
| 2.1.4 | Trạng thái bằng chứng và quy ước trích dẫn |
| 2.2 | Thuật ngữ và khung cơ học |
| 2.2.1 | Robot continuum và các đại lượng độ cứng |
| 2.2.2 | Jamming, frictional locking và slip |
| 2.2.3 | Áp suất cấp và lực pháp tuyến |
| 2.3 | Các cơ chế variable stiffness và prior art jamming |
| 2.3.1 | Phân loại cơ chế |
| 2.3.2 | Wire/fiber jamming |
| 2.3.3 | Layer/laminar và granular jamming như nhóm so sánh |
| 2.3.4 | Positive-pressure jamming và các miền trạng thái |
| 2.3.5 | Synthesis của nhóm jamming |
| 2.4 | TiNi, ma sát bó dây và nguồn tạo áp |
| 2.4.1 | Chuyển pha và siêu đàn hồi của TiNi |
| 2.4.2 | Bó dây, cáp và chuyển vị tương đối |
| 2.4.3 | SMA điều biến ma sát |
| 2.4.4 | SMA–piston và truyền áp suất |
| 2.5 | Mô hình cơ học, phép đo và khả năng nhận dạng |
| 2.5.1 | Coulomb và chuyển tiếp stick–partial slip–full slip |
| 2.5.2 | Hai cận độ cứng tham chiếu |
| 2.5.3 | M–κ, stiffness và vòng trễ |
| 2.5.4 | Nhận dạng và bất định |
| 2.5.5 | So sánh các nhóm phương pháp |
| 2.6 | Tổng hợp khoảng trống và handoff sang thí nghiệm |
| 2.6.1 | Điều đã có cơ sở |
| 2.6.2 | Điều còn bất định đối với cấu hình nghiên cứu |
| 2.6.3 | Khoảng trống có thể kiểm chứng |
| 2.6.4 | Câu hỏi và tiêu chí chuyển sang Chương 3–4 |

## Audit mạch lập luận

Các nhận định được kế thừa từ self-review, không phải nghiệm thu độc lập.

```json
[
  {
    "pair": "2.1→2.2",
    "classification": "COHERENT_WITH_LOCAL_REPETITION",
    "evidence": "2.1 body[8,21,25,38] announces terms, pressure levels and uncertainty; 2.2 body[3-16,27-44] defines them. 2.1 and 2.2 repeat the three pressure levels but the second supplies the mechanics."
  },
  {
    "pair": "2.2→2.3",
    "classification": "COHERENT_WITH_HEADING_GAP",
    "evidence": "2.2 body[25,44] calls for distinguishing pressure from contact and architecture; 2.3 body[2-6,11-16] classifies and tests transfer. 2.3 lacks the parent title."
  },
  {
    "pair": "2.3→2.4",
    "classification": "COHERENT",
    "evidence": "2.3 body[50-51] narrows to TiNi, packing, membrane and pressure transfer; 2.4 body[3,16-19,36-37] opens with TiNi state and cable geometry."
  },
  {
    "pair": "2.4→2.5",
    "classification": "COHERENT_WITH_REPETITION",
    "evidence": "2.4 body[84-87] requires source/specimen/contact separation; 2.5 body[3-10,33-38] repeats it to formulate Coulomb assumptions. Repetition is functional but could be shortened."
  },
  {
    "pair": "2.5→2.6",
    "classification": "COHERENT_WITH_UNRESOLVED_PROTOCOL",
    "evidence": "2.5 body[152-155] leaves H0b live and human decisions open; 2.6 body[17,32-34,43-48,50-63] synthesizes bounded gaps and Bench A/B gates. It cannot close protocol choices."
  }
]
```
## P3 status

```json
{
  "H0a": "REFUTED_IN_TRANSFORMATION_REGIME",
  "H0b": "NOT_FALSIFIED_LIVE_COMPETITOR",
  "H1": "INSUFFICIENT_EVIDENCE",
  "G00": "CLOSED_AS_GENERAL_MECHANISM",
  "G01–G08": "CONDITIONAL; original P3 decisions retained",
  "G09": "PROJECT_PREREQUISITE",
  "G10": "NOT_ESTABLISHED",
  "G11": "NO_UNIVERSAL_NOVELTY_CLAIM",
  "RQ_MAPPING_STATUS": "PROVISIONAL_MANY_TO_MANY",
  "HUMAN_DECISIONS_PENDING": 5
}
```
## Kiểm mới và giới hạn coverage

Coverage ký tự w:t xác nhận bản thảo có mapping, không xác nhận từng câu đúng về khoa học. Overlap giữa support/structural row được đếm riêng. Không gộp overlap thành claim độc lập.

```json
{
  "status": "PASS",
  "pdf_page_selfchecks": "PASS",
  "original_record_set_equal": true,
  "original_record_json_equal": true,
  "input_records": 913,
  "trace_rows": 2859,
  "source_and_final_anchor_checks": 5716,
  "terminology_original_json_equal": true,
  "terminology_records": 313,
  "source_paragraph_manifest_complete": true,
  "preservation_paragraphs": 2171,
  "final_text_coverage_gaps": [],
  "covered_text_characters": 284215,
  "overlapping_text_characters": 153359,
  "overlap_boundary": "Repeated support and structural records are expected; no duplicate chapter_claim_id allowed.",
  "archive_only_records": [
    "CH2-S4-R0013-A01",
    "CH2-S4-R0092-A01",
    "CH2-S4-R0093-A01",
    "CH2-S4-R0094-A01",
    "CH2-S4-R0095-A01"
  ],
  "record_kind_counts": {
    "SCIENTIFIC_CLAIM": 931,
    "STRUCTURAL_RECORD": 1923,
    "ARCHIVAL_SUPPORT_ONLY": 5
  },
  "anchor_granularity_counts": {
    "SOURCE_EXACT_ANCHOR": 637,
    "PARAGRAPH_OR_TABLE_SCOPE": 75,
    "TABLE_ROW_SCOPE": 48,
    "PARAGRAPH_SCOPE": 136,
    "ARCHIVAL_SUPPORT_ONLY": 5,
    "SUBSECTION_SCOPE": 9,
    "PARAGRAPH_OR_EQUATION_SCOPE": 95,
    "WHOLE_PARAGRAPH": 1852,
    "NEW_STRUCTURE": 2
  },
  "immutable_outputs_verified": 5,
  "qa_exactly_matches_checkpoint": true,
  "visual_reviews_inherited": 101,
  "visual_images_hash_checked": 101,
  "images_viewed_in_resume": 0,
  "new_render_performed": false,
  "microsoft_word_validation": "NOT_VERIFIED",
  "omml_exact_c14n_source_final_checks": 19,
  "inherited_crosswalk_visual_statuses": {
    "PENDING_FINAL_RENDER_REVIEW": 85
  },
  "crosswalk_status_boundary": "The immutable CSV predates final visual review. The 7-gate report links the later inherited review evidence without rewriting CSV status."
}
```
## Review thị giác kế thừa từng trang

Không gán lại tác giả hoặc thời điểm review. Đường dẫn /tmp trong bản ghi là provenance gốc; ảnh thực được phục hồi ở scratch hiện tại.

```json
{
  "final_docx_sha256": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
  "final_pdf_sha256": "fd9ff79381519958ba917c52cb64cac17b2941b4a5e34378e5f9101d521da44a",
  "reviewed_pdf_sha256": "6a9d7d87430cfb7ac425637b30570828bc01ae5a4b47097414579d7abe480b94",
  "pages": 101,
  "all_final_render_rasters_byte_identical_to_reviewed_images": true,
  "raster_hashes": [
    "e2e587468893d9e80d4dfad06010147cce60cba356df8b8de865f8b8fc721311",
    "2a5b54b7c1987c41136dbf9d0f31e123e531820acf5fe9f86889ee5bd58a5fba",
    "b286ee3177bc523973fb0de928908ccebfc23fe78f4671d3a9c18888519806bc",
    "e09a53653aabdda265af29a087fc45c0442953ac90947db59296ba4c57bd108b",
    "07e8e9cbd3aa7231a5ca20166cb58771381c3bc35f6520789abaecfa5a706092",
    "3796fbf9773d4f0981c5123dde6200556e34fcc78f27e59dca2de320872a3042",
    "a366fac831dfec52a5bb37d0779ace1914285a329b16906c38a85aa103b3d702",
    "7df7885730372890036b63263db0b7900b76810077d35317432d6764426f11b0",
    "3b32e6ef92e8907e0cfdcb8d7fc05ff6c95282b4bd43e53457af1027cddbe0ef",
    "2419dbdf47bc85fe5ff03533c65c83c9264ec1c877934d927ca3d08c8a8ef945",
    "278a14b2834e607f769bf90d6c934ae14069796535da478a377e0caaa1975048",
    "8934de723a91d558d7f760f570261038e95cc99737db44e1459e8cdfd5763adf",
    "8a828e5c4ee3a2359393aa9d442771232a30ed6eb19402efad5d014222051906",
    "680a06533cb00f6ae3fa69847a85b8d1d8b7518ada9cefd5364c29cb62e270da",
    "951fae32b689b3b22a4b8a0b9d5a5e8df875b5305046eb9dfad7641264ad9790",
    "88443283210e07fc712dd4069dd6de33f5d2ab9bb978ff5b3fd01b326ad366d1",
    "8268ab333533fc67621f4a99aa22d27331319f3d01149dd08da58df3b5715915",
    "0957a80c7085df5ceeb6fef0fc951c7ffc6eba77e0d52ba12d695734163c03be",
    "ed6938d326c59875ffda5851f45e3c613d2224e8f178e6ac2d792c27bc59fd41",
    "f77a57653fba30287940ee8557e8c3fc5a286fc95efcee2a78848cdd8d33bf1e",
    "69442080a648efd9ba62924a99e566864d2b0783768e9f05b52cd97ccb48adf5",
    "d74a44fb7514cc5d03af14cf41238822af1d075f6671bac98e90979bf02b2744",
    "e282c22524b7d33471943ac418e986646f62fd9ba3968cf7c6af6c592db6ac9f",
    "da7bfd21579028c53a5d74e64231fe850807e83e7ba4388c35e9895030e6e1df",
    "8e9e66c2dfdb23299770ef857cc19d87d0561c31727bb2bc880d830c59a72973",
    "bb7a9b3b757a393982de26803b76c435cf6bb8b2953f69b96a5c2e7123ddb204",
    "142b00f11aa00de43bf8ac1a6d15c203002219fd919f2cf54c5a489505c06105",
    "2797791a0808a6740901de1483633dbed5be99305bb540d1e2f96a3aaaa40669",
    "e5a87bed1e00846f1e900631235a56f77badd13f49c9883c5597fdae8329cab7",
    "ae342d60edf6abd070ab3235561d52b289476fbf082a185660bbec8489b3688a",
    "73835a477cc3b06157af207db9104745ce1cd770ff80af6133867c60844bcb4b",
    "1277d3f1091a6523f31dd0515ee09963ce8355519bc4a563854a6ecf17bb34b8",
    "af2e15e40ef86e810da4f3c8851578513d2a61cf7299a6642df01514414358f6",
    "bb9a51b2c60ac081249852c2a14225ddef9aeb8c0e78291d4ac994f2cce22aca",
    "2b9da0dfc21d23bc209968db311bab1f28b025d58b5c23226cd0693cdb036765",
    "a22e5968b114cdd282abec07139156c901fc89e68a23c02f5317ec24eafb0cb5",
    "363d6e27687db8052fabddece713409756df2a9ba418c762c119ae30f653763d",
    "911b05080f370afdb7e2736d2e7bed190cdcba7e913c5f41d5d94b0b643269b5",
    "57e8f7a93c794bb7fc53cd45125602defc81fff6f92ecb9bb5029cbc2bc3fed7",
    "1b6d3668ec4478ad2290583b2f055a5e3639263ed10dc9f4c302bb64e3b7174c",
    "e8f9826d2a4be7f74eb0fc5cd95629ab720111128e5c0a8b658865e97f20233a",
    "d768bd56544d4a0923600dc587dd2abd1a0375ce5a414d752f805ba939370f7e",
    "9e171f7123e10cb729060d1f60259edcb46518f45b95eb40bd9ee73c60b610bc",
    "8869fa972734bcd25d16020909fac5d1653f2e18e6bf21d024cfd14dafc2880d",
    "c245b6b6bc85ba4a49b15de937148ad298c6ef4982a5806344ac7650b4dab695",
    "00a560dcd9dd15276379ad6ffbce1ff5cae61932fe382ec45cc0e7c6aea753ca",
    "3885958bea92af70729d92f7e2585e91032f438db18c9d3b6f3fa2d5db351130",
    "5cf1770ae8588a9a3419f95be8ead02d8593760d72f7c9d4af8fbaa20b19df8b",
    "be2144557d98218a33157d1a6c0804c141c4d2aff1da74aad8006a06d20c4344",
    "1673ab0fdc108bfa80fc9797af51ddf3a34dd6a69a8e1f8fc07b28237cb417ff",
    "17835f75e61b5b3817744aa4f7a38b3b9e21bbc279bdc859198ed7991722a463",
    "3b3a0c01f88de1f1e2bf1d8146d177ca89d22e9b3e7487782bc2924f2abc25e2",
    "edc5117de9f4bc0818775b50cbedfb7717a68d75b0b3dab0613054de026f17ea",
    "950cb8039bcaea0546cd0843c4fdcd5645f1e746d4fadcb6f1751cf34e12d7c3",
    "865aed54a9c689ed5391e92fdce759c9e7d0d9affb54e982363541915c97d1bc",
    "70fef5775b6f9409ee2b312277452949ffbd6d5c3c0b91c097d19cb317bcb363",
    "d77b2749aa743461b5e511d98937d20945f4cca497f337f4ea37a4fb43b78aaf",
    "11338aee36ab7e459ea080a656bbfc1dec2bb3558436848c350cfa8acfb7f4e3",
    "98bf8bd3e427913a0f21cc820a12af4b98e28842e2154f646da1c1efe38e3d2d",
    "2711137c24f15593938840bda909cace045edd701ce26364a6bc90f7db0dc72f",
    "f2ddd9d0522fab96b06aeeebb2c67ed9261dd6d94362070f12ae0409984fd1bf",
    "02e8cdd5f9d90f2f99e89e80638ca6c8603013b774850e339f262e8f2043b706",
    "fa9e052667e0631f8dd87904a7fe53ebb1346bcfe9da71e883156186a6cf3a9a",
    "88dc53be121f4096b65b99d8db466879fbae6e32000f44055f378c84395b8031",
    "d44a9068e1c106325deb550d644266cd8aa58e4bb1730cdff6c150168963d41a",
    "c3604efd727baceb93d3e718479ec097f2b96d099a30f7af84a2434bcefc336b",
    "aeb3e748ce2f95dd3a8918db7d631c146d053ed93f95d6141b933e3aa465a9a9",
    "e10022e5aa07df7a05b9e426de3d660dc343d88e2c72612d68dc6ecbb592f7a5",
    "5e80addea29ba5f14ce6ce2f5f54b8d54a7de2ea812e79138dc8b941f37193b8",
    "d5ec8c350618c0045074c9f54873c3e6d5d13a64dfe29477cf1ad9ffd647069c",
    "ad475562aff27edbdeff0442edff57b0c706bd3e3c7b1d6c7d8da4c35d72b975",
    "33a3f9644d3ded20d075b644248f25854e459c3ff3fee11b2857cc6204cedfa6",
    "823600295ad4130b45410382edea01bdd2f44c7148f5efd8dca4351affbdb29a",
    "56ca55b5bbf18f2b606f08c30f7a50f78bbede7abf235ad02c41277a6ce67e73",
    "7ada8a50dd6643b0eafcb100154aa9af8b926a876d3b0ca4478056f492e552ff",
    "b1b5d10ec0a4cc1ad0516f0d7ec837773615a40b5c4521ce3eff9e0b1143abde",
    "df9f3e258e4fcda90526eb44478c5cca58f1b8fdbc92517acfa5723bb297a34c",
    "d275c4071727c11a1b7285ff499f733a09c2781227af8c0d8a438228f79caf9c",
    "954aee24f348c7f06047769405f3bca28d0ba9af0d8b6255803f636569c96a82",
    "01e354cec372abe450e475aa7ad9af2240317fd2a46a72b898f2897774022187",
    "ca403512f332ffde98e33428a4c717d90fe6023622ca575bbd46a372c2214e0d",
    "7d842982bb266ab34739975f8b6c17c55754c4d78f80b808ced742636219bc6c",
    "df52b474fb740f40a61520779d392271851f3109ad44347e1007f3e8bf843ac2",
    "c88ab78dd3d7e480b9abeb03d394bae52263b53fb8c2ed44a24ecc59cfd51fb3",
    "ef8fd695f48560e55a60b3ccf934310545692efda9c52b9e9351ae96cc46ba42",
    "d8f5492739cbdedb94969c0aa9dace3f46f1d2e4ea3065f1feb1e235eceec9b4",
    "5d69c27edb65fb1c885243f7d1805b1b006b25043c72fbb11d5200d1e4bdf759",
    "5c6bf7cab4ea70bd4631f9c3c6d4f19a18cc7eea86c9eac037eeacbb14de573c",
    "a78387764ecff3775eddd0d7d727cf6d0b877630f93afa154d155a83e5f19342",
    "6bdab8488b2392de5e16f8b0d55c6c99e2ec9bf2c6f4374315b88c446df08968",
    "39feaca18ba54860cadddd249d1b04353b492ded75189cf99447b43968e4dfce",
    "7b20509b597a5e9a47084ee0e3ec61e16c7f6dd841f8a756e6ed330586cc6e4a",
    "4a53411c6610cc6b42b40defc04c88efd74a00cef7e9cf17f1145494acba05d0",
    "2e5a850b89cd31f30249dbe42a8e0383997ca4680edf905bd251776f7c5627d4",
    "78fa4113d42afa11796d14c4183d846beb7e92cecff0c4b35a7b3c346c8fe26c",
    "ed615170ed044b4847ded1ca705e7fa1cd6861da9aa6a1fd33a37201cc87a68e",
    "80e6ffd31e2334c56d872e42eb7e4138e041fe2201a7a8e9db299d3e01de8f0b",
    "8e5ecb6af7ddbfcd2c16e142a13979fd6963645d30129a831651f4ddfc9de822",
    "7eb82af50762e24c12b81ebdd1c802767bdc1e288a9f750478ae7f825f75822b",
    "759612a03ecc75f8877c181bcfaedf9be3149472db86cf4f9f389183f59720b0",
    "7443949d28e84a452ee5e61103732e3b22f6c6b253104e900cf7f6d8375b1dad"
  ],
  "reason": "Chỉ chuẩn hóa outlineLvl=3 cho 33 nhãn hỗ trợ; không thay đổi pixel, text, phương trình hoặc dàn trang."
}
```
| Trang | Trạng thái review cũ | File review | SHA-256 ảnh |
|---|---|---|---|
| 1 | PASS | final_visual_001_030.json | e2e587468893d9e80d4dfad06010147cce60cba356df8b8de865f8b8fc721311 |
| 2 | PASS | final_visual_001_030.json | 2a5b54b7c1987c41136dbf9d0f31e123e531820acf5fe9f86889ee5bd58a5fba |
| 3 | PASS | final_visual_001_030.json | b286ee3177bc523973fb0de928908ccebfc23fe78f4671d3a9c18888519806bc |
| 4 | NOTE | final_visual_001_030.json | e09a53653aabdda265af29a087fc45c0442953ac90947db59296ba4c57bd108b |
| 5 | PASS | final_visual_001_030.json | 07e8e9cbd3aa7231a5ca20166cb58771381c3bc35f6520789abaecfa5a706092 |
| 6 | PASS | final_visual_001_030.json | 3796fbf9773d4f0981c5123dde6200556e34fcc78f27e59dca2de320872a3042 |
| 7 | PASS | final_visual_001_030.json | a366fac831dfec52a5bb37d0779ace1914285a329b16906c38a85aa103b3d702 |
| 8 | PASS | final_visual_001_030.json | 7df7885730372890036b63263db0b7900b76810077d35317432d6764426f11b0 |
| 9 | PASS | final_visual_001_030.json | 3b32e6ef92e8907e0cfdcb8d7fc05ff6c95282b4bd43e53457af1027cddbe0ef |
| 10 | PASS | final_visual_001_030.json | 2419dbdf47bc85fe5ff03533c65c83c9264ec1c877934d927ca3d08c8a8ef945 |
| 11 | NOTE | final_visual_001_030.json | 278a14b2834e607f769bf90d6c934ae14069796535da478a377e0caaa1975048 |
| 12 | PASS | final_visual_001_030.json | 8934de723a91d558d7f760f570261038e95cc99737db44e1459e8cdfd5763adf |
| 13 | PASS | final_visual_001_030.json | 8a828e5c4ee3a2359393aa9d442771232a30ed6eb19402efad5d014222051906 |
| 14 | PASS | final_visual_001_030.json | 680a06533cb00f6ae3fa69847a85b8d1d8b7518ada9cefd5364c29cb62e270da |
| 15 | PASS | final_visual_001_030.json | 951fae32b689b3b22a4b8a0b9d5a5e8df875b5305046eb9dfad7641264ad9790 |
| 16 | PASS | final_visual_001_030.json | 88443283210e07fc712dd4069dd6de33f5d2ab9bb978ff5b3fd01b326ad366d1 |
| 17 | PASS | final_visual_001_030.json | 8268ab333533fc67621f4a99aa22d27331319f3d01149dd08da58df3b5715915 |
| 18 | PASS | final_visual_001_030.json | 0957a80c7085df5ceeb6fef0fc951c7ffc6eba77e0d52ba12d695734163c03be |
| 19 | NOTE | final_visual_001_030.json | ed6938d326c59875ffda5851f45e3c613d2224e8f178e6ac2d792c27bc59fd41 |
| 20 | NOTE | final_visual_001_030.json | f77a57653fba30287940ee8557e8c3fc5a286fc95efcee2a78848cdd8d33bf1e |
| 21 | PASS | final_visual_001_030.json | 69442080a648efd9ba62924a99e566864d2b0783768e9f05b52cd97ccb48adf5 |
| 22 | NOTE | final_visual_001_030.json | d74a44fb7514cc5d03af14cf41238822af1d075f6671bac98e90979bf02b2744 |
| 23 | NOTE | final_visual_001_030.json | e282c22524b7d33471943ac418e986646f62fd9ba3968cf7c6af6c592db6ac9f |
| 24 | PASS | final_visual_001_030.json | da7bfd21579028c53a5d74e64231fe850807e83e7ba4388c35e9895030e6e1df |
| 25 | PASS | final_visual_001_030.json | 8e9e66c2dfdb23299770ef857cc19d87d0561c31727bb2bc880d830c59a72973 |
| 26 | PASS | final_visual_001_030.json | bb7a9b3b757a393982de26803b76c435cf6bb8b2953f69b96a5c2e7123ddb204 |
| 27 | PASS | final_visual_001_030.json | 142b00f11aa00de43bf8ac1a6d15c203002219fd919f2cf54c5a489505c06105 |
| 28 | PASS | final_visual_001_030.json | 2797791a0808a6740901de1483633dbed5be99305bb540d1e2f96a3aaaa40669 |
| 29 | NOTE | final_visual_001_030.json | e5a87bed1e00846f1e900631235a56f77badd13f49c9883c5597fdae8329cab7 |
| 30 | NOTE | final_visual_001_030.json | ae342d60edf6abd070ab3235561d52b289476fbf082a185660bbec8489b3688a |
| 31 | PASS | final_visual_031_060.json | 73835a477cc3b06157af207db9104745ce1cd770ff80af6133867c60844bcb4b |
| 32 | PASS | final_visual_031_060.json | 1277d3f1091a6523f31dd0515ee09963ce8355519bc4a563854a6ecf17bb34b8 |
| 33 | PASS | final_visual_031_060.json | af2e15e40ef86e810da4f3c8851578513d2a61cf7299a6642df01514414358f6 |
| 34 | PASS | final_visual_031_060.json | bb9a51b2c60ac081249852c2a14225ddef9aeb8c0e78291d4ac994f2cce22aca |
| 35 | PASS | final_visual_031_060.json | 2b9da0dfc21d23bc209968db311bab1f28b025d58b5c23226cd0693cdb036765 |
| 36 | PASS | final_visual_031_060.json | a22e5968b114cdd282abec07139156c901fc89e68a23c02f5317ec24eafb0cb5 |
| 37 | PASS | final_visual_031_060.json | 363d6e27687db8052fabddece713409756df2a9ba418c762c119ae30f653763d |
| 38 | PASS | final_visual_031_060.json | 911b05080f370afdb7e2736d2e7bed190cdcba7e913c5f41d5d94b0b643269b5 |
| 39 | PASS WITH DENSE TABLE | final_visual_031_060.json | 57e8f7a93c794bb7fc53cd45125602defc81fff6f92ecb9bb5029cbc2bc3fed7 |
| 40 | PASS WITH DENSE TABLE | final_visual_031_060.json | 1b6d3668ec4478ad2290583b2f055a5e3639263ed10dc9f4c302bb64e3b7174c |
| 41 | PASS | final_visual_031_060.json | e8f9826d2a4be7f74eb0fc5cd95629ab720111128e5c0a8b658865e97f20233a |
| 42 | PASS | final_visual_031_060.json | d768bd56544d4a0923600dc587dd2abd1a0375ce5a414d752f805ba939370f7e |
| 43 | PASS WITH DENSE TABLE | final_visual_031_060.json | 9e171f7123e10cb729060d1f60259edcb46518f45b95eb40bd9ee73c60b610bc |
| 44 | PASS WITH DENSE TABLE | final_visual_031_060.json | 8869fa972734bcd25d16020909fac5d1653f2e18e6bf21d024cfd14dafc2880d |
| 45 | PASS | final_visual_031_060.json | c245b6b6bc85ba4a49b15de937148ad298c6ef4982a5806344ac7650b4dab695 |
| 46 | PASS | final_visual_031_060.json | 00a560dcd9dd15276379ad6ffbce1ff5cae61932fe382ec45cc0e7c6aea753ca |
| 47 | PASS WITH DENSE TABLE | final_visual_031_060.json | 3885958bea92af70729d92f7e2585e91032f438db18c9d3b6f3fa2d5db351130 |
| 48 | PASS; EQUATION VISIBLE | final_visual_031_060.json | 5cf1770ae8588a9a3419f95be8ead02d8593760d72f7c9d4af8fbaa20b19df8b |
| 49 | PASS WITH DENSE TABLE | final_visual_031_060.json | be2144557d98218a33157d1a6c0804c141c4d2aff1da74aad8006a06d20c4344 |
| 50 | PASS WITH DENSE TABLE | final_visual_031_060.json | 1673ab0fdc108bfa80fc9797af51ddf3a34dd6a69a8e1f8fc07b28237cb417ff |
| 51 | PASS | final_visual_031_060.json | 17835f75e61b5b3817744aa4f7a38b3b9e21bbc279bdc859198ed7991722a463 |
| 52 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | 3b3a0c01f88de1f1e2bf1d8146d177ca89d22e9b3e7487782bc2924f2abc25e2 |
| 53 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | edc5117de9f4bc0818775b50cbedfb7717a68d75b0b3dab0613054de026f17ea |
| 54 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | 950cb8039bcaea0546cd0843c4fdcd5645f1e746d4fadcb6f1751cf34e12d7c3 |
| 55 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | 865aed54a9c689ed5391e92fdce759c9e7d0d9affb54e982363541915c97d1bc |
| 56 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | 70fef5775b6f9409ee2b312277452949ffbd6d5c3c0b91c097d19cb317bcb363 |
| 57 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | d77b2749aa743461b5e511d98937d20945f4cca497f337f4ea37a4fb43b78aaf |
| 58 | PASS WITH APPENDIX TABLE | final_visual_031_060.json | 11338aee36ab7e459ea080a656bbfc1dec2bb3558436848c350cfa8acfb7f4e3 |
| 59 | PASS; EQUATIONS VISIBLE | final_visual_031_060.json | 98bf8bd3e427913a0f21cc820a12af4b98e28842e2154f646da1c1efe38e3d2d |
| 60 | PASS | final_visual_031_060.json | 2711137c24f15593938840bda909cace045edd701ce26364a6bc90f7db0dc72f |
| 61 | PASS_VISUAL | final_visual_061_090.json | f2ddd9d0522fab96b06aeeebb2c67ed9261dd6d94362070f12ae0409984fd1bf |
| 62 | PASS_VISUAL | final_visual_061_090.json | 02e8cdd5f9d90f2f99e89e80638ca6c8603013b774850e339f262e8f2043b706 |
| 63 | PASS_VISUAL | final_visual_061_090.json | fa9e052667e0631f8dd87904a7fe53ebb1346bcfe9da71e883156186a6cf3a9a |
| 64 | PASS_VISUAL | final_visual_061_090.json | 88dc53be121f4096b65b99d8db466879fbae6e32000f44055f378c84395b8031 |
| 65 | PASS_VISUAL | final_visual_061_090.json | d44a9068e1c106325deb550d644266cd8aa58e4bb1730cdff6c150168963d41a |
| 66 | PASS_VISUAL | final_visual_061_090.json | c3604efd727baceb93d3e718479ec097f2b96d099a30f7af84a2434bcefc336b |
| 67 | PASS_VISUAL | final_visual_061_090.json | aeb3e748ce2f95dd3a8918db7d631c146d053ed93f95d6141b933e3aa465a9a9 |
| 68 | PASS_VISUAL | final_visual_061_090.json | e10022e5aa07df7a05b9e426de3d660dc343d88e2c72612d68dc6ecbb592f7a5 |
| 69 | PASS_VISUAL | final_visual_061_090.json | 5e80addea29ba5f14ce6ce2f5f54b8d54a7de2ea812e79138dc8b941f37193b8 |
| 70 | PASS_VISUAL | final_visual_061_090.json | d5ec8c350618c0045074c9f54873c3e6d5d13a64dfe29477cf1ad9ffd647069c |
| 71 | PASS_VISUAL | final_visual_061_090.json | ad475562aff27edbdeff0442edff57b0c706bd3e3c7b1d6c7d8da4c35d72b975 |
| 72 | PASS_VISUAL | final_visual_061_090.json | 33a3f9644d3ded20d075b644248f25854e459c3ff3fee11b2857cc6204cedfa6 |
| 73 | PASS_VISUAL | final_visual_061_090.json | 823600295ad4130b45410382edea01bdd2f44c7148f5efd8dca4351affbdb29a |
| 74 | PASS_VISUAL | final_visual_061_090.json | 56ca55b5bbf18f2b606f08c30f7a50f78bbede7abf235ad02c41277a6ce67e73 |
| 75 | FINDING | final_visual_061_090.json | 7ada8a50dd6643b0eafcb100154aa9af8b926a876d3b0ca4478056f492e552ff |
| 76 | PASS_VISUAL | final_visual_061_090.json | b1b5d10ec0a4cc1ad0516f0d7ec837773615a40b5c4521ce3eff9e0b1143abde |
| 77 | FINDING | final_visual_061_090.json | df9f3e258e4fcda90526eb44478c5cca58f1b8fdbc92517acfa5723bb297a34c |
| 78 | PASS_VISUAL | final_visual_061_090.json | d275c4071727c11a1b7285ff499f733a09c2781227af8c0d8a438228f79caf9c |
| 79 | PASS_VISUAL | final_visual_061_090.json | 954aee24f348c7f06047769405f3bca28d0ba9af0d8b6255803f636569c96a82 |
| 80 | PASS_VISUAL | final_visual_061_090.json | 01e354cec372abe450e475aa7ad9af2240317fd2a46a72b898f2897774022187 |
| 81 | PASS_VISUAL | final_visual_061_090.json | ca403512f332ffde98e33428a4c717d90fe6023622ca575bbd46a372c2214e0d |
| 82 | PASS_VISUAL | final_visual_061_090.json | 7d842982bb266ab34739975f8b6c17c55754c4d78f80b808ced742636219bc6c |
| 83 | PASS_VISUAL | final_visual_061_090.json | df52b474fb740f40a61520779d392271851f3109ad44347e1007f3e8bf843ac2 |
| 84 | PASS_VISUAL | final_visual_061_090.json | c88ab78dd3d7e480b9abeb03d394bae52263b53fb8c2ed44a24ecc59cfd51fb3 |
| 85 | PASS_VISUAL | final_visual_061_090.json | ef8fd695f48560e55a60b3ccf934310545692efda9c52b9e9351ae96cc46ba42 |
| 86 | PASS_VISUAL | final_visual_061_090.json | d8f5492739cbdedb94969c0aa9dace3f46f1d2e4ea3065f1feb1e235eceec9b4 |
| 87 | PASS_VISUAL | final_visual_061_090.json | 5d69c27edb65fb1c885243f7d1805b1b006b25043c72fbb11d5200d1e4bdf759 |
| 88 | PASS_VISUAL | final_visual_061_090.json | 5c6bf7cab4ea70bd4631f9c3c6d4f19a18cc7eea86c9eac037eeacbb14de573c |
| 89 | PASS_VISUAL | final_visual_061_090.json | a78387764ecff3775eddd0d7d727cf6d0b877630f93afa154d155a83e5f19342 |
| 90 | PASS_VISUAL | final_visual_061_090.json | 6bdab8488b2392de5e16f8b0d55c6c99e2ec9bf2c6f4374315b88c446df08968 |
| 91 | PASS | final_visual_091_101.json | 39feaca18ba54860cadddd249d1b04353b492ded75189cf99447b43968e4dfce |
| 92 | PASS | final_visual_091_101.json | 7b20509b597a5e9a47084ee0e3ec61e16c7f6dd841f8a756e6ed330586cc6e4a |
| 93 | PASS_WITH_DOCUMENTED_LIMITATIONS | final_visual_091_101.json | 4a53411c6610cc6b42b40defc04c88efd74a00cef7e9cf17f1145494acba05d0 |
| 94 | PASS | final_visual_091_101.json | 2e5a850b89cd31f30249dbe42a8e0383997ca4680edf905bd251776f7c5627d4 |
| 95 | PASS | final_visual_091_101.json | 78fa4113d42afa11796d14c4183d846beb7e92cecff0c4b35a7b3c346c8fe26c |
| 96 | PASS | final_visual_091_101.json | ed615170ed044b4847ded1ca705e7fa1cd6861da9aa6a1fd33a37201cc87a68e |
| 97 | PASS | final_visual_091_101.json | 80e6ffd31e2334c56d872e42eb7e4138e041fe2201a7a8e9db299d3e01de8f0b |
| 98 | PASS_WITH_DOCUMENTED_LIMITATIONS | final_visual_091_101.json | 8e5ecb6af7ddbfcd2c16e142a13979fd6963645d30129a831651f4ddfc9de822 |
| 99 | PASS | final_visual_091_101.json | 7eb82af50762e24c12b81ebdd1c802767bdc1e288a9f750478ae7f825f75822b |
| 100 | PASS | final_visual_091_101.json | 759612a03ecc75f8877c181bcfaedf9be3149472db86cf4f9f389183f59720b0 |
| 101 | PASS | final_visual_091_101.json | 7443949d28e84a452ee5e61103732e3b22f6c6b253104e900cf7f6d8375b1dad |

### Bản ghi review gốc

```json
[
  {
    "file": "/home/khanh/mp1-work/MP1-CH2-RESUME-20261021/artifacts/final_visual_001_030.json",
    "report": {
      "status": "SELF_REVIEW_ONLY",
      "current_docx_sha256": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
      "current_pdf_sha256": "fd9ff79381519958ba917c52cb64cac17b2941b4a5e34378e5f9101d521da44a",
      "reviewed_pdf_sha256": "6a9d7d87430cfb7ac425637b30570828bc01ae5a4b47097414579d7abe480b94",
      "pixel_identity_proof": "/tmp/mp1-ch2-full-integration/final_raster_equivalence.json",
      "pixel_identity_scope": "All 101 page rasters byte-identical; this file records actual view_image inspection of pages 1–30.",
      "counts": {
        "PASS": 22,
        "NOTE": 8,
        "BLOCKER": 0
      },
      "pages": [
        {
          "page": 1,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-001.png",
          "sha256": "e2e587468893d9e80d4dfad06010147cce60cba356df8b8de865f8b8fc721311",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Chapter 2 title, 2.1 and 2.1.1 share the opening page; text readable and not clipped."
        },
        {
          "page": 2,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-002.png",
          "sha256": "2a5b54b7c1987c41136dbf9d0f31e123e531820acf5fe9f86889ee5bd58a5fba",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.1.1 finishes and 2.1.2 begins; readable, no blank page."
        },
        {
          "page": 3,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-003.png",
          "sha256": "b286ee3177bc523973fb0de928908ccebfc23fe78f4671d3a9c18888519806bc",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.1.2 continues and 2.1.3 starts with a full paragraph; no orphan heading."
        },
        {
          "page": 4,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-004.png",
          "sha256": "e09a53653aabdda265af29a087fc45c0442953ac90947db59296ba4c57bd108b",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.1.3 text finishes above a deliberate table break; lower space remains because Table 2.1.3 moves intact to page 5."
        },
        {
          "page": 5,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-005.png",
          "sha256": "07e8e9cbd3aa7231a5ca20166cb58771381c3bc35f6520789abaecfa5a706092",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.1.3, caption, rows, source note and start of 2.1.4 all fit; no clipped cell."
        },
        {
          "page": 6,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-006.png",
          "sha256": "3796fbf9773d4f0981c5123dde6200556e34fcc78f27e59dca2de320872a3042",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "METADATA ONLY paragraph begins and ends on this page; the earlier cross-page “tóm tắt” split is gone. Section continues readably."
        },
        {
          "page": 7,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-007.png",
          "sha256": "a366fac831dfec52a5bb37d0779ace1914285a329b16906c38a85aa103b3d702",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.1 closes and 2.2/2.2.1 start with text; no title-only page."
        },
        {
          "page": 8,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-008.png",
          "sha256": "7df7885730372890036b63263db0b7900b76810077d35317432d6764426f11b0",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.2.1 continues; citations and symbols legible."
        },
        {
          "page": 9,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-009.png",
          "sha256": "3b32e6ef92e8907e0cfdcb8d7fc05ff6c95282b4bd43e53457af1027cddbe0ef",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.2.1 closes and 2.2.2 starts; no clipped line."
        },
        {
          "page": 10,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-010.png",
          "sha256": "2419dbdf47bc85fe5ff03533c65c83c9264ec1c877934d927ca3d08c8a8ef945",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.2.2 closes and 2.2.3 starts; text and citations readable."
        },
        {
          "page": 11,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-011.png",
          "sha256": "278a14b2834e607f769bf90d6c934ae14069796535da478a377e0caaa1975048",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Text ends in upper half. Lower half blank because the complete Figure 2.2.3-1 moves to page 12."
        },
        {
          "page": 12,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-012.png",
          "sha256": "8934de723a91d558d7f760f570261038e95cc99737db44e1459e8cdfd5763adf",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Figure 2.2.3-1, all boxes/arrows, caption and surrounding text visible; no clipping."
        },
        {
          "page": 13,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-013.png",
          "sha256": "8a828e5c4ee3a2359393aa9d442771232a30ed6eb19402efad5d014222051906",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.2.3-1 fits completely; cells and following paragraphs legible."
        },
        {
          "page": 14,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-014.png",
          "sha256": "680a06533cb00f6ae3fa69847a85b8d1d8b7518ada9cefd5364c29cb62e270da",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "§2.2 terminology support table begins; header and rows readable."
        },
        {
          "page": 15,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-015.png",
          "sha256": "951fae32b689b3b22a4b8a0b9d5a5e8df875b5305046eb9dfad7641264ad9790",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "§2.2 terminology continuation legible. 2x check confirmed no cell overlap or clipping."
        },
        {
          "page": 16,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-016.png",
          "sha256": "88443283210e07fc712dd4069dd6de33f5d2ab9bb978ff5b3fd01b326ad366d1",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "§2.2 terminology continuation with repeated header; all rows legible."
        },
        {
          "page": 17,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-017.png",
          "sha256": "8268ab333533fc67621f4a99aa22d27331319f3d01149dd08da58df3b5715915",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "§2.2 terminology continuation with repeated header; all rows legible."
        },
        {
          "page": 18,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-018.png",
          "sha256": "0957a80c7085df5ceeb6fef0fc951c7ffc6eba77e0d52ba12d695734163c03be",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "§2.2 terminology ends; 2.3 parent heading and 2.3.1 begin below on same page."
        },
        {
          "page": 19,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-019.png",
          "sha256": "ed6938d326c59875ffda5851f45e3c613d2224e8f178e6ac2d792c27bc59fd41",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.3.1 text ends high on page; Table 2.3.1 begins next page to keep table layout. No content loss."
        },
        {
          "page": 20,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-020.png",
          "sha256": "f77a57653fba30287940ee8557e8c3fc5a286fc95efcee2a78848cdd8d33bf1e",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.3.1 uses uniform small type and continues by one row to page 21; header repeated there. No clipping or oversized text."
        },
        {
          "page": 21,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-021.png",
          "sha256": "69442080a648efd9ba62924a99e566864d2b0783768e9f05b52cd97ccb48adf5",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Final row and source note for Table 2.3.1 stay together; 2.3.2 follows. Readable."
        },
        {
          "page": 22,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-022.png",
          "sha256": "d74a44fb7514cc5d03af14cf41238822af1d075f6671bac98e90979bf02b2744",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.3.2 text ends mid-page; Table 2.3.2 moves intact to page 23. No clipped text."
        },
        {
          "page": 23,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-023.png",
          "sha256": "e282c22524b7d33471943ac418e986646f62fd9ba3968cf7c6af6c592db6ac9f",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.3.2 is borderless with dense columns, but text and caption remain legible; 2.3.3 begins below."
        },
        {
          "page": 24,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-024.png",
          "sha256": "da7bfd21579028c53a5d74e64231fe850807e83e7ba4388c35e9895030e6e1df",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.3.3 prose continues; no clipping or anomalous break."
        },
        {
          "page": 25,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-025.png",
          "sha256": "8e9e66c2dfdb23299770ef857cc19d87d0561c31727bb2bc880d830c59a72973",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.3.3, caption and 2.3.4 opening fit; table cells legible."
        },
        {
          "page": 26,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-026.png",
          "sha256": "bb7a9b3b757a393982de26803b76c435cf6bb8b2953f69b96a5c2e7123ddb204",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.3.4 displays all three equations and labels (1)–(3); formula bodies are visible. Paragraphs and citations legible."
        },
        {
          "page": 27,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-027.png",
          "sha256": "142b00f11aa00de43bf8ac1a6d15c203002219fd919f2cf54c5a489505c06105",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.3.4 closes; Table 2.3.4 and 2.3.5 heading fit and are readable."
        },
        {
          "page": 28,
          "status": "PASS",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-028.png",
          "sha256": "2797791a0808a6740901de1483633dbed5be99305bb540d1e2f96a3aaaa40669",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "2.3.5 synthesis prose readable, with no clipping."
        },
        {
          "page": 29,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-029.png",
          "sha256": "e5a87bed1e00846f1e900631235a56f77badd13f49c9883c5597fdae8329cab7",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.3.5 starts and continues with one row to page 30; header repeats. No clipping."
        },
        {
          "page": 30,
          "status": "NOTE",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-030.png",
          "sha256": "ae342d60edf6abd070ab3235561d52b289476fbf082a185660bbec8489b3688a",
          "view_image_inspected": true,
          "blank_page": false,
          "visible_clipping": false,
          "finding": "Table 2.3.5 last row/source arrangement stays readable; unnumbered 2.3 terminology support table begins below. Editorial placement remains separate from visual integrity."
        }
      ],
      "no_visual_blocker_in_range": true,
      "scientific_scope": "Layout/render check only. Does not approve literature claims, school style, P3 protocol, or human decisions."
    }
  },
  {
    "file": "/home/khanh/mp1-work/MP1-CH2-RESUME-20261021/artifacts/final_visual_031_060.json",
    "report": {
      "review_type": "SELF_REVIEW_ONLY; not independent acceptance",
      "scope": {
        "pdf": "/tmp/mp1-ch2-full-integration/render_math/MP1_CH2_FULL_INTEGRATED.pdf",
        "pages_inclusive": [
          31,
          60
        ],
        "count": 30,
        "page_images": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-031.png through /tmp/mp1-ch2-full-integration/pages-reviewed-final/page-060.png",
        "additional_detail_renders": [
          "250 dpi pages 31–36 for glossary table header/cell inspection",
          "250 dpi pages 59–60 for equations and continuation"
        ]
      },
      "frozen_docx_sha256_reported_by_parent": "4d4005611dec7cd2714b87499b570f3f8f140f7e638c271a7436f3a9f8b0ea5b",
      "pdf_sha256_reported_by_parent": "fd9ff79381519958ba917c52cb64cac17b2941b4a5e34378e5f9101d521da44a",
      "pdf_sha256_observed_at_review": "fd9ff79381519958ba917c52cb64cac17b2941b4a5e34378e5f9101d521da44a",
      "pdf_hash_matches_reported": true,
      "method": "All 30 final page PNGs were individually opened at original resolution with view_image. Pages 31–36 and 59–60 were additionally rendered and individually viewed at 250 dpi. Targeted crops of current PDF pages 35, 36, 54, 56, and 57 were also opened with view_image. No contact sheet used. final_raster_equivalence.json confirms all 101 current-PDF page rasters are byte-identical to pages-reviewed-final images.",
      "summary": {
        "pages_reviewed": 30,
        "equations_checked": {
          "p48": "Q_out ≥ Q_in visible",
          "p59": [
            "(2.5.1-1) |F_t| ≤ μ_s N",
            "(2.5.1-2) |t_t(x)| ≤ μ_s p_n(x)"
          ],
          "render_visible_missing_equations": 0
        },
        "layout_findings": [
          "Dense comparison tables on pp.39–40, 43–44, 47, 49–50 are compact but fit page width."
        ],
        "sparse_pages": []
      },
      "findings": [
        {
          "id": "FVIS-03",
          "severity": "low",
          "pages": [
            39,
            40,
            43,
            44,
            47,
            49,
            50
          ],
          "finding": "Comparison tables have compact font and wrapped text but remain within page margins with no visible clipping. Targeted header crops also confirmed the repeated headers on pp.35–36 and pp.54, 56–57 are complete."
        }
      ],
      "pages": [
        {
          "pdf_page": 31,
          "status": "PASS",
          "visual_notes": "Glossary/table begins with complete five-column header; cells and citations visible, centered, and inside margins.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-031.png",
          "image_sha256": "73835a477cc3b06157af207db9104745ce1cd770ff80af6133867c60844bcb4b",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 32,
          "status": "PASS",
          "visual_notes": "Glossary continuation; complete repeated header visible at 250 dpi. Rows intact and within margins.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-032.png",
          "image_sha256": "1277d3f1091a6523f31dd0515ee09963ce8355519bc4a563854a6ecf17bb34b8",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 33,
          "status": "PASS",
          "visual_notes": "Glossary continuation; complete repeated header visible at 250 dpi. No clipping or overlap.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-033.png",
          "image_sha256": "af2e15e40ef86e810da4f3c8851578513d2a61cf7299a6642df01514414358f6",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 34,
          "status": "PASS",
          "visual_notes": "Glossary continuation; full header and rows visible. No clipping/overlap.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-034.png",
          "image_sha256": "bb9a51b2c60ac081249852c2a14225ddef9aeb8c0e78291d4ac994f2cce22aca",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 35,
          "status": "PASS",
          "visual_notes": "Glossary table continues with complete five-column repeated header. Targeted 160 pt top crop of current PDF confirms all labels (English term; Thuật ngữ tiếng Việt; Định nghĩa cơ học; Ngữ cảnh sử dụng; Nguồn) are visible; no clipping. Body rows fit.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-035.png",
          "image_sha256": "2b9da0dfc21d23bc209968db311bab1f28b025d58b5c23226cd0693cdb036765",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 36,
          "status": "PASS",
          "visual_notes": "Glossary table continues with complete five-column repeated header. Targeted 160 pt top crop of current PDF confirms all labels (English term; Thuật ngữ tiếng Việt; Định nghĩa cơ học; Ngữ cảnh sử dụng; Nguồn) are visible; no clipping. Body rows fit.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-036.png",
          "image_sha256": "a22e5968b114cdd282abec07139156c901fc89e68a23c02f5317ec24eafb0cb5",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 37,
          "status": "PASS",
          "visual_notes": "Final glossary rows end, then §2.4 begins on same page. Full table header visible; transition is coherent.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-037.png",
          "image_sha256": "363d6e27687db8052fabddece713409756df2a9ba418c762c119ae30f653763d",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 38,
          "status": "PASS",
          "visual_notes": "Prose continuation, no clipping/overlap or orphan heading.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-038.png",
          "image_sha256": "911b05080f370afdb7e2736d2e7bed190cdcba7e913c5f41d5d94b0b643269b5",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 39,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Table 2.4.1 caption and first rows begin near page foot; compact six-column text but readable. Table continues to p.40.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-039.png",
          "image_sha256": "57e8f7a93c794bb7fc53cd45125602defc81fff6f92ecb9bb5029cbc2bc3fed7",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 40,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Table 2.4.1 continues with repeated full header and final rows, then prose begins. Cells remain within margins.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-040.png",
          "image_sha256": "1b6d3668ec4478ad2290583b2f055a5e3639263ed10dc9f4c302bb64e3b7174c",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 41,
          "status": "PASS",
          "visual_notes": "Prose page, no visible layout defects.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-041.png",
          "image_sha256": "e8f9826d2a4be7f74eb0fc5cd95629ab720111128e5c0a8b658865e97f20233a",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 42,
          "status": "PASS",
          "visual_notes": "Prose page, no visible layout defects.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-042.png",
          "image_sha256": "d768bd56544d4a0923600dc587dd2abd1a0375ce5a414d752f805ba939370f7e",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 43,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Table 2.4.2 caption and initial rows at page foot; text small but fits. Continuation on p.44.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-043.png",
          "image_sha256": "9e171f7123e10cb729060d1f60259edcb46518f45b95eb40bd9ee73c60b610bc",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 44,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Table 2.4.2 continues with repeated header and completes; following prose and subsection heading fit cleanly.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-044.png",
          "image_sha256": "8869fa972734bcd25d16020909fac5d1653f2e18e6bf21d024cfd14dafc2880d",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 45,
          "status": "PASS",
          "visual_notes": "§2.4.3 prose continuation; no clipping or awkward orphan.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-045.png",
          "image_sha256": "c245b6b6bc85ba4a49b15de937148ad298c6ef4982a5806344ac7650b4dab695",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 46,
          "status": "PASS",
          "visual_notes": "Prose page ends with normal lower white space; no clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-046.png",
          "image_sha256": "00a560dcd9dd15276379ad6ffbce1ff5cae61932fe382ec45cc0e7c6aea753ca",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 47,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Table 2.4.3 has compact six-column typesetting but all cells fit; following synthesis prose is legible.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-047.png",
          "image_sha256": "3885958bea92af70729d92f7e2585e91032f438db18c9d3b6f3fa2d5db351130",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 48,
          "status": "PASS; EQUATION VISIBLE",
          "visual_notes": "§2.4.4 prose and subheads fit. Displayed Q_out ≥ Q_in is visible and legible; no clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-048.png",
          "image_sha256": "5cf1770ae8588a9a3419f95be8ead02d8593760d72f7c9d4af8fbaa20b19df8b",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 49,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Prose continues normally; Table 2.4.4 caption and first rows begin below, with continuation to p.50. No sparse-page issue.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-049.png",
          "image_sha256": "be2144557d98218a33157d1a6c0804c141c4d2aff1da74aad8006a06d20c4344",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 50,
          "status": "PASS WITH DENSE TABLE",
          "visual_notes": "Table 2.4.4 continues with repeated header and completes; following prose begins normally. Text compact but cells fit.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-050.png",
          "image_sha256": "1673ab0fdc108bfa80fc9797af51ddf3a34dd6a69a8e1f8fc07b28237cb417ff",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 51,
          "status": "PASS",
          "visual_notes": "Section-ending prose page; no unusual blank area or clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-051.png",
          "image_sha256": "17835f75e61b5b3817744aa4f7a38b3b9e21bbc279bdc859198ed7991722a463",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 52,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix terminology table begins with title and three-column header; text dense but readable.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-052.png",
          "image_sha256": "3b3a0c01f88de1f1e2bf1d8146d177ca89d22e9b3e7487782bc2924f2abc25e2",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 53,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix table continues with full repeated header. No clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-053.png",
          "image_sha256": "edc5117de9f4bc0818775b50cbedfb7717a68d75b0b3dab0613054de026f17ea",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 54,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix table continuation; targeted 160 pt top crop of current PDF confirms complete three-column header (English / Tiếng Việt; Định nghĩa và ngữ cảnh; Nguồn) is visible. Rows intact; no clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-054.png",
          "image_sha256": "950cb8039bcaea0546cd0843c4fdcd5645f1e746d4fadcb6f1751cf34e12d7c3",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 55,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix table continues with repeated header and compact entries; no clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-055.png",
          "image_sha256": "865aed54a9c689ed5391e92fdce759c9e7d0d9affb54e982363541915c97d1bc",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 56,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix table continuation; targeted 160 pt top crop of current PDF confirms complete three-column header (English / Tiếng Việt; Định nghĩa và ngữ cảnh; Nguồn) is visible. Rows intact; no clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-056.png",
          "image_sha256": "70fef5775b6f9409ee2b312277452949ffbd6d5c3c0b91c097d19cb317bcb363",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 57,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix table continuation; targeted 160 pt top crop of current PDF confirms complete three-column header (English / Tiếng Việt; Định nghĩa và ngữ cảnh; Nguồn) is visible. Rows intact; no clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-057.png",
          "image_sha256": "d77b2749aa743461b5e511d98937d20945f4cca497f337f4ea37a4fb43b78aaf",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 58,
          "status": "PASS WITH APPENDIX TABLE",
          "visual_notes": "Appendix table continuation has full header; rows fit. No visible clipping.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-058.png",
          "image_sha256": "11338aee36ab7e459ea080a656bbfc1dec2bb3558436848c350cfa8acfb7f4e3",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 59,
          "status": "PASS; EQUATIONS VISIBLE",
          "visual_notes": "Appendix table ends; §2.5 starts. At 250 dpi, (2.5.1-1) |F_t| ≤ μ_s N and (2.5.1-2) |t_t(x)| ≤ μ_s p_n(x) are both present and readable, including subscripts.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-059.png",
          "image_sha256": "98bf8bd3e427913a0f21cc820a12af4b98e28842e2154f646da1c1efe38e3d2d",
          "reviewed_at": "original raster via view_image"
        },
        {
          "pdf_page": 60,
          "status": "PASS",
          "visual_notes": "§2.5 prose continues under next subheading. No clipping, overlap, or abnormal blank space.",
          "image": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-060.png",
          "image_sha256": "2711137c24f15593938840bda909cace045edd701ce26364a6bc90f7db0dc72f",
          "reviewed_at": "original raster via view_image"
        }
      ],
      "raster_equivalence_evidence": {
        "path": "/tmp/mp1-ch2-full-integration/final_raster_equivalence.json",
        "final_docx_sha256": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
        "final_pdf_sha256": "fd9ff79381519958ba917c52cb64cac17b2941b4a5e34378e5f9101d521da44a",
        "reviewed_pdf_sha256": "6a9d7d87430cfb7ac425637b30570828bc01ae5a4b47097414579d7abe480b94",
        "pages_compared": 101,
        "all_page_rasters_byte_identical": true,
        "interpretation": "Current canonical PDF differs in 33 paragraph outlineLvl overrides only; all 101 rendered page rasters are byte-identical to the reviewed image set, so the pages actually inspected are visually identical to the current canonical render."
      }
    }
  },
  {
    "file": "/home/khanh/mp1-work/MP1-CH2-RESUME-20261021/artifacts/final_visual_061_090.json",
    "report": {
      "authority": "SELF_REVIEW_ONLY",
      "pdf_path": "/tmp/mp1-ch2-full-integration/render_math/MP1_CH2_FULL_INTEGRATED.pdf",
      "pdf_sha256": "fd9ff79381519958ba917c52cb64cac17b2941b4a5e34378e5f9101d521da44a",
      "docx_sha256_reported_by_root": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
      "page_range": [
        61,
        90
      ],
      "pages_reviewed": 30,
      "method": "Every assigned PNG 61–90 opened with view_image original. Apparent p63 heading collision and p80–81 table header clipping from downsampled or overly large image display were checked against targeted high-resolution crops; p63 line break and p81 repeated header/top border are present. The 30 reviewed PNG SHA-256 values match the current final PDF raster hashes in final_raster_equivalence.json.",
      "overall_status": "PASS_VISUAL_WITH_MINOR_STYLE_NOTES",
      "equations_checked": {
        "2.5.2-1_to_2.5.2-4": "VISIBLE",
        "2.5.3-1_to_2.5.3-6": "VISIBLE"
      },
      "pages": [
        {
          "page": 61,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-061.png",
          "image_sha256": "f2ddd9d0522fab96b06aeeebb2c67ed9261dd6d94362070f12ae0409984fd1bf",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.1 pressure threshold models; three displayed equations visible and readable.",
          "findings": []
        },
        {
          "page": 62,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-062.png",
          "image_sha256": "02e8cdd5f9d90f2f99e89e80638ca6c8603013b774850e339f262e8f2043b706",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "Table 2.5.1 complete and readable; assumptions prose follows.",
          "findings": []
        },
        {
          "page": 63,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-063.png",
          "image_sha256": "fa9e052667e0631f8dd87904a7fe53ebb1346bcfe9da71e883156186a6cf3a9a",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "Transition to §2.5.2; heading/body separation confirmed at 220 dpi; readable.",
          "findings": []
        },
        {
          "page": 64,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-064.png",
          "image_sha256": "88dc53be121f4096b65b99d8db466879fbae6e32000f44055f378c84395b8031",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.2 formulas (2.5.2-1)–(2.5.2-4) visible and readable.",
          "findings": []
        },
        {
          "page": 65,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-065.png",
          "image_sha256": "d44a9068e1c106325deb550d644266cd8aa58e4bb1730cdff6c150168963d41a",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.2 mechanics prose; readable.",
          "findings": []
        },
        {
          "page": 66,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-066.png",
          "image_sha256": "c3604efd727baceb93d3e718479ec097f2b96d099a30f7af84a2434bcefc336b",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "Table 2.5.2 and transition; readable.",
          "findings": []
        },
        {
          "page": 67,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-067.png",
          "image_sha256": "aeb3e748ce2f95dd3a8918db7d631c146d053ed93f95d6141b933e3aa465a9a9",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.3 formulas (2.5.3-1)–(2.5.3-4) visible and readable.",
          "findings": []
        },
        {
          "page": 68,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-068.png",
          "image_sha256": "e10022e5aa07df7a05b9e426de3d660dc343d88e2c72612d68dc6ecbb592f7a5",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.3 formula (2.5.3-5) visible and readable.",
          "findings": []
        },
        {
          "page": 69,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-069.png",
          "image_sha256": "5e80addea29ba5f14ce6ce2f5f54b8d54a7de2ea812e79138dc8b941f37193b8",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.3 formula (2.5.3-6) visible and readable.",
          "findings": []
        },
        {
          "page": 70,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-070.png",
          "image_sha256": "d5ec8c350618c0045074c9f54873c3e6d5d13a64dfe29477cf1ad9ffd647069c",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "Table 2.5.3 and start §2.5.4; readable.",
          "findings": []
        },
        {
          "page": 71,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-071.png",
          "image_sha256": "ad475562aff27edbdeff0442edff57b0c706bd3e3c7b1d6c7d8da4c35d72b975",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.4 prose; readable.",
          "findings": []
        },
        {
          "page": 72,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-072.png",
          "image_sha256": "33a3f9644d3ded20d075b644248f25854e459c3ff3fee11b2857cc6204cedfa6",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "Table 2.5.4 complete and readable.",
          "findings": []
        },
        {
          "page": 73,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-073.png",
          "image_sha256": "823600295ad4130b45410382edea01bdd2f44c7148f5efd8dca4351affbdb29a",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.4 prose; readable.",
          "findings": []
        },
        {
          "page": 74,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-074.png",
          "image_sha256": "56ca55b5bbf18f2b606f08c30f7a50f78bbede7abf235ad02c41277a6ce67e73",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.4 closing prose; readable.",
          "findings": []
        },
        {
          "page": 75,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-075.png",
          "image_sha256": "7ada8a50dd6643b0eafcb100154aa9af8b926a876d3b0ca4478056f492e552ff",
          "view_image_checked": true,
          "status": "FINDING",
          "observation": "§2.5.5 opens with black heading; readable; style differs from adjacent blue subsection headings.",
          "findings": [
            {
              "severity": "P3",
              "type": "heading_style_inconsistent",
              "detail": "§2.5.5 heading black rather than blue as adjacent headings."
            }
          ]
        },
        {
          "page": 76,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-076.png",
          "image_sha256": "b1b5d10ec0a4cc1ad0516f0d7ec837773615a40b5c4521ce3eff9e0b1143abde",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5.5 prose; readable.",
          "findings": []
        },
        {
          "page": 77,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-077.png",
          "image_sha256": "df9f3e258e4fcda90526eb44478c5cca58f1b8fdbc92517acfa5723bb297a34c",
          "view_image_checked": true,
          "status": "FINDING",
          "observation": "Table 2.5.5, black caption; readable; style differs from adjacent blue captions.",
          "findings": [
            {
              "severity": "P3",
              "type": "caption_style_inconsistent",
              "detail": "Table 2.5.5 caption black rather than blue as adjacent table captions."
            }
          ]
        },
        {
          "page": 78,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-078.png",
          "image_sha256": "d275c4071727c11a1b7285ff499f733a09c2781227af8c0d8a438228f79caf9c",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5 glossary starts; readable.",
          "findings": []
        },
        {
          "page": 79,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-079.png",
          "image_sha256": "954aee24f348c7f06047769405f3bca28d0ba9af0d8b6255803f636569c96a82",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5 glossary continuation; repeated header and rows readable.",
          "findings": []
        },
        {
          "page": 80,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-080.png",
          "image_sha256": "01e354cec372abe450e475aa7ad9af2240317fd2a46a72b898f2897774022187",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5 glossary continuation; header fully visible at 220 dpi and rows readable.",
          "findings": []
        },
        {
          "page": 81,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-081.png",
          "image_sha256": "ca403512f332ffde98e33428a4c717d90fe6023622ca575bbd46a372c2214e0d",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5 glossary continuation; full repeated header and top border at normal margin confirmed by targeted crop header-081.png. Contact traction begins below header.",
          "findings": []
        },
        {
          "page": 82,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-082.png",
          "image_sha256": "7d842982bb266ab34739975f8b6c17c55754c4d78f80b808ced742636219bc6c",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.5 glossary ends and §2.6 begins; readable.",
          "findings": []
        },
        {
          "page": 83,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-083.png",
          "image_sha256": "df52b474fb740f40a61520779d392271851f3109ad44347e1007f3e8bf843ac2",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.1 prose; readable.",
          "findings": []
        },
        {
          "page": 84,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-084.png",
          "image_sha256": "c88ab78dd3d7e480b9abeb03d394bae52263b53fb8c2ed44a24ecc59cfd51fb3",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.1 prose; readable.",
          "findings": []
        },
        {
          "page": 85,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-085.png",
          "image_sha256": "ef8fd695f48560e55a60b3ccf934310545692efda9c52b9e9351ae96cc46ba42",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.2 begins; readable.",
          "findings": []
        },
        {
          "page": 86,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-086.png",
          "image_sha256": "d8f5492739cbdedb94969c0aa9dace3f46f1d2e4ea3065f1feb1e235eceec9b4",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.2 prose; readable.",
          "findings": []
        },
        {
          "page": 87,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-087.png",
          "image_sha256": "5d69c27edb65fb1c885243f7d1805b1b006b25043c72fbb11d5200d1e4bdf759",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.2 prose; readable.",
          "findings": []
        },
        {
          "page": 88,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-088.png",
          "image_sha256": "5c6bf7cab4ea70bd4631f9c3c6d4f19a18cc7eea86c9eac037eeacbb14de573c",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.3 begins; readable.",
          "findings": []
        },
        {
          "page": 89,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-089.png",
          "image_sha256": "a78387764ecff3775eddd0d7d727cf6d0b877630f93afa154d155a83e5f19342",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.3 prose; readable.",
          "findings": []
        },
        {
          "page": 90,
          "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-090.png",
          "image_sha256": "6bdab8488b2392de5e16f8b0d55c6c99e2ec9bf2c6f4374315b88c446df08968",
          "view_image_checked": true,
          "status": "PASS_VISUAL",
          "observation": "§2.6.4 begins; readable.",
          "findings": []
        }
      ],
      "limitations": [
        "Only assigned final pages 61–90 were inspected in this report.",
        "This is self-review, not independent acceptance."
      ],
      "reviewed_source_pdf_sha256": "6a9d7d87430cfb7ac425637b30570828bc01ae5a4b47097414579d7abe480b94",
      "raster_equivalence_proof": "/tmp/mp1-ch2-full-integration/final_raster_equivalence.json",
      "raster_equivalence_verified_for_assigned_pages": true
    }
  },
  {
    "file": "/home/khanh/mp1-work/MP1-CH2-RESUME-20261021/artifacts/final_visual_091_101.json",
    "report": [
      {
        "page": 91,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-091.png",
        "image_sha256": "39feaca18ba54860cadddd249d1b04353b492ded75189cf99447b43968e4dfce",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 92,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-092.png",
        "image_sha256": "7b20509b597a5e9a47084ee0e3ec61e16c7f6dd841f8a756e6ed330586cc6e4a",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 93,
        "status": "PASS_WITH_DOCUMENTED_LIMITATIONS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-093.png",
        "image_sha256": "4a53411c6610cc6b42b40defc04c88efd74a00cef7e9cf17f1145494acba05d0",
        "findings": "Bảng thuật ngữ hỗ trợ giữ nguyên, trang kết bảng thưa nhưng không trắng hoặc clipping.",
        "severity": "P3"
      },
      {
        "page": 94,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-094.png",
        "image_sha256": "2e5a850b89cd31f30249dbe42a8e0383997ca4680edf905bd251776f7c5627d4",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 95,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-095.png",
        "image_sha256": "78fa4113d42afa11796d14c4183d846beb7e92cecff0c4b35a7b3c346c8fe26c",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 96,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-096.png",
        "image_sha256": "ed615170ed044b4847ded1ca705e7fa1cd6861da9aa6a1fd33a37201cc87a68e",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 97,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-097.png",
        "image_sha256": "80e6ffd31e2334c56d872e42eb7e4138e041fe2201a7a8e9db299d3e01de8f0b",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 98,
        "status": "PASS_WITH_DOCUMENTED_LIMITATIONS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-098.png",
        "image_sha256": "8e5ecb6af7ddbfcd2c16e142a13979fd6963645d30129a831651f4ddfc9de822",
        "findings": "Bảng thuật ngữ hỗ trợ giữ nguyên, trang kết bảng thưa nhưng không trắng hoặc clipping.",
        "severity": "P3"
      },
      {
        "page": 99,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-099.png",
        "image_sha256": "7eb82af50762e24c12b81ebdd1c802767bdc1e288a9f750478ae7f825f75822b",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 100,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-100.png",
        "image_sha256": "759612a03ecc75f8877c181bcfaedf9be3149472db86cf4f9f389183f59720b0",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      },
      {
        "page": 101,
        "status": "PASS",
        "reviewer": "/root",
        "review_method": "view_image original 1.5x 893x1263, đọc trực tiếp từng trang; bảng/citation được xem ở mức đọc được",
        "image_path": "/tmp/mp1-ch2-full-integration/pages-reviewed-final/page-101.png",
        "image_sha256": "7443949d28e84a452ee5e61103732e3b22f6c6b253104e900cf7f6d8375b1dad",
        "findings": "Nội dung, ký hiệu, citation và bố cục đọc được; không mất đối tượng.",
        "severity": "NONE"
      }
    ]
  }
]
```
## Dữ liệu QA trực tiếp

```json
{
  "docx_sha256": "9c6ada2bf80ca37ed14278d48fa01e3d385870c5f74631295a71ee72825c0269",
  "zip_crc": "PASS",
  "xml_parts_parsed": 16,
  "relationships_checked": 14,
  "external_relationships": [],
  "bookmark_pairs": 421,
  "duplicate_bookmark_ids": 0,
  "dangling_relationships": 0,
  "style_references": "PASS",
  "media": [
    {
      "section": 2,
      "source": "word/media/image1.png",
      "sha256": "26db28e4b1ff2d51a4be4f140dbf082ef8817301e7cfcbc9d955177409784b8f",
      "output": [
        "word/media/section2_image1.png"
      ]
    }
  ],
  "source_stats": {
    "1": {
      "all_paragraphs": 72,
      "body_paragraphs": 42,
      "tables": 1,
      "omml": 0,
      "drawings": 0
    },
    "2": {
      "all_paragraphs": 178,
      "body_paragraphs": 58,
      "tables": 2,
      "omml": 0,
      "drawings": 1
    },
    "3": {
      "all_paragraphs": 509,
      "body_paragraphs": 63,
      "tables": 6,
      "omml": 3,
      "drawings": 0
    },
    "4": {
      "all_paragraphs": 652,
      "body_paragraphs": 101,
      "tables": 5,
      "omml": 1,
      "drawings": 0
    },
    "5": {
      "all_paragraphs": 499,
      "body_paragraphs": 165,
      "tables": 6,
      "omml": 15,
      "drawings": 0
    },
    "6": {
      "all_paragraphs": 261,
      "body_paragraphs": 81,
      "tables": 1,
      "omml": 0,
      "drawings": 0
    }
  },
  "input_objects": {
    "tables": 21,
    "omml": 19,
    "drawings": 1
  },
  "output_objects": {
    "tables": 21,
    "omml": 19,
    "drawings": 1
  },
  "superscript_subscript_before": {
    "subscript": 91
  },
  "superscript_subscript_after": {
    "subscript": 91
  },
  "input_citation_groups": 758,
  "input_atomic_citations": 783,
  "output_citation_groups": 778,
  "output_atomic_citations": 783,
  "input_local_reference_entries": 69,
  "input_unique_references": 30,
  "output_references": 30,
  "global_renumbering_entries": 69,
  "duplicates_removed": 39,
  "missing_references": 0,
  "orphan_references": 0,
  "numbering_conflicts": 0,
  "unexplained_duplicates": 0,
  "doi_identity_conflicts_unresolved": 0,
  "first_citation_order": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30
  ],
  "captions": [
    {
      "label": "Bảng 2.1.3",
      "container": "/w:document/w:body/w:p[27]",
      "text": "Bảng 2.1.3. Khung trích xuất chín phương diện từ ma trận luận cứ và bản ghi bằng chứng"
    },
    {
      "label": "Hình 2.2.3-1",
      "container": "/w:document/w:body/w:p[73]",
      "text": "Hình 2.2.3-1. Sơ đồ khái niệm về đường tác động của áp suất và suy luận từ quan sát. Sơ đồ khái niệm; không phải hình học, vị trí cảm biến hoặc thiết kế MP1 đã được phê duyệt."
    },
    {
      "label": "Bảng 2.2.3-1",
      "container": "/w:document/w:body/w:p[78]",
      "text": "Bảng 2.2.3-1. Trạng thái quan sát phụ thuộc hệ đo và mô hình."
    },
    {
      "label": "Bảng 2.3.1",
      "container": "/w:document/w:body/w:p[90]",
      "text": "Bảng 2.3.1. Phân loại hai tầng các nguyên lý và kiến trúc điều chỉnh độ cứng"
    },
    {
      "label": "Bảng 2.3.2",
      "container": "/w:document/w:body/w:p[99]",
      "text": "Bảng 2.3.2. So sánh các kiến trúc kẹt dây/sợi và nguồn đối chiếu"
    },
    {
      "label": "Bảng 2.3.3",
      "container": "/w:document/w:body/w:p[107]",
      "text": "Bảng 2.3.3. So sánh cơ chế kẹt lớp/tấm và kẹt hạt theo cấu trúc tiếp xúc và phương thức tạo tải"
    },
    {
      "label": "Bảng 2.3.4",
      "container": "/w:document/w:body/w:p[121]",
      "text": "Bảng 2.3.4. So sánh cơ chế kẹt phụ thuộc áp suất và mô hình chuyển trạng thái"
    },
    {
      "label": "Bảng 2.3.5",
      "container": "/w:document/w:body/w:p[131]",
      "text": "Bảng 2.3.5. Tổng hợp các yếu tố chi phối đáp ứng cơ học và giới hạn so sánh giữa các cơ chế jamming"
    },
    {
      "label": "Bảng A.1",
      "container": "/w:document/w:body/w:p[134]",
      "text": "Bảng A.1. Thuật ngữ chuyên ngành dùng trong mục 2.3"
    },
    {
      "label": "Bảng 2.4.1",
      "container": "/w:document/w:body/w:p[147]",
      "text": "Bảng 2.4.1. So sánh bằng chứng về đáp ứng cơ–nhiệt của NiTi và ảnh hưởng của cấu trúc cáp"
    },
    {
      "label": "Bảng 2.4.2",
      "container": "/w:document/w:body/w:p[167]",
      "text": "Bảng 2.4.2. So sánh mô hình cơ học và bằng chứng thực nghiệm về tiếp xúc, trượt tương đối và đáp ứng uốn của bó dây/cáp"
    },
    {
      "label": "Bảng 2.4.3",
      "container": "/w:document/w:body/w:p[181]",
      "text": "Bảng 2.4.3. So sánh cơ chế SMA điều biến ma sát và bằng chứng về khả năng phục hồi"
    },
    {
      "label": "Bảng 2.4.4",
      "container": "/w:document/w:body/w:p[202]",
      "text": "Bảng 2.4.4. So sánh các cơ cấu tạo và truyền áp suất với vai trò của vật liệu SMA"
    },
    {
      "label": "Bảng A.2",
      "container": "/w:document/w:body/w:p[221]",
      "text": "Bảng A.2. Thuật ngữ cơ học và cách dùng trong mục 2.4"
    },
    {
      "label": "Bảng 2.5.1",
      "container": "/w:document/w:body/w:p[252]",
      "text": "Bảng 2.5.1. So sánh điều kiện dính–trượt, đại lượng quan sát và giới hạn mô hình ma sát"
    },
    {
      "label": "Bảng 2.5.2",
      "container": "/w:document/w:body/w:p[287]",
      "text": "Bảng 2.5.2. Giả thiết cơ học và giới hạn áp dụng của hai trạng thái độ cứng uốn tham chiếu"
    },
    {
      "label": "Bảng 2.5.3",
      "container": "/w:document/w:body/w:p[323]",
      "text": "Bảng 2.5.3. Đại lượng đánh giá độ cứng và vòng trễ trong các nghiên cứu jamming"
    },
    {
      "label": "Bảng 2.5.4",
      "container": "/w:document/w:body/w:p[338]",
      "text": "Bảng 2.5.4. So sánh đại lượng đo, phương pháp nhận dạng và phạm vi kiểm chứng của các nghiên cứu"
    },
    {
      "label": "Bảng 2.5.5",
      "container": "/w:document/w:body/w:p[365]",
      "text": "Bảng 2.5.5. So sánh khả năng mô tả, yêu cầu tham số và phạm vi kiểm chứng của các nhóm phương pháp"
    }
  ],
  "cross_reference_occurrences": 25,
  "cross_reference_checks": [
    {
      "label": "Bảng 2.1.3",
      "container": "/w:document/w:body/w:p[21]",
      "target": "/w:document/w:body/w:p[27]",
      "start": 213,
      "end": 223
    },
    {
      "label": "Bảng 2.1.3",
      "container": "/w:document/w:body/w:p[27]",
      "target": "/w:document/w:body/w:p[27]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Hình 2.2.3-1",
      "container": "/w:document/w:body/w:p[71]",
      "target": "/w:document/w:body/w:p[73]",
      "start": 0,
      "end": 12
    },
    {
      "label": "Hình 2.2.3-1",
      "container": "/w:document/w:body/w:p[73]",
      "target": "/w:document/w:body/w:p[73]",
      "start": 0,
      "end": 12
    },
    {
      "label": "Bảng 2.2.3-1",
      "container": "/w:document/w:body/w:p[77]",
      "target": "/w:document/w:body/w:p[78]",
      "start": 330,
      "end": 342
    },
    {
      "label": "Bảng 2.2.3-1",
      "container": "/w:document/w:body/w:p[78]",
      "target": "/w:document/w:body/w:p[78]",
      "start": 0,
      "end": 12
    },
    {
      "label": "Bảng 2.3.1",
      "container": "/w:document/w:body/w:p[90]",
      "target": "/w:document/w:body/w:p[90]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.3.2",
      "container": "/w:document/w:body/w:p[99]",
      "target": "/w:document/w:body/w:p[99]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.3.3",
      "container": "/w:document/w:body/w:p[107]",
      "target": "/w:document/w:body/w:p[107]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.3.4",
      "container": "/w:document/w:body/w:p[121]",
      "target": "/w:document/w:body/w:p[121]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.3.5",
      "container": "/w:document/w:body/w:p[131]",
      "target": "/w:document/w:body/w:p[131]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.4.1",
      "container": "/w:document/w:body/w:p[147]",
      "target": "/w:document/w:body/w:p[147]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.4.1",
      "container": "/w:document/w:body/w:p[148]",
      "target": "/w:document/w:body/w:p[147]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.4.2",
      "container": "/w:document/w:body/w:p[166]",
      "target": "/w:document/w:body/w:p[167]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.4.2",
      "container": "/w:document/w:body/w:p[167]",
      "target": "/w:document/w:body/w:p[167]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.4.3",
      "container": "/w:document/w:body/w:p[181]",
      "target": "/w:document/w:body/w:p[181]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.4.4",
      "container": "/w:document/w:body/w:p[201]",
      "target": "/w:document/w:body/w:p[202]",
      "start": 282,
      "end": 292
    },
    {
      "label": "Bảng 2.4.4",
      "container": "/w:document/w:body/w:p[202]",
      "target": "/w:document/w:body/w:p[202]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.5.1",
      "container": "/w:document/w:body/w:p[251]",
      "target": "/w:document/w:body/w:p[252]",
      "start": 190,
      "end": 200
    },
    {
      "label": "Bảng 2.5.1",
      "container": "/w:document/w:body/w:p[252]",
      "target": "/w:document/w:body/w:p[252]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.5.2",
      "container": "/w:document/w:body/w:p[287]",
      "target": "/w:document/w:body/w:p[287]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.5.3",
      "container": "/w:document/w:body/w:p[323]",
      "target": "/w:document/w:body/w:p[323]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.5.4",
      "container": "/w:document/w:body/w:p[338]",
      "target": "/w:document/w:body/w:p[338]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.5.5",
      "container": "/w:document/w:body/w:p[364]",
      "target": "/w:document/w:body/w:p[365]",
      "start": 0,
      "end": 10
    },
    {
      "label": "Bảng 2.5.5",
      "container": "/w:document/w:body/w:p[365]",
      "target": "/w:document/w:body/w:p[365]",
      "start": 0,
      "end": 10
    }
  ],
  "equation_labels": [
    {
      "container": "/w:document/w:body/w:p[114]",
      "label": "(1)",
      "omml_text": "τmax(Q) = μp"
    },
    {
      "container": "/w:document/w:body/w:p[115]",
      "label": "(2)",
      "omml_text": "QJ = kμp"
    },
    {
      "container": "/w:document/w:body/w:p[116]",
      "label": "(3)",
      "omml_text": "QS = Aμp"
    },
    {
      "container": "/w:document/w:body/w:p[193]",
      "label": "",
      "omml_text": "Qout ≥ Qin"
    },
    {
      "container": "/w:document/w:body/w:p[227]",
      "label": "(2.5.1-1)",
      "omml_text": "Ft ≤ μs N"
    },
    {
      "container": "/w:document/w:body/w:p[230]",
      "label": "(2.5.1-2)",
      "omml_text": "tt(x) ≤ μs pn(x)"
    },
    {
      "container": "/w:document/w:body/w:p[243]",
      "label": "(2.5.1-3)",
      "omml_text": "τmax(Q) = μ p"
    },
    {
      "container": "/w:document/w:body/w:p[245]",
      "label": "(2.5.1-4)",
      "omml_text": "QJ = k μ p"
    },
    {
      "container": "/w:document/w:body/w:p[247]",
      "label": "(2.5.1-5)",
      "omml_text": "QS = A μ p"
    },
    {
      "container": "/w:document/w:body/w:p[268]",
      "label": "(2.5.2-1)",
      "omml_text": "Bind = i=1nEiIi,c"
    },
    {
      "container": "/w:document/w:body/w:p[270]",
      "label": "(2.5.2-2)",
      "omml_text": "Ii,c = π d4 / 64"
    },
    {
      "container": "/w:document/w:body/w:p[273]",
      "label": "(2.5.2-3)",
      "omml_text": "yNA = Σ Ei Ai yiΣ Ei Ai"
    },
    {
      "container": "/w:document/w:body/w:p[275]",
      "label": "(2.5.2-4)",
      "omml_text": "Bbond = i=1nEi[Ii,c + Ai(yi − yNA)²]"
    },
    {
      "container": "/w:document/w:body/w:p[295]",
      "label": "(2.5.3-1)",
      "omml_text": "M = Bκ"
    },
    {
      "container": "/w:document/w:body/w:p[298]",
      "label": "(2.5.3-2)",
      "omml_text": "Kt,M = dM/dκ"
    },
    {
      "container": "/w:document/w:body/w:p[300]",
      "label": "(2.5.3-3)",
      "omml_text": "Kt,F = dF/dδ"
    },
    {
      "container": "/w:document/w:body/w:p[303]",
      "label": "(2.5.3-4)",
      "omml_text": "Ksec = F₂ − F₁δ₂ − δ₁"
    },
    {
      "container": "/w:document/w:body/w:p[312]",
      "label": "(2.5.3-5)",
      "omml_text": "WF = ∮ F dδ ;  WT = ∮ T dθ"
    },
    {
      "container": "/w:document/w:body/w:p[315]",
      "label": "(2.5.3-6)",
      "omml_text": "WMκ = 0L∮ M(s) dκ(s) ds"
    }
  ],
  "original_records_mapped": 913,
  "trace_rows": 2859,
  "unresolved_anchors": 0,
  "source_content_manifest_rows": 2171,
  "unexplained_source_content_loss": 0,
  "unapproved_scientific_changes": 0,
  "scientific_claim_promotion": 0
}
```
```json
{
  "input_trace_records": 913,
  "original_records_mapped": 913,
  "output_trace_records": 2859,
  "record_kind_counts": {
    "SCIENTIFIC_CLAIM": 931,
    "STRUCTURAL_RECORD": 1923,
    "ARCHIVAL_SUPPORT_ONLY": 5
  },
  "anchor_granularity_counts": {
    "SOURCE_EXACT_ANCHOR": 637,
    "PARAGRAPH_OR_TABLE_SCOPE": 75,
    "TABLE_ROW_SCOPE": 48,
    "PARAGRAPH_SCOPE": 136,
    "ARCHIVAL_SUPPORT_ONLY": 5,
    "SUBSECTION_SCOPE": 9,
    "PARAGRAPH_OR_EQUATION_SCOPE": 95,
    "WHOLE_PARAGRAPH": 1852,
    "NEW_STRUCTURE": 2
  },
  "archival_support_only": [
    [
      4,
      "24-1-C13"
    ],
    [
      4,
      "24-4-C08"
    ],
    [
      4,
      "24-4-C09"
    ],
    [
      4,
      "24-4-C10"
    ],
    [
      4,
      "24-4-C11"
    ]
  ],
  "source_anchor_repairs": [],
  "unresolved_anchors": 0,
  "duplicate_claim_ids": 0,
  "input_terminology_records": 313,
  "output_terminology_records": 313,
  "scientific_definition_conflicts": 0,
  "terminology_alias_resolutions": 9
}
```


## Kiểm package sau xuất hotfix

Đã mở lại9 deliverable và1 phụ lục. Kết quả cuối ghi ở scratch và tóm tắt tại đây.

```json
{
  "status": "PASS",
  "branch": "main",
  "head": "e66bb2f2339006e763cd60687cfc24680b945d97",
  "all_preexisting_input_files_checked": 23407,
  "all_unchanged_outside_scope": true,
  "source_packages_unchanged": 42,
  "canonical_baselines_unchanged": 6,
  "protected_external_files_unchanged": 30,
  "wep_p3_registry_unchanged": true,
  "modified": [
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_7_GATE_REVIEW.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_EXECUTION_REPORT.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_FULL_INTEGRATED.docx",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_GLOBAL_CITATION_REFERENCE_MAP.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_INTEGRATION_CHANGELOG.md",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_SOURCE_TRACEABILITY.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_MASTER_TERMINOLOGY.csv",
    "outputs/thesis_drafts/chapter_2/chapter_2_integrated/MP1_CH2_UNRESOLVED_ISSUES.md"
  ],
  "created": [
    "outputs/thesis_drafts/chapter_2/appendix_terminology_staging/MP1_THESIS_TERMINOLOGY_APPENDIX_STAGING.docx"
  ],
  "tracked_and_cached_diff_unchanged": true,
  "git_status_added_paths": [
    "?? outputs/thesis_drafts/chapter_2/appendix_terminology_staging/MP1_THESIS_TERMINOLOGY_APPENDIX_STAGING.docx"
  ],
  "original_records": 913,
  "trace_rows": 2935,
  "terminology": 313,
  "citation_map_rows": 69,
  "object_crosswalk_rows": 86,
  "mandatory_execution_fields": 63,
  "nine_deliverables_reopened": true,
  "appendix_reopened": true,
  "no_qa_files_in_output_directories": true,
  "no_commit": true,
  "no_push": true,
  "independent_acceptance": "REQUIRED_NOT_PERFORMED"
}
```
