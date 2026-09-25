# MP1-V002 Final Adjudication

- **Protocol outcome:** SURVIVES_TARGETED_CITATION_CHASE
- **Confidence:** high
- **Citation coverage closed:** True
- **Direct kill found:** False
- **MSc topic readiness:** READY_FOR_CROSS_DIRECTION_COMPARISON
- **Bundle SHA256:** 101211ee18b94343e4a7622b79c58014becdfe116867f408f2eeab54dce508a4

## Executive summary

The documented V002 citation chase reached its stop condition, and the 16-paper full-text matrix contains no direct kill of actively pressure-controlled NiTi-bundle bending. The direction survives only as a narrow, falsifiable mechanics question. This is a protocol-bounded decision, not proof of universal novelty. The interim audit’s earlier open-coverage status is superseded by citation_coverage.json.

## Surviving contribution

Experimental characterization and model discrimination for a NiTi wire bundle under bending with independently varied radial or transverse confinement pressure, resolving pressure-dependent normal contact, stick/partial-slip/full-slip transitions, transformation distribution, hysteresis, and tangent bending stiffness.

## What is not novel

- NiTi wire bundles, inter-wire friction, and NiTi transformation coupled with contact or hysteresis are established in the V002 full texts, including papers 40760daa02, 53200aa0c6, and e8462758c3.
- Wire/fiber jamming, positive-pressure jamming, and SMA combined with jamming were already closed as broad claims in MP1-V001.
- Passive helix-induced contact pressure, manufacturing preload, fixed radial pressure, and metallic-rope bending stick-slip mechanics are established by papers aaad9c248c, ccdc1bb980, and 9f4295be23.
- Failure of a constant-modulus substitution during NiTi transformation does not itself establish a need for a new constitutive law.

## What remains unestablished

- Whether independently varied confinement pressure creates a measurable NiTi-bundle bending response beyond ordinary calibrated effective parameters.
- Whether the feasible operating domain contains both inter-wire slip and stress-induced transformation.
- Whether established transformation-aware NiTi constitutive and contact formulations adequately predict pressure-dependent observations.
- Universal absence of closer prior work outside the V002 search cutoff and protocol.

## Final research question

Across a declared pressure and curvature domain, do independently varied radial or transverse confinement pressures produce NiTi-bundle stick-slip transitions, transformation distributions, hysteresis, and tangent bending stiffness that established calibrated elastic-wire and transformation-aware NiTi contact models cannot adequately predict?

## Scientific hypothesis

Where bending activates both slip and NiTi transformation, independently varied confinement pressure produces reproducible changes in local transformation and slip, and in bending hysteresis and tangent stiffness, that cannot be explained by ordinary calibrated effective parameters in an elastic-wire pressure/contact model. This hypothesis remains untested; an established transformation-aware NiTi contact model may explain the data without a new constitutive law.

## Model-discrimination plan

- **baseline_model:** Established elastic-wire/fiber pressure and Coulomb-contact bending framework, using the pressure-dependent slip regimes of Zhang and Yao 2026 and metallic-rope bending bounds of Barsi et al. 2025 as applicable baselines; calibrate effective parameters under a declared protocol.
- **transformation_aware_model:** Established superelastic NiTi constitutive formulation coupled to normal contact and Coulomb friction, using the Vahidi et al. framework as a precedent; impose measured pressure as a boundary input and independently characterize material and contact parameters.
- **comparison_domain:** The same specimen geometry, pressure levels, curvature cycles, temperature, loading rate, axial condition, and preconditioning history, including an elastic-only regime and a verified transformation-plus-slip regime.
- **falsification_logic:** Lock calibration rules before evaluating withheld pressure-curvature conditions. Compare moment-curvature loops, tangent stiffness, slip thresholds, and local transformation indicators. If no transformation-plus-slip domain is reached, or ordinary calibrated effective parameters explain the measured response adequately, reject the distinct MP1 mechanics claim. If the transformation-aware model also predicts the observations adequately, do not claim a new constitutive coupling.

