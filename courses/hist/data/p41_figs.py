# data/p41_figs.py: draws the two stacked-box figures of P41 (hist.skills.sources, hist.skills.essays) and checks that
# every label fits its box (7 px per character) and every box clears the next. Prints the SVG to data/p41_*.svg.txt.
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

W = 340
X0, BW = 15, 310
CH = 7.0      # px per character of a 13 px label
LINE = 17
GAP = 24


def stack(name, boxes, aria, caption):
    """boxes: list of (class_fill, title, [lines]). Returns svg text."""
    y = 10
    parts, arrows, geo = [], [], []
    for i, (fill, title, lines) in enumerate(boxes):
        n = 1 + len(lines)
        h = 10 + LINE * n + 2
        parts.append(f'<rect class="{fill} s-acc sw2" x="{X0}" y="{y}" width="{BW}" height="{h}" rx="6"/>')
        ty = y + 20
        assert len(title) * CH <= BW - 20, f"{name}: title too long: {title}"
        parts.append(f'<text class="tl tb" x="{X0 + 10}" y="{ty}">{title}</text>')
        for j, ln in enumerate(lines):
            assert len(ln) * CH <= BW - 20, f"{name}: line too long ({len(ln) * CH:.0f}px): {ln}"
            parts.append(f'<text class="tl" x="{X0 + 10}" y="{ty + LINE * (j + 1)}">{ln}</text>')
        geo.append((y, y + h))
        if i < len(boxes) - 1:
            arrows.append(f'<line class="ln" x1="{W // 2}" y1="{y + h + 3}" x2="{W // 2}" y2="{y + h + GAP - 3}" marker-end="url(#ah)"/>')
        y += h + GAP
    total = y - GAP + 12
    for a, b in zip(geo, geo[1:]):
        assert b[0] - a[1] == GAP
    svg = (f'<figure class="fig small"><svg viewBox="0 0 {W} {total}" role="img" aria-label="{aria}">'
           + "".join(parts) + "".join(arrows)
           + f'</svg><figcaption>{caption}</figcaption></figure>')
    with open(f"data/p41_{name}.svg.txt", "w", encoding="utf-8") as f:
        f.write(svg)
    print(name, "viewBox", W, total, "boxes", len(boxes), "chars", len(svg))
    return svg


stack("sources", [
    ("fm", "1  Decode the claim", ["What exactly must the sources show?", "Underline the key words."]),
    ("fp", "2  One line per source", ["Does it support, challenge or do both?", "Quote the words that show it."]),
    ("fm", "3  Weigh each source", ["Nature, origin, purpose, context:", "stronger or weaker for THIS claim?"]),
    ("fp", "4  Bring your knowledge", ["Test each source against what you know;", "add what the sources leave out."]),
    ("fm", "5  Group and judge", ["Paragraphs by argument, not by source;", "end with a judgement on 'how far'."]),
], "Five stacked steps for a Paper 1 part (b) answer joined by downward arrows. Step 1, decode the claim: what exactly must the sources show, underline the key words. Step 2, one line per source: does it support, challenge or do both, quote the words that show it. Step 3, weigh each source: nature, origin, purpose and context, stronger or weaker for this claim. Step 4, bring your knowledge: test each source against what you know and add what the sources leave out. Step 5, group and judge: paragraphs by argument, not by source, ending with a judgement on how far.",
   "The five steps of a part (b) answer. Steps 2 and 3 are done on the question paper; steps 4 and 5 are the answer.")

stack("essays", [
    ("fm", "1  Unpack the question", ["Command word, topic, focus, dates.", "What would a one-sided answer ignore?"]),
    ("fp", "2  Plan in 3 to 5 minutes", ["Factors for and against, ranked.", "Choose the criterion and the judgement."]),
    ("fm", "3  Introduction", ["Two to four sentences: your line of", "argument and how you will judge it."]),
    ("fp", "4  Paragraphs that argue", ["Point, evidence, explain, then link to", "the question and to the other factors."]),
    ("fm", "5  Conclusion", ["Weigh the factors by your criterion.", "Say which is stronger and why."]),
], "Five stacked steps for an essay answer joined by downward arrows. Step 1, unpack the question: command word, topic, focus and dates, and what a one-sided answer would ignore. Step 2, plan in three to five minutes: factors for and against, ranked, with the criterion and the judgement chosen. Step 3, introduction: two to four sentences giving your line of argument and how you will judge it. Step 4, paragraphs that argue: point, evidence, explain, then link to the question and to the other factors. Step 5, conclusion: weigh the factors by your criterion and say which is stronger and why.",
   "The route from question to judgement. The plan decides the argument before a word of the answer is written.")
