### 2026-10-06T14:20:36Z | worker-dev | task handed out
coordinator -> worker-dev (item I-05): build the dev test set and its GT. (1) Copy R1=fixtures/spec_A.md, R2=fixtures/rewrite_B.md, R3=fixtures/rewrite_C.md byte for byte into cases/dev/. (2) Label R2 and R3 against all 105 facts of facts.json (stated / missing / contradicted), plus every unsupported behavioural sentence (added) and non-behavioural framing sentences (neutral_sentences); R1 GT has no issues. Per-fact labelling evidence goes to cases/dev_labelling_R2_R3.md. (3) Build M1-M5 from byte-exact copies of rewrite_C with 2-4 planted errors each, 15 total (>=6 contradicted, >=4 missing, >=3 added), spread over F and H facts; GT = R3 GT adjusted + planted; manifest in cases/dev_manifest.md. (4) Sanity-check score.py on GT echo (must be F1=1.0), paste output here, delete runs/gt_echo. Will not open cases/holdout or cases/holdout_answers and will not design or run any other checking method. Read BRIEF.md in full.
### 2026-10-06T14:27:47Z | worker-dev | result returned
worker-dev -> coordinator (item I-05). Produced:
- cases/dev/R1.md, R2.md, R3.md: `cp` of fixtures/spec_A.md, rewrite_B.md, rewrite_C.md; `cmp` and sha256 identical (cb29ba18..., 7a846b5c..., e52d795a...).
- cases/dev/M1-M5.md: each `cp` of fixtures/rewrite_C.md (byte equality asserted before editing), then 2-4 exact one-occurrence string replacements. Word-level diffs against rewrite_C show only the planned edits.
- cases/dev_answers/{R1,R2,R3,M1..M5}.json (BRIEF section 4 format, with "base" and a "note" on every issue).
- cases/dev_labelling_R2_R3.md: for R2 and R3, one line per fact (105 each) giving the status and the exact draft text that states it, plus an inventory of every sentence/list/code unit of each draft (R2 91 units, R3 78) showing the facts it states or its class (neutral / supported summary). A script asserted that every quote is an exact substring found exactly once in the draft and that no unit is left unclassified.
- cases/dev_manifest.md: per mutant, each planted error with fact_id/added, kind, original text, new text, note, and the co-located facts that remain stated.
Labelling result: R2 = 105/105 stated, 0 added, 0 neutral. R3 = 105/105 stated, 0 added, 3 neutral ("A table often needs a row of totals or notes below its data." / "Some tables need a title over several columns." / "There is more than one way to draw a group title in plain text."). R1 = spec itself, no issues. So the real cases carry 0 GT issues, and all 15 GT issues in dev are planted.
GT issue counts: R1 0, R2 0, R3 0; M1 2C+1A (F13, H20); M2 1C+1M (F14, H54); M3 2C+1M+1A (H05, H70, F33); M4 1C+1M+1A (F26, H38); M5 1C+1M+1A (H23, F05). Totals 7 contradicted, 4 missing, 4 added = 15 (footer side 7, headergroups side 8).
Judgement calls: (1) R2 sentence "footer adds a row of cells below the table data, and headergroups adds titled groups of columns above the header." and the same clause in R3's first sentence are labelled a supported summary (F07, H01, H24, H45, H55, H59), so they are neither added nor neutral. (2) R3 H01 "such column groups" is read as pointing back to the framing sentence, not as limiting groups to several columns. (3) H10: the spec's "only when" is matched by the draft's "If ... then" together with "Otherwise ... one level". (4) I dropped a footer left->right flip (F10) because it would arguably also make F11 ("left padding ... same as headers") wrong; I used H20 first->last instead so the GT stays unambiguous.
Generator and check scripts are in the session scratchpad (label_evidence.py, build_labelling.py, build_mutants.py). They are not copied into RUN because they contain GT. cases/holdout* not opened. fixtures unchanged (sha256 -c all OK). No checking method designed or run.
Scorer sanity check: runs/gt_echo/1 = copy of all 8 GT files; `python3 tools/score.py --answers cases/dev_answers --runs runs/gt_echo/1` exit=0, output:
```
answers: cases/dev_answers
runs:    runs/gt_echo/1
cases scored: 8 (M1, M2, M3, M4, M5, R1, R2, R3)

== micro-averaged ==
group            TP   FP   FN  precision   recall      F1
overall          15    0    0      1.000    1.000   1.000
fact issues      11    0    0      1.000    1.000   1.000
added issues      4    0    0      1.000    1.000   1.000

kind agreement (matched fact issues whose kind also agrees): 11/11 = 1.000
mean (t_end - t_start): n/a over 0 of 8 cases with both fields

== per case ==
case              out       TP  FP  FN      P      R     F1  fact t/f/n added t/f/n(+ign)    kind      sec
M1                ok         3   0   0  1.000  1.000  1.000  2/0/0      1/0/0(+0)             2/2        -
M2                ok         2   0   0  1.000  1.000  1.000  2/0/0      0/0/0(+0)             2/2        -
M3                ok         4   0   0  1.000  1.000  1.000  3/0/0      1/0/0(+0)             3/3        -
M4                ok         3   0   0  1.000  1.000  1.000  2/0/0      1/0/0(+0)             2/2        -
M5                ok         3   0   0  1.000  1.000  1.000  2/0/0      1/0/0(+0)             2/2        -
R1                ok         0   0   0  1.000  1.000  1.000  0/0/0      0/0/0(+0)               -        -
R2                ok         0   0   0  1.000  1.000  1.000  0/0/0      0/0/0(+0)               -        -
R3                ok         0   0   0  1.000  1.000  1.000  0/0/0      0/0/0(+0)               -        -
```
runs/gt_echo deleted afterwards.
