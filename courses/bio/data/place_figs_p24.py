# data/place_figs_p24.py: pastes the P24 figures into the two mock chapters. It replaces only the text after a marker
# <!--FIG:name--> on the same line; every other line is left unchanged. Run: py data/place_figs_p24.py
import importlib.util, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
bad = []
for chap, fname in (("bio.mock.p3", "fig_bio.mock.p3.py"), ("bio.mock.p5", "fig_bio.mock.p5.py")):
    spec = importlib.util.spec_from_file_location("m_" + chap.replace(".", "_"), os.path.join(HERE, fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    out = m.figures()
    figs, problems = out[0], out[1]
    bad += problems
    path = os.path.join(ROOT, "chapters", chap + ".md")
    if not os.path.exists(path):
        continue
    text = open(path, encoding="utf-8").read()
    n = 0
    for name, html in figs.items():
        pat = re.compile(r"<!--FIG:" + re.escape(name) + r"-->(<figure.*?</figure>)?")
        text, k = pat.subn(lambda mm: "<!--FIG:" + name + "-->" + html, text)
        n += k
    open(path, "w", encoding="utf-8").write(text)
    print(chap, "figures placed:", n, "of", len(figs))
print("\n".join(bad) or "clearance ok")
