# Báo cáo bảy Gate của bản tích hợp mục 2.2

TASK_ID: MP1-CH2-2.2-INTEGRATION
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING
INDEPENDENT_ACCEPTANCE_STATUS: REQUIRED; NOT_PERFORMED

## Gate 1. Dàn ý, phạm vi và nội dung

STATUS: PASS

METHOD: ROOT kiểm hash, văn bản và ảnh trang vật lý 11 PDF canonical; so sánh từng đoạn theo source identity và Citation Map.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 34/34 body paragraphs; 3/3 subsections; 0 đoạn khoa học mới; 0 đoạn bị xóa.

FINDINGS: Heading/order khớp; giữ ba đoạn chuyển tiếp có sẵn. Không tạo mục 2.2.4.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: Không có xung đột dàn ý hoặc nội dung.

FINAL_DECISION: PASS; chỉ là tự kiểm trong phạm vi tích hợp.

## Gate 2. Liêm chính khoa học và P3

STATUS: PASS

METHOD: ROOT đọc manuscript cuối và sáu tệp P3 canonical, đối chiếu matrix12 gaps và reconciliation H0a.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 3/3 hypotheses đúng; 12/12 gaps đúng; 5 nhóm quyết định vẫn mở; 5 PDF RQ ↔4 nhóm P3.

FINDINGS: Không đổi giả thuyết, không suy H1 từ H0a, không phê duyệt topology/p-to-N/Bench hoặc tính mới.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: Các quyết định khoa học của con người và nghiệm thu độc lập tiếp tục pending theo thiết kế tác vụ.

FINAL_DECISION: PASS; chỉ là tự kiểm trong phạm vi tích hợp.

## Gate 3. Master traceability

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Bộ QA riêng không import builder: JSON equality từng source record, union tên cột, bookmark/container/section, slice Unicode exact; worker B kiểm lại.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 226/226 lossless; 226 IDs unique; 226/226 anchors exact; 0 unresolved; body118/table15/figure14/glossary77/caption2.

FINDINGS: Schema36 bảo toàn đầy đủ; không chỉ đếm dòng. Kiểm cả alt text, caption và đúng ô bảng. Không tạo Evidence ID.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: M03/M23/M38 và trạng thái nguồn được kế thừa; không tái kiểm mọi PDF.

FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chỉ là tự kiểm trong phạm vi tích hợp.

## Gate 4. Tính nhất quán cơ học

STATUS: PASS

METHOD: ROOT đọc lại toàn bộ nội dung sau ghép và xử lý 15 checks; đối chiếu DOCX, terminology/traceability §§2.3–2.6; worker C hỗ trợ.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 15/15 checks; 0 scientific conflicts chưa giải; 0 kết quả MP1 thêm.

FINDINGS: E/B/EI/K, M–κ, Coulomb, slip, vòng trễ, áp suất/traction/N, mặt cong, đo lường và TiNi phân biệt đúng miền.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: Không có P1/P2 trong phạm vi tích hợp. Không biến kiểm từ vựng thành kiểm chứng mô hình MP1.

FINAL_DECISION: PASS; chỉ là tự kiểm trong phạm vi tích hợp.

## Gate 5. Citation và thuật ngữ

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Định danh theo section+Paper ID+DOI/title, kiểm lần dùng đầu; đối chiếu đủ71 occurrences và lineage; Word/CSV exact từng ô glossary.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 16/16 local refs→13 canonical; DOI12; citations71→71, đổi36; orphan0; terms35→33, gộp2, lineage35/35.

FINDINGS: GUM không DOI; ba cặp duplicate đúng. M–κ relation và paired quantities giữ riêng. Không gộp áp suất với traction/N.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: M23 năm tạp chí2021/online2020 được giữ; không bổ sung metadata mới.

FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chỉ là tự kiểm trong phạm vi tích hợp.

## Gate 6. DOCX và kiểm tra trực quan

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Kiểm ZIP CRC/XML/relationships/style/margins/font/media; Microsoft Word COM mở bản sao chỉ đọc và xuất PDF; ROOT xem mọi trang.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 16 XML/.rels parsed;14 rels resolved;1 image/1 scientific table6×3/1 glossary34×3;0 OMML;13/13 pages viewed;0 blank pages.

