/* sampling: the sample mean as a random variable, and confidence intervals that hit or miss.
   data-mode means | ci   data-pop uniform | skewed | normal | bernoulli   data-n 10   data-p 0.3 (bernoulli)
   data-level 95 (ci mode: 90, 95 or 99)   data-seed (optional, for a repeatable run) */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const num = (v, d) => { const n = parseFloat(v); return isFinite(n) ? n : d; };
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

  const POPS = {
    uniform: { name: 'Uniform', range: [0, 10], mu: () => 5, sd: () => Math.sqrt(100 / 12), pdf: () => 0.1, draw: (r) => r() * 10, label: 'uniform on 0 to 10' },
    skewed: { name: 'Skewed', range: [0, 12], mu: () => 2, sd: () => 2, pdf: (x) => (x < 0 ? 0 : 0.5 * Math.exp(-x / 2)), draw: (r) => -2 * Math.log(1 - r()), label: 'skewed (μ 2, σ 2)' },
    normal: { name: 'Normal', range: [0, 10], mu: () => 5, sd: () => 1.5, pdf: (x) => Math.exp(-((x - 5) ** 2) / (2 * 2.25)) / (1.5 * Math.sqrt(2 * Math.PI)), draw: null, label: 'normal (μ 5, σ 1.5)' },
    bernoulli: { name: 'Yes / no', range: [-0.3, 1.3], mu: (p) => p, sd: (p) => Math.sqrt(p * (1 - p)), pdf: null, draw: null, label: 'yes / no' },
  };
  const Z = { 90: 1.6448536269514722, 95: 1.959963984540054, 99: 2.5758293035489004 };

  W.register('sampling', function (el, o) {
    const warn = [];
    const mode = String(o.mode) === 'ci' ? 'ci' : 'means';
    let pop = String(o.pop || (mode === 'ci' ? 'normal' : 'skewed')).toLowerCase();
    if (!POPS[pop]) { warn.push(`Unknown population "${o.pop}". Using ${mode === 'ci' ? 'normal' : 'skewed'}.`); pop = mode === 'ci' ? 'normal' : 'skewed'; }
    let n = Math.round(clamp(num(o.n, mode === 'ci' ? 25 : 10), 1, 200));
    let p = clamp(num(o.p, 0.3), 0.05, 0.95);
    let level = Object.prototype.hasOwnProperty.call(Z, String(o.level)) ? parseInt(o.level, 10) : 95;
    if (o.level != null && !Z[String(o.level)]) warn.push('data-level must be 90, 95 or 99. Using 95.');

    // seeded generator (mulberry32) with Box-Muller for normal values
    let seed = (o.seed != null && isFinite(parseFloat(o.seed)) ? parseFloat(o.seed) : Math.floor(Math.random() * 1e9)) >>> 0;
    const rnd = () => { seed = (seed + 0x6D2B79F5) >>> 0; let t = seed; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
    const gauss = () => Math.sqrt(-2 * Math.log(1 - rnd())) * Math.cos(2 * Math.PI * rnd());
    const one = () => (pop === 'normal' ? 5 + 1.5 * gauss() : pop === 'bernoulli' ? (rnd() < p ? 1 : 0) : POPS[pop].draw(rnd));
    const mu = () => POPS[pop].mu(p), sd = () => POPS[pop].sd(p);
    const sampleMean = () => { let s = 0; for (let i = 0; i < n; i++) s += one(); return s / n; };

    const { body } = W.frame(el, mode === 'ci' ? 'Confidence intervals: hit or miss' : 'The sample mean varies less than one value',
      mode === 'ci' ? 'many samples, one interval from each' : 'draw samples and watch the means pile up');

    const means = [];            // sample means (means mode)
    const ivs = [];              // {m, hit} for the last intervals (ci mode)
    let total = 0, hits = 0, last = null;
    const MAXKEEP = 6000, SHOW = 40;

    /* controls */
    const row = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } });
    const tabs = W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Population shape' });
    const tabBtns = [];
    for (const k of Object.keys(POPS)) {
      const b = W.h('button', { type: 'button', class: 'w-tab', role: 'tab', 'aria-selected': String(k === pop) }, POPS[k].name);
      b.addEventListener('click', () => { pop = k; tabBtns.forEach(([kk, bb]) => bb.setAttribute('aria-selected', String(kk === pop))); pSl.el.style.display = pop === 'bernoulli' ? '' : 'none'; reset(); });
      tabBtns.push([k, b]); tabs.append(b);
    }
    row.append(tabs);
    const nSl = W.sliderNum({ label: 'Sample size n', min: 1, max: 200, step: 1, value: n, oninput: (v) => { const m = Math.round(clamp(v, 1, 200)); if (m !== n) { n = m; reset(); } } });
    const pSl = W.sliderNum({ label: 'Proportion p', min: 0.05, max: 0.95, step: 0.05, value: p, oninput: (v) => { const m = clamp(v, 0.05, 0.95); if (m !== p) { p = m; reset(); } } });
    pSl.el.style.display = pop === 'bernoulli' ? '' : 'none';
    row.append(nSl.el, pSl.el);
    body.append(row);

    const row2 = W.h('div', { class: 'w-row' });
    const btn = (t, f, sec) => { const b = W.h('button', { type: 'button', class: 'btn btn-sm' + (sec ? ' btn-sec' : '') }, t); b.addEventListener('click', f); return b; };
    if (mode === 'ci') {
      const lv = W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Confidence level' });
      const lvB = [];
      for (const k of [90, 95, 99]) {
        const b = W.h('button', { type: 'button', class: 'w-tab', role: 'tab', 'aria-selected': String(k === level) }, k + '%');
        b.addEventListener('click', () => { level = k; lvB.forEach(([kk, bb]) => bb.setAttribute('aria-selected', String(kk === level))); reset(); });
        lvB.push([k, b]); lv.append(b);
      }
      row2.append(lv, btn('Draw 1 interval', () => draw(1)), btn('Draw 20 intervals', () => draw(20)), btn('Clear', reset, true));
    } else {
      row2.append(btn('Draw 1 sample', () => draw(1)), btn('Draw 100 samples', () => draw(100)), btn('Clear', reset, true));
    }
    body.append(row2);

    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const cv = W.canvas(body, { height: mode === 'ci' ? 300 : 320, draw: render });
    cv.wrap.setAttribute('role', 'img');
    const R = W.readout(mode === 'ci'
      ? [['pop', 'Population'], ['n', 'Intervals drawn'], ['hit', 'Containing the true mean'], ['exp', 'Expected share'], ['width', 'Width of each interval']]
      : [['pop', 'Population'], ['n', 'Samples drawn'], ['mean', 'Mean of the sample means'], ['sd', 'Spread of the sample means']]);
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, mode === 'ci'
      ? 'Draw 20 intervals several times. Each blue interval is one sample\'s x̄ ± zσ/√n; a red one has missed the true mean. About 95% should hit when the level is 95%; a higher level makes every interval wider.'
      : 'Start with the skewed population and n = 1: the means copy the skewed shape. Raise n and draw 100 samples again: the pile of means becomes narrow and bell-shaped, centred on μ, close to the curve N(μ, σ²/n).'));

    function reset() { means.length = 0; ivs.length = 0; total = 0; hits = 0; last = null; update(); }

    function draw(k) {
      for (let i = 0; i < k; i++) {
        const m = sampleMean();
        total++;
        if (mode === 'ci') {
          const half = Z[level] * sd() / Math.sqrt(n), hit = Math.abs(m - mu()) <= half;
          if (hit) hits++;
          ivs.push({ m, half, hit }); if (ivs.length > SHOW) ivs.shift();
        } else {
          if (means.length < MAXKEEP) means.push(m);
        }
        last = m;
      }
      update();
    }

    function update() {
      R.set('pop', POPS[pop].label + (pop === 'bernoulli' ? ` (p = ${W.fmt(p, 2)})` : ''));
      R.set('n', String(total));
      if (mode === 'ci') {
        R.set('hit', total ? `${hits} of ${total} (${W.fmt(100 * hits / total, 3)}%)` : '—');
        R.set('exp', level + '%');
        R.set('width', W.fmt(2 * Z[level] * sd() / Math.sqrt(n), 3));
      } else {
        if (means.length) {
          const mm = means.reduce((a, b) => a + b, 0) / means.length;
          const v = means.length > 1 ? means.reduce((a, b) => a + (b - mm) ** 2, 0) / (means.length - 1) : 0;
          R.set('mean', `${W.fmt(mm, 3)} (true μ = ${W.fmt(mu(), 3)})`);
          R.set('sd', `${W.fmt(Math.sqrt(v), 3)} (σ/√n = ${W.fmt(sd() / Math.sqrt(n), 3)})`);
        } else { R.set('mean', `— (true μ = ${W.fmt(mu(), 3)})`); R.set('sd', `— (σ/√n = ${W.fmt(sd() / Math.sqrt(n), 3)})`); }
      }
      cv.wrap.setAttribute('aria-label', mode === 'ci'
        ? `${total} confidence intervals drawn at ${level}%, ${hits} contain the true mean ${W.fmt(mu(), 3)}.`
        : `${total} sample means of size ${n} from a ${POPS[pop].label} population, centred near ${W.fmt(mu(), 3)} with standard deviation about ${W.fmt(sd() / Math.sqrt(n), 3)}.`);
      cv.redraw();
    }

    function render(ctx, w, h, c) {
      let [x0, x1] = POPS[pop].range;
      if (mode === 'ci') { const H = 3.4 * sd() / Math.sqrt(n); x0 = mu() - H; x1 = mu() + H; }
      const L = 14, Rr = w - 14;
      const X = (x) => L + (x - x0) / (x1 - x0) * (Rr - L);
      const axisFor = (y) => {
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(L, Math.round(y) + 0.5); ctx.lineTo(Rr, Math.round(y) + 0.5); ctx.stroke();
      };
      const ticksAt = (y, labels) => {
        ctx.fillStyle = c.ink2; ctx.font = '11px ' + c.font; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        ctx.strokeStyle = c.ink3; ctx.lineWidth = 1;
        const tk = pop === 'bernoulli' && mode !== 'ci' ? [0, 0.25, 0.5, 0.75, 1] : W.ticks(x0, x1, Math.max(3, Math.round((Rr - L) / 60)));
        for (const t of tk) {
          if (t < x0 || t > x1) continue;
          const x = Math.round(X(t)) + 0.5; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x, y + 4); ctx.stroke();
          if (labels) ctx.fillText(String(parseFloat(t.toPrecision(4))), x, y + 6);
        }
      };

      if (mode === 'ci') {
        const top = 24, bot = h - 26;
        const rows = SHOW, rh = (bot - top) / rows;
        // true mean
        ctx.strokeStyle = c.ink; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(Math.round(X(mu())) + 0.5, top - 2); ctx.lineTo(Math.round(X(mu())) + 0.5, bot); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = c.ink2; ctx.font = '11px ' + c.font; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
        ctx.save(); ctx.beginPath(); ctx.rect(L, 0, Rr - L, h); ctx.clip();
        ivs.forEach((v, i) => {
          const y = top + (i + 0.5) * rh;
          const xa = X(v.m - v.half), xb = X(v.m + v.half), xm = X(v.m);
          ctx.strokeStyle = v.hit ? c.sc : c.red; ctx.fillStyle = v.hit ? c.sc : c.red;
          ctx.lineWidth = Math.max(1.5, Math.min(4, rh * 0.5));
          ctx.beginPath(); ctx.moveTo(xa, y); ctx.lineTo(xb, y); ctx.stroke();
          ctx.beginPath(); ctx.arc(xm, y, Math.max(1.6, Math.min(3, rh * 0.35)), 0, Math.PI * 2); ctx.fill();
        });
        ctx.restore();
        if (!ivs.length) { ctx.fillStyle = c.ink2; ctx.font = '13px ' + c.font; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText('Press "Draw 20 intervals"', w / 2, (top + bot) / 2); }
        axisFor(bot + 2); ticksAt(bot + 2, true);
        ctx.fillStyle = c.ink2; ctx.font = '11px ' + c.font; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
        ctx.fillText('true mean μ', Math.min(Math.max(X(mu()), L + 36), Rr - 36), 4);
        return;
      }

      // means mode: population panel above, histogram of sample means below
      const topPanel = { t: 10, b: Math.round(h * 0.30) };
      const lowPanel = { t: topPanel.b + 34, b: h - 24 };
      // population
      ctx.fillStyle = c.ink2; ctx.font = '11px ' + c.font; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText('Population (one value)', L, topPanel.t - 2);
      const pb = topPanel.b, ph = pb - topPanel.t - 12;
      ctx.fillStyle = c.sc; ctx.globalAlpha = 0.35; ctx.strokeStyle = c.sc; ctx.lineWidth = 1.8;
      if (pop === 'bernoulli') {
        const bw = (Rr - L) * 0.06;
        for (const [v, pr] of [[0, 1 - p], [1, p]]) { const bh = ph * pr / Math.max(p, 1 - p); ctx.fillRect(X(v) - bw / 2, pb - bh, bw, bh); }
        ctx.globalAlpha = 1;
        for (const [v, pr] of [[0, 1 - p], [1, p]]) { const bh = ph * pr / Math.max(p, 1 - p); ctx.strokeRect(X(v) - bw / 2, pb - bh, bw, bh); }
      } else {
        const f = POPS[pop].pdf, N = 160;
        let mx = 0; for (let i = 0; i <= N; i++) mx = Math.max(mx, f(x0 + (x1 - x0) * i / N));
        ctx.beginPath(); ctx.moveTo(X(x0), pb);
        for (let i = 0; i <= N; i++) { const x = x0 + (x1 - x0) * i / N; ctx.lineTo(X(x), pb - ph * f(x) / mx); }
        ctx.lineTo(X(x1), pb); ctx.closePath(); ctx.fill(); ctx.globalAlpha = 1;
        ctx.beginPath();
        for (let i = 0; i <= N; i++) { const x = x0 + (x1 - x0) * i / N; const y = pb - ph * f(x) / mx; if (i) ctx.lineTo(X(x), y); else ctx.moveTo(X(x), y); }
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
      axisFor(pb); ticksAt(pb, false);

      // histogram of means
      const lb = lowPanel.b, lh = lb - lowPanel.t - 4;
      ctx.fillStyle = c.ink2; ctx.font = '11px ' + c.font; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.fillText(`Means of samples of size ${n}`, L, lowPanel.t - 16);
      const sdm = sd() / Math.sqrt(n), m0 = mu();
      const bins = pop === 'bernoulli' ? Math.min(60, n + 1) : 44;
      const lo = pop === 'bernoulli' ? -0.5 / n : x0, hi = pop === 'bernoulli' ? 1 + 0.5 / n : x1;
      const useBins = pop === 'bernoulli' && n + 1 <= 60 ? n + 1 : (pop === 'bernoulli' ? 60 : bins);
      const bw = (hi - lo) / useBins;
      const cnt = new Array(useBins).fill(0);
      for (const m of means) { const k = Math.floor((m - lo) / bw); if (k >= 0 && k < useBins) cnt[k]++; }
      const dens = cnt.map((q) => (means.length ? q / (means.length * bw) : 0));
      const gpdf = (x) => Math.exp(-((x - m0) ** 2) / (2 * sdm * sdm)) / (sdm * Math.sqrt(2 * Math.PI));
      const ymax = Math.max(gpdf(m0), ...dens) * 1.08 || 1;
      const Y = (d) => lb - lh * d / ymax;
      ctx.save(); ctx.beginPath(); ctx.rect(L, lowPanel.t - 4, Rr - L, lb - lowPanel.t + 6); ctx.clip();
      ctx.fillStyle = c.sc2; ctx.globalAlpha = 0.45;
      dens.forEach((d, k) => { if (d > 0) ctx.fillRect(X(lo + k * bw), Y(d), Math.max(1, X(lo + (k + 1) * bw) - X(lo + k * bw) - 1), lb - Y(d)); });
      ctx.globalAlpha = 1;
      // theory curve
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2.2; ctx.beginPath();
      const N = 200;
      for (let i = 0; i <= N; i++) { const x = x0 + (x1 - x0) * i / N, y = Y(gpdf(x)); if (i) ctx.lineTo(X(x), y); else ctx.moveTo(X(x), y); }
      ctx.stroke();
      // true mean
      ctx.strokeStyle = c.ink; ctx.lineWidth = 1.3; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(Math.round(X(m0)) + 0.5, lowPanel.t - 2); ctx.lineTo(Math.round(X(m0)) + 0.5, lb); ctx.stroke(); ctx.setLineDash([]);
      // newest mean
      if (last != null) {
        ctx.strokeStyle = c.red; ctx.fillStyle = c.red; ctx.lineWidth = 2;
        const xl = clamp(X(last), L, Rr);
        ctx.beginPath(); ctx.moveTo(xl, lb); ctx.lineTo(xl, lb - 18); ctx.stroke();
        ctx.beginPath(); ctx.arc(xl, lb - 20, 3.5, 0, Math.PI * 2); ctx.fill();
      }
      ctx.restore();
      axisFor(lb); ticksAt(lb, true);
      // legend
      ctx.font = '11px ' + c.font; ctx.textAlign = 'right'; ctx.textBaseline = 'top';
      ctx.fillStyle = c.sc; ctx.fillText('curve: N(μ, σ²/n)', Rr, lowPanel.t - 16);
    }

    draw(mode === 'ci' ? 20 : 100);
  });
})();
