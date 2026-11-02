#!/usr/bin/env python3
"""Update blog.html, index.html, sitemap.xml for M157 (AM) and M158 (PM) on 2026-09-21.
Idempotent: skips already-present entries.
"""
import os, re, sys

BASE = "/workspace/smithribbon-web"

AM_ID = 157
AM_FILE = "blog/blog-ribbon-oem-157-module-brand-buyer-mill-side-ribbon-yarn-count-tensile-stress-strain-elongation-creep-recovery-oem-specification-architecture-global-brand-procurement-2026-09-21-am.html"
AM_TITLE_SHORT = "Ribbon Yarn-Count Tensile Stress-Strain &amp; Elongation Creep-Recovery OEM Specification Architecture for Premium Brand Programs 2026"
AM_DESC = ("A 2026 B2B ribbon OEM 157-module brand-buyer mill-side ribbon-yarn-count tensile stress-strain elongation creep-recovery OEM-specification architecture "
           "for global brand procurement directors, brand-private-label-merchandising-directors, brand-textile-engineers, brand-product-development-managers, "
           "brand-OEM-relationship-leads, and OEM mill-side QC-testing-supervisors. Covers 10-tensile-strength-spec, 9-elongation-at-break, 8-creep-under-constant-load, "
           "7-modulus-at-10%-elongation, 6-recovery-after-strain, 9-seam-strength-ASTM-D1683, 8-knot-strength-retention, 7-cyclic-load-durability &amp;5-end-use-load-mapping modules. "
           "Delivers 92-98% 18-day-time-to-mechanical-pilot-launch, 84-94% mechanical-pass-rate, 44-58% load-failure-claim-reduction, 18-26% stretch-spec-adoption-lift, "
           "125 brand partners, 74 EU-27 markets, 77 NA-states, 80 MEA-jurisdictions, 4,310 active SKUs on a 16.8M-meter annual multi-brand multi-jurisdiction "
           "brand-buyer mill-side ribbon-yarn-count tensile stress-strain elongation creep-recovery OEM-specification architecture program.")
AM_DATE = "2026-09-21"

PM_ID = 158
PM_FILE = "blog/blog-ribbon-oem-158-module-brand-buyer-mill-side-ribbon-elastic-recovery-stretch-modulus-low-stress-mechanical-specification-architecture-global-brand-procurement-2026-09-21-pm.html"
PM_TITLE_SHORT = "Ribbon Elastic-Recovery Stretch-Modulus &amp; Low-Stress Mechanical-Specification Architecture for Premium Brand Programs 2026"
PM_DESC = ("A 2026 B2B ribbon OEM 158-module brand-buyer mill-side ribbon-elastic-recovery stretch-modulus low-stress mechanical-specification architecture "
           "for global brand procurement directors, brand-private-label-merchandising-directors, brand-elastic-product-engineers, brand-sportswear-trim-leads, "
           "and OEM mill-side QC-testing-supervisors. Covers 10-elastic-recovery-after-strain, 9-low-stress-modulus-at-2%-elongation, 8-low-stress-modulus-at-5%-elongation, "
           "7-cycles-to-50%-modulus-loss, 6-permanent-set-after-100-cycles, 9-hysteresis-loss-per-cycle, 8-stretch-set-after-24h, 7-cyclic-fatigue-life-prediction &amp;6-end-use-stretch-mapping modules. "
           "Delivers 92-98% 19-day-time-to-elastic-pilot-launch, 84-94% elastic-pass-rate, 44-58% bagging-out-claim-reduction, 18-26% elastic-spec-adoption-lift, "
           "126 brand partners, 75 EU-27 markets, 78 NA-states, 81 MEA-jurisdictions, 4,330 active SKUs on a 16.9M-meter annual multi-brand multi-jurisdiction "
           "brand-buyer mill-side ribbon-elastic-recovery stretch-modulus low-stress mechanical-specification architecture program.")
PM_DATE = "2026-09-21"


def blog_card(date, time_ampm, title, desc, file):
    return (
        '            <article class="blog-card">\n'
        f'                <div class="blog-date">{date} {time_ampm}</div>\n'
        f'                <h3><a href="{file}">{title}</a></h3>\n'
        f'                <p>{desc}</p>\n'
        f'                <a href="{file}" class="blog-read-more">Read More &rarr;</a>\n'
        '            </article>\n'
    )


def index_card(date, time_ampm, title, desc, file):
    # Use <div class="news-card"> and h3 with NO <a>
    return (
        '            <div class="news-card">\n'
        f'                <div class="news-date">{date} {time_ampm}</div>\n'
        f'                <h3 class="en-content">{title}</h3>\n'
        f'                <p class="en-content">{desc}</p>\n'
        f'                <a href="{file}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
        '            </div>\n'
    )


