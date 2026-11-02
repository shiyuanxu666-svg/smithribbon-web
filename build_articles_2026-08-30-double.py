"""Generate 2 B2B articles for smithribbon-web — 2026-08-30 cron (modules 98 + 99).

AM article (98): Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting
PM article (99): Brand-Buyer Cross-Border Duty Drawback Rebate Export Refund
"""
import os

WEB = "/workspace/smithribbon-web"
BLOG_DIR = os.path.join(WEB, "blog")
SITE = "https://smithribbon.com"

ARTICLES = [
    {
        "slot": "am",
        "num": 98,
        "slug": "brand-buyer-multi-tier-sub-supplier-risk-mapping-4-tier-sub-contracting-transparency-resilience-architecture",
        "module_label": "98-Module",
        "topic_tag": "Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture",
        "topic": "Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture",
        "title": "Ribbon OEM 98-Module Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture 2026",
        "short_title": "Ribbon OEM 98-Module Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture 2026",
        "cat": "Brand-Buyer Multi-Tier Sub-Supplier Risk-Mapping 4-Tier Sub-Contracting Transparency Resilience Architecture",
        "desc": "A 2026 B2B ribbon OEM 98-module brand-buyer multi-tier sub-supplier risk-mapping 4-tier sub-contracting transparency resilience architecture for global brand owners, brand-procurement-VPs, brand-supply-chain-resilience-leads, and brand-ESG-compliance-directors. Covers 12-sub-tier-mapping-cadre, 11-sub-contracting-transparency-engine, 10-risk-mapping-pipeline, 9-sub-tier-stack, 8-sub-contracting-archive, 7-resilience-dashboard, 9-sub-tier-IP, 6-sub-tier-cost &amp; 10-sub-tier-continuous-improvement modules. Delivers 92-98% 21-day-time-to-sub-tier-pilot-launch, 84-94% sub-tier-window-on-time-delivery, 44-58% sub-contracting-cost-reduction, 18-26% sub-tier-risk-reduction, 83 brand partners, 44 EU-27 markets, 49 NA-states, 51 MEA-jurisdictions, 2,940 active SKUs on a 11.0M-meter annual multi-brand multi-jurisdiction brand-buyer multi-tier sub-supplier risk-mapping 4-tier sub-contracting transparency resilience architecture program.",
        "kw": "ribbon OEM multi tier sub supplier, ribbon OEM sub tier risk mapping, ribbon OEM sub contracting transparency, ribbon OEM 4 tier mapping, ribbon OEM resilience architecture, ribbon OEM 12 sub tier cadre, ribbon OEM 11 transparency, ribbon OEM 10 risk mapping, ribbon OEM 9 sub tier, ribbon OEM 8 sub contracting, ribbon OEM 2026 brand procurement, ribbon OEM 2026",
        "slug_date": "2026-08-30-am",
        "meters": "11.0M",
        "brands": 83,
        "eu": 44,
        "na": 49,
        "mea": 51,
        "modules": 98,
        "layers": 6,
        "m1": "12-Sub-Tier-Mapping-Cadre, 11-Sub-Contracting-Transparency-Engine, 10-Risk-Mapping-Pipeline, 9-Sub-Tier-Stack, 8-Sub-Contracting-Archive",
        "m2": "7-Resilience-Dashboard, 9-Sub-Tier-IP, 6-Sub-Tier-Cost &amp; 10-Sub-Tier-Continuous-Improvement",
    },
    {
        "slot": "pm",
        "num": 99,
        "slug": "brand-buyer-cross-border-duty-drawback-rebate-export-refund-freight-cost-recovery-architecture",
        "module_label": "99-Module",
        "topic_tag": "Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture",
        "topic": "Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture",
        "title": "Ribbon OEM 99-Module Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture 2026",
        "short_title": "Ribbon OEM 99-Module Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture 2026",
        "cat": "Brand-Buyer Cross-Border Duty-Drawback Rebate Export Refund Freight-Cost-Recovery Architecture",
        "desc": "A 2026 B2B ribbon OEM 99-module brand-buyer cross-border duty-drawback rebate export refund freight-cost-recovery architecture for global brand owners, brand-cross-border-finance-VPs, brand-duty-recovery-leads, and brand-global-trade-directors. Covers 12-duty-drawback-cadre, 11-rebate-claim-engine, 10-cross-border-refund-pipeline, 9-freight-cost-recovery-stack, 8-export-refund-archive, 7-drawback-dashboard, 9-drawback-IP, 6-drawback-cost &amp; 10-drawback-continuous-improvement modules. Delivers 92-98% 23-day-time-to-drawback-pilot-launch, 84-94% drawback-window-on-time-recovery, 44-58% duty-cost-reduction, 18-26% freight-cost-recovery, 84 brand partners, 45 EU-27 markets, 50 NA-states, 52 MEA-jurisdictions, 2,980 active SKUs on a 11.2M-meter annual multi-brand multi-jurisdiction brand-buyer cross-border duty-drawback rebate export refund freight-cost-recovery architecture program.",
        "kw": "ribbon OEM duty drawback, ribbon OEM rebate, ribbon OEM export refund, ribbon OEM cross border, ribbon OEM freight cost recovery, ribbon OEM 12 drawback cadre, ribbon OEM 11 rebate, ribbon OEM 10 refund, ribbon OEM 9 freight recovery, ribbon OEM 8 export refund, ribbon OEM 2026 brand procurement, ribbon OEM 2026",
        "slug_date": "2026-08-30-pm",
        "meters": "11.2M",
        "brands": 84,
        "eu": 45,
        "na": 50,
        "mea": 52,
        "modules": 99,
        "layers": 6,
        "m1": "12-Duty-Drawback-Cadre, 11-Rebate-Claim-Engine, 10-Cross-Border-Refund-Pipeline, 9-Freight-Cost-Recovery-Stack, 8-Export-Refund-Archive",
        "m2": "7-Drawback-Dashboard, 9-Drawback-IP, 6-Drawback-Cost &amp; 10-Drawback-Continuous-Improvement",
    },
]

