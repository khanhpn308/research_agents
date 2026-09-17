# Verification Matrix

**Verification ID:** D1-V004
**Paper count:** 15
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — BENDING STRESS ENHANCEMENT IN MATERIALS WITH LIMITED SHEAR RESISTANCE-PART I. SLIPPING-LAYERS MODEL

- **paper_id:** `66fcf766cb`
- **year:** 1993
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- frictionally coupled layers
- interlayer frictional slip
- overhang-induced stiffening

### Modeling Methods

- Discrete slipping-layers beam theory treating the cross-section as n elastic layers coupled by frictional interfaces with finite shear strength tau_p.
- Application of the generalized Bernoulli hypothesis ('plane sections remain plane') to each layer individually, yielding linear normal stress and parabolic shear stress profiles.
- Section and beamlet partitioning technique demarcated by slip zone endpoints and external concentrated load locations.
- Formulation of equilibrium equations for individual beamlets and continuity of vertical deflection and curvature derivatives across non-slipping and slipping interfaces.
- Enforcement of continuity of layer axial forces, bending moments, and normal stresses across section boundaries.
- Integral continuity condition requiring zero net tangential relative displacement across each slip zone.
- Exploitation of beam symmetries (about x = 0 and y = 0) and numerical resolution of non-linear slip zone extents using Powell's optimization method under monotonically incremented loading.

### Performance Metrics

- Normalized maximum axial stress ratio S_i,max / sigma_max (layer peak axial stress divided by the maximum axial stress in a solid beam under identical load).
- Dimensionless slip initiation load ratios P_si / P_s8 and complete slip load ratios P_Ci / P_s8.
- Normalized midspan deflection w(0) / H.
- Normalized half-length of interfacial slip zones r_i = R_i / L.

### Future Work

- Presenting Part II containing a simplified continuum theory for a shear-weak unlayered beam to circumvent the computationally demanding discrete-layer analysis (pages 1, 2, 12).
- Demonstrating the formal equivalence between the discrete slipping-layers model and the shear-weak unlayered continuum beam model as the number of layers n becomes large (pages 1, 2).
- Investigating the detailed dependence of bending stress enhancement on layer count n and span-to-depth aspect ratio L/H in Part II (page 8).
- Using the simplified theory in Part II to infer practical levels of bending stress enhancement expected in physical composite materials (pages 1, 12).

## V02 — Bending Stress Enhancement in Materials with Limited Shear Resistance-Part II. Unlayered Shear-Weak Model

- **paper_id:** `f00d886124`
- **year:** 1993
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Modeling Methods

- Unlayered shear-weak beam continuum model based on classical perfect plasticity with infinite anisotropy (Hill, 1948).
- Piecewise cross-sectional stress formulation dividing the section into an inner plastic core (tau = tau_p, sigma = 0) and outer elastic regions governed by modified beam theory.
- Equilibrium and cross-sectional strain continuity conditions used to determine the plastic boundary Hp(x) and surface stress enhancement.
- Curvature calculation through integration of axial strain variation across the elastic beam portion.
- Asymptotic limit analysis (n -> infinity) of a third-order algebraic equation governing slipping interfaces in discretely layered beams.
- Bending moment versus shear force failure locus modeling for combined loading states.

### Performance Metrics

- Percentage error e1 = [V - V*(n*)] / V*(n*) for shear force required to achieve a given plastic zone size.
- Percentage error e2 = [S_max - S_max^n] / S_max^n for maximum surface tensile stress between unlayered and layered models.
- Stress enhancement ratio S_max / sigma_max^e (ratio of maximum tensile stress to elastic beam theory stress).
- Normalized failure load ratio P / P_max in three-point bending.
- Critical length-to-height aspect ratio threshold (L/H)* = sigma_max / (2 tau_p).

### Future Work

- Detailed quantitative comparison between the unlayered shear-weak model predictions and experimental results on carbon-fiber reinforced glass matrix composites is indicated as reported in a companion work (Steif and Trojnacki, 1992).
- Simultaneous determination of stress resultants and deflections in statically indeterminate beam configurations.

