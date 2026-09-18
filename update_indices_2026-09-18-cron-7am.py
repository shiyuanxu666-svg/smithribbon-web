"""Wire 2026-09-18 cron 7am UTC DOUBLE articles (146-AM, 147-PM) into index.html, blog.html, sitemap.xml.
Anchor: 145-PM card end (most recent article on disk before this batch).
"""
import re, os
WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
TODAY = "2026-09-18"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-146-module-brand-buyer-mill-side-brand-spec-sheet-tech-pack-translation-decoder-architecture-global-brand-procurement-2026-09-18-am.html",
        "date": "2026-09-18 10:00 AM",
        "title": "Ribbon OEM 146-Module Brand-Buyer Mill-Side Brand-Spec-Sheet &amp; Tech-Pack Translation-Decoder Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Brand-Spec-Sheet &amp; Tech-Pack Translation-Decoder Architecture",
        "iso_date": "2026-09-18",
        "desc": "A 2026 B2B ribbon OEM 146-module brand-buyer mill-side brand-spec-sheet & tech-pack translation-decoder architecture for global brand procurement directors, brand-product-development-managers, brand-private-label-merchandising-directors, brand-tech-pack-engineers, and OEM mill-side sample-room coordinators. Covers 10-spec-intake, 9-tech-pack-mapping, 8-translation-decoder, 7-bilingual-glossary, 6-ambiguity-flag, 9-dimension-tolerance, 8-color-Pantone-cross-reference, 7-finish-decode &amp;6-cross-functional-handoff modules. Delivers 92-98% 18-day-time-to-spec-pilot-launch, 84-94% spec-acceptance-rate, 44-58% ambiguity-resolution-lift, 18-26% tech-pack-clarity-lift, 120 brand partners, 70 EU-27 markets, 73 NA-states, 76 MEA-jurisdictions, 4,230 active SKUs on a 16.4M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side brand-spec-sheet & tech-pack translation-decoder architecture program.",
        "short": "A 2026 B2B ribbon OEM 146-module brand-buyer mill-side brand-spec-sheet & tech-pack translation-decoder architecture for global brand procurement directors, brand-product-development-managers, brand-private-label-merchandising-directors, brand-tech-pack-engineers, and OEM mill-side sample-room coordinators. Covers spec-intake, tech-pack-mapping, translation-decoder, bilingual-glossary, ambiguity-flag, dimension-tolerance, color-Pantone-cross-reference, finish-decode, cross-functional-handoff, and 18-day time-to-spec-pilot-launch...",
        "mins": "44 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-147-module-brand-buyer-mill-side-pre-production-sample-pps-first-article-approval-faa-architecture-global-brand-procurement-2026-09-18-pm.html",
        "date": "2026-09-18 15:00 PM",
        "title": "Ribbon OEM 147-Module Brand-Buyer Mill-Side Pre-Production Sample (PPS) &amp; First-Article Approval (FAA) Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Pre-Production Sample (PPS) &amp; First-Article Approval (FAA) Architecture",
        "iso_date": "2026-09-18",
        "desc": "A 2026 B2B ribbon OEM 147-module brand-buyer mill-side pre-production sample (PPS) & first-article approval (FAA) architecture for global brand procurement directors, brand-quality-directors, brand-product-engineers, brand-factory-audit-leads, and OEM mill-side pre-production sample-room supervisors. Covers 10-PPS-baseline, 9-FAA-protocol, 8-sample-bundle, 7-measurement-grid, 6-acceptance-criteria, 9-rework-loop, 8-signature-binder, 7-retain-archive &amp;6-PPS-to-mass-production modules. Delivers 92-98% 22-day-time-to-PPS-pilot-launch, 84-94% first-article-approval-rate, 44-58% rework-cycle-reduction, 18-26% mass-production-yield-lift, 121 brand partners, 71 EU-27 markets, 74 NA-states, 77 MEA-jurisdictions, 4,250 active SKUs on a 16.5M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side pre-production sample (PPS) & first-article approval (FAA) architecture program.",
        "short": "A 2026 B2B ribbon OEM 147-module brand-buyer mill-side pre-production sample (PPS) & first-article approval (FAA) architecture for global brand procurement directors, brand-quality-directors, brand-product-engineers, brand-factory-audit-leads, and OEM mill-side pre-production sample-room supervisors. Covers PPS-baseline, FAA-protocol, sample-bundle, measurement-grid, acceptance-criteria, rework-loop, signature-binder, retain-archive, PPS-to-mass-production, and 22-day time-to-PPS-pilot-launch...",
        "mins": "44 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 145-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_145_PM_END = (
    '<a href="blog/blog-ribbon-oem-145-module-brand-buyer-mill-side-lead-time-engineering-on-time-in-full-otif-architecture-global-brand-procurement-2026-09-18-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_145_PM_END not in html:
        raise SystemExit("ANCHOR_145_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_145_PM_END, ANCHOR_145_PM_END + cards_block, 1)
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
    anchor_145 = 'blog/blog-ribbon-oem-145-module-brand-buyer-mill-side-lead-time-engineering-on-time-in-full-otif-architecture-global-brand-procurement-2026-09-18-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_145) + r'" class="blog-read-more">Read More &rarr;</a>\s*</article>)'
    )
    if not pattern.search(html):
        raise SystemExit("145-PM anchor not found in blog.html")
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
