#!/usr/bin/env python3
"""Generate 2026-08-07 AM + PM B2B articles for smithribbon.com."""
import os, re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-08-07"

ARTICLES = [
    {
        "label": "AM",
        "datetime": f"{DATE_ISO}T10:00:00+08:00",
        "slug": "blog-ribbon-oem-24-module-sku-rationalization-moq-optimization-playbook-global-brand-procurement-2026-08-07-am",
        "short_title": "Ribbon OEM 24-Module SKU Rationalization &amp; MOQ Optimization Playbook 2026",
        "category": "SKU Rationalization &amp; MOQ Optimization Playbook",
        "description": "A 2026 B2B ribbon OEM 24-module SKU rationalization &amp; MOQ optimization playbook for global brand owners, retail category buyers, and private-label program directors. Covers the 6-SKU-audit-framework, 7-portfolio-segmentation, 8-MOQ-engineering, 9-color-width-substrate consolidation, 8-finishing-print consolidation, 6-licensed-SKU governance, 7-seasonal-SKU calendar, 5-bespoke-private-label review, 8-supplier-capacity matching, 6-warehouse-inventory right-sizing, 5-deadstock recovery, 4-SKU-rationalization committee, 7-MOQ-tier optimization, 6-volume-commitment discount, 4-MOQ-relaxation-trade-off, 8-safety-stock rebalancing, 7-forecast-driven MOQ, 5-supplier-managed inventory, 6-make-to-stock vs make-to-order, 7-cost-down annual review, 6-margin-mix optimization, 5-substitution-engine, 4-SKU-retirement protocol, 6-portfolio-governance, and 3-IT-architecture modules. Includes how Smith Ribbon operates a 24-module SKU rationalization playbook on a 7.4M-meter multi-SKU program delivering 14-28% SKU reduction, 18-32% MOQ improvement, 22-36% working-capital release, 9-16% cost-down, and 96-100% on-shelf availability over 28 months.",
        "keywords": "ribbon OEM SKU rationalization, ribbon OEM MOQ optimization, ribbon OEM portfolio segmentation, ribbon OEM color consolidation, ribbon OEM width consolidation, ribbon OEM substrate consolidation, ribbon OEM finishing consolidation, ribbon OEM print consolidation, ribbon OEM licensed SKU governance, ribbon OEM seasonal SKU, ribbon OEM bespoke private label, ribbon OEM supplier capacity matching, ribbon OEM warehouse inventory, ribbon OEM deadstock recovery, ribbon OEM MOQ tier, ribbon OEM volume commitment, ribbon OEM safety stock, ribbon OEM forecast driven MOQ, ribbon OEM VMI, ribbon OEM make to stock, ribbon OEM cost down annual review, ribbon OEM margin mix, ribbon OEM substitution engine, ribbon OEM SKU retirement, ribbon OEM 2026 brand procurement",
        "read_time": "30",
        "date_label": "August 7, 2026",
        "footer_blurb": "Need a ribbon OEM with a 24-module SKU rationalization &amp; MOQ optimization playbook, 6-SKU-audit-framework, 7-portfolio-segmentation, 8-MOQ-engineering, 9-color-width-substrate consolidation, 8-finishing-print consolidation, 6-licensed-SKU governance, 7-seasonal-SKU calendar, 5-bespoke-private-label review, 8-supplier-capacity matching, 6-warehouse-inventory right-sizing, 5-deadstock recovery, 4-SKU-rationalization committee, 7-MOQ-tier optimization, 6-volume-commitment discount, 4-MOQ-relaxation-trade-off, 8-safety-stock rebalancing, 7-forecast-driven MOQ, 5-supplier-managed inventory, 6-make-to-stock vs make-to-order, 7-cost-down annual review, 6-margin-mix optimization, 5-substitution-engine, 4-SKU-retirement protocol, 6-portfolio-governance, and 3-IT-architecture? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented 14-28% SKU reduction, 18-32% MOQ improvement, 22-36% working-capital release, 9-16% cost-down, and 96-100% on-shelf availability over 28 months on a 7.4M-meter multi-SKU ribbon program.",
        "sections_file": os.path.join(BASE, "_art1_sections_2026-08-07-am.txt"),
        "module_n": "24",
        "time_label": "Morning",
        "time_short": "10:00",
    },
    {
        "label": "PM",
        "datetime": f"{DATE_ISO}T15:00:00+08:00",
        "slug": "blog-ribbon-oem-25-module-cross-border-ecommerce-fba-marketplace-compliance-architecture-global-brand-procurement-2026-08-07-pm",
        "short_title": "Ribbon OEM 25-Module Cross-Border E-Commerce FBA &amp; Marketplace Compliance Architecture 2026",
        "category": "Cross-Border E-Commerce FBA &amp; Marketplace Compliance Architecture",
        "description": "A 2026 B2B ribbon OEM 25-module cross-border e-commerce FBA &amp; marketplace compliance architecture for global brand owners, Amazon FBA sellers, TikTok-Shop operators, Tmall-Global flagship-store owners, Shopee-Lazada-Shopify sellers, and Etsy-eBay-Wayfair-Faire sellers. Covers the 6-marketplace-onboarding module, 7-listing-compliance workflow, 8-packaging-compliance stack, 9-labeling-and-barcode stack, 7-hazmat-and-product-safety stack, 6-EPR-extended-producer-responsibility, 8-Amazon-FBA-prep workflow, 7-TikTok-Shop-listing workflow, 6-Tmall-Global-flagship workflow, 7-Shopee-Lazada-Shopify workflow, 5-Etsy-eBay-Wayfair-Faire workflow, 4-multi-marketplace-PIM, 8-prohibited-items-and-restricted-SKU, 6-freight-and-3PL-routing, 5-customs-and-duty-paid, 7-returns-and-reverse-logistics, 6-marketplace-fee-and-margin, 4-promotion-and-seasonal, 7-customer-review-and-feedback, 6-counterfeit-and-grey-market, 5-recall-and-delist, 6-multi-currency-pricing, 7-tax-and-VAT-GST, 4-dispute-and-chargeback, 5-account-health KPI, and 3-architecture IT-integration modules. Includes how Smith Ribbon operates a 25-module cross-border architecture on a 7.4M-meter multi-marketplace program delivering 14-26% marketplace-revenue acceleration, 18-34% compliance-cost reduction, 0% marketplace-listing-rejection, 24-72 hour FBA-prep SLA, and 96-100% first-pass listing approval over 30 months.",
        "keywords": "ribbon OEM cross border ecommerce, ribbon OEM Amazon FBA, ribbon OEM TikTok Shop, ribbon OEM Tmall Global, ribbon OEM Shopee Lazada, ribbon OEM Shopify, ribbon OEM Etsy eBay, ribbon OEM Wayfair Faire, ribbon OEM marketplace compliance, ribbon OEM listing compliance, ribbon OEM packaging compliance, ribbon OEM labeling barcode, ribbon OEM GS1 FNSKU, ribbon OEM hazmat, ribbon OEM product safety, ribbon OEM EPR extended producer responsibility, ribbon OEM FBA prep, ribbon OEM prohibited items, ribbon OEM freight 3PL, ribbon OEM customs duty, ribbon OEM returns reverse logistics, ribbon OEM marketplace fee margin, ribbon OEM customer review, ribbon OEM counterfeit grey market, ribbon OEM multi currency pricing, ribbon OEM VAT GST, ribbon OEM account health, ribbon OEM 2026 brand procurement",
        "read_time": "32",
        "date_label": "August 7, 2026",
        "footer_blurb": "Need a ribbon OEM with a 25-module cross-border e-commerce FBA &amp; marketplace compliance architecture, 6-marketplace-onboarding, 7-listing-compliance, 8-packaging-compliance, 9-labeling-and-barcode, 7-hazmat-and-product-safety, 6-EPR-extended-producer-responsibility, 8-Amazon-FBA-prep, 7-TikTok-Shop-listing, 6-Tmall-Global-flagship, 7-Shopee-Lazada-Shopify, 5-Etsy-eBay-Wayfair-Faire, 4-multi-marketplace-PIM, 8-prohibited-items-and-restricted-SKU, 6-freight-and-3PL-routing, 5-customs-and-duty-paid, 7-returns-and-reverse-logistics, 6-marketplace-fee-and-margin, 4-promotion-and-seasonal, 7-customer-review-and-feedback, 6-counterfeit-and-grey-market, 5-recall-and-delist, 6-multi-currency-pricing, 7-tax-and-VAT-GST, 4-dispute-and-chargeback, 5-account-health KPI, and 3-architecture IT-integration? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented 14-26% marketplace-revenue acceleration, 18-34% compliance-cost reduction, 0% marketplace-listing-rejection, 24-72 hour FBA-prep SLA, and 96-100% first-pass listing approval over 30 months on a 7.4M-meter multi-marketplace ribbon program.",
        "sections_file": os.path.join(BASE, "_art2_sections_2026-08-07-pm.txt"),
        "module_n": "25",
        "time_label": "Afternoon",
        "time_short": "15:00",
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


def build_article(art, sections):
    sections_html = ""
    for h2, content in sections:
        sections_html += f'''
    <section class="post-section">
      <h2>{h2}</h2>
      <p>{content}</p>
    </section>
'''
    og_url = f"https://smithribbon.com/{art['slug']}.html"
    word_count = 1700 + int(art["read_time"]) * 32
    short_d = art["description"][:197] + "..."

    full_title = art["short_title"].replace("&amp;", "&amp;")

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{art["short_title"]}</title>
    <meta name="description" content="{short_d}">
    <meta name="keywords" content="{art["keywords"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{og_url}">
    <meta property="og:title" content="{art["short_title"]}">
    <meta property="og:description" content="{short_d}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{og_url}">
    <meta property="og:image" content="https://smithribbon.com/banner.png">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{art["datetime"]}">
    <meta property="article:section" content="{art["category"]}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{art["short_title"]}">
    <meta name="twitter:description" content="{short_d}">
    <link rel="stylesheet" href="styles.css">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{art["short_title"]}",
        "description": "{short_d}",
        "image": "https://smithribbon.com/banner.png",
        "datePublished": "{art["datetime"]}",
        "dateModified": "{art["datetime"]}",
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
        <h1>{art["short_title"]}</h1>

        <div class="blog-content">
<p>{art["description"]}</p>
{sections_html}
        </div>

        <footer class="post-footer">
            <p><strong>{art["footer_blurb"]}</strong> <a href="contact.html">Contact us today</a> for a custom quotation and the {art["module_n"]}-module architecture onboarding package.</p>
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
        card = f'''        <!-- {article["time_label"]} Article - {article["date_label"]} ({article["time_short"]} UTC) -->
        <article class="blog-card">
            <span class="blog-tag">{article["category"]}</span>
            <h3><a href="{article["slug"]}.html">{article["short_title"]}</a></h3>
            <p>{article["description"][:240]}...</p>
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
    for art_cfg in ARTICLES:
        print(f"=== Generating {art_cfg['date_label']} {art_cfg['label']} B2B Article for smithribbon.com (Module #{art_cfg['module_n']}) ===")
        sections = load_sections(art_cfg["sections_file"])
        art = {
            "slug": art_cfg["slug"],
            "full_title": art_cfg["short_title"],
            "short_title": art_cfg["short_title"],
            "category": art_cfg["category"],
            "description": art_cfg["description"],
            "keywords": art_cfg["keywords"],
            "read_time": art_cfg["read_time"],
            "date_label": art_cfg["date_label"],
            "datetime": art_cfg["datetime"],
            "footer_blurb": art_cfg["footer_blurb"],
            "module_n": art_cfg["module_n"],
            "time_label": art_cfg["time_label"],
            "time_short": art_cfg["time_short"],
        }
        path = os.path.join(BASE, f"{art['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_article(art, sections))
        print(f"  [OK] Created: {art['slug']}.html")

        update_blog_html(art)
        print("  [OK] Updated: en-blog.html, blog.html")

        update_sitemap(art)
        print("  [OK] Updated: sitemap.xml")

    print("\nDone.")


if __name__ == "__main__":
    main()
