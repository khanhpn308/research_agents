# Báo cáo thực hiện tiểu mục 2.2.3, Chương 2 của MP1

Bộ tài liệu là bản thảo luận văn bằng tiếng Việt trong phạm vi đã giới hạn. Nội dung khoa học đầy đủ nằm trong DOCX; hai CSV lưu truy xuất ở cấp câu và thuật ngữ. Không thay đổi trạng thái nghiên cứu, sổ đăng ký hoặc vòng kiểm chứng.

## TASK_ID
MP1-CH2-2.2.3-RESEARCH-THESIS-DRAFT

## STATUS
COMPLETED_WITH_DOCUMENTED_LIMITATIONS

## OFFICIAL_HEADING
2.2.3. Áp suất cấp và lực pháp tuyến

## OUTLINE_SHA256
18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e

## OUTLINE_PHYSICAL_PAGE
11

## OUTLINE_BULLETS
[
  "Đặt áp suất là input hoặc traction boundary, không đồng nhất ngay với lực pháp tuyến giữa một cặp dây.",
  "Đưa sơ đồ truyền lực từ nguồn áp suất, màng hoặc ống bao, mạng tiếp xúc đến response M–κ.",
  "Chỉ ra biến nào đo trực tiếp, biến nào là proxy và biến nào cần calibration."
]

## WORKSPACE
/home/khanh/projects/mechanical-research-agents

## BRANCH
main

## HEAD
e66bb2f2339006e763cd60687cfc24680b945d97

## ROOT_MODEL_REQUESTED
GPT-6.1 Sol High

## ROOT_MODEL_ACTUAL
NOT_BACKEND_VERIFIABLE

## WORKER_MODEL_REQUESTED
Sol Medium

## WORKER_MODEL_ACTUAL
NOT_BACKEND_VERIFIABLE

## PARALLEL_DISPATCH_STATUS
DISPATCHED_CONCURRENTLY_WITH_WORKSTREAM_A

## WORKSTREAM_START_TIME
2026-10-20T07:44:46Z

## WORKSTREAM_END_TIME
2026-10-20T07:58:46Z

## CONCURRENCY_VERIFICATION_METHOD
Theo biên nhận điều phối và các mốc thời gian được điều phối viên lưu: B bắt đầu 07:44:46Z; A bắt đầu 07:43:38Z và kết thúc 07:51:47.263992Z. Hai khoảng giao nhau 421.263992 giây. Điều phối viên cũng quan sát cả hai tác vụ ở trạng thái RUNNING. Đây là ghi nhận lưu trữ của lượt gốc, không phải sự kiện được tái tạo trong lượt tiếp tục; không khẳng định sai số của hai người soạn độc lập.

## REVIEW_AUTHORITY
SELF_REVIEW_ONLY

## AUTHOR_APPROVAL_STATUS
HUMAN_APPROVAL_PENDING

## WEP_READINESS_STATUS
BOUNDED_WRITING_READY

## WEP_SOURCE_BINDINGS
§2.2.3 = BOUNDED_WRITING_READY trong 09/11. B01–B03 đều SUPPORTED_WITH_LIMITATIONS trong01. Bindings WEP chính M06-E02; M13-E02; M23-E06; M34-E09. Bổ sung đúng vai trò M13-E01, đoạn PDF9/10 chưa có ID riêng, M38-E02/E03 và các đoạn GUM chưa có ID riêng để làm rõ nhận dạng/đo/bất định. Không đặt quota nguồn.

## WEP_EVIDENCE_GAPS
Chưa có ánh xạ áp suất sang lực pháp tuyến cho MP1, lựa chọn cảm biến, phép đo traction cục bộ thực tế, ngân sách độ không đảm bảo định lượng hoặc giao diện đã chốt. Trạng thái sẵn sàng chỉ cho phép viết trong phạm vi giới hạn. M23-E06: WEP ghi PDF2 nhưng fragment thực tại PDF vật lý3, trang in3, §2.1 tiếp nối trước §2.2. M23: năm tạp chí2021, online2020, DOI chứa2020. M38-E02: §4.1.1 là vật lý20/trang in8 và Eq.(1), không phải vật lý8/Eq.(4) như record. M38-E03: §5.2 và Eq.(13) ở vật lý33/trang in21; record vật lý18 không đúng cho covariance. M38-E04 không được gán cho claim U vì record locator không khớp; dùng đoạn trực tiếp vật lý19/in7 với SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID. M34-E09 hỗ trợ phần static-head/operation tại PDF12; không dùng Table3 hoặc số liệu bảng để tránh gộp locator. Không sửa nguồn canonical.

## SOURCE_PAPERS
[
  "M06",
  "M13",
  "M23",
  "M34",
  "M38"
]

## VERIFIED_PDFS
5

## PDF_PAGES_DIRECTLY_VERIFIED
{
  "claim_pages_used": [
    [
      "M06",
      5
    ],
    [
      "M13",
      1
    ],
    [
      "M13",
      3
    ],
    [
      "M13",
      9
    ],
    [
      "M13",
      10
    ],
    [
      "M23",
      3
    ],
    [
      "M34",
      12
    ],
    [
      "M38",
      17
    ],
    [
      "M38",
      18
    ],
    [
      "M38",
      19
    ],
    [
      "M38",
      20
    ],
    [
      "M38",
      33
    ]
  ],
  "identity_pages": "Trang vật lý 1 của cả năm PDF; M23 kiểm thêm trang 2–3 và dòng xuất bản ở trang 1; GUM kiểm hình trang vật lý 20/33 để phân biệt số trang PDF và số trang in.",
  "boundary": "Chỉ các trang và đoạn được chọn, không phải toàn bộ PDF."
}

## EVIDENCE_IDS
[
  "M06-E02",
  "M13-E01",
  "M13-E02",
  "M23-E06",
  "M34-E09",
  "M38-E02",
  "M38-E03"
]

## REGISTERED_EVIDENCE_ID_COUNT
7

SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID là dấu trạng thái cho đoạn nguồn đã kiểm nhưng chưa có mã đoạn được đăng ký, không phải mã bằng chứng thứ tám. Hai CSV giữ nguyên dấu này để bảo toàn truy xuất.

## BODY_PARAGRAPHS
12

## CLAIM_RECORDS
113

## UNRESOLVED_ANCHORS
0

## TERMINOLOGY_ENTRIES
13

## REFERENCES
5

## UNIQUE_DOIS
4

## CITATION_OCCURRENCES
{
  "body": 12,
  "glossary": 4
}

## ORPHAN_CITATIONS
0

## ORPHAN_REFERENCES
0

## SCIENTIFIC_TABLES
1

## GLOSSARY_TABLES
1

## FIGURES
1

## OMML_EQUATIONS
0

## B01_COVERAGE
PASS: P001–P005 nêu quy ước áp suất và phân biệt tải với tiếp xúc.

## B02_COVERAGE
PASS: P006/FIG01/CAP01/P007. Sơ đồ khái niệm do tác giả tổng hợp có hai mạch riêng, được nhúng ở độ phân giải 450 dpi với chiều rộng 15.8 cm.

## B03_COVERAGE
PASS: P009–P012; bảng Word ba cột phân biệt có điều kiện biến đo trực tiếp, đại lượng thay thế, biến suy ra, hiệu chuẩn và biến chưa quan sát.

## SCIENTIFIC_BOUNDARIES
Không chốt luật MP1 hoặc đồng nhất các loại áp suất; không chuyển kết luận giữa vật liệu hoặc cấu trúc tiếp xúc; không khẳng định độ cứng tăng đơn điệu phổ quát. Không bịa vị trí, đặc tính cảm biến, tốc độ hoặc ngân sách độ không đảm bảo. Khớp đáp ứng toàn cục chưa xác định được traction cục bộ.

## P3_STATUS_PRESERVATION
H0a=REFUTED_IN_TRANSFORMATION_REGIME chỉ trong miền chuyển pha; H0b=NOT_FALSIFIED_LIVE_COMPETITOR; H1=INSUFFICIENT_EVIDENCE. G00 đã đóng; G01–G08 có điều kiện; G09 là điều kiện tiên quyết; G10 chưa được xác lập; G11 không được dùng làm tuyên bố mới. Không sửa nguồn chuẩn.

## RQ_MAPPING_STATUS
PROVISIONAL_MANY_TO_MANY/HUMAN_DECISION_PENDING; năm câu hỏi nghiên cứu trong PDF so với bốn nhóm P3.

## PENDING_HUMAN_DECISIONS
[
  "hình học và cấu trúc tiếp xúc",
  "ánh xạ áp suất sang lực pháp tuyến và đại lượng thay thế",
  "trạng thái TiNi, nhiệt độ, tốc độ và lịch sử tải",
  "đại lượng độ cứng và độ không đảm bảo",
  "vai trò SMA và piston"
]

## CROSS_SECTION_TERMINOLOGY_FINDINGS
Giữ E[Pa], B/EI[N·m²], K[N/m hoặc N/mm], M[N·m], κ[m⁻¹]. σ_n và p_n ở mục 2.5 cùng biểu diễn loại traction pháp tuyến cục bộ theo quy ước đã nêu; áp suất nguồn và áp suất gần mẫu là các biến riêng.

## CROSS_WORKSTREAM_FINDINGS
CW-01; DIFFERENT_VALID_DOMAINS_RESOLVED_WITHOUT_MANUSCRIPT_CHANGE

## RESOLUTION_STATUS
DIFFERENT_VALID_DOMAINS_RESOLVED_WITHOUT_MANUSCRIPT_CHANGE

## BASELINES_UNCHANGED
{
  "section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx": "9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba",
  "section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
  "section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
  "section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
  "section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b"
}

## INPUT_CHECKSUMS_UNCHANGED
597/597; không có thay đổi. Danh sách kiểm tra đầy đủ ở dưới.

## GIT_CHANGE_SCOPE
10 tệp bàn giao cuối được cho phép và 1 tệp khóa kiểu Word quan sát được ngoài phạm vi ghi và bàn giao, chưa được quy nguồn gốc và được giữ nguyên. B chỉ ghi năm tệp thuộc phạm vi B; hai tệp đã sửa cùng 363 mục chưa được theo dõi từ trước được bảo toàn.

Điều phối viên quan sát phần tăng thêm so với trạng thái gốc gồm 10 tệp bàn giao được cho phép và một tệp khóa kiểu Word ngoài phạm vi ghi và phạm vi bàn giao: outputs/thesis_drafts/chapter_2/section_2_3_integrated/~$1_CH2_2_3_INTEGRATED.docx. Tệp khóa có kích thước 162 byte, ctime và mtime 2026-10-20T08:34:39Z, không có trong trạng thái gốc 365 mục hoặc ảnh chụp trạng thái tiếp tục 375 mục. ORIGIN: NOT_ATTRIBUTED. Không xóa hoặc sửa tệp khóa này; giữ nguyên thay đổi có thể do hoạt động đồng thời. Các lệnh B trong lượt tiếp tục không mở DOCX nền bằng Word hoặc LibreOffice và không nhắm ghi tệp khóa; không đủ bằng chứng để quy nguồn gốc của nó. Theo kiểm tra của điều phối viên, cả 597 đầu vào và các DOCX nền vẫn khớp băm; phần khác biệt đã theo dõi và vùng chờ Git không đổi. Đây là giới hạn bảo toàn hiện trạng, không phải xung đột khoa học P1/P2.

## DOCX_SHA256
3b9cb65a0a2566d9ed44af6fd2e3c3d9c5891f5cf2d82b423f40bdaad8ac69ce

## DOCX_ZIP_XML_STATUS
PASS: CRC của ZIP hợp lệ; phân tích được 13 phần XML; đích liên kết ảnh nhúng tồn tại; không có ảnh ngoài.

## WORD_RENDER_VALIDATION
PASS: LibreOffice 24.2.7.2 kết xuất DOCX sau sửa, tiến trình kết thúc với mã 0 trước khi đọc PDF. Người soạn đã mở và xem riêng cả năm ảnh trang mới. Có cảnh báo javaldx và dữ liệu liblangtag; xuất PDF vẫn thành công.

## RENDERED_PAGES
5

## PAGES_VISUALLY_REVIEWED
[
  1,
  2,
  3,
  4,
  5
]

## MICROSOFT_WORD_VALIDATION
NOT_PERFORMED

## P1_P2_UNRESOLVED
0

## DOCUMENTED_LIMITATIONS
Tự rà soát; chưa được tác giả/người hướng dẫn phê duyệt. Microsoft Word chưa được kiểm trực tiếp. Chỉ kiểm các đoạn/trang PDF được sử dụng, không tuyên bố đã kiểm toàn bộ năm PDF. Sơ đồ là khái niệm của tác giả, không phải thiết kế hoặc sơ đồ cảm biến MP1 đã chốt. Quan hệ p-to-N và các quyết định khoa học MP1 vẫn mở.

## FILES_CREATED
[
  "MP1_CH2_2_2_3_DRAFT.docx",
  "MP1_CH2_2_2_3_SOURCE_TRACEABILITY.csv",
  "MP1_CH2_2_2_3_TERMINOLOGY.csv",
  "MP1_CH2_2_2_3_7_GATE_REVIEW.md",
  "MP1_CH2_2_2_3_EXECUTION_REPORT.md"
]

## COMMIT_STATUS
NOT_PERFORMED

## PUSH_STATUS
NOT_PERFORMED

## FINAL_SELF_REVIEW_DECISION
READY_AS_BOUNDED_DRAFT_CANDIDATE; NOT_AUTHOR_APPROVED

## NEXT_ACTION
AWAIT_TWO_INDEPENDENT_ACCEPTANCES

Điều phối viên theo dõi hai chấp nhận độc lập riêng; hỗ trợ rà soát hiện tại không được tính là chấp nhận độc lập. Các quyết định khoa học và phê duyệt của tác giả vẫn chờ.

## GATE_1
PASS

## GATE_2
PASS_WITH_DOCUMENTED_LIMITATIONS

## GATE_3
PASS_WITH_DOCUMENTED_LIMITATIONS

## GATE_4
PASS

## GATE_5
PASS_WITH_DOCUMENTED_LIMITATIONS

## GATE_6
PASS_WITH_DOCUMENTED_LIMITATIONS

## GATE_7
PASS_WITH_DOCUMENTED_LIMITATIONS

## Danh sách nguồn và kiểm tra các đoạn được sử dụng

M23-E06: WEP ghi PDF2 nhưng fragment thực tại PDF vật lý3, trang in3, §2.1 tiếp nối trước §2.2. M23: năm tạp chí2021, online2020, DOI chứa2020. M38-E02: §4.1.1 là vật lý20/trang in8 và Eq.(1), không phải vật lý8/Eq.(4) như record. M38-E03: §5.2 và Eq.(13) ở vật lý33/trang in21; record vật lý18 không đúng cho covariance. M38-E04 không được gán cho claim U vì record locator không khớp; dùng đoạn trực tiếp vật lý19/in7 với SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID. M34-E09 hỗ trợ phần static-head/operation tại PDF12; không dùng Table3 hoặc số liệu bảng để tránh gộp locator. Không sửa nguồn canonical.

