# data/place_figs_p19.py: pastes the P19 figures into the chapters. It replaces only the text after a marker
# <!--FIG:name--> on the same line; every other line is left unchanged.
# Run: py data/place_figs_p19.py
import importlib.util, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load(fname):
    p = os.path.join(HERE, fname)
    if not os.path.exists(p):
        return {}, []
    spec = importlib.util.spec_from_file_location("m_" + fname.replace(".", "_"), p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.figures()


CHAPTERS = {"bio.practical": "fig_bio.practical.py", "bio.practical2": "fig_bio.practical2.py"}
bad = []
for chap, fname in CHAPTERS.items():
    figs, problems = load(fname)
    bad += problems
    path = os.path.join(ROOT, "chapters", chap + ".md")
    if not os.path.exists(path) or not figs:
        continue
    text = open(path, encoding="utf-8").read()
    n = 0
    for name, html in figs.items():
        pat = re.compile(r"<!--FIG:" + re.escape(name) + r"-->(<figure.*?</figure>)?")
        text, k = pat.subn(lambda m: "<!--FIG:" + name + "-->" + html, text)
        n += k
    open(path, "w", encoding="utf-8").write(text)
    print(chap, "figures placed:", n, "of", len(figs))
print("\n".join(bad) or "clearance ok")
