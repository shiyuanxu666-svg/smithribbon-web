#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-05 cron DOUBLE articles (modules 196 AM + 197 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Quality-Issue, AQL Defect-Library & 8D Root-Cause Supplier-Recovery CAPA Playbook v2.0 Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Go-to-Market (GTM) Launch-Sample-Pack Co-Marketing & Brand-Launch GTM-Playbook Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-196-module-brand-buyer-mill-side-quality-issue-aql-defect-library-8d-root-cause-supplier-recovery-capa-playbook-v2-architecture-global-brand-procurement-2026-10-05-am.html"
A2_FILE = "blog-ribbon-oem-197-module-brand-buyer-mill-side-go-to-market-launch-sample-pack-co-marketing-gtm-playbook-architecture-global-brand-procurement-2026-10-05-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog-ribbon-oem-194-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 194 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 196/197")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-194-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>9-category AQL defect-library, 5-tier AQL defect-severity matrix, 8-stage 8D root-cause analysis, 6-pillar CAPA playbook v2.0, brand-buyer-witness scorecard. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>5-stage brand-launch cascade, 4-tower launch-sample-pack pillar, co-marketing brand-launch asset library, retailer-onboarding kit, sell-through telemetry. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 194 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 196/197")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-05-am.html" in sitemap and "196" in sitemap:
    print("[SKIP] sitemap.xml already has 196/197")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-194-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-05</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-05</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 194 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 196/197")