M06 cung cấp bối cảnh tổng quan thứ cấp; M13 là nghiên cứu gốc về kẹt sợi để đối chiếu; M23 cung cấp mô hình cáp và giới hạn; M34 cung cấp bối cảnh bộ tạo áp suất; M38 là hướng dẫn đo lường gốc. Không nguồn nào thay thế bằng chứng về giao diện MP1. Lượt gốc đã đọc trực tiếp văn bản bằng PyMuPDF và kết xuất các trang, hình được chọn. CSV nguồn ghi đúng trang và đoạn hỗ trợ từng bản ghi. Đoạn chưa có mã bằng chứng đã đăng ký được ghi SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID, không tạo mã giả.

{
  "M06": {
    "path": "data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf",
    "sha": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
    "citation": "1"
  },
  "M13": {
    "path": "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf",
    "sha": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
    "citation": "2"
  },
  "M23": {
    "path": "data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf",
    "sha": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a",
    "citation": "3"
  },
  "M34": {
    "path": "data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf",
    "sha": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
    "citation": "4"
  },
  "M38": {
    "path": "data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf",
    "sha": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
    "citation": "5"
  }
}

## Nguồn gốc sơ đồ và bản kết xuất

Lượt gốc tạo sơ đồ trong thư mục tạm bằng các phần tử hình học Python/Pillow, không dùng ảnh AI hoặc sao chép hình nguồn. Dùng PNG vì khi đó chưa cài công cụ kết xuất vectơ. SHA256 ảnh PNG nhúng: 26db28e4b1ff2d51a4be4f140dbf082ef8817301e7cfcbc9d955177409784b8f. Các nhãn và chú thích mang trạng thái AUTHOR_CONCEPTUAL_SCHEMATIC. Cả 14 điểm neo của nhãn và ghi chú nằm nguyên văn trong văn bản thay thế của hình ở XML; chú thích là đoạn Word. Mã kiểm tra tái chạy kiểm các liên kết hình.

Đường dẫn kết xuất lịch sử của lượt gốc: /tmp/mp1-222-223-epok9rg6/B/render/MP1_CH2_2_2_3_DRAFT.pdf và final-p1.png đến final-p5.png. Thư mục tạm này đã mất khi tiếp tục phiên; không dùng nó làm bằng chứng kiểm tra hiện tại. Việc tái chạy kiểm CSV, Word, nguồn và danh sách băm không phụ thuộc thư mục cũ. Hồ sơ LibreOffice và thư mục kết xuất mới thuộc riêng B. Chưa kiểm kết xuất bằng Microsoft Word.

## Số liệu kiểm tra
```json
{
  "body_paragraphs": 12,
  "claim_records": 113,
  "categories": {
    "DEFINITION_OR_CONVENTION": 50,
    "AUTHOR_SYNTHESIS": 31,
    "SOURCE_GROUNDED_CLAIM": 10,
    "CROSS_STUDY_INFERENCE": 6,
    "AUTHOR_CONCEPTUAL_SCHEMATIC": 15,
    "PENDING_HUMAN_DECISION": 1
  },
  "body_claim_records": 43,
  "source_fragment_checks": 36,
  "terminology_entries": 13,
  "unresolved_anchors": 0,
  "references": 5,
  "unique_dois": 4,
  "citation_occurrences_body": 12,
  "citation_occurrences_glossary": 4,
  "orphan_citations": 0,
  "orphan_references": 0,
  "scientific_tables": 1,
  "glossary_tables": 1,
  "figures": 1,
  "omml_equations": 0,
  "source_papers": [
    "M06",
    "M13",
    "M23",
    "M34",
    "M38"
  ],
  "evidence_ids": [
    "M06-E02",
    "M13-E01",
    "M13-E02",
    "M23-E06",
    "M34-E09",
    "M38-E02",
    "M38-E03"
  ],
  "registered_evidence_id_count": 7,
  "evidence_status_markers": [
    "SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID"
  ],
  "docx_sha256": "3b9cb65a0a2566d9ed44af6fd2e3c3d9c5891f5cf2d82b423f40bdaad8ac69ce",
  "image_sha256": "26db28e4b1ff2d51a4be4f140dbf082ef8817301e7cfcbc9d955177409784b8f",
  "source_pages_used": [
    [
      "M06",
      5
    ],
    [
      "M13",
      1
    ],
    [
      "M13",
      3
    ],
    [
      "M13",
      9
    ],
    [
      "M13",
      10
    ],
    [
      "M23",
      3
    ],
    [
      "M34",
      12
    ],
    [
      "M38",
      17
    ],
    [
      "M38",
      18
    ],
    [
      "M38",
      19
    ],
    [
      "M38",
      20
    ],
    [
      "M38",
      33
    ]
  ],
  "shared_inputs_checked": 597,
  "shared_inputs_changed": [],
  "xml_parts": 13
}
```

## Mã tự chứa để tái chạy kiểm tra
Chạy từ thư mục gốc kho mã với python-docx, lxml và pymupdf. Trích khối Python dưới đây ra một tệp tạm rồi chạy. Mã chỉ đọc năm tệp bàn giao, PDF và bản ghi nguồn chuẩn cùng danh sách băm đầu vào nhúng. Độ phủ ký tự chỉ xác nhận điểm neo về mặt kỹ thuật; mức hỗ trợ ngữ nghĩa được tự rà soát riêng. Mã không chứng nhận tính đúng khoa học, tính mới, phê duyệt của tác giả hoặc khả năng dự báo của mô hình.

```python
import csv,json,re,zipfile,hashlib,unicodedata
from pathlib import Path
from collections import Counter
from lxml import etree
from docx import Document
import pymupdf
ROOT=Path.cwd()
OUT=ROOT/'outputs/thesis_drafts/chapter_2/section_2_2_3';PRE='MP1_CH2_2_2_3_'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def norm(t):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',t).replace('−','-')).strip()
def check():
 d=Document(OUT/(PRE+'DRAFT.docx'));paras=[p.text for p in d.paragraphs]
 assert paras[0]=='2.2.3. Áp suất cấp và lực pháp tuyến'
 assert 'Bảng thuật ngữ dùng trong tiểu mục' in paras
 assert not any('N_i = p_source' in s for s in paras)
 rows=list(csv.DictReader((OUT/(PRE+'SOURCE_TRACEABILITY.csv')).open(encoding='utf-8-sig')))
 terms=list(csv.DictReader((OUT/(PRE+'TERMINOLOGY.csv')).open(encoding='utf-8-sig')))
 assert len({r['claim_id'] for r in rows})==len(rows)
 z=zipfile.ZipFile(OUT/(PRE+'DRAFT.docx'));assert z.testzip() is None
 for n in z.namelist():
  if n.endswith('.xml') or n.endswith('.rels'):etree.fromstring(z.read(n))
 x=etree.fromstring(z.read('word/document.xml'));ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
 assert not x.findall('.//w:headerReference',ns) and not x.findall('.//w:footerReference',ns)
 alt=x.find('.//wp:docPr',ns).get('descr');assert alt.startswith('AUTHOR_CONCEPTUAL_SCHEMATIC')
 embeds=x.findall('.//a:blip',ns);assert len(embeds)==1
 rels=etree.fromstring(z.read('word/_rels/document.xml.rels'))
 rid=embeds[0].get('{'+ns['r']+'}embed');rel=[a for a in rels if a.get('Id')==rid][0];assert rel.get('TargetMode')!='External'
 media='word/'+rel.get('Target');assert media in z.namelist();assert len(z.read(media))>20000
 assert len(d.tables)==2;assert len(d.tables[1].rows)==len(terms)+1
 assert d.tables[1].rows[0].cells[0].text=='Thuật ngữ Anh/Việt'
 for i,t in enumerate(terms,1):
  assert [c.text for c in d.tables[1].rows[i].cells]==[t['word_term_text'],t['word_definition_and_context'],t['word_source_text']]
 for table in d.tables:assert table.rows[0]._tr.find('.//'+ '{'+ns['w']+'}tblHeader') is not None
 body={};pdfs={};evidence={}
 for f in (ROOT/'outputs/literature/MP1_READING_PACK').glob('02_*/WP-*/EVIDENCE_RECORDS.jsonl'):
  for ln in f.read_text().splitlines():
   r=json.loads(ln);evidence[r['evidence_id']]=r
 for r in rows:
  anchor=r['manuscript_anchor'];pid=r['paragraph_id'];a,b=int(r['anchor_start']),int(r['anchor_end'])
  if r['anchor_container']=='body_paragraph':
   if pid not in body:
    candidates=[p for p in paras if p[a:b]==anchor];assert len(candidates)==1,(r['claim_id'],len(candidates));body[pid]=candidates[0]
   actual=body[pid]
  elif r['anchor_container']=='drawing_alt_text':actual=alt
  elif r['anchor_container']=='caption':
   hits=[p for p in paras if p==anchor];assert len(hits)==1;actual=hits[0]
  elif r['anchor_container']=='table_cell':
   m=re.fullmatch(r'(T1|G1)R(\d+)C(\d+)',pid);assert m
   actual=d.tables[0 if m[1]=='T1' else 1].rows[int(m[2])].cells[int(m[3])].text
  else:raise AssertionError(r['anchor_container'])
  assert actual[a:b]==anchor,r['claim_id']
  if r['canonical_pdf_path']:
   p=ROOT/r['canonical_pdf_path'];assert sha(p)==r['canonical_pdf_sha256']
   if str(p) not in pdfs:pdfs[str(p)]=pymupdf.open(p)
   pg=pdfs[str(p)][int(r['verified_physical_pdf_page'])-1]
   assert r['source_fragment'] and norm(r['source_fragment']) in norm(pg.get_text()),r['claim_id']
   if r['evidence_ids']!='SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID':
    assert r['evidence_ids'] in evidence
    er=evidence[r['evidence_ids']];assert er['paper_id']==r['canonical_paper_id'];assert er['source_sha256']==r['canonical_pdf_sha256']
  if r['claim_category']=='SOURCE_GROUNDED_CLAIM':assert r['canonical_pdf_path'] and r['evidence_class']=='VERIFIED FULL TEXT'
 for pid,text in body.items():
  covered=set()
  for r in rows:
   if r['anchor_container']=='body_paragraph' and r['paragraph_id']==pid:covered.update(range(int(r['anchor_start']),int(r['anchor_end'])))
  assert all(i in covered for i,c in enumerate(text) if not c.isspace()),pid
 assert len(body)==12
 ri=paras.index('Tài liệu tham khảo');refs=[s for s in paras[ri+1:] if s]
 btext='\n'.join(body[k] for k in sorted(body));cit=[int(n) for n in re.findall(r'\[(\d+)\]',btext)]
 assert list(dict.fromkeys(cit))==list(range(1,6));assert len(refs)==5;assert set(cit)==set(range(1,6))
 dois=re.findall(r'DOI: ([^\s]+)', '\n'.join(refs));assert len(dois)==len(set(dois))==4
 sec=d.sections[0]
 for actual,cm in [(sec.page_width,21),(sec.page_height,29.7),(sec.left_margin,3),(sec.right_margin,2),(sec.top_margin,2.5),(sec.bottom_margin,2.5)]:assert abs(actual.cm-cm)<.003
 assert d.styles['Normal'].font.name=='Times New Roman' and d.styles['Normal'].font.size.pt==12
 assert d.styles['Normal'].paragraph_format.line_spacing==1.15
 assert d.paragraphs[0].style.name=='Heading 3'
 assert not any('Theme' in k for rf in x.findall('.//w:rFonts',ns) for k in rf.attrib)
 assert all(c.get('{'+ns['w']+'}val')=='000000' for c in x.findall('.//w:color',ns))
 report=(OUT/(PRE+'EXECUTION_REPORT.md')).read_text();shared=json.loads(report.split('<!-- INPUT_MANIFEST_BEGIN -->'+chr(10)+chr(96)*3+'json'+chr(10),1)[1].split(chr(10)+chr(96)*3,1)[0]);changed=[p for p,h in shared.items() if not Path(p).is_file() or sha(p)!=h];assert not changed,changed
 output_manifest=json.loads(report.split('<!-- OUTPUT_MANIFEST_BEGIN -->'+chr(10)+chr(96)*3+'json'+chr(10),1)[1].split(chr(10)+chr(96)*3,1)[0])
 assert len(output_manifest)==4
 assert all(sha(OUT/name)==digest for name,digest in output_manifest.items())
 result={'body_paragraphs':len(body),'claim_records':len(rows),'categories':dict(Counter(r['claim_category'] for r in rows)),'body_claim_records':sum(r['anchor_container']=='body_paragraph' for r in rows),'source_fragment_checks':sum(bool(r['canonical_pdf_path']) for r in rows),'terminology_entries':len(terms),'unresolved_anchors':0,'references':len(refs),'unique_dois':len(dois),'citation_occurrences_body':len(cit),'citation_occurrences_glossary':sum(len(re.findall(r'\[(\d+)\]',t['word_source_text'])) for t in terms),'orphan_citations':0,'orphan_references':0,'scientific_tables':1,'glossary_tables':1,'figures':len(embeds),'omml_equations':len(x.findall('.//m:oMath',ns)),'source_papers':sorted({r['canonical_paper_id'] for r in rows if r['canonical_paper_id']}),'evidence_ids':sorted({r['evidence_ids'] for r in rows if r['evidence_ids'] and r['evidence_ids']!='SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID'}),'registered_evidence_id_count':len({r['evidence_ids'] for r in rows if r['evidence_ids'] and r['evidence_ids']!='SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID'}),'evidence_status_markers':sorted({r['evidence_ids'] for r in rows if r['evidence_ids']=='SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID'}),'docx_sha256':sha(OUT/(PRE+'DRAFT.docx')),'image_sha256':hashlib.sha256(z.read(media)).hexdigest(),'source_pages_used':sorted({(r['canonical_paper_id'],int(r['verified_physical_pdf_page'])) for r in rows if r['canonical_pdf_path']}),'shared_inputs_checked':len(shared),'shared_inputs_changed':changed,'xml_parts':sum(n.endswith('.xml') for n in z.namelist())}
 assert len(list(OUT.iterdir()))==5
 return result
if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))

```

