# Worker W2-04-09: Full-text extraction for papers 15–16 (Liu 2026 & Silva 2022) Report

> **Worker:** W2-04-09  
> **Nhiệm vụ:** Full-text extraction for papers 15–16 (Liu 2026 & Silva 2022)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [15]:** `e8462758c3` — *High damping capacity with a wide temperature window in braided NiTi microfilaments* (Yiwen Liu et al., 2026)
- **Bài báo [16]:** `6dd1ca94d1` — *NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings* (Paulo C. S. Silva et al., 2022)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [15]: High damping capacity with a wide temperature window in braided NiTi microfilaments
- **Mã định danh:** `e8462758c3` | **DOI:** [10.1016/j.matlet.2026.141544](https://doi.org/10.1016/j.matlet.2026.141544)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf`
- **Mục tiêu đe dọa:** Threatens T1 and T3 by demonstrating recent 2026 advances in friction-transformation coupling of NiTi microfilaments.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Experimental fabrication, dynamic mechanical analysis (DMA), and cyclic tensile testing trên Braided multi-strand NiTi microfilaments (wire diameters 50 to 100 micrometers) dưới chế độ tải Cyclic tension and dynamic oscillatory flexure across temperature range (-50 deg C to 100 deg C)
- **Mô hình tiếp xúc & Cấu thành:** Temperature-dependent martensitic phase transformation combined with contact friction / Inter-filament contact friction in braided architecture
- **Bằng chứng xác thực trực tiếp:**
  - The synergistic combination of inter-filament frictional sliding and martensitic phase transformation broadens the damping temperature window (Section 3, pp. 3-5).
  - Braided architecture facilitates continuous contact reorientation during cyclic deformation (Section 4, pp. 5-7).
- **Điều bài báo thực sự chứng minh:** Proves that microfilament NiTi bundles exhibit simultaneous friction sliding and phase transformation damping.
- **Điều bài báo KHÔNG chứng minh:** Does not apply active pneumatic confinement pressure for stiffness tuning.
- **Giới hạn khoa học:** Braided sleeves rather than straight parallel bundles; focus on damping rather than variable stiffness robotics.
- **Tác động tới MP1:** `BOUNDS` — Confirms that 2026 literature actively leverages coupled NiTi friction-transformation mechanics in multi-filament structures.
- **Chỉ dẫn bằng chứng trang/mục:** Section 3 (pp. 3-5), Section 4 (pp. 5-8) (Fig. 2 (braided NiTi microstructure), Fig. 4 (tan delta vs temperature across frequencies))

### Bài báo [16]: NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings
- **Mã định danh:** `6dd1ca94d1` | **DOI:** [10.3390/s22208045](https://doi.org/10.3390/s22208045)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A8-2022-NiTi SMA Superelastic Micro Cables Thermomechanical Behavior and Fatigue Life under Dynamic Loadings.pdf`
- **Mục tiêu đe dọa:** Threatens feasibility and durability assumptions of NiTi multiwire jamming bundles under cyclic actuation.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Experimental cyclic tensile and dynamic fatigue testing with infrared thermography trên 1x7 and 7x7 superelastic NiTi micro-cables (diameters 0.5 mm to 1.8 mm) dưới chế độ tải High-cycle dynamic uniaxial tension at varying frequencies (0.5 Hz to 5 Hz)
- **Mô hình tiếp xúc & Cấu thành:** Cyclic superelastic constitutive degradation model / Frictional contact fretting wear characterization via SEM analysis
- **Bằng chứng xác thực trực tiếp:**
  - Premature fatigue fractures in multiwire NiTi cables initiate predominantly at inter-wire contact points due to fretting wear (Section 3.3, pp. 11-14).
  - Dynamic cycling above 1 Hz induces substantial internal temperature rise, altering the transformation plateau stress via Clausius-Clapeyron relation (Section 3.2, pp. 8-10).
- **Điều bài báo thực sự chứng minh:** Proves that inter-wire contact friction causes localized fretting wear and accelerates fatigue failure in dynamic NiTi multiwire bundles.
- **Điều bài báo KHÔNG chứng minh:** Does not test lateral bending stiffness modulation under positive pressure.
- **Giới hạn khoa học:** Axial tension fatigue only; does not evaluate variable stiffness jamming.
- **Tác động tới MP1:** `BOUNDS` — Directly informs feasibility and experimental identifiability: fretting wear and self-heating must be accounted for in cyclic tests.
- **Chỉ dẫn bằng chứng trang/mục:** Section 3 (pp. 7-14), Section 4 (pp. 14-16) (Fig. 8 (temperature rise vs frequency), Fig. 12 (SEM images of inter-wire fretting fatigue cracks))
