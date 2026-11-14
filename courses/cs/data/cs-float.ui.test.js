// data/cs-float.ui.test.js: drives the cs-float widget's bit buttons, field, Normalise, Reset and sliders through a
// minimal fake DOM and checks the messages and readouts. Run: node data/cs-float.ui.test.js
const path = require('path');

class El {
  constructor(tag) { this.tag = tag; this.children = []; this.attrs = {}; this.style = {}; this.listeners = {}; this._text = ''; this.className = ''; this.value = ''; this.placeholder = ''; }
  appendChild(c) { this.children.push(c); return c; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  getAttribute(k) { return this.attrs[k]; }
  addEventListener(t, f) { (this.listeners[t] = this.listeners[t] || []).push(f); }
  focus() {}
  set textContent(v) { this.children = []; this._text = String(v); }
  get textContent() { return this._text + this.children.map(function (c) { return c.textContent; }).join(''); }
  fire(t, ev) { (this.listeners[t] || []).forEach(function (f) { f(ev || {}); }); }
  all(pred, out) { out = out || []; if (pred(this)) out.push(this); this.children.forEach(function (c) { c.all(pred, out); }); return out; }
}
let sliders = [];
let readout = null;
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
  sliderNum: function (o) {
    const s = { el: new El('div'), val: o.value, oninput: o.oninput, get: function () { return s.val; }, set: function (v) { s.val = v; } };
    sliders.push(s);
    return s;
  },
  readout: function (rows) {
    const r = { el: new El('table'), vals: {}, set: function (k, t) { r.vals[k] = t; } };
    readout = r;
    return r;
  },
  say: function () {},
  register: function (name, fn) { global.__init = fn; }
};
require(path.join(__dirname, '..', 'widgets', 'cs-float.js'));

let n = 0;
function eq(a, b, label) { if (JSON.stringify(a) !== JSON.stringify(b)) { console.error('FAIL ' + label + '\n  got  ' + JSON.stringify(a) + '\n  want ' + JSON.stringify(b)); process.exit(1); } n++; }
function mount(opts) {
  sliders = [];
  const root = new El('div');
  global.__init(root, opts);
  const ro = readout;
  const q = {
    root: root, ro: ro, sliders: sliders,
    button: function (text) { const b = root.all(function (x) { return x.tag === 'button' && x._text === text; })[0]; if (!b) throw new Error('no button ' + text); return b; },
    input: root.all(function (x) { return x.tag === 'input'; })[0],
    msgs: function () { return root.all(function (x) { return x.attrs['aria-live'] === 'polite' && x.className === 'w-note'; }); },
    note: function () { return root.all(function (x) { return x.attrs['aria-live'] === 'polite' && x.className === 'w-note'; })[1].textContent; },
    err: function () { const e = root.all(function (x) { return x.className === 'w-err'; })[0]; return e.style.display === 'none' ? '' : e.textContent; },
    bits: function () { return root.all(function (x) { return x.tag === 'button' && x.attrs['aria-pressed'] !== undefined && /bit /.test(x.attrs['aria-label'] || ''); }); },
    pattern: function () { return ro.vals.pattern; },
    click: function (text) { q.button(text).fire('click'); },
    type: function (v) { q.input.value = v; }
  };
  return q;
}

// start state
let q = mount({ m: '8', e: '4', bits: '00011010 0100' });
eq(q.pattern(), '00011010 0100', 'initial pattern');
eq(q.ro.vals.dec, '3.25', 'initial decimal');
eq(q.ro.vals.mant, '0.0011010 = 13/64 = 0.203125', 'mantissa row');
eq(q.ro.vals.exp, '0100 = 4', 'exponent row');
eq(q.ro.vals.norm.slice(0, 14), 'Not normalised', 'not normalised');
eq(q.bits().length, 12, '12 bit buttons');
eq(q.ro.vals.big, '01111111 0111 = 127', 'largest');
eq(q.ro.vals.small, '01000000 1000 = 1/512 = 0.001953125', 'smallest');
eq(q.ro.vals.neg, '10000000 0111 = ' + '−128', 'most negative');

// Normalise twice, then it says so
q.click('Normalise (one step)');
eq(q.pattern(), '00110100 0011', 'first shift');
eq(q.msgs()[1].textContent.slice(0, 30), 'Shifted the mantissa left one ', 'shift message');
q.click('Normalise (one step)');
eq(q.pattern(), '01101000 0010', 'second shift');
eq(q.ro.vals.dec, '3.25', 'value unchanged');
eq(q.ro.vals.norm.slice(0, 11), 'Normalised:', 'normalised');
q.click('Normalise (one step)');
eq(q.msgs()[1].textContent.slice(0, 18), 'Already normalised', 'already normalised');

