# Generates the acquisitions figure of hist.int.empire.4 (viewBox 340 x 534; panels stacked for phones)
import re
W, H = 340, 534
panels = [
    ("Pacific", "fm", [("Hawaii", "annexed July 1898"), ("Philippines and Guam", "Treaty of Paris, Dec 1898"),
                       ("Wake Island", "taken 1899"), ("American Samoa", "treaty of 1899")]),
    ("Caribbean and Central America", "fm2", [("Puerto Rico", "Treaty of Paris, Dec 1898"), ("Cuba", "Platt Amendment, 1901"),
                       ("Panama Canal Zone", "treaty of November 1903"), ("Virgin Islands", "bought from Denmark, 1917")]),
]
BOXH, GAP, TOP, BOT = 46, 8, 30, 14
ph = TOP + 4 * BOXH + 3 * GAP + BOT
out = []
y0 = 10
for title, fill, items in panels:
    out.append(f'<rect class="fp s-acc sw2" x="10" y="{y0}" width="320" height="{ph}" rx="8"/>')
    out.append(f'<text class="tl tb tc" x="170" y="{y0 + 21}">{title}</text>')
    for i, (a, b) in enumerate(items):
        y = y0 + TOP + i * (BOXH + GAP)
        out.append(f'<rect class="{fill} s-acc sw2" x="22" y="{y}" width="296" height="{BOXH}" rx="6"/>')
        out.append(f'<text class="tl tb" x="34" y="{y + 19}">{a}</text>')
        out.append(f'<text class="tl" x="34" y="{y + 37}">{b}</text>')
        assert len(a) * 7 <= 296 - 24 and len(b) * 7 <= 296 - 24
    y0 += ph + 10
assert y0 - 10 + 10 <= H, (y0, H)
alt = ("Schematic map of the American acquisitions of 1898 to 1917, in two lists. Pacific: Hawaii (annexed July 1898), the Philippines and Guam "
       "(Treaty of Paris, December 1898), Wake Island (taken 1899), American Samoa (treaty of 1899). Caribbean and Central America: Puerto Rico "
       "(Treaty of Paris, December 1898), Cuba (Platt Amendment, 1901), the Panama Canal Zone (treaty of November 1903) and the Virgin Islands "
       "(bought from Denmark, 1917).")
fig = (f'<figure class="fig small"><svg viewBox="0 0 {W} {y0 - 10 + 10}" role="img" aria-label="{alt}">' + "".join(out) +
       '</svg><figcaption>American acquisitions and protectorates, 1898–1917. Cuba was never annexed: it stayed formally independent but bound by the Platt Amendment until 1934.</figcaption></figure>')
p = "chapters/hist.int.empire.4.md"
t = open(p, encoding="utf8").read()
t2, n = re.subn(r'<figure class="fig"><svg viewBox="0 0 600 300".*?</figure>', lambda m: fig, t, flags=re.S)
assert n == 1
open(p, "w", encoding="utf8").write(t2)
print("viewBox height", y0)
