# Verification Matrix

**Verification ID:** MP1-V001
**Paper count:** 11
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump

- **paper_id:** `de64029540`
- **year:** 2013
- **doi:** 10.1109/TMECH.2012.2211032
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- robotic pump

### Actuation

- wet shape memory alloy (SMA) actuation
- thermofluidic forced convection heating and cooling
- electrical Joule heating assistance

### Modeling Methods

- Energy bond graph modeling integrated with state-space representation coupling wet SMA actuators, mechanical lever kinematics, and pumping chambers
- One-dimensional dynamic heat transfer equations modeling forced convection and conduction among fluid, SMA wire, compliant tube, and ambient air
- Discretized multi-segment representation of the wet SMA actuators (20 segments per actuator)
- Differential hysteresis model for martensite fraction using a cumulative normal distribution function modulated by wire temperature
- Piecewise linear constitutive model capturing twinned martensite, detwinned martensite, and austenite elastic moduli and phase transformation stresses
- Lumped-parameter fluid dynamic state equations for piston chamber pressures accounting for volumetric capacitance, fluidic resistance, and check valves

### Performance Metrics

- Volumetric output-to-input ratio (Qout/Qin, dimensionless)
- Net fluid flow rate output (mL/min)
- Thermodynamic efficiency (theoretical maximum and practical, %)
- Heartbeat period / cycle time (s)
- Actuator stroke and piston displacement (m)

### Future Work

- Making the robotic pump system more compact in volume without impairing SMA contraction
- Removing the need for auxiliary electrical inputs by using fluid-only heating and mechanically timed valve mechanisms
- Characterizing and optimizing practical thermodynamic efficiency by minimizing thermal and mechanical losses
- Powering continuous, silent operation using high-energy-density chemical energy sources instead of electrical heating

## V02 — A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots

- **paper_id:** `182d854610`
- **year:** 2021
- **doi:** 10.1109/LRA.2021.3097255
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- Wearable robot (wearable limb support device for arm and leg assistance)

### Stiffness Mechanism

- Positive Pressure Jamming (PPJ) / granular jamming (Shape Memory Polymer granules compressed between an internal inflatable bladder and an external non-stretchable sleeve)
- Friction pad self-locking revolute joint (sandpaper friction pads compressed by pressurized granules/actuator to lock joint angles)

### Actuation

- Pneumatic actuation
- Positive pressure compressed air via miniature motor pumps

### Modeling Methods

- Euler-Bernoulli cantilever beam bending stiffness formulation: K = 3EI / L^3
- Ring-shaped cross-section area moment of inertia calculation: I = pi * (D^4 - d^4) / 64
- Empirical/analytical equivalent Young's modulus scaling model: E = C / (D^2 - d^2) based on average cross-sectional contact force Faverage = 4Ft / [pi * (D^2 - d^2)]
- Composite bending stiffness relation as a function of sleeve and bladder diameters: K = 3 * pi * C * (D^2 + d^2) / (64 * L^3)
- Jamming efficiency / stiffness-to-mass optimization model: K / mass = 3 * C * (D^2 + d^2) / [16 * L^4 * rho_0 * (D^2 - d^2)]
- Static torque balance formulation for the critical slip force of the self-locking joint: Fc * (L + l/2) = P * S * mu * ds and piecewise two-stage stiffness representation

### Performance Metrics

- Cantilever bending stiffness (N/mm)
- Equivalent Young's modulus / bending elastic modulus (MPa)
- Resisting force (N)
- Force increment at specified deflection (N at 1 mm and 10 mm displacement)
- Critical slip force Fc (N) and joint torque limit (N*m)
- Jamming efficiency / stiffness-to-mass ratio (times baseline)
- Coefficient of static friction mu
- Linear regression determination coefficient R^2

### Future Work

- Fabricating positive pressure jamming structures in non-cylindrical pre-designed geometries, such as torus shapes
- Combining multiple shapes of jamming structures to form complex 3D deployable frames (e.g., tent frames)
- Conducting dynamic transition tests to quantify the switching times from soft to stiff and from stiff to soft states
- Investigating alternative bladder materials that reduce radial compliance and deformation under high positive pressure
- Developing more durable, wear-resistant friction materials to enhance self-locking joint longevity
- Incorporating internal fabric partitions inside the chamber to ensure a more uniform initial distribution of granules

## V03 — Shape Memory Alloy Capsule Micropump for Drug Delivery Applications

- **paper_id:** `55457a97c6`
- **year:** 2021
- **doi:** 10.3390/mi12050520
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type


