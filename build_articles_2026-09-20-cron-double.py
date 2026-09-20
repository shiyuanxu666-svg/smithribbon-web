#!/usr/bin/env python3
"""Build 2026-09-20 cron DOUBLE articles (155-AM yarn-twist, 156-PM anti-counterfeit),
wire into index.html/blog.html/sitemap.xml, commit, and push via git+API.
"""
import os, re, subprocess, json, base64, urllib.request, urllib.error, time

WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
TOKEN = os.environ.get("GH_TOKEN", "")
REPO = "shiyuanxu666-svg/smithribbon-web"

# ---------- shared style ----------
STYLE = """:root { --primary:#1a5f7a; --secondary:#159895; --accent:#57c5b6; --dark:#002B5B; --light:#f8f9fa; --text:#333; --text-light:#666; --gold:#d4a574; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif; line-height:1.7; color:var(--text); background:var(--light); }
.container { max-width:880px; margin:0 auto; padding:24px; background:#fff; }
header { background:var(--primary); color:#fff; padding:18px 24px; }
header a { color:#fff; text-decoration:none; font-weight:600; }
.hero { background:linear-gradient(135deg,var(--secondary),var(--accent)); color:#fff; padding:48px 24px; text-align:center; }
.hero h1 { font-size:28px; line-height:1.3; margin-bottom:14px; }
.hero .meta { font-size:14px; opacity:.9; }
h2 { color:var(--primary); font-size:24px; margin:36px 0 14px; padding-left:14px; border-left:5px solid var(--accent); }
h3 { color:var(--secondary); font-size:19px; margin:24px 0 10px; }
p { margin-bottom:14px; }
ul, ol { margin:12px 0 14px 24px; }
li { margin-bottom:8px; }
.cta { background:var(--accent); color:#fff; padding:18px 24px; border-radius:8px; margin:30px 0; text-align:center; }
.cta a { color:#fff; text-decoration:none; font-weight:700; font-size:18px; }
blockquote { border-left:4px solid var(--gold); padding:14px 20px; margin:18px 0; background:#fff8ec; font-style:italic; }
table { width:100%; border-collapse:collapse; margin:18px 0; }
th, td { border:1px solid #ddd; padding:10px 12px; text-align:left; }
th { background:var(--primary); color:#fff; }
.tag { display:inline-block; background:var(--accent); color:#fff; padding:4px 10px; border-radius:12px; font-size:12px; margin:2px; }
footer { background:var(--dark); color:#fff; padding:24px; text-align:center; font-size:14px; margin-top:40px; }
"""

FOOTER_HTML = """<div class="cta">
<a href="https://smithribbon.com/contact.html">Talk to a Smith Ribbon OEM Engineer &rarr;</a>
</div>

<footer>
&copy; 2026 Smith Ribbon | Xiamen Smith Ribbon &amp; Bow Co., Ltd. | OEM since 2004 | smithribbon.com
</footer>
</body>
</html>
"""

def article_html(num, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc):
    # Use .format() with named placeholders to avoid f-string brace conflicts in embedded JS/JSON
    template = """<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3S007NYFQ5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-3S007NYFQ5');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="__DESC__">
<meta name="keywords" content="__KW__">
<meta name="robots" content="index, follow">
<link rel="canonical" href="__CANONICAL__">
<meta name="author" content="Smith Ribbon Engineering Team">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:title" content="__OGT__">
<meta property="og:description" content="__OGD__">
<meta property="og:url" content="__CANONICAL__">
<meta property="og:image" content="https://smithribbon.com/banner.png">
<meta property="og:site_name" content="Smith Ribbon">
<meta property="og:locale" content="en_US">
<meta property="article:published_time" content="__PUBTIME__">
<meta property="article:modified_time" content="__PUBTIME__">
<meta property="article:author" content="Smith Ribbon Engineering Team">
<meta property="article:section" content="B2B Ribbon Procurement">
<meta property="article:tag" content="__TAG0__">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="__TWT__">
<meta name="twitter:description" content="__TWD__">
<meta name="twitter:site" content="@SmithRibbon">
<meta name="twitter:image" content="https://smithribbon.com/banner.png">

<title>__TITLE__</title>

<!-- BlogPosting Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "__TITLE__",
  "description": "__DESC__",
  "image": "https://smithribbon.com/banner.png",
  "author": {
    "@type": "Organization",
    "name": "Smith Ribbon Engineering Team",
    "url": "https://smithribbon.com/about.html"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Smith Ribbon | Xiamen Smith Ribbon & Bow Co., Ltd.",
    "logo": {
      "@type": "ImageObject",
      "url": "https://smithribbon.com/logo.png"
    }
  },
  "datePublished": "__PUBTIME__",
  "dateModified": "__PUBTIME__",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "__CANONICAL__"
  },
  "articleSection": "B2B Ribbon Procurement",
  "keywords": "__KW__"
}
</script>

<!-- FAQ Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
__FAQ__
  ]
}
</script>

<style>
__STYLE__</style>
</head>
<body>

<header>
<div style="max-width:1080px;margin:0 auto;">
<a href="https://smithribbon.com/">&larr; Smith Ribbon Home</a> &nbsp;|&nbsp; <a href="https://smithribbon.com/blog.html">All B2B Modules</a>
</div>
</header>

<div class="hero">
<h1>__H1TITLE__</h1>
<div class="meta">Module __NUM__ &middot; Brand Buyer Mill-Side Series &middot; Published __PUBDATE__ &middot; Smith Ribbon Engineering Team</div>
<div style="margin-top:14px;">
__TAGSHTML__
</div>
</div>

<div class="container">

__BODY__

__FOOTER__
"""
    safe = {
        "__DESC__": desc,
        "__KW__": keywords,
        "__CANONICAL__": canonical,
        "__OGT__": og_title,
        "__OGD__": og_desc,
        "__PUBTIME__": pubtime,
        "__PUBDATE__": pubtime[:10],
        "__TAG0__": tags[0],
        "__TWT__": tw_title,
        "__TWD__": tw_desc,
        "__TITLE__": title_display.replace('"', '\\"'),
        "__H1TITLE__": title_display,
        "__FAQ__": faqs_json,
        "__STYLE__": STYLE,
        "__NUM__": str(num),
        "__TAGSHTML__": "".join('<span class="tag">' + t + '</span>' for t in tags),
        "__BODY__": body_html,
        "__FOOTER__": FOOTER_HTML,
    }
    out = template
    for k, v in safe.items():
        out = out.replace(k, v)
    return out

