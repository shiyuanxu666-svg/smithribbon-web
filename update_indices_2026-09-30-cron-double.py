#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-09-30 cron DOUBLE articles (modules 183 AM + 184 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Carbon-Footprint, LCA Scope 1-2-3 Verification &amp; CBAM Carbon-Border-Adjustment-Mechanism Compliance Architecture for Ribbon OEM 2026"
A2_TITLE = "Mill-Side Co-Innovation Joint-R&amp;D Lab Custom-Trim Designer-Residency Program Architecture for Ribbon OEM 2026"
A1_H3 = "Mill-Side Carbon-Footprint, LCA Scope 1-2-3 Verification &amp; CBAM Carbon-Border-Adjustment-Mechanism Compliance Architecture 2026"
A2_H3 = "Mill-Side Co-Innovation Joint-R&amp;D Lab Custom-Trim Designer-Residency Program Architecture 2026"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
A1_FILE = "blog-ribbon-oem-183-module-brand-buyer-mill-side-carbon-footprint-lca-scope-1-2-3-verification-cbam-carbon-border-adjustment-mechanism-compliance-architecture-global-brand-procurement-2026-09-30-am.html"
A2_FILE = "blog-ribbon-oem-184-module-brand-buyer-mill-side-co-innovation-joint-r-d-lab-custom-trim-designer-residency-program-architecture-global-brand-procurement-2026-09-30-pm.html"

if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Find the 181/182 anchor block and insert 183/184 BEFORE it (most recent at top)
    pattern = '<li><a href="blog-ribbon-oem-181-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 181 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 183/184")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-181-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>5-layer carbon-data architecture, ISO-14067 / GHG-Protocol calculation-engine, EU-CBAM / UK-CBAM / CDP / CSRD / TCFD-aligned disclosure, SGS / TUV / Bureau-Veritas third-party-verification. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-stage residency-curriculum, IP-allocation + royalty-model framework, brand-designer-mill-trilateral workflow, 4-9 month residency-cycle, trend-resonance lift. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 181 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 183/184")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-09-30-am.html" in sitemap and "183" in sitemap:
    print("[SKIP] sitemap.xml already has 183/184")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-181-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-09-30</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-09-30</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 181 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 183/184")