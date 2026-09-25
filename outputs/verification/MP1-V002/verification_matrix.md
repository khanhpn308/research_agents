# Verification Matrix

**Verification ID:** MP1-V002
**Paper count:** 13
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — Superelastic shape memory alloy cables: Part I – Isothermal tension experiments

- **paper_id:** `00414aac4b`
- **year:** 2013
- **doi:** 10.1016/j.ijsolstr.2013.03.013
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** High-value NiTi cable baseline: full-scale 7x7 and 1x27 superelastic cable experiments; architecture, friction/sliding boundary, and phase-transformation response relevant to T1/T3 baseline.

### Robot / Structure Type


### Stiffness Mechanism

- Reversible stress-induced martensitic transformation (superelasticity)
- Cable construction architecture and helical lay angle variation

### Actuation

- Lead-screw driven electro-mechanical load frame (elongation control in uniaxial tension)

### Modeling Methods

- Calculation of idealized polar moment of inertia (J0) and reference elastic shear stress (Mz*R/J0) for cables
- Empirical exponential curve fitting and first-order Maxwellian differential rate equations for cyclic shakedown of characteristic stresses and residual strains

### Performance Metrics

- Loading and unloading plateau stresses (or characteristic knee stresses)
- Plateau strain extent and total recoverable superelastic strain
- Accumulated residual strain (ratcheting strain) after unloading
- Effective initial loading elastic modulus and unloading modulus
- Normalized reaction torque magnitude (Mz*R/J0)
- Specimen temperature deviation from ambient (Delta Ts)
- Cycle-to-cycle shakedown progression rate and asymptotic residual strain values

### Future Work

- Developing structural and constitutive models to capture multi-axial stress states, contact mechanics, and phase transformation kinetics in SMA cables
- Experimentally dissecting and testing hierarchical subcomponents (strands and single wires) in Part II to quantify individual constituent contributions
- Investigating higher strain rate regimes and thermomechanical coupling effects on cable behavior
- Exploring alternative cable architectures, layups, and geometries to tailor mechanical response, compliance, and energy absorption for specific applications

## V02 — Superelastic Shape Memory Alloy Cables: Part II – Subcomponent Isothermal Responses

- **paper_id:** `fac21c950e`
- **year:** 2013
- **doi:** 10.1016/j.ijsolstr.2013.03.015
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** High-threat MP1-V002 citation-chase paper for NiTi cable contact/subcomponent mechanics and parameter-substitution kill test.

### Robot / Structure Type


### Stiffness Mechanism

- superelasticity
- stress-induced martensitic transformation
- stress-induced rhombohedral phase (R-phase) transformation
- helical wire cable architecture / lay angle adjustment

### Actuation

- thermally-responsive actuation
- tendon-driven actuation

### Modeling Methods

- Analytic estimation of axial transformation force plateau for helical wire strands based on wire lay angle and tensile transformation stress.
- Analytic estimation of transformation-induced reaction torque for helical wire strands.
- Steady-state transformation front velocity relationship and local strain rate amplification formula.
- Subcomponent response subtraction methodology to infer individual wire layer force and torque contributions.
- Biot number heat transfer calculation assessing the validity of isothermal conditions in stagnant air.

### Performance Metrics

- Loading and unloading transformation plateau stress levels (MPa).
- Transformation plateau strain lengths and extents (%).
- Initial elastic modulus and tensile secant modulus at specified strain levels (GPa).
- Axial reaction torque magnitude (N-mm) and normalized torque (GPa).
- Residual unrecovered strain upon complete unloading (%).
- Ultimate strain at failure / breaking strain (%).
- Specimen surface temperature excursion amplitude (Delta Ts in °C).

### Future Work

- Developing reliable 3D structural and computational constitutive modeling tools to simulate the thermomechanical behavior of SMA cables.
- Gathering multiaxial constitutive data on tension, torsion, and bending of SMA wires to improve model fidelity.
- Exploring alternative cable cross-sections, lay architectures, and NiTi alloy compositions.
- Investigating shape memory behavior at elevated or sub-ambient transformation temperatures for thermally-responsive, high-tension cable actuators in flexible robotic and prosthetic systems.

## V03 — Nonlinear Vibration Absorber with Pinched Hysteresis: Theory and Experiments

- **paper_id:** `40760daa02`
- **year:** 2016
- **doi:** 10.1061/(ASCE)EM.1943-7889.0001072
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** High-threat full text: mixed NiTiNOL-steel wire rope under bending; directly couples interwire friction and NiTi phase transformation; relevant to T3 and parameter-substitution test.

### Robot / Structure Type


### Stiffness Mechanism