## V03 — A relative gradient theory for layered materials

- **paper_id:** `2f85ad579a`
- **year:** 1998
- **doi:** 10.1051/jp4:1998833
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Modeling Methods

- Relative gradient continuum theory incorporating relative spin and relative curvature tensors.
- Virtual work principle formulation for infinitesimal deformation and incremental virtual work for finite deformation.
- Elasto-plastic interface constitutive modeling with friction angle and cohesion (Mohr-Coulomb type criterion and plastic potential).
- Generalized 1D layered beam theory incorporating macro- and micro-element equilibrium and kinematic rotations.
- Analytical derivation of crack extension force for laminated beam compliance testing.
- Homogenization and scale-dependent parameter renormalization for layered media.
- Finite element analysis using 250 eight-node isoparametric continuum elements and 4x25 six-node joint elements.
- Eigenvalue buckling analysis for layered beam columns under axial prestress.

### Performance Metrics

- Normalized center displacement v_0 / v_0^infty.
- Relative percentage difference between gradient beam model predictions and finite element calculations (less than 5%).
- Normalized crack extension force g / g_infty.
- Critical dimensionless horizontal buckling load/stress sigma^*.
- Asymptotic recovery of exact classical limits at zero and infinite interface shear stiffness.

### Future Work

- Application of the relative gradient ideas to regular dislocation structures with couple stresses and single slip in crystalline materials.
- Extension to granular material theories with isotropic or multidirectional contact distributions where interfacial slip occurs across multiple orientations.
- Comprehensive formulation of large-deformation problems without neglecting higher-order geometric nonlinearities.

## V04 — Assessment and correction of theories for multilayered plates with imperfect interfaces

- **paper_id:** `33ea203427`
- **year:** 2014
- **doi:** 10.1007/s11012-014-9994-x
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Modeling Methods

- Two-length-scales displacement field superposition combining global C1 thickness displacements, C0 zigzag enrichment functions, and discontinuous interfacial displacement jumps (pages 2, 4-5).
- A priori imposition of interfacial transverse shear and normal traction continuity conditions to homogenize the formulation into 5 (sliding) or 6 (mixed-mode) global displacement variables independent of layer number (pages 1, 5-6).
- Hamilton's elastokinetic principle / principle of virtual work including interfacial strain energy terms from imperfect interfaces (pages 7, 19).
- First-order shear deformation theory incorporating a shear correction factor K2 (pages 15, 24-25).
- A posteriori derivation of transverse shear stresses from longitudinal bending stresses via local cross-sectional equilibrium equations (pages 13, 15).
- Exact 2D elasticity benchmark formulation extending Pagano's stress-function solution in cylindrical bending to multilayered plates with elastic interfaces (pages 14, 26).

### Performance Metrics

- Relative percentage error of interfacial shear tractions compared to exact 2D elasticity solutions (pages 14, 15).
- Normalized transverse deflection ratio w / w_2D compared to exact elasticity solutions (pages 16, 18).
- Through-thickness distribution and interface continuity of transverse shear stresses sigma_23 and longitudinal displacements v2 (pages 14-17).
- Physical consistency and monotonicity of transverse shear resultant Q2 across varying interfacial stiffnesses (avoidance of slip-locking anomalies) (pages 15-16).

### Future Work

- Validation of the proposed homogenized formulation for general mixed-mode interfaces involving normal opening separation and contact (BN != 0 and w_jump != 0) (page 18).
- Formulation of an interfacial-stiffness-dependent shear correction factor to accurately predict transverse displacements in thick, highly orthotropic plates with very compliant interfaces (pages 15, 17, 18, 25).
- Resolution of boundary region inconsistencies in clamped plates under intermediate interface stiffnesses (page 13).
- Application of the affine interface formulation to progressive delamination modeling with nonlinear cohesive laws approximated as piecewise linear functions (pages 2, 4, 18).
- Extension of the corrected formulations to buckling, vibration, blast, impact, and thermo-magneto-electro-mechanical loading problems (page 18).

