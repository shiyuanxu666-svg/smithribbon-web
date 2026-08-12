#!/usr/bin/env python3
"""Update index.html (news-card) and blog.html (blog-card) with the 2 new articles."""
from pathlib import Path
import re

ROOT = Path("/workspace/smithribbon-web")

A1_FILE = "blog-ribbon-oem-44-module-in-store-visual-merchandising-retail-experience-brand-identity-architecture-global-brand-procurement-2026-08-12-am.html"
A1_TITLE = "Ribbon OEM 44-Module In-Store Visual Merchandising &amp; Retail-Experience Brand-Identity Architecture 2026"
A1_DATE = "2026-08-12 10:00 AM"
A1_CATEGORY = "In-Store Visual Merchandising &amp; Retail-Experience Architecture"
A1_BLURB = "A 2026 B2B ribbon OEM 44-module in-store visual merchandising (VM) and retail-experience brand-identity architecture for global brand owners, retail-banner merchandisers, store-planning directors, and private-label program directors. Covers 7-VM-strategy, 8-VM-concept, 6-VM-color, 5-VM-material, 4-VM-finish, 6-VM-form, 5-VM-typography, 4-VM-illustration, 6-VM-prop, 5-VM-fixture, 4-VM-graphic, 6-window-display, 5-end-cap, 4-counter-display, 6-floor-display, 5-pillar-display, 4-podium-display, 6-banner-ribbon, 5-bow-rosette, 4-bow-pull, 6-bow-loose, 5-bow-tree, 4-bow-cascade, 6-ribbon-wrap, 5-ribbon-bow-combination, 4-ribbon-banner, 6-seasonal-VM, 5-holiday-VM, 4-occasion-VM, 6-regional-VM, 5-store-format-VM, 4-window-VM, 6-pillar-VM, 5-counter-VM, 4-endcap-VM, 6-fixture-VM, 5-graphic-VM, 4-illumination-VM, 6-fragrance-VM, 5-music-VM, 4-touch-VM, 6-VM-SOP, 5-VM-QC, 4-VM-photo, 6-VM-rollout, 5-VM-train, 4-VM-KPI, 6-VM-A/B &amp; 4-VM-archive modules. Includes 18-32% higher foot-fall, 24-38% higher dwell-time, 22-36% higher conversion-rate, 14-24% higher AOV, 9-17% higher repeat-visit, 4,800 store-rollouts, 22 retail-banners, 18 regional-clusters on a 4.4M-meter annual multi-brand VM-ribbon program over 30 months."

A2_FILE = "blog-ribbon-oem-45-module-brand-buyer-rfq-to-award-decision-architecture-global-brand-procurement-2026-08-12-pm.html"
A2_TITLE = "Ribbon OEM 45-Module Brand-Buyer RFQ-to-Award Decision Architecture 2026"
A2_DATE = "2026-08-12 15:00 PM"
A2_CATEGORY = "Brand-Buyer RFQ-to-Award Decision Architecture"
A2_BLURB = "A 2026 B2B ribbon OEM 45-module brand-buyer RFQ-to-award decision architecture for global brand owners, supply-chain leaders, sourcing-directors, and private-label program directors. Covers 7-RFQ-intake, 8-supplier-discovery, 6-supplier-pre-qual, 5-supplier-RFI, 4-RFQ-spec, 6-RFQ-pricing, 5-RFQ-incoterms, 4-RFQ-payment, 6-RFQ-capacity, 5-RFQ-lead-time, 4-RFQ-quality, 6-RFQ-compliance, 5-RFQ-esg, 4-RFQ-capability, 6-site-audit, 5-quotation-review, 4-quotation-comparison, 6-supplier-shortlist, 5-supplier-clarification, 4-supplier-revision, 6-supplier-bid, 5-supplier-best-final-offer, 4-supplier-final-pitch, 6-supplier-decision, 5-supplier-award, 4-supplier-decline, 6-supplier-contract, 5-supplier-onboard, 4-supplier-PPAP, 6-supplier-pilot, 5-supplier-Q1, 4-supplier-Q2, 6-supplier-Q3, 5-supplier-Q4, 4-supplier-annual-review, 6-supplier-renewal, 5-supplier-extension, 4-supplier-SLA, 6-supplier-scorecard, 5-supplier-KPI, 4-supplier-tier-1, 6-supplier-tier-2, 5-supplier-tier-3, 4-supplier-develop, 6-supplier-disqualify, 5-supplier-replace &amp; 4-supplier-knowledge modules. Includes 28-42% faster RFQ-cycle-time, 18-32% higher award-rate, 24-38% lower TCO, 22-36% higher on-time-fulfillment, 14-24% lower supplier-risk, 9-17% higher renewal-rate on a 1,250-RFQ, 38 brand-buyer-partner, 4,800 SKU annual multi-brand RFQ program over 30 months."

