# data/place_figs_p10.py: pastes the generated <figure> lines over the placeholder lines
# <figure data-ph="name"></figure> in the P10 chapters. Changes no other line. Run after fig_bio.*.py.
import json, re
for ch, js in (("bio.immunity", "data/out_immunity.json"), ("bio.antibodies", "data/out_antibodies.json")):
    figs = json.load(open(js, encoding="utf-8"))
    p = f"chapters/{ch}.md"
    import os
    if not os.path.exists(p):
        continue
    lines = open(p, encoding="utf-8").read().split("\n")
    n = 0
    for i, ln in enumerate(lines):
        m = re.match(r'<figure data-ph="(\w+)"></figure>$', ln)
        if m:
            lines[i] = figs[m.group(1)]
            n += 1
        elif ln.startswith("<figure") and 'data-ph' not in ln:
            for name, fig in figs.items():
                # re-placement: a figure already pasted is replaced when its aria-label matches the new one
                lab = re.search(r'aria-label="([^"]{30})', fig).group(1)
                if f'aria-label="{lab}' in ln:
                    lines[i] = fig
                    n += 1
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    print(ch, n, "figures placed")
