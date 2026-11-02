#!/usr/bin/env python3
"""Update blog.html, index.html, sitemap.xml with smithribbon modules 254 (AM) + 255 (PM), 2026-10-22."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-10-22"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-254-module-mill-side-brand-buyer-lab-dip-physical-swatch-library-colour-approval-"
                 "sign-off-architecture-global-brand-procurement-2026-10-22-am.html"),
        "title": ("Mill-Side Brand-Buyer Lab Dip &amp; Physical Swatch-Library Colour-Approval Sign-Off "
                  "Architecture for Global Brand Procurement 2026"),
        "h3": ("Mill-Side Brand-Buyer Lab Dip &amp; Physical Swatch-Library Colour-Approval Sign-Off "
               "Architecture for Global Brand Procurement 2026"),
        "desc": ("B2B ribbon OEM 254-module lab-dip and physical swatch-library colour-approval sign-off "
                 "architecture. 5-tier sign-off authority ladder, 6-stage lab-dip release workflow, 4-gate "
                 "colour-approval chain, colour-master and swatch-archive model. Cuts colour approval from "
                 "18-32 days to 3-6 days and holds Delta-E under 1.0. Smith Ribbon OEM since 2004."),
        "cat": "Lab Dip / Physical Swatch-Library Colour-Approval Sign-Off",
    },
    {
        "file": ("blog-ribbon-oem-255-module-mill-side-brand-buyer-lab-dip-to-scale-up-capacity-release-"
                 "yarn-ou-lot-interlock-architecture-global-brand-procurement-2026-10-22-pm.html"),
        "title": ("Mill-Side Brand-Buyer Lab-Dip-to-Scale-Up Capacity-Release &amp; Yarn-OU-Lot Interlock "
                  "Architecture for Global Brand Procurement 2026"),
        "h3": ("Mill-Side Brand-Buyer Lab-Dip-to-Scale-Up Capacity-Release &amp; Yarn-OU-Lot Interlock "
               "Architecture for Global Brand Procurement 2026"),
        "desc": ("B2B ribbon OEM 255-module lab-dip-to-scale-up capacity-release and yarn-lot interlock "
                 "architecture. 5-tier capacity-release authority ladder, 6-stage release-to-roll workflow, "
                 "4-gate interlock chain, yarn-lot reservation and fair-queuing model. Cuts approval-to-production "
                 "from 14-24 days to 2-4 days. Smith Ribbon OEM since 2004."),
        "cat": "Lab-Dip-to-Scale-Up Capacity-Release / Yarn-Lot Interlock",
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
    assert (ROOT / a["file"]).exists(), f"article file missing {slug}"
print("Verification OK: modules 254 + 255 linked in blog.html, index.html and sitemap.xml (valid XML)")