# Bảy Gate tự kiểm tích hợp §2.6

TASK_ID: MP1-CH2-2.6-INTEGRATION

STATUS: COMPLETED_SELF_REVIEW_ONLY

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

INDEPENDENT_ACCEPTANCE_STATUS: AWAIT_INDEPENDENT_ACCEPTANCE

DOCX_SHA256: `d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b`

Các kết quả dưới đây là kiểm tra thực tế của phiên và worker cùng nhóm. Không phải nghiệm thu độc lập.

## Gate 1. Phạm vi, dàn ý và bảo toàn nội dung

STATUS: PASS

METHOD: Đối chiếu PDF trang 14–15; so từng đoạn nguồn/đích sau khi chỉ đổi số trích dẫn; so chữ và định dạng đậm/nghiêng/chỉ số trên/dưới ngoài phần trích dẫn.

CHECKLIST: Đủ 4 tiêu đề đã nghiệm thu, đúng thứ tự; 58 đoạn thân; không có mục 2.6.5, bìa, mở đầu/kết luận riêng hoặc nội dung ngoài phạm vi.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 58/58 đoạn; 30 đoạn giữ nguyên ký tự; 28 đoạn chỉ đổi trích dẫn; 4/4 tiêu đề; ADDED_CLAIM = 0.

FINDINGS: Khác biệt giữa tiêu đề PDF ở §2.6.1/§2.6.2 và tiêu đề đã nghiệm thu được ghi rõ; không phát hiện đoạn bị mất.

SEVERITY: Không.

UNRESOLVED: Không còn lỗi chưa giải quyết.

FINAL_DECISION: PASS; chỉ tự rà soát, không cấp acceptance độc lập.


## Gate 2. Liêm chính khoa học và P3

STATUS: PASS

METHOD: Root và worker C đã đọc P3/WP-E, đối chiếu nguyên văn phần thân và giữ trạng thái P3 ngoài bản thảo trong bảng kiểm.

CHECKLIST: G00 đóng cơ chế chung; G01–G08 là câu hỏi có điều kiện; G09 là điều kiện tiên quyết; G10 chưa được xác lập; G11 là cách diễn đạt bị cấm; H0b còn là đối thủ sống; H1 chưa đủ bằng chứng; các quyết định còn mở được giữ nguyên.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 12/12 dòng P3 được đối chiếu; H0a/H0b/H1 không đổi; 5 quyết định còn mở; 2 nhóm RQ giữ nguyên namespace.

FINDINGS: Không nâng tuyên bố mới, không chốt bench/cảm biến/hình học và không tạo kết quả MP1.

SEVERITY: Không.

UNRESOLVED: Các quyết định nghiên cứu và nghiệm thu của con người còn chờ, được bảo lưu.

FINAL_DECISION: PASS; chỉ tự rà soát, không cấp acceptance độc lập.


## Gate 3. Truy vết cấp claim

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Phân tích hợp nhất 63 cột; so sánh lossless JSON ở 267 dòng; kiểm bookmark, ancestor và anchor range trong DOCX đã mở lại; kiểm hash nguồn và lớp hiệu chỉnh locator.

CHECKLIST: Giữ ID/phân loại/vai trò/provenance nguồn; 267 master ID duy nhất; mọi anchor đều phân giải được; không tạo Evidence ID hoặc giả xác minh mới.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 267/267 dòng nguồn; 223 bản ghi phần thân + 44 bản ghi thuật ngữ; 267/267 anchor; 9 hiệu chỉnh/7 claim; 0 mục chưa phân giải.

FINDINGS: B-01 được xử lý trong `integration_verified_locator`; locator gốc vẫn được lưu để kiểm tra.

SEVERITY: P2 ban đầu; đã xử lý trong bản tích hợp.

UNRESOLVED: Không tái kiểm toàn bộ 39 PDF; trạng thái bằng chứng nguồn được kế thừa và ghi rõ.

FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chỉ tự rà soát, không cấp acceptance độc lập.


## Gate 4. Cơ học, mô hình và bất định

STATUS: PASS

METHOD: Đọc toàn văn và bảng thuật ngữ; đối chiếu P3/WP-E; so nội dung nguồn/đích để tìm thay đổi ngoài phần trích dẫn.

