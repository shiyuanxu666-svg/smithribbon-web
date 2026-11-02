#!/usr/bin/env python3
"""Build smithribbon B2B module 264 (AM), 2026-10-25.

Topic: mill-side SELVEDGE & CUT-EDGE QUALITY interlock — how a brand buyer
controls the selvage formation, edge fray resistance, edge parallelism and
cut-edge cleanliness of woven and printed ribbon.

Distinct from every existing module: 259 warp-sett/crease-reset, 260 pick
density, 261 weft-sett/width, 262 elastic recovery/edge sealing, 263
colourfastness/crocking, 256 print route, 257 slit width, 258 shrinkage.
This module covers the EDGE AS A FUNCTION — the two narrow strips of ribbon
that a customer actually touches, cuts, folds and sews, and that decide
whether a trim reads as precision or as cheap.
"""
from pathlib import Path
import sys

sys.path.insert(0, "/workspace/smithribbon-web")
from sr_page import write_article

SLUG = ("blog-ribbon-oem-264-module-mill-side-brand-buyer-selvedge-cut-edge-quality-fray-resistance-edge-parallelism-"
        "interlock-architecture-global-brand-procurement-2026-10-25-am")

a = {
    "title": "Mill-Side Brand-Buyer Selvedge &amp; Cut-Edge Quality Interlock Architecture &mdash; "
             "Controlling Fray Resistance, Edge Parallelism and Cut Cleanliness in Ribbon Programmes 2026",
    "desc": "B2B ribbon OEM 264-module selvedge and cut-edge quality interlock architecture. "
            "5-layer edge authority ladder, 4-stage edge approval gate, 3-tier edge-defect reconciliation ladder, "
            "and a fray early-warning threshold. Smith Ribbon OEM since 2004.",
    "kw": "selvedge ribbon quality, cut edge ribbon, edge fray ribbon, ribbon edge parallelism, "
          "ribbon selvage formation, woven edge construction, ribbon cutting quality, "
          "edge treatment ribbon, satin ribbon edge, grosgrain selvage, ribbon edge defect, "
          "cut edge cleanliness, private label ribbon quality, ribbon OEM edge control, "
          "ribbon edge straightness tolerance, ribbon finishing edge quality",
    "author": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
    "date_iso": "2026-10-25T02:00:00+00:00",
    "date_human": "October 25, 2026",
    "slug": SLUG,
    "section": "Ribbon OEM Manufacturing",
    "tag": "Ribbon OEM",
    "read": "16 min read",
    "word_count": 2600,
}

