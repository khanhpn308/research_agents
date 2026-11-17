# Tự kiểm bảy gate cho bản thảo §2.2.1

TASK_ID: MP1-CH2-2.2.1-RESEARCH-THESIS-DRAFT
REVIEW_AUTHORITY: SELF_REVIEW_ONLY
AUTHOR_APPROVAL_STATUS: HUMAN_APPROVAL_PENDING
FINAL_INDEPENDENT_ACCEPTANCE: REQUIRED, NOT_PERFORMED
FINAL_SELF_REVIEW_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; chuyển người nghiệm thu độc lập, chưa nghiệm thu khoa học cuối.

## Phạm vi và cách đọc kết quả

Đối tượng là duy nhất `2.2.1. Robot continuum và các đại lượng độ cứng`. ROOT viết và phân xử; ba worker hỗ trợ đối chiếu trong cùng phiên. Các nhận xét của worker không tạo thành nghiệm thu độc lập. PASS dưới đây là kết quả tự kiểm theo phạm vi nhiệm vụ; không phê duyệt thiết kế, protocol hoặc giả thuyết MP1.

## Gate 1 — Dàn ý và phạm vi

STATUS: PASS
METHOD: ROOT mở trực tiếp PDF canonical, trích văn bản và xem ảnh trang vật lý 11; tính SHA-256; đối chiếu 14 đoạn Word với hai bullet.
EVIDENCE: `/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/04_WRITING_EVIDENCE_PACK/00_INPUTS/LR-FORMATED-rewrite-outline-de-xuat(2).pdf`; SHA256 `18ec221fa39ccad04fa25bafa5c0e2e97384d39e831827595ae62b0f1534c35e`. Trang nằm dưới §2.2 Thuật ngữ và khung cơ học, trước §2.2.2 và §2.2.3. Word chỉ có heading chính thức, glossary và tài liệu tham khảo.
COUNTS: 2/2 bullet, 14 đoạn nội dung, 0 heading tiểu mục mới, 0 mục 2.2.2/2.2.3/2.1 được viết.
FINDINGS: B01 được bao phủ ở P001–P009 và glossary; B02 ở P004, P010–P014. Mạch đi từ đối tượng vật lý và biểu diễn hình học đến cấp đại lượng, giả thiết dầm và giới hạn chuyển động nội tại; không phải danh sách định nghĩa mở rộng.
SEVERITY: Không có P1/P2.
UNRESOLVED: Không có xung đột dàn ý.
FINAL_DECISION: PASS cho đúng §2.2.1; không ủy quyền tích hợp §2.2.

B01 nguyên văn: Định nghĩa vật thể, dầm tương đương, độ cứng vật liệu, độ cứng uốn và độ cứng đầu công tác.

B02 nguyên văn: Giải thích điều kiện khi dùng mô hình dầm và khi chuyển động tương đối giữa các phần tử làm mô hình dầm đơn không còn đủ.

