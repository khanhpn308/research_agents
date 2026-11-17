# Vấn đề hiện hành sau hotfix

TASK_ID: MP1-CH2-FULL-INTEGRATION-GATE1-HOTFIX

STATUS: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED

CH2-OUTLINE-01: RESOLVED trong SELF_REVIEW_ONLY; không đồng nghĩa independent acceptance. Các trạng thái cũ bên dưới được giữ riêng như lịch sử. Không đóng chính sách trường, RQ mapping hoặc năm quyết định khoa học.

## CH2-OOS-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-OOS-01 |
| SOURCE_SECTION | 2.3;2.5;2.6 |
| SOURCE_LOCATION | §2.3 [8]; §2.5 [3]; §2.6 [2]; chapter [19] |
| ISSUE_CATEGORY | BIBLIOGRAPHIC_CORRECTION |
| SEVERITY | CLOSED |
| DESCRIPTION | Khoảng trang Crowley 5477–5483 ở §2.3 mâu thuẫn 5477–5482 ở §2.6. Đã thống nhất 5477–5482 chỉ trong bản toàn chương. |
| EVIDENCE | PDF M11 trang vật lý1/in5477 và6/in5482, SHA cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827; SOURCE_REGISTRY.json::records[10]; WEP crosswalk paper_id=M11. |
| IMPACT_ON_CHAPTER | Không còn hai metadata tranh chấp trong reference cuối. |
| PROPOSED_ACTION | Đã sửa chapter [19], giữ nguyên baseline và finding lịch sử. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | RESOLVED_IN_CHAPTER_ONLY |
| DISPOSITION_CLASS | RESOLVED |

## CH2-OUTLINE-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-OUTLINE-01 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Bullets 2.1.3.3, 2.3.3.2, 2.5.3.2; năm bảng thuật ngữ kế thừa |
| ISSUE_CATEGORY | OUTLINE_CONFLICT / HUMAN_DECISION_PENDING |
| SEVERITY | RESOLVED_P2 |
| DESCRIPTION | Bốn patch đúng nội dung duyệt; ba bullet được bao phủ53/12 tổng thể;17 nhóm có synthesis cuối phần lập luận; năm glossary và10 lead-in/caption chuyển nguyên vẹn sang staging. |
| EVIDENCE | 913/913 record;5792 neo exact;783/783 citation;976 cell C14N exact;73+32 trang được xem; Gate1–7 tự kiểm. |
| IMPACT_ON_CHAPTER | Đóng findingP2 trong tự kiểm; không cấp independent acceptance. |
| PROPOSED_ACTION | Chờ người nghiệm thu độc lập kiểm toàn chương và phụ lục, gồm cách hiểu vị trí synthesis trước bảng hỗ trợ. |
| HUMAN_DECISION_REQUIRED | INDEPENDENT_ACCEPTANCE_REQUIRED |
| BLOCKS_INDEPENDENT_ACCEPTANCE | PENDING_INDEPENDENT_REVIEW; NO_REMAINING_P2_SELF_REVIEW |
| STATUS | RESOLVED |
| DISPOSITION_CLASS | RESOLVED_IN_SELF_REVIEW_ONLY |

