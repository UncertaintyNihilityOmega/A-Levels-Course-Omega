/* widgets/cs-float.js: a floating-point number with a two's complement mantissa (binary point after the sign bit)
   and a two's complement exponent, in the Cambridge format. Every bit is a button; a typed denary value is stored as
   the nearest normalised pattern; Normalise shifts one place at a time.
   <div class="widget" data-w="cs-float" data-m="8" data-e="4" data-bits="01011000 0011"></div>
   data-m 6 to 16 (mantissa bits), data-e 3 to 8 (exponent bits), data-bits "mantissa exponent" (spaces optional).
   All arithmetic is exact (BigInt fractions). The logic (object L) is exported for data/cs-float.test.js. */
(function () {
  'use strict';

  const B = BigInt;
  const Z = B(0), ONE = B(1), TWO = B(2), TEN = B(10);
  const MINUS = '−';
  const SUPS = '⁰¹²³⁴⁵⁶⁷⁸⁹';

  // ---------------------------------------------------------------------------------------------
  // Pure logic
  // ---------------------------------------------------------------------------------------------
  const L = {};
  L.MINUS = MINUS;
  L.MIN_M = 6; L.MAX_M = 16; L.MIN_E = 3; L.MAX_E = 8;

  function absB(n) { return n < Z ? -n : n; }
  function gcdB(a, b) { while (b > Z) { const t = a % b; a = b; b = t; } return a; }
  function pow2(k) { return ONE << B(k); }
  function pow10(k) { let r = ONE; for (let i = 0; i < k; i++) r *= TEN; return r; }
  function bitLen(n) { return n === Z ? 0 : n.toString(2).length; }

  L.frac = function (n, d) {
    if (d < Z) { n = -n; d = -d; }
    const g = gcdB(absB(n), d);
    return g > Z ? { n: n / g, d: d / g } : { n: n, d: d };
  };
  L.twos = function (bits) {
    const v = B('0b' + bits);
    return bits.charAt(0) === '1' ? v - (ONE << B(bits.length)) : v;
  };
  L.mantissa = function (mbits) { return L.frac(L.twos(mbits), pow2(mbits.length - 1)); };
  L.exp = function (ebits) { return Number(L.twos(ebits)); };
  L.value = function (mbits, ebits) {
    const m = L.mantissa(mbits);
    const E = L.exp(ebits);
    return E >= 0 ? L.frac(m.n * pow2(E), m.d) : L.frac(m.n, m.d * pow2(-E));
  };
  L.isZero = function (mbits) { return /^0+$/.test(mbits); };
  L.isNormalised = function (mbits) { return mbits.length >= 2 && mbits.charAt(0) !== mbits.charAt(1); };
  L.exponentRange = function (e) { return { min: -Math.pow(2, e - 1), max: Math.pow(2, e - 1) - 1 }; };
  L.toBits = function (n, width) {
    let v = n < Z ? n + (ONE << B(width)) : n;
    let s = v.toString(2);
    while (s.length < width) s = '0' + s;
    return s;
  };
  L.rep = function (c, n) { let s = ''; for (let i = 0; i < n; i++) s += c; return s; };

  L.numStr = function (n) { return n < Z ? MINUS + (-n).toString() : n.toString(); };
  L.fracStr = function (f) { return f.d === ONE ? L.numStr(f.n) : L.numStr(f.n) + '/' + f.d.toString(); };

  // Exact decimal when the fraction terminates (denominator 2^a x 5^b) within 40 places, else null.
  L.exactDec = function (f) {
    const neg = f.n < Z;
    const a = absB(f.n);
    let d = f.d;
    let twos = 0;
    let fives = 0;
    while (d % TWO === Z) { d /= TWO; twos++; }
    while (d % B(5) === Z) { d /= B(5); fives++; }
    const k = Math.max(twos, fives);
    if (d !== ONE || k > 40) return null;
    let digits = (a * pow10(k) / f.d).toString();
    if (k > 0) {
      while (digits.length <= k) digits = '0' + digits;
      let whole = digits.slice(0, digits.length - k);
      let part = digits.slice(digits.length - k).replace(/0+$/, '');
      digits = part === '' ? whole : whole + '.' + part;
    }
    if (digits.replace(/[-.]/g, '').length > 30 && f.d === ONE) return null;
    return (neg ? MINUS : '') + digits;
  };
  // Scientific notation with sig significant digits, from exact BigInt arithmetic.
  L.sciStr = function (f, sig) {
    sig = sig || 6;
    if (f.n === Z) return '0';
    const neg = f.n < Z;
    const a = absB(f.n);
    const k0 = a.toString().length - f.d.toString().length;
    for (let k = k0 - 1; k <= k0 + 1; k++) {
      const t = sig - 1 - k;
      const num = t >= 0 ? a * pow10(t) : a;
      const den = t >= 0 ? f.d : f.d * pow10(-t);
      const q = (TWO * num + den) / (TWO * den);
      const qs = q.toString();
      if (qs.length === sig) {
        let m = qs.charAt(0) + (sig > 1 ? '.' + qs.slice(1).replace(/0+$/, '') : '');
        m = m.replace(/\.$/, '');
        return (neg ? MINUS : '') + m + ' × 10' + (k < 0 ? MINUS : '') + toSup(Math.abs(k));
      }
    }
    return '?';
  };
  function toSup(n) { return String(n).split('').map(function (c) { return SUPS.charAt(+c); }).join(''); }
  L.decStr = function (f) {
    if (f.n === Z) return '0';
    const ex = L.exactDec(f);
    return ex !== null ? ex : '≈ ' + L.sciStr(f, 6);
  };

  // Largest, smallest positive normalised and most negative values of an m + e format.
  L.limits = function (m, e) {
    const top = '0' + L.rep('1', e - 1);
    const out = {
      largest: { m: '0' + L.rep('1', m - 1), e: top },
      smallest: { m: '01' + L.rep('0', m - 2), e: '1' + L.rep('0', e - 1) },
      mostNegative: { m: '1' + L.rep('0', m - 1), e: top }
    };
    Object.keys(out).forEach(function (k) { out[k].value = L.value(out[k].m, out[k].e); });
    return out;
  };

  // Typed text to an exact fraction: decimals (-12.5, .25, 3) or a/b. {f} or {error}.
  L.parseValue = function (text) {
    const t = String(text == null ? '' : text).replace(/[\s_]/g, '').replace(/[−–]/g, '-');
    if (t === '') return { error: 'Type a denary value first, such as 6.25 or -3.5.' };
    let m = /^([+-])?(\d*)(?:\.(\d*))?$/.exec(t);
    if (m && (m[2] !== '' || (m[3] !== undefined && m[3] !== ''))) {
      const whole = m[2] || '';
      const part = m[3] || '';
      if (whole.length + part.length > 30) return { error: 'That has too many digits. Try a shorter number.' };
      const n = B((whole + part) || '0');
      return { f: L.frac(m[1] === '-' ? -n : n, pow10(part.length)) };
    }
    m = /^([+-])?(\d+)\/(\d+)$/.exec(t);
    if (m) {
      if (m[2].length > 30 || m[3].length > 30) return { error: 'That has too many digits. Try a shorter number.' };
      const den = B(m[3]);
      if (den === Z) return { error: 'The bottom of a fraction cannot be 0.' };
      return { f: L.frac(m[1] === '-' ? -B(m[2]) : B(m[2]), den) };
    }
    return { error: 'Use digits, a point and an optional minus sign, for example 6.25, -3.5 or 1/10.' };
  };

  function cmpPow(p, q, k) {
    const l = k >= 0 ? p : p << B(-k);
    const r = k >= 0 ? q << B(k) : q;
    return l < r ? -1 : (l > r ? 1 : 0);
  }

  // Nearest normalised pattern (ties away from zero). status: ok, zero, overflow, underflow.
  L.encode = function (f, m, e) {
    if (f.n === Z) return { status: 'zero', m: L.rep('0', m), e: L.rep('0', e) };
    const range = L.exponentRange(e);
    const neg = f.n < Z;
    const p = absB(f.n);
    const q = f.d;
    let E = bitLen(p) - bitLen(q);
    while (cmpPow(p, q, E) >= 0) E++;
    while (cmpPow(p, q, E - 1) < 0) E--;
    if (neg && cmpPow(p, q, E - 1) === 0) E--;
    const up = (m - 1) - E;
    const num = up >= 0 ? p * pow2(up) : p;
    const den = up >= 0 ? q : q * pow2(-up);
    let N = (TWO * num + den) / (TWO * den);
    if (!neg && N === pow2(m - 1)) { N = pow2(m - 2); E++; }
    if (neg && N === pow2(m - 2)) { N = pow2(m - 1); E--; }
    if (E > range.max) return { status: 'overflow' };
    if (E < range.min) return { status: 'underflow', m: L.rep('0', m), e: L.rep('0', e) };
    return { status: 'ok', m: L.toBits(neg ? -N : N, m), e: L.toBits(B(E), e) };
  };

  // One left shift of the mantissa with the exponent reduced by 1.
  L.normaliseStep = function (mbits, ebits) {
    if (L.isZero(mbits)) return { kind: 'zero' };
    if (L.isNormalised(mbits)) return { kind: 'done' };
    const E = L.exp(ebits);
    if (E - 1 < L.exponentRange(ebits.length).min) return { kind: 'blocked' };
    return { kind: 'step', m: mbits.slice(1) + '0', e: L.toBits(B(E - 1), ebits.length), from: E, to: E - 1 };
  };
  L.whyNot = function (mbits) {
    if (L.isZero(mbits)) return 'zero: every mantissa bit is 0, so there is no leading digit to shift into place';
    const c = mbits.charAt(0);
    return 'the first two bits are both ' + c + ', so the mantissa can be shifted left (a normalised ' + (c === '0' ? 'positive' : 'negative') + ' mantissa starts ' + (c === '0' ? '01' : '10') + ')';
  };

  // Change the split of bits: store the current value again in the new format (normalised, nearest).
  L.reformat = function (mbits, ebits, m2, e2) {
    const v = L.value(mbits, ebits);
    const r = L.encode(v, m2, e2);
    if (r.status === 'overflow') {
      const lim = L.limits(m2, e2);
      const big = v.n < Z ? lim.mostNegative : lim.largest;
      return { m: big.m, e: big.e, note: 'The value is too large for the new format (overflow), so the ' + (v.n < Z ? 'most negative' : 'largest') + ' value is shown instead.' };
    }
    if (r.status === 'underflow') return { m: r.m, e: r.e, note: 'The value is too close to zero for the new format (underflow), so it becomes 0.' };
    const same = L.value(r.m, r.e);
    const exact = same.n === v.n && same.d === v.d;
    return { m: r.m, e: r.e, note: exact ? 'The same value is stored again, normalised, in the new format.' : 'The value is stored again in the new format, rounded to the nearest value it can hold.' };
  };

  // Explanation of the mantissa as a sum of place values.
  L.mantissaSum = function (mbits) {
    const parts = [];
    if (mbits.charAt(0) === '1') parts.push(MINUS + '1');
    for (let i = 1; i < mbits.length; i++) if (mbits.charAt(i) === '1') parts.push('1/' + pow2(i).toString());
    return parts.length ? parts.join(' + ').replace(/\+ −/g, '− ') : '0';
  };

  L.errorPercent = function (err, x) {
    if (x.n === Z) return '';
    const pc = Math.abs(Number(err.n) / Number(err.d)) / Math.abs(Number(x.n) / Number(x.d)) * 100;
    if (!isFinite(pc)) return '';
    return pc < 0.01 ? '< 0.01%' : pc.toPrecision(2) + '%';
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  function clampInt(text, lo, hi, dflt) {
    const k = parseInt(text, 10);
    return isNaN(k) ? dflt : Math.max(lo, Math.min(hi, k));
  }
  function setAttrs(node, obj) {
    Object.keys(obj).forEach(function (k) { node.setAttribute(k, obj[k]); });
    return node;
  }
  function supPow(k) { return '2' + MINUS.replace('−', '⁻') + String(k).split('').map(function (c) { return SUPS.charAt(+c); }).join(''); }

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'Floating-point numbers', 'Toggle the bits, type a value, or normalise');
    const body = frame.body;

    // starting state from the attributes
    let m = clampInt(opts.m, L.MIN_M, L.MAX_M, 8);
    let e = clampInt(opts.e, L.MIN_E, L.MAX_E, 4);
    let mbits = null;
    let ebits = null;
    const given = String(opts.bits == null ? '' : opts.bits).trim().split(/\s+/);
    if (given.length === 2 && /^[01]+$/.test(given[0]) && /^[01]+$/.test(given[1]) &&
        given[0].length >= L.MIN_M && given[0].length <= L.MAX_M && given[1].length >= L.MIN_E && given[1].length <= L.MAX_E) {
      mbits = given[0]; ebits = given[1]; m = mbits.length; e = ebits.length;
    } else {
      const start = L.encode(L.frac(B(11), B(2)), m, e);
      mbits = start.status === 'ok' ? start.m : L.rep('0', m);
      ebits = start.status === 'ok' ? start.e : L.rep('0', e);
    }
    const initial = { m: mbits, e: ebits };
    let mButtons = [];
    let eButtons = [];

    // controls
    const mSlider = W.sliderNum({ label: 'Mantissa bits', min: L.MIN_M, max: L.MAX_M, step: 1, value: m, oninput: function () { changeFormat(); } });
    const eSlider = W.sliderNum({ label: 'Exponent bits', min: L.MIN_E, max: L.MAX_E, step: 1, value: e, oninput: function () { changeFormat(); } });
    const total = W.h('div', { 'class': 'w-note', 'aria-live': 'polite' });

    const mWrap = W.h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '3px', alignItems: 'flex-end', margin: '2px 0 8px' } });
    const eWrap = W.h('div', { style: { display: 'flex', flexWrap: 'wrap', gap: '3px', alignItems: 'flex-end', margin: '2px 0 8px' } });

    const valueBox = W.h('input', { type: 'text' });
    setAttrs(valueBox, { inputmode: 'text', autocomplete: 'off', spellcheck: 'false', size: '12', 'aria-label': 'Denary value to store' });
    valueBox.value = '';
    valueBox.placeholder = 'e.g. 6.25 or -0.1';
    const encodeBtn = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Store this value' });
    const normBtn = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Normalise (one step)' });
    const resetBtn = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Reset' });
    const entry = W.h('div', { 'class': 'w-row' },
      W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Denary value to store' }), valueBox),
      encodeBtn, normBtn, resetBtn);

    const msg = setAttrs(W.h('div', { 'class': 'w-note' }), { 'aria-live': 'polite' });
    const err = setAttrs(W.h('div', { 'class': 'w-err' }), { 'aria-live': 'polite' });
    const ro = W.readout([
      ['pattern', 'Bit pattern'], ['mant', 'Mantissa'], ['sum', 'Mantissa as place values'], ['exp', 'Exponent'],
      ['val', 'Value'], ['dec', 'Value in denary'], ['norm', 'Normalised?'],
      ['big', 'Largest positive'], ['small', 'Smallest positive normalised'], ['neg', 'Most negative']
    ]);
    if (ro.el.querySelectorAll) {
      Array.prototype.forEach.call(ro.el.querySelectorAll('td:last-child'), function (c) { c.style.overflowWrap = 'anywhere'; });
    }
    const note = W.h('div', { 'class': 'w-note', text: 'Try: press Normalise until the number is normalised and see that the value does not change. Then drag the sliders to share the bits differently: more mantissa bits give more precision, more exponent bits give more range. Type 0.1 to see a rounding error.' });

    body.appendChild(W.h('div', { 'class': 'w-row' }, mSlider.el, eSlider.el));
    body.appendChild(total);
    body.appendChild(W.h('div', { 'class': 'w-lab', text: 'Mantissa (two’s complement, binary point after the sign bit)' }));
    body.appendChild(mWrap);
    body.appendChild(W.h('div', { 'class': 'w-lab', text: 'Exponent (two’s complement integer)' }));
    body.appendChild(eWrap);
    body.appendChild(entry);
    body.appendChild(err);
    body.appendChild(msg);
    body.appendChild(ro.el);
    body.appendChild(note);

    function bitCell(bit, label, aria, onclick) {
      const btn = W.h('button', { 'class': 'w-tab', type: 'button', text: '0', style: { width: '30px', minWidth: '30px', padding: '6px 0', border: '1px solid var(--rule)', fontFamily: 'ui-monospace, Menlo, Consolas, monospace', fontSize: '16px' } });
      btn.setAttribute('aria-pressed', 'false');
      btn.addEventListener('click', onclick);
      const cell = W.h('div', { style: { textAlign: 'center' } },
        W.h('div', { text: label, style: { fontSize: '11px', color: 'var(--ink-2)', lineHeight: '1.2', whiteSpace: 'nowrap' } }), btn);
      return { cell: cell, btn: btn, aria: aria };
    }

    function buildBits() {
      mWrap.textContent = '';
      eWrap.textContent = '';
      mButtons = [];
      eButtons = [];
      for (let i = 0; i < m; i++) {
        const pv = i === 0 ? MINUS + '1' : supPow(i);
        const spoken = i === 0 ? 'minus 1' : '1/' + pow2(i).toString();
        const c = bitCell(i, pv, 'Mantissa bit ' + (i + 1) + ', place value ' + spoken, function () { flip('m', i); });
        mButtons.push(c);
        mWrap.appendChild(c.cell);
        if (i === 0) mWrap.appendChild(W.h('span', { text: '.', 'aria-hidden': 'true', style: { fontWeight: '800', fontSize: '20px', alignSelf: 'flex-end', padding: '0 1px 4px' } }));
      }
      for (let i = 0; i < e; i++) {
        const k = e - 1 - i;
        const pv = i === 0 ? MINUS + pow2(k).toString() : pow2(k).toString();
        const c = bitCell(i, pv, 'Exponent bit ' + (i + 1) + ', place value ' + (i === 0 ? 'minus ' : '') + pow2(k).toString(), function () { flip('e', i); });
        eButtons.push(c);
        eWrap.appendChild(c.cell);
      }
    }

    function showErr(text) {
      err.textContent = text || '';
      err.style.display = text ? '' : 'none';
    }
    function say(text) { msg.textContent = text; }

    function paint() {
      mButtons.forEach(function (c, i) {
        const one = mbits.charAt(i) === '1';
        c.btn.textContent = one ? '1' : '0';
        c.btn.setAttribute('aria-pressed', one ? 'true' : 'false');
        c.btn.setAttribute('aria-label', c.aria + ', now ' + (one ? '1' : '0'));
        c.btn.style.fontWeight = one ? '800' : '400';
        c.btn.style.borderColor = one ? 'var(--sc)' : 'var(--rule)';
        c.btn.style.borderWidth = one ? '2px' : '1px';
      });
      eButtons.forEach(function (c, i) {
        const one = ebits.charAt(i) === '1';
        c.btn.textContent = one ? '1' : '0';
        c.btn.setAttribute('aria-pressed', one ? 'true' : 'false');
        c.btn.setAttribute('aria-label', c.aria + ', now ' + (one ? '1' : '0'));
        c.btn.style.fontWeight = one ? '800' : '400';
        c.btn.style.borderColor = one ? 'var(--sc)' : 'var(--rule)';
        c.btn.style.borderWidth = one ? '2px' : '1px';
      });
    }

    function refresh() {
      paint();
      total.textContent = m + ' + ' + e + ' = ' + (m + e) + ' bits. The exponent runs from ' + L.numStr(B(L.exponentRange(e).min)) + ' to ' + L.exponentRange(e).max + '.';
      const mant = L.mantissa(mbits);
      const E = L.exp(ebits);
      const v = L.value(mbits, ebits);
      const spaced = mbits.charAt(0) + '.' + mbits.slice(1);
      ro.set('pattern', mbits + ' ' + ebits);
      ro.set('mant', spaced + ' = ' + L.fracStr(mant) + (mant.d === ONE ? '' : ' = ' + L.decStr(mant)));
      ro.set('sum', L.mantissaSum(mbits) + ' = ' + L.fracStr(mant));
      ro.set('exp', ebits + ' = ' + L.numStr(B(E)));
      ro.set('val', L.fracStr(mant) + ' × 2' + (E < 0 ? '⁻' : '') + toSup(Math.abs(E)) + ' = ' + L.fracStr(v));
      ro.set('dec', L.decStr(v));
      let norm;
      if (L.isNormalised(mbits)) norm = 'Normalised: the first two bits differ (' + mbits.slice(0, 2) + ')';
      else if (L.isZero(mbits)) norm = 'Not normalised: ' + L.whyNot(mbits);
      else norm = 'Not normalised: ' + L.whyNot(mbits);
      ro.set('norm', norm);
      const lim = L.limits(m, e);
      ro.set('big', lim.largest.m + ' ' + lim.largest.e + ' = ' + L.decStr(lim.largest.value));
      ro.set('small', lim.smallest.m + ' ' + lim.smallest.e + ' = ' + L.fracStr(lim.smallest.value) + ' = ' + L.decStr(lim.smallest.value));
      ro.set('neg', lim.mostNegative.m + ' ' + lim.mostNegative.e + ' = ' + L.decStr(lim.mostNegative.value));
    }

    function flip(which, i) {
      const s = which === 'm' ? mbits : ebits;
      const t = s.slice(0, i) + (s.charAt(i) === '1' ? '0' : '1') + s.slice(i + 1);
      if (which === 'm') mbits = t; else ebits = t;
      showErr('');
      say('');
      refresh();
      W.say(el, (which === 'm' ? 'Mantissa' : 'Exponent') + ' bit ' + (i + 1) + ' is now ' + t.charAt(i) + '. The value is ' + L.decStr(L.value(mbits, ebits)) + '.');
    }

    function changeFormat() {
      const m2 = clampInt(mSlider.get(), L.MIN_M, L.MAX_M, m);
      const e2 = clampInt(eSlider.get(), L.MIN_E, L.MAX_E, e);
      if (m2 === m && e2 === e) return;
      const r = L.reformat(mbits, ebits, m2, e2);
      m = m2; e = e2; mbits = r.m; ebits = r.e;
      buildBits();
      showErr('');
      say('Format changed to ' + m + ' + ' + e + ' bits. ' + r.note);
      refresh();
    }

    function store() {
      const parsed = L.parseValue(valueBox.value);
      if (parsed.error) { showErr(parsed.error); say(''); return; }
      showErr('');
      const x = parsed.f;
      const typed = valueBox.value.trim();
      const r = L.encode(x, m, e);
      const lim = L.limits(m, e);
      if (r.status === 'overflow') {
        say('Overflow: ' + typed + ' is ' + (x.n < Z ? 'more negative than the most negative' : 'larger than the largest') + ' value this format can hold (' + L.decStr(x.n < Z ? lim.mostNegative.value : lim.largest.value) + '). The exponent needed is too big for ' + e + ' exponent bits, so nothing was stored.');
        refresh();
        return;
      }
      mbits = r.m; ebits = r.e;
      refresh();
      if (r.status === 'zero') { say('0 is stored as all zeros. It cannot be normalised.'); return; }
      if (r.status === 'underflow') {
        say('Underflow: ' + typed + ' is closer to zero than the smallest positive normalised value (' + L.fracStr(lim.smallest.value) + '), so the exponent needed is too small for ' + e + ' exponent bits. It is stored as 0.');
        return;
      }
      const v = L.value(mbits, ebits);
      const diff = L.frac(v.n * x.d - x.n * v.d, v.d * x.d);
      if (diff.n === Z) say(typed + ' is stored exactly.');
      else {
        const mag = L.frac(diff.n < Z ? -diff.n : diff.n, diff.d);
        say(typed + ' cannot be stored exactly. The nearest value is ' + L.decStr(v) + '. The rounding error is ' + L.decStr(mag) + ' (' + L.errorPercent(diff, x) + '): the stored value is too ' + (diff.n < Z ? 'small' : 'large') + '.');
      }
    }

    function normalise() {
      const r = L.normaliseStep(mbits, ebits);
      showErr('');
      if (r.kind === 'zero') { say('Zero cannot be normalised: every mantissa bit is 0.'); return; }
      if (r.kind === 'done') { say('Already normalised: the first two mantissa bits differ.'); return; }
      if (r.kind === 'blocked') { say('The exponent is already as small as it can be, so the mantissa cannot be shifted further (underflow).'); return; }
      mbits = r.m; ebits = r.e;
      refresh();
      say('Shifted the mantissa left one place and reduced the exponent from ' + r.from + ' to ' + r.to + '. The value is unchanged.');
    }

    encodeBtn.addEventListener('click', store);
    valueBox.addEventListener('keydown', function (ev) { if (ev.key === 'Enter') { ev.preventDefault(); store(); } });
    normBtn.addEventListener('click', normalise);
    resetBtn.addEventListener('click', function () {
      m = initial.m.length; e = initial.e.length;
      mSlider.set(m); eSlider.set(e);
      mbits = initial.m; ebits = initial.e;
      buildBits();
      showErr('');
      say('Back to the starting pattern.');
      refresh();
    });

    buildBits();
    showErr('');
    refresh();
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-float', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = L;
})();
