# data/cs.prolog_sim.py: a tiny Prolog-style engine used by checks/cs.paradigms.py to recompute every goal result.
# Facts and rules are read in the Cambridge form (IF, AND) or the SWISH form (:-, comma). Supports atoms, variables,
# compound terms, numbers, the tests  \=  >  <  >=  <=  =  and NOT goal (negation as failure, as in the 9618/31
# and 9618/32 June 2024 mark schemes). Depth-first, top to bottom, left to right: answers come
# in the same order as a real Prolog system.
import re
import itertools

_counter = itertools.count()


class Var:
    def __init__(self, name):
        self.name = name


def split_top(text, sep=","):
    parts, depth, cur = [], 0, ""
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def parse_term(s, env):
    s = s.strip()
    m = re.fullmatch(r"([a-z]\w*)\((.*)\)", s, re.S)
    if m:
        return (m.group(1),) + tuple(parse_term(a, env) for a in split_top(m.group(2)))
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        return float(s) if "." in s else int(s)
    if re.fullmatch(r"[A-Z_]\w*", s):
        if s == "_":
            return Var("_" + str(next(_counter)))
        return env.setdefault(s, Var(s))
    if re.fullmatch(r"[a-z]\w*", s):
        return s
    raise ValueError("cannot parse term: " + repr(s))


TESTS = ["\\=", ">=", "<=", ">", "<", "="]


def parse_goal(s, env):
    s = s.strip()
    if s.startswith("NOT ") or s.startswith("NOT("):  # negation as failure, the Cambridge form NOT goal
        inner = s[3:].strip()
        if inner.startswith("(") and inner.endswith(")"):
            inner = inner[1:-1]
        return ("$not", parse_goal(inner, env), None)
    for t in TESTS:
        if t in s and "(" not in s.split(t)[0]:
            left, right = s.split(t, 1)
            return ("$" + t, parse_term(left, env), parse_term(right, env))
    return parse_term(s, env)


def normalise(text):
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\bIF\b", ":-", text)
    text = re.sub(r"\bAND\b", ",", text)
    return text


def parse_program(text):
    clauses = []
    for stmt in re.split(r"\.(?=\s|$)", normalise(text)):
        stmt = " ".join(stmt.split())
        if not stmt:
            continue
        head, _, body = stmt.partition(":-")
        env = {}
        h = parse_term(head, env)
        goals = [parse_goal(g, env) for g in split_top(body)] if body.strip() else []
        clauses.append((h, goals))
    return clauses


def walk(t, b):
    while isinstance(t, Var) and t in b:
        t = b[t]
    return t


def unify(x, y, b):
    x, y = walk(x, b), walk(y, b)
    if x is y or (not isinstance(x, Var) and not isinstance(y, Var) and x == y and not isinstance(x, tuple)):
        return b
    if isinstance(x, Var):
        nb = dict(b)
        nb[x] = y
        return nb
    if isinstance(y, Var):
        nb = dict(b)
        nb[y] = x
        return nb
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y) and x[0] == y[0]:
        for p, q in zip(x[1:], y[1:]):
            b = unify(p, q, b)
            if b is None:
                return None
        return b
    return None


def rename(t, m):
    if isinstance(t, Var):
        return m.setdefault(t, Var(t.name))
    if isinstance(t, tuple):
        return (t[0],) + tuple(rename(a, m) for a in t[1:])
    return t


def solve(goals, b, prog):
    if not goals:
        yield b
        return
    g, rest = goals[0], goals[1:]
    if g[0] == "$not":
        if next(solve([g[1]], b, prog), None) is None:
            yield from solve(rest, b, prog)
        return
    if g[0].startswith("$"):
        x, y = walk(g[1], b), walk(g[2], b)
        op = g[0][1:]
        if op == "=":
            nb = unify(x, y, b)
            if nb is not None:
                yield from solve(rest, nb, prog)
            return
        assert not isinstance(x, Var) and not isinstance(y, Var), "comparison with an unbound variable"
        ok = {"\\=": x != y, ">=": x >= y, "<=": x <= y, ">": x > y, "<": x < y}[op]
        if ok:
            yield from solve(rest, b, prog)
        return
    for head, body in prog:
        m = {}
        h = rename(head, m)
        nb = unify(g, h, b)
        if nb is None:
            continue
        yield from solve([rename(x, m) for x in body] + rest, nb, prog)


def resolve(t, b):
    t = walk(t, b)
    if isinstance(t, tuple):
        return t[0] + "(" + ", ".join(str(resolve(a, b)) for a in t[1:]) + ")"
    return t


def query(prog_text, goal_text):
    """Return the list of answers, in order. A goal with no variables gives [{}] (true) or [] (false);
    otherwise each answer is a dict {variable name: value}."""
    prog = prog_text if isinstance(prog_text, list) else parse_program(prog_text)
    env = {}
    goals = [parse_goal(g, env) for g in split_top(normalise(goal_text).strip().rstrip("."))]
    out = []
    for b in solve(goals, {}, prog):
        out.append({n: resolve(v, b) for n, v in env.items() if not n.startswith("_")})
    return out
