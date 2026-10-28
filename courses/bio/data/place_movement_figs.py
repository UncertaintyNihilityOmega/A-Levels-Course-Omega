# data/place_movement_figs.py: replaces the @@NAME@@ placeholder lines of chapters/bio.movement.md with the figures
# that data/fig_bio.movement.py generates (order there: plant, rbc, active, visking). Touches only those lines.
import re, subprocess, sys
root = __file__.rsplit("data", 1)[0]
out = subprocess.run([sys.executable, root + "data/fig_bio.movement.py"], capture_output=True, encoding="utf-8").stdout
figs = [l for l in out.splitlines() if l.startswith("<figure")]
assert len(figs) == 4, len(figs)
names = ["PLANT", "RBC", "ACTIVE", "VISKING"]
path = root + "chapters/bio.movement.md"
text = open(path, encoding="utf-8", newline="").read()
for n, fig in zip(names, figs):
    pat = re.compile(r"^@@" + n + r"@@(\r?)$", re.M)
    if pat.search(text):
        text = pat.sub(lambda m: fig + m.group(1), text, count=1)
open(path, "w", encoding="utf-8", newline="").write(text)
print("placed", [n for n in names if "@@" + n + "@@" not in text])
