# data/place_figs_p14.py <chapter id>: puts the figures of data/fig_<id>.py into chapters/<id>.md (copy of place_figs_p6.py).
# First run: replaces each @@FIG_<NAME> placeholder line; later runs refresh the <figure> lines in order. Only those lines change.
# Only those lines change; every other line of the chapter is written back unchanged.
import subprocess, sys, os, re
cid = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
chap = os.path.join(root, "chapters", f"{cid}.md")
src = open(os.path.join(here, f"fig_{cid}.py"), encoding="utf-8").read()
names = eval(re.search(r"^NAMES = (\[.*\])", src, re.M).group(1))
out = subprocess.run([sys.executable, os.path.join(here, f"fig_{cid}.py")], capture_output=True, text=True, encoding="utf-8")
figs = [x.strip() for x in out.stdout.strip().split("\n\n") if x.strip()]
assert len(figs) == len(names), (len(figs), out.stderr[-500:])
lines = open(chap, encoding="utf-8").read().split("\n")
for i, l in enumerate(lines):
    if l.startswith("@@FIG_"):
        lines[i] = figs[names.index(l[6:].strip())]
fig_idx = [i for i, l in enumerate(lines) if l.startswith("<figure")]
assert len(fig_idx) == len(figs), f"{len(fig_idx)} figure lines in the chapter but {len(figs)} figures made"
for i, f_ in zip(fig_idx, figs):        # placed ones are replaced by the same text; older ones are refreshed
    lines[i] = f_
open(chap, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print(out.stderr.strip() or "clearance ok", "| placed", len(figs))
