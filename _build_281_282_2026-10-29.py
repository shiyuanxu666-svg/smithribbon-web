#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon articles 281 (AM) + 282 (PM), 2026-10-29.

Module 281 (AM): Ribbon Slit-Width Tolerance & Selvedge-Weave Stability Interlock
Module 282 (PM): Ribbon Twist & Yarn Directionality Interlock (S/Z twist, torque memory)

Both follow the established mill-side brand-buyer interlock format:
h1, meta, OG/Twitter, BlogPosting + BreadcrumbList + FAQPage JSON-LD,
visible FAQ section, standard footer.
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-29"
FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")
AUTHOR = "Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.)"

# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_page(*, slug, title, desc, keywords, section, module, time_hm,
               body_sections, faq, published_iso):
    """body_sections: list of (h2_text, html_block)"""
    url = f"https://smithribbon.com/{slug}.html"
    kw = esc(keywords)

    # ---- BlogPosting ----
    blogposting = f"""{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{esc(title)}",
  "description": "{esc(desc)}",
  "image": "https://smithribbon.com/logo.png",
  "author": {{
    "@type": "Organization",
    "name": "{AUTHOR}",
    "url": "https://smithribbon.com/about.html"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "{AUTHOR}",
    "url": "smithribbon.com"
  }},
  "datePublished": "{DATE}",
  "dateModified": "{DATE}",
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{url}"
  }},
  "keywords": "{kw}"
}}"""

    # ---- BreadcrumbList ----
    breadcrumb = f"""{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://smithribbon.com/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://smithribbon.com/blog.html"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{esc(title)}",
      "item": "{url}"
    }}
  ]
}}"""

    # ---- FAQPage ----
    qa = []
    for q, a in faq:
        qa.append(f"""    {{
      "@type": "Question",
      "name": "{esc(q)}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{esc(a)}"
      }}
    }}""")
    faqpage = f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{",".join(qa)}
  ]
}}"""

    # ---- visible body ----
    parts = []
    for h2, block in body_sections:
        parts.append(f"<h2>{h2}</h2>\n{block}")

    # visible FAQ section
    fq = []
    for i, (q, a) in enumerate(faq, 1):
        fq.append(f'<h3>FAQ {i}: {esc(q)}</h3>\n<p>{a}</p>')
    parts.append('<h2 id="faq">Frequently Asked Questions</h2>\n' + "\n".join(fq))

    body = "\n".join(parts)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)} | Smith Ribbon</title>
    <meta name="description" content="{esc(desc)}">
    <meta name="keywords" content="{kw}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://smithribbon.com/logo.png">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{published_iso}">
    <meta property="article:modified_time" content="{published_iso}">
    <meta property="article:author" content="{AUTHOR}">
    <meta property="article:section" content="{esc(section)}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="https://smithribbon.com/logo.png">
    <script type="application/ld+json">
{blogposting}
    </script>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
    </nav>
    <main>
        <article>
            <h1>{esc(title)}</h1>
            <p class="meta"><span class="tag">{esc(section)}</span> &middot; Module {module} &middot; {DATE}</p>
            <p class="lede">{esc(desc)}</p>
{body}
        </article>

    <script type="application/ld+json">
{breadcrumb}
    </script>

    <script type="application/ld+json">
{faqpage}
    </script>
</main>
    <p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>
</body>
</html>
"""


# ============================================================================
# MODULE 281 — AM
# ============================================================================

T281 = ("Mill-Side Brand-Buyer Ribbon Slit-Width Tolerance &amp; Selvedge-Weave Stability "
        "Interlock Architecture &mdash; Edge Parallelism, Bow Symmetry and Repeat-Order "
        "Width Drift 2026")

D281 = ("A mill-side brand-buyer guide to ribbon slit-width tolerance and selvedge-weave "
        "stability. Covers why a nominal 10 mm ribbon measures 9.4 mm at the selvedge and "
        "10.6 mm at the centre, how loom-width tolerance and slittability interact with "
        "bow loop symmetry, the width-versus-weave-construction trade-off, how to set a "
        "measurement protocol that survives a change of roll width, and why width drift "
        "shows up first in pre-tied bows rather than on the roll.")

K281 = ("ribbon slit width tolerance, ribbon selvedge stability, ribbon edge parallelism, "
        "bow loop symmetry ribbon, ribbon width measurement protocol, ribbon narrow woven "
        "fabric slitting, ribbon loom width tolerance, ribbon repeat order width drift, "
        "brand buyer ribbon quality, ribbon width spec sheet, ribbon selvage fraying "
        "control, ribbon gauge tolerance ribbon, ribbon bow size consistency")

S281 = "B2B Sourcing"

