#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon articles 298 (AM) + 299 (PM) - 2026-11-02.

298 AM: Quote-to-shelf costing for brand buyers - reading a ribbon quote properly,
         the cost waterfall to a per-unit landed cost, margin model for private-label
         programmes, and where quotes hide cost.
299 PM: Supplier quality agreement - governance, defect taxonomy, CAPA, and the
         audit/escalation cadence that keeps a ribbon programme on spec.

Uses smithribbon_article_lib.py for head/JSON-LD/FAQ scaffolding.
"""
from pathlib import Path
import importlib.util, sys

LIB = "/workspace/smithribbon-web/smithribbon_article_lib.py"
spec = importlib.util.spec_from_file_location("srl", LIB)
srl = importlib.util.module_from_spec(spec)
sys.modules["srl"] = srl
spec.loader.exec_module(srl)

ROOT = Path("/workspace/smithribbon-web")

# ============================================================================
# ARTICLE 298 (AM) - Quote-to-shelf costing / margin model
# ============================================================================

A298 = {
    "fname": ("blog-ribbon-oem-298-module-brand-buyer-ribbon-quote-reading-cost-waterfall-landed-cost-"
              "per-unit-margin-model-private-label-programme-pricing-structure-2026-11-02-am.html"),
    "slug": ("blog-ribbon-oem-298-module-brand-buyer-ribbon-quote-reading-cost-waterfall-landed-cost-"
             "per-unit-margin-model-private-label-programme-pricing-structure-2026-11-02-am"),
    "title": ("How to Read a Ribbon Quote &mdash; Cost Waterfall, Landed Cost per Unit and the Margin "
              "Model Behind a Private-Label Programme 2026"),
    "desc": ("A brand-buyer guide to ribbon OEM quotes: reading the cost waterfall, converting per-metre "
             "pricing into landed cost per finished unit, building a margin model for private-label programmes, "
             "and finding where cost is hidden in a quote."),
    "keywords": [
        "ribbon OEM quote explained", "ribbon pricing per metre vs per roll", "ribbon cost waterfall breakdown",
        "landed cost per unit ribbon trim", "private label ribbon margin model", "ribbon quote comparison guide",
        "ribbon bulk pricing tiers", "ribbon tooling cost amortisation", "ribbon freight cost per unit",
        "packaging ribbon cost calculation", "ribbon OEM price negotiation breakdown", "ribbon quote MOQ effect",
        "brand buyer ribbon costing model", "ribbon hidden cost in quotes", "custom ribbon price per metre",
        "ribbon unit economics private label", "ribbon procurement cost model 2026", "ribbon supplier quote audit",
    ],
    "pub_iso": "2026-11-02T02:00:00+00:00",
    "wordcount": 2900,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Quoting, Costing &amp; Margin Modelling for Brand Buyers",
    "lede": ("A ribbon quote arrives as a single number and is almost never a single number. The unit price "
             "on the quotation is the last figure in a chain that begins with substrate and fibre, runs "
             "through construction, colour, printing, finishing, packing, freight, duty and inventory "
             "carrying cost, and ends at a finished component that has to sit inside a margin your commercial "
             "team has already committed to. Buyers who compare quotes at the unit price alone are comparing "
             "the parts of the cost that are easiest to see, and they are systematically mis-ranking "
             "suppliers. This guide is about opening the quote up and understanding what is actually inside it."),
    "body": """
<h2>Why the number on the quotation is not the number you will pay</h2>
<p>Nearly every ribbon quote is presented as a price per metre for a defined width, substrate, colour,
print, finish and order quantity. It looks precise. It is also the narrowest possible slice of the total
cost of the component, and the slice that most often differs least between competing mills. Two mills can
quote the same woven polyester grosgrain at a per-metre price within a few percent of each other and still
produce finished components whose landed costs differ by thirty percent or more.</p>

<p>The reason is that the per-metre price covers the operations that happen on the ribbon mill's own equipment.
Everything that happens after the ribbon leaves the mill - the die-cutting, the bow assembly, the folding,
the bundling into retail packs, the carton, the freight, the duty, the inspection, the financing of the
inventory sitting in a port - happens either at a subcontractor or on the buyer's side of the ledger, and
none of it appears in the quoted price per metre.</p>

<p>The practical consequence is a rule that should govern every comparison you make: <strong>compare
suppliers on the cost of the delivered, ready-to-use component, not on the price of the ribbon.</strong> To
do that you need the quote decomposed. That means asking the supplier to state, separately, what is in the
per-metre price and what sits outside it.</p>

<h2>The ribbon cost waterfall: eight layers between the fibre and the shelf</h2>
<p>Working from the mill outward, a decorative ribbon programme carries cost at eight distinct layers. A
credible quote makes each of them visible.</p>

