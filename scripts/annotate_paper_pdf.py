#!/usr/bin/env python3
"""
scripts/annotate_paper_pdf.py

Tool for highlighting scientific papers (PDF) based on extraction JSON schemas.
Ignores bibliographic fields (title, authors, year, doi) and maps each scientific
field to a distinct color with multi-line text highlighting, PDF bookmark TOC,
and hoverable annotation popups containing extracted evidence.
"""

import os
import sys
import json
import re
import unicodedata
import argparse
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


def build_page_word_map(doc):
    """
    Extracts words from each page and merges hyphenated words across linebreaks
    to ensure 100% robust substring searching regardless of PDF layout.
    """
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
        cleaned = [
            re.sub(r"[^a-zA-Z0-9]", "", unicodedata.normalize("NFKD", item[1])).lower()
            for item in merged
        ]
        page_data.append({
            "page_idx": page_idx,
            "merged": merged,
            "cleaned": cleaned
        })
    return page_data


def merge_line_rects(rects):
    """
    Merges individual word bounding boxes that reside on the same line
    into a continuous, professional highlight rectangle.
    """
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


def find_phrase(target_phrase, page_data):
    """
    Searches for an exact normalized phrase within pre-processed page word maps.
    Returns a list of (page_idx, [merged_line_rects]).
    """
    target_clean = [
        re.sub(r"[^a-zA-Z0-9]", "", unicodedata.normalize("NFKD", w)).lower()
        for w in target_phrase.split()
        if re.sub(r"[^a-zA-Z0-9]", "", w)
    ]
    if not target_clean:
        return []
    n = len(target_clean)
    all_matches = []
    for p_info in page_data:
        cleaned = p_info["cleaned"]
        merged = p_info["merged"]
        for i in range(len(cleaned) - n + 1):
            if cleaned[i:i + n] == target_clean:
                rects = []
                for k in range(i, i + n):
                    for w in merged[k][0]:
                        rects.append(pymupdf.Rect(w[:4]))
                merged_line_rects = merge_line_rects(rects)
                all_matches.append((p_info["page_idx"], merged_line_rects))
    return all_matches


