#!/usr/bin/env python3
"""Build 2026-09-24 cron DOUBLE B2B articles:
- AM (Module 165): Brand-Initiated Co-Innovation Lab Architecture
- PM (Module 166): Mill-Side Make-or-Buy Decision Framework on Bow-Assembly
"""
import subprocess, os, re

WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
ISO_AM = "2026-09-24T07:00:00+00:00"
ISO_PM = "2026-09-24T15:00:00+00:00"
DISPLAY_AM = "September 24, 2026 (AM)"
DISPLAY_PM = "September 24, 2026 (PM)"
FILE_165 = "blog/blog-ribbon-oem-165-module-brand-buyer-mill-side-brand-initiated-coinnovation-lab-architecture-global-brand-procurement-2026-09-24-am.html"
FILE_166 = "blog/blog-ribbon-oem-166-module-brand-buyer-mill-side-make-or-buy-bow-assembly-hand-tie-vs-pre-tied-architecture-global-brand-procurement-2026-09-24-pm.html"
CANONICAL_165 = f"{SITE_URL}/{FILE_165}"
CANONICAL_166 = f"{SITE_URL}/{FILE_166}"

DISPLAY_TITLE_165 = "Brand-Initiated Co-Innovation Lab Architecture for Ribbon OEM 2026"
DISPLAY_TITLE_166 = "Mill-Side Make-or-Buy Decision Framework on Bow-Assembly & Hand-Tie vs Pre-Tied 2026"

DESC_165 = "B2B ribbon OEM 165-module brand-buyer mill-side brand-initiated co-innovation lab architecture. Trend-forecasting, rapid-prototyping, sustainability-track, brand-team residency. 30-day pilot. Smith Ribbon OEM since 2004."
DESC_166 = "B2B ribbon OEM 166-module brand-buyer mill-side make-or-buy decision framework on bow-assembly: hand-tie vs pre-tied, in-house vs outsourced, automation capex, total-cost comparison. Smith Ribbon OEM since 2004."

TAGS_165 = "Co-Innovation Lab, Brand Procurement, Rapid Prototyping, OEM Ribbon, Trend Forecasting"
TAGS_166 = "Make or Buy, Bow Assembly, Hand Tie, Pre-Tied Bow, OEM Ribbon"
KEYWORDS_165 = "brand co-innovation lab ribbon, rapid prototyping ribbon OEM, trend forecasting mill, brand procurement innovation"
KEYWORDS_166 = "make or buy bow assembly, hand tie vs pre-tied bow, bow assembly automation, OEM bow manufacturing, brand procurement"

FAQS_165 = '[{"q":"What is a brand-initiated co-innovation lab in ribbon OEM?","a":"A co-innovation lab is a dedicated space inside or alongside the mill where the brand team runs trend-forecasting research, rapid-prototype runs, sustainability track pilots, and joint material exploration with mill engineers. Unlike a one-off development PO, the lab is a standing relationship with quarterly business reviews, shared IP protocols, and an annual roadmap."},{"q":"What are the four typical tracks inside a co-innovation lab?","a":"Four parallel tracks: (1) Trend & Color Forecasting; (2) Robust Prototyping; (3) Sustainability; (4) Automation / Efficiency. Each track has its own quarterly KPI."},{"q":"How does the lab protect IP for both sides?","a":"Three mechanisms: Background-IP stays with originator; Foreground-IP is co-owned with negotiated exclusive-license; Third-party-IP requires pre-agreed license terms. Signed before lab launch."},{"q":"What does a 30-day pilot-launch sequence look like?","a":"Days 1-5: scope, IP-protocol signature, lab-team composition. Days 6-12: tooling & sample-base provisioning, Pantone library refresh. Days 13-20: trend-track prototypes + sustainability sample. Days 21-25: brand-team residency week on-site. Days 26-30: first quarterly review, roadmap sign-off."},{"q":"What ROI can a brand expect from a co-innovation lab?","a":"Typical brand-side ROI ranges 3-8x annual lab investment within 24 months, from shorter time-to-market, lower per-unit cost, higher sell-through, and reduced sustainability-claim substantiation cost."}]'

