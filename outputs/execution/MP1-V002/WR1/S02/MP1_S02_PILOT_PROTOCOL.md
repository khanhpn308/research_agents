# MP1-V002 WR1-S02 — sealed coexistence and sensing feasibility pilot protocol

**Status: PREPARATION_COMPLETE_PHYSICAL_PILOT_PENDING.** No physical pilot, pressure test, parameter fit or model discrimination has occurred. GAP-05, GAP-06 and GAP-08 are OPEN; all eventual S02 pass criteria are NOT_YET_TESTED. This is an executable design after the human researcher fills the selected hardware, ratings, lot calibration and safety limits below.

## Objective and falsification question

Find the cheapest safe test that can establish, or fail to establish, **same-region, same-time interwire slip and stress-induced NiTi transformation** in a sealed, positively confined wire specimen while independently measuring both mechanisms. If the accessible safe domain or measurement channels fail, stop or narrow the current MP1 coupling-core question before S03–S07. A negative result from a small screening geometry is generalized only when its tested domain brackets the intended actual bundle.

The scientific status inherited from W02 and S01 is H0a = REFUTED_IN_TRANSFORMATION_REGIME, H0b = NOT_FALSIFIED / LIVE COMPETITOR, H1 = INSUFFICIENT_EVIDENCE, and formulation-level GAP-07 = EXISTING_FORMULATION_SUFFICIENT_IN_PRINCIPLE. This pilot does not formulate H1 or judge novelty.

## Preflight decisions the researcher must record before energizing

| Decision | Provisional selection and value class | Required human record before test |
|---|---|---|
| Contact specimen | Three straight NiTi wires in triangular packing — **ENGINEERING_STARTING_POINT**. | Actual MP1 target count/packing and whether this small section covers its intended strain/contact domain. |
| Wire diameters | Primary 0.5 mm; alternate 0.25 mm — **ENGINEERING_STARTING_POINT**, not final stock. | Exact lot, measured diameters, transformation temperatures, cyclic response, surface state, safe strain/fatigue limit. |
| Active span | 50 mm — **ENGINEERING_STARTING_POINT**. | Chosen span from fixture clearance, local curvature uniformity, image field of view and load range. |
| Initial geometry/prestrain | Straight and no intentional prestrain — **ENGINEERING_STARTING_POINT**. | Measured initial curvature and assembly axial strain; any deliberate prestress with a separate safety rationale. |
| Pressure | Ambient differential, then low and higher nonzero levels — **ENGINEERING_STARTING_POINT sequence**. | Exact cuff/inner membrane/outer restraint/tubing/window ratings, proof/leak limit, regulator limit, relief and approved pressure values. |
| Curvature | Adaptive staircase guided by measured same-lot transformation threshold and approved wire/sleeve limits. | Approved maximum curvature and strain with uncertainty; do not adopt W02's approximate threshold as lot-specific safety limit. |
| Loading rate/history | Slow and faster actual local rates or slow/dwell contrast; three confirmation cycles are **ENGINEERING_STARTING_POINT**. | Numeric rates, dwell, training and repeat count with thermal sensor bandwidth and fatigue/integrity basis. |
| Safety | No numeric limit is approved by this document. | Written stop values for pressure, strain/curvature, load, temperature, leak, residual set, clamp motion and sensor failure, with named operator and lab approval. |

The positive-pressure cuff is an **annular chamber** around a dry wire lumen: a compliant inner membrane transmits load inward while an outer pressure-reacting layer restrains outward inflation. The assembly must visibly and measurably contract toward the wire bundle at approved pressure. The bend section must remain flexible. A generic pressurized tube is not assumed to provide confinement. End collars seal the annulus; instrumented wire tails and fixture markers remain outside the active pressure section. All-component pressure rating and proof/leak testing precede wire testing. The apparatus specification gives the exact proposed architecture and the remaining selections.

## Minimum measurement functions

Acquire synchronized global load/moment, **local** curvature and active-cuff pressure. Acquire corrected interwire relative displacement, a separately supported transformation-sensitive local signature, wire-relevant temperature plus actual rate/cycle history, membrane/section deformation and clamp/fixture motion. The measurement matrix specifies candidate methods, required resolution, range, sampling, intrusion, sealed compatibility, calibration, confounds and fallback for each function.

The first-choice low-cost slip channel is optical tracking of paired material markers on neighboring exposed outer wire surfaces through a pressure-rated transparent path, while simultaneously tracking membrane, bundle and clamp references. That optical path and marker perturbation are **unproven**. An end-tail differential displacement channel is only a proxy: subtract rigid motion and calibrated differential elastic extension, then validate it against a direct visible reference. If neither works under seal, STOP-4.

Local strain alone is never called phase fraction. The least expensive defensible **indirect transformation support** is: batch-matched single-wire thermomechanical calibration at the pilot temperature/rate/history; local wire strain trajectory and a thermal or separately calibrated phase-sensitive response in the bundle; and elastic, friction-only, membrane and fixture controls that cannot explain the signal within uncertainty. Four-terminal resistance is optional only if interwire electrical shunting and pressure-sensitive contact resistance are excluded. If evidence is limited to strain crossing a nominal threshold, transformation is INDETERMINATE and PASS-4 is unmet.

## Execution sequence

