# D1-V003 Cross-Round Adversarial Synthesis

- **Status:** SURVIVES_WITH_REVISED_SCOPE
- **Confidence:** medium
- **Final verdict allowed:** False
- **Evidence bundle SHA256:** `efe7916b1849d6f76d7f16294300e060b58d6736cc3680835d397f12dba07122`

## Current P1

For one specified Zhang-type continuous-slip beam model and one fixed slender rectangular vacuum-jammed beam/material family under quasi-static planar bending, determine where predictions of transition load, force–deflection response, bending stiffness, and slip-zone state exceed predeclared error tolerances relative to explicit-interface mechanics and independently calibrated experiments as physical layer count, vacuum pressure, normalized load/curvature, and boundary condition are varied independently.

## Executive summary

[VERIFIED_FULL_TEXT] The broad premise is substantially pre-empted: continuum, continuous-slip-boundary, RVE-homogenized, discrete multilayer, pressure-dependent, curved-beam, hysteretic, and experimentally compared layer-jamming models already exist. Zhang's beam papers are the strongest threats because they already combine continuous slip representations with pressure, layer scale, curvature or large deformation, FEA, and experiments. Caruso and Narang already provide explicit-interface/discrete baselines across multiple layer counts and pressures. Fan/Yi provide reduced dynamic and control-oriented models with experimental pressure–stiffness validation. [INFERENCE] The essential residual problem is narrower: the supplied qualifying evidence does not establish a predeclared-tolerance validity domain or quantitative breakdown boundary for a named continuum mechanics model against both explicit-interface mechanics and independent experiment. Because adjacent-mechanics Track C is incomplete, this is a provisional corpus-bounded survival result, not a final novelty verdict.

## Model families

### Fan / Yi control-oriented continuum-robot family

**Model type:** Robot-level equivalent-beam and finite-dimensional PCC/rigid-link dynamics with lumped LuGre friction, pressure-dependent fitted stiffness terms, and passivity-based control; not an interface-resolved homogenization framework.

**Threat to P1:** medium

**Papers:**
- Fan, Liu, and Ye (2022), A Novel Continuum Robot With Stiffness Variation Capability Using Layer Jamming: Design, Modeling, and Validation, DOI 10.1109/ACCESS.2022.3228775
- Yi, Fan, and Liu (2024), A Novel Model for Layer Jamming-based Continuum Robots, DOI 10.1109/ICRA57147.2024.10610912
- Fan, Yi, and Liu (2026), Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots, DOI 10.1109/TCST.2026.3690756

**Established:**
- [VERIFIED_FULL_TEXT] Pressure-dependent aggregate transverse stiffness and shape locking are modeled and experimentally demonstrated.
- [VERIFIED_FULL_TEXT] The 2024/2026 models combine energy-based or port-Hamiltonian robot dynamics with lumped LuGre friction.
- [VERIFIED_FULL_TEXT] Fan 2026 reports a pressure–stiffness fit with R² = 0.9216 and experimentally demonstrates setpoint and stiffness regulation.
- [VERIFIED_FULL_TEXT] Fan 2022 experimentally characterizes transverse and axial stiffness versus pressure, robot curvature, and sheath overlap configuration.

**Not established:**
- [VERIFIED_FULL_TEXT] No physical interface-indexed slip field, contact-traction field, or discrete-layer reference is used to validate the lumped LuGre states.
- [VERIFIED_FULL_TEXT] Two- and five-layer sheaths serve different tasks rather than an independently controlled layer-count convergence study.
- [INFERENCE] Controller tracking error and in-sample stiffness-fit quality do not establish mechanics-model validity boundaries.
- [INFERENCE] No tolerance-defined failure surface over physical layer count, pressure, curvature/load, and slip regime is established.

### Caruso / Zhang mechanics lineage

**Model type:** Caruso retains discrete interface-indexed progressive slip; Zhang supplies continuous yielded-band beam models and an average-field/RVE elastoplastic continuum constitutive model.

**Threat to P1:** high