## CH2-LIM-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-01 |
| SOURCE_SECTION | 2.1.4 |
| SOURCE_LOCATION | Dàn ý bullet2.1.4.2 |
| ISSUE_CATEGORY | SCHOOL_CITATION_POLICY |
| SEVERITY | P3 |
| DESCRIPTION | IEEE theo AUTHOR_APPROVED_STYLE_DECISION; quy định trường/niên khóa chưa được xác minh. |
| EVIDENCE | Baseline §2.1.4 và quyết định của tác giả trong nhiệm vụ. |
| IMPACT_ON_CHAPTER | Không gọi IEEE là chuẩn bắt buộc của HCMUT. |
| PROPOSED_ACTION | Kiểm quy định trường trước tích hợp toàn luận văn. |
| HUMAN_DECISION_REQUIRED | YES_LATER |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-02

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-02 |
| SOURCE_SECTION | 2.1;2.6 |
| SOURCE_LOCATION | RQ1–RQ5 đối chiếu P3 |
| ISSUE_CATEGORY | RQ_MAPPING |
| SEVERITY | P3 |
| DESCRIPTION | Ánh xạ vẫn PROVISIONAL_MANY_TO_MANY; năm RQ của dàn ý và nhóm P3 không được tự coi đồng nhất. |
| EVIDENCE | P3_RESEARCH_QUESTIONS.md; source baseline §§2.1/2.6. |
| IMPACT_ON_CHAPTER | Không cấp phê duyệt RQ. |
| PROPOSED_ACTION | Tác giả khóa ánh xạ trước protocol cuối. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD1

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD1 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Contact topology |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Giao diện dây–dây, dây–ống bao hoặc mạng kết hợp và mặt phản lực chưa khóa. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD2

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD2 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Pressure-to-normal-load transfer |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Áp suất nguồn/gần mẫu chưa là luật lực pháp tuyến cục bộ; đại lượng đại diện cần chứng cứ. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD3

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD3 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | TiNi thermal/phase/history domain |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Miền pha, nhiệt độ, tốc độ và lịch sử TiNi chịu tải chưa được chốt. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD4

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD4 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Stiffness metric and uncertainty |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Metric độ cứng, mô hình đo, bất định và ngưỡng phân biệt cần tác giả phê duyệt. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD5

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD5 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | SMA–piston and Bench B scope |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Đặc trưng nguồn và vai trò BenchB còn mở; chưa có performance hoặc tương đương BenchA. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-LIM-03

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-03 |
| SOURCE_SECTION | 2.1;2.2;2.4–2.6 |
| SOURCE_LOCATION | Các locator/version notes trong original_record_json |
| ISSUE_CATEGORY | INHERITED_SOURCE_BOUNDARY |
| SEVERITY | P3 |
| DESCRIPTION | Giữ M01 locator không dùng để hỗ trợ claim; chênh locator M03-E02/M23-E06; không tự tái gán M38-E04; năm online/issue của M20/M23/M24/M36 giữ phân biệt; giới hạn đơn vị k_i/M23 và phạm vi phương trình P3 không được nâng cấp. |
| EVIDENCE | Source packages, source CSV JSON nguyên trạng, P3_DECISION_REPORT và P3_GAP_ADJUDICATION. |
| IMPACT_ON_CHAPTER | Vòng tích hợp không tái thẩm định toàn văn toàn bộ luận cứ hoặc sửa phương trình nguồn. |
| PROPOSED_ACTION | Rà đúng nguồn sơ cấp khi tác giả cần dùng ngoài miền đã chấp nhận; giữ locator tranh chấp là giới hạn. |
| HUMAN_DECISION_REQUIRED | AS_NEEDED |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_IF_BOUNDARY_PRESERVED |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-04

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-04 |
| SOURCE_SECTION | 2.3;2.4 |
| SOURCE_LOCATION | Bảng A.1; Bảng A.2; các nhãn Hình/Bảng2.x |
| ISSUE_CATEGORY | CAPTION_POLICY |
| SEVERITY | P3 |
| DESCRIPTION | Không có nhãn trùng hoặc đích Hình/Bảng2.x bị thiếu; nhãn A.1/A.2 và numbering phương trình theo mục giữ từ baseline vì chính sách chưa khóa. |
| EVIDENCE | 19 caption; 25 lần xuất hiện nhãn có đích, trong đó 8 lần ngoài paragraph caption. 19 OMML giữ nguyên. |
| IMPACT_ON_CHAPTER | Chưa tự đổi sang một chính sách số Hình/Bảng/Phương trình mới. |
| PROPOSED_ACTION | Tác giả quyết định numbering đồng bộ khi tích hợp toàn luận văn; gắn với CH2-OUTLINE-01. |
| HUMAN_DECISION_REQUIRED | YES_LATER |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_BLOCKER |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-05

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-05 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | 73 trang chapter và32 trang appendix |
| ISSUE_CATEGORY | MICROSOFT_WORD_VALIDATION |
| SEVERITY | P3 |
| DESCRIPTION | Chỉ kiểm LibreOffice24.2.7.2 với Math; MicrosoftWord chưa được chạy. |
| EVIDENCE | Kết xuất LibreOffice mới,105 trang được xem; Microsoft Word chưa chạy. |
| IMPACT_ON_CHAPTER | Không tuyên bố MicrosoftWord PASS. |
| PROPOSED_ACTION | Người nghiệm thu mở DOCX trong MicrosoftWord để rà bản ứng dụng native. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_BLOCKER |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-06

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-06 |
| SOURCE_SECTION | 2.3–2.5 |
| SOURCE_LOCATION | Bản ghi neo theo đoạn/tiểu mục;5archive-only |
| ISSUE_CATEGORY | TRACE_GRANULARITY |
| SEVERITY | P3 |
| DESCRIPTION | Một số source packages chỉ có locator cấp đoạn/tiểu mục hoặc hồ sơ hỗ trợ, không có neo câu nguyên văn. Đã lập container/offset thật cho bản toàn chương và phân loại rõ mức chi tiết; không giả tạo neo câu. |
| EVIDENCE | 913/913 record;2935 trace row;5792 neo;0 gap trong cả hai đích;5 archive-only giữ riêng. |
| IMPACT_ON_CHAPTER | 100% account-for-record không đồng nghĩa mọi claim đã tái xác minh tới một câu PDF sơ cấp. |
| PROPOSED_ACTION | Dùng exact final anchors để tái kiểm; chỉ tăng độ chi tiết sau khi có source evidence phù hợp. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-07

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-07 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | Các bảng thuật ngữ và nhãn phụ |
| ISSUE_CATEGORY | STYLE_AND_LENGTH |
| SEVERITY | P3 |
| DESCRIPTION | Các bảng thuật ngữ đã ra phụ lục. Style/cỡ chữ và khoảng trắng kế thừa còn đọc được, được ghi riêng sau kết xuất mới. |
| EVIDENCE | Chương73 trang; phụ lục32 trang; ROOT và worker tự kiểm từng trang; findingP3 trang39/47. |
| IMPACT_ON_CHAPTER | Bản toàn chương dài101trang; vị trí/khối lượng thuật ngữ cần quyết định biên tập. |
| PROPOSED_ACTION | Cân nhắc đồng bộ style trong lần dàn trang được duyệt; không rút gọn dữ liệu để sửa bố cục. |
| HUMAN_DECISION_REQUIRED | YES_LATER |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_BLOCKER |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-RENDER-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-RENDER-01 |
| SOURCE_SECTION | 2.3–2.5 |
| SOURCE_LOCATION | Các bản render đầu trong scratch |
| ISSUE_CATEGORY | QA_RENDERER_CONFIGURATION |
| SEVERITY | CLOSED |
| DESCRIPTION | Render đầu không hiện OMML do thiếu libreoffice-math. Bổ sung module trong runtime tạm, dựng lại; không chuyển công thức thành ảnh/plaintext hoặc sửa biểu thức. |
| EVIDENCE | 19OMML exactcanonical; renderMath và visualreviewcuối. |
| IMPACT_ON_CHAPTER | Finding cũ không còn trên bản raster cuối. |
| PROPOSED_ACTION | Đã xử lý; giữ lịch sử QA trong scratch. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | RESOLVED |
| DISPOSITION_CLASS | RESOLVED |

