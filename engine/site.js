// site.js — turns chapter sources into a finished site folder: index.html (core chapters, navigation, data)
// plus c/<course>.js chunks that the page loads with <script> on demand, so it works from file://.
// Used by engine/build.js (the whole guide), engine/check.js (validation only) and the course kit (preview).
'use strict';
const { createRenderer, escapeHtml, stripTags, LINK_KINDS } = require('./lib');

const LEVELS = { start: 'Start here', pre: 'Foundations', as: 'AS Level', a2: 'A Level (A2)', guide: 'Guide', tool: 'Interactive', ref: 'Reference', sum: 'Summary', ext: 'Beyond A Level', mock: 'Mock paper' };
/** "1 h 50 min", "1 hour 15", "75 minutes" → minutes (0 if none) */
const parseMinutes = (t) => {
  const s = String(t || '');
  const h = s.match(/(\d+(?:\.\d+)?)\s*h(?:ours?|rs?)?\b\s*(\d+)?/i);
  if (h) return Math.round(+h[1] * 60 + (+h[2] || 0));
  const m = s.match(/(\d+)\s*min/i);
  return m ? +m[1] : 0;
};
const REG_RE = /W\.register\(\s*['"]([a-z0-9-]+)['"]/g;
const stripComments = (src) => String(src || '').replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '');
const widgetNames = (src) => [...stripComments(src).matchAll(REG_RE)].map(m => m[1]);
const safeJson = (o) => JSON.stringify(o).replace(/</g, '\\u003c').replace(/-->/g, '--\\u003e').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
const slug = (s) => String(s).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

/**
 * sources: [{ id, kind: 'core'|'course', title, short, code, desc, chapters: [{id,title,level,group}], aliases: {old: new},
 *             files: [{ name, text }], widgets: '<js source>' | '' }]
 * opts:    { order: [source ids], external: Map(id -> {t, s}) of ids that live elsewhere, formulaSheets: {sheetId: [course ids]},
 *            assets: {shell, css, core, app, study}, inlineAll: bool, home: '<article html>' | null,
 *            fontFace: (chars: string) => '@font-face css', write: bool }
 * returns: { errors, warnings, files: { relPath: string }, chapters, stats }
 */
function buildSite(sources, opts) {
  const R = createRenderer({ proofBadge: (sid) => ((sources.find(s => s.id === sid) || {}).json || {}).proofBadge || 'Not examined' });
  const { st } = R;
  const errors = st.errors, warnings = st.warnings;
  const order = opts.order || [];
  sources = [...sources].sort((a, b) => (order.indexOf(a.id) + 1 || 999) - (order.indexOf(b.id) + 1 || 999));
  const external = opts.external || new Map();

  // ---------- widget registry: name -> owning source ('core' for the shared study widgets) ----------
  const regOwner = {};
  for (const n of widgetNames(opts.assets.study)) regOwner[n] = 'core';
  for (const s of sources) for (const n of widgetNames(s.widgets)) {
    if (regOwner[n] && regOwner[n] !== s.id) errors.push(`widget "${n}" is registered by both ${regOwner[n]} and ${s.id}: rename one`);
    else regOwner[n] = s.id;
  }
  const extWidgets = opts.externalWidgets || {};   // name -> course, for widgets outside this build (the kit)
  for (const [n, o] of Object.entries(extWidgets)) {
    if (regOwner[n] && regOwner[n] !== o) errors.push(`widget "${n}" is already registered by the ${o} course: rename yours`);
  }

  // ---------- planned ids and aliases ----------
  const planned = new Map();
  for (const s of sources) for (const c of s.chapters) {
    if (planned.has(c.id)) errors.push(`chapter id ${c.id} is listed twice (${planned.get(c.id).src.id} and ${s.id})`);
    else planned.set(c.id, { src: s, entry: c });
    if (s.kind === 'course' && !c.id.startsWith(s.id + '.')) errors.push(`[${s.id}] chapter id ${c.id} must start with "${s.id}."`);
  }
  const aliases = {};
  for (const s of sources) for (const [from, to] of Object.entries(s.aliases || {})) {
    if (planned.has(from)) errors.push(`[${s.id}] alias ${from} is still a chapter id: remove it from the chapter list or the aliases`);
    else if (!planned.has(to) && !external.has(to)) errors.push(`[${s.id}] alias ${from} points to unknown id ${to}`);
    aliases[from] = to;
  }
  for (const [from, to] of Object.entries(opts.externalAliases || {})) if (!aliases[from]) aliases[from] = to;

  // ---------- papers (course.json "papers": [{id, title, chapters}]): practice sets and checklist roll-ups ----------
  const papers = {};
  for (const s of sources) {
    const list = (s.json && s.json.papers) || [];
    if (!Array.isArray(list)) { errors.push(`[${s.id}] "papers" in course.json must be a list`); continue; }
    for (const p of list) {
      if (!p.id || !p.title || !Array.isArray(p.chapters)) { errors.push(`[${s.id}] each paper needs id, title and chapters`); continue; }
      for (const id of p.chapters) if (!planned.has(id) || planned.get(id).src !== s) errors.push(`[${s.id}] paper ${p.id} lists ${id}, which is not a chapter of this course`);
    }
    papers[s.id] = list.filter(p => p.id && Array.isArray(p.chapters));
  }

  // ---------- render every chapter file ----------
  const written = new Map();
  for (const s of sources) {
    for (const f of s.files) {
      const { chapters } = R.renderFile(f.text, s.id, f.name);
      if (!chapters.length) errors.push(`[${s.id}/${f.name}] no @chapter line at the top`);
      if (chapters.length > 1) errors.push(`[${s.id}/${f.name}] one chapter per file (found ${chapters.length})`);
      for (const c of chapters) {
        c.file = f.name;
        c.src = s;
        if (f.name !== c.id + '.md') errors.push(`[${c.id}] file is named ${f.name}: rename it to ${c.id}.md`);
        const p = planned.get(c.id);
        if (!p) { errors.push(`[${c.id}] is not in ${s.kind === 'core' ? 'core.json' : 'course.json'}${aliases[c.id] ? ` (it is an alias of ${aliases[c.id]})` : ': add it to the chapter list'}`); continue; }
        if (p.src !== s) { errors.push(`[${c.id}] belongs to ${p.src.id}, not ${s.id}`); continue; }
        if (written.has(c.id)) { errors.push(`duplicate chapter ${c.id} (${written.get(c.id).file} and ${f.name})`); continue; }
        if (p.entry.title && stripTags(R.inline(c.title)) !== stripTags(R.inline(p.entry.title))) warnings.push(`[${c.id}] @title "${c.title}" differs from the chapter list ("${p.entry.title}")`);
        c.group = p.entry.group || 'Contents';
        written.set(c.id, c);
      }
    }
  }

  // ---------- formula sheets from :::key / :::formula boxes ----------
  for (const [sheetId, courseIds] of Object.entries(opts.formulaSheets || {})) {
    const sheet = written.get(sheetId);
    if (!sheet) continue;
    let html = '';
    for (const cid of courseIds) {
      const s = sources.find(x => x.id === cid);
      if (!s) continue;
      for (const e of s.chapters) {
        const keys = st.KEYS.filter(k => k.c === e.id);
        if (!keys.length || !written.has(e.id)) continue;
        const t = R.inline(written.get(e.id).title);
        html += `<h2 id="${sheetId}--${slug(e.id)}">${t}</h2>${keys.map(k => R.subMath(k.html)).join('')}<p class="sheet-link"><a href="#${e.id}">Revise: ${t}</a></p>`;
      }
    }
    sheet.html += html || '<p class="sheet-empty"><em>The formulas appear here as the chapters are written.</em></p>';
  }

  // ---------- "Learn more online" pages from :::links boxes, grouped by course group, chapter and kind ----------
  for (const [sheetId, courseIds] of Object.entries(opts.linkSheets || {})) {
    const sheet = written.get(sheetId);
    if (!sheet) continue;
    let html = '', kinds = new Set(), n = 0;
    for (const cid of courseIds) {
      const s = sources.find(x => x.id === cid);
      if (!s) continue;
      let group = null;
      for (const e of s.chapters) {
        const links = st.LINKS.filter(l => l.c === e.id);
        if (!links.length || !written.has(e.id)) continue;
        const c = written.get(e.id);
        if (c.group !== group) { group = c.group; html += `<h2 id="${sheetId}--${slug(group)}">${escapeHtml(group)}</h2>`; }
        const t = R.inline(c.title);
        html += `<h3 id="${sheetId}--${slug(e.id)}"><a href="#${e.id}">${t}</a></h3><div class="links-b">`
          + links.map(l => { kinds.add(l.kind); n += (l.html.match(/<li>/g) || []).length; return `<div class="lk-g lk-${l.kind}" data-kind="${l.kind}"><div class="lk-gt">${LINK_KINDS[l.kind].t}</div><ul>${l.html}</ul></div>`; }).join('') + '</div>';
      }
    }
    const order = Object.keys(LINK_KINDS).filter(k => kinds.has(k));
    sheet.html += html
      ? `<div class="lk-sheet"><div class="lk-filter" role="group" aria-label="Show links of one kind"><button type="button" data-k="" aria-pressed="true">All ${n}</button>${order.map(k => `<button type="button" data-k="${k}" aria-pressed="false">${LINK_KINDS[k].t}</button>`).join('')}</div>${html}</div>`
      : '<p class="sheet-empty"><em>The links appear here as the chapters get their "Learn more online" boxes.</em></p>';
  }

  // ---------- :::progress roll-ups of the course's checklists, per paper ----------
  const checksOf = (id) => written.has(id) ? st.CHECKS.filter(k => k.c === id).flatMap(k => k.keys) : [];
  const row = (keys, label) => `<li data-clp="${keys.join(',')}"><span class="clp-t">${label}</span><span class="clp-n"></span><span class="clp-bar"><i></i></span></li>`;
  const paperRows = (p) => p.chapters.map(id => [id, checksOf(id)]).filter(([, k]) => k.length).map(([id, k]) => row(k, `<a href="#${id}">${R.inline(written.get(id).title)}</a>`));
  for (const c of written.values()) {
    c.html = c.html.replace(/<div class="cl-prog" data-prog="([^"|]*)\|([^"]*)"><\/div>/g, (m, sid, pid) => {
      const list = papers[sid] || [];
      if (!list.length) { errors.push(`[${c.id}] :::progress needs "papers" in course.json`); return ''; }
      let title, rows, all;
      if (pid) {
        const p = list.find(x => x.id === pid);
        if (!p) { errors.push(`[${c.id}] :::progress ${pid}: no paper with that id in course.json (have ${list.map(x => x.id).join(', ')})`); return ''; }
        title = escapeHtml(p.title); rows = paperRows(p).join(''); all = p.chapters.flatMap(checksOf);
      } else {
        title = 'All papers';
        rows = list.map(p => { const k = p.chapters.flatMap(checksOf); return k.length ? `<li class="clp-p" data-clp="${k.join(',')}"><details><summary><span class="clp-t">${escapeHtml(p.title)}</span><span class="clp-n"></span><span class="clp-bar"><i></i></span></summary><ul>${paperRows(p).join('')}</ul></details></li>` : ''; }).join('');
        all = [...new Set(list.flatMap(p => p.chapters.flatMap(checksOf)))];
      }
      return `<div class="cl-prog"><div class="cl-h"><span class="cl-l">Checklist progress</span><span class="cl-t">${title}</span><span class="cl-n" data-clp="${all.join(',')}"></span></div>${rows ? `<ul class="clp-list">${rows}</ul>` : '<p class="sheet-empty"><em>Checklists appear here as the chapters get them.</em></p>'}</div>`;
    });
  }

  // ---------- links: aliases, unknown ids, chapters not written yet ----------
  let soonLinks = 0;
  for (const c of written.values()) {
    c.html = c.html.replace(/<a href="#([^"]+)">([\s\S]*?)<\/a>/g, (m, href, txt) => {
      let [base, sec] = [href.split('--')[0], href.includes('--') ? href.slice(href.indexOf('--')) : ''];
      if (aliases[base]) { base = aliases[base]; sec = ''; }
      // an empty link is a "revise" link from a :::try question: it shows the chapter's title
      if (!txt) txt = 'Revise: ' + (written.has(base) ? R.inline(written.get(base).title) : planned.has(base) ? R.inline(planned.get(base).entry.title || base) : external.has(base) ? escapeHtml(external.get(base).t) : base);
      if (written.has(base)) return `<a href="#${base}${sec}">${txt}</a>`;
      if (planned.has(base) || external.has(base)) { soonLinks++; return `<span class="soon" title="Coming soon">${txt}</span>`; }
      errors.push(`[${c.id}] link to unknown chapter #${href}`);
      return txt;
    });
  }

  // ---------- order, groups, chunks ----------
  const ordered = [];
  const subjects = [];
  for (const s of sources) {
    const sub = { id: s.id, kind: s.kind, title: s.title, short: s.short, code: s.code, desc: s.desc, groups: [], planned: s.chapters.length };
    subjects.push(sub);
    for (const e of s.chapters) {
      const c = written.get(e.id);
      if (!c) continue;
      const last = sub.groups[sub.groups.length - 1];
      if (last && last.title === c.group) last.chapters.push(c); else sub.groups.push({ title: c.group, chapters: [c] });
      ordered.push(c);
      c.chunk = (s.kind === 'course' && !opts.inlineAll) ? s.id : null;
    }
  }
  const chunks = [...new Set(ordered.map(c => c.chunk).filter(Boolean))];
  for (const c of ordered) {
    const need = new Set();
    for (const m of c.html.matchAll(/data-w="([^"]+)"/g)) {
      const owner = regOwner[m[1]];
      if (!owner && extWidgets[m[1]]) warnings.push(`[${c.id}] widget "${m[1]}" comes from the ${extWidgets[m[1]]} course: it works in the full site; the preview shows a placeholder`);
      else if (!owner) warnings.push(`[${c.id}] widget "${m[1]}" is not built yet (it shows a placeholder until a widgets.js registers it)`);
      else if (owner !== 'core' && owner !== c.chunk && chunks.includes(owner)) need.add(owner);
    }
    c.need = [...need];
  }

  // ---------- HTML ----------
  const titleOf = (c) => R.inline(c.title);
  const subjOf = (id) => subjects.find(s => s.id === id);
  function header(c) {
    if (c.meta.hero === 'none') return '';
    const s = subjOf(c.subject);
    const chips = [];
    if (c.meta.level) for (const lv of c.meta.level.split(/[ ,]+/).filter(Boolean)) {
      const k = lv.toLowerCase();
      chips.push(`<span class="chip lv lv-${k}">${LEVELS[k] || escapeHtml(lv)}</span>`);
    }
    if (c.meta.paper) chips.push(`<span class="chip chip-paper"><span class="chip-k">Exams</span>${escapeHtml(c.meta.paper)}</span>`);
    const mock = /\bmock\b/i.test(c.meta.level || '');
    if (mock && c.marks) chips.push(`<span class="chip chip-marks"><span class="chip-k">Total</span>${c.marks} marks</span>`);
    if (c.meta.time) chips.push(`<span class="chip chip-time"><span class="chip-k">${mock ? 'Time allowed' : 'Study time'}</span>${escapeHtml(c.meta.time)}</span>`);
    const first = s.groups[0] && s.groups[0].chapters[0];
    const crumbs = `<nav class="crumbs" aria-label="Breadcrumb"><a href="#${first ? first.id : 'home'}">${escapeHtml(s.title)}</a><span aria-hidden="true">/</span><span>${escapeHtml(c.group)}</span></nav>`;
    const lede = c.meta.summary ? `<p class="lede">${R.inline(c.meta.summary)}</p>` : '';
    return `<header class="ch-head">${crumbs}<h1>${titleOf(c)}</h1>${chips.length ? `<div class="chips">${chips.join('')}</div>` : ''}${lede}</header>`;
  }
  const articles = {};
  ordered.forEach((c, i) => {
    const prev = ordered[i - 1], next = ordered[i + 1];
    const foot = c.meta.foot === 'none' ? '' : `<footer class="ch-foot">
<button class="done-btn" type="button" data-done="${c.id}" aria-pressed="false"><span class="done-box" aria-hidden="true"></span><span class="done-txt">Mark as learned</span></button>
<div class="pn">${prev ? `<a class="pn-prev" href="#${prev.id}"><small>Previous</small><span>${stripTags(titleOf(prev))}</span></a>` : '<span></span>'}${next ? `<a class="pn-next" href="#${next.id}"><small>Next</small><span>${stripTags(titleOf(next))}</span></a>` : '<span></span>'}</div></footer>`;
    const k = c.chunk || '';
    const lv = (c.meta.level || '').split(/[ ,]+/)[0].toLowerCase();
    const mockAttrs = lv === 'mock' ? ` data-level="mock" data-min="${parseMinutes(c.meta.time)}" data-marks="${c.marks}"` : '';
    articles[k] = (articles[k] || '') + `<article class="chapter s-${c.subject}" id="c-${c.id}" data-id="${c.id}" data-subject="${c.subject}"${mockAttrs} hidden>${header(c)}<div class="prose">${c.html}</div>${foot}</article>\n`;
  });

  let nav = '';
  for (const s of subjects) {
    if (!s.groups.length) continue;
    nav += `<section class="nav-subj s-${s.id}" data-subject="${s.id}"><button class="nav-s" type="button" aria-expanded="false" data-toggle="${s.id}"><span class="dot" aria-hidden="true"></span><span class="nav-st">${escapeHtml(s.title)}</span><span class="nav-pc" data-pc="${s.id}"></span><svg class="chev" viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M4 2l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button><div class="nav-groups" data-groups="${s.id}">`;
    for (const g of s.groups) {
      nav += `<div class="nav-g">${s.groups.length > 1 ? `<div class="nav-gt">${escapeHtml(g.title)}</div>` : ''}<ul>`;
      for (const c of g.chapters) {
        const lv = (c.meta.level || '').split(/[ ,]+/)[0].toLowerCase();
        nav += `<li><a href="#${c.id}" data-nav="${c.id}"><span class="tick" aria-hidden="true"></span><span class="nav-t">${stripTags(titleOf(c))}</span>${lv === 'as' || lv === 'a2' ? `<em class="lvl lvl-${lv}">${lv === 'as' ? 'AS' : 'A2'}</em>` : ''}</a></li>`;
      }
      nav += `</ul></div>`;
    }
    nav += `</div></section>`;
  }

  // quiz + glossary data, split by where each chapter lives
  const chunkOfCh = (id) => (written.get(id) || {}).chunk || '';
  const quiz = {}, gloss = {};
  st.QUIZ.forEach((q, i) => { const k = chunkOfCh(q.c); (quiz[k] = quiz[k] || {})[i] = q; });
  for (const g of st.GLOSSARY) { const k = chunkOfCh(g.c); (gloss[k] = gloss[k] || []).push(g); }

  const DATA = {
    order: ordered.map(c => c.id),
    ch: Object.fromEntries(ordered.map(c => {
      const o = { t: stripTags(titleOf(c)), s: c.subject, g: c.group, l: (c.meta.level || '').split(/[ ,]+/)[0].toLowerCase(), w: c.words };
      if (c.chunk) o.k = c.chunk;
      if (c.need.length) o.n = c.need;
      if (c.meta.foot !== 'none') o.f = 1;
      return [c.id, o];
    })),
    subjects: subjects.map(s => ({ id: s.id, c: s.kind === 'course' ? 1 : 0, t: s.title, short: s.short, code: s.code, desc: s.desc, n: s.groups.reduce((a, g) => a + g.chapters.length, 0), p: s.planned, first: s.groups[0] ? s.groups[0].chapters[0].id : null })),
    chunks,
    papers: Object.fromEntries(Object.entries(papers).filter(([, l]) => l.length).map(([sid, l]) => [sid, l.map(p => ({ id: p.id, t: p.title, c: p.chapters.filter(id => written.has(id)) }))])),
    built: new Date().toISOString().slice(0, 10)
  };

  const files = {};
  if (opts.write !== false) {
    const A = opts.assets;
    const fontFace = opts.fontFace ? opts.fontFace([...st.mathChars].join('')) : '';
    const inlineWidgets = [A.study, ...sources.filter(s => s.widgets && (s.kind === 'core' || opts.inlineAll)).map(s => `/* ${s.id} widgets */\n${s.widgets}`)].join('\n;\n');
    files['index.html'] = A.shell
      .replace('/*FONTFACE*/', () => fontFace)
      .replace('/*CSS*/', () => A.css)
      .replace('<!--NAV-->', () => nav)
      .replace('<!--CHAPTERS-->', () => (opts.home || '') + (articles[''] || ''))
      .replace('/*DATA*/', () => `window.GUIDE=${safeJson(DATA)};window.QUIZ=${safeJson(quiz[''] || {})};window.GLOSSARY=${safeJson(gloss[''] || [])};`)
      .replace('/*CORE*/', () => A.core)
      .replace('/*WIDGETS*/', () => inlineWidgets)
      .replace('/*APP*/', () => A.app);
    for (const k of chunks) {
      const s = sources.find(x => x.id === k);
      files[`c/${k}.js`] = `/* Zero to A* — ${s.title} (generated by engine/build.js; do not edit) */\n${s.widgets ? s.widgets + '\n;\n' : ''}ZTA.chunk(${JSON.stringify(k)}, ${safeJson({ html: articles[k] || '', quiz: quiz[k] || {}, gloss: gloss[k] || [] })});\n`;
    }
  }

  const stats = {
    chapters: ordered.length, planned: planned.size, words: ordered.reduce((a, c) => a + c.words, 0), math: st.mathCount,
    quiz: st.QUIZ.length, glossary: st.GLOSSARY.length, soonLinks,
    by: Object.fromEntries(subjects.map(s => [s.id, `${s.groups.reduce((a, g) => a + g.chapters.length, 0)}/${s.planned}`]))
  };
  return { errors, warnings, files, chapters: ordered, written, planned, stats, R, regOwner };
}

module.exports = { buildSite, widgetNames, LEVELS, parseMinutes };