body281 = [
("The width you order is not the width you receive",
"""<p>Almost every brand buyer working with ribbon has had the same experience. The specification says 10 mm. The supplier confirms 10 mm. The roll arrives and the tape measure says 10 mm in the middle and something else — noticeably less — about four millimetres in from each edge. Nothing is wrong with the roll in any legal sense. Nothing is wrong with the mill either. What has happened is that a single nominal number has been asked to stand in for a physical quantity that varies across the width of the material and from roll to roll within a programme.</p>
<p>This matters far more for ribbon than it does for most textiles, because ribbon is not usually consumed as a length of material. It is consumed as a <strong>shape</strong>. A ribbon becomes a bow, and a bow becomes a product that a customer sees from a distance and compares against a photograph. Width error that would be irrelevant in a metre of lining fabric becomes the single most visible attribute of a gift bow. The buyer who specifies width as one number without a measurement protocol is buying a shape whose dimensions are unknown.</p>
<p>This guide sets out how slit width and selvedge weave stability actually interact, how the two contribute to bow symmetry defects, and how to write a width specification that a mill and a QA laboratory can both execute without ambiguity.</p>"""),

("Why width varies across the width of the ribbon",
"""<p>Width variation in ribbon has three separate physical sources, and they need to be understood separately because they have different remedies and different tolerances.</p>
<p><strong>1. Loom-width tolerance.</strong> The ribbon is woven on a loom at a nominal reed width. The reed does not deliver an absolutely uniform spacing of warp ends across its full width, because warp tension is not perfectly uniform, because the reed dents flex slightly under load, and because the fabric is under tension as it leaves the reed and relaxes as it moves through the rest of the loom. The practical result is that the fabric as woven has a width that is close to nominal at the centre and marginally narrower toward each selvedge. This is the dominant source of width error in narrow woven ribbon, and it is why an 8 mm ribbon typically behaves differently from a 38 mm ribbon: the absolute tolerance in millimetres that the mill can hold does not scale linearly with the nominal width.</p>
<p><strong>2. Slitting tolerance.</strong> A wide ribbon fabric is produced and then slit into narrower widths for the slitted product. The slitting knife has to be set to the required width, and the setting is a physical position that is repeated on a rotating or traversing cutter. Setting accuracy, blade deflection under load and roll-mounting concentricity all contribute. Slitting is the source of the <em>roll-level</em> width error: a roll that is uniformly 9.6 mm when it should be 10.0 mm.</p>
<p><strong>3. Relaxation and finishing shrinkage.</strong> Woven ribbon relaxes when it comes off the loom and again when it is heat-set or coated. If the width specification is written against the loom state rather than the finished state, the finished product will not meet it. This is the most common technical dispute in ribbon procurement and it is entirely avoidable by stating which state is being measured.</p>
<p>The important consequence is that a buyer who measures only at the centre of the ribbon will systematically over-read the width and will miss the edge behaviour that determines whether the bow hangs correctly.</p>"""),

("The width-versus-weave-construction trade-off",
"""<p>Narrow widths impose real technical constraints that buyers rarely appreciate when they write the specification. A 6 mm ribbon and a 38 mm ribbon are not the same product with different numbers on the label.</p>
<ul>
<li><strong>Selvedge structure.</strong> Below roughly 10 mm, a plain-weave construction often has no room for a dedicated selvedge, and the edge is simply the termination of the warp and weft. That edge will fray under handling, and it will not support a wired edge or a turned hem. Above 15 mm, a mill can run a woven selvedge or a reinforced edge treatment that changes the character of the material entirely.</li>
<li><strong>Pick density per unit width.</strong> To hold a consistent weight per metre across a range of widths, the pick density per centimetre must increase as the width decreases. This raises tension, raises the risk of a snagging weft, and can make the ribbon noticeably stiffer or more board-like at narrow widths.</li>
<li><strong>Dimensional stability.</strong> A narrow ribbon has less transverse resistance to distortion. Once a bow is tied, or a ribbon is folded, the narrow width more readily takes a permanent set.</li>
<li><strong>Print registration tolerance.</strong> On very narrow widths, a printed repeat cannot be centred with the same absolute precision, and edge waste becomes proportionally larger. Buyers specifying narrow printed ribbon should expect the mill to quote a wider registration tolerance than for a 25 mm product.</li>
</ul>
<p>The point is not that narrow ribbon is problematic. It is that a width specification which ignores construction is not a specification the mill can quote accurately, and a mill forced to quote it will either absorb a cost it should have flagged or guess and get it wrong.</p>"""),

("Selvedge weave stability and edge parallelism",
"""<p>Selvedge weave stability describes whether the edge holds its geometry under the stresses the ribbon will actually meet: winding tension during slitting and rewinding, tension during conversion, tension during tying into a bow, and handling friction during packing and shipping.</p>
<p>Three measurable properties define it.</p>
<p><strong>Edge parallelism</strong> is the deviation of the edge from a straight line across the width of the roll. It is measured by taking the roll and checking whether the edge is parallel to the roll axis over a stated length. A ribbon with a non-parallel edge will produce a bow whose two loops are different lengths even when the ribbon itself is nominally the same width throughout — because a bow is made from a finite segment of material and the width available for each loop varies along that segment.</p>
<p><strong>Edge straightness over the roll length</strong> is related but separate. A ribbon can be parallel and still wander, or straight and not parallel. Both cause loop asymmetry, and both cause a visible difference in how the ribbon lies in a folded stack.</p>
<p><strong>Selvedge fray resistance</strong> is the ability of the edge to survive handling without threads pulling out. This is where construction matters most: a plain selvedge on a narrow ribbon will fray under the tension of a pre-tied bow assembly line, and the fray will be visible on the finished product. A mill that has tested its edge under bow-assembly tension will be able to tell you how it performs; one that has only tested it under a static pull test has not answered the question you are asking.</p>
<p>The buyer-facing implication is that the width specification and the edge specification should be written together and should be tested together. A ribbon that measures perfectly at the centre but frays at the edge will produce a defective bow that no incoming inspection based on centre measurement will catch.</p>"""),

("How width defects become bow defects",
"""<p>Translating a mill measurement into a product outcome is what turns a tolerance into a specification. For a pre-tied bow made from a fixed length of ribbon, the relationship between width error and the finished bow is direct.</p>
<p><strong>Loop symmetry.</strong> A bow's visual balance depends on the two loops being the same length and the same width. If the ribbon width varies along the segment used for the bow, or if the segment spans a region where the edge is non-parallel, the two loops will differ. A buyer who has received returns described as &quot;off-centre bows&quot; should look first at width tolerance and edge parallelism, not at the bow-making labour.</p>
<p><strong>Loop volume and drape.</strong> Ribbon width controls how much material is available to form a loop. At a constant length, a narrower ribbon produces a flatter, tighter loop; a wider ribbon produces a fuller loop with more body. Where a product photography shot or a previous product line defines the intended look, the width tolerance is doing aesthetic work and should be specified more tightly than a purely functional tolerance would require.</p>
<p><strong>Height consistency.</strong> If a bow is assembled by folding the ribbon at a fixed distance from the cut end, and the ribbon is wider than the fold allows, the fold encroaches on the loop. If the ribbon is narrower than the fold pattern expects, the bow looks under-filled. The assembly tolerance and the width tolerance are therefore coupled, and the tighter of the two governs the achievable product consistency.</p>
<p>None of this is a reason to specify an impossibly tight tolerance. It is a reason to specify width at the level that the end product actually needs, and to know which end-product attribute each increment of tolerance buys.</p>"""),

("A width measurement protocol that survives reorders",
"""<p>The single most valuable thing a brand buyer can put in a ribbon specification is a statement of exactly where and how the width is measured. The following protocol has the advantage that it can be executed identically by the mill, by an incoming inspection laboratory and by a third-party inspector, and it survives a change of roll width without needing to be rewritten.</p>
<ul>
<li><strong>State the measurement position.</strong> Measure at the centre, and separately at 4 mm in from each selvedge. Report all three. For ribbons narrower than 12 mm, use 2 mm in from each edge instead, so that the measurement point is not inside the selvedge structure itself.</li>
<li><strong>State the state of the material.</strong> Measure on the finished, conditioned ribbon &mdash; after heat setting and after any reasonable period of conditioning in the standard atmosphere &mdash; not on the loom or immediately off the slitter.</li>
<li><strong>State the conditioning condition.</strong> Temperature and relative humidity for the conditioning period, and the conditioning period itself. Width is a physical measurement and it is not independent of the atmosphere.</li>
<li><strong>State the sampling rule.</strong> How many points along the roll, measured from which end, and whether the roll is measured before or after rewinding onto the shipping core.</li>
<li><strong>State the instrument.</strong> A calibrated micrometer or a digital caliper of stated resolution, applied without compression &mdash; a micrometer's anvil compresses soft ribbon and a caliper's jaws do the same, which is why ribbon width measurements should specify the closure force or, more practically, the measurement method that the mill and the inspector both already use consistently.</li>
<li><strong>State the acceptance rule.</strong> Whether the requirement is on the mean width, on every individual measurement, or on a stated proportion of measurements within tolerance. This is the point at which most ribbon disputes actually originate.</li>
</ul>
<p>Two further details save arguments later. First, specify the tolerance <em>relative</em> where the width is narrow and <em>absolute</em> where it is wide: a &plusmn;0.3 mm tolerance on a 6 mm ribbon is a five percent variation, while the same tolerance on a 38 mm ribbon is under one percent and is tighter than most mills can hold consistently. Second, always state the tolerance as it applies to the width <strong>of the supplied product</strong>, not to the width of the loom product before slitting.</p>"""),

("Managing width drift across a reorder programme",
"""<p>Width drift across reorder cycles has the same root cause as colour drift, expressed differently: the specification described a target rather than a controlled process. Four practices prevent it.</p>
<p><strong>Lock the slittability envelope, not just the target width.</strong> The mill's ability to slit a given fabric to a given width depends on the fabric. The buyer should specify the fabric construction &mdash; yarn counts, weave, pick density, finish &mdash; because it is the construction that constrains the width tolerance. A mill that changes yarn count to manage cost will change the width behaviour, and the buyer should know that this is a specification-controlled event, not a purchasing decision.</p>
<p><strong>Retain the production roll reference.</strong> Where a programme has an approved width at a specific roll construction, that construction should be named in the purchase order so that a reorder is checked against it rather than against a bare number.</p>
<p><strong>Require a width profile, not a width number.</strong> The three-point measurement protocol should be attached to the first production lot approval, so that the actual profile of the material is on record rather than inferred from a single centre measurement.</p>
<p><strong>Treat a loom-width change as a qualification event.</strong> If the programme moves to a different loom width or a different weaving programme, the slittability of the new fabric must be re-established before it is relied upon for the established widths. This is a short test and it prevents a systematic narrowing that would otherwise appear gradually across a year of orders.</p>
<p>Buyers who adopt this discipline find that width complaints largely stop, not because the tolerance was tightened but because the tolerance finally meant one thing to both parties.</p>"""),
]

