# REVIEW helper: prints the :::why, :::key, :::eg, :::quiz and exam-practice blocks of a chapter (no figure lines)
import sys, re
t = open(f"chapters/{sys.argv[1]}.md", encoding="utf-8").read().split("\n")
want = tuple(sys.argv[2].split(",")) if len(sys.argv) > 2 else (":::why", ":::key", ":::eg", ":::quiz", ":::try Exam")
out, on, depth = [], False, 0
for i, l in enumerate(t, 1):
    if not on and l.startswith(want): on, depth = True, 0
    if on:
        if l.startswith("<figure") or l.startswith("--"): out.append(f"{i}: [figure/plot]")
        else: out.append(f"{i}: {l}")
        if l.startswith(":::") and l.strip() != ":::": depth += 1
        elif l.strip() == ":::":
            depth -= 1
            if depth <= 0: on = False
print("\n".join(out))
