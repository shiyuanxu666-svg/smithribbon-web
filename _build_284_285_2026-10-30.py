#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon B2B articles 284 (AM) and 285 (PM) - 2026-10-30.

AM: ribbon OEM 284 - ribbon width tolerance & edge parallelism on bows / narrow-width
    stability: slittable width tolerance, selvedge vs cut edge, bow symmetry drift.
PM: ribbon OEM 285 - ribbon roll packaging format & carton configuration: roll length,
    core winding direction, weight tolerance, carton/loading, moisture barrier.

Both: 1200+ words, full meta + OG + Twitter, BlogPosting + BreadcrumbList + FAQPage
JSON-LD, visible FAQ section at the end, standard footer.
"""
import sys
from pathlib import Path

sys.path.insert(0, "/workspace/smithribbon-web")
from smithribbon_article_lib import write_article

ROOT = Path("/workspace/smithribbon-web")

# ============================================================================
# ARTICLE 284 (AM) - Width tolerance / edge parallelism / bow symmetry
# ============================================================================

A284 = {
    "fname": ("blog-ribbon-oem-284-module-mill-side-brand-buyer-ribbon-width-tolerance-slitting-"
              "edge-parallelism-bow-symmetry-drift-interlock-architecture-cut-vs-selvedge-edge-"
              "narrow-width-stability-2026-10-30-am.html"),
    "slug": ("blog-ribbon-oem-284-module-mill-side-brand-buyer-ribbon-width-tolerance-slitting-"
             "edge-parallelism-bow-symmetry-drift-interlock-architecture-cut-vs-selvedge-edge-"
             "narrow-width-stability-2026-10-30-am"),
    "title": ("Mill-Side Brand-Buyer Ribbon Width Tolerance &amp; Edge Parallelism Interlock Architecture "
              "&mdash; Cut Edge vs Selvedge, Narrow-Width Stability and Bow Symmetry Drift 2026"),
    "desc": ("A mill-side brand-buyer guide to ribbon width tolerance and edge parallelism. Covers why a "
             "width tolerance without an edge-type reference is meaningless, how a cut edge frays and drifts "
             "differently from a self-selvage edge, why narrow widths amplify loom instability, how width "
             "drift propagates into bow asymmetry, and the 6-part width and edge specification template "
             "that makes a repeat order land on the same bow geometry."),
    "keywords": [
        "ribbon width tolerance OEM", "ribbon slitting width control", "cut edge selvedge ribbon",
        "bow symmetry ribbon", "narrow width ribbon stability", "ribbon edge parallelism inspection",
        "ribbon width measurement method", "custom ribbon slitting supplier", "ribbon OEM China width spec",
        "grosgrain width tolerance", "satin ribbon width variance", "ribbon selvage fray prevention",
        "printed ribbon registration width", "ribbon bow leg length consistency", "brand buyer ribbon spec sheet",
        "ribbon trimming edge quality", "woven ribbon width tolerance guide",
    ],
    "pub_iso": "2026-10-30T02:00:00+00:00",
    "wordcount": 2600,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Ribbon Width Tolerance &amp; Edge Parallelism Interlock",
    "lede": ("Width tolerance is the specification that most often appears in a ribbon purchase order and most "
             "often does nothing. A number written as plus or minus 0.5 mm looks like a commitment, but it is "
             "not a commitment at all until the reader knows which edge is the reference, where along the roll "
             "the measurement is taken, how the ribbon is tensioned during measurement, and whether the number "
             "describes the ribbon as woven or the ribbon as slit and finished. The same ribbon, measured two "
             "ways by two competent inspectors, can differ by more than the entire tolerance band. Once that "
             "ambiguity is understood, the rest of the subject becomes surprisingly tractable: width drift is "
             "not random, it has identifiable causes, and each cause has a specific place in the process where "
             "it can be stopped."),
    "body": """
<h2>Why a width tolerance without an edge reference is not a specification</h2>
<p>A woven ribbon is not a uniform solid. It has two physically different edges, and they behave differently
for the whole of its life.</p>

<p>The <strong>selvedge</strong> is the edge created by the loom itself, where the warp yarns turn around and
return. It is compact, it is structurally integral to the cloth, and it is typically the most stable edge the
ribbon has. The <strong>cut edge</strong> is created after weaving, by a slitter knife or a rotary knife
passing through the fabric. It has no selvedge structure at all. It is a raw cut through the yarn system, and
it will behave like a cut edge for the entire life of the product.</p>

<p>Here is the practical consequence that catches almost every brand buyer at least once: a ribbon 20 mm wide
with a 19 mm selvedge on one side and a 1 mm trimmed margin on the other is <em>not</em> the same product as
a ribbon 20 mm wide with selvedge on both sides, even though both measure 20 mm. The trimmed side will
fray differently, will show a different print registration behaviour at the edge, will have a different
tensile strength profile, and will look visibly different when the ribbon is folded or tied. If your
tolerance says only "width 20 mm, tolerance plus or minus 0.5 mm", the inspector and the mill can each
satisfy it and still deliver materially different goods.</p>

<p>Every usable width specification therefore has to name, at minimum:</p>
<ol>
  <li>the nominal width and the tolerance band, stated with a plus/minus or a min/max, never a bare number;</li>
  <li>the edge type on each side - selvedge, trimmed, or self-hemmed;</li>
  <li>the measurement method, including tension, gauge and instrument;</li>
  <li>the sampling rule - how many points across the width, how many points along the length, how many rolls;</li>
  <li>the measurement condition - relaxed or under stated tension, after stated conditioning;</li>
  <li>which state of the process the width refers to - loom, post-dye, post-finish, or post-slit.</li>
