// plot.js — house-style SVG function graphs for :::plot blocks (JS port of the old tools/svgplot.py).
//
//   :::plot The parabola y = x² − 2x − 3      <- block title = caption
//   --f "x**2-2*x-3" --x -3 5 --y -5 7 --pt "1,-4,vertex (1, −4)@e" --vline 1 --label "y = x² − 2x − 3"
//   :::
//
// Functions use Python syntax: x**2, sin(x), exp(x), log(x) (natural log), sqrt(x), pi, e, abs(x).
// Output: <figure class="fig"><svg>…</svg><figcaption>…</figcaption></figure> using the page's theme classes.
'use strict';

const FNS = {
  sin: Math.sin, cos: Math.cos, tan: Math.tan, asin: Math.asin, acos: Math.acos, atan: Math.atan, atan2: Math.atan2,
  sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh, exp: Math.exp, log: (x, b) => b === undefined ? Math.log(x) : Math.log(x) / Math.log(b),
  log10: Math.log10, log2: Math.log2, sqrt: Math.sqrt, abs: Math.abs, floor: Math.floor, ceil: Math.ceil,
  pow: Math.pow, radians: (d) => d * Math.PI / 180, degrees: (r) => r * 180 / Math.PI, min: Math.min, max: Math.max,
  pi: Math.PI, e: Math.E, tau: 2 * Math.PI
};
const NAMES = Object.keys(FNS);

function compile(expr, deg) {
  const src = String(expr).trim();
  if (!src) throw new Error('empty --f');
  if (/\^/.test(src)) throw new Error(`use ** for powers, not ^ (in --f "${src}")`);
  if (/\/\//.test(src)) throw new Error(`// is not allowed (in --f "${src}")`);
  if (!/^[\w\s.+\-*/(),]*$/.test(src)) throw new Error(`unexpected character in --f "${src}"`);
  for (const m of src.matchAll(/[A-Za-z_]\w*/g)) {
    if (m[0] !== 'x' && !NAMES.includes(m[0])) throw new Error(`unknown name "${m[0]}" in --f "${src}" (allowed: x, ${NAMES.join(', ')})`);
  }
  const env = { ...FNS };
  if (deg) for (const k of ['sin', 'cos', 'tan']) { const f = Math[k]; env[k] = (t) => f(t * Math.PI / 180); }
  // eslint-disable-next-line no-new-func
  const fn = new Function('x', ...NAMES, `return (${src});`);
  const args = NAMES.map(n => env[n]);
  return (x) => {
    try {
      const y = fn(x, ...args);
      return typeof y === 'number' && isFinite(y) ? y : null;
    } catch (e) { return null; }
  };
}

// Split an option line like a shell: --f "x**2 - 1" --pt '1,2,A' --x -3 5
function shellSplit(line) {
  const out = [];
  let cur = '', q = null, any = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (q) {
      if (ch === q) q = null;
      else if (ch === '\\' && q === '"' && line[i + 1] === '"') { cur += '"'; i++; }
      else cur += ch;
    } else if (ch === '"' || ch === "'") { q = ch; any = true; }
    else if (/\s/.test(ch)) { if (any || cur) out.push(cur); cur = ''; any = false; }
    else cur += ch;
  }
  if (q) throw new Error('unclosed quote in :::plot options');
  if (any || cur) out.push(cur);
  return out;
}

const SPEC = {
  f: 'list', label: 'list', pt: 'list', vline: 'nums', hline: 'nums',
  x: 2, y: 2, w: 1, h: 1, xstep: 1, ystep: 1,
  nogrid: 0, noticks: 0, deg: 0,
  shade: 'str', xlabel: 'str', ylabel: 'str', caption: 'str', legend: 'str', alt: 'str'
};

