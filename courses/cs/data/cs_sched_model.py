# data/cs_sched_model.py: the scheduling simulation used by checks/cs.os.py and by the cs-sched widget test.
# Rules (the same as the chapter and the widget state under the Gantt chart):
#  * a process is (name, arrival, burst); time is in whole units; only CPU bursts are modelled;
#  * ties are broken by earlier arrival, then by name;
#  * SRT: a new process pre-empts the running one only if its remaining time is strictly smaller;
#  * RR: a process that arrives while another runs (or exactly when a slice ends) joins the queue
#    before the pre-empted process; consecutive slices of the same process are shown as one bar;
#  * the CPU idles when nothing has arrived.
# Run  py data/cs_sched_model.py --dump N  to print N random cases as JSON (used by data/cs-sched.test.js).
import json
import random
import sys
from fractions import Fraction


def _merge(segs):
    out = []
    for name, s, e in segs:
        if out and out[-1][0] == name and out[-1][2] == s:
            out[-1] = (name, out[-1][1], e)
        else:
            out.append((name, s, e))
    return out


def schedule(procs, algo, q=2):
    """procs: list of (name, arrival, burst). Returns the Gantt segments [(name or None, start, end)]."""
    procs = [(n, int(a), int(b)) for n, a, b in procs]
    arr = {n: a for n, a, b in procs}
    rem = {n: b for n, a, b in procs}
    order = sorted(procs, key=lambda p: (p[1], p[0]))
    segs = []
    t = 0
    if algo == "fcfs":
        for n, a, b in order:
            if t < a:
                segs.append((None, t, a))
                t = a
            segs.append((n, t, t + b))
            t += b
    elif algo == "sjf":
        left = list(order)
        while left:
            ready = [p for p in left if p[1] <= t]
            if not ready:
                nxt = min(p[1] for p in left)
                segs.append((None, t, nxt))
                t = nxt
                continue
            n, a, b = min(ready, key=lambda p: (p[2], p[1], p[0]))
            segs.append((n, t, t + b))
            t += b
            left.remove((n, a, b))
    elif algo == "srt":
        current = None
        while any(v > 0 for v in rem.values()):
            ready = [n for n in rem if rem[n] > 0 and arr[n] <= t]
            if not ready:
                nxt = min(arr[n] for n in rem if rem[n] > 0)
                segs.append((None, t, nxt))
                t = nxt
                current = None
                continue
            n = min(ready, key=lambda x: (rem[x], 0 if x == current else 1, arr[x], x))
            segs.append((n, t, t + 1))
            rem[n] -= 1
            t += 1
            current = n if rem[n] > 0 else None
    elif algo == "rr":
        queue = []
        pending = list(order)

        def admit(upto):
            while pending and pending[0][1] <= upto:
                queue.append(pending.pop(0)[0])

        while pending or queue:
            admit(t)
            if not queue:
                nxt = pending[0][1]
                segs.append((None, t, nxt))
                t = nxt
                continue
            n = queue.pop(0)
            run = min(q, rem[n])
            segs.append((n, t, t + run))
            t += run
            rem[n] -= run
            admit(t)
            if rem[n] > 0:
                queue.append(n)
    else:
        raise ValueError(algo)
    return _merge(segs)


def stats(procs, segs):
    """Completion, turnaround and waiting time of each process, and the averages as Fractions."""
    done = {}
    for n, s, e in segs:
        if n is not None:
            done[n] = e
    rows = {}
    for n, a, b in procs:
        c = done[n]
        rows[n] = (c, c - a, c - a - b)
    k = len(procs)
    avg_t = Fraction(sum(r[1] for r in rows.values()), k)
    avg_w = Fraction(sum(r[2] for r in rows.values()), k)
    return rows, avg_t, avg_w


def switches(segs):
    """Number of times the CPU is handed from one process to a different one (idle gaps ignored)."""
    runs = [s[0] for s in segs if s[0] is not None]
    return sum(1 for a, b in zip(runs, runs[1:]) if a != b)


def cases(n, seed=7):
    r = random.Random(seed)
    out = []
    for _ in range(n):
        k = r.randint(1, 6)
        names = "ABCDEF"[:k]
        procs = [[nm, r.randint(0, 12), r.randint(1, 9)] for nm in names]
        algo = r.choice(["fcfs", "sjf", "srt", "rr"])
        q = r.randint(1, 5)
        segs = schedule(procs, algo, q)
        rows, at, aw = stats(procs, segs)
        out.append({"procs": procs, "algo": algo, "q": q,
                    "segs": [[a, b, c] for a, b, c in segs],
                    "rows": {n: list(v) for n, v in rows.items()},
                    "avgT": [at.numerator, at.denominator], "avgW": [aw.numerator, aw.denominator]})
    return out


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--dump":
        print(json.dumps(cases(int(sys.argv[2]))))
    else:
        P = [("A", 0, 5), ("B", 1, 3), ("C", 2, 8), ("D", 3, 2)]
        for algo in ("fcfs", "sjf", "srt", "rr"):
            s = schedule(P, algo, 2)
            r, at, aw = stats(P, s)
            print(algo, s, r, at, aw, switches(s))
