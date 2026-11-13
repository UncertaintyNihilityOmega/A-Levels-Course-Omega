# data/cs.asmsim.py: a small simulator of the Cambridge example instruction set (FACTS.md "Assembly language").
# The text between the two marker lines is copied unchanged into checks/cs.processor.py and checks/cs.assembly.py,
# and data/cs-asm.test.js runs it against widgets/cs-asm.js.
# --- begin asm simulator ---
import re


class AsmError(Exception):
    pass


NOARG = {"IN", "OUT", "END"}
REGARG = {"INC", "DEC", "MOV"}
IMMONLY = {"LDM", "LDR", "LSL", "LSR"}
ADDRONLY = {"LDD", "LDI", "LDX", "STO", "JMP", "CMI", "JPE", "JPN"}
BOTH = {"ADD", "SUB", "CMP", "AND", "OR", "XOR"}
OPS = NOARG | REGARG | IMMONLY | ADDRONLY | BOTH


def value_of(tok, bits=8):
    """#n denary, Bn binary, &n hex, or a bare denary number."""
    t = tok.strip()
    m = re.fullmatch(r"#?(-?\d+)", t)
    if m:
        v = int(m.group(1))
    elif re.fullmatch(r"B[01]+", t):
        v = int(t[1:], 2)
    elif re.fullmatch(r"&[0-9A-F]+", t):
        v = int(t[1:], 16)
    else:
        raise AsmError(f"cannot read the number {tok!r}")
    if v < 0:
        v += 2 ** bits
    if not 0 <= v < 2 ** bits:
        raise AsmError(f"{tok} does not fit in {bits} bits")
    return v


def is_imm(tok):
    return tok.startswith("#") or re.fullmatch(r"B[01]+", tok) is not None or re.fullmatch(r"&[0-9A-F]+", tok) is not None


def assemble(text, start=100, bits=8):
    """Pass 1 builds the symbol table, pass 2 resolves operands.
    Returns (mem, labels, first): mem[addr] = ('I', op, kind, value, source) or ('D', value, source)."""
    items, labels, loc = [], {}, start
    for n, raw in enumerate(text.split("\n"), 1):
        line = raw.split("//")[0].strip()
        if not line:
            continue
        m = re.match(r"(\d+)\s+(\S.*)$", line)
        if m:
            loc, line = int(m.group(1)), m.group(2)
        m = re.match(r"([A-Za-z_]\w*)\s*:\s*(.*)$", line)
        label = None
        if m:
            label, line = m.group(1), m.group(2).strip()
            if label.upper() in OPS:
                raise AsmError(f"line {n}: {label} is an instruction name, not a label")
            if label in labels:
                raise AsmError(f"line {n}: the label {label} is used twice")
            labels[label] = loc
        if not line:
            raise AsmError(f"line {n}: nothing after the label")
        if any(a == loc for a, *_ in items):
            raise AsmError(f"line {n}: address {loc} is already used")
        items.append((loc, n, line))
        loc += 1
    mem, first = {}, None
    for loc, n, line in items:
        parts = line.split()
        op = parts[0].upper()
        if op in OPS:
            arg = parts[1] if len(parts) > 1 else None
            if len(parts) > 2:
                raise AsmError(f"line {n}: too many items after {op}")
            if op in NOARG:
                if arg is not None:
                    raise AsmError(f"line {n}: {op} takes no operand")
                kind, val = "none", None
            elif arg is None:
                raise AsmError(f"line {n}: {op} needs an operand")
            elif op in REGARG:
                allowed = ("IX",) if op == "MOV" else ("ACC", "IX")
                if arg.upper() not in allowed:
                    raise AsmError(f"line {n}: {op} needs {' or '.join(allowed)}")
                kind, val = "reg", arg.upper()
            else:
                if op in IMMONLY or (op in BOTH and is_imm(arg)):
                    if not is_imm(arg):
                        raise AsmError(f"line {n}: {op} needs a number such as #5, B101 or &1F")
                    kind, val = "imm", value_of(arg, bits)
                else:
                    if re.fullmatch(r"\d+", arg):
                        kind, val = "addr", int(arg)
                    elif re.fullmatch(r"[A-Za-z_]\w*", arg):
                        if arg not in labels:
                            raise AsmError(f"line {n}: the label {arg} is never defined")
                        kind, val = "addr", labels[arg]
                    else:
                        raise AsmError(f"line {n}: {arg!r} is not an address or a label")
            mem[loc] = ("I", op, kind, val, line)
            if first is None:
                first = loc
        else:
            if len(parts) != 1:
                raise AsmError(f"line {n}: {parts[0]!r} is not an instruction")
            mem[loc] = ("D", value_of(parts[0], bits), line)
    if first is None:
        raise AsmError("the program has no instructions")
    return mem, labels, first