<table>
  <tr><th>#</th><th>Cost layer</th><th>What drives it</th><th>Questions to ask</th></tr>
  <tr><td>1</td><td>Raw fibre and yarn</td><td>Polyester chip price, recycled content premium, yarn cost by
      denier, RPET availability</td><td>Is the price indexed to a published fibre benchmark, and over what
      period?</td></tr>
  <tr><td>2</td><td>Construction</td><td>Woven vs jacquard vs knitted; picks per inch; yarn count; whether
      the base fabric is stocked or made to order</td><td>Is the base construction a stock item you are
      buying from, or something woven for you?</td></tr>
  <tr><td>3</td><td>Dyeing and colour</td><td>Yarn-dyed vs piece-dyed vs greige; number of dye lots; lab-dip
      and strike-off approvals; custom Pantone matching</td><td>Is the Pantone match a standard shade in the
      dyehouse or a one-off recipe requiring its own lab dip?</td></tr>
  <tr><td>4</td><td>Printing</td><td>Number of colours, repeat length, print method, screen or plate cost,
      setup</td><td>What is the screen charge, and is it per colour, per design, or per order?</td></tr>
  <tr><td>5</td><td>Finishing</td><td>Edge treatments, hemming, tipping, heat-sealing, coating, backing,
      metallisation, calendering</td><td>Are any of these applied in-house, and which are subcontracted?</td></tr>
  <tr><td>6</td><td>Converting</td><td>Slitting to width, die-cutting, folding, bow assembly, piece
      assembly, banding, retail packaging</td><td>Which steps happen at your mill and which go to a
      subcontractor, and what does each cost?</td></tr>
  <tr><td>7</td><td>Logistics and duty</td><td>Carton configuration, roll length, container utilisation,
      freight, insurance, duty and any trade remedy</td><td>What is the roll length, and what is the
      resulting number of cartons and container fit?</td></tr>
  <tr><td>8</td><td>Inventory and finance</td><td>Lead time, safety stock, write-off risk, obsolescence,
      payment terms, FX exposure</td><td>What is the quoted lead time, and does it include the approval
      cycle or only production?</td></tr>
</table>

<p>Most quote disputes come from a difference in layer six or seven, not in layer one. Two suppliers quoting
the same woven and printed ribbon at the same per-metre price can produce finished components at very
different landed costs purely because one packs on a longer roll and fills a container properly, and the other
ships short rolls that waste freight space and require more cartons to move the same volume.</p>

<h2>Converting per-metre pricing into a landed cost per finished unit</h2>
<p>Most ribbon programmes do not end in ribbon. They end in a bow, a cut length, a tie, a folded band, a
rosette or a bundled pack. The per-metre price is therefore not the unit cost of anything that actually
reaches your warehouse, and the arithmetic from one to the other is where margin quietly disappears.</p>

<p>The calculation is straightforward once the structure is understood. For a die-cut bow from printed
grosgrain:</p>

<p><strong>Metres consumed per bow</strong> = (bow loop length &times; 2 + tail length &times; 2 + knot
allowance) &divide; 1, with the width of the ribbon fixed by the bow specification. The knot allowance is
the part people forget. A bow that consumes 0.42 m and a bow that consumes 0.50 m differ by nineteen percent
in material cost, and the extra eight centimetres is usually the tail allowance, the knot wrap and the
cut-and-sew waste that gets trimmed off and thrown away.</p>

<p><strong>Material cost per bow</strong> = metres consumed &times; per-metre price &times; (1 + trim
waste factor). The trim factor for a die-cut bow is commonly ten to twenty-five percent and should be a
number you have measured on your own line rather than one you accept from a supplier.</p>

<p><strong>Conversion cost per bow</strong> = cutting and assembly labour plus the amortised cost of the
tooling, plus the cost of the wire, elastic, adhesive, backing or card that the bow is built on.</p>

<p><strong>Finished cost per bow</strong> = material + conversion + packaging, before freight.</p>

<p>Then, and only then, the landed cost:</p>

<p><strong>Landed cost per bow</strong> = finished cost &divide; (1 &minus; defect and reject rate) &plus;
freight per unit &plus; duty per unit &plus; inspection cost per unit &plus; inventory carrying cost per
unit, where carrying cost is the financing cost of the inventory over its dwell time in the pipeline.</p>

<p>Two of those terms deserve attention because buyers frequently omit them. The first is the reject rate.
A programme running at ninety-five percent first-pass yield does not have a five percent cost increase - it
has a five percent cost increase plus the material consumed by the rejects, which is already inside the
consumption figure, plus the freight on a scrapped unit, plus the schedule disruption. The second is
inventory carrying cost. Ribbon ordered eleven months ahead of a seasonal peak is carried for a long time, and
at a meaningful cost of capital, that is a real component price that belongs in the model.</p>

<h2>The margin model: where ribbon programmes actually lose money</h2>
<p>Private-label programmes are usually modelled on gross margin at the retail level, with the trim cost
treated as a percentage of retail price. That model is adequate for a first cut and dangerous for anything
beyond it, because ribbon programmes have a distinctive property: <strong>the trim cost per unit is
independent of the retail price, but it is not independent of the order quantity.</strong></p>

<p>This creates a specific and common failure. A buyer launches with a low-volume first order to test
demand. The unit economics at that volume are poor, because the tooling, the dye recipe, the print screens
and the setup are spread across a small number of units. The retail margin looks acceptable because the
retail price was set high enough to cover it. As volume grows, the buyer expects the margin to improve. It
does not, because the price was negotiated down faster than the fixed costs amortised away, and the
landed-cost structure was never re-examined once the volume arrived.</p>