</ol>

<h2>The four sources of width drift, and where each one is stopped</h2>
<p>Width variance in a finished ribbon is not one phenomenon. It is the sum of several distinct causes, and
each has a different owner and a different fix.</p>

<h3>1. Loom-width instability - the ribbon was never the width it was supposed to be</h3>
<p>Every loom has a nominal working width and a real working width that moves. Weaving tension on the warp,
the take-up rate on the weft, the shrinkage of the warp in the reed, and the temperature and humidity of the
weaving hall all shift the fabric width during the run. On a wide ribbon, this is absorbed by the selvedge
margin and is invisible. On a narrow ribbon, the same instability is a meaningful percentage of the total
width.</p>

<p>This is why narrow-width ribbon is disproportionately difficult and why the tolerance for a 6 mm ribbon
should not simply be the tolerance for a 50 mm ribbon expressed as a percentage. A mill that produces a 50 mm
ribbon to plus or minus 0.5 mm is working with a roughly 1 percent band on a width where a fraction of a
millimetre of loom movement is easily absorbed. The same mill asked to hold 6 mm to plus or minus 0.5 mm is
being asked for an 8 percent band on a width where the loom cannot deliver that precision without dedicated
narrow-width weaving and a specific width-control strategy.</p>

<p>As a general procurement rule: ask the mill to state the tolerance band they can actually hold on that
specific width, on that specific construction, and treat any request for a narrower band as a request for a
different manufacturing route rather than a request for more care. Narrow-width ribbon is often better made on
a wide loom and slit down, precisely because that is where width control is easiest.</p>

<h3>2. Slitting tolerance - the ribbon was right and the knife was not</h3>
<p>When ribbon is woven wide and slit to width, the slitting operation introduces its own tolerance. Two
mechanisms are common. A straight knife in a slitter produces a cut whose position depends on the tension
running through the fabric at the moment of the cut; fabric that is not uniformly tensioned across its width
will be cut with the knife at a slightly different distance from the reference edge at different points in the
roll. A rotary knife produces a cleaner edge with less drag and less fraying, but still has a positional
tolerance.</p>

<p>There is also a <strong>bow and skew</strong> component. If the fabric entering the slitter is skewed -
the warp yarns running at an angle rather than square to the edge - then a slitter that cuts parallel to the
machine direction produces an edge that drifts in and out across the width of the ribbon over the length of
the roll. This is not a width error at all. The ribbon is exactly the right width everywhere; it is just not
square. The result is a ribbon whose usable width varies, and whose two edges are not parallel.</p>

<p>This is why <strong>edge parallelism</strong> has to be measured and specified separately from width. A ribbon
that is 20.0 mm wide and whose edges are not parallel is a worse problem than a ribbon that is 20.4 mm wide
and whose edges are perfectly parallel. The first one cannot be cut reliably by the customer's converting
process; the second one just needs a slightly wider allowance.</p>

<h3>3. Dimensional change through dyeing and finishing</h3>
<p>Wet processing relaxes and re-tensions the yarn system. Heat-setting stabilises it, but the width the ribbon
has after finishing is not automatically the width it had off the loom. A ribbon that is 20.5 mm off the loom
and finishes at 20.0 mm is perfectly healthy; the problem arises when the mill slits to 20.0 mm before
finishing and then relaxes the ribbon during finishing, so the finished product is 19.4 mm. This is a
sequencing error, and it is common, because slitting before finishing is faster and cheaper than slitting
after.</p>

<p>The rule that follows from this is simple: <strong>the width in your purchase order is the width of the
finished product.</strong> Any mill-side documentation that quotes a loom or greige width against your
finished-goods tolerance is comparing two different things.</p>

<h3>4. Winding and roll build - the ribbon was right and the roll is lying</h3>
<p>A ribbon wound onto a core under insufficient or excessive tension will measure differently at the roll
surface and at the roll core. It will also develop a memory: a roll that has been held under tension for
months will not lie flat when opened, and the ribbon will appear narrower or wider depending on how the
inspector happens to be holding it. This is the cheapest of the four causes to eliminate and the one most
often left in place, because it is invisible to everyone who is not measuring.</p>

<h2>Edge type: the specification most worth getting right</h2>
<p>Given that the cut edge and the selvedge behave differently, the practical question for a brand buyer is
which edge type the application actually requires.</p>

<table>
  <tr><th>Edge type</th><th>Structure</th><th>Fray behaviour</th><th>Typical use</th></tr>
  <tr><td>Selvedge (woven)</td><td>Compact, integral to the cloth, yarn turns around</td>
      <td>Does not fray in normal use; may ravel slightly at a raw cut through it</td>
      <td>Premium trims, visible edges on bows, narrow bands</td></tr>
  <tr><td>Cut / slit edge</td><td>No edge structure; yarns severed</td>
      <td>Will fray along the cut line, more so with low-density constructions and in high humidity</td>
      <td>Interior trims, wrapped edges, anything later over-sewn or bound</td></tr>
  <tr><td>Folded / self-hemmed</td><td>Edge turned and stitched or glued</td>
      <td>None at the fold; adds width and thickness</td>
      <td>Retail display trims, garment edging, visible cut edges</td></tr>
</table>

<p>If the application is a retail product where the ribbon edge is visible and handled by the end consumer -
a hair bow, a gift bow, a favour ribbon on a package - a selvedge edge is worth specifying even though it
costs more, because the failure mode of a fraying edge is a consumer complaint rather than a factory rework.
If the edge is going to be bound, over-sewn or hidden inside a construction, a cut edge is entirely adequate
and considerably more economical.</p>

