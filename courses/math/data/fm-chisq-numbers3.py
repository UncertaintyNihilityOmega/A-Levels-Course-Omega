from math import comb, exp
def x2(o,e): return sum((a-b)**2/b for a,b in zip(o,e))
def r(l,n=3): return [round(a,n) for a in l]
def c(o,e): return r([(a-b)**2/b for a,b in zip(o,e)],4)
o=[4,20,46,32,14,4]; n=120; m=sum(i*f for i,f in enumerate(o))/n; ph=m/5
e=[n*comb(5,k)*ph**k*(1-ph)**(5-k) for k in range(6)]
oc=[o[0]+o[1],o[2],o[3],o[4]+o[5]]; ec=[e[0]+e[1],e[2],e[3],e[4]+e[5]]
print(m,ph,r(e,4),r(ec,4),oc,c(oc,ec),x2(oc,ec))
# T6 ν details, S1
# EP5 sums
print(24.01/40.961)
# geometric T? skip
# stretch S2: threshold k
print(11.070/4.5)
# S1 check: two classes
n=100;p=0.3;x=40
print((x-n*p)**2/(n*p)+((n-x)-n*(1-p))**2/(n*(1-p)), (x-n*p)**2/(n*p*(1-p)))
# S3 contingency stretch later
