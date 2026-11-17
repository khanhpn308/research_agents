# Kiểm tra bảy Gate — §2.6.4
TASK_ID: MP1-CH2-2.6.4-RESEARCH-THESIS-DRAFT

REVIEW_AUTHORITY: SELF_REVIEW_ONLY

DOCX_SHA256: `607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45`

Không phải nghiệm thu độc lập. Gate chỉ đánh giá bản thảo chuyển tiếp và hồ sơ nguồn; không nghiệm thu thiết kế/thí nghiệm.

## GATE 1 — ORIGINAL OUTLINE COMPLIANCE

STATUS: PASS

METHOD: ROOT+workerC đọcPDF15 bằngPyMuPDF; ROOT xem ảnh trang; đối chiếuCSV/WEP vàWord anchors.

EVIDENCE: PDFcanonical physical15; mapping dưới đây; WEP264; WordP01–P14.

COUNT: 8 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] Đọc trực tiếp PDF canonical physical15, gồm giới hạn tiểu mục và đúng tên chính thức.
- [x] Đủ ba bullet B01–B03; nguyên văn đối chiếu PDF và Crosswalk.
- [x] WEP Writing Brief riêng264, Source Matrix và readiness được đối chiếu.
- [x] Mỗi bullet có câu hỏi → bằng chứng → nguồn/phương pháp → quan sát → phụ thuộc → kết luận → Word.
- [x] Không lấy candidate/framework thay bullet; không lặp dài §§2.3–2.6.3.
- [x] Không viết Chương3–4 hoặc tích hợp toàn§2.6.
- [x] Phân biệt nguồn công bố, suy luận, đề xuất và quyết định nội bộ chưa được duyệt.
- [x] Không đổi tên từ DOCX cũ; sai khác phiên bản dàn ý được ghi nhận.

FINDINGS: Đủ3bullet. PDF/WEP được ưu tiên đúng provenance; DOCX dàn ý rút gọn khác cấu trúc không được dùng thayPDF.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: AUTHOR_APPROVAL_PENDING; không phê duyệt bất kỳ thiết kế nào.

## GATE 2 — SCIENTIFIC CLAIM TRACEABILITY

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: Python csv/json parsing; original EVIDENCE_RECORDS đối chiếu nguyên bản; kiểm từng57anchor và10row Word.

EVIDENCE: SOURCE_TRACEABILITY CSV, Word anchors, các phụ lục source/QA/render và ExecutionReport của chính task.

COUNT: 10 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] 57/57 claim có provenance và anchor đúng chính DOCX hash cuối.
- [x] 19 Evidence IDs có thật, giữ nguyên record JSONL/path/line; không tạo ID.
- [x] 6 source identities/path/hash và locators nguồn được đối chiếu; internal requirements không gán journal IDs.
- [x] SOURCE_GROUNDED_CLAIM/INFERENCE/AUTHOR_PROPOSAL/PENDING_HUMAN_DECISION tách riêng.
- [x] DIRECT_SUPPORT là kết quả hệ nguồn, COMPARATOR không thành direct MP1 proof; GUM là METHODOLOGY.
- [x] Multi-source giữ locator và phần hỗ trợ theo từng EID; không giả locator gộp.
- [x] DOCUMENT_COVERAGE/P3 internal không được đếm như kết quả thực nghiệm; category này có0record.
- [x] Negative claims chỉ giới hạn miền hệ nguồn/bằng chứng MP1, không toàn thế giới.
- [x] 47 anchor đoạn +10 anchor glossary;0unresolved; glossary CSV=Word theo danh tính/nghĩa/ngữ cảnh/nguồn.
- [x] Canonical original locator được giữ cạnh corrected/additional direct fragments, không âm thầm sửa registry.

FINDINGS: 57record/63columns, giữ53columns263 vàthêm10;0anchor thất lạc/0glossary mismatch. Định nghĩaGUM có fragment trực tiếp bổ sung được gắn nhãn riêng.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: FragmentGUM ngoài original EID locator được khai báo additional_direct_pdf_fragment; không tạo canonicalEID mới.

## GATE 3 — ORIGINAL PDF / EQUATION / FIGURE VERIFICATION

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: ROOT mở trang chọn lọc6contentPDF+M28, riêngM38 model/definitions; workersA/B tái đọc nguồn. Đối chiếu physical/printed locators.

EVIDENCE: SOURCE_TRACEABILITY CSV, Word anchors, các phụ lục source/QA/render và ExecutionReport của chính task.

COUNT: 12 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] Mở PDF canonical của cả6nguồn dùng và M28 hỗ trợ metadata; tách directROOT và worker pages.
- [x] Trang vật lý/trang in, hình học, vật liệu, sơ đồ tải và điều kiện nguồn được giữ.
- [x] M13 nylon/positive-pressure bending khác MP1; không chuyển cận hoặc protocol nguồn.
- [x] M31 kéo dây–cao su khác quan sát mọi trượt dây trong uốn; số lần lặp nguồn không thành yêu cầu MP1.
- [x] M26 nearly-isothermal tension và chu trình khác uốn; pha/nhiệt/lịch sử nguồn không thành ngưỡng MP1.
- [x] M34 có thực nghiệm động và cột áp tĩnh; không gộp cực đại khác chế độ thành một khả năng đồng thời.
- [x] M16 áp âm và calibration/control được phân biệt; fitted data không gọi heldout predictive validation.
- [x] M38 là hướng dẫn đo; định nghĩa repeatability ởPDF47, model ở20–21, covariance ở31/33.
- [x] Số liệu/protocol nguồn không được sao sang lựa chọn MP1; chỉ có đơn vị cơ học được dùng trong prose.
- [x] M13 Eq4 dimensional warning được đọc lại ởPDF3; Equation Notes B06/B07 không thay kiểm Eq4; không dùng/sửa Eq4.
- [x] N/A: tái tạo phương trình/hình/bảng khoa học nguồn vì số lượng0; prose vẫn kiểm PDF.
- [x] Không đồng nhất mở trang chọn lọc với kiểm độc lập toàn bài hoặc nghiệm thu ngoài phiên.

FINDINGS: 7PDF phục vụ6nguồn+metadata đã kiểm trang chọn lọc; không full-paper external re-audit. Source choices/protocol không chuyển sangMP1.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: Chỉ kiểm các trang liên quan, không kiểm độc lập lại toàn corpus39bài; không đánh đồng WORKER_REPORTED với independent validation.

## GATE 4 — CROSS-STUDY SYNTHESIS

STATUS: PASS

METHOD: ROOT đọc văn xuôi theo cụm vấn đề; workerB phản chứng, không quyết định bằng đa số.

EVIDENCE: SOURCE_TRACEABILITY CSV, Word anchors, các phụ lục source/QA/render và ExecutionReport của chính task.

COUNT: 10 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] Tổng hợp pressure→contact→bending từM13 và phép đo giao diện riêngM31, không bỏ qua phần prior art đã có.
- [x] DùngM26 để giới hạn trạng thái/lịch sử vàM38 để xây dựng yêu cầu đo/lặp lại/bất định.
- [x] DùngM34 thừa nhận prior art SMA→pressure và nguồn động trước đề xuất tầng đặc trưng riêng.
- [x] DùngM16 thừa nhận nhận dạng và thí nghiệm điều khiển đã có; tách khỏi validationMP1.
- [x] Đối chiếu kiến trúc/vật liệu/gá/tải/đại lượng/giả thiết và mức bằng chứng khi liên quan.
- [x] Không coi áp âm và áp dương hoặc dây–cao su/dây–dây là tương đương.
- [x] Không cộng dữ liệu cùng nghiên cứu thành replication độc lập; không tổng hợp số/tỉ lệ qua phép đo không tương thích.
- [x] Không so E, B/EI vàK như một thang; không xếp hạng công nghệ hoặc tạo quy luật phổ quát.
- [x] Văn xuôi tổ chức theo câu hỏi BenchA/B và điều kiện bằng chứng, không liệt kê từng bài đơn lẻ.
- [x] Hai bench và việc kết hợp các cơ chế không phải novelty proof.

FINDINGS: Các nguồn đã giải quyết một phần được thừa nhận; đề xuất BenchA/B không đổi thành source finding hoặc novelty.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: Không có dữ liệuA/BMP1; đây là tổng hợp yêu cầu, không mô hình/phép đo đã vận hành.

