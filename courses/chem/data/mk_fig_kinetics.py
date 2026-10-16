# data/mk_fig_kinetics.py: builds the SVG snippets for chem.kinetics and checks label clearances.
# Run: py -X utf8 data/mk_fig_kinetics.py syringe|collide|cat
import sys
sys.path.insert(0, 'data')
from mk_fig_energetics import Fig, bez

def syringe():
    f = Fig()
    # flask: neck x 90-110, top y 60; shoulder y 100; base y 160 from x 55 to 145
    f.add('<path class="ln" d="M90 60V100L55 160H145L110 100V60"/>')
    f.seg([(90, 60), (90, 100), (55, 160), (145, 160), (110, 100), (110, 60)])
    f.add('<path class="fa" d="M65.0 142H135.0L145 160H55Z"/>')
    f.add('<path class="fm2" d="M86 48H114L112 64H88Z"/>')
    # delivery tube from the bung up and across to the syringe
    f.add('<path class="ln thick" d="M100 52V26H262"/>'); f.seg([(100, 52), (100, 26), (262, 26)])
    # syringe barrel: x 262-452, y 10-42 ; plunger head at x 330 ; rod to 500
    f.add('<path class="ln" d="M262 10H452M262 42H452M262 10V42"/>'); f.seg([(262, 10), (452, 10)]); f.seg([(262, 42), (452, 42)]); f.seg([(262, 10), (262, 42)])
    f.add('<path class="fa2" d="M264 12H330V40H264Z"/>')
    f.add('<path class="ln thick" d="M330 12V40"/>'); f.seg([(330, 12), (330, 40)])
    f.add('<path class="ln thick" d="M330 26H500"/>'); f.seg([(330, 26), (500, 26)])
    f.add('<path class="ln thick" d="M500 14V38"/>'); f.seg([(500, 14), (500, 38)])
    for x in range(280, 450, 20):
        f.add(f'<path class="ln thin" d="M{x} 10V16"/>'); f.seg([(x, 10), (x, 16)])
    # labels
    f.label(300, 70, 'gas syringe', 'middle')
    f.add('<path class="ln-m thin" d="M300 56V45"/>'); f.seg([(300, 56), (300, 45)])
    f.label(160, 100, 'delivery tube', 'start')
    f.add('<path class="ln-m thin" d="M158 96L112 40"/>')
    f.add('<path class="ln-m thin" d="M118 152L172 152"/>')
    f.label(178, 156, 'metal and acid', 'start')
    f.label(500, 62, 'plunger moves out as', 'end'); f.label(500, 79, 'gas collects', 'end')
    return f

def collide():
    f = Fig()
    r = 15
    panels = [
        (110, 'too slow:', 'not enough energy', 'right', 22),
        (345, 'wrong end:', 'wrong orientation', 'left', 56),
        (500, 'fast, right end:', 'reaction occurs', 'right', 56),
    ]
    y = 70
    f.add('<path class="ln-m thin dash" d="M232 30V150"/>'); f.add('<path class="ln-m thin dash" d="M432 30V150"/>')
    for cx, l1, l2, side, L in panels:
        for (px, t, c) in ((cx - 17, 'X', 'fm'), (cx + 17, 'Y', 'fm2')):
            f.add(f'<circle class="{c} s-acc" cx="{px}" cy="{y}" r="{r}"/>'); f.add(f'<text class="tl tc" x="{px}" y="{y+5}">{t}</text>')
        zx = cx + 80 if side == 'right' else cx - 80
        f.add(f'<circle class="fa s-acc" cx="{zx}" cy="{y}" r="{r}"/>'); f.add(f'<text class="tl tc tp" x="{zx}" y="{y+5}">Z</text>')
        if side == 'right':
            f.add(f'<path class="ln" d="M{zx+10} {y-30}H{zx+10-L}" marker-end="url(#ah)"/>')
        else:
            f.add(f'<path class="ln" d="M{zx-10} {y-30}H{zx-10+L}" marker-end="url(#ah)"/>')
        f.label(cx, y + 50, l1, 'middle'); f.label(cx, y + 68, l2, 'middle')
    return f

