#!/usr/bin/env python3
"""Generate 2 B2B SEO articles for July 26, 2026 (AM + PM) for smithribbon.com
Article content is stored in _art1_sections_2026-07-26-am.txt and _art2_sections_2026-07-26-pm.txt
"""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-07-26"
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
        "slug": "blog-ribbon-oem-4-tier-sub-tier-mapping-subcontracting-transparency-global-brand-procurement-2026-07-26-am",
        "title": "Ribbon OEM 4-Tier Sub-Tier Subcontracting Mapping Playbook 2026: Tier 1 OEM Self-Audit, Tier 2 Yarn/Greige Supplier Disclosure, Tier 3 Dyestuff/Chemical Origin, Tier 4 Feedstock (Recycled PET, Cotton, FSC Paper), 9 Disqualifying Red Flags, Quarterly Refresh, Remediation Loop, and How Global Brand Procurement Hits UFLPA / EU CSDDD / LkSG Compliance Baseline",
        "description": "A 2026 B2B ribbon OEM 4-tier sub-tier mapping playbook for global brand procurement directors, supplier qualification leads, and compliance officers. Covers the 4 tiers (Tier 1 ribbon OEM, Tier 2 yarn / greige / sub-component supplier, Tier 3 dyestuff / chemical / auxiliary, Tier 4 raw material feedstock origin), 12 disclosure fields per tier, 9 disqualifying red flags, quarterly refresh cadence, semi-annual right-to-audit, 30-day remediation loop, and the ROI math (avoided-cost 8-25x). Includes how Smith Ribbon operates a 4-tier mapping program with documented disclosure, GRS / OEKO-TEX / FSC third-party certificates, and Intertek annual on-site verification — 96% multi-year renewal rate, 0 UFLPA / REACH enforcement actions across 14 years.",
        "keywords": "ribbon OEM 4-tier sub-tier mapping, ribbon subcontracting transparency, ribbon UFLPA compliance, ribbon EU CSDDD, ribbon LkSG, ribbon Tier 2 supplier disclosure, ribbon GRS scope certificate, ribbon OEKO-TEX chain of custody, ribbon sub-tier audit, Smith Ribbon 4-tier mapping",
        "read_time": "24",
        "date_label": "July 26, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "4-Tier Sub-Tier Mapping",
        "tagline": "4-tier sub-tier mapping playbook for ribbon OEM subcontracting transparency in 2026 global brand procurement",
        "footer_blurb": "Need a ribbon OEM with documented 4-tier sub-tier mapping for UFLPA / EU CSDDD / LkSG compliance? Xiamen Smith Ribbon &amp; Bow Co., Ltd. operates a quarterly-refreshed 4-tier program with GRS, OEKO-TEX, FSC third-party certificates and Intertek annual verification — 96% multi-year renewal rate, 0 enforcement actions in 14 years.",
        "sections_source": "_art1_sections_2026-07-26-am.txt",
    },
    {
        "slug": "blog-ribbon-oem-ai-vision-quality-inspection-defect-control-global-brand-procurement-2026-07-26-pm",
        "title": "Ribbon OEM AI Vision Quality Inspection Playbook 2026: 4 Inspection Stations (Substrate, Print, Color, Finishing), 11 Defect Classes per Station, 7-Day Validation Protocol, 30-Day Continuous-Learning Loop, 99.7% Lot Acceptance, 0.10% Escape Rate, and How Global Brand Procurement Hits 12-Month Defect Warranty",
        "description": "A 2026 B2B ribbon OEM AI vision quality inspection playbook for global brand procurement directors, supplier qualification leads, and quality managers. Covers the 4 inspection stations (substrate line-scan 99.2%, print area-scan 99.7%, color spectrophotometer ΔE ≤ 1.0, finishing 12MP robotic pick-and-place), 11 defect classes per station, the 7-day validation protocol, the 30-day continuous-learning loop, the ROI math (defect escape 1.8% to 0.10%, QC cost -75%, warranty exposure -$180K-$540K/yr), and how AI vision becomes a procurement requirement rather than a pilot. Includes how Smith Ribbon operates AI vision on 4 production lines with YOLOv8 / U-Net models, SGS semi-annual audit, and 12-month defect-rate warranty — 62% manual QC headcount reduction, 100% line coverage vs 12% sampling.",
        "keywords": "ribbon OEM AI vision inspection, ribbon machine vision defect detection, ribbon OEM 4 station inspection, ribbon vision quality control, ribbon YOLOv8 defect, ribbon U-Net segmentation, ribbon AQL alternative, ribbon line scan camera, ribbon vision validation, Smith Ribbon AI vision",
        "read_time": "24",
        "date_label": "July 26, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "AI Vision Quality Inspection",
        "tagline": "AI vision quality inspection playbook for ribbon OEM defect control in 2026 global brand procurement",
        "footer_blurb": "Need a ribbon OEM with production-grade AI vision quality inspection across substrate, print, color, and finishing? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs 4 vision stations with 7-day validation, 30-day continuous learning, and SGS semi-annual audit — defect escape rate 1.8% to 0.10%, 12-month defect warranty, 62% manual QC reduction.",
        "sections_source": "_art2_sections_2026-07-26-pm.txt",
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
        card = f'''        <!-- {article["section"]} Article - July 26, 2026 ({article["datetime"][11:16]} UTC) -->
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
    print("=== Generating July 26, 2026 (AM + PM) B2B Articles for smithribbon.com ===")
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
