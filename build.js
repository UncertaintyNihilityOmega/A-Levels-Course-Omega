// Build: content/*.md -> dist/index.html  (node build.js [--strict] [--only=subj,subj])
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { createRenderer, escapeHtml, stripTags } = require('./lib');

const ROOT = __dirname;
const SCRATCH = process.env.SCRATCH || require('os').tmpdir();
const outline = JSON.parse(fs.readFileSync(path.join(ROOT, 'src/outline.json'), 'utf8'));
const R = createRenderer();
const { st } = R;
const missing = [];

// ---------- render all files ----------
const subjects = [];
const chapters = [];
for (const subj of outline.subjects) {
  const s = { id: subj.id, title: subj.title, short: subj.short, code: subj.code, desc: subj.desc, groups: [] };
  subjects.push(s);
  for (const file of subj.files) {
    const fp = path.join(ROOT, 'content', file);
    if (!fs.existsSync(fp)) { missing.push(file); continue; }
    const { chapters: chs, groups } = R.renderFile(fs.readFileSync(fp, 'utf8'), subj.id, file);
    for (const g of groups) {
      const last = s.groups[s.groups.length - 1];
      if (last && last.title === g.title) last.chapters.push(...g.chapters);
      else s.groups.push({ title: g.title, chapters: [...g.chapters] });
    }
    for (const c of chs) {
      if (chapters.find(x => x.id === c.id)) st.errors.push(`duplicate chapter id ${c.id}`);
      chapters.push(c);
    }
  }
}

// ---------- link check ----------
const ids = new Set(chapters.map(c => c.id));
const planned = new Set(outline.subjects.flatMap(s => s.chapters.map(c => c.id)));
const brokenLinks = [];
for (const c of chapters) {
  for (const m of c.html.matchAll(/href="#([^"]+)"/g)) {
    const target = m[1].split('--')[0];
    if (!ids.has(target)) (planned.has(target) ? brokenLinks : st.errors).push(`[${c.id}] link to ${planned.has(target) ? 'not-yet-written' : 'UNKNOWN'} #${m[1]}`);
  }
  if (!planned.has(c.id)) st.errors.push(`chapter id ${c.id} is not in the outline`);
}
// links to chapters that are not written yet: degrade to plain text
for (const c of chapters) {
  c.html = c.html.replace(/<a href="#([^"]+)">([\s\S]*?)<\/a>/g, (m, h, txt) => ids.has(h.split('--')[0]) ? m : `<span class="soon" title="Coming soon">${txt}</span>`);
}

// ---------- assemble ----------
const LEVELS = { start: 'Start here', pre: 'Foundations', as: 'AS Level', a2: 'A Level (A2)', guide: 'Guide', tool: 'Interactive', ref: 'Reference', sum: 'Summary', ext: 'Beyond A Level' };
const titleOf = (c) => R.inline(c.title);
function chapterHeader(c) {
  if (c.meta.hero === 'none') return '';
  const subj = subjects.find(s => s.id === c.subject);
  const chips = [];
  if (c.meta.level) for (const lv of c.meta.level.split(/[ ,]+/).filter(Boolean)) {
    const k = lv.toLowerCase();
    chips.push(`<span class="chip lv lv-${k}">${LEVELS[k] || escapeHtml(lv)}</span>`);
  }
  if (c.meta.paper) chips.push(`<span class="chip chip-paper"><span class="chip-k">Exams</span>${escapeHtml(c.meta.paper)}</span>`);
  if (c.meta.time) chips.push(`<span class="chip chip-time"><span class="chip-k">Study time</span>${escapeHtml(c.meta.time)}</span>`);
  const first = subj.groups[0] && subj.groups[0].chapters[0];
  const crumbs = `<nav class="crumbs" aria-label="Breadcrumb"><a href="#${first ? first.id : 'home'}">${escapeHtml(subj.title)}</a><span aria-hidden="true">/</span><span>${escapeHtml(c.group)}</span></nav>`;
  const summary = c.meta.summary ? `<p class="lede">${R.inline(c.meta.summary)}</p>` : '';
  return `<header class="ch-head">${crumbs}<h1>${titleOf(c)}</h1>${chips.length ? `<div class="chips">${chips.join('')}</div>` : ''}${summary}</header>`;
}

// order chapters by subject/group order
const ordered = [];
for (const s of subjects) for (const g of s.groups) for (const c of g.chapters) ordered.push(c);
let chaptersHtml = '';
ordered.forEach((c, i) => {
  const prev = ordered[i - 1], next = ordered[i + 1];
  const foot = c.meta.foot === 'none' ? '' : `<footer class="ch-foot">
<button class="done-btn" type="button" data-done="${c.id}" aria-pressed="false"><span class="done-box" aria-hidden="true"></span><span class="done-txt">Mark as learned</span></button>
<div class="pn">${prev ? `<a class="pn-prev" href="#${prev.id}"><small>Previous</small><span>${stripTags(titleOf(prev))}</span></a>` : '<span></span>'}${next ? `<a class="pn-next" href="#${next.id}"><small>Next</small><span>${stripTags(titleOf(next))}</span></a>` : '<span></span>'}</div></footer>`;
  chaptersHtml += `<article class="chapter s-${c.subject}" id="c-${c.id}" data-id="${c.id}" data-subject="${c.subject}" hidden>${chapterHeader(c)}<div class="prose">${c.html}</div>${foot}</article>\n`;
});