## Gate 2 — Nguồn và truy vết claim

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: ROOT đọc các đoạn PDF sử dụng, đối chiếu fragment/trang và hash; parser giải tất cả anchor trên DOCX cuối; kiểm ID đã dùng tồn tại trong Evidence Records. Fragment được đối chiếu sau chuẩn hóa NFKC và bỏ ký tự không phải chữ/số để loại khác biệt xuống dòng, gạch nối và ligature; đây chỉ là kiểm vị trí văn bản. Sức hỗ trợ khoa học được ROOT tự đọc và phân xử.
EVIDENCE: SOURCE_TRACEABILITY.csv có đường dẫn tuyệt đối, hash, trang vật lý/trang in, locator, fragment, vai trò nguồn, loại claim và giới hạn. M02-E02 ở WP-A; M22-E02 ở Pilot; M31-E07 ở WP-D. Các đoạn bổ sung không được cấp Evidence ID trong phiên.
COUNTS: 60 dòng = 46 dòng nội dung cho 42 span câu riêng biệt + 14 dòng glossary. 34/34 fragment khớp; 0 anchor chưa giải; 5608/5608 ký tự không trắng của nội dung nằm trong span. Đếm phủ văn bản không tự chứng minh tính đầy đủ ngữ nghĩa; ROOT đã đọc lại từng câu. 5 PDF, 12 trang vật lý khác nhau thực sự dùng cho claim. 3 Evidence ID duy nhất.
FINDINGS: M03-E02 trong WEP ghi PDF3/§1.2/Table1 nhưng PDF3 là §2.1.1/Fig.1. Không dùng locator sai hoặc tự gán ID đó cho trang 9. M03 trang 1/9 được kiểm trực tiếp, ghi SOURCE_VERIFIED_NO_REGISTERED_EVIDENCE_ID. M22 DOI một số record bị rút gọn; DOI đầy đủ được đọc trên PDF1 và ghi trong CSV, giữ registry nguyên trạng. Không lặp phần diễn giải quá mức của brief về việc chuyển tiếp độ cứng nhất thiết đòi mô hình phân lớp.
SEVERITY: P3 provenance lịch sử, đã cô lập khỏi lập luận bản thảo. Không còn P1/P2 trong bản thảo.
UNRESOLVED: Chỉnh locator/DOI của registry lịch sử nằm ngoài quyền hạn tác vụ; không còn locator nguồn đang dùng chưa kiểm. Không tuyên bố đã kiểm toàn bộ mỗi bài. Các hàng suy luận mang INFERENCE_FROM_VERIFIED_SELECTED_PDF_PASSAGE; định nghĩa/quy ước tách khỏi kết quả thực nghiệm.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS; có thể nghiệm thu độc lập từ chính CSV và PDF, không phụ thuộc scratch.

## Gate 3 — Đúng đắn khoa học

STATUS: PASS
METHOD: ROOT đọc lại Word theo các phủ định/ranh giới V-A, V-D, V-E; đối chiếu P3 canonical và phản biện của worker A/B/C.
EVIDENCE: M02 PDF2,5–7; M03 PDF9; M22 PDF1–3; các dòng C001–C060. P003 giữ bó TiNi là cấu trúc ứng viên; P010 tách bỏ qua cắt khỏi tuyến tính hóa hình học; P012 giữ giá trị mô hình dầm có trượt; P013 tách mô tả, dự đoán và quy kết cơ chế.
COUNTS: 0 kết quả thực nghiệm MP1, 0 novelty claim mới, 0 phê duyệt prototype/cấu hình, 0 sửa trạng thái giả thuyết.
FINDINGS: Độ cong hằng có điều kiện; chuyển vị lớn không tự bác bỏ mọi dầm; cùng độ võng không đồng nghĩa cùng biến dạng dọc; độ phù hợp toàn cục không nhận dạng duy nhất tiếp xúc. Không dùng kéo TiNi để xác lập luật uốn MP1. Không đồng nhất trượt với ma sát bằng không hoặc biến dạng dẻo.
SEVERITY: Không có P1/P2.
UNRESOLVED: Năm quyết định con người vẫn mở; chúng không ngăn soạn khung thuật ngữ có điều kiện.
FINAL_DECISION: PASS; H0b/H1 và các kết luận P3 được bảo toàn.

## Gate 4 — Cơ học và thứ nguyên

