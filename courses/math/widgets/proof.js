/* proof: step-through proofs with a diagram. <div class="widget" data-w="proof" data-proof="chordlimit"></div>
   One object per scene in SCENES: title, lines (algebra, revealed one per step), sliders, draw(g), result.
   Scenes so far (P16): completesquare inverse perp sector apsum gpsum pascal chordlimit ftc discs compound expderiv sinlimit productrule dotcosine tree pythagoras cosinerule */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const S = {};          // the scenes
  const fx = (v, d = 3) => W.fmt(v, d);

  /* ---------- small drawing helpers ---------- */
  function text(ctx, c, s, x, y, o = {}) {
    ctx.font = `${o.size || 12}px ${o.mono ? c.mono : c.font}`;
    ctx.textAlign = o.align || 'center'; ctx.textBaseline = o.base || 'middle';
    ctx.fillStyle = o.color || c.ink; ctx.fillText(s, x, y);
  }
  function box(ctx, c, x, y, w, h, o = {}) {
    ctx.save();
    ctx.globalAlpha = o.alpha == null ? 0.28 : o.alpha; ctx.fillStyle = o.fill || c.sc; ctx.fillRect(x, y, w, h);
    ctx.globalAlpha = 1; ctx.strokeStyle = o.stroke || o.fill || c.sc; ctx.lineWidth = o.lw || 1.6;
    if (o.dash) ctx.setLineDash(o.dash);
    ctx.strokeRect(x + 0.5, y + 0.5, w, h); ctx.restore();
  }
  function seg(ctx, c, x0, y0, x1, y1, o = {}) {
    ctx.save(); ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1);
    ctx.strokeStyle = o.color || c.ink; ctx.lineWidth = o.lw || 2; if (o.dash) ctx.setLineDash(o.dash); ctx.stroke(); ctx.restore();
  }
  function dot(ctx, x, y, r, color) { ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fillStyle = color; ctx.fill(); }
  function curve(ctx, f, x0, x1, X, Y, color, lw = 2.4, N = 160) {
    ctx.beginPath(); let pen = false;
    for (let i = 0; i <= N; i++) { const x = x0 + (x1 - x0) * i / N, y = f(x); if (!isFinite(y)) { pen = false; continue; } if (pen) ctx.lineTo(X(x), Y(y)); else { ctx.moveTo(X(x), Y(y)); pen = true; } }
    ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.stroke();
  }
  const clipPlot = (ctx, pad, w, h) => { ctx.save(); ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip(); };
  const PAD = { l: 38, r: 14, t: 12, b: 26 };
  // equal-scale axes: x from x0 to x1, y fitted so one unit is the same length both ways
  function axes(g, x0, x1, y0, y1, eq) {
    if (eq) {      // same length for one unit on both axes: widen whichever range is too tight
      const pw = g.w - PAD.l - PAD.r, ph = g.h - PAD.t - PAD.b, k = Math.min(pw / (x1 - x0), ph / (y1 - y0));
      const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
      x0 = cx - pw / k / 2; x1 = cx + pw / k / 2; y0 = cy - ph / k / 2; y1 = cy + ph / k / 2;
    }
    return W.axes(g.ctx, g.w, g.h, { x0, x1, y0, y1 }, g.c, { pad: PAD, xlabel: 'x', ylabel: 'y' });
  }

  /* what each diagram shows, for screen readers (the step text and the live line are added to it) */
  const ALT = {
    completesquare: 'Areas: a square of side x with a strip of area (b/a)x beside it; the strip is halved and moved, and the corner square (b/2a)² completes a larger square.',
    inverse: 'The graph of y = f(x) and its inverse, mirror images in the line y = x, with a point P(a, b), its reflection Q(b, a) and their midpoint M on the line.',
    perp: 'Two lines through the origin O, with a point A on one and B on the other, forming triangle OAB; the angle between the lines is printed on the diagram.',
    sector: 'A sector of a circle of radius r with angle θ at the centre, its arc and its area.',
    apsum: 'Blocks for the terms of an arithmetic series, two copies fitted together into a rectangle labelled a + l and 2Sₙ.',
    gpsum: 'The terms of a geometric series and their running total, compared with the limit a/(1 − r).',
    pascal: "Pascal's triangle down to the chosen row, with the chosen entry and the two numbers above it picked out.",
    chordlimit: 'The curve y = xⁿ with a fixed point P at x = 1 and a second point Q a distance h to the right, joined by a chord.',
    ftc: 'The graph of y = f(x) with the area A(x) under it up to x, and a thin strip of width h, about f(x)·h in area, added at the end.',
    discs: 'The line y = x from 0 to 3 rotated about the x-axis, approximated by a stack of thin discs of volume πy²δx, which makes a cone.',
    compound: 'A unit-circle diagram with angles A and B, whose right-angled triangles give sin(A + B) and cos(A + B) as sums and differences of lengths such as sin B cos A and sin B sin A.',
    expderiv: 'The curve y = aˣ with a chord from x = 0 to x = h and the tangent at x = 0, whose gradient is k.',
    sinlimit: 'A sector of the unit circle with angle h, with the lengths sin h, the arc h and tan h marked.',
    productrule: 'A rectangle with sides u and v whose sides grow by δu and δv, split into the strips v δu and u δv and the small corner δuδv.',
    dotcosine: 'Triangle OAB with vectors a and b from the origin O, the angle θ between them, and the third side b − a.',
    tree: 'A probability tree with branches A and A′ and the outcomes A ∩ B and A′ ∩ B, shown inside the box of all outcomes.',
    pythagoras: 'A right-angled triangle with sides a and b and hypotenuse c, and squares built from copies of the triangle to compare a² + b² with c².',
    cosinerule: 'Triangle ABC with a perpendicular from C meeting AB at D, giving the lengths b sin A and DB, with sides a, b and c.',
  };

  /* ---------- the widget ---------- */
  W.register('proof', function (el, o) {
    const key = String(o.proof || '').trim();
    const sc = S[key];
    const { body } = W.frame(el, sc ? sc.title : 'Proof', 'step through it with Back and Next, or the ← → keys');
    if (!sc) { body.append(W.h('div', { class: 'w-err' }, `There is no proof scene called "${key}".`)); return; }
    const v = {};
    const ctl = W.h('div', { class: 'w-row' });
    const sliders = [];
    for (const d of sc.sliders || []) {
      v[d.key] = d.value;
      const s = W.sliderNum({ label: d.label, min: d.min, max: d.max, step: d.step, value: d.value, oninput: (val) => { v[d.key] = val; cv.redraw(); readout(); } });
      sliders.push([d.key, s]); ctl.append(s.el);
    }
    let step = 0;
    const describe = () => {
      const [t, why] = sc.lines[step];
      return `${ALT[key] || sc.title} Step ${step + 1} of ${sc.lines.length}: ${t}${why ? '. ' + why : ''} ${sc.live ? sc.live(v, step) : ''}`;
    };
    const cv = W.canvas(body, { height: sc.height || 260, label: `Diagram: ${sc.title}`, describe, draw: (ctx, w, h, c) => { const g = { ctx, w, h, c, i: step, v }; sc.draw(g); } });
    const list = W.h('div', { style: { display: 'grid', gap: '4px', margin: '8px 0' } });
    const rows = sc.lines.map(([t, why]) => {
      const r = W.h('div', { style: { padding: '4px 10px', borderLeft: '3px solid var(--rule)', fontSize: '.97rem', lineHeight: '1.45' } },
        W.h('div', { style: { fontFamily: 'var(--f-mono)', overflowWrap: 'anywhere' } }, t), why ? W.h('div', { class: 'w-note', style: { margin: '2px 0 0' } }, why) : null);
      list.append(r); return r;
    });
    const resBox = W.h('div', { style: { border: '2px solid var(--sc)', borderRadius: '8px', padding: '8px 12px', fontWeight: 600, display: 'none', overflowWrap: 'anywhere' } }, sc.result);
    const live = W.h('div', { class: 'w-val', 'aria-live': 'polite', 'aria-atomic': 'true', style: { minHeight: '1.4em' } });
    const st = W.stepper(body, { steps: sc.lines.length, onstep: (i) => { step = i; paint(); } });
    body.append(ctl, live, st.el, list, resBox);
    function readout() { live.textContent = sc.live ? sc.live(v, step) : ''; }
    function paint() {
      rows.forEach((r, k) => {
        r.style.display = k <= step ? '' : 'none';
        const cur = k === step;
        r.style.borderLeftColor = cur ? 'var(--sc)' : 'var(--rule)';
        r.style.background = cur ? 'color-mix(in srgb, var(--sc) 10%, transparent)' : 'transparent';
        r.style.opacity = cur ? '1' : '0.82';
        if (cur) r.setAttribute('aria-current', 'step'); else r.removeAttribute('aria-current');
      });
      resBox.style.display = step === sc.lines.length - 1 ? '' : 'none';
      readout(); cv.redraw();
    }
    st.go(0);
  });

  /* ================= completesquare ================= */
  S.completesquare = {
    title: 'Where the quadratic formula comes from', height: 270,
    sliders: [{ key: 'k', label: 'b ÷ a', min: 2, max: 8, step: 2, value: 6 }],
    lines: [
      ['ax² + bx + c = 0'],
      ['x² + (b/a)x + c/a = 0', 'Divide by a. The first two terms are a square x² and a strip of width b/a and height x.'],
      ['(x + b/2a)² − b²/4a² + c/a = 0', 'Cut the strip in half, move one half under the square, and add the missing corner (b/2a)², then take it away again.'],
      ['(x + b/2a)² = (b² − 4ac) / 4a²', 'Move the constants across: b²/4a² − c/a has denominator 4a².'],
      ['x + b/2a = ± √(b² − 4ac) / 2a', 'Square root of both sides: remember ±.'],
      ['x = (−b ± √(b² − 4ac)) / 2a', 'Subtract b/2a.'],
    ],
    result: 'x = (−b ± √(b² − 4ac)) / 2a: completing the square, done once for every quadratic.',
    draw(g) {
      const { ctx, w, h, c, i } = g, k = g.v.k, xs = 6;
      const u = Math.min(30, (h - 60) / (xs + k / 2 + 0.4), (w - 40) / (xs + k + 1.5));
      const stage = i < 2 ? 0 : i === 2 ? 1 : 2;
      const total = (xs + (stage ? k / 2 : k)) * u;
      const ox = Math.max(20, (w - total) / 2), oy = 22, sx = xs * u, half = (k / 2) * u;
      box(ctx, c, ox, oy, sx, sx, { fill: c.sc });
      text(ctx, c, 'x²', ox + sx / 2, oy + sx / 2, { size: 16 });
      if (stage === 0) {
        box(ctx, c, ox + sx, oy, k * u, sx, { fill: c.sc2 });
        text(ctx, c, 'strip: (b/a)x', ox + sx + k * u / 2, oy + sx / 2, { size: 11 });
      } else {
        box(ctx, c, ox + sx, oy, half, sx, { fill: c.sc2 });
        box(ctx, c, ox, oy + sx, sx, half, { fill: c.sc2 });
        text(ctx, c, '½ strip', ox + sx + half / 2, oy + sx / 2, { size: 10 });
        text(ctx, c, '½ strip (moved)', ox + sx / 2, oy + sx + half / 2, { size: 10 });
        box(ctx, c, ox + sx, oy + sx, half, half, stage === 1 ? { fill: c.red, alpha: 0.06, dash: [4, 3] } : { fill: c.red, alpha: 0.3 });
        text(ctx, c, '(b/2a)²', ox + sx + half / 2, oy + sx + half / 2, { size: 10, color: c.red });
        if (stage === 2) {
          text(ctx, c, 'x + b/2a', ox + (sx + half) / 2, oy - 11, { size: 12, color: c.sc });
          text(ctx, c, 'a complete square: (x + b/2a)²', ox + (sx + half) / 2, oy + sx + half + 16, { size: 12 });
        } else text(ctx, c, 'one corner is missing', ox + (sx + half) / 2, oy + sx + half + 16, { size: 12, color: c.red });
      }
    },
  };

  /* ================= inverse ================= */
  S.inverse = {
    title: 'The inverse is the reflection in y = x', height: 330,
    sliders: [{ key: 'a', label: 'a', min: 0.4, max: 2.2, step: 0.1, value: 1.4 }],
    lines: [
      ['P(a, b) is on y = f(x), so b = f(a)', 'Here f(x) = x² for x ≥ 0, so b = a².'],
      ['f⁻¹(b) = a, so Q(b, a) is on y = f⁻¹(x)', 'The inverse takes the output back to the input.'],
      ['midpoint of PQ = ((a + b)/2, (a + b)/2)', 'Equal coordinates: the midpoint lies on y = x.'],
      ['gradient of PQ = (a − b)/(b − a) = −1', 'The line y = x has gradient 1 and 1 × (−1) = −1, so PQ is perpendicular to y = x.'],
      ['Q is the reflection of P in y = x'],
    ],
    result: 'Every point of y = f⁻¹(x) is the reflection of a point of y = f(x) in the line y = x.',
    live: (v) => `a = ${fx(v.a, 2)},  b = a² = ${fx(v.a * v.a, 3)}:  P(${fx(v.a, 3)}, ${fx(v.a * v.a, 3)}),  Q(${fx(v.a * v.a, 3)}, ${fx(v.a, 3)})`,
    draw(g) {
      const { ctx, c, i } = g, a = g.v.a, b = a * a;
      const A = axes(g, -0.3, 5.2, -0.3, 5.2, true), X = A.X, Y = A.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      seg(ctx, c, X(-0.3), Y(-0.3), X(5.2), Y(5.2), { color: c.ink3, dash: [6, 4], lw: 1.4 });
      curve(ctx, (x) => x * x, 0, 2.3, X, Y, c.sc);
      if (i >= 1) curve(ctx, (x) => Math.sqrt(x), 0, 5.2, X, Y, c.sc2);
      if (i >= 3) seg(ctx, c, X(a), Y(b), X(b), Y(a), { color: c.red, lw: 1.8 });
      if (i >= 2) { const m = (a + b) / 2; dot(ctx, X(m), Y(m), 4.5, c.ink); text(ctx, c, 'midpoint M', X(m) + 40, Y(m) + 12, { size: 11, align: 'left' }); }
      dot(ctx, X(a), Y(b), 5.5, c.sc); text(ctx, c, `P(a, b)`, X(a) - 8, Y(b) - 10, { align: 'right', color: c.sc });
      if (i >= 1) { dot(ctx, X(b), Y(a), 5.5, c.sc2); text(ctx, c, 'Q(b, a)', X(b) + 8, Y(a) + 12, { align: 'left', color: c.sc2 }); }
      text(ctx, c, 'y = x', X(4.6), Y(5), { size: 11, color: c.ink3 });
      ctx.restore();
    },
  };

  /* ================= perp ================= */
  S.perp = {
    title: 'Why perpendicular gradients multiply to −1', height: 300,
    sliders: [{ key: 'm1', label: 'm₁', min: 0.3, max: 3, step: 0.1, value: 2 }, { key: 'm2', label: 'm₂', min: -4, max: 4, step: 0.05, value: -0.5 }],
    lines: [
      ['Two lines through O with gradients m₁ and m₂', 'Try to make them perpendicular by moving m₂.'],
      ['A(1, m₁) and B(1, m₂)', 'Each line passes through the point with x = 1.'],
      ['OA² = 1 + m₁²,  OB² = 1 + m₂²,  AB² = (m₁ − m₂)²', 'Distance formula.'],
      ['Right angle at O ⇔ OA² + OB² = AB²', 'Pythagoras and its converse.'],
      ['2 + m₁² + m₂² = m₁² − 2m₁m₂ + m₂²  ⇒  2 = −2m₁m₂', 'The squares cancel.'],
      ['m₁m₂ = −1'],
    ],
    result: 'Perpendicular lines have gradients that multiply to −1: m₂ = −1/m₁.',
    live: (v, s) => { const d = 2 + 2 * v.m1 * v.m2; return s >= 2 ? `OA² + OB² − AB² = 2 + 2m₁m₂ = ${fx(d, 3)}${Math.abs(d) < 0.02 ? '   (zero: a right angle)' : ''}` : `m₁m₂ = ${fx(v.m1 * v.m2, 3)}`; },
    draw(g) {
      const { ctx, c, i } = g, { m1, m2 } = g.v;
      const A = axes(g, -1, 2.6, -2.4, 3.2, true), X = A.X, Y = A.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      for (const [m, col] of [[m1, c.sc], [m2, c.sc2]]) seg(ctx, c, X(-12), Y(-12 * m), X(12), Y(12 * m), { color: col, lw: 2.2 });
      if (i >= 1) { seg(ctx, c, X(1), Y(m1), X(1), Y(m2), { color: c.red, lw: 2, dash: [5, 4] }); dot(ctx, X(1), Y(m1), 5, c.sc); dot(ctx, X(1), Y(m2), 5, c.sc2); text(ctx, c, 'A', X(1) + 12, Y(m1), { color: c.sc }); text(ctx, c, 'B', X(1) + 12, Y(m2), { color: c.sc2 }); }
      dot(ctx, X(0), Y(0), 4.5, c.ink); text(ctx, c, 'O', X(0) - 10, Y(0) + 11);
      const ang = Math.abs(Math.atan(m1) - Math.atan(m2)) * 180 / Math.PI;
      text(ctx, c, `angle between the lines: ${fx(ang, 4)}°`, g.w / 2, PAD.t + 10, { size: 12, color: Math.abs(ang - 90) < 0.5 ? c.ok : c.ink });
      if (Math.abs(m1 * m2 + 1) < 0.02) { ctx.strokeStyle = c.ok; ctx.lineWidth = 2; ctx.strokeRect(X(0) + 4, Y(0) - 18, 14, 14); }
      ctx.restore();
    },
  };

  /* ================= sector ================= */
  S.sector = {
    title: 'Arc length and sector area', height: 270,
    sliders: [{ key: 'th', label: 'θ (radians)', min: 0.3, max: 6, step: 0.1, value: 1.2 }],
    lines: [
      ['one radian: arc length = radius', 'This is the definition of a radian.'],
      ['θ radians: arc length s = rθ', 'An angle θ times as big has an arc θ times as long.'],
      ['fraction of the circle = θ / 2π', 'A whole turn is 2π radians.'],
      ['A = (θ/2π) × πr² = ½r²θ', 'That fraction of the circle area πr².'],
    ],
    result: 's = rθ and A = ½r²θ, with θ in radians.',
    live: (v, s) => (s === 0 ? 'r = 3: a 1-radian sector has an arc of length 3, the same as r.' : `r = 3, θ = ${fx(v.th, 2)}:  s = ${fx(3 * v.th, 3)},  fraction θ/2π = ${fx(v.th / (2 * Math.PI), 3)},  A = ${fx(4.5 * v.th, 4)}`),
    draw(g) {
      const { ctx, w, h, c, i } = g, th = i === 0 ? 1 : g.v.th;
      const r = Math.min(h / 2 - 16, w / 2 - 20), cx = w / 2, cy = h / 2;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.strokeStyle = c.rule; ctx.lineWidth = 1.4; ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, r, 0, -th, true); ctx.closePath();
      ctx.globalAlpha = i >= 2 ? 0.3 : 0.12; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1; ctx.strokeStyle = c.sc; ctx.lineWidth = 1.8; ctx.stroke();
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, -th, true); ctx.strokeStyle = c.red; ctx.lineWidth = 4; ctx.stroke();
      text(ctx, c, i === 0 ? 's = r' : 's = rθ', cx + (r + 14) * Math.cos(th / 2), cy - (r + 14) * Math.sin(th / 2), { color: c.red, size: 13 });
      text(ctx, c, 'θ', cx + 26 * Math.cos(th / 2), cy - 26 * Math.sin(th / 2), { color: c.sc, size: 13 });
      text(ctx, c, 'r', cx + r / 2, cy + 12, { size: 12, color: c.ink2 });
    },
  };

  /* ================= apsum ================= */
  S.apsum = {
    title: 'The sum of an arithmetic series', height: 250,
    sliders: [{ key: 'n', label: 'n (terms)', min: 3, max: 10, step: 1, value: 6 }],
    lines: [
      ['Sₙ = a + (a + d) + … + (l − d) + l', 'Here a = 2, d = 3. Each bar is a term.'],
      ['Sₙ = l + (l − d) + … + (a + d) + a', 'Write it again in reverse order and stack it on top.'],
      ['every column has height a + l, and there are n columns', 'The first and last, the second and second last, … all add to a + l.'],
      ['2Sₙ = n(a + l)'],
      ['Sₙ = ½n(a + l) = ½n(2a + (n − 1)d)', 'Use l = a + (n − 1)d.'],
    ],
    result: 'Sₙ = ½n(a + l) = ½n(2a + (n − 1)d).',
    live: (v) => { const n = Math.round(v.n), l = 2 + 3 * (n - 1); return `n = ${n}, a = 2, l = ${l}:  Sₙ = ½ × ${n} × ${2 + l} = ${n * (2 + l) / 2}`; },
    draw(g) {
      const { ctx, w, h, c, i } = g, n = Math.round(g.v.n);
      const l = 2 + 3 * (n - 1), bw = Math.min(48, (w - 50) / n), hu = (h - 50) / (l + 2 + 0.5), ox = (w - bw * n) / 2, base = h - 20;
      for (let k = 0; k < n; k++) {
        const t = 2 + 3 * k, t2 = 2 + 3 * (n - 1 - k);
        box(ctx, c, ox + k * bw + 2, base - t * hu, bw - 4, t * hu, { fill: c.sc });
        if (i >= 1) box(ctx, c, ox + k * bw + 2, base - (t + t2) * hu, bw - 4, t2 * hu, { fill: c.sc2 });
      }
      if (i >= 2) { box(ctx, c, ox, base - (2 + l) * hu, bw * n, (2 + l) * hu, { fill: c.red, alpha: 0.04, dash: [5, 4], lw: 1.5 }); text(ctx, c, `a + l = ${2 + l}`, ox + bw * n / 2, base - (2 + l) * hu - 9, { color: c.red }); }
      if (i >= 3) text(ctx, c, `2Sₙ = ${n} × ${2 + l}`, w / 2, base - (2 + l) * hu / 2, { size: 14 });
    },
  };

  /* ================= gpsum ================= */
  S.gpsum = {
    title: 'The sum of a geometric series', height: 270,
    sliders: [{ key: 'r', label: 'r', min: -0.9, max: 0.9, step: 0.05, value: 0.6 }, { key: 'n', label: 'n (terms)', min: 1, max: 20, step: 1, value: 8 }],
    lines: [
      ['Sₙ = a + ar + ar² + … + arⁿ⁻¹', 'Here a = 1. Bars are the terms, dots are the running total.'],
      ['rSₙ = ar + ar² + … + arⁿ⁻¹ + arⁿ', 'Multiply by r: every term moves one place along.'],
      ['Sₙ − rSₙ = a − arⁿ', 'Almost everything cancels.'],
      ['Sₙ = a(1 − rⁿ) / (1 − r)', 'Divide by 1 − r (r ≠ 1).'],
      ['if −1 < r < 1 then rⁿ → 0 as n grows', 'Watch the dots settle as n increases.'],
      ['S∞ = a / (1 − r)'],
    ],
    result: 'Sₙ = a(1 − rⁿ)/(1 − r), and S∞ = a/(1 − r) when |r| < 1.',
    live: (v) => { const n = Math.round(v.n), r = v.r; const S = (1 - r ** n) / (1 - r); return `Sₙ = (1 − ${fx(r, 2)}${W.sup(n)})/(1 − ${fx(r, 2)}) = ${fx(S, 5)};  S∞ = ${fx(1 / (1 - r), 5)}`; },
    draw(g) {
      const { ctx, c, i } = g, r = g.v.r, N = 20, n = Math.round(g.v.n);
      let run = 0; const sums = []; for (let k = 0; k < N; k++) { run += r ** k; sums.push(run); }
      const top = Math.max(1.2, ...sums) * 1.12, bot = Math.min(0, ...sums, -0.1) * 1.12;
      const A = axes(g, -0.8, N + 0.2, bot, top), X = A.X, Y = A.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      const bw = Math.max(3, (X(1) - X(0)) * 0.55);
      for (let k = 0; k < N; k++) {
        const t = r ** k, on = k < n;
        ctx.globalAlpha = on ? 0.5 : 0.15; ctx.fillStyle = c.sc; ctx.fillRect(X(k) - bw / 2, Math.min(Y(0), Y(t)), bw, Math.abs(Y(t) - Y(0))); ctx.globalAlpha = 1;
        dot(ctx, X(k), Y(sums[k]), on ? 4.5 : 2.5, on ? c.red : c.ink3);
      }
      if (i >= 4) { seg(ctx, c, X(-0.8), Y(1 / (1 - r)), X(N + 0.2), Y(1 / (1 - r)), { color: c.ok, dash: [6, 4], lw: 1.8 }); text(ctx, c, 'a/(1 − r)', X(N - 2.5), Y(1 / (1 - r)) - 10, { color: c.ok, size: 12 }); }
      ctx.restore();
    },
  };

  /* ================= pascal ================= */
  S.pascal = {
    title: "Pascal's rule", height: 260,
    sliders: [{ key: 'n', label: 'row n', min: 2, max: 6, step: 1, value: 4 }, { key: 'r', label: 'position r', min: 0, max: 5, step: 1, value: 1 }],
    lines: [
      ['C(n, r) + C(n, r+1) = C(n+1, r+1)', 'Two neighbours in row n add to the number between them in row n+1. Choose n and r with the sliders.'],
      ['n!/(r!(n−r)!) + n!/((r+1)!(n−r−1)!)', 'Write both with factorials.'],
      ['= [n!(r+1) + n!(n−r)] / ((r+1)!(n−r)!)', 'Common denominator (r+1)!(n−r)!.'],
      ['= n!(n+1) / ((r+1)!(n−r)!) = (n+1)! / ((r+1)!(n−r)!)', 'n!(r + 1 + n − r) = n!(n + 1) = (n + 1)!'],
      ['= C(n+1, r+1)'],
    ],
    result: 'Each number in Pascal’s triangle is the sum of the two above it.',
    live: (v) => { const n = Math.round(v.n), r = Math.min(Math.round(v.r), n - 1); const C = (a, b) => { let t = 1; for (let k = 1; k <= b; k++) t = t * (a - b + k) / k; return Math.round(t); }; return `C(${n}, ${r}) + C(${n}, ${r + 1}) = ${C(n, r)} + ${C(n, r + 1)} = ${C(n + 1, r + 1)} = C(${n + 1}, ${r + 1})`; },
    draw(g) {
      const { ctx, w, h, c } = g, n = Math.round(g.v.n), r = Math.min(Math.round(g.v.r), n - 1), rows = 8;
      const dx = Math.min(46, (w - 20) / rows), dy = Math.min(30, (h - 24) / rows);
      const C = (a, b) => { let t = 1; for (let k = 1; k <= b; k++) t = t * (a - b + k) / k; return Math.round(t); };
      for (let a = 0; a < rows; a++) for (let b = 0; b <= a; b++) {
        const x = w / 2 + (b - a / 2) * dx, y = 18 + a * dy;
        const hit = a === n && (b === r || b === r + 1), sum = a === n + 1 && b === r + 1;
        if (hit || sum) { ctx.beginPath(); ctx.arc(x, y, dx * 0.4, 0, Math.PI * 2); ctx.globalAlpha = 0.25; ctx.fillStyle = sum ? c.ok : c.sc2; ctx.fill(); ctx.globalAlpha = 1; }
        text(ctx, c, String(C(a, b)), x, y, { size: 13, color: hit ? c.sc2 : sum ? c.ok : c.ink2 });
      }
      text(ctx, c, `row ${n}`, 28, 18 + n * dy, { size: 11, color: c.ink3 });
    },
  };

  /* ================= chordlimit ================= */
  S.chordlimit = {
    title: 'The gradient of xⁿ as a limit', height: 280,
    sliders: [{ key: 'n', label: 'power n', min: 2, max: 5, step: 1, value: 3 }, { key: 'h', label: 'h', min: 0.02, max: 1.2, step: 0.02, value: 0.8 }],
    lines: [
      ['chord from P(x, xⁿ) to Q(x + h, (x + h)ⁿ)', 'Take x = 1. Move h towards 0 and watch the chord.'],
      ['gradient = ((x + h)ⁿ − xⁿ) / h', 'Rise over run.'],
      ['(x + h)ⁿ = xⁿ + nxⁿ⁻¹h + C(n,2)xⁿ⁻²h² + … + hⁿ', 'Binomial theorem.'],
      ['gradient = nxⁿ⁻¹ + C(n,2)xⁿ⁻²h + … + hⁿ⁻¹', 'xⁿ cancels and every other term has a factor h.'],
      ['as h → 0, every term with an h tends to 0'],
      ['gradient → nxⁿ⁻¹'],
    ],
    result: 'The derivative of xⁿ is nxⁿ⁻¹ (n a positive whole number).',
    live: (v) => { const n = Math.round(v.n), h = v.h; return `x = 1:  chord gradient = ((1 + ${fx(h, 2)})^${n} − 1)/${fx(h, 2)} = ${fx(((1 + h) ** n - 1) / h, 5)};  n·xⁿ⁻¹ = ${n}`; },
    draw(g) {
      const { ctx, c, i } = g, n = Math.round(g.v.n), h = g.v.h, f = (x) => x ** n;
      const A = axes(g, -0.3, 2.4, -0.5, Math.min(2.2 ** n, 30)), X = A.X, Y = A.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      curve(ctx, f, 0, 2.4, X, Y, c.sc);
      const m = (f(1 + h) - 1) / h;
      seg(ctx, c, X(-0.3), Y(1 + m * -1.3), X(2.4), Y(1 + m * 1.4), { color: c.sc2, lw: 2, dash: [7, 5] });
      if (i >= 4) seg(ctx, c, X(-0.3), Y(1 - n * 1.3), X(2.4), Y(1 + n * 1.4), { color: c.red, lw: 2 });
      dot(ctx, X(1), Y(1), 5.5, c.red); dot(ctx, X(1 + h), Y(f(1 + h)), 5, c.sc2);
      text(ctx, c, 'P', X(1) - 10, Y(1) + 12, { color: c.red }); text(ctx, c, 'Q', X(1 + h) + 11, Y(f(1 + h)) + 4, { color: c.sc2 });
      ctx.restore();
    },
  };

  /* ================= ftc ================= */
  S.ftc = {
    title: 'Why integration gives area', height: 280,
    sliders: [{ key: 'x', label: 'x', min: 0.5, max: 3.2, step: 0.1, value: 2 }, { key: 'h', label: 'h', min: 0.05, max: 1, step: 0.05, value: 0.6 }],
    lines: [
      ['A(x) = area under y = f(x) from the start up to x', 'Here f(x) = x²/4 + 1, starting at x = 0.'],
      ['A(x + h) − A(x) ≈ f(x) × h', 'A thin strip of width h and height about f(x).'],
      ['(A(x + h) − A(x)) / h ≈ f(x)', 'Divide by h.'],
      ['as h → 0:  A′(x) = f(x)', 'The approximation becomes exact.'],
      ['A(x) = F(x) + c, where F′ = f', 'So the area function is an integral of f.'],
      ['A(a) = 0, so A(b) = F(b) − F(a)'],
    ],
    result: 'The area under y = f(x) from a to b is F(b) − F(a): ∫ f(x) dx = F(x) + c.',
    live: (v) => { const F = (x) => x ** 3 / 12 + x, f = (x) => x * x / 4 + 1; const dA = F(v.x + v.h) - F(v.x); return `ΔA = ${fx(dA, 4)},  f(x)·h = ${fx(f(v.x) * v.h, 4)},  ΔA/h = ${fx(dA / v.h, 4)},  f(x) = ${fx(f(v.x), 4)}`; },
    draw(g) {
      const { ctx, c, i } = g, { x, h } = g.v, f = (t) => t * t / 4 + 1;
      const A = axes(g, -0.3, 4.2, -0.4, 5), X = A.X, Y = A.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      ctx.beginPath(); ctx.moveTo(X(0), Y(0)); for (let k = 0; k <= 60; k++) { const t = x * k / 60; ctx.lineTo(X(t), Y(f(t))); } ctx.lineTo(X(x), Y(0)); ctx.closePath();
      ctx.globalAlpha = 0.2; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1;
      if (i >= 1) {
        ctx.beginPath(); ctx.moveTo(X(x), Y(0)); for (let k = 0; k <= 30; k++) { const t = x + h * k / 30; ctx.lineTo(X(t), Y(f(t))); } ctx.lineTo(X(x + h), Y(0)); ctx.closePath();
        ctx.globalAlpha = 0.4; ctx.fillStyle = c.red; ctx.fill(); ctx.globalAlpha = 1;
        box(ctx, c, X(x), Y(f(x)), X(x + h) - X(x), Y(0) - Y(f(x)), { fill: c.ink3, alpha: 0, dash: [4, 3], lw: 1.3 });
        text(ctx, c, 'strip ≈ f(x)·h', X(x + h / 2), Y(0) - 8, { size: 11, color: c.red });
      }
      curve(ctx, f, 0, 4.2, X, Y, c.sc);
      text(ctx, c, 'A(x)', X(x / 2), Y(0.45), { size: 13, color: c.sc });
      ctx.restore();
    },
  };

  /* ================= discs ================= */
  S.discs = {
    title: 'Volume of revolution as a stack of discs', height: 270,
    sliders: [{ key: 'n', label: 'discs', min: 1, max: 30, step: 1, value: 5 }],
    lines: [
      ['slice the solid into discs of thickness δx', 'Here y = x for 0 ≤ x ≤ 3, which makes a cone.'],
      ['a disc at x has radius y: volume ≈ πy² δx', 'A cylinder has volume πr²h.'],
      ['V ≈ Σ πy² δx', 'Add up all the discs.'],
      ['as δx → 0 the sum becomes an integral', 'More discs, better fit.'],
      ['V = π ∫ y² dx'],
    ],
    result: 'Rotating about the x-axis, V = π∫ y² dx. Check: the cone has V = ⅓πr²h = ⅓π(3²)(3) = 9π.',
    live: (v, s) => { const n = Math.round(v.n), d = 3 / n; let t = 0; for (let k = 0; k < n; k++) t += Math.PI * ((k + 0.5) * d) ** 2 * d; return `${n} disc${n > 1 ? 's' : ''}: total ${fx(t, 4)};  exact π∫₀³ x² dx = 9π = ${fx(9 * Math.PI, 4)}`; },
    draw(g) {
      const { ctx, c, i } = g, n = Math.round(g.v.n), d = 3 / n;
      const A = axes(g, -0.3, 3.6, -3.4, 3.4, true), X = A.X, Y = A.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      for (let k = 0; k < n; k++) {
        const r = (k + 0.5) * d, px0 = X(k * d), px1 = X((k + 1) * d), top = Y(r), bot = Y(-r), ex = Math.min(8, (px1 - px0) * 0.35);
        ctx.globalAlpha = 0.26; ctx.fillStyle = c.sc2; ctx.fillRect(px0, top, px1 - px0, bot - top);
        ctx.globalAlpha = 0.5; ctx.beginPath(); ctx.ellipse(px1, (top + bot) / 2, ex, (bot - top) / 2, 0, 0, Math.PI * 2); ctx.fill(); ctx.globalAlpha = 1;
        ctx.strokeStyle = c.sc2; ctx.lineWidth = 1.2; ctx.strokeRect(px0 + 0.5, top, px1 - px0, bot - top);
      }
      curve(ctx, (x) => x, 0, 3, X, Y, c.sc); curve(ctx, (x) => -x, 0, 3, X, Y, c.sc, 2.4);
      if (i >= 1 && n < 12) { const k = Math.min(1, n - 1); text(ctx, c, 'disc: πy²δx', X((k + 0.5) * d), Y(((k + 0.5) * d)) - 12, { size: 11, color: c.sc2 }); }
      ctx.restore();
    },
  };

  /* ================= compound ================= */
  S.compound = {
    title: 'Where sin(A + B) and cos(A + B) come from', height: 340,
    sliders: [{ key: 'A', label: 'A (degrees)', min: 15, max: 70, step: 5, value: 35 }, { key: 'B', label: 'B (degrees)', min: 15, max: 60, step: 5, value: 30 }],
    lines: [
      ['P = (cos(A + B), sin(A + B))', 'P is on the unit circle at angle A + B.'],
      ['draw the ray at angle A; drop a perpendicular from P to it, foot Q', 'Triangle OQP has a right angle at Q, hypotenuse 1 and angle B at O.'],
      ['OQ = cos B and QP = sin B', 'Adjacent and opposite sides of the right-angled triangle.'],
      ['Q = cos B × (cos A, sin A)', 'Q is on the ray at angle A, a distance cos B from O.'],
      ['Q to P: sin B × (−sin A, cos A)', 'QP is perpendicular to the ray, so it points at angle A + 90°.'],
      ['height of P: sin(A + B) = cos B sin A + sin B cos A', 'Add the heights: first the height of Q, then the rise from Q to P.'],
      ['across to P: cos(A + B) = cos B cos A − sin B sin A', 'Add the sideways steps: Q is across by cos B cos A, then QP goes back by sin B sin A.'],
    ],
    result: 'sin(A + B) = sin A cos B + cos A sin B and cos(A + B) = cos A cos B − sin A sin B.',
    live: (v) => { const A = v.A * Math.PI / 180, B = v.B * Math.PI / 180; return `A = ${v.A}°, B = ${v.B}°:  sin(A + B) = ${fx(Math.sin(A + B), 4)},  sin A cos B + cos A sin B = ${fx(Math.sin(A) * Math.cos(B) + Math.cos(A) * Math.sin(B), 4)}`; },
    draw(g) {
      const { ctx, c, i } = g, A = g.v.A * Math.PI / 180, B = g.v.B * Math.PI / 180;
      const ax = axes(g, -0.75, 1.25, -0.2, 1.25, true), X = ax.X, Y = ax.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      const P = [Math.cos(A + B), Math.sin(A + B)], Q = [Math.cos(B) * Math.cos(A), Math.cos(B) * Math.sin(A)];
      ctx.beginPath(); for (let k = 0; k <= 90; k++) { const t = (130 * Math.PI / 180) * k / 90; k ? ctx.lineTo(X(Math.cos(t)), Y(Math.sin(t))) : ctx.moveTo(X(1), Y(0)); }
      ctx.strokeStyle = c.rule; ctx.lineWidth = 1.4; ctx.stroke();
      seg(ctx, c, X(0), Y(0), X(P[0]), Y(P[1]), { color: c.ink, lw: 2 });
      if (i >= 1) {
        seg(ctx, c, X(0), Y(0), X(1.15 * Math.cos(A)), Y(1.15 * Math.sin(A)), { color: c.ink3, dash: [6, 4], lw: 1.4 });
        seg(ctx, c, X(0), Y(0), X(Q[0]), Y(Q[1]), { color: c.sc, lw: 2.6 });
        seg(ctx, c, X(Q[0]), Y(Q[1]), X(P[0]), Y(P[1]), { color: c.sc2, lw: 2.6 });
        dot(ctx, X(Q[0]), Y(Q[1]), 4.5, c.sc);
        text(ctx, c, 'Q', X(Q[0]) + 10, Y(Q[1]) + 11, { color: c.sc });
        text(ctx, c, 'A', X(0.2 * Math.cos(A / 2)), Y(0.2 * Math.sin(A / 2)), { size: 11 });
        text(ctx, c, 'B', X(0.28 * Math.cos(A + B / 2)), Y(0.28 * Math.sin(A + B / 2)), { size: 11 });
      }
      if (i >= 2) {
        text(ctx, c, 'cos B', X(Q[0] / 2) + 8, Y(Q[1] / 2) + 14, { size: 11, color: c.sc });
        if (i < 4) text(ctx, c, 'sin B', X((Q[0] + P[0]) / 2) - 24, Y((Q[1] + P[1]) / 2) - 4, { size: 11, color: c.sc2 });
      }
      if (i >= 3) {
        seg(ctx, c, X(Q[0]), Y(Q[1]), X(Q[0]), Y(0), { color: c.sc, dash: [4, 3], lw: 1.3 });
        seg(ctx, c, X(Q[0]), Y(Q[1]), X(0), Y(Q[1]), { color: c.sc, dash: [4, 3], lw: 1.3 });
      }
      const C = [Q[0] - Math.sin(B) * Math.sin(A), Q[1]];
      if (i >= 4) {
        seg(ctx, c, X(Q[0]), Y(Q[1]), X(C[0]), Y(C[1]), { color: c.red, lw: 2.2, dash: [5, 3] });
        seg(ctx, c, X(C[0]), Y(C[1]), X(P[0]), Y(P[1]), { color: c.red, lw: 2.2, dash: [5, 3] });
        text(ctx, c, 'sin B sin A', X((Q[0] + C[0]) / 2), Y(Q[1]) + 13, { size: 10, color: c.red });
        text(ctx, c, 'sin B cos A', X(P[0]) - 6, Y((Q[1] + P[1]) / 2), { size: 10, color: c.red, align: 'right' });
      }
      if (i === 5) { seg(ctx, c, X(P[0]), Y(0), X(P[0]), Y(P[1]), { color: c.ok, lw: 3.4 }); text(ctx, c, 'sin(A + B)', X(P[0]) + 8, Y(P[1] / 2), { size: 11, color: c.ok, align: 'left' }); }
      if (i >= 6) { seg(ctx, c, X(0), Y(0), X(P[0]), Y(0), { color: c.ok, lw: 3.4 }); text(ctx, c, 'cos(A + B)', X(P[0] / 2), Y(0) - 11, { size: 11, color: c.ok }); }
      dot(ctx, X(P[0]), Y(P[1]), 5.5, c.ink); text(ctx, c, 'P', X(P[0]) + 4, Y(P[1]) - 11);
      dot(ctx, X(0), Y(0), 3.5, c.ink);
      ctx.restore();
    },
  };

  /* ================= expderiv ================= */
  S.expderiv = {
    title: 'Why eˣ is its own derivative', height: 300,
    sliders: [{ key: 'a', label: 'base a', min: 1.5, max: 3.5, step: 0.01, value: 2 }, { key: 'h', label: 'h', min: 0.05, max: 1.2, step: 0.05, value: 0.6 }],
    lines: [
      ['f(x) = aˣ: chord gradient = (aˣ⁺ʰ − aˣ) / h', 'The picture shows the chord at x = 0. Make h smaller.'],
      ['= aˣ · (aʰ − 1) / h', 'Index law: aˣ⁺ʰ = aˣ · aʰ, so aˣ is a common factor.'],
      ['as h → 0, (aʰ − 1)/h tends to a number k', 'k is the gradient of y = aˣ at x = 0, the red line. It depends on a, not on x.'],
      ['d/dx aˣ = k · aˣ', 'The gradient is always k times the height of the curve.'],
      ['choose the base a so that k = 1', 'Move the slider for a until the red line has gradient 1 (a is a little over 2.7).'],
      ['that special number is e = 2.718…, and d/dx eˣ = eˣ'],
    ],
    result: 'e is the base for which the gradient at x = 0 is exactly 1. Then d/dx eˣ = eˣ.',
    live: (v) => { const a = v.a, h = v.h; return `a = ${fx(a, 3)},  h = ${fx(h, 2)}:  chord gradient (aʰ − 1)/h = ${fx((a ** h - 1) / h, 4)};  gradient at x = 0: k = ${fx(Math.log(a), 4)}`; },
    draw(g) {
      const { ctx, c, i } = g, a = g.v.a, h = g.v.h, f = (x) => a ** x, k = Math.log(a);
      const ax = axes(g, -1.8, 2.1, -0.6, 7), X = ax.X, Y = ax.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      curve(ctx, f, -1.8, 2.1, X, Y, c.sc);
      const m = (f(h) - 1) / h;
      seg(ctx, c, X(-1), Y(1 - m), X(1.6), Y(1 + 1.6 * m), { color: c.sc2, lw: 2, dash: [7, 5] });
      if (i >= 2) seg(ctx, c, X(-1), Y(1 - k), X(1.6), Y(1 + 1.6 * k), { color: c.red, lw: 2.2 });
      dot(ctx, X(0), Y(1), 5.5, c.red); dot(ctx, X(h), Y(f(h)), 5, c.sc2);
      if (i >= 4 && Math.abs(k - 1) < 0.015) text(ctx, c, 'k = 1: this is e', X(-0.9), Y(5.6), { size: 13, color: c.ok });
      ctx.restore();
    },
  };

  /* ================= sinlimit ================= */
  S.sinlimit = {
    title: 'Why the derivative of sin x is cos x', height: 330,
    sliders: [{ key: 'h', label: 'h (radians)', min: 0.05, max: 1, step: 0.05, value: 0.6 }],
    lines: [
      ['d/dx sin x = lim (sin(x + h) − sin x) / h', 'The gradient of a chord, with h → 0 and x in radians.'],
      ['= lim (sin x cos h + cos x sin h − sin x) / h', 'Compound angle formula for sin(x + h).'],
      ['= lim [ sin x · (cos h − 1)/h + cos x · (sin h)/h ]', 'Group the terms. Two limits are needed.'],
      ['sin h < h < tan h, so cos h < (sin h)/h < 1', 'The sector is between two triangles. Divide by sin h, then take reciprocals. As h → 0, cos h → 1, so (sin h)/h → 1.'],
      ['(cos h − 1)/h = −(sin h / h) × sin h / (1 + cos h) → −1 × 0 / 2 = 0', 'Use cos h − 1 = −sin²h / (1 + cos h).'],
      ['d/dx sin x = sin x × 0 + cos x × 1 = cos x'],
    ],
    result: 'The derivative of sin x is cos x. This used (sin h)/h → 1, which is only true when h is in radians.',
    live: (v) => { const h = v.h; return `h = ${fx(h, 2)}:  sin h = ${fx(Math.sin(h), 4)},  tan h = ${fx(Math.tan(h), 4)};  (sin h)/h = ${fx(Math.sin(h) / h, 4)},  (cos h − 1)/h = ${fx((Math.cos(h) - 1) / h, 4)}`; },
    draw(g) {
      const { ctx, c, i } = g, h = g.v.h;
      const ax = axes(g, -0.25, 1.4, -0.2, 1.7, true), X = ax.X, Y = ax.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      const P = [Math.cos(h), Math.sin(h)], T = [1, Math.tan(h)], hi = i >= 3;
      ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(1), Y(0)); ctx.lineTo(X(T[0]), Y(T[1])); ctx.closePath();
      ctx.globalAlpha = hi ? 0.14 : 0.06; ctx.fillStyle = c.sc2; ctx.fill(); ctx.globalAlpha = 1;
      ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(1), Y(0)); for (let k = 0; k <= 40; k++) { const t = h * k / 40; ctx.lineTo(X(Math.cos(t)), Y(Math.sin(t))); } ctx.closePath();
      ctx.globalAlpha = hi ? 0.3 : 0.12; ctx.fillStyle = c.red; ctx.fill(); ctx.globalAlpha = 1;
      ctx.beginPath(); for (let k = 0; k <= 60; k++) { const t = (Math.PI / 2) * k / 60; k ? ctx.lineTo(X(Math.cos(t)), Y(Math.sin(t))) : ctx.moveTo(X(1), Y(0)); }
      ctx.strokeStyle = c.rule; ctx.lineWidth = 1.4; ctx.stroke();
      ctx.beginPath(); for (let k = 0; k <= 40; k++) { const t = h * k / 40; k ? ctx.lineTo(X(Math.cos(t)), Y(Math.sin(t))) : ctx.moveTo(X(1), Y(0)); }
      ctx.strokeStyle = c.red; ctx.lineWidth = 3.4; ctx.stroke();
      seg(ctx, c, X(0), Y(0), X(T[0]), Y(T[1]), { color: c.ink3, dash: [5, 4], lw: 1.4 });
      seg(ctx, c, X(P[0]), Y(0), X(P[0]), Y(P[1]), { color: c.sc2, lw: 3 });
      seg(ctx, c, X(1), Y(0), X(1), Y(T[1]), { color: c.sc, lw: 3 });
      seg(ctx, c, X(0), Y(0), X(P[0]), Y(P[1]), { color: c.ink, lw: 1.8 });
      dot(ctx, X(P[0]), Y(P[1]), 5, c.ink); dot(ctx, X(1), Y(T[1]), 4.5, c.sc);
      text(ctx, c, 'sin h', X(P[0]) - 6, Y(P[1] / 2), { size: 11, color: c.sc2, align: 'right' });
      text(ctx, c, 'tan h', X(1) + 7, Y(T[1] / 2), { size: 11, color: c.sc, align: 'left' });
      text(ctx, c, 'arc = h', X(1) + 6, Y(0) + 13, { size: 11, color: c.red, align: 'left' });
      text(ctx, c, 'h', X(0.22 * Math.cos(h / 2)), Y(0.22 * Math.sin(h / 2)), { size: 11 });
      ctx.restore();
    },
  };

  /* ================= productrule ================= */
  S.productrule = {
    title: 'Where the product rule comes from', height: 300,
    sliders: [{ key: 'h', label: 'h', min: 0.05, max: 1, step: 0.05, value: 0.6 }],
    lines: [
      ['uv is the area of a rectangle: width u, height v', 'Here u = x² + 1 and v = x + 1, at x = 1: u = 2, v = 2.'],
      ['x goes up by h: u grows by δu and v grows by δv', 'The rectangle gets wider and taller.'],
      ['δ(uv) = v δu + u δv + δu δv', 'Three new pieces: a strip at the side, a strip on top and a small corner.'],
      ['δ(uv)/h = v (δu/h) + u (δv/h) + (δu/h) δv', 'Divide by h.'],
      ['as h → 0: δu/h → u′, δv/h → v′ and δv → 0', 'The corner term (δu/h) × δv tends to u′ × 0 = 0.'],
      ['d(uv)/dx = v u′ + u v′'],
    ],
    result: 'The product rule: d(uv)/dx = u′v + uv′. Check with x = 1: u′v + uv′ = 2 × 2 + 2 × 1 = 6, and uv = x³ + x² + x + 1 has gradient 3 + 2 + 1 = 6.',
    live: (v, s) => { const h = v.h, u = 2, vv = 2, du = (1 + h) ** 2 + 1 - 2, dv = h; return `h = ${fx(h, 2)}:  δu = ${fx(du, 3)},  δv = ${fx(dv, 3)};  δ(uv)/h = ${fx((du * vv + u * dv + du * dv) / h, 4)}${s >= 4 ? ',  tends to 6' : ''}`; },
    draw(g) {
      const { ctx, c, i } = g, h = g.v.h, u = 2, v = 2, du = (1 + h) ** 2 + 1 - 2, dv = h;
      const ax = axes(g, -0.3, 5.4, -0.3, 3.4, true), X = ax.X, Y = ax.Y;
      clipPlot(ctx, PAD, g.w, g.h);
      box(ctx, c, X(0), Y(v), X(u) - X(0), Y(0) - Y(v), { fill: c.sc });
      text(ctx, c, 'uv', X(u / 2), Y(v / 2), { size: 15 });
      text(ctx, c, 'u', X(u / 2), Y(0) + 14, { size: 12, color: c.ink2 }); text(ctx, c, 'v', X(0) - 11, Y(v / 2), { size: 12, color: c.ink2 });
      if (i >= 1) {
        box(ctx, c, X(u), Y(v), X(u + du) - X(u), Y(0) - Y(v), { fill: c.sc2, alpha: i >= 2 ? 0.35 : 0.08 });
        box(ctx, c, X(0), Y(v + dv), X(u) - X(0), Y(v) - Y(v + dv), { fill: c.sc2, alpha: i >= 2 ? 0.35 : 0.08 });
        box(ctx, c, X(u), Y(v + dv), X(u + du) - X(u), Y(v) - Y(v + dv), { fill: c.red, alpha: i >= 2 ? 0.5 : 0.08 });
        text(ctx, c, 'δu', X(u + du / 2), Y(0) + 14, { size: 12, color: c.sc2 }); text(ctx, c, 'δv', X(0) - 13, Y(v + dv / 2), { size: 12, color: c.sc2 });
      }
      if (i >= 2) {
        text(ctx, c, 'v δu', X(u + du / 2), Y(v / 2), { size: 11, color: c.ink });
        text(ctx, c, 'u δv', X(u / 2), Y(v + dv / 2), { size: 11, color: c.ink });
        if (X(u + du) - X(u) > 22 && Y(v) - Y(v + dv) > 12) text(ctx, c, 'δuδv', X(u + du / 2), Y(v + dv / 2), { size: 9, color: c.red });
      }
      ctx.restore();
    },
  };

  /* ================= dotcosine ================= */
  S.dotcosine = {
    title: 'Why a·b = |a||b| cos θ', height: 270,
    sliders: [{ key: 'th', label: 'θ (degrees)', min: 20, max: 160, step: 5, value: 60 }],
    lines: [
      ['Triangle OAB with OA = a, OB = b and angle θ at O', 'Here |a| = 4 and |b| = 3. Move θ.'],
      ['AB = b − a', 'Go from A back to O, then out to B.'],
      ['|b − a|² = |a|² + |b|² − 2|a||b| cos θ', 'The cosine rule in triangle OAB.'],
      ['|b − a|² = (b₁ − a₁)² + (b₂ − a₂)² + (b₃ − a₃)²', 'Magnitude squared, component by component.'],
      ['= |a|² + |b|² − 2(a₁b₁ + a₂b₂ + a₃b₃)', 'Expand each bracket: the squares make |a|² and |b|², and the cross terms are −2a₁b₁ and so on.'],
      ['a₁b₁ + a₂b₂ + a₃b₃ = |a||b| cos θ', 'Compare the two results: subtract |a|² + |b|² and divide by −2.'],
    ],
    result: 'a·b = a₁b₁ + a₂b₂ + a₃b₃ = |a||b| cos θ. If θ = 90° the cosine is 0, so perpendicular vectors have a·b = 0.',
    live: (v, s) => { const t = v.th * Math.PI / 180, ab = 12 * Math.cos(t), d2 = 25 - 24 * Math.cos(t); return s >= 2 ? `θ = ${fx(v.th, 3)}°:  |b − a|² = 16 + 9 − 24 cos θ = ${fx(d2, 4)},  a·b = 12 cos θ = ${fx(ab, 4)}` : `θ = ${fx(v.th, 3)}°`; },
    draw(g) {
      const { ctx, w, h, c, i } = g, t = g.v.th * Math.PI / 180;
      const u = Math.max(8, Math.min((w - 70) / 7.4, (h - 56) / 3.2));
      const ox = 36 + Math.max(0, -3 * Math.cos(t)) * u, oy = h - 26;
      const A = [ox + 4 * u, oy], B = [ox + 3 * u * Math.cos(t), oy - 3 * u * Math.sin(t)];
      if (i >= 1) seg(ctx, c, A[0], A[1], B[0], B[1], { color: c.red, lw: 2.4, dash: i === 1 ? undefined : [6, 4] });
      seg(ctx, c, ox, oy, A[0], A[1], { color: c.sc, lw: 2.8 }); seg(ctx, c, ox, oy, B[0], B[1], { color: c.sc2, lw: 2.8 });
      ctx.beginPath(); ctx.arc(ox, oy, 28, 0, -t, true); ctx.strokeStyle = c.ink; ctx.lineWidth = 1.4; ctx.stroke();
      text(ctx, c, 'θ', ox + 40 * Math.cos(t / 2), oy - 40 * Math.sin(t / 2), { size: 13 });
      dot(ctx, ox, oy, 4, c.ink); dot(ctx, A[0], A[1], 4, c.sc); dot(ctx, B[0], B[1], 4, c.sc2);
      text(ctx, c, 'O', ox - 11, oy + 4); text(ctx, c, 'A', A[0] + 11, A[1] + 3, { color: c.sc }); text(ctx, c, 'B', B[0], B[1] - 12, { color: c.sc2 });
      text(ctx, c, 'a', (ox + A[0]) / 2, oy + 14, { color: c.sc, size: 13 });
      text(ctx, c, 'b', (ox + B[0]) / 2 - 12, (oy + B[1]) / 2 - 6, { color: c.sc2, size: 13 });
      if (i >= 1) text(ctx, c, 'b − a', (A[0] + B[0]) / 2 + 24, (A[1] + B[1]) / 2 - 8, { color: c.red, size: 12 });
    },
  };

  /* ================= tree ================= */
  S.tree = {
    title: 'Why you multiply along a branch', height: 290,
    sliders: [
      { key: 'pa', label: 'P(A)', min: 0.1, max: 0.9, step: 0.1, value: 0.6 },
      { key: 'p1', label: 'P(B | A)', min: 0.1, max: 0.9, step: 0.1, value: 0.3 },
      { key: 'p2', label: 'P(B | A′)', min: 0.1, max: 0.9, step: 0.1, value: 0.5 },
    ],
    lines: [
      ['A square of area 1 stands for every outcome', 'Equal areas are equal probabilities.'],
      ['P(A) = the width of the left strip', 'The strip A has width P(A). The rest, A′, has width 1 − P(A).'],
      ['Inside A, a fraction P(B | A) is also in B', 'Given A, you only look inside the strip. P(B | A) is the share of the strip that lies in B.'],
      ['P(A ∩ B) = width × height = P(A) × P(B | A)', 'The shaded rectangle has width P(A) and height P(B | A). This is the multiplication rule: multiply along the branch.'],
      ['If P(B | A) = P(B), then P(A ∩ B) = P(A) P(B)', 'Knowing A changes nothing about B. That is independence.'],
      ['P(A′ ∩ B) = P(A′) × P(B | A′)', 'The right strip works the same way, with its own fraction.'],
      ['P(B) = P(A) P(B | A) + P(A′) P(B | A′)', 'B is the two shaded rectangles. Add the branches that end in B.'],
    ],
    result: 'P(A ∩ B) = P(A) × P(B | A): multiply along a branch, and add the branches that end in B.',
    live: (v, s) => {
      const a = v.pa, p1 = v.p1, p2 = v.p2;
      if (s < 3) return `P(A) = ${fx(a, 2)}, P(B | A) = ${fx(p1, 2)}`;
      if (s < 5) return `P(A ∩ B) = ${fx(a, 2)} × ${fx(p1, 2)} = ${fx(a * p1, 3)}`;
      if (s === 5) return `P(A′ ∩ B) = ${fx(1 - a, 2)} × ${fx(p2, 2)} = ${fx((1 - a) * p2, 3)}`;
      return `P(B) = ${fx(a * p1, 3)} + ${fx((1 - a) * p2, 3)} = ${fx(a * p1 + (1 - a) * p2, 3)}`;
    },
    draw(g) {
      const { ctx, w, h, c, i } = g, a = g.v.pa, p1 = g.v.p1, p2 = g.v.p2;
      const s = Math.max(120, Math.min(h - 46, w - 80)), ox = Math.max(36, (w - s) / 2), oy = 10, wa = a * s;
      if (i >= 1) box(ctx, c, ox, oy, wa, s, { fill: c.sc, alpha: 0.1 });
      if (i >= 2) box(ctx, c, ox, oy + s - p1 * s, wa, p1 * s, { fill: c.sc, alpha: i >= 3 ? 0.45 : 0.3 });
      if (i >= 4 && i < 5) seg(ctx, c, ox, oy + s - p1 * s, ox + s, oy + s - p1 * s, { color: c.red, lw: 1.6, dash: [6, 4] });
      if (i >= 5) box(ctx, c, ox + wa, oy + s - p2 * s, s - wa, p2 * s, { fill: c.sc2, alpha: 0.45 });
      ctx.save(); ctx.strokeStyle = c.rule; ctx.lineWidth = 1.6; ctx.strokeRect(ox + 0.5, oy + 0.5, s, s); ctx.restore();
      if (i >= 1) {
        seg(ctx, c, ox + wa, oy, ox + wa, oy + s, { color: c.ink2, lw: 1.4 });
        text(ctx, c, 'A', ox + wa / 2, oy + s + 14, { color: c.sc, size: 13 });
        text(ctx, c, 'A′', ox + wa + (s - wa) / 2, oy + s + 14, { color: c.sc2, size: 13 });
        text(ctx, c, fx(a, 2), ox + wa / 2, oy + s + 30, { size: 11, color: c.ink2 });
        text(ctx, c, fx(1 - a, 2), ox + wa + (s - wa) / 2, oy + s + 30, { size: 11, color: c.ink2 });
      }
      if (i >= 3 && wa > 54 && p1 * s > 22) text(ctx, c, 'A ∩ B', ox + wa / 2, oy + s - p1 * s / 2, { size: 12 });
      if (i >= 5 && s - wa > 62 && p2 * s > 22) text(ctx, c, 'A′ ∩ B', ox + wa + (s - wa) / 2, oy + s - p2 * s / 2, { size: 12 });
      if (i === 0) text(ctx, c, 'all outcomes', ox + s / 2, oy + s / 2, { size: 13, color: c.ink2 });
    },
  };

  /* ================= pythagoras ================= */
  S.pythagoras = {
    title: "Why a² + b² = c² (Pythagoras' theorem)", height: 290,
    sliders: [{ key: 'a', label: 'a', min: 1, max: 6, step: 0.5, value: 3 }, { key: 'b', label: 'b', min: 1, max: 6, step: 0.5, value: 4 }],
    lines: [
      ['A right-angled triangle with legs a and b and hypotenuse c', 'Change a and b. We want a rule that links c to them.'],
      ['Put four copies inside a square of side a + b', 'Each copy has its short leg along one side, so the sides of the big square are a + b long. Area of the big square = (a + b)².'],
      ['The four hypotenuses make a tilted square of side c', 'Its corners are right angles because the two acute angles of the triangle add to 90°. Its area is c².'],
      ['(a + b)² = 4 × ½ab + c²', 'The big square is four triangles plus the tilted square.'],
      ['a² + 2ab + b² = 2ab + c²', 'Expand the left side. On the right, 4 × ½ab = 2ab.'],
      ['a² + b² = c²', 'Subtract 2ab from both sides.'],
    ],
    result: 'a² + b² = c²: in a right-angled triangle the square on the hypotenuse equals the sum of the squares on the other two sides.',
    live: (v, s) => { const c2 = v.a * v.a + v.b * v.b; return s < 3 ? `a = ${fx(v.a, 2)}, b = ${fx(v.b, 2)},  c = ${fx(Math.sqrt(c2), 4)}` : `(a + b)² = ${fx((v.a + v.b) ** 2, 4)},  2ab + c² = ${fx(2 * v.a * v.b + c2, 4)}  (equal)`; },
    draw(g) {
      const { ctx, w, h, c, i } = g, a = g.v.a, b = g.v.b, S0 = a + b;
      if (i === 0) {
        const u = Math.min((w - 90) / b, (h - 70) / a), ox = (w - b * u) / 2, oy = h - 30;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + b * u, oy); ctx.lineTo(ox, oy - a * u); ctx.closePath();
        ctx.globalAlpha = 0.22; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1; ctx.strokeStyle = c.sc; ctx.lineWidth = 2.2; ctx.stroke();
        ctx.strokeStyle = c.ink; ctx.lineWidth = 1.2; ctx.strokeRect(ox + 0.5, oy - 12.5, 12, 12);
        text(ctx, c, 'b', ox + b * u / 2, oy + 14, { color: c.sc, size: 13 });
        text(ctx, c, 'a', ox - 12, oy - a * u / 2, { color: c.sc, size: 13 });
        text(ctx, c, 'c', ox + b * u / 2 + 12, oy - a * u / 2 - 8, { color: c.red, size: 13 });
        return;
      }
      const s = Math.min(h - 40, w - 60), u = s / S0, ox = (w - s) / 2, oy = 12;
      const P = (x, y) => [ox + x * u, oy + s - y * u];            // y up inside the big square
      const tri = (p, q, r, alpha) => { ctx.beginPath(); ctx.moveTo(...p); ctx.lineTo(...q); ctx.lineTo(...r); ctx.closePath(); ctx.globalAlpha = alpha; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1; ctx.strokeStyle = c.sc; ctx.lineWidth = 1.6; ctx.stroke(); };
      const m = [P(a, 0), P(S0, a), P(S0 - a, S0), P(0, S0 - a)];    // corners of the tilted square
      const k = [P(0, 0), P(S0, 0), P(S0, S0), P(0, S0)];
      for (let j = 0; j < 4; j++) tri(k[j], m[j], m[(j + 3) % 4], i >= 3 ? 0.32 : 0.2);
      ctx.beginPath(); m.forEach((p, j) => (j ? ctx.lineTo(...p) : ctx.moveTo(...p))); ctx.closePath();
      if (i >= 2) { ctx.globalAlpha = 0.28; ctx.fillStyle = c.red; ctx.fill(); ctx.globalAlpha = 1; ctx.strokeStyle = c.red; ctx.lineWidth = 2.2; ctx.stroke(); }
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.6; ctx.strokeRect(ox + 0.5, oy + 0.5, s, s);
      text(ctx, c, 'a', ox + a * u / 2, oy + s + 12, { size: 12, color: c.sc }); text(ctx, c, 'b', ox + a * u + b * u / 2, oy + s + 12, { size: 12, color: c.sc });
      if (i >= 2) text(ctx, c, 'c²', ox + s / 2, oy + s / 2, { size: 16, color: c.red });
      if (i >= 3) for (let j = 0; j < 4; j++) { const q = m[(j + 3) % 4]; text(ctx, c, '½ab', (k[j][0] + m[j][0] + q[0]) / 3, (k[j][1] + m[j][1] + q[1]) / 3, { size: 10 }); }
    },
  };

  /* ================= cosinerule ================= */
  S.cosinerule = {
    title: 'Where the cosine rule comes from', height: 290,
    sliders: [{ key: 'A', label: 'angle A (degrees)', min: 25, max: 155, step: 5, value: 65 }],
    lines: [
      ['Triangle ABC with AB = c, AC = b and angle A between them', 'Here b = 4 and c = 5. We want the side a opposite A.'],
      ['Drop the perpendicular CD from C to the line AB', 'This splits the problem into right-angled triangles.'],
      ['AD = b cos A and CD = b sin A', 'SOH CAH TOA in the right-angled triangle ACD. If A is obtuse, cos A is negative and D lies on the other side of A: the algebra below still works.'],
      ['DB = c − b cos A', 'D to B is the whole of AB less the part AD.'],
      ['a² = CD² + DB² = (b sin A)² + (c − b cos A)²', 'Pythagoras in the right-angled triangle CDB.'],
      ['a² = b² sin²A + c² − 2bc cos A + b² cos²A', 'Expand the bracket.'],
      ['a² = b²(sin²A + cos²A) + c² − 2bc cos A = b² + c² − 2bc cos A', 'Take b² out of the two terms that have it, then use sin²A + cos²A = 1.'],
    ],
    result: 'a² = b² + c² − 2bc cos A. When A = 90°, cos A = 0 and this is Pythagoras.',
    live: (v) => { const t = v.A * Math.PI / 180; return `A = ${fx(v.A, 3)}°:  a² = 16 + 25 − 40 cos A = ${fx(41 - 40 * Math.cos(t), 4)},  a = ${fx(Math.sqrt(41 - 40 * Math.cos(t)), 4)}`; },
    draw(g) {
      const { ctx, w, h, c, i } = g, t = g.v.A * Math.PI / 180, b = 4, cc = 5;
      const cx = b * Math.cos(t), cy = b * Math.sin(t), minX = Math.min(0, cx);
      const u = Math.min((w - 70) / (cc - minX), (h - 56) / cy), ox = (w - (cc - minX) * u) / 2 - minX * u, oy = h - 28;
      const P = (x, y) => [ox + x * u, oy - y * u], A0 = P(0, 0), B = P(cc, 0), C = P(cx, cy), D = P(cx, 0);
      if (i >= 1) {
        seg(ctx, c, C[0], C[1], D[0], D[1], { color: c.red, lw: 2, dash: [6, 4] });
        if (cx < 0) seg(ctx, c, D[0], D[1], A0[0], A0[1], { color: c.ink3, lw: 1.4, dash: [3, 4] });
        ctx.strokeStyle = c.ink; ctx.lineWidth = 1.2; const sg = cx >= 0 ? -1 : 1; ctx.strokeRect(D[0] + (sg < 0 ? -11 : 0) + 0.5, D[1] - 11.5, 11, 11);
      }
      seg(ctx, c, A0[0], A0[1], B[0], B[1], { color: c.sc, lw: 2.6 }); seg(ctx, c, A0[0], A0[1], C[0], C[1], { color: c.sc2, lw: 2.6 }); seg(ctx, c, B[0], B[1], C[0], C[1], { color: c.ink, lw: 2.6 });
      ctx.beginPath(); ctx.arc(A0[0], A0[1], 24, 0, -t, true); ctx.strokeStyle = c.ink; ctx.lineWidth = 1.3; ctx.stroke();
      text(ctx, c, 'A', A0[0] - 11, A0[1] + 10); text(ctx, c, 'B', B[0] + 11, B[1] + 8); text(ctx, c, 'C', C[0], C[1] - 12);
      if (i >= 1) text(ctx, c, 'D', D[0] + (cx >= 0 ? 0 : 0), D[1] + 13, { size: 12 });
      text(ctx, c, 'c', (A0[0] + B[0]) / 2, A0[1] + 14, { color: c.sc, size: 13 });
      text(ctx, c, 'b', (A0[0] + C[0]) / 2 - 10, (A0[1] + C[1]) / 2 - 6, { color: c.sc2, size: 13 });
      text(ctx, c, 'a', (B[0] + C[0]) / 2 + 12, (B[1] + C[1]) / 2 - 6, { size: 13 });
      if (i >= 2) { text(ctx, c, 'b sin A', D[0] + (cx >= 0 ? 34 : -34), (C[1] + D[1]) / 2, { size: 11, color: c.red }); }
      if (i >= 3) text(ctx, c, 'DB', (D[0] + B[0]) / 2, B[1] - 10, { size: 11, color: c.ink2 });
    },
  };
})();
