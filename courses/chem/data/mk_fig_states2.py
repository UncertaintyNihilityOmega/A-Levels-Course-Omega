# data/mk_fig_states2.py: SVG coordinates for the graphite figure of chem.states
import math
s=24; w=math.sqrt(3)*s
def hexpath(cx,cy):
    pts=[(cx+s*math.cos(math.radians(90+60*k)), cy-s*math.sin(math.radians(90+60*k))) for k in range(6)]
    return "M"+"L".join(f"{x:.0f} {y:.0f}" for x,y in pts)+"Z"
cent=[(60,70),(60+w,70),(60+2*w,70),(60+w/2,70+1.5*s),(60+1.5*w,70+1.5*s),(60,70+3*s),(60+w,70+3*s),(60+2*w,70+3*s)]
# a clean honeycomb: rows 3,2,3
for c in cent: print(f'<path class="ln thick" d="{hexpath(*c)}"/>')
print(min(c[0] for c in cent)-w/2, max(c[0] for c in cent)+w/2, 70-s, 70+3*s+s)
