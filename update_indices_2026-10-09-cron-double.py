#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-09 cron DOUBLE articles (modules 210 AM + 211 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Digital Asset Management, Product Information Management & Master-Data-Synchronization Catalog-Syndication Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Holiday-Peak Q4 SKU Rationalization & 80/20 Velocity-Tier Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-210-module-brand-buyer-mill-side-digital-asset-management-dam-product-information-management-pim-master-data-synchronization-catalog-syndication-architecture-global-brand-procurement-2026-10-09-am.html"
A2_FILE = "blog-ribbon-oem-211-module-brand-buyer-mill-side-holiday-peak-q4-sku-rationalization-80-20-velocity-tier-architecture-global-brand-procurement-2026-10-09-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Anchor: the existing 209 entry line; insert 210 + 211 BEFORE it
    pattern = '<li><a href="blog/blog-ribbon-oem-209-module'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 209 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 210/211")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog/blog-ribbon-oem-209-module'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>7-stage catalog-syndication pipeline, 4-pillar master-data-synchronization, DAM-tokenized-asset-license, PIM-portal-ready data. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-tier velocity classification, 4-stage SKU-rationalization funnel, Pareto-curve governance, holiday-peak pre-booking. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 209 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 210/211")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-09-am.html" in sitemap and "210" in sitemap:
    print("[SKIP] sitemap.xml already has 210/211")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-209-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-09</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-09</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 209 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 210/211")