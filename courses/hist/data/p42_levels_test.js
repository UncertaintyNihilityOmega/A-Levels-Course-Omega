// Node test for widgets/hist-levels.js: logic of the data and of the UI wiring (minimal DOM stub). Run: node data/p42_levels_test.js
'use strict';
const fs = require('fs');
const path = require('path');
const assert = require('assert');

// --- minimal DOM stub ---
function Node_(tag) {
  this.tag = tag; this.children = []; this.attrs = {}; this.style = {}; this.className = ''; this._text = '';
  this.checked = false; this.parent = null;
}
Node_.prototype.appendChild = function (c) { c.parent = this; this.children.push(c); return c; };
Node_.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
Node_.prototype.getAttribute = function (k) { return Object.prototype.hasOwnProperty.call(this.attrs, k) ? this.attrs[k] : null; };
Object.defineProperty(Node_.prototype, 'textContent', {
  get: function () { return this._text + this.children.map(function (c) { return c.textContent; }).join(''); },
  set: function (v) { this._text = String(v); this.children = []; }
});
global.document = { createElement: function (t) { return new Node_(t); }, createTextNode: function (s) { const n = new Node_('#text'); n._text = s; return n; } };
let registered = {};
global.W = { register: function (name, fn) { registered[name] = fn; }, frame: function (el, t, s) { const b = new Node_('div'); el.appendChild(b); return { root: el, body: b }; } };

eval(fs.readFileSync(path.join(__dirname, '..', 'widgets', 'hist-levels.js'), 'utf8'));
const core = W.__histLevelsCore;
assert(core && registered['hist-levels'], 'widget registered');

function find(node, pred, out) { out = out || []; if (pred(node)) out.push(node); node.children.forEach(function (c) { find(c, pred, out); }); return out; }

// --- data checks ---
const expectTop = { p1a: 15, p1b: 25, p2a: 10, p2b: 20, p3a: 20, p3b: 20, p4a: 15, p4b: 15 };
const expectLevels = { p1a: 4, p1b: 5, p2a: 4, p2b: 5, p3a: 6, p3b: 6, p4a: 5, p4b: 5 };
core.PARTS.forEach(function (p) {
  assert.strictEqual(p.levels[0].hi, expectTop[p.key], p.key + ' top mark');
  assert.strictEqual(p.levels[0].hi, p.marks, p.key + ' marks field');
  assert.strictEqual(p.levels.length, expectLevels[p.key], p.key + ' number of levels');
  let prevLo = p.marks + 1;
  p.levels.forEach(function (lv, i) {
    assert.strictEqual(lv.n, p.levels.length - i, p.key + ' level numbering');
    assert.strictEqual(lv.hi, prevLo - 1, p.key + ' L' + lv.n + ' contiguous');
    assert(lv.lo <= lv.hi);
    prevLo = lv.lo;
    assert(core.need(lv) >= 1 && core.need(lv) <= lv.f.length);
  });
  assert.strictEqual(prevLo, 1, p.key + ' bottom level starts at 1');
});

// --- logic: ticking the features of level L and of every level below it gives level L; nothing gives Level 0 ---
core.PARTS.forEach(function (p) {
  let t = core.emptyTicks(p);
  assert.strictEqual(core.bestFit(p, t), -1, p.key + ' nothing ticked');
  p.levels.forEach(function (lv, li) {
    t = core.emptyTicks(p);
    for (let k = li; k < p.levels.length; k++) for (let j = 0; j < core.need(p.levels[k]); j++) t[k][j] = true;
    assert.strictEqual(core.bestFit(p, t), li, p.key + ' level ' + lv.n + ' met');
    // the same ticks without the level below: a level above the lowest does not count alone
    if (li < p.levels.length - 1) {
      const t2 = core.emptyTicks(p);
      for (let j = 0; j < core.need(lv); j++) t2[li][j] = true;
      assert.strictEqual(core.bestFit(p, t2), -1, p.key + ' level ' + lv.n + ' alone is not met');
      assert(core.blockedAbove(p, t2, p.levels.length - 1), p.key + ' blocked hint');
    }
    // one fewer than needed does not meet it (falls to a lower level or 0)
    if (core.need(lv) >= 1) {
      t = core.emptyTicks(p);
      for (let k = li + 1; k < p.levels.length; k++) for (let j = 0; j < core.need(p.levels[k]); j++) t[k][j] = true;
      for (let j = 0; j < core.need(lv) - 1; j++) t[li][j] = true;
      assert(core.bestFit(p, t) > li || core.bestFit(p, t) === -1, p.key + ' L' + lv.n + ' not met with one missing');
    }
  });
  // everything ticked -> top level; marks
  t = core.emptyTicks(p).map(function (r) { return r.map(function () { return true; }); });
  assert.strictEqual(core.bestFit(p, t), 0, p.key + ' all ticked is top level');
  assert.deepStrictEqual(core.markRange(p, 0, 'convincingly'), [p.marks, p.marks]);
  assert.deepStrictEqual(core.markRange(p, 0, 'just'), [p.levels[0].lo, p.levels[0].lo]);
});