## Danh sách băm đầu vào
Danh sách đầy đủ được ghi trước khi soạn, dùng để so sánh khi tái chạy; đường dẫn tuyệt đối giữ nguồn gốc lượt gốc.
<!-- INPUT_MANIFEST_BEGIN -->
```json
{
  "/home/khanh/projects/mechanical-research-agents/AGENTS.md": "bf6bd863326f85f1f77eeccaec10928439555b939a6701fd5134aec0a7abcd00",
  "/home/khanh/projects/mechanical-research-agents/docs/README.md": "ee87dd76eaf983521550499cc5662f64f331347cf0fab89af4cbe5cc285a5fc2",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_5_RESEARCH_GAP_AND_CONTRIBUTION_ADJUDICATION_2026-10-02.md": "253629f4e5811b5ca184415b7a0acb403dd9025238c8249f86bcde74d7af29e2",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_2_DEEP_SEARCH_AND_CORPUS_MAP_2026-10-02.md": "f60d89fcabbd5028ff92464b18fb469fdd909168888b170853f2ab0a3dd042b1",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md": "98cb37bc018a42fd5682964606a3ba0d66f43176c8d132778abcea2b5d3f1d2b",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/PDF_ANNOTATION_REPORT_2013_PUMP.md": "576548af10cc8409286e3d050c71269033aea24cb85661d6ad63ebd29d7efac3",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_2_ERRATA_S18_S20_2026-10-02.md": "97421ffa94a78835a8724e564877dc9753e0a8c9d7550d29dfcad8eebb77ebd6",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md": "4dd71b45f52a0e5bb18f92c3a76064aa4e395bc4a9feee19f827d6f463140f08",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/THESIS_READING_LIST_CURRENT_VI.md": "ce5b9d62da5efab09c702f2948565cf3ba901c36fff2f71a317eb5cd53a64f57",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md": "e5650636b3c8858394b619bf3f06386b65a9827bdf8e73d18f777144d57d6f7c",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_4_CROSS_STUDY_SYNTHESIS_A_GEMINI_2026-10-02.md": "d05459d657f90365f8465e9b3fa893cca1f72c8afa3cd1bb2aaf86558245f0d3",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_BULK_ANNOTATION_REPORT.md": "a72a2528b017b892d91ac10bdfb43013a11c2e0d92c8fc2a30d9d8e034b67c2b",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_4_CROSS_STUDY_SYNTHESIS_B_GPT_2026-10-02.md": "4a5793ef4e7df3d62b898d729cc1be7e1d60d738926b0faeabd985a65b75949d",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/LITERATURE_STRATEGY.md": "2a4853e7228c66273916db8e129ff2a42d76b76bae418e7f6e368ff644cd32f6",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_6_CHAPTER_2_DRAFTING_REPORT_2026-10-02.md": "29b65bcd2d8050f3a70c3e76ee3eed8bd845a47a8c3decb67d695c08097329ce",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md": "a948bd201fda61b29de142e40a95606cf47a7c83d05c2a81e7683db371e9453c",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md": "ca00e83f44803666f8ab7509ed585264cf88a1b980eac1be722e6c84af8c4195",
  "/home/khanh/projects/mechanical-research-agents/docs/learning/EVIDENCE_JSON_FRAMEWORK_GUIDE_VI.md": "f6b5a693936d2b50712114dc8518eb62c36e0f794e5e8bee265d7d8020b1772e",
  "/home/khanh/projects/mechanical-research-agents/docs/learning/CURRENT_RESEARCH_DIRECTION_TUTORIAL.md": "0fc9a203f1c09da57953dce55e5f7a3b48497bb9c31f91f8ec57b633a131d98e",
  "/home/khanh/projects/mechanical-research-agents/docs/learning/ZHANG_CONTINUUM_PAPERS_READING_GUIDE_VI.md": "db6358858352e5f2ef7f663000b2c45cb337e4a2257708ef945eee38db88095a",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx": "833344a5d64632ff9336832dbfccb2a8ae98dec45df046278e26d229b189ca9b",
  "/home/khanh/projects/mechanical-research-agents/docs/project/POST_D1_V009_RESEARCH_ROADMAP_VI.md": "43f43d17db00ac68917cccd23ebf1e4cfc4e9b61b569b85e711a1d5d7c9eaf2b",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_2026-10-02.md": "5b3ee8e1032de8909b0146ad3a1f826ad31a3f10fc9308107117d4424325d136",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_CHAPTERS_1_2_WORKING_DRAFT_2026-09-29_VI.md": "8ff36e2327b4a6de2f43a051a805646b648c91a7ff1d2e75e46ec552709bdeaa",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45",
  "/home/khanh/projects/mechanical-research-agents/docs/project/RESEARCH_STATE.md": "f302c37003601a20de6c148b5c84a6824618df4bcc9c34e5d09797ab3b1f3296",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_CLAIM_EVIDENCE_REPORT_TUTOR.md": "6136c4d4433675d471953f5683d9a82beff4b2a11749bec037f7318c9bec3587",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_MENTOR_FEEDBACK_RESCOPE_2026-09-29_VI.md": "8eadfc48b2d1b64443543f11c9993b538ecad3b9b90afdda80c07ea41f4c4a9c",
  "/home/khanh/projects/mechanical-research-agents/docs/project/PROJECT_HANDOFF_CURRENT.md": "b84cde745e54b6b7ab83fe7da67d8e31f4ca7c38533a2f2bd81dd16673658423",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx": "3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_CHAPTER_1_2_WRITING_PLAN_VI.md": "682554cc75d871bc050cc37bf478b2107356be67d0729c1771b05273a60355cd",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_THESIS_OUTLINE_AND_RESEARCH_MASTER_PROMPT_VI.md": "21ab597f5875bb2683913a9645bcbdca668186040789aa6a3e797173d8e94352",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_MENTOR_PIVOT_TUTOR.md": "df5a7edb7c71ebb8b20f9144164eed515c1f8811472bd9e61c396399fecc32be",
  "/home/khanh/projects/mechanical-research-agents/docs/project/POST_D1_V009_RESEARCH_ROADMAP.md": "d0aa08b8c7a42aa196d71ba65c63b619808452aa84922d19cf4a11e5717c2554",
  "/home/khanh/projects/mechanical-research-agents/docs/project/RESEARCH_LOG.md": "7cd88db0b06ee2a8ef01896412a469b0447dd83b7fbc8e8b21a8e3ce692cd575",
  "/home/khanh/projects/mechanical-research-agents/docs/project/research_state.json": "70b17fda40524a9e1c81231d6d969048cff5bcf0fc33052dffd85f75eaf58c67",
  "/home/khanh/projects/mechanical-research-agents/docs/project/CURRENT_EXECUTION_SNAPSHOT.md": "f2a673fe397f879ba1c5fc1dcc55649855c2c876c430490e28e4a4519f813fa9",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1-V002_CURRENT_HANDOFF.md": "fe48c78ff4e7d4437c17dcc044caf98e8df963349b01853968c3235ec7a2d025",
  "/home/khanh/projects/mechanical-research-agents/docs/project/NEXT_SESSION_START_HERE.md": "f2ec58cbffef9b90c8d3c8640309f30ae1d42014cc1bd5b75b5a14f5ad635ace",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_MENTOR_PIVOT_CURRENT.md": "9eb6cd362729d7aa1ea6b0094c21f753b3c0f011d69b7c112aa4deedfd1df3f8",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MENTOR_PIVOT_STATUS.md": "b73c248cef5214fcae49261ae2506830d298922eeed10299976d407317bc9f7f",
  "/home/khanh/projects/mechanical-research-agents/docs/project/MP1_STATUS_AND_NEXT_STEPS_VI.md": "1a9b89f55d2ead283631215e300833928eb8c9bf97b85599fa594028ac043341",
  "/home/khanh/projects/mechanical-research-agents/docs/vocabularies/README.md": "ac25e61b8c8c0ec88f579b2002156b511b575be454cfda2a66b3ab0e543b8987",
  "/home/khanh/projects/mechanical-research-agents/docs/vocabularies/21-09-2026.md": "a548145d6a90999fed380ccfe072c22b48e41e0234de8c73fa3ca80e1a572b56",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_ASTRA_CRITIQUE_REMEDIATION_2026-09-25.md": "a0f15375f50caae6857fb2a865709186e4d37f17f923b66cb480182f060f41f7",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md": "f53f896801113150bd83e84d6c68dd542804fc65a619ae34fd568e7f7c276a99",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_ASTRA_SCIENTIFIC_CRITIQUE_2026-09-25.md": "271a15428e5c265e98dbc86bc7c924291e3911e3d592b3ba6d98f5712b510fcb",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.md": "5dbc563cb7028ce8cce94a746122636d3fd0b87abf364a5285992bce6a1d2adf",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_CITATION_COMPLIANCE_REPORT.md": "790eb32de83f705b32fa4e84037bcde72034d16e7698c3288e1a0810ec7fb64b",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/D1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.docx": "7bb4e70ed9a22954c482d7437143fd0112765d2cd7b11e4be6235e2308d244d5",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_MENTOR_NARROWING_REPORT_2026-09-26.md": "79726226bdb95e05f26c6f498c18d940b6c0c8af1750ab4e15253578c5e4fe17",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/D1_MENTOR_RESEARCH_NARROWING_REPORT.docx": "6c7e6c03ef055f49bd51bf613e87158e9d3d5c8e2e24686ad8079edba09ed984",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md": "af57cc6a53c38ea430b4369d6afe7df86f61956d3320d7ce3977f957f5de3145",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/D1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.md": "d767c51b3456fa7643205c7fdf65cfac9a71614bd582fdf1947d1d20f54fce61",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_DETAILED_SCIENTIFIC_EVIDENCE_REPORT_2026-09-25.md": "ea0c1794cfdcb86ddf375f3529edc052b371c06c9caa23d8ce32395cf829484a",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/D1_CITATION_COMPLIANCE_REPORT.md": "3647302e5cd490806a82eff663a71ca4bad0022d5bf2e850989582db6f1c2625",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1.docx": "492fcb11cd35f3f16d73c8e92576f9869a99d6edf373b13b7e8330393448479a",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_MENTOR_NARROWING_REPORT_2026-09-26.docx": "5445a557dbf65c61528ac8ad682ffbcff9ff65b23a2f0666dcfb8a7d6f4f0fb0",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_MENTOR_RESEARCH_NARROWING_REPORT_2026-09-26.docx": "681b22749518897bdb82f9cb90cfc2de5302c5227df2baf5b61f5f8f4c700bba",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/D1_MENTOR_RESEARCH_NARROWING_REPORT.md": "372ad663be8a811f17bbe17fe6023d9317e001339a6722af691f9bebe5ba619f",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/MP1_Matrix_paper.xlsx": "be204ad3029984cb6ad15379925f90c44ff9d5c6c4a8ae5b5e3e0810e844ff01",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/D1_FROM_54_PAPERS_TO_FALSIFICATION_SEARCH_VI.md": "fee718bb458caea0f47ba931955c3b14c58b05397dee147e9279a062f2989937",
  "/home/khanh/projects/mechanical-research-agents/docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md": "2d26d9cbd7883442428585de82b53b320f28a275937f94d724097a61723ac166",
  "/home/khanh/projects/mechanical-research-agents/docs/operations/KNOWN_ISSUES.md": "ae4db17709c0d7f5af82746c5a51aee6be03cb7d1513335e68d91212e3f1bfcb",
  "/home/khanh/projects/mechanical-research-agents/docs/research_design/M1_RESEARCH_ARCHITECTURE.md": "7bddda804bfafcc55011cd90c3a9983a245ba069868c61bb5b8c5a13b5b77f17",
  "/home/khanh/projects/mechanical-research-agents/docs/research_design/EXACT_MODEL_SELECTION.md": "9b9d85255d0c2f6b9a0a7b522af9c10cd93ef8befdbff242a730dbf8e2f90981",
  "/home/khanh/projects/mechanical-research-agents/docs/research_design/LAYER_JAMMING_MODEL_COMPARISON.md": "db8d8b6f81723b8fdeeed72dd2747b7b2c72dd7c04caff42cc98f0e76e164dc7",
  "/home/khanh/projects/mechanical-research-agents/docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md": "6b2e210b46791bf990075dc4d4e3ea58c266722aa418be39827ebf38d01de156",
  "/home/khanh/projects/mechanical-research-agents/docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md": "5f72a12e1052cda57e6f7e9d57a6f6e2311b118f6b0c49c24bf7a40cd253e30e",
  "/home/khanh/projects/mechanical-research-agents/docs/protocols/D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md": "b6d69e7ed922562ffaf91042fd450f3ac5fb64b32007a4604a4fa59050154476",
  "/home/khanh/projects/mechanical-research-agents/docs/protocols/MP1_NOVELTY_FALSIFICATION_ROADMAP.md": "cbdd30f5b35dc487d38b6182cb74eb7dfee95a23025b1654b4ab2607513d859c",
  "/home/khanh/projects/mechanical-research-agents/docs/protocols/D1-V003_LITERATURE_AUDIT_PLAN.md": "2078e6e9997c01d9c19ecd1f66d143bcebe55714454942c012d66ba8acf9b999",
  "/home/khanh/projects/mechanical-research-agents/docs/protocols/MP1-V001_CORE_PRIOR_ART_AUDIT_PLAN.md": "a4022362286cde0c6a5764ab0cea7e7c37449bec54059b3e56a592d43d1e0173",
  "/home/khanh/projects/mechanical-research-agents/docs/protocols/D1-V009_LATE_FOUND_ADJACENT_AUDIT_PLAN.md": "25dd679749a9a164a3297e0aeb773f5e818835c553d8b276da7c0d9a3149c574",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_assessments/YE_2024_PROJECT_RELEVANCE_VI.md": "04dfdb37b8137a51b549e6a416368e0f8bffdebe3b6ad6649b7b87e604a0f3eb",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/source_bundle.json": "23b198df73c98fa6cf89bbe03a81c48a3a2e48194c48a6b1946f96ebd0d8640b",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/paper-card.md": "b0e0e9a043be9b42adf5ccb2fa938a748ac7eb3cfb0d099ee67f673ce0d90e0c",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/audit-report.json": "5890257ca3c326fa4da9d1448650fcb2e70bdaaa0e3548c296f21512c803aa86",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-002.png": "a290a96bf1ca30a5b3ea2afabce4ae12a0569b776e084901a17288cc3fc3c211",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-010.png": "5afc5f0fbd64c618a8621ea8f6781904b46eee7f15b1b83ccddf4074678bcfd2",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-009.png": "2efb47c35fc6646b7aca05f2a107a2dc5c34e25ddaf72876c3bc2b2a184f5eae",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-001.png": "1d0756a27d8a7af2258a0e991cc76d2c2a097b9a0b571a7d4e8ef9c2904652a5",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-003.png": "be037131c4878e48fbead3a80ac7b501a34ddf6e9a1e1e4e5271f295e9e87c8e",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-005.png": "985ecdb2779b3e8ebcae6b19b8e9667508be4edeea3a01394e332a443fe7e647",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-006.png": "5337a360f54baa1f9249d8fb9b03c87052652eb7f1fac2e7ceb8e8ab4bced8e4",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-007.png": "c52366447df9ed885b1eca3461b0916ccf3c50746083bf8fdc9a08c20c579f99",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-004.png": "0b3e4cb9d9bd61cd99db094541841ad580ea0515625a21c8ad3c0ef3a9d10db6",
  "/home/khanh/projects/mechanical-research-agents/docs/literature/paper_cards/zhang_2025_continuum_beam/rendered-pages/page-008.png": "a69cd9d2b372f471ff595337abc27c3937427dd79e60ee7ad7c9c247f8fd3b94",
  "/home/khanh/projects/mechanical-research-agents/docs/project/almost done/LR-FORMATED.docx": "a63016590d98ff10636895166307603e2b3095ee5b632a30891b71c21190986c",
  "/home/khanh/projects/mechanical-research-agents/docs/reports/figures/mp1_narrative_narrowing_diagram.png": "c7da4dc36877f1695b2afe5932e252f6bcbf8bb8bfb36abc690ab9493313f3e4",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md": "72a9556ed438ef126da2d186add01b053970cae41df9b3e151d1b6e443621128",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv": "f3778953f446e71e61ae192a3021b02407b13c35b11df2d30ab5914da49181dc",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md": "d87a902881e1d5d2161172d2db700c261a8ba653af2f7cff1722ea5213206e19",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx": "35a6842cd1513cb2ac91328ebadc1de0feacb2c6d421c5c4170d7ddce3c7e4e5",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv": "ca606e7804945c1ac719f8088b4a9965525078033cced17e08364c45705a31b7",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx": "38be496eb71922f7165b916ac552f9b9bcb54dbfd94dc0f635acd55372ce793d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md": "bfedc08e96e0163ce64b75a967f6327e42e49bee87dad55fcf522f9747ea22db",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv": "7b3105acf012369a2c3a7ee4426ef66d457c874da38d2dd2d6fc8f518daed630",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv": "735c2ad438e0a2ae0c05e83483ed51b6aeba2e49e372d59dc89bf6c6d9f1c223",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md": "7d3b803e0d690dacd49997861769e218186b6719f11c2337b5ebff813864bfb3",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv": "5cf9d23f204943bd173b5f41d8df46c20c3197eae302d9656e8364bfdcd73c9b",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx": "8172cd2e8e1351d29a4fd170dedcce88af94eb0d44ff9b42b7e023b9059439da",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv": "c93f94ec90be90caca8f253d9951c9e2d8c108e252991797bb4b24da3bfa3169",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md": "d667a6a32337f5ee279e96a64b6a5941da2ad621138bf0661f4940d3a0ad5e52",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md": "c5b3e070aa748a2a458f809edcd183938177295ce76d13ff52c539bdbbc1690d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md": "91947d11eea09cac56f882936218d690458b1cbbbe431bd7f854be6a172ac9b7",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv": "08202df03396abf83a4d320b56bd91abface6535c0379c1b75ec0c4ff89f3649",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv": "f917c23d7dc2a404dbbbfa38874ede6dd10a50fac598cf7e3cfd880fdce83a2f",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md": "402f6fc7c9d279b6b0c1fb6af3d72c5d42d131eeb0d8994a61c71c21cbc902cb",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx": "6ded97f12de61cde7be319c865c3ea40cc6cbdc8d04e00cc648530ec718311a0",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx": "024ef04fdc572956de10464863aba7f1d3781811c63791625be9fec1c5262db1",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md": "256e03c47dedd7c4b65e2fe766b4c1cbbc60f63b1520b629b0948508108a4ab0",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv": "8b50e5a95a18931a56cf680f63ab0d48e1cc68694cbe47f1674b36d940fc12ec",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv": "baa4781a3e3486ba1999eb8bbbed4197658398b7626700035a111dbb25ce647b",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md": "ef0a5351270a7a6beacd568de56d721f9b01bb60e6155d4f31b7375a1c48faa2",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md": "675b612f8a73117fb6c775c1c741337fdcb5f5d79d8d36e86c22c06fe05d1aff",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx": "0a83c721da6b44d92038dc5905bf0aa1842fa63c660f6b5e58886ed9dc31f376",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv": "49b1601a3ed4c2a71cc361892b32024fddcdfbab33d75ebaa96b545bffdcb550",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv": "a2f4c50c447df93bf37bebb95c1381728f658aabb435ffa5e858ebe4c13131e7",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md": "543a25380b524439bcb97253e4531aefff28a6a50912b16a23e9815f154e98e9",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md": "1191dfd41f394d76ed933c3805c69ad4be1a47ac69e4494f19743a414696136a",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv": "d9bcd231bfb43ed223b8db6b270060196d5f485aa9f848cc5459d64ae857ba91",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx": "a58cf37dee216f2e193f9ee607fa15ba4987cf49b66c4a884dab895172ebf6d4",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md": "9f60f4434b1699bc38ad23fbe7f5e7ae8c816957f4885caae3cd83dd6c0d5d7b",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv": "dacb3c6ad632a1ec7e3aab167f614cddaa00c7a76850506616060c332eac7890",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv": "636a5acb7514ccd8309a6e786280252847bdbd5c6674264069866a772429275b",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md": "93abadee17152b5e6eef625915ea7b828ee54f69124335a2de215e11b62ae65a",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md": "efc42a239b43168aa4f24fe938892cc7969bf062827e92103e3587dc0379bf2d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv": "346ffdf77c8e5b60680d7fb57ee9992765a7112de12673a4328ce3c8149a64f5",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md": "932a5705b875d978a2158d4b1a590d4c2170cae3a60d4385a0b5cbc3b03466f4",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv": "aa372e9fa39f91b4bfb04c9342831cd90e9ecd530c537c2361c35d45de1548c5",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx": "2ecd6ccd690b0285e3414faa52135aaeb2db738e3b69df773548a597a4230da2",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md": "cb02fffbe114df41dd6068c908f8e53d5de323c296b2b43a903f33519c027832",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv": "4eaae31d939e4fe3a64c2ae2afac173eafa843a22f86d9d88befc62d14bc98c5",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md": "09c1e649deba6fb98b0e510416c43bfee4e461516fc5ea9f3f2ab86d9b7910dc",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv": "3fd856fb96e62614ad9cec2f1d24618accfa26f0fc8bf47aac1574c6f86e0f23",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md": "0d8332d332cb7de691149b59cda915d1c9a16395722db517db3ed1c002e8c34d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md": "751147cc2c7bcedbfd61eec6b3d7f68b04a72a6649e99fe734d1f2aace24eb70",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv": "eb9e51a3e7b2b3ec8df27b437e664baa2f895eb70e8e650364f531ca6f729534",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv": "d94fde9a6091e4c29071e9e366ab2ca4d3083dc9c765af65bde0e43d78602c49",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv": "ec725c4206ac2854febc16f7ddb882802c1d71e53037792dd6ad6383869bca09",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md": "b066121b47c37197b10d2bed2fa9709d5688d4973b5d13e23121c7bbf6ed275a",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv": "987fb13dda00f2d62abb4da346f2c6da7e3cbd3857749edc3f72725b59049a13",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md": "de894a4c00089ca73f15076e06fdba9870b86231e236f7a7add802e9f701a2d6",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md": "15fc8d6380b20bff447626adff74034251ab633c548dea0893a836d7f0f28fc0",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv": "019d4780f896a73b3b85400675d394dcfdda1c13e8404d7a0ff9723db4887944",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md": "1d12b07ae29792e7ae547576468134926e6acefde9ccc740dd670cea084f70cd",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv": "3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv": "badd05403089b6a04ee064a937c0d6bdb90a48540dc132e8d89d52c92cdcee5d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md": "5a9b1e21647777cb2855490d42e553a92f56906dad609522cc92841c4c59a9c9",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx": "5346143c47b008cc93d08d725593769f90b06c969e912d9a2d3d7d4914676b0d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md": "557429b44c0a0dfb8036e3aa734c8bcffc04bafbfd0be6f47bda207148ff3531",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md": "757ba0ea8e15d71d2a9bbe2ba1bc2add412122ef610753b898871038a109bfc4",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx": "1727dd0eeb32da84135d094f34c443605060cfd3fa39d269d85f855ce731b563",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv": "d79fa7a1611883a9ad6dfb5d4f02a58622c48e7533d0efc20ea4e3bd04b3bb76",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv": "c075ca7049f5cb81ea7fe997a9f29a0d0cc07971af52594f4560d2e659991826",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv": "a5c8e9eccfbc5e690df3b1a3cb5f7c028e2e23575c5f048acf4526616ba09fd5",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md": "b918c9eb0dd903d78e999c648626d43a35d9c578271a33d1adcaa2bba9d0c11d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv": "229397820ceeaa8797ba8e991026eaf15cb9b7a7e19b88ebbffc4eff9c2c98c1",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv": "70e84334053fe8321f50ca0cdec8a5c5b170931bdb6927071cabf8ff0a9030ff",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md": "d7711a9c4c1e4a8fc066e0e80e231a60b8ca32dc79957bc0538507db4e5cc5f5",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md": "3bc0d655160a18522dbcb17f02e2a55e0b394c058442951e5d5027fd85c57aa2",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv": "0a8934d82feeb19bc0071c5b1c57a13890a2e96dcbab40deb8e2c656c80219dc",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv": "de0fd3ac57a0fb1fca4d3e8be5eabc4210a62337fed5c2fe4b141d9720272aa3",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md": "86b20ae5932f4c36df8f8073bf1c09aa6bdd5e32b8528781726aec558061b8a7",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md": "eadf8e6d29a53f5241394c21310570e4e1431f22598bc7c953b92e4b91093648",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx": "9fcc37d66f231a7177c21dbe197d6b3f084649b8cfe1bad9a5dd8abe9f85fead",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv": "e5df3d17e042e098ade700aeae5ec8e5683a6afc84baf1123a6abe53e5bc6f61",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md": "31864677083fce756781a474e7eb35553680ba63cdad8b2cbc0c272f6e665d97",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx": "a23869a21f9c518ece89da52557933458474486567cf7dc29f57ff1eea63ea3d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md": "78890ccb40a5badcee687b3c3cd9b4b0a6b6a1133cff49f1bbebdaf69e0a8cec",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv": "3833cd5a5418784b20d82d7b5df7b79cb03b9382808f095c7e4ebefdd47cb11b",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md": "e22706b48a14faf48300c816a227341d851155a5b95eb855f89f193943002f5d",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx": "fbe155cd0ea02732fa4157000d2fa28745d38c5a57c2d02a0d7e5e8020c0fc63",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md": "c6f5db10db305678c4dec12c4a12859d54a93443e83201ff4f129f95d8cca866",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv": "ae28b4ae92c47fd5c8af1aaa4486a292683d1a4043108daa9b319d6a5baea6cd",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_TERMINOLOGY.csv": "25bc782f7adb4b14f0531ab77be4d29642e18ba1b574f258491b51174c26113e",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_EXECUTION_REPORT.md": "9e6dba4acad36a783ec250ec703cb2c62b210492c7346c2dc6b42abc625c08cc",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx": "9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv": "c57f02dd60264c9c7689211783a5ca51171abe6e479ca93d519c0a0464b0e0f4",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_7_GATE_REVIEW.md": "3c5a8a85b77c3dd685c6c50b0b757603910710f4dc7b5bd52c367961f7d7ffcf",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv": "ec210ec6bf5bd02798db60db8a9366b3981efc23a9ddff0303051d7220f2523f",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md": "4ca60c29585ed5a364ae526397fe7120976a3912ea9342996ba105f05e56e9ba",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md": "b6e59281460fcf9a88df683bebcebef1007c232ce9497da1ce3952b46402f622",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx": "7f614d06edca11ae573f27aeb5d277e5e7d74f3dc1d6ec9978dbe43f1795c8fb",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv": "287da4a23314f4a98d0ce9a9bbd84946ec235af7fd6a147e95f02b85e81f4984",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv": "65897d9b3bede963c436304abd7278853b49018807988317a2fa012aede7e0be",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md": "25ac75af37e465d3c5ecf7f3c8a7472c79e7d31fc0a776039aa390a53346c034",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md": "e8b911e442b8be1d932f6b12d73c082b8b50ac5abc19b060d625d4f3f3d4b80e",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv": "eed153eaf48e8a9465b8bef645999c171dbeaa6a692ee55ab8b2394114f88b99",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv": "54714bb4d127b129618cb4fbad537ca6ffe3f28a32ace36a0df722c57002dfb0",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md": "84ec29fc2ce12d74ef2629ddbc90078ecdcfaee15c308d9918224ac6ea5a17ed",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx": "8fc3b6cb9c34eb30c7f51840c2224ba9588be17ca1e11fb1e5b5d3368c19e2b7",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md": "a7e19fc11e736c4349242ce61a9b5ddf19056c9c96c6a5d8ccc3f4c71ad1a817",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md": "945df9aa88bba48f29e029a8613fa4dec4669f3f2b29948b99ef619829ef02ea",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv": "336078f0d828ef780792d4081469963fa9a5a344b00ef6530a992da58c862b84",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv": "6eb8ce9e2a1b3de8577b7619d04b8f38d34275c4dc2bbe6dab710ec7c05ceb1c",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md": "03d5f722b8f51c0b66afd5ba1e22d6f4c9210d5e94aed57cd75ccb4020eb0f97",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx": "983ab931ff3f973317b6b892d64a2226aac5ef04e82bda1194a096b2a4bc7b3e",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv": "b968675cdadc8193ae8777255a220b273996d9a3cda5ec19176dfddca1d65e5c",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md": "0b3d70d549ca3a575ea3cb8db22ea524ae5c7e85025f778e1a9123ee74c337ca",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md": "c0aed9db3f084398feda73059135071c66d453e204afe08ed7fb6eef78cc4c10",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv": "4c97bff4f998a10c465abde26731e236759599a17a32923a6459e6fc6bff73fa",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx": "a7a46894a3384cc519cdea0ab6b957cbb5e8fb130dd9b2073678a6d5513546e4",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md": "15537e97652af58e55a85bf001a604205953111db06dafb17243f481f266eec1",
  "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv": "a86e1e9c781a788bea9de40bdb4a0186abf5a5f4c4382a74edeff02ad8ea6463",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md:Zone.Identifier": "b952d24cf701bc4e7a7d21e1ae85c611824e80579a89836c0cb49b193446ccfe",
  "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json": "0c88fa8d97a0eca3dd165a35969ad92246cdb6201b2445a89fc8b99c88e37a06",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv": "942108b492317b4dab974c807923b8c6dbdc218da60b8fc2ca782b8e1c74bdd6",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl": "e66ea1db1d3992786a38bd9a517198b271826bd2e26a9040b30013dc2988306c",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip": "ceae269d7b5bfac451ece3b2430e75f53e865ced8407501a907255218e225ad4",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip": "fe5e5a76485110d448aff4bc78eefe26aeef53b5cf27a556c45145a585d91d1e",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip": "9f5e7df4b38613c0d3decd0d4e394b2c2a53974d85529c935abd7e0f4a58159c",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip": "fa2a6c2cc4bc638c4cfea3b1b13cae267d2549bbfb5114bb6257dd69b87b2b14",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md": "e7c2f0f5dd2a90f683a0786fde59d4b9d280c5aae802d3b0ca73ad2678e99880",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md": "e942f011b39251d88412c5191355a464bf31fe55937f99712b8869be1440f68d",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md": "bf61f7d43c41fe8132ed02a05781d1992b688de602d5c2c05b334a5383a21cca",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md": "f9e4deae3bb04e6d733cf9327d6bd4ed6e8bd50d2e8fca0f88d3e90a64108bf9",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md": "99227959536b4713684cc926f4d61c0b4968b3dc2e11ca9a698887d4c8584cd8",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl": "a73e6a1aaa3a7f2c5d83606d9f2bc1340529508c0a53995c6e9e9edca8cf49ba",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md": "9a3fcb83122ac3a87263c5200c8c3668c1b2a909e3b45cedaee3769183761a65",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md": "1fcf487d1cce20983bed931c3656021f3f3dd70ff911244ee0c1a16c01bc578a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md": "c211a83df7479748e3abf1f4fb3d0d1de15d6d7337ca93b77a10c73f923d8b02",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md": "6e56f1fd4541411be2c61b9ad6a3ec5e7208c3b21a5ef0ed0b8fe7c36c6ad7ca",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md": "a2c4780bb91b3e2842b50851f694218ccbd2b915c315c2a9352d14ad872b6037",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md": "227baca74d45585e3d9fbd2c9fbdbc55cf1c39b66c5769d465d139d23ecbdb72",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv": "3a1a2a01fa3dc8358e90c712fd036132ae53086a2f586a8bf7ff09018148db23",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv": "2d7ec9bc0fce7881ab46d2d068ae573b4bd472c7fee1c3300184e9c4e2e15bb9",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md": "5cfa993c5ab380010b70f7bef5b01d30d9899752ecec61b32d7a570f9bd14a2e",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md": "65253134ca853af03d050247bac17d6d10645e8ec5bb3cb34845acc2b7e37a05",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl": "a92b5fd0a949ec2414f508c2405ba17307c2f7261dda32b280071b3f580705e2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md": "4bb7ece7b35ddd69859e577a2f80ba3a6d815337ff3dfeff34d6c05727cbc894",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md": "86e7f554855c325a2e2d9202281aed66635ab1fc82d9b5737f8b65e4709df059",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md": "f1f56770b28b3d8f7e2dba99ef1a4c1716572e9d13b4ab920985d9504b6ac13c",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md": "7295fb038944a2f94669cbfd3018806b2c9171510e73f7c0675767f1beda4864",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md": "2c34c38e5d1a4ee0f5f48f831ab91c2b09e49be7902c897a230de89dbec7c88d",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md": "da23ff9d0d0263a2d3ec33017f4af51d5c2143e945afdab4196bb556ce62e44a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md": "76269f965567d9c63ab3d46d2cb74b38e7817b8664adf197972c4c99b4b4c75f",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md": "59c58a98ca4f0769a017f959d52129250c4ed13c195bc2e19d61dd09e55cfdde",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md": "561c9433740bef2a075b89b4542ab1ada507e8c5da537766cb973fa55887863a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md": "6757c38856b1cff291d20b4b4f64766c3613c5429acc76179f7ecb4382414d80",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md": "6acac4d999a51ba00a3555b06ed984b3717777e0224a2e63731319d643125a46",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md": "0090fb4a156348e94ce257daea74cf831ca9516c9f543ac9616c1a4977142cad",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md": "d3257abbe75e0522dcf742c116bf90e2a71ec9a40f8c8b07219a34e6d29b8160",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md": "4d7fe0e82aa3cb8d2b7fe3bbe0e82707b5b49c1768ecc0903d17ec066f1a306d",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md": "37d2c0a93d61363ba129c90ae2ba6036aa0b54b57df70c134962c980408a8844",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md": "58d3e6cad974f8b046ae7a1518427e5847005ef43580560b2da7e1d3b1b86f11",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md": "77600455ce66efed8ad1f021b046f138987c0b1fd8d8dd5385f71adcd92e2930",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md": "b8c2a8e005fba969cb93cf39e5814b7ee9101e2317c4a3d265b11e1b4d56d7ad",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md": "2cb4a9dd21a955d9384db39b62da5d289ce8a1804250e2f5bc6023d2cfdb39bf",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md": "c66a797a0d955950fe2ac9544bd26653162469f01c43559e94f037822b305aec",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md": "99108328ba97a0247626dcae6fc12a61e6a1423695d76bbe389b7fe0a3c3a25d",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md": "fc309e685dccad25170acd96ce245c5034ad0030d1304ed0c89abf4451acd6d2",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md": "613a9e639cfa42ed0187c376ec1905f83cc188a7bb2feb5cdec74d7e6f173fc8",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md": "d8fd9e3c0db14c3eea75517dd1b6470e59c828c92ba0c32f379c9ec824be9d24",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md": "4386bf87ffc2a5855c5efd1f35d1618d8927a9e28d100d75f086599afd18d4bf",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md": "a6457ac3981f6838b2522d273160f0c58c0b331f42ce7aaa72790a5533b95b2f",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md": "a63d0b0c1a7a2b88eb66e3f1a7bdc2344823ff7858b79ff0ee27c1d01a2f5195",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md": "0b3b22bea89b9531ac47916b2580c7c441eb40db942aec71120436c7d5041c3a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md": "287c5be073d1d20046438bb49d137b967afb664d775a85a3657fa78d4dafb151",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md": "0de72a805a00c375927951f7824045e5527ca633ef68048451089d963b3fe284",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md": "31553d50fe7211714ba653c2b2fb53cee62ff8f778ee945b78a0939282104b1c",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md": "98a9f38b831f10c2db3ded14f98828db297b69ac5013eb56d90840417312e0f8",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md": "2f46a71b74bd5f60f8b64d697ec5c634f571b6b16049a5e25ec94d6bc94b0344",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md": "5c27ba3288b8ccb9f7b10e6b80ef60fa074957157f194dd8741b2592ece5e38a",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md": "3c345cefeb83a7eddd6c7e397bed2ce4ac9b5b78fd51ce5653b2c687f0e5da5c",
  "/home/khanh/projects/mechanical-research-agents/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md": "f0ec5b33fcce777ceb08f520a79def984fd3849e18fc5df7217052ad5b65d0ee",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.pdf": "9f4295be2368f46bab9394f062b7f3cd8570093ed7855d2815c37c6cedc186a6",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M28__2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf": "1c81b2d35c0df0efefd34f244dfa023045dfc33762f78d14fae54de0b040ae65",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M25__A3-2022-Mechanical response of single and double-helix.pdf": "53200aa0c608c3ff3b7819b6c17bc87a79f236ac4e8ff4b1c69e3c5d7cbfed1a",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M02__2015-Burgner-Kahrs-Continuum_Robots_for_Medical_Applications_A_Survey.pdf": "d3c865e043053477d3672b41d95bdbeab3c8752b94c0cf0aadcb83d22601305b",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M20__2025-Continuum modeling for layer jamming structures.pdf": "a792efc4453c0565fb59af285a2c564793728ac68a259dcb0bdb2710a53cb59a",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M38_2008-Evaluation of measurement data — Guide to the expression of uncertainty in measurement.pdf": "41bbf068fbc0d7986c98691b2d1af6680cb3044f6a1a89b3560933ed9ef9626c",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M22__2018-Bending Stiffness of Parallel Wire Cables.pdf": "9c2773e4cdfa29ee850d44206f42c1e21a658b8755fbffc164978d2a48d9d2fe",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M15__A Novel Model for Layer Jamming-based Continuum Robots.pdf": "b573b2ab6bad556d79298b9374ca2767d8d9785abc03a08736504747ad2b7f63",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.pdf": "652e62758fe4816182d09ed860dc18e8cd4d65004191b63f84a56c9293eccaee",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M33__2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf": "de64029540c3243da2f2499630ff1af3b20235a208762b78e2df286d88827fac",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M37__2024-Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon.pdf": "7ce492505ddd58fcabcf7c1e2d41706e788e7b57448483c8f3210155b5721f08",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M30__A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf": "e8462758c39bdc7291365effe5e6cb74fb16c2a1201698e999f4ee2f4ca2840f",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M03__2023-Russo-Continuum Robots  An Overview.pdf": "51d6d346041ee4b7e7b2bdee9a6da3dbe23d9a8d12f3fe87c44d8d724bb504b2",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf": "240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M05__2.2024-Fan-An overview of stiffening approaches for continuum robots.pdf": "90523cdcece9144bc2f60c5f3e3874f1d30e3b5925dcf4e2036231b13ed84cc7",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M31_2022-Towards a Snake Like Flexible Robot With Variable Stiffness Using an SMA Spring Based Friction Change Mechanism.pdf": "65d0979f319bb43c45a92020760e649ccd67e647fc58271cafe89b3c73c8ef03",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M18__2025-A continuum-based model for a layer jamming beam.pdf": "95646b2cfc4bd65cbf8564775714afedfa0f2864fcbdc96c8287390b2989b8dd",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.pdf": "5f7ccd7357928e6acbc35645bdd2cfadd1d6e63aa8212c62513a362ff71ec8e5",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M34__2021-Shape Memory Alloy Capsule Micropump for Drug Delivery Applications.pdf": "55457a97c60efae1ddb90544d5382e1786579dfbdff5e445b51085db5dfbb782",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf": "182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M36__2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf": "40760daa02b35309d91df1f6aadf35cf34726dc98d8e9520f1324e23cc59a4b3",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M21__An_Underactuated_Variable_Stiffness_Continuum_Robot_With_Multi-Layer_Jamming_Spherical_Joints.pdf": "ac542457be6803ea9c9717bd8b7e03ace65c4bc98ac2d702a39bf80da83ad752",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M35__A5-Cable vibration considering internal friction.pdf": "aaad9c248c7dea248b14e986a530760646cb7dbac8a44d41b94642a583514800",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M12__2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf": "bbe88a0c04b7a725f44d8f0271086a494a785b84030bde75a35ef892eeeecfcf",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf": "3aa8790db042279ff0fe1f61876b3cdcc573878fd25a50be6ddc6f9ec7b8577f",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.pdf": "7310944b4c2ba8bec78f7ea09ed831e109cd72daa4e6721276dac04405680933",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M19__2025-Toward a deeper understanding of layer jamming structures.pdf": "7cb387b88dc14f9c30f98b778259133caf83aaa41346ae1ab674cd695405b59a",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M32__2022-Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon.pdf": "2cd907e77a983f289850ca4519da87f99b5fd5b26f6455fff5275ecc5baf8b6b",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M27__2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf": "fac21c950ecbe7dcc0ef246a6cf958186112529fc3f98be8241fb81d0dc7a284",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M23__2021-Analytical model for the bending of parallel wire cables considering interactions among wires.pdf": "1829a6d3b2286d1ad44f8a9e922d7048328b2cc466334e4c99756d622803278a",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M16__2026-Fan-Modeling-Control-Stiffness-Regulation-Layer-Jamming.pdf": "1f05cf83bc7825f9f8aa44db1715a7bd73dd671b78424304f7e36717b4276e3a",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M26__2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf": "00414aac4beeeba749d7c59ffa6c9ddd3ee5f3dfc97c0d0529241f8bcf4f5ce9",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M04__1.2024-Lin-Variable stiffness methods of flexible robots for minimally invasive surgery  a review.pdf": "52f65769269d5fb82a7a0c9b62553d8d389f23b8dfcd1126ca7d914c8fa48d12",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.pdf": "6583ae5919cf3f544b652c2e6b8bd59a06e47d1e99cf7cbad3d036f266cbb807",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M01__Telling-a-Research Story Writing a Literature Review (Christine B. Feak, John M..pdf": "5b498f49612dc5d612c604085f5f8266b990a42755188f7be5c036e0ec6059b0",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M29__2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf": "56793dea9b3dcbb4224e7c61297f37983f9ff0abcf43d1d782c0e0ad26355b61",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M39_1994-Guidelines for Evaluating and Expressing.pdf": "24ab13bd20d97d8157f50671cff90fd93a7dbe66172b6afc55d00064b3f1c55a",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M06__A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf": "f5f31ef249916924831919f6cf5a85b356b49069c2e2ebe9a7a5c58cd4eded7b",
  "/home/khanh/projects/mechanical-research-agents/data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.pdf": "cb423f09c9cdd885ad8371c10817522d1a57f55f06f1e1db1206aa1e45ce8827",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/INTEGRATION_MANIFEST.json": "23b1afe288f5fd73c7032d7fb1617f69a58f9cd22e1488bdc75a9cb76bd4b8c2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/INTEGRATION_REPORT.md": "3f013e43d325b712ef8b25ee3444be00aeaac7414c506884438777faade0d0a8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/08_UNRESOLVED_AND_HUMAN_DECISIONS.md": "999d66635a1b142ea346b0db46d88d5f62e89840a073f06715d257403ae6440c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/05_CROSS_STUDY_COMPARISONS.md": "adc1af3835a4026aa84d6d757f1927de9d03dc2c68fbde1206842b41d9526d1f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/03_CHAPTER_2_WRITING_BRIEFS.md": "6ce0649066fb84379c6f77d732274d7fc76ea10980703dd4a2df97419b35fb9c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/10_EXECUTION_REPORT.md": "65ea0328fa4d383676f9bde02b7cddbeaffff7b0b644459b7c2bdaf7f58865fd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/11_CHAPTER_2_READINESS_GATE.md": "8c563abc1d8134e0e18942c0250ff9064c4e7d31ac79f494399b20830eadafc3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/12_R3_CHANGELOG.md": "bb500361fe698d61b9629049612fed994986278ef7e8927944e99f4c23a23cdd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/09_COVERAGE_AND_READINESS_REPORT.md": "0cdc669ef4b8fa1aa5f5d25fef1c7afdaa3964031b4ce413782c019b505f2519",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/02_SECTION_SOURCE_MATRIX.csv": "5cf85b7d5bb5946672755e2d66897333326f83e4fdba0c75086b0a7fb2cc454c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/04_CHAPTER_1_WRITING_BRIEFS.md": "2766850b820b31fde477a8b5b72491372ca881b62b92a9f0923f2515676f80a8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv": "f0f7b1428d09bd2aa6a2ef412730a577328c971c315decbcfa8fa0418371c1e0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/07_CITATION_AND_REFERENCE_CROSSWALK.csv": "1c651403bdaa31564975ea178e868cf6be0a3b2b4adceeffaf6228754f67636c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/01_OUTLINE_BULLET_CROSSWALK.csv": "75d156154c148565197fbb5d1a6cccccfed4640c58974d44522b5fd09f0bf008",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json": "15d7889dcd3d755a866507569b1b97efd8c2de01d6aff4eeb07498042f729cae",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md": "0eaa5359303f8df294136eac63847bacf67e400fae821ce0bf9eb056a183c406",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md": "12840926c15734d16a262f245540801a04d6e75d7343e38f2d4f7102a2eb5c79",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md": "bab7f7aca4ccd34f9f4ce50e24be3834a9f4efef7270588e09d0d246dc0e8de2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md": "c5ae20a7b801a280c0c9756130fca92e8540e6d8bc5fbe7a414ad640d6ed18f2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv": "6c54a359b89d971ef8d77bd7c8b63ec776117cecedf8af01ff2781f26e4a9005",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md": "5227e1b339a8c2ea87a8ada8449a01dbfa5cb5c3d859acf670fa0e34fc4c2ad8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md": "a02a84af3c2e15ebe7974bed10ab7ea298d93ee8f6bdd5b76c2ae90fef6ff682",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv": "ded2f71918191a57df34e94b5f150f82e9360be7639244fc664826e5fed681fd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md": "56bded9082535752d7dfb3c2f8aaa360aa4eda7dcdddd76fb81f47f990fd1b24",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md": "71dc08da3ba129f5319c5a243e2b0e2b239336c5ea5d4cfeb8ee402340aa7003",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md": "26e9a09ec7d7e10514f8a5f6bb6dcce58fa7f713a03ed6aa555d9e36b545faa1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl": "bc13f0264e0017ad1a9bba875dd1205b0caa69bdf9d632f944d7a68f9df5af87",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md": "a0aa4364cc2147ef1cc97d21645c62e42bc1a6544181c6d0715c1b1d7645ee5b",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv": "245459ccda31da0e0e8ff974243d901774d01c8b41e79ea8b41f0d7d896bcf1e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md": "3e008fc231ad09f39a5c7dc90267822035a9e3f17ba25b4d93101c9f7e4de513",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md": "ebbaa7d2c70a454b8103d106daa12761a6f4b98121e9d76b1356b732760b5a40",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md": "809a5df6fa3de1d9060a4d44753ac95ffdf54cb7d1485a0a6c84507b285e323b",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md": "6a8154223b67f8571986f0aa73f8605e0c0084675616b0397a1cf903cec3a4e8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip": "7f027721546578ef03021ac790c3998ec4da8606f9f3396ac683ebd833914f6c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip": "db4acb3fb55941b55b7e23aa0fc168c5bd554e92871679a45f2492b9a3166b6a",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip": "5c85ed4ec9380a2f2ed71c8d099b66f517816dce34d78f36ef8b44db45fb0e94",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip": "9bdabbf233fe02ae280e745631b1e9cfa442be59b1e52419fb302b2cf10e1766",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md": "6b6104566ba9b897a5ee9e9dc94c05a979b8a5328c4d074b1446005da34277b7",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md": "cd286a999a62a73ae1c4106cb9ea4777b75fddfdcdeee60060e2c14200323c38",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md": "b21816a15a170aa76b66348e80a9f8268d6bf59c69922b276ec8f2b97ebfab1e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json": "0fcfc87c4f34a087793f9cc7982e633a9fae2b3db0ee75a8c3f4378a97f8f5c1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md": "9351a77dd7c841de232117fbcf5b9362413ebcabe0bb3fe35fac048997f197b5",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv": "fe4a66aab01ac3812592f80ad9fe5fb381818bd2c0812663a9a6b34f5b60e3e9",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md": "e9a906d7a211d76d866f279cb9a892315d2bd596d3fe95082a940b4e3185b4da",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json": "0e3cc7ce3eac0bbcf562f3c2c051f4a28ec75d61735a1d1ddb3bf12e33abeae7",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_CONSISTENCY_GATE/WP_E_P3_READINESS.md": "846a321c47bf3e7b4ce509b8142cf6d7d15ac203cab0eeb5c66243a78f131f19",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_CONSISTENCY_GATE/CONSISTENCY_FINDINGS.json": "1df6322e6e8c16d0477fcfbb023f11268d5a364b423dad9ff23d935148cbb35b",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_CONSISTENCY_GATE/CONSISTENCY_GATE_REPORT.md": "a5c0e76073533212dd05f88c81f07290365ff15354eaf3d9aafb80579f2cc5dc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv": "9094ff7358352c5319e29675c1c13416a1c481e60988663264b632c277ccb011",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_DECISION_REPORT.md": "e06325a7c0c496ed96f8e45740b6a1628fa3d26ae2ddc70502869cc0d4623ed9",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_GAP_ADJUDICATION.md": "f51af652c5ae0adfc9aee205abed97dfa6808efc7dccd19bb55e55bd690dcfb3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_EXPERIMENTAL_VALIDATION_PLAN.md": "f8e647ff907a30c638d5706ad8f1cd1993a379b8690e0b4e4e69f3965acd2ce1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_MODEL_STRATEGY.md": "61e20c4bdb1e5e7a8577423063c5c93cfe519725096dff04d30278ca22f1cf58",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_HYPOTHESIS_ASSESSMENT.md": "2b8614b1bf2193ae3ffd716c173d28059b313e4a55fcad3e33be1711eab6fd90",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md": "09557a7d45da259dd085bd05d28e798148025a7fc59576bf48d79963bd27672f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_SYSTEM_IDENTIFICATION_MATRIX.csv": "894bee238316e1d34a654d4669b6b0dca23fa93b2ce05e3bb71157f31e7fa201",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/AGENT_PROMPT.md": "91e1fdebe210f01236c0f64f6b9c5bb49fff0fc855967f8a7b45ed470f8e3284",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.json": "55e15a0425dbde3ec3eb54c1e1a769c52717f03ca5d16c5fdfa8ab326d8217cd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf": "18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_OUTLINE_2026-10-14.md": "45542951080f66859241e7ee3c9666b7d22df2348d3236e7560f59aef955f605",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/MP1_CH1_CH2_SECTION_INDEX.csv": "ac0a8bf828c9e69362112c6d8282f9de25cb3616ee36fd0448d741dccba59633",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md": "554a8b40537bb19a8b2d546cac7cc7b378c1fa787e4d9903202da03c305ccc8b",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md": "78f5659de21eb44c5d8e0ba52a69ff8cf984f93c1b8dff8a8543325df4160fc1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md": "044100d12d32f3d18833c5f64859b88b101e04058a2f92da1e50818172d48ccb",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md": "f13887e81e5f1ac73ffbaa735437e29171d157f2f3fe5b17f4d2a7f0ea18ab4c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md": "1271d8c79136bd6899ff0c87c6c854365dce7df275bf872f7ec43e2ab29d2cbc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md": "d15a3219062cb526bc9efcc18a3353f069981bcb28d3096a9531005aa8684f9d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_UNRESOLVED_ITEMS.md": "ff0354b39cbe55ac27abc0f70d3cb09e480bfe5fa36698c5433d4b54aa036cd8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv": "7f03876bf6a015347c020f285d3ddddb9c865b337876276b2f59bb6ccb23bf34",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R2_SCIENTIFIC_QUALITY_REPORT.md": "560f4a02b96d034f29ccac56f398260b5022ff82f3032d01fe5f5781ae27fc04",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md": "67c79f38c14e21a635813d80138c81e02dc09b551c4ed71ca6ae8443313e8907",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md": "7ffa3cd9c7806ece721f4f25ad82febc5fe8bdeabcbabc9fa67bc8d47a8a6101",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md": "17e362f52e2aa248dccfcafc64ac7782ef6bb6576424a9f2383d005d7db652e1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CONTENT_QUALITY_REPORT.md": "b7d32ab21bb4b80ea66fa576d5b77fde441c09b317ad577f023cbab22f2f105b",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl": "d4f36cdefb54258e7ce7848f60368084bffcc2b7b97891a49371e03f72b651b8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R2_CHANGELOG.md": "136dbe08555b950cf487b7f10057fe1f2b0d8470a8dc515ce380d4af57cdd7d4",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md": "49f44ee6cb94c190942afa1096f65b614364cf1258e30236b3b07ee54b9e5a8a",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md": "24789bad80234de8ac8cade1c4627873295ee85a7ab10ddba6f1cc2b424f0996",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md": "607646587b0b968f0cd6f27635d2b295b63e22608246b39344fe920de462cf1d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md": "24f5bf7e6d6a8f3b82c9f1da88dd6b78b4f528fa3064e4c7e84f0f2eab784dba",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R1_CHANGELOG.md": "bffab8c4cb5e19d02e035be998c26d3caef78a5bfc37cd97640fe55d3aba85ce",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R2_CHANGELOG.md": "34b8d091e1709d282c1d89fb780d591f9d1cab36506bc320e6262da3fb06c0b3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json": "19fe99c6ce010687cfdf53940f8543e77e79ed0869f0af03be327fc14a5863a6",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md": "34c7e6fc2fe1f5a2f604ecf94fd33fa0aa701c7f9c9ca1e3f06c2462715ec213",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R2_UNRESOLVED_ITEMS.md": "1251149365edb262f26531736755087e8a00a50b450c1acceeece8c01c945261",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R2_HOTFIX_REPORT.md": "d38fe03567fb6343852f5019b96fa7c0f79670d1a18641b3b4cad405d841c207",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv": "b009902cbbc308eb05669f0ff19df66ae3c84a6b0f181e6f7bab35524deab2be",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R2_SCIENTIFIC_QUALITY_REPORT.md": "c35f2552d03d5feb3ff7fb491d7d8671666c5e8c7af545cc0de4404894e38ba2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md": "5bd0c26fe9be561cb6ce2fbb83effd8d8ee92b1e1606369c84989c39b6e121a1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md": "c4ded1b7e7f2e01d2e9637ceca9030e013612a5eccef57c0afa62028808dacda",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R2_LOCATOR_CORRECTIONS.csv": "ac95602b75ca3f4ded9bc02bf1da313fdb4b906f0a2ece4bfbf053fc3cc92ef1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl": "9e0fe91a9ca80add25f9e2927c4ee6c4c1360b3ecb7822041abbdd407e92b033",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md": "ac9a739621f13ce6b7a09b33b3db48df5004ef13c735540bb80f31e42f059b09",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md": "7d82c14ad46589d0982774a3acbdae46f6440e2216cda96502a69fcb43a51087",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md": "9dc9cf2e28c1aa0b3e29d467702ab87c0747b6d096d037ab8163d4aa9dc7363a",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/WP_B_R1_CONTENT_QUALITY_REPORT.md": "c1aee80ec93f339b4b55b46bbfae27f9dce05521b3e27b46c1214021ff6fbe51",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md": "3a84d673b39ec32c1fe6f5e7850fef54a8874faf2f2a687a40bee448ea0d898c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md": "a18aacb7fc9e670f56d96e7899e0d59e6d16273b673e31883268386410714907",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQ_R2_SCIENTIFIC_AUDIT.md": "30b9daf6fd0a4c0ad5e65eec20f7a03f2932240ffe0526e0250f3ed1b8eb0703",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQ_R2_BLOCKING_ITEMS.md": "298332e01633636ecb6a9a802c2f6d66e877c89b45265e9a4b8dde617ba1cc56",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md": "65949463d48033db715625d2b05a723c173b46a571f1f8f3a51cc57e3a443b13",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md": "319c7e1489219525380497dbba2c03d9c394bcfc652edd6fd0e4bd6a3bed4618",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md": "56d25573b11b05005399f005019edde24a48a11a461c392e11f480ca0e9c7210",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv": "6d5e8aca20c63e5fee1bbe832ef36d94d958fee86d453411721c30bc8ddcd4ff",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQ_R2_CHANGELOG.md": "9415637e7f374354f4894b776816ac67cd24dc31e63348045c2de9eda6e397a1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv": "bd12972b968d26ed8d620de3b991910efecda5fb3b79485f584243e3e9d0bfb9",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQ_R2_PATCH_REPORT.md": "2d2a4713f95257dbcd6285748c4d9b33cccca0bf4ba48b4c1f3ddc21585dde60",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md": "67313bd827a964639ba9e75e4712dfb907265786a86a0a86a0bbe1ac6fc05f5e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_ASSUMPTIONS_LIMITATIONS.md": "cc210c66582944fa2fd94fbb8fb6c5c03af852b1645a9fdb6ad68c3aa162dcda",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_SOURCE_MAP.csv": "2d80ff743568128c2af7f52576569db1589c422a5d8210bb705761bcf8153959",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_P3_HANDOFF.md": "bfad030b49553a3b7cf7cb3a8dc9199100bc70a6797090fa7f52e337b8a9840c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_THEMATIC_SYNTHESIS.md": "5287d555b02cfb13f0b795f568cf3903c7278f15ef388ad9df267687de28fca3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_EXECUTION_REPORT.md": "631d151891ebb0f964901f0dff2a6b956a70d872648e11df56308e9c7955f29e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_CROSS_PAPER_CLAIMS.csv": "235765674f4ac445fa2001cb301ab4f4aabd79d05914eba2f08738e76ae98a25",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-E/WP_E_MODEL_APPLICABILITY_MATRIX.csv": "06a7179fdef9f5bb82adea8ef06ded04082e18ec956f1f008f45b4e7fec44d4a",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md": "ea564e570bce74507b961831b7274ad0b93f217cf34033a148fafe007cef1ea0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/WP_D_R2_CHANGELOG.md": "475af0829e2a56d0fe7de301d10e8a708f5aecad870fa7183066ed219316713a",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/WP_D_R2_UNRESOLVED_ITEMS.md": "57db2e20c467ee3f2b81a7d3c9d090e7695414d91bad6d40125bc8b2582aba5f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv": "b4cae1bad35a16d7a220947be903474137a765914e9b666d7384a21535c87dd2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/WP_D_R1_CONTENT_QUALITY_REPORT.md": "4f24453e2995747d98002aedc86b574451f2993baa9e9d9e14e4c3de55793bbc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md": "4739dcc4eb0b007e9c2c0feb252c637a8c380e71f605bcef52a43b8784946ab6",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md": "4ed181e645d9b04f19e65db39357237d30449d03b07a0949eff7c899ec2edac2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json": "eeb5ced8ff4c9f719600b5e026442d815066e02c694b06f43098ac530bc98cd3",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl": "ce7171530866bc9b453cabda421fb88622acd1359c02b920055f0a191dee38fd",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md": "fae8b24e6ce5aeaf4150666a4b46d0deb22a2198a0d4092ff7c939f432556b09",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md": "2e7fc9d6fa9aad1f5e4538399cb661159a7dd2d326bddca389fa3593f4cb3f79",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/WP_D_R1_CHANGELOG.md": "1403187dbec66a42df7e7c0ae5df4629db274b385d5685076930f24bbd5dce2e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md": "880d457198114df2afe0bdfa95ed574cadc043542e23a22b1cd70b4c5b9ee4b2",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/WP_D_R2_SCIENTIFIC_QUALITY_REPORT.md": "dccb3ed6ec623eef6d5507cd32891fdd1d2f0cbf1f78693642229fc148b232ae",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md": "3c54877d2c14708070c4961d28fea2da149c7ad09dd29702bb70cd925e08d7b7",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R3_SCIENTIFIC_QUALITY_REPORT.md": "0bf0887febb4ebd08a9a7c16bf3b6010ecf19f3d5469437c9ab157002269d9c0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R3_CHANGELOG.md": "2d3372e9c481c2ab3f03804607d01b46f005fd0729e72c8665960d625501b096",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv": "237c7701b0a73123ae28502d627df54e1581295d682cf9b5f229f2059c6f5fe7",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R3_UNRESOLVED_ITEMS.md": "1ce80c43b8d6458df35c2ba5273951d0b0ab9bdaf02cf206a729d790689410cf",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R3_PATCH_CHANGELOG.md": "0759dd21ffe4f960e3d2fa93b00ff7ecc4a1911bbb6c92bf662b7db8d7761ef5",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md": "fbfda0e614567361f17769156c5e65c848bbfc5d700dad7eb08249b84c11dcf6",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv": "7417b70078af5a94373b8ea13745ed658fede9337ca7e3af7c80ce383370c4f0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md": "485342d453598572a76e25c7270aca54aa396cec9c7bd11e82818d155d497753",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md": "c746d5fbe5471cf0d630e4b1dd1c7bf4c4648aa6f0a5c1492d8685aa021d0861",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl": "2cbc09545b108ebd128c22d569cad8c72b2748c56e14fefef2596f27a15607da",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md": "8783a647e95b89086ca536710abfbd99247544e6d12f555529f74bc2e133c1ed",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md": "4b0e4006066def789723fd19204d62328ab039035f9049b57c78eb6a3a44baca",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md": "1a9478b4a21bc85dd83c3d894fdee413a09d1614796c2008836dea78be402b7c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_M27_LOCATOR_TOPOLOGY_FIX_REPORT.md": "48a771487ac2c9a69c8610e78bafd41cf265549449dc2b6dadcecc42c67562a1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md": "78bf1863b4a5eaa01af9656e4abaf7fa78df817805d911330b4b1d92ddc69109",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_M27_FINAL_RECONCILIATION_REPORT.md": "5a60961efd963674eb9f6f59ab51916dbdac7c35e9ba921ab2724d95c5da201a",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_UNRESOLVED_ITEMS.md": "774115627d9adf1cb97a177a44cbca83b12160eba5431827b43da9c2ea1cdaa1",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R3_PATCH_QUALITY_REPORT.md": "c5f4c8d2273da0729088698dda8fe7fd4c32cbf14af6c2299f262cd8e1e0b66f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R3_CLOSEOUT_REPORT.md": "e3946a4e7324b0aa2a0bab99ec076c6bc7858692e474b139d9afc852eff047e7",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_R1_CHANGELOG.md": "8a464696abcef4982313d213b02af509811a630c0eddaec1b31ebf94b2f6bc61",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_QUALITY_MATRIX.csv": "721a68b55851e1eb66c4ecb8cb0e156481ce35578a63dcb9c887ff0fc8abf43d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_R2_QUALITY_REPORT.md": "f66e402c8aa2650c94d11f463375c8c661035f9a5c39cf17e4b30dbc12c1ffcf",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_TARGETED_REMEDIATION_PLAN.md": "d0392ef2119a88fe797ebbfde7fd11ba946423d5142feaff0f62d3d6997cd4dc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/R2_HOTFIX_REPORT.md": "8f141afa0b9e872d98fa01948c9590d122f5361c0dc4bf20cf17c1ce1bd17986",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_QA_COMPLETION_REPORT.md": "88b3cf558ce0effe5517f4cd576d06b97e46b318720cfa99a0719f44c9a54327",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_GAP_REPORT.md": "0dd1b3c398086bf78c5fd027d86fb3b13decf09519740431e32683c484b80b05",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_R1_UNRESOLVED_ITEMS.md": "74df7eb1420a0ff919babd4198b56d52d788c2a10746982f61c5b5e3727d9d0b",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_R1_QUALITY_REPORT.md": "45c4bb1f2ef65e374fdd83dbdcb3f4f9ea9b9d334b3bd2624dcf84738433a3cf",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/PILOT_NOTES_QA/PILOT_NOTES_R2_CHANGELOG.md": "c2e3fbc956e574b8bef32130e4d276ddd93a0006a43ca410365984e4be8d9989",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md": "eaf40e4e6bc8d22a12962cdd3be7d47c6df44679163c123aee0a277275936593",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md": "96ea41da978b46705b13b3db02371f2e1994044f6a3e0da2d9e8931ceb69a03c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md": "07f5bde934b387c0950a46bca7bd59f8060c86eb20a7347081a6e217497304dc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md": "794f5df32727937150be8a644bed7d0f9f5ad269de68d561361af08443bdde9d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md": "a6d81de86d8a778c91e438c34aec825c89bca3d23f666d4269d957cf2e59ab01",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md": "7f7ed2f7bb0cff4eef1a67ccf48c3ac73ac4911b98b82c1eba25c4175075b150",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md": "ec7083c454b268600be19add6b8cc962e3f426b8a713ddabda9a8ce2d9b10f54",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md": "7ad86973b930cfeb8ffd330b0c1abcd7df7db8a55c7066eab7c93a97ee9acf59",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md": "92440f3e5dbe9b7fd58f66d649d8f5907c6a0c98fb876a94aa3881385a247279",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md": "cf332837e96ddd444cc9e44665b39b2f952df0eb60aad2961f7d845354c0cc70",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md": "8c8fe9e8c73a41ab6bf20f67c44a2c45625450da3e9522acb14bc8c91c25da62",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md": "7bc2b5231d31d7b9f2baa8224dd6a761e22878496b9f2cf1adea4b41fd8fa09f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md": "98aee756c82109c8d0d6b06da7da7b39f1ae0d13f26edc937e6254b93adc7d5d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md": "6eef45e59253e87bce5ac28f22b39db1bf61b771c5b066519d2b85545a7a05c6",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md": "18949a93ea21477a9b4ad2f6dee52bab1174be7dab5a0e10977a615aa34c2136",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md": "5709d71af2e3218e1c2957db7f05484e762ba627b97b4ca015cefb09b364809d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md": "49d8461c026cf19b5ad5b5f283dbbda68db16e6a608656f176e3e9444bfa2f9f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md": "24a3feda721c4fa0dfac6f869d357799a85198a349b17da8782d9b2ed6bbbb1e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md": "bcac155053a9b19ffe05b421d7d9b3141fd7b791cb0e4bb80d4786ff98fee3af",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md": "f1c22cce165192b9e8efb556eef328cd00c9ebbef842a803e221b1f2c37f83dc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md": "d5a470251647344a7873d8cc185e8c9e8657a03a635fac66484c6838db69d8eb",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md": "5c10e3f6a979ede135b4154c3f71a074c14c9b3b02d473ffe4af3af8589509af",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md": "c320f4ef1815e4fd3dc77ac639981e8aa92a53043f23237e1299870fb0cf4eef",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md": "50f94e03c835c643d898f16ca1449ac6b9667dd5ad178708ec958d9f2bb371bc",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md": "9142f951299de77bcb586e31f0755d00e6a664fb15045d0855e13cd7914abfb0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md": "8ff2a3626f4344e4076d01a96fd50c71c8e3bdb8707e2bf8307ab6982ea1c01c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md": "fd893c9e33b92c6d941e4edcf3579534e4379bbb96fe976f96647f0b6a08c034",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md": "0d108e522c6b683a7e1fdb373c16046f186deec8c1e1f0dc7e14549a0561c848",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md": "0e53c91fc03c31d1247a5b9cb7e810db253f9be47f9986f14aa54eea088c898e",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md": "1bbf8692b579cbc84d8af664c1659b28f0b32456ae3faaf8e98a9332a71283ac",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md": "ebd75796ad125d21bb452d5f62709d5c9d5b555008a416992c7cc04e53e1ff4c",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md": "7b7307754e959217d9369478b1da01fb27659dd7027d51c44301d430a188f628",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md": "13e99dac2f92bbf0deeefdbaaf56603545cc7242e1b3fe64a480425cdb7877e0",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md": "0516479bd439207e25e6c7a9f7824d4c6227365849ee0d0aef9c4ec84720c6f8",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md": "4d2bb266e4ac3f803aa8a1a852644d03d10e8acd280ef17aa5a5446c67a6f4fe",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md": "dc71a88dbdfab9078b513798acfd7f509b86ac68f4b7f9155fc6977f13d00e45",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md": "ca15e86752e6de69860f5175e538ca5a4ac446ea9857d3170b8b076028a16c8f",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_HYPOTHESIS_RECONCILIATION.md": "5574c5d6ac0ced0c4511bf9bd5e9c0755fc16a14c98166bbc97025505eb9df33",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_DECISION_MATRIX.md": "4ff682b4a41a127bb8cb95189b9153ea2100f27a8f613c4d9d0455ddd81cc99d",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_R2_REPORT.md": "a6105145c51d6d58438de566af9e913a9847509fdf7b346721bcbaf1d2ecfed5",
  "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/DECISION_SUPPORT/P3_PROTOCOL_FREEZE_CHECKLIST.md": "cbe8005a3265ccf546cbc9b19ae85d9046b7773a6e06c15fb4fa031bab916e55"
}
```
<!-- INPUT_MANIFEST_END -->

