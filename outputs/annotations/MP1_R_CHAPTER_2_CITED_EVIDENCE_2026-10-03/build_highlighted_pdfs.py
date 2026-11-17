"""Write editable PDF highlights and a source/claim index; preserve inputs."""
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf
from docx import Document

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
DOCX = ROOT / 'docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx'
TRACE = ROOT / 'outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json'
INPUTS = json.loads((OUT / 'inputs.json').read_text())
CACHE = json.loads((OUT / 'pdf_text_geometry.json').read_text())
UNITS = json.loads((OUT / 'curated_passages.json').read_text())
TRACE_DATA = json.loads(TRACE.read_text())
CLAIMS = {x['claim_id']: x for x in TRACE_DATA['claims']}
REFS = {x['source_work_id']: x for x in TRACE_DATA['reference_register']}
COLORS = {'FINDING': (1, .90, .20), 'METHOD_MODEL': (.25, .70, 1),
          'LIMITATION_SCOPE': (1, .55, .15)}
COLOR_NAMES = {'FINDING': 'Vàng: kết quả/mô tả được bài gốc báo cáo',
               'METHOD_MODEL': 'Xanh: phương pháp, mô hình, quan hệ tính toán',
               'LIMITATION_SCOPE': 'Cam: giả thiết, phạm vi hoặc giới hạn suy luận'}