FINDINGS: Ảnh byte/alt/title/extent giữ nguyên, hai mạch A/B đầy đủ; caption đúng đối tượng. Không clipping/glyph lỗi. TNR12, A4, lề đúng, header bảng lặp, hàng không cắt.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: Chỉ kiểm Microsoft Word16.0 build16.0.20430 ở môi trường hiện tại; chưa kiểm mọi phiên bản/ứng dụng hoặc chỉnh sửa-lưu lại. Source baseline Word validation vẫn chưa xác minh.

FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chỉ là tự kiểm trong phạm vi tích hợp.

## Gate 7. Bảo toàn baseline và bàn giao

STATUS: PASS

METHOD: Đối chiếu checksum15 nguồn và bốn DOCX đối chiếu; toàn2016 tệp workspace có sẵn+14 external canonical snapshot; git status/diff/cached và HEAD trước/sau; đọc lại7 deliverables.

EVIDENCE: `MP1_CH2_2_2_INTEGRATED.docx`, các CSV master/map và mục tương ứng trong `MP1_CH2_2_2_INTEGRATION_CHANGELOG.md`; DOCX SHA-256 `701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34`. Bộ đếm thực và mã kiểm tái lập ở phần dưới; manifest và pre/postflight đầy đủ ở Execution Report.

COUNTS: 15/15 accepted inputs unchanged;4/4 integrated DOCX unchanged;2016/2016 workspace files unchanged;14/14 external snapshot files unchanged;7 final files;0 stage/commit/push.

FINDINGS: Chỉ thêm bảy tệp trong thư mục được phép. Hai modified files và373 untracked trước tác vụ được bảo toàn. Word lock được nêu không hiện diện tại preflight.

SEVERITY: Không còn P1/P2; các giới hạn được ghi nhận không bị nâng thành kết quả xác minh mới.

UNRESOLVED: SELF_REVIEW_ONLY; HUMAN_APPROVAL_PENDING; REQUIRED independent acceptance chưa thực hiện.

FINAL_DECISION: PASS; chỉ là tự kiểm trong phạm vi tích hợp.

## Kết quả kiểm định thực

```json
{
  "status": "PASS",
  "docx_sha256": "701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34",
  "source_records": 226,
  "mapped_records": 226,
  "unresolved_records": 0,
  "target_anchors_exact_match": 226,
  "anchor_counts": {
    "BODY_PARAGRAPH": 118,
    "GLOSSARY_CELL": 77,
    "DRAWING_ALT_TEXT": 14,
    "FIGURE_CAPTION": 1,
    "TABLE_CAPTION": 1,
    "TABLE_CELL": 15
  },
  "body_source": 34,
  "body_target": 34,
  "terms_source": 35,
  "terms_target": 33,
  "merges": 2,
  "source_citation_occurrences": 71,
  "target_citation_occurrences": 71,
  "citations_renumbered": 36,
  "source_reference_entries": 16,
  "references_target": 13,
  "unique_dois": 12,
  "scientific_tables": 1,
  "glossary_tables": 1,
  "figures": 1,
  "image_sha256": "26db28e4b1ff2d51a4be4f140dbf082ef8817301e7cfcbc9d955177409784b8f",
  "omml": 0,
  "xml_parts_parsed": 16,
  "internal_relationships_resolved": 14,
  "condition_word_counts": {
    "có thể": {
      "source": 21,
      "target": 21
    },
    "trong điều kiện": {
      "source": 2,
      "target": 2
    },
    "không nhất thiết": {
      "source": 1,
      "target": 1
    },
    "chưa xác định": {
      "source": 0,
      "target": 0
    },
    "chưa được kiểm chứng": {
      "source": 0,
      "target": 0
    },
    "không tự": {
      "source": 4,
      "target": 4
    },
    "phụ thuộc": {
      "source": 4,
      "target": 4
    },
    "giới hạn": {
      "source": 3,
      "target": 3
    }
  },
  "heading_inventory": [
    [
      "2.2. Thuật ngữ và khung cơ học",
      "Heading 1"
    ],
    [
      "2.2.1. Robot continuum và các đại lượng độ cứng",
      "Heading 2"
    ],
    [
      "2.2.2. Jamming, frictional locking và slip",
      "Heading 2"
    ],
    [
      "2.2.3. Áp suất cấp và lực pháp tuyến",
      "Heading 2"
    ],
    [
      "Bảng thuật ngữ của mục 2.2",
      "Heading 2"
    ],
    [
      "Tài liệu tham khảo",
      "Heading 2"
    ]
  ]
}
```

