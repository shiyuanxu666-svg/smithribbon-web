#!/usr/bin/env python3
"""Generate 2026-08-06 AM B2B article for smithribbon.com — 22-Module Mill-to-Shelf Material Provenance & Full-Stack Traceability Architecture."""
import os, re

BASE = "/workspace/smithribbon-web"
DATE_ISO = "2026-08-06"
DATE_AM = f"{DATE_ISO}T10:00:00+08:00"
SLUG = "blog-ribbon-oem-22-module-mill-to-shelf-material-provenance-full-stack-traceability-architecture-global-brand-procurement-2026-08-06-am"
SHORT_TITLE = "Ribbon OEM 22-Module Mill-to-Shelf Material Provenance &amp; Full-Stack Traceability Architecture 2026"
CATEGORY = "Mill-to-Shelf Material Provenance &amp; Full-Stack Traceability Architecture"
DESCRIPTION = "A 2026 B2B ribbon OEM 22-module mill-to-shelf material provenance &amp; full-stack traceability architecture for global brand owners, retail category buyers, and private-label program directors. Covers the 6-tier material genealogy, 7-fiber-origin verification, 8-yarn-spinner traceability, 6-dye-house chemical ledger, 7-weaving-mill provenance, 5-finishing-mill disclosure, 9-trim-component sub-tier map, 6-packaging-component traceability, 7-warehouse-3PL chain-of-custody, 4-cross-dock-handling, 8-incoming-quality traceability, 5-conformance-test-report stack, 7-social-compliance-credential vault, 4-environmental-permit register, 6-carbon-scope-3 model, 8-water-effluent disclosure, 5-RPET-recycled-content ledger, 6-FSC-paper-packaging chain, 6-customer-handover dossier, 4-audit-recall readiness, 4-third-party-verification engine, and 3-architecture IT-integration. Includes how Smith Ribbon operates a 22-module mill-to-shelf material provenance architecture on a 7.4M-meter multi-material program delivering 100% mill-to-shelf chain-of-custody, 0% audit-finding, 14-26% lower Scope-3 disclosure effort, 18-32% faster customs clearance, and 96-100% first-pass conformance over 26 months."
KEYWORDS = "ribbon OEM material provenance, ribbon OEM mill-to-shelf traceability, ribbon OEM fiber origin, ribbon OEM yarn spinner, ribbon OEM dye house chemical, ribbon OEM weaving mill, ribbon OEM finishing mill, ribbon OEM trim component, ribbon OEM packaging component, ribbon OEM warehouse 3PL, ribbon OEM cross-dock, ribbon OEM IQC traceability, ribbon OEM test report, ribbon OEM social compliance, ribbon OEM environmental permit, ribbon OEM carbon scope 3, ribbon OEM water effluent, ribbon OEM RPET GRS, ribbon OEM FSC paper, ribbon OEM 2026 brand procurement, ribbon OEM customer dossier, ribbon OEM audit recall, ribbon OEM third party verification, ribbon OEM IT integration"
READ_TIME = "28"
DATE_LABEL = "August 6, 2026"
FOOTER_BLURB = "Need a ribbon OEM with a 22-module mill-to-shelf material provenance &amp; full-stack traceability architecture, 6-tier material genealogy, 7-fiber-origin verification, 8-yarn-spinner traceability, 6-dye-house chemical ledger, 7-weaving-mill provenance, 5-finishing-mill disclosure, 9-trim-component sub-tier map, 6-packaging-component traceability, 7-warehouse-3PL chain-of-custody, 4-cross-dock-handling, 8-incoming-quality traceability, 5-conformance-test-report stack, 7-social-compliance-credential vault, 4-environmental-permit register, 6-carbon-scope-3 model, 8-water-effluent disclosure, 5-RPET-recycled-content ledger, 6-FSC-paper-packaging chain, 6-customer-handover dossier, 4-audit-recall readiness, 4-third-party-verification engine, and 3-architecture IT-integration? Xiamen Smith Ribbon &amp; Bow Co., Ltd. runs documented 100% mill-to-shelf chain-of-custody, 0% audit-finding, 14-26% lower Scope-3 disclosure effort, 18-32% faster customs clearance, and 96-100% first-pass conformance over 26 months on a 7.4M-meter multi-material ribbon program."

SECTIONS_FILE = "/workspace/smithribbon-web/_art1_sections_2026-08-06-am.txt"


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
        <h1>{art["full_title"]}</h1>

        <div class="blog-content">
<p>{art["description"]}</p>
{sections_html}
        </div>

        <footer class="post-footer">
            <p><strong>{art["footer_blurb"]}</strong> <a href="contact.html">Contact us today</a> for a custom quotation and the mill-to-shelf material provenance architecture onboarding package.</p>
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
        card = f'''        <!-- Morning Article - August 6, 2026 (10:00 UTC) -->
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


def update_index_html(article):
    index_path = os.path.join(BASE, "index.html")
    if not os.path.exists(index_path):
        return
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Add link rel=alternate or similar — skip for safety; just no-op


def main():
    print("=== Generating August 6, 2026 AM B2B Article for smithribbon.com (Module #22 — Mill-to-Shelf Material Provenance & Full-Stack Traceability) ===")
    sections = load_sections(SECTIONS_FILE)
    art = {
        "slug": SLUG,
        "full_title": "Ribbon OEM 22-Module Mill-to-Shelf Material Provenance &amp; Full-Stack Traceability Architecture 2026: 6-Tier Material Genealogy, 7-Fiber-Origin Verification, 8-Yarn-Spinner Traceability, 6-Dye-House Chemical Ledger, 7-Weaving-Mill Provenance, 5-Finishing-Mill Disclosure, 9-Trim-Component Sub-Tier Map, 6-Packaging-Component Traceability, 7-Warehouse-3PL Chain-of-Custody, 4-Cross-Dock Handling, 8-Incoming-Quality Traceability, 5-Conformance-Test-Report Stack, 7-Social-Compliance Credential Vault, 4-Environmental-Permit Register, 6-Carbon-Scope-3 Model, 8-Water-Effluent Disclosure, 5-RPET-Recycled-Content Ledger, 6-FSC-Paper-Packaging Chain, 6-Customer-Handover Dossier, 4-Audit-Recall Readiness, 4-Third-Party-Verification Engine &amp; 3-Architecture IT-Integration for Global Brand Owners, Retail Category Buyers &amp; Private-Label Program Directors",
        "short_title": SHORT_TITLE,
        "category": CATEGORY,
        "description": DESCRIPTION,
        "keywords": KEYWORDS,
        "read_time": READ_TIME,
        "date_label": DATE_LABEL,
        "datetime": DATE_AM,
        "footer_blurb": FOOTER_BLURB,
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
