# Tự rà soát bảy cổng: §2.1.3

Đây là SELF_REVIEW_ONLY. ROOT đã kiểm lại các sửa đổi; hai nghiệm thu độc lập chưa thực hiện. Chi tiết manifest và phân xử C01–C12 ở báo cáo thực hiện.

## Gate 1. Outline và phạm vi

STATUS: PASS
METHOD: Đọc outline canonical trang vật lý 10/22, đối chiếu heading và ba bullet B01–B03 với DOCX cuối.
EVIDENCE: Heading đúng §2.1.3; B01 là chín phương diện, B02 là nhóm theo câu hỏi/cơ chế với thời gian ở trong nhóm, B03 là đoạn tổng hợp cuối nhóm.
COUNTS: 1 heading; 3/3 bullet; 7 đoạn thân luận văn; 1 bảng native.
FINDINGS: Không viết §2.1.4 và không tích hợp §2.1.
SEVERITY: LOW
UNRESOLVED: Không có lệch outline trong phạm vi này.
FINAL_DECISION: PASS

## Gate 2. Trung thực phương pháp

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Phân biệt bản ghi lịch sử với quy tắc nhóm đề xuất trong từng đoạn Word và trace.
EVIDENCE: P2 gọi chín phương diện là khung đối chiếu; P6 quy định cách ghi khi ranh giới hiệu chỉnh–kiểm chứng chưa rõ; P7 giữ cấu hình TiNi ở trạng thái dự kiến.
COUNTS: 7 đoạn luận văn; 0 tuyên bố mọi nguồn đã đủ chín trường; 3 locator M01 còn tranh chấp và không trích dẫn trong Word.
FINDINGS: CR-01/CR-02 và B01/B02 đã sửa, ROOT kiểm lại. Không suy số dòng là số nghiên cứu.
SEVERITY: MODERATE
UNRESOLVED: Không có hồ sơ cho thấy đã trích đủ chín phương diện ở từng nguồn.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Gate 3. Dữ liệu, nguồn và anchor

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Mở DOCX cuối, giải 40 XPath và kiểm Unicode offsets; kiểm SHA-256 nguồn chính/phụ trong trace và trạng thái ZIP/XML.
EVIDENCE: 40/40 anchor đúng container; 29 bản ghi có nguồn phụ và hash đúng; 3 tệp nguồn chính khác nhau, 5 tệp nguồn phụ khác nhau. ROOT xác nhận ZIP CRC và 16 XML parts.
COUNTS: 40 claim records; 29 secondary provenance records; 0 nội dung thân Word ngoài anchor; 75 Evidence IDs trong 123 WEP source-bound rows.
FINDINGS: M22 là một identity nhưng bản local P0/Pilot có DOI cụt; bản writing-workspace và WEP có DOI đầy đủ. Không sửa nguồn.
SEVERITY: MODERATE
UNRESOLVED: M01-E01/E02/E03 và M03-E02 còn vấn đề locator nguồn; không dùng làm bằng chứng kết quả cơ học.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Gate 4. Nhất quán khoa học và chương

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Đọc P3 sáu tệp và các baseline §2.1.1, §§2.2–2.6; kiểm đại diện các đoạn tổng hợp ở §2.3–2.6.
EVIDENCE: Bảng kiểm trong execution report nêu vị trí đoạn, thống nhất, khác biệt, không so sánh trực tiếp và hệ quả MP1. G00 đã đóng như gap chung; H0b vẫn là đối chứng.
COUNTS: 4 nhóm đoạn tổng hợp đại diện; 5 câu hỏi trong outline đối với 4 nhóm P3; 5 quyết định con người còn mở.
FINDINGS: Không suy áp suất nguồn bằng tải pháp tuyến cục bộ; không chuyển độ cứng của lớp/hạt sang bó dây TiNi.
SEVERITY: MODERATE
UNRESOLVED: Ghép RQ là PROVISIONAL_MANY_TO_MANY/HUMAN_DECISION_PENDING; chưa kiểm toán toàn bộ nhóm.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Gate 5. Ma trận chín trường và nhóm

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Đọc WEP02 CSV và WP JSONL, đối chiếu trường và định danh DOI; giữ riêng hạn chế schema với giá trị NOT_REPORTED.
EVIDENCE: Bảng Word nêu 9/9 phương diện; execution report có ánh xạ từng trường. WEP02 có 126 argument rows, 123 source-bound, 32 Paper IDs và 75 Evidence IDs; registry có 39 Paper IDs.
COUNTS: 29 DOI chuẩn ở WEP, 0 DOI trong bibliography; 59/123 hàng nguồn ghi model_assumptions NOT_REPORTED, 19/123 ghi context NOT_REPORTED; 0 paper được xác nhận đủ chín trường từ schema; số đủ thực tế chưa xác định.
FINDINGS: Không nhận MATRIX_COMPLETE hoặc lấy số dòng làm số bài. B02/B03 thể hiện quy tắc nhóm; kiểm đại diện bốn nhóm của baseline và giữ trạng thái chưa kiểm toàn bộ.
SEVERITY: MODERATE
UNRESOLVED: Độ phủ chín trường theo từng bài NOT_DETERMINABLE_FROM_SCHEMA_ALONE.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Gate 6. Viết, trích dẫn và kết xuất Word

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Kiểm DOCX A4, Times New Roman 12, giãn dòng 1,15, lề 3/2/2,5/2,5 cm, heading thật và bảng native có hàng đầu lặp; kết xuất bằng LibreOffice 24.2.7.2, xem toàn bộ trang.
EVIDENCE: ROOT và owner cùng xem 2/2 trang của DOCX cuối; bảng ba cột, mười hàng đọc được; không có hình, OMML, glossary table hoặc tài liệu tham khảo.
COUNTS: 2 trang A4; 1 bảng; 0 bibliography entries; 0 citations; 0 figures; 0 OMML.
FINDINGS: Không có dòng cô độc sau khi sửa phân trang. TNR trong heading không bị font theme override.
SEVERITY: LOW
UNRESOLVED: MICROSOFT_WORD_VALIDATION=NOT_VERIFIED.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## Gate 7. Gói đầu ra, bất biến và song song

