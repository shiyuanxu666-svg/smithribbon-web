#!/usr/bin/env python3
"""Shared page-assembly helpers for smithribbon.com cron-built B2B articles."""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
SITE = "https://smithribbon.com"


def head_block(a):
    wc = a.get("word_count")
    if not wc:
        # Estimate from BODY when not supplied; callers may pass exact count.
        wc = a.get("body_words", 1760)
    return f"""<title>{a['title']}</title>
<meta name="description" content="{a['desc']}">
<meta name="keywords" content="{a['kw']}">
<meta name="author" content="Xiamen Smith Ribbon &amp; Bow Co., Ltd.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}/{a['slug']}">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:title" content="{a['title']}">
<meta property="og:description" content="{a['desc']}">
<meta property="og:url" content="{SITE}/{a['slug']}">
<meta property="og:image" content="{SITE}/banner.png">
<meta property="og:site_name" content="SmithRibbon &mdash; Xiamen Smith Ribbon &amp; Bow">
<meta property="article:published_time" content="{a['date_iso']}">
<meta property="article:modified_time" content="{a['date_iso']}">
<meta property="article:author" content="Xiamen Smith Ribbon &amp; Bow Co., Ltd.">
<meta property="article:section" content="{a['section']}">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{a['title']}">
<meta name="twitter:description" content="{a['desc']}">
<meta name="twitter:image" content="{SITE}/banner.png">

<!-- JSON-LD: BlogPosting -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{a['title']}",
  "description": "{a['desc']}",
  "image": "{SITE}/banner.png",
  "datePublished": "{a['date_iso']}",
  "dateModified": "{a['date_iso']}",
  "author": {{
    "@type": "Organization",
    "name": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
    "url": "{SITE}"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
    "url": "{SITE}",
    "logo": {{
      "@type": "ImageObject",
      "url": "{SITE}/banner.png"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{SITE}/{a['slug']}"
  }},
  "keywords": "{a['kw']}",
  "wordCount": {wc},
  "inLanguage": "en-US",
  "articleSection": "{a['section']}"
}}
</script>

<style>
  body {{ font-family: 'Segoe UI', system-ui, sans-serif; line-height: 1.8; color: #2a2a2a; max-width: 980px; margin: 0 auto; padding: 24px; background: #fafafa; }}
  h1 {{ font-size: 2.1rem; color: #8b1538; margin-bottom: 0.4em; line-height: 1.3; }}
  h2 {{ font-size: 1.55rem; color: #5a0f25; margin-top: 1.8em; border-left: 4px solid #b8854a; padding-left: 12px; }}
  h3 {{ font-size: 1.25rem; color: #5a0f25; margin-top: 1.4em; }}
  .meta {{ color: #777; font-size: 0.92rem; margin-bottom: 1.6em; padding-bottom: 12px; border-bottom: 1px solid #e0e0e0; }}
  .kpi {{ background: #f0f7f0; border: 1px solid #c8e0c8; border-radius: 6px; padding: 14px 18px; margin: 1.2em 0; }}
  .kpi strong {{ color: #2e6b2e; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1.2em 0; background: #fff; }}
  th, td {{ border: 1px solid #e0d0c0; padding: 10px 12px; text-align: left; font-size: 0.95rem; }}
  th {{ background: #f5ebe0; color: #5a0f25; font-weight: 600; }}
  ul, ol {{ margin: 0.8em 0 0.8em 1.6em; }}
  li {{ margin-bottom: 6px; }}
  .cta {{ background: linear-gradient(135deg, #8b1538 0%, #b8854a 100%); color: #fff; padding: 22px 28px; border-radius: 8px; margin: 2em 0; text-align: center; }}
  .cta a {{ color: #fff; text-decoration: underline; font-weight: 600; }}
  .tag {{ display: inline-block; background: #f5ebe0; color: #5a0f25; padding: 4px 12px; border-radius: 14px; font-size: 0.85rem; margin-right: 6px; }}
</style>
    <meta name="msvalidate.01" content="ECF29653135740AB77EEF5074F931DF4" />
  </head>
<body>

<h1>{a['title']}</h1>
<div class="meta">
  <span class="tag">{a['tag']}</span>
  Published {a['date_human']} &middot; Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; {a['read']}
</div>
"""


def cta_block(heading, cta_text):
    return f"""<div class="cta">
  <h3 style="color:#fff;border:none;margin-top:0;">{heading}</h3>
  <p>Smith Ribbon has supplied woven and printed ribbon, bows, and decorative trims to 1,000+ brands and retailers across 50+ countries since 2004. Our 15,000 m&sup2; plant runs 200+ employees with 100,000 meters of daily capacity, certified to OEKO-TEX&reg;, FSC&reg;, BSCI, SEDEX, SMETA and ISO 9001.</p>
  <p><strong>Talk to a compliance engineer:</strong> +86 13779951780 (WeChat) &nbsp;|&nbsp; xmmsd@126.com &nbsp;|&nbsp; www.smithribbon.com</p>
  <p><a href="/contact.html">{cta_text} &rarr;</a></p>
</div>

<p style="font-size:0.9rem;color:#777;margin-top:2em;">Smith Ribbon OEM since 2004 &mdash; woven ribbon, satin, grosgrain, velvet, organza, RPET, printed bows, decorative trims, and private-label accessories for global brand buyers.</p>
</div>
</body>
</html>
"""


def write_article(a, body, cta_heading, cta_text, min_words=1200):
    html = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n' + head_block(a)
            + body + "\n" + cta_block(cta_heading, cta_text))
    out = ROOT / (a["slug"] + ".html")
    out.write_text(html, encoding="utf-8")
    words = len(body.split())
    print(f"Wrote {out.name} ({len(html)} bytes, ~{words} body words)")
    assert words >= min_words, f"too short: {words}"
    return out