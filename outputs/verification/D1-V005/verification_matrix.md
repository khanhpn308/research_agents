# Verification Matrix

**Verification ID:** D1-V005
**Paper count:** 16
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — THE DEPENDENCE OF SHEAR LAG ON PARTIAL INTERACTION IN COMPOSITE BEAMS

- **paper_id:** `8a6d33e527`
- **year:** 1974
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- flexible shear connectors

### Modeling Methods

- Linear elastic plate bending theory using the biharmonic equation for deflexion
- Airy stress function formulation using the biharmonic equation for in-plane slab stresses
- Fourier series representations for applied loading, plate deflexion, and stress functions
- Interface slip compatibility condition relating interface slip gradient to differential strain and connector stiffness
- Boundary value problem solution using trigonometric orthogonality and the segmentation method (5x5 or 7x7) for truncated infinite linear systems
- Transformed section theory for equivalent composite section properties

### Performance Metrics

- Deflexion factor (gamma_w)
- Effective width factor based on deflexion (beta_w)
- Effective width factor based on longitudinal stress distribution (beta)
- Stress ratio of transformed section theory to exact analytical stress (sigma_tr/sigma_sb)
- Interface slip normalized as a fraction of maximum central deflexion
- Reduction of steel bottom flange stress

## V02 — The Deformation of Composite Beams with Discrete Flexible Connection

- **paper_id:** `99721ae369`
- **year:** 1990
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- discrete flexible connection
- shear connectors
- through-deck welded studs
- partial interaction

### Modeling Methods

- Folded plate method extended to model discrete non-linear connection with free-slip interfaces and iterative stud reactions.
- Plastic section analysis for ultimate flexural capacity.
- Engineers' bending theory with modular ratio approach (assuming zero slip).
- Empirical linear interaction modification based on degree of interaction (Johnson).
- Closed-form second-order differential equations assuming continuous linear elastic connection (Newmark et al.; Johnson).
- Finite difference formulation for partial interaction (Roberts).
- Finite element analysis with discrete connector elements (Jefferson; Al-Hayderi).

### Performance Metrics

- Central vertical beam deflection (mm).
- Interfacial slip along the beam span and end slip (mm).
- Secant stiffness at working load as a percentage of theoretical fully composite stiffness (%).
- Total load capacity (kN) and distributed load capacity (kN/m²).
- Degree of interaction (N/Nf).
- Connector secant modulus (kN/mm²).

### Future Work

- Investigating the mechanisms causing higher connector stiffness in beams relative to push-off tests.
- Examining the influence of cross-beam hogging action in the concrete slab over the steel beam.
- Conducting push-off tests with larger slab portions and six connectors instead of four.
- Testing full-scale composite beams under negative (hogging) moment conditions over the beam.
- Assessing the feasibility of reducing the standard code minimum interaction threshold below 50%.

## V03 — A Rational Model for the Degree of Interaction in Composite Beams with Flexible Shear Connectors

- **paper_id:** `a28d4f1668`
- **year:** 1998
- **doi:** 10.1080/08905459808945426
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- flexible shear connectors
- mechanical shear connectors

### Modeling Methods

- Mixed elastic-plastic beam analysis (elastic steel and concrete elements with perfectly plastic shear connectors)
- Rigid plastic cross-sectional equilibrium analysis
- Closed-form differential and integral formulations for curvature, slip strain, and interfacial slip
- Non-dimensional parametric formulation for neutral axis separation and degrees of interaction/shear connection

### Performance Metrics

- Maximum longitudinal slip at the supports (s_max)
- Maximum slip strain ((ds/dx)_max) and midspan slip strain ((ds/dx)_mid)
- Maximum curvature (phi_max) and its location along the beam span (x_m)
- Neutral axis separation at midspan (h_na,mid / h_cs)
- Degree of interaction (phi) and degree of shear connection (eta, eta_fi)

### Future Work

- Application of the research as part of an ongoing project on the upgrade and repair of reinforced concrete beams using externally bonded steel plates.
- Using the derived interaction-connection relationships to estimate neutral axis separation and evaluate whether rigid plastic strength is reduced in structural design.

## V04 — Steel and concrete composite beams with flexible shear connection: ‘‘exact’’ analytical expression of the stiffness matrix and applications

- **paper_id:** `d0699583ac`
- **year:** 2002
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- flexible shear connection

### Modeling Methods

