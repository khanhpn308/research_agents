# MP1-V002 WR1-S01 — Existing-Formulation Audit and Strongest H0b

**Stage:** WR1-S01, low-cost analytical triage.
**Date:** 2026-09-26 (Asia/Bangkok).
**Scope:** Existing repository corpus only; five named formulations audited against their PDFs.
**Evidence status:** Formulation-level analysis completed; no MP1 simulation, calibration, pilot, or held-out validation has occurred.
**Scientific state:** H0a = REFUTED_IN_TRANSFORMATION_REGIME; H0b = NOT_FALSIFIED / LIVE COMPETITOR; H1 = INSUFFICIENT_EVIDENCE.

## Research question and decision

Can existing mechanics already represent the pressure-confined, superelastic NiTi wire-bundle bending system well enough to serve as the strongest H0b competitor?

**S01 answer: EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE.** A component-resolved 3D finite-element model can combine an established history-dependent NiTi transformation update, frictional wire contact, a deformable sleeve, external fluid pressure, measured prestrain and bending. This is an **INFERENCE from compatible full-text formulations**, not a claim that any cited paper has implemented or validated the whole MP1 bundle. No exact mechanically missing field equation has been established. Transfer and quantitative adequacy remain untested. GAP-07 is analytically triaged but its empirical resolution, and GAP-01, remain open.

The competitor selected here is deliberately stronger than a constant-modulus substitution. H0a's failure in a transformation regime does not support a distinct H1 law.

## Methods and evidence hierarchy

The W02 source manifest and the WR1 routing files defined the closed corpus. I read the repository PDFs of Barsi (2025), Tjahjanto (2017), Xin Liu (2004), Kang (2020) and Vahidi (online 2021; corpus file labeled 2022), and checked their methods against the W2-04 role matrix and the canonical W02 K/gap registers. Full-text PDF statements take precedence over worker summaries where these conflict. The structured crosswalk gives each source's kinematics, contact, constitutive law, applicability and exact repository pointer.

No literature search or targeted retrieval was run. This audit does not establish novelty, formulate H1, compare directions, or fit validation data.

## What the named formulations actually provide

| Formulation | Verified contribution | Transfer limit |
|---|---|---|
| **Barsi et al. 2025** | **VERIFIED FULL TEXT:** Shear-deformable short-rope beam; individual curved rods; eigenstrain hypotheses for perfect stick, partial stick and full slip; generalized six-component stiffness. Section 2, Eqs. (1), (2), (6), (7), (11), (12), (18). | It calculates **limit-state stiffness bounds**, not a local evolving Coulomb traction law or a pressure-dependent transition path. Linearized deformation, common rotations and a uniform slip-state assumption restrict direct transfer. A nonlinear NiTi tangent would require rederivation, not merely swapping one constant E in its published closed form. |
| **Tjahjanto et al. 2017** | **VERIFIED FULL TEXT:** Geometrically nonlinear 3D FE of cores, fillers, armour and sheaths under bending, axial strain and outer radial pressure. Normal penalty contact and tangential Coulomb friction; the analytical comparator's Eq. (6) distinguishes available friction f from inner/outer contact lineloads. | Published constituent materials are elastic and the FE resolves cable components, not every MP1 wire. The analytical loxodromic simplification and its neglect of same-layer contact should not be imposed on a straight packed MP1 bundle. Its fixed 0.2 MPa load case is evidence that pressure is an outer boundary input, not proof of MP1's pressure-transfer map. |
| **Xin Liu 2004** | **VERIFIED FULL TEXT:** MSc thesis with a one-dimensional transverse cable equation and an EI-curvature relationship supplied by CableCAD using measured internal layer pressures (Chapters 2–3; Appendix A). | The vibration PDE does not generate local contact tractions or NiTi transformation state. It is a reduced response comparator only unless an independent contact/material solver supplies EI. |
| **Kang et al. 2020** | **VERIFIED FULL TEXT:** Incremental transformation-aware SMA UMAT in a 3D solid FE tensile model; temperature and material state are represented (English abstract; Section 1; model setup). | Reported interwire contact is smooth/frictionless. The paper does not validate a frictional beam-contact formulation or pressure-controlled bending. Coulomb contact and the MP1 sleeve must be added. |
| **Vahidi et al. online 2021 / corpus-labeled 2022** | **VERIFIED FULL TEXT:** 3D solid wire-rope FE, surface contact with interwire friction, and Souza's history-dependent 3D SMA model in UMAT. Section 2 Eqs. (1)–(8) show transformation strain, temperature dependence and a transformation surface; Section 4 reports wire geometry, contacts and tensile loading. | It studies helical ropes in tension, without pressure sleeve or MP1 bending. Its PDF names **Souza**, not Auricchio–Petrini, as the implemented material model. Its published tension comparison is not locked independent MP1 bending validation. |

