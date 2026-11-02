#!/usr/bin/env python3
"""Diagnose + repair malformed JSON-LD on smithribbon blog pages.

Common causes: unescaped quotes inside strings (e.g. "10-module"), raw
newlines, trailing commas. Strategy: locate the offending script, try to
repair in place; if unrecoverable, drop the invalid block (a missing schema
block is far better than an invalid one, which can break rich results for
the whole page).
"""
import re, os, glob, json

ROOT = "/workspace/smithribbon-web"
report = {"repaired": [], "removed": [], "unfixable": []}

def try_repair(raw):
    """Attempt conservative fixes."""
    s = raw.strip()
    # 1. raw newlines inside strings -> \n escape (crude but effective when the
    #    only issue is literal newlines between quotes)
    try:
        return json.loads(s), "orig"
    except Exception:
        pass
    # 2. escape control chars
    s2 = re.sub(r'(?<!\\)\n(?!\s*["\}\]])', ' ', s)
    try:
        return json.loads(s2), "newline"
    except Exception:
        pass
    # 3. smart-quote / typographic quote damage inside strings
    s3 = s2.replace("\u201c", '"').replace("\u201d", '"')
    try:
        return json.loads(s3), "quotes"
    except Exception:
        pass
    # 4. trailing commas
    s4 = re.sub(r",\s*([\]\}])", r"\1", s3)
    try:
        return json.loads(s4), "trailing-comma"
    except Exception:
        pass
    # 5. combine
    try:
        return json.loads(s), "combined"
    except Exception:
        return None, None

for fp in glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True):
    rel = os.path.relpath(fp, ROOT)
    if rel.endswith("_fix_smith_sitemap_2026-10-22.py"):
        continue
    h = open(fp, encoding="utf-8", errors="ignore").read()
    blocks = list(re.finditer(
        r'<script type="application/ld\+json">(.*?)</script>', h, re.S))
    changed = False
    out = h
    for m in reversed(blocks):          # reverse so indices stay valid
        raw = m.group(1)
        try:
            json.loads(raw.strip()); continue
        except Exception:
            pass
        obj, how = try_repair(raw)
        if obj is not None:
            newraw = "\n" + json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
            out = out[:m.start(1)] + newraw + out[m.end(1):]
            report["repaired"].append((rel, how))
            changed = True
        else:
            # remove the invalid block entirely
            out = out[:m.start()] + out[m.end():]
            report["removed"].append(rel)
            changed = True
    if changed:
        open(fp, "w", encoding="utf-8").write(out)

# re-validate
still = []
for fp in glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True):
    h = open(fp, encoding="utf-8", errors="ignore").read()
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            json.loads(blob.strip())
        except Exception:
            still.append(os.path.relpath(fp, ROOT))
            break

print("repaired :", len(report["repaired"]))
print("removed  :", len(report["removed"]))
print("STILL BROKEN after repair:", len(still))
for s in still[:10]:
    print("   ", s)
json.dump({"repaired": len(report["repaired"]), "removed": len(report["removed"])},
          open("/workspace/smithribbon-web/_jsonld_fix_report.json", "w"), indent=2)