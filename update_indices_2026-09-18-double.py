"""Wire 2026-09-18 cron 2am UTC DOUBLE articles (144-AM, 145-PM) into index.html, blog.html, sitemap.xml.
Anchor: 143-PM card end (most recent article on disk before this batch).
"""
import re, os
WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
TODAY = "2026-09-18"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-144-module-brand-buyer-mill-side-mill-capacity-utilization-production-cascade-architecture-global-brand-procurement-2026-09-18-am.html",
        "date": "2026-09-18 10:00 AM",
        "title": "Ribbon OEM 144-Module Brand-Buyer Mill-Side Mill-Capacity-Utilization &amp; Production-Cascade Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Mill-Capacity-Utilization &amp; Production-Cascade Architecture",
        "iso_date": "2026-09-18",
        "desc": "A 2026 B2B ribbon OEM 144-module brand-buyer mill-side mill-capacity-utilization & production-cascade architecture for global brand procurement directors, brand-supply-chain-VPs, brand-production-planning-leads, brand-private-label-merchandising-directors, and OEM mill-side production-engineering managers. Covers 10-capacity-baseline, 9-load-balance, 8-shift-cascade, 7-peak-reserve, 6-cascade-trigger, 9-bottleneck-decoder, 8-cascade-recovery, 7-OEE-ladder &amp;6-line-balance modules. Delivers 92-98% 18-day-time-to-capacity-pilot-launch, 84-94% capacity-utilization-rate, 44-58% peak-shortfall-recovery, 18-26% OEE-lift, 118 brand partners, 68 EU-27 markets, 71 NA-states, 74 MEA-jurisdictions, 4,190 active SKUs on a 16.2M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side mill-capacity-utilization & production-cascade architecture program.",
        "short": "A 2026 B2B ribbon OEM 144-module brand-buyer mill-side mill-capacity-utilization & production-cascade architecture for global brand procurement directors, brand-supply-chain-VPs, brand-production-planning-leads, brand-private-label-merchandising-directors, and OEM mill-side production-engineering managers. Covers capacity-baseline, load-balance, shift-cascade, peak-reserve, cascade-trigger, bottleneck-decoder, cascade-recovery, OEE-ladder, line-balance, and 18-day time-to-capacity-pilot-launch...",
        "mins": "44 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-145-module-brand-buyer-mill-side-lead-time-engineering-on-time-in-full-otif-architecture-global-brand-procurement-2026-09-18-pm.html",
        "date": "2026-09-18 15:00 PM",
        "title": "Ribbon OEM 145-Module Brand-Buyer Mill-Side Lead-Time-Engineering &amp; On-Time-In-Full (OTIF) Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Lead-Time-Engineering &amp; On-Time-In-Full (OTIF) Architecture",
        "iso_date": "2026-09-18",
        "desc": "A 2026 B2B ribbon OEM 145-module brand-buyer mill-side lead-time-engineering & on-time-in-full (OTIF) architecture for global brand procurement directors, brand-supply-chain-OTIF-leads, brand-retail-replenishment-managers, brand-3PL-logistics-coordinators, and OEM mill-side production-planning engineers. Covers 10-lead-time-baseline, 9-route-engineering, 8-cutoff-cascade, 7-handoff-window, 6-OTIF-monitor, 9-exception-decoder, 8-recovery-protocol, 7-customer-pulse &amp;6-continuous-OTIF modules. Delivers 92-98% 22-day-time-to-OTIF-pilot-launch, 84-94% OTIF-rate, 44-58% lead-time-variance-reduction, 18-26% on-time-delivery-lift, 119 brand partners, 69 EU-27 markets, 72 NA-states, 75 MEA-jurisdictions, 4,210 active SKUs on a 16.3M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side lead-time-engineering & on-time-in-full (OTIF) architecture program.",
        "short": "A 2026 B2B ribbon OEM 145-module brand-buyer mill-side lead-time-engineering & on-time-in-full (OTIF) architecture for global brand procurement directors, brand-supply-chain-OTIF-leads, brand-retail-replenishment-managers, brand-3PL-logistics-coordinators, and OEM mill-side production-planning engineers. Covers lead-time-baseline, route-engineering, cutoff-cascade, handoff-window, OTIF-monitor, exception-decoder, recovery-protocol, customer-pulse, continuous-OTIF, and 22-day time-to-OTIF-pilot-launch...",
        "mins": "44 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 143-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_143_PM_END = (
    '<a href="blog/blog-ribbon-oem-143-module-brand-buyer-mill-side-mill-lab-capability-lab-test-cycle-time-architecture-oeko-tex-reach-cpsia-prop-65-espr-dpp-global-brand-procurement-2026-09-17-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_143_PM_END not in html:
        raise SystemExit("ANCHOR_143_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_143_PM_END, ANCHOR_143_PM_END + cards_block, 1)
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
    anchor_143 = 'blog/blog-ribbon-oem-143-module-brand-buyer-mill-side-mill-lab-capability-lab-test-cycle-time-architecture-oeko-tex-reach-cpsia-prop-65-espr-dpp-global-brand-procurement-2026-09-17-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_143) + r'" class="blog-read-more">Read More &rarr;</a>\s*</article>)'
    )
    if not pattern.search(html):
        raise SystemExit("143-PM anchor not found in blog.html")
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = pattern.sub(lambda m: m.group(1) + cards_block, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

SITEMAP_URL_TEMPLATE = (
    '    <url>\n'
    '        <loc>{loc}</loc>\n'
    '        <lastmod>{lastmod}</lastmod>\n'
    '        <changefreq>weekly</changefreq>\n'
    '        <priority>0.9</priority>\n'
    '    </url>'
)

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    # Insert before </urlset>
    if "</urlset>" not in xml:
        raise SystemExit("</urlset> not found in sitemap.xml")
    blocks = []
    for e in ENTRIES:
        loc = f"{SITE_URL}/{e['file']}"
        blocks.append(SITEMAP_URL_TEMPLATE.format(loc=loc, lastmod=e["iso_date"]))
    insertion = "\n" + "\n".join(blocks) + "\n"
    new_xml = xml.replace("</urlset>", insertion + "</urlset>", 1)
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(new_xml)
    print(f"sitemap.xml: {len(xml):,} -> {len(new_xml):,} bytes (+{len(ENTRIES)} URLs)")

def main():
    update_index()
    update_blog()
    update_sitemap()

if __name__ == "__main__":
    main()