<p>The model that works has three layers, and it is worth building it explicitly before the first purchase
order rather than reconstructing it during a quarterly review.</p>

<table>
  <tr><th>Layer</th><th>What it captures</th><th>What it tells you</th></tr>
  <tr><td>Variable cost</td><td>Material at per-metre price, converted and variable labour, variable packaging,
      unit freight and duty</td><td>The floor below which the programme cannot be profitable at any volume</td></tr>
  <tr><td>Allocated fixed cost</td><td>Tooling, dye lab dips, screen charges, setup, artwork and
      pre-press amortised over the planned run</td><td>The volume at which the programme reaches its target
      margin, and the break-even volume</td></tr>
  <tr><td>Programme cost</td><td>Inventory carrying cost, quality and inspection, obsolescence provision,
      freight variance, administrative cost of managing the SKU</td><td>The true cost of the programme, which
      is what should inform whether to expand, hold or exit it</td></tr>
</table>

<p>With those three layers, the questions become answerable. What volume does this programme need to reach
its target gross margin? At the current forecast, does it get there? If not, is the answer more volume, a
different construction, a different print method, or a different retail price - and in what order should
you try them? The order matters. Changing the substrate is usually the largest lever, changing the print
method is usually cheaper and faster, and changing retail price is usually last because it affects the
whole channel plan.</p>

<h2>Eight things that hide inside a ribbon quote</h2>
<p>These are the recurring omissions, in rough order of how much money they usually cost.</p>

<ol>
  <li><strong>The dye recipe fee.</strong> A custom Pantone that is not already in the dyehouse requires a
  lab dip, a strike-off and a recipe that has to be maintained for the life of the programme. Some mills
  quote it separately, some bury it, and some charge it only when you reorder and it has to be rematched.</li>

  <li><strong>Screen and plate charges.</strong> Per colour, per design, or per order. A programme that reprints
  the same design in three colourways can face three separate screen charges, and the buyer who assumed one
  setup cost will find it in the invoice.</li>

  <li><strong>Tooling and its amortisation.</strong> Bow dies, folding jigs, cutting blades, and the fact
  that a die has a finite life and is amortised across a quantity the mill chooses. Ask what the life
  assumption is.</li>

  <li><strong>Short-run and repeat-order price steps.</strong> The first order is priced at one rate and the
  repeat at another. The step should be stated, along with the quantity at which it applies.</li>

  <li><strong>Packaging that is not in the scope.</strong> Retailing a ribbon product requires a header card,
  a poly bag, a barcode label, a carton and a pallet. If the quote covers "the ribbon", none of that is
  included.</li>

  <li><strong>Freight on a suboptimal roll length.</strong> Longer rolls reduce freight per metre, but they
  also raise the risk of damage in transit and increase the inventory commitment per SKU. There is an
  optimum, and it is not the longest possible roll.</li>

  <li><strong>Inspection and AQL sampling.</strong> Pre-shipment inspection by a third party is a real cost
  that is frequently omitted from the quote and discovered on the freight invoice.</li>

  <li><strong>The cost of changing something later.</strong> Artwork revisions, colour corrections, changed
  quantities, split deliveries. Ask what the change charges are before you need them, because they are set
  against a deadline you will not control.</li>
</ol>

<h2>Building a quote comparison that actually decides the award</h2>
<p>A comparison sheet should have one column per supplier and one row per cost layer, with a final row that
shows landed cost per finished unit and a further row that shows landed cost per unit at the actual planned
volume rather than the quoted volume. Ask every supplier to fill the same template, and require the
per-metre price to be broken into its components. A mill that will not decompose its quote is telling you
something about how the relationship will go.</p>

<p>Then apply the judgement that the spreadsheet cannot. The lowest landed cost is not always the best
supplier, and the difference between first and second place is often smaller than the uncertainty in the
numbers. Weight the other things you would have to live with: whether the mill holds the construction you
need in stock or weaves it for you, whether your colour is a standard shade or a custom recipe, how they
handled the first sample, whether they will hold capacity in peak season, and whether their communication
during the quote process was precise. A quote that arrives with every number specified is itself evidence
about the supplier, and for a long-term programme that evidence is worth more than the last two percent of
price.</p>

<h2>What a good quote conversation looks like</h2>
<p>The most productive single request you can make is to ask a mill to quote the same specification twice -
once as the standard construction and once with the changes you would consider if the price were different -
and to explain what is driving the difference. A mill that can do that is telling you where the engineering
headroom is. A mill that can only repeat the same number is telling you the price is a price and not a
relationship.</p>

<p>Equally useful is asking for the quote with the quantity bands made explicit, and then asking what
specifically has to change for the programme to reach the next band. The answer is usually not volume - it
is usually a longer print run, a stock construction, a standard shade, a simpler finish or a different
pack format. Each of those is a lever you can pull without renegotiating the unit price, and finding them is
what turns a buyer from a price-taker into a partner.</p>

