# REVIEW P6/P8/P9: one-off helper that replaced section 5 (capillary bed) of data/fig_bio.mammaltransport.py
# with a 340-wide version (the 560-wide figure had 6 px labels on phones). Kept for the record; running it twice is harmless.
p = 'data/fig_bio.mammaltransport.py'
s = open(p, encoding='utf-8').read()
a = s.index('# ---------- 5. capillary bed')
b = s.index('print(' + chr(34) + chr(92) + 'n' + chr(92) + 'n' + chr(34) + '.join(figs))')
new = '''# ---------- 5. capillary bed with pressure arrows (REVIEW P6/P8/P9: redrawn 340 wide for phones) ----------
f = Fig("capbed")
cy = 124
top_y, bot_y = cy - 18, cy + 18
# arteriole (left) tapering into the capillary, venule (right)
f.poly([(10, cy - 36), (60, top_y), (60, bot_y), (10, cy + 36)], MID, closed=False, check=True)
f.poly([(330, cy - 36), (280, top_y), (280, bot_y), (330, cy + 36)], MID, closed=False, check=True)
# capillary walls with gaps (every arrow passes through a gap)
gaps_top = [85, 115, 225, 255]
gaps_bot = [85, 115, 170, 225, 255]
def wall(y, gaps):
    xs = [60] + [g for g in gaps for g in (g - 4, g + 4)] + [280]
    for a, b in zip(xs[::2], xs[1::2]):
        f.line([(a, y), (b, y)], "c1 sw3", check=True)
wall(top_y, gaps_top); wall(bot_y, gaps_bot)
# one tissue cell above
f.rect(135, 34, 70, 36, WALL, 8)
f.text(170, 56, "tissue cell", "tl", "middle")
# red cells and proteins in the lumen
for x in (75, 150, 205, 268):
    f.parts.append(f'<ellipse class="fr ln" cx="{x}" cy="{cy}" rx="8" ry="5"/>')
for x, y in [(98, cy - 8), (128, cy + 8), (178, cy - 8), (188, cy + 7), (238, cy + 8), (248, cy - 7)]:
    f.parts.append(f'<circle class="fi" cx="{x}" cy="{y}" r="2.5"/>')
# fluid out at the arterial end, water back in at the venous end
for x in (85, 115):
    f.line([(x, top_y - 4), (x, 50)], "c3 sw2", "ah")
    f.line([(x, bot_y + 4), (x, cy + 64)], "c3 sw2", "ah")
for x in (225, 255):
    f.line([(x, 50), (x, top_y - 4)], "c4 sw2", "ah")
    f.line([(x, cy + 64), (x, bot_y + 4)], "c4 sw2", "ah")
# along the top: pressure falls
f.text(170, 12, "hydrostatic pressure falls", "tl", "middle")
f.line([(60, 22), (280, 22)], "ln-m thin dash", "ah")
# labels
f.text(10, 70, "arteriole", "tl"); f.text(330, 70, "venule", "tl", "end")
f.text(170, 94, "tissue fluid", "tl", "middle")
f.text(170, 176, "gap between", "tl", "middle"); f.text(170, 190, "endothelium cells", "tl", "middle")
f.leader((170, 164), (170, bot_y + 3))
f.text(10, 214, "high pressure:", "tl"); f.text(10, 228, "fluid forced out", "tl")
f.text(330, 214, "lower pressure:", "tl", "end"); f.text(330, 228, "water in by osmosis", "tl", "end")
f.text(10, 256, "red blood cell", "tl"); f.parts.append('<ellipse class="fr ln" cx="100" cy="252" rx="8" ry="5"/>')
f.text(140, 256, "plasma protein", "tl"); f.parts.append('<circle class="fi" cx="229" cy="252" r="2.5"/>')
f.text(10, 278, "blood flows from left to right", "tl")
done(f, (340, 290),
     "A capillary bed. Blood flows from an arteriole on the left, through a capillary with gaps between the endothelium cells of its wall, to a venule on the right. At the arterial end, arrows show fluid forced out through the gaps into the tissue fluid by high hydrostatic pressure. At the venous end, arrows show water returning into the capillary by osmosis. Red blood cells and plasma proteins stay inside the capillary.",
     "Tissue fluid. Outward arrows: fluid is forced out at the arterial end by hydrostatic pressure. Inward arrows: water returns by osmosis at the venous end because the plasma proteins lower the water potential of the plasma. Red blood cells and proteins stay in the capillary. Excess tissue fluid drains into lymph vessels.")

'''
s = s[:a] + new + s[b:]
open(p, 'w', encoding='utf-8').write(s)
print("section 5 replaced")
