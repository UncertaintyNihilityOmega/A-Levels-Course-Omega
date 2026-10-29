# data/fig_bio.conservation.py: figures of chapters/bio.conservation.md. Run: py data/fig_bio.conservation.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit_p18 import Fig, place, report

figs = {}
objs = []

# ---- 1 fragmentation: one block v sixteen patches (1 km = 25 px); edge zone 0.25 km = 6.25 px
f = Fig("conservation1")
f.text(10, 16, "A  One block, 4 km by 4 km", "tl tb")
f.rect(20, 28, 100, 100, "f1 s-acc sw2")
f.rect(26.25, 34.25, 87.5, 87.5, "f2 s-acc2 sw2")
f.text(150, 54, "edge zone")
f.line([(146, 50), (117, 50)], "ln-m thin")
f.text(150, 82, "core 12.25 km²")
f.line([(146, 78), (100, 78)], "ln-m thin")
f.text(150, 110, "edge length 16 km")
f.text(10, 152, "B  Cut into 16 patches of 1 km by 1 km", "tl tb")
for i in range(4):
    for j in range(4):
        x, y = 20 + 29 * i, 164 + 29 * j
        f.rect(x, y, 25, 25, "f1 s-acc sw2")
        f.rect(x + 6.25, y + 6.25, 12.5, 12.5, "f2 s-acc2 sw2")
f.text(150, 172, "edge zone")
f.line([(146, 168), (129, 168)], "ln-m thin")
f.text(150, 209, "core 4.0 km² in all")
f.line([(146, 205.5), (122, 205.5)], "ln-m thin")
f.text(150, 250, "edge length 64 km")
f.text(20, 304, "gap (road or field)")
f.line([(47, 288), (47, 270)], "ln-m thin")
figs["conservation1"] = f.svg((340, 312),
    "Two squares of forest drawn to scale, each 16 square kilometres in all. A: one block 4 km by 4 km with a narrow edge zone round it and a large core of 12.25 square kilometres; the edge is 16 km long. B: the same forest cut by gaps into 16 patches each 1 km by 1 km; each patch is mostly edge zone with a small core, the cores total 4.0 square kilometres, and the edge is 64 km long.",
    "The same area of forest before (A) and after (B) it is cut into patches. Each patch has an edge zone round it (0.25 km wide in this example) and a core. The total area is unchanged, but the core falls from 12.25 km² to 4.0 km² and the length of edge rises fourfold.")
objs.append(f)

# ---- 2 IVF, embryo transfer, surrogacy
f = Fig("conservation2")
tops = [8 + 68 * k for k in range(4)]
steps = [
    ("1  Eggs collected from the female,", "sperm from a male or the frozen zoo", "f1 s-acc sw2"),
    ("2  IVF: eggs and sperm mixed in a dish;", "early embryos form (can be frozen)", "f1 s-acc sw2"),
    ("3  Embryo transfer into the uterus of", "a surrogate female", "f1 s-acc sw2"),
    ("4  Surrogate carries the embryo to birth;", "young have the genes of both donors", "f2 s-acc2 sw2"),
]
for (t, (a, b, cls)) in zip(tops, steps):
    f.rect(10, t, 320, 46, cls, rx=6)
    f.text(170, t + 19, a, "tl", "middle")
    f.text(170, t + 35, b, "tl", "middle")
for t in tops[:3]:
    f.line([(170, t + 46), (170, t + 66)], "ln", "ah", check=False)
figs["conservation2"] = f.svg((340, 266),
    "Flow diagram in four boxes joined by downward arrows. 1: eggs collected from the female and sperm from a male or the frozen zoo. 2: IVF, eggs and sperm mixed in a dish, early embryos form and can be frozen. 3: embryo transfer into the uterus of a surrogate female. 4: the surrogate carries the embryo to birth and the young have the genes of both donors.",
    "Assisted reproduction in an endangered mammal: IVF, embryo transfer and surrogacy.")
objs.append(f)

report(objs)
place("bio.conservation", figs)
