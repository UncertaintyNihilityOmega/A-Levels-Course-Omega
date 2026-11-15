/* app.js — router, navigation, progress, search, quizzes, glossary, practice */
(function () {
  'use strict';
  const G = window.GUIDE || { order: [], ch: {}, subjects: [] };
  const QUIZ = window.QUIZ = window.QUIZ || {};   // index -> question; course chunks add theirs
  const quizIds = () => Object.keys(QUIZ).map(Number).sort((a, b) => a - b);
  const GLOSS = window.GLOSSARY = window.GLOSSARY || [];
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const root = document.documentElement;
  const app = $('#app');
  const store = W.store;

  /* ---------- theme & text size ---------- */
  const savedTheme = store.get('theme', null);
  if (savedTheme) root.setAttribute('data-theme', savedTheme);
  const savedSize = store.get('size', null);
  if (savedSize) root.setAttribute('data-size', savedSize);
  // reading font ('sans', default serif) and animations ('off', default: follow the device), from Settings
  if (store.get('font', null) === 'sans') root.setAttribute('data-font', 'sans');
  if (store.get('motion', null) === 'off') root.setAttribute('data-motion', 'off');
  function effectiveDark() {
    const t = root.getAttribute('data-theme');
    if (t) return t === 'dark';
    try { return window.matchMedia('(prefers-color-scheme: dark)').matches; } catch (e) { return false; }
  }
  function syncThemeIcon() {
    if (!root.getAttribute('data-theme')) root.setAttribute('data-theme-auto', effectiveDark() ? 'dark' : 'light');
    $('#themeBtn').setAttribute('aria-pressed', effectiveDark() ? 'true' : 'false');
  }
  /** theme: 'light', 'dark' or null (follow the system) */
  function setTheme(next, quiet) {
    if (next) root.setAttribute('data-theme', next); else root.removeAttribute('data-theme');
    store.set('theme', next);
    syncThemeIcon();
    if (!quiet) toast(next === 'dark' ? 'Chalkboard mode' : next === 'light' ? 'Paper mode' : 'Follows your device');
    setTimeout(W.themeChanged, 30);
  }
  $('#themeBtn').addEventListener('click', () => setTheme(effectiveDark() ? 'light' : 'dark'));
  try { window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', syncThemeIcon); } catch (e) { /* old browsers */ }
  /** text size: 'm', 'l' or 'xl' */
  function setSize(next, quiet) {
    if (next === 'm') root.removeAttribute('data-size'); else root.setAttribute('data-size', next);
    store.set('size', next === 'm' ? null : next);
    if (!quiet) toast({ m: 'Text size: normal', l: 'Text size: large', xl: 'Text size: extra large' }[next]);
    setTimeout(W.themeChanged, 30);
    setTimeout(() => { if (current) markScrollers(current); }, 60);
  }
  $('#textBtn').addEventListener('click', () => {
    const cur = root.getAttribute('data-size') || 'm';
    setSize(cur === 'm' ? 'l' : cur === 'l' ? 'xl' : 'm');
  });
  syncThemeIcon();

  let toastT = 0;
  function toast(msg) {
    const t = $('#toast');
    t.textContent = msg; t.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(() => { t.hidden = true; }, 1800);
    say(msg);
  }
  // the toast is hidden from screen readers; this always-present status region reads the message instead
  let sayT = 0;
  function say(msg) {
    const a = $('#announce');
    a.textContent = '';
    clearTimeout(sayT); sayT = setTimeout(() => { a.textContent = msg; }, 60);
  }
  /** Move keyboard and screen-reader focus to an element that is not a control (a heading, a section). */
  function focusOn(el) {
    if (!el) return;
    if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1');
    el.focus({ preventScroll: true });
  }

  /* ---------- progress ---------- */
  let done = store.get('done', {});
  const trackable = new Set(G.order.filter(id => G.ch[id].f));
  function saveDone() { store.set('done', done); }
  /* spaced re-testing: a learned chapter's quiz questions come back 1, 3, 7 and 21 days after it was marked as learned.
     retest[chapter] = how many of those re-tests are behind the reader (done, or skipped because a later one was due) */
  const RT_DAYS = [1, 3, 7, 21], DAY = 864e5;
  const retest = store.get('retest', {});
  function retestOf(c, now) {
    const t0 = done[c], info = G.ch[c];
    if (!info || !info.q || typeof t0 !== 'number' || t0 < 1e12) return null;
    const n = retest[c] || 0;
    if (n >= RT_DAYS.length) return null;
    return { c, n, due: t0 + RT_DAYS[n] * DAY, isDue: now >= t0 + RT_DAYS[n] * DAY };
  }
  const retestsDue = (now) => Object.keys(done).map(c => retestOf(c, now)).filter(r => r && r.isDue).sort((a, b) => a.due - b.due);
  function subjectStats(sid) {
    let n = 0, d = 0;
    for (const id of G.order) { if (G.ch[id].s === sid && trackable.has(id)) { n++; if (done[id]) d++; } }
    return { n, d };
  }
  function renderProgress() {
    for (const a of $$('.nav-g a[data-nav]')) {
      const on = !!done[a.getAttribute('data-nav')], sr = $('.nav-sr', a);
      a.classList.toggle('done', on);
      if (on && !sr) a.append(W.h('span', { class: 'sr-only nav-sr' }, ' (learned)'));
      else if (!on && sr) sr.remove();
    }
    for (const b of $$('[data-done]')) {
      const on = !!done[b.getAttribute('data-done')];
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      $('.done-txt', b).textContent = on ? 'Learned — nice work' : 'Mark as learned';
    }
    let tn = 0, td = 0;
    for (const s of G.subjects) {
      const { n, d } = subjectStats(s.id);
      tn += n; td += d;
      for (const el of $$(`[data-pc="${s.id}"]`)) el.textContent = n ? `${d}/${n}` : '';
      for (const el of $$(`[data-bar="${s.id}"]`)) el.style.width = n ? (100 * d / n).toFixed(1) + '%' : '0';
      for (const el of $$(`[data-cnt="${s.id}"]`)) el.textContent = n ? `${d} of ${n} learned` : 'Coming soon';
    }
    $('#sideProgTxt').textContent = `${td} of ${tn} chapters learned`;
    $('#sideProgBar').style.width = tn ? (100 * td / tn).toFixed(1) + '%' : '0';
  }
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-done]');
    if (!b) return;
    const id = b.getAttribute('data-done');
    if (done[id]) delete done[id]; else { done[id] = Date.now(); toast('Marked as learned'); }
    // the re-test dates count from the day a chapter is marked as learned: marking it again starts them again
    if (retest[id] != null) { delete retest[id]; store.set('retest', retest); }
    saveDone(); renderProgress();
  });

  /* ---------- checklists: ticks saved per viewer, rolled up by :::progress ---------- */
  const ticks = store.get('ticks', {});
  function renderTicks(scope) {
    for (const cb of $$('input[data-ck]', scope)) cb.checked = !!ticks[cb.getAttribute('data-ck')];
    for (const el of $$('[data-clp]', scope)) {
      const keys = el.getAttribute('data-clp').split(',').filter(Boolean);
      const d = keys.filter(k => ticks[k]).length, n = keys.length;
      const out = el.classList.contains('cl-n') ? el : $('.clp-n', el);
      if (out) out.textContent = n ? `${d} of ${n}` : '';
      el.style.setProperty('--p', n ? (100 * d / n).toFixed(1) + '%' : '0%');
      el.classList.toggle('all', n > 0 && d === n);
    }
  }
  document.addEventListener('change', (e) => {
    const cb = e.target.closest && e.target.closest('input[data-ck]');
    if (!cb) return;
    const k = cb.getAttribute('data-ck');
    if (cb.checked) ticks[k] = 1; else delete ticks[k];
    store.set('ticks', ticks);
    renderTicks(document);
  });

  /* ---------- mock papers: clock, answers hidden until Finish, self-marking ---------- */
  function initMock(art) {
    const id = art.getAttribute('data-id'), total = +art.getAttribute('data-marks') || 0, mins = +art.getAttribute('data-min') || 0;
    const answer = +art.getAttribute('data-answer') || 0;   // a paper with a choice: the reader answers this many questions
    const key = 'mock:' + id;
    let S = store.get(key, null) || { start: 0, spent: 0, done: false, marks: {} };
    const save = () => store.set(key, S);
    const qs = $$('.try-mock .try-list > li', art);
    const prose = $('.prose', art);
    const clock = W.h('b', { class: 'mock-clock', 'aria-live': 'off' });
    const clockLab = W.h('span', { class: 'mock-k' }, mins ? 'Time left' : 'Time');
    const runBtn = W.h('button', { class: 'btn btn-sm', type: 'button' });
    const finBtn = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button' }, 'Finish and mark');
    const score = W.h('span', { class: 'mock-score' });
    const note = W.h('span', { class: 'mock-note' });
    const againBtn = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button' }, 'Start again');
    const bar = W.h('div', { class: 'mock-bar', role: 'region', 'aria-label': 'Mock paper controls' },
      W.h('span', { class: 'mock-time' }, clockLab, clock), runBtn, finBtn, score, againBtn, note);
    prose.prepend(bar);
    const rev = W.h('div', { class: 'mock-rev' });
    prose.append(rev);
    let warned = false, confirmT = 0, iv = 0;
    const elapsed = () => S.spent + (S.start ? Date.now() - S.start : 0);
    const hms = (ms) => { const s = Math.floor(Math.abs(ms) / 1000); return `${Math.floor(s / 3600)}:${String(Math.floor(s / 60) % 60).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`; };
    function tick() {
      const e = elapsed(), left = mins * 60000 - e;
      clockLab.textContent = S.done ? 'Time taken' : mins ? 'Time left' : 'Time';
      if (!mins || S.done) clock.textContent = hms(e);
      else if (left >= 0) clock.textContent = hms(left);
      else clock.textContent = '+' + hms(left);
      bar.classList.toggle('over', !!mins && left < 0);
      if (mins && left < 0 && !warned && S.start && !art.hidden) { warned = true; toast('Time is up. Finish the question you are on, then mark the paper.'); }
    }
    function marksInputs() {
      for (const [i, li] of qs.entries()) {
        let box = $('.mock-mark', li);
        if (!S.done) { if (box) box.remove(); continue; }
        const n = +li.getAttribute('data-marks') || 0;
        if (box || !n) continue;
        const inp = W.h('input', { type: 'number', min: 0, max: n, step: 1, inputmode: 'numeric', 'aria-label': `Your mark for question ${i + 1}, out of ${n}` });
        if (S.marks[i] != null) inp.value = S.marks[i];
        inp.addEventListener('input', () => {
          const v = Math.max(0, Math.min(n, Math.round(+inp.value)));
          if (inp.value === '' || !isFinite(+inp.value)) delete S.marks[i]; else S.marks[i] = v;
          save(); summary();
        });
        // show the mark that counts: a number above the maximum (or below 0) is put back in range when the field is left
        inp.addEventListener('change', () => { if (S.marks[i] != null && +inp.value !== S.marks[i]) inp.value = S.marks[i]; });
        box = W.h('label', { class: 'mock-mark' }, W.h('span', {}, 'Your mark'), inp, W.h('span', {}, `out of ${n}`));
        li.append(box);
      }
    }
    function summary() {
      // with a choice of questions, the best `answer` marks count (a reader who marks extra questions cannot pass the total)
      const got = Object.values(S.marks).sort((a, b) => b - a).slice(0, answer || Infinity).reduce((a, b) => a + b, 0);
      const marked = Object.keys(S.marks).length;
      score.textContent = S.done ? `${got} / ${total}${total ? ` · ${Math.round(100 * got / total)}%` : ''}` : '';
      const weak = qs.map((li, i) => ({ li, i, n: +li.getAttribute('data-marks') || 0, m: S.marks[i] })).filter(q => q.m != null && q.m < q.n / 2);
      rev.innerHTML = '';
      if (!S.done) return;
      const need = answer || qs.filter(li => +li.getAttribute('data-marks')).length;
      if (marked < need) { rev.append(W.h('p', { class: 'mock-note' }, answer ? `Mark the ${answer === 1 ? 'question' : answer + ' questions'} you answered against the mark scheme to see what to revise.` : 'Mark every question against the mark scheme to see what to revise.')); return; }
      if (!weak.length) { rev.append(W.h('p', {}, W.h('b', {}, 'No weak questions.'), ' Every question earned at least half its marks.')); return; }
      rev.append(W.h('h3', {}, 'Revise these next'));
      const ul = W.h('ul', {});
      for (const q of weak) {
        const a = $('.ta-rev a', q.li);
        ul.append(W.h('li', {}, `Question ${q.i + 1} (${q.m} of ${q.n}): `, a ? W.h('a', { href: a.getAttribute('href') }, a.textContent.replace(/^Revise:\s*/, '')) : 'see the mark scheme'));
      }
      rev.append(ul);
      if (G.ch['practice.next']) rev.append(W.h('p', {}, 'All your mocks, quizzes and checklists together: ', W.h('a', { href: '#practice.next' }, 'What to revise next'), '.'));
    }
    function render() {
      art.classList.toggle('mock-done', S.done);
      runBtn.hidden = S.done;
      finBtn.hidden = S.done;
      againBtn.hidden = !S.done;
      runBtn.textContent = S.start ? 'Pause' : (S.spent ? 'Resume' : (mins ? `Start the clock (${mins} min)` : 'Start the clock'));
      note.textContent = S.done ? (answer ? `Mark the ${answer === 1 ? 'question' : answer + ' questions'} you answered against the mark scheme under it; leave the others blank.` : 'Mark each question against the mark scheme under it.') : (answer ? `Answer ${answer === 1 ? 'one question' : answer + ' questions'}, as the instructions say. Answers and mark schemes appear when you finish.` : 'Answers and mark schemes appear when you finish.');
      clearInterval(iv);
      if (S.start && !S.done) iv = setInterval(tick, 1000);
      tick(); marksInputs(); summary();
    }
    runBtn.addEventListener('click', () => {
      if (S.start) { S.spent += Date.now() - S.start; S.start = 0; } else S.start = Date.now();
      save(); render();
    });
    finBtn.addEventListener('click', () => {
      if (!confirmT) { finBtn.textContent = 'Show the answers?'; say('Press again to finish and show the answers.'); confirmT = setTimeout(() => { confirmT = 0; finBtn.textContent = 'Finish and mark'; }, 3000); return; }
      clearTimeout(confirmT); confirmT = 0; finBtn.textContent = 'Finish and mark';
      if (S.start) { S.spent += Date.now() - S.start; S.start = 0; }
      S.done = true; save(); render();
      for (const d of $$('.try-mock details.ta', art)) d.open = true;
      bar.scrollIntoView({ block: 'nearest' });
      // focus the first mark box (not "Start again", where a second Enter would wipe the paper)
      ($('.mock-mark input', art) || againBtn).focus({ preventScroll: true });
      say('Answers shown. Mark each question against the mark scheme under it.');
    });
    againBtn.addEventListener('click', () => {
      S = { start: 0, spent: 0, done: false, marks: {} }; save(); warned = false;
      for (const d of $$('.try-mock details.ta', art)) d.open = false;
      render(); window.scrollTo(0, art.offsetTop);
      runBtn.focus({ preventScroll: true });
    });
    render();
  }

  /* ---------- "Learn more online" page: show one kind of link ---------- */
  function initLinkFilter(art) {
    for (const f of $$('.lk-filter', art)) {
      const sheet = f.closest('.lk-sheet');
      f.addEventListener('click', (e) => {
        const b = e.target.closest('button[data-k]');
        if (!b) return;
        const k = b.getAttribute('data-k');
        for (const x of $$('button', f)) x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
        for (const g of $$('.lk-g', sheet)) g.hidden = !!k && g.getAttribute('data-kind') !== k;
        for (const box of $$('.links-b', sheet)) {
          const show = $$('.lk-g', box).some(g => !g.hidden);
          box.hidden = !show;
          if (box.previousElementSibling && box.previousElementSibling.tagName === 'H3') box.previousElementSibling.hidden = !show;
        }
        for (const h2 of $$('h2', sheet)) {
          let el = h2.nextElementSibling, any = false;
          while (el && el.tagName !== 'H2') { if (el.tagName === 'H3' && !el.hidden) any = true; el = el.nextElementSibling; }
          h2.hidden = !any;
        }
      });
    }
  }

  /* ---------- sidebar ---------- */
  function openSubject(sid, only) {
    for (const sec of $$('.nav-subj')) {
      const is = sec.getAttribute('data-subject') === sid;
      if (is) { sec.classList.add('open'); $('.nav-s', sec).setAttribute('aria-expanded', 'true'); }
      else if (only) { sec.classList.remove('open'); $('.nav-s', sec).setAttribute('aria-expanded', 'false'); }
    }
  }
  for (const btn of $$('.nav-s')) {
    btn.addEventListener('click', () => {
      const sec = btn.closest('.nav-subj');
      const open = !sec.classList.contains('open');
      sec.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  const menuBtn = $('#menuBtn'), scrim = $('#scrim'), sidebar = $('#sidebar');
  const drawerMode = () => getComputedStyle(menuBtn).display !== 'none';
  function setDrawer(open, focus) {
    const was = app.classList.contains('nav-open');
    app.classList.toggle('nav-open', open);
    scrim.hidden = !open;
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) {
      const a = $('.nav-g a.active');
      if (a) a.scrollIntoView({ block: 'center' });
      // focus moves into the drawer (it is hidden until the slide starts, so wait a frame)
      if (focus) requestAnimationFrame(() => (a && a.offsetParent ? a : $('.side-home')).focus({ preventScroll: true }));
    } else if (was && focus) menuBtn.focus();
  }
  menuBtn.addEventListener('click', () => setDrawer(!app.classList.contains('nav-open'), true));
  scrim.addEventListener('click', () => setDrawer(false, true));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && app.classList.contains('nav-open')) setDrawer(false, true); });
  sidebar.addEventListener('focusout', (e) => {
    if (app.classList.contains('nav-open') && drawerMode() && e.relatedTarget && !sidebar.contains(e.relatedTarget) && e.relatedTarget !== menuBtn) setDrawer(false);
  });

  /* ---------- quizzes ---------- */
  function renderQuizInto(el, idxs, opts) {
    opts = opts || {};
    el.innerHTML = '';
    idxs.forEach((qi, n) => {
      const q = QUIZ[qi]; if (!q) return;
      const box = W.h('div', { class: 'qz' });
      const qid = W.uid('qz');
      box.append(W.h('div', { class: 'qz-q', id: qid, html: `<span class="qz-n">${opts.numbered === false ? '' : (n + 1) + '.'}</span>${q.q}` }));
      const opt = W.h('div', { class: 'qz-o', role: 'group', 'aria-labelledby': qid });
      const order = opts.shuffle ? W.shuffle(q.o.map((_, i) => i)) : q.o.map((_, i) => i);
      const btns = [];
      order.forEach((oi, k) => {
        const b = W.h('button', { class: 'qz-btn', type: 'button', html: `<span class="qz-k">${'ABCDEF'[k]}</span><span>${q.o[oi]}</span>` });
        b.addEventListener('click', () => {
          if (b.getAttribute('aria-disabled') === 'true') return;
          const right = oi === q.a;
          btns.forEach(x => {
            x.b.setAttribute('aria-disabled', 'true');
            if (x.oi === q.a) { x.b.classList.add('right'); x.b.append(W.h('span', { class: 'sr-only' }, ' (correct answer)')); }
          });
          if (!right) { b.classList.add('wrong'); b.append(W.h('span', { class: 'sr-only' }, ' (your answer, not correct)')); }
          const ex = W.h('div', { class: 'qz-e ' + (right ? 'ok' : 'no'), html: `<b>${right ? 'Correct.' : 'Not quite.'}</b>${q.e || ''}` });
          box.append(ex);
          say(ex.textContent);
          // the last 10 answers per chapter feed "What to revise next"
          const log = store.get('quizlog', {});
          log[q.c] = ((log[q.c] || '') + (right ? '1' : '0')).slice(-10);
          store.set('quizlog', log);
          if (opts.onAnswer) opts.onAnswer(right, qi);
        });
        btns.push({ b, oi });
        opt.append(b);
      });
      box.append(opt);
      el.append(box);
    });
  }

  /* ---------- widgets & lazy hydration ---------- */
  function hydrate(art) {
    if (art.dataset.hydrated) return;
    art.dataset.hydrated = '1';
    for (const qz of $$('.quiz[data-qs]', art)) renderQuizInto(qz, qz.getAttribute('data-qs').split(',').filter(Boolean).map(Number));
    for (const el of $$('.widget[data-w]', art)) {
      const name = el.getAttribute('data-w');
      const fn = W.reg[name];
      if (!fn) { el.innerHTML = `<div class="w"><div class="w-b"><div class="w-note">This interactive tool (${W.esc(name)}) is being built and will appear in a later update.</div></div></div>`; continue; }
      try { fn(el, Object.assign({}, el.dataset)); } catch (err) { console.error(err); el.innerHTML = `<div class="w"><div class="w-b"><div class="w-err">This tool could not start: ${W.esc(err.message)}</div></div></div>`; }
    }
    renderTicks(art);
    if (art.getAttribute('data-level') === 'mock') initMock(art);
    if ($('.lk-filter', art)) initLinkFilter(art);
    if (art.id === 'c-practice.quiz') ZTA.loadAll().then(() => initPractice(art), loadFailed);
    if (art.id === 'c-tools.glossary') ZTA.loadAll().then(() => initGlossary(art), loadFailed);
  }

  function markScrollers(scope) {
    for (const el of $$('.tw, .mb', scope)) {
      if (el.scrollWidth > el.clientWidth + 1) el.setAttribute('tabindex', '0');
      else if (el.getAttribute('tabindex') === '0') el.removeAttribute('tabindex');
    }
  }
  let rsT = 0;
  window.addEventListener('resize', () => { clearTimeout(rsT); rsT = setTimeout(() => { if (current) markScrollers(current); }, 250); });

  /* ---------- router ---------- */
  let current = null, routed = false;
  const rail = $('#railToc');
  let spy = null;
  function route() {
    let h = '';
    try { h = decodeURIComponent(location.hash.slice(1)); } catch (e) { h = location.hash.slice(1); }
    if (!h) h = 'home';
    let cid = h, sec = null;
    const k = h.indexOf('--');
    if (k > 0) { cid = h.slice(0, k); sec = h; }
    const need = ZTA.needs(cid);
    if (need.length) {
      const slow = setTimeout(() => toast('Loading…'), 250);
      Promise.all(need.map(ZTA.load)).then(() => { clearTimeout(slow); route(); }, (e) => { clearTimeout(slow); loadFailed(e); });
      return;
    }
    let art = document.getElementById('c-' + cid);
    if (!art) { art = document.getElementById('c-home') || $('.chapter'); cid = art ? art.getAttribute('data-id') : ''; sec = null; }
    if (!art) return;
    const changed = current !== art;
    if (current && changed) current.hidden = true;
    art.hidden = false; current = art;
    hydrate(art);
    // nav state
    for (const a of $$('.nav-g a.active')) { a.classList.remove('active'); a.removeAttribute('aria-current'); }
    const link = $(`.nav-g a[data-nav="${CSS.escape(cid)}"]`);
    if (link) { link.classList.add('active'); link.setAttribute('aria-current', 'page'); }
    const sid = art.getAttribute('data-subject');
    if (changed) openSubject(sid, false);
    if (link && changed) {
      const sb = $('#sidebar');
      const r = link.getBoundingClientRect(), sr = sb.getBoundingClientRect();
      if (r.top < sr.top + 60 || r.bottom > sr.bottom - 20) link.scrollIntoView({ block: 'center' });
    }
    app.className = 'app s-' + sid + (app.classList.contains('nav-open') ? ' nav-open' : '');
    setDrawer(false);
    buildToc(art);
    const info = G.ch[cid];
    document.title = info && cid !== 'home' ? `${info.t} · Zero to A* Ω` : 'Zero to A* Ω';
    if (cid !== 'home') store.set('last', cid);
    const target = sec && document.getElementById(sec);
    if (changed) offerResume(art, cid, !!target);
    if (target) { requestAnimationFrame(() => { target.scrollIntoView({ block: 'start' }); trackSoon(); }); }
    else if (changed) window.scrollTo(0, 0);
    track();
    if (cid === 'home') renderHome();
    if (cid === 'practice.next') renderNext(art);
    markScrollers(art);
    // after a navigation (not the first load) keyboard and screen-reader focus starts at the new page or section
    if (routed && (changed || target)) focusOn(target || $('h1', art));
    routed = true;
    if (changed) fetchAhead(cid);
  }
  // when the browser is idle, fetch the next chapter's file so "Next" opens at once (not on a data-saving connection)
  function fetchAhead(cid) {
    const next = G.order[G.order.indexOf(cid) + 1];
    if (!next || !ZTA.needs(next).length) return;
    const c = navigator.connection;
    if (c && (c.saveData || /2g/.test(c.effectiveType || ''))) return;
    const go = () => { if (current && current.getAttribute('data-id') === cid) Promise.all(ZTA.needs(next).map(ZTA.load)).catch(() => {}); };
    if (window.requestIdleCallback) requestIdleCallback(go, { timeout: 4000 }); else setTimeout(go, 1500);
  }
  $('#skipLink').addEventListener('click', (e) => { e.preventDefault(); focusOn((current && $('h1', current)) || $('#main')); });
  window.addEventListener('hashchange', route);
  function loadFailed(e) {
    if (/^https?:$/.test(location.protocol)) toast(navigator.onLine === false ? 'This course is not saved on this device. Go online, or download it in Settings.' : e.message + '. Check your connection.');
    else toast(e.message + '. Keep the c folder next to index.html.');
  }

  /* The contents list is drawn twice: in the rail (wide screens) and in the "On this page" sheet (where the rail is
     hidden). track() follows the scroll position: it marks the current section in both lists, moves the reading
     progress line under the top bar, and remembers the section so the reader can resume there. */
  const sheetToc = $('#sheetToc'), tocBtn = $('#tocBtn'), tocSheet = $('#tocSheet'), tocScrim = $('#tocScrim'), readProg = $('#readProg');
  let heads = [], curSec = null, trackT = 0;
  const secs = store.get('secs', {});   // chapter -> [section id, section title] where the reader last was
  function buildToc(art) {
    rail.innerHTML = ''; sheetToc.innerHTML = '';
    if (spy) { spy.disconnect(); spy = null; }
    setSheet(false);
    heads = $$('.prose h2, .prose h3', art).filter(h => h.id);
    curSec = null;
    const id = art.getAttribute('data-id');
    const none = !heads.length || id === 'home';
    tocBtn.hidden = none; readProg.hidden = none;
    if (!heads.length) { $('#rail').style.visibility = 'hidden'; return; }
    $('#rail').style.visibility = 'visible';
    for (const h of heads) {
      for (const list of [rail, sheetToc]) list.append(W.h('li', { class: h.tagName === 'H3' ? 'h3' : 'h2' }, W.h('a', { href: '#' + h.id, 'data-for': h.id }, h.textContent)));
    }
    const info = G.ch[id];
    $('#railProg').textContent = info && info.w ? `About ${Math.max(1, Math.round(info.w / 200))} min read` : '';
  }
  function track() {
    trackT = 0;
    if (!current || !heads.length) return;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    readProg.firstElementChild.style.transform = `scaleX(${p.toFixed(4)})`;
    // the current section: the last heading that has passed the line just under the top bar (headings inside a
    // closed proof have no box and are skipped)
    const line = $('.bar').offsetHeight + 28;
    let cur = null;
    for (const h of heads) { if (h.offsetParent !== null && h.getBoundingClientRect().top <= line) cur = h; }
    if (cur === curSec) return;
    curSec = cur;
    for (const a of $$('.rail-toc a.on')) { a.classList.remove('on'); a.removeAttribute('aria-current'); }
    const h2s = heads.filter(h => h.tagName === 'H2');
    let k = 0;
    if (cur) {
      for (const a of $$(`.rail-toc a[data-for="${CSS.escape(cur.id)}"]`)) { a.classList.add('on'); a.setAttribute('aria-current', 'location'); }
      const own = cur.tagName === 'H2' ? cur : heads.slice(0, heads.indexOf(cur)).reverse().find(h => h.tagName === 'H2');
      k = own ? h2s.indexOf(own) + 1 : 0;
      // remember where the reader is (not on the first load of a page: only once they have scrolled to a section)
      const cid = current.getAttribute('data-id');
      if (G.ch[cid] && cid !== 'home') {
        secs[cid] = [cur.id, cur.textContent.trim().slice(0, 90)];
        clearTimeout(track.saveT); track.saveT = setTimeout(() => store.set('secs', secs), 400);
        const note = $('.ch-resume', current);
        if (note && note.getAttribute('data-sec') === cur.id) note.remove();
      }
    }
    $('#tocSheetN').textContent = h2s.length ? (k ? `Section ${k} of ${h2s.length}` : `${h2s.length} sections`) : '';
  }
  // once per frame; the timer covers a page whose frames are paused (a background tab that is scrolled by a link)
  function trackSoon() {
    if (trackT) return;
    trackT = 1;
    let ran = false;
    const go = () => { if (!ran) { ran = true; track(); } };
    requestAnimationFrame(go); setTimeout(go, 150);
  }
  window.addEventListener('scroll', trackSoon, { passive: true });
  window.addEventListener('resize', trackSoon);
  /** A chapter opened at its top offers a link to the section the reader was in last time. */
  function offerResume(art, cid, atSection) {
    for (const old of $$('.ch-resume', art)) old.remove();
    const s = secs[cid], head = $('.ch-head', art);
    if (atSection || !s || !head || !heads.length || s[0] === heads[0].id || !document.getElementById(s[0])) return;
    head.append(W.h('p', { class: 'ch-resume', 'data-sec': s[0] }, 'Last time you were at ', W.h('a', { href: '#' + s[0] }, s[1]), '.'));
  }
  function setSheet(open, focus) {
    const was = !tocSheet.hidden;
    if (open === was) return;
    tocSheet.hidden = !open; tocScrim.hidden = !open;
    tocBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) {
      track();
      const on = $('a.on', sheetToc) || $('a', sheetToc);
      if (on) { on.scrollIntoView({ block: 'center' }); if (focus) on.focus({ preventScroll: true }); }
    } else if (focus) tocBtn.focus({ preventScroll: true });
  }
  tocBtn.addEventListener('click', () => setSheet(tocSheet.hidden, true));
  $('#tocClose').addEventListener('click', () => setSheet(false, true));
  tocScrim.addEventListener('click', () => setSheet(false, true));
  sheetToc.addEventListener('click', (e) => { if (e.target.closest('a')) setSheet(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !tocSheet.hidden) setSheet(false, true); });
  tocSheet.addEventListener('focusout', (e) => { if (!tocSheet.hidden && e.relatedTarget && !tocSheet.contains(e.relatedTarget) && e.relatedTarget !== tocBtn) setSheet(false); });

  /* ---------- home ---------- */
  let homeDrawn = false;
  function renderHome() {
    const list = $('#subjects');
    if (list && !list.children.length) {
      list.innerHTML = G.subjects.filter(s => s.c).map(s => {
        // a course with no chapters yet links to its About page (core about.<id>) until its first chapter is written
        const href = s.first || s.ab;
        const open = href ? `<a class="subj${s.first ? '' : ' subj-soon'}" href="#${href}">` : '<div class="subj subj-soon">';
        return `<li class="s-${s.id}">${open}`
          + `<span class="subj-c">${W.esc(s.code === 'ALL' ? 'More' : s.code || '')}${s.y ? ` · ${W.esc(s.y)} syllabus` : ''}</span><span class="subj-t">${W.esc(s.t)}</span>`
          + `<span class="subj-d">${W.esc(s.desc || '')}</span>`
          + `<span class="subj-p"><span data-cnt="${s.id}"></span><span class="subj-bar"><span data-bar="${s.id}"></span></span>`
          + (s.n ? `<span>${s.n} of ${s.p} chapters ready</span>` : s.ab ? '<span>Read what this subject is about</span>' : '') + `</span>${href ? '</a>' : '</div>'}</li>`;
      }).join('');
    }
    const road = $('#c-home .road');
    if (road && !homeDrawn) { homeDrawn = true; road.classList.add('draw'); }
    renderProgress();
    const last = store.get('last', null);
    const box = $('#resume');
    if (box) {
      if (last && G.ch[last]) {
        box.hidden = false;
        const a = $('#resumeLink', box);
        // straight to the section the reader was in, when one is remembered
        const s = secs[last];
        if (a) { a.href = '#' + (s ? s[0] : last); a.textContent = G.ch[last].t + (s ? ' › ' + s[1] : ''); }
      } else box.hidden = true;
      // re-tests that are due (spaced re-testing, on "What to revise next")
      let dueBox = $('#retestDue');
      const due = G.ch['practice.next'] ? retestsDue(Date.now()).length : 0;
      if (due && !dueBox) { dueBox = W.h('div', { class: 'resume', id: 'retestDue' }); box.after(dueBox); }
      if (dueBox) {
        dueBox.hidden = !due;
        dueBox.innerHTML = '';
        if (due) dueBox.append(W.h('span', {}, 'Due for a re-test:'), ' ', W.h('a', { href: '#practice.next' }, `${due} chapter${due === 1 ? '' : 's'} you marked as learned`));
      }
    }
  }

  /* ---------- search ---------- */
  const input = $('#searchInput'), results = $('#searchResults');
  let index = null, sel = -1, hits = [];
  // Chapters inside index.html (core pages; every chapter in a kit preview) are read from the page; course chapters
  // come from the search files (c/<course>.search.js), so searching never loads the chapters themselves.
  const domIndex = new Map();   // id -> entry, kept between rebuilds
  function buildIndex() {
    index = [];
    const seen = new Set();
    for (const rows of Object.values(ZTA.search)) for (const r of rows) {
      const info = G.ch[r[0]];
      if (!info || seen.has(r[0])) continue;
      seen.add(r[0]);
      if (!r[3]) r[3] = { id: r[0], t: info.t, s: info.s, heads: r[1].map(h => ({ id: h[0], t: h[1] })), text: r[2], lt: info.t.toLowerCase(), lx: r[2].toLowerCase() };
      index.push(r[3]);
    }
    for (const art of $$('.chapter')) {
      const id = art.getAttribute('data-id');
      if (seen.has(id)) continue;
      if (!domIndex.has(id)) {
        const info = G.ch[id] || { t: id, s: art.getAttribute('data-subject') };
        const heads = $$('.prose h2, .prose h3', art).map(h => ({ id: h.id, t: h.textContent }));
        const text = (art.querySelector('.prose') || art).textContent.replace(/\s+/g, ' ');
        domIndex.set(id, { id, t: info.t, s: info.s, heads, text, lt: info.t.toLowerCase(), lx: text.toLowerCase() });
      }
      index.push(domIndex.get(id));
    }
  }
  const subjShort = (sid) => { const s = G.subjects.find(x => x.id === sid); return s ? s.short : sid; };
  function search(q) {
    if (!index) buildIndex();
    const terms = q.toLowerCase().split(/\s+/).filter(t => t.length > 1 || /\d/.test(t));
    if (!terms.length) return [];
    const out = [];
    for (const d of index) {
      let score = 0, head = null, ok = true;
      for (const t of terms) {
        const inT = d.lt.includes(t);
        const h = d.heads.find(x => x.t.toLowerCase().includes(t));
        const pos = d.lx.indexOf(t);
        if (!inT && !h && pos < 0) { ok = false; break; }
        if (inT) score += d.lt.startsWith(t) ? 30 : 18;
        if (h) { score += 8; head = head || h; }
        if (pos >= 0) { let c = 0, i = pos; while (i >= 0 && c < 12) { c++; i = d.lx.indexOf(t, i + t.length); } score += c; }
      }
      if (!ok) continue;
      out.push({ d, score, head });
    }
    out.sort((a, b) => b.score - a.score);
    const res = out.slice(0, 12).map(({ d, head }) => {
      const t = terms[0];
      const pos = d.lx.indexOf(t);
      let snip = '';
      if (pos >= 0) {
        const s0 = Math.max(0, pos - 60), s1 = Math.min(d.text.length, pos + 110);
        snip = (s0 > 0 ? '…' : '') + d.text.slice(s0, s1) + (s1 < d.text.length ? '…' : '');
      }
      let html = W.esc(snip);
      for (const tt of terms) html = html.replace(new RegExp('(' + tt.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<b>$1</b>');
      return { href: '#' + (head && !d.lt.includes(t) ? head.id : d.id), title: d.t + (head && !d.lt.includes(t) ? ' › ' + head.t : ''), s: d.s, html };
    });
    // glossary terms
    for (const g of GLOSS) {
      const term = g.t.replace(/<[^>]+>/g, '');
      if (terms.every(t => term.toLowerCase().includes(t)) && res.length < 16) {
        res.unshift({ href: '#' + g.c, title: 'Key term: ' + term, s: g.s, html: W.esc(g.d.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').slice(0, 150)) + '…' });
      }
    }
    return res.slice(0, 14);
  }
  // search files still on their way (results are shown course by course as they arrive)
  let searchFailed = false;
  const searchWaiting = () => searchFailed ? 0 : (G.chunks || []).filter(k => !ZTA.search[k]).length;
  /** keep = a re-draw because more search text arrived: the reader's highlighted result stays highlighted */
  function showResults(keep) {
    const q = input.value.trim();
    if (!q) { closeSearch(); return; }
    const was = keep === true && sel >= 0 && hits[sel] ? hits[sel].href : null;
    hits = search(q); sel = was ? hits.findIndex(r => r.href === was) : -1;
    const waiting = searchWaiting(), all = (G.chunks || []).length;
    const more = waiting ? `<div class="sr-more">Searching the other courses… (${all - waiting} of ${all} ready)</div>` : '';
    results.innerHTML = hits.length ? hits.map((r, i) => `<a class="sr s-${r.s}" role="option" id="sr${i}" tabindex="-1" aria-selected="${i === sel ? 'true' : 'false'}" href="${r.href}"><div class="sr-t"><span class="sr-s">${W.esc(subjShort(r.s))}</span><span>${W.esc(r.title)}</span></div>${r.html ? `<div class="sr-x">${r.html}</div>` : ''}</a>`).join('') + more
      : waiting ? more : `<div class="sr-empty">No matches for “${W.esc(q)}”. Try a shorter word, or a topic name such as “moles” or “break-even”.</div>`;
    results.hidden = false;
    input.setAttribute('aria-expanded', 'true');
    if (sel >= 0) input.setAttribute('aria-activedescendant', 'sr' + sel); else input.removeAttribute('aria-activedescendant');
    // the count is read out once the search is complete, not for every file that arrives
    if (!waiting || !keep) $('#searchStatus').textContent = hits.length ? `${hits.length} result${hits.length === 1 ? '' : 's'}${waiting ? ' so far' : ''}. Use the up and down arrows to choose.` : waiting ? 'Searching.' : 'No matches.';
  }
  let st = 0, moreT = 0;
  const redraw = () => { clearTimeout(moreT); moreT = setTimeout(() => { if (input.value.trim() && document.activeElement === input) showResults(true); }, 60); };
  input.addEventListener('input', () => { clearTimeout(st); st = setTimeout(showResults, 120); });
  input.addEventListener('focus', () => {
    // The text comes from the search files: the course being read is fetched first, then the others, and the
    // results are re-drawn as each one arrives (zta:search). Key terms come from the base files.
    const here = current && (G.ch[current.getAttribute('data-id')] || {}).k;
    searchFailed = false;
    (here ? ZTA.load(here + '.search').catch(() => {}) : Promise.resolve())
      .then(() => ZTA.loadSearch()).catch((e) => { searchFailed = true; redraw(); loadFailed(e); });
    ZTA.loadAll().then(redraw, loadFailed);
    if (input.value.trim()) showResults();
  });
  document.addEventListener('zta:chunk', () => { index = null; renderProgress(); renderTicks(document); });
  document.addEventListener('zta:search', () => { index = null; redraw(); });
  document.addEventListener('zta:page', () => { index = null; renderProgress(); });
  input.addEventListener('keydown', (e) => {
    const items = $$('.sr', results);
    if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(items.length - 1, sel + 1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(0, sel - 1); }
    else if (e.key === 'Enter') { const it = items[sel >= 0 ? sel : 0]; if (it) { location.hash = it.getAttribute('href'); closeSearch(); } return; }
    else if (e.key === 'Escape') { closeSearch(); input.blur(); return; }
    else return;
    items.forEach((it, i) => it.setAttribute('aria-selected', i === sel ? 'true' : 'false'));
    if (items[sel]) { items[sel].scrollIntoView({ block: 'nearest' }); input.setAttribute('aria-activedescendant', items[sel].id); }
  });
  function closeSearch() { results.hidden = true; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); }
  $('.search').addEventListener('focusout', () => setTimeout(() => { if (!$('.search').contains(document.activeElement)) closeSearch(); }, 150));
  results.addEventListener('click', (e) => { if (e.target.closest('.sr')) { closeSearch(); input.blur(); } });
  document.addEventListener('click', (e) => { if (!e.target.closest('.search')) closeSearch(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && !/input|textarea|select/i.test(document.activeElement.tagName)) { e.preventDefault(); input.focus(); input.select(); }
  });

  /* ---------- glossary page ---------- */
  function initGlossary(art) {
    const host = $('#glossaryApp', art);
    if (!host) return;
    const items = GLOSS.map(g => ({ ...g, plain: g.t.replace(/<[^>]+>/g, '').trim() }))
      .filter(g => g.plain)
      .sort((a, b) => a.plain.localeCompare(b.plain, 'en', { sensitivity: 'base' }));
    const filt = W.h('input', { type: 'search', placeholder: `Filter ${items.length} key terms…`, 'aria-label': 'Filter key terms', id: 'glossFilter' });
    const subjSel = W.h('select', { 'aria-label': 'Subject', id: 'glossSubject' }, W.h('option', { value: '' }, 'All subjects'),
      ...G.subjects.filter(s => items.some(i => i.s === s.id)).map(s => W.h('option', { value: s.id }, s.t)));
    const count = W.h('div', { class: 'w-note', 'aria-live': 'polite' });
    const list = W.h('dl', {});
    const letters = W.h('div', { class: 'gl-letters', role: 'group', 'aria-label': 'Jump to a letter' });
    const wrap = W.h('div', { class: 'w' }, W.h('div', { class: 'w-b' }, W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-ctl', style: { flex: '3 1 14rem' } }, W.h('label', {}, 'Search terms'), filt), W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Subject'), subjSel)), count));
    host.append(wrap, letters, list);
    // The list shows 600 terms at a time. The letter links cover every letter that has a term: a letter outside the
    // 600 on screen re-draws the list from that letter (`from`).
    let from = 0, first = {};
    function draw() {
      const q = filt.value.trim().toLowerCase(), s = subjSel.value;
      const shown = items.filter(i => (!s || i.s === s) && (!q || i.plain.toLowerCase().includes(q) || i.d.toLowerCase().includes(q)));
      count.textContent = `${shown.length} term${shown.length === 1 ? '' : 's'}`;
      const letter = (i) => { const L = (i.plain[0] || '#').toUpperCase(); return /[A-Z]/.test(L) ? L : 'num'; };
      first = {};
      shown.forEach((i, k) => { const L = letter(i); if (!(L in first)) first[L] = k; });
      if (from >= shown.length) from = 0;
      const seen = new Set();
      list.innerHTML = (from ? `<p class="w-note">Showing the terms from “${W.esc(shown[from].plain)}” on. Choose a letter to move.</p>` : '') + shown.slice(from, from + 600).map(i => {
        const L = letter(i);
        const anchor = seen.has(L) ? '' : ` id="gl-${L}"`;
        seen.add(L);
        const subj = G.subjects.find(x => x.id === i.s);
        const ch = G.ch[i.c];
        return `<div class="gl-item s-${i.s}"${anchor}><dt>${i.t}<a href="#${i.c}">${W.esc(subj ? subj.short : '')} · ${W.esc(ch ? ch.t : '')}</a></dt><dd>${i.d}</dd></div>`;
      }).join('') + (shown.length > from + 600 ? `<p class="w-note">Showing 600 of ${shown.length} terms. Choose a later letter, or type to narrow the list.</p>` : '');
      letters.innerHTML = Object.keys(first).filter(l => l !== 'num').map(l => `<a href="#tools.glossary" data-l="${l}">${l}</a>`).join('');
    }
    letters.addEventListener('click', (e) => {
      const a = e.target.closest('[data-l]'); if (!a) return;
      e.preventDefault();
      const L = a.dataset.l;
      if (!document.getElementById('gl-' + L)) { from = first[L] || 0; draw(); }
      const t = document.getElementById('gl-' + L);
      if (t) { t.scrollIntoView({ block: 'start' }); focusOn(t); }
    });
    const restart = () => { from = 0; draw(); };
    filt.addEventListener('input', restart); subjSel.addEventListener('change', restart);
    draw();
  }

  /* ---------- practice page ---------- */
  function initPractice(art) {
    const host = $('#practiceApp', art);
    if (!host) return;
    const all = quizIds();
    const subjects = G.subjects.filter(s => all.some(i => QUIZ[i].s === s.id));
    const subjSel = W.h('select', { id: 'pqSubject', 'aria-label': 'Subject' }, W.h('option', { value: '' }, `All subjects (${all.length})`),
      ...subjects.map(s => W.h('option', { value: s.id }, `${s.t} (${all.filter(i => QUIZ[i].s === s.id).length})`)));
    const nSel = W.h('select', { id: 'pqCount', 'aria-label': 'Number of questions' }, ...[5, 10, 20, 40].map(n => W.h('option', { value: n, selected: n === 10 }, `${n} questions`)));
    const setSel = W.h('select', { id: 'pqPaper', 'aria-label': 'Paper' });
    const setCtl = W.h('div', { class: 'w-ctl', hidden: true }, W.h('label', {}, 'Paper'), setSel);
    const startBtn = W.h('button', { class: 'btn', type: 'button' }, 'Start a quiz');
    const area = W.h('div', {});
    host.append(W.h('div', { class: 'w' }, W.h('div', { class: 'w-h' }, W.h('span', { class: 'w-t' }, 'Mixed practice'), W.h('span', { class: 'w-s' }, 'Questions take turns between chapters, so you practise choosing the method')),
      W.h('div', { class: 'w-b' }, W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Subject'), subjSel), setCtl, W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Length'), nSel), startBtn), area)));
    if (!all.length) { area.append(W.h('p', { class: 'w-note' }, 'Quizzes will appear here as chapters are added.')); return; }
    const papersOf = (sid) => ((G.papers || {})[sid] || []).filter(p => p.c.some(c => all.some(i => QUIZ[i].c === c)));
    function fillPapers() {
      const ps = papersOf(subjSel.value);
      setSel.innerHTML = '';
      setSel.append(W.h('option', { value: '' }, 'All chapters'), ...ps.map(p => W.h('option', { value: p.id }, `${p.t} (${all.filter(i => p.c.includes(QUIZ[i].c)).length})`)));
      setCtl.hidden = !ps.length;
    }
    subjSel.addEventListener('change', fillPapers);
    fillPapers();
    // interleave: shuffle each chapter's questions, then take one chapter at a time in turn
    function interleave(pool, n) {
      const by = new Map();
      for (const i of W.shuffle(pool)) { const c = QUIZ[i].c; if (!by.has(c)) by.set(c, []); by.get(c).push(i); }
      const lists = W.shuffle([...by.values()]), out = [];
      while (out.length < n && lists.some(l => l.length)) for (const l of lists) if (l.length && out.length < n) out.push(l.shift());
      return out;
    }
    startBtn.addEventListener('click', () => {
      const paper = papersOf(subjSel.value).find(p => p.id === setSel.value);
      const pool = all.filter(i => (!subjSel.value || QUIZ[i].s === subjSel.value) && (!paper || paper.c.includes(QUIZ[i].c)));
      const pick = interleave(pool, +nSel.value);
      let right = 0, answered = 0;
      const wrongCh = new Map();
      area.innerHTML = '';
      const score = W.h('div', { class: 'pq-score', 'aria-live': 'polite' }, `0 / ${pick.length}`);
      const qbox = W.h('div', { class: 'quiz-wrap' });
      const review = W.h('div', {});
      area.append(score, qbox, review);
      renderQuizInto(qbox, pick, {
        shuffle: true, onAnswer: (ok, qi) => {
          answered++; if (ok) right++; else wrongCh.set(QUIZ[qi].c, (wrongCh.get(QUIZ[qi].c) || 0) + 1);
          score.textContent = `${right} / ${pick.length}` + (answered === pick.length ? ` — ${Math.round(100 * right / pick.length)}%` : '');
          if (answered === pick.length) {
            review.innerHTML = wrongCh.size ? `<h3>Revise these chapters next</h3><ul>${[...wrongCh.keys()].map(c => `<li><a href="#${c}">${W.esc(G.ch[c] ? G.ch[c].t : c)}</a></li>`).join('')}</ul>` : '<p><b>Perfect score.</b> Try a longer quiz or another subject.</p>';
          }
        }
      });
      score.scrollIntoView({ block: 'nearest' });
    });
  }

  /* ---------- "What to revise next": marks lost in mocks, recent quiz misses, unticked checklists ---------- */
  // Re-drawn each time the page is shown, from what this browser has saved. Scores: each mark lost in the latest
  // marking of a mock counts 1, each wrong answer among a chapter's last 10 quiz answers 2, and each unticked
  // checklist line in a chapter marked as learned 0.5.
  let nextSubj = '';
  function renderNext(art) {
    const host = $('#nextApp', art);
    if (!host) return;
    const T = {};
    const get = (c) => T[c] || (T[c] = { c, lost: 0, of: 0, mocks: new Set(), qw: 0, qn: 0, ul: 0, un: 0 });
    let mocksMarked = 0, answers = 0, learned = 0;
    for (const [mid, qs] of Object.entries(G.mocks || {})) {
      const S = store.get('mock:' + mid, null);
      if (!S || !S.done || !S.marks) continue;
      let any = false;
      qs.forEach(([n, rev], i) => {
        if (!n || !rev || !G.ch[rev] || S.marks[i] == null) return;
        any = true;
        const t = get(rev); t.lost += n - S.marks[i]; t.of += n; t.mocks.add(mid);
      });
      if (any) mocksMarked++;
    }
    for (const [c, s] of Object.entries(store.get('quizlog', {}))) {
      if (!G.ch[c] || !s) continue;
      const t = get(c); t.qn = s.length; t.qw = s.replace(/1/g, '').length; answers += s.length;
    }
    for (const [c, keys] of Object.entries(G.ck || {})) {
      if (!done[c]) continue;
      learned++;
      const un = keys.filter(k => !ticks[k]).length;
      if (un) { const t = get(c); t.ul = un; t.un = keys.length; }
    }
    const rows = Object.values(T).map(t => Object.assign(t, { score: t.lost + 2 * t.qw + 0.5 * t.ul })).filter(t => t.score > 0);
    const subjects = G.subjects.filter(s => rows.some(t => G.ch[t.c].s === s.id));
    if (!subjects.some(s => s.id === nextSubj)) nextSubj = '';
    const list = rows.filter(t => !nextSubj || G.ch[t.c].s === nextSubj).sort((a, b) => b.score - a.score || a.c.localeCompare(b.c));
    const top = list.length ? list[0].score : 1;

    host.innerHTML = '';
    renderRetests(host);
    const sel = W.h('select', { 'aria-label': 'Subject' }, W.h('option', { value: '' }, 'All subjects'),
      ...subjects.map(s => W.h('option', { value: s.id, selected: s.id === nextSubj }, s.t)));
    sel.addEventListener('change', () => { nextSubj = sel.value; renderNext(art); });
    const plural = (n, w) => `${n} ${w}${n === 1 ? '' : 's'}`;
    const basis = `From ${plural(mocksMarked, 'marked mock paper')}, ${plural(answers, 'recent quiz answer')} and the checklists of ${plural(learned, 'chapter')} you marked as learned.`;
    const body = W.h('div', { class: 'w-b' });
    host.append(W.h('div', { class: 'w' }, W.h('div', { class: 'w-h' }, W.h('span', { class: 'w-t' }, 'What to revise next'), W.h('span', { class: 'w-s' }, 'Your weakest chapters first')), body));
    if (subjects.length > 1) body.append(W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Subject'), sel)));
    body.append(W.h('p', { class: 'w-note' }, basis));
    if (!list.length) {
      body.append(W.h('p', {}, W.h('b', {}, 'Nothing to revise yet. '), rows.length ? 'Pick another subject.' : 'Mark a mock paper, do a few ',
        ...(rows.length ? [] : [W.h('a', { href: '#practice.quiz' }, 'practice quizzes'), ', or tick the checklists in chapters you have learned. Then come back here.'])));
      return;
    }
    const ol = W.h('ol', { class: 'rn-list' });
    for (const t of list.slice(0, 15)) {
      const why = [];
      if (t.of) why.push(`lost ${t.lost} of ${t.of} marks in ${plural(t.mocks.size, 'mock')}`);
      if (t.qw) why.push(`${t.qw} of your last ${t.qn} quiz answers wrong`);
      if (t.ul) why.push(`${t.ul} of ${t.un} checklist lines not ticked`);
      const info = G.ch[t.c], subj = G.subjects.find(s => s.id === info.s);
      ol.append(W.h('li', {},
        W.h('div', { class: 'rn-t' }, W.h('a', { href: '#' + t.c }, info.t), subj && !nextSubj ? W.h('span', { class: 'rn-s' }, subj.short || subj.t) : ''),
        W.h('div', { class: 'rn-why' }, why.join(' · ')),
        W.h('span', { class: 'rn-bar', 'aria-hidden': 'true' }, W.h('i', { style: { width: (100 * t.score / top).toFixed(1) + '%' } }))));
    }
    body.append(ol);
    if (list.length > 15) body.append(W.h('p', { class: 'w-note' }, `${list.length - 15} more after these. Revise the top ones, then redo the questions you lost marks on.`));
  }

  /* ---------- spaced re-testing (on "What to revise next") ---------- */
  function renderRetests(host) {
    const now = Date.now();
    const due = retestsDue(now);
    const later = Object.keys(done).map(c => retestOf(c, now)).filter(r => r && !r.isDue).sort((a, b) => a.due - b.due);
    const body = W.h('div', { class: 'w-b' });
    host.append(W.h('div', { class: 'w' }, W.h('div', { class: 'w-h' }, W.h('span', { class: 'w-t' }, 'Due for a re-test'),
      W.h('span', { class: 'w-s' }, 'Quiz questions from chapters you marked as learned, 1, 3, 7 and 21 days later')), body));
    const days = (ms) => { const d = Math.max(1, Math.ceil(ms / DAY)); return d === 1 ? 'within a day' : `in ${d} days`; };
    const coming = later.length ? `${later.length} more chapter${later.length === 1 ? '' : 's'} to come; the next one is due ${days(later[0].due - now)}.` : '';
    if (!due.length) {
      body.append(W.h('p', {}, W.h('b', {}, 'Nothing is due today. '), coming || 'Mark a chapter as learned (the button at its end) and its quiz questions come back here after 1, 3, 7 and 21 days.'));
      return;
    }
    const ul = W.h('ul', { class: 'rt-list' });
    for (const r of due.slice(0, 8)) {
      const info = G.ch[r.c], subj = G.subjects.find(s => s.id === info.s);
      const late = Math.floor((now - r.due) / DAY);
      const btn = W.h('button', { class: 'btn btn-sm', type: 'button' }, 'Re-test now');
      const area = W.h('div', { class: 'rt-q' });
      const why = W.h('div', { class: 'rn-why' }, `Re-test ${r.n + 1} of ${RT_DAYS.length} (${RT_DAYS[r.n]} day${RT_DAYS[r.n] === 1 ? '' : 's'} after you learned it)` + (late > 0 ? ` · ${late} day${late === 1 ? '' : 's'} late` : ''));
      ul.append(W.h('li', {}, W.h('div', { class: 'rt-row' },
        W.h('div', { class: 'rn-t' }, W.h('a', { href: '#' + r.c }, info.t), subj ? W.h('span', { class: 'rn-s' }, subj.short || subj.t) : ''), btn), why, area));
      btn.addEventListener('click', () => {
        btn.disabled = true;
        (info.k ? ZTA.load(info.k) : Promise.resolve()).then(() => {
          // at most 6 of the chapter's questions, in a new order with the options shuffled
          const pick = W.shuffle(quizIds().filter(i => QUIZ[i].c === r.c)).slice(0, 6);
          if (!pick.length) { area.textContent = 'This chapter has no quiz questions.'; return; }
          btn.hidden = true;
          let right = 0, answered = 0;
          const qbox = W.h('div', { class: 'quiz-wrap' }), res = W.h('p', { class: 'rt-res', 'aria-live': 'polite' });
          area.append(qbox, res);
          renderQuizInto(qbox, pick, {
            shuffle: true, onAnswer: (ok) => {
              answered++; if (ok) right++;
              if (answered < pick.length) return;
              // this re-test is behind the reader, and so is every later one whose day has already passed
              const t0 = done[r.c];
              const passed = RT_DAYS.filter(d => Date.now() >= t0 + d * DAY).length;
              retest[r.c] = Math.max(r.n + 1, passed);
              store.set('retest', retest);
              const next = retestOf(r.c, Date.now());
              res.textContent = `${right} of ${pick.length} right. ` + (next ? `The next re-test of this chapter is due ${days(next.due - Date.now())}.` : 'That was the last re-test of this chapter.');
              if (right < 0.7 * pick.length) res.append(' Below 70%: ', W.h('a', { href: '#' + r.c }, 'reread the chapter'), next ? ' before the next one.' : ' and try its quiz again.');
              why.textContent = 'Done today.';
            }
          });
          focusOn(qbox);
        }, (e) => { btn.disabled = false; loadFailed(e); });
      });
    }
    body.append(ul);
    const rest = due.length > 8 ? `${due.length - 8} more are due after these. ` : '';
    if (rest || coming) body.append(W.h('p', { class: 'w-note' }, rest + coming));
  }

  // for settings.js
  W.ui = { toast, setTheme, setSize, renderProgress, refreshToc: () => { if (current) { buildToc(current); track(); } } };

  /* ---------- start ---------- */
  renderProgress();
  route();
  // open the current subject in the sidebar on first load
  if (current) openSubject(current.getAttribute('data-subject'), true);
})();