## Ghi nhận trước khi thực hiện
```json
{
  "coordinator_task": "MP1-CH2-2.2.2-2.2.3-PARALLEL-RESEARCH-DRAFT",
  "workspace": "/home/khanh/projects/mechanical-research-agents",
  "branch": "main",
  "head": "e66bb2f2339006e763cd60687cfc24680b945d97",
  "preflight_time_utc": "2026-10-20T07:42:20.400082+00:00",
  "input_count": 597,
  "baseline_checks": {
    "section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx": "9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba",
    "section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx": "bb9d61ced051204661de2b27515e6f275f79b774e9767fedf9afad93499875ec",
    "section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx": "d43cc4f959a84215a168e728ae58ceb7f4761bf5be36244a54d06b38c6a715ea",
    "section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx": "cc4874de9300a8a1aa4346fd1ce898067499820d2da7330d49917a3731aadebc",
    "section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx": "d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b"
  },
  "target_A_existed": false,
  "target_B_existed": false
}
```
SHA256 trạng thái Git ban đầu: c6479df426fb3eec84d26dbed2d72616fe187bb5ae837c975c37b82c7ad191fc; SHA256 danh sách đầu vào: f079b7929958537c0c2d90af4ed849e789da719a7ed90f4752de48973a33477b; SHA256 phần khác biệt chưa đưa vào vùng chờ: 6a5d7bf90c5c7973677a22d6c781178a2d43daf4d5383595fb3806ca4b6dc1ba; SHA256 phần khác biệt trong vùng chờ: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.