### Stiffness Mechanism

- Variable phase stiffness of shape memory alloy (NiTi) wire transitioning between lower shear modulus martensite (5.65 GPa) and higher shear modulus austenite (18.3 GPa) phases upon Joule heating
- Antagonistic passive elastic restoration provided by a flexible silicone elastomer enclosure (Ecoflex 00-30) acting as an integrated return spring

### Actuation

- Shape memory alloy (NiTi wire) Joule heating / resistive heating
- Passive elastic restoration via flexible silicone polymer enclosure (Ecoflex 00-30) acting as an antagonistic spring

### Modeling Methods

- Analytical Brinson one-dimensional thermomechanical constitutive modeling relating detwinned martensite volume fraction to shear stress.
- Static two-state force-displacement spring formulation (An et al. 2012) incorporating torsional wire stress and outer diameter variations for austenite and martensite states.
- Linear elastic spring modeling of the silicone enclosure based on experimental force-displacement measurements.
- Equilibrium solution via MATLAB numerical curve intersection to identify peak deflections and delineate plastic failure boundaries across design parameters.

### Performance Metrics

- Maximum linear stroke (5.6 mm) and deflection ratio (27%)
- Actuation speed (up to 11 mm/s)
- Maximum static head pressure (14 kPa / 105 mmHg at 7.1 W; 6.5 kPa / 48 mmHg in limit-switch mode)
- Maximum volume flow rate (2524 µL/min at 7.1 W under free convection)
- Maximum flow rate per watt (364.52 µL/(W·min) at 4.2 W)
- Maximum flow rate per pump volume (5.94 µL/(min·mm³))
- Total pump volume (424.7 µL / 424.7 mm³)

## V04 — Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming

- **paper_id:** `240fbf6022`
- **year:** 2022
- **doi:** 10.3390/app12073582
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- Fiber-reinforced soft pneumatic actuator, soft robotic gripper, and wearable exoskeleton (detachable soft glove and detachable elbow sleeve)

### Stiffness Mechanism

- wire jamming
- fiber jamming

### Actuation

- Pneumatic actuation (positive air pressure for fiber-reinforced soft bending actuator)
- Vacuum pressure (negative air pressure for wire jamming structure)

### Modeling Methods

- Euler-Bernoulli cantilever beam theoretical modeling for unjammed (individual independent beams) and jammed (unified solid composite beam) wire states.
- Theoretical modeling of the fiber-reinforced soft actuator bending behavior to determine actuator geometric parameters.
- Finite element (FE) simulation of the fiber-reinforced soft actuator bending state under positive air pressure.

### Performance Metrics

- Bending stiffness (N/mm, defined as the ratio of applied force to deflection)
- Bending stiffness increase ratio under vacuum (up to ~7x increase at -85 kPa vs. 0 kPa)
- Torsional torque (N*mm) and torsional stiffness range (ratio between jammed and unjammed states, 1.88 to 2.02)
- Free bending angle (degrees) as a function of positive air pressure (kPa)
- Maximum payload mass of the soft robotic gripper (g)
- Maximum lifting weight capacity of the detachable soft glove (g / kg)
- Initial (unjammed) stiffness and stiffness variation range

### Future Work

- Further research into 3D printing materials and advanced printing devices suitable for soft robotics.
- Exploring application prospects of stiffness-tunable soft actuators in medical devices, biomimetic robots, and immersive haptic feedback for VR/AR.
- Adding or replacing specialized sensing and driving units onto the modular soft gloves for diverse working tasks.

## V05 — Soft actuator with switchable stiffness using a micropump-activated jamming system

- **paper_id:** `bbe88a0c04`
- **year:** 2022
- **doi:** 10.1016/j.sna.2022.113449
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- Pneu-Nets soft actuator

### Stiffness Mechanism

- granular jamming
- particle jamming

### Actuation

- electro-conjugate fluid (ECF) micropump
- micro hydraulic actuation

### Performance Metrics

- Maximum output pressure: ±55 kPa at 2.5 kV
- Maximum flow rate: 140 mm³/s at 2.5 kV
- Stiffness increase factor: 5.5-fold (bending force increased from 0.134 N to 0.743 N at 3 mm deflection)
- Maximum bending angle: 16° at +50 kPa (2.45 kV)
- Maximum vertical tip displacement: 7 mm at +50 kPa
- Load-to-weight ratio: 5.2x (130 g payload supported by a 25 g actuator)
- Bidirectional asymmetry: 11% difference in static pressure and 3% difference in flow rate between flow directions