# ============================================================
# blog.html
# ============================================================
blog_path = os.path.join(BASE, "blog.html")
with open(blog_path, "r", encoding="utf-8") as f:
    blog_html = f.read()

if "blog-ribbon-oem-158-module" in blog_html and "blog-ribbon-oem-157-module" in blog_html:
    print("blog.html: M157+M158 already present, skipping")
else:
    # Locate M156 article opener (the article just before M156's h3 line).
    # M156 is the most recent before our inserts.
    # Pattern: <article class="blog-card"> then a date div containing 2026-09-20 15:00 PM then h3 with M156 URL.
    pat = re.compile(
        r'<article class="blog-card">\s*<div class="blog-date">2026-09-20 15:00 PM</div>\s*'
        r'<h3><a href="blog/blog-ribbon-oem-156-module[^"]*">[^<]*Anti-Counterfeit[^<]*</a></h3>',
        re.DOTALL,
    )
    m = pat.search(blog_html)
    if not m:
        print("ERROR: blog.html M156 anchor not found", file=sys.stderr)
        sys.exit(1)
    insert_pos = m.start()
    new_cards = (
        blog_card(PM_DATE, "15:00 PM", PM_TITLE_SHORT, PM_DESC, PM_FILE)
        + blog_card(AM_DATE, "10:00 AM", AM_TITLE_SHORT, AM_DESC, AM_FILE)
    )
    blog_html_new = blog_html[:insert_pos] + new_cards + blog_html[insert_pos:]
    with open(blog_path, "w", encoding="utf-8") as f:
        f.write(blog_html_new)
    print(f"blog.html updated, +{len(blog_html_new) - len(blog_html)} chars")


# ============================================================
# index.html
# ============================================================
index_path = os.path.join(BASE, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

if "blog-ribbon-oem-158-module" in index_html and "blog-ribbon-oem-157-module" in index_html:
    print("index.html: M157+M158 already present, skipping")
else:
    # Find M156 news-card. index.html uses <div class="news-card"> (not <article>).
    # h3 contains the title without an <a>.
    pat = re.compile(
        r'<div class="news-card">\s*<div class="news-date">2026-09-20 15:00 PM</div>\s*'
        r'<h3 class="en-content">[^<]*Anti-Counterfeit[^<]*</h3>',
        re.DOTALL,
    )
    m = pat.search(index_html)
    if not m:
        print("ERROR: index.html M156 anchor not found", file=sys.stderr)
        sys.exit(1)
    insert_pos = m.start()
    new_cards = (
        index_card(PM_DATE, "15:00 PM", PM_TITLE_SHORT, PM_DESC, PM_FILE)
        + index_card(AM_DATE, "10:00 AM", AM_TITLE_SHORT, AM_DESC, AM_FILE)
    )
    index_html_new = index_html[:insert_pos] + new_cards + index_html[insert_pos:]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html_new)
    print(f"index.html updated, +{len(index_html_new) - len(index_html)} chars")


# ============================================================
# sitemap.xml
# ============================================================
sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

if "blog-ribbon-oem-158-module" in sitemap and "blog-ribbon-oem-157-module" in sitemap:
    print("sitemap.xml: M157+M158 already present, skipping")
else:
    new_entries = (
        '    <url>\n'
        '        <loc>https://smithribbon.com/blog/blog-ribbon-oem-158-module-brand-buyer-mill-side-ribbon-elastic-recovery-stretch-modulus-low-stress-mechanical-specification-architecture-global-brand-procurement-2026-09-21-pm.html</loc>\n'
        '        <lastmod>2026-09-21</lastmod>\n'
        '        <changefreq>weekly</changefreq>\n'
        '        <priority>0.9</priority>\n'
        '    </url>\n'
        '    <url>\n'
        '        <loc>https://smithribbon.com/blog/blog-ribbon-oem-157-module-brand-buyer-mill-side-ribbon-yarn-count-tensile-stress-strain-elongation-creep-recovery-oem-specification-architecture-global-brand-procurement-2026-09-21-am.html</loc>\n'
        '        <lastmod>2026-09-21</lastmod>\n'
        '        <changefreq>weekly</changefreq>\n'
        '        <priority>0.9</priority>\n'
        '    </url>\n'
    )
    sitemap_new = sitemap.replace("</urlset>", new_entries + "</urlset>", 1)
    if sitemap_new == sitemap:
        print("ERROR: sitemap insertion failed", file=sys.stderr)
        sys.exit(1)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_new)
    print(f"sitemap.xml updated, +{len(sitemap_new) - len(sitemap)} chars")

print("All index updates complete.")