## GATE 5 — MECHANICAL AND P3 BOUNDARIES

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: ROOT đối chiếuP3/WP-E/12hồ sơ263; workerC boundary/terms review; targeted recheck sau sửa.

EVIDENCE: SOURCE_TRACEABILITY CSV, Word anchors, các phụ lục source/QA/render và ExecutionReport của chính task.

COUNT: 16 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] Giữ H0b NOT_FALSIFIED_LIVE_COMPETITOR vàH1 INSUFFICIENT_EVIDENCE; định nghĩa từP3, không journal finding.
- [x] G00 đóng; G01–G08 có điều kiện; G09 prerequisite, G10 chưa thiết lập,G11 cấm novelty; không sửa canonical.
- [x] 5nhóm quyết định mở; không khóa topology/interface/sensor/range/repetitions/ngưỡng.
- [x] Nguồn áp suất ≠ gần mẫu ≠ local normal traction/contact force; proxy không là trường ứng suất.
- [x] Lực ma sát thực tế khác Coulomb limit; prose không suy từ threshold thành actual friction.
- [x] Local stick không tự fully-composite; full slip không zero friction hay dây uốn độc lập; không đưa các cận sai vào Word.
- [x] E(Pa) khác B/EI(N·m²),K(N/m hoặcN/mm); F–δ→M–κ cần mô hình/hình học/biên/curvature.
- [x] Vòng trễ không định danh duy nhất TiNi/ma sát/giao diện; vật liệu phụ thuộc pha,nhiệt,tốc độ,lịch sử.
- [x] Cấu trúc mô hình vàtham số phải được khóa trước reserved data; không dùng lại validation để chọn mô hình.
- [x] Không transfer nguyên mô hình layer/fiber/granular tớiMP1 hoặc mặc định luật cấu thành mới.
- [x] Không tuyên bố đã đo tham số/traction, vận hành piston hay hoàn thành thí nghiệm MP1.
- [x] Không bác H0b/chứng H1/tính mới tuyệt đối từ thiếu dữ liệu corpus.
- [x] Null/inconclusive khác zero effect vàkhông bị ép thành positive novelty.
- [x] Tách readiness vận hành, comparability vàđủ bằng chứng kết luận; tách physical stop với hạn chế diễn giải.
- [x] NămPDF-RQ vàbốnP3-groups giữ namespace/mapping PROVISIONAL_MANY_TO_MANY; HUMAN_DECISION_PENDING.
- [x] Không đóng băng BenchA/B hoặc protocol; mọi dự kiến kèm phạm vi kết luận.

FINDINGS: 2P2 ban đầu được sửa vàtargeted workerC đóng: giao diện thực tế chưa biếtdominance; reserveddata không dùng chọn cấu trúc mô hình. Không cònP1/P2.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: 5human decisions vàRQmap5↔4 chưa khóa; giới hạn khoa học hợp lệ, không lỗi phải ép giải quyết.

## GATE 6 — CITATIONS AND REFERENCES

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: PDF firstpage/headers/DOI; M28PDF19metadata secondary; regex firstuse/citations/bibliography.

EVIDENCE: SOURCE_TRACEABILITY CSV, Word anchors, các phụ lục source/QA/render và ExecutionReport của chính task.

COUNT: 10 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] Đối chiếu author names/order,title,venue,year,volume/issue/pages/article number/DOI theoPDF.
- [x] M26 volume/pages chỉ secondaryinternal M28PDF19ref14; không gọi publisher-final directly verified.
- [x] Không suy issue thiếu củaM13/M26/M34; không bịa DOI choJCGM.
- [x] 6refs tương ứng6identities;5DOIs duy nhất; không trùng canonical source.
- [x] First-use citation order[1]–[6] đúng;10body+2glossary=12occurrences, không đếm labels của bibliography.
- [x] Mọi citation prose/glossary córeference vàmọi reference được dùng.
- [x] N/A citations caption/phương trình/bảng khoa học vì không có dữ liệu nguồn tại các vị trí này.
- [x] Không còn Paper/Evidence/Bxx/P3/task tags trong Word; không dùng numbering củabaseline.
- [x] M28 chỉ provenance metadata, không thêm reference thừa trongWord.
- [x] Correction provenance chỉ ghi output mới; không sửa canonical metadata hoặc accepted numbering.

FINDINGS: 6refs/5DOI;12citations hợp lệ. Trường issue còn thiếu không bịa; M26pagination provenance thứ cấp nội bộ.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: M26volume/pages secondaryinternal; một sốissue NOT_VERIFIED/omitted; không mở rộng corpus Internet.

## GATE 7 — VIETNAMESE THESIS WRITING AND WORD QA

STATUS: PASS_WITH_DOCUMENTED_LIMITATIONS

METHOD: python-docx/lxml/ZIP/relationship assertions; LO headless task-local profile;ROOTview_image4trang cuối, không chỉXML.

EVIDENCE: SOURCE_TRACEABILITY CSV, Word anchors, các phụ lục source/QA/render và ExecutionReport của chính task.

COUNT: 12 hạng mục checklist; số lượng thực tế trong ExecutionReport.

CHECKLIST:

- [x] ROOT đọc lại toàn bộ14đoạn,10termrows và6refs; văn xuôi cơ khí tiếng Việt, có lập luận.
- [x] Không khẩu hiệu/quảng bá/claim mới tuyệt đối hoặc workflow trongWord.
- [x] A4,lề3/2/2.5/2.5cm,TNR12body/headingbold12,line1.15;glossary10pt.
- [x] Sửa font fallback do theme chỉ ở candidate; PDF cuối tất cả textspans TimesNewRoman.
- [x] Native glossary1table11rows; headerrepeat,11cantSplit,captionkeepWithNext;không tràn lề.
- [x] CSV=Word cảidentity,definition/context vàsource;57anchors đúng hash cuối.
- [x] ZIP CRC và16XML/rels parse hợp lệ; không externalrelationship/header/footer/editorial metadata trongbody.
- [x] OMML0/hình0 phù hợp nhu cầu;N/A kiểm công thức hiển thị.
- [x] LibreOffice24.2.7.2 riêng task/profile; render chínhDOCX607071…ca45 vàxem cả4trang cuối.
- [x] Không trang trắng/cắt chữ/mấtκ,⁻¹,²/tràn bảng/captionrời; mỗi reference giữ liền entry.
- [x] Không tuyên bố MicrosoftWord validation; MSWord NOT_VERIFIED.
- [x] QA cùng phiên làSELF_REVIEW, không independent acceptance.

FINDINGS: 4trang cuối đã xem; TimesNewRoman fonts thực tế, bảng nối trang cóheader. LOvisualPASS; MSWord chưa kiểm.

SEVERITY: Không còn P1/P2. Các giới hạn kiểm chứng/nguồn được ghi riêng; không gọi hạn chế khoa học là lỗi.

UNRESOLVED: MICROSOFT_WORD_VALIDATION NOT_VERIFIED; independent acceptance chưa thực hiện.

## Mapping ba bullet — dữ liệu kiểm tra

