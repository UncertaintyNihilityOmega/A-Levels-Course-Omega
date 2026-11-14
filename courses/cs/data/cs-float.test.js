// data/cs-float.test.js: checks the logic of widgets/cs-float.js against Python Fractions (data/cs_float_model.py).
// Run: node data/cs-float.test.js
const { execFileSync } = require('child_process');
const path = require('path');
const L = require(path.join(__dirname, '..', 'widgets', 'cs-float.js'));

const py = `
import json, random, sys
sys.path.insert(0, ${JSON.stringify(__dirname)})
from cs_float_model import *
from fractions import Fraction as F
from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 120
getcontext().rounding = ROUND_HALF_UP
random.seed(20261114)

def fs(f):
    f = F(f)
    s = str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"
    return s.replace("-", "\\u2212")

def exact_dec(f):
    f = F(f)
    d = f.denominator
    k = 0
    while d % 2 == 0 and d > 1:
        d //= 2
        k += 1
    if d != 1 or k > 40:
        return None
    s = format(Decimal(f.numerator) / Decimal(f.denominator), "f")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    if len(s.replace("-", "").replace(".", "")) > 30 and f.denominator == 1:
        return None
    return s.replace("-", "\\u2212")

def sci(f, sig=6):
    f = F(f)
    if f == 0:
        return "0"
    x = Decimal(abs(f.numerator)) / Decimal(f.denominator)
    t = format(x, "." + str(sig - 1) + "e")          # d.dddde+X
    mant, ex = t.split("e")
    if "." in mant:
        mant = mant.rstrip("0").rstrip(".")
    ex = int(ex)
    sup = "\\u2070\\u00b9\\u00b2\\u00b3\\u2074\\u2075\\u2076\\u2077\\u2078\\u2079"
    s = "".join(sup[int(c)] for c in str(abs(ex)))
    return ("\\u2212" if f < 0 else "") + mant + " \\u00d7 10" + ("\\u2212" if ex < 0 else "") + s

out = {"patterns": [], "encode": [], "reformat": []}
formats = [(6, 3), (8, 4), (7, 5), (10, 6), (16, 8), (6, 8), (16, 3), (9, 3), (12, 4)]
for m, e in formats:
    pats = ["0" * m, "1" * m, "1" + "0" * (m - 1), "0" + "1" * (m - 1), "01" + "0" * (m - 2), "10" + "1" * (m - 2)]
    pats += [format(random.getrandbits(m), "0%db" % m) for _ in range(25)]
    exps = ["0" * e, "1" * e, "1" + "0" * (e - 1), "0" + "1" * (e - 1)] + [format(random.getrandbits(e), "0%db" % e) for _ in range(6)]
    for mb in pats:
        for eb in random.sample(exps, 3):
            v = value(mb, eb)
            path = []
            mm, ee = mb, eb
            blocked = False
            if "1" in mm or True:
                e_val = twos(eb)
                emin = -(1 << (len(eb) - 1))
                cur_m, cur_e = mb, e_val
                while not is_normalised(cur_m) and "1" in cur_m:
                    if cur_e - 1 < emin:
                        blocked = True
                        break
                    cur_m, cur_e = cur_m[1:] + "0", cur_e - 1
                    path.append(1)
            if mb == "0" * m:
                cur_m, cur_e = mb, twos(eb)
            ef = format(cur_e & ((1 << len(eb)) - 1), "0%db" % len(eb))
            out["patterns"].append({"m": mb, "e": eb, "value": fs(v), "mant": fs(mantissa_value(mb)), "exp": twos(eb),
                                    "norm": is_normalised(mb), "zero": mb == "0" * m, "steps": len(path), "blocked": blocked,
                                    "finalM": cur_m, "finalE": ef, "exact": exact_dec(v),
                                    "sci": sci(v), "limits": None})
    lim = limits(m, e)
    out.setdefault("limits", []).append({"m": m, "e": e, "largest": fs(lim["largest"]), "smallest": fs(lim["smallest"]),
                                          "neg": fs(lim["most_negative"])})
typed = ["0.1", "-0.1", "6.25", "-3.5", "-4", "300", "-300", "0.001", "-0.001", "127", "128", "-128", "-129", "1/3", "-2/3",
         "0", "0.0", "+5", ".5", "5.", "22.5", "-5.25", "1000000", "0.00000001", "-0.5", "0.5", "1", "-1", "-0.75", "3.14159"]
for m, e in formats:
    vals = list(typed)
    for _ in range(25):
        p = random.randint(1, 10 ** random.randint(1, 9))
        q = random.randint(1, 10 ** random.randint(0, 6))
        vals.append(("-" if random.random() < 0.5 else "") + str(p) + "/" + str(q))
    for t in vals:
        if t.startswith("+") or t.startswith("-"):
            sign, body = (-1 if t[0] == "-" else 1), t[1:]
        else:
            sign, body = 1, t
        if "/" in body:
            a, b = body.split("/")
            x = F(int(a), int(b)) * sign
        else:
            if body.endswith("."):
                body = body[:-1]
            x = F(Decimal(body or "0")) * sign
        mb, eb, status = encode(x, m, e)
        out["encode"].append({"m": m, "e": e, "text": t, "status": "ok" if status == "ok" else status,
                              "mbits": mb, "ebits": eb, "x": fs(x)})
for m, e in formats:
    for m2, e2 in [(6, 3), (8, 4), (9, 3), (7, 5), (16, 8), (10, 6), (12, 4)]:
        for t in ["5.5", "-0.15625", "100", "-100", "0.1", "0", "-4", "0.001"]:
            x = F(Decimal(t))
            mb, eb, st = encode(x, m, e)
            if st == "overflow":
                continue
            v = value(mb, eb)
            a, b, st2 = encode(v, m2, e2)
            out["reformat"].append({"m": mb, "e": eb, "m2": m2, "e2": e2, "status": st2, "mbits": a, "ebits": b})
print(json.dumps(out))
`;
const data = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 }));
let checks = 0;
function eq(label, got, want) {
  checks++;
  if (got !== want) { console.error('FAIL ' + label + ': got ' + JSON.stringify(got) + ', want ' + JSON.stringify(want)); process.exit(1); }
}

