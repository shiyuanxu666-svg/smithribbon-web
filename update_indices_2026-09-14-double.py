"""Wire 2026-09-14 cron DOUBLE articles (126-AM, 127-PM) into index.html, blog.html, sitemap.xml.
Anchors: 125-PM (the most recent article on disk before this batch)."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-14"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-126-module-brand-buyer-mill-side-quality-issue-8d-root-cause-supplier-recovery-capa-playbook-ai-vision-closed-loop-architecture-global-brand-procurement-2026-09-14-am.html",
        "date": "2026-09-14 10:00 AM",
        "title": "Ribbon OEM 126-Module Brand-Buyer Mill-Side Quality-Issue 8D-Root-Cause Supplier-Recovery CAPA Playbook AI-Vision-Closed-Loop Architecture 2026",
        "tag": "Brand-Buyer Mill-Side Quality-Issue 8D-Root-Cause Supplier-Recovery CAPA Playbook AI-Vision-Closed-Loop Architecture",
        "iso_date": "2026-09-14",
        "desc": "A 2026 B2B ribbon OEM 126-module brand-buyer mill-side quality-issue 8D-root-cause supplier-recovery CAPA playbook AI-vision-closed-loop architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers 8-8D, 7-5-why, 6-fishbone, 5-IS-NOT-IS, 4-escape-point, 9-CAPA, 8-corrective, 7-preventive, 6-verification, 9-supplier-recovery, 8-supplier-scorecard, 7-AI-vision-closed-loop, 6-defect-library, 5-AQL &amp; 4-PPAP modules. Delivers 92-98% 27-day-time-to-CAPA-pilot-launch, 84-94% escape-point-detection-rate, 44-58% recurrence-reduction, 18-26% AQL-pass-rate-lift, 108 brand partners, 60 EU-27 markets, 63 NA-states, 66 MEA-jurisdictions, 3,970 active SKUs on a 15.4M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side quality-issue 8D-root-cause supplier-recovery CAPA playbook AI-vision-closed-loop architecture program.",
        "short": "A 2026 B2B ribbon OEM 126-module brand-buyer mill-side quality-issue 8D-root-cause supplier-recovery CAPA playbook AI-vision-closed-loop architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers 8D-process, 5-why, fishbone, IS-NOT-IS, escape-point, CAPA, corrective, preventive, verification, supplier-recovery, supplier-scorecard, AI-vision-closed-loop, defect-library, AQL, PPAP, and 27-day time-to-CAPA-pilot-launch...",
        "mins": "43 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-127-module-brand-buyer-cross-border-tariff-engineering-fta-preference-rules-of-origin-landed-cost-bridge-architecture-global-brand-procurement-2026-09-14-pm.html",
        "date": "2026-09-14 15:00 PM",
        "title": "Ribbon OEM 127-Module Brand-Buyer Cross-Border Tariff-Engineering FTA-Preference Rules-of-Origin Landed-Cost Bridge Architecture 2026",
        "tag": "Brand-Buyer Cross-Border Tariff-Engineering FTA-Preference Rules-of-Origin Landed-Cost Bridge Architecture",
        "iso_date": "2026-09-14",
        "desc": "A 2026 B2B ribbon OEM 127-module brand-buyer cross-border tariff-engineering FTA-preference rules-of-origin landed-cost bridge architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers 12-tariff-engineering, 11-HS-classification, 10-FTA-preference, 9-rules-of-origin, 8-COO-cert, 7-landed-cost-bridge, 6-drawback, 5-bonded-warehouse, 4-AEO, 9-EU-CBAM, 8-US-301, 7-UK-GSP, 6-RCEP &amp; 5-CPTPP modules. Delivers 92-98% 28-day-time-to-tariff-pilot-launch, 84-94% FTA-preference-yield, 44-58% landed-cost-bridge-savings, 18-26% tariff-engineering-deflection, 109 brand partners, 61 EU-27 markets, 64 NA-states, 67 MEA-jurisdictions, 4,000 active SKUs on a 15.5M-meter annual multi-brand multi-jurisdiction brand-buyer cross-border tariff-engineering FTA-preference rules-of-origin landed-cost-bridge architecture program.",
        "short": "A 2026 B2B ribbon OEM 127-module brand-buyer cross-border tariff-engineering FTA-preference rules-of-origin landed-cost-bridge architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers tariff-engineering, HS-classification, FTA-preference, rules-of-origin, COO-cert, landed-cost-bridge, drawback, bonded-warehouse, AEO, EU-CBAM, US-301, UK-GSP, RCEP, CPTPP, and 28-day time-to-tariff-pilot-launch...",
        "mins": "44 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 125-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_125_PM_END = (
    '<a href="blog/blog-ribbon-oem-125-module-brand-buyer-co-branded-holiday-cascade-multi-market-gifting-bundle-reverse-logistics-recovery-returns-clearance-architecture-global-brand-procurement-2026-09-14-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_125_PM_END not in html:
        raise SystemExit("ANCHOR_125_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_125_PM_END, ANCHOR_125_PM_END + cards_block, 1)
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
    # Anchor: 125-PM (most recent entry already in blog.html)
    anchor_125 = 'blog/blog-ribbon-oem-125-module-brand-buyer-co-branded-holiday-cascade-multi-market-gifting-bundle-reverse-logistics-recovery-returns-clearance-architecture-global-brand-procurement-2026-09-14-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_125) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    if not pattern.search(html):
        raise SystemExit("anchor 125-PM not found in blog.html")
    cards_block = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = pattern.sub(lambda m: m.group(1) + cards_block, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes, added {len(ENTRIES)} cards (126+127)")

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
