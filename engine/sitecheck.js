// sitecheck.js — checks the built site (run `node engine/build.js` first). Reads site/, writes nothing.
//   node engine/sitecheck.js           static pages and their links, sitemap, manifest, service worker, every chapter
//                                      (links, sections, maths errors, repeated ids, quizzes, widgets), quiz data, mocks
//   node engine/sitecheck.js --links   also fetch every external link (slow; 403 is usually a site refusing robots,
//                                      404, 410, 5xx and DNS errors are the ones to fix)
// Exit 1 if a problem is found. Widgets named in WAITING are planned and reported apart.
'use strict';
const fs = require('fs'), path = require('path');
process.chdir(path.join(__dirname, '..'));
const WAITING = new Set(['breakeven', 'npv']);   // tools.calc: built by Business and Accounting
const S = 'site'; const out = [];
const walk = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(path.join(d, e.name)) : [path.join(d, e.name)]);
const files = walk(S).map(f => f.split(path.sep).join('/'));
const set = new Set(files.map(f => f.slice(S.length + 1)));
console.log('files', files.length, 'MB', (files.reduce((a, f) => a + fs.statSync(f).size, 0) / 1e6).toFixed(1));

// 1 static pages: links between them and their anchors, raw markup left behind
const pset = [...set].filter(f => f.startsWith('p/') && f.endsWith('.html'));
let bad = 0, anch = 0; const ids = {};
const strip = h => h.replace(/<pre[\s\S]*?<\/pre>/g, '').replace(/<code[\s\S]*?<\/code>/g, '').replace(/<annotation[\s\S]*?<\/annotation>/g, '');
for (const f of pset) { const h = fs.readFileSync(S + '/' + f, 'utf8'); ids[f] = new Set([...h.matchAll(/\sid="([^"]+)"/g)].map(m => m[1])); }
for (const f of pset) {
  const h = fs.readFileSync(S + '/' + f, 'utf8');
  for (const m of h.matchAll(/href="([^"#:]+\.html)(#[^"]*)?"/g)) {
    const t = path.posix.normalize('p/' + m[1]);
    if (!set.has(t)) { bad++; if (bad < 6) out.push('static link to missing page: ' + f + ' -> ' + m[1]); }
    else if (m[2] && m[2].length > 1 && ids[t] && !ids[t].has(decodeURIComponent(m[2].slice(1)))) { anch++; if (anch < 8) out.push('static anchor missing: ' + f + ' -> ' + m[1] + m[2]); }
  }
  const body = strip(h);
  if (/\\\(|\\\[|^:::/m.test(body)) out.push('raw markup left in ' + f);
}
console.log('static pages', pset.length, '· links to missing pages', bad, '· missing anchors', anch);

// 2 sitemap
const sm = fs.readFileSync(S + '/sitemap.xml', 'utf8');
const locs = [...sm.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
const base = locs[0];
let smBad = 0;
for (const l of locs) { const rel = l.slice(base.length) || 'index.html'; if (!set.has(rel)) { smBad++; if (smBad < 4) out.push('sitemap url without a file: ' + l); } }
console.log('sitemap urls', locs.length, 'base', base, '· without a file', smBad);

// 3 manifest and service worker
const man = JSON.parse(fs.readFileSync(S + '/manifest.webmanifest', 'utf8'));
for (const i of man.icons) if (!set.has(i.src)) out.push('manifest icon missing ' + i.src);
const sw = fs.readFileSync(S + '/sw.js', 'utf8');
const quoted = [...sw.matchAll(/"((?:c\/|icons?\/|\.\/)?[\w./%-]+\.(?:js|html|png|svg|webmanifest))"/g)].map(m => m[1]);
const swMiss = [...new Set(quoted)].filter(x => !set.has(x.replace(/^\.\//, '')));
const cFiles = [...set].filter(f => f.startsWith('c/'));
const cNot = cFiles.filter(f => !sw.includes('"' + f + '"'));
console.log('sw.js names', new Set(quoted).size, 'files · missing on disk', swMiss.length, swMiss.slice(0, 4), '· course files not named in sw.js', cNot.length, cNot.slice(0, 3));

// 4 every chapter: links, sections, maths errors, repeated ids, empty quizzes
const idx = fs.readFileSync(S + '/index.html', 'utf8');
const G = JSON.parse(idx.match(/window\.GUIDE=(\{.*?\});window\.QUIZ=/s)[1]);
const heads = {};
for (const k of G.chunks) {
  const s = fs.readFileSync(`${S}/c/${k}.search.js`, 'utf8');
  const rows = JSON.parse(s.slice(s.indexOf(',') + 1, s.lastIndexOf(')')));
  for (const r of rows) heads[r[0]] = new Set(r[1].map(h => h[0]));
}
const coreArt = {};
for (const m of idx.matchAll(/<article[^>]*\sdata-id="([^"]+)"[\s\S]*?<\/article>/g)) { coreArt[m[1]] = m[0]; heads[m[1]] = new Set([...m[0].matchAll(/<h[23][^>]*\sid="([^"]+)"/g)].map(x => x[1])); }
let secBad = 0, idBad = 0, pages = 0, widgets = 0; const ext = new Set(); const html = {};
for (const id of G.order) {
  const c = G.ch[id]; let h;
  if (c.k) {
    const f = `${S}/c/${c.k}/${id}.js`;
    if (!fs.existsSync(f)) { out.push('chapter file missing: ' + id); continue; }
    const s = fs.readFileSync(f, 'utf8');
    h = JSON.parse(s.slice(`ZTA.page(${JSON.stringify(c.k)}, ${JSON.stringify(id)}, `.length, s.lastIndexOf(')')));
    if (!heads[id]) out.push('no search row for ' + id);
  } else h = coreArt[id] || '';
  if (!h) { out.push('no page for ' + id); continue; }
  html[id] = h; pages++;
}
const regW = new Set(), waiting = [];
for (const f of ['index.html', ...G.chunks.map(k => `c/${k}.js`)]) for (const m of fs.readFileSync(S + '/' + f, 'utf8').matchAll(/W\.register\(\s*['"]([\w-]+)['"]/g)) regW.add(m[1]);
for (const [id, h] of Object.entries(html)) {
  for (const m of h.matchAll(/href="#([^"]+)"/g)) {
    const t = decodeURIComponent(m[1]); const k = t.indexOf('--'); const cid = k > 0 ? t.slice(0, k) : t;
    if (!G.ch[cid] && cid !== 'home' && cid !== 'settings') { idBad++; if (idBad < 8) out.push(`link to unknown page: ${id} -> #${t}`); }
    else if (k > 0 && heads[cid] && !heads[cid].has(t)) { secBad++; if (secBad < 12) out.push(`link to missing section: ${id} -> #${t}`); }
  }
  if (/class="texerr"/.test(h)) out.push('maths error in ' + id);
  const all = [...h.matchAll(/\sid="([^"]+)"/g)].map(m => m[1]);
  const ds = [...new Set(all.filter((x, i) => all.indexOf(x) !== i))];
  if (ds.length) out.push('repeated ids in ' + id + ': ' + ds.slice(0, 3).join(', '));
  for (const m of h.matchAll(/data-qs="([^"]*)"/g)) if (!m[1]) out.push('empty quiz in ' + id);
  for (const m of h.matchAll(/data-w="([\w-]+)"/g)) { widgets++; if (!regW.has(m[1])) (WAITING.has(m[1]) ? waiting : out).push(`widget not registered: ${m[1]} in ${id}`); }
  for (const m of h.matchAll(/href="(https?:[^"]+)"/g)) ext.add(m[1]);
}
console.log('pages', pages, 'of', G.order.length, '· links to unknown pages', idBad, '· links to missing sections', secBad, '· widgets placed', widgets, '(registered names', regW.size + ')', '· external links', ext.size);

// 5 Next chain: every topic chapter's "Next:" link exists and no chapter is skipped inside a course
for (const s of G.subjects.filter(x => x.c)) {
  const list = G.order.filter(i => G.ch[i].s === s.id);
  const noNext = list.filter(i => html[i] && !/class="pn-next"|pn-next/.test(html[i]));
  if (list.length && noNext.length > 1) out.push(`${s.id}: ${noNext.length} chapters without a Next link: ${noNext.slice(0, 4).join(', ')}`);
}

// 6 quiz and glossary data
let qbad = 0, qn = 0, gl = 0;
const chk = (d) => {
  for (const [i, q] of Object.entries(d.quiz)) { qn++; if (!(q.a >= 0 && q.a < q.o.length) || q.o.length < 2 || !G.ch[q.c] || new Set(q.o).size !== q.o.length || !q.q) { qbad++; out.push('bad quiz question ' + i + ' in ' + q.c); } }
  for (const g of d.gloss) { gl++; if (!G.ch[g.c]) out.push('key term for an unknown chapter: ' + g.c); }
};
for (const k of G.chunks) { const s = fs.readFileSync(`${S}/c/${k}.js`, 'utf8'); const mm = s.match(/ZTA\.chunk\("[^"]+", (\{.*\})\);\s*$/s); chk(JSON.parse(mm[1])); }
console.log('quiz questions in course files', qn, '· bad', qbad, '· key terms', gl);
const noq = G.order.filter(i => ['as', 'a2'].includes(G.ch[i].l) && !G.ch[i].q);
console.log('AS/A2 chapters with no quiz question', noq.length, noq.slice(0, 8).join(', '));
const sum = Object.entries(G.ch).reduce((a, [, c]) => a + (c.q || 0), 0);
console.log('quiz count in navigation data', sum);

// 7 mocks: every question has marks and a revise chapter that exists
for (const [mid, qs] of Object.entries(G.mocks || {})) {
  const nom = qs.filter(q => !q[0]).length, norev = qs.filter(q => q[1] && !G.ch[q[1]]).length;
  if (nom || norev) out.push(`mock ${mid}: ${nom} question(s) without marks, ${norev} with an unknown revise chapter`);
}
console.log('mocks', Object.keys(G.mocks || {}).length);
if (waiting.length) console.log('planned widgets not built yet:', waiting.join(' · '));

// 8 external links (--links): the report-a-mistake links are left out (one per chapter, all to the same form)
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
async function fetchOne(u) {
  for (const method of ['HEAD', 'GET']) {
    try {
      const c = new AbortController(); const t = setTimeout(() => c.abort(), 20000);
      const r = await fetch(u, { method, redirect: 'follow', signal: c.signal, headers: { 'user-agent': UA, accept: 'text/html,*/*' } });
      clearTimeout(t);
      if (r.status < 400 || method === 'GET') return r.status;
    } catch (e) { if (method === 'GET') return (e.cause && e.cause.code) || e.name; }
  }
}
async function links() {
  const urls = [...ext].map(u => u.replace(/&amp;/g, '&')).filter(u => !/github\.com\/[^/]+\/[^/]+\/issues\/new/.test(u));
  const by = {}; let i = 0;
  const work = async () => { while (i < urls.length) { const u = urls[i++]; const k = await fetchOne(u); (by[k] = by[k] || []).push(u); } };
  await Promise.all(Array.from({ length: 12 }, work));
  console.log('external links', urls.length, '·', Object.entries(by).map(([k, v]) => k + ': ' + v.length).join(' · '));
  for (const [k, v] of Object.entries(by)) if (k !== '200') for (const u of v) (k === '403' || k === '429' ? console.log.bind(console, '  refused (open it by hand):') : (x) => out.push('external link ' + k + ': ' + x))(u);
}
(process.argv.includes('--links') ? links() : Promise.resolve()).then(() => {
  console.log(out.length ? '\nPROBLEMS (' + out.length + ')\n' + out.join('\n') : '\nno problems found');
  process.exit(out.length ? 1 : 0);
});
