# Verification Matrix

**Verification ID:** D1-V003
**Paper count:** 9
**Purpose:** Independent adversarial literature verification of an existing research direction. Verification papers must be used to challenge, narrow, pivot, or reject the direction rather than to confirm it by default.

## Verification Papers

## V01 — Design Characteristics of Continuum Robots Based on TSA Variable Stiffness Method

- **paper_id:** `6723402e32`
- **year:** 2026
- **doi:** 10.3390/act15030154
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Forward citation of Zhang et al. 2025 continuum model for D1-V003 verification audit

### Robot / Structure Type

- bionic spine-like continuum robot

### Stiffness Mechanism

- force-locking
- Twisted Multi-String Actuators (TSA)
- inter-substrate friction modulation via spherical contact interfaces

### Actuation

- Twisted Multi-String Actuator (TSA)
- Cable-driven (tendon-driven)

### Modeling Methods

- Kinematic/geometric modeling of twisted string contraction (cylindrical expansion and helix angle formulation modified for radius expansion).
- Energy balance and virtual work modeling of TSA contraction relating motor input torque to cable elastic strain energy.
- Cantilever beam structural mechanics modeling with a discrete matrix correction factor (Krobot = 2 * Ebase * Ibase / l^3).
- Tribological force-locking formulation deriving inter-substrate spherical contact friction torque from normal forces induced by TSA and drive cables.
- Two-state mechanical equilibrium modeling distinguishing between pure static friction (relative rest) and post-slip partial inter-substrate rotation.
- Geometric aperture constraint analysis for maximum inter-substrate bending and rotational limit angles.

### Performance Metrics

- Omnidirectional bending angle (degrees)
- Individual substrate joint limit angle (degrees)
- Axial cable contraction length (mm)
- End-effector radial displacement (mm)
- Average stiffness under load (N/m) and percentage stiffness increase (%)
- Maximum tolerable load / failure load (N) and percentage load capacity increase (%)
- Axial cable tension (N)

### Future Work

- Develop fully automated, dynamic retraction mechanisms to enable real-time and continuous variable stiffness modulation.
- Integrate embedded pose and tension sensors for closed-loop stiffness control.
- Explore alternative TSA cable routing and deployment topologies to expand robot workspace and bending curvature range.
- Incorporate higher-torque actuation units to further expand load-bearing capacity.
- Investigate robot dynamic interaction performance and stability during operational tasks.

## V02 — Modeling, Control, and Stiﬀness Regulation of Layer Jamming-Based Continuum Robots

- **paper_id:** `1f05cf83bc`
- **year:** 2026
- **doi:** 10.1109/TCST.2026.3690756
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Direct full-text adversarial evidence. The paper develops dynamic modeling and stiffness regulation for layer-jamming continuum robots and is required to determine whether the surviving D1-V003 validity/breakdown research gap remains open.

### Robot / Structure Type

- continuum robot

### Stiffness Mechanism

- layer jamming (LJ)

### Actuation

- tendon-driven actuation
- vacuum pressure (negative pressure)

### Modeling Methods

- port-Hamiltonian formulation
- energy-based modeling
- rigid-link approximation
- LuGre friction model
- piecewise constant curvature (PCC) assumption
- potential energy-shaping passivity-based control (PBC) with damping injection

### Performance Metrics

- Steady-state configuration error metrics: root mean square (RMS) error and mean absolute error (MAE) in degrees over steady-state window IB.
- Transient settling time / convergence duration (s).
- Shape-locking displacement drift (mm) after releasing tendon tension.
- Transverse stiffness KT (fext / δx in N/m) and coefficient of determination R2 for stiffness model fitting.
- Stiffness contribution percentages r1 (from gain γ) and r2 (from elastic coefficient α2).

### Future Work

- Investigating different jamming layer configurations to demonstrate framework generality and scalability.
- Extending the control formulation from setpoint regulation to trajectory tracking with guaranteed stability.
- Integrating direct task-to-actuator kinematic inversion to address underactuation challenges in continuum robots.
- Extending the framework to other actuation mechanisms and distributed-parameter models such as dynamic Cosserat formulations to account for length-scaling and multisection structures beyond PCC limits.
- Exploring advanced dynamic learning methods (such as Koopman operator, kernel methods, or Gaussian process regression) to approximate nonlinear functions α2(uP) and φ(uP).

## V03 — A Novel Model for Layer Jamming-based Continuum Robots

- **paper_id:** `b573b2ab6b`
- **year:** 2024
- **doi:** 10.1109/ICRA57147.2024.10610912
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- continuum robot

### Stiffness Mechanism

- layer jamming

### Actuation

