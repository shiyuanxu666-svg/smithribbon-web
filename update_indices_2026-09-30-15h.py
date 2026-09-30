#!/usr/bin/env python3
"""Update sitemap.xml and any blog list with article 185 PM — 2026-09-30 cron 15:00."""
import os, re

WEB = "/workspace/smithribbon-web"
BLOG = "/workspace/smithribbon-web/blog"
SITE_URL = "https://smithribbon.com"
TODAY = "2026-09-30"

FILE_185 = "blog-ribbon-oem-185-module-brand-buyer-mill-side-brand-engineer-residency-smart-trim-co-creation-architecture-5-day-pilot-90-day-scale-trim-sprint-global-brand-procurement-2026-09-30-pm.html"
TITLE_185 = "Brand-Buyer Mill-Side Brand-Engineer-Residency Smart-Trim Co-Creation Architecture: 5-Day Pilot 90-Day Scale-Trim Sprint — B2B Ribbon OEM 2026"
DESC_185 = "B2B ribbon OEM 185-module brand-buyer-mill-side brand-engineer-residency smart-trim co-creation architecture with 5-day pilot 90-day scale-trim sprint. Brand-brief discovery, mill-engineering feasibility, dual-key approval, IP-allocation royalty-model, SKU-velocity measurement. Smith Ribbon OEM since 2004."


def update_sitemap():
    path = os.path.join(WEB, "sitemap.xml")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()
    if FILE_185 in xml:
        print(f"  SITEMAP: {FILE_185} already present")
        return
    entry = (
        f"  <url>\n"
        f"    <loc>{SITE_URL}/{FILE_185}</loc>\n"
        f"    <lastmod>{TODAY}</lastmod>\n"
        f"    <changefreq>weekly</changefreq>\n"
        f"    <priority>0.85</priority>\n"
        f"  </url>\n"
    )
    closing = "</urlset>"
    idx = xml.rfind(closing)
    if idx == -1:
        updated = xml + entry
    else:
        updated = xml[:idx] + entry + xml[idx:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("  UPDATED sitemap.xml")


def update_blog_html():
    """If there's a blog.html that lists articles, prepend a new card."""
    for fname in ["blog.html", "en-blog.html", "index.html"]:
        path = os.path.join(WEB, fname)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        if FILE_185 in html:
            print(f"  {fname}: already present")
            continue
        # Skip index.html unless it has a blog list
        if fname == "index.html" and "blog" not in html.lower():
            continue
        card = (
            f'<article class="post-card">\n'
            f'  <a href="/{FILE_185}">\n'
            f'    <h3>{TITLE_185}</h3>\n'
            f'  </a>\n'
            f'  <p>{DESC_185}</p>\n'
            f'  <div class="post-meta">{TODAY} &middot; Brand-Buyer Residencies</div>\n'
            f'</article>\n'
        )
        # insert before any matching post-list container
        m = re.search(r'(<div\s+class\s*=\s*["\'][^"\']*post[^"\']*["\'])', html, re.IGNORECASE)
        if not m:
            continue
        end = m.end()
        new_html = html[:end] + "\n" + card + html[end:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"  UPDATED {fname}")


if __name__ == "__main__":
    update_sitemap()
    update_blog_html()
    print("Done.")