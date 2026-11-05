#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon articles 306 (AM) + 307 (PM) - 2026-11-04.

306 AM: Ribbon sample development & approval workflow - the prototype-to-approval
         ladder, sample set design that isolates variables, cost structure,
         approval record design, failure patterns.
307 PM: Factory cooperation arrangement for ribbon/trim programmes - decision
         types cooperation actually lowers, mechanism design, keeping it alive,
         telling a real arrangement from a label.

Bodies live in _body_306.html / _body_307.html.
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

A306 = {
    "fname": ("blog-ribbon-oem-306-module-brand-buyer-ribbon-sample-development-approval-workflow-"
              "prototype-to-production-ladder-colour-construction-sampling-cost-structure-"
              "golden-sample-reference-2026-11-04-am.html"),
    "slug": ("blog-ribbon-oem-306-module-brand-buyer-ribbon-sample-development-approval-workflow-"
             "prototype-to-production-ladder-colour-construction-sampling-cost-structure-"
             "golden-sample-reference-2026-11-04-am"),
    "title": ("Ribbon Sample Development &amp; Approval Workflow &mdash; How Brand Buyers Build a "
              "Prototype-to-Production Ladder That Actually Answers Questions 2026"),
    "desc": ("A brand-buyer guide to ribbon sample development and approval: the six-stage sample ladder, "
             "how to design a sample set that isolates variables, what a proper approval record must "
             "contain, how to manage sample cost without distorting the programme, and the failure "
             "patterns that turn approvals into disputes."),
    "keywords": [
        "ribbon sample development approval workflow", "ribbon prototype to production sample ladder",
        "custom ribbon sampling guide brand buyer", "ribbon lab dip colour approval process",
        "pre production sample ribbon trim", "ribbon golden sample reference standard",
        "printed ribbon sample approval checklist", "bow sample development brand buyer",
        "ribbon swatch handout approval criteria", "ribbon sample cost structure programme",
        "ribbon colour approval tolerance sign-off", "trim prototype approval process",
        "ribbon specification change after sample", "custom trim sampling timeline",
        "brand buyer ribbon sample strategy", "ribbon construction prototype review",
        "ribbon sampling common mistakes buyer", "custom ribbon new product development sample",
        "ribbon sample selection from production lot", "private label trim development sample",
        "ribbon brand buyer new programme launch", "sample approval record ribbon programme",
    ],
    "pub_iso": "2026-11-04T02:00:00+00:00",
    "wordcount": 2700,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Sample Development &amp; Approval",
    "lede": ("Ask a brand buyer what went wrong on a ribbon programme that reached production and "
             "failed, and the answer is rarely that the mill made a bad ribbon. It is that nobody "
             "ever established what a good ribbon looked like. The colour was approved on a swatch "
             "that had not been through the print route. The bow was approved as a photograph rather "
             "than as an object that had been folded, hung and left under compression for a week. "
             "This guide is about running sample development as an evidence-gathering discipline "
             "instead of as a formality between the brief and the purchase order."),
    "faq": [
        ("How many samples should a ribbon programme involve, and who pays for them?",
         "It depends on the number of colourways and the number of variables in the specification, "
         "not on a fixed number. The structure is six stages: material swatch, lab dip or strike-off, "
         "conversion sample, construction prototype, pre-production sample and shipped sample. Cost is "
         "commonly split into three categories that should be quoted separately: development samples "
         "from prototypes, production-intent samples which consume production material and machine "
         "time, and shipping. The two things to settle in writing before sampling starts are how sample "
         "charges are treated if the programme reaches production, credited against the first order or "
         "treated as a non-recoverable development fee, and whether the sample fee includes shipping "
         "to multiple test destinations. Ambiguity on these two points surfaces at the worst possible "
         "moment."),
        ("What should a ribbon approval record contain to be defensible later?",
         "Four elements, and the fourth is the one most often missing. First, what was approved, "
         "described specifically enough to identify unambiguously: SKU or trim number, colour standard "
         "and measured deviation, width in millimetres with tolerance, material composition by weight, "
         "construction parameters, packaging format and carton and unit counts. Second, who approved it "
         "and in what role, with a date, because a designer's visual approval and a quality engineer's "
         "measurable approval are different approvals. Third, what was measured rather than judged, "
         "including the measured value and the method used, since visual approval is appropriate for "
         "colour intention and inappropriate for width, weight, shrinkage or loop count. Fourth, and "
         "critically, what was explicitly not approved, including items deferred to a later stage. "
         "Without that last section, deferred items are implicitly approved and will be quoted back "
         "later as though the approval had been explicit."),
        ("Is it acceptable to approve a ribbon sample by photograph?",
         "For some things, yes, and for most things no. Photographs are appropriate for remote review "
         "of construction and for keeping a visual record. They are a poor substitute for a physical "
         "unit in a colour approval, because a single photograph under one lighting condition cannot "
         "show how a colour behaves at 3000K, under shop-window daylight, or after three months on a "
         "retail shelf. They are also a poor substitute for a shipped unit in any approval involving "
         "packaging, because ribbon is light, compressible and hygroscopic, and a bow that arrives "
         "flattened in a hot carton after six weeks at sea is a recurring and entirely predictable "
         "problem that only a physical shipment reveals."),
        ("Should every colourway in a programme be sampled separately?",
         "Yes, at the conversion stage at least. The common practice of sampling one colourway and "
         "assuming the rest will follow is a mistake that is easy to understand and expensive in "
         "practice, because colourways within one programme often vary more than colourways between "
         "different programmes. They are dyed in different lots, often against different recipes, and "
         "the visual difference that this produces is frequently enough to require a re-dye. Sampling "
         "one colourway per programme instead of one per programme colourway trades a modest sampling "
         "cost for a recurring risk of approving a range the brand cannot actually produce."),
        ("How do you stop a sample from being approved by default because nobody decided?",
         "Three procedural steps, none of them technical. Name a decision owner with the authority to "
         "approve and a named backup before the samples are made, so the review has a person rather "
         "than a department attached to it. Fix the review date at the point the sample is commissioned "
         "rather than when it arrives, and treat a missed review date as an escalation rather than as "
         "permission to approve. And require the approval record to list what was not approved, because "
         "the items left open in a sample review are exactly the items that reappear later as claims. "
         "Approval by default is the failure pattern with the highest long-run cost in a sample "
         "programme, because it converts a scheduling problem into a quality problem and a claims "
         "problem simultaneously."),
        ("Why is it useful to keep a golden sample from the approved production lot?",
         "Because it is the only artefact that settles a later question about whether a delivery "
         "matches what was approved. Buyers who keep no golden sample end every future dispute with a "
         "conversation about memory, which is a conversation nobody wins. A useful golden sample is "
         "retained from the approved production lot, photographed under defined lighting, "
         "dimensionally recorded, and stored so that it remains comparable. It should be referenced by "
         "the specification itself, so that an inspector at the mill and a buyer in another country are "
         "looking at the same reference rather than at two verbal descriptions of it."),
    ],
    "cta_title": "Planning a ribbon sample programme?",
    "cta_body": ("Tell us how many colourways and how many SKUs your programme carries, and we will "
                 "show you the sample schedule we would run against it, what each sample resolves, "
                 "and how we record approvals so the decision survives a dispute."),
    "cta_link_text": "Discuss your sample workflow",
}

