// Zero to A* course kit. Bundled by engine/sync.js into courses/<c>/kit/zta.js (needs only Node, no installs).
// Run from the course folder:
//   node kit/zta.js status                 what each role can do next (LEAD / WRITE Pn / FIX / REVIEW / DONE)
//   node kit/zta.js claim [Pn]             a Writer takes a package (the first free one if none given)
//   node kit/zta.js release Pn             give a claimed package back (the session stopped early)
//   node kit/zta.js done "<step>" "<summary>"   record a finished session in STATUS.md (LEAD, WRITE Pn, FIX, REVIEW, READER, REVIEW FINAL)
//   node kit/zta.js check [id ...]         check chapters (all if none given): maths, blocks, links, figures,
//                                          the STYLE checklist, and checks/<id>.py if it exists
//   node kit/zta.js phone [id ...]         every chapter at phone width (375 px) with all answers open, headless:
//                                          lists inline maths and anything else wider than the screen
//   node kit/zta.js preview                build preview/index.html (this course only, final design)
//   node kit/zta.js widget <name> ["attrs"] [--probe]   test page preview/widget.html for one widget;
//                                          --probe also loads it headless (light, dark, phone) and reports problems
//   node kit/zta.js shot <id> [--dark] [--phone]   the chapter's figures and widgets as PNGs in preview/shots/,
//                                          headless (look at them with the Read tool; no browser pane needed)
//   node kit/zta.js serve                  serve preview/ for the browser pane (http://localhost:<port>/)
'use strict';
const fs = require('fs');
const path = require('path');
const { buildSite, widgetNames } = require('../site');
const { loadCourse, runPython, mathFontFace, writeSite } = require('../util');
const { lintChapter, blocks, without } = require('../lint');
const { courseProgress, claim, release, done } = require('../progress');
const { serve } = require('../serve');
const ASSETS = require('zta:assets');
const LINKS = require('zta:links');

const DIR = path.resolve(__dirname, '..');
const PREVIEW = path.join(DIR, 'preview');
const [cmd, ...args] = process.argv.slice(2);
const course = () => loadCourse(DIR);
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const port = () => LINKS.ports[path.basename(DIR)] || 5199;

function external(c) {
  const m = new Map();
  for (const [id, v] of Object.entries(LINKS.ids)) if (v.s !== c.id) m.set(id, v);
  return m;
}
function site(c, opts) {
  const ext = external(c);
  const extAliases = {};
  for (const [a, t] of Object.entries(LINKS.aliases)) if (!a.startsWith(c.id + '.')) extAliases[a] = t;
  const extWidgets = {};
  for (const [n, o] of Object.entries(LINKS.widgets || {})) if (o !== c.id) extWidgets[n] = o;
  return buildSite([c], { external: ext, externalAliases: extAliases, externalWidgets: extWidgets, assets: ASSETS, ...opts });
}

// ---------- status ----------
function status() {
  const c = course();
  const p = courseProgress(DIR, c.json);
  console.log(`${c.title} (${c.id}) · chapters ${p.written}/${p.planned} · packages ${p.packagesDone}/${p.packages} written · unreviewed ${p.unreviewed.length} · being written ${p.writing.join(', ') || 'none'} · open fixes ${p.open}`);
  if (p.last) console.log(`Last: ${p.last}`);
  for (const w of p.incomplete) console.log('  ! ' + w);
  const show = (role, list) => { for (const s of list) console.log(`${role}: ${s.step}${s.why ? ' — ' + s.why : ''}`); };
  show('Specialist', p.specialist);
  show('Writer', p.writer);
  if (p.writer.some(s => /^WRITE/.test(s.step))) console.log('A Writer starts with `node kit/zta.js claim` (takes the first free package; several Writers can work at once).');
}