- tendon-driven
- vacuum pressure

### Modeling Methods

- Port-Hamiltonian framework
- Energy-based Hamiltonian mechanics with rigid link approximation
- LuGre dynamic friction model with virtual bristle deflection
- LaSalle's invariance principle for local asymptotic stability analysis
- Euler-Lagrange reformulation and Jacobian linearization for open-loop stiffness derivation

### Performance Metrics

- End-effector transverse stiffness KT (in N/mm)
- Coefficient of determination (R^2_s) for stiffness linearity with pressure
- Positional deviation / displacement during shape locking (in mm)

### Future Work

- Synthesizing model-based feedback controllers based on the proposed control-oriented port-Hamiltonian framework.
- Revisiting and refining Assumption 3 concerning the relationship between negative pressure and lumped normal force to improve stiffness prediction accuracy.

## V04 — A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics

- **paper_id:** `f5f31ef249`
- **year:** 2024
- **doi:** 10.3390/act13020064
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- soft grippers and fingers, continuum robots, wearable robots (exoskeletons, haptic gloves, and soft linear brakes), robot arms (variable stiffness links and joints), unmanned aerial vehicle (UAV) landing gear, and underwater robots (robot fish)

### Stiffness Mechanism

- laminar jamming (layer jamming / multi-layer beam)
- laminar jamming wrapped by shape memory alloy (SMA)
- electrostatic force / electrostatic layer jamming / electro-bonded lamination
- vacuum pressure laminar jamming
- discrete laminar jamming (DLJ)
- mesh sheath laminar jamming
- mechanical interference (teeth-clutching / form closure / smart form closure actuators)
- laminar jamming with heating blankets
- sliding-layer laminates (SLL)
- trapezoidal pin mechanism (discrete laminar jamming combined with mechanical interference)
- vacuum pressure combined with mechanical interference (multi-material teeth-clutching layer jamming)
- hybrid jamming (laminar jamming combined with particle jamming)
- hybrid variable stiffness link (airtight chamber, shape morphing, and laminar jamming)

### Actuation

- vacuum pump (vacuum / negative pressure)
- electric power / thermal conditions (shape memory alloy wires)
- electric power / high-voltage source (electrostatic force / electro-bonded lamination)
- mechanical / pressure clamps (bolts, rubber bands, piezoelectric actuators)
- mechanical motion / cable actuation (mesh sheath)
- heat source / thermal conditions / temperature controller (electric heating blankets)
- linear actuator / solenoid / linear motorized stage (sliding-layer laminates)
- air pressure / pneumatic cylinder (trapezoidal pin mechanism)
- positive pressure pneumatic actuators (pneu-net actuators, McKibben artificial muscles, air bladders)

### Modeling Methods

- Coulomb friction analytical modeling
- Energy method (conservation of external work, elastic bending strain energy, and inter-layer frictional work)
- Two-dimensional (2D) finite element analysis (FEA)
- Three-dimensional (3D) finite element analysis (FEA)
- Analytical beam models for arbitrary numbers of layers
- Pseudo-rigid-body modeling (for parallel guided beam compliant links)
- Model-based design frameworks and computational design scripts (e.g. Matlab-based design tools)

### Performance Metrics

- Stiffness variation (stiffness ratio, maximum stiffness / minimum stiffness)
- Stiffness range (N/mm)
- Speed of stiffening (actuation time, ms or s)
- Speed of destiffening (release/destiffening time, ms or s)
- Transition time constant (s)
- Yield force threshold / pre-slip to full-slip transition force (N)
- Torsional stiffness and critical vertical buckling load
- Pinch grasp force and grasp stability for various object sizes
- Impact peak force reduction and acceleration attenuation during collision
- Coefficient of determination (R^2) between model and experimental data

### Future Work

- Quantitatively measuring and reporting stiffening and destiffening velocities across all lock/unlock mechanisms
- Developing fast lock/unlock mechanisms, such as discrete laminar jamming with piezoelectric actuators, to enable active collision mitigation
- Combining fundamental laminar jamming mechanisms, such as vacuum pressure with mechanical interference, to boost stiffness ratio and maintain compactness
- Implementing electrostatic layer jamming in robotic arm links to exploit millisecond-scale actuation (<5 ms) and release (<15 ms) speeds
- Hybridizing laminar jamming with other variable stiffness methods such as shape-morphing air bladders and pneumatic chambers
- Developing closed-loop control algorithms for variable stiffness links and joints to regulate impedance, directional stiffness, and impact attenuation
- Extending design methodologies and computational design frameworks beyond vacuum-actuated jamming to other laminar jamming mechanisms
- Improving reporting of manufacturing techniques, material wear, failure modes, and long-term repeatability degradation