```json
[
  {
    "outline_bullet": "B01",
    "exact_original": "Bench A phải xác định pressure-only response, repeatability, pressure-transfer proxy và các metric M–κ.",
    "word_location": "P02–P06; P10; glossary rows1–6",
    "mechanical_question": "Áp suất gần mẫu → đáp ứng uốn trong miền xác định? Lặp lại và proxy có nghĩa gì?",
    "required_evidence": "Lịch sử áp suất, trạng thái vật liệu, tải/biên, M–κ và độ không đảm bảo; đại lượng đo/suy rõ.",
    "support_role": "M13, M31, M26 comparator; M38 methodology; yêu cầu PDF/WEP.",
    "observable_or_inference": "Áp suất nguồn/gần mẫu; lực/chuyển vị/độ cong nếu được phê duyệt; proxy không là local traction.",
    "dependency": "Hình học/giao diện/nhiệt-pha-lịch sử tải/mô hình đo chờ khóa.",
    "conclusion_scope": "Baseline có điều kiện, không nhận dạng duy nhất tiếp xúc hay loại trừ chuyển pha."
  },
  {
    "outline_bullet": "B02",
    "exact_original": "Bench B phải xác định response của SMA–piston độc lập và so sánh với Bench A ở cùng áp suất gần mẫu.",
    "word_location": "P07–P10; glossary rows7–8",
    "mechanical_question": "Nguồn hoạt động thế nào và hai hệ có tương thích ở cùng áp suất gần mẫu không?",
    "required_evidence": "Đặc trưng riêng nguồn trước; sau đó dữ liệu so sánh dưới điều kiện tương ứng; không phải thiết bị đã vận hành.",
    "support_role": "M34 comparator SMA→pressure; M16 comparator calibration/control; PDF/WEP yêu cầu.",
    "observable_or_inference": "Lực–hành trình–nhiệt–áp suất–thời gian cần cân nhắc; không phải danh sách kênh đo bắt buộc.",
    "dependency": "Tách tĩnh/lịch sử p(t), nhiệt mẫu/nguồn, biên, compliance/rò nếu đáng kể.",
    "conclusion_scope": "Không từ một chỉ số áp suất suy tương đương; không gán cơ chế mới cho residual."
  },
  {
    "outline_bullet": "B03",
    "exact_original": "Chỉ chuyển sang phần tích hợp khi geometry, interface, sensor placement, uncertainty và stop criteria đã được khóa.",
    "word_location": "P11–P14; glossary rows9–10",
    "mechanical_question": "Khi nào sẵn sàng thực hiện, so sánh, và đủ bằng chứng kết luận?",
    "required_evidence": "Phê duyệt hình học/giao diện/vị trí-vai trò đo/mô hình bất định/tiêu chí dừng trước tích hợp nghiên cứu.",
    "support_role": "PDF/WEP/P3 project requirement; M38 hỗ trợ mô hình đo, không chuẩn chấp nhận MP1.",
    "observable_or_inference": "Hồ sơ lựa chọn/mô hình phép đo/tiêu chí và dữ liệu đủ tương ứng; chưa đặt ngưỡng.",
    "dependency": "Cả năm nhóm quyết định mở; đủ vận hành không tự đủ so sánh/kết luận.",
    "conclusion_scope": "Cho phép kết quả chưa đủ dữ liệu; không zero-effect hay novelty proof."
  }
]
```

## Phán định ROOT và lịch sử xử lý findings

Hai P2 từ phản biện thuật ngữ đã được sửa trực tiếp trong bản hiện tại và kiểm lại. Không R2/R3. Hai minor về nghĩa độ cứng uốn và suy luận giao diện đã xử lý; font fallback được sửa ở candidate trước render cuối. Không sửa baseline.

### Hồ sơ draft_critical_qa.json (nội dung lưu bền, tệp tạm sẽ dọn)

