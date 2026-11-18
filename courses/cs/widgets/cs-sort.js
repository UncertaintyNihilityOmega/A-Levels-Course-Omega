/* widgets/cs-sort.js: bubble sort, insertion sort, binary search and linear search, step by step, with counters.
   <div class="widget" data-w="cs-sort" data-algo="insertion" data-values="29,10,14,37,13,5" data-target="35"></div>
   data-algo: bubble, insertion, binary or linear (the tab shown first; anything else gives bubble).
   data-values: 5 to 12 whole numbers from 1 to 99 (an invalid list falls back to the default for that kind).
   data-target: the number to look for in the two searches (default 35 for binary, 13 for linear).
   The algorithms (object S) are pure, count comparisons exactly as the chapter cs.algorithms2 does, and are exported for a
   Node test (data/cs-sort.test.js). Nothing throws: bad input returns {error}. */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure model
  // ---------------------------------------------------------------------------------------------
  const S = {};
  S.ALGOS = ['bubble', 'insertion', 'binary', 'linear'];
  S.NAMES = { bubble: 'Bubble sort', insertion: 'Insertion sort', binary: 'Binary search', linear: 'Linear search' };
  S.MIN = 5;
  S.MAX = 12;
  S.MAXVAL = 99;
  S.DEFAULT_SORT = [29, 10, 14, 37, 13, 5];
  S.DEFAULT_BINARY = [3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55];
  S.DEFAULT_LINEAR = [29, 10, 14, 37, 13, 5];
  S.isSort = function (algo) { return algo === 'bubble' || algo === 'insertion'; };
  S.algoOf = function (v) {
    const a = String(v == null ? '' : v).trim().toLowerCase();
    return S.ALGOS.indexOf(a) >= 0 ? a : 'bubble';
  };

  // Returns {values} or {error}
  S.parseValues = function (text) {
    if (text == null) return { error: 'Type 5 to 12 whole numbers from 1 to 99, separated by commas.' };
    const parts = String(text).split(/[\s,;]+/).filter(function (s) { return s !== ''; });
    if (parts.length < S.MIN || parts.length > S.MAX) return { error: 'Use ' + S.MIN + ' to ' + S.MAX + ' numbers (you typed ' + parts.length + ').' };
    const values = [];
    for (let i = 0; i < parts.length; i++) {
      if (!/^\d{1,2}$/.test(parts[i])) return { error: '"' + String(parts[i]).slice(0, 12) + '" is not a whole number from 1 to 99.' };
      const n = parseInt(parts[i], 10);
      if (n < 1 || n > S.MAXVAL) return { error: parts[i] + ' is outside 1 to 99.' };
      values.push(n);
    }
    return { values: values };
  };
  S.parseTarget = function (text) {
    const s = String(text == null ? '' : text).trim();
    if (!/^\d{1,2}$/.test(s)) return { error: 'The target must be a whole number from 1 to 99.' };
    const n = parseInt(s, 10);
    if (n < 1) return { error: 'The target must be a whole number from 1 to 99.' };
    return { target: n };
  };

  // Seeded random numbers (mulberry32) so "random" is the same every time for the same seed.
  S.prng = function (seed) {
    let a = (seed >>> 0) || 1;
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      let t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };
  // kind: 'sorted' | 'reversed' | 'random'; n items (5 to 12); distinct values from 1 to 99
  S.dataset = function (kind, n, seed) {
    n = Math.max(S.MIN, Math.min(S.MAX, Math.round(Number(n)) || 8));
    const r = S.prng(seed == null ? 1 : seed);
    const pool = [];
    for (let i = 1; i <= S.MAXVAL; i++) pool.push(i);
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(r() * (i + 1));
      const t = pool[i]; pool[i] = pool[j]; pool[j] = t;
    }
    const picked = pool.slice(0, n);
    const asc = picked.slice().sort(function (x, y) { return x - y; });
    if (kind === 'sorted') return asc;
    if (kind === 'reversed') return asc.slice().reverse();
    let out = picked.slice();
    let isAsc = true;
    for (let i = 1; i < out.length; i++) if (out[i - 1] > out[i]) isAsc = false;
    if (isAsc) out = out.slice(1).concat(out.slice(0, 1));
    return out;
  };

  function mk(a, extra) {
    const st = { arr: a.slice(), gap: -1, held: null, cmp: [], sorted: [], low: -1, mid: -1, high: -1, found: -1, comps: 0, moves: 0, text: '' };
    for (const k in extra) st[k] = extra[k];
    return st;
  }
  function flags(n, from, to) {
    const f = [];
    for (let i = 0; i < n; i++) f.push(i >= from && i <= to);
    return f;
  }

  // Each algorithm returns {steps: [...], result: ...}; a step is a snapshot of everything the widget draws.
  S.bubble = function (values) {
    const a = values.slice();
    const n = a.length;
    const steps = [];
    let comps = 0, moves = 0;
    steps.push(mk(a, { sorted: flags(n, 1, 0), comps: 0, moves: 0, text: 'Start. Compare neighbouring values from the left and swap any pair that is in the wrong order. Press Step.' }));
    let boundary = n - 1;
    let noSwaps = false;
    let pass = 0;
    while (!noSwaps && boundary > 0) {
      noSwaps = true;
      pass += 1;
      for (let j = 0; j < boundary; j++) {
        comps += 1;
        const x = a[j], y = a[j + 1];
        let msg;
        if (x > y) {
          a[j] = y; a[j + 1] = x; moves += 1; noSwaps = false;
          msg = 'Pass ' + pass + ': compare ' + x + ' and ' + y + ' (positions ' + (j + 1) + ' and ' + (j + 2) + '). ' + x + ' is greater, so swap them.';
        } else {
          msg = 'Pass ' + pass + ': compare ' + x + ' and ' + y + ' (positions ' + (j + 1) + ' and ' + (j + 2) + '). They are in order, so no swap.';
        }
        steps.push(mk(a, { cmp: [j, j + 1], sorted: flags(n, boundary + 1, n - 1), comps: comps, moves: moves, text: msg }));
      }
      const fixed = boundary;
      boundary -= 1;
      let end = 'End of pass ' + pass + ': the largest unsorted value is now in place at position ' + (fixed + 1) + '.';
      if (noSwaps) end += ' No swaps were made, so the array is sorted and the sort stops.';
      steps.push(mk(a, { sorted: noSwaps ? flags(n, 0, n - 1) : flags(n, fixed, n - 1), comps: comps, moves: moves, text: end }));
    }
    steps.push(mk(a, { sorted: flags(n, 0, n - 1), comps: comps, moves: moves, text: 'Sorted: ' + comps + ' comparisons and ' + moves + ' swaps.' }));
    return { steps: steps, result: a, comps: comps, moves: moves };
  };

  S.insertion = function (values) {
    const a = values.slice();
    const n = a.length;
    const steps = [];
    let comps = 0, moves = 0;
    steps.push(mk(a, { sorted: flags(n, 0, 0), comps: 0, moves: 0, text: 'Start. The first value alone is a sorted part. Each pass takes the next value and slides it into place in the sorted part. Press Step.' }));
    for (let index = 1; index < n; index++) {
      const item = a[index];
      let position = index - 1;
      a[index] = null;
      let gap = index;
      steps.push(mk(a, { gap: gap, held: item, sorted: flags(n, 0, index).map(function (f, i) { return f && i !== gap; }), comps: comps, moves: moves,
        text: 'Pass ' + index + ': take out ' + item + ' (position ' + (index + 1) + '). The gap is at position ' + (gap + 1) + '. Compare it with the values on its left.' }));
      let stopped = false;
      while (position >= 0 && !stopped) {
        comps += 1;
        const v = a[position];
        if (v > item) {
          a[position + 1] = v; a[position] = null; gap = position; moves += 1;
          steps.push(mk(a, { cmp: [position + 1], gap: gap, held: item, sorted: flags(n, 0, index).map(function (f, i) { return f && i !== gap; }), comps: comps, moves: moves,
            text: 'Compare ' + v + ' with ' + item + ': ' + v + ' is greater, so shift it one place right.' }));
          position -= 1;
        } else {
          steps.push(mk(a, { cmp: [position], gap: gap, held: item, sorted: flags(n, 0, index).map(function (f, i) { return f && i !== gap; }), comps: comps, moves: moves,
            text: 'Compare ' + v + ' with ' + item + ': ' + v + ' is not greater, so the gap is in the right place.' }));
          stopped = true;
        }
      }
      a[gap] = item;
      steps.push(mk(a, { sorted: flags(n, 0, index), comps: comps, moves: moves,
        text: (position < 0 ? 'No value is left on the left. ' : '') + 'Insert ' + item + ' at position ' + (gap + 1) + '. The sorted part is now positions 1 to ' + (index + 1) + '.' }));
    }
    steps.push(mk(a, { sorted: flags(n, 0, n - 1), comps: comps, moves: moves, text: 'Sorted: ' + comps + ' comparisons and ' + moves + ' shifts.' }));
    return { steps: steps, result: a, comps: comps, moves: moves };
  };

  S.binary = function (values, target) {
    const a = values.slice().sort(function (x, y) { return x - y; });
    const n = a.length;
    const steps = [];
    let comps = 0;
    let low = 0, high = n - 1;
    steps.push(mk(a, { low: low, high: high, comps: 0, text: 'Start: looking for ' + target + '. Low is 1 and High is ' + n + '. Press Step.' }));
    let found = -1;
    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      comps += 1;
      const v = a[mid];
      let msg = 'Low = ' + (low + 1) + ', High = ' + (high + 1) + ', so Mid = (' + (low + 1) + ' + ' + (high + 1) + ') DIV 2 = ' + (mid + 1) + '. Values[' + (mid + 1) + '] is ' + v + ', ';
      const st = { cmp: [mid], low: low, mid: mid, high: high, comps: comps };
      if (v === target) {
        found = mid;
        msg += 'which equals ' + target + ': found at position ' + (mid + 1) + '.';
        st.found = mid;
        st.text = msg;
        steps.push(mk(a, st));
        break;
      } else if (v < target) {
        msg += 'which is less than ' + target + ', so everything up to Mid is too small: Low becomes ' + (mid + 2) + '.';
        low = mid + 1;
      } else {
        msg += 'which is greater than ' + target + ', so everything from Mid on is too big: High becomes ' + mid + '.';
        high = mid - 1;
      }
      st.text = msg;
      steps.push(mk(a, st));
    }
    if (found < 0) {
      steps.push(mk(a, { low: low, high: high, comps: comps, text: 'Low (' + (low + 1) + ') is now greater than High (' + (high + 1) + '), so no values are left: ' + target + ' is not in the array. ' + comps + ' comparisons.' }));
    } else {
      steps[steps.length - 1].text += ' ' + comps + ' comparisons.';
    }
    return { steps: steps, result: found < 0 ? -1 : found + 1, comps: comps, moves: 0, sortedValues: a };
  };

  S.linear = function (values, target) {
    const a = values.slice();
    const n = a.length;
    const steps = [];
    let comps = 0;
    steps.push(mk(a, { comps: 0, text: 'Start: looking for ' + target + '. Check each value in turn from the first. Press Step.' }));
    let found = -1;
    for (let i = 0; i < n; i++) {
      comps += 1;
      if (a[i] === target) {
        found = i;
        steps.push(mk(a, { cmp: [i], found: i, comps: comps, text: 'Position ' + (i + 1) + ' holds ' + a[i] + ', which equals ' + target + ': found. ' + comps + ' comparisons.' }));
        break;
      }
      steps.push(mk(a, { cmp: [i], comps: comps, text: 'Position ' + (i + 1) + ' holds ' + a[i] + ', not ' + target + '. Move on.' }));
    }
    if (found < 0) steps.push(mk(a, { comps: comps, text: 'Every value has been checked: ' + target + ' is not in the array. ' + comps + ' comparisons.' }));
    return { steps: steps, result: found < 0 ? -1 : found + 1, comps: comps, moves: 0 };
  };

  S.run = function (algo, values, target) {
    if (algo === 'insertion') return S.insertion(values);
    if (algo === 'binary') return S.binary(values, target);
    if (algo === 'linear') return S.linear(values, target);
    return S.bubble(values);
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  function init(el, opts) {
    opts = opts || {};
    let algo = S.algoOf(opts.algo);
    let sortVals = S.DEFAULT_SORT.slice();
    let binVals = S.DEFAULT_BINARY.slice();
    let linVals = S.DEFAULT_LINEAR.slice();
    const given = S.parseValues(opts.values);
    if (!given.error) {
      if (algo === 'binary') binVals = given.values;
      else if (algo === 'linear') linVals = given.values;
      else sortVals = given.values;
    }
    let binTarget = 35, linTarget = 13;
    const gt = S.parseTarget(opts.target);
    if (!gt.error) { if (algo === 'binary') binTarget = gt.target; else if (algo === 'linear') linTarget = gt.target; }

    const frame = W.frame(el, 'Sorting and searching', 'Step through the algorithm and watch the counters');
    const body = frame.body;
    let steps = [];
    let k = 0;
    let timer = null;
    let seed = 1;

    function valsOf() { return algo === 'binary' ? binVals : (algo === 'linear' ? linVals : sortVals); }
    function setVals(v) { if (algo === 'binary') binVals = v; else if (algo === 'linear') linVals = v; else sortVals = v; }
    function targetOf() { return algo === 'binary' ? binTarget : linTarget; }

    // ----- tabs
    const tabsEl = W.h('div', { 'class': 'w-tabs', role: 'group', 'aria-label': 'Choose an algorithm', style: { display: 'flex', flexWrap: 'wrap', maxWidth: '100%', gap: '4px' } });
    const tabBtns = {};
    S.ALGOS.forEach(function (name) {
      const b = W.h('button', { type: 'button', 'class': 'w-tab', text: name === 'bubble' ? 'Bubble' : (name === 'insertion' ? 'Insertion' : (name === 'binary' ? 'Binary' : 'Linear')) });
      b.setAttribute('aria-label', S.NAMES[name]);
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () { setAlgo(name); });
      tabBtns[name] = b;
      tabsEl.appendChild(b);
    });
    body.appendChild(tabsEl);

    // ----- inputs
    const valIn = W.h('input', { type: 'text', value: '' });
    valIn.setAttribute('autocomplete', 'off');
    valIn.setAttribute('spellcheck', 'false');
    valIn.setAttribute('maxlength', '60');
    valIn.style.width = '100%'; valIn.style.maxWidth = '100%'; valIn.style.boxSizing = 'border-box';
    const valLab = W.h('label', { 'class': 'w-ctl', style: { flex: '1 1 14em', minWidth: '0', maxWidth: '100%' } },
      W.h('span', { 'class': 'w-lab', text: 'Values (5 to 12 whole numbers, 1 to 99)', style: { whiteSpace: 'normal' } }), valIn);
    const tgtIn = W.h('input', { type: 'text', value: '' });
    tgtIn.setAttribute('autocomplete', 'off');
    tgtIn.setAttribute('inputmode', 'numeric');
    tgtIn.setAttribute('maxlength', '2');
    tgtIn.style.width = '5em';
    const tgtLab = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Target' }), tgtIn);
    const err = W.h('div', { 'class': 'w-err', role: 'alert', style: { display: 'none' } });

    const dataBtns = W.h('div', { 'class': 'w-row', role: 'group', 'aria-label': 'Starting order of the data', style: { alignItems: 'center' } });
    [['sorted', 'Already sorted'], ['reversed', 'Reversed'], ['random', 'Random']].forEach(function (p) {
      const b = W.h('button', { type: 'button', 'class': 'btn btn-sm btn-sec', text: p[1] });
      b.addEventListener('click', function () {
        const n = valsOf().length;
        if (p[0] === 'random') { seed += 1; }
        setVals(S.dataset(p[0], n, p[0] === 'random' ? seed : 1));
        syncInputs();
        rebuild();
      });
      dataBtns.appendChild(b);
    });
    body.appendChild(W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-end' } }, valLab, tgtLab));
    body.appendChild(err);
    body.appendChild(dataBtns);

    // ----- chart
    const chart = W.h('div', { role: 'img', style: { display: 'flex', alignItems: 'flex-end', gap: '3px', margin: '12px 0 2px', width: '100%', maxWidth: '100%', minWidth: '0' } });
    const chartWrap = W.h('div', { style: { width: '100%', maxWidth: '100%', minWidth: '0', overflow: 'hidden' } }, chart);
    body.appendChild(chartWrap);
    body.appendChild(W.h('div', { 'class': 'w-note', text: 'Under each bar: its position, then a tag. C = being compared, S = in the sorted part, L, M, H = Low, Mid, High, F = found, and a dashed box is the gap that the held value will fill.' }));

    // ----- text, controls, counters
    const text = W.h('div', { 'aria-live': 'polite', style: { minHeight: '3.6em', margin: '8px 0' } });
    const back = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Back' });
    const next = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Step' });
    const run = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Run' });
    const reset = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Reset' });
    const lab = W.h('span', { 'class': 'w-step', 'aria-live': 'off' });
    const bar = W.h('div', { 'class': 'w-row', style: { alignItems: 'center', flexWrap: 'wrap', gap: '6px' } }, back, next, run, reset, lab);
    const stComps = W.stat('Comparisons');
    const stSwaps = W.stat('Swaps');
    const stShifts = W.stat('Shifts');
    const out = W.h('div', { 'class': 'w-out' }, stComps.el, stSwaps.el, stShifts.el);
    body.appendChild(text);
    body.appendChild(bar);
    body.appendChild(out);
    const note = W.h('p', { 'class': 'w-note' });
    body.appendChild(note);

    function stopTimer() {
      if (timer) { clearTimeout(timer); timer = null; }
      run.textContent = 'Run';
      run.setAttribute('aria-label', 'Run the algorithm automatically');
    }
    function tick() {
      timer = null;
      if (!el.isConnected) return;
      if (k >= steps.length - 1) { stopTimer(); return; }
      go(k + 1);
      if (k >= steps.length - 1) { stopTimer(); return; }
      timer = setTimeout(tick, 700);
    }

    function describe(st) {
      const arr = st.arr.map(function (v) { return v == null ? 'gap' : String(v); }).join(', ');
      let s = S.NAMES[algo] + '. Values by position: ' + arr + '.';
      if (st.cmp.length) s += ' Being compared: position ' + st.cmp.map(function (i) { return i + 1; }).join(' and ') + '.';
      if (st.low >= 0 && algo === 'binary') s += ' Low ' + (st.low + 1) + (st.mid >= 0 ? ', Mid ' + (st.mid + 1) : '') + ', High ' + (st.high + 1) + '.';
      return s;
    }

    function draw() {
      const st = steps[k];
      const n = st.arr.length;
      let max = 1;
      st.arr.forEach(function (v) { if (v != null && v > max) max = v; });
      chart.textContent = '';
      chart.setAttribute('aria-label', describe(st));
      for (let i = 0; i < n; i++) {
        const v = st.arr[i];
        const isCmp = st.cmp.indexOf(i) >= 0;
        const inRange = algo !== 'binary' || (st.low >= 0 && i >= st.low && i <= st.high);
        const isSorted = !!st.sorted[i];
        const isFound = st.found === i;
        let tag = '';
        if (isCmp) tag += 'C';
        if (isSorted && algo !== 'binary' && algo !== 'linear') tag += 'S';
        if (algo === 'binary') {
          if (st.low === i) tag += 'L';
          if (st.mid === i) tag += 'M';
          if (st.high === i) tag += 'H';
        }
        if (isFound) tag += 'F';
        if (i === st.gap) tag = '';
        const colour = isFound ? 'var(--ok)' : (isCmp ? 'var(--red)' : (isSorted ? 'var(--ok)' : (inRange ? 'var(--sc)' : 'var(--rule)')));
        const h = v == null ? 0 : Math.max(8, Math.round((v / max) * 100));
        const barBox = W.h('div', { style: { height: '112px', display: 'flex', alignItems: 'flex-end', justifyContent: 'center', width: '100%' } });
        if (v == null) {
          barBox.appendChild(W.h('div', { style: { width: '100%', height: '40px', boxSizing: 'border-box', border: '2px dashed var(--ink-2)' } }));
        } else {
          barBox.appendChild(W.h('div', { style: { width: '100%', height: h + '%', background: colour, boxSizing: 'border-box', border: isCmp ? '2px solid var(--ink)' : '2px solid transparent', borderRadius: '2px 2px 0 0' } }));
        }
        const col = W.h('div', { style: { flex: '1 1 0', minWidth: '0', display: 'flex', flexDirection: 'column', alignItems: 'center' } },
          W.h('div', { text: v == null ? '' : String(v), style: { fontWeight: '700', fontSize: '12px', color: 'var(--ink)', minHeight: '16px', lineHeight: '16px' } }),
          barBox,
          W.h('div', { text: String(i + 1), style: { fontSize: '11px', color: 'var(--ink-2)', lineHeight: '14px' } }),
          W.h('div', { text: tag, style: { fontSize: '11px', fontWeight: '700', color: 'var(--ink)', lineHeight: '14px', minHeight: '14px', whiteSpace: 'nowrap' } }));
        col.setAttribute('aria-hidden', 'true');
        chart.appendChild(col);
      }
      if (st.held != null) {
        chart.appendChild(W.h('div', { 'class': 'w-note', text: 'Holding ' + st.held, style: { flex: '0 0 auto', alignSelf: 'flex-start', marginLeft: '6px', whiteSpace: 'nowrap', fontWeight: '700' } }));
      }
      text.textContent = st.text;
      lab.textContent = k === 0 ? 'Start' : 'Step ' + k + ' of ' + (steps.length - 1);
      stComps.set(String(st.comps));
      stSwaps.set(String(st.moves));
      stShifts.set(String(st.moves));
      back.disabled = k === 0;
      next.disabled = k >= steps.length - 1;
      run.disabled = k >= steps.length - 1 && !timer;
      const a = document.activeElement;
      if (a && a.disabled && bar.contains(a)) reset.focus();
    }

    function go(i) {
      k = Math.max(0, Math.min(steps.length - 1, i));
      draw();
    }

    function rebuild() {
      stopTimer();
      const vals = valsOf();
      const model = S.run(algo, vals, targetOf());
      steps = model.steps;
      k = 0;
      stSwaps.el.style.display = algo === 'bubble' ? '' : 'none';
      stShifts.el.style.display = algo === 'insertion' ? '' : 'none';
      if (algo === 'bubble') note.textContent = 'Try: press "Already sorted" and Run: the flag stops the sort after one pass (n − 1 comparisons). Then "Reversed": every pair is out of order, so the comparisons and swaps both reach n(n − 1) ÷ 2.';
      else if (algo === 'insertion') note.textContent = 'Try: "Already sorted" needs only n − 1 comparisons and no shifts; "Reversed" shifts every value past all the others (n(n − 1) ÷ 2 comparisons and shifts). Compare the counters with Bubble on the same data.';
      else if (algo === 'binary') note.textContent = 'Binary search needs sorted data, so the values are shown in ascending order. Try a target that is not in the list, and add more values: doubling the number of values adds only one comparison.';
      else note.textContent = 'A linear search checks the values in the order given. Try a target at the front, at the end and not in the list, and compare with Binary search.';
      draw();
    }

    function syncInputs() {
      const vals = valsOf();
      valIn.value = (algo === 'binary' ? vals.slice().sort(function (x, y) { return x - y; }) : vals).join(', ');
      tgtIn.value = String(targetOf());
      err.style.display = 'none';
      err.textContent = '';
    }

    function setAlgo(name) {
      algo = name;
      S.ALGOS.forEach(function (n) { tabBtns[n].setAttribute('aria-pressed', n === algo ? 'true' : 'false'); });
      const search = !S.isSort(algo);
      tgtLab.style.display = search ? '' : 'none';
      dataBtns.style.display = search ? 'none' : '';
      syncInputs();
      rebuild();
    }

    function readInputs() {
      const pv = S.parseValues(valIn.value);
      if (pv.error) { err.textContent = pv.error; err.style.display = ''; return false; }
      if (!S.isSort(algo)) {
        const pt = S.parseTarget(tgtIn.value);
        if (pt.error) { err.textContent = pt.error; err.style.display = ''; return false; }
        if (algo === 'binary') binTarget = pt.target; else linTarget = pt.target;
      }
      err.style.display = 'none';
      err.textContent = '';
      setVals(pv.values);
      rebuild();
      return true;
    }
    valIn.addEventListener('input', readInputs);
    tgtIn.addEventListener('input', readInputs);

    back.addEventListener('click', function () { stopTimer(); go(k - 1); });
    next.addEventListener('click', function () { stopTimer(); go(k + 1); });
    reset.addEventListener('click', function () { stopTimer(); go(0); });
    run.addEventListener('click', function () {
      if (timer) { stopTimer(); draw(); return; }
      if (k >= steps.length - 1) return;
      if (W.reducedMotion && W.reducedMotion()) { go(steps.length - 1); return; }
      run.textContent = 'Pause';
      run.setAttribute('aria-label', 'Pause the automatic run');
      timer = setTimeout(tick, 400);
      draw();
    });
    bar.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); stopTimer(); go(k + 1); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); stopTimer(); go(k - 1); }
    });

    setAlgo(algo);
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-sort', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = S;
})();
