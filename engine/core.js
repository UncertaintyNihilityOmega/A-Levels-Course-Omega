/* core.js — shared helpers for interactive widgets. Exposes window.W */
(function () {
  'use strict';
  const W = window.W = { reg: {}, _theme: new Set() };

  /** Register a widget initialiser: W.register('name', (el, opts) => { ... }) */
  W.register = function (name, fn) { W.reg[name] = fn; };

  /** Tiny DOM builder: W.h('div', {class:'w-row', onclick: fn}, child, 'text', ...) */
  W.h = function (tag, props, ...kids) {
    const el = document.createElement(tag);
    if (props) for (const k in props) {
      const v = props[k];
      if (v == null || v === false) continue;
      if (k === 'class') el.className = v;
      else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
      else if (k === 'html') el.innerHTML = v;
      else if (k === 'text') el.textContent = v;
      else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2), v);
      else if (v === true) el.setAttribute(k, '');
      else el.setAttribute(k, v);
    }
    for (const kid of kids.flat()) {
      if (kid == null || kid === false) continue;
      el.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
    }
    return el;
  };

  /** Widget frame: returns {root, body} with the house header. */
  W.frame = function (el, title, subtitle) {
    el.innerHTML = '';
    const body = W.h('div', { class: 'w-b' });
    const root = W.h('div', { class: 'w' },
      W.h('div', { class: 'w-h' }, W.h('span', { class: 'w-t' }, title), subtitle ? W.h('span', { class: 'w-s' }, subtitle) : null),
      body);
    el.append(root);
    return { root, body };
  };

  /** localStorage wrapper that never throws */
  W.store = {
    get(k, d) { try { const v = localStorage.getItem('zta:' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem('zta:' + k, JSON.stringify(v)); } catch (e) { /* ignore */ } }
  };

  /** Read theme colours (resolved for the element, so subject colours apply). */
  W.colors = function (el) {
    const cs = getComputedStyle(el || document.documentElement);
    const g = (n) => cs.getPropertyValue(n).trim();
    return { ink: g('--ink'), ink2: g('--ink-2'), ink3: g('--ink-3'), rule: g('--rule'), rule2: g('--rule-2'), sheet: g('--sheet'), card: g('--card'),
      sc: g('--sc'), sc2: g('--sc2'), red: g('--red'), ok: g('--ok'), pen: g('--pen'), hl: g('--hl'), font: g('--f-body'), mono: g('--f-mono') };
  };
  /** Call fn whenever the theme changes (to redraw canvases). */
  W.onTheme = function (fn) { W._theme.add(fn); };
  W.themeChanged = function () { for (const fn of W._theme) { try { fn(); } catch (e) { console.warn(e); } } };
  try {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => setTimeout(W.themeChanged, 30));
  } catch (e) { /* old browsers */ }

  /** Hi-DPI canvas that redraws on resize & theme change.
   *  const c = W.canvas(parentEl, {height: 300, draw: (ctx, w, h, colors) => {...}});  c.redraw() */
  W.canvas = function (parent, opts) {
    const wrap = W.h('div', { class: 'w-canvas', style: { height: (opts.height || 300) + 'px' } });
    const cv = W.h('canvas');
    wrap.append(cv);
    parent.append(wrap);
    const ctx = cv.getContext('2d');
    const state = { cv, ctx, wrap, w: 0, h: 0 };
    let raf = 0;
    state.redraw = function () {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const r = wrap.getBoundingClientRect();
        const dpr = Math.min(window.devicePixelRatio || 1, 2.5);
        const w = Math.max(10, Math.round(r.width)), h = Math.max(10, Math.round(r.height));
        if (cv.width !== Math.round(w * dpr) || cv.height !== Math.round(h * dpr)) { cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); }
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        ctx.clearRect(0, 0, w, h);
        state.w = w; state.h = h;
        opts.draw(ctx, w, h, W.colors(parent));
      });
    };
    try { new ResizeObserver(() => state.redraw()).observe(wrap); } catch (e) { window.addEventListener('resize', state.redraw); }
    W.onTheme(state.redraw);
    state.redraw();
    return state;
  };

  /** Number formatting with a true minus sign. sf = significant figures. */
  W.fmt = function (x, sf) {
    if (x == null || !isFinite(x)) return x === Infinity ? '∞' : x === -Infinity ? '−∞' : '—';
    sf = sf || 4;
    let s;
    if (x !== 0 && (Math.abs(x) >= 1e7 || Math.abs(x) < 1e-4)) {
      const [m, e] = x.toExponential(sf - 1).split('e');
      s = `${parseFloat(m)} × 10${W.sup(String(+e))}`;
    } else {
      s = String(parseFloat(x.toPrecision(sf)));
    }
    return s.replace(/-/g, '−');
  };
  W.fix = function (x, dp) { return isFinite(x) ? x.toFixed(dp).replace(/-/g, '−') : '—'; };
  W.money = function (x, cur) { if (!isFinite(x)) return '—'; const s = Math.abs(x).toLocaleString('en-GB', { maximumFractionDigits: 2 }); return (x < 0 ? '−' : '') + (cur || '$') + s; };
  const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻', '+': '⁺' };
  W.sup = (s) => String(s).split('').map(c => SUP[c] || c).join('');

  /** Labelled range slider. Returns {el, input, get, set}. */
  W.slider = function ({ label, min, max, step, value, fmt, oninput, id }) {
    const out = W.h('output', {});
    const input = W.h('input', { type: 'range', min, max, step: step || 'any', value, id: id || null, 'aria-label': label });
    const show = () => { out.textContent = fmt ? fmt(+input.value) : W.fmt(+input.value, 4); };
    input.addEventListener('input', () => { show(); oninput && oninput(+input.value); });
    show();
    const el = W.h('div', { class: 'w-ctl' }, W.h('div', { class: 'w-lab', style: { display: 'flex', justifyContent: 'space-between', gap: '8px' } }, W.h('span', {}, label), out), input);
    return { el, input, get: () => +input.value, set: (v) => { input.value = v; show(); } };
  };
  /** Labelled number/text input. */
  W.field = function ({ label, value, type, step, oninput, placeholder, width }) {
    const input = W.h('input', { type: type || 'number', value: value ?? '', step: step || 'any', placeholder: placeholder || null, 'aria-label': label });
    if (oninput) input.addEventListener('input', () => oninput(input.value));
    const el = W.h('div', { class: 'w-ctl', style: width ? { flex: `0 1 ${width}` } : null }, W.h('label', {}, label), input);
    return { el, input, get: () => input.value };
  };
  W.stat = function (label, hi) {
    const b = W.h('b', {}, '—');
    const el = W.h('div', { class: 'w-stat' + (hi ? ' hi' : '') }, W.h('span', {}, label), b);
    return { el, set: (v) => { b.textContent = v; } };
  };

  /** Nice tick values between a and b (about n ticks). */
  W.ticks = function (a, b, n) {
    const span = b - a; if (!(span > 0)) return [a];
    const raw = span / (n || 8), mag = Math.pow(10, Math.floor(Math.log10(raw)));
    const step = [1, 2, 2.5, 5, 10].map(m => m * mag).find(s => s >= raw) || 10 * mag;
    const out = [];
    for (let v = Math.ceil(a / step) * step; v <= b + step * 1e-9; v += step) out.push(Math.abs(v) < step * 1e-9 ? 0 : +v.toPrecision(12));
    return out;
  };

  /** Draw graph-paper axes for a view {x0,x1,y0,y1}; returns mapping functions {X, Y}. */
  W.axes = function (ctx, w, h, view, c, opts) {
    opts = opts || {};
    const pad = opts.pad || { l: 38, r: 12, t: 12, b: 26 };
    const X = (x) => pad.l + (x - view.x0) / (view.x1 - view.x0) * (w - pad.l - pad.r);
    const Y = (y) => pad.t + (view.y1 - y) / (view.y1 - view.y0) * (h - pad.t - pad.b);
    const xt = W.ticks(view.x0, view.x1, opts.nx || Math.max(4, Math.round(w / 70)));
    const yt = W.ticks(view.y0, view.y1, opts.ny || Math.max(4, Math.round(h / 45)));
    ctx.save();
    ctx.lineWidth = 1; ctx.strokeStyle = c.rule2;
    ctx.beginPath();
    for (const v of xt) { ctx.moveTo(Math.round(X(v)) + .5, pad.t); ctx.lineTo(Math.round(X(v)) + .5, h - pad.b); }
    for (const v of yt) { ctx.moveTo(pad.l, Math.round(Y(v)) + .5); ctx.lineTo(w - pad.r, Math.round(Y(v)) + .5); }
    ctx.stroke();
    const ax = view.y0 <= 0 && view.y1 >= 0 ? Y(0) : h - pad.b;
    const ay = view.x0 <= 0 && view.x1 >= 0 ? X(0) : pad.l;
    ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.3;
    ctx.beginPath(); ctx.moveTo(pad.l, Math.round(ax) + .5); ctx.lineTo(w - pad.r, Math.round(ax) + .5);
    ctx.moveTo(Math.round(ay) + .5, pad.t); ctx.lineTo(Math.round(ay) + .5, h - pad.b); ctx.stroke();
    ctx.fillStyle = c.ink3; ctx.font = `11px ${c.mono || 'monospace'}`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'top';
    for (const v of xt) if (v !== 0 || opts.zeroX) ctx.fillText((opts.fx ? opts.fx(v) : W.fmt(v, 4)), X(v), Math.min(h - pad.b + 5, ax + 5));
    ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
    for (const v of yt) if (v !== 0 || opts.zeroY) ctx.fillText((opts.fy ? opts.fy(v) : W.fmt(v, 4)), Math.max(pad.l - 5, ay - 5), Y(v));
    if (opts.xlabel) { ctx.textAlign = 'right'; ctx.textBaseline = 'bottom'; ctx.font = `italic 12px ${c.font || 'sans-serif'}`; ctx.fillText(opts.xlabel, w - pad.r - 2, ax - 4); }
    if (opts.ylabel) { ctx.textAlign = 'left'; ctx.textBaseline = 'top'; ctx.font = `italic 12px ${c.font || 'sans-serif'}`; ctx.fillText(opts.ylabel, ay + 6, pad.t + 2); }
    ctx.restore();
    return { X, Y, pad, xt, yt };
  };

  /* ---------------- safe expression parser (no eval) ----------------
     W.parse('2x^2 - 3sin(x) + a') -> { f(scope) , vars:Set }
     Supports + - * / ^, unary minus, implicit multiplication, |x| not supported (use abs()).
     Functions: sin cos tan asin acos atan sinh cosh tanh sqrt cbrt abs ln log exp floor ceil round sign sec csc cosec cot min max
     Constants: pi π e. Single-letter variables (x, y, t, a, b, c, d, k, m, n, p, q, r, s, u, v, w). */
  const FUNCS = {
    sin: Math.sin, cos: Math.cos, tan: Math.tan, asin: Math.asin, acos: Math.acos, atan: Math.atan,
    arcsin: Math.asin, arccos: Math.acos, arctan: Math.atan, sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh,
    sqrt: Math.sqrt, cbrt: Math.cbrt, abs: Math.abs, ln: Math.log, log: Math.log10, exp: Math.exp, floor: Math.floor, ceil: Math.ceil,
    round: Math.round, sign: Math.sign, sec: (x) => 1 / Math.cos(x), csc: (x) => 1 / Math.sin(x), cosec: (x) => 1 / Math.sin(x), cot: (x) => 1 / Math.tan(x),
    min: Math.min, max: Math.max
  };
  const TRIG = new Set(['sin', 'cos', 'tan', 'sec', 'csc', 'cosec', 'cot']);
  const ATRIG = new Set(['asin', 'acos', 'atan', 'arcsin', 'arccos', 'arctan']);
  const CONSTS = { pi: Math.PI, 'π': Math.PI, e: Math.E };
  const NAMES = Object.keys(FUNCS).concat(Object.keys(CONSTS)).sort((a, b) => b.length - a.length);

  function tokenize(src) {
    src = String(src).replace(/[−–]/g, '-').replace(/×|·/g, '*').replace(/÷/g, '/').replace(/²/g, '^2').replace(/³/g, '^3').replace(/\*\*/g, '^').replace(/√/g, 'sqrt');
    const t = [];
    let i = 0;
    while (i < src.length) {
      const ch = src[i];
      if (/\s/.test(ch)) { i++; continue; }
      if (/[0-9.]/.test(ch)) {
        const m = src.slice(i).match(/^(\d+\.?\d*|\.\d+)(e[+-]?\d+)?/i);
        if (!m) throw new Error('Bad number near "' + src.slice(i, i + 6) + '"');
        t.push({ k: 'num', v: parseFloat(m[0]) }); i += m[0].length; continue;
      }
      if (/[a-zA-Zπ]/.test(ch)) {
        let run = src.slice(i).match(/^[a-zA-Zπ]+/)[0];
        i += run.length;
        while (run.length) {
          const name = NAMES.find(n => run.startsWith(n));
          if (name) { t.push(FUNCS[name] ? { k: 'fn', v: name } : { k: 'const', v: name }); run = run.slice(name.length); }
          else { t.push({ k: 'var', v: run[0] }); run = run.slice(1); }
        }
        continue;
      }
      if ('+-*/^(),'.includes(ch)) { t.push({ k: ch }); i++; continue; }
      throw new Error('Unexpected "' + ch + '"');
    }
    // implicit multiplication
    const out = [];
    for (let j = 0; j < t.length; j++) {
      const a = out[out.length - 1], b = t[j];
      const endsValue = a && (a.k === 'num' || a.k === 'var' || a.k === 'const' || a.k === ')');
      const startsValue = b.k === 'num' || b.k === 'var' || b.k === 'const' || b.k === 'fn' || b.k === '(';
      if (endsValue && startsValue) out.push({ k: '*' });
      out.push(b);
    }
    return out;
  }
  W.parse = function (src, opt) {
    opt = opt || {};
    const toks = tokenize(src);
    let p = 0;
    const vars = new Set();
    const peek = () => toks[p], next = () => toks[p++];
    const expect = (k) => { const tk = next(); if (!tk || tk.k !== k) throw new Error(`Expected "${k}"`); };
    function expr() { let n = term(); while (peek() && (peek().k === '+' || peek().k === '-')) { const op = next().k; const r = term(); const l = n; n = op === '+' ? (s) => l(s) + r(s) : (s) => l(s) - r(s); } return n; }
    function term() { let n = unary(); while (peek() && (peek().k === '*' || peek().k === '/')) { const op = next().k; const r = unary(); const l = n; n = op === '*' ? (s) => l(s) * r(s) : (s) => l(s) / r(s); } return n; }
    function unary() { if (peek() && peek().k === '-') { next(); const u = unary(); return (s) => -u(s); } if (peek() && peek().k === '+') { next(); return unary(); } return power(); }
    function power() { const b = atom(); if (peek() && peek().k === '^') { next(); const e = unary(); return (s) => Math.pow(b(s), e(s)); } return b; }
    function atom() {
      const tk = next();
      if (!tk) throw new Error('Unexpected end of expression');
      if (tk.k === 'num') { const v = tk.v; return () => v; }
      if (tk.k === 'const') { const v = CONSTS[tk.v]; return () => v; }
      if (tk.k === 'var') { const name = tk.v; vars.add(name); return (s) => { const v = s[name]; if (v === undefined) throw new Error('Unknown letter "' + name + '"'); return v; }; }
      if (tk.k === '(') { const n = expr(); expect(')'); return n; }
      if (tk.k === 'fn') {
        const name = tk.v, f = FUNCS[name];
        // allow sin^2(x)
        let powE = null;
        if (peek() && peek().k === '^') { next(); powE = atom(); }
        let args;
        if (peek() && peek().k === '(') { next(); args = [expr()]; while (peek() && peek().k === ',') { next(); args.push(expr()); } expect(')'); }
        else args = [power()];
        const deg = opt.degrees;
        let call;
        if (args.length === 1) {
          const a0 = args[0];
          if (deg && TRIG.has(name)) call = (s) => f(a0(s) * Math.PI / 180);
          else if (deg && ATRIG.has(name)) call = (s) => f(a0(s)) * 180 / Math.PI;
          else call = (s) => f(a0(s));
        } else call = (s) => f(...args.map(a => a(s)));
        return powE ? (s) => Math.pow(call(s), powE(s)) : call;
      }
      throw new Error('Unexpected "' + (tk.v || tk.k) + '"');
    }
    const root = expr();
    if (p < toks.length) throw new Error('Unexpected "' + (toks[p].v || toks[p].k) + '"');
    return { f: root, vars };
  };

  /** Shuffle (Fisher–Yates) */
  W.shuffle = function (arr) { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  /** Escape text for innerHTML */
  W.esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  /** Parse "a=1,-5,5,0.1; b=0,-3,3" into [{name,value,min,max,step}] */
  W.parseParams = function (s) {
    if (!s) return [];
    return s.split(';').map(x => x.trim()).filter(Boolean).map(x => {
      const [name, rest] = x.split('=');
      const [v, mn, mx, st] = (rest || '').split(',').map(Number);
      return { name: name.trim(), value: isFinite(v) ? v : 1, min: isFinite(mn) ? mn : -5, max: isFinite(mx) ? mx : 5, step: isFinite(st) ? st : 0.1 };
    });
  };

  /* ---------------- helpers for building widgets quickly (documented in kit/WIDGETS.md) ---------------- */

  /** Slider with a typed number box beside it, kept in step. Returns {el, get, set}. */
  W.sliderNum = function ({ label, min, max, step, value, oninput }) {
    const range = W.h('input', { type: 'range', min, max, step: step || 'any', value, 'aria-label': label });
    const num = W.h('input', { type: 'number', min, max, step: step || 'any', value, 'aria-label': label + ' (type a value)', class: 'w-num' });
    const fire = (v) => { oninput && oninput(v); };
    range.addEventListener('input', () => { num.value = range.value; fire(+range.value); });
    num.addEventListener('input', () => {
      const v = +num.value;
      if (num.value === '' || !isFinite(v)) return;
      range.value = Math.min(+max, Math.max(+min, v));
      fire(v);
    });
    const el = W.h('div', { class: 'w-ctl w-sn' }, W.h('label', {}, label), W.h('div', { class: 'w-sn-row' }, range, num));
    return { el, get: () => +num.value, set: (v) => { range.value = v; num.value = v; } };
  };

  /** A small two-column readout table: W.readout([['area', 'Area'], ['err', 'Error']]) → {el, set(key, text)} */
  W.readout = function (rows) {
    const cells = {};
    const tb = W.h('tbody', {}, rows.map(([k, label]) => { cells[k] = W.h('td', {}, '—'); return W.h('tr', {}, W.h('th', { scope: 'row' }, label), cells[k]); }));
    return { el: W.h('table', { class: 'w-read' }, tb), set: (k, v) => { if (cells[k]) cells[k].textContent = v; } };
  };

  /** Theme colours plus a series palette for several curves: c.series[0], c.series[1], … */
  W.palette = function (el) {
    const c = W.colors(el);
    c.series = [c.sc, c.sc2, c.red, c.ok, c.pen, c.ink2];
    return c;
  };

  /** Pointer dragging on an element (works for mouse, pen and touch).
   *  W.drag(el, { hit(x, y) → thing or null, move(thing, x, y), end(thing) }); x, y are CSS pixels inside el. */
  W.drag = function (el, h) {
    let thing = null;
    const pos = (e) => { const r = el.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
    el.style.touchAction = 'none';
    el.addEventListener('pointerdown', (e) => {
      const [x, y] = pos(e);
      thing = h.hit ? h.hit(x, y) : true;
      if (thing == null || thing === false) { thing = null; return; }
      el.setPointerCapture(e.pointerId); e.preventDefault();
      h.move && h.move(thing, x, y);
    });
    el.addEventListener('pointermove', (e) => { if (thing != null) { const [x, y] = pos(e); h.move && h.move(thing, x, y); } });
    const stop = () => { if (thing != null) { h.end && h.end(thing); thing = null; } };
    el.addEventListener('pointerup', stop);
    el.addEventListener('pointercancel', stop);
  };

  /** True when the reader has asked for reduced motion. */
  W.reducedMotion = function () { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } };

  /** Animation loop that respects reduced motion and stops while the page is hidden.
   *  const a = W.animate((dt, t) => { …; return false to stop }); a.start(); a.stop(); a.running
   *  Under reduced motion start() calls opts.still() once instead (draw the final frame). */
  W.animate = function (step, opts) {
    opts = opts || {};
    let raf = 0, last = 0, t = 0;
    const a = { running: false };
    const frame = (now) => {
      if (!a.running) return;
      const dt = Math.min(0.05, last ? (now - last) / 1000 : 0);
      last = now;
      if (document.hidden) { raf = requestAnimationFrame(frame); return; }
      t += dt;
      if (step(dt, t) === false) { a.stop(); return; }
      raf = requestAnimationFrame(frame);
    };
    a.start = () => {
      if (W.reducedMotion()) { if (opts.still) opts.still(); return; }
      if (a.running) return;
      a.running = true; last = 0; raf = requestAnimationFrame(frame);
    };
    a.stop = () => { a.running = false; cancelAnimationFrame(raf); };
    a.reset = () => { t = 0; };
    return a;
  };

  /** 3D view: rotate (yaw about the vertical axis, then pitch) and project to the canvas.
   *  const v = W.view3d({ yaw: 0.6, pitch: 0.35, scale: 40 }); v.project(x, y, z, w, h) → [sx, sy, depth]
   *  W.orbit(canvasWrap, v, redraw) lets the reader drag to rotate. Axes: x right, y into the page, z up. */
  W.view3d = function (o) {
    const v = Object.assign({ yaw: 0.6, pitch: 0.35, scale: 40 }, o);
    v.project = (x, y, z, w, h) => {
      const cy = Math.cos(v.yaw), sy = Math.sin(v.yaw), cp = Math.cos(v.pitch), sp = Math.sin(v.pitch);
      const x1 = x * cy - y * sy, y1 = x * sy + y * cy;
      const z2 = z * cp - y1 * sp, d = z * sp + y1 * cp;
      return [w / 2 + x1 * v.scale, h / 2 - z2 * v.scale, d];
    };
    return v;
  };
  W.orbit = function (el, v, redraw) {
    let x0 = 0, y0 = 0;
    W.drag(el, {
      hit: (x, y) => { x0 = x; y0 = y; return true; },
      move: (t, x, y) => { v.yaw += (x - x0) * 0.01; v.pitch = Math.max(-1.5, Math.min(1.5, v.pitch + (y - y0) * 0.01)); x0 = x; y0 = y; redraw(); }
    });
  };

  /** Seeded random numbers (the same seed gives the same sequence): const r = W.rng(42); r(), r.int(1, 6), r.normal(0, 1) */
  W.rng = function (seed) {
    let a = (seed >>> 0) || 1;
    const r = () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
    r.int = (lo, hi) => lo + Math.floor(r() * (hi - lo + 1));
    r.normal = (mu, sd) => { let u = 0; while (!u) u = r(); return (mu || 0) + (sd == null ? 1 : sd) * Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * r()); };
    return r;
  };

  /** Back / Next step controller with "Step 2 of 6" and ←/→ keys while the widget has focus.
   *  const s = W.stepper(root, { steps: 6, onstep(i) { … } }); body.append(s.el); s.go(0) */
  W.stepper = function (root, { steps, onstep, labels }) {
    let i = 0;
    const back = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button' }, 'Back');
    const next = W.h('button', { class: 'btn btn-sm', type: 'button' }, 'Next');
    const lab = W.h('span', { class: 'w-step', 'aria-live': 'polite' });
    const s = { el: W.h('div', { class: 'w-row w-stepper' }, back, lab, next), get i() { return i; } };
    s.go = (k) => {
      i = Math.max(0, Math.min(steps - 1, k));
      back.disabled = i === 0; next.disabled = i === steps - 1;
      lab.textContent = labels && labels[i] ? labels[i] : `Step ${i + 1} of ${steps}`;
      onstep && onstep(i);
    };
    back.addEventListener('click', () => s.go(i - 1));
    next.addEventListener('click', () => s.go(i + 1));
    root.setAttribute('tabindex', root.getAttribute('tabindex') || '0');
    root.addEventListener('keydown', (e) => {
      if (/input|select|textarea/i.test(e.target.tagName)) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); s.go(i + 1); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); s.go(i - 1); }
    });
    return s;
  };
})();

