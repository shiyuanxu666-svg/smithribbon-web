#!/usr/bin/env python3
"""Generate 2 B2B SEO articles for July 24, 2026 (AM + PM) for smithribbon.com
Article content is stored in _art1_sections.txt and _art2_sections.txt to avoid
huge inline strings.
"""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-07-24"
DATE_AM = f"{DATE_ISO}T10:00:00Z"
DATE_PM = f"{DATE_ISO}T15:00:00Z"


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


ARTICLES = [
    {
        "slug": "blog-ribbon-oem-digital-twin-demand-sensing-7-layer-stack-global-brand-procurement-2026-07-24-am",
        "title": "Ribbon OEM Digital Twin Demand-Sensing 7-Layer Stack 2026: Probabilistic Forecasting, 4-Tier Scenario Library, Weekly Cadence Workflow, 13-Week Capacity Reservation, and How a 7.8M Meter Program Hits 99.4% Fill Rate While Cutting Inventory 38% and Expedite Freight 42%",
        "description": "A 2026 B2B ribbon OEM digital twin demand-sensing playbook for global brand procurement directors, demand planners, and supply chain VPs. Covers the 7-layer sensing stack (historical sales, buyer rolling forecast, POS / market signal, macro / seasonal, supply / capacity, event / promotion, geopolitical / disruption), 4-tier scenario library (P10 / P50 / P90 / P99), weekly cadence workflow (Mon data ingest, Tue exception triage, Wed brand-buyer sync, Fri report), 13-week capacity reservation, and the 90-day implementation roadmap. Includes how Smith Ribbon operates a 7-layer demand-sensing stack with 99.4% fill rate, 38% inventory reduction, and 42% expedite freight savings.",
        "keywords": "ribbon OEM demand sensing, digital twin ribbon, ribbon forecast accuracy, probabilistic ribbon demand, ribbon capacity reservation, 13-week ribbon forecast, ribbon scenario planning, ribbon fill rate, ribbon inventory turns, ribbon expedite freight, Smith Ribbon demand sensing",
        "read_time": "22",
        "date_label": "July 24, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "Digital Twin Demand-Sensing Stack",
        "tagline": "7-layer demand-sensing stack for global ribbon brand procurement capacity planning",
        "footer_blurb": "Looking to lift ribbon OEM fill rate to 99.4% while cutting inventory 38%? Xiamen Smith Ribbon &amp; Bow Co., Ltd. operates a 7-layer demand-sensing stack with probabilistic forecasting, 4-tier scenario library, and 13-week capacity reservation.",
        "sections_source": "_art1_sections.txt",
    },
    {
        "slug": "blog-ribbon-oem-sub-tier-subcontracting-transparency-4-tier-mapping-2026-07-24-pm",
        "title": "Ribbon OEM Sub-Tier Subcontracting Transparency 4-Tier Mapping 2026: 6-Field Disclosure Template, 5-Dimension Risk-Tier Scoring, Quarterly Refresh Cadence, Brand-Buyer On-Demand Portal, and How a 6.6M Meter Program Hits 100% Tier 1-2 Mapping While Eliminating Sub-Tier Opacity and CSRD Audit Findings",
        "description": "A 2026 B2B ribbon OEM sub-tier subcontracting transparency playbook for global brand procurement directors, compliance officers, and CSRD / UFLPA leads. Covers the 4-tier mapping framework (Tier 1 direct, Tier 2 material input, Tier 3 raw material, Tier 4 provenance), 6-field disclosure template (identity, capability, commercial, risk score, sub-tier, audit status), 5-dimension risk-tier scoring (country, process, opacity, cert gap, financial), quarterly refresh cadence, and the 6-month implementation roadmap. Includes how Smith Ribbon operates a 4-tier sub-tier transparency map with on-demand brand-buyer export and zero CSRD audit findings.",
        "keywords": "ribbon OEM sub-tier transparency, ribbon subcontractor mapping, ribbon CSRD compliance, ribbon UFLPA compliance, ribbon sub-tier risk scoring, ribbon supply chain map, ribbon forced labor, ribbon tier 4 provenance, ribbon brand-buyer disclosure, Smith Ribbon transparency",
        "read_time": "23",
        "date_label": "July 24, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "Sub-Tier Subcontracting Transparency",
        "tagline": "4-tier sub-tier subcontracting mapping for global ribbon brand procurement compliance",
        "footer_blurb": "Need a 4-tier ribbon OEM sub-tier transparency map for CSRD, UFLPA, and retailer compliance? Xiamen Smith Ribbon &amp; Bow Co., Ltd. operates a 4-tier map with 6-field disclosure, 5-dimension risk scoring, and quarterly refresh — 100% Tier 1-2 mapped, 0% CSRD findings.",
        "sections_source": "_art2_sections.txt",
    },
]


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
            "id": "{og_url}"
        }},
        "keywords": "{art["keywords"]}",
        "wordCount": {1600 + int(art["read_time"]) * 32},
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
            <p><strong>{art["footer_blurb"]}</strong> <a href="contact.html">Contact us today</a> for a custom quotation and compliance documentation package.</p>
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
        card = f'''        <!-- {article["section"]} Article - July 24, 2026 ({article["datetime"][11:16]} UTC) -->
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
                <a href="{article["slug"]}.html" class="insight-link">Read full guide →</a>
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
    print("=== Generating July 24, 2026 (AM + PM) B2B Articles for smithribbon.com ===")
    for art in ARTICLES:
        art["sections"] = load_sections(os.path.join(BASE, art["sections_source"]))
        path = os.path.join(BASE, f"{art['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_article(art))
        print(f"  [OK] Created: {art['slug']}.html")
        update_blog_html(art)
        print(f"  [OK] Updated: en-blog.html / blog.html ({art['section']})")
        update_index_html(art)
        print(f"  [OK] Updated: index.html ({art['section']})")
        update_sitemap(art)
        print(f"  [OK] Updated: sitemap.xml ({art['section']})")
    print("\nDone. 2 articles ready for git commit.")


if __name__ == "__main__":
    main()
