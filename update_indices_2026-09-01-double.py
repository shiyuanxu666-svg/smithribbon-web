"""Wire 2026-09-01 cron DOUBLE articles (107-AM, 108-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-107-module-brand-buyer-mill-side-circular-economy-closed-loop-take-back-reuse-recycling-refurbishment-architecture-global-brand-procurement-2026-09-01-am.html",
        "date": "2026-09-01 10:00 AM",
        "title": "Ribbon OEM 107-Module Brand-Buyer Mill-Side Circular-Economy Closed-Loop Take-Back Reuse Recycling Refurbishment Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Circular-Economy Closed-Loop Take-Back Reuse Recycling Refurbishment Architecture",
        "iso_date": "2026-09-01",
        "desc": "A 2026 B2B ribbon OEM 107-module brand-buyer mill-side circular-economy closed-loop take-back reuse recycling refurbishment architecture for global brand owners, brand-circularity-VPs, brand-EPR-compliance-directors, and brand-post-consumer-recovery-leads. Covers 12-circular-cadre, 11-take-back-engine, 10-reuse-pipeline, 9-recycle-stack, 8-refurb-archive, 7-circular-dashboard, 9-take-back-IP, 6-circular-cost &amp; 10-circular-continuous-improvement modules. Delivers 92-98% 27-day-time-to-circular-pilot-launch, 84-94% take-back-window-on-time-recovery, 44-58% post-consumer-fiber-recovery, 18-26% closed-loop-yarn-reintroduction, 89 brand partners, 50 EU-27 markets, 55 NA-states, 57 MEA-jurisdictions, 3,180 active SKUs on a 12.2M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side circular-economy closed-loop take-back reuse recycling refurbishment architecture program.",
        "short": "A 2026 B2B ribbon OEM 107-module brand-buyer mill-side circular-economy closed-loop take-back reuse recycling refurbishment architecture for global brand owners, brand-circularity-VPs, brand-EPR-compliance-directors, and brand-post-consumer-recovery-leads. Covers circular cadre, take-back engine, reuse pipeline, recycle stack, refurb archive, and 27-day time-to-circular-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-108-module-brand-buyer-multi-market-cross-border-ddp-landed-cost-customs-broker-duty-vat-optimization-architecture-global-brand-procurement-2026-09-01-pm.html",
        "date": "2026-09-01 15:00 PM",
        "title": "Ribbon OEM 108-Module Brand-Buyer Multi-Market Cross-Border DDP Landed-Cost Customs-Broker Duty-Vat Optimization Architecture 2026",
        "tag": "Brand-Buyer Multi-Market Cross-Border DDP Landed-Cost Customs-Broker Duty-Vat Optimization Architecture",
        "iso_date": "2026-09-01",
        "desc": "A 2026 B2B ribbon OEM 108-module brand-buyer multi-market cross-border DDP landed-cost customs-broker duty-VAT optimization architecture for global brand owners, brand-landed-cost-VPs, brand-cross-border-procurement-directors, and brand-customs-compliance-leads. Covers 12-DDP-cadre, 11-customs-broker-engine, 10-duty-VAT-pipeline, 9-landed-cost-stack, 8-DDP-archive, 7-landed-cost-dashboard, 9-DDP-IP, 6-DDP-cost &amp; 10-DDP-continuous-improvement modules. Delivers 92-98% 29-day-time-to-DDP-pilot-launch, 84-94% landed-cost-window-on-time-clearance, 44-58% duty-VAT-recovery, 18-26% landed-cost-reduction, 90 brand partners, 51 EU-27 markets, 56 NA-states, 58 MEA-jurisdictions, 3,220 active SKUs on a 12.4M-meter annual multi-brand multi-jurisdiction brand-buyer multi-market cross-border DDP landed-cost customs-broker duty-VAT optimization architecture program.",
        "short": "A 2026 B2B ribbon OEM 108-module brand-buyer multi-market cross-border DDP landed-cost customs-broker duty-VAT optimization architecture for global brand owners, brand-landed-cost-VPs, brand-cross-border-procurement-directors, and brand-customs-compliance-leads. Covers DDP cadre, customs broker engine, duty VAT pipeline, landed cost stack, DDP archive, and 29-day time-to-DDP-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 106-PM card end (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_106_PM_END = (
    '<a href="blog/blog-ribbon-oem-106-module-brand-buyer-mill-side-eco-modulated-accu-product-carbon-footprint-pcf-api-architecture-global-brand-procurement-2026-08-31-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_106_PM_END not in html:
        raise SystemExit("ANCHOR_106_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_106_PM_END, ANCHOR_106_PM_END + cards_block, 1)
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
    anchor_106 = 'blog/blog-ribbon-oem-106-module-brand-buyer-mill-side-eco-modulated-accu-product-carbon-footprint-pcf-api-architecture-global-brand-procurement-2026-08-31-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_106) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    m = pattern.search(html)
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    if m:
        new_html = html[:m.end()] + cards_block + html[m.end():]
    else:
        idx = html.find(anchor_106)
        if idx < 0:
            raise SystemExit("106-PM not found in blog.html")
        end = html.find("</article>", idx)
        if end < 0:
            raise SystemExit("</article> after 106-PM not found in blog.html")
        insert_point = end + len("</article>")
        new_html = html[:insert_point] + cards_block + html[insert_point:]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    today = "2026-09-01"
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