**Papers:**
- Caruso et al. (2023), Layer jamming: Modeling and experimental validation, DOI 10.1016/j.ijmecsci.2023.108325
- Zhang et al. (2025), A continuum-based model for a layer jamming beam, DOI 10.5194/ms-16-821-2025
- Zhang et al. (2025), Toward a deeper understanding of layer jamming structures, DOI 10.1007/s11465-025-0843-5
- Zhang et al. (online 2025/issue 2026), Continuum modeling for layer jamming structures, DOI 10.1016/j.taml.2025.100633

**Established:**
- [VERIFIED_FULL_TEXT] Caruso predicts sequential interface slip, transition loads, piecewise bending stiffness, and hysteresis for multilayer three-point bending and validates across multiple layer counts and pressures.
- [VERIFIED_FULL_TEXT] Zhang's Mechanical Sciences model replaces discrete interfaces with continuous stress fields and a moving sliding boundary, compares with 10- and 25-layer explicit layered FEA, and compares global response with a 20-layer experiment at 60 kPa.
- [VERIFIED_FULL_TEXT] Zhang's deeper-understanding paper treats pressure, layer thickness, straight and initially curved beams, progressive/full slip, large-configuration increments, and cyclic response with experimental comparisons.
- [VERIFIED_FULL_TEXT] Zhang's RVE paper derives a multiaxial elastoplastic continuum law and quantitatively compares selected constitutive outputs with periodic discrete-contact RVE FEA.

**Not established:**
- [VERIFIED_FULL_TEXT] The Zhang RVE model lacks physical experimental validation.
- [VERIFIED_FULL_TEXT] Reported discrepancies include boundary/end effects, overestimated sliding-zone width, full-slip curvature errors, low-pressure/thin-layer critical-load overprediction, and cyclic-dissipation underprediction.
- [INFERENCE] These discrepancies are observations or qualitative limitations, not a common error map with a predeclared acceptance tolerance.
- [INFERENCE] No study independently varies physical layer count at fixed total stack geometry while mapping continuum-versus-discrete and experimental error across pressure and slip regime.

### Narang foundational analytical/contact family

**Model type:** Exact two-layer Euler–Bernoulli slip mechanics plus explicit many-layer frictional-contact FEA and experiments.

**Threat to P1:** medium

**Papers:**
- Narang, Vlassak, and Howe (2018), Mechanically Versatile Soft Machines through Laminar Jamming, DOI 10.1002/adfm.201707136

**Established:**
- [VERIFIED_FULL_TEXT] Pre-slip, transition, and full-slip mechanics; pressure/friction-dependent slip; stiffness loss; slip propagation; and frictional damping are established.
- [VERIFIED_FULL_TEXT] Many-layer explicit-contact FEA is compared with experiments across layer-count and pressure sweeps, with reported minimum R² of 0.9879.
- [VERIFIED_FULL_TEXT] High-layer-count continuum-like approximation was explicitly identified as future work because explicit-contact computation scales with layer count.

**Not established:**
- [VERIFIED_FULL_TEXT] The analytical solution demonstrated in the supplied main-text evidence is for two layers; many-layer treatment is primarily explicit-contact FEA.
- [INFERENCE] High agreement of a discrete FEA with experiments does not validate a homogenized continuum model or define its breakdown boundary.
- [INFERENCE] No finite-layer convergence threshold for a named homogenized representation is established.

## Strongest falsifying evidence

- **A project claiming to develop the first continuum or high-layer-count reduced layer-jamming beam model is already falsified.**
  - Source: Zhang et al. (2025), DOI 10.5194/ms-16-821-2025; Zhang et al. (2025), DOI 10.1007/s11465-025-0843-5; Zhang et al. (online 2025/issue 2026), DOI 10.1016/j.taml.2025.100633.
  - Evidence: VERIFIED_FULL_TEXT
  - Proves: Continuum yielded-band beam models, a continuous sliding-boundary beam model, and an average-field/RVE elastoplastic continuum constitutive model already exist and cover explicit frictional yielding or slip.
  - Does not prove: It does not establish that any one model has a tolerance-defined validity domain relative to both explicit-interface mechanics and independent physical experiments.