<p>Finally, get everything in writing at quotation stage, including the lead time definition, the payment
terms, the packaging scope, the freight basis and the Incoterm. A quote that is clear on all of these is a
quote you can turn into a purchase order without a meeting. A quote that is not, is going to generate a
dispute at the worst possible moment, and you will not win that argument later because the ambiguity was
resolved in your favour in the moment.</p>
""",
    "faq": [
        ("Why do two ribbon quotes for the same specification differ so much once converted to landed cost?",
         "Because the per-metre price usually covers only the operations performed on the mill's own equipment. "
         "Differences in die-cutting, bow assembly, roll length, carton configuration, container utilisation, "
         "packaging scope and third-party inspection can move landed cost by thirty percent or more between "
         "suppliers quoting the same per-metre price. This is why the comparison has to be made at the "
         "delivered finished-unit level."),
        ("Should I compare suppliers on price per metre or per kilogram?",
         "Neither, on its own. Per metre only makes sense once width is fixed, and per kilogram hides the "
         "construction differences that determine performance. The correct comparison unit for most programmes "
         "is landed cost per finished unit at your actual planned volume, with the construction and quality "
         "specification held constant across every supplier you quote."),
        ("What is the trim waste factor for a die-cut ribbon bow, and how do I measure it?",
         "It is typically ten to twenty-five percent of ribbon consumed, depending on how the bow is cut and "
         "how tight the material allowance is. You should measure it on your own line rather than accept a "
         "supplier's figure: weigh the finished bow, weigh the total ribbon issued to produce a batch, and "
         "compare. The difference is your waste factor, and it is one of the largest single levers on the "
         "material cost of a bow programme."),
        ("How should tooling costs be treated in the margin model?",
         "Amortise them over the planned production run at the point the programme is launched, not over the "
         "first order. Tooling - bow dies, folding jigs, cutting blades - has a finite life and a stated "
         "assumption about that life, and both should be confirmed with the mill in writing. If the mill "
         "amortises across a shorter run than you have planned, ask them to restate the amortisation against "
         "your volume before you accept the figure."),
        ("Why did our unit cost fall when volume rose but our margin did not?",
         "Almost always because the retail price was negotiated down faster than the fixed costs amortised "
         "away, or because the original quote's scope was narrower than the programme's actual scope and the "
         "difference only surfaced at higher volumes. The fix is to rebuild the three-layer model - variable "
         "cost, allocated fixed cost and programme cost - at the new volume, and then decide deliberately "
         "which lever to pull: substrate, print method, finish, packaging, quantity or retail price."),
        ("What does a supplier's willingness to break down a quote tell me about them as a partner?",
         "A great deal. A mill that will decompose its pricing into construction, dyeing, printing, finishing, "
         "converting and packaging is demonstrating that it understands your cost model and can work with it. "
         "A mill that only provides a single per-metre number is either not structured to discuss engineering "
         "trade-offs, or does not want them discussed. For a multi-year programme that distinction matters "
         "well beyond the initial award."),
        ("How do I handle a quote that excludes packaging, inspection and freight?",
         "Ask for a second version of the same quote that explicitly lists the excluded scope and prices it "
         "separately. This is a routine request and a mill that refuses it is telling you the exclusion is "
         "material. Record the exclusions in your purchase order so they are not billed later as unexpected "
         "charges, and price packaging and inspection into your margin model from the start."),
        ("Should I negotiate on unit price or on payment terms when the difference is small?",
         "If the unit price difference is genuinely marginal, payment terms are usually the better lever. "
         "Extended terms reduce your working capital exposure on the same programme without asking the mill "
         "to concede margin, and they are easier to agree because they cost the mill less than a price cut. "
         "The same reasoning applies to a split delivery schedule, a rolling forecast, or payment against "
         "accepted goods rather than against shipped goods."),
    ],
    "cta_title": "Send us your current ribbon quote and specification",
    "cta_body": ("Tell us what you are buying, the width, the construction, the print, the finish and the "
                 "quantity, and we will return a quote broken down by cost layer with a landed cost per "
                 "finished unit at your volume - so you can compare it properly against the quotes you already "
                 "hold. We will also flag the line items that are commonly omitted, because that is usually "
                 "where the real difference between quotes sits."),
    "cta_link_text": "Request a decomposed quote",
}

# ============================================================================
# ARTICLE 299 (PM) - Supplier quality agreement governance
# ============================================================================

A299 = {
    "fname": ("blog-ribbon-oem-299-module-brand-buyer-ribbon-supplier-quality-agreement-governance-defect-"
              "taxonomy-aql-continuity-conformance-capa-corrective-action-audit-cadence-2026-11-02-pm.html"),
    "slug": ("blog-ribbon-oem-299-module-brand-buyer-ribbon-supplier-quality-agreement-governance-defect-"
             "taxonomy-aql-continuity-conformance-capa-corrective-action-audit-cadence-2026-11-02-pm"),
    "title": ("The Ribbon Supplier Quality Agreement &mdash; Defect Taxonomy, Conformance Levels, CAPA "
              "Governance and the Audit Cadence That Holds a Programme to Spec 2026"),
    "desc": ("A brand-buyer framework for ribbon supplier quality: quality agreement terms, a workable defect "
             "taxonomy, AQL continuity rules, corrective and preventive action governance, and the audit "
             "cadence that keeps a private-label programme on specification."),
    "keywords": [
        "ribbon quality agreement template", "ribbon supplier quality management", "ribbon defect taxonomy AQL",
        "ribbon CAPA procedure supplier", "ribbon pre-shipment inspection AQL", "ribbon quality audit cadence",
        "ribbon supplier corrective action plan", "ribbon incoming inspection criteria", "ribbon quality agreement clause",
        "ribbon golden sample standard", "ribbon PPM defect tracking brand buyer", "ribbon quality continuity rules",
        "ribbon supplier audit checklist", "private label ribbon quality assurance", "ribbon eight defect report",
        "ribbon quality agreement negotiation", "ribbon supplier performance scorecard", "ribbon lot traceability quality",
    ],
    "pub_iso": "2026-11-02T07:00:00+00:00",
    "wordcount": 2850,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Quality Agreement &amp; Supplier Governance for Brand Buyers",
    "lede": ("Most ribbon quality disputes are not caused by a bad mill. They are caused by the absence of a "
             "shared definition. The mill believes a shade variation within an agreed tolerance is acceptable; "
             "the brand believes it is not. The mill believes a frayed selvedge within a length allowance is "
             "acceptable; the retailer's inspector disagrees. Nobody lied, and everybody was right, because "
             "the tolerance was never written down. A quality agreement is simply the document that closes "
             "that gap before it costs you a season."),
    "body": """