def run(text, inputs="", start=100, bits=8, max_steps=1000):
    """Run to END. Returns (steps, final); each step is a dict: addr, text (the source line), acc/ix (new value
    or None), mem {addr: value}, cmp (True/False or None), out (char or None) and micro: the fetch-execute
    register transfers as a list of (text, {register: new value}); a write to memory has the key 'mem'."""
    mem, labels, pc = assemble(text, start, bits)
    data = {a: v[1] for a, v in mem.items() if v[0] == "D"}
    top = 2 ** bits
    acc = ix = 0
    flag = None
    buf = list(inputs)
    steps = []

    def rd(a):
        if a in mem and mem[a][0] == "I":
            raise AsmError(f"address {a} holds an instruction, not data")
        return data.get(a, 0)

    while True:
        if len(steps) >= max_steps:
            raise AsmError("step limit reached: the program may never reach END")
        if pc not in mem or mem[pc][0] != "I":
            raise AsmError(f"address {pc} does not hold an instruction")
        _, op, kind, val, src = mem[pc]
        ins = re.sub(r"^\w+\s*:\s*", "", src)
        st = {"addr": pc, "text": src, "acc": None, "ix": None, "mem": {}, "cmp": None, "out": None}
        mi = [("MAR ← [PC]", {"MAR": pc}), ("PC ← [PC] + 1", {"PC": pc + 1}),
              ("MDR ← [[MAR]]", {"MDR": ins}), ("CIR ← [MDR]", {"CIR": ins})]
        nxt = pc + 1
        oacc, oix = acc, ix
        if op == "END":
            mi.append(("stop the program", {}))
            st["micro"] = mi
            steps.append(st)
            break
        if op == "LDM":
            acc = val; st["acc"] = acc
            mi.append((f"ACC ← {val}", {"ACC": acc}))
        elif op == "LDD":
            acc = rd(val); st["acc"] = acc
            mi += [(f"MAR ← {val}", {"MAR": val}), ("MDR ← [[MAR]]", {"MDR": acc}), ("ACC ← [MDR]", {"ACC": acc})]
        elif op == "LDI":
            p2 = rd(val); acc = rd(p2); st["acc"] = acc
            mi += [(f"MAR ← {val}", {"MAR": val}), ("MDR ← [[MAR]]", {"MDR": p2}), ("MAR ← [MDR]", {"MAR": p2}),
                   ("MDR ← [[MAR]]", {"MDR": acc}), ("ACC ← [MDR]", {"ACC": acc})]
        elif op == "LDX":
            ea = val + ix; acc = rd(ea); st["acc"] = acc
            mi += [(f"MAR ← {val} + [IX]", {"MAR": ea}), ("MDR ← [[MAR]]", {"MDR": acc}), ("ACC ← [MDR]", {"ACC": acc})]
        elif op == "LDR":
            ix = val; st["ix"] = ix
            mi.append((f"IX ← {val}", {"IX": ix}))
        elif op == "MOV":
            ix = acc; st["ix"] = ix
            mi.append(("IX ← [ACC]", {"IX": ix}))
        elif op == "STO":
            data[val] = acc; st["mem"][val] = acc
            mi += [(f"MAR ← {val}", {"MAR": val}), ("MDR ← [ACC]", {"MDR": acc}), ("[[MAR]] ← [MDR]", {"mem": {val: acc}})]
        elif op in ("ADD", "SUB", "AND", "OR", "XOR"):
            sym = {"ADD": "+", "SUB": "-", "AND": "AND", "OR": "OR", "XOR": "XOR"}[op]
            if kind == "imm":
                b = val
                mi.append((f"ACC ← [ACC] {sym} {val}", {}))
            else:
                b = rd(val)
                mi += [(f"MAR ← {val}", {"MAR": val}), ("MDR ← [[MAR]]", {"MDR": b}), (f"ACC ← [ACC] {sym} [MDR]", {})]
            acc = {"ADD": acc + b, "SUB": acc - b, "AND": acc & b, "OR": acc | b, "XOR": acc ^ b}[op] % top
            st["acc"] = acc
            mi[-1][1]["ACC"] = acc
        elif op in ("INC", "DEC"):
            d = 1 if op == "INC" else -1
            if val == "ACC":
                acc = (acc + d) % top; st["acc"] = acc
            else:
                ix = (ix + d) % top; st["ix"] = ix
            mi.append((f"{val} ← [{val}] {'+' if d == 1 else '-'} 1", {val: acc if val == "ACC" else ix}))
        elif op in ("LSL", "LSR"):
            acc = ((acc << val) % top) if op == "LSL" else acc >> val; st["acc"] = acc
            mi.append((f"ACC ← [ACC] shifted {'left' if op == 'LSL' else 'right'} {val} place{'s' if val != 1 else ''}", {"ACC": acc}))
        elif op == "JMP":
            nxt = val
            mi.append((f"PC ← {val}", {"PC": val}))
        elif op in ("CMP", "CMI"):
            if kind == "imm":
                b = val
                mi.append((f"compare [ACC] with {val}", {}))
            elif op == "CMP":
                b = rd(val)
                mi += [(f"MAR ← {val}", {"MAR": val}), ("MDR ← [[MAR]]", {"MDR": b}), ("compare [ACC] with [MDR]", {})]
            else:
                p2 = rd(val); b = rd(p2)
                mi += [(f"MAR ← {val}", {"MAR": val}), ("MDR ← [[MAR]]", {"MDR": p2}), ("MAR ← [MDR]", {"MAR": p2}),
                       ("MDR ← [[MAR]]", {"MDR": b}), ("compare [ACC] with [MDR]", {})]
            flag = acc == b; st["cmp"] = flag
            mi[-1] = (mi[-1][0] + f"; status ← {'TRUE' if flag else 'FALSE'}", {"SR": "TRUE" if flag else "FALSE"})
        elif op in ("JPE", "JPN"):
            if flag is None:
                raise AsmError(f"address {pc}: {op} before any compare")
            go = flag == (op == "JPE")
            mi.append((f"test the status register: {'TRUE' if flag else 'FALSE'}", {}))
            if go:
                nxt = val
                mi.append((f"PC ← {val}", {"PC": val}))
            else:
                mi.append(("no jump: PC is unchanged", {}))
        elif op == "IN":
            if not buf:
                raise AsmError("IN: the keyboard buffer is empty")
            acc = ord(buf.pop(0)); st["acc"] = acc
            mi.append((f"ACC ← ASCII code of the key pressed ({acc})", {"ACC": acc}))
        elif op == "OUT":
            st["out"] = chr(acc)
            mi.append((f"output the character whose code is [ACC] ({acc})", {}))
        st["micro"] = mi
        steps.append(st)
        pc = nxt
    return steps, {"acc": acc, "ix": ix, "mem": dict(data), "labels": labels,
                   "out": "".join(s["out"] for s in steps if s["out"] is not None)}


