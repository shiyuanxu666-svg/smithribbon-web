"""Wire new 2026-08-19 double-push articles (66-am, 67-pm) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-66-module-multi-tier-sub-supplier-chain-of-custody-mill-to-shelf-material-provenance-global-brand-procurement-2026-08-19-am.html",
        "abs_file": "blog/blog-ribbon-oem-66-module-multi-tier-sub-supplier-chain-of-custody-mill-to-shelf-material-provenance-global-brand-procurement-2026-08-19-am.html",
        "date": "2026-08-19 10:00 AM",
        "title": "Ribbon OEM 66-Module Multi-Tier Sub-Supplier Chain-of-Custody &amp; Mill-to-Shelf Material Provenance Architecture 2026",
        "tag": "Multi-Tier Sub-Supplier Chain-of-Custody &amp; Mill-to-Shelf Material Provenance",
        "iso_date": "2026-08-19",
        "desc": "A 2026 B2B ribbon OEM 66-module multi-tier sub-supplier chain-of-custody and mill-to-shelf material provenance architecture for global brand owners, ESG-directors, compliance-VPs, and procurement-leads. Covers 9-supplier-tier-mapping, 8-mill-to-shelf-trace, 7-chain-of-custody-document, 6-RTC-recycled-track, 5-OEKO-TEX-classify, 8-sub-supplier-audit, 6-tier-risk-score, 4-provenance-IP, 4-provenance-cost &amp; 5-provenance-continuous-improvement modules. Delivers 92-98% 21-day-time-to-traceability-report, 84-94% mill-to-shelf-coverage, 44-58% sub-supplier-audit-cost-savings, 18-26% brand-ESG-conversion-uplift, 53 brand partners, 18 EU-27 markets, 26 NA-states, 24 MEA-jurisdictions, 1,880 active SKUs on a 5.7M-meter annual multi-brand multi-jurisdiction chain-of-custody program.",
        "short": "A 2026 B2B ribbon OEM 66-module multi-tier sub-supplier chain-of-custody and mill-to-shelf material provenance architecture for global brand owners, ESG-directors, compliance-VPs, and procurement-leads. Covers supplier-tier-mapping, mill-to-shelf-trace, chain-of-custody documentation, RTC recycled-track, OEKO-TEX classification, and 21-day time-to-traceability-report...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-67-module-brand-buyer-quarterly-vendor-business-review-qbr-multi-year-sla-performance-global-brand-procurement-2026-08-19-pm.html",
        "abs_file": "blog/blog-ribbon-oem-67-module-brand-buyer-quarterly-vendor-business-review-qbr-multi-year-sla-performance-global-brand-procurement-2026-08-19-pm.html",
        "date": "2026-08-19 15:00 PM",
        "title": "Ribbon OEM 67-Module Brand-Buyer Quarterly Vendor Business-Review (QBR) &amp; Multi-Year SLA Performance Architecture 2026",
        "tag": "Brand-Buyer Quarterly Vendor Business-Review (QBR) &amp; Multi-Year SLA Performance",
        "iso_date": "2026-08-19",
        "desc": "A 2026 B2B ribbon OEM 67-module brand-buyer quarterly vendor business-review (QBR) and multi-year SLA performance architecture for global brand owners, vendor-managers, procurement-VPs, and supplier-quality-leads. Covers 9-QBR-cadre, 8-quarterly-KPI-scorecard, 7-SLA-uptime-monitor, 6-cost-savings-trace, 5-renewal-decision-build, 8-QBR-stakeholder-align, 6-SLA-escalation-route, 4-QBR-IP, 4-SLA-cost &amp; 5-SLA-continuous-improvement modules. Delivers 92-98% 12-day-time-to-QBR-pack, 86-96% SLA-uptime, 44-58% renewal-cost-savings, 18-26% multi-year-renewal-rate-uplift, 54 brand partners, 19 EU-27 markets, 26 NA-states, 25 MEA-jurisdictions, 1,900 active SKUs on a 5.9M-meter annual multi-brand multi-jurisdiction QBR program.",
        "short": "A 2026 B2B ribbon OEM 67-module brand-buyer quarterly vendor business-review (QBR) and multi-year SLA performance architecture for global brand owners, vendor-managers, procurement-VPs, and supplier-quality-leads. Covers QBR cadre, quarterly KPI scorecard, SLA uptime monitoring, cost-savings trace, renewal decision build, and 12-day time-to-QBR-pack...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the most recently wired (yesterday's 52-AM)
anchor = '<a href="blog/blog-ribbon-oem-52-module-recycled-content-mass-balance-chain-of-custody-audit-architecture-global-brand-procurement-2026-08-19-am.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 52-am not found in index.html")

# Insert the new cards right after the anchor card
pattern = re.escape(anchor) + r"\s*</div>"
for e in ENTRIES:
    card = f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    repl = anchor + "            </div>" + card
    new_html, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        new_html = html.replace(anchor, anchor + card, 1)
    html = new_html
    # Next insertion should anchor on the just-added card
    anchor = f'<a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: yesterday's 52-AM blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-52-module-recycled-content-mass-balance-chain-of-custody-audit-architecture-global-brand-procurement-2026-08-19-am.html">Ribbon OEM 52-Module Brand-Buyer Recycled-Content Mass-Balance &amp; Chain-of-Custody Audit Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 52-am not found in blog.html")

idx = blog.index(anchor_blog)
end_article = blog.index("</article>", idx)
insert_pt = end_article + len("</article>")

cards_parts = []
for e in ENTRIES:
    cards_parts.append(f"""

        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">August 19, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

new_urls = ""
for e in ENTRIES:
    new_urls += f"""  <url>
    <loc>{SITE}/{e['file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sm = sm.replace("</urlset>", new_urls + "</urlset>")
with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
print("DONE")
