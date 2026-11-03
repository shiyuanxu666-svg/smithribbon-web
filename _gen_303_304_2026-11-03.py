#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon articles 303 (AM) + 304 (PM) - 2026-11-03.

303 AM: Supplier Code of Conduct & ethical sourcing sign-off for ribbon/trim
         programmes - employment practices, forced labour, EHS, sub-tier
         transparency, audit rights, findings-to-award linkage.
304 PM: Should-cost model for ribbon and decorative trim - quantity build,
         material + conversion layers, sensitivity ranking, quote reading,
         landed cost bridge.

Bodies live in _body_303.html / _body_304.html.
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

A303 = {
    "fname": ("blog-ribbon-oem-303-module-brand-buyer-supplier-code-of-conduct-ethical-sourcing-"
              "sign-off-audit-rights-labour-compliance-ribbon-trim-programmes-2026-11-03-am.html"),
    "slug": ("blog-ribbon-oem-303-module-brand-buyer-supplier-code-of-conduct-ethical-sourcing-"
             "sign-off-audit-rights-labour-compliance-ribbon-trim-programmes-2026-11-03-am"),
    "title": ("The Supplier Code of Conduct &mdash; How Brand Buyers Structure Labour and Ethical "
              "Sourcing Sign-off for Ribbon and Decorative Trim Programmes 2026"),
    "desc": ("A brand-buyer guide to supplier code of conduct acceptance for ribbon and decorative trim: "
             "what a ribbon-specific code should cover, how to structure audit rights, how to link labour "
             "findings to the commercial relationship, and how to verify that a signature means something."),
    "keywords": [
        "ribbon supplier code of conduct", "ethical sourcing sign-off ribbon supplier",
        "ribbon labour compliance audit", "forced labour due diligence trim supplier",
        "textile supplier code of conduct template", "brand buyer social compliance ribbon",
        "ribbon mill audit rights negotiation", "sub-tier transparency ribbon supply chain",
        "supplier code of conduct acceptance process", "corrective action plan ribbon supplier",
        "sustainable sourcing policy ribbon brand", "worker grievance mechanism supplier",
        "supply chain labour due diligence trims", "compliance scorecard ribbon supplier",
        "ribbon supplier ethical sourcing programme", "brand supplier code conduct rollout",
        "social audit ribbon mill buyer guide", "supplier code conduct procurement framework",
        "ethical procurement decorative trim", "ribbon labour standards verification",
    ],
    "pub_iso": "2026-11-03T10:00:00+00:00",
    "wordcount": 2300,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Ethical Sourcing &amp; Social Compliance",
    "lede": ("Ask any procurement lead who has onboarded a new trim supplier what the hardest document to "
             "obtain was, and the answer is almost never the price list. It is the supplier code of "
             "conduct, because it asks the supplier to accept obligations that reach far past the mill "
             "floor: on working hours, on wage floors, on forced labour, on discrimination, on the "
             "environment, and on the buyer's right to inspect the sub-tier. This guide is about how to "
             "structure that acceptance programme so it produces verifiable obligations rather than a "
             "signed PDF that sits in a procurement folder."),
    "faq": [
        ("What should a ribbon supplier code of conduct contain that a generic one does not?",
         "Six blocks: employment practices covering recruitment, contracts, wages and hours; forced labour "
         "and human trafficking including recruitment fees and document retention; health, safety and "
         "environment with ribbon-specific hazards such as dyehouse chemical handling, effluent treatment, "
         "print solvent handling and boiler systems; freedom of association and grievance mechanisms; "
         "sub-tier transparency covering yarn, greige weaving, dyeing, printing and bow assembly "
         "subcontractors; and records and audit rights. The ribbon-specific points are the three-shift "
         "dyehouse and finishing departments, the pre-holiday migrant labour surge, and the private "
         "worker interview requirement."),
        ("How should audit rights be structured so a supplier will actually accept them?",
         "Three tiers, explained openly up front. Tier 1 is a documentary and desk review using a completed "
         "questionnaire covering wage records, hours by department, insurance enrolment, training records, "
         "chemical inventory, effluent permits and subcontractor disclosure, which should be the default. "
         "Tier 2 is a scheduled announced site visit confirming what the documents said. Tier 3 is "
         "unannounced or risk-triggered, reserved for credible allegations, unremedied Critical findings, "
         "sub-tier changes or production stress. Make the triggers explicit, publish the severity grades "
         "and their consequences, and give the supplier a defined right to respond before a finding is "
         "closed."),
        ("How should labour compliance findings be connected to the commercial relationship?",
         "Through four elements. Write the severity-to-consequence table before you need it so a Critical "
         "finding suspends new awards, a Major finding requires a corrective action plan within 30 days and "
         "verification, and a Minor finding closes within 90 days. Keep corrective action plans "
         "supplier-owned with buyer-owned verification on evidence rather than assertion. Separate the "
         "labour conversation structurally from the price negotiation so compliance is not treated as a "
         "discount lever. And record open findings on every award decision so an exception has to be "
         "deliberate and visible."),
        ("What is the most common mistake buyers make with a supplier code of conduct?",
         "Writing a universal clause that requires compliance with all applicable laws and international "
         "standards without naming any. It sounds strong, commits nothing and cannot be audited against a "
         "defined standard. Replace it with named instruments, each with a defined scope and a defined "
         "applicability, plus a specific record retention period. The second common mistake is "
         "unresourced audit rights: a broad right that the buyer never exercises trains the supplier to "
         "ignore every clause in the document."),
        ("How do we verify that a signed code of conduct actually means something?",
         "Track four things and review them quarterly alongside cost and delivery metrics. Closure rate and "
         "days-to-close by severity. The finding-to-award link, so every award records open findings, "
         "their grade and their age. Repeat-finding analysis, because the same Major finding in three "
         "consecutive audits is one unresolved system problem rather than three findings. And worker-facing "
         "channel evidence, since the most useful indicator is not the finding count but whether workers "
         "know how to raise a concern and believe they will be protected doing so."),
        ("Should a code of conduct be scaled down for smaller ribbon suppliers?",
         "Yes, and it should be said explicitly. A code written for a multinational apparel supply chain "
         "and applied verbatim to a 60-person bow assembly shop produces a predictable result: the small "
         "supplier signs it and performs the easy parts while the brand believes the relationship is "
         "covered when it is not. Scale the document, the audit scope and the corrective action timeline "
         "to the supplier's size and risk profile, and state that the document is proportionate to the "
         "operation."),
    ],
    "cta_title": "Preparing a supplier code of conduct rollout?",
    "cta_body": ("Tell us which processes you subcontract and which you run in house, and we will show you "
                 "the documentary evidence we can provide for each block, the audit access we are "
                 "practically able to support, and how we would structure a corrective action plan."),
    "cta_link_text": "Discuss your compliance framework",
}

