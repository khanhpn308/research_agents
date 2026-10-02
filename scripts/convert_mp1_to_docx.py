import re
import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders_none(table):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="none"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def parse_inline_into_paragraph(paragraph, text, base_font_size=12, default_italic=False):
    # Regex to capture tokens:
    # 1. Evidence badges (with or without ** around them):
    # 2. Hyperlinks: [text](url) or [text](<url>)
    # 3. Inline code: `code`
    # 4. Bold italic: ***text***
    # 5. Bold: **text**
    # 6. Italic: *text*
    token_pattern = re.compile(
        r'(\*{0,2}\[(?:HỒ SƠ QUYẾT ĐỊNH[^\]]*|VERIFIED FULL TEXT[^\]]*|METADATA ONLY[^\]]*|INFERENCE[^\]]*|HYPOTHESIS[^\]]*)\]\*{0,2})'
        r'|(\[[^\]]+\]\((?:<[^>]+>|[^\)]+)\))'
        r'|(`[^`]+`)'
        r'|(\*\*\*[^*]+\*\*\*)'
        r'|(\*\*[^*]+\*\*)'
        r'|(\*[^*]+\*)'
    )

    pos = 0
    for match in token_pattern.finditer(text):
        start, end = match.span()
        if start > pos:
            plain_text = text[pos:start]
            run = paragraph.add_run(plain_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.font.color.rgb = RGBColor(0, 0, 0)
            if default_italic:
                run.italic = True

        badge_match = match.group(1)
        link_match = match.group(2)
        code_match = match.group(3)
        bold_italic_match = match.group(4)
        bold_match = match.group(5)
        italic_match = match.group(6)

        if badge_match:
            clean_badge = badge_match.strip('*')
            run = paragraph.add_run(clean_badge)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif link_match:
            m = re.match(r'\[([^\]]+)\]\((<[^>]+>|[^\)]+)\)', link_match)
            if m:
                link_text, _ = m.groups()
                run = paragraph.add_run(link_text)
                run.font.name = 'Times New Roman'
                run.font.size = Pt(base_font_size)
                run.font.color.rgb = RGBColor(0, 0, 0)
                if default_italic:
                    run.italic = True
            else:
                run = paragraph.add_run(link_match)
                run.font.name = 'Times New Roman'
                run.font.size = Pt(base_font_size)
                run.font.color.rgb = RGBColor(0, 0, 0)
        elif code_match:
            c_text = code_match[1:-1]
            run = paragraph.add_run(c_text)
            run.font.name = 'Consolas'
            run.font.size = Pt(base_font_size - 1)
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif bold_italic_match:
            bi_text = bold_italic_match[3:-3]
            run = paragraph.add_run(bi_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.bold = True
            run.italic = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif bold_match:
            b_text = bold_match[2:-2]
            run = paragraph.add_run(b_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            if default_italic:
                run.italic = True
        elif italic_match:
            i_text = italic_match[1:-1]
            run = paragraph.add_run(i_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(base_font_size)
            run.italic = True
            run.font.color.rgb = RGBColor(0, 0, 0)

        pos = end

    if pos < len(text):
        plain_text = text[pos:]
        run = paragraph.add_run(plain_text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(base_font_size)
        run.font.color.rgb = RGBColor(0, 0, 0)
        if default_italic:
            run.italic = True

def get_table_col_widths(headers, num_cols):
    """Return tailored column widths in inches summing to 6.5 inches (standard 1-inch margin on 8.5in or 8.27in)."""
    h_str = " ".join(headers).lower()
    if "claim" in h_str and "diễn tiến sau đó" in h_str:
        return [0.75, 2.10, 1.35, 2.30]
    elif "bài then chốt" in h_str:
        return [1.70, 1.90, 1.10, 1.80]
    elif "target" in h_str and "từ vựng" in h_str:
        return [0.75, 1.85, 2.05, 1.85]
    elif "nhãn áp suất" in h_str:
        return [0.85, 1.85, 1.70, 2.10]
    elif "nguồn" in h_str and "điều thực sự hỗ trợ" in h_str:
        return [1.85, 2.05, 2.60]
    elif "vấn đề" in h_str and "sai bước suy luận" in h_str:
        return [1.35, 2.45, 2.70]
    elif "giả thuyết" in h_str and "trạng thái" in h_str:
        return [0.80, 2.45, 1.65, 1.60]
    elif "id / pha" in h_str:
        return [1.05, 1.40, 1.25, 1.45, 1.35]
    elif "gap" in h_str and "điều còn thiếu" in h_str:
        return [0.80, 2.50, 3.20]
    elif "bản tổng hợp" in h_str:
        return [2.80, 3.70]
    
    total_width = 6.5
    w = total_width / num_cols
    return [w] * num_cols

def convert_markdown_file(md_path, docx_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    doc = docx.Document()

    # Format cơ bản nhất: khổ A4, lề chuẩn 1 inch (2.54 cm)
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

        # Không header
        section.header.is_linked_to_previous = False
        for p in section.header.paragraphs:
            p.text = ""

        # Không footer
        section.footer.is_linked_to_previous = False
        for p in section.footer.paragraphs:
            p.text = ""

    # Style Normal mặc định: Times New Roman, 12pt, màu đen
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].rstrip()
        
        # Dòng trống
        if not line:
            i += 1
            continue

        # Code block (```...) -> format cơ bản: thụt lề, font Consolas, không viền, không màu
        if line.startswith('```'):
            i += 1
            while i < n and not lines[i].startswith('```'):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.3)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.05
                run = p.add_run(lines[i])
                run.font.name = 'Consolas'
                run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(0, 0, 0)
                i += 1
            i += 1  # bỏ dòng ``` đóng
            # Thêm khoảng cách nhẹ sau code block
            sp = doc.add_paragraph()
            sp.paragraph_format.space_before = Pt(0)
            sp.paragraph_format.space_after = Pt(4)
            continue

        # Tiêu đề chính (# ...) -> không kẻ dòng, màu đen, bold
        if line.startswith('# '):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.keep_with_next = True
            
            title_text = line[2:].strip()
            run = p.add_run(title_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(16)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            i += 1
            continue

        # Tiêu đề mục cấp 1 (## ...) -> màu đen, bold, không kẻ dòng
        if line.startswith('## '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            h2_text = line[3:].strip()
            run = p.add_run(h2_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            i += 1
            continue

        # Tiêu đề mục cấp 2 (### ...) -> màu đen, bold
        if line.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            h3_text = line[4:].strip()
            run = p.add_run(h3_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            i += 1
            continue

        # Trích dẫn (> ...) -> format cơ bản: thụt lề, in nghiêng, không đóng hộp, không kẻ dòng
        if line.startswith('>'):
            quote_lines = []
            while i < n and (lines[i].startswith('>') or not lines[i].strip()):
                if lines[i].startswith('>'):
                    q_line = lines[i][1:].strip()
                    quote_lines.append(q_line)
                elif not lines[i].strip():
                    if i + 1 < n and lines[i+1].startswith('>'):
                        quote_lines.append('')
                    else:
                        break
                i += 1

            for ql in quote_lines:
                if not ql:
                    continue
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.4)
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.line_spacing = 1.15
                parse_inline_into_paragraph(p, ql, base_font_size=11.5, default_italic=True)
            continue

        # Bảng dữ liệu (| ... |) -> không kẻ dòng, không đánh màu bảng
        if line.startswith('|') and '|' in line[1:]:
            table_lines = []
            while i < n and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            
            rows_data = []
            for tline in table_lines:
                content_inner = tline.strip()
                if content_inner.startswith('|'):
                    content_inner = content_inner[1:]
                if content_inner.endswith('|'):
                    content_inner = content_inner[:-1]
                cols = [c.strip() for c in content_inner.split('|')]
                if all(re.match(r'^:?-+:?$', c) for c in cols):
                    continue
                rows_data.append(cols)

            if rows_data:
                num_rows = len(rows_data)
                num_cols = max(len(r) for r in rows_data)
                
                for r in rows_data:
                    while len(r) < num_cols:
                        r.append('')

                table = doc.add_table(rows=num_rows, cols=num_cols)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.autofit = False
                
                # Không kẻ dòng
                set_table_borders_none(table)

                tblPr = table._tbl.tblPr
                tblW = parse_xml(f'<w:tblW {nsdecls("w")} w:w="5000" w:type="pct"/>')
                tblPr.append(tblW)

                header_tr = table.rows[0]._tr.get_or_add_trPr()
                header_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
                for row in table.rows:
                    trPr = row._tr.get_or_add_trPr()
                    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

                # Độ rộng cột phù hợp để không chồng lấn nội dung
                col_widths = get_table_col_widths(rows_data[0], num_cols)
                col_widths_dxa = [int(w * 1440) for w in col_widths]

                tblGrid = table._tbl.tblGrid
                if tblGrid is not None:
                    tblGrid.clear()
                    for w_dxa in col_widths_dxa:
                        gridCol = parse_xml(f'<w:gridCol {nsdecls("w")} w:w="{w_dxa}"/>')
                        tblGrid.append(gridCol)

                for r_idx, row_content in enumerate(rows_data):
                    is_header = (r_idx == 0)
                    for c_idx, cell_value in enumerate(row_content):
                        cell = table.cell(r_idx, c_idx)
                        cell.width = Inches(col_widths[c_idx])
                        
                        tcPr = cell._tc.get_or_add_tcPr()
                        tcW = parse_xml(f'<w:tcW {nsdecls("w")} w:w="{col_widths_dxa[c_idx]}" w:type="dxa"/>')
                        tcPr.append(tcW)

                        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

                        cp = cell.paragraphs[0]
                        cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        cp.paragraph_format.space_before = Pt(2)
                        cp.paragraph_format.space_after = Pt(2)
                        cp.paragraph_format.line_spacing = 1.1

                        if is_header:
                            # Không đánh màu bảng: không shading, chỉ in đậm chữ đen
                            run = cp.add_run(cell_value)
                            run.font.name = 'Times New Roman'
                            run.font.size = Pt(10.5)
                            run.bold = True
                            run.font.color.rgb = RGBColor(0, 0, 0)
                        else:
                            # Dòng dữ liệu thường: chữ đen, không màu nền
                            parse_inline_into_paragraph(cp, cell_value, base_font_size=10.5)

                sp = doc.add_paragraph()
                sp.paragraph_format.space_before = Pt(0)
                sp.paragraph_format.space_after = Pt(6)
            continue

        # Bullet list item (- ...)
        if line.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            list_text = line[2:].strip()
            parse_inline_into_paragraph(p, list_text, base_font_size=12)
            i += 1
            continue

        # Numbered list item (1. ..., 2. ...)
        num_match = re.match(r'^(\d+)\.\s+(.*)$', line)
        if num_match:
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            list_text = num_match.group(2)
            parse_inline_into_paragraph(p, list_text, base_font_size=12)
            i += 1
            continue

        # Subtitle / metadata line at start
        if line.startswith('Ngày dựng lại:'):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(10)
            parse_inline_into_paragraph(p, line, base_font_size=11, default_italic=True)
            i += 1
            continue

        # Đoạn văn bản chuẩn (Standard Paragraph)
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        parse_inline_into_paragraph(p, line, base_font_size=12)
        i += 1

    doc.save(docx_path)
    print(f"Successfully converted {md_path} -> {docx_path} (basic format)")

if __name__ == '__main__':
    md_file = sys.argv[1] if len(sys.argv) > 1 else "docs/reports/MP1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.md"
    docx_file = sys.argv[2] if len(sys.argv) > 2 else "docs/reports/MP1_DECISION_HISTORY_AND_EVIDENCE_FOR_SUPERVISOR_VI.docx"
    convert_markdown_file(md_file, docx_file)