Dưới đây là trạng thái Git có sẵn trước lượt gốc, không phải danh sách tệp do B tạo. Hai tệp đã sửa và 363 mục chưa được theo dõi được giữ nguyên.
```text
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/build_chapter2.py
 M outputs/reports/MP1_R_PHASE_6_2026-10-02/chapter2_readable_draft.md
?? .agents/skills.json
?? data/LR-FORMATED-rewrite.docx
?? data/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv
?? data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md
?? data/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md
?? data/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md
?? data/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md
?? "data/chap1-2_citations/M07__2018-Mechanically Versatile Soft Machines through Laminar.txt"
?? "data/chap1-2_citations/M08__7.2019-Brancadoro-Toward a Variable Stiffness Surgical Manipulator Based on Fiber Jamming Transition.txt"
?? "data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.txt"
?? "data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.txt"
?? data/chap1-2_citations/M11__2022-A_3D_Printed_Soft_Robotic_Gripper_With_a_Variable_Stiffness_Enabled_by_a_Novel_Positive_Pressure_Layer_Jamming_Technology.txt
?? "data/chap1-2_citations/M13__2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.txt"
?? data/chap1-2_citations/M14__A_Novel_Continuum_Robot_With_Stiffness_Variation_Capability_Using_Layer_Jamming_Design_Modeling_and_Validation.txt
?? data/chap1-2_citations/M17__2023-Caruso-Layer_Jamming_Modeling_and_Experimental_Validation.txt
?? "data/chap1-2_citations/M24__2025-A new mechanical model of short wire ropes Theory and experimental.txt"
?? data/chap1-2_citations/MANIFEST.json
?? data/chap1-2_citations/README.md
?? docs/literature/LR_CH1_CH2_EVALUATION_FEAK_2026-10-14.md
?? docs/literature/MP1_R_PHASE_7_CLAIM_CITATION_SCIENTIFIC_INTEGRITY_AUDIT_2026-10-03.md
?? docs/literature/MP1_R_PHASE_8_CHAPTER_2_FINALIZATION_AND_RELEASE_LOCK_2026-10-04.md
?? docs/operations/MP1_R_PDF_HIGHLIGHT_CHECKPOINT_2026-10-03.md
?? docs/project/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx
?? docs/project/MP1_R_CHAPTER_2_PHASE_7_AUDITED_2026-10-03.docx
?? "docs/project/almost done/LR-FORMATED.docx"
?? docs/reports/LR_FORMATED_REWRITE_CH1_CH2_REVIEW_2026-10-14_VI.md
?? docs/reports/MP1_R_CH1_CH2_LITERATURE_MATRIX_2026-10-14_VI.md
?? "literature review/LR-FORMATED-rewrite-outline-de-xuat.docx"
?? "literature review/LR-FORMATED-rewrite.docx"
?? "literature review/LR-FORMATED.docx"
?? "literature review/MP1_R_CHAPTER_2_FINAL_RELEASE_2026-10-04.docx"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/CLAIM_SOURCE_MAP.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/DELIVERY_REPORT.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/HIGHLIGHT_REGISTER.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/README.md"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/VALIDATION.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/curated_passages.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/inputs.json"
?? "literature review/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03/pdf.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL.zip"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/01_OUTLINE_BULLET_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/02_SECTION_SOURCE_MATRIX.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/03_CHAPTER_2_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/04_CHAPTER_1_WRITING_BRIEFS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/05_CROSS_STUDY_COMPARISONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/06_FIGURE_TABLE_EQUATION_CANDIDATES.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/07_CITATION_AND_REFERENCE_CROSSWALK.csv"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/09_COVERAGE_AND_READINESS_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/10_EXECUTION_REPORT.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/11_CHAPTER_2_READINESS_GATE.md"
?? "literature review/MP1_WRITING_EVIDENCE_FINAL/12_R3_CHANGELOG.md"
?? "literature review/ma-tran-tong-quan-tai-lieu.docx"
?? "literature review/new citation/MP1_2_1_7_PDF_highlight_co_ma_truy_vet/citation_trace_2_1.json"
?? "literature review/~$-FORMATED-rewrite.docx"
?? "literature review/~$-FORMATED.docx"
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/CLAIM_SOURCE_MAP.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/DELIVERY_REPORT.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/HIGHLIGHT_REGISTER.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/MP1_R_CHAPTER_2_HIGHLIGHTED_SOURCES_2026-10-03.zip
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/PACKAGE_VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/README.md
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S01_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S03_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S04_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05a_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S05b_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S06_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S07_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S09_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S10_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S11_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S12_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S13_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S15_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S17_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S18_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/S22_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/V-W02_search_text.txt
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/VALIDATION.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/build_highlighted_pdfs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curate_annotations.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/curated_passages.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/inputs.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/package_highlights.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/pdf_text_geometry.json
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/prepare_inputs.py
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S01_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S03_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S04_P5.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S07_P6.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S09_P9.png
?? outputs/annotations/MP1_R_CHAPTER_2_CITED_EVIDENCE_2026-10-03/previews/S22_P71.png
?? outputs/literature/LR_CITATION_MATRIX_2026-10-14.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_RECONCILIATION.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/CORPUS_STATUS.csv
?? outputs/literature/MP1_READING_PACK/00_CORPUS/LOCATOR_READINESS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/METADATA_CONFLICTS.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/OUTLINE_MAPPING_CHECK.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/P0_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_CORPUS/SOURCE_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/CHAPTER_NOTES_SPECIFICATION.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/COVERAGE_AND_RISK_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/EVIDENCE_SCHEMA.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/OUTLINE_SECTION_REGISTRY.json
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P1_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/P2_WORK_PACKAGES.md
?? outputs/literature/MP1_READING_PACK/00_PLANNING/PAPER_SECTION_CROSSWALK.csv
?? outputs/literature/MP1_READING_PACK/00_PLANNING/SECTION_EXTRACTION_PLAN.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_APPLICABILITY_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_READING_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_SELECTION_MATRIX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_UNVERIFIED_ITEMS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/EQUATION_VARIABLE_GLOSSARY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_B_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_C_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/EQUATION_READING_NOTES/WP_D_EQUATION_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M01_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M02_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M03_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M04_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M05_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M38_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/PAPER_NOTES/M39_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_CONTENT_QUALITY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-A/WP_A_R1_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/M09_M10_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M06_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M07_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M08_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M09_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M10_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M11_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M12_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M13_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M14_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M15_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M16_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M19_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M20_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PAPER_NOTES/M21_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/PILOT_REUSE_STATUS.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/SCHEMA_VALIDATION.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-B/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_INDEX_PAPER_LEVEL_BACKUP.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M23_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M24_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M25_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M27_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M28_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M29_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M30_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M35_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/PAPER_NOTES/M36_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CHANGELOG.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-C/WP_C_R2_CONSISTENCY_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D.zip
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/LOCATOR_ISSUES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COMPLETION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PACKAGE_MANIFEST.json
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M31_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M32_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M33_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M34_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/PAPER_NOTES/M37_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_FULL/WP-D/TERMINOLOGY_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EQUATION_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_INDEX.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl
?? outputs/literature/MP1_READING_PACK/02_PILOT/FIGURE_TABLE_REGISTRY.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/HUMAN_REVIEW_QUEUE.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_CORRECTIONS.csv
?? outputs/literature/MP1_READING_PACK/02_PILOT/LOCATOR_VERIFICATION_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_R1_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/P2_PILOT_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M17_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M18_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M22_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PAPER_NOTES/M26_NOTES.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/PILOT_COVERAGE_REPORT.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/SCHEMA_FEEDBACK.md
?? outputs/literature/MP1_READING_PACK/02_PILOT/TERMINOLOGY_NOTES.md
?? outputs/plans/MP1_R_PHASE_7_AUDITED_CLAIM_TRACEABILITY_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_CITATION_AUDIT_MATRIX_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_FINDING_REGISTER_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_7_SOURCE_VERIFICATION_LOG_2026-10-03.json
?? outputs/plans/MP1_R_PHASE_8_CHAPTER_2_RELEASE_MANIFEST_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINALIZATION_CHANGELOG_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CITATION_REGISTER_2026-10-04.json
?? outputs/plans/MP1_R_PHASE_8_FINAL_CLAIM_TRACEABILITY_2026-10-04.json
?? outputs/reports/MP1_GLOSSARY_C2_3_1_REPORT_2026-10-16.md
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/actual_docx_inventory.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/artifact_integrity_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/citation_appearances_original.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/inspect_artifact.py
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05a_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S05b_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/S11_crossref.json
?? outputs/reports/MP1_R_PHASE_7_2026-10-03/metadata/V-W02_crossref.json
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_2_1/MP1_CH2_2_2_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_1/MP1_CH2_2_3_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_2/MP1_CH2_2_3_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_3/MP1_CH2_2_3_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_4/MP1_CH2_2_3_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_5/MP1_CH2_2_3_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_3_integrated/MP1_CH2_2_3_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_1/MP1_CH2_2_4_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_2/MP1_CH2_2_4_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_3/MP1_CH2_2_4_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_4/MP1_CH2_2_4_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_4_integrated/MP1_CH2_2_4_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_1/MP1_CH2_2_5_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_2/MP1_CH2_2_5_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_3/MP1_CH2_2_5_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_4/MP1_CH2_2_5_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_5/MP1_CH2_2_5_5_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_5_integrated/MP1_CH2_2_5_MASTER_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_DRAFT.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_4/MP1_CH2_2_6_4_TERMINOLOGY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_7_GATE_REVIEW.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_CITATION_RENUMBERING_MAP.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_EXECUTION_REPORT.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATED.docx
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_INTEGRATION_CHANGELOG.md
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_SOURCE_TRACEABILITY.csv
?? outputs/thesis_drafts/chapter_2/section_2_6_integrated/MP1_CH2_2_6_MASTER_TERMINOLOGY.csv

```