A304 = {
    "fname": ("blog-ribbon-oem-304-module-brand-buyer-ribbon-should-cost-model-quantity-build-material-"
              "conversion-cost-landed-cost-bridge-negotiation-discipline-2026-11-03-pm.html"),
    "slug": ("blog-ribbon-oem-304-module-brand-buyer-ribbon-should-cost-model-quantity-build-material-"
             "conversion-cost-landed-cost-bridge-negotiation-discipline-2026-11-03-pm"),
    "title": ("Build Your Own Should-Cost Model for Ribbon &mdash; Quantity Build, Conversion Layers and "
              "the Landed Cost Bridge: A Guide for Brand Buyers Who Want to Read a Quotation Properly 2026"),
    "desc": ("A brand-buyer guide to building a should-cost model for ribbon and decorative trim: the "
             "quantity build, material and conversion cost layers, which assumptions actually move the "
             "price, how to read a quotation against your own number, and how to build the ex-works to "
             "landed cost bridge without damaging the supplier relationship."),
    "keywords": [
        "ribbon should cost model", "ribbon cost breakdown guide brand buyer",
        "how to read a ribbon quotation", "ribbon price negotiation cost build up",
        "ribbon conversion cost calculation", "ribbon material cost index yarn pick density",
        "landed cost bridge ribbon import", "ribbon quote comparison brand procurement",
        "decorative trim costing model", "ribbon pricing analysis buyer guide",
        "why did my ribbon price go up", "ribbon setup amortisation print cylinder cost",
        "ribbon tco cost model brand buyer", "ribbon quotation waterfall analysis",
        "cost engineering ribbon sourcing", "ribbon unit cost build up explained",
        "how to negotiate ribbon price without damaging supplier relationship",
        "ribbon greige conversion cost model", "trim cost model private label buyer",
        "ribbon costing framework procurement 2026",
    ],
    "pub_iso": "2026-11-03T15:00:00+00:00",
    "wordcount": 2400,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Costing, Pricing &amp; Quote Analysis",
    "lede": ("Every ribbon buyer eventually learns the same lesson: a quotation is a position, not a fact. "
             "Two buyers can receive materially different quotes for an identical specification, and both "
             "can be internally coherent, because the difference lives in assumptions that were never made "
             "explicit. A should-cost model is the discipline of building the cost of the product "
             "yourself so you can read a quote against your own number instead of against the last quote. "
             "It is not a negotiation weapon. It is a way to know whether a price is reasonable, and when "
             "a deviation is worth asking about."),
    "faq": [
        ("What is a should-cost model and what is it actually for?",
         "It is a build-up of the cost of your own product from first principles: the quantity chain, the "
         "material layers, the conversion operations, overhead and margin, and then the landed cost "
         "bridge. Its purpose is not to produce a number you can use to beat a supplier. It is to change "
         "the quality of your specifications and the quality of your questions, so that a price movement "
         "becomes explainable rather than something you react to."),
        ("What should the quantity build capture first?",
         "Start from the finished unit and work backwards: how many metres one bow actually consumes "
         "including cutting and tying waste, how many linear metres of greige are needed to yield one "
         "linear metre of finished ribbon after the width loss between loom width and finished width, and "
         "how many picks and ends that represents. Do this before any pricing work, because a five percent "
         "error in the quantity build is a five percent error in everything downstream."),
        ("Which assumptions drive a ribbon price the most?",
         "Four dominate: yarn price and yarn count, which are usually the largest single element and the "
         "one most often quoted as an index rather than a number; pick density and width, which determine "
         "metres per kilogram; colourway complexity, which drives dye lot minimums and lab dip cycles; and "
         "order quantity and run length, which drive setup amortisation and dye lot efficiency. When a "
         "quote moves unexpectedly, the reason is almost always in one of those four."),
        ("How do I read a quotation against my own model?",
         "Compare structure rather than total. For each layer, note what the supplier assumed and what you "
         "assumed, then classify the difference as explicable, which usually reflects a legitimate "
         "difference in construction and often improves the programme; as scope, which usually reflects an "
         "unwritten boundary such as an excluded finishing operation or an excluded hang tag; or as "
         "unexplained, which usually turns out to be a risk premium for a new programme, a negotiation "
         "cushion, or a real unmodelled cost."),
        ("What belongs in the landed cost bridge from an ex-works ribbon price?",
         "Four components. Freight and insurance, remembering that ribbon is volumetric and air freight is "
         "billed on the greater of actual gross weight and carton volume at 166 kg per cubic metre, while "
         "sea freight is billed on CBM and container fill rate is the dominant lever. Duty and trade "
         "measures, modelled as a percentage of customs value with attention to whether the classification "
         "of a jacquard woven ribbon differs from a printed ribbon. Origin handling, where you should ask "
         "for the ex-works component and build DDP yourself. And working capital plus the cost of a delay."),
        ("How do we use a should-cost model without damaging a working supplier relationship?",
         "Do the modelling quietly before the first meeting, because opening a model in the first "
         "conversation with an untested supplier reads as an attempt to prove overcharging. Use it to test "
         "the specification rather than to squeeze the margin. Use it to explain rather than to squeeze, "
         "so divergences resolve into a shared understanding. And accept that a margin is a legitimate "
         "part of the price: a model that leaves nothing is not a better buy, it is a fragile programme "
         "that shows up later as a quality or delivery failure."),
    ],
    "cta_title": "Building a cost model for your next ribbon programme?",
    "cta_body": ("Send us one SKU you have actually received and inspected. We will build the quantity "
                 "chain with you, show which cost layers our own production data supports, and flag the "
                 "questions we would expect a buyer to ask before the brief is released."),
    "cta_link_text": "Work through a cost build-up",
}


def build(a, body_file):
    body = (ROOT / body_file).read_text(encoding="utf-8").strip()
    fname = srl.write_article(
        a["fname"], a["slug"], a["title"], a["desc"], a["keywords"], a["pub_iso"],
        a["wordcount"], a["section"], a["cat_label"], a["lede"], body, a["faq"],
        a["cta_title"], a["cta_body"], a["cta_link_text"])
    print(f"[OK] built {fname}")


build(A303, "_body_303.html")
build(A304, "_body_304.html")
print("BUILD DONE")