## CH2-LIM-08

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-08 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | Scratch runtime LibreOffice |
| ISSUE_CATEGORY | RESTORATION_RUNTIME |
| SEVERITY | P3 |
| DESCRIPTION | Runtime bản sao trong scratch đã hoạt động cùng Math sau sửa đường dẫn và8 symlink; runtime checkpoint gốc không bị sửa. |
| EVIDENCE | Kết xuất mới73+32 trang; render-manifest.json; runtime-symlinks.json. |
| IMPACT_ON_CHAPTER | Không ảnh hưởng việc đóng gói artifact bất biến. Nếu cần render bản sửa, phải kiểm hoặc phục hồi môi trường kết xuất trước. |
| PROPOSED_ACTION | Giữ runtime scratch làm provenance; không ghi ngược vào checkpoint. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | RESOLVED_FOR_HOTFIX_RUNTIME |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-09

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-09 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv::visual_review_status |
| ISSUE_CATEGORY | INHERITED_SIDECAR_STATUS |
| SEVERITY | P3 |
| DESCRIPTION | 85 row cũ giữ pre_hotfix_visual_review_status;86 row hiện hành có post_hotfix_visual_review_status và chứng cứ kết xuất mới. |
| EVIDENCE | 86 row gồm85 row cũ+1 cross-reference củaFAILURE-233; visual-reviewed-final.json. |
| IMPACT_ON_CHAPTER | CSV là snapshot trước review, không phải trạng thái QA mới nhất. Báo cáo 7 gate liên kết chứng cứ review đến sau; không nâng ngầm trường CSV. |
| PROPOSED_ACTION | Dùng trường trước/sau riêng; không coi QA cũ là QA mới. |
| HUMAN_DECISION_REQUIRED | YES_IF_CSV_STATUS_UPDATE_REQUESTED |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_WITH_EXPLICIT_REPORT_RECONCILIATION |
| STATUS | RESOLVED_IN_HOTFIX |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-HF-QA-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HF-QA-01 |
| SOURCE_SECTION | 2.4.4 |
| SOURCE_LOCATION | CHAPTER_DOCX trang39 |
| ISSUE_CATEGORY | INHERITED_LAYOUT |
| SEVERITY | P3 |
| DESCRIPTION | Khoảng trắng lớn ở cuối§2.4.4. |
| EVIDENCE | ROOT xác nhận do blank paragraph pre-hotfix p218 có pageBreakBefore kế thừa. Không thêm page break; nội dung và định dạng baseline được giữ. Không clipping hoặc mất luận cứ. |
| IMPACT_ON_CHAPTER | Không mất nội dung; bảng/đoạn đọc được. |
| PROPOSED_ACTION | Giữ nguyên trong hotfix; nghiệm thu độc lập cân nhắc dàn trang sau. |
| HUMAN_DECISION_REQUIRED | NO_FOR_CURRENT_HOTFIX |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_P2 |
| STATUS | OPEN_DOCUMENTED_LIMITATION |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-HF-QA-02

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HF-QA-02 |
| SOURCE_SECTION | 2.5.2 |
| SOURCE_LOCATION | CHAPTER_DOCX trang47 |
| ISSUE_CATEGORY | INHERITED_LAYOUT |
| SEVERITY | P3 |
| DESCRIPTION | Cỡ chữ một số ô Bảng2.5.2 không đồng đều. |
| EVIDENCE | ROOT xác nhận bảng đọc được, không cắt ô. XML bảng khớp baseline nguyên vẹn; chuẩn hóa style nằm ngoài bốn patch được duyệt. |
| IMPACT_ON_CHAPTER | Không mất nội dung; bảng/đoạn đọc được. |
| PROPOSED_ACTION | Giữ nguyên trong hotfix; nghiệm thu độc lập cân nhắc dàn trang sau. |
| HUMAN_DECISION_REQUIRED | NO_FOR_CURRENT_HOTFIX |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_P2 |
| STATUS | OPEN_DOCUMENTED_LIMITATION |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## Giới hạn hiện hành