CHECKLIST: E tính bằng Pa; B/EI tính bằng N·m²; K tính bằng N/m hoặc N/mm; M tính bằng N·m; κ tính bằng m⁻¹. M–κ suy ra khác với phép đo trực tiếp; áp suất khác traction; ngưỡng Coulomb khác lực ma sát thực tế; slip/vòng trễ/hiệu chuẩn có giới hạn.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 58 đoạn thân + 35 hàng thuật ngữ; 0 phương trình mới; 0 kết quả MP1; 0 xung đột cơ học giữa các tiểu mục.

FINDINGS: Các mục ghép E/B/K vẫn giữ riêng; không dùng phép đo pull-out để nhận dạng duy nhất μ hoặc N.

SEVERITY: Không.

UNRESOLVED: Giới hạn phương pháp của đề tài vẫn còn mở, chưa phải dữ kiện đã được thiết lập.

FINAL_DECISION: PASS; chỉ tự rà soát, không cấp acceptance độc lập.


## Gate 5. Thuật ngữ và hợp nhất trích dẫn

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Đối chiếu 44 dòng nguồn với 35 hàng bảng/CSV; 34 ánh xạ tài liệu; khai triển khoảng trích dẫn; quét lần xuất hiện đầu, mục mồ côi và DOI.

CHECKLIST: Gộp 6 nhóm tương đương; giữ đủ định nghĩa; phần thân đứng trước bảng thuật ngữ; 16 tài liệu duy nhất; mọi ký hiệu trích dẫn cũ và mới đều phân giải được.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 44/44 lineage; 35/35 hàng khớp; 34 → 16 tài liệu tham khảo; 107 biểu thức → 117 lần trích dẫn; 15 DOI duy nhất; 0 mục mồ côi.

FINDINGS: Metadata cuối của M25/M26 dựa trên M28, PDF trang 19; JCGM không có DOI; không tự điền số kỳ.

SEVERITY: Giới hạn provenance metadata đã được ghi.

UNRESOLVED: Chưa đối chiếu thông tin với nhà xuất bản cho toàn bộ 16 tài liệu; không suy đoán metadata còn thiếu.

FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chỉ tự rà soát, không cấp acceptance độc lập.


## Gate 6. Kỹ thuật DOCX và kiểm tra trang

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Kiểm tra CRC/XML/relationships trong ZIP; kiểu định dạng, lề, phông và bảng; kết xuất bằng hồ sơ LibreOffice riêng rồi root xem từng trang; so văn bản PDF với DOCX.

CHECKLIST: Khổ A4, Times New Roman, 12 pt, giãn dòng 1,15, lề 3/2/2,5/2,5 cm; bảng thuật ngữ Word có 35 hàng; lặp hàng tiêu đề; không tách hàng; thụt dòng treo; không có header/footer cũ; Unicode đầy đủ.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 1 bảng thuật ngữ; 0 bảng khoa học; 0 ảnh; 0 OMML; 18 trang đã kết xuất; 18 trang đã xem.

FINDINGS: Đã kiểm từng trang và thông số; xem phần kiểm tra render bên dưới.

SEVERITY: Còn giới hạn về tương thích với Microsoft Word.

UNRESOLVED: MICROSOFT_WORD_VALIDATION: NOT_VERIFIED.

FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chỉ tự rà soát, không cấp acceptance độc lập.


## Gate 7. Gói, baseline và khả năng tái kiểm

STATUS: PASS

METHOD: So sánh snapshot 565 đường dẫn; kiểm tra git status/diff/staged; phân tích 7 tệp cuối; đọc lại mã QA, báo cáo, CSV và DOCX.

CHECKLIST: Đúng 7 tệp; không có scratch trong thư mục final; 20 đầu vào đã nghiệm thu và baseline §§2.3–2.5 giữ nguyên; branch main/HEAD không đổi; không stage/commit/push/PR.

EVIDENCE: DOCX hash ở trên; MASTER_SOURCE_TRACEABILITY; MASTER_TERMINOLOGY; CITATION_RENUMBERING_MAP; changelog mục tương ứng; kết quả QA bằng máy bên dưới.

COUNTS: 565/565 tệp snapshot không đổi; 20/20 đầu vào đã nghiệm thu không đổi; 7 tệp cuối; 3 CSV gắn với hash DOCX; 0 thay đổi ngoài thư mục final.

