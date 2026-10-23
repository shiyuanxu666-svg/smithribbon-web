#!/usr/bin/env python3
"""Update blog.html, index.html, sitemap.xml with smithribbon module 259 (AM), 2026-10-23."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-23"

FILE = ("blog-ribbon-oem-259-module-mill-side-brand-buyer-ribbon-warp-sett-crease-reset-heat-"
        "setting-memory-retention-interlock-architecture-global-brand-procurement-2026-10-23-am.html")
TITLE = ("Mill-Side Brand-Buyer Ribbon Warp-Sett, Crease-Reset &amp; Heat-Setting Memory-Retention "
         "Interlock Architecture for Global Brand Procurement 2026")
H3 = TITLE
DESC = ("B2B ribbon OEM 259-module warp-sett, crease-reset and heat-setting memory-retention interlock "
        "architecture. 6-tier sett authority ladder, 5-stage crease-retention test protocol, 3-gate "
        "heat-set release interlock, and a fold-memory drift index for reproducible reorders. "
        "Smith Ribbon OEM since 2004.")
CAT = "Warp-Sett &amp; Fold-Memory Interlock"

# ---------- blog.html ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
if FILE in blog:
    print(f"[SKIP] blog.html already has {FILE[:40]}")
else:
    card = (
        f'<article class="post-card">\n  <a href="/{FILE}">\n'
        f'    <h3>{H3}</h3>\n  </a>\n'
        f'  <p>{DESC}</p>\n'
        f'  <div class="post-meta">{DATE} &middot; {CAT}</div>\n</article>'
    )
    i = blog.rfind("</article>")
    if i == -1:
        raise SystemExit("could not locate last </article> in blog.html")
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + card + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {FILE[:40]}")

# ---------- index.html ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
if FILE in idxh:
    print(f"[SKIP] index.html already has {FILE[:40]}")
else:
    m = idxh.rfind("</li>")
    if m == -1:
        raise SystemExit("no </li> found in index.html")
    m += len("</li>")
    ip.write_text(idxh[:m] + f'\n<li><a href="blog/{FILE}">{TITLE}</a></li>' + idxh[m:],
                 encoding="utf-8")
    print(f"[OK] index.html + {FILE[:40]}")

# ---------- sitemap.xml ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
slug = FILE[:-5]
if slug in sm:
    print(f"[SKIP] sitemap.xml already has {slug[:40]}")
else:
    entry = (f'<url><loc>https://smithribbon.com/{slug}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    if ci == -1:
        raise SystemExit("</urlset> not found")
    sp.write_text(sm[:ci] + entry + sm[ci:], encoding="utf-8")
    print(f"[OK] sitemap.xml + {slug[:40]}")

# ---------- verify ----------
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
assert FILE in (ROOT / "blog.html").read_text(encoding="utf-8"), "blog.html missing"
assert FILE in (ROOT / "index.html").read_text(encoding="utf-8"), "index.html missing"
assert slug in sm_f, "sitemap.xml missing"
assert (ROOT / FILE).exists(), "article file missing"

art = (ROOT / FILE).read_text(encoding="utf-8")
for tok in ["BlogPosting", "og:title", "twitter:card", 'rel="canonical"', "<h1>"]:
    assert tok in art, f"missing {tok}"
assert art.count("<h1>") == 1, f"expected exactly one h1, got {art.count('<h1>')}"
print(f"Verification OK: module 259 linked in blog.html, index.html, sitemap.xml (valid XML); "
      f"article {len(art):,} bytes with meta/OG/JSON-LD present")