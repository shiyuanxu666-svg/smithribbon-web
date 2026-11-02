#!/usr/bin/env python3
"""Validate the 254 / 255 articles: meta, OG, Twitter, BlogPosting JSON-LD, canonical, H1, word count."""
import json, re
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
FILES = [
    "blog-ribbon-oem-254-module-mill-side-brand-buyer-lab-dip-physical-swatch-library-colour-approval-"
    "sign-off-architecture-global-brand-procurement-2026-10-22-am.html",
    "blog-ribbon-oem-255-module-mill-side-brand-buyer-lab-dip-to-scale-up-capacity-release-"
    "yarn-ou-lot-interlock-architecture-global-brand-procurement-2026-10-22-pm.html",
]

ok = True
for f in FILES:
    p = ROOT / f
    if not p.exists():
        print(f"[FAIL] missing file {f}"); ok = False; continue
    h = p.read_text(encoding="utf-8")
    checks = {
        "title":              "<title>" in h,
        "meta description":   'name="description"' in h,
        "meta keywords":      'name="keywords"' in h,
        "meta author":        'name="author"' in h,
        "meta robots":        'name="robots"' in h,
        "canonical":          'rel="canonical"' in h,
        "og:type":            'property="og:type"' in h and 'content="article"' in h,
        "og:title":           'property="og:title"' in h,
        "og:description":     'property="og:description"' in h,
        "og:url":             'property="og:url"' in h,
        "og:image":           'property="og:image"' in h,
        "og:site_name":       'property="og:site_name"' in h,
        "article:published":  'article:published_time"' in h,
        "twitter:card":       'name="twitter:card"' in h,
        "H1":                 bool(re.search(r"<h1>", h)),
        "DOCTYPE":            h.startswith("<!DOCTYPE html>"),
        "lang=en":            'lang="en"' in h,
    }
    # JSON-LD parse
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    if not m:
        checks["JSON-LD present"] = False
    else:
        try:
            ld = json.loads(m.group(1))
            checks["JSON-LD present"] = True
            checks["JSON-LD @type=BlogPosting"] = ld.get("@type") == "BlogPosting"
            checks["JSON-LD headline"] = bool(ld.get("headline"))
            checks["JSON-LD datePublished"] = bool(ld.get("datePublished"))
            checks["JSON-LD author"] = bool(ld.get("author"))
            checks["JSON-LD publisher"] = bool(ld.get("publisher"))
            checks["JSON-LD mainEntityOfPage"] = bool(ld.get("mainEntityOfPage"))
        except Exception as e:
            checks["JSON-LD parses"] = f"PARSE ERROR {e}"

    # body word count (exclude head/style)
    body = h.split("<body>", 1)[-1]
    words = len(re.sub(r"<[^>]+>", " ", body).split())

    bad = [k for k, v in checks.items() if v is not True]
    status = "OK " if not bad and words >= 1200 else "FAIL"
    if bad or words < 1200:
        ok = False
    print(f"[{status}] {f[:62]}...")
    print(f"       bytes={len(h)}  body_words={words}  checks={len(checks)}  failed={bad if bad else 'none'}")
    # self-closing tags sanity
    for t in ("div", "table", "ul", "ol"):
        o = len(re.findall(rf"<{t}[ >]", h)); c = len(re.findall(rf"</{t}>", h))
        if o != c:
            print(f"       [WARN] <{t}> open={o} close={c}")

print("\nRESULT:", "ALL PASS" if ok else "ISSUES FOUND")