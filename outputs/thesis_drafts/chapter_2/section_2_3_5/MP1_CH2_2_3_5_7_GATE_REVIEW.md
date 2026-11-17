# MP1-CH2-2.3.5 — BÁO CÁO BẢY CỔNG NGHIỆM THU

STATUS: PASS_ALL_7_GATES về khoa học và cấu trúc; WORD_RENDER_VALIDATION: NOT_VERIFIED.

## Gate 1 — Outline compliance: PASS

- B01 được bao phủ bằng tổng hợp nguyên lý và các phụ thuộc topology, packing, membrane/sleeve, biên và observable.
- B02 được bao phủ bằng câu hỏi hẹp về TiNi, pressure transfer và khả năng nhận dạng, với chuyển tiếp sang §2.4.
- Nội dung tích hợp wire/fibre, layer, granular và pressure-dependent jamming nhưng không lặp lại các mô tả chi tiết trước đó.

## Gate 2 — Claim traceability: PASS

- 10 technical claims (C01–C10) và 3 document-coverage records (C11, D01–D02).
- 4 nguồn mới M17/M18/M06/M07 được truy vết bằng PDF locator; các nguồn M08/M09/M10/M13 được dùng lại từ traceability đã nghiệm thu.
- DIRECT_SUPPORT, COMPARATOR, INFERENCE và AUTHOR_PROPOSAL được phân biệt.

## Gate 3 — Original PDF verification: PASS

- M17, M18, M06 và M07 đã được mở và kiểm tra trực tiếp.
- M17: 8/12/16/20 lớp, 68 kPa; 20 lớp thêm 24/48 kPa; ba lần lặp; uốn ba điểm và FE.
- M18: continuum limit, FEA 10/25 lớp, thí nghiệm PVC 20 lớp ở 60 kPa; sai lệch biên/trượt lớn được giữ.
- M06: Table 1 là tổng quan dị thể, không pooling; M07: kết luận phi tuyến/slip-dependent và giới hạn số lớp/áp suất được giữ đúng.

## Gate 4 — Cross-study synthesis: PASS

- Bảng 2.3.5 so sánh medium, topology, observable, model/validation và transfer limits.
- E, EI, lực–độ võng, mô men–độ cong, tỷ số độ cứng và tải tới hạn không bị gộp.
- FEA agreement, calibration và experimental validation được phân biệt.
- Không đưa ra universal jamming law hoặc pooled coefficient.

## Gate 5 — Mechanical assumptions and limitations: PASS

- Áp suất nguồn được tách khỏi áp suất gần mẫu và lực pháp tuyến cục bộ.
- Mô hình continuum không được chuyển trực tiếp sang bó dây TiNi.
- Topology MP1, pressure-transfer law và constitutive law vẫn để mở.
- Các yêu cầu về identifiability là AUTHOR_PROPOSAL, không phải kết quả đã xác nhận.

## Gate 6 — Citation and reference integrity: PASS

- 8 reference được sử dụng và có citation [1]–[8].
- Tác giả, năm, tiêu đề và DOI được đối chiếu với Source Matrix và PDF gốc.
- Không có Paper ID/Evidence ID trong manuscript prose.

## Gate 7 — Vietnamese MSc writing quality: PASS

- Nội dung học thuật bằng tiếng Việt, thuật ngữ cơ học nhất quán.
- Có phân biệt bằng chứng, suy luận tổng hợp và đề xuất yêu cầu nhận dạng.
- Glossary có 16 thuật ngữ, bảng 6 cột, header lặp, hàng không tách và cỡ chữ tường minh.
- Không có workflow/QA text trong thân bản thảo.

## Document QA

- DOCX ZIP integrity: PASS.
- Tables: 2; figures: 0; equations: 0.
- Citation/DOI closure: PASS.
- Technical claims: 10; document coverage: 3; terminology: 16.
- Không có trình kết xuất LibreOffice/soffice/pandoc; render trực quan: NOT_VERIFIED.

## Remaining limitations

- M17/M18 đều là layer-jamming architectures; không cung cấp validation trực tiếp cho bó dây TiNi.
- M18 có overlap mạnh với các câu hỏi continuum/homogenization, nhưng miền kiểm chứng vẫn hữu hạn và có sai lệch gần biên/trượt lớn.
- M06 là review dị thể; không dùng để suy ra tỷ số độ cứng hoặc thời gian chuyển trạng thái chung.
- Các quyết định về topology, pressure sensing, observable chính và tiêu chí nhận dạng MP1 được giữ nguyên để xử lý ở các bước sau.

## Final micro-hotfix

- C11 đã được phân loại lại thành `DOCUMENT_COVERAGE`; bằng chứng và nội dung chuyển tiếp được giữ nguyên.
- Bảng/glossary đã Việt hóa các nhãn thừa bằng tiếng Anh; cột English term giữ nguyên.
- Cỡ chữ bảng được tăng thận trọng: bảng so sánh 8,0–8,5 pt; glossary 8,0–8,5 pt.
- Technical claims: 10; document coverage: 3; terminology: 16.
- WORD_RENDER_VALIDATION: NOT_VERIFIED.

## Final citation/layout micro-fix

- Bảng 2.3.5: nhãn hàng granular được sửa thành `Hạt [7]`; [8] vẫn giữ ở hàng dây/sợi.
- Cụm “Hơn nữa” dùng non-breaking space để tránh tách dòng.
- Technical claims: 10; document coverage: 3; references: 8; terminology: 16.
- DOCX integrity, citations, table formatting and fonts: PASS; WORD_RENDER_VALIDATION: NOT_VERIFIED.
