"""Wire 2026-08-22 articles (76-am, 77-pm) into blog.html and sitemap.xml only.
index.html was already updated by update_indices_2026-08-22-double.py."""
import os
WEB = "/workspace/smithribbon-web"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-76-module-mill-side-ai-vision-defect-detection-real-time-inline-quality-edge-ai-closed-loop-global-brand-procurement-2026-08-22-am.html",
        "abs_file": "blog/blog-ribbon-oem-76-module-mill-side-ai-vision-defect-detection-real-time-inline-quality-edge-ai-closed-loop-global-brand-procurement-2026-08-22-am.html",
        "title": "Ribbon OEM 76-Module Mill-Side AI-Vision Defect-Detection Real-Time Inline-Quality Edge-AI Closed-Loop Architecture 2026",
        "tag": "Mill-Side AI-Vision Defect-Detection Real-Time Inline-Quality Edge-AI Closed-Loop",
        "iso_date": "2026-08-22",
        "short": "A 2026 B2B ribbon OEM 76-module mill-side AI-vision defect-detection real-time inline-quality edge-AI closed-loop architecture for global brand owners, QA-directors, quality-VPs, and pre-shipment-inspection leads. Covers edge-AI cadre, vision defect pipeline, inline quality engine, defect library, real-time CAPA, and 21-day time-to-vision-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-77-module-brand-buyer-holiday-seasonality-repeat-order-90-day-calendar-cascade-production-demand-sensing-global-brand-procurement-2026-08-22-pm.html",
        "abs_file": "blog/blog-ribbon-oem-77-module-brand-buyer-holiday-seasonality-repeat-order-90-day-calendar-cascade-production-demand-sensing-global-brand-procurement-2026-08-22-pm.html",
        "title": "Ribbon OEM 77-Module Brand-Buyer Holiday-Seasonality Repeat-Order 90-Day Calendar Cascade-Production Demand-Sensing Architecture 2026",
        "tag": "Brand-Buyer Holiday-Seasonality Repeat-Order 90-Day Calendar Cascade-Production Demand-Sensing",
        "iso_date": "2026-08-22",
        "short": "A 2026 B2B ribbon OEM 77-module brand-buyer holiday-seasonality repeat-order 90-day calendar cascade-production demand-sensing architecture for global brand owners, holiday-program-directors, merchandising-VPs, and seasonal-forecasting leads. Covers cascade cadre, 90-day calendar pipeline, repeat order engine, demand sensing, seasonal forecast, and 30-day time-to-cascade-pilot-launch...",
        "mins": "38 min read",
    },
]

BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

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
