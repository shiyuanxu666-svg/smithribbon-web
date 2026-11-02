#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish smithribbon articles 289 (AM) + 290 (PM) - 2026-10-31.

Updates: blog.html, index.html, sitemap.xml. Single verify pass at the end.
NOTE: these module articles live in the repo ROOT (not blog/), and their
canonical/sitemap URLs are root-level. Existing blog/ files keep their
/blog/ prefixed URLs - those are correct and must NOT be rewritten.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-31"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-289-module-mill-side-brand-buyer-ribbon-warp-yarn-tension-interlock-"
                 "architecture-warp-tension-uniformity-weft-tension-pick-density-crimp-width-drift-"
                 "print-registration-roll-build-tension-map-2026-10-31-am.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Warp &amp; Yarn Tension Interlock Architecture &mdash; "
                  "Warp Tension Uniformity, Weft Tension, Pick Density and What They Do to Width, Print "
                  "and Roll Build 2026"),
        "desc": ("A mill-side brand-buyer guide to warp and yarn tension in ribbon weaving. Covers why warp "
                 "tension uniformity across the beam matters more than the average, how weft tension and pick "
                 "density change crimp and width stability, why tension is the hidden cause behind print "
                 "registration drift and slit-width variation, how the warp beam to fabric beam tension transfer "
                 "works, and the tension record that makes a repeat order reproduce the first roll."),
        "cat": "Ribbon Warp &amp; Yarn Tension Interlock",
    },
    {
        "file": ("blog-ribbon-oem-290-module-mill-side-brand-buyer-ribbon-dyeing-handoff-colour-continuity-"
                 "interlock-architecture-greige-piece-dye-yarn-dye-route-dyehouse-change-dye-lot-approval-"
                 "retrigger-revalidation-2026-10-31-pm.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Dyeing Handoff &amp; Colour Continuity Interlock Architecture "
                  "&mdash; Greige, Piece-Dye and Yarn-Dye Routes, Dyehouse Change and the Re-Approval "
                  "Trigger 2026"),
        "desc": ("A mill-side brand-buyer guide to colour continuity across the dyeing process in a ribbon "
                 "programme. Covers how greige yarn, piece-dye and yarn-dye routes differ in what they fix and "
                 "what they leave open, why the dyehouse is a separate controlled process from the loom, what "
                 "actually changes when a mill moves dyehouse, dye supplier or yarn lot, how colour approval "
                 "should be revalidated, and the dyeing record that makes a repeat order match the first one."),
        "cat": "Ribbon Dyeing Handoff &amp; Colour Continuity Interlock",
    },
]

# ---------- 1. blog.html : insert after last </article> (newest at end = published desc) ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
cards = []
for art in ARTICLES:
    if art["file"] in blog:
        print(f"[SKIP] blog.html already has {art['file'][:40]}")
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

# ---------- 2. index.html : root-level href, inserted after last </li> ----------
ip = ROOT / "index.html"
idx = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idx:
        print(f"[SKIP] index.html already has {art['file'][:40]}")
        continue
    m = idx.rfind("</li>")
    assert m != -1, "no </li> in index.html"
    m += len("</li>")
    idx = idx[:m] + f'\n<li><a href="{art["file"]}">{art["title"]}</a></li>' + idx[m:]
    added += 1
if added:
    ip.write_text(idx, encoding="utf-8")
    print(f"[OK] index.html + {added} link(s)")

# ---------- 3. sitemap.xml : root-level loc, .html extension ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
for art in ARTICLES:
    loc = "https://smithribbon.com/" + art["file"]
    if loc in sm:
        print(f"[SKIP] sitemap has {loc[-50:]}")
        continue
    entry = (f'<url><loc>{loc}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    assert ci != -1, "no </urlset> in sitemap.xml"
    sm = sm[:ci] + entry + sm[ci:]
sp.write_text(sm, encoding="utf-8")
print("[OK] sitemap.xml updated")

# ================= VERIFY (single pass) =================
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)  # XML well-formed
locs = [l.text for l in ET.fromstring(sm_f).iter() if l.tag.endswith("loc")]
dups = len(locs) - len(set(locs))
missing = []
for l in locs:
    rel = l.replace("https://smithribbon.com/", "")
    if not (ROOT / rel).is_file():
        missing.append(rel)
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")
print(f"\n=== VERIFY ===")
print(f"sitemap locs={len(locs)} unique={len(set(locs))} dups={dups} xml=OK")
print(f"missing files={len(missing)}")
for x in missing[:10]:
    print("   MISSING:", x)
for art in ARTICLES:
    inb = art["file"] in blog_f
    ini = art["file"] in idx_f
    ins = ("https://smithribbon.com/" + art["file"]) in sm_f
    ok = all([inb, ini, ins])
    print(f"{'OK ' if ok else 'FAIL'} {art['file'][:44]}... blog={inb} index={ini} sitemap={ins}")
# confirm legacy blog/ locs untouched
legacy = [l for l in locs if "/blog/" in l]
print(f"legacy /blog/ locs in sitemap = {len(legacy)} (expected 0 - untouched)")
# confirm no future lastmod
import re
future = [l for l in sm_f.split("<lastmod>")[1:] if l[:10] > DATE]
print(f"future lastmod entries = {len(future)}")
