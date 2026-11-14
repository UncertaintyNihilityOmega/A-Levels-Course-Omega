# data/cs_kmap_model.py: exact Karnaugh-map solver used by checks/cs.boolean.py and the cs-kmap widget test.
# A minimal sum of products: the fewest product terms, then the fewest literals (prime implicants only).
# Run  py data/cs_kmap_model.py --dump  to print every 3-variable function and 2000 random 4-variable ones as JSON.
import itertools
import json
import random
import sys

GRAY2 = [0, 1, 3, 2]  # Gray code order of 2-bit numbers: 00, 01, 11, 10


def prime_implicants(nvars, ones):
    """Each implicant is (mask, value): mask bit = 1 means the variable is dropped (a dash)."""
    full = (1 << nvars) - 1
    cur = {(0, m) for m in ones}
    primes = set()
    while cur:
        nxt = set()
        used = set()
        items = sorted(cur)
        by_mask = {}
        for mask, val in items:
            by_mask.setdefault(mask, []).append(val)
        for mask, vals in by_mask.items():
            vs = set(vals)
            for v in vals:
                for bit in range(nvars):
                    b = 1 << bit
                    if mask & b or v & b:
                        continue
                    if (v | b) in vs:
                        nxt.add((mask | b, v))
                        used.add((mask, v))
                        used.add((mask, v | b))
        primes |= cur - used
        cur = nxt
    return sorted(primes)


def covers(imp, nvars):
    mask, val = imp
    return sorted(m for m in range(1 << nvars) if (m & ~mask) == val)


def literals(imp, nvars):
    return nvars - bin(imp[0]).count("1")


def solve(nvars, ones):
    ones = sorted(set(ones))
    if not ones:
        return []
    if len(ones) == 1 << nvars:
        return [((1 << nvars) - 1, 0)]
    pis = prime_implicants(nvars, ones)
    cov = [set(covers(p, nvars)) for p in pis]
    need = set(ones)
    for k in range(1, len(pis) + 1):
        best = None
        for combo in itertools.combinations(range(len(pis)), k):
            got = set().union(*(cov[i] for i in combo))
            if got >= need:
                lit = sum(literals(pis[i], nvars) for i in combo)
                key = (lit, combo)
                if best is None or key < best[0]:
                    best = (key, combo)
        if best:
            return [pis[i] for i in best[1]]
    raise AssertionError("no cover")


def cost(nvars, groups):
    return len(groups), sum(literals(g, nvars) for g in groups)


def term_text(imp, nvars, names="ABCD"):
    mask, val = imp
    parts = []
    for i in range(nvars):
        bit = 1 << (nvars - 1 - i)
        if mask & bit:
            continue
        parts.append(names[i] if val & bit else "NOT " + names[i])
    return " AND ".join(parts) if parts else "1"


def evaluate(groups, nvars, m):
    return any((m & ~mask) == val for mask, val in groups)


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--dump":
        out = []
        for f in range(256):
            ones = [m for m in range(8) if f >> m & 1]
            out.append([3, ones, list(cost(3, solve(3, ones)))])
        for f in range(16):
            ones = [m for m in range(4) if f >> m & 1]
            out.append([2, ones, list(cost(2, solve(2, ones)))])
        r = random.Random(11)
        for _ in range(2000):
            ones = [m for m in range(16) if r.random() < r.choice([0.2, 0.5, 0.8])]
            out.append([4, ones, list(cost(4, solve(4, ones)))])
        print(json.dumps(out))
    else:
        for ones in ([1, 3, 5, 7], [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]):
            n = 3 if max(ones) < 8 else 4
            print(ones, [term_text(g, n) for g in solve(n, ones)])