// flip a bit with a button (the first mantissa bit is the sign bit)
q.bits()[0].fire('click');
eq(q.pattern(), '11101000 0010', 'sign bit flipped');
eq(q.ro.vals.dec, '−0.75', 'negative value');
eq(q.bits()[0].attrs['aria-pressed'], 'true', 'button pressed');
eq(/now 1$/.test(q.bits()[0].attrs['aria-label']), true, 'label says now 1');
q.bits()[0].fire('click');
eq(q.pattern(), '01101000 0010', 'flipped back');

// exponent bit buttons come after the mantissa buttons
q.bits()[8].fire('click');                       // exponent sign bit: 1010 = -6
eq(q.pattern(), '01101000 1010', 'exponent sign bit');
eq(q.ro.vals.exp, '1010 = −6', 'exponent -6');
q.bits()[8].fire('click');

// typed values
q.type('0.1'); q.click('Store this value');
eq(q.pattern(), '01100110 1101', '0.1 stored');
eq(q.msgs()[1].textContent, '0.1 cannot be stored exactly. The nearest value is 0.099609375. The rounding error is 0.000390625 (0.39%): the stored value is too small.', 'rounding message');
q.type('6.25'); q.input.fire('keydown', { key: 'Enter', preventDefault: function () {} });
eq(q.pattern(), '01100100 0011', 'Enter stores 6.25');
eq(q.msgs()[1].textContent, '6.25 is stored exactly.', 'exact message');
q.type('300'); q.click('Store this value');
eq(q.pattern(), '01100100 0011', 'overflow leaves the pattern');
eq(q.msgs()[1].textContent.slice(0, 9), 'Overflow:', 'overflow message');
q.type('-300'); q.click('Store this value');
eq(q.msgs()[1].textContent.indexOf('more negative') > 0, true, 'negative overflow wording');
q.type('0.001'); q.click('Store this value');
eq(q.pattern(), '00000000 0000', 'underflow stores zero');
eq(q.msgs()[1].textContent.slice(0, 10), 'Underflow:', 'underflow message');
eq(q.ro.vals.norm.slice(0, 22), 'Not normalised: zero: ', 'zero is not normalised');
q.click('Normalise (one step)');
eq(q.msgs()[1].textContent.slice(0, 13), 'Zero cannot b', 'zero cannot be normalised');
q.type('0'); q.click('Store this value');
eq(q.msgs()[1].textContent.slice(0, 20), '0 is stored as all z', 'zero message');
q.type('abc'); q.click('Store this value');
eq(q.err().slice(0, 12), 'Use digits, ', 'bad input message');
q.type(''); q.click('Store this value');
eq(q.err().slice(0, 12), 'Type a denar', 'empty input message');
q.type('-4'); q.click('Store this value');
eq(q.err(), '', 'error cleared');
eq(q.pattern(), '10000000 0010', '-4 stored');
eq(q.ro.vals.mant, '1.0000000 = −1', 'mantissa -1');

// changing the format keeps the value
q.sliders[0].set(9); q.sliders[0].oninput();
eq(q.bits().length, 9 + 4, '13 bit buttons');
eq(q.pattern(), '100000000 0010', 'same value in 9 + 4');
eq(q.msgs()[1].textContent.slice(0, 15), 'Format changed ', 'format message');
q.sliders[1].set(3); q.sliders[1].oninput();
eq(q.pattern(), '100000000 010', '-4 in 9 + 3');
q.type('0.1'); q.click('Store this value');
q.sliders[0].set(6); q.sliders[0].oninput();
eq(q.msgs()[1].textContent.indexOf('rounded') > 0, true, 'rounding mentioned when the format shrinks');
q.sliders[0].set(16); q.sliders[1].set(8); q.sliders[0].oninput();
eq(q.bits().length, 24, '24 bit buttons');
q.type('0.1'); q.click('Store this value');
eq(q.ro.vals.dec.slice(0, 7), '0.09999', '0.1 in 16 + 8 is much closer');

// reset
q.click('Reset');
eq(q.pattern(), '00011010 0100', 'reset to the start');
eq(q.sliders[0].get(), 8, 'slider reset');
eq(q.bits().length, 12, '12 buttons again');

// bad attributes
q = mount({ m: 'x', e: '-5', bits: 'junk' });
eq(q.bits().length, 8 + 3, 'clamped sizes');
q = mount({});
eq(q.pattern(), '01011000 0011', 'default pattern is 5.5');
q = mount({ bits: '1000 1000' });
eq(q.bits().length, 12, 'too-short groups fall back to the default 8 + 4');

console.log('cs-float ui ok: ' + n + ' checks');
