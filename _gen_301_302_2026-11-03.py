#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon articles 301 (AM) + 302 (PM) - 2026-11-03.

301 AM: Trim programme bundling - consolidating ribbon, bows, boxes, tissue, labels
         and accessories into one coordinated pack.
302 PM: Freight mode selection - air vs sea vs rail for ribbon programmes.

Bodies live in _body_301.html / _body_302.html.
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

A301 = {
    "fname": ("blog-ribbon-oem-301-module-brand-buyer-trim-programme-bundling-ribbon-bow-box-tissue-label-"
              "accessory-single-supplier-consolidation-strategy-2026-11-03-am.html"),
    "slug": ("blog-ribbon-oem-301-module-brand-buyer-trim-programme-bundling-ribbon-bow-box-tissue-label-"
             "accessory-single-supplier-consolidation-strategy-2026-11-03-am"),
    "title": ("Bundling the Trim Programme &mdash; One Coordinated Pack Instead of Nine Purchase Orders: "
              "A Sourcing Strategy for Ribbon, Bows, Boxes, Tissue, Labels and Accessories 2026"),
    "desc": ("A brand-buyer guide to bundling a packaging trim programme: consolidating ribbon, bows, "
             "boxes, tissue, labels and accessories under one coordinated supplier, the consolidation "
             "benefits, the risks of over-concentration, and how to structure the transition."),
    "keywords": [
        "trim programme bundling strategy", "packaging trim consolidation buyer guide",
        "one supplier ribbon boxes tissue labels", "packaging component bundling strategy",
        "gift box and ribbon single supplier", "coordinated packaging trim programme",
        "trim supplier consolidation benefits", "packaging assembly single point of contact",
        "private label packaging components sourcing", "decorative trim procurement strategy",
        "bow tissue box label bundling", "packaging trim supplier selection guide",
        "brand buyer trim programme management", "packaging component supplier rationalisation",
        "gift set packaging component sourcing 2026", "packaging trim assembly strategy",
        "ribbon and packaging one mill sourcing", "multi component packaging procurement",
        "packaging trim vendor consolidation risk", "trim programme buying guide 2026",
    ],
    "pub_iso": "2026-11-03T02:00:00+00:00",
    "wordcount": 2700,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Trim Programme &amp; Component Sourcing Strategy",
    "lede": ("A finished gift set does not arrive as a gift set. It arrives as nine or eleven separately "
             "purchased components that were specified by three or four different people, bought on four "
             "different lead times, inspected by three different inspectors, and finally assembled by a "
             "factory that was never told the whole thing was one product. The pieces are compatible by "
             "coincidence rather than by design, and every point where a component slips out of the "
             "programme creates a delay for everything downstream of it. This guide is about the opposite "
             "approach: treating the trim programme as a single engineered pack, deciding deliberately "
             "which components to consolidate and which to leave alone, and managing the transition "
             "without putting your supply at risk."),
    "faq": [
        ("What does it really mean to bundle a packaging trim programme?",
         "It means a single party is accountable for the finished presentation of the pack, whether or not "
         "that party manufactures every component. Three models are common: integrated manufacturing, "
         "coordinated assembly with the supplier sourcing each component, and specification-led "
         "consolidation where components stay with their best-fit suppliers but are governed by one "
         "written pack specification and one approval gate."),
        ("Should every component in a gift set come from one supplier?",
         "Rarely. A ribbon mill does not make gift boxes and a box converter does not make velvet bows. "
         "The realistic approach is to bundle the components that are physically coupled - ribbon and bow, "
         "box and tissue, ribbon and hang tag - and specify the rest together while leaving them with "
         "specialist suppliers."),
        ("How do we consolidate without disrupting a programme that is already running?",
         "Work in five steps: document the pack as it is today, map which components are physically "
         "coupled, consolidate one coupling at a time starting with the strongest one, then issue a "
         "versioned pack specification with a single approval gate, and finally qualify a second source "
         "for the consolidated set. Do it outside peak season."),
        ("What should a pack specification contain that individual component specs do not?",
         "The relational information: component inventory with revisions and colour codes, geometry "
         "including ribbon width, bow loop count, tail length and knot type, the colour relationship "
         "between components, the order of assembly, the filler specification and compression limits, the "
         "batch and traceability coding convention, and a named assembly location with pack-level "
         "inspection responsibility."),
        ("How do you judge whether a supplier can actually run a coordinated trim programme?",
         "Ask how many sequential approval cycles they need for a coordinated pack, whether they can hold "
         "a shared colour standard across ribbon, board, tissue and print, what their pack-level defect "
         "rate is and how it is trending, and what their escalation path is when a component goes late. "
         "Then ask to physically see a pack they assembled last month."),
        ("Where does bundling actually save money?",
         "Less in unit price than in failure and schedule cost. Each separately sourced component carries "
         "its own purchase order, inspection, invoice and discrepancy cycle. The larger savings come from "
         "schedule compression, because nine lead times do not run in parallel, and from defect avoidance "
         "when one colour approval is shared across components instead of being approved four times."),
        ("What are the main risks of consolidating too much?",
         "Concentration risk: the partner's capacity problem, quality issue or price increase becomes your "
         "problem in full rather than in part. The mitigation is deliberate bundling of coupled "
         "components plus qualifying a second source for the consolidated set against the same "
         "specification."),
        ("Is it worth bundling for a small or irregular-volume programme?",
         "Usually not. Coordination overhead exceeds the benefit when volumes are small and irregular, when "
         "the components have unrelated specification and supplier pools, or when the programme is still "
         "in its first year and the design has not settled. Consolidation pays when the pack is sold as a "
         "single experience and the brand's differentiation lives in the details."),
    ],
    "cta_title": "Planning a coordinated trim programme?",
    "cta_body": ("Send us your pack components and target volumes. We will tell you which couplings make "
                 "sense to consolidate, what our own production capacity looks like for the ribbon and bow "
                 "side, and where we would suggest leaving a specialist in place."),
    "cta_link_text": "Discuss your trim programme",
}

