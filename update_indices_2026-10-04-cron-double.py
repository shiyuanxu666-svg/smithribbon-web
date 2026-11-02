#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-04 cron DOUBLE articles (modules 194 AM + 195 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Ribbon OEM E-E-A-T (Experience / Expertise / Authoritative / Trustworthy) Storytelling Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Multi-Tier Supply-Chain Risk-Mapping & 4-Tier Resilience Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Ribbon OEM E-E-A-T (Experience / Expertise / Authoritative / Trustworthy) Storytelling Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Multi-Tier Supply-Chain Risk-Mapping & 4-Tier Resilience Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-194-module-brand-buyer-mill-side-experience-expertise-authority-trustworthiness-eeat-ee-a-t-storytelling-architecture-global-brand-procurement-2026-10-04-am.html"
A2_FILE = "blog-ribbon-oem-195-module-brand-buyer-mill-side-multi-tier-supply-chain-risk-mapping-4-tier-resilience-architecture-global-brand-procurement-2026-10-04-pm.html"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    pattern = '<li><a href="blog-ribbon-oem-192-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 192 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 194/195")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-192-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>4-pillar E-E-A-T (Experience + Expertise + Authority + Trust), 7-stage trust-narrative-sprint, 5-layer evidence-graph, brand-buyer trust-signal calibration, AI-overview citation-engine. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>4-tier sub-tier risk-graph, dual-sourcing split-order, safety-stock tiering, 6-vector geopolitical-FX-weather-pandem-cyber-labor activation-trigger stack. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 192 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 194/195")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-04-am.html" in sitemap and "194" in sitemap:
    print("[SKIP] sitemap.xml already has 194/195")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-192-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-04</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-04</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 192 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 194/195")