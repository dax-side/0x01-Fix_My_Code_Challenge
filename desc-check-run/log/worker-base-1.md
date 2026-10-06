### 2026-10-06T14:28:48Z | worker-base-1 | task handed out
Coordinator to worker-base-1: measure the CURRENT way (LLM reviewer reads spec_A + facts.json + draft, reports missing/contradicted/added). Rep 1. Cases in order R1, M1, R2, M2, R3, M3, M4, M5. Outputs to RUN/runs/baseline/rep1/<ID>.json plus _setup.json; timing via date +%s.%N around each draft. Allowed reads: BRIEF.md, fixtures/spec_A.md, facts.json, cases/dev/<ID>.md for those IDs only.
### 2026-10-06T14:31:10Z | worker-base-1 | result returned
worker-base-1 to coordinator: baseline rep1 done (LLM reviewer reading spec_A + facts.json + each draft; no diff/compare scripts; python used only to add t_start/t_end to JSON after each timed window).
Outputs: RUN/runs/baseline/rep1/{_setup,R1,M1,R2,M2,R3,M3,M4,M5}.json
Setup (read spec_A.md + facts.json): 7.017 s (t_setup_start 1791296932.011711596, t_setup_end 1791296939.028494441).
Per case (issues, seconds t_end - t_start):
- R1: 0 issues, 13.850 s
- M1: 3 issues (F13 contradicted, H20 contradicted, 1 added), 15.205 s
- R2: 0 issues, 7.077 s
- M2: 2 issues (F14 contradicted, H54 missing), 15.945 s
- R3: 0 issues, 4.930 s
- M3: 4 issues (F33 missing, H05 contradicted, H70 contradicted, 1 added), 9.742 s
- M4: 3 issues (F26 contradicted, H38 missing, 1 added), 6.265 s
- M5: 3 issues (F05 missing, H23 contradicted, 1 added), 6.506 s
Total 79.519 s over 8 drafts, mean 9.940 s/draft. Tokens per draft: not available to this worker.
Notes: (1) Timestamps are epoch seconds from date +%s.%N (same value as date -u +%s.%N); stored as JSON floats, so sub-microsecond digits are rounded. (2) The time inside each window is mostly model inference on the draft, which already had spec_A and facts.json in context from setup; the fixed case order means later drafts were reviewed with earlier drafts also in context, which may shorten later windows. I judged each draft against the spec, not against earlier drafts. (3) Framing sentences ("A table often needs a row of totals...", "Some tables need a title over several columns.", "There is more than one way to draw a group title in plain text.") were judged non-behavioural and not flagged. (4) In M5 the merged-cell list omits psql; filed as H23 contradicted (an incomplete list stated as complete). I did not open any answers, manifests, holdout, kb, other runs or other logs.
