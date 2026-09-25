# W2-09 Astra High adversarial red-team report

## Scope and evidence status

This independent red-team inspected W2-01 through W2-08, the MP1-V002 verification matrix, targeted-threat audit, citation-coverage closure, final adjudication, and the three Astra/remediation reports. No web search, paper acquisition, ingestion, canonical-state edit, D1 analysis, or final adjudication was performed. Source claims are treated as `VERIFIED FULL TEXT` only where the cited matrix/evidence record says so; registry interpretations are marked `REGISTERED`; conclusions below are `INFERENCE`.

The candidate was challenged as a hypothesis. The evidence supports a narrow, falsifiable model-discrimination question, but does not support a claim that a distinct constitutive-contact coupling exists. The strongest surviving risks remain H0b sufficiency, experimental identifiability, pressure-to-contact-force mapping, and parameter leakage. Therefore the earlier K1-K9 gate remains scientifically blocking even though citation coverage later reached protocol closure.

## Candidate challenge

MP1-P1 is only defensible as: *test whether a locked, established transformation-aware NiTi plus contact/friction model predicts pressure-controlled bundle bending and local slip/transformation observables.* The wording “survives” is safe only when explicitly protocol-bounded. Any wording that says pressure-controlled NiTi bending is novel, that H1 follows from rejection of a constant-modulus model, or that 15/15 citation closure proves absence of prior art is unsupported.

## K1-K9 challenge summary

| Test | Astra challenge | Status | Blocking implication |
|---|---|---|---|
| K1 | Coexistence of slip and stress-induced transformation was bounded analytically/inferentially but not demonstrated in an accessible, durable operating envelope. Small-strain collapse and fatigue/membrane integrity remain live. | MAJOR_CHALLENGE | Blocks a claim that the proposed regime is experimentally reachable. |
| K2 | H0b (existing NiTi constitutive law + Coulomb contact) has not been run with locked calibration on pressure-curvature paths. H0a rejection cannot discriminate H1. | CONFIRMED_GAP | CRITICAL; H1 is not established. |
| K3 | Global M-kappa is non-identifying; local DIC/FBG/IR/slip channels are proposed but not executed and can still be confounded by clamps, packing, axial tension, and temperature. | CONFIRMED_GAP | CRITICAL; macro-only mechanism claims are invalid. |
| K4 | Device/jamming/active-pressure novelty is closed or downgraded. Only model discrimination remains; contribution value is conditional on a measurable H0b failure. | MAJOR_CHALLENGE | Broad architecture claims are killed. |
| K5 | The 15/15 stop condition is now true, but it means all required directions were screened under the protocol; many anchors remain `screened_candidates_found` and no full-text universal-absence inference is licensed. | MAJOR_CHALLENGE | Citation closure cannot be converted into universal novelty. |
| K6 | Chamber pressure is a boundary input, not a known inter-wire normal force. Membrane hoop stress, packing/arching, curvature and axial load make p -> f_n underdetermined without independent calibration. | CONFIRMED_GAP | HIGH; pressure-dependent model comparison is confounded. |
| K7 | Existing cable/contact incremental formulations can accept nonlinear constitutive laws. No forward calculation shows a phenomenon they cannot reproduce. | MAJOR_CHALLENGE | H1 distinctness remains unproven. |
| K8 | Locked Calibration Rule is a protocol requirement, not demonstrated data. mu, pressure transmission, prestrain, contact penalty and effective stiffness can compensate. | CONFIRMED_GAP | HIGH; free-fit results would be non-causal. |
| K9 | Hysteresis and stiffness are confounded by latent heat, rate, friction, training, wear, geometry, and clamp compliance. Quasi-static loading alone does not identify phase versus friction. | UNRESOLVED | MEDIUM/HIGH residual risk; thermal and history controls required. |

## Critical and high findings

