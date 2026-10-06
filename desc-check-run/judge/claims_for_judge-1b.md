# Claims for judge-1b (grade each: High / Medium / Low)

Evidence base: RUN/fixtures/spec_A.md, RUN/facts.json, RUN/facts_coverage.md, RUN/tools/check_facts_coverage.py, RUN/cases/** (drafts, answers, manifests, labelling files), RUN/BRIEF.md sections 3-5.

- R1. facts.json is complete and faithful: every behavioural statement in spec_A is represented by at least one fact, no fact says something spec_A does not say, and the facts are atomic enough that one planted error maps to one fact.
- R2. Dev ground truth is correct:
  - (a) R1, R2 (rewrite_B) and R3 (rewrite_C) have zero real issues, and R3's three neutral sentences are non-behavioural.
  - (b) Each of M1-M5 contains exactly the issues in its answer file. Every planted error is listed with the right fact_id, and no unlisted error exists, including side effects of the edits.
- R3. Holdout ground truth is correct:
  - (a) H6 (a fresh paraphrase) states all 105 facts and makes no added claims, and its 5 neutral sentences are non-behavioural.
  - (b) Each of H1-H5 contains exactly the issues in its answer file.
  - (c) cases/HOLDOUT_SHA256 verifies.
- R4. Two independent labellers (dev and holdout workers) agree that rewrite_B has zero issues against facts.json.
- R5. The test set is fair for comparing methods: it has a control with zero issues, real session texts and planted errors of all three kinds over both feature areas. Note any bias that would favour or penalise a particular kind of checker (for example, errors that are all single-token swaps).
