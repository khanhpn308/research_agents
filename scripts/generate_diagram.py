import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_narrowing_flowchart(output_path):
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=300)
    ax.axis('off')
    
    # Define steps
    steps = [
        ("1. Ý TƯỞNG BAN ĐẦU CỦA MENTOR (MENTOR INITIAL IDEA)",
         "Kiến trúc robot mềm biến thiên độ cứng: Bó dây kim loại/NiTi + Giam giữ áp suất dương\n+ Kẹt ma sát giữa các dây + Nguồn áp suất xilanh/piston SMA nhỏ gọn tích hợp.",
         "#E8E8E8", "#333333"),
        ("2. PHÂN RÃ CÁC TUYÊN BỐ TÍNH MỚI THIẾT BỊ (DEVICE CLAIMS DECOMPOSITION)",
         "C1 (Kẹt dây kim loại/sợi); C2 (Kẹt bằng áp suất dương); C3 (Tích hợp SMA + Jamming);\nC4/C8 (Bơm vi mô / Piston SMA tích hợp); C5-C7 (Dây NiTi cọ xát dưới áp suất).",
         "#F4F4F4", "#555555"),
        ("3. TRUY VẤN Y VĂN VÀ BÁC BỎ CẤP ĐỘ THIẾT BỊ (PRIOR ART FALSIFICATION)",
         "Bai (2022) & Zhang (2026) -> Loại bỏ C1; Liu (2021) & Zhang (2026) -> Loại bỏ C2;\nTakashima (2020-2026) -> Loại bỏ C3; Huynh (2022) & Wang (2024) -> Loại bỏ C4, C8.",
         "#EFEFEF", "#444444"),
        ("4. BƯỚC CHUYỂN HƯỚNG CỐT LÕI (PIVOT: DEVICE -> MECHANICS CORE)",
         "Tính mới tổ hợp linh kiện bị triệt tiêu (Pre-empted). Thay thế phần cứng không phải tính mới khoa học.\nChuyển toàn bộ trọng tâm sang Lõi Cơ học: Mục tiêu T1 (Tiếp xúc), T2 (Áp suất), T3 (Ghép cặp).",
         "#E2E2E2", "#222222"),
        ("5. KHẢO SÁT CƠ HỌC CÁP / DÂY NiTi (NiTi CABLE & CONTACT LITERATURE)",
         "Reedlunn (2013), Carboni (2015/2016), Fang (2019), Vahidi (2022), Kang (2020):\nChuyển pha, trễ thắt, ma sát tiếp xúc trong cáp NiTi đã được thiết lập -> Bác bỏ C5.",
         "#F4F4F4", "#555555"),
        ("6. KHẢO SÁT CƠ HỌC UỐN & ÁP SUẤT GIAM GIỮ (BENDING & PRESSURE MECHANICS)",
         "Xin Liu (2004), Tjahjanto (2017), Barsi (2025): Áp suất giam giữ là điều kiện biên lực mặt (sigma.n = -p.n);\nHiệu ứng vòm & màng làm áp suất buồng p != lực tiếp xúc fn -> Hạ cấp C6 thành ĐK biên thực nghiệm.",
         "#F4F4F4", "#555555"),
        ("7. THỬ NGHIỆM THẾ THAM SỐ & PHÂN TÁCH GIẢ THUYẾT (H0a / H0b / H1)",
         "H0a (Đàn hồi hằng số): REFUTED ở miền chuyển pha (>0.75%). Lưu ý: H0a sai KHÔNG chứng minh H1 đúng!\nH0b (NiTi phi tuyến + Tiếp xúc Coulomb): NOT FALSIFIED (Đối thủ mạnh nhất). H1: INSUFFICIENT.",
         "#EAEAEA", "#333333"),
        ("8. XÁC LẬP TÍNH ĐỦ CỦA CÔNG THỨC & KHOẢNG TRỐNG THỰC CHẤT (S01 AUDIT)",
         "Về mặt công thức (in principle), cơ học hiện hữu H0b đã đủ khả năng dung nạp bài toán.\nKhoảng trống thực sự: Tính thỏa đáng dự đoán (predictive adequacy) khi khóa tham số uốn chưa từng kiểm chứng.",
         "#F4F4F4", "#444444"),
        ("9. BÀI TOÁN PHÂN BIỆT MÔ HÌNH (MODEL-DISCRIMINATION PROBLEM)",
         "Không tìm kiếm định luật vi mô mới một cách tiên nghiệm. Đặt bài toán kiểm chứng thực nghiệm đối chứng:\nLiệu H0b với tham số khóa độc lập có dự đoán chính xác đáp ứng uốn dưới áp suất thay đổi hay không?",
         "#E2E2E2", "#222222"),
        ("10. CÂU HỎI NGHIÊN CỨU CUỐI CÙNG (FINAL RESEARCH QUESTION)",
         "\"Trong miền áp suất - độ cong - nhiệt độ cùng kích hoạt trượt và chuyển pha, liệu mô hình NiTi cấu thành\n+ tiếp xúc ma sát hiện hữu (H0b) được khóa tham số có dự đoán đầy đủ đáp ứng uốn bó dây hay không?\"",
         "#D8D8D8", "#111111")
    ]
    
    n = len(steps)
    box_height = 0.058
    box_width = 0.88
    spacing = 0.038
    start_y = 0.94
    
    for i, (title, desc, fill_color, border_color) in enumerate(steps):
        y = start_y - i * (box_height + spacing)
        x = (1.0 - box_width) / 2.0
        
        # Draw box
        rect = patches.FancyBboxPatch(
            (x, y - box_height), box_width, box_height,
            boxstyle="round,pad=0.012,rounding_size=0.015",
            linewidth=1.2, edgecolor=border_color, facecolor=fill_color
        )
        ax.add_patch(rect)
        
        # Add text
        ax.text(0.5, y - 0.016, title, ha='center', va='center',
                fontsize=9.0, fontweight='bold', family='serif', color='#000000')
        ax.text(0.5, y - 0.038, desc, ha='center', va='center',
                fontsize=7.5, family='serif', color='#222222', linespacing=1.2)
        
        # Draw arrow to next step
        if i < n - 1:
            arrow_y_start = y - box_height - 0.002
            arrow_y_end = arrow_y_start - (spacing - 0.004)
            ax.annotate(
                '', xy=(0.5, arrow_y_end), xytext=(0.5, arrow_y_start),
                arrowprops=dict(facecolor='#444444', edgecolor='#444444',
                                width=1.0, headwidth=5.0, headlength=5.0)
            )
            
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Diagram successfully saved to {output_path}")

if __name__ == '__main__':
    create_narrowing_flowchart("docs/reports/figures/mp1_narrative_narrowing_diagram.png")
