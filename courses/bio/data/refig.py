# data/refig.py <chapter id> [generator]: re-places hand SVGs after a generator change (REVIEW P4, P5, P7).
# Runs data/fig_<id>.py (or the generator named), and replaces each <figure> line of chapters/<id>.md whose aria-label
# starts with the same 40 characters as a generated figure. Touches only those lines; prints what it replaced.
import subprocess, sys, os, re
cid = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
gen = os.path.join(here, sys.argv[2] if len(sys.argv) > 2 else f"fig_{cid}.py")
out = subprocess.run([sys.executable, gen], capture_output=True, text=True, encoding="utf-8")
figs = [l.strip() for l in out.stdout.splitlines() if l.strip().startswith("<figure")]
key = lambda s: (re.search(r'aria-label="([^"]{0,40})', s) or [None, None])[1]
chap = os.path.join(root, "chapters", f"{cid}.md")
raw = open(chap, encoding="utf-8", newline="").read()
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.split(nl)
done = []
for f in figs:
    k = key(f)
    hits = [i for i, l in enumerate(lines) if l.startswith("<figure") and key(l) == k]
    if len(hits) == 1 and lines[hits[0]] != f:
        lines[hits[0]] = f; done.append(k)
open(chap, "w", encoding="utf-8", newline="").write(nl.join(lines))
print(out.stderr.strip()[-300:] or "clearance ok", "| replaced:", done)
