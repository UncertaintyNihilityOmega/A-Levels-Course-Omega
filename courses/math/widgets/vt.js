/* vt: a velocity-time graph made of straight segments, with the s-t graph below it.
   data-segs "0,0; 4,12; 10,12; 14,0"  (t, v points)  Drag a point, or type new values.
   Shaded area = displacement; distance counts area below the axis as positive. */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const MAXPTS = 6, MINPTS = 2, MINGAP = 0.5;
  const f1 = (x) => (Math.abs(x) < 5e-10 ? '0' : String(Math.round(x * 100) / 100).replace('-', '−'));
  const f3 = (x) => (Math.abs(x) < 5e-10 ? '0' : W.fmt(x, 3).replace('-', '−'));

  function parseSegs(s) {
    const out = [];
    for (const part of String(s || '').replace(/[−–]/g, '-').split(';')) {
      if (!part.trim()) continue;
      const p = part.split(',').map((t) => parseFloat(t));
      if (p.length < 2 || !isFinite(p[0]) || !isFinite(p[1])) return null;
      out.push([p[0], p[1]]);
    }
    if (out.length < MINPTS || out.length > MAXPTS) return null;
    for (let i = 1; i < out.length; i++) if (!(out[i][0] > out[i - 1][0])) return null;
    return out;
  }

  W.register('vt', function (el, o) {
    const warn = [];
    const dflt = [[0, 0], [4, 12], [10, 12], [14, 0]];
    let pts = parseSegs(o.segs);
    if (!pts) {
      if (o.segs != null && String(o.segs).trim() !== '') warn.push('data-segs should look like "0,0; 4,12; 10,12; 14,0" with 2 to 6 points and increasing times. Showing the default graph.');
      pts = dflt.map((p) => p.slice());
    }
    if (pts[0][0] !== 0) { warn.push('The first point must be at t = 0, so it has been moved there.'); pts[0][0] = 0; }
    const start = pts.map((p) => p.slice());

    // fixed view so that dragging does not rescale under the pointer
    const tTop = Math.max(...start.map((p) => p[0]));
    const vPos = Math.max(5, ...start.map((p) => p[1]));
    const vNeg = Math.min(0, ...start.map((p) => p[1]));
    const view = {
      x0: 0, x1: Math.ceil((tTop * 1.2) / 2) * 2,
      y1: Math.ceil(vPos * 1.3),
      y0: -Math.max(Math.ceil(-vNeg * 1.3), Math.ceil(vPos * 0.4)),
    };

    const { body } = W.frame(el, 'Velocity–time graph', 'Drag the points: area is displacement, gradient is acceleration');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    const showErr = (m) => { errBox.textContent = m; errBox.style.display = m ? '' : 'none'; };
    showErr(warn.join(' '));
    body.append(errBox);

    const vtCv = W.canvas(body, { height: 240, draw: drawVT });
    vtCv.wrap.style.touchAction = 'none';
    const stCv = W.canvas(body, { height: 170, draw: drawST });
    const tiles = W.h('div', { class: 'w-out' });
    const sDisp = W.stat('Displacement', true), sDist = W.stat('Distance'), sAvg = W.stat('Average speed');
    tiles.append(sDisp.el, sDist.el, sAvg.el);
    body.append(tiles);

    const tableWrap = W.h('div', { style: { overflowX: 'auto' } });
    body.append(tableWrap);

    // typed values for each point
    const edit = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } });
    body.append(edit);
    const btns = W.h('div', { class: 'w-row' });
    const addBtn = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', onclick: addPoint }, 'Add a point');
    const delBtn = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', onclick: delPoint }, 'Remove last point');
    const resetBtn = W.h('button', { type: 'button', class: 'btn btn-sec btn-sm', onclick: () => { pts = start.map((p) => p.slice()); showErr(warn.join(' ')); rebuild(); } }, 'Reset');
    btns.append(addBtn, delBtn, resetBtn);
    body.append(btns);
    body.append(W.h('div', { class: 'w-note' }, 'Try it: drag the top-right point down to make the car slow to a stop sooner, or below the axis so it reverses. The shaded area below the axis counts as negative displacement but positive distance. Times and velocities snap to half units.'));

    /* ----- geometry and maths ----- */
    const geoVT = { pad: { l: 44, r: 14, t: 12, b: 28 }, w: 0, h: 0 };

    function segInfo() {
      const rows = [];
      let s = 0, dist = 0;
      for (let i = 0; i + 1 < pts.length; i++) {
        const [t1, v1] = pts[i], [t2, v2] = pts[i + 1];
        const dt = t2 - t1, a = (v2 - v1) / dt;
        const disp = 0.5 * (v1 + v2) * dt;
        let d;
        if (v1 * v2 < 0) {
          const tc = dt * Math.abs(v1) / (Math.abs(v1) + Math.abs(v2));
          d = 0.5 * Math.abs(v1) * tc + 0.5 * Math.abs(v2) * (dt - tc);
        } else d = Math.abs(disp);
        rows.push({ i, t1, t2, v1, v2, a, disp, dist: d, s0: s });
        s += disp; dist += d;
      }
      return { rows, s, dist, T: pts[pts.length - 1][0] };
    }

    function sAt(info, t) {
      for (const r of info.rows) {
        if (t <= r.t2 + 1e-12) { const tau = t - r.t1; return r.s0 + r.v1 * tau + 0.5 * r.a * tau * tau; }
      }
      return info.s;
    }

    function drawVT(ctx, w, h, c) {
      geoVT.w = w; geoVT.h = h;
      const pad = geoVT.pad;
      const A = W.axes(ctx, w, h, view, c, { pad, xlabel: 't (s)', ylabel: 'v (m s⁻¹)' });
      const X = A.X, Y = A.Y;
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      const info = segInfo();
      // shaded areas
      for (const r of info.rows) {
        const poly = (a, b, c2, d2, col) => {
          ctx.beginPath(); ctx.moveTo(X(a[0]), Y(a[1])); ctx.lineTo(X(b[0]), Y(b[1])); ctx.lineTo(X(c2[0]), Y(c2[1]));
          if (d2) ctx.lineTo(X(d2[0]), Y(d2[1]));
          ctx.closePath(); ctx.globalAlpha = 0.28; ctx.fillStyle = col; ctx.fill(); ctx.globalAlpha = 1;
        };
        if (r.v1 * r.v2 < 0) {
          const tc = r.t1 + (r.t2 - r.t1) * Math.abs(r.v1) / (Math.abs(r.v1) + Math.abs(r.v2));
          poly([r.t1, 0], [r.t1, r.v1], [tc, 0], null, r.v1 > 0 ? c.sc2 : c.red);
          poly([tc, 0], [r.t2, r.v2], [r.t2, 0], null, r.v2 > 0 ? c.sc2 : c.red);
        } else {
          const neg = r.v1 + r.v2 < 0;
          poly([r.t1, 0], [r.t1, r.v1], [r.t2, r.v2], [r.t2, 0], neg ? c.red : c.sc2);
        }
      }
      // the graph
      ctx.beginPath(); pts.forEach((p, k) => (k ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1]))));
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2.6; ctx.lineJoin = 'round'; ctx.stroke();
      // dashed drop lines
      ctx.strokeStyle = c.ink3; ctx.lineWidth = 1; ctx.setLineDash([3, 4]);
      for (const p of pts) { ctx.beginPath(); ctx.moveTo(X(p[0]), Y(0)); ctx.lineTo(X(p[0]), Y(p[1])); ctx.stroke(); }
      ctx.setLineDash([]);
      // handles
      pts.forEach((p, k) => {
        ctx.beginPath(); ctx.arc(X(p[0]), Y(p[1]), 7, 0, Math.PI * 2);
        ctx.fillStyle = k === 0 ? c.card : c.red; ctx.fill();
        ctx.lineWidth = 2; ctx.strokeStyle = k === 0 ? c.ink2 : c.card; ctx.stroke();
      });
      // acceleration labels on slanted/flat segments
      ctx.font = `600 11px ${c.font}`; ctx.textAlign = 'center'; ctx.fillStyle = c.ink;
      for (const r of info.rows) {
        if (X(r.t2) - X(r.t1) < 46) continue;
        const mx = X((r.t1 + r.t2) / 2), my = Y((r.v1 + r.v2) / 2);
        // halo in the card colour so the label stays readable where it crosses the graph line
        ctx.lineWidth = 4; ctx.lineJoin = 'round'; ctx.strokeStyle = c.card;
        ctx.strokeText(`a = ${f3(r.a)}`, mx, my - 9);
        ctx.fillText(`a = ${f3(r.a)}`, mx, my - 9);
      }
      ctx.restore();
    }

    function drawST(ctx, w, h, c) {
      const pad = { l: 44, r: 14, t: 10, b: 28 };
      const info = segInfo();
      const N = 160; let lo = 0, hi = 0; const sp = [];
      for (let i = 0; i <= N; i++) { const t = view.x1 * i / N; const tt = Math.min(t, info.T); const s = sAt(info, tt) + (t > info.T ? 0 : 0); sp.push([t, s]); lo = Math.min(lo, s); hi = Math.max(hi, s); }
      if (!(hi - lo > 1e-9)) { hi = lo + 1; }
      const padY = (hi - lo) * 0.12;
      const A = W.axes(ctx, w, h, { x0: 0, x1: view.x1, y0: lo - padY, y1: hi + padY }, c, { pad, xlabel: 't (s)', ylabel: 's (m)' });
      ctx.save();
      ctx.beginPath(); ctx.rect(pad.l, pad.t, w - pad.l - pad.r, h - pad.t - pad.b); ctx.clip();
      ctx.beginPath();
      let first = true;
      for (const [t, s] of sp) { if (t > info.T + 1e-9) break; if (first) { ctx.moveTo(A.X(t), A.Y(s)); first = false; } else ctx.lineTo(A.X(t), A.Y(s)); }
      ctx.strokeStyle = c.sc; ctx.lineWidth = 2.4; ctx.stroke();
      // mark the points
      for (const p of pts) {
        ctx.beginPath(); ctx.arc(A.X(p[0]), A.Y(sAt(info, p[0])), 4, 0, Math.PI * 2);
        ctx.fillStyle = c.red; ctx.fill();
      }
      ctx.restore();
    }

    /* ----- readouts ----- */
    function update() {
      const info = segInfo();
      sDisp.set(`${f3(info.s)} m`);
      sDist.set(`${f3(info.dist)} m`);
      sAvg.set(`${f3(info.dist / info.T)} m s⁻¹`);
      const tb = W.h('table');
      tb.append(W.h('thead', {}, W.h('tr', {}, ...['Stage', 'From t to t', 'Acceleration (m s⁻²)', 'Displacement (m)'].map((t) => W.h('th', {}, t)))));
      const tbody = W.h('tbody');
      info.rows.forEach((r, k) => {
        tbody.append(W.h('tr', {}, W.h('td', {}, String(k + 1)), W.h('td', {}, `${f1(r.t1)} to ${f1(r.t2)} s`), W.h('td', {}, f3(r.a)), W.h('td', {}, f3(r.disp))));
      });
      tb.append(tbody);
      tableWrap.replaceChildren(tb);
      vtCv.wrap.setAttribute('role', 'img');
      vtCv.wrap.setAttribute('aria-label', `Velocity–time graph through ${pts.map((p) => `(${f1(p[0])}, ${f1(p[1])})`).join(', ')}. Displacement ${f3(info.s)} metres, distance ${f3(info.dist)} metres.`);
      stCv.wrap.setAttribute('role', 'img');
      stCv.wrap.setAttribute('aria-label', `Displacement–time graph for the same motion, ending at ${f3(info.s)} metres.`);
      addBtn.disabled = pts.length >= MAXPTS;
      delBtn.disabled = pts.length <= MINPTS;
      vtCv.redraw(); stCv.redraw();
    }

    function syncInputs() {
      pts.forEach((p, k) => {
        if (edit.__t && edit.__t[k]) { edit.__t[k].input.value = String(p[0]); edit.__v[k].input.value = String(p[1]); }
      });
    }

    function rebuild() {
      edit.replaceChildren();
      edit.__t = []; edit.__v = [];
      pts.forEach((p, k) => {
        const tf = W.field({ label: `Point ${k + 1}: t`, value: String(p[0]), type: 'number', step: 0.5, width: '5.2em',
          oninput: () => setFromField(k, 0, tf) });
        const vf = W.field({ label: `v`, value: String(p[1]), type: 'number', step: 0.5, width: '5.2em',
          oninput: () => setFromField(k, 1, vf) });
        if (k === 0) tf.input.disabled = true;
        edit.__t.push(tf); edit.__v.push(vf);
        edit.append(tf.el, vf.el);
      });
      update();
    }

    function setFromField(k, which, fld) {
      const raw = parseFloat(fld.input.value);
      if (!isFinite(raw)) { showErr('Type a number.'); return; }
      if (which === 0) {
        const lo = pts[k - 1][0] + MINGAP, hi = k + 1 < pts.length ? pts[k + 1][0] - MINGAP : view.x1;
        if (raw < lo || raw > hi) { showErr(`Time for point ${k + 1} must be between ${f1(lo)} and ${f1(hi)} s (times increase from left to right).`); return; }
        pts[k][0] = raw;
      } else {
        if (raw < view.y0 || raw > view.y1) { showErr(`Velocity must be between ${f1(view.y0)} and ${f1(view.y1)} m s⁻¹ for this graph.`); return; }
        pts[k][1] = raw;
      }
      showErr(''); update();
    }

    function addPoint() {
      if (pts.length >= MAXPTS) return;
      const [t, v] = pts[pts.length - 1];
      const nt = t + 2;
      if (nt > view.x1) { showErr('There is no room to the right for another point.'); return; }
      pts.push([nt, v]); showErr(''); rebuild();
    }
    function delPoint() { if (pts.length > MINPTS) { pts.pop(); showErr(''); rebuild(); } }

    /* ----- dragging ----- */
    const toData = (px, py) => {
      const p = geoVT.pad, pw = geoVT.w - p.l - p.r, ph = geoVT.h - p.t - p.b;
      return [view.x0 + (px - p.l) / pw * (view.x1 - view.x0), view.y1 - (py - p.t) / ph * (view.y1 - view.y0)];
    };
    const toPix = (t, v) => {
      const p = geoVT.pad, pw = geoVT.w - p.l - p.r, ph = geoVT.h - p.t - p.b;
      return [p.l + (t - view.x0) / (view.x1 - view.x0) * pw, p.t + (view.y1 - v) / (view.y1 - view.y0) * ph];
    };
    W.drag(vtCv.wrap, {
      hit(px, py) {
        let best = null, bd = 18;
        pts.forEach((p, k) => {
          const [qx, qy] = toPix(p[0], p[1]);
          const d = Math.hypot(qx - px, qy - py);
          if (d < bd) { bd = d; best = k; }
        });
        return best;
      },
      move(k, px, py) {
        const [t, v] = toData(px, py);
        const snap = (x) => Math.round(x * 2) / 2;
        if (k > 0) {
          const lo = pts[k - 1][0] + MINGAP, hi = k + 1 < pts.length ? pts[k + 1][0] - MINGAP : view.x1;
          pts[k][0] = clamp(snap(t), lo, hi);
        }
        pts[k][1] = clamp(snap(v), Math.ceil(view.y0), Math.floor(view.y1));
        syncInputs(); showErr(''); update();
      },
      end() {},
    });

    rebuild();
  });
})();