<h2>What a quality agreement is for, and what it is not</h2>
<p>A quality agreement between a brand buyer and a ribbon supplier is not a contract about quality in the
abstract. It is a shared technical specification of what the ribbon must be, written in language precise
enough that two people in different departments in different countries would measure the same ribbon and
reach the same conclusion.</p>

<p>It is also not a warranty, and it is not a substitute for the purchase order. The purchase order governs
the commercial transaction. The quality agreement governs the technical standard. Keeping them separate is
best practice, because quality terms change far more often than commercial terms - typically because a
substrate changes, a new colour is added, a defect rate is renegotiated after a difficult quarter, or a
compliance requirement is added to a material.</p>

<p>Written properly, a quality agreement covers five things: what is being specified, how conformance is
measured, what happens when conformance fails, how the parties communicate about it, and how the agreement
itself is kept current. Brands that skip the fifth item end up with a document that describes a programme
that has since been redesigned, which is worse than having no document because it creates false confidence.</p>

<h2>The specification section: everything that defines the article</h2>
<p>The opening section should be specific enough that a supplier can price it and a quality engineer can
inspect it without asking a question. For decorative ribbon, that means at minimum the following, and the
list is worth using as a checklist because it corresponds to the points where ambiguity actually occurs in
day-to-day trading.</p>

<table>
  <tr><th>Element</th><th>What to state</th><th>Why it matters</th></tr>
  <tr><td>Construction and substrate</td><td>Fibre type, weave, width and width tolerance, picks per inch
      or yarn count, weight per metre</td><td>Defines drape and hand feel, and is the root cause of most
      performance complaints</td></tr>
  <tr><td>Colour</td><td>Reference standard, tolerance method and value, whether shade matching is by
      visual assessment or instrument</td><td>The single largest source of disputes</td></tr>
  <tr><td>Print</td><td>Artwork reference, repeat length and tolerance, registration tolerance, colour
      count, method, and who owns the printing plates</td><td>Registration drift and repeat length error
      accumulate across a roll</td></tr>
  <tr><td>Edge and selvage</td><td>Edge treatment, permissible fray, and selvedge condition</td><td>Determines
      whether the ribbon can be cut without unravelling</td></tr>
  <tr><td>Physical performance</td><td>Tensile, abrasion, crocking, lightfastness, shrinkage, where these
      matter for the end use</td><td>Turns a marketing expectation into a testable claim</td></tr>
  <tr><td>Converting</td><td>Cut length tolerance, bow dimensions and symmetry, knot and loop consistency,
      piece counts per pack</td><td>Where most retail-facing defects actually appear</td></tr>
  <tr><td>Packing</td><td>Roll length, core, winding direction, carton configuration, labelling, barcode</td><td>
      Affects both shelf handling and inbound receipt</td></tr>
  <tr><td>Materials and compliance</td><td>Any restricted substance requirement, and the certification
      scope that covers it</td><td>Ensures the compliance obligation is attached to the article it covers</td></tr>
</table>

<p>Two drafting habits materially improve this section. First, state tolerances as a measurement method as
well as a number - "width +/- 1 mm measured at 1 m intervals on the roll" rather than simply "+/- 1 mm",
because the number alone is not reproducible. Second, where the article is subject to a standard test, cite
the standard by name and number rather than describing the test in your own words, so that the mill's
laboratory and your inspector run the same method.</p>

<h2>The defect taxonomy: name the defects before you argue about them</h2>
<p>Defect categories are the working vocabulary of the relationship. Most ribbon quality problems are not
novel - they are recurring, well-known failure modes. If both parties use the same word for the same defect,
discussions move faster and escalation becomes an exception rather than the normal state of affairs.</p>

<p>A workable ribbon defect taxonomy classifies by where the defect occurs in the value chain and whether
it is a critical, major or minor defect. In ribbon and trim terms the classification is roughly:</p>

