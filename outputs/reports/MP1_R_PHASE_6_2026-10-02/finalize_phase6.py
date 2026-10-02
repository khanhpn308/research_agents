"""Release Phase 6 drafting artifacts only; does not perform the Phase 7 audit."""
from pathlib import Path
import json,hashlib,re
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parents[3];RUN=Path(__file__).parent
DATE='2026-10-02';GATE='READY_FOR_PHASE_7_CLAIM_CITATION_AUDIT'
paths={
 'chapter2_docx':f'docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_{DATE}.docx',
 'drafting_report':f'docs/literature/MP1_R_PHASE_6_CHAPTER_2_DRAFTING_REPORT_{DATE}.md',
 'claim_traceability':f'outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_{DATE}.json',
 'source_reopen_log':f'outputs/plans/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_{DATE}.json',
 'phase7_handoff':f'outputs/plans/MP1_R_PHASE_6_PHASE_7_HANDOFF_{DATE}.json',
}
p5path=f'outputs/plans/MP1_R_PHASE_5_PHASE_6_HANDOFF_{DATE}.json'
p5=json.loads((ROOT/p5path).read_text())
metrics=json.loads((ROOT/'outputs/plans/MP1_R_PHASE_6_DRAFT_METRICS.json').read_text())
trace=json.loads((ROOT/paths['claim_traceability']).read_text())
inventory=json.loads((RUN/'chapter2_content_inventory.json').read_text())
validation=json.loads((RUN/'formatting_and_content_validation.json').read_text())
assert validation['automated_result']=='PASS'
assert validation['docx_sha256']==hashlib.sha256((ROOT/paths['chapter2_docx']).read_bytes()).hexdigest()