FAQS_166 = '[{"q":"What is the make-or-buy decision for bow-assembly in ribbon OEM?","a":"Whether the brand assembles pre-tied bows in-house, outsources to a dedicated bow-assembly house, or uses mill-side offering. Decision factors: annual volume, complexity, labor geography, capex, SKU flexibility."},{"q":"What is the cost difference between hand-tied and pre-tied bows?","a":"Hand-tied: $0.40-$1.20 per piece direct labor. Pre-tied: $0.08-$0.35 per piece. Hand-tied has 3-7% defect rate; pre-tied 1-2%."},{"q":"What capex is needed for in-house bow assembly automation?","a":"Manual $2-8K, semi-auto $25-80K, fully-auto $250-800K. Payback: manual 6mo, semi-auto 18-24mo, fully-auto 36-48mo."},{"q":"How does the decision affect sustainability reporting?","a":"In-house gives direct visibility. Outsourced requires disclosure from partner; gaps undermine claims. Mill-side offering inherits existing sustainability program with lowest reporting friction."},{"q":"What contractual protections should a brand put in place?","a":"Five must-have clauses: volume commitment with take-or-pay, defect-rate cap with scorecard penalty, IP protection with liquidated damages, capacity reservation during Q4 peak, exit-right with tooling transfer."}]'

