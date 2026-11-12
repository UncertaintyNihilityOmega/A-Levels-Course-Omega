// Logic test for widgets/hist-essayplan.js: runs the widget against a tiny fake DOM and checks parsing, sorting, ranking, validation, plan text.
const fs = require('fs');
const assert = require('assert');

function node(tag) {
  const n = { tag, children: [], style: {}, attrs: {}, className: '', _text: '', value: '', focused: 0 };
  n.setAttribute = (k, v) => { n.attrs[k] = String(v); };
  n.getAttribute = (k) => (k in n.attrs ? n.attrs[k] : null);
  n.appendChild = (c) => { n.children.push(c); return c; };
  n.focus = () => { n.focused++; };
  n.select = () => {};
  Object.defineProperty(n, 'textContent', {
    get() { return n._text + n.children.map((c) => c.textContent || '').join(''); },
    set(v) { n._text = String(v); n.children = []; }
  });
  return n;
}
global.document = { createElement: node, createTextNode: (t) => ({ textContent: String(t) }) };
global.navigator = {};
let registered = null;
let uid = 0;
global.W = {
  register: (name, fn) => { registered = { name, fn }; },
  frame: () => ({ body: node('div') }),
  uid: (p) => p + '-' + (++uid)
};
eval(fs.readFileSync(__dirname + '/../widgets/hist-essayplan.js', 'utf8'));
assert.strictEqual(registered.name, 'hist-essayplan');

function make(attrs) {
  const el = node('div');
  Object.keys(attrs).forEach((k) => el.setAttribute('data-' + k, attrs[k]));
  registered.fn(el, {});
  return el;
}

const el = make({
  question: 'Q?',
  factors: 'F1 | support | hint one | why one ;; F2 | Challenge | hint two ;; F3 | challenge ;; bad | maybe ;; | support ;; F4 | support | h4 | w4 | extra',
  criteria: 'C1 | C2',
  judgements: 'J1 | J2 | J3'
});
const h = el.__histEssay;
assert.ok(h, 'widget built');
let st = h.state();
assert.deepStrictEqual(st.order, [0, 1, 2, 3], 'four valid factors; two bad ones skipped');
assert.strictEqual(st.status, '0 of 4 factors sorted.');

// parsing
const pf = h.parseFactors('a | support | h ;; b | challenge ;; c | x ;; | support');
assert.strictEqual(pf.factors.length, 2);
assert.strictEqual(pf.problems.length, 2);
assert.strictEqual(h.parseFactors('').factors.length, 0);
assert.strictEqual(h.parseFactors(undefined).factors.length, 0);
const nine = h.parseFactors(Array.from({ length: 9 }, (_, i) => 'f' + i + ' | support').join(' ;; '));
assert.strictEqual(nine.factors.length, 8);
assert.strictEqual(nine.problems.length, 1);
assert.deepStrictEqual(h.parseList('x', ['a', 'b']), ['a', 'b']);
assert.deepStrictEqual(h.parseList('x | y | x', ['a', 'b']), ['x', 'y']);

// build is refused until everything is chosen
assert.strictEqual(h.build(), '');
assert.strictEqual(h.state().status, 'Not yet: 4 factors not sorted, no criterion, no judgement.');
h.setSide(0, 'support'); h.setSide(1, 'challenge'); h.setSide(2, 'challenge');
assert.strictEqual(h.build(), '');
assert.strictEqual(h.state().status, 'Not yet: 1 factor not sorted, no criterion, no judgement.');
// toggling a side twice clears it; bad input is ignored
h.setSide(3, 'support'); assert.strictEqual(h.state().side[3], 'support');
h.setSide(3, 'support'); assert.strictEqual(h.state().side[3], '');
h.setSide(9, 'support'); h.setSide(-1, 'support'); h.setSide(3, 'nonsense');
assert.strictEqual(h.state().side[3], '');
h.setSide(3, 'challenge');   // course says support, so one sorting differs
h.setCriterion(0);
assert.strictEqual(h.build(), '');
assert.strictEqual(h.state().status, 'Not yet: no judgement.');
h.setJudgement(7);           // out of range clears
assert.strictEqual(h.state().judgement, -1);
h.setJudgement(1);

// ranking: move factor 3 to the top, edges do nothing
h.move(3, -1); h.move(3, -1); h.move(3, -1);
assert.deepStrictEqual(h.state().order, [3, 0, 1, 2]);
h.move(3, -1);
assert.strictEqual(h.state().status, 'That factor is already ranked first.');
h.move(2, 1);
assert.strictEqual(h.state().status, 'That factor is already ranked last.');
h.move(99, 1);
assert.deepStrictEqual(h.state().order, [3, 0, 1, 2], 'unknown factor ignored');

// the plan text
const text = h.build();
assert.ok(text.startsWith('QUESTION: Q?'));
assert.ok(text.includes('Line of argument: J2.'));
assert.ok(text.includes('Criterion for the judgement: C1.'));
assert.ok(text.includes('PARAGRAPH 1 (for the view; ranked 2 of 4)'), 'supporting paragraphs come first: F1 is ranked 2');
assert.ok(text.includes('PARAGRAPH 2 (against the view; ranked 1 of 4)'));
assert.ok(text.includes('the factor ranked 1 is "F4"'));
assert.ok(text.includes('Evidence to use: hint one.'));
assert.ok(!text.includes('NOTE: every factor is on one side'));
assert.ok(/sorted differently from the course/.test(h.state().status), 'F4 was sorted differently');
// one-sided plans carry a warning
const el2 = make({ factors: 'a | support ;; b | support' });
const h2 = el2.__histEssay;
h2.setSide(0, 'support'); h2.setSide(1, 'support'); h2.setCriterion(0); h2.setJudgement(0);
assert.ok(h2.build().includes('NOTE: every factor is on one side'));
assert.ok(h2.build().includes('QUESTION: Your question'), 'default question');
// reset
h.reset();
st = h.state();
assert.deepStrictEqual(st.side, ['', '', '', '']);
assert.deepStrictEqual(st.order, [0, 1, 2, 3]);
assert.strictEqual(st.criterion, -1);
// bad attributes: nothing built
assert.strictEqual(make({}).__histEssay, undefined);
assert.strictEqual(make({ factors: 'only | support' }).__histEssay, undefined);
// pure function
assert.ok(h.planText('Q', [{ text: 'A', side: 'support', hint: '', why: '' }, { text: 'B', side: 'challenge', hint: '', why: '' }], [1, 0], ['support', 'challenge'], 'C', 'J').includes('ranked 2 of 2'));
console.log('ok');
