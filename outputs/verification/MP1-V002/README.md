# MP1-V002

Targeted citation-chasing round for the mentor-proposed NiTi wire-jamming direction.

> **Current state:** 8 targeted full texts are registered, screened, ingested, and present in `verification_matrix.json`.
> **Important:** the first audit is INTERIM. It may falsify the direction, but it may not declare final citation-chase survival before coverage closes.

## Targets

- T1 — superelastic NiTi wires themselves as the frictional contacting/slipping bundle;
- T2 — positive/internal pressure directly confining a metallic/NiTi wire bundle;
- T3 — coupled superelastic NiTi + inter-wire friction/slip + pressure + structural stiffness mechanics.

## Current 8-paper targeted set

The current matrix contains the targeted NiTi/cable mechanics papers selected after the Scopus T1-T3 search, including:

- Nitinol/steel strand hysteresis and inter-wire friction;
- superelastic SMA cable FE mechanics;
- SMA wire-rope mechanics;
- NiTiNOL wire-rope nonlinear response;
- cable internal-friction mechanics;
- cable bending/contact mechanics;
- braided NiTi microfilaments;
- NiTi superelastic micro-cables.

Canonical evidence:

- `outputs/verification/MP1-V002/verification_matrix.json`
- `outputs/verification/MP1-V002/verification_matrix.md`

## Phase A — interim targeted-threat audit

Compile:

```bash
python -m py_compile \
  app/ingestion/mp1_v002_targeted_threat_audit.py
```

Load environment:

```bash
set -a
source .env
set +a
```

Prepare:

```bash
python -m app.ingestion.mp1_v002_targeted_threat_audit \
  --prepare-only
```

If preparation passes:

```bash
python -m app.ingestion.mp1_v002_targeted_threat_audit
```

Canonical outputs:

- `TARGETED_THREAT_AUDIT.json`
- `TARGETED_THREAT_AUDIT.md`
- `TARGETED_THREAT_AUDIT_raw.json`

Allowed interim outcomes:

- `FALSIFIED`
- `SUBSTANTIALLY_NARROWED`
- `SURVIVES_CURRENT_FULL_TEXT_SET`
- `INCONCLUSIVE`

`SURVIVES_CURRENT_FULL_TEXT_SET` is NOT a final novelty lock.

## Phase B — initialize citation-coverage tracking

Only if the interim result is not already a direct falsification:

```bash
python -m py_compile \
  app/ingestion/mp1_v002_citation_coverage.py

python -m app.ingestion.mp1_v002_citation_coverage \
  --init
```

This creates:

- `citation_coverage.json`
- `CITATION_COVERAGE_STATUS.md`

The tracker requires backward and forward screening of the core protocol anchors and adds the high-priority V002 papers selected by the interim audit as backward-citation anchors.

## Recording coverage

For each required anchor/direction in `citation_coverage.json`, fill:

- `status`: `screened_no_high_threat` or `screened_candidates_found`;
- `database`: normally `Scopus`;
- `search_date`;
- `records_screened`;
- `included_candidate_ids`;
- `unresolved_high_threat_sources`;
- `notes`.

Also set top-level `search_cutoff_date`.

After each citation-screening batch:

```bash
python -m app.ingestion.mp1_v002_citation_coverage \
  --check
```

The stop condition remains OPEN until:

1. every required backward/forward direction is screened;
2. every new high-threat named source is resolved;
3. no unresolved high-threat source remains.

## Protocol guardrail

Do not treat any of the following as sufficient scientific novelty by themselves:

- NiTi instead of nylon;
- SMA instead of another actuator;
- a syringe/piston instead of an existing pump;
- a different robot platform;
- generic NiTi cable hysteresis without pressure-controlled contact mechanics.

The remaining MP1 question must survive as a distinct mechanics problem, not as component substitution.

## Protocol

- `docs/protocols/MP1-V002_TARGETED_CITATION_CHASING_PROTOCOL.md`

Do not fabricate a final V002 verdict before the citation-coverage stop condition is satisfied.
