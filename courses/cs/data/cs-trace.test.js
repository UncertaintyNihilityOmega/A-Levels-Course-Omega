// data/cs-trace.test.js: checks the pure helpers of widgets/cs-trace.js against the generated programs.
// Run: py data/cs.trace_gen.py && node data/cs-trace.test.js
const path = require('path');
global.W = { register() {} };
const w = require(path.join(process.cwd(), 'widgets', 'cs-trace.js'));
let bad = 0, runs = 0;
for (const [name, prog] of Object.entries(w.PROGRAMS)) {
  for (const run of prog.runs) {
    runs++;
    const n = run.events.length;
    const rows = w.rowsUpTo(run, n);
    // the last value shown in every column equals the program's final state
    for (const [k, v] of Object.entries(run.final)) {
      const last = rows.filter(r => r.cells[k] !== undefined).map(r => r.cells[k]).pop();
      if (last !== v) { bad++; console.log('FINAL', name, run.label, k, last, v); }
    }
    // OUTPUT cells equal the outputs list, in order
    const outs = rows.filter(r => r.cells.OUTPUT !== undefined).map(r => r.cells.OUTPUT);
    if (JSON.stringify(outs) !== JSON.stringify(run.outputs)) { bad++; console.log('OUT', name, run.label, outs, run.outputs); }
    // every row's columns are known, every line number is inside the listing
    for (const r of rows) {
      for (const k of Object.keys(r.cells)) if (!prog.columns.includes(k)) { bad++; console.log('COL', name, k); }
      if (r.line < 1 || r.line > prog.lines.length) { bad++; console.log('LINE', name, r.line); }
    }
    // rows only grow as steps advance
    let prev = 0;
    for (let k = 0; k <= n; k++) { const c = w.rowsUpTo(run, k).length; if (c < prev) { bad++; console.log('SHRINK', name); } prev = c; }
    if (w.currentLine(run, 0) !== 0 || w.currentLine(run, n) !== run.events[n - 1].line) { bad++; console.log('CURRENT', name); }
  }
}
console.log(bad === 0 ? 'cs-trace logic ok: ' + runs + ' runs' : bad + ' problems');
