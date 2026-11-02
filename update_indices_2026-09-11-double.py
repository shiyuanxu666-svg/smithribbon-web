"""Wire 2026-09-11 cron DOUBLE articles (113-AM, 114-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-11"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-113-module-brand-buyer-vendor-managed-inventory-vmi-hub-and-spoke-replenishment-auto-reorder-architecture-global-brand-procurement-2026-09-11-am.html",
        "date": "2026-09-11 10:00 AM",
        "title": "Ribbon OEM 113-Module Brand-Buyer Vendor-Managed Inventory VMI Hub-and-Spoke Replenishment Auto-Reorder Architecture 2026",
        "tag": "Brand-Buyer Vendor-Managed Inventory VMI Hub-and-Spoke Replenishment Auto-Reorder Architecture",
        "iso_date": "2026-09-11",
        "desc": "A 2026 B2B ribbon OEM 113-module brand-buyer vendor-managed inventory VMI hub-and-spoke replenishment auto-reorder architecture for global brand owners, brand-supply-chain-VPs, brand-inventory-planning-directors, and brand-3PL-distribution-leads. Covers 11-VMI-cadre, 10-hub-engine, 9-spoke-pipeline, 8-replenishment-stack, 7-archive, 6-dashboard, 8-IP, 5-cost &amp; 9-CI modules. Delivers 92-98% 21-day-time-to-VMI-pilot-launch, 84-94% hub-on-time-replenishment, 44-58% inventory-carry-reduction, 18-26% stockout-rate-reduction, 98 brand partners, 55 EU-27 markets, 58 NA-states, 60 MEA-jurisdictions, 3,520 active SKUs on a 13.7M-meter annual multi-brand multi-jurisdiction brand-buyer vendor-managed inventory VMI hub-and-spoke replenishment auto-reorder architecture program.",
        "short": "A 2026 B2B ribbon OEM 113-module brand-buyer vendor-managed inventory VMI hub-and-spoke replenishment auto-reorder architecture for global brand owners, brand-supply-chain-VPs, brand-inventory-planning-directors, and brand-3PL-distribution-leads. Covers VMI cadre, hub engine, spoke pipeline, replenishment stack, and 21-day time-to-VMI-pilot-launch...",
        "mins": "39 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-114-module-brand-buyer-q4-holiday-peak-cascade-multi-market-production-capacity-pre-booking-architecture-global-brand-procurement-2026-09-11-pm.html",
        "date": "2026-09-11 15:00 PM",
        "title": "Ribbon OEM 114-Module Brand-Buyer Q4-Holiday Peak Cascade Multi-Market Production Capacity Pre-Booking Architecture 2026",
        "tag": "Brand-Buyer Q4-Holiday Peak Cascade Multi-Market Production Capacity Pre-Booking Architecture",
        "iso_date": "2026-09-11",
        "desc": "A 2026 B2B ribbon OEM 114-module brand-buyer Q4-holiday peak cascade multi-market production capacity pre-booking architecture for global brand owners, brand-seasonal-merchandising-VPs, brand-holiday-gifting-directors, and brand-peak-capacity-planning-leads. Covers 12-peak-cadre, 11-cascade-engine, 10-multi-market-pipeline, 9-pre-booking-stack, 8-archive, 7-dashboard, 9-IP, 6-cost &amp; 10-CI modules. Delivers 92-98% 24-day-time-to-peak-pilot-launch, 84-94% cascade-window-on-time-recovery, 44-58% pre-booked-capacity-yield, 18-26% peak-stockout-prevention, 101 brand partners, 56 EU-27 markets, 59 NA-states, 61 MEA-jurisdictions, 3,640 active SKUs on a 14.2M-meter annual multi-brand multi-jurisdiction brand-buyer Q4-holiday peak cascade multi-market production capacity pre-booking architecture program.",
        "short": "A 2026 B2B ribbon OEM 114-module brand-buyer Q4-holiday peak cascade multi-market production capacity pre-booking architecture for global brand owners, brand-seasonal-merchandising-VPs, brand-holiday-gifting-directors, and brand-peak-capacity-planning-leads. Covers peak cadre, cascade engine, multi-market pipeline, pre-booking stack, and 24-day time-to-peak-pilot-launch...",
        "mins": "40 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 112-PM card end (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_112_PM_END = (
    '<a href="blog/blog-ribbon-oem-112-module-brand-buyer-cross-border-ecommerce-fba-tiktok-shop-tmall-marketplace-compliance-listing-ready-architecture-global-brand-procurement-2026-09-10-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
    '            </div>'
)

def make_index_card(e):
    return (
        '\n            <div class="news-card">\n'
        f'                <div class="news-date">{e["date"]}</div>\n'
        f'                <h3 class="en-content">{e["title"]}</h3>\n'
        f'                <p class="en-content">{e["desc"]}</p>\n'
        f'                <a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
        '            </div>'
    )

def update_index():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()
    cards_block = "".join(make_index_card(e) for e in ENTRIES)
    if ANCHOR_112_PM_END not in html:
        raise SystemExit("ANCHOR_112_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_112_PM_END, ANCHOR_112_PM_END + cards_block, 1)
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"index.html: {len(html):,} -> {len(new_html):,} bytes")

def make_blog_card(e):
    return (
        '\n            <article class="blog-card">\n'
        f'                <div class="blog-date">{e["date"]}</div>\n'
        f'                <h3><a href="{e["file"]}">{e["title"]}</a></h3>\n'
        f'                <p>{e["short"]}</p>\n'
        f'                <a href="{e["file"]}" class="blog-read-more">Read More &rarr;</a>\n'
        '            </article>'
    )

def update_blog():
    with open(BLOG_HTML, "r", encoding="utf-8") as f:
        html = f.read()
    anchor_112 = 'blog/blog-ribbon-oem-112-module-brand-buyer-cross-border-ecommerce-fba-tiktok-shop-tmall-marketplace-compliance-listing-ready-architecture-global-brand-procurement-2026-09-10-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_112) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    m = pattern.search(html)
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    if m:
        new_html = html[:m.end()] + cards_block + html[m.end():]
    else:
        idx = html.find(anchor_112)
        if idx < 0:
            raise SystemExit("112-PM not found in blog.html")
        end = html.find("</article>", idx)
        if end < 0:
            raise SystemExit("</article> after 112-PM not found in blog.html")
        insert_point = end + len("</article>")
        new_html = html[:insert_point] + cards_block + html[insert_point:]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    today = TODAY
    new_entries = []
    for e in ENTRIES:
        url_path = f"https://smithribbon.com/{e['file']}"
        block = (
            "  <url>\n"
            f"    <loc>{url_path}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>0.8</priority>\n"
            "  </url>\n"
        )
        new_entries.append(block)
    insertion = "".join(new_entries)
    marker = "</urlset>"
    if marker not in xml:
        raise SystemExit("</urlset> not found in sitemap.xml")
    new_xml = xml.replace(marker, insertion + marker, 1)
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(new_xml)
    print(f"sitemap.xml: {len(xml):,} -> {len(new_xml):,} bytes")

if __name__ == "__main__":
    update_index()
    update_blog()
    update_sitemap()
    print("DONE.")
