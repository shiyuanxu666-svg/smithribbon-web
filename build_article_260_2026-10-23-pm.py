#!/usr/bin/env python3
"""Build smithribbon B2B module 260 (PM), 2026-10-23.

Topic: mill-side PICK / DENSITY & WARP-COUNT interlock — the woven-structure
parameters that decide ribbon weight, hand-feel and cost-per-metre, and how a brand
buyer controls them across a multi-season program.
"""
from pathlib import Path
import sys

sys.path.insert(0, "/workspace/smithribbon-web")
from sr_page import write_article

SLUG = ("blog-ribbon-oem-260-module-mill-side-brand-buyer-ribbon-pick-density-warp-count-end-down-"
        "interlock-architecture-weight-cost-per-metre-governance-global-brand-procurement-2026-10-23-pm")

a = {
    "title": "Mill-Side Brand-Buyer Ribbon Pick-Density, Warp-Count &amp; End-Down Interlock Architecture "
             "&mdash; Weight, Hand-Feel and Cost-Per-Metre Governance for Global Brand Procurement 2026",
    "desc": "B2B ribbon OEM 260-module pick-density, warp-count and end-down interlock architecture. "
            "6-layer woven-structure authority model, 4-stage construction approval gate, 3-tier "
            "weight-and-cost reconciliation ladder, and a pick-deviation early-warning threshold. "
            "Smith Ribbon OEM since 2004.",
    "kw": "ribbon pick density, ribbon warp count, ribbon end down, woven ribbon construction, "
          "ribbon weight per metre, ribbon GSM, satin ribbon OEM, grosgrain construction, "
          "ribbon cost per metre, ribbon hand feel specification, private label ribbon, "
          "ribbon loom settings, fabric count ribbon",
    "author": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
    "date_iso": "2026-10-23T15:00:00+00:00",
    "date_human": "October 23, 2026",
    "slug": SLUG,
    "section": "Ribbon OEM Manufacturing",
    "tag": "Ribbon OEM",
    "read": "15 min read",
    "word_count": 2500,
}

