#!/usr/bin/env python3
"""Update index.html, blog.html with the 2026-10-12 cron DOUBLE articles (modules 222 AM + 223 PM).
Uses unique end-of-anchor fragments to avoid exact-byte matching issues.
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Mill-Calendar Production-Slot-Reservation &amp; Brand-Buyer-Priority-Alignment Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side Brand-Asset Library (BAL), Asset-Lifecycle &amp; Royalty-Allocation Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Mill-Calendar Production-Slot-Reservation & Brand-Buyer-Priority-Alignment Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side Brand-Asset Library (BAL), Asset-Lifecycle & Royalty-Allocation Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-222-module-brand-buyer-mill-side-mill-calendar-production-slot-reservation-brand-buyer-priority-alignment-architecture-global-brand-procurement-2026-10-12-am.html"
A2_FILE = "blog-ribbon-oem-223-module-brand-buyer-mill-side-brand-asset-library-bal-asset-lifecycle-royalty-allocation-architecture-global-brand-procurement-2026-10-12-pm.html"

# === Update index.html — anchor: end of 221 <li> ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Use the unique closing fragment of the 221 <li> that is the last article in the recent block
    anchor = 'Mill-Side Digital Artwork Pre-Press & Color-Separation Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 221 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 222/223")

# === Update blog.html — anchor: end of 221 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = '>6-stage pre-press pipeline, 4-pillar color-separation, RIP-to-engrave linkage, 3-tier substrate-calibration (textile/foil/metallic). Smith Ribbon OEM since 2004.</p></a></article>'
    new_block = (
        f'<article class="blog-card"><a href="blog/{A1_FILE}"><h3>{A1_H3}</h3>'
        f'<p>6-stage mill-calendar pipeline, 4-pillar slot-governance, slot-steward-to-line-supervisor linkage, 3-tier brand-buyer-priority (Strategic-Partner/Recurring-Volume/Project-Order). Smith Ribbon OEM since 2004.</p></a></article>'
        f'<article class="blog-card"><a href="blog/{A2_FILE}"><h3>{A2_H3}</h3>'
        f'<p>6-stage brand-asset pipeline, 4-pillar asset-governance, asset-curator-to-legal-counsel linkage, 3-tier asset-rights-class (Brand-Owned/Co-Developed/Mill-Library). Smith Ribbon OEM since 2004.</p></a></article>'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 221 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 222/223")
