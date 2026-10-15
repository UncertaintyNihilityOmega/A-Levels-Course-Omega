# Figures for chem.redox: (1) electron transfer between Zn and Cu2+, (2) oxidation-number line for chlorine disproportionation.
# Prints each figure's HTML; paste into chapters/chem.redox.md. Also checks label boxes (7 px per character, 13 px tall).
import sys

def W(s):  # rough width of a label in px
    return 7 * len(s)

# ---------- figure 1: electron transfer ----------
f1 = []
f1.append('<text class="tl" x="188" y="50" text-anchor="end">Zn</text>')
f1.append('<path class="ln" d="M200 46H250" marker-end="url(#ah)"/>')
f1.append('<text class="tl" x="262" y="50">Zn²⁺ + 2e⁻</text>')
f1.append('<text class="tl" x="352" y="50">oxidation: electrons lost</text>')
f1.append('<text class="tl" x="188" y="116" text-anchor="end">Cu²⁺ + 2e⁻</text>')
f1.append('<path class="ln" d="M200 112H250" marker-end="url(#ah)"/>')
f1.append('<text class="tl" x="262" y="116">Cu</text>')
f1.append('<text class="tl" x="352" y="116">reduction: electrons gained</text>')
f1.append('<path class="c2 sw2" d="M318 60Q250 62 168 96" marker-end="url(#ah)"/>')
fig1 = ('<figure class="fig"><svg viewBox="0 20 610 125" role="img" aria-label="Half-equations for zinc reacting with copper(II) ions: zinc loses two electrons to form Zn2+ (oxidation), and a curved arrow carries the two electrons to Cu2+, which gains them to form copper (reduction)">'
        + "".join(f1) + '</svg><figcaption>Zinc is oxidised and copper(II) ions are reduced. The curved arrow shows the two electrons passing from the zinc to the copper(II) ion.</figcaption></figure>')

# ---------- figure 2: oxidation number line ----------
X = lambda v: 200 + 48 * (v + 2)
ax = 105
f2 = []
f2.append(f'<path class="ax" d="M{X(-2)-12} {ax}H{X(6)+20}" marker-end="url(#ahm)"/>')
for v in range(-2, 7):
    lab = ('+' + str(v)) if v > 0 else ('−' + str(-v) if v < 0 else '0')
    f2.append(f'<path class="ln-m" d="M{X(v)} {ax-4}V{ax+4}"/><text class="ts tc" x="{X(v)}" y="{ax+20}">{lab}</text>')
f2.append('<text class="tl" x="10" y="24">oxidation number of chlorine</text>')
f2.append(f'<text class="tl" x="{X(-2)-12}" y="52">← reduction</text><text class="tl" x="{X(6)+20}" y="52" text-anchor="end">oxidation →</text>')
for v, s in ((-1, 'Cl⁻'), (0, 'Cl₂'), (1, 'ClO⁻'), (5, 'ClO₃⁻')):
    f2.append(f'<circle class="fa s-acc" cx="{X(v)}" cy="{ax}" r="4"/><text class="tl tc" x="{X(v)}" y="{ax-14}">{s}</text>')
# guides to the arrow rows
for v in (-1, 0, 1, 5):
    f2.append(f'<path class="ln-m thin dash" d="M{X(v)} {ax+30}V212"/>')
y1, y2 = 160, 198
f2.append(f'<text class="tl" x="10" y="{y1+4}">cold NaOH(aq)</text>')
f2.append(f'<path class="ln" d="M{X(0)-4} {y1}H{X(-1)+6}" marker-end="url(#ah)"/><path class="ln" d="M{X(0)+4} {y1}H{X(1)-6}" marker-end="url(#ah)"/>')
f2.append(f'<text class="tl" x="10" y="{y2+4}">hot NaOH(aq)</text>')
f2.append(f'<path class="ln" d="M{X(0)-4} {y2}H{X(-1)+6}" marker-end="url(#ah)"/><path class="ln" d="M{X(0)+4} {y2}H{X(5)-6}" marker-end="url(#ah)"/>')
fig2 = ('<figure class="fig"><svg viewBox="0 8 610 218" role="img" aria-label="Number line of oxidation numbers for chlorine from minus 2 to plus 6, marking Cl minus (−1), Cl2 (0), ClO minus (+1) and ClO3 minus (+5). Chlorine at 0 forms Cl minus and ClO minus with cold sodium hydroxide, and Cl minus and ClO3 minus with hot sodium hydroxide">'
        + "".join(f2) + '</svg><figcaption>Chlorine disproportionates in sodium hydroxide: some atoms move left on the line (reduction to chloride) and some move right (oxidation). With cold NaOH(aq) the product is chlorate(I), ClO⁻; with hot NaOH(aq) it is chlorate(V), ClO₃⁻.</figcaption></figure>')

# label checks: no two label boxes overlap
boxes = []
def box(name, x, y, text, anchor='start'):
    w = W(text)
    x0 = x if anchor == 'start' else (x - w if anchor == 'end' else x - w / 2)
    boxes.append((name, x0, y - 10, x0 + w, y + 3))
box('a', 10, 24, 'oxidation number of chlorine')
box('red', X(-2) - 12, 52, '← reduction'); box('ox', X(6) + 20, 52, 'oxidation →', 'end')
for v, s in ((-1, 'Cl⁻'), (0, 'Cl₂'), (1, 'ClO⁻'), (5, 'ClO₃⁻')):
    box(s, X(v), ax - 14, s, 'mid')
box('cold', 10, y1 + 4, 'cold NaOH(aq)'); box('hot', 10, y2 + 4, 'hot NaOH(aq)')
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        a, b = boxes[i], boxes[j]
        if a[1] < b[3] + 4 and b[1] < a[3] + 4 and a[2] < b[4] + 4 and b[2] < a[4] + 4:
            print("OVERLAP", a, b, file=sys.stderr)
for b in boxes:
    assert b[3] <= 610, b
# the cold/hot labels must end before the first guide line (x of -1) and arrow
assert 10 + W('cold NaOH(aq)') < X(-1) - 8, "label hits guide"
print(fig1); print(); print(fig2)