BODY_165 = """<div class="container">
<p>Most ribbon OEM relationships are transactional: brand sends a spec, mill sends a sample, brand sends a PO. The brand-initiated co-innovation lab inverts that pattern. A standing lab at or alongside the mill turns innovation into a structural capability — trend-forecasting, rapid prototyping, sustainability-track, and automation become quarterly KPI-tracked workstreams, not sporadic fire-drills. Smith Ribbon's 165-module architecture is a 30-day pilot-launch framework covering lab governance, four parallel tracks, IP protocols, and ROI economics.</p>

<h2>1. The Business Case: Why Stand Up a Co-Innovation Lab?</h2>
<p>Brand buyers in 2026 face a structural squeeze: trend cycles compress from 18 months to 6-9 months; sustainability claims must be substantiated not asserted; SKU proliferation explodes as personalization becomes table-stakes; and retailer-vendor-compliance audits demand documented evidence of innovation pipelines. A transactional OEM relationship cannot answer these in time. The lab is the structural answer.</p>

<h3>1.1 The 4 Innovation Pressures on Brand Buyers</h3>
<ul>
<li><strong>Trend Compression:</strong> SS26 color stories must be locked by Q4 prior year; lab lead-time of 4-6 weeks is the new normal.</li>
<li><strong>Sustainability Substantiation:</strong> every recycled-content, bio-based, or closed-loop claim must trace to a verifiable supply chain.</li>
<li><strong>SKU Proliferation:</strong> retailer-specific color stories, personalization programs, co-branded capsules each add 5-20 SKUs per cycle.</li>
<li><strong>Compliance Audit Pressure:</strong> retailer-vendor audits increasingly require documented innovation pipelines, not just CSR statements.</li>
</ul>

<h2>2. The Four Parallel Tracks</h2>
<p>A co-innovation lab runs four tracks in parallel. Each track has its own quarterly KPI, its own budget envelope, and its own IP protocol.</p>

<h3>2.1 Track A — Trend &amp; Color Forecasting</h3>
<p>Quarterly trend presentation aligned to brand merchandising calendar: Pantone+ palette refresh, metallic and iridescent stories, mood-board prototypes, and 3-5 directional concepts per cycle. Lead-time 12-18 months; output: signed-off direction by week 14-15 of the prior cycle.</p>

<h3>2.2 Track B — Rapid Prototyping</h3>
<p>7-day sample turnaround SLA on new constructions, finishes, or embellishments. Sample-base of 50-100 stock SKU constructions maintained; sub-7-day bespoke run for a new construction. KPI: 95%+ of requests delivered within 7 calendar days.</p>

<h3>2.3 Track C — Sustainability Track</h3>
<p>Recycled-content exploration (RPET, GRS-certified, post-consumer waste), bio-based fiber pilots (bamboo, hemp, lyocell variants), closed-loop and take-back programs, OEKO-TEX claim-substantiation support. KPI: 2-3 new sustainability-validated SKUs per quarter, each with claim-substantiation dossier.</p>

<h3>2.4 Track D — Automation &amp; Efficiency</h3>
<p>Bow-assembly line speed-up, AI-vision quality inspection, RFID spool-tracking, automated packaging. Each quarter ships 1-2 production-floor improvements with measured ROI. KPI: $0.005-$0.02 per piece cost-takeout per track-quarter.</p>

<h2>3. Lab Governance &amp; Team Composition</h2>
<p>The lab is governed by a joint steering committee meeting quarterly: brand-side merchandising, design, sustainability, and procurement leads; mill-side design, R&amp;D, production-engineering, and sales leads. Decision rights are pre-agreed on a RACI matrix — brand has final say on aesthetic and commercial questions, mill has final say on manufacturability and capacity questions.</p>

<table>
<thead><tr><th>Role</th><th>Brand Side</th><th>Mill Side</th></tr></thead>
<tbody>
<tr><td>Lab Director (Joint)</td><td>Brand-design lead</td><td>Mill R&amp;D head</td></tr>
<tr><td>Trend Lead</td><td>Brand merchandising</td><td>Mill color-lab manager</td></tr>
<tr><td>Prototype Lead</td><td>Brand product dev</td><td>Mill sample-room supervisor</td></tr>
<tr><td>Sustainability Lead</td><td>Brand ESG / CSR</td><td>Mill OEKO-TEX coordinator</td></tr>
<tr><td>Automation Lead</td><td>Brand procurement</td><td>Mill production engineering</td></tr>
</tbody>
</table>

<h2>4. IP Protocol — Three Mechanisms</h2>
<p>The IP protocol is signed before the lab launches, not after the first dispute. Three mechanisms protect both sides:</p>
<ul>
<li><strong>Background-IP:</strong> stays with originator. Pre-existing brand trade dress remains brand. Pre-existing mill processes remain mill.</li>
<li><strong>Foreground-IP:</strong> co-developed in lab is typically co-owned with negotiated exclusive-license to brand for the field-of-use (e.g., brand has exclusive ribbon rights; mill retains process IP for non-ribbon applications).</li>
<li><strong>Third-Party-IP:</strong> brought in (e.g., third-party dye supplier, external design studio) requires pre-agreed license terms before project starts.</li>
</ul>

<h2>5. The 30-Day Pilot-Launch Sequence</h2>
<p>Smith Ribbon recommends a 30-day pilot-launch to prove the lab before scaling:</p>
<ol>
<li><strong>Days 1-5:</strong> scope, IP-protocol signature, lab-team composition, RACI matrix.</li>
<li><strong>Days 6-12:</strong> tooling &amp; sample-base provisioning, Pantone library refresh, joint trend-walk.</li>
<li><strong>Days 13-20:</strong> first two trend-track prototypes (one color, one construction) + first sustainability sample.</li>
<li><strong>Days 21-25:</strong> brand-team residency week on-site at mill — designers, sustainability, procurement all visit.</li>
<li><strong>Days 26-30:</strong> first quarterly review, KPI dashboard, roadmap sign-off for next quarter.</li>
</ol>

<h2>6. ROI Economics &amp; Brand-Side Value Capture</h2>
<p>Typical brand-side ROI ranges 3-8x annual lab investment within 24 months. Gains materialize as:</p>
<ul>
<li><strong>40-60% shorter time-to-market</strong> on new SKUs — from trend-lock to shelf-ready in 8-12 weeks instead of 16-24.</li>
<li><strong>15-25% lower per-unit cost</strong> on co-developed constructions vs off-the-shelf catalog ribbon.</li>
<li><strong>20-30% higher sell-through</strong> on trend-validated launches vs brand-only trend calls.</li>
<li><strong>50%+ reduction in sustainability-claim substantiation cost</strong> via pre-developed recycled / bio-based track.</li>
<li><strong>$0.005-$0.02 per piece cost-takeout</strong> per automation track-quarter.</li>
</ul>

<h2>7. Connection to Multi-Supplier Resilience</h2>
<p>Module 165 closes the loop on dual-sourcing resilience. The co-innovation lab at the primary mill becomes the technical-benchmark source; the secondary mill is benchmarked against the lab's output. Without the lab, dual-sourcing collapses into visual-drift between mills; with the lab, dual-sourcing is anchored to a single innovation pipeline.</p>

<div class="cta">
<a href="/contact.html">Talk to Smith Ribbon about a Brand-Initiated Co-Innovation Lab &rarr;</a>
</div>
</div>
"""

