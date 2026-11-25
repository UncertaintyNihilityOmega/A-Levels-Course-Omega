from math import sqrt
def tab(T):
    r=[sum(row) for row in T]; c=[sum(col) for col in zip(*T)]; N=sum(r)
    E=[[ri*cj/N for cj in c] for ri in r]
    C=[[(T[i][j]-E[i][j])**2/E[i][j] for j in range(len(c))] for i in range(len(r))]
    return r,c,N,E,C,sum(map(sum,C))
def show(n,T):
    r,c,N,E,C,X=tab(T); print(n,r,c,N,"\n E",[[round(x,3) for x in a] for a in E],"\n C",[[round(x,4) for x in a] for a in C],"X2",round(X,4))
show("Q6 merged",[[33,46,35],[26,26,38],[14,22,14]])
show("Q6 orig",[[3,4,7],[30,42,28],[26,26,38],[14,22,14]])
show("sat2 merged",[[36,44],[56,64],[28,72]])
show("sat2 orig",[[2,34,44],[6,50,64],[2,26,72]])
show("EP4 full",[[18,22,20],[32,28,30]])
show("EP3",[[3,25,52],[9,38,63],[8,27,65]])
show("EP1",[[30,25,15],[20,30,30],[10,25,45]])
show("EP2",[[45,55],[30,70]])
show("Q7",[[56,24],[64,56]])
show("flag",[[36,12,30,42],[38,22,40,40],[20,38,56,46]])
show("EgB orig",[[46,30,12,2],[50,38,14,8],[44,50,22,4]])
# stretch roots
A=150-3.841*(-1); 
# 150(a-20)^2 > 3.841 (a+30)(70-a)
a2=150+3.841; a1=-6000-3.841*40; a0=60000-3.841*2100
d=a1*a1-4*a2*a0; print("roots",(-a1-sqrt(d))/(2*a2),(-a1+sqrt(d))/(2*a2))
f=lambda a:150*(a-20)**2/((a+30)*(70-a))
for a in range(0,41):
    if f(a)>3.841: print(a,round(f(a),3),end="; ")
print()
print(round(f(8),3),round(f(9),3),round(f(31),3),round(f(32),3))
