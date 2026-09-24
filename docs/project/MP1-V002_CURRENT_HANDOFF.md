# MP1-V002 — Current Handoff

> **Purpose:** fast handoff for continuing MP1-V002 in a new chat without reconstructing the full history.  
> **Status:** MP1-V002 ACTIVE. Interim full-text audit has substantially narrowed the direction; citation coverage is still open.  
> **Important:** D1/M1 remains the preserved thesis direction until MP1 survives final adjudication.

## 1. Current scientific state

MP1 began from the mentor-proposed architecture:

```text
superelastic NiTi / metallic wire bundle
+ positive-pressure confinement
+ inter-wire frictional jamming
+ variable bending stiffness
+ optional SMA-driven syringe/piston pressure source
```

MP1-V001 formally returned:

```text
STATUS      = PIVOT_TO_MECHANICS_CORE
CONFIDENCE  = high
```

Broad claims already closed or substantially pre-empted:

- wire/fiber jamming;
- positive-pressure jamming;
- SMA + jamming in one device;
- compact/onboard pressure source;
- SMA-driven pump/syringe as a stand-alone novelty claim;
- mechanical piston-driven jamming;
- NiTi tendons/wires merely being present in a variable-stiffness robot.

The surviving question moved to mechanics rather than component combination.

## 2. MP1-V002 interim result

The current 8-paper full-text threat set produced:

```text
STATUS      = SUBSTANTIALLY_NARROWED
CONFIDENCE  = high
```

Interpretation:

### T1 — NiTi wires as contacting/slipping frictional bundles

**Substantially closed.**

Prior literature already establishes NiTi/Nitinol strands, ropes, cables, and braided microfilaments with:

- inter-wire/inter-filament contact;
- friction and micro-slip;
- hysteresis and damping;
- superelastic / phase-transformation response;
- structural stiffness effects.

Therefore, `NiTi + inter-wire friction + hysteresis` is not a defensible novelty claim by itself.

### T2 — actively pressure-controlled NiTi/metallic wire bundle

**Still open in the current full-text set.**

The present evidence includes:

- passive contact pressure caused by helix geometry;
- axial-load-induced radial pressure;
- manufacturing/preforming pressure;
- fixed preload or confinement;

but has not yet established:

```text
actively varied positive / radial / transverse confinement pressure
→ changes wire-wire normal force
→ changes friction / stick-slip state
→ changes bending or flexural stiffness
```

for a NiTi wire bundle.

### T3 — NiTi superelasticity coupled with pressure-controlled contact/slip/stiffness

**Substantially narrowed.**

NiTi phase transformation + inter-wire friction is already known. The remaining candidate contribution is narrower:

```text
actively varied confinement pressure
+
NiTi phase transformation / superelasticity
+
inter-wire contact / stick-slip
+
bending stiffness / hysteresis
```

## 3. Current provisional mechanics core

The strongest surviving question is:

> Does actively varied radial/transverse confinement pressure create pressure-dependent stick/slip, bending stiffness, and hysteresis in a superelastic NiTi wire bundle that cannot be reproduced adequately by an existing elastic-fiber/contact model using only substituted material modulus and friction parameters?

### Kill test

MP1 should be killed or narrowed again if prior work shows either:

1. actively pressure-controlled NiTi/metallic wire-bundle stiffness mechanics already exist; or
2. the proposed response is adequately reproduced by an existing elastic-fiber/contact framework with only parameter substitution.

## 4. Pressure classification used in V002

Every pressure-related source must be classified as:

```text
P1 = passive contact pressure
     caused by helix geometry, axial load, bending, or deformation

P2 = fixed preload / fixed confinement
     imposed but not varied as an operational control variable

P3 = actively varied confinement pressure
     pressure is an independent control variable during operation
```

Only **P3** is a direct threat to the currently surviving pressure-controlled mechanics question.

## 5. Current 8-paper targeted full-text set

The V002 matrix already includes the targeted NiTi/cable mechanics sources selected after Scopus T1-T3 searching, including:

- Carboni et al. — Nitinol/steel strand hysteresis and inter-wire friction;
- Liu et al. — superelastic SMA cable mechanics / simplified FE;
- Vahidi et al. — single/double-helix SMA wire ropes;
- Niu/Chen lineage — Nitinol wire-rope nonlinear response;
- Xin Liu — cable vibration considering internal friction;
- Tjahjanto et al. — cable-core bending/contact mechanics;
- Liu et al. — braided NiTi microfilaments;
- Silva et al. — NiTi SMA superelastic micro-cables.

Key current conclusion from this set:

```text
NiTi + inter-wire friction/slip + hysteresis = known
active pressure control of NiTi bundle stiffness = not established in current set
```

## 6. Citation-chasing protocol now in force

Protocol:

`docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`

No broad keyword search should be reopened unless a later adjudication explicitly requires it.

Required coverage:

### Backward citation branches

1. **B01 — Carboni et al.**
   - DOI: `10.1061/(ASCE)EM.1943-7889.0000852`
   - Direction: References / backward

2. **B02 — Vahidi et al.**
   - DOI: `10.1080/15376494.2021.1955313`
   - Direction: References / backward