<h2>How width drift turns into bow asymmetry</h2>
<p>Most buyers think about width as a quality metric. Its real significance is that it propagates directly
into the geometry of the finished bow, and bow geometry is what the end consumer sees.</p>

<p>A bow is made by folding ribbon at a defined point and forming the two legs and the tails. The relationship
between ribbon width and bow proportion is close to linear: a wider ribbon at the same fold and same loop
depth produces a wider, flatter bow with shorter-looking legs. Change the width by one millimetre on a
38 mm ribbon and you have changed the silhouette of the product. On a 20 mm ribbon, the same one millimetre is
a proportionally larger shift, and on a 10 mm ribbon it dominates entirely.</p>

<p>Across a production run, width drift therefore shows up downstream as a spread in the finished bow: some
bows in the same carton have visibly wider loops or longer tails than others. It is a subtle, cumulative
inconsistency that is very hard to photograph and very easy for a customer to feel. Buyers who have chased
"the bows look inconsistent" for months have frequently been chasing a width tolerance all along.</p>

<p>There is a second, more mechanical route by which width reaches bow geometry. A ribbon that is not edge
parallel will not fold symmetrically. On a pre-tied bow, the fold sits on the diagonal, and a skewed ribbon
will present an unequal fold angle on the two loops, so one loop stands up and the other lies flatter. This is
visible in finished goods at a glance, and it is not a workmanship problem - it is a material problem that was
detectable at the incoming inspection stage.</p>

<h2>The 6-part width and edge specification template</h2>
<p>Pulling this together into something you can hand to a mill and an inspector and have both read the same
thing:</p>

<table>
  <tr><th>#</th><th>Element</th><th>How to specify it</th></tr>
  <tr><td>1</td><td>Nominal width and tolerance</td>
      <td>State nominal, state the band as plus/minus or min/max, and state the band per width band and per
      construction. Ask the mill to confirm the band it can hold on that width.</td></tr>
  <tr><td>2</td><td>Edge type, both sides</td>
      <td>Selvedge / trimmed / self-hemmed, stated per side, not just "raw edge" or "finished edge".</td></tr>
  <tr><td>3</td><td>Measurement method</td>
      <td>Instrument, gauge location, applied tension, whether relaxed or tensioned, and whether the reading
      is taken at the roll surface or the core.</td></tr>
  <tr><td>4</td><td>Sampling rule</td>
      <td>Number of points across the width and along the length, number of rolls per lot, and whether the
      acceptance is per-roll or per-lot.</td></tr>
  <tr><td>5</td><td>Edge parallelism</td>
      <td>Maximum permitted bow or skew as a millimetre figure per metre of length, measured against the
      selvedge or a declared reference edge.</td></tr>
  <tr><td>6</td><td>Measurement state</td>
      <td>Conditioning temperature and humidity and duration, and whether the value refers to loom, greige,
      post-dye, post-finish or slit state.</td></tr>
</table>

<p>Add two triggers: a <strong>re-test trigger clause</strong> naming the changes that invalidate an approved
width - a change of loom, a change of yarn supplier or denier, a change of dyehouse, a change of finishing
route, a change of width, a change of slitting route - and a <strong>bow consequence clause</strong> stating
what the finished bow geometry must be when made from the approved ribbon width. The first clause prevents
silent drift across a reorder programme; the second closes the loop between a mill-side number and the
product the consumer actually receives.</p>

<h2>Incoming inspection: what to actually measure</h2>
<p>A width inspection that only measures width will pass ribbons that will fail downstream. The minimum
practical incoming check on a narrow-width programme is four measurements:</p>
<ul>
  <li><strong>Width</strong> at the specified reference points, with the specified tension and instrument;</li>
  <li><strong>Edge parallelism</strong>, checking the cut or selvedge edge against a straight reference over a
  defined length, to catch bow and skew;</li>
  <li><strong>Edge condition</strong>, examined at the cut line for evidence of fraying, loose yarns or a
  crushed edge from a dull or damaged knife;</li>
  <li><strong>Width across the roll</strong>, measured at the roll surface and at the core, to detect roll
  build differences that will show up as dimensional drift after storage.</li>
</ul>

<p>Cutting a bow from a ribbon whose edges are not parallel produces a visibly asymmetric product that no
amount of care in the bow-making step will fix. That is worth remembering at the inspection table: some
defects are created long before the product that shows them exists.</p>

<h2>Working with the mill</h2>
<p>Most mills welcome a width and edge specification of this detail, because it removes ambiguity from the
quotation. The mills that object are usually the ones whose process is not actually controlled tightly enough
to meet it, which is useful information in itself.</p>

<p>Ask for the mill's own capability: not "can you hold plus or minus 0.5 mm" but "what tolerance do you
routinely hold on this width and this construction, and how do you measure it". A mill with a real slitting and
measurement discipline will answer with numbers and will tell you the measurement conditions. A mill that
answers with "we always make it right" is telling you something else entirely.</p>

