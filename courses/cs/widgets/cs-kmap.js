/* widgets/cs-kmap.js: a Karnaugh map for 2, 3 or 4 variables with an exact solver.
   <div class="widget" data-w="cs-kmap" data-vars="3" data-ones="1,3,5,7"></div>
   data-vars: 2, 3 or 4 (default 3). data-ones: minterm numbers that are 1 (A is the most significant bit).
   The solver (object K) is pure and exported for the Node test (data/cs-kmap.test.js): it finds a minimal sum
   of products (fewest terms, then fewest literals) from the prime implicants. */
(function () {
  'use strict';

  const K = {};
  K.GRAY = [0, 1, 3, 2];
  K.NAMES = ['A', 'B', 'C', 'D'];

  // Prime implicants by repeated pairing. An implicant is {mask, val}: a 1 in mask means "variable dropped".
  K.primes = function (n, ones) {
    let cur = {};
    ones.forEach(function (m) { cur['0:' + m] = [0, m]; });
    const primes = {};
    while (Object.keys(cur).length) {
      const used = {};
      const next = {};
      const keys = Object.keys(cur);
      keys.forEach(function (k1) {
        const a = cur[k1];
        for (let bit = 0; bit < n; bit++) {
          const b = 1 << bit;
          if ((a[0] & b) || (a[1] & b)) continue;
          const partner = a[0] + ':' + (a[1] | b);
          if (cur[partner]) {
            next[(a[0] | b) + ':' + a[1]] = [a[0] | b, a[1]];
            used[k1] = 1;
            used[partner] = 1;
          }
        }
      });
      keys.forEach(function (k) { if (!used[k]) primes[k] = cur[k]; });
      cur = next;
    }
    return Object.keys(primes).map(function (k) { return primes[k]; })
      .sort(function (x, y) { return x[0] - y[0] || x[1] - y[1]; });
  };

  K.cells = function (n, imp) {
    const out = [];
    for (let m = 0; m < (1 << n); m++) if ((m & ~imp[0]) === imp[1]) out.push(m);
    return out;
  };

  K.literals = function (n, imp) {
    let dropped = 0;
    for (let i = 0; i < n; i++) if (imp[0] & (1 << i)) dropped++;
    return n - dropped;
  };

  // Returns an array of implicants [mask, val] forming a minimal cover, in a fixed order.
  K.solve = function (n, ones) {
    const set = {};
    ones.forEach(function (m) { set[m] = 1; });
    const list = Object.keys(set).map(Number).sort(function (a, b) { return a - b; });
    if (!list.length) return [];
    if (list.length === (1 << n)) return [[(1 << n) - 1, 0]];
    const pis = K.primes(n, list);
    const cov = pis.map(function (p) { return K.cells(n, p); });
    const lits = pis.map(function (p) { return K.literals(n, p); });
    const P = pis.length;
    for (let size = 1; size <= P; size++) {
      let best = null;
      const combo = [];
      const go = function (start) {
        if (combo.length === size) {
          const got = {};
          combo.forEach(function (i) { cov[i].forEach(function (m) { got[m] = 1; }); });
          for (let j = 0; j < list.length; j++) if (!got[list[j]]) return;
          let l = 0;
          combo.forEach(function (i) { l += lits[i]; });
          if (best === null || l < best.l) best = { l: l, c: combo.slice() };
          return;
        }
        for (let i = start; i < P; i++) { combo.push(i); go(i + 1); combo.pop(); }
      };
      go(0);
      if (best) return best.c.map(function (i) { return pis[i]; });
    }
    return [];
  };

  K.cost = function (n, groups) {
    let l = 0;
    groups.forEach(function (g) { l += K.literals(n, g); });
    return [groups.length, l];
  };

  // The product term of one group, as a list of literals.
  K.literalList = function (n, imp) {
    const out = [];
    for (let i = 0; i < n; i++) {
      const bit = 1 << (n - 1 - i);
      if (imp[0] & bit) continue;
      out.push({ name: K.NAMES[i], neg: !(imp[1] & bit) });
    }
    return out;
  };
  K.termWords = function (n, imp) {
    const l = K.literalList(n, imp);
    if (!l.length) return '1';
    return l.map(function (x) { return (x.neg ? 'NOT ' : '') + x.name; }).join(' AND ');
  };
  K.termAlg = function (n, imp) {
    const l = K.literalList(n, imp);
    if (!l.length) return '1';
    return l.map(function (x) { return (x.neg ? 'NOT ' : '') + x.name; }).join(' · ');
  };
  K.exprWords = function (n, groups) {
    if (!groups.length) return '0';
    if (groups.length === 1) return K.termWords(n, groups[0]);
    return groups.map(function (g) {
      const t = K.termWords(n, g);
      return K.literalList(n, g).length > 1 ? '(' + t + ')' : t;
    }).join(' OR ');
  };
  K.exprAlg = function (n, groups) {
    if (!groups.length) return '0';
    return groups.map(function (g) { return K.termAlg(n, g); }).join(' + ');
  };
  K.evalGroups = function (groups, m) {
    return groups.some(function (g) { return (m & ~g[0]) === g[1]; });
  };

  // Grid position of minterm m: {r, c} for n variables.
  K.layout = function (n) {
    if (n === 2) return { rows: [0, 1], cols: [0, 1], rowVars: 'A', colVars: 'B', cell: function (r, c) { return r * 2 + c; } };
    if (n === 3) return { rows: [0, 1], cols: K.GRAY, rowVars: 'A', colVars: 'BC', cell: function (r, c) { return r * 4 + c; } };
    return { rows: K.GRAY, cols: K.GRAY, rowVars: 'AB', colVars: 'CD', cell: function (r, c) { return r * 4 + c; } };
  };

  // Does a group wrap round an edge of the map (its cells are not one block in the printed grid)?
  K.wraps = function (n, cellsList) {
    const lay = K.layout(n);
    const rowsUsed = {};
    const colsUsed = {};
    cellsList.forEach(function (m) {
      for (let ri = 0; ri < lay.rows.length; ri++) {
        for (let ci = 0; ci < lay.cols.length; ci++) {
          if (lay.cell(lay.rows[ri], lay.cols[ci]) === m) { rowsUsed[ri] = 1; colsUsed[ci] = 1; }
        }
      }
    });
    const run = function (o) {
      const ks = Object.keys(o).map(Number).sort(function (a, b) { return a - b; });
      return ks[ks.length - 1] - ks[0] + 1 === ks.length;
    };
    return !(run(rowsUsed) && run(colsUsed));
  };

  K.parseOnes = function (text, n) {
    const s = String(text == null ? '' : text).trim();
    if (s === '') return { ones: [] };
    const parts = s.split(/[\s,;]+/).filter(function (x) { return x !== ''; });
    const ones = [];
    const max = (1 << n) - 1;
    for (let i = 0; i < parts.length; i++) {
      if (!/^\d+$/.test(parts[i])) return { error: '"' + parts[i] + '" is not a cell number. Type numbers such as 1, 3, 5, 7.' };
      const v = parseInt(parts[i], 10);
      if (v > max) return { error: 'Cell ' + v + ' does not exist on a ' + n + '-variable map. Use numbers from 0 to ' + max + '.' };
      if (ones.indexOf(v) < 0) ones.push(v);
    }
    return { ones: ones.sort(function (a, b) { return a - b; }) };
  };

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'Karnaugh map', 'Press a cell to switch it between 0 and 1, then press Solve');
    const body = frame.body;
    let n = parseInt(opts.vars, 10);
    if (n !== 2 && n !== 3 && n !== 4) n = 3;
    let ones = {};
    let solution = null;
    const startParsed = K.parseOnes(opts.ones, n);
    (startParsed.ones || [1, 3, 5, 7].filter(function (m) { return m < (1 << n); })).forEach(function (m) { ones[m] = 1; });
    if (opts.ones == null || String(opts.ones).trim() === '') {
      ones = {};
      (n === 2 ? [1, 3] : n === 3 ? [1, 3, 5, 7] : [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]).forEach(function (m) { ones[m] = 1; });
    }

    const tabs = W.h('div', { 'class': 'w-tabs' });
    tabs.setAttribute('role', 'group');
    tabs.setAttribute('aria-label', 'Number of variables');
    const tabBtn = {};
    [2, 3, 4].forEach(function (k) {
      const b = W.h('button', { 'class': 'w-tab', type: 'button', text: k + ' variables' });
      b.addEventListener('click', function () {
        if (k === n) return;
        n = k;
        const keep = {};
        Object.keys(ones).forEach(function (m) { if (+m < (1 << n)) keep[m] = 1; });
        ones = keep;
        solution = null;
        build();
        tabBtn[k].focus();
      });
      tabBtn[k] = b;
      tabs.appendChild(b);
    });
    body.appendChild(tabs);

    const typed = W.h('input', { type: 'text', value: '' });
    typed.setAttribute('autocomplete', 'off');
    typed.setAttribute('spellcheck', 'false');
    typed.setAttribute('size', '22');
    typed.style.maxWidth = '100%';
    const typedLab = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Cells that are 1 (cell numbers, for example 1, 3, 5, 7)' }), typed);
    const err = W.h('div', { 'class': 'w-err', 'aria-live': 'polite' });
    err.style.display = 'none';
    body.appendChild(typedLab);
    body.appendChild(err);

    const gridWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0', margin: '6px 0' } });
    body.appendChild(gridWrap);

    const solveBtn = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Solve' });
    const clearBtn = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Clear the map' });
    body.appendChild(W.h('div', { 'class': 'w-row', style: { alignItems: 'center' } }, solveBtn, clearBtn));
    const result = W.h('div', { 'aria-live': 'polite', style: { minWidth: '0', maxWidth: '100%' } });
    body.appendChild(result);
    body.appendChild(W.h('div', { 'class': 'w-note', text: 'Cells are numbered by the inputs read as a binary number (A is the leftmost digit). The headings run in Gray code, so only one variable changes between neighbours, and the left and right edges (and, with four variables, the top and bottom edges) are neighbours too. Each group of 1, 2, 4, 8 or 16 cells gives one product term.' }));

    function onesList() {
      return Object.keys(ones).map(Number).sort(function (a, b) { return a - b; });
    }

    function groupsOf(m) {
      const tags = [];
      if (solution) solution.groups.forEach(function (g, i) { if (g.cells.indexOf(m) >= 0) tags.push(i + 1); });
      return tags;
    }

    function build() {
      [2, 3, 4].forEach(function (k) { tabBtn[k].setAttribute('aria-pressed', k === n ? 'true' : 'false'); });
      paint();
    }

    function paint() {
      const lay = K.layout(n);
      const bin = function (v, w) { let s = v.toString(2); while (s.length < w) s = '0' + s; return s; };
      const rw = lay.rowVars.length;
      const cw = lay.colVars.length;
      typed.value = onesList().join(', ');
      gridWrap.textContent = '';
      const t = W.h('table', { style: { width: 'auto', borderCollapse: 'separate', borderSpacing: '3px' } });
      t.setAttribute('aria-label', 'Karnaugh map for ' + n + ' variables');
      const head = W.h('tr', {});
      head.appendChild(W.h('th', { text: lay.rowVars + ' \\ ' + lay.colVars, scope: 'col' }));
      lay.cols.forEach(function (c) { head.appendChild(W.h('th', { text: bin(c, cw), scope: 'col', style: { textAlign: 'center' } })); });
      t.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      lay.rows.forEach(function (r) {
        const tr = W.h('tr', {});
        tr.appendChild(W.h('th', { text: bin(r, rw), scope: 'row', style: { textAlign: 'center' } }));
        lay.cols.forEach(function (c) {
          const m = lay.cell(r, c);
          const v = ones[m] ? 1 : 0;
          const tags = groupsOf(m);
          const inGroup = tags.length > 0;
          const letters = [];
          for (let i = 0; i < n; i++) letters.push(K.NAMES[i] + ' = ' + ((m >> (n - 1 - i)) & 1));
          const b = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', style: { minWidth: '54px', minHeight: '54px', padding: '2px 4px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '0', lineHeight: '1.15', border: inGroup ? '3px solid var(--sc)' : '' } });
          b.appendChild(W.h('span', { text: String(v), style: { fontWeight: '700', fontSize: '1.2em' } }));
          b.appendChild(W.h('span', { text: '#' + m, style: { fontSize: '0.72em', color: 'var(--ink-2)' } }));
          b.appendChild(W.h('span', { text: inGroup ? 'G' + tags.join(',') : ' ', style: { fontSize: '0.72em', fontWeight: '700' } }));
          b.setAttribute('aria-label', 'Cell ' + m + ', ' + letters.join(', ') + ', value ' + v + (inGroup ? ', in group ' + tags.join(' and ') : '') + '. Press to change it.');
          b.setAttribute('aria-pressed', v ? 'true' : 'false');
          b.addEventListener('click', function () {
            if (ones[m]) delete ones[m]; else ones[m] = 1;
            solution = null;
            paint();
            const again = gridWrap.querySelectorAll('button')[findIndex(m)];
            if (again) again.focus();
            W.say(el, 'Cell ' + m + ' is now ' + (ones[m] ? 1 : 0) + '.');
          });
          tr.appendChild(W.h('td', { style: { padding: '0', textAlign: 'center' } }, b));
        });
        tb.appendChild(tr);
      });
      t.appendChild(tb);
      gridWrap.appendChild(t);
      paintResult();
    }

    function findIndex(m) {
      const lay = K.layout(n);
      let idx = 0;
      for (let ri = 0; ri < lay.rows.length; ri++) {
        for (let ci = 0; ci < lay.cols.length; ci++) {
          if (lay.cell(lay.rows[ri], lay.cols[ci]) === m) return idx;
          idx++;
        }
      }
      return 0;
    }

    function paintResult() {
      result.textContent = '';
      const list = onesList();
      if (!solution) {
        result.appendChild(W.h('div', { 'class': 'w-note', text: list.length ? 'The 1s are in cells ' + list.join(', ') + '. Press Solve to find the groups.' : 'Every cell is 0. Press a cell to make it 1.' }));
        return;
      }
      const lines = [];
      lines.push(W.h('div', { style: { fontWeight: '700' }, text: 'X = ' + K.exprWords(n, solution.raw) }));
      lines.push(W.h('div', { text: 'In Boolean algebra: X = ' + K.exprAlg(n, solution.raw) }));
      lines.push(W.h('div', { 'class': 'w-note', text: solution.raw.length + (solution.raw.length === 1 ? ' group, ' : ' groups, ') + K.cost(n, solution.raw)[1] + ' literals in total.' }));
      const ul = W.h('ul', {});
      solution.groups.forEach(function (g, i) {
        ul.appendChild(W.h('li', { text: 'Group ' + (i + 1) + ': cells ' + g.cells.join(', ') + ' (' + g.cells.length + ' cells' + (g.wrap ? ', wraps round the edge' : '') + ') → ' + g.words }));
      });
      result.appendChild(lines[0]);
      result.appendChild(lines[1]);
      result.appendChild(lines[2]);
      if (solution.groups.length) result.appendChild(ul);
    }

    function solveNow() {
      const list = onesList();
      const raw = K.solve(n, list);
      solution = {
        raw: raw,
        groups: raw.map(function (g) {
          const cells = K.cells(n, g);
          return { cells: cells, words: K.termWords(n, g), wrap: K.wraps(n, cells) };
        })
      };
      paint();
      W.say(el, 'Solved. X = ' + K.exprWords(n, raw) + '.');
    }

    solveBtn.addEventListener('click', solveNow);
    clearBtn.addEventListener('click', function () {
      ones = {};
      solution = null;
      err.style.display = 'none';
      err.textContent = '';
      paint();
      clearBtn.focus();
    });
    typed.addEventListener('input', function () {
      const p = K.parseOnes(typed.value, n);
      if (p.error) {
        err.textContent = p.error;
        err.style.display = '';
        return;
      }
      err.textContent = '';
      err.style.display = 'none';
      ones = {};
      p.ones.forEach(function (m) { ones[m] = 1; });
      solution = null;
      const keep = typed.value;
      paint();
      typed.value = keep;
    });

    build();
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-kmap', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = K;
})();
