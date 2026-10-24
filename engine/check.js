// check.js — validates the whole project without writing anything.
//   node engine/check.js              errors for everything + a checklist summary per course
//   node engine/check.js math core    details for some courses (core = Organizer chapters)
//   node engine/check.js --py         also run every courses/*/checks/*.py
'use strict';
const path = require('path');
const fs = require('fs');
const { buildSite } = require('./site');
const { loadCore, loadCourse, runPython } = require('./util');
const { lintChapter } = require('./lint');

const ROOT = path.join(__dirname, '..');
const args = process.argv.slice(2);
const runPy = args.includes('--py');
const only = args.filter(a => !a.startsWith('--'));
const { core, sources: coreSources } = loadCore(path.join(ROOT, 'core'));
const courses = fs.readdirSync(path.join(ROOT, 'courses')).filter(d => fs.existsSync(path.join(ROOT, 'courses', d, 'course.json')))
  .map(d => loadCourse(path.join(ROOT, 'courses', d)));
const sources = [...coreSources, ...courses].sort((a, b) => core.order.indexOf(a.id) - core.order.indexOf(b.id));
const res = buildSite(sources, { order: core.order, formulaSheets: core.formulaSheets, linkSheets: core.linkSheets, assets: require('./assets'), write: false });

let bad = res.errors.length;
const rows = [];
for (const s of sources) {
  const group = s.kind === 'core' ? 'core' : s.id;
  const chs = res.chapters.filter(c => c.src === s); // by source file (core about.<c> pages show in a course section)
  let notes = 0, pyFail = 0, pyRun = 0;
  const detail = [];
  for (const c of chs) {
    const text = s.files.find(f => f.name === c.file).text;
    const check = s.dir ? path.join(s.dir, 'checks', c.id + '.py') : null;
    const L = lintChapter(c, text, { course: s.id, hasCheck: check ? fs.existsSync(check) : undefined });
    bad += L.errors.length;
    notes += L.notes.length;
    for (const e of L.errors) res.errors.push(`[${c.id}] ${e}`);
    if (L.notes.length) detail.push(`  ${c.id}: ${L.notes.join('; ')}`);
    if (runPy && check && fs.existsSync(check)) {
      pyRun++;
      const r = runPython([check], { cwd: s.dir });
      if (!r.ok) { pyFail++; bad++; res.errors.push(`[${c.id}] checks/${c.id}.py failed: ${r.out.trim().split('\n').slice(-2).join(' | ')}`); }
    }
  }
  rows.push({ id: s.id, group, n: chs.length, p: s.chapters.length, notes, py: runPy ? `${pyRun - pyFail}/${pyRun} py ok` : '', detail });
}

console.log('section   written  checklist notes' + (runPy ? '  python checks' : ''));
for (const r of rows) console.log(`${r.id.padEnd(9)} ${String(r.n).padStart(3)}/${String(r.p).padEnd(4)} ${String(r.notes).padStart(6)}${runPy ? '           ' + r.py : ''}`);
for (const r of rows) if (only.includes(r.id) || only.includes(r.group)) { console.log(`\n${r.id} checklist:`); console.log(r.detail.join('\n') || '  (nothing)'); }
if (res.errors.length) { console.log(`\n${res.errors.length} ERROR(S):`); for (const e of res.errors.slice(0, 150)) console.log(' - ' + e); }
else console.log('\n0 errors');
if (args.includes('--warn')) for (const w of res.warnings) console.log(' · ' + w);
process.exit(bad ? 1 : 0);
