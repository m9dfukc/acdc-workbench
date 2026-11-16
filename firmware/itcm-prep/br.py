import re,sys,collections,bisect
S=sys.argv[1]
nm={}
for l in open(S+'/nm.txt'):
    p=l.split()
    if len(p)==4 and p[2] in 'tTwW': nm.setdefault(p[3],(int(p[0],16),int(p[1],16)))
hot=[l.split()[1] for l in open(S+'/hot.txt')]
st=sorted(set(v for v in nm.values()))
cnt=collections.Counter()
for l in open(S+'/dis.txt'):
    m=re.match(r'^\s*([0-9a-f]+):\s+(b\S*)\s+([0-9a-f]+)\s+<([^>+]+)',l)
    if not m: continue
    a=int(m.group(1),16); op=m.group(2); tgt=m.group(4)
    if op in('bic','bics','bfi','bfc','bx','blx'): continue
    for n in hot:
        if n in nm:
            fa,fs=nm[n]
            if fa<=a<fa+fs and not tgt.startswith(n.split('.')[0][:20]) and int(m.group(3),16) not in range(fa,fa+fs):
                cnt[(op if op in('bl','b.w') else 'cond/other:'+op)]+=1
                if op not in ('bl','b.w'): print(n,op,tgt)
print(cnt)
