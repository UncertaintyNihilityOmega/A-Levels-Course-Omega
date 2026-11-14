// data/cs-pipeline.test.js: checks widgets/cs-pipeline.js against an independent cycle-by-cycle simulation of a
// five-stage pipeline with a taken jump, and drives its controls through a minimal fake DOM.
// Run: node data/cs-pipeline.test.js   (from the course folder)
const path = require('path');

class El {
  constructor(tag) { this.tag = tag; this.children = []; this.attrs = {}; this.style = {}; this.listeners = {}; this._text = ''; this.className = ''; this.value = ''; }
  appendChild(c) { this.children.push(c); return c; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  getAttribute(k) { return this.attrs[k]; }
  addEventListener(t, f) { (this.listeners[t] = this.listeners[t] || []).push(f); }
  set textContent(v) { this.children = []; this._text = String(v); }
  get textContent() { return this._text + this.children.map(function (c) { return c.textContent; }).join(''); }
  fire(t) { (this.listeners[t] || []).forEach(function (f) { f({}); }); }
  all(pred, out) { out = out || []; if (pred(this)) out.push(this); this.children.forEach(function (c) { c.all(pred, out); }); return out; }
}
global.W = {
  h: function (tag, props) {
    const e = new El(tag);
    props = props || {};
    Object.keys(props).forEach(function (k) {
      if (k === 'class') e.className = props[k];
      else if (k === 'text') e._text = props[k];
      else if (k === 'style') Object.assign(e.style, props[k]);
      else e.setAttribute(k, props[k]);
    });
    for (let i = 2; i < arguments.length; i++) if (arguments[i]) e.appendChild(arguments[i]);
    return e;
  },
  frame: function (el) { const body = new El('div'); el.appendChild(body); return { root: el, body: body }; },
  register: function (name, fn) { global.__init = fn; }
};
const P = require(path.join(__dirname, '..', 'widgets', 'cs-pipeline.js'));

let checks = 0;
function eq(a, b, label) { checks++; if (JSON.stringify(a) !== JSON.stringify(b)) { console.error('FAIL ' + label + '\n  got  ' + JSON.stringify(a) + '\n  want ' + JSON.stringify(b)); process.exit(1); } }

// ---- an independent simulation: instructions enter one per cycle; a taken jump is known at the end of its EX ----
function simulate(n, branch) {
  const K = 5;
  const stages = ['IF', 'ID', 'OF', 'EX', 'WB'];
  const pipe = new Array(K).fill(null);        // pipe[s] = {id, wrong} or null
  const grid = {};                              // key id -> {cycle: stage}
  const order = [];
  let nextReal = 1, nextWrong = 0, wrongMode = false, cycle = 0, done = 0, flushedIds = {};
  while (done < n) {
    cycle++;
    // advance
    for (let s = K - 1; s > 0; s--) pipe[s] = pipe[s - 1];
    // fetch
    if (wrongMode) { nextWrong++; pipe[0] = { id: 'w' + nextWrong, wrong: true }; }
    else if (nextReal <= n) { pipe[0] = { id: 'i' + nextReal, wrong: false }; nextReal++; }
    else pipe[0] = null;
    // record
    for (let s = 0; s < K; s++) if (pipe[s]) { (grid[pipe[s].id] = grid[pipe[s].id] || {})[cycle] = stages[s]; if (order.indexOf(pipe[s].id) < 0) order.push(pipe[s].id); }
    // the jump is in EX (stage 3) this cycle: flush what is behind it, then fetch the real next instruction
    if (pipe[3] && !pipe[3].wrong && pipe[3].id === 'i' + branch && branch) {
      pipe[0] = null; pipe[1] = null; pipe[2] = null;
      // the fake wrong instructions were already recorded; the real fetch continues from the next cycle
      wrongMode = false;
    }
    // while the jump is not yet in EX, instructions fetched after it are wrong
    if (branch && pipe[0] && !pipe[0].wrong && pipe[0].id === 'i' + branch && !flushedIds[branch]) { flushedIds[branch] = true; wrongMode = true; nextReal = branch + 1; }
    if (pipe[4] && !pipe[4].wrong) done++;
  }
  return { cycles: cycle, grid: grid };
}

// the widget's rows must agree with the simulation for every n and every jump
for (let n = 3; n <= 10; n++) {
  for (let b = 0; b <= n - 1; b++) {
    const lay = P.layout(n, b, true);
    const sim = simulate(n, b);
    eq(lay.cycles, sim.cycles, 'cycles n=' + n + ' b=' + b);
    eq(lay.cycles, P.counts(n, b).pipelined, 'counts n=' + n + ' b=' + b);
    lay.rows.forEach(function (r) {
      const id = r.flushed ? 'w' + r.label.split(' ')[1] : 'i' + r.label.slice(1);
      eq(r.cells, sim.grid[id], 'cells ' + r.label + ' n=' + n + ' b=' + b);
    });
    eq(lay.rows.filter(function (r) { return r.flushed; }).length, b ? 3 : 0, 'flushed rows');
    // formulas from the chapter
    eq(P.counts(n, b).noJump, 5 + n - 1, 'no jump formula');
    eq(P.counts(n, b).notPipelined, 5 * n, 'sequential formula');
    eq(P.counts(n, b).pipelined, 5 + n - 1 + (b ? 3 : 0), 'jump penalty');
    // not pipelined: one instruction at a time, no flushed rows, no gaps
    const seq = P.layout(n, b, false);
    eq(seq.cycles, 5 * n, 'seq cycles');
    eq(seq.rows.length, n, 'seq rows');
    seq.rows.forEach(function (r, i) { eq(Object.keys(r.cells).map(Number), [1, 2, 3, 4, 5].map(function (s) { return 5 * i + s; }), 'seq cells'); });
  }
}
// the numbers in the chapter
eq(P.counts(4, 0).pipelined, 8, 'chapter 4 instructions');
eq(P.counts(4, 0).notPipelined, 20, 'chapter 4 sequential');
eq(P.counts(6, 3).pipelined, 13, 'chapter jump 3 of 6');
eq(P.counts(8, 4).pipelined, 15, 'chapter jump 4 of 8');
eq(P.counts(5, 0).pipelined, 9, 'chapter 5 instructions');
eq(P.inCycle(P.layout(4, 0, true), 4).map(function (x) { return x.label + x.stage; }), ['I1EX', 'I2OF', 'I3ID', 'I4IF'], 'cycle 4');
eq(P.inCycle(P.layout(6, 3, true), 6).map(function (x) { return x.label + x.stage + (x.flushed ? '*' : ''); }), ['I2WB', 'I3EX', 'wrong 1OF*', 'wrong 2ID*', 'wrong 3IF*'], 'cycle 6 with jump');
// bad input
eq(P.clampN('abc'), 6, 'bad n'); eq(P.clampN(1), 3, 'low n'); eq(P.clampN(99), 10, 'high n'); eq(P.clampN('7.4'), 7, 'round n');
eq(P.clampBranch(5, 5), 0, 'branch = n'); eq(P.clampBranch(-2, 5), 0, 'negative branch'); eq(P.clampBranch('x', 5), 0, 'text branch'); eq(P.clampBranch(4, 5), 4, 'last valid');

// ---- the UI ----
function mount(opts) {
  const root = new El('div');
  global.__init(root, opts);
  const q = {
    root: root,
    slider: root.all(function (e) { return e.attrs['aria-label'] === 'Number of instructions'; })[0],
    select: root.all(function (e) { return e.tag === 'select'; })[0],
    cslider: root.all(function (e) { return e.attrs['aria-label'] === 'Clock cycle to look at'; })[0],
    tabs: root.all(function (e) { return e.className === 'w-tab'; }),
    text: function () { return root.textContent; },
    cap: function () { return root.all(function (e) { return e.tag === 'caption'; })[0]._text; },
    rows: function () { return root.all(function (e) { return e.tag === 'tbody'; })[0].children.length; },
    err: function () { return root.all(function (e) { return e.className === 'w-err'; }).map(function (e) { return e._text; }); }
  };
  return q;
}
let w = mount({ n: '6', branch: '3' });
eq(w.cap(), 'Pipelined: 13 clock cycles for 6 instructions', 'start caption');
eq(w.rows(), 9, 'six instructions and three flushed rows');
eq(w.err(), [], 'no error');
eq(w.tabs[0].attrs['aria-pressed'], 'true', 'pipelined pressed');
w.tabs[1].fire('click');
eq(w.cap(), 'Not pipelined: 30 clock cycles for 6 instructions', 'sequential caption');
eq(w.rows(), 6, 'rows without a pipeline');
eq(w.tabs[1].attrs['aria-pressed'], 'true', 'sequential pressed');
eq(/5 × 6 = 30/.test(w.text()) && /13 cycles/.test(w.text()), true, 'sequential sentence');
w.tabs[0].fire('click');
w.select.value = '0'; w.select.fire('change');
eq(w.cap(), 'Pipelined: 10 clock cycles for 6 instructions', 'no jump');
w.slider.value = '4'; w.slider.fire('input');
eq(w.cap(), 'Pipelined: 8 clock cycles for 4 instructions', 'four instructions');
eq(/pipeline is 2\.50 times as fast/.test(w.text()), true, '20 / 8 = 2.50');
eq(w.select.children.length, 4, 'none, I1, I2, I3');
w.select.value = '3'; w.select.fire('change');
eq(w.cap(), 'Pipelined: 11 clock cycles for 4 instructions', 'jump at 3 of 4');
w.slider.value = '3'; w.slider.fire('input');
eq(w.select.children.length, 3, 'options shrink');
eq(w.select.value, '0', 'jump no longer valid, reset to none');
w.cslider.value = '5'; w.cslider.fire('input');
eq(/Cycle 5: /.test(w.text()), true, 'look at cycle 5');
// bad attributes
w = mount({ n: 'many', branch: '99' });
eq(w.cap(), 'Pipelined: 10 clock cycles for 6 instructions', 'bad attributes fall back');
eq(w.err().length, 1, 'one message');
w = mount({});
eq(w.cap(), 'Pipelined: 10 clock cycles for 6 instructions', 'defaults');
w = mount({ n: '3', branch: '2' });
eq(w.cap(), 'Pipelined: 10 clock cycles for 3 instructions', 'n=3 jump at 2: 7 + 3');

console.log('cs-pipeline logic and UI ok: ' + checks + ' checks');