```json
{
  "status": "PASS_WITH_OPTIONAL_MINOR_CLARIFICATIONS",
  "review_type": "SELF_REVIEW: same task source worker scientific countercheck, not independent external validation",
  "scope": "All14 paragraphs,47 units and10 terminology entries in current §2.6.4 draft; no edits to draft/finals.",
  "input_provenance": [
    {
      "path": "/tmp/mp1-264-hlbiqcs2/draft.json",
      "sha256": "33f1eaa09a1997af5efd5e628ab48e8d5293ff59435e51fae9a071a0ae82707f"
    },
    {
      "path": "/tmp/mp1-264-hlbiqcs2/source_B.json",
      "sha256": "43dd5dcde1ffaaf7d593a5848a66f8e524eb7c0fa4aa9e1e929a7327d9fa07ce"
    }
  ],
  "P1_findings": [],
  "P2_findings": [],
  "minor_findings": [
    {
      "severity": "MINOR",
      "unit": "P14-U01",
      "issue": "giao diện chi phối may sound chosen by approval, although dominant interface is a mechanical inference needing evidence.",
      "exact_original": "hình học và giao diện chi phối",
      "exact_replacement": "hình học và các giao diện cần xét",
      "required": false
    },
    {
      "severity": "MINOR",
      "unit": "P06-U03",
      "issue": "The intended conservative attribution limit is valid, but literal wording may disallow bounded model-based inference when direct slip observations are absent.",
      "exact_original": "nếu chưa có quan sát trượt tại giao diện, kết luận cần dừng ở đáp ứng toàn hệ thực sự được đo.",
      "exact_replacement": "nếu chưa có quan sát trượt tại giao diện, kết luận trực tiếp cần giới hạn ở đáp ứng toàn hệ được đo, còn suy luận về trượt phải nêu rõ mô hình và giới hạn.",
      "required": false
    },
    {
      "severity": "MINOR_TRACEABILITY",
      "unit": "P10-U01",
      "issue": "M16-E05 is the dedicated parameter identification record; adding it would tighten calibration claim trace.",
      "exact_original": "M16-E02;M16-E04;M16-E06",
      "exact_replacement": "M16-E02;M16-E04;M16-E05;M16-E06",
      "required": false
    }
  ],
  "unit_reviews": [
    {
      "unit": "P01-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Conditional transition, no achieved result.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P01-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Bench A baseline then source characterization and comparison order preserved; chapter wording is proposal.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P01-U03",
      "category": "INFERENCE",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct no mechanism/novelty proof from organizing benches.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P02-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Conditional target question; domain not declared already selected.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P02-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Pressure-only explicitly excludes source role rather than all material/contact effects.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P02-U03",
      "category": "SOURCE_GROUNDED_CLAIM",
      "eids": [
        "M13-E01",
        "M13-E04"
      ],
      "status": "PASS",
      "assessment": "M13 bounded three-point bending nylon-chain prior art; no TiNi proof.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P02-U04",
      "category": "INFERENCE",
      "eids": [
        "M13-E04",
        "M13-E06"
      ],
      "status": "PASS",
      "assessment": "Correct transfer boundary; not global absence.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P03-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct pressure-source/near-specimen/local traction distinction.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P03-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Proxy needs location/calibration/model and boundary; no new pressure law.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P03-U03",
      "category": "SOURCE_GROUNDED_CLAIM",
      "eids": [
        "M31-E06",
        "M31-E07"
      ],
      "status": "PASS",
      "assessment": "M31 actual separate friction test acknowledged; no fabricated gap.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P03-U04",
      "category": "INFERENCE",
      "eids": [
        "M31-E03",
        "M31-E06"
      ],
      "status": "PASS",
      "assessment": "Correct friction force does not alone separate coefficient and normal load; interface specificity retained.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P04-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "M units N·m and curvature m^-1 correct; target proposed.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P04-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct force-deflection to M–κ is inferred using geometry/load model, not direct equivalence.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P04-U03",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "K N/m or N/mm, B/EI N·m², E Pa correct; EI conditional on beam representation.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P04-U04",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct branch/state-dependent stiffness; no implicit constant EI.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P05-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Repeatability domain conditional and unapproved.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P05-U02",
      "category": "SOURCE_GROUNDED_CLAIM",
      "eids": [
        "M26-E01",
        "M26-E04",
        "M26-E07"
      ],
      "status": "PASS",
      "assessment": "M26 E04 supports strain/thermal channels; E07 cycle response; near-isothermal tensile cable scope accurate.",
      "source_B_evidence_links": [
        {
          "eid": "M26-E01",
          "path": "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "line": 20
        },
        {
          "eid": "M26-E04",
          "path": "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "line": 23
        },
        {
          "eid": "M26-E07",
          "path": "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "line": 26
        }
      ]
    },
    {
      "unit": "P05-U03",
      "category": "INFERENCE",
      "eids": [
        "M38-E01"
      ],
      "status": "PASS",
      "assessment": "GUM definition is explicitly editorial synthesis using direct supplementary locator; no new invented canonical EID.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P05-U04",
      "category": "AUTHOR_PROPOSAL",
      "eids": [
        "M26-E07",
        "M38-E01"
      ],
      "status": "PASS",
      "assessment": "Correct repeatability versus between-specimen consistency and history drift; no repetition number set.",
      "source_B_evidence_links": [
        {
          "eid": "M26-E07",
          "path": "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "line": 26
        }
      ]
    },
    {
      "unit": "P06-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Information requirements are proposal, not an existing dataset.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P06-U02",
      "category": "SOURCE_GROUNDED_CLAIM",
      "eids": [
        "M38-E02",
        "M38-E03"
      ],
      "status": "PASS",
      "assessment": "GUM methodological support distinct from MP1 results.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P06-U03",
      "category": "AUTHOR_PROPOSAL",
      "eids": [
        "M38-E02",
        "M38-E03"
      ],
      "status": "PASS_WITH_OPTIONAL_CLARITY",
      "assessment": "Conservative attribution bound valid; optional wording could preserve explicitly labelled model-based interface inferences rather than forbid all inference when direct slip absent.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P06-U04",
      "category": "INFERENCE",
      "eids": [
        "M26-E04",
        "M26-E07",
        "M31-E03"
      ],
      "status": "PASS",
      "assessment": "Correct global-loop non-unique attribution; no numerical loss partition claimed.",
      "source_B_evidence_links": [
        {
          "eid": "M26-E04",
          "path": "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "line": 23
        },
        {
          "eid": "M26-E07",
          "path": "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "line": 26
        }
      ]
    },
    {
      "unit": "P07-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Bench B source-first level clearly separated from bending comparison.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P07-U02",
      "category": "SOURCE_GROUNDED_CLAIM",
      "eids": [
        "M34-E02",
        "M34-E07",
        "M34-E08",
        "M34-E09"
      ],
      "status": "PASS",
      "assessment": "M34 E02/E07/E08/E09 supports coil/enclosure force–displacement, static head and time experiments; no static-only misrepresentation.",
      "source_B_evidence_links": [
        {
          "eid": "M34-E02",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 25
        },
        {
          "eid": "M34-E07",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 30
        },
        {
          "eid": "M34-E08",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 31
        },
        {
          "eid": "M34-E09",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 32
        }
      ]
    },
    {
      "unit": "P07-U03",
      "category": "INFERENCE",
      "eids": [
        "M34-E02",
        "M34-E09"
      ],
      "status": "PASS",
      "assessment": "Correct source-pressure prior art and non-transfer to piston/MP1 traction.",
      "source_B_evidence_links": [
        {
          "eid": "M34-E02",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 25
        },
        {
          "eid": "M34-E09",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 32
        }
      ]
    },
    {
      "unit": "P08-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [
        "M34-E07",
        "M34-E08",
        "M34-E09"
      ],
      "status": "PASS",
      "assessment": "Candidate source quantities only; no target device specs or frozen measurement set.",
      "source_B_evidence_links": [
        {
          "eid": "M34-E07",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 30
        },
        {
          "eid": "M34-E08",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 31
        },
        {
          "eid": "M34-E09",
          "path": "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "line": 32
        }
      ]
    },
    {
      "unit": "P08-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Leakage/volume/compliance are conditional confounds, not claimed measured source findings.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P08-U03",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct actuator spring temperature and target bundle phase are distinct.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P08-U04",
      "category": "PENDING_HUMAN_DECISION",
      "eids": [],
      "status": "PASS",
      "assessment": "Explicitly not approved channels/operating envelope/final piston.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P09-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Second-level matched near-specimen comparison follows source characterization and retains material/thermal/history conditions.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P09-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct static pressure equality does not ensure equal time history or local contact state.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P09-U03",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct attribution limits; no residual automatically becomes source-induced mechanics novelty.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P10-U01",
      "category": "SOURCE_GROUNDED_CLAIM",
      "eids": [
        "M16-E02",
        "M16-E04",
        "M16-E06"
      ],
      "status": "PASS",
      "assessment": "M16 pressure identification plus later control experiments accurately separated; calibration trace could add E05 to original EID set.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P10-U02",
      "category": "INFERENCE",
      "eids": [
        "M16-E04",
        "M16-E06"
      ],
      "status": "PASS",
      "assessment": "Does not erase controller validation; source fit not independent MP1 prediction.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P10-U03",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Locked parameters/reserved tests and predeclared metrics are requirements, not numerical protocol freeze.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P10-U04",
      "category": "INFERENCE",
      "eids": [],
      "status": "PASS",
      "assessment": "H0b live preserved; one failed implementation does not reject entire conventional class or establish H1.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P11-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Readiness/comparability/inference levels are author-defined logical distinctions.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P11-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct operability does not establish comparison or discriminating evidence.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P12-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Conditional approvals before integration, no claim achieved.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P12-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [
        "M38-E02",
        "M38-E03"
      ],
      "status": "PASS",
      "assessment": "GUM-inspired proposed model inputs/covariance; measured/inferred distinction.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P12-U03",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Explicit future research integration, not completed bench or document merge.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P13-U01",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Proposed safety/validity/interpretation stop types; no numerical thresholds or automated exclusions.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P13-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Correct inconclusive is neither zero effect nor new effect; handling requires approval.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P13-U03",
      "category": "PENDING_HUMAN_DECISION",
      "eids": [],
      "status": "PASS",
      "assessment": "Explicit absence of final numerical criteria.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P14-U01",
      "category": "PENDING_HUMAN_DECISION",
      "eids": [],
      "status": "PASS_WITH_OPTIONAL_CLARITY",
      "assessment": "Pending five groups retained. Optional replace giao diện chi phối with các giao diện cần xét, since dominance is empirical rather than human-approved design choice.",
      "source_B_evidence_links": []
    },
    {
      "unit": "P14-U02",
      "category": "AUTHOR_PROPOSAL",
      "eids": [],
      "status": "PASS",
      "assessment": "Concluding conditional transition; no Chapter3/4 content drafted.",
      "source_B_evidence_links": []
    }
  ],
  "terminology_review": [
    {
      "term": "Pressure-only baseline",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Pressure-transfer proxy",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Moment–curvature relation",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Flexural rigidity",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Repeatability",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Measurement uncertainty",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Matched-pressure comparison",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Independent predictive validation",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Readiness condition",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    },
    {
      "term": "Stop criterion",
      "status": "PASS",
      "assessment": "Definition/domain and units consistent; author convention or GUM-derived synthesis clearly labelled; not an MP1 result or approved device/protocol."
    }
  ],
  "scientific_checks": {
    "source_claim_vs_proposal": "PASS: source findings remain bounded to M13/M31/M26/M34/M16 systems, other content is proposed requirements or explicit inference.",
    "prior_art": "PASS: pressure response, separate friction measurements, SMA pressure and source time behavior acknowledged.",
    "source_first_then_comparison": "PASS: P07–P09 clearly distinguish source characterization from matched near-specimen comparison.",
    "local_traction": "PASS: pressure/proxy/traction distinct; pressure equality not equal contact state.",
    "material_state": "PASS: M26 tensile near-isothermal history evidence used as methodological precedent, not MP1 bending validation.",
    "calibration_validation": "PASS: source characterization independence is not predictive validation; source fit/control evidence and MP1 reserved-path prediction remain distinct.",
    "units": "PASS: moment N·m, curvature m^-1, K N/m or N/mm, B/EI N·m², E Pa.",
    "H0b_H1": "PASS: conventional transformation/contact/friction live competitor, no new-law requirement from architecture or single-model residual.",
    "null_inconclusive": "PASS: inadequate resolution/observations not zero effect or novel mechanism.",
    "protocol_boundary": "PASS: no equipment selections, numerical thresholds, repetitions, final sampling plan, completed bench, or Chapter3/4 draft.",
    "approval": "PASS: human scientific/design approvals remain pending; author proposals do not report decisions achieved."
  },
  "verification_limits": [
    "This review checks scientific content and source_B evidence against previously reopened canonical PDFs, not Word rendering or final traceability CSV completeness.",
    "M13/M31/M38 claims checked for consistency with known directly verified source boundaries; dedicated source_A/root own exhaustive current locator QA.",
    "No new papers, web queries or MP1 data.",
    "No files written except requested draft_critical_qa.json."
  ]
}
```

### Hồ sơ terminology_boundary_qa.json (nội dung lưu bền, tệp tạm sẽ dọn)

