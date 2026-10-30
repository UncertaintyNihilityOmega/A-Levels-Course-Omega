# data/spearman_crit.py: exact two-tailed p = 0.05 critical values of Spearman's rs for n = 5..12.
# The exact null distribution of sum D^2 is built by dynamic programming over the set of ranks used;
# the critical value is the smallest rs whose upper-tail probability is <= 0.025 (as in Zar's and
# the usual biology tables: n = 8 0.738, 9 0.700, 10 0.648, 12 0.587). Run: py data/spearman_crit.py
import sys
from math import factorial
def dist(n):
    from collections import defaultdict
    cur={0:{0:1}}
    for pos in range(n):
        nxt={}
        for mask,d in cur.items():
            for r in range(n):
                if mask>>r&1: continue
                m2=mask|1<<r; dd=(pos-r)**2
                t=nxt.setdefault(m2,{})
                for s,c in d.items(): t[s+dd]=t.get(s+dd,0)+c
        cur=nxt
    return cur[(1<<n)-1]
for n in (5,6,7,8,9,10,11,12):
    d=dist(n); N=factorial(n); den=n**3-n
    # upper tail of rs = small sum D^2
    ss=sorted(d); cum=0; best=None
    for s in ss:
        cum+=d[s]
        if cum/N<=0.025: best=(s,cum/N)
        else: break
    rs=1-6*best[0]/den
    # next value (first not significant)
    s2=ss[ss.index(best[0])+1]; rs2=1-6*s2/den
    print(n,'smallest sig rs=%.4f (P=%.4f)  next rs=%.4f'%(rs,best[1],rs2))
