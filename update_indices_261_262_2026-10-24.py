#!/usr/bin/env python3
"""Update blog.html, index.html, sitemap.xml with smithribbon modules 261 (AM) + 262 (PM), 2026-10-24."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-24"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-261-module-mill-side-brand-buyer-ribbon-weft-sett-compression-width-edge-"
                 "stability-interlock-architecture-ribbon-oem-program-resilience-2026-10-24-am.html"),
        "title": ("Mill-Side Brand-Buyer Ribbon Weft-Sett Compression &amp; Width-Edge Stability Interlock "
                  "Architecture &mdash; Controlling Ribbon Width, Selvedge Rigidity and Weight Across a "
                  "Multi-Season Programme 2026"),
        "desc": ("B2B ribbon OEM 261-module weft-sett compression and width-edge stability interlock architecture. "
                 "5-layer sett authority ladder, 4-stage width-and-edge approval gate, 3-tier compression "
                 "reconciliation ladder, and a selvedge-rigidity early-warning threshold. Smith Ribbon OEM since 2004."),
        "cat": "Weft-Sett &amp; Width-Edge Interlock",
    },
    {
        "file": ("blog-ribbon-oem-262-module-mill-side-brand-buyer-lace-trim-elastic-recovery-edge-sealing-"
                 "differential-shrinkage-interlock-architecture-global-brand-procurement-2026-10-24-pm.html"),
        "title": ("Mill-Side Brand-Buyer Lace-Trim &amp; Elastic Recovery Interlock Architecture &mdash; "
                  "Controlling Edge Seal Quality, Stretch Retention and Differential Shrinkage in Elasticated "
                  "Trim Programmes 2026"),
        "desc": ("B2B ribbon OEM 262-module lace-trim and elastic recovery interlock architecture. "
                 "5-layer elastic authority ladder, 4-stage elastic-recovery approval gate, 3-tier shrinkage "
                 "reconciliation ladder, and a recovery-retention early-warning threshold. Smith Ribbon OEM since 2004."),
        "cat": "Elastic Recovery &amp; Edge-Seal Interlock",
    },
]

FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")

# ---------- standardize the footer on the two new articles ----------
for art in ARTICLES:
    ap = ROOT / art["file"]
    ah = ap.read_text(encoding="utf-8")
    if FOOTER not in ah:
        # insert the standardized footer line just before the closing </body>
        marker = "<p style=\"font-size:0.9rem;color:#777;margin-top:2em;\">Smith Ribbon OEM since 2004"
        j = ah.find(marker)
        if j == -1:
            j = ah.rfind("</body>")
        ah = ah[:j] + (f'<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>\n'
                       if j == ah.rfind("</body>") else
                       f'<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>\n') + ah[j:]
        ap.write_text(ah, encoding="utf-8")
        print(f"[OK] footer standardized on {art['file'][:40]}")
    else:
        print(f"[SKIP] footer already present on {art['file'][:40]}")

# ---------- blog.html (append cards at end, newest last -> but published order desc means newest FIRST) ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")

# Build all cards, insert newest (PM) first then AM, so reading order is published_time desc
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
    # newest first: reverse so PM card appears before AM card
    cards.reverse()
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

# no duplicate sitemap locs
import re
locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs: {len(locs)} vs {len(set(locs))}"

print(f"Verification OK: 2 articles linked in blog.html, index.html, sitemap.xml (valid XML, "
      f"{len(locs)} unique locs, 0 dups); both have BlogPosting + FAQPage + OG + canonical + one h1")
