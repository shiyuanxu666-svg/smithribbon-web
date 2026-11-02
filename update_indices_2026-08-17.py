"""Wire new 2026-08-17 articles into index.html, blog.html, sitemap.xml."""
import re, os, json
WEB = "/workspace/smithribbon-web"
SITE = "https://smithribbon.com"

# Slot data
ENTRIES = [
    {
        "slot": "am",
        "file": "blog-ribbon-oem-56-module-spec-sheet-techpack-translation-decoder-global-brand-procurement-2026-08-17-am.html",
        "date": "2026-08-17 10:00 AM",
        "title": "Ribbon OEM 56-Module Spec-Sheet &amp; Tech-Pack Translation-Decoder Architecture 2026",
        "tag": "Spec-Sheet &amp; Tech-Pack Translation-Decoder Architecture",
        "iso_date": "2026-08-17",
        "desc": "A 2026 B2B ribbon OEM 56-module spec-sheet and tech-pack cross-functional translation-decoder architecture for global brand owners, merchandising-directors, sourcing-managers, and private-label program directors. Covers 9-spec-ingest, 8-bilingual-translate, 7-color-callout-convert, 6-tolerance-translate, 5-mill-instruction-handoff, 7-cross-functional-loop, 6-document-archive, 4-spec-IP, 4-spec-cost &amp; 4-spec-CI modules. Delivers 92-98% 90-day-time-to-RFQ-response, 72-88% spec-decode-accuracy, 44-58% spec-roundtrip-cost-savings, 18-26% RFQ-conversion-uplift, 46 brand partners, 15 EU-27 markets, 23 NA-states, 19 MEA-jurisdictions, 1,820 active SKUs on a 4.1M-meter annual multi-brand multi-jurisdiction spec-decode program.",
        "short": "A 2026 B2B ribbon OEM 56-module spec-sheet and tech-pack cross-functional translation-decoder architecture for global brand owners, merchandising-directors, sourcing-managers, and private-label program directors. Covers bilingual spec-decode, tech-pack-to-mill-instruction handoff, color-callout conversion, tolerance-translation, and 90-day time-to-RFQ-response...",
        "mins": "38 min read",
    },
    {
        "slot": "pm",
        "file": "blog-ribbon-oem-57-module-adjacent-material-bundle-program-global-brand-procurement-2026-08-17-pm.html",
        "date": "2026-08-17 15:00 PM",
        "title": "Ribbon OEM 57-Module Adjacent-Material Sourcing &amp; Bundle-Program Architecture 2026",
        "tag": "Cross-Category Adjacent-Material Sourcing &amp; Bundle-Program Architecture",
        "iso_date": "2026-08-17",
        "desc": "A 2026 B2B ribbon OEM 57-module cross-category adjacent-material sourcing and bundle-program architecture for global brand owners, gifting-program-directors, seasonal-merchandising-managers, and private-label program directors. Covers 8-adjacent-source, 9-bundle-engineer, 7-multi-SKU-consolidate, 6-cross-category-cost-arbitrage, 5-bundle-shelf-handoff, 8-compliance, 6-bundle-logistics, 4-bundle-IP, 4-bundle-cost &amp; 5-bundle-CI modules. Delivers 92-98% 90-day-time-to-bundle-shelf, 78-92% bundle-cost-savings, 44-58% cross-category-margin-uplift, 18-26% bundle-conversion-uplift, 48 brand partners, 15 EU-27 markets, 24 NA-states, 20 MEA-jurisdictions, 1,820 active SKUs on a 4.4M-meter annual multi-brand multi-jurisdiction bundle-program program.",
        "short": "A 2026 B2B ribbon OEM 57-module cross-category adjacent-material sourcing and bundle-program architecture for global brand owners, gifting-program-directors, seasonal-merchandising-managers, and private-label program directors. Covers adjacent-tissue, tag-stock, box, jar, pouch, and twine bundle-engineering, multi-SKU consolidation, cross-category cost-arbitrage, and 90-day time-to-bundle-shelf...",
        "mins": "38 min read",
    },
]

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

# --- index.html ---
# Insert a new <div class="news-card"> right after the 2026-08-16 PM card.
# We use the 55-module card (line ~1703) as the anchor.
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Find anchor: the closing </div> after the 55-module link
anchor_55 = '<a href="blog-ribbon-oem-55-module-multi-year-supplier-lifecycle-contract-renewal-architecture-global-brand-procurement-2026-08-16-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>'

if anchor_55 not in html:
    raise SystemExit("anchor 55 not found in index.html")

for e in ENTRIES:
    card = f"""
            <div class="news-card">
                <div class="news-date">{e['date']}</div>
                <h3 class="en-content">{e['title']}</h3>
                <p class="en-content">{e['desc']}</p>
                <a href="{e['file']}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    insertion = anchor_55 + card
    # Replace only first occurrence (the 55-module card is the latest)
    # To avoid replacing the 55-module anchor for the PM card as well, we
    # anchor on the 55-module link + the </div> that closes its news-card.
    # The structure is: link\n </div>\n <div class="news-card">...
    # We'll insert after the 55-module's enclosing </div>.
    # The 55-module card's </div> is the one immediately after the link.
    pattern = re.escape(anchor_55) + r"\s*</div>"
    repl = anchor_55 + "            </div>" + card
    new_html, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        # fallback: insert right after anchor
        new_html = html.replace(anchor_55, anchor_55 + card, 1)
    html = new_html

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated")

# --- blog.html ---
with open(BLOG_HTML, "r", encoding="utf-8") as f:
    blog = f.read()

# Insert new <article class="blog-card"> right after the 55-module card.
# The 55-module card's closing pattern is:
#  </article>\n\n        <article class="blog-card">
# but we have a 53-module card after it. Insert AFTER the 55-module card
# (i.e., between 55-module </article> and the 53-module <article ...>).
anchor_55_blog = '<h3><a href="blog-ribbon-oem-55-module-multi-year-supplier-lifecycle-contract-renewal-architecture-global-brand-procurement-2026-08-16-pm.html">Ribbon OEM 55-Module Multi-Year Supplier Lifecycle &amp; Contract-Renewal Architecture 2026</a></h3>'

if anchor_55_blog not in blog:
    raise SystemExit("anchor 55 not found in blog.html")

# Find the end of the 55-module card (its </article>) and insert after it
# Locate the 55-module anchor and the next </article>
idx = blog.index(anchor_55_blog)
end_article = blog.index("</article>", idx)
insert_pt = end_article + len("</article>")

# Build cards in reverse so they appear in order
cards = []
for e in reversed(ENTRIES):
    card = f"""

        <article class="blog-card">
            <span class="blog-tag">{e['tag']}</span>
            <h3><a href="{e['file']}">{e['title']}</a></h3>
            <p>{e['short']}</p>
            <div class="blog-meta">August 17, 2026 &middot; {e['mins']}</div>
        </article>"""
    cards.append(card)

insertion = "".join(cards)
blog = blog[:insert_pt] + insertion + blog[insert_pt:]

with open(BLOG_HTML, "w", encoding="utf-8") as f:
    f.write(blog)
print("blog.html updated")

# --- sitemap.xml ---
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()

# Insert two <url> entries right before </urlset>
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