### Future Work

- Improving the bonding technique for the micropump assembly to eliminate asymmetric channel expansion and achieve identical performance in both flow directions.
- Fabricating the soft actuator from softer elastomeric materials (such as Ecoflex rubbers) to achieve larger bending angles and displacements.

## V06 — Variable-Stiffness and Deformable Link Using Shape-Memory Material and Jamming Transition Phenomenon

- **paper_id:** `2cd907e77a`
- **year:** 2022
- **doi:** 10.20965/jrm.2022.p0466
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- variable-stiffness and deformable link

### Stiffness Mechanism

- shape-memory polymer (SMP) phase transition
- shape-memory alloy (SMA) phase transformation
- granular jamming transition phenomenon

### Actuation

- Electrical Joule heating (PWM-controlled AC for SMP, direct AC for SMA)
- Pneumatic vacuum / air evacuation (below -90 kPa) and air injection
- Manual external deformation (applied external load)

### Modeling Methods

- Euler-Bernoulli linear beam bending / cantilever deflection model: P/delta = 3*n*E*I / L^3
- Linear regression approximation of force versus displacement curves below 20 N force to calculate bending stiffness (gradient)

### Performance Metrics

- Bending stiffness (N/mm)
- Stiffness variation ratio (up to ~33-fold change)
- Tip deflection over time under 2 kg load (mm)
- Shape recovery duration (s / min) and relative recovery speed ratio (0.24x)
- Residual tip displacement after recovery (mm)
- Hysteresis and reaction force loss across 10 reciprocating cycles (N)
- Self-weight retention capability in horizontal unjammed cantilever state

### Future Work

- Optimize internal structures according to shape-memory material properties, including forming SMA wires into complex 3D shapes such as coils.
- Optimize selection and formulation of SMP and SMA materials to tailor transition temperatures, hysteresis, and recovery strains to application requirements.
- Optimize granular filler material and incorporate internal membrane partitions to prevent particle redistribution and ensure uniform distribution.
- Implement closed-loop temperature control for SMA wires similar to the SMP control system.
- Develop autonomous actuation/deformation mechanisms to eliminate reliance on manual shaping.
- Integrate the deformable link onto a robotic arm and evaluate performance in realistic manipulation tasks.
- Quantitatively evaluate gripping capacity through load-cell pull-off force testing.

## V07 — Effect of R-phase on shape recovery speed of Ti-Ni shape memory alloy wire for variable-stiffness mechanism using jamming transition phenomenon

- **paper_id:** `7ce492505d`
- **year:** 2024
- **doi:** 10.1299/mej.24-00130
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- variable-stiffness and deformable link (variable-stiffness mechanism for attachment to a robot arm for pick-and-place motion)

### Stiffness Mechanism

- Jamming transition phenomenon (granular jamming using coarse coffee grounds)
- Shape memory effect / phase transformation of Ti-Ni shape memory alloy (SMA) wire

### Actuation

- Electrical heating (Joule heating / energization at a constant voltage of 0.5 V) for shape memory alloy recovery
- Pneumatic evacuation (vacuum / air removal) for jamming transition and air injection for unjamming

### Modeling Methods

- Empirical linear regression / approximation of the displacement-time curve up to 50 mm deformation to compute the recovery velocity (slope)
- Direct calculation of stress by dividing measured tensile force by wire cross-sectional area
- Extraction of tangential stiffness (EA2) as the linear slope of the recovery plateau region from tensile stress-strain curves

### Performance Metrics

- Shape recovery velocity (mm/s)
- Displacement (mm) as a function of energization time (s)
- Stress at the start of shape recovery σA (MPa)
- Tangential stiffness during shape recovery EA2 (MPa)
- Plastic strain / residual strain (%) after deformation and training cycles
- Device recovery time required to reach 10 mm short of initial shape (s)
- Shape recovery extent / height achieved by the variable-stiffness device (mm)

### Future Work

- Establishing a clear target recovery velocity for the variable-stiffness device in practical pick-and-place applications
- Investigating the influence of different training conditions on the shape-recovery characteristics and performance of Ti-Ni SMA elements to achieve complete shape recovery

## V08 — Motion Evaluation of Variable-Stiffness Link Based on Shape-Memory Alloy and Jamming Transition Phenomenon

- **paper_id:** `99fe24da8b`
- **year:** 2024
- **doi:** 10.20965/jrm.2024.p0181
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- variable-stiffness link attached to a robot arm (also operated as a jamming gripper)