function packageNotes(id) {
  const f = path.join('packages', id + '.md');
  return fs.existsSync(path.join(DIR, f)) ? f : `the ${id} notes in COURSE.md`;
}
function claimCmd(id) {
  const c = course();
  const r = claim(DIR, c.title, c.json, id);
  if (!r.ok) { console.log(`✗ ${r.msg}`); process.exitCode = 1; return; }
  const p = r.pkg;
  console.log(`✓ ${r.msg}: ${p.title || ''}`);
  console.log(`chapters: ${(p.chapters || []).join(', ')}${p.widgets && p.widgets.length ? `\nwidgets: ${p.widgets.join(', ')}` : ''}`);
  if (p.notes) console.log(`notes: ${p.notes}`);
  console.log(`read: COURSE.md, kit/STYLE.md, the gold chapter, and ${packageNotes(p.id)}`);
  console.log(`when finished: node kit/zta.js done "WRITE ${p.id}" "<one-line summary>"`);
}
function releaseCmd(id) {
  const c = course();
  const r = release(DIR, c.title, c.json, id);
  console.log(`${r.ok ? '✓' : '✗'} ${r.msg}`);
  if (!r.ok) process.exitCode = 1;
}
function doneCmd(step, summary) {
  const c = course();
  if (!step || !summary) { console.log('usage: node kit/zta.js done "<LEAD | WRITE Pn | FIX | REVIEW | READER | REVIEW FINAL>" "<one-line summary>"'); process.exitCode = 2; return; }
  const r = done(DIR, c.title, c.json, step, summary);
  if (!r.ok) { console.log(`✗ ${r.msg}`); process.exitCode = 1; return; }
  console.log(`✓ ${r.msg}`);
  status();
}

// ---------- check ----------
function check(ids) {
  const c = course();
  const res = site(c, { write: false, inlineAll: true });
  const want = ids.length ? ids.map(a => path.basename(a).replace(/\.md$/, '')) : c.files.map(f => f.name.replace(/.md$/, ''));
  let bad = 0;
  const tagOf = (e) => (e.match(/^\[([^\]]+)\]/) || [])[1];
  const general = res.errors.filter(e => !want.includes(tagOf(e)) && !res.written.has(tagOf(e)) && !res.planned.has(tagOf(e)));
  for (const e of general) { console.log('✗ ' + e); bad++; }
  for (const id of want) {
    const ch = res.written.get(id);
    const tag = `[${id}]`;
    const errs = res.errors.filter(e => e.startsWith(tag)).map(e => e.slice(tag.length).trim());
    const warns = res.warnings.filter(e => e.startsWith(tag)).map(e => e.slice(tag.length).trim());
    if (!ch) {
      const file = path.join(DIR, 'chapters', id + '.md');
      console.log(`✗ ${id}: ${fs.existsSync(file) ? 'could not be read as a chapter' : 'no file chapters/' + id + '.md'}`);
      for (const e of errs) console.log('   - ' + e);
      bad++; continue;
    }
    const text = c.files.find(f => f.name === ch.file).text;
    const pyFile = path.join(DIR, 'checks', id + '.py');
    const L = lintChapter(ch, text, { course: c.id, hasCheck: fs.existsSync(pyFile) });
    errs.push(...L.errors);
    let py = '';
    if (fs.existsSync(pyFile)) {
      const r = runPython([pyFile], { cwd: DIR });
      if (r.ok) py = ' · checks ok';
      else { errs.push(`checks/${id}.py failed:\n     ${r.out.trim().split('\n').slice(-6).join('\n     ')}`); }
    }
    const n = (t) => blocks(without(text, 'proof'), t);
    const counts = `${ch.words} words · ${n('eg').length} eg · ${n('try').join('\n').split('\n').filter(l => /^Q:/.test(l)).length} try · ${n('quiz').join('\n').split('\n').filter(l => /^\? /.test(l)).length} quiz${ch.marks ? ` · ${ch.marks} marks` : ''}`;
    if (errs.length) { bad++; console.log(`✗ ${id} · ${counts}`); for (const e of errs) console.log('   - ' + e); }
    else console.log(`✓ ${id} · ${counts}${py}`);
    for (const w of [...warns, ...L.notes]) console.log('   · ' + w);
  }
  if (!want.length) console.log('No chapters in chapters/ yet.');
  process.exitCode = bad ? 1 : 0;
}

