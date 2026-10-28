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

const ROOT = path.join(__dirname, '..');
const { core, sources: coreSources } = loadCore(path.join(ROOT, 'core'));
const courses = fs.readdirSync(path.join(ROOT, 'courses')).filter(d => fs.existsSync(path.join(ROOT, 'courses', d, 'course.json')))
  .map(d => loadCourse(path.join(ROOT, 'courses', d)));

const assets = require('./assets');
const res = buildSite([...coreSources, ...courses], {
  order: core.order,
  formulaSheets: core.formulaSheets,
  linkSheets: core.linkSheets,
  assets,
  head: pwa.head(assets.css),
  fontFace: (chars) => mathFontFace(path.join(__dirname, 'latinmodern-math.otf'), chars)
});
Object.assign(res.files, pwa.pwaFiles(res.files, assets.css));
writeSite(path.join(ROOT, 'site'), res.files);

const s = res.stats;
const size = Object.values(res.files).reduce((a, f) => a + Buffer.byteLength(f), 0);
console.log(`chapters ${s.chapters}/${s.planned}  words ${s.words}  math ${s.math}  quiz ${s.quiz}  glossary ${s.glossary}  size ${(size / 1024).toFixed(0)} KB (index ${(Buffer.byteLength(res.files['index.html']) / 1024).toFixed(0)} KB)`);
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
