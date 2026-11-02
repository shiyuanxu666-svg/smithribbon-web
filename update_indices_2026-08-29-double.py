"""Wire new 2026-08-29 articles (96-AM, 97-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-96-module-brand-buyer-holiday-peak-capacity-pre-booking-cascade-production-multi-market-q4-2026-architecture-global-brand-procurement-2026-08-29-am.html",
        "abs_file": "blog/blog-ribbon-oem-96-module-brand-buyer-holiday-peak-capacity-pre-booking-cascade-production-multi-market-q4-2026-architecture-global-brand-procurement-2026-08-29-am.html",
        "date": "2026-08-29 10:00 AM",
        "title": "Ribbon OEM 96-Module Brand-Buyer Holiday-Peak Capacity-Pre-Booking Cascade-Production Multi-Market Q4-2026 Architecture 2026",
        "tag": "Brand-Buyer Holiday-Peak Capacity-Pre-Booking Cascade-Production Multi-Market Q4-2026 Architecture",
        "iso_date": "2026-08-29",
        "desc": "A 2026 B2B ribbon OEM 96-module brand-buyer holiday-peak capacity-pre-booking cascade-production multi-market Q4-2026 architecture for global brand owners, retail-merchandising-VPs, brand-seasonal-planning-leads, and brand-peak-supply-chain-directors. Covers 12-peak-capacity-cadre, 11-cascade-production-engine, 10-multi-market-routing-pipeline, 9-Q4-peak-stack, 8-holiday-replenishment-engine, 7-peak-archive, 9-peak-dashboard, 6-peak-IP, 6-peak-cost &amp; 10-peak-continuous-improvement modules. Delivers 92-98% 22-day-time-to-peak-pilot-launch, 84-94% peak-window-on-time-delivery, 44-58% peak-freight-cost-reduction, 18-26% peak-stockout-reduction, 81 brand partners, 42 EU-27 markets, 47 NA-states, 49 MEA-jurisdictions, 2,860 active SKUs on a 10.6M-meter annual multi-brand multi-jurisdiction brand-buyer holiday-peak capacity-pre-booking cascade-production multi-market Q4-2026 architecture program.",
        "short": "A 2026 B2B ribbon OEM 96-module brand-buyer holiday-peak capacity-pre-booking cascade-production multi-market Q4-2026 architecture for global brand owners, retail-merchandising-VPs, brand-seasonal-planning-leads, and brand-peak-supply-chain-directors. Covers peak capacity cadre, cascade production engine, multi-market routing pipeline, Q4 peak stack, holiday replenishment engine, and 22-day time-to-peak-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-97-module-brand-buyer-vendor-managed-inventory-vmi-replenishment-architecture-multi-market-3pl-routing-global-brand-procurement-2026-08-29-pm.html",
        "abs_file": "blog/blog-ribbon-oem-97-module-brand-buyer-vendor-managed-inventory-vmi-replenishment-architecture-multi-market-3pl-routing-global-brand-procurement-2026-08-29-pm.html",
        "date": "2026-08-29 15:00 PM",
        "title": "Ribbon OEM 97-Module Brand-Buyer Vendor-Managed-Inventory VMI Replenishment Architecture Multi-Market 3PL-Routing 2026",
        "tag": "Brand-Buyer Vendor-Managed-Inventory VMI Replenishment Architecture Multi-Market 3PL-Routing",
        "iso_date": "2026-08-29",
        "desc": "A 2026 B2B ribbon OEM 97-module brand-buyer vendor-managed-inventory VMI replenishment architecture multi-market 3PL-routing for global brand owners, brand-supply-chain-VPs, brand-3PL-distribution-leads, and brand-VMI-procurement-directors. Covers 12-VMI-cadre, 11-replenishment-engine, 10-multi-market-3PL-routing-pipeline, 9-VMI-cost-stack, 8-VMI-integration-engine, 7-VMI-archive, 9-VMI-dashboard, 6-VMI-IP, 6-VMI-cost &amp; 10-VMI-continuous-improvement modules. Delivers 92-98% 24-day-time-to-VMI-pilot-launch, 84-94% VMI-window-on-time-delivery, 44-58% 3PL-routing-cost-reduction, 18-26% VMI-stockout-reduction, 82 brand partners, 43 EU-27 markets, 48 NA-states, 50 MEA-jurisdictions, 2,900 active SKUs on a 10.8M-meter annual multi-brand multi-jurisdiction brand-buyer vendor-managed-inventory VMI replenishment architecture multi-market 3PL-routing program.",
        "short": "A 2026 B2B ribbon OEM 97-module brand-buyer vendor-managed-inventory VMI replenishment architecture multi-market 3PL-routing for global brand owners, brand-supply-chain-VPs, brand-3PL-distribution-leads, and brand-VMI-procurement-directors. Covers VMI cadre, replenishment engine, multi-market 3PL routing pipeline, VMI cost stack, VMI integration engine, and 24-day time-to-VMI-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor: latest in index.html = 94-am
anchor = '<a href="blog/blog-ribbon-oem-94-module-brand-buyer-cross-border-ecommerce-marketplace-listing-amazon-fba-tiktok-shop-tmall-compliance-architecture-global-brand-procurement-2026-08-28-am.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    anchor = '<a href="blog/blog-ribbon-oem-95-module-mill-side-water-reclaim-recycling-zero-liquid-discharge-zld-process-water-architecture-premium-brand-global-brand-procurement-2026-08-28-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'
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
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-94-module-brand-buyer-cross-border-ecommerce-marketplace-listing-amazon-fba-tiktok-shop-tmall-compliance-architecture-global-brand-procurement-2026-08-28-am.html">Ribbon OEM 94-Module Brand-Buyer Cross-Border-Ecommerce Marketplace-Listing Amazon-FBA TikTok-Shop Tmall Compliance Architecture 2026</a></h3>'

if anchor_blog not in blog:
    anchor_blog = '<h3><a href="blog/blog-ribbon-oem-95-module-mill-side-water-reclaim-recycling-zero-liquid-discharge-zld-process-water-architecture-premium-brand-global-brand-procurement-2026-08-28-pm.html">Ribbon OEM 95-Module Mill-Side Water-Reclaim Recycling Zero-Liquid-Discharge ZLD Process-Water Architecture Premium-Brand 2026</a></h3>'
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
            <div class="blog-meta">August 29, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-94-module-brand-buyer-cross-border-ecommerce-marketplace-listing-amazon-fba-tiktok-shop-tmall-compliance-architecture-global-brand-procurement-2026-08-28-am.html"

if anchor_url not in sm:
    anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-95-module-mill-side-water-reclaim-recycling-zero-liquid-discharge-zld-process-water-architecture-premium-brand-global-brand-procurement-2026-08-28-pm.html"
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
