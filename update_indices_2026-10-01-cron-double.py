#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-01 cron DOUBLE articles (modules 186 AM + 187 PM)."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Buyer-Finance Trade-Finance Supplier-Financing Working-Capital Letter-of-Credit (LC) / Open-Account (OA) / DP / DA Architecture for Ribbon OEM 2026"
A2_TITLE = "Mill-Side Supplier-Onboarding 7-Stage Brief-to-Shelf Knowledge-Transfer &amp; Vendor-Ramp Architecture for Ribbon OEM 2026"
A1_H3 = "Mill-Side Buyer-Finance Trade-Finance Supplier-Financing Working-Capital LC / OA / DP / DA Architecture for Ribbon OEM 2026"
A2_H3 = "Mill-Side Supplier-Onboarding 7-Stage Brief-to-Shelf Knowledge-Transfer &amp; Vendor-Ramp Architecture for Ribbon OEM 2026"

# === Update index.html ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
A1_FILE = "blog-ribbon-oem-186-module-brand-buyer-mill-side-buyer-finance-trade-finance-supplier-financing-working-capital-letter-of-credit-lc-open-account-oa-dp-da-architecture-global-brand-procurement-2026-10-01-am.html"
A2_FILE = "blog-ribbon-oem-187-module-brand-buyer-mill-side-supplier-onboarding-7-stage-brief-to-shelf-knowledge-transfer-vendor-ramp-architecture-global-brand-procurement-2026-10-01-pm.html"

if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Find the 183/184 anchor block and insert 186/187 BEFORE it (most recent at top)
    pattern = '<li><a href="blog-ribbon-oem-183-module'
    new_block = (
        f'<li><a href="{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(pattern, new_block + pattern, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 183 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 186/187")

# === Update blog.html ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    pattern = '<article class="blog-card"><a href="blog-ribbon-oem-183-module'
    new_block = (
        f'<article class="blog-card"><a href="{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>4-tier financing-stack, UCP-600 / ISBP-745 / URDG-758 / URC-522 / ISP98 / Incoterms-2020 financial-instrument-stack, FX-hedge + multi-currency architecture, brand-buyer credit-risk visibility-dashboard. Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>7-stage brief-to-shelf sequence, 4-module knowledge-transfer SOP-playbook, IQC + PQC + FQC handoff-architecture, capacity-coordination 4-time-horizon, OTIF ramp 96-99% steady-state. Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(pattern, new_block + pattern, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 183 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 186/187")

# === Update sitemap.xml ===
sitemap_path = ROOT / "sitemap.xml"
sitemap = sitemap_path.read_text(encoding="utf-8")
if "2026-10-01-am.html" in sitemap and "186" in sitemap:
    print("[SKIP] sitemap.xml already has 186/187")
else:
    pattern = '<url><loc>https://smithribbon.com/blog/blog-ribbon-oem-183-module'
    new_block = (
        f'<url><loc>https://smithribbon.com/blog/{A1_FILE}</loc><lastmod>2026-10-01</lastmod></url>'
        f'<url><loc>https://smithribbon.com/blog/{A2_FILE}</loc><lastmod>2026-10-01</lastmod></url>'
    )
    sitemap2 = sitemap.replace(pattern, new_block + pattern, 1)
    if sitemap2 == sitemap:
        print("[ERROR] sitemap.xml: 183 anchor not found")
    else:
        sitemap_path.write_text(sitemap2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 186/187")