// lint.js — chapter structure checklist (STYLE.md) and figure rules. Returns { errors, notes }.
// Errors break the page; notes are checklist items a reviewer will look at (fix them unless there is a reason).
'use strict';
const { splitMarks } = require('./lib');

const TOPIC = new Set(['pre', 'as', 'a2', 'ext']);
const ESSAY = new Set(['bus', 'econ', 'other', 'psych']);

function blocks(text, type) {
  // bodies of top-level-or-nested ":::type" blocks
  const out = [];
  const lines = text.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (!new RegExp(`^:::${type}(\\s|$)`).test(lines[i])) continue;
    let depth = 1; const body = [];
    for (i++; i < lines.length; i++) {
      if (/^:::\w+/.test(lines[i])) depth++;
      else if (/^:::\s*$/.test(lines[i]) && --depth === 0) break;
      body.push(lines[i]);
    }
    out.push(body.join('\n'));
  }
  return out;
}

/** the file without any ":::type" blocks (nested blocks inside them go too) */
function without(text, type) {
  const lines = text.split('\n'), out = [];
  for (let i = 0; i < lines.length; i++) {
    if (!new RegExp(`^:::${type}(\\s|$)`).test(lines[i])) { out.push(lines[i]); continue; }
    let depth = 1;
    for (i++; i < lines.length; i++) {
      if (/^:::\w+/.test(lines[i])) depth++;
      else if (/^:::\s*$/.test(lines[i]) && --depth === 0) break;
    }
  }
  return out.join('\n');
}

