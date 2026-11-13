// data/cs-logic.test.js: checks widgets/cs-logic.js (parser, truth tables, marking) against Python.
// Python builds 300 random expressions as trees and computes the truth table itself; Node parses the text
// and must give the same rows. Run: node data/cs-logic.test.js
const { execFileSync } = require('child_process');
const path = require('path');
const L = require(path.join(__dirname, '..', 'widgets', 'cs-logic.js'));

const py = `
import json, random
random.seed(7)
OPS = {'AND': lambda a, b: a & b, 'OR': lambda a, b: a | b, 'NAND': lambda a, b: 1 - (a & b),
       'NOR': lambda a, b: 1 - (a | b), 'XOR': lambda a, b: a ^ b}
def tree(d, names):
    if d == 0 or random.random() < 0.25:
        return ('v', random.choice(names))
    if random.random() < 0.25:
        return ('not', tree(d - 1, names))
    return ('bin', random.choice(list(OPS)), tree(d - 1, names), tree(d - 1, names))
def render(t, top=True, spaced=True):
    if t[0] == 'v':
        return t[1]
    if t[0] == 'not':
        inner = render(t[1], False)
        return 'NOT ' + (inner if t[1][0] != 'bin' else inner)
    a, b = render(t[2], False), render(t[3], False)
    s = f'{a} {t[1]} {b}'
    return s if top else '(' + s + ')'
def val(t, env):
    if t[0] == 'v': return env[t[1]]
    if t[0] == 'not': return 1 - val(t[1], env)
    return OPS[t[1]](val(t[2], env), val(t[3], env))
def names_in(t):
    if t[0] == 'v': return {t[1]}
    if t[0] == 'not': return names_in(t[1])
    return names_in(t[2]) | names_in(t[3])
out = []
for _ in range(300):
    t = tree(random.choice([1, 2, 3, 3, 4]), random.choice([['A'], ['A', 'B'], ['A', 'B', 'C'], ['A', 'B', 'C', 'D']]))
    text = render(t)
    vs = sorted(names_in(t))
    n = len(vs)
    rows = []
    for i in range(2 ** n):
        env = {v: (i >> (n - 1 - k)) & 1 for k, v in enumerate(vs)}
        rows.append(val(t, env))
    out.append({'text': text, 'vars': vs, 'x': rows})
print(json.dumps(out))
`;
const data = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8', maxBuffer: 1 << 26 }));
let checks = 0;
function eq(label, got, want) {
  checks++;
  const g = JSON.stringify(got), w = JSON.stringify(want);
  if (g !== w) { console.error('FAIL ' + label + ': got ' + g + ', want ' + w); process.exit(1); }
}

// 1. random expressions: the parser reads them and the table matches Python
data.forEach(function (d) {
  const p = L.parse(d.text);
  if (p.error) { console.error('FAIL parse ' + d.text + ': ' + p.error); process.exit(1); }
  const t = L.table(p);
  eq('vars ' + d.text, t.vars, d.vars);
  eq('x ' + d.text, t.rows.map(function (r) { return r.x; }), d.x);
  eq('rows ' + d.text, t.rows.length, Math.pow(2, d.vars.length));
  // re-parsing the displayed text gives the same table
  const again = L.table(L.parse(L.show(p.ast)));
  eq('show ' + d.text, again.rows.map(function (r) { return r.x; }), d.x);
  // working columns: the last sub-expression is the whole expression
  eq('last sub ' + d.text, t.rows.map(function (r) { return r.work[r.work.length - 1]; }),
    p.ast.t === 'var' ? t.rows.map(function (r) { return undefined; }) : d.x);
});

