#!/usr/bin/env python3
"""
scripts/batch_annotate_mp1.py

Batch PDF Annotation Pipeline with 12 Parallel Workers.
Highlights all 27 papers in data/final/MP1 according to JSON extraction schemas.
Ignores bibliographic metadata (title, authors, year, doi).
Maps each extracted field to a distinct color with line-merged highlights,
interactive popups, and a navigable bookmark outline hierarchy.
"""

import os
import sys
import glob
import json
import time
import re
import unicodedata
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import pymupdf


COLOR_PALETTE = {
    # Nhóm Câu hỏi nghiên cứu
    "research_problem": (0.95, 0.35, 0.35),          # Đỏ san hô (Coral Red)
    "research_objective": (1.00, 0.55, 0.10),        # Cam tươi (Bright Orange)
    # Nhóm Hệ thống/cơ chế
    "robot_type": (1.00, 0.88, 0.10),                # Vàng nghệ (Gold Yellow)
    "stiffness_mechanism": (0.60, 0.60, 0.20),       # Xanh ô liu (Olive)
    "actuation": (0.90, 0.72, 0.15),                 # Vàng hổ phách (Amber)
    # Nhóm Mô hình
    "modeling_methods": (0.65, 0.40, 0.88),          # Tím hoa cà (Violet Purple)
    "constitutive_assumptions": (0.82, 0.32, 0.82),  # Tím phong lan (Plum/Magenta)
    # Nhóm Các biến
    "independent_variables": (0.15, 0.78, 0.95),     # Xanh lơ (Cyan)
    "dependent_variables": (0.15, 0.52, 0.95),       # Xanh lam đậm (Dodger Blue)
    "control_variables": (0.12, 0.72, 0.65),         # Xanh mòng két (Teal)
    # Nhóm Thực nghiệm/đánh giá
    "experimental_setup": (0.62, 0.85, 0.18),        # Xanh nõn chuối (Lime Green)
    "performance_metrics": (0.18, 0.82, 0.48),       # Xanh bạc hà (Mint Green)
    "main_results": (0.15, 0.75, 0.25),              # Xanh lá cây đậm (Emerald Green)
    # Nhóm Bằng chứng liên quan
    "evidence_relevant_to_topic": (0.30, 0.45, 0.90),# Xanh hoàng gia (Royal Blue)
    # Nhóm Giới hạn
    "limitations_stated_by_authors": (0.95, 0.45, 0.35), # Cá hồi (Salmon Coral)
    "limitations_inferred": (0.95, 0.48, 0.68),      # Hồng cánh sen (Rose Pink)
    # Nhóm Hướng tiếp theo
    "future_work": (0.85, 0.22, 0.75),               # Tím hồng tươi (Fuchsia)
    "possible_gap_implications": (0.78, 0.38, 0.18), # Nâu gạch (Rust Orange)
}

FIELD_GROUPS = {
    "research_problem": "Câu hỏi nghiên cứu",
    "research_objective": "Câu hỏi nghiên cứu",
    "robot_type": "Hệ thống/cơ chế",
    "stiffness_mechanism": "Hệ thống/cơ chế",
    "actuation": "Hệ thống/cơ chế",
    "modeling_methods": "Mô hình",
    "constitutive_assumptions": "Mô hình",
    "independent_variables": "Các biến",
    "dependent_variables": "Các biến",
    "control_variables": "Các biến",
    "experimental_setup": "Thực nghiệm/đánh giá",
    "performance_metrics": "Thực nghiệm/đánh giá",
    "main_results": "Thực nghiệm/đánh giá",
    "evidence_relevant_to_topic": "Bằng chứng liên quan",
    "limitations_stated_by_authors": "Giới hạn",
    "limitations_inferred": "Giới hạn",
    "future_work": "Hướng tiếp theo",
    "possible_gap_implications": "Hướng tiếp theo",
}

IGNORE_FIELDS = {"title", "authors", "year", "doi", "confidence"}

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with",
    "by", "from", "up", "about", "into", "over", "after", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did", "that", "this",
    "these", "those", "it", "its", "they", "them", "their", "we", "us", "our", "as",
    "can", "could", "should", "would", "which", "where", "who", "whom", "whose"
}