3. **B03 — Xin Liu thesis**
   - Title: *Cable Vibration Considering Internal Friction*
   - University of Hawai‘i, M.S. thesis, 2004
   - DOI: none
   - Direction: References / backward

4. **B04 — Tjahjanto et al.**
   - DOI: `10.1115/OMAE2017-62553`
   - Direction: References / backward

5. **B05 — braided NiTi microfilaments**
   - DOI: `10.1016/j.matlet.2026.141544`
   - Direction: References / backward

6. **B06 — Silva et al.**
   - DOI: `10.3390/s22208045`
   - Direction: References / backward
   - Scopus does not expose the full reference list; use the publisher reference list:
     `https://www.mdpi.com/1424-8220/22/20/8045#References`

### Forward citation branches

1. **F01 — Bai et al. 2022**
   - DOI: `10.3390/app12073582`

2. **F02 — Liu et al. 2021**
   - DOI: `10.1109/LRA.2021.3097255`

3. **F03 — Zhang & Yao 2026**
   - DOI: `10.5194/ms-17-481-2026`
   - Current Scopus result: **0 forward citations**
   - Record this as a completed zero-result branch.

4. **F04 — Takashima et al. 2022**
   - DOI: `10.20965/jrm.2022.p0466`

5. **F05 — Matsumoto et al. 2024**
   - DOI: `10.1299/mej.24-00130`
   - ResearchGate currently reports 1 citation.
   - Need metadata of the **citing paper**, not another copy of the Matsumoto abstract.

6. **F06 — Wang et al. 2024**
   - DOI: `10.1108/IR-11-2023-0305`
   - Current Scopus result: **0 forward citations**
   - Record this as a completed zero-result branch.

## 7. Citation exports already collected

Current working set contains:

```text
B01.csv
B02.csv
B03.csv
B04.csv
B05.csv

F01.csv
F02.csv
F04.csv
```

Observed record counts:

```text
B01 = 57
B02 = 33
B03 = 4
B04 = 9
B05 = 10

F01 = 14
F02 = 51
F04 = 9

Total CSV records = 187
```

Still to preserve manually:

```text
B06_silva_publisher_references.txt
F03_zhang_yao_zero.txt
F05_matsumoto_researchgate.txt
F06_wang_zero.txt
```

CSV is not mandatory for coverage. A publisher reference list, secondary-document record, or manual zero-result record is acceptable if provenance is explicit.

## 8. Recommended repository layout for citation exports

```text
data/search_exports/MP1-V002/raw/backward/
    B01.csv
    B02.csv
    B03.csv
    B04.csv
    B05.csv
    B06_silva_publisher_references.txt

data/search_exports/MP1-V002/raw/forward/
    F01.csv
    F02.csv
    F03_zhang_yao_zero.txt
    F04.csv
    F05_matsumoto_researchgate.txt
    F06_wang_zero.txt
```

Zero-result note example:

```text
Anchor DOI: 10.5194/ms-17-481-2026
Database: Scopus
Search date: 2026-09-24
Direction: forward
Records found: 0
Conclusion: No forward citations available in Scopus at the search cutoff date.
```

## 9. Screening rubric for citation candidates

Do not ingest all citation records.

Classify metadata candidates as:

```text
EXCLUDE
→ unrelated to T1/T2/T3

KEEP_METADATA
→ relevant mechanics but not a direct threat

GET_FULL_TEXT
→ plausible threat to the remaining T2/T3 mechanics

POTENTIAL_KILL_PAPER
→ direct threat to the surviving mechanics core
```

A strong kill candidate should approach:

```text
actively varied confinement pressure
+
metallic / NiTi wire bundle
+
inter-wire normal-force / friction / stick-slip mechanics
+
bending / flexural stiffness
```

or:

```text
NiTi phase transformation
+
pressure-controlled contact/slip
+
structural stiffness / hysteresis
```

## 10. Important cable-mechanics lineage already exposed

The Xin Liu thesis confirms a prior cable-mechanics lineage involving:

- Lanteigne (1985) — helically armored cable response;
- Sauter & Hagedorn (2002) — hysteresis of wire cables in Stockbridge dampers;
- Sauter (2003) — dynamic characteristics of slack wire cables;
- Vinogradov & Atatekin (1986);
- Zhong (2003) — frictional bending model;
- related work on wire slippage and curvature-dependent flexural rigidity.

These are relevant mechanics sources, but passive/internal radial pressure or friction does not automatically close the active-pressure question.

## 11. Citation coverage tracker

Current tracker script:

`app/ingestion/mp1_v002_citation_coverage.py`

Commands:

```bash
python -m app.ingestion.mp1_v002_citation_coverage --check
```

Before citation screening, the tracker reported an open stop condition with:

```text
6 required forward branches
6 required backward branches
+ unresolved named high-threat sources
```

The tracker should only be marked complete after each required branch is actually screened and any high-threat candidate is either resolved or explicitly left unresolved.

## 12. Immediate next action

Do **not** download dozens of full texts yet.

Next workflow:

