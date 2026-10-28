# data/place_membranes_figs.py: replaces only the fluid mosaic <figure> line of chapters/bio.membranes.md with the one
# data/fig_bio.membranes.py generates (the first figure it prints). Every other line is left unchanged.
import subprocess, sys
root = __file__.rsplit("data", 1)[0]
out = subprocess.run([sys.executable, root + "data/fig_bio.membranes.py"], capture_output=True, encoding="utf-8").stdout
fig = [l for l in out.splitlines() if l.startswith("<figure")][0]
path = root + "chapters/bio.membranes.md"
lines = open(path, encoding="utf-8", newline="").read().split("\n")
hits = [i for i, l in enumerate(lines) if l.startswith("<figure") and 'aria-label="Fluid mosaic model' in l]
assert len(hits) == 1, hits
eol = "\r" if lines[hits[0]].endswith("\r") else ""
lines[hits[0]] = fig + eol
open(path, "w", encoding="utf-8", newline="").write("\n".join(lines))
print("replaced line", hits[0] + 1)
