# Sketch of the eleven successive ionisation energies of sodium (log scale, no numbers on the axis).
# Heights: electrons 1-4 from the FACTS.md values (494, 4560, 6940, 9540) on a log scale; the rest are
# qualitative (gentle rise inside the second shell, small 2p->2s step, big jump to the first shell).
from math import log10
H = {1: (log10(494) - 2.4) * 70, 2: (log10(4560) - 2.4) * 70, 3: (log10(6940) - 2.4) * 70, 4: (log10(9540) - 2.4) * 70,
     5: 120, 6: 128, 7: 136, 8: 148, 9: 156, 10: 205, 11: 212}
base = 235
X = {i: 80 + 46 * (i - 1) for i in range(1, 12)}
Y = {i: round(base - H[i], 1) for i in H}
assert all(Y[i + 1] < Y[i] for i in range(1, 11)), "must rise"
assert Y[11] > 18
p = []
p.append(f'<path class="ax" d="M68 {base}H599" marker-end="url(#ahm)"/><path class="ax" d="M68 {base}V24" marker-end="url(#ahm)"/>')
p.append('<text class="tl" x="74" y="14">log(ionisation energy)</text>')
p.append('<path class="ln-m thin dash" d="M103 30V235"/><path class="ln-m thin dash" d="M471 30V235"/>')
pts = " ".join(("M" if i == 1 else "L") + f"{X[i]} {Y[i]}" for i in range(1, 12))
p.append(f'<path class="c1" d="{pts}"/>')
for i in range(1, 12):
    p.append(f'<circle class="fa s-acc" cx="{X[i]}" cy="{Y[i]}" r="4"/><text class="ts tc" x="{X[i]}" y="253">{i}</text>')
p.append('<text class="tl" x="165" y="190" text-anchor="middle">big jump</text>')
p.append('<text class="tl" x="430" y="42" text-anchor="middle">big jump</text>')
p.append(f'<path class="ln-m thin" d="M379 130V96"/><text class="ts tc" x="379" y="144">small step: 2p to 2s</text>')
for a, b in ((74, 86), (120, 454), (488, 546)):
    p.append(f'<path class="ln-m" d="M{a} 262v4H{b}v-4"/>')
p.append('<text class="tl tc" x="80" y="284">3rd shell</text><text class="tl tc" x="287" y="284">2nd shell</text><text class="tl tc" x="517" y="284">1st shell</text>')
p.append('<text class="tl tc" x="320" y="304">electron removed (1st to 11th)</text>')
svg = ('<figure class="fig"><svg viewBox="0 0 610 312" role="img" aria-label="Sketch of the logarithm of the eleven successive ionisation energies of sodium: one low point, a big jump to a gently rising group of eight, then a second big jump to the last two electrons">'
       + "".join(p) + '</svg><figcaption>A sketch (not to scale) of log(ionisation energy) for the eleven electrons of sodium, grouped 1 | 8 | 2. The two big jumps are where the next electron comes from a shell closer to the nucleus.</figcaption></figure>')
print(svg)