## Phạm vi kiểm tra cuối
Đã mở lại cả năm tệp và xác nhận không rỗng; phân tích ZIP/XML của DOCX, hai CSV và hai báo cáo Markdown. Có đúng năm tệp đích; mã và ảnh kiểm tra chỉ ở thư mục tạm B. Không đưa tệp vào vùng chờ Git, không tạo commit hoặc đẩy lên máy chủ. Các giới hạn khoa học vẫn được nêu rõ; đang chờ phê duyệt của con người.


## Ghi nhận lượt tiếp tục

RESUME_START_UTC: 2026-10-20T08:19:02Z

Thư mục tạm và tác vụ con của lượt gốc đã mất khi phiên được tiếp tục. Giữ nguyên các mốc thời gian gốc như ghi nhận lịch sử; không tạo lại sự kiện cũ. Lượt tiếp tục sửa tiêu đề bảng thuật ngữ, thay biểu thức văn bản bằng diễn giải điều kiện bằng tiếng Việt, bổ sung đơn vị ở hai hàng thuật ngữ, đồng bộ điểm neo CSV và dịch phần diễn giải báo cáo. 597 băm đầu vào và trạng thái Git ban đầu được giữ nguyên trong báo cáo. Kết xuất và rà soát mới được ghi bằng thời gian UTC thực. Tại thời điểm sửa và kết xuất mới, rà soát chéo còn chờ; kết quả phân xử cuối được ghi riêng ở dưới.