// ---------- preview ----------
function homeArticle(c, res) {
  const rows = c.chapters.map((e, i) => {
    const w = res.written.get(e.id);
    const t = w ? `<a href="#${e.id}">${esc(e.title)}</a>` : `<span class="soon">${esc(e.title)}</span>`;
    return `<tr><td>${i + 1}</td><td>${t}<br><small><code>${e.id}</code></small></td><td>${esc(e.level || '')}</td><td>${esc(e.group || '')}</td><td>${w ? w.words + ' words' : 'not written'}</td></tr>`;
  }).join('');
  const pk = (c.packages || []).map(p => `<li><b>${esc(p.id)}</b> ${esc(p.title || '')}: ${(p.chapters || []).map(esc).join(', ')}</li>`).join('');
  return `<article class="chapter s-${c.id}" id="c-home" data-id="home" data-subject="${c.id}" hidden><header class="ch-head"><h1>${esc(c.title)}: course preview</h1><p class="lede">Only this course is in the preview. Links to other courses and to chapters not written yet show as plain text.</p></header><div class="prose"><div class="tw"><table><thead><tr><th>#</th><th>Chapter</th><th>Level</th><th>Group</th><th>Status</th></tr></thead><tbody>${rows}</tbody></table></div>${pk ? `<h2 id="home--packages">Packages</h2><ul>${pk}</ul>` : ''}</div></article>`;
}
function preview() {
  const c = course();
  const dry = site(c, { write: false, inlineAll: true });
  const res = site(c, { home: homeArticle(c, dry), fontFace: (chars) => mathFontFace(path.join(__dirname, 'math.otf'), chars) });
  fs.mkdirSync(PREVIEW, { recursive: true });
  writeSite(PREVIEW, res.files);
  console.log(`preview: ${res.stats.chapters} chapter(s), ${res.errors.length} error(s)${res.errors.length ? ' (run check)' : ''}`);
  console.log(`view: start the "preview" server (node kit/zta.js serve) and open http://localhost:${port()}/#<chapter-id>`);
}

// ---------- widget test page ----------
function widget(name, attrs, probe) {
  const c = course();
  if (!name) { console.log('usage: node kit/zta.js widget <name> ["data-a=\\"1\\" data-b=\\"2\\""]'); process.exitCode = 2; return; }
  const known = new Set([...widgetNames(ASSETS.study), ...widgetNames(c.widgets)]);
  const owner = (LINKS.widgets || {})[name];
  if (!known.has(name) && owner && owner !== c.id) { console.log(`✗ "${name}" belongs to the ${owner} course: test it there (you can still use it in your chapters)`); process.exitCode = 1; return; }
  if (!known.has(name)) { console.log(`✗ no W.register('${name}', ...) in widgets.js (known: ${[...known].join(', ') || 'none'})`); process.exitCode = 1; return; }
  attrs = attrs || '';
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Widget test: ${esc(name)}</title>
<style>${ASSETS.css}</style><style>
.wt-bar{position:sticky;top:0;z-index:5;display:flex;gap:8px;flex-wrap:wrap;align-items:center;padding:10px 16px;background:var(--card);border-bottom:1px solid var(--rule);font:14px var(--f-body,system-ui)}
.wt-bar code{font-size:12px;color:var(--ink-2)}.wt-main{padding:16px;margin:0 auto;max-width:760px}.phone .wt-main{max-width:380px;outline:1px dashed var(--rule)}
.wt-err{color:var(--red);white-space:pre-wrap;font:13px monospace}</style></head>
<body class="app s-${c.id}"><div class="wt-bar"><b>${esc(name)}</b><code>${esc(attrs)}</code>
<a href="?">light</a> · <a href="?dark">dark</a> · <a href="?phone">phone</a> · <a href="?dark&phone">phone + dark</a></div>
<main class="wt-main" id="main"><article class="chapter s-${c.id}"><div class="prose"><div class="widget" data-w="${esc(name)}" ${attrs}></div></div></article><div class="wt-err" id="wtErr"></div></main>
<script>window.GUIDE={order:[],ch:{},subjects:[],chunks:[]};window.QUIZ={};window.GLOSSARY=[];
var q=location.search;if(/dark/.test(q))document.documentElement.setAttribute('data-theme','dark');if(/phone/.test(q))document.body.classList.add('phone');
window.addEventListener('error',function(e){document.getElementById('wtErr').textContent+='Error: '+e.message+'\\n';});</script>
<script>${ASSETS.core}</script><script>${ASSETS.study}
;
${c.widgets}</script>
<script>document.querySelectorAll('.widget[data-w]').forEach(function(el){var fn=W.reg[el.getAttribute('data-w')];try{fn(el,Object.assign({},el.dataset));}catch(e){document.getElementById('wtErr').textContent+='Widget threw: '+e.message+'\\n'+(e.stack||'');}});</script>
<script>${PROBE_JS}</script>
</body></html>`;
  fs.mkdirSync(PREVIEW, { recursive: true });
  fs.writeFileSync(path.join(PREVIEW, 'widget.html'), html);
  if (probe) fs.writeFileSync(path.join(PREVIEW, `probe-${process.pid}.html`), html);
  console.log(`wrote preview/widget.html — open http://localhost:${port()}/widget.html (add ?dark, ?phone or ?dark&phone)`);
  if (probe) { runProbe(name, `probe-${process.pid}.html`); fs.rmSync(path.join(PREVIEW, `probe-${process.pid}.html`), { force: true }); }
}

