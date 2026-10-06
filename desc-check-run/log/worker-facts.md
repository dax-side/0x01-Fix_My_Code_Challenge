### 2026-10-06T14:17:22Z | worker-facts | task handed out
coordinator -> worker-facts (item I-03): build the measuring ruler RUN/facts.json from RUN/fixtures/spec_A.md (atomic, independently checkable facts; IDs F01.. for the general arguments and footer, paragraphs 1-7 up to and including the latex_longtable/rst footer-line paragraph; H01.. for headergroups, paragraphs 8-19; fields id, section, text, spec_sentence, plus ambiguity where needed; spec's own terms, nothing added). Also RUN/facts_coverage.md (every spec sentence in order with its fact IDs, counts at the end) and RUN/tools/check_facts_coverage.py (mechanical check that every spec sentence appears as some fact's spec_sentence; output recorded here). Will not read RUN/cases/ and will not design any checking method. Read BRIEF.md in full; spec_A.md checksum verified OK against fixtures/SHA256SUMS.
### 2026-10-06T14:19:26Z | worker-facts | result returned
worker-facts -> coordinator (item I-03). Produced:
- RUN/facts.json: 105 facts (F01-F33 from spec paragraphs 1-7, H01-H72 from paragraphs 8-19). Fields: id, section, text, spec_sentence (verbatim spec sentence), plus "ambiguity" on 29 facts and "also_in" on H18 (S31 "...including the `showindex` column" restates S43, so it maps to H18 rather than creating a duplicate fact). 17 compound sentences were split because their parts could be wrong independently. Name lists (merged-cell formats H23, unsupported formats H71, pipe/github/asciidoc F27) are one fact each, and the two headergroups examples are H08 and H09.
- RUN/facts_coverage.md: all 88 spec sentences in order, verbatim, each with its fact IDs; counts at the end (19 paragraphs, 88 sentences, 105 facts, 0 sentences without a fact).
- RUN/tools/check_facts_coverage.py: stdlib check with 6 parts (schema/IDs, verbatim substrings, sentence coverage, character coverage independent of sentence splitting, F/H paragraph rule, coverage.md consistency). Negative tests run on scratchpad copies (H72 removed; F01 spec_sentence altered) both gave FAIL with exit 1, as expected.
Check output (python3 -I tools/check_facts_coverage.py):
    spec: 19 paragraphs, 88 sentences
    facts: 105 (F=33, H=72); with ambiguity note: 29
    [3] sentences covered by a spec_sentence: 88/88
    [4] non-whitespace spec characters covered: 5062/5062
    [6] coverage.md rows: 88; fact ids listed: 105/105
    RESULT: PASS (all 6 checks)
    exit=0
Method: fact texts were written by hand in a generator script kept in the session scratchpad (not in RUN). The generator copies spec_sentence verbatim from spec_A by sentence number. fixtures/ unchanged (SHA256SUMS all OK). RUN/cases/ not opened. No checking method designed.