<p>Smith Ribbon has manufactured ribbon and bows since 2004, running in-house weaving, dyeing, finishing,
slitting and bow assembly in Xiamen. Our engineering team will quote the width band we can actually hold for
your specific width, construction and edge type, together with the measurement conditions we use, and we will
tell you where we think a narrower band would require a different manufacturing route rather than more care.
If you have a current width specification that is causing disputes, send it to us and we will tell you
honestly whether the band is realistic for your construction.</p>
""",
    "faq": [
        ("What is a reasonable width tolerance for ribbon?",
         "It depends on the width and the construction, and the honest answer is that it is narrower than most "
         "buyers assume at narrow widths and wider than they assume at wide widths. For wide ribbon made on a "
         "wide loom, a band of plus or minus 0.5 mm is comfortably achievable. For narrow ribbon below about "
         "10 mm, the same absolute band represents a much larger proportion of the width and is usually not "
         "achievable by weaving to width - the practical route is to weave wide and slit, or to accept a wider "
         "band. The correct approach is to ask the mill to state the band it routinely holds on your specific "
         "width and construction, with its measurement conditions, and to write that number into the purchase "
         "order instead of assuming a number."),
        ("What is the difference between a selvedge edge and a cut edge on ribbon?",
         "A selvedge edge is created by the loom as the warp yarns turn around, so it is compact and integral to "
         "the structure. A cut edge is created by a slitting or rotary knife passing through the fabric, which "
         "severs the yarns and leaves no edge structure at all. The practical consequences are that a cut edge "
         "can fray along the cut line, particularly on low-density constructions, while a selvedge edge does "
         "not fray in normal use, and that the two edges have different print registration behaviour, "
         "different tensile profiles and different visual appearance when the ribbon is folded or tied."),
        ("Why does the same ribbon measure differently at different points across the width?",
         "Three things cause it. First, loom working width moves during a run as weaving tension, take-up "
         "rate and hall conditions shift, and the effect is proportionally larger on narrow ribbon. Second, "
         "slitting introduces its own positional tolerance and, if the incoming fabric is skewed, produces an "
         "edge that is cut square to the machine but not parallel across the ribbon. Third, yarn tension "
         "across the width is rarely perfectly even, so a ribbon will pull slightly narrower under tension in "
         "one region than another. This is why edge parallelism has to be specified and measured separately "
         "from width, rather than treated as a detail of the width measurement."),
        ("Does ribbon width drift really affect the finished bow?",
         "Yes, and this is where width stops being a quality number and becomes a product-design variable. The "
         "relationship between ribbon width and bow proportion is close to linear, because a wider ribbon at the "
         "same fold and loop depth produces a wider, flatter bow with legs that appear shorter. Change the width "
         "by one millimetre on a 38 mm ribbon and the silhouette changes visibly; on a 10 mm ribbon the same "
         "millimetre dominates the shape entirely. Separately, a ribbon whose edges are not parallel does not "
         "fold symmetrically, so one loop of a pre-tied bow stands up while the other lies flatter - a defect "
         "that is created at the slitting stage but only becomes visible at the bow-making stage."),
        ("Should the width in the purchase order be the loom width or the finished width?",
         "The finished width, always. Wet processing relaxes and re-tensions the yarn system, and heat-setting "
         "then stabilises it, so the finished width is not automatically the greige width. The common error is "
         "for a mill to slit to target before finishing and then let the ribbon relax during finishing, "
         "delivering a product that is genuinely narrower than the purchase order. Any mill-side document "
         "quoting a loom or greige width against your finished-goods tolerance is comparing two different "
         "measurements, and that discrepancy should be corrected before the first order is placed."),
        ("What causes width variation between different rolls of the same order?",
         "Three causes account for most of it. Different rolls may come from different production runs with "
         "different loom conditions, so the mill should tell you the lot or run structure of your order. "
         "Different positions in the roll behave differently, because roll build tension varies from surface to "
         "core, so the same ribbon measures differently depending on where the sample is taken. And different "
         "storage history changes the reading, because ribbon that has been held under tension in storage "
         "develops a set. Measuring at a defined position in the roll, under a defined conditioning regime, "
         "with a defined tension, removes all three as sources of dispute."),
        ("How do we avoid disputes with the mill about width?",
         "Agree the measurement protocol before the order is placed, not after the first shipment arrives, and "
         "write it into the purchase order as six elements: nominal width with a stated band, edge type per "
         "side, measurement method including instrument and tension, sampling rule for points and rolls, edge "
         "parallelism limit, and the measurement state including conditioning. Then add a re-test trigger clause "
         "naming the changes that invalidate an approved width - loom, yarn supplier, dyehouse, finishing "
         "route, width, slitting route - so that re-qualification is prompted by the specification rather than "
         "by memory."),
        ("Does a narrow ribbon need a wider tolerance than a wide one?",
         "Yes, as a proportion, and this is where specifications most often go wrong. The absolute tolerance "
         "that a wide loom can hold on a 50 mm ribbon may be impossible to hold on a 6 mm ribbon, because loom "
         "movement that is absorbed by a wide selvedge margin becomes a large percentage of a narrow width. "
         "Rather than applying one absolute band across a range of widths, specify a band per width band and "
         "per construction, and ask the mill to confirm what it can actually hold. If the band you want on a "
         "narrow width is tighter than the mill can hold by weaving, the answer is often to change the "
         "manufacturing route - weaving wide and slitting - rather than to ask for more care."),
    ],
    "cta_title": "Need a width band you can actually hold?",
    "cta_body": ("Send us your current width specification, your construction and your edge requirement. We will "
                 "quote the tolerance band we can reliably hold for that specific width and tell you plainly "
                 "whether a tighter band is realistic or requires a different manufacturing route."),
    "cta_link_text": "Request a width capability quote",
}

# ============================================================================
# ARTICLE 285 (PM) - Roll packaging format / carton / winding
# ============================================================================

A285 = {
    "fname": ("blog-ribbon-oem-285-module-mill-side-brand-buyer-ribbon-roll-packaging-format-carton-"
              "configuration-interlock-architecture-roll-length-core-winding-direction-weight-tolerance-"
              "moisture-barrier-loading-2026-10-30-pm.html"),
    "slug": ("blog-ribbon-oem-285-module-mill-side-brand-buyer-ribbon-roll-packaging-format-carton-"
             "configuration-interlock-architecture-roll-length-core-winding-direction-weight-tolerance-"
             "moisture-barrier-loading-2026-10-30-pm"),
    "title": ("Mill-Side Brand-Buyer Ribbon Roll Packaging &amp; Carton Configuration Interlock Architecture "
              "&mdash; Roll Length, Core Winding Direction, Weight Tolerance and Moisture Barrier 2026"),
    "desc": ("A mill-side brand-buyer guide to ribbon roll packaging and carton configuration. Covers why roll "
             "length is a costing variable and not just a packing detail, how core winding direction and "
             "rotation affect how a ribbon behaves in your converting line, why weight tolerance matters more "
             "than length tolerance for automatic feeding, how carton format interacts with humidity and "
             "compression damage, and the packaging specification that keeps ribbon arriving in the same "
             "condition it left the mill in."),
    "keywords": [
        "ribbon roll packaging specification", "ribbon carton configuration OEM", "ribbon core winding direction",
        "ribbon roll weight tolerance", "ribbon moisture barrier packaging", "custom ribbon packaging format",
        "ribbon roll length standard", "ribbon OEM carton loading", "ribbon storage humidity damage",
        "ribbon roll compression set", "ribbon core size 76mm", "ribbon winding direction converter",
        "ribbon packaging B2B guide", "ribbon reel packaging supplier", "brand buyer ribbon packing spec",
        "ribbon carton weight limits", "ribbon mill roll format",
    ],
    "pub_iso": "2026-10-30T07:00:00+00:00",
    "wordcount": 2600,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Ribbon Roll Packaging &amp; Carton Configuration Interlock",
    "lede": ("Packaging is the last specification a buyer writes and the first one that determines what happens "
             "to your ribbon before your customer sees it. A ribbon that leaves the mill perfectly on width and "
             "colour can arrive with a compression set from a carton stacked three high in a humid warehouse, "
             "or with a moisture gradient that shifts the colour of the outer wrap relative to the core, or "
             "wound in a direction that fights your converting line every time it runs. None of this is visible "
             "on an incoming inspection that only measures width and colour. It shows up as production problems "
             "in your own plant, weeks later, and it is very often attributed to the wrong cause."),
    "body": """
