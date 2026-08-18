"""Wire new 2026-08-18 double-push articles (61-am, 62-pm) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog-ribbon-oem-61-module-spec-sheet-rfq-to-award-reverse-engineering-brand-buyer-cost-engineering-global-brand-procurement-2026-08-18-am.html",
        "date": "2026-08-18 10:30 AM",
        "title": "Ribbon OEM 61-Module Spec-Sheet RFQ-to-Award Reverse-Engineering &amp; Brand-Buyer Cost-Engineering Architecture 2026",
        "tag": "Spec-Sheet RFQ-to-Award Reverse-Engineering &amp; Brand-Buyer Cost-Engineering Architecture",
        "iso_date": "2026-08-18",
        "desc": "A 2026 B2B ribbon OEM 61-module spec-sheet RFQ-to-award reverse-engineering and brand-buyer cost-engineering architecture for global brand owners, procurement-directors, vendor-managers, and private-label program directors. Covers 9-spec-sheet-reverse-engineer, 8-RFQ-bid-decode, 7-cost-engineering-build, 6-award-decision-validate, 5-supplier-shortlist-finalize, 8-RFQ-compliance, 6-bid-logistics, 4-RFQ-IP, 4-RFQ-cost &amp; 5-RFQ-continuous-improvement modules. Delivers 92-98% 21-day-time-to-award-letter, 78-92% RFQ-bid-win-rate, 44-58% RFQ-cost-savings, 18-26% brand-buyer-conversion-uplift, 51 brand partners, 17 EU-27 markets, 26 NA-states, 23 MEA-jurisdictions, 1,840 active SKUs on a 5.3M-meter annual multi-brand multi-jurisdiction spec-sheet RFQ-to-award program.",
        "short": "A 2026 B2B ribbon OEM 61-module spec-sheet RFQ-to-award reverse-engineering and brand-buyer cost-engineering architecture for global brand owners, procurement-directors, vendor-managers, and private-label program directors. Covers spec-sheet reverse-engineering, RFQ bid decoding, cost-engineering build, award-decision validation, and 21-day time-to-award-letter...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog-ribbon-oem-62-module-cross-border-ecommerce-marketplace-brand-listing-fba-prep-compliance-global-brand-procurement-2026-08-18-pm.html",
        "date": "2026-08-18 15:30 PM",
        "title": "Ribbon OEM 62-Module Cross-Border-Ecommerce Marketplace Brand-Listing &amp; FBA-Prep Compliance Architecture 2026",
        "tag": "Cross-Border-Ecommerce Marketplace Brand-Listing &amp; FBA-Prep Compliance Architecture",
        "iso_date": "2026-08-18",
        "desc": "A 2026 B2B ribbon OEM 62-module cross-border-ecommerce marketplace brand-listing and FBA-prep compliance architecture for global brand owners, marketplace-directors, FBA-operations-VPs, and private-label program directors. Covers 9-marketplace-listing-build, 8-FBA-barcode-pack, 7-listing-image-render, 6-Amazon-Walmart-TikTok-Shein-attribute-fill, 5-fulfillment-routing-plan, 8-marketplace-compliance, 6-FNSKU-label, 4-listing-IP, 4-FBA-cost &amp; 5-listing-continuous-improvement modules. Delivers 92-98% 18-day-time-to-listing-live, 86-96% marketplace-attribute-completeness, 44-58% FBA-prep-cost-savings, 18-26% marketplace-conversion-uplift, 52 brand partners, 18 EU-27 markets, 26 NA-states, 24 MEA-jurisdictions, 1,860 active SKUs on a 5.6M-meter annual multi-brand multi-marketplace cross-border-ecommerce program.",
        "short": "A 2026 B2B ribbon OEM 62-module cross-border-ecommerce marketplace brand-listing and FBA-prep compliance architecture for global brand owners, marketplace-directors, FBA-operations-VPs, and private-label program directors. Covers Amazon-Walmart-TikTok-Shein attribute fill, FNSKU label, fulfillment routing, and 18-day time-to-listing-live...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor: the 59-module card (the most recent previously wired in index.html)
anchor_60 = '<a href="blog-ribbon-oem-59-module-multi-market-holiday-gifting-peak-capacity-pre-booking-cascade-production-global-brand-procurement-2026-08-17-pm2.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor_60 not in html:
    raise SystemExit("anchor 59 not found in index.html")

# Insert the new cards right after the anchor card
pattern = re.escape(anchor_60) + r"\s*</div>"
for e in ENTRIES:
    card = f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    repl = anchor_60 + "            </div>" + card
    new_html, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        new_html = html.replace(anchor_60, anchor_60 + card, 1)
    html = new_html
    # Next insertion should anchor on the just-added card
    anchor_60 = f'<a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: the 59-module blog-card heading
anchor_60_blog = '<h3><a href="blog-ribbon-oem-59-module-multi-market-holiday-gifting-peak-capacity-pre-booking-cascade-production-global-brand-procurement-2026-08-17-pm2.html">Ribbon OEM 59-Module Multi-Market Holiday-Gifting Peak-Capacity Pre-Booking &amp; Cascade-Production Architecture 2026</a></h3>'

if anchor_60_blog not in blog:
    raise SystemExit("anchor 59 not found in blog.html")

idx = blog.index(anchor_60_blog)
end_article = blog.index("</article>", idx)
insert_pt = end_article + len("</article>")

cards_parts = []
for e in ENTRIES:
    cards_parts.append(f"""

        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">August 18, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
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
