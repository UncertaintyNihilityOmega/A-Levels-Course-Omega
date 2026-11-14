# data/cs.os_fig.py: generates and checks the SVG figures of cs.os (layers, process states, Gantt charts, paging).
# Usage: py data/cs.os_fig.py          writes data/cs.os_figs.txt and checks label positions
#        py data/cs.os_fig.py inject   replaces each line "@@FIG name@@" in chapters/cs.os.md by its block
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "data"))
spec = importlib.util.spec_from_file_location("bfig", ROOT / "data" / "cs.boolean_fig.py")
bfig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bfig)
Fig = bfig.Fig
PROBLEMS = bfig.PROBLEMS
from cs_sched_model import schedule  # noqa: E402

FIGS = []


def layers():
    f = Fig("layers", 330, 262, "fig small",
            "Layers between a user and the hardware, from top to bottom: the user; application software; the user interface (graphical or command line); the operating system, with its kernel and system calls; device drivers; the hardware, which is the processor, memory and devices.",
            "The user never deals with the hardware directly. Each layer hides the details of the layer below it.")
    labels = [("The user", 0), ("Application software", 1), ("User interface (GUI or command line)", 2),
              ("Operating system: kernel and system calls", 3), ("Device drivers", 4), ("Hardware: processor, memory, devices", 5)]
    for text, k in labels:
        y = 8 + k * 40
        f.rect(20, y, 290, 28, "fm s-acc sw2", 4)
        f.text(165, y + 19, text, "middle")
    for k in range(5):
        y = 8 + k * 40 + 28
        f.line([(165, y), (165, y + 12)], arrow=True)
    FIGS.append(f)


def states():
    f = Fig("states", 660, 270, "fig",
            "Process state diagram. Five boxes: New, Ready, Running, Blocked and Terminated. New goes to Ready when the process is admitted. Ready goes to Running when the scheduler dispatches it. Running goes back to Ready when its time slice ends. Running goes to Blocked when it waits for input, output or an event. Blocked goes to Ready when that input, output or event completes. Running goes to Terminated when the process finishes. There is no arrow from Blocked to Running.",
            "The life of a process. Only three of the states (Running, Ready, Blocked) are examined in detail; a Blocked process can only move to Ready, never straight to Running.")
    boxes = {"New": (10, 50, 80, 40), "Ready": (170, 50, 90, 40), "Running": (380, 50, 100, 40),
             "Blocked": (240, 200, 100, 40), "Terminated": (530, 200, 100, 40)}
    for name, (x, y, w, h) in boxes.items():
        f.rect(x, y, w, h, "fm s-acc sw2", 6)
        f.text(x + w / 2, y + h / 2 + 5, name, "middle", "tb")
    f.line([(90, 70), (168, 70)], arrow=True)
    f.text(129, 62, "admitted", "middle")
    f.line([(260, 60), (378, 60)], arrow=True)
    f.text(319, 46, "dispatched", "middle")
    f.line([(378, 80), (262, 80)], arrow=True)
    f.text(319, 102, "time slice ends", "middle")
    f.line([(440, 90), (440, 220), (342, 220)], arrow=True)
    f.text(448, 150, "waits for I/O")
    f.text(448, 171, "or an event")
    f.line([(240, 220), (215, 220), (215, 92)], arrow=True)
    f.text(207, 150, "I/O or event", "end")
    f.text(207, 171, "completes", "end")
    f.line([(480, 70), (580, 70), (580, 198)], arrow=True)
    f.text(588, 140, "finishes")
    FIGS.append(f)


