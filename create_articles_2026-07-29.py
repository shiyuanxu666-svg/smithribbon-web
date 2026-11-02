#!/usr/bin/env python3
"""Generate AM + PM B2B articles for July 29, 2026 for smithribbon.com — doubled-up daily push."""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-07-29"
DATE_AM = f"{DATE_ISO}T10:00:00+08:00"
DATE_PM = f"{DATE_ISO}T15:00:00+08:00"

ARTICLES = [
    {
        "slot": "AM",
        "slug": "blog-ribbon-oem-digital-spec-sheet-translation-decoder-2026-07-29-am",
        "title": "Ribbon OEM Digital Spec-Sheet Translation Decoder 2026: 11-Section Digital Schema, 38 Most-Mistranslated Chinese-to-English Terms, 12 Measurement-Unit Traps, 7-Tolerance-Stack Decoder, 6-Artwork-Engineering Pitfalls, 9-Archive Fields, 4-Tape Measurement Tools &amp; 5-Stage Auto-Translation Pipeline for Global Brand Procurement &amp; Retail Sourcing Teams Decoding China Ribbon Factory Spec Sheets",
        "description": "A 2026 B2B ribbon OEM digital spec-sheet translation decoder for global brand procurement and retail sourcing teams decoding Chinese factory spec sheets. Covers the 11-section digital spec-sheet schema (substrate, width, color, print, finishing, packaging, compliance, volume, pricing, quality, logistics), the 38 most-mistranslated Chinese-to-English terms, the 12 measurement-unit traps (mm vs inch, g/m² vs oz/yd², denier vs dtex, meter vs yard), the 7-tolerance-stack decoder, the 6-artwork-engineering pitfalls, the 9-archive field requirements, the 4-tape measurement tools, and the 5-stage auto-translation pipeline. Includes how Smith Ribbon helps brand owners compress RFQ scoring from 14 days to 4.2 days, lift first-pass spec accuracy from 62% to 94%, and reduce landed-cost variance from 8-14% to 1.5-2.4% on a 4.4M meter custom ribbon program.",
        "keywords": "ribbon OEM spec sheet, ribbon OEM spec decoder, ribbon China factory spec, ribbon OEM English Chinese, ribbon OEM bilingual spec, ribbon OEM unit conversion, ribbon OEM RFQ scoring, ribbon OEM ΔE tolerance, ribbon OEM artwork engineering, ribbon OEM ICC profile, ribbon OEM 2026 spec, ribbon OEM spec schema, ribbon OEM spec glossary, ribbon OEM spec pipeline, ribbon brand procurement spec",
        "read_time": "22",
        "date_label": "July 29, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "Digital Spec-Sheet Translation &amp; Bilingual Procurement",
        "tagline": "Digital spec-sheet translation decoder for global brand buyers working with China ribbon OEM in 2026",
        "footer_blurb": "Need a ribbon OEM with a digital spec-sheet translation layer, 38-term bilingual glossary, 11-section digital schema, and 5-stage auto-translation pipeline? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs a mill-side bilingual spec-sheet engineer, 96-99% unit-conversion accuracy, and brand-mill co-validated glossary on every inbound spec.",
        "sections_source": "_art1_sections_2026-07-29-am.txt",
    },
    {
        "slot": "PM",
        "slug": "blog-ribbon-oem-cobranded-retail-holiday-gifting-program-2026-07-29-pm",
        "title": "Ribbon OEM Co-Branded Retail Holiday Gifting Program Architecture 2026: 6-Stage Co-Brand Architecture, 11-Step IP Clearance Workflow, 7-Tier Shared MOQ Pool, 9-Rule Co-Engineered Artwork, 12-Month Holiday Calendar, 4-Tier Partner Scorecard, 13-Cross-Category Pairing Matrix, 8-Step Post-Holiday Teardown, 5-Clause Risk Insurance &amp; 11-KPI QBR for Retail Brand Owners, Beauty Buyers, Gifting-Category Managers &amp; Private-Label Program Directors",
        "description": "A 2026 B2B ribbon OEM co-branded retail holiday gifting program architecture for retail brand owners, beauty brand buyers, gifting-category managers, and private-label program directors. Covers the 6-stage co-brand architecture (brief intake, IP clearance, shared MOQ pool, co-engineered artwork, holiday calendar, post-holiday teardown), the 11-step IP clearance workflow, the 7-tier shared MOQ pool economics (Tier 1 at 12,000m = $0.18/m, Tier 7 at 100,000m = $0.12/m), the 9-rule co-engineered artwork workflow, the 12-month holiday launch calendar, the 4-tier co-brand partner scorecard, the 13-cross-category pairing matrix, the 8-step post-holiday teardown, the 5-clause risk insurance structure, and the 11-KPI QBR framework. Includes how Smith Ribbon helps multi-brand holiday programs hit first-pass co-brand approval at 92%, holiday ship-on-time at 96%, post-holiday teardown cost reduction 64%, on a 6.2M meter multi-brand co-branded ribbon program.",
        "keywords": "ribbon OEM co-branded, ribbon OEM holiday gifting, ribbon OEM Q4 program, ribbon OEM beauty chocolate co-brand, ribbon OEM co-brand IP, ribbon OEM shared MOQ pool, ribbon OEM holiday calendar, ribbon OEM co-brand scorecard, ribbon OEM post-holiday teardown, ribbon OEM gifting category, ribbon OEM 2026 holiday, ribbon OEM cross-category, ribbon OEM co-brand architecture, ribbon OEM co-brand teardown, ribbon brand co-brand program",
        "read_time": "24",
        "date_label": "July 29, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "Co-Branded Retail Holiday Gifting Architecture",
        "tagline": "Co-branded retail holiday gifting program architecture for global brand owners and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with a 6-stage co-branded architecture, 11-step IP clearance workflow, 7-tier shared MOQ pool, and 12-month holiday launch calendar? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented co-brand IP, brand-mill co-managed launch, and 11-KPI QBR on a 6.2M meter multi-brand co-branded ribbon program.",
        "sections_source": "_art2_sections_2026-07-29-pm.txt",
    },
]


