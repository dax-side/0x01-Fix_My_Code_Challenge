# Limitations (run paused after step 3)

| ID | Limitation | What it affected |
|---|---|---|
| L-001 | No knowledge base exists besides this session's conversation. It was extracted verbatim from the transcript into fixtures/. The coordinator's own search was name-only to depth 4 (errata E5). worker-kb's fuller search found nothing either. | The claims base is limited to 4 assistant replies and the checker output. |
| L-002 | The external Description Quality checker and its AI detector cannot be run from here. | Real-checker pass/fail cannot be measured. Rebuilding is scoped to draft verification (D-001). |
| L-003 | The hidden tests and implementation for footer/headergroups are not available. tabulate is not installed, and the only local tabulate material is a 0.9 type stub without these arguments. | spec_A is the reference by the user's authorship and cannot be verified against code (errata E3/E4). |
| L-004 | The time a person spends writing an own-words draft cannot be measured. | The time measure covers verification only. |
| L-005 | The git push initially failed with a 403 because the GitHub App lacked access. **Resolved**: later pushes succeeded. | Durability between checkpoints only. |
| L-006 | Per-draft tokens inside a multi-draft agent run cannot be split exactly. Per-agent totals come from completion notices. | Token cost per draft is an estimate (agent total / drafts). |
| L-007 | The dev-set baseline is already at F1 = 1.000 in 3/3 reps. | A new method can at best tie on dev accuracy. The dev mutants may be too easy (ungraded; judge-1b was stopped before ruling). |
| L-008 | Parallel agents share one scratchpad. worker-base-3's timestamp helper was overwritten mid-run; values were checked and verdicts were not affected. | Timing hygiene for rep3 case R2 and the first M1 t_start. |
| L-009 | Style claims K01-K35 can only be tested on readme_excerpt.md. The fixture extraction from the transcript was not re-checked by an independent agent. No Markdown renderer is installed, so K40 cannot be tested. | Grading of those claims. |
| L-010 | The run was paused on the user's request ("stop for now and save all work"). judge-1a and judge-1b were stopped before producing grades. | No claim has a judge's grade yet. Steps 4-8 have not been done. Nothing in this run counts as an accepted finding yet. |
| L-011 | The budget keeper was never started (planned for after the baseline; the run was paused first). Spending was logged by the coordinator but never independently checked or flagged. | Nobody warned that the run cost ~80x the per-draft cost of the step being measured. |
