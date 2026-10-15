# data/mk_fig_energetics.py: builds the SVG snippets for the figures of chem.energetics and checks label clearances.
# Run: py -X utf8 data/mk_fig_energetics.py [name]   (prints the <svg> body to paste into the chapter)
import sys, math

def tw(s):  # width of a 13 px label: ~7 px per character
    return 7 * len(s)

class Fig:
    def __init__(self): self.out=[]; self.labels=[]; self.segs=[]
    def add(self, s): self.out.append(s)
    def seg(self, pts): self.segs.append(pts)
    def label(self, x, y, text, anchor='start', cls='tl', halo=False):
        w=tw(text)
        x0 = x if anchor=='start' else (x-w if anchor=='end' else x-w/2)
        a = {'start':'', 'end':' text-anchor="end"', 'middle':' tc'}[anchor]
        c = cls + (' tc' if anchor=='middle' else '') + (' halo' if halo else '')
        ta = ' text-anchor="end"' if anchor=='end' else ''
        self.add(f'<text class="{c}" x="{x}" y="{y}"{ta}>{text}</text>')
        self.labels.append((text, x0, y-10, x0+w, y+3))
    def check(self, extra_ok=()):
        bad=0
        L=self.labels
        for i,(t,x0,y0,x1,y1) in enumerate(L):
            for j,(t2,a0,b0,a1,b1) in enumerate(L):
                if j<=i: continue
                if x0-4<a1 and a0-4<x1 and y0-4<b1 and b0-4<y1:
                    print('LABEL OVERLAP', t, '|', t2); bad+=1
            for pts in self.segs:
                for (p,q) in zip(pts, pts[1:]):
                    n=int(max(abs(q[0]-p[0]),abs(q[1]-p[1]))/2)+1
                    for k in range(n+1):
                        u=k/n; x=p[0]+(q[0]-p[0])*u; y=p[1]+(q[1]-p[1])*u
                        if x0-4<x<x1+4 and y0-4<y<y1+4:
                            print('LINE NEAR LABEL', t, (round(x),round(y))); bad+=1; break
        print('problems:', bad)
        return bad

def bez(p0,p1,p2,p3,n=40):
    return [tuple((1-t)**3*p0[i]+3*(1-t)**2*t*p1[i]+3*(1-t)*t**2*p2[i]+t**3*p3[i] for i in (0,1)) for t in [k/n for k in range(n+1)]]

def profile(ox, exo=True):
    """one reaction-pathway panel; ox = x of the y-axis"""
    f=Fig()
    base=205
    top=40
    f.add(f'<path class="ax" d="M{ox} {base}V{top-8}" marker-end="url(#ahm)"/>')
    f.add(f'<path class="ax" d="M{ox} {base}H{ox+270}" marker-end="url(#ahm)"/>')
    f.seg([(ox,base),(ox,top-8)]); f.seg([(ox,base),(ox+270,base)])
    f.label(ox+8, 24, 'enthalpy')
    f.label(ox+270, base+22, 'progress of reaction', 'end')
    return f

def panel(ox, exo):
    f=profile(ox, exo)
    if exo: yr, yp = 105, 155
    else: yr, yp = 155, 105
    peak=48
    xr0,xr1 = ox+40, ox+95      # reactant level
    xp0,xp1 = ox+175, ox+225    # product level
    xpk=(xr1+xp0)/2
    f.add(f'<path class="ln thick" d="M{xr0} {yr}H{xr1}"/>'); f.seg([(xr0,yr),(xr1,yr)])
    f.add(f'<path class="ln thick" d="M{xp0} {yp}H{xp1}"/>'); f.seg([(xp0,yp),(xp1,yp)])
    c1=bez((xr1,yr),(xr1+22,yr),(xpk-22,peak),(xpk,peak)); c2=bez((xpk,peak),(xpk+22,peak),(xp0-22,yp),(xp0,yp))
    f.add(f'<path class="c1 sw2" d="M{xr1} {yr}C{xr1+22} {yr} {xpk-22} {peak} {xpk} {peak}C{xpk+22} {peak} {xp0-22} {yp} {xp0} {yp}"/>')
    f.seg(c1); f.seg(c2)
    # dashed guide from reactant level to the right end
    xg=xp1+22
    f.add(f'<path class="ln-m thin dash" d="M{xr1} {yr}H{xg+8}"/>'); f.seg([(xr1,yr),(xg+8,yr)])
    # DH arrow at xg
    ym=(yr+yp)/2
    s=1 if yp>yr else -1
    f.add(f'<path class="c2 sw2" d="M{xg} {ym}V{yr+s*3}" marker-end="url(#ah)"/>')
    f.add(f'<path class="c2 sw2" d="M{xg} {ym}V{yp-s*3}" marker-end="url(#ah)"/>')
    f.seg([(xg,yr),(xg,yp)])
    f.label(xg+9, ym+4, 'ΔH')
    # Ea arrow at the left, with a dashed guide from the peak
    xe=ox+22
    ye=(yr+peak)/2
    f.add(f'<path class="ln-m thin dash" d="M{xe} {peak}H{xpk-4}"/>'); f.seg([(xe,peak),(xpk-4,peak)])
    f.add(f'<path class="ln-m thin dash" d="M{xe} {yr}H{xr0}"/>'); f.seg([(xe,yr),(xr0,yr)])
    f.add(f'<path class="c2 sw2" d="M{xe} {ye}V{peak+3}" marker-end="url(#ah)"/>')
    f.add(f'<path class="c2 sw2" d="M{xe} {ye}V{yr-3}" marker-end="url(#ah)"/>')
    f.seg([(xe,peak),(xe,yr)])
    # level labels
    if exo:
        f.label((xr0+xr1)/2, yr-10, 'reactants', 'middle')
        f.label((xp0+xp1)/2, yp+20, 'products', 'middle')
    else:
        f.label((xr0+xr1)/2, yr+20, 'reactants', 'middle')
        f.label((xp0+xp1)/2, yp-10, 'products', 'middle')
    # Ea label: left of arrow if space
    f.label(xe+8, ye+4 if not exo else 66, 'Eₐ')
    f.label(ox+125, 232 + 14, 'exothermic: ΔH negative' if exo else 'endothermic: ΔH positive', 'middle', 'tl')
    return f

