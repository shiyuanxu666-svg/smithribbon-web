"""Wire 2026-08-30 cron DOUBLE-2 articles (100-AM, 101-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-100-module-brand-buyer-holiday-peak-reverse-logistics-returns-recovery-clearance-restock-grade-architecture-global-brand-procurement-2026-08-30-am2.html",
        "date": "2026-08-30 10:30 AM",
        "title": "Ribbon OEM 100-Module Brand-Buyer Holiday-Peak Reverse-Logistics Returns-Recovery Clearance Restock-Grade Architecture 2026",
        "tag": "Brand-Buyer Holiday-Peak Reverse-Logistics Returns-Recovery Clearance Restock-Grade Architecture",
        "iso_date": "2026-08-30",
        "desc": "A 2026 B2B ribbon OEM 100-module brand-buyer holiday-peak reverse-logistics returns-recovery clearance restock-grade architecture for global brand owners, brand-returns-management-VPs, brand-post-peak-supply-chain-leads, and brand-circular-economy-directors. Covers 12-reverse-logistics-cadre, 11-returns-recovery-engine, 10-clearance-restock-pipeline, 9-restock-grade-stack, 8-returns-archive, 7-reverse-dashboard, 9-returns-IP, 6-returns-cost &amp; 10-returns-continuous-improvement modules. Delivers 92-98% 25-day-time-to-reverse-pilot-launch, 84-94% reverse-window-on-time-clearance, 44-58% reverse-cost-reduction, 18-26% restock-yield, 85 brand partners, 46 EU-27 markets, 51 NA-states, 53 MEA-jurisdictions, 3,020 active SKUs on a 11.4M-meter annual multi-brand multi-jurisdiction brand-buyer holiday-peak reverse-logistics returns-recovery clearance restock-grade architecture program.",
        "short": "A 2026 B2B ribbon OEM 100-module brand-buyer holiday-peak reverse-logistics returns-recovery clearance restock-grade architecture for global brand owners, brand-returns-management-VPs, brand-post-peak-supply-chain-leads, and brand-circular-economy-directors. Covers reverse logistics cadre, returns recovery engine, clearance restock pipeline, restock grade stack, returns archive, and 25-day time-to-reverse-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-101-module-brand-buyer-mill-side-carbon-water-scope-3-decarbonization-esg-disclosure-architecture-global-brand-procurement-2026-08-30-pm2.html",
        "date": "2026-08-30 15:30 PM",
        "title": "Ribbon OEM 101-Module Brand-Buyer Mill-Side Carbon-Water Scope-3 Decarbonization ESG-Disclosure Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Carbon-Water Scope-3 Decarbonization ESG-Disclosure Architecture",
        "iso_date": "2026-08-30",
        "desc": "A 2026 B2B ribbon OEM 101-module brand-buyer mill-side carbon-water scope-3 decarbonization ESG-disclosure architecture for global brand owners, brand-ESG-VPs, brand-sustainability-procurement-leads, and brand-CSRD-CSDDD-disclosure-directors. Covers 12-decarbonization-cadre, 11-scope-3-engine, 10-ESG-disclosure-pipeline, 9-carbon-water-stack, 8-CSRD-archive, 7-ESG-dashboard, 9-ESG-IP, 6-ESG-cost &amp; 10-ESG-continuous-improvement modules. Delivers 92-98% 27-day-time-to-ESG-pilot-launch, 84-94% ESG-window-on-time-disclosure, 44-58% scope-3-emission-reduction, 18-26% water-withdrawal-reduction, 86 brand partners, 47 EU-27 markets, 52 NA-states, 54 MEA-jurisdictions, 3,060 active SKUs on a 11.6M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side carbon-water scope-3 decarbonization ESG-disclosure architecture program.",
        "short": "A 2026 B2B ribbon OEM 101-module brand-buyer mill-side carbon-water scope-3 decarbonization ESG-disclosure architecture for global brand owners, brand-ESG-VPs, brand-sustainability-procurement-leads, and brand-CSRD-CSDDD-disclosure-directors. Covers decarbonization cadre, scope 3 engine, ESG disclosure pipeline, carbon water stack, CSRD archive, and 27-day time-to-ESG-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 99-PM card (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_99_PM_END = (
    '<a href="blog/blog-ribbon-oem-99-module-brand-buyer-cross-border-duty-drawback-rebate-export-refund-freight-cost-recovery-architecture-global-brand-procurement-2026-08-30-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    # Insert both cards after 99-PM
    cards_block = "".join(make_index_card(e) for e in ENTRIES)
    if ANCHOR_99_PM_END not in html:
        raise SystemExit("ANCHOR_99_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_99_PM_END, ANCHOR_99_PM_END + cards_block, 1)
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
    # The blog.html uses similar card structure, anchor on the 99-PM article link
    anchor_99 = 'blog/blog-ribbon-oem-99-module-brand-buyer-cross-border-duty-drawback-rebate-export-refund-freight-cost-recovery-architecture-global-brand-procurement-2026-08-30-pm.html'
    # Find a closing </article> right after the 99-PM href
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_99) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    m = pattern.search(html)
    if not m:
        # fallback: anchor on 99-PM href and append cards after the surrounding </article>
        idx = html.find(anchor_99)
        if idx < 0:
            raise SystemExit("99-PM not found in blog.html")
        end = html.find("</article>", idx)
        if end < 0:
            raise SystemExit("</article> after 99-PM not found in blog.html")
        insert_point = end + len("</article>")
        cards_block = "".join(make_blog_card(e) for e in ENTRIES)
        new_html = html[:insert_point] + cards_block + html[insert_point:]
    else:
        cards_block = "".join(make_blog_card(e) for e in ENTRIES)
        new_html = html[:m.end()] + cards_block + html[m.end():]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    today = "2026-08-30"
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
    # Insert after the closing of the last <url>...</url> before </urlset>
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
