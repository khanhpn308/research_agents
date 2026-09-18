# D1-V007 C04 semantic correction

## Scope

This note records a semantic correction discovered during review of the
current canonical C04 adversarial audit.

## Correction

The verified focal-paper evidence for paper_id `ca46dc062d` establishes
that the paper uses an explicit/adopted 5% maximum-displacement-error
threshold to define permissible deformation/rotation limits against a
discrete-contact reference.

However, the supplied evidence does **not** establish that this 5%
threshold was **predeclared a priori** before the relevant validation or
model-form error results were examined.

Therefore, until the audit is rerun with the corrected prompt semantics:

- do not treat `kill_test.predeclared_acceptance_tolerance = true` in
  the previous canonical C04 output as established;
- do not treat
  `four_link_chain_audit.discrepancy_to_predeclared_tolerance.supported = true`
  as established;
- interpret the focal paper as supporting an **explicit/adopted
  applicability threshold**, not a verified predeclared acceptance
  tolerance.

## Expected rerun interpretation

Unless another supplied verified-full-text source explicitly establishes
that the acceptance tolerance was fixed before validation/error
inspection, the corrected C04 run should set:

```text
kill_test.predeclared_acceptance_tolerance = false

four_link_chain_audit.discrepancy_to_predeclared_tolerance.supported = false
```

This correction does not reverse the current overall falsification
result. The prior run already had:

```text
experiment_tests_both_sides_of_boundary = false
transferable_to_vacuum_layer_jamming_without_new_mechanics = false
kill_condition_met = false
```

The correction therefore strengthens the surviving-gap interpretation
rather than changing the current no-kill conclusion.

## Required next action

Pull the updated audit script and rerun C04 with `--force` so that the
canonical JSON/Markdown outputs and provenance reflect the corrected
definition of **predeclared**.

After the rerun, the only remaining targeted literature action is the
named DOI:

`10.1061/JSENDH.STENG-13096`

Broad literature searching should remain stopped unless that targeted
audit reveals a new specifically named high-threat branch.
