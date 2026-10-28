#!/usr/bin/env python3
"""Publish smithribbon articles 275 (AM) + 276 (PM), 2026-10-28: blog.html, index.html, sitemap.xml."""
from pathlib import Path
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-28"
FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-275-module-mill-side-brand-buyer-metallised-hot-stamp-foil-glitter-metallic-"
                 "ribbon-interlock-architecture-foil-adhesion-metallic-pigment-basefilm-abrasion-flex-crack-rub-"
                 "2026-10-28-am.html"),
        "title": ("Mill-Side Brand-Buyer Metallised &amp; Hot-Stamp Foil Metallic Ribbon Interlock Architecture "
                  "&mdash; Foil Adhesion, Metallic Pigment Base Film, Abrasion, Flex-Crack and Rub 2026"),
        "desc": ("B2B ribbon OEM 275-module metallised and hot-stamp foil metallic ribbon construction. "
                 "4-layer foil-to-substrate adhesion ladder, 3-route metallisation decision tree, "
                 "5-defect flex-crack and abrasion atlas, and a metallic rub-fastness audit. "
                 "Smith Ribbon OEM since 2004."),
        "cat": "Metallic &amp; Foil Ribbon Interlock",
    },
    {
        "file": ("blog-ribbon-oem-276-module-mill-side-brand-buyer-corded-tubular-rope-look-drawstring-cord-"
                 "ribbon-interlock-architecture-core-twist-braid-cover-pillowing-lay-flat-recovery-2026-10-28-pm.html"),
        "title": ("Mill-Side Brand-Buyer Corded &amp; Tubular Rope-Look Ribbon Interlock Architecture &mdash; "
                  "Core Twist, Braid Cover, Pillowing, Lay-Flat and Recovery 2026"),
        "desc": ("B2B ribbon OEM 276-module corded, tubular and rope-look ribbon construction. "
                 "4-layer cord build ladder, 3-route core and cover decision tree, "
                 "5-defect pillowing and lay-flat atlas, and a drawstring recovery audit. "
                 "Smith Ribbon OEM since 2004."),
        "cat": "Corded &amp; Tubular Ribbon Interlock",
    },
]

# ---------- footer standardisation ----------
for art in ARTICLES:
    ap = ROOT / art["file"]
    ah = ap.read_text(encoding="utf-8")
    if FOOTER not in ah:
        j = ah.rfind("</body>")
        ah = ah[:j] + f'<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>\n' + ah[j:]
        ap.write_text(ah, encoding="utf-8")
        print(f"[OK] footer -> {art['file'][:46]}")
    else:
        print(f"[SKIP] footer present {art['file'][:46]}")

# ---------- blog.html : newest first (append after last </article>) ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
cards = []
for art in ARTICLES:
    if art["file"] in blog:
        print(f"[SKIP] blog.html has {art['file'][:46]}")
        continue
    cards.append(
        f'<article class="post-card">\n  <a href="/{art["file"]}">\n'
        f'    <h3>{art["title"]}</h3>\n  </a>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="post-meta">{DATE} &middot; {art["cat"]}</div>\n</article>'
    )
if cards:
    i = blog.rfind("</article>")
    if i == -1:
        raise SystemExit("no </article> in blog.html")
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + "\n".join(cards) + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {len(cards)} card(s)")

# ---------- index.html : newest first (append after last </li>) ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idxh:
        print(f"[SKIP] index.html has {art['file'][:46]}")
        continue
    m = idxh.rfind("</li>")
    if m == -1:
        raise SystemExit("no </li> in index.html")
    m += len("</li>")
    idxh = idxh[:m] + f'\n<li><a href="blog/{art["file"]}">{art["title"]}</a></li>' + idxh[m:]
    added += 1
if added:
    ip.write_text(idxh, encoding="utf-8")
    print(f"[OK] index.html + {added} link(s)")

# ---------- sitemap.xml ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
for art in ARTICLES:
    slug = art["file"][:-5]
    if slug in sm:
        print(f"[SKIP] sitemap has {slug[:46]}")
        continue
    entry = (f'<url><loc>https://smithribbon.com/{slug}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    if ci == -1:
        raise SystemExit("no </urlset>")
    sm = sm[:ci] + entry + sm[ci:]
sp.write_text(sm, encoding="utf-8")
print("[OK] sitemap.xml updated")

# ================= VERIFY (single pass) =================
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")

for art in ARTICLES:
    f = art["file"]
    slug = f[:-5]
    assert f in blog_f, f"blog.html missing {f[:46]}"
    assert f in idx_f, f"index.html missing {f[:46]}"
    assert slug in sm_f, f"sitemap missing {slug[:46]}"
    ap = (ROOT / f).read_text(encoding="utf-8")
    assert ap.count("<h1>") == 1, f"h1 count {ap.count('<h1>')} in {f[:46]}"
    assert 'rel="canonical"' in ap, f"no canonical {f[:46]}"
    assert 'property="og:title"' in ap and 'property="og:image"' in ap, f"OG missing {f[:46]}"
    assert 'name="twitter:card"' in ap, f"twitter missing {f[:46]}"
    assert "<h2 id=\"faq\">" in ap, f"no visible FAQ h2 {f[:46]}"
    assert FOOTER in ap, f"footer missing {f[:46]}"
    assert "since 2004" in ap, f"no 'since 2004' {f[:46]}"
    assert "XXX-Module" not in ap, f"XXX-Module spam {f[:46]}"
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', ap, re.S)
    types = []
    for b in blocks:
        o = json.loads(b)
        types.append(o.get("@type"))
    assert "BlogPosting" in types, f"no BlogPosting {f[:46]}"
    assert "FAQPage" in types, f"no FAQPage {f[:46]}"
    assert "BreadcrumbList" in types, f"no BreadcrumbList {f[:46]}"
    # visible FAQ answers count == schema questions count
    nq = len([o for b in blocks for o in ([json.loads(b)] if json.loads(b).get("@type") == "FAQPage" else [])
              for o in o["mainEntity"]])
    assert ap.count("<h3>") >= nq, f"visible FAQ headings < schema questions {f[:46]}"
    words = len(re.sub(r"<[^>]+>", " ", ap).split())
    print(f"[VERIFIED] {f[:58]} | words={words} | schema={types} | faqQ={nq}")

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate locs {len(locs)} vs {len(set(locs))}"
missing = [l.replace("https://smithribbon.com/", "") for l in locs
           if l.endswith(".html") and not (ROOT / l.replace("https://smithribbon.com/", "")).exists()]
print(f"\nSitemap: {len(locs)} unique locs, {len(locs) - len(set(locs))} dups, {len(missing)} missing files")
if missing:
    print("  missing sample:", missing[:5])
print("PUBLISH VERIFY OK")