```text
complete B06/F03/F05/F06 provenance files
→ normalize/deduplicate citation metadata
→ screen titles + abstracts
→ classify EXCLUDE / KEEP_METADATA / GET_FULL_TEXT / POTENTIAL_KILL_PAPER
→ download only high-threat full texts
→ register those new full texts under MP1-V002
→ ingest
→ rebuild verification matrix
→ re-audit / final V002 adjudication after coverage closes
```

## 13. Guardrails

Do not claim novelty from:

- NiTi instead of nylon;
- wire instead of fiber;
- SMA instead of another actuator;
- syringe/piston instead of an existing pump;
- a different robot platform;
- generic NiTi cable hysteresis;
- passive cable contact pressure;
- fixed preload alone.

Do not equate:

```text
NiTi wire rope friction
==
pressure-controlled NiTi jamming
```

and do not equate:

```text
passive radial contact pressure
==
actively varied confinement pressure
```

## 14. Canonical project files

- `docs/project/MP1_MENTOR_PIVOT_CURRENT.md`
- `docs/project/MP1-V002_CURRENT_HANDOFF.md`
- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.md`
- `outputs/verification/MP1-V001/CORE_PRIOR_ART_AUDIT.json`
- `outputs/verification/MP1-V002/verification_matrix.json`
- `outputs/verification/MP1-V002/verification_matrix.md`

When continuing in a new chat, read this file first, then the V002 protocol, then the latest citation-coverage output.


## 15. Continuation checkpoint — 2026-09-24 citation provenance

A follow-on citation-provenance pass completed the four manual artifacts that were still open in Section 7.

Preserved on branch `mp1-v002-citation-provenance-20260924`:

```text
data/search_exports/MP1-V002/raw/backward/
    B06_silva_publisher_references.txt

data/search_exports/MP1-V002/raw/forward/
    F03_zhang_yao_zero.txt
    F05_matsumoto_researchgate.txt
    F06_wang_zero.txt
```

### B06 interim metadata screen

Silva et al. (2022) exposes 22 publisher references.

Current pressure classification for the branch remains:

```text
P1/passive cable contact pressure and geometry = present
P3 actively varied confinement pressure         = not identified
```

Two references are promoted for later full-text review because they matter to the parameter-substitution kill test:

1. Reedlunn, Daly & Shaw (2013), Part II — DOI `10.1016/j.ijsolstr.2013.03.015`
   - reason: hierarchical NiTi cable subcomponent/contact mechanics and phase-transformation response;
   - current disposition: `GET_FULL_TEXT`;
   - no P3 pressure-control signal in metadata.

2. Fang et al. (2019) — DOI `10.1016/j.engstruct.2019.01.049`
   - reason: superelastic NiTi cable hysteretic modelling and an effective numerical modelling approach;
   - current disposition: `GET_FULL_TEXT`;
   - no P3 pressure-control signal in metadata.

Other cable-specific B06 references remain `KEEP_METADATA` unless full text exposes active radial/transverse confinement. Bulk NiTi material/fatigue/R-phase references are not direct threats to the surviving T2/T3 mechanics and can be `EXCLUDE` from this branch.

### F05 resolved

The single citing work for Matsumoto et al. (2024) is:

```text
Kazuto Takashima; Yuma Hirose; Hidetaka Suzuki; Hiroki Cho
Pick-and-Place Motion by Two-Robot-Arm System Equipped with
Variable-Stiffness and Deformable Link Using Shape-Memory Alloy
and Jamming Transition Phenomenon
Journal of Robotics and Mechatronics 38(2):646-657 (2026)
DOI: 10.20965/jrm.2026.p0646
```

Screening disposition:

```text
KEEP_METADATA
```

Reason: this extends the SMA + jamming robot-link lineage but does not establish actively varied radial/transverse confinement of a metallic/NiTi wire bundle controlling inter-wire normal force, stick-slip, and flexural stiffness.

### F03 / F06

The previously obtained Scopus zero-result checks are now preserved as provenance records:

```text
F03  DOI 10.5194/ms-17-481-2026  forward citations = 0
F06  DOI 10.1108/IR-11-2023-0305 forward citations = 0
search cutoff = 2026-09-24
```

These are protocol-bounded zero results, not universal novelty evidence.

### Remaining execution dependency

The 187 CSV records (B01-B05, F01, F02, F04) exist in the local working set described above but are not present on GitHub or in the connected Project/Library file surface. Therefore the deterministic metadata-screening script cannot be executed from the connected environment without inventing records.

The next exact local command remains:

```bash
python -m app.ingestion.mp1_v002_screen_citation_metadata
```

Expected inputs:

```text
data/search_exports/MP1-V002/raw/backward/B01.csv ... B05.csv
data/search_exports/MP1-V002/raw/forward/F01.csv F02.csv F04.csv
```

After that command, inspect:

```text
outputs/verification/MP1-V002/citation_screening/METADATA_SCREENING.csv
outputs/verification/MP1-V002/citation_screening/FULL_TEXT_SHORTLIST.csv
```

Do not download full text for the full 187-record set. Only resolve `POTENTIAL_KILL_PAPER` and `GET_FULL_TEXT` candidates, including the two B06 modelling/mechanics candidates above.
