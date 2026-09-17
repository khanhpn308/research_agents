# Verification Matrix

**Verification ID:** D1-V002
**Paper count:** 4
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — A continuum-based model for a layer jamming beam

- **paper_id:** `95646b2cfc`
- **year:** 2025
- **doi:** 10.5194/ms-16-821-2025
- **source_type:** verification
- **verification_id:** D1-V002
- **screening_status:** included
- **screening_reason:** Direct prior work on a continuum-based layer-jamming beam model; potentially decisive for testing P1's claimed gap concerning scalable continuum/homogenized representation, interlayer slip, and model validity limits.

### Robot / Structure Type


### Stiffness Mechanism

- layer jamming

### Actuation

- vacuum pressure

### Modeling Methods

- Continuum mechanics modeling treating multi-layer systems as a continuous medium under the limit of infinite thin layers (delta -> 0, n -> infinity).
- Euler-Bernoulli curved beam equilibrium formulations relating internal forces (axial force N, shear force Q, moment M) to distributed loads.
- Sectional elastoplastic analysis in tau-sigma stress space implementing Coulomb friction slip criteria.
- Step-by-step incremental algorithm to handle large external loads under small-deformation incremental steps.
- Finite element analysis (FEA) using Abaqus with 2D plane-stress quadrilateral elements (CPS4R).

### Performance Metrics

- Load-deflection response and deviation relative to the experimental mean and +/- 1 standard deviation interval
- Agreement of predicted normal and shear stress profiles across the cross-section with FEA benchmarks
- Extent and boundary position of the interlayer sliding zone (ys)

### Future Work

- Incorporation of boundary correction factors into the continuum model to better capture end effects near constraints and free ends.
- Development of a more detailed analytical treatment of beam curvature in the jamming region under large-slip conditions.
- Utilization of FEA for final verification of designs near free boundaries or under extreme loads causing full slipping.

## V02 — Analysis and modeling of nonlinear saturated behavior of layer jamming soft pneumatic bending actuator

- **paper_id:** `1337634c62`
- **year:** 2025
- **doi:** 10.1088/1361-665X/adbf56
- **source_type:** verification
- **verification_id:** D1-V002
- **screening_status:** included
- **screening_reason:** Direct novelty threat to P1: experimentally models a 25-layer vacuum-actuated layer-jamming soft actuator, explicitly discussing progressive interlayer slip, stiffness degradation, nonlinear hysteresis, and prediction error.

### Robot / Structure Type

- layer jamming soft pneumatic bending actuator

### Stiffness Mechanism

- layer jamming

### Actuation

- pneumatic actuation
- vacuum actuation

### Modeling Methods

- Strain energy method combining Neo-Hookean hyperelastic strain energy for the silicone actuator and Euler-Bernoulli beam strain energy for the layer jamming packet
- Taylor series expansion to approximate deformation invariant terms
- Castigliano's first theorem to derive the pressure-bending angle governing equilibrium equation
- Modified Prandtl-Ishlinskii (PI) model combining rate-independent backlash operators, multi-condition saturation functions, and an exponential cycle-dependent growth term for saturated hysteresis
- Least-squares optimization for identifying hysteresis model parameters

### Performance Metrics

- Stiffness enhancement ratio (greater than 9-fold increase upon activation)
- Strain energy model prediction error in the linear range (6.3% average error)
- Modified Prandtl-Ishlinskii model prediction error (8.5% average error during identification; approximately 8% at doubled frequency)
- Maximum input pressure tested (up to 1.57 bar) and corresponding bending angles
- Residual deformation angle (ranging from 3.6 degrees at 1.0 bar to 14 degrees at 1.57 bar)
- Sensor measurement accuracy (within 0.1 degrees) and DAQ nominal angular resolution (approximately 0.005 degrees)

### Future Work

- Extending the modeling framework to dynamic operating conditions
- Determining the upper frequency limits of the proposed quasi-static hysteresis model
- Comparing accuracy between the proposed model and dynamic models across varying actuation frequencies

## V03 — Continuum modeling for layer jamming structures

