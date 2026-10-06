### 2026-10-06T14:14:40Z | worker-scorer | task handed out
Coordinator to worker-scorer (item I-04): implement the BRIEF.md section 3 measuring tools exactly as defined, without changing the definitions. Deliverables: RUN/tools/score.py (Python 3.11 stdlib; CLI --answers --runs [--cases] [--json]), RUN/tools/timeit.sh (N runs, mean/sd/min/max wall seconds as JSON), RUN/tools/test_score.py with synthetic data only under RUN/tools/testdata/ (perfect output, missing output file, duplicate fact_id, added match by containment, added match by Jaccard, neutral ignored, false positive, kind disagreement). I will not read RUN/cases or RUN/fixtures. Report: file paths, test results, any ambiguity in section 3 and how resolved.
### 2026-10-06T14:19:00Z | worker-scorer | result returned
worker-scorer to coordinator (item I-04). Produced, all under RUN/tools/:
- score.py (Python 3.11, stdlib only; CLI `--answers --runs [--cases M1,M2] [--json out.json]`)
- timeit.sh (`tools/timeit.sh N <command...>`; JSON with n, mean, sd, min, max, unit, failures, times, command; wall time via python perf_counter wrapper; sample sd; command stdout discarded, stderr passed through; exit 1 if any run failed)
- test_score.py (25 unittest tests) + synthetic data in testdata/answers/ (17 GT files) and testdata/runs/main/ (16 run files; t_missing_output deliberately has none; t_orphan has no GT). Nothing under RUN/cases or RUN/fixtures was read or used.
Section 3 definitions implemented unchanged. Mutation check: changing the Jaccard threshold, disabling containment, disabling the neutral filter, or replacing best-first greedy ordering each makes at least 2 tests fail.
Choices where section 3 is silent (also reported to the coordinator):
 1. Zero-division: P = 1.0 when TP+FP = 0, R = 1.0 when TP+FN = 0 (each read as "nothing to report" / "nothing to find"); F1 = harmonic mean, so an empty output on a case with GT issues has P=1.0, R=0.0, F1=0.0.
 2. Greedy order: candidate pairs taken best-first (highest Jaccard, then containment, then earlier output flag, then earlier GT item), one-to-one.
 3. A second added flag that matches an already-matched GT item is a FP (one-to-one), unlike duplicate fact_ids which count once.
 4. Order of checks for added flags: GT matching first; only the leftover flags are tested against neutral_sentences (neutral is not one-to-one, one neutral sentence can absorb many flags).
 5. Normalisation is lower-case plus whitespace collapse only; punctuation is kept for the containment test (so "x." is not contained in "x and y"), as the brief states. Words for Jaccard come from [a-z0-9_]+. Jaccard compared exactly (3/5 matches).
 6. Duplicate fact_ids in output: first occurrence decides the kind used for kind agreement. Duplicate fact_ids in a GT file also count once (noted).
 7. Output issue entries that cannot match anything (not an object, no fact_id, or an added flag without a sentence) count as FP; unknown kinds with a fact_id are matched on fact_id (kind then disagrees).
 8. A run file that is not valid JSON is treated like a missing file (all GT FN, flagged "unreadable"). A bad GT file, an unknown --cases id or a missing directory is a hard error (exit 2).
 9. Timing mean is over scored cases that have both t_start and t_end; the report says how many that is (n_timed of n_cases). Missing outputs contribute no time.
 10. fact_id comparison is exact after strip (no case folding). Output files with no GT file are ignored with a warning.
Test results (python3 tools/test_score.py):
    test_cli_bad_directory_is_an_error (__main__.TestCli.test_cli_bad_directory_is_an_error) ... ok
    test_cli_report_and_json_file (__main__.TestCli.test_cli_report_and_json_file) ... ok
    test_cli_unknown_case_is_an_error (__main__.TestCli.test_cli_unknown_case_is_an_error) ... ok
    test_duplicate_added_flag_matches_gt_item_only_once (__main__.TestFurtherRules.test_duplicate_added_flag_matches_gt_item_only_once) ... ok
    test_full_set_totals_match_hand_count (__main__.TestFurtherRules.test_full_set_totals_match_hand_count) ... ok
    test_greedy_one_to_one_is_best_first (__main__.TestFurtherRules.test_greedy_one_to_one_is_best_first) ... ok
    test_malformed_entries_are_false_positives (__main__.TestFurtherRules.test_malformed_entries_are_false_positives) ... ok
    test_micro_aggregation_on_a_subset (__main__.TestFurtherRules.test_micro_aggregation_on_a_subset) ... ok
    test_normalisation_and_compare (__main__.TestFurtherRules.test_normalisation_and_compare) ... ok
    test_punctuation_is_literal (__main__.TestFurtherRules.test_punctuation_is_literal) ... ok
    test_unreadable_output_is_treated_like_missing (__main__.TestFurtherRules.test_unreadable_output_is_treated_like_missing) ... ok
    test_zero_division_convention (__main__.TestFurtherRules.test_zero_division_convention) ... ok
    test_added_match_by_containment (__main__.TestRequiredScenarios.test_added_match_by_containment) ... ok
    test_added_match_by_jaccard (__main__.TestRequiredScenarios.test_added_match_by_jaccard) ... ok
    test_duplicate_fact_id_counts_once (__main__.TestRequiredScenarios.test_duplicate_fact_id_counts_once) ... ok
    test_false_positive (__main__.TestRequiredScenarios.test_false_positive) ... ok
    test_jaccard_boundary_is_inclusive (__main__.TestRequiredScenarios.test_jaccard_boundary_is_inclusive) ... ok
    test_kind_disagreement (__main__.TestRequiredScenarios.test_kind_disagreement) ... ok
    test_missing_output_file (__main__.TestRequiredScenarios.test_missing_output_file) ... ok
    test_neutral_sentence_is_ignored (__main__.TestRequiredScenarios.test_neutral_sentence_is_ignored) ... ok
    test_perfect_output (__main__.TestRequiredScenarios.test_perfect_output) ... ok
    test_same_flags_without_neutral_list_are_false_positives (__main__.TestRequiredScenarios.test_same_flags_without_neutral_list_are_false_positives) ... ok
    test_timeit_json (__main__.TestTimeit.test_timeit_json) ... ok
    test_timeit_reports_failures (__main__.TestTimeit.test_timeit_reports_failures) ... ok
    test_timeit_usage_errors (__main__.TestTimeit.test_timeit_usage_errors) ... ok
    
    ----------------------------------------------------------------------
    Ran 25 tests in 0.482s
    
    OK
