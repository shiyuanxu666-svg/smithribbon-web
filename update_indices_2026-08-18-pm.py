"""Wire new 2026-08-18 PM article into index.html, blog.html, sitemap.xml."""
import re, os, json
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

# Slot data
ENTRIES = [
    {
        "slot": "pm",
        "file": "blog-ribbon-oem-65-module-q4-holiday-peak-capacity-pre-booking-cascade-production-architecture-global-brand-procurement-2026-08-18-pm.html",
        "date": "2026-08-18 15:00 PM",
        "title": "Ribbon OEM 65-Module Q4 Holiday Peak-Season Capacity Pre-Booking &amp; Cascade-Production Architecture 2026",
        "tag": "Q4 Holiday Peak-Season Capacity Pre-Booking &amp; Cascade-Production Architecture",
        "iso_date": "2026-08-18",
        "desc": "A 2026 B2B ribbon OEM 65-module Q4 holiday peak-season capacity pre-booking and cascade-production architecture for global brand owners, retail-merchandising-directors, holiday-gifting-program-leads, and private-label program directors. Covers 9-month pre-book calendar, 8-tier capacity reservation ladder, 7-multi-region cascade, 6-supplier-pool failover, 5-supplier-finance bridge, 4-freight pre-position, 4-warehouse 3PL pre-stage, 6-raw-material lock, 4-color-master pre-build, 5-tooling-die pre-fab, 6-packaging pre-print, 4-label/hangtag pre-print, 5-multi-SKU mix-shuffle, 4-color-fade overrun, 5-finishing-overrun, 6-print-overrun, 4-AQL-overrun, 4-quality-NCR, 4-customer-claim-cost, 5-replenishment, 4-reorder-cycle, 5-post-holiday stock-balance &amp; 4-quarter-review cadence. Delivers 92-98% 90-day-time-to-Q4-shelf, 78-92% capacity-reservation-savings, 0% Q4-stockout, 18-26% freight-pre-position-savings, 100% Q4-on-time-delivery, 49 brand partners, 15 EU-27 markets, 24 NA-states, 20 MEA-jurisdictions, 1,820 active SKUs on a 4.6M-meter annual multi-brand multi-jurisdiction Q4 holiday pre-booking program.",
        "short": "A 2026 B2B ribbon OEM 65-module Q4 holiday peak-season capacity pre-booking and cascade-production architecture for global brand owners, retail-merchandising-directors, holiday-gifting-program-leads, and private-label program directors. Covers 9-month pre-book calendar, 8-tier capacity reservation ladder, 7-multi-region cascade, 6-supplier-pool failover, 5-supplier-finance bridge, 4-freight pre-position, 4-warehouse 3PL pre-stage, 6-raw-material lock, 4-color-master pre-build, 5-tooling-die pre-fab, 6-packaging pre-print, 4-label/hangtag pre-print, 5-multi-SKU mix-shuffle, 4-color-fade overrun, 5-finishing-overrun, 6-print-overrun, 4-AQL-overrun, 4-quality-NCR, 4-customer-claim-cost, 5-replenishment, 4-reorder-cycle, 5-post-holiday stock-balance &amp; 4-quarter-review cadence...",
        "mins": "36 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
# Anchor: the 64-module card (PM) is the most recent. We insert after it.
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

anchor_64 = '<a href="blog-ribbon-oem-64-module-brand-marketing-seasonal-storytelling-campaign-bundle-global-brand-procurement-2026-08-18-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor_64 not in html:
    raise SystemExit("anchor 64 not found in index.html")

for e in ENTRIES:
    card = f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    pattern = re.escape(anchor_64) + r"\s*</div>"
    repl = anchor_64 + "            </div>" + card
    new_html, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        new_html = html.replace(anchor_64, anchor_64 + card, 1)
    html = new_html

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

anchor_64_blog = '<h3><a href="blog-ribbon-oem-64-module-brand-marketing-seasonal-storytelling-campaign-bundle-global-brand-procurement-2026-08-18-pm.html">Ribbon OEM 64-Module Brand-Marketing Seasonal-Storytelling Campaign-Bundle Architecture 2026</a></h3>'

if anchor_64_blog not in blog:
    raise SystemExit("anchor 64 not found in blog.html")

idx = blog.index(anchor_64_blog)
end_article = blog.index("</article>", idx)
insert_pt = end_article + len("</article>")

cards = []
for e in reversed(ENTRIES):
    card = f"""

        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">August 18, 2026 &middot; {e['mins']}</div>
        </article>"""
    cards.append(card)

insertion = "".join(cards)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

new_urls = ""
for e in ENTRIES:
    new_urls += f"""  <url>
    <loc>{SITE}/{e['file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sm = sm.replace("</urlset>", new_urls + "</urlset>")
with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
print("DONE")
