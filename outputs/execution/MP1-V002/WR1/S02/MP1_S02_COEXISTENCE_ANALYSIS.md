# WR1-S02 coexistence analysis — planning derivation, no pilot result

**Question.** Can a sealed, positively confined NiTi wire specimen reach a safe state in which frictional interwire slip and stress-induced transformation occur at the same place and time, with separately supported measurements?

**Status.** PREPARATION_ONLY. GAP-05/K1, GAP-08/K3 and GAP-06/K9 remain OPEN. Equations below are planning approximations or standard mechanics inferences, not measured thresholds for this specimen. The S01 competitor remains an explicit-wire transformation-aware contact model with membrane pressure as external traction.

## Transformation condition

For a nearly straight wire i in a small-curvature section, the first planning approximation is

epsilon_i(x,y,t) ≈ epsilon_pre,i + epsilon_axial,i(t) + kappa(x,t) y_i(t).

Here epsilon_i is local axial strain; epsilon_pre,i is measured assembly prestrain; epsilon_axial,i is the common/load-induced axial contribution; kappa is measured local curvature; y_i is the signed distance of the material fiber from the current neutral axis in the bending plane. y_i changes if the bundle rearranges or ovalizes. Transformation onset is a **local constitutive condition**: the tensile or compressive wire strain/stress path reaches its same-lot, temperature- and history-dependent onset surface. A useful screening estimate for a tensile-side fiber is

kappa_tr,screen ≈ [epsilon_tr,start(T,history) - epsilon_pre,i - epsilon_axial,i] / y_i,

provided y_i is positive and the numerator is positive. This is not a safe-curvature prescription. At large curvature, finite strain, shifting neutral axis, wire slip and phase-dependent tangent response invalidate a constant-y estimate; actual local strain and temperature must be measured.

For ideal straight triangular packing of equal wires with diameter d, the center distance from section centroid is d/sqrt(3). If one vertex lies on the tensile side, an approximate extreme fiber distance is y_max ≈ d/sqrt(3)+d/2. The actual bend-plane orientation and deformed cross-section determine y_max. The proposed primary d = 0.5 mm is **ENGINEERING_STARTING_POINT**, not selected stock. W02's approximately 0.75% transformation-strain estimate is **VERIFIED_FROM_EXISTING_REPOSITORY_EVIDENCE AS A PLANNING BOUND**, not a universal onset for this NiTi lot. Combining those illustrative inputs at zero prestrain gives y_max about 0.54 mm and kappa_tr,screen about 0.014 mm^-1, both **ENGINEERING_STARTING_POINT DERIVATIONS**. Do not command this curvature until the selected wire's safe-strain/fatigue envelope and sleeve limits are known. An alternate smaller wire increases the required curvature at fixed threshold while reducing bending force; it is a tradeoff, not automatically safer.

## Slip condition and pressure boundary

For neighboring wire centers separated by signed bend-plane distance Delta y, no-slip compatibility creates an axial strain mismatch of order kappa Delta y. Over an active length L, free relative displacement scales as Delta u_free ~ kappa Delta y L, modified by end constraints and local transformation strain. The contact must transmit shear to prevent this mismatch. In a wire-level equilibrium description, dN_i/dx balances contact tangential line load q_t and any applied distributed load. Stick is feasible while the required tangential line load satisfies |q_req| <= mu q_n at each contact; slip begins where this bound is exceeded, with q_n the local compressive contact line load and mu the relevant measured friction coefficient. Pressure, packing, prestrain and curvature affect q_n, but **chamber pressure p is not q_n or an interwire normal force**.

The fluid acts on the inner membrane through the pressurized annulus. The outer restraint supplies the reaction; membrane deformation and contact topology transmit an uncertain traction to the wires. An unreinforced internally pressurized sleeve could expand outward rather than confine the bundle, so the cuff geometry and measured radial contraction under pressure are mandatory preflight observations. A pressure-induced reduction of slip is a candidate signature, not an assumed monotonic law because rearrangement and local contact loss are possible.

## Desired overlap and what would prove it

Define S_i as the time/space interval where corrected relative motion across a particular wire pair exceeds its calibrated control/noise envelope and cannot be attributed to clamp, common bundle or elastic strain. Define T_i as the interval where an independently calibrated transformation-sensitive signature is supported for a wire in the same region. The coexistence condition for this pilot is nonempty S_i intersection T_i within the same pressure-curvature-temperature state, with onset/duration uncertainty small enough that the intersection cannot be explained by clock offset or proxy lag. Repeat it under the confirmation cycles and document integrity.

A global moment-curvature loop cannot define S_i or T_i. End-tail relative motion alone can include differential elastic extension, and local strain crossing a published threshold alone does not establish phase transformation. The preferred S_i channel tracks registered material markers on neighboring wires through a verified pressure optical path, corrected with simultaneously tracked sleeve/bundle/clamp markers and local axial strain. The fallback tail channel must be independently validated against a visible local reference. The T_i support set combines same-lot single-wire cyclic stress-strain and thermal calibration at matched temperature/rate/history with specimen local strain, thermal response and a phase-sensitive proxy if one can be made nonintrusive. Friction-only, elastic NiTi, sleeve-only and fixture-only controls must fail to explain the signature. If only strain and a rough threshold are available, mark transformation INDETERMINATE. If direct phase measurement is unavailable, report **INDIRECT_SUPPORT**, never measured phase fraction.

## Thermal, rate and history condition

Transformation stress and phase kinetics depend on temperature and history; friction and membrane losses can also heat the specimen. Compare a slow condition with a faster one or a slow load with a dwell at matched pressure and curvature, using measured local rate rather than actuator command. Track wire-adjacent, membrane and ambient temperatures, cycle number and dwell duration. Correct for sensor thermal lag. If the thermal/rate uncertainty propagated through same-lot calibration is smaller than a predeclared future discrimination margin, and no unexplained rate/history trend remains, the later S05 model may use the ISOTHERMAL_H0b_ALLOWED branch within that declared domain. Otherwise route to THERMOMECHANICAL_H0b_REQUIRED; if temperature is unobservable, the branch is INDETERMINATE and the pilot cannot pass that gate.

## Limits and evidence

**VERIFIED REPOSITORY STATE:** W02 K1 says the overlap domain has not been physically demonstrated; K3 says global response is non-identifying; K9 leaves thermal/rate/history confounding open. Reedlunn et al. (2013 Part I, paper_id 00414aac4b, repository full-text PDF under data/papers/verification/MP1-V002) used synchronized DIC and thermal imaging on exposed cable tension specimens. That proves method precedent, not visibility or phase identification through this pressure cuff. The S01 observable register supplies candidate functions, not validated channels. All specimen dimensions, pressure, fatigue and sensor performance remain to be selected or measured.

**References/provenance:** outputs/execution/MP1-V002/W2/MP1_W02_K1_K9_RECONCILED_MATRIX.json (K1,K3,K9); MP1_W02_BLOCKING_GAP_REGISTER.json (GAP-05,06,08); outputs/execution/MP1-V002/WR1/S01/MP1_S01_H0B_MODEL_SPECIFICATION.md and MP1_S01_OBSERVABLE_SIGNATURE_REGISTER.json; data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf. AI assistance was used for design; no experimental result or external source was generated.