function parseOptions(line) {
  const tok = shellSplit(line);
  const o = { f: [], label: [], pt: [], vline: [], hline: [], x: [-5, 5], y: [-5, 5], w: 560, h: 320, xstep: null, ystep: null,
    nogrid: false, noticks: false, deg: false, shade: null, xlabel: 'x', ylabel: 'y', caption: '', legend: 'tr', alt: '' };
  const num = (s, k) => { const v = Number(String(s).replace('−', '-')); if (!isFinite(v)) throw new Error(`--${k} needs a number, got "${s}"`); return v; };
  for (let i = 0; i < tok.length; i++) {
    const t = tok[i];
    if (!t.startsWith('--')) throw new Error(`unexpected "${t}" (options start with --)`);
    const k = t.slice(2);
    if (!(k in SPEC)) throw new Error(`unknown option --${k} (allowed: ${Object.keys(SPEC).map(s => '--' + s).join(' ')})`);
    const kind = SPEC[k];
    const next = () => { if (i + 1 >= tok.length) throw new Error(`--${k} needs a value`); return tok[++i]; };
    if (kind === 0) o[k] = true;
    else if (kind === 'list') o[k].push(next());
    else if (kind === 'nums') o[k].push(num(next(), k));
    else if (kind === 'str') o[k] = next();
    else if (kind === 1) o[k] = num(next(), k);
    else if (kind === 2) o[k] = [num(next(), k), num(next(), k)];
  }
  if (!o.f.length && !o.pt.length) throw new Error('a :::plot needs at least one --f or --pt');
  if (o.x[0] >= o.x[1] || o.y[0] >= o.y[1]) throw new Error('--x and --y need "min max" with min < max');
  return o;
}

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const f1 = (v) => v.toFixed(1);
const f0 = (v) => v.toFixed(0);

function nice(span) {
  const raw = span / 8;
  const mag = Math.pow(10, Math.floor(Math.log10(raw)));
  for (const m of [1, 2, 2.5, 5, 10]) if (raw <= m * mag) return m * mag;
  return 10 * mag;
}
function fmt(v) {
  if (Math.abs(v) < 1e-9) return '0';
  return v.toFixed(4).replace(/0+$/, '').replace(/\.$/, '').replace('-', '−');
}

/** What a screen reader hears instead of the picture (the caption is read separately): axes and ranges,
 *  the curves by their labels, shading, dashed lines and marked points. --alt replaces it. */
function describe(a, nf, marked) {
  const d = [`Graph of ${a.ylabel} against ${a.xlabel}, ${a.xlabel} from ${fmt(a.x[0])} to ${fmt(a.x[1])}, ${a.ylabel} from ${fmt(a.y[0])} to ${fmt(a.y[1])}.`];
  if (a.label.length) d.push((a.label.length > 1 ? 'Curves: ' : 'Curve: ') + a.label.join('; ') + '.');
  else if (nf > 1) d.push(`${nf} curves.`);
  if (a.shade) { const [, sa, sb] = a.shade.split(',').map(Number); d.push(`The area under the curve is shaded from ${fmt(sa)} to ${fmt(sb)}.`); }
  const lines = [...a.vline.map(v => `${a.xlabel} = ${fmt(v)}`), ...a.hline.map(v => `${a.ylabel} = ${fmt(v)}`)];
  if (lines.length) d.push(`Dashed line${lines.length > 1 ? 's' : ''} at ${lines.join(', ')}.`);
  if (marked.length) d.push(`Marked point${marked.length > 1 ? 's' : ''}: ${marked.join('; ')}.`);
  return d.join(' ');
}