Đối chiếu siêu dữ liệu bổ sung từ nguồn chính do điều phối viên cung cấp: M13 https://ms.copernicus.org/articles/17/481/2026/ và GUM https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf. Các liên kết này không thay thế các đoạn PDF cục bộ đã kiểm.

ORIGINAL_DOCX_SHA256: a661c18c0fe83f37b24412c815ac3faa2a08e85a9d131709bb4f632844539ef9

Băm trên thuộc DOCX đã lưu của lượt gốc trước sửa; không thay cho băm hiện tại ở DOCX_SHA256.

## Kết xuất và tự rà soát mới

Đã xem riêng từng ảnh trang sau lần sửa cuối của DOCX. Không thấy chữ bị cắt, hàng bị cắt, hình thiếu, trang trắng hoặc chú thích bị tách khỏi hình. Tiêu đề bảng thuật ngữ và đơn vị uốn hiển thị đúng. Không thay đổi nội dung khoa học sau kết xuất này.

```json
{
  "render_completed_observed_utc": "2026-10-20T08:29:08.733334+00:00",
  "page_count": 5,
  "pdf_sha256": "40cdcc4cef6d4478858f13b4d76c11f8e0ff2cd60fc6f37771d48330167442d3",
  "page_text_lengths": [
    2809,
    1321,
    3019,
    2076,
    2125
  ],
  "visual_review_completed_utc": "2026-10-20T08:30:13.490495+00:00",
  "pages_visually_reviewed": [
    1,
    2,
    3,
    4,
    5
  ],
  "libreoffice_version": "24.2.7.2",
  "process_exit_code": 0,
  "pdf_path": "/tmp/mp1-parallel-resume-63e0r36a/B/render/MP1_CH2_2_2_3_DRAFT.pdf",
  "page_image_pattern": "/tmp/mp1-parallel-resume-63e0r36a/B/render/final-p{1..5}.png"
}
```