```json
{
  "task": "§2.6.4 terminology and P3-boundary review",
  "review_authority": "SELF_REVIEW",
  "same_session": true,
  "independent_acceptance": "NOT_PERFORMED",
  "status": "P2_FIXES_REQUIRED; ROOT_FINAL_JUDGMENT",
  "inputs": {
    "draft": "/tmp/mp1-264-hlbiqcs2/draft.json",
    "draft_sha256": "33f1eaa09a1997af5efd5e628ab48e8d5293ff59435e51fae9a071a0ae82707f",
    "internal_transition": "/tmp/mp1-264-hlbiqcs2/internal_transition.json",
    "baselines": [
      {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv",
        "sha256": "bf047860d2689dd7a492fa20688ae74647e55a839673f84b503495a9b8551c8a",
        "term_count": 14
      },
      {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv",
        "sha256": "c36f8421433b82a1ce60985e57e609c0bf7728dfd884a42cf1412f2533869237",
        "term_count": 11
      },
      {
        "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
        "sha256": "3fd5f1ca6e4a0e14048c8bd1fb97a1d8c68b7fc6888e5a6685aad9763932aa13",
        "term_count": 9
      }
    ]
  },
  "counts": {
    "paragraphs_reviewed": 14,
    "terms_reviewed": 10,
    "P1": 0,
    "P2": 2,
    "minor": 1
  },
  "findings": [
    {
      "severity": "P2",
      "location": "P14 unit1",
      "category": "PENDING_DECISION_VERSUS_EMPIRICAL_ATTRIBUTION",
      "current": "Năm nhóm lựa chọn vẫn cần người nghiên cứu phê duyệt: hình học và giao diện chi phối; biểu diễn tải pháp tuyến hữu hiệu; miền nhiệt độ, pha, tốc độ và lịch sử tải TiNi; đại lượng độ cứng chính cùng độ không đảm bảo; và phạm vi kiểm chứng SMA–piston.",
      "issue": "Giao diện chi phối is a mechanism finding to identify or bound, not the geometry/interface-topology choice for a human to approve. The same sentence can retain the exact remaining choices more clearly, including proxy feasibility and Bench B core/support scope.",
      "suggested_replacement": "Năm nhóm lựa chọn vẫn cần người nghiên cứu phê duyệt: hình học, các giao diện tiếp xúc và đường truyền phản lực; khả năng đo hoặc dùng đại lượng đại diện cho tải pháp tuyến, hoặc thu hẹp phạm vi kết luận; miền nhiệt độ, pha, tốc độ và lịch sử tải TiNi; đại lượng độ cứng chính cùng tiêu chí xét độ không đảm bảo; và vai trò chính hay hỗ trợ của kiểm chứng SMA–piston trong luận văn.",
      "basis": [
        {
          "path": "/home/khanh/projects/mechanical-research-agents/data/MP1_WRITING_EVIDENCE_FINAL/08_UNRESOLVED_AND_HUMAN_DECISIONS.md",
          "heading": "Five pending human decisions"
        },
        {
          "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_GAP_MATRIX.csv",
          "keys": [
            "G02",
            "G09"
          ],
          "meaning": "Topology is prerequisite; dominance is a conditional identification question."
        }
      ]
    },
    {
      "severity": "P2",
      "location": "P10 unit3 and term Independent predictive validation",
      "category": "RESERVED_DATA_INDEPENDENCE",
      "issue": "Current wording protects the parameter values but not choosing or adjusting model form using reserved data. Holding parameters fixed alone is insufficient for the claimed independence, and it is narrower than the untouched-data/locked-model requirement and predecessor definition.",
      "current_body": "Đối với luận văn, cần khai báo dữ liệu hiệu chuẩn, giữ cố định tham số trước khi dùng dữ liệu dành riêng để kiểm chứng và xác định trước đại lượng đánh giá cùng cách xét độ không đảm bảo; cách chia dữ liệu cụ thể vẫn cần được phê duyệt.",
      "suggested_body_replacement": "Đối với luận văn, cần khai báo dữ liệu hiệu chuẩn, giữ cố định mô hình cùng các tham số trước khi dùng dữ liệu dành riêng để kiểm chứng và xác định trước đại lượng đánh giá cùng cách xét độ không đảm bảo; dữ liệu dành riêng không được dùng để lựa chọn hay điều chỉnh mô hình đang được kiểm tra, còn cách chia dữ liệu cụ thể vẫn cần được phê duyệt.",
      "current_term_definition": "Đánh giá dự đoán với tham số đã giữ cố định trên dữ liệu dành riêng, không dùng chính dữ liệu đó để hiệu chuẩn.",
      "suggested_term_definition": "Đánh giá dự đoán trên dữ liệu không dùng để lựa chọn hay điều chỉnh mô hình hoặc ước lượng các tham số đang được kiểm tra.",
      "basis": [
        {
          "path": "/home/khanh/projects/mp1-writing-evidence-r1/outputs/literature/MP1_READING_PACK/03_PHASE_3/P3_RESEARCH_QUESTIONS.md",
          "heading": "RQ1",
          "line": 18,
          "anchor": "lock parameters and numerical settings; evaluate independent pressure–curvature paths or specimens with untouched data"
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
          "term": "Independent predictive validation",
          "anchor": "dữ liệu hoặc điều kiện không dùng để ước lượng hay điều chỉnh tham số đang được kiểm tra"
        }
      ]
    },
    {
      "severity": "minor",
      "location": "term Flexural rigidity / definition",
      "category": "DEFINITION_COMPLETENESS",
      "current": "Đại lượng B có đơn vị N·m²; ký hiệu EI chỉ dùng khi mô hình dầm tương ứng cho phép. Khác mô đun E (Pa) và độ dốc lực–chuyển vị K (N/m hoặc N/mm).",
      "issue": "The definition distinguishes units but omits the mechanical meaning of B already present in all three predecessor glossaries.",
      "suggested_replacement": "Đại lượng B đặc trưng sức kháng uốn cấp tiết diện, có đơn vị N·m²; ký hiệu EI chỉ dùng khi mô hình dầm tương ứng cho phép. Khác mô đun E (Pa) và độ dốc lực–chuyển vị K (N/m hoặc N/mm).",
      "basis": [
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv",
          "term": "Flexural rigidity, B or EI"
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
          "term": "Flexural rigidity, elastic modulus and force–deflection stiffness"
        }
      ]
    }
  ],
  "paragraph_checks": [
    {
      "paragraph": "P01",
      "status": "PASS",
      "reason": "Conditional research handoff and prior-art boundary; no novelty claimed."
    },
    {
      "paragraph": "P02",
      "status": "PASS",
      "reason": "External-pressure baseline excludes source actuation role, not TiNi/contact/boundary physics."
    },
    {
      "paragraph": "P03",
      "status": "PASS",
      "reason": "Source/specimen pressure and local normal loading remain distinct; proxy not treated as field."
    },
    {
      "paragraph": "P04",
      "status": "PASS",
      "reason": "M–κ, K, B/EI and E are separated with correct units and branch/load qualifications."
    },
    {
      "paragraph": "P05",
      "status": "PASS",
      "reason": "Repeatability and inter-specimen generalization distinguished; source fact verification remains source-worker scope."
    },
    {
      "paragraph": "P06",
      "status": "PASS",
      "reason": "Direct/proxy/derived quantities and global-loop attribution limits preserved."
    },
    {
      "paragraph": "P07",
      "status": "PASS",
      "reason": "Separate source characterization precedes comparison; prior art not turned into MP1 validation."
    },
    {
      "paragraph": "P08",
      "status": "PASS",
      "reason": "Source/bundle thermal states separated; no sensor/geometry/operating range chosen."
    },
    {
      "paragraph": "P09",
      "status": "PASS",
      "reason": "Near-specimen pressure plus history/material/boundary comparability required; no asserted equivalence."
    },
    {
      "paragraph": "P10",
      "status": "P2_FIX_REQUIRED",
      "reason": "H0b live-competitor boundary correct. Reserved-data independence needs model-selection protection."
    },
    {
      "paragraph": "P11",
      "status": "PASS",
      "reason": "Readiness, comparability and sufficient scientific evidence distinguished."
    },
    {
      "paragraph": "P12",
      "status": "PASS",
      "reason": "Geometry/interface/measurement/uncertainty/stop decisions prospective, not approved. Integration means research benches."
    },
    {
      "paragraph": "P13",
      "status": "PASS",
      "reason": "Four stop/withhold categories covered with no thresholds; unresolved effect not zero or new-mechanism proof."
    },
    {
      "paragraph": "P14",
      "status": "P2_FIX_REQUIRED",
      "reason": "Five groups present, but dominant interface must remain an empirical question rather than a design choice."
    }
  ],
  "terminology_checks": [
    {
      "term_number": 1,
      "english_term": "Pressure-only baseline",
      "vietnamese_term": "Đối chứng chỉ dùng nguồn áp suất ngoài",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 2,
      "english_term": "Pressure-transfer proxy",
      "vietnamese_term": "Đại lượng đại diện cho truyền áp",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 3,
      "english_term": "Moment–curvature relation",
      "vietnamese_term": "Quan hệ mô men–độ cong",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 4,
      "english_term": "Flexural rigidity",
      "vietnamese_term": "Độ cứng uốn",
      "status": "MINOR_DEFINITION_ADDITION",
      "baseline_matches": [
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv",
          "english_term": "Flexural rigidity, B or EI",
          "vietnamese_term": "Độ cứng uốn, B hoặc EI",
          "mechanical_definition": "Đại lượng chống uốn cấp tiết diện trong mô hình dầm; có đơn vị N·m². EI là dạng của dầm đàn hồi đồng nhất, B có thể là đại lượng tương đương."
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv",
          "english_term": "Flexural rigidity and structural stiffness",
          "vietnamese_term": "Độ cứng uốn và độ cứng kết cấu",
          "mechanical_definition": "Độ cứng uốn B hoặc EI là đại lượng chống uốn cấp tiết diện, có đơn vị N·m²; K đặc trưng quan hệ lực–chuyển vị theo độ dốc hoặc tỷ số lực trên chuyển vị tùy quy ước nguồn, có đơn vị N/m hoặc N/mm."
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
          "english_term": "Flexural rigidity, elastic modulus and force–deflection stiffness",
          "vietnamese_term": "Độ cứng uốn, mô đun đàn hồi và độ cứng lực–độ võng",
          "mechanical_definition": "Độ cứng uốn B hoặc EI mô tả sức kháng uốn cấp tiết diện; E là mô đun vật liệu; K mô tả độ dốc hoặc tỷ số lực–độ võng theo quy ước đã chọn."
        }
      ],
      "new_editorial_term": false,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 5,
      "english_term": "Repeatability",
      "vietnamese_term": "Độ lặp lại",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Editorial source-grounded definition; verify precise source fragments in source traceability. This review does not re-audit GUM PDF."
    },
    {
      "term_number": 6,
      "english_term": "Measurement uncertainty",
      "vietnamese_term": "Độ không đảm bảo đo",
      "status": "PASS",
      "baseline_matches": [
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_1/MP1_CH2_2_6_1_TERMINOLOGY.csv",
          "english_term": "Measurement uncertainty",
          "vietnamese_term": "Độ không đảm bảo đo",
          "mechanical_definition": "Tham số đặc trưng độ phân tán của các giá trị có thể quy cho đại lượng cần đo, được đánh giá trên cơ sở thông tin sử dụng."
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv",
          "english_term": "Measurement uncertainty",
          "vietnamese_term": "Độ không đảm bảo đo",
          "mechanical_definition": "Tham số đặc trưng độ phân tán của các giá trị có thể quy cho đại lượng cần đo, được đánh giá trên cơ sở thông tin sử dụng."
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
          "english_term": "Measurement uncertainty",
          "vietnamese_term": "Độ không đảm bảo đo",
          "mechanical_definition": "Tham số gắn với kết quả đo, đặc trưng độ phân tán của các giá trị có thể quy một cách hợp lý cho đại lượng cần đo."
        }
      ],
      "new_editorial_term": false,
      "attribution_boundary": "Editorial source-grounded definition; verify precise source fragments in source traceability. This review does not re-audit GUM PDF."
    },
    {
      "term_number": 7,
      "english_term": "Matched-pressure comparison",
      "vietnamese_term": "So sánh ở cùng áp suất gần mẫu",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 8,
      "english_term": "Independent predictive validation",
      "vietnamese_term": "Kiểm chứng dự đoán độc lập",
      "status": "P2_FIX_REQUIRED",
      "baseline_matches": [
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_2/MP1_CH2_2_6_2_TERMINOLOGY.csv",
          "english_term": "Independent predictive validation",
          "vietnamese_term": "Kiểm chứng dự đoán độc lập",
          "mechanical_definition": "Đánh giá dự đoán bằng dữ liệu hoặc điều kiện không dùng để ước lượng hay điều chỉnh tham số đang được kiểm tra."
        },
        {
          "path": "/home/khanh/projects/mechanical-research-agents/outputs/thesis_drafts/chapter_2/section_2_6_3/MP1_CH2_2_6_3_TERMINOLOGY.csv",
          "english_term": "Independent predictive validation",
          "vietnamese_term": "Kiểm chứng dự đoán độc lập",
          "mechanical_definition": "Đánh giá dự đoán bằng dữ liệu hoặc điều kiện không dùng để ước lượng hay điều chỉnh tham số đang được kiểm tra."
        }
      ],
      "new_editorial_term": false,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 9,
      "english_term": "Readiness condition",
      "vietnamese_term": "Điều kiện sẵn sàng",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    },
    {
      "term_number": 10,
      "english_term": "Stop criterion",
      "vietnamese_term": "Tiêu chí dừng",
      "status": "PASS",
      "baseline_matches": [],
      "new_editorial_term": true,
      "attribution_boundary": "Source-free author proposal, not journal terminology verification."
    }
  ],
  "bullet_coverage": {
    "B01": {
      "status": "PASS",
      "paragraphs": [
        "P02",
        "P03",
        "P04",
        "P05",
        "P06",
        "P10"
      ],
      "content": [
        "external-pressure response",
        "repeatability/state/history",
        "pressure-transfer proxy and normal-traction boundary",
        "M–κ and derived-metric definition"
      ]
    },
    "B02": {
      "status": "PASS",
      "paragraphs": [
        "P07",
        "P08",
        "P09",
        "P10"
      ],
      "content": [
        "separate source characterization",
        "matched near-specimen pressure",
        "thermal/loading/history and source compliance alternatives",
        "no asserted equivalence"
      ]
    },
    "B03": {
      "status": "PASS_WITH_P14_FIX",
      "paragraphs": [
        "P11",
        "P12",
        "P13",
        "P14"
      ],
      "content": [
        "geometry/interface/measurement placement/uncertainty/stop decisions pending",
        "readiness vs comparability vs claims distinct",
        "safety physical stop vs interpretation restrictions",
        "no numerical protocol"
      ]
    }
  },
  "canonical_boundaries": {
    "H0b": "PASS: kept conventional transformation-aware TiNi/contact/friction explanation live; not refuted.",
    "H1": "PASS: no coupling-law proof or required thesis outcome.",
    "G00": "PASS: established mechanisms/prior art acknowledged; no reopening.",
    "G01_G08": "PASS: conditional observations/interpretations, no global gap claim.",
    "G09": "P14 correction needed to preserve topology prerequisite versus dominant-interface finding.",
    "no_protocol": "PASS: no actual geometry, sensor, range, stop threshold or data split selected.",
    "five_pending_choices": "P14 correction proposed; no actual approval claimed.",
    "rq_mapping": "No renumbering or replacement occurs in prose. Preserve existing 4-P3-group/5-PDF-question mapping and HUMAN_DECISION_PENDING in final report/sidecar; no need to insert all RQs into body.",
    "stop_categories": "PASS: P13 covers operational safety, specimen/measurement validity, comparability and model discrimination. Distinguishes stopping operation from withholding or limiting interpretation.",
    "scope": "PASS: research Bench A/B integration, not Word-file merge; no Chapter 3/4 protocol drafted."
  },
  "nonfindings": [
    "No needless stylistic rewrite requested.",
    "Term labels Measurement uncertainty and Independent predictive validation retain predecessor Vietnamese labels.",
    "Flexural rigidity wording is a compact version of predecessor concept, not a new physical definition.",
    "Source-free terms are appropriately author proposals; do not turn their source cells into published-paper authority."
  ],
  "limits": [
    "No journal PDF/source truth re-audit or bibliographic/citation-number audit.",
    "No rendered Word/layout check; draft JSON only.",
    "This review is same-session SELF_REVIEW and does not approve pending scientific choices."
  ],
  "writes": {
    "only_output": "/tmp/mp1-264-hlbiqcs2/terminology_boundary_qa.json",
    "inputs_or_finals_modified": false
  },
  "resolution_history": [
    {
      "review_authority": "SELF_REVIEW",
      "scope": "Targeted re-read only: P06 unit3, P10 unit3, P14 unit1, Independent predictive validation and Flexural rigidity definitions. Original findings and review preserved above.",
      "draft_sha256": "e710805d844f49c421df76741f049d5448b7455f77c19745fb23d6d95397427a",
      "effective_status": "PASS_TARGETED_BOUNDARY_AND_TERMINOLOGY_RECHECK; ROOT_FINAL_JUDGMENT",
      "remaining_findings": {
        "P1": 0,
        "P2": 0,
        "minor": 0
      },
      "resolutions": [
        {
          "original_location": "P14 unit1",
          "original_severity": "P2",
          "status": "CLOSED",
          "current_text": "Năm nhóm lựa chọn vẫn cần người nghiên cứu phê duyệt: hình học và các giao diện cần xét; biểu diễn hoặc quan sát tải pháp tuyến hữu hiệu; miền nhiệt độ, pha, tốc độ và lịch sử tải TiNi; đại lượng độ cứng chính cùng độ không đảm bảo; và phạm vi kiểm chứng SMA–piston.",
          "reason": "Actual interfaces to consider are pending, rather than approval of interface dominance. Five decision groups remain prospective; their full canonical meaning remains in internal_transition.json."
        },
        {
          "original_location": "P10 unit3 and term Independent predictive validation",
          "original_severity": "P2",
          "status": "CLOSED",
          "current_body": "Đối với luận văn, cần khai báo dữ liệu hiệu chuẩn, giữ cố định dạng mô hình và tham số trước khi dùng dữ liệu dành riêng để kiểm chứng và xác định trước đại lượng đánh giá cùng cách xét độ không đảm bảo; dữ liệu kiểm chứng không được dùng lại để lựa chọn hay điều chỉnh mô hình, còn cách chia dữ liệu cụ thể vẫn cần được phê duyệt.",
          "current_term_definition": "Đánh giá dự đoán với dạng mô hình và tham số đã giữ cố định trên dữ liệu dành riêng, không dùng dữ liệu đó để lựa chọn mô hình hoặc hiệu chuẩn.",
          "reason": "Model form and parameters are fixed before reserved-data use; the same data cannot guide model selection or adjustment."
        },
        {
          "original_location": "term Flexural rigidity / definition",
          "original_severity": "minor",
          "status": "CLOSED",
          "current_definition": "Đại lượng B mô tả sức kháng uốn cấp tiết diện, có đơn vị N·m²; ký hiệu EI chỉ dùng khi mô hình dầm tương ứng cho phép. Khác mô đun E (Pa) và độ dốc lực–chuyển vị K (N/m hoặc N/mm).",
          "reason": "Definition now states the mechanical meaning of B while retaining units and E/K distinctions."
        }
      ],
      "additional_change_checked": {
        "location": "P06 unit3",
        "status": "PASS",
        "current_text": "Do đó, đại lượng đo trực tiếp, đại lượng đại diện cho truyền áp và đại lượng suy từ mô hình phải được tách rõ cùng độ không đảm bảo thích hợp; nếu chưa có quan sát trượt tại giao diện, kết luận trực tiếp cần giới hạn ở đáp ứng toàn hệ thực sự được đo, còn suy luận về giao diện phải nêu rõ mô hình và giả thiết đi kèm.",
        "reason": "Direct claims remain limited to observed whole-system response while interface inferences are explicitly conditional on model and assumptions. This does not claim interface observability or uniqueness."
      },
      "limitations": "No source PDF, rendered Word, final-file or independent acceptance review in this targeted recheck."
    }
  ]
}
```

