#!/usr/bin/env python3
"""Build smithribbon B2B module 269 (AM), 2026-10-26.

Topic: mill-side RIBBON FOIL & METALLIC LAMINATION ADHESION / DELAMINATION
interlock — how a brand buyer controls the metallic (hot-stamp foil, vacuum
metallised film, laminated foil) surface applied to a woven ribbon: adhesive
system choice, foil-to-substrate adhesion strength, flex-crack and peel
resistance under repeated folding, abrasion over the foil, and the peel
behaviour that determines whether the metallic survives the product's life.

Distinct from every existing module: 256 covers PRINT ROUTE selection (yarn
print vs woven substrate print); 263 covers COLOURFASTNESS (crocking / rub /
wash / perspiration) of the dye; 264 covers the selvedge / cut edge; 268
covers the care label. None covers the metallic film layer as a bonded
composite — its adhesive chemistry, its peel-strength floor, its flex-crack
behaviour, or the fact that a foil that passes an initial peel test can still
delaminate after a season of folding.
"""
from pathlib import Path
import sys

sys.path.insert(0, "/workspace/smithribbon-web")
from sr_page import write_article

SLUG = ("blog-ribbon-oem-269-module-mill-side-brand-buyer-ribbon-metallic-foil-lamination-adhesion-"
        "delamination-interlock-architecture-hot-stamp-vacuum-metallised-film-adhesive-system-peel-"
        "strength-flex-crack-abrasion-2026-10-26-am")

a = {
    "title": "Mill-Side Brand-Buyer Ribbon Metallic Foil &amp; Lamination Adhesion / Delamination Interlock "
             "Architecture &mdash; Hot-Stamp, Vacuum-Metallised Film, Adhesive System Choice, Peel Strength, "
             "Flex-Crack and Abrasion Resistance 2026",
    "desc": "B2B ribbon OEM 269-module metallic foil and lamination adhesion/delamination interlock architecture. "
            "5-layer metallic-surface authority ladder, 4-stage foil approval gate, 3-tier delamination "
            "reconciliation ladder, and a flex-crack + peel-strength retention audit. Smith Ribbon OEM since 2004.",
    "kw": "metallic ribbon OEM, foil ribbon manufacturer, hot stamp foil adhesion test, ribbon lamination "
          "delamination, vacuum metallised film ribbon, peel strength adhesive ribbon, flex crack foil "
          "durability, glitter ribbon supplier, foil ribbon abrasion test, ribbon metallic finish, "
          "custom metallic ribbon China, holographic ribbon OEM, ribbon foil lamination process, "
          "brand buyer foil trim, ribbon print metallic finish, foil ribbon quality control, "
          "metallic ribbon packaging supplier, ribbon OEM decorative trim, foil ribbon 100d satin, "
          "metallic ribbon delamination causes",
    "author": "Xiamen Smith Ribbon &amp; Bow Co., Ltd.",
    "date_iso": "2026-10-26T02:00:00+00:00",
    "date_human": "October 26, 2026",
    "slug": SLUG,
    "section": "Ribbon OEM Manufacturing",
    "tag": "Ribbon OEM",
    "read": "17 min read",
    "word_count": 2750,
}

