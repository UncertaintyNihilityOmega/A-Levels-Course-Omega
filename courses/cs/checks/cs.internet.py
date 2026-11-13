# checks/cs.internet.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every number the chapter states (streams, addresses, masks, subnets, DNS).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.internet"

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


PAIRS = [("IF", "ENDIF"), ("WHILE", "ENDWHILE"), ("FOR", "NEXT"), ("REPEAT", "UNTIL"),
         ("CASE OF", "ENDCASE"), ("PROCEDURE", "ENDPROCEDURE"), ("FUNCTION", "ENDFUNCTION"),
         ("CLASS", "ENDCLASS")]


def lint_pseudocode_blocks():
    """Light checks on ```pseudocode blocks: Cambridge symbols, no Python syntax, balanced
    structures (blocks that are deliberate fragments contain a line '...' and skip the balance test)."""
    n = 0
    for f in FENCES:
        if f.group(1) != "pseudocode":
            continue
        n += 1
        code = f.group(2)
        lines = [re.sub(r"^\s*\d+\s{2,}", "", ln).split("//")[0] for ln in code.split("\n")]
        body = "\n".join(lines)
        for bad in ("<-", "==", "!=", "print(", "elif", "range(", "True", "False", "\t"):
            assert bad not in body, f"pseudocode block {n}: contains {bad!r}"
        if any(ln.strip() == "..." for ln in lines):
            continue
        words = [ln.strip() for ln in lines]
        for start, end in PAIRS:
            if start == "FOR":
                opened = sum(1 for w in words if re.match(r"FOR \w+ ←", w))
            elif start == "CASE OF":
                opened = sum(1 for w in words if w.startswith("CASE OF"))
            elif start in ("PROCEDURE", "FUNCTION"):
                opened = sum(1 for w in words if re.match(rf"(PUBLIC |PRIVATE )?{start} ", w))
            else:
                opened = sum(1 for w in words if re.match(rf"{start}\b", w))
            closed = sum(1 for w in words if re.match(rf"{end}\b", w))
            # a block of four lines or fewer may be a fragment (for example a corrected swap)
            assert opened == closed or len(words) <= 4, f"pseudocode block {n}: {start}/{end} {opened}/{closed}"
        types = sum(1 for w in words if re.match(r"TYPE \w+\s*$", w))
        assert types == sum(1 for w in words if w.startswith("ENDTYPE")), f"pseudocode block {n}: TYPE/ENDTYPE"
    return n


import ipaddress

blocks = run_python_blocks([])
assert blocks == 7, f"expected 7 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 1

# Warm-up
assert int("11000000", 2) == 192 and 2 ** 8 == 256

# Streaming calculations
assert 5 * 10 ** 6 * 600 == 3 * 10 ** 9 and 3 * 10 ** 9 / 8 == 375 * 10 ** 6
assert 4 * 10 ** 6 * 30 == 120_000_000
assert 600 * 8 / 8 == 600                      # 600 MB at 8 Mbps
assert 10 / 8 == 1.25                           # 10 Mbps is 1.25 MB per second
assert 4 * 10 ** 6 * 1800 == 7.2 * 10 ** 9 and 7.2 * 10 ** 9 / 8 == 900 * 10 ** 6
assert 2.5 > 2 and 4 > 3                        # stream faster than connection

# Stretch 2: wait before playing a 10-minute 5 Mbps film over a 3 Mbps connection
film_s, rate, link = 600, 5, 3
wait = max(max(0, (rate - link) * t / link) for t in range(0, film_s + 1))
assert wait == 400 and film_s * rate / link == 1000 and 1000 - film_s == 400
# simulate: with a 400 s wait the data never runs out, with 399 s it does
def never_runs_out(w):
    return all(link * (w + t) >= rate * t for t in range(0, film_s + 1))
assert never_runs_out(400) and not never_runs_out(399)