BODY = """
<p class="lede">Every other variable in a ribbon program &mdash; colour, print, finish, packaging &mdash;
is downstream of one number that most buyers never write down: the woven construction. Pick density
and warp count determine the ribbon's weight per metre, its hand-feel, its drape, its price, and its
abrasion life. Change them and you have effectively launched a different product. This module is
about controlling them like the fixed parameters they are, rather than discovering them in a landed
cost that came in 12% over plan.</p>

<h2>1. Why Construction Is the Specification Nobody Writes</h2>

<p>A typical ribbon tech pack from a brand buyer reads like this:</p>

<blockquote style="border-left:4px solid #b8854a;padding:8px 16px;margin:1.2em 0;background:#faf6f1;">
&quot;1&ndash;5/8&quot; satin ribbon, 100% polyester, Pantone 294 C, single-side print, 500&nbsp;m per
carton, target FOB Xiamen.&quot;
</blockquote>

<p>Every one of those attributes is measurable and checkable. None of them tell you how the ribbon
feels in the hand, how it drapes over a gift box corner, whether the selvedge will fray during the
customer's converting, or why the same quote came back 12% higher last quarter. Those outcomes are
determined by the woven construction &mdash; and construction is described, in mill documents, by
densities, ends and picks.</p>

<h3>The three numbers that actually matter</h3>

<p><strong>Ends per inch (EPI)</strong> is the warp count. More ends means a denser, more stable,
heavier ribbon with better selvedge strength and lower abrasion. <strong>Picks per inch (PPI)</strong>
is the weft insertion rate, which controls how tightly the structure is packed and therefore how
firm the hand-feel is. <strong>Total picks per centimetre</strong> is what the mill actually programs
into the loom, and it is the number that governs how far the loom can run without a pick miss.</p>

<p>These are not interchangeable. A satin ribbon's sheen comes from a <em>floating warp</em> structure
&mdash; long warp floats over many picks &mdash; which is why satin picks-per-inch is far lower than
its ends-per-inch would suggest. A grosgrain is the opposite: a firm ribbed weft structure with high
ppi. Same fibres, same width, completely different hand-feel, weight and cost.</p>

<div class="kpi">
  <p><strong>Rule of thumb:</strong> a 10% increase in pick density typically adds 6&ndash;9% to
  material cost and 4&ndash;7% to loom cycle time. It is the cheapest performance upgrade available
  &mdash; and the easiest thing for a mill to quietly drop when a program gets tight.</p>
</div>

<h2>2. The 6-Layer Woven-Structure Authority Model</h2>

<p>As with any multi-mill program, the first requirement is to know who may change what. Construction
parameters are assigned across six layers, each with a different owner and a different threshold.</p>

<table>
  <thead>
    <tr><th>Layer</th><th>Parameter</th><th>Owner</th><th>Change threshold</th></tr>
  </thead>
  <tbody>
    <tr><td>L1</td><td>Fibre type and denier (e.g. 150D/48F PET)</td><td>Brand, frozen at FAI</td>
        <td>None. Substitution requires re-qualification.</td></tr>
    <tr><td>L2</td><td>Ends per inch (warp count)</td><td>Mill weaving, brand co-sign</td>
        <td>&plusmn;2 ends/inch without notice</td></tr>
    <tr><td>L3</td><td>Picks per inch (weft count)</td><td>Mill weaving, brand co-sign</td>
        <td>&plusmn;3 picks/inch without notice</td></tr>
    <tr><td>L4</td><td>Weave pattern / float length (satin vs. grosgrain vs. organza)</td>
        <td>Brand, frozen at FAI</td><td>None without new sample round</td></tr>
    <tr><td>L5</td><td>Loom class, reed, harness, tension window</td><td>Mill, internal only</td>
        <td>Mill notifies brand on change of loom class</td></tr>
    <tr><td>L6</td><td>Width and picks-per-cm programme (the actual loom setting)</td>
        <td>Mill, brand informed</td><td>Deviation beyond agreed pick tolerance</td></tr>
  </tbody>
</table>

<p>The critical discipline is at <strong>L2 and L3</strong>. These are the two numbers a mill can
adjust most easily on a running programme &mdash; a change of reed or a change in weft insertion
rate is a loom adjustment, not a machine purchase &mdash; and they are also the two that most
directly move weight, hand-feel and cost. A buyer who has not co-signature authority at L2/L3 has,
in practice, outsourced their most important specification.</p>

<h3>Why L1 is genuinely frozen</h3>

<p>Fibre substitution is the substitution buyers hear about most &mdash; "the mill offered us a
recycled RPET at the same price". It is also the substitution that most often fails downstream.
Recycled and virgin polyester differ in dye uptake, surface hand, abrasion behaviour and shrinkage.
A fibre swap made to hold a price will show up as a hand-feel complaint, a colour-drift complaint, or
a converting problem six weeks later. Freeze L1 and force any change through a full re-qualification.</p>

<h2>3. The 4-Stage Construction Approval Gate</h2>

<p>Construction is approved before colour, and this ordering matters. A buyer who locks Pantone 294 C
first and accepts whatever construction the mill proposes will spend the next three rounds chasing a
colour that was never achievable on the proposed structure &mdash; because sheen, pick density and
fibre together determine which colours are reproducible.</p>

<h3>Stage 1 &mdash; Construction brief (no colour)</h3>
<p>Specify fibre, ends/inch, picks/inch, weave pattern, finished width and target weight per metre.
No colour reference at all. The mill returns a construction sample plus a weight statement. This
stage exists to settle <em>what the fabric is</em> before anyone argues about <em>what colour it
is</em>.</p>

<h3>Stage 2 &mdash; Hand-feel reference and weight reconciliation</h3>
<p>Receive the construction sample and measure weight per metre on a calibrated balance across three
cuts. Compare against the theoretical weight implied by EPI, PPI and denier. A deviation beyond 5%
between theoretical and actual is the signal that the mill is running a different construction from
the one you specified &mdash; and it is far cheaper to catch here than at a pre-shipment inspection.</p>

<h3>Stage 3 &mdash; Convertibility trial</h3>
<p>Run the construction sample through the actual converting operation &mdash; winding onto the
customer's bobbin, folding through a bow machine, or feeding a bag-sealing line. Construction that
passes a hand-feel check can still fail here: high-construction ribbons can be stiff, can crease at
the slitter, and can generate more static and dust. This stage is skipped by most buyers and should
not be.</p>

<h3>Stage 4 &mdash; Construction freeze at FAI</h3>
<p>L1, L2, L3 and L4 are locked and signed. Colour development proceeds against a now-fixed
structure. From this point the construction numbers go into the quality agreement verbatim, and any
movement becomes a non-conformance rather than a conversation.</p>

<h2>4. The 3-Tier Weight-and-Cost Reconciliation Ladder</h2>

<p>Buyers discovering a construction drift usually discover it through a price variance. The ladder
below turns that variance into a diagnosis.</p>

<h3>Tier 1 &mdash; Reconcile the physical</h3>
<p>Before arguing about money, establish the physical facts. Weigh the delivered ribbon. Count ends
and picks on a section using a pick glass or a loupe. Measure width with a micrometer. If measured
weight is above nominal, the mill has over-constructed; if below, it has under-constructed. In our
experience most price disputes at this stage are measurement disagreements, not disagreements about
intent.</p>

<h3>Tier 2 &mdash; Reconcile the arithmetic</h3>
<p>Rebuild the cost from first principles: yarn consumption per metre (derivable from denier, EPI and
PPI), dye and finishing cost, conversion cost, and overhead. Compare to the invoiced figure. A mill
running a heavier yarn than specified shows up immediately as a yarn-consumption divergence. This is
also where an FX or energy surcharge should be visible as a separate line &mdash; if it is buried
inside a unit-price increase, the mill has an incentive problem you should address contractually.</p>

<h3>Tier 3 &mdash; Reconcile the commercial</h3>
<p>Only when Tiers 1 and 2 are settled should the conversation become commercial: is this a
one-off adjustment, or does the programme now sit on a different economics basis? Answer honestly.
A programme that was priced at 40 EPI is not the same programme as one at 43 EPI, and pretending
otherwise for eight months rarely ends well for either side.</p>

<div class="kpi">
  <p><strong>Diagnostic shortcut:</strong> weight up + price up, with no construction change on paper
  = <em>over-construction</em>. Weight flat + price up = a <em>cost or surcharge issue</em>, and
  belongs in Tier 2. Weight down + price flat = the most dangerous case &mdash; <em>under-construction</em>,
  which usually surfaces later as an abrasion or fray complaint.</p>
</div>

<h2>5. Pick-Deviation Early-Warning Threshold</h2>

<p>Construction drift is measurable continuously. A buyer running a multi-season programme should
track two derived indicators per lot.</p>

<p><strong>Construction variance index (CVI)</strong> compares actual weight per metre against the
frozen nominal, normalised so that a reading of 1.000 is on-target. A CVI above 1.05 or below 0.95
triggers a review.</p>

<p><strong>Pick-deviation count</strong> tracks observed pick misses and ends-down per 100&nbsp;metres.
A rising trend here is an early signal of loom-setting drift &mdash; before weight has moved
measurably. Pick misses are cheap to detect and expensive to ignore, because they produce visible
striped defects that a brand customer will attribute to printing.</p>

<table>
  <thead><tr><th>Indicator</th><th>Green</th><th>Amber</th><th>Red</th></tr></thead>
  <tbody>
    <tr><td>Construction variance index (CVI)</td><td>0.98&ndash;1.02</td><td>0.95&ndash;0.98 / 1.02&ndash;1.05</td>
        <td>Below 0.95 / above 1.05</td></tr>
    <tr><td>Pick-deviation count per 100&nbsp;m</td><td>0&ndash;1</td><td>2&ndash;4</td><td>5+</td></tr>
    <tr><td>Selvedge fray rate (per 1,000&nbsp;m)</td><td>0&ndash;2</td><td>3&ndash;6</td><td>7+</td></tr>
    <tr><td>Width variance from nominal</td><td>&plusmn;0.2&nbsp;mm</td><td>&plusmn;0.2&ndash;0.4&nbsp;mm</td>
        <td>&gt;&plusmn;0.4&nbsp;mm</td></tr>
  </tbody>
</table>

<p>Two consecutive amber readings, or any single red reading, should trigger a hold-and-investigate
before the lot moves into assembly. The cost of holding one lot is a few hours. The cost of a
multi-season programme quietly running 6% heavy on a nominally fixed construction is not.</p>

<h2>6. Five Failure Modes, Diagnosed</h2>

<h3>Failure mode 1 &mdash; The price rise with no paper change</h3>
<p>The most common case by a wide margin. Construction was never actually frozen with co-signature
authority, so the mill adjusted EPI to manage a yarn cost or capacity issue. Detection: weight up,
specification unchanged. Fix: this is a contract problem, not a technical one &mdash; which is exactly
why L2/L3 co-signature must exist before the first order.</p>

<h3>Failure mode 2 &mdash; Under-construction that looks fine at inspection</h3>
<p>The mill is running lighter to protect margin. The ribbon passes a visual check, passes a
colour check and passes a hand-feel check at the counter &mdash; and then fails in the customer's
converting line with selvedge fraying and abrasion failures. Detection: CVI consistently below 0.95
with amber pick-deviation counts. Fix: reject and re-establish; do not accept a price concession in
lieu of compliant construction, because the failure mode lands on the retailer, not on you.</p>

<h3>Failure mode 3 &mdash; Construction drift across a multi-mill programme</h3>
<p>You qualify two mills for capacity redundancy. They build subtly different fabric, because each
interpreted the construction brief in its own standard. Product shipped from mill B does not quite
match mill A, and the inconsistency surfaces in reviews. Detection: side-by-side weight and pick
count across mill lots. Fix: specify EPI/PPI/denier absolutely rather than as a range, and require
each mill to submit a construction sample through the same Stage 1&ndash;4 gate.</p>

<h3>Failure mode 4 &mdash; Construction approved before colour feasibility</h3>
<p>The mill proposes a construction that is perfectly acceptable structurally but cannot hold the
target Pantone repeatably &mdash; typically a low-pick satin that cannot achieve saturation, or a
sheen level that shifts the perceived hue. Detection: lab-dip ΔE drifting between dips on the same
construction. Fix: reorder the approval sequence &mdash; construction first, colour second &mdash;
as described in Stage 1.</p>

<h3>Failure mode 5 &mdash; Fibre substitution offered as a cost saving</h3>
<p>A recycled or lower-denier fibre is proposed to hold the price. It passes all four gates because
nothing in the gates checks long-term abrasion life. Detection: abrasion and crocking results
deteriorate 3&ndash;4 months into retail. Fix: freeze L1, and add an abrasion-life requirement to the
construction brief rather than treating it as a finishing-stage property.</p>

<h2>7. Implementation Roadmap</h2>

<h3>Weeks 1&ndash;2 &mdash; Find out what you actually specified</h3>
<p>Pull the tech pack for your largest active ribbon programme and check whether EPI, PPI and denier
are stated at all. Most buyers discover they are not, and that the mill chose them. This is the
single highest-value hour in this entire module.</p>

<h3>Weeks 3&ndash;4 &mdash; Populate the authority model</h3>
<p>Fill L1&ndash;L6 into the quality agreement with named owners and explicit thresholds. Confirm
with each mill that L2/L3 co-signature is accepted in writing. Where a mill resists co-signature at
L2/L3, treat that as qualifying information about the relationship, not a negotiation point.</p>

<h3>Weeks 5&ndash;10 &mdash; Run the 4-stage gate on the next new development</h3>
<p>Apply the construction-first approval sequence to your next new ribbon. Measure theoretical versus
actual weight at Stage 2. Run the convertibility trial at Stage 3. Expect at least one material you
currently buy to come back with a different construction than assumed.</p>

<h3>Months 3&ndash;6 &mdash; Trend CVI across all lots</h3>
<p>Track the construction variance index per lot per mill. Three amber readings in a row on one mill
is a supplier-development conversation, not a per-lot non-conformance. Publish the trend to
finance: cost variance caused by construction drift is invisible to them until someone connects the
CVI chart to the spend curve.</p>

<h3>Month 9&ndash;12 &mdash; Re-verify at programme renewal</h3>
<p>Reconcile actual delivered construction against the frozen spec across the whole programme year.
Where a consistent gap exists, decide deliberately: accept it and re-freeze at the actual numbers,
or require correction and plan the transition. What you should not do is let a fourth year pass
without deciding.</p>

<h2>8. Conclusion</h2>

<p>Woven construction is the part of a ribbon that looks like a number on a mill document and behaves
like a product decision. Ends per inch, picks per inch and fibre denier together set the weight, the
hand-feel, the abrasion life, the conversion behaviour and the price. Every one of those outcomes is
a specification you care about.</p>

<p>The architecture is deliberately unglamorous: six layers with named owners, four approval gates
with construction ahead of colour, three tiers of reconciliation when the numbers disagree, and two
indicators tracked per lot. It costs almost nothing and it converts the most important parameter in
your ribbon programme from something the mill decided into something you control.</p>

<p>When you next qualify a ribbon supplier, ask the question that settles it: <em>Show me the EPI, PPI
and denier for my programme, and tell me who signs off if they change.</em> A mill that answers
with construction numbers and an authority model is a mill that can hold a specification for three
years. A mill that answers with price is telling you exactly what will happen in month four.</p>
"""

write_article(a, BODY,
              "Freeze the construction before you freeze the colour",
              "Request the woven-structure spec template and a construction approval walkthrough")
print(f"slug={SLUG}")