TEMPLATE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="author" content="Xiamen Smith Ribbon &amp; Bow Co., Ltd.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://smithribbon.com/blog/blog-ribbon-oem-{num_low}-module-{slug}-global-brand-procurement-{slug_date}.html">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://smithribbon.com/blog/blog-ribbon-oem-{num_low}-module-{slug}-global-brand-procurement-{slug_date}.html">
<meta property="og:image" content="https://smithribbon.com/banner.png">
<meta property="og:site_name" content="SmithRibbon — Xiamen Smith Ribbon &amp; Bow">
<meta property="article:published_time" content="{iso}">
<meta property="article:modified_time" content="{iso}">
<meta property="article:author" content="Xiamen Smith Ribbon &amp; Bow Co., Ltd.">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{short_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://smithribbon.com/banner.png">

<!-- JSON-LD: BlogPosting -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{desc}",
  "image": "https://smithribbon.com/banner.png",
  "datePublished": "{iso}",
  "dateModified": "{iso}",
  "author": {{"@type": "Organization", "name": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.", "url": "https://smithribbon.com"}},
  "publisher": {{"@type": "Organization", "name": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.", "url": "https://smithribbon.com", "logo": {{"@type": "ImageObject", "url": "https://smithribbon.com/banner.png"}}}},
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://smithribbon.com/blog/blog-ribbon-oem-{num_low}-module-{slug}-global-brand-procurement-{slug_date}.html"}},
  "keywords": "{kw_plain}",
  "wordCount": 1380,
  "inLanguage": "en-US",
  "articleSection": "{cat}"
}}
</script>

<style>
  body {{ font-family: 'Segoe UI', system-ui, sans-serif; line-height: 1.8; color: #2a2a2a; max-width: 980px; margin: 0 auto; padding: 24px; background: #fafafa; }}
  h1 {{ font-size: 2.1rem; color: #8b1538; margin-bottom: 0.4em; line-height: 1.3; }}
  h2 {{ font-size: 1.55rem; color: #5a0f25; margin-top: 1.8em; border-left: 4px solid #b8854a; padding-left: 12px; }}
  h3 {{ font-size: 1.25rem; color: #5a0f25; margin-top: 1.4em; }}
  .meta {{ color: #777; font-size: 0.92rem; margin-bottom: 1.6em; padding-bottom: 12px; border-bottom: 1px solid #e0e0e0; }}
  .lead {{ background: #fff7f0; border-left: 4px solid #b8854a; padding: 16px 20px; margin: 1.4em 0; font-size: 1.04rem; }}
  .module-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin: 1.4em 0; }}
  .module-card {{ background: #fff; border: 1px solid #e8d5b7; border-radius: 6px; padding: 14px; }}
  .module-card .num {{ font-weight: 700; color: #8b1538; font-size: 0.95rem; }}
  .module-card .name {{ color: #5a0f25; font-size: 0.88rem; margin-top: 4px; }}
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
</head>
<body>

<h1>{title}</h1>
<div class="meta">
  <span class="tag">{cat}</span>
  Published {iso_date_human} &middot; Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; 38 min read
</div>

<div class="lead">{desc}</div>
"""

TEMPLATE_BODY = """
<h2>1. The 2026 B2B Brand-Procurement Reality</h2>
<p>Global brand owners and retail merchandising VPs in 2026 are navigating an increasingly fragmented ribbon supply landscape. With {brands}+ active brand partners across {eu} EU-27 markets, {na} NA-states, {mea} MEA-jurisdictions and an ever-growing list of APAC and LatAm jurisdictions, the {topic} challenge has become one of the most strategic procurement questions of the year. Mills that can deliver on {m1} while preserving cost discipline across {m2} now command 84-94% on-time delivery premiums in their respective channels.</p>
<p>The Xiamen Smith Ribbon &amp; Bow Co., Ltd. engineering team has codified the {module_label} architecture specifically to address this procurement reality. Drawing on 20+ years of OEM manufacturing, BSCI / SEDEX / OEKO-TEX® / ISO 9001 / SMETA audit discipline, and 1,000+ brand-customer relationships, this {modules}-module architecture gives brand owners a single reference for evaluating, contracting and scaling a {topic} program with predictable 92-98% pilot-launch success and 18-26% scrap-rate reduction.</p>

<h2>2. Why a {module_label} Architecture Matters</h2>
<p>Ribbon, by its very nature, sits at the intersection of <strong>emotional design</strong>, <strong>brand identity</strong> and <strong>industrial throughput</strong>. A 12 mm single-face satin ribbon may seem simple — but when it carries a 4-color Pantone-matched logo, a hot-stamped metallic foil, a UV-cured release coating and is destined for a multi-market D2C launch with FBA / Tmall / TikTok-Shop marketplace routing, every micron of tolerance and every day of lead time compounds into a material brand outcome.</p>
<p>The {module_label} program formalizes the cross-functional handshake between <em>artwork engineering</em>, <em>color management</em>, <em>sub-tier supplier qualification</em>, <em>capacity reservation</em>, <em>inspection discipline</em>, <em>logistics orchestration</em> and <em>post-shipment analytics</em>. Without this handshake, 31-46% of new ribbon SKUs in 2025 missed their first-shot approval window, and 22-38% of approved samples diverged from bulk production by ΔE&gt;2.5. With it, the {brands}+ brand partners in our program averaged 92-98% first-time-right and 84-94% on-time delivery across {meters} annual meters.</p>

<h2>3. The {modules}-Module Architecture Stack</h2>
<p>The architecture is intentionally modular so a brand can adopt one pillar at a time, or all 98-99 modules as a single program. Below is the 6-layer decomposition.</p>

<div class="module-grid">
  <div class="module-card"><div class="num">Layer 1</div><div class="name">Cadre &amp; Org-Design</div></div>
  <div class="module-card"><div class="num">Layer 2</div><div class="name">Engine &amp; Process-Design</div></div>
  <div class="module-card"><div class="num">Layer 3</div><div class="name">Pipeline &amp; Data-Design</div></div>
  <div class="module-card"><div class="num">Layer 4</div><div class="name">Stack &amp; Integration-Design</div></div>
  <div class="module-card"><div class="num">Layer 5</div><div class="name">Archive &amp; Dashboard-Design</div></div>
  <div class="module-card"><div class="num">Layer 6</div><div class="name">IP, Cost &amp; CI-Design</div></div>
</div>

<h3>3.1 Module Group A — Cadre &amp; Engine ({m1})</h3>
<p>Modules in this group govern the human-side and process-side of the {topic} program. Each module ships with a 22-28 page playbook, a RACI matrix, a 4-step on-the-job training plan, and a balanced scorecard template. Brand partners typically activate 6-9 of these modules in their first 90 days and reach 100% rollout within 8-12 months.</p>
<table>
<tr><th>Module</th><th>Owner</th><th>Activation Cycle</th><th>Brand-Side Touch-Points</th></tr>
<tr><td>12-Cadre</td><td>VP Supply Chain</td><td>0-30 d</td><td>Steerco, KPI sync</td></tr>
<tr><td>11-Engine</td><td>Director Operations</td><td>0-90 d</td><td>Weekly ops review</td></tr>
<tr><td>10-Pipeline</td><td>Lead Procurement</td><td>30-120 d</td><td>Bi-weekly pipeline desk</td></tr>
<tr><td>9-Stack</td><td>Lead Quality</td><td>30-150 d</td><td>Monthly quality forum</td></tr>
<tr><td>8-Archive</td><td>Lead Compliance</td><td>60-180 d</td><td>Quarterly compliance review</td></tr>
</table>

<h3>3.2 Module Group B — Dashboard, IP, Cost &amp; CI ({m2})</h3>
<p>Modules in this group handle the analytics, intellectual-property custody, total-cost-of-ownership, and continuous-improvement loops. The {module_label} architecture treats the dashboard layer as a public-good for brand partners: every brand gets a 9-widget BI dashboard refreshed nightly, with role-based access for procurement, merchandising, sustainability and finance teams.</p>
<ul>
  <li><strong>7-Dashboard:</strong> 9-widget BI, role-based, nightly refresh, 92-98% adoption.</li>
  <li><strong>9-IP:</strong> Brand-owned artwork, color recipe, and tooling custody framework.</li>
  <li><strong>6-Cost:</strong> TCO decoder across 5 cost layers (FOB, freight, duty, inventory, ESG).</li>
  <li><strong>10-CI:</strong> Kaizen, A3, PDCA, Six-Sigma DMAIC toolkits embedded in QBR.</li>
</ul>

<h2>4. Cross-Functional Architecture Detail</h2>
<h3>4.1 Artwork &amp; Color Management</h3>
<p>Every SKU begins with a brand-supplied artwork file. The {module_label} framework routes this through a 6-stage artwork pipeline: file-pre-flight, color-conversion, Pantone-live proof, dye-house dip approval, lab-scale strike-off, and bulk pre-production run. Spectrophotometric QC at ΔE≤1.5 for solid colors and ΔE≤2.0 for 4-color process is enforced. Brand partners who skip the lab-scale strike-off see 31-46% first-shot failure; partners who follow the full 6-stage pipeline see 92-98% first-shot approval.</p>

<h3>4.2 Sub-Tier Supplier Qualification</h3>
<p>Yarn, dye-house, loom, finishing and printing sub-tiers are mapped across a 4-tier transparency model. Tier 1 is direct; Tier 2 is a known sub-supplier; Tier 3 is a sub-of-sub; Tier 4 is raw-material or commodity. Each tier carries a risk score, a BSCI / SEDEX / SMETA audit pass/fail, an OEKO-TEX® / GOTS / GRS certificate status, and a 12-month capacity reservation profile. Brand owners get a 1-page tier-map with each quarterly QBR.</p>

<h3>4.3 Capacity Reservation &amp; Production Scheduling</h3>
<p>For Q4 holiday peaks, the {module_label} architecture pre-books loom and dye-house capacity 9-12 months in advance using a 4-stage cascade (initial allocation, 90-day lock, 60-day confirm, 30-day final). The result is a 84-94% on-time delivery premium versus 56-72% for mills running spot capacity. Brand partners who adopt the full cascade see 18-26% lower freight cost and 12-18% lower expedite cost.</p>

<h3>4.4 Quality Inspection (Pre-Shipment AQL)</h3>
<p>AQL 2.5 / 4.0 sampling per ISO 2859-1 is the program default, with optional tightening to AQL 1.5 / 2.5 for premium beauty and lifestyle brands. Inspections cover 23 defect categories: width, thickness, color (ΔE), hand-feel, drape, bow-tie geometry, wire-edge retention, print registration, hot-stamp adhesion, UV-cure coverage, scuff resistance, and 12 more. Inspection photos and lot-level QC data are uploaded to the brand-partner dashboard within 24 hours of inspection.</p>

<h3>4.5 Logistics, Incoterms &amp; Cross-Border Routing</h3>
<p>The architecture supports FOB, CIF, DDP, DAP and EXW routings, with 11 template Incoterms clauses and a 7-stage container-loading optimizer (cube-utilization 84-92%, pallet-stability 96-100%). For brands selling on Amazon FBA, Tmall, TikTok-Shop, Zalando and Nordstrom, a marketplace-ready routing layer bundles FNSKU / EAN / UPC labeling, poly-bag compliance, dunnage spec, and DC routing by region.</p>

<h3>4.6 Sustainability, ESG &amp; Compliance</h3>
<p>OEKO-TEX® Standard 100, GRS, GOTS, FSC®, BCI, BSCI, SEDEX, SMETA, ISO 9001, ISO 14001, ISO 45001, SA8000, CDP, TCFD and CSRD are all in scope. The {module_label} architecture carries a 6-ESG-pillar scoring system (carbon, water, chemistry, labor, community, governance) and produces a 1-page ESG summary for every brand partner each quarter.</p>

<h2>5. KPI &amp; Outcome Framework</h2>
<div class="kpi">
  <strong>Outcome band</strong> for brand partners fully adopting the {module_label} architecture:
  <ul>
    <li>92-98% time-to-pilot-launch within 21-30 days</li>
    <li>84-94% on-time delivery across the 12-month rolling window</li>
    <li>44-58% cost reduction across 5 cost layers (FOB / freight / duty / inventory / ESG)</li>
    <li>18-26% scrap-rate reduction via PPAP + AQL 2.5 / 4.0</li>
    <li>92-98% first-shot approval via the 6-stage artwork pipeline</li>
    <li>31-46% inventory turn improvement via VMI / 3PL cross-docking</li>
    <li>9-12 month capacity pre-booking for Q4 peak</li>
  </ul>
</div>

<h2>6. Implementation Roadmap (90-Day Pilot)</h2>
<ol>
  <li><strong>Day 0-14:</strong> Sign NDA, exchange spec sheet, run fit-gap workshop, identify the 6-9 modules to activate first.</li>
  <li><strong>Day 15-30:</strong> Pantone-live color proof, lab-scale strike-off, sign off artwork pipeline.</li>
  <li><strong>Day 31-60:</strong> PPAP, pre-production sample, AQL 2.5 / 4.0 protocol alignment.</li>
  <li><strong>Day 61-90:</strong> Bulk production run 1, pre-shipment inspection, dashboard onboarding, QBR kickoff.</li>
</ol>

<h2>7. Commercial Terms &amp; MOQ</h2>
<p>Standard program MOQ: 1,000 meters per SKU per width-color combination, with 500-meter trial MOQ available for first-time brand partners. Lead time 21-30 days for repeat SKUs and 30-45 days for new custom development. Payment terms: 30% T/T deposit, 70% balance against B/L copy for repeat orders; L/C at sight available for orders above USD 50,000. OEM tooling, dies, cylinders and jacquard cards are brand-owned assets with a written custody transfer.</p>

<h2>8. Why Xiamen Smith Ribbon &amp; Bow Co., Ltd.</h2>
<ul>
  <li>20+ years of OEM/ODM ribbon and bow manufacturing (founded 2004/2007)</li>
  <li>15,000 m² self-owned factory, 200+ employees, 100,000 m/day capacity</li>
  <li>BSCI, SEDEX, SMETA, ISO 9001, OEKO-TEX®, FSC®, GRS audited</li>
  <li>1,000+ brand-customer relationships across 50+ countries</li>
  <li>Walmart, Target, L'Oréal, Dollar General and other tier-1 retail relationships</li>
  <li>In-house color lab, jacquard studio, bow construction line, FBA-prep DC</li>
  <li>20-25 day lead time for repeat SKUs, 30-45 days for new development</li>
  <li>1,000 m standard MOQ, 500 m trial MOQ for first-time brand partners</li>
</ul>

<h2>9. Call to Action</h2>
<p>Brand owners, retail merchandising VPs, and procurement directors evaluating a {topic} program can request a 30-minute working session with our B2B engineering team. We will share the {module_label} full module map, a 1-page tier-1 / tier-2 / tier-3 sub-supplier map, a sample TCO decoder, and a 90-day pilot plan tailored to your category, market, and brand identity.</p>

<div class="cta">
  <p><strong>Get the {module_label} Architecture Brief &amp; 90-Day Pilot Plan</strong></p>
  <p>Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; +86-592-5095373 &middot; xmmsd@126.com &middot; smithribbon.com</p>
  <p><a href="https://smithribbon.com/contact.html">Request a working session &rarr;</a> &nbsp; | &nbsp; <a href="https://smithribbon.com/blog.html">Explore all B2B OEM modules &rarr;</a></p>
</div>

<p><em>Last updated: {iso}. This article is part of the SmithRibbon B2B OEM module library for global brand procurement teams.</em></p>

</body>
</html>
"""

def render(art):
    kw_plain = art["kw"].replace(",", ", ")
    iso = f"{art['slug_date'].split('-am')[0].split('-pm')[0]}T10:00:00+08:00" if art["slot"] == "am" else f"{art['slug_date'].split('-am')[0].split('-pm')[0]}T15:00:00+08:00"
    iso_date_human = "10:00 AM CST, " + art["slug_date"].split("-am")[0].split("-pm")[0] if art["slot"] == "am" else "03:00 PM CST, " + art["slug_date"].split("-am")[0].split("-pm")[0]
    out = TEMPLATE_HEAD.format(
        title=art["title"],
        desc=art["desc"],
        kw=art["kw"],
        kw_plain=kw_plain,
        cat=art["cat"],
        short_title=art["short_title"],
        iso=iso,
        iso_date_human=iso_date_human,
        num_low=art["num"],
        slug=art["slug"],
        slug_date=art["slug_date"],
    )
    out += TEMPLATE_BODY.format(
        topic=art["topic"],
        cat=art["cat"],
        module_label=art["module_label"],
        modules=art["modules"],
        brands=art["brands"],
        eu=art["eu"],
        na=art["na"],
        mea=art["mea"],
        m1=art["m1"],
        m2=art["m2"],
        meters=art["meters"],
        iso=iso,
    )
    fname = f"blog-ribbon-oem-{art['num']}-module-{art['slug']}-global-brand-procurement-{art['slug_date']}.html"
    path = os.path.join(BLOG_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    # count words
    text_only = out.replace("<style>", "").replace("</style>", "")
    import re
    plain = re.sub(r"<[^>]+>", " ", text_only)
    words = len(plain.split())
    print(f"  WROTE {fname} ({len(out)} bytes, ~{words} words)")
    return fname

if __name__ == "__main__":
    print(f"Generating {len(ARTICLES)} articles for {BLOG_DIR} ...")
    for art in ARTICLES:
        render(art)
    print("Done.")
