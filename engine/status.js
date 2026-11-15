// status.js — one line per course: chapters, packages, reviews and the next session to run.
//   node engine/status.js
'use strict';
const path = require('path');
const fs = require('fs');
const { readJson } = require('./util');
const { courseProgress } = require('./progress');

const ROOT = path.join(__dirname, '..');
const dirs = fs.readdirSync(path.join(ROOT, 'courses')).filter(d => fs.existsSync(path.join(ROOT, 'courses', d, 'course.json')));
const order = readJson(path.join(ROOT, 'core', 'core.json')).order;
dirs.sort((a, b) => order.indexOf(a) - order.indexOf(b));
console.log('course  chapters  packages  unreviewed  open fixes  syllabus   next');
const year = new Date().getFullYear();
const warns = [];
let tw = 0, tp = 0;
for (const d of dirs) {
  const dir = path.join(ROOT, 'courses', d);
  const cj = readJson(path.join(dir, 'course.json'));
  const p = courseProgress(dir, cj);
  const end = cj.years ? +String(cj.years).slice(-4) : 0;
  if (end && year >= end) warns.push(`${d}: the ${cj.years} syllabus ${year > end ? 'has ended' : 'ends this year'}: check the board's next syllabus and update FACTS.md`);
  tw += p.written; tp += p.planned;
  console.log(`${d.padEnd(7)} ${`${p.written}/${p.planned}`.padStart(8)}  ${`${p.packagesDone}/${p.packages}`.padStart(8)}  ${String(p.unreviewed.length).padStart(10)}  ${String(p.open).padStart(10)}  ${(cj.years || '-').padEnd(9)}  ${p.next}`);
  for (const w of p.incomplete) console.log(`        ! ${w}`);
}
const core = readJson(path.join(ROOT, 'core', 'core.json'));
const coreN = core.sections.reduce((a, s) => a + s.chapters.length, 0);
const coreW = core.sections.reduce((a, s) => a + s.chapters.filter(c => fs.existsSync(path.join(ROOT, 'core', c.id + '.md'))).length, 0);
console.log(`core    ${`${coreW}/${coreN}`.padStart(8)}  (Organizer)`);
console.log(`total   ${`${tw + coreW}/${tp + coreN}`.padStart(8)} chapters`);
for (const w of warns) console.log(`! ${w}`);

// Dated facts: a full date in a core page (a deadline, a test sitting, a results day) that is now in the past is a
// fact to renew for the next cycle. "Links checked <date>" lines and dates before last year are history, not facts.
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const DATE_RE = new RegExp(`\\b(\\d{1,2})(?:[–-]\\d{1,2})? (${MONTHS.join('|')}) (20\\d\\d)\\b`, 'g');
const today = new Date(), past = [];
for (const f of fs.readdirSync(path.join(ROOT, 'core')).filter(x => x.endsWith('.md'))) {
  fs.readFileSync(path.join(ROOT, 'core', f), 'utf8').split('\n').forEach((line, i) => {
    if (/Links checked|released on|were released/.test(line)) return;
    for (const m of line.matchAll(DATE_RE)) {
      const d = new Date(+m[3], MONTHS.indexOf(m[2]), +m[1] + 1);
      if (d < today && +m[3] >= year - 1) past.push(`${f}:${i + 1} ${m[0]}`);
    }
  });
}
if (past.length) console.log(`! dated facts: ${past.length} date(s) in core pages are now in the past; renew them for the next cycle (FACTS.md): ${past.slice(0, 6).join(' · ')}${past.length > 6 ? ' …' : ''}`);
