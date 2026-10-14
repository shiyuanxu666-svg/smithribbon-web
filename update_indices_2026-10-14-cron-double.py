#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-14 cron DOUBLE articles (modules 226 AM + 227 PM).
"""
from pathlib import Path
import re

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Brand-Narrative-Protection &amp; Trade-Mark-Trademark-Custody Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Content-Marketing-Narrative &amp; Earned-Media-Coverage Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Brand-Narrative-Protection & Trade-Mark-Trademark-Custody Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Content-Marketing-Narrative & Earned-Media-Coverage Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-226-module-brand-buyer-mill-side-brand-narrative-protection-trade-mark-trademark-custody-architecture-global-brand-procurement-2026-10-14-am.html"
A2_FILE = "blog-ribbon-oem-227-module-brand-buyer-mill-side-content-marketing-narrative-earned-media-coverage-architecture-global-brand-procurement-2026-10-14-pm.html"

# === Update index.html — anchor: end of 225 <li> ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Mill-Side Vintage-Aware-Demand-Sensing &amp; Replenishment-Cadence Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 225 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 226/227")

# === Update blog.html — anchor: end of 225 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = '>6-stage vintage-aware-demand-sensing pipeline, 4-pillar replenishment-cadence-governance, vintage-CSM-to-replenishment-lead linkage, 3-tier vintage-aware-class (JIT-90-Day/VMI-180-Day/Safety-Stock-365-Day). Smith Ribbon OEM since 2004.</p></a></article>'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>6-stage brand-narrative-protection pipeline, 4-pillar trademark-custody-governance, brand-CSM-to-IP-counsel linkage, 3-tier brand-narrative-class (Global-Trademark-Registry/Regional-Trademark-Registry/Co-Branded-Gateway). Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-stage content-marketing-narrative pipeline, 4-pillar earned-media-coverage-governance, content-CSM-to-PR-lead linkage, 3-tier content-marketing-class (Global-Media-Outreach/Industry-Media-Outreach/Boutique-Blogger-Outreach). Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 225 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 226/227")

# === Update sitemap.xml — add new urls ===
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
if A1_FILE in sm:
    print("[SKIP] sitemap.xml already has A1")
else:
    lastmod = "2026-10-14"
    new_urls = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
    )
    sm2 = sm.replace("</urlset>", new_urls + "</urlset>", 1)
    if sm2 == sm:
        print("[ERROR] sitemap.xml: </urlset> not found")
    else:
        sm_path.write_text(sm2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 226/227")