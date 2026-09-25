# Final Cross-Direction MSc Adjudication

- **Selected direction:** D1_M1
- **Decision:** LOCK_WITH_FEASIBILITY_GATE
- **Confidence:** medium
- **Astra escalation:** False
- **Bundle SHA256:** 9fd2de53ff436591394306f26c925441890d1a10e22f4a7ed853d056ebd15fa4

## Executive summary

Select D1/M1 provisionally. It has a specified baseline model, a clearer model-error question, measurable beam-level outputs, and a stronger path to an interpretable result even if the expected breakdown pattern is wrong. Its contribution must be an experimentally tested, output-specific validity map with a physical explanation; predeclared tolerances alone add little. MP1 survived its citation audit, but its decisive transformation-plus-slip regime is not yet known to be accessible, and an existing transformation-aware NiTi contact model may explain the data. D1/M1 should pass one boundary-resolvability pilot before irreversible thesis commitment.

## D1/M1 assessment

- **scientific_question:** Where, across layer count, vacuum pressure, and bending severity, does the specified Zhang et al. continuum beam model predict selected outputs within justified tolerances, and what contact or slip mechanisms explain failure?
- **novelty_position:** D1-V008 and D1-V009 permit a protocol-bounded novelty lock for an experimentally supported validity/breakdown map. Neither a predeclared tolerance by itself nor established continuum, frictional-slip, or contact mechanics is a contribution.
- **modeling_readiness:** The reduced model M1 is named and its principal slip mechanics and beam outputs are documented. A full-layer frictional-contact FE reference is specified in architecture but its formulation, pressure representation, convergence protocol, and implementation remain open.
- **experimental_readiness:** Deflection and load response are plausible primary measurements; stiffness and slip onset are candidates. The apparatus and boundary-sampling plan are not frozen.
- **identifiability:** Vacuum-to-interface-pressure mapping, friction, contact state, and sheath effects could confound model-form error. Independent calibration and uncertainty bounds are needed before interpreting an M1–reference discrepancy.
- **execution_risk:** Moderate to high: reconstructing M1 and building a credible contact FE reference are substantial MSc tasks. The critical risk is that the predicted accepted and rejected regions cannot be resolved experimentally within an accessible domain.
- **publication_logic:** A journal paper is coherent if it reports reproducible output-specific validity regions, deliberately tests conditions on both sides, and explains discrepancies through observed or well-supported contact and slip mechanisms. A merely expanded M1 comparison or threshold choice would be weak.
### remaining_unknowns
- Exact full-layer reference formulation and its numerical credibility
- Final shared outputs, error metrics, and justified tolerances
- Independent calibration of friction and vacuum-generated contact pressure
- Existence of experimentally accessible, distinguishable valid and invalid conditions

## MP1 assessment

- **scientific_question:** Does independently varied confinement pressure alter NiTi-bundle bending, slip, transformation, and hysteresis in ways that calibrated elastic-wire and transformation-aware NiTi contact models cannot predict?
- **novelty_position:** MP1-V002 closed its targeted citation coverage without a direct kill. Active pressure is a control protocol; NiTi friction, transformation, wire mechanics, and contact are prior art. A distinct coupling claim fails if the existing transformation-aware contact model, H0b, predicts the declared domain adequately.
- **modeling_readiness:** Relevant elastic-wire and transformation-aware contact frameworks are identified, but no single implemented baseline and higher-fidelity pair is frozen for the proposed specimen and loading protocol.
- **experimental_readiness:** Moment–curvature loops and pressure can be measured in principle. Credible discrimination also requires local transformation evidence, inter-wire slip evidence, independent material calibration, and control of temperature and history.
- **identifiability:** Material transformation, friction, contact force, temperature, axial bias, and cycle history can trade off in fitted bending curves. Without local measurements, model discrimination may collapse into effective-parameter fitting.
- **execution_risk:** High: the required pressure-controlled fixture, NiTi state control, and local diagnostics add substantial burden. It is unverified that slip and stress-induced transformation coexist in an accessible pressure–curvature domain.
- **publication_logic:** A strong paper is possible if an accessible transformation-plus-slip regime supports a decisive, independently calibrated H0b comparison. If H0b predicts the observations, a distinct mechanics claim is lost; careful characterization may still be useful but has less certain publication strength.
### remaining_unknowns
- Accessible overlap of inter-wire slip and stress-induced transformation
- Practical resolution of local transformation and slip measurements
- Pressure-to-contact-force calibration
- Predictive adequacy of the existing transformation-aware NiTi contact model

## Direct comparison

