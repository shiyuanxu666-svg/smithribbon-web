"""Wire 2026-09-11 cron DOUBLE articles (115-AM, 116-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-11"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-115-module-brand-buyer-mill-side-digital-twin-smart-mill-iot-edge-production-architecture-global-brand-procurement-2026-09-11-am.html",
        "date": "2026-09-11 10:00 AM",
        "title": "Ribbon OEM 115-Module Brand-Buyer Mill-Side Digital-Twin Smart-Mill IoT-Edge Production Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Digital-Twin Smart-Mill IoT-Edge Production Architecture",
        "iso_date": "2026-09-11",
        "desc": "A 2026 B2B ribbon OEM 115-module brand-buyer mill-side digital-twin smart-mill IoT-edge production architecture for global brand owners, brand-smart-manufacturing-VPs, brand-Industry-4.0-program-leads, and brand-mill-digital-twin-architects. Covers 12-twin-cadre, 11-edge-engine, 10-iot-mesh-pipeline, 9-production-stack, 8-archive, 7-dashboard, 9-IP, 6-cost &amp; 10-CI modules. Delivers 92-98% 22-day-time-to-twin-pilot-launch, 84-94% edge-data-freshness, 44-58% OEE-lift, 18-26% defect-detection-latency-reduction, 102 brand partners, 56 EU-27 markets, 59 NA-states, 61 MEA-jurisdictions, 3,720 active SKUs on a 14.6M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side digital-twin smart-mill IoT-edge production architecture program.",
        "short": "A 2026 B2B ribbon OEM 115-module brand-buyer mill-side digital-twin smart-mill IoT-edge production architecture for global brand owners, brand-smart-manufacturing-VPs, brand-Industry-4.0-program-leads, and brand-mill-digital-twin-architects. Covers twin cadre, edge engine, IoT mesh pipeline, production stack, and 22-day time-to-twin-pilot-launch...",
        "mins": "39 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-116-module-brand-buyer-cosmetic-contact-compliance-reach-ca-prop-65-heavy-metal-migration-architecture-global-brand-procurement-2026-09-11-pm.html",
        "date": "2026-09-11 15:00 PM",
        "title": "Ribbon OEM 116-Module Brand-Buyer Cosmetic-Contact Compliance REACH/CA Prop 65 Heavy-Metal Migration Architecture 2026",
        "tag": "Brand-Buyer Cosmetic-Contact Compliance REACH/CA Prop 65 Heavy-Metal Migration Architecture",
        "iso_date": "2026-09-11",
        "desc": "A 2026 B2B ribbon OEM 116-module brand-buyer cosmetic-contact compliance REACH/CA Prop 65 heavy-metal migration architecture for global brand owners, brand-cosmetic-compliance-VPs, brand-regulatory-affairs-directors, and brand-product-safety-leads. Covers 12-compliance-cadre, 11-reach-engine, 10-prop65-pipeline, 9-migration-stack, 8-archive, 7-dashboard, 9-IP, 6-cost &amp; 10-CI modules. Delivers 92-98% 23-day-time-to-compliance-pilot-launch, 84-94% migration-test-pass-rate, 44-58% compliance-doc-cycle-reduction, 18-26% regulatory-risk-reduction, 104 brand partners, 57 EU-27 markets, 60 NA-states, 62 MEA-jurisdictions, 3,810 active SKUs on a 15.1M-meter annual multi-brand multi-jurisdiction brand-buyer cosmetic-contact compliance REACH/CA Prop 65 heavy-metal migration architecture program.",
        "short": "A 2026 B2B ribbon OEM 116-module brand-buyer cosmetic-contact compliance REACH/CA Prop 65 heavy-metal migration architecture for global brand owners, brand-cosmetic-compliance-VPs, brand-regulatory-affairs-directors, and brand-product-safety-leads. Covers compliance cadre, REACH engine, Prop 65 pipeline, migration stack, and 23-day time-to-compliance-pilot-launch...",
        "mins": "40 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 114-PM card end (most recent PM in index.html) — insert new cards RIGHT AFTER it.
ANCHOR_114_PM_END = (
    '<a href="blog/blog-ribbon-oem-114-module-brand-buyer-q4-holiday-peak-cascade-multi-market-production-capacity-pre-booking-architecture-global-brand-procurement-2026-09-11-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_114_PM_END not in html:
        raise SystemExit("ANCHOR_114_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_114_PM_END, ANCHOR_114_PM_END + cards_block, 1)
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
    anchor_114 = 'blog/blog-ribbon-oem-114-module-brand-buyer-q4-holiday-peak-cascade-multi-market-production-capacity-pre-booking-architecture-global-brand-procurement-2026-09-11-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_114) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    if not pattern.search(html):
        raise SystemExit("anchor 114-PM not found in blog.html")
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = pattern.sub(lambda m: m.group(1) + cards_block, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        sm = f.read()
    additions = []
    for e in ENTRIES:
        loc = f"{SITE}/{e['file']}"
        # Avoid duplicate insertion
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
        print(f"sitemap.xml: {len(sm):,} -> {len(new_sm):,} bytes, added {len(additions)} URLs")
    else:
        print("sitemap.xml: no additions needed")

def main():
    update_index()
    update_blog()
    update_sitemap()

if __name__ == "__main__":
    main()
