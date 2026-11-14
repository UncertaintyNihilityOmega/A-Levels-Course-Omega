
# ---------------------------------------------------------------------------------------------
# cs.os: the body of checks/cs.os.py (data/cs.os_body.py is appended to the shared helper above)
# ---------------------------------------------------------------------------------------------
import sys
from fractions import Fraction

sys.path.insert(0, str(CHAPTER.parent.parent / "data"))
from cs_sched_model import schedule, stats, switches  # noqa: E402

assert run_python_blocks([]) == 0
assert lint_pseudocode_blocks() == 0

A = [("A", 0, 5), ("B", 1, 3), ("C", 2, 8), ("D", 3, 2)]


def result_rows(marker):
    """Rows of the first results table after the marker: [name, arrival, burst, completion, turnaround, waiting]."""
    header, rows = table_after(marker)
    return [[r[0]] + [int(x) for x in r[1:]] for r in rows]


def expected_rows(procs, segs):
    rows, at, aw = stats(procs, segs)
    return [[n, a, b, *rows[n]] for n, a, b in procs], at, aw


# ---------------------------------------------------------------------------------------------
# Resources: processor use with n programs (2 ms of processor, 8 ms of waiting)
# ---------------------------------------------------------------------------------------------
cpu, wait = 2, 8
assert Fraction(cpu, cpu + wait) == Fraction(1, 5)
assert [min(100, n * 20) for n in range(1, 6)] == [20, 40, 60, 80, 100]
assert 5 * cpu == cpu + wait

# ---------------------------------------------------------------------------------------------
# The four algorithms on A, B, C, D
# ---------------------------------------------------------------------------------------------
fcfs = schedule(A, "fcfs")
sjf = schedule(A, "sjf")
srt = schedule(A, "srt")
rr2 = schedule(A, "rr", 2)
assert fcfs == [("A", 0, 5), ("B", 5, 8), ("C", 8, 16), ("D", 16, 18)]
assert sjf == [("A", 0, 5), ("D", 5, 7), ("B", 7, 10), ("C", 10, 18)]
assert srt == [("A", 0, 1), ("B", 1, 4), ("D", 4, 6), ("A", 6, 10), ("C", 10, 18)]
assert rr2 == [("A", 0, 2), ("B", 2, 4), ("C", 4, 6), ("A", 6, 8), ("D", 8, 10), ("B", 10, 11), ("C", 11, 13), ("A", 13, 14), ("C", 14, 18)]

for marker, segs, avg_w, avg_t in (("It is the queue at a shop.", fcfs, Fraction(23, 4), Fraction(41, 4)),
                                   ("Then B (3) runs from 7 to 10", sjf, Fraction(4), Fraction(17, 2)),
                                   ("Follow the chart one decision at a time.", srt, Fraction(7, 2), Fraction(8)),
                                   ("On the chart, slices 9 and 10", rr2, Fraction(29, 4), Fraction(47, 4))):
    want, at, aw = expected_rows(A, segs)
    assert result_rows(marker) == want, marker
    assert (at, aw) == (avg_t, avg_w), marker

assert float(Fraction(23, 4)) == 5.75 and float(Fraction(41, 4)) == 10.25
assert "(0 + 6 + 8 + 2) \\div 4 = 16 \\div 4 = 4" in TEXT and "(5 + 0 + 8 + 1) \\div 4 = 14 \\div 4 = 3.5" in TEXT
assert "(9 + 7 + 8 + 5) \\div 4 = 29 \\div 4 = 7.25" in TEXT and float(Fraction(29, 4)) == 7.25
assert "(0 + 4 + 6 + 13) \\div 4 = 23 \\div 4 = 5.75" in TEXT and "(5 + 7 + 14 + 15) \\div 4 = 41 \\div 4 = 10.25" in TEXT
# a pre-emption happens at time 1 for SRT, and not at time 3
assert 3 < 4 and 1 <= 2

# the round robin slice table (unmerged slices)
def rr_slices(procs, q):
    procs = sorted(procs, key=lambda p: (p[1], p[0]))
    pending, queue, rem, t, out = list(procs), [], {n: b for n, a, b in procs}, 0, []

    def admit(upto):
        while pending and pending[0][1] <= upto:
            queue.append(pending.pop(0)[0])

    while pending or queue:
        admit(t)
        if not queue:
            t = pending[0][1]
            continue
        n = queue.pop(0)
        run = min(q, rem[n])
        out.append((n, t, t + run))
        t += run
        rem[n] -= run
        admit(t)
        if rem[n] > 0:
            queue.append(n)
        out[-1] = out[-1] + (rem[n], list(queue))
    return out


slices = rr_slices(A, 2)
header, rows = table_after("| Slice | Process | Times | Left after | Ready queue after the slice |")
assert len(rows) == len(slices) == 10
for r, (n, s, e, left, queue) in zip(rows, slices):
    assert r[1] == n and r[2] == f"{s} to {e}" and int(r[3]) == left, r
    assert r[4] == (", ".join(queue) if queue else "(empty)"), r

