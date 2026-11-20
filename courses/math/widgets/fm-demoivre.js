/* fm-demoivre: powers and roots of a complex number on the Argand diagram (9231 Paper 2, de Moivre and roots of unity).
   data-mode="powers"   the points z, z², …, zⁿ joined in order from 1 (a spiral when r ≠ 1); n from −6 to 12, negative powers too
   data-mode="roots"    the n roots of w = r e^{iθ} as a regular polygon on the circle of radius r^(1/n), with their sum (always 0)
   data-z="r,theta"     modulus and argument in radians (expressions such as 2*pi/3 are allowed); default "1.1,0.5" for powers, "1,0" for roots
   data-n="5"           the exponent (powers) or the number of roots (roots)
   The arithmetic is plain functions, exported for Node tests (data/test_fm_demoivre.js, which compares them with Python's cmath). */
(function () {
  'use strict';
  const PI = Math.PI, TAU = 2 * Math.PI;
  const W = typeof window !== 'undefined' ? window.W : undefined;

  /* ---- pure helpers ---- */
  function reduceArg(t) {
    // the argument in (−π, π]
    const v = t - TAU * Math.ceil((t - PI) / TAU - 1e-12);
    return Math.abs(v) < 1e-14 ? 0 : v;
  }
  function powerPoints(r, theta, n) {
    // z⁰ = 1, then z¹ … zⁿ (or z⁻¹ … zⁿ for negative n); each {k, mod, arg, re, im}
    const out = [];
    const step = n >= 0 ? 1 : -1;
    for (let k = 0; k !== n + step; k += step) {
      const mod = Math.pow(r, k), a = k * theta;
      out.push({ k, mod, arg: reduceArg(a), re: mod * Math.cos(a), im: mod * Math.sin(a) });
    }
    return out;
  }
  function rootList(r, theta, n) {
    // the n roots of z^n = r e^{iθ}: modulus r^(1/n), argument (θ + 2πk)/n reduced to (−π, π]
    const mod = Math.pow(r, 1 / n), out = [];
    for (let k = 0; k < n; k++) {
      const a = (theta + TAU * k) / n;
      out.push({ k, mod, arg: reduceArg(a), re: mod * Math.cos(a), im: mod * Math.sin(a) });
    }
    return out;
  }
  const core = { reduceArg, powerPoints, rootList };
  if (typeof module !== 'undefined' && module.exports) module.exports = core;
  if (!W) return;

  /* ---- formatting ---- */
  const SUP = { '-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' };
  const SUB = { '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉' };
  const sup = (k) => String(k).split('').map((ch) => SUP[ch] || ch).join('');
  const sub = (k) => String(k).split('').map((ch) => SUB[ch] || ch).join('');
  const num3 = (x) => {
    if (!isFinite(x)) return '—';
    if (Math.abs(x) >= 1e6 || (x !== 0 && Math.abs(x) < 1e-4)) return Number(x).toExponential(2).replace('-', '−');
    let v = parseFloat(Number(x).toPrecision(3));
    if (Object.is(v, -0)) v = 0;
    return String(v).replace('-', '−');
  };
  const fmtC = (re, im) => {
    const scale = Math.max(Math.abs(re), Math.abs(im));
    if (Math.abs(re) < 1e-9 * Math.max(1, scale)) re = 0;
    if (Math.abs(im) < 1e-9 * Math.max(1, scale)) im = 0;
    if (im === 0) return num3(re);
    const b = num3(Math.abs(im));
    return (re === 0 ? '' : num3(re) + ' ') + (im < 0 ? (re === 0 ? '−' : '− ') : (re === 0 ? '' : '+ ')) + (b === '1' ? '' : b) + 'i';
  };
  const fmtPi = (t) => {
    const v = (t / PI).toFixed(3);
    if (v === '0.000' || v === '-0.000') return '0';
    return v.replace('-', '−') + 'π';
  };
  const norm = (s) => String(s == null ? '' : s).replace(/[−–]/g, '-').replace(/π/g, 'pi').replace(/\bpi\b/g, '(' + PI + ')');
  function evalNumber(src) {
    const v = W.parse(norm(src), {}).f({});
    if (typeof v !== 'number' || !isFinite(v)) throw new Error('not a number');
    return v;
  }
  function parsePair(s, dflt) {
    if (s == null || String(s).trim() === '') return { v: dflt.slice(), err: '' };
    const parts = String(s).split(',');
    if (parts.length !== 2) return { v: dflt.slice(), err: 'data-z should look like "1.1,0.5" (modulus, argument in radians), so the default is used.' };
    try { return { v: [evalNumber(parts[0]), evalNumber(parts[1])], err: '' }; }
    catch (e) { return { v: dflt.slice(), err: 'data-z should look like "1.1,0.5" (modulus, argument in radians), so the default is used.' }; }
  }

  W.register('fm-demoivre', function (el, o) {
    const warn = [];
    let mode = String(o.mode || 'powers').trim().toLowerCase();
    if (mode !== 'powers' && mode !== 'roots') { warn.push('data-mode should be powers or roots, so powers is used.'); mode = 'powers'; }
    const isPow = mode === 'powers';
    const LIM = isPow ? { rMin: 0.2, rMax: 3, nMin: -6, nMax: 12 } : { rMin: 0.05, rMax: 100, nMin: 2, nMax: 12 };
    const dflt = isPow ? [1.1, 0.5] : [1, 0];
    const pz = parsePair(o.z, dflt);
    if (pz.err) warn.push(pz.err);
    let r = pz.v[0], th = pz.v[1];
    if (!(r >= LIM.rMin && r <= LIM.rMax)) { warn.push(`The modulus must be from ${LIM.rMin} to ${LIM.rMax}, so ${dflt[0]} is used.`); r = dflt[0]; }
    if (!(Math.abs(th) <= 100)) { warn.push('The argument must be between −100 and 100 radians, so the default is used.'); th = dflt[1]; }
    let n = isPow ? 6 : 5;
    if (o.n != null && String(o.n).trim() !== '') {
      const nn = Number(o.n);
      if (!(isFinite(nn) && Math.round(nn) === nn && nn >= LIM.nMin && nn <= LIM.nMax)) warn.push(`data-n should be a whole number from ${LIM.nMin} to ${LIM.nMax}, so ${n} is used.`);
      else n = nn;
    }
    const start = { r, th, n };

    const { body } = W.frame(el, isPow ? 'Powers of a complex number' : 'Roots of a complex number',
      isPow ? 'z, z², …, zⁿ on the Argand diagram' : 'The n roots of w = r e^(iθ) form a regular polygon');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    const setErr = (t) => { errBox.textContent = t; errBox.style.display = t ? '' : 'none'; };
    setErr(warn.join(' '));
    body.append(errBox);

    /* ---- controls ---- */
    const rField = W.field({ label: isPow ? 'Modulus r of z' : 'Modulus r of w', value: String(r), type: 'number', step: '0.05', width: '6.5em' });
    const tField = W.field({ label: isPow ? 'Argument θ of z (radians)' : 'Argument θ of w (radians)', value: String(Math.round(th * 10000) / 10000), type: 'number', step: '0.05', width: '6.5em' });
    body.append(W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } }, rField.el, tField.el));
    const nSlider = W.slider({ label: isPow ? 'Power n' : 'Number of roots n', min: LIM.nMin, max: LIM.nMax, step: 1, value: n,
      fmt: (v) => String(Math.round(+v)), oninput: (v) => { n = Math.round(+v); update(); } });
    body.append(nSlider.el);
    const resetBtn = W.h('button', { type: 'button', class: 'btn btn-sm btn-sec', 'aria-label': 'Reset r, θ and n to their starting values' }, 'Reset');
    body.append(W.h('div', { class: 'w-row' }, resetBtn));

    const cv = W.canvas(body, { height: 340, draw, label: isPow ? 'Argand diagram of the powers of z' : 'Argand diagram of the roots of w', describe });
    const R = W.readout(isPow
      ? [['z', 'zⁿ'], ['mod', '|zⁿ| = rⁿ'], ['arg', 'arg zⁿ = nθ, reduced to (−π, π]']]
      : [['mod', 'Modulus of each root, r^(1/n)'], ['sep', 'Angle between neighbours, 2π/n'], ['sum', 'Sum of the roots']]);
    body.append(R.el);
    let table = null;
    if (!isPow) {
      table = W.h('table', { 'aria-label': 'The roots, in modulus-argument form and as a + bi' });
      body.append(table);
    }
    body.append(W.h('div', { class: 'w-note' }, isPow
      ? 'Try it: set r = 1 and the points stay on the unit circle, each a turn of θ from the one before. Make r larger than 1 for an outward spiral and smaller for an inward one. Slide n below zero to see z⁻¹, z⁻², … (the angles run backwards).'
      : 'Try it: with r = 1 and θ = 0 these are the nth roots of unity. Change θ and the whole polygon turns by θ/n; change r and it grows by r^(1/n). Check that the sum of the roots is always 0.'));

    function readInputs() {
      const rr = parseFloat(rField.input.value), tt = parseFloat(tField.input.value);
      if (!(rr >= LIM.rMin && rr <= LIM.rMax)) return `Type a modulus from ${LIM.rMin} to ${LIM.rMax}.`;
      if (!(Math.abs(tt) <= 100)) return 'Type an argument between −100 and 100 radians.';
      r = rr; th = tt;
      return '';
    }
    const onType = () => { const m = readInputs(); setErr(m); if (!m) update(); else cv.redraw(); };
    rField.input.addEventListener('input', onType);
    tField.input.addEventListener('input', onType);
    resetBtn.addEventListener('click', () => {
      r = start.r; th = start.th; n = start.n;
      rField.input.value = String(r); tField.input.value = String(Math.round(th * 10000) / 10000);
      nSlider.set(n); setErr(''); update();
    });

    /* ---- model ---- */
    let model = null;
    function build() {
      if (isPow) {
        const pts = powerPoints(r, th, n);
        let ext = 1;
        pts.forEach((p) => { ext = Math.max(ext, Math.abs(p.re), Math.abs(p.im), p.mod); });
        return { pts, ext };
      }
      const pts = rootList(r, th, n);
      return { pts, ext: Math.max(1e-9, pts[0].mod) };
    }
    function update() {
      model = build();
      const last = model.pts[model.pts.length - 1];
      if (isPow) {
        R.set('z', `z${sup(n)} = ${fmtC(last.re, last.im)}`);
        R.set('mod', `${num3(Math.pow(r, n))}  (= ${num3(r)}${sup(n)})`);
        R.set('arg', `${fmtPi(last.arg)}  (n × θ = ${num3(n * th)} rad before reducing)`);
      } else {
        let sr = 0, si = 0;
        model.pts.forEach((p) => { sr += p.re; si += p.im; });
        R.set('mod', num3(model.pts[0].mod));
        R.set('sep', `${fmtPi(TAU / n)}  (${num3(TAU / n)} rad)`);
        R.set('sum', fmtC(sr, si));
        table.replaceChildren();
        table.append(W.h('tr', {}, W.h('th', { scope: 'col' }, 'Root'), W.h('th', { scope: 'col' }, 'R e^(iφ), φ in (−π, π]'), W.h('th', { scope: 'col' }, 'a + bi')));
        model.pts.forEach((p) => {
          table.append(W.h('tr', {}, W.h('td', {}, `z${sub(p.k)}`), W.h('td', {}, `${num3(p.mod)} e^(${fmtPi(p.arg)} i)`), W.h('td', {}, fmtC(p.re, p.im))));
        });
      }
      cv.redraw();
    }
    function describe() {
      if (!model) return 'No picture yet.';
      if (isPow) {
        const last = model.pts[model.pts.length - 1];
        return `Argand diagram: the points z⁰ = 1 to z${sup(n)} for z of modulus ${num3(r)} and argument ${num3(th)} radians, joined in order. The last point z${sup(n)} is ${fmtC(last.re, last.im)}, modulus ${num3(Math.pow(r, n))}, argument ${fmtPi(last.arg)}.`;
      }
      return `Argand diagram: the ${n} roots of w with modulus ${num3(r)} and argument ${num3(th)} radians, on a circle of radius ${num3(model.pts[0].mod)}, at the corners of a regular polygon.`;
    }

    /* ---- drawing ---- */
    function draw(ctx, w, h, c) {
      if (!(w > 40 && h > 40) || !model) return;
      const pad = { l: 34, r: 14, t: 16, b: 26 };
      const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
      if (!(pw > 20 && ph > 20)) return;
      const Rv = Math.max(isPow ? 1.3 : 0.3, model.ext * 1.25);
      const scale = Math.min(pw, ph) / (2 * Rv);
      const hx = pw / (2 * scale), hy = ph / (2 * scale);
      const A = W.axes(ctx, w, h, { x0: -hx, x1: hx, y0: -hy, y1: hy }, c, { pad, xlabel: 'Re', ylabel: 'Im' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
      const cx = X(0), cy = Y(0);
      // the unit circle (powers) or the circle through the roots
      const circR = isPow ? 1 : model.pts[0].mod;
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.arc(cx, cy, circR * scale, 0, TAU); ctx.stroke(); ctx.setLineDash([]);
      const P = (p) => [X(p.re), Y(p.im)];
      const halo = (txt, x, y, col, align) => {
        ctx.font = `600 12px ${c.font}`; ctx.textBaseline = 'middle'; ctx.textAlign = align;
        ctx.lineWidth = 3; ctx.strokeStyle = c.card; ctx.lineJoin = 'round'; ctx.strokeText(txt, x, y);
        ctx.fillStyle = col; ctx.fillText(txt, x, y);
      };
      if (isPow) {
        // path from 1 through the powers
        ctx.strokeStyle = c.sc; ctx.lineWidth = 1.8; ctx.beginPath();
        model.pts.forEach((p, i) => { const q = P(p); i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1]); });
        ctx.stroke();
        // ray to the last power
        const last = model.pts[model.pts.length - 1], ql = P(last);
        ctx.strokeStyle = c.sc2; ctx.lineWidth = 1.4; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(ql[0], ql[1]); ctx.stroke(); ctx.setLineDash([]);
        const placed = [];
        model.pts.forEach((p, i) => {
          const q = P(p), isLast = i === model.pts.length - 1;
          ctx.fillStyle = isLast ? c.red : c.sc; ctx.beginPath(); ctx.arc(q[0], q[1], isLast ? 4.8 : 3.4, 0, TAU); ctx.fill();
          if (p.k === 0) return;
          if (!isLast && placed.some((s) => Math.hypot(s[0] - q[0], s[1] - q[1]) < 26)) return;
          const len = Math.hypot(q[0] - cx, q[1] - cy) || 1, ux = (q[0] - cx) / len, uy = (q[1] - cy) / len;
          const txt = 'z' + (p.k === 1 ? '' : sup(p.k));
          halo(txt, q[0] + ux * 13, q[1] + uy * 11 - (Math.abs(uy) < 0.25 ? 10 : 0), isLast ? c.red : c.ink, ux > 0.3 ? 'left' : ux < -0.3 ? 'right' : 'center');
          placed.push(q);
        });
        const p0 = P(model.pts[0]);
        halo('1', p0[0] + 5, p0[1] + 12, c.ink2, 'left');
      } else {
        ctx.strokeStyle = c.sc; ctx.lineWidth = 1.8; ctx.fillStyle = c.sc; ctx.beginPath();
        model.pts.forEach((p, i) => { const q = P(p); i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1]); });
        ctx.closePath(); ctx.globalAlpha = 0.12; ctx.fill(); ctx.globalAlpha = 1; ctx.stroke();
        ctx.strokeStyle = c.rule; ctx.lineWidth = 1;
        model.pts.forEach((p) => { const q = P(p); ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(q[0], q[1]); ctx.stroke(); });
        model.pts.forEach((p, i) => {
          const q = P(p);
          ctx.fillStyle = i === 0 ? c.red : c.sc; ctx.beginPath(); ctx.arc(q[0], q[1], i === 0 ? 4.8 : 3.6, 0, TAU); ctx.fill();
          const len = Math.hypot(q[0] - cx, q[1] - cy) || 1, ux = (q[0] - cx) / len, uy = (q[1] - cy) / len;
          halo('z' + sub(p.k), q[0] + ux * 14, q[1] + uy * 11 - (Math.abs(uy) < 0.25 ? 10 : 0), i === 0 ? c.red : c.ink, ux > 0.3 ? 'left' : ux < -0.3 ? 'right' : 'center');
        });
      }
      ctx.fillStyle = c.ink; ctx.beginPath(); ctx.arc(cx, cy, 2.6, 0, TAU); ctx.fill();
      ctx.restore();
    }

    update();
  });
})();
