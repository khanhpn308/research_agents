# Worker W2-04-04: Full-text extraction for papers 05–06 (Salvatore 2021 & Narjabadifam 2024) Report

> **Worker:** W2-04-04  
> **Nhiệm vụ:** Full-text extraction for papers 05–06 (Salvatore 2021 & Narjabadifam 2024)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [05]:** `7f3f45407f` — *Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation* (Andrea Salvatore et al., 2021)
- **Bài báo [06]:** `1c81b2d35c` — *Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes* (Peyman Narjabadifam et al., 2024)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [05]: Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation
- **Mã định danh:** `7f3f45407f` | **DOI:** [10.1016/j.engstruct.2021.112121](https://doi.org/10.1016/j.engstruct.2021.112121)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2021-Nonlinear dynamic response of a wire rope isolator Experiment, identification and validation.pdf`
- **Mục tiêu đe dọa:** Threatens T1 by proving that multi-axis stick-slip friction in wire bundles is rigorously understood.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C1', 'C5']` | Targets `['T1']` | Hypotheses `['H0a']`
- **Phương pháp & Vật liệu:** Experimental dynamic shaker testing and multi-mechanism phenomenological identification trên Standard stainless steel wire rope isolator (WRI) with helical loop configuration dưới chế độ tải Multi-axis dynamic excitation: compression-roll and tension-shear cyclic loading
- **Mô hình tiếp xúc & Cấu thành:** Nonlinear elastic restoring force combined with hysteretic friction displacement variables / Smooth hysteretic friction formulation representing distributed inter-wire slip
- **Bằng chứng xác thực trực tiếp:**
  - Inter-wire friction generates non-symmetric pinched hysteretic response under combined compression and roll (Section 3, pp. 6-9).
  - Initial stiffness is dominated by stick state, followed by gradual softening as inter-wire slip propagates (Section 4, pp. 10-12).
- **Điều bài báo thực sự chứng minh:** Proves that inter-wire friction in helical wire ropes produces amplitude-dependent stiffness variation and dry friction damping.
- **Điều bài báo KHÔNG chứng minh:** Does not use shape memory alloys (steel only); does not apply active fluid confinement pressure.
- **Giới hạn khoa học:** Stainless steel only; phenomenological lumped parameter model rather than continuum FEA.
- **Tác động tới MP1:** `BOUNDS` — Demonstrates that friction-induced stiffness variation in wire bundles is thoroughly established in structural mechanics.
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 3-6), Section 4 (pp. 10-14) (Fig. 4 (experimental multi-axis hysteresis loops), Fig. 11 (model validation))

### Bài báo [06]: Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes
- **Mã định danh:** `1c81b2d35c` | **DOI:** [10.3390/buildings14061567](https://doi.org/10.3390/buildings14061567)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf`
- **Mục tiêu đe dọa:** Threatens T1 and T3 by directly testing laboratory-made NiTi wire ropes under cyclic loading.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Laboratory fabrication, mechanical tensile testing, and Abaqus 3D finite element modeling trên 1x7 laboratory-made steel wire ropes and 1x7 NiTi shape memory alloy wire ropes dưới chế độ tải Quasi-static monotonic and cyclic axial tension
- **Mô hình tiếp xúc & Cấu thành:** Built-in Abaqus Superelastic material model (Auricchio formulation) / Surface-to-surface penalty contact with Coulomb friction (mu = 0.15)
- **Bằng chứng xác thực trực tiếp:**
  - NiTi wire ropes exhibit Flag-shaped hysteresis with minimal residual strain after cyclic loading to 6% strain (Section 3.2, pp. 8-11).
  - Abaqus 3D FE model with Auricchio superelasticity and Coulomb friction accurately captures inter-wire contact and axial response (Section 4, pp. 12-15).
- **Điều bài báo thực sự chứng minh:** Proves that NiTi wire ropes can be fabricated and simulated using standard 3D FE contact tools, confirming mutual wire slip and phase transformation.
- **Điều bài báo KHÔNG chứng minh:** Does not apply active transverse fluid pressure; tension loading only.
- **Giới hạn khoa học:** 1x7 strands only; uniaxial tension only; no active fluid confinement pressure.
- **Tác động tới MP1:** `WEAKENS` — Provides direct evidence that NiTi wire bundles in mutual contact are established in 2024 literature and well-predicted by H0b.
- **Chỉ dẫn bằng chứng trang/mục:** Section 3 (pp. 7-11), Section 4 (pp. 12-16) (Fig. 7 (experimental load-unload curves), Fig. 12 (FEA contact stress contours))
