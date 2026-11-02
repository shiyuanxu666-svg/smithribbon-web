"""Wire new 2026-08-30 articles (98-AM, 99-PM) into index.html, blog.html, sitemap.xml.

Robust version: anchors on the full news-card block (date + title + read-more)
so we don't accidentally hit a stale link in an older card.
"""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-98-module-brand-buyer-multi-tier-sub-supplier-risk-mapping-4-tier-sub-contracting-transparency-resilience-architecture-global-brand-procurement-2026-08-30-am.html",
        "abs_file": "blog/blog-ribbon-oem-98-module-brand-buyer-multi-tier-sub-supplier-risk-mapping-4-tier-sub-contracting-transparency-resilience-architecture-global-brand-procurement-2026-08-30-am.html",
        "date": "2026-08-30 10:00 AM",
        "title": "Ribbon OEM 98-Module Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture 2026",
        "tag": "Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture",
        "iso_date": "2026-08-30",
        "desc": "A 2026 B2B ribbon OEM 98-module brand-buyer multi-tier sub-supplier risk-mapping 4-tier sub-contracting transparency resilience architecture for global brand owners, brand-procurement-VPs, brand-supply-chain-resilience-leads, and brand-ESG-compliance-directors. Covers 12-sub-tier-mapping-cadre, 11-sub-contracting-transparency-engine, 10-risk-mapping-pipeline, 9-sub-tier-stack, 8-sub-contracting-archive, 7-resilience-dashboard, 9-sub-tier-IP, 6-sub-tier-cost &amp; 10-sub-tier-continuous-improvement modules. Delivers 92-98% 21-day-time-to-sub-tier-pilot-launch, 84-94% sub-tier-window-on-time-delivery, 44-58% sub-contracting-cost-reduction, 18-26% sub-tier-risk-reduction, 83 brand partners, 44 EU-27 markets, 49 NA-states, 51 MEA-jurisdictions, 2,940 active SKUs on a 11.0M-meter annual multi-brand multi-jurisdiction brand-buyer multi-tier sub-supplier risk-mapping 4-tier sub-contracting transparency resilience architecture program.",
        "short": "A 2026 B2B ribbon OEM 98-module brand-buyer multi-tier sub-supplier risk-mapping 4-tier sub-contracting transparency resilience architecture for global brand owners, brand-procurement-VPs, brand-supply-chain-resilience-leads, and brand-ESG-compliance-directors. Covers sub-tier mapping cadre, sub-contracting transparency engine, risk mapping pipeline, sub-tier stack, sub-contracting archive, and 21-day time-to-sub-tier-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-99-module-brand-buyer-cross-border-duty-drawback-rebate-export-refund-freight-cost-recovery-architecture-global-brand-procurement-2026-08-30-pm.html",
        "abs_file": "blog/blog-ribbon-oem-99-module-brand-buyer-cross-border-duty-drawback-rebate-export-refund-freight-cost-recovery-architecture-global-brand-procurement-2026-08-30-pm.html",
        "date": "2026-08-30 15:00 PM",
        "title": "Ribbon OEM 99-Module Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture 2026",
        "tag": "Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture",
        "iso_date": "2026-08-30",
        "desc": "A 2026 B2B ribbon OEM 99-module brand-buyer cross-border duty-drawback rebate export refund freight-cost-recovery architecture for global brand owners, brand-cross-border-finance-VPs, brand-duty-recovery-leads, and brand-global-trade-directors. Covers 12-duty-drawback-cadre, 11-rebate-claim-engine, 10-cross-border-refund-pipeline, 9-freight-cost-recovery-stack, 8-export-refund-archive, 7-drawback-dashboard, 9-drawback-IP, 6-drawback-cost &amp; 10-drawback-continuous-improvement modules. Delivers 92-98% 23-day-time-to-drawback-pilot-launch, 84-94% drawback-window-on-time-recovery, 44-58% duty-cost-reduction, 18-26% freight-cost-recovery, 84 brand partners, 45 EU-27 markets, 50 NA-states, 52 MEA-jurisdictions, 2,980 active SKUs on a 11.2M-meter annual multi-brand multi-jurisdiction brand-buyer cross-border duty-drawback rebate export refund freight-cost-recovery architecture program.",
        "short": "A 2026 B2B ribbon OEM 99-module brand-buyer cross-border duty-drawback rebate export refund freight-cost-recovery architecture for global brand owners, brand-cross-border-finance-VPs, brand-duty-recovery-leads, and brand-global-trade-directors. Covers duty drawback cadre, rebate claim engine, cross-border refund pipeline, freight cost recovery stack, export refund archive, and 23-day time-to-drawback-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Build the FULL anchor block: the entire 96-am news-card (date, h3, p, read-more)
