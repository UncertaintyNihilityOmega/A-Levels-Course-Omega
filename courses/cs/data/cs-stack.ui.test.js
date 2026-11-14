// data/cs-stack.ui.test.js: drives the widget's buttons, tabs and field through a minimal fake DOM and checks the
// messages, tables and focus. Run: node data/cs-stack.ui.test.js
const path = require('path');

class El {
  constructor(tag) { this.tag = tag; this.children = []; this.attrs = {}; this.style = {}; this.listeners = {}; this._text = ''; this.className = ''; this.value = ''; this.focused = false; }
  appendChild(c) { this.children.push(c); return c; }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  getAttribute(k) { return this.attrs[k]; }
  addEventListener(t, f) { (this.listeners[t] = this.listeners[t] || []).push(f); }
  focus() { this.focused = true; El.lastFocus = this; }
  set textContent(v) { this.children = []; this._text = String(v); }
  get textContent() { return this._text + this.children.map(function (c) { return c.textContent; }).join(''); }
  fire(t, ev) { (this.listeners[t] || []).forEach(function (f) { f(ev || {}); }); }
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
const S = require(path.join(__dirname, '..', 'widgets', 'cs-stack.js'));

let n = 0;
function eq(a, b, label) { if (JSON.stringify(a) !== JSON.stringify(b)) { console.error('FAIL ' + label + '\n  got  ' + JSON.stringify(a) + '\n  want ' + JSON.stringify(b)); process.exit(1); } n++; }
function mount(opts) {
  const root = new El('div');
  global.__init(root, opts);
  const q = {
    root: root,
    button: function (text) { const b = root.all(function (x) { return x.tag === 'button' && x._text === text; })[0]; if (!b) throw new Error('no button ' + text); return b; },
    input: root.all(function (x) { return x.tag === 'input'; })[0],
    msg: function () { return root.all(function (x) { return x.attrs['aria-live'] === 'polite'; })[0]; },
    rows: function () { return root.all(function (x) { return x.tag === 'tr'; }).slice(1).map(function (tr) { return tr.children.map(function (c) { return c.textContent; }); }); },
    notes: function () { return root.all(function (x) { return x.className === 'w-note'; }).map(function (x) { return x.textContent; }); },
    click: function (text) { q.button(text).fire('click'); },
    type: function (v) { q.input.value = v; }
  };
  return q;
}

// Stack
let q = mount({ type: 'stack', size: '5', items: '12,7,30' });
eq(q.rows()[2], ['3', '30', '← Top'], 'initial top row');
q.type('5'); q.click('Push');
eq(q.msg().textContent, 'Pushed 5 at index 4; TopPointer = 4.', 'push message');
eq(q.input.value, '', 'field cleared after push');
q.click('Pop'); q.click('Pop');
eq(q.msg().textContent.slice(0, 14), 'Popped 30 from', 'pop message');
eq(q.rows().map(function (r) { return r[1]; }), ['12', '7', '(30)', '(5)', ''], 'stale values in brackets');
q.click('Peek');
eq(q.msg().textContent, 'Peek: the top item is 7 at index 2. TopPointer is unchanged (2).', 'peek');
q.type(''); q.click('Push');
eq([q.msg().className, q.msg().textContent], ['w-err', 'Type a value first (a number or a short word).'], 'empty input message');
eq(El.lastFocus, q.input, 'focus returns to the field');
q.type('a'.repeat(13)); q.click('Push');
eq(q.msg().className, 'w-err', 'too long');
q.type('9'); q.input.fire('keydown', { key: 'Enter', preventDefault: function () {} });
eq(q.msg().textContent, 'Pushed 9 at index 3; TopPointer = 3.', 'Enter pushes');
q.type('1'); q.click('Push'); q.type('2'); q.click('Push'); q.type('3'); q.click('Push');
eq([q.msg().className, q.msg().textContent.slice(0, 15)], ['w-err', 'Stack overflow:'], 'overflow message');
q.click('Empty');
q.click('Pop');
eq([q.msg().className, q.msg().textContent.slice(0, 16)], ['w-err', 'Stack underflow:'], 'underflow message');
q.click('Reset');
eq(q.rows().map(function (r) { return r[1]; }), ['12', '7', '30', '', ''], 'reset');

// Tabs keep separate states; pressed state follows the click
q.click('Linked list');
eq(q.button('Linked list').attrs['aria-pressed'], 'true', 'tab pressed');
eq(q.button('Stack').attrs['aria-pressed'], 'false', 'old tab not pressed');
q.type('Chen'); q.click('Insert in order');
eq(q.msg().textContent.slice(0, 40), 'Inserted Chen at index 4 after Bilal (in', 'list insert message');
eq(q.rows()[2], ['3', 'Bilal', '4', '← Start'], 'list row 3');
eq(q.rows()[4], ['5', '', '0', '← Free'], 'free marker');
q.type('Dina'); q.click('Find');
eq(q.msg().textContent, 'Found Dina at index 1 after visiting 3 nodes: Bilal (3), Chen (4), Dina (1).', 'find');
q.type('Zara'); q.click('Delete');
eq([q.msg().className, q.msg().textContent], ['w-err', 'Zara is not in the list, so nothing was deleted.'], 'delete missing');
q.type('Dina'); q.click('Delete');
eq(q.rows()[0], ['1', '(Dina)', '5', '← Free'], 'deleted node is free with stale data');
q.click('Stack');
eq(q.rows()[2], ['3', '30', '← Top'], 'stack state kept');

// Circular queue
q = mount({ type: 'circular', size: '6', items: 'J1,J2,J3,J4,J5,J6' });
q.click('Dequeue'); q.click('Dequeue'); q.click('Dequeue');
q.type('J7'); q.click('Enqueue');
eq(q.msg().textContent, 'Enqueued J7 at index 1; RearPointer = 1, Count = 4.', 'circular wrap');
eq(q.rows().map(function (r) { return r[1]; }), ['J7', '(J2)', '(J3)', 'J4', 'J5', 'J6'], 'circular cells');
eq(q.rows()[0][2], '← Rear', 'rear marker'); eq(q.rows()[3][2], '← Front', 'front marker');
q.click('Queue');
for (let k = 0; k < 4; k++) { q.type('x'); q.click('Enqueue'); }
eq(q.msg().textContent.slice(0, 11), 'Queue full:', 'linear queue full');

// Bad attributes
q = mount({ type: 'zzz', size: 'abc', base: '5', items: ',,' });
eq(q.rows().length, 8, 'default size 8');
q = mount({ type: 'list', size: '99', base: '0', items: 'x' });
eq(q.rows().length, 12, 'size capped at 12');
eq(q.rows()[0], ['0', 'x', '-1', '← Start'], 'base 0');
q = mount({ type: 'queue', size: '1' });
eq(q.rows().length, 3, 'size at least 3');
q = mount({});
eq(q.rows().length, 8, 'no attributes');
console.log('cs-stack ui: ' + n + ' checks passed');
