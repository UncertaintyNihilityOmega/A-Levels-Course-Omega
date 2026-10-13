// progress.js — reads and updates a course's STATUS.md, and decides what each role can do next.
//
// STATUS.md keeps the current state, not a log. The kit writes it (`claim`, `done`); sessions never edit these lines:
//   Last: 2026-10-13 · WRITE P5 · what the last session did
//   - LEAD: done 2026-10-03
//   - P1: reviewed 2026-10-05        (open → writing → written → reviewed)
//   - P2: writing 2026-10-06
//   - FINAL: open
// A package with no line is open. REVIEW.md: open items are lines starting "- [ ]".
// Several Writers may work at once, each on its own claimed package, up to AHEAD packages past the last review.
'use strict';
const fs = require('fs');
const path = require('path');

const AHEAD = 4;
const STEP_RE = /^- (LEAD|FINAL|P\d+): (open|writing|written|reviewed|done)\b(.*)$/;
const today = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
const readLines = (p) => fs.existsSync(p) ? fs.readFileSync(p, 'utf8').split(/\r?\n/) : [];

function readStatus(dir) {
  const steps = {};
  let last = '';
  for (const l of readLines(path.join(dir, 'STATUS.md'))) {
    const m = l.match(STEP_RE);
    if (m) steps[m[1]] = { state: m[2], rest: m[3].trim() };
    else if (/^Last:/.test(l)) last = l.slice(5).trim();
  }
  return { steps, last };
}

function writeStatus(dir, title, course, { steps, last }) {
  const pk = course.packages || [];
  const line = (id, def) => { const s = steps[id] || { state: def, rest: '' }; return `- ${id}: ${s.state}${s.rest ? ' ' + s.rest : ''}`; };
  const out = [`# STATUS: ${title}`, '', `Last: ${last || '(nothing yet)'}`, '',
    '## Steps', 'The kit writes these lines (`node kit/zta.js claim` and `done`). Never edit them by hand.'];
  if (course.lead !== false) out.push(line('LEAD', 'open'));
  for (const p of pk) out.push(line(p.id, 'open'));
  if (course.lead !== false) out.push(line('FINAL', 'open'));
  fs.writeFileSync(path.join(dir, 'STATUS.md'), out.join('\n') + '\n');
}

function courseProgress(dir, course) {
  const { steps, last } = readStatus(dir);
  const open = readLines(path.join(dir, 'REVIEW.md')).filter(l => /^\s*- \[ \]/.test(l));
  const written = new Set(fs.existsSync(path.join(dir, 'chapters')) ? fs.readdirSync(path.join(dir, 'chapters')).filter(f => f.endsWith('.md')).map(f => f.slice(0, -3)) : []);
  const pk = course.packages || [];
  const lead = course.lead !== false;
  const state = (id) => (steps[id] || { state: 'open' }).state;
  const hadLead = !lead || state('LEAD') === 'done';
  const finalDone = state('FINAL') === 'done';
  const byState = (s) => pk.filter(p => state(p.id) === s).map(p => p.id);
  const writing = byState('writing'), free = byState('open');
  const unreviewed = lead ? byState('written') : [];
  const missing = (p) => (p.chapters || []).filter(id => !written.has(id));
  const incomplete = pk.filter(p => ['written', 'reviewed'].includes(state(p.id)) && missing(p).length).map(p => `${p.id} is marked written but lacks ${missing(p).join(', ')}`);
  const describe = (p) => [p.title, (p.chapters || []).join(', '), p.widgets && p.widgets.length ? 'widgets: ' + p.widgets.join(', ') : ''].filter(Boolean).join(' · ');

  const writer = [], specialist = [];
  if (lead && !hadLead) specialist.push({ step: 'LEAD', why: pk.length ? 'no LEAD done in STATUS.md yet' : 'no packages in course.json yet' });
  else if (!pk.length) writer.push({ step: 'ORGANIZER', why: 'no packages in course.json: the Organizer plans this course' });
  else {
    if (open.length) writer.push({ step: 'FIX', why: `${open.length} open item(s) in REVIEW.md` });
    const allWritten = !free.length && !writing.length;
    if (lead && (unreviewed.length >= 2 || (allWritten && unreviewed.length))) specialist.push({ step: `REVIEW ${unreviewed.join(', ')}`, why: `${unreviewed.length} written package(s) not reviewed yet` });
    if (free.length) {
      if (unreviewed.length + writing.length < AHEAD || !lead) {
        const p = pk.find(x => x.id === free[0]);
        writer.push({ step: `WRITE ${p.id}`, why: describe(p) + (free.length > 1 ? ` (also free: ${free.slice(1).join(', ')})` : '') });
      } else writer.push({ step: 'WAIT', why: `${AHEAD} packages are written or being written past the last review: the Specialist reviews first` });
    } else if (writing.length && !open.length) writer.push({ step: 'WAIT', why: `${writing.join(', ')} being written; no free package` });
    if (lead && allWritten && !unreviewed.length && !open.length && !finalDone) specialist.push({ step: 'REVIEW FINAL', why: 'every package written and reviewed' });
    if ((lead ? finalDone : allWritten) && !open.length) writer.push({ step: 'DONE', why: 'course complete: tell the Organizer' });
  }
  const first = specialist.find(s => s.step === 'LEAD') || writer.find(s => s.step === 'FIX') || specialist[0] || writer[0] || { step: 'DONE', why: '' };
  return {
    next: first.step, why: first.why, writer, specialist, last, steps, open: open.length, unreviewed, writing, free, incomplete, hadLead,
    packages: pk.length, packagesDone: pk.filter(p => ['written', 'reviewed'].includes(state(p.id))).length,
    planned: (course.chapters || []).length, written: (course.chapters || []).filter(c => written.has(c.id)).length
  };
}