- **Most proposed parameter axes—pressure, layer scale, curvature, slip regime, cyclic loading, and bending response—have already been included in one or more closely related models and experiments.**
  - Source: Caruso et al. (2023), DOI 10.1016/j.ijmecsci.2023.108325; Zhang et al. (2025), DOI 10.1007/s11465-025-0843-5; Zhang et al. (2025), DOI 10.5194/ms-16-821-2025.
  - Evidence: VERIFIED_FULL_TEXT
  - Proves: Merely adding these variables, more FEA cases, more pressure levels, curved specimens, or hysteresis measurements is not a defensible mechanics contribution.
  - Does not prove: It does not show that prediction error has been mapped over their joint parameter space or converted into an acceptance boundary.
- **Continuum models have already been compared quantitatively with interface-resolving numerical references.**
  - Source: Zhang et al. (2025), DOI 10.5194/ms-16-821-2025; Zhang et al. (online 2025/issue 2026), DOI 10.1016/j.taml.2025.100633.
  - Evidence: VERIFIED_FULL_TEXT
  - Proves: The literature goes beyond merely proposing continuum equations: it includes explicit layered FEA comparisons and periodic discrete-contact RVE comparisons, including reported constitutive deviations.
  - Does not prove: Selected comparisons are not a systematic finite-layer convergence study, declared-tolerance validity map, or experimentally validated breakdown boundary.
- **Discrete progressive-slip mechanics and multilayer experimental validation are mature enough to serve as established baselines.**
  - Source: Narang et al. (2018), DOI 10.1002/adfm.201707136; Caruso et al. (2023), DOI 10.1016/j.ijmecsci.2023.108325.
  - Evidence: VERIFIED_FULL_TEXT
  - Proves: Pressure–friction–slip transitions, interface progression, bending-stiffness degradation, hysteresis, and layer-count effects cannot be claimed as new.
  - Does not prove: Neither paper evaluates the later Zhang continuum representations across a tolerance-defined discrete-to-continuum boundary.
- **Reduced dynamic layer-jamming models with experimental pressure-dependent stiffness and shape-locking validation already exist.**
  - Source: Yi, Fan, and Liu (2024), DOI 10.1109/ICRA57147.2024.10610912; Fan, Yi, and Liu (2026), DOI 10.1109/TCST.2026.3690756.
  - Evidence: VERIFIED_FULL_TEXT
  - Proves: Broad novelty claims based on reduced modeling, LuGre friction, pressure–stiffness fitting, shape locking, or stiffness regulation are pre-empted.
  - Does not prove: These robot-level fitted models are not validated against discrete interlayer mechanics and do not map mechanics-model breakdown.

## Strongest surviving evidence

- **No predeclared-tolerance validity domain for a named mechanics-level continuum model.**
  - Basis: Across the verified Narang, Caruso, Zhang, Khaloujini, Yi, and Fan papers, errors, R² values, uncertainty bands, or qualitative mismatches are reported, but no supplied paper classifies parameter combinations as valid or invalid using a declared mechanics-error tolerance.
  - Evidence: INFERENCE
  - Why it survives: Model validation, good agreement, and isolated prediction errors are not equivalent to a validity map or breakdown boundary.
  - Uncertainty: Track C may contain a transferable general criterion under terminology such as partial interaction, shear lag, imperfect interfaces, or discrete-to-continuum convergence.
- **No systematic finite-layer convergence map from discrete interface mechanics to a specified continuum representation.**
  - Basis: Zhang's beam model includes selected 10- and 25-layer FEA comparisons; Zhang's continuous-boundary work uses several FEA layer counts and layer-thickness experiments; Caruso and Narang vary layer count in discrete models.
  - Evidence: INFERENCE
  - Why it survives: The evidence does not map a common error norm versus independently varied physical layer count while holding total stack geometry and other confounders fixed.
  - Uncertainty: Adjacent homogenization literature may already provide finite-layer convergence rates or scale-separation criteria directly transferable to this stack.
