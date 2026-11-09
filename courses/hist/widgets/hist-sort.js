/* hist-sort: sort statements into categories, then check with explanations. No dragging: every statement has one button per category.
   <div class="widget" data-w="hist-sort" data-title="Which school would write this?"
        data-cats="Fischer thesis,Shared responsibility,Contingency"
        data-items="statement | correct category | short explanation ;; statement | category | explanation"></div>
   2 to 5 categories separated by commas; statements separated by " ;; ", fields by " | " (the explanation is optional). */
(function () {
  'use strict';

  // "a, b, c" -> {cats, problems}
  function parseCats(raw) {
    const cats = [];
    const problems = [];
    String(raw || '').split(',').forEach(function (s) {
      const c = s.trim();
      if (c && cats.indexOf(c) < 0) cats.push(c);
    });
    if (cats.length < 2) problems.push('data-cats needs at least two categories separated by commas.');
    if (cats.length > 5) { problems.push('data-cats can hold at most five categories; the extra ones were ignored.'); cats.length = 5; }
    return { cats: cats, problems: problems };
  }

  // "text | category | explanation ;; …" -> {items:[{text, cat, why}], problems}
  function parseItems(raw, cats) {
    const items = [];
    const problems = [];
    String(raw || '').split(';;').map(function (s) { return s.trim(); }).filter(Boolean).forEach(function (part, i) {
      const f = part.split('|').map(function (s) { return s.trim(); });
      const ci = cats.indexOf(f[1] || '');
      if (!f[0] || ci < 0) {
        problems.push('Statement ' + (i + 1) + ' ("' + part.slice(0, 40) + (part.length > 40 ? '…' : '') + '") needs text and one of the categories.');
        return;
      }
      items.push({ text: f[0], cat: ci, why: f.slice(2).join(' | ') });
    });
    return { items: items, problems: problems };
  }

  W.register('hist-sort', function (el, opts) {
    const get = function (k) { return el.getAttribute('data-' + k) || (opts && (opts[k] || opts['data-' + k])) || ''; };
    const title = get('title') || 'Sort the statements';
    const frame = W.frame(el, title, 'Choose a category for each statement, then press Check.');
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

    const pc = parseCats(get('cats'));
    const cats = pc.cats;
    const pi = parseItems(get('items'), cats);
    const items = pi.items;
    const problems = pc.problems.concat(pi.problems);

    if (cats.length < 2 || !items.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'This exercise needs data-cats (two to five categories) and data-items written as: statement | category | explanation ;; statement | category | explanation.' }));
      if (problems.length) body.appendChild(mk('p', { class: 'w-err', text: problems.slice(0, 3).join(' ') }));
      return;
    }
    if (problems.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: problems.slice(0, 3).join(' ') }));
    }

    const choice = items.map(function () { return -1; });   // chosen category index, or -1
    const shown = items.map(function () { return false; });  // result visible for this statement
    let order = items.map(function (x, i) { return i; });
    let anyChecked = false;

    const list = mk('ol', { 'aria-label': 'Statements to sort', style: { margin: '6px 0 0', padding: '0 0 0 22px' } });
    const score = mk('p', { class: 'w-lab', 'aria-live': 'polite', 'aria-atomic': 'true', style: { margin: '8px 0 0', color: 'var(--ink-2)', fontWeight: '600' }, text: '0 of ' + items.length + ' answered.' });
    const rows = [];   // per statement: {li, btns, result}

    function answered() { return choice.filter(function (c) { return c >= 0; }).length; }

    function paintChoices(i) {
      rows[i].btns.forEach(function (b, ci) { b.setAttribute('aria-pressed', choice[i] === ci ? 'true' : 'false'); });
    }

    function paintResult(i) {
      const r = rows[i].result;
      r.textContent = '';
      if (!shown[i]) { r.style.display = 'none'; return; }
      r.style.display = '';
      const it = items[i];
      if (choice[i] < 0) {
        r.appendChild(mk('strong', { text: '– Not answered. ' }));
        r.appendChild(document.createTextNode('Correct category: ' + cats[it.cat] + '.'));
      } else if (choice[i] === it.cat) {
        r.appendChild(mk('strong', { style: { color: 'var(--ok)' }, text: '✓ Right. ' }));
        r.appendChild(document.createTextNode('Category: ' + cats[it.cat] + '.'));
      } else {
        r.appendChild(mk('strong', { style: { color: 'var(--red)' }, text: '✗ Not quite. ' }));
        r.appendChild(document.createTextNode('You chose ' + cats[choice[i]] + '; the correct category is ' + cats[it.cat] + '.'));
      }
      if (it.why) r.appendChild(mk('div', { style: { marginTop: '2px', color: 'var(--ink-2)' }, text: it.why }));
    }

    function updateScore(afterCheck) {
      if (afterCheck) {
        const right = items.filter(function (it, i) { return choice[i] === it.cat; }).length;
        score.textContent = 'Score: ' + right + ' of ' + items.length + ' right.' + (answered() < items.length ? ' ' + (items.length - answered()) + ' not answered.' : '');
      } else if (anyChecked) {
        score.textContent = 'Choices changed. Press Check to see your score.';
      } else {
        score.textContent = answered() + ' of ' + items.length + ' answered.';
      }
    }

    function choose(i, ci) {
      if (i < 0 || i >= items.length || ci < 0 || ci >= cats.length) return;
      choice[i] = choice[i] === ci ? -1 : ci;   // pressing the chosen button again clears it
      shown[i] = false;
      paintChoices(i);
      paintResult(i);
      updateScore(false);
    }

    function check() {
      anyChecked = true;
      items.forEach(function (it, i) { shown[i] = true; paintResult(i); });
      updateScore(true);
    }

    function reset() {
      anyChecked = false;
      order = items.map(function (x, i) { return i; });
      items.forEach(function (it, i) { choice[i] = -1; shown[i] = false; paintChoices(i); paintResult(i); });
      renderOrder();
      updateScore(false);
    }

    function shuffle() {
      order = W.shuffle ? W.shuffle(order.slice()) : order.slice().reverse();
      renderOrder();
    }

    function renderOrder() {
      list.textContent = '';
      order.forEach(function (i) { list.appendChild(rows[i].li); });
    }

    items.forEach(function (it, i) {
      const tid = W.uid ? W.uid('hist-sort') : 'hist-sort-' + i;
      const text = mk('div', { id: tid, style: { fontWeight: '600', marginBottom: '4px' }, text: it.text });
      const group = mk('div', { class: 'w-tabs', role: 'group', 'aria-labelledby': tid });
      const btns = cats.map(function (c, ci) {
        const b = mk('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false', text: c });
        b.onclick = function () { choose(i, ci); };
        group.appendChild(b);
        return b;
      });
      const result = mk('div', { style: { display: 'none', marginTop: '4px', fontSize: '0.92em' } });
      const li = mk('li', { style: { margin: '0 0 14px', paddingLeft: '2px' } }, text, mk('div', { class: 'w-row' }, group), result);
      rows[i] = { li: li, btns: btns, result: result };
    });
    renderOrder();
    body.appendChild(list);

    const checkBtn = mk('button', { type: 'button', class: 'btn btn-sm', text: 'Check' });
    const resetBtn = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset' });
    const shuffleBtn = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Shuffle' });
    checkBtn.onclick = check;
    resetBtn.onclick = reset;
    shuffleBtn.onclick = shuffle;
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, checkBtn, resetBtn, shuffleBtn));
    body.appendChild(score);
    body.appendChild(mk('p', { class: 'w-note', text: 'Try: sort all the statements before you press Check. Pressing a chosen button again clears it. Reset starts again; Shuffle changes the order.' }));

    // test hook for Node-style checks (no effect on readers)
    el.__histSort = {
      parseCats: parseCats, parseItems: parseItems, choose: choose, check: check, reset: reset, shuffle: shuffle,
      state: function () { return { choice: choice.slice(), shown: shown.slice(), order: order.slice(), score: score.textContent }; }
    };
  });
})();
