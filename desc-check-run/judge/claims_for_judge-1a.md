# Claims for judge-1a (grade each: High / Medium / Low)

Evidence base: RUN/fixtures/* (originals, checksummed), RUN/kb/claims.md (claim index with quotes and sources), RUN/BRIEF.md sections 3-4 (the metric definition), RUN/tools/score.py and RUN/tools/test_score.py.

## A. The 17 decision-relevant claims in kb/claims.md
K36, K39, K42, K43, K46, K61, K62, K63, K65, K66, K67, K68, K71, K73, K75, K76, K77. For K36, K39, K42, K43 and K46 (claims about whether rewrites B and C are faithful to spec_A), use as evidence RUN/fixtures/spec_A.md, RUN/fixtures/rewrite_B.md, RUN/fixtures/rewrite_C.md and RUN/facts.json. Check them yourself, as far as needed to grade.

## B. Premises the run's scope decision rests on
- P1. The checker's FAIL on rewrite C was caused only by AI detection: verdictBasis has majors=1 (category ai_generated), minors=0, aiDetectionBlocking=true.
- P2. The checker's remedy text asks the person to write the description in their own words.
- P3. The checker output contains no evidence that a fact-by-fact content check against the spec or tests was run.
- P4. From fixtures/session_timeline.csv: rewrite C was delivered 196.4 s before the checker result was pasted, and the first user turn to the last assistant turn took 422.8 s.
- P5. No knowledge base other than the conversation exists in the workspace (evidence: RUN/kb/search.md; you may re-run searches yourself, but do not open /root/.claude/projects/*.jsonl).

## C. The measuring tool
- S1. RUN/tools/score.py implements BRIEF.md section 3 exactly (matching rules, neutral handling, duplicates, micro P/R/F1). Write your own small adversarial test cases in RUN/judge/scratch_1a/ to try to break it.
