import re
WEB = "/workspace/smithribbon-web"
files = ["index.html", "blog.html", "sitemap.xml"]
for fname in files:
    txt = open(f"{WEB}/{fname}").read()
    for n in (56, 57):
        slug = "spec-sheet-techpack-translation-decoder" if n == 56 else "adjacent-material-bundle-program"
        slot = "am" if n == 56 else "pm"
        pat = f"blog-ribbon-oem-{n}-module-{slug}-global-brand-procurement-2026-08-17-{slot}"
        cnt = txt.count(pat)
        print(f"{fname}: {n}-{slot} -> {cnt}")
print("---")
sm = open(f"{WEB}/sitemap.xml").read()
print("sitemap last 20 lines:")
print("\n".join(sm.splitlines()[-22:]))
