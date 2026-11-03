#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish smithribbon articles 303 (AM) + 304 (PM) - 2026-11-03.

Also fixes the hardcoded 'Published October 28, 2026' meta line that
smithribbon_article_lib.write_article() writes for every article, replacing
it with the correct publication date for this run.

Updates: blog.html, en-blog.html, index.html, sitemap.xml.
Single verify pass at the end.

NOTE: legacy blog/ files keep their /blog/ prefixed sitemap URLs - those are
correct (200) and must NOT be rewritten. Only these two new root-level
module articles get root-level locs.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import re

ROOT = Path("/workspace/smithribbon-web")
DATE = "2026-11-03"

ARTICLES = [
    {
        "file": ("blog-ribbon-oem-303-module-brand-buyer-supplier-code-of-conduct-ethical-sourcing-"
                 "sign-off-audit-rights-labour-compliance-ribbon-trim-programmes-2026-11-03-am.html"),
        "title": ("The Supplier Code of Conduct &mdash; How Brand Buyers Structure Labour and Ethical "
                  "Sourcing Sign-off for Ribbon and Decorative Trim Programmes 2026"),
        "desc": ("A brand-buyer guide to supplier code of conduct acceptance for ribbon and decorative trim: "
                 "what a ribbon-specific code should cover, how to structure audit rights, how to link labour "
                 "findings to the commercial relationship, and how to verify that a signature means something."),
        "cat": "Ethical Sourcing &amp; Social Compliance",
    },
    {
        "file": ("blog-ribbon-oem-304-module-brand-buyer-ribbon-should-cost-model-quantity-build-material-"
                 "conversion-cost-landed-cost-bridge-negotiation-discipline-2026-11-03-pm.html"),
        "title": ("Build Your Own Should-Cost Model for Ribbon &mdash; Quantity Build, Conversion Layers and "
                  "the Landed Cost Bridge: A Guide for Brand Buyers Who Want to Read a Quotation Properly "
                  "2026"),
        "desc": ("A brand-buyer guide to building a should-cost model for ribbon and decorative trim: the "
                 "quantity build, material and conversion cost layers, which assumptions actually move the "
                 "price, how to read a quotation against your own number, and how to build the ex-works to "
                 "landed cost bridge without damaging the supplier relationship."),
        "cat": "Costing, Pricing &amp; Quote Analysis",
    },
]


# ---------- 0. fix hardcoded publish date in the two new articles ----------
for art in ARTICLES:
    p = ROOT / art["file"]
    t = p.read_text(encoding="utf-8")
    old = "Published October 28, 2026 &middot; Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; 16 min read"
    new = "Published November 3, 2026 &middot; Xiamen Smith Ribbon &amp; Bow Co., Ltd. &middot; 16 min read"
    if old in t:
        t = t.replace(old, new)
        p.write_text(t, encoding="utf-8")
        print(f"[OK] fixed publish date in {art['file'][:44]}")
    else:
        print(f"[WARN] publish date pattern not found in {art['file'][:44]}")


def card(art):
    return (
        f'<article class="post-card">\n  <a href="{art["file"]}">\n'
        f'    <h3>{art["title"]}</h3>\n  </a>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="post-meta">{DATE} &middot; {art["cat"]}</div>\n</article>'
    )


# ---------- 1. blog.html : insert after last </article> (newest at end) ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
cards = []
for art in ARTICLES:
    if art["file"] in blog:
        print(f"[SKIP] blog.html already has {art['file'][:40]}")
        continue
    cards.append(card(art))
if cards:
    i = blog.rfind("</article>")
    assert i != -1, "no </article> in blog.html"
    i += len("</article>")
    bp.write_text(blog[:i] + "\n" + "\n".join(cards) + blog[i:], encoding="utf-8")
    print(f"[OK] blog.html + {len(cards)} card(s)")

