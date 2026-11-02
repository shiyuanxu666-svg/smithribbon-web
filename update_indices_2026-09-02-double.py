"""Wire 2026-09-02 cron DOUBLE articles (109-AM, 110-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-109-module-brand-buyer-mill-side-recycled-pet-grs-closed-loop-rpet-recycled-polyester-acrylic-fiber-yarn-traceability-mill-to-shelf-architecture-global-brand-procurement-2026-09-02-am.html",
        "date": "2026-09-02 10:00 AM",
        "title": "Ribbon OEM 109-Module Brand-Buyer Mill-Side Recycled-PET GRS Closed-Loop rPET-Recycled-Polyester-Acrylic-Fiber-Yarn Traceability Mill-to-Shelf Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Recycled-PET GRS Closed-Loop rPET-Recycled-Polyester-Acrylic-Fiber-Yarn Traceability Mill-to-Shelf Architecture",
        "iso_date": "2026-09-02",
        "desc": "A 2026 B2B ribbon OEM 109-module brand-buyer mill-side recycled-PET GRS closed-loop rPET-recycled-polyester-acrylic-fiber-yarn traceability mill-to-shelf architecture for global brand owners, brand-sustainability-VPs, brand-circularity-directors, and brand-rPET-procurement-leads. Covers 12-rPET-cadre, 11-GRS-engine, 10-acrylic-fiber-pipeline, 9-traceability-stack, 8-mill-to-shelf-archive, 7-rPET-dashboard, 9-closed-loop-IP, 6-rPET-cost &amp; 10-rPET-continuous-improvement modules. Delivers 92-98% 28-day-time-to-rPET-pilot-launch, 84-94% rPET-window-on-time-recovery, 44-58% post-consumer-bottle-recovery, 18-26% rPET-yarn-reintroduction, 88 brand partners, 49 EU-27 markets, 54 NA-states, 56 MEA-jurisdictions, 3,140 active SKUs on a 12.0M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side recycled-PET GRS closed-loop rPET-recycled-polyester-acrylic-fiber-yarn traceability mill-to-shelf architecture program.",
        "short": "A 2026 B2B ribbon OEM 109-module brand-buyer mill-side recycled-PET GRS closed-loop rPET-recycled-polyester-acrylic-fiber-yarn traceability mill-to-shelf architecture for global brand owners, brand-sustainability-VPs, brand-circularity-directors, and brand-rPET-procurement-leads. Covers rPET cadre, GRS engine, acrylic fiber pipeline, traceability stack, mill-to-shelf archive, and 28-day time-to-rPET-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-110-module-brand-buyer-multi-tier-sub-tier-subcontracting-4-tier-mapping-risk-resilience-supplier-diversification-transparency-architecture-global-brand-procurement-2026-09-02-pm.html",
        "date": "2026-09-02 15:00 PM",
        "title": "Ribbon OEM 110-Module Brand-Buyer Multi-Tier Sub-Tier Subcontracting 4-Tier Mapping Risk-Resilience Supplier-Diversification Transparency Architecture 2026",
        "tag": "Brand-Buyer Multi-Tier Sub-Tier Subcontracting 4-Tier Mapping Risk-Resilience Supplier-Diversification Transparency Architecture",
        "iso_date": "2026-09-02",
        "desc": "A 2026 B2B ribbon OEM 110-module brand-buyer multi-tier sub-tier subcontracting 4-tier mapping risk-resilience supplier-diversification transparency architecture for global brand owners, brand-procurement-resilience-VPs, brand-supply-chain-risk-directors, and brand-sub-tier-compliance-leads. Covers 12-tier-cadre, 11-sub-tier-engine, 10-subcontracting-pipeline, 9-mapping-stack, 8-resilience-archive, 7-diversification-dashboard, 9-transparency-IP, 6-resilience-cost &amp; 10-resilience-continuous-improvement modules. Delivers 92-98% 27-day-time-to-resilience-pilot-launch, 84-94% resilience-window-on-time-recovery, 44-58% sub-tier-risk-score-reduction, 18-26% supplier-diversification-coverage, 91 brand partners, 52 EU-27 markets, 57 NA-states, 59 MEA-jurisdictions, 3,260 active SKUs on a 12.6M-meter annual multi-brand multi-jurisdiction brand-buyer multi-tier sub-tier subcontracting 4-tier mapping risk-resilience supplier-diversification transparency architecture program.",
        "short": "A 2026 B2B ribbon OEM 110-module brand-buyer multi-tier sub-tier subcontracting 4-tier mapping risk-resilience supplier-diversification transparency architecture for global brand owners, brand-procurement-resilience-VPs, brand-supply-chain-risk-directors, and brand-sub-tier-compliance-leads. Covers tier cadre, sub-tier engine, subcontracting pipeline, mapping stack, resilience archive, and 27-day time-to-resilience-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 108-PM card end (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_108_PM_END = (
    '<a href="blog/blog-ribbon-oem-108-module-brand-buyer-multi-market-cross-border-ddp-landed-cost-customs-broker-duty-vat-optimization-architecture-global-brand-procurement-2026-09-01-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_108_PM_END not in html:
        raise SystemExit("ANCHOR_108_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_108_PM_END, ANCHOR_108_PM_END + cards_block, 1)
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
    anchor_108 = 'blog/blog-ribbon-oem-108-module-brand-buyer-multi-market-cross-border-ddp-landed-cost-customs-broker-duty-vat-optimization-architecture-global-brand-procurement-2026-09-01-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_108) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    m = pattern.search(html)
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    if m:
        new_html = html[:m.end()] + cards_block + html[m.end():]
    else:
        idx = html.find(anchor_108)
        if idx < 0:
            raise SystemExit("108-PM not found in blog.html")
        end = html.find("</article>", idx)
        if end < 0:
            raise SystemExit("</article> after 108-PM not found in blog.html")
        insert_point = end + len("</article>")
        new_html = html[:insert_point] + cards_block + html[insert_point:]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    today = "2026-09-02"
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
