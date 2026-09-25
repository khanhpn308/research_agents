# Worker W2-04-06: Full-text extraction for papers 09–10 (Carboni 2015 & Liu 2023) Report

> **Worker:** W2-04-06  
> **Nhiệm vụ:** Full-text extraction for papers 09–10 (Carboni 2015 & Liu 2023)  
> **Trạng thái:** `COMPLETE`  

## 1. Tổng quan Lô Xử lý
- **Bài báo [09]:** `d9966f2f5e` — *Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification* (Biagio Carboni et al., 2015)
- **Bài báo [10]:** `9e15094d68` — *Superelasticity SMA cables and its simplified FE model* (Jiaxing Liu et al., 2023)

## 2. Chi tiết Trích xuất Toàn văn
### Bài báo [09]: Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification
- **Mã định danh:** `d9966f2f5e` | **DOI:** [10.1061/(ASCE)EM.1943-7889.0000852](https://doi.org/10.1061/(ASCE)EM.1943-7889.0000852)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A1-2015-Hysteresis of Multiconfiguration Assemblies of.pdf`
- **Mục tiêu đe dọa:** Central paper for T1 and T3; historically linked to CONTRA-03 (S2a steel vs S1a NiTi misattribution).
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Experimental dynamic testing and phenomenological hysteresis identification trên Multiconfiguration strand assemblies: Specimen S1a (NiTi7 strand) and Specimen S2a (ST49 steel wire rope) dưới chế độ tải Cyclic tension and combined tension-bending flexure
- **Mô hình tiếp xúc & Cấu thành:** Graesser-type superelastic formulation combined with Bouc-Wen friction damping / Inter-wire friction dissipation captured via evolutionary differential variable
- **Bằng chứng xác thực trực tiếp:**
  - Specimen S1a is composed of a 1x7 NiTi strand tested under combined tension and flexure (Table 1, p. 3).
  - Specimen S2a is an ST49 high-strength steel wire rope tested under cyclic flexure (Table 1, p. 3; Table 4, p. 10).
  - Energy dissipation in S1a originates from both Coulomb friction and martensitic phase transformation (Section 5, pp. 8-11).
- **Điều bài báo thực sự chứng minh:** Proves that multiwire NiTi assemblies under cyclic flexure dissipate energy via simultaneous inter-wire friction and pseudoelasticity (in configuration S1a).
- **Điều bài báo KHÔNG chứng minh:** Did NOT test pure cyclic bending of NiTi without tension preload; did NOT test specimen S2a as NiTi (S2a was steel).
- **Giới hạn khoa học:** S1a required substantial axial tension preload (1.5-4.5 kN); S2a was steel; no active fluid confinement pressure.
- **Tác động tới MP1:** `BOUNDS` — Direct focus of mandatory correction CONTRA-03: Stage 1 extraction error claiming S2a proved NiTi pure bending is completely expunged.
- **Chỉ dẫn bằng chứng trang/mục:** Table 1 (p. 3), Table 4 (p. 10), Section 5 (pp. 8-12) (Table 1 (specimen designations S1a vs S2a), Fig. 8 (S1a tension-bending hysteresis loops))

### Bài báo [10]: Superelasticity SMA cables and its simplified FE model
- **Mã định danh:** `9e15094d68` | **DOI:** [10.1007/s40430-022-03957-2](https://doi.org/10.1007/s40430-022-03957-2)
- **Đường dẫn PDF:** `data/papers/verification/MP1-V002/A2-2023-Superelasticity SMA cables and its simplified FE model.pdf`
- **Mục tiêu đe dọa:** Threatens model necessity by demonstrating efficient simplified FE modeling of NiTi cables.
- **Ảnh hưởng Khẳng định/Mục tiêu/Giả thuyết:** Claims `['C5', 'C7']` | Targets `['T1', 'T3']` | Hypotheses `['H0a', 'H0b']`
- **Phương pháp & Vật liệu:** Theoretical simplification, 3D FE modeling, and experimental tension validation trên 1x7 and 7x7 superelastic NiTi SMA cables dưới chế độ tải Quasi-static and cyclic axial tension
- **Mô hình tiếp xúc & Cấu thành:** Auricchio superelastic model implemented in ANSYS/Abaqus / Coupled kinematic constraint representing inter-wire frictional resistance
- **Bằng chứng xác thực trực tiếp:**
  - The simplified FE model reproduces cyclic tension curves with <5% error while reducing computational degrees of freedom by an order of magnitude (Section 3, pp. 5-8).
  - Axial stiffness degrades progressively during early loading cycles before stabilizing into a steady limit cycle (Section 4, pp. 9-11).
- **Điều bài báo thực sự chứng minh:** Proves that simplified structural models can capture multiwire NiTi cable response accurately without full 3D contact discretization.
- **Điều bài báo KHÔNG chứng minh:** Does not examine lateral bending under variable transverse pressure.
- **Giới hạn khoa học:** Axial tension only; no lateral confinement pressure.
- **Tác động tới MP1:** `BOUNDS` — Reinforces H0b by showing that simplified structural models adequately describe NiTi cables.
- **Chỉ dẫn bằng chứng trang/mục:** Section 2 (pp. 3-5), Section 3 (pp. 5-9) (Fig. 5 (simplified model schematic), Fig. 9 (comparison of simplified vs 3D solid model))