BODY = """
<p class="lede">The metallic ribbon is the trim that looks the most like a promise and behaves the most like a
liability. A roll of gold, silver or holographic foil ribbon leaves the mill looking magnificent. It arrives at the
brand looking magnificent. It reaches the customer having been folded four hundred times in a gift box, or pulled
through a bow loop, or washed in a hair accessory, and it has cracked along every one of those fold lines into a fine
silver dust that transfers to the customer's fingers. The failure is invisible at the point of inspection because the
foil is still there, still shiny, still perfectly conformed to the ribbon surface. It has simply lost its bond to
the substrate underneath, and it will shed that bond at the first repeated flex.</p>

<p>This is not a defect in the printing. It is a defect in the composite, and the distinction matters enormously
because the party who applies the foil is rarely the party that owns the specification. A brand buyer writes a
specification that says "metallic gold, 15 mm, 100% polyester satin base" and assumes that "metallic" is a colour
rather than a bonded film with its own chemistry, its own adhesion requirement, and its own failure mode. The
supplier chooses a foil, a hot-melt or acrylic adhesive, and an application temperature, because none of those were
in the specification. The result is a trim that passes an initial peel test on the day it is made and fails eight
months later in a retailer's fulfilment centre.</p>

<blockquote style="border-left:4px solid #b8854a;padding:8px 16px;margin:1.2em 0;background:#faf6f1;">
&quot;Metallic trim specification: 15&nbsp;mm 100&nbsp;% polyester satin, 100&nbsp;denier, foil-applied metallic
surface in antique gold, base film 12&nbsp;&micro;m aluminium on 12&nbsp;&micro;m PET carrier.
Hot-melt adhesive system, application temperature 150&ndash;170&nbsp;&deg;C, nip pressure 3&nbsp;bar.
Peel strength, 180&deg; adhesive tape peel at 180&deg;, minimum 8&nbsp;N/25&nbsp;mm on the finished
ribbon after 24&nbsp;h conditioning. Flex-crack retention: no visible cracking of the metallic layer after
1,000 cycles of 180&deg; flexing at 25&nbsp;mm radius. Abrasion: Martindale, minimum 500 rubs on the
metallic face with no metallic transfer to the abrading cloth. Delamination after 10 wash cycles at
40&nbsp;&deg;C: no edge lifting over 2&nbsp;mm.&quot;
</blockquote>

<p>That specification contains fourteen separate requirements, and it is worth noting which of them the market
normally omits. "Metallic gold" is nearly universal. The adhesive system is nearly universal as a concept and
almost never as a stated requirement. The peel-strength floor, the flex-crack cycle count, the abrasion transfer
criterion, and the post-wash delamination limit are the four requirements that separate a metallic trim that lasts
a season from one that is on a return list by February.</p>

<div class="kpi">
  <p><strong>Commercial significance:</strong> a delaminating metallic trim is not a cosmetic complaint. It is a
  photograph problem, because metallic dust on the inside of a gift box or a black retail display is a defect the
  customer sees before they see the product. It is a returns problem, because the complaint arrives as "the ribbon
  is shedding" and the retailer treats it as a defect on the finished product rather than a bond on a component.
  And it is a repeat-business problem, because the brand that experiences it once will not simply re-order at the
  same volume &mdash; they will re-source the trim.</p>
</div>

<h2>1. Why Foil Failure Is a Composite Problem, Not a Print Problem</h2>

<p>Every metallic ribbon on the market is a laminate of at least three layers, and each layer brings its own
failure mechanism. The bottom layer is the textile substrate, usually polyester satin, which is compliant and
dimensionally stable but chemically relatively unreactive. The middle layer is the adhesive, which is what actually
joins the foil to the substrate and which is the layer that fails. The top layer is the metallic film itself,
either a hot-stamp foil transferred from a carrier or a vacuum-metallised film applied directly.</p>

<p>The failure mechanics follow from the geometry. A satin substrate is a woven structure with a crown-and-valley
profile on its surface, and the peaks of that profile carry load while the valleys between them carry nothing. An
adhesive film applied by nip pressure flows into the valleys and bridges over the peaks, which means the adhesive
layer is not uniformly bonded &mdash; it is a series of contact islands separated by adhesive that never touched
the substrate at all. When the laminate is flexed, the peaks flex more than the valleys, and the adhesive bridges
over the valleys are where the stress concentrates. A foil bond that appears solid on the flat face of the ribbon
can therefore fail on the edge, where the substrate curves most sharply and the film has to stretch further than
the substrate beneath it.</p>

<p>Two practical consequences follow, and both should be written into the specification. First, <strong>peel
strength must be tested on the edge, not only on the face</strong>, because the edge is where the composite is
weakest and the edge is what the customer handles. Second, <strong>the flex-crack test must be performed at a stated
radius</strong>, because a foil that survives a 180&deg; bend at a 25&nbsp;mm radius may crack badly at a
5&nbsp;mm radius, and a 5&nbsp;mm radius is what a folded bow loop actually imposes on the trim.</p>

<table>
  <thead>
    <tr><th>Layer</th><th>Material</th><th>Failure mechanism</th><th>Test that detects it</th></tr>
  </thead>
  <tbody>
    <tr><td>Substrate</td><td>Polyester satin, 100 denier</td><td>Crown/valley profile creates discontinuous adhesive contact</td><td>Cross-section peel mapping</td></tr>
    <tr><td>Adhesive</td><td>Hot-melt polyamide or acrylic PSA</td><td>Brittle at low temperature, softens at heat, creep under sustained load</td><td>Peel strength, temperature-cycled peel</td></tr>
    <tr><td>Metallic film</td><td>Aluminium on PET carrier, or vacuum-metallised</td><td>Flex-crack through the aluminium layer; edge lift under repeated folding</td><td>Flex-crack cycle test, edge-peel</td></tr>
    <tr><td>Composite</td><td>All three, bonded</td><td>Differential strain between stiff film and compliant textile</td><td>Post-wash delamination, abrasion transfer</td></tr>
  </tbody>
</table>

<h2>2. The 5-Layer Metallic-Surface Authority Model</h2>

<p>Five layers govern the metallic surface, ordered from most frozen to most operational, each with a named owner
and an explicit change threshold. The model exists because the dominant cause of metallic failure is not
manufacturing. It is that the metallic appearance was specified as a colour and then changed by someone with
authority over the colour but not over the bonding, so the new foil arrived with the same adhesive that had been
sized for the old foil's thermal behaviour.</p>

<table>
  <thead>
    <tr><th>Layer</th><th>Parameter</th><th>Owner</th><th>Change threshold</th></tr>
  </thead>
  <tbody>
    <tr><td>L1 Visual identity</td><td>Metallic hue, tone, level, finish (bright, antique, holographic)</td><td>Brand design function</td><td>Design revision. Requires a new foil reference.</td></tr>
    <tr><td>L2 Regulatory and substrate claim</td><td>Base material declaration, OEKO-TEX or GRS chain for the substrate</td><td>Brand compliance function</td><td>Material or certification change. Requires re-issue of the declaration.</td></tr>
    <tr><td>L3 Bond specification</td><td>Adhesive system, coat weight, application temperature, nip pressure, peel floor</td><td>Supplier engineering</td><td>Any change of foil reference, substrate or adhesive lot</td></tr>
    <tr><td>L4 Process control</td><td>Application temperature window, nip dwell, line speed, roll-to-roll registration</td><td>Supplier production</td><td>Changeover or speed adjustment</td></tr>
    <tr><td>L5 Appearance and format</td><td>Edge lift, roll registration, metallic coverage on the selvedge</td><td>Supplier production</td><td>New size or new colourway</td></tr>
  </tbody>
</table>

<p>The threshold in L3 is the one that catches people. Changing the foil reference alone, with the same adhesive
and the same application temperature, is enough to break the bond, because foil suppliers do not standardise their
surface treatment and a hot-melt adhesive tuned for one foil's surface energy will sit on a different foil's
surface like water on wax. The specification should therefore bind the foil reference and the adhesive system
together as a single controlled combination, and require that a change to either triggers a peel re-test before
production release.</p>

<h2>3. The 4-Stage Foil Approval Gate</h2>

<p>Metallic trim should not move from sample to bulk production on a visual check. Four gates, each with a defined
artefact, prevent the most expensive failure in the programme, which is a bulk order of foil that peels in the
fulfilment centre.</p>

<h3>Gate 1 &mdash; Foil and adhesive compatibility confirmation</h3>

<p>Before any ribbon is made, the supplier confirms that the nominated foil reference and the nominated adhesive
system bond to the nominated substrate. This is a coupon test on plain substrate stock, not on finished ribbon, and
it exists to de-risk the adhesive before any production setup cost is incurred. The output is a compatibility
record naming the three references &mdash; foil, adhesive, substrate &mdash; as a combination that has been
verified. This gate catches the majority of adhesive problems at a cost of a few dollars of material.</p>

<h3>Gate 2 &mdash; Lab dip and bulk-trim peel confirmation</h3>

<p>Peel strength on a clean coupon is not the same as peel strength on a ribbon that has been dyed, heat-set, washed
and possibly coated. Dye chemistry and heat-setting both alter the substrate surface, and the metallic roll is
applied after those processes, so the bond is to a dyed and relaxed surface rather than to virgin fibre. The gate
requires that peel strength measured on the finished ribbon meets the stated floor, and that the floor is expressed
as a minimum rather than as a typical value, because the failure mode is the tail of the distribution, not the
average.</p>

<blockquote style="border-left:4px solid #b8854a;padding:8px 16px;margin:1.2em 0;background:#faf6f1;">
&quot;Peel strength is reported as a minimum of the five specimens tested, not as the mean. A specification that
states the mean is a specification that accepts a 3&nbsp;N outlier, and the 3&nbsp;N outlier is the roll that
reaches the customer.&quot;
</blockquote>

<h3>Gate 3 &mdash; Flex-crack and abrasion retention</h3>

<p>This is the gate that most programmes omit and most need. A foil bond that meets a peel requirement on day one
can still crack under repeated flexing, because cracking is a fatigue phenomenon and a single peel test says nothing
about fatigue life. The gate requires two results on the finished trim: a flex-crack count at a stated bend radius
and a stated number of cycles, and an abrasion result expressed as a transfer criterion rather than as a rating.
The transfer criterion is the one that matters commercially, because "no metallic transfer to the abrading cloth"
is a statement about the customer's packaging that the brand cares about, whereas "grade 4 on the Martindale scale"
is a number that has to be interpreted.</p>

<h3>Gate 4 &mdash; Wash and end-use verification</h3>

<p>The final gate puts the trim through the conditions the finished product will meet. For a gift-wrapping ribbon
that means a handling and abrasion cycle rather than a wash; for a garment trim or a hair accessory it means wash
cycles at the stated temperature with the stated number of cycles. The gate also includes the end-use assembly
trial, where the ribbon is formed into the bow, the loop, or the wrap, and the laminate is flexed at the actual
radius the assembly imposes. This is the only test that reproduces the field condition, and it is the test that
catches a 5&nbsp;mm-radius failure that the flat-panel flex test passes.</p>

<h2>4. The 3-Tier Delamination Reconciliation Ladder</h2>

<p>When metallic failure appears, it is usually reported as a single complaint &mdash; "the ribbon is peeling" &mdash;
without a stage, a location, or a mechanism. The reconciliation ladder forces the diagnosis before any corrective
action is agreed, because the three tiers have different causes and different remedies, and treating them the same
way is what causes repeat failures.</p>

<table>
  <thead>
    <tr><th>Tier</th><th>Presentation</th><th>Probable cause</th><th>Corrective action</th></tr>
  </thead>
  <tbody>
    <tr><td>T1 Surface release</td><td>Metallic film lifts in flakes across the face, adhesive visible beneath</td><td>Under-cure or insufficient adhesive coat weight</td><td>Raise coat weight or cure; re-qualify the foil-adhesive pair</td></tr>
    <tr><td>T2 Edge lift</td><td>Film peels away from the selvedge and the cut edge in a continuous strip</td><td>Differential strain; edge not sealed, or radius too tight for the film</td><td>Seal or fold the edge; change foil carrier thickness</td></tr>
    <tr><td>T3 Flex crack</td><td>Fine parallel cracks appear at fold lines; metallic dust transfers</td><td>Aluminium film too thin or too rigid for the fold radius</td><td>Select a more flexible film; change the assembly radius</td></tr>
  </tbody>
</table>

<p>The distinction between T2 and T3 is the one most often missed, and they have opposite remedies. Edge lift is a
bond problem at the boundary, and the fix is to reinforce the boundary or to relieve the strain there. Flex crack is
a material-stiffness problem in the film, and the fix is a different film or a larger assembly radius. Applying an
edge sealant to a flex-crack failure produces a stronger bond that cracks in exactly the same place, and it costs
money, because the reel is scrapped.</p>

<h2>5. The Flex-Crack and Peel-Strength Retention Audit</h2>

<p>Retention is the audit that distinguishes a metallic programme from a metallic product. The question is not
"does it pass at approval" but "what fraction of the original bond survives the life of the product". Retention is
measured as the ratio of post-stress peel strength to initial peel strength, and it is the metric that correlates
with field returns rather than with laboratory pass rates.</p>

<p>For a metallic gift-wrapping ribbon, the realistic stress set is folding, handle abrasion, and thermal storage.
For a garment trim it adds wash. For a hair bow it adds repeated flexing of the bow loop at a small radius, which
is the most severe of the three because the radius is fixed by the bow construction and cannot be adjusted. Each
stress type has a retention target, and the audit reports one combined figure for the programme rather than a list
of individual results, because the buyer needs to know whether the trim will still be acceptable after a season in
market.</p>

<div class="kpi">
  <p><strong>How Smith Ribbon runs the programme:</strong> foil reference, adhesive system and substrate are
  nominated as a single controlled combination, with the peel-strength floor written as a minimum of five specimens.
  Flex-crack and abrasion retention are measured on the finished trim rather than on a flat coupon, and the
  end-use assembly trial is run at the actual formation radius. Xiamen Smith Ribbon &amp; Bow Co., Ltd. has supplied
  woven, printed and metallic ribbon, bows and decorative trims to 1,000+ brands and retailers across 50+ countries
  since 2004, from a 15,000&nbsp;m&sup2; plant running 200+ employees with 100,000 metres of daily capacity, certified
  to OEKO-TEX&reg;, FSC&reg;, BSCI, SEDEX, SMETA and ISO 9001.</p>
</div>

<h2>6. Building the Metallic Requirement Into the RFQ</h2>

<p>The reason metallic programmes fail is usually that the RFQ treats the metallic as a finish rather than as a
bonded composite. A short, precise request saves weeks of sampling and removes the most common source of
disappointment for both sides. The elements that matter are these seven:</p>

<ol>
  <li><strong>Base substrate specification</strong> &mdash; material, width, denier or weight, weave, and the
  certification chain for the substrate itself.</li>
  <li><strong>Metallic route</strong> &mdash; hot-stamp foil transferred from a carrier, vacuum-metallised film, or
  laminated foil, with the film thickness and carrier stated.</li>
  <li><strong>Peel-strength floor</strong> &mdash; method, specimen count, conditioning, and the minimum value
  expressed per 25&nbsp;mm.</li>
  <li><strong>Flex-crack requirement</strong> &mdash; bend radius, cycle count, and what constitutes a failure.</li>
  <li><strong>Abrasion criterion</strong> &mdash; expressed as a transfer prohibition rather than as a rating.</li>
  <li><strong>Washing and end-use conditions</strong> &mdash; temperature, cycle count, and the assembly the trim
  will be formed into.</li>
  <li><strong>Change-control commitment</strong> &mdash; the supplier notifies and re-qualifies before any change to
  foil reference, adhesive lot or substrate.</li>
</ol>

<p>Written this way, a quote becomes comparable. Two suppliers quoting the same metallic trim from this brief are
quoting the same composite, and the difference between their prices reflects a difference in process rather than a
difference in what is being delivered. That is the only way a metallic price comparison is worth making.</p>

<h2>7. Common Mistakes and How to Avoid Them</h2>

<p><strong>Specifying the metallic as a colour.</strong> "Metallic gold" is a visual instruction, not a technical
one. Two metallic golds from two mills can differ in film thickness, in adhesive system, in tone and in field
durability, while satisfying the same instruction. Fix: name the route, the film, the adhesive class and the
performance floors.</p>

<p><strong>Testing peel on the face only.</strong> The edge is where the composite is weakest and where the customer
handles it. Fix: require edge peel as a separate reported result.</p>

<p><strong>Accepting a mean instead of a minimum.</strong> A mean hides the failure tail. Fix: report the minimum of
five specimens.</p>

<p><strong>Skipping the wash or handling verification.</strong> A foil that passes a flat-panel flex test can still
fail in a folded bow loop at a 5&nbsp;mm radius. Fix: run the assembly trial at the real formation radius.</p>

<p><strong>Changing foil without re-qualifying.</strong> The foil is the variable that changes most often because
design wants a slightly different tone, and it is the variable that changes the adhesive behaviour most. Fix: bind
the foil reference to the adhesive system and require re-qualification on any change.</p>

<p><strong>Treating the delamination as a cosmetic issue.</strong> Metallic dust in a gift box or on a retail
display is a packaging defect in the customer's eyes. Fix: write the no-transfer criterion into the specification
and into the purchase order.</p>

<h2>8. Conclusion</h2>

<p>A metallic ribbon is a composite, and the buyer who specifies it as a colour buys a lottery ticket on the field
durability of a bonded film. The four requirements that make the difference are unglamorous and specific: a
minimum peel strength on the finished ribbon, an edge-peel result, a flex-crack count at a stated radius, and an
abrasion transfer prohibition. Add an assembly trial at the real formation radius and the programme becomes
predictable, because the failure that used to appear in the fulfilment centre is now caught at the gate.</p>

<p>For a brand buyer who wants a metallic trim that holds its bond through a season of folding, that specification
is the whole conversation. Everything else &mdash; the number of layers, the authority model, the reconciliation
ladder &mdash; exists to make sure that specification is executed rather than interpreted.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What causes metallic ribbon foil to peel off during use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three distinct mechanisms are responsible for most metallic ribbon peeling, and they need to be told apart before any remedy is chosen. The first is surface release, where the metallic film lifts in flakes because the adhesive did not cure fully or the coat weight was too low, and the fix is to increase coat weight or cure time and re-qualify the foil and adhesive as a pair. The second is edge lift, where the film peels in a continuous strip from the selvedge or the cut edge because of differential strain between a stiff film and a compliant textile at the point where the substrate curves most sharply, and the fix is to seal or fold the edge or to change the carrier thickness. The third is flex crack, where fine parallel cracks appear at fold lines and metallic dust transfers, because the aluminium film is too thin or too rigid for the radius the assembly imposes, and the fix is a more flexible film or a larger formation radius. Applying an edge sealant to a flex-crack failure usually produces a stronger bond that cracks in the same place, because the reel is scrapped."
      }
    },
    {
      "@type": "Question",
      "name": "How do you test the adhesion strength of foil on a woven ribbon?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use a 180 degree adhesive tape peel test on the finished ribbon, not on a flat substrate coupon, because dyeing and heat-setting both alter the substrate surface and the metallic roll is applied after those processes. Condition the specimens for at least 24 hours at standard temperature and humidity before testing, test at least five specimens taken across the width, and report the minimum value per 25 millimetres rather than the mean. A specification written as a mean accepts a weak outlier, and the weak outlier is the roll that reaches the customer. Report the edge separately from the face, because the edge is where the adhesive bridges over the valleys of the woven substrate and the stress concentrates. At Smith Ribbon the peel floor, the flex-crack cycle count and the abrasion transfer criterion are issued as one programme file with each shipment."
      }
    },
    {
      "@type": "Question",
      "name": "What is a flex-crack test and why does it matter for metallic ribbon?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A flex-crack test cycles a specimen through repeated bending at a stated radius and then checks whether the metallic layer has cracked. It matters because metallic failure by cracking is a fatigue phenomenon, so a single peel test taken on the day of production says nothing about how the trim behaves after a season of handling. The test is meaningless without two stated parameters: the bend radius and the cycle count, because a foil that survives 180 degree bends at a 25 millimetre radius can crack badly at a 5 millimetre radius. For a hair bow or a small gift loop, the 5 millimetre radius is the condition the assembly actually imposes and cannot be adjusted, so the assembly trial should be run at that radius rather than relying on a flat-panel test."
      }
    },
    {
      "@type": "Question",
      "name": "Can a ribbon supplier apply metallic foil to a custom woven or printed base?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it is usually the better arrangement because the metallic roll is bonded to a substrate the same party controls, so the substrate surface state at the moment of bonding is known rather than assumed. Smith Ribbon applies metallic surfaces to woven polyester satin, grosgrain, organza and printed ribbon bases for brand buyers across more than 50 countries. The sequence matters: dyeing and heat-setting happen first, then printing if the programme includes a print, then the metallic application, because the metallic roll is bonded to a dyed, relaxed and possibly printed surface rather than to virgin fibre. If the programme includes both a print and a metallic finish, the two need a stated relationship, because a print layer under the foil changes the adhesive behaviour and has to be part of the qualification rather than an afterthought."
      }
    },
    {
      "@type": "Question",
      "name": "How do I write a metallic ribbon specification so that two suppliers quote the same product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Specify the composite in seven parts rather than naming a metallic colour. Give the base substrate material, width, denier or weight, weave and certification chain. Give the metallic route, which is hot-stamp foil transferred from a carrier, vacuum-metallised film or laminated foil, together with the film thickness and the carrier material. Give the adhesive class and the peel-strength floor with its method, specimen count and conditioning. Give the flex-crack requirement with its bend radius and cycle count. Give the abrasion criterion expressed as a prohibition on metallic transfer to the abrading cloth. Give the wash or handling conditions and the assembly the trim will be formed into. Add a change-control commitment so that a change of foil reference, adhesive lot or substrate triggers re-qualification before production. Written this way, a price difference between two suppliers reflects a difference in process rather than a difference in what is being delivered."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum order quantity for custom metallic ribbon?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "At Smith Ribbon, custom metallic ribbon typically starts around 500 metres per colour and width for an existing base construction, with a new base weave or a new metallic colour adding normally seven to twelve days on top of the standard 25 to 40 days to production readiness. The binding constraint on a metallic programme is rarely the unit price but the number of distinct combinations, because each new base construction and each new foil reference is a separate qualification with its own compatibility gate, its own lab dip and its own peel and flex-crack verification. That is also why the foil reference and the adhesive system should be specified as a single controlled combination rather than as two independent selections."
      }
    }
  ]
}
</script>

<h3>What causes metallic ribbon foil to peel off during use?</h3>
<p>Three distinct mechanisms are responsible for most metallic ribbon peeling, and they need to be told apart before
any remedy is chosen. The first is surface release, where the metallic film lifts in flakes because the adhesive
did not cure fully or the coat weight was too low, and the fix is to increase coat weight or cure time and
re-qualify the foil and adhesive as a pair. The second is edge lift, where the film peels in a continuous strip from
the selvedge or the cut edge because of differential strain between a stiff film and a compliant textile at the point
where the substrate curves most sharply, and the fix is to seal or fold the edge or to change the carrier thickness.
The third is flex crack, where fine parallel cracks appear at fold lines and metallic dust transfers, because the
aluminium film is too thin or too rigid for the radius the assembly imposes, and the fix is a more flexible film or
a larger formation radius. Applying an edge sealant to a flex-crack failure usually produces a stronger bond that
cracks in the same place, because the reel is scrapped.</p>

<h3>How do you test the adhesion strength of foil on a woven ribbon?</h3>
<p>Use a 180&deg; adhesive tape peel test on the finished ribbon, not on a flat substrate coupon, because dyeing and
heat-setting both alter the substrate surface and the metallic roll is applied after those processes. Condition the
specimens for at least 24 hours at standard temperature and humidity before testing, test at least five specimens
taken across the width, and report the minimum value per 25&nbsp;millimetres rather than the mean. A specification
written as a mean accepts a weak outlier, and the weak outlier is the roll that reaches the customer. Report the edge
separately from the face, because the edge is where the adhesive bridges over the valleys of the woven substrate and
the stress concentrates. At Smith Ribbon the peel floor, the flex-crack cycle count and the abrasion transfer
criterion are issued as one programme file with each shipment.</p>

<h3>What is a flex-crack test and why does it matter for metallic ribbon?</h3>
<p>A flex-crack test cycles a specimen through repeated bending at a stated radius and then checks whether the
metallic layer has cracked. It matters because metallic failure by cracking is a fatigue phenomenon, so a single peel
test taken on the day of production says nothing about how the trim behaves after a season of handling. The test is
meaningless without two stated parameters: the bend radius and the cycle count, because a foil that survives
180&deg; bends at a 25&nbsp;millimetre radius can crack badly at a 5&nbsp;millimetre radius. For a hair bow or a
small gift loop, the 5&nbsp;millimetre radius is the condition the assembly actually imposes and cannot be
adjusted, so the assembly trial should be run at that radius rather than relying on a flat-panel test.</p>

<h3>Can a ribbon supplier apply metallic foil to a custom woven or printed base?</h3>
<p>Yes, and it is usually the better arrangement because the metallic roll is bonded to a substrate the same party
controls, so the substrate surface state at the moment of bonding is known rather than assumed. Smith Ribbon
applies metallic surfaces to woven polyester satin, grosgrain, organza and printed ribbon bases for brand buyers
across more than 50 countries. The sequence matters: dyeing and heat-setting happen first, then printing if the
programme includes a print, then the metallic application, because the metallic roll is bonded to a dyed, relaxed
and possibly printed surface rather than to virgin fibre. If the programme includes both a print and a metallic
finish, the two need a stated relationship, because a print layer under the foil changes the adhesive behaviour and
has to be part of the qualification rather than an afterthought.</p>

<h3>How do I write a metallic ribbon specification so that two suppliers quote the same product?</h3>
<p>Specify the composite in seven parts rather than naming a metallic colour. Give the base substrate material,
width, denier or weight, weave and certification chain. Give the metallic route, which is hot-stamp foil transferred
from a carrier, vacuum-metallised film or laminated foil, together with the film thickness and the carrier
material. Give the adhesive class and the peel-strength floor with its method, specimen count and conditioning. Give
the flex-crack requirement with its bend radius and cycle count. Give the abrasion criterion expressed as a
prohibition on metallic transfer to the abrading cloth. Give the wash or handling conditions and the assembly the
trim will be formed into. Add a change-control commitment so that a change of foil reference, adhesive lot or
substrate triggers re-qualification before production. Written this way, a price difference between two suppliers
reflects a difference in process rather than a difference in what is being delivered.</p>

<h3>What is the minimum order quantity for custom metallic ribbon?</h3>
<p>At Smith Ribbon, custom metallic ribbon typically starts around 500 metres per colour and width for an existing
base construction, with a new base weave or a new metallic colour adding normally seven to twelve days on top of the
standard 25 to 40 days to production readiness. The binding constraint on a metallic programme is rarely the unit
price but the number of distinct combinations, because each new base construction and each new foil reference is a
separate qualification with its own compatibility gate, its own lab dip and its own peel and flex-crack verification.
That is also why the foil reference and the adhesive system should be specified as a single controlled combination
rather than as two independent selections.</p>
"""

write_article(a, BODY,
              "Specify the metallic composite, not the metallic colour",
              "Request the metallic foil specification template with peel, flex-crack and abrasion floors")
print(f"slug={SLUG}")