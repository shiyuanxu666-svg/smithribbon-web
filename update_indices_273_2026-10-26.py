#!/usr/bin/env python3
"""Update smithribbon blog.html, index.html, sitemap.xml with module 273 (PM), 2026-10-26."""
from pathlib import Path
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-26"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-273-module-mill-side-brand-buyer-organza-chiffon-voile-sheer-ribbon-transparency-"
                 "sheerness-weave-openness-edge-fray-crinkle-finish-interlock-architecture-2026-10-26-pm.html"),
        "title": ("Mill-Side Brand-Buyer Organza &amp; Chiffon Sheer Ribbon Transparency &amp; Sheerness Interlock "
                  "Architecture &mdash; Yarn Denier, Weave Openness, Edge Fray and Crinkle Finish 2026"),
        "desc": ("B2B ribbon OEM 273-module organza and chiffon sheer ribbon transparency and sheerness interlock "
                 "architecture. 5-layer sheer-construction authority ladder, 4-stage transparency approval gate, "
                 "3-tier sheer-defect reconciliation ladder, and an openness + edge-fray audit. Smith Ribbon OEM "
                 "since 2004."),
        "cat": "Organza &amp; Chiffon Sheer Interlock",
    },
]

FOOTER = ("&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. | "
          "Professional Ribbon Manufacturer Since 2004")

# ---------- standardize the footer on the new articles ----------
for art in ARTICLES:
    ap = ROOT / art["file"]
    ah = ap.read_text(encoding="utf-8")
    if FOOTER not in ah:
        marker = '<p style="font-size:0.9rem;color:#777;margin-top:2em;">Smith Ribbon OEM since 2004'
        j = ah.find(marker)
        if j == -1:
            j = ah.rfind("</body>")
        ah = ah[:j] + f'<p style="font-size:0.85rem;color:#888;margin-top:1.4em;">{FOOTER}</p>\n' + ah[j:]
        ap.write_text(ah, encoding="utf-8")
        print(f"[OK] footer standardized on {art['file'][:40]}")
    else:
        print(f"[SKIP] footer already present on {art['file'][:40]}")

# ---------- blog.html (newest first: append after last </article>) ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")

cards = []
for art in ARTICLES:
    if art["file"] in blog:
        print(f"[SKIP] blog.html already has {art['file'][:40]}")
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
        raise SystemExit("could not locate last </article> in blog.html")
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + "\n".join(cards) + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {len(cards)} card(s)")

# ---------- index.html ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idxh:
        print(f"[SKIP] index.html already has {art['file'][:40]}")
        continue
    m = idxh.rfind("</li>")
    if m == -1:
        raise SystemExit("no </li> found in index.html")
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
        print(f"[SKIP] sitemap.xml already has {slug[:40]}")
        continue
    entry = (f'<url><loc>https://smithribbon.com/{slug}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    if ci == -1:
        raise SystemExit("</urlset> not found")
    sm = sm[:ci] + entry + sm[ci:]
sp.write_text(sm, encoding="utf-8")
print("[OK] sitemap.xml updated")

# ---------- verify ----------
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")

for art in ARTICLES:
    f = art["file"]
    assert f in blog_f, f"blog.html missing {f[:40]}"
    assert f in idx_f, f"index.html missing {f[:40]}"
    slug = f[:-5]
    assert slug in sm_f, f"sitemap.xml missing {slug[:40]}"
    ap = (ROOT / f).read_text(encoding="utf-8")
    assert ap.count("<h1>") == 1, f"h1 count != 1 in {f[:40]}"
    assert "application/ld+json" in ap, f"no JSON-LD in {f[:40]}"
    assert 'rel="canonical"' in ap, f"no canonical in {f[:40]}"
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', ap, re.S):
        json.loads(m)

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs: {len(locs)} vs {len(set(locs))}"

missing = []
for l in locs:
    p = l.replace("https://smithribbon.com/", "")
    if p.endswith(".html") and not (ROOT / p).exists():
        missing.append(p)

print(f"Verification OK: {len(ARTICLES)} article(s) linked in blog.html, index.html, sitemap.xml | "
      f"{len(locs)} unique locs, 0 dups, {len(missing)} missing files")
if missing[:5]:
    print("  missing:", missing[:5])