faq281 = [
("What is the standard width tolerance for ribbon?",
 "There is no universal figure, and any mill that quotes one without asking about the width, the construction and the end use is guessing. In practice, a narrow plain-weave ribbon below 10 mm behaves in the region of plus or minus 0.2 to 0.3 mm at the centre, while a wider satin or grosgrain above 25 mm may be held to plus or minus 0.5 mm. The more useful approach is to specify relative tolerance for narrow widths and absolute tolerance for wide ones, and to state where on the ribbon the measurement is taken. If you need the edge value as well as the centre value, say so explicitly, because the centre reading alone will not predict bow loop symmetry."),
("Should I measure ribbon width at the centre or at the edge?",
 "Measure at both and record three values: the centre and two points set in from each selvedge. The centre reading tells you whether the roll is the right width. The edge readings tell you whether the material is stable across its width, which is what determines whether a cut segment will produce two identical bow loops. A ribbon can pass a centre-only inspection and still produce asymmetric bows, because the inspection never looked at the property that causes the defect."),
("How does ribbon width affect pre-tied bow quality?",
 "Width affects bow quality through three channels: loop symmetry, where a width that varies along the segment makes one loop fuller than the other; loop volume and drape, where a narrower ribbon gives a flatter, tighter loop and a wider one gives a fuller loop with more body; and height consistency, where a width that does not match the fold pattern produces either an encroaching fold or an under-filled bow. If a buyer is receiving returns for off-centre or uneven bows, width tolerance and edge parallelism should be investigated before the assembly operation is blamed."),
("Can you slit ribbon narrower than the loom width?",
 "Yes, and every narrow ribbon in production is slit from a wider fabric. The limit is not the loom but the fabric. Slitting tolerance depends on how well the woven construction supports the cut, and on whether the selvedge has enough structure to survive it. Below roughly 10 mm, a plain-weave construction often has no true selvedge, so the cut edge is an unfinished edge and will fray under tension. A mill should tell you whether your target width can be cut from your chosen construction without edge treatment, and what the resulting edge will survive."),
("What happens to width when the mill changes loom width or yarn count?",
 "It moves, usually gradually, and it usually moves in the direction of the new construction rather than randomly. Changing yarn count or pick density to manage cost changes the transverse behaviour of the fabric, which changes both the loom-width tolerance and the slittability. This should be treated as a specification-controlled event: the buyer approves the new construction, the mill re-establishes the width profile against the three-point protocol, and the first production lot is released only after the profile has been confirmed. A qualification test is inexpensive and prevents a year of drift."),
("Why does ribbon width vary between rolls within the same order?",
 "Within-roll and between-roll variation come from different sources. Between-roll variation is typically the slitter setting and the roll-mounting concentricity, and it is the larger of the two for a slitted product. Within-roll variation comes from the loom-width behaviour and from relaxation, and it tends to be larger at the edge than at the centre. Because both are real and both are controllable to a degree, the specification should carry a sampling rule that states how many measurement points along the roll and how many rolls from the order are checked. A single measurement per roll cannot detect either failure mode."),
]

