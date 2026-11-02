#!/usr/bin/env python3
"""Generate PM2 B2B article for July 26, 2026 for smithribbon.com"""
import os
import re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-07-26"
DATE_PM2 = f"{DATE_ISO}T15:30:00Z"


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


ARTICLE = {
    "slug": "blog-ribbon-oem-90-day-brief-to-shelf-onboarding-playbook-global-brand-procurement-2026-07-26-pm2",
    "title": "Ribbon OEM 90-Day Brief-to-Shelf Onboarding Playbook 2026: 6 Macro-Stages (RFI, Sample, Pre-Production, Pilot, Mass-Production, Replenishment), 24 Sub-Stages, 8 Decision Gates, 11 KPIs, 9 Failure Modes, and How Global Brand Buyers Hit 96% Multi-Year Renewal",
    "description": "A 2026 B2B ribbon OEM 90-day brief-to-shelf onboarding playbook for global brand procurement directors, supplier qualification leads, and merchandising managers. Covers the 6 macro-stages (RFI & capability assessment 12 days, sample development 22 days, pre-production validation 20 days, pilot run 20 days, mass-production ramp 30 days, replenishment hand-off 5 days), 8 decision gates with documented sign-off, 11 KPI targets, 9 common failure modes, and the ROI math (6-month timeline compression worth $1.2M-$3.4M on a 1.2M-meter program, 8-18x cumulative 3-year ROI). Includes how Smith Ribbon runs a 90-day onboarding playbook with first shipment in 78-92 days, 11-KPI scorecard, and 96% 12-month renewal rate — vs 9-14 months for traditional fragmented onboarding.",
    "keywords": "ribbon OEM 90 day onboarding, ribbon brief to shelf, ribbon supplier qualification, ribbon OEM RFI, ribbon lab dip approval, ribbon pilot run, ribbon mass production ramp, ribbon replenishment program, ribbon multi-year supply, Smith Ribbon onboarding",
    "read_time": "24",
    "date_label": "July 26, 2026",
    "datetime": DATE_PM2,
    "section": "Afternoon 2",
    "category": "90-Day Onboarding Playbook",
    "tagline": "90-day brief-to-shelf ribbon OEM onboarding playbook for global brand procurement directors in 2026",
    "footer_blurb": "Need a ribbon OEM with documented 90-day brief-to-shelf onboarding discipline? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs 6 macro-stages with 8 decision gates, 11-KPI scorecard, and 96% 12-month renewal rate — first shipment in 78-92 calendar days, vs 9-14 months for traditional fragmented onboarding.",
    "sections_source": "_art1_sections_2026-07-26-pm2.txt",
}


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
            <p><strong>{art["footer_blurb"]}</strong> <a href="contact.html">Contact us today</a> for a custom quotation and 90-day onboarding playbook template.</p>
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
    print("=== Generating July 26, 2026 PM2 B2B Article for smithribbon.com ===")
    art = ARTICLE
    path = os.path.join(BASE, f"{art['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_article(art))
    print(f"  [OK] Created: {art['slug']}.html")
    update_blog_html(art)
    print(f"  [OK] Updated: en-blog.html / blog.html")
    update_index_html(art)
    print(f"  [OK] Updated: index.html")
    update_sitemap(art)
    print(f"  [OK] Updated: sitemap.xml")
    print("\nDone.")


if __name__ == "__main__":
    main()
