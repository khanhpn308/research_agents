# Worker W2-04-08: Full-text extraction for papers 13–14 (Liu 2004 & Tjahjanto 2017) Report

> **Worker:** W2-04-08  
> **Nhiệm vụ:** Full-text extraction for papers 13–14 (Liu 2004 & Tjahjanto 2017)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [13]:** `aaad9c248c` — *Cable Vibration Considering Internal Friction* (Xin Liu et al., 2004)
- **Bài báo [14]:** `ccdc1bb980` — *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable* (Denny D. Tjahjanto et al., 2017)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [13]: Cable Vibration Considering Internal Friction
- **Mã định danh:** `aaad9c248c` | **DOI:** [10.1115/1.1767817](https://doi.org/10.1115/1.1767817)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf`
- **Mục tiêu đe dọa:** Threatens T1 by proving that inter-wire friction mechanics in slender wire bundles is an established classical discipline.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C1', 'C5']` | Targets `['T1']` | Hypotheses `['H0a']`
- **Phương pháp & Vật liệu:** Analytical continuum mechanics and boundary value problem formulation trên Multi-wire stranded cables and parallel wire bundles under tension dưới chế độ tải Transverse flexural vibration under axial tension
- **Mô hình tiếp xúc & Cấu thành:** Linear elastic wire material / Micro-slip Coulomb contact model with shear traction boundary conditions
- **Bằng chứng xác thực trực tiếp:**
  - Internal friction between adjacent wires produces amplitude-dependent damping and flexural stiffness modulation (Section 2, pp. 2-4).
  - Contact pressure between wires governs the threshold amplitude required to trigger inter-wire slip (Section 3, pp. 5-7).
- **Điều bài báo thực sự chứng minh:** Proves that inter-wire friction in slender wire bundles is fully treatable using continuum mechanics.
- **Điều bài báo KHÔNG chứng minh:** Does not involve shape memory alloys or active pressure control.
- **Giới hạn khoa học:** Linear elastic steel cables only; axial tension required to generate contact pressure.
- **Tác động tới MP1:** `BOUNDS` — Demonstrates classical lineage of wire bundle friction mechanics.
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 1-4), Section 4 (pp. 6-8) (Eq. (8)-(14) (inter-wire shear slip equations), Fig. 3 (damping vs vibration amplitude))

### Bài báo [14]: Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable
- **Mã định danh:** `ccdc1bb980` | **DOI:** [10.1115/OMAE2017-61198](https://doi.org/10.1115/OMAE2017-61198)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf`
- **Mục tiêu đe dọa:** Directly threatens T2 by proving that external radial contact pressure modulating flexural stiffness is prior art.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C2', 'C6']` | Targets `['T2']` | Hypotheses `['H0b']`
- **Phương pháp & Vật liệu:** Analytical formulation and finite element beam bending simulation trên Dynamic submarine power cables consisting of multiple metallic conductor cores and polymer fillers dưới chế độ tải Cyclic lateral bending under external radial contact pressure (0.2 MPa)
- **Mô hình tiếp xúc & Cấu thành:** Elastic metallic conductor cores and viscoelastic/plastic filler material / Coulomb friction law with radial contact pressure acting across cylindrical contact interfaces
- **Bằng chứng xác thực trực tiếp:**
  - External radial pressure p directly increases the contact normal force between internal cable elements, delaying the onset of slip to higher curvatures (Section 3, pp. 4-6).
  - The bending stiffness transitions from a high stick bound to a lower slip bound as inter-element friction is overcome (Section 4, pp. 7-9).
- **Điều bài báo thực sự chứng minh:** Proves that external radial confining pressure directly increases inter-element normal force and modulates flexural rigidity under bending.
- **Điều bài báo KHÔNG chứng minh:** Applies a constant external radial pressure rather than actively modulating pressure as a variable stiffness control parameter on NiTi.
- **Giới hạn khoa học:** Constant radial pressure; copper conductors rather than NiTi superelastic wires.
- **Tác động tới MP1:** `WEAKENS` — Direct basis for CONTRA-05: proves active pressure is an experimental boundary condition, closing T2 as mechanics novelty.
- **Chỉ dẫn bằng chứng trang/mục:** Section 3 (pp. 3-6), Section 4 (pp. 7-10) (Fig. 5 (radial contact pressure schematic), Fig. 8 (moment-curvature curves under radial pressure))