- Microsoft Word chưa được chạy; MICROSOFT_WORD_VALIDATION=NOT_VERIFIED. LibreOffice24.2.7.2 với Math là công cụ kết xuất.
- Bốn nhóm§2.3.1/2.3.2/2.3.4/2.3.5 có đoạn tổng hợp cuối phần lập luận và bảng hỗ trợ theo sau. Root phân xử đủ nội dung; cách hiểu vị trí được ghi rõ để nghiệm thu độc lập. Không lấy caption hoặc bảng thay paragraph.
- Chỉ tự kiểm. Trạng thái VERIFIED FULL TEXT/METADATA ONLY của nguồn được kế thừa theo lineage, không phải tuyên bố tái đọc toàn bộ PDF. Bốn claim mới là AUTHOR_METHOD_SYNTHESIS và INFERENCE/PROPOSAL.
- Chính sách trích dẫn của trường, ánh xạ RQ tạm thời và năm quyết định khoa học vẫn mở. H0b chưa bị bác bỏ, H1 chưa đủ bằng chứng.
- Mười bốn record thuật ngữ§2.1 chỉ có mapping cấp phạm vi§2.1; định nghĩa nguyên gốc vẫn nằm trong original_record_json. Không tạo bảng thuật ngữ giả hoặc neo một câu không tồn tại.
- Khoảng trắng kế thừa ở trang39 và cỡ chữ chưa đều trong Bảng2.5.2 trang47 vẫn được ghi làP3. Các đối tượng không bị cắt; không sửa style ngoài phạm vi hotfix.
- Nhãn A.1/A.2 và ghi chú nguồn được giữ nguyên trong staging như lịch sử; chưa gán số phụ lục chính thức. Chỉ mục nguồn bổ sung30 lượt dẫn cấu trúc, không bổ sung nguồn khoa học.
- Backend không cung cấp chứng cứ xác minh model thực tế. Cấu hình lời gọi worker được ghi nhận: gpt-6-sol/medium ×1, gpt-6-luna/medium ×2; đây không phải xác nhận backend. Root được yêu cầu GPT-6.1 Sol High, không suy model thực tế từ yêu cầu.