- Newmark's differential equation for composite beams with linear elastic shear connection
- Principle of Virtual Work applied to compute flexibility coefficients of simply supported composite beams
- Direct matrix inversion of the flexibility matrix to obtain displacement-based stiffness matrix terms
- Compatibility equations for equivalent fixed-end nodal force vectors under distributed loads and shrinkage
- Viscous algebraic formulations (effective modulus method and mean stress method / age-adjusted effective modulus method) for concrete creep and shrinkage

### Performance Metrics

- Internal support reaction force (X)
- Deflection ratio relative to full interaction (f / ffull)
- Bending moment redistribution ratio (delta = Mred / Mel and delta / dfull)
- Concrete slab normal stress at the central support

## V05 — Time analysis of composite beams with partial interaction using available modelling techniques: A comparative study

- **paper_id:** `a577a30ffd`
- **year:** 2006
- **doi:** 10.1016/j.jcsr.2005.11.024
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Modeling Methods

- Exact analytical model / Closed-form solutions (CFS)
- Direct stiffness method (DSM)
- Finite element method with 8 degrees of freedom (FEM 8 dof)
- Finite element method with 10 degrees of freedom (FEM 10 dof)
- Finite difference method (FDM)
- Age-adjusted effective modulus method (AEMM) for concrete creep modeling
- Newmark's kinematic model for partial interaction with interlayer slip
- Weak and strong variational formulations of the governing differential equations

### Performance Metrics

- Percentage relative error evaluated against the exact analytical benchmark solution (with an acceptable error threshold defined as 2%).
- Minimum number of elements (FEM) or grid points (FDM) required to achieve a relative error below 2%.
- Presence and magnitude of unphysical inter-element nodal discontinuities (jumps) in stress resultants and curvature.

### Future Work

- Investigating non-uniform spatial discretizations (such as mesh refinement near support regions for the finite difference method) to improve computational efficiency.
- Applying the comparative findings to the modeling and design of multi-span continuous composite beam structures.

## V06 — Analytical Solution of Two-Layer Beam Taking into account Interlayer Slip and Shear Deformation

- **paper_id:** `f5bba53ef2`
- **year:** 2007
- **doi:** 10.1061/ASCE0733-94452007133:6886
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Modeling Methods

- Linear elastic Timoshenko beam theory incorporating transverse shear deformation in each layer via Reissner's one-dimensional beam kinematics.
- Formulation of a system of 21 differential and algebraic governing equations combining kinematics, section equilibrium, constitutive equations, and interface constraints.
- Derivation of a coupled system of two higher-order linear ordinary differential equations with constant coefficients for interlayer slip and normal contact traction.
- Exact analytical solution of the differential equation system obtained using symbolic computation in Mathematica.
- Global tangent stiffness matrix formulation to resolve boundary displacements, rotations, and end forces.

### Performance Metrics

- Ratio of Timoshenko vertical deflection to Euler-Bernoulli vertical deflection (wT / wB).
- Deflection ratios relative to rigidly connected composite beams (wB / wB*, wT / wT*, wT / wB*).
- Comparison ratios with Eurocode 5 empirical predictions (EC5 / wB, EC5 / wT).
- Ratios of Timoshenko to Euler-Bernoulli static and kinematic quantities (wT/wB, Delta_T/Delta_B, phi_aT/phi_aB, phi_bT/phi_bB, epsilon_aT/epsilon_aB, epsilon_bT/epsilon_bB, NaT/NaB, kappa_aT/kappa_aB, pnT/pnB).
- Ratio of tangential to normal contact tractions (pt / pn).
- Longitudinal normal stress (sigma_xx) and tangential shear stress (sigma_xz) profiles across beam depth.

## V07 — Exact static analysis of partially composite beams and beam-columns

- **paper_id:** `eeb0863c0d`
- **year:** 2007
- **doi:** 10.1016/j.ijmecsci.2006.07.005
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- interlayer slip
- flexible shear connection
- shear connectors with slip modulus K
- partial composite action

### Modeling Methods

- Euler-Bernoulli beam kinematics applied to individual sub-elements (neglecting shear deformation)
- Variational energy minimization (principle of minimum potential energy) using Lagrange multipliers to incorporate the strain-deflection constraint
- Sixth-order governing ordinary differential equations for transverse deflection w(x) and internal actions under first- and second-order static loading
- Continuous linear elastic interface modeling characterized by a constant slip modulus K [N/m^2]
- Characteristic equation derivation, Gaussian elimination, and determinant analysis of 6x6 boundary matrices for eigenvalue and buckling length coefficient evaluation
- Effective bending stiffness (EI_eff) formulation for simplified first-order and buckling approximations