art281 = dict(
    slug=("blog-ribbon-oem-281-module-mill-side-brand-buyer-ribbon-slit-width-tolerance-"
          "selvedge-weave-stability-interlock-architecture-edge-parallelism-bow-symmetry-"
          "repeat-order-width-drift-2026-10-29-am"),
    title=T281, desc=D281, keywords=K281, section=S281, module=281,
    time_hm="10:00", published_iso="2026-10-29T10:00:00+08:00",
    body_sections=body281, faq=faq281,
)

# ============================================================================
# MODULE 282 — PM
# ============================================================================

T282 = ("Mill-Side Brand-Buyer Ribbon Yarn Twist Direction &amp; Twist-Levelling Interlock "
        "Architecture &mdash; S/Z Twist, Torque Memory and Balanced Bow Hangs 2026")

D282 = ("A mill-side brand-buyer guide to ribbon yarn twist direction and twist-levelling "
        "interlock architecture. Covers why a satin ribbon with the wrong twist direction "
        "untwists in the bow, what torque memory does to a bow over a year of shelf life, "
        "how S-twist and Z-twist yarn interact when they meet in a woven ribbon, how to "
        "specify twist direction so it survives slitting and conversion, and the balance "
        "and conditioning tests that catch a twist problem before it reaches a customer.")