## Đăng ký trước hotfix, giữ nguyên lịch sử

Mọi trạng tháiOPEN/PENDING của hồ sơ bên dưới chỉ là lịch sử trước hotfix. Dùng bảng hiện hành phía trên để đọc trạng thái mới.

# Đăng ký vấn đề và giới hạn của bản tích hợp Chương 2

TASK_ID: MP1-CH2-FULL-CHAPTER-INTEGRATION

STATUS: PARTIAL_WITH_FINDINGS

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE: REQUIRED_NOT_PERFORMED

EXECUTION_PLAN_APPROVAL: APPROVED

CONTENT_PATCH_APPROVAL: PENDING

## Quy tắc phân loại

CH2-OUTLINE-01 là một blocker P2 bao gồm ba coverage gap và vị trí bảng thuật ngữ. Các thành phần được tách rõ trong đề xuất sửa. Năm quyết định khoa học giữ mở; RQ mapping vẫn tạm thời. Các giới hạn này không tự động là lỗi ngăn bàn giao bản tổng quan.

## CH2-OOS-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-OOS-01 |
| SOURCE_SECTION | 2.3;2.5;2.6 |
| SOURCE_LOCATION | §2.3 [8]; §2.5 [3]; §2.6 [2]; chapter [19] |
| ISSUE_CATEGORY | BIBLIOGRAPHIC_CORRECTION |
| SEVERITY | CLOSED |
| DESCRIPTION | Khoảng trang Crowley 5477–5483 ở §2.3 mâu thuẫn 5477–5482 ở §2.6. Đã thống nhất 5477–5482 chỉ trong bản toàn chương. |
| EVIDENCE | PDF M11 trang vật lý1/in5477 và6/in5482, SHA cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827; SOURCE_REGISTRY.json::records[10]; WEP crosswalk paper_id=M11. |
| IMPACT_ON_CHAPTER | Không còn hai metadata tranh chấp trong reference cuối. |
| PROPOSED_ACTION | Đã sửa chapter [19], giữ nguyên baseline và finding lịch sử. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | RESOLVED_IN_CHAPTER_ONLY |
| DISPOSITION_CLASS | RESOLVED |

## CH2-OUTLINE-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-OUTLINE-01 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Bullets 2.1.3.3, 2.3.3.2, 2.5.3.2; năm bảng thuật ngữ kế thừa |
| ISSUE_CATEGORY | OUTLINE_CONFLICT / HUMAN_DECISION_PENDING |
| SEVERITY | P2 |
| DESCRIPTION | Ba bullet chưa được diễn đạt đầy đủ theo vị trí/cách tổ chức của dàn ý: tổng hợp cuối mọi nhóm; đối chiếu failure mode có hệ thống; nối từng metric với toàn bộ điều kiện đo. Các bảng/nhãn phụ lục thuật ngữ của baseline còn trong chương, nhưng PDF không xác nhận vị trí này. |
| EVIDENCE | 65 bullet: 52 COVERED, 10 COVERED_WITH_BOUNDARY, 3 PARTIAL_EDITORIAL. Xem crosswalk trong báo cáo 7 gate. |
| IMPACT_ON_CHAPTER | Không được tự nhận tuân thủ hoàn toàn dàn ý hoặc đóng Gate1. Không có mất claim nguồn. |
| PROPOSED_ACTION | Xem COVERAGE_PATCH_PROPOSAL.md trong scratch. Bảng 2.3.3 đã có cột chuyển tiếp/giới hạn; cần phân xử mức bao phủ thực tế, không tự bổ sung failure mode. |
| HUMAN_DECISION_REQUIRED | YES_EDITORIAL |
| BLOCKS_INDEPENDENT_ACCEPTANCE | YES |
| STATUS | OPEN |
| DISPOSITION_CLASS | ACCEPTANCE_BLOCKER |