# This is the most-recent (top) card.
ANCHOR_96_AM_FULL = (
    '<div class="news-card">\n'
    '                <div class="news-date">2026-08-29 10:00 AM</div>\n'
    '                <h3 class="en-content">Ribbon OEM 96-Module Brand-Buyer Holiday-Peak Capacity-Pre-Booking Cascade-Production Multi-Market Q4-2026 Architecture 2026</h3>\n'
    '                <p class="en-content">A 2026 B2B ribbon OEM 96-module brand-buyer holiday-peak capacity-pre-booking cascade-production multi-market Q4-2026 architecture for global brand owners, retail-merchandising-VPs, brand-seasonal-planning-leads, and brand-peak-supply-chain-directors. Covers 12-peak-capacity-cadre, 11-cascade-production-engine, 10-multi-market-routing-pipeline, 9-Q4-peak-stack, 8-holiday-replenishment-engine, 7-peak-archive, 9-peak-dashboard, 6-peak-IP, 6-peak-cost &amp; 10-peak-continuous-improvement modules. Delivers 92-98% 22-day-time-to-peak-pilot-launch, 84-94% peak-window-on-time-delivery, 44-58% peak-freight-cost-reduction, 18-26% peak-stockout-reduction, 81 brand partners, 42 EU-27 markets, 47 NA-states, 49 MEA-jurisdictions, 2,860 active SKUs on a 10.6M-meter annual multi-brand multi-jurisdiction brand-buyer holiday-peak capacity-pre-booking cascade-production multi-market Q4-2026 architecture program.</p>\n'
    '                <a href="blog/blog-ribbon-oem-96-module-brand-buyer-holiday-peak-capacity-pre-booking-cascade-production-multi-market-q4-2026-architecture-global-brand-procurement-2026-08-29-am.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
    '            </div>'
)

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

if ANCHOR_96_AM_FULL not in html:
    raise SystemExit("FATAL: 96-AM full anchor not found in index.html")

# Insert the 2 new cards BEFORE the 96-AM card.
# Order: 99-PM first, then 98-AM, so that 98-AM stays immediately above 96-AM (becomes the "latest").
# But typical layout has 10:00 AM then 15:00 PM. Let's match the order 99-PM, 98-AM, 96-AM
# Actually, looking at past runs, the order seems to be: 15:00 PM (same day) on top, then 10:00 AM (same day), then previous day's PM, etc.
# Let's match the existing layout: 99-PM appears first, then 98-AM, then 96-AM.

# Re-look at the existing order in index.html: 24-PM, 26-PM, 29-PM (97), 29-AM (96), 28-PM, 28-AM
# So pattern is: PM-of-day-X, PM-of-day-Y, ... , AM-of-most-recent-day (96 is the most recent date)
# For us adding 2026-08-30: 99-PM and 98-AM. Both are date 2026-08-30 (newest).
# So both should be above 96-AM. Order between them: 99-PM first, 98-AM second.
# (Following: 24-PM 26-PM 29-PM 29-AM pattern where newest AM comes right after newest PMs)

new_cards = ""
for e in ENTRIES:
    new_cards += f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""

