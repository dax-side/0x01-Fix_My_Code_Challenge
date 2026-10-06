#!/usr/bin/env python3
"""Self-tests for tools/score.py and tools/timeit.sh.

Uses ONLY the synthetic files under tools/testdata/ (answers/ and runs/main/).
Never reads anything under RUN/cases or RUN/fixtures.

Run:  python3 tools/test_score.py          (from RUN)
      python3 -m unittest -v tools/test_score.py
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import score  # noqa: E402

ANSWERS = HERE / "testdata" / "answers"
RUNS = HERE / "testdata" / "runs" / "main"
SCORE_PY = HERE / "score.py"
TIMEIT = HERE / "timeit.sh"


def one(case_id):
    """Score a single synthetic case and return (whole result, that case's row)."""
    res = score.score_all(ANSWERS, RUNS, [case_id])
    return res, res["per_case"][0]


class TestRequiredScenarios(unittest.TestCase):
    def test_perfect_output(self):
        res, c = one("t_perfect")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (3, 0, 0))
        self.assertEqual((c["precision"], c["recall"], c["f1"]), (1.0, 1.0, 1.0))
        self.assertEqual((c["fact"]["tp"], c["added"]["tp"]), (2, 1))
        self.assertEqual(res["kind_agreement"], {"matched": 2, "agree": 2, "share": 1.0})
        self.assertEqual(c["seconds"], 2.0)

    def test_missing_output_file(self):
        res, c = one("t_missing_output")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (0, 0, 3))
        self.assertEqual((c["fact"]["fn"], c["added"]["fn"]), (2, 1))
        self.assertEqual(c["output"], "missing")
        self.assertEqual(res["missing_outputs"], ["t_missing_output"])
        self.assertEqual(c["recall"], 0.0)
        self.assertEqual(c["f1"], 0.0)
        self.assertTrue(any("missing" in n for n in c["notes"]))
        self.assertIsNone(c["seconds"])

    def test_duplicate_fact_id_counts_once(self):
        res, c = one("t_dup_fact")
        # F05 appears 3 times (missing, contradicted, missing): 1 TP, no FP.
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (1, 0, 0))
        # first occurrence (missing) decides the kind; GT says missing -> agrees.
        self.assertEqual(c["kind_agreement"], {"matched": 1, "agree": 1})
        self.assertTrue(any("duplicate fact_id" in n for n in c["notes"]))

    def test_added_match_by_containment(self):
        _, c = one("t_added_contain")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (2, 0, 0))
        for m in c["added"]["matches"]:
            self.assertTrue(m["contained"], m)
            self.assertLess(m["jaccard"], 0.6, m)  # so containment alone caused the match

    def test_added_match_by_jaccard(self):
        _, c = one("t_added_jaccard")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (1, 0, 0))
        m = c["added"]["matches"][0]
        self.assertFalse(m["contained"])
        self.assertGreaterEqual(m["jaccard"], 0.6)

    def test_jaccard_boundary_is_inclusive(self):
        _, c = one("t_added_boundary")
        # 3/5 = 0.6 matches; 3/6 = 0.5 does not.
        self.assertEqual((c["added"]["tp"], c["added"]["fp"], c["added"]["fn"]), (1, 1, 1))
        self.assertEqual(c["added"]["matches"][0]["jaccard"], 0.6)
        self.assertEqual(c["added"]["fp_sentences"], ["one three five six"])

    def test_neutral_sentence_is_ignored(self):
        _, c = one("t_neutral")
        # 3 added flags match neutral sentences (equality, containment, Jaccard): neither TP nor FP.
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (1, 0, 0))
        self.assertEqual(len(c["added"]["ignored_neutral"]), 3)
        self.assertEqual((c["added"]["tp"], c["added"]["fp"], c["added"]["fn"]), (0, 0, 0))

    def test_same_flags_without_neutral_list_are_false_positives(self):
        _, c = one("t_neutral_absent")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (1, 3, 0))
        self.assertEqual(c["added"]["ignored_neutral"], [])

    def test_false_positive(self):
        _, c = one("t_false_pos")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (1, 2, 0))
        self.assertEqual(c["fact"]["fp_ids"], ["F08"])
        self.assertEqual(c["added"]["fp_sentences"], ["The tool uploads results to a server."])
        self.assertAlmostEqual(c["precision"], 1 / 3)
        self.assertEqual(c["recall"], 1.0)
        self.assertAlmostEqual(c["f1"], 0.5)

    def test_kind_disagreement(self):
        res, c = one("t_kind_disagree")
        # kind is ignored for matching ...
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (2, 0, 0))
        # ... and reported separately.
        self.assertEqual(res["kind_agreement"], {"matched": 2, "agree": 1, "share": 0.5})
        self.assertEqual(c["fact"]["kind_disagree"],
                         [{"fact_id": "F09", "gt_kind": "missing", "out_kind": "contradicted"}])


