#!/usr/bin/env python3
"""Build 2026-09-25 cron DOUBLE B2B articles (run 09-24 07:00 UTC for next-day slots):
- AM (Module 167): Mill-Side Seasonality Cascade — Holiday + Non-Holiday Capacity Pre-Booking
- PM (Module 168): Brand-Buyer 7-Stage Brief-to-Shelf Onboarding Playbook
"""
import os

WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
ISO_AM = "2026-09-25T07:00:00+00:00"
ISO_PM = "2026-09-25T15:00:00+00:00"
DISPLAY_AM = "September 25, 2026 (AM)"
DISPLAY_PM = "September 25, 2026 (PM)"
FILE_167 = "blog/blog-ribbon-oem-167-module-brand-buyer-mill-side-seasonality-cascade-holiday-non-holiday-capacity-pre-booking-architecture-global-brand-procurement-2026-09-25-am.html"
FILE_168 = "blog/blog-ribbon-oem-168-module-brand-buyer-mill-side-7-stage-brief-to-shelf-onboarding-playbook-architecture-global-brand-procurement-2026-09-25-pm.html"
CANONICAL_167 = f"{SITE_URL}/{FILE_167}"
CANONICAL_168 = f"{SITE_URL}/{FILE_168}"

DISPLAY_TITLE_167 = "Mill-Side Seasonality Cascade — Holiday + Non-Holiday Capacity Pre-Booking Architecture 2026"
DISPLAY_TITLE_168 = "Brand-Buyer 7-Stage Brief-to-Shelf Onboarding Playbook for Ribbon OEM 2026"

DESC_167 = "B2B ribbon OEM 167-module mill-side seasonality cascade architecture. Holiday + non-holiday capacity pre-booking, 12-month calendar lock, multi-market brand carve-out, Q4 peak surge rules. Smith Ribbon OEM since 2004."
DESC_168 = "B2B ribbon OEM 168-module brand-buyer mill-side 7-stage brief-to-shelf onboarding playbook. RFQ, sample, color match, pre-production, PPAP, first PO, replenishment cadence. Smith Ribbon OEM since 2004."

TAGS_167 = "Seasonality Cascade, Capacity Pre-Booking, Q4 Peak, Holiday Ribbon, OEM Ribbon"
TAGS_168 = "Onboarding Playbook, Brief to Shelf, Brand Procurement, OEM Ribbon, New SKU Launch"
KEYWORDS_167 = "seasonality cascade ribbon, capacity pre-booking mill, Q4 holiday peak ribbon, brand carve-out, OEM capacity calendar"
KEYWORDS_168 = "ribbon OEM onboarding playbook, brief to shelf ribbon, brand buyer onboarding, 7 stage ribbon launch, PPAP ribbon"

FAQS_167 = '[{"q":"What is a mill-side seasonality cascade in ribbon OEM?","a":"A capacity-planning framework that sequences holiday and non-holiday demand into a unified 12-month mill calendar. Each season gets a reservation window, a confirmation trigger, and a cascade-priority rule — typically with Q4 holiday demand locked first."},{"q":"How early should a brand pre-book Q4 holiday ribbon?","a":"Q4 peak should be reserved 9-12 months ahead, with final PO confirmed by T-180 days. Brands that miss the T-180 trigger pay 8-15% spot premiums or accept allocation."},{"q":"What is a multi-market brand carve-out?","a":"A clause in a multi-brand or multi-market mill agreement that allocates fixed capacity slices to each brand or market region. Each brand gets its own confirmation trigger, its own surge budget, and its own shortage-allocation priority."},{"q":"What are the four cascade-priority tiers?","a":"(1) Confirmed PO at T-180 or earlier. (2) Forecast PO at T-90. (3) Replenishment intent at T-30. (4) Spot / new-buyer orders. Tier 1 ships first; Tier 4 only fills leftover slots."},{"q":"How does seasonality cascade interact with multi-supplier resilience?","a":"The cascade at the primary mill anchors demand; the secondary mill is benchmarked against the cascade calendar. Without the cascade, dual-sourcing collapses into Q4 scheduling chaos; with the cascade, dual-sourcing stays ordered across both mills."}]'

