/* phys-quarks: build hadrons from quarks, and see beta decay at quark level (phys.particles).
   data-tab="build|beta" (optional, default build). Plain DOM, no canvas.
   Charges are kept in thirds of e, so the sums are exact. */
(function () {
  'use strict';
  W.register('phys-quarks', function (el, opts) {
    const { body } = W.frame(el, 'Quarks and hadrons', 'Build a hadron from quarks, or watch β decay at quark level');
    const BAR = '̄';
    const FL = [['u', 2, 'up'], ['d', -1, 'down'], ['s', -1, 'strange'], ['c', 2, 'charm'], ['t', 2, 'top'], ['b', -1, 'bottom']];
    const info = {};
    FL.forEach((f) => { info[f[0]] = { q: f[1], name: f[2] }; });
    const sym = (x) => x.f + (x.anti ? BAR : '');
    const thirds = (x) => (x.anti ? -1 : 1) * info[x.f].q;
    const MINUS = '−';
    const showT = (t) => {            // charge in thirds -> text in units of e
      const sign = t > 0 ? '+' : t < 0 ? MINUS : '';
      const a = Math.abs(t);
      if (a % 3 === 0) return sign + (a / 3);
      return sign + a + '/3';
    };
    const showD = (t) => (t === 0 ? '0' : (t > 0 ? '+' : MINUS) + (Math.abs(t) / 3).toFixed(2));

    const st = { tab: opts.tab === 'beta' ? 'beta' : 'build', picked: [], plus: false };

    const tabRow = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose an activity' });
    const bBuild = W.h('button', { class: 'w-tab', type: 'button', onclick: () => { st.tab = 'build'; sync(); } }, 'Build a hadron');
    const bBeta = W.h('button', { class: 'w-tab', type: 'button', onclick: () => { st.tab = 'beta'; sync(); } }, 'β decay');
    tabRow.append(bBuild, bBeta);

    /* ---------- build panel ---------- */
    const build = W.h('div', {});
    const mkBtn = (f, anti) => {
      const x = { f, anti };
      const t = thirds(x);
      return W.h('button', {
        class: 'btn btn-sm btn-sec', type: 'button',
        'aria-label': 'Add ' + (anti ? 'anti-' : '') + info[f].name + ' quark, charge ' + (t > 0 ? 'plus ' : 'minus ') + (Math.abs(t) === 2 ? 'two' : 'one') + ' third',
        onclick: (e) => {
          if (st.picked.length < 3) { st.picked.push(x); render(); }
          if (e.currentTarget.disabled) clearBtn.focus();           // the quark buttons switch off when the three slots are full
        }
      }, sym(x) + ' ' + showT(t));
    };
    const rowQ = W.h('div', { class: 'w-row' });
    const rowA = W.h('div', { class: 'w-row' });
    const btnAll = [];
    FL.forEach((f) => { const b = mkBtn(f[0], false); btnAll.push(b); rowQ.append(b); });
    FL.forEach((f) => { const b = mkBtn(f[0], true); btnAll.push(b); rowA.append(b); });
    const slotRow = W.h('div', { class: 'w-row' });
    const clearBtn = W.h('button', { class: 'btn btn-sm', type: 'button', onclick: () => { st.picked = []; render(); btnAll[0].focus(); } }, 'Clear');
    const out = W.h('div', {});
    const res = W.readout([['charge', 'Total charge'], ['type', 'Type'], ['name', 'Name']]);
    const bnote = W.h('div', { class: 'w-note' }, 'Try uud and udd, then u with anti-d. Click a quark in the slots to remove it. Quarks have charges of ±⅓ e or ±⅔ e, and they are never found alone.');
    out.append(res.el);
    build.append(
      W.h('div', { class: 'w-lab' }, 'Quarks'), rowQ,
      W.h('div', { class: 'w-lab' }, 'Antiquarks'), rowA,
      W.h('div', { class: 'w-lab' }, 'Your hadron (up to three, click one to remove it)'),
      W.h('div', { class: 'w-row' }, slotRow, clearBtn), out, bnote
    );

    const NAMES = {
      'd|u|u': 'proton (baryon)', 'd|d|u': 'neutron (baryon)',
      'D|U|U': 'antiproton (antibaryon)', 'D|D|U': 'antineutron (antibaryon)',
      'D|u': 'π⁺ meson (for interest)', 'U|d': 'π⁻ meson (for interest)',
      'S|u': 'K⁺ meson (for interest)', 'U|s': 'K⁻ meson (for interest)'
    };
    function classify(list) {
      const n = list.length, na = list.filter((x) => x.anti).length;
      if (n === 0) return { type: 'Add some quarks.', name: '' };
      if (n === 1) return { type: 'Not a hadron: a quark is never found on its own.', name: '' };
      if (n === 2) {
        if (na === 1) return { type: 'Meson: one quark and one antiquark.', name: '' };
        return { type: 'Not a hadron in this syllabus: two quarks (or two antiquarks) do not make a hadron. A meson needs one quark and one antiquark.', name: '' };
      }
      if (na === 0) return { type: 'Baryon: three quarks.', name: '' };
      if (na === 3) return { type: 'Antibaryon: three antiquarks.', name: '' };
      return { type: 'Not a hadron in this syllabus: three particles must be all quarks (a baryon) or all antiquarks (an antibaryon).', name: '' };
    }
    function nameOf(list) {
      const key = (x) => (x.anti ? x.f.toUpperCase() : x.f);
      return NAMES[list.map(key).sort().join('|')] || '';
    }
    // after a slot is removed the slots shift left: focus the one now at that place, else the nearest enabled control
    function refocusSlot(i) {
      const bs = Array.from(slotRow.children);
      const t = !bs[i].disabled ? bs[i] : (i > 0 && !bs[i - 1].disabled) ? bs[i - 1] : !clearBtn.disabled ? clearBtn : btnAll[0];
      t.focus();
    }
    function render() {
      slotRow.replaceChildren();
      for (let i = 0; i < 3; i++) {
        const x = st.picked[i];
        const b = x
          ? W.h('button', { class: 'btn btn-sm', type: 'button', 'aria-label': 'Remove ' + (x.anti ? 'anti-' : '') + info[x.f].name + ' quark from slot ' + (i + 1), onclick: () => { st.picked.splice(i, 1); render(); refocusSlot(i); } }, sym(x) + ' (' + showT(thirds(x)) + ')')
          : W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', disabled: true, 'aria-label': 'Empty slot ' + (i + 1) }, 'empty');
        slotRow.append(b);
      }
      btnAll.forEach((b) => { b.disabled = st.picked.length >= 3; });
      clearBtn.disabled = st.picked.length === 0;
      const total = st.picked.reduce((s, x) => s + thirds(x), 0);
      const cl = classify(st.picked);
      res.set('charge', st.picked.length ? showT(total) + ' e' + (Math.abs(total) % 3 === 0 ? '' : ' (' + showD(total) + ' e)') : '—');
      res.set('type', cl.type);
      res.set('name', st.picked.length >= 2 ? (nameOf(st.picked) || '—') : '—');
    }

    /* ---------- beta panel ---------- */
    const beta = W.h('div', {});
    const modeRow = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Type of beta decay' });
    const mMinus = W.h('button', { class: 'w-tab', type: 'button', onclick: () => { st.plus = false; drawBeta(); } }, 'β⁻ decay');
    const mPlus = W.h('button', { class: 'w-tab', type: 'button', onclick: () => { st.plus = true; drawBeta(); } }, 'β⁺ decay');
    modeRow.append(mMinus, mPlus);
    const stage = W.h('div', { style: { display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '8px', margin: '10px 0' } });
    const eqn = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    beta.append(modeRow, stage, eqn);

    const chip = (txt, hot, kind) => W.h('span', {
      style: {
        display: 'inline-block', minWidth: '34px', textAlign: 'center', padding: '6px 10px', borderRadius: '999px',
        fontWeight: '700', background: 'var(--card)', color: 'var(--ink)',
        border: kind === 'u' ? '2px solid var(--sc)' : '2px dashed var(--ink-2)',
        outline: hot ? '3px solid var(--red)' : 'none', outlineOffset: '1px'
      }
    }, txt, hot ? W.h('span', { class: 'sr-only' }, ' (this one changes)') : null);
    const label = (txt) => W.h('span', { style: { color: 'var(--ink-2)', fontSize: '0.9em' } }, txt);
    const group = (title, chips) => {
      const g = W.h('div', { style: { display: 'flex', flexDirection: 'column', gap: '4px', alignItems: 'center' } });
      g.append(label(title), W.h('div', { style: { display: 'flex', gap: '4px' } }, ...chips));
      return g;
    };
    function drawBeta() {
      mMinus.setAttribute('aria-pressed', String(!st.plus));
      mPlus.setAttribute('aria-pressed', String(st.plus));
      stage.replaceChildren();
      if (!st.plus) {
        stage.append(
          group('neutron', [chip('u', false, 'u'), chip('d', true, 'd'), chip('d', false, 'd')]),
          label('→'),
          group('proton', [chip('u', false, 'u'), chip('u', true, 'u'), chip('d', false, 'd')]),
          label('+'), group('electron', [chip('e⁻', false, 'd')]),
          label('+'), group('antineutrino', [chip('ν' + BAR, false, 'd')])
        );
        eqn.textContent = 'β⁻ decay: a down quark changes into an up quark, d → u + e⁻ + ν' + BAR + '. Charge before: −1/3. Charge after: +2/3 + (−1) + 0 = −1/3. Nucleon number: the nucleon stays one nucleon, so it is conserved. A neutron (udd) has become a proton (uud).';
      } else {
        stage.append(
          group('proton', [chip('u', true, 'u'), chip('u', false, 'u'), chip('d', false, 'd')]),
          label('→'),
          group('neutron', [chip('d', true, 'd'), chip('u', false, 'u'), chip('d', false, 'd')]),
          label('+'), group('positron', [chip('e⁺', false, 'u')]),
          label('+'), group('neutrino', [chip('ν', false, 'u')])
        );
        eqn.textContent = 'β⁺ decay: an up quark changes into a down quark, u → d + e⁺ + ν. Charge before: +2/3. Charge after: −1/3 + 1 + 0 = +2/3. A proton (uud) has become a neutron (udd). This happens inside nuclei, never to a free proton.';
      }
    }

    body.append(tabRow, build, beta);
    function sync() {
      bBuild.setAttribute('aria-pressed', String(st.tab === 'build'));
      bBeta.setAttribute('aria-pressed', String(st.tab === 'beta'));
      build.style.display = st.tab === 'build' ? '' : 'none';
      beta.style.display = st.tab === 'beta' ? '' : 'none';
    }
    // start in a useful state: a proton already built
    st.picked = [{ f: 'u', anti: false }, { f: 'u', anti: false }, { f: 'd', anti: false }];
    render(); drawBeta(); sync();
  });
})();