### Hồ sơ static_qa.json (nội dung lưu bền, tệp tạm sẽ dọn)

```json
{
  "status": "PASS",
  "scope": "Bounded static QA for §2.6.4 only, exact candidate and CSV hashes below. No rendering, visual review, new literature, or final/input modifications.",
  "artifact_hashes": {
    "candidate.docx": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
    "trace.csv": "636a5acb7514ccd8309a6e786280252847bdbd5c6674264069866a772429275b",
    "terms.csv": "346ffdf77c8e5b60680d7fb57ee9992765a7112de12673a4328ce3c8149a64f5",
    "draft.json": "20552c84c721f5211f73c0da0a662f27d4c6e30ba212b4578075a38a4909e723",
    "source_A.json": "48cc8bf836bc68867308f06c1e15538019810acdbcae008060cc7bc34f9598e5",
    "source_B.json": "43dd5dcde1ffaaf7d593a5848a66f8e524eb7c0fa4aa9e1e929a7327d9fa07ce",
    "references.json": "2113103f03d9628cf4a4e6a13a6866eff3f2a7e56549afd4bda1a43f93be61ae",
    "source_fragments.json": "163bc7922efcb5e73374a37602e3c9c7a67fbd9a2bb29cbf1b073c5a4ecbb158"
  },
  "recomputed": {
    "trace_rows": 57,
    "trace_columns": 63,
    "body_claims": 47,
    "glossary_claims": 10,
    "body_paragraphs": 14,
    "glossary_terms": 10,
    "used_evidence_ids": 19,
    "references": 6,
    "unique_DOIs": 5,
    "body_citation_occurrences": 10,
    "glossary_citation_occurrences": 2,
    "native_tables": 1,
    "OMML_equations": 0,
    "figures": 0,
    "body_whitespace_tokens": 1949,
    "body_outline_bullets": [
      "B01",
      "B02",
      "B03"
    ]
  },
  "checks": [
    {
      "check": "57 unique trace records and anchors",
      "pass": true,
      "detail": {
        "all": 57,
        "body": 47,
        "glossary": 10
      }
    },
    {
      "check": "all57 anchors resolve uniquely at exact Word location",
      "pass": true,
      "detail": {
        "resolved": 57,
        "glossary_identity_and_source_cells_checked": 10
      }
    },
    {
      "check": "approved draft prose and trace unit identity",
      "pass": true,
      "detail": {
        "paragraphs": 14,
        "units": 47,
        "normalization": "Editorial trailing whitespace removed; all visible approved prose and trace units identical."
      }
    },
    {
      "check": "10 glossary entries exact identity definition context and source",
      "pass": true,
      "detail": {
        "entries_checked": 10,
        "source_attributions": [
          "Quy ước của luận văn.",
          "Diễn giải yêu cầu chuyển tiếp của luận văn.",
          "Quy ước đại lượng cơ học của luận văn.",
          "Quy ước đại lượng cơ học của luận văn.",
          "GUM [4], Phụ lục B.2.15–B.2.16.",
          "GUM [4], mục 2.2.3, 4.1 và 5.2.",
          "Diễn giải yêu cầu chuyển tiếp của luận văn.",
          "Yêu cầu phương pháp của luận văn.",
          "Diễn giải yêu cầu chuyển tiếp của luận văn.",
          "Diễn giải yêu cầu chuyển tiếp của luận văn."
        ]
      }
    },
    {
      "check": "63 trace columns preserve inherited53 in order",
      "pass": true,
      "detail": {
        "total": 63,
        "inherited": 53,
        "added": [
          "bench_role",
          "transition_requirement",
          "measurement_or_inference_level",
          "scientific_dependency",
          "validation_role",
          "decision_status",
          "unresolved_human_decision",
          "author_inference_or_proposal",
          "scope_of_claim",
          "word_anchor_json"
        ]
      }
    },
    {
      "check": "exact raw canonical records provenance lookup and PDF identity",
      "pass": true,
      "detail": {
        "unique_EIDs": 19,
        "EIDs": [
          "M13-E01",
          "M13-E04",
          "M13-E06",
          "M16-E02",
          "M16-E04",
          "M16-E06",
          "M26-E01",
          "M26-E04",
          "M26-E07",
          "M31-E03",
          "M31-E06",
          "M31-E07",
          "M34-E02",
          "M34-E07",
          "M34-E08",
          "M34-E09",
          "M38-E01",
          "M38-E02",
          "M38-E03"
        ],
        "canonical_jsonl_files": [
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-B/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-D/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_PILOT/EVIDENCE_RECORDS.jsonl",
          "outputs/literature/MP1_READING_PACK/02_FULL/WP-A/EVIDENCE_RECORDS.jsonl"
        ],
        "PDFs_hashed": 6,
        "errors": []
      }
    },
    {
      "check": "M16E05 not silently introduced",
      "pass": true,
      "detail": {
        "M16_EIDs": [
          "M16-E02",
          "M16-E04",
          "M16-E06"
        ]
      }
    },
    {
      "check": "current physical printed source locators match worker packets",
      "pass": true,
      "detail": {
        "errors": [],
        "GUM_root_fragments": "M38 fragments separately ROOT checked; not represented as workerA/B verification. Additional canonical-record fragments disclosed in trace."
      }
    },
    {
      "check": "six reference identities ordered authors and metadata",
      "pass": true,
      "detail": {
        "errors": [],
        "ordered_papers": [
          "M13",
          "M31",
          "M26",
          "M38",
          "M34",
          "M16"
        ],
        "M38_metadata_scope": "Institutional author/title/JCGM100:2008 from root PDF check; no DOI invented."
      }
    },
    {
      "check": "citation first use local order and all references used",
      "pass": true,
      "detail": {
        "body_citations": 10,
        "glossary_citations": 2,
        "first_use_order": [
          1,
          2,
          3,
          4,
          5,
          6
        ]
      }
    },
    {
      "check": "source claims author proposals and inference roles distinct",
      "pass": true,
      "detail": {
        "errors": [],
        "claim_category_counts": {
          "AUTHOR_PROPOSAL": 38,
          "INFERENCE": 10,
          "SOURCE_GROUNDED_CLAIM": 6,
          "PENDING_HUMAN_DECISION": 3
        },
        "source_role_counts": {
          "CONTEXT_ONLY": 39,
          "DIRECT_SUPPORT": 5,
          "COMPARATOR": 7,
          "METHODOLOGY": 6
        },
        "bounded_reading": "Bench A/B organization and integration/readiness/stop choices are conditional author requirements. Cited papers support source findings and methods, not completed MP1 outcomes."
      }
    },
    {
      "check": "essential scientific distinctions explicit in Word",
      "pass": true,
      "detail": {
        "Fdelta_vs_Mkappa": true,
        "gauge_vs_local_contact": true,
        "pull_force_vs_normal_load": true,
        "fit_vs_independent_prediction": true,
        "proposed_gates_not_completed": true,
        "numerical_limits_not_frozen": true
      }
    },
    {
      "check": "ZIP CRC and all XML parse",
      "pass": true,
      "detail": {
        "CRC_bad_member": null,
        "XML_errors": []
      }
    },
    {
      "check": "native10term3column table repeat header nonsplitting rows",
      "pass": true,
      "detail": {
        "native_tables": 1,
        "rows_including_header": 11,
        "columns": 3,
        "repeat_headers": 1,
        "cantSplit_rows": 11
      }
    },
    {
      "check": "TimesNewRoman12prose10glossary",
      "pass": true,
      "detail": {
        "prose_and_references_pt": 12,
        "glossary_pt": 10
      }
    },
    {
      "check": "A4 and specified3left2right2.5topbottom margins",
      "pass": true,
      "detail": [
        {
          "width_cm": 21.001,
          "height_cm": 29.7,
          "left_cm": 3.0,
          "right_cm": 2.0,
          "top_cm": 2.499,
          "bottom_cm": 2.499
        }
      ]
    },
    {
      "check": "no internal markers in Word",
      "pass": true,
      "detail": {}
    },
    {
      "check": "no unsupported equations or embedded figures",
      "pass": true,
      "detail": {
        "OMML": 0,
        "drawings": 0,
        "note": "M–κ,EI and unit definitions are prose symbols, not copied mechanics equations."
      }
    },
    {
      "check": "active prose heading and caption font themes cannot override TNR",
      "pass": true,
      "detail": {
        "active_styles": [
          "Caption",
          "Heading2",
          "Normal"
        ],
        "theme_attributes": [],
        "scope": "Unused default Word styles do not affect active paragraphs."
      }
    },
    {
      "check": "final textual update recheck exact candidate",
      "pass": true,
      "detail": {
        "candidate_sha256": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
        "57_anchors_rechecked": true,
        "10_glossaries_rechecked": true,
        "raw_canonical_records_rechecked": true,
        "P06_explicit_2_3_citations": true,
        "model_structure_wording": true,
        "M16_evidence_class": "EXPERIMENTALLY_DEMONSTRATED;CALIBRATION_SUPPORTED",
        "errors": []
      }
    }
  ],
  "findings": [],
  "limitations": [
    "Source content was verified in source packets; this static pass confirms exact canonical record/hash/provenance consistency and claim/role boundaries, not a fresh independent all-PDF audit.",
    "Root handles rendered-page layout inspection and final scientific adjudication.",
    "No novelty, final protocol, numerical thresholds or human design approval certified."
  ],
  "checked_candidate_hash": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
  "final_resolution": "Relevant static checks rerun after final citation/terminology/calibration-label update. No scientific re-audit, source-worker rerun or rendering performed."
}
```

