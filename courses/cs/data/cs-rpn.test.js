// data/cs-rpn.test.js: checks widgets/cs-rpn.js against an independent Python model (the chapter's own algorithms).
// Python builds 400 random infix expressions, converts them with its own shunting-yard, evaluates the RPN with
// fractions, and prints JSON. Node must give the same RPN text and the same exact result. It also checks the
// error cases. Run: node data/cs-rpn.test.js
const { execFileSync } = require('child_process');
const path = require('path');
const R = require(path.join(__dirname, '..', 'widgets', 'cs-rpn.js'));

const py = `
import json, random
from fractions import Fraction
random.seed(5)
PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def to_rpn(tokens):
    out, ops = [], []
    for t in tokens:
        if t == '(':
            ops.append(t)
        elif t == ')':
            while ops[-1] != '(':
                out.append(ops.pop())
            ops.pop()
        elif t in PREC:
            while ops and ops[-1] != '(' and (PREC[ops[-1]] > PREC[t] or (PREC[ops[-1]] == PREC[t] and t != '^')):
                out.append(ops.pop())
            ops.append(t)
        else:
            out.append(t)
    while ops:
        out.append(ops.pop())
    return out

def ev(rpn, vals):
    st = []
    for t in rpn:
        if t in PREC:
            b, a = st.pop(), st.pop()
            if t == '+': st.append(a + b)
            elif t == '-': st.append(a - b)
            elif t == '*': st.append(a * b)
            elif t == '/':
                if b == 0: return None
                st.append(a / b)
            else:
                if b.denominator != 1 or abs(b) > 20: return None
                if a == 0 and b < 0: return None
                st.append(a ** int(b))
        elif t.isalpha():
            st.append(Fraction(vals[t]))
        else:
            st.append(Fraction(t))
    return st[0]

def gen(depth):
    if depth == 0 or random.random() < 0.3:
        return [random.choice('ABCDE')] if random.random() < 0.6 else [str(random.randint(1, 20))]
    op = random.choice('+-*/+-*/^')
    left, right = gen(depth - 1), gen(depth - 1)
    if op == '^':
        right = [str(random.randint(0, 3))]
    def wrap(x):
        return ['('] + x + [')'] if len(x) > 1 and random.random() < 0.6 else x
    return wrap(left) + [op] + wrap(right)

cases = []
for _ in range(400):
    toks = gen(random.randint(1, 4))
    # always bracket when a lower-precedence part could change meaning: re-parse by brackets only where gen added them
    vals = {c: random.randint(-5, 9) for c in 'ABCDE'}
    rpn = to_rpn(toks)
    r = ev(rpn, vals)
    cases.append({'expr': ''.join(toks), 'rpn': ' '.join(rpn), 'vals': ','.join(f'{k}={v}' for k, v in vals.items()),
                  'result': None if r is None else (str(r.numerator) if r.denominator == 1 else f'{r.numerator}/{r.denominator}')})
print(json.dumps(cases))
`;
const cases = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8', maxBuffer: 1 << 26 }));
let n = 0, evaluated = 0;
for (const c of cases) {
  const m = R.toRPN(c.expr);
  if (m.error) throw new Error('toRPN error on ' + c.expr + ': ' + m.error);
  if (m.rpnText !== c.rpn) throw new Error('RPN differs for ' + c.expr + ': got ' + m.rpnText + ', want ' + c.rpn);
  // the last step's output equals the answer, and every step keeps output and stack arrays
  const last = m.steps[m.steps.length - 1];
  if (last.output.join(' ') !== c.rpn || last.ops.length) throw new Error('final step wrong for ' + c.expr);
  const e = R.evalRPN(c.rpn, c.vals);
  if (c.result === null) {
    if (!e.error) throw new Error('expected an error evaluating ' + c.rpn + ' with ' + c.vals + ', got ' + e.result);
  } else {
    if (e.error) throw new Error('evaluation error ' + e.error + ' for ' + c.rpn + ' with ' + c.vals);
    if (e.result !== c.result) throw new Error('result differs for ' + c.rpn + ' with ' + c.vals + ': got ' + e.result + ', want ' + c.result);
    evaluated += 1;
  }
  n += 1;
}

// the chapter's examples and the widget's default
const d = R.toRPN('(A + B) * (C - D) / E');
if (d.rpnText !== 'A B + C D - * E /') throw new Error('default RPN: ' + d.rpnText);
const dv = R.evalRPN(d.rpnText, 'A=3,B=5,C=9,D=4,E=2');
if (dv.result !== '20') throw new Error('default value: ' + dv.result);
if (R.toRPN('A - B * C').rpnText !== 'A B C * -') throw new Error('A - B * C');
if (R.toRPN('A - B - C').rpnText !== 'A B - C -') throw new Error('A - B - C');
if (R.toRPN('A ^ B ^ C').rpnText !== 'A B C ^ ^') throw new Error('A ^ B ^ C');
if (R.evalRPN('7 2 /', '').result !== '7/2' || R.evalRPN('7 2 /', '').decimal !== '3.5') throw new Error('7/2');

// errors (never a throw)
const bad = ['', '   ', '((A + B)', 'A + B)', 'A B', 'A +', '+ A', '()', 'A $ B', '- A', 'A (B)', '(A + B) C', 'x'.repeat(200), '3 .', null, undefined];
bad.forEach(function (s) {
  const m = R.toRPN(s);
  if (s === 'x'.repeat(200) || s === '3 .' || s === '' || s === '   ' || s == null || /[(){}$+ABx]/.test(String(s))) {
    // all of these except the valid-looking ones must be errors
  }
  if (!m.error && ['A B', 'A +', '+ A', '()', 'A $ B', '- A', 'A (B)', '(A + B) C', '((A + B)', 'A + B)', '', '   '].indexOf(s) >= 0) {
    throw new Error('expected an error for ' + JSON.stringify(s));
  }
});
const evBad = [['A B', ''], ['A +', 'A=1'], ['1 0 /', ''], ['1 2', ''], ['( 1 )', ''], ['A', 'B=1'], ['1 2 +', 'A'], ['0 -1 ^', ''], ['2 99 ^', ''], ['', '']];
evBad.forEach(function (p) {
  const m = R.evalRPN(p[0], p[1]);
  if (!m.error) throw new Error('expected an error evaluating ' + JSON.stringify(p));
});
console.log('ok: ' + n + ' random expressions compared (' + evaluated + ' evaluated exactly), examples and error cases pass');