The PDF check also found bibliographic and method errors in the historical W2-04 worker matrix. Kang is described there as a corotational Coulomb beam model with bending validation, but its PDF uses SMA solid elements, smooth contact and tensile loading. Tjahjanto's PDF identifies **Jonathan Mullins** and proceeding **OMAE2017-62553**; the worker row gives another first name and proceeding identifier. Xin Liu's repository item is a **thesis**, and no DOI is verified from that PDF. These are S01 provenance corrections only; the historical matrix is preserved. Barsi's abstract and Section 2 explicitly limit the model to stiffness bounds; treating it as a solved local pressure-dependent stick-slip transition overstates the paper.

## Strongest H0b specification

The most defensible existing-mechanics baseline is **explicit-wire 3D thermomechanical FE contact with a deformable pressurized membrane**, using:

1. The **actual** MP1 wire count, diameters, packing, initial curvature, surface condition and assembly prestrain.
2. An established 3D NiTi material update with transformation strain as a history variable and temperature-dependent thresholds. Souza's law in Vahidi is a verified precedent. A different established law can be selected from independent single-wire calibration and algorithm verification before lock; the choice cannot be made by held-out bending fit.
3. Frictional wire-to-wire surface contact with separation, normal traction and tangential stick/slip. The friction capacity depends on **local normal contact traction**, not directly on chamber pressure.
4. A deformable membrane/sleeve with measured properties. Fluid pressure p(t) is prescribed on the **fluid-wetted membrane boundary**. Contact and membrane equilibrium determine the distributed internal normal tractions. An independently calibrated, uncertainty-bounded pressure-transfer representation is required.
5. Measured axial prestrain/prestress, clamps, fixture compliance and bending history. The 3D model must permit finite bending, wire rotation/sliding and section shape change over the declared domain.
6. Material/contact history and, if S02 pilots show meaningful self-heating or rate effects, a coupled thermal field. A nominal quasi-static setting is not evidence of isothermality.
7. Independently calibrated physical parameters; convergence-controlled numerical parameters; frozen code, parameter file, uncertainties, paths, metrics and tolerances before untouched validation data.

**Generic formulation sketch (INFERENCE, not a quoted paper equation).** For each wire i, enforce mechanical balance div(sigma_i)+b_i=0 in the selected finite-deformation formulation, with sigma_i=F(epsilon_i,z_i,T_i;theta_NiTi) and a verified evolution update for transformation state z_i. At contact, enforce nonpenetration and compressive normal traction, with tangential traction below mu times local normal traction in stick and opposing relative sliding at the friction bound. On the fluid-wetted sleeve, apply the pressure traction with a declared sign convention. The mapping from measured p(t) to each contact traction is an **output of membrane/packing/contact mechanics or an independently calibrated bounded latent map**, not the identity p=f_n. Here sigma_i is wire stress, b_i is body force density, epsilon_i is the selected strain measure, z_i is the transformation internal state, T_i is wire temperature, theta_NiTi is the independently calibrated material parameter set, mu is wire friction coefficient, and p(t) is measured chamber pressure history. Contact traction is a local stress distribution, whereas an interwire normal force is its integral over the relevant contact patch; neither is numerically identical to chamber pressure. The model's exact weak form, element technology and contact enforcement will be fixed and verified at S05.

A 3D explicit-wire formulation is favored because it avoids assuming a helical lay, uniform slip state or unchanged cross-section. Barsi's states remain useful **limit checks** for a reduced model within their assumptions; they are not substituted for the forward frictional contact solve.

### Physical versus numerical parameters

**Physical parameters** include single-wire NiTi moduli, transformation thresholds/hardening and temperature coefficients; measured friction properties; membrane thickness and constitutive behavior; wire geometry, packing, prestrain, initial contact state, fixture compliance and pressure-transfer uncertainty. Their provenance must be independent of held-out bending.

**Numerical parameters** include normal/tangential penalty stiffness, smoothing or elastic-slip regularization, mesh size and element order, increment size, solver tolerances and stabilization. They are chosen by penetration, convergence, equilibrium and energy checks. Changing them to improve agreement with held-out bending would be validation leakage.

## Applicability assumptions and remaining mechanical absence

The major transfer assumptions are documented individually in the assumption register. The strongest are: the actual packing and membrane can be meshed without replacing them by helical cable geometry; single-wire NiTi constitutive behavior is independently characterized in bending-relevant tension/compression and temperature states; wire friction and pressure transmission are separately constrained; thermal effects are bounded or modeled; and numerical contact regularization does not control the scientific verdict.

**No new field law is presently shown to be mechanically absent.** A finite-deformation contact/material/membrane system can in principle represent the specified loading and local degrees of freedom. What remains absent from the *published examples* is the exact combined MP1 geometry/loading implementation, independently calibrated pressure transfer, local observables and a locked forward prediction. These are ordinary but nontrivial adaptation, calibration, measurement and verification tasks. If a later locked H0b has systematic residuals correlated with independently observed local mechanisms, that would motivate a separate later inquiry; S01 does not identify a new constitutive term.

## Candidate observable signatures for S03

