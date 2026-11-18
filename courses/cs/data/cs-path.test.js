// data/cs-path.test.js: node data/cs-path.test.js
// Compares widgets/cs-path.js with the chapter's Python (data/cs-path.expected.json) for every start and goal pair.
const fs = require('fs');
const path = require('path');
const P = require(path.resolve(__dirname, '..', 'widgets', 'cs-path.js'));
const expected = JSON.parse(fs.readFileSync(path.join(__dirname, 'cs-path.expected.json'), 'utf8'));
let n = 0, bad = 0;
['town', 'grid'].forEach(function (gid) {
  const graph = P.GRAPHS[gid];
  ['dijkstra', 'astar'].forEach(function (algo) {
    Object.keys(expected[gid][algo]).forEach(function (key) {
      const parts = key.split('-');
      const run = P.search(graph, algo, parts[0], parts[1]);
      const want = expected[gid][algo][key];
      const ord = P.order(run);
      const ok = JSON.stringify(ord) === JSON.stringify(want.order) && run.cost === want.cost && JSON.stringify(run.path) === JSON.stringify(want.path) && run.found === true;
      n++;
      if (!ok) { bad++; if (bad < 6) console.log('MISMATCH', gid, algo, key, ord.join(''), want.order.join(''), run.cost, want.cost); }
      run.steps.forEach(function (s, k) {
        const t = P.describeStep(run, k, algo);
        if (/NaN|undefined|Infinity/.test(t)) { bad++; console.log('TEXT', gid, algo, key, k, t); }
      });
    });
  });
});
const eq = function (a, b, m) { if (a !== b) { bad++; console.log('FAIL', m, a, b); } };
eq(P.parseChoice('Grid ', ['town', 'grid'], 'town'), 'grid', 'case and spaces');
eq(P.parseChoice('moon', ['town', 'grid'], 'town'), 'town', 'unknown');
eq(P.parseChoice(undefined, ['town', 'grid'], 'town'), 'town', 'undefined');
eq(P.parseChoice(null, ['A', 'B'], 'A'), 'A', 'null');
const r = P.search(P.GRAPHS.town, 'dijkstra', 'A', 'G'); eq(r.chosen, 7, 'town dijkstra chosen'); eq(r.cost, 15, 'town dijkstra cost');
const a = P.search(P.GRAPHS.town, 'astar', 'A', 'G'); eq(a.chosen, 5, 'town astar chosen'); eq(a.path.join(''), 'ADEG', 'town astar path');
const z = P.search(P.GRAPHS.grid, 'astar', 'A1', 'A1'); eq(z.cost, 0, 'same node cost'); eq(z.chosen, 1, 'same node chosen');
console.log(n + ' pairs checked, ' + bad + ' problems');
process.exit(bad ? 1 : 0);
