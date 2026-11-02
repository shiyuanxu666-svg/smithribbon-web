"""Wire 2026-09-15 cron DOUBLE articles (129-AM, 130-PM) into index.html, blog.html, sitemap.xml.
Anchors: 127-PM (the most recent article on disk before this batch)."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-15"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-129-module-brand-buyer-mill-side-adjacent-material-bundle-program-hair-bow-sock-tag-cross-sell-architecture-global-brand-procurement-2026-09-15-am.html",
        "date": "2026-09-15 10:00 AM",
        "title": "Ribbon OEM 129-Module Brand-Buyer Mill-Side Adjacent-Material Bundle-Program Hair-Bow-Sock-Tag Cross-Sell Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Adjacent-Material Bundle-Program Hair-Bow-Sock-Tag Cross-Sell Architecture",
        "iso_date": "2026-09-15",
        "desc": "A 2026 B2B ribbon OEM 129-module brand-buyer mill-side adjacent-material bundle-program hair-bow-sock-tag cross-sell architecture for global brand owners, brand-Category-Managers, brand-D2C-Operators, brand-private-label-VPs, and brand-merchandising-leads. Covers 10-adjacent-material, 9-bundle-program, 8-cross-sell, 7-hair-bow, 6-sock, 5-tag, 9-AOV-lift, 8-repeat-rate, 7-bundle-margin &amp; 6-holiday-bundle modules. Delivers 92-98% 26-day-time-to-bundle-pilot-launch, 84-94% AOV-lift, 44-58% cross-sell-yield, 18-26% bundle-margin-lift, 111 brand partners, 62 EU-27 markets, 65 NA-states, 68 MEA-jurisdictions, 4,040 active SKUs on a 15.6M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side adjacent-material bundle-program hair-bow-sock-tag cross-sell architecture program.",
        "short": "A 2026 B2B ribbon OEM 129-module brand-buyer mill-side adjacent-material bundle-program hair-bow-sock-tag cross-sell architecture for global brand owners, brand-Category-Managers, brand-D2C-Operators, brand-private-label-VPs, and brand-merchandising-leads. Covers adjacent-material, bundle-program, cross-sell, hair-bow, sock, tag, AOV-lift, repeat-rate, bundle-margin, holiday-bundle, and 26-day time-to-bundle-pilot-launch...",
        "mins": "44 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-130-module-brand-buyer-omni-channel-fulfillment-d2c-b2b-b2b2c-amazon-walmart-marketplace-architecture-global-brand-procurement-2026-09-15-pm.html",
        "date": "2026-09-15 15:00 PM",
        "title": "Ribbon OEM 130-Module Brand-Buyer Omni-Channel Fulfillment D2C-B2B-B2B2C-Amazon-Walmart-Marketplace Architecture 2026",
        "tag": "Brand-Buyer Omni-Channel Fulfillment D2C-B2B-B2B2C-Amazon-Walmart-Marketplace Architecture",
        "iso_date": "2026-09-15",
        "desc": "A 2026 B2B ribbon OEM 130-module brand-buyer omni-channel fulfillment D2C-B2B-B2B2C-Amazon-Walmart-marketplace architecture for global brand owners, brand-fulfillment-VPs, brand-D2C-Operators, brand-marketplace-managers, and brand-supply-chain-orchestration-leads. Covers 12-omni-channel, 11-D2C, 10-B2B, 9-B2B2C, 8-Amazon-FBA, 7-Walmart-marketplace, 6-TikTok-shop, 5-Tmall, 9-3PL, 8-cross-docking, 7-last-mile &amp; 6-returns-recovery modules. Delivers 92-98% 27-day-time-to-omni-pilot-launch, 84-94% fill-rate-lift, 44-58% marketplace-yield, 18-26% omni-channel-deflection, 112 brand partners, 63 EU-27 markets, 66 NA-states, 69 MEA-jurisdictions, 4,070 active SKUs on a 15.7M-meter annual multi-brand multi-jurisdiction brand-buyer omni-channel fulfillment D2C-B2B-B2B2C-Amazon-Walmart-marketplace architecture program.",
        "short": "A 2026 B2B ribbon OEM 130-module brand-buyer omni-channel fulfillment D2C-B2B-B2B2C-Amazon-Walmart-marketplace architecture for global brand owners, brand-fulfillment-VPs, brand-D2C-Operators, brand-marketplace-managers, and brand-supply-chain-orchestration-leads. Covers omni-channel, D2C, B2B, B2B2C, Amazon-FBA, Walmart-marketplace, TikTok-shop, Tmall, 3PL, cross-docking, last-mile, returns-recovery, and 27-day time-to-omni-pilot-launch...",
        "mins": "44 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 127-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_127_PM_END = (
    '<a href="blog/blog-ribbon-oem-127-module-brand-buyer-cross-border-tariff-engineering-fta-preference-rules-of-origin-landed-cost-bridge-architecture-global-brand-procurement-2026-09-14-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_127_PM_END not in html:
        raise SystemExit("ANCHOR_127_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_127_PM_END, ANCHOR_127_PM_END + cards_block, 1)
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
    # Anchor: 127-PM (most recent entry already in blog.html)
    anchor_127 = 'blog/blog-ribbon-oem-127-module-brand-buyer-cross-border-tariff-engineering-fta-preference-rules-of-origin-landed-cost-bridge-architecture-global-brand-procurement-2026-09-14-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_127) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    if not pattern.search(html):
        raise SystemExit("anchor 127-PM not found in blog.html")
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = pattern.sub(lambda m: m.group(1) + cards_block, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes, added {len(ENTRIES)} cards (129+130)")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        sm = f.read()
    additions = []
    for e in ENTRIES:
        loc = f"{SITE}/{e['file']}"
        if loc in sm:
            print(f"  sitemap: skip (already present) {loc}")
            continue
        addition = (
            f'  <url>\n'
            f'    <loc>{loc}</loc>\n'
            f'    <lastmod>{e["iso_date"]}</lastmod>\n'
            f'    <changefreq>monthly</changefreq>\n'
            f'    <priority>0.8</priority>\n'
            f'  </url>\n'
        )
        additions.append(addition)
    if additions:
        new_sm = sm.replace('</urlset>', ''.join(additions) + '</urlset>')
        with open(SITEMAP, "w", encoding="utf-8") as f:
            f.write(new_sm)
        print(f"sitemap.xml: {len(sm):,} -> {len(new_sm):,} bytes, added {len(additions)} urls")

if __name__ == "__main__":
    update_index()
    update_blog()
    update_sitemap()
    print("Done.")