STATUS: PASS
METHOD: Kiểm từng đại lượng trong nội dung, glossary và CSV; kiểm mô hình liên hệ, nhánh và điều kiện suy đại lượng; đọc M02 PDF6, M31 PDF6, M22 PDF2–3 và M26 PDF2/8.
EVIDENCE: P005–P010; các thuật ngữ T005–T012. E: Pa=N/m²; I: m⁴; B hoặc EI: N·m²; K lực–chuyển vị: N/m hoặc N/mm; M: N·m; κ: m⁻¹. Độ dốc mô men theo độ cong có đơn vị N·m².
COUNTS: 0 phương trình hiển thị/OMML; 0 công thức quy đổi MP1; 0 giá trị tham số MP1; 7 ký hiệu chính E/I/B/EI/K/M/κ được phân cấp.
FINDINGS: Không viết luật tuyến tính tổng quát cho TiNi hoặc hệ có trượt. Thay đổi độ cong được phân biệt với độ cong tuyệt đối trong văn xuôi. Tiếp tuyến/cát tuyến được định nghĩa trên nhánh/điểm; K cần vị trí/phương tải, chuyển vị, chiều dài/cấu hình, gá, trạng thái và miền. M31 chỉ minh họa phép đo và suy EI công xôn; không chuyển công thức cho MP1. Bề mảnh và giả thiết tiết diện được bổ sung tường minh trong P010 rồi chạy lại parser/render.
SEVERITY: Không có P1/P2.
UNRESOLVED: Không có phương trình cần audit dấu/render; không chọn lý thuyết dầm hay ngưỡng độ mảnh cuối cho MP1.
FINAL_DECISION: PASS.

## Gate 5 — Thuật ngữ và liên tục với baseline

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Đọc terminology/source traceability master và ngữ cảnh Word §§2.3–2.6; dùng cách phân biệt chặt hơn ở §2.6; kiểm từng ô glossary bằng parser với CSV.
EVIDENCE: 12 tệp baseline DOCX/terminology/traceability được hash trước/sau; T005–T008 và T010–T012; đoạn chuyển P014.
COUNTS: 14/14 thuật ngữ/ô tương ứng khớp nguyên văn; 0 sửa baseline. §2.6 hash khớp kỳ vọng d2c4715283d637578454d09635237e7135912263a8df391e6fc9a477a52f097b.
FINDINGS: CROSS_SECTION_TERMINOLOGY_FINDING-01: §2.3 dùng “độ cứng uốn” khá rộng, §2.6 phân biệt B/EI với K. Bản thảo mới khai báo ký hiệu/đơn vị, không sửa thuật ngữ cũ. FINDING-02: mô đun hiệu dụng suy từ phép thử trong §2.5–§2.6 khác mô đun vật liệu E; §2.2.1 không đưa thêm E_eff hoặc một phép nhận dạng mới. Không sửa minor errata §2.5. “Trượt tại giao diện” theo động học §2.4; không triển khai các miền dính/trượt chi tiết.
SEVERITY: P3 khác mức khái quát thuật ngữ, có giải thích; không còn P1/P2.
UNRESOLVED: Người nghiệm thu quyết định việc thống nhất cách gọi ở toàn chương trong một tác vụ riêng; không phụ thuộc việc đó để hiểu các định nghĩa hiện tại.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS.

## Gate 6 — Citation, văn phong và Word

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS
METHOD: Parser đối chiếu thứ tự first-use, reference/DOI, XML/ZIP, kiểu trang, lề, font, bảng. ROOT đọc văn bản và xem trực tiếp tất cả trang render cuối bằng LibreOffice 24.2.7.2 cục bộ trong scratch. Dùng academic-humanizer/unslop để sửa diễn đạt, không làm mạnh claim.
EVIDENCE: DOCX SHA256 `9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba`; 13 phần XML parse được; PDF render SHA256 `e868cd4b06073f7043bc640e34bf4594461046eea028b293041a4513ae5c63ae`. Font thực sự dùng trong PDF cuối chỉ TimesNewRomanPSMT và TimesNewRomanPS-BoldMT. A4, lề trái3/phải2/trên-dưới2.5 cm; body12pt, giãn dòng1.15; glossary10.5pt; Heading styles, màu đen, không header/footer/watermark.
COUNTS: 5 reference/5 DOI; 27 citation nội dung + 8 glossary = 35 occurrence, không tính 5 nhãn bibliography. 0 orphan citation/reference. 1 bảng native gồm 14 hàng dữ liệu, có lặp tiêu đề; 0 hình; 4/4 trang đã xem trực tiếp. 0 dòng/ô bị cắt, 0 trang trắng.
FINDINGS: Lượt render đầu lộ font/màu Heading theo theme Word mặc định; đã bỏ theme và đặt Times New Roman/màu đen, render lại toàn bộ. Đoạn P007 nối qua trang1–2, vẫn đủ dòng; P014 bắt đầu trang3, không mất nội dung. Bảng tách giữa các hàng và lặp header ở trang4. Tài liệu M26 là bản article-in-press: giữ số trang in1–18 của PDF trong traceability, phân biệt pagination3009–3026 ở bản xuất bản được đối chiếu publisher. Không thêm nội dung workflow vào manuscript.
SEVERITY: P3 giới hạn ứng dụng Word; không có P1/P2 về bố cục hoặc cơ học.
UNRESOLVED: MICROSOFT_WORD_VALIDATION: NOT_VERIFIED. Runtime LibreOffice portable có cảnh báo Java/liblangtag khi chạy; tiến trình xuất PDF trả0 và toàn bộ văn bản/font/trang cuối được kiểm. Không dùng kết quả render để tuyên bố tương đương mọi phiên bản Word.
FINAL_DECISION: PASS_WITH_DOCUMENTED_LIMITATIONS.

