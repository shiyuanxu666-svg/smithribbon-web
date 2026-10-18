#!/usr/bin/env python3
"""Update index.html, blog.html, sitemap.xml with the 2026-10-18 cron DOUBLE articles (modules 239 AM + 240 PM).
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")

A1_TITLE = "Mill-Side Smart-City / Smart-Factory IoT-Edge Digital-Twin &amp; Real-Time MES Architecture for Global Brand Procurement 2026"
A2_TITLE = "Mill-Side AI-Agent Co-Pilot Brand-Procurement Decision-Support &amp; Natural-Language RFQ-Quote-Spec-Sheet Architecture for Global Brand Procurement 2026"
A1_H3 = "Mill-Side Smart-City / Smart-Factory IoT-Edge Digital-Twin & Real-Time MES Architecture for Global Brand Procurement 2026"
A2_H3 = "Mill-Side AI-Agent Co-Pilot Brand-Procurement Decision-Support & Natural-Language RFQ-Quote-Spec-Sheet Architecture for Global Brand Procurement 2026"

A1_FILE = "blog-ribbon-oem-239-module-brand-buyer-mill-side-smart-city-smart-factory-iot-edge-digital-twin-real-time-mes-architecture-global-brand-procurement-2026-10-18-am.html"
A2_FILE = "blog-ribbon-oem-240-module-brand-buyer-mill-side-ai-agent-co-pilot-brand-procurement-decision-support-natural-language-rfq-quote-spec-sheet-architecture-global-brand-procurement-2026-10-18-pm.html"

# === Update index.html — anchor: end of 237 <li> ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    anchor = 'Mill-Side AI-Blockchain Anti-Counterfeit Ribbon Provenance Authentication Architecture for Global Brand Procurement 2026</a></li>'
    new_block = (
        f'<li><a href="blog/{A1_FILE}">{A1_TITLE}</a></li>'
        f'<li><a href="blog/{A2_FILE}">{A2_TITLE}</a></li>'
    )
    idx2 = idx.replace(anchor, anchor + new_block, 1)
    if idx2 == idx:
        print("[ERROR] index.html: 237 anchor not found")
    else:
        idx_path.write_text(idx2, encoding="utf-8")
        print("[OK] index.html updated with 239/240")

# === Update blog.html — anchor: end of 237 <article> ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    anchor = '6-stage AI-blockchain anti-counterfeit pipeline, 5-pillar provenance authentication governance, 6-tier provenance-class, AI-vision-anti-counterfeit-CSM-to-verification-body linkage table. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">'
    new_block = (
        f'<article class="post-card">\n  <a href="/{A1_FILE}">\n    <h3>{A1_H3} \u2014 B2B Ribbon OEM Module 239 (2026-10-18)</h3>\n  </a>\n  <p>B2B ribbon OEM 239-module mill-side smart-city / smart-factory IoT-edge digital-twin real-time MES architecture for global brand procurement. 6-stage IoT-edge digital-twin pipeline, 5-pillar real-time-MES governance, 6-tier real-time-MES-class, IoT-edge-digital-twin-CSM-to-OEM brand-procurement linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-18 &middot; Smart-City IoT-Edge Digital-Twin Real-Time MES</div>\n</article>\n<article class="post-card">\n  <a href="/{A2_FILE}">\n    <h3>{A2_H3} \u2014 B2B Ribbon OEM Module 240 (2026-10-18)</h3>\n  </a>\n  <p>B2B ribbon OEM 240-module mill-side AI-agent co-pilot brand-procurement decision-support &amp; natural-language RFQ-quote-spec-sheet architecture for global brand procurement. 6-stage AI-agent co-pilot pipeline, 5-pillar natural-language-RFQ-quote-spec-sheet governance, 6-tier decision-support-class, AI-agent-co-pilot-CSM-to-procurement-contract linkage. Smith Ribbon OEM since 2004.</p>\n  <div class="post-meta">2026-10-18 &middot; AI-Agent Co-Pilot Brand-Procurement Decision-Support</div>\n</article>\n<article class="post-card">'
    )
    blog2 = blog.replace(anchor, anchor + new_block, 1)
    if blog2 == blog:
        print("[ERROR] blog.html: 237 anchor not found")
    else:
        blog_path.write_text(blog2, encoding="utf-8")
        print("[OK] blog.html updated with 239/240")

# === Update sitemap.xml — add new urls ===
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
if A1_FILE in sm:
    print("[SKIP] sitemap.xml already has A1")
else:
    lastmod = "2026-10-18"
    new_urls = (
        f'<url><loc>https://smithribbon.com/{A1_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
        f'<url><loc>https://smithribbon.com/{A2_FILE}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
    )
    sm2 = sm.replace("</urlset>", new_urls + "</urlset>", 1)
    if sm2 == sm:
        print("[ERROR] sitemap.xml: </urlset> not found")
    else:
        sm_path.write_text(sm2, encoding="utf-8")
        print("[OK] sitemap.xml updated with 239/240")