## Experimental scope

### independent_variables

- Applied radial or transverse confinement pressure
- Bending curvature and loading-unloading path
- Transformation regime, set through controlled temperature or axial bias where feasible

### dependent_variables

- Bending moment-curvature response and tangent/effective stiffness
- Stick, partial-slip, and full-slip onset
- Hysteresis loop shape and energy
- Spatial transformation and strain distribution
- Inter-wire normal contact or a validated proxy

### control_variables

- Wire alloy and heat treatment
- Bundle geometry, wire count, and surface condition
- Specimen length and end constraints
- Temperature, loading rate, and cycle history
- Axial force or prestrain

### minimum_measurements

- Single-wire transformation response for independent constitutive calibration
- Pressure at the bundle and pressure-to-contact-force calibration or validated proxy
- Cyclic bending moment and curvature at multiple pressures
- Local strain or phase-sensitive measurements sufficient to verify transformation
- Inter-wire displacement or slip evidence sufficient to identify transition regimes
- Repeat measurements and calibration data kept separate from model evaluation data

## Topic-lock rationale

MP1 has a concrete falsifiable question and V002 coverage is closed, so it can advance to research design and comparison. D1/M1 remains preserved; V002 does not rank the directions or lock the MSc topic.

## Working title

**English:** Modeling and Experimental Characterization of Pressure-Controlled Bending Mechanics in Superelastic NiTi Wire Bundles

**Vietnamese:** Mô hình hóa và đặc trưng thực nghiệm cơ học uốn của bó dây NiTi siêu đàn hồi dưới áp suất giam giữ điều khiển

## Remaining pre-execution checks

- Confirm that achievable curvature and pressure produce overlapping slip and NiTi transformation regimes.
- Define pressure, contact, and local transformation measurements with adequate resolution.
- Predefine parameter calibration, held-out operating conditions, and material discrepancy criteria.
- Compare MP1 with preserved D1/M1 before topic lock.

## Astra escalation

- **Required:** False
- **Reason:** The supplied full-text evidence and the documented coverage closure support an unambiguous protocol-bounded outcome. The remaining model test is ordinary research design, and cross-direction comparison has not yet shown a conflict requiring high-cost critique.

## Recommended next action

Advance MP1 to a scoped feasibility and model-discrimination design, then compare its scientific value and execution risk with preserved D1/M1 before selecting the MSc topic.

## Provenance

- V002_PROTOCOL — docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md — SHA256 5f72a12e1052cda57e6f7e9d57a6f6e2311b118f6b0c49c24bf7a40cd253e30e
- MP1_PROJECT_STATE — docs/project/MP1_MENTOR_PIVOT_CURRENT.md — SHA256 51a980c8e2f81444a568f9828c5b2d02c5cef7f0a6a465786d2aefe9531da016
- V001_BASELINE_AUDIT — outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json — SHA256 0f7d8dfc4aae78139a483a9132b54e2eb1ada0a69304f96c3f1b0e2c197a7e81
- V002_16_PAPER_FULL_TEXT_MATRIX — outputs/verification/MP1-V002/verification_matrix.json — SHA256 85f7858ca0ac7e0a8bbc23bb97076d1c56b22b71f38bcc0f15012b1f39bb9445
- V002_INTERIM_TARGETED_THREAT_AUDIT — outputs/verification/MP1-V002/TARGETED_THREAT_AUDIT.json — SHA256 2a7062fc2ef72d7d0ad49ed102d1ac6d24e1c45fed7440bb89e57d8cc1eb8e7d
- V002_CITATION_COVERAGE_CLOSURE — outputs/verification/MP1-V002/citation_coverage.json — SHA256 c04f4d70eb560b71b907e4e3158a27a427d9e5248150d2d72738f7c8a5af6b7b