if __name__=='__main__':
    which=sys.argv[1] if len(sys.argv)>1 else 'profile'
    if which=='profile':
        a=panel(20, True); b=panel(315, False)
        a.check(); b.check()
        print("\n".join(a.out)); print("\n".join(b.out))

# ---------------------------------------------------------------- cooling-curve graph
def cooling():
    f=Fig()
    ox,base=60,215
    f.add(f'<path class="ax" d="M{ox} {base}V30" marker-end="url(#ahm)"/>'); f.seg([(ox,base),(ox,30)])
    f.add(f'<path class="ax" d="M{ox} {base}H530" marker-end="url(#ahm)"/>'); f.seg([(ox,base),(530,base)])
    f.label(ox+8, 28, 'temperature / °C')
    f.label(530, base+22, 'time / min', 'end')
    yb=180
    # before mixing: flat readings
    f.add(f'<path class="c1 sw2" d="M{ox+15} {yb}H165"/>'); f.seg([(ox+15,yb),(165,yb)])
    for x in range(ox+15,166,25): f.add(f'<circle class="fi" cx="{x}" cy="{yb}" r="2.5"/>')
    # after mixing: rises to a maximum, then cools along a nearly straight line
    p0=(200,125); pk=(228,72); pe=(500,128)
    f.add(f'<path class="c1 sw2" d="M{p0[0]} {p0[1]}Q205 {pk[1]} {pk[0]} {pk[1]}L{pe[0]} {pe[1]}"/>')
    f.seg(bez(p0,(203,95),(210,72),pk,12)); f.seg([pk,pe])
    for x in range(260,501,40):
        y=pk[1]+(x-pk[0])*(pe[1]-pk[1])/(pe[0]-pk[0]); f.add(f'<circle class="fi" cx="{x}" cy="{y:.0f}" r="2.5"/>')
    slope=(pe[1]-pk[1])/(pe[0]-pk[0])
    xm=185; ym=pk[1]-(pk[0]-xm)*slope
    f.add(f'<path class="ln-m thin dash" d="M{pk[0]} {pk[1]}L{xm} {ym:.1f}"/>'); f.seg([pk,(xm,ym)])
    f.add(f'<path class="ln-m thin dash" d="M165 {yb}H{xm}"/>'); f.seg([(165,yb),(xm,yb)])
    f.add(f'<path class="ln-m thin dash" d="M{xm} {yb}V{base}"/>'); f.seg([(xm,yb),(xm,base)])
    ymid=(yb+ym)/2
    f.add(f'<path class="c2 sw2" d="M{xm} {ymid:.1f}V{ym+3:.1f}" marker-end="url(#ah)"/>')
    f.add(f'<path class="c2 sw2" d="M{xm} {ymid:.1f}V{yb-3}" marker-end="url(#ah)"/>')
    f.seg([(xm,ym),(xm,yb)])
    f.label(xm-9, ymid+4, 'ΔT', 'end')
    f.label(xm, base+22+0, 'time of mixing', 'middle')
    f.label(300, 160, 'readings before mixing' , 'start') if False else None
    f.label(ox+10, yb+22, 'before mixing', 'start')
    f.label(285, 165, 'dashed line: the cooling line', 'start')
    f.label(285, 183, 'extended back to the time of mixing', 'start')
    print(round(ym,1), 'extrapolated y; DT px', round(yb-ym,1))
    return f

