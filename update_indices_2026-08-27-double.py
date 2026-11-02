"""Wire new 2026-08-27 articles (92-AM, 93-PM) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-92-module-brand-buyer-sustainability-procurement-roadmap-csrd-esg-disclosure-supplier-data-collection-architecture-global-brand-procurement-2026-08-27-am.html",
        "abs_file": "blog/blog-ribbon-oem-92-module-brand-buyer-sustainability-procurement-roadmap-csrd-esg-disclosure-supplier-data-collection-architecture-global-brand-procurement-2026-08-27-am.html",
        "date": "2026-08-27 10:00 AM",
        "title": "Ribbon OEM 92-Module Brand-Buyer Sustainability-Procurement-Roadmap CSRD ESG-Disclosure Supplier-Data-Collection Architecture 2026",
        "tag": "Brand-Buyer Sustainability-Procurement-Roadmap CSRD ESG-Disclosure Supplier-Data-Collection",
        "iso_date": "2026-08-27",
        "desc": "A 2026 B2B ribbon OEM 92-module brand-buyer sustainability-procurement-roadmap CSRD ESG-disclosure supplier-data-collection architecture for global brand owners, ESG-and-sustainability-VPs, chief-procurement-officers, and brand-supply-chain-compliance-leads. Covers 12-sustainability-procurement-cadre, 11-CSRD-disclosure-engine, 10-supplier-data-collection-pipeline, 9-ESG-cascade-stack, 8-supplier-emissions-engine, 7-sustainability-archive, 9-sustainability-dashboard, 6-sustainability-IP, 6-sustainability-cost &amp; 10-sustainability-continuous-improvement modules. Delivers 92-98% 25-day-time-to-CSRD-pilot-launch, 84-94% Scope-3-disclosure-completeness, 44-58% supplier-data-collection-cost-reduction, 18-26% ESG-audit-finding-reduction, 77 brand partners, 38 EU-27 markets, 43 NA-states, 45 MEA-jurisdictions, 2,700 active SKUs on a 9.8M-meter annual multi-brand multi-jurisdiction brand-buyer sustainability-procurement-roadmap CSRD ESG-disclosure supplier-data-collection program.",
        "short": "A 2026 B2B ribbon OEM 92-module brand-buyer sustainability-procurement-roadmap CSRD ESG-disclosure supplier-data-collection architecture for global brand owners, ESG-and-sustainability-VPs, chief-procurement-officers, and brand-supply-chain-compliance-leads. Covers sustainability procurement cadre, CSRD disclosure engine, supplier data collection pipeline, ESG cascade stack, supplier emissions engine, and 25-day time-to-CSRD-pilot-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-93-module-mill-side-rpet-recycling-loop-post-consumer-bottle-to-yarn-pellet-to-ribbon-finish-architecture-premium-brand-global-brand-procurement-2026-08-27-pm.html",
        "abs_file": "blog/blog-ribbon-oem-93-module-mill-side-rpet-recycling-loop-post-consumer-bottle-to-yarn-pellet-to-ribbon-finish-architecture-premium-brand-global-brand-procurement-2026-08-27-pm.html",
        "date": "2026-08-27 15:00 PM",
        "title": "Ribbon OEM 93-Module Mill-Side RPET Recycling-Loop Post-Consumer-Bottle-to-Yarn-Pellet-to-Ribbon-Finish Architecture Premium-Brand 2026",
        "tag": "Mill-Side RPET Recycling-Loop Post-Consumer-Bottle-to-Yarn-Pellet-to-Ribbon-Finish Architecture Premium-Brand",
        "iso_date": "2026-08-27",
        "desc": "A 2026 B2B ribbon OEM 93-module mill-side RPET recycling-loop post-consumer-bottle-to-yarn-pellet-to-ribbon-finish architecture for premium-brand owners, brand-circularity-VPs, ESG-and-circular-economy-directors, and brand-rPET-procurement-leads. Covers 12-RPET-recycling-cadre, 11-post-consumer-bottle-collection-engine, 10-yarn-pellet-extrusion-pipeline, 9-ribbon-finish-cascade-stack, 8-GRS-chain-of-custody-engine, 7-RPET-archive, 9-RPET-dashboard, 6-RPET-IP, 6-RPET-cost &amp; 10-RPET-continuous-improvement modules. Delivers 92-98% 23-day-time-to-RPET-pilot-launch, 84-94% GRS-chain-of-custody-completeness, 44-58% post-consumer-bottle-recovery-cost-reduction, 18-26% RPET-finish-defect-reduction, 78 brand partners, 39 EU-27 markets, 44 NA-states, 46 MEA-jurisdictions, 2,740 active SKUs on a 10.0M-meter annual multi-brand multi-jurisdiction mill-side RPET recycling-loop post-consumer-bottle-to-yarn-pellet-to-ribbon-finish architecture premium-brand program.",
        "short": "A 2026 B2B ribbon OEM 93-module mill-side RPET recycling-loop post-consumer-bottle-to-yarn-pellet-to-ribbon-finish architecture for premium-brand owners, brand-circularity-VPs, ESG-and-circular-economy-directors, and brand-rPET-procurement-leads. Covers RPET recycling cadre, post consumer bottle collection engine, yarn pellet extrusion pipeline, ribbon finish cascade stack, GRS chain of custody engine, and 23-day time-to-RPET-pilot-launch...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor: latest in index.html = 90-pm (since 91-pm3 is a separate file in blog/ but let's check)
# Find the 91-pm3 reference or fall back to 90-pm
anchor = '<a href="blog/blog-ribbon-oem-91-module-mill-side-digital-thread-yarn-polymerization-to-retail-till-traceability-architecture-premium-brand-global-brand-procurement-2026-08-26-pm3.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    # try 90-pm
    anchor = '<a href="blog/blog-ribbon-oem-90-module-mill-side-loom-maintenance-yarn-path-calibration-tension-profile-defect-prevention-architecture-premium-brand-global-brand-procurement-2026-08-26-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'
    if anchor not in html:
        # try 89-am
        anchor = '<a href="blog/blog-ribbon-oem-89-module-brand-buyer-supplier-scorecard-quarterly-business-review-vendor-lifecycle-qbr-cab-global-procurement-architecture-global-brand-procurement-2026-08-26-am.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'
        if anchor not in html:
            raise SystemExit("anchor not found in index.html")

pattern = re.escape(anchor) + r"\s*</div>"
for e in ENTRIES:
    card = f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    repl = anchor + "            </div>" + card
    new_html, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        new_html = html.replace(anchor, anchor + card, 1)
    html = new_html
    anchor = f'<a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: latest blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-91-module-mill-side-digital-thread-yarn-polymerization-to-retail-till-traceability-architecture-premium-brand-global-brand-procurement-2026-08-26-pm3.html">Ribbon OEM 91-Module Mill-Side Digital-Thread Yarn-Polymerization-to-Retail-Till Traceability-Architecture Premium-Brand 2026</a></h3>'

if anchor_blog not in blog:
    anchor_blog = '<h3><a href="blog/blog-ribbon-oem-90-module-mill-side-loom-maintenance-yarn-path-calibration-tension-profile-defect-prevention-architecture-premium-brand-global-brand-procurement-2026-08-26-pm.html">Ribbon OEM 90-Module Mill-Side Loom-Maintenance Yarn-Path Calibration Tension-Profile Defect-Prevention Architecture Premium-Brand 2026</a></h3>'
    if anchor_blog not in blog:
        anchor_blog = '<h3><a href="blog/blog-ribbon-oem-89-module-brand-buyer-supplier-scorecard-quarterly-business-review-vendor-lifecycle-qbr-cab-global-procurement-architecture-global-brand-procurement-2026-08-26-am.html">Ribbon OEM 89-Module Brand-Buyer Supplier-Scorecard Quarterly-Business-Review Vendor-Lifecycle QBR CAB Global Procurement Architecture 2026</a></h3>'
        if anchor_blog not in blog:
            raise SystemExit("anchor not found in blog.html")

# Find the FIRST occurrence (top of blog list)
idx = blog.index(anchor_blog)
end_article = blog.index("</article>", idx)
insert_pt = end_article + len("</article>")

cards_parts = []
for e in ENTRIES:
    cards_parts.append(f"""

        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">August 27, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-91-module-mill-side-digital-thread-yarn-polymerization-to-retail-till-traceability-architecture-premium-brand-global-brand-procurement-2026-08-26-pm3.html"

if anchor_url not in sm:
    anchor_url = "https://smithribbon.com/blog/blog-ribbon-oem-90-module-mill-side-loom-maintenance-yarn-path-calibration-tension-profile-defect-prevention-architecture-premium-brand-global-brand-procurement-2026-08-26-pm.html"
    if anchor_url not in sm:
        raise SystemExit("anchor not found in sitemap.xml")

sm_entries = []
for e in ENTRIES:
    sm_entries.append(f"""  <url>
    <loc>https://smithribbon.com/{e['abs_file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

idx = sm.index(anchor_url)
end_url = sm.index("</url>", idx) + len("</url>")
sm = sm[:end_url] + "\n" + "\n".join(sm_entries) + sm[end_url:]

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