new_html = html.replace(ANCHOR_96_AM_FULL, new_cards + "\n            " + ANCHOR_96_AM_FULL, 1)
if new_html == html:
    raise SystemExit("FATAL: index.html replacement did not change content")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(new_html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: the article block for 96-AM (the most recent date in blog.html)
# Note: blog.html uses <article class="blog-card"> with span.blog-tag, not div.blog-card
ANCHOR_96_AM_BLOG = (
    '<article class="blog-card">\n'
    '            <span class="blog-tag">Brand-Buyer Holiday-Peak Capacity-Pre-Booking Cascade-Production Multi-Market Q4-2026 Architecture</span>\n'
    '            <h3><a href="blog/blog-ribbon-oem-96-module-brand-buyer-holiday-peak-capacity-pre-booking-cascade-production-multi-market-q4-2026-architecture-global-brand-procurement-2026-08-29-am.html">Ribbon OEM 96-Module Brand-Buyer Holiday-Peak Capacity-Pre-Booking Cascade-Production Multi-Market Q4-2026 Architecture 2026</a></h3>\n'
    '            <p>A 2026 B2B ribbon OEM 96-module brand-buyer holiday-peak capacity-pre-booking cascade-production multi-market Q4-2026 architecture for global brand owners, retail-merchandising-VPs, brand-seasonal-planning-leads, and brand-peak-supply-chain-directors. Covers peak capacity cadre, cascade production engine, multi-market routing pipeline, Q4 peak stack, holiday replenishment engine, and 22-day time-to-peak-pilot-launch...</p>\n'
    '            <div class="blog-meta">August 29, 2026 &middot; 38 min read</div>\n'
    '        </article>'
)

if ANCHOR_96_AM_BLOG not in blog:
    raise SystemExit("FATAL: 96-AM blog anchor not found in blog.html")

# Build the new blog-card block matching the existing structure
import re
def human_date(iso_d, slot):
    months = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June",
              "07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
    y, m, d = iso_d.split("-")
    return f"{months[m]} {int(d)}, {y}"

new_blog_cards = ""
for e in ENTRIES:
    new_blog_cards += f"""
        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">{human_date(e['iso_date'], e['slot'])} &middot; {e['mins']}</div>
        </article>"""

new_blog = blog.replace(ANCHOR_96_AM_BLOG, new_blog_cards + "\n        " + ANCHOR_96_AM_BLOG, 1)
if new_blog == blog:
    raise SystemExit("FATAL: blog.html replacement did not change content")

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(new_blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

# Use the most-recent 97-PM as the anchor
last_anchor = '<loc>https://smithribbon.com/blog/blog-ribbon-oem-97-module-brand-buyer-vendor-managed-inventory-vmi-replenishment-architecture-multi-market-3pl-routing-global-brand-procurement-2026-08-29-pm.html</loc>'
if last_anchor not in sm:
    raise SystemExit("sitemap anchor 97-pm not found")

# Also bump home lastmod to 2026-08-30
sm_new = sm.replace(
    '<loc>https://smithribbon.com/</loc>\n    <lastmod>2026-08-29</lastmod>',
    '<loc>https://smithribbon.com/</loc>\n    <lastmod>2026-08-30</lastmod>',
    1,
)

# Insert 99-PM and 98-AM after the 97-PM anchor
insert_block = ""
for e in reversed(ENTRIES):  # oldest first so order becomes 99-PM, 98-AM
    url = f"https://smithribbon.com/{e['file']}"
    insert_block += f"    <loc>{url}</loc>\n"

sm_new = sm_new.replace(last_anchor, last_anchor + "\n" + insert_block.rstrip(), 1)
with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm_new)
print("sitemap.xml updated")

# --- llms.txt: bump Last updated ---
LLMS = os.path.join(WEB, "llms.txt")
with open(LLMS, "r", encoding="utf-8") as f:
    ll = f.read()
ll_new = ll.replace("# Last updated: 2026-08-29", "# Last updated: 2026-08-30", 1)
with open(LLMS, "w", encoding="utf-8") as f:
    f.write(ll_new)
print("llms.txt updated")
