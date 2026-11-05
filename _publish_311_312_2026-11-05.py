#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish smithribbon articles 311 (AM) + 312 (PM) - 2026-11-05.

Updates: blog.html, en-blog.html, index.html, sitemap.xml.
IMPORTANT: legacy blog/ files keep their /blog/ prefixed sitemap URLs (those are
correct, 200). Only these two new root-level module articles get root-level locs.
"""
from pathlib import Path

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-11-05"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-311-module-brand-buyer-custom-ribbon-oem-specification-decorations-"
                 "finishing-cut-length-packaging-conversion-cost-structure-brief-template-2026-11-05-am.html"),
        "title": ("Custom Ribbon OEM Specification &mdash; How to Specify Decorations, Finishing, Cut Length, "
                  "Packaging and Conversion So Two Mills Quote the Same Object 2026"),
        "desc": ("A brand-buyer guide to specifying custom ribbon for OEM programmes: where the cost actually "
                 "sits, choosing between woven jacquard and print, colour tolerance control, edge and cut "
                 "treatment, packaging and labelling, and writing a brief two mills can quote identically."),
        "cat": "OEM Customisation &amp; Specification",
    },
    {
        "file": ("blog-ribbon-oem-312-module-brand-buyer-ribbon-certification-reading-guide-iso-9001-bsci-smeta-"
                 "seda-fsc-oeko-tex-scope-audit-date-verify-register-evidence-pack-2026-11-05-pm.html"),
        "title": ("How to Read a Ribbon Supplier&rsquo;s Certifications &mdash; ISO 9001, BSCI, SMETA, SEDEX, FSC and "
                  "OEKO-TEX Decoded, with the Questions That Actually Narrow the Risk 2026"),
        "desc": ("A brand-buyer guide to reading ribbon and trim supplier certifications: the four certification "
                 "families and what each proves, how to verify a certificate, whether it covers your construction and "
                 "decoration, and the evidence pack that survives a retailer audit."),
        "cat": "Certification &amp; Compliance",
    },
]


def card(art):
    return (
        f'<article class="post-card">\n  <a href="{art["file"]}">\n'
        f'    <h3>{art["title"]}</h3>\n  </a>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="post-meta">{DATE} &middot; {art["cat"]}</div>\n</article>'
    )


# ---------- 1. blog.html ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
cards = []
for art in ARTICLES:
    if art["file"] in blog:
        print(f"[SKIP] blog.html has {art['file'][:40]}")
        continue
    cards.append(card(art))
if cards:
    i = blog.rfind("</article>")
    assert i != -1, "no </article> in blog.html"
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + "\n".join(cards) + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {len(cards)} card(s)")

# ---------- 2. en-blog.html ----------
ep = ROOT / "en-blog.html"
try:
    en = ep.read_text(encoding="utf-8")
    ecards = []
    for art in ARTICLES:
        if art["file"] in en:
            print(f"[SKIP] en-blog.html has {art['file'][:40]}")
            continue
        if "</article>" in en:
            ecards.append(card(art))
        else:
            ecards.append(f'<li><a href="{art["file"]}">{art["title"]}</a></li>')
    if ecards:
        if "</article>" in en:
            i = en.rfind("</article>") + len("</article>")
            en = en[:i] + "\n" + "\n".join(ecards) + en[i:]
        else:
            i = en.rfind("</ul>")
            if i == -1:
                i = en.rfind("</body>")
            en = en[:i] + '\n<ul class="post-list">\n' + "\n".join(ecards) + "\n</ul>\n" + en[i:]
        ep.write_text(en, encoding="utf-8")
        print(f"[OK] en-blog.html + {len(ecards)} card(s)")
    else:
        print("[OK] en-blog.html no change")
except FileNotFoundError:
    print("[SKIP] en-blog.html not found")

# ---------- 3. index.html ----------
ip = ROOT / "index.html"
idx = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idx:
        print(f"[SKIP] index.html has {art['file'][:40]}")
        continue
    m = idx.rfind("</li>")
    assert m != -1, "no </li> in index.html"
    m += len("</li>")
    idx = idx[:m] + f'\n<li><a href="{art["file"]}">{art["title"]}</a></li>' + idx[m:]
    added += 1
if added:
    ip.write_text(idx, encoding="utf-8")
    print(f"[OK] index.html + {added} link(s)")

# ---------- 4. sitemap.xml ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
for art in ARTICLES:
    loc = "https://smithribbon.com/" + art["file"]
    if loc in sm:
        print(f"[SKIP] sitemap has {art['file'][:40]}")
        continue
    entry = (
        f'\n<url>\n    <loc>{loc}</loc>\n    <lastmod>{DATE}</lastmod>\n'
        f'    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    )
    i = sm.rfind("</urlset>")
    assert i != -1, "no </urlset> in sitemap.xml"
    sm = sm[:i] + entry + sm[i:]
    print(f"[OK] sitemap + {art['file'][:45]}")
sp.write_text(sm, encoding="utf-8")
print("[DONE] publish complete")