<h2>Why packaging is a technical specification, not a logistics detail</h2>
<p>Ribbon is a lightweight, hygroscopic, dimensionally sensitive textile product with a very high surface-area-
to-weight ratio. That combination makes it unusually sensitive to how it is packed. A carton of ribbon that is
left in a hot, humid distribution centre does not simply arrive damp - it arrives with a moisture gradient
through the roll, a compressed core, and a surface that no longer matches the colour of the material beneath
it.</p>

<p>For a brand buyer, packaging is therefore relevant to at least five separate decisions, and it is worth
making each of them explicitly rather than accepting the mill's default:</p>
<ol>
  <li>How much material arrives per roll, and therefore how much material you handle per receiving operation;</li>
  <li>How the ribbon is oriented when it is unwound, and therefore how your converting line behaves;</li>
  <li>How the ribbon is protected from humidity and from compression while in transit and storage;</li>
  <li>How the carton is packed, which determines how many cartons fit on a pallet and whether the load is stable;</li>
  <li>How much the packaging costs, which is a larger share of the material cost than most buyers expect.</li>
</ol>

<h2>Roll length: a costing variable disguised as a convenience</h2>
<p>The single most consequential packaging decision is the roll length, and it is usually made by whoever set
up the slitting and winding process, not by the buyer.</p>

<p>Roll length determines how many changes the buyer makes per production run. A 200-metre roll of 20 mm ribbon
on a 76 mm core means 20 or 30 changes to produce 6 kilometres of material. A 1,000-metre roll means three or
four. Every change carries a cost: restocking the winder, splicing, re-threading, trimming the lead-in, and
re-establishing tension. For high-volume programmes this is significant, and for programs where the ribbon is
cut in short runs it can dominate the conversion cost.</p>

<p>But roll length is not a free choice, because of two opposing constraints.</p>

<p>The first is <strong>core deflection and set</strong>. A long roll of ribbon wound on a small core develops a
conical profile: the outer layers are held under higher compression than the inner layers, and a ribbon wound
over many hours of production will carry a memory of that compression. The longer the roll, the more pronounced
this becomes, particularly on soft constructions such as satin or velvet where the pile or the lustre is
affected. A buyer receiving 1,000-metre rolls of soft ribbon will often find that the material at the roll
core is measurably different in behaviour from the material at the roll surface.</p>

<p>The second is <strong>handling weight</strong>. Ribbon is light per metre, but a long roll on a small core
becomes awkward to handle, and combined with a carton that is itself heavy, the total handling unit can
exceed what a warehouse team will lift comfortably or what a pallet can carry without exceeding standard
pallet weights. This matters for DDP and FOB arrangements and for warehouse labour planning in a way that is
rarely visible in a purchase order.</p>

<p>The pragmatic approach is to specify roll length by programme type rather than by a single global rule:
development and sample rolls short, mainstream production rolls at a length that balances changeover cost
against core deflection, and very high-volume programmes negotiated on a dedicated winding plan with the
mill so that the roll geometry is designed rather than inherited.</p>

<h2>Core winding direction and rotation: a detail that costs hours per week</h2>
<p>Every roll of ribbon is wound in a specific direction. The direction of winding, and the direction the roll
is permitted to rotate on the winder, determines how the ribbon feeds onto your converting equipment.</p>