// --- marks within a level ---
const p1a = core.partByKey('p1a'), p2a = core.partByKey('p2a');
assert.deepStrictEqual(core.markRange(p1a, 0, 'adequately'), [13, 14]);   // 12-15: middle marks 13 and 14
assert.deepStrictEqual(core.markRange(p1a, 1, 'adequately'), [9, 10]);    // 8-11
assert.deepStrictEqual(core.markRange(p2a, 0, 'adequately'), [9, 10]);    // 9-10: no middle mark
assert.deepStrictEqual(core.markRange(core.partByKey('p3a'), 3, 'adequately'), [10, 10]); // 9-11: one middle mark
assert.deepStrictEqual(core.markRange(p1a, -1, 'just'), [0, 0]);

// --- what moves it up ---
let t = core.emptyTicks(p1a);
t[1][0] = true; t[1][1] = true;                       // two of three Level 3 features
let nu = core.nextUp(p1a, t, core.bestFit(p1a, t));   // best fit is Level 0 -> next is Level 1
assert.strictEqual(core.bestFit(p1a, t), -1);
assert.strictEqual(nu.level.n, 1);
t[1][2] = true;                                        // all of Level 3, but Level 2 and Level 1 are not met: still Level 0
assert.strictEqual(core.bestFit(p1a, t), -1);
t[2][0] = true; t[3][0] = true;                        // Level 2 (need 1) and Level 1 (need 1) met -> Level 3
assert.strictEqual(core.bestFit(p1a, t), 1);
nu = core.nextUp(p1a, t, core.bestFit(p1a, t));
assert.strictEqual(nu.level.n, 4);
assert.strictEqual(nu.missing.length, 2);
t[0][0] = true; t[0][1] = true;
assert.strictEqual(core.nextUp(p1a, t, core.bestFit(p1a, t)), null);

// the reported case: P1 (a) with only "develops the comparison" and "explains why" ticked is Level 0, not Level 4
t = core.emptyTicks(p1a);
t[0][0] = true; t[0][1] = true;
assert.strictEqual(core.bestFit(p1a, t), -1);
t[3][0] = true;                                        // add only the lowest-level feature: Level 1 met, Levels 2 and 3 not
assert.strictEqual(core.bestFit(p1a, t), 3);
t[2][1] = true;                                        // Level 2 "only asserts" ticked: Level 3 still unmet
assert.strictEqual(core.bestFit(p1a, t), 2);
assert.strictEqual(core.blockedAbove(p1a, t, 1), true);

// --- feature order is stable and complete ---
core.PARTS.forEach(function (p) {
  const o1 = core.featureOrder(p), o2 = core.featureOrder(p);
  assert.deepStrictEqual(o1, o2);
  const total = p.levels.reduce(function (s, lv) { return s + lv.f.length; }, 0);
  assert.strictEqual(o1.length, total);
});

// --- attribute parsing ---
assert.deepStrictEqual(core.parseParts('p1a, P1B ,zz,,p1a'), { keys: ['p1a', 'p1b'], bad: ['zz'] });
assert.deepStrictEqual(core.parseParts(''), { keys: [], bad: [] });