## Gate 7 — Đóng gói, bảo toàn và tái lập

STATUS: PASS
METHOD: So manifest SHA-256 trước/sau, git status -uall và diff/staged diff byte-for-byte; reopen cả năm đầu ra; chạy lại bộ kiểm dưới đây; xác nhận chỉ năm deliverables trong thư mục final.
EVIDENCE: Execution report chứa đầy đủ pre-status, input manifest196 tệp, hash bốn baseline DOCX cùng các CSV, manifest bốn output còn lại và mã kiểm tự chứa. Scratch/PDF/PNG/script/runtime không nằm trong final.
COUNTS: 196/196 input bảo toàn; 12/12 baseline DOCX/master CSV bảo toàn; 2 modified và 358 untracked có sẵn giữ nguyên; đúng5 file mới; 0 stage/commit/push/checkout/reset/restore/pull/rebase/clean; 0 sửa registry/scientific state/P3.
FINDINGS: Thư mục target chưa có output khi pre-flight; không có xung đột TASK_ID hoặc ghi đè tác vụ khác. Chỉ cập nhật các file do chính tác vụ này tạo trong quá trình sửa và render. Không tự kiểm toàn bộ corpus hoặc hoàn tất human approvals.
SEVERITY: Không còn P1/P2 trong phạm vi tự kiểm.
UNRESOLVED: Chờ phê duyệt tác giả và nghiệm thu độc lập. Hash tự thân của execution report không nhúng vào chính nó để tránh tự tham chiếu; lệnh hash tất cả năm tệp ở cuối report cho phép người nghiệm thu tạo manifest ngoài thư mục final.
FINAL_DECISION: PASS; chỉ dừng ở bản thảo §2.2.1.

## Phân xử nhận xét worker

Worker A/B không phát hiện lỗi P1/P2 về source hoặc phạm vi ở candidate. Worker C đề nghị làm rõ phương trượt, độ cong hiện tại và câu K dày; ROOT đã thêm “trượt dọc tương đối”, giữ phân biệt độ cong/thay đổi độ cong ở P006–P007, và giữ câu K vì liệt kê điều kiện đo cần thiết. Gợi ý độ cong/câu K được phân xử là cải thiện văn phong mức P3, không phải sai cơ học tồn đọng. Ghi chú lịch sử M03 bị copy trang9 vào dòng PDF1 đã sửa theo locator riêng từng dòng. ROOT bổ sung điều kiện thân dài/mảnh ở P010; hai binding bổ sung được kiểm trực tiếp với M02 PDF6 và M03 PDF9. Mọi sửa được chạy lại parser và xem lại render cuối. Kết luận không dựa vào đa số worker.

## Kết quả đếm trên tệp cuối

