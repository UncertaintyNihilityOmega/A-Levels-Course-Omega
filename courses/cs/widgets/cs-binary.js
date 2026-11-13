/* widgets/cs-binary.js: Binary, hexadecimal, BCD, one's and two's complement, and binary addition with overflow.
   <div class="widget" data-w="cs-binary" data-bits="8" data-value="-37" data-base="10" data-mode="convert"></div>
   data-bits 4 to 16; data-base 10, 2 or 16 (how data-value is read); data-mode convert or add (add: data-value2).
   The logic (object L) is pure, and is exported for a Node test (data/cs-binary.test.js). */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure logic
  // ---------------------------------------------------------------------------------------------
  const L = {};
  const MINUS = '−';
  L.num = function (v) { return v < 0 ? MINUS + (-v) : String(v); };
  L.pad = function (s, n) { return s.length >= n ? s : new Array(n - s.length + 1).join('0') + s; };
  L.pow2 = function (n) { return Math.pow(2, n); };
  L.range = function (n) {
    return { umax: L.pow2(n) - 1, tmin: -L.pow2(n - 1), tmax: L.pow2(n - 1) - 1 };
  };
  L.toPattern = function (v, n) {
    const m = L.pow2(n);
    return L.pad((((v % m) + m) % m).toString(2), n);
  };
  L.unsignedOf = function (p) { return parseInt(p, 2); };
  L.twosOf = function (p) {
    const u = parseInt(p, 2);
    return p.charAt(0) === '1' ? u - L.pow2(p.length) : u;
  };
  L.invert = function (p) { return p.replace(/[01]/g, function (c) { return c === '0' ? '1' : '0'; }); };
  L.onesOf = function (p) {
    return p.charAt(0) === '1' ? -parseInt(L.invert(p), 2) : parseInt(p, 2);
  };
  L.hexOf = function (p) {
    const q = L.pad(p, Math.ceil(p.length / 4) * 4);
    let out = '';
    for (let i = 0; i < q.length; i += 4) out += parseInt(q.substr(i, 4), 2).toString(16).toUpperCase();
    return out;
  };
  L.bcdOf = function (v) {
    return String(v).split('').map(function (d) { return L.pad(parseInt(d, 10).toString(2), 4); }).join(' ');
  };

  // Turn what the reader typed into {kind:'value', v} or {kind:'pattern', p}, or {error}.
  L.parse = function (text, base, n) {
    let t = String(text == null ? '' : text).replace(/[\s_]/g, '');
    if (t === '') return { error: 'Type a number first.' };
    const r = L.range(n);
    if (base === '10') {
      if (!/^[+-]?\d+$/.test(t)) return { error: 'Denary input must be a whole number such as 37 or -37.' };
      if (t.replace(/^[+-]/, '').length > 9) return { error: 'That number is far too large for ' + n + ' bits.' };
      return { kind: 'value', v: parseInt(t, 10) };
    }
    if (base === '2') {
      t = t.replace(/^0b/i, '');
      if (!/^[01]+$/.test(t)) return { error: 'Binary input may use only the digits 0 and 1.' };
      const trimmed = t.replace(/^0+/, '');
      if (trimmed.length > n) return { error: 'That pattern needs ' + trimmed.length + ' bits, but you chose ' + n + ' bits.' };
      return { kind: 'pattern', p: L.pad(trimmed, n) };
    }
    t = t.replace(/^0x/i, '');
    if (!/^[0-9a-fA-F]+$/.test(t)) return { error: 'Hexadecimal input may use only 0 to 9 and A to F.' };
    if (t.length > 8) return { error: 'That hex number is far too large for ' + n + ' bits.' };
    const v = parseInt(t, 16);
    if (v > r.umax) return { error: 'That hex number needs more than ' + n + ' bits (the largest is ' + L.hexOf(L.toPattern(r.umax, n)) + ').' };
    return { kind: 'pattern', p: L.toPattern(v, n) };
  };

  // Everything the Convert tab shows. Returns {error} or {pattern, rows}; pattern is the bit row (or null).
  L.analyse = function (parsed, n) {
    if (parsed.error) return { error: parsed.error, pattern: null, rows: null };
    const r = L.range(n);
    const rows = {};
    if (parsed.kind === 'pattern') {
      const p = parsed.p;
      const u = L.unsignedOf(p);
      const s = L.twosOf(p);
      const o = L.onesOf(p);
      rows.den = L.num(u) + ' as unsigned; ' + L.num(s) + " as two's complement";
      rows.uns = p + ' (= ' + u + ')';
      rows.hex = L.hexOf(p);
      rows.bcd = L.bcdOf(u) + ' (the unsigned value ' + u + ', one nibble per digit)';
      rows.ones = p + ' (= ' + (p.indexOf('0') < 0 ? MINUS + '0, the second zero' : L.num(o)) + ')';
      rows.twos = p + ' (= ' + L.num(s) + ')';
      return { error: null, pattern: p, rows: rows };
    }
    const v = parsed.v;
    const inU = v >= 0 && v <= r.umax;
    const inT = v >= r.tmin && v <= r.tmax;
    const inO = v >= -r.tmax && v <= r.tmax;
    if (!inU && !inT) {
      return {
        error: L.num(v) + ' is out of range for ' + n + ' bits: unsigned values run 0 to ' + r.umax + " and two's complement values run " +
          L.num(r.tmin) + ' to ' + r.tmax + '. Choose more bits.',
        pattern: null,
        rows: null
      };
    }
    const p = L.toPattern(v, n);
    rows.den = L.num(v);
    rows.uns = inU ? p : (v < 0 ? 'none: a negative number is not unsigned' : 'out of range: unsigned values run 0 to ' + r.umax);
    rows.hex = L.hexOf(p) + ' (of the pattern in the bit row)';
    rows.bcd = v >= 0 ? L.bcdOf(v) + ' (' + 4 * String(v).length + ' bits)' : 'none: BCD holds digits 0 to 9 and this tool stores no sign';
    rows.ones = inO ? (v >= 0 ? p : L.invert(L.toPattern(-v, n))) : 'out of range: one’s complement runs ' + L.num(-r.tmax) + ' to ' + r.tmax;
    rows.twos = inT ? p : 'out of range: two’s complement runs ' + L.num(r.tmin) + ' to ' + r.tmax;
    if (!inT) rows.den = L.num(v) + " (the pattern shown is unsigned; as two's complement it would mean " + L.num(L.twosOf(p)) + ')';
    return { error: null, pattern: p, rows: rows };
  };

  // Column addition of two equal-length patterns: carries into each column (left to right), carry out, result.
  L.addCols = function (a, b) {
    const n = a.length;
    let carry = 0;
    const into = new Array(n);
    let res = '';
    for (let i = n - 1; i >= 0; i--) {
      const s = parseInt(a.charAt(i), 10) + parseInt(b.charAt(i), 10) + carry;
      into[i] = String(carry);
      res = String(s % 2) + res;
      carry = Math.floor(s / 2);
    }
    return { carries: into.join(''), carryOut: carry, result: res };
  };

  // Turn one typed value into an n-bit pattern for the Add tab, or an error message.
  L.toAddPattern = function (parsed, n, name) {
    if (parsed.error) return { error: name + ': ' + parsed.error };
    if (parsed.kind === 'pattern') return { p: parsed.p };
    const r = L.range(n);
    if (parsed.v < r.tmin || parsed.v > r.umax) {
      return { error: name + ': ' + L.num(parsed.v) + ' is out of range for ' + n + ' bits (' + L.num(r.tmin) + ' to ' + r.umax + ').' };
    }
    return { p: L.toPattern(parsed.v, n) };
  };

  L.addAnalyse = function (pa, pb) {
    const n = pa.length;
    const r = L.range(n);
    const add = L.addCols(pa, pb);
    const ua = L.unsignedOf(pa), ub = L.unsignedOf(pb), ur = L.unsignedOf(add.result);
    const sa = L.twosOf(pa), sb = L.twosOf(pb), sr = L.twosOf(add.result);
    const trueSigned = sa + sb;
    const signedOverflow = trueSigned < r.tmin || trueSigned > r.tmax;
    let why = '';
    if (signedOverflow) {
      why = sa >= 0 && sb >= 0 ? ' (two positive numbers gave a negative result)' : ' (two negative numbers gave a positive result)';
    }
    return {
      carries: add.carries,
      carryOut: add.carryOut,
      result: add.result,
      carry: add.carryOut === 1 ? 'Yes: a 1 carries out of the leftmost column' : 'No',
      uns: ua + ' + ' + ub + ' = ' + (ua + ub) + '; the ' + n + ' bits hold ' + ur,
      unsOverflow: add.carryOut === 1,
      sig: L.num(sa) + ' + ' + L.num(sb) + ' = ' + L.num(trueSigned) + '; the ' + n + ' bits hold ' + L.num(sr),
      sigOverflow: signedOverflow,
      sigWhy: why
    };
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  function clampInt(text, lo, hi, dflt) {
    const k = parseInt(text, 10);
    return isNaN(k) ? dflt : Math.max(lo, Math.min(hi, k));
  }
  function attrs(node, obj) {
    Object.keys(obj).forEach(function (k) { node.setAttribute(k, obj[k]); });
    return node;
  }

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'Binary, hex and two’s complement', 'Type a number, toggle the bits, or add two patterns');
    const body = frame.body;
    let bits = clampInt(opts.bits, 4, 16, 8);
    let mode = opts.mode === 'add' ? 'add' : 'convert';
    let base = (opts.base === '2' || opts.base === '16') ? opts.base : '10';
    let pattern = null;
    let bitButtons = [];

    // mode tabs
    const tabs = attrs(W.h('div', { 'class': 'w-tabs' }), { role: 'group', 'aria-label': 'What to do' });
    const tabConvert = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Convert' });
    const tabAdd = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Add' });
    tabs.appendChild(tabConvert);
    tabs.appendChild(tabAdd);

    // controls
    function select(label, options, value, onchange) {
      const s = W.h('select', {});
      options.forEach(function (o) { s.appendChild(W.h('option', { value: o[0], text: o[1] })); });
      s.value = value;
      s.addEventListener('change', function () { onchange(s.value); });
      return { el: W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: label }), s), sel: s };
    }
    const bitsOptions = [];
    for (let k = 4; k <= 16; k++) bitsOptions.push([String(k), k + ' bits']);
    const bitsCtl = select('Number of bits', bitsOptions, String(bits), function (v) { bits = clampInt(v, 4, 16, 8); buildBits(); refresh(); });
    const baseCtl = select('Type the number as', [['10', 'Denary'], ['2', 'Binary'], ['16', 'Hexadecimal']], base, function (v) { rebase(v); refresh(); });

    // Rewrite both boxes in the new base so a change of base never turns a good input into an error.
    function rebase(nb) {
      if (nb === base) return;
      [boxA, boxB].forEach(function (box) {
        const parsed = L.parse(box.input.value, base, bits);
        const ap = L.toAddPattern(parsed, bits, '');
        if (ap.error) return;
        if (nb === '2') box.input.value = ap.p;
        else if (nb === '16') box.input.value = L.hexOf(ap.p);
        else box.input.value = parsed.kind === 'value' ? String(parsed.v) : String(L.unsignedOf(ap.p));
      });
      base = nb;
      baseCtl.sel.value = nb;
    }

    function textBox(labelText, initial) {
      const input = attrs(W.h('input', { type: 'text' }), { inputmode: 'text', autocomplete: 'off', spellcheck: 'false', size: '14' });
      input.value = initial;
      input.addEventListener('input', function () { refresh(); });
      const lab = W.h('span', { 'class': 'w-lab', text: labelText });
      return { el: W.h('label', { 'class': 'w-ctl' }, lab, input), input: input, lab: lab };
    }
    const boxA = textBox('Number', opts.value == null || opts.value === '' ? '-37' : String(opts.value));
    const boxB = textBox('Second number (B)', opts.value2 == null || opts.value2 === '' ? '45' : String(opts.value2));

    const controls = W.h('div', { 'class': 'w-row' }, bitsCtl.el, baseCtl.el, boxA.el, boxB.el);
    const err = attrs(W.h('div', { 'class': 'w-err' }), { 'aria-live': 'polite' });

    // Convert view: bit row + readout
    const bitWrap = W.h('div', {});
    const bitNote = W.h('div', { 'class': 'w-note' });
    const ro = W.readout([
      ['den', 'Denary value'], ['uns', 'Unsigned binary'], ['hex', 'Hexadecimal'], ['bcd', 'BCD'],
      ['ones', 'One’s complement'], ['twos', 'Two’s complement']
    ]);
    const convertBox = W.h('div', {}, bitWrap, bitNote, ro.el);

    // Add view: column addition + readout
    const sum = attrs(W.h('pre', { 'class': 'w-note', style: { fontFamily: 'ui-monospace, Menlo, Consolas, monospace', overflowX: 'auto', margin: '6px 0' } }), { 'aria-label': 'Column addition' });
    const ra = W.readout([
      ['carry', 'Carry out of the leftmost column'], ['uns', 'As unsigned numbers'], ['unsov', 'Unsigned overflow'],
      ['sig', 'As two’s complement numbers'], ['sigov', 'Signed overflow']
    ]);
    const addBox = W.h('div', {}, sum, ra.el);

    const note = W.h('div', { 'class': 'w-note' });
    body.appendChild(tabs);
    body.appendChild(controls);
    body.appendChild(err);
    body.appendChild(convertBox);
    body.appendChild(addBox);
    body.appendChild(note);

    function buildBits() {
      bitWrap.textContent = '';
      bitButtons = [];
      const perRow = Math.min(8, bits);
      for (let start = 0; start < bits; start += perRow) {
        const row = W.h('div', { style: { display: 'grid', gridTemplateColumns: 'repeat(' + perRow + ', minmax(0, 1fr))', gap: '3px', margin: '4px 0' } });
        for (let k = start; k < Math.min(bits, start + perRow); k++) {
          const pos = bits - 1 - k;
          const pv = pos === bits - 1 ? MINUS + L.pow2(pos) : String(L.pow2(pos));
          const btn = W.h('button', { 'class': 'w-tab', type: 'button', text: '0', style: { width: '100%', minWidth: '0', padding: '6px 0', border: '1px solid var(--rule)', fontFamily: 'ui-monospace, Menlo, Consolas, monospace', fontSize: '16px' } });
          btn.setAttribute('aria-pressed', 'false');
          btn.setAttribute('aria-label', 'Bit ' + pos + ', place value ' + pv);
          btn.addEventListener('click', function () { toggle(k, pos); });
          bitButtons.push({ btn: btn, pos: pos, pv: pv });
          const cell = W.h('div', { style: { textAlign: 'center', minWidth: '0' } },
            W.h('div', { text: pv, style: { fontSize: '11px', color: 'var(--ink-2)', lineHeight: '1.2', whiteSpace: 'nowrap' } }), btn);
          row.appendChild(cell);
        }
        bitWrap.appendChild(row);
      }
    }

    function paintBits() {
      bitButtons.forEach(function (b, k) {
        if (pattern) {
          const one = pattern.charAt(k) === '1';
          b.btn.textContent = one ? '1' : '0';
          b.btn.setAttribute('aria-pressed', one ? 'true' : 'false');
          b.btn.style.fontWeight = one ? '800' : '400';
          b.btn.style.borderColor = one ? 'var(--sc)' : 'var(--rule)';
          b.btn.style.borderWidth = one ? '2px' : '1px';
          b.btn.disabled = false;
        } else {
          b.btn.textContent = '–';
          b.btn.setAttribute('aria-pressed', 'false');
          b.btn.disabled = true;
        }
      });
    }

    function toggle(k, pos) {
      if (!pattern) return;
      const arr = pattern.split('');
      arr[k] = arr[k] === '1' ? '0' : '1';
      const np = arr.join('');
      rebase('2');
      boxA.input.value = np;
      refresh();
      W.say(el, 'Bit ' + pos + ' is now ' + arr[k] + '. The pattern is ' + np + '.');
    }

    function setMode(m) {
      mode = m;
      tabConvert.setAttribute('aria-pressed', m === 'convert' ? 'true' : 'false');
      tabAdd.setAttribute('aria-pressed', m === 'add' ? 'true' : 'false');
      convertBox.style.display = m === 'convert' ? '' : 'none';
      addBox.style.display = m === 'add' ? '' : 'none';
      boxB.el.style.display = m === 'add' ? '' : 'none';
      boxA.lab.textContent = m === 'add' ? 'First number (A)' : 'Number';
      refresh();
    }
    tabConvert.addEventListener('click', function () { setMode('convert'); });
    tabAdd.addEventListener('click', function () { setMode('add'); });

    function showErr(msg) {
      err.textContent = msg || '';
      err.style.display = msg ? '' : 'none';
    }

    function refresh() {
      if (mode === 'convert') {
        const a = L.analyse(L.parse(boxA.input.value, base, bits), bits);
        pattern = a.pattern;
        showErr(a.error);
        paintBits();
        const keys = ['den', 'uns', 'hex', 'bcd', 'ones', 'twos'];
        keys.forEach(function (k) { ro.set(k, a.rows ? a.rows[k] : '–'); });
        bitNote.textContent = 'Place values are for two’s complement (the left-hand bit is negative). Press a bit to flip it.';
        note.textContent = a.rows ? 'Try 127, 128 and -128 with 8 bits, then 8 bits against 9 bits.' : 'Fix the input or choose more bits.';
      } else {
        const pa = L.toAddPattern(L.parse(boxA.input.value, base, bits), bits, 'A');
        const pb = L.toAddPattern(L.parse(boxB.input.value, base, bits), bits, 'B');
        const msg = pa.error || pb.error || '';
        showErr(msg);
        if (msg) {
          sum.textContent = '';
          ['carry', 'uns', 'unsov', 'sig', 'sigov'].forEach(function (k) { ra.set(k, '–'); });
          note.textContent = 'Fix the input or choose more bits.';
          return;
        }
        const s = L.addAnalyse(pa.p, pb.p);
        sum.textContent = ['carries   ' + s.carries, 'A         ' + pa.p, 'B       + ' + pb.p, '          ' + new Array(bits + 1).join('-'), 'result    ' + s.result].join('\n');
        ra.set('carry', s.carry);
        ra.set('uns', s.uns);
        ra.set('unsov', s.unsOverflow ? 'Overflow (the carry out means the result needs more than ' + bits + ' bits)' : 'No overflow');
        ra.set('sig', s.sig);
        ra.set('sigov', s.sigOverflow ? 'Overflow' + s.sigWhy : 'No overflow');
        note.textContent = 'A carry out is not always an overflow: for signed numbers look at the signs. Try -1 + -1, then 100 + 50 with 8 bits.';
      }
    }

    buildBits();
    setMode(mode);
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-binary', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = L;
})();