## V05 — A Novel Continuum Robot With Stiffness Variation Capability Using Layer Jamming: Design, Modeling, and Validation

- **paper_id:** `6583ae5919`
- **year:** 2022
- **doi:** 10.1109/ACCESS.2022.3228775
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- continuum robot

### Stiffness Mechanism

- layer jamming
- support spine with ball joints and helical compression springs

### Actuation

- tendon-driven actuation
- cable-driven actuation (servo motors XM430-W350 with tailored aluminium spools and 1.2 mm stainless steel wire ropes)

### Modeling Methods

- Euler-Bernoulli beam theory
- Maxwell-Mohr method (used for straight beam under transverse load, curved beam under transverse load, and curved beam under axial load)
- Integral method with fixed-fixed boundary conditions (used for straight beam buckling analysis under axial load)

### Performance Metrics

- Resisting force (N)
- Average transverse stiffness ST (N/m)
- Average axial stiffness SAS and SAC (N/m)
- Stiffness variation ratio (maximum stiffness / minimum stiffness)
- Sheath stroke / allowable length change range Δl (mm)
- Payload and gripping capacity (grams / kilograms lifted or restrained)

### Future Work

- Improvement of the stiffness model to enable quantitative numerical analysis of variable stiffness capability.
- Analytical or numerical formulation to calculate the effective flexural rigidity (D) of the robot.
- Workspace analysis of the continuum robot.
- Real-time position and stiffness control algorithms.

## V06 — An Underactuated Variable Stiffness Continuum Robot With Multi-Layer Jamming Spherical Joints

- **paper_id:** `ac542457be`
- **year:** 2026
- **doi:** 10.1109/TASE.2026.3673298
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- underactuated variable stiffness continuum robot

### Stiffness Mechanism

- multi-layer jamming spherical joint (MLJSJ)
- layer jamming
- positive-pressure variable stiffness
- frictional locking between interleaved resin layers

### Actuation

- Positive-pressure pneumatic actuation (segmented spherical Dragon Skin 30 airbag regulated via electro-pneumatic proportional valves)
- Rod-driven actuation (four circumferentially arranged Nitinol rods driven by stepper motors and linear lead screws; one base lead-screw slide)

### Modeling Methods

- Interfacial friction locking torque formulation based on Coulomb friction integrated over spherical micro-elements
- Structural stiffness prediction derived via the principle of virtual work under small-deformation assumptions
- Piecewise constant curvature (PCC) forward kinematics mapping actuator rod lengths to configuration space (bending and deflection angles) and Cartesian task space
- Energy method formulation to quantify dissipated energy and equivalent damping ratio (ζeq) from cyclic hysteresis loops
- MATLAB numerical workspace simulation establishing an ellipsoidal reachable boundary (870 mm × 870 mm × 716 mm)

### Performance Metrics

- Maximum structural stiffness (1403.03 N/m at 300 kPa)
- Minimum structural stiffness (39.14 N/m at 12.5 kPa)
- Stiffness modulation ratio (35.85)
- Individual stiffness switching duration (0.07 s to 0.43 s)
- Cumulative pneumatic switching latency (approx. 3.44 s for four segments)
- Maximum single-segment payload capacity (2 kg)
- Manipulation target payload (50 g grasped using a 48.3 g soft gripper)
- Average and maximum positioning errors (single segment: 1.38 mm / 3.24 mm; four segments: 15.1 mm / 28 mm)
- Maximum safe operational pressure limit (300 kPa)
- Stiffness degradation rate under cyclic wear (3.6% after 1000 cycles)
- Equivalent damping ratio range (0.05 down to 0.015)

### Future Work

- Developing advanced hybrid control algorithms to bridge the gap toward continuous decoupling and enhance motion accuracy
- Addressing manufacturing precision for miniaturization in medical intervention applications
- Optimizing the strength-to-weight ratio to support structural upscaling for heavy-duty industrial inspections
- Incorporating identified damping and hysteresis parameters into dynamic modeling and controller tuning

## V07 — Decoupling Control of a Multi-Segment Hybrid-Actuated Soft Origami Continuum Robot Through Variable Stiffness

- **paper_id:** `8d3b7d72a6`
- **year:** 2026
- **doi:** 10.1109/TASE.2026.3700107
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- multi-segment hybrid-actuated soft origami continuum robot

### Stiffness Mechanism

- antagonistic actuation
- layer jamming
- hybrid variable stiffness

### Actuation

- hybrid actuation
- tendon-driven actuation
- pneumatic actuation

### Modeling Methods