BODY_166 = """<div class="container">
<p>The make-or-buy decision on bow-assembly is one of the most consequential structural choices a brand buyer makes in ribbon OEM. Get it right, and unit-cost drops 30-50% while defect-rate halves. Get it wrong, and the brand is locked into either manual-labor escalation, stranded automation capex, or supplier-margin leakage. Smith Ribbon's 166-module framework gives brand buyers a structured decision matrix across volume, complexity, geography, capex, sustainability, and IP — covering hand-tie vs pre-tied, in-house vs outsourced, and mill-side offering.</p>

<h2>1. The Three Bow-Assembly Models</h2>
<p>Three structural models exist; each has a sweet spot and a failure mode:</p>

<table>
<thead><tr><th>Model</th><th>Sweet-Spot</th><th>Failure Mode</th></tr></thead>
<tbody>
<tr><td>Hand-Tied (artisan)</td><td>Premium / luxury / signature irregularity</td><td>Volume ceiling, high defect rate</td></tr>
<tr><td>Pre-Tied Manual / Semi-Auto</td><td>Mid-volume retail 50K-500K pieces</td><td>Capex payback risk if demand softens</td></tr>
<tr><td>Fully-Auto Assembly Line</td><td>Mass retail above 1M pieces</td><td>SKU flexibility constraint</td></tr>
</tbody>
</table>

<h2>2. The Volume Decision Tree</h2>
<p>Annual volume is the single largest driver. Below ~50K pieces, outsourced assembly is almost always optimal. 50K-500K pieces is the contested middle where brand geography, labor cost, and SKU complexity decide. Above 500K pieces, in-house or dedicated partner is the structural choice.</p>

<h3>2.1 Annual Volume &lt; 50K Pieces — Outsource</h3>
<p>Outsourced bow-assembly via a dedicated bow-house or via the mill's own bow-assembly offering is the dominant choice. Capex is zero; per-piece cost is $0.40-$1.20 hand-tied or $0.08-$0.35 pre-tied; defect rate is supplier-managed; SKU flexibility is high. The brand pays for flexibility and avoids capex risk.</p>

<h3>2.2 Annual Volume 50K-500K Pieces — Make-or-Buy Decision</h3>
<p>This is the contested zone. The decision pivots on:</p>
<ul>
<li><strong>Geography &amp; Labor Cost:</strong> if brand operates in high-labor-cost geography (US, EU, JP, KR), outsource to Asia-side mill offering. If brand operates in moderate-labor-cost geography, in-house semi-auto may pencil out.</li>
<li><strong>SKU Complexity:</strong> if &gt;30 active bow SKUs per season with frequent style refresh, outsource for flexibility. If &lt;10 stable SKUs with annual refresh, in-house semi-auto amortizes capex.</li>
<li><strong>Lead-Time Pressure:</strong> if Q4 holiday cascade requires &lt;14-day reorder, in-house or mill-side offering wins over third-party.</li>
</ul>

<h3>2.3 Annual Volume &gt; 500K Pieces — In-House or Dedicated Partner</h3>
<p>At this scale, fully-auto or dedicated bow-house partnership is the structural answer. Capex of $250-800K per fully-auto line pays back in 36-48 months at high-volume economics; per-piece cost drops to $0.04-$0.15. The brand gains direct QC visibility and ESG narrative control.</p>

<h2>3. Hand-Tie vs Pre-Tied — The Aesthetic vs Economic Decision</h2>
<p>Hand-tied and pre-tied bows are not direct substitutes — they serve different brand positions.</p>

<table>
<thead><tr><th>Dimension</th><th>Hand-Tied</th><th>Pre-Tied</th></tr></thead>
<tbody>
<tr><td>Direct Labor</td><td>$0.40-$1.20 / piece</td><td>$0.08-$0.35 / piece</td></tr>
<tr><td>Defect Rate</td><td>3-7%</td><td>1-2%</td></tr>
<tr><td>QC Method</td><td>100% visual required</td><td>AQL sampling viable</td></tr>
<tr><td>Aesthetic</td><td>Slight irregularity = signature</td><td>Uniformity = retail-ready</td></tr>
<tr><td>Volume Ceiling</td><td>~50K pieces / season</td><td>Unlimited at scale</td></tr>
<tr><td>Sustainability</td><td>Lower energy, no machine capex</td><td>Higher energy, machine-capex amortized</td></tr>
</tbody>
</table>

<p>Premium and luxury brands often pay the hand-tie premium because the slight irregularity is part of the value proposition. Mass retail and value-positioned brands default to pre-tied for unit-cost economics. Some brands run a hybrid: pre-tied for core SKUs, hand-tied for limited-edition / capsule collections.</p>

<h2>4. Capex Tiers &amp; Payback Thresholds</h2>
<p>Three capex tiers for in-house bow assembly:</p>
<ul>
<li><strong>Manual table-set-up:</strong> $2-8K per workstation, 200-400 pieces/shift per worker. Suited for sample-runs and micro-batch premium. Payback within 6 months.</li>
<li><strong>Semi-auto bow machines:</strong> $25-80K per line, 1,500-3,500 pieces/shift. Suited for 50K-500K annual volume. Payback 18-24 months.</li>
<li><strong>Fully-auto bow assembly line with vision QC:</strong> $250-800K per line, 8,000-15,000 pieces/shift. Suited for above 1M annual volume. Payback 36-48 months.</li>
</ul>

<h2>5. Sustainability &amp; ESG Implications</h2>
<p>The make-or-buy decision has measurable sustainability consequences:</p>
<ul>
<li><strong>Labor Disclosure:</strong> in-house assembly gives direct visibility into labor conditions and energy use — easier ESG reporting. Outsourced assembly requires the brand to obtain labor and energy disclosure from the partner; gaps in disclosure can undermine sustainability claims.</li>
<li><strong>Carbon Footprint:</strong> in-urban in-house assembly inflates scope 1+2; outsourced to a coastal mill deflates scope 3 freight per piece. Net carbon per piece varies 15-40% by model.</li>
<li><strong>Material Waste:</strong> in-house assembly lets the brand capture trim-waste for closed-loop. Outsourced assembly requires explicit trim-recovery clauses in the partner contract.</li>
<li><strong>Mill-Side Offering:</strong> inherits the mill's existing sustainability program (OEKO-TEX, GRS, BSCI/SMETA audits) — typically the lowest reporting friction.</li>
</ul>

<h2>6. Five Must-Have Contractual Protections</h2>
<ol>
<li><strong>Volume Commitment with Take-or-Pay Threshold:</strong> protects capex payback. Typical threshold: 70-80% of forecast volume; shortfall triggers take-or-pay invoice.</li>
<li><strong>Defect-Rate Cap with Vendor Scorecard Penalty:</strong> defect cap typically 1.5-2.5% for pre-tied, 5-7% for hand-tied. Exceedance triggers vendor-scorecard penalty schedule.</li>
<li><strong>IP Protection on Bow-Design Silhouette:</strong> with liquidated damages for unauthorized use. Brand-owned bow dies tie into the brand-owned tooling framework.</li>
<li><strong>Capacity Reservation during Peak Season (Q4):</strong> with cascade-priority rules. Critical for holiday programs where 30-60% of annual volume ships in 8 weeks.</li>
<li><strong>Exit-Right with Tooling Transfer or Graceful Wind-Down:</strong> on 90-day notice. Tooling transfers per the brand-owned-tooling asset-custody framework; ongoing POs ship.</li>
</ol>

<h2>7. Decision Matrix Summary</h2>
<p>A quick reference for brand buyers facing the make-or-buy decision:</p>
<table>
<thead><tr><th>Annual Volume</th><th>Geography</th><th>SKU Complexity</th><th>Recommended Model</th></tr></thead>
<tbody>
<tr><td>&lt;50K</td><td>Any</td><td>Any</td><td>Outsource (mill-side or bow-house)</td></tr>
<tr><td>50K-500K</td><td>High-labor-cost</td><td>High (&gt;30 SKUs)</td><td>Outsource to Asia-side mill</td></tr>
<tr><td>50K-500K</td><td>Moderate-labor-cost</td><td>Low (&lt;10 SKUs)</td><td>In-house semi-auto</td></tr>
<tr><td>&gt;500K</td><td>Any</td><td>Any</td><td>In-house fully-auto or dedicated partner</td></tr>
<tr><td>Premium / luxury</td><td>Any</td><td>Hand-tie signature</td><td>Hand-tied artisan, dedicated partner</td></tr>
</tbody>
</table>

<div class="cta">
<a href="/contact.html">Request the Bow-Assembly Make-or-Buy Decision Worksheet &rarr;</a>
</div>
</div>
"""