def normalize_token(w):
    w = unicodedata.normalize("NFKD", w)
    return re.sub(r"[^a-zA-Z0-9]", "", w).lower()


def build_page_word_map(doc):
    page_data = []
    for page_idx in range(len(doc)):
        p = doc[page_idx]
        raw_words = p.get_text("words")
        merged = []
        i = 0
        while i < len(raw_words):
            w = raw_words[i]
            text = w[4]
            if text.endswith("-") and i + 1 < len(raw_words):
                next_w = raw_words[i + 1]
                merged.append(([w, next_w], text[:-1] + next_w[4]))
                i += 2
            else:
                merged.append(([w], text))
                i += 1
        cleaned = [normalize_token(item[1]) for item in merged]
        page_data.append({
            "page_idx": page_idx,
            "merged": merged,
            "cleaned": cleaned
        })
    return page_data


def merge_line_rects(rects):
    lines = []
    sorted_rects = sorted(rects, key=lambda r: (round(r.y0 / 3) * 3, r.x0))
    current_line = []
    for r in sorted_rects:
        if not current_line:
            current_line.append(r)
        else:
            last = current_line[-1]
            if abs(r.y0 - last.y0) < 4 and abs(r.y1 - last.y1) < 4:
                current_line.append(r)
            else:
                lines.append(current_line)
                current_line = [r]
    if current_line:
        lines.append(current_line)
    merged = []
    for line in lines:
        x0 = min(r.x0 for r in line)
        y0 = min(r.y0 for r in line)
        x1 = max(r.x1 for r in line)
        y1 = max(r.y1 for r in line)
        merged.append(pymupdf.Rect(x0, y0, x1, y1))
    return merged


def find_phrase_rects(words_subseq, p_info):
    cleaned = p_info["cleaned"]
    merged = p_info["merged"]
    target_clean = [normalize_token(w) for w in words_subseq if normalize_token(w)]
    if not target_clean:
        return []
    n = len(target_clean)
    for i in range(len(cleaned) - n + 1):
        if cleaned[i:i + n] == target_clean:
            rects = []
            for k in range(i, i + n):
                for w in merged[k][0]:
                    rects.append(pymupdf.Rect(w[:4]))
            return merge_line_rects(rects)
    return []


def extract_page_sentences(doc):
    page_sentences = []
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        blocks = page.get_text("blocks")
        for b in blocks:
            b_text = b[4].strip()
            b_text = re.sub(r"(\w+)-\s*\n\s*(\w+)", r"\1\2", b_text)
            b_text = re.sub(r"\s+", " ", b_text)
            s_list = re.split(r"(?<=[.!?])\s+", b_text)
            for s in s_list:
                s = s.strip()
                tokens = [normalize_token(w) for w in s.split() if normalize_token(w)]
                content_tokens = set(tokens) - STOP_WORDS
                if len(content_tokens) >= 3:
                    page_sentences.append({
                        "page_idx": page_idx,
                        "text": s,
                        "tokens": tokens,
                        "content_tokens": content_tokens
                    })
    return page_sentences


def match_claim(claim_text, page_sentences, min_score=0.20):
    claim_tokens = [normalize_token(w) for w in claim_text.split() if normalize_token(w)]
    claim_content = set(claim_tokens) - STOP_WORDS
    if not claim_content:
        return []
    scored = []
    for s_info in page_sentences:
        overlap = claim_content & s_info["content_tokens"]
        if overlap:
            score = len(overlap) / (len(claim_content) ** 0.55 * len(s_info["content_tokens"]) ** 0.45)
            if score >= min_score:
                scored.append((score, s_info))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:1]