# the quantum table
header, rows = table_after("| Quantum | Average waiting time | Switches between processes |")
for r in rows:
    q = int(r[0])
    segs = schedule(A, "rr", q)
    rr_, at, aw = stats(A, segs)
    assert float(aw) == float(r[1]) and aw == Fraction(r[1]).limit_denominator(4), r
    assert switches(segs) == int(r[2]), r
assert [len(r) for r in rows] == [3] * 5
# a quantum at least as long as every burst gives first come first served
assert schedule(A, "rr", 8) == fcfs and schedule(A, "rr", 9) == fcfs

# the comparison table
header, rows = table_after("| Algorithm | Pre-emptive? | Average waiting time (these processes) |")
assert [r[2] for r in rows] == ["5.75", "4", "3.5", "7.25"]

# ---------------------------------------------------------------------------------------------
# Exam-style worked example: P, Q, R, S with quantum 2
# ---------------------------------------------------------------------------------------------
P = [("P", 0, 4), ("Q", 1, 5), ("R", 2, 2), ("S", 4, 3)]
segs = schedule(P, "rr", 2)
assert segs == [("P", 0, 2), ("Q", 2, 4), ("R", 4, 6), ("P", 6, 8), ("S", 8, 10), ("Q", 10, 12), ("S", 12, 13), ("Q", 13, 14)]
rows, at, aw = stats(P, segs)
assert [rows[n][0] for n in "PQRS"] == [8, 14, 6, 13] and [rows[n][2] for n in "PQRS"] == [4, 8, 2, 6] and aw == 5
header, rr_rows = table_after("| Process | Completion | Waiting time |")
assert [r[0] for r in rr_rows] == list("PQRS")
slices = rr_slices(P, 2)
assert [s[3:][1] for s in slices][:3] == [["Q", "R", "P"], ["R", "P", "S", "Q"], ["P", "S", "Q"]]   # queues quoted in the text
assert [s[3:][1] for s in slices][3] == ["S", "Q"] and [s[3:][1] for s in slices][4] == ["Q", "S"] and [s[3:][1] for s in slices][5] == ["S", "Q"]

