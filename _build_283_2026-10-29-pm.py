#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon article 283 (PM), 2026-10-29.

Module 283: Elastic-Core Thermal Setting & Pre-Shrink Control Interlock Architecture
(anchor/cure setting before dyeing, thermal window, relaxation and re-shrink control
on the elastane core, and how a buyer's pre-shrink % is actually defined and verified).

Follows the established mill-side brand-buyer interlock format:
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
# MODULE 283 — PM
# ============================================================================

T283 = ("Mill-Side Brand-Buyer Elastic-Core Thermal Setting &amp; Pre-Shrink Control "
        "Interlock Architecture &mdash; Anchor Setting, Dyeing Sequence and Re-Shrink "
        "Resistance 2026")

D283 = ("A mill-side brand-buyer guide to elastic-core thermal setting and pre-shrink "
        "control in elasticated ribbon. Covers why pre-shrink percentage is meaningless "
        "without a stated measurement axis and conditioning, why the elastane core must be "
        "anchor-set before dyeing and not after, the narrow thermal window between setting "
        "the core and glazing the face yarn, how relaxation and re-shrink behave after the "
        "core is over- or under-set, and the conditioning protocol that makes a pre-shrink "
        "claim reproducible on both sides of the order.")

K283 = ("elastic ribbon pre-shrink control, elasticated ribbon thermal setting, ribbon "
        "anchor setting before dyeing, elastane core heat setting, ribbon relaxation "
        "measurement, ribbon re-shrink resistance, elastic ribbon shrinkage percentage, "
        "ribbon pre-shrink specification, brand buyer ribbon elastic quality, ribbon "
        "conditioning protocol textile, ribbon heat setting window, elastic ribbon dye "
        "sequence, ribbon dimensional stability elastic, elastic trim manufacturing "
        "process")

S283 = "B2B Sourcing"

body283 = [
("Pre-shrink is a number without an axis, and that is the whole problem",
"""<p>Ask three mills for the pre-shrinkage of the same elasticated ribbon and you will get three numbers. One will be lengthwise, one will be widthwise, and one will be a residual figure measured after a wash the others did not run. All three are defensible. None of them is comparable to the others, and almost none of them answers the question the buyer was actually asking, which is: <em>will this ribbon still fit the same way after it has been washed three times?</em></p>
<p>This is a specification-design problem rather than a manufacturing problem. Pre-shrinkage in an elasticated ribbon is a genuinely multi-variable physical quantity, because the ribbon contains at least two materials with different thermal responses and different relaxation behaviour, and because the answer depends on how you ask the question: which axis, what conditioning, what wash or heat condition, how long, and measured before or after conditioning to a standard atmosphere.</p>
<p>The consequence for a brand buyer is a familiar one. A specification says "maximum 5% pre-shrink". The mill tests it, passes it, and the buyer's converter washes the ribbon at 40 degrees with a specific agitation, and the finished product does not fit. Both parties were technically correct. The number was never defined well enough to be an agreement.</p>
<p>This guide sets out how pre-shrinkage is actually produced in an elasticated ribbon, why the sequence of operations around the elastane core determines whether pre-shrink control is even possible, and how to write a pre-shrink requirement that both a mill and an independent testing laboratory can execute and get the same answer.</p>"""),

("The material stack: two materials, two behaviours",
"""<p>An elasticated ribbon is not one material. It is a composite of at least two, usually three, and the pre-shrinkage of the assembly is the sum of their behaviours, not the behaviour of any one of them.</p>
<p><strong>The elastane core.</strong> Elastane is a physically cross-linked thermoplastic elastomer. Under sustained extension it does not merely stretch; it undergoes a stress-relaxation process in which the network rearranges. That rearrangement is the source of the phenomenon buyers call <em>permanent set</em>, and it is the reason that an elastic ribbon which has been stretched and held will not return exactly to its original width. Elastane also has a defined melting range in the region of 170 to 200 degrees Celsius for most commercial grades, but its practical behaviour at setting temperatures is dominated by its softening and recovery characteristics rather than by the melting point.</p>
<p><strong>The face yarn.</strong> Whatever is wrapped around the core &mdash; polyester, nylon, cotton, a textured yarn, a metallic film for reflective trims &mdash; has its own thermal history. A thermoplastic face yarn will shrink and set when heated. A cellulosic face yarn behaves differently, and reacts badly to the acid and heat of a dye bath in ways a thermoplastic does not.</p>
<p><strong>The interface.</strong> This is where the specification most often loses control. Whether the face yarn is mechanically bound around the core (a woven or knitted wrap), adhesively bonded, or a combination, the bond has its own thermal and dimensional behaviour, and it is the first thing to give when a ribbon is washed at a temperature the elastic core tolerated but the bond did not.</p>
<p>The practical conclusion: <strong>you cannot specify a pre-shrink percentage for an elasticated ribbon without specifying the construction.</strong> A pre-shrink figure attached to a construction description is meaningful. The same figure attached to a colour or a width is not.</p>"""),

("Why the core must be anchor-set before dyeing",
"""<p>The central manufacturing decision in elasticated ribbon is when the elastane core is thermally set relative to the dyeing operation. The sequence is not interchangeable, and the order determines whether the finished ribbon has controlled dimensions or merely controlled dimensions at the moment it left the mill.</p>
<p><strong>Setting after dyeing.</strong> Here the core is relaxed and unconstrained while the face yarn is dyed, and only then is the assembly heated to set the core. The problem is that the dyeing operation itself imposes stress on an unset elastane core: winding tension, liquor circulation, and the handling of the material through the dyehouse all apply load to a core that has not yet been stabilised. When the core is subsequently set, it sets in the state it was left in by the dyeing operation, which is a state that is not reproducible and varies with the dyehouse conditions on the day. Worse, the face yarn has already been dyed, so any dimensional change that occurs during setting will present as a mismatch between the core and the face, visible as waviness, bowing or ribbing across the ribbon width.</p>
<p><strong>Setting before dyeing (anchor setting).</strong> Here the core is thermally set while held at a defined length and width, typically in a stentered and tensioned frame or on a setting machine that controls both dimensions. The core reaches a stable, reproducible state before it ever sees the dyehouse. The face yarn is then dyed around an already-stable core, and any dyehouse stress is applied to a core that has already reached its dimensional equilibrium and will not fight back.</p>
<p>This ordering is the reason anchor-set elastic ribbon behaves predictably and non-anchor-set elastic ribbon does not. It is also the reason a mill with a proper setting operation can quote a pre-shrink figure with a degree of confidence that a mill without one cannot. When you ask a supplier about their elastic ribbon, one of the most discriminating questions you can ask is simply: <em>is the core set before or after dyeing, and how is it held while it is set?</em></p>
"""),

("The thermal window, and what happens outside it",
"""<p>The same heat that sets the elastane core also acts on the face yarn, on the bond and on any finish or coating. The usable window is narrow, and both of its failure modes are common enough that a buyer should know what they look like.</p>
<p><strong>Over-setting.</strong> The core is exposed to more thermal energy than it needs, or for longer than it needs. The elastane network cross-links further than intended. The result is a ribbon that is dimensionally excellent at the roll and that behaves like a plain woven band: it does not recover, the stretch is reduced, and the recovery after a stretch cycle is poor. It will also tend to show a lower shrinkage figure, which is precisely why over-set elastic ribbon can pass a naive pre-shrink test and still fail in the application. This is the most dangerous failure mode in the whole subject, because the quality metric and the functional requirement point in opposite directions.</p>
<p><strong>Under-setting.</strong> The core has not received enough thermal energy to reach a stable cross-linked state. The ribbon looks and measures fine when it is cool and relaxed, but under sustained extension in a warm environment it relaxes further than it should, and it does not return to its original width. The visible symptom is a slowly loosening elastic that no longer performs, often reported by a converter as "the elastic went slack" rather than as a material defect. Under-setting also produces higher residual shrinkage, because the unstabilised core continues to relax over its first weeks in service.</p>
<p><strong>What sits in the middle.</strong> A correctly set core reaches a state where the dimensional behaviour is stable and repeatable, the stretch and recovery are within specification, and the face and bond remain intact. Establishing this is a matter of a temperature and dwell window, a tension or held-dimension constraint, and a cooling step that is part of the process rather than an afterthought.</p>
<p>Two practical consequences. First, the setting window must be validated on each construction, not carried over from the last one: a different face yarn, a different core denier, a different bond route and a different finish all move it. Second, the window has to be recorded, because a buyer who later changes the core supplier needs to know whether the mill re-qualified the setting window or simply ran the old one.</p>"""),

("Relaxation, re-shrink, and the difference that matters",
"""<p>There are two distinct shrinkage behaviours in an elasticated ribbon, and conflating them causes most of the specification disputes.</p>
<p><strong>Pre-shrinkage</strong> is the dimensional change that has already occurred in the material by the time it reaches the buyer: the ribbon as supplied no longer measures what it measured when it left the loom, because the heat and moisture of dyeing, setting and finishing relaxed it. This is a property of the delivered material, and it is what a buyer should be measuring on receipt.</p>
<p><strong>Re-shrinkage</strong> is what happens afterwards, when the material is washed or heat-treated again in the customer's process. It is the residual relaxation that the manufacturing process did not fully remove. The relationship between the two is the whole subject of good pre-shrink control: <strong>a material with a high pre-shrink figure can have excellent re-shrink resistance if the relaxation that caused the pre-shrink was fully stabilised during manufacture</strong>, and a material with a low pre-shrink figure can be badly behaved if the relaxation was simply frozen in by insufficient setting.</p>
<p>This is why a pre-shrink specification that states only a maximum figure is weak. It measures the symptom, not the property. The stronger specification states three things: the pre-shrink figure with its axis and conditioning, the residual re-shrink figure after a defined wash or heat condition, and the recovery behaviour of the core after a defined extension-and-hold cycle.</p>
<p>Relaxation measurement itself needs the same discipline. A ribbon measured immediately off the roll, or measured under tension from a roll core, gives a different answer from the same ribbon after conditioning. The standard approach is to cut a defined specimen, condition it in a specified atmosphere for a specified duration, measure it in a relaxed state, then apply the defined heat or wash condition, re-condition, and measure again. Both results belong in the specification, and the conditioning must be identical on both sides or the numbers are not comparable.</p>
"""),

("Writing a pre-shrink and re-shrink specification that survives contact with reality",
"""<p>A workable elasticated-ribbon dimensional specification has six parts. Each exists to close a specific ambiguity that otherwise becomes an argument.</p>
<ul>
<li><strong>The construction fingerprint.</strong> Name the base yarn and its percentage composition, the elastane type and denier or compression, the binding method (woven wrap, knitted, adhesive, or a stated combination), the total and cut width, the mass per unit length, and the finish route. Pre-shrink cannot be meaningfully transferred between constructions, so this clause is what binds the number to something real.</li>
<li><strong>The axis.</strong> State whether the requirement is lengthwise, widthwise, or both, and separately, because an elastic ribbon can be dimensionally stable in one axis and mobile in the other.</li>
<li><strong>The conditioning.</strong> Give the temperature, the relative humidity and the conditioning duration before the measurement, and require the specimen to be in a relaxed state and not under residual tension from winding or from the measurement apparatus.</li>
<li><strong>The measurement point and the sample size.</strong> How many specimens, taken from how many positions across the roll width and along the roll length, and the rule by which the reported figure is derived. A single measurement from a single point is not a pre-shrink figure.</li>
<li><strong>The re-shrink condition.</strong> The exact wash or heat treatment applied before the second measurement: temperature, duration, agitation if washed, and whether the specimen is dried flat, hung, or at a stated tension. Drying conditions matter because a ribbon dried under tension will read differently from one dried relaxed.</li>
<li><strong>The acceptance rule.</strong> Whether the requirement applies to the mean, to every individual specimen, or to a stated proportion within tolerance, and what the consequence of a failure is at goods-in.</li>
</ul>
<p>Two further clauses earn their place. A <strong>re-test trigger</strong> clause, naming the changes that invalidate the figures &mdash; a change of core supplier or denier, a change of face yarn, a change of binding route, a change of setting route or of dyehouse, and a change of width &mdash; prevents the most common form of drift, which is the slow accumulation of undocumented construction changes. And a <strong>core recovery clause</strong>, specifying the extension and hold used in the recovery test and the percentage of original width recovered after a stated dwell, ties the dimensional figures to the functional property the buyer actually bought.</p>
"""),

("From a mill specification to a garment that fits",
"""<p>The value of all of this is only realised downstream, and it is worth being concrete about where the payoff appears in a brand buyer's own process.</p>
<p><strong>At goods-in.</strong> A buyer who has a defined pre-shrink protocol catches a bad lot at the point of receipt, when the remedy is a replacement and the cost is a credit. A buyer who has not, catches the same lot three weeks later at final assembly, when the remedy is scrapping cut panels and the cost is the entire cut lot plus the labour already spent on it.</p>
<p><strong>At the wash test.</strong> Most converters run some form of wash or steam test on trims before a launch. The number that comes out of that test is only interpretable against a stated baseline. A ribbon that shrinks 4% from its as-supplied state is a different commercial proposition from one that shrinks 4% from a state the buyer never measured, and the difference is entirely in the specification.</p>
<p><strong>On the shelf.</strong> Elastic ribbon that has been under-set loses its recovery progressively in the first months of use, and the garment it is in stops fitting. This is the failure that generates returns rather than complaints, and it is the reason the core recovery clause belongs in the specification even though it is the part buyers are most inclined to leave out.</p>
<p><strong>Across a reorder programme.</strong> The single largest source of dimensional drift across reorder cycles is not a process failure at all. It is that the programme quietly changed something that was never in the specification, and therefore was never re-qualified. A construction fingerprint plus a re-test trigger clause is what prevents that. It also makes a reorder conversation productive, because the question becomes "has anything in the fingerprint changed?" rather than "why does it look different from last time?".</p>
"""),
]

faq283 = [
("What does pre-shrinkage mean for elasticated ribbon?",
 "It means the dimensional change that has already occurred in the material between the loom and the point at which it is supplied, caused by the heat and moisture of dyeing, setting and finishing. It is a property of the delivered material, not a prediction of future behaviour. The important caveat is that a pre-shrink figure is meaningless without three stated conditions: which axis, what conditioning regime the specimen received, and whether the figure is measured before or after the residual re-shrink treatment. Two mills quoting the same number for the same ribbon are frequently measuring different things."),
("Should the elastane core be heat-set before or after dyeing?",
 "Before. Anchor-setting the core while it is held at a defined length and width gives a stable, reproducible thermal state before the ribbon ever enters the dyehouse, so dyehouse stress and handling are applied to an already-equilibrated core that will not fight back. It also avoids the mismatch between a face yarn that has already been dyed and a core that is subsequently set, which presents as waviness, bowing or ribbing across the ribbon width. Setting after dyeing locks in whatever dimensional state the dyehouse happened to leave the material in, which is not reproducible from run to run."),
("How much can an elastic ribbon be over-set without being ruined?",
 "There is no universal figure, because it depends on the elastane grade, the core denier, the face yarn and the binding route. The more useful way to frame it is that over-setting is the failure mode that is most dangerous precisely because it looks good on the metrics that are easiest to measure. An over-set core is dimensionally excellent at the roll and behaves like a plain woven band in service: reduced stretch, poor recovery, and a tendency to look tight. Always require a core recovery figure after a defined extension-and-hold cycle alongside the dimensional figures, because a pre-shrink specification alone will not catch over-setting."),
("What is the difference between pre-shrinkage and residual shrinkage?",
 "Pre-shrinkage is the change that has already happened before you receive the material. Residual shrinkage, or re-shrink, is what happens when the ribbon is washed or heat-treated again in your own process. The commercially important point is that the two can move in opposite directions. A ribbon with a substantial pre-shrink figure can have excellent re-shrink resistance if the mill fully stabilised the material during manufacture, while a ribbon with almost no pre-shrink can be badly behaved if the relaxation was simply frozen in by insufficient setting. That is why a specification stating only a maximum pre-shrink figure is weaker than one that also states the residual figure under a defined wash condition."),
("How should I specify the measurement conditions for pre-shrink?",
 "Give the axis, the specimen size and sampling rule across the roll width and length, the conditioning temperature and relative humidity with the conditioning duration, and the requirement that the specimen be in a relaxed state and free of residual winding tension before measurement. For the re-shrink figure, additionally specify the exact wash or heat condition applied and how the specimen is dried, because a ribbon dried flat, hung, or under tension will read differently from the same ribbon measured relaxed. The conditioning must be identical on both the mill side and the inspection side or the numbers are not comparable."),
("Does changing the elastane supplier invalidate our pre-shrink figures?",
 "Yes, in almost every case, and this is one of the most common sources of drift across a reorder programme. A different elastane grade or denier changes the thermal response of the core and therefore the setting window that stabilises it. That in turn changes both the pre-shrink and the residual re-shrink behaviour, and usually the recovery performance as well. Put a re-test trigger clause into the specification that names a change of core supplier or denier explicitly, alongside changes of face yarn, binding route, setting route, dyehouse and width, so that the decision to re-qualify is triggered by the specification rather than by memory."),
("What should we do if an elastic ribbon lot fails the pre-shrink test at goods-in?",
 "Quarantine the lot and keep a retained sample from the same production run. Then establish whether the failure is in the material or in the measurement, because a conditioning or tension difference between the mill and the inspection laboratory is a common and legitimate cause. Neither party should argue from a single figure without agreeing the protocol first. Once the cause is established, the practical options are a re-test under an agreed protocol, a concession against the re-shrink figure, or replacement. The commercial outcome depends almost entirely on whether the requirement was written with a stated axis, conditioning and acceptance rule, which is precisely the situation in which the dispute does not arise."),
]

if __name__ == "__main__":
    slug = ("blog-ribbon-oem-283-module-mill-side-brand-buyer-elastic-core-thermal-setting-"
            "pre-shrink-control-interlock-architecture-anchor-setting-before-dyeing-thermal-"
            "window-relaxation-re-shrink-resistance-2026-10-29-pm")
    html = build_page(
        slug=slug,
        title=T283,
        desc=D283,
        keywords=K283,
        section=S283,
        module=283,
        time_hm="15:00",
        body_sections=body283,
        faq=faq283,
        published_iso="2026-10-29T15:00:00+08:00",
    )
    out = ROOT / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    import re
    words = len(re.sub(r"<[^>]+>", " ", html).split())
    print(f"[WROTE] {out.name} ({len(html):,} bytes, ~{words} words)")
