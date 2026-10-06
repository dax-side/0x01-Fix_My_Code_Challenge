#!/usr/bin/env python3
"""Append-only merge of per-role log files (log/*.md) into log.md, in time order.
Entry format in every log file:  '### <ISO-8601 UTC> | <role> | <entry type>' then body lines.
Already-merged entries are remembered by hash in log/.merged and never rewritten."""
import glob, hashlib, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
state = os.path.join(here, 'log', '.merged')
seen = set(open(state).read().split()) if os.path.exists(state) else set()
entries = []
for path in sorted(glob.glob(os.path.join(here, 'log', '*.md'))):
    text = open(path).read()
    for chunk in re.split(r'(?m)^(?=### )', text):
        if not chunk.startswith('### '):
            continue
        h = hashlib.sha256(chunk.strip().encode()).hexdigest()[:16]
        if h in seen:
            continue
        ts = chunk[4:].split('|', 1)[0].strip()
        entries.append((ts, os.path.basename(path), h, chunk.rstrip() + '\n'))
entries.sort()
with open(os.path.join(here, 'log.md'), 'a') as out:
    for ts, src, h, chunk in entries:
        out.write(chunk.replace('\n', f'  \n_(source: log/{src})_\n', 1) + '\n')
with open(state, 'a') as f:
    for e in entries:
        f.write(e[2] + '\n')
print(f'merged {len(entries)} new entries')
