#!/usr/bin/env python3
"""Generate 2 B2B SEO articles for July 23, 2026 (AM + PM) for smithribbon.com
Article content is stored in _art1_sections.txt and _art2_sections.txt to avoid
huge inline strings.
"""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-07-23"
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
        "slug": "blog-ribbon-oem-certification-stack-decoder-global-brand-procurement-2026-07-23-am",
        "title": "Ribbon OEM Certification Stack Decoder 2026: 14-Cert Framework for Global Brand Procurement — OEKO-TEX, GRS, BSCI, SEDEX, SMETA, FSC, ISO 9001, ISO 14001, SA8000, WRAP, FSSC 22000, RCS, C2C, ZDHC, and How a 6.2M Meter Program Hits 100% Multi-Tier Retailer Compliance While Reducing Audit Fatigue by 64%",
        "description": "A 2026 B2B ribbon OEM certification stack decoder for global brand procurement directors, sustainability leads, and compliance officers. Covers the 14-cert framework (OEKO-TEX Standard 100, GRS, RCS, BSCI, SEDEX, SMETA, FSC, ISO 9001, ISO 14001, SA8000, WRAP, FSSC 22000, Cradle to Cradle, ZDHC), audit-fatigue reduction strategy, multi-tier retailer compliance mapping (Walmart, Target, IKEA, H&M, Inditex, L'Oreal, Sephora, Costco), 18-month recertification calendar, and shared audit data room architecture. Includes how Smith Ribbon supports brand buyers with a 14-cert unified stack, shared audit reports, and single-window compliance portal.",
        "keywords": "ribbon OEM certification, OEKO-TEX ribbon, GRS ribbon, BSCI SEDEX SMETA, FSC ribbon, ISO 9001 ribbon, ISO 14001, SA8000 ribbon, WRAP certification, FSSC 22000, RCS recycled, Cradle to Cradle, ribbon compliance, multi-tier retailer compliance, ribbon audit fatigue, Smith Ribbon certifications",
        "read_time": "21",
        "date_label": "July 23, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "Certification Stack &amp; Compliance",
        "tagline": "14-cert unified framework for global ribbon brand procurement compliance",
        "footer_blurb": "Managing multi-tier retailer ribbon compliance? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs a 14-cert unified stack with shared audit reports, single-window compliance portal, and 18-month recertification calendar — cutting audit fatigue by 64%.",
        "sections_source": "_art1_sections.txt",
    },
    {
        "slug": "blog-ribbon-oem-trusted-advisor-relationship-model-global-brand-procurement-2026-07-23-pm",
        "title": "Ribbon OEM Trusted Advisor Relationship Model 2026: From Transactional Vendor to Strategic Partner — 8-Tier Engagement Maturity, 4 Quarterly Cadence Touchpoints, 12 KPI Joint Scorecard, 6 Co-Investment Models, and How a 7.4M Meter Strategic Partnership Captures 28% Joint Margin Lift, 36% Innovation Pipeline Fill, and 96% Multi-Year Renewal",
        "description": "A 2026 B2B ribbon OEM trusted advisor relationship model for global brand procurement directors, vendor management leads, and strategic sourcing heads. Covers the 8-tier engagement maturity (transactional to preferred to strategic to trusted to co-developer to embedded to innovation partner to strategic alliance), 4 quarterly cadence touchpoints (QBR, innovation review, capacity planning, sustainability sync), 12 KPI joint scorecard, 6 co-investment models (tooling, R&D, capacity, sustainability, marketing, IP), and the 4 anti-patterns that destroy ribbon OEM trust. Includes how Smith Ribbon operates as a trusted advisor with 7.4M+ meter strategic partnerships, joint innovation roadmaps, and 5-year continuity contracts.",
        "keywords": "ribbon OEM trusted advisor, strategic ribbon supplier, ribbon vendor relationship, ribbon OEM partnership, ribbon procurement strategy, joint scorecard, QBR ribbon supplier, co-investment ribbon, innovation pipeline, strategic sourcing ribbon, Smith Ribbon strategic partner",
        "read_time": "22",
        "date_label": "July 23, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "Trusted Advisor Relationship Model",
        "tagline": "From transactional vendor to strategic partner — the 8-tier ribbon OEM relationship model",
        "footer_blurb": "Looking for a ribbon OEM trusted advisor — not just a transactional vendor? Xiamen Smith Ribbon &amp; Bow Co., Ltd. operates as a strategic partner with 7.4M+ meter joint programs, 12-KPI scorecards, 5-year continuity contracts, and 36% innovation pipeline fill.",
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
        card = f'''        <!-- {article["section"]} Article - July 23, 2026 ({article["datetime"][11:16]} UTC) -->
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
    print("=== Generating July 23, 2026 (AM + PM) B2B Articles for smithribbon.com ===")
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
