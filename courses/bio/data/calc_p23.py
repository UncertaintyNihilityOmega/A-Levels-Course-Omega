import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crit import chi2_crit, t_crit, r_crit
print("crit", chi2_crit(1), chi2_crit(3), t_crit(22), t_crit(28), t_crit(14), r_crit(8), r_crit(10))
# S1 chi2
O=[171,68,57,24];E=[180,60,60,20]
print("S1", sum((o-e)**2/e for o,e in zip(O,E)))
# S2 t
m1,s1,n1,m2,s2,n2=34.2,4.1,12,29.6,3.6,12
t=abs(m1-m2)/math.sqrt(s1**2/n1+s2**2/n2); print("S2 t",t, s1**2/n1, s2**2/n2)
# S3 spearman
x=[23,41,15,36,52,28,47,33]; y=[14,52,20,33,68,24,57,41]
def rank(v):
    s=sorted(v,reverse=True); return [s.index(a)+1 for a in v]
rx,ry=rank(x),rank(y); D=[a-b for a,b in zip(rx,ry)]; print("S3",rx,ry,D,sum(d*d for d in D),1-6*sum(d*d for d in D)/(8**3-8))
# mock Q7
O=[196,28,24,72];E=[180,60,60,20]
print("Q7",sum((o-e)**2/e for o,e in zip(O,E)), [(o-e)**2/e for o,e in zip(O,E)], sum(O))
# mock Q8 t
m1,s1,n1,m2,s2,n2=18.6,1.9,15,17.3,2.2,15
print("Q8 t", abs(m1-m2)/math.sqrt(s1**2/n1+s2**2/n2), s1**2/n1, s2**2/n2)
