// test.js — engine self-test: builds a tiny in-memory course and checks what the engine must keep doing.
//   node engine/test.js        exit 1 if any check fails (run in CI before the real build)
// It guards the 380+ written chapters against an engine change that silently alters every page.
'use strict';
const { buildSite } = require('./site');
const { lintChapter } = require('./lint');
const assets = require('./assets');

let fails = 0, n = 0;
function ok(cond, what) { n++; if (!cond) { fails++; console.log(' FAIL ' + what); } }

const ONE = `@chapter tst.one
@title Forces and motion
@level as
@paper P1
@time 2 hours
@summary A test chapter.

:::why
Why it matters.
:::

Speed is \\(v = \\dfrac{s}{t}\\) and water is \\(\\ce{H2O}\\). See [the second chapter](#tst.two), the
[old name](#tst.old), a [planned chapter](#tst.three) and [its section](#tst.two--more).

:::def Velocity
The rate of change of displacement.
:::

:::key Speed
\\[v = \\frac{s}{t}\\]
:::

:::eg [2 marks] Find the speed
\\(v = 10 / 2\\) [M1]

\\(v = 5\\,\\mathrm{m\\,s^{-1}}\\) [A1]
:::

:::try Practice
Q: [3 marks] (#tst.two) Solve \\(2x = 6\\).
H: Divide both sides by 2.
A: \\(2x = 6\\) [M1] so \\(x = 3\\) [A1] [A1]
Q: What is \\(1 + 1\\)?
A: 2
:::

:::quiz Check
? Which is a vector?
- speed
+ velocity
- mass
> Velocity has a direction.
:::

:::html
<div class="widget" data-w="tst-missing"></div>
<svg viewBox="0 0 10 10" role="img" aria-label="A dot"><circle cx="5" cy="5" r="2" class="f-ink"/></svg>
:::

:::recap
- One point.
:::

Next: [More](#tst.two)
`;
const TWO = `@chapter tst.two
@title More
@level as
@paper P1
@time 1 hour
@summary Second test chapter.

## More

Text with a < sign and an & sign.
`;
const course = (files, extra) => Object.assign({
  id: 'tst', kind: 'course', title: 'Test', short: 'Test', code: '0000', desc: 'd', json: { papers: [{ id: 'P1', title: 'Paper 1', chapters: ['tst.one', 'tst.two'] }] },
  chapters: [{ id: 'tst.one', title: 'Forces and motion', group: 'A' }, { id: 'tst.two', title: 'More', group: 'A' }, { id: 'tst.three', title: 'Planned', group: 'B' }],
  aliases: { 'tst.old': 'tst.two' }, files, widgets: ''
}, extra || {});
const build = (files, opts, extra) => buildSite([course(files, extra)], Object.assign({ order: ['tst'], assets }, opts || {}));

// ---------- a good course ----------
const res = build([{ name: 'tst.one.md', text: ONE }, { name: 'tst.two.md', text: TWO }], { issues: 'https://github.com/o/r/issues' });
const index = res.files['index.html'] || '', chunk = res.files['c/tst.js'] || '';
const one = res.written.get('tst.one');
ok(res.errors.length === 0, 'good course builds with no errors: ' + res.errors.join(' | '));
ok(res.chapters.length === 2 && res.stats.planned === 3, 'two chapters written of three planned');
ok(!!one && /<math/.test(one.html) && !/\\\(|\\\[/.test(one.html), 'maths becomes MathML, no raw \\( left');
ok(/<a href="#tst\.two">the second chapter<\/a>/.test(one.html), 'link to a written chapter');
ok(/<a href="#tst\.two">old name<\/a>/.test(one.html), 'alias link is rewritten');
ok(/<span class="soon"[^>]*>planned chapter<\/span>/.test(one.html), 'link to a planned chapter is plain text');
ok(/<a href="#tst\.two--more">its section<\/a>/.test(one.html), 'section link keeps its anchor');
ok(/data-marks="3"/.test(one.html) && /data-rev="tst\.two"/.test(one.html), 'try question carries marks and its revise chapter');
ok(/Revise: More/.test(one.html), 'revise link shows the chapter title');
ok(res.stats.quiz === 1 && res.stats.glossary === 1, 'one quiz question and one glossary term collected');
ok(/ZTA\.chunk\("tst"/.test(chunk) && /id=\\?"c-tst\.one\\?"/.test(chunk), 'course chapters go into the course chunk');
ok(!/id="c-tst\.one"/.test(index), 'course chapters are not in index.html');
ok(/window\.GUIDE=\{/.test(index) && /"tst\.one":\{/.test(index), 'index.html carries the navigation data');
ok(/data-nav="tst\.one"/.test(index), 'sidebar lists the chapter');
ok(/issues\/new\?title=%5Btst\.one%5D/.test(chunk), 'report-a-mistake link names the chapter');
ok(res.warnings.some(w => /tst-missing/.test(w)), 'unregistered widget is a warning');
ok(!/<script>[^]*<\/script>[^]*\u2028/.test(index), 'no raw line separators in the data');
const q = Object.values(JSON.parse((chunk.match(/"quiz":(\{.*?\}),"gloss"/) || [0, '{}'])[1]))[0] || {};
ok(q.a === 1 && q.o && q.o.length === 3 && q.c === 'tst.one', 'quiz answer index and chapter are right');
const L = lintChapter(one, ONE, { course: 'tst', hasCheck: true });
ok(L.errors.length === 0, 'good chapter lints clean: ' + L.errors.join(' | '));

// ---------- things that must be errors ----------
const errs = (text, name) => { const r = build([{ name: name || 'tst.one.md', text }, { name: 'tst.two.md', text: TWO }]); const c = r.written.get('tst.one'); return r.errors.concat(c ? lintChapter(c, text, { course: 'tst', hasCheck: true }).errors : []).join(' | '); };
ok(/unknown chapter/.test(errs(ONE.replace('#tst.three', '#tst.nowhere'))), 'link to an unknown id is an error');
ok(/marks: a try question says \[3 marks\]/.test(errs(ONE.replace('[A1] [A1]', '[A1]'))), 'try marks that do not add up are an error');
ok(/marks: worked example/.test(errs(ONE.replace('[M1]\n', '\n'))), 'worked-example marks that do not add up are an error');
ok(/role="img"/.test(errs(ONE.replace(' role="img" aria-label="A dot"', ''))), 'an unlabelled SVG is an error');
ok(/never colours/.test(errs(ONE.replace('class="f-ink"', 'fill="red"'))), 'a coloured SVG is an error');
ok(/rename it/.test(errs(ONE, 'wrong.md')), 'a file not named after its chapter is an error');
ok(/must start with "tst\."/.test(build([], {}, { chapters: [{ id: 'other.one', title: 'x' }] }).errors.join(' | ')), 'a chapter id outside its course is an error');
ok(/alias .* unknown id/.test(build([], {}, { aliases: { 'tst.old': 'tst.none' } }).errors.join(' | ')), 'an alias to an unknown id is an error');

console.log(fails ? `\n${fails} of ${n} engine checks FAILED` : `engine self-test: ${n} checks ok`);
process.exit(fails ? 1 : 0);
