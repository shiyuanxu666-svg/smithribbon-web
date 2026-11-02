#!/usr/bin/env python3
"""Rebuild valid BlogPosting + Breadcrumb schema for the 15 smithribbon blog
pages whose original JSON-LD was unrecoverable and got removed.
Derives title/description/date/image from each page's own meta so the schema
matches the visible content.
"""
import re, os, glob, json
from datetime import datetime

ROOT = "/workspace/smithribbon-web"
URL = "https://smithribbon.com"
TODAY = "2026-10-22"

TARGETS = [
 "blog-ribbon-oem-61-module-spec-sheet-rfq-to-award-reverse-engineering-brand-buyer-cost-engineering-global-brand-procurement-2026-08-18-am.html",
 "blog-ribbon-oem-56-module-spec-sheet-techpack-translation-decoder-global-brand-procurement-2026-08-17-am.html",
 "blog-ribbon-oem-15-module-wholesale-distribution-channel-partner-architecture-global-brand-procurement-2026-08-01-am.html",
 "blog-ribbon-oem-63-module-post-award-kpi-reporting-brand-buyer-vendor-scorecard-architecture-global-brand-procurement-2026-08-18-am.html",
 "blog-ribbon-oem-59-module-multi-market-holiday-gifting-peak-capacity-pre-booking-cascade-production-global-brand-procurement-2026-08-17-pm2.html",
 "blog-ribbon-oem-14-module-brand-compliance-regulatory-reporting-architecture-global-brand-procurement-2026-08-01-pm.html",
 "blog-ribbon-oem-58-module-custom-jacquard-woven-brand-identity-rapid-sampling-global-brand-procurement-2026-08-17-am2.html",
 "blog-ribbon-oem-12-module-brand-owned-tooling-asset-custody-architecture-global-brand-procurement-2026-08-02-pm.html",
 "blog-ribbon-oem-57-module-adjacent-material-bundle-program-global-brand-procurement-2026-08-17-pm.html",
 "blog-ribbon-oem-12-module-currency-fx-hedging-architecture-global-brand-procurement-2026-07-31-pm.html",
 "blog-ribbon-oem-13-module-tariff-hs-classification-architecture-global-brand-procurement-2026-08-02-am.html",
 "blog-ribbon-oem-64-module-brand-marketing-seasonal-storytelling-campaign-bundle-global-brand-procurement-2026-08-18-pm.html",
]

def get(pattern, h, default=""):
    m = re.search(pattern, h, re.S | re.I)
    return m.group(1).strip() if m else default

def pick_date(fn):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", fn)
    return m.group(1) if m else "2026-08-01"

done = []
for fn in TARGETS:
    fp = os.path.join(ROOT, fn)
    if not os.path.exists(fp):
        print("MISSING", fn); continue
    h = open(fp, encoding="utf-8", errors="ignore").read()

    title = get(r"<title>(.*?)</title>", h, fn.replace(".html", ""))
    title = re.split(r"\s*\|\s*", title)[0].strip()
    desc  = get(r'<meta\s+name="description"\s+content="([^"]*)"', h)
    ogimg = get(r'<meta\s+property="og:image"\s+content="([^"]*)"', h,
                f"{URL}/banner.png")
    if ogimg.startswith("/"):
        ogimg = URL + ogimg
    h1 = get(r"<h1[^>]*>(.*?)</h1>", h, title)
    h1 = re.sub(r"<[^>]+>", "", h1).strip() or title
    date = pick_date(fn)
    pageurl = f"{URL}/{fn}"

    desc = (desc or f"{title} — a Smith Ribbon B2B OEM guide for global brand procurement teams.")
    desc = desc[:300]

    schema = {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BlogPosting",
          "headline": h1[:110],
          "description": desc,
          "url": pageurl,
          "mainEntityOfPage": {"@type": "WebPage", "@id": pageurl},
          "datePublished": date,
          "dateModified": TODAY,
          "inLanguage": "en",
          "author": {"@type": "Organization", "name": "Smith Ribbon",
                     "url": URL,
                     "email": "xmmsd@126.com"},
          "publisher": {
            "@type": "Organization", "name": "Smith Ribbon",
            "url": URL, "logo": {"@type": "ImageObject", "url": f"{URL}/banner.png"}
          },
          "image": [ogimg],
        },
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{URL}/blog.html"},
            {"@type": "ListItem", "position": 3, "name": title[:80], "item": pageurl},
          ]
        },
        {
          "@type": "WebPage",
          "@id": pageurl,
          "name": title,
          "description": desc,
          "isPartOf": {"@type": "WebSite", "name": "Smith Ribbon", "url": URL},
        }
      ]
    }
    block = ('<script type="application/ld+json">\n'
             + json.dumps(schema, ensure_ascii=False, indent=2)
             + "\n</script>\n")
    if "application/ld+json" in h:
        i = h.rfind("</script>")
        h = h[:i + len("</script>")] + "\n" + block + h[i + len("</script>"):]
    else:
        i = h.lower().find("</head>")
        h = h[:i] + block + "  " + h[i:] if i != -1 else block + h
    open(fp, "w", encoding="utf-8").write(h)
    done.append(fn)

print("rebuilt BlogPosting schema on", len(done), "pages")

# final validation across whole site
bad = []
for fp in glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True):
    hh = open(fp, encoding="utf-8", errors="ignore").read()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', hh, re.S):
        try:
            json.loads(b.strip())
        except Exception:
            bad.append(os.path.relpath(fp, ROOT)); break
print("site-wide invalid JSON-LD blocks:", len(bad))

# sitemap: make sure these 15 are present & fresh
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
for fn in TARGETS:
    if f"{URL}/{fn}" not in sm:
        print("  NOT IN SITEMAP:", fn)
print("sitemap lastmod today:", sm.count(f"<lastmod>{TODAY}</lastmod>"))