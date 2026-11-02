#!/usr/bin/env python3
"""Generate AM + PM B2B articles for August 2, 2026 for smithribbon.com — doubled-up daily push."""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-08-02"
DATE_AM = f"{DATE_ISO}T10:00:00+08:00"
DATE_PM = f"{DATE_ISO}T15:00:00+08:00"

ARTICLES = [
    {
        "slot": "AM",
        "slug": "blog-ribbon-oem-12-module-brand-owned-tooling-asset-custody-architecture-global-brand-procurement-2026-08-02-am",
        "title": "Ribbon OEM 12-Module Brand-Owned Tooling &amp; Asset Custody Architecture 2026: 8-Asset Class Catalog, 11-Custody Contract Clause, 9-Ownership Transfer Workflow, 7-Storage Condition Standard, 6-Tooling Lifecycle Stage, 5-Multi-Mill Transfer Playbook, 4-IP Protection Clause, 8-Tooling Audit Cadence, 6-Tooling Maintenance Schedule, 9-Custody KPI Dashboard, 4-Tooling Insurance Stack &amp; 3-Asset Disposition Rule for Global Brand Owners, Private-Label Program Directors &amp; Retail Sourcing Leaders",
        "description": "A 2026 B2B ribbon OEM 12-module brand-owned tooling &amp; asset custody architecture for global brand owners, private-label program directors, and retail sourcing leaders. Covers the 8-asset class catalog (cylinders, jacquard cards, color masters, dies, hot-stamp dies, fixtures, packaging, color-management hardware), the 11-custody contract clause, the 9-ownership transfer workflow, the 7-storage condition standard, the 6-tooling lifecycle stage, the 5-multi-mill transfer playbook, the 4-IP protection clause, the 8-tooling audit cadence, the 6-tooling maintenance schedule, the 9-custody KPI dashboard, the 4-tooling insurance stack, and the 3-asset disposition rule. Includes how Smith Ribbon operates a 12-module brand-owned tooling &amp; asset custody architecture to deliver 14-22 days transfer time savings, 0% tool-loss over 36 months, 4-9% landed-cost variance reduction, and 100% IP control on a 7.8M meter multi-brand ribbon program.",
        "keywords": "ribbon OEM tooling, ribbon OEM asset custody, ribbon OEM brand-owned tooling, ribbon OEM cylinder, ribbon OEM jacquard card, ribbon OEM multi-mill transfer, ribbon OEM IP protection, ribbon OEM tooling insurance, ribbon OEM tooling maintenance, ribbon OEM tooling audit, ribbon OEM brand IP control, ribbon OEM 2026 brand procurement, ribbon OEM tooling custody, ribbon OEM color master, ribbon OEM die asset",
        "read_time": "24",
        "date_label": "August 2, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "Brand-Owned Tooling &amp; Asset Custody Architecture",
        "tagline": "Brand-owned tooling &amp; asset custody architecture for global brand owners and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with a 12-module brand-owned tooling &amp; asset custody architecture, 8-asset class catalog, 11-custody contract clause, 9-ownership transfer workflow, and 9-custody KPI dashboard? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented brand-side ownership, multi-mill transfer rights, and 4-policy insurance stack on every brand-owned tooling set.",
        "sections_source": "_art1_sections_2026-08-02-am.txt",
    },
    {
        "slot": "PM",
        "slug": "blog-ribbon-oem-11-module-incoming-quality-inspection-first-article-approval-architecture-global-brand-procurement-2026-08-02-pm",
        "title": "Ribbon OEM 11-Module Incoming Quality Inspection &amp; First-Article Approval Architecture 2026: 9-Stage Incoming Inspection Workflow, 7-Tool Inspection Kit, 12-Defect Classification Library, 8-AQL Sampling Plan, 5-Stage First-Article Approval Workflow, 6-Measurement KPI Stack, 4-Photo Documentation Standard, 7-Failure-Mode Corrective Action Playbook, 11-Supplier Scorecard Weight, 6-Monthly Audit Cadence &amp; 3-Disposition Rule for Global Brand Procurement, Retail Sourcing QA &amp; Private-Label Compliance Teams",
        "description": "A 2026 B2B ribbon OEM 11-module incoming quality inspection (IQC) and first-article approval (FAA) architecture for global brand procurement, retail sourcing QA, and private-label compliance teams. Covers the 9-stage incoming inspection workflow (pre-arrival doc review, container receiving, pallet sampling, visual, dimensional, color, functional, documentation reconciliation, disposition), the 7-tool inspection kit (caliper, ruler, spectrophotometer, light booth, scale, rub tester, microscope), the 12-defect classification library, the 8-AQL sampling plan, the 5-stage first-article approval workflow, the 6-measurement KPI stack, the 4-photo documentation standard, the 7-failure-mode corrective action playbook, the 11-supplier scorecard weight, the 6-monthly audit cadence, and the 3-disposition rule for failed lots. Includes how Smith Ribbon operates an 11-module IQC-FAA architecture to deliver 96.4% first-pass acceptance, 0.42% defect rate, 100% audit pass, and 98% holiday ship-on-time on a 6.7M meter multi-brand ribbon program.",
        "keywords": "ribbon OEM IQC, ribbon OEM FAA, ribbon OEM first-article approval, ribbon OEM AQL, ribbon OEM defect library, ribbon OEM CAPA, ribbon OEM scorecard, ribbon OEM supplier quality, ribbon OEM incoming inspection, ribbon OEM photo documentation, ribbon OEM 2026 brand procurement, ribbon OEM QA audit, ribbon OEM retail compliance, ribbon OEM holiday QA, ribbon OEM private label QA",
        "read_time": "23",
        "date_label": "August 2, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "Incoming Quality Inspection &amp; First-Article Approval Architecture",
        "tagline": "Incoming quality inspection and first-article approval architecture for global brand buyers and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with an 11-module IQC-FAA architecture, 9-stage incoming workflow, 7-tool inspection kit, 12-defect classification library, 8-AQL plan, 5-stage FAA, 6-KPI stack, 4-photo documentation standard, 7-CAPA playbook, 11-supplier scorecard, 6-monthly audit, and 3-disposition rule? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented IQC-FAA with mill-side and DC-side stations on a 6.7M meter multi-brand ribbon program.",
        "sections_source": "_art2_sections_2026-08-02-pm.txt",
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
        card = f'''        <!-- {article["section"]} Article - August 2, 2026 ({article["datetime"][11:16]} UTC) -->
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
