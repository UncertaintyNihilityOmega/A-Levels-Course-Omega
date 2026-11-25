exec(open('data/fm-nonpar-explore.py').read().split('print("sign crit')[0])
from statistics import NormalDist
N=NormalDist()
def ranks(vals):
    s=sorted(vals); return [s.index(v)+1 for v in vals]
def sr(d):
    a=[abs(x) for x in d]; r=ranks(a)
    P=sum(rk for rk,x in zip(r,d) if x>0); Q=sum(rk for rk,x in zip(r,d) if x<0); return r,P,Q
print("battery", sr([-6,-2,1,-7,-9,3,-4,-8,-5]))
print("pairs", sr([14,9,-3,22,7,18,-5,11,25,16]))
print("ex1", sr([-7,11,-12,5,-3,-14,9,-1]))
# rank sum
def rsum(A,B):
    allv=sorted(A+B); rk={v:i+1 for i,v in enumerate(allv)}
    return sum(rk[v] for v in A), sum(rk[v] for v in B)
print("Y,X", rsum([36,43,39,35,46,37],[41,38,47,52,44,49,40,55]))
print("q2", rsum([12,15,9,20],[14,8,17,22,18,11]), [rs_crit(4,6,F(a)) for a in ("0.05","0.025","0.01")])
# normal approx
n=24; mu=n*(n+1)/4; sd=(n*(n+1)*(2*n+1)/24)**.5; print(mu,sd,(88.5-mu)/sd,N.cdf((88.5-mu)/sd))
m,nn=12,15; mu=m*(m+nn+1)/2; sd=(m*nn*(m+nn+1)/12)**.5; print(mu,sd,(128.5-mu)/sd,N.cdf((128.5-mu)/sd))
n=30; mu=n*(n+1)/4; sd=(n*(n+1)*(2*n+1)/24)**.5; print(mu,sd,(150.5-mu)/sd,N.cdf((150.5-mu)/sd))
# q3 matched pairs two-tailed n=9 
before=[82,75,91,68,77,85,72,88,79]; after=[78,77,83,65,70,86,60,79,71]
d=[b-a for b,a in zip(before,after)]; print(d, sr(d), [sr_crit(9,F(a)) for a in ("0.05","0.025")])
# q4 rank sum two-tailed
A=[31,25,38,29,34]; B=[27,36,42,33,40,45,39]; print("q4",rsum(A,B),[rs_crit(5,7,F(a)) for a in ("0.05","0.025","0.01")])
# q6 paired n=9
d6=[6,-2,9,4,-1,11,7,3,-12]; print("q6",sr(d6), sr_crit(9,F("0.05")))
# q7 normal rank sum m=11 n=14
m,nn=11,14; mu=m*(m+nn+1)/2; sd=(m*nn*(m+nn+1)/12)**.5; print(mu,sd,(172.5-mu)/sd, 2*N.cdf((172.5-mu)/sd), (176.5-mu)/sd)
print([ (s,c) for s,c in enumerate(sr_dist(5))])
print([ (s,c) for s,c in enumerate(sr_dist(4))])