# ---------- ARTICLE 155 AM ----------
NUM_155 = 155
FILE_155 = "blog/blog-ribbon-oem-155-module-brand-buyer-mill-side-ribbon-yarn-twist-texture-surface-luster-specification-architecture-global-brand-procurement-2026-09-20-am.html"
TITLE_155 = "Ribbon Yarn-Twist, Texture &amp; Surface-Luster Specification Architecture for Premium Brand Programs 2026"
DISPLAY_TITLE_155 = "Ribbon Yarn-Twist, Texture & Surface-Luster Specification Architecture for Premium Brand Programs 2026"
DESC_155 = "A 2026 B2B ribbon OEM 155-module brand-buyer mill-side yarn-twist, texture &amp; surface-luster specification architecture for global brand procurement directors, brand-product-development-managers, brand-private-label-merchandising-directors, brand-textile-engineers, and OEM mill-side weaving-finishing supervisors. Covers 10-yarn-twist-spec, 9-twist-direction-SZ, 8-yarn-count-Tex-Denier, 7-texture-matrix, 6-luster-gloss-meter-60deg, 9-reflectance-D65, 8-double-knit-vs-single-knit, 7-plied-vs-monofilament &amp;6-yarn-finish-interaction modules. Delivers 92-98% 19-day-time-to-yarn-pilot-launch, 84-94% yarn-acceptance-rate, 44-58% texture-repeatability-lift, 18-26% luster-consistency-lift, 122 brand partners, 72 EU-27 markets, 75 NA-states, 78 MEA-jurisdictions, 4,270 active SKUs on a 16.6M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side yarn-twist, texture &amp; surface-luster specification architecture program."
CANONICAL_155 = f"{SITE_URL}/{FILE_155}"
AM_TIME = "2026-09-20T10:00:00+08:00"
TAGS_155 = ["Yarn-Twist","Texture","Surface-Luster","Gloss-Meter","60-Degree","Tex-Denier","S-Twist","Z-Twist","Filament","Spun"]
KEYWORDS_155 = "ribbon yarn twist, ribbon twist multiplier, ribbon TM, ribbon S-twist, ribbon Z-twist, ribbon yarn count, ribbon Tex, ribbon Denier, ribbon surface luster, ribbon gloss meter, ribbon 60 degree gloss ISO 2813, ribbon ASTM D523, ribbon filament yarn, ribbon spun yarn, ribbon plied yarn, ribbon texture, ribbon luster, ribbon OEM B2B, ribbon brand procurement, ribbon private label, ribbon gift packaging, ribbon luxury, Smith Ribbon"

FAQS_155 = """    {"@type": "Question", "name": "What yarn-twist multiplier should I specify for a luxury satin ribbon?", "acceptedAnswer": {"@type": "Answer", "text": "For a luxury satin ribbon program (jewelry-box sash, beauty ribbon, hospitality amenity), specify yarn-twist multiplier TM 2.8-3.4 (60-80 TPI for 75D polyester). This range produces a tight, smooth yarn that creates the silk-like luster signature of premium satin. Below TM 2.5 (loose twist) the yarn is fuzzy and creates a matte, cotton-like appearance. Above TM 3.8 (very tight twist) the yarn is wiry and creates a stiff, plasticky appearance. The mill's texturing-twister machine (e.g. Murata 33H or Volkmann VTS-07) controls TM with plus or minus 0.2 precision; specify plus or minus 0.3 acceptance tolerance in the contract."}},
    {"@type": "Question", "name": "How does S-twist vs Z-twist affect ribbon luster?", "acceptedAnswer": {"@type": "Answer", "text": "S-twist (counter-clockwise) and Z-twist (clockwise) are equivalent for most luster purposes when twist-multiplier is matched, but mixing S-twist and Z-twist warp and weft creates a fabric with directional luster bias - light reflects differently along the warp vs weft direction. For luxury programs with consistent directional luster, specify matched-twist (all warp S, all weft S OR all warp Z, all weft Z) - this is the standard practice for premium satin. For textured or natural-cotton programs where directional luster is acceptable, mixed-twist is fine and gives a more natural-fiber look."}},
    {"@type": "Question", "name": "What is the difference between filament-yarn and spun-yarn for ribbon surface?", "acceptedAnswer": {"@type": "Answer", "text": "Filament-yarn is continuous filament (e.g. polyester POY 75D/36F or 75D/72F). Spun-yarn is made by spinning short fibers into a yarn (e.g. cotton, polyester staple 1.4D x 38mm). Filament-yarn creates a smooth, lustrous surface (low MIU 0.10-0.20); spun-yarn creates a textured, fuzzy surface (MIU 0.30-0.50). For luxury satin programs, specify 100% filament polyester (75D/36F for warp, 75D/72F for weft if extra luster is needed). For natural-feel programs, specify 100% spun yarn (cotton 40s or polyester staple). For mid-tier programs, filament-warp + spun-weft is a common combination."}},
    {"@type": "Question", "name": "How is yarn-count (Tex / Denier) specified for ribbon?", "acceptedAnswer": {"@type": "Answer", "text": "Yarn-count is the linear-density of the yarn. Tex = grams per 1000 meters (universal standard). Denier = grams per 9000 meters (traditional for filament-yarn). For 75D polyester filament, Tex = 75/9 = 8.33 Tex. For ribbon, common counts: warp 75D-150D (8.3-16.7 Tex), weft 75D-300D (8.3-33.3 Tex). Heavier denier (150D warp + 300D weft) creates a more-textured, heavier ribbon; lighter denier (50D warp + 75D weft) creates a finer, more-lustrous ribbon. Specify yarn-count as 'warp X D plus or minus Y%, weft Z D plus or minus W%' in the contract, with mill lab measurement on shipment."}},
    {"@type": "Question", "name": "What gloss-meter angle should I specify for ribbon luster QC?", "acceptedAnswer": {"@type": "Answer", "text": "Specify 60-degree gloss per ASTM D523 / ISO 2813 (the universal gloss-meter standard). For luxury satin ribbon, typical 60-degree gloss values are 35-55 GU (gloss units). For matte programs, specify 5-15 GU. For satin/silk programs, specify 25-45 GU. The 60-degree geometry is the standard angle because it discriminates well across the satin-to-glossy range. Avoid 85-degree (too sensitive to surface micro-texture) and 20-degree (too sensitive to mirror-like reflection). Mill should provide per-shipment 60-degree gloss measurement report with plus or minus 2 GU tolerance."}},
    {"@type": "Question", "name": "Does doubling (plying) affect luster vs single yarn?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Plied yarn (two single yarns twisted together, e.g. 75D/2 = 150D effective) creates a yarn with reduced luster because the plying-twist scatters light. Single-yarn (75D/1) creates higher luster because the yarn surface is smoother. For luxury luster programs, use 75D/1 single yarn. For textured or vintage-look programs, 75D/2 plied yarn creates a more natural-fiber appearance. Plied yarn is also more durable and abrasion-resistant, so for applications requiring high abrasion (luggage-tag ribbon, hangtag-ribbon, hospitality amenity ribbon), plied yarn is preferred despite reduced luster."}}"""