def gantt():
    P = [("A", 0, 5), ("B", 1, 3), ("C", 2, 8), ("D", 3, 2)]
    unit, x0 = 30, 62
    f = Fig("gantt", 624, 262, "fig",
            "Four Gantt charts for the same four processes (A arrives at 0 and needs 5 units, B arrives at 1 and needs 3, C arrives at 2 and needs 8, D arrives at 3 and needs 2). First come first served: A 0 to 5, B 5 to 8, C 8 to 16, D 16 to 18. Shortest job first: A 0 to 5, D 5 to 7, B 7 to 10, C 10 to 18. Shortest remaining time: A 0 to 1, B 1 to 4, D 4 to 6, A 6 to 10, C 10 to 18. Round robin with quantum 2: A 0 to 2, B 2 to 4, C 4 to 6, A 6 to 8, D 8 to 10, B 10 to 11, C 11 to 13, A 13 to 14, C 14 to 18.",
            "The same four processes under four algorithms. Each bar shows which process has the processor, and the numbers under it are times.")
    for r, (algo, label) in enumerate((("fcfs", "FCFS"), ("sjf", "SJF"), ("srt", "SRT"), ("rr", "RR (2)"))):
        y = 10 + r * 62
        f.text(8, y + 19, label)
        segs = schedule(P, algo, 2)
        ticks = []
        for name, s, e in segs:
            f.rect(x0 + s * unit, y, (e - s) * unit, 26, "fm s-acc sw2")
            f.text(x0 + (s + e) * unit / 2, y + 18, name, "middle", "tb")
            ticks.append(s)
        ticks.append(segs[-1][2])
        for t in ticks:
            f.text(x0 + t * unit, y + 42, str(t), "middle")
    FIGS.append(f)


def paging():
    f = Fig("paging", 640, 300, "fig",
            "Paging. A process has four pages numbered 0 to 3. The page table says page 0 is in frame 1, page 1 is in frame 2, page 2 is not in RAM and is on disk, and page 3 is in frame 4. RAM has five frames, numbered 0 to 4: frame 0 holds a page of another process, frame 1 holds page 0, frame 2 holds page 1, frame 3 is free, and frame 4 holds page 3. Arrows run from the page table entries to the frames.",
            "Pages of one process (left) are placed in any free frames of RAM (right). The page table records where each page is, or that it is on disk.")
    f.text(10, 20, "Pages of the process")
    f.text(210, 20, "Page table")
    f.text(440, 20, "RAM (frames)")
    entries = ["frame 1", "frame 2", "on disk", "frame 4"]
    for k in range(4):
        y = 40 + k * 36
        f.rect(10, y, 100, 36, "fm s-acc sw2")
        f.text(60, y + 23, f"Page {k}", "middle")
        f.line([(110, y + 18), (210, y + 18)], arrow=True)
        f.rect(210, y, 130, 36, "fm s-acc sw2")
        f.text(220, y + 23, f"{k}: {entries[k]}")
    contents = ["other process", "page 0", "page 1", "free", "page 3"]
    for k in range(5):
        y = 40 + k * 36
        f.rect(440, y, 130, 36, "fm s-acc sw2")
        f.text(450, y + 23, f"{k}: {contents[k]}")
    # table rows to frames: row 0 -> frame 1, row 1 -> frame 2, row 3 -> frame 4
    f.line([(340, 58), (370, 58), (370, 94), (438, 94)], arrow=True)
    f.line([(340, 94), (355, 94), (355, 130), (438, 130)], arrow=True)
    f.line([(340, 166), (385, 166), (385, 202), (438, 202)], arrow=True)
    f.rect(210, 232, 130, 36, "fm s-acc sw2 dash")
    f.text(275, 255, "Disk: page 2", "middle")
    FIGS.append(f)


def main():
    layers()
    states()
    gantt()
    paging()
    for f in FIGS:
        f.check()
    out = [f"=== {f.name} ===\n:::html\n{f.block()}\n:::\n" for f in FIGS]
    (ROOT / "data" / "cs.os_figs.txt").write_text("\n".join(out), encoding="utf-8")
    print("figures:", len(FIGS), "problems:", len(PROBLEMS))
    for p in PROBLEMS:
        print("  ", p)
    if len(sys.argv) > 1 and sys.argv[1] == "refresh":
        path = ROOT / "chapters" / "cs.os.md"
        text = path.read_text(encoding="utf-8")
        for f in FIGS:
            pat = re.compile(r'<figure[^>]*><svg[^>]*aria-label="' + re.escape(f.aria) + r'".*?</figure>', re.S)
            assert pat.search(text), f.name
            text = pat.sub(lambda m: f.block(), text, count=1)
        path.write_text(text, encoding="utf-8")
        print("refreshed")
    if len(sys.argv) > 1 and sys.argv[1] == "inject":
        path = ROOT / "chapters" / "cs.os.md"
        text = path.read_text(encoding="utf-8")
        for f in FIGS:
            marker = f"@@FIG {f.name}@@"
            assert marker in text, marker
            text = text.replace(marker, f":::html\n{f.block()}\n:::")
        path.write_text(text, encoding="utf-8")
        print("injected")


if __name__ == "__main__":
    main()