K282 = ("ribbon twist direction, S twist vs Z twist yarn, ribbon torque memory, ribbon "
        "twist levelling, satin ribbon untwisting, balanced bow hang, ribbon spiral "
        "distortion, ribbon yarn twist specification, brand buyer ribbon quality, ribbon "
        "twist count per inch, ribbon roll relaxation twist, ribbon bow storage deformation")

S282 = "B2B Sourcing"

body282 = [
("The defect that appears six months after the bow leaves the factory",
"""<p>There is a class of ribbon defect that passes every inspection on the day it is made and fails in the hands of the customer weeks or months later. The bow looks correct in the sample room. It looks correct in the photograph. It arrives at the retailer correct. Then the retail shelf does what retail shelves do &mdash; it warms, it cools, it sits under lights for a season &mdash; and the bow slowly develops a spiral. The loops no longer sit in the same plane. One loop has wound inward. The product that was signed off has changed shape with no one touching it.</p>
<p>The cause is almost always twist, and it is almost always a specification failure rather than a manufacturing failure. The mill produced ribbon with a twist direction that is perfectly serviceable for the product it makes. The buyer bought ribbon without specifying the twist direction, or specified it in a way that the conversion process could not honour, and the mismatch only became visible once the finished product had time and temperature.</p>
<p>This guide explains what twist direction and torque memory are, how they behave through slitting, conversion, packing and shelf life, and how to write a twist specification that a mill can execute and a buyer can verify.</p>"""),

("Twist direction: what S and Z actually mean",
"""<p>Yarn is twisted. The direction of that twist is described by the letter that describes the slope of the helix when the yarn is viewed along its length. In an <strong>S-twist</strong> yarn, the helix runs in the same direction as the middle stroke of the letter S. In a <strong>Z-twist</strong> yarn, it runs in the same direction as the middle stroke of the letter Z.</p>
<p>The distinction is not cosmetic. It is the single most consequential binary choice in a ribbon programme, because it determines which way the yarn wants to unwind when it is cut, folded or tied.</p>
<p>The rule of thumb that runs through the industry is that the twist direction of the yarn and the twist direction of the resulting ribbon should be the same. When they are the same, the ribbon is balanced: it lies flat, it folds without spiralling, and a bow made from it holds a stable plane. When they are opposed &mdash; a Z-twist yarn woven into an S-twist ribbon, or a fibre content whose natural twist opposes the yarn twist &mdash; the ribbon is unbalanced. It has a tendency to rotate, and the tendency is activated the moment the ribbon is cut and the ends are freed.</p>
<p>Two further factors determine whether a given ribbon is balanced in practice. The first is the relative magnitude of the yarn twist and the fabric twist: in a woven ribbon, the warp yarns are twisted one way and the weft is inserted and held in tension, and the balance of the finished fabric depends on how those two effects interact. The second is the balance between the two fibre directions &mdash; a fabric made from a staple fibre with a high natural twist will behave very differently from one made from a continuous filament with minimal twist.</p>"""),

("Torque memory: the slow failure",
"""<p>Torque memory is the tendency of a yarn or a ribbon to retain a rotational bias after the tension that created the bias has been removed. It is best understood as stored energy. Twist in a yarn is, mechanically, a storage of elastic energy in the form of a helix; the fibres are held at an angle to the yarn axis and they would prefer to lie straighter. Cutting the yarn releases the constraint at the ends, and the helix relaxes.</p>
<p>For a ribbon, this shows up in a specific and very commercial way.</p>
<p>When a length of ribbon is folded to make a bow, one side of the fold goes into compression and the other into tension. The fibres on the compressed side are already inclined at the helix angle and are pushed further; the fibres on the tensioned side are pulled closer to the yarn axis and therefore want to rotate back. Over a length of time in storage, the ribbon gradually adopts the twisted state. The bow's loops slowly rotate relative to each other. The product develops a visible spiral.</p>
<p>Three factors govern how fast this happens and whether it happens at all.</p>
<ul>
<li><strong>Magnitude of the stored bias.</strong> A ribbon made from a high-twist yarn with an unbalanced construction has more stored energy, and therefore a stronger tendency to move.</li>
<li><strong>Environment.</strong> Temperature and humidity both accelerate relaxation. A bow stored in a warm warehouse or in a shop window will develop a spiral considerably faster than one kept in a stable, cool environment. This is why the defect is frequently reported as seasonal.</li>
<li><strong>Whether the product is restrained.</strong> A bow that is folded flat and constrained in a card or a bag cannot move. A bow that is presented loose on a display or shipped in an open carton can. The retailer who receives a carton of loose bows in August sees the problem sooner than the retailer who receives them in November.</li>
</ul>
<p>The practical implication for a buyer is that a twist problem is often invisible at goods-in and almost always visible at the point of sale. It is also one of the very few ribbon defects that is genuinely a time bomb, which makes it worth specifying carefully rather than accepting the mill's standard construction.</p>"""),

("How twist behaves through slitting and conversion",
"""<p>A ribbon that leaves the loom balanced can still arrive at the bow factory unbalanced, because the processes between the loom and the finished product add and remove twist energy in ways that are rarely specified.</p>
<p><strong>Slitting.</strong> Slitting is a tensioned process. The wide fabric passes through slitters under tension and is wound onto cores under tension. Tension applied asymmetrically to one side of the web introduces a torque into the material that is baked in by the winding tension. A ribbon wound too tightly will develop a set, and part of that set is rotational. This is one reason that roll tension specification exists, and why it matters more for twist-sensitive products than for ordinary webbing.</p>
<p><strong>Rewinding and let-down.</strong> The number of times a ribbon is unwound and rewound between the loom and the shipment changes its stress history. Each cycle releases some tension and can introduce a small net rotation. A programme that is slit, rewound for inspection, then slit again is a different material from one that is slit once.</p>
<p><strong>Cutting.</strong> Cutting to length frees the ends and allows the stored bias to act. Ribbon cut and used immediately from the same roll behaves better than ribbon cut weeks earlier, because the relaxation has already begun rather than being concentrated at the moment of assembly. For twist-sensitive programmes, specifying a maximum period between slitting and conversion, and requiring the ribbon to be cut and bow-assembled within the same production window, is a genuine control.</p>
<p><strong>Bow tying.</strong> The tie itself introduces a controlled twist into the centre. The skill of the operator is precisely in managing that. A factory that has tuned its tie to the ribbon's twist direction will produce a stable bow; a factory that has not will produce a bow that looks right when it is tied and spirals afterwards, regardless of how carefully it was tied.</p>
<p>The lesson for a brand buyer is that the twist specification is not a property of the ribbon alone. It is a property of the ribbon in combination with the conversion route. Buying twist-sensitive ribbon without specifying what happens to it afterwards is the same category of error as buying a colour without specifying the lighting.</p>"""),

("Specifying twist direction so it survives the supply chain",
"""<p>There are two ways to write a twist specification, and one of them does not work.</p>
<p><strong>The specification that does not work</strong> is &quot;balanced ribbon&quotquot; or &quot;no untwist tendency&quotquot;. It cannot be verified objectively, it cannot be plotted on a control plan, and it leaves the mill to define it however it likes. It is better than nothing, because it tells the mill the customer cares, but it is not a specification.</p>
<p><strong>The specification that works</strong> states the physical parameters. A workable twist specification for a ribbon programme contains the following elements.</p>
<ul>
<li><strong>The yarn twist direction</strong> for the warp and, where relevant, the weft, expressed as S or Z.</li>
<li><strong>The target twist level</strong>, expressed as turns per metre or per inch, with a tolerance. This is what lets the mill control the yarn preparation rather than merely the finished appearance.</li>
<li><strong>The required balance state</strong> of the finished ribbon, expressed in a way that can be tested. The standard tests are a residual-twist or torque measurement after conditioning, and a spiral or flatness observation after a defined relaxation period.</li>
<li><strong>The conditioning specification</strong> &mdash; temperature, relative humidity and duration &mdash; before measurement, because twist balance is a climate-sensitive property and a number measured without a stated conditioning condition is not comparable to anything.</li>
<li><strong>The post-conversion window</strong> for twist-sensitive programmes: the maximum interval between slitting and assembly, and a requirement that the finished product be relax-tested before shipment.</li>
</ul>
<p>Two of these are worth emphasising. The conditioning specification is what makes the residual-twist figure meaningful; it is the same discipline as conditioning before a colour measurement, and for the same reason. The post-conversion window is what converts a ribbon specification into a product specification, and it is the element most often missing because it sits outside the ribbon supplier's own control.</p>"""),

("Testing balance and twist before the product ships",
"""<p>Twist problems are cheap to catch and expensive to discover in the market. Four checks cover most of the risk, and they belong in the approval sequence rather than in the incoming inspection plan.</p>
<p><strong>1. Residual twist measurement.</strong> A defined length of conditioned ribbon is suspended or held under a specified light tension and any rotation is measured. This produces a number that can be trended across lots, which matters far more than the absolute value: a programme whose residual twist trends upward across successive lots is telling you something before any single lot fails a limit.</p>
<p><strong>2. Flat-fold observation.</strong> A length of ribbon is folded back on itself and the fold is released, or the ribbon is laid in a relaxed loop. A balanced ribbon stays in the plane it was folded into. An unbalanced ribbon rotates and will show a visible spiral within a defined period. The observation period should be stated, and for twist-sensitive programmes it should be long enough to be meaningful rather than convenient.</p>
<p><strong>3. Accelerated conditioning.</strong> Conditioning at elevated temperature and humidity accelerates the relaxation that would otherwise take months. This is the single most valuable test in the whole sequence, because it turns a one-year feedback cycle into a one-day one. A bow that holds its shape after an accelerated conditioning cycle is a ribbon that will hold its shape on the shelf. This test should be applied to the actual finished bow, not only to the ribbon, because the tie introduces its own torque.</p>
<p><strong>4. Finished-bow storage simulation.</strong> A sample of finished bows is stored in the packaging configuration in which they will actually ship, under accelerated conditions, and inspected at defined intervals. This is the only test that reproduces the real failure mode, because the failure mode is a property of the assembly plus the environment plus time, not of the ribbon alone. It is also the test that most often exonerates the ribbon and identifies the conversion operation as the source, which is a valuable outcome even though it is unwelcome.</p>
<p>The recommended sequence for a twist-sensitive programme is to run the residual twist and flat-fold checks on the first production lot, to run the accelerated conditioning on the finished bow, and to hold the finished-bow storage simulation open for a defined period as the primary acceptance evidence for the programme. Once a programme has passed that simulation, a lighter recurring regime is sufficient for subsequent lots.</p>"""),

("Buying twist-sensitive ribbon as a programme, not a purchase order",
"""<p>The commercial argument for specifying twist explicitly is that the affected products are the ones where the brand's margin and the brand's reputation live. A gift bow that spirals on the shelf is not a minor cosmetic issue; it is the product failing in the one place where the customer sees it, and it is exactly the kind of defect that generates a photo, a review and a return.</p>
<p>For those programmes, three structural decisions pay for themselves.</p>
<p><strong>Treat the ribbon and the bow as one specification.</strong> Where a brand buys ribbon and has bows made by a converter, the twist requirement, the post-conversion window and the storage simulation should be written into the relationship with both parties, and the evidence should be shared. A converter who knows that the ribbon is twist-sensitive will manage the tie, the tension and the packing accordingly. A converter who has not been told is working to their own habit.</p>
<p><strong>Choose construction over correction.</strong> Where a programme has a persistent twist problem, the tempting response is a chemical finish or a heat-setting adjustment that reduces the torque after the fact. These work, but they add cost and they add a process variable. Choosing the yarn twist direction and the construction so that the ribbon is inherently balanced is cheaper and more stable, and it is a decision made once rather than a control maintained forever.</p>
<p><strong>Run a periodic twist review.</strong> Twist balance is not a property that is guaranteed for the life of a programme. Raw material sources change, a supplier changes a machine, a labour mix shifts, and the balance that was approved two years ago is not necessarily the balance being produced today. A periodic review &mdash; a residual twist measurement and a finished-bow storage simulation on a sample, once or twice a year for a twist-sensitive programme &mdash; is inexpensive and keeps a latent problem from returning as a customer complaint.</p>
<p>None of this requires the buyer to become a textile engineer. It requires the buyer to specify twist in measurable terms, to insist on conditioning before measurement, to test the finished product rather than only the material, and to keep the test in place after the programme has launched. That is a reasonable amount of diligence for a defect that otherwise costs a season of returns.</p>"""),
]