<p>Most ribbon converting - cutting to length, folding into bows, over-sewing, edge binding, gift set assembly -
uses a roll that unwinds with the <strong>face side out</strong> and the ribbon running in a specific direction
relative to the winder axes. When the mill winds the roll in the opposite direction from what the converter
expects, the result is not a quality failure. It is a line that runs with the ribbon inside out, or a line
that requires a roll to be flipped and re-spooled every time a new roll is mounted, or a line where the
operator has to stop and reverse the rotation direction each time.</p>

<p>That last case is the expensive one. It is invisible in the incoming goods, it is invisible on the purchase
order, and it consumes several minutes of operator attention every single time a roll is changed. Across a year
with weekly changes on multiple lines, it becomes a meaningful and entirely avoidable production cost.</p>

<p>The specification should therefore state, unambiguously: the winding direction, the face-out or face-in
orientation, the permitted rotation direction on the winder, and the position of the free end so it can be
found without unwinding the roll. Experienced buyers also ask for a printed arrow or a coloured tape mark at
the roll start, because the operator who is changing the roll at 3 a.m. is not going to be reading a purchase
order.</p>

<p>Two further points are worth stating. First, the roll should be wound without a leader or with a leader of a
material that will not mark the ribbon. Second, the roll should start at a position where the free end can be
found without unrolling the entire roll, because a roll buried under fifty metres of ribbon is a roll that gets
cut off and re-spooled anyway.</p>

<h2>Weight tolerance versus length tolerance</h2>
<p>Buyers routinely specify roll length to the metre and leave weight unqualified. For automated or
semi-automated feeding, this is backwards.</p>

<p>A converting line that feeds ribbon by weight - counting a pre-weighed cut length per cycle - is far less
sensitive to how many metres are on the roll than to how much each metre weighs. A ribbon at 0.06 g/m will
produce a different cut length from the same ribbon at 0.07 g/m, and the control loop on the machine will
compensate automatically if it is set up for weight. A ribbon at the right weight but 15 percent short on the
roll will simply mean more roll changes.</p>

<p>Weight tolerance also matters for shipment planning and freight costing, because ribbon is frequently sold
and shipped on a weight basis for customs and freight purposes. A wide weight tolerance makes the freight
estimate unreliable and makes it hard to reconcile the invoice against the arrival.</p>

<p>The specification should therefore give weight tolerance at a stated roll length, and should state the basis
on which the weight is measured: net of core, or inclusive of core, and at what conditioning state. It should
also state the width and construction, because a weight figure is only meaningful alongside a construction -
a 38 mm velvet ribbon and a 38 mm organza ribbon at the same roll length have no meaningful weight
relationship.</p>

<h2>Moisture, barrier packaging and colour shift</h2>
<p>Polyester ribbon is hygroscopic to a modest but commercially significant degree. Absorbed moisture changes
the refractive behaviour of the fibre and the perceived colour of the material, and the effect is strongest at
the surface of a roll that has been in a humid environment - which means the outer wrap can read differently
from the material beneath it.</p>

<p>For a brand with a tight colour tolerance this produces a problem at the retail floor: the ribbon on the
outer roll matches the approved swatch, and the ribbon from the middle of the roll does not. For a buyer
running a colour-matching workflow across multiple lots, it creates the impression of lot inconsistency when
the material is in fact perfectly consistent and the packaging is the variable.</p>

<p>Three packaging decisions address it:</p>
<ol>
  <li><strong>Barrier material.</strong> Polyethylene or metallised film around the roll, which slows moisture
  transfer. Where colour consistency across a programme matters enough to justify it, the barrier specification
  should be a line item rather than left to the mill's default.</li>
  <li><strong>Individual roll wrapping versus carton-level protection.</strong> Wrapping each roll individually
  protects the outer surface of each roll; wrapping the carton protects the outermost rolls of the carton only,
  and leaves the inner rolls exposed to the humidity that develops inside a closed carton over a long sea
  transit. For long-haul or seasonal storage, individual wrapping is the meaningful protection.</li>
  <li><strong>Desiccant and conditioning.</strong> A moisture absorber in the carton controls the humidity inside
  the closed package. It must be appropriate to the quantity of material and the transit duration, and it must
  not be so aggressive that it creates its own problem at the other end - an over-dried ribbon can be brittle
  and can behave differently in a hot, dry shop floor.</li>
</ol>

<p>And one decision that is often overlooked entirely: <strong>the carton should be lined or the rolls should be
segregated so that a damaged or defective roll does not contaminate its neighbours.</strong> A single
water-stained or oil-stained roll in a carton can transfer the stain to adjacent rolls through contact, and the
damage is discovered after the rolls have been opened and used rather than at goods-in.</p>

<h2>Carton configuration and compression damage</h2>
<p>Ribbon cartons fail in a characteristic way: the carton walls bow outwards or the corners crush under the
weight of the cartons stacked above them, and the rolls inside take the load. The compression reaches the
outer ribbon layers first and the effect is a permanent set - a flat ribbon that no longer lies flat, or a
curved ribbon whose edges will not meet when the customer folds it.</p>

<p>This is why compression damage is nearly invisible on a roll in the middle of a carton and severe on the
rolls at the bottom. It also explains why a ribbon that was perfect at incoming inspection can be rejected by
the customer three weeks later, and why the rejected goods look fine while the ribbon from the same carton
that was on top looks slightly different.</p>

