# D1-V009 — Late-Found Adjacent-Mechanics Audit Plan

> **Status:** SETUP ONLY — target paper not yet registered/ingested in the repository
> **Purpose:** audit one high-relevance paper found after the D1-V008 provisional novelty lock without rewriting prior rounds.

## Target

Adhikary, D. P.; Mühlhaus, H.-B.; Dyskin, A. V. (1999).

**Title:** *Modelling the large deformations in stratified media—the Cosserat continuum approach*

**Journal:** *Mechanics of Cohesive-Frictional Materials*, 4, 195–213.

This is a late-found adjacent-mechanics source. It is not a vacuum layer-jamming paper, but it is highly relevant because it develops an equivalent continuum for layered media with layer bending stiffness, large deformation, frictional/sliding interfaces, and possible interface opening.

## Why D1-V009 instead of rewriting earlier rounds?

The paper was discovered after D1-V008 reached its stopping condition. Preserve provenance:

    D1-V008
    → provisional novelty lock
    → late-found relevant source
    → D1-V009 independent post-lock audit

Do not retroactively insert this paper into C01/C02/C03 and then treat it as if it had been part of those original decisions.

## Current surviving P1 to attack

> For one specified reduced/continuum vacuum-layer-jamming beam model under quasi-static planar bending, define output-specific predeclared model-form acceptance tolerances and determine experimentally validated validity/breakdown boundaries against an interface-resolving/full-layer reference, while explicitly accounting for vacuum-pressure-controlled normal contact, friction/slip evolution, and, where necessary, pressure redistribution or layer separation.

## Primary falsification question

Does Adhikary et al. (1999) already establish enough of the reduced/continuum-versus-discrete validity framework to falsify or materially narrow the final P1?

The audit must distinguish mechanics lineage/theoretical precedent from the specific surviving scientific contribution.

## Mandatory mechanics overlap audit

Explicitly determine whether the paper establishes:

- equivalent/smeared continuum treatment of layered media;
- generalized/Cosserat continuum mechanics;
- layer bending stiffness represented through couple stresses/internal rotations;
- large-deformation formulation;
- elastic or elastoplastic interface behavior;
- Coulomb / Mohr–Coulomb slip criterion;
- interface opening or separation;
- finite-element implementation;
- quantitative analytical or experimental validation.

## Mandatory kill-chain audit

Test the paper against:

    named reduced / continuum model
    → interface-resolving or discrete reference
    → quantitative model-form discrepancy
    → finite parameter / layer-discreteness sweep
    → PREDECLARED output-specific acceptance tolerance
    → tolerance-defined validity / breakdown boundary
    → experiment intentionally sampling both sides of that boundary
    → transfer to vacuum layer jamming without materially new mechanics

A kill requires the complete relevant chain, not merely sophisticated continuum mechanics.

## Semantic guardrails

1. Observed error is not a predeclared tolerance unless the source establishes that the criterion was fixed before the validation/error result was inspected.
2. Buckling, yielding, opening, delamination, or a load fraction at which geometric nonlinearity matters are physical/assumption transitions, not automatically tolerance-defined model-validity boundaries.
3. Matching an Euler buckling solution is useful verification, but is not automatically a reduced-continuum-versus-explicit-interface error study.
4. Prior experiments cited for context are not automatically validation experiments of the proposed continuum model.

## Possible outcomes

- FALSIFIES_FINAL_P1
- SUBSTANTIALLY_NARROWS_FINAL_P1
- SURVIVES_LATE_FOUND_TARGET
- INCONCLUSIVE

## Local execution order after pulling

Use the actual local path to the PDF:

    python -m app.ingestion.add_paper "/path/to/Adhikary_1999.pdf" \
      --type verification \
      --verification-id D1-V009 \
      --reason "Late-found adjacent-mechanics target: equivalent/Cosserat continuum for layered media with large deformation, frictional slip, bending stiffness and interface opening. Post-lock audit against final P1."

Then screen it:

    python -m app.ingestion.screen_paper \
      --id <PAPER_ID> \
      --decision include \
      --reason "High-relevance post-lock adjacent-mechanics source for continuum layered media, frictional slip, large deformation and interface separation; include for D1-V009 falsification audit."

Then:

    python -m app.ingestion.ingest_papers --limit 1
    python -m app.ingestion.validate_evidence
    python -m app.ingestion.build_verification_matrix --verification-id D1-V009
    python -m app.ingestion.d1_v009_late_found_adjacent_audit --prepare-only
    python -m app.ingestion.d1_v009_late_found_adjacent_audit

Use --force only when deliberately replacing an existing canonical D1-V009 audit.

## Expected canonical outputs

    outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.json
    outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT.md
    outputs/verification/D1-V009/LATE_FOUND_ADJACENT_AUDIT_raw.json
    outputs/verification/D1-V009/late_found_runs/<timestamp>/

## Post-audit decision rule

- FALSIFIES_FINAL_P1 → reopen research architecture.
- SUBSTANTIALLY_NARROWS_FINAL_P1 → revise P1/title/RQ before implementation.
- SURVIVES_LATE_FOUND_TARGET → retain the provisional lock, but incorporate Adhikary 1999 into the theoretical lineage and literature review.
- INCONCLUSIVE → perform only the targeted follow-up identified by the audit; do not automatically reopen broad searching.
