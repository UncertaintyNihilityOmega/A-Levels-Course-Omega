// Logic test for widgets/hist-sort.js: runs the widget against a tiny fake DOM and checks parsing, choosing, checking, reset and shuffle.
const fs = require('fs');
const assert = require('assert');

function node(tag) {
  const n = { tag, children: [], style: {}, attrs: {}, className: '', _text: '' };
  n.setAttribute = (k, v) => { n.attrs[k] = String(v); };
  n.getAttribute = (k) => (k in n.attrs ? n.attrs[k] : null);
  n.appendChild = (c) => { n.children.push(c); return c; };
  Object.defineProperty(n, 'textContent', {
    get() { return n._text + n.children.map((c) => c.textContent || '').join(''); },
    set(v) { n._text = String(v); n.children = []; }
  });
  return n;
}
global.document = { createElement: node, createTextNode: (t) => ({ textContent: String(t) }) };
let registered = null;
let uid = 0;
global.W = {
  register: (name, fn) => { registered = { name, fn }; },
  frame: (el) => ({ body: node('div') }),
  uid: (p) => p + '-' + (++uid),
  shuffle: (a) => a.slice().reverse()
};
eval(fs.readFileSync(__dirname + '/../widgets/hist-sort.js', 'utf8'));
assert.strictEqual(registered.name, 'hist-sort');

function make(attrs) {
  const el = node('div');
  Object.keys(attrs).forEach((k) => el.setAttribute('data-' + k, attrs[k]));
  registered.fn(el, {});
  return el;
}

const good = make({
  title: 'T',
  cats: 'A,B,C',
  items: 's1 | A | because one ;; s2 | B | because two ;; s3 | C ;; bad | Z | nope ;; s4 | A | with | pipe'
});
const h = good.__histSort;
assert.ok(h, 'widget built');
let st = h.state();
assert.deepStrictEqual(st.choice, [-1, -1, -1, -1], 'four valid statements (the one with category Z is skipped)');
assert.strictEqual(st.score, '0 of 4 answered.');

// parsing
assert.deepStrictEqual(h.parseCats('A, B ,A,, C').cats, ['A', 'B', 'C']);
assert.strictEqual(h.parseCats('A').problems.length, 1);
const six = h.parseCats('1,2,3,4,5,6');
assert.strictEqual(six.cats.length, 5);
assert.strictEqual(six.problems.length, 1);
const pi = h.parseItems('x | A | e1 | e2 ;; y | Q | e ;; | A | e ;; z | B', ['A', 'B']);
assert.strictEqual(pi.items.length, 2);
assert.strictEqual(pi.items[0].why, 'e1 | e2', 'extra pipes stay in the explanation');
assert.strictEqual(pi.problems.length, 2);
assert.strictEqual(h.parseItems('', ['A']).items.length, 0);
assert.strictEqual(h.parseItems(undefined, ['A']).items.length, 0);

// choosing: right, wrong, unanswered, toggle off, out-of-range ignored
h.choose(0, 0);           // s1 right
h.choose(1, 0);           // s2 wrong (correct is B)
h.choose(9, 0); h.choose(0, 9); h.choose(-1, 0);
st = h.state();
assert.deepStrictEqual(st.choice, [0, 0, -1, -1]);
assert.strictEqual(st.score, '2 of 4 answered.');
h.choose(1, 0);           // pressing again clears
assert.strictEqual(h.state().choice[1], -1);
h.choose(1, 1);           // s2 right now
h.check();
st = h.state();
assert.ok(st.shown.every(Boolean));
assert.strictEqual(st.score, 'Score: 2 of 4 right. 2 not answered.');
h.choose(2, 0);           // s3 wrong (correct is C), after a check
st = h.state();
assert.strictEqual(st.shown[2], false, 'result for a changed statement is hidden');
assert.strictEqual(st.score, 'Choices changed. Press Check to see your score.');
h.choose(2, 2); h.choose(3, 0);
h.check();
assert.strictEqual(h.state().score, 'Score: 4 of 4 right.');

// shuffle keeps the choices; reset clears everything and restores the order
h.shuffle();
assert.deepStrictEqual(h.state().order, [3, 2, 1, 0]);
assert.deepStrictEqual(h.state().choice, [0, 1, 2, 0]);
h.reset();
st = h.state();
assert.deepStrictEqual(st.order, [0, 1, 2, 3]);
assert.deepStrictEqual(st.choice, [-1, -1, -1, -1]);
assert.ok(st.shown.every((s) => !s));
assert.strictEqual(st.score, '0 of 4 answered.');

// bad attributes never throw and show a message
for (const attrs of [{}, { cats: 'A' }, { cats: 'A,B' }, { cats: 'A,B', items: 'x | Z' }, { items: 'x | A' }]) {
  const e = make(attrs);
  assert.strictEqual(e.__histSort, undefined, JSON.stringify(attrs));
}
// two widgets on one page do not share state
const a = make({ cats: 'A,B', items: 'x | A' }).__histSort;
const b = make({ cats: 'A,B', items: 'x | A' }).__histSort;
a.choose(0, 0);
assert.deepStrictEqual(b.state().choice, [-1]);
console.log('hist-sort logic ok');
