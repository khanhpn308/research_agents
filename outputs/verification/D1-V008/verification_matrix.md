# Verification Matrix

**Verification ID:** D1-V008
**Paper count:** 1
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — Analytical Solution for Bending Deformation of Steel–Concrete Composite Beams Considering Nonlinear Interfacial Slip

- **paper_id:** `53d328abaa`
- **year:** 2024
- **doi:** 10.1061/JSENDH.STENG-13096
- **source_type:** verification
- **verification_id:** D1-V008
- **screening_status:** included
- **screening_reason:** Named high-threat target from C04. Full text confirms nonlinear interfacial-slip analytical model, experimental comparison, FE comparison, and explicit applicability limits; must be included in final P1 falsification.

### Robot / Structure Type


### Stiffness Mechanism

- headed-stud shear connectors
- partial shear connection

### Modeling Methods

- Principle of minimum potential energy
- Variational principle (first-order variation of total potential energy)
- Undetermined coefficient method using Fourier trigonometric series
- Euler-Bernoulli beam theory
- Energy-based nonlinear shear load-slip interface model
- Nonlinear 3D finite element modeling in ANSYS (SHELL181 for steel beam, SOLID65 for concrete slab, COMBIN39 for shear studs)

### Performance Metrics

- Percentage difference between predicted (analytical and numerical) deflections and experimental deflections (3% for analytical, 5% for FE model)
- Absolute difference between predicted interfacial slip and experimental measurements (maximum difference <= 0.02 mm under lower load)
- Percentage discrepancy between predicted and experimental cross-sectional bending strains (< 8%)
- Relative increase in maximum end slip between nonlinear and linear interface slip models (40% increase)
- Deflection increase caused by shear deformation at low span-to-depth ratios (up to 20% increase at L/H = 5)
