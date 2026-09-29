#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-09-29 cron DOUBLE articles (modules 181 AM + 182 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Data-Lakehouse, Streaming-Analytics &amp; Decision-Intelligence Architecture for Ribbon OEM Brand Procurement 2026"
A2_TITLE = "Cross-Border Fulfillment, 3PL Warehouse &amp; DTC-B2B Omnichannel Distribution Architecture for Ribbon OEM 2026"
A1_H3 = "Mill-Side Data-Lakehouse, Streaming-Analytics &amp; Decision-Intelligence Architecture 2026"
A2_H3 = "Cross-Border Fulfillment, 3PL Warehouse &amp; DTC-B2B Omnichannel Distribution Architecture 2026"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
A1_FILE = "blog-ribbon-oem-181-module-brand-buyer-mill-side-mill-data-lakehouse-streaming-analytics-decision-intelligence-architecture-global-brand-procurement-2026-09-29-am.html"
A2_FILE = "blog-ribbon-oem-182-module-brand-buyer-mill-side-cross-border-fulfillment-3pl-warehouse-dtc-b2b-omnichannel-distribution-architecture-global-brand-procurement-2026-09-29-pm.html"

if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Find the 179/180 anchor block and insert 181/182 BEFORE it (most recent at top)
    pattern = '<li><a href="blog-ribbon-oem-179-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 179 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 181/182")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-179-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>Bronze-silver-gold lakehouse, 5-domain ontology, real-time KPI streaming, predictive yield-OEE, brand-buyer API, 4-tier governance. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>4-tier hub-and-spoke, DTC-B2B-marketplace-value omnichannel, returns-reverse-logistics, marketplace-FBA prep, brand-tech-stack integration. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 179 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 181/182")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-09-29-am.html" in sitemap and "181" in sitemap:
    print("[SKIP] sitemap.xml already has 181/182")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-179-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-09-29</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-09-29</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 179 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 181/182")