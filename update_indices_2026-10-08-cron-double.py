#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-08 cron DOUBLE articles (modules 204 AM + 205 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Holiday-Peak Q4 Reverse-Logistics Returns Clearance Recovery RMA Take-Back ReCommerce Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Multi-Market Cross-Border Tariff Engineering CBAM EU-301-Section-232 Origin-Shifting Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-204-module-brand-buyer-mill-side-holiday-peak-q4-reverse-logistics-returns-clearance-recovery-rma-take-back-recommerce-architecture-global-brand-procurement-2026-10-08-am.html"
A2_FILE = "blog-ribbon-oem-205-module-brand-buyer-mill-side-multi-market-cross-border-tariff-engineering-cbam-eu-301-section-232-origin-shifting-architecture-global-brand-procurement-2026-10-08-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog-ribbon-oem-202-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 202 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 204/205")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-202-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>10-stage post-holiday returns cascade, RMA-grade classification, recommerce-grade refurbishment workflow, 3PL-cross-dock return-freight consolidation, take-back closed-loop material recovery. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>9-stage tariff-engineering stack, CBAM-scope-3-embedded-emission accounting, EU-301-Section-232 origin-shifting waterfall, FTA-preferential-rule utilization, drawback-rebate program. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 202 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 204/205")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-08-am.html" in sitemap and "204" in sitemap:
    print("[SKIP] sitemap.xml already has 204/205")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-202-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-08</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-08</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 202 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 204/205")