## CH2-LIM-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-01 |
| SOURCE_SECTION | 2.1.4 |
| SOURCE_LOCATION | Dàn ý bullet2.1.4.2 |
| ISSUE_CATEGORY | SCHOOL_CITATION_POLICY |
| SEVERITY | P3 |
| DESCRIPTION | IEEE theo AUTHOR_APPROVED_STYLE_DECISION; quy định trường/niên khóa chưa được xác minh. |
| EVIDENCE | Baseline §2.1.4 và quyết định của tác giả trong nhiệm vụ. |
| IMPACT_ON_CHAPTER | Không gọi IEEE là chuẩn bắt buộc của HCMUT. |
| PROPOSED_ACTION | Kiểm quy định trường trước tích hợp toàn luận văn. |
| HUMAN_DECISION_REQUIRED | YES_LATER |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-02

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-02 |
| SOURCE_SECTION | 2.1;2.6 |
| SOURCE_LOCATION | RQ1–RQ5 đối chiếu P3 |
| ISSUE_CATEGORY | RQ_MAPPING |
| SEVERITY | P3 |
| DESCRIPTION | Ánh xạ vẫn PROVISIONAL_MANY_TO_MANY; năm RQ của dàn ý và nhóm P3 không được tự coi đồng nhất. |
| EVIDENCE | P3_RESEARCH_QUESTIONS.md; source baseline §§2.1/2.6. |
| IMPACT_ON_CHAPTER | Không cấp phê duyệt RQ. |
| PROPOSED_ACTION | Tác giả khóa ánh xạ trước protocol cuối. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD1

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD1 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Contact topology |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Giao diện dây–dây, dây–ống bao hoặc mạng kết hợp và mặt phản lực chưa khóa. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD2

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD2 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Pressure-to-normal-load transfer |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Áp suất nguồn/gần mẫu chưa là luật lực pháp tuyến cục bộ; đại lượng đại diện cần chứng cứ. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD3

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD3 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | TiNi thermal/phase/history domain |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Miền pha, nhiệt độ, tốc độ và lịch sử TiNi chịu tải chưa được chốt. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD4

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD4 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | Stiffness metric and uncertainty |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Metric độ cứng, mô hình đo, bất định và ngưỡng phân biệt cần tác giả phê duyệt. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-HD5

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-HD5 |
| SOURCE_SECTION | 2.1–2.6 |
| SOURCE_LOCATION | SMA–piston and Bench B scope |
| ISSUE_CATEGORY | SCIENTIFIC_HUMAN_DECISION |
| SEVERITY | P3 |
| DESCRIPTION | Đặc trưng nguồn và vai trò BenchB còn mở; chưa có performance hoặc tương đương BenchA. |
| EVIDENCE | P3 canonical và nội dung baseline đã bảo toàn. |
| IMPACT_ON_CHAPTER | Không ngăn bàn giao bản thảo tổng quan nếu diễn đạt có điều kiện; ngăn khóa nghiên cứu/thực nghiệm tương ứng. |
| PROPOSED_ACTION | Giữ mở; không tự quyết trong lần tích hợp. |
| HUMAN_DECISION_REQUIRED | YES |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_FOR_THIS_DRAFT |
| STATUS | OPEN |
| DISPOSITION_CLASS | FUTURE_RESEARCH_DECISION |

