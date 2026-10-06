#!/usr/bin/env python3
"""score.py - micro-averaged issue-detection scorer (BRIEF.md section 3).

Usage:
    python3 tools/score.py --answers <dir of GT json> --runs <dir of output json>
                           [--cases M1,M2,...] [--json out.json]

Python 3.11, standard library only. Never reads anything except the two
directories it is pointed at.

Definitions implemented (BRIEF.md section 3, unchanged):

* A `missing`/`contradicted` issue matches a GT fact issue on `fact_id` alone;
  the kind is ignored for matching. Duplicate fact_ids in one output count once.
  Kind agreement (share of matched fact issues whose kind also agrees) is
  reported as a separate number.
* An `added` issue matches a GT `added` item if, after lower-casing and
  collapsing whitespace, one sentence contains the other, or their word-set
  Jaccard (words = [a-z0-9_]+) is >= 0.6. Matching is one-to-one and greedy, so
  each GT item is matched at most once.
* An `added` flag that matches (same rule) a sentence in the case's
  `neutral_sentences` is ignored: it counts neither as TP nor as FP.
* precision = TP/(TP+FP), recall = TP/(TP+FN), F1 = harmonic mean, micro-averaged
  over all scored cases, with fact-vs-added and per-case breakdowns.
* Missing output file: every GT issue of that case is an FN.
* Zero-division: precision = 1.0 when TP+FP == 0 (nothing reported), recall = 1.0
  when TP+FN == 0 (nothing to find).

Implementation choices where the brief is silent are listed in the module-level
constants/docstrings below and in RUN/log/worker-scorer.md.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

WORD_RE = re.compile(r"[a-z0-9_]+")
JACCARD_THRESHOLD = Fraction(3, 5)  # 0.6, compared exactly (no float rounding)
FACT_KINDS = ("missing", "contradicted")


class DataError(Exception):
    """Unusable input that should stop the run (exit code 2)."""


# --------------------------------------------------------------------------- #
# Sentence matching
# --------------------------------------------------------------------------- #

def normalize(text: str) -> str:
    """Lower-case and collapse all whitespace runs to single spaces."""
    return " ".join(str(text).lower().split())


class Prepared:
    """A sentence normalised once, with its word set."""

    __slots__ = ("raw", "norm", "words")

    def __init__(self, raw: str) -> None:
        self.raw = raw
        self.norm = normalize(raw)
        self.words = frozenset(WORD_RE.findall(self.norm))


def compare(a: Prepared, b: Prepared) -> tuple[bool, Fraction, bool]:
    """Return (is_match, jaccard, contained) for two prepared sentences.

    contained: one normalised sentence is a substring of the other (never for an
    empty sentence). Jaccard is over the [a-z0-9_]+ word sets (0 if both empty).
    """
    contained = bool(a.norm) and bool(b.norm) and (a.norm in b.norm or b.norm in a.norm)
    union = len(a.words | b.words)
    jac = Fraction(len(a.words & b.words), union) if union else Fraction(0)
    return (contained or jac >= JACCARD_THRESHOLD), jac, contained


def match_added(gt: list[Prepared], out: list[Prepared]):
    """One-to-one greedy matching of output added flags to GT added items.

    Candidate pairs are every (output, GT) pair that satisfies the match rule.
    They are taken best-first: highest Jaccard, then containment before
    Jaccard-only, then earlier output flag, then earlier GT item. Each output
    flag and each GT item is used at most once.
    Returns (pairs, unmatched_out_indexes, unmatched_gt_indexes) where pairs is a
    list of (out_idx, gt_idx, jaccard, contained).
    """
    cands = []
    for oi, o in enumerate(out):
        for gi, g in enumerate(gt):
            ok, jac, contained = compare(o, g)
            if ok:
                cands.append((-jac, 0 if contained else 1, oi, gi, jac, contained))
    cands.sort(key=lambda c: c[:4])
    used_o: set[int] = set()
    used_g: set[int] = set()
    pairs = []
    for _, _, oi, gi, jac, contained in cands:
        if oi in used_o or gi in used_g:
            continue
        used_o.add(oi)
        used_g.add(gi)
        pairs.append((oi, gi, jac, contained))
    pairs.sort()
    un_o = [i for i in range(len(out)) if i not in used_o]
    un_g = [i for i in range(len(gt)) if i not in used_g]
    return pairs, un_o, un_g


# --------------------------------------------------------------------------- #
# Metrics
# --------------------------------------------------------------------------- #

def prf(tp: int, fp: int, fn: int) -> dict[str, Any]:
    p = 1.0 if tp + fp == 0 else tp / (tp + fp)
    r = 1.0 if tp + fn == 0 else tp / (tp + fn)
    f1 = 0.0 if (p + r) == 0 else 2 * p * r / (p + r)
    return {"tp": tp, "fp": fp, "fn": fn, "precision": p, "recall": r, "f1": f1}


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

def load_gt(path: Path) -> dict[str, Any]:
    """Load and validate one GT file. Any defect is a hard DataError."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise DataError(f"cannot read GT file {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise DataError(f"GT file {path} is not a JSON object")
    issues = data.get("issues", [])
    if not isinstance(issues, list):
        raise DataError(f"GT file {path}: 'issues' is not a list")
    fact: dict[str, str] = {}
    added: list[str] = []
    dup_gt_facts: list[str] = []
    for i, it in enumerate(issues):
        if not isinstance(it, dict):
            raise DataError(f"GT file {path}: issue #{i} is not an object")
        kind = it.get("kind")
        if kind == "added":
            s = it.get("sentence")
            if not isinstance(s, str) or not normalize(s):
                raise DataError(f"GT file {path}: added issue #{i} has no sentence")
            added.append(s)
        elif kind in FACT_KINDS:
            fid = it.get("fact_id")
            if not isinstance(fid, str) or not fid.strip():
                raise DataError(f"GT file {path}: {kind} issue #{i} has no fact_id")
            fid = fid.strip()
            if fid in fact:
                dup_gt_facts.append(fid)  # GT duplicates count once as well
            else:
                fact[fid] = kind
        else:
            raise DataError(f"GT file {path}: issue #{i} has unknown kind {kind!r}")
    neutral = data.get("neutral_sentences", [])
    if not isinstance(neutral, list) or not all(isinstance(s, str) for s in neutral):
        raise DataError(f"GT file {path}: 'neutral_sentences' is not a list of strings")
    return {"fact": fact, "added": added, "neutral": neutral, "dup_gt_facts": dup_gt_facts}


def load_run(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    """Return (parsed output or None, problem or None). Missing file -> (None, 'missing')."""
    if not path.is_file():
        return None, "missing"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return None, f"unreadable ({exc.__class__.__name__}: {exc})"
    if not isinstance(data, dict) or not isinstance(data.get("issues", []), list):
        return None, "unreadable (top level is not an object with an 'issues' list)"
    return data, None


def _num(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


# --------------------------------------------------------------------------- #
# Scoring one case
# --------------------------------------------------------------------------- #

def score_case(case_id: str, gt: dict[str, Any], run: dict[str, Any] | None,
               run_problem: str | None = None) -> dict[str, Any]:
    notes: list[str] = []
    gt_fact: dict[str, str] = gt["fact"]
    gt_added = [Prepared(s) for s in gt["added"]]
    neutral = [Prepared(s) for s in gt["neutral"]]
    if gt["dup_gt_facts"]:
        notes.append("GT lists fact_id more than once (counted once): "
                     + ", ".join(sorted(set(gt["dup_gt_facts"]))))

    out_fact: dict[str, str] = {}      # fact_id -> kind of its first occurrence
    out_added: list[Prepared] = []
    malformed_fact = 0
    malformed_added = 0
    dup_out_facts: list[str] = []
    seconds = None

    if run is None:
        notes.append(f"output file {run_problem}: every GT issue counted as FN")
    else:
        for i, it in enumerate(run.get("issues", [])):
            if isinstance(it, dict) and it.get("kind") == "added":
                s = it.get("sentence")
                if isinstance(s, str) and normalize(s):
                    out_added.append(Prepared(s))
                else:
                    malformed_added += 1
                    notes.append(f"issue #{i}: added flag without a usable 'sentence' (counted as FP)")
            else:
                fid = it.get("fact_id") if isinstance(it, dict) else None
                if isinstance(fid, str) and fid.strip():
                    fid = fid.strip()
                    if fid in out_fact:
                        dup_out_facts.append(fid)
                    else:
                        out_fact[fid] = it.get("kind")
                else:
                    malformed_fact += 1
                    notes.append(f"issue #{i}: not an added flag and has no fact_id (counted as FP)")
        if dup_out_facts:
            notes.append("duplicate fact_id in output counted once: "
                         + ", ".join(sorted(set(dup_out_facts))))
        ts, te = run.get("t_start"), run.get("t_end")
        if _num(ts) and _num(te):
            seconds = float(te) - float(ts)
            if seconds < 0:
                notes.append(f"t_end < t_start ({seconds:.3f}s)")
        if run.get("case_id") not in (None, case_id):
            notes.append(f"output says case_id={run.get('case_id')!r}")

    # --- fact issues: fact_id only ---
    gt_ids = set(gt_fact)
    out_ids = set(out_fact)
    tp_ids = sorted(gt_ids & out_ids)
    fp_ids = sorted(out_ids - gt_ids)
    fn_ids = sorted(gt_ids - out_ids)
    kind_disagree = [{"fact_id": f, "gt_kind": gt_fact[f], "out_kind": out_fact[f]}
                     for f in tp_ids if out_fact[f] != gt_fact[f]]
    fact_fp = len(fp_ids) + malformed_fact
    fact = prf(len(tp_ids), fact_fp, len(fn_ids))
    fact.update({"tp_ids": tp_ids, "fp_ids": fp_ids, "fn_ids": fn_ids,
                 "malformed_fp": malformed_fact, "kind_disagree": kind_disagree})

    # --- added issues: one-to-one greedy, then neutral filter on the leftovers ---
    pairs, un_o, un_g = match_added(gt_added, out_added)
    ignored, fps = [], []
    for oi in un_o:
        if any(compare(out_added[oi], n)[0] for n in neutral):
            ignored.append(out_added[oi].raw)
        else:
            fps.append(out_added[oi].raw)
    added = prf(len(pairs), len(fps) + malformed_added, len(un_g))
    added.update({
        "matches": [{"out": out_added[oi].raw, "gt": gt_added[gi].raw,
                     "jaccard": round(float(j), 4), "contained": c}
                    for oi, gi, j, c in pairs],
        "fp_sentences": fps,
        "fn_sentences": [gt_added[gi].raw for gi in un_g],
        "ignored_neutral": ignored,
        "malformed_fp": malformed_added,
    })

    total = prf(fact["tp"] + added["tp"], fact["fp"] + added["fp"], fact["fn"] + added["fn"])
    return {
        "case_id": case_id,
        "output": "ok" if run is not None else run_problem,
        **total,
        "fact": fact,
        "added": added,
        "kind_agreement": {"matched": len(tp_ids), "agree": len(tp_ids) - len(kind_disagree)},
        "seconds": seconds,
        "notes": notes,
    }


# --------------------------------------------------------------------------- #
# Scoring a set of cases
# --------------------------------------------------------------------------- #

def natural_key(s: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def score_all(answers_dir: Path, runs_dir: Path, cases: list[str] | None = None) -> dict[str, Any]:
    if not answers_dir.is_dir():
        raise DataError(f"--answers is not a directory: {answers_dir}")
    if not runs_dir.is_dir():
        raise DataError(f"--runs is not a directory: {runs_dir}")
    available = sorted((p.stem for p in answers_dir.glob("*.json")), key=natural_key)
    if cases is None:
        ids = available
    else:
        ids = list(dict.fromkeys(cases))
        unknown = [c for c in ids if c not in available]
        if unknown:
            raise DataError("no GT file for case(s): " + ", ".join(unknown))
    if not ids:
        raise DataError(f"no cases to score (no *.json in {answers_dir})")

    per_case = []
    warnings: list[str] = []
    for cid in ids:
        gt = load_gt(answers_dir / f"{cid}.json")
        run, problem = load_run(runs_dir / f"{cid}.json")
        res = score_case(cid, gt, run, problem)
        per_case.append(res)
        if problem is not None:
            warnings.append(f"{cid}: output {problem}")

    scored = set(ids)
    extra = sorted((p.stem for p in runs_dir.glob("*.json") if p.stem not in scored), key=natural_key)
    if extra and cases is None:
        warnings.append("output files with no GT file (not scored): " + ", ".join(extra))

    def tot(group: str | None):
        src = [c if group is None else c[group] for c in per_case]
        return prf(sum(c["tp"] for c in src), sum(c["fp"] for c in src), sum(c["fn"] for c in src))

    matched = sum(c["kind_agreement"]["matched"] for c in per_case)
    agree = sum(c["kind_agreement"]["agree"] for c in per_case)
    timed = [c["seconds"] for c in per_case if c["seconds"] is not None]
    return {
        "answers_dir": str(answers_dir),
        "runs_dir": str(runs_dir),
        "cases": ids,
        "overall": tot(None),
        "by_kind": {"fact": tot("fact"), "added": tot("added")},
        "kind_agreement": {"matched": matched, "agree": agree,
                           "share": (agree / matched) if matched else None},
        "timing": {"n_timed": len(timed), "n_cases": len(per_case),
                   "mean_seconds": (sum(timed) / len(timed)) if timed else None},
        "missing_outputs": [c["case_id"] for c in per_case if c["output"] == "missing"],
        "unreadable_outputs": [c["case_id"] for c in per_case
                               if c["output"] not in ("ok", "missing")],
        "per_case": per_case,
        "warnings": warnings,
    }


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def _f(x: float | None) -> str:
    return "n/a" if x is None else f"{x:.3f}"


def format_report(res: dict[str, Any]) -> str:
    L: list[str] = []
    o = res["overall"]
    L.append(f"answers: {res['answers_dir']}")
    L.append(f"runs:    {res['runs_dir']}")
    L.append(f"cases scored: {len(res['cases'])} ({', '.join(res['cases'])})")
    L.append("")
    L.append("== micro-averaged ==")
    L.append(f"{'group':<14}{'TP':>5}{'FP':>5}{'FN':>5}{'precision':>11}{'recall':>9}{'F1':>8}")
    for name, m in (("overall", o), ("fact issues", res["by_kind"]["fact"]),
                    ("added issues", res["by_kind"]["added"])):
        L.append(f"{name:<14}{m['tp']:>5}{m['fp']:>5}{m['fn']:>5}"
                 f"{m['precision']:>11.3f}{m['recall']:>9.3f}{m['f1']:>8.3f}")
    ka = res["kind_agreement"]
    L.append("")
    L.append(f"kind agreement (matched fact issues whose kind also agrees): "
             f"{ka['agree']}/{ka['matched']} = {_f(ka['share'])}")
    tm = res["timing"]
    mean_txt = "n/a" if tm["mean_seconds"] is None else f"{tm['mean_seconds']:.3f} s"
    L.append(f"mean (t_end - t_start): {mean_txt} over {tm['n_timed']} of {tm['n_cases']} cases with both fields")
    if res["missing_outputs"]:
        L.append("MISSING OUTPUT FILES (all GT issues counted as FN): " + ", ".join(res["missing_outputs"]))
    if res["unreadable_outputs"]:
        L.append("UNREADABLE OUTPUT FILES (all GT issues counted as FN): " + ", ".join(res["unreadable_outputs"]))
    L.append("")
    L.append("== per case ==")
    L.append(f"{'case':<18}{'out':<8}{'TP':>4}{'FP':>4}{'FN':>4}{'P':>7}{'R':>7}{'F1':>7}"
             f"  {'fact t/f/n':<11}{'added t/f/n(+ign)':<19}{'kind':>6}{'sec':>9}")
    for c in res["per_case"]:
        fa, ad, ka_c = c["fact"], c["added"], c["kind_agreement"]
        kcol = f"{ka_c['agree']}/{ka_c['matched']}" if ka_c["matched"] else "-"
        sec = "-" if c["seconds"] is None else f"{c['seconds']:.3f}"
        out = "ok" if c["output"] == "ok" else ("missing" if c["output"] == "missing" else "BAD")
        fact_col = f"{fa['tp']}/{fa['fp']}/{fa['fn']}"
        added_col = f"{ad['tp']}/{ad['fp']}/{ad['fn']}(+{len(ad['ignored_neutral'])})"
        L.append(f"{c['case_id']:<18}{out:<8}{c['tp']:>4}{c['fp']:>4}{c['fn']:>4}"
                 f"{c['precision']:>7.3f}{c['recall']:>7.3f}{c['f1']:>7.3f}"
                 f"  {fact_col:<11}{added_col:<19}{kcol:>6}{sec:>9}")
    notes = [(c["case_id"], n) for c in res["per_case"] for n in c["notes"]]
    if notes:
        L.append("")
        L.append("== notes ==")
        for cid, n in notes:
            L.append(f"{cid}: {n}")
    if res["warnings"]:
        L.append("")
        L.append("== warnings ==")
        L.extend(res["warnings"])
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Score verifier outputs against ground truth (BRIEF.md section 3).")
    ap.add_argument("--answers", required=True, help="directory of ground-truth <case_id>.json files")
    ap.add_argument("--runs", required=True, help="directory of verifier output <case_id>.json files")
    ap.add_argument("--cases", help="comma-separated case ids to score (default: every case with a GT file)")
    ap.add_argument("--json", dest="json_out", help="also write the full result to this JSON file")
    args = ap.parse_args(argv)
    cases = None
    if args.cases is not None:
        cases = [c.strip() for c in args.cases.split(",") if c.strip()]
        if not cases:
            print("error: --cases is empty", file=sys.stderr)
            return 2
    try:
        res = score_all(Path(args.answers), Path(args.runs), cases)
    except DataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(format_report(res))
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
