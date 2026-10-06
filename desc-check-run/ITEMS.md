# Master list of open items (coordinator-owned)

| ID | Item | Owner | Status | Notes |
|---|---|---|---|---|
| I-01 | Brief written | coordinator | done | BRIEF.md |
| I-02 | Index knowledge base / extract session claims | worker-kb | done | |
| I-03 | Build facts.json ruler from spec_A | worker-facts | done | |
| I-04 | Build tools/score.py + tools/timeit.sh | worker-scorer | done | |
| I-05 | Build dev cases + GT (R1-R3, M1-M5) | worker-dev | done | needs I-03 |
| I-06 | Build holdout cases + GT (H1-H6) | worker-holdout | done | needs I-03 |
| I-07 | Judge: grade decision claims, ruler, GT, scorer | judge-1a/1b | dropped: run closed by user before grading | needs I-02..I-06 |
| I-08 | Baseline: LLM reviewer x3 on dev | worker-base-1..3 | done (F1 1.000 x3, 8.80 s/draft) | |
| I-09 | Budget note after baseline | budget-1 | dropped: run closed by user after baseline | |
| I-10 | Planner: breakdown, ceiling, designs | planner | dropped: run closed by user after baseline | |
| I-11 | Coordinator picks design | coordinator | dropped: run closed by user after baseline | |
| I-12 | Build pilot slice | worker-build | dropped: run closed by user after baseline | |
| I-13 | Measure pilot (old vs new) | worker-measure | dropped: run closed by user after baseline | |
| I-14 | Judge grades pilot | judge-2 | dropped: run closed by user after baseline | |
| I-15 | Extend + re-measure | worker-build/measure | dropped: run closed by user after baseline | |
| I-16 | Final: old on holdout x3, new on dev+holdout | workers | dropped: run closed by user after baseline | |
| I-17 | Judge grades final | judge-3 | dropped: run closed by user after baseline | |
| I-18 | Final budget report | budget-2 | dropped: run closed by user after baseline | |
| I-19 | Limitations file + report | coordinator | done (REPORT.md, limitations.md) | |