## Audit cơ học do ROOT phân xử

| Kiểm | Vị trí | Kết luận |
| --- | --- | --- |
| 1. Robot continuum | 2.2.1 P003 | Bó TiNi là cấu trúc ứng viên, chưa phải robot continuum hoàn chỉnh. |
| 2. Dầm tương đương | 2.2.1 P004, P010–P012 | Giữ điều kiện hình học, tiết diện, cấu thành, biên; có trượt không bác bỏ mọi mô hình dầm. |
| 3. Các cấp độ cứng | 2.2.1 P005–P009; glossary T005–T012 | E: Pa; B/EI: N·m²; K: N/m hoặc N/mm; không dùng lực cực đại thay độ dốc. |
| 4. Jamming và stick | 2.2.2 P01–P03 | Jamming cấp cấu trúc không đòi mọi tiếp xúc luôn bám. |
| 5. Giới hạn Coulomb | 2.2.2 P03 | \|Ft\| ≤ μ_s N là giới hạn mô hình ma sát tĩnh, lực thực do cân bằng; không cần thêm công thức vào baseline. |
| 6. Full slip | 2.2.2 P04–P05 | Theo miền giao diện công bố, không đồng nghĩa μ=0, dây độc lập hoàn toàn, dẻo hoặc B=0. |
| 7. Vòng trễ | 2.2.2 P05–P07 | Giữ lịch sử tải và các cơ chế cạnh tranh; không quy mọi trễ cho ma sát hoặc dẻo. |
| 8. Truyền áp suất | 2.2.3 P001–P005 | p_source không tự bằng p_near_sample; áp suất gần mẫu không tự bằng traction. |
| 9. Traction và hợp lực | 2.2.3 P005; bảng hàng dữ liệu 2; glossary hàng 26–27 | σ_n: Pa; N_i: N; mặt cong cần tích phân vectơ hoặc phép chiếu theo hướng xác định. |
| 10. Khả năng nhận dạng | 2.2.3 P004, P008–P010 | Áp suất tại một cổng không xác định duy nhất tải trên từng dây; tham số khớp không thành phép đo tiếp xúc. |
| 11. M–κ | 2.2.1 P007–P009; 2.2.3 bảng hàng 3 | M: N·m, κ: m⁻¹; F–δ cần sơ đồ tải, hình học và giả thiết để suy M–κ. |
| 12. Đo lường | 2.2.3 P009–P011 | Đo trực tiếp có thể đã hiệu chuẩn; repeatability khác uncertainty; nhận dạng/hiệu chuẩn khác kiểm chứng dự báo độc lập. |
| 13. Trạng thái TiNi | 2.2.1 P005; 2.2.2 P05–P07 | Pha, nhiệt độ, tốc độ và lịch sử vẫn có thể ảnh hưởng; không xác định trạng thái chỉ từ tên vật liệu. |
| 14. Diễn giải hình | 2.2.3 FIG01/CAP01 | Mạch A là tác động có điều kiện; mạch B là suy luận, không là đường truyền lực hoặc cấu hình MP1. |
| 15. Kết quả MP1 | 34 đoạn và toàn bộ glossary/bảng | Không thêm kết quả MP1, luật tiếp xúc hoặc claim tính mới; thêm claim khoa học = 0. |

## Kiểm tra trực quan từng trang

