# data/place_figs_mitosis.py: replaces the @@FIG_* placeholder lines of chapters/bio.mitosis.md by the figures printed by
# data/fig_bio.mitosis.py (in order CHROM, CYCLE, ST1, ST2, CYTO, FIVE). Touches only those lines.
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
chap = os.path.join(root, "chapters", "bio.mitosis.md")
out = subprocess.run([sys.executable, os.path.join(here, "fig_bio.mitosis.py")], capture_output=True, text=True, encoding="utf-8")
figs = [x.strip() for x in out.stdout.strip().split("\n\n") if x.strip()]
names = ["CHROM", "CYCLE", "ST1", "ST2", "CYTO", "FIVE"]
assert len(figs) == len(names), len(figs)
lines = open(chap, encoding="utf-8").read().split("\n")
for i, l in enumerate(lines):
    if l.startswith("@@FIG_"):
        lines[i] = figs[names.index(l[6:].strip())]
open(chap, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print(out.stderr.strip(), "placed")