STATUS: PASS
METHOD: ROOT đối chiếu manifest SHA-256 trước/sau, git diff trước/sau, scope tệp mới, receipt UTC và dispatch log.
EVIDENCE: 973/973 tệp bảo vệ không đổi; 387 tệp có sẵn giữ nguyên; 10 tệp mới đúng A/B (5 của B); tracked/cached diff byte-identical. Hai nhánh giao nhau 199.224118 giây.
COUNTS: 5 tệp B; 10 tệp A+B; 973 protected; 387 preexisting; overlap 199.224118 giây.
FINDINGS: Không branch/worktree, stage, commit hoặc push. ROOT chỉ bắt đầu cross-review sau khi hai nhánh hoàn tất vòng đầu.
SEVERITY: LOW
UNRESOLVED: Hai nghiệm thu độc lập và phê duyệt con người chưa thực hiện.
FINAL_DECISION: PASS


# HOTFIX GATES ADDENDUM — MP1-CH2-2.1.3-CALIBRATION-VALIDATION-WORDING-HOTFIX

Đây là kết quả mới nhất cho hotfix sau đánh giá MINOR_REVISION_REQUIRED. Phần tự rà soát trước được giữ nguyên làm lịch sử. Các kết quả hiển thị và hash ở phần này được kiểm trên DOCX đã sửa, không kế thừa QA cũ.

TASK_ID: MP1-CH2-2.1.3-CALIBRATION-VALIDATION-WORDING-HOTFIX
STATUS: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING

## HOTFIX GATE 1. Dàn ý và phạm vi

STATUS: PASS
METHOD: Đọc trực tiếp PDF canonical trang vật lý 10/22 đúng SHA-256; đối chiếu heading/B01–B03 và XML trước/sau.
EVIDENCE: Chỉ thay câu đầu P006 theo nguyên văn người dùng phê duyệt. Heading, các đoạn khác, caption và bảng giữ nguyên.
COUNTS: 3 bullet không đổi; 1 câu sửa; 7 đoạn nội dung và 2 caption/source.
FINDINGS: Đúng phạm vi §2.1.3; không viết §2.1.4 hoặc tích hợp chương.
SEVERITY: NONE
UNRESOLVED: Không còn finding về phạm vi hotfix.
FINAL_DECISION: PASS

## HOTFIX GATE 2. Tính đúng khoa học

STATUS: PASS
METHOD: Đối chiếu câu đã phê duyệt, nội dung còn lại P006 và phân biệt parameter estimation/calibration/predictive validation.
EVIDENCE: Tham số có thể được ước lượng từ dữ liệu hiệu chỉnh. Mô hình/tham số xác định và cố định trước đánh giá; tập kiểm chứng không tham gia hiệu chỉnh hoặc lựa chọn mô hình và không dùng để tinh chỉnh lại rồi nhận cùng tập đó là kiểm chứng độc lập.
COUNTS: 1 câu sai cách diễn đạt được sửa; 0 dữ liệu/thí nghiệm mới; 0 tuyên bố H0b đã kiểm chứng.
FINDINGS: Bỏ điều kiện sai rằng tham số phải độc lập với dữ liệu dùng ước lượng chính nó. Khớp calibration không tự chứng minh dự báo.
SEVERITY: NONE
UNRESOLVED: Ranh giới split trong nguồn không rõ vẫn được ghi chưa xác định, không suy held-out validation.
FINAL_DECISION: PASS

## HOTFIX GATE 3. Truy vết và anchors

