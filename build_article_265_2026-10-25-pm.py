#!/usr/bin/env python3
"""Build smithribbon B2B module 265 (PM), 2026-10-25.

Topic: mill-side ROLL-BUILD & PACKING-FORMAT interlock — how a brand buyer
controls the roll length, core specification, winding direction, roll-weight
tolerance and carton configuration of finished ribbon.

Distinct from every existing module: 259 warp-sett, 260 pick density, 261
weft-sett/width, 262 elastic recovery, 263 colourfastness, 264 selvedge/cut
edge, 257 slit width, 258 shrinkage, 256 print route. This module covers the
DELIVERY UNIT — the roll, the core, the carton and the configuration in which
the ribbon reaches the customer's warehouse.
"""
from pathlib import Path
import sys

sys.path.insert(0, "/workspace/smithribbon-web")
from sr_page import write_article

SLUG = ("blog-ribbon-oem-265-module-mill-side-brand-buyer-roll-build-packing-format-interlock-architecture-"
        "roll-length-core-winding-direction-weight-tolerance-carton-configuration-global-brand-procurement-2026-10-25-pm")

a = {
    "title": "Mill-Side Brand-Buyer Roll-Build &amp; Packing-Format Interlock Architecture &mdash; "
             "Controlling Roll Length, Core Specification, Winding Direction and Carton Configuration 2026",
    "desc": "B2B ribbon OEM 265-module roll-build and packing-format interlock architecture. "
            "5-layer delivery-unit authority ladder, 4-stage roll approval gate, 3-tier roll-defect reconciliation "
            "ladder, and a winding-tension early-warning threshold. Smith Ribbon OEM since 2004.",
    "kw": "ribbon roll specification, ribbon core size, ribbon winding direction, roll length tolerance, "
          "ribbon carton configuration, ribbon packing format, ribbon roll weight, ribbon packaging OEM, "
          "custom ribbon rolls, ribbon spool core, ribbon winding tension, ribbon delivery format, "
          "private label ribbon packaging, ribbon OEM packing standard, ribbon carton quantity, "
          "ribbon roll build interlock, ribbon bulk packing",
    "author": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
    "date_iso": "2026-10-25T07:00:00+00:00",
    "date_human": "October 25, 2026",
    "slug": SLUG,
    "section": "Ribbon OEM Manufacturing",
    "tag": "Ribbon OEM",
    "read": "16 min read",
    "word_count": 2600,
}