- **No unified continuum–discrete–experiment triad across pressure, curvature/load, slip regime, and boundary condition.**
  - Basis: The Zhang beam studies provide portions of this triad, while Caruso and Narang provide strong discrete/experimental baselines; the comparisons are not assembled into one factorial validity study.
  - Evidence: INFERENCE
  - Why it survives: The closest papers either use the discrete model to formulate the reduced model, validate only selected cases, fit structural parameters from response data, or omit one leg of the triad.
  - Uncertainty: The surviving study could be merely methodological unless it identifies a reproducible governing parameter or first omitted failure mechanism.
- **Quantitative separation of failure mechanisms remains unresolved.**
  - Basis: Verified papers identify boundary/end effects, transverse-normal-stress omission, pressure nonuniformity, large-curvature/full-slip error, fixture compliance, and friction-law limitations.
  - Evidence: VERIFIED_FULL_TEXT
  - Why it survives: These mechanisms are acknowledged but not ranked through controlled error decomposition or used to locate separate breakdown boundaries.
  - Uncertainty: Some discrepancies may be dominated by manufacturing or fixture artifacts rather than a fundamental continuum-limit failure.

## Evidence-gap matrix

| Dimension | Status | Interpretation |
|---|---|---|
| finite_layer_count_scaling | PRESENT | Layer-count effects are established. What remains unmapped is the error of a named continuum model versus finite layer count under controlled geometry. |
| explicit_interlayer_slip | PRESENT | Interlayer slip itself is not an open novelty claim; only representation error and breakdown may remain. |
| independent_layer_count_variation | PARTIAL | Counts are varied, but the supplied evidence does not establish the controlled fixed-total-height layer-count sweep needed to isolate discrete-to-continuum error from changing total thickness or other variables. |
| pressure_dependence | PRESENT | Pressure dependence is established; pressure–stiffness correlation is not a validity-domain map. |
| curvature_dependence | PRESENT | Curvature effects have been modeled and measured, but mechanics-model error versus curvature has not been converted into a breakdown boundary. |
| bending_stiffness_prediction | PRESENT | Predicting bending stiffness is already solved broadly and cannot constitute the thesis contribution by itself. |
| experimental_validation | PRESENT | Experimental validation exists across several families, although the Zhang RVE constitutive model itself lacks physical validation. |
| quantitative_prediction_error | PARTIAL | Numerical errors or fit statistics exist, but they are heterogeneous, often in-sample or selected-case results, and are not mapped into a common mechanics-error surface. |
| continuum_vs_discrete_validation | PRESENT | Meaningful continuum-versus-interface-resolving comparisons exist. Their limited parameter coverage and lack of declared tolerances prevent them from constituting a validity map. |
| tolerance_defined_validity_domain | ABSENT | This is the central residual gap within the supplied evidence, not a claim about all literature. |
| breakdown_boundary | ABSENT | Slip onset, full slip, tested-range limits, operational locking, and qualitative mismatch are not model-breakdown boundaries. |

## Fatal novelty conflicts

- Fatal to any claim of the first continuum or homogenized layer-jamming model: Zhang 2025 Mechanical Sciences, Zhang 2025 Frontiers of Mechanical Engineering, and Zhang 2025/2026 TAML.
- Fatal to any claim of the first predictive pressure–friction–slip or multilayer bending-stiffness model: Narang 2018 and Caruso 2023.
- Fatal to novelty based merely on pressure, curvature, layer thickness/count, cyclic hysteresis, experimental validation, or more FEA: these elements already occur across Caruso and Zhang-family work.
- Fatal to any claim of the first reduced dynamic or pressure-dependent stiffness-control model for a layer-jamming continuum robot: Yi 2024 and Fan 2026.
- No fatal conflict is established in the supplied full-text corpus against the strictly revised tolerance-defined discrete-to-continuum breakdown question.