A307 = {
    "fname": ("blog-ribbon-oem-307-module-brand-buyer-ribbon-factory-cooperation-arrangement-"
              "joint-capacity-planning-forecast-confidence-instrumentation-escalation-framework-"
              "2026-11-04-pm.html"),
    "slug": ("blog-ribbon-oem-307-module-brand-buyer-ribbon-factory-cooperation-arrangement-"
             "joint-capacity-planning-forecast-confidence-instrumentation-escalation-framework-"
             "2026-11-04-pm"),
    "title": ("A Factory Cooperation Arrangement for Ribbon &mdash; Joint Capacity Planning, Forecast "
              "Confidence and an Escalation Framework That Works 2026"),
    "desc": ("A brand-buyer guide to building a factory cooperation arrangement with a ribbon or trim "
             "mill: the four decision types cooperation actually lowers, the mechanisms a workable "
             "arrangement contains, how it differs from a multi-year supply agreement, how to keep it "
             "alive, and how to tell a genuine arrangement from a relabelled transaction."),
    "keywords": [
        "ribbon factory cooperation arrangement", "ribbon mill strategic partnership buyer",
        "ribbon supplier partnership guide brand", "joint capacity planning ribbon mill",
        "ribbon forecast confidence range supplier", "ribbon mill capacity reservation agreement",
        "trim supplier cooperation framework", "ribbon multi year supply agreement difference",
        "supplier partnership escalation framework trim", "ribbon tooling ownership agreement",
        "ribbon capacity hold pre holiday season", "brand buyer supplier relationship ribbon",
        "ribbon supplier investment commitment programme", "joint business planning ribbon brand",
        "ribbon supply chain partnership governance", "trim mill relationship management buyer",
        "ribbon cooperative agreement structure", "supplier collaboration ribbon programme",
        "ribbon factory partner evaluation criteria", "brand procurement partnership maturity",
    ],
    "pub_iso": "2026-11-04T08:00:00+00:00",
    "wordcount": 2600,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Supplier Cooperation &amp; Partnerships",
    "lede": ("Most ribbon supplier relationships begin as a transaction, and that is entirely correct "
             "while the specification is stable, the volume is predictable and the quality is "
             "acceptable. The relationship needs a different structure when the programme becomes "
             "complex, when volume makes capacity planning matter, or when the market turns volatile "
             "and a quarterly forecast stops being enough. This guide is about building that structure "
             "for ribbon and decorative trim, and about the practical difference between a genuine "
             "cooperation arrangement and one that has simply been given a better name."),
    "faq": [
        ("What is the difference between a factory cooperation arrangement and a multi-year supply agreement?",
         "They serve different purposes and are frequently conflated. A multi-year supply agreement is a "
         "commercial instrument: it fixes price mechanisms, volumes, payment terms and legal "
         "obligations over a period. A cooperation arrangement is a working method: it fixes how "
         "information flows, how decisions are made jointly and how both parties behave when something "
         "is difficult. A multi-year agreement can exist without cooperation and will produce exactly "
         "the transactional behaviour you would expect. Cooperation can exist without a multi-year "
         "agreement and produces the coordination benefits without the legal protections. The common "
         "mistake is trying to write cooperation into a supply agreement, which produces a legally "
         "dense and behaviourally inert document."),
        ("What should a ribbon factory cooperation arrangement actually contain?",
         "Six mechanisms, each tied to a specific decision the parties have to make together. A shared "
         "forecast with an explicit confidence range and a defined review cadence, rather than a single "
         "number treated as a commitment by one side and an aspiration by the other. A capacity "
         "reservation mechanism specifying what is held, for how long, when a hold converts to firm "
         "production, and what happens if volume comes in below the hold. A forward cost and price "
         "mechanism for handling raw material movement. A development and tooling commitment covering "
         "what the mill invests, who owns it and what happens on discontinuation. A joint quality and "
         "escalation framework with defined severities and response times. And confidentiality "
         "covering the buyer's artwork, packaging files and forecast data."),
        ("How do you tell a genuine factory cooperation arrangement from a partnership label?",
         "Five behavioural tests. Does the supplier know your rolling forecast before you place the order, "
         "and can they act on it? Do they invest for your programme ahead of a specific order, such as "
         "holding capacity, building a dye recipe or setting up a printing cylinder against a forecast? "
         "Do they tell you about problems before those problems become claims, which is the single most "
         "reliable indicator of all? Can the relationship absorb a dispute without converting it into a "
         "claim? And does the arrangement commit either side to something it would not do if it were "
         "not written down, because an arrangement that merely records what would happen anyway adds "
         "nothing."),
        ("How do you keep a cooperation arrangement from decaying?",
         "Watch for the four predictable causes of decline. The forecast becomes fiction because the "
         "buyer's own demand planning is unstable, which is the most common cause and is fixed by "
         "bringing sales and finance into the review so the number is owned by the people who set it. "
         "The reviews stop happening because both parties are busy, fixed by a short agenda and a "
         "standing date where a missed review is moved rather than cancelled. New people arrive and "
         "inherit undocumented verbal commitments, fixed by recording named contacts and roles in the "
         "written document. And the mill's ownership or key personnel change without anyone deciding "
         "it, which is usually visible in the first two quarters and responds to an explicit "
         "re-establishment rather than an assumption that the arrangement carries over."),
        ("Should a cooperation arrangement with a ribbon mill include exclusivity?",
         "No. A ribbon mill that is genuinely good at what it does will serve many brands, and an "
         "exclusivity clause that prevents it from doing so is either unenforceable or destructive. The "
         "same reasoning applies to an open-ended priority clause without a defined scope, because "
         "priority against whom, for what and for how long are the three questions that distinguish a "
         "useful commitment from an unusable one. Where exclusivity is genuinely wanted, it has to be "
         "narrowly defined, time-bounded, and compensated by the buyer, which in practice means paying "
         "for the capacity the mill commits to hold."),
        ("How should a buyer approach asking a supplier for a cooperation arrangement?",
         "Start with evidence rather than a proposal. Assemble a factual picture from the last four "
         "quarters of where coordination currently costs money: specification changes that came after "
         "the order was placed, slipped delivery windows, quality claims that took more than one cycle "
         "to resolve, and forecasts that were missed and how the mill responded. Then make the ask "
         "proportionate to the history, because a supplier with two years of clean predictable orders "
         "has no reason to accept a substantial new commitment. Then agree the mechanisms before "
         "writing the document, since a document cannot manufacture behaviour the parties have not "
         "actually agreed. A short working session with the mill's commercial and production leads "
         "does more than a long draft."),
    ],
    "cta_title": "Building a cooperative arrangement with a ribbon mill?",
    "cta_body": ("Tell us what your programme volume looks like across the year and where coordination "
                 "currently costs you time, and we will show you the mechanisms we run on our side: "
                 "forecast format, capacity holding, escalation routing and tooling ownership."),
    "cta_link_text": "Discuss a cooperation framework",
}

# ---------------------------------------------------------------------------
BODIES = {
    A306["fname"]: ROOT / "_body_306.html",
    A307["fname"]: ROOT / "_body_307.html",
}

for art in (A306, A307):
    body = BODIES[art["fname"]].read_text(encoding="utf-8")
    fname = srl.write_article(
        art["fname"], art["slug"], art["title"], art["desc"], art["keywords"],
        art["pub_iso"], art["wordcount"], art["section"], art["cat_label"],
        art["lede"], body, art["faq"], art["cta_title"], art["cta_body"], art["cta_link_text"],
    )
    p = ROOT / fname
    t = p.read_text(encoding="utf-8")
    # fix hardcoded publish date from the lib template
    t = t.replace("Published October 28, 2026", "Published November 4, 2026")
    p.write_text(t, encoding="utf-8")
    print(f"[OK] wrote {fname}")
