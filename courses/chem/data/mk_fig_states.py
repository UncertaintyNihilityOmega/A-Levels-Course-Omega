# data/mk_fig_states.py: prints the SVG coordinates for the chem.states figures (paste into the chapter)
import math
out=[]
# --- fig 1: NaCl lattice and metallic lattice
s=34; x0=69; y0=40
for r in range(4):
    for c in range(4):
        x=x0+c*s; y=y0+r*s
        if (r+c)%2==0: out.append(f'<circle class="f1 s-acc sw2" cx="{x}" cy="{y}" r="9"/><text class="tl tc" x="{x}" y="{y+5}">+</text>')
        else: out.append(f'<circle class="f2 s-acc sw2" cx="{x}" cy="{y}" r="13"/><text class="tl tc" x="{x}" y="{y+5}">−</text>')
print("\n".join(out)); print('-----')
out=[]
xm=369
for r in range(4):
    for c in range(4):
        x=xm+c*s; y=y0+r*s
        out.append(f'<circle class="fm s-acc sw2" cx="{x}" cy="{y}" r="10"/><text class="tl tc" x="{x}" y="{y+5}">+</text>')
import random
random.seed(3)
for r in range(3):
    for c in range(3):
        x=xm+c*s+s/2+random.choice([-5,5,0]); y=y0+r*s+s/2+random.choice([-5,5,0])
        out.append(f'<circle class="fi" cx="{x:.0f}" cy="{y:.0f}" r="2.5"/>')
print("\n".join(out))
