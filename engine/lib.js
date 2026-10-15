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
const BLOCK_TYPES = new Set(['def', 'eg', 'try', 'quiz', 'html', 'plot', 'cols', 'col', 'steps', 'links', 'proof', 'checklist', 'progress', ...Object.keys(CALLOUTS)]);

// :::links kinds, in display order, each with a small line icon
const LINK_KINDS = {
  watch: { t: 'Watch', i: '<circle cx="8" cy="8" r="6.5"/><path d="M6.6 5.4v5.2L10.8 8z" fill="currentColor"/>' },
  practise: { t: 'Practise', i: '<path d="M10.8 2.6l2.6 2.6-7.6 7.6-3.3.7.7-3.3z"/><path d="M9.3 4.1l2.6 2.6"/>' },
  explore: { t: 'Explore', i: '<circle cx="8" cy="8" r="6.5"/><path d="M10.6 5.4L9.1 9.1 5.4 10.6 6.9 6.9z"/>' },
  read: { t: 'Read', i: '<path d="M8 4.2C6.6 3.2 4.5 2.8 2 3v9.3c2.5-.2 4.6.2 6 1.2 1.4-1 3.5-1.4 6-1.2V3c-2.5-.2-4.6.2-6 1.2zM8 4.2v9.3"/>' },
  papers: { t: 'Papers', i: '<path d="M4.5 2.5h5l2.5 2.5v8.5h-7.5z"/><path d="M9.5 2.5V5H12M6.5 8h3.5M6.5 10.5h3.5"/>' }
};
const LINK_TAGS = { paid: 'Some content paid', unofficial: 'Unofficial archive' };
const icon = (paths) => `<svg class="ico" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round">${paths}</svg>`;
const hash = (s) => { let h = 5381; for (const ch of String(s)) h = ((h * 33) ^ ch.codePointAt(0)) >>> 0; return h.toString(36); };

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

// "[M1 A1]" is written as shorthand for "[M1] [A1]"; the marks code only knows the separate form.
const splitMarks = (s) => s.replace(/\[([MABCE]\d(?:[ ,]+[MABCE]\d)+)\]/g, (m, x) => x.split(/[ ,]+/).map(k => `[${k}]`).join(' '));

// Split inline TeX after each relation at the top level (outside braces, brackets, \left…\right and environments).
// Short formulas and anything with unbalanced brackets (e.g. the interval [0, 1)) stay whole.
const RELATIONS = new Set(['le', 'leq', 'ge', 'geq', 'ne', 'neq', 'lt', 'gt', 'leqslant', 'geqslant', 'approx', 'equiv',
  'Rightarrow', 'Leftarrow', 'Leftrightarrow', 'implies', 'iff', 'Longrightarrow', 'propto', 'cong']);
const SPLIT_MIN = 24;
function splitRelations(tex) {
  if (tex.replace(/\s+/g, '').length < SPLIT_MIN) return [tex];
  const cuts = [];
  let depth = 0;
  for (let i = 0; i < tex.length; i++) {
    const c = tex[i];
    if (c === '\\') {
      const m = tex.slice(i + 1).match(/^[a-zA-Z]+|^./);
      const name = m ? m[0] : '';
      if (name === 'left' || name === 'begin') depth++;
      else if (name === 'right' || name === 'end') depth--;
      else if (depth === 0 && RELATIONS.has(name)) cuts.push(i + 1 + name.length);
      i += name.length;
    } else if ('{(['.includes(c)) depth++;
    else if ('})]'.includes(c)) depth--;
    else if (depth === 0 && '=<>'.includes(c)) cuts.push(i + 1);
    if (depth < 0) return [tex];
  }
  if (depth !== 0 || !cuts.length) return [tex];
  const parts = [];
  let from = 0;
  for (const at of cuts) { parts.push(tex.slice(from, at)); from = at; }
  parts.push(tex.slice(from));
  // never leave a piece that is only a relation or empty (e.g. "a = {}" at the end)
  return parts.filter(p => p.trim()).length === parts.length ? parts : [tex];
}

