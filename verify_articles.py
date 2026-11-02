import re, os, glob
for f in sorted(glob.glob("/workspace/smithribbon-web/blog-ribbon-oem-5[67]-module-*2026-08-17*.html")):
    txt = open(f).read()
    h2 = len(re.findall(r'<h2>', txt))
    body = re.sub(r'<[^>]+>', ' ', txt)
    words = len(body.split())
    schema = "BlogPosting" in txt
    canonical = "https://smithribbon.com/" in txt
    print(f"{os.path.basename(f)}")
    print(f"  h2={h2} words={words} schema={schema} canonical={canonical}")
