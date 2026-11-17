# Figure/Table Registry — WP-A

## 1. Summary Registry Table

| Paper | Locator in Records | Verified PDF Page | Status | Conceptual & Methodological Use |
|---|---|---:|---|---|
| M02 | Fig. 1 | 1 | VERIFIED_FULL_TEXT | Continuum vs. discrete rigid-link structures: continuous curvilinear elastic deformation. |
| M04 | Fig. 2(a–d) | 2 | VERIFIED_FULL_TEXT | Operational stiffness calculation methods: linear endpoint, torsional, three-point bending, and cantilever bending. |
| M05 | Fig. 8 [Legacy locator; Fig. 5(g) & Table 4] | 10–11 | VERIFIED_FULL_TEXT | Fibre/filament jamming (FJ) classification: axially packed 1D filaments within flexible airtight envelope. |
| M05 | Fig. 10 [Legacy locator; Fig. 5(e, f) & Table 4] | 10–12 | VERIFIED_FULL_TEXT | Layer/laminar jamming (LJ) classification: stacked 2D flaps/sheets in tendon-driven and fluidic continuum arms. |

---

## 2. Detailed Figure & Table Descriptions

### 2.1. M02 — Fig. 1: Continuum vs. Discrete Joint Architectures
- **Source:** Burgner-Kahrs, Rucker, and Choset (2015), p. 1 (printed p. 1261).
- **Description:** Contrasts conventional serial kinematic chains characterized by discrete rigid links and articulated pin/ball joints (e.g. Kuka industrial manipulator) with continuum robots having an infinite-DOF curvilinear elastic structure (e.g. Hansen Medical catheter robot).
- **Role in MP1:** Visual anchor for Section C1.1 and C2.2.1 defining the continuum robot class, where flexibility is distributed throughout the backbone rather than localized at discrete hinges.

### 2.2. M04 — Fig. 2(a–d): Operational Stiffness Calculation Methods
- **Source:** Lin, Song, and Wang (2024), p. 2.
- **Description:** Illustrates the four primary boundary and loading conditions used to quantify flexible robot stiffness:
  - *(a)* End-effector lateral force $F$ producing deviation $d$.
  - *(b)* Pure torque $\tau$ producing rotational angle $\theta$.
  - *(c)* Three-point bending of a beam supported at both ends with central transverse load $F$ and midpoint deflection $\Delta w$.
  - *(d)* Cantilever beam with fixed base and distal transverse force $F$ producing end deflection $\Delta w$.
- **Role in MP1:** Primary visual taxonomy for Section C1.1.3 and C2.3.1, establishing why reported stiffness values depend intrinsically on the chosen operational setup and why flexural rigidity ($EI$) must be distinguished from linear spring stiffness ($K = F/\Delta w$).

### 2.3. M05 — Jamming Classification: Fig. 5(g) & Table 4 (Fibre Jamming)
- **Source:** Fan et al. (2024), Section 3.3.1 (p. 10), Fig. 5(g) (p. 10), Table 4 (p. 11).
- **Description:** Illustrates fibre/filament jamming (FJ) composed of axially aligned polymer/glass/abrasive fibres inside a sealed flexible envelope. When a vacuum is drawn, atmospheric pressure compresses the fibres together, engaging Coulomb friction along their contact lines to resist axial shear and bending.
- **Role in MP1:** Used in Section C1.1.3 and C2.3.1 to distinguish 1D fibre-based jamming mechanisms from 2D layer-based jamming mechanisms.

### 2.4. M05 — Jamming Classification: Fig. 5(e, f) & Table 4 (Layer Jamming)
- **Source:** Fan et al. (2024), Section 3.3.3 (p. 11), Fig. 5(e, f) (p. 10), Table 4 (pp. 11–12).
- **Description:** Illustrates layer/laminar jamming (LJ) structures, showing double-flap patterns (5e) and their integration into tendon-driven continuum manipulator segments (5f). Table 4 lists material types (paper, spring steel, Neobond) and actuation types.
- **Role in MP1:** Key classification reference for Section C2.3.1 and C2.5.5, illustrating practical implementations of layer jamming in continuum robots and confirming that the review provides macroscopic taxonomy without an analytical local traction model.
