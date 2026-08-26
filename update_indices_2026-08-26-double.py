"""Wire new 2026-08-26 articles (89-AM, 90-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-89-module-brand-buyer-supplier-scorecard-quarterly-business-review-vendor-lifecycle-qbr-cab-global-procurement-architecture-global-brand-procurement-2026-08-26-am.html",
        "abs_file": "blog/blog-ribbon-oem-89-module-brand-buyer-supplier-scorecard-quarterly-business-review-vendor-lifecycle-qbr-cab-global-procurement-architecture-global-brand-procurement-2026-08-26-am.html",
        "date": "2026-08-26 10:00 AM",
        "title": "Ribbon OEM 89-Module Brand-Buyer Supplier-Scorecard Quarterly-Business-Review Vendor-Lifecycle QBR CAB Global Procurement Architecture 2026",
        "tag": "Brand-Buyer Supplier-Scorecard Quarterly-Business-Review Vendor-Lifecycle QBR CAB Global Procurement",
        "iso_date": "2026-08-26",
        "desc": "A 2026 B2B ribbon OEM 89-module brand-buyer supplier-scorecard quarterly-business-review vendor-lifecycle QBR CAB global procurement architecture for global brand owners, procurement-VPs, supply-chain-directors, and strategic-vendor-management-leads. Covers 12-supplier-scorecard-cadre, 11-quarterly-business-review-engine, 10-vendor-lifecycle-pipeline, 9-QBR-cascade-stack, 8-CAB-governance-engine, 7-scorecard-archive, 9-scorecard-dashboard, 6-scorecard-IP, 6-scorecard-cost &amp; 10-scorecard-continuous-improvement modules. Delivers 92-98% 26-day-time-to-vendor-pilot-launch, 84-94% supplier-on-time-delivery, 44-58% vendor-cost-rationalization, 18-26% supplier-defect-reduction, 74 brand partners, 35 EU-27 markets, 40 NA-states, 42 MEA-jurisdictions, 2,580 active SKUs on a 9.2M-meter annual multi-brand multi-jurisdiction brand-buyer supplier-scorecard quarterly-business-review vendor-lifecycle QBR CAB global procurement program.",
        "short": "A 2026 B2B ribbon OEM 89-module brand-buyer supplier-scorecard quarterly-business-review vendor-lifecycle QBR CAB global procurement architecture for global brand owners, procurement-VPs, supply-chain-directors, and strategic-vendor-management-leads. Covers supplier scorecard cadre, quarterly business review engine, vendor lifecycle pipeline, QBR cascade stack, CAB governance engine, and 26-day time-to-vendor-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-90-module-mill-side-loom-maintenance-yarn-path-calibration-tension-profile-defect-prevention-architecture-premium-brand-global-brand-procurement-2026-08-26-pm.html",
        "abs_file": "blog/blog-ribbon-oem-90-module-mill-side-loom-maintenance-yarn-path-calibration-tension-profile-defect-prevention-architecture-premium-brand-global-brand-procurement-2026-08-26-pm.html",
        "date": "2026-08-26 15:00 PM",
        "title": "Ribbon OEM 90-Module Mill-Side Loom-Maintenance Yarn-Path Calibration Tension-Profile Defect-Prevention Architecture Premium-Brand 2026",
        "tag": "Mill-Side Loom-Maintenance Yarn-Path Calibration Tension-Profile Defect-Prevention Architecture Premium-Brand",
        "iso_date": "2026-08-26",
        "desc": "A 2026 B2B ribbon OEM 90-module mill-side loom-maintenance yarn-path calibration tension-profile defect-prevention architecture for premium-brand owners, ribbon-mill-engineering-VPs, weaving-production-directors, and ribbon-textile-quality-leads. Covers 11-loom-maintenance-cadre, 10-yarn-path-calibration-stack, 9-tension-profile-engineering-pipeline, 8-defect-prevention-cascade-engine, 7-premium-defect-library, 11-defect-archive, 9-defect-dashboard, 6-defect-IP, 6-defect-cost &amp; 10-defect-continuous-improvement modules. Delivers 92-98% 24-day-time-to-defect-prevention-pilot-launch, 84-94% first-pass-yield-uplift, 44-58% loom-downtime-reduction, 18-26% premium-defect-reduction, 75 brand partners, 36 EU-27 markets, 41 NA-states, 43 MEA-jurisdictions, 2,620 active SKUs on a 9.4M-meter annual multi-brand multi-jurisdiction mill-side loom-maintenance yarn-path calibration tension-profile defect-prevention architecture premium-brand program.",
        "short": "A 2026 B2B ribbon OEM 90-module mill-side loom-maintenance yarn-path calibration tension-profile defect-prevention architecture for premium-brand owners, ribbon-mill-engineering-VPs, weaving-production-directors, and ribbon-textile-quality-leads. Covers loom maintenance cadre, yarn path calibration stack, tension profile engineering pipeline, defect prevention cascade engine, premium defect library, and 24-day time-to-defect-prevention-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the 87-am card (latest in index.html)
anchor = '<a href="blog/blog-ribbon-oem-87-module-brand-buyer-sku-rationalization-assortment-optimization-moq-engineering-multi-market-retail-procurement-architecture-global-brand-procurement-2026-08-25-am.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 87-am not found in index.html")

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

# Anchor: 87-am blog-card heading (latest in blog.html)
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-87-module-brand-buyer-sku-rationalization-assortment-optimization-moq-engineering-multi-market-retail-procurement-architecture-global-brand-procurement-2026-08-25-am.html">Ribbon OEM 87-Module Brand-Buyer SKU Rationalization Assortment Optimization MOQ Engineering Multi-Market Retail Procurement Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 87-am not found in blog.html")

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
            <div class="blog-meta">August 26, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-88-module-mill-side-yarn-blending-twist-texture-engineering-hand-feel-drape-premium-brand-finish-library-architecture-global-brand-procurement-2026-08-25-pm.html"

if anchor_url not in sm:
    # fallback: 87-am
    anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-87-module-brand-buyer-sku-rationalization-assortment-optimization-moq-engineering-multi-market-retail-procurement-architecture-global-brand-procurement-2026-08-25-am.html"
    if anchor_url not in sm:
        raise SystemExit("anchor not found in sitemap.xml")

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
