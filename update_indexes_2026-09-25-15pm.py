#!/usr/bin/env python3
"""Update smithribbon index.html, blog.html, en-blog.html, sitemap.xml with articles 171 + 172."""
import os, re

WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
TODAY = "September 25, 2026 (PM)"
ISO = "2026-09-25T15:00:00+08:00"

FILE_171 = "blog/blog-ribbon-oem-171-module-brand-buyer-mill-side-smart-specimen-co-design-portal-ai-visual-library-color-stewardship-pantone-fhi-translation-engine-architecture-global-brand-procurement-2026-09-25-am.html"
TITLE_171 = "Mill-Side Smart-Specimen Co-Design Portal — AI Visual Library, Color-Stewardship & Pantone-FHI Translation-Engine Architecture 2026"
DESC_171 = "B2B ribbon OEM 171-module mill-side smart-specimen co-design portal architecture. AI visual library curation, color-stewardship cadence, Pantone-FHI translation-engine, substrate-aware delta-E prediction."
SHORT_171 = "Mill-side smart-specimen co-design portal for ribbon OEM — 9-stage workflow, AI visual library 14k-19k records, Pantone-FHI translation-engine, substrate-aware delta-E prediction."

FILE_172 = "blog/blog-ribbon-oem-172-module-brand-buyer-mill-side-sustainability-narrative-csr-esg-disclosure-mill-to-shelf-architecture-global-brand-procurement-2026-09-25-pm.html"
TITLE_172 = "Mill-Side Sustainability Narrative — CSR/ESG Disclosure Mill-to-Shelf Architecture for Ribbon Brands 2026"
DESC_172 = "B2B ribbon OEM 172-module mill-side sustainability-narrative CSR-ESG-disclosure mill-to-shelf architecture. GRS-RPET provenance, FSC-paper traceability, recycled-claim substantiation, anti-greenwashing workflow, retailer-tender verification."
SHORT_172 = "Mill-side sustainability-narrative CSR-ESG-disclosure mill-to-shelf architecture for ribbon OEM — GRS-RPET 6-tier provenance, FSC-paper traceability, recycled-claim substantiation, anti-greenwashing, retailer-tender verification."


def make_index_card(e):
    return (
        '\n            <div class="news-card">\n'
        f'                <div class="news-date">{e["date"]}</div>\n'
        f'                <h3 class="en-content">{e["title"]}</h3>\n'
        f'                <p class="en-content">{e["desc"]}</p>\n'
        f'                <a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
        '            </div>'
    )


def make_blog_card(e):
    return (
        '\n<article class="post-card">\n'
        f'  <div class="post-meta">{e["date"]} &middot; 26 min read</div>\n'
        f'  <h3 class="post-title"><a href="{e["file"]}">{e["title"]}</a></h3>\n'
        f'  <p class="post-excerpt">{e["desc"]}</p>\n'
        f'  <a href="{e["file"]}" class="read-more">Read More &rarr;</a>\n'
        '</article>\n'
    )


def make_en_blog_card(e):
    return (
        f'<article class="blog-card">\n'
        f'  <div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,#2c3e50);">📰</div>\n'
        f'  <div class="blog-card-content">\n'
        f'    <h3><a href="{e["file"]}">{e["title"]}</a></h3>\n'
        f'    <div class="blog-card-meta">📅 {e["date"]} · ⏱ 26 min read</div>\n'
        f'    <p>{e["desc"]}</p>\n'
        f'    <a href="{e["file"]}" class="read-more">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


ENTRIES = [
    {"file": FILE_171, "title": TITLE_171, "desc": DESC_171, "short": SHORT_171, "date": "September 25, 2026 (AM)", "iso_date": "2026-09-25T08:00:00+08:00"},
    {"file": FILE_172, "title": TITLE_172, "desc": DESC_172, "short": SHORT_172, "date": "September 25, 2026 (PM)", "iso_date": "2026-09-25T15:00:00+08:00"},
]

# Insert after 170 anchor in index.html
INDEX_HTML = os.path.join(WEB, "index.html")
ANCHOR_170 = "blog/blog-ribbon-oem-170-module-brand-buyer-mill-side-supplier-qualification-onboarding-playbook-audit-capability-architecture-global-brand-procurement-2026-09-25-pm.html"

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()
if FILE_171 in html and FILE_172 in html:
    print(f"index.html: 171 + 172 already inserted — skipping")
else:
    if ANCHOR_170 not in html:
        print(f"index.html: ANCHOR_170 not found; falling back to anchor 168")
        ANCHOR_170 = ANCHOR_170
    idx = html.find(f'href="{ANCHOR_170}"')
    if idx < 0:
        print(f"index.html: anchor not found")
    else:
        close_idx = html.find('</div>', idx)
        insertion_point = close_idx + len('</div>')
        cards = "".join(make_index_card(e) for e in ENTRIES)
        new_html = html[:insertion_point] + cards + html[insertion_point:]
        with open(INDEX_HTML, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"index.html: updated with 171 + 172 ({len(html):,} -> {len(new_html):,} bytes)")


# Update blog.html and en-blog.html
for html_file, card_maker in [
    (os.path.join(WEB, "blog.html"), make_blog_card),
    (os.path.join(WEB, "en-blog.html"), make_en_blog_card),
]:
    if not os.path.exists(html_file):
        print(f"{html_file}: not found")
        continue
    with open(html_file, encoding="utf-8") as f:
        html = f.read()
    if FILE_172 in html:
        print(f"{html_file}: 172 already in HTML — skipping")
        continue
    # Find first article entry and insert before it
    pattern = re.compile(r'(<article\s+class="[^"]*card[^"]*"\s*>)', re.IGNORECASE)
    matches = list(pattern.finditer(html))
    if matches:
        first = matches[0]
        cards = "".join(card_maker(e) for e in ENTRIES)
        new_html = html[:first.start()] + cards + html[first.start():]
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"{html_file}: updated with 171 + 172 ({len(html):,} -> {len(new_html):,} bytes)")
    else:
        # Fallback: append before </main>
        if "</main>" in html:
            cards = "".join(card_maker(e) for e in ENTRIES)
            new_html = html.replace("</main>", cards + "</main>")
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(new_html)
            print(f"{html_file}: appended before </main>")


# Update sitemap.xml
SITEMAP = os.path.join(WEB, "sitemap.xml")
if not os.path.exists(SITEMAP):
    print(f"{SITEMAP}: not found")
else:
    with open(SITEMAP, encoding="utf-8") as f:
        xml = f.read()
    new_xml = xml
    for e in ENTRIES:
        url_full = f"{SITE_URL}/{e['file']}"
        if url_full in new_xml:
            print(f"{e['file']} already in sitemap.xml — skipping")
            continue
        block = (
            "  <url>\n"
            f"    <loc>{url_full}</loc>\n"
            f"    <lastmod>2026-09-25</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.85</priority>\n"
            "  </url>\n"
        )
        new_xml = new_xml.replace("</urlset>", block + "</urlset>")
        print(f"sitemap.xml: appended {e['file']}")
    if new_xml != xml:
        with open(SITEMAP, "w", encoding="utf-8") as f:
            f.write(new_xml)
        print(f"sitemap.xml: total {len(xml):,} -> {len(new_xml):,} bytes")
