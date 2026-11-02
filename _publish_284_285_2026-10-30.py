#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish smithribbon articles 284 (AM) + 285 (PM) - 2026-10-30.

Updates: blog.html, index.html, sitemap.xml. Single verify pass.
"""
from pathlib import Path
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-30"
FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-284-module-mill-side-brand-buyer-ribbon-width-tolerance-slitting-"
                 "edge-parallelism-bow-symmetry-drift-interlock-architecture-cut-vs-selvedge-edge-"
                 "narrow-width-stability-2026-10-30-am.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Width Tolerance &amp; Edge Parallelism Interlock Architecture "
                  "&mdash; Cut Edge vs Selvedge, Narrow-Width Stability and Bow Symmetry Drift 2026"),
        "desc": ("A mill-side brand-buyer guide to ribbon width tolerance and edge parallelism. Covers why a "
                 "width tolerance without an edge-type reference is meaningless, how a cut edge frays and "
                 "drifts differently from a self-selvage edge, why narrow widths amplify loom instability, how "
                 "width drift propagates into bow asymmetry, and the 6-part width and edge specification "
                 "template that makes a repeat order land on the same bow geometry."),
        "cat": "Ribbon Width Tolerance &amp; Edge Parallelism Interlock",
    },
    {
        "file": ("blog-ribbon-oem-285-module-mill-side-brand-buyer-ribbon-roll-packaging-format-carton-"
                 "configuration-interlock-architecture-roll-length-core-winding-direction-weight-tolerance-"
                 "moisture-barrier-loading-2026-10-30-pm.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Roll Packaging &amp; Carton Configuration Interlock Architecture "
                  "&mdash; Roll Length, Core Winding Direction, Weight Tolerance and Moisture Barrier 2026"),
        "desc": ("A mill-side brand-buyer guide to ribbon roll packaging and carton configuration. Covers why "
                 "roll length is a costing variable and not just a packing detail, how core winding direction "
                 "and rotation affect how a ribbon behaves in your converting line, why weight tolerance "
                 "matters more than length tolerance for automatic feeding, how carton format interacts with "
                 "humidity and compression damage, and the packaging specification that keeps ribbon arriving "
                 "in the same condition it left the mill in."),
        "cat": "Ribbon Roll Packaging &amp; Carton Configuration Interlock",
    },
]

# ---------- 1. footer standardisation ----------
for art in ARTICLES:
    ap = ROOT / art["file"]
    ah = ap.read_text(encoding="utf-8")
    if FOOTER not in ah:
        j = ah.rfind("</body>")
        assert j != -1, f"no </body> in {art['file']}"
        ah = ah[:j] + f'<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>\n' + ah[j:]
        ap.write_text(ah, encoding="utf-8")
        print(f"[OK] footer -> {art['file'][:50]}")
    else:
        print(f"[SKIP] footer present {art['file'][:50]}")

# ---------- 2. blog.html (newest first: insert after last </article>) ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
cards = []
for art in ARTICLES:
    if art["file"] in blog:
        print(f"[SKIP] blog.html has {art['file'][:50]}")
        continue
    cards.append(
        f'<article class="post-card">\n  <a href="/{art["file"]}">\n'
        f'    <h3>{art["title"]}</h3>\n  </a>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="post-meta">{DATE} &middot; {art["cat"]}</div>\n</article>'
    )
if cards:
    i = blog.rfind("</article>")
    assert i != -1, "no </article> in blog.html"
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + "\n".join(cards) + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {len(cards)} card(s)")

# ---------- 3. index.html (newest first: insert after last </li>) ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idxh:
        print(f"[SKIP] index.html has {art['file'][:50]}")
        continue
    m = idxh.rfind("</li>")
    assert m != -1, "no </li> in index.html"
    m += len("</li>")
    idxh = idxh[:m] + f'\n<li><a href="blog/{art["file"]}">{art["title"]}</a></li>' + idxh[m:]
    added += 1
if added:
    ip.write_text(idxh, encoding="utf-8")
    print(f"[OK] index.html + {added} link(s)")

# ---------- 4. sitemap.xml ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
for art in ARTICLES:
    slug = art["file"][:-5]
    if slug in sm:
        print(f"[SKIP] sitemap has {slug[:50]}")
        continue
    entry = (f'<url><loc>https://smithribbon.com/{slug}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    assert ci != -1, "no </urlset> in sitemap.xml"
    sm = sm[:ci] + entry + sm[ci:]
sp.write_text(sm, encoding="utf-8")
print("[OK] sitemap.xml updated")

# ================= VERIFY (single pass) =================
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")

for art in ARTICLES:
    f = art["file"]
    slug = f[:-5]
    assert f in blog_f, f"blog.html missing {f[:50]}"
    assert f in idx_f, f"index.html missing {f[:50]}"
    assert slug in sm_f, f"sitemap missing {slug[:50]}"
    ap = (ROOT / f).read_text(encoding="utf-8")
    assert ap.count("<h1>") == 1, f"h1 count {ap.count('<h1>')} in {f[:50]}"
    assert 'rel="canonical"' in ap, f"no canonical {f[:50]}"
    assert 'property="og:title"' in ap and 'property="og:image"' in ap, f"OG missing {f[:50]}"
    assert 'name="twitter:card"' in ap, f"twitter missing {f[:50]}"
    assert '<meta name="description"' in ap, f"no meta description {f[:50]}"
    assert '<h2 id="faq">' in ap, f"no visible FAQ h2 {f[:50]}"
    assert FOOTER in ap, f"footer missing {f[:50]}"
    assert "since 2004" in ap.lower(), f"no 'since 2004' {f[:50]}"
    assert "XXX-Module" not in ap, f"XXX-Module spam {f[:50]}"
    assert "2004" in ap, f"no 2004 founding year {f[:50]}"
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', ap, re.S)
    types, nq = [], 0
    for b in blocks:
        o = json.loads(b)
        types.append(o.get("@type"))
        if o.get("@type") == "FAQPage":
            nq = len(o["mainEntity"])
    assert "BlogPosting" in types, f"no BlogPosting {f[:50]}"
    assert "FAQPage" in types, f"no FAQPage {f[:50]}"
    assert "BreadcrumbList" in types, f"no BreadcrumbList {f[:50]}"
    assert ap.count("<h3>") >= nq, f"visible FAQ headings < schema questions {f[:50]}"
    assert ap.rstrip().endswith("</html>"), f"file truncated {f[:50]}"
    words = len(re.sub(r"<[^>]+>", " ", ap).split())
    assert words >= 1200, f"too short: {words} {f[:50]}"
    print(f"[VERIFIED] {f[:58]} | words={words} | schema={types} | faqQ={nq}")

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate locs {len(locs)} vs {len(set(locs))}"
missing = [l.replace("https://smithribbon.com/", "") for l in locs
           if l.endswith(".html") and not (ROOT / l.replace("https://smithribbon.com/", "")).exists()]
print(f"\nSitemap: {len(locs)} unique locs, {len(locs) - len(set(locs))} dups, {len(missing)} missing files")
if missing:
    print("  missing sample:", missing[:5])
print("PUBLISH VERIFY OK")
