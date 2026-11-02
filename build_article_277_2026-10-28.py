#!/usr/bin/env python3
"""Build smithribbon B2B article 277 (PM) 2026-10-28: ribbon converting & finishing.

Topic: ribbon converting and finishing - slitting, cross-cutting, die-cutting,
folding, edge binding/taping, tipping and piece output. The mill-side module
that sits between a finished ribbon roll and a finished trim component.

Gap check against modules 250-276 (weave, pick density, weft sett, warp sett,
shrinkage, roll build, fringing, velvet pile, organza sheer, twill, metallic,
corded, elastic, lace, fusible, label, print route, colourfastness, lab dip,
DPP, AI QC, claim substantiation, contract change order, vendor scorecard):
none of them cover the converting operation. Module 264 covers selvedge/cut
edge quality on the WOVED ribbon and module 266 covers fringing/end-thread
finish; neither covers the downstream cutting, folding, binding and piece-
output stage that converts a ribbon roll into a trim component.
"""
import sys
sys.path.insert(0, "/workspace/smithribbon-web")
from smithribbon_article_lib import write_article, ROOT  # noqa

A277 = {
    "fname": ("blog-ribbon-oem-277-module-mill-side-brand-buyer-ribbon-converting-finishing-"
              "slitting-cross-cutting-die-cutting-folding-edge-binding-tipping-piece-output-"
              "interlock-architecture-2026-10-28-pm.html"),
    "slug": ("blog-ribbon-oem-277-module-mill-side-brand-buyer-ribbon-converting-finishing-"
             "slitting-cross-cutting-die-cutting-folding-edge-binding-tipping-piece-output-"
             "interlock-architecture-2026-10-28-pm"),
    "title": ("Mill-Side Brand-Buyer Ribbon Converting &amp; Finishing Interlock Architecture &mdash; "
              "Slitting, Cross-Cutting, Die-Cutting, Folding, Edge Binding, Tipping and Piece Output 2026"),
    "desc": ("B2B ribbon OEM 277-module ribbon converting and finishing. 6-stage conversion ladder, "
             "5-route slitting and width decision tree, 6-defect edge and fold atlas, and a piece-output "
             "and yield reconciliation audit. Smith Ribbon OEM since 2004."),
    "keywords": [
        "ribbon converting OEM", "ribbon slitting service", "cross cutting ribbon supplier",
        "die cut ribbon manufacturer", "ribbon edge binding", "ribbon folding service",
        "ribbon tipping cut ends", "ribbon cut to length", "ribbon piece parts supplier",
        "ribbon finishing service China", "ribbon OEM secondary processing",
        "brand buyer ribbon converting guide", "ribbon slitting width tolerance",
        "ribbon die cut shape tolerance", "ribbon edge tape folding", "ribbon yield reconciliation",
        "ribbon cut piece packaging", "ribbon conversion interlock", "Smith Ribbon converting",
    ],
    "pub_iso": "2026-10-28T15:00:00+00:00",
    "wordcount": 2800,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Converting &amp; Finishing Interlock",
    "lede": ("A mill that weaves ribbon and a mill that converts ribbon are two different suppliers, and a "
             "brand buyer who treats them as one supplier discovers the gap at the point where the ribbon "
             "becomes a component. Weaving produces a roll: continuous, wide, wound, and not yet in the shape "
             "any downstream process needs. Converting is what makes it into a component - slit to width, cut "
             "to length, folded, bound, tipped, and packed in the exact format an assembly line can consume. "
             "Every one of those six operations introduces tolerances, and every one of them can introduce "
             "defects that the incoming roll inspection would never have caught."),
    "body": """
<h2>The gap between a roll and a component</h2>
<p>Every ribbon programme eventually runs into the same wall: the ribbon arrives as a roll, and the assembly
line needs a component. Those are not the same thing, and the distance between them is a manufacturing process
that has to be specified, quoted, measured and controlled in its own right.</p>

<p>A woven ribbon roll has no width tolerance that matters (it is the loom width), no length definition beyond
the roll, and no cut ends. It has a selvedge or it has a cut edge, but that edge was made by the loom, not by
the finisher. It has no fold, no binding, no tip, no piece count, and no pack format that a picker can work
from. A brand buyer who specifies only "38mm printed grosgrain" has specified about half of what the assembly
line will consume.</p>

<div class="kpi">
  <p><strong>Why converting deserves its own module:</strong> at the mill, the conversion operation is where
  the material cost is committed and the yield is lost. A slitting setup that is one millimetre too wide
  produces a ribbon outside the spec that can only be sold as seconds. A cross-cut length that is off by two
  millimetres produces a bow whose tails are asymmetric. A fold that is not square produces a bow that sits
  crooked on the box. None of these are visible on the roll, and all of them are visible on the shelf. This is
  why converting must be specified as an interlock rather than treated as a hidden mill step.</p>
</div>

<h2>The 6-stage conversion ladder</h2>
<p>Conversion is a sequence, and each stage constrains the next. Specifying the stages out of order is the most
common cause of a conversion quote that cannot be honoured.</p>

<table>
  <tr><th>Stage</th><th>What it is</th><th>What it constrains</th></tr>
  <tr><td>1. Roll intake</td>
      <td>Verification of the incoming roll: construction, width, colour, print registration, lot, condition</td>
      <td>Everything downstream - a defect found here is free, the same defect found at piece output is a write-off</td></tr>
  <tr><td>2. Slitting</td>
      <td>Longitudinal splitting of the wide loom width into one or more finished widths</td>
      <td>Width tolerance, edge type, and whether the selvedge is preserved or the edge is a knife cut</td></tr>
  <tr><td>3. Cross-cutting</td>
      <td>Cutting the slit ribbon into discrete lengths</td>
      <td>Length tolerance, end finish, and the piece count that will be packed</td></tr>
  <tr><td>4. Shaping</td>
      <td>Die-cutting, notching, hole-punching, corner-rounding, or slotting</td>
      <td>Shape tolerance, edge burr, and whether the shaped feature is a functional datum or decorative</td></tr>
  <tr><td>5. Assembly prep</td>
      <td>Folding, edge binding, edge taping, tipping, backing and lining</td>
      <td>Fold squareness, bond security, end security, and the hand-feel of the finished trim</td></tr>
  <tr><td>6. Piece output and packing</td>
      <td>Counting, collating, and packing into the format the assembly line consumes</td>
      <td>Count accuracy, pack format, and the traceability that ties the pack back to the roll lot</td></tr>
</table>

<p>The practical consequence of the ladder is that <strong>stage 1 is the cheapest place to find a problem</strong>.
A colour-lot error found at roll intake costs a roll. The same error found at stage 6 costs every piece on that
roll, plus the picker's time, plus the schedule. This is why a converter who has a disciplined intake inspection
is worth more than one who quotes a lower rate.</p>

<h2>The 5-route slitting and width decision tree</h2>
<p>Slitting is where most of the yield loss happens, and the route is determined by which of five conditions the
programme requires.</p>

<h3>Route 1 - Selvedge preserved (loom-width direct)</h3>
<p>Where the finished width matches the loom width, or matches one of the mill's standard widths, the ribbon is
slit only to trim the edge, and the woven selvedge survives into the finished component. This is the premium
route: the selvedge is denser, stronger, does not fray, and gives the ribbon a finished, stable edge that will
survive folding and binding. It is also the route with the best appearance on a visible trim edge, and it is
what should be specified for any ribbon whose edge will be seen in the finished product.</p>

<h3>Route 2 - Knife-cut edge (fabricated selvedge)</h3>
<p>Where the required width is narrower than any available selvedge, the ribbon must be cut through the weave.
The knife-cut edge is clean but it is not reinforced, it will fray under abrasion, and it has a slightly harder
feel than a selvedge. This is acceptable where the edge is bound, covered, or hidden in a fold. It is not
acceptable where the cut edge will be the visible edge of the finished trim. If a programme needs a knife-cut
edge visible to the customer, that is a specification problem to solve in the design stage, not a production
problem to solve on the floor.</p>

<h3>Route 3 - Multi-width slitting from a single loom width</h3>
<p>Where one loom width can yield several finished widths, the yield per metre of loom output improves
substantially. This is economically attractive and technically demanding: the slitter must hold registration
across the full width, the selvedge material at each slit line must be accounted for, and the yarn count or
pick density of each slit ribbon is determined by its position in the loom width. Slit ribbons from different
positions in the same loom width are not identical, and a brand that has received "the same" ribbon from two
positions has received two different ribbons.</p>

<h3>Route 4 - Warp-direction conversion</h3>
<p>Where the trim must be cut on the warp direction rather than the weft - which happens where the ribbon is
used in a tensioned or structural application, or where a specific hand or stretch behaviour is required - the
piece geometry changes entirely and the yield calculation inverts. This is a routing decision made at the design
stage, not at the mill stage, and it is one of the most common late discoveries in a ribbon programme.</p>

<h3>Route 5 - Pre-slit supplied strip</h3>
<p>Where the programme consumes narrow pre-slit strips, the conversion can be pushed upstream so that the mill
delivers strips and the converter only cross-cuts and finishes. This shifts value and risk between two
suppliers, and it is worth structuring deliberately rather than by accident, because the tolerance responsibility
at each interface has to be unambiguous.</p>

<div class="kpi">
  <p><strong>Decision rule:</strong> Route 1 wherever the edge is visible and the ribbon is folded or bound;
  Route 3 wherever the width programme allows it and the position-in-width variation has been accepted and
  specified; Route 2 only where the edge is hidden, bound or covered; Route 4 wherever the design stage has
  already been checked for it. Never let Route 2 happen by accident on a visible edge.</p>
</div>

<h2>The 6-defect edge and fold atlas</h2>
<p>These are the six defects that account for the large majority of conversion rejects, and each one is
traceable to a specific stage. A converter that can name the stage for each defect is one that has already
solved the problem before it reached the customer's line.</p>

<table>
  <tr><th>Defect</th><th>Stage</th><th>Cause</th><th>Control</th></tr>
  <tr><td>Width drift across the roll</td>
      <td>2 - Slitting</td>
      <td>Slitter blade wear or tension variance across the roll length</td>
      <td>Blade change schedule on a piece-count trigger, not a time trigger</td></tr>
  <tr><td>Frayed or fuzzy slit edge</td>
      <td>2 - Slitting</td>
      <td>Dull blade, high blade speed relative to feed rate, or loose warp end</td>
      <td>Blade sharpness spec and feed/speed ratio window; edge inspection at roll start and end</td></tr>
  <tr><td>Length off-tolerance</td>
      <td>3 - Cross-cutting</td>
      <td>Feed slip, blade deflection under load, or thermal drift on a long run</td>
      <td>Calibrated feed with a hard stop; verified length every fixed piece count</td></tr>
  <tr><td>Burr or torn shape edge</td>
      <td>4 - Shaping</td>
      <td>Die clearance too tight, or a worn die</td>
      <td>Specified die clearance, die life tracked in cycles, burr check on a defined sample rate</td></tr>
  <tr><td>Rogue or lifted binding tape</td>
      <td>5 - Assembly prep</td>
      <td>Adhesive transfer on a dusty or low-temperature web, or insufficient dwell</td>
      <td>Surface clean-down, specified temperature and pressure, peel test on a sample rate</td></tr>
  <tr><td>Loose thread or untipped cut end</td>
      <td>5 - Assembly prep</td>
      <td>Tipping omitted on the specification, or tipping applied to a frayed rather than a trimmed end</td>
      <td>End trim before tipping; tipping specified by cut-end type, not generically</td></tr>
</table>

<h2>The piece-output and yield reconciliation audit</h2>
<p>The single most useful control a brand buyer can ask for is a yield reconciliation that runs from the
incoming roll to the packed piece count. It is a simple document and it is almost never requested, and it
is the fastest way to see whether the quoted unit price is honest.</p>

<p>The reconciliation reads as a chain, and every step should account for the previous one:</p>

<ol>
  <li><strong>Input metres</strong> - the total ribbon length received at intake, measured on the roll, not
  taken from the purchase order.</li>
  <li><strong>Loss to slitting</strong> - the trim and the selvedge removed to reach the finished width, plus
  the set-up length on each roll.</li>
  <li><strong>Usable metres</strong> - input less slitting loss, before any other conversion loss.</li>
  <li><strong>Loss to conversion</strong> - the length consumed by set-up, testing, start-up reject and end-of-
  roll reject.</li>
  <li><strong>Net metres</strong> - the length actually available for production.</li>
  <li><strong>Pieces produced</strong> - the count that reaches stage 6.</li>
  <li><strong>Pieces packed</strong> - the count that actually leaves the building, and the difference between
  it and the previous line is the reject and rework rate.</li>
</ol>

<p>Read the ratio between lines 5 and 7 and you have the conversion yield. A healthy converting operation on a
stable construction typically lands somewhere in the mid-to-high 80s into the 90s in percentage terms. A yield
that looks poor usually indicates one of three things: the slitting loss is higher than the programme needs
(which is a width-routing decision), the set-up losses are high (which is a lot-size decision), or the reject
rate is high (which is a process-control issue). Each of those has a different owner and a different fix, and
a reconciliation lets you tell them apart.</p>

<p>Two further reconciliations matter. The first is <strong>colour reconciliation</strong>: the number of
finished pieces by colour against the number ordered by colour, which catches both over-production and
under-production against a call-off schedule. The second is <strong>lot traceability reconciliation</strong>:
which upstream roll lot, dye lot and print lot each pack of finished pieces came from. This is the document that
lets a brand answer a retailer's traceability question about a specific finished trim, rather than a general
statement about the mill.</p>

<h2>What to specify, and what to ask a converter</h2>
<p>When a brand buyer specifies converted ribbon trim, the specification needs to describe the component and not
merely the material. At minimum it should carry: the substrate and construction; the finished width and the
width tolerance; whether the edge is selvedge or knife-cut; the finished length and the length tolerance; the
quantity and whether it is a call-off schedule or a fixed lot; the end finish, which may be heat-sealed, bound,
tipped, folded or left raw; the fold, where there is one, including the fold style, the fold position and the
fold squareness tolerance; the shape, where there is one, as a dimensioned drawing rather than a photograph; the
bond and adhesive specification for any binding or backing; the pack format, which should be the format the
assembly line actually consumes rather than the format the converter finds convenient; and the piece count per
pack and the pack label content.</p>

<p>And the questions worth asking, which are the ones that distinguish a converter from a cutter:</p>

<ul>
  <li>What is the measured conversion yield on a comparable programme, and can we see the reconciliation?</li>
  <li>What is your blade-change interval, and is it triggered by piece count or by time?</li>
  <li>How do you guarantee the edge type on a knife-cut ribbon, and how do you verify selvedge integrity?</li>
  <li>What is your die clearance specification, and how do you track die life?</li>
  <li>What is your die life tracking method, and what is your reject rate by defect category over the last
  three months?</li>
  <li>Can you pack to our assembly sequence, so the picker takes one piece at a time without tangling?</li>
  <li>How is a finished piece linked back to its input roll, dye lot and print lot?</li>
  <li>What is your tolerance for a mixed-lot pack, and how is mixed-lot packing controlled?</li>
</ul>

<p>At Smith Ribbon, in Xiamen since 2004, we run the full conversion ladder in-house on our own 15,000 square
metre site, with approximately 200 staff and a daily ribbon capacity in the region of 100,000 metres. That
means the slitting, cross-cutting, die-cutting, folding, binding and tipping happen under the same roof and the
same quality system as the weaving, which removes the tolerance gap that appears when weaving and converting sit
with two different suppliers. We hold OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA, we ship to over 50
countries, and we can supply the lot-level traceability, the incoming and outgoing inspection records and the
yield reconciliation for any programme we run.</p>

<p>The practical advice is to bring the converter into the specification conversation before the first sample, not
after the first production lot. The width routing decision, the fold design, the pack format and the piece
count are all design-stage decisions that a converter can influence, and a programme that fixes them before
the sample is far cheaper than one that discovers them in the second production run.</p>
""",
    "faq": [
        ("What does ribbon converting actually include?",
         "Ribbon converting is everything that happens to a finished ribbon roll before it becomes a component "
         "an assembly line can consume. It covers slitting the loom width down to the finished width, "
         "cross-cutting to length, die-cutting and shaping, folding, edge binding and taping, tipping the cut "
         "ends, and finally counting, collating and packing. Each stage carries its own tolerances and its own "
         "defect modes."),
        ("Why does it matter whether the ribbon edge is selvedge or knife-cut?",
         "A woven selvedge is denser and stronger, does not fray, and gives a finished appearance. A knife-cut "
         "edge is clean but unreinforced and will fray under abrasion. Where the edge will be visible in the "
         "finished trim, or where it will be folded or bound, the selvedge route should be specified. Knife-cut "
         "is acceptable only where the edge is bound, covered or hidden in a fold."),
        ("What is a reasonable conversion yield to expect?",
         "On a stable construction with a well-matched lot size, a healthy converting operation typically reaches "
         "a yield in the mid-to-high 80s into the 90s in percentage terms, measured from net input metres to "
         "pieces packed. A lower figure usually points at one of three causes: slitting loss higher than the "
         "width programme requires, high set-up losses from small lot sizes, or a high reject rate in a specific "
         "defect category. A yield reconciliation from input roll to packed count identifies which one it is."),
        ("Why should the pack format match our assembly line rather than the converter's preference?",
         "Because the pack format is a productivity and accuracy decision, not just a logistics one. A pack that "
         "forces a picker to untangle, sort or re-orient ribbon to find the right piece adds handling time at "
         "every box and introduces the risk of the wrong colour or the wrong length going into a pack. "
         "Specifying the assembly-line consumption format in the spec removes that risk at source rather than "
         "auditing it afterwards."),
        ("What tolerance should we specify on converted ribbon trim?",
         "Specify the finished width, the length, and the fold squareness separately, because each is controlled "
         "at a different stage. Width tolerance is set at slitting, length tolerance at cross-cutting, and fold "
         "squareness at the assembly-prep stage. For a visible trim on a premium product, a tight width tolerance "
         "and a defined fold squareness matter more than the length tolerance, since the length is usually "
         "hidden in the fold or the knot."),
        ("Can converting be outsourced to a separate supplier from the mill?",
         "It can, but the tolerance responsibility at the interface then has to be written down explicitly. When "
         "weaving and converting sit with two different suppliers, an edge defect or a registration error can sit "
         "between them, and neither has full ownership of the finished component. Many programmes run converting "
         "in-house at the mill for exactly this reason, since it removes the tolerance gap and keeps lot "
         "traceability on one record."),
    ],
    "cta_title": "Send us your trim drawing and lot size",
    "cta_body": ("We will come back with a conversion route recommendation, an indicative yield for your "
                 "width and piece format, and an indicative price per piece. Physical swatches and conversion "
                 "samples can be couriered to Europe and North America."),
    "cta_link_text": "Request a ribbon converting quote",
}

write_article(**{k: v for k, v in A277.items() if k not in ("fname", "slug", "body")},
              fname=A277["fname"], slug=A277["slug"], body_html=A277["body"])
print(f"Wrote {A277['fname']}")