// mhchem: find each \ce{…} with its matching brace and replace it with fn(content)
function mapCe(tex, fn) {
  let out = '', i = 0;
  for (;;) {
    const at = tex.indexOf('\\ce{', i);
    if (at < 0) return out + tex.slice(i);
    let depth = 0, j = at + 3;
    for (; j < tex.length; j++) { if (tex[j] === '{') depth++; else if (tex[j] === '}' && --depth === 0) break; }
    if (j >= tex.length) return out + tex.slice(i);
    out += tex.slice(i, at) + fn(tex.slice(at + 4, j));
    i = j + 1;
  }
}
// mhchem draws isotopes (\ce{^{35}_{17}Cl}) with the numbers over the symbol in MathML, so each isotope is taken
// out of the \ce and written as {}^{35}_{17}\ce{Cl} (with its subscripts and charge), the rest stays in \ce{}.
const ISOTOPE = /(^|[\s(])\^\{?(\d+)\}?(?:_\{?(-?\d+)\}?)?([A-Z][a-z]?(?:\d+)?(?:\^\{?\d*[+-]\}?|[+-](?=\s|$))?)/g;
function fixIsotopes(tex) {
  if (!tex.includes('\\ce{') || !/\^/.test(tex)) return tex;
  return mapCe(tex, (c) => {
    if (!ISOTOPE.test(c)) { ISOTOPE.lastIndex = 0; return `\\ce{${c}}`; }
    ISOTOPE.lastIndex = 0;
    let out = '', from = 0;
    for (const m of c.matchAll(ISOTOPE)) {
      const pre = c.slice(from, m.index) + m[1];
      if (pre.trim()) out += `\\ce{${pre}}`;
      out += `{}^{${m[2]}}${m[3] != null ? `_{${m[3]}}` : ''}\\ce{${m[4]}}`;
      from = m.index + m[0].length;
    }
    const rest = c.slice(from);
    return out + (rest.trim() ? `\\ce{${rest}}` : '');
  });
}
// A long inline \ce{…} equation is cut before each arrow and after each " + " at its top level, so it can wrap on phones.
function splitCe(tex) {
  const m = tex.match(/^\\ce\{([\s\S]*)\}$/);
  if (!m || mapCe(tex, () => '') !== '' || m[1].replace(/\s+/g, '').length < SPLIT_MIN) return [tex];
  const c = m[1], cuts = [];
  let depth = 0;
  for (let i = 0; i < c.length; i++) {
    const ch = c[i];
    if ('{['.includes(ch)) depth++;
    else if ('}]'.includes(ch)) depth--;
    else if (depth === 0 && ch === ' ') {
      if (/^ (<=>>|<<=>|<=>|<-->|<->|->|<-)/.test(c.slice(i))) cuts.push(i);
      else if (c.slice(i, i + 3) === ' + ') cuts.push(i + 2);
    }
  }
  if (!cuts.length) return [tex];
  const parts = [];
  let from = 0;
  for (const at of cuts) { parts.push(c.slice(from, at)); from = at; }
  parts.push(c.slice(from));
  return parts.filter(p => p.trim()).map(p => `\\ce{${p.trim()}}`);
}

function createRenderer(opts = {}) {
  const md = new MarkdownIt({ html: true, linkify: false, typographer: true, breaks: false });
  md.disable(['replacements']);
  const st = {
    MATH: [], BLOCKS: [], GLOSSARY: [], QUIZ: [], KEYS: [], LINKS: [], CHECKS: [], errors: [], warnings: [], mathChars: new Set(), mathCount: 0,
    chapter: null, subject: null, level: '', qn: 0, marks: 0, line: 0
  };
  const err = (msg) => st.errors.push(`[${st.chapter || '?'}] ${msg}`);
  const warn = (msg) => st.warnings.push(`[${st.chapter || '?'}] ${msg}`);

  function renderMath(tex, display) {
    st.mathCount++;
    let out;
    tex = fixIsotopes(tex);
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
    // (not after a closing bracket or a factorial: "(x + 2) − 3" is a binary minus)
    s = s.replace(/(<mo[^>]*>[^<)\]}⟩!]*<\/mo>|<mrow>|<math[^>]*>|<mtd[^>]*>)<mo>([−+±∓])<\/mo>/g, '$1<mo lspace="0" rspace="0">$2</mo>');
    s = fixTables(s);
    for (const tm of s.matchAll(/>([^<>]+)</g)) for (const ch of tm[1]) st.mathChars.add(ch);
    return display ? `<span class="mb">${s}</span>` : `<span class="mi">${s}</span>`;
  }

  // A long inline chain is rendered as one piece per relation ("a =" "b =" "c"), with a break opportunity
  // between pieces: browsers never wrap inside a <math>, so this is what lets it fit a phone.
  function renderInline(tex) {
    const ce = splitCe(tex);
    if (ce.length > 1) return ce.map(p => renderMath(p, false)).join('<wbr>');
    const parts = splitRelations(tex);
    if (parts.length < 2) return renderMath(tex, false);
    return parts.map((p, i) => renderMath(i < parts.length - 1 ? p + '{}' : p, false)).join('<wbr>');
  }

  function extractMath(src) {
    src = src.replace(/\\\[([\s\S]+?)\\\]/g, (m, tex) => { st.MATH.push(renderMath(tex.trim(), true)); return `@@D${st.MATH.length - 1}@@`; });
    src = src.replace(/\\\(([\s\S]+?)\\\)/g, (m, tex) => { st.MATH.push(renderInline(tex.trim())); return `@@M${st.MATH.length - 1}@@`; });
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

  // Q: [3 marks] (#chapter.id) question…   H: hint (any number, revealed one at a time)   A: answer
  function renderTry(body) {
    const items = [];
    let cur = null, mode = null;
    for (const line of body.split('\n')) {
      const mq = line.match(/^Q:\s?(.*)$/);
      const mh = line.match(/^H:\s?(.*)$/);
      const ma = line.match(/^A:\s?(.*)$/);
      if (mq) { cur = { q: mq[1], h: [], a: null }; items.push(cur); mode = 'q'; continue; }
      if (mh && cur) {
        if (mode === 'a') err(`H: hint after A: in :::try (hints go between Q: and A:) → "${mh[1].slice(0, 50)}"`);
        else { cur.h.push(mh[1]); mode = 'h'; }
        continue;
      }
      if (ma && cur) { cur.a = ma[1]; mode = 'a'; continue; }
      if (cur) { if (mode === 'q') cur.q += '\n' + line; else if (mode === 'h') cur.h[cur.h.length - 1] += '\n' + line; else cur.a += '\n' + line; }
      else if (line.trim()) err(`text before first Q: in :::try → "${line.slice(0, 50)}"`);
    }
    if (!items.length) err('empty :::try block (needs Q:/A: lines)');
    const lis = items.map(it => {
      if (it.a === null) err(`:::try question without A: → "${it.q.slice(0, 60)}"`);
      let q = it.q.trim(), marks = 0, rev = '';
      const m1 = q.match(/^\[(\d+)(?:\s*marks?)?\]\s*/);
      if (m1) { marks = +m1[1]; q = q.slice(m1[0].length); }
      const r1 = q.match(/^\(#([\w.-]+)\)\s*/);
      if (r1) { rev = r1[1]; q = q.slice(r1[0].length); }
      if (!marks) { const m2 = q.match(/\s*\[(\d+) marks?\]\s*$/); if (m2) { marks = +m2[1]; q = q.slice(0, q.length - m2[0].length); } }
      st.marks += marks;
      const badge = marks ? `<span class="tq-m" title="${marks} mark${marks === 1 ? '' : 's'}">[${marks}]</span>` : '';
      let hints = '';
      for (let k = it.h.length - 1; k >= 0; k--) {
        hints = `<details class="th"><summary>${it.h.length > 1 ? `Hint ${k + 1} of ${it.h.length}` : 'Hint'}</summary><div class="th-b">${processBlocks(it.h[k].trim())}${hints}</div></details>`;
      }
      // the revise link's text is filled in by site.js ("Revise: <chapter title>")
      const revLink = rev ? `<p class="ta-rev"><a href="#${rev}"></a></p>` : '';
      return `<li${marks ? ` data-marks="${marks}"` : ''}${rev ? ` data-rev="${rev}"` : ''}><div class="tq">${badge}${processBlocks(q)}</div>${hints}<details class="ta"><summary>Show answer</summary><div class="ta-b">${addMarks(processBlocks((it.a || '').trim()))}${revLink}</div></details></li>`;
    }).join('\n');
    return `<ol class="try-list">${lis}</ol>`;
  }

  // :::links: "- watch: [Title](https://…) · Site · note [paid] [unofficial]"; other lines become a note underneath
  function renderLinks(body, title) {
    const groups = {}, notes = [];
    for (const raw of body.split('\n')) {
      const line = raw.trim();
      if (!line) continue;
      const m = line.match(/^-\s+(?:\*\*)?([A-Za-z]+):(?:\*\*)?\s+(.*)$/);
      if (!m) {
        if (/^-\s/.test(line)) err(`:::links line needs a kind ("- watch: [Title](https://…) · Site · note") → "${line.slice(0, 60)}"`);
        else notes.push(line);
        continue;
      }
      let kind = m[1].toLowerCase();
      if (kind === 'practice') kind = 'practise';
      if (!LINK_KINDS[kind]) { err(`:::links kind "${m[1]}" is not one of ${Object.keys(LINK_KINDS).join(', ')}`); continue; }
      const tags = [];
      const rest = m[2].replace(/\s*\[(paid|unofficial)\]/gi, (x, t) => { tags.push(t.toLowerCase()); return ''; })
        .replace(/\s*\*\(some content paid\)\*/i, () => { tags.push('paid'); return ''; })
        .replace(/\s*\*\(unofficial archive\)\*/i, () => { tags.push('unofficial'); return ''; });
      const lm = rest.match(/^\[([^\]]+)\]\(([^)\s]+)\)\s*(.*)$/);
      if (!lm) { err(`:::links line must start with [Title](https://…) after the kind → "${line.slice(0, 60)}"`); continue; }
      if (!/^https:\/\/[^\s/]+\.[^\s]+$/.test(lm[2])) err(`:::links URL must be a full https:// address → ${lm[2].slice(0, 80)}`);
      const parts = lm[3].replace(/^·\s*/, '').split(/\s+·\s+/).map(x => x.trim()).filter(Boolean);
      const site = parts[0] || '', note = parts.slice(1).join(' · ');
      const li = `<li><a class="lk-a" href="${escapeHtml(lm[2])}" target="_blank" rel="noopener noreferrer">${mdInline(lm[1])}</a>`
        + (site ? `<span class="lk-site">${mdInline(site)}</span>` : '')
        + (note ? `<span class="lk-n">${mdInline(note)}</span>` : '')
        + (tags.length ? `<span class="lk-tags">${[...new Set(tags)].map(t => `<span class="lk-tag">${LINK_TAGS[t]}</span>`).join('')}</span>` : '') + '</li>';
      (groups[kind] = groups[kind] || []).push(li);
    }
    if (!Object.keys(groups).length) err('empty :::links block');
    const kinds = Object.keys(LINK_KINDS).filter(k => groups[k]);
    for (const k of kinds) st.LINKS.push({ c: st.chapter, s: st.subject, kind: k, html: groups[k].join('') });
    const inner = kinds.map(k => `<div class="lk-g lk-${k}" data-kind="${k}"><div class="lk-gt">${icon(LINK_KINDS[k].i)}${LINK_KINDS[k].t}</div><ul>${groups[k].join('')}</ul></div>`).join('');
    return `<aside class="links"><div class="links-h"><span class="links-l">Learn more online</span>${title ? `<span class="links-t">${mdInline(title)}</span>` : ''}<span class="links-on">Needs the internet</span></div><div class="links-b">${inner}</div>${notes.length ? `<p class="links-foot">${notes.map(mdInline).join(' ')}</p>` : ''}</aside>`;
  }

  // :::checklist: "- [ ] I can …" lines; ticks are saved in the viewer's browser (app.js)
  function renderChecklist(body, title) {
    const items = [];
    for (const raw of body.split('\n')) {
      const line = raw.trim();
      if (!line) continue;
      const m = line.match(/^-\s+(?:\[[ xX]?\]\s+)?(.+)$/);
      if (!m) { err(`:::checklist lines start with "- [ ] " → "${line.slice(0, 60)}"`); continue; }
      items.push({ k: hash(st.chapter + '|' + m[1].trim()), html: mdInline(m[1].trim()) });
    }
    if (!items.length) err('empty :::checklist block');
    st.CHECKS.push({ c: st.chapter, s: st.subject, keys: items.map(i => i.k) });
    return `<div class="checklist"><div class="cl-h"><span class="cl-l">Checklist</span><span class="cl-t">${title ? mdInline(title) : 'Tick what you can do without your notes'}</span><span class="cl-n" data-clp="${items.map(i => i.k).join(',')}"></span></div><ul class="cl-list">${items.map(i => `<li><label><input type="checkbox" data-ck="${i.k}"><span>${i.html}</span></label></li>`).join('')}</ul></div>`;
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
        } else if (type === 'try' && /\bmock\b/.test(st.level)) {
          html = `<div class="try try-mock"><div class="try-h"><span class="try-l">Question ${++st.qn}</span>${title ? `<span class="try-t">${mdInline(title)}</span>` : ''}</div>${renderTry(inner)}</div>`;
        } else if (type === 'links') {
          html = renderLinks(inner, title);
        } else if (type === 'checklist') {
          html = renderChecklist(inner, title);
        } else if (type === 'progress') {
          // filled in by site.js once every chapter is rendered (it needs the course's papers and all checklists)
          html = `<div class="cl-prog" data-prog="${escapeHtml(st.subject)}|${escapeHtml(title)}"></div>`;
        } else if (type === 'proof') {
          const ex = /^examinable\b/i.test(title);
          const t = title.replace(/^examinable\b\s*/i, '');
          const badge = ex ? '' : `<span class="proof-badge">${escapeHtml(opts.proofBadge ? opts.proofBadge(st.subject) : 'Not examined')}</span>`;
          html = `<details class="proof${ex ? ' proof-ex' : ''}"><summary><span class="proof-l">Why it's true</span>${t ? `<span class="proof-t">${mdInline(t)}</span>` : ''}${badge}</summary><div class="proof-b">${addMarks(processBlocks(inner))}</div></details>`;
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
      st.level = String(meta.level || '').toLowerCase();
      st.qn = 0; st.marks = 0;
      if (!meta.title) err('missing @title');
      const body = pl.slice(bodyStart).join('\n');
      if (/^# /m.test(body)) err('use ## for section headings (the chapter title is the only h1)');
      const dollar = body.match(/\$[a-zA-Z\\{^_]/);
      if (dollar && subjectId !== 'bus' && subjectId !== 'econ') warn('found "$" followed by a letter — math must use \\( \\) not $');
      const html = finishChapterHtml(processBlocks(extractMath(splitMarks(body))), meta.chapter);
      if (meta.summary) inline(meta.summary);
      inline(meta.title || '');
      const words = stripTags(html).split(/\s+/).filter(Boolean).length;
      const ch = { id: meta.chapter, title: meta.title || meta.chapter, subject: subjectId, group: group.title, meta, html, words, marks: st.marks };
      chapters.push(ch);
      group.chapters.push(ch);
    });
    return { chapters, groups };
  }

  return { st, renderFile, inline, extractMath, subMath, mdInline, escapeHtml, stripTags };
}

module.exports = { createRenderer, escapeHtml, stripTags, splitMarks, splitRelations, splitCe, fixIsotopes, CALLOUTS, BLOCK_TYPES, LINK_KINDS };
