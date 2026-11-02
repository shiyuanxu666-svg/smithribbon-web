"""Wire 2026-09-15 cron DOUBLE articles (131-AM, 132-PM) into index.html, blog.html, sitemap.xml.
Anchors: 130-PM (the most recent article on disk before this batch)."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-15"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-131-module-brand-buyer-mill-side-brand-licensing-royalty-engine-program-architecture-global-brand-procurement-2026-09-15-am.html",
        "date": "2026-09-15 10:00 AM",
        "title": "Ribbon OEM 131-Module Brand-Buyer Mill-Side Brand-Licensing Royalty-Engine Program Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Brand-Licensing Royalty-Engine Program Architecture",
        "iso_date": "2026-09-15",
        "desc": "A 2026 B2B ribbon OEM 131-module brand-buyer mill-side brand-licensing royalty-engine program architecture for global brand owners, brand-IP-counsel, brand-licensing-VPs, brand-character-program-directors, and brand-royalty-program-leads. Covers 10-licensing, 9-IP-counsel, 8-royalty-engine, 7-character-program, 6-trademark-clearance, 9-artwork-rights, 8-territory-rights, 7-channel-rights &amp; 6-sub-license modules. Delivers 92-98% 26-day-time-to-license-pilot-launch, 84-94% royalty-collection-rate, 44-58% margin-lift, 18-26% audit-pass-rate, 113 brand partners, 64 EU-27 markets, 67 NA-states, 70 MEA-jurisdictions, 4,100 active SKUs on a 15.8M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side brand-licensing royalty-engine program architecture program.",
        "short": "A 2026 B2B ribbon OEM 131-module brand-buyer mill-side brand-licensing royalty-engine program architecture for global brand owners, brand-IP-counsel, brand-licensing-VPs, brand-character-program-directors, and brand-royalty-program-leads. Covers licensing, IP-counsel, royalty-engine, character-program, trademark-clearance, artwork-rights, territory-rights, channel-rights, sub-license, and 26-day time-to-license-pilot-launch...",
        "mins": "44 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-132-module-brand-buyer-cross-border-e-commerce-fba-tiktok-shop-tmall-marketplace-compliance-listing-ready-architecture-global-brand-procurement-2026-09-15-pm.html",
        "date": "2026-09-15 15:00 PM",
        "title": "Ribbon OEM 132-Module Brand-Buyer Cross-Border E-Commerce FBA-TikTok-Shop-Tmall Marketplace-Compliance Listing-Ready Architecture 2026",
        "tag": "Brand-Buyer Cross-Border E-Commerce FBA-TikTok-Shop-Tmall Marketplace-Compliance Listing-Ready Architecture",
        "iso_date": "2026-09-15",
        "desc": "A 2026 B2B ribbon OEM 132-module brand-buyer cross-border e-commerce FBA-TikTok-shop-Tmall marketplace-compliance listing-ready architecture for global brand owners, brand-marketplace-VPs, brand-D2C-Operators, brand-Amazon-account-leads, and brand-cross-border-e-commerce-directors. Covers 10-Amazon-FBA, 9-TikTok-shop, 8-Tmall, 7-Walmart-marketplace, 6-listing-ready, 9-barcode, 8-labeling, 7-packaging-compliance &amp; 6-hazmat modules. Delivers 92-98% 28-day-time-to-marketplace-pilot-launch, 84-94% listing-approval-rate, 44-58% cross-border-yield, 18-26% buy-box-lift, 114 brand partners, 65 EU-27 markets, 68 NA-states, 71 MEA-jurisdictions, 4,130 active SKUs on a 15.9M-meter annual multi-brand multi-jurisdiction brand-buyer cross-border e-commerce FBA-TikTok-shop-Tmall marketplace-compliance listing-ready architecture program.",
        "short": "A 2026 B2B ribbon OEM 132-module brand-buyer cross-border e-commerce FBA-TikTok-shop-Tmall marketplace-compliance listing-ready architecture for global brand owners, brand-marketplace-VPs, brand-D2C-Operators, brand-Amazon-account-leads, and brand-cross-border-e-commerce-directors. Covers Amazon-FBA, TikTok-shop, Tmall, Walmart-marketplace, listing-ready, barcode, labeling, packaging-compliance, hazmat, and 28-day time-to-marketplace-pilot-launch...",
        "mins": "44 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 130-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_130_PM_END = (
    '<a href="blog/blog-ribbon-oem-130-module-brand-buyer-omni-channel-fulfillment-d2c-b2b-b2b2c-amazon-walmart-marketplace-architecture-global-brand-procurement-2026-09-15-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_130_PM_END not in html:
        raise SystemExit("ANCHOR_130_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_130_PM_END, ANCHOR_130_PM_END + cards_block, 1)
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
    # Anchor: 130-PM (most recent entry already in blog.html)
    anchor_130 = 'blog/blog-ribbon-oem-130-module-brand-buyer-omni-channel-fulfillment-d2c-b2b-b2b2c-amazon-walmart-marketplace-architecture-global-brand-procurement-2026-09-15-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_130) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        raise SystemExit("Anchor 130-PM not found in blog.html")
    blog_block = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = html[: m.end()] + blog_block + html[m.end():]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def make_sitemap_url(e):
    return (
        '\n  <url>\n'
        f'    <loc>{SITE}/blog/{e["file"].split("/", 1)[1]}</loc>\n'
        f'    <lastmod>{e["iso_date"]}</lastmod>\n'
        '    <changefreq>monthly</changefreq>\n'
        '    <priority>0.8</priority>\n'
        '  </url>'
    )

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    # Anchor: 130-PM url block end
    anchor_130_loc = f'{SITE}/blog/blog-ribbon-oem-130-module-brand-buyer-omni-channel-fulfillment-d2c-b2b-b2b2c-amazon-walmart-marketplace-architecture-global-brand-procurement-2026-09-15-pm.html'
    pattern = re.compile(
        r'(    <loc>' + re.escape(anchor_130_loc) + r'</loc>\s*\n\s*<lastmod>[^<]+</lastmod>\s*\n\s*<changefreq>[^<]+</changefreq>\s*\n\s*<priority>[^<]+</priority>\s*\n\s*</url>)',
        re.DOTALL,
    )
    m = pattern.search(xml)
    if not m:
        raise SystemExit("Anchor 130-PM not found in sitemap.xml")
    sm_block = "".join(make_sitemap_url(e) for e in ENTRIES)
    new_xml = xml[: m.end()] + sm_block + xml[m.end():]
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(new_xml)
    print(f"sitemap.xml: {len(xml):,} -> {len(new_xml):,} bytes")

def main():
    update_index()
    update_blog()
    update_sitemap()

if __name__ == "__main__":
    main()