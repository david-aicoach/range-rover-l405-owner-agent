#!/usr/bin/env python3
"""Search all bundled Range Rover L405 structured knowledge datasets."""
import argparse
import json
import signal
from pathlib import Path

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FILES = {
    "issue": DATA / "issues.jsonl",
    "feature": DATA / "features.jsonl",
    "procedure": DATA / "procedures.jsonl",
    "code": DATA / "codes.jsonl",
    "module": DATA / "modules.jsonl",
}

p = argparse.ArgumentParser(description="Search the bundled L405 knowledge base.")
p.add_argument("terms", nargs="*", help="All terms must match somewhere in the record")
p.add_argument("--kind", choices=["all", *FILES], default="all")
p.add_argument("--category", help="Filter category/system/domain text")
p.add_argument("--confidence", help="Filter confidence text")
p.add_argument("--compact", action="store_true", help="One JSON object per line")
a = p.parse_args()
terms = [t.casefold() for t in a.terms]

for kind, path in FILES.items():
    if a.kind != "all" and a.kind != kind:
        continue
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        hay = json.dumps(row, ensure_ascii=False).casefold()
        if terms and not all(t in hay for t in terms):
            continue
        if a.category:
            category_hay = " ".join(str(row.get(k, "")) for k in ("category", "system", "domain")).casefold()
            if a.category.casefold() not in category_hay:
                continue
        if a.confidence and a.confidence.casefold() not in str(row.get("confidence", "")).casefold():
            continue
        out = {"kind": kind, **row}
        print(json.dumps(out, ensure_ascii=False) if a.compact else json.dumps(out, ensure_ascii=False, indent=2))