```json
{
  "body_paragraphs": 14,
  "claim_records": 60,
  "claim_categories": {
    "SOURCE_GROUNDED_CLAIM": 12,
    "CROSS_STUDY_INFERENCE": 12,
    "AUTHOR_SYNTHESIS": 14,
    "DEFINITION_OR_CONVENTION": 21,
    "PENDING_HUMAN_DECISION": 1
  },
  "body_claim_records": 46,
  "glossary_claim_records": 14,
  "source_fragment_checks": 34,
  "unresolved_source_fragments": 0,
  "body_unique_claim_spans": 42,
  "unresolved_anchors": 0,
  "body_nonspace_characters": 5608,
  "covered_body_nonspace_characters": 5608,
  "terminology_entries": 14,
  "glossary_entries": 14,
  "references": 5,
  "unique_dois": 5,
  "citation_occurrences_body": 27,
  "citation_occurrences_glossary": 8,
  "orphan_citations": 0,
  "orphan_references": 0,
  "omml_equations": 0,
  "figures": 0,
  "scientific_tables": 0,
  "glossary_tables": 1,
  "xml_parts": 13,
  "docx_sha256": "9a332dd845352f5afcc0d821e2e0e2f28d805b92265ad8547c28b2a800a2dbba",
  "evidence_ids": [
    "M02-E02",
    "M22-E02",
    "M31-E07"
  ],
  "source_papers": [
    "M02",
    "M03",
    "M22",
    "M26",
    "M31"
  ]
}
```

## Mã kiểm tái lập

Lưu code dưới đây bên ngoài thư mục final và chạy bằng Python có python-docx, lxml, pymupdf. Không cần bất kỳ tệp nào trong scratch của phiên này. Mã kiểm cấu trúc/anchor/hash/fragment; kiểm ý nghĩa claim và quan sát bố cục vẫn cần người đọc. Cơ sở chỉ số body là các đoạn sau heading chính và trước heading glossary; Gxxx là hàng glossary, không tính header. Offset là Unicode code point, 0-based, end-exclusive. Citation occurrence không gồm số nhãn bibliography.