## CH2-LIM-03

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-03 |
| SOURCE_SECTION | 2.1;2.2;2.4–2.6 |
| SOURCE_LOCATION | Các locator/version notes trong original_record_json |
| ISSUE_CATEGORY | INHERITED_SOURCE_BOUNDARY |
| SEVERITY | P3 |
| DESCRIPTION | Giữ M01 locator không dùng để hỗ trợ claim; chênh locator M03-E02/M23-E06; không tự tái gán M38-E04; năm online/issue của M20/M23/M24/M36 giữ phân biệt; giới hạn đơn vị k_i/M23 và phạm vi phương trình P3 không được nâng cấp. |
| EVIDENCE | Source packages, source CSV JSON nguyên trạng, P3_DECISION_REPORT và P3_GAP_ADJUDICATION. |
| IMPACT_ON_CHAPTER | Vòng tích hợp không tái thẩm định toàn văn toàn bộ luận cứ hoặc sửa phương trình nguồn. |
| PROPOSED_ACTION | Rà đúng nguồn sơ cấp khi tác giả cần dùng ngoài miền đã chấp nhận; giữ locator tranh chấp là giới hạn. |
| HUMAN_DECISION_REQUIRED | AS_NEEDED |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_IF_BOUNDARY_PRESERVED |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-04

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-04 |
| SOURCE_SECTION | 2.3;2.4 |
| SOURCE_LOCATION | Bảng A.1; Bảng A.2; các nhãn Hình/Bảng2.x |
| ISSUE_CATEGORY | CAPTION_POLICY |
| SEVERITY | P3 |
| DESCRIPTION | Không có nhãn trùng hoặc đích Hình/Bảng2.x bị thiếu; nhãn A.1/A.2 và numbering phương trình theo mục giữ từ baseline vì chính sách chưa khóa. |
| EVIDENCE | 19 caption; 25 lần xuất hiện nhãn có đích, trong đó 8 lần ngoài paragraph caption. 19 OMML giữ nguyên. |
| IMPACT_ON_CHAPTER | Chưa tự đổi sang một chính sách số Hình/Bảng/Phương trình mới. |
| PROPOSED_ACTION | Tác giả quyết định numbering đồng bộ khi tích hợp toàn luận văn; gắn với CH2-OUTLINE-01. |
| HUMAN_DECISION_REQUIRED | YES_LATER |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_BLOCKER |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-05

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-05 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | 101trang PDF QA |
| ISSUE_CATEGORY | MICROSOFT_WORD_VALIDATION |
| SEVERITY | P3 |
| DESCRIPTION | Chỉ kiểm LibreOffice24.2.7.2 với Math; MicrosoftWord chưa được chạy. |
| EVIDENCE | Review cũ đủ 101 trang; kiểm hash lại trong phiên tiếp tục. Microsoft Word chưa được chạy. |
| IMPACT_ON_CHAPTER | Không tuyên bố MicrosoftWord PASS. |
| PROPOSED_ACTION | Người nghiệm thu mở DOCX trong MicrosoftWord để rà bản ứng dụng native. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_BLOCKER |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-06

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-06 |
| SOURCE_SECTION | 2.3–2.5 |
| SOURCE_LOCATION | Bản ghi neo theo đoạn/tiểu mục;5archive-only |
| ISSUE_CATEGORY | TRACE_GRANULARITY |
| SEVERITY | P3 |
| DESCRIPTION | Một số source packages chỉ có locator cấp đoạn/tiểu mục hoặc hồ sơ hỗ trợ, không có neo câu nguyên văn. Đã lập container/offset thật cho bản toàn chương và phân loại rõ mức chi tiết; không giả tạo neo câu. |
| EVIDENCE | Đối chiếu tập record thực tế 913/913; 2.859 trace row; 5.716 neo nguồn/đích; coverage văn bản không thiếu ký tự. Năm record archive-only giữ riêng. |
| IMPACT_ON_CHAPTER | 100% account-for-record không đồng nghĩa mọi claim đã tái xác minh tới một câu PDF sơ cấp. |
| PROPOSED_ACTION | Dùng exact final anchors để tái kiểm; chỉ tăng độ chi tiết sau khi có source evidence phù hợp. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-07

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-07 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | Các bảng thuật ngữ và nhãn phụ |
| ISSUE_CATEGORY | STYLE_AND_LENGTH |
| SEVERITY | P3 |
| DESCRIPTION | Một số nhãn phụ/caption giữ màu hoặc cỡ chữ baseline; bảng thuật ngữ dài. Không thấy clipping hoặc công thức mất trong render cuối. |
| EVIDENCE | Review 101 trang kế thừa. Cấp điều hướng của 33 nhãn phụ đã được lưu trong build_state, không đồng nghĩa vị trí đã được tác giả duyệt. |
| IMPACT_ON_CHAPTER | Bản toàn chương dài101trang; vị trí/khối lượng thuật ngữ cần quyết định biên tập. |
| PROPOSED_ACTION | Xử lý cùng CH2-OUTLINE-01; không xóa claim hoặc định nghĩa để làm ngắn. |
| HUMAN_DECISION_REQUIRED | YES_LATER |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_SEPARATE_BLOCKER |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-RENDER-01

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-RENDER-01 |
| SOURCE_SECTION | 2.3–2.5 |
| SOURCE_LOCATION | Các bản render đầu trong scratch |
| ISSUE_CATEGORY | QA_RENDERER_CONFIGURATION |
| SEVERITY | CLOSED |
| DESCRIPTION | Render đầu không hiện OMML do thiếu libreoffice-math. Bổ sung module trong runtime tạm, dựng lại; không chuyển công thức thành ảnh/plaintext hoặc sửa biểu thức. |
| EVIDENCE | 19OMML exactcanonical; renderMath và visualreviewcuối. |
| IMPACT_ON_CHAPTER | Finding cũ không còn trên bản raster cuối. |
| PROPOSED_ACTION | Đã xử lý; giữ lịch sử QA trong scratch. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | RESOLVED |
| DISPOSITION_CLASS | RESOLVED |