### Performance Metrics

- Buckling length coefficient (mu)
- Critical buckling load (P_cr)
- Maximum transverse deflection (w_max)
- Magnification factor (exact second-order / first-order ratio vs approximate 1 / (1 - P/P_cr))
- Percentage error / deviation of approximate methods (solid-column coefficients or EI_eff) relative to exact solutions

### Future Work

- Dynamic analysis of composite beams and beam-columns with partial interaction (noted as addressed in a companion paper).
- Extending the formulation to handle discontinuities in flexural stiffness and slope by superimposing Macauley's singularity functions onto the one-dimensional field.

## V08 — Composite beam–columns with interlayer slip—Approximate analysis

- **paper_id:** `d87b4ad44d`
- **year:** 2008
- **doi:** 10.1016/j.ijmecsci.2008.09.003
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- interlayer slip
- shear connectors
- partial composite action

### Modeling Methods

- First-order and second-order governing differential equations derived from Euler-Bernoulli beam theory for partial composite members with interlayer slip.
- Magnification factor approach derived from initial deflected shapes and fundamental buckling loads (eigenvalues).
- Effective bending stiffness formulation incorporating buckling length coefficients across Euler cases.
- Decomposition of fixed-fixed (Euler case 4) and propped cantilever (Euler case 3) beam-columns at inflection (zero-moment) points into equivalent cantilever and hinged segments.

### Performance Metrics

- Percentage error of approximate second-order deflections and internal actions relative to exact second-order analytical solutions.
- Critical buckling load (P_cr) and effective bending stiffness (EI_eff).

### Future Work

- Detailed evaluation and validation of exact and approximate convenience factors for beam-columns under other Euler boundary conditions and varied transverse loading configurations.
- General application and validation of the approximate analysis method for design practice across practical ranges of geometric and elastic parameters.

## V09 — Locking problems in the partial interaction analysis of multi-layered composite beams

- **paper_id:** `2ad029e62c`
- **year:** 2008
- **doi:** 10.1016/j.engstruct.2008.04.006
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Modeling Methods

- Principle of virtual work to derive the weak form of the multi-layered partial shear interaction problem.
- Integration by parts to derive the strong form governing differential equations and static/kinematic boundary conditions.
- Euler-Bernoulli beam theory for kinematic modeling of individual layers.
- Continuous linear-elastic interface slip model relating shear flow to longitudinal slip discontinuity.
- Displacement-based finite element formulation: (2n + 4)dof element (cubic deflection, linear axial displacement) and (3n + 4)dof element (cubic deflection, parabolic axial displacement with an internal node).
- Specific three-layered beam finite element models: 10dof and 13dof elements.

### Performance Metrics

- Accuracy of calculated vertical deflection, interface slip, axial forces, and bending moments relative to a refined 50-element benchmark solution.
- Resistance to curvature locking under high interface shear connection stiffness (gamma_j*L = 50).
- Convergence and numerical robustness under coarse mesh discretisation (4 elements).

## V10 — A simplified analysis method for composite beams with interlayer slip

- **paper_id:** `aa091ea74d`
- **year:** 2009
- **doi:** 10.1016/j.ijmecsci.2009.05.003
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- partial composite action
- interlayer slip
- flexible shear connection with mechanical connectors (studs, screws, and nails)

### Modeling Methods

- Approximate static analysis replacing fully composite bending stiffness with effective composite bending stiffness in standard beam formulas.
- Determination of effective beam length using the fundamental buckling length coefficient (mu) from the corresponding column buckling problem.
- Exact static formulation based on the governing differential equations of partial composite action (Stüssi-Granholm-Newmark-Pleshkov model) for two-layer beams.
- Closed-form analytical equations for deflections, normal stresses, shear stresses, and interlayer slip forces.
- Navier's and Jouravski's stress formulations adapted for composite sections with partial interaction.

### Performance Metrics

- Percentage error between approximate (effective) predictions and exact analytical solutions for deflections, normal stresses, shear stresses, and interlayer slip forces.
- Normalized maximum deflection ratio (w_max / w_infty,max).
- Normalized maximum normal stress ratio (sigma_2,max / sigma_2,infty,max).
- Normalized maximum shear stress ratio (tau_2,max / tau_2,infty,max).
- Normalized maximum interlayer slip force ratio (Vs,max / Vs,infty,max).

### Future Work

- Extending the simplified analysis and design procedure to multi-layered composite beams, especially three-layered members.
- Extending the method to multiple stringer or joist systems with decking or sheathing.
- Incorporating gaps in the decking or sheathing into the analysis.
- Developing correction factors specifically for calculating interlayer shear forces.
- Conducting sensitivity analyses across a broader range of practical cases prior to code implementation.