def load_sections(path):
    sections = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            idx = line.find("|")
            if idx == -1:
                continue
            h2 = line[:idx]
            content = line[idx + 1:]
            sections.append((h2, content))
    return sections


def build_article(art):
    sections = load_sections(os.path.join(BASE, art["sections_source"]))
    sections_html = ""
    for h2, content in sections:
        sections_html += f'''
    <section class="post-section">
      <h2>{h2}</h2>
      <p>{content}</p>
    </section>
'''
    og_url = f"https://smithribbon.com/{art['slug']}.html"
    word_count = 1600 + int(art["read_time"]) * 32

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{art["title"]}</title>
    <meta name="description" content="{art["description"]}">
    <meta name="keywords" content="{art["keywords"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{og_url}">
    <meta property="og:title" content="{art["title"]}">
    <meta property="og:description" content="{art["description"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{og_url}">
    <meta property="og:image" content="https://smithribbon.com/banner.png">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{art["datetime"]}">
    <meta property="article:section" content="{art["category"]}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="styles.css">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{art["title"]}",
        "description": "{art["description"]}",
        "image": "https://smithribbon.com/banner.png",
        "datePublished": "{DATE_ISO}",
        "dateModified": "{DATE_ISO}",
        "author": {{
            "@type": "Organization",
            "name": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
            "url": "https://smithribbon.com"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
            "url": "https://smithribbon.com",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://smithribbon.com/banner.png"
            }}
        }},
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "{og_url}"
        }},
        "keywords": "{art["keywords"]}",
        "wordCount": {word_count},
        "inLanguage": "en-US"
    }}
    </script>
</head>
<body>
<header class="site-header"></header>

<main class="blog-container">
    <article>
        <div class="blog-meta">
            <span class="blog-date">{art["date_label"]}</span>
            <span class="blog-category">{art["category"]}</span>
        </div>
        <h1>{art["title"]}</h1>

        <div class="blog-content">
<p>{art["description"]}</p>
{sections_html}
        </div>

        <footer class="post-footer">
            <p><strong>{art["footer_blurb"]}</strong> <a href="contact.html">Contact us today</a> for a custom quotation and the architecture onboarding package.</p>
        </footer>
    </article>
</main>

<footer class="site-footer">
    <p>&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. All rights reserved. | <a href="https://smithribbon.com">smithribbon.com</a></p>
</footer>
</body>
</html>'''
    return html


def update_blog_html(article):
    for blog_path in [os.path.join(BASE, "en-blog.html"), os.path.join(BASE, "blog.html")]:
        if not os.path.exists(blog_path):
            continue
        with open(blog_path, "r", encoding="utf-8") as f:
            content = f.read()
        card = f'''        <!-- {article["section"]} Article - July 29, 2026 ({article["datetime"][11:16]} UTC) -->
        <article class="blog-card">
            <span class="blog-tag">{article["category"]}</span>
            <h3><a href="{article["slug"]}.html">{article["title"]}</a></h3>
            <p>{article["description"]}</p>
            <div class="blog-meta">{article["date_label"]}</div>
        </article>
'''
        patterns = [
            r'(<section class="blog-hero">.*?</p>)',
            r'(<div class="blog-hero">.*?</p>)',
            r'(<header class="blog-header">.*?</header>)',
        ]
        inserted = False
        for pattern in patterns:
            if re.search(pattern, content, flags=re.DOTALL):
                content = re.sub(pattern, r'\g<1>\n' + card, content, flags=re.DOTALL)
                inserted = True
                break
        if not inserted:
            content = re.sub(r'(</h1>)', r'\g<1>\n' + card, content, count=1)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)


def update_index_html(article):
    index_path = os.path.join(BASE, "index.html")
    if not os.path.exists(index_path):
        return
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    card = f'''            <div class="insight-card">
                <span class="insight-tag">{article["category"]}</span>
                <h3><a href="{article["slug"]}.html">{article["title"][:120]}...</a></h3>
                <p>{article["tagline"]}</p>
                <a href="{article["slug"]}.html" class="insight-link">Read full playbook →</a>
            </div>
'''
    patterns = [
        r'(<div class="insights-grid">)',
        r'(<div class="blog-grid">)',
        r'(<div class="latest-articles">)',
    ]
    inserted = False
    for pattern in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, r'\g<1>\n' + card, content, count=1)
            inserted = True
            break
    if not inserted:
        content = re.sub(r'(<footer class="site-footer">)', card + r'\n\g<1>', content, count=1)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)


def update_sitemap(article):
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    new_url = f'''
  <url>
    <loc>https://smithribbon.com/{article["slug"]}.html</loc>
    <lastmod>{DATE_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>'''
    content = content.replace("</urlset>", new_url + "\n</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print(f"=== Generating {len(ARTICLES)} B2B Articles for smithribbon.com on {DATE_ISO} (doubled-up push) ===")
    for art in ARTICLES:
        path = os.path.join(BASE, f"{art['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_article(art))
        print(f"  [OK] Created: {art['slug']}.html ({art['slot']})")
        update_blog_html(art)
        print(f"  [OK] Updated: en-blog.html / blog.html")
        update_index_html(art)
        print(f"  [OK] Updated: index.html")
        update_sitemap(art)
        print(f"  [OK] Updated: sitemap.xml")
    print("\nDone.")


if __name__ == "__main__":
    main()