// ---------- widget probe: load the test page headless (Edge or Chrome) in light, dark and phone width ----------
// The page collects errors, NaN/undefined/Infinity text, overflow and blank canvases into <pre id="zta-probe">.
const PROBE_JS = `if(/probe/.test(location.search)){var zErr=[];var oe=console.error;console.error=function(){zErr.push([].map.call(arguments,String).join(' '));oe.apply(console,arguments);};
window.addEventListener('error',function(e){zErr.push('Error: '+e.message);});window.addEventListener('unhandledrejection',function(e){zErr.push('Unhandled promise: '+((e.reason&&e.reason.message)||e.reason));});
setTimeout(function(){var root=document.querySelector('.widget');var R={errors:zErr.slice(),bad:[],overflow:[],blank:0,canvases:0,width:innerWidth};
var we=document.getElementById('wtErr').textContent.trim();if(we)R.errors.push(we);
var tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT),n;while((n=tw.nextNode())){if(/NaN|undefined|Infinity/.test(n.nodeValue)&&R.bad.length<8)R.bad.push(n.nodeValue.trim().slice(0,80));}
root.querySelectorAll('input,output').forEach(function(i){if(/NaN|undefined|Infinity/.test(i.value||i.textContent))R.bad.push((i.getAttribute('aria-label')||i.tagName)+' = '+(i.value||i.textContent));});
var de=document.documentElement;if(de.scrollWidth>innerWidth+1)R.overflow.push('the page is '+de.scrollWidth+'px wide in a '+innerWidth+'px window');
var rr=root.getBoundingClientRect();var scrolls=function(el){for(var p=el.parentElement;p&&p!==root;p=p.parentElement){var o=getComputedStyle(p).overflowX;if(o==='auto'||o==='scroll')return true;}return false;};
var edge=function(el){var b=el.parentElement&&el.parentElement.closest('.w-b');if(!b||!root.contains(b))return rr.right;return b.getBoundingClientRect().right-parseFloat(getComputedStyle(b).paddingRight);};
root.querySelectorAll('*').forEach(function(el){var r=el.getBoundingClientRect(),e=edge(el);if(r.width>0&&r.right>e+4&&!scrolls(el)&&R.overflow.length<6)R.overflow.push('<'+el.tagName.toLowerCase()+(el.className&&el.className.baseVal===undefined?' class="'+el.className+'"':'')+'> sticks out '+Math.round(r.right-e)+'px past the widget\\'s padding');});
root.querySelectorAll('canvas').forEach(function(cv){var x=cv.getContext('2d');if(!x||!cv.width||!cv.height)return;R.canvases++;var d=x.getImageData(0,0,cv.width,cv.height).data,any=false;for(var i=3;i<d.length;i+=4*97){if(d[i]){any=true;break;}}if(!any)R.blank++;});
var pre=document.createElement('pre');pre.id='zta-probe';pre.textContent=JSON.stringify(R);document.body.appendChild(pre);},1500);}`;

