# Run status: PAUSED (user asked to stop and save)

Paused at the end of step 3 of 8. Everything is committed on branch `claude/tabulate-writing-patterns-vx5oxh`.

## Done
1. Brief (BRIEF.md, with errata E1-E5), fixtures extracted verbatim from the session, append-only log (log.md, merged from log/*.md by merge_log.py).
2. Claims index kb/claims.md (80 claims, 17 decision-relevant). Ruler facts.json (105 facts, coverage check PASS). Scorer tools/score.py (25/25 self-tests). Dev set cases/dev (R1-R3 real, M1-M5 with 15 planted errors). Holdout cases/holdout (H1-H6, 14 planted, checksummed in cases/HOLDOUT_SHA256).
3. Baseline (current way: LLM reviewer reads spec + draft), 3 reps on dev: **F1 = 1.000 in all 3 reps; 8.80 s per draft on average (7.85-9.94); about 12k tokens per draft.**

## Not done
- Judge grading (judge-1a: claims + scorer; judge-1b: ruler + ground truth + test-set fairness). Both were stopped with no output. Their claim sheets are ready in judge/claims_for_judge-1a.md and judge/claims_for_judge-1b.md.
- Budget note, planner, pilot build, pilot grading, extension, final measurement on holdout, final judge, report.

## To resume
Re-dispatch judge-1a and judge-1b with the same claim sheets, then continue from step 4 (planner). The ITEMS.md statuses show where each item stands.

## Early observation (ungraded, not a finding)
On dev, the current way is already perfectly accurate, so the accuracy measure cannot improve, only tie. The session's real time loss was not verification (~9 s per draft) but producing model rewrites that could never pass the human-authorship gate, plus a ~196 s external round trip per submission.