# ---------------------------------------------------------------- bond energy level diagram
def bondlevels():
    f=Fig()
    ya,yr,yp=36,190,239
    f.add(f'<path class="ln thick" d="M120 {ya}H360"/>'); f.seg([(120,ya),(360,ya)])
    f.add(f'<path class="ln thick" d="M30 {yr}H220"/>'); f.seg([(30,yr),(220,yr)])
    f.add(f'<path class="ln thick" d="M300 {yp}H490"/>'); f.seg([(300,yp),(490,yp)])
    f.add(f'<path class="ln-m thin dash" d="M220 {yr}H470"/>'); f.seg([(220,yr),(470,yr)])
    f.add(f'<path class="c2 sw2" d="M160 {yr-3}V{ya+3}" marker-end="url(#ah)"/>'); f.seg([(160,yr),(160,ya)])
    f.add(f'<path class="c2 sw2" d="M330 {ya+3}V{yp-3}" marker-end="url(#ah)"/>'); f.seg([(330,ya),(330,yp)])
    f.add(f'<path class="c2 sw2" d="M450 {yr+3}V{yp-3}" marker-end="url(#ah)"/>'); f.seg([(450,yr),(450,yp)])
    f.label(240, ya-9, 'C(g) + 4H(g) + 4O(g)', 'middle')
    f.label(125, yr+20, 'CH₄(g) + 2O₂(g)', 'middle')
    f.label(395, yp+20, 'CO₂(g) + 2H₂O(g)', 'middle')
    f.label(170, 100, 'bonds broken', 'start'); f.label(170, 117, '+2632 kJ mol⁻¹', 'start')
    f.label(340, 100, 'bonds formed', 'start'); f.label(340, 117, '−3450 kJ mol⁻¹', 'start')
    f.label(462, 212, 'ΔH = −818', 'start'); f.label(462, 229, 'kJ mol⁻¹', 'start')
    return f

# ---------------------------------------------------------------- cycles
def box(f, cx, cy, text, h=30):
    w=tw(text)+16
    f.add(f'<rect class="fm s-acc" x="{cx-w/2:.0f}" y="{cy-h/2:.0f}" width="{w}" height="{h}" rx="8"/>')
    f.add(f'<text class="tl tc" x="{cx}" y="{cy+5}">{text}</text>')
    f.labels.append((text, cx-w/2, cy-h/2, cx+w/2, cy+h/2))
    return (cx-w/2, cy-h/2, cx+w/2, cy+h/2)

def arrow(f, x0, y0, x1, y1, cls='ln'):
    f.add(f'<path class="{cls}" d="M{x0} {y0}L{x1} {y1}" marker-end="url(#ah)"/>'); f.seg([(x0,y0),(x1,y1)])

def cycle_formation():
    f=Fig()
    L=box(f,125,45,'Fe₂O₃ + 3CO'); R=box(f,475,45,'2Fe + 3CO₂'); B=box(f,300,175,'2Fe + 3C + 3O₂')
    print(L,R,B)
    arrow(f,L[2]+8,45,R[0]-8,45)
    f.label(300,38,'ΔHr = ?','middle',halo=True)
    arrow(f,B[0]+22,B[1]-6,L[2]-30,L[3]+6)
    arrow(f,B[2]-22,B[1]-6,R[0]+30,R[3]+6)
    f.label(190,120,'ΔHf of reactants','end'); f.label(190,137,'−824 + 3(−111) = −1157','end')
    f.label(440,120,'ΔHf of products','start'); f.label(440,137,'3(−394) = −1182','start')
    return f

def cycle_combustion():
    f=Fig()
    L=box(f,135,45,'2C(s) + 3H₂(g) + ½O₂(g)'); R=box(f,495,45,'C₂H₅OH(l)'); B=box(f,315,185,'2CO₂(g) + 3H₂O(l)')
    print(L,R,B)
    arrow(f,L[2]+8,45,R[0]-8,45)
    f.label(335,38,'ΔHf = ?','middle',halo=True)
    arrow(f,L[0]+80,L[3]+6,B[0]+20,B[1]-6)
    arrow(f,R[0]+30,R[3]+6,B[2]-20,B[1]-6)
    f.label(180,120,'ΔHc of reactants','end'); f.label(180,137,'2(−394) + 3(−286) = −1646','end')
    f.label(445,120,'ΔHc of ethanol','start'); f.label(445,137,'= −1367','start')
    return f

def cycle_caco3():
    f=Fig()
    L=box(f,120,45,'CaCO₃(s)'); R=box(f,480,45,'CaO(s) + CO₂(g)'); B=box(f,300,185,'CaCl₂(aq) + H₂O(l) + CO₂(g)')
    print(L,R,B)
    arrow(f,L[2]+8,45,R[0]-8,45)
    f.label(300,38,'ΔH = ?','middle',halo=True)
    arrow(f,L[0]+55,L[3]+6,B[0]+45,B[1]-6)
    arrow(f,R[0]+55,R[3]+6,B[2]-45,B[1]-6)
    f.label(170,120,'ΔH₁ = −15','end'); f.label(170,137,'+ 2HCl(aq)','end')
    f.label(440,120,'ΔH₂ = −194','start'); f.label(440,137,'+ 2HCl(aq)','start')
    return f

if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]!='profile':
    fn={'cooling':cooling,'bond':bondlevels,'form':cycle_formation,'comb':cycle_combustion,'caco3':cycle_caco3}[sys.argv[1]]
    f=fn(); f.check(); print("\n".join(f.out))
