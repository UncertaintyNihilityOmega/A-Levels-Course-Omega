from math import comb, exp, factorial
from statistics import NormalDist
N01=NormalDist()
def x2(o,e): return sum((a-b)**2/b for a,b in zip(o,e))
def r(l,n=3): return [round(a,n) for a in l]
def c(o,e): return r([(a-b)**2/b for a,b in zip(o,e)],4)
print("T1",x2([24,18,22,15,21],[20]*5))
e=[10,30,30,10]; o=[14,27,29,10]; print("T3",c(o,e),x2(o,e))
e=[90,60,30]; o=[78,70,32]; print("T5",c(o,e),x2(o,e))
lam=1.5; p0=exp(-lam); p1=lam*p0; e=[60*p0,60*p1,60*(1-p0-p1)]; o=[10,24,26]; print("T6",r(e,4),c(o,e),x2(o,e))
# geometric 0.3
p=0.3;q=0.7
e=[100*q**(k-1)*p for k in range(1,8)]+[100*q**7]; print("G E",r(e,3))
ec=e[:6]+[e[6]+e[7]]; o=[34,20,13,12,7,5,3,6]; oc=o[:6]+[o[6]+o[7]]
print("G",r(ec,3),oc,sum(oc),c(oc,ec),x2(oc,ec))
# PDF 3x^2/8
pr=[(b**3-a**3)/8 for a,b in [(0,.5),(.5,1),(1,1.5),(1.5,2)]]; e=[160*a for a in pr]; print("PDF E",e)
oc=[3+19,44,94]; ec=[e[0]+e[1],e[2],e[3]]; print(c(oc,ec),x2(oc,ec))
# normal est
pb=[N01.cdf(-1),N01.cdf(0)-N01.cdf(-1),N01.cdf(1)-N01.cdf(0),1-N01.cdf(1)]; e=[120*a for a in pb]; o=[25,36,42,17]
print("N",r(pb,4),r(e,3),c(o,e),x2(o,e))
# typing errors Poisson
o=[40,55,31,15,7,2]; n=sum(o); lam=sum(i*f for i,f in enumerate(o))/n; print("typing",n,lam,sum(i*f for i,f in enumerate(o)))
pp=[exp(-lam)*lam**k/factorial(k) for k in range(5)]; e=[n*a for a in pp]+[n*(1-sum(pp))]; print(r(e,3),sum(e))
oc=o[:4]+[o[4]+o[5]]; ec=e[:4]+[e[4]+e[5]]; print(r(ec,3),c(oc,ec),x2(oc,ec), "P(X<=1)",exp(-lam)*(1+lam))
# seeds B(5,p)
for o in ([4,20,46,32,14,4],[6,22,45,30,14,3],[5,25,44,30,13,3]):
    n=sum(o); m=sum(i*f for i,f in enumerate(o))/n; ph=m/5
    e=[n*comb(5,k)*ph**k*(1-ph)**(5-k) for k in range(6)]
    print(o,n,m,ph,r(e,3))
    # combine last two
    oc=o[:4]+[o[4]+o[5]]; ec=e[:4]+[e[4]+e[5]]; print(r(ec,3),c(oc,ec),x2(oc,ec))
# stretch
print("S2", 4.5*3)
# T2 scenarios, try 4 combine
print(1.8+6.2,12.1+4.4)
print(sum([3.9,14.6,25.8,27.4,17.6,7.4,3.3]))
