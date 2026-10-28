# data/stitch.py: builds chapters/<id>.md from data/<id>.tpl.md by replacing %%FIGn%% (n = 0, 1, ...) with the
# n-th <figure> printed by data/fig_<id>.py. Only figure markup is inserted; the chapter text (maths, backslashes) is
# copied unchanged. Usage: py data/stitch.py bio.cells
import subprocess, sys, re, os
cid = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
out = subprocess.run([sys.executable, os.path.join(here, f"fig_{cid}.py")], capture_output=True, text=True, encoding="utf-8")
figs = [x.strip() for x in out.stdout.strip().split("\n\n") if x.strip()]
tpl = open(os.path.join(here, f"{cid}.tpl.md"), encoding="utf-8").read()
def sub(m):
    return figs[int(m.group(1))]
res = re.sub(r"%%FIG(\d+)%%", sub, tpl)
open(os.path.join(root, "chapters", f"{cid}.md"), "w", encoding="utf-8").write(res)
print(out.stderr.strip() or "clearance ok", f"| {len(figs)} figures | {len(res.split())} words")