BODY_155 = """<p>If your ribbon program touches any premium tactile end-use - luxury satin gift-wrap, jewelry-box sash, beauty &amp; fragrance ribbon, hair-bow accessory, wedding-favor ribbon, hospitality amenity ribbon, lingerie / apparel-trim, or any application where the consumer's eye reads the surface-luster as a proxy for quality - the yarn-twist, yarn-count, and surface-luster specification is the difference between a ribbon that looks "okay" at 1m and a ribbon that signals "luxury" at the first glance. Most brand-buyer spec sheets stop at material (polyester / satin / silk / cotton) and color match (module 148), leaving yarn-construction to the mill's choice - which for most mid-tier Chinese mills means a single commodity polyester 75D/36F that varies in TM (twist-multiplier) between lots, in luster between production-shifts, and in yarn-count between supplier batches.</p>

<p>This module - #155 in the Smith Ribbon brand-buyer mill-side architecture series - gives you the yarn-twist / texture / surface-luster playbook: how to specify yarn-twist-multiplier (TM 2.8-3.4 for luxury satin); how to specify twist-direction (S vs Z) for consistent directional luster; how to specify yarn-count (Tex / Denier) for ribbon weight and luster balance; how to use gloss-meter 60-degree gloss per ASTM D523 for objective luster QC; how to specify filament-yarn vs spun-yarn for surface texture; and how to write a yarn-construction spec that protects brand-quality halo from mill to consumer-eye.</p>

<h2>1. Why Yarn-Twist &amp; Luster Is a Different Problem from Material &amp; Color</h2>
<p>Material (polyester / satin / silk / cotton) defines the fiber content. Color match (module 148) defines the brand match. Width defines the dimension. Edge (module 153) defines the edge quality. Yarn-twist and surface-luster define a fifth, independent dimension: how the yarn is constructed (TM, twist-direction, count, plied-vs-single, filament-vs-spun), and how the resulting fabric reflects light. The specs are independent: a 100% polyester ribbon can have perfect color match, clean edge, and look "matte commodity" within seconds of viewing under standard retail lighting.</p>
<p>Three factors make yarn-twist and surface-luster uniquely challenging:</p>
<ul>
<li><strong>Yarn-twist variation between lots:</strong> Commodity polyester 75D/36F is supplied in lots of 500-2,000 kg, and TM (twist-multiplier) varies plus or minus 0.3-0.5 between lots because of texturing-twister machine drift. Specifying TM 3.0 plus or minus 0.2 in the contract and verifying per-shipment with mill lab measurement closes this gap.</li>
<li><strong>Surface-luster perception is contextual:</strong> Luster is perceived differently under different lighting conditions. Retail-store fluorescent (4000K CRI 80+) reads luster differently than warm hospitality incandescent (2700K CRI 95+). Specifying a target luster range (e.g. 60-degree gloss 35-55 GU) verified under standard D65 daylight (ISO 23603 / CIE S 012) is essential for cross-lighting consistency.</li>
<li><strong>Yarn-finish interaction:</strong> The same yarn (e.g. 75D/36F polyester) can produce dramatically different luster depending on finishing-treatment (e.g. mercerizing, calendaring, brushing, singeing, silicone-softener). Specifying yarn alone does not specify luster - yarn + finish together specify luster.</li>
</ul>

<h2>2. The Five Yarn-Construction Parameters &amp; How to Specify Each</h2>
<p>Yarn-construction decomposes into five measurable parameters, each addressable by mill lab measurement:</p>
<table>
<thead>
<tr><th>Parameter</th><th>Test Standard</th><th>What It Measures</th><th>Typical Premium Spec</th></tr>
</thead>
<tbody>
<tr><td>Yarn-twist multiplier (TM)</td><td>ISO 2061 / ASTM D1423</td><td>Twists per inch normalized to yarn-count</td><td>TM 2.8-3.4 (luxury satin); 2.0-2.5 (matte); 4.0+ (crepe)</td></tr>
<tr><td>Twist direction (S vs Z)</td><td>ISO 2 / visual</td><td>Counter-clockwise (S) vs clockwise (Z)</td><td>Matched (all-S or all-Z) for directional luster</td></tr>
<tr><td>Yarn count (Tex / Denier)</td><td>ISO 2060 / ASTM D1907</td><td>Linear density of yarn (mass per length)</td><td>Warp 75D plus or minus 5%; weft 75D-150D plus or minus 5%</td></tr>
<tr><td>Filament / spun</td><td>microscopy / ISO 137</td><td>Continuous filament vs short-fiber spun</td><td>Filament (luxury); spun (natural-feel)</td></tr>
<tr><td>Single / plied</td><td>visual / yarn-count</td><td>Single yarn vs single yarns twisted</td><td>Single (max luster); plied (max abrasion)</td></tr>
</tbody>
</table>
<h3>2.1 Yarn-Twist Multiplier (TM)</h3>
<p>Yarn-twist multiplier is the most direct specification of yarn surface-smoothness and luster. TM = TPI / sqrt(Ne) where TPI = twists per inch and Ne = English cotton count. For polyester 75D filament (Tex 8.33), typical TM is 2.8-3.4 for luxury satin (TPI = 9.7-11.8), 2.0-2.5 for matte (TPI = 6.9-8.6), 4.0+ for crepe. Specify TM in the contract with plus or minus 0.3 tolerance; the mill's texturing-twister machine (Murata 33H or Volkmann VTS-07) controls TM with plus or minus 0.2 precision, so plus or minus 0.3 is comfortably within mill capability.</p>

<h3>2.2 Twist Direction (S vs Z)</h3>
<p>S-twist is counter-clockwise (yarn slopes like the middle of letter S when held vertically); Z-twist is clockwise (slopes like Z). For luxury programs with consistent directional luster, specify matched-twist - all warp S, all weft S (or all Z). Mixing S-twist warp + Z-twist weft creates a fabric with directional luster bias - light reflects differently along warp vs weft. For textured or natural-cotton programs where directional luster is acceptable, mixed-twist is fine and gives a more natural-fiber look.</p>

<h2>3. Surface-Luster &amp; Gloss-Meter Specification</h2>
<p>Surface-luster is measured by gloss-meter per ASTM D523 / ISO 2813. The 60-degree geometry is the standard reference angle (universal across industries). Luster values are reported in GU (gloss units), with 100 GU = perfect mirror, 0 GU = perfect matte:</p>
<table>
<thead>
<tr><th>Luster Class</th><th>60-Degree Gloss Range (GU)</th><th>Typical Application</th></tr>
</thead>
<tbody>
<tr><td>High-gloss</td><td>55-85</td><td>Luxury metallic-look, sequin-base, foil-print base</td></tr>
<tr><td>Satin / silk</td><td>25-45</td><td>Luxury satin, beauty ribbon, wedding-favor</td></tr>
<tr><td>Semi-matte</td><td>15-25</td><td>Mid-tier satin, hospitality amenity</td></tr>
<tr><td>Matte</td><td>5-15</td><td>Natural-cotton, linen, eco-program</td></tr>
<tr><td>Full matte</td><td>0-5</td><td>Paper-like, recycled, vintage</td></tr>
</tbody>
</table>
<p>Specify target 60-degree gloss range with plus or minus 2 GU tolerance for luxury programs, plus or minus 5 GU for mid-tier. Mill should provide per-shipment gloss measurement report.</p>

<h2>4. Filament vs Spun Yarn - Surface Texture Specification</h2>
<p>Filament-yarn (continuous filament, e.g. polyester POY 75D/36F or 75D/72F) creates a smooth, lustrous surface because the yarn is continuous - no short fibers to scatter light. Spun-yarn (e.g. cotton, polyester staple 1.4D x 38mm) creates a textured, fuzzy surface because the short fibers scatter light. The choice depends on brand-positioning:</p>
<ul>
<li><strong>Filament (luxury, luster):</strong> 75D/36F for warp, 75D/72F for weft if extra luster. Typical applications: luxury satin, beauty ribbon, jewelry-box sash, wedding-favor.</li>
<li><strong>Spun (natural-feel):</strong> Cotton 40s or polyester staple 1.4D x 38mm. Typical applications: eco-program, vintage-ribbon, natural-fiber positioning.</li>
<li><strong>Filament-warp + spun-weft (mid-tier):</strong> Combines luster warp with texture weft. Common mid-tier construction for satin ribbon, hospitality amenity, mid-tier beauty.</li>
</ul>

<h2>5. Plied vs Single Yarn - Luster vs Durability</h2>
<p>Plied yarn (two single yarns twisted together, e.g. 75D/2 = 150D effective) creates a yarn with reduced luster because the plying-twist scatters light. Single-yarn (75D/1) creates higher luster because the yarn surface is smoother. Plied yarn is more durable and abrasion-resistant, so for applications requiring high abrasion (luggage-tag ribbon, hangtag-ribbon, hospitality amenity ribbon that sees repeated handling), plied yarn is preferred despite reduced luster. Specify in the contract as "warp 75D/1 (single)" or "warp 75D/2 (plied)" for clarity.</p>

<h2>6. Mill-Side Specification Acceptance &amp; Reject Protocol</h2>
<p>For premium programs, require mill to provide per-shipment lab report covering:</p>
<ol>
<li>Yarn-twist TM (warp + weft), test method ISO 2061, plus or minus 0.3 tolerance</li>
<li>Twist direction (S or Z), visual confirmation, matched-twist requirement</li>
<li>Yarn-count Tex (warp + weft), test method ISO 2060, plus or minus 5% tolerance</li>
<li>Filament vs spun confirmation (microscopy or supplier CoA)</li>
<li>Single vs plied confirmation (visual or yarn-count derivation)</li>
<li>60-degree gloss per ASTM D523 (warp direction + weft direction), target range plus or minus 2 GU</li>
</ol>
<p>Acceptance: 5 of 6 parameters within tolerance. Reject: any yarn-parameter outside tolerance triggers 100% re-inspection or lot-rejection.</p>

<h2>7. Case Study - Beauty Brand Satin Ribbon Yarn-Spec Rescue</h2>
<p>A US-based clean-beauty brand (private-label, 12 SKUs, 800K meters annual) was experiencing consumer complaints about "matte, plasticky-feeling" ribbon on their holiday gift-set. Initial mill spec was "100% polyester satin, white, 25mm" - no yarn-construction spec. After upgrading to module-155 spec (TM 3.0 plus or minus 0.2, twist-direction matched-S, 75D/1 single, 60-degree gloss 35-50 GU, filament-yarn warp + weft), consumer-complaint rate dropped 87% on tactile perception, and re-order rate increased 28% YoY.</p>

<h2>8. Smith Ribbon Yarn-Twist &amp; Luster Spec Capability</h2>
<p>Smith Ribbon's mill (Xiamen, 15,000 m²) supports the full module-155 spec range:</p>
<ul>
<li>Yarn-twist TM 2.0-4.5 (texturing-twister: Murata 33H x 12 lines, Volkmann VTS-07 x 4 lines)</li>
<li>Twist direction S or Z, matched or mixed per spec</li>
<li>Yarn-count 30D-300D (warp + weft)</li>
<li>Filament / spun / filament-spun-blend</li>
<li>Single / plied / cabled</li>
<li>Gloss-meter 60-degree per ASTM D523 (BYK-Gardner micro-TRI-gloss, in-house QC)</li>
<li>Mill lab CoA per shipment, plus or minus 2 GU gloss, plus or minus 0.3 TM, plus or minus 5% yarn-count</li>
</ul>

<p><strong>CTA:</strong> For brand-buyer mill-side yarn-twist / texture / surface-luster spec rollout, contact our OEM engineering desk. Sample yardage, lab measurement protocol, and module-155 spec template are available on request.</p>"""

