# Verification Matrix

**Verification ID:** D1-V007
**Paper count:** 3
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — A coupled electromagnetic-mechanical model for high temperature superconducting coils based on circuit model

- **paper_id:** `6bdb4151e2`
- **year:** 2026
- **doi:** 10.1016/j.supcon.2026.100280
- **source_type:** verification
- **verification_id:** D1-V007
- **screening_status:** included
- **screening_reason:** C04 high-threat direct descendant. Explicitly uses the multilayer continuum mechanical model associated with focal paper ca46dc062d, includes interfacial slip and experimental/numerical validation; directly relevant to testing whether P1 remains novel.

### Robot / Structure Type


### Modeling Methods

- Axisymmetric partial element equivalent circuit (A-PEEC) model based on Kirchhoff's current and voltage laws
- Multilayer structural continuum mechanics model based on elastic thin shell theory satisfying the Kirchhoff-Love hypothesis and incorporating interfacial slip
- Artificial neural network (ANN) with dual hidden layers to compute quadruple integrals for mutual and self-inductance from the Neumann formula
- Split-field iteration method coupling the circuit model in MATLAB (ode15s) with COMSOL finite-element magnetic and mechanical solvers
- Power-law E-J relation for superconducting resistive voltage and magnetic vector potential (A-formulation) for magnetic field solution
- Deformation-dependent critical current model incorporating magnetic field angle deflection and hoop strain degradation

### Performance Metrics

- Inductance evaluation computation time: approximately 0.02 s (ANN) vs. 10,199 s (numerical integration)
- Inductance coefficient relative error: maximum error <= 0.01%
- Relative error in strain difference compared to experimental data: 15.5% (coupled) vs. 70% (uncoupled)
- Maximum hoop strain suppression/amplification: 0.35% vs. 0.457% (early stage) and 0.481% vs. 0.456% (steady state)
- Split-field convergence iterations per time step: typically 3 to 5 iterations
- Loss power magnitudes: azimuthal magnetization loss power and radial Joule heating loss power

### Future Work

- Incorporating a more detailed contact resistance description that accounts for local contact pressure, preload, surface condition, and inter-turn sliding

## V02 — A global-local homogenization model for hierarchical chiral helical structures: Tension-torsion coupling and decoupling analysis

- **paper_id:** `1502d9c1c6`
- **year:** 2026
- **doi:** 10.1016/j.ijengsci.2026.104615
- **source_type:** verification
- **verification_id:** D1-V007
- **screening_status:** included
- **screening_reason:** C04 forward citation retained. Adjacent homogenization study with global-local mechanics, contact treatment, explicit model assumptions and quantitative validity ranges; medium relevance to P1 validity-boundary question.

### Robot / Structure Type


### Stiffness Mechanism

- Hierarchical chiral helical winding
- Tension-torsion coupling and decoupling
- Interwire line contact mechanics

### Modeling Methods

- Global-local homogenization model based on strain linearization
- Love's thin rod theory for curved rods in local Frenet coordinate systems
- Johnson's Hertzian contact theory and plane strain elastic cylinder contact formulation
- Kinematic analogy method for comparison of second-order helical kinematics
- Three-dimensional finite element modeling (FEM) with C3D8R elements

### Performance Metrics

- Stiffness prediction relative error compared to the Argatov analytical model (<7% error across beta_1 in [60 deg, 89 deg])
- Discrepancy with the kinematic analogy method (~6% difference at m = 3, beta_2 = 79 deg)
- Computational speedup (seconds for analytical homogenization model vs. ~1 hour for 3D FEM with 1.46 x 10^5 elements on an Intel Core i9-14900KF CPU)
- Tension-torsion coupling-decoupling coefficient (eta in [0, 1])
- Elastic strain energy partition ratios (tensile, torsional, coupling, contact)
- Peak Von Mises stress and contact stress concentration magnitude
- Target curve fitting error / decoupling load separation capability

### Future Work

- Incorporating tangential friction behavior into the homogenization framework to examine frictional dissipation under cyclic loading
- Extending the theoretical formulation to hyperelastic constitutive laws suitable for soft fibrous hierarchical structures
- Developing multi-level chiral array assemblies for complex mechanical signal encoding, high-precision curve reconstruction, and multifunctional mechanical logic operations

## V03 — Critical state model for superconductivity: features and numerical implementation

- **paper_id:** `a32f8501d6`
- **year:** 2026
- **doi:** 10.1016/j.jcp.2026.115273
- **source_type:** verification
- **verification_id:** D1-V007
- **screening_status:** included
- **screening_reason:** C04 citation-chain closure paper. Direct mechanical relevance is low, but retained to document and audit all currently identified Scopus forward citations of focal paper ca46dc062d.

### Robot / Structure Type


### Modeling Methods

- Finite element A-formulation (magnetic vector potential) for Maxwell's equations
- Continuum mechanics plasticity analogy using yield functions and the principle of maximum dissipation
- Flow rule and Karush-Kuhn-Tucker (KKT) complementary conditions formulation
- Coulomb-friction-inspired numerical regularization algorithm for non-smooth constitutive relations
- Penalty function method converted to an ordinary differential equation with an auxiliary variable for transport current constraints
- Mixed-order spatial discretization (second-order Lagrangian elements for A, constant discontinuous elements for J)
- Newton-Raphson nonlinear iterative solver

### Performance Metrics

- Coefficient of determination (R^2) comparing numerical results against analytical solutions
- Computation time (runtime in seconds) compared to T-A and H formulations
- Model convergence and absence of spurious numerical oscillations in large gradient zones
- Agreement of current density distributions, magnetic field profiles, losses, and magnetization loops against benchmark and power-law solutions

### Future Work

- Further development and improvement of the numerical implementation for transport current constraint conditions in the critical state model to mitigate stiffness matrix complications and improve efficiency.