def trace(text, watch=(), cols=("ACC", "IX"), inputs="", start=100, bits=8, start_row=False, show_cmp=False, address=True, binary=False):
    """A Markdown-style trace table as (header, rows) of strings. watch: labels or addresses to give a column.
    A cell is filled when the instruction writes that register or location (even with the same value)."""
    steps, fin = run(text, inputs, start, bits)
    mem, labels, _ = assemble(text, start, bits)
    fv = (lambda v: format(v, f"0{bits}b")) if binary else str
    addr_of = lambda w: labels[w] if w in labels else int(w)
    header = (["Address"] if address else []) + ["Instruction"] + list(cols) + [f"[{w}]" if w in labels else str(w) for w in watch]
    header += (["Compare"] if show_cmp else []) + ["OUTPUT"]
    rows = []
    if start_row:
        r = (["start"] if address else []) + [""] + [""] * len(cols)
        r += [fv(mem[addr_of(w)][1]) if addr_of(w) in mem and mem[addr_of(w)][0] == "D" else "" for w in watch]
        r += ([""] if show_cmp else []) + [""]
        rows.append(r)
    for s in steps:
        r = ([str(s["addr"])] if address else []) + [re.sub(r"^\w+\s*:\s*", "", s["text"])]
        r += [fv(s["acc"]) if (c == "ACC" and s["acc"] is not None) else (str(s["ix"]) if (c == "IX" and s["ix"] is not None) else "") for c in cols]
        r += [fv(s["mem"][addr_of(w)]) if addr_of(w) in s["mem"] else "" for w in watch]
        r += ([("TRUE" if s["cmp"] else "FALSE") if s["cmp"] is not None else ""] if show_cmp else [])
        r += [s["out"] if s["out"] is not None else ""]
        rows.append(r)
    return header, rows
# --- end asm simulator ---
