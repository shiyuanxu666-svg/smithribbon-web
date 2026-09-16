"""Wire 2026-09-16 cron 7am UTC DOUBLE articles (136-AM, 137-PM) into index.html, blog.html, sitemap.xml.
Anchors: 135-PM (the most recent article on disk before this batch).
"""
import re, os
WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
TODAY = "2026-09-16"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-136-module-brand-buyer-mill-side-brand-onboarding-knowledge-transfer-architecture-global-brand-procurement-2026-09-16-am.html",
        "date": "2026-09-16 10:00 AM",
        "title": "Ribbon OEM 136-Module Brand-Buyer Mill-Side Brand-Onboarding Knowledge-Transfer Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Brand-Onboarding Knowledge-Transfer Architecture",
        "iso_date": "2026-09-16",
        "desc": "A 2026 B2B ribbon OEM 136-module brand-buyer mill-side brand-onboarding knowledge-transfer architecture for global brand procurement directors, brand-sourcing-VPs, private-label merchandising controllers, brand-supplier-development managers, and OEM mill-side engineering leads. Covers 10-kickoff-brief, 9-knowledge-transfer, 8-supplier-day, 7-line-walk, 6-PPAP-handoff, 9-traceability, 8-quality-handoff, 7-logistics-handoff &amp;6-renewal-trigger modules. Delivers 92-98% 24-day-time-to-onboard-pilot-launch, 84-94% knowledge-retention-rate, 44-58% first-pass-acceptance, 18-26% renewal-rate-lift, 115 brand partners, 66 EU-27 markets, 69 NA-states, 72 MEA-jurisdictions, 4,150 active SKUs on a 16.0M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side brand-onboarding knowledge-transfer architecture program.",
        "short": "A 2026 B2B ribbon OEM 136-module brand-buyer mill-side brand-onboarding knowledge-transfer architecture for global brand procurement directors, brand-sourcing-VPs, private-label merchandising controllers, brand-supplier-development managers, and OEM mill-side engineering leads. Covers kickoff-brief, knowledge-transfer, supplier-day, line-walk, PPAP-handoff, traceability, quality-handoff, logistics-handoff, renewal-trigger, and 24-day time-to-onboard-pilot-launch...",
        "mins": "44 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-137-module-brand-buyer-mill-side-multi-year-supplier-lifecycle-contract-renewal-architecture-global-brand-procurement-2026-09-16-pm.html",
        "date": "2026-09-16 15:00 PM",
        "title": "Ribbon OEM 137-Module Brand-Buyer Mill-Side Multi-Year Supplier-Lifecycle Contract-Renewal Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Multi-Year Supplier-Lifecycle Contract-Renewal Architecture",
        "iso_date": "2026-09-16",
        "desc": "A 2026 B2B ribbon OEM 137-module brand-buyer mill-side multi-year supplier-lifecycle contract-renewal architecture for global brand procurement directors, brand-supplier-lifecycle-VPs, brand-contract-management counsel, brand-renewal-program directors, and OEM mill-side commercial leads. Covers 10-renewal-strategy, 9-supplier-scorecard, 8-volume-commit, 7-pricing-renewal, 6-SLA-renewal, 9-IP-renewal, 8-trace-renewal, 7-ESG-renewal &amp;6-multi-year modules. Delivers 92-98% 28-day-time-to-renewal-pilot-launch, 84-94% renewal-win-rate, 44-58% multi-year-margin-lift, 18-26% multi-year-volume-commit, 116 brand partners, 67 EU-27 markets, 70 NA-states, 73 MEA-jurisdictions, 4,170 active SKUs on a 16.1M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side multi-year supplier-lifecycle contract-renewal architecture program.",
        "short": "A 2026 B2B ribbon OEM 137-module brand-buyer mill-side multi-year supplier-lifecycle contract-renewal architecture for global brand procurement directors, brand-supplier-lifecycle-VPs, brand-contract-management counsel, brand-renewal-program directors, and OEM mill-side commercial leads. Covers renewal-strategy, supplier-scorecard, volume-commit, pricing-renewal, SLA-renewal, IP-renewal, trace-renewal, ESG-renewal, multi-year, and 28-day time-to-renewal-pilot-launch...",
        "mins": "44 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 135-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_135_PM_END = (
    '<a href="blog/blog-ribbon-oem-135-module-brand-buyer-mill-side-factory-cooperation-partnership-long-term-strategy-global-brand-procurement-architecture-2026-09-16-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_135_PM_END not in html:
        raise SystemExit("ANCHOR_135_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_135_PM_END, ANCHOR_135_PM_END + cards_block, 1)
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
    # Anchor: 135-PM (most recent entry already in blog.html)
    anchor_135 = 'blog/blog-ribbon-oem-135-module-brand-buyer-mill-side-factory-cooperation-partnership-long-term-strategy-global-brand-procurement-architecture-2026-09-16-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_135) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        raise SystemExit("Anchor 135-PM not found in blog.html")
    blog_block = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = html[: m.end()] + blog_block + html[m.end():]
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def make_sitemap_url(e):
    return (
        '\n  <url>\n'
        f'    <loc>{SITE_URL}/blog/{e["file"].split("/", 1)[1]}</loc>\n'
        f'    <lastmod>{e["iso_date"]}</lastmod>\n'
        '    <changefreq>monthly</changefreq>\n'
        '    <priority>0.8</priority>\n'
        '  </url>'
    )

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    # Anchor: 135-PM url block end
    anchor_135_loc = f'{SITE_URL}/blog/blog-ribbon-oem-135-module-brand-buyer-mill-side-factory-cooperation-partnership-long-term-strategy-global-brand-procurement-architecture-2026-09-16-pm.html'
    pattern = re.compile(
        r'(    <loc>' + re.escape(anchor_135_loc) + r'</loc>\s*\n\s*<lastmod>[^<]+</lastmod>\s*\n\s*<changefreq>[^<]+</changefreq>\s*\n\s*<priority>[^<]+</priority>\s*\n\s*</url>)',
        re.DOTALL,
    )
    m = pattern.search(xml)
    if not m:
        raise SystemExit("Anchor 135-PM not found in sitemap.xml")
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