// ---------- phone width: every chapter at 375 px with all answers and hints open, measured headless ----------
const PHONE_W = 375;
const PHONE_JS = `if(/phone-probe/.test(location.search)){setTimeout(function(){
var want=(new URLSearchParams(location.search).get('ids')||'').split(',').filter(Boolean);
var all=[].slice.call(document.querySelectorAll('article.chapter[data-id]'));
var W=document.documentElement.clientWidth,out=[];
var scrolls=function(el){for(var p=el.parentElement;p;p=p.parentElement){var o=getComputedStyle(p).overflowX;if(o==='auto'||o==='scroll')return true;}return false;};
var label=function(el){var t=(el.textContent||'').replace(/\\s+/g,' ').trim();return t.length>60?t.slice(0,57)+'…':t;};
all.forEach(function(a){var id=a.getAttribute('data-id');if(id==='home'||(want.length&&want.indexOf(id)<0))return;
all.forEach(function(x){x.hidden=x!==a;});a.querySelectorAll('details').forEach(function(d){d.open=true;});
var R={id:id,width:document.documentElement.scrollWidth,inline:[],other:[]};
a.querySelectorAll('.mi').forEach(function(m){var r=m.getBoundingClientRect();if(r.width&&r.right>W+1&&!scrolls(m)&&R.inline.length<12)R.inline.push([Math.round(r.right-W),label(m)]);});
if(R.width>W+1)a.querySelectorAll('*').forEach(function(el){if(el.closest('.mi'))return;var r=el.getBoundingClientRect();if(!r.width||r.right<=W+1||scrolls(el))return;
for(var c=el.firstElementChild;c;c=c.nextElementSibling){if(c.getBoundingClientRect().right>W+1)return;}
if(R.other.length<6)R.other.push([Math.round(r.right-W),'<'+el.tagName.toLowerCase()+'> '+label(el)]);});
out.push(R);});
parent.postMessage(JSON.stringify({w:W,ch:out}),'*');},1500);}`;
// the page runs in a phone-width frame (headless windows cannot be narrower than about 480 px)
const PHONE_FRAME = (src) => `<!doctype html><meta charset="utf-8"><body style="margin:0"><iframe src="${src}" style="width:${PHONE_W}px;height:900px;border:0"></iframe>
<script>addEventListener('message',function(e){var p=document.createElement('pre');p.id='zta-probe';p.textContent=e.data;document.body.appendChild(p);});</script>`;

function phone(ids) {
  const c = course();
  const exe = findBrowser();
  if (!exe) { console.log('phone: no Edge or Chrome found (set ZTA_BROWSER to a Chromium browser).'); process.exitCode = 1; return; }
  const res = site(c, { inlineAll: true, fontFace: (chars) => mathFontFace(path.join(__dirname, 'math.otf'), chars) });
  fs.mkdirSync(PREVIEW, { recursive: true });
  const own = `phone-${process.pid}`;
  fs.writeFileSync(path.join(PREVIEW, own + '.html'), res.files['index.html'].replace('</body>', () => `<style>html{scrollbar-width:none}</style><script>${PHONE_JS}</script></body>`));
  const want = ids.map(a => path.basename(a).replace(/\.md$/, ''));
  fs.writeFileSync(path.join(PREVIEW, own + '-frame.html'), PHONE_FRAME(`${own}.html?phone-probe${want.length ? '&ids=' + encodeURIComponent(want.join(',')) : ''}`));
  const R = headless(own + '-frame.html', 800, 30000);
  for (const f of [own + '.html', own + '-frame.html']) fs.rmSync(path.join(PREVIEW, f), { force: true });
  if (!R) { console.log('✗ phone: the page did not finish; run it again, or ask the Organizer'); process.exitCode = 1; return; }
  let bad = 0;
  for (const ch of R.ch) {
    const n = ch.inline.length + ch.other.length;
    if (!n && ch.width <= R.w + 1) continue;
    bad++;
    console.log(`✗ ${ch.id} · the page is ${ch.width} px wide in a ${R.w} px phone`);
    for (const [px, t] of ch.inline) console.log(`   - inline maths ${px} px past the edge: ${t}`);
    for (const [px, t] of ch.other) console.log(`   - ${px} px past the edge: ${t}`);
  }
  console.log(bad ? `phone: ${bad} of ${R.ch.length} chapter(s) too wide. Put long chains in \\[ … \\] (aligned for 3+ steps), then run phone again.`
    : `phone: all ${R.ch.length} chapter(s) fit ${R.w} px with every answer open.`);
  if (bad) process.exitCode = 1;
}

