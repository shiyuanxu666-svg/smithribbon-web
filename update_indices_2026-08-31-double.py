"""Wire 2026-08-31 cron DOUBLE articles (102-AM, 103-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-102-module-brand-buyer-mill-side-renewable-energy-ppa-power-purchase-agreement-decarbonization-architecture-global-brand-procurement-2026-08-31-am.html",
        "date": "2026-08-31 10:00 AM",
        "title": "Ribbon OEM 102-Module Brand-Buyer Mill-Side Renewable-Energy PPA Power-Purchase-Agreement Decarbonization Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Renewable-Energy PPA Power-Purchase-Agreement Decarbonization Architecture",
        "iso_date": "2026-08-31",
        "desc": "A 2026 B2B ribbon OEM 102-module brand-buyer mill-side renewable-energy PPA power-purchase-agreement decarbonization architecture for global brand owners, brand-ESG-VPs, brand-sustainability-procurement-leads, and brand-RE100-renewable-electricity-directors. Covers 12-renewable-cadre, 11-PPA-engine, 10-RE100-pipeline, 9-renewable-stack, 8-PPA-archive, 7-RE100-dashboard, 9-PPA-IP, 6-renewable-cost &amp; 10-renewable-continuous-improvement modules. Delivers 92-98% 26-day-time-to-PPA-pilot-launch, 84-94% RE100-window-on-time-attestation, 44-58% scope-2-emission-reduction, 18-26% grid-electricity-displacement, 87 brand partners, 48 EU-27 markets, 53 NA-states, 55 MEA-jurisdictions, 3,100 active SKUs on a 11.8M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side renewable-energy PPA power-purchase-agreement decarbonization architecture program.",
        "short": "A 2026 B2B ribbon OEM 102-module brand-buyer mill-side renewable-energy PPA power-purchase-agreement decarbonization architecture for global brand owners, brand-ESG-VPs, brand-sustainability-procurement-leads, and brand-RE100-renewable-electricity-directors. Covers renewable cadre, PPA engine, RE100 pipeline, renewable stack, PPA archive, and 26-day time-to-PPA-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-103-module-brand-buyer-multi-tier-sub-component-supplier-carbon-audit-tier-4-transparency-architecture-global-brand-procurement-2026-08-31-pm.html",
        "date": "2026-08-31 15:00 PM",
        "title": "Ribbon OEM 103-Module Brand-Buyer Multi-Tier Sub-Component Supplier Carbon-Audit Tier-4 Transparency Architecture 2026",
        "tag": "Brand-Buyer Multi-Tier Sub-Component Supplier Carbon-Audit Tier-4 Transparency Architecture",
        "iso_date": "2026-08-31",
        "desc": "A 2026 B2B ribbon OEM 103-module brand-buyer multi-tier sub-component supplier carbon-audit tier-4 transparency architecture for global brand owners, brand-sustainability-VPs, brand-scope-3-procurement-leads, and brand-supply-chain-decarbonization-directors. Covers 12-tier-4-cadre, 11-sub-component-audit-engine, 10-tier-4-pipeline, 9-carbon-tier-stack, 8-tier-4-archive, 7-tier-4-dashboard, 9-tier-4-IP, 6-tier-4-cost &amp; 10-tier-4-continuous-improvement modules. Delivers 92-98% 28-day-time-to-tier-4-pilot-launch, 84-94% tier-4-window-on-time-attestation, 44-58% tier-4-emission-reduction, 18-26% sub-tier-disclosure-coverage, 88 brand partners, 49 EU-27 markets, 54 NA-states, 56 MEA-jurisdictions, 3,140 active SKUs on a 12.0M-meter annual multi-brand multi-jurisdiction brand-buyer multi-tier sub-component supplier carbon-audit tier-4 transparency architecture program.",
        "short": "A 2026 B2B ribbon OEM 103-module brand-buyer multi-tier sub-component supplier carbon-audit tier-4 transparency architecture for global brand owners, brand-sustainability-VPs, brand-scope-3-procurement-leads, and brand-supply-chain-decarbonization-directors. Covers tier 4 cadre, sub-component audit engine, tier 4 pipeline, carbon tier stack, tier 4 archive, and 28-day time-to-tier-4-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 101-PM card (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_101_PM_END = (
    '<a href="blog/blog-ribbon-oem-101-module-brand-buyer-mill-side-carbon-water-scope-3-decarbonization-esg-disclosure-architecture-global-brand-procurement-2026-08-30-pm2.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_101_PM_END not in html:
        raise SystemExit("ANCHOR_101_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_101_PM_END, ANCHOR_101_PM_END + cards_block, 1)
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
    anchor_101 = 'blog/blog-ribbon-oem-101-module-brand-buyer-mill-side-carbon-water-scope-3-decarbonization-esg-disclosure-architecture-global-brand-procurement-2026-08-30-pm2.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_101) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    m = pattern.search(html)
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    if m:
        new_html = html[:m.end()] + cards_block + html[m.end():]
    else:
        idx = html.find(anchor_101)
        if idx < 0:
            raise SystemExit("101-PM not found in blog.html")
        end = html.find("</article>", idx)
        if end < 0:
            raise SystemExit("</article> after 101-PM not found in blog.html")
        insert_point = end + len("</article>")
        new_html = html[:insert_point] + cards_block + html[insert_point:]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    today = "2026-08-31"
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
