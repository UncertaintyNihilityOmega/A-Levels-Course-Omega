from math import comb, exp, factorial, erf, sqrt, lgamma
from statistics import NormalDist
N01=NormalDist()
def x2(o,e): return sum((a-b)**2/b for a,b in zip(o,e))
def r(l,n=3): return [round(a,n) for a in l]
# eg1 die
o=[15,25,22,18,24,16]; e=[20]*6
print("die",x2(o,e), sum(a*a/20 for a in o)-120)
# eg2 ratio
o=[160,84,52,24]; e=[180,60,60,20]
print("ratio contrib",r([(a-b)**2/b for a,b in zip(o,e)],4),x2(o,e))
# eg poisson
obs=[20,22,20,14,10,8,6]; n=100; lam=2.2
pp=[exp(-lam)*lam**k/factorial(k) for k in range(6)]; 
print("poisson P",r(pp,5), "tail",1-sum(pp))
e=[n*p for p in pp]+[n*(1-sum(pp))]
print("E",r(e,3)); ec=e[:5]+[e[5]+e[6]]; oc=obs[:5]+[obs[5]+obs[6]]
print("combined E5+",ec[5],"contrib",r([(a-b)**2/b for a,b in zip(oc,ec)],4),x2(oc,ec))
print("var",sum(i*i*f for i,f in enumerate(obs))/n-lam**2)
# exam A binomial
obs=[55,62,41,26,10,5,1]; n=200; mean=sum(i*f for i,f in enumerate(obs))/n; ph=mean/6
e=[n*comb(6,k)*ph**k*(1-ph)**(6-k) for k in range(7)]
print("binA mean",mean,"p",ph,"E",r(e,4))
oc=obs[:4]+[sum(obs[4:])]; ec=e[:4]+[sum(e[4:])]
print("combined",oc,r(ec,4),r([(a-b)**2/b for a,b in zip(oc,ec)],4),x2(oc,ec))
# PMF spinner
o=[22,27,41,60]; e=[15,30,45,60]; print("pmf",x2(o,e),r([(a-b)**2/b for a,b in zip(o,e)],4))
# geometric
mean=2.6; p=1/mean; q=1-p
e=[100*q**(r_-1)*p for r_ in range(1,6)]+[100*q**5]; o=[41,22,14,11,5,7]
print("geo p",p,"E",r(e,3),"contrib",r([(a-b)**2/b for a,b in zip(o,e)],4),x2(o,e))
# normal
bounds=[244,248,252,256]; cdf=[N01.cdf((b-250)/4) for b in bounds]
pr=[cdf[0],cdf[1]-cdf[0],cdf[2]-cdf[1],cdf[3]-cdf[2],1-cdf[3]]
e=[200*a for a in pr]; o=[18,45,70,52,15]
print("normal z probs",r([N01.cdf(z) for z in (-1.5,-.5,.5,1.5)],4),"P",r(pr,4),"E",r(e,3),r([(a-b)**2/b for a,b in zip(o,e)],4),x2(o,e))
# binomial p given
pm=[comb(5,k)*0.2**k*0.8**(5-k) for k in range(6)]; e=[200*p for p in pm]
print("binG E",r(e,4)); ec=e[:3]+[sum(e[3:])]; oc=[60,88,40,12]
print(r(ec,4),r([(a-b)**2/b for a,b in zip(oc,ec)],4),x2(oc,ec))
# spot the error
obs=[29,43,28,17,3]; n=120; mean=sum(i*f for i,f in enumerate(obs))/n; ph=mean/4
e=[n*comb(4,k)*ph**k*(1-ph)**(4-k) for k in range(5)]
print("spot mean",mean,"p",ph,"E",r(e,3)); oc=obs[:3]+[obs[3]+obs[4]]; ec=e[:3]+[e[3]+e[4]]
print(r(ec,3),r([(a-b)**2/b for a,b in zip(oc,ec)],4),x2(oc,ec))