## V11 — Analytical and numerical analysis of multilayered beams with interlayer slip

- **paper_id:** `14958e37b2`
- **year:** 2010
- **doi:** 10.1016/j.engstruct.2010.02.015
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- deformable connections allowing relative horizontal slip between layers (partial interaction)

### Modeling Methods

- Euler-Bernoulli beam theory with partial interaction
- Timoshenko beam theory with partial interaction and shear correction factors
- Interlayer slip-based analytical formulation (system of second-order differential equations in slip variables)
- Eigenvalue decoupling method for differential equations of statically determinate beams
- Zero-thickness interface finite elements based on Goodman-Taylor-Brekke element kinematics
- Interface Linear Cubic (ILC) finite element formulation
- Interface Quadratic Cubic (IQC) finite element formulation
- Interface Timoshenko Quadratic (ITQ) finite element formulation

### Performance Metrics

- Numerical accuracy of interlayer slips and maximum transverse displacements relative to closed-form analytical solutions
- Finite element convergence rate across mesh refinements (4, 8, 20 elements per interface)
- Curvature and slip distribution fidelity under high connection stiffness (evaluation of slip/curvature locking)

## V12 — Analysis of Composite Beams with Incomplete Interaction I. Theoretical study of bending stiffness of two-layered composite beams

- **paper_id:** `f8e8c7b1a4`
- **year:** 2013
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- shear connector

### Modeling Methods

- Newmark's theoretical method (continuous differential equation solution for incomplete interaction)
- Improved Kamiya rigorous numerical method (recurrence difference equations solved from mid-span to support with explicit boundary conditions)
- Improved Kamiya approximation method (non-iterative slip-profile ratio approximation using deflection angle formulas)
- Superposition principle (decomposing total deflection and slope into non-composite and axial relaxation components)
- Virtual work method (calculating deflection components from discrete shear connector forces)

### Performance Metrics

- Ratio of approximate to rigorous end-span interlayer slip (S1,AP / S1,RG)
- Ratio of approximate to rigorous mid-span axial force (F_mu,AP / F_mu,RG)
- Ratio of mid-span deflection component due to axial force relative to rigorous method (delta_Fmu,AP / delta_Fmu,RG and delta_Fmu,NM / delta_Fmu,RG)
- Percentage error of total mid-span deflection ((delta_mu - delta_mu,RG) / delta_mu,RG)

### Future Work

- Derivation of non-linear approximate solution methods
- Application to three-layered beams widely used in practice, such as I-beams and box beams
- Development of solution methods for conditions where external forces or shear connector arrangements are asymmetrical along the span

## V13 — Exact finite elements for multilayered composite beam-columns with partial interaction

- **paper_id:** `c9bf5cb21f`
- **year:** 2013
- **doi:** 10.1016/j.compstruc.2013.04.008
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Modeling Methods

- System of second-order ordinary differential equations formulated in terms of interlayer slip variables.
- Eigenvalue decomposition for decoupling the governing system of differential equations.
- Euler-Bernoulli (shear-rigid) beam kinematics.
- Timoshenko (shear-flexible) beam kinematics.
- Flexibility-based exact finite element formulation using a statically determinate coordinate system.
- Direct stiffness method via inversion of the flexibility matrix and static-kinematic transformation matrices.
- Displacement-based finite elements (linear, quadratic, and cubic field interpolations) for comparative benchmark analyses.

### Performance Metrics

- End slip magnitudes (s_i in mm).
- Midpoint and maximum transverse displacements (v_max in mm or m).
- Intermediate support bending moments (M_max in kNm).
- Convergence rate with respect to mesh refinement.
- Absence of slip locking, curvature locking, and shear locking under high connection stiffnesses.

## V14 — Derivation of the exact stiffness matrix of shear-deformable multi-layered beam element in partial interaction

- **paper_id:** `bdf95f0602`
- **year:** 2016
- **doi:** 10.1016/j.finel.2015.12.004
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Stiffness Mechanism

- shear connection
- interlayer slip

### Modeling Methods

- Timoshenko kinematic beam theory applied to individual layers with independent cross-section rotations and shear strains.
- Continuous linear shear connection modeling between interface shear flow and interlayer slip.
- Equilibrium formulation of differential multi-layer beam elements yielding coupled second-order ordinary differential equations.
- Eigenvalue decomposition / diagonalization of system matrix A to uncouple the differential equations for interlayer slips and shear deformations.
- Closed-form analytical integration of uncoupled differential equations under linear shear force distributions.
- Direct stiffness method to construct the (4n+6) x (4n+6) exact element stiffness matrix and equivalent nodal force vector.
- Displacement-based finite element implementation.

