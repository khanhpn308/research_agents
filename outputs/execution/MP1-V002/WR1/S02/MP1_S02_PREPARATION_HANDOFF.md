# MP1-V002 WR1-S02 preparation handoff

**Preparation status:** PREPARATION_COMPLETE_PHYSICAL_PILOT_PENDING. **WR1-S02 gate:** NOT_YET_TESTED; do not mark COMPLETE or PASS. GAP-05, GAP-06 and GAP-08 remain OPEN. No physical experiment, energized pressure test, search, H1 formulation, held-out fit or novelty adjudication occurred.

## Cheapest proposed pilot

Start with a short straight triangular **three-wire** NiTi specimen in a flexible annular positive-pressure cuff whose outer layer reacts pressure and whose inner membrane presses inward. The wire count, example diameters and span in the apparatus specification are ENGINEERING_STARTING_POINT values, not approved build dimensions or safety limits. The researcher must select and document the actual wire lot, geometry, cuff/connection ratings, allowed pressure/curvature/temperature/cycles and approved lab shutdown procedure before any loading.

Track load/moment, local curvature and chamber pressure; corrected adjacent-wire relative motion; a batch-calibrated transformation-sensitive **indirect** signature (unless direct phase sensing is validated); wire-relevant temperature and rate/history; membrane/section shape; and clamp motion. Optical access and feedthrough compatibility are untested. Use the adaptive C0–C5 screen, stop early on failed access or observability, and reserve repeat/rate tests for the most informative safe condition. A negative three-wire screen cannot be generalized to a larger actual MP1 bundle without a written domain-coverage argument.

## Deliverables and sequence

1. MP1_S02_PILOT_PROTOCOL.md — human-executable order, preflight blanks and decisions.
2. MP1_S02_SPECIMEN_AND_APPARATUS_SPEC.json — proposed build and classified provisional values.
3. MP1_S02_MEASUREMENT_CHANNEL_MATRIX.json — minimum channel functions and feasibility questions.
4. MP1_S02_COEXISTENCE_ANALYSIS.md — transformation/slip scaling and overlap proof standard.
5. MP1_S02_TEST_MATRIX.json — adaptive minimal pressure/curvature/rate/history cells.
6. MP1_S02_STOP_AND_PASS_GATE_REGISTER.json — seven stops and eight eventual pass criteria, all NOT_YET_TESTED.
7. MP1_S02_DATA_SCHEMA.json — synchronized raw/processed data and pilot-only segregation.
8. MP1_S02_UNCERTAINTY_PLAN.json — event, thermal, fixture, sleeve and sensor uncertainties.
9. MP1_S02_TARGETED_RETRIEVAL_TRIGGER.json — exact unexecuted lot/component requirements.
10. MP1_S02_PREPARATION_RECEIPT.json — preparation QA and scope receipt.
11. MP1_S02_PREPARATION_HANDOFF.md — this file.

## Human execution handoff

Before pressurization, select exact components and lot, obtain the approved wire fatigue/strain and full-assembly pressure limits, prove seal/relief and inward pressure transmission with dummy wires, calibrate local channels, and sign a pilot build/safety sheet. Review marker/feedthrough perturbation with matched controls. Acquire all S02 files under PILOT_ONLY IDs; none can be S06 untouched validation. The eventual S02 gate needs real repeatable sealed, overlap, channel-noise and specimen-integrity evidence plus human review. S03/S04 can use the pilot only after those limitations are explicit.

## Scientific boundary

S01 found an existing formulation sufficient **in principle**; H0b remains NOT_FALSIFIED. A pilot coexistence result does not show H0b failure or H1 necessity. Chamber pressure is external traction, not measured local normal force. The optional isothermal branch can be selected only from measured temperature/rate/history uncertainty; otherwise the later H0b needs a thermomechanical branch or a narrowed domain.
