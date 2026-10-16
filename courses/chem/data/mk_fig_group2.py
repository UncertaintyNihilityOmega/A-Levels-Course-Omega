# data/mk_fig_group2.py: the two A Level figures of chem.group2 (both `fig small`, 340 px wide).
# 1. polarisation of the carbonate ion by a small and a large cation; 2. the solution energy cycle.
# Run: py data/mk_fig_group2.py  (prints both figures; checks label boxes against shapes)
import sys, math
sys.stdout.reconfigure(encoding='utf-8')
boxes = []   # (x0, y0, x1, y1, name) label boxes
shapes = []  # (cx, cy, r, name) circles to keep labels clear of
def lab(x, y, s, anchor='middle', cls='tl tc', name=None):
    w = 7 * len(s)
    x0 = x - w / 2 if anchor == 'middle' else (x if anchor == 'start' else x - w)
    boxes.append((x0, y - 10, x0 + w, y + 3, name or s))
    anc = '' if anchor == 'middle' else f' text-anchor="{anchor}"'
    return f'<text class="{cls}" x="{x}" y="{y}"{anc}>{s}</text>'

# ---------- figure 1: polarisation ----------
p = []
def panel(cy, cat_cx, cat_r, cat_label, anion_path, caption1, caption2, cap_y):
    shapes.append((cat_cx, cy, cat_r, 'cation'))
    p.append(f'<circle class="ln-m thin dash" cx="240" cy="{cy}" r="40" fill="none"/>')
    p.append(anion_path)
    p.append(f'<circle class="fi" cx="{cat_cx}" cy="{cy}" r="{cat_r}"/>')
    p.append(lab(cat_cx - 8, cy - cat_r - 8, cat_label))
    p.append(lab(240, cy + 4, 'CO₃²⁻'))
    p.append(lab(170, cap_y, caption1))
    p.append(lab(170, cap_y + 18, caption2, cls='tl tc ta'))
y1, y2 = 62, 205
egg = f'<path class="f1 s-acc sw2" d="M199 {y1}C205 {y1-25} 235 {y1-32} 262 {y1-28}C290 {y1-22} 290 {y1+22} 262 {y1+28}C235 {y1+32} 205 {y1+25} 199 {y1}Z"/>'
rnd = f'<ellipse class="f1 s-acc sw2" cx="241" cy="{y2}" rx="38" ry="37"/>'
panel(y1, 184, 11, 'Mg²⁺', egg, 'small cation, high charge density', 'cloud strongly distorted', 118)
panel(y2, 170, 22, 'Ba²⁺', rnd, 'large cation, lower charge density', 'cloud hardly distorted', 262)
# clearance: label boxes vs the dashed circles and cation circles
def hits(b, cx, cy, r, m=4):
    nx = min(max(cx, b[0] - m), b[2] + m); ny = min(max(cy, b[1] - m), b[3] + m)
    return math.hypot(nx - cx, ny - cy) < r
bad = 0
for b in boxes:
    for (cx, cy, r) in ((240, y1, 40), (240, y2, 40), (184, y1, 11), (170, y2, 22)):
        if b[4] == 'CO₃²⁻' and cx == 240: continue
        if hits(b, cx, cy, r) and not (b[4] in ('Mg²⁺', 'Ba²⁺') and (cx, cy) in ((184, y1), (170, y2))):
            print('CLASH', b[4], (cx, cy, r)); bad += 1
for i, b1 in enumerate(boxes):
    for b2 in boxes[i + 1:]:
        if b1[0] < b2[2] + 4 and b2[0] < b1[2] + 4 and b1[1] < b2[3] + 4 and b2[1] < b1[3] + 4: print('OVERLAP', b1[4], b2[4]); bad += 1
print('fig1 problems', bad, file=sys.stderr)
print('<figure class="fig small"><svg viewBox="0 0 340 292" role="img" aria-label="Two drawings of a carbonate ion next to a cation. Top: a small, highly charged cation pulls the electron cloud of the carbonate ion strongly towards it, so the cloud is distorted. Bottom: a larger cation of the same charge pulls much less, so the cloud is hardly distorted. A dashed circle shows the carbonate ion without a cation">' + ''.join(p) + '</svg><figcaption>Polarisation of the carbonate ion. The dashed circle is the shape of the ion with no cation nearby. A small cation with a 2+ charge (high charge density) pulls the electron cloud towards it and distorts it much more than a larger cation of the same charge.</figcaption></figure>')

# ---------- figure 2: solution cycle ----------
boxes.clear()
q = []
q.append(lab(60, 34, 'ionic solid'))
q.append(lab(282, 34, 'gaseous ions'))
q.append(lab(170, 156, 'aqueous ions'))
q.append('<path class="ln" d="M110 30H228" marker-end="url(#ah)"/>')
q.append(lab(169, 20, '−ΔHlatt'))
q.append('<path class="ln" d="M66 46L130 132" marker-end="url(#ah)"/>')
q.append(lab(84, 96, 'ΔHsol', anchor='end', cls='tl'))
q.append('<path class="ln" d="M276 46L210 132" marker-end="url(#ah)"/>')
q.append(lab(256, 96, 'ΔHhyd', anchor='start', cls='tl'))
q.append(lab(170, 188, 'ΔHsol = −ΔHlatt + ΔHhyd'))
# arrow 1 label clearance and node boxes vs arrows
def seg_hit(b, a1, a2, m=4):
    for k in range(201):
        t = k / 200; x = a1[0] + (a2[0] - a1[0]) * t; y = a1[1] + (a2[1] - a1[1]) * t
        if b[0] - m <= x <= b[2] + m and b[1] - m <= y <= b[3] + m: return True
    return False
bad = 0
arrows = {'1': ((110, 30), (228, 30)), 'sol': ((66, 46), (130, 132)), 'hyd': ((276, 46), (210, 132))}
for b in boxes:
    for k, (a1, a2) in arrows.items():
        if seg_hit(b, a1, a2) and not (b[4] == 'ionic solid' and k in ('sol',)) and not (b[4] == 'gaseous ions' and k in ('hyd',)) and not (b[4] == 'aqueous ions' and k in ('sol', 'hyd')):
            print('CLASH', b[4], k); bad += 1
print('fig2 problems', bad, [ (round(b[0]),round(b[2])) for b in boxes], file=sys.stderr)
print('<figure class="fig small"><svg viewBox="0 0 340 200" role="img" aria-label="Energy cycle for dissolving an ionic solid: the solid goes to gaseous ions with enthalpy change minus the lattice energy, the gaseous ions go to aqueous ions with the enthalpy change of hydration, and the solid goes directly to aqueous ions with the enthalpy change of solution">' + ''.join(q) + '</svg><figcaption>The energy cycle for dissolving an ionic solid. The lattice energy is defined for gaseous ions forming the solid, so the solid breaking up into gaseous ions is −ΔHlatt.</figcaption></figure>')