### Stiffness Mechanism

- shape-memory alloy (SMA) phase transformation
- granular jamming transition phenomenon (coarse coffee grounds in a silicone rubber membrane under vacuum)

### Actuation

- Joule heating / thermal actuation of shape-memory alloy wires via direct AC voltage (3 VAC)
- Pneumatic / vacuum actuation (air evacuation to below -90 kPa via vacuum pump) to induce granular jamming
- External mechanical contact / external force applied by pushing against a rigid block and inserting into 3D-printed molds using a robot arm
- Electric motor actuation of a 4-DOF robot arm (Dobot Magician) for link positioning and transfer

### Performance Metrics

- Standard deviation of placement position coordinates (mm)
- Difference between placed position and reference position (mm, average +/- SD)
- Pick-and-place success rate across 11 trials (%)
- Contact area length between link and object (mm, average +/- SD)
- Straight tip length of link (mm, average +/- SD)

### Future Work

- Evaluating the variable-stiffness link using complex real-world benchmark objects, such as items from the YCB Objects and Model Set.
- Fabricating and testing a longer link to prevent objects from slipping off when deflection occurs under weight.
- Verifying whether the fixed cross-sectional shape remains stable and fixed after repeated pick-and-place cycles.
- Developing mold-free deformation techniques that eliminate the need for silicone spray lubrication (e.g., using a secondary robot arm to apply external deforming forces).
- Optimizing initial and fixed link shapes to minimize structural deflection under load and enhance payload capacity.

## V09 — Piston-like particle jamming for enhanced stiffness adjustment of soft robotic arm

- **paper_id:** `c6a31066f8`
- **year:** 2024
- **doi:** 10.1108/IR-11-2023-0305
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- soft robotic arm

### Stiffness Mechanism

- particle jamming
- piston-like particle jamming

### Actuation

- tendon-driven (differential super-elastic NiTi wires driven by digital servos via gear and rack mechanisms)
- motor and ball screw mechanism (driving a piston-like jamming rod)

### Modeling Methods

- Constant curvature kinematic geometry model mapping tendon length differentials to arm bending angles (theta, c) and accounting for piston stroke inflexibility DL
- Particle packing state transition formulation modeling conservation of macroscopic particle volume from random loose packing (RLP) to hexagonal close packing (HCP) with radial chamber expansion
- Geometric chamber elongation constraint formulation determining the maximum permissible initial filling ratio omega
- Euler-Bernoulli beam mechanics model incorporating bilinear elastic modulus formulation with equal tension-compression division (alpha = pi) to derive maximum proximal bending torque and critical collapsing load threshold M_0

### Performance Metrics

- Vertical tip displacement DY (mm)
- General bending stiffness K = Mg / DY (N/mm)
- Stiffening ratio gamma = DY_0 / DY
- Collapsing load threshold M_0 (kg)
- Axial jamming force F (N)

### Future Work

- Combining the variable-stiffness arm with other devices, such as soft end-effectors, to conduct deeper research on grasping or manipulating

## V10 — A variable stiffness omnidirectional chain based on positive-pressure fiber jamming

- **paper_id:** `3aa8790db0`
- **year:** 2026
- **doi:** 10.5194/ms-17-481-2026
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- variable stiffness omnidirectional chain (VSOC)

### Stiffness Mechanism

- positive-pressure fiber jamming
- fiber jamming

### Actuation

- positive-pressure pneumatic actuation
- internal inflatable bladder

### Modeling Methods

- Euler-Bernoulli beam theory applied to fiber jamming rods under bending
- Three-state mechanical framework defining jamming, transition, and slipping states
- Parabolic shear stress distribution analysis and conjugate shear stress theorem to formulate state transition criteria
- Work-energy balance under pure bending equating external moment work to elastic strain energy and Coulomb frictional sliding dissipation
- Derivation of pressure-dependent equivalent area moments of inertia (IJ and IS) adapted to compacted geometry under shaft and lateral bending modes
- Phenomenological quadratic interpolation of slipped cross-sectional area ratio across the transition regime (QJ <= Q <= QS)
- Adaptive piecewise linear regression algorithm using R^2 maximization to autonomously identify critical loads (FJ, FS) and stiffnesses (KH, KL) from experimental load-deflection data

### Performance Metrics