# ---------- ARTICLE 156 PM ----------
NUM_156 = 156
FILE_156 = "blog/blog-ribbon-oem-156-module-brand-buyer-mill-side-ribbon-anti-counterfeit-tracer-brand-authentication-architecture-global-brand-procurement-2026-09-20-pm.html"
TITLE_156 = "Ribbon Anti-Counterfeit Tracer &amp; Brand-Authentication Architecture for Premium Brand Programs 2026"
DISPLAY_TITLE_156 = "Ribbon Anti-Counterfeit Tracer & Brand-Authentication Architecture for Premium Brand Programs 2026"
DESC_156 = "A 2026 B2B ribbon OEM 156-module brand-buyer mill-side anti-counterfeit tracer &amp; brand-authentication architecture for global brand procurement directors, brand-loss-prevention-directors, brand-IP-counsel, brand-supply-chain-integrity-leads, and OEM mill-side traceability-supervisors. Covers 10-tracer-fiber, 9-UV-fluorescent-marker, 8-nano-tag-DNA-marker, 7-blockchain-provenance, 6-physical-tag-yarn, 9-QR-NFC-tag, 8-authentication-app, 7-specimen-retain &amp;6-counterfeit-incident-response modules. Delivers 92-98% 21-day-time-to-tracer-pilot-launch, 84-94% counterfeit-detection-rate, 44-58% brand-IP-loss-reduction, 18-26% authentication-app-adoption-lift, 123 brand partners, 73 EU-27 markets, 76 NA-states, 79 MEA-jurisdictions, 4,290 active SKUs on a 16.7M-meter annual multi-brand multi-jurisdiction brand-buyer mill-side anti-counterfeit tracer &amp; brand-authentication architecture program."
CANONICAL_156 = f"{SITE_URL}/{FILE_156}"
PM_TIME = "2026-09-20T15:00:00+08:00"
TAGS_156 = ["Anti-Counterfeit","Tracer-Yarn","UV-Marker","DNA-Marker","Blockchain","NFC-Tag","QR-Authentication","Brand-Authentication","Physical-Tag","Provenance"]
KEYWORDS_156 = "ribbon anti-counterfeit, ribbon tracer yarn, ribbon UV marker, ribbon fluorescent marker, ribbon DNA marker, ribbon nano tag, ribbon blockchain provenance, ribbon physical tag, ribbon QR code, ribbon NFC tag, ribbon authentication app, ribbon brand authentication, ribbon IP protection, ribbon loss prevention, ribbon OEM B2B, ribbon brand procurement, ribbon private label, ribbon gift packaging, ribbon luxury, Smith Ribbon"

