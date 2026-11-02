#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate smithribbon articles 289 (AM) + 290 (PM) - 2026-10-31.

289 AM: Mill-Side Ribbon Warp & Yarn Tension Interlock Architecture
        - warp tension uniformity across the loom, warp beam vs fabric beam
        - weft tension vs pick density, tension vs pick-up (weft crimp)
        - tension-driven print registration / width drift / roll build
        - warp tension map and the mill-side tension record

290 PM: Mill-Side Ribbon Dyeing Handoff & Colour Continuity Interlock Architecture
        - the dye house is a separate process from weaving
        - greige yarn vs piece-dyed vs yarn-dyed route selection
        - what changes when the mill changes dyehouse, dye house or yarn lot
        - re-approval triggers and the colour continuity record

Both follow the established house template (288): full meta + OG + Twitter,
BlogPosting + BreadcrumbList + FAQPage JSON-LD, visible FAQ section, CTA, footer.
"""
from pathlib import Path
import json

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-31"
FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")
ORG = "Xiamen Smith Ribbon &amp; Bow Co., Ltd."

CSS = """  body { font-family: 'Segoe UI', system-ui, sans-serif; line-height: 1.8; color: #2a2a2a; max-width: 980px; margin: 0 auto; padding: 24px; background: #fafafa; }
  h1 { font-size: 2.1rem; color: #8b1538; margin-bottom: 0.4em; line-height: 1.3; }
  h2 { font-size: 1.55rem; color: #5a0f25; margin-top: 1.8em; border-left: 4px solid #b8854a; padding-left: 12px; }
  h3 { font-size: 1.25rem; color: #5a0f25; margin-top: 1.4em; }
  .meta { color: #777; font-size: 0.92rem; margin-bottom: 1.6em; padding-bottom: 12px; border-bottom: 1px solid #e0e0e0; }
  .kpi { background: #f0f7f0; border: 1px solid #c8e0c8; border-radius: 6px; padding: 14px 18px; margin: 1.2em 0; }
  .kpi strong { color: #2e6b2e; }
  table { border-collapse: collapse; width: 100%; margin: 1.2em 0; background: #fff; }
  th, td { border: 1px solid #e0d0c0; padding: 10px 12px; text-align: left; font-size: 0.95rem; }
  th { background: #f5ebe0; color: #5a0f25; font-weight: 600; }
  ul, ol { margin: 0.8em 0 0.8em 1.6em; }
  li { margin-bottom: 6px; }
  .cta { background: linear-gradient(135deg, #8b1538 0%, #b8854a 100%); color: #fff; padding: 22px 28px; border-radius: 8px; margin: 2em 0; text-align: center; }
  .cta a { color: #fff; text-decoration: underline; font-weight: 600; }
  .tag { display: inline-block; background: #f5ebe0; color: #5a0f25; padding: 4px 12px; border-radius: 14px; font-size: 0.85rem; margin-right: 6px; }
"""


def slug_words(title):
    import re
    t = title.replace("&mdash;", " ").replace("&amp;", " ")
    t = re.sub(r"[^a-zA-Z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def build(a):
    fn = a["file"]
    url = "https://smithribbon.com/" + fn
    url_noh = url[:-5]
    title = a["title"]
    desc = a["desc"]
    kw = a["keywords"]
    words = a["wordcount"]
    faq = a["faq"]
    body = a["body"]
    pub = a["pubtime"]

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": ans},
            }
            for q, ans in faq
        ],
    }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://smithribbon.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://smithribbon.com/blog.html"},
            {"@type": "ListItem", "position": 3, "name": slug_words(title), "item": url},
        ],
    }

    blogposting = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "image": "https://smithribbon.com/banner.png",
        "datePublished": pub,
        "dateModified": pub,
        "author": {"@type": "Organization", "name": ORG, "url": "https://smithribbon.com"},
        "publisher": {
            "@type": "Organization",
            "name": ORG,
            "url": "https://smithribbon.com",
            "logo": {"@type": "ImageObject", "url": "https://smithribbon.com/banner.png"},
        },
        "mainEntityOfPage": {"@type": "WebPage", "id": url_noh},
        "keywords": kw,
        "wordCount": words,
        "inLanguage": "en-US",
        "articleSection": a["section"],
    }

    faq_html = "\n".join(
        f"<h3>{q}</h3>\n<p>{ans}</p>" for q, ans in faq
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="author" content="{ORG}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url_noh}">
<meta name="msvalidate.01" content="ECF29653135740AB77EEF5074F931DF4" />

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url_noh}">
<meta property="og:image" content="https://smithribbon.com/banner.png">
<meta property="og:site_name" content="SmithRibbon &mdash; Xiamen Smith Ribbon &amp; Bow">
<meta property="article:published_time" content="{pub}">
<meta property="article:modified_time" content="{pub}">
<meta property="article:author" content="{ORG}">
<meta property="article:section" content="{a['section']}">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://smithribbon.com/banner.png">
<!-- JSON-LD: BlogPosting -->
<script type="application/ld+json">
{json.dumps(blogposting, indent=2, ensure_ascii=False)}
</script>

<style>
{CSS}</style>
    <script type="application/ld+json">
{json.dumps(breadcrumb, indent=2, ensure_ascii=False)}
  </script>
<script type="application/ld+json">
{json.dumps(faq_schema, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>

<h1>{title}</h1>
<div class="meta">
  <span class="tag">Ribbon OEM</span>
  Published October 31, 2026 &middot; {ORG} &middot; {a['readtime']} min read
</div>

<p class="lede">{a['lede']}</p>

{body}

<h2 id="faq">Frequently Asked Questions</h2>
{faq_html}

<div class="cta">
  <h3 style="color:#fff;border:none;margin-top:0;">{a['cta_h']}</h3>
  <p>{a['cta_p']}</p>
  <p><strong>Talk to a compliance engineer:</strong> +86 13779951780 (WeChat) &nbsp;|&nbsp; xmmsd@126.com &nbsp;|&nbsp; www.smithribbon.com</p>
  <p><a href="/contact.html">{a['cta_link']} &rarr;</a></p>
</div>

<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>
<p style="font-size:0.9rem;color:#777;margin-top:2em;">Smith Ribbon OEM since 2004 &mdash; woven ribbon, satin, grosgrain, velvet, organza, RPET, printed bows, decorative trims, and private-label accessories for global brand buyers.</p>
</body>
</html>
"""
    (ROOT / fn).write_text(html, encoding="utf-8")
    return fn, len(html.split()), html


# ============================== ARTICLE 289 (AM) ==============================
A289 = {
    "file": ("blog-ribbon-oem-289-module-mill-side-brand-buyer-ribbon-warp-yarn-tension-interlock-"
             "architecture-warp-tension-uniformity-weft-tension-pick-density-crimp-width-drift-"
             "print-registration-roll-build-tension-map-2026-10-31-am.html"),
    "title": ("Mill-Side Brand-Buyer Ribbon Warp &amp; Yarn Tension Interlock Architecture &mdash; "
              "Warp Tension Uniformity, Weft Tension, Pick Density and What They Do to Width, Print and Roll Build 2026"),
    "desc": ("A mill-side brand-buyer guide to warp and yarn tension in ribbon weaving. Covers why warp tension "
             "uniformity across the beam matters more than the average, how weft tension and pick density change "
             "crimp and width stability, why tension is the hidden cause behind print registration drift and "
             "slit-width variation, how the warp beam to fabric beam tension transfer works, and the tension "
             "record that makes a repeat order reproduce the first roll."),
    "keywords": ("ribbon warp tension OEM, yarn tension uniformity ribbon weaving, weft tension ribbon width "
                 "stability, pick density crimp ribbon, warp beam fabric beam tension, ribbon print registration "
                 "drift cause, ribbon width variation loom tension, ribbon roll build tension, ribbon warp "
                 "tension map record, ribbon selvage waviness tension, mill side ribbon tension control, "
                 "ribbon repeat order colour continuity, jacquard ribbon warp tension, grosgrain ribbon tension "
                 "weave, ribbon weaving tension specification, private label ribbon tension approval, ribbon "
                 "weaving quality interlock architecture"),
    "wordcount": 3300,
    "pubtime": "2026-10-31T02:00:00+00:00",
    "section": "Ribbon OEM Manufacturing",
    "readtime": 17,
    "lede": ("Almost every ribbon quality complaint that reaches a brand buyer as a specification problem is "
             "actually a tension problem that was never written down. The colour drifts across the width. The "
             "print runs off register every forty metres. The width on the finished roll measures different "
             "from the width on the roll that was approved. The selvage waves in and out. None of these arrive "
             "with a tension requirement attached, and each of them gets solved downstream with a tolerance, a "
             "rejection, or a change of supplier when the real cause was a warp beam that was under-tensioned at "
             "the edges and over-tensioned in the middle."),
    "cta_h": "Let us put tension on the record for your programme",
    "cta_p": ("Tell us the ribbon construction, the width, the print repeat and the tolerance you are actually "
              "chasing. We will tell you which tension parameters govern it, what the mill-side tension record "
              "looks like for that route, and which acceptance limits are realistic to hold on a repeat order "
              "rather than only on the approved sample."),
    "cta_link": "Request a ribbon tension-control quote",
    "faq": [
        ("Why does warp tension uniformity matter more than the average tension level in a ribbon program?",
         "Because the loom compensates for the average. A warp under uniform tension weaves with a stable width "
         "and a stable pick-up; a warp where some ends are tight and others are loose weaves with a locally "
         "variable structure, and the variation shows up as waviness in the selvage, uneven density across the "
         "width, and a width that changes along the length of the roll. The average can be perfect and the "
         "ribbon can still be inconsistent. This is why a good mill records a tension map across the beam at "
         "set-up rather than only a headline figure, and why 'tension within X percent' is a much more useful "
         "requirement than 'tension maintained at Y'."),
        ("How does weft tension affect the width and the hand of a woven ribbon?",
         "Weft tension determines how tightly the weft yarn is pulled into the structure, which determines the "
         "crimp - the amount the weft yarn has to bend around each warp end - and crimp determines the width of "
         "the fabric. Higher weft tension packs the picks closer together, reduces the crimp of the weft and "
         "usually narrows the width, and gives a denser, firmer hand with less give. Lower weft tension lets the "
         "weft sit straighter across the width, which widens the ribbon and produces a softer, more fluid drape "
         "that many premium programmes want. Because the crimp is a structural property, the weft tension has to "
         "be set to the construction, not adjusted to chase a width target after the fact."),
        ("Is tension the usual cause of print registration drift on a wide ribbon?",
         "Frequently, yes, and it is worth checking before blaming the printing process. A woven ribbon that has "
         "uneven tension across its width will not lie flat; the edges will be slightly longer or shorter than "
         "the centre, and any stretch in the fabric will be taken up unevenly through the nip of the print "
         "rollers. The result is a registration error that grows along the roll rather than staying constant, "
         "which is the signature that distinguishes a tension problem from a roller-setting problem. A quick "
         "diagnostic is to lay the ribbon flat on a table, let it relax for a set period, and check whether the "
         "edges are parallel along the length. If they are not, the cause is upstream of the printer."),
        ("How does tension change between the warp beam and the fabric beam during weaving?",
         "This is the part most buyers have never had explained to them, and it is central to understanding "
         "why a ribbon can change behaviour over the course of a roll. The warp starts on the warp beam under a "
         "defined total tension. As weaving proceeds the warp ends are transferred one by one onto the fabric "
         "beam, and the fabric beam takes up the fabric as it is produced. The two beams do not run at the same "
         "surface speed, and the tension in the individual warp ends changes continuously as the beam diameters "
         "change. A good mill manages this with a controlled take-up and a regular tension check during the "
         "run, because the drifts that appear are cumulative and the middle of a roll is often not the same as "
         "either end."),
        ("How does roll build affect the ribbon, and why does it get worse on wide or heavy qualities?",
         "Roll build is the compression of the wound roll, and it becomes more significant as the ribbon gets "
         "wider, thicker, stiffer or heavier. A roll wound at high tension and low compression can develop a "
         "hard core and a set in the ribbon, so that when the roll is opened the ribbon does not lie flat but "
         "springs in a curve. That stored energy creates the waviness and the width variation that shows up "
         "when the ribbon is slit or wound onto a narrower core. The remedy is controlled winding tension, an "
         "appropriate core and width, and in some cases interleaving or a softer winding for particular "
         "constructions such as velvet and heavier satins. It is worth specifying the winding tension and the "
         "core explicitly for a wide programme."),
        ("What should a tension record actually contain for a ribbon supplier to be accountable to it?",
         "At minimum, the set-up values at which the loom ran the order (total warp tension and the tension map "
         "across the beam, weft tension, pick density, loom speed) and the readings taken during the run rather "
         "than only at set-up. Useful additional entries are the warp beam identification, the weft yarn lot, "
         "the roll identifiers with the roll-level readings, any tension adjustment made during the run and the "
         "reason for it, and the finished roll's measured width at specified positions. The reason to want this "
         "is not paperwork for its own sake: it is the only way to diagnose a repeat-order mismatch, and it is "
         "the difference between a supplier saying the ribbon is within tolerance and a supplier being able to "
         "show which parameter moved."),
        ("Can a brand buyer specify tension directly, or is that a mill-side control?",
         "Directly specifying a tension value in newtons on a purchase order is usually a mistake, because the "
         "meaningful number depends entirely on the yarn count, the construction, the loom and the width, and "
         "two mills quoting the same figure can be describing completely different machines. What a buyer can "
         "and should specify are the outcomes: the finished width tolerance across the roll and across the width, "
         "the flatness and selvage straightness requirement, the print registration tolerance over a stated "
         "repeat length, the density and hand, and the acceptable set or curl after a stated relaxation period. "
         "Those are the properties the mill must hit, and the mill owns the tension parameters that get it "
         "there."),
        ("How do you verify that tension was actually controlled on the ribbon you received?",
         "Three checks, in order of cost. First, the physical one: measure the width at regular intervals along "
         "the roll and at three or more positions across the width, and record whether the figure drifts. Second, "
         "the flatness one: lay a length of ribbon on a flat surface under a light tension, let it relax, and "
         "check the edges for parallelism and the surface for waviness or set. Third, the stress one: compare "
         "the ribbon against a retained sample from the approved lot under the same conditioning. If a supplier "
         "will not release the tension record alongside the shipment, that is worth understanding before the "
         "programme reaches volume rather than after."),
    ],
    "body": """
<h2>Tension Is the Parameter Nobody Writes Down</h2>

<p>Consider a typical ribbon specification a brand buyer sends to a mill. It lists width, construction, material, colour, print and a tolerance on each. It may list weight. It will almost never list anything about tension, because tension is invisible in the finished article and because the buyer has no vocabulary for it yet.</p>

<p>And yet tension governs more of the ribbon's behaviour than any other single variable. It governs whether the width is stable along the roll. It governs whether the selvage runs straight or waves. It governs the density and therefore the hand and the drape. It governs whether a print stays in register for forty metres or drifts out by the tenth. It governs how much the ribbon relaxes when it comes off the roll, which is the property that determines whether a bow sits flat or springs. A ribbon that fails any of these does so because of tension, and the failure gets attributed to a tolerance that was written badly, a mill that is inconsistent, or a material that was not quite right.</p>

<p>The purpose of this module is to make tension discussable. Not as a number the buyer imposes on the mill, but as a set of relationships between mill-side parameters and brand-side outcomes, so that when something drifts, both sides know where to look and both sides know what should have been recorded.</p>

<h2>Warp Tension: The Uniformity Is the Point</h2>

<p>A ribbon loom runs a number of warp ends across the width. Each end has its own tension, and those tensions are not equal. The warp beam is prepared under a defined total tension, but the distribution across the width depends on how the beam was built, how the ends were distributed and sized, and how the loom's tension control system distributes the load.</p>

<p>The critical insight for a buyer is that <strong>the loom reacts to the average, but the ribbon inherits the variation</strong>. A warp whose average tension is exactly on target can still produce an inconsistent ribbon if the individual ends differ from each other. That is what produces the characteristic defects: the edges of the ribbon sitting differently to the centre, the selvage waving in and out, the density varying across the width so that one side of a printed ribbon carries more ink than the other, and a width that is not simply narrow or wide but <em>variable</em>.</p>

<p>Good mill practice is to record a tension map across the beam at set-up rather than a single headline figure, and to check it again during the run as warp ends are transferred to the fabric beam. The buyer should ask for that map. The specification should say something like 'warp tension to be uniform across the beam within an agreed band, evidenced by a set-up tension map', rather than attempting to impose a newton figure that means nothing outside the mill's own machine.</p>

<div class="kpi">
  <p><strong>What a warp tension map should show a buyer:</strong></p>
  <ul>
    <li>Individual end tension readings across the full width at set-up</li>
    <li>The spread between the highest and lowest reading, expressed as a percentage of the mean</li>
    <li>A second map taken mid-run, because tension drifts as the run proceeds</li>
    <li>The mill's action if the spread exceeds the agreed band</li>
  </ul>
  <p>The spread is the number that matters. The mean is a set-up parameter.</p>
</div>

<h2>Weft Tension, Pick Density and the Width Question</h2>

<p>Weft tension is the second half of the story, and it is the half that explains why a ribbon's width and its hand are linked in a way that is not obvious until you see it.</p>

<p>When the shuttle or rapier inserts a weft yarn, that yarn has to be pushed against the previous pick. If the weft tension is high, the weft is pulled tight and sits with a deep crimp &mdash; it has to bend around each of the warp ends it crosses. Deep crimp consumes length of weft yarn, and the width of the fabric shrinks to accommodate it. The result is a narrower, denser, firmer ribbon with less give and a more structured hand.</p>

<p>If the weft tension is lower, the weft lies straighter across the width with less crimp. The ribbon comes off the loom wider, more open, softer, with a more fluid drape and more sheen in the case of a satin construction, because the flattened filament surface is less distorted. For a programme that is chasing an elegant fall on a gift bow, this is a meaningful design lever and it is one of the few places where the buyer can genuinely influence the tactile outcome without changing material.</p>

<p>Pick density &mdash; the number of weft picks per centimetre &mdash; works the same way. Higher density packs more weft into the same length, increases crimp, narrows the fabric and increases weight per metre. It also increases the number of ends the mill has to manage, which affects cost and lead time.</p>

<p>Here is the trap: if a buyer specifies a finished width and a density separately and the mill satisfies both by adjusting tension, the mill may be fighting itself, because the two are physically coupled. A better specification states the relationship explicitly &mdash; '12 mm finished width at 32 picks per centimetre, achieved at the mill's standard weft tension for this construction' &mdash; and then constrains the outcomes that matter (hand, drape, width stability along the roll) rather than the internal setting.</p>

<h2>The Beam Transfer: Why the Middle of a Roll Is Not the Ends</h2>

<p>Here is a mechanism that explains more real-world surprises than any other, and it is worth understanding even at a conceptual level.</p>

<p>The warp begins on the warp beam. As weaving proceeds, warp ends are transferred one at a time onto the fabric beam, which accumulates the finished fabric. The warp beam and the fabric beam do not rotate at the same surface speed, and both change diameter as the run proceeds. The net effect is that the tension in the individual warp ends is not constant over the length of a roll. It is typically highest at the start of the run, settles as the run proceeds, and drifts again as the fabric beam fills and its effective radius changes.</p>

<p>The practical consequences are these. A ribbon approved from the first fifty metres of a roll may not represent the middle of the same roll. A roll that was acceptable at set-up may relax differently at the core. A high-tension zone at the start produces a roll with a hard set that gets worse the longer it ages, and a slack zone produces width variation that a buyer will see as the roll unwinding and the ribbon lying unevenly on the table.</p>

<p>This is why 'roll-level' data beats 'batch-level' data. A good mill records measurements at defined positions along the roll, not just at the start, and a good specification asks for width readings at the beginning, the middle and the end of the roll, along with the roll identifiers. It is also why roll-build management matters: the tension at which the fabric is wound onto the fabric beam, and then onto the core, determines how much of that variation gets locked into the roll.</p>

<h2>What Tension Does to Print Registration</h2>

<p>Print registration on a woven ribbon is a mechanical problem before it is an ink problem, and tension is usually the upstream cause when registration drifts along the length of a roll.</p>

<p>A ribbon with uneven tension across its width does not lie flat. Its edges sit at slightly different lengths from the centre, and the fabric carries a small amount of stretch that is not uniformly distributed. Through the nip of the print rollers, that non-uniform stretch is taken up unevenly, and the printed image shifts relative to the web. Because the stretch distribution changes along the roll as the beams turn, the registration error is not constant &mdash; it grows, or it drifts, and the printer will compensate for it if it can, which makes the problem look intermittent and confusing.</p>

<p>The distinguishing signature of a tension-driven registration problem is that the error changes along the roll. A roller-setting problem, by contrast, tends to produce a consistent offset in one direction across the entire run. When a printer reports that registration drifts, the first diagnostic worth doing is physical rather than technical: lay the ribbon flat, allow it to relax, and check whether the edges are parallel along the length. Non-parallel edges mean the problem is upstream in the weave, and no amount of roller adjustment will fix it properly.</p>

<div class="kpi">
  <p><strong>Four tension-driven defects and their signatures:</strong></p>
  <ul>
    <li><strong>Registration drift along the roll</strong> &mdash; error changes with length; edges non-parallel when laid flat</li>
    <li><strong>Width variation along the roll</strong> &mdash; beats appear in the width readings at intervals</li>
    <li><strong>Selvage waviness</strong> &mdash; edge undulates in and out; causes fraying and print misalignment at the edge</li>
    <li><strong>Set and curl on unwinding</strong> &mdash; ribbon springs into a curve; usually roll-build tension</li>
  </ul>
</div>

<h2>Width Stability: The Property That Predicts the Repeat Order</h2>

<p>Width is the one specification every buyer checks, and it is also the one most often written in a way that makes it impossible to verify. A width tolerance expressed as a single band across the whole roll tells you nothing about whether the ribbon will be stable enough to slit, to wind onto a narrow core, or to convert into a bow where the loop has to be symmetrical.</p>

<p>A useful width specification is three-dimensional rather than one-dimensional. It needs a <strong>nominal</strong> and a tolerance, which is the obvious part. It needs a <strong>position requirement</strong>: width measured at specified intervals along the roll, so that variation along the length is constrained rather than averaged away. And it needs a <strong>cross-width requirement</strong>: width measured at several positions across the ribbon, so that the left edge and the right edge are constrained relative to the centre. A ribbon that meets a single-point tolerance can still be substantially out of square across its width, and out-of-square ribbon is what makes a bow loop asymmetric.</p>

<p>This connects directly to the slitting question. A ribbon that is width-stable on the loom but is cut from a roll that was wound with high tension will still vary once it is slit, because slitting releases the compressive set stored in the roll. This is why a slitting tolerance and a wound-roll specification have to be written together, and why the release protocol for a wide programme should include a check on the finished roll after a defined relaxation period rather than immediately after winding.</p>

<h2>Roll Build, Winding Tension and the Set That Appears Later</h2>

<p>Roll build is where a good ribbon becomes a problem, and it is a discipline of its own.</p>

<p>Winding too tightly creates a dense roll with a hard core and stores energy in the ribbon. Weeks later, when the customer opens the carton, the ribbon does not lie flat &mdash; it curves, or it takes a set along its length, and it will not behave in the converting process. Winding too loosely creates a soft roll that collapses, shows edge damage, and can telescope in the carton. For a wide or heavy quality, the practical variables are the winding tension, the core diameter and material, the number of layers per carton, and the compression applied to the packaged roll.</p>

<p>Some constructions are more sensitive than others. Velvet and flocked ribbon, which has significant pile, needs a specific approach because the pile direction and the pile height respond to compression in a way that a flat ribbon does not. Metallised and holographic ribbon is vulnerable to set because its stiffness means it holds a curve strongly. Heavy satins and wide jacquards store more energy and benefit from interleaving or a softer winding. Elasticated ribbon has its own behaviour, because the elastic core recovers over time and the wound roll can develop a set that changes the effective stretch.</p>

<p>The specification a buyer should ask for is modest and specific: the winding tension band or the compression target, the core specification, the maximum roll length and weight, and the relaxation period after which the flatness requirement is assessed. A mill that controls roll build well can take a programme with tighter tolerances downstream; a mill that does not will limit what every subsequent operation can achieve.</p>

<h2>What to Specify, What to Ask For, What to Verify</h2>

<p>The practical structure of a tension conversation between a brand buyer and a mill has three layers, and it is worth being explicit about which layer each party owns.</p>

<p><strong>The buyer specifies outcomes.</strong> Finished width nominal and tolerance, with position and cross-width requirements. Flatness and selvage straightness. Print registration tolerance over a stated repeat length. Density, weight per metre and hand. Selvedge treatment. Acceptable set or curl after a stated relaxation period. Winding tension or roll compression, core specification and maximum roll weight. These are all things the mill can be held to, and none of them requires the buyer to understand a loom.</p>

<p><strong>The mill controls parameters and records them.</strong> Warp tension and the uniformity map across the beam, weft tension, pick density, loom speed, warp beam identity, weft yarn lot, roll-level readings along the run, and any in-run adjustment with its reason. The mill owns these and should be able to produce them on request.</p>

<p><strong>Both verify on receipt.</strong> Width measured at intervals along the roll and across the width. Flatness check on a relaxed length. Comparison against the retained sample under the same conditioning. On a repeat order, comparison of the tension record against the previous order's record before the goods are accepted, not after.</p>

<div class="kpi">
  <p><strong>Tension specification checklist &mdash; eight clauses</strong></p>
  <ul>
    <li>Width nominal and tolerance, with measurement positions along the roll</li>
    <li>Cross-width width requirement at three or more positions</li>
    <li>Selvage straightness and flatness after a stated relaxation period</li>
    <li>Print registration tolerance over a stated repeat length</li>
    <li>Density (picks per centimetre) and weight per metre</li>
    <li>Winding tension or compression target, and the core specification</li>
    <li>Requirement for a set-up warp tension map and mid-run re-check</li>
    <li>Roll-level measurement record supplied with the shipment</li>
  </ul>
</div>

<h2>Why This Matters More in Repeat Orders Than in First Orders</h2>

<p>The first order is a sample conversation. The buyer looks at a ribbon, approves it, and the mill weaves it. The interesting part of the relationship begins with the second order, when the buyer expects the same ribbon and the mill has to reproduce a result that depends on a dozen interacting parameters that were never written down.</p>

<p>This is where a mill with good records separates itself from one without. A mill that keeps a tension record, a yarn lot record and a roll-level measurement record can answer the question 'why is this batch different from the approved one' with a diagnosis. A mill that does not can only answer 'we wove it the same way', which is not an answer, because nothing about weaving is the same way unless it is controlled.</p>

<p>It is worth noting what this means commercially. The cost of the tension discipline is process control and paperwork that a mill absorbs. The benefit lands on the buyer as reduced variation, fewer incoming rejections, fewer colour and registration complaints that reach the customer, and the ability to scale volume without the quality drifting as the order gets larger and the production schedule gets tighter. For a brand that is about to grow a programme from one SKU to thirty, that difference is what determines whether the brand stays with the mill or starts qualifying a second one.</p>

<p>At Smith Ribbon, in Xiamen since 2004, we control and record loom tension as part of the production file for every branded programme, and we will walk you through the parameters behind the ribbon you have approved. We would rather set these expectations at the sample stage than at the third repeat order, because a tension specification written then costs nothing and a tension specification written after a complaint costs a great deal.</p>

"""
}


# ============================== ARTICLE 290 (PM) ==============================
A290 = {
    "file": ("blog-ribbon-oem-290-module-mill-side-brand-buyer-ribbon-dyeing-handoff-colour-continuity-"
             "interlock-architecture-greige-piece-dye-yarn-dye-route-dyehouse-change-dye-lot-approval-"
             "retrigger-revalidation-2026-10-31-pm.html"),
    "title": ("Mill-Side Brand-Buyer Ribbon Dyeing Handoff &amp; Colour Continuity Interlock Architecture "
              "&mdash; Greige, Piece-Dye and Yarn-Dye Routes, Dyehouse Change and the Re-Approval Trigger 2026"),
    "desc": ("A mill-side brand-buyer guide to colour continuity across the dyeing process in a ribbon "
             "programme. Covers how greige yarn, piece-dye and yarn-dye routes differ in what they fix and what "
             "they leave open, why the dyehouse is a separate controlled process from the loom, what actually "
             "changes when a mill moves dyehouse, dye supplier or yarn lot, how colour approval should be "
             "revalidated, and the dyeing record that makes a repeat order match the first one."),
    "keywords": ("ribbon dyeing colour continuity OEM, greige yarn piece dye yarn dyed ribbon route, ribbon "
                 "dyehouse process control, ribbon dye lot management, ribbon colour approval revalidation, "
                 "ribbon colour matching repeat order, piece dyed ribbon colour consistency, yarn dyed ribbon "
                 "bulk dyeing advantage, ribbon dyeing shade variation cause, ribbon lab dip to bulk dye "
                 "approval, ribbon dyehouse change management, ribbon wet processing quality risk, ribbon "
                 "colour fastness after dyeing, private label ribbon colour locking, ribbon dyed versus "
                 "printed colour, mill side ribbon dyeing record, ribbon dyeing interlock architecture"),
    "wordcount": 3200,
    "pubtime": "2026-10-31T07:00:00+00:00",
    "section": "Ribbon OEM Manufacturing",
    "readtime": 16,
    "lede": ("A ribbon that was approved at the lab dip and then arrives a shade away from the approved sample "
             "is rarely a dyehouse problem in the way people usually mean it. It is almost always a handoff "
             "problem. The colour was decided on one process, the ribbon was woven on another, the piece was "
             "dyed on a third, and the four decisions that actually determine whether the colour repeats &mdash; "
             "which route, which dyehouse, which dye lot, which approval &mdash; were each made separately and "
             "none of them were written into the specification the buyer holds."),
    "cta_h": "Let us lock the colour route before the first bulk order",
    "cta_p": ("Tell us the colour, the quantity, the construction and the tolerance you need to hold across "
              "repeat orders. We will set out which dyeing route fits that requirement, what the approval and "
              "re-approval sequence should be, what a change of dyehouse or yarn lot would mean for your "
              "programme, and which records we keep so the colour is defensible six orders later."),
    "cta_link": "Request a ribbon dyeing-route quote",
    "faq": [
        ("What is the difference between greige, piece-dyed and yarn-dyed ribbon, and which is best for "
         "colour consistency?",
         "Greige ribbon is woven from undyed yarn and dyed after weaving, as a finished piece. Piece dyeing "
         "gives the greatest flexibility: you can dye to any shade from a single greige base, small quantities "
         "of a new colour cost very little, and colour changes are easy. The trade-off is that every piece is "
         "dyed individually or in small lots, so there is more handling, more exposure to shade variation "
         "between dye lots, and the colour is only locked in after the piece is finished. Yarn-dyed ribbon has "
         "the colour in the yarn before weaving, which gives excellent batch-to-batch consistency because "
         "the dye lot is continuous and uniform, but it requires the shade to be decided and the yarn dyed in "
         "quantity before weaving, so a new colour carries a much larger minimum commitment. For a brand with "
         "a locked core palette in volume, yarn dyeing usually gives the best consistency. For a brand testing "
         "colours in small quantities, piece dyeing gives the flexibility and the colour must simply be "
         "controlled more tightly."),
        ("Why does the dyehouse need to be treated as a separate controlled process from the loom?",
         "Because the two processes have completely different failure modes and completely different quality "
         "levers, and because most of the variables that affect the final colour are set before a single metre "
         "of ribbon is woven. Yarn dyeing sets the colour in the yarn. Piece dyeing sets it in the finished "
         "web. Printing sets it on the surface. Each has its own bath chemistry, its own temperature profile, "
         "its own time and agitation, its own preparation steps, and its own tolerances. A ribbon that is "
         "correctly woven and then badly dyed fails, and so does a badly woven ribbon that is correctly dyed. "
         "Specifying the construction and the colour in the same document does not mean the two processes can "
         "be managed as one."),
        ("What actually changes when a mill moves its dyeing to a different dyehouse?",
         "More than most people assume. A different dyehouse means a different machine, a different water "
         "supply, a different dye chemistry available, a different operator team, and a different set of "
         "standard recipes. The dyehouse's water is a genuine variable: hardness, mineral content and "
         "conductivity affect dye uptake and shade, and two dyehouses drawing from the same municipal supply "
         "can still behave differently if one treats its water and the other does not. Different equipment "
         "means different bath ratios, different heating and cooling rates, and different rinsing behaviour. "
         "The result is that a colour that was reproducible in the original dyehouse becomes a new colour to "
         "re-develop. A change of dyehouse is therefore not a continuity event, it is a re-approval event, and "
         "it should be handled as one."),
        ("What should trigger a colour re-approval, and what should not?",
         "A re-approval should be triggered by anything that can plausibly move the final shade: a change of "
         "dyehouse or dyeing equipment, a change of dye supplier or dye product, a change of yarn supplier or "
         "yarn lot for the same article number, a change of pretreatment or finishing route, a significant "
         "change in batch size, or a change in the finishing route such as heat-setting parameters. It should "
         "not be triggered by a repeat order of the same construction in the same dyehouse with the same yarn "
         "lot and the same recipe. The reason this matters is that re-approving everything on every order "
         "destroys the value of the approval and gets ignored by everyone, while re-approving nothing until "
         "the customer complains is the failure mode this whole module exists to prevent."),
        ("Why does an approved lab dip not guarantee an approved bulk dye?",
         "Because a lab dip is typically a small hand-dyed sample using a slightly different process from the "
         "production machine: a different bath ratio, a different dyeing temperature, a different dwell time, "
         "a different agitation and often a different pretreatment. Scale-up changes the mass and heat "
         "transfer characteristics of the bath, and it changes the ratio of dye to substrate, so a shade that "
         "is achievable in a small beaker can be difficult to hit and hold in a full machine. The correct "
         "sequence is therefore a defined progression: lab dip to confirm the recipe is feasible, then a "
         "production trial or pre-production lot on the actual machine, then the bulk lot, with the bulk lot "
         "assessed against a tolerance to the approved reference rather than against the lab dip. The frequent "
         "error is skipping the middle step and comparing bulk directly to the lab dip, which makes a correct "
         "batch look wrong."),
        ("How should colour tolerance be specified so it is actually verifiable?",
         "With an instrumented measurement and a stated conditioning, not with a visual judgement. The usual "
         "approach is a spectrophotometer reading under a defined illuminant and observer angle, on samples "
         "that have been conditioned to a specified temperature and relative humidity, expressed as a delta-E "
         "figure against the approved standard with a stated tolerance band. The measurement conditions matter "
         "as much as the number: a ribbon that is slightly warm when it comes off the machine and cools in the "
         "warehouse will read differently from the same ribbon measured the next morning, and a textile has "
         "moisture in it that shifts the reading. For many brands a delta-E tolerance around 1.0 to 1.5 is "
         "reasonable for a solid shade and tighter is unrealistic without a formal colour management system "
         "on the buyer's side as well."),
        ("What is the colour record a mill should be able to produce on request?",
         "A set that lets the colour be reproduced rather than merely described. It should include the approved "
         "standard with its instrument readings, the dye recipe with the dye products, concentrations and "
         "process parameters, the dye lot numbers used, the yarn lot and the pretreatment route, the batch "
         "records with bath ratio, temperature profile and dwell time for each production batch, the "
         "instrument readings for each batch, and the retained samples from each batch. The retained samples "
         "are the ones buyers most often forget to ask for and most often need: they are what makes it "
         "possible to answer a question eighteen months later about why the batch from March differs from the "
         "one from September."),
        ("Does piece-dyed ribbon need a different colour approval process from printed ribbon?",
         "Yes, and the reason is worth understanding because the two are often handled with the same paperwork "
         "despite behaving very differently. Printing applies colour to the surface of a finished ribbon, so "
         "the substrate's own colour, texture and absorbency all influence the result, and the printed colour "
         "is only as stable as the print's own fastness and adhesion. Dyeing puts the colour into the fibre, "
         "which generally gives much better fastness and a more homogeneous appearance, but it means the "
         "colour is a property of the whole ribbon rather than a layer on it. In practical terms, a printed "
         "ribbon's colour approval is tied to the substrate and the print route together, while a dyed "
         "ribbon's approval is tied to the dyeing route and the yarn. They need different records and, where "
         "both are used on the same product, they need to be checked against each other at assembly."),
    ],
    "body": """
<h2>Colour Is Decided Before Weaving Starts</h2>

<p>The most common misunderstanding in ribbon sourcing is that colour happens at the end. It does not. By the time a printed or dyed ribbon is on a roll and visible, the decisions that determine whether that colour repeats for two years have already been made &mdash; sometimes months earlier, in a meeting between a buyer and a mill that was never written down.</p>

<p>Those decisions are: which colour route the programme will use (greige, piece-dyed, yarn-dyed, or printed), which dyehouse and which machine will run the colour, which yarn lot will carry it, which recipe will be used, and what standard the bulk will be assessed against. Each of them is a source of variation. Get all five stable and colour is boring and repeatable. Change any one of them and the colour becomes a new colour to be re-developed, whether or not anyone notices at the time.</p>

<p>This module is about those five decisions and the interlock between them. It is deliberately structured around the buyer's actual problem: the approved colour does not repeat, and nobody can say why.</p>

<h2>The Three Routes, and What Each One Fixes</h2>

<p><b>Greige and piece-dyed.</b> The ribbon is woven from undyed yarn and dyed after weaving. This is the most flexible route and the most common starting point for a new programme, because a single greige base can be dyed into any shade, and a new colour in small quantity is inexpensive to trial. The colour is decided at the dyeing stage, which means the artwork is not the constraint.</p>

<p>What piece dyeing does not fix is consistency. Every piece is a separate dye lot, and between lots there is variation in bath chemistry, in the condition of the machine, in the water, in the pretreatment and in the operator's technique. This variation is manageable and a good mill manages it well, but it has to be managed actively. It cannot be assumed.</p>

<p><b>Yarn-dyed.</b> The yarn is dyed before weaving. This is the route for consistency, and the reason is structural: the dye lot is continuous and uniform, so every metre of ribbon woven from it carries essentially the same colour. For a brand with a locked core palette in real volume, this is the strongest answer to the repeat-order problem, and it is also the route that gives the most predictable results in bulk dye fastness.</p>

<p>The trade-off is commitment. The shade has to be decided and the yarn dyed in quantity before weaving begins, so the minimum for a new colour in yarn-dyed is substantially higher than for a piece-dyed trial. For a brand that is still exploring a colour, that is a real barrier; for a brand that has settled on a colour and will order it for years, it is the cheapest quality per metre in the programme.</p>

<p><b>Printed.</b> The colour is applied to the surface of the finished ribbon. Printing gives the widest design range and the tightest control over a specific artwork or logo, and it allows a small quantity in an arbitrary colour. But the printed colour sits on the substrate rather than in it, so it inherits the substrate's own colour and texture, it has its own adhesion and fastness questions, and its consistency depends on the printing route as much as on the colour itself.</p>

<p>There is also the hybrid case that many programmes actually use: a dyed base with a printed motif, or a printed ribbon with a dyed selvedge. These are common and perfectly workable, but they need two approval records rather than one, and the interaction between them &mdash; does the print sit on the dyed ground or fight with it &mdash; is worth checking explicitly rather than discovering at assembly.</p>

<div class="kpi">
  <p><strong>Route selection, at a glance:</strong></p>
  <ul>
    <li><strong>Piece-dyed</strong> &mdash; maximum flexibility, lowest entry commitment, needs the tightest dye-lot control</li>
    <li><strong>Yarn-dyed</strong> &mdash; best batch-to-batch consistency, highest entry commitment per colour</li>
    <li><strong>Printed</strong> &mdash; arbitrary artwork and colour, smallest quantities, colour lives on the surface</li>
    <li><strong>Hybrid</strong> &mdash; dyed ground with printed motif, requires two approval records and an interaction check</li>
  </ul>
</div>

<h2>The Dyehouse Is a Controlled Process, Not a Service</h2>

<p>The single most consequential thing a buyer can do is insist that the dyehouse is treated as a controlled process with the same seriousness as the loom.</p>

<p>A dyehouse has its own variables, and they are not the loom's variables. There is the bath ratio: the volume of water per kilogram of goods. There is the temperature profile: how fast the bath is raised to temperature, how long it is held, and how it is cooled. There is the dwell time at temperature. There is the agitation, which determines whether the bath stays uniform and whether the piece does not tangle or abrade. There is the pretreatment: scouring, bleaching, mercerising, or simply nothing. There is the rinse regime, which determines how much unfixed dye is carried forward. There is the sequence of additions, which for a particular shade may require the light and the dark components to go in at different times.</p>

<p>And there is the water. This is the variable buyers underestimate most. Dye uptake in a polyester or nylon ribbon depends on the pH, the ionic strength and the mineral content of the water in the bath. A dyehouse drawing from a municipal supply and treating that water will behave differently from one drawing from the same supply without treatment, and two dyehouses in different cities will have genuinely different water. This is why moving a programme between dyehouses is a serious event rather than a logistical one.</p>

<p>None of this is exotic, and none of it is exotic to a competent dyehouse. The problem is that it is invisible from the outside. A buyer who has visited the loom but not the dyehouse has seen half the process, and the half that determines the colour.</p>

<h2>What Changes When the Dyehouse Changes</h2>

<p>When a mill moves dyeing to a different facility, or brings dyeing in-house from a subcontractor, the honest position is that the colour has to be re-developed. Not because anyone did anything wrong, but because the variables listed above have all changed at once.</p>

<p>A new dyehouse means new equipment, which means new bath ratios, new heating and cooling behaviour and new rinsing. It means a new operator team learning the recipes, which means a period of settling-in during which the shade drifts as the team finds its rhythm. It means a new water supply. It may mean a different range of dyes is available, which can mean the recipe itself has to be re-derived rather than simply re-run, because the new dyehouse may not stock the same product at the same concentration.</p>

<p>In practice, the mill that handles this well will: run the existing recipe on the new equipment at the new bath ratio as a first check; treat the first production batch as a trial batch and assess it against the approved standard with the same instrument; hold the batch pending a colour decision rather than shipping it; and only release further batches once the mill and the buyer have both signed off that the shade has been re-established.</p>

<p>That process takes time and it is genuinely inconvenient, which is exactly why it needs to be anticipated rather than absorbed. A buyer who learns about it after the goods have shipped has no lever left. A buyer who knew it was coming can build the re-approval into the schedule, and a buyer who has specified the colour route, the dyehouse and the yarn lot in the programme documentation can at least tell whether a change has occurred.</p>

<h2>The Re-Approval Trigger List</h2>

<p>Re-approval discipline is what keeps a colour programme stable over years, and it works in both directions: it stops the mill shipping unreviewed changes, and it stops the buyer from being asked to re-approve everything every time.</p>

<p><strong>Triggers that require re-approval:</strong></p>

<ul>
  <li>Change of dyehouse or dyeing equipment</li>
  <li>Change of dye supplier, dye product or dye concentration basis</li>
  <li>Change of yarn supplier for the same article number, or a yarn lot change that moves the fibre characteristics</li>
  <li>Change of pretreatment, scouring or bleaching route</li>
  <li>Change of finishing route or of significant heat-setting parameters after dyeing</li>
  <li>Batch size moving materially outside the range on which the shade was established</li>
  <li>Any change in the build that alters the ratio of dye to substrate, such as a fabric weight or construction change</li>
</ul>

<p><strong>Events that do not require re-approval:</strong></p>

<ul>
  <li>A repeat order in the same construction, same dyehouse, same recipe, same yarn lot</li>
  <li>A normal batch-size variation within an agreed range</li>
  <li>Seasonal or ambient variation inside the established range, with the record showing it</li>
</ul>

<p>The reason the second list matters is that a re-approval regime which fires on every order stops being a control and becomes a rubber stamp. The buyer learns to sign without reading, the mill learns that the process does not need to be described accurately, and the value of the whole exercise evaporates. A trigger list that names the specific events, reviewed periodically against what actually changes in the programme, is what keeps it real.</p>

<h2>Why the Lab Dip Is Not the Approval</h2>

<p>The lab dip has a specific and limited role: it confirms that a recipe is feasible and roughly on target. It is a small sample, usually hand-dyed in a beaker or a small vessel, and the process parameters are necessarily different from production.</p>

<p>The bath ratio in a lab dip is small enough that the ratio of dye to substrate differs from production. The heating rate is different, because a small vessel heats fast and a production machine heats slowly and evenly. The agitation is different. The pretreatment is often more rigorous in the lab than in production. None of these differences are mistakes; they are simply what a small-scale dye is. And they mean a lab dip that looks exactly right on the bench can be impossible to reproduce at scale, or can be reproducible only after a small correction that the lab could not have predicted.</p>

<p>The sequence that works is therefore a three-step progression with an assessment against a fixed reference at each step:</p>

<ol>
  <li><strong>Lab dip</strong> &mdash; confirms the recipe is feasible and approximately on target</li>
  <li><strong>Production trial or pre-production lot</strong> &mdash; the same recipe on the actual machine, assessed against the approved standard and corrected if needed</li>
  <li><strong>Bulk lot</strong> &mdash; assessed against the approved standard with an instrument, and against the trial lot for consistency</li>
</ol>

<p>The most common error is skipping step two and assessing bulk directly against the lab dip. A correct bulk batch then looks wrong, gets rejected, and triggers a dispute about which sample was right &mdash; when in fact both were right and they were being compared against each other rather than against a common standard.</p>

<h2>Measuring Colour So It Is Verifiable</h2>

<p>A colour approval that is signed off by eye will drift, because human colour judgement in different lighting conditions on different days is genuinely inconsistent, and because the person doing the approving at the mill is not the person doing the accepting at the buyer's warehouse.</p>

<p>The instrumented approach is straightforward. A spectrophotometer reading under a defined illuminant and observer angle, on a sample conditioned to a specified temperature and relative humidity, expressed as a delta-E figure against the approved standard, with a stated tolerance band. The details matter more than people expect:</p>

<ul>
  <li><strong>Conditioning.</strong> A textile holds moisture, and moisture shifts the reading. A sample measured hot off the machine and the same sample measured the next morning will not give the same number. Condition before measuring, every time, or the number is noise.</li>
  <li><strong>Illuminant and observer.</strong> Daylight and tungsten give different results. State which is used; the industry default is typically D65 with a 10-degree observer for most textile work, but it needs to be stated.</li>
  <li><strong>Direction.</strong> A woven ribbon is not optically symmetric in every direction, and the reading position on the ribbon matters. A consistent measurement position &mdash; a defined point on the width, in the machine direction &mdash; removes a variable that otherwise produces phantom drift.</li>
  <li><strong>Tolerance band.</strong> For a solid shade, a delta-E tolerance in the region of 1.0 to 1.5 is generally reasonable. Tighter than that is unrealistic without a formal colour management system on the buyer's side as well, and setting an unachievable tolerance guarantees a dispute rather than a better colour.</li>
  <li><strong>Sample count.</strong> More than one reading per lot, at defined positions across the width and along the length, so that the assessment reflects the lot rather than one convenient spot.</li>
</ul>

<p>One caution worth stating: colour management systems exist to make the whole chain consistent, and they work. But a colour management system cannot create consistency that the process does not have. It standardises the measurement and the communication. If the dyehouse is producing genuine lot-to-lot variation, a spectrometer will simply document it more precisely than an eye would have.</p>

<h2>The Colour Record and Why Retained Samples Matter</h2>

<p>A colour record is not administrative overhead; it is the mechanism that makes a colour reproducible rather than merely repeatable. A useful record contains the approved standard and its instrument readings; the dye recipe with the products, concentrations and process parameters; the dye lot numbers used; the yarn lot and the pretreatment route; the batch records including bath ratio, temperature profile and dwell time for each production batch; the instrument readings for each batch; and the retained samples from each batch.</p>

<p>Retained samples are the item buyers most often forget to ask for and most often come to need. A retained sample from each dye lot, kept under defined storage conditions, is what allows a question to be answered eighteen months later: why does the batch from March differ from the batch from September, which one matches the standard, and what did the shade actually look like when it was approved. Without retained samples, that question is unanswerable and the argument becomes about memory.</p>

<p>Retained samples are also what make a re-approval quick. If the mill has to re-establish a shade after a dyehouse change, having the approved standard and the last production samples means the re-development starts from evidence rather than from a description of a colour that somebody once remembered.</p>

<div class="kpi">
  <p><strong>Colour specification checklist &mdash; eight clauses</strong></p>
  <ul>
    <li>Colour route: greige piece-dyed, yarn-dyed, printed or hybrid &mdash; stated explicitly</li>
    <li>Approved standard with instrument readings, illuminant and observer angle</li>
    <li>Conditioning conditions and measurement position on the ribbon width</li>
    <li>Delta-E tolerance band and sample count per lot</li>
    <li>Recipe reference, dye lot numbers, yarn lot and pretreatment route</li>
    <li>Re-approval trigger list, agreed and reviewed periodically</li>
    <li>Retained sample requirement: one per dye lot, storage conditions stated</li>
    <li>Batch record supplied with each shipment, including instrument readings</li>
  </ul>
</div>

<h2>How This Becomes a Commercial Advantage</h2>

<p>None of this is difficult to do. It is a set of records and a set of decisions taken at the right time, and a mill that has them can produce them cheaply. What it buys is the thing every brand buyer wants and few programmes have: a colour that arrives the same on the fourth order as it did on the first.</p>

<p>That matters commercially in a specific way. Colour inconsistency is the defect that generates the highest proportion of avoidable claims, because it is visible, because it is attributed to the brand, and because it is impossible for the brand to argue about. It is also the defect that most often triggers a qualification of a second supplier, since a brand that cannot trust a colour will not consolidate spend with one mill. And it is the defect that most often ends with the brand buying a more expensive mill, because a stable colour is worth a price premium and the buyer rarely frames it that way at the time of the decision.</p>

<p>There is a second commercial point, which is about programme growth. A colour programme that is stable at one SKU and one thousand metres is not necessarily stable at thirty SKUs and fifty thousand metres. Growing a programme changes batch sizes, changes lead times, changes how many dye lots you are running, and changes how often a mill is running a given recipe. The mill that has a controlled colour process can grow with the programme; the mill that has been getting away with a good eye and a consistent operator can scale into a problem.</p>

<p>At Smith Ribbon, in Xiamen since 2004, we run a defined colour route per programme with a written approval, an instrumented assessment, a batch record per dye lot and retained samples per lot. When a programme grows or a route changes, we re-approve rather than assume, and we would rather do that at the second order than at the twentieth. If your brand has been chasing a colour that will not settle, that is usually a routing and record-keeping problem rather than a dyehouse problem, and it is one we can walk through with you.</p>

"""
}


# ============================== BUILD ==============================
if __name__ == "__main__":
    for art in (A289, A290):
        fn, words, html = build(art)
        print(f"[OK] {fn}")
        print(f"     words={words} chars={len(html)}")