- Critical shear force for slip initiation QJ (N) and critical load FJ (N)
- Critical shear force for full slipping QS (N) and critical load FS (N)
- High-stiffness stage equivalent moment of inertia IJ (mm^4) and stiffness KH (N/mm)
- Low-stiffness / slipping state equivalent moment of inertia IS (mm^4) and stiffness KL (N/mm)
- Effective fiber elastic modulus E (GPa) and 95% confidence interval
- Effective inter-fiber static friction coefficient mu and 95% confidence interval
- Coefficient of determination (R^2) for linear fits and parameter regressions
- Relative error between theoretical and experimentally fitted critical force-pressure coefficients (%)
- Load standard deviation band (N) across repeated tests

### Future Work

- Optimizing the dynamic response of the variable stiffness structure.
- Refining the inter-fiber friction model to accommodate varying slip velocities.
- Exploring integrated sensing for closed-loop stiffness control.
- Conducting direct, independent material testing to cross-validate the fiber elastic modulus E.
- Developing more refined theoretical formulations and detailed experiments to characterize stochastic stick-slip behavior, non-uniform pressure transmission, and local fiber compaction.

## V11 — Pick-and-Place Motion by Two-Robot-Arm System Equipped with Variable-Stiffness and Deformable Link Using Shape-Memory Alloy and Jamming Transition Phenomenon

- **paper_id:** `d3b3b6963f`
- **year:** 2026
- **doi:** https://doi.org/10.20965/jrm.2026.p0646
- **source_type:** verification
- **verification_id:** MP1-V001
- **screening_status:** included
- **screening_reason:** High-relevance full-text prior art for MP1-V001 architecture and novelty falsification.

### Robot / Structure Type

- two-robot-arm system equipped with variable-stiffness and deformable link

### Stiffness Mechanism

- shape-memory alloy (Ni-Ti SMA wires; phase transformation from compliant at room temperature to rigid upon resistive heating above austenite start temperature As = 60 °C)
- jamming transition phenomenon / granular jamming (evacuation of air to below -90 kPa around coarse coffee grounds within a silicone rubber membrane)

### Actuation

- Joule heating / electrical heating of shape-memory alloy wires via slidac transformer (3 VAC)
- Pneumatic / vacuum pressure (exhausting air to below -90 kPa using a vacuum pump for jamming; injecting air to unjam)
- Robotic arm / automated stage external actuation (pushing and pressing using Dobot Magician robot arms or linear automatic stages)

### Modeling Methods

- Static friction slipping threshold formulation: theta = tan^-1(mu), calculating the critical inclination angle at which an object begins to slip on the inclined link surface based on the static friction coefficient mu between silicone rubber and payload materials.
- Geometric calculation of link tip inclination angle from measured post-experiment dimensions (width, height, length) to evaluate structural stability against the critical slip angle.

### Performance Metrics

- Mold exchange duration: 85 +- 8 s (Procedure 0), 135 +- 4 s (Procedure 1), 4.7 +- 0.1 s (Procedure 2).
- Payload capacity success rate: 100% across all payloads (up to 990 g / 651% link weight) for Procedures 1 and 2, compared to 0% at 990 g for Procedure 0 without motion (ii).
- Durability cycle count: > 500 cycles for Procedures 1 and 2 with motion (ii'), 372 cycles for Procedures 1 and 2 without motion (ii'), 2 cycles for Procedure 0 with motion (ii), and 0 cycles for Procedure 0 without motion (ii).
- Deformation pressing force: 20.9 +- 0.5 N (Procedure 1, triangle, full), 20.1 +- 0.6 N (Procedure 1, circle, full), 18.6 +- 0.3 N (Procedure 2, triangle, full), 8.1 +- 0.5 N (Procedure 2, triangle, half), 17.3 +- 0.3 N (Procedure 2, circle, full), 6.8 +- 0.3 N (Procedure 2, circle, half).
- Placement position standard deviation: lower standard deviations along X- and Y-axes when molded (e.g., Object 1 X/Y standard deviation reduced with motion (ii') and full distance).
- Contact area length: measured in mm across procedures, molds, and movement distances (e.g., higher for full distance than half distance or no mold).

### Future Work

- Using the variable-stiffness link to wrap around and grip objects directly during pick-and-place motions rather than hanging or hooking objects.
- Utilizing pre-bent SMA wires to achieve an initial bent configuration without needing an external inclined block for bending deformation.
- Preparing molds with more than two distinct shapes on the rotatable fixture to accommodate a wider variety of objects.
- Attaching a multi-finger robot hand to the secondary robot arm to perform repeated pressing from multiple directions to form arbitrary link geometries.