/** load preview/<page> headless at the given width and return the JSON it writes into <pre id="zta-probe"> */
function headless(page, width, budget) {
  const { pathToFileURL } = require('url');
  const [file, query] = page.split('?');
  const r = dumpDom(`${pathToFileURL(path.join(PREVIEW, file)).href}${query ? '?' + query : ''}`, width, budget, 180000);
  const m = (r.stdout || '').match(/<pre id="zta-probe">([\s\S]*?)<\/pre>/);
  if (!m) return null;
  return JSON.parse(m[1].replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&'));
}

function browsers() {
  const pf = process.env['ProgramFiles'] || 'C:\\Program Files', pf86 = process.env['ProgramFiles(x86)'] || 'C:\\Program Files (x86)', la = process.env.LOCALAPPDATA || '';
  const list = [process.env.ZTA_BROWSER,
    path.join(pf86, 'Microsoft/Edge/Application/msedge.exe'), path.join(pf, 'Microsoft/Edge/Application/msedge.exe'),
    path.join(pf, 'Google/Chrome/Application/chrome.exe'), path.join(pf86, 'Google/Chrome/Application/chrome.exe'), path.join(la, 'Google/Chrome/Application/chrome.exe'),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/microsoft-edge'];
  return [...new Set(list.filter(p => p && fs.existsSync(p)))];
}
const findBrowser = () => browsers()[0];
// A browser can be installed but broken headless (Edge 155 on 2026-10-14 printed nothing at all), so try each
// one until it returns a page, and remember the one that worked.
let goodBrowser = null;
function dumpDom(url, width, budget, timeout) {
  const { spawnSync } = require('child_process');
  const os = require('os');
  let last = null;
  for (const exe of goodBrowser ? [goodBrowser] : browsers()) {
    const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'zta-probe-'));
    const r = spawnSync(exe, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--disable-extensions', `--user-data-dir=${prof}`,
      `--window-size=${width},900`, `--virtual-time-budget=${budget}`, '--dump-dom', url], { encoding: 'utf8', timeout, maxBuffer: 256 * 1024 * 1024 });
    try { fs.rmSync(prof, { recursive: true, force: true }); } catch (e) { /* the browser may still hold it */ }
    last = r;
    if (/<html/i.test(r.stdout || '')) { goodBrowser = exe; return r; }
  }
  return last || { stdout: '', error: new Error('no Edge or Chrome found (set ZTA_BROWSER)') };
}
function runProbe(name, file) {
  const exe = findBrowser();
  if (!exe) { console.log('probe: no Edge or Chrome found (set ZTA_BROWSER to a Chromium browser). Open the page in the browser pane instead.'); return; }
  const { pathToFileURL } = require('url');
  const page = pathToFileURL(path.join(PREVIEW, file)).href;
  const dec = (s) => s.replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
  let problems = 0;
  for (const [label, q, w] of [['light', '', 1000], ['dark', 'dark', 1000], ['phone', 'phone', 400]]) {
    let r, m, R;
    // the first headless run after a widget file changes can report blank canvases (cold cache); retry once before flagging
    for (let tries = 0; tries < 2; tries++) {
      r = dumpDom(`${page}?probe${q ? '&' + q : ''}`, w, 6000, 60000);
      m = (r.stdout || '').match(/<pre id="zta-probe">([\s\S]*?)<\/pre>/);
      R = m && JSON.parse(dec(m[1]));
      if (R && !R.blank) break;
    }
    if (!m) { problems++; console.log(`✗ ${label}: the page did not finish (${r.error ? r.error.message : 'no report'}); open it in the browser pane`); continue; }
    const out = [];
    const errs = [...new Set(R.errors.flatMap(e => e.split('\n')).map(e => e.trim()).filter(e => e && !/^at\s/.test(e)))];
    for (const e of errs) out.push('error: ' + e.slice(0, 160));
    for (const b of R.bad) out.push('shows "' + b + '"');
    for (const o of R.overflow) out.push('overflow: ' + o);
    if (R.blank) out.push(`${R.blank} of ${R.canvases} canvas(es) drawn blank`);
    problems += out.length;
    console.log(`${out.length ? '✗' : '✓'} ${label} (${R.width}px)${out.length ? '' : ` · ${R.canvases} canvas(es) drawn, no errors`}`);
    for (const o of out) console.log('   - ' + o);
  }
  if (problems) process.exitCode = 1;
  console.log(problems ? `probe: ${problems} problem(s) in "${name}". Fix them, then probe again.` : `probe: "${name}" passed. Still look at it once in the browser pane (light, dark, phone).`);
}

