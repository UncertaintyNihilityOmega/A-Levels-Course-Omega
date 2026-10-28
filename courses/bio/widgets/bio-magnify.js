/* widgets/bio-magnify.js: magnification calculator (data-mode="mia") and eyepiece graticule calibration
   (data-mode="graticule"). Used in bio.microscopy. Facts: M = I/A, 1 mm = 1000 um, 1 um = 1000 nm,
   stage micrometer division = 10 um. Simplified model: the graticule is always drawn 0-100 units. */
(function () {
  'use strict';

  const UM = { mm: 1000, 'µm': 1, nm: 0.001 };      // micrometres in one unit
  const UNITS = ['mm', 'µm', 'nm'];
  const SUP = { '-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' };
  const NAMES = { I: 'the image size I', A: 'the actual size A', M: 'the magnification M' };

  // small DOM helper: class, style object, text, on* handlers, everything else as attributes
  function E(tag, props, ...kids) {
    const n = document.createElement(tag);
    for (const k in (props || {})) {
      const v = props[k];
      if (v == null) continue;
      if (k === 'class') n.className = v;
      else if (k === 'style') Object.assign(n.style, v);
      else if (k === 'text') n.textContent = v;
      else if (k.slice(0, 2) === 'on') n[k] = v;
      else n.setAttribute(k, v);
    }
    kids.forEach(c => { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return n;
  }

  function group(s) {
    const p = s.split('.');
    if (p[0].length >= 5) p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    return p.join('.');
  }

  // n significant figures, no trailing zeros, thin space between thousands, standard form for very large/small
  function sf(x, n) {
    n = n || 3;
    if (!isFinite(x)) return '–';
    if (x === 0) return '0';
    const e = Math.floor(Math.log10(Math.abs(x)));
    if (e >= 7 || e < -4) {
      const t = x.toExponential(n - 1).split('e');
      const m = String(Number(t[0]));
      return m + ' × 10' + String(parseInt(t[1], 10)).split('').map(c => SUP[c] || c).join('');
    }
    return group(String(Number(x.toPrecision(n))));
  }

  function parse(s) {
    const t = String(s == null ? '' : s).replace(/[\s ]/g, '').replace(',', '.');
    if (t === '') return NaN;
    return Number(t);
  }

  // ---------------------------------------------------------------------------------------------------
  function mia(el) {
    const { body } = W.frame(el, 'Magnification calculator', 'M = I ÷ A: choose what to find, enter the other two');
    const st = { find: 'M', I: '35', Iu: 'mm', A: '7', Au: 'µm', M: '5000' };
    const inputs = {}, selects = {}, labels = {};

    const tabs = E('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Quantity to find' });
    const tabBtns = {};
    [['M', 'Find M'], ['A', 'Find A'], ['I', 'Find I']].forEach(([k, txt]) => {
      const b = E('button', { type: 'button', class: 'w-tab', 'aria-pressed': k === st.find ? 'true' : 'false', text: txt, onclick: () => setFind(k, true) });
      tabBtns[k] = b;
      tabs.appendChild(b);
    });
    body.appendChild(E('div', { class: 'w-row' }, tabs));

    function mkField(k, text, withUnit) {
      const lab = E('label', { class: 'w-ctl' });
      labels[k] = E('span', { class: 'w-lab', text });
      const inp = E('input', { type: 'text', inputmode: 'decimal', autocomplete: 'off', style: { width: '120px' } });
      inp.value = st[k];
      inp.oninput = () => { st[k] = inp.value; update(); };
      inputs[k] = inp;
      lab.appendChild(labels[k]);
      lab.appendChild(inp);
      const row = [lab];
      if (withUnit) {
        const sel = E('select', { 'aria-label': 'Unit of ' + NAMES[k], style: { width: '88px' } });
        UNITS.forEach(u => sel.appendChild(E('option', { value: u, text: u })));
        sel.value = st[k + 'u'];
        sel.onchange = () => { st[k + 'u'] = sel.value; update(); };
        selects[k] = sel;
        row.push(sel);
      } else {
        row.push(E('span', { class: 'w-lab', text: '(a number: written ×, no unit)' }));
      }
      body.appendChild(E('div', { class: 'w-row', style: { alignItems: 'flex-end' } }, ...row));
    }
    mkField('I', 'Image size I', true);
    mkField('A', 'Actual size A', true);
    mkField('M', 'Magnification M (×)', false);

    const err = E('div', { class: 'w-err', 'aria-live': 'polite' });
    body.appendChild(err);
    const ans = W.stat('Answer', true);
    body.appendChild(E('div', { class: 'w-out' }, ans.el));
    const work = E('div', { class: 'w-note', 'aria-live': 'polite' });
    body.appendChild(work);
    body.appendChild(E('div', { class: 'w-note', text: 'Try each tab. Always convert I and A to the same unit first, then divide. A real red blood cell (about 7 µm) drawn 35 mm wide gives × 5000.' }));

    function setFind(k, focus) {
      st.find = k;
      Object.keys(tabBtns).forEach(t => tabBtns[t].setAttribute('aria-pressed', t === k ? 'true' : 'false'));
      if (focus) tabBtns[k].focus();
      update();
    }

    function line(txt) { work.appendChild(E('div', { text: txt })); }
    function conv(name, v, u) {
      if (u === 'µm') return name + ' = ' + sf(v, 6) + ' µm (already in µm)';
      return name + ' = ' + sf(v, 6) + ' ' + u + (u === 'mm' ? ' × 1000 = ' : ' ÷ 1000 = ') + sf(v * UM[u], 6) + ' µm';
    }

    function update() {
      work.textContent = '';
      err.textContent = '';
      const f = st.find;
      const vals = {};
      let bad = '';
      ['I', 'A', 'M'].forEach(k => {
        inputs[k].readOnly = (k === f);
        labels[k].textContent = ({ I: 'Image size I', A: 'Actual size A', M: 'Magnification M (×)' })[k] + (k === f ? ' (calculated)' : '');
        if (k === f || bad) return;
        const v = parse(inputs[k].value);
        if (isNaN(v)) bad = 'Enter a number for ' + NAMES[k] + ' (for example 35 or 0.5).';
        else if (v === 0) bad = 'The value of ' + NAMES[k] + ' cannot be zero.';
        else if (v < 0) bad = 'The value of ' + NAMES[k] + ' cannot be negative.';
        else if (!isFinite(v)) bad = 'That number for ' + NAMES[k] + ' is too large.';
        vals[k] = v;
      });
      if (bad) {
        err.textContent = bad;
        ans.set('–');
        inputs[f].value = '';
        return;
      }
      let result;
      if (f === 'M') {
        const iu = vals.I * UM[st.Iu], au = vals.A * UM[st.Au];
        const m = iu / au;
        line('1. Same unit (µm): ' + conv('I', vals.I, st.Iu) + '; ' + conv('A', vals.A, st.Au));
        line('2. M = I ÷ A = ' + sf(iu, 6) + ' ÷ ' + sf(au, 6) + ' = ' + sf(m, 6));
        line('3. M = × ' + sf(m));
        result = '× ' + sf(m);
        inputs.M.value = sf(m);
        if (m > 1e6) line('Check: a magnification over a million is very unlikely. Are I and A the right way round, and are the units right?');
        else if (m < 1) line('Check: M is below 1, which would be a reduction. Is the image really smaller than the object?');
      } else if (f === 'A') {
        const iu = vals.I * UM[st.Iu];
        const a = iu / vals.M;
        const out = a / UM[st.Au];
        line('1. Image in µm: ' + conv('I', vals.I, st.Iu));
        line('2. A = I ÷ M = ' + sf(iu, 6) + ' ÷ ' + sf(vals.M, 6) + ' = ' + sf(a, 6) + ' µm');
        if (st.Au !== 'µm') line('3. In ' + st.Au + ': ' + sf(a, 6) + ' µm ' + (st.Au === 'mm' ? '÷ 1000' : '× 1000') + ' = ' + sf(out, 6) + ' ' + st.Au);
        line((st.Au !== 'µm' ? '4' : '3') + '. A = ' + sf(out) + ' ' + st.Au);
        result = sf(out) + ' ' + st.Au;
        inputs.A.value = sf(out);
      } else {
        const au = vals.A * UM[st.Au];
        const i = vals.M * au;
        const out = i / UM[st.Iu];
        line('1. Actual size in µm: ' + conv('A', vals.A, st.Au));
        line('2. I = M × A = ' + sf(vals.M, 6) + ' × ' + sf(au, 6) + ' = ' + sf(i, 6) + ' µm');
        if (st.Iu !== 'µm') line('3. In ' + st.Iu + ': ' + sf(i, 6) + ' µm ' + (st.Iu === 'mm' ? '÷ 1000' : '× 1000') + ' = ' + sf(out, 6) + ' ' + st.Iu);
        line((st.Iu !== 'µm' ? '4' : '3') + '. I = ' + sf(out) + ' ' + st.Iu);
        result = sf(out) + ' ' + st.Iu;
        inputs.I.value = sf(out);
      }
      ans.set(result);
    }
    update();
  }

  // ---------------------------------------------------------------------------------------------------
  function grat(el, opts) {
    const { body } = W.frame(el, 'Eyepiece graticule calibration',
      'Line up the zeros, read the matching marks, then measure a cell');
    // Simplified model: at x10, one stage division (10 µm) is 1 eyepiece unit wide; at x40, 4 units wide.
    const S = { obj: (opts && String(opts.obj) === '40') ? 40 : 10, off: 6.3, cell: 22, ppu: 0, busy: false };
    const per = o => (o === 10 ? 1 : 4);
    const calib = o => 10 / per(o);
    const aligned = () => Math.abs(S.off) < 0.2;

    const tabs = E('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Objective lens' });
    const btns = {};
    [10, 40].forEach(o => {
      const b = E('button', { type: 'button', class: 'w-tab', 'aria-pressed': o === S.obj ? 'true' : 'false', text: 'Objective ×' + o,
        onclick: () => { S.obj = o; Object.keys(btns).forEach(k => btns[k].setAttribute('aria-pressed', Number(k) === o ? 'true' : 'false')); update(); } });
      btns[o] = b;
      tabs.appendChild(b);
    });
    body.appendChild(E('div', { class: 'w-row' }, tabs));

    const c = W.canvas(body, {
      height: 236,
      label: 'Eyepiece graticule laid over a stage micrometer, with a cell',
      describe: () => {
        const p = per(S.obj);
        let t = 'Graticule marked 0 to 100 units over a stage micrometer at objective ×' + S.obj +
          '. One stage division is ' + p + ' eyepiece unit' + (p > 1 ? 's' : '') + ' wide. ';
        t += aligned() ? 'The zero marks line up, and 10 stage divisions match ' + (10 * p) + ' eyepiece units. '
          : 'The zero of the stage scale is ' + Math.abs(S.off).toFixed(1) + ' units to the ' + (S.off > 0 ? 'right' : 'left') + ' of the graticule zero. ';
        return t + 'The cell is ' + S.cell + ' eyepiece units long.';
      },
      draw: (ctx, w, h, C) => {
        if (!(w > 0) || !(h > 0)) return;
        const padL = 14, padR = 14, span = w - padL - padR;
        if (span < 40) return;
        const ppu = span / 100;
        S.ppu = ppu;
        const X = u => padL + u * ppu;
        const p = per(S.obj);
        ctx.clearRect(0, 0, w, h);
        ctx.font = '11px ' + (C.font || 'sans-serif');
        ctx.textBaseline = 'alphabetic';
        const mw = t => { const m = ctx.measureText(t); return m && m.width ? m.width : t.length * 6; };
        const fit = (...opts) => { for (const t of opts) if (mw(t) <= span) return t; return opts[opts.length - 1]; };
        // eyepiece graticule (fixed)
        const yG = 58;
        ctx.fillStyle = C.ink2; ctx.textAlign = 'left';
        ctx.fillText(fit('Eyepiece graticule (fixed in the eyepiece)', 'Eyepiece graticule (fixed)'), padL, 13);
        ctx.strokeStyle = C.ink; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.moveTo(X(0), yG); ctx.lineTo(X(100), yG); ctx.stroke();
        const stepNum = ppu * 10 < 26 ? 20 : 10;
        for (let u = 0; u <= 100; u++) {
          const major = u % 10 === 0, mid = u % 5 === 0;
          if (!major && !mid && ppu < 3) continue;
          const t = major ? 12 : (mid ? 8 : 4);
          ctx.beginPath(); ctx.moveTo(X(u), yG); ctx.lineTo(X(u), yG - t); ctx.stroke();
          if (u % stepNum === 0) { ctx.textAlign = 'center'; ctx.fillStyle = C.ink; ctx.fillText(String(u), X(u), yG - 17); }
        }
        // the cell (drawn between the scales, length in eyepiece units)
        const cy = 106, c0 = 8, c1 = Math.min(100, c0 + S.cell);
        ctx.save();
        ctx.beginPath();
        ctx.ellipse((X(c0) + X(c1)) / 2, cy, Math.max(1, (X(c1) - X(c0)) / 2), 20, 0, 0, Math.PI * 2);
        ctx.globalAlpha = 0.22; ctx.fillStyle = C.sc2; ctx.fill();
        ctx.globalAlpha = 1; ctx.strokeStyle = C.sc2; ctx.lineWidth = 2; ctx.stroke();
        ctx.restore();
        ctx.fillStyle = C.ink2; ctx.textAlign = 'center';
        ctx.fillText('cell: ' + S.cell + (span > 300 ? ' eyepiece units' : ' units'), (X(c0) + X(c1)) / 2, cy + 36);
        // stage micrometer (moves with the slide)
        const yS = 176;
        ctx.textAlign = 'left'; ctx.fillStyle = C.ink2;
        ctx.fillText(fit('Stage micrometer (drag it, or use the slider): 1 division = 10 µm', 'Stage micrometer: 1 division = 10 µm', 'Stage: 1 division = 10 µm'), padL, 229);
        const x0 = S.off;
        ctx.strokeStyle = C.sc; ctx.lineWidth = 1.2;
        const xa = Math.max(0, x0), xb = Math.min(100, x0 + 100 * p);
        if (xb > xa) { ctx.beginPath(); ctx.moveTo(X(xa), yS); ctx.lineTo(X(xb), yS); ctx.stroke(); }
        const dpx = p * ppu;                         // pixels per stage division
        const stepD = dpx * 5 < 26 ? 20 : (dpx < 12 ? 10 : 5);
        for (let k = 0; k <= 100; k++) {
          const u = x0 + k * p;
          if (u < 0 || u > 100) continue;
          const maj = k % 10 === 0;
          if (!maj && dpx < 3) continue;
          ctx.beginPath(); ctx.moveTo(X(u), yS); ctx.lineTo(X(u), yS + (maj ? 14 : 9)); ctx.stroke();
          if (k % stepD === 0) { ctx.textAlign = 'center'; ctx.fillStyle = C.sc; ctx.fillText(String(k), X(u), yS + 27); }
        }
        // guides when the zeros are lined up
        if (aligned()) {
          ctx.save();
          ctx.strokeStyle = C.red; ctx.lineWidth = 1.2; ctx.setLineDash([4, 3]);
          [0, 10 * p].forEach(u => {
            const ux = x0 + u;
            ctx.beginPath(); ctx.moveTo(X(u), yG + 2); ctx.lineTo(X(u), yS); ctx.stroke();
          });
          ctx.restore();
          ctx.fillStyle = C.red; ctx.textAlign = 'right';
          ctx.fillText('10 divisions = ' + (10 * p) + ' units', X(10 * p) - 6, 144);
        }
      }
    });

    const sl = W.sliderNum({ label: 'Move the stage scale (eyepiece units)', min: -12, max: 12, step: 0.05, value: S.off,
      oninput: () => { if (S.busy) return; S.off = Number(sl.get()); update(); } });
    body.appendChild(sl.el);
    const csl = W.sliderNum({ label: 'Cell length (eyepiece units)', min: 1, max: 80, step: 1, value: S.cell,
      oninput: () => { S.cell = Math.round(Number(csl.get())) || 1; update(); } });
    body.appendChild(csl.el);

    const rd = W.readout([['obj', 'Objective'], ['state', 'Stage scale'], ['cal', 'One eyepiece unit'], ['cell', 'Length of the cell']]);
    body.appendChild(rd.el);
    body.appendChild(E('div', { class: 'w-note', text: 'Change the objective and watch the calibration change: you must recalibrate for every objective. This is a simplified model of one microscope.' }));

    W.drag(c.wrap, {
      hit: (x, y) => (y > 130 ? { sx: x, s0: S.off } : null),
      move: (t, x) => {
        if (!(S.ppu > 0)) return;
        const v = Math.max(-12, Math.min(12, t.s0 + (x - t.sx) / S.ppu));
        S.off = Math.round(v * 20) / 20;
        S.busy = true; sl.set(S.off); S.busy = false;
        update();
      },
      end: () => {}
    });

    function update() {
      const p = per(S.obj);
      rd.set('obj', '× ' + S.obj + ' (total × ' + (S.obj * 10) + ' with a × 10 eyepiece)');
      if (aligned()) {
        rd.set('state', 'zeros lined up: 10 divisions (100 µm) match ' + (10 * p) + ' eyepiece units');
        rd.set('cal', '100 µm ÷ ' + (10 * p) + ' = ' + sf(calib(S.obj)) + ' µm');
        rd.set('cell', S.cell + ' × ' + sf(calib(S.obj)) + ' µm = ' + sf(S.cell * calib(S.obj)) + ' µm');
      } else {
        rd.set('state', 'zero is ' + Math.abs(S.off).toFixed(1) + ' units to the ' + (S.off > 0 ? 'right' : 'left') + ' of the graticule zero: move it until the zeros line up');
        rd.set('cal', '– (line up the zeros first)');
        rd.set('cell', '–');
      }
      c.redraw();
    }
    update();
  }

  W.register('bio-magnify', function (el, opts) {
    try {
      if (opts && opts.mode === 'graticule') grat(el, opts);
      else mia(el);
    } catch (e) {
      el.textContent = 'This tool could not start.';
    }
  });
})();
