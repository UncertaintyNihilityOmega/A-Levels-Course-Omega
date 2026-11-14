// data/cs-kmap.test.js: tests the cs-kmap solver against data/cs_kmap_model.py (every 2- and 3-variable function
// and 2000 random 4-variable ones). Run from the course folder: node data/cs-kmap.test.js
const { execSync } = require('child_process');
const path = require('path');
const K = require(path.join(process.cwd(), 'widgets', 'cs-kmap.js'));
const cases = JSON.parse(execSync('py data/cs_kmap_model.py --dump', { maxBuffer: 1 << 26 }).toString());
let bad = 0;
cases.forEach(function (c) {
  const n = c[0], ones = c[1], want = c[2];
  const g = K.solve(n, ones);
  const got = K.cost(n, g);
  let ok = got[0] === want[0] && got[1] === want[1];
  for (let m = 0; m < (1 << n); m++) if (K.evalGroups(g, m) !== (ones.indexOf(m) >= 0)) ok = false;
  if (!ok) { bad++; if (bad < 6) console.log('MISMATCH', n, ones, got, want); }
});
console.log(cases.length + ' cases, ' + bad + ' mismatches');
const eq = function (a, b, m) { if (JSON.stringify(a) !== JSON.stringify(b)) { bad++; console.log('FAIL', m, JSON.stringify(a), JSON.stringify(b)); } };
eq(K.parseOnes('1, 3 5;7', 3).ones, [1, 3, 5, 7], 'parse');
eq(!!K.parseOnes('9', 3).error, true, 'range');
eq(!!K.parseOnes('x', 3).error, true, 'junk');
eq(K.parseOnes('', 4).ones, [], 'empty');
eq(K.wraps(3, [0, 2]), true, 'wrap 0,2');
eq(K.wraps(3, [1, 3]), false, 'no wrap 1,3');
eq(K.wraps(4, [0, 8]), true, 'wrap rows');
eq(K.wraps(4, [0, 1, 2, 3]), false, 'row not wrap');
eq(K.exprWords(3, K.solve(3, [1, 3, 5, 7])), 'C', 'C');
eq(K.exprAlg(3, K.solve(3, [0, 1, 2, 3, 4, 5, 6, 7])), '1', 'all ones');
eq(K.exprAlg(3, K.solve(3, [])), '0', 'none');
process.exit(bad ? 1 : 0);
