from math import comb, sqrt
from fractions import Fraction as F
from itertools import combinations
from statistics import NormalDist
N=NormalDist()
def bcdf(n,k): return F(sum(comb(n,i) for i in range(0,k+1)),2**n)
def sr_dist(n):
    # distribution of sum of ranks of positive signs
    c=[0]*(n*(n+1)//2+1); c[0]=1
    for r in range(1,n+1):
        for s in range(len(c)-1,r-1,-1): c[s]+=c[s-r]
    return c
def sr_crit(n,a):
    c=sr_dist(n); tot=2**n; cum=0; best=None
    for t in range(len(c)):
        cum+=c[t]
        if F(cum,tot)<=a: best=t
        else: break
    return best
def rs_dist(m,n):
    from collections import Counter
    c=Counter(sum(s) for s in combinations(range(1,m+n+1),m)); return c
def rs_crit(m,n,a):
    c=rs_dist(m,n); tot=comb(m+n,m); cum=0; best=None
    for w in range(m*(m+1)//2, m*(2*n+m+1)//2+1):
        cum+=c.get(w,0)
        if F(cum,tot)<=a: best=w
        else: break
    return best
print("sign crit n=6..20 (5%,2.5%,1%)")
for n in range(6,21):
    row=[]
    for a in (F(5,100),F(25,1000),F(1,100)):
        b=None
        for k in range(0,n+1):
            if bcdf(n,k)<=a: b=k
            else: break
        row.append(b)
    print(n,row)
print("signed rank table")
for n in range(6,21):
    print(n,[sr_crit(n,F(a)) for a in ("0.05","0.025","0.01","0.005")])
for (m,n) in [(3,3),(3,4),(4,4),(5,5),(5,7),(6,8),(7,9),(8,8),(10,10),(4,7),(6,6)]:
    print("RS",m,n,[rs_crit(m,n,F(a)) for a in ("0.05","0.025","0.01")])