// --- UI wiring ---
function mount(attrs) {
  const el = new Node_('div');
  Object.keys(attrs || {}).forEach(function (k) { el.setAttribute('data-' + k, attrs[k]); });
  registered['hist-levels'](el, {});
  return el;
}
let el = mount({ parts: 'p1a,p1b', start: 'p1b' });
const api = el.__histLevels;
assert.strictEqual(api.current(), 'p1b');
assert(/Level 0/.test(api.text()));
// tick the Level 4 features of part (b) by clicking the checkboxes found in the DOM
const labels = find(el, function (n) { return n.tag === 'label'; });
const p1b = core.partByKey('p1b');
assert.strictEqual(labels.length, p1b.levels.reduce(function (s, lv) { return s + lv.f.length; }, 0));
// tick every checkbox whose text belongs to Level 5 using the click handler
const l5 = p1b.levels[0].f;
labels.forEach(function (lab) {
  const text = lab.children[1].textContent;
  if (l5.indexOf(text) >= 0) { const cb = lab.children[0]; cb.checked = true; cb.onchange(); }
});
assert(/Level 0/.test(api.text()), api.text());   // Level 5 features alone do not count: the levels below are not met
// now the features each lower level needs (every level above the lowest needs the one below it)
labels.forEach(function (lab) {
  const text = lab.children[1].textContent;
  p1b.levels.slice(1).forEach(function (lv) {
    if (lv.f.slice(0, core.need(lv)).indexOf(text) >= 0) { const cb = lab.children[0]; cb.checked = true; cb.onchange(); }
  });
});
assert(/^Level 5 · 23 to 23|^Level 5 · /.test(api.text()), api.text());
assert(/Level 5 · 21 to 25|Level 5 · 22 to 24/.test(api.text()), api.text());
// switch part by clicking its tab, then quality
const tabs = find(el, function (n) { return n.tag === 'button' && /^P1 \(a\)$/.test(n.textContent); });
assert.strictEqual(tabs.length, 1);
tabs[0].onclick();
assert.strictEqual(api.current(), 'p1a');
assert(/Level 0/.test(api.text()));
const q = find(el, function (n) { return n.tag === 'button' && n.textContent === 'Convincingly meets it'; })[0];
q.onclick();
api.tick(0, 0, true); api.tick(0, 1, true);
assert(/^Level 0/.test(api.text()), api.text());              // top-level features alone do not count
api.tick(1, 0, true); api.tick(1, 1, true); api.tick(1, 2, true); api.tick(2, 0, true); api.tick(3, 0, true);
assert(/^Level 4 · 15 of 15/.test(api.text()), api.text());
// bad attributes
el = mount({ parts: 'zz,qq', start: 'nope' });
assert.strictEqual(el.__histLevels.current(), 'p1a');
assert(find(el, function (n) { return n.className === 'w-err'; }).length === 1);
el = mount({});
assert.strictEqual(find(el, function (n) { return n.tag === 'button' && /^P[1-4] /.test(n.textContent); }).length, 8);
// pair total for paper 3
el = mount({ parts: 'p3a,p3b', start: 'p3a' });
const ap = el.__histLevels;
const pa = core.partByKey('p3a');
ap.quality('convincingly');
pa.levels.forEach(function (lv, li) { lv.f.forEach(function (x, j) { ap.tick(li, j, true); }); });
const totalNodes = find(el, function (n) { return n.tag === 'p' && /question total/.test(n.textContent); });
assert(/20 of 40/.test(totalNodes[0].textContent), totalNodes[0].textContent);
ap.select('p3b');
ap.quality('convincingly');
core.partByKey('p3b').levels.forEach(function (lv, li) { lv.f.forEach(function (x, j) { ap.tick(li, j, true); }); });
assert(/40 of 40/.test(totalNodes[0].textContent), totalNodes[0].textContent);
// a single part of a pair offers no total
el = mount({ parts: 'p3a', start: 'p3a' });
assert.strictEqual(find(el, function (n) { return n.tag === 'p' && /question total/.test(n.textContent); }).length, 0);
console.log('hist-levels: all tests passed');