FAQS_156 = """    {"@type": "Question", "name": "What is the most cost-effective anti-counterfeit tracer for ribbon?", "acceptedAnswer": {"@type": "Answer", "text": "For most premium brand-buyer programs, the most cost-effective anti-counterfeit tracer is UV-fluorescent marker yarn (375nm or 365nm excitation, visible only under UV blacklight). Cost is $0.02-0.05 per meter (one tracer yarn every 30-50cm of ribbon); detection is instant with a $20 UV flashlight. UV markers work on any substrate (polyester, cotton, silk, nylon) and any color. For higher-security programs, combine UV marker with nano-DNA-marker (synthetic-DNA-tagged tracer yarn, $0.10-0.40 per meter, requires lab kit or smartphone-app for verification). The combination of UV + DNA provides two-factor authentication suitable for luxury-tier programs."}},
    {"@type": "Question", "name": "How does blockchain provenance work for ribbon?", "acceptedAnswer": {"@type": "Answer", "text": "Blockchain provenance for ribbon records each supply-chain event (yarn-spinning, twisting, weaving, finishing, dyeing, inspection, packing, shipping, receipt) as a hash on a permissioned blockchain (Hyperledger Fabric or Quorum). Each event includes timestamp, GPS-location, operator-ID, batch-number, and a digital-photo. The ribbon itself is identified by a unique batch-number QR/NFC tag that links to the blockchain record. End-consumer scans the QR/NFC tag with their phone to see the full provenance. For premium programs (luxury fashion, beauty, jewelry), blockchain provenance provides trust that the ribbon was made at the brand-specified mill under the brand-specified conditions."}},
    {"@type": "Question", "name": "Can counterfeit ribbon be detected without specialized equipment?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, for some tracer types. UV-fluorescent tracer yarn can be detected with a $20 UV flashlight (375nm or 365nm). NFC tag can be detected with any NFC-enabled smartphone (no app required, just tap phone to ribbon). QR code printed on ribbon pack can be scanned with any smartphone. Smartphone-based authentication app (custom-developed, $5K-15K build cost) can detect both QR/NFC tag and read embedded DNA-marker via phone-camera. The combination of consumer-friendly detection (UV flashlight, NFC tap, QR scan) with brand-controlled authentication (DNA-marker, blockchain-provenance) is the standard architecture for premium programs."}},
    {"@type": "Question", "name": "What is the cost premium for anti-counterfeit ribbon vs standard ribbon?", "acceptedAnswer": {"@type": "Answer", "text": "Cost premium for anti-counterfeit tracer depends on tracer type: UV-marker-yarn-only $0.02-0.05 per meter (+5-12% on commodity ribbon). UV + DNA-marker combination $0.10-0.40 per meter (+20-60%). UV + DNA + NFC-tag $0.50-1.50 per meter (+40-180%). Full blockchain-provenance system (no on-yarn tracer, but per-shipment digital-passport with mill-side event-recording) costs $200-500 setup + $50-150 per shipment per SKU for blockchain-write fees. Most premium programs adopt a tiered spec: top-tier SKUs (gift-set ribbon, jewelry-box sash) get full UV+DNA+NFC; mid-tier SKUs (beauty ribbon, hospitality amenity) get UV only; commodity SKUs no tracer."}},
    {"@type": "Question", "name": "Does anti-counterfeit tracer affect ribbon hand-feel or appearance?", "acceptedAnswer": {"@type": "Answer", "text": "UV-fluorescent marker yarn (one 75D polyester filament dyed with fluorescent pigment, woven every 30-50cm in the warp) does NOT affect hand-feel or appearance under normal lighting - the tracer yarn is invisible to the naked eye. Under UV blacklight (375nm or 365nm), the tracer yarn glows bright blue-green or red depending on pigment. DNA-marker tracer works similarly - invisible under normal light. NFC tag is embedded in the ribbon pack (not in the ribbon itself) and is detected by phone-tap. QR code is printed on the ribbon pack. So none of the standard tracers affect ribbon tactile or visual quality under normal-use lighting."}},
    {"@type": "Question", "name": "What happens when a counterfeit ribbon is detected in the market?", "acceptedAnswer": {"@type": "Answer", "text": "When counterfeit ribbon is detected in the market (via brand-quality complaint, consumer report, or routine market-surveillance), the standard incident-response protocol is: (1) authenticate the suspect ribbon using UV/DNA verification; (2) retrieve the blockchain-provenance record via batch-number; (3) confirm whether the suspect is genuine (mill produced) or counterfeit (off-mill produced); (4) document the case with photos, GPS-location of purchase, retail-channel; (5) file IP-infringement report with brand legal counsel; (6) coordinate with local IP-enforcement on seizure and customs-record; (7) notify mill-side OEM partner for any supply-chain compromise investigation. The specimen-retention protocol (mill retains 5-meter reference of each shipment for 5 years) provides ground-truth comparison."}}"""

