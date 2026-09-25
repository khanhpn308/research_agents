# Worker W2-04-07: Full-text extraction for papers 11–12 (Vahidi 2022 & Niu 2021) Report

> **Worker:** W2-04-07  
> **Nhiệm vụ:** Full-text extraction for papers 11–12 (Vahidi 2022 & Niu 2021)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [11]:** `53200aa0c6` — *Mechanical response of single and double-helix SMA wire ropes* (Saeed Vahidi et al., 2022)
- **Bài báo [12]:** `98fee47c04` — *Nonlinear Vibration Isolation via a NiTiNOL Wire Rope* (Mu-Qing Niu et al., 2021)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [11]: Mechanical response of single and double-helix SMA wire ropes
- **Mã định danh:** `53200aa0c6` | **DOI:** [10.1080/15376494.2021.1955313](https://doi.org/10.1080/15376494.2021.1955313)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf`
- **Mục tiêu đe dọa:** Directly closes T1 and demonstrates H0b sufficiency by modeling 3D NiTi multiwire bundles with Coulomb friction and Auricchio superelasticity.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** 3D nonlinear continuum finite element analysis in Abaqus/Standard with custom UMAT trên 1x27 single-helix and 7x7 double-helix superelastic NiTi wire ropes dưới chế độ tải Quasi-static cyclic uniaxial tension under fixed-end rotation
- **Mô hình tiếp xúc & Cấu thành:** Auricchio-Petrini 3D phenomenological superelastic constitutive model implemented in UMAT / Penalty formulation Coulomb friction with isotropic friction coefficient mu = 0.115
- **Bằng chứng xác thực trực tiếp:**
  - Abaqus FEA combining Auricchio UMAT with Coulomb friction (mu = 0.115) accurately predicts the complete cyclic response of 1x27 and 7x7 NiTi cables (Section 4, pp. 6-10).
  - Inter-wire friction increases axial stiffness and energy dissipation while reducing total recoverable strain (Section 4.3, pp. 11-13).
  - The model reproduces the experimental data of Reedlunn 2013 without introducing any new micro-coupling laws (Section 4.1, pp. 7-9).
- **Điều bài báo thực sự chứng minh:** Proves that existing transformation-aware constitutive models coupled with standard Coulomb contact mechanics (H0b) are fully sufficient to predict multiwire NiTi bundle response.
- **Điều bài báo KHÔNG chứng minh:** Does not apply an active transverse fluid confinement pressure independent of axial tension.
- **Giới hạn khoa học:** Axial tension only; isothermal assumption; no transverse fluid pressure.
- **Tác động tới MP1:** `WEAKENS` — Decisive paper: closes C5/T1 at existence level and establishes H0b as a formidable, non-falsified competitor null hypothesis.
- **Chỉ dẫn bằng chứng trang/mục:** Section 3 (pp. 3-6), Section 4 (pp. 6-14) (Fig. 4 (3D FEA mesh and contact definitions), Fig. 7 (validation against Reedlunn 1x27 and 7x7 data), Fig. 12 (friction sensitivity analysis))

### Bài báo [12]: Nonlinear Vibration Isolation via a NiTiNOL Wire Rope
- **Mã định danh:** `98fee47c04` | **DOI:** [10.3390/app112110032](https://doi.org/10.3390/app112110032)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A4-2021-Nonlinear vibration isolation via a nitinol wire rope.pdf`
- **Mục tiêu đe dọa:** Threatens T1 and T3 by demonstrating that NiTi wire ropes provide tunable stiffness and damping under cyclic loading.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Experimental vibration testing and nonlinear dynamic modeling trên Laboratory NiTi wire rope isolator dưới chế độ tải Vertical dynamic base excitation and harmonic force excitation
- **Mô hình tiếp xúc & Cấu thành:** Polynomial restoring force combined with Bouc-Wen hysteresis / Frictional dissipation represented via Bouc-Wen evolutionary variable
- **Bằng chứng xác thực trực tiếp:**
  - NiTi wire rope isolators exhibit amplitude-dependent resonance frequency shifts due to superelastic softening (Section 3, pp. 6-9).
  - Superelasticity provides enhanced energy dissipation and displacement control over conventional steel wire ropes (Section 4, pp. 10-12).
- **Điều bài báo thực sự chứng minh:** Proves that NiTi wire ropes modulate dynamic stiffness and dissipate energy under cyclic deformation.
- **Điều bài báo KHÔNG chứng minh:** Does not apply active pneumatic/hydraulic confinement pressure.
- **Giới hạn khoa học:** Lumped parameter dynamic testing; no local slip measurement.
- **Tác động tới MP1:** `BOUNDS` — Demonstrates prior art use of NiTi wire ropes for stiffness modulation.
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 3-5), Section 3 (pp. 6-10) (Fig. 5 (transmissibility curves), Fig. 8 (hysteresis loops under dynamic loading))
