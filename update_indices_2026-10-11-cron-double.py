#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-11 cron DOUBLE articles (modules 218 AM + 219 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Pre-Production Sample (PPS) Sign-Off & First-Article Approval Workflow Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Inbound Logistics, Container Loading & Freight Cost-Per-Meter Optimization Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-218-module-brand-buyer-mill-side-pre-production-sample-pps-sign-off-first-article-approval-fa-architecture-global-brand-procurement-2026-10-11-am.html"
A2_FILE = "blog-ribbon-oem-219-module-brand-buyer-mill-side-inbound-logistics-container-loading-freight-cost-per-meter-optimization-architecture-global-brand-procurement-2026-10-11-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog/blog-ribbon-oem-216-module'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 216 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 218/219")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog/blog-ribbon-oem-216-module'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>6-stage PPS-FAA pipeline, 4-pillar PPS-governance, AQL-linkage to PSI, 3-tier severity-class (critical-major-minor). Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-stage inbound-cost pipeline, 4-layer freight-mix, 3D-container-load-optimization, HS-code-driven duty-engineering. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 216 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 218/219")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "blog-ribbon-oem-218" in sitemap:
    print("[SKIP] sitemap.xml already has 218/219")
else:
    pattern = '<loc>https://smithribbon.com/blog/blog-ribbon-oem-217-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-11</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-11</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 217 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 218/219")
