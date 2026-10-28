/* widgets/chem-chiral.js: two tetrahedral models that are mirror images, and a "can you superimpose them?" test.
   Attributes: data-mol="butan-2-ol" (butan-2-ol, lactic, alanine, chfclbr, propan-2-ol). */
(function () {
  'use strict';

  // groups: the four groups on the central carbon. The first two are always different from each other.
  const MOLS = {
    'butan-2-ol': { name: 'butan-2-ol', groups: ['H', 'OH', 'CH₃', 'C₂H₅'] },
    'lactic': { name: 'lactic acid (2-hydroxypropanoic acid)', groups: ['H', 'OH', 'CH₃', 'COOH'] },
    'alanine': { name: 'alanine (2-aminopropanoic acid)', groups: ['H', 'NH₂', 'CH₃', 'COOH'] },
    'chfclbr': { name: 'bromochlorofluoromethane', groups: ['H', 'F', 'Cl', 'Br'] },
    'propan-2-ol': { name: 'propan-2-ol', groups: ['H', 'OH', 'CH₃', 'CH₃'] }
  };
  const ORDER = ['butan-2-ol', 'lactic', 'alanine', 'chfclbr', 'propan-2-ol'];

  // ---- small 3x3 maths (x right, y into the page, z up) ----
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const norm = a => { const l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; };
  const mulv = (M, v) => [dot(M[0], v), dot(M[1], v), dot(M[2], v)];
  const transpose = M => [[M[0][0], M[1][0], M[2][0]], [M[0][1], M[1][1], M[2][1]], [M[0][2], M[1][2], M[2][2]]];
  const mul = (A, B) => { const Bt = transpose(B); return A.map(r => Bt.map(c => dot(r, c))); };
  const IDENT = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
  function frame(a, b) {
    const e1 = norm(a), e3 = norm(cross(a, b)), e2 = cross(e3, e1);
    return [[e1[0], e2[0], e3[0]], [e1[1], e2[1], e3[1]], [e1[2], e2[2], e3[2]]];
  }
  function matToQuat(R) {
    const tr = R[0][0] + R[1][1] + R[2][2];
    let w, x, y, z, S;
    if (tr > 0) { S = Math.sqrt(tr + 1) * 2; w = S / 4; x = (R[2][1] - R[1][2]) / S; y = (R[0][2] - R[2][0]) / S; z = (R[1][0] - R[0][1]) / S; }
    else if (R[0][0] > R[1][1] && R[0][0] > R[2][2]) { S = Math.sqrt(1 + R[0][0] - R[1][1] - R[2][2]) * 2; w = (R[2][1] - R[1][2]) / S; x = S / 4; y = (R[0][1] + R[1][0]) / S; z = (R[0][2] + R[2][0]) / S; }
    else if (R[1][1] > R[2][2]) { S = Math.sqrt(1 + R[1][1] - R[0][0] - R[2][2]) * 2; w = (R[0][2] - R[2][0]) / S; x = (R[0][1] + R[1][0]) / S; y = S / 4; z = (R[1][2] + R[2][1]) / S; }
    else { S = Math.sqrt(1 + R[2][2] - R[0][0] - R[1][1]) * 2; w = (R[1][0] - R[0][1]) / S; x = (R[0][2] + R[2][0]) / S; y = (R[1][2] + R[2][1]) / S; z = S / 4; }
    if (w < 0) { w = -w; x = -x; y = -y; z = -z; }
    return [w, x, y, z];
  }
  function quatToMat(q) {
    const [w, x, y, z] = q;
    return [[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
            [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
            [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]];
  }
  function partial(q, t) {            // rotation that is the fraction t of rotation q
    const th = Math.acos(Math.max(-1, Math.min(1, q[0])));
    if (th < 1e-6) return IDENT;
    const s = Math.sin(th), k = Math.sin(t * th) / s;
    return quatToMat([Math.cos(t * th), q[1] * k, q[2] * k, q[3] * k]);
  }

  // tetrahedral directions (unit vectors): one up, three below at azimuths 315, 195 and 75 degrees
  // (turned off the symmetric "cross" view so the model reads as 3D: one group near, one far)
  const RL = Math.sqrt(8 / 9);
  const az = a => a * Math.PI / 180;
  const DIRS = [
    [0, 0, 1],
    [RL * Math.cos(az(315)), RL * Math.sin(az(315)), -1 / 3],
    [RL * Math.cos(az(195)), RL * Math.sin(az(195)), -1 / 3],
    [RL * Math.cos(az(75)), RL * Math.sin(az(75)), -1 / 3]
  ];
  const PITCH = 0.35;
  const MIRROR = d => [-d[0], d[1], d[2]];

  W.register('chem-chiral', function (el, opts) {
    const { body } = W.frame(el, 'Chiral centre: mirror images', 'Can the mirror image be turned to match the original?');

    let key = 'butan-2-ol', msg = '';
    if (opts.mol !== undefined && opts.mol !== '') {
      const k = String(opts.mol).trim().toLowerCase();
      if (MOLS[k]) key = k;
      else msg = 'The molecule "' + String(opts.mol).slice(0, 24) + '" is not in the list. Showing butan-2-ol instead; pick another from the list.';
    }

    // ----- controls -----
    const sel = W.h('select', { 'aria-label': 'Molecule' });
    ORDER.forEach(k => sel.appendChild(W.h('option', { value: k, text: MOLS[k].name })));
    body.appendChild(W.h('div', { class: 'w-row' },
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Molecule' }), sel)));
    const err = W.h('div', { class: 'w-err', role: 'status' });
    body.appendChild(err);

    // ----- state -----
    let progress = 0;                  // 0 = right model as drawn, 1 = fully rotated onto the left
    let target = IDENT, targetQ = [1, 0, 0, 0];
    let verdict = '';
    let t0 = 0;
    const view = W.view3d({ yaw: 0, pitch: PITCH, scale: 60 });

    function groups() { return MOLS[key].groups; }
    function rightDirs() { return DIRS.map(MIRROR); }

    // rotation that puts right groups 0 and 1 on left groups 0 and 1
    function computeTarget() {
      const L = DIRS, Rr = rightDirs();
      const Fl = frame(L[0], L[1]), Fr = frame(Rr[0], Rr[1]);
      target = mul(Fl, transpose(Fr));
      targetQ = matToQuat(target);
    }
    function judge() {
      const g = groups(), L = DIRS, Rr = rightDirs();
      const moved = Rr.map(d => mulv(target, d));
      const result = [];
      for (let k = 2; k < 4; k++) {
        let m = -1;
        for (let j = 0; j < 4; j++) {
          if (Math.hypot(moved[k][0] - L[j][0], moved[k][1] - L[j][1], moved[k][2] - L[j][2]) < 0.05) m = j;
        }
        result.push({ k, m });
      }
      const allMatch = result.every(r => r.m >= 0 && g[r.m] === g[r.k]);
      if (allMatch) return 'All four groups match: the two models can be superimposed, so the molecule is not chiral.';
      return g[0] + ' and ' + g[1] + ' match, but ' + g[2] + ' and ' + g[3] + ' are swapped: the models cannot be superimposed, so the two forms are different molecules (enantiomers).';
    }

    // ----- the picture -----
    const cvs = W.canvas(body, {
      height: 270,
      draw(ctx, w, h, col) {
        if (!(w > 40 && h > 40)) return;
        const pal = W.palette(el), series = pal.series || [];
        const g = groups();
        const half = w / 2;
        view.scale = Math.max(10, Math.min((w / 4 - 20) / 0.95, h * 0.34));   // the widest group stays inside its half
        ctx.textBaseline = 'alphabetic';

        // mirror line and titles
        ctx.save();
        ctx.setLineDash([5, 5]); ctx.strokeStyle = col.rule2; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(half, 26); ctx.lineTo(half, h - 22); ctx.stroke();
        ctx.restore();
        ctx.font = '600 12px ' + col.font; ctx.textAlign = 'center'; ctx.fillStyle = col.ink2;
        ctx.fillText('mirror', half, h - 6);
        ctx.fillText('original', w * 0.25, 16);
        ctx.fillText('mirror image', w * 0.75, 16);

        const rot = progress <= 0 ? IDENT : progress >= 1 ? target : partial(targetQ, progress);
        const dy = 6;
        [0, 1].forEach(side => {
          const shift = (side === 0 ? w * 0.25 : w * 0.75) - half;
          const dirs = side === 0 ? DIRS : rightDirs().map(d => mulv(rot, d));
          const C = view.project(0, 0, 0, w, h);
          const cx = C[0] + shift, cy = C[1] + dy;
          const items = [];
          dirs.forEach((d, i) => {
            const P = view.project(d[0], d[1], d[2], w, h);
            items.push({ d: P[2], i, x: P[0] + shift, y: P[1] + dy });
          });
          items.push({ d: C[2], centre: true });
          // depth cue, as in wedge and hashed bonds: near bonds thick, far bonds thin and dashed
          ctx.strokeStyle = col.ink3;
          items.forEach(it => {
            if (it.centre) return;
            const dz = it.d - C[2];
            ctx.save();
            ctx.lineWidth = dz < -0.5 ? 5 : dz > 0.5 ? 2 : 3;
            if (dz > 0.5) ctx.setLineDash([4, 4]);
            ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(it.x, it.y); ctx.stroke();
            ctx.restore();
          });
          items.sort((a, b) => b.d - a.d).forEach(it => {
            if (it.centre) {
              ctx.lineWidth = 3; ctx.strokeStyle = col.ink2; ctx.fillStyle = col.card;
              ctx.beginPath(); ctx.arc(cx, cy, 11, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
              ctx.fillStyle = col.ink; ctx.font = '600 13px ' + col.font; ctx.textAlign = 'center';
              ctx.fillText('C', cx, cy + 5);
              return;
            }
            const label = g[it.i];
            const dd = Math.max(-1, Math.min(1, (it.d - C[2]) / 1.5));      // nearer groups are drawn larger
            const r = Math.max(11, (6 + 3.3 * label.length) * (1 - 0.2 * dd));
            ctx.lineWidth = 3; ctx.strokeStyle = series[it.i % series.length] || col.ink2; ctx.fillStyle = col.card;
            ctx.beginPath(); ctx.arc(it.x, it.y, r, 0, 2 * Math.PI); ctx.fill(); ctx.stroke();
            ctx.fillStyle = col.ink; ctx.font = '600 ' + (label.length > 3 ? 11 : 12) + 'px ' + col.font; ctx.textAlign = 'center';
            ctx.fillText(label, it.x, it.y + 4);
          });
        });
      }
    });
    cvs.cv.setAttribute('role', 'img');
    cvs.describe = () => 'Left: the original, a central carbon with the groups ' + groups().join(', ') + ' on tetrahedral bonds, thick bonds towards you and dashed bonds away. Right: its mirror image, '
      + (progress <= 0 ? 'as first drawn.' : progress < 1 ? 'turning to match the original.' : 'turned so that ' + groups()[0] + ' and ' + groups()[1] + ' sit on the same positions as the original. ' + verdict);
    W.orbit(cvs.wrap, view, cvs.redraw);

    // ----- buttons and readout -----
    const turn = W.h('button', { class: 'btn btn-sm', type: 'button' }, 'Rotate right model to match two groups');
    const reset = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button' }, 'Reset');
    const left = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', 'aria-label': 'Turn both models left' }, '◀ Turn');
    const right = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', 'aria-label': 'Turn both models right' }, 'Turn ▶');
    body.appendChild(W.h('div', { class: 'w-row' }, turn, reset, left, right));
    const read = W.readout([['centre', 'Chiral centre?'], ['groups', 'Groups on the carbon'], ['test', 'Result of the test']]);
    body.appendChild(read.el);
    body.appendChild(W.h('div', { class: 'w-note', text: 'The right-hand model is the mirror image of the left. Press the first button to turn it so that two of its groups sit on the same groups of the left model, then see whether the other two match. A thick bond points towards you and a dashed bond points away, like a wedge and a hashed bond. Drag the picture to turn both models together.' }));

    const anim = W.animate(() => {
      const p = Math.min(1, (performance.now() - t0) / 1400);
      progress = p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;   // ease in and out
      if (p >= 1) { progress = 1; finish(); cvs.redraw(); return false; }
      cvs.redraw();
      return true;
    }, { still() { progress = 1; finish(); cvs.redraw(); } });

    function finish() {
      verdict = judge();
      read.set('test', verdict);
    }

    function update() {
      const g = groups();
      sel.value = key;
      const distinct = new Set(g).size;
      read.set('groups', g.join(', '));
      read.set('centre', distinct === 4 ? 'Yes: all four groups are different' : 'No: two of the groups are the same (' + g.filter((x, i) => g.indexOf(x) !== i)[0] + ')');
      read.set('test', 'Press the first button to test.');
      progress = 0; verdict = '';
      computeTarget();
      err.textContent = msg;
      cvs.setLabel('Two mirror-image tetrahedral models of ' + MOLS[key].name);
      cvs.redraw();
    }

    sel.addEventListener('change', () => { key = sel.value; msg = ''; anim.stop(); update(); });
    turn.addEventListener('click', () => {
      if (progress >= 1) { progress = 0; }
      t0 = performance.now();
      anim.stop();
      anim.start();
    });
    reset.addEventListener('click', () => { anim.stop(); view.yaw = 0; view.pitch = PITCH; update(); });
    left.addEventListener('click', () => { view.yaw -= 0.4; cvs.redraw(); });
    right.addEventListener('click', () => { view.yaw += 0.4; cvs.redraw(); });
    update();
  });
})();