/* Course chunks: each course lives in c/<course>.js, loaded on demand with a <script> tag (works from file://).
   A chunk registers its widgets, then calls ZTA.chunk(id, {html, quiz, gloss}). */
(function () {
  'use strict';
  const ZTA = window.ZTA = { loaded: {}, pending: {} };
  ZTA.chunk = function (id, data) {
    const main = document.getElementById('main');
    if (main) main.insertAdjacentHTML('beforeend', data.html);
    Object.assign(window.QUIZ, data.quiz);
    window.GLOSSARY.push(...data.gloss);
    ZTA.loaded[id] = true;
    const p = ZTA.pending[id];
    delete ZTA.pending[id];
    if (p) p.resolve();
    document.dispatchEvent(new CustomEvent('zta:chunk', { detail: id }));
  };
  ZTA.load = function (id) {
    if (ZTA.loaded[id]) return Promise.resolve();
    if (ZTA.pending[id]) return ZTA.pending[id].promise;
    const p = ZTA.pending[id] = {};
    p.promise = new Promise((resolve, reject) => { p.resolve = resolve; p.reject = reject; });
    const s = document.createElement('script');
    s.src = 'c/' + encodeURIComponent(id) + '.js';
    s.onerror = () => { delete ZTA.pending[id]; s.remove(); p.reject(new Error('Could not load c/' + id + '.js')); };
    document.head.appendChild(s);
    return p.promise;
  };
  /** Load every chunk (search, glossary and practice need all of them). */
  ZTA.loadAll = function () { return Promise.all(((window.GUIDE || {}).chunks || []).map(ZTA.load)); };
  /** Chunks a chapter needs before it can be shown: its own and those owning widgets it uses. */
  ZTA.needs = function (id) {
    const c = ((window.GUIDE || {}).ch || {})[id];
    if (!c) return [];
    return [c.k].concat(c.n || []).filter(k => k && !ZTA.loaded[k]);
  };
})();
