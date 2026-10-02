import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_element(name):
    return OxmlElement(name)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="B0B0B0", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders_xml = f'''
    <w:tblBorders {nsdecls("w")}>
        <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:left w:val="none"/>
        <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:right w:val="none"/>
        <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:insideV w:val="none"/>
    </w:tblBorders>
    '''
    tblPr.append(parse_xml(borders_xml))

def set_cell_shading(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def add_page_number_to_footer(footer):
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Trang ")
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(128, 128, 128)
    
    fldSimple = OxmlElement('w:fldSimple')
    fldSimple.set(qn('w:instr'), 'PAGE')
    p._p.append(fldSimple)

def build_report():
    doc = docx.Document()
    
    # Page setup - A4: 8.27 x 11.69 inches, 1.0 inch margins
    # Printable width: 8.27 - 2.0 = 6.27 inches
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    # Add page number to footer
    add_page_number_to_footer(section.footer)
    
    # Helper to style body paragraphs: Times New Roman, 13 pt, line spacing 1.5, space after 6 pt, justified
    def add_p(text, bold=False, italic=False, space_after=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.line_spacing = line_spacing
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(13)
        run.bold = bold
        run.italic = italic
        return p

    # Headings: Times New Roman, 13 pt, Bold, line spacing 1.5, space after 6 pt
    def add_heading_1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(13)
        run.bold = True
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(13)
        run.bold = True
        return p

    # --- TITLE BLOCK ---
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.line_spacing = 1.5
    p_title.paragraph_format.space_after = Pt(6)
    
    run_t1 = p_title.add_run("BÁO CÁO TIẾN TRÌNH THU HẸP PHẠM VI NGHIÊN CỨU\n")
    run_t1.font.name = "Times New Roman"
    run_t1.font.size = Pt(13)
    run_t1.bold = True

    run_t2 = p_title.add_run("TỪ Ý TƯỞNG BAN ĐẦU ĐẾN CÂU HỎI NGHIÊN CỨU MP1\n")
    run_t2.font.name = "Times New Roman"
    run_t2.font.size = Pt(13)
    run_t2.bold = True

    run_t3 = p_title.add_run("(CƠ HỌC UỐN BÓ DÂY NiTi DƯỚI ÁP SUẤT GIAM GIỮ VÀ PHÂN BIỆT MÔ HÌNH H0b / H1)")
    run_t3.font.name = "Times New Roman"
    run_t3.font.size = Pt(13)
    run_t3.bold = True

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.line_spacing = 1.15
    p_meta.paragraph_format.space_after = Pt(18)
    run_meta = p_meta.add_run(
        "Báo cáo tiến trình rà soát y văn trình Cán bộ hướng dẫn (Mentor Progress Report) | Ngày: 26/09/2026\n"
        "Phương pháp luận: Rà soát đối kháng (Falsification-First) & Thu hẹp dựa trên bằng chứng (Evidence-Based)"
    )
    run_meta.font.name = "Times New Roman"
    run_meta.font.size = Pt(10.5)
    run_meta.font.color.rgb = RGBColor(100, 100, 100)

    # --- 1. MỤC TIÊU ---
    add_heading_1("1. MỤC TIÊU BÁO CÁO")
    add_p(
        "Báo cáo này trình bày có hệ thống tiến trình rà soát y văn đối kháng, phân rã kiến trúc phần cứng và thu hẹp phạm vi "
        "nghiên cứu của đề tài MP1, từ ý tưởng tổ hợp ban đầu do cán bộ hướng dẫn (mentor) đề xuất đến câu hỏi nghiên cứu cơ học "
        "cốt lõi có thể kiểm chứng và bác bỏ (falsifiable) ở thời điểm hiện tại. Báo cáo không phải là một bài tổng quan y văn "
        "(literature review) diện rộng, không phải một hồ sơ thiết kế thí nghiệm chi tiết, và không diễn giải quy trình làm việc nội bộ. "
        "Trọng tâm duy nhất của báo cáo là trả lời chuỗi logic khoa học: Tôi đã làm gì? Sau bước đó rút ra kết luận gì? Tại sao có thể "
        "kết luận như vậy dựa trên bằng chứng công bố nào? Nhóm bài báo đó được định vị qua từ khóa tìm kiếm (search keywords) nào? "
        "Phạm vi nghiên cứu bị thu hẹp ra sao và checkpoint tiếp theo là gì?"
    )
    add_p(
        "Toàn bộ phân tích tuân thủ nghiêm ngặt nguyên tắc cốt lõi của repository: Không bảo vệ ý tưởng bằng suy diễn định tính mà "
        "chủ động tìm kiếm các công trình đi trước gần nhất để kiểm chứng và phản bác (falsification-first). Các tuyên bố tính mới ở cấp độ "
        "ghép nối thiết bị thuần túy bị loại bỏ dứt điểm khi phát hiện prior art tương đương. Mọi dữ liệu trích dẫn và kết luận cơ học trong "
        "báo cáo đều được truy xuất trực tiếp từ các bằng chứng đã bóc tách, kiểm chứng toàn văn (verified full-text) và đối soát độc lập trong repository."
    )

    # --- 2. STARTING POINT ---
    add_heading_1("2. ĐIỂM KHỞI ĐẦU: Ý TƯỞNG BAN ĐẦU CỦA MENTOR")
    add_p(
        "Ý tưởng nghiên cứu ban đầu được mentor đề xuất bao gồm một tổ hợp đa thành phần cấp độ thiết bị: (1) Bó dây hợp kim ghi nhớ "
        "hình dạng (SMA) / NiTi siêu đàn hồi hoặc dây kim loại; (2) Cơ cấu giam giữ bằng áp suất dương (positive-pressure confinement); "
        "(3) Hiện tượng kẹt ma sát trượt giữa các sợi dây (inter-wire frictional jamming) để điều biến độ cứng uốn thích ứng (variable bending stiffness); "
        "và (4) Tùy chọn tích hợp nguồn tạo áp suất nhỏ gọn trên thân robot dẫn động bằng dây SMA hoặc cơ cấu piston/xi lanh thu nhỏ."
    )
    add_p(
        "Đánh giá khoa học tại thời điểm bắt đầu cho thấy: Ý tưởng này hoàn toàn là một tổ hợp phần cứng (component combination / device-level architecture). "
        "Ở quy mô này, đề tài quá rộng và tiềm ẩn rủi ro nghiêm trọng về tính mới khoa học: Việc kết hợp các thành phần sẵn có vào một robot mềm "
        "có thể chỉ là một sự thay thế kỹ thuật thông thường (engineering/actuator substitution) mà không tạo ra bất kỳ đóng góp mới nào về mặt "
        "nguyên lý cơ học hay mô hình hóa. Nếu không phân rã kiến trúc và rà soát prior art nghiêm ngặt, nghiên cứu sẽ đối mặt với nguy cơ bị "
        "bác bỏ hoàn toàn khi công bố vì các thành phần riêng lẻ hoặc các tổ hợp tương đương đã được giải quyết từ trước."
    )

    # --- 3. TIMELINE THU HẸP PHẠM VI NGHIÊN CỨU ---
    add_heading_1("3. TIẾN TRÌNH THU HẸP PHẠM VI NGHIÊN CỨU (TIMELINE & CHECKPOINTS)")
    add_p(
        "Quá trình thu hẹp được thực hiện qua chuỗi 9 checkpoint tuần tự, phân định rõ giữa truy vấn lịch sử thực tế (EXACT QUERY / PROTOCOL EXPORTS) "
        "và từ khóa kỹ thuật tái dựng từ ý định tìm kiếm (RECONSTRUCTED KEYWORDS), bảo đảm mọi kết luận đều truy nguyên được bằng chứng cụ thể:"
    )

    # Table 1: Timeline
    table1 = doc.add_table(rows=1, cols=6)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table1)

    t1_headers = [
        "Checkpoint",
        "Tôi đã làm gì?",
        "Từ khóa tìm kiếm (Search Keywords)",
        "Tài liệu & Bằng chứng chính",
        "Tôi rút ra gì & Tại sao?",
        "Phạm vi bị thu hẹp & Kết quả"
    ]
    # Sum of widths: 0.70 + 1.10 + 1.10 + 1.10 + 1.27 + 1.00 = 6.27 inches
    t1_widths = [Inches(0.70), Inches(1.10), Inches(1.10), Inches(1.10), Inches(1.27), Inches(1.00)]
    t1_hdr_cells = table1.rows[0].cells
    hdr_tr = table1.rows[0]._tr.get_or_add_trPr()
    hdr_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    hdr_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for idx, heading in enumerate(t1_headers):
        t1_hdr_cells[idx].width = t1_widths[idx]
        p = t1_hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(heading)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = True
        set_cell_shading(t1_hdr_cells[idx], "F0F0F0")
        set_cell_margins(t1_hdr_cells[idx], top=80, bottom=80, left=80, right=80)

    checkpoint_data = [
        (
            "CP 0\nÝ tưởng Mentor",
            "Tiếp nhận và lập hồ sơ ý tưởng tổ hợp phần cứng ban đầu của mentor.",
            "RECONSTRUCTED KEYWORDS:\n\"variable stiffness soft robot\" \"jamming transition mechanism\"",
            "Tổng quan chung robot mềm và biến đổi độ cứng.",
            "Ý tưởng ở dạng tổ hợp phần cứng quá rộng, không chứa câu hỏi cơ học cụ thể và không thể bác bỏ (unfalsifiable).",
            "Loại bỏ việc chế tạo thử nghiệm ngay. Yêu cầu phân rã thành các claim độc lập."
        ),
        (
            "CP 1\nPhân rã kiến trúc",
            "Phân rã kiến trúc thiết bị thành 8 claim độc lập C1–C8 để kiểm chứng đối kháng.",
            "RECONSTRUCTED KEYWORDS:\n\"wire jamming variable stiffness\" \"positive pressure jamming\" \"SMA jamming robot\"",
            "outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json",
            "Cần cô lập từng thành phần phần cứng và nguyên lý hoạt động để kiểm tra khả năng bị pre-empt riêng rẽ.",
            "Tách bạch ranh giới giữa tính mới cấp thiết bị (device-level) và tính mới cơ học (mechanics-level)."
        ),
        (
            "CP 2\nĐối soát broad prior art",
            "Đối soát y văn về kẹt dây, kẹt áp suất dương, tổ hợp SMA + jamming và nguồn áp suất nhỏ gọn.",
            "RECONSTRUCTED KEYWORDS:\n\"wire jamming\" \"fiber jamming\" \"positive pressure jamming\" \"SMA jamming\"",
            "Bai et al. (2022)\nZhang & Yao (2026)\nLiu et al. (2021)\nTakashima et al. (2022)\nMatsumoto et al. (2024)\nHuynh et al. (2022)\nWang et al. (2024)\nPierce & Mascaro (2013)",
            "C1, C2, C3, C4, C8 đã hoàn toàn có prior art trực tiếp:\n- Kẹt dây: Bai (2022), Zhang & Yao (2026);\n- Áp suất dương: Liu (2021), Zhang & Yao (2026);\n- SMA + jamming: Takashima (2022), Matsumoto (2024);\n- Bơm vi mô/piston: Huynh (2022), Wang (2024), Pierce & Mascaro (2013).",
            "LOẠI BỎ TOÀN BỘ TÍNH MỚI CẤP THIẾT BỊ (C1–C4, C8). Ban hành quyết định bước ngoặt: PIVOT TO MECHANICS CORE."
        ),
        (
            "CP 3\nPivot sang cơ học cốt lõi",
            "Chuyển toàn bộ trọng tâm MP1 sang bài toán cơ học tiếp xúc và uốn của bó dây NiTi.",
            "RECONSTRUCTED KEYWORDS:\n\"superelastic wire bundle bending\" \"NiTi cable friction\" \"confined wire stiffness\"",
            "docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md\n(Thiết lập 3 target T1, T2, T3)",
            "Chỉ có thể tạo đóng góp khoa học nếu chứng minh được tương tác giữa siêu đàn hồi NiTi, trượt ma sát và áp suất tạo ra hiện tượng cơ học chưa có lời giải.",
            "Thu hẹp phạm vi vào bó dây NiTi chịu uốn dưới áp suất giam giữ (C5–C7 / T1–T3). Khởi động vòng MP1-V002."
        ),
        (
            "CP 4\nMa sát tiếp xúc NiTi",
            "Rà soát y văn toàn văn về cáp và bó dây NiTi nhiều sợi chịu kéo, uốn và trượt ma sát.",
            "RECONSTRUCTED KEYWORDS:\n\"NiTi cable interwire friction\" \"superelastic wire rope contact\" \"Nitinol strand hysteresis\"",
            "Carboni et al. (2015)\nCarboni & Lacarbonara (2016)\nReedlunn et al. (2013)\nFang et al. (2019)\nVahidi et al. (2021)",
            "T1 ĐÃ ĐÓNG: Ma sát giữa các sợi NiTi và vòng trễ pinched hysteresis là hiện tượng đã biết rõ (Carboni 2015, 2016; Reedlunn 2013; Fang 2019). Mô hình FEA tiếp xúc Coulomb 3D đã tồn tại (Vahidi 2021).",
            "Loại bỏ tính mới về sự tồn tại của ma sát giữa các sợi NiTi (C5/T1). Chuyển thành dữ liệu đầu vào cơ sở cho mô hình đối thủ H0b."
        ),
        (
            "CP 5\nCơ học uốn & Áp suất",
            "Rà soát cơ học uốn cáp, trượt stick-slip cục bộ và tác động của áp suất giam giữ hướng kính.",
            "RECONSTRUCTED KEYWORDS:\n\"cable bending stick slip\" \"radial pressure cable bending\" \"wire rope flexural rigidity\"",
            "Tjahjanto et al. (2017)\nBarsi et al. (2025)\nXin Liu (2004)",
            "T2 BỊ THU HẸP: Áp suất giam giữ ngoài chỉ là điều kiện biên lực mặt sigma.n = -p(t)n trong cơ học tiếp xúc (Tjahjanto 2017). Áp suất buồng p không bằng lực pháp tuyến fn. Barsi (2025) cung cấp biên độ cứng uốn nhưng không giải tiếp xúc dính-trượt phụ thuộc áp suất.",
            "Hạ cấp áp suất dương P3 từ 'nguyên lý cơ học mới' thành điều kiện biên thực nghiệm p(t). Loại bỏ nguy cơ phóng đại tính mới của áp suất."
        ),
        (
            "CP 6\nTái cấu trúc H0a / H0b / H1",
            "Thiết lập bài toán kiểm chứng giả thuyết 3 tầng nhằm phân định mô hình cơ sở, mô hình nâng cao và giả thuyết mới.",
            "RECONSTRUCTED KEYWORDS:\n\"superelastic constitutive model contact friction\" \"NiTi wire rope finite element model\"",
            "Reedlunn et al. (2013)\nFang et al. (2019)\nVahidi et al. (2021)\nKang et al. (2020)",
            "H0a (mô đun E hằng số) bị bác bỏ khi chuyển pha siêu đàn hồi (Reedlunn 2013, Fang 2019). Tuy nhiên, H0a sai KHÔNG chứng minh H1 đúng! H0b (mô hình Souza/Auricchio + tiếp xúc Coulomb) vẫn là đối thủ cạnh tranh trực tiếp chưa bị đánh bại (Vahidi 2021).",
            "Chuyển toàn bộ nghiên cứu thành bài toán phân biệt mô hình (Model Discrimination): H0b có dự đoán được uốn phụ thuộc áp suất hay không?"
        ),
        (
            "CP 7\nĐóng citation protocol",
            "Thực hiện truy vết trích dẫn hai chiều 15 hướng, rà soát 187 hồ sơ y văn và 16 bài toàn văn.",
            "EXACT QUERY / EXPORTS:\nScopus/Publisher:\nF01 (Bai 2022, 14)\nF02 (Liu 2021, 51)\nF03 (Zhang 2026, 0)\nF04 (Takashima, 10)\nF05 (Matsumoto, 1)\nB03 (Xin Liu 2004, 4)\nB04 (Tjahjanto, 9)\nB06 (Silva, 22)\nB11 (Kang 2020, 22)\nB12 (Barsi 2025, 46)",
            "outputs/verification/MP1-V002/citation_coverage.json\nFINAL_ADJUDICATION.json",
            "Đóng giao thức trích dẫn (15/15 hướng: backward 9/9, forward 6/6). Không phát hiện bài báo nào trực tiếp giải quyết uốn bó dây NiTi dưới áp suất giam giữ chủ động. Đây là kết quả đóng theo giao thức, không phải chứng minh tính mới phổ quát.",
            "Khóa chặt MP1 trong ranh giới mô hình phân biệt uốn. Loại bỏ mọi kỳ vọng về một phát hiện vật lý phổ quát chưa từng có."
        ),
        (
            "CP 8\nKhóa RQ sống sót cuối cùng",
            "Tổng hợp kết quả V001, V002 và W02 để phát biểu câu hỏi nghiên cứu trung tính, có thể bác bỏ.",
            "RECONSTRUCTED KEYWORDS:\n\"model discrimination NiTi bundle pressure bending\" \"held-out validation superelastic contact\"",
            "outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json\nFINAL_ADJUDICATION.md",
            "MP1 sống sót như một bài toán phân biệt mô hình có điều kiện (conditional candidate) bị chặn bởi 8 khoảng trống khoa học (nhận dạng cơ chế, quan hệ p -> fn, miền cùng tồn tại trượt - chuyển pha).",
            "Khóa Research Question ở dạng đối sánh mô hình H0b đã khóa tham số với H1. MP1 là phương án dự phòng khả thi (viable alternative)."
        )
    ]

    for row_data in checkpoint_data:
        row = table1.add_row()
        row_tr = row._tr.get_or_add_trPr()
        row_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        row_cells = row.cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = t1_widths[col_idx]
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.0)
            if col_idx == 0:
                run.bold = True
            set_cell_margins(row_cells[col_idx], top=60, bottom=60, left=70, right=70)

    # --- 4. NHỮNG CLAIM ĐÃ BỊ LOẠI BỎ ---
    add_heading_1("4. ĐỐI SOÁT CÁC TUYÊN BỐ ĐÃ BỊ LOẠI BỎ (REJECTED BROAD CLAIMS)")
    add_p(
        "Quá trình kiểm chứng đối kháng đã bóc tách và loại bỏ dứt điểm các tuyên bố tính mới cấp độ thiết bị ban đầu nhằm bảo vệ "
        "tính liêm chính học thuật của đề tài. Bảng dưới đây đối soát cụ thể từng tuyên bố bị bác bỏ cùng bằng chứng y văn tương ứng:"
    )

    table2 = doc.add_table(rows=1, cols=4)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table2)

    # Sum of widths: 1.40 + 1.70 + 1.70 + 1.47 = 6.27 inches
    t2_widths = [Inches(1.40), Inches(1.70), Inches(1.70), Inches(1.47)]
    t2_headers = ["Tuyên bố cấp thiết bị ban đầu", "Bằng chứng phản bác (Prior Art)", "Kết luận & Lý do bác bỏ", "Phạm vi thay thế hợp lệ"]
    t2_hdr_cells = table2.rows[0].cells
    hdr2_tr = table2.rows[0]._tr.get_or_add_trPr()
    hdr2_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    hdr2_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for idx, heading in enumerate(t2_headers):
        t2_hdr_cells[idx].width = t2_widths[idx]
        p = t2_hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(heading)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = True
        set_cell_shading(t2_hdr_cells[idx], "F0F0F0")
        set_cell_margins(t2_hdr_cells[idx], top=80, bottom=80, left=80, right=80)

    rejected_claims_data = [
        (
            "C1: Kẹt sợi/dây kim loại tạo biến đổi độ cứng là một nguyên lý mới.",
            "Bai et al. (2022) chế tạo robot kẹt dây ma sát thay đổi độ cứng uốn. Zhang & Yao (2026) chế tạo chuỗi kẹt sợi dưới áp suất thay đổi độ cứng uốn rõ rệt.",
            "BỊ LOẠI BỎ (CLOSED). Nguyên lý biến đổi độ cứng bằng kẹt sợi và dây kim loại đã có tiền lệ thực nghiệm vững chắc trong y văn.",
            "Chuyển sang khảo sát bản chất tiếp xúc và trượt ma sát phi tuyến của hợp kim siêu đàn hồi NiTi."
        ),
        (
            "C2: Cơ chế kẹt bằng áp suất dương là một nguyên lý vật lý mới.",
            "Liu et al. (2021) chứng minh cấu trúc kẹt áp suất dương đến 200 kPa cho robot đeo. Zhang & Yao (2026) kẹt sợi bằng áp suất dương đến 300 kPa.",
            "BỊ LOẠI BỎ (CLOSED). Áp suất dương là phương pháp kích hoạt khí nén thông dụng, không tạo ra nguyên lý cơ học mới.",
            "Quy định áp suất giam giữ là điều kiện biên lực mặt p(t) tác động lên vỏ ngoài của bó dây."
        ),
        (
            "C3: Tích hợp hợp kim nhớ hình (SMA) và cơ chế jamming trong cùng thiết bị là tính mới.",
            "Takashima et al. (2022) chế tạo khớp biến đổi độ cứng kết hợp dây SMA và jamming. Matsumoto et al. (2024) nghiên cứu biến dạng pha R của dây Ti-Ni trong cơ cấu kẹt.",
            "BỊ LOẠI BỎ (CLOSED). Việc bố trí dây SMA cùng với cấu trúc kẹt hạt/dây là ý tưởng đã được công bố nhiều lần.",
            "Chỉ khảo sát khi các dây NiTi tự thân đóng vai trò là môi trường tiếp xúc ma sát và chịu tải uốn kết cấu."
        ),
        (
            "C4: Tích hợp nguồn tạo áp suất nhỏ gọn trên thân robot kẹt là đóng góp khoa học mới.",
            "Huynh et al. (2022) tích hợp bơm vi mô điện động lỏng kích hoạt jamming. Wang et al. (2024) tích hợp piston trục vít thu nhỏ nén hạt kẹt trong tay máy robot mềm.",
            "BỊ LOẠI BỎ (CLOSED). Tích hợp bơm hoặc cơ cấu nén nhỏ gọn là giải pháp đóng gói cơ điện tử, không phải đóng góp cơ học kết cấu.",
            "Loại bỏ hoàn toàn yêu cầu chế tạo bơm nhỏ gọn ra khỏi đóng góp khoa học cốt lõi của đề tài."
        ),
        (
            "C5: Bản thân dây NiTi làm môi trường ma sát trượt là một cơ chế chưa từng biết.",
            "Carboni et al. (2015) và Carboni & Lacarbonara (2016) đo đạc ma sát và trễ giữa các sợi cáp Nitinol. Reedlunn et al. (2013) nghiên cứu tiếp xúc và ma sát tĩnh trong cáp NiTi.",
            "BỊ LOẠI BỎ (CLOSED). Hiện tượng ma sát trượt và tiêu tán năng lượng giữa các sợi NiTi đã được nghiên cứu sâu trong cơ học cáp.",
            "Không claim hiện tượng ma sát NiTi là mới; sử dụng định luật ma sát Coulomb làm giả thuyết cơ sở H0b."
        ),
        (
            "C8: Dùng cơ cấu piston/xi lanh SMA để cấp áp suất cho cơ cấu kẹt là tính mới.",
            "Pierce & Mascaro (2013) đã phát triển bơm piston dẫn động bằng dây SMA. Wang et al. (2024) đã dùng piston nén trực tiếp môi trường kẹt.",
            "BỊ LOẠI BỎ (PRE-EMPTED). Dùng SMA kéo piston tạo áp suất chỉ là sự thay thế cơ cấu chấp hành (actuator substitution).",
            "Tách cơ cấu cấp áp suất thành thiết bị phụ trợ phòng thí nghiệm, không đưa vào tuyên bố tính mới của luận văn."
        )
    ]

    for row_data in rejected_claims_data:
        row = table2.add_row()
        row_tr = row._tr.get_or_add_trPr()
        row_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        row_cells = row.cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = t2_widths[col_idx]
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.5)
            if col_idx == 0:
                run.bold = True
            set_cell_margins(row_cells[col_idx], top=60, bottom=60, left=80, right=80)

    # --- 5. PHẦN "5 WHY" ---
    add_heading_1("5. BẢN ĐỒ LÝ DO THU HẸP (5 WHY ANALYSIS)")
    add_p(
        "Chuỗi 5 câu hỏi 'Tại sao' dưới đây cô đọng bản chất lập luận đã dẫn dắt toàn bộ tiến trình thu hẹp, từ một ý tưởng thiết bị "
        "rộng đến câu hỏi phân biệt mô hình chính xác hiện tại:"
    )

    table3 = doc.add_table(rows=1, cols=5)
    table3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table3)

    # Sum of widths: 0.70 + 1.50 + 1.50 + 1.37 + 1.20 = 6.27 inches
    t3_widths = [Inches(0.70), Inches(1.50), Inches(1.50), Inches(1.37), Inches(1.20)]
    t3_headers = ["Mức độ", "Câu hỏi Tại sao (Why?)", "Câu trả lời bản chất (Answer)", "Bằng chứng y văn xác thực", "Hệ quả thu hẹp phạm vi"]
    t3_hdr_cells = table3.rows[0].cells
    hdr3_tr = table3.rows[0]._tr.get_or_add_trPr()
    hdr3_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    hdr3_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for idx, heading in enumerate(t3_headers):
        t3_hdr_cells[idx].width = t3_widths[idx]
        p = t3_hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(heading)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = True
        set_cell_shading(t3_hdr_cells[idx], "F0F0F0")
        set_cell_margins(t3_hdr_cells[idx], top=80, bottom=80, left=80, right=80)

    why_data = [
        (
            "Why 1",
            "Tại sao không thể giữ 'Robot biến đổi độ cứng bằng kẹt dây NiTi' làm đóng góp khoa học chính?",
            "Vì các nguyên lý kẹt dây/sợi tạo biến đổi độ cứng và tích hợp SMA với cơ cấu kẹt đều đã được công bố từ trước.",
            "Bai et al. (2022); Zhang & Yao (2026); Takashima et al. (2022).",
            "Loại bỏ tính mới cấp độ thiết bị và tổ hợp phần cứng."
        ),
        (
            "Why 2",
            "Tại sao phải chuyển dịch trọng tâm sang bản chất cơ học?",
            "Vì việc kết hợp các linh kiện đã biết (dây kim loại + vỏ bọc khí nén + bơm thu nhỏ) chỉ là bài toán gia công tích hợp kỹ thuật, không trả lời một câu hỏi khoa học mới.",
            "Huynh et al. (2022); Wang et al. (2024); Pierce & Mascaro (2013).",
            "Pivot hoàn toàn từ bài toán chế tạo robot sang bài toán cơ học kết cấu (Mechanics Core)."
        ),
        (
            "Why 3",
            "Tại sao không thể coi ma sát trượt và tiêu tán năng lượng trong bó dây NiTi là một cơ chế mới?",
            "Vì cơ học tiếp xúc ma sát, trượt tương đối và tổn hao trễ (pinched hysteresis) của tao cáp NiTi đã được nghiên cứu kỹ lưỡng trong cơ học kết cấu.",
            "Carboni et al. (2015); Carboni & Lacarbonara (2016); Reedlunn et al. (2013); Vahidi et al. (2021).",
            "Không claim hiện tượng ma sát NiTi là mới; chuyển thành dữ liệu đầu vào cơ sở cho mô hình H0b."
        ),
        (
            "Why 4",
            "Tại sao áp suất dương chủ động không tạo ra một nguyên lý vật lý mới?",
            "Vì trong cơ học môi trường liên tục, áp suất giam giữ bên ngoài thuần túy là một điều kiện biên lực mặt sigma.n = -p(t)n. Hơn nữa, áp suất buồng khí p không trực tiếp đồng nhất với lực pháp tuyến fn giữa các sợi.",
            "Tjahjanto et al. (2017); Barsi et al. (2025); Xin Liu (2004).",
            "Hạ cấp áp suất dương P3 thành điều kiện biên tải trọng ngoài p(t) dùng trong giao thức điều khiển thực nghiệm."
        ),
        (
            "Why 5",
            "Vậy bài toán khoa học duy nhất còn lại chưa có lời giải là gì?",
            "Liệu một mô hình kết hợp giữa định luật cấu thành NiTi hiện hữu và cơ học tiếp xúc Coulomb (H0b), khi được hiệu chuẩn độc lập và khóa tham số, có dự đoán được hành vi uốn phụ thuộc áp suất hay bắt buộc phải có định luật ghép cặp mới (H1)?",
            "Vahidi et al. (2021); Kang et al. (2020); Reedlunn et al. (2013); Fang et al. (2019).",
            "Khóa câu hỏi nghiên cứu ở dạng Model Discrimination giữa H0b đã khóa tham số và H1."
        )
    ]

    for row_data in why_data:
        row = table3.add_row()
        row_tr = row._tr.get_or_add_trPr()
        row_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        row_cells = row.cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = t3_widths[col_idx]
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.5)
            if col_idx == 0:
                run.bold = True
            set_cell_margins(row_cells[col_idx], top=60, bottom=60, left=80, right=80)

    # --- 6. TOPIC -> RESEARCH QUESTION ---
    add_heading_1("6. DIỄN TIẾN TỪ CHỦ ĐỀ ĐẾN CÂU HỎI NGHIÊN CỨU")
    add_p(
        "Bảng dưới đây tóm tắt các phiên bản tiến hóa của đề tài qua từng vòng rà soát, chỉ rõ lý do phiên bản trước không đạt yêu cầu "
        "và cơ sở bằng chứng dẫn dắt việc chuyển dịch sang phiên bản tiếp theo:"
    )

    table4 = doc.add_table(rows=1, cols=5)
    table4.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table4)

    # Sum of widths: 0.80 + 1.50 + 1.47 + 1.30 + 1.20 = 6.27 inches
    t4_widths = [Inches(0.80), Inches(1.50), Inches(1.47), Inches(1.30), Inches(1.20)]
    t4_headers = ["Phiên bản", "Phát biểu chủ đề / Đề tài", "Lý do không đạt yêu cầu", "Bằng chứng y văn dẫn dắt", "Phiên bản tiếp theo"]
    t4_hdr_cells = table4.rows[0].cells
    hdr4_tr = table4.rows[0]._tr.get_or_add_trPr()
    hdr4_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    hdr4_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for idx, heading in enumerate(t4_headers):
        t4_hdr_cells[idx].width = t4_widths[idx]
        p = t4_hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(heading)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = True
        set_cell_shading(t4_hdr_cells[idx], "F0F0F0")
        set_cell_margins(t4_hdr_cells[idx], top=80, bottom=80, left=80, right=80)

    version_data = [
        (
            "V0\n(Gốc)",
            "Robot mềm biến đổi độ cứng bằng cơ chế kẹt dây NiTi dưới áp suất dương.",
            "Tổ hợp phần cứng cấp thiết bị; các thành phần riêng rẽ đều đã có prior art trực tiếp.",
            "Bai et al. (2022)\nLiu et al. (2021)\nTakashima et al. (2022)",
            "V1: Chuyển dịch sang cơ học bó dây dưới áp suất giam giữ."
        ),
        (
            "V1\n(Cơ học)",
            "Cơ học biến dạng và kẹt ma sát của bó dây NiTi dưới áp suất giam giữ.",
            "Vẫn quá rộng; hiện tượng ma sát dây NiTi và giam giữ áp suất đều đã có tiền lệ trong cơ học cáp.",
            "Carboni et al. (2015)\nReedlunn et al. (2013)\nTjahjanto et al. (2017)",
            "V2: Thu hẹp vào cơ học uốn và kiểm soát độ cứng uốn."
        ),
        (
            "V2\n(Cơ học uốn)",
            "Cơ học uốn và chuyển tiếp dính-trượt của bó dây NiTi dưới áp suất giam giữ chủ động.",
            "Áp suất giam giữ chỉ là điều kiện biên lực mặt p(t); chưa làm rõ bản chất phi tuyến do chuyển pha siêu đàn hồi.",
            "Tjahjanto et al. (2017)\nBarsi et al. (2025)\nXin Liu (2004)",
            "V3: Tích hợp hiện tượng chuyển pha siêu đàn hồi với trượt ma sát."
        ),
        (
            "V3\n(Ghép cặp)",
            "Tương tác ghép cặp giữa chuyển pha siêu đàn hồi NiTi, trượt ma sát Coulomb và áp suất giam giữ.",
            "Mô hình thay thế đàn hồi đơn giản H0a thất bại, nhưng mô hình chuyển pha hiện hữu H0b chưa hề bị bác bỏ.",
            "Reedlunn et al. (2013)\nFang et al. (2019)\nVahidi et al. (2021)",
            "V4: Khóa bài toán phân biệt mô hình (Model Discrimination)."
        ),
        (
            "V4\n(Hiện tại)",
            "Đánh giá năng lực dự đoán của mô hình cấu thành NiTi hiện hữu kết hợp tiếp xúc Coulomb (H0b) đối với đáp ứng uốn phụ thuộc áp suất của bó dây NiTi.",
            "HOÀN TOÀN ĐẠT YÊU CẦU: Câu hỏi khoa học cụ thể, trung tính, có thể bác bỏ, không giả định trước tính mới.",
            "outputs/execution/MP1-V002/W2/MP1_W02_FINAL_STATE.json\nFINAL_ADJUDICATION.json",
            "Khóa làm đề tài MP1 chính thức (phương án dự phòng khả thi)."
        )
    ]

    for row_data in version_data:
        row = table4.add_row()
        row_tr = row._tr.get_or_add_trPr()
        row_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        row_cells = row.cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = t4_widths[col_idx]
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.5)
            if col_idx == 0:
                run.bold = True
            set_cell_margins(row_cells[col_idx], top=60, bottom=60, left=80, right=80)

    # --- 7. H0a / H0b / H1 ---
    add_heading_1("7. CẤU TRÚC BA TẦNG GIẢ THUYẾT: H0a / H0b / H1")
    add_p(
        "Để đảm bảo tính chặt chẽ về phương pháp luận và ngăn ngừa ngụy biện khẳng định hệ quả (fallacy of affirming the consequent), "
        "không gian giả thuyết của MP1 được cấu trúc thành ba tầng riêng biệt:"
    )
    add_p(
        "• Giả thuyết H0a (Mô hình thay thế đàn hồi đơn giản - Naive Elastic Substitution): Dự đoán đáp ứng uốn của bó dây bằng cách "
        "thay thế mô đun đàn hồi hiệu dụng hằng số (E = const) vào các phương trình bó cáp thông thường. "
        "Trạng thái: BỊ BÁC BỎ DỨT ĐIỂM TRONG MIỀN CHUYỂN PHA (REFUTED_IN_TRANSFORMATION_REGIME). Bằng chứng thực nghiệm của "
        "Reedlunn et al. (2013) và Fang et al. (2019) chứng minh rằng khi ứng suất cục bộ vượt ngưỡng chuyển pha Martensite, "
        "đáp ứng cơ học biến thiên phi tuyến mạnh mẽ và giả định mô đun hằng số hoàn toàn sụp đổ."
    )
    add_p(
        "• Giả thuyết H0b (Mô hình cấu thành NiTi hiện hữu kết hợp tiếp xúc Coulomb - Transformation-Aware NiTi + Coulomb Contact): "
        "Sử dụng các mô hình cấu thành cơ học nhiệt động học hiện hữu của NiTi (như mô hình Souza et al. hoặc Auricchio et al.) kết hợp với "
        "định luật ma sát tiếp xúc Coulomb bề mặt tiêu chuẩn dưới điều kiện biên lực mặt p(t) tác động từ màng bọc. "
        "Trạng thái: CHƯA BỊ BÁC BỎ / ĐỐI THỦ CẠNH TRANH TRỰC TIẾP (NOT_FALSIFIED / LIVE COMPETITOR). Vahidi et al. (2021) đã chứng minh "
        "rằng mô hình phần tử hữu hạn 3D sử dụng UMAT Souza kết hợp tiếp xúc ma sát phạt trong Abaqus tái hiện được đáp ứng phi tuyến phức tạp "
        "của cáp NiTi nhiều sợi mà không cần viện dẫn thêm bất kỳ định luật vi mô mới nào. Cho đến nay, chưa có bằng chứng thực nghiệm nào "
        "chứng minh mô hình H0b thất bại trong việc dự đoán hành vi uốn phụ thuộc áp suất khi được hiệu chuẩn độc lập."
    )
    add_p(
        "• Giả thuyết H1 (Định luật ghép cặp vi mô mới - Novel Constitutive-Contact Coupling): Cho rằng tồn tại một cơ chế ghép cặp "
        "trực tiếp chưa từng biết giữa động học chuyển pha tinh thể NiTi và hiện tượng trượt ma sát giao diện giữa các sợi dưới áp suất giam giữ, "
        "đòi hỏi phải xây dựng một phương trình cấu thành - tiếp xúc hoàn toàn mới. "
        "Trạng thái: CHƯA CÓ ĐỦ BẰNG CHỨNG (INSUFFICIENT_EVIDENCE)."
    )
    add_p(
        "QUY TẮC LOGIC CỐT LÕI (BẮT BUỘC): Việc giả thuyết H0a bị bác bỏ KHÔNG ĐỒNG NGHĨA với việc giả thuyết H1 được chứng minh. "
        "Sự thất bại của mô hình đàn hồi hằng số H0a chỉ khẳng định rằng cần phải tính đến hiện tượng chuyển pha siêu đàn hồi của vật liệu; "
        "nó hoàn toàn không chứng minh rằng các mô hình cấu thành NiTi phi tuyến hiện hữu (H0b) là không đủ. Đây chính là lý do khoa học tối thượng "
        "buộc câu hỏi nghiên cứu của MP1 phải chuyển dịch từ một tuyên bố tính mới sang một bài toán phân biệt mô hình (model discrimination): "
        "Kiểm chứng xem mô hình H0b đã khóa tham số có đủ năng lực dự đoán hay không trước khi được phép khẳng định sự cần thiết của H1."
    )

    # --- 8. FINAL RESEARCH QUESTION ---
    add_heading_1("8. CÂU HỎI NGHIÊN CỨU CUỐI CÙNG (FINAL RESEARCH QUESTION)")
    add_p(
        "Dựa trên toàn bộ kết quả rà soát đối kháng và cấu trúc giả thuyết đã được xác lập, câu hỏi nghiên cứu khoa học chính thức của "
        "hướng đề tài MP1 được phát biểu chuẩn xác, trung tính, không chứa định kiến hay suy diễn thiên vị tính mới như sau:"
    )
    add_p(
        "English Formulation:\n"
        "\"Across a declared, experimentally accessible range of positive confinement pressure, curvature, and temperature where both "
        "inter-wire slip and stress-induced Martensitic transformation coexist, does an established transformation-aware NiTi constitutive "
        "and Coulomb-contact model (H0b) under locked parameter calibration adequately predict the pressure-dependent moment-curvature response, "
        "tangent bending stiffness, hysteresis loops, and local slip/transformation observables of a superelastic NiTi wire bundle, or does model "
        "failure under held-out conditions demonstrate the necessity of a novel constitutive-contact coupling law (H1)?\"",
        italic=True
    )
    add_p(
        "Phát biểu tiếng Việt:\n"
        "\"Trong một miền áp suất giam giữ dương, độ cong uốn và nhiệt độ được xác định trước và có thể tiếp cận được về mặt thực nghiệm—nơi mà "
        "hiện tượng trượt tương đối giữa các sợi và chuyển pha Martensite cảm ứng do ứng suất đồng thời cùng tồn tại—liệu một mô hình kết hợp "
        "giữa định luật cấu thành NiTi có xét chuyển pha hiện hữu và mô hình tiếp xúc Coulomb (H0b) dưới quy trình hiệu chuẩn khóa tham số "
        "có dự đoán thỏa đáng quan hệ mô men - độ cong phụ thuộc áp suất, độ cứng uốn tiếp tuyến, các vòng trễ năng lượng và các đại lượng "
        "quan sát trượt/chuyển pha cục bộ của bó dây NiTi siêu đàn hồi hay không, hay sự thất bại của mô hình này dưới các điều kiện kiểm chứng "
        "độc lập mới chứng minh sự cần thiết của một định luật ghép cặp cấu thành - tiếp xúc mới (H1)?\"",
        italic=True
    )
    add_p(
        "Câu hỏi này hoàn toàn trung tính vì nó không đặt cược vào tính mới của H1: Nếu thực nghiệm kiểm chứng cho thấy H0b dự đoán chính xác "
        "trong dung sai cho phép, nghiên cứu đóng góp một kết luận khoa học có giá trị khẳng định miền hiệu lực của các công cụ phần tử hữu hạn "
        "tiếp xúc hiện hữu cho kết cấu bó dây NiTi; ngược lại, nếu H0b thất bại có hệ thống dưới điều kiện kiểm chứng độc lập (held-out validation), "
        "nghiên cứu mới chính thức mở ra cơ sở thực nghiệm vững chắc để bảo vệ sự cần thiết của một định luật ghép cặp mới."
    )

    # --- 9. KẾT LUẬN CUỐI ---
    add_heading_1("9. TỔNG KẾT VÀ TRẠNG THÁI NGHIÊN CỨU HIỆN TẠI")
    add_p(
        "1. Những việc đã làm được: (1) Đã phân rã toàn diện ý tưởng tổ hợp thiết bị ban đầu của mentor thành các giả thuyết độc lập; "
        "(2) Đã rà soát đối kháng prior art và dứt khoát loại bỏ các tuyên bố tính mới cấp thiết bị (C1–C4, C8); (3) Đã chuyển dịch trọng tâm "
        "thành công từ chế tạo robot sang cơ học kết cấu cốt lõi; (4) Đã làm rõ bản chất của áp suất giam giữ và ma sát tiếp xúc trong cáp NiTi; "
        "(5) Đã hoàn thành quy trình truy vết trích dẫn mục tiêu 15/15 hướng và đóng giao thức kiểm chứng MP1-V002; (6) Đã thiết lập khung phân biệt "
        "mô hình H0b / H1 trung tính và có thể bác bỏ."
    )
    add_p(
        "2. Những kết luận rút ra: (1) Ý tưởng tổ hợp thiết bị không đủ tính mới để làm đề tài nghiên cứu; (2) Ma sát và tiêu tán trễ trong dây NiTi "
        "là hiện tượng đã biết rõ; (3) Áp suất dương không tạo ra nguyên lý vật lý mới mà chỉ là điều kiện biên lực mặt; (4) Mô hình H0b hiện hữu "
        "vẫn là một đối thủ cạnh tranh đáng gờm chưa bị đánh bại; (5) MP1 chỉ có thể đứng vững dưới dạng một câu hỏi nghiên cứu phân biệt mô hình có điều kiện."
    )
    add_p(
        "3. Trạng thái khoa học hiện tại (Current Canonical Research State):\n"
        "• Giao thức trích dẫn mục tiêu (Citation Protocol): ĐÃ ĐÓNG (CLOSED 15/15 directions screened: backward 9/9, forward 6/6; search cutoff: 2026-09-25).\n"
        "• Bằng chứng trực tiếp bác bỏ (Direct Prior-Art Kill trong protocol): CHƯA TÌM THẤY (NOT FOUND).\n"
        "• Trạng thái mô hình H0b: CHƯA BỊ BÁC BỎ (NOT FALSIFIED / LIVE COMPETITOR).\n"
        "• Trạng thái giả thuyết H1: CHƯA CÓ ĐỦ BẰNG CHỨNG (INSUFFICIENT EVIDENCE).\n"
        "• Trạng thái đề tài MP1: ỨNG VIÊN CÓ ĐIỀU KIỆN (CONDITIONAL CANDIDATE), cổng khoa học hiện ở trạng thái BLOCKED bởi 8 khoảng trống khoa học "
        "và 5 bài kiểm tra K-tests chưa giải quyết (đặc biệt là tính khả thi của miền cùng tồn tại trượt - chuyển pha, khả năng nhận dạng cơ chế từ dữ liệu uốn toàn cục, "
        "và sự sai lệch giữa áp suất buồng khí p với lực pháp tuyến cục bộ fn)."
    )
    add_p(
        "MP1 hiện được bảo tồn nguyên vẹn như một phương án dự phòng khả thi (viable alternative) đã được kiểm chứng đối kháng nghiêm ngặt, "
        "sẵn sàng cho bước đối chiếu toàn diện với hướng nghiên cứu D1/M1 trước khi đưa ra quyết định khóa đề tài thạc sĩ chính thức."
    )

    # --- 10. REFERENCES ---
    add_heading_1("10. TÀI LIỆU THAM KHẢO (REFERENCES)")
    add_p(
        "Danh mục tài liệu tham khảo dưới đây bao gồm đầy đủ 17 công trình khoa học thực sự được trích dẫn và sử dụng trực tiếp trong báo cáo, "
        "được định dạng chuẩn xác theo quy chuẩn APA 7th dựa trên metadata đã kiểm chứng toàn văn trong repository:",
        italic=True
    )

    references = [
        "Bai, L., Yan, H., Li, J., Shan, J., & Hou, P. (2022). Detachable soft actuators with tunable stiffness based on wire jamming. Applied Sciences, 12(7), 3582. https://doi.org/10.3390/app12073582",
        "Barsi, F., Carboni, B., & Lacarbonara, W. (2025). A new mechanical model of short wire ropes: Theory and experimental validation. Engineering Structures, 323, 119217. https://doi.org/10.1016/j.engstruct.2024.119217",
        "Carboni, B., & Lacarbonara, W. (2016). Nonlinear vibration absorber with pinched hysteresis: Theory and experiments. Journal of Engineering Mechanics, 142(5), 04016023. https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072",
        "Carboni, B., Lacarbonara, W., & Auricchio, F. (2015). Hysteresis of multiconfiguration assemblies of Nitinol and steel strands. Journal of Engineering Mechanics, 141(4), 04014138. https://doi.org/10.1061/(ASCE)EM.1943-7889.0000852",
        "Fang, C., Zheng, Y., Chen, J., Yam, M. C. H., & Wang, W. (2019). Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteresis and self-centering. Engineering Structures, 183, 550–563. https://doi.org/10.1016/j.engstruct.2019.01.049",
        "Huynh, H. H., Han, D., Yoshida, K., De Volder, M., & Kim, J. W. (2022). Soft actuator with switchable stiffness using a micropump-activated jamming system. Sensors and Actuators A: Physical, 338, 113449. https://doi.org/10.1016/j.sna.2022.113449",
        "Kang, Z., Wang, Z., Zhou, B., & Xue, S. (2020). Finite element method for mechanical behavior of shape memory alloy superelastic cables. Journal of Mechanical Engineering, 56(14), 65–73. https://doi.org/10.3901/JME.2020.14.065",
        "Liu, T., Xia, H., Lee, D. Y., Firouzeh, A., Park, Y. L., & Cho, K. J. (2021). A positive pressure jamming based variable stiffness structure and its application on wearable robots. IEEE Robotics and Automation Letters, 6(4), 7874–7881. https://doi.org/10.1109/LRA.2021.3097255",
        "Liu, X. (2004). Cable vibration considering internal friction [Master's thesis, University of Hawaii at Manoa].",
        "Matsumoto, N., Cho, H., Takashima, K., & Suzuki, H. (2024). Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon. Mechanical Engineering Journal, 11(4), 24-00130. https://doi.org/10.1299/mej.24-00130",
        "Pierce, M. D., & Mascaro, S. A. (2013). A biologically inspired wet shape memory alloy actuated robotic pump. IEEE/ASME Transactions on Mechatronics, 18(6), 1709–1718. https://doi.org/10.1109/TMECH.2012.2211032",
        "Reedlunn, B., Daly, S., & Shaw, J. (2013a). Superelastic shape memory alloy cables: Part I – Isothermal tension experiments. International Journal of Solids and Structures, 50(20–21), 3009–3026. https://doi.org/10.1016/j.ijsolstr.2013.03.013",
        "Reedlunn, B., Daly, S., & Shaw, J. (2013b). Superelastic shape memory alloy cables: Part II – Subcomponent investigations. International Journal of Solids and Structures, 50(20–21), 3027–3044. https://doi.org/10.1016/j.ijsolstr.2013.03.015",
        "Takashima, K., Imazawa, T., & Cho, H. (2022). Variable-stiffness and deformable link using shape-memory material and jamming transition phenomenon. Journal of Robotics and Mechatronics, 34(3), 466–474. https://doi.org/10.20965/jrm.2022.p0466",
        "Tjahjanto, D. D., Tyrberg, A., & Mullins, J. (2017). Bending mechanics of cable cores and fillers in a dynamic submarine cable. In Proceedings of the ASME 2017 36th International Conference on Ocean, Offshore and Arctic Engineering (OMAE2017) (Paper No. OMAE2017-62553). ASME.",
        "Vahidi, S., Arghavani, J., Choi, E., & Ostadrahimi, A. (2021). Mechanical response of single and double-helix SMA wire ropes. Mechanics of Advanced Materials and Structures, 29(26), 5035–5046. https://doi.org/10.1080/15376494.2021.1955313",
        "Wang, T., Ding, F., & Sun, Z. (2024). Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm. Industrial Robot: The International Journal of Robotics Research and Application, 51(5), 837–846. https://doi.org/10.1108/IR-11-2023-0305",
        "Zhang, S., & Yao, J. (2026). A variable stiffness omnidirectional chain based on positive-pressure fiber jamming. Mechanical Sciences, 17(2), 481–492. https://doi.org/10.5194/ms-17-481-2026"
    ]

    for ref in references:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)
        run = p.add_run(ref)
        run.font.name = "Times New Roman"
        run.font.size = Pt(13)

    output_path = "docs/reports/MP1_MENTOR_NARROWING_REPORT_2026-09-26.docx"
    doc.save(output_path)
    print(f"Report successfully saved to: {output_path}")

if __name__ == "__main__":
    build_report()
