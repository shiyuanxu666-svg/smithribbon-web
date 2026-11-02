"""Wire new 2026-08-17 double-push articles (58-am2, 59-pm2) into index.html, blog.html, sitemap.xml."""
import re, os
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

ENTRIES = [
    {
        "slot": "am",
        "file": "blog-ribbon-oem-58-module-custom-jacquard-woven-brand-identity-rapid-sampling-global-brand-procurement-2026-08-17-am2.html",
        "date": "2026-08-17 10:30 AM",
        "title": "Ribbon OEM 58-Module Custom Jacquard-Woven Brand-Identity Ribbon Development &amp; Rapid-Sampling Architecture 2026",
        "tag": "Custom Jacquard-Woven Brand-Identity Ribbon Development &amp; Rapid-Sampling Architecture",
        "iso_date": "2026-08-17",
        "desc": "A 2026 B2B ribbon OEM 58-module custom jacquard-woven brand-identity ribbon development and rapid-sampling architecture for global brand owners, design-directors, merchandising-VPs, and private-label program directors. Covers 9-brand-artwork-ingest, 8-weave-structure-select, 7-yarn-dye-plan, 6-warp-design-build, 5-loom-counter-sample, 8-jacquard-compliance, 6-sample-logistics, 4-weave-IP, 4-weave-cost &amp; 4-weave-CI modules. Delivers 92-98% 21-day-time-to-counter-sample, 78-92% jacquard-loom-yield, 44-58% weave-cost-savings, 18-26% brand-line-extension-uplift, 49 brand partners, 15 EU-27 markets, 25 NA-states, 21 MEA-jurisdictions, 1,820 active SKUs on a 4.7M-meter annual multi-brand multi-jurisdiction custom-jacquard program.",
        "short": "A 2026 B2B ribbon OEM 58-module custom jacquard-woven brand-identity ribbon development and rapid-sampling architecture for global brand owners, design-directors, merchandising-VPs, and private-label program directors. Covers jacquard-weave-structure selection, yarn-dye planning, logo-resolution warp-design, loom-sampling turnaround, and 21-day time-to-counter-sample...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog-ribbon-oem-59-module-multi-market-holiday-gifting-peak-capacity-pre-booking-cascade-production-global-brand-procurement-2026-08-17-pm2.html",
        "date": "2026-08-17 15:30 PM",
        "title": "Ribbon OEM 59-Module Multi-Market Holiday-Gifting Peak-Capacity Pre-Booking &amp; Cascade-Production Architecture 2026",
        "tag": "Multi-Market Holiday-Gifting Peak-Capacity Pre-Booking &amp; Cascade-Production Architecture",
        "iso_date": "2026-08-17",
        "desc": "A 2026 B2B ribbon OEM 59-module multi-market holiday-gifting peak-capacity pre-booking and cascade-production architecture for global brand owners, seasonal-merchandising-VPs, gifting-program-directors, and private-label program directors. Covers 9-holiday-calendar-map, 8-peak-capacity-pre-book, 7-cascade-production-plan, 6-market-overlap-balance, 5-peak-shelf-restock-handoff, 8-holiday-compliance, 6-peak-logistics, 4-holiday-IP, 4-holiday-cost &amp; 5-holiday-CI modules. Delivers 92-98% 14-day-time-to-peak-shelf-restock, 82-94% peak-capacity-fill-rate, 44-58% peak-cost-arbitrage, 18-26% holiday-conversion-uplift, 50 brand partners, 16 EU-27 markets, 25 NA-states, 22 MEA-jurisdictions, 1,820 active SKUs on a 5.0M-meter annual multi-brand multi-jurisdiction peak-capacity pre-booking program.",
        "short": "A 2026 B2B ribbon OEM 59-module multi-market holiday-gifting peak-capacity pre-booking and cascade-production architecture for global brand owners, seasonal-merchandising-VPs, gifting-program-directors, and private-label program directors. Covers 12-month holiday-cascade calendar, peak-capacity pre-booking, market-overlap risk-balancing, and 14-day time-to-peak-shelf-restock...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Anchor: the 57-module card (the most recent previously wired)
anchor_57 = '<a href="blog-ribbon-oem-57-module-adjacent-material-bundle-program-global-brand-procurement-2026-08-17-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor_57 not in html:
    raise SystemExit("anchor 57 not found in index.html")

# Insert the new cards right after the 57-module card
pattern = re.escape(anchor_57) + r"\s*</div>"
for e in ENTRIES:
    card = f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    repl = anchor_57 + "            </div>" + card
    new_html, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        new_html = html.replace(anchor_57, anchor_57 + card, 1)
    html = new_html
    # Next insertion should anchor on the just-added card
    anchor_57 = f'<a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Anchor: the 57-module blog-card heading
anchor_57_blog = '<h3><a href="blog-ribbon-oem-57-module-adjacent-material-bundle-program-global-brand-procurement-2026-08-17-pm.html">Ribbon OEM 57-Module Adjacent-Material Sourcing &amp; Bundle-Program Architecture 2026</a></h3>'

if anchor_57_blog not in blog:
    raise SystemExit("anchor 57 not found in blog.html")

# Find the end of the 57-module card (its </article>) and insert after it
idx = blog.index(anchor_57_blog)
end_article = blog.index("</article>", idx)
insert_pt = end_article + len("</article>")

# Build cards (in normal order; insert at one point)
cards_parts = []
for e in ENTRIES:
    cards_parts.append(f"""

        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">August 17, 2026 &middot; {e['mins']}</div>
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