BODY = """
<p class="lede">A customer will forgive a ribbon that is a shade off. A customer will not forgive a ribbon whose
edge frays in the guillotine, whose selvage wanders half a millimetre from side to side, or whose cut edge comes
out of the slitter visibly bevelled. The edge is the part of a trim that the human hand touches, folds, wraps and
stitches &mdash; and it is, for most buyers, the least specified part of the whole specification. This module is
about turning the edge into a controlled, measurable, owned parameter rather than an inherited by-product of how
the loom happened to be threaded.</p>

<h2>1. Why the Edge Is the Last Parameter Nobody Writes Down</h2>

<p>Almost every ribbon specification a brand buyer issues will cover width, construction, colour, material, finish
and packing. It will rarely, if ever, cover the selvage. The result is that the edge arrives as a surprise: a
roll that is beautiful in the middle and untidy at the two narrow strips that run the full length of it.</p>

<p>This happens because the edge is not a designed feature in most mills. It is what remains after the weft turns
around at the far side of the reed. Whether that turn-around produces a dense, locked, straight edge or a soft,
open, wandering one is a function of reed design, warp tension at the edge, weft tension at the edge, pick-up
angle, and the finishing route &mdash; five variables, none of which the buyer named, all of which the customer
sees.</p>

<blockquote style="border-left:4px solid #b8854a;padding:8px 16px;margin:1.2em 0;background:#faf6f1;">
&quot;38&nbsp;mm polyester satin ribbon, 2&nbsp;cm printed repeat, cut-edge, for folded gift box closures.
 selvage to be self-locking and to pass a 20&nbsp;mm pull test at 1&nbsp;kg without visible filament
 withdrawal. Edge parallelism to remain within 0.3&nbsp;mm across the roll. Do not ship selvedge-fibre
 wefts visible at 300&nbsp;mm viewing distance.&quot;
</blockquote>

<p>Read that specification and count the parameters: fray resistance, tensile pull test, edge parallelism across the
roll, and cut-edge cleanliness at a defined viewing distance. Four measurable requirements, none of which appear
in a typical purchase order. Every one of them is a different measurement, and every one of them fails
differently.</p>

<div class="kpi">
  <p><strong>Commercial significance:</strong> edge quality failures are among the most expensive low-visibility
  defects in trim, because they are detected by the customer, not by the mill. A frayed edge is discovered on the
  cutting table of the customer&rsquo;s own conversion plant &mdash; after the ribbon has been cut, stacked and
  partly consumed. It re-enters your system as a quality incident, a credit request, or a supplier review, and the
  conversation is no longer about the ribbon. It is about why the mill shipped something it could have seen.</p>
</div>

<h2>2. The 5-Layer Edge Authority Model</h2>

<p>Edge quality is governed by five layers. Each has a named owner and a defined change threshold. When the layers
are named, edge problems stop being mysterious and start being diagnosable in minutes rather than weeks.</p>

<table>
  <thead>
    <tr><th>Layer</th><th>Parameter</th><th>Owner</th><th>Change threshold</th></tr>
  </thead>
  <tbody>
    <tr><td>E1</td><td>Selvage construction type (constructed selvage with locked-in weft turns, or natural turn-around)
        and reed profile</td>
        <td>Brand, frozen at FAI</td><td>None. A change of selvage construction is a new SKU.</td></tr>
    <tr><td>E2</td><td>Edge warp tension, edge pick-up angle and weft tension differential across the width</td>
        <td>Brand, frozen at FAI</td><td>None without a re-qualification sample</td></tr>
    <tr><td>E3</td><td>Edge parallelism tolerance (deviation of the selvage line from nominal across the roll length)</td>
        <td>Mill, brand co-sign</td><td>Beyond 0.3&nbsp;mm over any 10&nbsp;m length</td></tr>
    <tr><td>E4</td><td>Fray resistance index (filament withdrawal under a defined pull test) and cut-edge cleanliness grade</td>
        <td>Mill, brand co-sign</td><td>Fray index below 0.95 of reference, or cleanliness grade drop of one level</td></tr>
    <tr><td>E5</td><td>Slitting and winding edge treatment: slitter blade condition, edge dressing, roll build and
        compression profile</td>
        <td>Mill, internal only</td><td>Mill informs brand on change of blade, dressing or slitting route</td></tr>
  </tbody>
</table>

<p><strong>E1</strong> is where most of the value sits, and it is the layer buyers almost never specify. A constructed
selvage &mdash; in which the weft is turned back into the warp with extra picks or a dedicated edge binding
&mdash; produces an edge that resists fraying and can be cut cleanly without unravelling. A natural turn-around
edge is cheaper to weave and perfectly acceptable for many applications, but it frays, and it will not survive a
guillotine cut in a customer&rsquo;s warehouse. The decision belongs to the brand, not to the mill, and it needs to
be made before the loom is set.</p>

<p><strong>E2</strong> is the physical cause of most edge wander. A loom whose edge warps are tensioned differently
from the centre warps will produce a visibly curved or scalloped selvage. This is a tension-setting question, and it
is invisible on the fabric body. It appears only at the edge, which is exactly why it survives to the customer.</p>

<p><strong>E5</strong> is the layer that quietly destroys good edges. A slitter blade that has been running past its
life produces a bevelled, compressed, slightly burred edge rather than a clean knife cut. The woven fabric can be
perfect and the delivered edge can still be poor. At Smith Ribbon, blade replacement and edge dressing are tracked
per slitter with a recorded change interval, because the cheapest fix for an edge complaint is to notice that the
blade was due.</p>

<h2>3. The 4-Stage Edge Approval Gate</h2>

<p>Edge quality is approved in four stages. Each stage answers a different question, and skipping one is how
buyers end up approving a swatch that cannot survive production cutting.</p>

<h3>Stage 1 &mdash; Construction review (before loom setup)</h3>
<p>Confirm the selvage construction type, reed profile, edge warp routing and tension plan against the technical
specification before the loom is threaded. This is a paper review and it costs nothing. It is also the stage at
which a constructed selvage can still be added at negligible cost, and the stage at which adding it later becomes an
expensive conversation.</p>

<h3>Stage 2 &mdash; Greige edge check (after weaving, before finishing)</h3>
<p>Inspect the edge on the greige, before dyeing, printing, heat setting or calendaring. At this point the edge is
unobscured by finish, and the loom contribution can be separated from the finishing contribution. If the edge is
already defective here, no amount of finishing will fix it, and the mill should stop and correct the loom setting
rather than continue.</p>

<h3>Stage 3 &mdash; Finished-article edge qualification (on the approved sample)</h3>
<p>This is the gate most mills skip, and it is the one that protects the buyer. Heat setting, calendaring, coating
and printing all change the edge. A calendered ribbon can be pressed flat at the edge while a soft satin is left
unchanged. Measure the fray index, the parallelism and the cut-edge cleanliness on the <em>finished</em> article,
with the finishing route applied, not on a sample that skipped finishing.</p>

<h3>Stage 4 &mdash; In-line verification on production (per lot, sampled)</h3>
<p>During production, sample the edge at the start, middle and end of each lot and run the same three measurements.
The purpose is not to re-inspect every metre. It is to catch the drift &mdash; the slowly dulling blade, the slowly
changing tension, the heat build-up in the slitter &mdash; before it becomes a lot-wide defect.</p>

<div class="kpi">
  <p><strong>The Smith Ribbon edge approval rule:</strong> an edge parameter is approved on the finished article
  only. A green edge on greige fabric is not evidence of a green edge on the shipped roll, and a mill that quotes
  greige edge results is quoting you a number that has not yet been tested against the process that changes it.</p>
</div>

<h2>4. Measuring the Edge: Three Numbers, Not One</h2>

<p>&ldquo;Good edge&rdquo; is not a measurable claim. Three measurements make it one, and each catches a different
failure mode.</p>

<table>
  <thead>
    <tr><th>Measurement</th><th>Method</th><th>What it catches</th><th>Typical failure signature</th></tr>
  </thead>
  <tbody>
    <tr><td>Edge parallelism (mm)</td>
        <td>Deviation of the selvage line from the nominal edge position, sampled at 10&nbsp;m intervals along the roll
            against a reference edge</td>
        <td>Loom tension imbalance, weft tension differential, roll-build distortion</td>
        <td>Scalloped or bowed edge; ribbon that will not feed straight in a converting machine</td></tr>
    <tr><td>Fray index (ratio)</td>
        <td>Filament withdrawal count under a defined pull test at the edge, normalised to the qualified reference
            sample. Green 0.97&ndash;1.03, amber 0.90&ndash;0.97, red below 0.90</td>
        <td>Weft turn-around weakness, insufficient edge warp tension, natural (non-constructed) selvage on a
            guillotine-cut application</td>
        <td>Raveling at the cut line; lint and loose fibres in the finished assembly</td></tr>
    <tr><td>Cut-edge cleanliness (grade)</td>
        <td>Assessment of the cut edge at a defined viewing distance (typically 300&ndash;500&nbsp;mm) against a
            reference scale covering bevelling, burred filaments, edge dressing residue and shadowing</td>
        <td>Slitter blade condition, edge dressing quality, calendaring pressure at the edge</td>
        <td>Bevelled or burred edge; visible loose fibre halo; a trim that looks cheap under a shelf light</td></tr>
  </tbody>
</table>

<p>The three fail independently, which is why three are needed. A ribbon can be perfectly parallel and fray
badly &mdash; that is a selvage construction problem. It can fray well and be bevelled &mdash; that is a slitter
problem. It can be clean and out of parallel &mdash; that is a loom tension problem. A mill that reports only one
of the three has, in effect, reported the one that is easiest to measure.</p>

<h2>5. The 3-Tier Edge-Defect Reconciliation Ladder</h2>

<p>When the edge fails, the response should follow a fixed order, because the intuitive order &mdash; blame the
mill, then blame the material, then blame the machine &mdash; is usually backwards.</p>

<ol>
  <li><strong>Tier 1 &mdash; Isolate the layer.</strong> Re-measure on greige versus finished article. If the greige
  edge passes and the finished edge fails, the cause is in the finishing route (Tier E5 / E2), and the corrective
  action is a process adjustment. If both fail, the cause is upstream in construction (Tier E1) or loom setup
  (Tier E2).</li>
  <li><strong>Tier 2 &mdash; Isolate the mechanism.</strong> Establish whether the mechanism is a <em>material</em>
  mechanism (wrong yarn for the selvage, insufficient edge warp tension, a construction that cannot lock) or a
  <em>process</em> mechanism (blade wear, dressing residue, calendaring pressure, roll-build compression). These
  have different owners and different remedies, and conflating them is what turns a two-hour fix into a two-month
  dispute.</li>
  <li><strong>Tier 3 &mdash; Isolate the lot.</strong> Determine the extent. Is the defect present across the whole lot
  or confined to a start, middle or end segment? A defect that appears only in the last third of a lot usually points
  to blade wear developing during the run &mdash; a scheduled maintenance miss, not a quality decision. A defect
  present from the first metre points to setup. A defect that moves with the roll build points to compression or
  to winding tension.</li>
</ol>

<div class="kpi">
  <p><strong>The Smith Ribbon escalation rule:</strong> an edge defect is never closed on the basis of a verbal
  assurance that the next roll will be fine. Closure requires a re-measured sample from the corrected process, with
  all three measurements shown, plus a corrective action recorded against the specific layer and mechanism
  identified in Tiers 1 and 2.</p>
</div>

<h2>6. The Fray Early-Warning Threshold</h2>

<p>Most quality systems only react when a defect escapes. A better system watches the leading indicator and acts
before the defect is made. For edge quality, the leading indicator is the <strong>fray index trend across
consecutive lots</strong>.</p>

<p>The rule Smith Ribbon applies: if the fray index on three consecutive lots declines, even when every lot is still
inside the amber band, the loom is drifting and the corrective action is triggered at Tier 1. The most common
physical cause is progressive edge warp tension loss as the loom runs, combined with a slitter blade that is
simultaneously dulling &mdash; two slow drifts in the same direction, which together cross a threshold long before
either would alone.</p>

<p>A second leading indicator is the ratio of edge-related claims to total claims. A programme with a stable 2%
edge-claim rate that rises to 4% over two quarters is telling you something that the absolute number is not. The
percentage does not need to be large to be informative; it needs to be <em>trending</em>.</p>

<h2>7. Designing the Edge for the Customer&rsquo;s Actual End Use</h2>

<p>The single most useful question a buyer can ask a mill is not &ldquo;how good is your edge&rdquo; but
&ldquo;how is my edge going to be cut and handled&rdquo;. The correct edge specification is a function of the
customer&rsquo;s conversion process, and the most common specification error is asking for a general-purpose edge
for a specific-purpose application.</p>

<table>
  <thead>
    <tr><th>Customer end use</th><th>Cutting method</th><th>Edge requirement</th></tr>
  </thead>
  <tbody>
    <tr><td>Gift-box closure ribbon, pre-cut lengths</td>
        <td>Guillotine / straight knife in the customer&rsquo;s own plant</td>
        <td>Constructed selvage mandatory. Fray index at 1.00&ndash;1.03. A natural turn-around edge will not
            survive this process.</td></tr>
    <tr><td>Garment trim, stitched directly to the panel</td>
        <td>Fed through a sewing machine edge to edge</td>
        <td>Constructed selvage preferred. Parallelism matters more than fray, because feeding stability
            determines stitch quality.</td></tr>
    <tr><td>Floral and gift-wrapping, wound on spools for resale</td>
        <td>Customer-spooled, cut by the end consumer</td>
        <td>Parallelism primary, fray secondary. Cut-edge cleanliness matters because the consumer cuts it.</td></tr>
    <tr><td>Decorative bows, edge concealed inside the fold</td>
        <td>Cut short and folded; edge hidden</td>
        <td>Fray tolerance is generous. Parallelism and cleanliness remain relevant for the visible fold line.</td></tr>
    <tr><td>Automotive and technical trim, heat-sealed or encapsulated</td>
        <td>Cut then encapsulated in polymer</td>
        <td>Cleanliness primary. Any edge dressing residue or loose filament becomes a defect in the encapsulated
            part.</td></tr>
  </tbody>
</table>

<p>Two of these five rows would fail under a general-purpose specification. That is the practical argument for
writing edge requirements against end use rather than copying a generic clause.</p>

<h2>8. Implementation Path</h2>

<h3>Stage A &mdash; Add the three measurements to the incoming inspection plan</h3>
<p>Extend the existing incoming inspection routine to cover edge parallelism, fray index and cut-edge cleanliness on
a sampled basis per lot. The cost is a few minutes per roll. The benefit is that the first conversation about an
edge problem starts with data instead of with a photograph.</p>

<h3>Stage B &mdash; Freeze the edge at first article approval</h3>
<p>Put the selvage construction type, the fray requirement, the parallelism tolerance and the cleanliness grade
into the technical specification, and freeze them at FAI. Treat them as frozen parameters, exactly as colour is
frozen once approved. An edge that drifts is an edge that has been informally re-opened.</p>

<h3>Stage C &mdash; Track the fray trend, not just the fray result</h3>
<p>Plot the fray index by lot across the programme. A program-level trend line catches loom drift weeks before a
complaint is raised, because the complaint is raised by the customer and the trend is visible to you first.</p>

<h3>Stage D &mdash; Agree the reconciliation protocol before it is needed</h3>
<p>Agree with the mill, in writing and in advance, how an edge defect is isolated and closed: which measurement
distinguishes a material cause from a process cause, who runs the re-sample, and what evidence closes the incident.
Agreements reached during an incident are slow and defensive. Agreements reached during a calm month are fast and
neutral.</p>

<h2>9. Conclusion</h2>

<p>The edge of a ribbon is the only part of the trim that a customer physically handles, and it is the part most
often left unspecified. That combination is what makes it expensive: the parameter that is most visible to the end
buyer is the parameter the brand buyer has not written down.</p>

<p>The architecture in this module is deliberately mechanical rather than fashionable. Five layers with named
owners. Four approval gates, with the finished-article gate doing the real work. Three measurements that fail
independently and therefore must all be taken. A three-tier reconciliation ladder that separates material cause
from process cause before assigning blame. And a leading indicator that catches drift before a customer does.</p>

<p>When you next qualify a ribbon supplier, ask: <em>Show me the selvage construction type, the edge parallelism
across a roll, the fray index under a pull test on the finished article, and the cut edge at 300&nbsp;mm.</em> A
mill that can answer all four has an edge process. A mill that answers with a photograph of a swatch has an edge
outcome, and outcomes are not what you are buying.</p>

<h2>10. Frequently Asked Questions</h2>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a constructed selvage and when do I need it on ribbon?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A constructed selvage is an edge built so that the weft turns back into the warp with additional picks or a dedicated edge binding, locking the edge structure in place rather than letting the weft simply turn around. It costs more to weave than a natural turn-around edge, but it resists fraying and survives a guillotine cut in the customer's own plant. Constructed selvage is effectively mandatory for gift-box closure ribbon cut by the customer, and preferred for garment trim fed through sewing equipment. A natural turn-around edge is acceptable for decorative bows where the edge is concealed inside the fold."
      }
    },
    {
      "@type": "Question",
      "name": "How do you test the fray resistance of ribbon edge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fray resistance is measured as a fray index: the count of filaments withdrawn from the edge under a defined pull test, normalised against the qualified reference sample. The Smith Ribbon scale reads green from 0.97 to 1.03, amber from 0.90 to 0.97, and red below 0.90. The test must be run on the finished article with all finishing applied, because calendaring, heat setting and coating all change edge behaviour. Smith Ribbon tracks the index by lot so that a declining trend across three consecutive lots triggers a loom correction before a defect reaches the customer."
      }
    },
    {
      "@type": "Question",
      "name": "What causes a ribbon edge to look bevelled or burred?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The most common cause is a slitter blade that has run past its service life. It compresses and slightly rounds the cut rather than producing a clean knife edge, and it can leave a visible halo of loose fibres. A second cause is calendaring or pressing pressure applied unevenly at the edge. A third is edge-dressing residue left on the cut. This is why Smith Ribbon tracks blade change intervals per slitter as a controlled parameter, because bevelling is a maintenance miss rather than a design decision."
      }
    },
    {
      "@type": "Question",
      "name": "How much does a constructed selvage cost compared with a natural turn-around edge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A constructed selvage adds loom time and a small material allowance for the additional picks or edge binding, which typically puts it in the range of five to twelve per cent above the equivalent natural-edge construction depending on width and construction. Against a customer who cuts ribbon on their own guillotine, the avoided cost is usually far larger: a single cut-line failure in a customer's conversion plant consumes material that has already been invoiced, billed, and shipped. The comparison should be made against conversion-line failure cost, not against ribbon unit price."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum order quantity and lead time for custom ribbon with a controlled selvage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Xiamen Smith Ribbon & Bow Co., Ltd. has manufactured ribbon and decorative trims since 2004 in a 15,000 square metre plant with 200+ employees and 100,000 meters of daily capacity. Custom ribbon starts at 1,000 meters per colour, width and construction, with 500 meters available for small batches. A new construction with a defined selvage specification runs 25 to 35 days to an approved sample and 40 to 55 days to first production shipment, with OEKO-TEX, FSC, BSCI, SEDEX, SMETA and ISO 9001 certification available."
      }
    }
  ]
}
</script>

<p>Below are the questions brand buyers most frequently raise when introducing a formal edge-quality programme into an
OEM ribbon relationship. If your question is not covered here, our compliance engineers will answer it directly.</p>

<h3>What is a constructed selvage and when do I need it on ribbon?</h3>
<p>A constructed selvage is an edge built so that the weft turns back into the warp with additional picks or a
dedicated edge binding, locking the edge structure in place rather than letting the weft simply turn around. It
costs more to weave than a natural turn-around edge, but it resists fraying and survives a guillotine cut in the
customer&rsquo;s own plant. Constructed selvage is effectively mandatory for gift-box closure ribbon cut by the
customer, and preferred for garment trim fed through sewing equipment. A natural turn-around edge is acceptable for
decorative bows where the edge is concealed inside the fold.</p>

<h3>How do you test the fray resistance of ribbon edge?</h3>
<p>Fray resistance is measured as a fray index: the count of filaments withdrawn from the edge under a defined pull
test, normalised against the qualified reference sample. The Smith Ribbon scale reads green from 0.97 to 1.03, amber
from 0.90 to 0.97, and red below 0.90. The test must be run on the finished article with all finishing applied,
because calendaring, heat setting and coating all change edge behaviour. Smith Ribbon tracks the index by lot so that
a declining trend across three consecutive lots triggers a loom correction before a defect reaches the customer.</p>

<h3>What causes a ribbon edge to look bevelled or burred?</h3>
<p>The most common cause is a slitter blade that has run past its service life. It compresses and slightly rounds the
cut rather than producing a clean knife edge, and it can leave a visible halo of loose fibres. A second cause is
calendaring or pressing pressure applied unevenly at the edge. A third is edge-dressing residue left on the cut. This
is why Smith Ribbon tracks blade change intervals per slitter as a controlled parameter, because bevelling is a
maintenance miss rather than a design decision.</p>

<h3>How much does a constructed selvage cost compared with a natural turn-around edge?</h3>
<p>A constructed selvage adds loom time and a small material allowance for the additional picks or edge binding, which
typically puts it in the range of five to twelve per cent above the equivalent natural-edge construction depending on
width and construction. Against a customer who cuts ribbon on their own guillotine, the avoided cost is usually far
larger: a single cut-line failure in a customer&rsquo;s conversion plant consumes material that has already been
invoiced, billed, and shipped. The comparison should be made against conversion-line failure cost, not against
ribbon unit price.</p>

<h3>What is the minimum order quantity and lead time for custom ribbon with a controlled selvage?</h3>
<p>Smith Ribbon has run production since 2004 with 1,000&nbsp;m MOQ per colour, width and construction, and
500&nbsp;m for small batches. A new construction with a defined selvage specification runs 25&ndash;35 days to an
approved sample and 40&ndash;55 days to first production shipment, with OEKO-TEX, FSC, BSCI, SEDEX, SMETA and
ISO 9001 certification available.</p>
"""

write_article(a, BODY,
              "Specify the edge, not just the width",
              "Request the selvedge and cut-edge specification template and a fray-index walkthrough")
print(f"slug={SLUG}")