<p>Four practical controls, all of which belong in the packaging specification:</p>
<ul>
  <li><strong>Gross weight limit per carton</strong>, so that the handling unit stays within a weight that the
  pallet and the warehouse can carry safely, and so that the bottom rolls are not bearing more load than the
  material tolerates;</li>
  <li><strong>Carton board grade and edge protection</strong>, so the carton resists the stacking load it will
  actually see rather than a nominal one;</li>
  <li><strong>Interleaving or separator sheets</strong> between vertically stacked rolls, which distributes the
  load rather than concentrating it on the outermost layer of the roll beneath;</li>
  <li><strong>A stacking limit stated on the carton</strong>, which protects the mill's warehouse staff as much
  as the ribbon, and prevents a well-meaning distribution centre from stacking to the ceiling.</li>
</ul>

<h2>Carton format and pallet efficiency</h2>
<p>Carton dimensions determine how many cartons fit on a standard pallet, and this is where packaging cost
becomes visible. A carton that does not fit the pallet footprint wastes a significant proportion of the
freight bill on air, and in a low-value, high-volume material like ribbon the freight can be a substantial
share of the landed cost.</p>

<p>The relevant variables are the outer carton dimensions, the pallet type and the resulting carton count per
pallet, and the allowable stack height. The most common mistake is allowing the carton size to be driven
purely by the roll size without checking the resulting palletisation, and then discovering at shipping that the
cartons have to be loaded with gaps.</p>

<p>A packaging specification that works well covers: outer carton dimensions and board grade; gross weight
limit; net ribbon weight per carton and the roll count it contains; roll length and core size; winding
direction and rotation; roll orientation within the carton; barrier protection; separators; and the pallet
configuration with the resulting carton count.</p>

<h2>The packaging specification, in one table</h2>

<table>
  <tr><th>#</th><th>Element</th><th>What to state</th></tr>
  <tr><td>1</td><td>Roll length</td>
      <td>Metres per roll, stated per programme type, with the roll geometry and core size. Confirm whether the
      length is nominal or includes a lead-in.</td></tr>
  <tr><td>2</td><td>Roll weight tolerance</td>
      <td>Net weight per roll at a stated roll length, with tolerance, measured net of core, under stated
      conditioning.</td></tr>
  <tr><td>3</td><td>Winding direction</td>
      <td>Direction of winding, face-out or face-in, permitted winder rotation direction, and position of the free
      end.</td></tr>
  <tr><td>4</td><td>Core</td>
      <td>Core size, material and, where the converter requires it, the rotation direction marking.</td></tr>
  <tr><td>5</td><td>Barrier protection</td>
      <td>Roll-level wrapping, carton-level wrapping, desiccant type and quantity, and the required seal.</td></tr>
  <tr><td>6</td><td>Carton format</td>
      <td>Outer dimensions, board grade, gross weight limit, roll count, separators, and stack limit.</td></tr>
  <tr><td>7</td><td>Pallet configuration</td>
      <td>Pallet type, carton count per pallet, maximum gross weight and allowable stack height.</td></tr>
  <tr><td>8</td><td>Marking</td>
      <td>Roll identification, lot number, colour code, production date, winding direction arrow, and a
      standard carton label format the receiving warehouse can scan.</td></tr>
</table>

<h2>Incoming inspection: the packaging checks that catch real problems</h2>
<p>Most incoming inspections check width, colour and length. Three packaging-related checks catch problems that
matter more than their effort suggests:</p>
<ol>
  <li><strong>Open a roll from the bottom of the carton, not the top.</strong> The rolls at the bottom carry the
  stacking load and are where compression set appears. A roll taken from the top of a carton is the best
  condition the shipment contains.</li>
  <li><strong>Check the winding direction and rotation against the specification.</strong> It takes ten seconds
  and it prevents the recurring line-stoppage problem that is otherwise diagnosed as operator error.</li>
  <li><strong>Check for compression set</strong> by cutting a short length from the roll, letting it relax for a
  fixed period, and confirming it lies flat and the edges meet when folded. A ribbon that springs back into a
  curve will not fold symmetrically in the customer's process.</li>
</ol>

<p>And one record-keeping discipline that pays for itself: <strong>retain a length from the carton for the life of
the programme.</strong> When a complaint arrives three months after a shipment, the retained length from that
lot is the only evidence that separates a material problem from a packaging problem, a storage problem or a
handling problem. Without it, every complaint is settled by assumption, and the default assumption is usually
that the mill is at fault.</p>

<h2>Working with the mill</h2>
<p>Packaging is frequently the part of a ribbon programme that gets specified last and revised most often, usually
after a packaging-related failure that was misdiagnosed as a quality problem. It is also the part where the
buyer has the most leverage, because most of it is free to change - no new machinery is required, only a
different specification.</p>

