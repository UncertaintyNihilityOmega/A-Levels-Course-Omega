// Shared Markdown → HTML renderer (used by engine/build.js, engine/check.js and the course kit)
const katex = require('katex');
require('katex/contrib/mhchem');
const MarkdownIt = require('markdown-it');
const { plot } = require('./plot');

const CALLOUTS = {
  tip: 'Tip', warn: 'Common mistake', exam: 'Exam technique', analogy: 'Think of it like this', key: 'Key facts',
  note: 'Note', board: 'Board differences', why: 'Why this matters', recap: 'Summary', story: 'Background', lab: 'Practical skills',
  formula: 'Formula', career: 'Where this leads'
};
const BLOCK_TYPES = new Set(['def', 'eg', 'try', 'quiz', 'html', 'plot', 'cols', 'col', 'steps', ...Object.keys(CALLOUTS)]);

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function stripTags(s) { return String(s).replace(/<[^>]+>/g, ''); }
function slug(s) {
  return String(s).toLowerCase().replace(/<[^>]+>/g, '').replace(/@@[A-Z]\d+@@/g, '').replace(/&[a-z#0-9]+;/g, '')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 48) || 'section';
}

const BOLD = (ch) => {
  const c = ch.codePointAt(0);
  if (c >= 65 && c <= 90) return String.fromCodePoint(0x1D400 + c - 65);
  if (c >= 97 && c <= 122) return String.fromCodePoint(0x1D41A + c - 97);
  if (c >= 48 && c <= 57) return String.fromCodePoint(0x1D7CE + c - 48);
  return ch;
};
const BOLDITALIC = (ch) => {
  const c = ch.codePointAt(0);
  if (c >= 65 && c <= 90) return String.fromCodePoint(0x1D468 + c - 65);
  if (c >= 97 && c <= 122) return String.fromCodePoint(0x1D482 + c - 97);
  return ch;
};
const DS = { R: 'ℝ', N: 'ℕ', Z: 'ℤ', Q: 'ℚ', C: 'ℂ' };

function fixTables(s) {
  let guard = 0;
  const re = /<mtable([^>]*)>((?:(?!<mtable)[\s\S])*?)<\/mtable>/;
  while (re.test(s) && guard++ < 300) {
    s = s.replace(re, (m, attrs, inner) => {
      const ca = (attrs.match(/columnalign="([^"]*)"/) || [])[1];
      const aligns = ca ? ca.trim().split(/\s+/) : null;
      const alignedMode = aligns && aligns[0] === 'right' && aligns[1] === 'left';
      const casesMode = aligns && aligns.length >= 2 && aligns.every(a => a === 'left');
      let newInner = inner;
      if (aligns) {
        newInner = inner.replace(/<mtr>([\s\S]*?)<\/mtr>/g, (mr, row) => {
          let j = 0;
          const r = row.replace(/<mtd([^>]*)>/g, (mt, a2) => {
            const al = aligns[Math.min(j, aligns.length - 1)];
            let st = `text-align:${al};`;
            if (alignedMode) {
              if (al === 'right') st += `padding-left:${j > 0 ? '1.6em' : '0'};padding-right:0;`;
              else st += 'padding-left:0;padding-right:0;';
            } else if (casesMode) {
              st += j === 0 ? 'padding-left:0;padding-right:1.2em;' : 'padding-left:0;';
            }
            j++;
            return `<MTD${a2} style="${st}">`;
          });
          return `<MTR>${r}</MTR>`;
        });
      }
      return `<MTABLE${attrs}>${newInner}</MTABLE>`;
    });
  }
  return s.replace(/<(\/?)MTABLE/g, '<$1mtable').replace(/<(\/?)MTR>/g, '<$1mtr>').replace(/<MTD/g, '<mtd');
}

function createRenderer(opts = {}) {
  const md = new MarkdownIt({ html: true, linkify: false, typographer: true, breaks: false });
  md.disable(['replacements']);
  const st = {
    MATH: [], BLOCKS: [], GLOSSARY: [], QUIZ: [], KEYS: [], errors: [], warnings: [], mathChars: new Set(), mathCount: 0,
    chapter: null, subject: null, line: 0
  };
  const err = (msg) => st.errors.push(`[${st.chapter || '?'}] ${msg}`);
  const warn = (msg) => st.warnings.push(`[${st.chapter || '?'}] ${msg}`);

  function renderMath(tex, display) {
    st.mathCount++;
    let out;
    try {
      out = katex.renderToString(tex, { output: 'mathml', displayMode: display, throwOnError: true, strict: 'ignore', trust: false });
    } catch (e) {
      err(`TeX error: ${e.message.replace(/\s+/g, ' ').slice(0, 170)}  ⟵ in: ${tex.slice(0, 140)}`);
      return `<code class="texerr">${escapeHtml(tex)}</code>`;
    }
    const m = out.match(/<math[\s\S]*<\/math>/);
    if (!m) return escapeHtml(tex);
    let s = m[0];
    s = s.replace(/<annotation[^>]*>[\s\S]*?<\/annotation>/g, '').replace(/<\/?semantics>/g, '');
    s = s.replace(/ xmlns="http:\/\/www\.w3\.org\/1998\/Math\/MathML"/, '');
    s = s.replace(/<(mi|mn|mtext) mathvariant="bold">([^<]*)<\/\1>/g, (x, t, txt) => `<${t}${t === 'mi' ? ' mathvariant="normal"' : ''}>${[...txt].map(BOLD).join('')}</${t}>`);
    s = s.replace(/<(mi|mn|mtext) mathvariant="bold-italic">([^<]*)<\/\1>/g, (x, t, txt) => `<${t}${t === 'mi' ? ' mathvariant="normal"' : ''}>${[...txt].map(BOLDITALIC).join('')}</${t}>`);
    s = s.replace(/<mi mathvariant="double-struck">([A-Z])<\/mi>/g, (x, c) => `<mi mathvariant="normal">${DS[c] || c}</mi>`);
    s = s.replace(/<mo>\u2061<\/mo>(?!<mrow><mo[^>]*>[(\[|]|<mo[^>]*>[(\[|])/g, '<mo>\u2061</mo><mspace width="0.1667em"></mspace>');
    // unary minus/plus after an operator, an opening bracket or at the start: no extra spacing
    s = s.replace(/(<mo[^>]*>[^<]*<\/mo>|<mrow>|<math[^>]*>|<mtd[^>]*>)<mo>([−+±∓])<\/mo>/g, '$1<mo lspace="0" rspace="0">$2</mo>');
    s = fixTables(s);
    for (const tm of s.matchAll(/>([^<>]+)</g)) for (const ch of tm[1]) st.mathChars.add(ch);
    return display ? `<span class="mb">${s}</span>` : `<span class="mi">${s}</span>`;
  }

  function extractMath(src) {
    src = src.replace(/\\\[([\s\S]+?)\\\]/g, (m, tex) => { st.MATH.push(renderMath(tex.trim(), true)); return `@@D${st.MATH.length - 1}@@`; });
    src = src.replace(/\\\(([\s\S]+?)\\\)/g, (m, tex) => { st.MATH.push(renderMath(tex.trim(), false)); return `@@M${st.MATH.length - 1}@@`; });
    if (/\\\(|\\\)|\\\[|\\\]/.test(src)) {
      const i = src.search(/\\\(|\\\)|\\\[|\\\]/);
      err(`unmatched math delimiter near: ${src.slice(Math.max(0, i - 40), i + 40).replace(/\n/g, ' ')}`);
    }
    return src;
  }
  const subMath = (html) => html.replace(/@@([DM])(\d+)@@/g, (m, k, i) => st.MATH[+i]);
  function subBlocks(html) {
    let guard = 0;
    while (/@@B\d+@@/.test(html) && guard++ < 12) {
      html = html.replace(/<p>@@B(\d+)@@<\/p>/g, (m, i) => st.BLOCKS[+i]).replace(/@@B(\d+)@@/g, (m, i) => st.BLOCKS[+i]);
    }
    return html;
  }
  // Examiner marks: a run like "[M1] [A1]" becomes one group. A group written after display maths moves in front
  // of it, so the page's examiner margin can show the marks level with the line that earns them.
  const addMarks = (html) => html.replace(/(@@D\d+@@)?\s*((?:\[(?:M|A|B|C|E)\d\]\s*)+)/g, (m, disp, run) => {
    const group = `<span class="mks">${[...run.matchAll(/\[(M|A|B|C|E)(\d)\]/g)].map(x => `<span class="mk mk-${x[1]}">${x[1]}${x[2]}</span>`).join('')}</span>`;
    return disp ? group + disp : ' ' + group + (/\s$/.test(run) ? ' ' : '');
  });
  const mdInline = (s) => md.renderInline(s);

  function renderTry(body) {
    const items = [];
    let cur = null, mode = null;
    for (const line of body.split('\n')) {
      const mq = line.match(/^Q:\s?(.*)$/);
      const ma = line.match(/^A:\s?(.*)$/);
      if (mq) { cur = { q: mq[1], a: null }; items.push(cur); mode = 'q'; continue; }
      if (ma && cur) { cur.a = ma[1]; mode = 'a'; continue; }
      if (cur) { if (mode === 'q') cur.q += '\n' + line; else cur.a += '\n' + line; }
      else if (line.trim()) err(`text before first Q: in :::try → "${line.slice(0, 50)}"`);
    }
    if (!items.length) err('empty :::try block (needs Q:/A: lines)');
    const lis = items.map(it => {
      if (it.a === null) err(`:::try question without A: → "${it.q.slice(0, 60)}"`);
      return `<li><div class="tq">${processBlocks(it.q.trim())}</div><details class="ta"><summary>Show answer</summary><div class="ta-b">${addMarks(processBlocks((it.a || '').trim()))}</div></details></li>`;
    }).join('\n');
    return `<ol class="try-list">${lis}</ol>`;
  }

  function renderQuiz(body) {
    const qs = [];
    let cur = null;
    for (const raw of body.split('\n')) {
      const line = raw.trimEnd();
      if (!line.trim()) continue;
      if (line.startsWith('? ')) { cur = { q: line.slice(2), o: [], a: [], e: '' }; qs.push(cur); continue; }
      if (!cur) { err(`text before first "? " in :::quiz → "${line.slice(0, 50)}"`); continue; }
      if (line.startsWith('+ ')) { cur.a.push(cur.o.length); cur.o.push(line.slice(2)); continue; }
      if (line.startsWith('- ')) { cur.o.push(line.slice(2)); continue; }
      if (line.startsWith('> ')) { cur.e += (cur.e ? ' ' : '') + line.slice(2); continue; }
      if (cur.o.length === 0) cur.q += ' ' + line.trim();
      else err(`unrecognised quiz line → "${line.slice(0, 60)}" (use "? ", "+ ", "- ", "> ")`);
    }
    if (!qs.length) err('empty :::quiz block');
    const ids = [];
    for (const q of qs) {
      if (q.a.length !== 1) err(`quiz question needs exactly one "+ " correct option (has ${q.a.length}): ${q.q.slice(0, 60)}`);
      if (q.o.length < 3) err(`quiz question needs at least 3 options: ${q.q.slice(0, 60)}`);
      if (!q.e) warn(`quiz question has no "> " explanation: ${q.q.slice(0, 60)}`);
      st.QUIZ.push({ c: st.chapter, s: st.subject, q: subMath(mdInline(q.q)), o: q.o.map(o => subMath(mdInline(o))), a: q.a[0] ?? 0, e: subMath(mdInline(q.e || '')) });
      ids.push(st.QUIZ.length - 1);
    }
    return `<div class="quiz" data-qs="${ids.join(',')}"></div>`;
  }

  function processBlocks(src) {
    const lines = src.split('\n');
    const out = [];
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const m = line.match(/^:::(\w+)\s*(.*)$/);
      if (m) {
        const type = m[1], title = m[2].trim();
        const body = [];
        let depth = 1, closed = false;
        i++;
        for (; i < lines.length; i++) {
          const l = lines[i];
          if (/^:::\w+/.test(l)) depth++;
          else if (/^:::\s*$/.test(l)) { depth--; if (depth === 0) { closed = true; break; } }
          body.push(l);
        }
        if (!closed) err(`unclosed :::${type} block (missing a line with just ":::")`);
        const inner = body.join('\n');
        let html = '';
        if (type === 'def') {
          const d = processBlocks(inner);
          const t = mdInline(title);
          if (!title) err(':::def needs a term after it, e.g. ":::def Gradient"');
          st.GLOSSARY.push({ t: subMath(t), d: subMath(subBlocks(d)), c: st.chapter, s: st.subject });
          html = `<dl class="def"><dt>${t}</dt><dd>${d}</dd></dl>`;
        } else if (type === 'eg') {
          const total = [...inner.matchAll(/\[(?:M|A|B|C|E)(\d)\]/g)].reduce((a, m) => a + +m[1], 0);
          const marks = total ? `<span class="eg-m">${total} mark${total === 1 ? '' : 's'}</span>` : '';
          html = `<div class="eg"><div class="eg-h"><span class="eg-l">Worked example</span>${title ? `<span class="eg-t">${mdInline(title)}</span>` : ''}${marks}</div><div class="eg-b">${addMarks(processBlocks(inner))}</div></div>`;
        } else if (type === 'try') {
          html = `<div class="try"><div class="try-h"><span class="try-l">Try it yourself</span>${title ? `<span class="try-t">${mdInline(title)}</span>` : ''}</div>${renderTry(inner)}</div>`;
        } else if (type === 'quiz') {
          html = `<div class="quiz-wrap"><div class="quiz-h"><span class="quiz-l">Quick check</span>${title ? `<span class="quiz-t">${mdInline(title)}</span>` : ''}</div>${renderQuiz(inner)}</div>`;
        } else if (type === 'html') {
          html = inner;
        } else if (type === 'plot') {
          try { html = plot(inner.replace(/\s*\n\s*/g, ' ').trim(), title ? subMath(mdInline(title)) : ''); }
          catch (e) { err(`:::plot: ${e.message}`); html = ''; }
        } else if (type === 'cols') {
          html = `<div class="cols">${processBlocks(inner)}</div>`;
        } else if (type === 'col') {
          html = `<div class="col">${title ? `<div class="col-h">${mdInline(title)}</div>` : ''}${processBlocks(inner)}</div>`;
        } else if (type === 'steps') {
          html = `<div class="steps">${processBlocks(inner)}</div>`;
        } else if (CALLOUTS[type]) {
          html = `<aside class="co co-${type}"><div class="co-h"><span class="co-l">${CALLOUTS[type]}</span>${title ? `<span class="co-t">${mdInline(title)}</span>` : ''}</div><div class="co-b">${processBlocks(inner)}</div></aside>`;
          // key and formula boxes also feed the automatic formula sheets (math placeholders resolved later with subMath)
          if (type === 'key' || type === 'formula') st.KEYS.push({ c: st.chapter, s: st.subject, html });
        } else {
          err(`unknown block type :::${type} (allowed: ${[...BLOCK_TYPES].join(', ')})`);
          html = processBlocks(inner);
        }
        st.BLOCKS.push(html);
        out.push('', `@@B${st.BLOCKS.length - 1}@@`, '');
      } else {
        if (/^\s+:::\w/.test(line)) err(`indented ::: block is not allowed (blocks must start at column 0): "${line.trim().slice(0, 40)}"`);
        out.push(line);
      }
    }
    return subBlocks(md.render(out.join('\n')));
  }

  function finishChapterHtml(html, cid) {
    html = subBlocks(html);
    html = html.replace(/<p>\s*@@D(\d+)@@\s*<\/p>/g, (m, i) => st.MATH[+i]);
    html = subMath(html);
    const used = new Set();
    html = html.replace(/<h([234])>([\s\S]*?)<\/h\1>/g, (m, lvl, inner) => {
      const s = slug(stripTags(inner));
      let k = s, n = 2;
      while (used.has(k)) k = `${s}-${n++}`;
      used.add(k);
      return `<h${lvl} id="${cid}--${k}">${inner}</h${lvl}>`;
    });
    html = html.replace(/<table>/g, '<div class="tw"><table>').replace(/<\/table>/g, '</table></div>');
    html = html.replace(/<a href="(https?:[^"]+)"/g, '<a href="$1" target="_blank" rel="noopener"');
    if (/@@[BDM]\d+@@/.test(html)) err('internal placeholder left in output (a block or formula landed somewhere odd)');
    return html;
  }

  // Inline render of a short string that may contain \( \) math
  function inline(s) { return subMath(mdInline(extractMath(s || ''))); }

  // Parse a whole content file → chapters
  function renderFile(raw, subjectId, fileName) {
    st.subject = subjectId;
    raw = raw.replace(/\r\n/g, '\n');
    const chapters = [];
    let group = null;
    const groups = [];
    const parts = raw.split(/^(?=@chapter )/m);
    parts.forEach((part, pi) => {
      const pl = part.split('\n');
      const meta = {};
      let bodyStart = 0;
      for (let i = 0; i < pl.length; i++) {
        const mm = pl[i].match(/^@(\w+)\s+(.*)$/);
        if (mm) {
          if (mm[1] === 'group') {
            if (opts.groups) { group = { title: mm[2].trim(), chapters: [] }; groups.push(group); }
            else st.warnings.push(`[${fileName}] @group lines are ignored: the group comes from course.json`);
          } else meta[mm[1]] = mm[2].trim();
          bodyStart = i + 1;
        } else if (pl[i].trim() === '') { bodyStart = i + 1; if (Object.keys(meta).length) { /* blank after meta */ } }
        else break;
      }
      if (!meta.chapter) {
        if (pi === 0 && pl.slice(bodyStart).join('').trim()) st.errors.push(`[${fileName}] text before the first @chapter line is ignored`);
        return;
      }
      if (!group) { group = { title: 'Contents', chapters: [] }; groups.push(group); }
      st.chapter = meta.chapter;
      if (!meta.title) err('missing @title');
      const body = pl.slice(bodyStart).join('\n');
      if (/^# /m.test(body)) err('use ## for section headings (the chapter title is the only h1)');
      const dollar = body.match(/\$[a-zA-Z\\{^_]/);
      if (dollar && subjectId !== 'bus' && subjectId !== 'econ') warn('found "$" followed by a letter — math must use \\( \\) not $');
      const html = finishChapterHtml(processBlocks(extractMath(body)), meta.chapter);
      if (meta.summary) inline(meta.summary);
      inline(meta.title || '');
      const words = stripTags(html).split(/\s+/).filter(Boolean).length;
      const ch = { id: meta.chapter, title: meta.title || meta.chapter, subject: subjectId, group: group.title, meta, html, words };
      chapters.push(ch);
      group.chapters.push(ch);
    });
    return { chapters, groups };
  }

  return { st, renderFile, inline, extractMath, subMath, mdInline, escapeHtml, stripTags };
}

module.exports = { createRenderer, escapeHtml, stripTags, CALLOUTS, BLOCK_TYPES };
