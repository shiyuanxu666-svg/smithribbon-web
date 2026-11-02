#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Driver: write articles 296 (AM) + 297 (PM) - 2026-11-02 to smithribbon-web."""
from pathlib import Path
import importlib.util, sys

spec = importlib.util.spec_from_file_location(
    "gen", "/workspace/smithribbon-web/_gen_296_297_2026-11-02.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["gen"] = mod
spec.loader.exec_module(mod)

srl = sys.modules["srl"]

for A in (mod.A296, mod.A297):
    out = srl.write_article(
        fname=A["fname"], slug=A["slug"], title=A["title"], desc=A["desc"],
        keywords=A["keywords"], pub_iso=A["pub_iso"], wordcount=A["wordcount"],
        section=A["section"], cat_label=A["cat_label"], lede=A["lede"],
        body_html=A["body"], faq=A["faq"], cta_title=A["cta_title"],
        cta_body=A["cta_body"], cta_link_text=A["cta_link_text"])
    p = Path("/workspace/smithribbon-web") / out
    txt = p.read_text(encoding="utf-8")
    # quick self-checks
    import re
    words = len(re.sub(r"<[^>]+>", " ", A["body"]).split())
    print(f"[OK] {out}")
    print(f"     size={len(txt)}B body_words~{words} faq={len(A['faq'])} "
          f"jsonld={txt.count('application/ld+json')} faqpage={'FAQPage' in txt}")
    assert "since 2004" in txt or "Since 2004" in txt or "since 2004" in A["body"], "missing since 2004"
    assert "2007" not in txt, "stale since-2007 reference found"
    assert "id=\"faq\"" in txt, "missing visible FAQ section"
    assert "BlogPosting" in txt and "FAQPage" in txt and "BreadcrumbList" in txt
