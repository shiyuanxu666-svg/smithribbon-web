"""Wire 2026-09-13 cron DOUBLE articles (122-AM, 123-PM) into index.html, blog.html, sitemap.xml.
Also wire the 121 article into blog.html (it was missing)."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"
TODAY = "2026-09-13"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-122-module-brand-buyer-agile-plan-replenishment-mts-mto-ato-hybrid-decoupling-point-architecture-global-brand-procurement-2026-09-13-am.html",
        "date": "2026-09-13 10:00 AM",
        "title": "Ribbon OEM 122-Module Brand-Buyer Agile-Plan Replenishment &amp; Make-to-Stock vs Make-to-Order MTO vs Assemble-to-Order ATO Hybrid Decoupling-Point Architecture 2026",
        "tag": "Brand-Buyer Agile-Plan Replenishment &amp; MTS/MTO/ATO Hybrid Decoupling-Point Architecture",
        "iso_date": "2026-09-13",
        "desc": "A 2026 B2B ribbon OEM 122-module brand-buyer agile-plan replenishment, MTS/MTO/ATO hybrid decoupling-point, demand-shock-absorber, VMI, postponed-final-finish, late-stage-customization, color-locking, lot-size-reduction, QR/SMED, Kanban, Heijunka, DBR/TOC architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers 11-agile-plan, 10-replenishment, 9-decoupling-point, 8-MTS, 7-MTO, 6-ATO, 5-hybrid, 4-VMI, 3-postponed-finish, 4-late-custom, 9-color-lock, 6-lot-reduction, 5-QR, 4-SMED, 6-mixed-model, 5-small-batch, 6-safety-stock, 5-service-level, 4-base-stock, 6-Kanban, 5-Heijunka, 4-DBR, 6-TOC modules. Delivers 92-98% 18-day-time-to-pilot-launch, 84-94% replenishment-fill-rate, 44-58% lead-time-collapsing-yield, 18-26% inventory-turn-lift, 102 brand partners, 56 EU-27 markets, 60 NA-states, 62 MEA-jurisdictions, 3,760 active SKUs on a 14.3M-meter annual multi-brand multi-jurisdiction brand-buyer agile-replenishment hybrid decoupling-point architecture program.",
        "short": "A 2026 B2B ribbon OEM 122-module brand-buyer agile-plan replenishment, MTS/MTO/ATO hybrid decoupling-point, demand-shock-absorber, VMI, postponed-final-finish, late-stage-customization, color-locking, lot-size-reduction, QR/SMED, Kanban, Heijunka, DBR/TOC architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers agile-plan cadence, replenishment trigger, decoupling-point position, MTS/MTO/ATO mix, VMI, color-lock, lot-reduction, QR/SMED changeover, Kanban, Heijunka, drum-buffer-rope and theory-of-constraints, and 18-day time-to-pilot-launch...",
        "mins": "40 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-123-module-brand-buyer-sustainability-packaging-epr-compliance-extended-producer-responsibility-drs-architecture-global-brand-procurement-2026-09-13-pm.html",
        "date": "2026-09-13 15:00 PM",
        "title": "Ribbon OEM 123-Module Brand-Buyer Sustainability-Packaging EPR-Compliance &amp; Extended-Producer-Responsibility DRS Architecture 2026",
        "tag": "Brand-Buyer Sustainability-Packaging EPR-Compliance &amp; Extended-Producer-Responsibility DRS Architecture",
        "iso_date": "2026-09-13",
        "desc": "A 2026 B2B ribbon OEM 123-module brand-buyer sustainability-packaging EPR-compliance, extended-producer-responsibility, deposit-return-scheme (DRS), PPWR, ESPR-DPP, EU-CBAM-style material-passport, fiber-circularity, mono-material-design, paperization, 3R, reverse-logistics, PCR/GRS, mass-balance, recycled-claim-substantiation, EPR-fee-modulation, eco-modulation, multi-jurisdiction regulatory architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers 12-EPR-policy, 11-DRS, 10-PPWR, 9-ESPR, 8-DPP, 7-EU-CBAM, 6-fiber-circular, 5-mono-material, 4-paperization, 9-3R, 6-reverse-log, 5-PCR, 4-GRS, 6-mass-balance, 5-recycled-claim, 4-EPR-fee, 6-eco-mod, 5-IOR, 7-cross-border, 6-NA-state, 5-AU-state, 4-CA-province, 6-multi-jurisdiction modules. Delivers 92-98% 24-day-time-to-pilot-launch, 84-94% EPR-fee-clean-record, 44-58% recycled-claim-pass-rate, 18-26% 3R-yield-lift, 105 brand partners, 58 EU-27 markets, 61 NA-states, 64 MEA-jurisdictions, 3,880 active SKUs on a 14.9M-meter annual multi-brand multi-jurisdiction brand-buyer sustainability-packaging EPR-compliance architecture program.",
        "short": "A 2026 B2B ribbon OEM 123-module brand-buyer sustainability-packaging EPR-compliance, extended-producer-responsibility, DRS, PPWR, ESPR-DPP, EU-CBAM-style material-passport, fiber-circularity, mono-material-design, paperization, 3R, reverse-logistics, PCR/GRS, mass-balance, recycled-claim-substantiation, EPR-fee-modulation, eco-modulation, multi-jurisdiction regulatory architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers EPR policy, DRS, PPWR, ESPR, DPP, EU-CBAM, fiber-circular, mono-material, paperization, 3R, reverse-logistics, PCR, GRS, mass-balance, recycled-claim, EPR-fee, eco-modulation, IOR, cross-border, NA-state, AU-state, CA-province, multi-jurisdiction, and 24-day time-to-pilot-launch...",
        "mins": "41 min read",
    },
]

# Also wire 121 into blog.html (it was missing)
LEGACY_121 = {
    "slot": "pm",
    "file": "blog/blog-ribbon-oem-121-module-brand-buyer-dual-sourcing-resiliency-china-plus-1-multi-country-ribbon-sourcing-risk-architecture-global-brand-procurement-2026-09-12-pm.html",
    "date": "2026-09-12 15:00 PM",
    "title": "Ribbon OEM 121-Module Brand-Buyer Dual-Sourcing Resiliency &amp; China+1 Multi-Country Ribbon-Sourcing Risk-Architecture 2026",
    "short": "A 2026 B2B ribbon OEM 121-module brand-buyer dual-sourcing resiliency, China+1 multi-country ribbon-sourcing, geographic risk-diversification, geopolitical-risk-shield, tariff-engineering, currency-hedging and multi-plant mill-qualification risk-architecture for global brand procurement, retail private-label directors, beauty and fashion merchandising leaders, holiday-gifting category sourcing heads, and OEM program management offices. Covers dual-sourcing strategy, China+1 mix, multi-country mill-qualification, geographic-risk tier, geopolitical-risk shield, tariff-engineering, currency-hedging, multi-plant bridge, lead-time resilience, quality parity, capacity parity, freight resilience, customs resilience, AEO/C-TPAT, multi-currency pay, trade-compliance, export-control, sanction-screening, modern-slavery, conflict-mineral, multi-country-ESG, multi-country-cert, multi-country-audit, multi-country-traceability, multi-country-blockchain, multi-country-mass-balance, multi-country-recycled-claim, multi-country-carbon, multi-country-circular and resilience-scorecard, and 18-day time-to-pilot-launch...",
}

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# Anchor: the 121-PM card end (most recent in index.html) - insert new cards RIGHT AFTER it.
ANCHOR_121_PM_END = (
    '<a href="blog-ribbon-oem-121-module-brand-buyer-dual-sourcing-resiliency-china-plus-1-multi-country-ribbon-sourcing-risk-architecture-global-brand-procurement-2026-09-12-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
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
    if ANCHOR_121_PM_END not in html:
        raise SystemExit("ANCHOR_121_PM_END not found in index.html")
    new_html = html.replace(ANCHOR_121_PM_END, ANCHOR_121_PM_END + cards_block, 1)
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
    # Anchor: 120-PM (most recent entry already in blog.html)
    anchor_120 = 'blog/blog-ribbon-oem-120-module-brand-buyer-quality-issue-8d-root-cause-supplier-recovery-capa-playbook-architecture-global-brand-procurement-2026-09-12-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_120) + r'"[^>]*>[^<]*</a>\s*</article>)',
        re.S
    )
    if not pattern.search(html):
        raise SystemExit("anchor 120-PM not found in blog.html")
    # Wire 121 (legacy missing) + 122 + 123
    all_entries = [LEGACY_121] + ENTRIES
    cards_block = "".join(make_blog_card(e) for e in all_entries)
    new_html = pattern.sub(lambda m: m.group(1) + cards_block, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes, added {len(all_entries)} cards (121+122+123)")

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