/** Render a plot from an option line. captionHtml (the rendered block title) overrides --caption. Returns HTML. */
function plot(line, caption) {
  const a = parseOptions(line);
  if (caption) { a.captionHtml = caption; a.caption = caption.replace(/<[^>]+>/g, ''); }
  const W = a.w, H = a.h;
  const ml = 34, mr = 18, mt = 14, mb = 26;
  const [x0, x1] = a.x, [y0, y1] = a.y;
  const px = (x) => ml + (x - x0) / (x1 - x0) * (W - ml - mr);
  const py = (y) => mt + (y1 - y) / (y1 - y0) * (H - mt - mb);
  const xs = a.xstep || nice(x1 - x0);
  const ys = a.ystep || nice(y1 - y0);
  const fns = a.f.map(f => compile(f, a.deg));
  const out = [];
  out.push('');   // the <svg> tag, written at the end once its description is known
  if (!a.nogrid) {
    const g = [];
    for (let k = Math.ceil(x0 / xs); k * xs <= x1 + 1e-9; k++) g.push(`M${f1(px(k * xs))} ${mt}V${H - mb}`);
    for (let k = Math.ceil(y0 / ys); k * ys <= y1 + 1e-9; k++) g.push(`M${ml} ${f1(py(k * ys))}H${W - mr}`);
    out.push(`<path class="gr" d="${g.join(' ')}"/>`);
  }
  const axY = (y0 <= 0 && 0 <= y1) ? py(0) : py(y0);
  const axX = (x0 <= 0 && 0 <= x1) ? px(0) : px(x0);
  out.push(`<path class="ax" d="M${f1(axX)} ${H - mb + 4}V${mt - 6}" marker-end="url(#ahm)"/>`);
  out.push(`<path class="ax" d="M${ml - 4} ${f1(axY)}H${W - mr + 6}" marker-end="url(#ahm)"/>`);
  out.push(`<text class="tl ti" x="${f0(W - mr + 2)}" y="${f0(axY - 7)}" text-anchor="end">${esc(a.xlabel)}</text>`);
  out.push(`<text class="tl ti" x="${f0(axX + 7)}" y="${f0(mt + 4)}">${esc(a.ylabel)}</text>`);
  // tick labels go on top of the curves (pushed after them), with a halo so a curve never crosses them
  const ticks = [];
  if (!a.noticks) {
    for (let k = Math.ceil(x0 / xs); k * xs <= x1 + 1e-9; k++) {
      const v = k * xs;
      if (Math.abs(v) > 1e-9) ticks.push(`<text class="ts tc halo" x="${f1(px(v))}" y="${f0(axY + 15)}">${fmt(v)}</text>`);
    }
    for (let k = Math.ceil(y0 / ys); k * ys <= y1 + 1e-9; k++) {
      const v = k * ys;
      if (Math.abs(v) > 1e-9) ticks.push(`<text class="ts te halo" x="${f0(axX - 5)}" y="${f1(py(v) + 4)}">${fmt(v)}</text>`);
    }
    ticks.push(`<text class="ts te halo" x="${f0(axX - 5)}" y="${f0(axY + 14)}">0</text>`);
  }
  if (a.shade) {
    const [i, sa, sb] = a.shade.split(',').map(Number);
    if (!fns[i] || !isFinite(sa) || !isFinite(sb)) throw new Error('--shade needs "index,a,b" with a valid --f index (from 0)');
    const pts = [];
    for (let j = 0; j <= 200; j++) {
      const x = sa + (sb - sa) * j / 200;
      const y = fns[i](x);
      if (y === null) continue;
      pts.push(`${f1(px(x))} ${f1(py(Math.max(Math.min(y, y1), y0)))}`);
    }
    out.push(`<path class="f1" d="M${f1(px(sa))} ${f1(axY)}L${pts.join('L')}L${f1(px(sb))} ${f1(axY)}Z" opacity="0.8"/>`);
  }
  for (const v of a.vline) out.push(`<path class="ln-m dash" d="M${f1(px(v))} ${mt}V${H - mb}"/>`);
  for (const v of a.hline) out.push(`<path class="ln-m dash" d="M${ml} ${f1(py(v))}H${W - mr}"/>`);
  // series colours: course colour, its second colour, ink, red (in dark mode the second colour and red are both pink)
  const cls = ['c1', 'c2', 'c4', 'c3'];
  const textCls = ['ta', 'ta2', '', 'tr'];
  fns.forEach((fn, idx) => {
    const segs = [];
    let cur = [], prev = null;
    const n = 320;
    for (let j = 0; j <= n; j++) {
      const x = x0 + (x1 - x0) * j / n;
      const y = fn(x);
      const inside = y !== null && y0 <= y && y <= y1;
      if (prev && y !== null && prev[1] !== null) {
        const [pxv, pyv] = prev;
        if (Math.abs(y - pyv) > (y1 - y0) * 1.2) { // asymptote
          if (cur.length) segs.push(cur);
          cur = []; prev = [x, y]; continue;
        }
        const pin = y0 <= pyv && pyv <= y1;
        if (pin && !inside) {
          const yb = y > y1 ? y1 : y0;
          const t = (yb - pyv) / (y - pyv);
          cur.push([px(pxv + t * (x - pxv)), py(yb)]); segs.push(cur); cur = [];
        } else if (inside && !pin) {
          const yb = pyv > y1 ? y1 : y0;
          const t = (yb - pyv) / (y - pyv);
          cur = [[px(pxv + t * (x - pxv)), py(yb)]];
        }
      }
      if (inside) cur.push([px(x), py(y)]);
      else if (y === null && cur.length) { segs.push(cur); cur = []; }
      prev = [x, y];
    }
    if (cur.length) segs.push(cur);
    const d = segs.filter(s => s.length > 1).map(s => 'M' + s.map(([X, Y]) => `${f1(X)} ${f1(Y)}`).join('L')).join(' ');
    out.push(`<path class="${cls[idx % 4]}" d="${d}"/>`);
  });
  out.push(...ticks);
  a.label.forEach((lab, idx) => {
    const c = textCls[idx % 4];
    if (a.legend === 'tl') out.push(`<text class="tl halo ${c}" x="${ml + 8}" y="${mt + 16 + idx * 18}">${esc(lab)}</text>`);
    else out.push(`<text class="tl halo ${c}" x="${W - mr - 6}" y="${mt + 16 + idx * 18}" text-anchor="end">${esc(lab)}</text>`);
  });
  const DIRS = { n: [0, -11, 'middle'], s: [0, 19, 'middle'], e: [9, 4, 'start'], w: [-9, 4, 'end'],
    ne: [7, -9, 'start'], nw: [-7, -9, 'end'], se: [7, 17, 'start'], sw: [-7, 17, 'end'] };
  const marked = [];
  for (const p of a.pt) {
    const parts = p.split(',');
    const x = Number(parts[0].replace('−', '-')), y = Number((parts[1] || '').replace('−', '-'));
    if (!isFinite(x) || !isFinite(y)) throw new Error(`--pt needs "x,y,label", got "${p}"`);
    let lab = parts.length > 2 ? parts.slice(2).join(',') : '';
    const X = px(x), Y = py(y);
    out.push(`<circle class="fi" cx="${f1(X)}" cy="${f1(Y)}" r="4"/>`);
    if (lab) {
      let d = null;
      const at = lab.lastIndexOf('@');
      if (at >= 0) { d = lab.slice(at + 1); lab = lab.slice(0, at); }
      if (!DIRS[d]) d = X < W * 0.7 ? 'ne' : 'nw';
      const [dx, dy, anc] = DIRS[d];
      out.push(`<text class="tl halo" x="${f1(X + dx)}" y="${f1(Y + dy)}" text-anchor="${anc}">${esc(lab)}</text>`);
    }
    marked.push((lab ? lab + ' ' : '') + `at (${fmt(x)}, ${fmt(y)})`);
  }
  out[0] = `<figure class="fig"><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(a.alt || describe(a, fns.length, marked))}">`;
  out.push('</svg>');
  if (a.caption) out.push(`<figcaption>${a.captionHtml || esc(a.caption)}</figcaption>`);
  out.push('</figure>');
  return out.join('');
}

module.exports = { plot, parseOptions, shellSplit, compile };
