# Worker W2-04-03: Full-text extraction for papers 03–04 (Carboni 2016 & Fang 2019) Report

> **Worker:** W2-04-03  
> **Nhiệm vụ:** Full-text extraction for papers 03–04 (Carboni 2016 & Fang 2019)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [03]:** `40760daa02` — *Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments* (Biagio Carboni et al., 2016)
- **Bài báo [04]:** `2f7fcf2f8f` — *Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application* (Cheng Fang et al., 2019)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [03]: Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments
- **Mã định danh:** `40760daa02` | **DOI:** [10.1061/(ASCE)EM.1943-7889.0001072](https://doi.org/10.1061/(ASCE)EM.1943-7889.0001072)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf`
- **Mục tiêu đe dọa:** Directly threatens T3 by demonstrating that inter-wire friction combined with NiTi phase transformation is established prior art.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Theoretical asymptotic formulation and experimental dynamic shaker testing trên Nonlinear vibration absorber consisting of a cantilever assembly with superelastic NiTi wires and friction sliders dưới chế độ tải Harmonic base excitation inducing cyclic bending
- **Mô hình tiếp xúc & Cấu thành:** Multi-mechanism pinched hysteresis model combining Bouc-Wen friction and Graesser NiTi superelasticity / Coulomb-like friction sliding element coupled in parallel/series
- **Bằng chứng xác thực trực tiếp:**
  - Pinched hysteresis arises naturally when frictional contact dissipation is combined with superelastic phase transformation (Section 2, pp. 2-4).
  - The flexural resonance peak shifts and broadens due to amplitude-dependent stiffness reduction during phase transformation (Section 4, pp. 8-10).
- **Điều bài báo thực sự chứng minh:** Proves that coupling of friction and NiTi superelasticity directly governs flexural stiffness and damping in mechanical assemblies.
- **Điều bài báo KHÔNG chứng minh:** Does not apply an active pneumatic or hydraulic fluid confinement pressure on the wire assembly.
- **Giới hạn khoa học:** Focused on vibration absorption; friction was concentrated at slider interfaces rather than distributed throughout a dense wire bundle.
- **Tác động tới MP1:** `WEAKENS` — Preempts claims that friction-transformation coupling is an unaddressed mechanics phenomenon; reinforces H0b.
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 2-5), Section 4 (pp. 7-11) (Fig. 3 (pinched hysteresis loops), Fig. 8 (experimental frequency-response curves))

### Bài báo [04]: Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application
- **Mã định danh:** `2f7fcf2f8f` | **DOI:** [10.1016/j.engstruct.2019.01.049](https://doi.org/10.1016/j.engstruct.2019.01.049)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2019-Superelastic NiTi SMA cables Thermal-mechanical behavior, hysteretic modelling and seismic application.pdf`
- **Mục tiêu đe dọa:** Threatens model necessity: proves that phenomenological fiber models capture cable hysteresis without resolving micro-contacts (H0b competitor).
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Experimental testing, OpenSees fiber macromodeling, and seismic nonlinear time-history analysis trên 1x7 and 7x7 superelastic NiTi cables (diameters 2.5 mm to 12.7 mm) dưới chế độ tải Cyclic uniaxial tension on cables; pushover/cyclic loading on RC bridge pier
- **Mô hình tiếp xúc & Cấu thành:** Steel02 (for core plastic residual strain) combined with Self-centering material in parallel/series / Macroscopic phenomenological compliance; inter-wire contact is not explicitly modeled
- **Bằng chứng xác thực trực tiếp:**
  - Cables were tested exclusively in axial tension; the nonlinear beam-column fiber element in OpenSees was used to model the 1.4 m diameter reinforced concrete bridge pier (Section 4, pp. 11-14).
  - Multiple distinct parameter combinations produce identical macroscopic hysteretic curves (Section 3.2, pp. 7-9).
- **Điều bài báo thực sự chứng minh:** Proves that macroscopic phenomenological models can accurately predict overall cable stiffness and energy dissipation with minimal computational cost.
- **Điều bài báo KHÔNG chứng minh:** Does not model or test NiTi cables in bending; does not test positive confinement pressure.
- **Giới hạn khoa học:** Axial tension only for SMA cables; beam model was for RC column; free floating parameters in Steel02 calibration.
- **Tác động tới MP1:** `WEAKENS` — Conservative remediation (Astra G07): corrects misconception that Fang modeled cable bending; highlights the macromodel parsimony threat to MP1.
- **Chỉ dẫn bằng chứng trang/mục:** Section 3 (pp. 6-10), Section 4 (pp. 11-15) (Fig. 6 (OpenSees fiber discretization), Fig. 13 (RC bridge pier pushover response))