FINDINGS: Các thay đổi/untracked có sẵn được bảo lưu; không phát hiện tiến trình khác sửa cùng vùng.

SEVERITY: Không.

UNRESOLVED: REVIEW_AUTHORITY chỉ là SELF_REVIEW_ONLY; nghiệm thu độc lập vẫn còn chờ.

FINAL_DECISION: PASS; chỉ tự rà soát, không cấp acceptance độc lập.


## Đối chiếu trạng thái P3

| Gap | Classification canonical | Status canonical | Xử lý tích hợp |
|---|---|---|---|
| G00 | SUPPORTED_WITHIN_REVIEWED_CORPUS | CLOSED_AS_GENERAL_MECHANISM; MP1 transfer remains open | Giữ nguyên; không thay hồ sơ P3. |
| G01 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-IDENTIFICATION QUESTION | Giữ nguyên; không thay hồ sơ P3. |
| G02 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-IDENTIFICATION QUESTION | Giữ nguyên; không thay hồ sơ P3. |
| G03 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN BOUNDED EMPIRICAL CHARACTERIZATION | Giữ nguyên; không thay hồ sơ P3. |
| G04 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN ENGINEERING/SYSTEM-IDENTIFICATION QUESTION | Giữ nguyên; không thay hồ sơ P3. |
| G05 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN ATTRIBUTION/REPEATABILITY QUESTION | Giữ nguyên; không thay hồ sơ P3. |
| G06 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN BOUNDED MODEL-DISCRIMINATION QUESTION | Giữ nguyên; không thay hồ sơ P3. |
| G07 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN IDENTIFIABILITY GATE | Giữ nguyên; không thay hồ sơ P3. |
| G08 | PLAUSIBLE_REQUIRES_FURTHER_EVIDENCE | OPEN SYSTEM-CALIBRATION QUESTION | Giữ nguyên; không thay hồ sơ P3. |
| G09 | OUT_OF_SCOPE | PROJECT PREREQUISITE, NOT A LITERATURE GAP | Giữ nguyên; không thay hồ sơ P3. |
| G10 | NOT_ESTABLISHED | CONDITIONAL STRETCH ONLY | Giữ nguyên; không thay hồ sơ P3. |
| G11 | NOT_ESTABLISHED | PROHIBITED CLAIM | Giữ nguyên; không thay hồ sơ P3. |

H0a = REFUTED_IN_TRANSFORMATION_REGIME; không suy rộng kết luận ra mọi miền. H0b = NOT_FALSIFIED_LIVE_COMPETITOR. H1 = INSUFFICIENT_EVIDENCE. Việc đóng G00 không bác bỏ H0b. Luận văn không cần chứng minh phải có luật cấu thành mới.

RQ_MAPPING: 5 RQ trong PDF ↔ 4 nhóm RQ của P3; PROVISIONAL_MANY_TO_MANY; HUMAN_DECISION_PENDING. Không nhập namespace này với năm quyết định còn mở. Năm quyết định là: hình học/giao diện; khả năng quan sát hoặc đại diện tải pháp tuyến; miền nhiệt độ/pha/tốc độ/lịch sử TiNi; đại lượng độ cứng và bất định; phạm vi SMA–piston.


## Kết quả kiểm bằng máy

```json
{
  "qa_status": "PASS",
  "docx_sha256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "master_records": 267,
  "original_rows_lossless": 267,
  "anchors_resolved": 267,
  "body_paragraphs_preserved": 58,
  "source_terminology_lineage": 44,
  "master_terms": 35,
  "local_reference_mappings": 34,
  "integrated_references": 16,
  "doi_unique": 15,
  "reference_incidences": 117,
  "first_use_order": [
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
    16
  ],
  "source_union_columns": 63,
  "zip_crc_xml_relationships": "PASS",
  "native_tables": 1,
  "figures": 0,
  "omml": 0,
  "top_level_paragraphs": 81,
  "integration_locator_correction_claims": 7
}
```

## Kiểm render sau cùng