# ---------- STYLE ----------
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

def article_html(num, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc, date_label):
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
    "url": "https://smithribbon.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Xiamen Smith Ribbon & Bow Co., Ltd.",
    "logo": {
      "@type": "ImageObject",
      "url": "https://smithribbon.com/banner.png"
    }
  },
  "datePublished": "__PUBTIME__",
  "dateModified": "__PUBTIME__",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "__CANONICAL__"
  },
  "keywords": "__KW__",
  "articleSection": "B2B Ribbon Procurement"
}
</script>

<!-- FAQ Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": __FAQS__
}
</script>

<style>__STYLE__</style>
</head>
<body>
<header>
<a href="https://smithribbon.com">&larr; Smith Ribbon OEM B2B Knowledge Base</a>
</header>

<section class="hero">
<h1>__TITLE__</h1>
<div class="meta">__DATE__ &middot; Module 16__NUM__ &middot; 14&nbsp;min read &middot; B2B Ribbon Procurement</div>
<div style="margin-top:14px;">
<span class="tag">__TAG0__</span>
<span class="tag">__TAG1__</span>
<span class="tag">__TAG2__</span>
</div>
</section>

__BODY__
</body>
</html>
"""
    return template.replace("__TITLE__", title_display)\
        .replace("__DESC__", desc)\
        .replace("__KW__", keywords)\
        .replace("__CANONICAL__", canonical)\
        .replace("__OGT__", og_title)\
        .replace("__OGD__", og_desc)\
        .replace("__TWT__", tw_title)\
        .replace("__TWD__", tw_desc)\
        .replace("__PUBTIME__", pubtime)\
        .replace("__TAG0__", tags.split(",")[0].strip())\
        .replace("__TAG1__", tags.split(",")[1].strip() if "," in tags else tags)\
        .replace("__TAG2__", tags.split(",")[2].strip() if tags.count(",") >= 2 else "OEM Ribbon")\
        .replace("__DATE__", date_label)\
        .replace("__NUM__", str(num))\
        .replace("__FAQS__", faqs_json)\
        .replace("__BODY__", body_html + FOOTER_HTML)\
        .replace("__STYLE__", STYLE)


# ---------- INDEX / BLOG / SITEMAP WIRING ----------
INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")
ANCHOR_164_END = "blog/blog-ribbon-oem-164-module-brand-buyer-mill-side-brand-owned-tooling-die-cylinder-asset-custody-framework-global-brand-procurement-2026-09-23-pm.html"

ENTRIES = [
    {
        "file": FILE_165,
        "title": "Brand-Initiated Co-Innovation Lab Architecture for Ribbon OEM",
        "desc": "B2B ribbon OEM 165-module mill-side brand-initiated co-innovation lab architecture: 4 parallel tracks (trend, prototype, sustainability, automation), IP protocols, 30-day pilot.",
        "short": "Brand-initiated co-innovation lab at the mill — 4 parallel tracks (trend, prototype, sustainability, automation), IP protocols, 30-day pilot-launch.",
        "date": DISPLAY_AM,
        "iso_date": ISO_AM,
        "num": 5,
    },
    {
        "file": FILE_166,
        "title": "Mill-Side Make-or-Buy Decision Framework on Bow-Assembly & Hand-Tie vs Pre-Tied",
        "desc": "B2B ribbon OEM 166-module brand-buyer make-or-buy decision framework on bow-assembly: hand-tie vs pre-tied, in-house vs outsourced, automation capex, total-cost comparison.",
        "short": "Make-or-buy decision framework on bow-assembly — hand-tie vs pre-tied, in-house vs outsourced, capex tiers, ESG implications, contractual protections.",
        "date": DISPLAY_PM,
        "iso_date": ISO_PM,
        "num": 6,
    },
]


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
    if ANCHOR_164_END not in html:
        raise SystemExit(f"ANCHOR_164_END ({ANCHOR_164_END}) not found in index.html")
    # Find the </div> closing the news-card containing the 164 anchor
    idx = html.find(f'href="{ANCHOR_164_END}"')
    if idx < 0:
        raise SystemExit("anchor not found in index.html")
    close_idx = html.find('</div>', idx)
    insertion_point = close_idx + len('</div>')
    cards = "".join(make_index_card(e) for e in ENTRIES)
    new_html = html[:insertion_point] + cards + html[insertion_point:]
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
    # blog.html's last entry should be 164 (2026-09-23 PM) — use that as anchor
    pattern = re.compile(
        r'(<a href="' + re.escape(ANCHOR_164_END) + r'" class="blog-read-more">Read More &rarr;</a>\s*</article>)'
    )
    if not pattern.search(html):
        raise SystemExit("blog anchor (164) not found in blog.html")
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
        lastmod = e["iso_date"].split("T")[0]
        blocks.append(SITEMAP_URL_TEMPLATE.format(loc=loc, lastmod=lastmod))
    insertion = "\n" + "\n".join(blocks) + "\n"
    new_xml = xml.replace("</urlset>", insertion + "</urlset>", 1)
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(new_xml)
    print(f"sitemap.xml: {len(xml):,} -> {len(new_xml):,} bytes (+{len(ENTRIES)} URLs)")


def write_article(e, og_title, og_desc, tw_title, tw_desc):
    path = os.path.join(WEB, e["file"])
    canonical = f"{SITE_URL}/{e['file']}"
    pubtime = e["iso_date"]
    if e["num"] == 5:
        tags = TAGS_165
        keywords = KEYWORDS_165
        faqs_json = FAQS_165
        body = BODY_165
        title_display = DISPLAY_TITLE_165
    else:
        tags = TAGS_166
        keywords = KEYWORDS_166
        faqs_json = FAQS_166
        body = BODY_166
        title_display = DISPLAY_TITLE_166
    html = article_html(
        e["num"], title_display, e["desc"], canonical, pubtime,
        tags, keywords, faqs_json, body,
        og_title, og_desc, tw_title, tw_desc, e["date"],
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"WROTE {e['file']}: {len(html):,} bytes")
    root_filename = e["file"].replace("blog/", "", 1)
    root_path = os.path.join(WEB, root_filename)
    if root_path != path:
        with open(root_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  MIRRORED to root: {root_filename}")


def main():
    # AM 165
    write_article(
        ENTRIES[0],
        "Brand-Initiated Co-Innovation Lab Architecture for Ribbon OEM 2026",
        "B2B ribbon OEM 165-module brand-buyer mill-side brand-initiated co-innovation lab architecture. Trend, prototype, sustainability, automation tracks. Smith Ribbon OEM since 2004.",
        "Co-Innovation Lab Architecture for Ribbon OEM | B2B 2026",
        "B2B ribbon OEM 165-module brand-buyer mill-side brand-initiated co-innovation lab. 4 parallel tracks, IP protocols, 30-day pilot. Smith Ribbon since 2004.",
    )
    # PM 166
    write_article(
        ENTRIES[1],
        "Mill-Side Make-or-Buy Decision Framework on Bow-Assembly 2026",
        "B2B ribbon OEM 166-module brand-buyer make-or-buy decision framework on bow-assembly: hand-tie vs pre-tied, in-house vs outsourced, automation capex, total-cost comparison. Smith Ribbon OEM since 2004.",
        "Bow-Assembly Make-or-Buy Decision Framework | B2B OEM 2026",
        "B2B ribbon OEM 166-module make-or-buy framework on bow-assembly. Hand-tie vs pre-tied, in-house vs outsourced, capex, ESG, contractual protections. Smith Ribbon since 2004.",
    )
    update_index()
    update_blog()
    update_sitemap()
    print("\nAll wired. Ready for git commit & push.")


if __name__ == "__main__":
    main()