### Performance Metrics

- Mid-span and maximum deflection ratios between shear-deformable (Timoshenko) and shear-rigid (Bernoulli) models.
- Interlayer slip ratios (Timoshenko to Bernoulli) at beam ends.
- Cross-section rotation ratios (Timoshenko to Bernoulli) at beam ends.
- Maximum bending moment Mmax (kN*m).
- Interlayer slip magnitudes g1, g2, g3 (mm).
- Computational processing time (seconds) versus element count.

## V15 — Flexible N-layer composite beam/column elements with interlayer partial interaction imperfection–A novel approach to structural stability and dynamic analyses

- **paper_id:** `8a4d5de33a`
- **year:** 2025
- **doi:** 10.1016/j.compstruct.2025.119219
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Modeling Methods

- Extended Hamilton's variational energy principle for deriving governing differential equations and boundary conditions.
- Euler-Bernoulli partial-composite (EBPC) beam-column model.
- Timoshenko/Engesser partial-composite (TEPC) shear-deformable beam-column model.
- Linear shear spring-like slip model correlating interlayer shear force to relative displacement.
- Separation of variables for harmonic vibration modal analysis.
- Reduction of coupled governing differential equations to second-order difference equations solved analytically using hyperbolic functions.
- Effective buckling length and effective eigenmode length formulations for handling various boundary conditions.
- Derivation of explicit dimensionless conversion coefficients (Euler-to-partial-composite and Euler-to-Timoshenko/Engesser).

### Performance Metrics

- Critical buckling load (P).
- Natural frequencies / angular frequencies of vibration (Hz or rad/s).
- Percentage difference / discrepancy (% Diff) relative to experimental data, 3-D FEA, GEM/FEM benchmarks, and exact nonlinear characteristic roots.
- Buckling conversion factors (eta_pc-0, eta_pc-infinity, psi_T-E).
- Vibration frequency conversion factors (kappa_pc-0, kappa_pc-infinity, zeta_T-E).

### Future Work

- The authors did not include an explicit future work section or specific future work statements in the text.

## V16 — Laminated Partially-Composite Plate Theory (LPCPT)—An extension of the classical laminated plate theory for flexible n-layer plates with partial interlayer interaction

- **paper_id:** `71c8d5e2c7`
- **year:** 2026
- **doi:** 10.1016/j.compstruct.2025.119951
- **source_type:** verification
- **verification_id:** D1-V005
- **screening_status:** included
- **screening_reason:** Included for D1-V005 C02 partial/incomplete-interaction adversarial audit.

### Robot / Structure Type


### Modeling Methods

- Laminated Partial-Composite Plate Theory (LPCPT) based on Kirchhoff-Love kinematics per layer.
- Extended Hamilton's variational energy principle for governing equations and extended boundary conditions.
- Shear spring interface model relating transverse shear stress to tangential slip discontinuities.
- Navier-type double Fourier series combined with truncated polynomial displacement fields.
- Coupled difference equation analytical scheme using hyperbolic functions (cosh, sinh) for arbitrary layer numbers.
- Direct algebraic characteristic determinant method for non-identical multilayer plates.
- 3-D Finite Element Analysis (FEA) in Abaqus/CAE using continuum solid shell elements (CSS8) for plates and solid brick elements (C3D8R) for adhesive layers.

### Performance Metrics

- Dimensionless critical buckling load parameter (Ncr = Ncr * a^2 / D_infinity or Ncr * b^2 / (pi^2 * D)).
- Dimensionless natural frequency parameter (omega_bar = omega * a^2 * sqrt(rho_ell * hTot / D_infinity)).
- Percentage discrepancy relative to 3-D elasticity theory and classical plate theory (CPT).
- Buckling and vibration mode sequences and mode shifting indicators.

### Future Work

- Extending LPCPT to incorporate shear-deformable kinematic models (from Mindlin-Reissner to higher-order shear deformation theories) for internal transverse shear deformation within individual layers.
- Developing laminated partial-composite shell theories based on diverse kinematic models.
- Applying LPCPT formulations to other material classes, such as functionally graded materials (FGMs).
- Extending analytical and numerical solutions to different boundary conditions, general loading scenarios, and wider static and dynamic problems.
