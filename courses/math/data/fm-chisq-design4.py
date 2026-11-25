from math import comb
exec(open("data/fm-chisq-design3.py").read().split('def test')[0])
def x2(o,e): return sum((a-b)**2/b for a,b in zip(o,e))
# binomial B(4,p) estimated, N=120
for obs in ([30,44,30,12,4],[28,46,30,13,3],[25,47,31,13,4],[27,50,26,12,5],[22,50,30,14,4],[26,52,22,16,4],[24,48,32,12,4]):
    n=sum(obs); mean=sum(i*f for i,f in enumerate(obs))/n; ph=mean/4
    e=[n*comb(4,k)*ph**k*(1-ph)**(4-k) for k in range(5)]
    print(obs,"p",round(ph,4),[round(a,2) for a in e],"X2",round(x2(obs,e),3))
# contingency 3x3 combining first two columns
import itertools
def X(T):
    r=[sum(row) for row in T]; c=[sum(col) for col in zip(*T)]; N=sum(r)
    return sum((T[i][j]-r[i]*c[j]/N)**2/(r[i]*c[j]/N) for i in range(len(r)) for j in range(len(c)))
for T in ([[4,26,50],[7,38,45],[3,22,45]],[[3,22,55],[8,30,42],[3,20,47]],[[5,25,45],[6,38,56],[2,29,64]]):
    Tc=[[a+b,c] for a,b,c in T]
    print(T,"X2 full",round(X(T),3),"merged",round(X(Tc),3),"colsum",[sum(c) for c in zip(*T)])
