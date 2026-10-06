# Master list of open items (coordinator-owned)

| ID | Item | Owner | Status | Notes |
|---|---|---|---|---|
| I-01 | Brief written | coordinator | done | BRIEF.md |
| I-02 | Index knowledge base / extract session claims | worker-kb | done | |
| I-03 | Build facts.json ruler from spec_A | worker-facts | done | |
| I-04 | Build tools/score.py + tools/timeit.sh | worker-scorer | done | |
| I-05 | Build dev cases + GT (R1-R3, M1-M5) | worker-dev | done | needs I-03 |
| I-06 | Build holdout cases + GT (H1-H6) | worker-holdout | done | needs I-03 |
| I-07 | Judge: grade decision claims, ruler, GT, scorer | judge-1a/1b | paused (stopped, no output) | needs I-02..I-06 |
| I-08 | Baseline: LLM reviewer x3 on dev | worker-base-1..3 | done (F1 1.000 x3, 8.80 s/draft) | |
| I-09 | Budget note after baseline | budget-1 | open | |
| I-10 | Planner: breakdown, ceiling, designs | planner | open | |
| I-11 | Coordinator picks design | coordinator | open | |
| I-12 | Build pilot slice | worker-build | open | |
| I-13 | Measure pilot (old vs new) | worker-measure | open | |
| I-14 | Judge grades pilot | judge-2 | open | |
| I-15 | Extend + re-measure | worker-build/measure | open | |
| I-16 | Final: old on holdout x3, new on dev+holdout | workers | open | |
| I-17 | Judge grades final | judge-3 | open | |
| I-18 | Final budget report | budget-2 | open | |
| I-19 | Limitations file + report | coordinator | open | |
