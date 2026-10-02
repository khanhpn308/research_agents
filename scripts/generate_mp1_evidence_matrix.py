#!/usr/bin/env python3
"""
generate_mp1_evidence_matrix.py
-------------------------------
Trích xuất dữ liệu từ toàn bộ các file evidence JSON trong data/final/MP1
theo khung trích xuất Phần 4 -> Phần 11 (EVIDENCE_JSON_FRAMEWORK_GUIDE_VI.md)
Triển khai xử lý song song với 12 workers.
Đầu ra: File Excel .xlsx với định dạng chuyên nghiệp.
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Đường dẫn gốc
WORKSPACE_DIR = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = WORKSPACE_DIR / "data" / "final" / "MP1"
OUTPUT_PATHS = [
    WORKSPACE_DIR / "docs" / "reports" / "MP1_EVIDENCE_EXTRACTION_MATRIX.xlsx",
    WORKSPACE_DIR / "outputs" / "reports" / "MP1_EVIDENCE_EXTRACTION_MATRIX.xlsx",
    WORKSPACE_DIR / "data" / "final" / "MP1" / "MP1_EVIDENCE_EXTRACTION_MATRIX.xlsx",
]

NUM_WORKERS = 12

def format_list_field(items, bullet=True):
    """Format danh sách các chuỗi thành chuỗi xuống dòng có gạch đầu dòng."""
    if not items:
        return ""
    if isinstance(items, str):
        return items
    cleaned = [str(x).strip() for x in items if str(x).strip()]
    if not cleaned:
        return ""
    if bullet:
        return "\n".join(f"• {x}" for x in cleaned)
    return ", ".join(cleaned)

def format_evidence_claims_summary(claims):
    """Format danh sách claims từ evidence_relevant_to_topic."""
    if not claims or not isinstance(claims, list):
        return ""
    lines = []
    for idx, c in enumerate(claims, 1):
        if not isinstance(c, dict):
            lines.append(f"[{idx}] {str(c)}")
            continue
        claim_text = c.get("claim", "").strip()
        ev_type = c.get("evidence_type", "").strip()
        pages = c.get("page_numbers", [])
        page_str = ", ".join(map(str, pages)) if pages else "N/A"
        prefix = f"[{idx}]"
        meta = []
        if ev_type:
            meta.append(f"Type: {ev_type}")
        if page_str != "N/A":
            meta.append(f"pp. {page_str}")
        meta_str = f" ({', '.join(meta)})" if meta else ""
        lines.append(f"• {prefix}{meta_str}: {claim_text}")
    return "\n".join(lines)

def process_single_evidence_file(file_path_str):
    """Worker task: Đọc và trích xuất thông tin từ một file evidence JSON."""
    file_path = Path(file_path_str)
    worker_id = os.getpid()
    
    try:
        with open(file_path, "rb") as f:
            raw_bytes = f.read()
            file_hash = hashlib.sha256(raw_bytes).hexdigest()
            data = json.loads(raw_bytes.decode("utf-8"))
        
        # Xác định relative path và step folder
        try:
            rel_path = file_path.relative_to(WORKSPACE_DIR)
        except ValueError:
            rel_path = file_path
            
        try:
            rel_to_mp1 = file_path.relative_to(EVIDENCE_DIR)
            step_folder = rel_to_mp1.parent.as_posix()
            if step_folder == ".":
                step_folder = "root"
        except ValueError:
            step_folder = file_path.parent.name
            
        source = data.get("source", {})
        model = data.get("model", "")
        usage = data.get("usage", {})
        paper = data.get("paper", {})
        
        paper_id = source.get("paper_id") or data.get("paper_id") or ""
        source_pdf = source.get("filename") or ""
        
        # Section 4: Model & Usage
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        total_tokens = usage.get("total_tokens", 0)
        thinking_tokens = usage.get("thinking_tokens", 0)
        cache_read_tokens = usage.get("cache_read_tokens", 0)
        usage_details = f"Prompt: {prompt_tokens:,} | Completion: {completion_tokens:,} | Thinking: {thinking_tokens:,} | Cache: {cache_read_tokens:,}"
        
        # Section 5: Bibliographic
        title = paper.get("title", "").strip()
        authors_raw = paper.get("authors", [])
        authors_str = format_list_field(authors_raw, bullet=False)
        year = str(paper.get("year", "")).strip()
        doi = str(paper.get("doi", "")).strip()
        
        # Section 6: Research problem & system
        research_problem = paper.get("research_problem", "").strip()
        research_objective = paper.get("research_objective", "").strip()
        robot_type = paper.get("robot_type", "").strip()
        stiffness_mechanism = format_list_field(paper.get("stiffness_mechanism", []))
        actuation = format_list_field(paper.get("actuation", []))
        
        # Section 7: Models & assumptions
        modeling_methods = format_list_field(paper.get("modeling_methods", []))
        constitutive_assumptions = format_list_field(paper.get("constitutive_assumptions", []))
        
        # Section 8: Variables
        independent_vars = format_list_field(paper.get("independent_variables", []))
        dependent_vars = format_list_field(paper.get("dependent_variables", []))
        control_vars = format_list_field(paper.get("control_variables", []))
        
        # Section 9: Experiments & results
        experimental_setup = format_list_field(paper.get("experimental_setup", []))
        performance_metrics = format_list_field(paper.get("performance_metrics", []))
        main_results = format_list_field(paper.get("main_results", []))
        
        # Section 10: Relevant evidence
        raw_claims = paper.get("evidence_relevant_to_topic", [])
        claims_count = len(raw_claims) if isinstance(raw_claims, list) else 0
        claims_summary = format_evidence_claims_summary(raw_claims)
        
        # Section 11: Limitations & future work
        limitations_stated = format_list_field(paper.get("limitations_stated_by_authors", []))
        limitations_inferred = format_list_field(paper.get("limitations_inferred", []))
        future_work = format_list_field(paper.get("future_work", []))
        gap_implications = format_list_field(paper.get("possible_gap_implications", []))
        confidence = str(paper.get("confidence", "")).strip()
        
        record = {
            "status": "SUCCESS",
            "file_path_str": str(rel_path),
            "step_folder": step_folder,
            "filename": file_path.name,
            "sha256": file_hash,
            "paper_id": paper_id,
            "source_pdf": source_pdf,
            "model": model,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "thinking_tokens": thinking_tokens,
            "cache_read_tokens": cache_read_tokens,
            "usage_details": usage_details,
            "title": title,
            "authors": authors_str,
            "year": year,
            "doi": doi,
            "research_problem": research_problem,
            "research_objective": research_objective,
            "robot_type": robot_type,
            "stiffness_mechanism": stiffness_mechanism,
            "actuation": actuation,
            "modeling_methods": modeling_methods,
            "constitutive_assumptions": constitutive_assumptions,
            "independent_variables": independent_vars,
            "dependent_variables": dependent_vars,
            "control_variables": control_vars,
            "experimental_setup": experimental_setup,
            "performance_metrics": performance_metrics,
            "main_results": main_results,
            "claims_count": claims_count,
            "claims_summary": claims_summary,
            "raw_claims": raw_claims,
            "limitations_stated_by_authors": limitations_stated,
            "limitations_inferred": limitations_inferred,
            "future_work": future_work,
            "possible_gap_implications": gap_implications,
            "confidence": confidence,
            "worker_pid": worker_id
        }
        return record
        
    except Exception as e:
        return {
            "status": "ERROR",
            "file_path_str": str(file_path),
            "error_msg": str(e),
            "worker_pid": worker_id
        }

def setup_sheet_style(ws, title_color="1F4E79"):
    """Thiết lập styling chuẩn cho worksheet openpyxl."""
    ws.views.sheetView[0].showGridLines = True
    
    # Định dạng header
    header_fill = PatternFill(start_color=title_color, end_color=title_color, fill_type="solid")
    header_font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    thin_border = Border(
        left=Side(style="thin", color="D9D9D9"),
        right=Side(style="thin", color="D9D9D9"),
        top=Side(style="thin", color="D9D9D9"),
        bottom=Side(style="thin", color="D9D9D9")
    )
    
    header_border = Border(
        left=Side(style="thin", color="FFFFFF"),
        right=Side(style="thin", color="FFFFFF"),
        top=Side(style="medium", color="1F4E79"),
        bottom=Side(style="medium", color="1F4E79")
    )

    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_alignment
        cell.border = header_border
        
    ws.row_dimensions[1].height = 36
    
    zebra_fill = PatternFill(start_color="F9FAFC", end_color="F9FAFC", fill_type="solid")
    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    body_font = Font(name="Arial", size=9.5)
    
    for row in range(2, ws.max_row + 1):
        ws.row_dimensions[row].height = None  # Auto height
        is_even = (row % 2 == 0)
        current_fill = zebra_fill if is_even else white_fill
        
        for col in range(1, ws.max_column + 1):
            cell = ws.cell(row=row, column=col)
            cell.font = body_font
            cell.border = thin_border
            if not cell.fill or cell.fill.fill_type is None:
                cell.fill = current_fill
            # Canh lề mặc định
            if col in [1, 4, 6]:  # STT, Year, ID
                cell.alignment = Alignment(horizontal="center", vertical="top")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

def adjust_column_widths(ws, min_w=10, max_w=55):
    """Tự động điều chỉnh độ rộng cột."""
    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        header_len = len(str(col[0].value or ""))
        for cell in col:
            val = str(cell.value or "")
            if "\n" in val:
                lines = val.split("\n")
                line_lens = [len(l) for l in lines]
                max_len = max(max_len, max(line_lens) if line_lens else 0)
            else:
                max_len = max(max_len, len(val))
        
        # Đặt độ rộng hợp lý
        target_w = max(header_len + 4, min(max_len + 3, max_w))
        target_w = max(target_w, min_w)
        ws.column_dimensions[col_letter].width = target_w

def build_excel_workbook(all_records):
    """Xây dựng file Excel hoàn chỉnh gồm 4 sheets."""
    wb = openpyxl.Workbook()
    
    # -------------------------------------------------------------
    # 1. Tách danh sách 27 bài báo duy nhất (canonical papers)
    # -------------------------------------------------------------
    unique_papers = {}
    for r in all_records:
        if r["status"] != "SUCCESS":
            continue
        pid = r["paper_id"]
        if pid and pid not in unique_papers:
            unique_papers[pid] = r
            
    sorted_papers = sorted(unique_papers.values(), key=lambda x: (x["year"], x["title"]))
    
    # Sheet 1: Ma trận trích xuất 27 bài báo (Sections 5-11, đã bỏ các cột vận hành model/token/độ tin cậy)
    ws1 = wb.active
    ws1.title = "Ma_tran_27_bai_bao"
    ws1.freeze_panes = "C2"
    
    ws1_headers = [
        "STT",
        "Tên bài báo (Title)",
        "Tác giả (Authors)",
        "Năm",
        "DOI",
        "Paper ID",
        "Vấn đề nghiên cứu (Research Problem)",
        "Mục tiêu nghiên cứu (Research Objective)",
        "Loại Robot / Kết cấu (Robot Type)",
        "Cơ chế thay đổi độ cứng (Stiffness Mechanism)",
        "Cơ cấu tác động (Actuation)",
        "Phương pháp mô hình hóa (Modeling Methods)",
        "Giả thiết cấu thành (Constitutive Assumptions)",
        "Biến độc lập (Independent Variables)",
        "Biến phụ thuộc (Dependent Variables)",
        "Biến kiểm soát (Control Variables)",
        "Thiết lập thí nghiệm (Experimental Setup)",
        "Chỉ số đánh giá (Performance Metrics)",
        "Kết quả chính (Main Results)",
        "Số Claims",
        "Bằng chứng liên quan (Evidence Relevant to Topic)",
        "Giới hạn tác giả nêu (Limitations - Authors)",
        "Giới hạn suy luận (Limitations - Inferred)",
        "Hướng phát triển tiếp theo (Future Work)",
        "Ý nghĩa Gap nghiên cứu (Gap Implications)"
    ]
    ws1.append(ws1_headers)
    
    for idx, p in enumerate(sorted_papers, 1):
        ws1.append([
            idx,
            p["title"],
            p["authors"],
            p["year"],
            p["doi"],
            p["paper_id"],
            p["research_problem"],
            p["research_objective"],
            p["robot_type"],
            p["stiffness_mechanism"],
            p["actuation"],
            p["modeling_methods"],
            p["constitutive_assumptions"],
            p["independent_variables"],
            p["dependent_variables"],
            p["control_variables"],
            p["experimental_setup"],
            p["performance_metrics"],
            p["main_results"],
            p["claims_count"],
            p["claims_summary"],
            p["limitations_stated_by_authors"],
            p["limitations_inferred"],
            p["future_work"],
            p["possible_gap_implications"]
        ])
    setup_sheet_style(ws1, title_color="1F4E79")
    adjust_column_widths(ws1, min_w=10, max_w=60)
    
    # Custom widths for sheet 1
    ws1.column_dimensions["A"].width = 6   # STT
    ws1.column_dimensions["B"].width = 40  # Title
    ws1.column_dimensions["C"].width = 25  # Authors
    ws1.column_dimensions["D"].width = 8   # Year
    ws1.column_dimensions["E"].width = 26  # DOI
    ws1.column_dimensions["F"].width = 14  # Paper ID
    
    # -------------------------------------------------------------
    # Sheet 2: Chi tiết các phát biểu bằng chứng (Claims - Section 10)
    # -------------------------------------------------------------
    ws2 = wb.create_sheet(title="Chi_tiet_Claims_Phan_10")
    ws2.freeze_panes = "D2"
    ws2_headers = [
        "STT",
        "Tên bài báo (Title)",
        "Paper ID",
        "Năm",
        "Claim #",
        "Nội dung phát biểu bằng chứng (Claim Statement)",
        "Loại bằng chứng (Evidence Type)",
        "Số trang trong PDF (Page Numbers)",
        "DOI"
    ]
    ws2.append(ws2_headers)
    
    claim_stt = 1
    for p in sorted_papers:
        raw_claims = p.get("raw_claims", [])
        if not raw_claims:
            continue
        for c_idx, c in enumerate(raw_claims, 1):
            if isinstance(c, dict):
                ctext = c.get("claim", "")
                ctype = c.get("evidence_type", "")
                cpages = ", ".join(map(str, c.get("page_numbers", [])))
            else:
                ctext = str(c)
                ctype = "unspecified"
                cpages = ""
                
            ws2.append([
                claim_stt,
                p["title"],
                p["paper_id"],
                p["year"],
                c_idx,
                ctext,
                ctype,
                cpages,
                p["doi"]
            ])
            claim_stt += 1
            
    setup_sheet_style(ws2, title_color="2E5B82")
    adjust_column_widths(ws2, min_w=10, max_w=70)
    ws2.column_dimensions["A"].width = 6
    ws2.column_dimensions["B"].width = 38
    ws2.column_dimensions["C"].width = 14
    ws2.column_dimensions["D"].width = 8
    ws2.column_dimensions["E"].width = 10
    ws2.column_dimensions["F"].width = 65
    ws2.column_dimensions["G"].width = 18
    ws2.column_dimensions["H"].width = 16
    ws2.column_dimensions["I"].width = 24
    
    # -------------------------------------------------------------
    # Sheet 3: Từ điển trường trích xuất (Tu_dien_trich_xuat - Phần 5 đến 11, đã bỏ Phần 4)
    # -------------------------------------------------------------
    ws3 = wb.create_sheet(title="Tu_dien_trich_xuat")
    ws3_headers = [
        "Phần",
        "Nhóm trường",
        "Tên trường JSON",
        "Kiểu dữ liệu",
        "Ý nghĩa và Câu hỏi giúp trả lời",
        "Lưu ý phương pháp luận & Cảnh báo khoa học"
    ]
    ws3.append(ws3_headers)
    
    guide_rows = [
        # Phần 5
        ["Phần 5", "Thông tin thư mục", "title", "Chuỗi", "Tên bài báo khoa học", "Dùng để đối chiếu và xác nhận danh mục."],
        ["Phần 5", "Thông tin thư mục", "authors", "Danh sách", "Danh sách đầy đủ các tác giả", "Giúp truy nguyên nhóm nghiên cứu và citation network."],
        ["Phần 5", "Thông tin thư mục", "year", "Chuỗi", "Năm công bố chính thức", "Phân biệt online-first và năm issue; không lấy năm từ filename."],
        ["Phần 5", "Thông tin thư mục", "doi", "Chuỗi", "Mã định danh số học DOI", "DOI rỗng không khẳng định bài không có DOI; cần kiểm tra chéo."],
        
        # Phần 6
        ["Phần 6", "Vấn đề & Hệ thống", "research_problem", "Chuỗi", "Vấn đề hoặc hạn chế bài muốn xử lý (Vì sao cần nghiên cứu?)", "Phân biệt vấn đề tác giả nêu với điều tác giả thực sự làm."],
        ["Phần 6", "Vấn đề & Hệ thống", "research_objective", "Chuỗi", "Mục tiêu cụ thể của bài (Tác giả định làm gì?)", "Xác định ranh giới mục tiêu nghiên cứu."],
        ["Phần 6", "Vấn đề & Hệ thống", "robot_type", "Chuỗi", "Loại robot hoặc cấu trúc ứng dụng", "Hệ được nghiên cứu hoặc ứng dụng vào đâu."],
        ["Phần 6", "Vấn đề & Hệ thống", "stiffness_mechanism", "Danh sách", "Cơ chế tạo hoặc thay đổi độ cứng (Vì sao độ cứng đổi?)", "CƠ CHẾ ĐỘ CỨNG KHÁC CƠ CẤU TÁC ĐỘNG. Ví dụ: friction vs khí nén."],
        ["Phần 6", "Vấn đề & Hệ thống", "actuation", "Danh sách", "Cách tác động/điều khiển hệ (Hệ được kích hoạt bằng gì?)", "Không coi là từ đồng nghĩa với stiffness_mechanism."],
        
        # Phần 7
        ["Phần 7", "Mô hình & Giả thiết", "modeling_methods", "Danh sách", "Danh sách phương pháp mô hình hóa (analytical, FEM, phenomenological...)", "Cần phân biệt closed-form formulation với numerical fitting."],
        ["Phần 7", "Mô hình & Giả thiết", "constitutive_assumptions", "Danh sách", "Giả thiết ứng xử vật liệu/cơ học (đàn hồi tuyến tính, NiTi, Coulomb...)", "Có thể bị trộn lẫn kinematic assumption; cần tách material law và contact law."],
        
        # Phần 8
        ["Phần 8", "Ba nhóm biến", "independent_variables", "Danh sách", "Các biến chủ động thay đổi (ví dụ: áp suất, mức uốn)", "Cùng 1 đại lượng có thể là independent ở bài này nhưng control ở bài khác."],
        ["Phần 8", "Ba nhóm biến", "dependent_variables", "Danh sách", "Đại lượng đáp ứng được đo/tính (ví dụ: lực, độ cứng, trượt)", "Đo đại lượng gì khác với tiêu chí đánh giá performance."],
        ["Phần 8", "Ba nhóm biến", "control_variables", "Danh sách", "Yếu tố giữ cố định để so sánh công bằng (vật liệu, chiều dài, nhiệt độ)", "Rất quan trọng để đánh giá tính hợp lệ của thí nghiệm."],
        
        # Phần 9
        ["Phần 9", "Thí nghiệm & Kết quả", "experimental_setup", "Danh sách", "Mẫu, apparatus, cảm biến, gá kẹp và cách tạo tải", "Xác định rõ calibration apparatus vs validation apparatus."],
        ["Phần 9", "Thí nghiệm & Kết quả", "performance_metrics", "Danh sách", "Tiêu chí đánh giá (độ cứng, sai số dự đoán, năng lượng tiêu tán)", "Tiêu chí định lượng dùng để kết luận thành công."],
        ["Phần 9", "Thí nghiệm & Kết quả", "main_results", "Danh sách", "Những kết quả chính được trích xuất từ bài", "Không suy từ main_results là đã có independent experimental validation."],
        
        # Phần 10
        ["Phần 10", "Bằng chứng liên quan", "evidence_relevant_to_topic.claim", "Chuỗi", "Phát biểu cụ thể được rút từ nguồn liên quan câu hỏi nghiên cứu", "Có thể là background bài trích dẫn lại; cần kiểm tra primary vs secondary."],
        ["Phần 10", "Bằng chứng liên quan", "evidence_relevant_to_topic.evidence_type", "Chuỗi", "Loại hỗ trợ: experimental / analytical / numerical / background", "Phân loại mức độ chứng cứ vật lý hay giải tích."],
        ["Phần 10", "Bằng chứng liên quan", "evidence_relevant_to_topic.page_numbers", "Danh sách", "Danh sách trang để truy ngược PDF", "Phân biệt printed page và PDF page count khi cite."],
        
        # Phần 11
        ["Phần 11", "Giới hạn & Suy luận", "limitations_stated_by_authors", "Danh sách", "Giới hạn được ghi là do tác giả trực tiếp nêu", "Cần kiểm tra đúng văn cảnh và phạm vi trong bài."],
        ["Phần 11", "Giới hạn & Suy luận", "limitations_inferred", "Danh sách", "Giới hạn do người/model phân tích suy ra", "KHÔNG GÁN THÀNH KẾT LUẬN CỦA TÁC GIẢ."],
        ["Phần 11", "Giới hạn & Suy luận", "future_work", "Danh sách", "Hướng nghiên cứu tiếp theo được trích xuất", "Future work năm trước không chứng minh vấn đề vẫn mở hiện nay."],
        ["Phần 11", "Giới hạn & Suy luận", "possible_gap_implications", "Danh sách", "Suy luận ảnh hưởng đối với gap đề tài", "KHÔNG PHẢI BẰNG CHỨNG XÁC NHẬN NOVELTY."],
        ["Phần 11", "Giới hạn & Suy luận", "confidence", "Chuỗi", "Mức tự đánh giá độ tin cậy trích xuất", "Không phải confidence đề tài mới; không bảo đảm trích xuất không sai."]
    ]
    
    for row in guide_rows:
        ws3.append(row)
        
    setup_sheet_style(ws3, title_color="23496D")
    adjust_column_widths(ws3, min_w=12, max_w=65)
    ws3.column_dimensions["A"].width = 12
    ws3.column_dimensions["B"].width = 22
    ws3.column_dimensions["C"].width = 30
    ws3.column_dimensions["D"].width = 14
    ws3.column_dimensions["E"].width = 45
    ws3.column_dimensions["F"].width = 50
    
    return wb

def main():
    print("=" * 70)
    print("KHỞI TẠO TIẾN TRÌNH TRÍCH XUẤT EVIDENCE MATRIX MP1")
    print(f"Số lượng worker triển khai song song: {NUM_WORKERS}")
    print(f"Thư mục dữ liệu nguồn: {EVIDENCE_DIR}")
    print("=" * 70)
    
    # Quét tất cả các file evidence JSON
    all_json_files = []
    for root, dirs, files in os.walk(EVIDENCE_DIR):
        for f in files:
            if f.endswith(".json") and f != "manifest.json" and not f.endswith("annotation_manifest.json"):
                all_json_files.append(os.path.join(root, f))
                
    total_files = len(all_json_files)
    print(f"Tìm thấy tổng cộng: {total_files} file evidence JSON trong MP1.")
    
    if total_files == 0:
        print("LỖI: Không tìm thấy file JSON nào!")
        sys.exit(1)
        
    start_time = time.time()
    results = []
    
    # Triển khai 12 workers qua ProcessPoolExecutor
    print(f"\n>>> Bắt đầu xử lý {total_files} file với 12 worker processes...")
    with ProcessPoolExecutor(max_workers=NUM_WORKERS) as executor:
        future_to_file = {executor.submit(process_single_evidence_file, f): f for f in all_json_files}
        
        completed_count = 0
        for future in as_completed(future_to_file):
            res = future.result()
            results.append(res)
            completed_count += 1
            if completed_count % 50 == 0 or completed_count == total_files:
                print(f"  [Tiến độ: {completed_count}/{total_files} file ({completed_count/total_files*100:.1f}%)]")
                
    elapsed_time = time.time() - start_time
    print(f"\n>>> Hoàn thành trích xuất {total_files} file trong {elapsed_time:.2f} giây!")
    
    # Kiểm tra kết quả
    successful_count = sum(1 for r in results if r["status"] == "SUCCESS")
    error_count = sum(1 for r in results if r["status"] == "ERROR")
    unique_pids = set(r["paper_id"] for r in results if r["status"] == "SUCCESS" and r.get("paper_id"))
    
    print(f"  - Thành công: {successful_count}")
    print(f"  - Lỗi: {error_count}")
    print(f"  - Số bài báo duy nhất (Unique Papers): {len(unique_pids)}")
    
    # Xây dựng file Excel
    print("\n>>> Đang tổng hợp và định dạng workbook Excel (4 sheets)...")
    wb = build_excel_workbook(results)
    
    # Lưu ra các đường dẫn đích
    for out_p in OUTPUT_PATHS:
        out_p.parent.mkdir(parents=True, exist_ok=True)
        wb.save(str(out_p))
        print(f"  [V] Đã lưu file Excel thành công: {out_p}")
        
    print("\n" + "=" * 70)
    print("HOÀN TẤT TÁC VỤ XÂY DỰNG EVIDENCE MATRIX EXCEL!")
    print("=" * 70)

if __name__ == "__main__":
    main()