## V05 — INFLUENCE OF SLIP EFFECT ON BENDING CHARACTERISTICS OF FRICTIONAL LAMINATED BEAMS

- **paper_id:** `47fe4949dc`
- **year:** 2016
- **doi:** 10.6052/j.issn.1000-4750.2015.12.0952
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- interfacial friction
- Coulomb friction

### Modeling Methods

- Analytical derivation of cross-sectional shear stress and equilibrium equations incorporating interfacial Coulomb friction
- Transfer matrix method for discrete multi-node beam elements under axial and lateral loads
- Incremental superposition method for tracking load-dependent slip front propagation
- Finite element modeling in ANSYS using BEAM3 beam elements, rigid arm elements, and iterative degree-of-freedom release/coupling to simulate stick-slip contact

### Performance Metrics

- Midspan deflection (mm)
- Interfacial slip length and number of slipped elements along the span
- Critical slip shear force (N)
- Cross-sectional moment of inertia (mm^4)
- Maximum bending stress (MPa) and percentage increase in flexural stress due to slip effect (%)
- Agreement between transfer matrix calculations and ANSYS finite element results

## V06 — A homogenized structural model for shear deformable composites with compliant interlayers

- **paper_id:** `8113666e96`
- **year:** 2018
- **doi:** 10.1007/s41939-018-0032-x
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- thin compliant interlayers
- sliding interfaces controlled by linear-elastic interfacial tangential stiffness
- uniformly distributed mechanical fasteners (nails, dowels, screws, pins, stitches)

### Modeling Methods

- Homogenized structural zigzag theory extending Tessler et al. (2009) refined zigzag kinematics to zero-thickness imperfect interfaces using Massabò and Campi (2014) multiscale strategy
- Principle of virtual work / variational derivation of homogenized equilibrium equations and boundary conditions
- Closed-form decoupling of the eighth-order system of governing differential equations
- A posteriori transverse shear stress recovery via integration of local equilibrium equations
- Benchmarking against 2D elasticity solutions (transfer matrix method) and discrete layer interface models

### Performance Metrics

- Comparison of mid-span transverse displacement with exact 2D elasticity solutions and relative percentage error
- Through-thickness distribution of longitudinal displacement and interfacial slip jumps compared to 2D elasticity
- Through-thickness distribution of bending normal stress and a posteriori transverse shear stress compared to 2D elasticity
- Interfacial shear traction distribution along the span compared to discrete layer interface models
- Continuity and deformed shape profiles across in-plane interface discontinuities in ENF specimens

### Future Work

- Extending the homogenized framework to two-dimensional plate and shell structures
- Incorporating generally nonlinear interfacial traction laws (e.g., piecewise linear cohesive laws) to simulate damage, delamination growth, and connector nonlinearity
- Accounting for interfacial normal tractions and transverse opening displacements to model peel stresses and asymmetric layups accurately

## V07 — Bending Stiffness of Parallel Wire Cables Including Interfacial Slips among Wires

- **paper_id:** `9c2773e4cd`
- **year:** 2018
- **doi:** 10.1061/(ASCE)ST.1943-541X.0002171
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- interfacial slip among wires
- friction among wires
- axial tension / average tensile stress affecting slip rigidity

### Modeling Methods

- Multilayer rectangular laminated beam idealization with interlayer slips
- Governing differential equilibrium equations for multilayer composite beams under axial tension and transverse loads
- Analytical closed-form solutions for deflection and equivalent bending stiffness under uniform and concentrated loading
- Euler-Bernoulli classical beam theory relations for individual layers and bounding states
- State space method (SSM) numerical modeling used as a verification benchmark
- Empirical linear least-squares regression relating slip rigidity to average tensile stress

### Performance Metrics

