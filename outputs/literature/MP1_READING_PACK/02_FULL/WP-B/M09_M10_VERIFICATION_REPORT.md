# M09/M10 source verification report

**Purpose.** Verify the two supplied primary PDFs for mechanism, geometry, materials, figure/section locators, and relevance to P1. Evidence labels below mean `VERIFIED FULL TEXT` unless explicitly marked otherwise. This report does not change a verification-round registry or final scientific state.

## M09 — Bai et al. (2022), wire jamming

### Identity and provenance

- **Title:** *Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming*
- **Authors:** Long Bai, Hao Yan, Jiafeng Li, Jiefeng Shan, Penghao Hou.
- **Venue/metadata in PDF:** *Applied Sciences* 2022, 12, 3582; published 1 April 2022.
- **DOI:** `10.3390/app12073582` (printed in the article citation, p. 1).
- **Source:** `data/chap1-2_citations/M09__2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf`
- **SHA-256:** `240fbf60229a87953954c85c3d858bebf945c06c2689f5dcb7c8d5c51742b2b5`
- **PDF extent:** 14 physical pages; article printed pagination is 1–14. Physical page numbers below are PDF page indices.
- **Verification status:** `VERIFIED FULL TEXT` (PDF text, captions, equations/sections and quantitative conditions checked). No DOI conflict found.

### Verified claims and conditions

1. **Mechanism and model level (Sec. 2.1–2.2, physical pp. 4–6; Fig. 2).** The structure is an airtight HDPE envelope containing discrete inextensible wires/ropes. Vacuum changes normal compression and therefore wire–wire friction, switching the medium from separate beams (vacuum off) to a jammed beam (vacuum on). The paper uses a cantilever/Euler–Bernoulli model and treats wire count, single-wire diameter and material properties as stiffness drivers. This is **wire/fiber jamming**, not laminar sheet jamming and not granular jamming.
2. **Material and geometry choices (Sec. 2.1, physical pp. 4–5; Fig. 2d–f).** Candidate media are kraft rope (one-strand twisted kraft paper), hemp rope (two-strand twisted rope), and nylon PA6 wire. The authors empirically select 1 mm diameter wires. The envelope is HDPE film; final layout is installation layout 2 with a rectangular wire arrangement. A circular arrangement is reported as more prone to circumferential sliding/misalignment and pre-jamming. Layout 2 is selected because it avoids severe compression/stretching after bending.
3. **Wire placement and end effects (Sec. 2.1, physical pp. 5; Fig. 2g–k).** Bending creates a free-end gradient because wires and membrane have different bending radii. Local twisting/arching can cause irreversible deformation; a slightly longer envelope or reverse-gradient trimming of free wire ends reduces the gradient. These are placement/end-condition effects, not a homogenized layer-count validity study.
4. **Characterization conditions (Sec. 3.1, physical pp. 8–9; Fig. 4).** Three-point bending and torsion tests use a slow force-sensor speed; each test is repeated five times. Representative wire length is 140–150 mm and the figure caption reports a 6 mm structure thickness (`d = 6 mm`). For the three media, tests compare 0 and −60 kPa vacuum. Vacuum increases stiffness; nylon has higher stiffness but higher initial stiffness/localized rearrangement, while hemp has lower stiffness attributed to frictional sliding and fiber branches. Kraft rope is selected for subsequent studies.
5. **Slip regimes (Sec. 3.1, physical p. 9; Fig. 4g).** The paper describes pre-slip/cohesive, transition/nonlinear slip onset, and post-slip/full-slip regimes from force–deflection behavior. This is an author interpretation of system-level curves; local inter-wire slip is not independently tracked or mapped to a constitutive validity boundary.
6. **Application conditions (Sec. 3.2–3.3, physical pp. 10–12; Fig. 5).** At 90° bending, the assembled actuator requires 145 kPa positive pneumatic pressure versus about 87 kPa for the actuator alone; the wire-jamming vacuum is separately varied (0 to −85 kPa). The paper reports approximately doubled gripper grasping mass from 0 to −85 kPa and glove lifting over 10,000 g. These are prototype/application outcomes, not independent constitutive validation.

### Limitations and P1 relevance

- **Reported limitations:** Velcro is non-stretchable and limits some glove applications; nylon shows localized rearrangement; end-gradient effects require trimming. The paper does not report an uncertainty budget, local contact-pressure measurement, or independent validation of a homogenized high-layer-count model.
- **Scope limitation for P1:** discrete wires/ropes in an HDPE envelope differ mechanically from stacked flexible sheets in a vacuum layer-jamming beam. Wire count `n1` appears in the beam model, but this is not evidence that a homogenized slip model for high layer counts has been validated or falsified.
- **Status for audit:** `VERIFIED FULL TEXT`; useful as a **mechanism/terminology boundary and adjacent comparator**, not a direct P1 prior-art closure. Claims above are `AUTHOR_RESULT` unless identified as interpretation (slip regimes).