FAQS_168 = '[{"q":"What is the 7-stage brief-to-shelf onboarding playbook in ribbon OEM?","a":"A structured 90-day onboarding sequence from brand brief to first shelf-ready PO: (1) RFQ & spec sheet, (2) Sample dispatch & approval, (3) Color matching & Pantone lock, (4) Pre-production sample run, (5) PPAP / pre-shipment approval, (6) First production PO with on-time-in-full target, (7) Replenishment cadence & vendor scorecard."},{"q":"How long does each stage typically take?","a":"Stage 1 RFQ 1-3 days. Stage 2 Sample 7-10 days. Stage 3 Color match 5-7 days. Stage 4 PPS 7-10 days. Stage 5 PPAP 5-7 days. Stage 6 First PO 14-21 days. Stage 7 Replenishment starts at week 9-12."},{"q":"What deliverables are needed at each stage?","a":"Stage 1: tech-pack, Pantone refs, target cost. Stage 2: hand-sample + lab-dip. Stage 3: production-ready color recipe. Stage 4: bulk yardage for fit-test. Stage 5: AQL-passed first-article with test report. Stage 6: bulk PO with packaging spec. Stage 7: replenishment cadence sign-off."},{"q":"How does the playbook protect against rework?"],"question":"What common onboarding mistakes do brand buyers make?"}]'

# Fix FAQ JSON (last entry had malformed quote)
FAQS_168 = '[{"q":"What is the 7-stage brief-to-shelf onboarding playbook in ribbon OEM?","a":"A structured 90-day onboarding sequence from brand brief to first shelf-ready PO: (1) RFQ & spec sheet, (2) Sample dispatch & approval, (3) Color matching & Pantone lock, (4) Pre-production sample run, (5) PPAP / pre-shipment approval, (6) First production PO with on-time-in-full target, (7) Replenishment cadence & vendor scorecard."},{"q":"How long does each stage typically take?","a":"Stage 1 RFQ 1-3 days. Stage 2 Sample 7-10 days. Stage 3 Color match 5-7 days. Stage 4 PPS 7-10 days. Stage 5 PPAP 5-7 days. Stage 6 First PO 14-21 days. Stage 7 Replenishment starts at week 9-12."},{"q":"What deliverables are needed at each stage?","a":"Stage 1: tech-pack, Pantone refs, target cost. Stage 2: hand-sample + lab-dip. Stage 3: production-ready color recipe. Stage 4: bulk yardage for fit-test. Stage 5: AQL-passed first-article with test report. Stage 6: bulk PO with packaging spec. Stage 7: replenishment cadence sign-off."},{"q":"What common onboarding mistakes do brand buyers make?","a":"Five most common: skipping color-management at Stage 3 (causes 1.5-2.5 delta EΔ drift), under-sampling QA before first PO (causes 8-15% defect-cost floor), no replenishment cadence (causes 6-10 week stock-out risk), no vendor scorecard (no learning loop), no formal change-control between stages (causes spec drift)."},{"q":"How does the playbook connect to dual-sourcing resilience?","a":"Stages 5-7 are run in parallel with the secondary mill to validate dual-sourcing capability. Without parallel-stage validation, dual-sourcing collapses into visual-drift between mills; with it, dual-sourcing is anchored to a single validated process."}]'

