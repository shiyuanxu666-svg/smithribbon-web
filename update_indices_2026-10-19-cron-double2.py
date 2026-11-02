#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-19 cron DOUBLE-2 articles (modules 245 + 246).
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Brand-Buyer Holiday-Peak Q1-2027 Valentines-Easter-Mother's-Day Pre-Booking Capacity-Lock Architecture & 4-Tier Capacity-Cascade for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Brand-Buyer Vendor-Scorecard KPI Architecture & 15-KPI ESG-SQA-Sustainability-Cost-Digital 6-Tier Vendor-Class for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Brand-Buyer Holiday-Peak Q1-2027 Pre-Booking Capacity-Lock Architecture & 4-Tier Capacity-Cascade for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Brand-Buyer Vendor-Scorecard KPI Architecture & 15-KPI ESG-SQA-Sustainability-Cost-Digital 6-Tier Vendor-Class for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-245-module-brand-buyer-mill-side-holiday-peak-q1-2027-valentines-easter-mothers-day-pre-booking-capacity-lock-4-tier-capacity-cascade-architecture-global-brand-procurement-2026-10-19-am.html"
A2_FILE = "blog-ribbon-oem-246-module-brand-buyer-mill-side-vendor-scorecard-kpi-15-kpi-esg-sqa-sustainability-cost-digital-6-tier-vendor-class-architecture-global-brand-procurement-2026-10-19-pm.html"

# === Update index.html - append after 244 anchor ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Tier-4-Transparency Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 244 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 245/246")

# === Update blog.html - append after 244 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = "Multi-Tier Sub-Component Carbon-Audit Tier-4-Transparency</div>\n</article>"
    new_block = (
        f'<article class="post-card">\n  <a href="/{A1_FILE}">\n    <h3>{A1_H3} \u2014 B2B Ribbon OEM Module 245 (2026-10-19)</h3>\n  </a>\n  <p>B2B ribbon OEM 245-module mill-side brand-buyer holiday-peak Q1-2027 Valentines-Easter-Mother\'s-Day pre-booking capacity-lock architecture &amp; 4-tier capacity-cascade for global brand procurement. 4-tier capacity-cascade (Tier-1-Domestic / Tier-2-Regional / Tier-3-Export / Tier-4-Brand-Contract), 6-stage pre-booking capacity-lock pipeline, 5-pillar capacity-cascade governance, capacity-lock-CSM-to-brand-procurement holiday-forecast linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-19 &middot; Holiday-Peak Q1-2027 Capacity-Lock</div>\n</article>\n<article class="post-card">\n  <a href="/{A2_FILE}">\n    <h3>{A2_H3} \u2014 B2B Ribbon OEM Module 246 (2026-10-19)</h3>\n  </a>\n  <p>B2B ribbon OEM 246-module mill-side brand-buyer vendor-scorecard KPI architecture &amp; 15-KPI ESG-SQA-sustainability-cost-digital 6-tier vendor-class for global brand procurement. 15-KPI vendor scorecard (5xESG, 4xSQA, 3xSustainability, 2xCost, 1xDigital), 5-pillar scorecard governance, 6-tier vendor-class assignment, scorecard-CSM-to-brand-procurement linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-19 &middot; Vendor-Scorecard KPI Architecture</div>\n</article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 244 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 245/246")

# === Update sitemap.xml - add new urls ===
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
        print("[OK] sitemap.xml updated with 245/246")