# === Update index.html (news-card) ===
idx_path = ROOT / "index.html"
idx = idx_path.read_text(encoding="utf-8")
if A1_FILE in idx:
    print("[SKIP] index.html already has A1")
else:
    # Find the most recent news-card (the 40-module one based on earlier grep)
    # Pattern: insert AFTER the </div> of the news-card containing "blog-ribbon-oem-40"
    new_card_1 = f"""
            <div class="news-card">
                <div class="news-date">{A1_DATE}</div>
                <h3 class="en-content">{A1_TITLE}</h3>
                <p class="en-content">{A1_BLURB}</p>
                <a href="blog/{A1_FILE}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""
    new_card_2 = f"""
            <div class="news-card">
                <div class="news-date">{A2_DATE}</div>
                <h3 class="en-content">{A2_TITLE}</h3>
                <p class="en-content">{A2_BLURB}</p>
                <a href="blog/{A2_FILE}" class="news-link"><span class="en-content">Read More</span> &rarr;</a>
            </div>"""

    # Anchor: insert after the news-card containing 40-module (the most recent)
    # Look for </div> closing the 40-module news-card
    pattern_40 = r'(<a href="blog/blog-ribbon-oem-40-module-brand-buyer-coinnovation-lab-architecture-global-brand-procurement-2026-08-11-pm\.html" class="news-link">.*?</a>\s*</div>)'
    m = re.search(pattern_40, idx, re.DOTALL)
    if m:
        idx = idx[:m.end()] + new_card_1 + new_card_2 + idx[m.end():]
        idx_path.write_text(idx, encoding="utf-8")
        print("[OK] index.html updated with 2 news cards (after 40-module)")
    else:
        print("[WARN] index.html: 40-module anchor not found, trying first news-card anchor")
        # Fallback: after the 39-module entry
        pattern_39 = r'(<a href="blog/blog-ribbon-oem-39-module-rfp-technical-specification-architecture-global-brand-procurement-2026-08-11-am\.html" class="news-link">.*?</a>\s*</div>)'
        m = re.search(pattern_39, idx, re.DOTALL)
        if m:
            idx = idx[:m.end()] + new_card_1 + new_card_2 + idx[m.end():]
            idx_path.write_text(idx, encoding="utf-8")
            print("[OK] index.html updated with 2 news cards (after 39-module)")
        else:
            print("[ERROR] Could not locate insertion anchor in index.html")

# === Update blog.html (blog-card) ===
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
if A1_FILE in blog:
    print("[SKIP] blog.html already has A1")
else:
    # Find the blog-card for 43-module and insert AFTER it (43 was the previous one for 08-12 PM, but per the cron we go: 44 AM, 45 PM; 44 is newest)
    # The 43-module card is the most recent blog-card entry
    pattern_43 = r'(<article class="blog-card">\s*<span class="blog-tag">Omnichannel Fulfillment Architecture</span>\s*<h3><a href="blog-ribbon-oem-43-module-omnichannel-fulfillment-architecture[^"]+">[^<]+</a></h3>.*?</article>)'
    m = re.search(pattern_43, blog, re.DOTALL)
    if m:
        new_b1 = f"""
        <article class="blog-card">
            <span class="blog-tag">{A1_CATEGORY}</span>
            <h3><a href="{A1_FILE}">{A1_TITLE}</a></h3>
            <p>{A1_BLURB}</p>
            <div class="blog-meta">{A1_DATE}</div>
        </article>"""
        new_b2 = f"""
        <article class="blog-card">
            <span class="blog-tag">{A2_CATEGORY}</span>
            <h3><a href="{A2_FILE}">{A2_TITLE}</a></h3>
            <p>{A2_BLURB}</p>
            <div class="blog-meta">{A2_DATE}</div>
        </article>"""
        blog = blog[:m.end()] + new_b1 + new_b2 + blog[m.end():]
        blog_path.write_text(blog, encoding="utf-8")
        print("[OK] blog.html updated with 2 blog-cards (after 43-module)")
    else:
        print("[ERROR] Could not locate 43-module blog-card anchor in blog.html")