// pattern values, mantissas, exponents, normalised flags, decimals, normalise paths
data.patterns.forEach(function (p) {
  const v = L.value(p.m, p.e);
  eq('value ' + p.m + ' ' + p.e, L.fracStr(v), p.value);
  eq('mantissa ' + p.m, L.fracStr(L.mantissa(p.m)), p.mant);
  eq('exp ' + p.e, L.exp(p.e), p.exp);
  eq('norm ' + p.m, L.isNormalised(p.m), p.norm);
  eq('zero ' + p.m, L.isZero(p.m), p.zero);
  const dec = L.exactDec(v);
  eq('exactDec ' + p.value, dec, p.exact);
  eq('sci ' + p.value, L.sciStr(v, 6), p.sci);
  // follow Normalise to the end
  let m = p.m, e = p.e, steps = 0, blocked = false;
  for (let i = 0; i < 40; i++) {
    const r = L.normaliseStep(m, e);
    if (r.kind === 'step') { m = r.m; e = r.e; steps++; continue; }
    if (r.kind === 'blocked') blocked = true;
    break;
  }
  eq('norm steps ' + p.m + ' ' + p.e, steps, p.steps);
  eq('norm blocked ' + p.m + ' ' + p.e, blocked, p.blocked);
  eq('norm final m ' + p.m + ' ' + p.e, m, p.finalM);
  eq('norm final e ' + p.m + ' ' + p.e, e, p.finalE);
  if (!blocked) {
    const v2 = L.value(m, e);
    eq('norm keeps value', L.fracStr(v2), p.value);
  }
});