- Deflection magnification coefficient (delta = w_max / w_max_bar)
- Equivalent bending stiffness coefficient (EI_eff / EI_infinity = 1 / delta)
- Relative error in deflection magnification compared to classical beam theory in limit states (%)
- Fundamental natural frequency (omega_eff) and relative error compared to zero bending stiffness ((omega_eff - omega_0) / omega_0 * 100%)

### Future Work

- Conducting additional experimental tests to investigate the realistic behavior of wires during bending.
- Extending the approximated linear formulation between tensile stress and slip rigidity to a nonlinear formulation for more accurate bending stiffness calculation.

## V08 — Mechanism research of slip effect between frictional laminated beams

- **paper_id:** `ee464a718b`
- **year:** 2019
- **doi:** 10.1177/1687814019828461
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- Coulomb friction
- interlayer slippage
- interlayer friction

### Modeling Methods

- Segment micro-element method
- Euler-Bernoulli beam theory
- Section analysis method
- Transfer matrix method (TMM)
- Laplace transform / Laplace transfer method
- Incremental iterative recursive algorithm (implemented in MATLAB)
- Finite element numerical simulation (ANSYS using BEAM188 3D beam elements and rigid arm coupling units)

### Performance Metrics

- Displacement comparison and agreement between ANSYS FEM and proposed TMM algorithm across span and substeps
- Shear force comparison and relative numerical error between FEM and proposed algorithm
- Maximum shear force at rigid girder coupling nodes (11.9 N simulated vs. 12.3 N calculated ultimate friction resistance)
- Number of slipped elements and longitudinal length of interlayer slippage per load substep
- Midspan vertical displacement variation with and without considering slip effect

### Future Work

- Mechanical analysis of local bending behavior of the laminated beam under interlayer slip effect across different axial force conditions.
- Achieving a better understanding of the effect of interlayer slip on the vibration characteristics of the frictional laminated beam.
- Application of the derivatives of eigen parameters method to identify interlayer slip damage of the laminated beam.

## V09 — Novel dynamic model for calculating the equivalent Young’s modulus and loss factor of layered beams

- **paper_id:** `2d30a68b71`
- **year:** 2020
- **doi:** 10.1016/j.jsv.2020.115634
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- inter-layer friction
- clamping force
- number of layers

### Modeling Methods

