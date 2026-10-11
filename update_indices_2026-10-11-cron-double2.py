#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-11 cron DOUBLE2 articles (modules 220 AM + 221 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Third-Party Audit Preparation & Certification-Renewal Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Digital Artwork Pre-Press & Color-Separation Architecture for Global Brand Procurement 2026"
A1_H3 = A1_TITLE
A2_H3 = A2_TITLE

A1_FILE = "blog-ribbon-oem-220-module-brand-buyer-mill-side-third-party-audit-preparation-certification-renewal-architecture-global-brand-procurement-2026-10-11-am.html"
A2_FILE = "blog-ribbon-oem-221-module-brand-buyer-mill-side-digital-artwork-pre-press-color-separation-architecture-global-brand-procurement-2026-10-11-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog/blog-ribbon-oem-218-module'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 218 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 220/221")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog/blog-ribbon-oem-218-module'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>6-stage audit-prep pipeline, 4-pillar certification-stewardship, audit-librarian-to-surveyor linkage, 3-tier audit-tier playbook (Brand/Industry/Regulator). Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-stage pre-press pipeline, 4-pillar color-separation, RIP-to-engrave linkage, 3-tier substrate-calibration (textile/foil/metallic). Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 218 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 220/221")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "blog-ribbon-oem-220" in sitemap:
    print("[SKIP] sitemap.xml already has 220/221")
else:
    pattern = '<loc>https://smithribbon.com/blog/blog-ribbon-oem-219-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-11</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-11</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 219 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 220/221")