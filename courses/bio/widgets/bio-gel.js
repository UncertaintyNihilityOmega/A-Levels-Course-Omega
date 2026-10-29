/* widgets/bio-gel.js: gel electrophoresis of DNA cut by restriction endonucleases. Used in bio.genetech.
   Model (stated on screen): DNA is negative and runs from the wells (cathode, -) to the anode (+); a fragment of length L bp travels a distance
   proportional to log10(M) - log10(L), where M is just above the longest length shown, so shorter fragments travel further; equal lengths make one thicker band.
   Attributes: data-dna = length of the linear DNA in bp (200 to 20000, default 5000); data-cuts = cut positions of lane 1 in bp from one end (default "1200,3100").
   Enzyme A cuts at 24% and 62% of the length, enzyme B at 40% (the same as 1200, 3100 and 2000 bp when the DNA is 5000 bp). Pure functions are exported for data/test_bio-gel.js. */
(function () {
  'use strict';

  const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
  const LADDER = [5000, 3000, 2000, 1000, 500, 200, 100];
  const MINLEN = 50;
  const FRAC = { A: [0.24, 0.62], B: [0.40], AB: [0.24, 0.40, 0.62] };

  function numOr(v, d, lo, hi) { const x = parseFloat(v); return isFinite(x) ? clamp(x, lo, hi) : d; }

  // text "1200, 3100" -> {cuts: sorted unique integers strictly inside (0, L), bad: [rejected items]}
  function parseCuts(text, L) {
    const out = { cuts: [], bad: [] };
    String(text == null ? '' : text).split(/[\s,;]+/).forEach(function (s) {
      if (s === '') return;
      const x = Number(s);
      if (!isFinite(x) || x <= 0 || x >= L || Math.round(x) !== x) { out.bad.push(s); return; }
      if (out.cuts.indexOf(x) < 0) out.cuts.push(x);
    });
    out.cuts.sort(function (a, b) { return a - b; });
    return out;
  }
  function presetCuts(kind, L) {
    const f = FRAC[kind] || [];
    const set = [];
    f.forEach(function (p) { const c = Math.round(p * L); if (c > 0 && c < L && set.indexOf(c) < 0) set.push(c); });
    return set.sort(function (a, b) { return a - b; });
  }
  // linear DNA of length L cut at the sorted positions: the fragment lengths (in order along the DNA)
  function fragments(L, cuts) {
    const pts = [0].concat(cuts, [L]);
    const out = [];
    for (let i = 1; i < pts.length; i++) out.push(pts[i] - pts[i - 1]);
    return out;
  }
  // [[length, count], ...] longest first
  function groups(frags) {
    const m = {};
    frags.forEach(function (f) { m[f] = (m[f] || 0) + 1; });
    return Object.keys(m).map(function (k) { return [Number(k), m[k]]; }).sort(function (a, b) { return b[0] - a[0]; });
  }
  // fraction of the gel length (0 at the wells, 1 at the bottom) reached by a fragment of length len when the longest length shown is M
  function travel(len, M) {
    const lo = Math.log10(MINLEN), hi = Math.log10(M);
    if (!(hi > lo)) return 0;
    return clamp((hi - Math.log10(isFinite(len) ? Math.max(len, 1) : 1)) / (hi - lo), 0, 1);
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { parseCuts, presetCuts, fragments, groups, travel, numOr, LADDER, MINLEN };
  if (typeof W === 'undefined') return;

  W.register('bio-gel', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Gel electrophoresis of cut DNA', 'Choose the DNA and the cuts, then run the gel');
    const S = {
      L: Math.round(numOr(opts.dna, 5000, 200, 20000)),
      own: opts.cuts != null && opts.cuts !== '' ? String(opts.cuts) : '1200,3100',
      mode: ['own', 'B', 'AB'],
      p: 1
    };

    const TREAT = [['off', 'Lane not used'], ['uncut', 'Uncut DNA'], ['A', 'Enzyme A'], ['B', 'Enzyme B'], ['AB', 'Enzymes A and B together'], ['own', 'My own cut positions']];
    function treatName(k) { for (let i = 0; i < TREAT.length; i++) if (TREAT[i][0] === k) return TREAT[i][1]; return k; }

    // compute the three lanes from the state
    function lanes() {
      const pc = parseCuts(S.own, S.L);
      return S.mode.map(function (m) {
        let cuts = [];
        if (m === 'own') cuts = pc.cuts;
        else if (m === 'A' || m === 'B' || m === 'AB') cuts = presetCuts(m, S.L);
        if (m === 'off') return { mode: m, frags: [], groups: [], cuts: [] };
        const fr = fragments(S.L, cuts);
        return { mode: m, cuts: cuts, frags: fr, groups: groups(fr) };
      });
    }
    function scaleMax(ls) {
      let m = Math.max(5000, S.L);
      ls.forEach(function (l) { l.frags.forEach(function (f) { m = Math.max(m, f); }); });
      return m * 1.15;
    }
    function fmtGroups(g) {
      return g.map(function (x) { return x[0] + ' bp' + (x[1] > 1 ? ' × ' + x[1] : ''); }).join(', ');
    }

    function describe() {
      const ls = lanes();
      let s = 'Gel with a DNA ladder of 5000, 3000, 2000, 1000, 500, 200 and 100 base pairs and three sample lanes. Wells are at the top (negative) and shorter fragments have travelled further towards the positive end. ';
      ls.forEach(function (l, i) {
        s += 'Lane ' + (i + 1) + ': ' + (l.mode === 'off' ? 'not used. ' : treatName(l.mode) + ', bands at ' + fmtGroups(l.groups) + '. ');
      });
      return s + (S.p < 1 ? 'The gel is still running.' : '');
    }

    function draw(ctx, w, h, c) {
      if (!(w > 0) || !(h > 0) || w < 240 || h < 200) return;
      const ls = lanes(), M = scaleMax(ls);
      const padL = 52, padR = 28, top = 34, bot = h - 18;
      const gx0 = padL - 6, gx1 = w - padR + 14;
      const nL = 4, laneW = (gx1 - gx0) / nL, bw = Math.min(46, laneW * 0.72);
      const wellY = top + 8, y0 = wellY + 8, y1 = bot - 8;
      const ease = 1 - Math.pow(1 - S.p, 2.2);
      // gel
      ctx.save();
      ctx.fillStyle = c.card; ctx.strokeStyle = c.rule2; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.rect(gx0, top, gx1 - gx0, bot - top); ctx.fill(); ctx.stroke();
      ctx.restore();
      const font = '12px ' + (c.font || 'sans-serif');
      function label(txt, x, y, align, color, size) {
        ctx.save(); ctx.font = (size || 12) + 'px ' + (c.font || 'sans-serif'); ctx.textAlign = align; ctx.textBaseline = 'alphabetic';
        ctx.fillStyle = color || c.ink; ctx.fillText(txt, x, y); ctx.restore();
      }
      const names = ['ladder', 'lane 1', 'lane 2', 'lane 3'];
      for (let i = 0; i < nL; i++) {
        const cx = gx0 + laneW * (i + 0.5);
        // well
        ctx.save(); ctx.fillStyle = c.sheet; ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.rect(cx - bw / 2, top + 2, bw, 10); ctx.fill(); ctx.stroke(); ctx.restore();
        label(names[i], cx, top - 8, 'center', c.ink2, 11);
        const dead = i > 0 && ls[i - 1].mode === 'off';
        if (dead) { label('(unused)', cx, top + 34, 'center', c.ink3, 11); continue; }
        const bands = i === 0 ? LADDER.map(function (L) { return [L, 1]; }) : ls[i - 1].groups;
        bands.forEach(function (g) {
          const target = y0 + travel(g[0], M) * (y1 - y0);
          const y = wellY + (target - wellY) * ease;
          const th = i === 0 ? 3 : clamp(3 + 3.5 * (g[1] - 1), 3, 14);
          ctx.save();
          ctx.fillStyle = i === 0 ? c.sc2 : c.sc; ctx.globalAlpha = i === 0 ? 0.85 : 1;
          ctx.beginPath(); ctx.rect(cx - bw / 2, y - th / 2, bw, th); ctx.fill();
          ctx.restore();
          if (i === 0 && S.p >= 1) label(String(g[0]), gx0 - 5, y + 4, 'right', c.ink2, 11);
        });
      }
      label('−', gx1 + 10, top + 12, 'center', c.red, 16);
      label('+', gx1 + 10, bot - 2, 'center', c.red, 16);
      if (S.p >= 1) label('bp', gx0 - 5, top + 12, 'right', c.ink3, 10);
      void font;
    }

    const cv = W.canvas(body, {
      height: 300,
      label: 'Drawing of an agarose gel with a DNA ladder and three sample lanes, wells at the negative end, bands of DNA fragments',
      describe: describe,
      draw: draw
    });

    // ---------------- controls
    const err = W.h('div', { class: 'w-err', role: 'status', 'aria-live': 'polite' });
    const fLen = W.field({ label: 'Length of the linear DNA / bp', value: S.L, type: 'number', step: 100, width: '7em', oninput: function () { S.L = Math.round(numOr(fLen.get(), S.L, 200, 20000)); settle(); } });
    const fCuts = W.field({ label: 'Own cut positions / bp from one end, separated by commas', value: S.own, type: 'text', width: '100%', oninput: function () { S.own = fCuts.get(); settle(); } });
    fCuts.el.style.flex = '1 1 14em'; fCuts.el.style.maxWidth = '26em';
    body.appendChild(W.h('div', { class: 'w-row' }, fLen.el, fCuts.el));

    const sels = [];
    const selRow = W.h('div', { class: 'w-row' });
    for (let i = 0; i < 3; i++) {
      const sel = W.h('select', { 'aria-label': 'Treatment of the DNA in lane ' + (i + 1) });
      TREAT.forEach(function (t) { sel.appendChild(W.h('option', { value: t[0], text: t[1] })); });
      sel.value = S.mode[i];
      sel.onchange = function () { S.mode[i] = sel.value; settle(); };
      sels.push(sel);
      selRow.appendChild(W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Lane ' + (i + 1) }), sel));
    }
    body.appendChild(selRow);

    const runBtn = W.h('button', { class: 'btn btn-sm', type: 'button', text: 'Run the gel' });
    const resetBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', text: 'Reset', 'aria-label': 'Reset: return the DNA to the wells' });
    body.appendChild(W.h('div', { class: 'w-row' }, runBtn, resetBtn));
    body.appendChild(err);

    const ro = W.readout([['1', 'Lane 1 fragments'], ['2', 'Lane 2 fragments'], ['3', 'Lane 3 fragments']]);
    body.appendChild(ro.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'DNA is negatively charged (phosphate groups), so it moves from the wells at the negative end towards the positive end, the anode. The agarose gel is a mesh, so shorter fragments move further. In this model the distance moved depends on the logarithm of the length. Try: (1) run the gel and compare lane 1 with the ladder; (2) set a lane to "A and B together" and count the bands; (3) type cuts that make two equal fragments, such as 1500, 3500 in 5000 bp, and see one thicker band.' }));

    let t0 = 0;
    const anim = W.animate(function () {
      S.p = clamp((Date.now() - t0) / 3200, 0, 1);
      cv.redraw();
      return S.p < 1;
    }, { still: function () { S.p = 1; cv.redraw(); } });

    function showReadout() {
      const ls = lanes();
      ls.forEach(function (l, i) {
        const total = l.frags.reduce(function (a, b) { return a + b; }, 0);
        ro.set(String(i + 1), l.mode === 'off' ? 'not used' : treatName(l.mode) + ': ' + fmtGroups(l.groups) + ' (total ' + total + ' bp)');
      });
    }
    function settle() {
      // keep the fields in step with the clamped state
      const pc = parseCuts(S.own, S.L);
      err.textContent = pc.bad.length && S.mode.indexOf('own') >= 0 ? 'Ignored (not a whole number between 0 and ' + S.L + '): ' + pc.bad.join(', ') : '';
      anim.stop();
      S.p = 1;
      showReadout();
      cv.redraw();
    }
    runBtn.onclick = function () {
      anim.stop();
      S.p = 0; t0 = Date.now();
      if (W.reducedMotion && W.reducedMotion()) { anim.start(); showReadout(); return; }
      cv.redraw(); anim.start(); showReadout();
    };
    resetBtn.onclick = function () { anim.stop(); S.p = 0; cv.redraw(); showReadout(); };

    settle();
  });
})();
