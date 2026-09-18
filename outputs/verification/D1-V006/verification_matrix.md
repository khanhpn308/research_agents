# Verification Matrix

**Verification ID:** D1-V006
**Paper count:** 16
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — The existence of a critical length scale in regularised friction

- **paper_id:** `7c3aac183e`
- **year:** 2014
- **doi:** 10.1016/j.jmps.2013.10.007
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- Finite-element method (FEM) with two-dimensional regular quadrilateral elements and linear interpolation (four integration points)
- Explicit Newmark-beta time integration scheme with lumped mass matrix
- Simplified Prakash-Clifton dynamic friction regularisation law
- Laplace-transform-based steady-state frequency response / spectral analysis

### Performance Metrics

- Mesh convergence criteria (relative error over total propagation distance below 0.5% and arrival time error below 0.1%)
- Slip velocity amplitude and temporal profile
- Rupture front velocity Vr
- Critical characteristic length scale Lc
- Output-to-input amplitude attenuation ratio A/A0

### Future Work

- Investigating the existence and behavior of critical length scales for slip events propagating along more general deformable-deformable (bimaterial) interfaces.
- Applying the proposed verification procedure to experimentally monitor slip pulses with rich high-frequency content to measure physical characteristic interface length scales.

## V02 — Transition from stick to slip in Hertzian contact with “Griffith” friction: The Cattaneo–Mindlin problem revisited

- **paper_id:** `ac9973e89e`
- **year:** 2015
- **doi:** 10.1016/j.jmps.2015.08.002
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- Superposition method extending the Cattaneo-Mindlin tangential contact formulation.
- Classical Hertzian contact pressure theory for spherical normal contact.
- Mode II fracture mechanics formulation using the JKR adhesive contact solution for the corrective shear traction distribution in the stick zone.
- Amontons-Coulomb friction law applied within the slip annulus.
- Linearly pressure-dependent fracture toughness model accounting for real contact area variations.
- Bounded asymptotic stress intensity factor analysis at the stick-slip boundary.

### Performance Metrics

