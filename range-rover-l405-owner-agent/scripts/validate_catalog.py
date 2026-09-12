#!/usr/bin/env python3
"""Validate all structured L405 JSONL knowledge datasets."""
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCHEMAS = {
    "issues.jsonl": {"id","system","variants","years","issue","evidence","confidence","symptoms","hidden_clue","false_positive","verify","source"},
    "features.jsonl": {"id","category","feature","applies_to","availability","owner_value","tip_or_operation","evidence","confidence","source"},
    "procedures.jsonl": {"id","name","scope","applies_to","evidence","confidence","steps","warning","source"},
    "codes.jsonl": {"code","module","meaning","context","action","confidence","source"},
    "modules.jsonl": {"id","name","domain","role","diagnostic_value","notes","source"},
}

errors=[]
seen_global=set()
counts={}
for filename, required in SCHEMAS.items():
    path=DATA/filename
    if not path.exists():
        errors.append(f"{filename}: missing file")
        continue
    seen_local=set()
    count=0
    for n,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():
            continue
        count += 1
        try:
            row=json.loads(line)
        except Exception as e:
            errors.append(f"{filename}:{n}: invalid JSON: {e}")
            continue
        missing=required-set(row)
        if missing:
            errors.append(f"{filename}:{n}: missing {sorted(missing)}")
        key = row.get("id") or row.get("code")
        if not key:
            errors.append(f"{filename}:{n}: missing id/code key")
        elif key in seen_local:
            errors.append(f"{filename}:{n}: duplicate local key {key}")
        seen_local.add(key)
        global_key=(filename,key)
        if global_key in seen_global:
            errors.append(f"{filename}:{n}: duplicate global key {key}")
        seen_global.add(global_key)
        src=str(row.get('source',''))
        parsed=urlparse(src)
        if parsed.scheme not in {"http","https"} or not parsed.netloc:
            errors.append(f"{filename}:{n}: source is not an http(s) URL")
        for list_field in ("variants","symptoms","steps"):
            if list_field in row and not isinstance(row[list_field],list):
                errors.append(f"{filename}:{n}: {list_field} must be a list")
    counts[filename]=count

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("OK: " + ", ".join(f"{name}={counts.get(name,0)}" for name in SCHEMAS))
print(f"TOTAL: {sum(counts.values())} structured records")