<p>Smith Ribbon has manufactured ribbon and bows since 2004, running weaving, dyeing, finishing, slitting,
winding and bow assembly in Xiamen. We will quote the roll format, winding direction, carton configuration and
palletisation for your programme, and we will tell you where the packaging cost is concentrated so you can
decide where spending is worthwhile. If you are currently receiving ribbon that arrives with a compression set
or a colour shift across the roll, send us the carton specification and we will tell you honestly what we would
change and what we would leave alone.</p>
""",
    "faq": [
        ("What roll length should I specify for ribbon?",
         "It depends on your conversion rate and your material, and there is no single correct number. The "
         "commercial case for longer rolls is fewer changeovers: a 1,000-metre roll of 20 mm ribbon on a 76 mm "
         "core replaces roughly five 200-metre rolls, saving restocking, splicing, trimming and re-threading "
         "time on every run. The counterweight is core deflection and set, which becomes more pronounced on long "
         "rolls and is worst on soft constructions such as satin and velvet, plus the handling weight of a full "
         "carton. A sensible rule is to specify development rolls short, production rolls at a length that "
         "balances changeover cost against deflection, and to negotiate a dedicated winding plan with the mill "
         "for very high-volume programmes."),
        ("Which way should ribbon be wound on the roll?",
         "The correct answer is the way your converting line expects, and it should be written into the purchase "
         "order rather than assumed. Most converting - cutting, folding into bows, over-sewing, edge binding - "
         "unwinds with the face side out on a winder rotating in a defined direction. If the mill winds the "
         "opposite way, the ribbon feeds inside out, the line has to be reversed at every roll change, or rolls "
         "have to be flipped and re-spooled manually. The specification should state the winding direction, the "
         "face-out or face-in orientation, the permitted winder rotation direction, and the position of the free "
         "end. Experienced buyers also ask for a printed arrow or coloured tape mark at the roll start."),
        ("Why does the weight tolerance of a ribbon roll matter more than the length tolerance?",
         "Because most converting lines feed ribbon by weight rather than by metre. A control loop set up for "
         "weight compensates automatically for the difference between 0.06 and 0.07 grams per metre; it cannot "
         "compensate for a roll that is fifteen percent short, which simply means more roll changes. Weight also "
         "drives freight and customs calculations, so a wide tolerance makes the landed cost estimate unreliable "
         "and the invoice hard to reconcile. State the weight tolerance at a stated roll length, measured net of "
         "core, under stated conditioning, and always give it alongside the width and construction, because a "
         "weight figure means nothing without them."),
        ("How does packaging cause colour shift in ribbon?",
         "Polyester is hygroscopic to a modest but commercially significant degree, and absorbed moisture changes "
         "the refractive behaviour of the fibre and therefore the perceived colour. The effect is strongest at the "
         "surface of a roll that has spent time in a humid environment, so the outer wrap can read differently "
         "from the material beneath it. For a brand with a tight colour tolerance this produces the confusing "
         "result that the approved swatch matches the outside of the roll and the middle of the roll appears off. "
         "Roll-level barrier wrapping rather than carton-level wrapping is what actually addresses it, since "
         "carton wrapping leaves the inner rolls exposed to the humidity that develops inside a closed carton."),
        ("What causes compression set in ribbon rolls?",
         "Stacking load. The weight of the cartons above compresses the rolls beneath them, and the effect reaches "
         "the outer ribbon layers first, producing a permanent set that shows up as a ribbon that will not lie "
         "flat or whose edges will not meet when folded. It is nearly invisible on a roll from the top of a carton "
         "and severe on a roll from the bottom, which is why it so often emerges as a customer complaint weeks "
         "after the ribbon was approved. The controls are a gross weight limit per carton, appropriate board "
         "grade, separator sheets between vertically stacked rolls, and a stated stacking limit on the carton."),
        ("How much does ribbon packaging cost, and is it worth optimising?",
         "More than most buyers expect, because packaging is a significant proportion of the cost of a low-value, "
         "high-volume material, and it also drives freight: a carton that does not fit the pallet footprint wastes "
         "a meaningful share of the freight bill on air. Most of the optimisation is free, because it requires no "
         "new machinery, only a different specification. The highest-value changes are usually roll-level barrier "
         "wrapping where colour consistency matters, and carton dimensions chosen for pallet efficiency rather "
         "than for roll size alone. Ask the mill where the packaging cost is concentrated before deciding where "
         "spending is worthwhile."),
        ("What should we check at incoming goods inspection on packaging?",
         "Three checks catch more real problems than their effort suggests. Open a roll from the bottom of the "
         "carton rather than the top, because the bottom rolls carry the stacking load and are where compression "
         "set appears. Check the winding direction and rotation against the specification, which takes ten seconds "
         "and prevents the recurring line-stoppage problem that is otherwise blamed on the operator. And check for "
         "compression set by cutting a short length, letting it relax for a fixed period, and confirming it lies "
         "flat and folds with the edges meeting. Separately, retain a length from each lot for the life of the "
         "programme, because it is the only evidence that separates a material problem from a packaging, storage "
         "or handling problem when a complaint arrives months later."),
        ("Does changing the packaging affect the ribbon itself?",
         "It can, and this is why packaging changes should be treated as a specification change rather than a "
         "logistics detail. Individual roll wrapping combined with desiccant protects against moisture, but an "
         "over-aggressive drying regime can leave ribbon brittle and can change its behaviour on a hot, dry shop "
         "floor. A change in roll length changes the core deflection profile and can change the dimensional "
         "behaviour of the inner versus outer layers, particularly on soft constructions. A change of winding "
         "direction will not alter the material, but it can change how the ribbon is handled, and therefore how it "
         "is fed and converted. Put packaging changes through the same change-control route as any other change "
         "that touches the product specification."),
    ],
    "cta_title": "Let us quote your roll format and carton configuration",
    "cta_body": ("Tell us your programme volume, conversion method and current roll format. We will quote the "
                 "roll length, winding direction, carton configuration and palletisation, and tell you where the "
                 "packaging cost is actually concentrated."),
    "cta_link_text": "Request a packaging quote",
}

# ============================================================================
# WRITE
# ============================================================================

if __name__ == "__main__":
    for art in (A284, A285):
        fname = write_article(
            art["fname"], art["slug"], art["title"], art["desc"], art["keywords"],
            art["pub_iso"], art["wordcount"], art["section"], art["cat_label"],
            art["lede"], art["body"], art["faq"], art["cta_title"], art["cta_body"],
            art["cta_link_text"],
        )
        p = ROOT / fname
        import re as _re
        words = len(_re.sub(r"<[^>]+>", " ", p.read_text(encoding="utf-8")).split())
        print(f"[BUILT] {fname}  words={words}")
