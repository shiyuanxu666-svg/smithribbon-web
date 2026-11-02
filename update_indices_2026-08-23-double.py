"""Wire new 2026-08-23 articles (79-am, 80-pm) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-79-module-brand-buyer-co-branded-holiday-cluster-cross-region-gifting-bundle-reverse-logistics-recovery-global-brand-procurement-2026-08-23-am.html",
        "abs_file": "blog/blog-ribbon-oem-79-module-brand-buyer-co-branded-holiday-cluster-cross-region-gifting-bundle-reverse-logistics-recovery-global-brand-procurement-2026-08-23-am.html",
        "date": "2026-08-23 10:00 AM",
        "title": "Ribbon OEM 79-Module Brand-Buyer Co-Branded Holiday-Cluster Cross-Region Gifting Bundle Reverse-Logistics Recovery Architecture 2026",
        "tag": "Brand-Buyer Co-Branded Holiday-Cluster Cross-Region Gifting Bundle Reverse-Logistics Recovery",
        "iso_date": "2026-08-23",
        "desc": "A 2026 B2B ribbon OEM 79-module brand-buyer co-branded holiday-cluster cross-region gifting bundle reverse-logistics recovery architecture for global brand owners, holiday-program-directors, retail-merchandising-VPs, and CSR / sustainability leads. Covers 9-cluster-cadre, 8-cross-region-pipeline, 7-co-branded-bundle, 6-gifting-engine, 5-recovery-CAPA, 8-cluster-archive, 6-holiday-dashboard, 4-cluster-IP, 4-cluster-cost &amp; 5-cluster-continuous-improvement modules. Delivers 92-98% 21-day-time-to-cluster-pilot-launch, 84-94% on-time-cluster-delivery, 44-58% reverse-logistics-savings, 18-26% seasonal-stockout-reduction, 63 brand partners, 27 EU-27 markets, 32 NA-states, 33 MEA-jurisdictions, 2,180 active SKUs on a 7.6M-meter annual multi-brand multi-jurisdiction co-branded holiday-cluster cross-region gifting bundle reverse-logistics program.",
        "short": "A 2026 B2B ribbon OEM 79-module brand-buyer co-branded holiday-cluster cross-region gifting bundle reverse-logistics recovery architecture for global brand owners, holiday-program-directors, retail-merchandising-VPs, and CSR / sustainability leads. Covers cluster cadre, cross region pipeline, co-branded bundle, gifting engine, recovery CAPA, and 21-day time-to-cluster-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-80-module-mill-side-closed-loop-take-back-reuse-recycling-circular-economy-brand-trade-in-recovery-global-brand-procurement-2026-08-23-pm.html",
        "abs_file": "blog/blog-ribbon-oem-80-module-mill-side-closed-loop-take-back-reuse-recycling-circular-economy-brand-trade-in-recovery-global-brand-procurement-2026-08-23-pm.html",
        "date": "2026-08-23 15:00 PM",
        "title": "Ribbon OEM 80-Module Mill-Side Closed-Loop Take-Back Reuse Recycling Circular-Economy Brand-Trade-In Recovery Architecture 2026",
        "tag": "Mill-Side Closed-Loop Take-Back Reuse Recycling Circular-Economy Brand-Trade-In Recovery",
        "iso_date": "2026-08-23",
        "desc": "A 2026 B2B ribbon OEM 80-module mill-side closed-loop take-back reuse recycling circular-economy brand-trade-in recovery architecture for global brand owners, ESG-directors, sustainability-VPs, and circular-economy-program-leads. Covers 9-circular-cadre, 8-take-back-pipeline, 7-reuse-engine, 6-recycling-line, 5-trade-in-recovery, 8-circular-archive, 6-circular-dashboard, 4-circular-IP, 4-circular-cost &amp; 5-circular-continuous-improvement modules. Delivers 92-98% 30-day-time-to-circular-pilot-launch, 84-94% take-back-capture-rate, 44-58% recycled-content-uplift, 18-26% virgin-polyester-reduction, 64 brand partners, 28 EU-27 markets, 33 NA-states, 34 MEA-jurisdictions, 2,220 active SKUs on a 7.8M-meter annual multi-brand multi-jurisdiction mill-side closed-loop take-back reuse recycling circular-economy brand-trade-in program.",
        "short": "A 2026 B2B ribbon OEM 80-module mill-side closed-loop take-back reuse recycling circular-economy brand-trade-in recovery architecture for global brand owners, ESG-directors, sustainability-VPs, and circular-economy-program-leads. Covers circular cadre, take back pipeline, reuse engine, recycling line, trade-in recovery, and 30-day time-to-circular-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the 77-pm card (latest 2026-08-22)
anchor = '<a href="blog/blog-ribbon-oem-77-module-brand-buyer-holiday-seasonality-repeat-order-90-day-calendar-cascade-production-demand-sensing-global-brand-procurement-2026-08-22-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 77-pm not found in index.html")

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

# Anchor: 77-pm blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-77-module-brand-buyer-holiday-seasonality-repeat-order-90-day-calendar-cascade-production-demand-sensing-global-brand-procurement-2026-08-22-pm.html">Ribbon OEM 77-Module Brand-Buyer Holiday-Seasonality Repeat-Order 90-Day Calendar Cascade-Production Demand-Sensing Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 77-pm not found in blog.html")

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
            <div class="blog-meta">August 23, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-78-module-brand-buyer-digital-showroom-live-configuration-ar-vr-3d-render-e-commerce-customization-global-brand-procurement-2026-08-22-pm.html"

if anchor_url not in sm:
    raise SystemExit("anchor 78-pm not found in sitemap.xml")

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