## CH2-LIM-08

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-08 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | Scratch runtime LibreOffice |
| ISSUE_CATEGORY | RESTORATION_RUNTIME |
| SEVERITY | P3 |
| DESCRIPTION | Checkpoint chứa 10 symlink runtime đã mất đích. Bản làm việc giữ nguyên literal target; runtime phục hồi chưa được xác minh chạy được. |
| EVIDENCE | resume_manifest.json::dangling_runtime_symlinks; PDF và 101 PNG có hash khớp. |
| IMPACT_ON_CHAPTER | Không ảnh hưởng việc đóng gói artifact bất biến. Nếu cần render bản sửa, phải kiểm hoặc phục hồi môi trường kết xuất trước. |
| PROPOSED_ACTION | Chỉ khắc phục runtime khi có bản DOCX được phép sửa và cần render. |
| HUMAN_DECISION_REQUIRED | NO |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## CH2-LIM-09

| Trường | Giá trị |
|---|---|
| ISSUE_ID | CH2-LIM-09 |
| SOURCE_SECTION | Toàn chương |
| SOURCE_LOCATION | MP1_CH2_FIGURE_TABLE_EQUATION_CROSSWALK.csv::visual_review_status |
| ISSUE_CATEGORY | INHERITED_SIDECAR_STATUS |
| SEVERITY | P3 |
| DESCRIPTION | 85 row của crosswalk CSV vẫn ghi PENDING_FINAL_RENDER_REVIEW vì CSV được tạo trước review cuối. Phạm vi được duyệt yêu cầu giữ nguyên CSV. |
| EVIDENCE | Kiểm trực tiếp 85 row; hồ sơ review kế thừa đủ 101 trang và hash khớp. |
| IMPACT_ON_CHAPTER | CSV là snapshot trước review, không phải trạng thái QA mới nhất. Báo cáo 7 gate liên kết chứng cứ review đến sau; không nâng ngầm trường CSV. |
| PROPOSED_ACTION | Nếu cần đồng bộ trường CSV, xin duyệt riêng thao tác cập nhật trạng thái và giữ lineage gốc. Hiện dùng báo cáo 7 gate để đọc trạng thái QA. |
| HUMAN_DECISION_REQUIRED | YES_IF_CSV_STATUS_UPDATE_REQUESTED |
| BLOCKS_INDEPENDENT_ACCEPTANCE | NO_WITH_EXPLICIT_REPORT_RECONCILIATION |
| STATUS | OPEN |
| DISPOSITION_CLASS | DOCUMENTED_LIMITATION |

## Trạng thái bằng chứng

VERIFIED FULL TEXT là trạng thái nguồn được kế thừa, không phải chứng nhận tái đọc toàn bộ PDF trong phiên tiếp tục. METADATA ONLY giữ nguyên mức bằng chứng. INFERENCE và PROPOSAL tiếp tục là suy luận và đề xuất. Kiểm mới trong phiên này gồm đối chiếu record nguồn, XPath/offset, coverage văn bản, OOXML, citation và hash. Hồ sơ thị giác là review của phiên trước, được liên kết bằng hash với DOCX/PDF hiện tại. Không xem lại 101 ảnh trong phiên này.