The separate register predeclares expected sensitivity of slip onset, transformation onset, local strain, curvature, temperature, cross-section shape, membrane deformation, chamber pressure, local contact traction and global moment-curvature loops. The critical composite idea is to separate a pressure-associated shift in local slip threshold from a thermomechanical shift in transformation onset while monitoring section shape and fixture effects. This is **INFERENCE** from H0b and a design input to S03. S02 has not established that sealed, non-perturbing channels can measure these states. A global M–kappa curve alone is non-identifying.

## Calibration and validation governance

The partition file assigns independent single-wire thermomechanical tests, friction/direct shear or pull-out, membrane coupon/inflation, pressure-transfer/section tests, geometry/packing metrology, prestrain and fixture characterization to future calibration. It reserves future pressure-curvature-temperature bending paths/specimens as held-out. S05 must lock code, physical estimates with covariance or bounds, numerical settings, metrics, uncertainty propagation and tolerances before S06 acquisition/unblinding. S07 may evaluate one frozen forward prediction. Any fit to held-out data fails that model version and requires a new untouched validation set.

The existence of this plan does not mean any parameter is already independently identified. In particular, mu and pressure transmission can compensate in slip predictions, while material, membrane and fixture compliance can compensate in global stiffness.

## GAP-07 result, retrieval state and downstream limits

**GAP-07:** formulation-level kill test yields **EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE**. It withdraws any rationale that a new coupling law follows simply from the inability of a constant-modulus beam or from the use of NiTi plus pressure. It **does not** determine H0b empirical adequacy. That remains with S02 → S03/S04 → S05 model lock → S06 held-out experiment → S07 forward comparison.

**Targeted retrieval:** CLOSED. The necessary named governing ingredients and applicability conditions are in the local PDFs. Vahidi does not specify every contact-regularization implementation detail in the checked text, but this does not block S01 because the chosen contact formulation and convergence tests belong to S05. No broad or targeted search occurred.

**Unresolved evidence gaps:** Actual sealed coexistence of slip and transformation; instrumentable local states; pressure-to-contact transfer; independent parameter identification; thermal branch decision; mesh/solver convergence; and locked forward adequacy. All eight W02 blocking gaps remain open at the scientific gate.

## Direct answer to the work-order question

The strongest H0b MP1 must defeat is a fully resolved, transformation-aware NiTi wire FE model with frictional contact and a deformable pressure-loaded membrane, calibrated independently and locked before held-out bending. Existing papers separately demonstrate the essential material/contact architecture and pressure/bending/contact architecture. Transfer requires measured MP1 packing and prestrain, membrane mechanics, a calibrated uncertain pressure-to-contact map, an appropriate NiTi temperature/history law, validated contact settings and real boundary conditions. No missing governing coupling term is demonstrated before the model-discrimination experiment; the missing evidence is whether this strongest existing model predicts the actual bundle adequately.

## References and provenance

- **VERIFIED FULL TEXT:** F. Barsi, B. Carboni and W. Lacarbonara (2025), *A new mechanical model of short wire ropes: Theory and experimental validation*, *Engineering Structures* 323, 119217, DOI 10.1016/j.engstruct.2024.119217. Repository PDF: data/papers/verification/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf. Paper ID 9f4295be23.
- **VERIFIED FULL TEXT:** D. D. Tjahjanto, A. Tyrberg and J. Mullins (2017), *Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable*, ASME OMAE2017-62553. Repository PDF: data/papers/verification/MP1-V002/A6-2017-Bending Mechanics of Cable Cores and Fillers in a Dynamic Submarine Cable.pdf. Paper ID ccdc1bb980. DOI unverified in repository PDF.
- **VERIFIED FULL TEXT:** X. Liu (2004), *Cable Vibration Considering Internal Friction*, MSc thesis, University of Hawaii. Repository PDF: data/papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf. Paper ID aaad9c248c. No DOI verified.
- **VERIFIED FULL TEXT:** Z. Kang, Z. Wang, B. Zhou and S. Xue (2020), *Finite Element Method for Mechanical Behavior of Shape Memory Alloy Superelastic Cables*, *Journal of Mechanical Engineering* 56(14), DOI 10.3901/JME.2020.14.065. Repository PDF: data/papers/verification/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf. Paper ID 56793dea9b; filename year is misleading.
- **VERIFIED FULL TEXT:** S. Vahidi, J. Arghavani, E. Choi and A. Ostadrahimi (published online 2021; corpus file labeled 2022), *Mechanical response of single and double-helix SMA wire ropes*, *Mechanics of Advanced Materials and Structures*, DOI 10.1080/15376494.2021.1955313. Repository PDF: data/papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf. Paper ID 53200aa0c6.
- **Repository authority:** outputs/execution/MP1-V002/W2/MP1_W02_SOURCE_MANIFEST.json; MP1_W02_K1_K9_RECONCILED_MATRIX.json; MP1_W02_BLOCKING_GAP_REGISTER.json; outputs/execution/MP1-V002/WR1/MP1_WR1_STAGE_GATE_REGISTER.json.
- **AI assistance:** This analytical crosswalk and inference were prepared with AI assistance; source-level claims were checked against the repository PDFs. No new experiment or external source verification was performed.
