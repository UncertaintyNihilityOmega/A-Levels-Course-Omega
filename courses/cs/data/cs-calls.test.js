// data/cs-calls.test.js: the pure model of widgets/cs-calls.js against Python (call counts, values, outputs).
// Run from the course folder: node data/cs-calls.test.js
const S = require('./../widgets/cs-calls.js');
const { execFileSync } = require('child_process');
const py = `
import json
calls = 0
def fact(n):
    global calls; calls += 1
    return 1 if n <= 1 else n * fact(n - 1)
def power(e):
    global calls; calls += 1
    return 1 if e == 0 else 2 * power(e - 1)
def sd(n):
    global calls; calls += 1
    return n if n < 10 else n % 10 + sd(n // 10)
def fib(n):
    global calls; calls += 1
    return n if n <= 1 else fib(n - 1) + fib(n - 2)
def cd(n, out):
    global calls; calls += 1
    if n > 0:
        out.append(n); cd(n - 1, out)
def cu(n, out):
    global calls; calls += 1
    if n > 0:
        cu(n - 1, out); out.append(n)
res = {}
def val(name, f, rng):
    global calls
    for n in rng:
        calls = 0
        v = f(n)
        res[name + ':' + str(n)] = [v, calls]
val('factorial', fact, range(0, 9)); val('power', power, range(0, 9)); val('fib', fib, range(0, 7))
val('sumdigits', sd, [0, 9, 10, 274, 2758, 99999, 5000])
for name, f in (('countdown', cd), ('countup', cu)):
    for n in range(0, 9):
        calls = 0; out = []; f(n, out)
        res[name + ':' + str(n)] = [out, calls]
print(json.dumps(res))
`;
const want = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8' }));
let count = 0;
function eq(label, got, exp) {
  if (JSON.stringify(got) !== JSON.stringify(exp)) throw new Error(label + ': got ' + JSON.stringify(got) + ', Python says ' + JSON.stringify(exp));
  count += 1;
}
Object.keys(want).forEach(function (key) {
  const parts = key.split(':');
  const m = S.run(parts[0], parseInt(parts[1], 10));
  const w = want[key];
  if (S.FNS[parts[0]].proc) eq(key + ' outputs', m.outputs.map(Number), w[0]);
  else eq(key + ' value', m.value, w[0]);
  eq(key + ' calls', m.calls, w[1]);
  const last = m.steps[m.steps.length - 1];
  eq(key + ' final stack empty', last.stack.length, 0);
  eq(key + ' final calls', last.calls, w[1]);
  // every frame pushed is popped: depth never negative and the first step is empty
  eq(key + ' first step empty', m.steps[0].stack.length, 0);
});
// chapter facts
eq('factorial 4 deepest', S.run('factorial', 4).maxDepth, 4);
eq('fib 4 calls', S.run('fib', 4).calls, 9);
eq('fib 6 calls', S.run('fib', 6).calls, 25);
eq('power 5 calls', S.run('power', 5).calls, 6);
eq('sumdigits 274', [S.run('sumdigits', 274).value, S.run('sumdigits', 274).calls], [13, 3]);
eq('countup 3 outputs', S.run('countup', 3).outputs, ['1', '2', '3']);
eq('countdown 3 outputs', S.run('countdown', 3).outputs, ['3', '2', '1']);
// bad input never throws
eq('bad fn', S.fnOf('nonsense'), 'factorial');
eq('bad fn null', S.fnOf(null), 'factorial');
eq('bad n -> default', S.run('fib', NaN).n, 4);
eq('bad n range -> default', S.run('fib', 99).n, 4);
eq('parse bad', typeof S.parseN('fib', 'x').error, 'string');
eq('parse range', typeof S.parseN('fib', '7').error, 'string');
eq('parse ok', S.parseN('fib', '6').n, 6);
eq('parse empty', typeof S.parseN('fib', '').error, 'string');
eq('parse undefined', typeof S.parseN('fib', undefined).error, 'string');
// a snapshot at every step has text
S.ORDER.forEach(function (f) {
  const m = S.run(f, S.FNS[f].max > 9 ? 12 : S.FNS[f].max);
  m.steps.forEach(function (s, i) { if (!s.text) throw new Error(f + ' step ' + i + ' has no text'); });
});
console.log('ok', count, 'assertions');
