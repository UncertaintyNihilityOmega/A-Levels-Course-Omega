// progress.js — reads a course's STATUS.md / REVIEW.md / course.json and decides the next session.
//
// STATUS.md lines (one per session, newest last):
//   - 2026-10-04 · LEAD · plan + packages P1–P7 + gold chapter math.p1.quadratics · next: WRITE P1
//   - 2026-10-05 · WRITE P1 · 6 chapters, widgets normal · next: WRITE P2
//   - 2026-10-07 · REVIEW P1–P2 · 3 fixes in REVIEW.md · next: FIX
//   - 2026-10-07 · FIX · REVIEW.md items closed · next: WRITE P3
//   - 2026-11-20 · REVIEW FINAL · course complete
// REVIEW.md: open items are lines starting "- [ ]"; closed items "- [x]".
'use strict';
const fs = require('fs');
const path = require('path');

function readLines(p) { return fs.existsSync(p) ? fs.readFileSync(p, 'utf8').split(/\r?\n/) : []; }

function courseProgress(dir, course) {
  const lines = readLines(path.join(dir, 'STATUS.md')).filter(l => /^\s*-\s.*·/.test(l));
  const open = readLines(path.join(dir, 'REVIEW.md')).filter(l => /^\s*- \[ \]/.test(l));
  const written = new Set(fs.existsSync(path.join(dir, 'chapters')) ? fs.readdirSync(path.join(dir, 'chapters')).filter(f => f.endsWith('.md')).map(f => f.slice(0, -3)) : []);
  const pk = course.packages || [];
  const lead = course.lead !== false;
  let hadLead = false, finalReview = false, unreviewed = [];
  const done = new Set();
  for (const l of lines) {
    const step = (l.split('·')[1] || '').trim();
    if (/^LEAD\b/i.test(step)) hadLead = true;
    const w = step.match(/^WRITE\s+(P\d+)/i);
    if (w) { done.add(w[1].toUpperCase()); unreviewed.push(w[1].toUpperCase()); }
    if (/^REVIEW\b/i.test(step)) { unreviewed = []; if (/FINAL/i.test(step)) finalReview = true; }
  }
  const missing = (p) => (p.chapters || []).filter(id => !written.has(id));
  const incomplete = pk.filter(p => done.has(p.id) && missing(p).length).map(p => `${p.id} is marked written but lacks ${missing(p).join(', ')}`);
  let next, why = '';
  const nextPk = pk.find(p => !done.has(p.id));
  if (lead && (!hadLead || !pk.length)) { next = 'LEAD'; why = pk.length ? 'no LEAD line in STATUS.md yet' : 'no packages in course.json yet'; }
  else if (!pk.length) { next = 'ORGANIZER'; why = 'no packages in course.json: the Organizer plans this course'; }
  else if (open.length) { next = 'FIX'; why = `${open.length} open item(s) in REVIEW.md`; }
  else if (lead && unreviewed.length >= 2) { next = 'REVIEW'; why = `packages ${unreviewed.join(', ')} not reviewed yet`; }
  else if (nextPk) { next = `WRITE ${nextPk.id}`; why = [nextPk.title, (nextPk.chapters || []).join(', '), nextPk.widgets && nextPk.widgets.length ? 'widgets: ' + nextPk.widgets.join(', ') : ''].filter(Boolean).join(' · '); }
  else if (lead && !finalReview) { next = 'REVIEW FINAL'; why = 'all packages written'; }
  else { next = 'DONE'; why = 'course complete: tell the Organizer'; }
  return {
    next, why, open: open.length, unreviewed, incomplete, hadLead,
    packages: pk.length, packagesDone: pk.filter(p => done.has(p.id)).length,
    planned: (course.chapters || []).length, written: (course.chapters || []).filter(c => written.has(c.id)).length
  };
}

module.exports = { courseProgress };
