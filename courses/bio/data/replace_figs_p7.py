# data/replace_figs_p7.py <chapter id>: replaces every <figure> line of chapters/<id>.md, in order, by the figures printed by
# data/fig_<id>.py (same order as NAMES). Touches only <figure> lines; every other line stays unchanged.
import subprocess, sys, os
cid = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
chap = os.path.join(root, "chapters", f"{cid}.md")
out = subprocess.run([sys.executable, os.path.join(here, f"fig_{cid}.py")], capture_output=True, text=True, encoding="utf-8")
figs = [x.strip() for x in out.stdout.strip().split("\n\n") if x.strip()]
lines = open(chap, encoding="utf-8").read().split("\n")
idx = [i for i, l in enumerate(lines) if l.startswith("<figure")]
assert len(idx) == len(figs), (len(idx), len(figs))
for i, f in zip(idx, figs):
    lines[i] = f
open(chap, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print(out.stderr.strip() or "clearance ok", "| replaced", len(idx))
