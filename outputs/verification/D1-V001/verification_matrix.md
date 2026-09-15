# Verification Matrix

**Verification ID:** D1-V001
**Paper count:** 3
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — Mechanically Versatile Soft Machines through Laminar Jamming

- **paper_id:** `5f7ccd7357`
- **year:** 2018
- **doi:** 10.1002/adfm.201707136
- **source_type:** verification
- **verification_id:** D1-V001
- **screening_status:** included
- **screening_reason:** Foundational laminar-jamming study directly relevant to interlayer slip, friction, bending stiffness, and deformation-regime modeling; included as adversarial prior work for D1 verification.

### Robot / Structure Type

- soft machines, pneumatic soft bending actuator, cable-actuated variable kinematics system, two-fingered grasper, continuum manipulators

### Stiffness Mechanism

- laminar jamming (layer jamming)

### Actuation

- vacuum pressure (pressure gradient)
- pneumatic actuation
- cable actuation

### Modeling Methods

- Euler-Bernoulli beam theory extended for vacuum pressure, interfacial friction, and interfacial slip
- Boundary-value problem formulation and explicit analytical solution for cantilevered two-layer jamming beams under uniform distributed load
- Two-dimensional plane-strain finite element analysis (ABAQUS 6.14r2) with penalty contact friction formulation and large-deformation analysis

### Performance Metrics

- Bending stiffness (pre-slip, transition, and full-slip stiffness values; n^2 theoretical multiplier; >=32-fold measured increase in finger bending stiffness)
- Goodness-of-fit coefficient of determination (R^2 >= 0.9879 for FEA vs. experimental bending force; R^2 = 0.9835 for shape-locking fidelity)
- Discreteness ratio (maximum curvature to mean curvature, kappa_max / kappa_mean, increasing by a factor of 6.65)
- Perturbation resistance force (at least 8-fold increase in dislodging force for pinch grasping)
- Off-axis bending stiffness (2.5-fold increase under vacuum)
- Torsional stiffness (2.7-fold increase under vacuum)
- Full-slip damping force (analytically expressed as mu*P*b*h)
- Experimental repeatability (maximum deviation of 0.24 N across loading cycles and samples)

### Future Work

- Approximating high-layer-count jamming structures as a single crystal with a single slip system to reduce finite element computational runtime.
- Incorporating a one-way valve to maintain vacuum without requiring a tethered continuous vacuum source.
- Using electrostatic actuation or elastic actuation (such as external elastic mesh envelopes or spring clips) to overcome ambient atmospheric pressure limits on normal force.
- Applying variable kinematics to medical and surgical devices traversing vasculature before applying high forces, as well as continuum manipulators.

## V02 — Layer jamming: Modeling and experimental validation

- **paper_id:** `652e62758f`
- **year:** 2023
- **doi:** 10.1016/j.ijmecsci.2023.108325
- **source_type:** verification
- **verification_id:** D1-V001
- **screening_status:** included
- **screening_reason:** Direct prior work on multi-layer vacuum layer jamming, interlayer slip propagation, bending stiffness, analytical modeling, finite-element simulation, and experimental validation; critical adversarial evidence for testing the novelty boundary of D1.

### Robot / Structure Type


### Stiffness Mechanism

- layer jamming
- vacuum jamming
- interlayer friction coupling

### Actuation

- vacuum pressure
- transverse mechanical loading

### Modeling Methods

- Euler-Bernoulli beam theory
- Jourawski formula for shear stress distribution in rectangular cross-sections
- Piecewise linear approximation of stiffness degradation corresponding to discrete slip propagation steps
- Clamped boundary condition representation at support lines to capture overhanging stiffness contributions
- Finite element analysis (FEA) in Abaqus/Standard 2017 using 2D four-node bilinear hybrid plane strain elements with reduced integration (CPE4RH), penalty friction formulation, and geometric nonlinearity (Nlgeom ON)

### Performance Metrics

- Force versus deflection response across deformation regimes
- Critical transition loads (F_0, F_1, F_i) and deflections (w_0, w_1, w_i)
- Variable stiffness ratio between jammed and unjammed states (scaling with n^2)
- Energy dissipated per load-unload cycle (hysteresis loop area)

## V03 — Layer Jamming of Magnetorheological Elastomers for Variable Stiffness in Soft Robots

- **paper_id:** `56d058a34a`
- **year:** 2024
- **doi:** 10.1007/s11340-024-01031-7
- **source_type:** verification
- **verification_id:** D1-V001
- **screening_status:** included
- **screening_reason:** Recent layer-jamming study directly relevant to pre-slip, partial-slip, full-slip, friction assumptions, and stiffness evolution; included to test the mechanics and novelty claims of D1.

### Robot / Structure Type


### Stiffness Mechanism

- layer jamming
- multi-layer jamming
- magnetic jamming
- magnetorheological elastomer viscoelasticity change

### Actuation

- magnetic
- flexible NdFeB permanent magnets

### Modeling Methods

- Euler-Bernoulli beam theory for pre-slip and post-slip bending stiffness formulations and area moment of inertia scaling
- Hyperelastic material modeling using the Neo-Hookean strain energy function calibrated from uniaxial tensile data
- 3D magnetostatic finite element analysis in ANSYS to compute magnetic surface force magnitudes and distributions as a function of beam deflection and MRE volume fraction
- 2D quasi-static finite element analysis in ANSYS with large deflection using plane-stress elements and frictional contact pairs

### Performance Metrics

- Bending stiffness (N/mm) in ON and OFF states
- Stiffness ratio K (ratio of ON-state stiffness to OFF-state stiffness)
- Mean slip initiation deflection (mm)
- Full slip deflection (mm)
- Average magnetic jamming force (N)
- Kinetic coefficient of friction (µ)

### Future Work

- Employing electronically controlled electro-permanent magnets (EPMs) or electromagnets to allow rapid millisecond switching between jammed and unjammed states with low power consumption, eliminating manual magnet exchange
- Reducing MRE sheet thickness via micro-molding or extrusion-based 3D printing to enable stacking a higher number of layers
- Fabricating anisotropic MREs with aligned CIP chains parallel to the magnetic field direction to enhance the MR effect
- Utilizing elastomer matrices with lower modulus to increase the relative stiffening ratio of the MREs
- Developing a soft robot integrating axial MRE fibers within a central channel enclosed by radially polarized EPMs to achieve multi-directional variable bending stiffness
