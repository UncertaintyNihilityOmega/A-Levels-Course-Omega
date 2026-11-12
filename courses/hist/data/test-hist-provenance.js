// Logic test for widgets/hist-provenance.js: runs the widget against a tiny fake DOM and checks parsing, choosing, checking, reset.
const fs = require('fs');
const assert = require('assert');

function node(tag) {
  const n = { tag, children: [], style: {}, attrs: {}, className: '', _text: '', value: '' };
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
  frame: () => ({ body: node('div') }),
  uid: (p) => p + '-' + (++uid)
};
eval(fs.readFileSync(__dirname + '/../widgets/hist-provenance.js', 'utf8'));
assert.strictEqual(registered.name, 'hist-provenance');

function make(attrs) {
  const el = node('div');
  Object.keys(attrs).forEach((k) => el.setAttribute('data-' + k, attrs[k]));
  registered.fn(el, {});
  return el;
}

const good = make({
  question: 'Q?',
  sources: 'A | prov A | text A ;; B | prov B | text B with | a pipe ;; C | only two fields ;; | no label | x',
  answers: 'A | stronger | because a | Speech | Leader or decision-maker | Persuade ;; B | weak | because b | Cartoon or poster | Outside observer | Mock or criticise ;; Z | stronger | unknown source ;; A2 | maybe | bad verdict',
  purposes: 'Persuade | Mock or criticise'
});
const h = good.__histProv;
assert.ok(h, 'widget built');
assert.strictEqual(h.state().state.length, 2, 'two valid sources (C and the unlabelled one are skipped)');
assert.strictEqual(h.state().score, '0 of 2 sources fully answered.');

// parsing
const ps = h.parseSources('A | p | t ;; B | p | t | u ;; C | p ;; | p | t');
assert.strictEqual(ps.sources.length, 2);
assert.strictEqual(ps.sources[1].text, 't | u', 'extra pipes stay in the content');
assert.strictEqual(ps.problems.length, 2);
assert.strictEqual(h.parseSources('').sources.length, 0);
assert.strictEqual(h.parseSources(undefined).sources.length, 0);
const pa = h.parseAnswers('A | Stronger | why ;; b | weaker ;; X | stronger ;; A | maybe', ['A', 'B']);
assert.strictEqual(Object.keys(pa.answers).length, 2);
assert.strictEqual(pa.answers.b.verdict, 'weaker');
assert.strictEqual(pa.problems.length, 2, 'unknown label and bad verdict');
assert.deepStrictEqual(h.parseList('a | b | a | | c', ['x', 'y']), ['a', 'b', 'c']);
assert.deepStrictEqual(h.parseList('only', ['x', 'y']), ['x', 'y'], 'a list of fewer than two falls back to the defaults');
assert.ok(h.lists.purpose.length === 2 && h.lists.nature.indexOf('Speech') >= 0 && h.lists.nature.indexOf('Cartoon or poster') >= 0);

// choosing: all right for A, mixed for B
const nat = h.lists.nature, org = h.lists.origin, pur = h.lists.purpose;
h.setTag(0, 'nature', nat.indexOf('Speech'));
h.setTag(0, 'origin', org.indexOf('Leader or decision-maker'));
h.setTag(0, 'purpose', pur.indexOf('Persuade'));
h.setVerdict(0, 'stronger');
h.setTag(1, 'nature', nat.indexOf('Speech'));        // wrong (model: Cartoon or poster)
h.setVerdict(1, 'stronger');                          // wrong (model: weaker)
assert.strictEqual(h.state().score, '1 of 2 sources fully answered.');
h.check();
let st = h.state();
assert.ok(st.checked);
assert.strictEqual(st.score, 'Score: judgements 1 of 2 right; tags 3 of 6 right.');
// toggling a verdict off clears it, out-of-range choices are ignored, and a change after checking marks the score stale
h.setVerdict(1, 'stronger');
assert.strictEqual(h.state().state[1].verdict, '');
assert.strictEqual(h.state().score, 'Choices changed. Press Check to see your score.');
h.setTag(5, 'nature', 0); h.setTag(0, 'bogus', 0); h.setTag(0, 'nature', 99); h.setVerdict(0, 'bogus'); h.setVerdict(-1, 'weaker');
assert.strictEqual(h.state().state[0].nature, -1, 'index 99 clears the choice');
assert.strictEqual(h.state().state[0].verdict, '', 'bogus verdict toggles off nothing new');
h.reset();
st = h.state();
assert.strictEqual(st.checked, false);
assert.deepStrictEqual(st.state.map((s) => [s.nature, s.origin, s.purpose, s.verdict]), [[-1, -1, -1, ''], [-1, -1, -1, '']]);

// bad attributes: no sources, no answers, empty everything
const none = make({});
assert.strictEqual(none.__histProv, undefined, 'no widget without sources');
const noans = make({ sources: 'A | p | t' });
noans.__histProv.setVerdict(0, 'weaker');
noans.__histProv.check();
assert.ok(/judgements 0 of 0/.test(noans.__histProv.state().score));
// a model tag outside the lists is added to the list
const extra = make({ sources: 'A | p | t', answers: 'A | stronger | w | Telegram | Spy | Bribe' });
assert.ok(extra.__histProv.lists.nature.indexOf('Telegram') >= 0 && extra.__histProv.lists.purpose.indexOf('Bribe') >= 0);
console.log('ok');
