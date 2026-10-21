#!/usr/bin/env python3
"""Update blog.html, index.html, sitemap.xml with smithribbon modules 252 (AM) + 253 (PM), 2026-10-21."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-21"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-252-module-mill-side-brand-buyer-ai-powered-quality-claim-substantiation-"
                 "marketing-claim-review-governance-architecture-global-brand-procurement-2026-10-21-am.html"),
        "title": ("Mill-Side Brand-Buyer AI-Powered Quality-Claim Substantiation &amp; Marketing-Claim "
                  "Review-Governance Architecture for Global Brand Procurement 2026"),
        "h3": ("Mill-Side Brand-Buyer AI-Powered Quality-Claim Substantiation &amp; Marketing-Claim "
               "Review-Governance Architecture for Global Brand Procurement 2026"),
        "desc": ("B2B ribbon OEM 252-module AI-powered quality-claim substantiation and marketing-claim "
                 "review-governance architecture. 5-layer claim-evidence stack, 6-stage substantiation cascade, "
                 "4-gate claim-release workflow, 5-tier claim-confidence classification. EU 2024/825 and FTC Green "
                 "Guides ready. Smith Ribbon OEM since 2004."),
        "cat": "AI-Powered Quality-Claim Substantiation / Marketing-Claim Review Governance",
    },
    {
        "file": ("blog-ribbon-oem-253-module-mill-side-brand-buyer-contract-manufacturing-scope-creep-change-order-"
                 "control-architecture-global-brand-procurement-2026-10-21-pm.html"),
        "title": ("Mill-Side Brand-Buyer Contract-Manufacturing Scope-Creep &amp; Change-Order Control "
                  "Architecture for Global Brand Procurement 2026"),
        "h3": ("Mill-Side Brand-Buyer Contract-Manufacturing Scope-Creep &amp; Change-Order Control "
               "Architecture for Global Brand Procurement 2026"),
        "desc": ("B2B ribbon OEM 253-module contract-manufacturing scope-creep and change-order control architecture. "
                 "5-tier change-classification ladder, 6-stage change-control workflow, 4-gate change-authorisation "
                 "chain, baseline-freeze integrity model. Recovers 3-7% of margin lost to absorbed scope drift. "
                 "Smith Ribbon OEM since 2004."),
        "cat": "Contract-Manufacturing Scope-Creep / Change-Order Control",
    },
]

for a in ARTICLES:
    # ---------- blog.html ----------
    bp = ROOT / "blog.html"
    blog = bp.read_text(encoding="utf-8")
    if a["file"] in blog:
        print(f"[SKIP] blog.html already has {a['file'][:40]}")
    else:
        card = (
            f'<article class="post-card">\n  <a href="/{a["file"]}">\n'
            f'    <h3>{a["h3"]}</h3>\n  </a>\n'
            f'  <p>{a["desc"]}</p>\n'
            f'  <div class="post-meta">{DATE} &middot; {a["cat"]}</div>\n</article>'
        )
        idx = blog.rfind("</article>")
        if idx == -1:
            raise SystemExit("could not locate last </article> in blog.html")
        idx += len("</article>")
        bp.write_text(blog[:idx] + "\n" + card + blog[idx:], encoding="utf-8")
        print(f"[OK] blog.html + {a['file'][:40]}")

    # ---------- index.html ----------
    ip = ROOT / "index.html"
    idxh = ip.read_text(encoding="utf-8")
    if a["file"] in idxh:
        print(f"[SKIP] index.html already has {a['file'][:40]}")
    else:
        m = idxh.rfind("</li>")
        if m == -1:
            raise SystemExit("no </li> found in index.html")
        m += len("</li>")
        ip.write_text(idxh[:m] + f'\n<li><a href="blog/{a["file"]}">{a["title"]}</a></li>' + idxh[m:],
                     encoding="utf-8")
        print(f"[OK] index.html + {a['file'][:40]}")

    # ---------- sitemap.xml ----------
    sp = ROOT / "sitemap.xml"
    sm = sp.read_text(encoding="utf-8")
    slug = a["file"][:-5]
    if slug in sm:
        print(f"[SKIP] sitemap.xml already has {slug[:40]}")
    else:
        entry = (f'<url><loc>https://smithribbon.com/{slug}</loc><lastmod>{DATE}</lastmod>'
                 f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
        ci = sm.rfind("</urlset>")
        if ci == -1:
            raise SystemExit("</urlset> not found")
        sp.write_text(sm[:ci] + entry + sm[ci:], encoding="utf-8")
        print(f"[OK] sitemap.xml + {slug[:40]}")

# ---------- verify ----------
sm_final = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_final)
blog_final = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_final = (ROOT / "index.html").read_text(encoding="utf-8")
for a in ARTICLES:
    slug = a["file"][:-5]
    assert a["file"] in blog_final, f"blog.html missing {slug}"
    assert a["file"] in idx_final, f"index.html missing {slug}"
    assert slug in sm_final, f"sitemap.xml missing {slug}"
print("Verification OK: modules 252 + 253 linked in blog.html, index.html and sitemap.xml (valid XML)")