/** claim a package for a Writer: the given id, or the first free one. Returns { ok, msg, pkg }. */
function claim(dir, title, course, id) {
  const st = readStatus(dir);
  const p = courseProgress(dir, course);
  const lead = course.lead !== false;
  if (lead && !p.hadLead) return { ok: false, msg: 'the Specialist LEAD has not been done yet' };
  id = id ? id.toUpperCase() : p.free[0];
  const pkg = (course.packages || []).find(x => x.id === id);
  if (!pkg) return { ok: false, msg: id ? `no package ${id} in course.json` : 'no free package to claim' };
  const s = (st.steps[id] || { state: 'open' }).state;
  if (s !== 'open') return { ok: false, msg: `${id} is already ${s}${p.free.length ? ` (free: ${p.free.join(', ')})` : ''}` };
  if (lead && p.unreviewed.length + p.writing.length >= AHEAD) return { ok: false, msg: `${AHEAD} packages are past the last review: the Specialist reviews first` };
  st.steps[id] = { state: 'writing', rest: today() };
  writeStatus(dir, title, course, st);
  return { ok: true, pkg, msg: `claimed ${id}` };
}

/** free a claimed package again (a Writer session that stopped before finishing) */
function release(dir, title, course, id) {
  const st = readStatus(dir);
  id = String(id || '').toUpperCase();
  if (!st.steps[id] || st.steps[id].state !== 'writing') return { ok: false, msg: `${id || '?'} is not being written` };
  st.steps[id] = { state: 'open', rest: '' };
  writeStatus(dir, title, course, st);
  return { ok: true, msg: `released ${id}` };
}

/** record a finished session: step is LEAD, WRITE Pn, FIX, REVIEW, REVIEW FINAL; summary goes in the Last line */
function done(dir, title, course, step, summary) {
  const st = readStatus(dir);
  const p = courseProgress(dir, course);
  const S = String(step || '').toUpperCase().trim();
  const date = today();
  let label = S;
  const w = S.match(/^WRITE\s+(P\d+)$/);
  if (S === 'LEAD') st.steps.LEAD = { state: 'done', rest: date };
  else if (w) {
    const pkg = (course.packages || []).find(x => x.id === w[1]);
    if (!pkg) return { ok: false, msg: `no package ${w[1]} in course.json` };
    const s = (st.steps[w[1]] || { state: 'open' }).state;
    if (s === 'written' || s === 'reviewed') return { ok: false, msg: `${w[1]} is already ${s}` };
    const miss = (pkg.chapters || []).filter(id => !fs.existsSync(path.join(dir, 'chapters', id + '.md')));
    if (miss.length) return { ok: false, msg: `${w[1]} still lacks ${miss.join(', ')}` };
    st.steps[w[1]] = { state: course.lead === false ? 'reviewed' : 'written', rest: date };
  } else if (S === 'REVIEW') {
    if (!p.unreviewed.length) return { ok: false, msg: 'no written package is waiting for review' };
    label = `REVIEW ${p.unreviewed.join(', ')}`;
    for (const id of p.unreviewed) st.steps[id] = { state: 'reviewed', rest: date };
  } else if (S === 'REVIEW FINAL' || S === 'FINAL') {
    const notDone = (course.packages || []).filter(x => (st.steps[x.id] || {}).state !== 'reviewed').map(x => x.id);
    if (notDone.length) return { ok: false, msg: `not reviewed yet: ${notDone.join(', ')}` };
    if (p.open) return { ok: false, msg: `${p.open} open item(s) in REVIEW.md` };
    label = 'REVIEW FINAL';
    st.steps.FINAL = { state: 'done', rest: date };
  } else if (S !== 'FIX') return { ok: false, msg: 'step must be LEAD, "WRITE Pn", FIX, REVIEW or "REVIEW FINAL"' };
  st.last = `${date} · ${label} · ${String(summary || '').replace(/\s+/g, ' ').trim()}`;
  writeStatus(dir, title, course, st);
  return { ok: true, msg: `recorded ${label}` };
}

module.exports = { courseProgress, claim, release, done, writeStatus, readStatus, AHEAD };
