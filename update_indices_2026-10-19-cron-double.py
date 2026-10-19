#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-19 cron DOUBLE articles (modules 243 + 244).
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Brand-Buyer Certification-Logic Stack Decoder Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Brand-Buyer Multi-Tier Sub-Component Supplier Carbon-Audit & Tier-4-Transparency Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Brand-Buyer Certification-Logic Stack Decoder Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Brand-Buyer Multi-Tier Sub-Component Supplier Carbon-Audit & Tier-4-Transparency Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-243-module-brand-buyer-mill-side-certification-logic-stack-decoder-architecture-global-brand-procurement-2026-10-19-am.html"
A2_FILE = "blog-ribbon-oem-244-module-brand-buyer-mill-side-multi-tier-sub-component-supplier-carbon-audit-tier-4-transparency-architecture-global-brand-procurement-2026-10-19-pm.html"

# === Update index.html — append after 242 anchor ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Mill-Side Counterfeit-Detection Quick-Response QR-Blockchain Provenance & Black-List Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 242 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 243/244")

# === Update blog.html — append after 242 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = "QR-Blockchain Provenance Black-List</div>\n</article>"
    new_block = (
        f'<article class="post-card">\n  <a href="/{A1_FILE}">\n    <h3>{A1_H3} \u2014 B2B Ribbon OEM Module 243 (2026-10-19)</h3>\n  </a>\n  <p>B2B ribbon OEM 243-module mill-side brand-buyer certification-logic stack decoder architecture for global brand procurement. 7-layer certification-logic stack, 6-pillar certification-logic-decoder governance, 6-tier certification-class assignment, certification-logic-CSM-to-brand-procurement conflict-resolution linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-19 &middot; Certification-Logic Stack Decoder</div>\n</article>\n<article class="post-card">\n  <a href="/{A2_FILE}">\n    <h3>{A2_H3} \u2014 B2B Ribbon OEM Module 244 (2026-10-19)</h3>\n  </a>\n  <p>B2B ribbon OEM 244-module mill-side brand-buyer multi-tier sub-component supplier carbon-audit &amp; tier-4-transparency architecture for global brand procurement. 7-stage sub-tier carbon-audit pipeline, 6-pillar tier-4-transparency governance, 6-tier sub-component supplier class assignment, tier-4-transparency-CSM-to-brand-procurement conflict-resolution linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-19 &middot; Multi-Tier Sub-Component Carbon-Audit Tier-4-Transparency</div>\n</article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 242 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 243/244")

# === Update sitemap.xml — add new urls ===
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
if A1_FILE in sm:
    print("[SKIP] sitemap.xml already has A1")
else:
    lastmod = "2026-10-19"
    new_urls = (
        f'<url><loc>https://smithribbon.com/{A1_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
        f'<url><loc>https://smithribbon.com/{A2_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
    )
    sm2 = sm.replace("</urlset>", new_urls + "</urlset>", 1)
    if sm2 == sm:
        print("[ERROR] sitemap.xml: </urlset> not found")
    else:
        sm_path.write_text(sm2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 243/244")