## Unresolved questions

- Which exact published continuum model will be audited: Zhang's CLJM, Zhang's continuous-boundary curved-beam model, or a structural implementation of the Zhang RVE constitutive law?
- Can the selected Zhang model be reproduced reliably given reported equation, notation, and algorithm ambiguities in the source audits?
- What error measures and predeclared tolerances are scientifically justified for transition load, force–deflection response, stiffness, slip-front/interface state, and energy dissipation?
- Can physical layer count be varied independently at fixed total height, material pair, surface condition, envelope, and boundary condition?
- Which mechanism first causes tolerance failure: discrete interface jumps, transverse normal stress, nonuniform pressure, end/contact boundary layers, large curvature, friction-law inadequacy, or fixture compliance?
- Does a transferable dimensionless parameter already exist in partial-interaction, shear-lag, leaf-spring, laminated-beam, or homogenization literature?
- Is the continuum–discrete discrepancy larger than experimental uncertainty and large enough to matter for design or control?
- Can calibration and validation be separated without fitting friction and modulus from the same structural curves used to claim accuracy?
- Does the residual problem remain feasible at MSc scale after restricting geometry, outputs, and parameter axes?

## Track C requirements

### Partial-interaction and incomplete-interaction multilayer beam theories with finite interface compliance or friction.

**Why it matters:** These theories may already provide dimensionless interaction parameters, convergence criteria, or error thresholds connecting layerwise slip to equivalent beam action.

**Falsification condition:** A verified paper derives and validates a directly transferable criterion that predicts when a continuum/equivalent beam matches a discrete multilayer frictional model within a defined tolerance, making the layer-jamming study a routine parameter substitution.

**Suggested queries:**
- `TITLE-ABS-KEY(("partial interaction" OR "incomplete interaction") AND ("multilayer beam" OR "layered beam" OR "built-up beam") AND ("interlayer slip" OR "interface slip" OR "shear connection") AND (continuum OR homogenization OR discrete))`
- `TITLE-ABS-KEY(("partial interaction" OR "incomplete interaction") AND ("multilayer beam" OR "layered beam") AND (convergence OR "error bound" OR "range of validity" OR breakdown) AND (experiment OR validation))`

### Frictional laminated beams and stacked-sheet bending with explicit Coulomb interfaces.

**Why it matters:** This is the closest non-jamming physical analogue and may already compare equivalent continua with interface-resolved stacks under bending and progressive slip.

**Falsification condition:** A transferable study provides explicit-interface mechanics, an equivalent continuum, quantitative error versus layer count/load/preload, and a validated acceptance or breakdown boundary.

**Suggested queries:**
- `TITLE-ABS-KEY(("frictional layered beam" OR "layered beam with friction" OR "stacked sheets" OR "stack of sheets") AND (bending OR curvature) AND ("Coulomb friction" OR stick-slip OR "partial slip"))`
- `TITLE-ABS-KEY(("frictional layered beam" OR "stacked sheets") AND ("explicit interface" OR discrete) AND (continuum OR homogenization OR "equivalent beam") AND (error OR tolerance OR validity OR breakdown))`

### Multi-leaf spring equivalent and contact models.

**Why it matters:** Multi-leaf springs combine curved stacked sheets, interleaf friction, progressive slip, hysteresis, clamps, and strong boundary effects; mature engineering literature may already define when equivalent models fail.

**Falsification condition:** A general leaf-stack criterion maps error of an equivalent beam against explicit leaf contact as a function of leaf count, preload, curvature/load, and friction, and transfers to vacuum-clamped sheets without a new mechanics derivation.

**Suggested queries:**
- `TITLE-ABS-KEY(("multi-leaf spring" OR "multi leaf spring" OR "leaf spring stack") AND ("interleaf friction" OR "inter-layer slip" OR stick-slip) AND ("equivalent beam" OR continuum OR homogenization))`
- `TITLE-ABS-KEY(("multi-leaf spring" OR "leaf spring stack") AND ("explicit contact" OR discrete) AND (validation OR experiment) AND (error OR convergence OR validity OR limitation))`

