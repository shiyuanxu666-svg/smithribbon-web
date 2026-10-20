#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with smithribbon module 251 (2026-10-21 PM)."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")

FILE = ("blog-ribbon-oem-251-module-mill-side-brand-buyer-digital-product-passport-dpp-espr-"
        "battery-passport-aligned-traceability-architecture-global-brand-procurement-2026-10-21-pm.html")
TITLE = ("Mill-Side Brand-Buyer Digital Product Passport (DPP) &amp; EU ESPR Battery-Passport-Aligned "
         "Traceability Architecture for Global Brand Procurement 2026")
H3 = ("Mill-Side Brand-Buyer Digital Product Passport (DPP) &amp; EU ESPR Battery-Passport-Aligned "
      "Traceability Architecture for Global Brand Procurement 2026")
DESC = ("B2B ribbon OEM 251-module mill-side brand-buyer digital product passport (DPP) and EU ESPR "
        "battery-passport-aligned traceability architecture for global brand procurement. 4-tier "
        "passport-data hierarchy, 6-stage passport-issuance cascade, 5-pillar passport-governance layer, "
        "6-tier passport-readiness-class assignment. Smith Ribbon OEM since 2004.")
DATE = "2026-10-21"

# ---------- blog.html ----------
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if FILE in blog:
    print("[SKIP] blog.html already has 251")
else:
    anchor = '<div class="post-meta">2026-10-20 &middot; Inbound Freight Rate-Benchmarking'
    i = blog.rfind("</article>", 0, blog.find(anchor) if anchor in blog else len(blog))
    if i == -1:
        raise SystemExit("could not locate last </article> in blog.html")
    i += len("</article>")
    card = (
        f'<article class="post-card">\n  <a href="/{FILE}">\n    <h3>{H3} &mdash; B2B Ribbon OEM Module 251 (2026-10-21)</h3>\n  </a>\n'
        f'  <p>{DESC}</p>\n  <div class="post-meta">{DATE} &middot; Digital Product Passport DPP / EU ESPR Traceability</div>\n</article>'
    )
    blog_path.write_text(blog[:i] + card + blog[i:], encoding="utf-8")
    print("[OK] blog.html updated with 251")

# ---------- index.html ----------
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if FILE in idx:
    print("[SKIP] index.html already has 251")
else:
    m = idx.rfind("</li>")
    if m == -1:
        raise SystemExit("no </li> found in index.html")
    m += len("</li>")
    idx_path.write_text(idx[:m] + f'<li><a href="blog/{FILE}">{TITLE}</a></li>' + idx[m:], encoding="utf-8")
    print("[OK] index.html updated with 251")

# ---------- sitemap.xml ----------
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
if FILE in sm:
    print("[SKIP] sitemap.xml already has 251")
else:
    entry = (f'<url><loc>https://smithribbon.com/{FILE}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    if ci == -1:
        raise SystemExit("</urlset> not found")
    sm_path.write_text(sm[:ci] + entry + sm[ci:], encoding="utf-8")
    print("[OK] sitemap.xml updated with 251")

# ---------- verify ----------
ET.fromstring(sm_path.read_text(encoding="utf-8"))
assert FILE in blog_path.read_text(encoding="utf-8"), "blog.html missing 251"
assert FILE in idx_path.read_text(encoding="utf-8"), "index.html missing 251"
print("Verification OK: module 251 linked in blog.html, index.html and sitemap.xml (valid XML)")