1. **H0a rejection does not imply H1.** Refuting a constant-modulus elastic strawman only establishes that a richer material/history law may be needed. H0b already contains established NiTi transformation and Coulomb contact. The logical path H0a -> H1 is invalid unless a locked H0b prediction fails on discriminating observables.
2. **H0b is still live and is the direct competitor.** Neither the 16-paper matrix nor the final adjudication contains a numerical benchmark or withheld-condition experiment that falsifies H0b. This is a critical blocking gap, not a routine implementation detail.
3. **Pressure is not an identified mechanics variable until p -> f_n is calibrated.** Calling active pressure a boundary condition is correct, but it does not solve transmission. A chamber gauge can be precise while contact force remains unknown; pressure changes may also alter membrane geometry, axial tension, and packing.
4. **M-kappa cannot identify mechanism globally.** A model can match or miss a moment-curvature loop for the wrong cause. Local slip and transformation measurements are necessary, but their feasibility under a sealed pressurized bundle, and their separation from clamp/packing effects, remain unproven.
5. **Locked calibration has not happened.** The rule is a guardrail. Until independent friction, single-wire constitutive, pressure-transfer, prestrain and contact parameters are measured and propagated with uncertainty, apparent model superiority can be post-hoc fit or parameter compensation.
6. **Coexistence is a feasibility hypothesis.** The reported ~0.75% small-strain boundary and deep-bending/axial-tension requirement bound the search, but no specimen-level map establishes simultaneous slip and transformation over a robust cycle life. If the accessible domain misses overlap, the candidate collapses to known elastic wire jamming or known NiTi hysteresis.
7. **Citation closure is protocol closure.** `all_required_directions_screened=true`, `no_unresolved_high_threat_source=true`, and `satisfied=true` supersede the stale pre-closure records, but cannot support “no closer prior work exists.” Several anchors are recorded as `screened_candidates_found` without included full-text candidates; the final adjudication correctly retains a universal-absence caveat.
8. **Carboni correction is necessary but narrows the evidence.** S2a is ST49 steel; S1a is NiTi7 under tension-bending with substantial axial preload. This correction removes the alleged pure-bending NiTi evidence. Any residual text that uses Carboni as pure-bending proof is a contradiction candidate.

## Confirmed gaps

- Locked H0b forward prediction on pressure-curvature paths: absent.
- Independent p -> f_n calibration as a function of curvature/packing: absent.
- Local, mechanism-specific measurements demonstrated in the actual sealed bundle: absent.
- Independent parameter calibration and uncertainty propagation: absent.
- A verified overlap domain for simultaneous slip and transformation with acceptable fatigue/membrane integrity: absent.
- Formal separation of thermal, frictional, clamp, axial-tension and geometry contributions to hysteresis: absent.

## Unresolved items and contradiction preservation

The red-team preserves rather than silently reconciles the following: (a) stale W2-08 K5/THREAT-05 still reports citation stopping unmet, while canonical `citation_coverage.json` and final adjudication report closure; (b) the audit's historical `established` language conflicts with the corrected H0b/H1 `NOT FALSIFIED`/`INSUFFICIENT` interpretation; (c) the Carboni S2a/S1a extraction error is corrected in current reports but remains in historical worker artifacts; (d) “Astra escalation not required” in the final adjudication is a prior governance decision, whereas this worker is explicitly the requested Astra red-team and cannot convert unresolved gaps into approval.

## Astra escalation status

This requested Astra High adversarial pass is complete. It does not authorize a thesis lock, final novelty adjudication, human sign-off, or a claim of H1. W2-10 must synthesize these challenges and keep the candidate conditional on decisive H0b and feasibility tests.

## QA

Seven required files were written only under `outputs/execution/MP1-V002/W2-09/`. JSON files were validated with Python's JSON parser; source inputs were not modified. No new literature was searched or added. No D1 or cross-direction analysis was performed.

WORKER = W2-09
TASK = ASTRA HIGH ADVERSARIAL RED-TEAM
MODEL = GPT-6-ASTRA
STATUS = COMPLETE
NEW_LITERATURE_SEARCH = false
NEW_PAPERS_ADDED = false
FINAL_NOVELTY_ADJUDICATION = NOT PERFORMED
D1_ANALYSIS = NOT PERFORMED
D1-vs-MP1_COMPARISON = NOT PERFORMED
HUMAN_SIGN_OFF = NOT PERFORMED
CANONICAL_FILES_MODIFIED = false
NEXT_DEPENDENCY = W2-10 — FINAL SOL SYNTHESIS
