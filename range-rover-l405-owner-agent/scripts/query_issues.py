#!/usr/bin/env python3
import argparse, json
from pathlib import Path

p=argparse.ArgumentParser(description='Search the bundled L405 issue catalog.')
p.add_argument('terms', nargs='*')
p.add_argument('--system')
p.add_argument('--variant')
a=p.parse_args()
path=Path(__file__).resolve().parents[1]/'data'/'issues.jsonl'
terms=[x.lower() for x in a.terms]
for line in path.read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    row=json.loads(line)
    hay=json.dumps(row).lower()
    if terms and not all(t in hay for t in terms): continue
    if a.system and a.system.lower() not in row.get('system','').lower(): continue
    if a.variant and a.variant.lower() not in ' '.join(row.get('variants',[])).lower(): continue
    print(json.dumps(row, ensure_ascii=False, indent=2))
