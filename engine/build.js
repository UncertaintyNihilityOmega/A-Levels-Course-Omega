// build.js — builds the finished guide: site/index.html (open it by double-click) + site/c/<course>.js chunks,
//   plus the installable-app files (pwa.js: manifest, icons, sw.js).
//   node engine/build.js            build; prints errors
//   node engine/build.js --strict   exit 1 on any error
//   node engine/build.js --warn     also print warnings
'use strict';
const path = require('path');
const fs = require('fs');
const { buildSite } = require('./site');
const { loadCore, loadCourse, mathFontFace, writeSite } = require('./util');
const pwa = require('./pwa');
const { staticPages } = require('./pages');

const ROOT = path.join(__dirname, '..');
const { core, sources: coreSources } = loadCore(path.join(ROOT, 'core'));
const courses = fs.readdirSync(path.join(ROOT, 'courses')).filter(d => fs.existsSync(path.join(ROOT, 'courses', d, 'course.json')))
  .map(d => loadCourse(path.join(ROOT, 'courses', d)));

const assets = require('./assets');
/** the public URL of the site from package.json "homepage" ('' if none): canonical links, sharing tags, sitemap.xml */
function homepage() {
  try { const h = String(require('../package.json').homepage || ''); return /^https:\/\//.test(h) ? h.replace(/\/*$/, '/') : ''; } catch (e) { return ''; }
}
/** "https://github.com/<owner>/<repo>/issues" from package.json "repository" ('' if it is not a GitHub URL) */
function repoIssues() {
  try {
    const r = require('../package.json').repository;
    const m = String((r && r.url) || r || '').match(/^https:\/\/github\.com\/[\w.-]+\/[\w.-]+?(?=\.git$|$)/);
    return m ? m[0] + '/issues' : '';
  } catch (e) { return ''; }
}
/** Google Search Console "HTML tag" check: package.json "googleSiteVerification" holds the code Google gives
 *  (the content="…" value); the tag then goes into the head of index.html. Empty: no tag. */
function siteVerification() {
  try { const v = String(require('../package.json').googleSiteVerification || '').trim(); return /^[\w-]{10,100}$/.test(v) ? `\n<meta name="google-site-verification" content="${v}">` : ''; } catch (e) { return ''; }
}
const res = buildSite([...coreSources, ...courses], {
  order: core.order,
  formulaSheets: core.formulaSheets,
  linkSheets: core.linkSheets,
  assets,
  issues: repoIssues(),
  head: pwa.head(assets.css, homepage()) + siteVerification(),
  fontFace: (chars) => mathFontFace(path.join(__dirname, 'latinmodern-math.otf'), chars)
});
Object.assign(res.files, pwa.pwaFiles(res.files, assets.css));
// findable pages (p/<chapter>.html, sitemap.xml): added after the PWA files, so the offline copy leaves them out
const appSize = Object.values(res.files).reduce((a, f) => a + Buffer.byteLength(f), 0);
Object.assign(res.files, staticPages(res, { css: assets.css, homepage: homepage() }));
writeSite(path.join(ROOT, 'site'), res.files);

const s = res.stats;
const size = Object.values(res.files).reduce((a, f) => a + Buffer.byteLength(f), 0);
const kb = (n) => (n / 1024).toFixed(0);
const pageSizes = Object.entries(res.files).filter(([f]) => /^c\/[^/]+\//.test(f)).map(([, v]) => Buffer.byteLength(v));
console.log(`chapters ${s.chapters}/${s.planned}  words ${s.words}  math ${s.math}  quiz ${s.quiz}  glossary ${s.glossary}  app ${kb(appSize)} KB (index ${kb(Buffer.byteLength(res.files['index.html']))} KB; largest chapter file ${kb(Math.max(0, ...pageSizes))} KB)  static pages ${kb(size - appSize)} KB`);
console.log('by section', Object.entries(s.by).map(([k, v]) => `${k} ${v}`).join(' · '));
if (s.soonLinks) console.log(`${s.soonLinks} link(s) to chapters not written yet (shown as plain text)`);
if (res.errors.length) {
  console.log(`\n${res.errors.length} ERROR(S):`);
  for (const e of res.errors.slice(0, 150)) console.log(' - ' + e);
}
if (process.argv.includes('--warn') && res.warnings.length) {
  console.log(`\n${res.warnings.length} warning(s):`);
  for (const e of res.warnings.slice(0, 80)) console.log(' - ' + e);
}
console.log(`\nOpen: ${path.join(ROOT, 'site', 'index.html')}`);
if (res.errors.length && process.argv.includes('--strict')) process.exit(1);