BODY = """
<p class="lede">Ribbon is specified in metres per colour, width and construction, and delivered in cartons of rolls.
Between those two numbers sits an entire specification that most purchase orders leave blank: what the roll
actually is. How long it is. What core it is wound on. Which way the winding runs. How much it is allowed to vary
in weight. How many rolls are in a carton and how the carton is configured. This module is about the delivery unit
&mdash; the last physical object the mill handles before the ribbon becomes somebody else&rsquo;s problem.</p>

<h2>1. Why the Roll Is a Specification, Not a Container</h2>

<p>A roll of ribbon is usually understood by buyers as a neutral carrier: a convenient way to move a length of
material. In practice, the roll is a specification that carries engineering consequences all the way into the
customer&rsquo;s own production line, and it is where a surprising number of avoidable disruptions originate.</p>

<p>Consider a customer who reels ribbon from a roll on a converting machine. The machine has a fixed core
diameter, a fixed unwind direction, and a fixed tension profile. If the mill ships rolls on a 25&nbsp;mm core
where the machine expects 76&nbsp;mm, the customer cannot run the ribbon at all. If the winding direction is
reversed, the ribbon unwinds backwards and the machine operator has to re-thread every time a new roll is
mounted. If the roll length does not divide evenly into the customer&rsquo;s cutting plan, the tail ends of the
programme become unusable scrap at a rate nobody costed.</p>

<blockquote style="border-left:4px solid #b8854a;padding:8px 16px;margin:1.2em 0;background:#faf6f1;">
&quot;38&nbsp;mm printed satin ribbon. 100&nbsp;m rolls, 76&nbsp;mm core, clockwise winding as viewed from the
 free end. Roll weight tolerance &plusmn;3&nbsp;% of nominal. 20 rolls per carton, 4 cartons per export
 case, 800&nbsp;m nominal per case. No splicing within a roll. Label each roll with colour code, width,
 lot number and production date.&quot;
</blockquote>

<p>That single paragraph contains at least eleven separate requirements, and each of them can fail independently.
None of them is difficult. All of them are expensive when they fail, because they fail at the customer&rsquo;s
end of the line rather than at the mill&rsquo;s.</p>

<div class="kpi">
  <p><strong>Commercial significance:</strong> delivery-format defects are the cheapest defects to prevent and the
  most expensive to discover late, because they are discovered by the customer&rsquo;s staff on a machine they have
  already committed production time to. A reversed winding direction that stops a converting line for an afternoon
  costs far more than the roll that caused it, and the mill rarely hears about it in a form that improves the next
  shipment.</p>
</div>

<h2>2. The 5-Layer Delivery-Unit Authority Model</h2>

<p>Five layers govern the delivery unit, each with a named owner and a change threshold. They are ordered from the
most frozen to the most operational, because that is how much freedom each layer genuinely has.</p>

<table>
  <thead>
    <tr><th>Layer</th><th>Parameter</th><th>Owner</th><th>Change threshold</th></tr>
  </thead>
  <tbody>
    <tr><td>R1</td><td>Core specification (inner and outer diameter, material, whether the core is supplied by the
        mill or by the customer)</td>
        <td>Brand, frozen at FAI</td><td>None. A core change is a new delivery format and a re-qualification.</td></tr>
    <tr><td>R2</td><td>Winding direction and winding tension profile (clockwise or counter-clockwise, as viewed
        from the free end; tension ramp profile across the build)</td>
        <td>Brand, frozen at FAI</td><td>None without a customer-line confirmation</td></tr>
    <tr><td>R3</td><td>Roll length tolerance and roll-weight tolerance against nominal</td>
        <td>Mill, brand co-sign</td><td>Length outside &plusmn;1&nbsp;% or weight outside &plusmn;3&nbsp;% of nominal</td></tr>
    <tr><td>R4</td><td>Carton configuration: rolls per carton, carton count per export case, case dimensions,
        gross and net weight, carton marking</td>
        <td>Mill, brand co-sign</td><td>Any change to the case count or marking content</td></tr>
    <tr><td>R5</td><td>Winder setup, tension ramp calibration, roll-build programming, compression and end-of-roll
        handling, splices policy</td>
        <td>Mill, internal only</td><td>Mill informs brand on change of winder, program or splice policy</td></tr>
  </tbody>
</table>

<p><strong>R1</strong> looks trivial and causes disproportionate friction. Core diameter is frequently decided by
the mill&rsquo;s convenience rather than the customer&rsquo;s machine, and it is often the last thing checked. The
question to ask is simple: <em>what core does the customer&rsquo;s converting equipment actually take, and is the
core a consumable the customer wants to control?</em> Some programmes require the mill to use customer-supplied
cores; others want a specific recycled-cardboard specification for their own sustainability reporting.</p>

<p><strong>R2</strong> is where the highest-cost defects live. Winding direction is a two-state parameter that is
almost never written down, because everybody assumes it is obvious. It is not: a ribbon wound clockwise and viewed
from the free end unwinds clockwise off the roll, and a reversing machine or an operator expecting the opposite will
produce a jam, a twist, or a pile-up. The specification should state the direction and the viewpoint explicitly,
because &ldquo;clockwise&rdquo; means nothing without a reference point.</p>

<p><strong>R5</strong> is the layer that produces the visible result. A wound roll that is over-compressed at the
core and under-tensioned at the outside will look fine on the shelf and behave badly on the line &mdash; a
&ldquo;soft spot&rdquo; that unwinds unevenly and causes tension ripple in the customer&rsquo;s converting process.
The tension ramp profile, not the final tension value, is usually the culprit.</p>

<h2>3. The 4-Stage Roll Approval Gate</h2>

<h3>Stage 1 &mdash; Format definition (before production)</h3>
<p>Confirm the full delivery format in writing before the order enters production: core, direction, roll length,
tolerance bands, rolls per carton, case configuration and marking content. This should appear on the purchase
order, not only in the quality agreement, because the purchase order is what travels with the goods and what the
warehouse works from.</p>

<h3>Stage 2 &mdash; First-roll verification (start of lot)</h3>
<p>Wind the first roll and verify it before the rest of the lot is produced. Confirm core fit, winding direction by
observation, roll length, weight against nominal, and that the roll unwinds without a hard spot or a collapse. A
defect found at the first roll costs one roll. The same defect found at the customer costs an entire lot.</p>

<h3>Stage 3 &mdash; In-line roll audit (sampled through the lot)</h3>
<p>Sample rolls at defined intervals through the run and check length, weight, core integrity, edge condition and
unwinding behaviour. This is where the tension-ramp drift and the winder-programme drift surface, because they
develop progressively rather than appearing at the start.</p>

<h3>Stage 4 &mdash; Case-level verification (before shipment)</h3>
<p>Verify the packed case, not just the roll: roll count per case, case dimensions, gross and net weight, marking
legibility and correctness, and carton integrity for export. A carton count that is short by one roll is a
reconciliation problem at the customer&rsquo;s receiving dock; it is caught in four seconds at the mill.</p>

<div class="kpi">
  <p><strong>The Smith Ribbon roll approval rule:</strong> the delivery format is verified at roll level and then
  again at case level, because most delivery-format errors survive the roll check and only surface in the case.
  A case is not a packaging decision; it is a counted, weighed and marked delivery unit with its own specification.</p>
</div>

<h2>4. The Six Parameters That Define a Ribbon Roll</h2>

<table>
  <thead>
    <tr><th>Parameter</th><th>Typical specification</th><th>What it controls</th><th>Failure signature downstream</th></tr>
  </thead>
  <tbody>
    <tr><td>Core inner diameter</td>
        <td>25&nbsp;mm, 38&nbsp;mm, 76&nbsp;mm, or customer-supplied</td>
        <td>Whether the roll mounts on the customer&rsquo;s unwind spindle</td>
        <td>Roll will not mount; or mounts loose and unwinds with run-out</td></tr>
    <tr><td>Winding direction</td>
        <td>Clockwise or counter-clockwise, as viewed from the free end</td>
        <td>Whether the ribbon unwinds in the direction the machine expects</td>
        <td>Backwards unwinding; twist accumulation; line stoppage on roll change</td></tr>
    <tr><td>Roll length</td>
        <td>50&nbsp;m, 100&nbsp;m, 200&nbsp;m, or 1,000&nbsp;m master rolls, &plusmn;1&nbsp;%</td>
        <td>Whether the roll divides evenly into the customer&rsquo;s cutting plan</td>
        <td>Excess tail scrap; programme-length mismatches; mid-programme roll changes</td></tr>
    <tr><td>Roll weight</td>
        <td>Nominal &plusmn;3&nbsp;%, declared on the label</td>
        <td>Whether the declared quantity is honest and the invoice is correct</td>
        <td>Receiving discrepancies; freight recalculation; disputes at month-end</td></tr>
    <tr><td>Winding tension profile</td>
        <td>Constant to a ramped profile across the build, controlled at the winder</td>
        <td>Whether the roll unwinds evenly under the customer&rsquo;s line tension</td>
        <td>Soft spots; tension ripple; web break at the converting machine</td></tr>
    <tr><td>Splice policy</td>
        <td>No splices within a roll; splices recorded at the roll card if unavoidable</td>
        <td>Whether an interruption point is hidden or passed to the customer</td>
        <td>Line stoppage at an unannounced splice; a join defect discovered in the finished assembly</td></tr>
  </tbody>
</table>

<p>Length and weight are the two the buyer thinks about. Direction and tension profile are the two that cause the
most operational disruption, and both are free to specify. The rule is simple: if it can be observed on the roll,
it belongs on the purchase order.</p>

<h2>5. The 3-Tier Roll-Defect Reconciliation Ladder</h2>

<ol>
  <li><strong>Tier 1 &mdash; Isolate the level.</strong> Is the defect in the roll, the carton, or the case? A
  roll-level defect (length, weight, tension, splice) points to the winder and to R5. A carton-level defect (roll
  count, positioning, crush damage) points to packing and to R4. A case-level defect (case count, marking, gross
  weight) points to case configuration and to R4. Fixing a roll-level defect by adjusting the case packing is
  common and always wrong.</li>
  <li><strong>Tier 2 &mdash; Isolate the mechanism.</strong> Establish whether the mechanism is
  <em>programme-driven</em> (the winder recipe, tension ramp or length counter was mis-set or drifted) or
  <em>material-driven</em> (a lot with different yarn behaviour, a roll build affected by a change in ribbon
  thickness or width across the lot). Programme-driven faults are corrected in the setup. Material-driven faults
  require the supplier&rsquo;s incoming-material assessment, not a winder adjustment.</li>
  <li><strong>Tier 3 &mdash; Isolate the extent.</strong> Determine how many rolls are affected and whether the
  defect is concentrated at the start of the lot, the end, or spread through it. Concentrated at the start points to
  a setup error. Concentrated at the end points to progressive drift or a winder programme change mid-run. Spread
  through the lot points to a material or measurement-system cause.</li>
</ol>

<div class="kpi">
  <p><strong>The Smith Ribbon closure rule:</strong> a roll-format incident is closed only when a re-wound sample
  from the corrected process is presented, re-measured on all six parameters, and accompanied by a corrective action
  recorded against the specific level and mechanism identified in Tiers 1 and 2. &ldquo;We will be more careful
  next time&rdquo; is not a corrective action.</p>
</div>

<h2>6. The Winding-Tension Early-Warning Threshold</h2>

<p>Most delivery-format problems are invisible until the customer tries to run them. The leading indicator is the
<strong>roll-weight coefficient of variation across a lot</strong> &mdash; the spread of actual roll weights around
the nominal, expressed as a percentage.</p>

<p>The Smith Ribbon threshold: if the coefficient of variation across consecutive rolls rises above 1.5&nbsp;% within
a lot, the winder tension ramp is treated as unstable and is corrected at Tier 1, even though every individual roll
is still inside the &plusmn;3&nbsp;% weight tolerance band. The reason is that weight variance is the earliest
observable proxy for tension-profile instability, and tension-profile instability is what produces the soft spots
and the uneven unwinding that cause web breaks on the customer&rsquo;s line.</p>

<p>A second early indicator is the incidence of re-winds. A rising rewind rate on a programme that has been stable for
months signals that something upstream is drifting &mdash; often a change in ribbon thickness or yarn behaviour
between lots, which alters how the material responds to the same winder settings.</p>

<h2>7. Case and Carton Design for the Receiving Operation</h2>

<p>The carton and the export case are the last place where a delivery format can still be improved, and they are
usually designed around the mill&rsquo;s warehouse rather than the customer&rsquo;s receiving dock. Three design
questions consistently separate a well-built case from an awkward one.</p>

<p><strong>Does the case open from the top, or from the side?</strong> A customer&rsquo;s warehouse team usually
wants top-opening cases that can be emptied onto a picking shelf without turning the case over. A side-opening case
requires either tipping or a second person, and it is a common source of the &ldquo;they damaged the roll&rdquo;
claim that neither side can explain.</p>

<p><strong>Does the roll count match a sensible picking quantity?</strong> A case of 800&nbsp;m that must be broken
into 40&nbsp;roll cartons for a customer who picks 4 rolls at a time is a case designed for transport, not for
picking. Where volume allows, the mill can offer an intermediate carton that matches the customer&rsquo;s picking
pattern without changing the case.</p>

<p><strong>Is the marking legible and complete at receiving conditions?</strong> Marking should carry the customer
order number, colour code, width, lot number, production date and roll count, in a position and size that survives
a warehouse label printer and a warehouse light. A case that has to be turned over to read is a case that gets
logged wrong.</p>

<h2>8. Implementation Path</h3>

<h3>Stage A &mdash; Write the delivery format onto the purchase order</h3>
<p>Move core, winding direction, length tolerance, weight tolerance, rolls per carton, case count and marking
content from the quality agreement onto the purchase order, where they travel with the goods and reach the
warehouse.</p>

<h3>Stage B &mdash; Add a first-roll gate to the production routine</h3>
<p>Verify the first roll of every lot against all six parameters before the lot continues. One roll of cost against
an entire lot of rework risk.</p>

<h3>Stage C &mdash; Track roll-weight variance per lot</h3>
<p>Record the coefficient of variation per lot, not just the pass/fail against tolerance. Trend it. The variance
leads the complaints.</p>

<h3>Stage D &mdash; Review the receiving experience annually</h3>
<p>Ask the customer&rsquo;s warehouse team two questions once a year: which part of the case was awkward to open,
and which part of the marking was hard to read. The answers usually convert directly into a packaging change with
no material cost.</p>

<h2>9. Conclusion</h2>

<p>The roll is the last thing the mill handles and the first thing the customer does. Almost every parameter that
governs it is free to specify and cheap to control, and almost none of them is normally specified at all.</p>

<p>The architecture here is operational rather than fashionable: five layers with named owners, four gates that
verify at roll level and again at case level, six parameters defined explicitly, a three-tier ladder that
separates roll faults from carton faults from case faults, and a variance threshold that catches winding problems
before they reach a converting line.</p>

<p>When you next qualify a ribbon supplier, ask: <em>Show me a roll wound on the core we specify, wound the
direction we specify, measured for length and weight, unwound on a machine, and packed in the carton we
specify.</em> A mill that can produce that on request has a delivery system. A mill that answers with a carton
photograph has a packing line &mdash; and the customer&rsquo;s line will find the difference in an afternoon.</p>

<h2>10. Frequently Asked Questions</h2>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What core sizes are available for custom ribbon rolls?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Common inner core diameters for ribbon are 25 mm, 38 mm and 76 mm, with cardboard or paper cores as standard and plastic cores available where durability or high-frequency unwinding requires it. Some programmes run customer-supplied cores so that the core specification and environmental claim remain under the customer's control. At Xiamen Smith Ribbon & Bow Co., Ltd. the core is a frozen Layer R1 parameter in the delivery-unit authority model, and changing it after programme approval requires re-qualification because it affects winding tension, roll geometry and downstream handling."
      }
    },
    {
      "@type": "Question",
      "name": "How do I specify winding direction so it is not ambiguous?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Always state the direction together with the viewpoint. The correct phrasing is clockwise as viewed from the free end of the roll, or counter-clockwise as viewed from the free end. Without the viewpoint the same roll can legitimately be described in two ways, and the customer will discover the mismatch on their converting line rather than on the delivery note. Smith Ribbon states the winding direction on the purchase order, the roll label and the quality agreement, and verifies it on the first roll of every lot."
      }
    },
    {
      "@type": "Question",
      "name": "What roll length should I order to minimise cutting waste?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The correct roll length is the one that divides most cleanly into your own cutting programme. If your programme cuts ribbon in fixed lengths, choose a roll length that is a multiple of that cut length so no residual tail is generated at the end of a run. Common configurations are 50 m, 100 m, 200 m and 1,000 m master rolls, each with a length tolerance of plus or minus one per cent. Smith Ribbon normally supplies 1,000 m master rolls for customer conversion and can supply pre-cut lengths in cartons for customers who do not run their own cutting equipment."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop rolls developing soft spots that break on my converting machine?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Soft spots are almost always a winding tension ramp problem rather than a material problem: the roll is over-compressed at the core and under-tensioned at the outside, so it unwinds unevenly under line tension. The early indicator is roll-weight variance within a lot. Smith Ribbon treats a coefficient of variation above 1.5 per cent across consecutive rolls as a winder instability signal and corrects the tension ramp at source, even when each individual roll is still within the plus or minus three per cent weight tolerance band."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum order quantity and lead time for custom ribbon with a specified delivery format?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Xiamen Smith Ribbon & Bow Co., Ltd. has manufactured ribbon and decorative trims since 2004 in a 15,000 square metre plant with 200+ employees and 100,000 meters of daily capacity. Custom ribbon starts at 1,000 meters per colour, width and construction, with 500 meters for small batches. A new delivery format requiring a specific core, winding programme and case configuration typically adds five to eight days on top of the standard 40 to 55 days to first production shipment, with OEKO-TEX, FSC, BSCI, SEDEX, SMETA and ISO 9001 certification available."
      }
    }
  ]
}
</script>

<p>Below are the questions brand buyers most frequently raise when introducing a formal delivery-format specification
into an OEM ribbon relationship. If your question is not covered here, our compliance engineers will answer it
directly.</p>

<h3>What core sizes are available for custom ribbon rolls?</h3>
<p>Common inner core diameters for ribbon are 25&nbsp;mm, 38&nbsp;mm and 76&nbsp;mm, with cardboard or paper cores
as standard and plastic cores available where durability or high-frequency unwinding requires it. Some programmes run
customer-supplied cores so that the core specification and environmental claim remain under the customer&rsquo;s
control. At Xiamen Smith Ribbon &amp; Bow Co., Ltd. the core is a frozen Layer R1 parameter in the delivery-unit
authority model, and changing it after programme approval requires re-qualification because it affects winding
tension, roll geometry and downstream handling.</p>

<h3>How do I specify winding direction so it is not ambiguous?</h3>
<p>Always state the direction together with the viewpoint. The correct phrasing is clockwise as viewed from the free end
of the roll, or counter-clockwise as viewed from the free end. Without the viewpoint the same roll can legitimately be
described in two ways, and the customer will discover the mismatch on their converting line rather than on the
delivery note. Smith Ribbon states the winding direction on the purchase order, the roll label and the quality
agreement, and verifies it on the first roll of every lot.</p>

<h3>What roll length should I order to minimise cutting waste?</h3>
<p>The correct roll length is the one that divides most cleanly into your own cutting programme. If your programme
cuts ribbon in fixed lengths, choose a roll length that is a multiple of that cut length so no residual tail is
generated at the end of a run. Common configurations are 50&nbsp;m, 100&nbsp;m, 200&nbsp;m and 1,000&nbsp;m master
rolls, each with a length tolerance of plus or minus one per cent. Smith Ribbon normally supplies 1,000&nbsp;m master
rolls for customer conversion and can supply pre-cut lengths in cartons for customers who do not run their own cutting
equipment.</p>

<h3>How do I stop rolls developing soft spots that break on my converting machine?</h3>
<p>Soft spots are almost always a winding tension ramp problem rather than a material problem: the roll is
over-compressed at the core and under-tensioned at the outside, so it unwinds unevenly under line tension. The early
indicator is roll-weight variance within a lot. Smith Ribbon treats a coefficient of variation above 1.5&nbsp;per cent
across consecutive rolls as a winder instability signal and corrects the tension ramp at source, even when each
individual roll is still within the plus or minus three per cent weight tolerance band.</p>

<h3>What is the minimum order quantity and lead time for custom ribbon with a specified delivery format?</h3>
<p>Smith Ribbon has run production since 2004 with 1,000&nbsp;m MOQ per colour, width and construction, and
500&nbsp;m for small batches. A new delivery format requiring a specific core, winding programme and case
configuration typically adds five to eight days on top of the standard 40&ndash;55 days to first production
shipment, with OEKO-TEX, FSC, BSCI, SEDEX, SMETA and ISO 9001 certification available.</p>
"""

write_article(a, BODY,
              "Specify the delivery format, not just the metres",
              "Request the roll and case specification template and a winding-tension walkthrough")
print(f"slug={SLUG}")