- **paper_id:** `a792efc445`
- **year:** 2026
- **doi:** 10.1016/j.taml.2025.100633
- **source_type:** verification
- **verification_id:** D1-V002
- **screening_status:** included
- **screening_reason:** Direct full-text prior work on continuum constitutive modeling of layer-jamming structures; critical for evaluating whether P1's proposed continuum-model validity/breakdown gap remains unresolved.

### Robot / Structure Type


### Stiffness Mechanism

- layer jamming
- interlayer friction

### Actuation

- vacuum
- hydrostatic pressure

### Modeling Methods

- Representative Volume Element (RVE) formulation spanning two layers
- First-order displacement field approximation through layer thickness
- Average-field theory (volume averaging for macroscopic stress and Bagi's boundary surface integral method for macroscopic displacement gradient)
- Elastoplastic continuum constitutive modeling (Coulomb-based slip condition function, yield surface tracking, and trial elastic stress increment decomposition)
- Finite element analysis (FEA) in Abaqus 6.14 with master-slave periodic boundary conditions, C3D8H hybrid linear hexahedral elements, virtual reference points, and finite sliding surface-to-surface contact

### Performance Metrics

- Elastic shear stiffness in the jamming state (GPa)
- Critical shear stress / yield boundary threshold for slip initiation (MPa)
- Residual shear strain upon unloading (per mille)
- Evolution of frictional dissipation energy density (mJ/mm^3 or equivalent energy per unit volume)
- Evolution of elastic strain energy density
- Relative deviation between theoretical continuum predictions and numerical FEA results

### Future Work

- Validate the proposed continuum model at the structural level by measuring macroscopic responses (such as bending stiffness, shear compliance, and energy dissipation) on physical layer jamming prototypes
- Integrate the continuum modeling framework into the design, optimization, and control of soft robotic systems and other jamming-based stiffness-tunable adaptive structures

## V04 — Toward a deeper understanding of layer jamming structures

- **paper_id:** `7cb387b88d`
- **year:** 2025
- **doi:** 10.1007/s11465-025-0843-5
- **source_type:** verification
- **verification_id:** D1-V002
- **screening_status:** included
- **screening_reason:** Direct 2025 full-text prior work relevant to large-deformation mechanics, pressure, layer-thickness effects, cyclic loading, and validity limits of layer-jamming models.

### Robot / Structure Type

- Layer jamming structure (LJS) beam (the paper investigates variable-stiffness layer jamming structure beam elements for soft robotics rather than a complete robotic device)

### Stiffness Mechanism

- layer jamming
- beam-stack layer jamming
- vacuum-induced interlayer friction

### Actuation

- vacuum
- hydrostatic pressure
- vacuum pressure

### Modeling Methods

- Finite element analysis (FEA) in Abaqus using 2D CPS4R elements under plane stress conditions
- Euler-Bernoulli beam theory extended to multi-layer composite beams with interlayer friction and sliding
- Cross-sectional stress distribution formulation for full-jamming, half-jamming, and full-sliding regimes
- Internal force equilibrium differential equations for curved continuous medium beams
- Quadratic closed-form approximation for the sliding boundary ys as a function of shear force Q
- Governing differential equation for angular deformation increment (Δθ') derived from strain compatibility and constitutive relations
- Iterative multi-step algorithm based on stress increments for large deformations and non-monotonic loading
- Equivalent moment of inertia (Ieq) formulation across sliding states

### Performance Metrics

- Bending stiffness (differential quotient ΔF/Δw)
- Critical load and critical shear force (Qcr) for sliding initiation
- Deflection under concentrated bending load
- Equivalent moment of inertia (Ieq, Ieq_max, Ieq_min)
- Load-deflection hysteresis loop area (frictional energy dissipation)
- Theoretical-to-experimental correlation across varying pressures and layer thicknesses

### Future Work

- Extending the analytical modeling methodology from beam-stack LJS to shell-stack LJS and other jamming configurations involving bending deformations
- Applying the model to structural design and optimization of soft robotic systems, prosthetics, and controllable-stiffness mechanisms
