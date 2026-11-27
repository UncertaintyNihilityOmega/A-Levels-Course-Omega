from math import *
def f(x): return ("%.1f" % x).rstrip('0').rstrip('.')
def P(x,y): return f"{f(x)} {f(y)}"
pts=[]
def chk(name,vb,*p):
    x0,y0,w,h=vb
    for (x,y) in p:
        assert x0<=x<=x0+w and y0<=y<=y0+h,(name,x,y)

# ---- rigid peg figure ----
c60,s60=cos(radians(60)),sin(radians(60))
A=(60,225); sc=36; gy=225
def rod(t): return (A[0]+t*sc*c60, A[1]-t*sc*s60)
C=rod(2/s60); B=rod(6); G=rod(3)
n=(-s60,-c60)
peg=(C[0]-4*n[0],C[1]-4*n[1])
Send=(C[0]+40*n[0],C[1]+40*n[1])
vb=(20,10,240,240)
chk('peg',vb,A,C,B,G,peg,Send,(A[0],A[1]-40),(A[0]+34,gy),(G[0],G[1]+54))
svg=[]
svg.append(f'<path class="ln thick" d="M30 {gy}H250"/>')
svg.append(f'<path class="ln thick" d="M{P(*A)}L{P(*B)}"/>')
svg.append(f'<circle class="f1 s-acc sw2" cx="{f(peg[0])}" cy="{f(peg[1])}" r="4"/>')
svg.append(f'<path class="c1" d="M{P(*A)}V{gy-40}" marker-end="url(#ah-math)"/>')
svg.append(f'<path class="c1" d="M{P(*A)}H{f(A[0]+34)}" marker-end="url(#ah-math)"/>')
svg.append(f'<path class="c1" d="M{P(*C)}L{P(*Send)}" marker-end="url(#ah-math)"/>')
svg.append(f'<path class="ln" d="M{P(*G)}V{f(G[1]+54)}" marker-end="url(#ah)"/>')
svg.append(f'<circle class="fi" cx="{f(G[0])}" cy="{f(G[1])}" r="3.5"/>')
r=28
svg.append(f'<path class="ln-m thin" d="M{f(A[0]+r)} {gy}A{r} {r} 0 0 0 {P(A[0]+r*c60,A[1]-r*s60)}"/>')
svg.append(f'<text class="tl halo" x="{f(A[0]-6)}" y="{gy-44}" text-anchor="end">R</text>')
svg.append(f'<text class="tl" x="{f(A[0]+38)}" y="{gy-4}">F</text>')
svg.append(f'<text class="tl halo" x="{f(Send[0]-4)}" y="{f(Send[1])}" text-anchor="end">S</text>')
svg.append(f'<text class="tl" x="{f(G[0]+6)}" y="{f(G[1]+50)}">100 N</text>')
svg.append(f'<text class="tl" x="{f(A[0]+34)}" y="{gy-16}">60°</text>')
svg.append(f'<text class="tl" x="{f(A[0]-6)}" y="{gy+16}" text-anchor="end">A</text>')
svg.append(f'<text class="tl" x="{f(B[0]+8)}" y="{f(B[1]+4)}">B</text>')
svg.append(f'<text class="tl" x="{f(peg[0]-12)}" y="{f(peg[1]+16)}" text-anchor="end">C</text>')
svg.append(f'<text class="tl" x="{f(G[0]+10)}" y="{f(G[1]-6)}">G</text>')
print("PEG viewBox",vb); print(chr(10).join(svg)); print()

# ---- rigid slope figure ----
al=radians(30); a=54; h=a/tan(al)
u=(cos(al),-sin(al)); nn=(-sin(al),-cos(al))
O=(130,250)
def pt(s,t): return (O[0]+s*u[0]+t*nn[0], O[1]+s*u[1]+t*nn[1])
c0,c1,c2,c3=pt(0,0),pt(2*a,0),pt(2*a,2*h),pt(0,2*h)
Gs=pt(a,h); F0=pt(a,0)
vb=(10,10,290,290)
chk('slope',vb,c0,c1,c2,c3,Gs,F0,(70,250+60*tan(al)),(260,250-130*tan(al)))
print("SLOPE",[ (round(x,1),round(y,1)) for x,y in (c0,c1,c2,c3,Gs,F0)], "h",round(h,1))