### Shear-lag and imperfect-interface laminated beam theories with characteristic interaction length.

**Why it matters:** A characteristic slip-transfer length relative to layer thickness, beam depth, or span may already be the governing scale for continuum validity.

**Falsification condition:** A validated shear-lag parameter supplies a finite-layer error threshold directly applicable to pressure-dependent Coulomb interfaces, leaving only an application exercise.

**Suggested queries:**
- `TITLE-ABS-KEY(("shear lag" OR shear-lag) AND ("imperfect interface" OR "interface slip" OR "partial interaction") AND (multilayer OR laminate OR "layered beam") AND (bending OR flexure))`
- `TITLE-ABS-KEY(("shear lag" OR shear-lag) AND (layerwise OR discrete OR continuum OR homogenization) AND ("error estimate" OR convergence OR "range of validity") AND (slip OR friction))`

### Asymptotic homogenization, discrete-to-continuum convergence, and generalized continua for frictional layered media.

**Why it matters:** Formal homogenization may already define scale separation, convergence rates, or the need for micropolar/Cosserat internal lengths when discrete slip cannot be represented by a classical continuum.

**Falsification condition:** A theorem or validated model gives a usable finite-layer-count error estimate or breakdown criterion for ordered elastic layers with Coulomb slip that specializes routinely to the target beam.

**Suggested queries:**
- `TITLE-ABS-KEY(("layered media" OR "laminated structure" OR "stacked elastic layers") AND ("asymptotic homogenization" OR "discrete-to-continuum" OR "continuum limit") AND (friction OR slip OR "imperfect interface") AND ("error estimate" OR "convergence rate" OR validity))`
- `TITLE-ABS-KEY((micropolar OR Cosserat OR "generalized continuum") AND (laminated OR multilayer OR "frictional interfaces") AND (slip OR "Coulomb friction") AND ("internal length" OR breakdown OR validity))`

### Boundary-layer, support-contact, and nonuniform-pressure corrections in layered beams with slip.

**Why it matters:** The closest Zhang and Caruso papers identify supports, end effects, transverse normal stress, and pressure redistribution as principal mismatch sources. Prior structural mechanics may already quantify these boundary layers.

**Falsification condition:** A transferable correction theory predicts the boundary-layer extent and resulting global-response error with a verified threshold, eliminating the need for a new breakdown study except for routine validation.

**Suggested queries:**
- `TITLE-ABS-KEY(("layered beam" OR "multilayer beam" OR laminate) AND ("interface slip" OR friction) AND ("boundary layer" OR "end effect" OR "support contact" OR "contact pressure"))`
- `TITLE-ABS-KEY(("partial interaction" OR "frictional laminate") AND (boundary OR support OR clamp) AND (error OR correction OR validity) AND bending)`

### Quantitative model-form validity studies using explicit tolerance or error maps.

**Why it matters:** Relevant papers may not emphasize homogenization but may already perform the exact validation methodology under terms such as model-form error, applicability range, or convergence domain.

**Falsification condition:** A paper applies an explicit-interface/continuum/experiment triad to frictional multilayers and locates a declared-tolerance boundary over layer count and loading variables.

**Suggested queries:**
- `TITLE-ABS-KEY((multilayer OR laminated OR "stacked sheets") AND ("model-form error" OR "prediction error" OR "validity domain" OR "applicability range") AND (slip OR friction) AND bending)`
- `TITLE-ABS-KEY(("continuum approximation" OR homogenization OR "equivalent beam") AND ("explicit interface" OR layerwise OR discrete) AND (RMSE OR MAE OR tolerance OR "error map" OR "breakdown boundary"))`

## Search stop condition

