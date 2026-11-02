#!/usr/bin/env python3
"""Build 15:00 cron B2B article for smithribbon.com (2026-09-19 PM).
Reads _article_152_template.html and substitutes placeholders.
"""
import os

WEB = "/workspace/smithribbon-web"
TODAY = "2026-09-19"
PM_TIME = "2026-09-19T15:00:00+08:00"
NUM = "152"
SLUG_FULL = "ribbon-crock-rub-fastness-printed-logo-brand-mark-isfa-116-iso-105-x12-aatcc-8-dry-wet-perspiration-fastness"

filename = f"blog-ribbon-oem-{NUM}-module-brand-buyer-mill-side-{SLUG_FULL}-architecture-global-brand-procurement-{TODAY}-pm.html"
canonical = f"https://smithribbon.com/{filename}"

display_title = f"Ribbon OEM {NUM}-Module Brand-Buyer Mill-Side Crock / Rub-Fastness for Printed Logo &amp; Brand-Mark Programs | Smith Ribbon"
jsonld_title = f"Ribbon OEM {NUM}-Module Brand-Buyer Mill-Side Crock / Rub-Fastness for Printed Logo & Brand-Mark Programs"
h1_title = f"Ribbon Crock / Rub-Fastness for Printed Logo &amp; Brand-Mark Programs — Mill-Side Spec, ISFA 116 / ISO 105-X12 / AATCC 8 Dry-Wet-Perspiration Fastness"

desc = (
    "Mill-side crock / rub-fastness playbook for printed logo and brand-mark ribbon programs: ISFA 116 industry-standard crock test, "
    "ISO 105-X12 dry / wet crock, AATCC 8 crockmeter, perspiration fastness ISO 105-E04, sublimation / bleed-resistance, "
    "white-ground staining, fabric-to-fabric crock, ink-recipe selection (water-based vs plastisol vs pigment vs dye-sublimation), "
    "and printed-ribbon-by-substrate spec — engineered for global brand procurement, retail private-label, and luxury gift packaging programs 2026."
)

template_path = os.path.join(WEB, "_article_152_template.html")
output_path = os.path.join(WEB, filename)

with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

# Substitute (avoid formatting of 152 by treating as literal)
html = html.replace("__DESC__", desc)
html = html.replace("__CANONICAL__", canonical)
html = html.replace("__DISPLAY_TITLE__", display_title)
html = html.replace("__JSONLD_TITLE__", jsonld_title)
html = html.replace("__H1_TITLE__", h1_title)
html = html.replace("__NUM__", NUM)
html = html.replace("__PM_TIME__", PM_TIME)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

size = os.path.getsize(output_path)
print(f"[OK] PM #{NUM}: {filename} ({size:,} bytes)")