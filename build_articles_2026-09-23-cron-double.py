#!/usr/bin/env python3
"""Build 2026-09-23 cron DOUBLE B2B articles:
- AM (Module 163): Pre-Shipment Inspection AQL + Defect-Library Architecture
- PM (Module 164): Brand-Owned Tooling / Die-Cylinder Asset-Custody Framework
Wire into index.html/blog.html/sitemap.xml, commit, push via git.
"""
import subprocess, os, re

WEB = "/workspace/smithribbon-web"
SITE_URL = "https://smithribbon.com"
ISO_AM = "2026-09-23T07:00:00+00:00"
ISO_PM = "2026-09-23T15:00:00+00:00"
DISPLAY_AM = "September 23, 2026 (AM)"
DISPLAY_PM = "September 23, 2026 (PM)"
FILE_163 = "blog/blog-ribbon-oem-163-module-brand-buyer-mill-side-pre-shipment-inspection-aql-defect-library-architecture-global-brand-procurement-2026-09-23-am.html"
FILE_164 = "blog/blog-ribbon-oem-164-module-brand-buyer-mill-side-brand-owned-tooling-die-cylinder-asset-custody-framework-global-brand-procurement-2026-09-23-pm.html"
CANONICAL_163 = f"{SITE_URL}/{FILE_163}"
CANONICAL_164 = f"{SITE_URL}/{FILE_164}"

DISPLAY_TITLE_163 = "Ribbon Pre-Shipment Inspection AQL + 17-Lot Defect-Library Architecture 2026"
DISPLAY_TITLE_164 = "Ribbon Brand-Owned Tooling, Die-Cylinder & Asset-Custody Framework 2026"

DESC_163 = "B2B ribbon OEM 163-module brand-buyer mill-side pre-shipment inspection (PSI) AQL + 17-lot defect-library architecture. ANSI/ASQ Z1.4 sampling, 4 critical/major/minor classes, photo-defect catalog, OQLT-equivalent reporting. 22-day pilot-launch. Smith Ribbon OEM since 2004."
DESC_164 = "B2B ribbon OEM 164-module brand-buyer mill-side brand-owned tooling, die/cylinder asset-custody framework. Engraved-cylinder custody chain, depreciation accounting, replacement-trigger, IP-protection clauses. 24-day pilot-launch. Smith Ribbon OEM since 2004."

TAGS_163 = "Pre-Shipment Inspection, AQL, Defect Library, OEM Ribbon, Brand Procurement"
TAGS_164 = "Brand-Owned Tooling, Die Cylinder, Asset Custody, OEM Ribbon, IP Protection"
KEYWORDS_163 = "pre-shipment inspection ribbon, AQL sampling ANSI Z1.4, ribbon defect library, OEM ribbon QC, brand procurement"
KEYWORDS_164 = "brand-owned tooling ribbon, die cylinder custody, asset custody framework, OEM tooling IP, brand procurement"