## M10 — Liu et al. (2021), positive-pressure granular jamming (**COMPARATOR**)

### Identity and provenance

- **Title:** *A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots*
- **Authors:** Tianxin Liu, Haisheng Xia, Dae-Young Lee, Amir Firouzeh, Yong-Lae Park, Kyu-Jin Cho (Tianxin Liu and Haisheng Xia are co-first authors).
- **Venue/metadata in PDF:** *IEEE Robotics and Automation Letters*, vol. 6, no. 4, October 2021; article pages 8078–8085; publication date 14 July 2021.
- **DOI:** `10.1109/LRA.2021.3097255` (printed on PDF p. 1).
- **Source:** `data/chap1-2_citations/M10__2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf`
- **SHA-256:** `182d8546102f3fb4d6bbd1bb3e3b86c55330ceabe2375364990d17f494af5b58`
- **PDF extent:** 8 physical pages (IEEE printed 8078–8085).
- **Verification status:** `VERIFIED FULL TEXT`; **audit role: `COMPARATOR`**. No DOI conflict found.

### Verified claims and conditions

1. **Mechanism and Fig. 1 (Sec. II-A, physical p. 2, IEEE printed p. 8079; Fig. 1).** A soft rubber bladder and silicon tube sit concentrically inside granules contained by a cylindrical, non-stretchable fabric sleeve and end caps. Positive air inflates the bladder, transmitting force to and compressing the granules; the sleeve constrains volume and the jammed granular medium stiffens the unit. Fig. 1c prototype is 26 mm diameter × 50 mm length.
2. **Distinct mechanism from M09/P1.** M10 is **positive-pressure granular jamming**: pressure path is bladder → granules → fabric sleeve, with particle rearrangement/friction. It does not use discrete wire/rope contacts, stacked laminar sheets, or vacuum-induced interlayer friction. It therefore cannot by itself validate a wire/layer homogenized slip model; it is retained as a comparator for pressure sign, granular versus wire/laminar medium, and effective-stiffness modeling.
3. **Self-locking layout and Fig. 2 (Sec. II-A, physical pp. 2–3; Fig. 2).** Multiple PPJ units are serially connected by a rotational joint and paired sandpaper friction pads. Inflation both jams granules and compresses pads, allowing shape locking; reported rotation range is −50° to +50° for the two-unit prototype.
4. **Material and test conditions (Sec. II-B–III-A, physical pp. 3–4, IEEE 8080–8081; Figs. 4–6).** Granules are SMP cuboids about 2 × 2 × 3 mm; the outer sleeve is single-ply non-stretchable fabric and the bladder is molded silicon/commercial latex. A 26 mm × 50 mm PPJ module is tested in cantilever bending. Comparators include a same-size rubber bladder and a negative-pressure jamming module. Tests use +62 kPa for PPJ baseline comparison; pressure-modulation tests use 69, 103, 138 and 172 kPa relative pressure. Four first-1-mm stiffness values are 0.69, 1.72, 2.75 and 4.02 N/mm; curves are means of eight repeats with 95% confidence intervals in Fig. 6.
5. **Effective model (Sec. III-C, physical pp. 4–5, IEEE 8081–8082; Eqs. (1)–(5), Fig. 7–8).** Under assumptions of a fully jammed annular section, tiny deformation and no granule slip, the paper defines an effective Young’s modulus `E = C/(D²−d²)` and cantilever stiffness `K = 3πC(D²+d²)/(64L³)`, with `C` absorbing pressure/material factors. This is a geometry- and condition-dependent effective relation, not a constitutive law for vacuum layer-jamming beams.
6. **Limitations (Sec. V, physical pp. 7–8, IEEE 8084–8085).** One PPJ unit cannot take arbitrary shapes; performance and maximum angle depend on initial granule distribution and fill fraction. The soft bladder can deform at positive pressure, reducing jamming effect; sandpaper friction pads can wear. Faster response is stated as potential, but transition time still requires testing. The authors also propose partitions to stabilize granule distribution.

### Comparator disposition

`COMPARATOR — RETAIN, NOT A DIRECT P1 THREAT.` M10 supplies a clear positive-pressure granular-jamming control case and an effective-modulus model with explicit geometric assumptions. Its mechanism, medium, and pressure path are materially different from high-layer-count vacuum-jammed beams; do not merge its equations or performance numbers into P1 evidence.

## Cross-paper conclusion

M09 verifies an adjacent **wire/fiber-jamming** family with discrete contact/slip and layout-sensitive end effects. M10 verifies a mechanistically distinct **positive-pressure granular-jamming** family and is explicitly a comparator. Neither paper, on the supplied full text, demonstrates an experimentally validated homogenized slip model for high-layer-count vacuum **laminar** jamming beams. That last sentence is a scoped evidence statement, not a global novelty claim.