| Criterion | D1/M1 | MP1 | Decision relevance |
|---|---|---|---|
| 1. Scientific-question clarity | One named model and an output-specific validity question. | Clear discrimination question, conditional on reaching coupled slip and transformation. | Favors D1/M1. |
| 2. Novelty/falsification maturity | D1-V008 and D1-V009 support a narrow, protocol-bounded lock. | MP1-V002 citation chase is closed; the distinct coupling claim remains experimentally contingent. | Favors D1/M1 modestly. |
| 3. Concrete baseline model | Zhang et al. M1 is fixed. | Candidate elastic-wire and NiTi-contact frameworks are identified but not frozen as one implementation. | Favors D1/M1. |
| 4. Concrete higher-fidelity/reference model | Full-layer explicit-contact FE is defined in scope; exact formulation remains open. | Transformation-aware constitutive plus Coulomb contact is a plausible comparator; implementation remains open. | Slightly favors D1/M1; neither reference is ready. |
| 5. Independent and dependent variables | Layer count, vacuum pressure, and bending severity map to beam outputs. | Pressure and curvature are controllable, while temperature, axial state, and history need tighter control. | Favors D1/M1. |
| 6. Parameter identifiability | Friction and contact pressure are challenging but can be separately constrained. | Transformation, friction, contact, and thermal history can produce similar global responses. | Favors D1/M1. |
| 7. Experimental measurability | Deflection and load are direct; local slip and pressure remain harder. | Global loops are accessible, but decisive local transformation and slip evidence is demanding. | Favors D1/M1. |
| 8. Apparatus complexity | Vacuum beam bending rig plus contact FE. | Pressure-controlled bundle fixture plus NiTi state and local diagnostics. | Favors D1/M1 for MSc execution. |
| 9. Reachability of critical regime | M1 explicitly predicts slip transitions; accessible boundary crossing is still unproved. | Coexistence of slip and stress-induced transformation is unproved. | Favors D1/M1, subject to the immediate gate. |
| 10. Model-discrimination strength | M1, full-layer reference, and experiment can give output-specific tests. | Could discriminate elastic and transformation-aware contact models if the coupled regime is reached and local states are measured. | D1/M1 has the more reliable path; MP1 has conditional upside. |
| 11. Risk of parameter fitting | Contact and pressure parameters could be tuned to hide model-form error. | Effective stiffness and hysteresis parameters could absorb the proposed effect. | Both require independent calibration; risk is greater for MP1. |
| 12. Scientifically weak negative result | No observed breakdown can still bound M1 validity if the tested domain and resolution are adequate. | If H0b predicts the data, the distinct coupling claim ends. | Favors D1/M1. |
| 13. MSc implementation burden | Contact FE is substantial, but the model and primary outputs are already specified. | Fixture development, NiTi calibration, local diagnostics, and multiple models must converge. | Favors D1/M1. |
| 14. Reproducibility | Geometry, pressure, loading, and numerical protocols can be reported explicitly. | Temperature, preconditioning, loading rate, and cycle history add sensitivity. | Favors D1/M1. |
| 15. Journal publication logic | A physically explained, experimentally tested validity map is a coherent mechanics paper. | A decisive H0b discrimination study could publish, but its key regime and measurements are unconfirmed. | Favors D1/M1 at current readiness. |
| 16. Specialized instrumentation or material control | Needs reliable pressure and beam-response measurement. | Needs credible transformation and inter-wire slip diagnostics plus material-state control. | Favors D1/M1. |
| 17. Publishability of a null result | An uncertainty-bounded wide validity domain or falsified expected mechanism remains informative. | H0b success can support a characterization paper, but weakens the distinct mechanics contribution. | Favors D1/M1. |
| 18. Remaining fatal unknowns | Reference credibility and experimental boundary resolvability. | Coupled-regime accessibility, local-state observability, and H0b adequacy. | D1/M1 has the more tractable immediate feasibility test. |

## Fatal risks

### D1_M1
- **Risk:** No accessible operating conditions yield an uncertainty-resolved accepted/rejected contrast, or the full-layer reference cannot credibly represent vacuum contact.
- **Kill/pivot condition:** The boundary-resolvability pilot fails after independent calibration and numerical verification; narrow to a defensible validity-domain study only if that result remains scientifically substantial.

### D1_M1
- **Risk:** The work becomes another M1 simulation/experiment comparison without an interpretable model-form boundary or physical mechanism.
- **Kill/pivot condition:** If no output-specific map and independently tested explanation can be produced, the claimed thesis contribution is not met.

### MP1
- **Risk:** Slip and stress-induced transformation do not coexist within safe, measurable pressure–curvature conditions.
- **Kill/pivot condition:** Reject the distinct coupled-mechanics question if the overlap regime cannot be demonstrated.

