"""Wire new 2026-08-25 articles (87-AM, 88-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-87-module-brand-buyer-sku-rationalization-assortment-optimization-moq-engineering-multi-market-retail-procurement-architecture-global-brand-procurement-2026-08-25-am.html",
        "abs_file": "blog/blog-ribbon-oem-87-module-brand-buyer-sku-rationalization-assortment-optimization-moq-engineering-multi-market-retail-procurement-architecture-global-brand-procurement-2026-08-25-am.html",
        "date": "2026-08-25 10:00 AM",
        "title": "Ribbon OEM 87-Module Brand-Buyer SKU Rationalization Assortment Optimization MOQ Engineering Multi-Market Retail Procurement Architecture 2026",
        "tag": "Brand-Buyer SKU Rationalization Assortment Optimization MOQ Engineering Multi-Market Retail Procurement",
        "iso_date": "2026-08-25",
        "desc": "A 2026 B2B ribbon OEM 87-module brand-buyer SKU rationalization assortment optimization MOQ engineering multi-market retail procurement architecture for global brand owners, retail-merchandising-VPs, private-label-program-directors, and assortment-planning-leads. Covers 12-SKU-rationalization-cadre, 11-assortment-optimization-engine, 10-MOQ-engineering-stack, 9-multi-market-retail-procurement-pipeline, 8-channel-mix-engine, 7-planning-archive, 9-planning-dashboard, 6-planning-IP, 6-planning-cost &amp; 9-planning-continuous-improvement modules. Delivers 92-98% 24-day-time-to-assortment-pilot-launch, 84-94% SKU-portfolio-margin-uplift, 44-58% inventory-carrying-reduction, 18-26% dead-stock-reduction, 72 brand partners, 33 EU-27 markets, 38 NA-states, 40 MEA-jurisdictions, 2,500 active SKUs on a 8.8M-meter annual multi-brand multi-jurisdiction SKU rationalization assortment optimization MOQ engineering multi-market retail procurement program.",
        "short": "A 2026 B2B ribbon OEM 87-module brand-buyer SKU rationalization assortment optimization MOQ engineering multi-market retail procurement architecture for global brand owners, retail-merchandising-VPs, private-label-program-directors, and assortment-planning-leads. Covers SKU rationalization cadre, assortment optimization engine, MOQ engineering stack, multi-market retail procurement pipeline, channel mix engine, and 24-day time-to-assortment-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-88-module-mill-side-yarn-blending-twist-texture-engineering-hand-feel-drape-premium-brand-finish-library-architecture-global-brand-procurement-2026-08-25-pm.html",
        "abs_file": "blog/blog-ribbon-oem-88-module-mill-side-yarn-blending-twist-texture-engineering-hand-feel-drape-premium-brand-finish-library-architecture-global-brand-procurement-2026-08-25-pm.html",
        "date": "2026-08-25 15:00 PM",
        "title": "Ribbon OEM 88-Module Mill-Side Yarn-Blending Twist Texture Engineering Hand-Feel Drape Premium-Brand Finish Library Architecture 2026",
        "tag": "Mill-Side Yarn-Blending Twist Texture Engineering Hand-Feel Drape Premium-Brand Finish Library",
        "iso_date": "2026-08-25",
        "desc": "A 2026 B2B ribbon OEM 88-module mill-side yarn-blending twist texture engineering hand-feel drape premium-brand finish library architecture for global brand owners, premium-finishing-VPs, beauty-fashion-luxury-merchandising-directors, and ribbon-textile-craft-leads. Covers 11-yarn-blending-cadre, 10-twist-texture-stack, 9-hand-feel-engineering-pipeline, 8-drape-cascade-engine, 7-premium-finish-library, 11-finish-archive, 9-finish-dashboard, 6-finish-IP, 6-finish-cost &amp; 10-finish-continuous-improvement modules. Delivers 92-98% 22-day-time-to-premium-finish-pilot-launch, 84-94% hand-feel-tolerance-capture, 44-58% premium-margin-uplift, 18-26% scrap-rate-reduction, 73 brand partners, 34 EU-27 markets, 39 NA-states, 41 MEA-jurisdictions, 2,540 active SKUs on a 9.0M-meter annual multi-brand multi-jurisdiction mill-side yarn-blending twist texture engineering hand-feel drape premium-brand finish library program.",
        "short": "A 2026 B2B ribbon OEM 88-module mill-side yarn-blending twist texture engineering hand-feel drape premium-brand finish library architecture for global brand owners, premium-finishing-VPs, beauty-fashion-luxury-merchandising-directors, and ribbon-textile-craft-leads. Covers yarn blending cadre, twist texture stack, hand-feel engineering pipeline, drape cascade engine, premium finish library, and 22-day time-to-premium-finish-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the 86-pm card (latest 2026-08-24)
anchor = '<a href="blog/blog-ribbon-oem-86-module-mill-side-finishing-line-thermal-uv-laser-hot-stamp-precision-tolerance-micron-grade-quality-data-twin-global-brand-procurement-2026-08-24-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 86-pm not found in index.html")

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

# Anchor: 86-pm blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-86-module-mill-side-finishing-line-thermal-uv-laser-hot-stamp-precision-tolerance-micron-grade-quality-data-twin-global-brand-procurement-2026-08-24-pm.html">Ribbon OEM 86-Module Mill-Side Finishing-Line Thermal UV Laser Hot-Stamp Precision Tolerance Micron-Grade Quality Data-Twin Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 86-pm not found in blog.html")

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
            <div class="blog-meta">August 25, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-86-module-mill-side-finishing-line-thermal-uv-laser-hot-stamp-precision-tolerance-micron-grade-quality-data-twin-global-brand-procurement-2026-08-24-pm.html"

if anchor_url not in sm:
    raise SystemExit("anchor 86-pm not found in sitemap.xml")

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
