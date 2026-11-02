#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B2B ribbon OEM articles for 2026-10-16 cron DOUBLE.

Module 232 AM — Mill-Side Digital-Bill-of-Lading Bill-of-Exchange Blockchain-Shipment-Handoff Architecture
Module 233 PM — Mill-Side ROHS-REACH-CPSIA Substance-Compliance Substance-Declaration Harmonoized-Restricted-Substance Attestation Architecture
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
TEMPLATE = (ROOT / "_html_template.html").read_text(encoding="utf-8")

SITE = "https://smithribbon.com"

# ---------- Article 232 (AM, 10:00) ----------
ART_232 = {
    "slug": "blog-ribbon-oem-232-module-brand-buyer-mill-side-digital-bill-of-lading-bill-of-exchange-blockchain-shipment-handoff-architecture-global-brand-procurement-2026-10-16-am.html",
    "title": "Mill-Side Digital-Bill-of-Lading Bill-of-Exchange Blockchain-Shipment-Handoff Architecture — B2B Ribbon OEM Module 232 (2026-10-16)",
    "desc": "B2B ribbon OEM 232-module mill-side digital-bill-of-lading bill-of-exchange blockchain-shipment-handoff architecture for global brand procurement. 6-stage digital-bill-of-lading pipeline, 5-pillar bill-of-exchange title-issuance governance, 6-tier digital-bill-of-lading-class, digital-bill-of-lading-CSM-to-trade-finance-bank linkage. Smith Ribbon OEM since 2004.",
    "kw": "digital bill of lading bill of exchange blockchain shipment handoff ribbon, 6 stage digital bill of lading pipeline 5 pillar bill of exchange title issuance governance, 6 tier digital bill of lading class L/C discountable non discountable open account CAD consignment, digital bill of lading CSM to trade finance bank linkage, UCP 600 ISBP 745 URC 522 Incoterms 2020 BAFT IFC, Smith Ribbon OEM since 2004",
    "tags": "Digital-Bill-of-Lading Bill-of-Exchange, Blockchain-Shipment-Handoff Architecture, 6-Stage Digital-Bill-of-Lading Pipeline, 5-Pillar Bill-of-Exchange Title-Issuance Governance, 6-Tier Digital-Bill-of-Lading-Class L/C-Discountable L/C-Non-Discountable Open-Account CAD Consignment, Digital-Bill-of-Lading-CSM Trade-Finance-Bank Linkage, UCP-600 ISBP-745 URC-522, Incoterms-2020 BAFT-IFC",
    "iso": "2026-10-16T10:00:00+08:00",
    "body_file": "_body_230.html",
}

# ---------- Article 233 (PM, 15:00) ----------
ART_233 = {
    "slug": "blog-ribbon-oem-233-module-brand-buyer-mill-side-rohs-reach-cpsia-substance-compliance-substance-declaration-harmonized-restricted-substance-attestation-architecture-global-brand-procurement-2026-10-16-pm.html",
    "title": "Mill-Side ROHS-REACH-CPSIA Substance-Compliance Substance-Declaration Harmonoized-Restricted-Substance Attestation Architecture — B2B Ribbon OEM Module 233 (2026-10-16)",
    "desc": "B2B ribbon OEM 233-module mill-side ROHS-REACH-CPSIA substance-compliance substance-declaration harmonized-restricted-substance attestation architecture for global brand procurement. 6-stage ROHS-REACH-CPSIA pipeline, 5-pillar substance-declaration governance, 6-tier restricted-substance-class, ROHS-CPSIA-CSM-to-EU-27-NA-buyer linkage. Smith Ribbon OEM since 2004.",
    "kw": "ROHS REACH CPSIA substance compliance substance declaration harmonized restricted substance attestation ribbon, 6 stage ROHS REACH CPSIA pipeline 5 pillar substance declaration governance, 6 tier restricted substance class EU 27 lead free SVHC disclosure NA lead free phthalate free children product cross region harmonized, ROHS CPSIA CSM to EU 27 NA buyer linkage, EN 71-3 ASTM F963 ISO 17072-1, Smith Ribbon OEM since 2004",
    "tags": "ROHS-REACH-CPSIA Substance-Compliance, Substance-Declaration Harmonoized-Restricted-Substance Attestation, 6-Stage ROHS-REACH-CPSIA Pipeline, 5-Pillar Substance-Declaration Governance, 6-Tier Restricted-Substance-Class EU-27-Lead-Free EU-27-SVHC-Disclosure NA-Lead-Free NA-Phthalate-Free NA-Children-Product Cross-Region-Harmonized, ROHS-CPSIA-CSM EU-27-NA-Buyer Linkage, EN-71-3 ASTM-F963 ISO-17072-1",
    "iso": "2026-10-16T15:00:00+08:00",
    "body_file": "_body_231.html",
}

def render(art):
    body = (ROOT / art["body_file"]).read_text(encoding="utf-8")
    canonical = f"{SITE}/{art['slug']}"
    html = TEMPLATE
    html = html.replace("__TITLE__", art["title"])
    html = html.replace("__DESC__", art["desc"])
    html = html.replace("__KW__", art["kw"])
    html = html.replace("__TAGS__", art["tags"])
    html = html.replace("__CANONICAL__", canonical)
    html = html.replace("__ISO__", art["iso"])
    html = html.replace("__SITE__", SITE)
    html = html.replace("__BODY__", body)
    return html

def main():
    for art in (ART_232, ART_233):
        out = ROOT / art["slug"]
        out.write_text(render(art), encoding="utf-8")
        # Word count sanity (body text only, ignore HTML tags)
        body_text = (ROOT / art["body_file"]).read_text(encoding="utf-8")
        import re
        plain = re.sub(r"<[^>]+>", " ", body_text)
        plain = re.sub(r"\s+", " ", plain).strip()
        wc = len(plain.split())
        print(f"[OK] {out.name}  words\u2248{wc}  size={out.stat().st_size}B")

if __name__ == "__main__":
    main()