PDF_DIR = OUT / 'pdf'
PDF_DIR.mkdir(exist_ok=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_digest(doc):
    return hashlib.sha256('\f'.join(p.get_text() for p in doc).encode()).hexdigest()


def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


DOCX_HASH = sha(DOCX)
assert DOCX_HASH == '3c94a19f66536bcc08b1c3cd79ee44bea9b3b85ab658e6c7e0810d43e2791b45'
original_artifact_hashes = {str(p.relative_to(ROOT)): sha(p) for p in [DOCX, TRACE]}
source_units = defaultdict(list)
for u in UNITS:
    assert u['source_work_id'] in REFS
    assert u['role'] in COLORS
    for claim_id in u['claim_ids']:
        assert claim_id in CLAIMS
        assert u['source_work_id'] in CLAIMS[claim_id]['source_work_ids'], (u['highlight_id'], claim_id)
    source_units[u['source_work_id']].append(u)

pdf_records = []
highlight_records = []
for src in INPUTS:
    sid = src['source_work_id']
    input_path = Path(src['path'])
    if not input_path.is_absolute(): input_path = ROOT / input_path
    assert sha(input_path) == src['sha256']
    original = pymupdf.open(input_path)
    assert not original.needs_pass
    before_text = text_digest(original)
    original_annotation_count = sum(len(list(p.annots() or [])) for p in original)
    for u in source_units[sid]:
        page = original[u['pdf_page']-1]
        page_data = CACHE[sid]['pages'][u['pdf_page']-1]
        blocks = {b['block_id']: b for b in page_data['blocks']}
        quads, excerpts, geometry = [], [], []
        for sel in u['selections']:
            selected_lines = blocks[sel['block_id']]['lines'][sel['line_start']:sel['line_end_exclusive']]
            for line in selected_lines:
                if not line['text'].strip(): continue
                rect = pymupdf.Rect(line['bbox'])
                assert rect.width > 0 and rect.height > 0
                assert rect.x0 >= -.5 and rect.y0 >= -.5
                assert rect.x1 <= page.rect.width+.5 and rect.y1 <= page.rect.height+.5
                # All selected passages have horizontal text. Reject rotated selection.
                assert abs(line['dir'][0]-1) < .001 and abs(line['dir'][1]) < .001
                quads.append(pymupdf.Quad(rect.tl, rect.tr, rect.bl, rect.br))
                geometry.append({'text': line['text'], 'bbox': line['bbox']})
            excerpts.append('\n'.join(l['text'] for l in selected_lines))
        assert quads
        sections = sorted({CLAIMS[x]['chapter_subsection'] for x in u['claim_ids']}, key=lambda t: [int(y) for y in t.split('.')])
        number = REFS[sid]['number']
        content = '\n'.join([
            f"Chương 2 — tài liệu [{number}] ({sid}); trang PDF {u['pdf_page']}",
            f"Ý được đối chiếu: {u['idea_vi']}",
            f"Mục liên quan: {', '.join(sections)}",
            f"Vai trò đoạn: {COLOR_NAMES[u['role']]}",
            f"Giới hạn: {u['wording_boundary_vi']}",
            'Đoạn tô hỗ trợ phần phát biểu tương ứng; không tự xác minh mọi mệnh đề trong đoạn tổng hợp.',
            f"Mã tra cứu: {u['highlight_id']}; {', '.join(u['claim_ids'])}",
        ])
        annot = page.add_highlight_annot(quads)
        annot.set_colors(stroke=COLORS[u['role']])
        annot.set_opacity(.32)
        annot.set_info(title=f'MP1-R | [{number}] {sid}', subject=u['idea_vi'], content=content)
        original.xref_set_key(annot.xref, 'NM', pymupdf.get_pdf_str(u['highlight_id']))
        annot.update()
        record = dict(u)
        record.update(ieee_reference_number=number, chapter_subsections=sections,
                      original_excerpt='\n\n'.join(excerpts), line_geometry=geometry,
                      annotation_color_rgb=list(COLORS[u['role']]), annotation_opacity=.32,
                      location_check='PDF_TEXT_GEOMETRY_CHECKED',
                      interpretation='PASSAGE_LOCATED_NOT_A_FULL_CLAIM_CITATION_AUDIT')
        highlight_records.append(record)
    output_path = PDF_DIR / f"{REFS[sid]['number']:02d}_{sid}_HIGHLIGHTED.pdf"
    meta = dict(original.metadata)
    meta['subject'] = (meta.get('subject') or '') + ' | MP1-R Chapter 2 cited passages; annotations only'
    original.set_metadata(meta)
    original.save(output_path, garbage=3, deflate=True)
    page_count = len(original)
    original.close()
    checked = pymupdf.open(output_path)
    new_annotations = [a.info for p in checked for a in (p.annots() or [])
                       if a.info.get('id') in {u['highlight_id'] for u in source_units[sid]}]
    assert len(checked) == page_count
    assert text_digest(checked) == before_text
    assert len(new_annotations) == len(source_units[sid])
    assert sum(len(list(p.annots() or [])) for p in checked) == original_annotation_count + len(source_units[sid])
    assert all('Ý được đối chiếu:' in x['content'] for x in new_annotations)
    checked.close()
    assert sha(input_path) == src['sha256']
    pdf_records.append({
        'reference_number': REFS[sid]['number'], 'source_work_id': sid,
        'bibliographic_entry': REFS[sid]['bibliographic_entry'],
        'original_pdf_path': src['path'], 'original_sha256': src['sha256'],
        'highlighted_pdf_path': str(output_path.relative_to(ROOT)), 'highlighted_sha256': sha(output_path),
        'page_count': page_count, 'pdf_pages_highlighted': sorted({u['pdf_page'] for u in source_units[sid]}),
        'highlights_added': len(source_units[sid]), 'original_annotations_preserved': original_annotation_count,
        'text_unchanged': True, 'original_unchanged': True, 'native_highlight_annotations': True,
    })


# The traceability table sometimes cites an entire source group for a metric row.
# Preserve that history while refusing to call unrelated rows directly supported.
metric_row_support = {
    'CH2C025': {'S03', 'S06'},
    'CH2C026': {'S03'},
    'CH2C027': {'S13'},
    'CH2C028': {'S06'},
}
project_inference_claims = {'CH2C019', 'CH2C031', 'CH2C035', 'CH2C036', 'CH2C042',
                          'CH2C044', 'CH2C050', 'CH2C056', 'CH2C057', 'CH2C058',
                          'CH2C059', 'CH2C060', 'CH2C061', 'CH2C062', 'CH2C067',
                          'CH2C068', 'CH2C069'}
pair_records = []
for claim in TRACE_DATA['claims']:
    for sid in claim['source_work_ids']:
        linked = [u for u in source_units[sid] if claim['claim_id'] in u['claim_ids']]
        cid = claim['claim_id']
        if cid in metric_row_support and sid not in metric_row_support[cid]:
            status = 'TABLE_LEVEL_CONTEXT_ONLY_NOT_ROW_EVIDENCE'
            reason = ('Nguồn thuộc nhóm trích dẫn chung của bảng, nhưng đoạn tô không chứng minh riêng đại lượng của hàng này. '
                      'Không tạo highlight giả để ép đủ độ phủ; xem các đoạn của nguồn như bối cảnh của bảng.')
            direct = []
            context = [u['highlight_id'] for u in source_units[sid]]
        elif cid in {'CH2C024', 'CH2C030'}:
            status = 'CHAPTER_METRIC_DEFINITION_WITH_SOURCE_CONTEXT'
            reason = ('Các nguồn minh họa thước đo khác nhau; định nghĩa, phân tích thứ nguyên và giới hạn phép suy của Chương 2 '
                      'là tổng hợp. Không có một câu nguyên văn trong mỗi nguồn chứng minh toàn bộ đoạn.')
            direct = []
            context = [u['highlight_id'] for u in linked]
        elif cid in metric_row_support:
            status = 'PARTIAL_METRIC_SUPPORT'
            reason = ('Đoạn tô hỗ trợ đại lượng vận hành tương ứng trong bài gốc; các công thức định nghĩa tổng quát '
                      'và cột không được suy ra của bảng là diễn giải/phân tích của Chương 2.')
            direct = [u['highlight_id'] for u in linked]
            context = []
        elif cid in project_inference_claims or claim['classification'] == 'inference':
            status = 'SOURCE_COMPONENT_PLUS_PROJECT_INFERENCE'
            reason = ('Đoạn tô là phần bằng chứng nền của nguồn. Kết luận về nhận dạng, giả thuyết, chuỗi nhân quả, '
                      'nhu cầu quan sát hoặc phần chưa xác định của MP1-R là suy luận có giới hạn của Chương 2; '
                      'không phải kết quả nguyên văn/thí nghiệm MP1-R trong bài gốc.')
            direct = []
            context = [u['highlight_id'] for u in linked]
        elif linked:
            status = 'SOURCE_PASSAGES_LOCATED_FOR_CITED_COMPONENT'
            reason = ('Đã xác định đoạn tương ứng với thành phần phát biểu về nguồn; so sánh, chuyển kiến trúc và giới hạn '
                      'suy luận cần đọc kèm ghi chú từng đoạn. Trạng thái này không thay cho kiểm toán toàn bộ mệnh đề.')
            direct = [u['highlight_id'] for u in linked]
            context = []
        else:
            status = 'NO_SPECIFIC_PASSAGE_ASSIGNED'
            reason = 'Chưa gán đoạn cụ thể; không khẳng định đã tìm được bằng chứng trực tiếp.'
            direct = context = []
        pair_records.append({
            'claim_id': cid, 'chapter_subsection': claim['chapter_subsection'],
            'chapter_location': claim['location'], 'claim_text': claim['claim_text'],
            'source_work_id': sid, 'ieee_reference_number': REFS[sid]['number'],
            'chapter_evidence_classification': claim['classification'],
            'inherited_table_citation': claim['citation_inherited_from_lead_or_table_note'],
            'correspondence_status': status, 'highlight_ids': direct,
            'context_highlight_ids': context, 'explanation_vi': reason,
            'phase4_proposition_mapping': claim['phase4_proposition_mapping'],
            'phase5_gap_mapping': claim['phase5_gap_mapping'],
            'phase5_contribution_mapping': claim['phase5_contribution_mapping'],
        })

assert all(x['correspondence_status'] != 'NO_SPECIFIC_PASSAGE_ASSIGNED' for x in pair_records)
assert sha(DOCX) == DOCX_HASH
assert all(sha(ROOT / p) == h for p, h in original_artifact_hashes.items())

docx = Document(DOCX)
body = []
references_started = False
for p in docx.paragraphs:
    if p.text.strip() == 'TÀI LIỆU THAM KHẢO': references_started = True
    if not references_started: body.append(p.text)
for table in docx.tables:
    for row in table.rows:
        body.extend(cell.text for cell in row.cells)
cited_numbers = set(map(int, re.findall(r'\[(\d+)\]', '\n'.join(body))))
assert cited_numbers == set(range(1,19))

summary = {
    'pdf_sources': len(pdf_records), 'highlight_annotations_added': len(highlight_records),
    'cited_claim_entries': len({p['claim_id'] for p in pair_records}),
    'claim_source_pairs': len(pair_records),
    'correspondence_status_counts': dict(Counter(p['correspondence_status'] for p in pair_records)),
    'colors': {k: {'rgb': list(v), 'meaning_vi': COLOR_NAMES[k]} for k,v in COLORS.items()},
    'original_pdf_files_unchanged': True, 'chapter_docx_unchanged': True,
    'all_outputs_reopened': True, 'page_counts_unchanged': True, 'source_text_unchanged': True,
    'broad_literature_searches': 0, 'new_sources_added': 0, 'phase7_audit_executed': False,
}

dump(OUT / 'HIGHLIGHT_REGISTER.json', {
    'schema_version': '1.0', 'artifact_type': 'chapter2_pdf_evidence_highlight_register',
    'date': '2026-10-03', 'workstream': 'MP1-R',
    'chapter_docx_path': str(DOCX.relative_to(ROOT)), 'chapter_docx_sha256': DOCX_HASH,
    'claim_traceability_path': str(TRACE.relative_to(ROOT)), 'claim_traceability_sha256': sha(TRACE),
    'page_convention': 'One-based PDF page index; not necessarily the printed page number',
    'scope': 'Annotation and evidence-location only; no scientific register changes, no formal Phase 7 audit',
    'summary': summary, 'sources': pdf_records, 'highlights': highlight_records,
})
dump(OUT / 'CLAIM_SOURCE_MAP.json', {
    'schema_version': '1.0', 'artifact_type': 'chapter2_claim_to_pdf_passage_map',
    'date': '2026-10-03', 'chapter_docx_sha256': DOCX_HASH,
    'important_boundary': 'Locating a source component is not attestation that every clause of a synthesis paragraph is directly demonstrated.',
    'pair_count': len(pair_records), 'pairs': pair_records,
})
dump(OUT / 'VALIDATION.json', summary)

lines = [
    '# PDF đã tô sáng bằng chứng được trích dẫn trong Chương 2', '',
    'Đã tạo **18 bản PDF mới**, chứa **' + str(len(highlight_records)) + ' chú thích highlight**. '
    'Các PDF gốc, Chương 2 DOCX và hồ sơ khoa học được giữ nguyên.', '',
    'Đối chiếu với: `docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx`.', '',
    '## Cách đọc', '',
    '- **Vàng:** kết quả hoặc mô tả được nguồn gốc báo cáo.',
    '- **Xanh:** phương pháp, mô hình và quan hệ tính toán.',
    '- **Cam:** giả thiết, phạm vi áp dụng và giới hạn suy luận.', '',
    'Mỗi vùng tô có ghi chú chứa ý tiếng Việt, mục Chương 2, số tài liệu IEEE, giới hạn và mã tra cứu. '
    'Nhấp hoặc mở bảng Comments/Annotations trong trình đọc PDF để xem. Đây là chú thích PDF gốc có thể chỉnh sửa, '
    'không phải màu được chụp thành ảnh. Số trang bên dưới là **thứ tự trang PDF tính từ 1**, '
    'có thể khác số trang in của bài báo/luận văn.', '',
    '## Danh mục 18 tài liệu', '',
    '| IEEE | Nguồn | Bản PDF đã tô | Trang PDF | Số vùng tô |',
    '|---|---|---|---|---:|',
]
for x in sorted(pdf_records, key=lambda x:x['reference_number']):
    name = Path(x['highlighted_pdf_path']).name
    lines.append(f"| [{x['reference_number']}] | {x['source_work_id']} | [{name}](pdf/{name}) | "
                 f"{', '.join(map(str,x['pdf_pages_highlighted']))} | {x['highlights_added']} |")
lines += [
    '', '## Ranh giới của việc đối chiếu', '',
    'Một đoạn tổng hợp trong Chương 2 có thể dựa trên nhiều kết quả và không có câu tương đương nguyên văn '
    'trong một bài. Các suy luận về MP1-R, yêu cầu nhận dạng, trạng thái giả thuyết và phần chưa được thiết lập '
    'được ghi là **bằng chứng nền cộng suy luận của luận văn**, không gọi là kết quả được bài gốc chứng minh trực tiếp.', '',
    'Bảng định nghĩa thước đo ở mục 2.3 dùng nhóm nguồn chung. Có **' +
    str(summary['correspondence_status_counts'].get('TABLE_LEVEL_CONTEXT_ONLY_NOT_ROW_EVIDENCE',0)) +
    ' cặp hàng–nguồn chỉ là bối cảnh cấp bảng**, không phải bằng chứng riêng cho hàng. '
    'Ví dụ nguồn DMA không chứng minh công thức độ cứng uốn tĩnh. Các trường hợp này được ghi rõ trong '
    '`CLAIM_SOURCE_MAP.json`; không tô một câu không liên quan để tạo cảm giác tất cả ô bảng đều có bằng chứng trực tiếp.', '',
    'Các công thức định nghĩa và phân tích thứ nguyên là phần tổng hợp của Chương 2. Các kết luận chưa xác định '
    'đối với MP1-R không được biến thành phát biểu rằng khoa học chưa biết hoặc không có nghiên cứu nào.', '',
    'Các giới hạn nổi bật được giữ trong ghi chú:', '',
    '- S18 là **layer-jamming PVC hút chân không**, chỉ là tương tự cơ học cho MP1-R.',
    '- S15 là tổng quan laminar jamming, không thay thế nguồn thực nghiệm sơ cấp.',
    '- S17 chỉ hỗ trợ thận trọng về thước đo và đơn vị.',
    '- S07 có đoạn thân bài nêu **bỏ qua ma sát** giữa các tao; phần tiếng Anh chỉ giúp định vị phương pháp.',
    '- S22 đo lực cản; lực pháp tuyến/áp lực được suy từ hệ số ma sát tham khảo và diện tích xấp xỉ.',
    '- S12 có thực nghiệm thép; mô hình SMA đối chiếu dữ liệu từ nghiên cứu trước.',
    '- V-W02 là bài số đã xuất bản, dùng niên đại online 2021; tên PDF có 2022 không sửa danh tính bài.', '',
    '## Hồ sơ tra cứu', '',
    '- [HIGHLIGHT_REGISTER.json](HIGHLIGHT_REGISTER.json): từng vùng tô, trích đoạn, trang, hình học, mục chương và mã ý.',
    '- [CLAIM_SOURCE_MAP.json](CLAIM_SOURCE_MAP.json): từng cặp ý–nguồn, phân biệt đoạn hỗ trợ và bối cảnh/suy luận.',
    '- [VALIDATION.json](VALIDATION.json): kiểm tra file mở lại được, số trang, văn bản, annotation và bảo toàn đầu vào.', '',
    '## Các vùng tô', '',
]
for src in sorted(pdf_records, key=lambda x:x['reference_number']):
    sid = src['source_work_id']
    lines += [f"### [{src['reference_number']}] {sid}", '', src['bibliographic_entry'], '',
              '| Mã vùng tô | Trang PDF | Màu/vai trò | Ý đối chiếu | Mục Chương 2 |',
              '|---|---:|---|---|---|']
    for u in highlight_records:
        if u['source_work_id'] == sid:
            color = {'FINDING':'Vàng','METHOD_MODEL':'Xanh','LIMITATION_SCOPE':'Cam'}[u['role']]
            lines.append(f"| {u['highlight_id']} | {u['pdf_page']} | {color} | {u['idea_vi']} | {', '.join(u['chapter_subsections'])} |")
    lines.append('')
lines += ['## Kiểm tra bảo toàn và phạm vi công việc', '',
          'Đã mở lại cả 18 PDF đầu ra, đối chiếu số trang và văn bản với PDF gốc, kiểm tra đủ chú thích mới '
          'và ghi chú tiếng Việt. Hash của PDF gốc và DOCX không đổi. Không thêm nguồn, không tìm kiếm tài liệu '
          'và không sửa nội dung khoa học. Việc này là định vị/tô sáng bằng chứng, không thực hiện Phase 7.', '']
(OUT / 'README.md').write_text('\n'.join(lines))
print(json.dumps(summary, ensure_ascii=False))
