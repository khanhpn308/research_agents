# Candidate Research Directions

## Corpus Assessment

The corpus supports a focused MSc thesis in mechanics-led characterization rather than a broad new gripper architecture. The most recurrent limitations are: simplified quasi-static models, friction and hysteresis treated as constants or neglected, thermal switching latency, inadequate cyclic durability data, and 2D models that omit warping or three-dimensional contact. Evidence is strongest for jamming and thermally controlled variable stiffness. Claims of novelty remain unverified because all batch-level gaps require external database checking. Evidence independence is also uneven: paper IDs 26fb5818d6 and cb423f09c9 are duplicate catalog records for the same article, while several proposed gaps depend primarily on one paper.

## D1 — Modeling and Experimental Characterization of Friction, Warping, and Cyclic Stiffness Degradation in Vacuum Layer-Jamming Structures

**Vietnamese title:** Mô hình hóa và đặc trưng thực nghiệm ma sát, biến dạng vênh và suy giảm độ cứng theo chu kỳ trong kết cấu kẹt lớp chân không

### Research problem

Vacuum layer-jamming models can overpredict bending stiffness because they commonly assume constant interlayer friction and omit cross-sectional warping, while the corpus repeatedly identifies stiction, hysteresis, wear, and durability as unresolved limitations.

### Candidate gap

A reduced-order mechanics model linking vacuum pressure, interlayer slip, cross-sectional warping, and cycle-dependent friction to bending stiffness and hysteresis remains a candidate gap in the supplied corpus.

### Research question

For a spring-steel–silicone vacuum layer-jamming beam under cyclic transverse bending, how do vacuum pressure, layer count, and loading cycles affect effective friction, warping, flexural stiffness, and hysteresis, and does a slip-and-wear augmented beam model predict these responses more accurately than a constant-friction planar model?

**MSc feasibility:** high

The project can be restricted to one specimen family and uses vacuum regulation, force–displacement measurement, optical tracking, MATLAB fitting, and optional targeted FEA. It does not require specialized smart materials or high-pressure equipment.

**Novelty confidence:** unverified

### Supporting papers

- `dbe0e69179`
- `5bdf50c599`
- `269d15b830`
- `26fb5818d6`

### Main risks

- Reliable warping measurement may be difficult without careful optical setup.
- A long fatigue campaign could exceed the thesis schedule.
- Friction, leakage, and viscoelasticity may be difficult to identify separately.

## D2 — Predictive Mechanics and Experimental Validation of Positive-Pressure Layer Jamming Under Flexural Loading

**Vietnamese title:** Cơ học dự đoán và kiểm chứng thực nghiệm cơ cấu kẹt lớp áp suất dương dưới tải uốn

### Research problem

Positive-pressure layer jamming produces large stiffness and pull-out forces, but its pressure–stiffness behavior, pre-slip threshold, and reported high-pressure saturation are described mainly through empirical characterization.

### Candidate gap

A predictive model coupling membrane pressure, layer-pack friction, layer geometry, and constraining-frame compliance remains a candidate gap within the corpus.

### Research question

For a positive-pressure layer-jamming link under quasi-static flexure, how do inflation pressure, layer count, and frame flexural rigidity determine pre-slip stiffness and slip-onset load, and can a frictional composite-beam model predict the transition and saturation more accurately than an empirical pressure–stiffness fit?

**MSc feasibility:** high

The work is tightly scoped to a beam-like test article and standard bending measurements. It is feasible if suitable pressure-rated facilities are available; testing need not reach the maximum pressure reported in the source study.

**Novelty confidence:** unverified

### Supporting papers

- `26fb5818d6`
- `cb423f09c9`
- `2404868fbc`

### Main risks

- Pressures approaching those reported in the corpus require appropriate pressure-rated hardware and shielding.
- Fabrication repeatability and membrane leakage may obscure contact mechanics.
- The evidence base for this exact mechanism is concentrated in one unique article.

## D3 — Coupled Thermomechanical Modeling and Experimental Investigation of Forced Cooling in a Phase-Change Variable-Stiffness Soft Finger

**Vietnamese title:** Mô hình hóa nhiệt–cơ liên hợp và khảo sát thực nghiệm làm mát cưỡng bức trong ngón tay mềm biến đổi độ cứng bằng chuyển pha

### Research problem

Thermal variable-stiffness fingers offer large stiffness changes but repeatedly suffer slow and asymmetric cooling. Existing studies show that cooling architecture matters, yet pressure, flow, spatial temperature gradients, curvature, and recovered stiffness are not consistently connected through a validated dynamic model.

