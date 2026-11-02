#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-18 cron DOUBLE-2 articles (modules 241 AM + 242 PM).
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Multi-Brand Co-Branding Cross-Licensing Royalty-Engine & B2B Ribbon OEM Program Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Counterfeit-Detection Quick-Response QR-Blockchain Provenance & Black-List Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Multi-Brand Co-Branding Cross-Licensing Royalty-Engine & B2B Ribbon OEM Program Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Counterfeit-Detection Quick-Response QR-Blockchain Provenance & Black-List Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-241-module-brand-buyer-mill-side-multi-brand-co-branding-cross-licensing-royalty-engine-b2b-ribbon-oem-program-architecture-global-brand-procurement-2026-10-18-am.html"
A2_FILE = "blog-ribbon-oem-242-module-brand-buyer-mill-side-counterfeit-detection-quick-response-qr-blockchain-provenance-black-list-architecture-global-brand-procurement-2026-10-18-pm.html"

# === Update index.html — append after 240 anchor ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Mill-Side AI-Agent Co-Pilot Brand-Procurement Decision-Support &amp; Natural-Language RFQ-Quote-Spec-Sheet Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 240 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 241/242")

# === Update blog.html — append after 240 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    # find the 240 article tag and append the new ones after it
    # search for the closing of the 240 article (post-meta with "AI-Agent Co-Pilot Brand-Procurement Decision-Support")
    anchor = "AI-Agent Co-Pilot Brand-Procurement Decision-Support</div>\n</article>"
    new_block = (
        f'<article class="post-card">\n  <a href="/{A1_FILE}">\n    <h3>{A1_H3} \u2014 B2B Ribbon OEM Module 241 (2026-10-18)</h3>\n  </a>\n  <p>B2B ribbon OEM 241-module mill-side multi-brand co-branding cross-licensing royalty-engine B2B ribbon OEM program architecture for global brand procurement. 6-stage co-branding cross-licensing pipeline, 5-pillar royalty-engine governance, 6-tier royalty-class assignment, co-branding-cross-licensing-CSM-to-brand-procurement royalty-reporting linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-18 &middot; Multi-Brand Co-Branding Cross-Licensing Royalty-Engine</div>\n</article>\n<article class="post-card">\n  <a href="/{A2_FILE}">\n    <h3>{A2_H3} \u2014 B2B Ribbon OEM Module 242 (2026-10-18)</h3>\n  </a>\n  <p>B2B ribbon OEM 242-module mill-side counterfeit-detection quick-response QR-blockchain provenance black-list architecture for global brand procurement. 6-stage QR-blockchain provenance pipeline, 5-pillar counterfeit-detection black-list governance, 6-tier counterfeit-class, QR-blockchain-provenance-CSM-to-brand-procurement loss-prevention legal-enforcement linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-18 &middot; QR-Blockchain Provenance Black-List</div>\n</article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 240 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 241/242")

# === Update sitemap.xml — add new urls ===
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
if A1_FILE in sm:
    print("[SKIP] sitemap.xml already has A1")
else:
    lastmod = "2026-10-18"
    new_urls = (
        f'<url><loc>https://smithribbon.com/{A1_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
        f'<url><loc>https://smithribbon.com/{A2_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
    )
    sm2 = sm.replace("</urlset>", new_urls + "</urlset>", 1)
    if sm2 == sm:
        print("[ERROR] sitemap.xml: </urlset> not found")
    else:
        sm_path.write_text(sm2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 241/242")
