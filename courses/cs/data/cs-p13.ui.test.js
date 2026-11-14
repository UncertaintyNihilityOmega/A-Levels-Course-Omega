// data/cs-p13.ui.test.js: drives the cs-kmap and cs-sched widgets through a minimal fake DOM: presses cells and
// buttons, types in the fields, and checks the messages and results. Run from the course folder: node data/cs-p13.ui.test.js
const path = require('path');
class El {
  constructor(tag) { this.tag = tag; this.children = []; this.attrs = {}; this.style = {}; this.listeners = {}; this._text = ''; this.className = ''; this.value = ''; this.disabled = false; }
  appendChild(c) { this.children.push(c); return c; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  getAttribute(k) { return this.attrs[k]; }
  addEventListener(t, f) { (this.listeners[t] = this.listeners[t] || []).push(f); }
  focus() {}
  set textContent(v) { this.children = []; this._text = String(v); }
  get textContent() { return this._text + this.children.map(function (c) { return c.textContent; }).join(''); }
  fire(t) { (this.listeners[t] || []).forEach(function (f) { f({}); }); }
  all(pred, out) { out = out || []; if (pred(this)) out.push(this); this.children.forEach(function (c) { c.all(pred, out); }); return out; }
  querySelectorAll(sel) {
    if (sel === 'tbody tr') {
      const tb = this.all(function (e) { return e.tag === 'tbody'; })[0];
      return tb ? tb.children.filter(function (c) { return c.tag === 'tr'; }) : [];
    }
    return this.all(function (e) { return e.tag === sel; }).filter(function (e) { return e !== this; }, this);
  }
  querySelector(sel) { return this.querySelectorAll(sel)[0] || null; }
}
global.W = {
  h: function (tag, props) {
    const e = new El(tag);
    props = props || {};
    Object.keys(props).forEach(function (k) {
      if (k === 'class') e.className = props[k];
      else if (k === 'text') e._text = props[k];
      else if (k === 'style') Object.assign(e.style, props[k]);
      else if (k === 'value') e.value = String(props[k]);
      else e.setAttribute(k, props[k]);
    });
    for (let i = 2; i < arguments.length; i++) if (arguments[i]) e.appendChild(arguments[i]);
    return e;
  },
  frame: function (el) { const body = new El('div'); el.appendChild(body); return { root: el, body: body }; },
  say: function () {},
  register: function (name, fn) { global.REG = global.REG || {}; global.REG[name] = fn; }
};
require(path.join(process.cwd(), 'widgets', 'cs-kmap.js'));
require(path.join(process.cwd(), 'widgets', 'cs-sched.js'));
let bad = 0;
const ok = function (c, m) { if (!c) { bad++; console.log('FAIL', m); } };
const byText = function (root, tag, text) { return root.all(function (e) { return e.tag === tag && e._text === text; })[0]; };
const cellButtons = function (root) { return root.all(function (e) { return e.tag === 'button' && /^Cell /.test(e.attrs['aria-label'] || ''); }); };

// ----- cs-kmap
let el = new El('div');
global.REG['cs-kmap'](el, { vars: '3', ones: '3,4,5,7' });
let cells = cellButtons(el);
ok(cells.length === 8, 'eight cells for 3 variables, got ' + cells.length);
ok(el.textContent.indexOf('Press Solve') >= 0, 'start state asks for Solve');
byText(el, 'button', 'Solve').fire('click');
let txt = el.textContent;
ok(txt.indexOf('X = (A AND NOT B) OR (B AND C)') >= 0, 'solution text: ' + txt.slice(0, 200));
ok(txt.indexOf('Group 1: cells 4, 5') >= 0 && txt.indexOf('Group 2: cells 3, 7') >= 0, 'group lines');
cells = cellButtons(el);
ok(cells.some(function (b) { return /^Cell 3,/.test(b.attrs['aria-label']) && /in group 2/.test(b.attrs['aria-label']); }), 'cell 3 labelled with its group');
cells.filter(function (b) { return /^Cell 0,/.test(b.attrs['aria-label']); })[0].fire('click');
ok(el.textContent.indexOf('Press Solve') >= 0 && el.textContent.indexOf('0, 3, 4, 5, 7') >= 0, 'after a press: ' + el.textContent.slice(0, 120));
const typed = el.all(function (e) { return e.tag === 'input'; })[0];
typed.value = '1, 9';
typed.fire('input');
ok(/does not exist on a 3-variable map/.test(el.textContent), 'range message');
typed.value = '1, 3, 5, 7';
typed.fire('input');
byText(el, 'button', 'Solve').fire('click');
ok(el.textContent.indexOf('X = C') >= 0 && el.textContent.indexOf('1 group, 1 literals') >= 0, 'C alone: ' + el.textContent.slice(0, 160));
byText(el, 'button', '4 variables').fire('click');
ok(cellButtons(el).length === 16, 'sixteen cells for 4 variables');
byText(el, 'button', 'Clear the map').fire('click');
ok(el.textContent.indexOf('Every cell is 0') >= 0, 'cleared');
byText(el, 'button', 'Solve').fire('click');
ok(el.textContent.indexOf('X = 0') >= 0, 'empty map solves to 0');
byText(el, 'button', '2 variables').fire('click');
typed.value = '0, 1, 2, 3';
typed.fire('input');
byText(el, 'button', 'Solve').fire('click');
ok(el.textContent.indexOf('X = 1') >= 0, 'all ones is 1: ' + el.textContent.slice(0, 100));
el = new El('div');
global.REG['cs-kmap'](el, { vars: '9', ones: 'abc' });
ok(cellButtons(el).length === 8, 'bad vars falls back to 3');

// ----- cs-sched
el = new El('div');
global.REG['cs-sched'](el, { algo: 'rr', q: '2', procs: 'A:0:5,B:1:3,C:2:8,D:3:2' });
txt = el.textContent;
ok(txt.indexOf('Average waiting time 7.25 (29/4)') >= 0, 'RR average: ' + txt.slice(-260));
ok(txt.indexOf('Context switches: 8') >= 0, 'RR switches');
byText(el, 'button', 'SRT').fire('click');
ok(el.textContent.indexOf('Average waiting time 3.5 (7/2)') >= 0, 'SRT average');
byText(el, 'button', 'FCFS').fire('click');
ok(el.textContent.indexOf('Average waiting time 5.75 (23/4)') >= 0, 'FCFS average');
byText(el, 'button', 'SJF').fire('click');
ok(el.textContent.indexOf('Average waiting time 4. Average turnaround') >= 0, 'SJF average: ' + el.textContent.slice(-200));
let inputs = el.all(function (e) { return e.tag === 'input'; });
inputs[2].value = '0';
inputs[2].fire('input');
ok(/burst time of A must be a whole number from 1 to 99/.test(el.textContent), 'burst error');
inputs[2].value = '12';
inputs[2].fire('input');
ok(!/must be a whole number/.test(el.textContent), 'error cleared');
const add = byText(el, 'button', 'Add a process');
add.fire('click');
ok(el.querySelectorAll('tbody tr').length >= 5, 'a fifth process row');
add.fire('click');
add.fire('click');
ok(add.disabled === true, 'add disabled at 6 processes');
inputs = el.all(function (e) { return e.tag === 'input'; });
inputs[0].value = 'B';
inputs[0].fire('input');
ok(/name B is used twice/.test(el.textContent), 'duplicate name message');
el = new El('div');
global.REG['cs-sched'](el, { algo: 'zzz', q: '99', procs: 'bad' });
ok(el.textContent.indexOf('Average waiting time') >= 0, 'bad attributes still draw');
console.log(bad ? bad + ' failures' : 'ui tests passed');
process.exit(bad ? 1 : 0);