STATUS: PASS
METHOD: Parse XML sau sửa; resolve từng XPath chọn đúng paragraph hoặc table-cell paragraph; kiểm Unicode slice, claim text, IDs, phủ ký tự và hash nguồn chính/phụ.
EVIDENCE: C007 giữ PROPOSED_METHOD/INTERNAL_RECORD/METHODOLOGY/B03 cùng toàn bộ provenance và boundary; chỉ đổi manuscript_anchor, claim_text_or_summary và anchor_end.
COUNTS: 40/40 anchors; 0 duplicate; 0 gap/overlap; C007[0,612); 29 nguồn phụ được kiểm hash.
FINDINGS: 39 records khác giữ nguyên mọi field value; không tạo Claim/Evidence ID mới.
SEVERITY: NONE
UNRESOLVED: Các locator M01 tranh chấp được giữ trong lịch sử và không được nâng thành verified scientific evidence.
FINAL_DECISION: PASS

## HOTFIX GATE 4. Liên tục khoa học

STATUS: PASS
METHOD: So sánh toàn bộ nội dung XML trước/sau và kiểm manifest của P3/accepted baselines.
EVIDENCE: Ngoài câu đầu P006, XML document giữ nguyên; mọi ZIP part ngoài document.xml giữ bytes. H0a/H0b/H1 và năm quyết định nghiên cứu không đổi.
COUNTS: 0 kết quả nguồn bị đổi; 0 novelty claim mới; 7 DOCX đã nghiệm thu giữ hash.
FINDINGS: Không suy H1 đúng hoặc H0b thất bại; giữ giới hạn chuyển giao và mapping RQ provisional.
SEVERITY: NONE
UNRESOLVED: Phê duyệt nghiên cứu và các câu hỏi mở vẫn ngoài phạm vi hotfix.
FINAL_DECISION: PASS

## HOTFIX GATE 5. Ma trận và synthesis

STATUS: PASS
METHOD: So sánh bytes XML toàn bảng, caption/source note; kiểm số hàng/cột, repeat header, chín phương diện và quy tắc tổng hợp.
EVIDENCE: Bảng native nguyên bytes, 3 cột/10 hàng; C007 làm rõ hiệu chỉnh–kiểm chứng, không thay các nhóm hoặc nhận MATRIX_COMPLETE. T03/T04 trong terminology vẫn nhất quán.
COUNTS: 9/9 phương diện; 1 bảng native; 5 thuật ngữ byte-identical; 0 references/DOI trong bibliography.
FINDINGS: B03 giữ nguyên nguyên tắc synthesis; không tái cấu trúc ma trận, không điền dữ liệu nguồn còn thiếu.
SEVERITY: NONE
UNRESOLVED: Giới hạn độ phủ từng bài và schema đã ghi trước hotfix còn nguyên.
FINAL_DECISION: PASS

## HOTFIX GATE 6. DOCX và kiểm tra hiển thị

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Kiểm CRC ZIP và tất cả XML/.rels; styles/lề/font; kết xuất bằng LibreOffice 24.2.7.2 với profile scratch riêng và xem trực tiếp tất cả trang.
EVIDENCE: DOCX đúng hash mới tạo PDF hai trang; P006 hiển thị đủ câu, dấu tiếng Việt đúng; bảng/caption không tràn hoặc bị tách bất thường.
COUNTS: 2/2 trang đã xem; 1 bảng native có repeat header; không trang trắng; XML/CRC PASS.
FINDINGS: Giữ A4, Times New Roman 12pt, line spacing 1.15 và lề 3/2/2.5/2.5 cm. Profile lần đầu trả81, chạy lại trả0, PDF hợp lệ.
SEVERITY: DOCUMENTED_LIMITATION
UNRESOLVED: MICROSOFT_WORD_VALIDATION=NOT_VERIFIED; không nhận LibreOffice là kiểm Microsoft Word.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS

## HOTFIX GATE 7. Baseline và gói

STATUS: PASS
METHOD: Tính lại manifest trước/sau, status/diff/cached và hash bảy DOCX đã nghiệm thu; kiểm đủ năm tên tệp, thuật ngữ và prefix báo cáo.
EVIDENCE: 614 tệp bảo vệ không đổi; toàn bộ §2.1.2 giữ bytes, DOCX accepted hash ed872c97025bdabc64b6efe79d83e1f80c0c72a021655b3401f90be16a327104. WEP/P3/registry không đổi.
COUNTS: 5 deliverables; chỉ4 tệp được sửa; 397 tệp có sẵn được ghi nhận,393ngoài scope không đổi.
FINDINGS: Không thêm/xóa final file; báo cáo chỉ append; scratch chứa mọi PDF/PNG/script; không stage/commit/push hoặc branch/worktree.
SEVERITY: NONE
UNRESOLVED: Independent hotfix acceptance vẫn bắt buộc; đây là SELF_REVIEW_ONLY.
FINAL_DECISION: PASS

FINDING_ID: P2-CALIBRATION-VALIDATION-DISTINCTION
FINDING_RESOLUTION_STATUS: RESOLVED_IN_SELF_REVIEW_PENDING_INDEPENDENT_ACCEPTANCE
P1_P2_UNRESOLVED: 0 trong phạm vi hotfix
FINAL_SELF_REVIEW_DECISION: HOTFIX_COMPLETED_WITH_DOCUMENTED_LIMITATIONS
NEXT_ACTION: AWAIT_INDEPENDENT_HOTFIX_ACCEPTANCE