- cyclic bending of mixed NiTiNOL-steel wire ropes
- interwire friction within wire ropes
- martensitic phase transformations in superelastic NiTiNOL wires

### Actuation

- passive

### Modeling Methods

- Modified Bouc-Wen hysteretic model featuring an exponential pinching function
- Differential evolution (DE) heuristic algorithm for parameter identification and multi-amplitude restoring force optimization
- Continuation / path-following pseudo-arc-length method based on the Jacobian of the Poincaré map for periodic solution branches and stability evaluation
- Fourth-order Runge-Kutta numerical integration scheme for evaluating Poincaré maps
- Reduced single-degree-of-freedom (SDOF) and two-degree-of-freedom (2DOF) state-space dynamic modeling
- Nonlinear least-squares fitting using the Levenberg-Marquardt algorithm for modal decay parameter estimation

### Performance Metrics

- Mean-square error (MSE) between experimental and modeled force-displacement and frequency-response curves
- Equivalent viscoelastic damping ratio (ξ0) evaluated from loop enclosed area and average stiffness
- Resonance frequency and frequency-response curves (FRCs) across target bandwidth
- Differential evolution cost function defined as the integrated area subtended by FRCs across multiple excitation levels
- Percentage mitigation of top-floor peak displacement and peak acceleration

## V04 — Superelastic NiTi SMA cables: Thermal-mechanical behavior, hysteretic modelling and seismic application

- **paper_id:** `2f7fcf2f8f`
- **year:** 2019
- **doi:** 10.1016/j.engstruct.2019.01.049
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** High-threat MP1-V002 citation-chase paper for superelastic NiTi cable hysteretic modelling and parameter-substitution kill test.

### Robot / Structure Type


### Stiffness Mechanism

- solid-to-solid phase transformation between austenite and martensite phases (superelasticity)
- heat treatment (annealing) induced microstructure and elastic modulus modification

### Modeling Methods

- One-dimensional (1D) flag-shaped hysteretic phenomenological modeling.
- Displacement-based nonlinear fiber beam-column elements in OpenSees.
- Multi-layer concentric fiber approach combining Self-centering SMA material and Steel02 isotropic hardening steel material.
- Zero-length gap elements placed in series to capture cable slack displacement.
- Uniaxial Menegotto-Pinto constitutive modeling for reinforcing steel bars.
- Kent-Scott-Park uniaxial constitutive modeling for confined and unconfined concrete.
- Zero-length spring elements with ideal elastic-plastic behavior for sliding bearings and soil-structure interaction (SSI).
- Nonlinear dynamic time-history analysis under unscaled earthquake ground motion (El Centro EW).

### Performance Metrics

- Transformation temperatures: Ms, Mf, As, Af, and R-phase peak temperatures (°C)
- Forward transformation start stress / yield strength (MPa) and finish stress (MPa)
- Reverse transformation start and finish stresses (MPa)
- Peak tensile stress (MPa)
- Initial elastic modulus (GPa)
- Accumulated residual strain (%) and recovery rate (%)
- Equivalent viscous damping ratio (EVD) (%)
- Peak girder displacement (mm) and residual girder displacement (mm)

### Future Work

- Testing larger-diameter SMA cables and calibrating numerical models to reduce the required number of physical restrainers.
- Evaluating seismic response under a wider and more diverse suite of earthquake ground motions.
- Developing a comprehensive performance-based design framework for structures incorporating SMA-cable restrainers.

## V05 — Nonlinear dynamic response of a wire rope isolator: Experiment, identification and validation

- **paper_id:** `7f3f45407f`
- **year:** 2021
- **doi:** 10.1016/j.engstruct.2021.112121
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Generic wire-rope mechanics baseline: interwire friction and geometric nonlinearity with experimentally identified phenomenological model; relevant to parameter-substitution test.

### Robot / Structure Type


### Stiffness Mechanism

- curved wire rope assembly undergoing interwire friction and geometric nonlinearities
- asymmetric tension-compression stiffness exhibiting softening under compression and hardening under tension
- tightening of spiral cable strands under tension and loosening under compression

### Modeling Methods

- Modified asymmetric Bouc-Wen hysteretic formulation with velocity-dependent control functions and asymmetric cubic polynomials
- Differential evolution optimization algorithm for parameter identification from quasi-static cyclic test data
- Lumped-parameter two-degree-of-freedom (2DOF) dynamic modeling using coupled second-order ordinary differential equations
- Numerical time-domain integration of equations of motion and Fast Fourier Transform (FFT) stationary response analysis
- Analytical transfer function and closed-form frequency response function modeling for the linear uncontrolled cantilever structure

