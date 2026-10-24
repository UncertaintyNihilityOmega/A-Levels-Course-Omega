/* widgets/chem-qa.js: qualitative analysis (Cambridge 9701 Qualitative Analysis notes, copied from FACTS.md).
   Attributes: data-mode="explore" (default) or "test"; data-seed="12" (number) fixes the unknowns in test mode.
   Explore: pick an ion (optionally a second one to compare) and read the results of every test.
   Test: an unknown cation solution and an unknown anion solution; apply tests one at a time, then answer.
   Observations are never invented: where the notes give no result, the tool says so. For cations an unlisted result is "not listed"
   (the notes give "–" or nothing); for anions the notes list only the positive tests, so an unlisted result is "no change" only where
   nothing happens in the laboratory, and "no result listed" where a reaction does happen that the notes do not describe. */
(function () {
  'use strict';

  const NOTLISTED = 'no result listed in the notes';
  const NOCHANGE = 'no change';

  const CTESTS = ['NaOH(aq), a few drops', 'NaOH(aq), then excess', 'NaOH(aq), warm gently', 'NH₃(aq), a few drops', 'NH₃(aq), then excess'];
  // [text, key] per test, null = not listed
  const CATIONS = [
    ['Al³⁺', [['white ppt.', 'ppt:white'], ['ppt. soluble in excess', 'sol'], null, ['white ppt.', 'ppt:white'], ['ppt. insoluble in excess', 'insol']]],
    ['NH₄⁺', [['no ppt.', 'noppt'], ['no ppt.', 'noppt'], ['ammonia produced on warming', 'nh3'], null, null]],
    ['Ba²⁺', [['faint white ppt. unless [Ba²⁺] is very low', 'ppt:white'], null, null, ['no ppt.', 'noppt'], ['no ppt.', 'noppt']]],
    ['Ca²⁺', [['white ppt. unless [Ca²⁺] is very low', 'ppt:white'], null, null, ['no ppt.', 'noppt'], ['no ppt.', 'noppt']]],
    ['Cr³⁺', [['grey-green ppt.', 'ppt:grey-green'], ['ppt. soluble in excess, giving a dark green solution', 'sol:dark green'], null, ['grey-green ppt.', 'ppt:grey-green'], ['ppt. insoluble in excess', 'insol']]],
    ['Cu²⁺', [['pale blue ppt.', 'ppt:pale blue'], ['ppt. insoluble in excess', 'insol'], null, ['pale blue ppt.', 'ppt:pale blue'], ['ppt. soluble in excess, giving a dark blue solution', 'sol:dark blue']]],
    ['Fe²⁺', [['green ppt., turning brown on contact with air', 'ppt:green'], ['ppt. insoluble in excess', 'insol'], null, ['green ppt., turning brown on contact with air', 'ppt:green'], ['ppt. insoluble in excess', 'insol']]],
    ['Fe³⁺', [['red-brown ppt.', 'ppt:red-brown'], ['ppt. insoluble in excess', 'insol'], null, ['red-brown ppt.', 'ppt:red-brown'], ['ppt. insoluble in excess', 'insol']]],
    ['Mg²⁺', [['white ppt.', 'ppt:white'], ['ppt. insoluble in excess', 'insol'], null, ['white ppt.', 'ppt:white'], ['ppt. insoluble in excess', 'insol']]],
    ['Mn²⁺', [['off-white ppt., rapidly turning brown on contact with air', 'ppt:off-white'], ['ppt. insoluble in excess', 'insol'], null, ['off-white ppt., rapidly turning brown on contact with air', 'ppt:off-white'], ['ppt. insoluble in excess', 'insol']]],
    ['Zn²⁺', [['white ppt.', 'ppt:white'], ['ppt. soluble in excess', 'sol'], null, ['white ppt.', 'ppt:white'], ['ppt. soluble in excess', 'sol']]]
  ];

  const ATESTS = ['dilute acid', 'Ag⁺(aq) (after acidifying with dilute nitric acid)', 'NH₃(aq) added to that silver precipitate', 'Ba²⁺(aq)',
    'excess dilute strong acid added to that barium precipitate', 'OH⁻(aq) and aluminium foil, warm', 'acidified KMnO₄(aq)', 'Ca²⁺(aq) at a high concentration'];
  // A test missing from an anion's object gives "no change" (true in the laboratory); null marks a test where a reaction does
  // happen (e.g. BaCO₃ precipitates, SO₂ leaves sulfite with acid, I⁻ and S₂O₃²⁻ decolourise KMnO₄) but the notes list no result.
  const ANIONS = [
    ['CO₃²⁻', { 0: ['CO₂ liberated', 'co2'], 3: null, 4: null, 6: ['effervescence (CO₂ from the acid), but the purple colour stays', 'fizz'], 7: null }],
    ['Cl⁻', { 1: ['white ppt.', 'white'], 2: ['ppt. soluble in NH₃(aq)', 'sol'] }],
    ['Br⁻', { 1: ['cream or off-white ppt.', 'cream'], 2: ['ppt. partially soluble in NH₃(aq)', 'part'], 6: null }],
    ['I⁻', { 1: ['pale yellow ppt.', 'yellow'], 2: ['ppt. insoluble in NH₃(aq)', 'insol'], 6: null }],
    ['NO₃⁻', { 5: ['NH₃ liberated', 'nh3'] }],
    ['NO₂⁻', { 0: null, 1: null, 2: null, 5: ['NH₃ liberated', 'nh3'], 6: ['decolourises acidified KMnO₄(aq)', 'decol'] }],
    ['SO₄²⁻', { 3: ['white ppt.', 'white'], 4: ['ppt. insoluble in excess dilute strong acids', 'insol'], 7: ['white ppt.', 'white'] }],
    ['SO₃²⁻', { 0: ['no precipitate; on warming a gas is given off (sulfur dioxide, which decolourises acidified KMnO₄(aq))', 'so2'], 1: null, 2: null, 3: ['white ppt.', 'white'], 4: ['ppt. soluble in excess dilute strong acids', 'sol'], 6: ['decolourises acidified KMnO₄(aq)', 'decol'], 7: null }],
    ['S₂O₃²⁻', { 0: ['off-white or pale yellow ppt. forms slowly with H⁺', 'slow'], 1: null, 2: null, 3: null, 4: null, 6: null }]
  ];
  const NEG = { 5: 'no ammonia given off: damp red litmus paper stays red' };
  const GASES = [['NH₃', 'turns damp red litmus paper blue'], ['CO₂', 'gives a white precipitate with limewater'], ['H₂', '"pops" with a lighted splint'], ['O₂', 'relights a glowing splint'],
    ['I₂ (an element)', 'blue-black with starch']];

  function result(kind, ion, i) {
    // -> {t, k, listed}
    if (kind === 'c') {
      const r = ion[1][i];
      return r ? { t: r[0], k: r[1], listed: true } : { t: NOTLISTED, k: 'none', listed: false };
    }
    const r = ion[1][i];
    if (r === null) return { t: NOTLISTED, k: 'nl', listed: false };
    return r ? { t: r[0], k: r[1], listed: true } : { t: NEG[i] || NOCHANGE, k: 'none', listed: true };
  }
  function ntests(kind) { return kind === 'c' ? CTESTS.length : ATESTS.length; }
  function tests(kind) { return kind === 'c' ? CTESTS : ATESTS; }
  function ions(kind) { return kind === 'c' ? CATIONS : ANIONS; }

  // can the listed tests separate a from b?
  function separates(kind, a, b, i) {
    const x = result(kind, a, i), y = result(kind, b, i);
    return x.listed && y.listed && x.k !== y.k;
  }
  function indist(kind, a, b) {
    for (let i = 0; i < ntests(kind); i++) if (separates(kind, a, b, i)) return false;
    return true;
  }
  // smallest set of tests that separates ion a from every other ion that can be separated from it
  function fastest(kind, a) {
    const n = ntests(kind), others = ions(kind).filter(b => b !== a && !indist(kind, a, b));
    let best = null;
    for (let mask = 1; mask < (1 << n); mask++) {
      let size = 0; for (let i = 0; i < n; i++) if (mask & (1 << i)) size++;
      if (best && size >= best.size) continue;
      if (others.every(b => { for (let i = 0; i < n; i++) if ((mask & (1 << i)) && separates(kind, a, b, i)) return true; return false; })) best = { mask: mask, size: size };
    }
    const out = [];
    if (best) for (let i = 0; i < n; i++) if (best.mask & (1 << i)) out.push(tests(kind)[i]);
    return out;
  }

  W.register('chem-qa', function (el, opts) {
    const { body } = W.frame(el, 'Qualitative analysis', 'Tests for ions, as printed in the Cambridge notes');
    const msgs = [];
    const get = k => (opts[k] === undefined ? '' : String(opts[k]).trim());
    let top = 'explore';
    if (get('mode')) {
      const m = get('mode').toLowerCase();
      if (m === 'explore' || m === 'test') top = m;
      else msgs.push('data-mode "' + get('mode').slice(0, 12) + '" is not explore or test, so the explore view is shown.');
    }
    let seed = 11;
    if (get('seed')) {
      const s = Number(get('seed'));
      if (isFinite(s)) seed = Math.floor(Math.abs(s)) % 100000; else msgs.push('data-seed must be a number, so a standard seed is used.');
    }
    let cat = 'c';              // explore category: c, a, g

    const err = W.h('div', { class: 'w-err', role: 'status' });
    const tabE = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Explore', onclick: () => { top = 'explore'; render(); } });
    const tabT = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Test yourself', onclick: () => { top = 'test'; render(); } });
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Mode' }, tabE, tabT)));
    const exploreBox = W.h('div'), testBox = W.h('div');
    body.appendChild(exploreBox); body.appendChild(testBox); body.appendChild(err);

    // ---------------- explore ----------------
    const catC = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Cations', onclick: () => { cat = 'c'; renderExplore(); } });
    const catA = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Anions', onclick: () => { cat = 'a'; renderExplore(); } });
    const catG = W.h('button', { class: 'w-tab', type: 'button', role: 'tab', text: 'Gases', onclick: () => { cat = 'g'; renderExplore(); } });
    exploreBox.appendChild(W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-tabs', role: 'tablist', 'aria-label': 'Kind of test' }, catC, catA, catG)));
    const selA = W.h('select', { 'aria-label': 'First ion' });
    const selB = W.h('select', { 'aria-label': 'Compare with' });
    const rowSel = W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Ion' }), selA),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Compare with' }), selB));
    exploreBox.appendChild(rowSel);
    const tableHost = W.h('div', { style: { overflowX: 'auto' } });
    exploreBox.appendChild(tableHost);
    const exNote = W.h('div', { class: 'w-note' });
    exploreBox.appendChild(exNote);
    selA.addEventListener('change', renderTable);
    selB.addEventListener('change', renderTable);

    function fillSelects() {
      const kind = cat;
      [selA, selB].forEach(s => { s.textContent = ''; });
      if (kind === 'g') return;
      const list = ions(kind);
      list.forEach((ion, i) => selA.appendChild(W.h('option', { value: String(i), text: ion[0] })));
      selB.appendChild(W.h('option', { value: '-1', text: 'none' }));
      list.forEach((ion, i) => selB.appendChild(W.h('option', { value: String(i), text: ion[0] })));
      selA.value = '0'; selB.value = '-1';
    }
    function renderExplore() {
      catC.setAttribute('aria-selected', cat === 'c' ? 'true' : 'false');
      catA.setAttribute('aria-selected', cat === 'a' ? 'true' : 'false');
      catG.setAttribute('aria-selected', cat === 'g' ? 'true' : 'false');
      rowSel.style.display = cat === 'g' ? 'none' : '';
      fillSelects();
      renderTable();
    }
    function tr(cells) { const r = document.createElement('tr'); cells.forEach(c => { if (c) r.appendChild(c); }); return r; }
    function cell(text, strong) { return W.h('td', { style: { padding: '4px 8px', verticalAlign: 'top', fontWeight: strong ? '600' : '' }, text: text }); }
    function renderTable() {
      tableHost.textContent = '';
      if (cat === 'g') {
        const t = W.h('table');
        t.appendChild(tr([W.h('th', { text: 'Gas' }), W.h('th', { text: 'Test and result' })]));
        GASES.forEach(g => t.appendChild(tr([cell(g[0], true), cell(g[1])])));
        tableHost.appendChild(t);
        exNote.textContent = 'Say what you did and what you saw, then name the gas: "damp red litmus paper turns blue, so ammonia".';
        return;
      }
      const kind = cat, list = ions(kind);
      const a = list[Number(selA.value)], bi = Number(selB.value), b = bi >= 0 ? list[bi] : null;
      if (!a) return;
      const t = W.h('table');
      t.appendChild(tr([W.h('th', { text: 'Test' }), W.h('th', { text: a[0] }), b ? W.h('th', { text: b[0] }) : null, b ? W.h('th', { text: 'Tells them apart?' }) : null]));
      const apart = [];
      tests(kind).forEach((name, i) => {
        const x = result(kind, a, i), y = b ? result(kind, b, i) : null;
        let verdict = '';
        if (b) {
          if (!x.listed || !y.listed) verdict = 'not compared';
          else if (x.k !== y.k) { verdict = 'yes'; apart.push(name); } else verdict = 'same';
        }
        t.appendChild(tr([cell(name), cell(x.t), b ? cell(y.t) : null, b ? cell(verdict, verdict === 'yes') : null]));
      });
      tableHost.appendChild(t);
      if (b) {
        exNote.textContent = a === b ? 'Choose a different second ion to compare.' :
          (apart.length ? 'Tests that tell ' + a[0] + ' and ' + b[0] + ' apart: ' + apart.join('; ') + '.' : 'No test in the notes tells ' + a[0] + ' and ' + b[0] + ' apart.');
      } else exNote.textContent = 'Pick a second ion under "Compare with" to find the test that separates the two. Where the notes list no result, the table says so: do not invent one.';
    }

    // ---------------- test ----------------
    let unk = null;
    function newUnknowns(bump) {
      if (bump) seed = (seed * 7 + 13 + Math.floor(Math.random() * 1000)) % 100000;
      const r = W.rng(seed);
      unk = { c: Math.min(CATIONS.length - 1, Math.floor(r() * CATIONS.length)), a: Math.min(ANIONS.length - 1, Math.floor(r() * ANIONS.length)) };
    }
    function buildTest() {
      testBox.textContent = '';
      testBox.appendChild(W.h('div', { class: 'w-note', text: 'Solution X contains one cation from the list. Solution Y contains one anion (its cation is sodium, which gives no result in these tests). Apply tests one at a time, read the observation, then give your answers.' }));
      ['c', 'a'].forEach(kind => {
        const secret = ions(kind)[unk[kind]];
        const log = W.h('ul', { style: { margin: '6px 0', paddingLeft: '20px' } });
        const fb = W.h('div', { class: 'w-note', role: 'status' });
        const done = {};
        const btns = W.h('div', { class: 'w-row' });
        tests(kind).forEach((name, i) => {
          btns.appendChild(W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: name, onclick: () => {
            let obs;
            if (kind === 'a' && i === 2 && result(kind, secret, 1).k === 'none') obs = 'there is no silver precipitate to add ammonia to';
            else if (kind === 'a' && i === 4 && result(kind, secret, 3).k === 'none') obs = 'there is no barium precipitate to add acid to';
            else obs = result(kind, secret, i).t;
            if (done[i]) return;
            done[i] = true;
            log.appendChild(W.h('li', {}, W.h('b', { text: name + ': ' }), W.h('span', { text: obs })));
          } }));
        });
        const sel = W.h('select', { 'aria-label': kind === 'c' ? 'Your cation' : 'Your anion' });
        sel.appendChild(W.h('option', { value: '-1', text: 'choose' }));
        ions(kind).forEach((ion, i) => sel.appendChild(W.h('option', { value: String(i), text: ion[0] })));
        const check = W.h('button', { class: 'btn btn-sm', type: 'button', text: 'Check my answer', onclick: () => {
          const v = Number(sel.value);
          if (!(v >= 0)) { fb.textContent = 'Choose an answer first.'; return; }
          const mine = ions(kind)[v];
          const fast = fastest(kind, secret);
          const faststr = fast.length ? ' Tests that would have been enough: ' + fast.join('; ') + '.' : '';
          if (mine === secret) fb.textContent = 'Correct: ' + secret[0] + '.' + faststr;
          else if (indist(kind, mine, secret)) fb.textContent = 'The unknown was ' + secret[0] + '. The listed tests cannot separate ' + mine[0] + ' from it, so your answer fits every result.' + faststr;
          else fb.textContent = 'Not quite: the unknown was ' + secret[0] + '.' + faststr;
        } });
        testBox.appendChild(W.h('div', { style: { margin: '10px 0 4px', fontWeight: '600' }, text: kind === 'c' ? 'Solution X: which cation?' : 'Solution Y: which anion?' }));
        testBox.appendChild(btns); testBox.appendChild(log);
        testBox.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'My answer' }), sel), check));
        testBox.appendChild(fb);
      });
      testBox.appendChild(W.h('div', { class: 'w-row' }, W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: 'New unknowns', onclick: () => { newUnknowns(true); buildTest(); } })));
    }

    function render() {
      tabE.setAttribute('aria-selected', top === 'explore' ? 'true' : 'false');
      tabT.setAttribute('aria-selected', top === 'test' ? 'true' : 'false');
      exploreBox.style.display = top === 'explore' ? '' : 'none';
      testBox.style.display = top === 'test' ? '' : 'none';
      err.textContent = msgs.join(' ');
    }
    newUnknowns(false);
    buildTest();
    renderExplore();
    render();
  });
})();
