# P2 work packages

P1 planning only; packages are not executed here. Each M01–M39 has one primary owner in WP-A–D; WP-E is a reuse/reconciliation package.

## WP-A — Background, review method and measurement standards
- Primary paper assignments: M01, M02, M03, M04, M05, M38, M39
- Required depth: TARGETED/DEEP
- Inputs: P0 registry + matrix + outline
- Output: `outputs/literature/MP1_READING_PACK/01_NOTES/WP-A/` with one Research Note per paper plus section cross-links.
- Parallel execution: compatible with other packages after P0 registry read; WP-E waits for WP-A–D.
- Verification: PDF locator, SHA-256 from P0 registry, identity status, author-result/inference separation, conditions and limitations.
- Completion: all assigned papers have a note or an explicit `NOT_VERIFIED`/`BLOCKED_IDENTITY` record; mapped sections have evidence coverage and unresolved questions.
- Notes: M01 owner for review method; M02–M05 context; M38–M39 uncertainty terminology

## WP-B — Jamming mechanisms and prior art
- Primary paper assignments: M06, M07, M08, M09, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21
- Required depth: DEEP
- Inputs: P0 registry + PDFs + section plan
- Output: `outputs/literature/MP1_READING_PACK/01_NOTES/WP-B/` with one Research Note per paper plus section cross-links.
- Parallel execution: compatible with other packages after P0 registry read; WP-E waits for WP-A–D.
- Verification: PDF locator, SHA-256 from P0 registry, identity status, author-result/inference separation, conditions and limitations.
- Completion: all assigned papers have a note or an explicit `NOT_VERIFIED`/`BLOCKED_IDENTITY` record; mapped sections have evidence coverage and unresolved questions.
- Notes: Mechanism topology, pressure/contact/slip, model level, validation and limitations

## WP-C — Wire bundle, cable and TiNi mechanics
- Primary paper assignments: M22, M23, M24, M25, M26, M27, M28, M29, M30, M35, M36
- Required depth: DEEP
- Inputs: P0 registry + PDFs + M23 remediation gate
- Output: `outputs/literature/MP1_READING_PACK/01_NOTES/WP-C/` with one Research Note per paper plus section cross-links.
- Parallel execution: compatible with other packages after P0 registry read; WP-E waits for WP-A–D.
- Verification: PDF locator, SHA-256 from P0 registry, identity status, author-result/inference separation, conditions and limitations.
- Completion: all assigned papers have a note or an explicit `NOT_VERIFIED`/`BLOCKED_IDENTITY` record; mapped sections have evidence coverage and unresolved questions.
- Notes: M23 owner is HOLD; do not open or extract current canonical content. M36 is assigned here for hysteresis/mechanics support.

## WP-D — SMA-controlled friction and pressure actuation
- Primary paper assignments: M31, M32, M33, M34, M37
- Required depth: DEEP
- Inputs: P0 registry + PDFs + section plan
- Output: `outputs/literature/MP1_READING_PACK/01_NOTES/WP-D/` with one Research Note per paper plus section cross-links.
- Parallel execution: compatible with other packages after P0 registry read; WP-E waits for WP-A–D.
- Verification: PDF locator, SHA-256 from P0 registry, identity status, author-result/inference separation, conditions and limitations.
- Completion: all assigned papers have a note or an explicit `NOT_VERIFIED`/`BLOCKED_IDENTITY` record; mapped sections have evidence coverage and unresolved questions.
- Notes: Friction-control and actuator-transfer records separated from material constitutive records

## WP-E — Cross-paper reconciliation and handoff
- Primary paper assignments: M01, M06, M07, M09, M10, M16, M17, M18, M19, M20, M22, M24, M31, M32, M33, M38
- Required depth: DEEP
- Inputs: Completed WP-A–D notes
- Output: `outputs/literature/MP1_READING_PACK/01_NOTES/WP-E/` with one Research Note per paper plus section cross-links.
- Parallel execution: compatible with other packages after P0 registry read; WP-E waits for WP-A–D.
- Verification: PDF locator, SHA-256 from P0 registry, identity status, author-result/inference separation, conditions and limitations.
- Completion: all assigned papers have a note or an explicit `NOT_VERIFIED`/`BLOCKED_IDENTITY` record; mapped sections have evidence coverage and unresolved questions.
- Notes: No new sources; reconcile contradictions, scope and conditional gaps

## Assignment constraints
- M23 is assigned to WP-C as `HOLD / BLOCKED_IDENTITY`; no P2 content extraction until `P0_M23_REMEDIATION` closes.
- Do not treat review sources as substitutes for original equations/results.
- Reuse evidence records across sections through `target_thesis_sections`; do not duplicate extraction without a new locator or question.
