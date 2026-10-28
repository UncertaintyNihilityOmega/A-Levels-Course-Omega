/* widgets-study.js — study-planning widgets for the Preparation Roadmap:
   planner (personal study-plan generator), timer (Pomodoro study timer), ucas (UCAS tariff calculator). */
(function () {
  'use strict';
  if (!window.W) return;
  const h = W.h;
  let UID = 0;

  /* ---------------- shared helpers ---------------- */
  const DAY = 86400000;
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const DOW = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const midnight = (d) => new Date(d.getFullYear(), d.getMonth(), d.getDate());
  const addDays = (d, n) => new Date(d.getFullYear(), d.getMonth(), d.getDate() + n);
  const dBetween = (a, b) => Math.round((b - a) / DAY);
  /** "1 Oct" or "1 Oct 2026" */
  const fd = (d, yr) => d.getDate() + ' ' + MON[d.getMonth()] + (yr ? ' ' + d.getFullYear() : '');
  /** half-hour units -> "6.5" */
  const hrs = (u) => String(Math.round(u) / 2);
  const reduced = () => { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } };
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));

  /** Split an integer total into parts proportional to weights (largest remainder). */
  function allocate(total, weights) {
    const sw = weights.reduce((a, b) => a + b, 0);
    if (!(sw > 0) || !(total > 0)) return weights.map(() => 0);
    const raw = weights.map((w) => total * w / sw);
    const out = raw.map(Math.floor);
    const rem = total - out.reduce((a, b) => a + b, 0);
    const order = raw.map((r, i) => [r - out[i], i]).sort((a, b) => b[0] - a[0] || a[1] - b[1]);
    for (let k = 0; k < rem; k++) out[order[k % order.length][1]]++;
    return out;
  }

  /** Small section heading used inside the bigger widgets. */
  function sec(title, extra) {
    return h('div', { style: { display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', gap: '4px 12px', flexWrap: 'wrap', borderTop: '1px solid var(--rule)', paddingTop: '12px', marginTop: '2px' } },
      h('span', { style: { fontFamily: 'var(--f-mono)', fontSize: '.72rem', textTransform: 'uppercase', letterSpacing: '.08em', fontWeight: '600', color: 'var(--ink-2)' } }, title),
      extra || null);
  }

  /** Coloured advice box. kind: red | amber | ok | plain. lines = paragraphs; list = optional {title, items} bullet list. */
  function box(kind, title, lines, list) {
    const bg = { red: 'var(--red-soft)', amber: 'var(--hl-soft)', ok: 'var(--ok-soft)' }[kind] || 'var(--card)';
    const bd = { red: 'var(--red)', amber: 'var(--hl)', ok: 'var(--ok)' }[kind] || 'var(--rule)';
    lines = (lines || []).filter(Boolean);
    const items = list && list.items.filter(Boolean);
    return h('div', { style: { background: bg, borderLeft: '4px solid ' + bd, borderRadius: '8px', padding: '9px 12px', fontSize: '.9rem', lineHeight: '1.45', color: 'var(--ink)' } },
      title ? h('b', { style: { display: 'block', marginBottom: '2px' } }, title) : null,
      lines.map((l) => h('div', { style: { margin: '2px 0' } }, l)),
      items && items.length ? h('div', { style: { marginTop: '5px', fontWeight: '600' } }, list.title) : null,
      items && items.length ? h('ul', { style: { margin: '2px 0 0', paddingLeft: '1.2em' } }, items.map((l) => h('li', { style: { margin: '2px 0' } }, l))) : null);
  }
  /** Small grey note (not .w-note: each widget keeps a single "what to try" .w-note line). */
  const small = (text, extra) => h('div', { style: Object.assign({ fontSize: '.8rem', color: 'var(--ink-2)', lineHeight: '1.45' }, extra || {}) }, text);

  /* =====================================================================
     1. planner — personal study-plan generator
     ===================================================================== */

  /* Typical exam windows. Exact dates come from each board's published timetable. */
  const SESS = {
    jan: { label: (y) => `January ${y} (Edexcel IAL)`, s: [0, 7], e: [0, 28], r: [2, 5], rTxt: 'early March',
      note: 'January: Pearson Edexcel IAL only, and not every subject or unit is offered. Cambridge has no January series. Papers ≈ 7–28 January.' },
    mj: { label: (y) => `May/June ${y}`, s: [3, 27], e: [5, 19], r: [7, 13], rTxt: 'mid-August',
      note: 'May/June: Cambridge, Edexcel IAL and the UK boards (AQA, OCR, Edexcel). Papers ≈ late April to mid-June (UK boards: mid-May to late June).' },
    on: { label: (y) => `Oct/Nov ${y}`, s: [9, 5], e: [10, 13], r: [0, 13], rNext: true, rTxt: 'January',
      note: 'Oct/Nov: Cambridge and Edexcel IAL only (UK boards set A Level exams in summer only). Papers ≈ early October to mid-November.' }
  };
  function sessionList(today) {
    const y = today.getFullYear(), out = [];
    for (let yy = y; yy <= y + 2; yy++) {
      for (const k of ['jan', 'mj', 'on']) {
        const S = SESS[k];
        const start = new Date(yy, S.s[0], S.s[1]);
        if (dBetween(today, start) < 14) continue; // past, or too close to plan for
        const results = new Date(yy + (S.rNext ? 1 : 0), S.r[0], S.r[1]);
        out.push({ id: k + yy, k, year: yy, label: S.label(yy), start, end: new Date(yy, S.e[0], S.e[1]), results,
          rTxt: S.rTxt + ' ' + results.getFullYear(), note: S.note });
      }
    }
    return out;
  }

  /* w = weight for weekly hours (maths/sciences a little higher); c = colour token; q = quantitative; e = essay-based */
  const SUBJ = [
    { n: 'Mathematics', s: 'Maths', w: 1.15, c: '--c-math', q: 1 },
    { n: 'Further Mathematics', s: 'Further Maths', w: 1.2, c: '--c2-math', q: 1 },
    { n: 'Physics', s: 'Physics', w: 1.15, c: '--c-phys', q: 1, sci: 1 },
    { n: 'Chemistry', s: 'Chemistry', w: 1.15, c: '--c-chem', q: 1, sci: 1 },
    { n: 'Biology', s: 'Biology', w: 1.1, c: '--c-bio', q: 1, sci: 1 },
    { n: 'Business', s: 'Business', w: 0.95, c: '--c-bus', e: 1 },
    { n: 'Economics', s: 'Economics', w: 1, c: '--c-econ', q: 1, e: 1 },
    { n: 'Accounting', s: 'Accounting', w: 1, c: '--c2-bus', q: 1 },
    { n: 'Computer Science', s: 'Comp. Sci.', w: 1.05, c: '--c-eng', q: 1 },
    { n: 'Psychology', s: 'Psychology', w: 0.95, c: '--c2-bio', e: 1 },
    { n: 'English', s: 'English', w: 0.95, c: '--c-other', e: 1 },
    { n: 'History', s: 'History', w: 0.95, c: '--c-practice', e: 1 },
    { n: 'Geography', s: 'Geography', w: 0.95, c: '--c2-other', e: 1 },
    { n: 'Other', s: 'Other', w: 1, c: '--c-tools', e: 1 }
  ];

  /* need = rough self-study hours for one full A Level from this starting point;
     f = foundations [share of learning time, min weeks, max weeks]; minW = shortest sensible run-up in weeks [full, AS] */
  const LEVELS = {
    zero: { label: 'Starting from zero', short: 'from zero', need: 400, f: [0.2, 2, 8], minW: [30, 18] },
    some: { label: 'Some GCSE/IGCSE background', short: 'from GCSE level', need: 300, f: [0.1, 1, 4], minW: [20, 12] },
    strong: { label: 'Strong background', short: 'from a strong start', need: 200, f: [0.04, 0.5, 1.5], minW: [12, 8] }
  };
  const AS_FACTOR = 0.55;

  const PH = [
    { n: 'Fix foundations', s: 'Foundations', link: 'road.foundations' },
    { n: 'Learn the content', s: 'Learn', link: 'road.learn' },
    { n: 'Practise', s: 'Practise', link: 'road.practice' },
    { n: 'Past papers', s: 'Past papers', link: 'road.pastpapers' },
    { n: 'Final revision', s: 'Revision', link: 'road.final' },
    { n: 'Exam period', s: 'Exams', link: 'road.examday' }
  ];
  const PH_BG = ['color-mix(in srgb, var(--sc) 20%, var(--sheet))', 'color-mix(in srgb, var(--sc) 35%, var(--sheet))',
    'color-mix(in srgb, var(--sc) 50%, var(--sheet))', 'color-mix(in srgb, var(--sc) 85%, var(--sheet))', 'var(--sc)', 'var(--ink)'];
  const PH_FG = ['var(--ink)', 'var(--ink)', 'var(--ink)', 'var(--sheet)', 'var(--sheet)', 'var(--sheet)'];

  /** Phase lengths in weeks [foundations, learn, practise, past papers, final revision] for T weeks of run-up. */
  function phaseWeeks(T, levelKey) {
    const L = LEVELS[levelKey];
    let fr, pp, f, p, learn, R;
    if (T >= 8) {
      fr = T >= 40 ? 5 : T >= 24 ? 4 : T >= 14 ? 3 : 2;
      pp = T >= 20 ? clamp(T * 0.25, 6, 8) : T * 0.27; // at least 6–8 weeks of past papers when there is time
      R = T - fr - pp;
      f = Math.min(L.f[2], Math.max(Math.min(L.f[1], R * 0.3), R * L.f[0]));
      p = R * 0.18;
    } else { // short run-up: squeeze everything, keep revision and papers
      fr = T * 0.3; pp = T * 0.35;
      R = T - fr - pp;
      f = R * (levelKey === 'zero' ? 0.25 : levelKey === 'some' ? 0.12 : 0);
      p = R * 0.3;
    }
    learn = Math.max(0, R - f - p);
    return [f, learn, p, pp, fr];
  }

  /** Weekly budget in half-hour units: per-subject units, Mon–Sat capacities and a day-by-day timetable. */
  function weekPlan(H, subs) {
    const total = Math.round(H * 2);
    const review = H >= 8 ? clamp(Math.round(H * 0.16), 2, 6) : 0; // Sunday review ≈ 8 % (1–3 h)
    const study = total - review;
    const units = allocate(study, subs.map((s) => s.w));
    const S = study / 2;
    const active = S <= 6 ? [0, 2, 5] : S <= 10 ? [0, 1, 3, 5] : S <= 14 ? [0, 1, 2, 3, 5] : [0, 1, 2, 3, 4, 5];
    const cap = new Array(7).fill(0);
    allocate(study, active.map((d) => (d === 5 ? 1.5 : 1))).forEach((u, k) => { cap[active[k]] = u; });
    const MAX = 18; // 9 h in one day is plenty
    for (let g = 0; g < 400; g++) {
      let over = -1, best = -1;
      for (let d = 0; d < 6; d++) if (cap[d] > MAX) { over = d; break; }
      if (over < 0) break;
      for (let d = 0; d < 6; d++) if (cap[d] < MAX && (best < 0 || cap[d] < cap[best])) best = d;
      if (best < 0) break;
      cap[over]--; cap[best]++;
    }
    const avg = study / active.length;
    const B = avg >= 10 ? 4 : avg >= 5 ? 3 : 2; // block length: 2 h, 1.5 h or 1 h
    const rem = units.slice();
    const grid = Array.from({ length: 7 }, () => []);
    for (let d = 0; d < 6; d++) {
      let c = cap[d], g = 0;
      while (c > 0 && g++ < 60) {
        const used = new Set(grid[d].map((x) => x.i));
        let k = -1;
        for (let i = 0; i < rem.length; i++) if (rem[i] > 0 && !used.has(i) && (k < 0 || rem[i] > rem[k])) k = i;
        if (k < 0) for (let i = 0; i < rem.length; i++) if (rem[i] > 0 && (k < 0 || rem[i] > rem[k])) k = i;
        if (k < 0) break;
        let put = Math.min(B, c, rem[k]);
        if (rem[k] - put === 1 && c >= put + 1) put++; // no half-hour crumbs of a subject
        else if (c - put === 1 && rem[k] >= put + 1) put++; // no half-hour holes in a day
        const ex = grid[d].find((x) => x.i === k);
        if (ex) ex.u += put; else grid[d].push({ i: k, u: put });
        rem[k] -= put; c -= put;
      }
    }
    return { total, review, study, units, cap, grid };
  }

  /* Optional data attributes (all strings): data-session="mj|on|jan|mj2028", data-subjects="Mathematics,Physics",
     data-level="zero|some|strong", data-aim="full|as", data-hours="20", data-private="1" */
  W.register('planner', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Study-plan generator', 'Your phases, dates and weekly timetable');
    const today = midnight(new Date());
    const SL = sessionList(today);
    const preset = ['session', 'subjects', 'level', 'aim', 'hours', 'private'].map((k) => opts[k] || '').join('|');
    const KEY = 'planner-v1' + (preset.replace(/\|/g, '') ? ':' + preset : ''), TKEY = 'planner-ticks-v1';
    const pickSess = (v) => { const s = v && (SL.find((x) => x.id === v) || SL.find((x) => x.k === v)); return s ? s.id : null; };
    const defSubj = String(opts.subjects || '').split(',').map((x) => x.trim()).filter((n) => SUBJ.some((x) => x.n === n));
    const DEF = {
      sess: pickSess(opts.session) || (SL.find((s) => s.k === 'mj') || SL[0]).id,
      subj: defSubj.length ? defSubj : ['Mathematics', 'Physics', 'Chemistry'],
      level: LEVELS[opts.level] ? opts.level : 'some',
      aim: opts.aim === 'as' ? 'as' : 'full',
      hours: opts.hours && isFinite(+opts.hours) ? clamp(Math.round(+opts.hours), 5, 50) : 20,
      priv: opts.private === '1' || opts.private === 'true'
    };
    const clean = (o) => {
      const s = Object.assign({}, DEF, { subj: DEF.subj.slice() });
      if (!o || typeof o !== 'object') return s;
      if (SL.some((x) => x.id === o.sess)) s.sess = o.sess;
      if (Array.isArray(o.subj)) s.subj = o.subj.filter((n) => SUBJ.some((x) => x.n === n));
      if (LEVELS[o.level]) s.level = o.level;
      if (o.aim === 'as' || o.aim === 'full') s.aim = o.aim;
      if (isFinite(o.hours)) s.hours = clamp(Math.round(o.hours), 5, 50);
      s.priv = o.priv === true;
      return s;
    };
    let st = clean(W.store.get(KEY, null));
    let ticks = W.store.get(TKEY, {});
    if (!ticks || typeof ticks !== 'object' || Array.isArray(ticks)) ticks = {};
    const id = 'st-pl' + (++UID) + '-';

    /* ---------- inputs ---------- */
    const selSess = h('select', { id: id + 's' }, SL.map((s) => h('option', { value: s.id }, s.label)));
    const selLevel = h('select', { id: id + 'l' }, Object.keys(LEVELS).map((k) => h('option', { value: k }, LEVELS[k].label)));
    const selAim = h('select', { id: id + 'a' }, h('option', { value: 'full' }, 'Full A Level'), h('option', { value: 'as' }, 'AS Level only'));
    const ctl = (lab, input, flex) => h('div', { class: 'w-ctl', style: { flex: flex || '1 1 11rem' } }, h('label', { for: input.id }, lab), input);
    const sessHint = small('', { marginTop: '-4px' });

    const chipStyle = (lab, on) => {
      lab.style.background = on ? 'var(--sc-soft)' : 'var(--sheet)';
      lab.style.borderColor = on ? 'var(--sc)' : 'var(--rule)';
      lab.style.fontWeight = on ? '600' : '400';
    };
    const chips = SUBJ.map((s) => {
      const cb = h('input', { type: 'checkbox', value: s.n, id: id + 'c' + s.n.replace(/\W/g, '') });
      const lab = h('label', { for: cb.id, style: { display: 'inline-flex', alignItems: 'center', gap: '6px', padding: '4px 11px 4px 8px', border: '1px solid var(--rule)', borderRadius: '999px', fontSize: '.88rem', cursor: 'pointer', lineHeight: '1.3', userSelect: 'none' } }, cb, s.n);
      cb.addEventListener('change', () => {
        st.subj = SUBJ.filter((x) => chips.find((c) => c.s === x).cb.checked).map((x) => x.n);
        chipStyle(lab, cb.checked);
        render();
      });
      return { s, cb, lab };
    });
    const subjBox = h('fieldset', { style: { border: '0', padding: '0', margin: '0', minWidth: '0' } },
      h('legend', { class: 'w-lab', style: { padding: '0', marginBottom: '6px' } }, 'Subjects'),
      h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '6px' } }, chips.map((c) => c.lab)));

    const hours = W.slider({ label: 'Study hours per week', min: 5, max: 50, step: 1, value: st.hours, fmt: (v) => v + ' h', oninput: (v) => { st.hours = v; render(); } });
    hours.el.style.flex = '2 1 15rem';
    const privCb = h('input', { type: 'checkbox', id: id + 'p' });
    const privLab = h('label', { for: id + 'p', style: { display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '.9rem', cursor: 'pointer', lineHeight: '1.3' } }, privCb, 'Private candidate (no school enters me for exams)');
    const resetBtn = h('button', { type: 'button', class: 'btn btn-sec btn-sm' }, 'Reset to example');

    function syncInputs() {
      selSess.value = st.sess; selLevel.value = st.level; selAim.value = st.aim;
      for (const c of chips) { c.cb.checked = st.subj.includes(c.s.n); chipStyle(c.lab, c.cb.checked); }
      hours.set(st.hours); privCb.checked = st.priv;
    }
    selSess.addEventListener('change', () => { st.sess = selSess.value; render(); });
    selLevel.addEventListener('change', () => { st.level = selLevel.value; render(); });
    selAim.addEventListener('change', () => { st.aim = selAim.value; render(); });
    privCb.addEventListener('change', () => { st.priv = privCb.checked; render(); });
    resetBtn.addEventListener('click', () => { st = clean(null); syncInputs(); render(); });

    body.append(
      h('div', { class: 'w-row' }, ctl('Exam session', selSess, '1 1 12rem'), ctl('Aiming for', selAim, '1 1 9rem'), ctl('Where you are starting', selLevel, '1.5 1 16rem')),
      sessHint,
      subjBox,
      h('div', { class: 'w-row', style: { alignItems: 'center' } }, hours.el, h('div', { style: { flex: '1 1 14rem', display: 'flex', gap: '10px 14px', alignItems: 'center', flexWrap: 'wrap' } }, privLab, resetBtn))
    );

    /* ---------- outputs ---------- */
    const sW = W.stat('Weeks to the exams'), sF = W.stat('First papers ≈'), sH = W.stat('Study time to then'), sL = W.stat('Workload', true);
    const loadB = sL.el.querySelector('b');
    body.append(h('div', { class: 'w-out' }, sW.el, sF.el, sH.el, sL.el));
    const out = h('div', { style: { display: 'grid', gap: '12px', minWidth: '0' } });
    body.append(out);
    body.append(h('div', { class: 'w-note' }, 'Try: drag the hours slider or pick a later session and watch the phases stretch; tick a fourth subject to see the workload change. Exam windows are typical ones: the exact dates come from your board’s published timetable.'));

    let barBlocks = [];
    function fitLabels() {
      for (const b of barBlocks) {
        const w = b.el.clientWidth;
        b.el.textContent = w >= b.full.length * 7.4 + 14 ? b.full : w >= 18 ? b.short : '';
      }
    }
    try { new ResizeObserver(() => requestAnimationFrame(fitLabels)).observe(out); } catch (e) { window.addEventListener('resize', fitLabels); }

    function render() {
      W.store.set(KEY, st);
      out.innerHTML = '';
      barBlocks = [];
      const sess = SL.find((s) => s.id === st.sess) || SL[0];
      sessHint.textContent = sess.note;
      const subs = SUBJ.filter((s) => st.subj.includes(s.n));
      const days = dBetween(today, sess.start);
      const T = days / 7;
      const H = st.hours;
      const yr = today.getFullYear();
      const fdy = (d) => fd(d, d.getFullYear() !== yr);
      sW.set(Math.floor(T) + ' weeks');
      sF.set(fd(sess.start, true));
      sH.set('≈ ' + Math.round(T * H / 10) * 10 + ' h');
      if (!subs.length) {
        sL.set('—'); loadB.style.color = '';
        out.append(h('div', { class: 'w-err' }, 'Tick at least one subject above to build your plan.'));
        return;
      }
      const L = LEVELS[st.level];
      const aimF = st.aim === 'as' ? AS_FACTOR : 1;
      const qual = st.aim === 'as' ? 'AS Level' : 'A Level';
      const n = subs.length;
      const has = (name) => subs.some((s) => s.n === name);
      const hasM = has('Mathematics'), hasFM = has('Further Mathematics');
      const quant = subs.some((s) => s.q), essay = subs.some((s) => s.e), sci = subs.filter((s) => s.sci);

      /* ----- workload check ----- */
      const effH = (x) => (x <= 40 ? x : 40 + (x - 40) * 0.5); // hours beyond ~40 a week add little
      const need = subs.reduce((a, s) => a + L.need * s.w * aimF, 0);
      const avail = T * effH(H);
      const ratio = avail / need;
      let lvl = ratio >= 1 ? 0 : ratio >= 0.75 ? 1 : ratio >= 0.55 ? 2 : ratio >= 0.38 ? 3 : 4;
      const minW = L.minW[st.aim === 'as' ? 1 : 0];
      if (T < minW * 0.6) lvl = Math.max(lvl, 4); else if (T < minW) lvl = Math.max(lvl, 3);
      const LOAD = ['Comfortable', 'Realistic', 'Demanding', 'Tight', 'Very tight'];
      sL.set(LOAD[lvl]);
      loadB.style.color = lvl <= 1 ? 'var(--ok)' : lvl >= 3 ? 'var(--red)' : '';

      const warn = [];
      const rnd10 = (x) => Math.round(x / 10) * 10;
      const plural = (k, w) => k + ' ' + w + (k === 1 ? '' : 's');
      const loadLine = `About ${rnd10(T * H)} h of study before the first paper; ${plural(n, qual)} ${L.short} typically take about ${rnd10(need)} h of self-study.`
        + (H > 40 ? ' Hours beyond about 40 a week count for less: tired study sticks badly.' : '');
      // weekly hours that would make a run-up of t weeks "realistic" (inverse of effH at ratio 0.8)
      const hoursFor = (t) => { const e = need * 0.8 / t; return Math.ceil(e <= 40 ? e : 40 + (e - 40) * 2); };
      if (lvl >= 2) {
        const opts = [];
        const hNeed = hoursFor(T);
        if (T < minW) { /* more hours cannot replace calendar time */ }
        else if (hNeed > H && hNeed <= 50) opts.push(`Study about ${hNeed} h a week instead of ${H} h.`);
        else if (hNeed > 50) opts.push('Even 50 h a week would not be enough before this session.');
        if (n > 1) {
          const per = subs.map((s) => L.need * s.w * aimF).sort((a, b) => a - b);
          let k = 0, acc = 0;
          while (k < per.length && acc + per[k] <= avail / 0.8) { acc += per[k]; k++; }
          if (k < n) opts.push(k > 0 ? `Take fewer subjects this session: about ${plural(k, 'subject')} fit${k === 1 ? 's' : ''} this time.` : 'Take fewer subjects this session.');
        }
        const laterAll = SL.filter((s) => s.start > sess.start && s.k !== 'jan');
        const wks = (s) => dBetween(today, s.start) / 7;
        const later = laterAll.find((s) => wks(s) >= minW && wks(s) * effH(H) >= need * 0.75);
        const laterMore = later ? null : laterAll.find((s) => wks(s) >= minW && hoursFor(wks(s)) <= 50);
        if (later) opts.push(`Aim for a later session: ${later.label} gives about ${Math.floor(wks(later))} weeks.`);
        else if (laterMore) opts.push(`Aim for a later session with more hours: ${laterMore.label} (about ${Math.floor(wks(laterMore))} weeks) at about ${Math.max(H + 1, hoursFor(wks(laterMore)))} h a week.`);
        if (st.aim === 'full' && ratio / AS_FACTOR >= 0.75 && T >= L.minW[1]) opts.push('Sit AS Level first, then complete the A Level in a later session (Cambridge lets you carry an AS result forward for 13 months; Edexcel IAL is modular).');
        else if (st.aim === 'full') opts.push('Consider AS Level first and the full A Level in a later session.');
        const title = lvl === 2 ? 'Demanding, but possible with steady weekly work' : lvl === 3 ? 'Tight: there is not much time for this plan' : 'Very tight: this plan is unlikely to fit the time';
        const calLine = T < minW ? `Learning ${plural(n, qual)} ${L.short} usually takes at least ${minW} weeks, even full-time; you have ${Math.floor(T)}.` : null;
        warn.push(box(lvl === 2 ? 'amber' : 'red', title, [loadLine, calLine], { title: lvl === 2 ? 'To give yourself more slack:' : 'Ways to make it fit:', items: opts }));
      } else {
        warn.push(box('ok', lvl === 0 ? 'Comfortable: you have spare time' : 'Realistic if you study every week', [loadLine + (lvl === 0 ? ' Use the spare time for extra past papers.' : '')]));
      }
      if (hasFM && !hasM) warn.push(box('red', 'Further Mathematics needs Mathematics', ['Further Maths builds on A Level Maths. Tick Mathematics too: most students take both, learning each Maths topic before the Further Maths that uses it.']));
      if (n >= 5) warn.push(box('amber', plural(n, 'subject') + ' is a lot', ['Universities rarely ask for more than three A Levels (four with Further Maths). Fewer subjects at higher grades is the better bet.']));
      else if (n === 4 && !hasFM) warn.push(box('amber', 'Four subjects is a heavy load', ['Most university offers are based on three A Levels. A fourth only helps if it does not pull the other grades down.']));
      const plan = weekPlan(H, subs);
      const minPer = Math.min(...plan.units) / 2;
      if (minPer < 3) warn.push(box('amber', 'Under 3 hours a week for some subjects', [`That is slow progress for an A Level. Add hours or take fewer subjects at once.`]));
      if (H >= 45) warn.push(box('amber', H + ' hours a week is more than a full-time job', ['Keep one rest day and 8 hours of sleep: tired hours add little and burnout costs weeks.']));
      if (sess.k === 'jan') {
        const lines = ['Only Pearson Edexcel IAL runs in January, and not every unit is offered: check the IAL timetable for your subjects.'];
        if (has('Computer Science')) lines.push('Computer Science is not an Edexcel IAL subject (IAL offers Information Technology), so it cannot be sat in January.');
        warn.push(box('amber', 'January series', lines));
      }
      if (st.priv) {
        const left = dBetween(today, sess.start);
        if (left < 120) warn.push(box('red', 'Entries for ' + sess.label + ' may already be closed', ['Private-candidate centres usually close entries 3–4 months before the first paper, sometimes earlier. Ask a centre today; if it is too late, plan for the next session.']));
        if (sci.length) warn.push(box('plain', 'Science practicals for private candidates', ['Cambridge Paper 3 (practical) is sat in a lab, so check that your centre runs it for private candidates. Edexcel IAL tests practical skills in written papers instead.']));
      }
      if (T > 60 && st.aim === 'full' && lvl <= 1) warn.push(box('plain', 'Long run-up: consider splitting', ['You could sit AS Level (or the first IAL units) in an earlier session and finish later: Cambridge lets you carry an AS result forward for 13 months.']));
      out.append(...warn);

      /* ----- phases ----- */
      const wk = phaseWeeks(T, st.level);
      let acc = 0, prev = 0;
      const phases = wk.map((w, i) => {
        acc += w;
        const endD = i === 4 ? days : Math.min(days, Math.round(acc * 7));
        const p = { i, d0: prev, d1: endD, days: endD - prev };
        prev = endD;
        p.start = addDays(today, p.d0); p.end = addDays(today, p.d1 - 1);
        return p;
      });
      phases.push({ i: 5, days: dBetween(sess.start, sess.end) + 1, start: sess.start, end: sess.end });
      const spanDays = dBetween(today, sess.end) + 1;

      out.append(sec('Your timeline', h('span', { class: 'w-lab' }, `${fd(today, true)} → ${fd(sess.end, true)}`)));
      const bar = h('div', { 'aria-hidden': 'true', style: { display: 'flex', height: '36px', borderRadius: '8px', overflow: 'hidden', border: '1px solid var(--rule)' } });
      for (const p of phases) {
        if (p.days <= 0) continue;
        const blk = h('div', { title: `${p.i + 1}. ${PH[p.i].n}: ${fd(p.start)} – ${fd(p.end)}`, style: { flex: `${p.days} 1 0px`, minWidth: '0', background: PH_BG[p.i], color: PH_FG[p.i], display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '.76rem', fontWeight: '700', whiteSpace: 'nowrap', overflow: 'hidden', borderRight: p.i < 5 ? '1px solid var(--sheet)' : '0', fontFamily: 'var(--f-mono)' } }, String(p.i + 1));
        barBlocks.push({ el: blk, full: `${p.i + 1} ${PH[p.i].s}`, short: String(p.i + 1) });
        bar.append(blk);
      }
      // month ticks
      const axis = h('div', { 'aria-hidden': 'true', style: { position: 'relative', height: '30px', fontFamily: 'var(--f-mono)', fontSize: '.7rem', color: 'var(--ink-3)', lineHeight: '1.2' } });
      const months = [];
      for (let m = new Date(today.getFullYear(), today.getMonth() + 1, 1); m <= sess.end; m = new Date(m.getFullYear(), m.getMonth() + 1, 1)) months.push(m);
      const step = Math.max(1, Math.ceil(months.length / 9));
      months.forEach((m, k) => {
        if (k % step) return;
        const pct = dBetween(today, m) / spanDays * 100;
        if (pct < 3 || pct > 97) return;
        axis.append(h('div', { style: { position: 'absolute', left: pct + '%', top: '0', transform: 'translateX(-50%)', textAlign: 'center', whiteSpace: 'nowrap' } },
          h('div', { style: { width: '1px', height: '5px', background: 'var(--ink-3)', margin: '0 auto 1px' } }), MON[m.getMonth()],
          m.getMonth() === 0 ? h('div', { style: { color: 'var(--ink-2)', fontWeight: '600' } }, String(m.getFullYear())) : null));
      });
      out.append(h('div', { style: { display: 'grid', gap: '2px' } }, bar, axis,
        h('div', { style: { display: 'flex', justifyContent: 'space-between', gap: '8px', fontSize: '.78rem', color: 'var(--ink-2)', fontFamily: 'var(--f-mono)' } },
          h('span', {}, 'Today'), h('span', { style: { textAlign: 'right' } }, 'Exams end ≈ ' + fdy(sess.end)))));

      // phase list
      const ppw = Math.max(1, Math.round(H * 0.6 / 3));
      const gaps = [quant && 'algebra, rearranging formulae and units', essay && 'clear, structured paragraphs'].filter(Boolean).join('; ');
      const desc = [
        st.level === 'strong' ? 'Quick check: one diagnostic test per subject, then fix anything shaky.'
          : st.level === 'zero' ? `Build the GCSE-level base first (${gaps}), a little every day.` : `A diagnostic test per subject, then patch the gaps (${gaps}).`,
        'Work through the syllabus in order: notes, worked examples, then 10–20 questions per topic.' + (hasFM && hasM ? ' Start each Further Maths topic once the Maths it uses is done.' : ''),
        'Topic questions and past-paper questions sorted by topic. Keep an error log and flashcards.',
        `Full papers under timed conditions, marked strictly with the mark scheme: about ${plural(ppw, 'paper')} a week.`,
        'Short notes, formula sheets and your error log. A few more timed papers; protect your sleep.',
        'Revise for the next paper only. Check the time, room and your kit the night before.'
      ];
      const plist = h('div', { style: { display: 'grid', gap: '0' } });
      for (const p of phases) {
        const dur = p.days <= 0 ? 'skipped' : p.days < 14 ? plural(p.days, 'day') : '≈ ' + Math.round(p.days / 7) + ' wk';
        const dates = p.days <= 0 ? '—' : (p.i === 5 ? '≈ ' : '') + `${fd(p.start)} – ${fdy(p.end)}`;
        plist.append(h('div', { style: { display: 'grid', gridTemplateColumns: '26px minmax(0, 1fr)', gap: '0 10px', padding: '8px 0', borderBottom: '1px solid var(--rule-2)', opacity: p.days <= 0 ? '.55' : '1' } },
          h('div', { 'aria-hidden': 'true', style: { width: '24px', height: '24px', borderRadius: '6px', background: PH_BG[p.i], color: PH_FG[p.i], display: 'grid', placeItems: 'center', fontFamily: 'var(--f-mono)', fontWeight: '700', fontSize: '.8rem', marginTop: '1px', border: '1px solid var(--rule)' } }, String(p.i + 1)),
          h('div', { style: { minWidth: '0' } },
            h('div', { style: { display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', gap: '0 12px', alignItems: 'baseline' } },
              h('a', { href: '#' + PH[p.i].link, style: { fontWeight: '700', color: 'var(--ink)' } }, `${p.i + 1}. ${PH[p.i].n}`),
              h('span', { style: { fontFamily: 'var(--f-mono)', fontSize: '.8rem', color: 'var(--ink-2)', whiteSpace: 'nowrap' } }, dates + ' · ' + dur)),
            h('div', { style: { fontSize: '.88rem', color: 'var(--ink-2)', lineHeight: '1.45' } }, desc[p.i]))));
      }
      out.append(plist);

      /* ----- hours per subject + weekly timetable ----- */
      const maxU = Math.max(...plan.units);
      const num = { textAlign: 'right', fontFamily: 'var(--f-mono)', whiteSpace: 'nowrap' };
      const htab = h('table', {},
        h('thead', {}, h('tr', {}, h('th', {}, 'Subject'), h('th', { style: { textAlign: 'right' } }, 'h / week'), h('th', { style: { textAlign: 'right' } }, 'By exams'))),
        h('tbody', {},
          subs.map((s, k) => h('tr', {},
            h('td', {}, s.n,
              s.n === 'Further Mathematics' ? h('div', { style: { fontSize: '.76rem', color: 'var(--ink-3)', lineHeight: '1.3' } }, hasM ? 'after the matching Maths topics' : 'needs Mathematics too') : null,
              h('div', { 'aria-hidden': 'true', style: { height: '6px', borderRadius: '3px', background: `var(${s.c})`, width: (plan.units[k] / maxU * 100) + '%', minWidth: '4px', margin: '3px 0 1px' } })),
            h('td', { style: Object.assign({ fontWeight: '600' }, num) }, hrs(plan.units[k])),
            h('td', { style: Object.assign({ color: 'var(--ink-2)' }, num) }, '≈ ' + Math.round(plan.units[k] / 2 * T / 5) * 5 + ' h'))),
          plan.review ? h('tr', {}, h('td', { style: { color: 'var(--ink-2)' } }, 'Weekly review (all subjects)'), h('td', { style: num }, hrs(plan.review)), h('td', { style: Object.assign({ color: 'var(--ink-2)' }, num) }, '≈ ' + Math.round(plan.review / 2 * T / 5) * 5 + ' h')) : null,
          h('tr', {}, h('td', { style: { fontWeight: '700' } }, 'Total'), h('td', { style: Object.assign({ fontWeight: '700' }, num) }, String(H)),
            h('td', { style: Object.assign({ fontWeight: '700' }, num) }, '≈ ' + rnd10(T * H) + ' h'))));

      const chip = (s, u) => h('span', { style: { display: 'inline-flex', alignItems: 'baseline', gap: '4px', padding: '0 6px', margin: '2px 3px 2px 0', borderRadius: '5px', fontSize: '.82rem', lineHeight: '1.6', background: `color-mix(in srgb, var(${s.c}) 14%, var(--sheet))`, borderLeft: `3px solid var(${s.c})`, whiteSpace: 'nowrap' } },
        s.s, h('b', { style: { fontFamily: 'var(--f-mono)', fontWeight: '600', fontSize: '.76rem' } }, hrs(u) + ' h'));
      const ttab = h('table', {},
        h('thead', {}, h('tr', {}, h('th', {}, 'Day'), h('th', {}, 'Study blocks'))),
        h('tbody', {}, DOW.map((dn, d) => {
          let cell, tot;
          if (d === 6) { cell = plan.review ? h('span', { style: { fontSize: '.85rem', color: 'var(--ink-2)' } }, 'Weekly review: flashcards, error log, plan the next week') : h('span', { style: { color: 'var(--ink-3)' } }, 'Rest day'); tot = plan.review; }
          else if (!plan.grid[d].length) { cell = h('span', { style: { color: 'var(--ink-3)' } }, 'Rest day'); tot = 0; }
          else { cell = h('div', {}, plan.grid[d].map((x) => chip(subs[x.i], x.u))); tot = plan.grid[d].reduce((a, x) => a + x.u, 0); }
          return h('tr', {}, h('td', { style: { width: '3.6em', verticalAlign: 'top', whiteSpace: 'nowrap' } }, h('div', { style: { fontWeight: '700' } }, dn),
            h('div', { style: { fontFamily: 'var(--f-mono)', fontSize: '.74rem', color: 'var(--ink-3)' } }, tot ? hrs(tot) + ' h' : '')), h('td', { style: { verticalAlign: 'top' } }, cell));
        })));
      const ppStart = phases[3].days > 0 ? phases[3].start : null;
      out.append(h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '12px 22px', alignItems: 'flex-start' } },
        h('div', { style: { display: 'grid', gap: '8px', minWidth: '0', flex: '1 1 17rem' } }, sec('Hours per subject each week'), htab,
          small('Maths and sciences get a little more time. “By exams” = hours from today to the first paper.')),
        h('div', { style: { display: 'grid', gap: '8px', minWidth: '0', flex: '1.5 1 21rem' } }, sec('A typical week'), ttab,
          small((ppStart ? `From ${fdy(ppStart)} (phase 4), use the Saturday block for one full timed paper. ` : '') + 'Move days around school or work, but keep the weekly total.'))));

      /* ----- milestones ----- */
      const ms = [];
      const add = (d, text, strong, dl) => ms.push({ d, text, strong, dl });
      if (st.priv) add(today, 'Contact an exam centre now — most close entries months before the exams. Ask about fees, deadlines and which papers they run.', true);
      add(today, st.level === 'strong' ? 'Start: a quick diagnostic test in each subject.' : 'Start phase 1: a short diagnostic test in each subject shows your gaps.');
      if (st.priv) {
        const entryBy = addDays(sess.start, -120);
        if (entryBy > today) add(entryBy, 'Have your entry confirmed by about now: many centres close entries 3–4 months before the exams.', true);
      }
      if (phases[0].days > 0 && phases[1].days > 0) add(phases[1].start, 'Foundations checked: start learning the A Level content.');
      if (phases[1].days >= 28) add(addDays(phases[1].start, Math.round(phases[1].days / 2)), 'Halfway through the content: compare progress with this plan and adjust.');
      if (phases[2].days > 0) add(phases[2].start, 'Whole syllabus learned once: switch to mixed topic practice.');
      if (phases[3].days > 0) add(phases[3].start, 'Start timed past papers.', true);
      if (phases[3].days >= 21) add(addDays(phases[3].start, Math.max(7, Math.round(phases[3].days / 3))), 'Mock exams 1: one full set of papers in exam conditions.');
      if (phases[3].days >= 35) add(addDays(phases[4].start, -7), 'Mock exams 2: a second full set; compare with mock 1.');
      const ttCheck = addDays(sess.start, -42);
      if (ttCheck > today) add(ttCheck, 'Check the final timetable and your statement of entry: every paper, time and option.');
      if (phases[4].days > 0) add(phases[4].start, 'Final revision begins.', true);
      add(sess.start, 'First papers (approximate: use your board’s timetable).', true, '≈ ' + fd(sess.start, true));
      add(sess.end, 'Last papers (approximate).', false, '≈ ' + fd(sess.end, true));
      add(sess.results, 'Results day (approximate).', false, sess.rTxt);
      ms.sort((a, b) => a.d - b.d);
      out.append(sec('Milestones'), h('div', { role: 'list' }, ms.map((m) => h('div', { role: 'listitem', style: { display: 'flex', flexWrap: 'wrap', gap: '0 14px', padding: '6px 0', borderBottom: '1px solid var(--rule-2)' } },
        h('div', { style: { flex: '0 0 7.4rem', fontFamily: 'var(--f-mono)', fontSize: '.8rem', paddingTop: '2px', color: m.strong ? 'var(--ink)' : 'var(--ink-2)', fontWeight: m.strong ? '600' : '400' } }, m.dl || fd(m.d, true)),
        h('div', { style: { flex: '1 1 15rem', minWidth: '0', fontSize: '.92rem', lineHeight: '1.45', fontWeight: m.strong ? '600' : '400', color: m.strong && m.d.getTime() === today.getTime() ? 'var(--red)' : 'var(--ink)' } }, m.text)))));

      /* ----- checklist ----- */
      const names = subs.map((s) => s.s);
      const listTxt = names.length > 1 ? names.slice(0, -1).join(', ') + ' and ' + names[names.length - 1] : names[0];
      const items = [
        ['syllabus', `Download the syllabus (specification) for ${listTxt}`],
        ['board', `Confirm the exam board and syllabus code for each subject, and that it runs in ${sess.label.replace(' (Edexcel IAL)', '')}`],
        st.priv && ['centre', 'Find an exam centre that takes private candidates; ask about fees and deadlines'],
        st.priv && ['entry', 'Entry made and confirmed (you have a candidate number)'],
        ['books', 'One main textbook or course for each subject'],
        ['papers', 'Past papers and mark schemes saved (at least the last 5 years)'],
        quant && ['calc', 'An exam-approved scientific calculator that you know well'],
        ['p1', 'Phase 1 done: foundations fixed'],
        ['p2', 'Phase 2 done: whole syllabus learned once'],
        ['p3', 'Phase 3 done: topic questions and an error log'],
        ['mock1', 'Mock exams 1 sat and marked'],
        ['p4', 'Phase 4 done: timed past papers'],
        ['mock2', 'Mock exams 2 sat and marked'],
        ['timetable', 'Exam timetable and statement of entry checked'],
        ['kit', 'Exam-day kit ready: photo ID, black pens, pencil, ruler, calculator']
      ].filter(Boolean);
      const done = items.filter((it) => ticks[it[0]]).length;
      const prog = h('span', { class: 'w-lab' }, `${done} of ${items.length} done`);
      const listEl = h('div', { style: { display: 'grid', gap: '0 22px', gridTemplateColumns: 'repeat(auto-fill, minmax(min(100%, 19rem), 1fr))' } });
      for (const [k, txt] of items) {
        const cb = h('input', { type: 'checkbox', id: id + 'k' + k });
        cb.checked = !!ticks[k];
        const span = h('span', {}, txt);
        const style = () => { span.style.textDecoration = cb.checked ? 'line-through' : 'none'; span.style.color = cb.checked ? 'var(--ink-3)' : 'var(--ink)'; };
        style();
        cb.addEventListener('change', () => {
          if (cb.checked) ticks[k] = 1; else delete ticks[k];
          W.store.set(TKEY, ticks); style();
          prog.textContent = `${items.filter((it) => ticks[it[0]]).length} of ${items.length} done`;
        });
        listEl.append(h('label', { for: cb.id, style: { display: 'flex', gap: '10px', alignItems: 'flex-start', padding: '4px 0', cursor: 'pointer', fontSize: '.92rem', lineHeight: '1.4' } }, h('span', { style: { paddingTop: '2px', flex: 'none', display: 'flex' } }, cb), span));
      }
      out.append(sec('Checklist (saved on this device)', prog), listEl);
      requestAnimationFrame(fitLabels);
    }

    syncInputs();
    render();
  });

  /* =====================================================================
     2. timer — Pomodoro study timer
     ===================================================================== */
  const SR_ONLY = { position: 'absolute', width: '1px', height: '1px', overflow: 'hidden', clip: 'rect(0 0 0 0)', whiteSpace: 'nowrap', margin: '-1px', padding: '0', border: '0' };
  const clock = (s) => {
    const p = (x) => String(x).padStart(2, '0');
    const hh = Math.floor(s / 3600), mm = Math.floor((s % 3600) / 60), ss = s % 60;
    return hh ? `${hh}:${p(mm)}:${p(ss)}` : `${p(mm)}:${p(ss)}`;
  };

  W.register('timer', function (el) {
    const { body } = W.frame(el, 'Study timer', 'Focus, short break, repeat');
    const id = 'st-tm' + (++UID) + '-';
    const PRE = { a: [25, 5], b: [50, 10] };
    let custom = W.store.get('timer-custom', [40, 8]);
    if (!Array.isArray(custom) || custom.length !== 2 || !custom.every((x) => Number.isFinite(x) && x >= 1 && x <= 180)) custom = [40, 8];
    let cfg = PRE.a.slice();
    let phase = 'focus', running = false, started = false, invalid = false;
    let total = cfg[0] * 60000, remaining = total, endAt = 0, timerH = 0;
    const dayKey = () => { const d = new Date(); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); };
    let day = W.store.get('timer-day', null);
    const freshDay = () => { if (!day || typeof day !== 'object' || day.d !== dayKey() || !Number.isFinite(day.n) || !Number.isFinite(day.m)) day = { d: dayKey(), n: 0, m: 0 }; };
    freshDay();

    /* mode tabs + custom lengths */
    const MODES = [['a', '25 / 5'], ['b', '50 / 10'], ['c', 'Custom']];
    const tabBtns = MODES.map(([k, t]) => h('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false', onclick: () => setMode(k) }, t + (k === 'c' ? '' : ' min')));
    const tabs = h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Focus and break lengths' }, tabBtns);
    const fF = W.field({ label: 'Focus (minutes)', value: custom[0], step: 1, oninput: onCustom, width: '9rem' });
    const fB = W.field({ label: 'Break (minutes)', value: custom[1], step: 1, oninput: onCustom, width: '9rem' });
    fF.input.min = 1; fF.input.max = 180; fB.input.min = 1; fB.input.max = 60;
    const err = h('div', { class: 'w-err', role: 'alert' });
    const customRow = h('div', { class: 'w-row', style: { display: 'none' } }, fF.el, fB.el);

    /* progress ring */
    const R = 88, C = 2 * Math.PI * R;
    const ring = h('div', { html: `<svg viewBox="0 0 200 200" width="100%" height="100%" aria-hidden="true" style="display:block">
      <circle cx="100" cy="100" r="${R}" fill="none" stroke-width="11" style="stroke:var(--rule)"></circle>
      <circle class="tm-p" cx="100" cy="100" r="${R}" fill="none" stroke-width="11" stroke-linecap="round" transform="rotate(-90 100 100)" stroke-dasharray="${C.toFixed(2)}" stroke-dashoffset="${C.toFixed(2)}" style="stroke:var(--sc)"></circle></svg>`,
      style: { position: 'absolute', inset: '0' } });
    const prog = ring.querySelector('.tm-p');
    if (!reduced()) prog.style.transition = 'stroke-dashoffset .3s linear';
    const phaseLab = h('div', { style: { fontFamily: 'var(--f-mono)', fontSize: '.74rem', letterSpacing: '.12em', textTransform: 'uppercase', fontWeight: '700' } });
    const timeEl = h('div', { role: 'timer', 'aria-live': 'off', style: { fontFamily: 'var(--f-mono)', fontSize: '2.7rem', fontWeight: '600', lineHeight: '1.05', fontVariantNumeric: 'tabular-nums', color: 'var(--ink)', letterSpacing: '-.02em' } });
    const subLab = h('div', { style: { fontSize: '.8rem', color: 'var(--ink-3)' } });
    const dial = h('div', { style: { position: 'relative', width: '220px', height: '220px', maxWidth: '100%', flex: 'none', margin: '0 auto' } }, ring,
      h('div', { style: { position: 'absolute', inset: '0', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '3px', textAlign: 'center' } }, phaseLab, timeEl, subLab));

    /* buttons, sound, stats */
    const startBtn = h('button', { type: 'button', class: 'btn', style: { minWidth: '6.5rem', justifyContent: 'center' } }, 'Start');
    const resetBtn = h('button', { type: 'button', class: 'btn btn-sec' }, 'Reset');
    const soundCb = h('input', { type: 'checkbox', id: id + 'snd' });
    soundCb.checked = W.store.get('timer-sound', true) !== false;
    const soundLab = h('label', { for: id + 'snd', style: { display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '.9rem', cursor: 'pointer' } }, soundCb, 'Soft beep when time is up');
    const status = h('div', { style: { fontSize: '.95rem', color: 'var(--ink)', lineHeight: '1.45', minHeight: '2.9em' } });
    const pending = small('');
    const sN = W.stat('Focus sessions today', true), sM = W.stat('Focus time today'), sNext = W.stat('Up next');
    const clearBtn = h('button', { type: 'button', style: { background: 'none', border: '0', padding: '2px 0', color: 'var(--ink-2)', textDecoration: 'underline', textUnderlineOffset: '3px', cursor: 'pointer', fontSize: '.82rem', fontFamily: 'inherit' } }, 'Clear today’s count');
    const live = h('div', { 'aria-live': 'polite', style: SR_ONLY });

    body.append(tabs, customRow, err,
      h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '16px 30px', alignItems: 'center' } }, dial,
        h('div', { style: { flex: '1 1 16rem', minWidth: '0', display: 'grid', gap: '12px' } },
          h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '10px 14px', alignItems: 'center' } }, startBtn, resetBtn, soundLab),
          status, pending,
          h('div', { class: 'w-out' }, sN.el, sM.el, sNext.el),
          h('div', {}, clearBtn))),
      live,
      h('div', { class: 'w-note' }, 'Try: press Start and work on one task until the ring closes, then take the break away from your screen. After four sessions, take a longer 15–30 minute break. The beep only plays after you have pressed a button.'));

    /* sound (WebAudio, created only inside a click handler) */
    let actx = null;
    function ensureAudio() {
      if (!soundCb.checked) return;
      try {
        if (!actx) { const AC = window.AudioContext || window.webkitAudioContext; if (AC) actx = new AC(); }
        if (actx && actx.state === 'suspended') actx.resume();
      } catch (e) { actx = null; }
    }
    function beep(up) {
      if (!soundCb.checked || !actx) return;
      try {
        const t0 = actx.currentTime + 0.03;
        (up ? [660, 880] : [880, 660]).forEach((f, i) => {
          const o = actx.createOscillator(), g = actx.createGain(), s = t0 + i * 0.3;
          o.type = 'sine'; o.frequency.value = f;
          g.gain.setValueAtTime(0.0001, s);
          g.gain.exponentialRampToValueAtTime(0.12, s + 0.04);
          g.gain.exponentialRampToValueAtTime(0.0001, s + 0.26);
          o.connect(g); g.connect(actx.destination);
          o.start(s); o.stop(s + 0.3);
        });
      } catch (e) { /* audio is optional */ }
    }

    /* timing (based on the clock, not on counting ticks, so it stays right in background tabs) */
    const left = () => (running ? Math.max(0, endAt - Date.now()) : remaining);
    function update() {
      const rem = left();
      timeEl.textContent = clock(Math.ceil(rem / 1000));
      const frac = total > 0 ? clamp(1 - rem / total, 0, 1) : 0;
      prog.style.strokeDashoffset = (C * (1 - frac)).toFixed(2);
      prog.style.opacity = frac > 0.003 ? '1' : '0';
      const col = phase === 'focus' ? 'var(--sc)' : 'var(--ok)';
      prog.style.stroke = col; phaseLab.style.color = col;
      phaseLab.textContent = phase === 'focus' ? 'Focus' : 'Break';
      subLab.textContent = phase === 'focus' ? `Session ${day.n + 1} today` : `${Math.round(total / 60000)} min break`;
      startBtn.textContent = running ? 'Pause' : started ? 'Resume' : 'Start';
      startBtn.disabled = invalid && !started;
      const longBreak = phase === 'break' && day.n > 0 && day.n % 4 === 0;
      status.textContent = !started ? (phase === 'focus' ? 'Ready. Pick one task, put your phone in another room, press Start.' : 'Break ready.')
        : !running ? 'Paused. Press Resume to carry on.'
          : phase === 'focus' ? 'Focus: one task only. If a thought pops up, jot it down and carry on.'
            : longBreak ? 'Four sessions done: take a longer break (15–30 min) away from the screen.' : 'Break: stand up, stretch, drink some water. No scrolling.';
      sN.set(String(day.n));
      sM.set(day.m >= 60 ? `${Math.floor(day.m / 60)} h ${day.m % 60} min` : `${day.m} min`);
      sNext.set(phase === 'focus' ? `${cfg[1]} min break` : `${cfg[0]} min focus`);
    }
    function complete(at) {
      freshDay();
      pending.textContent = '';
      if (phase === 'focus') {
        day.n++; day.m += Math.round(total / 60000); W.store.set('timer-day', day);
        beep(true);
        live.textContent = `Focus session ${day.n} done. Break time.`;
        phase = 'break'; total = cfg[1] * 60000; endAt = at + total; // the break starts by itself
      } else {
        beep(false);
        live.textContent = 'Break over. Press Start for the next focus session.';
        phase = 'focus'; total = remaining = cfg[0] * 60000;
        running = false; started = false; clearInterval(timerH);
      }
    }
    function tick() {
      if (!el.isConnected) { clearInterval(timerH); running = false; return; }
      if (running) { let g = 0; while (running && Date.now() >= endAt && g++ < 6) complete(endAt); }
      update();
    }
    function start() {
      if (running || (invalid && !started)) return;
      ensureAudio();
      running = true; started = true;
      endAt = Date.now() + remaining;
      clearInterval(timerH); timerH = setInterval(tick, 250);
      live.textContent = phase === 'focus' ? 'Focus started.' : 'Break started.';
      update();
    }
    function pause() {
      if (!running) return;
      remaining = left(); running = false; clearInterval(timerH);
      live.textContent = 'Paused.';
      update();
    }
    function reset() {
      running = false; started = false; clearInterval(timerH);
      phase = 'focus'; total = remaining = cfg[0] * 60000; pending.textContent = '';
      update();
    }
    function setCfg(c) {
      cfg = c;
      if (!started) { phase = 'focus'; total = remaining = cfg[0] * 60000; pending.textContent = ''; }
      else pending.textContent = 'New lengths start with the next focus or break. Press Reset to use them now.';
      update();
    }
    function onCustom() {
      const a = fF.input.value.trim(), b = fB.input.value.trim();
      const f = Number(a), br = Number(b);
      invalid = !(a !== '' && b !== '' && Number.isInteger(f) && Number.isInteger(br) && f >= 1 && f <= 180 && br >= 1 && br <= 60);
      err.textContent = invalid ? 'Enter whole minutes: focus 1–180 and break 1–60.' : '';
      if (invalid) { update(); return; }
      custom = [f, br]; W.store.set('timer-custom', custom);
      setCfg(custom.slice());
    }
    function setMode(k) {
      tabBtns.forEach((b, i) => b.setAttribute('aria-pressed', String(MODES[i][0] === k)));
      customRow.style.display = k === 'c' ? '' : 'none';
      W.store.set('timer-mode', k);
      if (k === 'c') onCustom();
      else { invalid = false; err.textContent = ''; setCfg(PRE[k].slice()); }
    }

    startBtn.addEventListener('click', () => { if (running) pause(); else start(); });
    resetBtn.addEventListener('click', reset);
    soundCb.addEventListener('change', () => { W.store.set('timer-sound', soundCb.checked); if (soundCb.checked) { ensureAudio(); beep(true); } });
    clearBtn.addEventListener('click', () => { day = { d: dayKey(), n: 0, m: 0 }; W.store.set('timer-day', day); update(); });
    document.addEventListener('visibilitychange', () => { if (running) tick(); });

    const m0 = W.store.get('timer-mode', 'a');
    setMode(MODES.some((m) => m[0] === m0) ? m0 : 'a');
  });

  /* =====================================================================
     3. ucas — UCAS tariff points calculator
     ===================================================================== */
  const TARIFF = {
    al: { label: 'A Level', grades: [['A*', 56], ['A', 48], ['B', 40], ['C', 32], ['D', 24], ['E', 16]] },
    as: { label: 'AS Level', grades: [['a', 20], ['b', 16], ['c', 12], ['d', 10], ['e', 6]] },
    epq: { label: 'EPQ', grades: [['A*', 28], ['A', 24], ['B', 20], ['C', 16], ['D', 12], ['E', 8]] }
  };
  const ROW_GRADES = ['A*', 'A', 'B', 'C', 'D', 'E'];
  const MAX_ROWS = 5;

  /* Optional: data-grades="A*,A,A" (A Levels) — the default example is A*AA = 152 points. */
  W.register('ucas', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'UCAS tariff calculator', 'Turn your grades into UCAS points');
    const id = 'st-uc' + (++UID) + '-';
    let n = 0;
    const start = String(opts.grades || 'A*,A,A').split(',').map((g) => g.trim().toUpperCase()).filter((g) => ROW_GRADES.includes(g)).slice(0, MAX_ROWS);
    const rows = [];
    const list = h('div', { style: { display: 'grid', gap: '8px' } });
    const head = h('div', { 'aria-hidden': 'true', style: { display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) 5.2rem 3.6rem 2.4rem', gap: '8px', fontFamily: 'var(--f-mono)', fontSize: '.7rem', textTransform: 'uppercase', letterSpacing: '.06em', color: 'var(--ink-3)' } },
      h('span', {}, 'Qualification'), h('span', {}, 'Grade'), h('span', { style: { textAlign: 'right' } }, 'Points'), h('span', {}));
    const addBtn = h('button', { type: 'button', class: 'btn btn-sec btn-sm' }, '+ Add a qualification');
    const sTot = W.stat('Total UCAS points', true), sProf = W.stat('Grades');
    const sum = h('div', { style: { fontFamily: 'var(--f-mono)', fontSize: '.85rem', color: 'var(--ink-2)', overflowWrap: 'anywhere' } });
    const msg = h('div', { class: 'w-err', role: 'status' });

    function addRow(q, g) {
      if (rows.length >= MAX_ROWS) return;
      const k = ++n;
      const qSel = h('select', { id: id + 'q' + k, 'aria-label': 'Qualification' }, Object.keys(TARIFF).map((key) => h('option', { value: key }, TARIFF[key].label)));
      const gSel = h('select', { id: id + 'g' + k, 'aria-label': 'Grade' });
      const pts = h('output', { for: gSel.id, style: { textAlign: 'right', fontFamily: 'var(--f-mono)', fontWeight: '600', fontSize: '.95rem' } });
      const rm = h('button', { type: 'button', class: 'btn btn-sec btn-sm', style: { padding: '6px 0', justifyContent: 'center' }, 'aria-label': 'Remove this qualification', title: 'Remove' }, '×');
      const fillGrades = (keep) => {
        gSel.innerHTML = '';
        for (const [gr, p] of TARIFF[qSel.value].grades) gSel.append(h('option', { value: gr }, `${gr} (${p})`));
        const want = TARIFF[qSel.value].grades.find(([gr]) => gr.toUpperCase() === String(keep || '').toUpperCase());
        gSel.value = want ? want[0] : TARIFF[qSel.value].grades[qSel.value === 'as' ? 0 : 1][0];
      };
      qSel.value = TARIFF[q] ? q : 'al';
      fillGrades(g);
      const row = { qSel, gSel, pts, rm, el: null };
      row.el = h('div', { style: { display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) 5.2rem 3.6rem 2.4rem', gap: '8px', alignItems: 'center' } }, qSel, gSel, pts, rm);
      qSel.addEventListener('change', () => { fillGrades(gSel.value); update(); });
      gSel.addEventListener('change', update);
      rm.addEventListener('click', () => {
        if (rows.length <= 1) return;
        const i = rows.indexOf(row);
        rows.splice(i, 1); row.el.remove();
        update();
        // the last row's remove button is disabled, so focus its qualification instead
        rows[Math.min(i, rows.length - 1)][rows.length > 1 ? 'rm' : 'qSel'].focus();
      });
      rows.push(row); list.append(row.el);
    }

    function update() {
      let total = 0;
      const al = [], as = [], ep = [], parts = [];
      for (const [i, r] of rows.entries()) {
        r.qSel.setAttribute('aria-label', 'Qualification ' + (i + 1)); r.gSel.setAttribute('aria-label', 'Grade ' + (i + 1));
        r.rm.setAttribute('aria-label', 'Remove qualification ' + (i + 1));
        const g = TARIFF[r.qSel.value].grades.find(([gr]) => gr === r.gSel.value);
        const p = g ? g[1] : 0;
        r.pts.textContent = String(p);
        total += p; parts.push(p);
        (r.qSel.value === 'al' ? al : r.qSel.value === 'as' ? as : ep).push(r.gSel.value);
        r.rm.disabled = rows.length <= 1;
      }
      const ord = (a) => a.slice().sort((x, y) => ROW_GRADES.indexOf(x.toUpperCase()) - ROW_GRADES.indexOf(y.toUpperCase()));
      const prof = [ord(al).join(''), as.length ? 'AS ' + ord(as).join('') : '', ep.length ? 'EPQ ' + ep.join(', ') : ''].filter(Boolean).join(' + ');
      sTot.set(total + ' points');
      sProf.set(prof || '—');
      sum.textContent = parts.join(' + ') + ' = ' + total;
      addBtn.disabled = rows.length >= MAX_ROWS;
      msg.textContent = ep.length > 1 ? 'Only one EPQ counts: you can take the Extended Project once.' : '';
      for (const td of refCells) td.cell.style.background = rows.some((r) => r.qSel.value === td.q && r.gSel.value === td.g) ? 'var(--hl-soft)' : '';
    }

    /* reference table */
    const refCells = [];
    const cell = (q, gr) => {
      const g = TARIFF[q].grades.find(([x]) => x.toUpperCase() === gr);
      const td = h('td', { style: { textAlign: 'right', fontFamily: 'var(--f-mono)' } }, g ? String(g[1]) : '—');
      if (g) refCells.push({ cell: td, q, g: g[0] });
      return td;
    };
    const ref = h('table', {},
      h('thead', {}, h('tr', {}, h('th', {}, 'Grade'), h('th', { style: { textAlign: 'right' } }, 'A Level'), h('th', { style: { textAlign: 'right' } }, 'AS Level'), h('th', { style: { textAlign: 'right' } }, 'EPQ'))),
      h('tbody', {}, ROW_GRADES.map((gr) => h('tr', {}, h('td', { style: { fontWeight: '700' } }, gr === 'A*' ? 'A*' : `${gr} / ${gr.toLowerCase()}`), cell('al', gr), cell('as', gr), cell('epq', gr)))));

    addBtn.addEventListener('click', () => { addRow('al', 'B'); update(); rows[rows.length - 1].qSel.focus(); });
    (start.length ? start : ['A*', 'A', 'A']).forEach((g) => addRow('al', g));

    body.append(head, list,
      h('div', { class: 'w-row', style: { alignItems: 'center' } }, addBtn, small('Up to five qualifications.')),
      msg,
      h('div', { class: 'w-out' }, sTot.el, sProf.el),
      sum,
      sec('Tariff points'),
      h('div', { style: { overflowX: 'auto' } }, ref),
      small('Example: A*AA = 56 + 48 + 48 = 152 points. AS grades are written a–e by Cambridge and A–E by UK boards; the EPQ (Extended Project) is a UK qualification.'),
      h('div', { class: 'w-note' }, 'Try: change one grade at a time and watch the total. Many offers are made in grades (such as AAA) rather than points, and an AS does not add points if you go on to the full A Level in the same subject.'));
    update();
  });
})();