Do not issue a final novelty verdict until Track C is completed with full-text screening. Stop immediately with FALSIFIED if one transferable verified paper contains all essential elements: a named continuum/equivalent representation, a genuinely interface-resolving reference, quantitative mechanics error over relevant finite layer count and loading variables, a declared acceptance tolerance, and a validated validity/breakdown boundary. Use SUBSTANTIALLY_NARROWED if adjacent theory supplies most of that framework but leaves one nontrivial vacuum-pressure, large-curvature, or boundary-condition coupling. If no kill is found after all Track C families are searched in multiple scholarly indexes, high-threat papers are citation-chained, and inaccessible full texts are recorded, retain only a provisional SURVIVES_WITH_REVISED_SCOPE result; search saturation still does not prove novelty.

## Recommended next action

Create the next non-overwriting verification round for Track C. First select one target continuum model—preferably Zhang's 2025 CLJM—and one explicit-interface baseline—preferably Caruso 2023 or a matched contact FEA. Then execute the Track C queries, acquire and verify every high-threat full text, and adjudicate whether any adjacent theory already supplies a transferable tolerance-defined discrete-to-continuum boundary. Do not begin experiments or claim novelty until that audit is complete.

## Evidence provenance

- `outputs/verification/D1-V001/direction_verification.json`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `1a39bfdecd7a6bc7001a258f81756aededc1e15b5ee68cedc8af5cea046ec731`
- `outputs/verification/D1-V001/verification_matrix.json`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `9e9d9471ac9488aea6e668be4b29c92d7d8a3291c80531f8abcf13500a0817bd`
- `outputs/verification/D1-V002/verification_matrix.json`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `2d8d0fdef3c8649631827717ab1d67cf262fa4dbd717f63e56aa7388806d3db1`
- `outputs/verification/D1-V002/adversarial_evidence_synthesis.md`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `3a40860317c608e11b733485c16615b007ed30bb433dfea7465828e6eacee49a`
- `outputs/verification/D1-V003/verification_matrix.json`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `759b9683bc97eb240abfb39557a1ff439a5fc82cc966393c6c9ff8fcccad44a6`
- `outputs/verification/D1-V003/FAN_2026_MODEL_AUDIT.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `a9b1ab01681064462f1cf2787e4d480061bf3f7adc8bc1f6b520c662b3da921f`
- `outputs/verification/D1-V003/ZHANG_2025_DEEPER_UNDERSTANDING_AUDIT.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `4b45b781437cc7c21c843b28161305505c372e1f9a88a1b5df3d04c8d4a2752a`
- `outputs/verification/D1-V003/D1-V003_EVIDENCE_MATRIX.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `3c170e4e189c84f70ee0ed2f847edb1e1884413cee28d57e93a164c004f4af79`
- `outputs/verification/D1-V003/D1-V003_LITERATURE_AUDIT.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `0161d22efb42c4109ab35ef6efe41ed81c0eaeef7028298191957867efe89318`
- `outputs/verification/D1-V003/D1-V003_SEARCH_LOG.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `d2b7134e8028265b270db95a043612fe34a7d4f8946b4479f1a1ad734cfecd6d`
- `docs/D1-V003_LITERATURE_AUDIT_PLAN.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `2078e6e9997c01d9c19ecd1f66d143bcebe55714454942c012d66ba8acf9b999`
- `docs/D1-V003_VALIDITY_GAP_SEARCH_PROTOCOL.md`
  - role: PRIOR_OR_POTENTIALLY_STALE_CONTEXT
  - sha256: `b6d69e7ed922562ffaf91042fd450f3ac5fb64b32007a4604a4fa59050154476`
- `docs/LAYER_JAMMING_MODEL_COMPARISON.md`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `9eba654b14fa5379e6a5991a3fefb612d7e6ece225a39d4d7d4ace0ac41df6b9`
- `docs/RESEARCH_STATE.md`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `d511973544a466ce6fc16b6c1f5785ac7ac7de2919ddeb543d3b7492aec07e26`
- `docs/RESEARCH_LOG.md`
  - role: CURRENT_OR_HISTORICAL_EVIDENCE
  - sha256: `95292229f8309fdc6c10a141a8abd2157688400b3df6b19d267095eab41bebca`
