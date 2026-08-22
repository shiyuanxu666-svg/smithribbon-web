"""Wire new 2026-08-22 articles (76-am, 77-pm) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-76-module-mill-side-ai-vision-defect-detection-real-time-inline-quality-edge-ai-closed-loop-global-brand-procurement-2026-08-22-am.html",
        "abs_file": "blog/blog-ribbon-oem-76-module-mill-side-ai-vision-defect-detection-real-time-inline-quality-edge-ai-closed-loop-global-brand-procurement-2026-08-22-am.html",
        "date": "2026-08-22 10:00 AM",
        "title": "Ribbon OEM 76-Module Mill-Side AI-Vision Defect-Detection Real-Time Inline-Quality Edge-AI Closed-Loop Architecture 2026",
        "tag": "Mill-Side AI-Vision Defect-Detection Real-Time Inline-Quality Edge-AI Closed-Loop",
        "iso_date": "2026-08-22",
        "desc": "A 2026 B2B ribbon OEM 76-module mill-side AI-vision defect-detection real-time inline-quality edge-AI closed-loop architecture for global brand owners, QA-directors, quality-VPs, and pre-shipment-inspection leads. Covers 9-edge-AI-cadre, 8-vision-defect-pipeline, 7-inline-quality-engine, 6-defect-library, 5-real-time-CAPA, 8-defect-archive, 6-AI-vision-dashboard, 4-vision-IP, 4-vision-cost &amp; 5-vision-continuous-improvement modules. Delivers 92-98% 21-day-time-to-vision-pilot-launch, 84-94% defect-detection-accuracy, 44-58% AQL-fail-reduction, 18-26% cost-of-quality-savings, 61 brand partners, 25 EU-27 markets, 30 NA-states, 31 MEA-jurisdictions, 2,100 active SKUs on a 7.2M-meter annual multi-brand multi-jurisdiction AI-vision inline-quality closed-loop program.",
        "short": "A 2026 B2B ribbon OEM 76-module mill-side AI-vision defect-detection real-time inline-quality edge-AI closed-loop architecture for global brand owners, QA-directors, quality-VPs, and pre-shipment-inspection leads. Covers edge-AI cadre, vision defect pipeline, inline quality engine, defect library, real-time CAPA, and 21-day time-to-vision-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-77-module-brand-buyer-holiday-seasonality-repeat-order-90-day-calendar-cascade-production-demand-sensing-global-brand-procurement-2026-08-22-pm.html",
        "abs_file": "blog/blog-ribbon-oem-77-module-brand-buyer-holiday-seasonality-repeat-order-90-day-calendar-cascade-production-demand-sensing-global-brand-procurement-2026-08-22-pm.html",
        "date": "2026-08-22 15:00 PM",
        "title": "Ribbon OEM 77-Module Brand-Buyer Holiday-Seasonality Repeat-Order 90-Day Calendar Cascade-Production Demand-Sensing Architecture 2026",
        "tag": "Brand-Buyer Holiday-Seasonality Repeat-Order 90-Day Calendar Cascade-Production Demand-Sensing",
        "iso_date": "2026-08-22",
        "desc": "A 2026 B2B ribbon OEM 77-module brand-buyer holiday-seasonality repeat-order 90-day calendar cascade-production demand-sensing architecture for global brand owners, holiday-program-directors, merchandising-VPs, and seasonal-forecasting leads. Covers 9-cascade-cadre, 8-90-day-calendar-pipeline, 7-repeat-order-engine, 6-demand-sensing, 5-seasonal-forecast, 8-cascade-capacity, 6-seasonality-dashboard, 4-cascade-IP, 4-cascade-cost &amp; 5-cascade-continuous-improvement modules. Delivers 92-98% 30-day-time-to-cascade-pilot-launch, 84-94% on-time-cascade-delivery, 44-58% safety-stock-reduction, 18-26% seasonal-stockout-reduction, 62 brand partners, 26 EU-27 markets, 31 NA-states, 32 MEA-jurisdictions, 2,140 active SKUs on a 7.4M-meter annual multi-brand multi-jurisdiction holiday-seasonality repeat-order 90-day cascade-demand-sensing program.",
        "short": "A 2026 B2B ribbon OEM 77-module brand-buyer holiday-seasonality repeat-order 90-day calendar cascade-production demand-sensing architecture for global brand owners, holiday-program-directors, merchandising-VPs, and seasonal-forecasting leads. Covers cascade cadre, 90-day calendar pipeline, repeat order engine, demand sensing, seasonal forecast, and 30-day time-to-cascade-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the just-added 75-pm card (latest 08-21)
anchor = '<a href="blog/blog-ribbon-oem-75-module-mill-side-bio-based-dyestuff-fermentation-dye-reach-compliant-carbon-reduction-architecture-global-brand-procurement-2026-08-21-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 75-pm not found in index.html")

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

# Anchor: 75-pm blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-75-module-mill-side-bio-based-dyestuff-fermentation-dye-reach-compliant-carbon-reduction-architecture-global-brand-procurement-2026-08-21-pm.html">Ribbon OEM 75-Module Mill-Side Bio-Based Dyestuff Fermentation-Dye REACH-Compliant Carbon-Reduction Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 75-pm not found in blog.html")

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
            <div class="blog-meta">August 22, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-75-module-mill-side-bio-based-dyestuff-fermentation-dye-reach-compliant-carbon-reduction-architecture-global-brand-procurement-2026-08-21-pm.html"

if anchor_url not in sm:
    raise SystemExit("anchor 75-pm not found in sitemap.xml")

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
