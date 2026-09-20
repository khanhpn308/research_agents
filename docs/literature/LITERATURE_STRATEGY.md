# LITERATURE_STRATEGY.md

## Objective

The current literature search is not a general review of soft robotics.

It is a targeted novelty audit designed to find the closest prior work capable of falsifying P1:

> Validity Limits of a Homogenized Slip Model for High-Layer-Count Vacuum-Jammed Beams

## Search Principle

Search for concepts, not exact wording.

Do not conclude that a gap exists just because one exact phrase returns zero results.

Authors may use:
- continuum model
- continuous medium
- homogenized model
- homogenization
- equivalent model
- effective model
- reduced-order model
- constitutive model
- macroscopic model
- partial-interaction model
- shear-lag model

## Priority Queries

### Direct layer-jamming queries

```text
"layer jamming" "continuum model"
"layer jamming" homogenized
"layer jamming" homogenization
"layer jamming" "equivalent model"
"layer jamming" "reduced-order model"
"layer jamming" constitutive model
"layer jamming" "interlayer slip"
"layer jamming" "partial slip"
"layer jamming" "progressive slip"
"layer jamming" "full slip"
"layer jamming" "high layer count"
"layer jamming" "number of layers" model
"layer jamming beam" model
"layer jamming beam" slip
"laminar jamming" continuum
"laminar jamming" homogenized
```

### Validity / breakdown queries

```text
"layer jamming" "model validity"
"layer jamming" "model limitation"
"layer jamming" "large deformation"
"layer jamming" "large deflection"
"layer jamming" boundary effects
"layer jamming" contact pressure
"layer jamming" "slip transition"
"layer jamming" hysteresis
```

### Broader mechanics queries

```text
"frictional laminated beam" "interlayer slip"
"multilayer beam" friction slip model
"laminated beam" "partial interaction"
"layered beam" "interlayer slip"
"multilayer beam" homogenization friction
"laminated beam" homogenized slip
"partial interaction beam" slip
"shear lag" multilayer beam friction
```

## Time Filter

Prioritize:
- 2025
- 2026

Older papers remain relevant when they are foundational or are direct prior work.

## Forward Citation Tracking

Mandatory seeds:

### Narang et al. 2018

DOI:
`10.1002/adfm.201707136`

### Caruso et al. 2023

DOI:
`10.1016/j.ijmecsci.2023.108325`

Goal:

```text
foundational paper
→ later citing papers
→ filter 2025–2026
→ screen
→ identify closest descendants
```

## Citation Sources

Use the union of:
- Google Scholar
- publisher Citing Literature pages
- Crossref metadata/citation links where useful
- Scopus
- Web of Science
- ResearchGate
- publisher article pages

Do not add citation counts across databases.

Different citation counts are expected because coverage differs.

## Recommended Bulk Workflow

For large forward-citation sets:

```text
Publish or Perish
→ retrieve citing works
→ export CSV / RIS
→ filter year
→ deduplicate DOI/title
→ keyword rank
→ manual scientific screening
```

Suggested filenames:

```text
data/search_results/Narang2018_forward_citations_2025_2026.csv
data/search_results/Caruso2023_forward_citations_2025_2026.csv
```

## Screening Criteria

### Include if a paper materially addresses one or more of:

- layer / laminar jamming mechanics
- continuum / homogenized / constitutive modeling
- multilayer slip
- partial / progressive / full slip
- high layer count
- equivalent / reduced-order beam modeling
- stiffness prediction
- large-deformation effects
- boundary / contact-pressure effects
- experimental validation of the above

### Exclude or deprioritize if:

- only general soft-gripper design
- only application demonstration
- no relevant mechanics
- only controller tuning with no new jamming mechanics
- granular jamming unrelated to the layer-jamming question
- review paper with no new mechanics contribution

## Ranking Heuristic

Highest-priority paper contains multiple of:

```text
layer jamming
+
beam / multilayer structure
+
continuum / homogenized / constitutive model
+
slip / friction
+
experimental validation
```

## Current Highest-Priority Papers

1. **A continuum-based model for a layer jamming beam** — Zhang et al., 2025
2. **Toward a deeper understanding of layer jamming structures** — Zhang et al., 2025
3. **Modeling, Control, and Stiffness Regulation of Layer Jamming-Based Continuum Robots** — Fan et al., 2026

## Novelty Standard

P1 is not defensible merely because exact wording is absent.

P1 survives only if the closest literature does **not** already cover the combination of:

```text
large/high layer count
+
continuum/homogenized representation
+
interlayer slip mechanics
+
experimental validation
+
validity/breakdown limits
```
