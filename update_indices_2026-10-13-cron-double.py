#!/usr/bin/env python3
"""Update index.html, blog.html with the 2026-10-13 cron DOUBLE articles (modules 224 AM + 225 PM).
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Brand-Relationship-Lifecycle &amp; Co-Innovation-Cadence Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Vintage-Aware-Demand-Sensing &amp; Replenishment-Cadence Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Brand-Relationship-Lifecycle & Co-Innovation-Cadence Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Vintage-Aware-Demand-Sensing & Replenishment-Cadence Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-224-module-brand-buyer-mill-side-brand-relationship-lifecycle-co-innovation-cadence-architecture-global-brand-procurement-2026-10-13-am.html"
A2_FILE = "blog-ribbon-oem-225-module-brand-buyer-mill-side-vintage-aware-demand-sensing-replenishment-cadence-architecture-global-brand-procurement-2026-10-13-pm.html"

# === Update index.html — anchor: end of 223 <li> ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Mill-Side Brand-Asset Library (BAL), Asset-Lifecycle &amp; Royalty-Allocation Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 223 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 224/225")

# === Update blog.html — anchor: end of 223 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = '>6-stage brand-asset pipeline, 4-pillar asset-governance, asset-curator-to-legal-counsel linkage, 3-tier asset-rights-class (Brand-Owned/Co-Developed/Mill-Library). Smith Ribbon OEM since 2004.</p></a></article>'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>6-stage brand-engagement pipeline, 4-pillar co-innovation-governance, brand-CSM-to-innovation-lead linkage, 3-tier brand-engagement-class (Strategic-Co-Create/Joint-Develop/Trusted-Supplier). Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-stage vintage-aware-demand-sensing pipeline, 4-pillar replenishment-cadence-governance, vintage-CSM-to-replenishment-lead linkage, 3-tier vintage-aware-class (JIT-90-Day/VMI-180-Day/Safety-Stock-365-Day). Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 223 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 224/225")