<ul>
  <li><strong>Critical</strong> - affects safety, compliance or fitness for purpose. Restricted substance
  exceedance, wrong fibre content, incorrect certification scope for the article, contamination, foreign body
  in a food-contact or child-use application.</li>
  <li><strong>Major</strong> - affects function, appearance or the agreed specification in a way the
  customer will reject. Shade outside tolerance, print registration outside tolerance, wrong width, wrong
  length, bow loop or tail asymmetry beyond limit, selvage fraying that prevents use, insufficient
  tensile, crocking failure.</li>
  <li><strong>Minor</strong> - cosmetic, does not affect function or acceptance. Minor surface irregularity,
  a small print imperfection outside the repeat, slight waviness, individual loose threads within
  tolerance, minor packaging scuffing.</li>
</ul>

<p>The most valuable clause in a quality agreement is the one that ties the defect class to the action
taken. Critical defects should trigger immediate containment, notification within a defined window, and
a formal corrective action with a named owner and a date. Major defects should trigger segregation of the
affected lot, a defined response time, and a decision on rework, downgrade or return. Minor defects should
be counted and trended rather than stopped shipment by shipment, because treating a one-percent cosmetic
rate as an emergency trains both sides to expect escalation on trivial issues.</p>

<h2>Acceptance sampling and the continuity rule that prevents argument</h2>
<p>Inspection of ribbon is normally by attribute sampling against a defined acceptable quality level,
drawn from the agreed inspection standard. Two features of ribbon make the classic treatment awkward, and
both need explicit handling.</p>

<p>The first is that ribbon is a continuous web rather than discrete units. A defect may run for metres
along a roll, and the affected quantity is not one unit but the whole run. The quality agreement should
state how a continuous defect is quantified - whether a defect run is measured by length, by the roll it
appears on, or by the whole lot - and how the sample is drawn from a roll. Where a defect is a shade band or
a registration drift that develops gradually, an attribute sample taken at the roll head is not
representative at all, and the agreement should say that inspections for such defects are taken at
defined intervals along the length.</p>

<p>The second is continuity. The rule that prevents most disputes is a simple one: once a shipment has been
accepted at a given conformance level, that same standard applies to subsequent shipments of the same article
until the parties agree otherwise. Without it, a mill can pass a shipment at one AQL, fail the next at the
same AQL, and the buyer cannot establish that anything changed - because nothing did, except the inspection
intensity on the day.</p>

<p>Two complementary clauses are worth adding. A re-inspection right, so that a buyer who rejects a shipment
can require the mill to re-inspect it at the mill's own cost if the buyer suspects the original inspection
was not representative. And a defined position on the disposition of rejected material, so that the question
of who owns the rejected stock and what happens to it is answered before it arises rather than during it.</p>

<h2>Corrective and preventive action: the clause that separates a supplier from a partner</h2>
<p>A supplier that rejects a shipment and fixes the shipment is adequate. A supplier that rejects a shipment,
finds the root cause, changes the process so the cause cannot recur, and demonstrates that the change worked
is a partner. The difference is worth money, and it is worth writing down.</p>

<p>A workable CAPA clause has five components. First, a definition of what triggers a formal corrective
action - typically a critical defect, a repeated major defect within a defined window, or a rejection rate
above a threshold. Second, a response structure, specifying containment, root cause analysis, corrective
action, verification of effectiveness and closure, each with its own deadline. Third, the standard for root
cause analysis, which should require evidence rather than assertion - a repeated defect explained as operator
error without process change will recur, and the agreement should say that. Fourth, the right to verify,
meaning the buyer can request the records supporting the root cause and the effectiveness check. Fifth,
the deadline for prevention: a corrective action that fixes this lot but leaves the same cause in place is
not closed, it is deferred.</p>

<p>Two practical rules make this work. Set the containment deadline in hours, not days, because containment
protects the next shipment rather than the one that failed. And require that effectiveness verification be
measured over a defined number of subsequent shipments rather than asserted immediately - a change that is
announced and never seen again under load has not been demonstrated.</p>

<h2>The audit cadence: four layers, each answering a different question</h2>
<p>Quality cannot be verified by inspection alone, because inspection samples what has already been made.
The layers below it are what make quality predictable.</p>

<ol>
  <li><strong>Self-inspection at the mill</strong> - the mill's own inspection against the agreed criteria,
  before goods leave its gate. This is the layer that prevents most problems from ever reaching you, and it
  is also the layer most often assumed rather than specified. Ask what the mill's own release criteria are
  and how conformance is recorded.</li>

  <li><strong>Incoming inspection at receipt</strong> - your inspection of what arrives, against the same
  criteria. This layer is about detecting the mill's misses, and its sample design matters: sampling a
  continuous web at the roll head is not a substitute for the agreed plan.</li>

  <li><strong>Pre-shipment inspection</strong> - inspection at the mill before loading, which is the last
  point at which a shipment can still be held or reworked. This layer is where the most value sits, because
  a defect caught here costs a rework, while the same defect caught at your dock costs a shipment, a
  schedule and a claim.</li>

  <li><strong>Periodic process audit</strong> - an audit of the mill's process and system rather than of a
  shipment: how the colour is controlled, how print registration is maintained, how traceability is handled,
  how the mill verifies its own release criteria. This is the layer that detects a process drifting before it
  produces a defect, and it is the layer most often skipped because it requires a buyer to spend time on
  site.</li>
