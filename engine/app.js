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
  function effectiveDark() {
    const t = root.getAttribute('data-theme');
    if (t) return t === 'dark';
    try { return window.matchMedia('(prefers-color-scheme: dark)').matches; } catch (e) { return false; }
  }
  function syncThemeIcon() { if (!root.getAttribute('data-theme')) root.setAttribute('data-theme-auto', effectiveDark() ? 'dark' : 'light'); }
  $('#themeBtn').addEventListener('click', () => {
    const next = effectiveDark() ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    store.set('theme', next);
    toast(next === 'dark' ? 'Chalkboard mode' : 'Paper mode');
    setTimeout(W.themeChanged, 30);
  });
  $('#textBtn').addEventListener('click', () => {
    const cur = root.getAttribute('data-size') || 'm';
    const next = cur === 'm' ? 'l' : cur === 'l' ? 'xl' : 'm';
    if (next === 'm') root.removeAttribute('data-size'); else root.setAttribute('data-size', next);
    store.set('size', next === 'm' ? null : next);
    toast({ m: 'Text size: normal', l: 'Text size: large', xl: 'Text size: extra large' }[next]);
    setTimeout(W.themeChanged, 30);
  });
  syncThemeIcon();

  let toastT = 0;
  function toast(msg) {
    const t = $('#toast');
    t.textContent = msg; t.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(() => { t.hidden = true; }, 1800);
  }

  /* ---------- progress ---------- */
  let done = store.get('done', {});
  const trackable = new Set(G.order.filter(id => G.ch[id].f));
  function saveDone() { store.set('done', done); }
  function subjectStats(sid) {
    let n = 0, d = 0;
    for (const id of G.order) { if (G.ch[id].s === sid && trackable.has(id)) { n++; if (done[id]) d++; } }
    return { n, d };
  }
  function renderProgress() {
    for (const a of $$('.nav-g a[data-nav]')) a.classList.toggle('done', !!done[a.getAttribute('data-nav')]);
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
      for (const el of $$(`[data-cnt="${s.id}"]`)) el.textContent = n ? `${d} of ${n} learned` : 'Being written';
    }
    $('#sideProgTxt').textContent = `${td} of ${tn} chapters learned`;
    $('#sideProgBar').style.width = tn ? (100 * td / tn).toFixed(1) + '%' : '0';
  }
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-done]');
    if (!b) return;
    const id = b.getAttribute('data-done');
    if (done[id]) delete done[id]; else { done[id] = Date.now(); toast('Marked as learned'); }
    saveDone(); renderProgress();
  });

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
  const menuBtn = $('#menuBtn'), scrim = $('#scrim');
  function setDrawer(open) {
    app.classList.toggle('nav-open', open);
    scrim.hidden = !open;
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) { const a = $('.nav-g a.active'); if (a) a.scrollIntoView({ block: 'center' }); }
  }
  menuBtn.addEventListener('click', () => setDrawer(!app.classList.contains('nav-open')));
  scrim.addEventListener('click', () => setDrawer(false));

  /* ---------- quizzes ---------- */
  function renderQuizInto(el, idxs, opts) {
    opts = opts || {};
    el.innerHTML = '';
    idxs.forEach((qi, n) => {
      const q = QUIZ[qi]; if (!q) return;
      const box = W.h('div', { class: 'qz' });
      box.append(W.h('div', { class: 'qz-q', html: `<span class="qz-n">${opts.numbered === false ? '' : (n + 1) + '.'}</span>${q.q}` }));
      const opt = W.h('div', { class: 'qz-o', role: 'group' });
      const order = opts.shuffle ? W.shuffle(q.o.map((_, i) => i)) : q.o.map((_, i) => i);
      const btns = [];
      order.forEach((oi, k) => {
        const b = W.h('button', { class: 'qz-btn', type: 'button', html: `<span class="qz-k">${'ABCDEF'[k]}</span><span>${q.o[oi]}</span>` });
        b.addEventListener('click', () => {
          const right = oi === q.a;
          btns.forEach(x => { x.b.disabled = true; if (x.oi === q.a) x.b.classList.add('right'); });
          if (!right) b.classList.add('wrong');
          const ex = W.h('div', { class: 'qz-e ' + (right ? 'ok' : 'no'), html: `<b>${right ? 'Correct.' : 'Not quite.'}</b>${q.e || ''}` });
          box.append(ex);
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
    if (art.id === 'c-practice.quiz') ZTA.loadAll().then(() => initPractice(art), loadFailed);
    if (art.id === 'c-tools.glossary') ZTA.loadAll().then(() => initGlossary(art), loadFailed);
  }

  /* ---------- router ---------- */
  let current = null;
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
    for (const a of $$('.nav-g a.active')) a.classList.remove('active');
    const link = $(`.nav-g a[data-nav="${CSS.escape(cid)}"]`);
    if (link) link.classList.add('active');
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
    document.title = info && cid !== 'home' ? `${info.t} · Zero to A*` : 'Zero to A*';
    if (cid !== 'home') store.set('last', cid);
    if (sec) {
      const target = document.getElementById(sec);
      if (target) { requestAnimationFrame(() => target.scrollIntoView({ block: 'start' })); }
    } else if (changed) window.scrollTo(0, 0);
    if (cid === 'home') renderHome();
  }
  window.addEventListener('hashchange', route);
  function loadFailed(e) { toast(e.message + ' — keep the c folder next to index.html.'); }

  function buildToc(art) {
    rail.innerHTML = '';
    const hs = $$('.prose h2, .prose h3', art);
    if (spy) spy.disconnect();
    if (!hs.length) { $('#rail').style.visibility = 'hidden'; return; }
    $('#rail').style.visibility = 'visible';
    for (const h of hs) {
      const li = W.h('li', { class: h.tagName === 'H3' ? 'h3' : 'h2' }, W.h('a', { href: '#' + h.id, 'data-for': h.id }, h.textContent));
      rail.append(li);
    }
    const id = art.getAttribute('data-id');
    const info = G.ch[id];
    $('#railProg').textContent = info && info.w ? `About ${Math.max(1, Math.round(info.w / 200))} min read` : '';
    try {
      spy = new IntersectionObserver((entries) => {
        for (const e of entries) {
          if (e.isIntersecting) {
            for (const a of $$('.rail-toc a.on')) a.classList.remove('on');
            const a = $(`.rail-toc a[data-for="${CSS.escape(e.target.id)}"]`);
            if (a) a.classList.add('on');
          }
        }
      }, { rootMargin: '-70px 0px -70% 0px' });
      hs.forEach(h => spy.observe(h));
    } catch (e) { /* no observer */ }
  }

  /* ---------- home ---------- */
  let homeDrawn = false;
  function renderHome() {
    const list = $('#subjects');
    if (list && !list.children.length) {
      list.innerHTML = G.subjects.filter(s => s.c).map(s => {
        const open = s.first ? `<a class="subj" href="#${s.first}">` : '<div class="subj subj-soon">';
        return `<li class="s-${s.id}">${open}`
          + `<span class="subj-c">${W.esc(s.code === 'ALL' ? 'More' : s.code || '')}</span><span class="subj-t">${W.esc(s.t)}</span>`
          + `<span class="subj-d">${W.esc(s.desc || '')}</span>`
          + `<span class="subj-p"><span data-cnt="${s.id}"></span><span class="subj-bar"><span data-bar="${s.id}"></span></span>`
          + (s.n ? `<span>${s.n} of ${s.p} chapters ready</span>` : '') + `</span>${s.first ? '</a>' : '</div>'}</li>`;
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
        if (a) { a.href = '#' + last; a.textContent = G.ch[last].t; }
      } else box.hidden = true;
    }
  }

  /* ---------- search ---------- */
  const input = $('#searchInput'), results = $('#searchResults');
  let index = null, sel = -1, hits = [];
  function buildIndex() {
    index = [];
    for (const art of $$('.chapter')) {
      const id = art.getAttribute('data-id');
      const info = G.ch[id] || { t: id, s: art.getAttribute('data-subject') };
      const heads = $$('.prose h2, .prose h3', art).map(h => ({ id: h.id, t: h.textContent }));
      const text = (art.querySelector('.prose') || art).textContent.replace(/\s+/g, ' ');
      index.push({ id, t: info.t, s: info.s, heads, text, lt: info.t.toLowerCase(), lx: text.toLowerCase() });
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
  function showResults() {
    const q = input.value.trim();
    if (!q) { results.hidden = true; return; }
    hits = search(q); sel = -1;
    results.innerHTML = hits.length ? hits.map((r, i) => `<a class="sr s-${r.s}" role="option" id="sr${i}" href="${r.href}"><div class="sr-t"><span class="sr-s">${W.esc(subjShort(r.s))}</span><span>${W.esc(r.title)}</span></div>${r.html ? `<div class="sr-x">${r.html}</div>` : ''}</a>`).join('')
      : `<div class="sr-empty">No matches for “${W.esc(q)}”. Try a shorter word, or a topic name such as “moles” or “break-even”.</div>`;
    results.hidden = false;
  }
  let st = 0;
  input.addEventListener('input', () => { clearTimeout(st); st = setTimeout(showResults, 120); });
  input.addEventListener('focus', () => {
    ZTA.loadAll().then(() => { if (input.value.trim() && document.activeElement === input) showResults(); }, loadFailed);
    if (input.value.trim()) showResults();
  });
  document.addEventListener('zta:chunk', () => { index = null; renderProgress(); });
  input.addEventListener('keydown', (e) => {
    const items = $$('.sr', results);
    if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(items.length - 1, sel + 1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(0, sel - 1); }
    else if (e.key === 'Enter') { const it = items[sel >= 0 ? sel : 0]; if (it) { location.hash = it.getAttribute('href'); closeSearch(); } return; }
    else if (e.key === 'Escape') { closeSearch(); input.blur(); return; }
    else return;
    items.forEach((it, i) => it.setAttribute('aria-selected', i === sel ? 'true' : 'false'));
    if (items[sel]) items[sel].scrollIntoView({ block: 'nearest' });
  });
  function closeSearch() { results.hidden = true; }
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
    const count = W.h('div', { class: 'w-note' });
    const list = W.h('dl', {});
    const letters = W.h('div', { class: 'gl-letters' });
    const wrap = W.h('div', { class: 'w' }, W.h('div', { class: 'w-b' }, W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-ctl', style: { flex: '3 1 14rem' } }, W.h('label', {}, 'Search terms'), filt), W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Subject'), subjSel)), count));
    host.append(wrap, letters, list);
    function draw() {
      const q = filt.value.trim().toLowerCase(), s = subjSel.value;
      const shown = items.filter(i => (!s || i.s === s) && (!q || i.plain.toLowerCase().includes(q) || i.d.toLowerCase().includes(q)));
      count.textContent = `${shown.length} term${shown.length === 1 ? '' : 's'}`;
      const seen = new Set();
      list.innerHTML = shown.slice(0, 600).map(i => {
        const L = (i.plain[0] || '#').toUpperCase();
        const anchor = seen.has(L) ? '' : ` id="gl-${/[A-Z]/.test(L) ? L : 'num'}"`;
        seen.add(L);
        const subj = G.subjects.find(x => x.id === i.s);
        const ch = G.ch[i.c];
        return `<div class="gl-item s-${i.s}"${anchor}><dt>${i.t}<a href="#${i.c}">${W.esc(subj ? subj.short : '')} · ${W.esc(ch ? ch.t : '')}</a></dt><dd>${i.d}</dd></div>`;
      }).join('') + (shown.length > 600 ? `<p class="w-note">Showing the first 600 — type to narrow the list.</p>` : '');
      letters.innerHTML = [...seen].filter(l => /[A-Z]/.test(l)).map(l => `<a href="#tools.glossary" data-l="${l}">${l}</a>`).join('');
    }
    letters.addEventListener('click', (e) => { const a = e.target.closest('[data-l]'); if (!a) return; e.preventDefault(); const t = document.getElementById('gl-' + a.dataset.l); if (t) t.scrollIntoView({ block: 'start' }); });
    filt.addEventListener('input', draw); subjSel.addEventListener('change', draw);
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
    const startBtn = W.h('button', { class: 'btn', type: 'button' }, 'Start a quiz');
    const area = W.h('div', {});
    host.append(W.h('div', { class: 'w' }, W.h('div', { class: 'w-h' }, W.h('span', { class: 'w-t' }, 'Mixed practice'), W.h('span', { class: 'w-s' }, 'Questions are drawn at random from every chapter')),
      W.h('div', { class: 'w-b' }, W.h('div', { class: 'w-row' }, W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Subject'), subjSel), W.h('div', { class: 'w-ctl' }, W.h('label', {}, 'Length'), nSel), startBtn), area)));
    if (!all.length) { area.append(W.h('p', { class: 'w-note' }, 'Quizzes will appear here as chapters are added.')); return; }
    startBtn.addEventListener('click', () => {
      const pool = all.filter(i => !subjSel.value || QUIZ[i].s === subjSel.value);
      const pick = W.shuffle(pool).slice(0, +nSel.value);
      let right = 0, answered = 0;
      const wrongCh = new Map();
      area.innerHTML = '';
      const score = W.h('div', { class: 'pq-score' }, `0 / ${pick.length}`);
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

  /* ---------- start ---------- */
  renderProgress();
  route();
  // open the current subject in the sidebar on first load
  if (current) openSubject(current.getAttribute('data-subject'), true);
})();
