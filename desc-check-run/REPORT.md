# Final report (run closed early at the user's request)

## Result in one line
The target was missed. No new method was built or measured. The run stopped after measuring the current way, which was already accurate (found 15/15 planted errors) and fast (~9 s per draft), so there was almost nothing left to save in the step a tool is allowed to do.

## What the run decided
- **Target:** checking that a person's own-words description still matches the spec (missing, wrong or invented facts). Getting model-written text past the AI detector was excluded, because the checker requires the person's own words.
- **Time measure:** seconds per draft, from opening the draft to writing the list of issues.
- **Accuracy measure:** F1 of found issues against known answers (1.0 = everything found, no false alarms).
- **Test set:** 8 dev drafts (the original spec, rewrites B and C, and 5 copies with 15 planted errors) and 6 held-back drafts (14 planted errors). The held-back drafts were never used.

## Before and after
| | Runs | Accuracy (F1) | Time per draft | Tokens per draft |
|---|---|---|---|---|
| Current way (model reviewer) | 3 | 1.000, 1.000, 1.000 (no spread) | 9.94 / 8.60 / 7.85 s (mean 8.80) | ~12k (estimate) |
| New way | 0 | not built | not built | not built |

**Reduction achieved:** none. **Ceiling:** not computed by a planner (the step was not run). The coordinator's ungraded estimate is that verification can save at most ~9 s per draft. The session's real loss was elsewhere: two rewrites that could not pass the authorship rule, and a ~196 s round trip per checker submission.

## Findings
None was graded by the judge: both judges were stopped before reporting. So **no finding counts as accepted, and none was disproved.** Ungraded observations:
- Rewrites B and C kept all 105 facts. Two workers agree on B.
- The planted errors may be too easy (all caught by every run).

## Cost (from budget/costs.csv; the budget keeper never ran)
10 agents started, 8 finished, about 964,000 tokens, about 25 minutes of run time.

## Limitations
See limitations.md (L-001 to L-010). The main ones: the real checker and the hidden tests are unreachable, your writing time can't be measured, and the run was closed before judging, designing or building.