# IPv4 and IPv6 facts
assert 2 ** 32 == 4294967296 and 2 ** 128 == 340282366920938463463374607431768211456
assert abs(2 ** 128 / 1e38 - 3.4) < 0.05
assert bin(192)[2:] == "11000000" and format(168, "08b") == "10101000" and format(20, "08b") == "00010100"
v6 = ipaddress.ip_address("2001:0db8:0000:0000:0000:ff00:0042:8329")
assert v6.compressed == "2001:db8::ff00:42:8329" and 8 - 5 == 3
assert ipaddress.ip_address("2001:0db8:0000:0042:0000:0000:0000:0001").compressed == "2001:db8:0:42::1"
assert ipaddress.ip_address("fe80:0000:0000:0000:0202:b3ff:fe1e:8329").compressed == "fe80::202:b3ff:fe1e:8329"

def valid4(text):
    try:
        ipaddress.IPv4Address(text)
        return True
    except ValueError:
        return False

assert valid4("172.16.254.3") and not valid4("192.168.1.256") and not valid4("10.0.5") and not valid4("10.256.4.1")
assert valid4("192.168.0.1") and not valid4("172.16.5") and valid4("255.255.255.0") and not valid4("300.1.1.1")
for bad in ("fe80::1::2", "2001:db8::8a2e::7334"):
    try:
        ipaddress.IPv6Address(bad)
        raise AssertionError(bad)
    except ValueError:
        pass
assert not valid4("192.168.1") and not valid4("192.168.1.1.1")

# Subnet arithmetic
def info(cidr):
    n = ipaddress.ip_interface(cidr)
    net = n.network
    return str(net.network_address), str(net.broadcast_address), net.num_addresses - 2, str(net.netmask)

assert info("172.16.37.200/20") == ("172.16.32.0", "172.16.47.255", 4094, "255.255.240.0")
assert 37 & 240 == 32 and format(37, "08b") == "00100101" and 32 + 15 == 47 and 2 ** 12 - 2 == 4094
assert 8 + 8 + 4 == 20 and 32 - 20 == 12
assert info("192.168.40.150/27") == ("192.168.40.128", "192.168.40.159", 30, "255.255.255.224")
assert 150 & 224 == 128 and 8 + 8 + 8 + 3 == 27 and 2 ** 5 - 2 == 30
assert info("10.1.150.20/18")[0] == "10.1.128.0"
assert info("192.168.5.37/24")[0] == "192.168.5.0"
assert 130 & 192 == 128 and 70 & 192 == 64 and format(130, "08b") == "10000010" and format(70, "08b") == "01000110"
assert ipaddress.ip_network("192.168.1.0/24").num_addresses - 2 == 254 and 4 * 62 == 248
assert [str(s) for s in ipaddress.ip_network("192.168.1.0/24").subnets(new_prefix=26)] == [
    "192.168.1.0/26", "192.168.1.64/26", "192.168.1.128/26", "192.168.1.192/26"]
assert [info(f"192.168.5.{n}/26")[2] for n in (0, 64, 128, 192)] == [62] * 4 and 2 ** 5 - 2 == 30 < 50 <= 62
assert 62 - 50 == 12
assert [2 ** (32 - p) - 2 for p in (24, 26, 28, 30)] == [254, 62, 14, 2]
assert 2 ** 24 == 16777216 and 2 ** 20 == 1048576 and 2 ** 16 == 65536
assert 2 ** 5 - 2 == 30

# Private ranges
def private_block(a):
    ip = ipaddress.ip_address(a)
    return any(ip in ipaddress.ip_network(b) for b in ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"))

assert private_block("172.20.14.9") and private_block("192.168.100.4") and private_block("10.0.0.5")
assert not private_block("172.32.0.5") and not private_block("172.32.0.1") and not private_block("11.0.0.1") and not private_block("8.8.8.8")
assert ipaddress.ip_network("172.16.0.0/12")[-1] == ipaddress.ip_address("172.31.255.255")

# Pseudocode validity check translated
def pseudo_valid(octets):
    valid = True
    for o in octets:
        if o < 0 or o > 255:
            valid = False
    return valid

assert pseudo_valid([192, 168, 1, 20]) and not pseudo_valid([192, 168, 1, 256])

print("ok")