```json
{
  "status": "PASS",
  "renderer": "LibreOffice 24.2.7.2 420(Build:2), headless writer_pdf_Export",
  "docx_sha256": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "pdf_sha256": "3e3f09928a71fb2fe29d84a575589a2cbcb22e023718d3432c6f4f04773f26f5",
  "pages": 18,
  "pages_visually_reviewed": [
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
    18
  ],
  "profile": "/tmp/mp1-ch26-integration/lo-final-profile3",
  "all_scratch_outside_final_directory": true,
  "command": "env DCONF_PROFILE=/dev/null XDG_RUNTIME_DIR=/tmp/mp1-ch26-integration/runtime LD_LIBRARY_PATH=/tmp/mp1-ch26-integration/lo-root/usr/lib/libreoffice/program:/tmp/mp1-ch26-integration/lo-root/usr/lib/x86_64-linux-gnu SAL_USE_VCLPLUGIN=svp /tmp/mp1-ch26-integration/lo-root/usr/lib/libreoffice/program/soffice.bin -env:UserInstallation=file:///tmp/mp1-ch26-integration/lo-final-profile3 --headless --convert-to pdf --outdir /tmp/mp1-ch26-integration/render /home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx",
  "portable_setup": "52 Ubuntu deb giải nén /tmp, không cài hệ thống; chuẩn lại absolute rc/symlinks, dùng unorc đúng thư mục thư viện, chép .registry vào registry scratch; bỏ dconf khỏi cấu hình scratch. Chạy render ngoài sandbox với quyền đã cho phép; khởi tạo profile trả81 rồi chạy lại thành công0.",
  "render_warning": "liblangtag báo thiếu /usr/share/liblangtag/language-subtag-registry.xml trong portable setup. Xuất PDF kết thúc0; kiểm đối chiếu toàn bộ text và fonts không thấy nội dung/glyph mất. Không dùng render này để đánh giá spellcheck/language tagging.",
  "text_checks": {
    "pdf_sha256": "3e3f09928a71fb2fe29d84a575589a2cbcb22e023718d3432c6f4f04773f26f5",
    "pages": 18,
    "body_missing": [],
    "glossary_missing": [],
    "fonts": {
      "TimesNewRomanPS-BoldMT": 968,
      "TimesNewRomanPSMT": 53365
    },
    "replacement_glyphs": 0
  },
  "MICROSOFT_WORD_VALIDATION": "NOT_VERIFIED",
  "page_audit": [
    {
      "page": 1,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        81.42,
        541.75,
        738.24
      ],
      "png_sha256": "b7b32541cd1b85a931af3ed91139091dda617b012f81c218ae3c6412a6391b49",
      "text_sha256": "f927389d2ceba0da6ae2e5b66e1ad2562b2e5fd19bba24006cabdd67cbed0052",
      "findings": "Trang đầu, heading cha và §2.6.1; font Times New Roman đúng.",
      "severity": "NONE"
    },
    {
      "page": 2,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        758.49
      ],
      "png_sha256": "9de5bde7af64ee7b8e82a0fa46cac5475a1fea4875f0dcb0899700329f0ff84a",
      "text_sha256": "aee06dad2cdd19ce28a2dbe34ed5e5396f974d8d98b9eb58d3dbe21857e51efc",
      "findings": "Nội dung liên tục, citation/Unicode rõ; không clipping hoặc tràn lề.",
      "severity": "NONE"
    },
    {
      "page": 3,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        710.94
      ],
      "png_sha256": "48182da5ca742897ea071aae0f533b632eb4785136726b59bdac3d9b3d97c7be",
      "text_sha256": "74b99343dbff735c0db23eefd5191e759bed3237ae3bb6a9b7bca37a64724386",
      "findings": "Cuối §2.6.1; không mất câu chuyển tiếp sang §2.6.2.",
      "severity": "NONE"
    },
    {
      "page": 4,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        770.49
      ],
      "png_sha256": "ec1d87f97835dd02fd9da0918ce6e5b0b6e8d3adb0b2724f3ced7ba7140efab6",
      "text_sha256": "bca8980453e61b08ef67c86d32ecdc453d24b86ec047a8b309b8ba5f27f8ce02",
      "findings": "Heading §2.6.2 và citation 11–13 đúng; tiếp nối đoạn qua trang bình thường.",
      "severity": "NONE"
    },
    {
      "page": 5,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.49
      ],
      "png_sha256": "a9709f3b79853b9055fef081f08271e5c574cf425ac8ebf408e384b29310b8b3",
      "text_sha256": "ab30f97b305bf9544168929b4899f20ba679c0e09886b9fc8a44c018c865cb69",
      "findings": "Nội dung liên tục, citation/Unicode rõ; không clipping hoặc tràn lề.",
      "severity": "NONE"
    },
    {
      "page": 6,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        732.79
      ],
      "png_sha256": "4694b4c55906dee289342270d57631c2dd04d27b15e5cc953f2d0bedac16c486",
      "text_sha256": "5d38b0b8059684d364c204cae580744de474be6d0fd56f293a16a4ed0867f195",
      "findings": "Cuối §2.6.2; giữ H0b và quyết định mở.",
      "severity": "NONE"
    },
    {
      "page": 7,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        770.49
      ],
      "png_sha256": "eff9a0e56c6e527a8ffc76e1a3755ac75a5b3aca8c0212571a8f6d5f65a6a592",
      "text_sha256": "89583487f410a91a39c864ab1565fdb9453805818b601c8869ef3ec23790fe7d",
      "findings": "Heading §2.6.3; prior art và câu hỏi có điều kiện.",
      "severity": "NONE"
    },
    {
      "page": 8,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.49
      ],
      "png_sha256": "161de63a6fd6935cb49034a5f0b619d2cf9e4f24e49632a1ab73eacad17c670a",
      "text_sha256": "6d589058894746178172562412f9e9fa54d086e2347f527e9cb1c8aa49e301d3",
      "findings": "Nối đoạn từ trang7; citation đầu trang thuộc cùng đoạn, còn đầy đủ.",
      "severity": "NONE"
    },
    {
      "page": 9,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.64
      ],
      "png_sha256": "3744e62020592a49651c7ee8055c41f3cffbaf64551931a26e9232149e886e1b",
      "text_sha256": "c4736492c75d63afb91222bfeaf0494ee814e0e4a25dd8ff5699462e87ddfee9",
      "findings": "Cuối §2.6.3 và heading §2.6.4; không mất đoạn.",
      "severity": "NONE"
    },
    {
      "page": 10,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        764.49
      ],
      "png_sha256": "9fa3d7017a03bb0f0412dc58bae7a372cbcf84d8fecad4d5615b35282b13864d",
      "text_sha256": "fbcfe16593c6037baef2b1a15acfb3013547766f89c52ad83cca2a19270c7508",
      "findings": "Ký hiệu M–κ, E, B/EI, K và đơn vị đọc được.",
      "severity": "NONE"
    },
    {
      "page": 11,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        669.39
      ],
      "png_sha256": "b4d9c1c67a6c9d05712cf0252a67c9e3132631f16068b96c608185059bdd237a",
      "text_sha256": "e9db78d6db1c6132cfcfdc566631432bef9bdf12ac35e19e43f64798dda24038",
      "findings": "Cuối §2.6.4; năm nhóm quyết định còn mở.",
      "severity": "NONE"
    },
    {
      "page": 12,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        514.41,
        697.16
      ],
      "png_sha256": "014ce062dddeb41983b766151a79dbc09bfe36a4af2724d34a11a3637610c419",
      "text_sha256": "879a3b8e3f5fbe0d9a5c467498bf3ee662a848e2ca25c49f194afcd1f0853cec",
      "findings": "Heading bảng chung cùng header; hàng thuật ngữ native không clipping.",
      "severity": "NONE"
    },
    {
      "page": 13,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        492.61,
        591.96
      ],
      "png_sha256": "eb0a53fa0f3cc4216940161b764e07f4e47bc718cf6cb8cfa8ce8eadb58521ea",
      "text_sha256": "81e4bee4e9f5fe1cd1e90a6ad8f2598235f03d65477564292396e30de1ba5d59",
      "findings": "Header lặp; khoảng trắng cuối trang do giữ nguyên hàng cao kế tiếp, có chủ đích.",
      "severity": "NONE"
    },
    {
      "page": 14,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        526.48,
        711.26
      ],
      "png_sha256": "807e19f23b371189ff2c48c190a75468bca0ca8c9006e5c9b593c7780f819116",
      "text_sha256": "cd070d57e9f1f958b6279e94d80b47d0fe61b7df8fb6648aeebe9f1a941cf1f2",
      "findings": "Hàng độ không đảm bảo bốn định nghĩa cùng trang; không tách/mất nội dung.",
      "severity": "NONE"
    },
    {
      "page": 15,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        528.05,
        739.46
      ],
      "png_sha256": "444c02c989727b858332415ef24905c89383bb3e5219ade90d90fea9144e6273",
      "text_sha256": "b0d1d3c29d938ae29836553b32191111fcd693db28e69b77c7f1938d62261bd8",
      "findings": "Gộp local traction và independent predictive validation; đủ các nhãn tiểu mục.",
      "severity": "NONE"
    },
    {
      "page": 16,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        524.84,
        717.61
      ],
      "png_sha256": "a408d79d0a7bde7e5b400598ac4a969dc06b93a25e4f0fa1f0e0398bdccc19f7",
      "text_sha256": "0922e9e1ca18a5d2eaf881d8e80f789d37d1906d4eb66f7457acd62d74a61642",
      "findings": "Các mục composite E/B/K giữ riêng; chữ/đơn vị không tràn ô.",
      "severity": "NONE"
    },
    {
      "page": 17,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.79,
        541.75,
        768.69
      ],
      "png_sha256": "0134742133fad64400c3f0e9a8822019699d96a0da8979e6a49e026ac493d099",
      "text_sha256": "27d7c97f12a3446d478421e88489b9d9fad93f92816f93165ab75bb582acd0f2",
      "findings": "Header lặp, hai hàng cuối glossary và bibliography[1]–[9].",
      "severity": "NONE"
    },
    {
      "page": 18,
      "visual_status": "PASS",
      "page_size_pt": [
        595.3,
        841.89
      ],
      "text_bbox_pt": [
        85.15,
        71.36,
        541.75,
        453.49
      ],
      "png_sha256": "4f3c2716a1f8b7babfe8be2e8872e7df6f4e6225996c0091e31991b96299963a",
      "text_sha256": "09ae527f35c3285d73f0e8f2153b2f0d2b1beb624ee83ab108d26adf1a564090",
      "findings": "Trang cuối bibliography[10]–[16]; không có nội dung ngoài §2.6.",
      "severity": "NONE"
    }
  ]
}
```