# Human visual inspection in this run: all-page contact sheets plus full-size
# equation and concluding-page previews. Tables continue with repeated headers.
validation['visual_validation']='PASS'
validation['visual_inspection']={
 'scope':'All-page previews; full-size equation page and final research-direction page inspected after the relevant corrections.',
 'renderer':'LibreOffice 24.2.7.2; native Times New Roman fonts',
 'page_count':19,
 'observations':['Vietnamese diacritics and equation render correctly.','Headings are black, hierarchical and legible.','Four editable tables fit the page width; continued tables repeat the header.','Top-center page fields render continuously from 1.'],
 'layout_note':'Standalone draft pagination is not the full-thesis offset; references are retained at 13 pt and 1.5-line spacing.',
 'no_independent_scientific_audit_claimed':True,
}
validation['formatting_result']='PASS'
validation['content_boundary_result']='PASS'
(RUN/'formatting_and_content_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2))

uncertainties=[
 {'source_work_ids':['S05a','S05b'],'type':'BIBLIOGRAPHIC_COMPLETENESS','detail':'Verified authors, titles, journal, year and DOI retained. Final issue volume/pages are not established in the accessed repository version and are omitted rather than guessed.','blocks_phase6':False},
 {'source_work_ids':['S11'],'type':'BIBLIOGRAPHIC_COMPLETENESS','detail':'Verified article identifier 04016023 and DOI retained; volume/issue are omitted because not verified.','blocks_phase6':False},
 {'source_work_ids':['V-W02'],'type':'VERSION_METADATA','detail':'Cites publisher-verified online version dated 3 Aug 2021. Historical summaries used 2022; final issue year/pages are not inferred. This is a bibliographic version distinction, not a change in scientific interpretation.','blocks_phase6':False},
]
restrictions={
 'S18':'Zhang, Yao, Zhao, Wei (2025), Mechanical Sciences 16, 821–830, 10.5194/ms-16-821-2025; vacuum-confined PVC layer-jamming theoretical/mechanistic analogue only. No positive-pressure fiber/TiNi/MP1-R validation.',
 'S15':'Secondary laminar-review orientation only; excludes fiber and granular coverage. Not independent mechanics replication.',
 'S17':'Metric-definition/context only; no primary mechanics support.',
 'S19':'QUARANTINED; not cited.', 'S20':'RETIRED; not cited.', 'S21':'QUARANTINED; not cited.',
 'S05':'Two distinct published works, Part I and Part II, retain separate IEEE numbers under one canonical source family.',
 'S07':'Transformation-aware FE with simplified/frictionless contact; not independent friction calibration.',
 'S12':'Physical steel-rope experiments versus numerical SMA results; do not describe SMA as independently experimentally validated.',
 'V-W02':'Formally published cable paper; numerical axial/transformation/contact role, not MP1-R experimental validation. No invented internal-artifact citation.',
 'S22':'Selected internal cable-layer resistance measured; normal load/average pressure inferred using borrowed friction and approximate area; no joint wire–wire/wire–sleeve partition.',
 'S04':'Dedicated wire–rubber sliding-resistance and SMA-friction precedent; resistance does not separately establish μ and N; actuator thermal state is distinct from structural TiNi.',
 'all_sources':'Evidence remains architecture/domain scoped; original publication controls source facts; canonical Phase 4/5 controls transfer and contribution wording.',
}
sections=[v for k,v in inventory['items'] if k=='h2']
rows='\n'.join(f'| {r["number"]} | {r["source_id"]}'+(f' ({r["source_work_id"]})' if r['source_id']!=r['source_work_id'] else '')+' | '+r['restriction'].replace('|','/')+' |' for r in trace['reference_register'])
formatrows='\n'.join(f'| {k} | {v["result"]} |' for k,v in validation['checks'].items())
structure='\n'.join(f'- {s}' for s in sections)
report=f'''# MP1-R — Phase 6: Báo cáo soạn thảo Chương 2 có kiểm soát bằng chứng

## Trạng thái phát hành

`{GATE}`

Bản Chương 2 bằng tiếng Việt đã được tạo thành DOCX Office Open XML thực, có thể chỉnh sửa. Đây là bản thảo để Phase 7 kiểm toán claim–citation; kiểm toán độc lập chưa được thực hiện.

## 1. Đầu vào, quyền hạn và điểm tiếp tục

Đã đọc bốn đầu vào theo thứ tự quy định của lượt Phase 6 ban đầu; phiên tiếp tục sử dụng checkpoint và kiểm tra lại các ranh giới cần thiết:

1. `{p5path}` — quyền hạn duy nhất của Phase 5 cho Phase 6;
2. `docs/literature/MP1_R_PHASE_5_RESEARCH_GAP_AND_CONTRIBUTION_ADJUDICATION_{DATE}.md`;
3. `docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_{DATE}.md`;
4. `docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_{DATE}.md`.

Hash của bốn đầu vào được lưu tại `outputs/reports/MP1_R_PHASE_6_{DATE}/input_manifest.json`; kiểm tra cuối xác nhận các tệp này không bị sửa. Không dùng bản Working Draft Chương 1–2, A_GEMINI/B_GPT hoặc D1/M1 làm mẫu lời văn. Bản nháp trước khi tạm dừng được bảo tồn riêng trong thư mục `checkpoint_backup` của lượt này.

## 2. Skill và cách áp dụng

Đã áp dụng `$academic-paper` phiên bản 3.3.1, từ `/home/khanh/.codex/skills/academic-paper/SKILL.md`, cho kiến trúc chương, lập bản đồ bằng chứng, lập luận claim–evidence, tổng hợp so sánh, tích hợp trích dẫn và tự kiểm tra chất lượng lời văn.

MODE full được giới hạn bởi chỉ dẫn entry giữa pipeline của người dùng: không chạy lại discovery, gap adjudication, peer review hay Phase 7. Bộ soạn DOCX dùng `python-docx`/OOXML trực tiếp vì Pandoc không có trong môi trường; tài liệu dùng cấu trúc Word thực cho đoạn, heading, bảng, field số trang và phương trình OMML. Script `check_acronyms.py` không có trong bộ skill đã cài; kiểm tra thuật ngữ và chữ viết tắt được thực hiện trong nội dung, thay vì báo một lượt kiểm tra script không tồn tại.

## 3. Corpus và mở lại nguồn

Chương sử dụng {metrics['canonical_sources_cited']} Source ID đã được phê duyệt, tương ứng {metrics['unique_references']} công bố/tài liệu tham khảo vì S05 gồm hai bài riêng. Tìm kiếm văn liệu rộng: **0**. Nguồn mới thêm: **0**. Truy vấn văn liệu bên ngoài: **0**.

Có **14** nguồn được mở đối chiếu qua văn bản gốc đã lưu trong kho, chủ yếu trang đầu và header trang, để kiểm tra thông tin thư mục. Log chi tiết: `{paths['source_reopen_log']}`. Đó là S01, S02, S03, S04, S05a, S06, S07, S09, S10, S11, S12, S13, S17 và V-W02. S05b, S15, S18 và S22 sử dụng thông tin đã được thẩm định trong kho; không mở lại toàn văn các nguồn này.

Thông tin thư mục đã được sửa ở bản tạm, gồm các tên viết tắt tác giả không đúng, tạp chí của S17, tập/mã bài của một số công bố và trang đã được xác minh. S18 giữ đúng danh tính và vai trò tương tự dầm lớp PVC dưới hút chân không. V-W02 được trích dẫn theo bản online năm 2021 đã xác minh trên trang nhà xuất bản trong bản lưu, thay vì đoán năm/số tập của bản in. Những sửa chữa này không đổi trạng thái giả thuyết hoặc phạm vi đóng góp được phê duyệt.

| Số IEEE | Source ID / công bố | Giới hạn sử dụng |
|---|---|---|
{rows}

## 4. Bản đồ bằng chứng và kiến trúc chương

Bản đồ từng mục được lưu trước khi dựng bản sửa tại `outputs/reports/MP1_R_PHASE_6_{DATE}/chapter2_evidence_map.json`. Mỗi mục có mục đích, claims, nguồn, sức mạnh theo RP, so sánh, tương phản, giới hạn, liên hệ MP1-R và điều không được tuyên bố. Lời văn và bảng đã được lưu thêm trong inventory có thể tái dựng; Markdown phụ trợ phục vụ kiểm tra, còn DOCX là sản phẩm chính.

{structure}

Bốn bảng so sánh lần lượt trình bày kiến trúc giam giữ, định nghĩa metric, trạng thái từng mắt xích và phân loại nhu cầu còn lại. Một phương trình Coulomb được soạn bằng OMML có thể chỉnh sửa; mọi ký hiệu được giải thích. Không sử dụng hình ngoài hoặc hình sao chép. Các bảng là bảng Word, có header lặp lại khi sang trang.

## 5. Quyết định tổng hợp và chất lượng lời văn

- So sánh theo vật liệu, đường áp suất/phản lực, tiếp diện, điều kiện biên, phép đo và giả thiết mô hình; không gộp hệ hạt, sợi nylon, cáp thép và lớp PVC thành phép lặp lại trên TiNi.
- Phân biệt tồn tại ma sát, lực pháp tuyến đã biết, tiếp diện chi phối và phân rã vòng trễ; không dùng uốn toàn cục để chứng minh cả bốn.
- Giữ riêng độ dốc F–δ, độ cứng tiếp tuyến/cát tuyến M–κ, tổn hao DMA và công vòng trễ; nêu điều kiện của công trên đơn vị chiều dài khi dùng M–κ.
- Tách phép thử TiNi thực nghiệm với mô phỏng SMA, cáp chịu kéo với bó chịu uốn và SMA dẫn động với TiNi chịu lực.
- Đặt hiệu chuẩn, khóa mô hình và kiểm tra trên dữ liệu giữ lại trước mọi giả thuyết về luật bổ sung; sai lệch của một giản lược không bác bỏ toàn bộ cơ học thông thường.
- Dùng tiếng Việt học thuật; giải thích SMA, siêu đàn hồi, dính–trượt, DIC, DMA và nhận dạng hệ thống; dùng nhất quán “lực cản”, “ống bao” và “tiếp diện”.
- Mỗi đoạn có chức năng lập luận hoặc tổng hợp; giới hạn chuyển giao bằng chứng được gắn với hệ được khảo sát. Loại các nhãn RP/GAP/Phase và trạng thái tiếng Anh khỏi lời văn luận văn.

## 6. Ranh giới khoa học được bảo toàn

| Nội dung | Trạng thái |
|---|---|
| Khoảng trống tri thức khoa học được tuyên bố | 0 |
| Nhu cầu đặc trưng hóa thực nghiệm | 2 |
| Yêu cầu nhận dạng hệ thống | 5 |
| Xác nhận kỹ thuật / tích hợp | 1 / 1 |
| H0a-R | PLAUSIBLE |
| H0b-R | PLAUSIBLE |
| H1-R | NOT_YET_DISTINGUISHABLE |
| H1 cần cho thành công luận văn | NO |
| Luật cấu thành mới được tuyên bố | NO |

Đóng góp chính vẫn là đặc trưng hóa định lượng ứng xử uốn phụ thuộc áp suất của bó TiNi đã định với mô hình đối chứng thông thường được khóa. PRQ01, SRQ01 và SRQ02 được chuyển thành lời văn tiếng Việt ở mục 2.12, không thêm câu hỏi chính. Xác nhận nguồn và tích hợp là nhiệm vụ hỗ trợ; hạng tử tương tác bổ sung chỉ là mở rộng có điều kiện.

Mắt xích yếu nhất giữ nguyên: **radial reaction → local wire–wire / wire–sleeve contact normal forces**. Bảng 2.3 diễn đạt tự nhiên mức phụ thuộc mô hình, suy luận, chưa thiết lập và được hỗ trợ một phần; không nâng các mức đó thành xác nhận toàn chuỗi trên MP1-R.

## 7. Trích dẫn và truy xuất

Có **{metrics['in_text_citations']}** lần xuất hiện trích dẫn trong thân chương, bảng và ghi chú; một [n] hoặc một dải [n]–[m] tính là một lần, còn [n], [m] tính hai. Có {metrics['citation_number_tokens']} token số ngoặc vuông nếu đếm riêng hai đầu dải. Danh mục gồm **18** mục, đánh số theo lần xuất hiện đầu tiên; đã kiểm tra theo thứ tự OOXML thật, bao gồm các ô bảng. Không có tài liệu mồ côi, số trích dẫn mồ côi, DOI trùng hoặc trích dẫn tác giả–năm.

Register `{paths['claim_traceability']}` chứa **{metrics['claim_count']}** đơn vị claim ở mức đoạn, hàng bảng, ghi chú và phương trình. Mỗi đơn vị ghi nguồn/công bố, số IEEE, trạng thái bằng chứng, loại trực tiếp/tổng hợp/tương tự/suy luận, RP, GAP/CONTRIB và ranh giới lời văn. Claims về phạm vi dự án dẫn về handoff Phase 5; định nghĩa phương trình và bảng metric có ghi nguồn kế thừa từ đoạn dẫn hoặc ghi chú. Trạng thái `DRAFT_TIME_CHECKED_PHASE7_PENDING` không phải chứng nhận đã hoàn thành Phase 7.

## 8. Thông tin thư mục còn giới hạn

- **S05a/S05b:** giữ tên tác giả, tiêu đề, tạp chí, năm và DOI đã xác minh; số tập/trang bản in chưa được thiết lập trong phiên bản kho đã dùng nên được bỏ trống.
- **S11:** giữ mã bài 04016023 và DOI đã xác minh; không suy đoán tập/số.
- **V-W02:** dùng bản online ngày 03-08-2021 đã xác minh; không suy đoán năm/trang của bản in từ tên tệp hoặc DOI.

Các giới hạn này được ghi trước phát hành. Không có xung đột bằng chứng nội bộ ngăn cản lập luận bảo thủ; Phase 7 cần kiểm tra độ đầy đủ của các trường thư mục và sự phù hợp claim–citation.

## 9. Kiểm tra Word và hiển thị

DOCX đã được mở lại bằng `python-docx`, kiểm tra XML trong gói OOXML, rồi mở và kết xuất bằng LibreOffice 24.2.7.2 với font Times New Roman thực. Microsoft Word không có trong môi trường; không tuyên bố đã chạy ứng dụng đó. Đã xem bản xem trước toàn trang và các trang công thức/kết luận sau sửa. Bản riêng có **19 trang**, số trang tự động từ 1 ở đầu trang, giữa.

| Kiểm tra | Kết quả |
|---|---|
{formatrows}
| Kiểm tra trực quan | PASS |

Thông số áp dụng: A4; thân Times New Roman 13 pt; dãn dòng 1,5; căn đều; thụt đầu dòng 1 cm; lề trên/dưới/trái/phải 3/3/3,5/2 cm. Sai khác dưới 0,003 cm do làm tròn twip được chấp nhận. Heading chương 16 pt đậm, chữ hoa, căn giữa; heading mục 13 pt đậm, màu đen. Font bảng/ghi chú 11–12 pt để bảo đảm đọc được; bảng vẫn chỉnh sửa được. Phương trình có delimiter và chỉ số OMML thực, đã kiểm tra hiển thị.

Kết quả kiểm tra chi tiết: `outputs/reports/MP1_R_PHASE_6_{DATE}/formatting_and_content_validation.json`. Bộ dựng và script kiểm tra được lưu cùng thư mục để phục vụ tái lập.

## 10. Sản phẩm và handoff

- DOCX: `{paths['chapter2_docx']}`
- Claim traceability: `{paths['claim_traceability']}`
- Reopen log: `{paths['source_reopen_log']}`
- Handoff: `{paths['phase7_handoff']}`

Không có kết quả thí nghiệm MP1-R được tạo hoặc suy diễn. Phase 6 kết thúc tại việc soạn thảo và tự kiểm tra; bước kế tiếp là kiểm toán claim–citation độc lập theo handoff. Chưa thực hiện Phase 7, peer review, Chương 1 hoặc Chương 3.
'''
(ROOT/paths['drafting_report']).write_text(report,encoding='utf-8')

handoff={
 'schema_version':'1.1','artifact_type':'phase6_phase7_handoff','date':DATE,'timezone':'Asia/Bangkok','workstream':'MP1-R',
 'phase6_status':GATE,'exit_gate':GATE,'release_status':'READY',
 'authority_statement':'This is the Phase 6 drafting handoff for the Phase 7 claim–citation/scientific-integrity audit. Phase 5 remains authoritative for contribution and scope boundaries.',
 **paths,
 'citation_style':'IEEE numeric, first-appearance order','output_language':'Vietnamese',
 'citation_count':metrics['in_text_citations'],'reference_count':18,'canonical_source_count':17,'citation_counting_rule':metrics['counting_rule'],
 'subsection_count':12,'subsection_list':sections,'claim_count':metrics['claim_count'],
 'source_reopen_count':14,'broad_literature_searches':0,'new_sources_added':0,
 'source_restrictions':restrictions,'evidence_strength_restrictions':p5['evidence_strength_restrictions'],
 'canonical_evidence_strength_map':{rp:s for c in trace['claims'] for rp,s in c['evidence_status'].items() if rp.startswith('RP')},
 'prohibited_claims':p5['prohibited_claims'],
 'gap_boundary':{'approved_classifications':p5['approved_gap_need_classifications'],'scientific_knowledge_gap_claims_introduced':0,'wording':'Unestablished in the validated corpus / project-specific characterization or identification; no literature-wide absence or first-ever claim.'},
 'primary_contribution':p5['primary_contribution'],'secondary_contributions':p5['secondary_contributions'],'supporting_contributions':p5['supporting_contributions'],
 'final_candidate_research_questions':p5['final_candidate_research_questions'],
 'hypothesis_state':{'H0a-R':'PLAUSIBLE','H0b-R':'PLAUSIBLE','H1-R':'NOT_YET_DISTINGUISHABLE'},
 'thesis_success_requires_h1':False,'new_constitutive_law_claimed':False,
 'critical_weakest_causal_chain_link':'radial reaction → local wire–wire / wire–sleeve contact normal forces',
 'causal_chain_status':[{'link':l,'canonical_status':st} for l,st in [
    ('fluid pressure → membrane/enclosure response','MODEL_DEPENDENT'),('membrane/enclosure response → radial reaction','INFERRED'),
    ('radial reaction → local contact normal forces','NOT_ESTABLISHED'),('local contact normal forces → friction capacity','MODEL_DEPENDENT'),
    ('friction capacity → slip regime','MODEL_DEPENDENT'),('slip regime → bending response','PARTIALLY_SUPPORTED')]],
 'working_title_vietnamese':'ĐẶC TRƯNG HÓA ỨNG XỬ UỐN PHỤ THUỘC ÁP SUẤT CỦA BÓ DÂY TiNi VỚI NGUỒN ÁP SUẤT DẪN ĐỘNG BẰNG LÒ XO SMA',
 'approved_chapter2_gap_wording':p5['approved_chapter2_gap_wording'],
 'known_drafting_uncertainties':uncertainties,'unresolved_material_issues':[],
 'formatting_validation':validation,
 'recommended_phase7_audit_targets':[
    'Check every substantive claim against its actual source and preserve architecture/domain restrictions, not merely the presence of a citation.',
    'Verify S05 two-work bibliography, S11 missing volume/issue and V-W02 online-versus-print version without inventing metadata.',
    'Verify S18 vacuum PVC analogue, S15 laminar-review scope and S17 metric-context-only use.',
    'Verify S12 physical steel versus numerical SMA; V-W02 numerical axial scope; S04/S22 resistance versus independently known μ/N.',
    'Check metric dimensions, Coulomb bound assumptions and work-per-length versus total work/local dissipation.',
    'Check that global bending does not identify a dominant interface and that same-lot TiNi identity does not prove active transformation.',
    'Check PRQ01/SRQ01/SRQ02 and characterization/model discrimination boundary; ensure no claim requires H1.',
    'Check citations in editable table cells/notes as well as prose; first-appearance numbering and bibliography identities.',
    'Audit each clause of paragraph/row-level trace entries; RP evidence labels are canonical support/boundaries, not automatic proof of every clause.',
 ],
 'provenance':{'phase5_authority':p5path,'primary_inputs':trace['primary_input_manifest'],'canonical_phase4':p5['canonical_phase4_provenance'],'academic_skill':'/home/khanh/.codex/skills/academic-paper/SKILL.md','resume_checkpoint':f'docs/project/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_{DATE}.md','evidence_map':trace['evidence_map_path'],'reproducible_builder':str((RUN/'build_chapter2.py').relative_to(ROOT))},
 'phase7_audit_executed':False,'peer_review_executed':False,'stop_after_phase6':True,
}
handoff['artifact_hashes']={k:hashlib.sha256((ROOT/v).read_bytes()).hexdigest() for k,v in paths.items() if k!='phase7_handoff'}
(ROOT/paths['phase7_handoff']).write_text(json.dumps(handoff,ensure_ascii=False,indent=2))

# Preserve the paused state historically and add a clear current-state note.
checkpoint=ROOT/f'docs/project/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_{DATE}.md'
mark='## Resume completion — Phase 6 released'
note=f'''\n\n{mark}\n\nThe user subsequently requested “tiếp tục công việc”. The preceding paused-state description is historical. Current status: `{GATE}`.\n\nThe resumed run corrected draft citation ordering, bibliographic identities, metric/causal wording and Word rendering; Phase 3–5 scientific authorities remained unchanged. The final draft has 12 sections, 18 references, {metrics['in_text_citations']} citation appearances and {metrics['claim_count']} trace entries. The targeted archived-source reopen count is now 14; the earlier zero count remains historical.\n\nAll five required Phase 6 artifacts exist. Continue next with `{paths['phase7_handoff']}`; Phase 7 has not been executed.\n'''
text=checkpoint.read_text()
if mark not in text:checkpoint.write_text(text+note)
cpj=ROOT/f'outputs/plans/MP1_R_PHASE_6_NEXT_SESSION_CHECKPOINT_{DATE}.json'
cp=json.loads(cpj.read_text());cp['resume_completion']={'status':GATE,'user_resume_request':'tiếp tục công việc','phase7_handoff':paths['phase7_handoff'],'earlier_pause_fields_are_historical':True,'original_sources_reopened_in_resumed_run':14}
cpj.write_text(json.dumps(cp,ensure_ascii=False,indent=2))
print(json.dumps({'status':GATE,'metrics':metrics,'paths':paths},ensure_ascii=False,indent=2))
