"""Wire new 2026-08-20 double-push articles (68-am, 69-pm) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog/blog-ribbon-oem-68-module-brand-buyer-on-demand-digital-showroom-live-configuration-customization-e-commerce-global-brand-procurement-2026-08-20-am.html",
        "abs_file": "blog/blog-ribbon-oem-68-module-brand-buyer-on-demand-digital-showroom-live-configuration-customization-e-commerce-global-brand-procurement-2026-08-20-am.html",
        "date": "2026-08-20 10:00 AM",
        "title": "Ribbon OEM 68-Module Brand-Buyer On-Demand Digital-Showroom &amp; Live-Configuration Customization E-Commerce Architecture 2026",
        "tag": "Brand-Buyer On-Demand Digital-Showroom &amp; Live-Configuration Customization E-Commerce",
        "iso_date": "2026-08-20",
        "desc": "A 2026 B2B ribbon OEM 68-module brand-buyer on-demand digital-showroom and live-configuration customization e-commerce architecture for global brand owners, e-commerce-directors, merchandising-VPs, and digital-procurement-leads. Covers 9-showroom-cadre, 8-live-configurator, 7-3D-render, 6-AR-preview, 5-EDI-PUNCHOUT, 8-approval-route, 6-cart-to-PO, 4-showroom-IP, 4-showroom-cost &amp; 5-showroom-continuous-improvement modules. Delivers 92-98% 14-day-time-to-showroom-launch, 84-94% live-configurator-accuracy, 44-58% e-commerce-cycle-savings, 18-26% conversion-uplift, 55 brand partners, 19 EU-27 markets, 27 NA-states, 25 MEA-jurisdictions, 1,920 active SKUs on a 6.0M-meter annual multi-brand multi-jurisdiction on-demand digital-showroom program.",
        "short": "A 2026 B2B ribbon OEM 68-module brand-buyer on-demand digital-showroom and live-configuration customization e-commerce architecture for global brand owners, e-commerce-directors, merchandising-VPs, and digital-procurement-leads. Covers showroom cadre, live configurator, 3D render, AR preview, EDI PUNCHOUT, and 14-day time-to-showroom-launch...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog/blog-ribbon-oem-69-module-multi-tier-sub-supplier-child-labor-forced-labor-risk-management-human-rights-due-diligence-global-brand-procurement-2026-08-20-pm.html",
        "abs_file": "blog/blog-ribbon-oem-69-module-multi-tier-sub-supplier-child-labor-forced-labor-risk-management-human-rights-due-diligence-global-brand-procurement-2026-08-20-pm.html",
        "date": "2026-08-20 15:00 PM",
        "title": "Ribbon OEM 69-Module Multi-Tier Sub-Supplier Child-Labor &amp; Forced-Labor Risk-Management Human-Rights Due-Diligence Architecture 2026",
        "tag": "Multi-Tier Sub-Supplier Child-Labor &amp; Forced-Labor Risk-Management Human-Rights Due-Diligence",
        "iso_date": "2026-08-20",
        "desc": "A 2026 B2B ribbon OEM 69-module multi-tier sub-supplier child-labor and forced-labor risk-management human-rights due-diligence architecture for global brand owners, compliance-directors, ESG-VPs, and human-rights-procurement-leads. Covers 9-sub-supplier-mapping, 8-child-labor-audit, 7-forced-labor-screen, 6-Xinjiang-risk-tier, 5-UFLPA-evidence, 8-supplier-correction, 6-tier-risk-score, 4-human-rights-IP, 4-human-rights-cost &amp; 5-human-rights-continuous-improvement modules. Delivers 92-98% 28-day-time-to-due-diligence-report, 84-94% sub-supplier-coverage, 44-58% forced-labor-risk-savings, 18-26% UFLPA-cleared-import-uplift, 56 brand partners, 20 EU-27 markets, 27 NA-states, 26 MEA-jurisdictions, 1,940 active SKUs on a 6.2M-meter annual multi-brand multi-jurisdiction human-rights due-diligence program.",
        "short": "A 2026 B2B ribbon OEM 69-module multi-tier sub-supplier child-labor and forced-labor risk-management human-rights due-diligence architecture for global brand owners, compliance-directors, ESG-VPs, and human-rights-procurement-leads. Covers sub-supplier mapping, child-labor audit, forced-labor screen, Xinjiang risk-tier, UFLPA evidence, and 28-day time-to-due-diligence-report...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor on the most recently wired (yesterday's 67-PM)
anchor = '<a href="blog/blog-ribbon-oem-67-module-brand-buyer-quarterly-vendor-business-review-qbr-multi-year-sla-performance-global-brand-procurement-2026-08-19-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor not in html:
    raise SystemExit("anchor 67-pm not found in index.html")

# Insert the new cards right after the anchor card
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
    # Next insertion should anchor on the just-added card
    anchor = f'<a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: yesterday's 67-PM blog-card heading
anchor_blog = '<h3><a href="blog/blog-ribbon-oem-67-module-brand-buyer-quarterly-vendor-business-review-qbr-multi-year-sla-performance-global-brand-procurement-2026-08-19-pm.html">Ribbon OEM 67-Module Brand-Buyer Quarterly Vendor Business-Review (QBR) &amp; Multi-Year SLA Performance Architecture 2026</a></h3>'

if anchor_blog not in blog:
    raise SystemExit("anchor 67-pm not found in blog.html")

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
            <div class="blog-meta">August 20, 2026 &middot; {e['mins']}</div>
        </article>""")
insertion = "".join(cards_parts)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

new_urls = ""
for e in ENTRIES:
    new_urls += f"""  <url>
    <loc>{SITE}/{e['file']}</loc>
    <lastmod>{e['iso_date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sm = sm.replace("</urlset>", new_urls + "</urlset>")
with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write(sm)
print("sitemap.xml updated")
print("DONE")
