# data/calc_p20.py: scratch calculations that fix the data used in bio.stats, bio.planning, bio.evaluation
import sys, itertools
from math import sqrt
sys.path.insert(0, 'data')
from crit import chi2_crit, t_crit, r_crit
def mean(x): return sum(x)/len(x)
def sd(x):
    m=mean(x); return sqrt(sum((v-m)**2 for v in x)/(len(x)-1))
# stats eg1: six seedlings
x=[34,29,38,31,35,31]; print('eg1',mean(x),sum((v-mean(x))**2 for v in x),sd(x),sd(x)/sqrt(6),2*sd(x)/sqrt(6))
# chi2 woodlice
O=[66,54,38,22]; E=sum(O)/4; print('chi',E,sum((o-E)**2/E for o in O),chi2_crit(3))
# daphnia
a=[134,140,146,150,152,158,162,166]; b=[172,176,181,184,189,191,196,207]
for s in (a,b): print(sum(s),mean(s),sum((v-mean(s))**2 for v in s))
print('---')
a=[134,140,146,150,152,158,162,166]; b=[172,176,181,184,189,191,196,207]
t=abs(mean(a)-mean(b))/sqrt(sd(a)**2/8+sd(b)**2/8); print('t',sd(a),sd(b),t,t_crit(14))
# pearson: soil nitrate (mg/kg) v grass height cm, 7 sites
xs=[12,18,25,31,38,44,52]; ys=[14,19,18,27,31,30,41]
n=7; mx,my=mean(xs),mean(ys); sxy=sum(p*q for p,q in zip(xs,ys)); r=(sxy-n*mx*my)/((n-1)*sd(xs)*sd(ys))
print('pearson',mx,my,sxy,sd(xs),sd(ys),r,r_crit(7))
# spearman barnacles, 9 pairs
h=[0.5,0.9,1.2,1.8,2.1,2.6,3.0,3.4,4.1]; c=[210,180,195,120,96,110,40,52,18]
def rank(v):
    s=sorted(v); return [s.index(q)+1 for q in v]
rh,rc=rank(h),rank(c); D=[p-q for p,q in zip(rh,rc)]; n=9
print(rh,rc,D,sum(d*d for d in D),1-6*sum(d*d for d in D)/(n**3-n))
print('===')
xs=[10,20,30,40,50,60,70]; ys=[12,15,21,25,33,30,39]
n=7; mx,my=mean(xs),mean(ys); sxy=sum(p*q for p,q in zip(xs,ys)); r=(sxy-n*mx*my)/((n-1)*sd(xs)*sd(ys))
print('pearson',mx,my,sxy,sd(xs),sd(ys),r,r_crit(7), sxy-n*mx*my, (n-1)*sd(xs)*sd(ys))