// ---------- shot: a chapter's figures and widgets as PNGs, headless (no browser pane needed) ----------
// The page shows the chapter (route + hydrate), then hides everything but its figures and widgets (answers open),
// numbers them, and either reports their heights (measure) or shows the range from..to for a screenshot.
const SHOT_JS = `if(/[?&]shot/.test(location.search)){setTimeout(function(){
var P=new URLSearchParams(location.search),id=location.hash.slice(1);
document.documentElement.setAttribute('data-theme',P.has('dark')?'dark':'light');if(window.W&&W.themeChanged)W.themeChanged();
var out=function(R){var s=JSON.stringify(R);if(parent!==window)parent.postMessage(s,'*');else{var p=document.createElement('pre');p.id='zta-probe';p.textContent=s;document.body.appendChild(p);}};
var a=document.querySelector('article.chapter[data-id="'+id+'"]');if(!a){out({error:'no chapter '+id});return;}
a.querySelectorAll('details').forEach(function(d){d.open=true;});a.classList.add('mock-done');
var T=[].slice.call(a.querySelectorAll('figure,.widget')).filter(function(t){return !t.parentElement.closest('figure,.widget');});
var from=+(P.get('from')||0),to=P.has('to')?+P.get('to'):T.length,K=T.slice(from,to);
document.body.querySelectorAll('*').forEach(function(el){if(/^(SCRIPT|STYLE|PRE)$/.test(el.tagName))return;
if(K.some(function(t){return t===el||t.contains(el)||el.contains(t);}))return;
if(el.closest('.svgdefs')||el.querySelector('.svgdefs'))return;el.style.display='none';});
var css=document.createElement('style');css.textContent='html,body{overflow:visible!important}body *{margin-top:0}.zshot{font:600 13px system-ui;color:var(--ink-2);padding:14px 0 4px}';document.head.appendChild(css);
var R={n:T.length,items:[]};
K.forEach(function(t,i){var k=from+i,lab=document.createElement('div');lab.className='zshot';
var name=t.classList.contains('widget')?'widget '+t.getAttribute('data-w'):'figure: '+((t.querySelector('figcaption')||{}).textContent||'').replace(/\\s+/g,' ').trim().slice(0,70);
lab.textContent='#'+(k+1)+' '+name;t.parentNode.insertBefore(lab,t);R.items.push(name);});
scrollTo(0,0);if(window.W&&W.themeChanged)W.themeChanged();setTimeout(function(){R.h=K.map(function(t){return Math.ceil(t.getBoundingClientRect().height)+40;});R.total=document.documentElement.scrollHeight;out(R);},300);},1800);}`;
const SHOT_FRAME = (src, w, h) => `<!doctype html><meta charset="utf-8"><body style="margin:0"><iframe src="${src}" style="width:${w}px;height:${h}px;border:0;display:block"></iframe>
<script>addEventListener('message',function(e){var p=document.createElement('pre');p.id='zta-probe';p.textContent=e.data;document.body.appendChild(p);});</script>`;

