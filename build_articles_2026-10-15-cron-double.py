#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B2B ribbon OEM articles for 2026-10-15 cron DOUBLE.

Module 230 AM — Mill-Side Closed-Loop-Material-Recovery Take-Back-Program & Recommerce-Routing Architecture
Module 231 PM — Mill-Side AI-Vision Pre-Shipment-Inspection & Defect-Classification-Attribute-Fingerprinting Architecture
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
TEMPLATE = (ROOT / "_html_template.html").read_text(encoding="utf-8")

SITE = "https://smithribbon.com"

# ---------- Article 230 (AM, 10:00) ----------
ART_230 = {
    "slug": "blog-ribbon-oem-230-module-brand-buyer-mill-side-closed-loop-material-recovery-take-back-program-recommerce-routing-architecture-premium-brand-procurement-2026-10-15-am.html",
    "title": "Mill-Side Closed-Loop-Material-Recovery Take-Back-Program & Recommerce-Routing Architecture — B2B Ribbon OEM Module 230 (2026-10-15)",
    "desc": "B2B ribbon OEM 230-module mill-side closed-loop-material-recovery take-back-program recommerce-routing architecture for premium-brand procurement. 7-stage take-back-program pipeline, 5-pillar closed-loop-routing governance, 3-tier closed-loop-class, take-back-CSM-to-recovery-mill linkage. Smith Ribbon OEM since 2004.",
    "kw": "closed loop material recovery take back program ribbon, recommerce routing architecture premium brand procurement, 7 stage take back program pipeline 5 pillar closed loop routing governance, 3 tier closed loop class consumer recommerce retailer take back brand bulk recovery, take back CSM to recovery mill linkage, Smith Ribbon OEM since 2004",
    "tags": "Closed-Loop-Material-Recovery Take-Back-Program, Recommerce-Routing Premium-Brand Procurement, 7-Stage Take-Back-Program Pipeline, 5-Pillar Closed-Loop-Routing Governance, 3-Tier Closed-Loop-Class Consumer-Recommerce Retailer-Take-Back Brand-Bulk-Recovery, Take-Back-CSM Recovery-Mill Linkage, ISO 14021 Mass-Balance, EU-Green-Claims-Directive",
    "iso": "2026-10-15T10:00:00+08:00",
    "body_file": "_body_228.html",
}

# ---------- Article 231 (PM, 15:00) ----------
ART_231 = {
    "slug": "blog-ribbon-oem-231-module-brand-buyer-mill-side-ai-vision-pre-shipment-inspection-defect-classification-attribute-fingerprinting-architecture-global-brand-procurement-2026-10-15-pm.html",
    "title": "Mill-Side AI-Vision Pre-Shipment-Inspection & Defect-Classification-Attribute-Fingerprinting Architecture — B2B Ribbon OEM Module 231 (2026-10-15)",
    "desc": "B2B ribbon OEM 231-module mill-side AI-vision pre-shipment-inspection defect-classification-attribute-fingerprinting architecture for global brand procurement. 6-stage AI-vision pipeline, 5-pillar pre-shipment-defect-classification governance, 3-tier AI-vision-class, vision-CSM-to-defect-library linkage. Smith Ribbon OEM since 2004.",
    "kw": "AI vision pre shipment inspection defect classification attribute fingerprinting ribbon, 6 stage AI vision pipeline 5 pillar pre shipment defect classification governance, 3 tier AI vision class yarn level weave level finish level, vision CSM to defect library linkage, 23 defect library 0.05mm pixel resolution CNN Vision Transformer ResNet EfficientNet, Smith Ribbon OEM since 2004",
    "tags": "AI-Vision Pre-Shipment-Inspection, Defect-Classification Attribute-Fingerprinting, 6-Stage AI-Vision Pipeline, 5-Pillar Pre-Shipment-Defect-Classification Governance, 3-Tier AI-Vision-Class Yarn-Level Weave-Level Finish-Level, Vision-CSM Defect-Library Linkage, 23-Defect Library ISO 2859-1, IATF 16949 AS9100",
    "iso": "2026-10-15T15:00:00+08:00",
    "body_file": "_body_229.html",
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
    for art in (ART_230, ART_231):
        out = ROOT / art["slug"]
        out.write_text(render(art), encoding="utf-8")
        # Word count sanity (body text only, ignore HTML tags)
        body_text = (ROOT / art["body_file"]).read_text(encoding="utf-8")
        import re
        plain = re.sub(r"<[^>]+>", " ", body_text)
        plain = re.sub(r"\s+", " ", plain).strip()
        wc = len(plain.split())
        print(f"[OK] {out.name}  words≈{wc}  size={out.stat().st_size}B")

if __name__ == "__main__":
    main()
