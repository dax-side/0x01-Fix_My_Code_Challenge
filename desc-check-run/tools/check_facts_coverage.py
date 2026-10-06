#!/usr/bin/env python3
"""Mechanical coverage check for RUN/facts.json against RUN/fixtures/spec_A.md.

Checks (exit 1 if any fails):
  1. facts.json schema: every item has non-empty id/section/text/spec_sentence; ids unique;
     F01.. and H01.. are consecutive.
  2. Every spec_sentence (and every also_in entry) is a verbatim substring of spec_A.
  3. Sentence coverage: spec_A is split into sentences (paragraphs on blank lines, then on
     '.' followed by whitespace and an upper-case letter or backtick); every sentence must
     equal some fact's spec_sentence exactly.
  4. Character coverage (independent of the splitter): every non-whitespace character of
     spec_A lies inside an occurrence of some fact's spec_sentence.
  5. Prefix rule: F facts come from paragraphs 1-7, H facts from paragraphs 8-19.
  6. facts_coverage.md lists every sentence (verbatim, in order) with fact IDs; every ID exists;
     every fact appears there; each sentence lists at least the facts anchored on it.

Usage: python3 tools/check_facts_coverage.py [--spec PATH] [--facts PATH] [--coverage PATH]
Stdlib only, no network.
"""
import argparse, json, os, re, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def split_spec(text):
    paras = [p.strip().replace('\n', ' ') for p in re.split(r'\n\s*\n', text) if p.strip()]
    out = []
    for pi, p in enumerate(paras, 1):
        for s in re.split(r'(?<=\.)\s+(?=[A-Z`])', p):
            out.append((pi, s))
    return paras, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spec', default=os.path.join(RUN, 'fixtures', 'spec_A.md'))
    ap.add_argument('--facts', default=os.path.join(RUN, 'facts.json'))
    ap.add_argument('--coverage', default=os.path.join(RUN, 'facts_coverage.md'))
    a = ap.parse_args()

    spec_text = open(a.spec, encoding='utf-8').read()
    facts = json.load(open(a.facts, encoding='utf-8'))
    paras, sents = split_spec(spec_text)
    flat = '\n\n'.join(paras)
    fails = []

    # 1. schema
    ids = []
    for i, f in enumerate(facts):
        for k in ('id', 'section', 'text', 'spec_sentence'):
            if not isinstance(f.get(k), str) or not f[k].strip():
                fails.append(f'[1] item {i} missing/empty field {k!r}')
        ids.append(f.get('id'))
    if len(ids) != len(set(ids)):
        fails.append(f'[1] duplicate ids: {sorted({x for x in ids if ids.count(x) > 1})}')
    for pre in 'FH':
        got = [x for x in ids if isinstance(x, str) and x.startswith(pre)]
        want = [f'{pre}{n:02d}' for n in range(1, len(got) + 1)]
        if got != want:
            fails.append(f'[1] {pre} ids not consecutive/in order')
    bad = [x for x in ids if not (isinstance(x, str) and re.fullmatch(r'[FH]\d{2,}', x))]
    if bad:
        fails.append(f'[1] malformed ids: {bad}')

    # 2. verbatim substrings
    for f in facts:
        for s in [f.get('spec_sentence', '')] + list(f.get('also_in', [])):
            if s not in flat:
                fails.append(f"[2] {f.get('id')}: not a verbatim spec substring: {s!r}")

    # 3. sentence coverage
    anchored = {}
    for f in facts:
        anchored.setdefault(f['spec_sentence'], []).append(f['id'])
    uncovered = [(n, s) for n, (_, s) in enumerate(sents, 1) if s not in anchored]
    for n, s in uncovered:
        fails.append(f'[3] S{n:02d} has no fact: {s!r}')
    sent_set = {s for _, s in sents}
    for s, fids in anchored.items():
        if s not in sent_set:
            fails.append(f'[3] spec_sentence of {fids} is not a whole spec sentence: {s!r}')

    # 4. character coverage (no sentence splitting involved)
    covered = [False] * len(flat)
    for s in anchored:
        for m in re.finditer(re.escape(s), flat):
            for j in range(m.start(), m.end()):
                covered[j] = True
    gaps = [j for j, c in enumerate(flat) if not c.isspace() and not covered[j]]
    if gaps:
        fails.append(f'[4] {len(gaps)} non-whitespace spec characters not inside any spec_sentence, '
                     f'first at: {flat[gaps[0]:gaps[0] + 60]!r}')

    # 5. prefix rule
    para_of = {s: p for p, s in sents}
    for f in facts:
        p = para_of.get(f['spec_sentence'])
        if p is None:
            continue
        if f['id'].startswith('F') and p > 7 or f['id'].startswith('H') and p <= 7:
            fails.append(f"[5] {f['id']} anchored in paragraph {p}")

    # 6. facts_coverage.md
    md = open(a.coverage, encoding='utf-8').read()
    rows = re.findall(r'(?m)^- S(\d+): (.*?)  \n  -> (.*)$', md)
    if len(rows) != len(sents):
        fails.append(f'[6] coverage.md lists {len(rows)} sentences, spec has {len(sents)}')
    listed_ids = set()
    idset = set(ids)
    for num, s, idstr in rows:
        n = int(num)
        lid = [x.strip() for x in idstr.split(',') if x.strip()]
        listed_ids.update(lid)
        if n < 1 or n > len(sents) or sents[n - 1][1] != s:
            fails.append(f'[6] coverage.md S{num} text does not match spec sentence {n}')
            continue
        if not lid:
            fails.append(f'[6] coverage.md S{num} lists no fact')
        for x in lid:
            if x not in idset:
                fails.append(f'[6] coverage.md S{num} lists unknown id {x}')
        missing_here = set(anchored.get(s, [])) - set(lid)
        if missing_here:
            fails.append(f'[6] coverage.md S{num} omits facts anchored on it: {sorted(missing_here)}')
    not_listed = idset - listed_ids
    if not_listed:
        fails.append(f'[6] facts never listed in coverage.md: {sorted(not_listed)}')

    nF = sum(1 for x in ids if x.startswith('F'))
    print(f'spec: {len(paras)} paragraphs, {len(sents)} sentences')
    print(f'facts: {len(facts)} (F={nF}, H={len(facts) - nF}); '
          f'with ambiguity note: {sum("ambiguity" in f for f in facts)}')
    print(f'[3] sentences covered by a spec_sentence: {len(sents) - len(uncovered)}/{len(sents)}')
    print(f'[4] non-whitespace spec characters covered: '
          f'{sum(1 for j, c in enumerate(flat) if not c.isspace() and covered[j])}/'
          f'{sum(1 for c in flat if not c.isspace())}')
    print(f'[6] coverage.md rows: {len(rows)}; fact ids listed: {len(listed_ids & idset)}/{len(idset)}')
    if fails:
        print(f'RESULT: FAIL ({len(fails)} problems)')
        for x in fails:
            print('  ' + x)
        return 1
    print('RESULT: PASS (all 6 checks)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
