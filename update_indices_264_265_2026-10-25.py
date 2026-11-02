#!/usr/bin/env python3
"""Update smithribbon blog.html, index.html, sitemap.xml with modules 264 (AM) + 265 (PM), 2026-10-25."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-25"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-264-module-mill-side-brand-buyer-selvedge-cut-edge-quality-fray-resistance-edge-parallelism-"
                 "interlock-architecture-global-brand-procurement-2026-10-25-am.html"),
        "title": ("Mill-Side Brand-Buyer Selvedge &amp; Cut-Edge Quality Interlock Architecture &mdash; "
                  "Controlling Fray Resistance, Edge Parallelism and Cut Cleanliness in Ribbon Programmes 2026"),
        "desc": ("B2B ribbon OEM 264-module selvedge and cut-edge quality interlock architecture. "
                 "5-layer edge authority ladder, 4-stage edge approval gate, 3-tier edge-defect reconciliation ladder, "
                 "and a fray early-warning threshold. Smith Ribbon OEM since 2004."),
        "cat": "Selvedge &amp; Cut-Edge Quality Interlock",
    },
    {
        "file": ("blog-ribbon-oem-265-module-mill-side-brand-buyer-roll-build-packing-format-interlock-architecture-"
                 "roll-length-core-winding-direction-weight-tolerance-carton-configuration-global-brand-procurement-2026-10-25-pm.html"),
        "title": ("Mill-Side Brand-Buyer Roll-Build &amp; Packing-Format Interlock Architecture &mdash; "
                  "Controlling Roll Length, Core Specification, Winding Direction and Carton Configuration 2026"),
        "desc": ("B2B ribbon OEM 265-module roll-build and packing-format interlock architecture. "
                 "5-layer delivery-unit authority ladder, 4-stage roll approval gate, 3-tier roll-defect reconciliation "
                 "ladder, and a winding-tension early-warning threshold. Smith Ribbon OEM since 2004."),
        "cat": "Roll-Build &amp; Packing-Format Interlock",
    },
]

FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")

# ---------- standardize the footer on the new articles ----------
for art in ARTICLES:
    ap = ROOT / art["file"]
    ah = ap.read_text(encoding="utf-8")
    if FOOTER not in ah:
        marker = '<p style="font-size:0.9rem;color:#777;margin-top:2em;">Smith Ribbon OEM since 2004'
        j = ah.find(marker)
        if j == -1:
            j = ah.rfind("</body>")
        ah = ah[:j] + f'<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>\n' + ah[j:]
        ap.write_text(ah, encoding="utf-8")
        print(f"[OK] footer standardized on {art['file'][:40]}")
    else:
        print(f"[SKIP] footer already present on {art['file'][:40]}")

# ---------- blog.html (newest first: append after last </article>) ----------
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
    if i == -1:
        raise SystemExit("could not locate last </article> in blog.html")
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + "\n".join(cards) + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {len(cards)} card(s)")

# ---------- index.html ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idxh:
        print(f"[SKIP] index.html already has {art['file'][:40]}")
        continue
    m = idxh.rfind("</li>")
    if m == -1:
        raise SystemExit("no </li> found in index.html")
    m += len("</li>")
    idxh = idxh[:m] + f'\n<li><a href="blog/{art["file"]}">{art["title"]}</a></li>' + idxh[m:]
    added += 1
if added:
    ip.write_text(idxh, encoding="utf-8")
    print(f"[OK] index.html + {added} link(s)")

# ---------- sitemap.xml ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
for art in ARTICLES:
    slug = art["file"][:-5]
    if slug in sm:
        print(f"[SKIP] sitemap.xml already has {slug[:40]}")
        continue
    entry = (f'<url><loc>https://smithribbon.com/{slug}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    if ci == -1:
        raise SystemExit("</urlset> not found")
    sm = sm[:ci] + entry + sm[ci:]
sp.write_text(sm, encoding="utf-8")
print("[OK] sitemap.xml updated")

# ---------- verify ----------
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")

for art in ARTICLES:
    f = art["file"]
    slug = f[:-5]
    assert f in blog_f, f"blog.html missing {f[:40]}"
    assert f in idx_f, f"index.html missing {f[:40]}"
    assert slug in sm_f, f"sitemap.xml missing {slug[:40]}"
    assert (ROOT / f).exists(), f"article file missing {f[:40]}"
    art_html = (ROOT / f).read_text(encoding="utf-8")
    for tok in ["BlogPosting", "FAQPage", "og:title", "twitter:card", 'rel="canonical"', "<h1>",
                "article:published_time", "datePublished"]:
        assert tok in art_html, f"{f[:30]} missing {tok}"
    assert art_html.count("<h1>") == 1, f"{f[:30]} expected exactly one h1, got {art_html.count('<h1>')}"
    assert "since 2004" in art_html.lower(), f"{f[:30]} missing since 2004"
    assert FOOTER in art_html, f"{f[:30]} missing standardized footer"
    assert "XXX-Module" not in art_html, f"{f[:30]} contains spam marker"
    assert art_html.count('"@type": "FAQPage"') == 1, f"{f[:30]} FAQPage count wrong"
    assert art_html.count('"@type": "BlogPosting"') == 1, f"{f[:30]} BlogPosting count wrong"
    # JSON-LD must parse
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', art_html, re.S):
        import json
        json.loads(m.group(1))

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs: {len(locs)} vs {len(set(locs))}"

print(f"Verification OK: 2 articles linked in blog.html, index.html, sitemap.xml (valid XML, "
      f"{len(locs)} unique locs, 0 dups); BlogPosting + FAQPage + OG + canonical + one h1 confirmed")