### Performance Metrics

- Transmissibility coefficient (H) for displacement and absolute acceleration across 5–100 Hz
- Peak displacement and acceleration amplitudes at primary and superharmonic resonances
- Resonant frequency shift between non-isolated and isolated configurations
- Equivalent secant stiffness and equivalent hysteretic damping across displacement amplitudes
- Spectral power distribution of fundamental and superharmonic frequencies via FFT

## V06 — Hysteresis of Multiconfiguration Assemblies of Nitinol and Steel Strands: Experiments and Phenomenological Identification

- **paper_id:** `d9966f2f5e`
- **year:** 2014
- **doi:** 10.1061/(ASCE)EM.1943-7889.0000852
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Stiffness Mechanism

- Geometric hardening (tensile stretching induced by constrained kinematics during flexural deformation)
- Thermoelastic martensitic phase transformation / superelasticity of Nitinol wires and strands
- Interwire friction / contact sliding between individual wires within strands and wire ropes
- Kinematic reconfiguration / boundary constraint adjustment (locking horizontal sliding, permitting free sliding, or elastically coupling sliding blocks with a secondary stiffness group to alter the stiffness ratio)

### Actuation

- External displacement-controlled cyclic actuation applied by a Material Testing System (MTS) hydraulic actuator (piston P)

### Modeling Methods

- Extended Bouc-Wen (BW) phenomenological hysteresis model augmented with a two-parameter bell-shaped pinching function h(x) modulating origin tangent stiffness
- Linear-cubic elastic restoring force formulation combined with the hysteretic displacement variable
- Ivshin-Pence one-dimensional thermomechanical constitutive model for shape memory alloy wires and strands under uniaxial tension
- Differential Evolution (DE) metaheuristic optimization algorithm for parameter calibration via mean square error minimization

### Performance Metrics

- Mean Square Error (MSE, %) between experimental force-displacement measurements and model predictions
- Hysteretic energy dissipation per cycle represented by the enclosed loop area
- Hysteretic tangent stiffness and upper/lower bounds of the hysteretic force variable
- Residual strain / displacement upon full unloading at zero restoring force

### Future Work

- Developing systematic procedures for selecting a unified, amplitude-independent parameter set for dynamic simulations (such as identifying parameters from an average displacement amplitude or minimizing MSE across multiple amplitudes simultaneously)
- Applying multiconfiguration strand assemblies and the extended Bouc-Wen pinching model to passive or semiactive nonlinear vibration control devices and nonlinear vibration absorbers

## V07 — Superelasticity SMA cables and its simplified FE model

- **paper_id:** `9e15094d68`
- **year:** 2023
- **doi:** 10.1007/s40430-022-03957-2
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Stiffness Mechanism

- Shape memory alloy superelasticity (pseudoelasticity)
- Stress-induced solid phase transformation

### Modeling Methods

- Finite element (FE) modeling and numerical analysis in ANSYS.
- Refined 3D solid FE model using surface-to-surface contact elements (CONTA174 on central wire surface and TARGE170 on outer wire surfaces).
- Simplified FE model using coupled sections that couple translational degrees of freedom of cross-sectional nodes at spacing Δl without contact elements.
- Auricchio 3D superelasticity material formulation (accessed via TB, SMA in ANSYS).

### Performance Metrics

- Hysteresis loop area and percentage variation in energy dissipation capacity (within 5.8%).
- Computation time (reduction from 23 h to 30 min).
- Tensile force at the upper transformation plateau.
- Von Mises stress magnitude and stress ratio between core and outer strands (central strand 13.3% higher).
- Ductility comparison between strands and individual wires.
- Initial stiffness of the strand or rope.

## V08 — Mechanical response of single and double-helix SMA wire ropes

- **paper_id:** `53200aa0c6`
- **year:** 2021
- **doi:** 10.1080/15376494.2021.1955313
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Actuation

- thermal actuator
- thermal lock

### Modeling Methods

- Three-dimensional phenomenological SMA constitutive model (Souza model) based on plasticity theory and irreversible thermodynamics
- Finite element analysis using implicit solution method in Abaqus software
- User-defined material subroutine (UMAT) implementation
- Kinematic coupling of cross-sectional nodes at centerline reference points to enforce tensile displacement without artificial clamping constraints
- Surface-to-surface interwire contact formulation with tangential and normal interaction including Coulomb friction
- Parametric helical geometric modeling for single-helix and double-helix cables based on Stanova et al. formulation
- Design of experiments (3^2 factorial design and response surface methodology using Design-Expert software)

### Performance Metrics