// 2. the chapter's expressions and spellings
function xs(text) { const p = L.parse(text); return p.error ? p.error : L.table(p).rows.map(function (r) { return r.x; }); }
eq('chapter 1', xs('(A AND B) OR NOT C'), [1, 0, 1, 0, 1, 0, 1, 1]);
eq('lower case', xs('(a and b) or not c'), [1, 0, 1, 0, 1, 0, 1, 1]);
eq('spaces', xs('  (A   AND B)OR   NOT C '), [1, 0, 1, 0, 1, 0, 1, 1]);
eq('xor circuit', xs('(A OR B) AND NOT (A AND B)'), [0, 1, 1, 0]);
eq('not binds next', xs('NOT A AND B'), [0, 1, 0, 0]);
eq('not bracket', xs('NOT (A AND B)'), [1, 1, 1, 0]);
eq('double not', xs('NOT NOT A'), [0, 1]);
eq('chain and', xs('A AND B AND C'), [0, 0, 0, 0, 0, 0, 0, 1]);
eq('chain or', xs('A OR B OR C'), [0, 1, 1, 1, 1, 1, 1, 1]);
eq('single variable', xs('A'), [0, 1]);
eq('kiln', xs('(A AND B) AND NOT C'), [0, 0, 0, 0, 0, 0, 1, 0]);
eq('four variables', xs('(A AND B) OR (C AND D)').length, 16);

// 3. errors are friendly messages, never exceptions
const bad = ['', '   ', '(', ')', 'A AND', 'AND A', 'A B', 'A AND B OR C', 'A OR B AND C', 'A NAND B NAND C', 'A XOR B XOR C',
  '(A AND B', 'A AND B)', 'NOT', 'E AND A', 'A AND Q', 'FOO', 'A & B', 'A AND 1', '1', '()', 'A AND ()', 'NOT NOT', 'A,B',
  'A AND (B OR', '((A))) AND B', 'A AND OR B', 'A NOT B'];
bad.forEach(function (t) {
  const p = L.parse(t);
  eq('error for ' + JSON.stringify(t), typeof p.error === 'string' && p.error.length > 0 && !p.ast, true);
});
eq('long input', typeof L.parse(new Array(300).join('A AND ') + 'A').error, 'string');
eq('null input', typeof L.parse(null).error, 'string');
eq('undefined input', typeof L.parse(undefined).error, 'string');
eq('brackets only valid', xs('((A))'), [0, 1]);

// 4. working columns: one per distinct gate, inner gates first
const t3 = L.table(L.parse('(A AND B) OR NOT C'));
eq('subs', t3.subs.map(function (s) { return s.text; }), ['A AND B', 'NOT C', '(A AND B) OR NOT C']);
eq('work rows', t3.rows.map(function (r) { return r.work; }), [[0, 1, 1], [0, 0, 0], [0, 1, 1], [0, 0, 0], [0, 1, 1], [0, 0, 0], [1, 1, 1], [1, 0, 1]]);
const t4 = L.table(L.parse('(A XOR B) XOR (A XOR B)'));
eq('duplicate sub-expression shown once', t4.subs.map(function (s) { return s.text; }), ['A XOR B', '(A XOR B) XOR (A XOR B)']);

// 5. the six gates against their definitions
const defs = {
  NOT: function (a) { return a === 0 ? 1 : 0; },
  AND: function (a, b) { return a === 1 && b === 1 ? 1 : 0; },
  OR: function (a, b) { return a === 1 || b === 1 ? 1 : 0; },
  NAND: function (a, b) { return a === 1 && b === 1 ? 0 : 1; },
  NOR: function (a, b) { return a === 0 && b === 0 ? 1 : 0; },
  XOR: function (a, b) { return a !== b ? 1 : 0; }
};
L.GATE_NAMES.forEach(function (g) {
  [0, 1].forEach(function (a) {
    [0, 1].forEach(function (b) { eq(g + ' ' + a + b, L.gate(g, a, b), defs[g](a, b)); });
  });
  eq('rule text for ' + g, typeof L.rule[g], 'string');
});
eq('gates in the chapter order', L.GATE_NAMES, ['NOT', 'AND', 'OR', 'NAND', 'NOR', 'XOR']);

// 6. marking
const tt = L.table(L.parse('A AND B'));
let m = L.mark(tt, [0, 0, 0, 1]);
eq('all right', [m.right, m.total, m.marks.every(function (k) { return k.ok; })], [4, 4, true]);
m = L.mark(tt, [null, 1, 0, 1]);
eq('some wrong', [m.right, m.marks.map(function (k) { return k.ok; })], [2, [false, false, true, true]]);
eq('unanswered flagged', m.marks.map(function (k) { return k.answered; }), [false, true, true, true]);
eq('wanted values', m.marks.map(function (k) { return k.want; }), [0, 0, 0, 1]);

console.log('cs-logic: ' + checks + ' checks passed (' + data.length + ' random expressions compared with Python)');
