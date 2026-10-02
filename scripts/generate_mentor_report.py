# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive, academic, mentor-facing Word report for MP1:
docs/reports/MP1_MENTOR_RESEARCH_NARROWING_REPORT_2026-09-26.docx

Strictly conforms to:
- Font: Times New Roman throughout
- Body: 13 pt, Line spacing 1.5, Justified, Space after 6 pt
- Headings: Times New Roman 13 pt Bold, Line spacing 1.5, Space after 6 pt
- Tables: Clean, readable, Times New Roman 10-11 pt, header shading #EAEAEA, cantSplit, tblHeader
- Page numbers in footer
- Grayscale Figure 1 embedded
- Source Precedence: Canonical current state, S01 corrections, Citation closure 15/15 protocol satisfied
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

from report_helpers import (
    set_cell_margins, set_cell_shading, set_table_borders,
    make_row_header, prevent_row_split, add_page_number_to_run, add_total_pages_to_run
)

def create_report():
    doc = Document()
    
    # -------------------------------------------------------------
    # Page Setup: A4, Margins: Top 2.5cm, Bottom 2.5cm, Left 2.5cm, Right 2.0cm
    # -------------------------------------------------------------
    section = doc.sections[0]
    section.page_width = Inches(8.27)   # 210 mm
    section.page_height = Inches(11.69) # 297 mm
    section.top_margin = Inches(0.98)   # ~2.5 cm
    section.bottom_margin = Inches(0.98)# ~2.5 cm
    section.left_margin = Inches(0.98)  # ~2.5 cm
    section.right_margin = Inches(0.79) # ~2.0 cm
    
    # -------------------------------------------------------------
    # Styles Configuration
    # -------------------------------------------------------------
    styles = doc.styles
    
    # Normal Style (Body)
    normal_style = styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(13)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.space_after = Pt(6)
    normal_style.paragraph_format.space_before = Pt(0)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Header & Footer
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("Báo cáo Thu hẹp Phạm vi Nghiên cứu MP1 — Trình bày Mentor (26/09/2026)")
    hrun.font.name = 'Times New Roman'
    hrun.font.size = Pt(9.5)
    hrun.font.italic = True
    hrun.font.color.rgb = RGBColor(100, 100, 100)
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun1 = fp.add_run("Trang ")
    frun1.font.name = 'Times New Roman'
    frun1.font.size = Pt(10)
    frun1.font.color.rgb = RGBColor(80, 80, 80)
    add_page_number_to_run(frun1)
    frun2 = fp.add_run(" / ")
    frun2.font.name = 'Times New Roman'
    frun2.font.size = Pt(10)
    frun2.font.color.rgb = RGBColor(80, 80, 80)
    add_total_pages_to_run(frun2)
    
    # Helper for adding headings strictly in Times New Roman 13 pt Bold
    def add_custom_heading(text, level=1):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.keep_with_next = True
        
        if level == 1:
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(6)
        elif level == 2:
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.space_after = Pt(4)
        else:
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(3)
            
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_p(text, bold_prefix="", italic_prefix="", bold_runs=None):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.space_before = Pt(0)
        
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.name = 'Times New Roman'
            r_b.font.size = Pt(13)
            r_b.font.bold = True
            r_b.font.color.rgb = RGBColor(0, 0, 0)
            
        if italic_prefix:
            r_i = p.add_run(italic_prefix)
            r_i.font.name = 'Times New Roman'
            r_i.font.size = Pt(13)
            r_i.font.italic = True
            r_i.font.color.rgb = RGBColor(0, 0, 0)
            
        if bold_runs:
            for piece, is_bold, is_italic in bold_runs:
                r = p.add_run(piece)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(13)
                r.font.bold = is_bold
                r.font.italic = is_italic
                r.font.color.rgb = RGBColor(0, 0, 0)
        else:
            r_t = p.add_run(text)
            r_t.font.name = 'Times New Roman'
            r_t.font.size = Pt(13)
            r_t.font.color.rgb = RGBColor(0, 0, 0)
        return p

    # -------------------------------------------------------------
    # Title Block
    # -------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_t1 = p_title.add_run("BÁO CÁO KHOA HỌC DÀNH CHO MENTOR\n")
    r_t1.font.name = 'Times New Roman'
    r_t1.font.size = Pt(13)
    r_t1.font.bold = True
    r_t2 = p_title.add_run("TIẾN TRÌNH THU HẸP PHẠM VI NGHIÊN CỨU VÀ XÁC LẬP BÀI TOÁN KHOA HỌC CHO ĐỀ TÀI MP1\n")
    r_t2.font.name = 'Times New Roman'
    r_t2.font.size = Pt(13)
    r_t2.font.bold = True
    r_t3 = p_title.add_run("Từ Ý Tưởng Kiến Trúc Robot Mềm Ban Đầu Đến Bài Toán Phân Biệt Mô Hình Cơ Học Tiếp Xúc Của Bó Dây NiTi Dưới Áp Suất Giam Giữ Điều Khiển")
    r_t3.font.name = 'Times New Roman'
    r_t3.font.size = Pt(12)
    r_t3.font.italic = True
    r_t3.font.bold = True

    # Metadata Table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, color="CCCCCC", sz="4")
    
    meta_data = [
        ("Học viên / Người thực hiện:", "Tác giả nghiên cứu MP1 (MSc Research)"),
        ("Đề tài thảo luận:", "Hướng nghiên cứu MP1 (Mentor Pivot Candidate)"),
        ("Hồ sơ bằng chứng & Phân tích:", "Repository khanhpn308/research_agents (Vòng MP1-V001, MP1-V002, Macro-stage W02 Closeout, WR1-S01)"),
        ("Ngày báo cáo & Phiên bản:", "26/09/2026 — Phiên bản phục vụ phản biện học thuật với Mentor")
    ]
    
    for row_idx, (lbl, val) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        prevent_row_split(row)
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.5)
        c1.width = Inches(4.5)
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.paragraph_format.line_spacing = 1.15
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(lbl)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(11)
        r0.font.bold = True
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p1.paragraph_format.line_spacing = 1.15
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # PHẦN 1: MỤC TIÊU VÀ PHƯƠNG PHÁP LUẬN
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 1: MỤC TIÊU VÀ PHƯƠNG PHÁP LUẬN BÁO CÁO", level=1)
    
    add_p(
        "Báo cáo này được biên soạn nhằm trình bày một cách có hệ thống, minh bạch và có thể truy vết toàn diện quá trình đi từ ý tưởng nghiên cứu ban đầu do Mentor gợi ý đến một câu hỏi nghiên cứu (research question) cụ thể, có thể phản nghiệm và đạt chuẩn học thuật cho đề tài MP1. Mục tiêu tối thượng của báo cáo không phải là tìm kiếm các bài báo để tán dương hay chứng minh ý tưởng ban đầu là hoàn toàn mới lạ; ngược lại, phương pháp luận cốt lõi được áp dụng xuyên suốt là: \"Không bảo vệ ý tưởng một cách chủ quan, mà chủ động tìm kiếm các công trình gần nhất trong y văn quốc tế để cố gắng bác bỏ hoặc thu hẹp tối đa phạm vi ý tưởng\" (Do not defend the current idea. Try to falsify it using the closest prior work)."
    )
    
    add_p(
        "Trong quy trình học thuật nghiêm ngặt, việc tìm kiếm tài liệu (literature search) không phải là một hành động thụ động nhằm thu thập các tài liệu tham khảo bổ sung sau khi đề tài đã được chốt cứng. Tại đề tài MP1, tìm kiếm y văn chính là một động cơ của tiến trình suy luận khoa học (search as part of the research reasoning process). Quy trình này vận hành theo một vòng lặp suy diễn - phản nghiệm chặt chẽ: Câu hỏi nghiên cứu tại thời điểm t dẫn đến Ý định tìm kiếm cụ thể -> Xác lập bộ từ khóa tìm kiếm -> Phát hiện các bài báo đe dọa gần nhất -> Trích xuất bằng chứng cơ học toàn văn -> Đối chiếu và loại bỏ các giả định/tuyên bố tính mới không còn đứng vững -> Thu hẹp đề tài -> Hình thành câu hỏi nghiên cứu hẹp hơn -> Thiết lập bộ từ khóa tìm kiếm mới. Qua từng giai đoạn, người nghiên cứu luôn phải trả lời câu hỏi mang tính kỷ luật: \"Sau khi đọc bằng chứng này, tôi không còn được phép khẳng định điều gì?\"."
    )

    # -------------------------------------------------------------
    # PHẦN 2: Ý TƯỞNG MP1 BAN ĐẦU VÀ SỰ BẤT TOÀN KHOA HỌC
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 2: Ý TƯỞNG MP1 BAN ĐẦU VÀ SỰ BẤT TOÀN KHOA HỌC", level=1)
    
    add_p(
        "Ý tưởng MP1 ban đầu do Mentor đề xuất xuất phát từ mong muốn chế tạo một cơ cấu robot mềm có khả năng biến thiên độ cứng linh hoạt, kết hợp năm thành phần kỹ thuật chính: (1) Bó dây kim loại hoặc hợp kim nhớ hình siêu đàn hồi (superelastic NiTi wire bundle); (2) Cơ chế giam giữ bằng áp suất dương (positive pressure confinement) thông qua một màng bọc kín khí; (3) Hiệu ứng kẹt ma sát giữa các sợi dây (inter-wire frictional jamming) nhằm khóa chuyển vị trượt tương đối; (4) Khả năng điều khiển độ cứng uốn (variable bending stiffness) phục vụ cánh tay robot mềm hoặc tay gắp; và (5) Tùy chọn tích hợp một nguồn áp suất nhỏ gọn dẫn động bằng dây SMA co rút kéo piston/xilanh (compact SMA-driven syringe/piston pressure source)."
    )
    
    add_p(
        "Mặc dù ý tưởng này mang tính trực giác kỹ thuật hấp dẫn và hứa hẹn tiềm năng ứng dụng thực tế, việc phân tích bản chất khoa học ban đầu cho thấy đề tài ở dạng sơ khởi này hoàn toàn chưa đủ cơ sở để xem là một bài toán nghiên cứu (research problem) cấp độ thạc sĩ khoa học vì những lý do then chốt sau:",
        bold_prefix="Đánh giá tính bất toàn khoa học của ý tưởng ban đầu: "
    )

    add_p(
        "1. Nhầm lẫn giữa thiết kế thiết bị kỹ thuật và đóng góp khoa học: Ý tưởng ban đầu tập trung vào việc \"chế tạo một cánh tay/thiết bị hoạt động được\" bằng cách ghép nối nhiều linh kiện, thay vì xác định một khoảng trống tri thức cơ học chưa được giải quyết trong tự nhiên hoặc y văn.",
        bold_prefix="• "
    )
    add_p(
        "2. Tồn tại quá nhiều giả định tính mới chưa được kiểm chứng ở cấp linh kiện: Đề tài mặc định rằng việc dùng dây kim loại để kẹt, việc dùng áp suất dương để kẹt, việc kết hợp SMA với jamming, và việc chế tạo bơm nhỏ gọn đều là những ý tưởng mới chưa ai thực hiện.",
        bold_prefix="• "
    )
    add_p(
        "3. Thiếu vắng đối tượng khoa học và hệ biến số xác định: Đề tài chưa làm rõ biến độc lập là gì (áp suất buồng, lực pháp tuyến tiếp xúc, hay lịch sử biến dạng uốn?), biến phụ thuộc là gì (mô-men uốn, độ cứng cát tuyến, độ cứng tiếp tuyến, hay hao tán năng lượng trễ?), và miền làm việc dự kiến nằm ở đâu.",
        bold_prefix="• "
    )
    add_p(
        "4. Khoảng trống cơ học cốt lõi bị che lấp bởi phần cứng: Sự phức tạp của cơ cấu xilanh SMA và màng bọc làm phân tán nỗ lực nghiên cứu, khiến bản chất cơ học tiếp xúc vi mô giữa các sợi dây siêu đàn hồi không được mô hình hóa hay cô lập một cách có chủ đích.",
        bold_prefix="• "
    )
    add_p(
        "5. Chưa có giả thuyết khoa học có thể phản nghiệm (falsifiable hypothesis): Đề tài ban đầu không thể phân biệt được liệu các hiện tượng quan sát được là do cơ học tiếp xúc thông thường đã biết hay đòi hỏi một định luật vật lý mới.",
        bold_prefix="• "
    )

    # -------------------------------------------------------------
    # PHẦN 3: BẢNG DÒNG THỜI GIAN THU HẸP PHẠM VI NGHIÊN CỨU
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 3: DÒNG THỜI GIAN THU HẸP PHẠM VI NGHIÊN CỨU (TIMELINE NARROWING)", level=1)
    
    add_p(
        "Để biến ý tưởng ban đầu thành một bài toán khoa học thực thụ, đề tài đã trải qua một tiến trình kiểm chứng y văn gồm 14 giai đoạn liên tục (Stage 0 đến Stage 13). Mỗi bước đi đều gắn liền với một câu hỏi định hướng, một bộ từ khóa truy vấn, đối chiếu với các bài báo toàn văn thực tế, và đưa ra quyết định loại bỏ dứt khoát những tuyên bố tính mới không còn đứng vững. Bảng 1 tổng hợp toàn diện dòng thời gian suy luận này."
    )

    # Table 1: Timeline
    table1 = doc.add_table(rows=15, cols=6)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table1, color="B0B0B0", sz="4")
    
    headers_t1 = [
        "Giai đoạn & Topic",
        "Ý định tìm kiếm & Truy vấn (Trạng thái)",
        "Bằng chứng then chốt (Primary Evidence)",
        "Tuyên bố bị đe dọa & Phán quyết",
        "Phạm vi bị loại bỏ / Giới hạn còn lại",
        "Truy vấn & Câu hỏi tiếp theo"
    ]
    
    hdr_row1 = table1.rows[0]
    make_row_header(hdr_row1)
    prevent_row_split(hdr_row1)
    for col_idx, h_text in enumerate(headers_t1):
        cell = hdr_row1.cells[col_idx]
        set_cell_shading(cell, "EAEAEA")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.bold = True

    timeline_data = [
        (
            "Stage 0\n(Mentor Idea)\nKiến trúc robot mềm bó dây NiTi biến thiên độ cứng bằng áp suất dương + bơm SMA.",
            "Ý định: Khảo sát tổng quan về robot mềm biến thiên độ cứng.\nTruy vấn: \"variable stiffness soft robot\" OR \"jamming soft actuator\"\n(Trạng thái: INFERRED)",
            "Tổng quan y văn robot mềm biến thiên độ cứng giai đoạn 2015–2022 (hạt, lá mỏng, sợi).",
            "Mọi tuyên bố tính mới cấp thiết bị chưa được kiểm chứng.\nPhán quyết: CẦN PHÂN RÃ HỌC THUẬT.",
            "Loại bỏ: Sự mơ hồ cấp hệ thống.\nCòn lại: Bản thiết kế thiết bị gồm 5 thành phần kỹ thuật ghép nối.",
            "Câu hỏi: Các thành phần độc lập trong kiến trúc này đã có ai công bố chưa?\nTừ khóa tiếp: \"wire jamming soft robot\""
        ),
        (
            "Stage 1\n(Decomposition)\nPhân rã kiến trúc ban đầu thành 8 tuyên bố cụ thể C1–C8.",
            "Ý định: Thiết lập danh mục các tuyên bố độc lập để kiểm chứng y văn.\nTruy vấn: Phân rã nội bộ (C1-C8 protocol mapping)\n(Trạng thái: EXACT HISTORICAL)",
            "Đề cương kiểm chứng MP1-V001 (CORE_PRIOR_ART_AUDIT_PLAN.md, 2026-09-22).",
            "C1 (Kẹt dây), C2 (Áp suất dương), C3 (SMA+Jamming), C4 (Bơm nhỏ gọn), C8 (Xilanh SMA).\nPhán quyết: TÁCH ĐỂ PHẢN NGHIỆM.",
            "Loại bỏ: Tư duy bảo vệ toàn bộ thiết bị nguyên khối.\nCòn lại: 8 bài toán con có thể độc lập bác bỏ bằng y văn.",
            "Câu hỏi: Cơ chế kẹt sợi/dây (wire/fiber jamming) đã có ai nghiên cứu chưa?\nTừ khóa tiếp: \"wire jamming variable stiffness\""
        ),
        (
            "Stage 2\n(Wire Jamming)\nKiểm tra tính mới của cơ chế kẹt sợi/dây kim loại làm thay đổi độ cứng.",
            "Ý định: Tìm kiếm công trình dùng dây/sợi ma sát để thay đổi độ cứng uốn.\nTruy vấn: \"wire jamming\" OR \"fiber jamming\" AND \"variable stiffness\"\n(Trạng thái: RECONSTRUCTED)",
            "Bai et al. (2022) [App. Sci.]: Cơ cấu kẹt dây kim loại và sợi tự nhiên dưới chân không.\nZhang & Yao (2026) [Mech. Sci.]: Kẹt bó sợi.",
            "Tuyên bố C1: \"Kẹt dây/sợi kim loại để biến thiên độ cứng là mới\".\nPhán quyết: BÁC BỎ HOÀN TOÀN C1 (CLOSED).",
            "Loại bỏ: Tuyên bố tính mới của cơ chế kẹt dây/sợi (wire jamming novelty).\nCòn lại: Giam giữ bằng áp suất dương trên dây kim loại.",
            "Câu hỏi: Kẹt bằng áp suất dương (thay vì chân không) có phải là nguyên lý mới?\nTừ khóa tiếp: \"positive pressure jamming robot\""
        ),
        (
            "Stage 3\n(Positive Pressure)\nKiểm tra tính mới của việc dùng áp suất dương trong jamming.",
            "Ý định: Tìm kiếm công trình kẹt bằng cách nén áp suất dương bên ngoài.\nTruy vấn: \"positive pressure jamming\" AND \"variable stiffness\"\n(Trạng thái: EXACT HISTORICAL B02/F02)",
            "Liu et al. (2021) [IEEE RA-L]: Kẹt hạt bằng áp suất dương đến 200 kPa.\nZhang & Yao (2026): Nén bó sợi bằng áp suất dương 300 kPa.",
            "Tuyên bố C2: \"Kẹt bằng áp suất dương để thay đổi độ cứng là mới\".\nPhán quyết: BÁC BỎ HOÀN TOÀN C2 (CLOSED).",
            "Loại bỏ: Khẳng định dùng áp suất dương là một nguyên lý jamming mới.\nCòn lại: Tích hợp SMA và jamming trong cùng thiết bị.",
            "Câu hỏi: Sự kết hợp giữa dây SMA và cơ chế jamming có phải là đóng góp mới?\nTừ khóa tiếp: \"SMA wire granular jamming\""
        ),
        (
            "Stage 4\n(SMA + Jamming)\nKiểm tra tính mới của việc kết hợp hợp kim nhớ hình SMA với jamming.",
            "Ý định: Khảo sát các cơ cấu kết hợp dây NiTi SMA và bộ kẹt độ cứng.\nTruy vấn: \"shape memory alloy\" AND \"jamming\" AND \"soft actuator\"\n(Trạng thái: EXACT HISTORICAL B09/F05)",
            "Dòng công trình Takashima et al. (2020, 2022, 2026) & Matsumoto et al. (2021, 2024): Dây NiTi tích hợp trong cơ cấu kẹt hạt chân không.",
            "Tuyên bố C3: \"Tích hợp SMA và jamming trong cùng cơ cấu mềm là mới\".\nPhán quyết: BÁC BỎ HOÀN TOÀN C3 (CLOSED).",
            "Loại bỏ: Tính mới của việc ghép SMA với jamming ở cấp hệ thống thiết bị.\nCòn lại: Bản thân dây NiTi đóng vai trò trực tiếp là môi trường ma sát kẹt.",
            "Câu hỏi: Nguồn tạo áp suất nhỏ gọn (bơm vi mô/piston SMA) có mới không?\nTừ khóa tiếp: \"embedded micropump jamming soft robot\""
        ),
        (
            "Stage 5\n(Compact Pressure)\nKiểm tra tính mới của nguồn áp suất tích hợp / piston dẫn động bằng SMA.",
            "Ý định: Tìm kiếm bơm nhỏ gọn hoặc piston dẫn động jamming.\nTruy vấn: \"embedded pump jamming\" OR \"SMA piston pressure source\"\n(Trạng thái: RECONSTRUCTED)",
            "Huynh et al. (2022) [Sci. Robot.]: Bơm vi mô tích hợp kích hoạt jamming.\nWang et al. (2024): Cơ cấu piston motor nén hạt.\nPierce & Mascaro (2013): Bơm SMA.",
            "Tuyên bố C4, C8: \"Nguồn áp nhỏ gọn / piston SMA điều khiển jamming là mới\".\nPhán quyết: BÁC BỎ C4, C8 (PRE-EMPTED).",
            "Loại bỏ: Phép thế cơ cấu chấp hành (bơm SMA vs bơm piezo chỉ là hardware substitution).\nCòn lại: Lõi cơ học của bản thân bó dây NiTi.",
            "Câu hỏi: Nếu toàn bộ thiết bị đã bị pre-empted, đề tài còn giá trị khoa học gì?\nTừ khóa tiếp: Chuyển sang Lõi Cơ học (Mechanics Core)."
        ),
        (
            "Stage 6\n(Strategic Pivot)\nChuyển hướng chiến lược: Từ Kiến trúc thiết bị sang Lõi cơ học bó dây.",
            "Ý định: Tái định vị đề tài; từ bỏ đóng góp chế tạo máy để tập trung vào cơ học tiếp xúc.\nTruy vấn: Tái cấu trúc mục tiêu sang T1, T2, T3 (MP1-V001 Adjudication)\n(Trạng thái: CANONICAL PIVOT)",
            "Hồ sơ CORE_PRIOR_ART_AUDIT.json: Xác nhận C1–C4, C8 đã bị đóng dứt điểm; chỉ còn C5, C6, C7 mở về mặt cơ học.",
            "Tuyên bố thiết bị tổng thể bị triệt tiêu hoàn toàn.\nPhán quyết: PIVOT TO MECHANICS CORE (Đồng thuận cao).",
            "Loại bỏ: Toàn bộ mục tiêu chế tạo robot mềm và bơm xilanh SMA.\nCòn lại: T1 (Tiếp xúc NiTi), T2 (Áp suất hướng kính), T3 (Ghép siêu đàn hồi và ma sát).",
            "Câu hỏi: Tiếp xúc ma sát và trượt giữa các dây NiTi đã được nghiên cứu chưa?\nTừ khóa tiếp: \"superelastic NiTi cable interwire friction\""
        ),
        (
            "Stage 7\n(NiTi Contact Lit.)\nKhảo sát cơ học ma sát, trượt và tiếp xúc giữa các dây trong cáp/bó dây NiTi.",
            "Ý định: Tìm kiếm công trình về tiếp xúc ma sát trong bó dây/cáp NiTi.\nTruy vấn: \"NiTi wire contact\" OR \"Nitinol cable friction\" OR \"superelastic interwire slip\"\n(Trạng thái: EXACT HISTORICAL B10/F07/F08)",
            "Reedlunn et al. (2013) [IJSS]: Động học cáp NiTi.\nCarboni et al. (2015, 2016) [ASCE]: Trễ thắt do ma sát và chuyển pha trong cáp Nitinol.\nFang (2019): Cáp NiTi.",
            "Tuyên bố C5: \"Dùng dây NiTi làm môi trường cọ xát ma sát là hoàn toàn mới\".\nPhán quyết: BÁC BỎ C5 (ESTABLISHED IN CABLES).",
            "Loại bỏ: Tuyên bố tính mới về hiện tượng ma sát cọ xát giữa các dây NiTi.\nCòn lại: Phản ứng uốn và trượt dính-trượt dưới tác dụng của áp suất ngoài.",
            "Câu hỏi: Cơ học uốn và trượt dính-trượt (stick-slip) của cáp nhiều sợi được mô hình hóa ra sao?\nTừ khóa tiếp: \"wire rope bending stick-slip stiffness\""
        ),
        (
            "Stage 8\n(Bending Mechanics)\nKhảo sát cơ học uốn và các trạng thái trượt dính-trượt của cáp/bó dây.",
            "Ý định: Tìm kiếm mô hình cơ học uốn giải bài toán trượt ma sát giữa các sợi.\nTruy vấn: \"wire rope bending stiffness\" AND \"stick slip friction\"\n(Trạng thái: EXACT HISTORICAL B12/F13)",
            "Xin Liu (2004) [MSc Thesis]: Độ cứng uốn phụ thuộc độ cong và áp lực giữa các lớp.\nBarsi et al. (2025) [Eng. Struct.]: Giới hạn độ cứng dính/trượt của cáp ngắn.",
            "Tuyên bố: \"Hiện tượng thay đổi độ cứng uốn do trượt ma sát chưa được mô hình hóa\".\nPhán quyết: LÝ THUYẾT NỀN TẢNG ĐÃ TỒN TẠI.",
            "Loại bỏ: Khẳng định thiếu vắng mô hình cơ học về trượt uốn nhiều sợi.\nCòn lại: Tác động điều khiển của áp suất giam giữ chủ động lên tiếp xúc.",
            "Câu hỏi: Áp suất giam giữ bên ngoài có tạo ra một định luật cơ học mới không?\nTừ khóa tiếp: \"radial pressure cable friction bending\""
        ),
        (
            "Stage 9\n(Pressure Mechanics)\nKhảo sát cơ học của cáp/bó dây dưới áp suất giam giữ hướng kính.",
            "Ý định: Tìm kiếm công trình phân tích cáp chịu uốn dưới áp suất nén ngoài.\nTruy vấn: \"radial pressure cable bending\" OR \"external pressure interwire friction\"\n(Trạng thái: EXACT HISTORICAL B04/F10)",
            "Tjahjanto et al. (2017) [OMAE]: Mô hình uốn cáp ngầm dưới áp suất ngoài 0.2 MPa.\nPhân tích truyền lực: Hiệu ứng vòm và màng làm p != fn.",
            "Tuyên bố C6: \"Áp suất giam giữ chủ động tạo ra cơ chế vật lý mới\".\nPhán quyết: HẠ CẤP C6 THÀNH ĐIỀU KIỆN BIÊN.",
            "Loại bỏ: Luận điểm coi áp suất là định luật cấu thành mới (pressure is just a traction BC).\nCòn lại: Bài toán ghép cặp giữa chuyển pha NiTi và ma sát tiếp xúc.",
            "Câu hỏi: Các mô hình NiTi phi tuyến kết hợp tiếp xúc phần tử hữu hạn đã làm được gì?\nTừ khóa tiếp: \"superelastic NiTi UMAT contact friction\""
        ),
        (
            "Stage 10\n(FEA Formulations)\nKhảo sát các mô hình cấu thành NiTi phi tuyến kết hợp phần tử tiếp xúc ma sát.",
            "Ý định: Tìm kiếm mô hình 3D FEA kết hợp luật nhớ hình và tiếp xúc Coulomb.\nTruy vấn: \"superelastic cable finite element friction contact\"\n(Trạng thái: EXACT HISTORICAL B11/F10)",
            "Kang et al. (2020) [J. Mech. Eng.]: Mô hình 3D FE cáp NiTi chịu kéo (tiếp xúc trơn).\nVahidi et al. (2021/2022) [MAMS]: Mô hình Souza + ma sát Coulomb trong cáp xoắn.",
            "Tuyên bố: \"Chưa có công cụ lý thuyết nào có thể mô phỏng đồng thời NiTi và ma sát\".\nPhán quyết: KHUNG LÝ THUYẾT H0b ĐÃ TỒN TẠI.",
            "Loại bỏ: Khẳng định rằng toán học/mô phỏng hiện hữu bất lực trước bài toán này.\nCòn lại: Kiểm chứng thực nghiệm đối chứng dưới tham số bị khóa trong bài toán uốn.",
            "Câu hỏi: Liệu một mô hình đàn hồi sơ đẳng có thể giải thích được không?\nTừ khóa tiếp: Kiểm chứng thế tham số đàn hồi (Parameter-Substitution Test)."
        ),
        (
            "Stage 11\n(Hypothesis Separation)\nThử nghiệm thế tham số đàn hồi và phân tách hệ giả thuyết H0a / H0b / H1.",
            "Ý định: Kiểm tra xem có cần mô hình NiTi phức tạp không hay chỉ cần đổi mô-đun E.\nTruy vấn: Phân tích cơ học giải tích nội bộ & Red-team critique của Astra (2026-09-25)\n(Trạng thái: CANONICAL AUDIT)",
            "Phân tích miền biến dạng: Ở uốn lớn (>0.75%), mô-đun E biến thiên phi tuyến và trễ thắt.\nH0a bị bác bỏ. Tuy nhiên: H0a sai KHÔNG chứng minh H1 đúng!",
            "Tuyên bố: \"Bác bỏ mô hình đàn hồi hằng số đồng nghĩa với việc tìm ra định luật mới\".\nPhán quyết: THIẾT LẬP ĐỐI THỦ H0b.",
            "Loại bỏ: Giả thuyết rơm H0a; loại bỏ kết luận vội vã rằng H1 đã được chứng minh.\nCòn lại: Bài toán phân biệt mô hình giữa H0b và H1.",
            "Câu hỏi: Còn bài báo nào trên thế giới trực tiếp giải bài toán uốn bó dây NiTi dưới áp suất?\nTừ khóa tiếp: Targeted Citation Chasing Protocol."
        ),
        (
            "Stage 12\n(Citation Closure)\nThực hiện truy vết trích dẫn hai chiều (Citation Chasing) trên toàn bộ y văn then chốt.",
            "Ý định: Quét sạch trích dẫn xuôi/ngược từ 15 neo tài liệu để tìm kiếm direct kill.\nTruy vấn: 15 nhánh Scopus/Crossref (9 backward, 6 forward)\n(Trạng thái: PROTOCOL COMPLETED 15/15)",
            "Hồ sơ citation_coverage.json: Rà soát 312 bản ghi thô -> 258 bản ghi duy nhất. B11 và B12 đã rà soát dứt điểm. Không phát hiện bài báo nào giết chết trực tiếp MP1.",
            "Tuyên bố: \"Y văn còn nhánh trích dẫn mở đe dọa trực tiếp\".\nPhán quyết: PROTOCOL CLOSURE (stop_condition=true).",
            "Loại bỏ: Mối lo ngại về thiếu sót trong phạm vi giao thức.\nLưu ý: Đóng giao thức tra cứu KHÔNG tương đương chứng minh tính mới tuyệt đối trên toàn cầu.",
            "Câu hỏi: Câu hỏi khoa học chính xác, trung lập và có thể phản nghiệm là gì?\nTừ khóa tiếp: Xác lập Final Research Question."
        ),
        (
            "Stage 13\n(Final Research Question)\nXác lập Câu hỏi Nghiên cứu Cuối cùng: Bài toán Phân biệt Mô hình (Model Discrimination).",
            "Ý định: Đóng băng câu hỏi nghiên cứu bảo thủ, có thể phản nghiệm, trung lập khoa học.\nTruy vấn: FINAL_ADJUDICATION.md & S01 Formulation Crosswalk\n(Trạng thái: CANONICAL FROZEN)",
            "Đồng thuận khoa học cuối cùng: Đề tài MP1 sống sót như một bài toán kiểm chứng thực nghiệm đối chứng giữa H0b và thực nghiệm có kiểm soát.",
            "Không khẳng định tính mới tiên nghiệm; không khẳng định cần định luật mới.\nPhán quyết: MP1 LÀ ỨNG VIÊN KHẢ THI CÓ ĐIỀU KIỆN.",
            "Loại bỏ: Mọi tuyên bố tính mới cấp thiết bị và tính mới định luật vật lý chưa kiểm chứng.\nCòn lại: Câu hỏi phân biệt mô hình chính thức.",
            "Đích đến: Chuyển giao sang báo cáo so sánh Mentor với nhánh D1/M1."
        )
    ]
    
    for row_idx, row_content in enumerate(timeline_data, start=1):
        row = table1.rows[row_idx]
        prevent_row_split(row)
        for col_idx, text_val in enumerate(row_content):
            cell = row.cells[col_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            
            # Format text: split by lines and bold headers
            lines = text_val.split('\n')
            for l_idx, line in enumerate(lines):
                if l_idx > 0:
                    p.add_run('\n')
                if any(line.startswith(prefix) for prefix in [
                    "Stage", "Ý định:", "Truy vấn:", "Tuyên bố", "Phán quyết:",
                    "Loại bỏ:", "Còn lại:", "Câu hỏi:", "Từ khóa tiếp:", "Lưu ý:", "Đích đến:"
                ]):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        rb = p.add_run(parts[0] + ":")
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                        rt = p.add_run(parts[1])
                        rt.font.name = 'Times New Roman'
                        rt.font.size = Pt(9.5)
                    else:
                        rb = p.add_run(line)
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                else:
                    rt = p.add_run(line)
                    rt.font.name = 'Times New Roman'
                    rt.font.size = Pt(9.5)

    p_spacer2 = doc.add_paragraph()
    p_spacer2.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # PHẦN 4: TIẾN TRÌNH BIẾN ĐỔI CHIẾN LƯỢC TÌM KIẾM VÀ NHỮNG BÀI BÁO QUYẾT ĐỊNH
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 4: TIẾN TRÌNH BIẾN ĐỔI CHIẾN LƯỢC TÌM KIẾM VÀ NHỮNG BÀI BÁO QUYẾT ĐỊNH", level=1)
    
    add_p(
        "Một luận điểm cốt lõi mà báo cáo này muốn truyền tải tới Mentor là: Quá trình tìm kiếm tài liệu không phải là việc gõ vài từ khóa ngẫu nhiên trên Google Scholar rồi tổng hợp lại. Mỗi truy vấn tìm kiếm xuất hiện trong nghiên cứu này đều là kết quả tất yếu của một sự bế tắc hoặc sự thu hẹp về mặt logic khoa học ở bước trước đó. Khi một bằng chứng mới cho thấy một phần của ý tưởng đã được giải quyết, từ vựng tìm kiếm buộc phải thay đổi để thâm nhập sâu hơn vào tầng bản chất cơ học."
    )
    
    add_custom_heading("4.1. Bảng Tiến hóa Chiến lược Tìm kiếm (Search Strategy Evolution)", level=2)
    add_p(
        "Bảng 2 trình bày chi tiết sự biến chuyển của 8 nhóm chiến lược tìm kiếm (Search Groups 1–8), phân định rõ ràng giữa truy vấn lịch sử chính xác (EXACT HISTORICAL QUERY), truy vấn tái dựng từ biên bản thực thi (RECONSTRUCTED SEARCH KEYWORDS) và truy vấn suy luận logic (INFERRED SEARCH KEYWORDS)."
    )

    # Table 2: Search Strategy Evolution
    table2 = doc.add_table(rows=9, cols=5)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table2, color="B0B0B0", sz="4")
    
    headers_t2 = [
        "Nhóm tìm kiếm (Group)",
        "Bất định khoa học & Ý định tìm kiếm (Intent)",
        "Từ khóa tìm kiếm & Trạng thái (Query Status)",
        "Bài báo phát hiện & Kết luận thực tế (What became known)",
        "Phạm vi bị loại bỏ & Lý do đổi từ khóa (Why query changed)"
    ]
    
    hdr_row2 = table2.rows[0]
    make_row_header(hdr_row2)
    prevent_row_split(hdr_row2)
    for col_idx, h_text in enumerate(headers_t2):
        cell = hdr_row2.cells[col_idx]
        set_cell_shading(cell, "EAEAEA")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.bold = True

    search_groups_data = [
        (
            "Group 1:\nBroad Topic Discovery\n(Khám phá chủ đề rộng)",
            "Bất định: Liệu việc kết hợp robot mềm, vật liệu thông minh SMA và cơ chế jamming có phải là một hướng đi hoàn toàn mới chưa được khám phá?\nÝ định: Rà soát bức tranh toàn cảnh y văn quốc tế về biến thiên độ cứng trong robot mềm.",
            "Truy vấn: \"variable stiffness soft robot\" OR \"jamming variable stiffness robot\" OR \"shape memory alloy jamming\"\nTrạng thái: INFERRED SEARCH KEYWORDS (Khớp với các đợt rà soát tổng quan discovery ban đầu).",
            "Bài báo phát hiện: Các bài báo tổng quan về jamming (hạt, lá mỏng, sợi) và các cơ cấu biến thiên độ cứng giai đoạn 2015–2022.\nKết luận: Lĩnh vực biến thiên độ cứng bằng jamming đã rất phát triển; ý tưởng chung chung về robot mềm kẹt độ cứng không có tính mới.",
            "Bị loại bỏ: Tuyên bố tính mới ở cấp độ lĩnh vực tổng quát (broad field novelty).\nLý do đổi từ khóa: Cần đi sâu vào các cơ chế kẹt cụ thể của ý tưởng MP1: kẹt dây và kẹt áp suất dương.\nTừ khóa tiếp: \"wire jamming\", \"positive pressure jamming\"."
        ),
        (
            "Group 2:\nWire Jamming & Positive Pressure\n(Kẹt dây & Áp suất dương)",
            "Bất định: Liệu việc dùng dây kim loại/sợi (thay vì hạt cát hay tấm lá) và dùng áp suất nén dương (thay vì hút chân không) có tạo nên tính mới thiết bị không?\nÝ định: Tìm kiếm công trình kẹt sợi và kẹt áp suất dương.",
            "Truy vấn: \"wire jamming variable stiffness\" OR \"fiber jamming positive pressure\" OR \"positive pressure jamming soft robot\"\nTrạng thái: EXACT HISTORICAL (Từ các xuất nhập B01, B02, B03 trong data/search_exports/).",
            "Bài báo phát hiện: Bai et al. (2022) [App. Sci.]; Liu et al. (2021) [IEEE RA-L]; Zhang & Yao (2026) [Mech. Sci.].\nKết luận: Cả kẹt dây (Bai) và kẹt sợi nén bằng áp suất dương 300 kPa (Zhang & Yao) đều đã được công bố và mô hình hóa uốn thành công.",
            "Bị loại bỏ: Bác bỏ hoàn toàn C1 và C2. Thiết bị kẹt dây và áp suất dương không còn là phát minh mới.\nLý do đổi từ khóa: Thiết bị cơ bản đã có trước, phải kiểm tra xem sự xuất hiện của hợp kim SMA có tạo ra sự khác biệt không.\nTừ khóa tiếp: \"SMA wire granular jamming\"."
        ),
        (
            "Group 3:\nSMA + Jamming Integration\n(Tích hợp SMA và Jamming)",
            "Bất định: Liệu sự kết hợp đồng thời giữa cơ cấu chấp hành SMA và cơ chế jamming trong cùng một robot mềm có phải là một đóng góp kiến trúc mới?\nÝ định: Rà soát các thiết bị lai ghép giữa SMA và jamming.",
            "Truy vấn: \"shape memory alloy\" AND \"jamming\" AND \"variable stiffness actuator\"\nTrạng thái: EXACT HISTORICAL (Từ nhánh B09 và F05 liên kết Takashima lineage).",
            "Bài báo phát hiện: Takashima et al. (2020, 2022, 2026) và Matsumoto et al. (2021, 2024).\nKết luận: Việc dùng dây SMA làm gân co rút hoặc bộ nhớ hình kết hợp với buồng jamming chân không đã được nhóm Takashima khai thác triệt để.",
            "Bị loại bỏ: Bác bỏ hoàn toàn C3. Sự cùng tồn tại (coexistence) của SMA và jamming trong cùng một thiết bị là kiến trúc đã biết.\nLý do đổi từ khóa: Nhận ra tính mới cấp thiết bị đã bị triệt tiêu hoàn toàn (pre-empted). Bắt buộc phải chuyển hướng (pivot) sang Lõi Cơ học của chính bó dây NiTi.\nTừ khóa tiếp: \"NiTi wire contact mechanics\", \"Nitinol cable friction\"."
        ),
        (
            "Group 4:\nNiTi as Frictional Contacting Medium\n(Dây NiTi cọ xát ma sát)",
            "Bất định: Trong các công trình trước, NiTi chỉ là gân phụ trợ. Liệu khi chính các dây NiTi cọ xát vào nhau, cơ học ma sát và trượt có phải là hiện tượng mới?\nÝ định: Khảo sát cơ học tiếp xúc và ma sát trong cáp/bó dây NiTi nhiều sợi.",
            "Truy vấn: \"NiTi cable interwire friction\" OR \"superelastic NiTi wire rope contact\" OR \"Nitinol wire contact hysteresis\"\nTrạng thái: EXACT HISTORICAL (Từ các file truy vết B10, F07, F08, F09).",
            "Bài báo phát hiện: Reedlunn et al. (2013) [IJSS]; Carboni et al. (2015, 2016) [ASCE]; Fang et al. (2019).\nKết luận: Tiếp xúc ma sát giữa các sợi NiTi và trễ thắt (pinched hysteresis) kết hợp chuyển pha đã được nghiên cứu sâu sắc trong kết cấu giảm chấn.",
            "Bị loại bỏ: Bác bỏ C5. Hiện tượng cọ xát giữa các sợi NiTi không phải là phát hiện mới của MP1.\nLý do đổi từ khóa: Đã biết cáp NiTi có ma sát tiếp xúc, câu hỏi tiếp theo là: Cơ học uốn và các trạng thái trượt dính-trượt (stick-slip) được giải quyết thế nào?\nTừ khóa tiếp: \"wire rope bending stick slip stiffness\"."
        ),
        (
            "Group 5:\nBending & Stick-Slip Mechanics\n(Cơ học uốn & Trượt dính-trượt)",
            "Bất định: Khi bó dây/cáp bị uốn, độ cứng uốn thay đổi thế nào theo độ cong? Hiện tượng chuyển tiếp từ dính hoàn toàn sang trượt một phần và trượt toàn phần đã có mô hình chưa?\nÝ định: Tìm kiếm các mô hình giải tích và số về uốn cáp có ma sát.",
            "Truy vấn: \"wire rope bending stiffness\" AND \"interwire slip\" AND \"stick slip friction\"\nTrạng thái: EXACT HISTORICAL (Từ B12 Barsi 2025 và A5 Xin Liu 2004).",
            "Bài báo phát hiện: Xin Liu (2004) [MSc Thesis]; Barsi, Carboni & Lacarbonara (2025) [Eng. Struct.].\nKết luận: Xin Liu dùng bảng tra CableCAD; Barsi (2025) thiết lập chặn trên/chặn dưới độ cứng cho các trạng thái dính/trượt nhưng chưa giải trượt biến thiên cục bộ.",
            "Bị loại bỏ: Tuyên bố cho rằng cơ học uốn cáp có ma sát là mảnh đất hoàn toàn trống.\nLý do đổi từ khóa: Cần hiểu rõ vai trò của áp suất nén bên ngoài trong việc điều khiển lực tiếp xúc pháp tuyến giữa các sợi dây.\nTừ khóa tiếp: \"radial pressure cable friction bending\"."
        ),
        (
            "Group 6:\nPressure / Confinement / Contact\n(Áp suất giam giữ & Cơ học tiếp xúc)",
            "Bất định: Liệu áp suất giam giữ chủ động (active pressure) tác động từ bên ngoài có tạo ra một định luật vật lý hay cơ chế cơ học hoàn toàn mới hay không?\nÝ định: Tìm kiếm các công trình giải tích tiếp xúc cáp dưới áp suất nén hướng kính.",
            "Truy vấn: \"radial pressure cable bending\" OR \"external confinement pressure wire bundle contact\"\nTrạng thái: EXACT HISTORICAL (Từ B04 Tjahjanto et al. 2017).",
            "Bài báo phát hiện: Tjahjanto, Tyrberg & Mullins (2017) [ASME OMAE2017-62553].\nKết luận: Áp suất giam giữ chỉ đóng vai trò là điều kiện biên lực mặt (traction BC: sigma.n = -p.n). Hiệu ứng vòm hình học và màng đàn hồi làm suy giảm áp lực tiếp xúc (p != fn).",
            "Bị loại bỏ: Bác bỏ hoàn toàn luận điểm coi áp suất là \"cơ chế vật lý mới\". Hạ cấp C6 thành điều kiện biên thực nghiệm.\nLý do đổi từ khóa: Áp suất chỉ là tải trọng biên; câu hỏi là các mô hình cấu thành NiTi phi tuyến hiện hữu có tích hợp được điều kiện biên này không?\nTừ khóa tiếp: \"superelastic NiTi finite element contact pressure\"."
        ),
        (
            "Group 7:\nNiTi Constitutive + Contact Model\n(Mô hình cấu thành & Tiếp xúc NiTi)",
            "Bất định: Liệu việc kết hợp một mô hình cấu thành NiTi phi tuyến (như Souza hay Auricchio) với thuật toán tiếp xúc Coulomb bề mặt đã được thực hiện chưa?\nÝ định: Tìm kiếm các mô hình 3D FEA mô phỏng hành vi cơ học cáp NiTi có ma sát.",
            "Truy vấn: \"superelastic cable finite element friction\" OR \"NiTi UMAT wire rope contact\"\nTrạng thái: EXACT HISTORICAL (Từ B11 Kang 2020 và F10 Vahidi 2021/2022).",
            "Bài báo phát hiện: Kang et al. (2020) [J. Mech. Eng.]; Vahidi et al. (2021/2022) [MAMS].\nKết luận: Vahidi đã lập trình UMAT Souza kết hợp tiếp xúc Coulomb trong Abaqus để mô phỏng cáp xoắn NiTi (dù chỉ thực hiện dưới tải kéo dọc trục).",
            "Bị loại bỏ: Khẳng định rằng hiện nay chưa có công cụ mô hình hóa nào có thể mô tả đồng thời NiTi và tiếp xúc ma sát (H0b formulation exists in principle).\nLý do đổi từ khóa: Khung lý thuyết đã có, nhưng chưa từng được kiểm chứng thực nghiệm đối chứng trong bài toán uốn chịu áp suất. Cần tìm tài liệu về xác thực mô hình.\nTừ khóa tiếp: \"model validation locked parameter contact mechanics\"."
        ),
        (
            "Group 8:\nModel Validation & Model Discrimination\n(Xác thực & Phân biệt mô hình)",
            "Bất định: Trong các công trình trước, mô hình có được khóa tham số độc lập trước khi kiểm chứng không, hay tác giả tự do hiệu chỉnh tham số để khớp số liệu?\nÝ định: Tìm kiếm phương pháp phân biệt mô hình và xác thực thực nghiệm có kiểm soát.",
            "Truy vấn: \"model discrimination contact mechanics\" OR \"locked parameter validation NiTi\"\nTrạng thái: INFERRED METHODOLOGICAL KEYWORDS (Khớp với các khuyến nghị từ Astra Critique Remediation G06, G08, Stage 3).",
            "Bài báo phát hiện: Fang et al. (2019) và Silva et al. (2022).\nKết luận: Hiện tượng rò rỉ tham số (parameter compensation) rất nghiêm trọng nếu chỉ khớp đường cong vĩ mô; tự đốt nóng do nhiệt tiềm ẩn làm nhiễu trễ ma sát.",
            "Bị loại bỏ: Loại bỏ phương pháp so khớp đường cong tự do (unconstrained curve-fitting). Xác lập bài toán khoa học sống sót duy nhất: Model Discrimination.\nLý do đổi từ khóa: Đạt điểm đóng logic. Dừng tìm kiếm tổng quát; chuyển sang đóng giao thức trích dẫn (Citation Closure) và thiết lập Câu hỏi Nghiên cứu Cuối cùng."
        )
    ]
    
    for row_idx, row_content in enumerate(search_groups_data, start=1):
        row = table2.rows[row_idx]
        prevent_row_split(row)
        for col_idx, text_val in enumerate(row_content):
            cell = row.cells[col_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            
            lines = text_val.split('\n')
            for l_idx, line in enumerate(lines):
                if l_idx > 0:
                    p.add_run('\n')
                if any(line.startswith(prefix) for prefix in [
                    "Group", "Bất định:", "Ý định:", "Truy vấn:", "Trạng thái:",
                    "Bài báo phát hiện:", "Kết luận:", "Bị loại bỏ:", "Lý do đổi từ khóa:", "Từ khóa tiếp:"
                ]):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        rb = p.add_run(parts[0] + ":")
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                        rt = p.add_run(parts[1])
                        rt.font.name = 'Times New Roman'
                        rt.font.size = Pt(9.5)
                    else:
                        rb = p.add_run(line)
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                else:
                    rt = p.add_run(line)
                    rt.font.name = 'Times New Roman'
                    rt.font.size = Pt(9.5)

    p_spacer3 = doc.add_paragraph()
    p_spacer3.paragraph_format.space_after = Pt(6)

    # 4.2 Key Paper Impact Table
    add_custom_heading("4.2. Bảng Phân tích Tác động của 12 Bài báo Quyết định (Key Paper Impact Table)", level=2)
    add_p(
        "Không phải mọi bài báo trong y văn đều có sức nặng như nhau. Trong số 16 bài báo toàn văn của ma trận MP1-V002 và hàng trăm bài báo được sàng lọc qua trích dẫn, có 12 công trình then chốt đã trực tiếp làm thay đổi nhận thức, bác bỏ các giả định ban đầu và định hình nên hướng đi hiện tại của đề tài. Bảng 3 trình bày chi tiết từng bài báo, phương pháp, bằng chứng cụ thể và tác động mang tính quyết định của chúng, có cập nhật đầy đủ các đính chính khoa học mới nhất từ tài liệu S01 Formulation Crosswalk."
    )

    # Table 3: Key Paper Impact Table
    table3 = doc.add_table(rows=13, cols=6)
    table3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table3, color="B0B0B0", sz="4")
    
    headers_t3 = [
        "Bài báo (Paper ID & Metadata)",
        "Bài toán nghiên cứu & Hệ vật lý",
        "Kết quả cơ học then chốt liên quan MP1",
        "Tuyên bố MP1 bị đe dọa (Claim)",
        "Điều bị loại bỏ / Phạm vi còn lại",
        "Tác động thay đổi hướng nghiên cứu (Decision Impact)"
    ]
    
    hdr_row3 = table3.rows[0]
    make_row_header(hdr_row3)
    prevent_row_split(hdr_row3)
    for col_idx, h_text in enumerate(headers_t3):
        cell = hdr_row3.cells[col_idx]
        set_cell_shading(cell, "EAEAEA")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.bold = True

    key_papers_data = [
        (
            "Bai et al. (2022)\nPaper ID: 240fbf6022\nApp. Sci. 12(7), 3582\nDOI: 10.3390/app12073582",
            "Cơ cấu chấp hành mềm kẹp/uốn có thể tháo rời, ứng dụng cơ chế kẹt dây/sợi (wire jamming) dưới áp suất chân không. Hệ vật lý: Dây kim loại, dây nylon, dây gai.",
            "Chứng minh thực nghiệm rằng ma sát tiếp xúc trượt giữa các sợi dây kim loại hoặc polymer dưới áp suất hút chân không tạo ra khả năng điều chỉnh độ cứng uốn rõ rệt.",
            "Tuyên bố C1: \"Dùng dây/sợi kim loại ma sát để biến thiên độ cứng là tính mới khoa học của MP1\".",
            "Loại bỏ: Tuyên bố tính mới của cơ chế kẹt dây kim loại.\nCòn lại: Kẹt dây dưới áp suất dương chủ động.",
            "Tác động quyết định: Chấm dứt ý định tuyên bố \"phát minh ra cơ chế kẹt dây\". Bắt buộc phải tìm kiếm sự khác biệt ở vật liệu siêu đàn hồi và áp suất giam giữ dương."
        ),
        (
            "Liu et al. (2021)\nPaper ID: 182d854610\nIEEE RA-L 6(4), 7709-7716\nDOI: 10.1109/LRA.2021.3097255",
            "Cấu trúc biến thiên độ cứng ứng dụng trên robot mang mặc (wearable robots), sử dụng áp suất dương (positive pressure jamming) nén các hạt cản.",
            "Chứng minh áp suất dương lên đến 200 kPa trong buồng kín làm tăng đáng kể độ cứng chống uốn so với jamming chân không truyền thống (vốn bị giới hạn ở 100 kPa).",
            "Tuyên bố C2: \"Sử dụng áp suất dương để điều khiển độ cứng thông qua cơ chế kẹt là tính mới\".",
            "Loại bỏ: Tính mới của việc dùng áp suất dương trong jamming.\nCòn lại: Bó dây kim loại siêu đàn hồi chịu nén dương.",
            "Tác động quyết định: Bác bỏ việc lấy áp suất dương làm điểm tựa tính mới. Áp suất dương đã là kỹ thuật được công nhận rộng rãi trong cộng đồng robot mềm."
        ),
        (
            "Zhang & Yao (2026)\nPaper ID: 3aa8790db0\nMech. Sci. 17, 481-492\nDOI: 10.5194/ms-17-481-2026",
            "Chuỗi mềm đa hướng biến thiên độ cứng dựa trên kẹt bó sợi ma sát dưới áp suất dương (positive-pressure fiber jamming) lên đến 300 kPa.",
            "Mô hình hóa giải tích và đo đạc thực nghiệm các chế độ trượt dính-trượt (stick-slip regimes) và sự chuyển tiếp độ cứng uốn của bó sợi polymer chịu áp suất giam giữ.",
            "Tuyên bố C1, C2, C6: \"Kết hợp áp suất dương với bó sợi/dây ma sát uốn là đóng góp riêng của MP1\".",
            "Loại bỏ: Tính mới của kiến trúc bó sợi + áp suất dương + uốn.\nCòn lại: Bản chất phi tuyến chuyển pha của dây NiTi siêu đàn hồi.",
            "Tác động quyết định: Đây là mối đe dọa trực tiếp gần nhất về mặt kiến trúc. Nếu MP1 chỉ thay dây nylon bằng dây NiTi mà không chứng minh được sự khác biệt cơ học, đề tài sẽ sụp đổ thành một phép thế vật liệu tầm thường (trivial material substitution)."
        ),
        (
            "Takashima lineage (2020-2026)\nPaper IDs: 2cd907e77a, 7ce492505d, 99fe24da8b\nIEEE T-RO & RoMan",
            "Tích hợp dây hợp kim nhớ hình SMA (NiTi) với cơ chế kẹt hạt chân không trong các khớp nối robot mềm có thể biến thiên độ cứng và phục hồi hình dạng.",
            "Chứng minh sự hoạt động đồng thời của dây NiTi (phục hồi hình dạng, sinh lực kéo) và buồng jamming (khóa độ cứng) trong cùng một cơ cấu thiết bị mềm.",
            "Tuyên bố C3: \"Tích hợp vật liệu SMA và cơ chế jamming trong cùng một thiết bị robot mềm là mới\".",
            "Loại bỏ: Tính mới của việc kết hợp SMA và jamming ở cấp hệ thống.\nCòn lại: Bản thân dây NiTi là đối tượng ma sát cọ xát trực tiếp.",
            "Tác động quyết định: Bác bỏ toàn bộ các tuyên bố sáng chế thiết bị dạng \"SMA + Jamming\". Bắt buộc dây NiTi phải là môi trường kẹt (jamming medium) chứ không phải gân chấp hành phụ trợ."
        ),
        (
            "Huynh et al. (2022)\nPaper ID: bbe88a0c04\nScience Robotics 7(68)\nDOI: 10.1126/scirobotics.abq6388",
            "Bơm điện thủy động vi mô linh hoạt (flexible micropump) tích hợp trực tiếp trên robot mềm, tự tạo áp suất để kích hoạt cơ chế kẹt hạt không cần dây nối.",
            "Giải quyết hoàn toàn bài toán tích hợp nguồn áp suất nhỏ gọn (onboard/embedded pressure source) phục vụ điều khiển độ cứng cho robot mềm.",
            "Tuyên bố C4, C8: \"Nguồn tạo áp suất nhỏ gọn / piston tích hợp điều khiển jamming là tính mới của MP1\".",
            "Loại bỏ: Mọi tuyên bố tính mới xoay quanh bơm vi mô hay xilanh piston SMA.\nCòn lại: Thu hẹp hoàn toàn vào cơ học bó dây.",
            "Tác động quyết định: Chứng minh rằng việc gắn thêm xilanh piston SMA chỉ là một giải pháp thay thế phần cứng (hardware substitution). Toàn bộ nhánh phát triển nguồn áp bị cắt bỏ khỏi đóng góp khoa học."
        ),
        (
            "Reedlunn et al. (2013)\nPaper IDs: 00414aac4b, fac21c950e\nIJSS 50(20-21), 3209-3238\nDOI: 10.1016/j.ijsolstr.2013.06.011",
            "Đặc tính kéo, uốn và xoắn đẳng nhiệt của cáp hợp kim nhớ hình NiTi siêu đàn hồi (1x27 và 7x7). Khảo sát động học thanh Costello và tương tác tiếp xúc.",
            "Chỉ ra sai số phân kỳ của mô hình động học Costello ở góc xoắn dốc là do bỏ qua uốn/xoắn cục bộ của từng sợi; ở góc xoắn nông, cáp hành xử rất gần bó dây thẳng.",
            "Tuyên bố: \"Hành vi cơ học tiếp xúc và động học của bó/cáp nhiều sợi NiTi chưa từng được nghiên cứu\".",
            "Loại bỏ: Việc dùng sai số Costello của cáp xoắn để biện minh cho nhu cầu lý thuyết mới trên bó dây thẳng.\nCòn lại: Tác động của áp suất giam giữ chủ động.",
            "Tác động quyết định (Sửa đổi từ S01): Đính chính diễn giải cũ; không được suy diễn rằng Reedlunn đòi hỏi luật ghép vi mô mới cho bó dây thẳng. Thừa nhận động học cáp NiTi đã có nền tảng cơ học sâu sắc."
        ),
        (
            "Carboni et al. (2015, 2016)\nPaper IDs: d9966f2f5e, 40760daa02\nASCE J. Eng. Mech.\nDOI: 10.1061/(ASCE)EM.1943-7889.0000852",
            "Hiện tượng trễ thắt (pinched hysteresis) và tiêu tán năng lượng trong các cụm cáp Nitinol và thép dưới chuyển vị ngang, ứng dụng làm bộ hấp thụ dao động phi tuyến.",
            "Phân tích sự kết hợp giữa chuyển pha Martensite và ma sát tiếp xúc Coulomb giữa các sợi dây. (Bảng 4 PDF: S1a là cáp NiTi7 chịu kéo-uốn kết hợp; S2a là cáp thép thuần ma sát).",
            "Tuyên bố C5: \"Hiện tượng trễ và ma sát tiếp xúc kết hợp chuyển pha trong dây NiTi là phát hiện mới\".",
            "Loại bỏ: Nhận định sai cũ về cấu hình S2a (S2a là thép, không phải NiTi). Thừa nhận trễ tiếp xúc NiTi đã biết.\nCòn lại: Khảo sát uốn thuần túy dưới áp suất biến thiên.",
            "Tác động quyết định (Sửa đổi từ S01): Carboni chỉ nghiên cứu dưới điều kiện kéo-uốn kết hợp có lực căng dọc trục lớn (do ngàm khóa ngang). Khoảng trống uốn có kiểm soát áp suất hướng kính độc lập vẫn mở."
        ),
        (
            "Fang et al. (2019)\nPaper ID: 2f7fcf2f8f\nStructures 20, 20-30\nDOI: 10.1016/j.istruc.2019.03.003",
            "Mô hình hóa hành vi trễ phi tuyến và suy giảm độ cứng của cáp NiTi siêu đàn hồi chịu tải trọng chu kỳ, ứng dụng cho dây văng cầu và kết cấu chịu động đất.",
            "Chứng minh hiện tượng bù trừ tham số (parameter compensation): nhiều bộ tham số vật liệu và ma sát khác nhau có thể cho ra cùng một đường cong quan trắc lực vĩ mô.",
            "Tuyên bố: \"Chỉ cần khớp đường cong uốn vĩ mô là đủ chứng minh tính đúng đắn của mô hình cơ học\".",
            "Loại bỏ: Phương pháp so khớp tự do (unconstrained fitting).\nCòn lại: Bắt buộc áp dụng Quy tắc Khóa tham số độc lập (Locked Calibration Rule).",
            "Tác động quyết định: Thiết lập hàng rào phương pháp luận nghiêm ngặt: Mọi tham số cấu thành NiTi và hệ số ma sát phải được đo độc lập trên dây đơn trước khi nạp vào mô hình dự đoán bó dây."
        ),
        (
            "Vahidi et al. (2021/2022)\nPaper ID: 53200aa0c6\nMAMS 29(16), 2548-2560\nDOI: 10.1080/15376494.2021.1955313",
            "Mô hình phần tử hữu hạn 3D tường minh từng sợi dây (explicit-wire 3D FEA) cho cáp xoắn SMA đơn và kép, tích hợp luật cấu thành Souza và ma sát Coulomb (mu = 0.115).",
            "Mô phỏng thành công sự kết hợp giữa biến dạng chuyển pha NiTi và trượt ma sát tiếp xúc bề mặt dưới tải trọng kéo dọc trục bằng Abaqus UMAT.",
            "Tuyên bố: \"Cơ học tính toán hiện nay chưa có khung mô hình nào tích hợp được NiTi và ma sát tiếp xúc\".",
            "Loại bỏ: Luận điểm cho rằng H0b chưa từng tồn tại về mặt công thức.\nCòn lại: Kiểm chứng dự đoán uốn dưới áp suất giam giữ độc lập.",
            "Tác động quyết định (Sửa đổi từ S01): Sửa lỗi báo cáo cũ (báo cáo cũ ghi mô hình Auricchio và uốn; PDF thực tế dùng mô hình Souza và chỉ mô phỏng kéo). Vahidi chính là hiện thân mạnh nhất của H0b, là đối thủ khoa học trực tiếp của MP1."
        ),
        (
            "Barsi, Carboni & Lacarbonara (2025)\nPaper ID: 9f4295be23\nEng. Struct. 323, 119217\nDOI: 10.1016/j.engstruct.2024.119217",
            "Mô hình dầm biến dạng cắt tuyến tính hóa cho cáp xoắn thép ngắn chịu kéo, xoắn và uốn ngang, sử dụng biến dạng riêng (eigenstrain) để biểu diễn các trạng thái giới hạn.",
            "Thiết lập chặn trên độ cứng (dính hoàn toàn) và chặn dưới (trượt hoàn toàn). PDF không giải bài toán tiếp xúc Coulomb tiến triển cục bộ và không xét áp suất giam giữ điều khiển.",
            "Tuyên bố: \"Barsi et al. đã giải quyết đầy đủ bài toán trượt dính-trượt dưới áp suất thay đổi\".",
            "Loại bỏ: Sự ngộ nhận rằng bài toán cơ học uốn trượt dính-trượt đã được giải trọn vẹn.\nCòn lại: Mô hình hóa sự tiến triển trượt cục bộ phụ thuộc áp suất.",
            "Tác động quyết định (Sửa đổi từ S01): Đính chính triệt để so với worker report cũ. Barsi (2025) chỉ cung cấp các biên độ cứng chẩn đoán (diagnostic bounds), không phải là mô hình dự đoán phản ứng uốn biến thiên dưới áp suất."
        ),
        (
            "Tjahjanto, Tyrberg & Mullins (2017)\nPaper ID: ccdc1bb980\nASME OMAE2017-62553\n(No DOI verified in repo)",
            "Cơ học uốn của lõi cáp và chất độn trong cáp ngầm động lực học chịu uốn chu kỳ và áp suất giam giữ hướng kính 0.2 MPa tác dụng lên vỏ bọc ngoài.",
            "Chỉ ra rằng áp suất ngoài đi vào phương trình vi phân như một điều kiện biên lực mặt. Áp suất buồng p không đồng nhất với lực tiếp xúc pháp tuyến fn giữa các sợi do hiệu ứng vòm và màng.",
            "Tuyên bố C6: \"Áp suất buồng p nén trực tiếp bằng lực tiếp xúc pháp tuyến fn giữa các sợi dây\".",
            "Loại bỏ: Giả định giản đơn p = fn. Hạ cấp áp suất thành điều kiện biên thực nghiệm.\nCòn lại: Đo đạc và hiệu chuẩn chuỗi truyền áp lực p -> fn.",
            "Tác động quyết định (Sửa đổi từ S01): Đính chính tác giả là Jonathan Mullins. Khẳng định áp suất giam giữ không tạo ra vật lý mới; muốn đánh giá ma sát, bắt buộc phải giải bài toán truyền áp qua màng bọc."
        ),
        (
            "Silva et al. (2022)\nPaper ID: 6dd1ca94d1\nSensors 22(20), 8045\nDOI: 10.3390/s22208045",
            "Hành vi nhiệt-cơ và tuổi thọ mỏi của vi cáp hợp kim nhớ hình NiTi siêu đàn hồi dưới tải trọng động lực học chu kỳ. Đo đạc hiệu ứng tự đốt nóng (self-heating).",
            "Xác định nhiệt tiềm ẩn chuyển pha (10-25 J/g) làm dây tự nóng lên khi chịu tải chu kỳ nhanh, làm dịch chuyển ứng suất chuyển pha (6-8 MPa/degC), làm biến dạng vòng lặp trễ.",
            "Tuyên bố: \"Mọi hiện tượng suy giảm độ cứng và trễ đo được trong thí nghiệm uốn đều do ma sát tiếp xúc\".",
            "Loại bỏ: Việc bỏ qua yếu tố nhiệt độ; loại trừ nguy cơ quy kết sai hiện tượng nhiệt thành cơ học tiếp xúc.\nCòn lại: Bắt buộc khống chế tốc độ tải tựa tĩnh đẳng nhiệt.",
            "Tác động quyết định: Thiết lập điều kiện biên thực nghiệm: Thí nghiệm uốn MP1 bắt buộc phải thực hiện ở tốc độ chuẩn tựa tĩnh (quasi-static, <= 0.05 Hz) hoặc có đo nhiệt độ hồng ngoại để tránh hiện tượng nhiễu nhiệt (thermal confounding)."
        )
    ]
    
    for row_idx, row_content in enumerate(key_papers_data, start=1):
        row = table3.rows[row_idx]
        prevent_row_split(row)
        for col_idx, text_val in enumerate(row_content):
            cell = row.cells[col_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            
            lines = text_val.split('\n')
            for l_idx, line in enumerate(lines):
                if l_idx > 0:
                    p.add_run('\n')
                if any(line.startswith(prefix) for prefix in [
                    "Bai", "Liu", "Zhang", "Takashima", "Huynh", "Reedlunn", "Carboni", "Fang", "Vahidi", "Barsi", "Tjahjanto", "Silva",
                    "Paper ID:", "Tuyên bố", "Loại bỏ:", "Còn lại:", "Tác động quyết định"
                ]):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        rb = p.add_run(parts[0] + ":")
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                        rt = p.add_run(parts[1])
                        rt.font.name = 'Times New Roman'
                        rt.font.size = Pt(9.5)
                    else:
                        rb = p.add_run(line)
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                else:
                    rt = p.add_run(line)
                    rt.font.name = 'Times New Roman'
                    rt.font.size = Pt(9.5)

    p_spacer4 = doc.add_paragraph()
    p_spacer4.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # PHẦN 5: ÁP DỤNG QUY TẮC 5 WHY
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 5: ÁP DỤNG QUY TẮC 5 WHY ĐỂ TRUY NGƯỢC RESEARCH PROBLEM", level=1)
    
    add_p(
        "Quy tắc 5 Why thường được biết đến như một công cụ quản lý chất lượng để tìm nguyên nhân gốc rễ của lỗi sản phẩm. Tuy nhiên, trong nghiên cứu này, 5 Why được tái cấu trúc thành một phương pháp luận phản nghiệm triết học chặt chẽ. Xuất phát từ chủ đề ban đầu còn rộng và chứa nhiều giả định (\"Bó dây NiTi biến thiên độ cứng điều khiển bằng áp suất giam giữ\"), chúng tôi thực hiện đúng 5 tầng truy vấn WHY. Sau mỗi tầng, một giả định không đứng vững bị loại bỏ, phạm vi nghiên cứu hẹp lại, và một truy vấn tìm kiếm mới được kích hoạt."
    )

    five_whys_content = [
        (
            "WHY 1: Tại sao không thể đơn giản nghiên cứu \"Chế tạo robot mềm kẹt dây NiTi biến thiên độ cứng\"?",
            "Lập luận phản biện: Ý tưởng chế tạo một cánh tay robot mềm sử dụng cơ chế kẹt dây NiTi kết hợp áp suất thoạt nhìn rất hấp dẫn về mặt ứng dụng. Tuy nhiên, nếu xem đây là một đóng góp nghiên cứu khoa học, ta phải đặt câu hỏi: Bản thân việc kết hợp các linh kiện này lại với nhau có tạo ra tri thức mới hay không?",
            "Bằng chứng y văn đối chứng: Bai et al. (2022) đã công bố và chứng minh cơ chế kẹt dây kim loại; Liu et al. (2021) đã chứng minh kẹt bằng áp suất dương; Zhang & Yao (2026) đã kết hợp áp suất dương 300 kPa với bó sợi ma sát uốn; Takashima et al. (2020–2026) đã tích hợp dây SMA vào buồng kẹt; Huynh et al. (2022) đã tích hợp nguồn áp vi mô.",
            "Quyết định học thuật: Bác bỏ hoàn toàn tính mới ở cấp độ kiến trúc thiết bị (device-level novelty). Toàn bộ các tuyên bố C1, C2, C3, C4, C8 bị loại bỏ.",
            "Hệ quả thu hẹp: Không làm đề tài theo hướng chế tạo thiết bị robot mềm nói chung. Thu hẹp từ \"hệ thống robot mềm\" sang \"cơ học của bó dây\".",
            "Câu hỏi tìm kiếm kích hoạt: Bản thân bó dây kim loại siêu đàn hồi NiTi khi đóng vai trò là môi trường kẹt dưới áp suất có đặc tính cơ học nào chưa được y văn giải thích?",
            "Từ khóa kích hoạt: \"superelastic NiTi wire bundle contact\", \"NiTi interwire friction jamming\"."
        ),
        (
            "WHY 2: Tại sao phải chuyển hướng từ kiến trúc thiết bị (device architecture) sang lõi cơ học (mechanics core)?",
            "Lập luận phản biện: Tại sao không tiếp tục cải tiến cơ cấu chấp hành, ví dụ thiết kế một xilanh dẫn động bằng dây SMA nhỏ gọn hơn để tạo áp suất? Nếu làm như vậy, đóng góp của đề tài chỉ là thay thế một cơ cấu bơm sẵn có bằng một cơ cấu bơm khác (actuator substitution) hoặc thay sợi nylon của Zhang & Yao bằng sợi NiTi (material substitution). Đây là các giải pháp kỹ thuật thuần túy, không tạo ra tri thức cơ học mới.",
            "Bằng chứng y văn đối chứng: Zhang & Yao (2026) đã giải quyết trọn vẹn bài toán bó sợi đàn hồi dưới áp suất dương; Pierce & Mascaro (2013) và Wang et al. (2024) đã công bố các cơ cấu bơm và piston thu nhỏ dùng SMA.",
            "Quyết định học thuật: Từ bỏ toàn bộ nhánh phát triển nguồn áp suất SMA; chuyển 100% trọng tâm sang bài toán cơ học vật lý: Phân tích sự tương tác giữa tính chất siêu đàn hồi chuyển pha của NiTi, ma sát trượt giữa các sợi dây và áp suất giam giữ.",
            "Hệ quả thu hẹp: Định vị đề tài là một nghiên cứu Cơ học Ứng dụng (Applied Mechanics), xác lập 3 mục tiêu lõi: T1 (Tiếp xúc NiTi), T2 (Áp suất hướng kính), T3 (Ghép siêu đàn hồi và ma sát).",
            "Câu hỏi tìm kiếm kích hoạt: Cơ học tiếp xúc, ma sát và uốn của cáp/bó dây NiTi nhiều sợi đã được mô hình hóa và kiểm chứng thực nghiệm đến đâu trong các lĩnh vực kết cấu và giảm chấn?",
            "Từ khóa kích hoạt: \"NiTi cable bending stiffness\", \"superelastic wire rope interwire friction\", \"NiTi strand contact hysteresis\"."
        ),
        (
            "WHY 3: Tại sao không thể tuyên bố \"Sự cùng tồn tại của chuyển pha NiTi và ma sát giữa các sợi dây\" là tính mới?",
            "Lập luận phản biện: Khi uốn một bó dây NiTi, các sợi dây vừa trải qua quá trình chuyển pha tinh thể do ứng suất (stress-induced transformation) vừa cọ xát ma sát vào nhau. Liệu sự kết hợp này có phải là một hiện tượng vật lý hoàn toàn mới chưa từng ai biết đến?",
            "Bằng chứng y văn đối chứng: Reedlunn et al. (2013 Part I/II) đã đo đạc động học và kéo cáp NiTi nhiều sợi; Carboni et al. (2015, 2016) đã phân tích chi tiết trễ thắt (pinched hysteresis) kết hợp chuyển pha và ma sát Coulomb trong cáp Nitinol; Fang et al. (2019) đã mô hình hóa trễ cáp NiTi; Vahidi et al. (2021/2022) đã mô phỏng phần tử hữu hạn 3D cáp NiTi có ma sát tiếp xúc.",
            "Quyết định học thuật: Thừa nhận dứt khoát rằng sự kết hợp giữa chuyển pha NiTi và ma sát tiếp xúc là một hiện tượng cơ học đã được thiết lập (established phenomenon), không thể nhận làm phát minh riêng của MP1. Bác bỏ tuyên bố C5.",
            "Hệ quả thu hẹp: Đề tài không thể khẳng định mình là người đầu tiên phát hiện ra ma sát trong dây NiTi. Trọng tâm thu hẹp vào tác động điều khiển chủ động của áp suất giam giữ ngoài (active confinement pressure) lên phản ứng uốn.",
            "Câu hỏi tìm kiếm kích hoạt: Áp suất giam giữ tác động từ bên ngoài thay đổi lực tiếp xúc pháp tuyến và độ cứng uốn của bó dây/cáp như thế nào trong các mô hình cơ học hiện có?",
            "Từ khóa kích hoạt: \"radial pressure cable friction bending\", \"confinement pressure wire bundle\", \"cable bending internal friction pressure\"."
        ),
        (
            "WHY 4: Tại sao không thể tuyên bố \"Áp suất giam giữ chủ động (active positive pressure)\" là một nguyên lý cơ học mới?",
            "Lập luận phản biện: Liệu việc đưa áp suất khí nén p(t) vào buồng kín bao quanh bó dây có tạo ra một phương trình cấu thành cơ học mới hay làm thay đổi định luật ma sát của tự nhiên không?",
            "Bằng chứng y văn đối chứng: Tjahjanto et al. (2017) đã mô hình hóa cáp ngầm chịu uốn dưới áp suất ngoài 0.2 MPa và chỉ ra rằng áp suất ngoài đi vào phương trình vi phân cân bằng cơ học hoàn toàn tự nhiên dưới dạng điều kiện biên lực mặt (traction boundary condition: sigma.n = -p.n); Xin Liu (2004) đã dùng áp lực lớp để tính độ cứng uốn; Barsi et al. (2025) đã dùng giới hạn lực pháp tuyến để tính chặn độ cứng. Mặt khác, màng đàn hồi và hiệu ứng vòm làm suy giảm lực tiếp xúc thực tế (p != fn).",
            "Quyết định học thuật: Áp suất giam giữ chủ động chỉ là một điều kiện biên tải trọng ngoài (external traction boundary condition) phục vụ giao thức điều khiển thực nghiệm, không phải là một định luật vật lý mới. Hạ cấp C6 từ \"cơ chế vật lý mới\" thành điều kiện biên tải trọng.",
            "Hệ quả thu hẹp: Loại bỏ hoàn toàn lập luận \"áp suất tạo ra vật lý mới\". Trọng tâm chuyển sang đánh giá năng lực của các mô hình cơ học tiếp xúc và cấu thành NiTi hiện hữu trong việc dự đoán đáp ứng uốn dưới điều kiện biên áp suất này.",
            "Câu hỏi tìm kiếm kích hoạt: Liệu các mô hình cấu thành NiTi có xét chuyển pha kết hợp tiếp xúc Coulomb hiện hữu có đủ năng lực dự đoán phản ứng uốn phụ thuộc áp suất của bó dây hay không?",
            "Từ khóa kích hoạt: \"NiTi constitutive contact model validation\", \"superelastic cable finite element bending validation\", \"model discrimination contact mechanics\"."
        ),
        (
            "WHY 5: Vậy vấn đề khoa học thực sự chưa được giải quyết của MP1 là gì?",
            "Lập luận phản biện: Nếu kẹt dây đã biết, áp suất dương đã biết, SMA+jamming đã biết, ma sát trong dây NiTi đã biết, và áp suất chỉ là điều kiện biên, vậy đề tài này có còn lý do tồn tại không? Hay phải đóng lại hoàn toàn?",
            "Bằng chứng y văn đối chứng: Khi đối chiếu với hệ thống giả thuyết khoa học: (1) Mô hình thay thế đàn hồi sơ đẳng H0a (E = const) chắc chắn sai khi có chuyển pha; nhưng bác bỏ H0a không chứng minh được cần định luật mới H1. (2) Mô hình chuẩn đối thủ H0b (kết hợp luật cấu thành NiTi phi tuyến như Souza/Auricchio với tiếp xúc ma sát Coulomb trong 3D FEA) đã tồn tại về mặt nguyên lý công thức (S01 Formulation Crosswalk), nhưng các công trình trước (Vahidi 2022, Kang 2020) chỉ mô phỏng chịu kéo dọc trục, chưa từng có công trình nào kiểm chứng đối chứng thực nghiệm trong bài toán uốn dưới áp suất biến thiên với các tham số vật liệu và ma sát được khóa độc lập (locked calibration). (3) Giả thuyết H1 (cần một luật ghép cặp vi mô hoàn toàn mới) hoàn toàn chưa có bằng chứng thực nghiệm hay mô phỏng nào chứng minh sự cần thiết.",
            "Quyết định học thuật: Đóng góp khoa học duy nhất còn sống sót của MP1 không phải là sáng chế cơ cấu hay khám phá định luật mới, mà là xác lập một BÀI TOÁN PHÂN BIỆT MÔ HÌNH (MODEL-DISCRIMINATION PROBLEM): Đánh giá xem mô hình chuẩn đối thủ mạnh nhất H0b (với tham số được khóa độc lập) có đủ năng lực dự đoán đáp ứng uốn và các đại lượng cục bộ dưới áp suất giam giữ hay không, hay sẽ bộc lộ sai số hệ thống đòi hỏi một định luật ghép cặp mới.",
            "Hệ quả thu hẹp: Đây chính là điểm dừng logic cuối cùng. Đề tài được đóng băng thành một câu hỏi nghiên cứu cụ thể, trung lập, có thể phản nghiệm và đạt chuẩn học thuật.",
            "Câu hỏi tìm kiếm kích hoạt: Dừng tìm kiếm tổng quát; chuyển sang thiết lập giao thức khóa tham số và kiểm chứng thực nghiệm đối chứng.",
            "Từ khóa kích hoạt: \"locked calibration protocol\", \"held-out validation\", \"model discrimination\"."
        )
    ]

    for why_idx, (q, r, ev, dec, con, sq, sk) in enumerate(five_whys_content, start=1):
        add_p(f"{q}", bold_prefix=f"• Tầng {why_idx} — ")
        add_p(f"{r}", bold_prefix="   - Lập luận phản biện: ")
        add_p(f"{ev}", bold_prefix="   - Bằng chứng đối soát: ")
        add_p(f"{dec}", bold_prefix="   - Quyết định học thuật: ")
        add_p(f"{con}", bold_prefix="   - Hệ quả thu hẹp: ")
        add_p(f"{sq}", bold_prefix="   - Câu hỏi tìm kiếm nảy sinh: ")
        add_p(f"{sk}", bold_prefix="   - Từ khóa truy vấn tiếp theo: ")

    p_spacer5 = doc.add_paragraph()
    p_spacer5.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # PHẦN 6: QUÁ TRÌNH TIẾN HÓA CỦA ĐỀ TÀI (TOPIC EVOLUTION: V0 -> V4)
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 6: QUÁ TRÌNH TIẾN HÓA CỦA ĐỀ TÀI (TOPIC EVOLUTION)", level=1)
    
    add_p(
        "Nhờ việc áp dụng liên tục quy trình phản nghiệm bằng y văn và logic 5 Why, tên gọi và định nghĩa của đề tài MP1 đã trải qua 5 phiên bản tiến hóa rõ rệt (từ Topic V0 đến Topic V4). Bảng 4 làm sáng tỏ lý do tại sao cách diễn đạt ở phiên bản trước là chưa thỏa đáng về mặt khoa học, từ khóa tìm kiếm đã thay đổi như thế nào, và đề tài đã được tinh chỉnh ra sao để đạt tới phiên bản hiện tại."
    )

    # Table 4: Topic Evolution Table
    table4 = doc.add_table(rows=6, cols=5)
    table4.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table4, color="B0B0B0", sz="4")
    
    headers_t4 = [
        "Phiên bản Đề tài (Topic Version)",
        "Định nghĩa đề tài tại thời điểm đó (Wording)",
        "Lý do chưa thỏa đáng về mặt khoa học (Why scientifically insufficient)",
        "Truy vấn & Bằng chứng then chốt (Key Search & Evidence)",
        "Quyết định điều chỉnh sang phiên bản mới (Revised Direction)"
    ]
    
    hdr_row4 = table4.rows[0]
    make_row_header(hdr_row4)
    prevent_row_split(hdr_row4)
    for col_idx, h_text in enumerate(headers_t4):
        cell = hdr_row4.cells[col_idx]
        set_cell_shading(cell, "EAEAEA")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        r.font.bold = True

    topic_evolution_data = [
        (
            "Topic V0\n(Ý tưởng Mentor ban đầu)",
            "\"Phát triển cơ cấu robot mềm biến thiên độ cứng sử dụng bó dây NiTi giam giữ bằng áp suất dương kết hợp nguồn bơm xilanh SMA nhỏ gọn.\"",
            "Quá rộng, tập trung vào chế tạo máy; nhầm lẫn giữa tích hợp thiết bị và đóng góp khoa học; chứa nhiều giả định tính mới linh kiện chưa kiểm chứng.",
            "Truy vấn: \"variable stiffness soft robot\", \"wire jamming\"\nBằng chứng: Bai et al. (2022), Liu et al. (2021), Takashima et al. (2022), Huynh et al. (2022).",
            "Loại bỏ toàn bộ phần cứng xilanh SMA và các tuyên bố tính mới thiết bị. Chuyển sang nghiên cứu cơ học bó dây -> Hình thành Topic V1."
        ),
        (
            "Topic V1\n(Cơ học bó dây nén áp suất)",
            "\"Nghiên cứu cơ học của bó dây hợp kim nhớ hình NiTi siêu đàn hồi chịu giam giữ bằng áp suất.\"",
            "Vẫn quá rộng; chưa xác định rõ trạng thái chịu tải (kéo, nén, uốn hay xoắn?); chưa làm rõ hiện tượng ma sát cọ xát và chuyển pha đã được y văn nghiên cứu đến đâu.",
            "Truy vấn: \"NiTi wire bundle contact\", \"superelastic cable friction\"\nBằng chứng: Reedlunn et al. (2013), Carboni et al. (2015, 2016), Fang et al. (2019).",
            "Thừa nhận ma sát trong cáp NiTi đã được nghiên cứu. Giới hạn tải trọng vào bài toán biến dạng Uốn và cơ chế trượt dính-trượt -> Hình thành Topic V2."
        ),
        (
            "Topic V2\n(Cơ học uốn bó dây)",
            "\"Nghiên cứu cơ học uốn và biến thiên độ cứng của bó dây NiTi siêu đàn hồi dưới áp suất giam giữ điều khiển.\"",
            "Vẫn chưa đủ sâu; cơ học uốn của cáp nhiều sợi và tác động của áp suất hướng kính đã có các khung lý thuyết nền tảng trong ngành cáp kết cấu và cáp ngầm.",
            "Truy vấn: \"wire rope bending stiffness stick slip\", \"radial pressure cable\"\nBằng chứng: Xin Liu (2004), Tjahjanto et al. (2017), Barsi et al. (2025).",
            "Nhận diện áp suất chỉ là điều kiện biên lực mặt. Nhận diện tính mới không nằm ở uốn thông thường mà ở sự ghép cặp giữa chuyển pha và trượt ma sát -> Hình thành Topic V3."
        ),
        (
            "Topic V3\n(Hành vi ghép cặp chuyển pha - trượt)",
            "\"Mô hình hóa và thực nghiệm hành vi ghép cặp giữa chuyển pha siêu đàn hồi và trượt ma sát tiếp xúc trong bó dây NiTi dưới áp suất giam giữ.\"",
            "Có nguy cơ rơi vào bẫy ngộ nhận: cho rằng hiện tượng ghép cặp này bắt buộc cần một định luật cấu thành mới (H1), trong khi các mô hình 3D FEA hiện hữu có thể đã đủ sức giải thích.",
            "Truy vấn: \"superelastic cable finite element friction\", \"NiTi UMAT contact\"\nBằng chứng: Kang et al. (2020), Vahidi et al. (2021/2022), Astra Critique Remediation.",
            "Tách H0 thành H0a và H0b. Không khẳng định trước rằng cần định luật ghép cặp mới. Chuyển đề tài sang bài toán kiểm chứng phân biệt mô hình -> Hình thành Topic V4."
        ),
        (
            "Topic V4\n(Bài toán Phân biệt Mô hình)\n[Canonical Current]",
            "\"Bài toán phân biệt mô hình đối với phản ứng uốn phụ thuộc áp suất của bó dây NiTi siêu đàn hồi: Đánh giá tính thỏa đáng của khung lý thuyết cấu thành - tiếp xúc hiện hữu (H0b).\"",
            "Đã khắc phục hoàn toàn các nhược điểm trước: Định nghĩa rõ bài toán khoa học, trung lập, có thể phản nghiệm, không định kiến tính mới, bảo toàn tính liêm chính học thuật.",
            "Truy vấn: Targeted Citation Chasing Protocol (15/15 branches closed), S01 Formulation Crosswalk.\nBằng chứng: FINAL_ADJUDICATION.md (2026-09-26).",
            "Đạt trạng thái đóng băng đề tài học thuật chính thức (Frozen MSc Research Problem). Sẵn sàng chuyển giao sang so sánh hướng nghiên cứu với Mentor."
        )
    ]
    
    for row_idx, row_content in enumerate(topic_evolution_data, start=1):
        row = table4.rows[row_idx]
        prevent_row_split(row)
        for col_idx, text_val in enumerate(row_content):
            cell = row.cells[col_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            
            lines = text_val.split('\n')
            for l_idx, line in enumerate(lines):
                if l_idx > 0:
                    p.add_run('\n')
                if any(line.startswith(prefix) for prefix in [
                    "Topic", "Truy vấn:", "Bằng chứng:", "Phiên bản"
                ]):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        rb = p.add_run(parts[0] + ":")
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                        rt = p.add_run(parts[1])
                        rt.font.name = 'Times New Roman'
                        rt.font.size = Pt(9.5)
                    else:
                        rb = p.add_run(line)
                        rb.font.name = 'Times New Roman'
                        rb.font.size = Pt(9.5)
                        rb.font.bold = True
                else:
                    rt = p.add_run(line)
                    rt.font.name = 'Times New Roman'
                    rt.font.size = Pt(9.5)

    p_spacer6 = doc.add_paragraph()
    p_spacer6.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # PHẦN 7: CẤU TRÚC HỆ GIẢ THUYẾT H0a / H0b / H1
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 7: CẤU TRÚC HỆ GIẢ THUYẾT H0a / H0b / H1 VÀ TÍNH ĐỦ VỀ CÔNG THỨC", level=1)
    
    add_p(
        "Một trong những bước tiến quan trọng nhất về mặt phương pháp luận của đề tài MP1 là việc tái cấu trúc hệ giả thuyết khoa học. Trước đây, báo cáo sơ khởi mắc một lỗi ngụy biện logic nghiêm trọng: xem mô hình đàn hồi tuyến tính đơn giản là giả thuyết vô hiệu duy nhất, và cho rằng chỉ cần chứng minh mô hình này sai là mặc nhiên khẳng định ý tưởng của mình đúng. Sau khi tiếp thu phản biện khoa học độc lập của Astra và rà soát chuyên sâu S01, hệ giả thuyết đã được phân tách thành 3 tầng rành mạch:"
    )

    add_p(
        "1. Giả thuyết H0a (Naive Constant-Modulus Substitution): Dự đoán phản ứng uốn của bó dây bằng cách thế một mô-đun đàn hồi hằng số E = const vào phương trình cáp uốn đàn hồi cổ điển (như mô hình của Zhang & Yao 2026 hoặc Barsi et al. 2025).",
        bold_prefix="• "
    )
    add_p(
        "Trạng thái khoa học: ĐÃ BỊ BÁC BỎ TRONG MIỀN CHUYỂN PHA (REFUTED IN TRANSFORMATION REGIME). Khi độ cong uốn vượt qua ngưỡng kích hoạt chuyển pha biến dạng ngoài (outer fiber strain vượt quá 0.75%), mô-đun tiếp tuyến của NiTi biến thiên phi tuyến mạnh mẽ và hình thành vòng trễ vật liệu. Việc bác bỏ H0a là điều hiển nhiên và mang tính chất đối chiếu với một giả thuyết rơm (strawman hypothesis).",
        italic_prefix="   "
    )

    add_p(
        "2. Giả thuyết H0b (Established Transformation-Aware NiTi Model + Coulomb Contact): Dự đoán phản ứng uốn bằng cách kết hợp khung lý thuyết cấu thành NiTi phi tuyến chuẩn mực (như mô hình Souza-Auricchio đã tích hợp trong UMAT phần tử hữu hạn 3D) với cơ học tiếp xúc Coulomb bề mặt, chịu điều kiện biên lực mặt của áp suất giam giữ p(t).",
        bold_prefix="• "
    )
    add_p(
        "Trạng thái khoa học: CHƯA BỊ BÁC BỎ / ĐỐI THỦ CẠNH TRANH TRỰC TIẾP (NOT FALSIFIED / LIVE COMPETITOR). Các công trình của Vahidi et al. (2021/2022) và Kang et al. (2020) chứng minh rằng khung mô hình này hoàn toàn khả thi về mặt toán học và tính toán. H0b chính là bức tường thành khoa học vững chắc nhất mà đề tài MP1 phải đối đầu.",
        italic_prefix="   "
    )

    add_p(
        "3. Giả thuyết H1 (Novel Distinct Constitutive-Contact Coupling Law): Cho rằng sự tương tác vi cơ học giữa biến dạng chuyển pha tinh thể NiTi và hiện tượng trượt ma sát giữa các sợi dây tạo ra một hiệu ứng vật lý phi tuyến mới, khiến mô hình H0b thất bại trong việc dự đoán và bắt buộc phải bổ sung một định luật ghép cặp cấu thành - tiếp xúc mới.",
        bold_prefix="• "
    )
    add_p(
        "Trạng thái khoa học: CHƯA ĐỦ BẰNG CHỨNG (INSUFFICIENT EVIDENCE). Hiện nay trong toàn bộ y văn và dữ liệu mô phỏng chưa có bất kỳ bằng chứng thực nghiệm nào cho thấy H0b bị sụp đổ dưới điều kiện tham số bị khóa độc lập. H1 hiện chỉ tồn tại như một giả thuyết nghiên cứu tiềm năng.",
        italic_prefix="   "
    )

    add_p(
        "H0a sai KHÔNG ĐỒNG NGHĨA VỚI VIỆC H1 đúng (Rejection of H0a does not imply H1 is true)!",
        bold_prefix="Nguyên tắc logic bảo vệ sự liêm chính học thuật: "
    )
    add_p(
        "Việc một mô hình đàn hồi đơn giản (H0a) thất bại chỉ chứng minh rằng bó dây NiTi có tính phi tuyến vật liệu; nó hoàn toàn không chứng minh được rằng khoa học hiện nay thiếu định luật vật lý hay cần một phương trình mới. Trách nhiệm học thuật của người nghiên cứu là phải chứng minh được rằng mô hình chuẩn đối thủ mạnh nhất hiện nay (H0b) không đủ khả năng dự đoán trước khi được phép tuyên bố tính mới của H1."
    )

    add_p(
        "Về mặt công thức lý thuyết (in principle), các phương trình cơ học liên tục hiện hữu kết hợp mô hình NiTi 3D (UMAT), thuật toán tiếp xúc mặt - mặt (surface-to-surface contact) và điều kiện biên áp suất giam giữ tác dụng lên màng đàn hồi đã đủ hoàn chỉnh để mô tả bài toán. Khoảng trống khoa học thực sự của MP1 không nằm ở sự thiếu thốn về mặt công thức giải tích sơ cấp, mà nằm ở chỗ: Tính thỏa đáng dự đoán thực nghiệm (empirical predictive adequacy) của khung mô hình H0b dưới các tham số được đo đạc và khóa độc lập (locked parameters) chưa từng được kiểm chứng đối chứng trong bài toán uốn dưới áp suất thay đổi.",
        bold_prefix="Đánh giá tính đủ của công thức từ tài liệu S01 (Formulation Sufficiency): "
    )

    # -------------------------------------------------------------
    # PHẦN 8: BÀI TOÁN NGHIÊN CỨU VÀ CÂU HỎI NGHIÊN CỨU CUỐI CÙNG
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 8: BÀI TOÁN NGHIÊN CỨU VÀ CÂU HỎI NGHIÊN CỨU CUỐI CÙNG", level=1)
    
    add_p(
        "Để đảm bảo sự rành mạch tuyệt đối trong văn phong học thuật khi làm việc với Mentor và Hội đồng, chúng tôi phân định rõ ràng giữa Chủ đề nghiên cứu (Topic), Bài toán nghiên cứu (Research Problem), và Câu hỏi nghiên cứu (Research Question):"
    )

    add_p(
        "Chủ đề nghiên cứu (Research Topic): Đặc trưng cơ học uốn của bó dây hợp kim nhớ hình NiTi siêu đàn hồi dưới áp suất giam giữ điều khiển độc lập.",
        bold_prefix="1. "
    )
    add_p(
        "Bài toán nghiên cứu (Research Problem): Sự thiếu vắng các bằng chứng thực nghiệm đối chứng và mô phỏng được khóa tham số độc lập để biết liệu khung lý thuyết cấu thành NiTi phi tuyến và tiếp xúc ma sát Coulomb hiện hữu (H0b) có đủ khả năng dự đoán chính xác phản ứng uốn phụ thuộc áp suất và các đại lượng cục bộ trong miền cùng tồn tại trượt - chuyển pha hay không.",
        bold_prefix="2. "
    )
    add_p(
        "Câu hỏi nghiên cứu cuối cùng (Final Research Question): Câu hỏi được đóng băng chính thức dưới dạng song ngữ Anh - Việt, đảm bảo tính trung lập, có thể phản nghiệm và không áp đặt trước tính mới của H1:",
        bold_prefix="3. "
    )

    # Question Box in English and Vietnamese
    q_table = doc.add_table(rows=2, cols=1)
    q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(q_table, color="222222", sz="8")
    
    # English Cell
    c_en = q_table.rows[0].cells[0]
    set_cell_shading(c_en, "F4F4F4")
    set_cell_margins(c_en, top=100, bottom=100, left=150, right=150)
    p_en = c_en.paragraphs[0]
    p_en.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_en.paragraph_format.line_spacing = 1.25
    r_en_lbl = p_en.add_run("Final Research Question (English Form):\n")
    r_en_lbl.font.name = 'Times New Roman'
    r_en_lbl.font.size = Pt(12)
    r_en_lbl.font.bold = True
    r_en_lbl.font.color.rgb = RGBColor(0, 0, 0)
    r_en_txt = p_en.add_run(
        "\"Across a declared, experimentally accessible pressure-curvature-temperature domain in which inter-wire slip and stress-induced NiTi transformation coexist, can an established transformation-aware NiTi constitutive and frictional-contact model (H0b), calibrated independently and evaluated under locked parameters, adequately predict the pressure-dependent bending response, tangent stiffness, and relevant local observables of a superelastic NiTi wire bundle, or does predictive failure demonstrate that additional coupling physics (H1) is required?\""
    )
    r_en_txt.font.name = 'Times New Roman'
    r_en_txt.font.size = Pt(12)
    r_en_txt.font.italic = True

    # Vietnamese Cell
    c_vi = q_table.rows[1].cells[0]
    set_cell_shading(c_vi, "EFEFEF")
    set_cell_margins(c_vi, top=100, bottom=100, left=150, right=150)
    p_vi = c_vi.paragraphs[0]
    p_vi.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_vi.paragraph_format.line_spacing = 1.25
    r_vi_lbl = p_vi.add_run("Câu hỏi Nghiên cứu Cuối cùng (Bản dịch Tiếng Việt chuẩn mực):\n")
    r_vi_lbl.font.name = 'Times New Roman'
    r_vi_lbl.font.size = Pt(12)
    r_vi_lbl.font.bold = True
    r_vi_lbl.font.color.rgb = RGBColor(0, 0, 0)
    r_vi_txt = p_vi.add_run(
        "\"Trong một miền áp suất giam giữ – độ cong – nhiệt độ được xác định và khả thi về mặt thực nghiệm, nơi hiện tượng trượt giữa các dây và chuyển pha do ứng suất của NiTi cùng đồng thời xuất hiện, liệu một mô hình cấu thành NiTi có xét chuyển pha kết hợp với cơ học tiếp xúc ma sát hiện hữu (H0b), được hiệu chuẩn độc lập và khóa tham số trước khi đánh giá, có thể dự đoán đầy đủ đáp ứng uốn phụ thuộc áp suất, độ cứng tiếp tuyến và các đại lượng cục bộ liên quan của bó dây NiTi siêu đàn hồi hay không, hay sự thất bại của mô hình dự đoán sẽ chứng minh rằng bắt buộc phải bổ sung một định luật ghép cặp vật lý mới (H1)?\""
    )
    r_vi_txt.font.name = 'Times New Roman'
    r_vi_txt.font.size = Pt(12)
    r_vi_txt.font.italic = True

    p_spacer7 = doc.add_paragraph()
    p_spacer7.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # PHẦN 9: KẾT LUẬN VÀ KHUYẾN NGHỊ DÀNH CHO MENTOR
    # -------------------------------------------------------------
    add_custom_heading("PHẦN 9: KẾT LUẬN VÀ KHUYẾN NGHỊ DÀNH CHO MENTOR", level=1)
    
    add_p(
        "Qua toàn bộ tiến trình rà soát, phản nghiệm y văn và tái lập luận học thuật được trình bày ở trên, chúng tôi xin tóm lược các kết luận mang tính bản lề để báo cáo với Mentor như sau:"
    )

    add_p(
        "1. Tính mới cấp thiết bị đã bị triệt tiêu hoàn toàn (Broad device-level novelty is PREEMPTED): Các ý tưởng về kẹt dây kim loại, kẹt sợi dưới áp suất dương, kết hợp SMA với jamming và tích hợp bơm vi mô đều đã có các công trình độc lập đi trước công bố trên các tạp chí uy tín. Đề tài không được phép lấy việc chế tạo robot mềm làm đóng góp khoa học chính.",
        bold_prefix="• "
    )
    add_p(
        "2. Áp suất giam giữ không phải là nguyên lý vật lý mới (Pressure is NOT a new physical principle): Áp suất buồng p chỉ là điều kiện biên lực mặt tải trọng ngoài phục vụ giao thức điều khiển thực nghiệm. Lực tiếp xúc pháp tuyến fn thực tế giữa các sợi dây chịu sự suy giảm phi tuyến qua màng đàn hồi và hiệu ứng vòm hình học.",
        bold_prefix="• "
    )
    add_p(
        "3. Đóng góp còn sống sót là một bài toán phân biệt mô hình hẹp (Surviving contribution is a narrow model-discrimination question): Đề tài chuyển từ nỗ lực chứng minh một định luật mới sang việc thiết lập một phép thử thực nghiệm đối chứng nghiêm ngặt nhằm đánh giá năng lực dự đoán của khung mô hình hiện hữu H0b.",
        bold_prefix="• "
    )
    add_p(
        "4. Trạng thái đề tài MP1 là Khả thi nhưng có điều kiện (VIABLE BUT CONDITIONAL): Đề tài không bị giết chết trực tiếp (no direct kill found in protocol), nhưng đang bị khóa bởi 8 khoảng trống khoa học kỹ thuật nghiêm ngặt (GAP-01 đến GAP-08), trong đó trọng tâm là: tính khả thi của miền cùng tồn tại trượt - chuyển pha (coexistence feasibility), độ suy giảm áp suất (pressure transmission loss), sự thoái hóa thông tin của phép đo uốn vĩ mô (macroscopic degeneracy), hiện tượng bù trừ tham số (parameter compensation) và nhiễu do nhiệt tiềm ẩn (thermal confounding).",
        bold_prefix="• "
    )
    add_p(
        "5. Cảnh báo bắt buộc về trạng thái bao phủ trích dẫn (Citation Closure Caveat): Quy trình tra cứu trích dẫn hai chiều của đề tài MP1-V002 đã hoàn tất 100% điều kiện dừng theo giao thức (stop_condition.satisfied = true, với 15/15 nhánh trích dẫn xuôi/ngược hoàn thành ngày 25/09/2026). Tuy nhiên, chúng tôi khẳng định rõ ràng rằng: Việc đóng giao thức tra cứu y văn (protocol closure) chỉ có nghĩa là không tìm thấy công trình phủ quyết trực tiếp trong phạm vi tìm kiếm được thiết kế; ĐÂY HOÀN TOÀN KHÔNG PHẢI LÀ BẰNG CHỨNG TOÁN HỌC CHỨNG MINH RẰNG TOÀN BỘ KHOA HỌC THẾ GIỚI KHÔNG CÒN PRIOR ART TƯƠNG TỰ.",
        bold_prefix="• "
    )

    add_p(
        "Khuyến nghị chiến lược dành cho Mentor: Hướng nghiên cứu MP1 đã được tinh chỉnh thành một bài toán cơ học tiếp xúc chuẩn mực, có giá trị học thuật và tính liêm chính cao. Tuy nhiên, rủi ro thực thi thực nghiệm và rủi ro nhận diện cơ chế của MP1 là rất lớn do đòi hỏi các thiết bị đo vi mô cục bộ (như sợi quang FBG, tương quan ảnh số DIC và cảm biến nhiệt hồng ngoại) để bóc tách hiện tượng trượt khỏi chuyển pha. Chúng tôi khuyến nghị Mentor sử dụng bản báo cáo chi tiết này để làm cơ sở đối chiếu, so sánh trực tiếp độ tin cậy và rủi ro thực thi giữa đề tài MP1 và đề tài D1/M1 (Mô hình hóa giới hạn hợp lệ của dầm kẹt lớp chân không) trước khi đưa ra quyết định khóa đề tài luận văn thạc sĩ chính thức.",
        bold_prefix="Khuyến nghị chiến lược: "
    )

    # -------------------------------------------------------------
    # SƠ ĐỒ TIẾN TRÌNH THU HẸP (HÌNH 1)
    # -------------------------------------------------------------
    add_custom_heading("SƠ ĐỒ TIẾN TRÌNH THU HẸP PHẠM VI NGHIÊN CỨU", level=1)
    
    diagram_path = "docs/reports/figures/mp1_narrative_narrowing_diagram.png"
    if os.path.exists(diagram_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(diagram_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap_lbl = p_cap.add_run("Hình 1: ")
        r_cap_lbl.font.name = 'Times New Roman'
        r_cap_lbl.font.size = Pt(11)
        r_cap_lbl.font.bold = True
        r_cap_txt = p_cap.add_run("Sơ đồ tiến trình thu hẹp phạm vi nghiên cứu từ ý tưởng kiến trúc thiết bị ban đầu của Mentor đến bài toán phân biệt mô hình cơ học uốn có thể phản nghiệm của đề tài MP1.")
        r_cap_txt.font.name = 'Times New Roman'
        r_cap_txt.font.size = Pt(11)
        r_cap_txt.font.italic = True
    else:
        add_p("[Sơ đồ tiến trình thu hẹp đang được liên kết từ tệp hình ảnh docs/reports/figures/mp1_narrative_narrowing_diagram.png]")

    # -------------------------------------------------------------
    # TÀI LIỆU THAM KHẢO (REFERENCES)
    # -------------------------------------------------------------
    add_custom_heading("TÀI LIỆU THAM KHẢO (REFERENCES)", level=1)
    add_p(
        "Danh mục dưới đây bao gồm 15 công trình then chốt được trích dẫn trực tiếp trong báo cáo, đã được đối soát toàn văn và xác thực định danh chính xác từ kho dữ liệu repository:"
    )

    references_data = [
        "1. Bai, Y., et al. (2022). Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming. Applied Sciences, 12(7), 3582. DOI: 10.3390/app12073582",
        "2. Barsi, A., Carboni, B., & Lacarbonara, W. (2025). A new mechanical model of short wire ropes: Theory and experimental validation. Engineering Structures, 323, 119217. DOI: 10.1016/j.engstruct.2024.119217",
        "3. Carboni, B., Lacarbonara, W., & Auricchio, F. (2015). Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands. ASCE Journal of Engineering Mechanics, 141(11), 04015042. DOI: 10.1061/(ASCE)EM.1943-7889.0000852",
        "4. Carboni, B., & Lacarbonara, W. (2016). Nonlinear Vibration Absorber with Pinched Hysteresis. ASCE Journal of Engineering Mechanics, 142(7), 04016041. DOI: 10.1061/(ASCE)EM.1943-7889.0001072",
        "5. Fang, C., et al. (2019). Cyclic tensile behavior and hysteretic modeling of superelastic NiTi cables. Structures, 20, 20-30. DOI: 10.1016/j.istruc.2019.03.003",
        "6. Huynh, B. X., et al. (2022). Embedded flexible micropump for soft robotics. Science Robotics, 7(68), eabq6388. DOI: 10.1126/scirobotics.abq6388",
        "7. Kang, J., Wang, Z., Zhou, J., & Xue, X. (2020). Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables. Journal of Mechanical Engineering, 56(14), 65-73. DOI: 10.3901/JME.2020.14.065",
        "8. Liu, H., et al. (2021). A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots. IEEE Robotics and Automation Letters, 6(4), 7709-7716. DOI: 10.1109/LRA.2021.3097255",
        "9. Liu, Xin (2004). Cable Vibration Considering Internal Friction. MSc Thesis, Department of Mechanical Engineering, University of Hawaii at Manoa.",
        "10. Matsumoto, T., et al. (2021). Motion Evaluation of Variable Stiffness Robotic Link Driven by Shape Memory Alloy Wire and Jamming Transition. IEEE Transactions on Robotics / RoMan.",
        "11. Reedlunn, B., et al. (2013). Tension, bending, and twisting of superelastic shape memory alloy cables: Part I - Experimental results & Part II - Analytical modeling. International Journal of Solids and Structures, 50(20-21), 3209-3238. DOI: 10.1016/j.ijsolstr.2013.06.011",
        "12. Silva, M., et al. (2022). NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings. Sensors, 22(20), 8045. DOI: 10.3390/s22208045",
        "13. Takashima, K., et al. (2022). Variable-Stiffness Soft Robotic Link Integrating Shape Memory Alloy Actuation and Granular Jamming Mechanism. IEEE Robotics and Automation Letters.",
        "14. Tjahjanto, P. E., Tyrberg, A., & Mullins, Jonathan (2017). Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable. In Proceedings of the ASME 36th International Conference on Ocean, Offshore and Arctic Engineering (OMAE2017), Paper OMAE2017-62553.",
        "15. Vahidi, M., Arghavani, J., Choi, S. B., & Ostadrahimi, A. (2022). Mechanical response of single and double-helix SMA wire ropes. Mechanics of Advanced Materials and Structures, 29(16), 2548-2560. DOI: 10.1080/15376494.2021.1955313",
        "16. Zhang, Y., & Yao, J. (2026). A variable stiffness omnidirectional chain based on positive-pressure fiber jamming. Mechanical Sciences, 17, 481-492. DOI: 10.5194/ms-17-481-2026"
    ]

    for ref in references_data:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_ref.paragraph_format.line_spacing = 1.15
        p_ref.paragraph_format.space_after = Pt(4)
        p_ref.paragraph_format.left_indent = Inches(0.3)
        p_ref.paragraph_format.first_line_indent = Inches(-0.3)
        r_ref = p_ref.add_run(ref)
        r_ref.font.name = 'Times New Roman'
        r_ref.font.size = Pt(11)

    # -------------------------------------------------------------
    # Save Document
    # -------------------------------------------------------------
    output_dir = "docs/reports"
    os.makedirs(output_dir, exist_ok=True)
    output_docx_path = os.path.join(output_dir, "MP1_MENTOR_RESEARCH_NARROWING_REPORT_2026-09-26.docx")
    
    doc.save(output_docx_path)
    print(f"Report successfully built and saved to: {output_docx_path}")
    return output_docx_path

if __name__ == '__main__':
    create_report()
