import sys; sys.path.insert(0,'data')
from math import sqrt
from crit import *
def mean(x): return sum(x)/len(x)
def sd(x):
    m=mean(x); return sqrt(sum((v-m)**2 for v in x)/(len(x)-1))
x=[9,10,11,13,14,15]; y=[2.9,3.3,3.6,4.3,4.7,5.2]; n=6
sxy=sum(a*b for a,b in zip(x,y)); r=(sxy-n*mean(x)*mean(y))/((n-1)*sd(x)*sd(y))
print('pearson',mean(x),mean(y),sxy,sd(x),sd(y),r,r_crit(6))
t=[8,9,11,12,14,15,17,19]; c=[48,52,41,35,38,22,25,14]
def rank(v):
    s=sorted(v); return [s.index(q)+1 for q in v]
rt,rc=rank(t),rank(c); D=[a-b for a,b in zip(rt,rc)]; print(rt,rc,D,[d*d for d in D],sum(d*d for d in D),1-6*sum(d*d for d in D)/(8**3-8))
print('finch',0.6/sqrt(50),9.4-2*0.6/sqrt(50),9.4+2*0.6/sqrt(50))
O=[96,28,25,11];E=[90,30,30,10];print('maize',sum((o-e)**2/e for o,e in zip(O,E)),chi2_crit(3))
print('multi',1-0.95**20)
print(7/2*sqrt(10))