# ---------- 2. en-blog.html : same card pattern ----------
ep = ROOT / "en-blog.html"
try:
    en = ep.read_text(encoding="utf-8")
    ecards = []
    for art in ARTICLES:
        if art["file"] in en:
            print(f"[SKIP] en-blog.html already has {art['file'][:40]}")
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

# ---------- 3. index.html : root-level href ----------
ip = ROOT / "index.html"
idx = ip.read_text(encoding="utf-8")
added = 0
for art in ARTICLES:
    if art["file"] in idx:
        print(f"[SKIP] index.html already has {art['file'][:40]}")
        continue
    m = idx.rfind("</li>")
    assert m != -1, "no </li> in index.html"
    m += len("</li>")
    idx = idx[:m] + f'\n<li><a href="{art["file"]}">{art["title"]}</a></li>' + idx[m:]
    added += 1
if added:
    ip.write_text(idx, encoding="utf-8")
    print(f"[OK] index.html + {added} link(s)")

# ---------- 4. sitemap.xml : root-level loc ----------
sp = ROOT / "sitemap.xml"
sm = sp.read_text(encoding="utf-8")
for art in ARTICLES:
    loc = "https://smithribbon.com/" + art["file"]
    if loc in sm:
        print(f"[SKIP] sitemap has {loc[-50:]}")
        continue
    entry = (f'<url><loc>{loc}</loc><lastmod>{DATE}</lastmod>'
             f'<changefreq>monthly</changefreq><priority>0.8</priority></url>')
    ci = sm.rfind("</urlset>")
    assert ci != -1, "no </urlset> in sitemap.xml"
    sm = sm[:ci] + entry + sm[ci:]
sp.write_text(sm, encoding="utf-8")
print("[OK] sitemap.xml updated")

# ================= VERIFY (single pass) =================
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
locs = [l.text for l in ET.fromstring(sm_f).iter() if l.tag.endswith("loc")]
dups = len(locs) - len(set(locs))
missing = []
for l in locs:
    rel = l.replace("https://smithribbon.com/", "")
    if not (ROOT / rel).is_file():
        missing.append(rel)
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")
en_f = (ROOT / "en-blog.html").read_text(encoding="utf-8")
print("\n=== VERIFY ===")
print(f"sitemap locs={len(locs)} unique={len(set(locs))} dups={dups} xml=OK")
print(f"missing files={len(missing)}")
for x in missing[:10]:
    print("   MISSING:", x)
for art in ARTICLES:
    inb = art["file"] in blog_f
    ini = art["file"] in idx_f
    ine = art["file"] in en_f
    ins = ("https://smithribbon.com/" + art["file"]) in sm_f
    ok = all([inb, ini, ine, ins])
    print(f"{'OK ' if ok else 'FAIL'} {art['file'][:44]}... blog={inb} index={ini} enblog={ine} sitemap={ins}")
legacy = [l for l in locs if "/blog/blog-" in l]
print(f"legacy /blog/blog-xxx locs preserved = {len(legacy)}")
future = [l for l in sm_f.split("<lastmod>")[1:] if l[:10] > DATE]
print(f"future lastmod entries = {len(future)}")

# article content sanity
faq_marker = 'id="faq"'
for art in ARTICLES:
    t = (ROOT / art["file"]).read_text(encoding="utf-8")
    words = len(re.sub(r"<[^>]+>", " ", t).split())
    has_faq = faq_marker in t
    has_2004 = "since 2004" in t.lower()
    stale = "2007" in t
    has_footer = "Professional Ribbon Manufacturer Since 2004" in t
    n_faq_q = t.count('"@type": "Question"')
    n_blogposting = '"@type": "BlogPosting"' in t
    n_faqpage = '"@type": "FAQPage"' in t
    print(f"  {art['file'][:30]}... rendered_words={words} "
          f"faq_h={has_faq} faqQ={n_faq_q} BP={n_blogposting} FP={n_faqpage} "
          f"since2004={has_2004} stale2007={stale} footer={has_footer}")