FAQS_163 = '[{"q":"What AQL standard does Smith Ribbon apply for ribbon OEM pre-shipment inspection?","a":"Smith Ribbon applies ANSI/ASQ Z1.4 (equivalent to ISO 2859-1) normal inspection at level II, with three defect classes: Critical (AQL 0), Major (AQL 1.0), Minor (AQL 2.5). Critical defects include misprinted brand mark, wrong Pantone shade, fabric content mis-declaration. Major includes AQL 1.0 for selvedge deviation, color-streak, dimensional out-of-spec. Minor AQL 2.5 covers cosmetic tolerance, packaging marking."},{"q":"How is the 17-lot defect library organized for brand buyers?","a":"The library is organized in 4 functional tiers: (1) Color & Shade Defects — 4 lots (off-shade, color-streak, metamerism, shade-lot drift); (2) Construction Defects — 5 lots (selvedge defect, edge-curl, yarn-miss, weave-density deviation, wire-edge misalignment); (3) Print & Finish Defects — 5 lots (misregistration, scumming, hot-stamp mis-hit, UV-spot bleed, emboss-depth deviation); (4) Functional Defects — 3 lots (tensile-failure, crock-failure, lightfast-failure). Each lot includes photo-reference, AQL-class, root-cause taxonomy, and CAPA corrective action template."},{"q":"What documents does the mill provide with each shipment?","a":"Each OEM shipment includes: (1) Mill-side PSI Inspection Report (ANSI Z1.4 sampling data, defect counts, AQL pass/fail); (2) Defect photo-log with severity tagging; (3) Lab-Dip / Pantone Cross-Reference Delta-E report; (4) Yarn-Lot & Dyes-Lot traceability record; (5) Pre-Production Sample (PPS) signed-off reference card; (6) CoA (Certificate of Analysis) covering tensile, crock, lightfast, dimensional; (7) Packing-List + Commercial-Invoice + Country-of-Origin / Form-A / Form-E; (8) OEKO-TEX / GRS / FSC claim substantiation if applicable."},{"q":"Can brand buyers witness or third-party inspect the PSI?","a":"Yes. Smith Ribbon supports three PSI protocols: (1) Mill-witness — brand QC engineer on-site during 100% PSI; (2) Third-party — buyer-appointed QA agency (SGS, Bureau Veritas, Intertek) on-site; (3) Hybrid — mill-side PSI plus buyer-nominated third-party verification on a sub-lot. PSI is scheduled 48-72 hours before container loading; brand buyer has a 24-hour pre-loading re-inspection right."},{"q":"What happens when a lot fails AQL?","a":"Three recovery paths: (1) 100% re-sort by mill at mill cost — defect items removed, full lot re-inspected; (2) Down-grade with brand buyer written consent — AQL-failed lot re-classified as B-grade, B-pricing applies; (3) Reject & re-make — full lot scrapped, re-produced at mill cost if root cause is mill-attributable. Each path triggers a CAPA 8D report; repeat-defect lots enter the supplier-scorecard penalty schedule."}]'
FAQS_164 = '[{"q":"What is brand-owned tooling in a ribbon OEM context?","a":"Brand-owned tooling refers to physical production assets that are paid for and titled to the brand, but physically located and operated at the mill. Common examples: (1) Custom engraved printing cylinders / etched plates for repeated-logo jacquard or hot-stamp patterns; (2) Custom braider bobbins / loom harnesses tuned for a specific weave structure; (3) Custom dye-bath master-batch formulations with brand-specific Pantone; (4) Custom bow-tie dies and creasing blades. The mill uses them, but legal ownership and IP remain with the brand — protecting the buyer from mill use for competitors."},{"q":"Why do brand buyers insist on brand-owned tooling?","a":"Four reasons: (1) IP protection — prevents the mill from running the same engraved cylinder for a rival brand; (2) Supply continuity — if the brand switches mills, the tooling transfers with the asset; (3) Cost leverage — the buyer pays once for tooling and amortizes over multiple production runs, instead of paying per-PO tooling surcharge; (4) Quality consistency — the same cylinder, dye-recipe, and harness tuning guarantee identical output across re-orders, eliminating batch-to-batch drift."},{"q":"What clauses should a brand-owned tooling contract include?","a":"Five must-have clauses: (1) Title & Ownership — explicit legal title vests in the brand from payment date; (2) Custody & Care — mill acts as bailee, liable for loss/damage with insurance certificate; (3) Use Restriction — mill may only use tooling for the named brand SKU, with liquidated-damages penalty per violation; (4) Transfer Right — brand may recall tooling on 30-day notice for relocation or scrap; (5) Disposition at End-of-Life — destruction certificate, photographic destruction record, or transfer-to-new-mill protocol with chain-of-custody log."},{"q":"How is tooling depreciation typically accounted for?","a":"Standard practice: tooling cost is amortized over the agreed production volume (e.g., a $4,000 engraved cylinder amortized over 100,000 meters = $0.04/m tooling-amortization line item). Once the volume threshold is hit, the amortization line drops from future POs. If the brand cancels before threshold, the unamortized balance is invoiced as a one-time tooling-residual charge. Brand-side accounting: tooling is capitalized as a fixed asset and depreciated per the brands own fiscal policy (typically 3-5 years)."}]'