function shot(id, dark, phoneW) {
  const c = course();
  if (!id) { console.log('usage: node kit/zta.js shot <chapter-id> [--dark] [--phone]'); process.exitCode = 2; return; }
  id = path.basename(id).replace(/\.md$/, '');
  if (!findBrowser()) { console.log('shot: no Edge or Chrome found (set ZTA_BROWSER to a Chromium browser).'); process.exitCode = 1; return; }
  const res = site(c, { inlineAll: true, fontFace: (chars) => mathFontFace(path.join(__dirname, 'math.otf'), chars) });
  fs.mkdirSync(path.join(PREVIEW, 'shots'), { recursive: true });
  const own = `shot-${process.pid}`, W = phoneW ? PHONE_W : 800;
  fs.writeFileSync(path.join(PREVIEW, own + '.html'), res.files['index.html'].replace('</body>', () => `<script>${SHOT_JS}</script></body>`));
  const { pathToFileURL } = require('url');
  const base = pathToFileURL(path.join(PREVIEW, own + '.html')).href;
  const q = (extra) => `${base}?shot${dark ? '&dark' : ''}${extra}#${id}`;
  // pass 1: measure every figure in a frame of the target width
  fs.writeFileSync(path.join(PREVIEW, own + '-frame.html'), SHOT_FRAME(q(''), W, 900));
  const m = (dumpDom(pathToFileURL(path.join(PREVIEW, own + '-frame.html')).href, W + 100, 8000, 120000).stdout || '').match(/<pre id="zta-probe">([\s\S]*?)<\/pre>/);
  const R = m && JSON.parse(m[1].replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&'));
  const clean = () => { for (const f of [own + '.html', own + '-frame.html']) fs.rmSync(path.join(PREVIEW, f), { force: true }); };
  if (!R || R.error) { clean(); console.log(`✗ shot: ${R ? R.error : 'the page did not finish'}`); process.exitCode = 1; return; }
  if (!R.n) { clean(); console.log(`shot: ${id} has no figures or widgets`); return; }
  // pass 2: one PNG per group of figures up to about 1400 px tall
  const groups = [];
  R.h.forEach((h, i) => { const g = groups[groups.length - 1]; if (g && g.h + h <= 1100) { g.to = i + 1; g.h += h; } else groups.push({ from: i, to: i + 1, h }); });
  const { spawnSync } = require('child_process');
  const os = require('os');
  const tag = `${id}${dark ? '-dark' : ''}${phoneW ? '-phone' : ''}`;
  for (const old of fs.readdirSync(path.join(PREVIEW, 'shots'))) if (old.startsWith(tag + '-')) fs.rmSync(path.join(PREVIEW, 'shots', old), { force: true });
  const made = [];
  for (const g of groups) {
    // the boxes around each figure (question cards, padding) add height, so measure this group as it will be shown
    fs.writeFileSync(path.join(PREVIEW, own + '-frame.html'), SHOT_FRAME(q(`&from=${g.from}&to=${g.to}`), W, 900));
    const gm = (dumpDom(pathToFileURL(path.join(PREVIEW, own + '-frame.html')).href, W + 100, 8000, 120000).stdout || '').match(/<pre id="zta-probe">([\s\S]*?)<\/pre>/);
    const total = gm ? JSON.parse(gm[1].replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')).total : 0;
    const H = Math.max(g.h + 120, (total || 0) + 20);
    fs.writeFileSync(path.join(PREVIEW, own + '-frame.html'), SHOT_FRAME(q(`&from=${g.from}&to=${g.to}`), W, H));
    const file = path.join(PREVIEW, 'shots', `${tag}-${g.from + 1}.png`);
    const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'zta-shot-'));
    spawnSync(goodBrowser || findBrowser(), ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--hide-scrollbars',
      `--user-data-dir=${prof}`, `--window-size=${Math.max(W, 500)},${H}`, '--virtual-time-budget=8000', `--screenshot=${file}`,
      pathToFileURL(path.join(PREVIEW, own + '-frame.html')).href], { timeout: 120000 });
    try { fs.rmSync(prof, { recursive: true, force: true }); } catch (e) { /* still held */ }
    made.push(fs.existsSync(file) ? `${path.relative(DIR, file).replace(/\\/g, '/')}  (#${g.from + 1}–#${g.to})` : `✗ #${g.from + 1}–#${g.to}: no image`);
  }
  clean();
  console.log(`shot: ${id}${dark ? ' dark' : ''}${phoneW ? ' phone' : ''} · ${R.n} figure(s)/widget(s):`);
  R.items.forEach((t, i) => console.log(`  #${i + 1} ${t}`));
  console.log('images (open them with the Read tool):');
  for (const f of made) console.log('  ' + f);
}

switch (cmd) {
  case 'status': status(); break;
  case 'shot': shot(args.find(a => !a.startsWith('--')), args.includes('--dark'), args.includes('--phone')); break;
  case 'claim': claimCmd(args[0]); break;
  case 'release': releaseCmd(args[0]); break;
  case 'done': doneCmd(args[0], args.slice(1).join(' ')); break;
  case 'check': check(args); break;
  case 'preview': preview(); break;
  case 'widget': widget(args[0], args.slice(1).filter(a => a !== '--probe').join(' '), args.includes('--probe')); break;
  case 'phone': phone(args); break;
  case 'serve': fs.mkdirSync(PREVIEW, { recursive: true }); serve(PREVIEW, Number(args[0]) || port()); break;
  default: console.log('commands: status | claim [Pn] | release Pn | done "<step>" "<summary>" | check [id ...] | phone [id ...] | preview | widget <name> ["attrs"] [--probe] | shot <id> [--dark] [--phone] | serve'); process.exitCode = cmd ? 2 : 0;
}
