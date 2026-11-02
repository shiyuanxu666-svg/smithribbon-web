"""Wire new 2026-08-24 articles (85-AM, 86-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-85-module-brand-buyer-multi-channel-launch-cascade-eu-na-apac-mea-latin-america-distribution-routing-architecture-global-brand-procurement-2026-08-24-am.html",
        "abs_file": "blog/blog-ribbon-oem-85-module-brand-buyer-multi-channel-launch-cascade-eu-na-apac-mea-latin-america-distribution-routing-architecture-global-brand-procurement-2026-08-24-am.html",
        "date": "2026-08-24 10:00 AM",
        "title": "Ribbon OEM 85-Module Brand-Buyer Multi-Channel Launch Cascade EU-NA-APAC-MEA-Latin-America Distribution Routing Architecture 2026",
        "tag": "Brand-Buyer Multi-Channel Launch Cascade EU-NA-APAC-MEA-Latin-America Distribution Routing",
        "iso_date": "2026-08-24",
        "desc": "A 2026 B2B ribbon OEM 85-module brand-buyer multi-channel launch cascade EU-NA-APAC-MEA-Latin-America distribution routing architecture for global brand owners, regional-channel-directors, marketplace-fulfillment-VPs, and multi-market-launch-program-leads. Covers 11-channel-cascade-cadre, 10-EU-distribution-routing-stack, 9-NA-marketplace-pipeline, 8-APAC-3pl-pipeline, 7-MEA-distributor-engine, 6-LatAm-direct-ship-architecture, 12-multi-channel-archive, 10-launch-dashboard, 7-channel-IP, 6-channel-cost &amp; 6-channel-continuous-improvement modules. Delivers 92-98% 28-day-time-to-multi-market-pilot-launch, 84-94% on-time-channel-delivery, 44-58% cross-region-freight-savings, 18-26% channel-stockout-reduction, 70 brand partners, 31 EU-27 markets, 36 NA-states, 38 APAC-jurisdictions, 35 MEA-jurisdictions, 18 LatAm-jurisdictions, 2,420 active SKUs on a 8.4M-meter annual multi-brand multi-jurisdiction multi-channel launch cascade EU-NA-APAC-MEA-Latin-America distribution routing program.",
        "short": "A 2026 B2B ribbon OEM 85-module brand-buyer multi-channel launch cascade EU-NA-APAC-MEA-Latin-America distribution routing architecture for global brand owners, regional-channel-directors, marketplace-fulfillment-VPs, and multi-market-launch-program-leads. Covers channel cascade cadre, EU distribution routing, NA marketplace pipeline, APAC 3PL pipeline, MEA distributor engine, LatAm direct ship, and 28-day time-to-multi-market-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-86-module-mill-side-finishing-line-thermal-uv-laser-hot-stamp-precision-tolerance-micron-grade-quality-data-twin-global-brand-procurement-2026-08-24-pm.html",
        "abs_file": "blog/blog-ribbon-oem-86-module-mill-side-finishing-line-thermal-uv-laser-hot-stamp-precision-tolerance-micron-grade-quality-data-twin-global-brand-procurement-2026-08-24-pm.html",
        "date": "2026-08-24 15:00 PM",
        "title": "Ribbon OEM 86-Module Mill-Side Finishing-Line Thermal UV Laser Hot-Stamp Precision Tolerance Micron-Grade Quality Data-Twin Architecture 2026",
        "tag": "Mill-Side Finishing-Line Thermal UV Laser Hot-Stamp Precision Tolerance Micron-Grade Quality Data-Twin",
        "iso_date": "2026-08-24",
        "desc": "A 2026 B2B ribbon OEM 86-module mill-side finishing-line thermal UV laser hot-stamp precision tolerance micron-grade quality data-twin architecture for global brand owners, brand-protection-directors, premium-finishing-VPs, and luxury / beauty / fashion merchandising directors. Covers 10-finishing-cadre, 9-thermal-stack, 8-UV-stack, 7-laser-stack, 6-hot-stamp-stack, 5-precision-tolerance-engine, 11-finishing-archive, 9-finishing-dashboard, 6-finishing-IP, 6-finishing-cost &amp; 9-finishing-continuous-improvement modules. Delivers 92-98% 25-day-time-to-finishing-pilot-launch, 84-94% micron-grade-tolerance-capture, 44-58% finishing-defect-uplift, 18-26% scrap-rate-reduction, 71 brand partners, 32 EU-27 markets, 37 NA-states, 39 MEA-jurisdictions, 2,460 active SKUs on a 8.6M-meter annual multi-brand multi-jurisdiction mill-side finishing-line thermal UV laser hot-stamp precision tolerance micron-grade quality data-twin program.",
        "short": "A 2026 B2B ribbon OEM 86-module mill-side finishing-line thermal UV laser hot-stamp precision tolerance micron-grade quality data-twin architecture for global brand owners, brand-protection-directors, premium-finishing-VPs, and luxury / beauty / fashion merchandising directors. Covers finishing cadre, thermal stack, UV stack, laser stack, hot-stamp stack, precision tolerance engine, and 25-day time-to-finishing-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the 84-pm card (latest 2026-08-24)
anchor = '<a href="blog/blog-ribbon-oem-84-module-mill-side-bio-attributed-pet-rpet-feedstock-mass-balance-carbon-disclosure-architecture-global-brand-procurement-2026-08-24-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 84-pm not found in index.html")

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
    anchor = f'<a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: 84-pm blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-84-module-mill-side-bio-attributed-pet-rpet-feedstock-mass-balance-carbon-disclosure-architecture-global-brand-procurement-2026-08-24-pm.html">Ribbon OEM 84-Module Mill-Side Bio-Attributed-PET-RPET-Feedstock Mass-Balance Carbon-Disclosure Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 84-pm not found in blog.html")

# Find the FIRST occurrence (top of blog list)
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
            <div class="blog-meta">August 24, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-84-module-mill-side-bio-attributed-pet-rpet-feedstock-mass-balance-carbon-disclosure-architecture-global-brand-procurement-2026-08-24-pm.html"

if anchor_url not in sm:
    raise SystemExit("anchor 84-pm not found in sitemap.xml")

sm_entries = []
for e in ENTRIES:
    sm_entries.append(f"""  <url>
    <loc>https://smithribbon.com/{e['abs_file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

idx = sm.index(anchor_url)
end_url = sm.index("</url>", idx) + len("</url>")
sm = sm[:end_url] + "\n" + "\n".join(sm_entries) + sm[end_url:]

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
