import sys,collections
S=sys.argv[1]
nm={}
for l in open(S+'/nm.txt'):
    p=l.split()
    if len(p)==4 and p[2] in 'tTwW': nm.setdefault(p[3],(int(p[0],16),int(p[1],16),p[2]))
osec=collections.defaultdict(list)
for l in open(S+'/osec.txt'):
    o,sec,sz=l.split(); osec[sec].append((o,int(sz,16)))
tot=collections.Counter(); seen=set()
for l in open(S+'/hot.txt'):
    g,n=l.split()
    if n not in nm: print('MISSING',n); continue
    a,sz,t=nm[n]
    base=n.split('.part')[0].split('.constprop')[0].split('.isra')[0]
    sec='.text.'+base
    objs=osec.get(sec,[])
    if not objs:
        cand=[s for s in osec if s.startswith('.text') and base in s]
        objs=[(o+'?'+s,0) for s in cand for o,_ in osec[s]]
    # pick obj whose section size >= sz
    print(f"{g} {a:08x} {sz:5d} {t} {n:55s} {sec:60s} {';'.join(o for o,_ in objs)}")
    if (a) not in seen:
        seen.add(a); tot[g]+=sz
print(dict(tot), sum(tot.values()))
