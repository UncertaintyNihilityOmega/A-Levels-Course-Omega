/* incline: forces on a block on a rough slope (g = 10).
   data-angle 30  data-mu 0.4  data-mass 5  data-force 0  data-fangle 0  (force P at fangle above the slope)
   data-m2 0 (a hanging mass over a smooth pulley at the top; omit or 0 for none) */
(function () {
  'use strict';
  const W = window.W;
  if (!W) return;
  const G = 10;
  const num = (v, d) => { const n = parseFloat(v); return isFinite(n) ? n : d; };
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const r2 = (x) => W.fmt(x, 3).replace('-', '−');
  const rad = (d) => d * Math.PI / 180;

  W.register('incline', function (el, o) {
    const warn = [];
    const rd = (key, d, lo, hi) => {
      const raw = o[key];
      let v = num(raw, d);
      if (raw != null && String(raw).trim() !== '' && !isFinite(parseFloat(raw))) warn.push(`data-${key} should be a number, so ${d} is used.`);
      if (v < lo || v > hi) { warn.push(`data-${key} is outside ${lo} to ${hi}, so it was adjusted.`); v = clamp(v, lo, hi); }
      return v;
    };
    let theta = rd('angle', 30, 0, 70), mu = rd('mu', 0.4, 0, 1.5), m = rd('mass', 5, 0.5, 20);
    let P = rd('force', 0, 0, 150), beta = rd('fangle', 0, -90, 90);
    const m2start = rd('m2', 0, 0, 20);
    const pulley = m2start > 0;
    let m2 = pulley ? Math.max(0.5, m2start) : 0;

    const { body } = W.frame(el, 'Block on a slope', 'Change the angle, friction, mass and pull; watch the forces and the state');
    const errBox = W.h('div', { class: 'w-err', role: 'status' });
    errBox.textContent = warn.join(' ');
    errBox.style.display = warn.length ? '' : 'none';
    body.append(errBox);

    const ctl = W.h('div', { class: 'w-row', style: { alignItems: 'flex-end' } });
    const sl = (label, min, max, step, value, set) => W.sliderNum({ label, min, max, step, value, oninput: (v) => { set(v); update(); } });
    ctl.append(
      sl('Slope angle θ (°)', 0, 70, 1, theta, (v) => { theta = clamp(v, 0, 70); }).el,
      sl('Coefficient of friction μ', 0, 1.5, 0.05, mu, (v) => { mu = clamp(v, 0, 1.5); }).el,
      sl('Mass m (kg)', 0.5, 20, 0.5, m, (v) => { m = clamp(v, 0.5, 20); }).el,
      sl('Applied force P (N)', 0, 150, 1, P, (v) => { P = clamp(v, 0, 150); }).el,
      sl('P above the slope (°)', -90, 90, 5, beta, (v) => { beta = clamp(v, -90, 90); }).el,
    );
    if (pulley) ctl.append(sl('Hanging mass (kg)', 0.5, 20, 0.5, m2, (v) => { m2 = clamp(v, 0.5, 20); }).el);
    body.append(ctl);

    const cv = W.canvas(body, { height: 300, draw, label: 'Block on a slope with its force arrows', describe: describeScene });
    const R = W.readout([['state', 'State'], ['R', 'Normal reaction R'], ['F', 'Friction F'], ['max', 'Greatest friction μR'], ['a', 'Acceleration']].concat(pulley ? [['T', 'Tension T']] : []));
    body.append(R.el);
    body.append(W.h('div', { class: 'w-note' }, pulley
      ? 'Try it: with a hanging mass of 2 kg, raise θ until the block starts to slide down, then raise μ until it holds. The force arrows are drawn to one scale.'
      : 'Try it: set P to 0 and raise θ until the block slips: that happens when tan θ = μ. Then add a pull up the slope (P above the slope = 0°) and find the P that holds the block. g = 10.'));

    function calc() {
      const th = rad(theta), be = rad(beta);
      const mg = m * G;
      const Rn = mg * Math.cos(th) - P * Math.sin(be);
      const out = { mg, Rn, lift: Rn <= 0 };
      const Rpos = Math.max(0, Rn);
      const Fmax = mu * Rpos;
      const Pup = P * Math.cos(be);
      let N0 = Pup - mg * Math.sin(th) + m2 * G;   // up-slope force that friction must oppose (hanging mass included)
      let M = m + m2, slack = false;
      let T = m2 * G;
      let a = 0, F = 0, state;
      const lim = Math.max(0.05, 1e-3 * Fmax);
      if (out.lift) { // block leaves the slope: treat as no contact
        state = 'The block leaves the slope (R would be negative)';
        F = 0; a = NaN;
      } else if (Math.abs(N0) <= Fmax - lim) {
        F = -N0; a = 0; state = 'At rest (friction is less than μR)';
      } else if (Math.abs(N0) <= Fmax + lim) {
        F = -N0; a = 0; state = 'Limiting equilibrium (about to slip ' + (N0 > 0 ? 'up' : 'down') + ' the slope)';
      } else {
        const sgn = Math.sign(N0);
        a = (N0 - sgn * Fmax) / M;
        F = -sgn * Fmax;
        T = m2 * (G - a);
        if (pulley && T < 0) { // string goes slack: the block moves on its own
          slack = true; T = 0;
          N0 = Pup - mg * Math.sin(th);
          const s2 = Math.sign(N0);
          if (Math.abs(N0) <= Fmax) { a = 0; F = -N0; } else { a = (N0 - s2 * Fmax) / m; F = -s2 * Fmax; }
        }
        state = a > 0 ? 'Sliding up the slope' : 'Sliding down the slope';
      }
      return Object.assign(out, { Fmax, F, a, T, state, slack, N0 });
    }

    function arrow(ctx, x, y, dx, dy, col, w, dash) {
      const len = Math.hypot(dx, dy);
      if (len < 2) return;
      ctx.save();
      ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = w || 2.4;
      if (dash) ctx.setLineDash(dash);
      const ex = x + dx, ey = y + dy, ux = dx / len, uy = dy / len;
      const hl = Math.min(10, len * 0.5);
      ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(ex - ux * hl * 0.6, ey - uy * hl * 0.6); ctx.stroke();
      ctx.setLineDash([]);
      ctx.beginPath(); ctx.moveTo(ex, ey);
      ctx.lineTo(ex - ux * hl + uy * hl * 0.42, ey - uy * hl - ux * hl * 0.42);
      ctx.lineTo(ex - ux * hl - uy * hl * 0.42, ey - uy * hl + ux * hl * 0.42);
      ctx.closePath(); ctx.fill();
      ctx.restore();
    }

    function label(ctx, c, text, x, y, col, align) {
      ctx.font = `600 12px ${c.font}`; ctx.textAlign = align || 'left'; ctx.textBaseline = 'middle';
      ctx.lineWidth = 3; ctx.strokeStyle = c.card; ctx.lineJoin = 'round'; ctx.strokeText(text, x, y);
      ctx.fillStyle = col; ctx.fillText(text, x, y);
    }

    function draw(ctx, w, h, c) {
      const S = calc();
      const th = rad(theta), cs = Math.cos(th), sn = Math.sin(th);
      const u = [cs, -sn], n = [-sn, -cs];                // up the slope, out of the slope (canvas y points down)
      const rightRoom = pulley ? 64 : 24;
      const x0 = 18, yb = h - 20;
      const L = Math.min((w - x0 - rightRoom) / Math.max(cs, 0.34), (h - 120) / Math.max(sn, 0.1), 520);
      const top = [x0 + L * cs, yb - L * sn];
      // ground and slope
      ctx.lineWidth = 2.2; ctx.strokeStyle = c.ink2;
      ctx.beginPath(); ctx.moveTo(4, yb); ctx.lineTo(w - 4, yb); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x0, yb); ctx.lineTo(top[0], top[1]); ctx.lineTo(top[0], yb); ctx.closePath();
      ctx.globalAlpha = 0.1; ctx.fillStyle = c.ink2; ctx.fill(); ctx.globalAlpha = 1; ctx.stroke();
      // angle mark
      if (theta > 3) {
        ctx.beginPath(); ctx.arc(x0, yb, 34, -th, 0); ctx.lineWidth = 1.4; ctx.strokeStyle = c.ink3; ctx.stroke();
        label(ctx, c, `θ = ${theta}°`, x0 + 42, yb - 10, c.ink2);
      }
      // block, centred 0.5 along the slope
      const bw = 52, bh = 34;
      const s0 = Math.min(L * 0.5, L - 40);
      const base = [x0 + u[0] * s0, yb + u[1] * s0];
      const C = [base[0] + n[0] * bh / 2, base[1] + n[1] * bh / 2];
      const corner = (a, b) => [C[0] + u[0] * a * bw / 2 + n[0] * b * bh / 2, C[1] + u[1] * a * bw / 2 + n[1] * b * bh / 2];
      ctx.beginPath();
      [[-1, -1], [1, -1], [1, 1], [-1, 1]].forEach(([a, b], i) => { const p = corner(a, b); i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]); });
      ctx.closePath(); ctx.fillStyle = c.card; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = c.sc; ctx.stroke();
      // pulley and hanging mass
      if (pulley) {
        const px = top[0], py = top[1];
        ctx.beginPath(); ctx.arc(px, py - 2, 7, 0, Math.PI * 2); ctx.fillStyle = c.card; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = c.ink2; ctx.stroke();
        const hx = px + 7, hy = Math.min(yb - 30, py + 40 + 3 * m2);
        ctx.lineWidth = 1.6; ctx.strokeStyle = c.ink2;
        ctx.beginPath(); ctx.moveTo(corner(1, 0)[0], corner(1, 0)[1]); ctx.lineTo(px, py - 9); ctx.lineTo(hx, py - 2); ctx.lineTo(hx, hy); ctx.stroke();
        ctx.fillStyle = c.card; ctx.fillRect(hx - 14, hy, 28, 24); ctx.strokeStyle = c.sc2; ctx.lineWidth = 2; ctx.strokeRect(hx - 14, hy, 28, 24);
        label(ctx, c, `${W.fmt(m2, 3)} kg`, hx + 18, hy + 12, c.ink2);
      }
      // force arrows: one scale
      const forces = [
        { v: [0, 1], f: S.mg, col: c.ink, t: 'W' },
        { v: n, f: Math.max(0, S.Rn), col: c.sc, t: 'R' },
        { v: u, f: S.F, col: c.red, t: 'F' },
        { v: [Math.cos(rad(beta)) * u[0] + Math.sin(rad(beta)) * n[0], Math.cos(rad(beta)) * u[1] + Math.sin(rad(beta)) * n[1]], f: P, col: c.sc2, t: 'P' },
      ];
      if (pulley) forces.push({ v: u, f: S.T, col: c.ink2, t: 'T' });
      const fmax = Math.max(1, ...forces.map((q) => Math.abs(q.f)));
      const k = Math.min(86 / fmax, 1.4);
      // weight components (dashed, drawn first)
      if (theta > 1) {
        arrow(ctx, C[0], C[1], -u[0] * S.mg * Math.sin(th) * k, -u[1] * S.mg * Math.sin(th) * k, c.ink3, 1.6, [4, 3]);
        arrow(ctx, C[0], C[1], -n[0] * S.mg * Math.cos(th) * k, -n[1] * S.mg * Math.cos(th) * k, c.ink3, 1.6, [4, 3]);
      }
      const placed = [];
      for (const q of forces) {
        if (Math.abs(q.f) < 0.05) continue;
        const dx = q.v[0] * q.f * k, dy = q.v[1] * q.f * k;
        arrow(ctx, C[0], C[1], dx, dy, q.col, 2.6);
        let lx = C[0] + dx * 1.0, ly = C[1] + dy * 1.0;
        const len = Math.hypot(dx, dy) || 1;
        lx += dx / len * 14; ly += dy / len * 10;
        if (q.t === 'T') ly -= 13;
        for (const pl of placed) if (Math.abs(pl[0] - lx) < 34 && Math.abs(pl[1] - ly) < 14) ly += 15;
        placed.push([lx, ly]);
        label(ctx, c, `${q.t} ${W.fmt(Math.abs(q.f), 3)} N`, lx, ly, q.col, dx < -1 ? 'right' : 'left');
      }
      ctx.beginPath(); ctx.arc(C[0], C[1], 3.5, 0, Math.PI * 2); ctx.fillStyle = c.ink; ctx.fill();
      ctx.font = `11px ${c.font}`; ctx.fillStyle = c.ink3; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
      ctx.fillText('dashed: components of W', 8, 14);
      return S;
    }

    function update() {
      const S = calc();
      R.set('state', S.state);
      R.set('R', S.lift ? 'not in contact' : `${W.fmt(S.Rn, 3)} N`);
      R.set('F', S.lift ? '0 N' : Math.abs(S.F) < 0.005 ? '0 N' : `${W.fmt(Math.abs(S.F), 3)} N ${S.F > 0 ? 'up' : 'down'} the slope`);
      R.set('max', S.lift ? '0 N' : `${W.fmt(S.Fmax, 3)} N`);
      R.set('a', isNaN(S.a) ? '—' : Math.abs(S.a) < 5e-4 ? '0' : `${W.fmt(Math.abs(S.a), 3)} m s⁻² ${S.a > 0 ? 'up' : 'down'} the slope`);
      if (pulley) R.set('T', S.slack ? '0 N (string slack)' : `${W.fmt(S.T, 3)} N`);
      cv.redraw();
    }
    function describeScene() {
      const S = calc();
      const parts = [`Block of mass ${W.fmt(m, 3)} kg on a slope at ${theta} degrees, friction coefficient ${mu}.`,
        `Weight ${W.fmt(S.mg, 3)} N down`];
      if (!S.lift) parts.push(`normal reaction ${W.fmt(S.Rn, 3)} N`);
      if (!S.lift && Math.abs(S.F) >= 0.005) parts.push(`friction ${W.fmt(Math.abs(S.F), 3)} N ${S.F > 0 ? 'up' : 'down'} the slope`);
      if (P >= 0.05) parts.push(`applied force P ${W.fmt(P, 3)} N at ${beta} degrees above the slope`);
      if (pulley) parts.push(`tension ${S.slack ? '0 N, string slack' : W.fmt(S.T, 3) + ' N'} with a hanging mass of ${W.fmt(m2, 3)} kg`);
      return `${parts.join(', ')}. ${S.state}.`;
    }
    update();
  });
})();
