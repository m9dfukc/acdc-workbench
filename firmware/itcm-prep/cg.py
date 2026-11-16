import re,sys,collections
S=sys.argv[1]
funcs=[]
for l in open(S+'/nm_C.txt'):
    p=l.rstrip('\n').split(' ',3)
    if len(p)==4 and p[2] in 'tTwW':
        a=int(p[0],16); sz=int(p[1],16); funcs.append((a,sz,p[3]))
funcs.sort()
byaddr={}
for a,sz,n in funcs: byaddr.setdefault(a,(sz,n))
starts=sorted(byaddr)
import bisect
def owner(x):
    i=bisect.bisect_right(starts,x)-1
    if i<0: return None
    a=starts[i]; sz,n=byaddr[a]
    return (a,n) if a<=x<a+max(sz,1) else None
edges=collections.defaultdict(set); lits=collections.defaultdict(set)
cur=None
for l in open(S+'/dis.txt'):
    m=re.match(r'^\s*([0-9a-f]+):\s+(\S+)\s*(.*)$',l)
    if not m: continue
    addr=int(m.group(1),16); op=m.group(2); rest=m.group(3)
    o=owner(addr)
    if not o: continue
    if op.startswith('b') and not op.startswith('bic') and not op.startswith('bfi') and not op.startswith('bx'):
        t=re.match(r'([0-9a-f]+)\s*<',rest)
        if t:
            tgt=int(t.group(1),16); ot=owner(tgt)
            if ot and ot[0]!=o[0]: edges[o[1]].add(ot[1])
    if op.startswith('ldr') and '[pc' in rest:
        lits[o[1]].add(rest)
import json
json.dump({k:sorted(v) for k,v in edges.items()},open(S+'/edges.json','w'),indent=0)
size={n:sz for a,(sz,n) in byaddr.items()}
addr={n:a for a,(sz,n) in byaddr.items()}
roots=sys.argv[2:]
seen=[];st=list(roots)
while st:
    f=st.pop()
    if f in seen: continue
    seen.append(f)
    st.extend(edges.get(f,()))
for f in seen: print(f"{addr.get(f,0):08x} {size.get(f,0):5d} {f}  -> {', '.join(sorted(edges.get(f,())))}")
