from math import comb, exp, factorial
import importlib.util, sys
spec = importlib.util.spec_from_file_location("d", "data/fm-chisq-design.py")
# re-implement the few helpers (avoid running design.py prints)
from math import erf, sqrt, lgamma
def chi2_cdf(x, v, n=4000):
    if x <= 0: return 0.0
    if v == 1: return erf(sqrt(x/2))
    if v == 2: return 1-exp(-x/2)
    f = lambda t: t**(v/2-1)*exp(-t/2)/(2**(v/2)*exp(lgamma(v/2)))
    h = x/n
    return (f(0)+f(x)+sum((4 if i%2 else 2)*f(i*h) for i in range(1,n)))*h/3
def inv(p, v):
    lo, hi = 0.0, 400.0
    for _ in range(60):
        m=(lo+hi)/2
        lo,hi=(m,hi) if chi2_cdf(m,v)<p else (lo,m)
    return (lo+hi)/2
def x2(o,e): return sum((a-b)**2/b for a,b in zip(o,e))
def show(name,o,e,v):
    print(name,"E",[round(a,3) for a in e],"X2",round(x2(o,e),4),"v",v,"crit5",round(inv(.95,v),3),"crit1",round(inv(.99,v),3))
# poisson reject
obs=[20,22,20,14,10,8,6]; n=sum(obs); lam=sum(i*f for i,f in enumerate(obs))/n
pp=[exp(-lam)*lam**k/factorial(k) for k in range(6)]; pp.append(1-sum(pp)); e=[n*p for p in pp]
print("lam",lam,[round(a,3) for a in e])
# ratio
show("ratio",[160,84,52,24],[180,60,60,20],3)
# binomial B(6,p) overdispersed
for obs in ([55,62,41,26,10,5,1],[58,64,42,22,10,3,1]):
    n=sum(obs); mean=sum(i*f for i,f in enumerate(obs))/n; ph=mean/6
    e=[n*comb(6,k)*ph**k*(1-ph)**(6-k) for k in range(7)]
    print(n,"mean",mean,"p",ph,[round(a,3) for a in e])