/** ch = rendered chapter from lib.renderFile; text = the raw file; ctx = { course, hasCheck } */
function lintChapter(ch, text, ctx = {}) {
  const errors = [], notes = [];
  const m = ch.meta || {};
  text = without(text, 'proof');   // proofs never count towards the checklist minimums
  const levels = String(m.level || '').toLowerCase().split(/[ ,]+/).filter(Boolean);
  const topic = levels.some(l => TOPIC.has(l));
  const course = ctx.course || ch.subject;

  // figures: the page restyles SVG classes for light/dark, so no hard-coded colours or private defs
  const svgOpen = (ch.html.match(/<svg[\s>]/g) || []).length, svgClose = (ch.html.match(/<\/svg>/g) || []).length;
  if (svgOpen !== svgClose) errors.push(`<svg> open/close count mismatch (${svgOpen}/${svgClose})`);
  for (const svg of ch.html.match(/<svg[\s\S]*?<\/svg>/g) || []) {
    if (/<svg[^>]*\sid=|\sid="/.test(svg)) errors.push('SVG figures must not use id attributes');
    if (/<(defs|marker|style|script|foreignObject|image)\b/.test(svg)) errors.push('SVG figures must not contain defs, marker, style, script, foreignObject or image (use the shared arrowheads url(#ah) etc.)');
    if (/\s(fill|stroke)="(#|rgb|red|blue|green|black|white)/i.test(svg) || /style="[^"]*(color|fill|stroke)\s*:/i.test(svg)) errors.push('SVG figures must use classes, never colours (fill/stroke/style)');
  }
  for (const w of ch.html.match(/<div class="widget"[^>]*>/g) || []) if (!/data-w="/.test(w)) errors.push('a widget div needs data-w="name"');

  // marks: a "[n marks]" on a try question or a worked example must equal the [M1] [A1] [B1] … shown in its answer
  const marked = splitMarks(text);
  const sumMarks = (s) => [...s.matchAll(/\[(?:M|A|B|C|E)(\d)\]/g)].reduce((a, x) => a + +x[1], 0);
  for (const b of blocks(marked, 'try')) for (const it of b.split(/\n(?=Q:)/)) {
    const q = it.match(/^Q:\s*\[(\d+)(?:\s*marks?)?\]/) || it.match(/^Q:[^\n]*?\[(\d+) marks?\]\s*$/m);
    const shown = sumMarks(it.split(/\nA:/)[1] || '');
    if (q && shown && shown !== +q[1]) errors.push(`marks: a try question says [${q[1]} marks] but its answer shows ${shown} → "${it.slice(2, 60).replace(/\s+/g, ' ').trim()}"`);
  }
  for (const b of marked.matchAll(/^:::eg ([^\n]*)\n([\s\S]*?)\n:::\s*$/gm)) {
    const q = b[1].match(/\[(\d+) marks?\]/);
    const shown = sumMarks(b[2]);
    if (q && shown !== +q[1]) errors.push(`marks: worked example "${b[1].slice(0, 50)}" says [${q[1]} marks] but shows ${shown}`);
  }
  // mhchem reads a final "-" as a negative charge, so a bond fragment like \ce{-CO-NH-} or \ce{[...]n-} shows a false charge
  // Only the last term counts, and only a bond fragment open at both ends with an inner bond (-CO-NH-) or a polymer
  // bracket (]n-): ions such as Cl-, CH3O- or -COO- are left alone.
  const falseCharge = [...text.matchAll(/\\ce\{([^{}]*)\}/g)].map(x => x[1].trim().split(/\s+/).pop())
    .filter(s => /[\])]n-$/.test(s) || (/^-/.test(s) && /-$/.test(s) && /[A-Za-z0-9)]-[A-Za-z([]/.test(s)));
  if (falseCharge.length) notes.push(`${falseCharge.length} \\ce{} bond fragment(s) ending in "-" show a false negative charge (put the end bond outside \\ce): ${falseCharge.slice(0, 3).join(', ')}`);

  if (!m.summary) notes.push('add an @summary line');
  if (!m.level) notes.push('add an @level line');
  if (topic) {
    if (!m.time) notes.push('add an @time line (realistic study time)');
    if (!m.paper && !levels.includes('pre')) notes.push('add an @paper line (where it is examined)');
    const eg = blocks(text, 'eg');
    const tries = blocks(text, 'try').join('\n').split('\n').filter(l => /^Q:/.test(l)).length;
    const quiz = blocks(text, 'quiz').join('\n').split('\n').filter(l => /^\? /.test(l)).length;
    if (!blocks(text, 'why').length) notes.push('start with a :::why box');
    if (!blocks(text, 'def').length) notes.push('no :::def cards (define the key terms)');
    if (eg.length < 3) notes.push(`${eg.length} worked example(s): aim for at least 3, graded easy → exam style`);
    else if (!ESSAY.has(course) && !eg.some(b => /\[(M|A|B)\d\]/.test(b))) notes.push('no exam-style worked example with [M1] [A1] [B1] marks');
    if (tries < 5) notes.push(`${tries} :::try question(s): aim for at least 5, easy → exam style`);
    if (quiz < 3) notes.push(`${quiz} :::quiz question(s): aim for at least 3`);
    if (!blocks(text, 'recap').length) notes.push('end with a :::recap box');
    if (!/^Next: \[/m.test(text)) notes.push('finish with a "Next: [title](#id)" line');
    if (ctx.hasCheck === false && !ESSAY.has(course)) notes.push(`no checks/${ch.id}.py (recompute every number in the chapter)`);
  } else if (levels.includes('mock')) {
    // a mock paper: one :::try per question, every Q: with its marks, the time allowed in @time
    if (!/\d/.test(m.time || '') || !/h|min/i.test(m.time || '')) notes.push('a mock needs @time with the time allowed, e.g. "1 h 50 min"');
    const qs = blocks(text, 'try').join('\n').split('\n').filter(l => /^Q:/.test(l));
    const unmarked = qs.filter(l => !/^Q:\s*\[\d+(\s*marks?)?\]/.test(l) && !/\[\d+ marks?\]\s*$/.test(l));
    if (!qs.length) notes.push('a mock has one :::try per question (Q: [n marks] … A: mark scheme)');
    if (unmarked.length) notes.push(`${unmarked.length} mock question(s) without "[n marks]" after Q:`);
    if (ctx.hasCheck === false) notes.push(`no checks/${ch.id}.py (assert the marks total and recompute every answer)`);  } else if (levels.includes('guide') && !blocks(text, 'recap').length) notes.push('guide chapters usually end with a :::recap box');
  return { errors, notes };
}

module.exports = { lintChapter, blocks, without };