- Specific energy (g = F * delta / M in J/kg or equivalent force*displacement/mass)
- Normal stress-strain response (MPa vs. strain)
- Shear stress-strain response (MPa vs. strain)
- Axial force distribution across components (N) as a function of displacement (mm)
- Inelastic strain recovery as a function of temperature and time during heating
- Discrepancy / percentage error relative to reference experimental and numerical data

## V09 — Nonlinear Vibration Isolation via a NiTiNOL Wire Rope

- **paper_id:** `98fee47c04`
- **year:** 2021
- **doi:** 10.3390/app112110032
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Stiffness Mechanism

- NiTiNOL wire rope under geometric constraints (beam flexure under tension)
- vertical linear spring
- pseudoelastic phase transitions and pinching effect of NiTiNOL

### Modeling Methods

- Beam constraint model (two-dimensional beam flexure under initial axial tension)
- Modified Bouc-Wen phenomenological model with an exponential pinching effect function
- Harmonic balance method (HBM) with first- and third-order harmonics
- Alternating frequency/time domain (AFT) technique
- Arc-length continuation method
- Runge-Kutta numerical integration (direct time-domain integration)

### Performance Metrics

- Displacement transmissibility TD (dimensionless payload response amplitude ap = Ap / Ab)
- Peak displacement transmissibility Tp and minimum peak transmissibility Tpmin
- Resonant frequency and minimum resonant frequency eta_rmin
- Generalized equivalent stiffness ke (dimensional Ke)
- Generalized equivalent damping ratio zeta_e
- Most suitable excitation amplitude for resonance suppression (Ab-pmin) and for low-frequency vibration isolation (Ab-rmin)

## V10 — Cable Vibration Considering Internal Friction

- **paper_id:** `aaad9c248c`
- **year:** 2004
- **doi:** 
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Stiffness Mechanism

- variable flexural rigidity
- interlayer dry friction
- relative wire slippage
- interlayer radial pressure

### Modeling Methods

- One-dimensional continuum formulation for the governing fourth-order nonlinear partial differential equation of motion of transverse cable vibration (PAGE 13, 16, 20).
- Variational weak formulation in Sobolev space H1_0(Omega) (PAGE 20, 21).
- Finite Element Method (FEM) using fifth-order Hermite interpolation polynomials to ensure continuity of third derivatives of transverse deflection (PAGE 12, 22, 24).
- Derivation of elemental consistent mass, stiffness, and stability matrices (PAGE 24, 25).
- Newmark direct numerical time integration scheme with linear acceleration (beta = 0.25, gamma = 0.5) for solving dynamic equations (PAGE 12, 26, 27, 28).
- Incremental Newton-Raphson iterative formulation for resolving nonlinear equilibrium states (PAGE 29).
- Nonlinear flexural rigidity-curvature relationship evaluated via CableCAD software incorporating measured interlayer pressures (PAGE 12, 16, 18).
- Post-step least-squares polynomial curve fitting applied to smooth cable displacement configurations across time increments (PAGE 33, 47).

### Performance Metrics

- Vibration displacement amplitude decay over time (PAGE 37, 41, 44, 46, 53).
- Sum of squared error between least-squares fitted curve and nodal data points after time iteration (0.0024 reported after first iteration) (PAGE 47, 48).
- Percentage error between numerical predictions and experimental displacement measurements (within 10%) (PAGE 53).
- Force-displacement hysteresis cycle slope and enclosed hysteresis loop area (PAGE 54, 55).
- Maximum theoretical flexural rigidity at zero curvature (EI_max = 64.971 N*m^2 / 6.5 x 10^7 N*mm^2) (PAGE 16, 69).

### Future Work

- Extend the analytical bending model to include the effects of torsion, axial elongation, interlayer pressures, and geometric and material nonlinearities into an updated stiffness matrix (PAGE 57).
- Perform more accurate experimental determinations of interlayer radial pressure, such as using pressure-indicating sensor films (PAGE 57).
- Incorporate internal material damping as well as external damping effects to formulate damped cable vibration (PAGE 57).
- Apply large motion and deformation theory to replace the current small deformation assumption for more realistic dynamic results (PAGE 57).

## V11 — BENDING MECHANICS OF CABLE CORES AND FILLERS IN A DYNAMIC SUBMARINE CABLE

- **paper_id:** `ccdc1bb980`
- **year:** 2017
- **doi:** 
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Modeling Methods