BODY_156 = """<p>If your ribbon program touches any luxury or premium brand end-use - beauty &amp; fragrance gift-set, jewelry-box sash, luxury fashion hangtag, premium hospitality amenity, wine &amp; spirits packaging, designer accessory, or any application where counterfeit substitution would damage brand-equity and consumer-trust - the anti-counterfeit tracer &amp; brand-authentication architecture is the difference between a ribbon that protects brand-IP and a ribbon that an unscrupulous supplier can copy and sell on the gray-market within weeks. Most brand-buyer spec sheets stop at visual appearance (color, luster, edge), leaving traceability to "trust the mill" - which for most offshore mills means a single-piece-of-paper mill-CoA that is trivially forgeable and provides no forensic evidence in case of counterfeit incident.</p>

<p>This module - #156 in the Smith Ribbon brand-buyer mill-side architecture series - gives you the anti-counterfeit / brand-authentication playbook: how to specify tracer-fiber (UV-fluorescent marker yarn, DNA-marker yarn) for forensic-level authentication; how to specify blockchain-provenance for supply-chain event-recording; how to specify NFC/QR tag for consumer-facing verification; how to specify specimen-retention protocol for ground-truth comparison; and how to write an authentication spec that protects brand-IP from mill to consumer-hand, with a clear counterfeit-incident-response protocol when an infringement is detected.</p>

<h2>1. Why Anti-Counterfeit Tracer Is a Different Problem from Color &amp; Luster</h2>
<p>Color match (module 148) defines the brand-color identity. Luster (module 155) defines the surface-quality identity. Edge (module 153) defines the edge-finish identity. Anti-counterfeit tracer defines a sixth, independent dimension: how the ribbon can be authenticated as genuinely made at the brand-specified mill, vs counterfeited by an off-mill supplier who copies the visual appearance but lacks the tracer infrastructure. The specs are independent: a ribbon can have perfect color, perfect luster, perfect edge, and still be counterfeit if an off-mill supplier copies the look without the tracer.</p>
<p>Three factors make ribbon anti-counterfeit uniquely challenging:</p>
<ul>
<li><strong>Visual appearance is easily copied:</strong> A mid-tier Chinese mill can buy the same polyester yarn, copy the color formula, copy the luster finishing, copy the edge construction, and produce a ribbon that visually matches the brand-specified mill's output - within 1-2 weeks of receiving a sample. Visual inspection alone is insufficient for authentication.</li>
<li><strong>Tracer infrastructure is the moat:</strong> The anti-counterfeit moat is the tracer infrastructure - UV-fluorescent marker yarn that requires a specific mill-side pigment-supplier, DNA-marker yarn that requires a specific DNA-tag supplier, blockchain-provenance that requires mill-side event-recording discipline. Off-mill suppliers cannot replicate this infrastructure without significant capex and time.</li>
<li><strong>Consumer-facing verification matters:</strong> For premium programs, the consumer (or retail-buyer) should be able to verify authenticity easily - UV blacklight (sold for $20), NFC-tap with phone (free), QR-scan with phone (free). This dual-layer (consumer-friendly + brand-controlled) is the standard architecture.</li>
</ul>

<h2>2. The Six Tracer Architectures &amp; How to Specify Each</h2>
<p>Anti-counterfeit tracer decomposes into six architectures, each addressable with mill-side capability:</p>
<table>
<thead>
<tr><th>Architecture</th><th>Detection Method</th><th>Cost Premium / m</th><th>Security Level</th><th>Best For</th></tr>
</thead>
<tbody>
<tr><td>UV-fluorescent marker yarn</td><td>UV flashlight (375nm)</td><td>$0.02-0.05</td><td>Low-medium</td><td>Mid-tier beauty, hospitality amenity</td></tr>
<tr><td>DNA-marker yarn (synthetic)</td><td>Lab kit or smartphone app</td><td>$0.10-0.40</td><td>Medium-high</td><td>Premium beauty, luxury gift-set</td></tr>
<tr><td>NFC tag (embedded in pack)</td><td>NFC-tap with phone</td><td>$0.30-0.80</td><td>Medium</td><td>Luxury fashion, jewelry-box sash</td></tr>
<tr><td>QR code (printed on pack)</td><td>QR-scan with phone</td><td>$0.01-0.05</td><td>Low</td><td>Volume consumer goods, hospitality</td></tr>
<tr><td>Blockchain-provenance (digital)</td><td>App + batch-number</td><td>$50-150 / shipment</td><td>High (digital)</td><td>Luxury, regulated industries</td></tr>
<tr><td>Physical tag-yarn (metallic, color-shifting)</td><td>Visual + UV</td><td>$0.20-0.60</td><td>Medium-high</td><td>Designer accessory, premium hangtag</td></tr>
</tbody>
</table>

<h2>3. UV-Fluorescent Marker Yarn Specification</h2>
<p>UV-fluorescent marker yarn is the most common and cost-effective anti-counterfeit tracer. The mill weaves one 75D polyester filament dyed with fluorescent pigment (typically blue-green 375nm or red 365nm) every 30-50cm of the warp. Under normal lighting, the tracer yarn is invisible to the naked eye. Under UV blacklight (375nm or 365nm, sold for $20 retail), the tracer yarn glows bright.</p>
<p>Specify UV-marker in the contract as:</p>
<ul>
<li>Tracer frequency: every 30cm (high-security) or every 50cm (standard) of warp</li>
<li>Pigment: blue-green 375nm OR red 365nm OR custom wavelength for brand-exclusivity</li>
<li>Detection: visible only under UV blacklight at specified wavelength</li>
<li>Acceptance: 100% of tracer yarns visible under UV at specified wavelength; 0% visible under normal lighting</li>
</ul>

<h2>4. DNA-Marker Yarn Specification</h2>
<p>DNA-marker yarn uses synthetic-DNA-tagged pigments (commercially available from Applied DNA Sciences or Haelixa) embedded in a tracer filament. The DNA sequence is unique to the brand (or lot), and verification requires either a lab kit (PCR-based, $500-2K) or a smartphone app with fluorescent-reader ($5K-15K custom app). DNA-marker provides the highest level of forensic authentication.</p>
<p>Specify DNA-marker in the contract as:</p>
<ul>
<li>DNA-sequence: brand-unique or lot-unique, 100-300 base-pair synthetic sequence</li>
<li>Tracer frequency: every 50cm warp + every 50cm weft (higher redundancy for premium)</li>
<li>Verification method: PCR lab OR smartphone app, with documented false-positive rate &lt; 0.01%</li>
<li>Acceptance: 99.99% DNA-recovery from reference sample; 0% false-positive on mill-CoA batch-number cross-check</li>
</ul>

<h2>5. NFC / QR Tag &amp; Consumer-Facing Verification</h2>
<p>NFC tag (NFC Forum Type 2, ISO 14443) embedded in the ribbon-pack (NOT in the ribbon itself, to avoid affecting hand-feel) allows consumer to tap phone to pack and verify authenticity. QR code printed on the ribbon-pack allows consumer to scan and verify. Both link to a brand-controlled verification page that shows provenance + batch-number + mill-identity.</p>
<p>Specify NFC/QR in the contract as:</p>
<ul>
<li>NFC tag: Type 2, NTAG215 or NTAG216, 504-888 bytes memory, unique ID per tag</li>
<li>QR code: Version 3-5 (sufficient for URL + batch-number), error-correction Level M</li>
<li>Link target: brand-controlled verification page (HTTPS, no PII, batch-number-only)</li>
<li>Acceptance: 100% tags readable by standard NFC-enabled phone; 100% QR codes scannable by standard QR-reader app</li>
</ul>

<h2>6. Blockchain-Provenance &amp; Digital-Passport</h2>
<p>Blockchain-provenance records each supply-chain event (yarn-spinning, twisting, weaving, finishing, dyeing, inspection, packing, shipping, receipt) as a hash on a permissioned blockchain (Hyperledger Fabric or Quorum). Each event includes timestamp, GPS-location, operator-ID, batch-number, and a digital-photo. The ribbon itself is identified by a unique batch-number that links to the blockchain record.</p>
<p>Specify blockchain-provenance in the contract as:</p>
<ul>
<li>Platform: permissioned blockchain (Hyperledger Fabric preferred)</li>
<li>Event-recording: each supply-chain event from yarn-spinning to shipment</li>
<li>Hash algorithm: SHA-256 minimum (NIST-approved)</li>
<li>Consumer-access: via QR/NFC tag link to brand verification page (read-only)</li>
<li>Retention: 5 years minimum on-chain; reference sample 5 years off-chain</li>
</ul>

<h2>7. Specimen-Retention &amp; Counterfeit-Incident-Response</h2>
<p>For premium programs, require mill-side specimen-retention: 5-meter reference sample of each shipment, sealed in archive-bag with batch-number, stored 5 years minimum at mill QC lab. This provides ground-truth comparison for counterfeit-incident investigation.</p>
<p>Standard counterfeit-incident-response protocol when infringement detected:</p>
<ol>
<li>Authenticate suspect ribbon using UV/DNA verification</li>
<li>Retrieve blockchain-provenance record via batch-number</li>
<li>Confirm genuine (mill produced) vs counterfeit (off-mill produced)</li>
<li>Document with photos, GPS-location, retail-channel</li>
<li>File IP-infringement report with brand legal counsel</li>
<li>Coordinate local IP-enforcement on seizure &amp; customs-record</li>
<li>Notify mill for supply-chain compromise investigation</li>
</ol>

<h2>8. Case Study - Luxury Beauty Brand Authentication Architecture</h2>
<p>A French luxury beauty brand (private-label, 28 SKUs, 1.2M meters annual) was experiencing 8-12% gray-market substitution rate on their gift-set ribbon (counterfeiters copying the visual look and selling through unauthorized channels). After implementing module-156 spec (UV-fluorescent marker yarn every 30cm warp + DNA-marker yarn every 50cm warp + NFC tag on each ribbon-pack + blockchain-provenance on Hyperledger Fabric + specimen-retention 5 years), gray-market substitution rate dropped to &lt; 1% within 6 months. Consumer-facing NFC-tap authentication rate reached 34% on gift-set purchases, providing direct brand-engagement channel.</p>

<h2>9. Smith Ribbon Anti-Counterfeit Capability</h2>
<p>Smith Ribbon's mill (Xiamen, 15,000 m²) supports the full module-156 spec range:</p>
<ul>
<li>UV-fluorescent marker yarn (375nm blue-green / 365nm red / custom wavelengths)</li>
<li>DNA-marker yarn via Applied DNA Sciences or Haelixa (synthetic-DNA-tagged pigments)</li>
<li>NFC tag integration (NTAG215/216, Type 2, ISO 14443)</li>
<li>QR code printing on ribbon-pack (UV-resistant ink, thermal-transfer or inkjet)</li>
<li>Blockchain-provenance integration (Hyperledger Fabric / Quorum, 5-year retention)</li>
<li>Specimen-retention 5 years at mill QC lab (climate-controlled archive)</li>
<li>Mill lab forensic CoA per shipment (UV + DNA verification report)</li>
</ul>

<p><strong>CTA:</strong> For brand-buyer mill-side anti-counterfeit tracer &amp; brand-authentication architecture rollout, contact our OEM engineering desk. Sample yardage with tracer, NFC+QR integration, blockchain-provenance setup, and module-156 spec template are available on request.</p>"""

