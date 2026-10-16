#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B2B ribbon OEM articles for 2026-10-16 cron DOUBLE-3 (extra batch beyond existing 232/233).

Module 234 AM — Mill-Side Bonded-Warehouse Bond-Zone Cargo-Identity Custody-Title-Governance Architecture
Module 235 PM — Mill-Side Carbon-Credit-Class Voluntary-Market-Asset-Title-Custody Architecture
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
TEMPLATE = (ROOT / "_html_template.html").read_text(encoding="utf-8")

SITE = "https://smithribbon.com"

# ---------- Article 234 (AM, 10:00) ----------
ART_234 = {
    "slug": "blog-ribbon-oem-234-module-brand-buyer-mill-side-bonded-warehouse-bond-zone-cargo-identity-custody-title-governance-architecture-global-brand-procurement-2026-10-16-am.html",
    "title": "Mill-Side Bonded-Warehouse Bond-Zone Cargo-Identity Custody-Title-Governance Architecture — B2B Ribbon OEM Module 234 (2026-10-16)",
    "desc": "B2B ribbon OEM 234-module mill-side bonded-warehouse bond-zone cargo-identity custody-title-governance architecture for global brand procurement. 6-stage bonded-warehouse-custody pipeline, 5-pillar bond-zone-cargo-identity governance, 6-tier bonded-warehouse-class, bonded-warehouse-CSM-to-customs-broker linkage table. Smith Ribbon OEM since 2004.",
    "kw": "bonded warehouse bond zone cargo identity custody title governance ribbon, 6 stage bonded warehouse custody pipeline 5 pillar bond zone cargo identity governance, 6 tier bonded warehouse class export bonded zone import bonded zone free trade zone pre duty cross border e commerce bonded bulk cargo customs bonding, bonded warehouse CSM to customs broker linkage table, WTO Bonded Convention WCO SAFE Framework Kyoto Convention Specific Annex Incoterms 2020, Smith Ribbon OEM since 2004",
    "tags": "Bonded-Warehouse Bond-Zone Cargo-Identity Custody-Title-Governance, 6-Stage Bonded-Warehouse-Custody Pipeline, 5-Pillar Bond-Zone-Cargo-Identity Governance, 6-Tier Bonded-Warehouse-Class Export-Bonded-Zone Import-Bonded-Zone Free-Trade-Zone-Pre-Duty Free-Trade-Zone-Post-Duty Cross-Border-E-Commerce-Bonded Bulk-Cargo-Customs-Bonding, Bonded-Warehouse-CSM Customs-Broker Linkage, WTO-Bonded-Convention WCO-SAFE-Framework Kyoto-Convention-Specific-Annex",
    "iso": "2026-10-16T10:00:00+08:00",
    "body_file": "_body_234.html",
}

# ---------- Article 235 (PM, 15:00) ----------
ART_235 = {
    "slug": "blog-ribbon-oem-235-module-brand-buyer-mill-side-carbon-credit-class-voluntary-market-asset-title-custody-architecture-global-brand-procurement-2026-10-16-pm.html",
    "title": "Mill-Side Carbon-Credit-Class Voluntary-Market-Asset-Title-Custody Architecture — B2B Ribbon OEM Module 235 (2026-10-16)",
    "desc": "B2B ribbon OEM 235-module mill-side carbon-credit-class voluntary-market-asset-title-custody architecture for global brand procurement. 6-stage carbon-credit-class pipeline, 5-pillar carbon-credit-asset-title-custody governance, 6-tier carbon-credit-class assignment, carbon-credit-class-CSM-to-verification-body-as-a-v linkage. Smith Ribbon OEM since 2004.",
    "kw": "carbon credit class voluntary market asset title custody ribbon, 6 stage carbon credit class pipeline 5 pillar carbon credit asset title custody governance, 6 tier carbon credit class assignment VCS verified carbon gold standard CCER China ACR American carbon CAR climate action reserve Puro earth, carbon credit class CSM to verification body as a v linkage, VCS Standard Gold Standard 4.0 ISO 14064 2 ISO 14067 GHG Protocol Scope 3 Incoterms 2020, Smith Ribbon OEM since 2004",
    "tags": "Carbon-Credit-Class Voluntary-Market-Asset-Title-Custody, 6-Stage Carbon-Credit-Class Pipeline, 5-Pillar Carbon-Credit-Asset-Title-Custody Governance, 6-Tier Carbon-Credit-Class VCS-Verified-Carbon Gold-Standard-GS CCER-China ACR-American-Carbon CAR-Climate-Action Puro-Earth-Puro, Carbon-Credit-Class-CSM Verification-Body Linkage, VCS-Standard Gold-Standard-4.0 ISO-14064-2 ISO-14067 GHG-Protocol-Scope-3",
    "iso": "2026-10-16T15:00:00+08:00",
    "body_file": "_body_235.html",
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
    for art in (ART_234, ART_235):
        out = ROOT / art["slug"]
        out.write_text(render(art), encoding="utf-8")
        body_text = (ROOT / art["body_file"]).read_text(encoding="utf-8")
        import re
        plain = re.sub(r"<[^>]+>", " ", body_text)
        plain = re.sub(r"\s+", " ", plain).strip()
        wc = len(plain.split())
        print(f"[OK] {out.name}  words\u2248{wc}  size={out.stat().st_size}B")

if __name__ == "__main__":
    main()