BODY_167 = """<div class="container">
<p>Q4 holiday surge is the single most disruptive event in the ribbon OEM calendar. For a brand buyer, 30-60% of annual ribbon volume ships in 8 weeks; for a mill, that volume must be planned 9-12 months ahead or it does not get produced at the right quality. Smith Ribbon's 167-module seasonality-cascade architecture gives brand buyers a structured capacity-planning framework: 12-month pre-booking window, four cascade-priority tiers, multi-market brand carve-outs, and surge-budget rules that protect both mill margin and brand shelf-readiness.</p>

<h2>1. Why Seasonality Cascade Matters</h2>
<p>Holiday demand in ribbon OEM is mathematically non-linear. A typical year distributes roughly: Q1 15-18% of annual volume, Q2 18-22%, Q3 20-25%, Q4 40-55%. Q4 alone can absorb 50%+ of capacity for Halloween, Thanksgiving, Christmas, and New Year gifting — with week 48-51 often running at 110-130% of nominal capacity. Without a structured cascade, mills and brands both lose: mills accept orders they cannot deliver, brands receive late or partial shipments, end-retailers face empty stockrooms.</p>

<h3>1.1 The Three Failure Modes Without Cascade</h3>
<ul>
<li><strong>Spot-Premium Spiral:</strong> brands that miss the T-180 confirmation window pay 8-15% spot premium for last-minute capacity.</li>
<li><strong>Allocation Allocation:</strong> mills allocate based on which brand shouts loudest in week 47, not which contract committed earliest.</li>
<li><strong>Quality Compromise:</strong> mills accept rush orders beyond their true capacity and run multi-shift overtime — defect rate climbs 30-80% over baseline.</li>
</ul>

<h2>2. The 12-Month Capacity Calendar</h2>
<p>The seasonality cascade is anchored to a 12-month calendar with four reservation windows:</p>

<table>
<thead><tr><th>Window</th><th>Trigger</th><th>Confirmation Deadline</th><th>Capacity State</th></tr></thead>
<tbody>
<tr><td>Holiday Q4 (Oct-Dec)</td><td>T-12 months (Oct prior year)</td><td>T-180 days (Apr current year)</td><td>Locked + cascade priority</td></tr>
<tr><td>Spring/Easter (Jan-Apr)</td><td>T-9 months</td><td>T-120 days</td><td>Reserved, priority by history</td></tr>
<tr><td>Summer/Wedding (May-Jul)</td><td>T-9 months</td><td>T-120 days</td><td>Reserved, priority by history</td></tr>
<tr><td>Resort/Back-to-School (Aug-Sep)</td><td>T-6 months</td><td>T-90 days</td><td>Allocated by forecast</td></tr>
</tbody>
</table>

<h2>3. The Four Cascade-Priority Tiers</h2>
<p>Within each reservation window, orders are sequenced by four priority tiers. Tier 1 ships first; Tier 4 only fills leftover slots.</p>

<table>
<thead><tr><th>Tier</th><th>Order Type</th><th>Confirmation Depth</th><th>Surge Budget</th></tr></thead>
<tbody>
<tr><td>1 — Confirmed PO</td><td>Locked PO at T-180 or earlier</td><td>Hard PO with deposit</td><td>Full +25% surge</td></tr>
<tr><td>2 — Forecast PO</td><td>Forecast at T-90 with letter of intent</td><td>Forecast PO with commitment fee</td><td>+10% surge, then slot allocation</td></tr>
<tr><td>3 — Replenishment</td><td>Replenishment intent at T-30</td><td>Standing replenishment cadence</td><td>Slot only, no surge</td></tr>
<tr><td>4 — Spot / New Buyer</td><td>Orders post-T-30</td><td>PO only with premium</td><td>Leftover slots, premium pricing</td></tr>
</tbody>
</table>

<h2>4. Multi-Market Brand Carve-Out</h2>
<p>For global brands operating across regions, a single-mill capacity pool can be overwhelmed by competing regional priorities. The multi-market brand carve-out clause allocates fixed capacity slices to each market — typically by historic share of business, by strategic priority, or by contractual volume commitment.</p>

<h3>4.1 Carve-Out Mechanics</h3>
<ul>
<li><strong>Baseline Allocation:</strong> each market gets a baseline slice of the mill's Q4 capacity, set annually based on prior-year volume.</li>
<li><strong>Trade Window:</strong> markets can trade allocation within the same brand (e.g., EU brand transfers unused Q4 slice to US brand for premium surge).</li>
<li><strong>Independent Confirmation Triggers:</strong> each market has its own T-180 confirmation deadline, with cross-brand trade allowed up to T-90.</li>
<li><strong>Independent Surge Budgets:</strong> each market gets its own surge budget; unused surge is bankable but not transferable.</li>
</ul>

<h2>5. The Surge-Budget Rule</h2>
<p>Mill capacity cannot physically scale beyond ~125% of nominal without catastrophic quality risk. The surge-budget rule pre-allocates surge capacity by tier:</p>
<ul>
<li>Tier 1 brands may invoke up to +25% surge against the December PO with 7-day lead time.</li>
<li>Tier 2 brands may invoke +10% surge against the December PO with 14-day lead time; beyond that, slot allocation only.</li>
<li>Tier 3 and Tier 4 receive no surge; allocation is first-come-first-served within the remaining slot pool.</li>
</ul>

<h2>6. Three Contractual Protections</h2>
<ol>
<li><strong>T-180 Confirmation Lock with Take-or-Pay:</strong> Tier 1 brands that confirm at T-180 lock capacity for the season. Take-or-pay covers 70% of confirmed quantity if the brand pulls back post-confirmation.</li>
<li><strong>Cascade-Priority Enforcement Clause:</strong> mills commit to cascade priority order — Tier 1 first. If the mill breaches, brand is entitled to expedite premium refund or 10% volume credit.</li>
<li><strong>Multi-Market Carve-Out Reconciliation:</strong> annual review of carve-out slices based on actual pull-through. Brands that consistently under-pull lose baseline share; brands that over-pull gain share next year.</li>
</ol>

<h2>7. Connection to Multi-Supplier Resilience</h2>
<p>Module 167 closes the resilience loop. The seasonality cascade at the primary mill anchors the demand calendar; the secondary mill is benchmarked against it. Without the cascade, dual-sourcing collapses into Q4 scheduling chaos; with the cascade, dual-sourcing stays ordered across both mills. The cascade is the planning structure that makes multi-supplier resilience operationally viable.</p>

<div class="cta">
<a href="/contact.html">Request the Seasonality Cascade Calendar Worksheet &rarr;</a>
</div>
</div>
"""

