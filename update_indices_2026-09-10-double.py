"""Wire 2026-09-10 cron DOUBLE articles (111-AM, 112-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-10"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-111-module-brand-buyer-mill-side-closed-loop-take-back-reuse-refurbishment-reverse-logistics-program-architecture-global-brand-procurement-2026-09-10-am.html",
        "date": "2026-09-10 10:00 AM",
        "title": "Ribbon OEM 111-Module Brand-Buyer Mill-Side Closed-Loop Take-Back Reuse Refurbishment Reverse-Logistics Program Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Closed-Loop Take-Back Reuse Refurbishment Reverse-Logistics Program Architecture",
        "iso_date": "2026-09-10",
        "desc": "A 2026 B2B ribbon OEM 111-module brand-buyer mill-side closed-loop take-back reuse refurbishment reverse-logistics program architecture for global brand owners, brand-sustainability-VPs, brand-circularity-directors, and brand-reverse-logistics-procurement-leads. Covers 11-take-back-cadre, 10-reuse-engine, 9-refurbishment-pipeline, 8-reverse-stack, 7-archive, 6-dashboard, 8-IP, 5-cost &amp; 9-CI modules. Delivers 92-98% 29-day-time-to-take-back-pilot-launch, 84-94% take-back-window-on-time-recovery, 44-58% post-consumer-bottle-return, 18-26% reuse-reintroduction, 94 brand partners, 52 EU-27 markets, 57 NA-states, 59 MEA-jurisdictions, 3,360 active SKUs on a 12.9M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side closed-loop take-back reuse refurbishment reverse-logistics program architecture program.",
        "short": "A 2026 B2B ribbon OEM 111-module brand-buyer mill-side closed-loop take-back reuse refurbishment reverse-logistics program architecture for global brand owners, brand-sustainability-VPs, brand-circularity-directors, and brand-reverse-logistics-procurement-leads. Covers take-back cadre, reuse engine, refurbishment pipeline, reverse stack, archive, and 29-day time-to-take-back-pilot-launch...",
        "mins": "39 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-112-module-brand-buyer-cross-border-ecommerce-fba-tiktok-shop-tmall-marketplace-compliance-listing-ready-architecture-global-brand-procurement-2026-09-10-pm.html",
        "date": "2026-09-10 15:00 PM",
        "title": "Ribbon OEM 112-Module Brand-Buyer Cross-Border E-Commerce FBA TikTok-Shop Tmall Marketplace Compliance Listing-Ready Architecture 2026",
        "tag": "Brand-Buyer Cross-Border E-Commerce FBA TikTok-Shop Tmall Marketplace Compliance Listing-Ready Architecture",
        "iso_date": "2026-09-10",
        "desc": "A 2026 B2B ribbon OEM 112-module brand-buyer cross-border e-commerce FBA TikTok-Shop Tmall marketplace compliance listing-ready architecture for global brand owners, brand-D2C-VPs, brand-marketplace-directors, and brand-cross-border-fulfillment-leads. Covers 12-marketplace-cadre, 11-FBA-engine, 10-TikTok-Shop-pipeline, 9-Tmall-stack, 8-listing-ready-archive, 7-dashboard, 9-compliance-IP, 6-cost &amp; 10-CI modules. Delivers 92-98% 28-day-time-to-marketplace-pilot-launch, 84-94% listing-window-on-time-recovery, 44-58% FNSKU-prep-yield, 18-26% marketplace-defect-rate-reduction, 97 brand partners, 54 EU-27 markets, 58 NA-states, 60 MEA-jurisdictions, 3,480 active SKUs on a 13.4M-meter annual multi-brand multi-jurisdiction brand-buyer cross-border e-commerce FBA TikTok-Shop Tmall marketplace compliance listing-ready architecture program.",
        "short": "A 2026 B2B ribbon OEM 112-module brand-buyer cross-border e-commerce FBA TikTok-Shop Tmall marketplace compliance listing-ready architecture for global brand owners, brand-D2C-VPs, brand-marketplace-directors, and brand-cross-border-fulfillment-leads. Covers marketplace cadre, FBA engine, TikTok-Shop pipeline, Tmall stack, listing-ready archive, and 28-day time-to-marketplace-pilot-launch...",
        "mins": "40 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 110-PM card end (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_110_PM_END = (
    '<a href="blog/blog-ribbon-oem-110-module-brand-buyer-multi-tier-sub-tier-subcontracting-4-tier-mapping-risk-resilience-supplier-diversification-transparency-architecture-global-brand-procurement-2026-09-02-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_110_PM_END not in html:
        raise SystemExit("ANCHOR_110_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_110_PM_END, ANCHOR_110_PM_END + cards_block, 1)
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
    anchor_110 = 'blog/blog-ribbon-oem-110-module-brand-buyer-multi-tier-sub-tier-subcontracting-4-tier-mapping-risk-resilience-supplier-diversification-transparency-architecture-global-brand-procurement-2026-09-02-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_110) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    m = pattern.search(html)
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    if m:
        new_html = html[:m.end()] + cards_block + html[m.end():]
    else:
        idx = html.find(anchor_110)
        if idx < 0:
            raise SystemExit("110-PM not found in blog.html")
        end = html.find("</article>", idx)
        if end < 0:
            raise SystemExit("</article> after 110-PM not found in blog.html")
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
