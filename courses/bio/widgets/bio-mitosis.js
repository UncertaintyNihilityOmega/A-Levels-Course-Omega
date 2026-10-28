/* widgets/bio-mitosis.js: the stages of the mitotic cell cycle (package P6).
   Attributes: data-cell = animal | plant (default animal); data-n = 2 | 4 | 6 (chromosomes in the cell, 2n; default 4);
   data-step = 0-6 (the step to start on, default 0).
   Seven steps: interphase G1, interphase G2, prophase, metaphase, anaphase, telophase, cytokinesis. The counts under the
   picture follow the chapter's counting rule (kept in counts()): G1 n chromosomes and no chromatids (one DNA molecule each);
   G2 to metaphase n chromosomes with 2n chromatids; anaphase and telophase 2n chromosomes in the whole cell; each daughter
   cell n chromosomes. A simplified drawing, not to scale; it says so on screen. */
(function () {
  'use strict';

  const STAGES = [
    { name: 'Interphase: G1', group: 'interphase' },
    { name: 'Interphase: G2', group: 'interphase' },
    { name: 'Prophase', group: 'mitosis' },
    { name: 'Metaphase', group: 'mitosis' },
    { name: 'Anaphase', group: 'mitosis' },
    { name: 'Telophase', group: 'mitosis' },
    { name: 'Cytokinesis', group: 'not part of mitosis' }
  ];
  const LENS = { 2: [1], 4: [1, 0.62], 6: [1, 0.78, 0.52] };

  function text(i, plant) {
    const sp = plant ? 'the poles of the cell (plant cells have no centrioles)' : 'the centrioles, which have moved to opposite poles';
    switch (i) {
      case 0: return 'The cell grows and does its normal job. The DNA is spread out as chromatin inside the nuclear envelope, so no chromosomes can be seen.' + (plant ? '' : ' There is one pair of centrioles.');
      case 1: return 'DNA was replicated in S phase, so each chromosome now has two identical sister chromatids, still uncoiled. The cell grows more and makes the proteins it needs for mitosis' + (plant ? '.' : ', and copies its centrioles.');
      case 2: return 'The chromosomes condense and show as two sister chromatids joined at a centromere. The nucleolus disappears, the nuclear envelope starts to break down and the spindle begins to grow from ' + sp + '.';
      case 3: return 'The nuclear envelope has gone and the spindle is complete. The chromosomes line up on the equator, each attached by its centromere to spindle fibres from both poles.';
      case 4: return 'The centromeres divide and the spindle fibres shorten, pulling the chromatids (now chromosomes) to opposite poles, centromere first. This needs energy from ATP.';
      case 5: return 'The chromosomes reach the poles and uncoil, a nuclear envelope forms round each group and the nucleolus reappears. The spindle breaks down and the cell begins to divide' + (plant ? ': Golgi vesicles start to form a cell plate.' : ': the cell surface membrane starts to pull inwards.');
      default: return plant
        ? 'Vesicles from the Golgi body fuse across the equator to make a cell plate, which grows outwards to the cell wall; cellulose is added to make a new wall. Each daughter cell is genetically identical to the parent cell and starts G1.'
        : 'A ring of protein filaments pulls the cell surface membrane in (a cleavage furrow) until the cell is pinched into two. Each daughter cell is genetically identical to the parent cell and starts G1.';
    }
  }

  // chromosome, chromatid and DNA counts for step i (0-6) in a cell with n chromosomes in G1
  function counts(i, n) {
    if (i === 0) return { chr: n, chd: 0, dna: 1, note: '' };
    if (i <= 3) return { chr: n, chd: 2 * n, dna: 2, note: '' };
    if (i <= 5) return { chr: 2 * n, chd: 0, dna: 2, note: ' (whole cell)' };
    return { chr: n, chd: 0, dna: 1, note: ' (each daughter cell)' };
  }
  function countLine(i, n) {
    const c = counts(i, n);
    return 'chromosomes: ' + c.chr + ' · chromatids: ' + c.chd + ' · DNA content: ' + c.dna + '× G1' + c.note;
  }
  function chroms(n) {
    const out = [];
    LENS[n].forEach(function (len, k) { out.push({ len: len, k: k, hom: 0 }); out.push({ len: len, k: k, hom: 1 }); });
    return out;
  }
  function pickN(v) { const x = parseInt(v, 10); return x === 2 || x === 4 || x === 6 ? x : 4; }

  // ---------- drawing helpers ----------
  function seg(ctx, x0, y0, x1, y1) { ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke(); }
  function disc(ctx, x, y, r) { ctx.beginPath(); ctx.arc(x, y, Math.max(0.5, r), 0, 2 * Math.PI); ctx.fill(); }
  function rrect(ctx, x, y, w, h, r) {
    ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
  }
  function animalPath(ctx, cx, cy, A, B, p) {
    ctx.beginPath();
    if (p <= 0.001) { ctx.ellipse(cx, cy, A, B, 0, 0, 2 * Math.PI); return; }
    const off = A * 0.5 * p, rx = A - off;
    ctx.ellipse(cx - off, cy, rx, B, 0, 0, 2 * Math.PI);
    ctx.moveTo(cx + off + rx, cy);
    ctx.ellipse(cx + off, cy, rx, B, 0, 0, 2 * Math.PI);
  }
  function thread(ctx, x, y, len, ang, amp, ph, lw, col, dbl) {
    const pts = [];
    for (let t = 0; t <= 20; t++) {
      const u = t / 20 - 0.5, px = u * len, py = amp * Math.sin(u * 9 + ph);
      pts.push([x + px * Math.cos(ang) - py * Math.sin(ang), y + px * Math.sin(ang) + py * Math.cos(ang)]);
    }
    ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    for (let d = 0; d < (dbl ? 2 : 1); d++) {
      ctx.beginPath();
      pts.forEach(function (p, j) { const o = d * lw * 1.7; if (j) ctx.lineTo(p[0] + o, p[1] + o); else ctx.moveTo(p[0] + o, p[1] + o); });
      ctx.stroke();
    }
  }
  // replicated chromosome: two chromatids crossing at the centromere (long axis at angle ang)
  function xchrom(ctx, x, y, L, ang, lw, col, ink) {
    ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.lineCap = 'round';
    [-0.3, 0.3].forEach(function (d) {
      const dx = Math.cos(ang + d) * L / 2, dy = Math.sin(ang + d) * L / 2;
      seg(ctx, x - dx, y - dy, x + dx, y + dy);
    });
    ctx.fillStyle = ink; disc(ctx, x, y, lw * 0.75);
  }
  // one separated chromatid pulled by its centromere towards a pole; the arms trail behind it
  function vchrom(ctx, x, y, L, dirx, lw, col, ink) {
    ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.lineCap = 'round';
    const a = 0.55;
    [-1, 1].forEach(function (s) { seg(ctx, x, y, x - dirx * L * Math.cos(a), y + s * L * Math.sin(a)); });
    ctx.fillStyle = ink; disc(ctx, x, y, lw * 0.75);
  }
  function centrioles(ctx, x, y, ink) {
    ctx.fillStyle = ink; ctx.strokeStyle = ink;
    ctx.fillRect(x - 7, y - 8, 14, 5);
    ctx.fillRect(x - 2.5, y - 1, 5, 12);
  }

  function geom(w, h) {
    const m = w < 440 ? 66 : 104;
    const A0 = Math.max(10, (w - 2 * m) / 2);
    const B = Math.max(10, Math.min(h / 2 - 14, A0 * 1.2));
    const A = Math.max(10, Math.min(A0, B * 1.45));
    return { cx: w / 2, cy: h / 2, A: A, B: B, m: m };
  }

  // draws step i; returns the labels to place [{side, text, x, y}]
  function drawStage(ctx, w, h, c, series, st) {
    const g = geom(w, h), cx = g.cx, cy = g.cy, A = g.A, B = g.B;
    const i = st.i, plant = st.cell === 'plant', n = st.n, ch = chroms(n), N = ch.length;
    const lw = Math.max(3, B * 0.045), labels = [];
    const colOf = function (o) { return series[o.k % series.length]; };
    const lab = function (side, t, x, y) { labels.push({ side: side, text: t, x: x, y: y }); };
    const tint = function (a) { ctx.globalAlpha = a; ctx.fillStyle = c.sc; };
    ctx.lineCap = 'round'; ctx.lineJoin = 'round';

    // ----- the cell -----
    const pinch = i === 5 ? 0.45 : (i === 6 ? 0.97 : 0);
    const Bq = i === 6 && !plant ? Math.min(B, A * 0.72) : B;
    const cellStroke = function () {
      ctx.setLineDash([]);
      if (plant) {
        const two = i === 6;
        const rects = two ? [[cx - A, cx - 1], [cx + 1, cx + A]] : [[cx - A, cx + A]];
        rects.forEach(function (r) {
          rrect(ctx, r[0], cy - B, r[1] - r[0], 2 * B, 10);
          ctx.fillStyle = c.card; ctx.globalAlpha = 1; ctx.fill();
          ctx.strokeStyle = c.ink2; ctx.lineWidth = 4; ctx.stroke();
          tint(0.07); ctx.fill(); ctx.globalAlpha = 1;
          rrect(ctx, r[0] + 5, cy - B + 5, r[1] - r[0] - 10, 2 * B - 10, 7);
          ctx.strokeStyle = c.ink3; ctx.lineWidth = 1.3; ctx.stroke();
        });
      } else {
        animalPath(ctx, cx, cy, A, Bq, pinch);
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 4; ctx.stroke();
        ctx.fillStyle = c.card; ctx.globalAlpha = 1; ctx.fill();
        tint(0.07); ctx.fill(); ctx.globalAlpha = 1;
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 1.6;
        animalPath(ctx, cx, cy, A, Bq, pinch);
        ctx.stroke();
      }
    };
    cellStroke();

    const nucleus = function (x, y, r, dashed, a) {
      ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI);
      ctx.globalAlpha = a == null ? 0.16 : a; ctx.fillStyle = c.sc; ctx.fill(); ctx.globalAlpha = 1;
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 2; ctx.setLineDash(dashed ? [5, 4] : []); ctx.stroke(); ctx.setLineDash([]);
    };
    const threads = function (x, y, r, dbl, wavy) {
      ch.forEach(function (o, k) {
        const a = k * 2.1;
        thread(ctx, x + 0.38 * r * Math.cos(a), y + 0.36 * r * Math.sin(a), 0.95 * r * (0.6 + 0.4 * o.len), a * 0.7, (wavy ? 0.16 : 0.1) * r, k, dbl ? 1.8 : 1.6, colOf(o), dbl);
      });
    };

    if (i <= 1) {
      const rn = B * 0.52;
      nucleus(cx, cy, rn, false);
      threads(cx, cy, rn, i === 1, true);
      ctx.fillStyle = c.ink2; disc(ctx, cx + rn * 0.5, cy - rn * 0.45, rn * 0.17);
      lab('L', 'envelope', cx - rn * 0.71, cy - rn * 0.71);
      lab('L', 'chromatin', cx - 0.3 * rn, cy + 0.2 * rn);
      lab('R', 'nucleolus', cx + rn * 0.5, cy - rn * 0.45);
      if (plant) lab('R', 'cell wall', cx + A, cy + B * 0.2);
      else {
        const px = cx + rn + 18;
        centrioles(ctx, px, cy + 6, c.ink2);
        if (i === 1) centrioles(ctx, px + 22, cy + 6, c.ink2);
        lab('R', 'centrioles', px, cy + 8);
      }
    } else if (i === 2) {
      const rn = B * 0.6;
      nucleus(cx, cy, rn, true, 0.1);
      const pole = A * 0.74;
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1;
      [-1, 1].forEach(function (s) {
        for (let f = -2; f <= 2; f++) seg(ctx, cx + s * pole, cy + f * 3, cx + s * pole * 0.52, cy + f * B * 0.2);
      });
      let first = null;
      ch.forEach(function (o, k) {
        const a = 2 * Math.PI * k / N + 0.4, x = cx + 0.33 * B * Math.cos(a), y = cy + 0.33 * B * Math.sin(a);
        ctx.globalAlpha = o.hom ? 0.7 : 1;
        xchrom(ctx, x, y, 0.42 * B * o.len + 6, a + 1.1, lw, colOf(o), c.ink2);
        ctx.globalAlpha = 1;
        if (k === 0) first = [x, y];
      });
      lab('L', 'envelope', cx - rn, cy + 2);
      lab('L', 'chromatids', first[0], first[1]);
      if (plant) lab('R', 'spindle', cx + pole * 0.76, cy - B * 0.2);
      else {
        [-1, 1].forEach(function (s) { centrioles(ctx, cx + s * pole, cy, c.ink2); });
        lab('R', 'centrioles', cx + pole, cy + 4);
        lab('R', 'spindle', cx + pole * 0.76, cy - B * 0.2);
      }
    } else if (i === 3 || i === 4) {
      const pole = A * 0.8, sp = Math.min(0.34 * B, 1.4 * B / Math.max(1, N - 1));
      const ana = i === 4;
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1;
      const pts = [];
      ch.forEach(function (o, k) {
        const y = cy + (k - (N - 1) / 2) * sp, st2 = 0;
        pts.push([o, y, st2]);
      });
      pts.forEach(function (p) {
        const y = p[1], x0 = cx + p[2];
        if (!ana) { seg(ctx, cx - pole, cy, x0, y); seg(ctx, cx + pole, cy, x0, y); }
        else { const d = A * 0.42; seg(ctx, cx - pole, cy, cx - d + p[2], y); seg(ctx, cx + pole, cy, cx + d + p[2], y); }
      });
      pts.forEach(function (p, k) {
        const o = p[0], y = p[1], L = Math.min(0.4 * B * o.len + 4, sp * 1.05);
        ctx.globalAlpha = o.hom ? 0.7 : 1;
        if (!ana) xchrom(ctx, cx + p[2], y, L, Math.PI / 2, lw, colOf(o), c.ink2);
        else {
          const d = A * 0.42;
          vchrom(ctx, cx - d + p[2], y, L * 0.7, -1, lw, colOf(o), c.ink2);
          vchrom(ctx, cx + d + p[2], y, L * 0.7, 1, lw, colOf(o), c.ink2);
        }
        ctx.globalAlpha = 1;
      });
      if (!plant) [-1, 1].forEach(function (s) { centrioles(ctx, cx + s * pole, cy, c.ink2); });
      const p0 = pts[0], p1 = pts[Math.min(1, pts.length - 1)];
      if (!ana) {
        lab('L', 'centromere', cx + p0[2], p0[1]);
        lab('L', 'chromatid', cx + p0[2] - 3, p0[1] - 0.2 * B);
      } else {
        const d = A * 0.42;
        lab('L', 'centromere', cx - d + p0[2], p0[1]);
        lab('L', 'chromosome', cx - d + p1[2] + 18, p1[1] + 8);
      }
      lab('R', 'spindle', cx + pole * 0.6, cy + (ana ? 0 : -0.5 * sp));
      lab('R', plant ? 'pole' : 'centrioles', cx + pole, cy);
    } else if (i === 5) {
      const rn = Math.min(B * 0.44, A * 0.3), nx = A * 0.52;
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.globalAlpha = 0.45;
      for (let f = -2; f <= 2; f++) seg(ctx, cx - nx + rn, cy + f * 4, cx + nx - rn, cy + f * 4);
      ctx.globalAlpha = 1;
      [-1, 1].forEach(function (s) {
        nucleus(cx + s * nx, cy, rn, false, 0.12);
        threads(cx + s * nx, cy, rn * 0.9, false, false);
        if (!plant) centrioles(ctx, cx + s * (nx + rn + 16), cy, c.ink2);
      });
      ctx.fillStyle = c.ink2; disc(ctx, cx + nx + rn * 0.45, cy - rn * 0.45, rn * 0.15);
      if (plant) {
        ctx.strokeStyle = c.ink2; ctx.lineWidth = 2.5; ctx.setLineDash([6, 4]);
        seg(ctx, cx, cy - B * 0.62, cx, cy + B * 0.62); ctx.setLineDash([]);
      }
      lab('L', 'envelope', cx - nx - rn * 0.7, cy - rn * 0.7);
      lab('L', 'chromatin', cx - nx, cy + rn * 0.2);
      lab('R', 'nucleolus', cx + nx + rn * 0.45, cy - rn * 0.45);
      if (plant) lab('R', 'cell plate', cx, cy + B * 0.3);
      else lab('R', 'furrow', cx + 1, cy - B * 0.9);
    } else {
      const rn = Math.min(B * 0.44, A * 0.3), nx = A * 0.52;
      [-1, 1].forEach(function (s) {
        nucleus(cx + s * nx, cy, rn, false, 0.12);
        threads(cx + s * nx, cy, rn * 0.9, false, true);
        ctx.fillStyle = c.ink2; disc(ctx, cx + s * nx + rn * 0.4, cy - rn * 0.4, rn * 0.15);
        if (!plant) centrioles(ctx, cx + s * (nx + rn + 16), cy + 4, c.ink2);
      });
      lab('L', 'nucleus', cx - nx - rn * 0.7, cy - rn * 0.7);
      lab('L', 'chromatin', cx - nx, cy + rn * 0.2);
      lab('R', plant ? 'new wall' : 'furrow', cx, plant ? cy + B * 0.4 : cy - B * 0.1);
      if (plant) lab('R', 'cell wall', cx + A, cy - B * 0.2);
      else lab('R', 'centrioles', cx + nx + rn + 16, cy + 6);
    }
    return labels;
  }

  function placeLabels(ctx, w, h, c, labels) {
    ctx.font = '12px ' + c.font; ctx.textBaseline = 'middle';
    const cnt = { L: 0, R: 0 }, tot = { L: 0, R: 0 };
    labels.forEach(function (l) { tot[l.side]++; });
    labels.forEach(function (l) {
      const k = cnt[l.side]++, t = tot[l.side];
      const y = t === 1 ? h * 0.5 : h * (k === 0 ? 0.28 : 0.72) + (t > 2 ? (k - 1) * 0 : 0);
      const left = l.side === 'L', tx = left ? 6 : w - 6;
      const tw = (ctx.measureText(l.text) || {}).width || 60;
      ctx.textAlign = left ? 'left' : 'right';
      ctx.lineWidth = 4; ctx.strokeStyle = c.card; ctx.lineJoin = 'round';
      ctx.strokeText(l.text, tx, y); ctx.fillStyle = c.ink; ctx.fillText(l.text, tx, y);
      ctx.strokeStyle = c.ink2; ctx.lineWidth = 1; ctx.setLineDash([]);
      seg(ctx, left ? tx + tw + 4 : tx - tw - 4, y, l.x, l.y);
      ctx.fillStyle = c.ink2; disc(ctx, l.x, l.y, 2.2);
    });
  }

  function describe(st) {
    const s = STAGES[st.i], c = counts(st.i, st.n);
    return (st.cell === 'plant' ? 'Plant' : 'Animal') + ' cell, ' + s.name.toLowerCase() + ' (' + s.group + '). ' +
      text(st.i, st.cell === 'plant') + ' Counts: ' + countLine(st.i, st.n) + '.';
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { counts: counts, countLine: countLine, chroms: chroms, STAGES: STAGES, pickN: pickN };
  if (typeof W === 'undefined') return;

  W.register('bio-mitosis', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'The stages of mitosis', 'A simplified drawing, not to scale');
    const st = { i: 0, cell: opts.cell === 'plant' ? 'plant' : 'animal', n: pickN(opts.n) };

    // ----- controls -----
    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Type of cell' });
    const tb = {};
    ['animal', 'plant'].forEach(function (k) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': k === st.cell ? 'true' : 'false', text: k === 'animal' ? 'Animal cell' : 'Plant cell' });
      b.onclick = function () { st.cell = k; Object.keys(tb).forEach(function (j) { tb[j].setAttribute('aria-pressed', j === k ? 'true' : 'false'); }); refresh(); };
      tb[k] = b; tabs.appendChild(b);
    });
    const sel = W.h('select', { 'aria-label': 'Number of chromosomes in the cell' },
      W.h('option', { value: '2', text: '2 chromosomes' }), W.h('option', { value: '4', text: '4 chromosomes' }), W.h('option', { value: '6', text: '6 chromosomes' }));
    sel.value = String(st.n);
    sel.onchange = function () { st.n = pickN(sel.value); refresh(); };
    const playBtn = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Play' });
    body.appendChild(W.h('div', { class: 'w-row' }, tabs, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Chromosomes (2n)' }), sel), playBtn));

    const cv = W.canvas(body, {
      height: (el.clientWidth || 600) < 480 ? 250 : 290, label: 'Drawing of a dividing cell', describe: function () { return describe(st); },
      draw: function (ctx, w, h, c) {
        if (!(w > 0) || !(h > 0)) return;
        const pal = (W.palette && W.palette(el)) || {};
        const series = (pal.series && pal.series.length) ? pal.series : [c.sc, c.sc2, c.red, c.ok, c.ink2, c.ink3];
        ctx.save();
        const labels = drawStage(ctx, w, h, c, series, st);
        ctx.globalAlpha = 1;
        placeLabels(ctx, w, h, c, labels);
        ctx.restore();
      }
    });

    const stepper = W.stepper(body, { steps: STAGES.length, labels: STAGES.map(function (s) { return s.name; }), onstep: function (i) { st.i = i; refresh(); } });

    if (stepper.el && !stepper.el.parentNode) body.appendChild(stepper.el);
    const head = W.h('strong', { class: 'w-lab' });
    const para = W.h('div');
    const cnts = W.h('div', { class: 'w-stat hi' });
    const cap = W.h('div', { class: 'w-note', 'aria-live': 'polite' }, head, para, cnts);
    body.appendChild(cap);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Same colour and length: a pair of homologous chromosomes (one from each parent). Each chromosome is one DNA molecule until S phase copies it. The drawing is simplified and not to scale.' }));

    function refresh() {
      const s = STAGES[st.i];
      head.textContent = 'Step ' + (st.i + 1) + ': ' + s.name + ' (' + s.group + ')';
      para.textContent = text(st.i, st.cell === 'plant');
      cnts.textContent = countLine(st.i, st.n);
      cv.redraw();
    }

    // ----- Play -----
    let playing = false, lastT = 0;
    const setPlaying = function (p) { playing = p; playBtn.textContent = p ? 'Pause' : 'Play'; };
    const anim = W.animate(function () {
      const now = Date.now();
      if (now - lastT < 1800) return true;
      lastT = now;
      if (stepper.i < STAGES.length - 1) { stepper.go(stepper.i + 1); return true; }
      setPlaying(false);
      return false;
    }, { still: function () { if (stepper.i < STAGES.length - 1) stepper.go(stepper.i + 1); } });
    playBtn.onclick = function () {
      if (playing) { anim.stop(); setPlaying(false); return; }
      if (stepper.i >= STAGES.length - 1) stepper.go(0);
      if (W.reducedMotion && W.reducedMotion()) { anim.start(); return; }
      lastT = Date.now(); setPlaying(true); anim.start();
    };

    stepper.go(Math.min(STAGES.length - 1, Math.max(0, parseInt(opts.step, 10) || 0)));
  });
})();
