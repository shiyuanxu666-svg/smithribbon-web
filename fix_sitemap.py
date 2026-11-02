import os,re
sm=open('sitemap.xml',encoding='utf-8').read()
locs=re.findall(r'<loc>(.*?)</loc>',sm,re.S)
locs=[l.strip() for l in locs]
existing=set(locs)
BD='blog'
files=sorted(f for f in os.listdir(BD) if f.endswith('.html'))
def lastmod(f):
    m=re.search(r'(20\d\d-\d\d-\d\d)',f)
    return m.group(1) if m else '2026-10-21'
added=0; blocks=[]
for f in files:
    u=f'https://smithribbon.com/blog/{f}'
    if u in existing: continue
    blocks.append('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n'%(u,lastmod(f)))
    added+=1
if added:
    sm=sm.replace('</urlset>',''.join(blocks)+'</urlset>')
    # atomic write
    tmp=sitemap_tmp='sitemap.xml.tmp'
    open(tmp,'w',encoding='utf-8').write(sm)
    os.replace(tmp,'sitemap.xml')
print("added:",added,"| new total:",len(locs)+added)