def annotate_paper_pdf(pdf_path, json_path, output_pdf_path, phrase_map):
    """
    Performs PDF annotation based on JSON paper metadata and explicit phrase mappings.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        paper_data = json_data.get("paper", json_data)

    doc = pymupdf.open(pdf_path)
    page_data = build_page_word_map(doc)

    total_highlights = 0
    annotations_by_field = {}
    field_page_map = {}

    for field, phrases in phrase_map.items():
        if field in IGNORE_FIELDS:
            continue
        color = COLOR_PALETTE.get(field, (1.0, 1.0, 0.0))
        group = FIELD_GROUPS.get(field, "Khác")
        annotations_by_field[field] = 0
        field_page_map[field] = set()

        # Format popup note
        field_val = paper_data.get(field, "")
        if isinstance(field_val, list):
            summary_str = "\n".join([
                f"• {x.get('claim', str(x)) if isinstance(x, dict) else str(x)}"
                for x in field_val
            ])
        else:
            summary_str = str(field_val)

        popup_text = f"[{group}] {field}\n" + "-" * 40 + f"\nTrích xuất từ JSON:\n{summary_str}"

        for phrase in phrases:
            matches = find_phrase(phrase, page_data)
            for page_idx, line_rects in matches:
                page = doc[page_idx]
                annot = page.add_highlight_annot(line_rects)
                annot.set_colors(stroke=color)
                annot.set_info(
                    title=f"{field} ({group})",
                    content=popup_text
                )
                annot.update()
                total_highlights += 1
                annotations_by_field[field] += 1
                field_page_map[field].add(page_idx + 1)

    # Build Bookmarks / Table of Contents
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

    os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
    doc.save(output_pdf_path)
    doc.close()

    return {
        "output_pdf_path": output_pdf_path,
        "total_highlights": total_highlights,
        "annotations_by_field": annotations_by_field,
        "field_page_map": {k: sorted(list(v)) for k, v in field_page_map.items()}
    }


# Standard mappings for 2013-A Biologically Inspired Wet SMA Pump
PUMP_2013_PHRASE_MAPPINGS = {
    "research_problem": [
        "SMAs are commonly used for applications that do not require high reciprocation rates due to their limited bandwidth. This is due to the difficulty of heating and cooling the SMA quickly and efficiently",
        "output performance was not sufficient to sustain the actuation of its own wet SMA actuators",
        "amount of fluid output of the pump must be greater than the amount of fluid input required to cause actuation for the pumping action. This corresponds to having an output-to-input ratio greater than 1.0",
        "Multiple microscale SMA pumps have been developed for delivering small amounts of fluid for various MEMS-based chemical delivery systems",
        "Since the robotic pump must be able to actuate external wet SMA systems on a macroscale, high net volume outputs on the order of mL/min are necessary"
    ],
    "research_objective": [
        "presents the concept, design, optimization, and experimental analysis of a biologically inspired wet shape memory alloy (SMA) actuated pump for robotic and mechatronic systems",
        "Just as the human heart provides energy to the muscles in the body, the robotic SMA pump distributes thermofluidic energy to arrays of SMA actuators that function as robotic muscles. Furthermore, the robotic pump draws from its own fluidic output to assist in the actuation of its own internal SMA actuators, just as a portion of the blood pumped by the human heart supplies energy to its own muscles",
        "presents the design, theoretical analysis, and implementation of a biologically inspired wet SMA actuated robotic pump that can distribute thermal energy via forced fluid convection to external wet SMA subsystems on a macroscale over prolonged periods of time. The SMA pump uniquely draws from its own thermofluidic output to assist in actuating its own internal SMA actuators. Simulations and experiments are used to characterize the performance of the pump, and to demonstrate that it can operate in a self-sustaining cycle with a net positive output"
    ],
    "robot_type": [
        "biologically inspired wet shape memory alloy (SMA) actuated pump"
    ],
    "actuation": [
        "wet SMA actuator was developed to allow for more efficient actuation and increased rates using forced convection by using both thermofluidic heating and cooling",
        "continually add energy to the hot fluid in system. This can be accomplished by heating the fluid within the hot accumulator using an electrical heating coil or a chemical reaction",
        "Supplementary Joule heating may also be used in the wet SMA actuators themselves",
        "incorporation of electrical actuation will modify (21). By adding electrical heating in addition to the fluidic convection, the overall output of the system is increased"
    ],
    "modeling_methods": [
        "model the SMA pump dynamics in order to predict the behavior of the system under various conditions. This helps alleviate the number of experiments required in order to find the set of parameters that yields optimal output performance",
        "Ertel and Mascaro's dynamic model was derived using energy bond graphs and state-space methods. This allowed for combining individual wet SMA actuator models with the pumping system model",
        "divided into three segments per actuator as opposed to 20 segments used in the actual model",
        "differential hysteresis model of the SMA actuators [19], temperature-dependent fluid properties, the ability to use complex timing schemes, and the ability to apply Joule heating",
        "piecewise linear stress-strain relationship is used to model the SMA wire",
        "states of the model will now be presented. The states include actuator force, stress and strain, piston position and velocity, pumping chamber pressure, and volume output"
    ],
    "constitutive_assumptions": [
        "hysteresis can be approximated with a cumulative normal distribution curve",
        "moduli of elasticity for austenite, martensite, twinned and detwinned martensite, respectively",
        "where R is the linear damping coefficient",
        "values of these fluidic resistances approach infinity against check valves",
        "assuming full contraction and no volumetric loss within the pumping chambers",
        "Assuming that no heat is lost to the environment at any point in the system and that no mixing of hold and cold fluids occurs"
    ],
    "independent_variables": [
        "Seven parameters largely influence this output performance: SMA wire diameter, inner tube diameter, actuator length, accumulator pressure, pumping chamber cross-sectional area, mechanical advantage, and flow duration",
        "Key parameters include actuator length, mechanical advantage in the pumping lever, flow duration through the actuators, fluid temperature, and the use of electrical actuation",
        "amount of time prior to fluidic flow stopping that the electrical actuation begins. A lead time of 0.0 s means that the electrical actuation begins at the time the fluid stops",
        "with and without heat input to the hot accumulator water"
    ],
    "dependent_variables": [
        "volumetric output in terms of output-to-input ratio",
        "net output of 66 mL/min",
        "rate of change in temperature of an SMA actuator is given by",
        "piston position and velocity, pumping chamber pressure, and volume output"
    ],
    "control_variables": [
        "An accumulator pressure of 15 kPa was used to match that which will be used in",
        "working fluid used for simulation was water",
        "stagnation periods of 2 s were used for actuation timing",
        "electrical duration of 1 s was used for these simulations",
        "electrical current used for the simulations was 4.5 A"
    ],
    "experimental_setup": [
        "prototype utilizes complex timing control, electrical actuation, fluid separation and recycling, and continuous heat addition. Fig. 9 is an actual photograph of the working prototype used for experimental testing",
        "prototype allows for parameter variation such as actuator length and mechanical advantage. A heating element is located inside the hot water accumulator in order to sustain performance over extended periods of time",
        "flow path is controlled by four solenoid valves: two of them control the fluid input to the actuators through a control manifold and the other two separate",
        "the hot and cold fluid output from the actuators through a separation manifold",
        "Two power supplies are used to actuate the two individual actuators",
        "experimentation at an elevation of roughly 1400 m"
    ],
    "performance_metrics": [
        "output-to-input ratio greater than 1.0",
        "heartbeat period",
        "maximum efficiency that can be achieved with this pump system is 3.4%",
        "demonstrates that in order to increase the power output of the pump, longer actuators or more contracting actuators are required",
        "trade for decreased pump stroke"
    ],
    "main_results": [
        "pumping 2.1 times more fluid than is required to sustain its own actuation",
        "first successful implementation of such a robotic pump, such that it has a net positive thermofluidic output to provide to other actuators while sustaining its own actuation via thermofluidic feedback",
        "capable of pumping a net output of 66 mL/min, which is two orders of magnitude larger than the other SMA pumps previously mentioned",
        "simulation results are within 5-10% of the experimental results",
        "maximum output-to-input ratio obtained with fluid-only actuation under the conditions provided in Table II was 0.88",
        "maximum output-to-input ratio reached 1.35 for fluid-only actuation which is close to the predicted value of 1.38",
        "With electrical heating assistance, an output-to-input ratio of 2.1 was reached using 40-cm actuators and flow duration of 1.5 s. With this electrical configuration, the pump is capable of pumping a net output of 66 mL/min",
        "performance is sustained and that the performance is significantly higher with continuous heat addition than without"
    ],
    "evidence_relevant_to_topic": [
        "feasibility analysis provides insight to limits of configuration parameters",
        "maximum theoretical output-to-input ratio of a specific configuration can be determined by assuming full contraction",
        "Diagram demonstrating a pump that provides energy to external systems and itself, forming a self-sustaining pump analogous to a heart",
        "simulation results in Fig. 5 as a baseline and then performing quick tests to determine the optimal flow duration by monitoring the output"
    ],
    "limitations_stated_by_authors": [
        "maximum theoretical efficiency that this system can achieve is 3.4%. The actual efficiency of this prototype system is much less",
        "In an actual implementation of the proposed pump, the practical efficiency will be less than 3.4% due to mixing of the hot and cold fluids, heat loss to the environment, and parasitic mechanical losses",
        "prolonged durations of passing current through the actuators can cause permanent deformation",
        "Since the performance of the fluid-only experiments did not exceed a volume output-to-input ratio greater than 1.0, electrical actuation assistance is required",
        "high mechanical advantage can be beneficial for overpowering the accumulator pressure, but in a trade for decreased pump stroke",
        "efficiency of the optimized system will still be much lower than a pump driven by electric motors"
    ],
    "limitations_inferred": [
        "prototype utilizes complex timing control, electrical actuation, fluid separation and recycling, and continuous heat addition",
        "boiling point of the water will be higher due to the increased pressure within the accumulators",
        "Two power supplies are used to actuate the two individual actuators"
    ],
    "future_work": [
        "Future improvements planned for the robotic pump include making the system more compact in volume, removing the need for auxiliary electric inputs, and optimizing the practical efficiency of the pump",
        "Methods to decrease the electrical dependence include using fluid-only heating and using mechanically timed valves",
        "In future work, we will seek to characterize and optimize the practical efficiency of the system by minimizing thermal and mechanical losses"
    ],
    "possible_gap_implications": [
        "advantage of the SMA pump is that it is capable of running off of thermal energy. This is advantageous because the thermal energy could be provided by a chemical energy source with an energy density that is significantly higher than that of batteries",
        "Therefore, the 3.4% maximum efficiency is offset by a 100 to 1 advantage in energy storage",
        "efficiency disadvantage is theoretically offset by a 100 to 1 advantage in chemical versus electric"
    ]
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highlight paper PDF according to JSON extraction schema.")
    parser.add_argument("--pdf", default="data/final/MP1/08_current_reports/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf")
    parser.add_argument("--json", default="data/final/MP1/08_current_reports/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_de64029540.json")
    parser.add_argument("--output", default="data/final/MP1/annotated/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump_annotated.pdf")
    args = parser.parse_args()

    res = annotate_paper_pdf(args.pdf, args.json, args.output, PUMP_2013_PHRASE_MAPPINGS)
    print(f"SUCCESS: Generated {res['total_highlights']} annotations into {res['output_pdf_path']}")
