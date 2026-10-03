#!/usr/bin/env node
// Validate one or more content files.  Usage: node tools/check.js content/math-1.md [more files...]
// Checks: TeX errors, block syntax, quiz/try format, chapter ids vs outline, internal links, headings, word counts.
const fs = require('fs');
const path = require('path');
const { createRenderer } = require('../lib');

const ROOT = path.join(__dirname, '..');
const outline = JSON.parse(fs.readFileSync(path.join(ROOT, 'src/outline.json'), 'utf8'));
const planned = new Map();
for (const s of outline.subjects) for (const c of s.chapters) planned.set(c.id, { ...c, subject: s.id });

const files = process.argv.slice(2);
if (!files.length) { console.log('Usage: node tools/check.js content/<file>.md'); process.exit(2); }
let totalErrors = 0;
for (const f of files) {
  const fp = path.resolve(f);
  const base = path.basename(fp);
  const subj = outline.subjects.find(s => s.files.includes(base));
  if (!subj) { console.log(`✗ ${base}: not listed in src/outline.json`); totalErrors++; continue; }
  const R = createRenderer();
  const { chapters } = R.renderFile(fs.readFileSync(fp, 'utf8'), subj.id, base);
  const errs = [...R.st.errors];
  const expected = subj.chapters.filter(c => c.file === base).map(c => c.id);
  const got = chapters.map(c => c.id);
  for (const id of expected) if (!got.includes(id)) errs.push(`missing chapter @chapter ${id} (expected in this file)`);
  for (const id of got) {
    if (!planned.has(id)) errs.push(`@chapter ${id} is not in the outline (check spelling)`);
    else if (planned.get(id).file !== base) errs.push(`@chapter ${id} belongs in ${planned.get(id).file}, not ${base}`);
  }
  for (let i = 0; i < Math.min(expected.length, got.length); i++) {
    if (expected[i] !== got[i]) { errs.push(`chapter order differs from outline: expected ${expected.join(', ')}`); break; }
  }
  for (const c of chapters) {
    for (const m of c.html.matchAll(/href="#([^"]+)"/g)) {
      const t = m[1].split('--')[0];
      if (!planned.has(t)) errs.push(`[${c.id}] link to unknown chapter #${m[1]}`);
    }
    const svgOpen = (c.html.match(/<svg[\s>]/g) || []).length, svgClose = (c.html.match(/<\/svg>/g) || []).length;
    if (svgOpen !== svgClose) errs.push(`[${c.id}] <svg> open/close count mismatch (${svgOpen}/${svgClose})`);
    if (/<svg[^>]*\sid=|<marker|<defs/.test(c.html)) errs.push(`[${c.id}] SVGs must not define ids/markers/defs — use the shared markers url(#ah) etc.`);
    for (const w of c.html.matchAll(/data-w="([^"]+)"/g)) {
      const ok = ['graph','projectile','unitcircle','normal','binomial','wave','halflife','stats','units','timer','ucas','planner','periodic','molar','resistor','ohm','punnett','chisq','hardy','supplydemand','breakeven','npv','ratios'];
      if (!ok.includes(w[1])) errs.push(`[${c.id}] unknown widget data-w="${w[1]}"`);
    }
  }
  const warns = R.st.warnings;
  const words = chapters.map(c => `${c.id}:${c.words}`).join('  ');
  if (errs.length) {
    totalErrors += errs.length;
    console.log(`✗ ${base}: ${errs.length} error(s)`);
    for (const e of errs) console.log('   - ' + e);
  } else console.log(`✓ ${base}: ${chapters.length} chapter(s), ${R.st.mathCount} formulas, ${R.st.QUIZ.length} quiz Qs, ${R.st.GLOSSARY.length} definitions`);
  if (warns.length) { console.log(`  ${warns.length} warning(s):`); for (const w of warns.slice(0, 20)) console.log('   · ' + w); }
  console.log('  words: ' + words);
}
process.exit(totalErrors ? 1 : 0);