- Stick zone radius ratio (c / a)
- Normalized tangential load ratio (Q / (f * P))
- Normalized shear traction distribution (q_x / (f * p_0))
- Critical stick zone radius ratio (c_c / a and c_c' / a)
- Tangential load enhancement factor before global sliding (Q_max / (f * P))
- Mode II stress intensity factor (K_II)

### Future Work

- Developing criteria to reliably select appropriate physical constants for cohesive/fracture models of friction from experimental data.
- Extending the singular adhesive contact framework to more general non-axisymmetric contact geometries.
- Further investigating whether interfacial roughness effects or fracture mechanics models better explain observed deviations in frictional energy dissipation under oscillating loads.

## V03 — Friction Characteristics of CFRP Plates in Contact with Copper Plates under High Contact Pressure

- **paper_id:** `79d1adc34c`
- **year:** 2016
- **doi:** 10.1061/(ASCE)CC.1943-5614.0000673
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- Empirical linear contact friction modeling using Amonton's law (tau = 0.31 * sigma) for as-received copper plates
- Empirical power-law contact friction modeling based on Howell's formulation for viscoelastic materials (tau = 1.02 * sigma^0.76) for annealed copper plates
- Double-interface friction formulation relating total horizontal pullout force, normal force, shear stress, and contact stress (mu = Tmax / (2 * N) = tau / sigma)

### Performance Metrics

- Static coefficient of friction (mu)
- Interfacial shear stress (MPa)
- Maximum sliding distance before failure (mm)
- Horizontal breaking force / tensile rupture load (kN)

### Future Work

- Utilization of CFRP-copper friction parameters for the design and development of novel friction-based wedge anchors for composite plates in structural rehabilitation and retrofitting
- Application of friction data to the design of lightweight composite components in automotive, aviation, space, and shipbuilding industries
- Development of innovative composite materials combining carbon fibers, resin matrix, and copper
- Use of the experimental data as a benchmark for other composite-to-metal contact configurations of similar geometry

## V04 — A full layered numerical model for predicting hysteretic behavior of unbonded flexible pipes considering initial contact pressure

- **paper_id:** `afe2a3a310`
- **year:** 2021
- **doi:** 10.1016/j.apor.2021.102626
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Stiffness Mechanism

- interlayer friction
- internal slip mechanism

### Modeling Methods

- Full-layered 3D finite element modeling using the implicit solver of Abaqus/Standard under quasi-static conditions.
- Equivalent orthotropic shell modeling (S4R elements) for the interlocked carcass and pressure zeta armor layers with tuned directional stiffnesses.
- Incompatible mode 8-node hexahedral solid elements (C3D8I) for tensile armor tendons to eliminate shear locking and hourglassing.
- Surface-to-surface (S2S) penalty contact formulation with Coulomb friction and hard normal contact.
- Predefined stress fields method applied as initial hoop stress in the outer sheath to model manufacturing-induced contact pressure.
- Filling surface layers (SFM3D4 elements) with negligible stiffness to close gaps between equivalent shell layers and adjacent polymeric sheaths.
- Rigid body end fittings (R3D4 elements) coupled to reference points to accurately capture internal pressure endcap effects.
- Centrally located dummy beam element (B31) with negligible stiffness to extract curvature distribution along the pipe length.

### Performance Metrics

- Stick bending stiffness (slope of linear elastic stick zone)
- Slip bending stiffness (slope of full slip zone)
- Friction moment / hysteretic loop width
- Maximum bending moment at prescribed curvature
- Cross-sectional curvature at the gauge location and curvature distribution along pipe length
- Local axial stress (sigma_xx-ax), transverse bending stress (sigma_xx-my), and normal bending stress (sigma_xx-mz) in tendons
- CPU simulation runtime and computational resource utilization

### Future Work

- Investigate the applicability and transferability of the 2 MPa predefined stress value to other unbonded flexible pipe configurations and dimensions.
- Incorporate additional sources of initial contact pressure, such as residual stresses generated during the manufacturing and forming of tensile armor tendons.

## V05 — Experimental validation of the applicability of effective spring boundary conditions for modelling damaged interfaces in laminate structures

- **paper_id:** `444793969c`
- **year:** 2021
- **doi:** 10.1016/j.compstruct.2021.114141
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Actuation

- Piezoelectric actuation using thin circular PZT transducers (PZT PIC 151, 10 mm diameter, 0.5 mm thickness) to excite guided waves

### Modeling Methods

- Lamé elastodynamic differential formulation for in-plane wave propagation in multi-layered isotropic waveguides
- Effective spring boundary conditions (ESBC) specifying stress traction continuity and displacement jump proportional to interfacial spring stiffness (tau = kappa * [u])
- Spatial Fourier transform with respect to coordinate x1 to convert the governing partial differential equations into ordinary differential equations and establish linear dispersion algebraic systems
- Quasi-static micromechanical modeling (Baik-Thompson and Lekesiz-Katsube-Rokhlin-Seghi models) relating spring stiffness to crack density, average defect width, and elastic constants
- Two-dimensional Fourier transform frequency-wavenumber analysis (FWA) of measured surface velocity profiles to extract experimental dispersion curves

### Performance Metrics

- Guided wave slowness s (us/m) as a function of frequency f (MHz)
- Interfacial spring stiffness kappa (GPa/mm)
- Damage parameter product Cl (crack density C multiplied by average defect width l, mm)
- Agreement/discrepancy between theoretical and experimental dispersion curves

### Future Work

- Extending the ESBC methodology to account for other micro-defect geometries such as circular, elliptical, or rectangular cracks using alternative stiffness relations
- Applying the modeling framework to more complex composite materials and anisotropic media

## V06 — A barrier method for frictional contact on embedded interfaces

- **paper_id:** `202fd05d8f`
- **year:** 2022
- **doi:** 10.1016/j.cma.2022.114820
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- Extended Finite Element Method (XFEM) with Heaviside jump enrichment for embedded discontinuities
- Smooth barrier energy density function for contact constraint enforcement
- C1-continuous smoothed Coulomb friction law with microslip formulation
- Averaged surface integration scheme (weak penalty projection) for traction stabilization
- Newton-Raphson iteration with direct linear solvers for discrete nonlinear variational systems

### Performance Metrics

- Non-penetration constraint satisfaction (absence of over-closure / inter-penetration)
- Accuracy and error norms of normal contact pressure and shear traction compared to analytical and reference solutions
- Asymptotic convergence rate of Newton iterations (quadratic convergence behavior)
- Mesh refinement convergence of normal and slip displacement jumps and interface tractions
- Presence or suppression of spurious oscillations in interface traction fields
- Conditioning of the Jacobian system matrix

### Future Work

- Extending the barrier formulation to three-dimensional embedded interface geometries.
- Incorporating evolving or propagating interfaces and crack growth.
- Adapting the framework to handle more sophisticated friction laws beyond standard Coulomb friction.
- Extending the barrier method to other enriched or embedded numerical frameworks such as the extended material point method (XMPM).

## V07 — A novel helix contact model for predicting hysteretic behavior of unbonded flexible pipes

- **paper_id:** `a300a3b714`
- **year:** 2022
- **doi:** 10.1016/j.oceaneng.2022.112407
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Stiffness Mechanism

- stick-slip friction mechanism between tensile armor tendons and supporting layers (friction-induced hysteretic bending stiffness)
- shear interaction / shear deformation of supporting plastic layers
- structural stiffness of concentric helical and cylindrical metallic and polymeric layers

### Modeling Methods

- Equivalent layered finite element modeling in Abaqus/Standard using an implicit solver
- Double helix contact beam model (SHCONT2B) using B31 beam elements with node-to-surface contact discretization and hard normal penalty formulation
- Equivalent stiffness core layer formulation (orthotropic shell for inner core, isotropic shell for outer core)
- Closed-form thick-walled cylindrical shell theory (isotropic and orthotropic) for axisymmetric interlayer contact pressure calculation
- Helical layer mechanical equilibrium and geometric compatibility formulations accounting for fill factors, residual strain, local bending, and torsion
- Bending analytical models based on plane surfaces remain plane assumption and shear interaction assumption with return-mapping stick-slip formulations
- Hertz contact theory for determining contact half-width and contact angles for helix contact beams

### Performance Metrics

- Bending stick stiffness (slope in stick zone) and slip bending stiffness
- Bending friction moment and hysteretic dissipated energy (hysteresis loop area)
- Tensile armor tendon stress components: axial friction stress, normal bending stress, transverse bending stress, and maximum total axial stress
- Tangential and transverse relative slip displacements
- Cross-section ovality ratio e = (D_max - D_min) / (D_max + D_min)
- Total element count, node count, and total variables (degrees of freedom)
- Computational simulation runtime (hours) for internal pressure and bending cycles, and memory consumption (GB)

### Future Work

- Extension of the efficient cross-section contact modeling strategy to global dynamic analysis of flexible risers
- Application of the predicted maximum total axial stress distributions to fatigue damage evaluation of tensile armor tendons

## V08 — A Single-Variable Zigzag Approach to Model Imperfect Interfaces in Layered Beams

- **paper_id:** `a9cd14eca9`
- **year:** 2023
- **doi:** 10.3390/coatings13020445
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Stiffness Mechanism

- interfacial tangential stiffness
- sliding between layers at imperfect interfaces

### Modeling Methods

- Single-variable zigzag beam theory.
- Global first-order shear deformation kinematics enriched with local piecewise functions for interfacial displacement jumps.
- Principle of Virtual Work for deriving homogenized equilibrium equations.
- Decomposition of transverse displacement into bending and shear components to select a fictitious bending primal variable.
- Sixth-order ordinary differential equation governing the fictitious bending displacement.
- A posteriori evaluation of transverse shear and normal stresses through 2D local Cauchy equilibrium equations.
- Comparison and validation against Pagano's 2D elasticity exact solutions via the transfer matrix method.

### Performance Metrics

- Nondimensional through-thickness local longitudinal displacement (k)v2.
- Nondimensional local bending normal stress (k)sigma22.
- Nondimensional local transverse shear stress (k)sigma23 determined from local equilibrium.
- Degree of correlation/overlap with 2D exact elasticity solutions.

### Future Work

- Extending the single-variable formulation to layered systems possessing elastic mismatch between adjacent layers.
- Implementing the single-variable model into numerical isogeometric collocation schemes.
- Incorporating modeling of thick interlayers or transition zones between adjacent layers as weak layers.
- Accounting for thermal loads, residual stresses, and misfit strains.

## V09 — Modelling tangential friction considering contact pressure distribution of rough surfaces

- **paper_id:** `8ce1db3bca`
- **year:** 2023
- **doi:** 10.1016/j.ymssp.2023.110406
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- Fractal geometry surface generation using a modified two-variable Weierstrass-Mandelbrot (WM) function.
- Power spectrum density (PSD) method for identifying fractal parameters (dimension D and roughness G) from surface measurements.
- Three-dimensional elastoplastic finite element contact analysis in Abaqus using 8-node brick elements (C3D8) and periodic boundary conditions.
- Twofold Weibull mixture probability density modeling of contact pressure and normal contact force.
- Nonlinear least squares parameter optimization using a genetic algorithm.
- Continuous Iwan-type distributed spring-slider model with residual stiffness spring.
- Coulomb friction law mapping normal contact force to slider critical slip force.
- Mindlin contact theory for tangential stiffness of individual asperities and sphere-on-sphere contact.
- Masing hypothesis for reloading and unloading tangential hysteresis loops.
- Series expansion representation of exponential functions to obtain explicit closed-form integration of the tangential force-displacement curve.

### Performance Metrics

- Tangential force-displacement hysteresis loop shape matching against analytical and experimental curves.
- Accuracy of modeling the transition regime from microslip to macroslip.
- Dissipated energy per cycle (mJ/cycle) and relative percentage error of dissipated energy.
- Goodness-of-fit and cumulative distribution function error of contact pressure distribution (maximum error < 0.06).
- Prediction accuracy of initial tangential contact stiffness.

### Future Work

- Incorporating non-uniform spatial distribution of contact pressure across bolted joint interfaces by dividing the contact zone into sub-regions with distinct contact loads.
- Applying the physics-based rough surface tangential friction model to predictive dynamic simulations and vibration analysis of assembled jointed structures.
- Extending the contact modeling approach to incorporate surface waviness alongside roughness.

## V10 — A novel friction model for steel-polymer interfaces in sliding seismic isolation bearings

- **paper_id:** `13e407003a`
- **year:** 2024
- **doi:** 10.1002/eqe.4128
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Direct C03 high-threat evidence on frictional interface mechanics; previously missing DOI 10.1002/eqe.4128.

### Robot / Structure Type


### Modeling Methods

- Three-element parallel base friction model: Coulomb element (constant quasi-static friction), logarithmic velocity-dependent element, and exponential displacement-dependent stick-slip element.
- State-dependent displacement tracking mechanism updating reference displacement uR only upon reversal of the sliding velocity direction.
- Thermal degradation modeling using an exponentially decaying temperature factor based on a contact-averaged temperature field.
- One-dimensional transient heat conduction formulation solved efficiently using discrete Fourier transforms (DFT / inverse DFT via FFT algorithms).
- Pressure modification factor utilizing a hyperbolic tangent functional form to model friction reduction under increasing normal pressure.
- Parameter calibration performed through least-squares error minimization against experimental force-displacement hysteretic loops.

### Performance Metrics

- Coefficient of determination (R^2) of the coefficient of friction.
- Maximum absolute error (MaxAbsErr) of the coefficient of friction.
- Visual goodness-of-fit to experimental normalized force-displacement and force-velocity hysteretic loops.

### Future Work

- Conducting bidirectional sliding experiments to investigate stick-slip behavior under multi-axial displacement paths.
- Extending and reformulating the proposed unidirectional friction model into a bidirectional sliding formulation.
- Evaluating the influence of bearing stick-slip behavior on the dynamic response of structural secondary systems and building contents during earthquakes.

## V11 — 改进的连续尺度分形−离散Iwan 黏滑接触力学建模 (Modeling of Stick-Slip Contact Mechanics Based on Improved Continuous-Scale Fractal-Discrete Iwan Model)

- **paper_id:** `8daa38176d`
- **year:** 2024
- **doi:** 10.15918/j.tbit1001-0645.2024.039
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- Continuous-scale fractal surface representation based on Morag-Etsion (ME) and Weierstrass-Mandelbrot (W-M) theories.
- Chang-Etsion-Bogy (CEB) single-asperity contact model defining elastic-fully plastic transitions.
- Two-variable continuous-scale asperity distribution function n'(a, l) dependent on asperity scale and contact spot area.
- Discrete Iwan stick-slip model with parallel Jenkins elements and geometric-series normal load distribution.
- Masing mapping rule for predicting cyclic tangential force-displacement hysteresis loops during unloading and reloading.

### Performance Metrics

- Dimensionless normal contact stiffness (K*) versus dimensionless normal load (Fn*)
- Relative area proportion of micro-contacts smaller than a specified area (A/Ar versus a/aL)
- Tangential force-displacement hysteresis curve profile and enclosed loop area (frictional energy dissipation)
- Initial tangential contact stiffness
- Macroscopic sliding friction force
- Critical macro-slip displacement threshold (xslip)
- Correlation between theoretical hysteresis loops and experimental measurements

### Future Work

- Replacing the constant macroscopic friction coefficient with local, fractal-described friction coefficients for individual micro-contacts to enhance physical fidelity.
- Developing theoretical or physics-based formulations for initial tangential stiffness to eliminate reliance on empirical parameter identification.
- Applying the stick-slip contact formulation in structural finite element simulations of mechanical assembly interfaces.

## V12 — Fretting wear modeling of bolted joint interface with microscopic roughness using the 1D microslip friction model and equivalent thin layer

- **paper_id:** `7b85aadc84`
- **year:** 2025
- **doi:** 10.1080/15397734.2025.2456000
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Modeling Methods

- 1D continuum elastic beam microslip model for lap joint interfaces
- Greenwood and Williamson (GW) statistical micro-contact model for rough surface contact with Gaussian asperity distribution
- Equivalent thin-layer representation of interface micro-asperity compliance with derived tangential contact stiffness
- Exponent-law non-uniform normal clamping pressure distribution
- Archard wear model combined with isolated relative sliding distance (subtracting elastic deformation from total displacement)
- Coulomb friction model for interfacial shear stress

### Performance Metrics

- Nondimensional slip length (1 - b) and stuck length (b)
- 2D cross-sectional wear profile and maximum wear depth (μm)
- Relative error between predicted and measured maximum wear depth (%)
- Relative error in maximum tangential displacement of hysteresis loops (%)
- Hysteresis loop enclosed area (frictional energy dissipation)
- Minimum tangential force to initiate microslip and maximum tangential force for full slip

### Future Work

- Extending the equivalent thin-layer contact model to incorporate multiple contact regimes including elastic, elastoplastic, and fully plastic deformation of micro-asperities.
- Investigating the generation, accumulation, and entrapment of abrasive wear debris and its influence on thin-layer properties and surface topography evolution during cyclic loading.

## V13 — Theoretical, experimental, and numerical simulation studies on interface slip in steel-concrete composite continuous beams with high-strength bolted connectors

- **paper_id:** `fb057ab3b2`
- **year:** 2025
- **doi:** 10.1016/j.istruc.2024.108126
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Stiffness Mechanism

- high-strength bolt shear connectors
- friction generated by bolt pretension

### Modeling Methods

- Derivation of a second-order non-homogeneous linear differential equation with constant coefficients governing interface slip using calculus and static force equilibrium
- Superposition principle from mechanics of materials to determine continuous beam deflections with additional slip-induced curvature
- Finite element analysis (FEA) using ABAQUS with C3D8R 3D solid elements for steel beams, bolts, concrete slabs, and washers, and T3D2 truss elements for reinforcement
- Concrete Damaged Plasticity (CDP) model for concrete behavior
- Bilinear elastic-plastic constitutive model for steel components and high-strength bolts
- MATLAB numerical computation for slip and deflection profiles along the beam length

### Performance Metrics

- Relative interface slip (mm)
- Slip strain along the interface
- Mid-span deflection and slip-induced additional deflection (mm)
- Concrete cracking load (Pcr = 150 kN) and steel yielding load (Pu = 450 kN)
- Ultimate failure load (673.4 kN experimental vs. 675.3 kN numerical)
- Relative percentage error between theoretical analytical solutions and finite element simulations

## V14 — A novel frictional contact correction transfer matrix method for bolted vibration systems: modeling, simulation, and experimental validation

- **paper_id:** `20cee2210a`
- **year:** 2026
- **doi:** 10.1016/j.ymssp.2026.114421
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Actuation

- piezoelectric ceramic (PZT) plate

### Modeling Methods

- Frictional Contact Correction Transfer Matrix Method (FCCTMM) with iterative angular correction
- Traditional Transfer Matrix Method (T-TMM) assuming rigid connections and rigid SISO elements
- Corrected Transfer Matrix Method (C-TMM) with frictional correction but rigid SISO elements
- Elastic Transfer Matrix Method (E-TMM) with elastic SISO elements but rigid contact interfaces
- Finite Element Method (FEM) under fully bonded contact interface assumptions in ANSYS 19.2
- Frictional Contact Correction Finite Element Method (FCCFEM) using augmented Lagrangian contact formulation and Newton-Raphson solver in ANSYS 19.2
- Timoshenko beam theory for longitudinal-bending coupled transfer matrices of elastic and piezoelectric beam elements
- Planar motion transfer matrices of massless rigid bodies for arbitrary SISO coordinate transformations
- Complex Young's modulus and loss factor formulation for material and piezoelectric damping

### Performance Metrics

- Resonant frequency relative error percentage relative to experimental measurements
- Modal Assurance Criterion (MAC) values evaluating mode shape correlation
- Computation time in seconds and speedup factor relative to finite element contact simulations
- Iteration counts and convergence tolerances for the iterative contact correction process
- Coefficient of variation (CV) for experimental friction coefficient and preload measurements
- Coefficient of determination (R^2) for linear regression of the torque-preload relationship

### Future Work

- Extending the transfer matrix framework to incorporate tangential micro-slip effects and detailed contact mechanics (friction coefficient and preload dependence) for lap-type connections under longitudinal or lateral vibration
- Applying the generalized transfer matrix formulation for elements with arbitrary input/output locations to vibration dynamic analysis of more complex engineering structures

## V15 — Stick-slip friction model for soft-hard joints under preload degradation

- **paper_id:** `02d3360815`
- **year:** 2026
- **doi:** 10.1016/j.ijmecsci.2026.111929
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Stiffness Mechanism

- compressible constrained layer damping (CCLD)
- pre-compression modulation

### Modeling Methods

- Scaling analysis of dominant interfacial energy dissipation mechanisms
- Modified Prony series expansion with fractional exponents for viscoelastic complex modulus representation
- Dynamic friction formulation integrating viscoelastic loss modulus, Hurst exponent, RMS roughness, and interfacial adhesion energy
- Power-law slip area ratio model characterizing the transition from localized micro-slip to global macro-slip
- Empirical cubic polynomial velocity-correction smoothing function defining an effective reference velocity near motion reversal
- Algebraic hysteretic mapping based on extended Masing rules for harmonic cyclic loading
- Finite-dimensional Jenkins/Iwan distributed slider formulation solved via linear complementarity problem (LCP) algorithm for comparative evaluation and general loading

### Performance Metrics

- Dynamic friction factor prediction accuracy across 7 orders of magnitude of sliding velocity (1E-5 to 1E2 m/s)
- Relative error in hysteresis-loop area (energy dissipation) within 3.3% across 0.01, 0.1, and 1 Hz cyclic shear tests
- Mean relative amplitude error between algebraic and 15-element differential models below 0.5%
- Computation time ratio RT = T_Alg / T_Diff = 0.1% under harmonic excitation (99.9% reduction in computational time)

### Future Work

- Conducting systematic dynamic parameter calibration experiments specifically on soft matter to capture dynamic viscoelastic complex moduli across frequencies
- Investigating the observed correlation between critical slip displacement ucrit and cyclic loading frequency
- Incorporating acceleration-dependent mechanisms to capture frictional-lag behavior during macro-slip
- Establishing quantitative relationships between reduced lumped model parameters (such as exponent chi) and measurable lower-level physical properties
- Improving measurement consistency and reducing uncertainty in the macroscopic mechanical properties of polymer foams to minimize lumped parameter tuning
- Conducting broader systematic experiments to extend the model's applicability across wider soft matter contact conditions

## V16 — The global-local mechanical behaviors of multilayered structure and applications to superconducting coils

- **paper_id:** `ca46dc062d`
- **year:** 2026
- **doi:** 10.1016/j.ijsolstr.2025.113689
- **source_type:** verification
- **verification_id:** D1-V006
- **screening_status:** included
- **screening_reason:** Included for D1-V006 C03 adversarial full-text verification of pressure/contact/friction coupling and model-validity transferability.

### Robot / Structure Type


### Stiffness Mechanism

- interfacial contact pressure and friction
- interfacial slip
- interlayer friction

### Actuation

- electromagnetic force
- mechanical displacement loading via indenter

### Modeling Methods

- Continuum theory for multilayered structures with homogenized contact and friction
- Lagrange-like continuous displacement field interpolation across shell midplanes
- Modified Green-Lagrange strain incorporating interfacial slip correction in transverse strain
- Principle of minimum potential energy and principle of virtual power
- Coulomb friction law formulated as an associative flow rule via maximum dissipation principle
- Finite element method (FEM) utilizing quadratic serendipity elements and order reduction of fourth-order PDEs into second-order PDEs with Galerkin method for distributed moment
- Penalty method regularization for friction update algorithms
- T-A formulation for nonlinear electromagnetic modeling coupled with mechanical equilibrium
- Discrete contact model (DCM) based on penalty contact for reference comparison

### Performance Metrics

- Relative error in displacement compared to discrete contact models (using a 5% error threshold for applicability)
- Computation time / runtime reduction (e.g., 10 s vs. 740 s; 1 h 20 min vs. 1 d 22 h)
- Memory consumption (4.4 GB vs. 80 GB)
- Permissible rotation angle for a target error threshold (20 degrees for n=30, 7.5 degrees for n=150)

### Future Work

- Extending the proposed continuum model to the mechanical analysis of other multilayered structures, including 2D materials (such as graphene) and nacre-like biological or composite materials
