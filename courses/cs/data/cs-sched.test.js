// data/cs-sched.test.js: tests the cs-sched logic against data/cs_sched_model.py (random cases, all four
// algorithms, every quantum). Run from the course folder: node data/cs-sched.test.js
const { execSync } = require('child_process');
const path = require('path');
const S = require(path.join(process.cwd(), 'widgets', 'cs-sched.js'));
const cases = JSON.parse(execSync('py data/cs_sched_model.py --dump 3000', { maxBuffer: 1 << 26 }).toString());
let bad = 0;
cases.forEach(function (c) {
  const segs = S.schedule(c.procs, c.algo, c.q);
  const st = S.stats(c.procs, segs);
  const ok = JSON.stringify(segs) === JSON.stringify(c.segs) && JSON.stringify(st.rows) === JSON.stringify(c.rows) &&
    JSON.stringify(st.avgT) === JSON.stringify(c.avgT) && JSON.stringify(st.avgW) === JSON.stringify(c.avgW);
  if (!ok) { bad++; if (bad < 4) console.log('MISMATCH', JSON.stringify(c.procs), c.algo, c.q, JSON.stringify(segs), JSON.stringify(c.segs)); }
});
console.log(cases.length + ' cases, ' + bad + ' mismatches');
const eq = function (a, b, m) { if (JSON.stringify(a) !== JSON.stringify(b)) { bad++; console.log('FAIL', m, JSON.stringify(a), JSON.stringify(b)); } };
eq(S.parseProcs('A:0:5, B:1:3').procs, [['A', 0, 5], ['B', 1, 3]], 'parse');
eq(!!S.parseProcs('A:0:0').error, true, 'burst 0');
eq(!!S.parseProcs('A:0:5,A:1:2').error, true, 'dup');
eq(!!S.parseProcs('').error, true, 'empty');
eq(!!S.parseProcs('A:0:5,B:1:1,C:1:1,D:1:1,E:1:1,F:1:1,G:1:1').error, true, 'seven');
eq(S.showFrac([23, 4]), '5.75 (23/4)', 'show 23/4');
eq(S.showFrac([4, 1]), '4', 'show 4');
eq(S.showFrac([17, 3]), '\u2248 5.67 (17/3)', 'show 17/3');
eq(S.showFrac([7, 2]), '3.5 (7/2)', 'show 7/2');
eq(S.schedule([['A', 3, 2]], 'fcfs', 2), [[null, 0, 3], ['A', 3, 5]], 'idle');
process.exit(bad ? 1 : 0);