| Trang | Đã xem | Kết quả |
| --- | --- | --- |
| 1 | Có | Parent heading/subsection, E và B; không lỗi font. |
| 2 | Có | Dầm/độ cứng và điều kiện; đoạn sang trang3 đầy đủ. |
| 3 | Có | Chuyển §2.2.1→§2.2.2; Coulomb và slip. |
| 4 | Có | Chuyển §2.2.2→§2.2.3; pressure conventions. |
| 5 | Có | Truyền áp suất, mặt cong, giới hạn p×A; khoảng trắng do pagebreak nguồn. |
| 6 | Có | Hình2.2.3-1 cả mạchA/B, nhãn, caption và diễn giải; không clipping. |
| 7 | Có | Bảng2.2.3-1 đủ6×3 ô, caption và đoạn nhận dạng/bất định. |
| 8 | Có | Kết thúc body, mở glossary; header/6 hàng đầu. |
| 9 | Có | Glossary gồm hàng B/EI đã gộp, giữ cả hai định nghĩa. |
| 10 | Có | Glossary slip đã gộp và các trạng thái tiếp xúc, lịch sử. |
| 11 | Có | Glossary pressure/traction/N/proxy/model, khác miền được giữ. |
| 12 | Có | Glossary cuối và chuyển bibliography; thụt treo, citation không mồ côi. |
| 13 | Có | Bibliography còn lại [6]…[13], M23 năm/DOI và GUM không DOI; trang cuối đầy đủ. |

Kết xuất bằng Microsoft Word16.0 build16.0.20430, read-only=True, exit code0. PDF SHA-256 `8b35c8beca32dd1edbf8963c56a1b1cd00c681e19c7cc9b5abe806a6fa27591c`. Tệp PDF,13 PNG, scripts và JSON QA ở scratch `/tmp/MP1-CH2-2.2-INTEGRATION-89efai4_`, không là deliverable thứ tám. Bản sao Windows ở `C:\Users\khanh\AppData\Local\Temp\MP1-CH2-2.2-INTEGRATION-89efai4_`; Word đóng bản sao không lưu và thoát. Font text layer chỉ TimesNewRomanPSMT/TimesNewRomanPS-BoldMT. Không dùng ảnh render để sửa nhãn khoa học.

## Giới hạn và thẩm quyền


1. §2.2.1 giữ lịch sử xung đột locator M03-E02. WEP/registry cũ ghi PDF vật lý 3, §1.2/Table 1; các đoạn thực dùng ở PDF 1/9 trong baseline được giữ với nhãn `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID` khi chưa có ID đăng ký. Tác vụ này không sửa registry và không gán lại ID cũ.
2. §2.2.2 kế thừa việc kiểm các trang/đoạn thực dùng, không phải kiểm toàn bộ từng bài. Bằng chứng trùng dữ liệu hoặc dùng lại không trở thành các lần xác nhận độc lập.
3. §2.2.3 giữ provenance hiệu chỉnh trực tiếp của M23-E06: locator WEP cũ PDF 2 khác đoạn thực dùng PDF vật lý 3/trang in 3. Các locator M38-E02/E03 giữ trang vật lý/trang in đã ghi trong baseline. Không đổi citation để che khác biệt locator.
4. M38-E04 không được tự gán để hỗ trợ claim về U ngoài locator của record. Giữ `SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID` cho đoạn đã kiểm trong baseline mà chưa có ID đăng ký. Không tạo Evidence ID mới.
5. M23 có năm tạp chí 2021, công bố trực tuyến 2020 và DOI chứa 2020; target giữ nguyên văn mục tham khảo được nghiệm thu. `source_registry_year=2020` và `source_year=2021` cùng được bảo toàn trong Citation Map. M38 là JCGM 100:2008, không gán DOI.
6. Phân loại `VERIFIED FULL TEXT`/`VERIFIED_SELECTED_PDF_PASSAGE`, `METADATA ONLY` nếu có, và `INFERENCE` là trạng thái của hồ sơ nguồn được kế thừa theo từng record, không phải tuyên bố đã tái kiểm mọi PDF trong lần tích hợp. Kiểm checksum, metadata, anchor và khả năng bảo toàn nội dung không thay thế đọc lại nguồn khoa học.
7. Các baseline nguồn chưa được xác nhận trực tiếp trên Microsoft Word. Bản tích hợp hiện tại đã được mở chỉ đọc và xuất PDF bằng Microsoft Word 16.0, build 16.0.20430; điều này chỉ xác nhận artifact và môi trường nêu trên, không xác nhận mọi phiên bản Word hoặc thao tác chỉnh sửa/lưu lại. Không có LibreOffice trong runtime hiện tại; không cài thêm.
8. Hình là `AUTHOR_CONCEPTUAL_SCHEMATIC`, không phải thiết kế MP1. Hình học, ánh xạ áp suất–tải tiếp xúc, miền TiNi, metric/bất định và phạm vi SMA–piston vẫn chờ con người. Không đóng protocol, không phê duyệt Bench.
9. Backend mô hình không có telemetry xác nhận. Các tên mô hình đã gửi trong lệnh phân công không được coi là bằng chứng backend thực chạy. Ba worker cùng phục vụ `SELF_REVIEW_ONLY`, không thay nghiệm thu độc lập.