faq282 = [
("What is the difference between S-twist and Z-twist ribbon yarn?",
 "S-twist and Z-twist describe the direction of the helix formed when yarn is twisted. Viewed along the yarn, an S-twist yarn spirals in the same direction as the middle stroke of the letter S, and a Z-twist yarn spirals in the same direction as the middle stroke of the letter Z. The choice is not cosmetic: it determines which way the yarn wants to unwind when the ribbon is cut, folded or tied. In a woven ribbon the yarn twist and the fabric twist should run in the same direction, which produces a balanced ribbon that folds flat and holds a stable bow plane. Opposing them produces an unbalanced ribbon with a tendency to rotate."),
("Why does a ribbon bow spiral or curl after a few months in storage?",
 "The cause is torque memory. Twist in the yarn stores elastic energy, and when a ribbon is folded into a bow one side goes into compression and the other into tension, so the fibres on the tensioned side are inclined to rotate back toward the yarn axis. Over time, and faster in warm or humid conditions, the ribbon gradually adopts the twisted state and the bow's loops rotate relative to each other. The defect is often invisible at goods-in and appears at the point of sale because warmth and retail display lighting accelerate the relaxation. A restrained bow inside a card or bag will not move, which is why the same shipment can produce complaints from some retailers and not others."),
("How do I specify twist direction on a ribbon purchase order?",
 "State four things: the warp yarn twist direction as S or Z, the target twist level in turns per metre or per inch with a tolerance, the required balance state of the finished ribbon expressed in a testable way such as a residual twist limit, and the conditioning condition of temperature, relative humidity and duration before any measurement is taken. Without the conditioning specification the measured figure is not comparable to anything. For twist-sensitive programmes, also add a maximum interval between slitting and bow assembly and a requirement that the finished bow is relax-tested before shipment."),
("Does ribbon twist direction matter for satin and grosgrain specifically?",
 "It matters more for these constructions than for many others. Satin has a long float on the warp, which leaves the warp yarns relatively exposed and more mobile, and grosgrain uses a heavier weft relative to the warp with a pronounced rib. In both cases the balance between the twist of the warp yarns and the effect of the weft is closer to its limit than in a balanced plain weave, so small changes in yarn twist or in the weaving programme show up more clearly as a change in how the fabric lies. If you are specifying a satin or grosgrain for a bow that will be stored rather than used immediately, the twist requirement should be stated explicitly rather than assumed."),
("Can a mill correct a ribbon that untwists, or does it have to be re-made?",
 "It depends on the cause and how far the problem has gone. Finishes and heat-setting treatments can reduce residual torque in the finished ribbon and are a legitimate response to a modest imbalance. But if the underlying cause is that the yarn twist direction opposes the fabric twist direction, the correction is a treatment over a material that will continue to want to move, and the effect degrades with handling and storage. The more durable answer is to change the construction so the ribbon is inherently balanced, which is a decision made at the yarn and weaving stage. Where a programme has a persistent twist problem, ask the mill for a root-cause view rather than accepting a corrective finish."),
("How long should a finished bow be tested for twist stability before a programme is approved?",
 "The meaningful answer is that it should be tested long enough to catch the failure mode, which means it must be accelerated rather than simply long. A storage simulation under elevated temperature and humidity, applied to finished bows in their actual shipping configuration, converts a one-year feedback cycle into a one-day one and is the only test that reproduces the real failure mode because the failure is a property of the assembly, the environment and time together. Residual twist measurement and flat-fold observation on the ribbon are the useful screening tests, but they do not capture the torque introduced by the tie itself. Once a programme has passed an accelerated storage simulation, a lighter recurring regime once or twice a year is sufficient."),
]

art282 = dict(
    slug=("blog-ribbon-oem-282-module-mill-side-brand-buyer-ribbon-yarn-twist-direction-"
          "twist-levelling-interlock-architecture-s-z-twist-torque-memory-balanced-bow-"
          "hang-2026-10-29-pm"),
    title=T282, desc=D282, keywords=K282, section=S282, module=282,
    time_hm="15:00", published_iso="2026-10-29T15:00:00+08:00",
    body_sections=body282, faq=faq282,
)

# ============================================================================
# WRITE ARTICLES
# ============================================================================

for art in (art281, art282):
    html = build_page(**art)
    path = ROOT / f"{art['slug']}.html"
    path.write_text(html, encoding="utf-8")
    print(f"[WROTE] {path.name}  ({len(html)} bytes)")

print("BUILD OK")