data.limits.forEach(function (r) {
  const lim = L.limits(r.m, r.e);
  eq('largest ' + r.m + '+' + r.e, L.fracStr(lim.largest.value), r.largest);
  eq('smallest ' + r.m + '+' + r.e, L.fracStr(lim.smallest.value), r.smallest);
  eq('most negative ' + r.m + '+' + r.e, L.fracStr(lim.mostNegative.value), r.neg);
  eq('smallest normalised', L.isNormalised(lim.smallest.m), true);
  eq('most negative normalised', L.isNormalised(lim.mostNegative.m), true);
});

// typed values
data.encode.forEach(function (c) {
  const parsed = L.parseValue(c.text);
  eq('parse ok ' + c.text, !!parsed.f, true);
  eq('parse value ' + c.text, L.fracStr(parsed.f), c.x);
  const r = L.encode(parsed.f, c.m, c.e);
  eq('status ' + c.text + ' ' + c.m + '+' + c.e, r.status, c.status === 'ok' ? 'ok' : c.status === 'zero' ? 'zero' : c.status);
  if (c.status === 'ok' || c.status === 'zero' || c.status === 'underflow') {
    eq('mbits ' + c.text + ' ' + c.m + '+' + c.e, r.m, c.mbits);
    eq('ebits ' + c.text + ' ' + c.m + '+' + c.e, r.e, c.ebits);
  }
  if (c.status === 'ok') eq('normalised result ' + c.text, L.isNormalised(r.m), true);
});

// changing the split of bits
data.reformat.forEach(function (c) {
  const r = L.reformat(c.m, c.e, c.m2, c.e2);
  if (c.status === 'ok' || c.status === 'zero') {
    eq('reformat m ' + c.m + ' ' + c.e + ' to ' + c.m2 + '+' + c.e2, r.m, c.mbits);
    eq('reformat e ' + c.m + ' ' + c.e + ' to ' + c.m2 + '+' + c.e2, r.e, c.ebits);
  } else if (c.status === 'underflow') {
    eq('reformat underflow m', r.m, c.mbits);
  } else {
    eq('reformat overflow note', /too large/.test(r.note), true);
  }
});

// bad input never throws
['', ' ', 'abc', '1e5', '--5', '5/0', '.', '-', '1.2.3', '9999999999999999999999999999999999', '1/', '/2', '٣'].forEach(function (t) {
  const p = L.parseValue(t);
  eq('bad input ' + t, !!p.error, true);
});
eq('null input', !!L.parseValue(null).error, true);

// fixed examples from the chapter
function enc(t, m, e) { const r = L.encode(L.parseValue(t).f, m, e); return r.status === 'ok' ? r.m + ' ' + r.e : r.status; }
eq('6.25', enc('6.25', 8, 4), '01100100 0011');
eq('-3.5', enc('-3.5', 8, 4), '10010000 0010');
eq('-4', enc('-4', 8, 4), '10000000 0010');
eq('0.15625', enc('0.15625', 8, 4), '01010000 1110');
eq('0.1', enc('0.1', 8, 4), '01100110 1101');
eq('22.5', enc('22.5', 8, 4), '01011010 0101');
eq('-5.25', enc('-5.25', 8, 4), '10101100 0011');
eq('300 overflows', enc('300', 8, 4), 'overflow');
eq('0.001 underflows', enc('0.001', 8, 4), 'underflow');
eq('value 5.5', L.fracStr(L.value('01011000', '0011')), '11/2');
eq('decimal 5.5', L.decStr(L.value('01011000', '0011')), '5.5');
eq('value -2.5', L.decStr(L.value('10110000', '0010')), L.MINUS + '2.5');
eq('mantissa sum', L.mantissaSum('10110000'), L.MINUS + '1 + 1/4 + 1/8');
eq('smallest 8+4 decimal', L.decStr(L.limits(8, 4).smallest.value), '0.001953125');
eq('largest 8+4', L.decStr(L.limits(8, 4).largest.value), '127');
eq('why not', /both 0/.test(L.whyNot('00110100')), true);
eq('percent', L.errorPercent(L.frac(B(1), B(2560)), L.frac(B(1), B(10))), '0.39%');
function B(x) { return BigInt(x); }

console.log('cs-float logic ok: ' + checks + ' checks');
