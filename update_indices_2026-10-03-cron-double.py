#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-03 cron DOUBLE articles (modules 192 AM + 193 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Ribbon OEM Customization Certification-Stack Decoder Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Factory-Cooperation Partnership Long-Term-Strategy Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Ribbon OEM Customization Certification-Stack Decoder Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Factory-Cooperation Partnership Long-Term-Strategy Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-192-module-brand-buyer-mill-side-ribbon-customization-certification-stack-decoder-global-brand-procurement-architecture-2026-10-03-am.html"
A2_FILE = "blog-ribbon-oem-193-module-brand-buyer-mill-side-factory-cooperation-partnership-long-term-strategy-global-brand-procurement-architecture-2026-10-03-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog-ribbon-oem-190-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 190 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 192/193")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-190-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>4-tier certification-decoder-stack, OEKO-TEX / GRS / FSC / GOTS / BSCI / SEDEX-SMETA / ISO 9001 / ISO 14001 / REACH / CPSIA brand-buyer-audit-mapping, procurement-compliance-mesh. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>Tier-1 strategic-partner designation, 5-pillar partnership-mesh, 3-5-7-year joint-roadmap, gain-share / pain-share 60-40 / 70-30 / 50-50 model, joint-governance-committee. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 190 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 192/193")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-03-am.html" in sitemap and "192" in sitemap:
    print("[SKIP] sitemap.xml already has 192/193")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-190-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-03</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-03</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 190 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 192/193")