FINAL_SELF_REVIEW_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS
NEXT_ACTION: AWAIT_INDEPENDENT_ACCEPTANCE

## Mã kiểm tái lập chỉ đọc

Lưu mã sau ngoài thư mục final và chạy bằng Python có python-docx. Mã dùng bảy deliverables và baseline trong workspace, không phụ thuộc scratch, không ghi hoặc sửa tệp. Đây là kiểm cấu trúc/bảo toàn/anchor, không thay người đọc nguồn và kiểm tra trực quan.

```python
from pathlib import Path
from collections import Counter
import csv, json, re, hashlib, zipfile
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import _Cell
from docx.oxml.ns import qn

root = Path('/home/khanh/projects/mechanical-research-agents')
out = root / 'outputs/thesis_drafts/chapter_2/section_2_2_integrated'
prefix = 'MP1_CH2_2_2_'
read = lambda p: list(csv.DictReader(p.open(encoding='utf-8-sig', newline='')))
claims = read(out / (prefix + 'MASTER_SOURCE_TRACEABILITY.csv'))
terms = read(out / (prefix + 'MASTER_TERMINOLOGY.csv'))
refs = read(out / (prefix + 'CITATION_RENUMBERING_MAP.csv'))
docx = out / (prefix + 'INTEGRATED.docx')
assert hashlib.sha256(docx.read_bytes()).hexdigest() == '701f40942456a880d82163a05d5de545b24e9b07d2651c93723a0a9c6c6e8b34'
doc = Document(docx)
containers = {}
section = ''
for el in doc.element.body:
    if el.tag == qn('w:p'):
        text = Paragraph(el, doc).text
        if re.match(r'^2\.2\.[123]\. ', text): section = text.split('. ')[0]
        if text == 'Bảng thuật ngữ của mục 2.2': section = '2.2.glossary'
    for mark in el.xpath('.//w:bookmarkStart'):
        parent = mark.getparent()
        cells = parent.xpath('ancestor::w:tc')
        shapes = parent.xpath('.//wp:docPr')
        text = _Cell(cells[0], doc).text if cells else shapes[0].get('descr') if shapes else Paragraph(parent, doc).text
        containers[mark.get(qn('w:name'))] = (text, section)
assert len(claims) == len({r['target_master_claim_id'] for r in claims}) == 226
source_claims = {}
source_terms = {}
renumber = {(r['source_section'], r['source_reference_number']): r['target_reference_number'] for r in refs}
convert = lambda text, sec: re.sub(r'\[(\d+)\]', lambda m: '[' + renumber[(sec, m[1])] + ']', text)
body_count = 0
for sec in ['2.2.1', '2.2.2', '2.2.3']:
    folder = root / 'outputs/thesis_drafts/chapter_2' / ('section_' + sec.replace('.', '_'))
    stem = 'MP1_CH2_' + sec.replace('.', '_')
    source_claims[sec] = {r['claim_id']: r for r in read(folder / (stem + '_SOURCE_TRACEABILITY.csv'))}
    source_terms[sec] = {r['term_id']: r for r in read(folder / (stem + '_TERMINOLOGY.csv'))}
    source_doc = Document(folder / (stem + '_DRAFT.docx'))
    index = 0
    for paragraph in source_doc.paragraphs[1:]:
        if paragraph.text.startswith('Bảng thuật ngữ'): break
        if not paragraph.text or paragraph.text.startswith(('Hình 2.2.3-1.', 'Bảng 2.2.3-1.')): continue
        index += 1
        pid = ('P%02d' if sec == '2.2.2' else 'P%03d') % index
        text, actual_sec = containers['MP1_' + sec.replace('.', '') + '_' + pid]
        assert actual_sec == sec and text == convert(paragraph.text, sec)
        body_count += 1
for row in claims:
    original = source_claims[row['source_section']][row['source_original_claim_id']]
    assert json.loads(row['source_original_record_json']) == original
    assert all(row['source_csv__' + k] == value for k, value in original.items())
    text, sec = containers[row['target_element_id']]
    assert sec == ('2.2.glossary' if row['target_anchor_container'] == 'GLOSSARY_CELL' else row['source_section'])
    a, b = int(row['target_anchor_start']), int(row['target_anchor_end'])
    assert text[a:b] == row['target_manuscript_anchor'] == convert(original['manuscript_anchor'], row['source_section'])
lineage = []
for term in terms:
    r = doc.tables[1].rows[int(term['target_glossary_row'])]
    assert [c.text for c in r.cells] == [term[k] for k in ['word_term_text', 'word_definition_and_context', 'word_source_text']]
    for original in json.loads(term['source_original_rows_json']):
        sec = original['source_section']
        assert {k: v for k, v in original.items() if k != 'source_section'} == source_terms[sec][original['term_id']]
        lineage.append((sec, original['term_id']))
assert len(terms) == 33 and len(lineage) == len(set(lineage)) == 35
occurrences, bibliography, in_bib = [], [], False
for el in doc.element.body:
    text = ''.join(el.xpath('.//w:t/text()'))
    if text == 'Tài liệu tham khảo': in_bib = True; continue
    if in_bib:
        if text: bibliography.append(int(re.match(r'\[(\d+)\]', text)[1]))
    else: occurrences += [int(x) for x in re.findall(r'\[(\d+)\]', text)]
assert len(occurrences) == 71 and list(dict.fromkeys(occurrences)) == bibliography == list(range(1, 14))
assert len(refs) == 16 and len({r['source_paper_id'] for r in refs}) == 13
assert len({r['source_doi'].lower() for r in refs if r['source_doi']}) == 12
for row in refs:
    for loc in json.loads(row['target_integrated_locations']):
        el = doc.element.body[int(loc['element'])]
        paragraphs = [el] if el.tag == qn('w:p') else el.xpath('.//w:p')
        text = Paragraph(paragraphs[int(loc['paragraph'])], doc).text
        assert text[int(loc['start']):int(loc['end'])] == loc['text']
    for loc in json.loads(row['citation_occurrence_lineage_json']):
        text = containers[loc['target_element_id']][0]
        assert text[loc['target_offset_start']:loc['target_offset_end']] == '[' + row['target_reference_number'] + ']'
assert len(doc.tables) == 2 and [len(t.rows) for t in doc.tables] == [6, 34]
for table in doc.tables:
    assert len(table.columns) == 3
    assert len(table.rows[0]._tr.xpath('./w:trPr/w:tblHeader')) == 1
    assert all(len(r._tr.xpath('./w:trPr/w:cantSplit')) == 1 for r in table.rows)
with zipfile.ZipFile(docx) as z:
    assert z.testzip() is None
    media = [n for n in z.namelist() if n.startswith('word/media/')]
    assert len(media) == 1
    assert hashlib.sha256(z.read(media[0])).hexdigest() == '26db28e4b1ff2d51a4be4f140dbf082ef8817301e7cfcbc9d955177409784b8f'
assert body_count == 34 and len(list(out.iterdir())) == 7
print('PASS: 34 đoạn; 226 anchor; 35 lineage thuật ngữ; 71 citation; 13 tham khảo; 1 hình; 2 bảng; 7 tệp.')

```