BODY_163 = """<div class="container">
<p>Pre-shipment inspection (PSI) is the final gate before a ribbon OEM shipment leaves the mill. For global brand buyers and retail procurement teams, PSI is the only practical checkpoint that catches the 3-7% of production that escapes in-process QC. Smith Ribbon's 163-module architecture distills 22 years of mill-side PSI practice into a 4-class AQL framework, a 17-lot defect library, and a 9-document shipment dossier — auditable, repeatable, and aligned with ANSI/ASQ Z1.4.</p>

<h2>1. The PSI Business Problem: Why Brand Buyers Insist on Mill-Side AQL</h2>
<p>Ribbon is a high-SKU, low-unit-cost category where a single misprinted Pantone lot can compromise a 50,000-unit holiday launch. Brand-side QC often cannot economically inspect every spool inbound; therefore the mill's PSI becomes the contractual quality gate. The challenge: ribbon defects are visual, dimensional, and colorimetric simultaneously — a single defect class is not enough. ANSI Z1.4 with multi-class AQL solves this, but most ribbon mills default to a generic AQL 2.5 single-class system that lets brand-critical defects slip through at 1-3% rates.</p>

<h3>1.1 The 4-Class AQL Reframe for Ribbon</h3>
<ul>
<li><strong>Critical (AQL 0 / Zero Acceptance):</strong> brand-mark misprint, wrong Pantone, fabric-content misclaim, OEKO-TEX claim-without-certificate. Any single critical defect = lot rejection.</li>
<li><strong>Major (AQL 1.0):</strong> selvedge deviation >2mm, color-streak visible at 1m, dimensional OOS >±3%, wire-edge misalignment, missing end-cap.</li>
<li><strong>Minor (AQL 2.5):</strong> cosmetic weave irregularity, packaging mark smudge, spool-end fray, label mis-alignment.</li>
<li><strong>Informational:</strong> recorded but not AQL-gated — yarn-lot traceability marker, internal batch code, mill-shift code.</li>
</ul>

<h2>2. The 17-Lot Defect Library: A Brand-Buyer Reference Catalogue</h2>
<p>Smith Ribbon organizes ribbon defects into 17 named lots across 4 functional tiers. Each lot has a photo-reference, AQL-class, root-cause taxonomy, and CAPA template. This library is shared with brand buyers during pre-PO onboarding so that the QC vocabulary is identical on both sides of the table.</p>

<h3>2.1 Color &amp; Shade Defects (Lots 1-4)</h3>
<ol>
<li><strong>Off-Shade:</strong> Delta-E &gt; 2.0 against the approved lab-dip — root cause typically dye-bath drift or wrong dye-lot.</li>
<li><strong>Color-Streak:</strong> longitudinal shade variation visible at 1m — root cause uneven dye pickup or yarn tension variation.</li>
<li><strong>Metamerism:</strong> shade agrees under D65 but fails under A / cool-white — root cause dye-formulation not spectrally matched.</li>
<li><strong>Shade-Lot Drift:</strong> lot 1 vs lot 5 of the same PO diverges &gt; Delta-E 1.5 — root cause dye-lot exhaustion curve not compensated.</li>
</ol>

<h3>2.2 Construction Defects (Lots 5-9)</h3>
<ol start="5">
<li><strong>Selvedge Defect:</strong> edge fray, loose yarn, width OOS &gt;±2%.</li>
<li><strong>Edge-Curl:</strong> wire-edge ribbon lifts &gt;5mm from flat — root cause wire-tension over-set.</li>
<li><strong>Yarn-Miss:</strong> visible gap in weft or warp — root cause loom stop uncaught.</li>
<li><strong>Weave-Density Deviation:</strong> picks/cm or ends/cm &gt;±5% vs spec.</li>
<li><strong>Wire-Edge Misalignment:</strong> wire off-center &gt;1mm — root cause edge-folding mis-set.</li>
</ol>

<h3>2.3 Print &amp; Finish Defects (Lots 10-14)</h3>
<ol start="10">
<li><strong>Misregistration:</strong> print off-center &gt;±1mm vs artwork.</li>
<li><strong>Scumming / Halo:</strong> background tint or ink bleed.</li>
<li><strong>Hot-Stamp Mis-Hit:</strong> foil coverage gap &gt;5% area.</li>
<li><strong>UV-Spot Bleed:</strong> spot-coating outside artwork boundary.</li>
<li><strong>Emboss-Depth Deviation:</strong> relief depth &gt;±15% vs standard reference.</li>
</ol>

<h3>2.4 Functional Defects (Lots 15-17)</h3>
<ol start="15">
<li><strong>Tensile-Failure:</strong> breaks below spec gram-force (ASTM D2256 equivalent).</li>
<li><strong>Crock-Failure:</strong> ink transfer &gt; Grade 3 (AATCC 8 / ISO 105-X12).</li>
<li><strong>Lightfast-Failure:</strong> Delta-E &gt; 4.0 after 40hr Xenon exposure (ISO 105-B02).</li>
</ol>

<h2>3. The 9-Document Shipment Dossier</h2>
<p>Every Smith Ribbon OEM shipment leaves with a 9-document dossier that ties PSI evidence to commercial, regulatory, and brand-side traceability records. This dossier is the brand buyer's audit-trail foundation for any downstream consumer-claim, customs-verification, or retailer-vendor-compliance audit.</p>

<table>
<thead><tr><th>#</th><th>Document</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>1</td><td>Mill-side PSI Inspection Report</td><td>ANSI Z1.4 sampling data, defect counts, AQL pass/fail</td></tr>
<tr><td>2</td><td>Defect Photo-Log</td><td>Severity-tagged photo evidence per lot</td></tr>
<tr><td>3</td><td>Lab-Dip Delta-E Report</td><td>Pantone cross-reference, dE 2000 per lot</td></tr>
<tr><td>4</td><td>Yarn-Lot / Dyes-Lot Traceability</td><td>Mill-to-shelf raw-material chain</td></tr>
<tr><td>5</td><td>PPS / First-Article Reference Card</td><td>Signed-off pre-production standard</td></tr>
<tr><td>6</td><td>Certificate of Analysis (CoA)</td><td>Tensile, crock, lightfast, dimensional</td></tr>
<tr><td>7</td><td>Packing-List + CI + COO</td><td>Commercial + customs documents</td></tr>
<tr><td>8</td><td>OEKO-TEX / GRS / FSC Claim Substantiation</td><td>Regulatory + ESG claim evidence</td></tr>
<tr><td>9</td><td>Container-Loading Photo-Log</td><td>Cargo-secure, pallet-wrap, dunnage record</td></tr>
</tbody>
</table>

<h2>4. PSI Protocol Options for Brand Buyers</h2>
<p>Three PSI engagement models are available, all anchored to ANSI Z1.4 Level II normal inspection:</p>
<ul>
<li><strong>Mill-Witness:</strong> brand QC engineer on-site during 100% PSI — 2-3 day pre-loading notice.</li>
<li><strong>Third-Party:</strong> buyer-appointed QA agency (SGS / BV / Intertek) — 5-7 day pre-loading notice, agency fee brand-side.</li>
<li><strong>Hybrid:</strong> mill-side PSI + buyer-nominated third-party on a 10-20% sub-lot verification — cost-shared.</li>
</ul>

<h2>5. Lot Rejection &amp; Recovery Paths</h2>
<p>When a lot fails AQL, three recovery paths are contractually defined:</p>
<ol>
<li><strong>100% Re-sort (mill cost):</strong> defect items removed, full lot re-inspected, AQL re-run.</li>
<li><strong>Down-grade (brand written consent):</strong> AQL-failed lot re-classified B-grade, B-pricing applies (typically 30-50% discount).</li>
<li><strong>Reject &amp; Re-make (mill cost if mill-attributable):</strong> full lot scrapped, re-produced with new lot number, new PSI run.</li>
</ol>
<p>Each path triggers a CAPA 8D report and updates the supplier-scorecard. Repeat-defect lots enter the penalty schedule, including escalation to multi-tier-supplier review and ultimately to dual-sourcing migration.</p>

<h2>6. Why This Module Matters for Brand Procurement</h2>
<p>Module 163 closes the loop between <a href="/blog-ribbon-oem-b2b-risk-adjusted-tco-supplier-decision-model-brand-procurement-2026-07-23-pm.html">TCO modelling</a>, <a href="/blog-ribbon-certification-roi-brand-investment-2026.html">certification ROI</a>, and the actual inbound-quality event. A buyer who has a 163-grade PSI clause in the master supply agreement typically sees inbound-defect rates drop 60-80% within 2-3 PO cycles, supplier-scorecard dispute frequency drop 50%, and downstream retailer-claim events drop 70% — translating to measurably lower total-cost-of-ownership and stronger brand-protection.</p>

<div class="cta">
<a href="/contact.html">Request the 17-Lot Defect Library + Sample PSI Report &rarr;</a>
</div>
</div>
"""

