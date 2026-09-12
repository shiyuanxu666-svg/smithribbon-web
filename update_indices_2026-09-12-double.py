"""Wire 2026-09-12 cron DOUBLE articles (119-AM, 120-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-12"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-119-module-brand-buyer-total-cost-of-ownership-tco-7-layer-hidden-cost-decoder-architecture-global-brand-procurement-2026-09-12-am.html",
        "date": "2026-09-12 10:00 AM",
        "title": "Ribbon OEM 119-Module Brand-Buyer Total-Cost-of-Ownership TCO 7-Layer Hidden-Cost Decoder Architecture 2026",
        "tag": "Brand-Buyer Total-Cost-of-Ownership TCO 7-Layer Hidden-Cost Decoder Architecture",
        "iso_date": "2026-09-12",
        "desc": "A 2026 B2B ribbon OEM 119-module brand-buyer total-cost-of-ownership (TCO) 7-layer hidden-cost decoder architecture for global brand procurement directors, retail private-label sourcing leaders, beauty and fashion merchandising VPs, holiday-gifting category sourcing heads, and OEM program management offices. Covers 12-tco-cadre, 11-decoder-engine, 10-hidden-cost-pipeline, 9-should-cost-stack, 8-archive, 7-dashboard, 9-IP, 6-cost &amp; 10-CI modules. Delivers 92-98% 21-day-time-to-tco-pilot-launch, 84-94% hidden-cost-detection-rate, 44-58% tco-driven-savings-yield, 18-26% should-cost-accuracy-lift, 104 brand partners, 57 EU-27 markets, 60 NA-states, 62 MEA-jurisdictions, 3,820 active SKUs on a 14.8M-meter annual multi-brand multi-jurisdiction brand-buyer TCO 7-layer hidden-cost decoder architecture program.",
        "short": "A 2026 B2B ribbon OEM 119-module brand-buyer TCO 7-layer hidden-cost decoder architecture for global brand procurement directors, retail private-label sourcing leaders, beauty and fashion merchandising VPs, holiday-gifting category sourcing heads, and OEM program management offices. Covers TCO cadre, decoder engine, hidden-cost pipeline, should-cost stack, and 21-day time-to-tco-pilot-launch...",
        "mins": "39 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-120-module-brand-buyer-quality-issue-8d-root-cause-supplier-recovery-capa-playbook-architecture-global-brand-procurement-2026-09-12-pm.html",
        "date": "2026-09-12 15:00 PM",
        "title": "Ribbon OEM 120-Module Brand-Buyer Quality-Issue 8D Root-Cause Supplier-Recovery CAPA Playbook Architecture 2026",
        "tag": "Brand-Buyer Quality-Issue 8D Root-Cause Supplier-Recovery CAPA Playbook Architecture",
        "iso_date": "2026-09-12",
        "desc": "A 2026 B2B ribbon OEM 120-module brand-buyer quality-issue 8D root-cause supplier-recovery CAPA playbook architecture for global brand quality directors, retail private-label QA leaders, beauty and fashion merchandising VPs, holiday-gifting category sourcing heads, and OEM supplier-quality program offices. Covers 12-8d-cadre, 11-capa-engine, 10-root-cause-pipeline, 9-supplier-recovery-stack, 8-archive, 7-dashboard, 9-IP, 6-cost &amp; 10-CI modules. Delivers 92-98% 22-day-time-to-8d-pilot-launch, 84-94% capa-closure-rate, 44-58% repeat-defect-reduction, 18-26% supplier-recovery-cycle-time-lift, 106 brand partners, 58 EU-27 markets, 61 NA-states, 63 MEA-jurisdictions, 3,910 active SKUs on a 15.3M-meter annual multi-brand multi-jurisdiction brand-buyer quality-issue 8D root-cause supplier-recovery CAPA playbook architecture program.",
        "short": "A 2026 B2B ribbon OEM 120-module brand-buyer quality-issue 8D root-cause supplier-recovery CAPA playbook architecture for global brand quality directors, retail private-label QA leaders, beauty and fashion merchandising VPs, holiday-gifting category sourcing heads, and OEM supplier-quality program offices. Covers 8D cadre, CAPA engine, root-cause pipeline, supplier-recovery stack, and 22-day time-to-8d-pilot-launch...",
        "mins": "40 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 118-PM card end (most recent PM in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_118_PM_END = (
    '<a href="blog-ribbon-oem-118-module-brand-buyer-multi-tier-supplier-consolidation-vendor-base-rationalization-tier-1-tier-2-tier-3-ribbon-procurement-architecture-global-brand-procurement-2026-09-12-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_118_PM_END not in html:
        raise SystemExit("ANCHOR_118_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_118_PM_END, ANCHOR_118_PM_END + cards_block, 1)
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
    # Find the 116-PM anchor (most recent entry already in blog.html)
    anchor_116 = 'blog/blog-ribbon-oem-116-module-brand-buyer-cosmetic-contact-compliance-reach-ca-prop-65-heavy-metal-migration-architecture-global-brand-procurement-2026-09-11-pm.html'
    # Insert 117, 118, 119, 120 to catch up blog.html (since 117/118 were never wired)
    all_entries = [
        # 117 (already on disk, missing from blog.html)
        {
            "slot": "am",
            "file": "blog/blog-ribbon-oem-117-module-brand-buyer-make-vs-buy-bow-assembly-hand-tie-vs-pre-tied-in-house-vs-outsourced-ribbon-conversion-architecture-global-brand-procurement-2026-09-12-am.html",
            "date": "2026-09-12 10:00 AM",
            "title": "Ribbon OEM 117-Module Brand-Buyer Make-vs-Buy Bow-Assembly, Hand-Tie vs Pre-Tied, In-House vs Outsourced Ribbon-Conversion Architecture 2026",
            "short": "A 2026 B2B ribbon OEM 117-module make-vs-buy bow-assembly, hand-tie vs pre-tied, in-house vs outsourced ribbon-conversion architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers make-vs-buy decision-tree, hand-tie-vs-pre-tied mix, in-house line-build, outsourced partner-tier, cost-volume curve, quality-tier...",
        },
        # 118
        {
            "slot": "pm",
            "file": "blog/blog-ribbon-oem-118-module-brand-buyer-multi-tier-supplier-consolidation-vendor-base-rationalization-tier-1-tier-2-tier-3-ribbon-procurement-architecture-global-brand-procurement-2026-09-12-pm.html",
            "date": "2026-09-12 15:00 PM",
            "title": "Ribbon OEM 118-Module Brand-Buyer Multi-Tier Supplier-Consolidation, Vendor-Base Rationalization &amp; Tier-1/Tier-2/Tier-3 Ribbon-Procurement Architecture 2026",
            "short": "A 2026 B2B ribbon OEM 118-module multi-tier supplier-consolidation, vendor-base rationalization, tier-1/tier-2/tier-3 ribbon-procurement architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers supplier-tier-strategy, vendor-base-rationalization, tier-1 strategic partner, tier-2 preferred partner, tier-3 transactional...",
        },
    ] + ENTRIES
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_116) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    if not pattern.search(html):
        raise SystemExit("anchor 116-PM not found in blog.html")
    cards_block = "".join(make_blog_card(e) for e in all_entries)
    new_html = pattern.sub(lambda m: m.group(1) + cards_block, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes, added {len(all_entries)} cards")

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        sm = f.read()
    additions = []
    # 117 and 118 missing from sitemap too
    for num, slug, slot, title in [
        ("117", "make-vs-buy-bow-assembly-hand-tie-vs-pre-tied-in-house-vs-outsourced-ribbon-conversion", "am",
         "Ribbon OEM 117-Module Brand-Buyer Make-vs-Buy Bow-Assembly Architecture 2026"),
        ("118", "multi-tier-supplier-consolidation-vendor-base-rationalization-tier-1-tier-2-tier-3-ribbon-procurement", "pm",
         "Ribbon OEM 118-Module Brand-Buyer Multi-Tier Supplier-Consolidation Architecture 2026"),
    ]:
        filename = f"blog/blog-ribbon-oem-{num}-module-brand-buyer-{slug}-architecture-global-brand-procurement-2026-09-12-{slot}.html"
        loc = f"{SITE}/{filename}"
        if loc in sm:
            print(f"  sitemap: skip (already present) {loc}")
            continue
        addition = (
            f'  <url>\n'
            f'    <loc>{loc}</loc>\n'
            f'    <lastmod>{TODAY}</lastmod>\n'
            f'    <changefreq>monthly</changefreq>\n'
            f'    <priority>0.8</priority>\n'
            f'  </url>\n'
        )
        additions.append(addition)
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
        print(f"sitemap.xml: {len(sm):,} -> {len(new_sm):,} bytes, added {len(additions)} URLs")
    else:
        print("sitemap.xml: no additions needed")

def main():
    update_index()
    update_blog()
    update_sitemap()

if __name__ == "__main__":
    main()
