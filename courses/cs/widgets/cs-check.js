/* widgets/cs-check.js: block parity and check digits.
   <div class="widget" data-w="cs-check" data-mode="parity" data-parity="even" data-pos="left"
        data-data="1010011 1000101 1000011 1010101 1010010 1000101 1000100" data-seed="7"></div>
   <div class="widget" data-w="cs-check" data-mode="check" data-method="11" data-code="4829316" data-calc="calculate"></div>
   data-mode parity | check; data-parity even | odd; data-pos left | right (where each byte's parity bit sits);
   data-data seven 7-bit bytes; data-method 11 | 10; data-calc calculate | verify (verify: data-code includes the check digit).
   The logic (object L) is pure and is exported for a Node test (data/cs-check.test.js). */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure logic
  // ---------------------------------------------------------------------------------------------
  const L = {};
  const DEFAULT_BYTES = '1010011 1000101 1000011 1010101 1010010 1000101 1000100';   // SECURED in 7-bit ASCII
  L.DEFAULT_BYTES = DEFAULT_BYTES;

  L.ones = function (s) {
    let n = 0;
    for (let i = 0; i < s.length; i++) if (s.charAt(i) === '1') n++;
    return n;
  };
  L.parityFor = function (bits, type) {
    const odd = L.ones(bits) % 2 === 1;
    if (type === 'odd') return odd ? '0' : '1';
    return odd ? '1' : '0';
  };
  L.groupOk = function (bits, type) { return L.ones(bits) % 2 === (type === 'odd' ? 1 : 0); };

  L.parseBytes = function (text) {
    const parts = String(text == null ? '' : text).trim().split(/[\s,;]+/).filter(Boolean);
    if (parts.length !== 7) return { error: 'Type exactly seven bytes of 7 bits, separated by spaces (you typed ' + parts.length + ').' };
    for (let i = 0; i < 7; i++) {
      if (!/^[01]{7}$/.test(parts[i])) return { error: 'Byte ' + (i + 1) + ' must be exactly 7 bits, each 0 or 1.' };
    }
    return { bytes: parts };
  };

  // The block that is sent: seven bytes with a parity bit each, then the parity byte (a parity bit for every column).
  L.buildBlock = function (bytes, type, pos) {
    const rows = [];
    for (let i = 0; i < 7; i++) {
      const p = L.parityFor(bytes[i], type);
      rows.push(pos === 'right' ? bytes[i] + p : p + bytes[i]);
    }
    let last = '';
    for (let c = 0; c < 8; c++) {
      let col = '';
      for (let r = 0; r < 7; r++) col += rows[r].charAt(c);
      last += L.parityFor(col, type);
    }
    rows.push(last);
    return rows;
  };

  L.column = function (block, c) {
    let s = '';
    for (let r = 0; r < block.length; r++) s += block[r].charAt(c);
    return s;
  };

  // Which rows and columns fail, and where a single error is.
  L.analyse = function (block, type) {
    const badRows = [];
    const badCols = [];
    for (let r = 0; r < 8; r++) if (!L.groupOk(block[r], type)) badRows.push(r);
    for (let c = 0; c < 8; c++) if (!L.groupOk(L.column(block, c), type)) badCols.push(c);
    const located = badRows.length === 1 && badCols.length === 1 ? { row: badRows[0], col: badCols[0] } : null;
    return { badRows: badRows, badCols: badCols, located: located };
  };

  L.parityCol = function (pos) { return pos === 'right' ? 7 : 0; };
  L.dataBit = function (col, pos) { return pos === 'right' ? col + 1 : col; };
  L.rowName = function (row) { return row === 7 ? 'the parity byte' : 'byte ' + (row + 1); };
  L.colName = function (col, pos) {
    return col === L.parityCol(pos) ? 'the parity bit' : 'data bit ' + L.dataBit(col, pos);
  };
  L.where = function (row, col, pos) { return L.rowName(row) + ', ' + L.colName(col, pos); };

  L.flip = function (block, row, col) {
    const out = block.slice();
    const s = out[row];
    out[row] = s.substr(0, col) + (s.charAt(col) === '1' ? '0' : '1') + s.substr(col + 1);
    return out;
  };

  // Cells where two blocks differ, as [row, col] pairs.
  L.diff = function (a, b) {
    const out = [];
    for (let r = 0; r < 8; r++) for (let c = 0; c < 8; c++) if (a[r].charAt(c) !== b[r].charAt(c)) out.push([r, c]);
    return out;
  };

  // Choose k cells that are not already changed. rand() gives numbers in [0, 1).
  L.pickCells = function (rand, k, avoid) {
    const taken = {};
    avoid.forEach(function (p) { taken[p[0] + ',' + p[1]] = true; });
    const chosen = [];
    let guard = 0;
    while (chosen.length < k && guard < 1000) {
      guard++;
      const idx = Math.min(63, Math.floor(rand() * 64));
      const r = Math.floor(idx / 8);
      const c = idx % 8;
      const key = r + ',' + c;
      if (!taken[key]) { taken[key] = true; chosen.push([r, c]); }
    }
    return chosen;
  };

  L.listRows = function (rows) { return rows.map(function (r) { return L.rowName(r).replace('the ', ''); }).join(', '); };
  L.listCols = function (cols, pos) { return cols.map(function (c) { return L.colName(c, pos).replace('the ', ''); }).join(', '); };

  // The sentence the widget shows. changed = how many bits differ from what was sent.
  L.verdict = function (an, pos, changed) {
    if (!an.badRows.length && !an.badCols.length) {
      return changed === 0
        ? 'Every row and every column has the right parity: no error detected.'
        : 'Every row and every column has the right parity, yet ' + changed + ' bits were changed. These errors escape detection.';
    }
    if (an.located) {
      const w = L.where(an.located.row, an.located.col, pos);
      let s = 'One row and one column fail. Error at ' + w + '. Flip that bit to correct it.';
      if (changed > 1) s += ' (But ' + changed + ' bits were changed, so this position is wrong: with more than one error the crossing misleads.)';
      return s;
    }
    return an.badRows.length + (an.badRows.length === 1 ? ' row' : ' rows') + ' and ' + an.badCols.length +
      (an.badCols.length === 1 ? ' column' : ' columns') + ' fail. An error is detected, but it cannot be located, so the block must be sent again.';
  };

  // ---- check digits ----
  L.cdParse = function (text, method, calc) {
    const t = String(text == null ? '' : text).replace(/[\s-]/g, '').toUpperCase();
    if (t === '') return { error: 'Type a code first.' };
    if (calc === 'verify') {
      const okChars = method === '11' ? /^[0-9]+[0-9X]$/ : /^[0-9]+$/;
      if (!okChars.test(t)) return { error: method === '11' ? 'Use digits only, and X only as the last character.' : 'Use digits only for a modulo-10 code.' };
      if (t.length < 3 || t.length > 17) return { error: 'A code to verify needs 3 to 17 characters, including the check digit.' };
      return { code: t };
    }
    if (!/^[0-9]+$/.test(t)) return { error: 'Use digits only: the widget works out the check digit for you.' };
    if (t.length < 2 || t.length > 16) return { error: 'Use 2 to 16 digits (without the check digit).' };
    return { code: t };
  };

  L.weight = function (i, n, method) {                 // i is 0-based, n is the number of digits before the check digit
    return method === '10' ? ((n - 1 - i) % 2 === 0 ? 3 : 1) : n + 1 - i;
  };
  L.modulus = function (method) { return method === '10' ? 10 : 11; };

  L.cdCompute = function (digits, method) {
    const n = digits.length;
    const mod = L.modulus(method);
    const rows = [];
    let sum = 0;
    for (let i = 0; i < n; i++) {
      const d = parseInt(digits.charAt(i), 10);
      const w = L.weight(i, n, method);
      rows.push({ d: String(d), w: w, p: d * w });
      sum += d * w;
    }
    const rem = sum % mod;
    const raw = (mod - rem) % mod;
    return { rows: rows, sum: sum, rem: rem, mod: mod, raw: raw, check: raw === 10 ? 'X' : String(raw), n: n };
  };

  L.cdVerify = function (full, method) {
    const body = full.slice(0, -1);
    const last = full.slice(-1);
    const n = body.length;
    const mod = L.modulus(method);
    const calc = L.cdCompute(body, method);
    const lastValue = last === 'X' ? 10 : parseInt(last, 10);
    const lastWeight = 1;
    const rows = calc.rows.slice();
    rows.push({ d: last === 'X' ? 'X (10)' : last, w: lastWeight, p: lastValue * lastWeight, isCheck: true });
    const sum = calc.sum + lastValue * lastWeight;
    return { rows: rows, sum: sum, rem: sum % mod, mod: mod, valid: sum % mod === 0, expected: calc.check, last: last };
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  function attrs(node, obj) {
    Object.keys(obj).forEach(function (k) { node.setAttribute(k, obj[k]); });
    return node;
  }
  function pick(value, allowed, dflt) {
    const v = String(value == null ? '' : value).toLowerCase();
    return allowed.indexOf(v) >= 0 ? v : dflt;
  }
  function select(label, options, value, onchange) {
    const s = W.h('select', {});
    options.forEach(function (o) { s.appendChild(W.h('option', { value: o[0], text: o[1] })); });
    s.value = value;
    s.addEventListener('change', function () { onchange(s.value); });
    return { el: W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: label }), s), sel: s };
  }
  function textBox(label, initial, onchange, size) {
    const input = attrs(W.h('input', { type: 'text', style: { maxWidth: '100%', boxSizing: 'border-box' } }), { autocomplete: 'off', spellcheck: 'false', size: String(size || 14) });
    input.value = initial;
    input.addEventListener('input', function () { onchange(input.value); });
    return { el: W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: label }), input), input: input };
  }

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'Block parity and check digits', 'Flip bits and see which checks fail, or work out a check digit');
    const body = frame.body;
    let mode = pick(opts.mode, ['parity', 'check'], 'parity');
    let type = pick(opts.parity, ['even', 'odd'], 'even');
    let pos = pick(opts.pos, ['left', 'right'], 'left');
    let method = pick(opts.method, ['11', '10'], '11');
    let calc = pick(opts.calc, ['calculate', 'verify'], 'calculate');
    const seedNum = parseInt(opts.seed, 10);
    const rand = W.rng(isNaN(seedNum) ? 7 : seedNum);

    // tabs
    const tabs = attrs(W.h('div', { 'class': 'w-tabs' }), { role: 'group', 'aria-label': 'Which tool' });
    const tabParity = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Parity block' });
    const tabCheck = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Check digit' });
    tabs.appendChild(tabParity);
    tabs.appendChild(tabCheck);
    body.appendChild(tabs);

    // ======== Parity panel ========
    let dataText = opts.data && L.parseBytes(opts.data).bytes ? String(opts.data).trim().split(/[\s,;]+/).join(' ') : DEFAULT_BYTES;
    let sent = null;
    let received = null;
    const typeCtl = select('Parity', [['even', 'Even parity'], ['odd', 'Odd parity']], type, function (v) { type = v; rebuild(); });
    const posCtl = select('Parity bit position', [['left', 'Left (MSB)'], ['right', 'Right (LSB)']], pos, function (v) { pos = v; rebuild(); });
    const dataBox = textBox('Seven data bytes (7 bits each)', dataText, function (v) { dataText = v; rebuild(); }, 30);
    const perr = attrs(W.h('div', { 'class': 'w-err' }), { 'aria-live': 'polite' });
    const btnOne = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Corrupt 1 random bit' });
    const btnTwo = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Corrupt 2 random bits' });
    const btnReset = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Reset the block' });
    let reveal = false;
    const revealBox = attrs(W.h('input', { type: 'checkbox' }), {});
    const revealCtl = W.h('label', { 'class': 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } }, revealBox,
      W.h('span', { 'class': 'w-lab', text: 'Mark the bits I changed' }));
    revealBox.addEventListener('change', function () { reveal = revealBox.checked; paint(); });

    const table = attrs(W.h('table', { style: { borderCollapse: 'collapse', margin: '8px 0', width: 'auto' } }), { 'aria-label': 'The received block of bits. Each bit is a button that flips it.' });
    const headRow = W.h('tr', {});
    const headCells = [];
    headRow.appendChild(W.h('th', { text: '', style: { padding: '2px 4px' } }));
    for (let c = 0; c < 8; c++) {
      const th = attrs(W.h('th', { style: { padding: '2px 0', fontSize: '12px', textAlign: 'center' } }), { scope: 'col' });
      headCells.push(th);
      headRow.appendChild(th);
    }
    headRow.appendChild(attrs(W.h('th', { text: 'Row', style: { padding: '2px 4px', fontSize: '12px' } }), { scope: 'col' }));
    const thead = W.h('thead', {}, headRow);
    const tbody = W.h('tbody', {});
    const cellBtns = [];
    const rowMarks = [];
    for (let r = 0; r < 8; r++) {
      const tr = W.h('tr', {});
      tr.appendChild(attrs(W.h('th', { text: r === 7 ? 'Parity byte' : 'Byte ' + (r + 1), style: { padding: '2px 4px 2px 0', fontSize: '12px', textAlign: 'left', lineHeight: '1.15' } }), { scope: 'row' }));
      cellBtns.push([]);
      for (let c = 0; c < 8; c++) {
        const b = W.h('button', { type: 'button', text: '0', style: { width: '25px', height: '28px', margin: '1px 0', padding: '0', fontFamily: 'ui-monospace, Menlo, Consolas, monospace', fontSize: '14px', lineHeight: '1', minWidth: '0', cursor: 'pointer' } });
        b.addEventListener('click', function () { flipCell(r, c); });
        cellBtns[r].push(b);
        tr.appendChild(W.h('td', { style: { padding: '0', textAlign: 'center' } }, b));
      }
      const mark = W.h('td', { style: { padding: '0 2px', textAlign: 'center', fontSize: '15px', fontWeight: '700' } });
      rowMarks.push(mark);
      tr.appendChild(mark);
      tbody.appendChild(tr);
    }
    const colRow = W.h('tr', {});
    colRow.appendChild(attrs(W.h('th', { text: 'Column', style: { padding: '2px 6px 2px 0', fontSize: '12px', textAlign: 'left' } }), { scope: 'row' }));
    const colMarks = [];
    for (let c = 0; c < 8; c++) {
      const td = W.h('td', { style: { padding: '2px 0', textAlign: 'center', fontSize: '15px', fontWeight: '700' } });
      colMarks.push(td);
      colRow.appendChild(td);
    }
    colRow.appendChild(W.h('td', {}));
    tbody.appendChild(colRow);
    table.appendChild(thead);
    table.appendChild(tbody);
    const tableWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%' } }, table);

    const ro = W.readout([['rows', 'Rows that fail'], ['cols', 'Columns that fail'], ['res', 'Result']]);
    const pnote = W.h('div', { 'class': 'w-note', text: 'Each byte has seven data bits and a parity bit; the last byte holds a parity bit for every column. Press any bit to flip it, or corrupt bits at random. Try two bits in one row, then four bits at the corners of a rectangle.' });
    const parityPanel = W.h('div', {},
      W.h('div', { 'class': 'w-row' }, typeCtl.el, posCtl.el),
      W.h('div', { 'class': 'w-row' }, dataBox.el),
      perr,
      W.h('div', { 'class': 'w-row' }, btnOne, btnTwo, btnReset, revealCtl),
      tableWrap, ro.el, pnote);
    body.appendChild(parityPanel);

    function rebuild() {
      const parsed = L.parseBytes(dataText);
      if (parsed.error) {
        perr.textContent = parsed.error;
        perr.style.display = '';
        return;
      }
      perr.textContent = '';
      perr.style.display = 'none';
      sent = L.buildBlock(parsed.bytes, type, pos);
      received = sent.slice();
      paint();
    }

    function flipCell(r, c) {
      if (!received) return;
      received = L.flip(received, r, c);
      paint();
      W.say(el, 'Flipped ' + L.where(r, c, pos) + '. ' + lastVerdict);
    }

    let lastVerdict = '';
    function paint() {
      if (!received) return;
      const an = L.analyse(received, type);
      const changes = L.diff(sent, received);
      const changedKey = {};
      changes.forEach(function (p) { changedKey[p[0] + ',' + p[1]] = true; });
      for (let c = 0; c < 8; c++) {
        headCells[c].textContent = c === L.parityCol(pos) ? 'P' : String(L.dataBit(c, pos));
        headCells[c].setAttribute('aria-label', c === L.parityCol(pos) ? 'Parity bit column' : 'Data bit ' + L.dataBit(c, pos) + ' column');
      }
      for (let r = 0; r < 8; r++) {
        const rowBad = an.badRows.indexOf(r) >= 0;
        rowMarks[r].textContent = rowBad ? '✗' : '✓';
        rowMarks[r].style.color = rowBad ? 'var(--red)' : 'var(--ok)';
        rowMarks[r].setAttribute('aria-label', 'Row check for ' + L.rowName(r) + ': ' + (rowBad ? 'fails' : 'passes'));
        for (let c = 0; c < 8; c++) {
          const b = cellBtns[r][c];
          const v = received[r].charAt(c);
          const was = !!changedKey[r + ',' + c];
          b.textContent = v;
          b.style.fontWeight = v === '1' ? '800' : '400';
          const shown = reveal && was;
          b.style.borderWidth = shown ? '3px' : '';
          b.style.borderColor = shown ? 'var(--sc)' : '';
          b.setAttribute('aria-label', L.where(r, c, pos) + ': ' + v + (shown ? ', changed' : '') + '. Press to flip.');
        }
      }
      for (let c = 0; c < 8; c++) {
        const bad = an.badCols.indexOf(c) >= 0;
        colMarks[c].textContent = bad ? '✗' : '✓';
        colMarks[c].style.color = bad ? 'var(--red)' : 'var(--ok)';
        colMarks[c].setAttribute('aria-label', 'Column check for ' + L.colName(c, pos) + ': ' + (bad ? 'fails' : 'passes'));
      }
      lastVerdict = L.verdict(an, pos, changes.length);
      ro.set('rows', an.badRows.length ? L.listRows(an.badRows) : 'none');
      ro.set('cols', an.badCols.length ? L.listCols(an.badCols, pos) : 'none');
      ro.set('res', lastVerdict);
    }

    function corrupt(k) {
      if (!received) return;
      const cells = L.pickCells(rand, k, L.diff(sent, received));
      cells.forEach(function (p) { received = L.flip(received, p[0], p[1]); });
      paint();
      W.say(el, cells.length + (cells.length === 1 ? ' bit' : ' bits') + ' changed. ' + lastVerdict);
    }
    btnOne.addEventListener('click', function () { corrupt(1); });
    btnTwo.addEventListener('click', function () { corrupt(2); });
    btnReset.addEventListener('click', function () { if (sent) { received = sent.slice(); paint(); W.say(el, 'The block is back as it was sent.'); } });

    // ======== Check digit panel ========
    let code = String(opts.code == null || opts.code === '' ? (calc === 'verify' ? '48293164' : '4829316') : opts.code);
    const methodCtl = select('Method', [['11', 'Modulo 11'], ['10', 'Modulo 10']], method, function (v) { method = v; showCheck(); });
    const calcCtl = select('Task', [['calculate', 'Calculate'], ['verify', 'Verify a full code']], calc, function (v) {
      calc = v;
      if (v === 'verify' && /^[0-9]+$/.test(codeBox.input.value.replace(/[\s-]/g, ''))) {
        const c = L.cdParse(codeBox.input.value, method, 'calculate');
        if (c.code) { codeBox.input.value = c.code + L.cdCompute(c.code, method).check; code = codeBox.input.value; }
      } else if (v === 'calculate') {
        const t = codeBox.input.value.replace(/[\s-]/g, '').toUpperCase();
        if (t.length > 2 && /^[0-9X]+$/.test(t)) { codeBox.input.value = t.slice(0, -1); code = codeBox.input.value; }
      }
      showCheck();
    });
    const codeBox = textBox('Code', code, function (v) { code = v; showCheck(); }, 20);
    const cerr = attrs(W.h('div', { 'class': 'w-err' }), { 'aria-live': 'polite' });
    const ctable = attrs(W.h('table', { style: { width: 'auto', margin: '6px 0' } }), { 'aria-label': 'Each digit, its weight and their product' });
    const cro = W.readout([['sum', 'Total'], ['rem', 'Remainder'], ['res', 'Result']]);
    const cnote = W.h('div', { 'class': 'w-note' });
    const checkPanel = W.h('div', {}, W.h('div', { 'class': 'w-row' }, methodCtl.el, calcCtl.el, codeBox.el), cerr, ctable, cro.el, cnote);
    body.appendChild(checkPanel);

    function showCheck() {
      const parsed = L.cdParse(code, method, calc);
      ctable.textContent = '';
      if (parsed.error) {
        cerr.textContent = parsed.error;
        cerr.style.display = '';
        ['sum', 'rem', 'res'].forEach(function (k) { cro.set(k, '–'); });
        cnote.textContent = 'Fix the code to see the working.';
        return;
      }
      cerr.textContent = '';
      cerr.style.display = 'none';
      const hdr = W.h('tr', {});
      ['Digit', 'Weight', 'Product'].forEach(function (t) { hdr.appendChild(attrs(W.h('th', { text: t, style: { textAlign: 'right', padding: '2px 8px' } }), { scope: 'col' })); });
      ctable.appendChild(W.h('thead', {}, hdr));
      const tb = W.h('tbody', {});
      let res;
      if (calc === 'verify') res = L.cdVerify(parsed.code, method); else res = L.cdCompute(parsed.code, method);
      res.rows.forEach(function (row) {
        const tr = W.h('tr', {});
        [row.d + (row.isCheck ? ' (check digit)' : ''), '× ' + row.w, '= ' + row.p].forEach(function (t) { tr.appendChild(W.h('td', { text: t, style: { textAlign: 'right', padding: '2px 8px', fontFamily: 'ui-monospace, Menlo, Consolas, monospace' } })); });
        tb.appendChild(tr);
      });
      ctable.appendChild(tb);
      const m = res.mod;
      if (calc === 'verify') {
        cro.set('sum', 'sum of the products = ' + res.sum);
        cro.set('rem', res.sum + ' ÷ ' + m + ' leaves remainder ' + res.rem);
        cro.set('res', res.valid ? '✓ Valid: the total is a multiple of ' + m + '.' : '✗ Not valid: the total is not a multiple of ' + m + '. The check digit for this code should be ' + res.expected + '.');
        cnote.textContent = 'Try swapping two neighbouring digits of a valid code. Modulo 11 always notices; modulo 10 misses digits that differ by 5.';
      } else {
        cro.set('sum', 'sum of the products = ' + res.sum);
        cro.set('rem', res.sum + ' ÷ ' + m + ' leaves remainder ' + res.rem);
        const how = res.rem === 0 ? 'remainder 0, so the check digit is 0' : m + ' − ' + res.rem + ' = ' + res.raw;
        cro.set('res', 'Check digit: ' + how + (res.check === 'X' ? ', written X' : '') + '. Full code: ' + parsed.code + res.check);
        cnote.textContent = 'Modulo 11: weights count down from n + 1 to 2 and the check digit is 11 − remainder (10 is written X). Modulo 10: weights alternate 3, 1, 3, 1 working back from the check digit, and the check digit is 10 − remainder.';
      }
    }

    function setMode(m) {
      mode = m;
      tabParity.setAttribute('aria-pressed', m === 'parity' ? 'true' : 'false');
      tabCheck.setAttribute('aria-pressed', m === 'check' ? 'true' : 'false');
      parityPanel.style.display = m === 'parity' ? '' : 'none';
      checkPanel.style.display = m === 'check' ? '' : 'none';
    }
    tabParity.addEventListener('click', function () { setMode('parity'); });
    tabCheck.addEventListener('click', function () { setMode('check'); });

    rebuild();
    showCheck();
    setMode(mode);
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-check', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = L;
})();