1. **Freeze pilot build sheet.** Assign specimen IDs, wire lot, actual dimensions, packing orientation, sensor/marker layout, cuff component IDs, pressure/strain/temperature ratings, limit values and calibration IDs. Tag all future files S02_PILOT_ONLY. Human review signs the energized test plan.
2. **Calibrate single-wire and sensors.** On separate same-lot wires, measure cyclic response at planned temperatures/rates and identify transformation-sensitive signatures and variability. Calibrate load, pressure, geometry, clocks, optical distortion and thermal lag. Test elastic and friction-only controls. These are S02 pilot/calibration data, never S06 held-out data.
3. **Prove cuff without NiTi loading.** Check annulus pressure containment, inward displacement, line lag, optical path or feedthrough, leak, relief action and bend compatibility with inert dummy wires. Record sham moment/curvature and membrane-only effects.
4. **Quantify sensor perturbation.** Compare marked/instrumented with otherwise matched unmarked builds, geometry and bend response. If marker/lead/window changes packing or slip beyond the predeclared perturbation budget, STOP-5.
5. **Run adaptive regime screen.** Start at ambient differential pressure and below the measured transformation onset; move curvature only within approved limits. Seek a corrected slip-only state, then repeat at one approved low pressure. Increase curvature toward the batch-specific transformation window and seek temporal overlap. A higher pressure condition may reveal transformation without slip; it is optional if unsafe or redundant.
6. **Repeat and perturb rate/history.** Revisit the most informative safe pressure-curvature path at a distinguishable rate or with dwell, then confirmation cycles. Record temperature, cycle training, drift, membrane shape, clamp motion and damage. Use the smallest informative matrix in MP1_S02_TEST_MATRIX.json, not an open-ended DOE.
7. **Process blind to a favorable outcome.** Preserve raw data; apply preregistered calibrations, time alignment, rigid-body/clamp/elastic corrections and uncertainty intervals. Label each cell NO_SLIP_NO_TRANSFORMATION, SLIP_ONLY, TRANSFORMATION_ONLY, COEXISTENCE or INDETERMINATE. Do not select a favorable segment after seeing the loop.
8. **Apply stop/pass gates.** Stop immediately on integrity or safety triggers. All eight eventual pass criteria require real data and human review; preparation cannot pass them. Document whether any negative result genuinely covers the intended MP1 bundle or requires another specimen.

## Thermal decision

Two actual rate conditions or a rate/dwell contrast must test whether self-heating, thermal lag and cycle training change the mechanism signatures. Compare the measured shift plus uncertainty against the future discrimination margin chosen before later model validation. If negligible within the declared domain, record ISOTHERMAL_H0b_ALLOWED; if explanatory or material, record THERMOMECHANICAL_H0b_REQUIRED; if wire temperature is unresolved, record INDETERMINATE and redesign. No arbitrary universal temperature or rate threshold is specified.

## Predeclared stops and eventual pass

STOP-1 through STOP-7 and PASS-1 through PASS-8 are in MP1_S02_STOP_AND_PASS_GATE_REGISTER.json with observation, interpretation and route. The hard safety route is immediate physical shutdown under lab procedure. No claim of coexistence follows from an analytical strain threshold, global M–kappa loop, end-tail motion alone, or uncalibrated phase proxy.

An eventual pass needs sealed repeatability, safe durable p–kappa–T access, independent slip and transformation support with temporal overlap, measured noise/intrusion, bounded or explicitly modeled thermal/rate/history effects, and acceptable specimen integrity. This document records every criterion as **NOT_YET_TESTED**.

## Data, uncertainty, segregation and retrieval

Use MP1_S02_DATA_SCHEMA.json for raw stream/channel units, calibration IDs, synchronized timestamps, specimen/cycle/pressure/curvature/temperature context and processed provenance. Use MP1_S02_UNCERTAINTY_PLAN.json for shared optical, timing, thermal, membrane and fixture errors. All S02 data remain PILOT_ONLY. They may inform S03/S04 design but can never be untouched S06 validation. Chamber p is a boundary measurement, never interwire normal force.

Broad search is CLOSED. MP1_S02_TARGETED_RETRIEVAL_TRIGGER.json names the exact missing selected-wire fatigue envelope, selected cuff assembly rating and selected optical/feedthrough feasibility items. These triggers are **not executed**; component selection and direct bench proof close them. No supplier rating is guessed.

## Direct answer

The cheapest scientifically defensible screen is a short, straight, three-wire triangular NiTi specimen in a proof-tested inward-loading annular pressure cuff, bent under measured local curvature while tracking neighboring wire motion, a batch-calibrated transformation-sensitive signature, temperature, pressure, sleeve shape and clamps on a synchronized clock. Begin with pressure and curvature controls, then adaptively approach the safe transformation window and repeat only the most informative condition at another rate. If a safe overlap cannot be reached or the sealed channels cannot separate the mechanisms, stop or narrow the coupling-core question; a positive signal preserves only the **tested feasibility domain**, not a new mechanics law.

## Evidence and limitations

**VERIFIED REPOSITORY STATE:** WR1 stage gate and W02 K1/K3/K9 identify the three open S02 questions. **VERIFIED FULL TEXT:** Reedlunn et al. (2013 Part I, paper_id 00414aac4b) demonstrates synchronized optical/thermal methods on exposed tensile cables. **INFERENCE / DESIGN:** The three-wire cuff, equations, channels, matrix and stop logic are proposed for this pilot; no sealed optical method, wire-lot safe limit, pressure rating or local transformation channel has been demonstrated. Exact supporting pointers are in MP1_S02_COEXISTENCE_ANALYSIS.md and the S01 package. AI assistance was used for preparation. No physical experiment, new search or external source verification occurred.
