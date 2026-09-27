#!/usr/bin/env python3
"""Update blog.html, index.html, sitemap.xml for M175 (AM) and M176 (PM) on 2026-09-27.
Idempotent: skips already-present entries.
"""
import os, re, sys

BASE = "/workspace/smithribbon-web"

AM_ID = 175
AM_FILE = "blog/blog-ribbon-oem-175-module-brand-buyer-mill-side-pre-production-sample-pps-first-article-approval-faa-protocol-mill-to-brand-handoff-architecture-global-brand-procurement-2026-09-27-am.html"
AM_TITLE = "Pre-Production-Sample (PPS) &amp; First-Article-Approval (FAA) Protocol &mdash; Mill-to-Brand Handoff Architecture for Ribbon OEM 2026"
AM_DESC = "12-stage PPS workflow, AQL-linked FAA gates, dyelot-lot traceability, brand-buyer acceptance, ramp-trigger automation. Updated 2026-09-27."
AM_DATE = "2026-09-27"

PM_ID = 176
PM_FILE = "blog/blog-ribbon-oem-176-module-brand-buyer-mill-side-ribbon-corner-radius-rounding-curve-eyelet-grommet-pre-punched-hole-geometric-tolerance-architecture-global-brand-procurement-2026-09-27-pm.html"
PM_TITLE = "Ribbon Corner-Radius Rounding-Curve Eyelet &amp; Grommet Pre-Punched-Hole Geometric-Tolerance Architecture for Brand OEM 2026"
PM_DESC = "8-axis tolerance stack-up, ISO-2768-mK calibration, eyelet-pull-strength ASTM-D2262, grommet-crush-resistance. Updated 2026-09-27."
PM_DATE = "2026-09-27"


# ============================================================
# blog.html — compact inline <article class="blog-card"><a>...</a></article> style
# ============================================================
blog_path = os.path.join(BASE, "blog.html")
with open(blog_path, "r", encoding="utf-8") as f:
    blog_html = f.read()

if "blog-ribbon-oem-176-module" in blog_html and "blog-ribbon-oem-175-module" in blog_html:
    print("blog.html: M175+M176 already present, skipping")
else:
    # Anchor: the M173 <article> block. Insert PM then AM directly before it.
    anchor = '<article class="blog-card"><a href="blog-ribbon-oem-173-module-'
    if anchor not in blog_html:
        print("ERROR: blog.html M173 anchor not found", file=sys.stderr)
        sys.exit(1)
    new_cards = (
        f'<article class="blog-card"><a href="blog-ribbon-oem-176-module-brand-buyer-mill-side-ribbon-corner-radius-rounding-curve-eyelet-grommet-pre-punched-hole-geometric-tolerance-architecture-global-brand-procurement-2026-09-27-pm.html"><h3>{PM_TITLE}</h3><p>{PM_DESC}</p></a></article>'
        f'<article class="blog-card"><a href="blog-ribbon-oem-175-module-brand-buyer-mill-side-pre-production-sample-pps-first-article-approval-faa-protocol-mill-to-brand-handoff-architecture-global-brand-procurement-2026-09-27-am.html"><h3>{AM_TITLE}</h3><p>{AM_DESC}</p></a></article>'
    )
    blog_html_new = blog_html.replace(anchor, new_cards + anchor, 1)
    with open(blog_path, "w", encoding="utf-8") as f:
        f.write(blog_html_new)
    print(f"blog.html updated, +{len(blog_html_new) - len(blog_html)} chars")


# ============================================================
# index.html — compact <li>...</li> list style
# ============================================================
index_path = os.path.join(BASE, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

if "blog-ribbon-oem-176-module" in index_html and "blog-ribbon-oem-175-module" in index_html:
    print("index.html: M175+M176 already present, skipping")
else:
    # Anchor: the M173 <li>...</li> block. Insert PM then AM directly before it.
    anchor = '<li><a href="blog-ribbon-oem-173-module-'
    if anchor not in index_html:
        print("ERROR: index.html M173 anchor not found", file=sys.stderr)
        sys.exit(1)
    new_items = (
        f'<li><a href="blog-ribbon-oem-176-module-brand-buyer-mill-side-ribbon-corner-radius-rounding-curve-eyelet-grommet-pre-punched-hole-geometric-tolerance-architecture-global-brand-procurement-2026-09-27-pm.html">{PM_TITLE}</a></li>'
        f'<li><a href="blog-ribbon-oem-175-module-brand-buyer-mill-side-pre-production-sample-pps-first-article-approval-faa-protocol-mill-to-brand-handoff-architecture-global-brand-procurement-2026-09-27-am.html">{AM_TITLE}</a></li>'
    )
    index_html_new = index_html.replace(anchor, new_items + anchor, 1)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html_new)
    print(f"index.html updated, +{len(index_html_new) - len(index_html)} chars")


# ============================================================
# sitemap.xml — insert before </urlset>
# ============================================================
sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

if "blog-ribbon-oem-176-module" in sitemap and "blog-ribbon-oem-175-module" in sitemap:
    print("sitemap.xml: M175+M176 already present, skipping")
else:
    new_entries = (
        '    <url>\n'
        '        <loc>https://smithribbon.com/blog/blog-ribbon-oem-176-module-brand-buyer-mill-side-ribbon-corner-radius-rounding-curve-eyelet-grommet-pre-punched-hole-geometric-tolerance-architecture-global-brand-procurement-2026-09-27-pm.html</loc>\n'
        '        <lastmod>2026-09-27</lastmod>\n'
        '        <changefreq>weekly</changefreq>\n'
        '        <priority>0.9</priority>\n'
        '    </url>\n'
        '    <url>\n'
        '        <loc>https://smithribbon.com/blog/blog-ribbon-oem-175-module-brand-buyer-mill-side-pre-production-sample-pps-first-article-approval-faa-protocol-mill-to-brand-handoff-architecture-global-brand-procurement-2026-09-27-am.html</loc>\n'
        '        <lastmod>2026-09-27</lastmod>\n'
        '        <changefreq>weekly</changefreq>\n'
        '        <priority>0.9</priority>\n'
        '    </url>\n'
    )
    sitemap_new = sitemap.replace("</urlset>", new_entries + "</urlset>", 1)
    if sitemap_new == sitemap:
        print("ERROR: sitemap insertion failed", file=sys.stderr)
        sys.exit(1)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_new)
    print(f"sitemap.xml updated, +{len(sitemap_new) - len(sitemap)} chars")

print("All index updates complete.")