## Kiểm tra hiển thị cuối — ROOT trực tiếp

WORD_RENDER_VALIDATION: PASS_LIBREOFFICE_VISUAL

MICROSOFT_WORD_VALIDATION: NOT_VERIFIED

4/4 trang được xem qua ảnh render cuối; PDF không được coi là deliverable thứ sáu.

```json
{
  "docx_sha256": "607071daa1f173daa492b5b728a059b84759a0c0a6adc09bc6d49d8bec9bca45",
  "pdf_sha256": "f8bb8ca175e0dbd837c11a20b1b5a0c174143e82931d2578e722e0ce3ae6d15e",
  "page_checks": [
    {
      "page": 1,
      "finding": "Đọc heading/P01–P06 đầu; TNR12,κ vàđơn vị hiển thị đủ, đoạn nối trang hợp lý."
    },
    {
      "page": 2,
      "finding": "ĐọcP06tiếp–P10; citation[2],[3],sourceB vàcalibration/validation đầy đủ; không cắt chữ/tràn."
    },
    {
      "page": 3,
      "finding": "ĐọcP11–P14 vàglossaryrows1–5;captionđi cùngbảng; không splitrow hoặc trắng."
    },
    {
      "page": 4,
      "finding": "Headerglossarylặp;rows6–10 và6refs; entrieskhôngtáchvôlý, khôngtràn/mấtkýhiệu."
    }
  ],
  "page_geometry_fonts_hashes": [
    {
      "page": 1,
      "text_chars": 3576,
      "fonts": [
        "TimesNewRomanPS-BoldMT",
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 541.75,
      "min_y": 81.35877990722656,
      "max_y": 764.6427612304688,
      "top": "2.6.4. Câu hỏi và tiêu chí chuyển sang Chương 3–4\nCác câu hỏi có điều kiện ở tiểu mục trướ",
      "bottom": "rạng thái vật liệu và điều kiện biên tương ứng, thay vì chỉ một giá trị độ cứng. GUM yêu \n",
      "png_sha256": "dd47b30bbf1dc2d779b8361d60cbeb7690ac6f43da9682b0b1d942f7c2f67883"
    },
    {
      "page": 2,
      "text_chars": 3532,
      "fonts": [
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 541.75,
      "min_y": 71.35877990722656,
      "max_y": 758.4927368164062,
      "top": "cầu mô hình phép đo thể hiện các đại lượng đầu vào có liên quan và xem xét tương quan khi ",
      "bottom": "ô hình riêng chưa đủ để bác bỏ cả lớp giải thích ấy hoặc đòi hỏi một luật cấu \nthành mới.\n",
      "png_sha256": "38782e195c5de70a74f66be9c2674686bafc3d625fdc0f9dbfaa86117d6098d0"
    },
    {
      "page": 3,
      "text_chars": 3360,
      "fonts": [
        "TimesNewRomanPS-BoldMT",
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 541.75,
      "min_y": 71.35877990722656,
      "max_y": 760.5607299804688,
      "top": "Trước bước tích hợp nghiên cứu, cần phân biệt ba mức điều kiện: đủ sẵn sàng để thiết kế ho",
      "bottom": "hất quán giữa các mẫu hoặc dưới điều kiện đã thay đổi.\nGUM [4], \nPhụ lục \nB.2.15–\nB.2.16.\n",
      "png_sha256": "d11ca38732df955e07a3a19bc6f73cfe6aeb0fbecadd626181a13e2ad14aa77f"
    },
    {
      "page": 4,
      "text_chars": 3042,
      "fonts": [
        "TimesNewRomanPS-BoldMT",
        "TimesNewRomanPSMT"
      ],
      "min_x": 85.1500015258789,
      "max_x": 536.3860473632812,
      "min_y": 71.79074096679688,
      "max_y": 757.8927612304688,
      "top": "Thuật ngữ tiếng Anh / \ntiếng Việt\nĐịnh nghĩa và ngữ cảnh cơ học\nNguồn\nMeasurement uncertai",
      "bottom": "s on Control Systems \nTechnology, 34(5), 2219–2233, 2026. DOI: 10.1109/TCST.2026.3690756.\n",
      "png_sha256": "8ece10d13f3618d3cfca7af4feec3651537b37b383697683b63f6909f1efa632"
    }
  ]
}
```

FINAL_SELF_REVIEW_DECISION: SELF_REVIEW_COMPLETED_WITH_DOCUMENTED_LIMITATIONS

INDEPENDENT_ACCEPTANCE: REQUIRED_AFTER_DELIVERY; NOT_PERFORMED_BY_THIS_SESSION
