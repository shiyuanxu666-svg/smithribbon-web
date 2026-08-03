#!/usr/bin/env python3
"""Generate AM + PM B2B articles for August 3, 2026 for smithribbon.com — doubled-up daily push."""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-08-03"
DATE_AM = f"{DATE_ISO}T10:00:00+08:00"
DATE_PM = f"{DATE_ISO}T15:00:00+08:00"

ARTICLES = [
    {
        "slot": "AM",
        "slug": "blog-ribbon-oem-16-module-digital-thread-mill-to-retail-traceability-architecture-global-brand-procurement-2026-08-03-am",
        "title": "Ribbon OEM 16-Module Digital Thread &amp; Mill-to-Retail Traceability Architecture 2026: 6-Traceability Data Layer, 8-Data-Capture Touchpoint, 9-Timeline-Stage Milestone, 5-Tier Sub-Supplier Map, 7-Cert Chain-of-Custody Stack, 6-Blockchain Anchor, 4-QR/Serialization Standard, 8-Audit Log Retention, 6-Role Access Stack, 5-API Integration, 7-Data Validation Rule, 9-Traceability KPI Dashboard, 4-Incident-Response, 5-End-Consumer Transparency, 6-Data-Governance Policy &amp; 3-Legacy-Migration Path for Global Brand Owners, Private-Label Compliance Officers &amp; Retail ESG Auditors",
        "description": "A 2026 B2B ribbon OEM 16-module digital thread &amp; mill-to-retail traceability architecture for global brand owners, private-label compliance officers, and retail ESG auditors. Covers the 6-traceability data layer (material, sub-component, production, finishing, packaging, distribution), 8-data-capture touchpoint (yarn receiving, dye house, weaving, printing, QC, packing, shipping, DC/retail), 9-timeline-stage milestone, 5-tier sub-supplier mapping, 7-certification chain-of-custody stack (GRS, RCS, FSC, OEKO-TEX, ZDHC, BCI, GOTS), 6-blockchain anchor layer, 4-QR/serialization standard, 8-audit log retention, 6-role-based access stack, 5-API integration pattern, 7-data validation rule, 9-traceability KPI dashboard, 4-incident-response workflow, 5-end-consumer transparency layer, 6-data-governance policy, and 3-legacy-migration path. Includes how Smith Ribbon operates a 16-module digital thread architecture to deliver 100% mill-to-shelf traceability, 4.2-hour incident response, 18-28% ESG-audit time savings, and 0% counterfeiting risk on a 9.4M meter multi-brand ribbon program.",
        "keywords": "ribbon OEM digital thread, ribbon OEM traceability, ribbon OEM mill to shelf, ribbon OEM EU DPP, ribbon OEM ESG, ribbon OEM GRS, ribbon OEM FSC, ribbon OEM blockchain, ribbon OEM QR traceability, ribbon OEM anti-counterfeit, ribbon OEM 2026 brand procurement, ribbon OEM scope 3, ribbon OEM CSRD, ribbon OEM audit log, ribbon OEM consumer transparency",
        "read_time": "26",
        "date_label": "August 3, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "Digital Thread &amp; Mill-to-Retail Traceability Architecture",
        "tagline": "Digital thread and mill-to-retail traceability architecture for global brand owners and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with a 16-module digital thread &amp; mill-to-retail traceability architecture, 6-traceability data layer, 8-data-capture touchpoint, 5-tier sub-supplier map, 7-cert chain-of-custody, 6-blockchain anchor, 4-QR standard, 9-KPI dashboard, and 3-migration path? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented mill-to-shelf traceability, EU DPP compliance, and 4.2-hour incident response on a 9.4M meter multi-brand ribbon program.",
        "sections_source": "_art1_sections_2026-08-03-am.txt",
    },
    {
        "slot": "PM",
        "slug": "blog-ribbon-oem-14-module-mill-side-carbon-water-scope-3-decarbonization-architecture-global-brand-procurement-2026-08-03-pm",
        "title": "Ribbon OEM 14-Module Mill-Side Carbon, Water &amp; Scope-3 Decarbonization Architecture 2026: 6-Emission-Scope Layer, 8-Carbon-Data Touchpoint, 9-Energy-Source-Mix Map, 5-Renewable Procurement Playbook, 7-Water-Stewardship Stack, 6-Waste-Circularity Layer, 8-Supplier-Engagement Program, 9-Decarbonization KPI Dashboard, 5-Science-Based-Target Alignment, 7-Carbon-Offset Hierarchy, 4-LCA Boundary, 6-Climate-Disclosure Format, 5-Third-Party-Verification Cadence &amp; 3-Net-Zero Roadmap Scenario for Global Brand Owners, Private-Label Sustainability Leads &amp; Retail Climate-Disclosure Officers",
        "description": "A 2026 B2B ribbon OEM 14-module mill-side carbon, water, and Scope-3 decarbonization architecture for global brand owners, private-label sustainability leads, and retail climate-disclosure officers. Covers the 6-emission-scope layer (Scope 1, Scope 2, Scope 3 Cat 1, Cat 4, Cat 9, Cat 12), 8-carbon-data-capture touchpoint, 9-energy-source-mix map, 5-renewable-energy procurement playbook, 7-water-stewardship stack, 6-waste-circularity layer, 8-supplier-engagement program, 9-decarbonization KPI dashboard, 5-Science-Based-Target alignment, 7-carbon-offset hierarchy, 4-life-cycle-assessment boundary, 6-climate-disclosure report format, 5-third-party-verification cadence, and 3-net-zero roadmap scenario. Includes how Smith Ribbon operates a 14-module mill-side decarbonization architecture to deliver 38% Scope 1+2 reduction, 22% Scope 3 reduction, 100% SBTi alignment, and 100% third-party verified carbon disclosure on an 11.6M meter multi-brand ribbon program.",
        "keywords": "ribbon OEM decarbonization, ribbon OEM Scope 3, ribbon OEM carbon, ribbon OEM CSRD, ribbon OEM IFRS S2, ribbon OEM SBTi, ribbon OEM net zero, ribbon OEM water stewardship, ribbon OEM circularity, ribbon OEM climate disclosure, ribbon OEM 2026 brand procurement, ribbon OEM renewable energy, ribbon OEM LCA, ribbon OEM supplier engagement, ribbon OEM waste circularity",
        "read_time": "25",
        "date_label": "August 3, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "Mill-Side Carbon, Water &amp; Scope-3 Decarbonization Architecture",
        "tagline": "Mill-side carbon, water, and Scope-3 decarbonization architecture for global brand owners and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with a 14-module mill-side carbon, water &amp; Scope-3 decarbonization architecture, 6-emission-scope layer, 8-carbon touchpoint, 9-energy-mix map, 5-renewable procurement, 7-water stack, 6-circularity layer, 8-supplier program, 9-KPI dashboard, 5-SBT alignment, 7-offset hierarchy, 4-LCA boundary, 6-disclosure format, 5-verification cadence, and 3-net-zero roadmap? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented 38% Scope 1+2 reduction, 22% Scope 3 reduction, 100% SBTi alignment on an 11.6M meter multi-brand ribbon program.",
        "sections_source": "_art2_sections_2026-08-03-pm.txt",
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
        card = f'''        <!-- {article["section"]} Article - August 3, 2026 ({article["datetime"][11:16]} UTC) -->
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