### MP1
- **Risk:** Existing transformation-aware NiTi constitutive behavior plus Coulomb contact predicts the observations.
- **Kill/pivot condition:** Reject a new coupling or constitutive claim if independently calibrated H0b meets the declared predictive criteria.

## Selection rationale

D1/M1 better balances defensibility and MSc feasibility because its named model, measurable outputs, and M1–reference–experiment comparison make both agreement and disagreement interpretable. Its novelty survives only as a physical validity study, so commitment is conditional on showing that an accepted/rejected contrast can be resolved in practice. MP1 is scientifically legitimate but depends on a harder-to-reach coupled regime and measurements needed to distinguish a new effect from H0b or fitted parameters. This ranking is an inference from the supplied D1-V008, D1-V009, M1 architecture, MP1-V002 adjudication, and citation-coverage files; it is not a claim that either experiment has already succeeded.

## Final working title

**English:** Experimental Assessment of the Validity and Breakdown of a Continuum Model for Vacuum Layer-Jamming Beams

**Vietnamese:** Đánh giá thực nghiệm giới hạn hiệu lực và sự mất hiệu lực của mô hình liên tục cho dầm kẹt lớp chân không

## Final research question

Across a declared range of layer count, vacuum pressure, and quasi-static bending severity, for which measurable outputs and operating conditions does the Zhang et al. continuum layer-jamming beam model meet predeclared, justified error tolerances against a verified full-layer frictional-contact reference and independent experiments, and which contact or slip mechanisms explain failures?

## Scientific hypothesis

M1's output-specific error will generally grow as finite-layer discreteness and slip or contact-pressure redistribution become important, yielding experimentally resolvable validity and breakdown regions. The predicted trend and boundary are testable and may be rejected.

## Immediate next gate

- **name:** D1/M1 boundary-resolvability pilot
- **objective:** Determine whether a verified M1–full-layer reference comparison yields both accepted and rejected conditions within a physically testable domain, with measurement precision sufficient to test the distinction.
- **pass_condition:** Using independently calibrated parameters and tolerances fixed before inspecting final pilot errors, verify M1 and reference implementations; identify at least one accessible condition on each side of an output-specific M1–reference tolerance boundary with numerical uncertainty smaller than the classification margin; and demonstrate physical measurements of that output at those conditions with uncertainty small enough to test the classifications. Experimental disagreement is recorded as evidence, not treated as automatic gate failure.
- **fail_condition:** No accepted/rejected contrast is accessible and uncertainty-resolved for a shared measurable output, or the full-layer reference cannot be numerically verified or independently constrained well enough to interpret the contrast.
### required_outputs
- Reconstructed M1 equations, assumptions, and reproduction check
- Specified full-layer contact formulation, convergence check, and independent parameter-calibration record
- Predeclared primary output, error metric, justified tolerance, and uncertainty budget
- Predicted accepted and rejected pilot conditions within apparatus limits
- Pilot measurements and a decision on whether the boundary can be tested

## Astra escalation

- **Required:** False
- **Reason:** The supplied evidence supports a defensible D1/M1 preference with one concrete feasibility gate. The remaining uncertainty is empirical and implementation-specific rather than a close unresolved scientific contradiction requiring Astra.

## Provenance

- D1_CURRENT_HANDOFF — docs/project/PROJECT_HANDOFF_CURRENT.md — SHA256 7cc7cbbf8d5313dead2c81910a0342e222f75f7d4ffdb141f9333fb58118b4ff
- D1_FINAL_NAMED_TARGET_AUDIT — outputs/verification/D1-V008/FINAL_NAMED_TARGET_AUDIT.json — SHA256 b888cfe083888aa0b2859ee97046f60e2c4d505cc4882f258fd29e305f28cd3a
- D1_LATE_FOUND_TARGET_AUDIT — outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json — SHA256 6cb12372d216ed471bdaba91aaa2568061046e660696b00fec91e78dc059b474
- D1_M1_RESEARCH_ARCHITECTURE — docs/research_design/M1_RESEARCH_ARCHITECTURE_VI.md — SHA256 6b2e210b46791bf990075dc4d4e3ea58c266722aa418be39827ebf38d01de156
- MP1_FINAL_ADJUDICATION — outputs/verification/MP1-V002/FINAL_ADJUDICATION.json — SHA256 535eb2f4906804356a5573488b3d2bffa1f4527e48b3970488c9b501e5cc7ac3
- MP1_CITATION_COVERAGE_CLOSURE — outputs/verification/MP1-V002/citation_coverage.json — SHA256 c04f4d70eb560b71b907e4e3158a27a427d9e5248150d2d72738f7c8a5af6b7b
