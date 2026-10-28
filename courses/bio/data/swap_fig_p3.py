# data/swap_fig_p3.py: puts the SVG figures made by a data/fig_*.py script into a P3 chapter.
# Run: PYTHONUTF8=1 py data/swap_fig_p3.py chapters/<id>.md data/fig_<x>.py
# For each figure the generator prints (in order): if the chapter holds a line "@@FIG n@@" (n = 1, 2, ...) that line is replaced;
# otherwise the existing <figure> with the same aria-label start is replaced. Only <figure> lines are touched (no maths).
import re, subprocess, sys

chap, gen = sys.argv[1], sys.argv[2]
out = subprocess.run([sys.executable, gen], capture_output=True, text=True, encoding="utf-8",
                     env={**__import__("os").environ, "PYTHONUTF8": "1"}).stdout
figs = [b.strip() for b in out.split("\n\n") if b.strip().startswith("<figure")]
text = open(chap, encoding="utf-8").read()
n_new = n_swap = 0
for i, fig in enumerate(figs, 1):
    ph = f"@@FIG {i}@@"
    if ph in text:
        text = text.replace(ph, fig)
        n_new += 1
        continue
    key = re.search(r'aria-label="(.{0,60})', fig).group(1)
    m = re.search(r'<figure class="fig[^"]*"><svg viewBox="[^"]*" role="img" aria-label="' + re.escape(key) + r'.*?</figure>', text, re.S)
    if m:
        text = text[:m.start()] + fig + text[m.end():]
        n_swap += 1
open(chap, "w", encoding="utf-8").write(text)
print(f"figures generated {len(figs)}: placed {n_new}, swapped {n_swap}")
