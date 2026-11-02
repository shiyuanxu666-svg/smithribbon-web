import os,re,html
BD='blog'
files=sorted(f for f in os.listdir(BD) if f.endswith('.html'))
fixed=0; skipped=0; report=[]
for f in files:
    p=os.path.join(BD,f)
    h=open(p,encoding='utf-8').read()
    if re.search(r'<h1[\s>]',h,re.I):
        skipped+=1; continue
    t=re.search(r'<title>(.*?)</title>',h,re.S|re.I)
    if not t:
        report.append((f,'no-title')); continue
    title=html.unescape(t.group(1)).strip()
    # strip trailing year/site suffix noise, keep readable
    title=re.split(r'\s*[|–—-]\s*(Smith|20\d\d\s*$|B2B)',title)[0].strip(' |–—-')
    h1='<h1>%s</h1>'%html.escape(title,quote=False)
    # insert right after <body ...> or after </head>
    m=re.search(r'<body[^>]*>',h,re.I)
    if m:
        h=h[:m.end()]+'\n  '+h1+'\n'+h[m.end():]
    else:
        m2=re.search(r'</head>',h,re.I)
        h=h[:m2.end()]+'\n<body>\n  '+h1+'\n'+h[m2.end():]
    open(p,'w',encoding='utf-8').write(h)
    fixed+=1
print("added h1:",fixed,"| already had h1:",skipped,"| skipped:",report[:5])