- Uniform elastic beam theory (Euler-Bernoulli bending formulation) (Page 4).
- Analytical strain difference formulation for layered beams (internal and external strain differences) (Pages 3-4).
- Non-linear spring-damper contact model for friction energy dissipation (Pages 4-5, 12).
- Linear regression modeling of strain difference ratio versus clamping force (Page 10).
- Parameter optimization and curve-fitting from experimental frequency response functions (Pages 7, 8, 10).
- Finite element method (FEM) dynamic simulation using equivalent material properties (Young's modulus and loss factor) (Pages 1, 6-12).

### Performance Metrics

- Relative error of the first four natural frequencies between FEM simulations and experimental measurements (%) (Pages 1, 8, 10-11, 13).
- Equivalent bending stiffness and equivalent Young's modulus (GPa) (Pages 4, 8, 10).
- Damping loss factor (eta) (Pages 1, 4-6, 8-11).
- Strain difference ratio (zeta) (Pages 4, 8, 10).
- Agreement of simulated and measured frequency response functions (FRFs) (Pages 8-12).

### Future Work

- Obtain the strain difference ratio and model parameters for a real transformer (Page 13).
- Simulate and compare frequency response functions directly on a real transformer core structure (Page 13).
- Understand and explain the mode-splitting phenomenon caused by coupling between the laminated beam and the lower clamping structure (Pages 10, 11).

## V10 — Analytical model for the bending of parallel wire cables considering interactions among wires

- **paper_id:** `ecdac26196`
- **year:** 2021
- **doi:** 10.1016/j.ijmecsci.2020.106192
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- interfacial slips and interactive forces among wires
- contact and friction effects between adjacent wire layers
- clench effect of the protective cable sheath providing initial slip rigidity (k0)
- Poisson-effect radial tightening under axial tensile stress increasing interfacial slip rigidity

### Modeling Methods

- Equivalent plane-stress laminated composite beam model
- State space method for multilayered composite beams
- Fourier series expansion of state variables
- Layer-by-layer transfer matrix method
- Linear slip rigidity modeling strategy (k = \lambda\bar{\sigma} + k0)
- Bilinear modeling strategy for stick-to-slip state transition based on critical curvature/deflection threshold

### Performance Metrics

- Fourier series truncation error (< 0.2% for 15 terms)
- Force-deflection curve agreement with experimental measurements
- Deflection magnification coefficient (DMC, \delta = f_slip / f_no-slip)
- Equivalent bending stiffness coefficient (EBSC, \gamma = 1/\delta)
- Critical curvature threshold (\kappa \approx 6 \times 10^-6 m^-1)
- Interfacial slip ratio (\Delta u_i / \Delta u_1)

### Future Work

- Extending the analytical laminated beam formulation to incorporate realistic nonlinear inter-wire interaction and slip behaviors once the exact nonlinear mechanisms among wires are experimentally clarified.
- Applying the proposed analytical model to more complex cable studies, including dynamic properties and fatigue life predictions.

## V11 — Equivalent dynamic model of multilayered structures with imperfect interfaces: Application to a sandwich structured plate with sliding interfaces

- **paper_id:** `0f1b512cee`
- **year:** 2022
- **doi:** 10.1016/j.jsv.2022.117052
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Modeling Methods

- Guyader-Marchetti Zig-Zag equivalent single layer (ESL) plate modeling framework
- Discontinuous interface kinematic formulation introducing displacement slip jumps
- Piecewise linear spring/compliance interface constitutive equations relating interface stresses and displacement jumps
- Reissner-Mindlin plate kinematic assumptions (bending, shearing, and membrane displacements)
- Lagrangian mechanics and Hamilton's principle of least action to derive equations of motion
- Woodcock parameter reformulation incorporating imperfection correction terms
- Harmonic wave propagation formulation solved for complex wavenumbers via an 8th-order polynomial determinant
- Love-Kirchhoff equivalent thin-plate formulation for frequency-dependent complex flexural rigidity
- Energy damping formulation corrected by group-to-phase velocity ratio
- Asymptotic flexural rigidity limit analysis at low and high frequencies
- Benchmarking against Shorter's Spectral Finite Element Method (SFEM) and Ross-Kerwin-Ungar (RKU) model

### Performance Metrics

- Bending, shear, and extensional wavenumbers as a function of frequency
- Frequency-dependent equivalent complex flexural rigidity
- Frequency-dependent energy damping ratio
- Frequency of maximum shearing / maximum damping
- Dynamic parameter frequency shift between perfect and imperfect interfaces
- Low-frequency and high-frequency asymptotic flexural rigidity limits

### Future Work

- Incorporating third-order vertical displacement fields to better describe transverse shear stress variations, particularly under severe debonding conditions.
- Incorporating dilatational motion to extend the model's validity to higher frequencies and capture breathing modes.
- Modeling interfacial openings to account for normal separation and out-of-plane defect modes.
- Implementing frequency-dependent and spatially varying interface parameters.
- Developing nonlinear interface constitutive relations, including piecewise linear models.
- Validating the modeling methodology experimentally on physical sandwich panels with physical bonding defects.
- Applying the equivalent dynamic framework to Structural Health Monitoring (SHM) for detecting adhesive defects and tracking structural aging.

## V12 — An analytic solution for bending of multilayered structures with interlayer-slip

- **paper_id:** `bd5af3e26d`
- **year:** 2024
- **doi:** 10.1016/j.ijmecsci.2024.109642
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- interlayer slip
- elastic shearing at interfaces
- interfacial stiffness

### Modeling Methods

- Euler-Bernoulli beam theory for slender multilayered beams (p. 2, 3)
- Kirchhoff-Love plate hypotheses for multilayered circular plates (p. 5, 6)
- Linear elastic constitutive shear-slip interface formulation (t = K*delta) (p. 2, 3, 6)
- Analytical differential equation formulation using average shear force and an analytical non-uniform distribution function f(n) (p. 3, 4, 6, 7)
- Analytical solution using hyperbolic functions (sinh, cosh) for beams and modified Bessel functions of the first and second kinds (I0, I1, K0, K1) for circular plates (p. 3, 4, 7, 9-11)
- Finite element analysis (FEA) in ABAQUS using 2D quadrilateral plane stress elements, axisymmetric stress elements (CAX4R), and cohesive elements (COH2D4 and COHAX4) (p. 3, 7)

### Performance Metrics

- Normalized effective bending stiffness Se/S0 (ratio of effective stiffness to perfectly bonded stiffness) (p. 1, 4, 5, 7, 8, 11)
- Normalized deflection w/w0 relative to full-interaction counterpart (p. 4, 7)
- Normalized total interface shear force (normalized by M/L^2, q, F/L, or F/R) (p. 4, 7)
- Interfacial shear force distribution ratio (t1 + tn-1)/(2*t_bar) captured by distribution function f(n) (p. 3, 4, 5)

### Future Work

- Exploring multilayered structures with non-uniform interfacial properties across layers (p. 8)
- Incorporating normal interface separation and out-of-plane detachment/delamination (p. 8)
- Integrating inelastic mechanisms such as interfacial plasticity or damage laws, potentially via numerical methods (p. 8)
- Applying the formulation to predict interlayer strength and deformation in multi-scale layered materials such as graphene composites (p. 8)

## V13 — Slip-mediated axisymmetric bending of multilayered structures with different interfaces: Analytical solutions and design guidelines

- **paper_id:** `bdeedc2731`
- **year:** 2025
- **doi:** 10.1016/j.euromechsol.2024.105488
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- interlayer slip
- interfacial slip
- interlayer shear
- Elastic Shear Stress (ESS)
- Critical Shear Flow (CSF)

### Actuation

- uniform pressure

### Modeling Methods

- Uniform Slip Model (USM) displacement field formulation extended to axisymmetric bending
- Principle of minimum potential energy (variational energy formulation)
- Bending strain energy decomposition into stretching gradient and identical bending terms
- Inhomogeneous modified Bessel differential equation formulation and solution for the ESS interface
- Piecewise domain variational formulation with moving sticking/slipping boundary r0 for the CSF interface
- Finite Element Method (FEM) simulation for model verification

### Performance Metrics

- Bending stiffness retention ratio / correction factor f(N, κ) = Deff / Dplane_bend
- Maximum interlayer slip displacement Δmax and its radial position
- Critical pressure thresholds for slip initiation (pa) and full slip (p0)
- Agreement between analytical solutions and FEM simulation curves across parameter ranges
- Accuracy of extracted interlayer shear modulus G under different loading configurations

### Future Work

- Applying the analytical models and design guidelines to experimental characterization and parametric design of functionally integrated composite laminated structures.
- Tailoring interfacial properties to engineer integrated multifunctional capabilities across mechanical, thermal, electrical, and optical domains in microelectronics, bio-mimetic skins, and wearable/implantable devices.

## V14 — Thickness Gradient Design Enhances Bending Performance of Multilayer Beams through Slip Homogenization

- **paper_id:** `7f93ab3253`
- **year:** 2026
- **doi:** 10.1016/j.apm.2026.117249
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Stiffness Mechanism

- interlayer slip
- interfacial shear stiffness
- layer thickness gradient

### Modeling Methods

- Euler-Bernoulli beam theory for slender multilayer beams (p. 3).
- Principle of minimum total potential energy formulation incorporating layer axial, bending, and interlayer shear slip energies (p. 3).
- Linear elastic shear constitutive relation at interfaces (Si = Ki * si) (p. 3).
- Coupled system of second-order ordinary differential equations formulated in terms of interlayer slip variables (p. 4-5).
- Modal decoupling using eigenvalue decomposition of the interaction coefficient matrix G (p. 5).
- Two-dimensional plane stress finite element validation using 4-node bilinear plane stress elements (CPS4R) for solid layers and 4-node cohesive elements (COH2D4) for interfaces (p. 6).
- Least-squares regression fitting to establish power-law scaling relations for optimal gradient design (p. 14).

### Performance Metrics

- Relative error between theoretical analytical predictions and finite element / literature benchmark values (%) (p. 6, 7, 8).
- Interlayer slip magnitude and maximum slip s0 and sopt (mm or m) (p. 6, 7, 8, 15, 16, 17).
- Transverse beam deflection and maximum deflection wmax (mm or m) (p. 6, 7, 8, 10, 11, 12).
- Normalized structural strength / allowable external load capacity Qopt and Q0 (p. 15, 16, 17).
- Coefficient of determination R^2 for power-law scaling curve fits (p. 14).

### Future Work

- Quantitative performance comparison between the proposed thickness-graded design and conventional functionally graded materials (p. 18).
- Development of hybrid geometric-material grading strategies to achieve tighter slip consistency (p. 18).
- Physical experimental validation of thickness-gradient multilayer structures (p. 18).
- Extension of the analytical framework to dynamic loading and progressive failure analysis (p. 18).
- Optimization tailored for heterogeneous composite laminates (p. 18).
- Incorporation of time-dependent viscoelastic behavior in polymeric interlayers (p. 18).

## V15 — Influence of boundary conditions on the response of multilayered plates with cohesive interfaces and delaminations using a homogenized approach

- **paper_id:** `4994f7ed3f`
- **year:** 2014
- **doi:** 10.3221/IGF-ESIS.29.20
- **source_type:** verification
- **verification_id:** D1-V004
- **screening_status:** included
- **screening_reason:** Included for D1-V004 Track C adjacent-mechanics falsification audit.

### Robot / Structure Type


### Modeling Methods

- Homogenized first-order zigzag plate theory using a two-length-scales displacement field combining global first-order shear deformation kinematics, layerwise zigzag functions, and interface displacement jumps (pages 3-5).
- Affine (piecewise linear) interfacial traction laws relating interfacial shear stresses to sliding displacement jumps (pages 3-4).
- Principle of Virtual Works formulated with the inclusion of interface traction strain energy to derive weak-form equilibrium equations and boundary conditions (pages 5-6).
- Generalized transverse shear force formulation modifying the classical bending moment-shear force equilibrium relation (pages 6, 8).
- A posteriori determination of transverse shear and transverse normal stresses via local 2D equilibrium equations using bending stresses (pages 7-9).
- Application of a shear correction factor (K2) to account for thickness-wise transverse shear deformation (page 7).
- Analytical evaluation of energy release rates and stress intensity factors based on gross crack-tip stress resultants and couples (pages 9-10).

### Performance Metrics

- Accuracy of predicted displacement and stress fields compared to exact 2D elasticity solutions and discrete-layer model predictions (pages 2, 8-9).
- Equilibrium consistency of the generalized transverse shear force Q_2^g with the external equilibrant force F across the plate span (pages 2, 8).
- Size of the localized boundary zone near clamped supports and delamination crack tips where localized inaccuracies occur (pages 8-10).
- Accuracy of energy release rate and stress intensity factor predictions at delamination crack tips (pages 9-10).

### Future Work

- Derivation and implementation of a problem-dependent shear correction factor (K2) that depends on interfacial properties to improve transverse shear deformation and boundary region predictions (pages 2, 7, 10).
- Application of the generalized formulation accounting for interfacial opening (Mode I / mixed-mode) to cohesive delamination problems under general mixed-mode loading conditions (page 2).
- Extension and utilization of the homogenized plate formulation for broader fracture mechanics problem solving in multilayered structures (pages 2, 10).
