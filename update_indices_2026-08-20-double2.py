"""Wire new 2026-08-20 second-push articles (70-am2, 71-pm2) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-70-module-mill-side-predictive-quality-ai-vision-inline-defect-detection-closed-loop-manufacturing-global-brand-procurement-2026-08-20-am2.html",
        "abs_file": "blog/blog-ribbon-oem-70-module-mill-side-predictive-quality-ai-vision-inline-defect-detection-closed-loop-manufacturing-global-brand-procurement-2026-08-20-am2.html",
        "date": "2026-08-20 11:00 AM",
        "title": "Ribbon OEM 70-Module Mill-Side Predictive-Quality AI-Vision Inline-Defect-Detection Closed-Loop Manufacturing Architecture 2026",
        "tag": "Mill-Side Predictive-Quality AI-Vision Inline-Defect-Detection Closed-Loop Manufacturing",
        "iso_date": "2026-08-20",
        "desc": "A 2026 B2B ribbon OEM 70-module mill-side predictive-quality AI-vision inline-defect-detection closed-loop manufacturing architecture for global brand owners, quality-directors, plant-managers, and Industry-4.0-procurement-leads. Covers 9-AI-vision-cadre, 8-defect-library, 7-inference-edge, 6-closed-loop-feedback, 5-line-side-spectro, 8-defect-CAPA, 6-yield-dashboard, 4-vision-IP, 4-vision-cost &amp; 5-vision-continuous-improvement modules. Delivers 92-98% 21-day-time-to-line-pilot-launch, 84-94% inline-defect-detection-accuracy, 44-58% scrap-rate-savings, 18-26% first-pass-yield-uplift, 57 brand partners, 21 EU-27 markets, 27 NA-states, 27 MEA-jurisdictions, 1,960 active SKUs on a 6.4M-meter annual multi-brand multi-jurisdiction AI-vision closed-loop manufacturing program.",
        "short": "A 2026 B2B ribbon OEM 70-module mill-side predictive-quality AI-vision inline-defect-detection closed-loop manufacturing architecture for global brand owners, quality-directors, plant-managers, and Industry-4.0-procurement-leads. Covers AI-vision cadre, defect library, edge inference, closed-loop feedback, line-side spectro, defect CAPA, and 21-day time-to-line-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-71-module-cross-border-logistics-3pl-multi-market-warehouse-bonded-ftz-ddp-landed-cost-orchestration-global-brand-procurement-2026-08-20-pm2.html",
        "abs_file": "blog/blog-ribbon-oem-71-module-cross-border-logistics-3pl-multi-market-warehouse-bonded-ftz-ddp-landed-cost-orchestration-global-brand-procurement-2026-08-20-pm2.html",
        "date": "2026-08-20 15:00 PM",
        "title": "Ribbon OEM 71-Module Cross-Border-Logistics 3PL Multi-Market Warehouse Bonded FTZ DDP-Landed-Cost Orchestration Architecture 2026",
        "tag": "Cross-Border-Logistics 3PL Multi-Market Warehouse Bonded FTZ DDP-Landed-Cost Orchestration",
        "iso_date": "2026-08-20",
        "desc": "A 2026 B2B ribbon OEM 71-module cross-border-logistics 3PL multi-market warehouse bonded FTZ DDP-landed-cost orchestration architecture for global brand owners, logistics-directors, customs-trade-leads, and omnichannel-fulfillment-VPs. Covers 9-3PL-cadre, 8-bonded-FTZ, 7-multi-market-warehouse, 6-DDP-landed-cost, 5-customs-classification, 8-orchestration-engine, 6-track-trace, 4-logistics-IP, 4-logistics-cost &amp; 5-logistics-continuous-improvement modules. Delivers 92-98% 18-day-time-to-3PL-orchestration-go-live, 84-94% on-time-delivery-accuracy, 44-58% landed-cost-savings, 18-26% fill-rate-uplift, 58 brand partners, 22 EU-27 markets, 27 NA-states, 28 MEA-jurisdictions, 1,980 active SKUs on a 6.6M-meter annual multi-brand multi-jurisdiction cross-border-logistics orchestration program.",
        "short": "A 2026 B2B ribbon OEM 71-module cross-border-logistics 3PL multi-market warehouse bonded FTZ DDP-landed-cost orchestration architecture for global brand owners, logistics-directors, customs-trade-leads, and omnichannel-fulfillment-VPs. Covers 3PL cadre, bonded FTZ, multi-market warehouse, DDP landed-cost, customs classification, and 18-day time-to-3PL-orchestration-go-live...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the just-added 69-pm card
anchor = '<a href="blog/blog-ribbon-oem-69-module-multi-tier-sub-supplier-child-labor-forced-labor-risk-management-human-rights-due-diligence-global-brand-procurement-2026-08-20-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 69-pm not found in index.html")

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

# Anchor: 69-pm blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-69-module-multi-tier-sub-supplier-child-labor-forced-labor-risk-management-human-rights-due-diligence-global-brand-procurement-2026-08-20-pm.html">Ribbon OEM 69-Module Multi-Tier Sub-Supplier Child-Labor &amp; Forced-Labor Risk-Management Human-Rights Due-Diligence Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 69-pm not found in blog.html")

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
            <div class="blog-meta">August 20, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

# Anchor: existing 69-pm sitemap entry
anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-69-module-multi-tier-sub-supplier-child-labor-forced-labor-risk-management-human-rights-due-diligence-global-brand-procurement-2026-08-20-pm.html"

if anchor_url not in sm:
    raise SystemExit("anchor 69-pm not found in sitemap.xml")

# Build new sitemap entries
sm_entries = []
for e in ENTRIES:
    sm_entries.append(f"""  <url>
    <loc>https://smithribbon.com/{e['abs_file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

# Insert after 69-pm block; find end of url block containing anchor
idx = sm.index(anchor_url)
# Find the closing </url> after the anchor
end_url = sm.index("</url>", idx) + len("</url>")
sm = sm[:end_url] + "\n" + "\n".join(sm_entries) + sm[end_url:]

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