class TestFurtherRules(unittest.TestCase):
    def test_greedy_one_to_one_is_best_first(self):
        _, c = one("t_greedy")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (2, 0, 0))

    def test_duplicate_added_flag_matches_gt_item_only_once(self):
        _, c = one("t_dup_added")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (1, 1, 0))

    def test_zero_division_convention(self):
        _, ctl = one("t_zero_control")  # nothing to find, nothing reported
        self.assertEqual((ctl["precision"], ctl["recall"], ctl["f1"]), (1.0, 1.0, 1.0))
        _, fl = one("t_zero_gt_flag")  # nothing to find, one flag reported
        self.assertEqual((fl["tp"], fl["fp"], fl["fn"]), (0, 1, 0))
        self.assertEqual((fl["precision"], fl["recall"], fl["f1"]), (0.0, 1.0, 0.0))
        _, miss = one("t_missing_output")  # nothing reported, something to find
        self.assertEqual((miss["precision"], miss["recall"], miss["f1"]), (1.0, 0.0, 0.0))

    def test_punctuation_is_literal(self):
        _, c = one("t_punct_literal")  # "...zeta." is not contained in "...zeta and ..."; Jaccard 0.5
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (0, 1, 1))

    def test_malformed_entries_are_false_positives(self):
        _, c = one("t_malformed")
        self.assertEqual((c["fact"]["tp"], c["fact"]["fp"], c["added"]["fp"]), (1, 2, 1))

    def test_unreadable_output_is_treated_like_missing(self):
        res, c = one("t_bad_json")
        self.assertEqual((c["tp"], c["fp"], c["fn"]), (0, 0, 2))
        self.assertEqual(res["unreadable_outputs"], ["t_bad_json"])

    def test_normalisation_and_compare(self):
        self.assertEqual(score.normalize("  The\tWidget \n IS  "), "the widget is")
        a = score.Prepared("Foo_1 bar")
        b = score.Prepared("zzz foo_1   BAR yyy")
        ok, jac, contained = score.compare(a, b)
        self.assertTrue(ok and contained)
        ok, jac, contained = score.compare(score.Prepared(""), score.Prepared(""))
        self.assertFalse(ok)  # empty never matches

    def test_micro_aggregation_on_a_subset(self):
        res = score.score_all(ANSWERS, RUNS, ["t_perfect", "t_false_pos", "t_kind_disagree"])
        o = res["overall"]
        self.assertEqual((o["tp"], o["fp"], o["fn"]), (6, 2, 0))
        self.assertAlmostEqual(o["precision"], 0.75)
        self.assertAlmostEqual(o["f1"], 2 * 0.75 * 1.0 / 1.75)
        f, a = res["by_kind"]["fact"], res["by_kind"]["added"]
        self.assertEqual((f["tp"], f["fp"], f["fn"]), (5, 1, 0))
        self.assertEqual((a["tp"], a["fp"], a["fn"]), (1, 1, 0))
        self.assertEqual(res["kind_agreement"], {"matched": 5, "agree": 4, "share": 0.8})
        # timing: t_perfect 2.0 s, t_false_pos 0.5 s, t_kind_disagree has none
        self.assertEqual(res["timing"]["n_timed"], 2)
        self.assertAlmostEqual(res["timing"]["mean_seconds"], 1.25)

    def test_full_set_totals_match_hand_count(self):
        res = score.score_all(ANSWERS, RUNS)
        self.assertEqual(len(res["cases"]), 17)
        o = res["overall"]
        self.assertEqual((o["tp"], o["fp"], o["fn"]), (17, 12, 7))
        f, a = res["by_kind"]["fact"], res["by_kind"]["added"]
        self.assertEqual((f["tp"], f["fp"], f["fn"]), (9, 3, 3))
        self.assertEqual((a["tp"], a["fp"], a["fn"]), (8, 9, 4))
        self.assertEqual(sum(c["tp"] for c in res["per_case"]), o["tp"])
        self.assertAlmostEqual(res["timing"]["mean_seconds"], (2.0 + 0.5 + 0.25) / 3)
        self.assertTrue(any("t_orphan" in w for w in res["warnings"]))  # run without GT: warned, not scored


class TestCli(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCORE_PY), *args], capture_output=True, text=True)

    def test_cli_report_and_json_file(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "out.json"
            p = self.run_cli("--answers", str(ANSWERS), "--runs", str(RUNS),
                             "--cases", "t_perfect,t_missing_output", "--json", str(out))
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertIn("t_perfect", p.stdout)
            self.assertIn("MISSING OUTPUT FILES", p.stdout)
            data = json.loads(out.read_text())
            self.assertEqual(data["cases"], ["t_perfect", "t_missing_output"])
            self.assertEqual((data["overall"]["tp"], data["overall"]["fn"]), (3, 3))
            self.assertAlmostEqual(data["overall"]["recall"], 0.5)

    def test_cli_unknown_case_is_an_error(self):
        p = self.run_cli("--answers", str(ANSWERS), "--runs", str(RUNS), "--cases", "nope")
        self.assertEqual(p.returncode, 2)
        self.assertIn("nope", p.stderr)

    def test_cli_bad_directory_is_an_error(self):
        p = self.run_cli("--answers", str(ANSWERS / "does_not_exist"), "--runs", str(RUNS))
        self.assertEqual(p.returncode, 2)


class TestTimeit(unittest.TestCase):
    def test_timeit_json(self):
        p = subprocess.run([str(TIMEIT), "4", "sleep", "0.05"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        d = json.loads(p.stdout)
        self.assertEqual((d["n"], d["failures"]), (4, 0))
        for k in ("mean", "sd", "min", "max"):
            self.assertIn(k, d)
        self.assertGreaterEqual(d["min"], 0.05)
        self.assertLess(d["max"], 1.0)
        self.assertLessEqual(d["min"], d["mean"])
        self.assertLessEqual(d["mean"], d["max"])

    def test_timeit_usage_errors(self):
        self.assertEqual(subprocess.run([str(TIMEIT), "0", "true"], capture_output=True).returncode, 2)
        self.assertEqual(subprocess.run([str(TIMEIT)], capture_output=True).returncode, 2)

    def test_timeit_reports_failures(self):
        p = subprocess.run([str(TIMEIT), "2", "false"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)
        self.assertEqual(json.loads(p.stdout)["failures"], 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
