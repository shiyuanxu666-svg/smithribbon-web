#!/usr/bin/env python3
"""Update smithribbon blog.html, index.html, sitemap.xml with modules 266 (AM) + 267 (PM), 2026-10-25."""
from pathlib import Path
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-25"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-266-module-mill-side-brand-buyer-fringing-end-thread-finish-interlock-architecture-"
                 "loose-end-thread-control-cut-end-binding-fringe-trim-termination-global-brand-procurement-2026-10-25-am.html"),
        "title": ("Mill-Side Brand-Buyer Fringing &amp; End-Thread Finish Interlock Architecture &mdash; "
                  "Controlling Loose End Threads, Cut-End Binding and Fringe Trim Termination 2026"),
        "desc": ("B2B ribbon OEM 266-module fringing and end-thread finish interlock architecture. "
                 "5-layer end-finish authority ladder, 4-stage end-finish approval gate, 3-tier end-defect "
                 "reconciliation ladder, and a loose-thread early-warning threshold. Smith Ribbon OEM since 2004."),
        "cat": "Fringing &amp; End-Thread Finish Interlock",
    },
    {
        "file": ("blog-ribbon-oem-267-module-mill-side-brand-buyer-drawstring-cord-component-interlock-architecture-"
                 "cord-diameter-core-style-cordlock-aglet-pull-force-performance-global-brand-procurement-2026-10-25-pm.html"),
        "title": ("Mill-Side Brand-Buyer Drawstring &amp; Cord-Component Interlock Architecture &mdash; "
                  "Controlling Cord Diameter, Core Style, Cordlock Function, Aglet Finishing and Pull Force 2026"),
        "desc": ("B2B ribbon OEM 267-module drawstring and cord-component interlock architecture. "
                 "5-layer cord-component authority ladder, 4-stage cord assembly approval gate, 3-tier cord-defect "
                 "reconciliation ladder, and a pull-force drift early-warning threshold. Smith Ribbon OEM since 2004."),
        "cat": "Drawstring &amp; Cord-Component Interlock",
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
# NOTE: these modules live at repo root (not in blog/), so the sitemap URL is
# root-level: https://smithribbon.com/<slug>  -- matching modules 264/265.
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
    # word count (visible prose only, excluding JSON-LD)
    prose = re.sub(r'<script type="application/ld\+json">.*?</script>', ' ', art_html, flags=re.S)
    prose = re.sub(r'<[^>]+>', ' ', prose)
    wc = len(prose.split())
    assert wc >= 1200, f"{f[:30]} only {wc} visible words"
    print(f"[OK] {f[:46]}... visible words={wc}")
    # JSON-LD must parse
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', art_html, re.S):
        json.loads(m.group(1))

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs: {len(locs)} vs {len(set(locs))}"

print(f"Verification OK: 2 articles linked in blog.html, index.html, sitemap.xml (valid XML, "
      f"{len(locs)} unique locs, 0 dups); BlogPosting + FAQPage + OG + canonical + one h1 confirmed")
