import re,sys
S=sys.argv[1]
nm={};syms=[]
for l in open(S+'/nm.txt'):
    p=l.split()
    if len(p)==4: syms.append((int(p[0],16),int(p[1],16),p[2],p[3]))
    if len(p)==4 and p[2] in 'tTwW': nm.setdefault(p[3],(int(p[0],16),int(p[1],16)))
def symat(x):
    best=None
    for a,sz,t,n in syms:
        if a<=x<a+max(sz,1): best=(n,t,a);break
    return best
hot=[l.split()[1] for l in open(S+'/hot.txt')]
ranges={n:nm[n] for n in hot if n in nm}
words={}
for l in open(S+'/dis.txt'):
    m=re.match(r'^\s*([0-9a-f]+):\s+\.word\s+0x([0-9a-f]+)',l)
    if m: words[int(m.group(1),16)]=int(m.group(2),16)
for n,(a,sz) in ranges.items():
    out=[]
    for wa,w in words.items():
        if a<=wa<a+sz and 0x08000000<=w<0x08020000:
            s=symat(w&~1); out.append(f"{w:08x}={s[0] if s else '?'}({s[1] if s else ''})")
    if out: print(n, ' '.join(sorted(set(out))))
