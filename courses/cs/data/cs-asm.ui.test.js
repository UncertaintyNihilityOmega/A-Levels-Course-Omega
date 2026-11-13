// data/cs-asm.ui.test.js: drives the cs-asm widget (its buttons and tabs) in Node with a tiny fake DOM and checks the
// registers, the memory table and the messages after Step, Run, Reset, a changed program and bad input.
// Run: node data/cs-asm.ui.test.js
const path = require('path');
class E {
  constructor(tag) { this.tag = tag; this.children = []; this.attrs = {}; this.style = {}; this.listeners = {}; this._text = ''; this.value = ''; this.disabled = false; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  appendChild(c) { this.children.push(c); return c; }
  addEventListener(t, f) { (this.listeners[t] = this.listeners[t] || []).push(f); }
  click() { (this.listeners.click || []).forEach((f) => f()); }
  fire(t) { (this.listeners[t] || []).forEach((f) => f()); }
  set textContent(t) { this.children = []; this._text = String(t); }
  get textContent() { return this._text + this.children.map((c) => c.textContent).join(''); }
}
let registered = null;
const said = [];
global.W = {
  register(n, f) { registered = f; },
  h(tag, props) {
    const e = new E(tag);
    Object.keys(props || {}).forEach((k) => {
      if (k === 'style') Object.assign(e.style, props[k]);
      else if (k === 'text') e._text = props[k];
      else if (k === 'class') e.attrs.class = props[k];
      else if (k === 'value') e.attrs.value = props[k];
      else e.attrs[k] = props[k];
    });
    for (let i = 2; i < arguments.length; i++) if (arguments[i]) e.children.push(arguments[i]);
    return e;
  },
  frame(el) { const body = new E('div'); el.appendChild(body); return { root: el, body }; },
  readout(rows) { const vals = {}; const el = new E('div'); return { el, set(k, t) { vals[k] = t; }, vals }; },
  say(el, t) { said.push(t); },
  reducedMotion() { return true; }
};
require(path.join(__dirname, '..', 'widgets', 'cs-asm.js'));
let ro;
const origReadout = W.readout;
W.readout = function (rows) { ro = origReadout(rows); return ro; };

function find(e, pred, out) { out = out || []; if (pred(e)) out.push(e); e.children.forEach((c) => find(c, pred, out)); return out; }
function make(opts) {
  const root = new E('div');
  registered(root, opts);
  return root;
}
let checks = 0;
function eq(label, got, want) { checks++; if (got !== want) { console.error('FAIL ' + label + ': got ' + JSON.stringify(got) + ', want ' + JSON.stringify(want)); process.exit(1); } }
function btn(root, text) { return find(root, (e) => e.tag === 'button' && e.textContent === text)[0]; }
function memRows(root) { return find(root, (e) => e.tag === 'tr').slice(1).map((r) => r.children.map((c) => c.textContent)); }

// ---- fetch-execute mode on the sum program
let root = make({ program: 'sum', mode: 'fe' });
eq('start PC', ro.vals.PC, '100');
const step = () => btn(root, 'Step').click();
for (let i = 0; i < 4; i++) step();
eq('after fetch: PC', ro.vals.PC, '101'); eq('after fetch: MAR', ro.vals.MAR, '100'); eq('after fetch: MDR', ro.vals.MDR, 'LDD 200'); eq('after fetch: CIR', ro.vals.CIR, 'LDD 200');
for (let i = 0; i < 3; i++) step();
eq('after LDD: ACC', ro.vals.ACC, '7'); eq('after LDD: MAR', ro.vals.MAR, '200');
for (let i = 0; i < 7; i++) step();
eq('after ADD: ACC', ro.vals.ACC, '12');
for (let i = 0; i < 7; i++) step();
const m202 = memRows(root).find((r) => r[0] === '202');
eq('STO wrote 202', m202[2].indexOf('12') === 0, true);
eq('changed flag', m202[3].indexOf('changed') >= 0, true);
step(); step(); step(); step(); step();
eq('ended message', said[said.length - 1].indexOf('has ended') >= 0, true);
step();
eq('stays ended', said[said.length - 1].indexOf('has ended') >= 0, true);
btn(root, 'Reset').click();
eq('reset PC', ro.vals.PC, '100'); eq('reset ACC', ro.vals.ACC, '0');

// ---- whole-instruction mode and Run
root = make({ program: 'countdown', mode: 'run' });
btn(root, 'Whole instructions').click();
btn(root, 'Step').click();
eq('LDM executed', ro.vals.ACC, '53'); eq('PC after one instruction', ro.vals.PC, '101');
btn(root, 'Run').click();
eq('countdown output', find(root, (e) => e.attrs['aria-live'] === 'polite' && e.attrs.style === undefined && e.style.minHeight)[0].textContent, '54321');
btn(root, 'Run').click(); // after the end: resets and runs again
eq('run again output', find(root, (e) => e.style.minHeight === '1.4em')[0].textContent, '54321');

// ---- IN with the keyboard buffer, an edited program, bad programs
root = make({ program: 'upper', mode: 'run' });
btn(root, 'Run').click();
eq('upper output', find(root, (e) => e.style.minHeight === '1.4em')[0].textContent, 'Q');
const ta = find(root, (e) => e.tag === 'textarea')[0];
ta.value = '100 LDM #9\n101 ADD #1\n102 STO 150\n103 END';
ta.fire('input');
btn(root, 'Step').click();
eq('edited program loaded on Step', ro.vals.ACC, '9');
ta.value = '100 LDM #9\n101 FOO 3\n102 END';
ta.fire('input');
btn(root, 'Reset').click();
const errEl = find(root, (e) => e.attrs.class === 'w-err')[0];
eq('parse error names the line', errEl.textContent.indexOf('line 2') >= 0, true);
btn(root, 'Step').click(); btn(root, 'Run').click(); // must not throw
ta.value = '100 LOOP: JMP LOOP';
ta.fire('input');
btn(root, 'Run').click();
eq('step limit message', errEl.textContent.indexOf('step limit') >= 0, true);
ta.value = '100 IN\n101 END';
ta.fire('input');
find(root, (e) => e.tag === 'input')[0].value = '';
btn(root, 'Run').click();
eq('empty buffer message', errEl.textContent.indexOf('keyboard buffer') >= 0, true);

// ---- bad attributes
root = make({ program: 'zzz', mode: '??', bits: '99', input: '<b>x</b>' });
eq('bad program falls back to sum', ro.vals.PC, '100');
btn(root, 'Step').click();
console.log('ok: ' + checks + ' checks');
