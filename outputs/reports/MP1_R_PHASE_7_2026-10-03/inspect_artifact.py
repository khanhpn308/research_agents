"""Read-only reconstruction of the actual Phase 6 DOCX audit surfaces."""
from pathlib import Path
from hashlib import sha256
import json
import re
from collections import Counter
from zipfile import ZipFile
from docx import Document
from docx.oxml.ns import qn
from lxml import etree

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent
TARGET = ROOT / 'docs/project/MP1_R_CHAPTER_2_EVIDENCE_CONTROLLED_DRAFT_2026-10-02.docx'
TRACE = ROOT / 'outputs/plans/MP1_R_PHASE_6_CHAPTER_2_CLAIM_TRACEABILITY_2026-10-02.json'

def digest(p):
    return sha256(p.read_bytes()).hexdigest()

def txt(e):
    return ''.join(n.text or '' for n in e.iter() if n.tag in (qn('w:t'), qn('m:t')))

def extract(path):
    doc = Document(path)
    blocks = []
    section = None
    pi = ti = 0
    references = False
    for e in doc.element.body:
        if e.tag == qn('w:p'):
            pi += 1
            t = txt(e)
            if re.match(r'^2\.\d+\.', t):
                section = re.match(r'^(2\.\d+)\.', t)[1]
            if t == 'TÀI LIỆU THAM KHẢO':
                references = True
            kind = 'reference' if references else ('heading' if re.match(r'^2\.\d+\.', t) or t.startswith('CHƯƠNG') else 'caption' if re.match(r'^Bảng 2\.\d+\.', t) else 'equation' if e.xpath('.//m:oMath') else 'prose')
            blocks.append({'location': f'P{pi:03}', 'paragraph_index': pi, 'section': section, 'kind': kind, 'text': t, 'xml': etree.tostring(e, encoding='unicode') if kind == 'equation' else None})
        elif e.tag == qn('w:tbl'):
            ti += 1
            for ri, row in enumerate(e.findall(qn('w:tr')), 1):
                cells = [txt(c) for c in row.findall(qn('w:tc'))]
                blocks.append({'location': f'T{ti}R{ri}', 'table_index': ti, 'row_index': ri, 'section': section, 'kind': 'table_header' if ri == 1 else 'table_row', 'text': ' | '.join(cells), 'cells': cells})
    return doc, blocks

def citations(blocks):
    out = []
    for b in blocks:
        if b['kind'] == 'reference':
            continue
        for m in re.finditer(r'\[(\d+)\](?:[–−-]\[(\d+)\])?', b['text']):
            numbers = list(range(int(m[1]), int(m[2]) + 1)) if m[2] else [int(m[1])]
            out.append({'appearance_id': f'P7CA{len(out)+1:03}', 'location': b['location'], 'section': b['section'], 'offset': m.start(), 'citation': m[0], 'numbers': numbers, 'context': b['text'], 'range_requires_all_members': len(numbers) > 1})
    return out

def main():
    doc, blocks = extract(TARGET)
    trace = json.loads(TRACE.read_text())
    mappings = []
    for c in trace['claims']:
        found = [b for b in blocks if b['text'] == c['claim_text']]
        # OMML encodes absolute bars in delimiter properties, not m:t text nodes.
        if c['claim_id'] == 'CH2C018':
            found = [b for b in blocks if b['kind'] == 'equation']
            assert len(found) == 1 and 'm:begChr m:val="|"' in found[0]['xml'] and 'm:endChr m:val="|"' in found[0]['xml']
        assert len(found) == 1, c['claim_id']
        b = found[0]
        mappings.append({'phase6_claim_id': c['claim_id'], 'docx_location': b['location'], 'section': b['section'], 'text_matches': b['text'] == c['claim_text'], 'normalization_note': 'OMML absolute bars/subscripts and equation number reconstructed from XML' if c['claim_id'] == 'CH2C018' else None})
    substantive = [b for b in blocks if b['kind'] in ('prose', 'equation', 'table_row')]
    claimed = {m['docx_location'] for m in mappings}
    unregistered = [b for b in substantive if b['location'] not in claimed]
    apps = citations(blocks)
    first = []
    for a in apps:
        for n in a['numbers']:
            if n not in first:
                first.append(n)
    inputs = [
        'outputs/plans/MP1_R_PHASE_6_PHASE_7_HANDOFF_2026-10-02.json',
        str(TARGET.relative_to(ROOT)), str(TRACE.relative_to(ROOT)),
        'outputs/plans/MP1_R_PHASE_6_SOURCE_REOPEN_LOG_2026-10-02.json',
        'outputs/plans/MP1_R_PHASE_5_PHASE_6_HANDOFF_2026-10-02.json',
        'docs/literature/MP1_R_PHASE_4_RECONCILED_SYNTHESIS_2026-10-02.md',
        'docs/literature/MP1_R_PHASE_3_METHODOLOGICAL_APPRAISAL_AND_EVIDENCE_INTEGRITY_2026-10-02.md',
    ]
    integrity = {'date': '2026-10-03', 'timezone': 'Asia/Bangkok', 'inputs': [{'read_order': i, 'path': p, 'sha256': digest(ROOT/p)} for i,p in enumerate(inputs,1)], 'primary_docx_hash_matches_handoff': digest(TARGET) == json.loads((ROOT/inputs[0]).read_text())['artifact_hashes']['chapter2_docx'], 'substantive_audit_units': len(substantive), 'trace_units': len(mappings), 'unregistered_substantive_units': unregistered, 'heading_caption_header_surfaces_reviewed_separately': [b['location'] for b in blocks if b['kind'] in ('heading','caption','table_header')], 'citation_appearances': len(apps), 'expanded_reference_mentions': sum(len(a['numbers']) for a in apps), 'reference_count': sum(b['kind']=='reference' and bool(re.match(r'^\[\d+\]',b['text'])) for b in blocks), 'table_count': len(doc.tables), 'display_equation_count': sum(b['kind']=='equation' for b in blocks), 'subsection_count': len({b['section'] for b in blocks if b['section']}), 'first_appearance_order': first, 'trace_location_mappings': mappings, 'zip_crc_error': ZipFile(TARGET).testzip()}
    for name, value in [('actual_docx_inventory.json',blocks),('citation_appearances_original.json',apps),('artifact_integrity_original.json',integrity)]:
        (RUN/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in integrity.items() if k not in ('inputs','trace_location_mappings','heading_caption_header_surfaces_reviewed_separately')},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