def cat():
    f = Fig()
    ox, base = 20, 205
    f.add(f'<path class="ax" d="M{ox} {base}V30" marker-end="url(#ahm)"/>'); f.seg([(ox, base), (ox, 30)])
    f.add(f'<path class="ax" d="M{ox} {base}H290" marker-end="url(#ahm)"/>'); f.seg([(ox, base), (290, base)])
    f.label(ox + 8, 24, 'enthalpy'); f.label(290, base + 22, 'progress of reaction', 'end')
    yr, yp, pk, pc = 118, 168, 52, 86
    xr0, xr1, xp0, xp1 = ox + 40, ox + 95, ox + 175, ox + 225
    xm = (xr1 + xp0) / 2
    f.add(f'<path class="ln thick" d="M{xr0} {yr}H{xr1}"/>'); f.seg([(xr0, yr), (xr1, yr)])
    f.add(f'<path class="ln thick" d="M{xp0} {yp}H{xp1}"/>'); f.seg([(xp0, yp), (xp1, yp)])
    def hump(top, cls):
        d = f'M{xr1} {yr}C{xr1+22} {yr} {xm-22} {top} {xm} {top}C{xm+22} {top} {xp0-22} {yp} {xp0} {yp}'
        f.add(f'<path class="{cls}" d="{d}"/>')
        f.seg(bez((xr1, yr), (xr1 + 22, yr), (xm - 22, top), (xm, top))); f.seg(bez((xm, top), (xm + 22, top), (xp0 - 22, yp), (xp0, yp)))
    hump(pk, 'c1 sw2'); hump(pc, 'c1 sw2 dash')
    f.label((xr0 + xr1) / 2, yr + 20, 'reactants', 'middle'); f.label((xp0 + xp1) / 2, yp + 20, 'products', 'middle')
    # Ea without catalyst (left) and with catalyst (middle)
    xa, xb = ox + 18, ox + 46
    f.add(f'<path class="ln-m thin dash" d="M{xa-6} {pk}H{xm-4}"/>'); f.seg([(xa - 6, pk), (xm - 4, pk)])
    f.add(f'<path class="ln-m thin dash" d="M{xb-6} {pc}H{xm-4}"/>'); f.seg([(xb - 6, pc), (xm - 4, pc)])
    f.add(f'<path class="ln-m thin dash" d="M{xa-6} {yr}H{xr0}"/>'); f.seg([(xa - 6, yr), (xr0, yr)])
    f.add(f'<path class="c2 sw2" d="M{xa} {(yr+pk)/2}V{pk+3}" marker-end="url(#ah)"/>'); f.add(f'<path class="c2 sw2" d="M{xa} {(yr+pk)/2}V{yr-3}" marker-end="url(#ah)"/>')
    f.seg([(xa, pk), (xa, yr)])
    f.add(f'<path class="c2 sw2" d="M{xb} {(yr+pc)/2}V{pc+3}" marker-end="url(#ah)"/>'); f.add(f'<path class="c2 sw2" d="M{xb} {(yr+pc)/2}V{yr-3}" marker-end="url(#ah)"/>')
    f.seg([(xb, pc), (xb, yr)])
    f.label(xa + 7, 76, 'Eₐ')
    f.label(xb + 8, (yr + pc) / 2 + 4, 'Eₐ′')
    xd = xp1 + 30
    ym = (yr + yp) / 2
    f.add(f'<path class="ln-m thin dash" d="M{xr1} {yr}H{xd+8}"/>'); f.seg([(xr1, yr), (xd + 8, yr)])
    f.add(f'<path class="ln-m thin dash" d="M{xp1} {yp}H{xd+8}"/>'); f.seg([(xp1, yp), (xd + 8, yp)])
    f.add(f'<path class="c2 sw2" d="M{xd} {ym}V{yr+3}" marker-end="url(#ah)"/>'); f.add(f'<path class="c2 sw2" d="M{xd} {ym}V{yp-3}" marker-end="url(#ah)"/>')
    f.seg([(xd, yr), (xd, yp)])
    f.label(xd - 9, ym + 4, 'ΔH', 'end')
    f.add('<path class="c1 sw2" d="M200 40H224"/>'); f.seg([(200, 40), (224, 40)]); f.label(230, 44, 'no catalyst', 'start')
    f.add('<path class="c1 sw2 dash" d="M200 62H224"/>'); f.seg([(200, 62), (224, 62)]); f.label(230, 66, 'with catalyst', 'start')
    return f

if __name__ == '__main__':
    which = sys.argv[1]
    g = {'syringe': syringe, 'collide': collide, 'cat': cat}[which]()
    g.check()
    print(chr(10).join(g.out))