A302 = {
    "fname": ("blog-ribbon-oem-302-module-brand-buyer-ribbon-freight-mode-selection-air-vs-sea-vs-rail-"
              "lead-time-landed-cost-trade-off-shipping-decision-framework-2026-11-03-pm.html"),
    "slug": ("blog-ribbon-oem-302-module-brand-buyer-ribbon-freight-mode-selection-air-vs-sea-vs-rail-"
             "lead-time-landed-cost-trade-off-shipping-decision-framework-2026-11-03-pm"),
    "title": ("Air, Sea or Rail? &mdash; A Freight Mode Decision Framework for Ribbon Programmes: Lead "
              "Time, Landed Cost and Where Decorative Trim Loses Money 2026"),
    "desc": ("A brand-buyer guide to freight mode selection for ribbon and decorative trim: comparing air, "
             "sea and rail on cost and lead time, understanding container fill and chargeable weight for "
             "ribbon cargo, and building a shipping decision framework for seasonal programmes."),
    "keywords": [
        "air freight vs sea freight ribbon", "shipping mode selection packaging trim",
        "ribbon cargo container loading guide", "ocean freight decorative trim lead time",
        "air freight cost calculation textiles", "rail freight China Europe textiles",
        "landed cost freight mode comparison", "container volume weight ribbon roll",
        "chargeable weight bulky cargo air freight", "seasonal buying air freight buffer",
        "ribbon freight cost optimisation", "shipping decision framework brand buyer",
        "container fill rate ribbon rolls", "freight mode tradeoff supply chain lead time",
        "textile freight cost per carton", "ribbon OEM shipping guide buyers",
        "air freight peak season surcharge textiles", "ribbon order consolidation shipping",
        "ribbon programme freight planning 2026", "sea freight ribbon packaging procurement",
    ],
    "pub_iso": "2026-11-03T07:00:00+00:00",
    "wordcount": 2700,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Freight, Logistics &amp; Shipment Planning",
    "lede": ("Ribbon is light, voluminous and awkward. That combination makes its freight behave unlike the "
             "textile it usually sits next to in a costing model, and it is the single most common reason "
             "a ribbon programme's landed cost differs sharply from its quoted cost. A reel of ribbon "
             "occupies an enormous volume for the weight it carries, so it is charged on space rather than "
             "mass, it fills containers badly unless it is packed deliberately, and it becomes genuinely "
             "expensive to move quickly. This guide is about choosing a shipping mode on the evidence "
             "rather than on habit."),
    "faq": [
        ("Why does ribbon freight cost behave so differently from other textiles?",
         "Because ribbon is volumetric before it is heavy. A standard 40 mm polyester grosgrain roll of "
         "100 metres weighs roughly three to four kilograms with its core, so a carton of ribbon is "
         "mostly air. It is therefore charged on space rather than mass, it fills containers badly unless "
         "packed deliberately, and because its value density is low the freight can consume a "
         "disproportionate share of the product margin."),
        ("Should we ship ribbon by air or by sea?",
         "For planned programmes, sea is normally the only realistic option on cost, because volumetric "
         "charging makes air freight on ribbon routinely eight to fifteen times the sea rate per kilogram "
         "equivalent. Air earns its place on the first shipment of a new programme, on samples and "
         "tooling, and on small replenishment quantities where stock cover is thin and stockout risk is "
         "high."),
        ("How do I calculate the chargeable weight of a ribbon consignment?",
         "For air freight, compute both the actual gross weight and the volumetric weight, which is the "
         "carton volume in cubic metres multiplied by 166 kg per cubic metre, then use whichever is "
         "greater. For example, 4,000 kg gross occupying 40 cubic metres is charged on 6,640 kg. For sea "
         "freight the chargeable basis is the volume in CBM, with minimum charges applied to small "
         "consignments."),
        ("What is a good target for container fill on ribbon shipments?",
         "85% cubic utilisation or better on a full-container move. Below that the buyer is paying for "
         "air at ribbon freight rates. Fill is largely a purchasing decision rather than a logistics "
         "outcome: roll length, width consolidation, carton geometry against container geometry, and "
         "whether the load is floor-loaded or palletised are all worth negotiating in the purchase "
         "specification."),
        ("How do we decide between freight modes without over-comparing quotes?",
         "Use a five-step sequence that eliminates modes rather than comparing prices: establish the "
         "required warehouse date, remove every mode that cannot meet it, confirm at least two modes "
         "remain so the programme has a contingency, compare the survivors on delivered cost including "
         "in-transit working capital, and finally price the cost of a delay."),
        ("Is stock cover or faster freight the better way to manage demand uncertainty?",
         "They are the same decision viewed from two ends. Inventory carries uncertainty by holding stock; "
         "freight carries it by buying speed. For seasonal decorative trim with a spiky demand curve and a "
         "finite colour life, the usual answer is a split: sea freight for predictable base volume and a "
         "modest air-freighted buffer for the uncertain top end."),
        ("What transit risks matter most for ribbon specifically?",
         "Compression set from over-stacking rolls, abrasion and pile crushing on velvet and organza, "
         "static and dust pickup on dark and high-gloss shades, trapped conditioning moisture causing "
         "mildew on long sea transits, colour shift from cartons sitting on an open quay, and loss of "
         "lot identity when loose rolls are repacked at transshipment. All are mitigated by the packing "
         "specification rather than by the freight mode."),
        ("What should a freight forwarder be briefed so that quotes are comparable?",
         "Give the cargo description including packed dimensions and gross weight per carton, total CBM "
         "and total gross weight, origin and destination with the inland delivery point, the incoterm "
         "stated explicitly, the loaded cargo dimensions, the required delivery date and whether it is "
         "firm, any special handling requirements, and the complete document set. Forwarders quoting on "
         "vague cargo descriptions are pricing a guess."),
    ],
    "cta_title": "Planning a ribbon shipping strategy?",
    "cta_body": ("Tell us your target volumes and destination and we will show you the loaded cubic "
                 "utilisation we can achieve on your programme, the roll length that best fits your "
                 "container, and how we would stage a split delivery to cover a seasonal launch."),
    "cta_link_text": "Discuss your shipping plan",
}


def build(a, body_file):
    body = (ROOT / body_file).read_text(encoding="utf-8").strip()
    fname = srl.write_article(
        a["fname"], a["slug"], a["title"], a["desc"], a["keywords"], a["pub_iso"],
        a["wordcount"], a["section"], a["cat_label"], a["lede"], body, a["faq"],
        a["cta_title"], a["cta_body"], a["cta_link_text"])
    print(f"[OK] built {fname}")


build(A301, "_body_301.html")
build(A302, "_body_302.html")
print("BUILD DONE")
