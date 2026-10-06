# Brief for every agent in this run

Read this whole file before doing anything. You have no memory of the conversation this run came from; everything you need is here or in the paths below. Work only inside `/home/user/0x01-Fix_My_Code_Challenge/desc-check-run/` (called RUN below). Never edit anything under `RUN/fixtures/` (originals, checksummed in `RUN/fixtures/SHA256SUMS`). Never touch the network, git remotes, or anything outside RUN.

## 1. What happened before this run (the "current way")

A user had a ~1,000-word technical description (`RUN/fixtures/spec_A.md`) of a code change: two new optional arguments, `footer` and `headergroups`, for the Python `tabulate()` function. They needed to submit a description of that change to an external "Description Quality" checker. The checker also runs an AI-text detector and fails any description it judges AI-written, with the instruction "Rewrite it in your own words".

The session went like this (real timestamps in `RUN/fixtures/session_timeline.csv`):

1. The assistant analysed the house style of the tabulate README (`fixtures/readme_excerpt.md` → `fixtures/assistant_turn1_style_analysis.md`).
2. The assistant rewrote spec_A in that style: rewrite B (`fixtures/rewrite_B.md`), then rewrite C without lists (`fixtures/rewrite_C.md`). Each time it **asserted** that the rewrite "keeps every rule and error case" but never checked this.
3. The user submitted C. The checker returned FAIL: AI detection 0.94, one major issue (`ai_generated`), zero minor issues, summary "detail is warranted: the hidden tests pin down the API, validation, and format-specific rendering behavior" (`fixtures/checker_result_on_C.json`).
4. The assistant explained why and declined to rework text to get past the detector, because the platform requires the person's own words (`fixtures/assistant_turn4_detector_explanation.md`).

Total: about 7 minutes and three model-written versions. None of them can be submitted. The only accuracy check was the external one, which takes a ~3-minute human round trip and reported no fact-level findings.

## 2. What this run rebuilds (decided by the coordinator, see log.md)

**The draft-verification loop**: given the reference spec (spec_A) and a candidate description draft written by a person, report

- every fact of the spec that the draft **omits** (`missing`),
- every fact the draft states **wrongly** (`contradicted`), and
- every statement about the software's behaviour, API or output that the spec does not support (`added`).

This is the only part of the work that a tool may do under the platform's rule. The person writes the words, and the tool tells them quickly and correctly whether those words still match the spec. Producing, restyling or "humanising" text to get past the AI detector is **out of scope** for every agent in this run.

The result must still be able to:

- (a) take any draft, including one written in a person's own words, not just the session's texts;
- (b) report all three issue kinds against fact IDs from `RUN/facts.json`;
- (c) never rewrite or generate the draft text itself;
- (d) run inside this container with no network;
- (e) keep the current way (an LLM reviewer reading spec + draft) usable side by side.

## 3. The two measures (fixed once the baseline is recorded; nobody changes them afterwards)

**Time** = wall-clock seconds from "draft file exists" to "issues file written", per draft.
- For LLM-agent methods, the agent records `date -u +%s.%N` immediately before it first opens the draft and immediately after it writes the output file (`t_start`, `t_end` in the output).
- For script methods, the time is the mean over 20 runs of the per-draft command, measured by a worker with `RUN/tools/timeit.sh`.
- One-time setup costs (for example compiling checks from the spec) are reported separately, together with how many drafts it takes to pay them back.
- Tokens per draft are recorded where available.

**Accuracy** = micro-averaged F1 of issue detection against the ground truth (GT), computed by `RUN/tools/score.py`:
- A `missing`/`contradicted` issue matches GT on `fact_id` alone; the kind is ignored for matching, and kind agreement is reported separately. Duplicate fact_ids in one output count once.
- An `added` issue matches a GT `added` item if, after lower-casing and collapsing whitespace, one sentence contains the other or their word-set Jaccard is ≥ 0.6.
- `added` flags that match a sentence listed in the case's `neutral_sentences` (non-behavioural framing such as "A table often needs a row of totals") are ignored and count neither way.
- Precision = TP/(TP+FP), recall = TP/(TP+FN), F1 over all cases, with per-kind and per-case breakdowns.

A method counts as better only if its time is lower **and** its F1 is not lower than the baseline's (within the spread of the baseline's repeated runs).

## 4. Files and formats

- `RUN/facts.json`: the measuring ruler, a list of atomic facts of spec_A: `[{"id":"F01","section":"footer","text":"..."}]`. IDs use F (general/footer) and H (headergroups) prefixes.
- Draft cases: `RUN/cases/dev/<case_id>.md` (development set) and `RUN/cases/holdout/<case_id>.md` (held back).
- Ground truth: `RUN/cases/dev_answers/<case_id>.json` and `RUN/cases/holdout_answers/<case_id>.json`:
  `{"case_id":"M1","base":"rewrite_C","issues":[{"fact_id":"F07","kind":"contradicted","note":"..."},{"kind":"added","sentence":"<exact sentence from the draft>"}],"neutral_sentences":["..."]}`
- Verifier output: `RUN/runs/<method>/<rep>/<case_id>.json`:
  `{"case_id":"M1","issues":[{"fact_id":"F07","kind":"contradicted","evidence":"<draft sentence>"},{"kind":"added","sentence":"<exact draft sentence>"}],"t_start":1.0,"t_end":2.0}`
- **Builders of the new method must never open `RUN/cases/holdout/`, `RUN/cases/holdout_answers/` or `RUN/cases/dev_answers/`, and must never write per-case answers into the method.** The judge greps for this.

## 5. Test set

- **Dev** (for the baseline and for building): R1 = spec_A itself (control: expect zero issues), R2 = rewrite_B, R3 = rewrite_C (both real session outputs), M1–M5 = copies of rewrite_C with 2–4 planted errors each, of mixed kinds.
- **Holdout** (used only in the final measurement): H1–H6, built by a different worker from rewrite_B and from a fresh plain-language paraphrase of spec_A (a stand-in for a person's own-words draft). Includes one unmodified control.

## 6. Logging (everyone)

Append entries to your own file `RUN/log/<your-role-and-id>.md`. Never edit earlier entries. Format, one entry per event:

```
### 2026-10-06T14:20:00Z | <role-id> | <task handed out | result returned | decision | judge's grade | budget note | limitation>
<who to whom, what was asked/returned, where the evidence is>
```

Get the time with `date -u +%FT%TZ`. Log at least when you start (restating your task) and when you finish (what you produced, file paths, anything you could not do). If you hit something you cannot do, log a `limitation` entry and also append it to `RUN/limitations_inbox/<your-role-and-id>.md`. Then carry on.

## 7. Roles

The coordinator assigns work and owns `RUN/ITEMS.md` (master list) and `RUN/log.md`. The planner designs. The budget keeper tracks cost. Workers do one narrow job each and do not redesign. The judge grades claims using only the claim and its evidence, and its grade is final. No one grades their own work.
