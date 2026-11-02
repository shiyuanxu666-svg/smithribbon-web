"""Wire new 2026-08-28 articles (94-AM, 95-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-94-module-brand-buyer-cross-border-ecommerce-marketplace-listing-amazon-fba-tiktok-shop-tmall-compliance-architecture-global-brand-procurement-2026-08-28-am.html",
        "abs_file": "blog/blog-ribbon-oem-94-module-brand-buyer-cross-border-ecommerce-marketplace-listing-amazon-fba-tiktok-shop-tmall-compliance-architecture-global-brand-procurement-2026-08-28-am.html",
        "date": "2026-08-28 10:00 AM",
        "title": "Ribbon OEM 94-Module Brand-Buyer Cross-Border-Ecommerce Marketplace-Listing Amazon-FBA TikTok-Shop Tmall Compliance Architecture 2026",
        "tag": "Brand-Buyer Cross-Border-Ecommerce Marketplace-Listing Amazon-FBA TikTok-Shop Tmall Compliance",
        "iso_date": "2026-08-28",
        "desc": "A 2026 B2B ribbon OEM 94-module brand-buyer cross-border-ecommerce marketplace-listing Amazon-FBA TikTok-Shop Tmall compliance architecture for global brand owners, D2C-directors, marketplace-operations-VPs, and brand-cross-border-fulfillment-leads. Covers 12-marketplace-listing-cadre, 11-Amazon-FBA-prep-engine, 10-TikTok-Shop-listing-pipeline, 9-Tmall-marketplace-cascade-stack, 8-cross-border-compliance-engine, 7-marketplace-archive, 9-marketplace-dashboard, 6-marketplace-IP, 6-marketplace-cost &amp; 10-marketplace-continuous-improvement modules. Delivers 92-98% 22-day-time-to-marketplace-pilot-launch, 84-94% marketplace-listing-approval-completeness, 44-58% cross-border-fulfillment-cost-reduction, 18-26% marketplace-detention-reduction, 79 brand partners, 40 EU-27 markets, 45 NA-states, 47 MEA-jurisdictions, 2,780 active SKUs on a 10.2M-meter annual multi-brand multi-jurisdiction brand-buyer cross-border-ecommerce marketplace-listing Amazon-FBA TikTok-Shop Tmall compliance program.",
        "short": "A 2026 B2B ribbon OEM 94-module brand-buyer cross-border-ecommerce marketplace-listing Amazon-FBA TikTok-Shop Tmall compliance architecture for global brand owners, D2C-directors, marketplace-operations-VPs, and brand-cross-border-fulfillment-leads. Covers marketplace listing cadre, Amazon FBA prep engine, TikTok Shop listing pipeline, Tmall marketplace cascade stack, cross border compliance engine, and 22-day time-to-marketplace-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-95-module-mill-side-water-reclaim-recycling-zero-liquid-discharge-zld-process-water-architecture-premium-brand-global-brand-procurement-2026-08-28-pm.html",
        "abs_file": "blog/blog-ribbon-oem-95-module-mill-side-water-reclaim-recycling-zero-liquid-discharge-zld-process-water-architecture-premium-brand-global-brand-procurement-2026-08-28-pm.html",
        "date": "2026-08-28 15:00 PM",
        "title": "Ribbon OEM 95-Module Mill-Side Water-Reclaim Recycling Zero-Liquid-Discharge ZLD Process-Water Architecture Premium-Brand 2026",
        "tag": "Mill-Side Water-Reclaim Recycling Zero-Liquid-Discharge ZLD Process-Water Architecture Premium-Brand",
        "iso_date": "2026-08-28",
        "desc": "A 2026 B2B ribbon OEM 95-module mill-side water-reclaim recycling zero-liquid-discharge ZLD process-water architecture for premium-brand owners, brand-sustainability-VPs, ESG-and-water-stewardship-directors, and brand-ZLD-procurement-leads. Covers 12-ZLD-water-cadre, 11-process-water-collection-engine, 10-water-reclaim-recycling-pipeline, 9-zero-discharge-cascade-stack, 8-water-stewardship-engine, 7-ZLD-archive, 9-ZLD-dashboard, 6-ZLD-IP, 6-ZLD-cost &amp; 10-ZLD-continuous-improvement modules. Delivers 92-98% 24-day-time-to-ZLD-pilot-launch, 84-94% water-reclaim-completeness, 44-58% process-water-cost-reduction, 18-26% ZLD-system-defect-reduction, 80 brand partners, 41 EU-27 markets, 46 NA-states, 48 MEA-jurisdictions, 2,820 active SKUs on a 10.4M-meter annual multi-brand multi-jurisdiction mill-side water-reclaim recycling zero-liquid-discharge ZLD process-water architecture premium-brand program.",
        "short": "A 2026 B2B ribbon OEM 95-module mill-side water-reclaim recycling zero-liquid-discharge ZLD process-water architecture for premium-brand owners, brand-sustainability-VPs, ESG-and-water-stewardship-directors, and brand-ZLD-procurement-leads. Covers ZLD water cadre, process water collection engine, water reclaim recycling pipeline, zero discharge cascade stack, water stewardship engine, and 24-day time-to-ZLD-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor: latest in index.html = 92-am
anchor = '<a href="blog/blog-ribbon-oem-92-module-brand-buyer-sustainability-procurement-roadmap-csrd-esg-disclosure-supplier-data-collection-architecture-global-brand-procurement-2026-08-27-am.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    # try 93-pm
    anchor = '<a href="blog/blog-ribbon-oem-93-module-mill-side-rpet-recycling-loop-post-consumer-bottle-to-yarn-pellet-to-ribbon-finish-architecture-premium-brand-global-brand-procurement-2026-08-27-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'
    if anchor not in html:
        raise SystemExit("anchor not found in index.html")

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

# Anchor: latest blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-92-module-brand-buyer-sustainability-procurement-roadmap-csrd-esg-disclosure-supplier-data-collection-architecture-global-brand-procurement-2026-08-27-am.html">Ribbon OEM 92-Module Brand-Buyer Sustainability-Procurement-Roadmap CSRD ESG-Disclosure Supplier-Data-Collection Architecture 2026</a></h3>'

if anchor_blog not in blog:
    anchor_blog = '<h3><a href="blog/blog-ribbon-oem-93-module-mill-side-rpet-recycling-loop-post-consumer-bottle-to-yarn-pellet-to-ribbon-finish-architecture-premium-brand-global-brand-procurement-2026-08-27-pm.html">Ribbon OEM 93-Module Mill-Side RPET Recycling-Loop Post-Consumer-Bottle-to-Yarn-Pellet-to-Ribbon-Finish Architecture Premium-Brand 2026</a></h3>'
    if anchor_blog not in blog:
        raise SystemExit("anchor not found in blog.html")

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
            <div class="blog-meta">August 28, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-92-module-brand-buyer-sustainability-procurement-roadmap-csrd-esg-disclosure-supplier-data-collection-architecture-global-brand-procurement-2026-08-27-am.html"

if anchor_url not in sm:
    anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-93-module-mill-side-rpet-recycling-loop-post-consumer-bottle-to-yarn-pellet-to-ribbon-finish-architecture-premium-brand-global-brand-procurement-2026-08-27-pm.html"
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
