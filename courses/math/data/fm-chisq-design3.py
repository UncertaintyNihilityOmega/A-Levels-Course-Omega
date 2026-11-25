from math import erf, sqrt, lgamma, exp
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
def test(name,T):
    r=[sum(row) for row in T]; c=[sum(col) for col in zip(*T)]; N=sum(r)
    E=[[ri*cj/N for cj in c] for ri in r]
    C=[[(T[i][j]-E[i][j])**2/E[i][j] for j in range(len(c))] for i in range(len(r))]
    v=(len(r)-1)*(len(c)-1); X=sum(map(sum,C))
    print(name,"N",N,"r",r,"c",c,"\n E",[[round(x,3) for x in row] for row in E],"\n C",[[round(x,3) for x in row] for row in C],"\n X2",round(X,4),"v",v,"crit5",round(inv(.95,v),3),"crit1",round(inv(.99,v),3),"p",round(1-chi2_cdf(X,v),4),"minE",round(min(map(min,E)),2))
test("C1",[[78,22],[110,90]])
test("C2",[[28,45,17],[22,60,18]])
test("C2b",[[30,45,25],[20,55,25]])
test("C3 4 age",[[34,40,18,8],[30,42,16,12],[20,38,22,20]])
test("C3b",[[40,46,10,4],[35,50,12,3],[25,44,22,9]])
test("C4 travel Y7,9,11",[[48,30,54,18],[40,36,60,14],[26,44,62,18]])
test("C5 sat",[[14,52,34],[6,48,46],[3,40,57]])
test("C5b sat",[[4,40,56],[9,50,41],[3,30,67]])
print("=========")
test("flag",[[36,12,30,42],[38,22,40,40],[20,38,56,46]])
test("flag2",[[40,10,30,40],[32,24,44,40],[18,36,58,48]])
test("comb sat",[[2,28,50],[5,45,70],[3,27,70]])
test("comb sat2",[[2,34,44],[6,50,64],[2,26,72]])
test("ep1 3x3",[[30,25,15],[20,30,30],[10,25,45]])
test("ep3 comb",[[46,30,12,2],[50,38,14,8],[44,50,22,4]])
test("ep4 2x2 1%",[[45,55],[30,70]])
test("ep6 2x3",[[18,22,20],[32,28,30]])
test("spot",[[3,25,52],[9,38,63],[8,27,65]])
