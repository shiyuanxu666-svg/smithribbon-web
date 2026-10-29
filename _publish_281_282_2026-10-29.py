#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish smithribbon articles 281 (AM) + 282 (PM), 2026-10-29.
Updates: blog.html, index.html, sitemap.xml. Single verify pass."""
from pathlib import Path
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-29"
FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-281-module-mill-side-brand-buyer-ribbon-slit-width-tolerance-"
                 "selvedge-weave-stability-interlock-architecture-edge-parallelism-bow-symmetry-"
                 "repeat-order-width-drift-2026-10-29-am.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Slit-Width Tolerance &amp; Selvedge-Weave Stability "
                  "Interlock Architecture &mdash; Edge Parallelism, Bow Symmetry and Repeat-Order "
                  "Width Drift 2026"),
        "desc": ("A mill-side brand-buyer guide to ribbon slit-width tolerance and selvedge-weave "
                 "stability. Covers why a nominal 10 mm ribbon measures 9.4 mm at the selvedge and "
                 "10.6 mm at the centre, how loom-width tolerance and slittability interact with "
                 "bow loop symmetry, the width-versus-weave-construction trade-off, how to set a "
                 "measurement protocol that survives a change of roll width, and why width drift "
                 "shows up first in pre-tied bows rather than on the roll. Smith Ribbon OEM since 2004."),
        "cat": "Slit-Width Tolerance &amp; Selvedge Stability Interlock",
    },
    {
        "file": ("blog-ribbon-oem-282-module-mill-side-brand-buyer-ribbon-yarn-twist-direction-"
                 "twist-levelling-interlock-architecture-s-z-twist-torque-memory-balanced-bow-"
                 "hang-2026-10-29-pm.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Yarn Twist Direction &amp; Twist-Levelling Interlock "
                  "Architecture &mdash; S/Z Twist, Torque Memory and Balanced Bow Hangs 2026"),
        "desc": ("A mill-side brand-buyer guide to ribbon yarn twist direction and twist-levelling "
                 "interlock architecture. Covers why a satin ribbon with the wrong twist direction "
                 "untwists in the bow, what torque memory does to a bow over a year of shelf life, "
                 "how S-twist and Z-twist yarn interact when they meet in a woven ribbon, how to "
                 "specify twist direction so it survives slitting and conversion, and the balance "
                 "and conditioning tests that catch a twist problem before it reaches a customer. "
                 "Smith Ribbon OEM since 2004."),
        "cat": "Yarn Twist Direction &amp; Twist-Levelling Interlock",
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
    print(f"[VERIFIED] {f[:58]} | words={words} | schema={types} | faqQ={nq}")

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate locs {len(locs)} vs {len(set(locs))}"
missing = [l.replace("https://smithribbon.com/", "") for l in locs
           if l.endswith(".html") and not (ROOT / l.replace("https://smithribbon.com/", "")).exists()]
print(f"\nSitemap: {len(locs)} unique locs, {len(locs) - len(set(locs))} dups, {len(missing)} missing files")
if missing:
    print("  missing sample:", missing[:5])
print("PUBLISH VERIFY OK")
