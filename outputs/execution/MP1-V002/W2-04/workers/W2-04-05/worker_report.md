# Worker W2-04-05: Full-text extraction for papers 07–08 (Barsi 2025 & Kang 2020) Report

> **Worker:** W2-04-05  
> **Nhiệm vụ:** Full-text extraction for papers 07–08 (Barsi 2025 & Kang 2020)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [07]:** `9f4295be23` — *A new mechanical model of short wire ropes: Theory and experimental validation* (F. Barsi et al., 2025)
- **Bài báo [08]:** `56793dea9b` — *Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables (形状记忆合金超弹性缆索力学行为的有限单元法)* (KANG Zetian et al., 2020)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [07]: A new mechanical model of short wire ropes: Theory and experimental validation
- **Mã định danh:** `9f4295be23` | **DOI:** [10.1016/j.engstruct.2024.119217](https://doi.org/10.1016/j.engstruct.2024.119217)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf`
- **Mục tiêu đe dọa:** Directly threatens T1, T2, and H0b by formulating exact stick-slip bending bounds under contact friction.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C1', 'C5', 'C7']` | Targets `['T1', 'T2', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Analytical continuum beam modeling and experimental static/dynamic bending tests trên Short multiwire steel wire ropes (19-wire and 49-wire configurations) dưới chế độ tải Three-point bending and cantilever cyclic bending flexure
- **Mô hình tiếp xúc & Cấu thành:** Linear elastic wire material with inter-wire stick-slip contact equilibrium / Coulomb friction law with normal contact pressure resulting from internal geometry and clamping
- **Bằng chứng xác thực trực tiếp:**
  - The flexural rigidity of a multiwire rope transitions smoothly from EI_stick (full composite action) to EI_slip (isolated wire sum) as inter-wire friction is overcome (Section 2, pp. 3-6).
  - The model predicts both stiffness bounds using only wire geometry and elastic properties without fitting parameters (Section 4, pp. 11-14).
- **Điều bài báo thực sự chứng minh:** Proves that beam stick-slip mechanics rigorously predicts the variable flexural stiffness of multiwire bundles under frictional contact.
- **Điều bài báo KHÔNG chứng minh:** Does not incorporate superelastic NiTi phase transformation; steel ropes only.
- **Giới hạn khoa học:** Linear elastic steel wires; did not evaluate active fluid membrane confinement.
- **Tác động tới MP1:** `BOUNDS` — Confirms that variable bending stiffness via contact friction is a solved continuum mechanics problem (H0b competitor).
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 2-7), Section 4 (pp. 10-15) (Eq. (12)-(15) (stiffness bounds), Fig. 6 (bending moment vs curvature comparison))

### Bài báo [08]: Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables (形状记忆合金超弹性缆索力学行为的有限单元法)
- **Mã định danh:** `56793dea9b` | **DOI:** [10.3901/JME.2020.14.065](https://doi.org/10.3901/JME.2020.14.065)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf`
- **Mục tiêu đe dọa:** Threatens T1 and T3 by demonstrating tailored finite element formulation for contacting NiTi cable structures.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Nonlinear finite element formulation using corotational beam elements with contact trên 1x7 and 1x19 superelastic NiTi SMA cables dưới chế độ tải Monotonic and cyclic tension and pure bending
- **Mô hình tiếp xúc & Cấu thành:** 1D Auricchio superelastic constitutive model with tension-compression asymmetry / Point-to-line and line-to-line contact element with Coulomb friction
- **Bằng chứng xác thực trực tiếp:**
  - The corotational beam FE model with 1D Auricchio constitutive relations reproduces the tensile and bending hysteresis of SMA cables (Section 3, pp. 68-71).
  - Inter-wire contact forces concentrate along helical line contacts and dictate local frictional slip (Section 4, pp. 71-73).
- **Điều bài báo thực sự chứng minh:** Proves that existing beam contact finite elements combined with standard 1D Auricchio models (H0b) accurately simulate NiTi multiwire cable deformation.
- **Điều bài báo KHÔNG chứng minh:** Does not apply active external pneumatic/hydraulic confinement pressure.
- **Giới hạn khoa học:** Numerical paper without new standalone experimental tests (benchmarked against Reedlunn).
- **Tác động tới MP1:** `BOUNDS` — Confirms H0b feasibility for beam finite element modeling of NiTi wire bundles.
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 66-68), Section 3 (pp. 68-72) (Fig. 4 (corotational beam contact formulation), Fig. 7 (validation against Reedlunn 2013))