- Stacked 2-layer Long Short-Term Memory (LSTM) recurrent neural network for inverse kinematic modeling with hysteresis compensation
- Iterative learning strategy augmenting limited random point datasets with actual trajectory execution and small step-size data
- Neural network-based search optimizer and coordinate transformation for multi-segment inverse kinematic solutions
- Analytical tendon compensation model based on constant-curvature neutral axis compression to eliminate second-segment tendon slacking
- Euler angle orientation mapping via LSTM network for 3D spatial orientation control

### Performance Metrics

- Trajectory tracking Euclidean distance error (absolute in mm and relative error percentage over robot length)
- Directional Cartesian error components (axial Z error vs. lateral X and Y errors in mm)
- Repeat positioning accuracy (Euclidean distance error in mm over 30 cycles)
- Bending orientation error (absolute deviation in degrees for roll, pitch, and yaw Euler angles)
- Axial extension ratio (percentage)
- Mechanical hysteresis displacement (mm) and settling time (seconds)
- Payload tracking error degradation factor relative to no-load conditions
- Neural network training convergence time (milliseconds for 100 epochs)

### Future Work

- Further integrate robot hardware components
- Miniaturize and reduce the physical dimensions of the robot to develop collaborative devices for humans
- Extend and apply the LSTM-based iterative training model to other continuum robotic structures

## V08 — Stiffness Change for Reconfiguration of Inflated Beam Robots

- **paper_id:** `dc9ad29f75`
- **year:** 2023
- **doi:** 
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- inflated beam robot (compliant continuum robot / everting growing vine robot)

### Stiffness Mechanism

- layer jamming
- positive pressure layer jamming

### Actuation

- pneumatic pressure-driven tip eversion (growth and internal pressurization)
- motorized spool-driven cables / tendons with stoppers

### Modeling Methods

- Finite element analysis (FEA) in ABAQUS 2021 simulating localized buckling, joint deformation, and strain distributions of two-segment tubes under transverse loading.
- Flexural modulus calculation using Euler-Bernoulli beam theory for three-point bending (E = L^3 * m / (4 * b * d^3)).

### Performance Metrics

- Flexural modulus / effective material stiffness (kPa)
- Transverse force required for a 10 mm beam tip deflection (N)
- Percentage increase in beam stiffness/force due to jamming (%)
- Segment angular displacement (degrees) for distal (θ1) and proximal (θ2) segments
- Targeted joint bending angle (e.g., 30 degrees per joint)

### Future Work

- Leveraging growth, variable stiffness, and combined continuum/discrete joint properties for robotic manipulation tasks.
- Incorporating embedded sensing to achieve closed-loop control.
- Investigating stiffness change across different length and diameter scales for applications such as minimally invasive surgery and reconfigurable structures.

## V09 — Stiffness-Tuneable Segment for Continuum Soft Robots with Vertebrae

- **paper_id:** `7366c065fa`
- **year:** 2022
- **doi:** 10.3390/machines10070581
- **source_type:** verification
- **verification_id:** D1-V003
- **screening_status:** included
- **screening_reason:** Included for D1-V003 adversarial full-text literature audit.

### Robot / Structure Type

- tuneable-stiffness soft continuum robot (TSCR)

### Stiffness Mechanism

- layer jamming

### Actuation

- pneumatic
- vacuum
- manual

### Modeling Methods

- Minimal analytical mechanics model for structural layer jamming of two-layer and extended N-layer flap systems
- Euler-Bernoulli beam theory applied under cantilevered conditions to evaluate layer structure deflection and effective shear stiffness
- Piecewise shear interface modeling divided into three distinct operational regimes: pre-slip regime, transition regime, and full-slip regime
- Lumped series and parallel spring stiffness combinations for flap-flap, flap-membrane, flap-nylon, and membrane tensile stiffness components
- Finite element analysis of TSCR mechanical behavior

### Performance Metrics

- Deflection force (N) and axial compression force (N)
- Stiffening coefficient gamma (ratio of average jammed force to average unjammed force)
- Central diameter ratio relative to initial 0-degree diameter
- Maximum achievable bending angle (degrees)
- Adjustable length range (mm)
- Coefficient of determination (R^2) between theoretical model predictions and experimental measurements

### Future Work

- Miniaturization of the TSCR for interventional medicine applications
- Application of the current TSCR design to exoskeleton rehabilitation robots
- Designing biomimetic flaps inspired by scaled organisms such as pangolins and fish to improve the trade-off between rigidity and flexibility
- Investigation of alternative flap weaving patterns and materials
- Quantifying the hysteresis effect of stiffening segment loading and unloading for TSCR controller development
