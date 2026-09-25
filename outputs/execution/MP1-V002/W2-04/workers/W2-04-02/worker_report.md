# Worker W2-04-02: Full-text extraction for papers 01–02 (Reedlunn 2013 Part I & Part II) Report

> **Worker:** W2-04-02  
> **Nhiệm vụ:** Full-text extraction for papers 01–02 (Reedlunn 2013 Part I & Part II)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [01]:** `00414aac4b` — *Superelastic shape memory alloy cables: Part I – Isothermal tension experiments* (Benjamin Reedlunn et al., 2013)
- **Bài báo [02]:** `fac21c950e` — *Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses* (Benjamin Reedlunn et al., 2013)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [01]: Superelastic shape memory alloy cables: Part I – Isothermal tension experiments
- **Mã định danh:** `00414aac4b` | **DOI:** [10.1016/j.ijsolstr.2013.03.013](https://doi.org/10.1016/j.ijsolstr.2013.03.013)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf`
- **Mục tiêu đe dọa:** Directly threatens T1 by proving inter-wire contact, friction, and hysteretic energy dissipation in NiTi wire bundles.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Experimental testing with non-contact optical diagnostics and thermal imaging trên 7x7 right regular lay and 1x27 alternating lay superelastic NiTi cables dưới chế độ tải Quasi-static isothermal uniaxial elongation under rigid end rotation constraint
- **Mô hình tiếp xúc & Cấu thành:** Phenomenological shakedown laws (modeling deferred to Part II) / Qualitative Coulomb friction assessment via dry vs lubricated testing
- **Bằng chứng xác thực trực tiếp:**
  - Lubrication does not noticeably alter the axial load-strain curves of 7x7 or 1x27 NiTi cables (Section 4.1, p. 3012).
  - 7x7 cable exhibits localized transformation front propagation with localized rotation kinks (Section 4.2, p. 3014).
  - Contact indentations observed in SEM are pre-existing manufacturing artifacts from stranding and shape setting (Section 4.5, p. 3019).
- **Điều bài báo thực sự chứng minh:** Proves that multiwire NiTi cables exhibit inter-wire contact normal forces, high static friction, and severe cyclic shakedown.
- **Điều bài báo KHÔNG chứng minh:** Does not evaluate bending flexure or external transverse fluid confinement pressure; does not validate a predictive contact constitutive law.
- **Giới hạn khoa học:** Uniaxial tension only; constrained rotation boundary condition; isothermal slow strain rates.
- **Tác động tới MP1:** `BOUNDS` — Closes C5/T1 at existence level by demonstrating mutual contact in NiTi wire bundles; refutes overclaims that contact indentations were operational fretting wear.
- **Chỉ dẫn bằng chứng trang/mục:** Section 4.1 (pp. 3011-3013), Section 4.5 (pp. 3018-3021) (Fig. 5 (load-strain curves), Fig. 8 (SEM micrographs of inter-wire contact indentations))

### Bài báo [02]: Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses
- **Mã định danh:** `fac21c950e` | **DOI:** [10.1016/j.ijsolstr.2013.03.015](https://doi.org/10.1016/j.ijsolstr.2013.03.015)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf`
- **Mục tiêu đe dọa:** Evaluates whether existing cable kinematics and contact formulations can predict multiwire NiTi response (T1, T3, H0b).
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Hierarchical experimental testing and analytical kinematic modeling trên Single NiTi wires, 1x7 strands, 1x19 cables, and 1x27 cables dưới chế độ tải Quasi-static uniaxial tension
- **Mô hình tiếp xúc & Cấu thành:** Costello wire rope kinematics combined with single-wire experimental curves / Line contact formulation with inter-wire radial pressure
- **Bằng chứng xác thực trực tiếp:**
  - The Costello model divergence in 1x27 cables stems from the neglect of individual wire bending and twisting moments (Section 5.3, pp. 3035-3037).
  - Single wire responses closely match 1x7 strand response when normalized by metallic cross-sectional area (Section 4.2, p. 3028).
- **Điều bài báo thực sự chứng minh:** Proves that shallow helix angle NiTi bundles behave closely to single wires; proves that model divergence at steep angles is due to kinematic reduction omissions.
- **Điều bài báo KHÔNG chứng minh:** Does not prove a failure of continuum contact mechanics; does not support the requirement of a new micro-coupling law H1.
- **Giới hạn khoa học:** Tension only; analytical model did not resolve full 3D frictional stick-slip.
- **Tác động tới MP1:** `BOUNDS` — Mandates conservative remediation of Reedlunn 2013 (Astra G07): model failure in steep helical cables cannot be cited as evidence that parallel NiTi bundles require new mechanics.
- **Chỉ dẫn bằng chứng trang/mục:** Section 5.3 (pp. 3034-3038) (Fig. 11 (Costello model vs experiment for 1x7 and 1x27 cables))
