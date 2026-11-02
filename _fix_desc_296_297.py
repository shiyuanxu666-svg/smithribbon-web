#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix card descriptions in blog.html / en-blog.html / index.html for articles 296 & 297.

The publish script inserted cards before the meta descriptions were shortened.
This rewrites the stale long description text inside those cards to the final
short version, so the cards match the article meta descriptions.
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

OLD296 = ("A buyer-side guide to reading ribbon certifications correctly. What OEKO-TEX Standard 100, "
          "Global Recycled Standard, FSC Chain of Custody and BSCI social compliance each do and do not "
          "prove, how certificate scope and certificate number checking works, why a certification is a "
          "supply-chain document rather than a product guarantee, and how to write marketing claims your "
          "supplier can actually substantiate.")
NEW296 = ("What ribbon certifications actually prove. A brand-buyer guide to OEKO-TEX Standard 100, GRS, "
          "FSC Chain of Custody and BSCI social compliance scope, certificate number verification and "
          "claim substantiation for packaging and trim programmes.")

OLD297 = ("A buyer-side framework for supplier relationship depth in decorative trim. The five "
          "partnership tiers, the governance cadence and escalation paths that belong at each tier, how "
          "joint business planning actually works, when a supplier should be promoted or demoted, and how "
          "to build a partnership that survives a difficult season.")
NEW297 = ("A buyer-side framework for supplier relationship depth in decorative trim: the five partnership "
          "tiers, governance cadence and escalation paths, joint business planning, promotion and demotion "
          "criteria.")

PAIRS = [(OLD296, NEW296), (OLD297, NEW297)]

for fname in ["blog.html", "en-blog.html", "index.html"]:
    p = ROOT / fname
    t = p.read_text(encoding="utf-8")
    n = 0
    for old, new in PAIRS:
        # descriptions may be HTML-escaped in some files; handle both
        for o, nw in [(old, new),
                      (old.replace("&", "&amp;"), new.replace("&", "&amp;"))]:
            if o in t:
                t = t.replace(o, nw)
                n += 1
                break
    if n:
        p.write_text(t, encoding="utf-8")
    print(f"{fname}: {n} description(s) updated")
