# D1-V003 Evidence Matrix

| Paper / Source | Source Type | Tests Failed (Threats) | Tests Passed (Defenses) | Threat Level | Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Zhang et al. 2025 (Mech. Sci. / 10.5194/ms-16-821-2025) | [VERIFIED FULL TEXT] | T1, T2, T3 (Proposes a continuum model) | T4 (Does not compare w/ discrete model), T5, T6, T7, T8, T9 | LOW | Establishes existence of continuum model, but does not define its limits. |
| Zhang et al. 2026 (TAML / 10.1016/j.taml.2025.100633) | [VERIFIED FULL TEXT] | T1, T2, T3 | T4, T5, T6, T7, T8, T9 | LOW | Applies equivalent continuum method for specific topology; no systematic error bound mapping. |
| Fan et al. 2026 (TCST / 10.1109/TCST.2026.3690756) | [METADATA ONLY] / [INFERENCE] | T1 (Dynamic model) | T2, T3, T4, T5, T6, T7, T8, T9 | LOW | Focuses on port-Hamiltonian control, not solid mechanics validity boundaries. |
| Multi-leaf spring literature (General) | [INFERENCE] (Web Search) | T2 (Interface slip) | T1 (Not layer jamming), T3, T8 (Rejects homogenization for slip) | NONE | Proves adjacent fields recognize the breakdown of homogenization, reinforcing the gap in layer jamming. |
| Partial interaction composite beams (General) | [INFERENCE] (Web Search) | T2 (Interface slip) | T1 (Not layer jamming), T8 (Defines thresholds for slip stiffness, but not for vacuum layer jamming) | NONE | Identifies methodology for defining limits (slip stiffness thresholds) but applied to different structures. |

## Threat Test Legend
- **T1:** Is it about layer/laminar jamming?
- **T2:** Does it explicitly represent inter-layer slip / friction?
- **T3:** Does it propose a continuum, homogenized, or equivalent model?
- **T4:** Does it explicitly compare the continuum model against a *discrete* (layer-by-layer) analytical or numerical model?
- **T5:** Does it systematically quantify the *error* between the continuum and discrete models?
- **T6:** Does it evaluate the model across a wide range of layer counts ($N$), including low $N$ (e.g., $N < 10$)?
- **T7:** Does it mathematically define a breakdown criterion or a dimensionless parameter governing validity?
- **T8:** Does it explicitly map the domain of validity (e.g., in a parameter space)?
- **T9:** Does it validate the breakdown boundary experimentally?