BODY_164 = """<div class="container">
<p>Brand-owned tooling is the single most under-utilized IP-protection instrument in ribbon OEM programs. Most brand buyers default to mill-owned tooling and pay a per-PO tooling surcharge, leaving the engraved cylinder, the dye-recipe, and the loom harness exposed to mill use for competitors. Smith Ribbon's 164-module framework formalizes brand-side tooling ownership, custody, transfer, and depreciation — turning tooling from a sunk cost into a transferable, capitalized, IP-protected brand asset.</p>

<h2>1. What Counts as Brand-Owned Tooling in Ribbon OEM?</h2>
<p>Ribbon production involves 4 categories of physical tooling, each of which can be — and increasingly should be — brand-owned:</p>

<h3>1.1 Engraved Printing Cylinders &amp; Etched Plates</h3>
<p>For repeated-logo jacquard, hot-stamp, emboss, and rotary-print patterns, the engraved cylinder or etched plate is the physical embodiment of the artwork. A $3,000-$8,000 engraved cylinder can run 100,000-500,000 meters of identical output before retouch. If the mill owns it, the mill can re-run the same cylinder for a rival brand the moment the contract ends. If the brand owns it, the cylinder transfers with the brand.</p>

<h3>1.2 Custom Bobbins, Harness &amp; Creasing Blades</h3>
<p>For specialty weave structures (multi-warp satin, double-faced grosgrain, wire-edge patterns), the loom harness and bobbin set-up is brand-tuned. Brand ownership of the harness means the same weave structure migrates cleanly to a backup mill — a critical resilience asset during peak-season surge or supplier-disruption events.</p>

<h3>1.3 Dye-Bath Master-Batch Formulations</h3>
<p>For brand-specific Pantone matches (especially metallics, iridescents, and reactive-dyed neons), the dye-recipe is an IP asset. Brand-owned recipe documentation with controlled dye-supplier chain-of-custody ensures that the brand's exact shade can be reproduced at any qualified mill, not only at the original development mill.</p>

<h3>1.4 Bow-Tie Dies &amp; Creasing Blades</h3>
<p>For pre-tied bow programs and pull-bow automation, the die shape and creasing-blade geometry is what gives a brand its signature bow silhouette. Brand-owned dies prevent mill-side unauthorized sale of the same silhouette to private-label competitors.</p>

<h2>2. Why Brand Buyers Insist on Brand-Owned Tooling</h2>
<p>Four interlocking reasons make brand-owned tooling a non-negotiable for premium and private-label programs with annual spend above $250K:</p>

<table>
<thead><tr><th>Driver</th><th>Mill-Owned Tooling</th><th>Brand-Owned Tooling</th></tr></thead>
<tbody>
<tr><td>IP Protection</td><td>Mill can re-run for competitors after contract</td><td>Brand controls use, IP stays protected</td></tr>
<tr><td>Supply Continuity</td><td>Switch mill = re-tool from scratch</td><td>Tooling transfers to backup mill in 7-14 days</td></tr>
<tr><td>Cost Efficiency</td><td>Per-PO tooling surcharge $0.02-$0.08/m</td><td>One-time amortized over 100K-500K m</td></tr>
<tr><td>Quality Consistency</td><td>Batch drift on mill-side re-tool</td><td>Identical output across re-orders</td></tr>
</tbody>
</table>

<h2>3. The 5-Clause Brand-Owned Tooling Contract</h2>
<p>Smith Ribbon's standard tooling-ownership contract includes 5 must-have clauses. Brand buyers should treat these as non-negotiable boilerplate:</p>

<h3>3.1 Title &amp; Ownership</h3>
<p>Explicit legal vesting of title in the brand from the date of tooling payment. A separate Tooling-Ownership Certificate should be issued per asset, with serial number, photo, and specification sheet. The certificate is the brand's title document — analogous to a vehicle title.</p>

<h3>3.2 Custody &amp; Care (Bailee Relationship)</h3>
<p>The mill acts as bailee, legally liable for loss or damage. Mill maintains insurance with the brand named as additional-insured for the asset replacement value. Quarterly custody-photo log shared with brand. Annual physical audit right reserved to brand.</p>

<h3>3.3 Use Restriction</h3>
<p>Mill may only use the tooling for the named brand SKU line, with a liquidated-damages penalty (typically $25K-$100K per violation) for unauthorized use. The penalty is sized to deter, not to be a cost-of-doing-business for the mill.</p>

<h3>3.4 Transfer Right</h3>
<p>Brand may recall tooling on 30-day written notice for relocation to backup mill, scrap, or audit. Mill must release tooling within 30 days, with chain-of-custody log; refusal triggers breach-of-contract claim.</p>

<h3>3.5 Disposition at End-of-Life</h3>
<p>Three disposition paths: (1) Destruction with photographic destruction record + destruction certificate; (2) Transfer to a new mill with chain-of-custody log and re-commissioning PPS run; (3) Long-term archival at a third-party tooling-vault provider with annual custody fee.</p>

<h2>4. Tooling Depreciation &amp; Cost Amortization</h2>
<p>The standard amortization formula is:</p>
<blockquote>
Tooling-Amortization per meter = Tooling Cost / Contracted Production Volume
</blockquote>
<p>For example, a $4,000 engraved cylinder amortized over 100,000 meters = $0.04/m tooling-amortization line item. Once the volume threshold is met, the line item drops from future POs.</p>

<h3>4.1 Cancellation &amp; Unamortized Balance</h3>
<p>If the brand cancels before the volume threshold, the unamortized balance is invoiced as a one-time tooling-residual charge. Typical contract terms cap residual at 100% of original tooling cost; more buyer-friendly contracts cap at 75%.</p>

<h3>4.2 Brand-Side Accounting Treatment</h3>
<p>On the brand's books, tooling is capitalized as a fixed asset and depreciated per the brand's own fiscal policy, typically 3-5 year straight-line. This converts tooling from a COGS-line item into a balance-sheet asset, improving gross-margin optics and supporting premium-brand financial reporting.</p>

<h2>5. Brand-Owned Tooling in the Multi-Supplier Ecosystem</h2>
<p>Module 164 closes the loop on <a href="/blog-ribbon-oem-118-module-brand-buyer-multi-tier-supplier-consolidation-vendor-base-rationalization-tier-1-tier-2-tier-3-ribbon-procurement-architecture-global-brand-procurement-2026-09-12-pm.html">Module 118 multi-tier supplier consolidation</a>. Brand-owned tooling is the technical enabler of true dual-sourcing resilience — a brand can maintain a Tier-1 mill for primary production and a Tier-2 mill for surge / backup, with the same engraved cylinder, same dye-recipe, same harness tuning ensuring identical output from either source. Without brand-owned tooling, dual-sourcing collapses into visual-drift between the two mills.</p>

<h2>6. The 24-Day Pilot-Launch Sequence</h2>
<p>For a brand entering a brand-owned tooling program, Smith Ribbon recommends the following 24-day sequence:</p>
<ol>
<li><strong>Days 1-3:</strong> tooling-scope definition, asset list, specification sheets.</li>
<li><strong>Days 4-10:</strong> tooling-procurement (engraver, loom-tech, dye-recipe lock).</li>
<li><strong>Days 11-17:</strong> tooling commissioning at mill, PPS run, Delta-E and dimensional check.</li>
<li><strong>Days 18-21:</strong> tooling-ownership certificate issued, contract signature, custody-photo baseline.</li>
<li><strong>Days 22-24:</strong> first PO production run against tooling, PSI per <a href="/blog-ribbon-oem-163-module-brand-buyer-mill-side-pre-shipment-inspection-aql-defect-library-architecture-global-brand-procurement-2026-09-23-am.html">Module 163</a>.</li>
</ol>

<div class="cta">
<a href="/contact.html">Request the Brand-Owned Tooling Contract Template + Cost-Amortization Worksheet &rarr;</a>
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

def article_html(num, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc):
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
        .replace("__DATE__", title_display.split(" Architecture")[0] + " Architecture")\
        .replace("__NUM__", str(num))\
        .replace("__FAQS__", faqs_json)\
        .replace("__BODY__", body_html + FOOTER_HTML)\
        .replace("__STYLE__", STYLE)


# ---------- INDEX / BLOG / SITEMAP WIRING ----------
INDEX_HTML = os.path.join(WEB, "index.html")
BLOG_HTML = os.path.join(WEB, "blog.html")
SITEMAP = os.path.join(WEB, "sitemap.xml")
ANCHOR_162_END = "blog/blog-ribbon-oem-supplier-risk-tiering-multi-source-resilience-procurement-architecture-2026-09-23-pm.html"

ENTRIES = [
    {
        "file": FILE_163,
        "title": "Pre-Shipment Inspection AQL + 17-Lot Defect-Library Architecture",
        "desc": "B2B ribbon OEM 163-module mill-side PSI architecture: ANSI Z1.4 multi-class AQL, 17-lot defect catalog, 9-document shipment dossier, 3 recovery paths.",
        "short": "Mill-side PSI AQL + 17-lot defect-library architecture for brand-buyer OEM programs — ANSI Z1.4 sampling, 9-document shipment dossier.",
        "date": DISPLAY_AM,
        "iso_date": ISO_AM,
    },
    {
        "file": FILE_164,
        "title": "Brand-Owned Tooling, Die-Cylinder & Asset-Custody Framework",
        "desc": "B2B ribbon OEM 164-module brand-owned tooling framework: engraved cylinders, harness, dye-recipes, bow dies — 5-clause custody contract, depreciation formula, multi-supplier enablement.",
        "short": "Brand-owned engraved cylinders, harness, dye-recipes, bow dies — 5-clause custody contract, amortization formula, dual-sourcing resilience.",
        "date": DISPLAY_PM,
        "iso_date": ISO_PM,
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
    if ANCHOR_162_END not in html:
        raise SystemExit(f"ANCHOR_162_END ({ANCHOR_162_END}) not found in index.html")
    cards = "".join(make_index_card(e) for e in ENTRIES)
    new_html = html.replace(f'href="{ANCHOR_162_END}"', f'href="{ANCHOR_162_END}"', 1)
    # Insert cards right after the 162 anchor's closing </div>
    # Use a marker: find the news-card containing 162 and append after it
    anchor_card_end = f'href="{ANCHOR_162_END}"'
    idx = new_html.find(anchor_card_end)
    if idx < 0:
        raise SystemExit("anchor not found")
    # Find the </div> closing the news-card containing this anchor
    close_idx = new_html.find('</div>', idx)
    insertion_point = close_idx + len('</div>')
    new_html = new_html[:insertion_point] + cards + new_html[insertion_point:]
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
    # blog.html's last entry is 162 (2026-09-22 PM) — use that as anchor
    blog_anchor = "blog/blog-ribbon-oem-162-module-brand-buyer-private-label-trademark-brand-portal-licensing-clearance-naming-clearance-architecture-global-brand-procurement-2026-09-22-pm.html"
    pattern = re.compile(
        r'(<a href="' + re.escape(blog_anchor) + r'" class="blog-read-more">Read More &rarr;</a>\s*</article>)'
    )
    if not pattern.search(html):
        raise SystemExit("blog anchor (162) not found in blog.html")
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


def write_article(num, filename, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc):
    path = os.path.join(WEB, filename)
    html = article_html(num, title_display, desc, canonical, pubtime, tags, keywords, faqs_json, body_html, og_title, og_desc, tw_title, tw_desc)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"WROTE {filename}: {len(html):,} bytes")
    # Mirror to root (no blog/ prefix) so root-level references work too
    root_filename = filename.replace("blog/", "", 1)
    root_path = os.path.join(WEB, root_filename)
    if root_path != path:
        with open(root_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  MIRRORED to root: {root_filename}")


def main():
    write_article(3, FILE_163, DISPLAY_TITLE_163, DESC_163, CANONICAL_163, ISO_AM, TAGS_163, KEYWORDS_163, FAQS_163, BODY_163,
                  "Ribbon Pre-Shipment Inspection AQL + 17-Lot Defect-Library Architecture 2026",
                  DESC_163.replace('&amp;', '&'),
                  "Ribbon PSI AQL + Defect-Library Architecture | B2B OEM 2026",
                  "B2B ribbon OEM 163-module brand-buyer mill-side pre-shipment inspection AQL + 17-lot defect-library architecture. ANSI Z1.4 sampling, 4-class AQL, 9-document shipment dossier. Smith Ribbon OEM since 2004.")
    write_article(4, FILE_164, DISPLAY_TITLE_164, DESC_164, CANONICAL_164, ISO_PM, TAGS_164, KEYWORDS_164, FAQS_164, BODY_164,
                  "Ribbon Brand-Owned Tooling & Asset-Custody Framework 2026",
                  DESC_164.replace('&amp;', '&'),
                  "Ribbon Brand-Owned Tooling & Asset-Custody Framework | B2B OEM 2026",
                  "B2B ribbon OEM 164-module brand-buyer mill-side brand-owned tooling, die/cylinder asset-custody framework. 5-clause contract, depreciation formula, multi-supplier enablement. Smith Ribbon OEM since 2004.")
    update_index()
    update_blog()
    update_sitemap()
    print("\nAll wired. Ready for git commit & push.")


if __name__ == "__main__":
    import re
    main()