def process_paper_worker(task_info):
    """
    Worker function executed by each of the 12 concurrent workers.
    """
    worker_id = task_info.get("worker_id", 0)
    paper_id = task_info["paper_id"]
    title = task_info["title"]
    pdf_path = task_info["pdf_path"]
    json_path = task_info["json_path"]
    output_pdf_path = task_info["output_pdf_path"]

    start_time = time.time()
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            jdata = json.load(f)
            paper_data = jdata.get("paper", jdata)

        doc = pymupdf.open(pdf_path)
        page_data = build_page_word_map(doc)
        page_sentences = extract_page_sentences(doc)

        total_annot = 0
        annotations_by_field = {}
        field_page_map = {}

        for field, val in paper_data.items():
            if field in IGNORE_FIELDS:
                continue
            color = COLOR_PALETTE.get(field, (1.0, 1.0, 0.0))
            group = FIELD_GROUPS.get(field, "Khác")
            annotations_by_field[field] = 0
            field_page_map[field] = set()

            items = val if isinstance(val, list) else [val]
            for it in items:
                claim = it.get("claim", str(it)) if isinstance(it, dict) else str(it)
                if not claim or len(claim.strip()) < 3:
                    continue

                popup_text = f"[{group}] {field}\n" + "-" * 40 + f"\nTrích xuất JSON:\n{claim}"

                # 1. Direct phrase search if short term
                rects = []
                matched_page = -1
                claim_words = claim.split()
                if len(claim_words) <= 7:
                    for p_idx, p_info in enumerate(page_data):
                        r = find_phrase_rects(claim_words, p_info)
                        if r:
                            rects = r
                            matched_page = p_idx
                            break

                # 2. Semantic sentence match if not found directly
                if not rects:
                    res = match_claim(claim, page_sentences)
                    if res:
                        score, s_info = res[0]
                        matched_page = s_info["page_idx"]
                        p_info = page_data[matched_page]
                        s_words = s_info["text"].split()
                        # Find best sub-window
                        for window_size in [len(s_words), 14, 10, 7]:
                            for start_w in range(max(1, len(s_words) - window_size + 1)):
                                chunk = s_words[start_w:start_w + window_size]
                                r = find_phrase_rects(chunk, p_info)
                                if r:
                                    rects = r
                                    break
                            if rects:
                                break

                # Apply annotation if rects found
                if rects and matched_page >= 0:
                    page = doc[matched_page]
                    annot = page.add_highlight_annot(rects)
                    annot.set_colors(stroke=color)
                    annot.set_info(
                        title=f"{field} ({group})",
                        content=popup_text
                    )
                    annot.update()
                    total_annot += 1
                    annotations_by_field[field] += 1
                    field_page_map[field].add(matched_page + 1)

        # Build Bookmarks / TOC
        groups_ordered = [
            ("Câu hỏi nghiên cứu", ["research_problem", "research_objective"]),
            ("Hệ thống/cơ chế", ["robot_type", "stiffness_mechanism", "actuation"]),
            ("Mô hình", ["modeling_methods", "constitutive_assumptions"]),
            ("Các biến", ["independent_variables", "dependent_variables", "control_variables"]),
            ("Thực nghiệm/đánh giá", ["experimental_setup", "performance_metrics", "main_results"]),
            ("Bằng chứng liên quan", ["evidence_relevant_to_topic"]),
            ("Giới hạn", ["limitations_stated_by_authors", "limitations_inferred"]),
            ("Hướng tiếp theo", ["future_work", "possible_gap_implications"]),
        ]

        toc = []
        for g_name, g_fields in groups_ordered:
            g_pages = []
            for gf in g_fields:
                g_pages.extend(field_page_map.get(gf, []))
            if not g_pages:
                continue
            min_page = min(g_pages)
            toc.append([1, f"📁 {g_name}", min_page])
            for gf in g_fields:
                if gf not in field_page_map or not field_page_map[gf]:
                    continue
                f_pages = sorted(list(field_page_map[gf]))
                f_min_page = f_pages[0]
                page_str = ", ".join(f"P.{p}" for p in f_pages)
                toc.append([2, f"🎯 {gf} ({page_str})", f_min_page])

        doc.set_toc(toc)
        os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
        doc.save(output_pdf_path)
        doc.close()

        elapsed = time.time() - start_time
        return {
            "status": "SUCCESS",
            "worker_id": worker_id,
            "paper_id": paper_id,
            "title": title,
            "output_pdf": output_pdf_path,
            "total_highlights": total_annot,
            "annotations_by_field": annotations_by_field,
            "elapsed_seconds": round(elapsed, 2)
        }
    except Exception as e:
        elapsed = time.time() - start_time
        return {
            "status": "FAILED",
            "worker_id": worker_id,
            "paper_id": paper_id,
            "title": title,
            "error": str(e),
            "elapsed_seconds": round(elapsed, 2)
        }


