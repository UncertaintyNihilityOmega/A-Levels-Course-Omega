/* hist-chart: a line or bar chart of historical statistics, with a table and a source line.
   <div class="widget" data-w="hist-chart" data-title="Russian coal output, 1860-1900" data-unit="million tonnes"
        data-type="line" data-series="Coal: 1860=0.3, 1880=3.28, 1900=15.88" data-source="Statesman's Year-Book, 1913"></div>
   Series: "Name: key=value, key=value ;; Second name: key=value, ..." (at most two series, one axis).
   A key is a year ("1880") or a label ("1880-4"). Lines place all-year keys in proportion to the year. */
(function () {
  'use strict';

  const MAX_SERIES = 2;

  // Parses data-series. Returns {series: [{name, vals: {key: number}}], keys: [], numeric: bool, problems: []}
  function parseSeries(raw) {
    const problems = [];
    const series = [];
    const parts = String(raw == null ? '' : raw).split(';;').map(function (s) { return s.trim(); }).filter(Boolean);
    parts.forEach(function (part, i) {
      const colon = part.indexOf(':');
      if (colon < 1) {
        problems.push('Series ' + (i + 1) + ' needs a name, a colon and values, like "Coal: 1880=3.3, 1900=15.9".');
        return;
      }
      const name = part.slice(0, colon).trim();
      const vals = {};
      const order = [];
      part.slice(colon + 1).split(',').forEach(function (pair) {
        const p = pair.trim();
        if (!p) return;
        const eq = p.indexOf('=');
        const key = eq > 0 ? p.slice(0, eq).trim() : '';
        const numText = eq > 0 ? p.slice(eq + 1).trim() : '';
        const num = numText === '' ? NaN : Number(numText);
        if (!key || !isFinite(num)) {
          problems.push('In "' + name + '", "' + p.slice(0, 30) + '" is not key=number.');
          return;
        }
        if (!Object.prototype.hasOwnProperty.call(vals, key)) order.push(key);
        vals[key] = num;
      });
      if (!order.length) {
        problems.push('"' + name + '" has no usable values.');
        return;
      }
      if (series.length >= MAX_SERIES) {
        problems.push('Only two series are shown; "' + name + '" was left out.');
        return;
      }
      series.push({ name: name, vals: vals, order: order });
    });
    // categories: union of keys in order of first appearance; sorted when all are years
    const keys = [];
    series.forEach(function (s) { s.order.forEach(function (k) { if (keys.indexOf(k) < 0) keys.push(k); }); });
    const numeric = keys.length > 0 && keys.every(function (k) { return /^-?\d{1,4}$/.test(k); });
    if (numeric) keys.sort(function (a, b) { return Number(a) - Number(b); });
    return { series: series, keys: keys, numeric: numeric, problems: problems };
  }

  // Tick values for the range [lo, hi]; about n intervals, steps of 1, 2, 2.5 or 5 times a power of ten
  function niceTicks(lo, hi, n) {
    if (!(isFinite(lo) && isFinite(hi))) return { ticks: [0, 1], lo: 0, hi: 1, step: 1 };
    if (hi <= lo) hi = lo + (Math.abs(lo) || 1);
    const rough = (hi - lo) / Math.max(1, n);
    const pow = Math.pow(10, Math.floor(Math.log10(rough)));
    let step = pow;
    [1, 2, 2.5, 5, 10].some(function (m) { step = m * pow; return step >= rough; });
    const a = Math.floor(lo / step + 1e-9) * step;
    const b = Math.ceil(hi / step - 1e-9) * step;
    const ticks = [];
    for (let i = 0, v = a; v <= b + step * 1e-6 && i < 60; i++, v = a + i * step) ticks.push(Math.round(v / step * 1e6) / 1e6 * step);
    return { ticks: ticks, lo: a, hi: b, step: step };
  }

  function decimals(vals) {
    let d = 0;
    vals.forEach(function (v) {
      const s = String(v);
      const i = s.indexOf('.');
      if (i >= 0 && s.indexOf('e') < 0) d = Math.max(d, Math.min(3, s.length - i - 1));
    });
    return d;
  }

  function fmtNum(v, d) {
    if (v == null || !isFinite(v)) return 'no figure';
    return v.toLocaleString('en-GB', { minimumFractionDigits: d, maximumFractionDigits: d });
  }

  // Plain-words trend for one series: first and last values
  function trendWords(s, keys, d) {
    const have = keys.filter(function (k) { return s.vals[k] != null; });
    if (!have.length) return s.name + ': no figures.';
    const first = have[0];
    const last = have[have.length - 1];
    const a = s.vals[first];
    const b = s.vals[last];
    if (have.length === 1) return s.name + ': one figure, ' + fmtNum(a, d) + ' in ' + first + '.';
    const dir = b > a ? 'rises' : (b < a ? 'falls' : 'stays level');
    let t = s.name + ' ' + dir + ' from ' + fmtNum(a, d) + ' in ' + first + ' to ' + fmtNum(b, d) + ' in ' + last;
    if (a > 0 && b > a) t += ' (about ' + (Math.round(b / a * 10) / 10) + ' times as much)';
    return t + '.';
  }

  W.register('hist-chart', function (el, opts) {
    function attr(name) {
      const v = el.getAttribute('data-' + name);
      if (v != null) return v;
      return opts && (opts[name] != null ? opts[name] : opts['data-' + name]);
    }
    const title = String(attr('title') || 'Chart of historical statistics');
    const unit = String(attr('unit') || '');
    const type = String(attr('type') || 'line').toLowerCase() === 'bar' ? 'bar' : 'line';
    const source = String(attr('source') || '').trim();
    const parsed = parseSeries(attr('series'));
    const series = parsed.series;
    const keys = parsed.keys;

    const frame = W.frame(el, title, unit ? 'Vertical axis: ' + unit + '.' : 'Historical statistics');
    const body = frame.body;

    function mk(tag, props) {
      const n = document.createElement(tag);
      const p = props || {};
      Object.keys(p).forEach(function (k) {
        if (k === 'text') n.textContent = p[k];
        else if (k === 'style') Object.assign(n.style, p[k]);
        else if (k === 'class') n.className = p[k];
        else if (k.slice(0, 2) === 'on') n[k] = p[k];
        else n.setAttribute(k, p[k]);
      });
      for (let i = 2; i < arguments.length; i++) {
        const c = arguments[i];
        if (c) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
      }
      return n;
    }

    if (!series.length || !keys.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'This chart needs data. Write it in data-series as: Name: 1880=3.3, 1890=6.0 ;; Second name: 1880=1.2, 1890=2.5' }));
      if (parsed.problems.length) body.appendChild(mk('p', { class: 'w-err', text: parsed.problems.slice(0, 3).join(' ') }));
      return;
    }
    if (parsed.problems.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: parsed.problems.slice(0, 2).join(' ') }));
    }
    if (!source) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'This chart has no data-source. Add the source of the figures.' }));
    }

    const allVals = [];
    series.forEach(function (s) { keys.forEach(function (k) { if (s.vals[k] != null) allVals.push(s.vals[k]); }); });
    const dec = decimals(allVals);
    let sel = keys.length - 1;
    let geo = null; // layout of the last drawing, for pointer input

    // Legend (names with a symbol, so colour is not the only cue)
    const legend = mk('div', { class: 'w-row', style: { gap: '14px', alignItems: 'center' } });
    series.forEach(function (s, i) {
      const sym = type === 'bar' ? (i === 0 ? '■' : '□') : (i === 0 ? '● ─' : '○ - -');
      legend.appendChild(mk('span', { class: 'w-lab', style: { color: 'var(--ink-2)' } },
        mk('span', { 'aria-hidden': 'true', style: { color: i === 0 ? 'var(--sc)' : 'var(--sc2)', marginRight: '4px' }, text: sym }), s.name));
    });
    body.appendChild(legend);

    function describe() {
      let t = (type === 'bar' ? 'Bar chart' : 'Line chart') + ': ' + title + (unit ? ' (' + unit + ')' : '') + '. ';
      series.forEach(function (s) { t += trendWords(s, keys, dec) + ' '; });
      return t.trim();
    }

    const c = W.canvas(body, {
      height: 260,
      label: title + (unit ? ' (' + unit + ')' : ''),
      describe: describe,
      draw: function (ctx, w, h, col) {
        ctx.clearRect(0, 0, w, h);
        geo = null;
        if (!(w > 60 && h > 60)) return;
        const padL = 50, padR = 16, padT = 14, padB = 30;
        const pw = w - padL - padR;
        const ph = h - padT - padB;
        if (!(pw > 20 && ph > 20)) return;
        let lo = Math.min.apply(null, allVals);
        let hi = Math.max.apply(null, allVals);
        if (lo >= 0 && (type === 'bar' || lo <= 0.5 * hi)) lo = 0;
        if (hi === lo) hi = lo + (Math.abs(lo) || 1);
        const nt = niceTicks(lo, hi, 4);
        const y0 = nt.lo, y1 = nt.hi;
        const Y = function (v) { return padT + ph - (v - y0) / (y1 - y0) * ph; };
        const n = keys.length;
        const proportional = type === 'line' && parsed.numeric && n > 1 && Number(keys[n - 1]) > Number(keys[0]);
        const xMin = Number(keys[0]);
        const xMax = Number(keys[n - 1]);
        const X = function (i) {
          if (type === 'bar') return padL + (i + 0.5) / n * pw;
          // inset 12 px each side so the first point never sits on the y-axis tick labels
          if (proportional) return padL + 12 + (Number(keys[i]) - xMin) / (xMax - xMin) * (pw - 24);
          return n === 1 ? padL + pw / 2 : padL + 12 + i / (n - 1) * (pw - 24);
        };
        const fontFamily = col.font || 'sans-serif';
        ctx.font = '11px ' + fontFamily;
        ctx.lineWidth = 1;
        // grid and y labels
        ctx.textAlign = 'right';
        ctx.textBaseline = 'middle';
        nt.ticks.forEach(function (v) {
          const y = Y(v);
          ctx.strokeStyle = col.rule;
          ctx.beginPath(); ctx.moveTo(padL, y); ctx.lineTo(w - padR, y); ctx.stroke();
          ctx.fillStyle = col.ink2;
          ctx.fillText(fmtNum(v, nt.step < 1 ? Math.min(3, Math.max(0, Math.ceil(-Math.log10(nt.step) - 1e-9))) : 0), padL - 6, y);
        });
        // axes
        ctx.strokeStyle = col.ink3;
        ctx.beginPath(); ctx.moveTo(padL, padT); ctx.lineTo(padL, padT + ph); ctx.lineTo(w - padR, padT + ph); ctx.stroke();
        // x labels, thinned to fit
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        const maxLabels = Math.max(1, Math.floor(pw / 52));
        const every = Math.max(1, Math.ceil(n / maxLabels));
        for (let i = 0; i < n; i++) {
          if (i % every !== 0 && i !== sel) continue;
          ctx.fillStyle = i === sel ? col.ink : col.ink2;
          ctx.fillText(keys[i], X(i), padT + ph + 8);
        }
        // selected category marker
        if (type === 'line') {
          ctx.strokeStyle = col.ink3;
          ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(X(sel), padT); ctx.lineTo(X(sel), padT + ph); ctx.stroke();
          ctx.setLineDash([]);
        }
        const cols = [col.sc, col.sc2 || col.red];
        series.forEach(function (s, si) {
          ctx.strokeStyle = cols[si];
          ctx.fillStyle = cols[si];
          if (type === 'bar') {
            const group = pw / n;
            const bw = Math.max(2, group * 0.72 / series.length);
            keys.forEach(function (k, i) {
              const v = s.vals[k];
              if (v == null) return;
              const x = padL + i * group + group * 0.14 + si * bw;
              const yTop = Math.min(Y(v), Y(0 < y0 ? y0 : 0));
              const hh = Math.abs(Y(v) - Y(0 < y0 ? y0 : 0));
              ctx.globalAlpha = si === 0 ? 1 : 0.35;
              ctx.fillRect(x, yTop, bw, Math.max(1, hh));
              ctx.globalAlpha = 1;
              ctx.lineWidth = i === sel ? 2.5 : 1.5;
              ctx.strokeStyle = i === sel ? col.ink : cols[si];
              ctx.strokeRect(x, yTop, bw, Math.max(1, hh));
            });
            ctx.lineWidth = 1;
          } else {
            ctx.lineWidth = 2.2;
            ctx.setLineDash(si === 0 ? [] : [6, 4]);
            ctx.beginPath();
            let pen = false;
            keys.forEach(function (k, i) {
              const v = s.vals[k];
              if (v == null) { pen = false; return; }
              if (!pen) { ctx.moveTo(X(i), Y(v)); pen = true; } else ctx.lineTo(X(i), Y(v));
            });
            ctx.stroke();
            ctx.setLineDash([]);
            keys.forEach(function (k, i) {
              const v = s.vals[k];
              if (v == null) return;
              const r = i === sel ? 5.5 : 3.5;
              ctx.beginPath();
              if (si === 0) ctx.arc(X(i), Y(v), r, 0, Math.PI * 2);
              else ctx.rect(X(i) - r, Y(v) - r, r * 2, r * 2);
              if (si === 0) ctx.fill();
              else { ctx.fillStyle = col.card || col.sheet || '#fff'; ctx.fill(); ctx.strokeStyle = cols[si]; ctx.lineWidth = 2; ctx.stroke(); ctx.fillStyle = cols[si]; }
            });
            ctx.lineWidth = 1;
          }
        });
        geo = { padL: padL, pw: pw, n: n, X: X, type: type };
      }
    });

    // Readout of the selected category
    const read = mk('div', { 'aria-live': 'polite', 'aria-atomic': 'true', style: { border: '1px solid var(--rule)', borderLeft: '4px solid var(--sc)', borderRadius: '8px', padding: '8px 12px', margin: '8px 0', background: 'var(--card)' } });
    function updateRead() {
      const k = keys[sel];
      const parts = series.map(function (s) {
        const v = s.vals[k];
        return s.name + ': ' + (v == null ? 'no figure' : fmtNum(v, dec) + (unit ? ' ' + unit : ''));
      });
      read.textContent = k + ' — ' + parts.join('; ');
    }
    function select(i) {
      sel = ((i % keys.length) + keys.length) % keys.length;
      updateRead();
      c.redraw();
    }

    const byYear = parsed.numeric;
    const prev = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: byYear ? '← Earlier' : '← Previous' });
    const next = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: byYear ? 'Later →' : 'Next →' });
    prev.onclick = function () { select(sel - 1); };
    next.onclick = function () { select(sel + 1); };

    const tableId = W.uid ? W.uid('hist-chart-table') : 'hist-chart-table';
    const toggle = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', 'aria-expanded': 'false', 'aria-controls': tableId, text: 'Show table' });
    const tableWrap = mk('div', { id: tableId, hidden: '', style: { overflowX: 'auto', margin: '6px 0' } });
    const table = mk('table');
    table.appendChild(mk('caption', { class: 'sr-only', text: title + (unit ? ' (' + unit + ')' : '') }));
    const headRow = mk('tr', {}, mk('th', { scope: 'col', text: byYear ? 'Year or period' : 'Item' }));
    series.forEach(function (s) { headRow.appendChild(mk('th', { scope: 'col', text: s.name })); });
    table.appendChild(mk('thead', {}, headRow));
    const tb = mk('tbody');
    keys.forEach(function (k) {
      const tr = mk('tr', {}, mk('th', { scope: 'row', text: k }));
      series.forEach(function (s) { tr.appendChild(mk('td', { text: s.vals[k] == null ? 'no figure' : fmtNum(s.vals[k], dec) })); });
      tb.appendChild(tr);
    });
    table.appendChild(tb);
    tableWrap.appendChild(table);
    toggle.onclick = function () {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      toggle.textContent = open ? 'Show table' : 'Hide table';
      if (open) tableWrap.setAttribute('hidden', ''); else tableWrap.removeAttribute('hidden');
    };

    body.appendChild(read);
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, prev, next, toggle));
    body.appendChild(tableWrap);
    if (source) body.appendChild(mk('p', { class: 'w-note', text: 'Source: ' + source }));
    body.appendChild(mk('p', { class: 'w-note', text: byYear ? 'Try: step through the years with the buttons, or press on the chart, and compare each figure with the one before it.' : 'Try: step through the bars with the buttons, or press on the chart, and compare the figures for each one.' }));

    // Press or move over the chart to choose the nearest year
    function pick(ev) {
      if (!geo || !geo.n) return;
      const r = c.wrap.getBoundingClientRect();
      const x = ev.clientX - r.left;
      let best = 0, bd = Infinity;
      for (let i = 0; i < geo.n; i++) {
        const d = Math.abs(geo.X(i) - x);
        if (d < bd) { bd = d; best = i; }
      }
      if (best !== sel) select(best);
    }
    c.wrap.addEventListener('pointerdown', pick);
    c.wrap.addEventListener('pointermove', function (ev) { if (ev.pointerType === 'mouse' || ev.buttons) pick(ev); });

    updateRead();
    c.redraw();
  });

  if (typeof module !== 'undefined' && module.exports) module.exports = { parseSeries: parseSeries, niceTicks: niceTicks, decimals: decimals, fmtNum: fmtNum, trendWords: trendWords };
})();
