// Zero to A* course kit. Bundled by engine/sync.js into courses/<c>/kit/zta.js (needs only Node, no installs).
// Run from the course folder:
//   node kit/zta.js status                 what to do next (LEAD / WRITE Pn / FIX / REVIEW / DONE)
//   node kit/zta.js check [id ...]         check chapters (all if none given): maths, blocks, links, figures,
//                                          the STYLE checklist, and checks/<id>.py if it exists
//   node kit/zta.js preview                build preview/index.html (this course only, final design)
//   node kit/zta.js widget <name> ["attrs"] [--probe]   test page preview/widget.html for one widget;
//                                          --probe also loads it headless (light, dark, phone) and reports problems
//   node kit/zta.js serve                  serve preview/ for the browser pane (http://localhost:<port>/)
'use strict';
const fs = require('fs');
const path = require('path');
const { buildSite, widgetNames } = require('../site');
const { loadCourse, runPython, mathFontFace, writeSite } = require('../util');
const { lintChapter, blocks, without } = require('../lint');
const { courseProgress } = require('../progress');
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
  console.log(`${c.title} (${c.id}) · chapters ${p.written}/${p.planned} · packages ${p.packagesDone}/${p.packages} · unreviewed ${p.unreviewed.length} · open fixes ${p.open}`);
  for (const w of p.incomplete) console.log('  ! ' + w);
  console.log(`NEXT: ${p.next}${p.why ? ' — ' + p.why : ''}`);
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
  console.log(`wrote preview/widget.html — open http://localhost:${port()}/widget.html (add ?dark, ?phone or ?dark&phone)`);
  if (probe) runProbe(name);
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

function findBrowser() {
  const pf = process.env['ProgramFiles'] || 'C:\\Program Files', pf86 = process.env['ProgramFiles(x86)'] || 'C:\\Program Files (x86)', la = process.env.LOCALAPPDATA || '';
  const list = [process.env.ZTA_BROWSER,
    path.join(pf86, 'Microsoft/Edge/Application/msedge.exe'), path.join(pf, 'Microsoft/Edge/Application/msedge.exe'),
    path.join(pf, 'Google/Chrome/Application/chrome.exe'), path.join(pf86, 'Google/Chrome/Application/chrome.exe'), path.join(la, 'Google/Chrome/Application/chrome.exe'),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/microsoft-edge'];
  return list.find(p => p && fs.existsSync(p));
}
function runProbe(name) {
  const exe = findBrowser();
  if (!exe) { console.log('probe: no Edge or Chrome found (set ZTA_BROWSER to a Chromium browser). Open the page in the browser pane instead.'); return; }
  const { spawnSync } = require('child_process');
  const { pathToFileURL } = require('url');
  const os = require('os');
  const page = pathToFileURL(path.join(PREVIEW, 'widget.html')).href;
  const dec = (s) => s.replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
  let problems = 0;
  for (const [label, q, w] of [['light', '', 1000], ['dark', 'dark', 1000], ['phone', 'phone', 400]]) {
    const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'zta-probe-'));
    const r = spawnSync(exe, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--disable-extensions', `--user-data-dir=${prof}`,
      `--window-size=${w},900`, '--virtual-time-budget=6000', '--dump-dom', `${page}?probe${q ? '&' + q : ''}`], { encoding: 'utf8', timeout: 60000, maxBuffer: 64 * 1024 * 1024 });
    try { fs.rmSync(prof, { recursive: true, force: true }); } catch (e) { /* the browser may still hold it */ }
    const m = (r.stdout || '').match(/<pre id="zta-probe">([\s\S]*?)<\/pre>/);
    if (!m) { problems++; console.log(`✗ ${label}: the page did not finish (${r.error ? r.error.message : 'no report'}); open it in the browser pane`); continue; }
    const R = JSON.parse(dec(m[1]));
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

switch (cmd) {
  case 'status': status(); break;
  case 'check': check(args); break;
  case 'preview': preview(); break;
  case 'widget': widget(args[0], args.slice(1).filter(a => a !== '--probe').join(' '), args.includes('--probe')); break;
  case 'serve': fs.mkdirSync(PREVIEW, { recursive: true }); serve(PREVIEW, Number(args[0]) || port()); break;
  default: console.log('commands: status | check [id ...] | preview | widget <name> ["attrs"] [--probe] | serve'); process.exitCode = cmd ? 2 : 0;
}
