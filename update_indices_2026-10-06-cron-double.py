#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-06 cron DOUBLE articles (modules 198 AM + 199 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Private-Label Collection-Program 7-Pillar Launch-Architecture for Global Brand Buyers 2026"
A2_TITLE = "Mill-Side Holiday-Peak Demand-Sensing 12-Month Capacity Pre-Booking Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-198-module-brand-buyer-mill-side-private-label-collection-program-7-pillar-launch-architecture-global-brand-procurement-2026-10-06-am.html"
A2_FILE = "blog-ribbon-oem-199-module-brand-buyer-mill-side-holiday-peak-demand-sensing-12-month-capacity-pre-booking-architecture-global-brand-procurement-2026-10-06-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog-ribbon-oem-196-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 196 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 198/199")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-196-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>7-stage collection-cascade, 5-tower SKU-curation, retailer-buyer onboarding-kit, demand-sensing telemetry, replenishment-rhythm, line-review architecture, sell-through-loop. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>12-month capacity calendar, 4-tier pre-booking cascade, AI demand-sensing engine, 3-stage forecast-sync, brand-buyer lock-in window, safety-stock buffer. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 196 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 198/199")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-06-am.html" in sitemap and "198" in sitemap:
    print("[SKIP] sitemap.xml already has 198/199")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-196-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-06</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-06</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 196 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 198/199")