- 3D finite element (FE) modeling representing 1/3 of the lay-length of the cable power cores incorporating all components (cores, fillers, armour wires, tapes, sheaths).
- Geometrically non-linear FE formulation accounting for large rigid body rotations, sliding, and component twisting.
- Non-linear penalty contact formulation in the normal direction and Coulomb friction formulation with elastic slip limit in the tangential direction.
- Periodic boundary condition formulation applied at both ends of the cable segment.
- Analytical modeling of axial stress combining axisymmetric tensile/pressure stress, curvature-change bending stress, and loxodromic stick-slip friction stress.

### Performance Metrics

- Contact lineload per unit length (kN/m).
- Axial stress range and cyclic stress history in the conductor (MPa).
- Relative slip distance in axial/loxodromic and transverse/radial directions (mm).
- Shear strain percentage in profile fillers (gamma_theta_z, %).
- Agreement/discrepancy between analytical stress equations and 3D FE simulation outputs.

### Future Work

- Development of an analytical formulation for the relative slip and kinematic interactions of helically-interwound power cores.
- Use of the 3D FE modeling results to verify and refine analytical formulations for fatigue life assessments of dynamic cables.

## V12 — High damping capacity with a wide temperature window in braided NiTi microfilaments

- **paper_id:** `e8462758c3`
- **year:** 2026
- **doi:** 10.1016/j.matlet.2026.141544
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Stiffness Mechanism

- Braided architecture (spatial helical interlacing and double-braiding creating a micro-spring network converting deformation into localized bending and torsion)
- Sequential localized martensitic transformation induced by inhomogeneous stress distribution within the braided structure
- Geometric constraint variation via braiding density (picks per inch, ppi)

### Performance Metrics

- Loss tangent (tanδ) / internal friction damping plateau values (e.g., ~0.11 for 88B; 0.02-0.05 for 8B; 0.008-0.02 for 4B; 0.03-0.06 for 12B; 0.02-0.04 for ppi80)
- Storage modulus in GPa (e.g., ~3.6-4.3 GPa for 88B; ~11-12 GPa for 8B; ~17-19 GPa for 4B; ~18-22 GPa for 12B vs. ~20-61 GPa for single wire)
- Operating temperature window width (>145 °C, from -70 °C to 75 °C)
- Cyclic repeatability of damping performance (10 cooling-heating cycles)
- Frequency insensitivity (overlap of tanδ and modulus curves between 1 Hz and 5 Hz)

## V13 — NiTi SMA Superelastic Micro Cables: Thermomechanical Behavior and Fatigue Life under Dynamic Loadings

- **paper_id:** `6dd1ca94d1`
- **year:** 2022
- **doi:** 10.3390/s22208045
- **source_type:** verification
- **verification_id:** MP1-V002
- **screening_status:** included
- **screening_reason:** Concrete full-text mechanics threat to MP1-V002 T1/T2/T3.

### Robot / Structure Type


### Stiffness Mechanism

- superelasticity
- stress-induced martensitic phase transformation
- thermomechanical coupling / temperature-induced stiffening governed by the Clausius-Clapeyron law

### Modeling Methods

- Calculation of dissipated energy per cycle (ED) via numerical integration of the stress-strain hysteresis loop (closed contour integral of σ dε).
- Calculation of equivalent viscous damping factor (ξ) using the dissipated energy normalized by 4π times the equivalent linear stored elastic energy.
- Identification of the critical self-heating frequency (fc) via interpolation of the zero-crossing of percentage peak stress difference (Δσ = 0) between the 1st and 128th cycles.
- Linear Clausius-Clapeyron phase diagram regression to determine temperature stress coefficients CM (5.54 MPa/°C) and CA (6.28 MPa/°C).
- Asymptotic non-linear regression modeling of cycle temperature amplitude (Tamp) as a function of loading frequency.
- Linear regression modeling of 128th cycle mean temperature (Tmean) and cycles to failure (Nf) as functions of loading frequency.

### Performance Metrics

- Critical self-heating frequency (fc, in Hz)
- Dissipated energy per cycle (ED, in MJ/m³)
- Equivalent viscous damping factor (ξ, in %)
- Upper Plateau Strength (UPS, in MPa) and Lower Plateau Strength (LPS, in MPa)
- Peak tensile stress (σpeak, in MPa) and peak stress variation (Δσ, in %)
- Temperature amplitude (Tamp, in °C) and mean temperature (Tmean, in °C)
- Cycles to failure (Nf for first failure and Nif for the ith failure, in cycles)

### Future Work

- Conducting detailed statistical fatigue analyses across larger specimen cohorts to establish probabilistic fatigue life distributions.
- Investigating varying environmental convective and conductive heat transfer boundary conditions to control self-heating.
- Optimizing cable manufacturing processes to minimize surface defect generation (e.g., dimples) that accelerate crack initiation.
