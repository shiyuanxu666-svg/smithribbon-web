"""Wire new 2026-08-21 articles (72-am, 73-pm) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-72-module-brand-buyer-digital-showroom-live-configuration-ar-vr-3d-render-e-commerce-customization-global-brand-procurement-2026-08-21-am.html",
        "abs_file": "blog/blog-ribbon-oem-72-module-brand-buyer-digital-showroom-live-configuration-ar-vr-3d-render-e-commerce-customization-global-brand-procurement-2026-08-21-am.html",
        "date": "2026-08-21 10:00 AM",
        "title": "Ribbon OEM 72-Module Brand-Buyer Digital-Showroom Live-Configuration AR-VR 3D-Render E-Commerce Customization Architecture 2026",
        "tag": "Brand-Buyer Digital-Showroom Live-Configuration AR-VR 3D-Render E-Commerce Customization",
        "iso_date": "2026-08-21",
        "desc": "A 2026 B2B ribbon OEM 72-module brand-buyer digital-showroom live-configuration AR-VR 3D-render e-commerce customization architecture for global brand owners, merchandising-directors, e-commerce-VPs, and digital-product-leads. Covers 9-digital-showroom-cadre, 8-AR-VR-render-pipeline, 7-live-configuration-engine, 6-3D-material-library, 5-ecommerce-API, 8-pantone-live-link, 6-merchandising-portal, 4-showroom-IP, 4-showroom-cost &amp; 5-showroom-continuous-improvement modules. Delivers 92-98% 14-day-time-to-showroom-go-live, 84-94% live-config-accuracy, 44-58% merchandising-cycle-savings, 18-26% e-commerce-conversion-uplift, 59 brand partners, 23 EU-27 markets, 28 NA-states, 29 MEA-jurisdictions, 2,020 active SKUs on a 6.8M-meter annual multi-brand multi-jurisdiction digital-showroom live-configuration program.",
        "short": "A 2026 B2B ribbon OEM 72-module brand-buyer digital-showroom live-configuration AR-VR 3D-render e-commerce customization architecture for global brand owners, merchandising-directors, e-commerce-VPs, and digital-product-leads. Covers digital-showroom cadre, AR-VR render pipeline, live-configuration engine, 3D material library, e-commerce API, pantone-live-link, and 14-day time-to-showroom-go-live...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-73-module-mill-side-closed-loop-water-reclaim-zero-liquid-discharge-zld-membrane-recycle-esg-water-global-brand-procurement-2026-08-21-pm.html",
        "abs_file": "blog/blog-ribbon-oem-73-module-mill-side-closed-loop-water-reclaim-zero-liquid-discharge-zld-membrane-recycle-esg-water-global-brand-procurement-2026-08-21-pm.html",
        "date": "2026-08-21 15:00 PM",
        "title": "Ribbon OEM 73-Module Mill-Side Closed-Loop Water-Reclaim Zero-Liquid-Discharge ZLD Membrane-Recycle ESG-Water Architecture 2026",
        "tag": "Mill-Side Closed-Loop Water-Reclaim Zero-Liquid-Discharge ZLD Membrane-Recycle ESG-Water",
        "iso_date": "2026-08-21",
        "desc": "A 2026 B2B ribbon OEM 73-module mill-side closed-loop water-reclaim zero-liquid-discharge ZLD membrane-recycle ESG-water architecture for global brand owners, ESG-directors, sustainability-VPs, and CDP-TCFD-CSRD-reporting-leads. Covers 9-ZLD-cadre, 8-water-reclaim-loop, 7-membrane-recycle, 6-effluent-ZLD, 5-ESG-water-disclosure, 8-CDP-TCFD-report, 6-water-dashboard, 4-water-IP, 4-water-cost &amp; 5-water-continuous-improvement modules. Delivers 92-98% 28-day-time-to-ZLD-pilot-launch, 84-94% water-reclaim-rate, 44-58% freshwater-intake-savings, 18-26% ESG-score-uplift, 60 brand partners, 24 EU-27 markets, 29 NA-states, 30 MEA-jurisdictions, 2,060 active SKUs on a 7.0M-meter annual multi-brand multi-jurisdiction closed-loop water-reclaim ZLD ESG-water program.",
        "short": "A 2026 B2B ribbon OEM 73-module mill-side closed-loop water-reclaim zero-liquid-discharge ZLD membrane-recycle ESG-water architecture for global brand owners, ESG-directors, sustainability-VPs, and CDP-TCFD-CSRD-reporting-leads. Covers ZLD cadre, water-reclaim loop, membrane recycle, effluent ZLD, ESG water-disclosure, CDP-TCFD report, and 28-day time-to-ZLD-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the just-added 71-pm2 card
anchor = '<a href="blog/blog-ribbon-oem-71-module-cross-border-logistics-3pl-multi-market-warehouse-bonded-ftz-ddp-landed-cost-orchestration-global-brand-procurement-2026-08-20-pm2.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 71-pm2 not found in index.html")

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

# Anchor: 71-pm2 blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-71-module-cross-border-logistics-3pl-multi-market-warehouse-bonded-ftz-ddp-landed-cost-orchestration-global-brand-procurement-2026-08-20-pm2.html">Ribbon OEM 71-Module Cross-Border-Logistics 3PL Multi-Market Warehouse Bonded FTZ DDP-Landed-Cost Orchestration Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 71-pm2 not found in blog.html")

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
            <div class="blog-meta">August 21, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

# Anchor: existing 71-pm2 sitemap entry
anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-71-module-cross-border-logistics-3pl-multi-market-warehouse-bonded-ftz-ddp-landed-cost-orchestration-global-brand-procurement-2026-08-20-pm2.html"

if anchor_url not in sm:
    raise SystemExit("anchor 71-pm2 not found in sitemap.xml")

# Build new sitemap entries
sm_entries = []
for e in ENTRIES:
    sm_entries.append(f"""  <url>
    <loc>https://smithribbon.com/{e['abs_file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

# Insert after 71-pm2 block; find end of url block containing anchor
idx = sm.index(anchor_url)
# Find the closing </url> after the anchor
end_url = sm.index("</url>", idx) + len("</url>")
sm = sm[:end_url] + "\n" + "\n".join(sm_entries) + sm[end_url:]

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