BODY_168 = """<div class="container">
<p>The 90-day window between brand brief and shelf-ready SKU is the highest-risk phase of any ribbon OEM relationship. Get it right, and the brand launches on time with predictable unit cost. Get it wrong, and the brand is mid-season with empty shelves, late shipments, or colors that do not match the lookbook. Smith Ribbon's 168-module 7-stage brief-to-shelf onboarding playbook gives brand buyers a structured 90-day sequence: RFQ, sample, color match, PPS, PPAP, first PO, replenishment cadence — with deliverables, timing, and common pitfalls documented at each stage.</p>

<h2>1. Why Onboarding Discipline Matters</h2>
<p>Most ribbon OEM onboarding failures trace to three structural causes: skipped color management, under-sampled QA before first PO, and missing replenishment cadence. Each adds 2-6 weeks of slip and 5-15% cost. The 7-stage playbook disciplines each step.</p>

<h3>1.1 The Three Most Common Pitfalls</h3>
<ul>
<li><strong>Skipping Color Management:</strong> jumping from sample (Stage 2) to first PO (Stage 6) without locking the production-ready color recipe (Stage 3) causes 1.5-2.5 delta EΔ drift in production.</li>
<li><strong>Under-Sampled QA:</strong> accepting a single pre-production sample without bulk-yardage QA causes 8-15% defect-cost floor on the first PO.</li>
<li><strong>Missing Replenishment Cadence:</strong> without a replenishment cadence signed at Stage 7, brands face 6-10 week stock-out windows between repeat orders.</li>
</ul>

<h2>2. The 7 Stages — Overview</h2>
<table>
<thead><tr><th>Stage</th><th>Name</th><th>Duration</th><th>Deliverable</th></tr></thead>
<tbody>
<tr><td>1</td><td>RFQ &amp; Spec Sheet</td><td>1-3 days</td><td>Tech-pack, Pantone refs, target cost</td></tr>
<tr><td>2</td><td>Sample Dispatch &amp; Approval</td><td>7-10 days</td><td>Hand-sample + lab-dip</td></tr>
<tr><td>3</td><td>Color Match &amp; Pantone Lock</td><td>5-7 days</td><td>Production-ready color recipe</td></tr>
<tr><td>4</td><td>Pre-Production Sample Run</td><td>7-10 days</td><td>Bulk yardage for fit-test</td></tr>
<tr><td>5</td><td>PPAP / Pre-Shipment Approval</td><td>5-7 days</td><td>AQL-passed first-article with test report</td></tr>
<tr><td>6</td><td>First Production PO</td><td>14-21 days</td><td>Bulk PO with packaging spec</td></tr>
<tr><td>7</td><td>Replenishment Cadence &amp; Scorecard</td><td>Ongoing</td><td>Cadence sign-off, scorecard live</td></tr>
</tbody>
</table>

<h2>3. Stage-by-Stage Detail</h2>

<h3>3.1 Stage 1 — RFQ &amp; Spec Sheet (Days 1-3)</h3>
<p>The brand issues a Request for Quotation with the spec sheet. The spec sheet covers fiber content (polyester, satin, grosgrain, velvet, organza), width (mm or inch), edge treatment (cut, woven, wired), color (Pantone code or reference swatch), print type (rotary hot-stamp, digital, screen), MOQ expectation, target FOB price, and delivery window. The mill responds with quote + lead-time within 1-3 days. Common pitfall: vague spec sheet leads to ambiguous quotes and downstream rework.</p>

<h3>3.2 Stage 2 — Sample Dispatch &amp; Approval (Days 4-13)</h3>
<p>Mill produces a hand-sample and a lab-dip. Lab-dip is a small fabric piece dyed to the requested color. Brand reviews against its reference swatch or Pantone book. Approval triggers Stage 3. Common pitfall: approving a lab-dip on screen rather than physical swatch — screen color rendering varies 1-3 delta EΔ.</p>

<h3>3.3 Stage 3 — Color Match &amp; Pantone Lock (Days 14-20)</h3>
<p>Mill produces a production-ready color recipe. Spectrophotometer measurement validates delta EΔ against the lab-dip. Locked recipe becomes the color-of-record for the SKU. Common pitfall: skipping this stage and going direct to bulk production — produces the 1.5-2.5 delta EΔ drift we saw in Module 68.</p>

<h3>3.4 Stage 4 — Pre-Production Sample (Days 21-30)</h3>
<p>Mill produces 50-200 meters of bulk ribbon at production-machine settings. Brand evaluates against fit-test criteria: hand-feel, drape, edge treatment, print registration. PPS approval triggers PPAP. Common pitfall: PPS rushed without fit-test on actual downstream product — discover issues only at first bulk delivery.</p>

<h3>3.5 Stage 5 — PPAP / Pre-Shipment Approval (Days 31-37)</h3>
<p>Mill runs AQL inspection on the first bulk run, typically 100-500 meters. Test report includes tensile strength, color match (delta EΔ), print registration, edge treatment, hand-feel. Brand signs off. Common pitfall: brand accepts PPAP on single sample without lot sampling — single-piece validation has 8-15% defect-cost risk.</p>

<h3>3.6 Stage 6 — First Production PO (Days 38-58)</h3>
<p>Bulk production run, typically 1,000-10,000 meters. Brand receives finished goods with packaging spec, bar-coded labels, AQL report, and conformity documents. Common pitfall: brand has no on-time-in-full (OTIF) target at first PO — sets a low bar for future replenishment.</p>

<h3>3.7 Stage 7 — Replenishment Cadence &amp; Scorecard (Day 59 onwards)</h3>
<p>Brand and mill sign off on replenishment cadence (e.g., monthly 5K-piece standing order, weekly call-off), vendor scorecard (on-time-in-full, defect rate, color consistency, response time), and quarterly business review. Common pitfall: cadence not signed off means ad-hoc ordering and stock-out risk.</p>

<h2>4. Common Mistakes &amp; How to Avoid Them</h2>
<p>Five most common onboarding mistakes:</p>
<ol>
<li><strong>Skipping color-management at Stage 3.</strong> Causes 1.5-2.5 delta EΔ drift. Always run spectrophotometer color-lock.</li>
<li><strong>Under-sampling QA before first PO.</strong> Causes 8-15% defect-cost floor. Always run AQL lot sampling at Stage 5.</li>
<li><strong>No replenishment cadence.</strong> Causes 6-10 week stock-out risk. Always sign cadence at Stage 7.</li>
<li><strong>No vendor scorecard.</strong> No learning loop; quality drift is invisible. Always install scorecard from Stage 7.</li>
<li><strong>No formal change-control between stages.</strong> Spec drift between Stage 2 and Stage 6 causes 5-15% cost. Always document change-control.</li>
</ol>

<h2>5. Connection to Multi-Supplier Resilience</h2>
<p>Stages 5-7 should run in parallel with the secondary mill to validate dual-sourcing capability. Without parallel-stage validation, dual-sourcing collapses into visual-drift between mills; with it, dual-sourcing is anchored to a single validated process. The onboarding playbook is the structural foundation that makes multi-supplier resilience operationally viable.</p>

<div class="cta">
<a href="/contact.html">Request the Brief-to-Shelf Onboarding Worksheet &rarr;</a>
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

def article_html(num, title_display, desc, canonical, pubtime, tags_str, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc, date_label):
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
    tag_parts = [t.strip() for t in tags_str.split(",")]
    tag0 = tag_parts[0] if len(tag_parts) > 0 else "OEM Ribbon"
    tag1 = tag_parts[1] if len(tag_parts) > 1 else tag0
    tag2 = tag_parts[2] if len(tag_parts) > 2 else "OEM Ribbon"
    return template.replace("__TITLE__", title_display)\
        .replace("__DESC__", desc)\
        .replace("__KW__", keywords)\
        .replace("__CANONICAL__", canonical)\
        .replace("__OGT__", og_title)\
        .replace("__OGD__", og_desc)\
        .replace("__TWT__", tw_title)\
        .replace("__TWD__", tw_desc)\
        .replace("__PUBTIME__", pubtime)\
        .replace("__TAG0__", tag0)\
        .replace("__TAG1__", tag1)\
        .replace("__TAG2__", tag2)\
        .replace("__DATE__", date_label)\
        .replace("__NUM__", str(num))\
        .replace("__FAQS__", faqs_json)\
        .replace("__BODY__", body_html + FOOTER_HTML)\
        .replace("__STYLE__", STYLE)


# ---------- INDEX / BLOG / SITEMAP WIRING ----------
INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")
ANCHOR_166_END = "blog/blog-ribbon-oem-166-module-brand-buyer-mill-side-make-or-buy-bow-assembly-hand-tie-vs-pre-tied-architecture-global-brand-procurement-2026-09-24-pm.html"

ENTRIES = [
    {
        "file": FILE_167,
        "title": "Mill-Side Seasonality Cascade — Holiday + Non-Holiday Capacity Pre-Booking Architecture",
        "desc": "B2B ribbon OEM 167-module mill-side seasonality cascade architecture. Holiday + non-holiday capacity pre-booking, 12-month calendar lock, multi-market brand carve-out, Q4 peak surge rules.",
        "short": "Mill-side seasonality cascade for ribbon OEM — 12-month capacity calendar, 4 cascade-priority tiers, multi-market carve-out, Q4 surge budget rules.",
        "date": DISPLAY_AM,
        "iso_date": ISO_AM,
        "num": 7,
    },
    {
        "file": FILE_168,
        "title": "Brand-Buyer 7-Stage Brief-to-Shelf Onboarding Playbook for Ribbon OEM",
        "desc": "B2B ribbon OEM 168-module brand-buyer mill-side 7-stage brief-to-shelf onboarding playbook. RFQ, sample, color match, pre-production, PPAP, first PO, replenishment cadence.",
        "short": "Brand-buyer 7-stage brief-to-shelf onboarding playbook for ribbon OEM — 90-day sequence from RFQ to replenishment cadence with deliverables and pitfalls at each stage.",
        "date": DISPLAY_PM,
        "iso_date": ISO_PM,
        "num": 8,
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
    if ANCHOR_166_END not in html:
        raise SystemExit(f"ANCHOR_166_END ({ANCHOR_166_END}) not found in index.html")
    idx = html.find(f'href="{ANCHOR_166_END}"')
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
    pattern = (
        r'(<a href="' + ANCHOR_166_END.replace("/", r"/") + r'" class="blog-read-more">Read More &rarr;</a>\s*</article>)'
    )
    import re
    pat = re.compile(pattern)
    if not pat.search(html):
        raise SystemExit("blog anchor (166) not found in blog.html")
    cards = "".join(make_blog_card(e) for e in ENTRIES)
    new_html = pat.sub(lambda m: m.group(1) + cards, html, count=1)
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
    if e["num"] == 7:
        tags = TAGS_167
        keywords = KEYWORDS_167
        faqs_json = FAQS_167
        body = BODY_167
        title_display = DISPLAY_TITLE_167
    else:
        tags = TAGS_168
        keywords = KEYWORDS_168
        faqs_json = FAQS_168
        body = BODY_168
        title_display = DISPLAY_TITLE_168
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
    write_article(
        ENTRIES[0],
        "Mill-Side Seasonality Cascade — Capacity Pre-Booking 2026",
        "B2B ribbon OEM 167-module mill-side seasonality cascade architecture. Holiday + non-holiday capacity pre-booking, 12-month calendar lock, multi-market brand carve-out. Smith Ribbon OEM since 2004.",
        "Seasonality Cascade for Ribbon OEM | B2B 2026",
        "B2B ribbon OEM 167-module seasonality cascade: 12-month capacity calendar, 4 cascade tiers, Q4 surge budget rules, multi-market carve-out. Smith Ribbon since 2004.",
    )
    write_article(
        ENTRIES[1],
        "Brand-Buyer 7-Stage Brief-to-Shelf Onboarding Playbook 2026",
        "B2B ribbon OEM 168-module brand-buyer mill-side 7-stage brief-to-shelf onboarding playbook. RFQ, sample, color match, pre-production, PPAP, first PO, replenishment cadence. Smith Ribbon OEM since 2004.",
        "7-Stage Brief-to-Shelf Onboarding Playbook | B2B OEM 2026",
        "B2B ribbon OEM 168-module 7-stage brief-to-shelf onboarding playbook for ribbon OEM. RFQ to replenishment cadence, deliverables, common pitfalls. Smith Ribbon since 2004.",
    )
    update_index()
    update_blog()
    update_sitemap()
    print("\nAll wired. Ready for git commit & push.")


if __name__ == "__main__":
    main()