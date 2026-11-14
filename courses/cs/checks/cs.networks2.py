# checks/cs.networks2.py: runs every Python block in the chapter and recomputes every number it states
# (segments, header overhead, packet arrival times, reassembly, routing table, time to live, BitTorrent pieces).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.networks2"

# ---------------------------------------------------------------------------------------------
# Helper (copy unchanged into every checks file of this course; only CHAPTER_ID and INPUTS change)
# ---------------------------------------------------------------------------------------------
CHAPTER = pathlib.Path(__file__).resolve().parent.parent / "chapters" / f"{CHAPTER_ID}.md"
TEXT = CHAPTER.read_text(encoding="utf-8")
FENCES = list(re.finditer(r"^```(\w+)\n(.*?)^```", TEXT, re.S | re.M))


def run_python_blocks(inputs):
    """Run each ```python block in a fresh namespace inside a temporary folder.
    inputs: list of (text found in the block, [values the user types]). Typed values are echoed after
    the prompt, as a console shows them. If the next fence after a python block is ```output, the
    printed text must match it exactly (trailing spaces ignored)."""
    ran = 0
    with tempfile.TemporaryDirectory() as tmp:
        old = os.getcwd()
        os.chdir(tmp)
        try:
            for i, f in enumerate(FENCES):
                if f.group(1) != "python":
                    continue
                code = f.group(2)
                ran += 1
                typed = list(next((v for key, v in inputs if key in code), []))
                out = io.StringIO()

                def fake_input(prompt=""):
                    assert typed, f"python block {ran}: input() called but no typed value left"
                    value = typed.pop(0)
                    out.write(str(prompt) + value + "\n")
                    return value

                namespace = {"__name__": "__main__", "input": fake_input}
                with contextlib.redirect_stdout(out):
                    exec(compile(code, f"{CHAPTER_ID} python block {ran}", "exec"), namespace)
                assert not typed, f"python block {ran}: typed values not used: {typed}"
                nxt = FENCES[i + 1] if i + 1 < len(FENCES) else None
                if nxt is not None and nxt.group(1) == "output":
                    got = [line.rstrip() for line in out.getvalue().rstrip("\n").split("\n")]
                    want = [line.rstrip() for line in nxt.group(2).rstrip("\n").split("\n")]
                    assert got == want, f"python block {ran}: printed {got}, chapter shows {want}"
        finally:
            os.chdir(old)
    return ran




# ---------------------------------------------------------------------------------------------
# Every Python block runs and prints exactly what the chapter shows
# ---------------------------------------------------------------------------------------------
blocks = run_python_blocks([])
assert blocks == 3, blocks

# warm-up
assert 12000 // 8 == 1500

# segments and overhead (worked example and the Python block)
import math
size, mx, hdr = 5200, 1000, 40
n = math.ceil(size / mx)
assert n == 6 and size - 5 * mx == 200 and n * hdr == 240 and size + n * hdr == 5440 == 5 * 1040 + 240
assert 3500 // 1000 == 3 and math.ceil(3500 / 1000) == 4 and 3500 - 3000 == 500

# BitTorrent pieces
assert 2 ** 30 // 2 ** 18 == 2 ** 12 == 4096 and 1024 ** 3 // (256 * 1024) == 4096
assert 2 ** 21 // 2 ** 17 == 16 and 2 * 1024 ** 2 // (128 * 1024) == 16
swarm = {"S": {1, 2, 3, 4, 5, 6}, "P1": {1, 2, 3}, "P2": {3, 4}, "P3": {2, 5}}
need = sorted(set(range(1, 7)) - swarm["P2"])
assert need == [1, 2, 5, 6]
sources = {p: sorted(k for k, v in swarm.items() if k != "P2" and p in v) for p in need}
assert sources == {1: ["P1", "S"], 2: ["P1", "P3", "S"], 5: ["P3", "S"], 6: ["S"]}

# packet switching example: route times, arrival times, order, completion time
upper, lower = 5 + 12 + 10 + 5, 5 + 20 + 25 + 5
assert (upper, lower) == (32, 55)
sent = {1: 0, 2: 4, 3: 8, 4: 12}
route = {1: upper, 2: lower, 3: upper, 4: upper}
arrive = {p: sent[p] + route[p] for p in sent}
assert arrive == {1: 32, 2: 59, 3: 40, 4: 44}
assert sorted(arrive, key=arrive.get) == [1, 3, 4, 2] and max(arrive.values()) == 59

# the table of the worked example, parsed from the chapter
start = TEXT.index("| Packet | Sent at (ms) | Route | Route time (ms) | Arrives at (ms) |")
tab = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in TEXT[start:].split("\n\n")[0].split("\n")][2:]
assert [(int(r[0]), int(r[1]), r[2], int(r[3]), int(r[4])) for r in tab] == [
    (p, sent[p], "upper" if route[p] == upper else "lower", route[p], arrive[p]) for p in (1, 2, 3, 4)]

# time to live
assert 64 - 5 == 59
ttl, dead_at = 3, None
for router in range(1, 6):
    ttl -= 1
    if ttl == 0:
        dead_at = router
        break
assert dead_at == 3
ttl, dead_at = 5, None
for router in range(1, 7):
    ttl -= 1
    if ttl == 0:
        dead_at = router
        break
assert dead_at == 5

# routing table questions
import ipaddress
nets = ["203.0.113.0/24", "198.51.100.0/24"]
assert ipaddress.ip_address("198.51.100.9") in ipaddress.ip_network(nets[1])
assert ipaddress.ip_address("192.0.2.5") not in ipaddress.ip_network(nets[0]) and ipaddress.ip_address("192.0.2.5") not in ipaddress.ip_network(nets[1])
assert ipaddress.ip_address("203.0.113.77") in ipaddress.ip_network(nets[0])

# lost segments, worked example (cumulative acknowledgement: lowest missing segment)
def acks(arrivals):
    have, out = set(), []
    for s in arrivals:
        have.add(s)
        nxt = 1
        while nxt in have:
            nxt += 1
        out.append(nxt)
    return out


assert acks([1, 2, 4, 5]) == [2, 3, 3, 3] and acks([1, 2, 4, 5, 3])[-1] == 6
# stretch: segments 4 and 6 lost
assert acks([1, 2, 3, 5, 7, 8]) == [2, 3, 4, 4, 4, 4]
assert acks([1, 2, 3, 5, 7, 8, 4]) [-1] == 6 and acks([1, 2, 3, 5, 7, 8, 4, 6])[-1] == 9

# layer facts stated in the text
for word in ("Application", "Transport", "Internet", "Link"):
    assert word in TEXT
assert TEXT.count(":::def ") >= 20

print("ok")
