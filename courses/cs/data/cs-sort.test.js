// data/cs-sort.test.js: the pure model of widgets/cs-sort.js against the numbers in chapters/cs.algorithms2.md.
// Run from the course folder: node data/cs-sort.test.js
const S = require('./../widgets/cs-sort.js');
function eq(label, got, want) {
  if (JSON.stringify(got) !== JSON.stringify(want)) throw new Error(label + ': got ' + JSON.stringify(got) + ', chapter says ' + JSON.stringify(want));
}
let n = 0;
// the chapter's comparison table (n = 8)
const sets = { sorted: [1, 2, 3, 4, 5, 6, 7, 8], reversed: [8, 7, 6, 5, 4, 3, 2, 1], random: [5, 2, 8, 1, 7, 3, 6, 4] };
const bub = { sorted: [7, 0], reversed: [28, 28], random: [25, 14] };
const ins = { sorted: [7, 0], reversed: [28, 28], random: [19, 14] };
Object.keys(sets).forEach(function (k) {
  const b = S.bubble(sets[k]);
  const i = S.insertion(sets[k]);
  eq('bubble ' + k, [b.comps, b.moves], bub[k]);
  eq('insertion ' + k, [i.comps, i.moves], ins[k]);
  eq('bubble result ' + k, b.result, [1, 2, 3, 4, 5, 6, 7, 8]);
  eq('insertion result ' + k, i.result, [1, 2, 3, 4, 5, 6, 7, 8]);
  n += 4;
});
// the chapter's insertion example
const e = S.insertion([29, 10, 14, 37, 13, 5]);
eq('insertion example', [e.comps, e.moves, e.result], [13, 10, [5, 10, 13, 14, 29, 37]]);
// the efficient bubble sort of cs.datatypes: 41, 17, 33, 8, 25 makes 10 comparisons
const g = S.bubble([41, 17, 33, 8, 25]);
eq('bubble gold', [g.comps, g.moves], [10, 7]);
// binary search: the chapter's two traces
const b35 = S.binary([3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55], 35);
eq('binary 35', [b35.result, b35.comps], [8, 4]);
eq('binary 35 mids', b35.steps.slice(1).map(function (s) { return s.mid + 1; }), [6, 9, 7, 8]);
const b20 = S.binary([3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55], 20);
eq('binary 20', [b20.result, b20.comps], [-1, 4]);
eq('binary 20 mids', b20.steps.slice(1, 5).map(function (s) { return s.mid + 1; }), [6, 3, 4, 5]);
const l = S.linear([29, 10, 14, 37, 13, 5], 13);
eq('linear', [l.result, l.comps], [5, 5]);
const lm = S.linear([29, 10, 14, 37, 13, 5], 99);
eq('linear missing', [lm.result, lm.comps], [-1, 6]);
// worst case of binary search is floor(log2 n) + 1 for every target
for (let size = 1; size <= 300; size++) {
  const arr = [];
  for (let i = 0; i < size; i++) arr.push(2 * i + 2);
  let worst = 0;
  for (let t = 1; t <= 2 * size + 1; t++) worst = Math.max(worst, S.binary(arr, t).comps);
  eq('binary worst ' + size, worst, Math.floor(Math.log2(size)) + 1);
  n += 1;
}
// random data: result sorted, swaps equal inversions, shifts equal swaps
for (let seed = 1; seed <= 200; seed++) {
  const size = 5 + (seed % 8);
  const data = S.dataset('random', size, seed);
  let inv = 0;
  for (let i = 0; i < size; i++) for (let j = i + 1; j < size; j++) if (data[i] > data[j]) inv += 1;
  const bb = S.bubble(data), ii = S.insertion(data);
  const sorted = data.slice().sort(function (x, y) { return x - y; });
  eq('bubble sorted ' + seed, bb.result, sorted);
  eq('insertion sorted ' + seed, ii.result, sorted);
  eq('swaps = inversions ' + seed, [bb.moves, ii.moves], [inv, inv]);
  eq('distinct ' + seed, new Set(data).size, size);
  if (bb.steps[bb.steps.length - 1].sorted.indexOf(false) >= 0) throw new Error('not all marked sorted');
  n += 5;
}
// dataset kinds
eq('sorted kind', S.dataset('sorted', 7, 3), S.dataset('reversed', 7, 3).slice().reverse());
const sd = S.dataset('sorted', 9, 5);
eq('sorted counts n-1', [S.bubble(sd).comps, S.insertion(sd).comps, S.bubble(sd).moves, S.insertion(sd).moves], [8, 8, 0, 0]);
const rd = S.dataset('reversed', 9, 5);
eq('reversed counts', [S.bubble(rd).comps, S.insertion(rd).comps, S.bubble(rd).moves], [36, 36, 36]);
eq('repeatable', S.dataset('random', 8, 7), S.dataset('random', 8, 7));
// parsing and bad input (never throws)
['', null, undefined, '1,2,3', '1,2,3,4,5,6,7,8,9,10,11,12,13', 'a,b,c,d,e', '0,1,2,3,4', '100,1,2,3,4', '1.5,2,3,4,5', '-1,2,3,4,5', '1,2,3,4,5'].forEach(function (s) {
  const r = S.parseValues(s);
  if (!r.error && !r.values) throw new Error('parseValues gave neither');
  n += 1;
});
eq('parse ok', S.parseValues('5, 2 ,8;1 7').values, [5, 2, 8, 1, 7]);
['', 'x', '0', '100', '-3', null].forEach(function (s) { if (!S.parseTarget(s).error) throw new Error('target ' + s); });
eq('target ok', S.parseTarget(' 35 ').target, 35);
eq('algo', [S.algoOf('Binary'), S.algoOf('zzz'), S.algoOf(null)], ['binary', 'bubble', 'bubble']);
// every step has a snapshot of the right size and clean text
['bubble', 'insertion', 'binary', 'linear'].forEach(function (a) {
  const m = S.run(a, [29, 10, 14, 37, 13, 5], 13);
  m.steps.forEach(function (s) {
    if (s.arr.length !== 6 || typeof s.text !== 'string' || !s.text) throw new Error(a + ' step');
    if (/NaN|undefined|Infinity/.test(s.text)) throw new Error(a + ' text: ' + s.text);
  });
});
console.log('ok: ' + n + ' checks against the chapter and brute force');