Lệnh kết xuất dùng thư mục đầu ra và hồ sơ riêng B; thư viện dùng chung chỉ đọc. Mã 0 đã được quan sát trước khi mở PDF.

```sh
LD_LIBRARY_PATH=/tmp/mp1-parallel-resume-63e0r36a/lo/usr/lib/libreoffice/program:/tmp/mp1-parallel-resume-63e0r36a/lo/usr/lib/x86_64-linux-gnu /tmp/mp1-parallel-resume-63e0r36a/lo/usr/lib/libreoffice/program/soffice -env:UserInstallation=file:///tmp/mp1-parallel-resume-63e0r36a/B/lo-profile --headless --convert-to pdf --outdir /tmp/mp1-parallel-resume-63e0r36a/B/render outputs/thesis_drafts/chapter_2/section_2_2_3/MP1_CH2_2_2_3_DRAFT.docx
```

## Băm các tệp bàn giao sau sửa

Không tự băm báo cáo này để tránh vòng phụ thuộc. Bốn băm sau thuộc đúng các tệp hiện tại; cần cập nhật nếu rà soát chéo yêu cầu sửa.

<!-- OUTPUT_MANIFEST_BEGIN -->
```json
{
  "MP1_CH2_2_2_3_7_GATE_REVIEW.md": "37ae7ff62e9f728c474404c580b68dd9069b1fddc395681d80e9deb7fd6a7765",
  "MP1_CH2_2_2_3_DRAFT.docx": "3b9cb65a0a2566d9ed44af6fd2e3c3d9c5891f5cf2d82b423f40bdaad8ac69ce",
  "MP1_CH2_2_2_3_SOURCE_TRACEABILITY.csv": "514418c27bdeaef445dfe9d0ec965c74ec3ad8323756ef99ef4718929f4479e0",
  "MP1_CH2_2_2_3_TERMINOLOGY.csv": "53b4a03d93d41b04bbebf3c8ff4a2a8d526d2834eee2ce510ead0c65733d44ae"
}
```
<!-- OUTPUT_MANIFEST_END -->

RESUME_CANDIDATE_FREEZE_UTC: 2026-10-20T08:30:13.490495+00:00

CROSS_WORKSTREAM_FINDINGS: CW-01; DIFFERENT_VALID_DOMAINS_RESOLVED_WITHOUT_MANUSCRIPT_CHANGE. Phê duyệt của con người vẫn HUMAN_APPROVAL_PENDING.

## Phân xử rà soát chéo cuối

CROSS_WORKSTREAM_FINDING: CW-01

SEVERITY: NONE

A_LOCATION: 2.2.2 P001–P008 và bảng thuật ngữ.

B_LOCATION: Thân bài 2.2.3, sơ đồ, bảng quan sát và bảng thuật ngữ.

SCIENTIFIC_CONFLICT: NONE

PROPOSED_RESOLUTION: Giữ các miền bổ trợ. A trình bày động học tiếp xúc và lịch sử tải; B phân biệt áp suất, traction, hợp lực và khả năng quan sát. M13 được dùng trong giới hạn kiến trúc nguồn ở mỗi mục; không chuyển luật hoặc tham số sang MP1.

RESOLUTION_STATUS: DIFFERENT_VALID_DOMAINS_RESOLVED_WITHOUT_MANUSCRIPT_CHANGE

Điều phối viên đã phân xử không có xung đột P1/P2 và không yêu cầu sửa bản thảo. Điều phối viên đã tái chạy mã nhúng từ báo cáo, xác nhận 113 bản ghi với không có điểm neo hoặc trích dẫn mồ côi, đồng thời xem cả năm trang kết xuất mới và sơ đồ hai mạch; phông thân bài Times New Roman hiển thị rõ, không cắt chữ. Báo cáo hỗ trợ Luna đã được mở lại tại /tmp/mp1-parallel-resume-63e0r36a/review/final_luna_review.md; SHA256 3623d97438ea2c8830141e333c4ff3b639e0ef5d802e69541377fcacfaf00be3.

Rà soát Luna là SELF_REVIEW_ONLY, hỗ trợ tự rà soát, chưa phải một chấp nhận độc lập hoặc phê duyệt của tác giả. Luna không mở lại PDF nguồn, không chạy bộ kiểm hoặc kết xuất của điều phối viên và không thực hiện tìm kiếm tính mới rộng. Backend thực tế của Luna là NOT_VERIFIABLE; backend của các vai trò yêu cầu trong tác vụ vẫn NOT_BACKEND_VERIFIABLE.

Mười đối chiếu của điều phối viên và báo cáo hỗ trợ Luna:

1. Hợp lực pháp tuyến cục bộ N_i không được đồng nhất với áp suất nguồn; đơn vị lực N khác đơn vị áp suất và traction Pa.

2. Giới hạn ma sát tĩnh là ngưỡng; lực tiếp tuyến thực không mặc nhiên bằng ngưỡng ở mọi trạng thái.

3. Phạm vi dính, trượt một phần và trượt hoàn toàn tương thích khi giữ rõ miền tiếp xúc hoặc miền mô hình; không suy dính cục bộ thành tác dụng liên hợp toàn bó.

4. Khóa ma sát của toàn hệ chưa có nghĩa mọi tiếp xúc đều dính; trượt hoàn toàn chưa có nghĩa mất ma sát hoặc mất toàn bộ độ cứng uốn còn lại.

5. Quy ước E[Pa], B/EI[N·m²], K[N/m hoặc N/mm], M[N·m] và κ[m⁻¹] nhất quán với mục 2.2.1.

6. Sơ đồ hai mạch ở mục 2.2.3 là sơ đồ khái niệm có điều kiện, không xác nhận cấu trúc tiếp xúc hoặc vị trí cảm biến MP1; mạch suy luận không phải đường truyền lực.

7. Vòng trễ toàn cục không xác định duy nhất tổn hao tại piston hoặc một giao diện; các đóng góp phụ thuộc cấu hình và trạng thái TiNi vẫn cần phân biệt.

8. Giữ H0a trong miền chuyển pha, H0b=NOT_FALSIFIED_LIVE_COMPETITOR và H1=INSUFFICIENT_EVIDENCE. Ánh xạ năm câu hỏi trong PDF sang bốn nhóm P3 và năm nhóm quyết định của con người vẫn chờ giải quyết.

9. Hai tiểu mục có hệ đánh số trích dẫn cục bộ riêng hợp lệ; năm tài liệu tham khảo và bốn DOI của B được giữ nguyên, GUM không được gán DOI.

10. Không ép gộp các thuật ngữ xuất hiện ở cả hai tiểu mục khi phạm vi và nguồn gốc diễn giải khác nhau.

HANDOFF_REPORT_UPDATED_UTC: 2026-10-20T08:42:30.775750+00:00

Bản DOCX và hai CSV giữ nguyên băm đã đóng băng; lượt cuối chỉ cập nhật hai báo cáo. Không có tệp bàn giao thứ mười một. Trạng thái COMPLETED_WITH_DOCUMENTED_LIMITATIONS và HUMAN_APPROVAL_PENDING được giữ nguyên. Bước tiếp theo AWAIT_TWO_INDEPENDENT_ACCEPTANCES do điều phối viên theo dõi riêng; rà soát hiện tại không được tính là hai chấp nhận độc lập.

## Đối chiếu nguồn gốc đồng thời và lượt tiếp tục

Sự đồng thời của lượt gốc đã được điều phối viên xác nhận bằng quan sát công cụ thực tế thấy cả hai tác vụ RUNNING, cùng các khoảng A 2026-10-20T07:43:38Z đến 07:51:47.263992Z và B 2026-10-20T07:44:46Z đến 07:58:46Z, giao nhau 421.263992 giây. Đây là ghi nhận lịch sử, không tạo lại tệp sự kiện gốc. Lượt tiếp tục cũng có hai chủ sở hữu hoạt động đồng thời, nhưng không dùng điều đó thay bằng chứng đồng thời gốc.

Sau khi thư mục tạm gốc mất, điều phối viên khôi phục danh sách 597 đầu vào từ chính báo cáo B đã lưu và xác nhận khớp toàn bộ trước khi các chủ sở hữu sửa. Nguồn và các DOCX nền đều khớp. Các mốc đóng băng bản thảo gốc, lượt tiếp tục và cập nhật bàn giao cuối được giữ riêng.

## Ngoại lệ hiện trạng Git cuối

Điều phối viên quan sát phần tăng thêm so với trạng thái gốc gồm 10 tệp bàn giao được cho phép và một tệp khóa kiểu Word ngoài phạm vi ghi và phạm vi bàn giao: outputs/thesis_drafts/chapter_2/section_2_3_integrated/~$1_CH2_2_3_INTEGRATED.docx. Tệp khóa có kích thước 162 byte, ctime và mtime 2026-10-20T08:34:39Z, không có trong trạng thái gốc 365 mục hoặc ảnh chụp trạng thái tiếp tục 375 mục. ORIGIN: NOT_ATTRIBUTED. Không xóa hoặc sửa tệp khóa này; giữ nguyên thay đổi có thể do hoạt động đồng thời. Các lệnh B trong lượt tiếp tục không mở DOCX nền bằng Word hoặc LibreOffice và không nhắm ghi tệp khóa; không đủ bằng chứng để quy nguồn gốc của nó. Theo kiểm tra của điều phối viên, cả 597 đầu vào và các DOCX nền vẫn khớp băm; phần khác biệt đã theo dõi và vùng chờ Git không đổi. Đây là giới hạn bảo toàn hiện trạng, không phải xung đột khoa học P1/P2.

LOCK_EXCEPTION_RECORDED_UTC: 2026-10-20T08:49:10.630622+00:00

GATE_7: PASS_WITH_DOCUMENTED_LIMITATIONS

P1_P2_UNRESOLVED: 0 trong phạm vi khoa học tự rà soát; nguồn gốc tệp khóa vẫn NOT_ATTRIBUTED. Trạng thái COMPLETED_WITH_DOCUMENTED_LIMITATIONS, HUMAN_APPROVAL_PENDING và bước tiếp theo AWAIT_TWO_INDEPENDENT_ACCEPTANCES giữ nguyên.
