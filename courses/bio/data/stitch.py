# data/stitch.py: builds chapters/<id>.md from data/<id>.tpl.md by replacing %%FIGn%% (n = 0, 1, ...) with the
# n-th <figure> printed by data/fig_<id>.py. Only figure markup is inserted; the chapter text (maths, backslashes) is
# copied unchanged. Usage: py data/stitch.py bio.cells
# REVIEW P2: the template is a second copy of the chapter text. Any Edit to the chapter must be made to the template
# too. This script refuses to run if the chapter's non-figure lines differ from the template's (so no Edit is lost).
import subprocess, sys, re, os
cid = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
chap = os.path.join(root, "chapters", f"{cid}.md")
tpl = open(os.path.join(here, f"{cid}.tpl.md"), encoding="utf-8").read()
if os.path.exists(chap):
    a = [l for l in open(chap, encoding="utf-8").read().split("\n") if not l.startswith("<figure")]
    b = [l for l in tpl.split("\n") if not re.fullmatch(r"%%FIG\d+%%", l)]
    if a != b:
        bad = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        sys.exit(f"stitch: chapters/{cid}.md and data/{cid}.tpl.md differ (first at non-figure line {bad + 1}); "
                 "copy the Edit into the template first")
out = subprocess.run([sys.executable, os.path.join(here, f"fig_{cid}.py")], capture_output=True, text=True, encoding="utf-8")
figs = [x.strip() for x in out.stdout.strip().split("\n\n") if x.strip()]
def sub(m):
    return figs[int(m.group(1))]
res = re.sub(r"%%FIG(\d+)%%", sub, tpl)
open(chap, "w", encoding="utf-8").write(res)
print(out.stderr.strip() or "clearance ok", f"| {len(figs)} figures | {len(res.split())} words")