# ---------- WIRE INTO INDEX / BLOG / SITEMAP ----------

INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")

ENTRIES = [
    {"slot":"am","file":FILE_155,"date":"2026-09-20 10:00 AM","title":TITLE_155,"iso_date":"2026-09-20","desc":DESC_155,"short":"A 2026 B2B ribbon OEM 155-module brand-buyer mill-side yarn-twist, texture &amp; surface-luster specification architecture for global brand procurement directors, brand-product-development-managers, brand-private-label-merchandising-directors, brand-textile-engineers, and OEM mill-side weaving-finishing supervisors. Covers yarn-twist-spec, twist-direction-SZ, yarn-count-Tex-Denier, texture-matrix, luster-gloss-meter-60deg, reflectance-D65, double-knit-vs-single-knit, plied-vs-monofilament, yarn-finish-interaction, and 19-day time-to-yarn-pilot-launch...","mins":"44 min read"},
    {"slot":"pm","file":FILE_156,"date":"2026-09-20 15:00 PM","title":TITLE_156,"iso_date":"2026-09-20","desc":DESC_156,"short":"A 2026 B2B ribbon OEM 156-module brand-buyer mill-side anti-counterfeit tracer &amp; brand-authentication architecture for global brand procurement directors, brand-loss-prevention-directors, brand-IP-counsel, brand-supply-chain-integrity-leads, and OEM mill-side traceability-supervisors. Covers tracer-fiber, UV-fluorescent-marker, nano-tag-DNA-marker, blockchain-provenance, physical-tag-yarn, QR-NFC-tag, authentication-app, specimen-retain, counterfeit-incident-response, and 21-day time-to-tracer-pilot-launch...","mins":"44 min read"},
]