```python
import csv,json,re,zipfile,hashlib,sys,unicodedata
import pymupdf
from pathlib import Path
from collections import Counter
from lxml import etree
from docx import Document
ROOT=Path('/home/khanh/projects/mechanical-research-agents')
OUT=ROOT/'outputs/thesis_drafts/chapter_2/section_2_2_1'
HEADING='2.2.1. Robot continuum và các đại lượng độ cứng'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def check():
 d=Document(OUT/'MP1_CH2_2_2_1_DRAFT.docx')
 text=[p.text for p in d.paragraphs]
 assert text[0]==HEADING
 gi=text.index('Bảng thuật ngữ dùng trong tiểu mục');ri=text.index('Tài liệu tham khảo')
 body=text[1:gi];refs=text[ri+1:]
 assert len(d.tables)==1
 terms=list(csv.DictReader((OUT/'MP1_CH2_2_2_1_TERMINOLOGY.csv').open(encoding='utf-8-sig')))
 claims=list(csv.DictReader((OUT/'MP1_CH2_2_2_1_SOURCE_TRACEABILITY.csv').open(encoding='utf-8-sig')))
 assert len({r['claim_id'] for r in claims})==len(claims)
 assert len(terms)==len(d.tables[0].rows)-1
 for i,t in enumerate(terms,1):
  assert int(t['word_glossary_row'])==i
  assert [c.text for c in d.tables[0].rows[i].cells]==[t['word_term_text'],t['word_definition_and_context'],t['word_source_text']]
 mapped=Counter();covered=set()
 for c in claims:
  i=int(c['paragraph_id'][1:])-1
  actual=body[i] if c['anchor_container']=='body' else d.tables[0].rows[i+1].cells[1].text
  a,b=int(c['anchor_start']),int(c['anchor_end'])
  assert actual[a:b]==c['manuscript_anchor'],c['claim_id']
  assert actual.count(c['manuscript_anchor'])==1,c['claim_id']
  if c['anchor_container']=='body':
   mapped[c['paragraph_id']]+=1;covered.update((i,j) for j in range(a,b) if not actual[j].isspace())
  if c['canonical_pdf_path']:
   assert sha(c['canonical_pdf_path'])==c['canonical_pdf_sha256']
   assert int(c['verified_physical_pdf_page'])>0
   with pymupdf.open(c['canonical_pdf_path']) as pdf:
    page=pdf[int(c['verified_physical_pdf_page'])-1].get_text()
   def normalize(s):return ''.join(x for x in unicodedata.normalize('NFKC',s).lower() if x.isalnum())
   assert c['source_fragment'] and normalize(c['source_fragment']) in normalize(page),c['claim_id']
  if c['claim_category']=='SOURCE_GROUNDED_CLAIM':assert c['canonical_paper_id']
 assert len(mapped)==len(body)
 total=sum(not x.isspace() for p in body for x in p)
 assert len(covered)==total
 cite=[int(n) for n in re.findall(r'\[(\d+)\]','\n'.join(body))]
 first=list(dict.fromkeys(cite));refnums=[int(re.match(r'\[(\d+)\]',r).group(1)) for r in refs]
 assert first==refnums==list(range(1,len(refs)+1))
 assert set(cite)==set(refnums)
 dois=re.findall(r'DOI: (.+)\.$','\n'.join(refs),re.M);assert len(dois)==len(set(dois))==len(refs)
 with zipfile.ZipFile(OUT/'MP1_CH2_2_2_1_DRAFT.docx') as z:
  assert z.testzip() is None
  xmls=[n for n in z.namelist() if n.endswith('.xml')]
  for n in xmls:etree.fromstring(z.read(n))
  root=etree.fromstring(z.read('word/document.xml'));ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
  assert not root.findall('.//w:headerReference',ns) and not root.findall('.//w:footerReference',ns)
  assert root.find('.//w:tblHeader',ns) is not None
  omml=len(root.findall('.//m:oMath',ns));figs=len(root.findall('.//w:drawing',ns))
  assert not omml and not figs
 sec=d.sections[0]
 for actual,cm in [(sec.page_width,21),(sec.page_height,29.7),(sec.left_margin,3),(sec.right_margin,2),(sec.top_margin,2.5),(sec.bottom_margin,2.5)]:assert abs(actual.cm-cm)<.003
 assert d.styles['Normal'].font.name=='Times New Roman'
 assert d.styles['Normal'].font.size.pt==12
 assert d.styles['Normal'].paragraph_format.line_spacing==1.15
 assert not any(re.search(r'^2\.2\.[23]|^2\.2\.1\.\d',t) for t in text)
 counts=dict(body_paragraphs=len(body),claim_records=len(claims),claim_categories=dict(Counter(c['claim_category'] for c in claims)),body_claim_records=sum(c['anchor_container']=='body' for c in claims),glossary_claim_records=sum(c['anchor_container']!='body' for c in claims),source_fragment_checks=sum(bool(c['canonical_pdf_path']) for c in claims),unresolved_source_fragments=0,body_unique_claim_spans=len({(c['paragraph_id'],c['anchor_start'],c['anchor_end']) for c in claims if c['anchor_container']=='body'}),unresolved_anchors=0,body_nonspace_characters=total,covered_body_nonspace_characters=len(covered),terminology_entries=len(terms),glossary_entries=len(terms),references=len(refs),unique_dois=len(dois),citation_occurrences_body=len(cite),citation_occurrences_glossary=sum(len(re.findall(r'\[(\d+)\]',r['word_source_text'])) for r in terms),orphan_citations=0,orphan_references=0,omml_equations=omml,figures=figs,scientific_tables=0,glossary_tables=1,xml_parts=len(xmls),docx_sha256=sha(OUT/'MP1_CH2_2_2_1_DRAFT.docx'),evidence_ids=sorted({r['evidence_ids'] for r in claims if r['evidence_ids']}),source_papers=sorted({r['canonical_paper_id'] for r in claims if r['canonical_paper_id']}))
 return counts
if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))

```