def collect_paper_pairs():
    manifest_path = "data/final/MP1/manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    paper_pairs = []
    for p in manifest.get("papers", []):
        pid = p["paper_id"]
        title = p["title"]
        pdf_copies = [
            c["destination"] for c in manifest.get("copies", [])
            if c["paper_id"] == pid and c["destination"].endswith(".pdf")
        ]
        if not pdf_copies:
            continue
        pdf_path = pdf_copies[0]
        dir_name = os.path.dirname(pdf_path)
        base_name = os.path.basename(pdf_path)[:-4]
        json_path = os.path.join(dir_name, f"{base_name}_{pid}.json")
        if not os.path.exists(json_path):
            found = glob.glob(f"data/final/MP1/**/{base_name}_{pid}.json", recursive=True)
            if found:
                json_path = found[0]

        if os.path.exists(pdf_path) and os.path.exists(json_path):
            output_name = f"{os.path.basename(pdf_path)[:-4]}_annotated.pdf"
            output_pdf_path = os.path.join("data/final/MP1/annotated", output_name)
            paper_pairs.append({
                "paper_id": pid,
                "title": title,
                "pdf_path": pdf_path,
                "json_path": json_path,
                "output_pdf_path": output_pdf_path
            })

    return paper_pairs


def main():
    parser = argparse.ArgumentParser(description="Bulk PDF annotator with 12 parallel workers.")
    parser.add_argument("--workers", type=int, default=12, help="Number of concurrent workers (default: 12)")
    args = parser.parse_args()

    paper_pairs = collect_paper_pairs()
    print(f"=== KHỞI CHẠY TIẾN TRÌNH TAKE NOTE HÀNG LOẠT (WORKERS={args.workers}) ===")
    print(f"Tổng số cặp file cần xử lý: {len(paper_pairs)} papers\n")

    tasks = []
    for idx, item in enumerate(paper_pairs):
        item["worker_id"] = (idx % args.workers) + 1
        tasks.append(item)

    start_total = time.time()
    results = []

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_paper_worker, t): t for t in tasks}
        completed_count = 0
        for future in as_completed(futures):
            completed_count += 1
            res = future.result()
            results.append(res)
            w_id = res.get("worker_id", "?")
            pid = res.get("paper_id", "")
            title = res.get("title", "")[:45]
            if res.get("status") == "SUCCESS":
                hl = res.get("total_highlights", 0)
                sec = res.get("elapsed_seconds", 0)
                print(f"[{completed_count:02d}/{len(tasks):02d}] Worker #{w_id:02d} | Paper {pid} | {hl:2d} highlights ({sec:.1f}s) | {title}")
            else:
                err = res.get("error", "")
                print(f"[{completed_count:02d}/{len(tasks):02d}] Worker #{w_id:02d} | Paper {pid} | FAILED: {err} | {title}")

    total_time = round(time.time() - start_total, 2)
    success_count = sum(1 for r in results if r.get("status") == "SUCCESS")
    total_highlights_all = sum(r.get("total_highlights", 0) for r in results if r.get("status") == "SUCCESS")

    print("\n" + "=" * 60)
    print(f"HOÀN TẤT TIẾN TRÌNH: {success_count}/{len(paper_pairs)} papers thành công trong {total_time}s.")
    print(f"Tổng số vị trí highlight đã tạo: {total_highlights_all:,} annotations.")
    print(f"Thư mục lưu kết quả: data/final/MP1/annotated/")
    print("=" * 60)

    # Save manifest index
    manifest_out = "data/final/MP1/annotated/annotation_manifest.json"
    with open(manifest_out, "w", encoding="utf-8") as f:
        json.dump({
            "total_papers": len(paper_pairs),
            "successful_papers": success_count,
            "total_highlights": total_highlights_all,
            "total_time_seconds": total_time,
            "worker_count": args.workers,
            "papers": sorted(results, key=lambda x: x.get("paper_id", ""))
        }, f, indent=2, ensure_ascii=False)

    print(f"Đã lưu chỉ mục kết quả: {manifest_out}")


if __name__ == "__main__":
    main()