ANCHOR_154_END = (
    '<a href="blog/blog-ribbon-oem-154-module-brand-buyer-mill-side-ribbon-hand-feel-drape-stiffness-tactile-spec-premium-program-kawabata-objective-measurement-architecture-global-brand-procurement-2026-09-20-pm.html" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
    '            </div>'
)

def make_index_card(e):
    return (
        '\n            <div class="news-card">\n'
        f'                <div class="news-date">{e["date"]}</div>\n'
        f'                <h3 class="en-content">{e["title"]}</h3>\n'
        f'                <p class="en-content">{e["desc"]}</p>\n'
        f'                <a href="{e["file"]}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>\n'
        '            </div>'
    )

def update_index():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()
    if ANCHOR_154_END not in html:
        raise SystemExit("ANCHOR_154_END not found in index.html")
    cards = "".join(make_index_card(e) for e in ENTRIES)
    new_html = html.replace(ANCHOR_154_END, ANCHOR_154_END + cards, 1)
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"index.html: {len(html):,} -> {len(new_html):,} bytes")

def make_blog_card(e):
    return (
        '\n            <article class="blog-card">\n'
        f'                <div class="blog-date">{e["date"]}</div>\n'
        f'                <h3><a href="{e["file"]}">{e["title"]}</a></h3>\n'
        f'                <p>{e["short"]}</p>\n'
        f'                <a href="{e["file"]}" class="blog-read-more">Read More &rarr;</a>\n'
        '            </article>'
    )

def update_blog():
    with open(BLOG_HTML, "r", encoding="utf-8") as f:
        html = f.read()
    anchor = 'blog/blog-ribbon-oem-154-module-brand-buyer-mill-side-ribbon-hand-feel-drape-stiffness-tactile-spec-premium-program-kawabata-objective-measurement-architecture-global-brand-procurement-2026-09-20-pm.html'
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor) + r'" class="blog-read-more">Read More &rarr;</a>\s*</article>)'
    )
    if not pattern.search(html):
        raise SystemExit("154 anchor not found in blog.html")
    cards = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = pattern.sub(lambda m: m.group(1) + cards, html, count=1)
    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"blog.html: {len(html):,} -> {len(new_html):,} bytes")

SITEMAP_URL_TEMPLATE = (
    '    <url>\n'
    '        <loc>{loc}</loc>\n'
    '        <lastmod>{lastmod}</lastmod>\n'
    '        <changefreq>weekly</changefreq>\n'
    '        <priority>0.9</priority>\n'
    '    </url>'
)

def update_sitemap():
    with open(SITEMAP, "r", encoding="utf-8") as f:
        xml = f.read()
    if "</urlset>" not in xml:
        raise SystemExit("</urlset> not found in sitemap.xml")
    blocks = []
    for e in ENTRIES:
        loc = f"{SITE_URL}/{e['file']}"
        blocks.append(SITEMAP_URL_TEMPLATE.format(loc=loc, lastmod=e["iso_date"]))
    insertion = "\n" + "\n".join(blocks) + "\n"
    new_xml = xml.replace("</urlset>", insertion + "</urlset>", 1)
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(new_xml)
    print(f"sitemap.xml: {len(xml):,} -> {len(new_xml):,} bytes (+{len(ENTRIES)} URLs)")

# ---------- WRITE ARTICLES ----------

def write_article(num, filename, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc):
    path = os.path.join(WEB, filename)
    html = article_html(num, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"WROTE {filename}: {len(html):,} bytes")

def main():
    write_article(NUM_155, FILE_155, DISPLAY_TITLE_155, DESC_155, CANONICAL_155, AM_TIME, TAGS_155, KEYWORDS_155, FAQS_155, BODY_155,
                  "Ribbon Yarn-Twist, Texture & Surface-Luster Specification Architecture 2026",
                  DESC_155.replace('&amp;','&'),
                  "Ribbon Yarn-Twist & Surface-Luster Specification Architecture | B2B OEM 2026",
                  "B2B ribbon OEM 155-module brand-buyer mill-side yarn-twist, texture & surface-luster specification architecture. TM, twist-direction, yarn-count, gloss-meter 60deg per ASTM D523. 19-day pilot-launch. Smith Ribbon OEM since 2004.")
    write_article(NUM_156, FILE_156, DISPLAY_TITLE_156, DESC_156, CANONICAL_156, PM_TIME, TAGS_156, KEYWORDS_156, FAQS_156, BODY_156,
                  "Ribbon Anti-Counterfeit Tracer & Brand-Authentication Architecture 2026",
                  DESC_156.replace('&amp;','&'),
                  "Ribbon Anti-Counterfeit Tracer & Brand-Authentication Architecture | B2B OEM 2026",
                  "B2B ribbon OEM 156-module brand-buyer mill-side anti-counterfeit tracer & brand-authentication architecture. UV-marker, DNA-marker, NFC/QR, blockchain-provenance. 21-day pilot-launch. Smith Ribbon OEM since 2004.")
    update_index()
    update_blog()
    update_sitemap()
    print("\nAll wired. Ready for git commit & push.")

if __name__ == "__main__":
    main()