let navHtml = '';
for (const s of subjects) {
  const total = s.groups.reduce((a, g) => a + g.chapters.length, 0);
  if (!total) continue;
  const first = s.groups[0].chapters[0];
  navHtml += `<section class="nav-subj s-${s.id}" data-subject="${s.id}"><button class="nav-s" type="button" aria-expanded="false" data-toggle="${s.id}"><span class="dot" aria-hidden="true"></span><span class="nav-st">${escapeHtml(s.title)}</span><span class="nav-pc" data-pc="${s.id}"></span><svg class="chev" viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M4 2l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button><div class="nav-groups" data-groups="${s.id}">`;
  for (const g of s.groups) {
    const showTitle = s.groups.length > 1;
    navHtml += `<div class="nav-g">${showTitle ? `<div class="nav-gt">${escapeHtml(g.title)}</div>` : ''}<ul>`;
    for (const c of g.chapters) {
      const lv = (c.meta.level || '').split(/[ ,]+/)[0].toLowerCase();
      navHtml += `<li><a href="#${c.id}" data-nav="${c.id}"><span class="tick" aria-hidden="true"></span><span class="nav-t">${stripTags(titleOf(c))}</span>${lv === 'as' || lv === 'a2' ? `<em class="lvl lvl-${lv}">${lv === 'as' ? 'AS' : 'A2'}</em>` : ''}</a></li>`;
    }
    navHtml += `</ul></div>`;
  }
  navHtml += `</div></section>`;
}

const DATA = {
  order: ordered.map(c => c.id),
  ch: Object.fromEntries(ordered.map(c => [c.id, { t: stripTags(titleOf(c)), s: c.subject, g: c.group, l: (c.meta.level || '').split(/[ ,]+/)[0].toLowerCase(), w: c.words }])),
  subjects: subjects.map(s => ({ id: s.id, t: s.title, short: s.short, code: s.code, desc: s.desc, n: s.groups.reduce((a, g) => a + g.chapters.length, 0), first: s.groups[0] && s.groups[0].chapters[0] ? s.groups[0].chapters[0].id : null })),
  planned: outline.subjects.map(s => ({ id: s.id, n: s.chapters.length })),
  built: new Date().toISOString().slice(0, 10)
};

// ---------- math font subset ----------
let fontFace = '';
try {
  const chars = [...st.mathChars].join('') + '()[]{}|‖√∫∑∏0123456789+−=<>';
  fs.writeFileSync(path.join(SCRATCH, 'mathchars.txt'), chars);
  const outFont = path.join(SCRATCH, 'guide-math.woff2');
  execFileSync('pyftsubset', [(fs.existsSync(path.join(ROOT, 'vendor/latinmodern-math.otf')) ? path.join(ROOT, 'vendor/latinmodern-math.otf') : '/usr/share/texmf/fonts/opentype/public/lm-math/latinmodern-math.otf'), `--text-file=${path.join(SCRATCH, 'mathchars.txt')}`, '--layout-features=*', '--flavor=woff2', `--output-file=${outFont}`], { stdio: 'pipe' });
  fontFace = `@font-face{font-family:"Guide Math";src:url(data:font/woff2;base64,${fs.readFileSync(outFont).toString('base64')}) format("woff2");font-display:swap}`;
} catch (e) { st.errors.push('font subset failed: ' + e.message); }

const read = (p) => fs.existsSync(path.join(ROOT, p)) ? fs.readFileSync(path.join(ROOT, p), 'utf8') : '';
const safeJson = (o) => JSON.stringify(o).replace(/</g, '\\u003c').replace(/-->/g, '--\\u003e');
let shell = read('src/shell.html');
const widgetFiles = fs.readdirSync(path.join(ROOT, 'src')).filter(f => /^widgets.*\.js$/.test(f)).sort();
shell = shell
  .replace('/*FONTFACE*/', () => fontFace)
  .replace('/*CSS*/', () => read('src/style.css'))
  .replace('<!--NAV-->', () => navHtml)
  .replace('<!--CHAPTERS-->', () => chaptersHtml)
  .replace('/*DATA*/', () => `window.GUIDE=${safeJson(DATA)};window.QUIZ=${safeJson(st.QUIZ)};window.GLOSSARY=${safeJson(st.GLOSSARY)};`)
  .replace('/*CORE*/', () => read('src/core.js'))
  .replace('/*WIDGETS*/', () => widgetFiles.map(f => `/* ${f} */\n` + read('src/' + f)).join('\n;\n'))
  .replace('/*APP*/', () => read('src/app.js'));

fs.mkdirSync(path.join(ROOT, 'dist'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'dist/index.html'), shell);
fs.writeFileSync(path.join(ROOT, 'dist/test.html'), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0;font:14px system-ui;background:#fafafa}[hidden]{display:none!important}img{max-width:100%}</style></head><body>${shell}</body></html>`);
fs.copyFileSync(path.join(ROOT, 'dist/test.html'), path.join(ROOT, 'dist/zero-to-a-star.html'));

const size = Buffer.byteLength(shell);
const words = ordered.reduce((a, c) => a + c.words, 0);
console.log(`chapters ${ordered.length}/${planned.size}  words ${words}  math ${st.mathCount}  quiz ${st.QUIZ.length}  glossary ${st.GLOSSARY.length}  size ${(size / 1024).toFixed(0)} KB`);
const by = {};
for (const c of ordered) by[c.subject] = (by[c.subject] || 0) + 1;
console.log('by subject', JSON.stringify(by));
if (missing.length) console.log('missing files:', missing.join(', '));
if (brokenLinks.length) console.log(`${brokenLinks.length} link(s) to chapters not written yet (shown as plain text)`);
if (st.errors.length) {
  console.log(`\n${st.errors.length} ERROR(S):`);
  for (const e of st.errors.slice(0, 120)) console.log(' - ' + e);
  if (process.argv.includes('--strict')) process.exit(1);
}
if (process.argv.includes('--warn') && st.warnings.length) {
  console.log(`\n${st.warnings.length} warning(s):`);
  for (const e of st.warnings.slice(0, 60)) console.log(' - ' + e);
}
