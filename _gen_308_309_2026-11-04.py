#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build smithribbon articles 308 (AM) + 309 (PM) - 2026-11-04.

308 AM: Ribbon supply contract clause architecture - the 11 clause families,
         change control, capacity reservation, liability caps, continuity.
309 PM: Peak-season capacity audit & second-source qualification - how to audit
         real capacity, real lead time math, peak shape, qualified 2nd source.

Bodies live in _body_308.html / _body_309.html.
Uses smithribbon_article_lib.py for head/JSON-LD/FAQ scaffolding.
"""
from pathlib import Path
import importlib.util, sys, re

LIB = "/workspace/smithribbon-web/smithribbon_article_lib.py"
spec = importlib.util.spec_from_file_location("srl", LIB)
srl = importlib.util.module_from_spec(spec)
sys.modules["srl"] = srl
spec.loader.exec_module(srl)

ROOT = Path("/workspace/smithribbon-web")

A308 = {
    "fname": ("blog-ribbon-oem-308-module-brand-buyer-ribbon-supply-contract-clause-architecture-"
              "specification-change-control-quantity-forecast-capacity-reservation-liability-cap-"
              "continuity-2026-11-04-am.html"),
    "slug": ("blog-ribbon-oem-308-module-brand-buyer-ribbon-supply-contract-clause-architecture-"
             "specification-change-control-quantity-forecast-capacity-reservation-liability-cap-"
             "continuity-2026-11-04-am"),
    "title": ("Ribbon Supply Contract Clause Architecture &mdash; The 11 Clause Families That Decide "
              "Who Absorbs a Late Delivery, a Colour Drift or a Price Move 2026"),
    "desc": ("A brand-buyer guide to ribbon and decorative trim supply agreements: the eleven clause "
             "families a contract should contain, how to draft specification change control, how to "
             "separate committed quantity from forecast, capacity reservation and liability caps, and "
             "how to build a continuity plan that survives a supplier exit."),
    "keywords": [
        "ribbon supply contract clause template", "ribbon purchase agreement structure brand buyer",
        "trim supplier contract change control specification", "ribbon MOQ lead time capacity clause",
        "ribbon supply agreement quality AQL acceptance clause", "ribbon supplier liability cap negotiation",
        "ribbon contract committed quantity vs forecast", "ribbon peak capacity reservation clause",
        "ribbon OEM contract clauses checklist", "decorative trim agreement terms brand buyer",
        "ribbon tooling ownership cylinder custody clause", "ribbon subcontracting transparency clause",
        "ribbon supplier termination continuity last time buy", "ribbon incoterms title risk clause",
        "ribbon certification documentation schedule clause", "ribbon price adjustment mechanism clause",
        "ribbon contract negotiation order brand buyer", "trim supplier contract guide 2026",
        "ribbon OEM supply agreement guide global brands", "ribbon purchase order vs supply agreement",
    ],
    "pub_iso": "2026-11-04T02:00:00+00:00",
    "wordcount": 2700,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Supply Contracts &amp; Agreements",
    "lede": ("A ribbon programme that ends in a signed purchase order has, on paper, a legally binding "
             "agreement. It has a specification, a price, a quantity, a lead time and a delivery date. "
             "What it usually does not have is a mechanism for handling the things that actually go "
             "wrong: the colour drifts one unit from the approved standard on the third dye lot, the "
             "mill runs out of a specific yarn in the middle of a peak season, the print cylinder wears "
             "faster than the quoted tolerance allowed. None of these events are unusual. All of them "
             "are foreseeable. And the reason they turn into disputes rather than adjustments is almost "
             "always the same: the contract described the happy path in detail and the unhappy path "
             "not at all. This guide covers the eleven clause families a ribbon agreement should "
             "contain and what each one must settle to be useful."),
    "faq": [
        ("How many clauses does a ribbon supply agreement actually need?",
         "Around eleven clause families for a multi-programme, multi-mill brand, structured so that "
         "every agreement is a variation of a known template rather than a negotiation from scratch. "
         "The families are specification and change control, quantity and forecast, MOQ and lead time "
         "with capacity reservation, pricing and cost adjustment, quality standards and inspection and "
         "acceptance, claims and remedies and liability caps, delivery and Incoterms and title and "
         "risk, documentation and certification, subcontracting and transparency, intellectual property "
         "and tooling, and term and termination and continuity and dispute resolution. For a single "
         "small pilot order, a purchase order with a good specification is entirely sufficient, and "
         "over-engineering it is wasteful."),
        ("What is the single most important clause in a ribbon supply agreement?",
         "Specification and change control, because it prevents the largest number of downstream "
         "disputes. The clause has to do two things: state the attributes that define the product "
         "specifically enough to identify it unambiguously, including material composition by weight, "
         "construction, width and tolerance, colour standard and tolerance, finish, edge treatment, "
         "packaging format and carton counts; and define the change mechanism, meaning who may request "
         "a change, what evidence accompanies the request, what the lead-time impact is, who approves "
         "it, and which party bears the cost of a change. Almost every argument a buyer has with a "
         "ribbon mill about what was actually ordered traces back to an under-specified attribute."),
        ("Should a forecast in a ribbon agreement be treated as a commitment?",
         "No, and keeping those two things separate is one of the highest-value disciplines in trim "
         "procurement. A committed quantity creates firm obligations on both sides. A non-binding "
         "forecast creates an obligation only to plan and should be labelled as such with a stated "
         "planning horizon. A capacity reservation is a third category entirely, where the buyer pays "
         "a fee to hold a defined slot and can release it under stated conditions. Conflating these "
         "is what creates the expectation that a mill can absorb a 40 percent demand increase on "
         "short notice, and the mill will have planned for it on the buyer's own forecast."),
        ("Is it normal for a ribbon supplier to refuse uncapped liability?",
         "Yes, and the refusal is usually rational rather than evasive. Uncapped liability is not "
         "priced and cannot be, so a supplier asked to accept it will decline the agreement rather than "
         "the clause. The workable structure is layered: a general cap tied to the value of the "
         "affected goods or order, with a higher cap or an uncapped carve-out for defined categories "
         "such as wilful misconduct, breach of confidentiality, intellectual property infringement and "
         "personal injury or property damage. Buyers should also check how consequential and indirect "
         "damages are treated, because a trim delay that causes a retailer to pull a product from "
         "shelf creates a loss far larger than the value of the ribbon."),
        ("How should price adjustments work when raw material costs move?",
         "Separate the fixed and floating elements explicitly. Conversion, setup and margin are the "
         "mill's own costs and its own risk, and they are normally fixed for the contract term. Raw "
         "material, and sometimes energy and freight, float against a stated index with a stated "
         "reference period. The formula should be auditable by the buyer: which index, which period, "
         "how the adjustment is calculated, how often it may trigger. Crucially it should have a "
         "symmetrical floor and cap applied to the indexed component rather than to the total price, "
         "because an uncapped adjustment mechanism is not agreed in practice, so its absence produces "
         "no protection for either party."),
        ("What should a buyer do about the mill's subcontracted processes?",
         "Require disclosure of the sub-tier process map, naming the functions that are subcontracted "
         "and the locations involved, then set obligations that flow down: the sub-tier must meet the "
         "same quality and compliance requirements, the mill remains responsible for the sub-tier "
         "output, traceability records must reach the level of the individual dye lot or print run, "
         "and the buyer may audit the sub-tier. A buyer with audit rights that stop at the mill's "
         "front gate is auditing a company that may not physically make the product. This matters "
         "commercially as well as compliance-wise, because an unknown sub-tier is also an unknown "
         "capacity and an unknown single point of failure."),
        ("What is a concession mechanism and why does a buyer want one?",
         "A concession is a controlled acceptance of a minor nonconformity, shipped on time with a "
         "documented discount, rework credit or agreed replacement, instead of a rejection that would "
         "protect the specification but create a stockout. The agreement should define the threshold "
         "below which the mill may ship with a concession, the documentation required, and the "
         "reconciliation process afterwards. Buyers who reject minor defects by default end up "
         "losing the delivery schedule they were trying to protect, because the rejected goods come "
         "back as a new shipment on a later date rather than as an absent shipment on the original one."),
        ("How should a brand handle brand-owned tooling such as a printing cylinder?",
         "Treat it as an asset with custody rules from the day it is funded. The clause should specify "
         "ownership of artwork and the licence to use it, confidentiality of the artwork, ownership of "
         "brand-funded tooling and dies, where the tooling is stored and how it is maintained, the "
         "inspection right to verify it, the transfer process if the relationship ends, and the terms "
         "for disposal. It is also worth stating whether the brand's marks may be used in the mill's "
         "marketing or as a reference, because many brands do not think about that until they see "
         "their logo on a competitor's website."),
        ("What belongs in a ribbon contract's termination and continuity provisions?",
         "A distinction between termination for cause, which follows an uncured material breach, and "
         "termination for convenience, which is a right to exit on notice with an agreed financial "
         "settlement. Then the consequences, which is the part most often omitted: what happens to work "
         "in progress, to material already committed, to brand-owned tooling, to retained samples and "
         "golden samples, to open quality claims, and to delivery of the final balance of the "
         "programme. Continuity planning belongs in the agreement rather than in an exit interview, "
         "because a brand that discovers at termination that the mill held the only golden sample and "
         "the brand-owned cylinder has no path to a smooth transition."),
        ("Does a buyer need to renegotiate every ribbon agreement individually?",
         "No, and this is where procurement effort is usually wasted. The standardisation that pays "
         "most is not legal, it is commercial: a single pre-agreed specification template, a single "
         "quality and AQL standard, a single price-adjustment mechanism and a single documentation "
         "schedule, applied consistently across mills. Those four artefacts make each negotiation "
         "shorter and each agreement more comparable, and they are the reason two mills quote on the "
         "same basis. When you do have to move a clause, the useful order is: specification, quantity "
         "structure, price formation and adjustment, and capacity first, because those are the "
         "substantive terms and the supplier's willingness to accommodate on them is high; then "
         "quality and acceptance; then liability caps, approached with a bounded proposal; then "
         "operational clauses; and term and termination last."),
    ],
    "cta_title": "Need a ribbon supply agreement that actually covers the difficult parts?",
    "cta_body": ("We have been manufacturing ribbons, bows and decorative trims in Xiamen since 2004, "
                 "and we work with brand buyers on specification sheets, quality standards, capacity "
                 "reservation and the documentation schedules their retail customers require. Tell us "
                 "how your programme is structured and we will tell you what we would put in the "
                 "agreement and what we would want settled before we start."),
    "cta_link_text": "Talk to our OEM team",
}

A309 = {
    "fname": ("blog-ribbon-oem-309-module-brand-buyer-peak-season-capacity-audit-second-source-"
              "qualification-reserved-capacity-real-lead-time-peak-plan-2026-11-04-pm.html"),
    "slug": ("blog-ribbon-oem-309-module-brand-buyer-peak-season-capacity-audit-second-source-"
             "qualification-reserved-capacity-real-lead-time-peak-plan-2026-11-04-pm"),
    "title": ("Peak-Season Capacity Audit for Ribbon &mdash; How to Verify a Mill Can Actually Take "
              "Your Volume, Qualify a Real Second Source and Plan the Curve 2026"),
    "desc": ("A brand-buyer guide to peak-season ribbon capacity: how to audit whether a mill can "
             "really run your volume, how to read optimistic capacity claims, the four intervals that "
             "make the real lead time longer than the quoted one, how to qualify a second source that "
             "is a genuine alternative, and how to build a peak plan that survives a bad month."),
    "keywords": [
        "ribbon peak season capacity planning", "ribbon mill capacity audit brand buyer",
        "ribbon second source qualification", "ribbon supplier capacity reservation peak",
        "real ribbon lead time calculation", "ribbon peak season planning calendar brand buyer",
        "ribbon capacity utilisation dye house bottleneck", "ribbon second source qualification checklist",
        "ribbon switching plan supplier risk", "ribbon OEM peak season pre booking",
        "ribbon production slot allocation December", "ribbon peak order cut off date",
        "brand buyer ribbon supply risk mitigation", "ribbon buffer strategy split shipment peak",
        "ribbon capacity constraint printed ribbon winter", "ribbon supplier reference peak season",
        "ribbon second source golden sample qualification", "ribbon peak plan required on shelf date",
        "ribbon trim peak season delay prevention", "ribbon capacity audit checklist 2026",
    ],
    "pub_iso": "2026-11-04T08:00:00+00:00",
    "wordcount": 2600,
    "section": "Ribbon OEM Manufacturing",
    "cat_label": "Peak Season &amp; Capacity Planning",
    "lede": ("Every year, a brand buyer discovers in September that the ribbon needed for the Christmas "
             "season cannot be made in time, and every year the discovery is treated as a supply "
             "failure. It is usually not. It is the predictable result of a capacity question that "
             "was never asked. Loom slots, dye capacity, printing cylinders, hand-tie assembly labour "
             "and finishing equipment are scheduled well in advance of the demand they will serve. A "
             "mill that receives its October orders in August has no physical capacity to add them. "
             "This guide covers how to audit real capacity, how to read optimistic answers, how "
             "qualify a second source properly, and how to build a peak plan that survives a bad "
             "month."),
    "faq": [
        ("How do I audit whether a ribbon mill can really handle my volume?",
         "Ask for capacity in units of your own constraint rather than as a percentage: metres per "
         "week at peak for your width, your print route and your colourway count. Then ask what shifts "
         "that number, how many machines and how many trained operators sit behind it, what the "
         "historical peak utilisation was in the busiest month of the last two years, and what the "
         "earliest production date for your programme would be. Finally ask the two most revealing "
         "questions: what would have to change for that date to be June rather than September, and "
         "if you asked for double the December volume, what specifically would change to make it "
         "possible. The answers locate the real bottleneck and separate capability from aspiration."),
        ("How long does a ribbon programme really take from order to delivery?",
         "Considerably longer than the quoted manufacturing lead time, because the quoted figure "
         "covers only the production process. Four intervals sit on the critical path: order to "
         "material, typically one to four weeks, because custom colourway greige must be sourced and "
         "dyed; sample to approval, one to three weeks, which buyers routinely omit because it feels "
         "like a formality; production to ship, one to three weeks, where inspection is a queue as "
         "well as an activity; and ship to deliver, two to six weeks by sea. A mill quoting 25 days "
         "for a printed programme in June is describing the manufacturing leg, and the honest planning "
         "number for a first delivery is closer to 60 to 90 days."),
        ("What is a genuinely qualified second source for ribbon?",
         "A second source that has made your specification at commercial volume, or at minimum a "
         "production-intent run measured against your own golden sample. It also needs its own tooling "
         "and its own material chain, because a second mill sharing your printing cylinder or dye "
         "house is a second door to the same building; a capacity reservation rather than good "
         "intentions, because unreserved capacity goes to whoever asks first; and a switching plan "
         "with a defined trigger and a rehearsed execution, since a switch that has never been tested "
         "takes weeks to perform even when the capacity was genuinely held."),
        ("When should I reserve peak-season capacity with a ribbon mill?",
         "Early enough that the mill can still schedule rather than triage, which in practice means "
         "booking in the late summer for an October delivery, and ideally looking at shapes and "
         "volumes in the spring. The peak is decided by the last week of September, not by the first "
         "week of December. Capacity reserved in August can be released if it is not needed; capacity "
         "requested in October is allocated by whoever contacts the factory first. Reservation should "
         "state the fee, the release conditions and, most importantly, the priority sequence used "
         "when capacity is genuinely constrained."),
        ("Is a capacity percentage a useful answer during a ribbon supplier audit?",
         "No, and it is one of the three clearest signs of a capacity claim that will not hold in "
         "practice. A percentage does not say a percentage of what, and it cannot be converted into a "
         "plan. Two other tells indicate the same thing: capacity expressed as machine rating rather "
         "than realised output, which ignores the setup loss that consumes 25 to 40 percent of "
         "printing capacity in setup, colour change and material change; and capacity that assumes "
         "staffing which has not yet been recruited or trained, particularly for hand-tie assembly "
         "where the training period is typically eight weeks."),
        ("Why does peak-season demand affect manufacturing times as well as prices?",
         "Because a mill running near capacity experiences queueing. A dye lot waits behind other dye "
         "lots, a finishing line waits for material rather than for operators, and a printing cylinder "
         "waits for a colour change. A 25-day manufacturing leg quoted in June can become a 35-day "
         "leg in November at the same volume, without any change in the underlying efficiency. "
         "Inbound material also becomes less reliable before it becomes more expensive, because "
         "upstream mills in peak season cut corners on delivery to their own customers, so your "
         "greige arrives later than the paperwork promised."),
        ("How should I structure a peak-season plan for a ribbon programme?",
         "Five elements. A required-on-shelf date stated as an actual date rather than a season, "
         "because the whole plan is built backwards from it. A materials calendar naming the critical "
         "input for each programme and the date by which it must be committed, because material "
         "lead times run longer than manufacturing lead times. A firm cut-off date per programme, "
         "after which changes are not accepted for that season, which protects committed programmes "
         "from unplanned changes. A prioritisation rule for genuine capacity conflicts, decided in "
         "advance. And a buffer expressed as schedule rather than inventory, such as shipping 80 "
         "percent early and the balance later, which gives a small lot the chance to be corrected."),
        ("Should a buyer use air freight to solve a late ribbon delivery?",
         "At ribbon volumes, rarely, and it is worth understanding why before assuming it is an "
         "option. Ribbon is light and compressible, so it fills a disproportionate share of air "
         "freight capacity, and the freight cost per unit is high. More importantly, air freight "
         "addresses the transit interval without addressing the interval that usually caused the "
         "lateness, which is the order-to-material and production queue time inside the mill. If the "
         "goods do not exist, shipping them faster is not available at any price. The exceptions are a "
         "genuine shortfall against an otherwise complete order, and a partial shipment as a "
         "replacement for a split delivery, which is where air freight genuinely pays for itself."),
        ("How do I tell a real second source from a document exercise?",
         "By asking three questions that a genuine second source can answer and a hypothetical one "
         "cannot. Can I see a measured colour and construction comparison against my golden sample, "
         "with numbers rather than impressions? Which of the process steps in your quotation are done "
         "in-house, and which are subcontracted, and where? And has a slot actually been held for my "
         "volume, or is my order a hopeful entry into a queue? If the answers are a capability deck, "
         "a sample couriered on the day of the visit and a verbal assurance about peak capacity, the "
         "second source is a document, and it should be reported to the risk register as such rather "
         "than counted as coverage."),
    ],
    "cta_title": "Planning a peak-season ribbon programme?",
    "cta_body": ("Capacity is decided months before the peak arrives, and the most useful thing a "
                 "mill can give a brand buyer is a straight answer about what can be produced, when, "
                 "and on what terms. We have been making ribbon, bows and decorative trims in Xiamen "
                 "since 2004, and we will tell you our realistic capacity for your specification and "
                 "date, our lead time broken into its component intervals, and where we are genuinely "
                 "tight rather than where we are merely optimistic."),
    "cta_link_text": "Request a capacity check",
}


def build(art, body_file):
    body = (ROOT / body_file).read_text(encoding="utf-8")
    # lib hardcodes a date line; substitute the correct one
    out = srl.write_article(
        art["fname"], art["slug"], art["title"], art["desc"], art["keywords"],
        art["pub_iso"], art["wordcount"], art["section"], art["cat_label"],
        art["lede"], body, art["faq"], art["cta_title"], art["cta_body"], art["cta_link_text"])
    p = ROOT / out
    t = p.read_text(encoding="utf-8")
    t = t.replace("Published October 28, 2026 &middot; Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; 16 min read",
                  "Published November 4, 2026 &middot; Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; 16 min read")
    p.write_text(t, encoding="utf-8")
    words = len(re.sub(r"<[^>]+>", " ", t).split())
    print(f"[OK] {out}  words={words}")


build(A308, "_body_308.html")
build(A309, "_body_309.html")