### Candidate gap

For one selected phase-change polymer architecture, the corpus suggests a candidate gap in predicting how forced-cooling flow and channel geometry control spatial temperature gradients, stiffness recovery, curvature drift, and cyclic hysteresis.

### Research question

For a conductive-polymer/elastomer variable-stiffness finger undergoing fixed cyclic bending, how do coolant flow rate and channel geometry affect the temperature field, stiffness-recovery time, and curvature drift relative to passive cooling, and can a lumped or reduced-order thermomechanical model predict these responses across repeated cycles?

**MSc feasibility:** medium

The modeling and benchtop tests are manageable, but fabrication, thermal instrumentation, electrical safety, and possible fluid leakage create more integration risk than the jamming topics.

**Novelty confidence:** unverified

### Supporting papers

- `6a92ae2d88`
- `96aec3bae3`
- `4bf6ae90e0`
- `7eddb5d92e`
- `db0ccb7d74`
- `f28f2201b8`

### Main risks

- Multi-material fabrication, sealing, and thermal cycling may cause delamination.
- Temperature-dependent modulus measurement can require careful mechanical testing.
- The topic can drift into cooling-system optimization without a sufficient mechanics contribution.

## D4 — Investigation of Membrane–Granulate Interaction and Surface-Friction Scaling in Vacuum Jamming Grippers

**Vietnamese title:** Nghiên cứu tương tác màng–hạt và quy luật tỷ lệ ma sát bề mặt trong kẹp kẹt hạt chân không

### Research problem

Thin membranes can transmit granular morphology to the outer surface and alter retention, but existing observations confound membrane thickness with material and do not establish a predictive relationship among membrane thickness, particle size, pressure, surface waviness, and frictional holding.

### Candidate gap

A dimensionless, experimentally validated scaling relationship based on membrane-thickness-to-particle-diameter ratio is a candidate gap within the supplied corpus.

### Research question

For a vacuum granular-jamming gripper made with one membrane material, how do membrane-thickness-to-particle-diameter ratio and vacuum pressure affect exterior waviness, tangential friction, and pull-off force relative to smooth unfilled and unjammed controls?

**MSc feasibility:** high

The project requires inexpensive granular media, vacuum equipment, force measurement, and surface imaging. It can begin with flat coupons before committing to a complete gripper.

**Novelty confidence:** unverified

### Supporting papers

- `f17bc7cbcc`
- `923285b103`
- `64a83322f3`

### Main risks

- Consistent fabrication of very thin membranes is difficult.
- Separating suction, geometric interlocking, and friction contributions requires careful controls.
- A purely empirical design chart would offer limited mechanics depth.

## D5 — Higher-Order Shear-Deformation Modeling and Experimental Validation of Ribbed Fluidic Prestressed Composite Actuators

**Vietnamese title:** Mô hình biến dạng cắt bậc cao và kiểm chứng thực nghiệm cơ cấu chấp hành composite lưu chất có ứng suất trước và gân tăng cứng

### Research problem

Classical laminated plate theory underpredicts the stiffness of fluidic prestressed composite actuators when thick internal and constraining ribs violate thin-plate and plane-stress assumptions.

### Candidate gap

The corpus suggests that incorporating transverse shear into a reduced-order chained-composite formulation could close the documented model–experiment discrepancy without requiring full 3D FEA.

### Research question

For ribbed fluidic prestressed composite actuators under fixed pressure and tip loading, does a first-order shear-deformation chained-composite model predict curvature, flexural rigidity, and tip force more accurately than the existing classical-laminate model as rib-height-to-wall-thickness ratio increases?

**MSc feasibility:** medium

The work has strong mechanical-engineering depth and limited hardware requirements, but its mathematical load and dependence on repeatable composite fabrication make schedule risk higher than the first two directions.

**Novelty confidence:** unverified

### Supporting papers

- `b62675b62a`

### Main risks

- The analytical derivation may become too extensive for the experimental payoff.
- Fabricating repeatable prestressed composite actuators can be difficult.
- The chosen geometry may require full 3D analysis, defeating the reduced-order objective.

## Provisional Recommendation

**D1**

D1 is the most defensible provisional topic because it is grounded in repeated limitations across several batches, poses a genuine mechanics question, provides measurable variables and a clear baseline model, and can be completed using MATLAB, modest FEA, prototype fabrication, vacuum regulation, optical tracking, and benchtop force–displacement testing. The provisional claim should be limited to developing and validating the specified model for the selected architecture; novelty must not be claimed until external searches are completed.

> This recommendation is provisional. Novelty has not yet been established by an external database search.
