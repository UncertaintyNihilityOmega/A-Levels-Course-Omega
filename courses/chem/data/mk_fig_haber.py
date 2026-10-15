# Flow diagram of the Haber process for chem.equilibria (schematic). Prints the figure HTML; checks label widths.
W = lambda s: 7 * len(s)
parts = []
def box(x0, x1, lines, y0=42, y1=104):
    parts.append(f'<rect class="fm s-acc" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="8"/>')
    cx = (x0 + x1) / 2
    n = len(lines)
    base = y0 + (y1 - y0) / 2 - (n - 1) * 8 + 4
    for i, s in enumerate(lines):
        assert W(s) <= (x1 - x0) - 8, (s, W(s), x1 - x0)
        parts.append(f'<text class="tl tc" x="{cx}" y="{base + 16 * i}">{s}</text>')
box(110, 214, ['compressor', '200 atm'])
box(254, 404, ['reactor', 'iron catalyst', '450 °C'])
box(440, 544, ['cooler', 'NH₃ liquefies'])
parts.append('<text class="tl" x="10" y="58">N₂ + H₂</text>')
parts.append('<path class="ln" d="M66 73H106" marker-end="url(#ah)"/>')
parts.append('<path class="ln" d="M216 73H250" marker-end="url(#ah)"/>')
parts.append('<path class="ln" d="M406 73H436" marker-end="url(#ah)"/>')
parts.append('<path class="ln" d="M546 73H588" marker-end="url(#ah)"/>')
parts.append('<text class="tl tc" x="567" y="58">NH₃(l)</text>')
parts.append('<path class="ln" d="M492 106V176H162V110" marker-end="url(#ah)"/>')
parts.append('<text class="tl tc" x="327" y="168">unreacted N₂ and H₂ recycled</text>')
assert 567 + W('NH₃(l)') / 2 <= 605
svg = ('<figure class="fig"><svg viewBox="0 30 610 160" role="img" aria-label="Flow diagram of the Haber process: nitrogen and hydrogen are compressed to 200 atmospheres, pass over an iron catalyst at 450 degrees Celsius, then are cooled so that ammonia liquefies and is removed; unreacted nitrogen and hydrogen return to the compressor">'
       + "".join(parts) + '</svg><figcaption>The Haber process (schematic). Ammonia is removed as a liquid and the unreacted gases go round again, so the reaction does not need to reach a high yield in a single pass.</figcaption></figure>')
print(svg)