</ol>

<p>These four layers are not alternatives; they are a sequence, and each one that is skipped becomes an
expense borne further down. When a buyer skips the process audit, the mill's own inspection carries the
whole load. When a buyer skips pre-shipment inspection, the cost of discovery moves to their own dock and
the shipment has already been paid for and shipped.</p>

<h2>Traceability and record retention</h2>
<p>Ribbon is rarely the only thing in a finished product, but it frequently becomes the hardest thing to
identify when a problem surfaces. The clause that prevents this is a traceability requirement: the mill
must be able to identify, for any lot, the raw material and dye lot used, the production dates, the machine
and shift, the print plates and screens used, the finishing route, the inspection records and the shipment
reference. It must be able to produce that within a defined period of the request.</p>

<p>Record retention periods matter as much as the records themselves. The mill must hold the colour recipe,
the approved lab dip, the print registration master and the inspection results for a period that matches
your programme's life plus a margin - typically three years for the active programme - because the most
common trigger for a quality investigation is a consumer complaint on a product that was on shelf two years
ago. A mill that cannot reproduce a shade it supplied two years ago cannot answer that complaint, and the
commercial consequence falls on whoever cannot answer it.</p>

<h2>Measurement: scorecards that produce decisions rather than decoration</h2>
<p>At the heart of quality governance is a small number of measurements reviewed on a fixed cadence. The
measurements that actually change behaviour are few, and they should be chosen so that both parties can
influence them.</p>

<table>
  <tr><th>Measure</th><th>How it is calculated</th><th>What it drives</th></tr>
  <tr><td>Defect rate by class</td><td>Defects found at each inspection layer per unit or per metre
      inspected</td><td>Which layer is failing, and whether the mill's self-inspection is working</td></tr>
  <tr><td>First-pass yield</td><td>Shipments accepted without rework or concession, as a share of shipments
      received</td><td>The mill's process capability, and the case for process investment</td></tr>
  <tr><td>Repeat defect incidence</td><td>How often a previously identified defect category reappears</td>
     >CAPA effectiveness, and whether root causes are genuinely being closed</td></tr>
  <tr><td>Concession rate</td><td>Units accepted with a documented deviation, as a share of units
      received</td><td>The health of the specification - a rising rate means the spec no longer fits the
      process</td></tr>
  <tr><td>On-time delivery against spec</td><td>Shipments arriving on the committed date and conforming on
      receipt</td><td>Overall supplier performance, and the input to tier decisions</td></tr>
  <tr><td>Response time to claims</td><td>Time from buyer notification to a written containment response</td>
     >The relationship itself</td></tr>
</table>

<p>Two principles keep a scorecard useful. First, review it on a fixed cadence and with a defined audience, so
it becomes a decision rather than a report nobody acts on. Second, use it to allocate investment. A mill
with a high repeat-defect incidence in print registration needs plate maintenance and operator training, not
a lecture; a mill with a high incoming-inspection defect rate but a clean pre-shipment rate has a self-
inspection problem; a mill that is clean at every layer but concedes heavily may have a specification that
does not match what the process can reliably produce, which is a problem for the agreement rather than the
mill.</p>

<h2>Putting the agreement together in a workable order</h2>
<p>Negotiating a quality agreement is often treated as a confrontation, and it does not need to be. The
useful framing is that both parties want the same outcome and neither wants to spend the season's margin on
disputes about definitions. A workable drafting order runs: scope and definitions, the technical
specification, defect taxonomy and classification, inspection and sampling, acceptance and continuity,
correction and CAPA, record retention and traceability, governance and escalation, and finally review and
revision.</p>

<p>Two drafts carry most of the weight in practice. A technical specification annex that specifies the
article precisely enough to be measured, and a defect classification table that names the defects and ties
each class to an action. Get those two right and the rest of the agreement is comparatively straightforward,
because most of what feels difficult in negotiation is really an attempt to agree a definition that these
two documents will contain.</p>

<h2>Three failure patterns worth avoiding</h2>
<p><strong>Writing a quality agreement that is only an inspection standard.</strong> It describes how to
sample and what to reject on, but says nothing about process control, root cause or what happens after a
rejection. It therefore handles the last ten percent of problems and ignores the ninety percent that never
reached your dock.</p>

<p><strong>Treating the agreement as immutable.</strong> A programme that adds a colour, changes a substrate,
moves a converter or adds a compliance requirement will fall out of agreement if the document has no
revision mechanism. Include one: what constitutes a change, who authorises it, how it is communicated, and
a scheduled review date.</p>

<p><strong>Using the agreement as a weapon rather than a framework.</strong> Invoking a clause to extract a
discount on a shipment that is slightly off is not a governance model; it teaches the mill that the agreement
is a weapon, and the next negotiation will be conducted on those terms. The agreement works when both sides
use it to resolve things quickly, and that only holds if using it is never an act of aggression. Reserve the
escalation path for the cases where it should be used, and let the agreement handle the ordinary ones.</p>

