#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-10 cron DOUBLE articles (modules 213 AM + 214 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Greenfield vs. Brownfield Capacity Expansion & Investment-Grade Business-Case Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Post-Merger-Acquisition 100-Day Integration Playbook & M&A Ribbon-Procurement Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-213-module-brand-buyer-mill-side-greenfield-brownfield-capacity-expansion-investment-grade-business-case-architecture-global-brand-procurement-2026-10-10-am.html"
A2_FILE = "blog-ribbon-oem-214-module-brand-buyer-mill-side-post-merger-acquisition-100-day-integration-playbook-m-and-a-ribbon-procurement-architecture-global-brand-procurement-2026-10-10-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Anchor: the existing 211 entry line; insert 213 + 214 BEFORE it
    pattern = '<li><a href="blog/blog-ribbon-oem-211-module'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 211 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 213/214")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog/blog-ribbon-oem-211-module'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>6-stage capex-decision pipeline, 4-pillar capex-governance, capex-funding-mix optimization, post-capex ramp curriculum. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-wave 100-day M&A roadmap, 5-pillar integration governance, TSA-bridge for legacy systems, cultural-integration playbook. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 211 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 213/214")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-10-am.html" in sitemap and "213" in sitemap:
    print("[SKIP] sitemap.xml already has 213/214")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-211-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-10</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-10</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 211 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 213/214")
