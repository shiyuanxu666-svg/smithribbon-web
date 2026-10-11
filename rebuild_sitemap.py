#!/usr/bin/env python3
"""Rebuild smithribbon.com/sitemap.xml from scratch — clean, well-formed.

Fix corruption where <url> tags were nested and missing closing tags.
"""
from pathlib import Path
import re
import datetime as dt

ROOT = Path("/workspace/smithribbon-web")

# Collect all public HTML pages
def collect():
    urls = []
    for f in sorted(ROOT.rglob("*.html")):
        # Skip utility / backup / chrome files
        name = f.name
        if name.startswith(("zz", "_", ".")):
            continue
        if name.endswith(".bak") or ".bak." in name:
            continue
        # Compose public URL
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith("blog/"):
            url = f"https://smithribbon.com/{rel}"
        elif rel == "index.html":
            url = "https://smithribbon.com/"
        else:
            url = f"https://smithribbon.com/{rel}"
        # Skip if file is in /images/ or /styles/ related places
        if "/images/" in rel or "/js/" in rel or "/img/" in rel:
            continue
        # mtime -> lastmod
        mt = dt.date.fromtimestamp(f.stat().st_mtime).isoformat()
        urls.append((url, mt))
    return urls

def main():
    urls = collect()
    today = dt.date.today().isoformat()
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, lastmod in urls:
        out.append('  <url>')
        out.append(f'    <loc>{url}</loc>')
        out.append(f'    <lastmod>{lastmod}</lastmod>')
        out.append('    <changefreq>weekly</changefreq>')
        out.append('    <priority>0.80</priority>')
        out.append('  </url>')
    out.append('</urlset>')
    out.append('')
    # Backup then write
    bak = ROOT / "sitemap.xml.bak"
    src = ROOT / "sitemap.xml"
    if src.exists():
        src.replace(bak)
    src.write_text("\n".join(out), encoding="utf-8")
    print(f"[OK] smithribbon sitemap.xml rebuilt with {len(urls)} URLs")
    # validate
    import xml.etree.ElementTree as ET
    try:
        ET.parse(src)
        print("[OK] sitemap parses as valid XML")
    except ET.ParseError as e:
        print(f"[ERROR] XML parse error: {e}")

if __name__ == "__main__":
    main()
