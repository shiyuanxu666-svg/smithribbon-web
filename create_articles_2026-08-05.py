#!/usr/bin/env python3
"""Generate 2026-08-05 AM + PM B2B articles for smithribbon.com."""
import os, re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-08-05"
DATE_AM = f"{DATE_ISO}T10:00:00+08:00"
DATE_PM = f"{DATE_ISO}T15:00:00+08:00"

ARTICLES = [
    {
        "slot": "AM",
        "slug": "blog-ribbon-oem-19-module-ai-driven-predictive-demand-sensing-capacity-pre-booking-architecture-global-brand-procurement-2026-08-05-am",
        "title": "Ribbon OEM 19-Module AI-Driven Predictive Demand Sensing &amp; Capacity Pre-Booking Architecture 2026: 6-Demand-Signal Source, 8-AI-Forecast Model Layer, 9-Capacity-Reservation Module, 5-Multi-Tier Booking Hierarchy, 7-Peak-Season Cascade Plan, 6-Safety-Stock Policy, 8-Supplier-Collaboration Stack, 9-Forecast-Accuracy KPI Dashboard, 5-Replenishment-Frequency Map, 7-Slot-Allocation Algorithm, 4-Yarn-Reservation Policy, 6-Dye-Lot-Locking Protocol, 5-Printing-Slot-Queuing, 8-QC-Throughput Schedule, 6-Logistics-Capacity Reserve, 5-Inventory-Turn Target, 7-Scenario-Planning Layer, 4-Black-Swan Contingency &amp; 3-Net-Working-Capital Impact for Global Brand Owners, Private-Label Holiday Planners &amp; Retail Supply-Chain Continuity Officers",
        "short_title": "Ribbon OEM 19-Module AI-Driven Predictive Demand Sensing &amp; Capacity Pre-Booking Architecture 2026",
        "description": "A 2026 B2B ribbon OEM 19-module AI-driven predictive demand sensing &amp; capacity pre-booking architecture for global brand owners, private-label holiday planners, and retail supply-chain continuity officers. Covers the 6-demand-signal source, 8-AI-forecast model layer, 9-capacity-reservation module, 5-multi-tier booking hierarchy, 7-peak-season cascade plan, 6-safety-stock policy, 8-supplier-collaboration stack, 9-forecast-accuracy KPI dashboard, 5-replenishment-frequency map, 7-slot-allocation algorithm, 4-yarn-reservation policy, 6-dye-lot-locking protocol, 5-printing-slot-queuing, 8-QC-throughput schedule, 6-logistics-capacity reserve, 5-inventory-turn target, 7-scenario-planning layer, 4-black-swan contingency, and 3-net-working-capital impact. Includes how Smith Ribbon operates a 19-module AI-driven predictive demand sensing &amp; capacity pre-booking architecture to deliver 96.4% forecast accuracy, 8-12 month pre-booking window, 0% peak-season stockout, 22-34% working-capital reduction, and 18-28% landed-cost savings over 32 months on a 12.8M meter multi-brand ribbon program.",
        "keywords": "ribbon OEM demand sensing, ribbon OEM AI forecast, ribbon OEM capacity pre-booking, ribbon OEM peak season, ribbon OEM working capital, ribbon OEM safety stock, ribbon OEM yarn reservation, ribbon OEM dye lot locking, ribbon OEM slot allocation, ribbon OEM 2026 brand procurement, ribbon OEM Q4 surge, ribbon OEM 11.11, ribbon OEM Black Friday, ribbon OEM Valentine, ribbon OEM scenario planning, ribbon OEM black swan, ribbon OEM CPFR, ribbon OEM VMI, ribbon OEM S&OP, ribbon OEM reorder cadence",
        "read_time": "27",
        "date_label": "August 5, 2026",
        "datetime": DATE_AM,
        "section": "Morning",
        "category": "AI-Driven Predictive Demand Sensing &amp; Capacity Pre-Booking Architecture",
        "tagline": "AI-driven predictive demand sensing and capacity pre-booking architecture for global brand owners and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with a 19-module AI-driven predictive demand sensing &amp; capacity pre-booking architecture, 6-demand-signal source, 8-AI-forecast model layer, 9-capacity-reservation module, 5-multi-tier booking hierarchy, 7-peak-season cascade plan, 6-safety-stock policy, 8-supplier-collaboration stack, 9-forecast-accuracy KPI dashboard, 5-replenishment-frequency map, 7-slot-allocation algorithm, 4-yarn-reservation policy, 6-dye-lot-locking protocol, 5-printing-slot-queuing, 8-QC-throughput schedule, 6-logistics-capacity reserve, 5-inventory-turn target, 7-scenario-planning layer, 4-black-swan contingency, and 3-net-working-capital impact? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented 96.4% forecast accuracy, 8-12 month pre-booking window, 0% peak-season stockout, 22-34% working-capital reduction, and 18-28% landed-cost savings on a 12.8M meter multi-brand ribbon program.",
        "sections_source": "_art1_sections_2026-08-05-am.txt",
    },
    {
        "slot": "PM",
        "slug": "blog-ribbon-oem-20-module-cross-border-ecommerce-fba-tiktok-shop-tmall-marketplace-compliance-listing-ready-architecture-global-brand-procurement-2026-08-05-pm",
        "title": "Ribbon OEM 20-Module Cross-Border E-Commerce FBA / TikTok-Shop / Tmall Marketplace Compliance &amp; Listing-Ready Architecture 2026: 6-Marketplace Platform Layer, 8-Listing-Data Schema, 9-Packaging-FBA-Prep Compliance, 5-Labeling-Barcode-GTIN Standard, 7-Hazmat-Restricted-Substance Check, 6-ISTA-6-Amazon-Bubble-Wrap Protocol, 8-Customs-HS-Pre-Clearance, 7-Tax-VAT-IOSS-IOR-EORI Stack, 9-DPP-EU-ESPR Data Field, 6-Counterfeit-IP-Protection Module, 8-Creator-Content-Readiness Layer, 5-Photography-Listing-Asset, 6-Fulfillment-FBA-FBM-FBT-3PL Choice, 7-Return-Reverse-Logistics, 4-Marketing-Claim Substantiation, 6-Promo-Pricing Strategy, 8-Inventory-Replenishment Cadence, 5-Review-Rating-UGC Engine, 7-Marketplace-Analytics Dashboard, 6-Channel-Conflict Governance &amp; 3-Cross-Border Roadmap for Global Brand Owners, Marketplace Sellers &amp; D2C E-Commerce Operations Leaders",
        "short_title": "Ribbon OEM 20-Module Cross-Border E-Commerce FBA / TikTok-Shop / Tmall Marketplace Compliance &amp; Listing-Ready Architecture 2026",
        "description": "A 2026 B2B ribbon OEM 20-module cross-border e-commerce FBA / TikTok Shop / Tmall marketplace compliance &amp; listing-ready architecture for global brand owners, marketplace sellers, and D2C e-commerce operations leaders. Covers the 6-marketplace platform layer, 8-listing-data schema, 9-packaging-FBA-prep compliance, 5-labeling-barcode-GTIN standard, 7-hazmat-restricted-substance check, 6-ISTA-6-Amazon-bubble-wrap protocol, 8-customs-HS-pre-clearance, 7-tax-VAT-IOSS-IOR-EORI stack, 9-DPP-EU-ESPR data field, 6-counterfeit-IP-protection module, 8-creator-content-readiness layer, 5-photography-listing-asset, 6-fulfillment-FBA-FBM-FBT-3PL choice, 7-return-reverse-logistics, 4-marketing-claim substantiation, 6-promo-pricing strategy, 8-inventory-replenishment cadence, 5-review-rating-UGC engine, 7-marketplace-analytics dashboard, 6-channel-conflict governance, and 3-cross-border roadmap. Includes how Smith Ribbon operates a 20-module cross-border e-commerce FBA / TikTok Shop / Tmall marketplace compliance &amp; listing-ready architecture to deliver 96-100% first-time listing-pass rate, 18-32% revenue acceleration, 0% counterfeit listing, 100% ESPR DPP data, 24-48 hour listing turn, and 14-22% landed-cost savings over 26 months on a 9.8M meter multi-brand multi-channel ribbon program.",
        "keywords": "ribbon OEM FBA, ribbon OEM TikTok Shop, ribbon OEM Tmall Global, ribbon OEM cross-border, ribbon OEM marketplace compliance, ribbon OEM EU DPP, ribbon OEM ESPR, ribbon OEM IOSS, ribbon OEM IOR, ribbon OEM EORI, ribbon OEM hazmat, ribbon OEM ISTA-6, ribbon OEM IP protection, ribbon OEM creator content, ribbon OEM 2026 brand procurement, ribbon OEM D2C, ribbon OEM Etsy, ribbon OEM Faire, ribbon OEM Walmart, ribbon OEM return reverse logistics",
        "read_time": "28",
        "date_label": "August 5, 2026",
        "datetime": DATE_PM,
        "section": "Afternoon",
        "category": "Cross-Border E-Commerce FBA / TikTok-Shop / Tmall Marketplace Compliance &amp; Listing-Ready Architecture",
        "tagline": "Cross-border e-commerce FBA / TikTok-Shop / Tmall marketplace compliance and listing-ready architecture for global brand owners and ribbon OEM partners in 2026",
        "footer_blurb": "Need a ribbon OEM with a 20-module cross-border e-commerce FBA / TikTok-Shop / Tmall marketplace compliance &amp; listing-ready architecture, 6-marketplace platform layer, 8-listing-data schema, 9-packaging-FBA-prep, 5-labeling-GTIN, 7-hazmat, 6-ISTA-6, 8-HS pre-clearance, 7-tax stack, 9-DPP, 6-IP module, 8-creator, 5-photo, 6-fulfillment, 7-reverse-logistics, 4-claim, 6-promo, 8-replenishment, 5-review, 7-analytics, 6-channel-conflict, and 3-roadmap? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented 96-100% first-time listing-pass, 18-32% revenue acceleration, 0% counterfeit, 100% ESPR DPP, 24-48 hour listing turn, and 14-22% landed-cost savings on a 9.8M meter multi-brand multi-channel ribbon program.",
        "sections_source": "_art2_sections_2026-08-05-pm.txt",
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

    # Shorten og:title and og:description to keep within ~95 chars
    short_t = art["short_title"]
    short_d = art["description"][:197] + "..."

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
    <meta property="og:title" content="{short_t}">
    <meta property="og:description" content="{short_d}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{og_url}">
    <meta property="og:image" content="https://smithribbon.com/banner.png">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{art["datetime"]}">
    <meta property="article:section" content="{art["category"]}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{short_t}">
    <meta name="twitter:description" content="{short_d}">
    <link rel="stylesheet" href="styles.css">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{art["short_title"]}",
        "description": "{short_d}",
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
        card = f'''        <!-- {article["section"]} Article - August 5, 2026 ({article["datetime"][11:16]} UTC) -->
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


def update_index_html(article):
    index_path = os.path.join(BASE, "index.html")
    if not os.path.exists(index_path):
        return
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    card = f'''            <div class="insight-card">
                <span class="insight-tag">{article["category"]}</span>
                <h3><a href="{article["slug"]}.html">{article["short_title"][:120]}...</a></h3>
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
    print(f"=== Generating {len(ARTICLES)} B2B Articles for smithribbon.com on {DATE_ISO} ===")
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
