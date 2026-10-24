import sys; sys.path.insert(0, 'data'); sys.stdout.reconfigure(encoding='utf-8')
from mk_fig_synthesis import f, tw

def axes(x0, x1, y0, ytop, ticks, xs, xlabel_y, xlabel_x, xlabel='m/e'):
    P = []
    P.append('<path class="ax" d="M%s %s H%s" marker-end="url(#ahm)"/>' % (f(x0), f(y0), f(x1)))
    P.append('<path class="ax" d="M%s %s V%s" marker-end="url(#ahm)"/>' % (f(x0), f(y0), f(ytop)))
    return P

# propanone: m/e 0..70 over x 40..320 (4 px per unit); 0% at y150, 100% at y 50 (1 px per %)
def prop():
    P = []
    X0, S, Y0 = 40, 4, 150
    P.append('<path class="ax" d="M40 150H328" marker-end="url(#ahm)"/>')
    P.append('<path class="ax" d="M40 150V22" marker-end="url(#ahm)"/>')
    for m in range(0, 71, 10):
        x = X0 + S * m
        P.append('<path class="ln-m thin" d="M%s 150v4"/>' % f(x))
        P.append('<text class="ts tc" x="%s" y="166">%d</text>' % (f(x), m))
    P.append('<text class="tl tc" x="180" y="186">m/e</text>')
    P.append('<text class="tl" x="46" y="14">relative abundance / %</text>')
    for m, h, lab in [(15, 24, 'CH₃⁺'), (43, 100, 'CH₃CO⁺'), (58, 34, 'M⁺')]:
        x = X0 + S * m
        P.append('<path class="c1 sw3" d="M%s 150V%s"/>' % (f(x), f(150 - h)))
        t = '%d  %s' % (m, lab) if False else '%d %s' % (m, lab)
        P.append('<text class="tl tc" x="%s" y="%s">%s</text>' % (f(x), f(150 - h - 7), t))
        print('label', t, x - tw(t) / 2, x + tw(t) / 2, 150 - h - 17)
    return '\n'.join(P)

# M+2 patterns: two panels
def m2():
    P = []
    # panel 1 axis x 20..160 ; panel 2 axis x 190..330 ; baseline y 130 ; 100% at y 40
    for ax0, title, peaks in [(20, 'C₂H₅Cl', [(64, 100), (66, 33)]), (190, 'C₂H₅Br', [(108, 100), (110, 98)])]:
        P.append('<path class="ax" d="M%d 130H%d" marker-end="url(#ahm)"/>' % (ax0, ax0 + 140))
        cxm = ax0 + 70
        P.append('<text class="tl tc" x="%d" y="14">%s</text>' % (cxm, title))
        for i, (m, h) in enumerate(peaks):
            x = ax0 + 40 + 40 * i
            hh = 0.9 * h
            P.append('<path class="c1 sw3" d="M%d 130V%s"/>' % (x, f(130 - hh)))
            P.append('<text class="tl tc" x="%d" y="%s">%d</text>' % (x, f(130 - hh - 7), m))
        P.append('<text class="tl tc" x="%d" y="150">m/e</text>' % cxm)
    return '\n'.join(P)

# Mg spectrum: m/e 24,25,26 ; axis x 40..300; 0 at y130, 100% at y30
def mg():
    P = []
    P.append('<path class="ax" d="M40 130H300" marker-end="url(#ahm)"/>')
    P.append('<path class="ax" d="M40 130V14" marker-end="url(#ahm)"/>')
    P.append('<text class="tl" x="46" y="12">relative abundance / %</text>')
    for i, (m, h) in enumerate([(24, 79), (25, 10), (26, 11)]):
        x = 90 + 70 * i
        P.append('<path class="c1 sw3" d="M%d 130V%s"/>' % (x, f(130 - h)))
        P.append('<text class="tl tc" x="%d" y="%s">%s</text>' % (x, f(130 - h - 7), h))
        P.append('<text class="ts tc" x="%d" y="146">%d</text>' % (x, m))
    P.append('<text class="tl tc" x="170" y="164">m/e</text>')
    return '\n'.join(P)

open('scratch/ms_prop.svg.txt', 'w', encoding='utf-8').write(prop())
open('scratch/ms_m2.svg.txt', 'w', encoding='utf-8').write(m2())
open('scratch/ms_mg.svg.txt', 'w', encoding='utf-8').write(mg())