<h2>The practical starting point</h2>
<p>You do not need a forty-page agreement to begin. For most ribbon programmes, a well-written technical
specification, a defect classification table with agreed actions, a sampling and continuity clause, a CAPA
procedure with deadlines and a review cadence will handle the overwhelming majority of what actually goes
wrong. Write those, get them signed, and then expand the document only as the programme earns the need - at
the point where you add a new substrate, a new converter or a new market's compliance requirement, which is
exactly when a well-structured agreement makes the change easy rather than contentious.</p>
""",
    "faq": [
        ("What is the difference between a quality agreement and a purchase order?",
         "A purchase order governs the commercial transaction - price, quantity, delivery and payment. A "
         "quality agreement governs the technical standard the article must meet, how conformance is measured, "
         "and what happens when it fails. Keeping them separate is best practice because quality terms change "
         "far more often than commercial terms. The purchase order should reference the quality agreement so "
         "the two are linked, but each should be version-controlled independently."),
        ("How do I define acceptable quality for a continuous web rather than discrete units?",
         "Specify the measurement method, not just the number, and address sampling position explicitly. For "
         "ribbon, state whether a defect run is quantified by length, by the roll it appears on, or by the "
         "whole lot, and require that inspections for gradual defects such as shade banding or registration "
         "drift are taken at defined intervals along the roll length rather than only at the roll head."),
        ("What does a continuity rule mean in a ribbon quality agreement?",
         "It means that once a shipment has been accepted against a given conformance level, the same standard "
         "applies to subsequent shipments of the same article until both parties agree otherwise. Without it, "
         "a supplier can pass one shipment and fail the next at the same AQL, and neither party can show that "
         "anything actually changed. The rule removes inspection-day variability from the argument."),
        ("What should a corrective and preventive action clause require?",
         "Five elements: what triggers a formal CAPA, a response structure with separate deadlines for "
         "containment, root cause analysis, corrective action, effectiveness verification and closure, a "
         "standard for root cause analysis that requires evidence rather than assertion, the buyer's right to "
         "verify the underlying records, and an explicit prevention step. A CAPA that fixes the affected lot "
         "but leaves the cause in place has not been closed."),
        ("How often should we audit a ribbon supplier, and what should the audit cover?",
         "Frequency should scale with programme volume and risk - a high-volume or compliance-sensitive "
         "programme warrants an on-site process audit at least annually, with additional audits triggered by "
         "repeat defects or specification changes. The audit should cover process and system rather than "
         "shipment: colour control methods, print registration maintenance, traceability, change control, "
         "calibration, and how the mill verifies its own internal release criteria before goods ship."),
        ("Should a supplier be allowed to ship with documented concessions?",
         "Yes, provided the concession mechanism is explicit and the volume is visible. A concession is a "
         "shipment accepted with a documented deviation, and it should require named authorisation on both "
         "sides, record of the affected quantity and reason, and a defined expiry for the concession itself. "
         "Track the concession rate as a metric - a rising rate usually means the specification has drifted "
         "away from what the process can reliably produce, which is a problem for the agreement rather than "
         "the mill."),
        ("What records must a ribbon mill retain, and for how long?",
         "The colour recipe and approved lab dip, the print registration master and any plate or screen "
         "references, inspection records by lot, non-conformance and CAPA records, and traceability linking "
         "raw material and dye lot to shipment. Retention should match the programme's life plus a margin, "
         "commonly three years from the last shipment. The practical driver is that consumer complaints "
         "arrive years after production, and a mill that cannot reproduce an old shade cannot answer them."),
        ("Our programme keeps shipping concessions and nobody escalates. How do we fix that?",
         "Treat the concession rate as a governance trigger rather than an accounting detail. If it is "
         "persistently above a threshold, that is evidence the specification no longer matches what the "
         "process can deliver reliably, and the corrective action is to revise the specification or invest in "
         "process capability - not to continue accepting deviations informally. Agree the threshold in the "
         "quality agreement and have the review meeting actually apply it."),
    ],
    "cta_title": "Let's put a quality agreement on your ribbon programme",
    "cta_body": ("Send us your current specification and a sample of the defects that keep costing you "
                 "time, and we will draft the defect taxonomy and the inspection and CAPA clauses against "
                 "your actual programme rather than a generic template. We will also tell you where our own "
                 "process does not meet the standard we would write - because a quality agreement is only "
                 "worth anything if both sides can meet it."),
    "cta_link_text": "Request a quality agreement draft",
}

# ============================================================================
# WRITE BOTH ARTICLES
# ============================================================================

for art in (A298, A299):
    fname = srl.write_article(
        fname=art["fname"], slug=art["slug"], title=art["title"], desc=art["desc"],
        keywords=art["keywords"], pub_iso=art["pub_iso"], wordcount=art["wordcount"],
        section=art["section"], cat_label=art["cat_label"], lede=art["lede"],
        body_html=art["body"], faq=art["faq"], cta_title=art["cta_title"],
        cta_body=art["cta_body"], cta_link_text=art["cta_link_text"])
    print("[OK] wrote", fname)