## Giới hạn bằng chứng và thẩm quyền

- Chỉ SELF_REVIEW_ONLY. Ba worker nằm trong cùng phiên, không phải hội đồng nghiệm thu độc lập và không bỏ phiếu quyết định.
- MICROSOFT_WORD_VALIDATION: NOT_VERIFIED. LibreOffice không bảo đảm phân trang giống Microsoft Word.
- Nhãn VERIFIED FULL TEXT trong các trường nguồn được kế thừa từ baseline; không phải xác minh mới toàn bộ 267 claim hoặc 39 PDF. Tái kiểm trực tiếp chỉ gồm nhóm metadata/locator rủi ro được liệt kê.
- Metadata xuất bản cuối của M25 và M26 có xuất xứ thứ cấp nội bộ từ danh mục tài liệu tham khảo M28, trang vật lý 19. Không tuyên bố đã kiểm tra metadata với nhà xuất bản cho toàn bộ tài liệu; không tự bổ sung số kỳ hoặc DOI.
- RQ_MAPPING là 5 RQ của PDF ↔ 4 nhóm P3, PROVISIONAL_MANY_TO_MANY, HUMAN_DECISION_PENDING. Năm nhóm quyết định của con người là danh sách riêng.
- Các lựa chọn hình học, đại diện tải pháp tuyến, miền trạng thái TiNi, đại lượng độ cứng/bất định và phạm vi SMA–piston còn mở. Nghiệm thu văn bản không phê duyệt thí nghiệm.
- Việc giữ nguyên định nghĩa theo từng tiểu mục làm một số hàng thuật ngữ dài và có lặp có chủ đích. Không rút gọn để đổi lấy số trang.


## Quyết định cuối

SEVEN_GATE_RESULT: G1=PASS; G2=PASS; G3=PASS_WITH_DOCUMENTED_LIMITATIONS; G4=PASS; G5=PASS_WITH_DOCUMENTED_LIMITATIONS; G6=PASS_WITH_DOCUMENTED_LIMITATIONS; G7=PASS

P1_P2_UNRESOLVED: 0

FINAL_SELF_REVIEW_DECISION: Đủ điều kiện gửi người dùng nghiệm thu độc lập với các giới hạn đã ghi; chưa được chấp nhận.

NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE