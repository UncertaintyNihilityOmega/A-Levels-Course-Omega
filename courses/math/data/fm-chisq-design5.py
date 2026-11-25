from math import comb
import random
random.seed(3)
def x2(o,e): return sum((a-b)**2/b for a,b in zip(o,e))
found=0
for _ in range(20000):
    base=[26,50,30,12,2]
    obs=[max(0,b+random.randint(-8,8)) for b in base]
    obs[0]+=120-sum(obs)
    if min(obs)<0: continue
    n=120; mean=sum(i*f for i,f in enumerate(obs))/n; ph=mean/4
    e=[n*comb(4,k)*ph**k*(1-ph)**(4-k) for k in range(5)]
    oc=obs[:3]+[obs[3]+obs[4]]; ec=e[:3]+[e[3]+e[4]]
    if min(ec)<5: continue
    X=x2(oc,ec)
    if 6.3<X<7.5 and obs[4]>=2 and obs[4]<=5:
        print(obs,round(ph,4),[round(a,2) for a in ec],round(X,3)); found+=1
        if found>6: break