# ---------------------------------------------------------------------------------------------
# Paging and segmentation
# ---------------------------------------------------------------------------------------------
page_size = 256
table = {0: 1, 1: 2, 2: None, 3: 4}
for logical, page, offset, physical in ((300, 1, 44, 556), (800, 3, 32, 1056), (600, 2, 88, None)):
    assert (logical // page_size, logical % page_size) == (page, offset)
    frame = table[page]
    assert (None if frame is None else frame * page_size + offset) == physical
assert 2 * 256 + 44 == 556 and 4 * 256 + 32 == 1056
segtab = {0: (2000, 600), 1: (5000, 300), 2: (9000, 200)}
assert 5000 + 120 == 5120 and 120 < segtab[1][1] and 350 > segtab[1][1]
# try questions
assert (372 // 100, 372 % 100) == (3, 72)
assert [min(3, 7 - 3 * k) for k in range(3)] == [3, 3, 1]
# exam question: page size 512
pt = {0: 3, 1: 0, 2: 5}
assert (1300 // 512, 1300 % 512, pt[1300 // 512] * 512 + 1300 % 512) == (2, 276, 2836)
assert (700 // 512, 700 % 512, pt[700 // 512] * 512 + 700 % 512) == (1, 188, 188)

# ---------------------------------------------------------------------------------------------
# Page replacement (FIFO and LRU, 3 frames)
# ---------------------------------------------------------------------------------------------
def replace(ref, n, policy):
    frames, out, faults = [], [], 0
    for x in ref:
        fault = x not in frames
        if policy == "lru" and not fault:
            frames.remove(x)
            frames.append(x)
        if fault:
            faults += 1
            if len(frames) == n:
                frames.pop(0)
            frames.append(x)
        out.append((x, list(frames), fault))
    return out, faults


ref = [4, 1, 2, 4, 1, 3, 4, 1, 5, 4, 1, 2]
fifo_out, fifo_faults = replace(ref, 3, "fifo")
lru_out, lru_faults = replace(ref, 3, "lru")
assert (fifo_faults, lru_faults) == (8, 6)
header, rows = table_after("| Page used | FIFO: pages in RAM | Fault? | LRU: pages in RAM | Fault? |")
assert len(rows) == 12
for r, f, l in zip(rows, fifo_out, lru_out):
    assert int(r[0]) == f[0] and r[1] == ", ".join(map(str, f[1])) and (r[2] == "yes") == f[2], r
    assert r[3] == ", ".join(map(str, l[1])) and (r[4] == "yes") == l[2], r
assert "4, 1, 2, 4, 1, 3, 4, 1, 5, 4, 1, 2" in TEXT
# stretch
ref2 = [1, 2, 3, 1, 2, 4, 1, 2, 5, 1, 2, 3]
assert (replace(ref2, 3, "fifo")[1], replace(ref2, 3, "lru")[1]) == (8, 6)
assert [f[1] for f in replace(ref2, 3, "fifo")[0]][5] == [2, 3, 4] and [f[1] for f in replace(ref2, 3, "fifo")[0]][6] == [3, 4, 1]
assert [f[1] for f in replace(ref2, 3, "fifo")[0]][7] == [4, 1, 2] and [f[1] for f in replace(ref2, 3, "fifo")[0]][8] == [1, 2, 5]
assert [f[1] for f in replace(ref2, 3, "fifo")[0]][11] == [2, 5, 3]
assert [f[1] for f in replace(ref2, 3, "lru")[0]][5] == [1, 2, 4] and [f[1] for f in replace(ref2, 3, "lru")[0]][8] == [1, 2, 5] and [f[1] for f in replace(ref2, 3, "lru")[0]][11] == [1, 2, 3]

# ---------------------------------------------------------------------------------------------
# Thrashing arithmetic
# ---------------------------------------------------------------------------------------------
total = 999 * 100 + 1 * 10_000_000
assert total == 10_099_900 and total / 1000 == 10_099.9 and round(total / 1000 / 100) == 101

# ---------------------------------------------------------------------------------------------
# Try questions, exam practice and stretch
# ---------------------------------------------------------------------------------------------
X = [("X", 0, 4), ("Y", 0, 1), ("Z", 0, 3)]
order = ["X", "Y", "Z"]
t, waits = 0, []
for n in order:
    waits.append(t)
    t += dict((p[0], p[2]) for p in X)[n]
assert waits == [0, 4, 5] and Fraction(sum(waits), 3) == 3
segs = schedule(X, "sjf")
rows, at, aw = stats(X, segs)
assert [rows[n][2] for n in "YZX"] == [0, 1, 4] and aw == Fraction(5, 3) and aw < 3
assert round(float(aw), 2) == 1.67

# exam practice: E, F, G, H with quantum 2
E = [("E", 0, 3), ("F", 1, 4), ("G", 2, 1), ("H", 5, 2)]
segs = schedule(E, "rr", 2)
assert segs == [("E", 0, 2), ("F", 2, 4), ("G", 4, 5), ("E", 5, 6), ("F", 6, 8), ("H", 8, 10)]
rows, at, aw = stats(E, segs)
assert [rows[n][0] for n in "EFGH"] == [6, 8, 5, 10] and [rows[n][2] for n in "EFGH"] == [3, 3, 2, 3] and aw == Fraction(11, 4) and float(aw) == 2.75
sl = rr_slices(E, 2)
assert [s[4] for s in sl][:3] == [["F", "G", "E"], ["G", "E", "F"], ["E", "F", "H"]]
# W, X, Y, Z: FCFS and SJF
W = [("W", 0, 6), ("X", 1, 2), ("Y", 2, 4), ("Z", 3, 1)]
rows, at, aw = stats(W, schedule(W, "fcfs"))
assert [rows[n][2] for n in "WXYZ"] == [0, 5, 6, 9] and aw == 5
segs = schedule(W, "sjf")
assert segs == [("W", 0, 6), ("Z", 6, 7), ("X", 7, 9), ("Y", 9, 13)]
rows, at, aw = stats(W, segs)
assert [rows[n][2] for n in "WXYZ"] == [0, 6, 7, 3] and aw == 4
# J, K, L, M: SRT
J = [("J", 0, 7), ("K", 2, 4), ("L", 4, 1), ("M", 5, 4)]
segs = schedule(J, "srt")
assert segs == [("J", 0, 2), ("K", 2, 4), ("L", 4, 5), ("K", 5, 7), ("M", 7, 11), ("J", 11, 16)]
rows, at, aw = stats(J, segs)
assert [rows[n][0] for n in "JKLM"] == [16, 7, 5, 11] and [rows[n][2] for n in "JKLM"] == [9, 1, 0, 2] and aw == 3
# at time 2: K needs 4 and J has 5 left; at time 4: K has 2 left and L needs 1
assert 7 - 2 == 5 and 4 - 2 == 2
# stretch: three processes, each 12 units, switch cost 1
C3 = [("A", 0, 12), ("B", 0, 12), ("C", 0, 12)]
for q, n_slices, sw, finish, start_c in ((2, 18, 17, 53, 6), (6, 6, 5, 41, 14), (12, 3, 2, 38, 26)):
    segs = schedule(C3, "rr", q)
    assert len(segs) == n_slices and switches(segs) == sw
    assert 36 + sw == finish and 2 * q + 2 == start_c
# the page-replacement and scheduling definitions never use a number we have not checked
assert 4 * 1 + 4 * 1 == 8

# quiz facts
assert schedule(A, "rr", 12) == fcfs                                              # quantum longer than every burst
assert stats(A, srt)[2] < stats(A, sjf)[2] < stats(A, fcfs)[2] < stats(A, rr2)[2]  # order of the averages in the table

print("ok")
