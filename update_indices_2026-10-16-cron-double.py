#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-16 cron DOUBLE articles (modules 232 AM + 233 PM).
"""
from pathlib import Path
import re

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Digital-Bill-of-Lading Bill-of-Exchange &amp; Blockchain-Shipment-Handoff Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side ROHS-REACH-CPSIA Substance-Compliance Substance-Declaration Harmonoized-Restricted-Substance Attestation Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Digital-Bill-of-Lading Bill-of-Exchange & Blockchain-Shipment-Handoff Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side ROHS-REACH-CPSIA Substance-Compliance Substance-Declaration Harmonoized-Restricted-Substance Attestation Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-232-module-brand-buyer-mill-side-digital-bill-of-lading-bill-of-exchange-blockchain-shipment-handoff-architecture-global-brand-procurement-2026-10-16-am.html"
A2_FILE = "blog-ribbon-oem-233-module-brand-buyer-mill-side-rohs-reach-cpsia-substance-compliance-substance-declaration-harmonized-restricted-substance-attestation-architecture-global-brand-procurement-2026-10-16-pm.html"

# === Update index.html — anchor: end of 231 <li> ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Mill-Side AI-Vision Pre-Shipment-Inspection &amp; Defect-Classification-Attribute-Fingerprinting Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 231 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 232/233")

# === Update blog.html — anchor: end of 231 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = '>6-stage AI-vision pipeline, 5-pillar pre-shipment-defect-classification governance, 3-tier AI-vision-class, vision-CSM-to-defect-library linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">'
    new_block = (
        f'<article class="post-card">\n  <a href="/{A1_FILE}">\n    <h3>{A1_H3} \u2014 B2B Ribbon OEM Module 232 (2026-10-16)</h3>\n  </a>\n  <p>B2B ribbon OEM 232-module mill-side digital-bill-of-lading bill-of-exchange blockchain-shipment-handoff architecture for global brand procurement. 6-stage digital-bill-of-lading pipeline, 5-pillar bill-of-exchange title-issuance governance, 6-tier digital-bill-of-lading-class, digital-bill-of-lading-CSM-to-trade-finance-bank linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-16 &middot; Digital-Bill-of-Lading Bill-of-Exchange</div>\n</article>\n<article class="post-card">\n  <a href="/{A2_FILE}">\n    <h3>{A2_H3} \u2014 B2B Ribbon OEM Module 233 (2026-10-16)</h3>\n  </a>\n  <p>B2B ribbon OEM 233-module mill-side ROHS-REACH-CPSIA substance-compliance substance-declaration harmonized-restricted-substance attestation architecture for global brand procurement. 6-stage ROHS-REACH-CPSIA pipeline, 5-pillar substance-declaration governance, 6-tier restricted-substance-class, ROHS-CPSIA-CSM-to-EU-27-NA-buyer linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-16 &middot; ROHS-REACH-CPSIA Substance-Compliance</div>\n</article>\n<article class="post-card">'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 231 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 232/233")

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
        print("[OK] sitemap.xml updated with 232/233")