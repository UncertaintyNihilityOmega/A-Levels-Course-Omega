# data/packages.py: writes packages/Pn.md from course.json, data/outcomes.json (syllabus content) and data/pkg_notes.py
# Run from the course folder: py data/packages.py   (overwrites packages/*.md: run it only before Writers add notes)
import json
import os
import sys

sys.path.insert(0, "data")
from pkg_notes import N, W  # noqa: E402

J = json.load(open("course.json", encoding="utf-8"))
O = json.load(open("data/outcomes.json", encoding="utf-8"))
order = [c["id"] for c in J["chapters"]]
title = {c["id"]: c["title"] for c in J["chapters"]}
level = {c["id"]: c["level"] for c in J["chapters"]}
AS_T = ["hist.eu.france", "hist.eu.germany", "hist.eu.russia", "hist.us.civilwar", "hist.us.gilded",
        "hist.us.depression", "hist.int.empire", "hist.int.1919", "hist.int.1929"]
P4_T = ["hist.d.italy", "hist.d.stalin", "hist.d.hitler", "hist.d.usa45", "hist.d.usa61", "hist.d.usa74",
        "hist.d.soviet", "hist.d.safrica", "hist.d.malaysia"]
ROT = {  # Paper 1 year for each AS topic (FACTS.md)
    "hist.eu.france": 2027, "hist.eu.germany": 2028, "hist.eu.russia": 2029,
    "hist.us.gilded": 2027, "hist.us.depression": 2028, "hist.us.civilwar": 2029,
    "hist.int.empire": 2027, "hist.int.1919": 2028, "hist.int.1929": 2029}
OPT = {"eu": "European option (Section A)", "us": "American option (Section B)", "int": "International option (Section C)",
       "d.italy": "European option", "d.stalin": "European option", "d.hitler": "European option",
       "d.usa45": "American option", "d.usa61": "American option", "d.usa74": "American option",
       "d.soviet": "International option", "d.safrica": "International option", "d.malaysia": "International option"}


def syllabus(cid):
    parts = cid.split(".")
    pre, n = ".".join(parts[:-1]), parts[-1]
    if pre in AS_T and n.isdigit():
        t, k, bl = O["AS"][AS_T.index(pre) * 4 + int(n) - 1]
    elif pre in P4_T and n.isdigit():
        t, k, bl = O["P4"][P4_T.index(pre) * 4 + int(n) - 1]
    else:
        return None
    lines = [f"- Syllabus topic: {t.strip()}", f"- Key question {k}", "- Content (cover all of it; 'including' items in full):"]
    for b in bl:
        head, subs = b[0][2:].strip(), b[1:]
        line = head
        if subs:
            items = []
            for x in subs:
                if x.startswith("–"):
                    items.append(x[1:].strip())
                elif items:
                    items[-1] += (": " if items[-1].endswith("including") else ", ") + x[1:].strip()
                else:
                    items.append(x[1:].strip())
            line += ": " + "; ".join(items)
        lines.append("  - " + line)
    return "\n".join(lines)


def examined(cid):
    pre = ".".join(cid.split(".")[:-1])
    if pre in ROT:
        y = ROT[pre]
        others = [x for x in (2027, 2028, 2029) if x != y]
        opt = OPT[cid.split(".")[1]]
        return (f"- Examined: AS {opt}. **Paper 1** (sources) in **{y}**; **Paper 2** (essays) in **{others[0]}** and "
                f"**{others[1]}**. Teach both styles (COURSE.md). Opening `:::exam Where this is examined` box says this.")
    if pre in P4_T:
        return f"- Examined: A Level **Paper 4**, {OPT[cid.split('.')[1] + '.' + cid.split('.')[2]]}: [30] essays, 'Assess' and 'Evaluate' (FACTS.md)."
    if cid.startswith("hist.interp"):
        return "- Examined: A Level **Paper 3** (one extract, one [40] question; FACTS.md has the levels)."
    return None


def nxt(cid):
    i = order.index(cid)
    return order[i + 1] if i + 1 < len(order) else None


HEAD = """# {pid}: {ptitle}

One Writer's package. Read, in this order: COURSE.md (rules, conventions, chapter structure, widget formats, the
verified links), kit/STYLE.md, the gold chapter chapters/hist.eu.france.1.md (match its structure, depth, tone and the
level-by-level model answers), then this file. Grep FACTS.md for your topic's outcomes and for the paper facts and
level descriptors (never invent exam facts). Write each chapter whole, then checks/<id>.py, then `node kit/zta.js check <id>`.

Rules that matter most here:
- Every fact exact; where you are not sure, leave it out. Items marked "check" in these notes are ones to verify in
  a reliable source before you use the number; if you cannot, write a rounded figure with "about" or leave it out.
- Sources: real documents only, provenance line in italics, "Adapted from" when shortened or simplified. Never an
  invented quotation. Historians: named only with work and year, as in these notes.
- No mark tokens ([M1] etc.) in History answers; levels in words. Exam practice in the real styles (FACTS.md).
- Never copy specimen or past-paper questions; these notes say which ones to avoid.
"""

os.makedirs("packages", exist_ok=True)
for p in J["packages"]:
    out = [HEAD.format(pid=p["id"], ptitle=p["title"])]
    out.append("## Chapters\n")
    for cid in p["chapters"]:
        n = N.get(cid, {})
        out.append(f"### {cid} · {title[cid]} (`@level {level[cid]}`)\n")
        if cid == "hist.eu.france.1":
            out.append("Already written by the Specialist (the gold chapter). Do not edit it. Read it first.\n")
            continue
        for x in (examined(cid), syllabus(cid)):
            if x:
                out.append(x)
        for key, lab in (("cover", "What to cover and stress"), ("src", "Real sources for Paper 1 practice and quotation"),
                         ("eg", "Worked examples and practice"), ("hist", "Historians you may name"),
                         ("pit", "Pitfalls"), ("fig", "Figures and widgets")):
            v = n.get(key)
            if v and v != "—":
                out.append(f"- **{lab}.** {v}")
        nx = nxt(cid)
        if nx:
            out.append(f"- **Next line.** `Next: [{title[nx]}](#{nx})`")
        out.append("")
    if p["widgets"]:
        out.append("## Widgets (this package builds them; one file each in widgets/<name>.js; kit/WIDGETS.md)\n")
        for w in p["widgets"]:
            out.append(f"- `{w}`: {W[w]}")
        out.append("- Probe each (`node kit/zta.js widget <name> '<attrs>' --probe`) until clean; look once; use it "
                   "with the keyboard only; test its logic with a small Node script.\n")
    out.append("## Writer's notes\n(The Writer adds notes for the reviewer here: what was hard, anything left out and why, "
               "facts to double-check.)\n")
    open(f"packages/{p['id']}.md", "w", encoding="utf-8").write("\n".join(out))
print(len(J["packages"]), "package files written")
