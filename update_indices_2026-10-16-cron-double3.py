#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-16 cron DOUBLE-3 articles (modules 234 AM + 235 PM).
"""
from pathlib import Path
import re

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Bonded-Warehouse Bond-Zone Cargo-Identity Custody-Title-Governance Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Carbon-Credit-Class Voluntary-Market-Asset-Title-Custody Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Bonded-Warehouse Bond-Zone Cargo-Identity Custody-Title-Governance Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Carbon-Credit-Class Voluntary-Market-Asset-Title-Custody Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-234-module-brand-buyer-mill-side-bonded-warehouse-bond-zone-cargo-identity-custody-title-governance-architecture-global-brand-procurement-2026-10-16-am.html"
A2_FILE = "blog-ribbon-oem-235-module-brand-buyer-mill-side-carbon-credit-class-voluntary-market-asset-title-custody-architecture-global-brand-procurement-2026-10-16-pm.html"

# === Update index.html — anchor: end of 233 <li> ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Find the 232/233 anchor (latest entries just added in this morning's cron)
    anchor = 'Mill-Side ROHS-REACH-CPSIA Substance-Compliance Substance-Declaration Harmonoized-Restricted-Substance Attestation Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 233 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 234/235")

# === Update blog.html — anchor: end of 233 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = '<div class="post-meta">2026-10-16 &middot; ROHS-REACH-CPSIA Substance-Compliance</div>\n</article>'
    new_block = (
        anchor + '\n' +
        f'<article class="post-card">\n  <a href="/{A1_FILE}">\n    <h3>{A1_H3} \u2014 B2B Ribbon OEM Module 234 (2026-10-16)</h3>\n  </a>\n  <p>B2B ribbon OEM 234-module mill-side bonded-warehouse bond-zone cargo-identity custody-title-governance architecture for global brand procurement. 6-stage bonded-warehouse-custody pipeline, 5-pillar bond-zone-cargo-identity governance, 6-tier bonded-warehouse-class, bonded-warehouse-CSM-to-customs-broker linkage table. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-16 &middot; Bonded-Warehouse Bond-Zone Cargo-Identity Custody-Title-Governance</div>\n</article>\n' +
        f'<article class="post-card">\n  <a href="/{A2_FILE}">\n    <h3>{A2_H3} \u2014 B2B Ribbon OEM Module 235 (2026-10-16)</h3>\n  </a>\n  <p>B2B ribbon OEM 235-module mill-side carbon-credit-class voluntary-market-asset-title-custody architecture for global brand procurement. 6-stage carbon-credit-class pipeline, 5-pillar carbon-credit-asset-title-custody governance, 6-tier carbon-credit-class assignment, carbon-credit-class-CSM-to-verification-body-as-a-v linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-16 &middot; Carbon-Credit-Class Voluntary-Market-Asset-Title-Custody</div>\n</article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 233 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 234/235")

# === Update sitemap.xml — add new urls ===
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
if A1_FILE in sm:
    print("[SKIP] sitemap.xml already has A1")
else:
    lastmod = "2026-10-16"
    new_urls = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
    )
    sm2 = sm.replace("</urlset>", new_urls + "</urlset>", 1)
    if sm2 == sm:
        print("[ERROR] sitemap.xml: </urlset> not found")
    else:
        sm_path.write_text(sm2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 234/235")