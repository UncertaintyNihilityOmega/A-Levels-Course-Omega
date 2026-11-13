/* settings.js — the Settings page (#settings, last in the sidebar): appearance (theme, text size, subject colours,
   background, highlighter), progress (export, import, reset, keep my data), offline downloads (all, core only, per
   course; talks to sw.js). Appearance is stored as zta:look and applied as a <style> on :root. Runs after app.js. */
(function () {
  'use strict';
  const G = window.GUIDE || { subjects: [], chunks: [] };
  const W = window.W, store = W.store, ui = W.ui || {};
  const $ = (s, r) => (r || document).querySelector(s);
  const h = W.h;
  const root = document.documentElement;
  const toast = (m) => (ui.toast ? ui.toast(m) : null);

  /* ---------- colours ---------- */
  const rgb = (x) => [1, 3, 5].map((i) => parseInt(x.slice(i, i + 2), 16));
  const toHex = (c) => '#' + c.map((v) => Math.round(Math.max(0, Math.min(255, v))).toString(16).padStart(2, '0')).join('');
  const mixHex = (a, b, t) => { const x = rgb(a), y = rgb(b); return toHex(x.map((v, i) => v + (y[i] - v) * t)); };
  const lum = (x) => { const c = rgb(x).map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
  const contrast = (a, b) => { const p = lum(a), q = lum(b); return (Math.max(p, q) + 0.05) / (Math.min(p, q) + 0.05); };
  const isHex = (x) => typeof x === 'string' && /^#[0-9a-f]{6}$/i.test(x);
  /** a colour picked for paper mode, lightened for the chalkboard */
  const forDark = (x) => mixHex(x, '#ffffff', 0.55);

  // the default values, read from the stylesheet (:root = paper, :root[data-theme="dark"] = chalkboard)
  const DEF = { light: {}, dark: {} };
  try {
    for (const sh of document.styleSheets) for (const r of sh.cssRules || []) {
      const mode = r.selectorText === ':root' ? 'light' : r.selectorText === ':root[data-theme="dark"]' ? 'dark' : null;
      if (!mode) continue;
      for (let i = 0; i < r.style.length; i++) { const p = r.style[i]; if (p.startsWith('--')) DEF[mode][p] = r.style.getPropertyValue(p).trim(); }
    }
  } catch (e) { /* no CSSOM */ }
  const def = (mode, v) => { const x = DEF[mode][v] || DEF.light[v] || ''; return isHex(x) ? x.toLowerCase() : '#000000'; };

  const BLANK = () => ({ colors: {}, bg: { light: {}, dark: {} }, hl: null });
  let look = Object.assign(BLANK(), store.get('look', null) || {});
  if (!look.bg || typeof look.bg !== 'object') look.bg = { light: {}, dark: {} };
  look.bg.light = look.bg.light || {}; look.bg.dark = look.bg.dark || {};

  function applyLook() {
    const L = [], D = [];
    for (const [id, c] of Object.entries(look.colors || {})) if (isHex(c) && /^[\w-]+$/.test(id)) { L.push(`--c-${id}:${c}!important`); D.push(`--c-${id}:${forDark(c)}!important`); }
    for (const [mode, arr] of [['light', L], ['dark', D]]) for (const k of ['desk', 'sheet']) { const c = look.bg[mode][k]; if (isHex(c)) arr.push(`--${k}:${c}!important`); }
    if (isHex(look.hl)) {
      const [r, g, b] = rgb(look.hl);
      L.push(`--hl:${look.hl}!important`, `--hl-soft:rgba(${r},${g},${b},.42)!important`);
      D.push(`--hl:${forDark(look.hl)}!important`, `--hl-soft:rgba(${r},${g},${b},.2)!important`);
    }
    let css = '';
    // paper values only in paper mode (chosen, or the device's when it does not prefer dark)
    if (L.length) css += `:root[data-theme="light"]{${L.join(';')}}@media not all and (prefers-color-scheme: dark){:root:not([data-theme="dark"]){${L.join(';')}}}`;
    if (D.length) css += `:root[data-theme="dark"]{${D.join(';')}}@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){${D.join(';')}}}`;
    let el = document.getElementById('zta-look');
    if (!el) { el = document.createElement('style'); el.id = 'zta-look'; document.head.appendChild(el); }
    el.textContent = css;
    if (W.themeChanged) setTimeout(W.themeChanged, 30);
  }
  function saveLook() { store.set('look', look); applyLook(); }
  applyLook();

  /* ---------- small builders ---------- */
  const section = (title, sub) => {
    const s = h('section', { class: 'set-sec' }, h('h2', {}, title));
    if (sub) s.append(h('p', { class: 'set-sub' }, sub));
    return s;
  };
  const row = (label, ...ctl) => h('div', { class: 'set-row' }, h('div', { class: 'set-l' }, label), h('div', { class: 'set-c' }, ...ctl));
  const btn = (txt, fn, cls) => { const b = h('button', { type: 'button', class: 'btn btn-sm ' + (cls || 'btn-sec') }, txt); b.addEventListener('click', fn); return b; };
  let uid = 0;
  function colorInput(label, value, onPick) {
    const id = 'set-c' + (++uid);
    const inp = h('input', { type: 'color', id, value });
    inp.addEventListener('input', () => onPick(inp.value));
    return [h('label', { for: id, class: 'set-cl' }, label), inp];
  }
  const fmtMB = (n) => (n >= 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB');

  /* ---------- appearance ---------- */
  function appearance() {
    const s = section('Appearance', 'Saved on this device. Pick colours for paper mode; chalkboard (dark) mode uses a lighter version automatically.');
    const theme = h('select', { id: 'set-theme' },
      h('option', { value: '' }, 'Follow my device'), h('option', { value: 'light' }, 'Paper (light)'), h('option', { value: 'dark' }, 'Chalkboard (dark)'));
    theme.value = store.get('theme', null) || '';
    theme.addEventListener('change', () => ui.setTheme && ui.setTheme(theme.value || null));
    const size = h('select', { id: 'set-size' }, h('option', { value: 'm' }, 'Normal'), h('option', { value: 'l' }, 'Large'), h('option', { value: 'xl' }, 'Extra large'));
    size.value = store.get('size', null) || 'm';
    size.addEventListener('change', () => ui.setSize && ui.setSize(size.value));
    s.append(row(h('label', { for: 'set-theme' }, 'Theme'), theme), row(h('label', { for: 'set-size' }, 'Text size'), size));

    // subject colours: every section of the sidebar
    const grid = h('div', { class: 'set-grid' });
    for (const sub of G.subjects) {
      const cur = look.colors[sub.id] || def('light', '--c-' + sub.id);
      const [lab, inp] = colorInput(sub.t, cur, (v) => { look.colors[sub.id] = v; saveLook(); });
      grid.append(h('div', { class: 'set-sw s-' + sub.id }, inp, lab));
    }
    s.append(h('h3', {}, 'Course and section colours'), grid);

    // background: page (desk) and paper (sheet), per mode
    const bg = h('div', { class: 'set-grid' });
    const warn = h('p', { class: 'set-warn', role: 'status' });
    const ink = { light: def('light', '--ink'), dark: def('dark', '--ink') };
    const checkBg = () => {
      const bad = ['light', 'dark'].filter((m) => contrast(look.bg[m].sheet || def(m, '--sheet'), ink[m]) < 4.5);
      warn.textContent = bad.length ? `Text may be hard to read on the ${bad.map((m) => (m === 'light' ? 'paper-mode' : 'chalkboard')).join(' and ')} page colour. Pick a ${bad[0] === 'light' ? 'lighter' : 'darker'} one.` : '';
    };
    for (const [mode, name] of [['light', 'Paper mode'], ['dark', 'Chalkboard mode']]) for (const [k, what] of [['desk', 'background'], ['sheet', 'page']]) {
      const [lab, inp] = colorInput(`${name} ${what}`, look.bg[mode][k] || def(mode, '--' + k), (v) => { look.bg[mode][k] = v; saveLook(); checkBg(); });
      bg.append(h('div', { class: 'set-sw' }, inp, lab));
    }
    const [hlLab, hlInp] = colorInput('Highlighter', look.hl || def('light', '--hl'), (v) => { look.hl = v; saveLook(); });
    bg.append(h('div', { class: 'set-sw' }, hlInp, hlLab));
    s.append(h('h3', {}, 'Background and highlighter'), bg, warn);
    checkBg();
    s.append(h('div', { class: 'set-act' }, btn('Return to default', () => {
      look = BLANK(); store.set('look', null);
      if (ui.setTheme) ui.setTheme(null, true);
      if (ui.setSize) ui.setSize('m', true);
      applyLook(); render(); toast('Appearance back to default');
    }, 'btn-sec set-reset')));
    return s;
  }

  /* ---------- progress ---------- */
  const LOOK_KEYS = ['look', 'theme', 'size'];
  function allKeys() {
    const out = [];
    try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k && k.startsWith('zta:')) out.push(k.slice(4)); } } catch (e) { /* blocked */ }
    return out;
  }
  function progress() {
    const s = section('Progress', 'Your progress (chapters learned, quiz answers, checklists, mock marks) is saved only on this device and in this browser. Export it to keep a backup or to move it to another device.');
    const learned = Object.keys(store.get('done', {})).length;
    s.append(h('p', {}, h('b', {}, `${learned} chapter${learned === 1 ? '' : 's'} learned`), ' on this device.'));
    const file = h('input', { type: 'file', accept: '.json,application/json', class: 'sr-only', id: 'set-import', tabindex: '-1' });
    file.addEventListener('change', () => {
      const f = file.files && file.files[0];
      if (!f) return;
      f.text().then((txt) => {
        const d = JSON.parse(txt);
        if (!d || d.app !== 'zero-to-a-star' || typeof d.data !== 'object') throw new Error('not a Zero to A* progress file');
        if (!confirm('Replace the progress on this device with the progress in this file?')) return;
        for (const k of allKeys()) if (!LOOK_KEYS.includes(k)) localStorage.removeItem('zta:' + k);
        for (const [k, v] of Object.entries(d.data)) if (typeof v === 'string' && /^[\w:.-]+$/.test(k)) localStorage.setItem('zta:' + k, v);
        toast('Progress imported');
        setTimeout(() => location.reload(), 600);
      }).catch((e) => toast('Could not import: ' + e.message)).finally(() => { file.value = ''; });
    });
    s.append(h('div', { class: 'set-act' },
      btn('Export progress', () => {
        const data = {};
        for (const k of allKeys()) data[k] = localStorage.getItem('zta:' + k);
        const blob = new Blob([JSON.stringify({ app: 'zero-to-a-star', version: 1, exported: new Date().toISOString(), data }, null, 1)], { type: 'application/json' });
        const a = h('a', { href: URL.createObjectURL(blob), download: `zero-to-a-star-progress-${new Date().toISOString().slice(0, 10)}.json` });
        document.body.append(a); a.click(); a.remove();
        setTimeout(() => URL.revokeObjectURL(a.href), 4000);
        toast('Progress file saved');
      }),
      btn('Import progress', () => file.click()),
      btn('Clear progress', () => {
        if (!confirm('Delete all progress on this device (learned chapters, quiz answers, checklists, mock marks)? This cannot be undone. Export it first if you may want it back.')) return;
        for (const k of allKeys()) if (!LOOK_KEYS.includes(k)) localStorage.removeItem('zta:' + k);
        toast('Progress cleared');
        setTimeout(() => location.reload(), 600);
      }, 'btn-sec set-danger'), file));

    // storage the browser may clear when space runs low, unless it is persistent
    const st = h('p', { class: 'set-sub', role: 'status' });
    s.append(h('h3', {}, 'Keep my data safe'), st);
    const sm = navigator.storage;
    if (sm && sm.persisted) {
      const show = () => Promise.all([sm.persisted(), sm.estimate ? sm.estimate() : Promise.resolve(null)]).then(([p, est]) => {
        st.textContent = (p ? 'Protected: this browser will not delete your progress or offline copy to free space.' : 'Not protected yet: when the device is short of space, the browser may delete your progress and offline copy.')
          + (est && est.usage ? ` Using ${fmtMB(est.usage)} on this device.` : '');
        keep.hidden = p;
      });
      const keep = btn('Protect my data', () => sm.persist().then((ok) => { toast(ok ? 'Your data is protected' : 'The browser said no. Installing the guide (Add to Home Screen) usually allows it.'); show(); }));
      s.append(h('div', { class: 'set-act' }, keep));
      show();
    } else st.textContent = 'This browser cannot protect stored data. Export your progress now and then.';
    return s;
  }

  /* ---------- offline downloads ---------- */
  function swAsk(msg) {
    return navigator.serviceWorker.ready.then((reg) => new Promise((resolve, reject) => {
      const ch = new MessageChannel(), t = setTimeout(() => reject(new Error('no answer')), 120000);
      ch.port1.onmessage = (e) => { clearTimeout(t); if (e.data && e.data.type === 'error') reject(new Error(e.data.message)); else resolve(e.data); };
      (navigator.serviceWorker.controller || reg.active).postMessage(msg, [ch.port2]);
    }));
  }
  function offline() {
    const s = section('Offline downloads', 'Choose what this device keeps for use without internet. The core pages (home, roadmap, toolbox, practice) are always kept. A course you do not keep still opens when you are online.');
    const box = h('div', { class: 'set-off' });
    s.append(box);
    if (!/^https?:$/.test(location.protocol) || !('serviceWorker' in navigator)) {
      box.append(h('p', { class: 'set-sub' }, 'Offline downloads work on the published site (and in the installed app), not in this preview.'));
      return s;
    }
    const msg = h('p', { class: 'set-sub', role: 'status' }, 'Checking what is saved…');
    box.append(msg);
    const nameOf = (id) => { const x = G.subjects.find((t) => t.id === id); return x ? x.t : id; };
    let busy = false;
    function draw(st) {
      box.textContent = '';
      msg.textContent = '';
      const have = new Set(st.have);
      const coreFiles = st.files.filter((f) => !/^c\//.test(f));
      const coreSize = coreFiles.reduce((a, f) => a + (st.sizes[f] || 0), 0);
      const kept = (c) => st.keep === 'all' || st.keep.includes(c);
      const total = st.files.filter((f) => have.has(f)).reduce((a, f) => a + (st.sizes[f] || 0), 0);
      box.append(h('p', {}, h('b', {}, `${fmtMB(total)} saved for offline use`), ` (everything: ${fmtMB(st.files.reduce((a, f) => a + (st.sizes[f] || 0), 0))}).`));
      const list = h('ul', { class: 'set-dl' });
      list.append(h('li', {}, h('span', { class: 'set-dl-n' }, 'Core pages'), h('span', { class: 'set-dl-s' }, fmtMB(coreSize)), h('span', { class: 'set-dl-st ok' }, coreFiles.every((f) => have.has(f)) ? 'Saved' : 'Saving…')));
      for (const c of st.courses) {
        const f = `c/${c}.js`, id = 'set-k-' + c;
        const cb = h('input', { type: 'checkbox', id, checked: kept(c) });
        cb.addEventListener('change', () => send(st.courses.filter((x) => (x === c ? cb.checked : kept(x)))));
        list.append(h('li', {}, h('span', { class: 'set-dl-n' }, cb, h('label', { for: id }, nameOf(c))), h('span', { class: 'set-dl-s' }, fmtMB(st.sizes[f] || 0)),
          h('span', { class: 'set-dl-st' + (have.has(f) ? ' ok' : '') }, have.has(f) ? 'Saved' : kept(c) ? 'Saving…' : 'Online only')));
      }
      box.append(list, h('div', { class: 'set-act' },
        btn('Download everything', () => send('all'), 'btn'), btn('Core pages only', () => send([]))));
      box.append(msg);
    }
    function send(keep) {
      if (busy) return;
      busy = true;
      msg.textContent = 'Updating the offline copy… keep this page open.';
      if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(() => {});
      swAsk({ type: 'keep', keep }).then((st) => { busy = false; draw(st); msg.textContent = 'Offline copy updated.'; toast('Offline copy updated'); },
        (e) => { busy = false; msg.textContent = 'Could not update the offline copy (' + e.message + '). Check your connection and try again.'; });
    }
    swAsk({ type: 'status' }).then(draw, () => { msg.textContent = 'The offline copy is still being set up. Open this page again in a minute.'; });
    return s;
  }

  /* ---------- page ---------- */
  function render() {
    const body = $('#settingsBody');
    if (!body) return;
    body.textContent = '';
    body.append(appearance(), progress(), offline(),
      h('p', { class: 'set-sub set-ver' }, `Version of ${G.built || 'this build'}.`));
  }
  function onRoute() {
    const on = location.hash === '#settings';
    const link = $('.side-settings');
    if (link) { link.classList.toggle('active', on); if (on) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current'); }
    if (on) render();
  }
  window.addEventListener('hashchange', onRoute);
  onRoute();

  // tell the reader when the offline copy is ready or updated
  if ('serviceWorker' in navigator) navigator.serviceWorker.addEventListener('message', (e) => {
    const d = e.data || {};
    if (d.type === 'activated') toast(d.first ? 'Saved on this device: the guide now works offline' : 'Updated: the newest version is saved for offline use');
  });
})();
