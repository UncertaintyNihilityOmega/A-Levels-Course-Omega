/* units: unit converter, prefix helper and base-unit finder (phys.units, Toolbox page).
   data-tab="convert|prefix|base"  (default convert)
   data-q="length|mass|time|volume|energy|pressure|temperature"  (default length; anything else falls back to length)
   data-v="3.5"  optional starting value for the converter.
   Values: 9702 data sheet (1 u = 1.66e-27 kg, 1 eV = 1.60e-19 J). */
(function () {
  'use strict';
  W.register('units', function (el, opts) {
    const { body } = W.frame(el, 'Units, prefixes and conversions', 'Convert units, meet the prefixes, find base units');

    // ---------- data ----------
    const QUANTITIES = {
      length: { label: 'Length', base: 'm', from: 3, to: 5, v: '3.5', units: [
        ['pm', 'picometre', 1e-12], ['nm', 'nanometre', 1e-9], ['μm', 'micrometre', 1e-6], ['mm', 'millimetre', 1e-3], ['cm', 'centimetre', 1e-2],
        ['m', 'metre', 1], ['km', 'kilometre', 1e3], ['ly', 'light-year', 9.461e15], ['AU', 'astronomical unit', 1.496e11]],
        note: 'Try: 650 nm to m (visible light), or 1 ly to m. 1 ly = 9.461 × 10¹⁵ m, 1 AU = 1.496 × 10¹¹ m.' },
      mass: { label: 'Mass', base: 'kg', from: 2, to: 3, v: '250', units: [
        ['μg', 'microgram', 1e-9], ['mg', 'milligram', 1e-6], ['g', 'gram', 1e-3], ['kg', 'kilogram', 1], ['t', 'tonne', 1e3], ['u', 'unified atomic mass unit', 1.66e-27]],
        note: 'The kilogram is the SI base unit of mass. 1 u = 1.66 × 10⁻²⁷ kg (9702 data value).' },
      time: { label: 'Time', base: 's', from: 4, to: 3, v: '90', units: [
        ['ns', 'nanosecond', 1e-9], ['μs', 'microsecond', 1e-6], ['ms', 'millisecond', 1e-3], ['s', 'second', 1], ['min', 'minute', 60],
        ['h', 'hour', 3600], ['day', 'day', 86400], ['year', 'year', 3.156e7]],
        note: 'Try: 72 km h⁻¹ needs hours to seconds. 1 year = 3.156 × 10⁷ s.' },
      volume: { label: 'Volume', base: 'm³', from: 1, to: 5, v: '2.4', units: [
        ['mm³', 'cubic millimetre', 1e-9], ['cm³', 'cubic centimetre', 1e-6], ['dm³', 'cubic decimetre', 1e-3], ['L', 'litre', 1e-3],
        ['mL', 'millilitre', 1e-6], ['m³', 'cubic metre', 1]],
        note: 'The prefix is cubed with the unit: 1 cm³ = (10⁻² m)³ = 10⁻⁶ m³, and 1 L = 1 dm³.' },
      energy: { label: 'Energy', base: 'J', from: 6, to: 0, v: '1.5', units: [
        ['J', 'joule', 1], ['kJ', 'kilojoule', 1e3], ['MJ', 'megajoule', 1e6], ['eV', 'electronvolt', 1.60e-19], ['keV', 'kiloelectronvolt', 1.60e-16],
        ['MeV', 'megaelectronvolt', 1.60e-13], ['kWh', 'kilowatt-hour', 3.6e6]],
        note: '1 eV = 1.60 × 10⁻¹⁹ J (9702 data value; the exact SI value is 1.602 176 634 × 10⁻¹⁹ J).' },
      pressure: { label: 'Pressure', base: 'Pa', from: 1, to: 0, v: '101.3', units: [
        ['Pa', 'pascal', 1], ['kPa', 'kilopascal', 1e3], ['MPa', 'megapascal', 1e6], ['atm', 'standard atmosphere', 101325],
        ['mmHg', 'millimetre of mercury', 133.322], ['bar', 'bar', 1e5]],
        note: '1 atm = 101 325 Pa and 1 bar = 10⁵ Pa. The 9702 papers usually quote pressures in Pa.' },
      temperature: { label: 'Temperature', base: 'K', from: 0, to: 1, v: '25', units: [
        ['°C', 'degree Celsius', null], ['K', 'kelvin', null]],
        note: 'T / K = θ / °C + 273.15. A temperature difference of 1 K equals 1 °C. Nothing can be colder than 0 K.' }
    };
    const PREFIXES = [
      ['pico', 'p', -12, 'a capacitance of 47 pF'], ['nano', 'n', -9, 'a wavelength of 550 nm'], ['micro', 'μ', -6, 'a red blood cell, 7 μm'],
      ['milli', 'm', -3, 'a current of 5 mA'], ['centi', 'c', -2, 'a length of 2.5 cm'], ['deci', 'd', -1, '1 dm³ is one litre'],
      ['(none)', '', 0, 'a mass of 2 kg'], ['kilo', 'k', 3, 'a resistance of 4.7 kΩ'], ['mega', 'M', 6, 'a frequency of 5 MHz'],
      ['giga', 'G', 9, 'a clock speed of 3 GHz'], ['tera', 'T', 12, 'a frequency of 1 THz']
    ];
    // base-unit exponents: kg, m, s, A
    const DERIVED = [
      ['N', 'newton', 'F = ma', 'kg × m s⁻² = kg m s⁻²', [1, 1, -2, 0]],
      ['J', 'joule', 'W = Fs', 'N × m = kg m s⁻² × m', [1, 2, -2, 0]],
      ['W', 'watt', 'P = W / t', 'J ÷ s = kg m² s⁻² ÷ s', [1, 2, -3, 0]],
      ['Pa', 'pascal', 'p = F / A', 'N ÷ m² = kg m s⁻² ÷ m²', [1, -1, -2, 0]],
      ['C', 'coulomb', 'Q = It', 'A × s', [0, 0, 1, 1]],
      ['V', 'volt', 'V = W / Q', 'J ÷ C = kg m² s⁻² ÷ (A s)', [1, 2, -3, -1]],
      ['Ω', 'ohm', 'R = V / I', 'V ÷ A = kg m² s⁻³ A⁻¹ ÷ A', [1, 2, -3, -2]],
      ['Hz', 'hertz', 'f = 1 / T', '1 ÷ s', [0, 0, -1, 0]],
      ['T', 'tesla', 'F = BIL, so B = F / (IL)', 'N ÷ (A × m) = kg m s⁻² ÷ (A m)', [1, 0, -2, -1]],
      ['Wb', 'weber', 'Φ = BA', 'T × m² = kg s⁻² A⁻¹ × m²', [1, 2, -2, -1]],
      ['F', 'farad', 'C = Q / V', 'C ÷ V = A s ÷ (kg m² s⁻³ A⁻¹)', [-1, -2, 4, 2]]
    ];

    // ---------- helpers ----------
    const SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
    const supStr = (n) => String(n).split('').map((c) => SUP[c] || c).join('');
    const UNSUP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-' };

    function parseNum(raw) {
      let s = String(raw == null ? '' : raw).trim();
      if (!s) return { err: 'Type a number, for example 4.7, 4.7e3 or 4.7 × 10^3.' };
      s = s.replace(/[−–]/g, '-').replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]/g, (c) => UNSUP[c]).replace(/ | | /g, ' ');
      // "4.7 x 10^3", "4.7×10^-3", "4.7*10^3", "4.7 · 10 3" -> 4.7e3
      s = s.replace(/^\s*([+-]?\d*\.?\d+)\s*(?:[x×*·])\s*10\s*\^?\s*\(?\s*([+-]?\d+)\s*\)?\s*$/i, '$1e$2');
      // "4.7 x 10" with no exponent is just 47 (rare): leave to Number
      if (!/^[+-]?(\d+\.?\d*|\.\d+)(e[+-]?\d+)?$/i.test(s.replace(/\s+/g, ''))) {
        return { err: 'That is not a number I can read. Try 4.7, 4.7e3 or 4.7 × 10^3 (use a dot for a decimal point).' };
      }
      const x = Number(s.replace(/\s+/g, ''));
      if (!isFinite(x)) return { err: 'That number is too large or too small.' };
      return { x };
    }
    function sci(x) {
      if (x === 0) return { m: '0.000', e: 0 };
      const p = x.toExponential(3).split('e');
      return { m: p[0], e: parseInt(p[1], 10) };
    }
    function sciStr(x, unit) {
      const p = sci(x);
      return p.m + ' × 10' + supStr(p.e) + (unit ? ' ' + unit : '');
    }
    function group(s) {
      const parts = s.split('.');
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      return parts.join('.');
    }
    function plainStr(x) {
      if (x === 0) return '0';
      const a = Math.abs(x);
      if (a < 1e-4 || a >= 1e15) return null;
      let t = Number(x.toPrecision(4)).toString();
      if (/e/i.test(t)) return null;
      // group only the integer part when it has 5 or more digits
      const ip = t.replace('-', '').split('.')[0];
      return ip.length >= 5 ? group(t) : t;
    }
    function ratioStr(r) {
      const l = Math.log10(r);
      if (Math.abs(l - Math.round(l)) < 1e-9) { const k = Math.round(l); return k === 0 ? '1' : '10' + supStr(k); }
      return sciStr(r, '');
    }
    function expStr(v) {
      const names = ['kg', 'm', 's', 'A'];
      return v.map((e, i) => e === 0 ? '' : names[i] + (e === 1 ? '' : supStr(e))).filter(Boolean).join(' ');
    }
    const makeSelect = (label, items, value, onchange) => {
      const sel = W.h('select', { 'aria-label': label });
      items.forEach((t, i) => sel.append(W.h('option', { value: String(i) }, t)));
      sel.value = String(value);
      sel.addEventListener('change', () => onchange(parseInt(sel.value, 10)));
      return { sel, el: W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab' }, label), sel) };
    };

    // ---------- state ----------
    const tabNames = ['convert', 'prefix', 'base'];
    const qKey = QUANTITIES[opts.q] ? opts.q : 'length';
    const st = { tab: tabNames.indexOf(opts.tab) >= 0 ? opts.tab : 'convert', q: qKey, from: 0, to: 0, derived: 0 };
    st.from = QUANTITIES[st.q].from; st.to = QUANTITIES[st.q].to;

    // ---------- tabs ----------
    const tabLabels = { convert: 'Convert', prefix: 'Prefixes', base: 'Base units' };
    const tabRow = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose a tool' });
    const tabBtns = {};
    tabNames.forEach((t) => {
      const b = W.h('button', { class: 'w-tab', type: 'button', onclick: () => { st.tab = t; showTab(); } }, tabLabels[t]);
      tabBtns[t] = b; tabRow.append(b);
    });
    const panels = { convert: W.h('div'), prefix: W.h('div'), base: W.h('div') };
    function showTab() {
      tabNames.forEach((t) => {
        tabBtns[t].setAttribute('aria-selected', String(st.tab === t));
        panels[t].style.display = st.tab === t ? '' : 'none';
      });
    }
    body.append(tabRow, panels.convert, panels.prefix, panels.base);

    // ---------- Convert ----------
    const cErr = W.h('div', { class: 'w-err', style: { display: 'none' } });
    const cNote = W.h('div', { class: 'w-note' });
    const cOut = W.readout([['res', 'Result'], ['sci', 'Standard form'], ['work', 'Working']]);
    const valField = W.field({ label: 'Value', value: opts.v != null && opts.v !== '' ? String(opts.v) : QUANTITIES[st.q].v, type: 'text', placeholder: '4.7e3', width: '9em' });
    valField.input.setAttribute('inputmode', 'text');
    valField.input.setAttribute('autocomplete', 'off');
    const unitLabels = () => QUANTITIES[st.q].units.map((u) => u[0] + ' (' + u[1] + ')');
    let qSel, fromSel, toSel;
    qSel = makeSelect('Quantity', Object.keys(QUANTITIES).map((k) => QUANTITIES[k].label), Object.keys(QUANTITIES).indexOf(st.q), (i) => {
      st.q = Object.keys(QUANTITIES)[i];
      st.from = QUANTITIES[st.q].from; st.to = QUANTITIES[st.q].to;
      valField.input.value = QUANTITIES[st.q].v;
      fillUnits(); convert();
    });
    fromSel = makeSelect('From', unitLabels(), st.from, (i) => { st.from = i; convert(); });
    toSel = makeSelect('To', unitLabels(), st.to, (i) => { st.to = i; convert(); });
    function fillUnits() {
      [fromSel, toSel].forEach((s, k) => {
        while (s.sel.firstChild) s.sel.removeChild(s.sel.firstChild);
        unitLabels().forEach((t, i) => s.sel.append(W.h('option', { value: String(i) }, t)));
        s.sel.value = String(k === 0 ? st.from : st.to);
      });
    }
    const swapBtn = W.h('button', { class: 'btn btn-sec btn-sm', type: 'button', 'aria-label': 'Swap the two units', onclick: () => {
      const t = st.from; st.from = st.to; st.to = t;
      fromSel.sel.value = String(st.from); toSel.sel.value = String(st.to); convert();
    } }, '⇄ Swap');
    valField.input.addEventListener('input', () => convert());
    panels.convert.append(
      W.h('div', { class: 'w-row' }, qSel.el, valField.el),
      W.h('div', { class: 'w-row' }, fromSel.el, toSel.el, swapBtn),
      cErr, cOut.el, cNote
    );

    function setOut(res, sc, work) { cOut.set('res', res); cOut.set('sci', sc); cOut.set('work', work); }
    function convert() {
      const Q = QUANTITIES[st.q];
      cNote.textContent = Q.note;
      const p = parseNum(valField.input.value);
      if (p.err) { cErr.textContent = p.err; cErr.style.display = ''; setOut('–', '–', '–'); return; }
      const x = p.x, f = Q.units[st.from], t = Q.units[st.to];
      cErr.style.display = 'none';
      const raw = String(valField.input.value).trim();
      if (st.q === 'temperature') {
        const inK = f[0] === 'K' ? x : x + 273.15;
        if (inK < 0) {
          cErr.textContent = f[0] === 'K'
            ? 'A temperature below 0 K cannot exist: 0 K is absolute zero.'
            : 'A temperature below −273.15 °C cannot exist: that is below absolute zero (0 K).';
          cErr.style.display = ''; setOut('–', '–', '–'); return;
        }
        const out = t[0] === 'K' ? inK : inK - 273.15;
        const outStr = Number(out.toFixed(4)).toString();
        let work;
        if (f[0] === t[0]) work = 'Same unit, so the value does not change.';
        else if (f[0] === '°C') work = 'T / K = θ / °C + 273.15 = ' + raw + ' + 273.15 = ' + outStr + ' K';
        else work = 'θ / °C = T / K − 273.15 = ' + raw + ' − 273.15 = ' + outStr + ' °C';
        setOut(outStr + ' ' + t[0], sciStr(out, t[0]), work);
        return;
      }
      const ratio = f[2] / t[2];
      const out = x * ratio;
      if (!isFinite(out)) { cErr.textContent = 'The result is too large or too small to show.'; cErr.style.display = ''; setOut('–', '–', '–'); return; }
      const pl = plainStr(out);
      const sc = sciStr(out, t[0]);
      const work = f[0] === t[0]
        ? 'Same unit, so the value does not change.'
        : '1 ' + f[0] + ' = ' + ratioStr(ratio) + ' ' + t[0] + ', so ' + raw + ' ' + f[0] + ' × ' + ratioStr(ratio) + ' = ' + sci(out).m + ' × 10' + supStr(sci(out).e) + ' ' + t[0];
      setOut(pl == null ? 'see standard form' : pl + ' ' + t[0], sc, work);
    }

    // ---------- Prefixes ----------
    const pTable = W.h('table', { class: 'w-prefix-table' });
    pTable.append(W.h('tr', {}, W.h('th', {}, 'Prefix'), W.h('th', {}, 'Symbol'), W.h('th', {}, 'Factor'), W.h('th', {}, 'Example')));
    const pRows = [];
    PREFIXES.forEach((p) => {
      const tr = W.h('tr', {}, W.h('td', {}, p[0]), W.h('td', {}, p[1] || '–'), W.h('td', {}, '10' + supStr(p[2])), W.h('td', {}, p[3]));
      pRows.push(tr); pTable.append(tr);
    });
    const hNum = W.field({ label: 'Any number', value: '0.00047', type: 'text', placeholder: '0.00047', width: '9em' });
    const hUnit = W.field({ label: 'Unit symbol', value: 'm', type: 'text', placeholder: 'm', width: '6em' });
    hNum.input.setAttribute('autocomplete', 'off'); hUnit.input.setAttribute('autocomplete', 'off');
    const hErr = W.h('div', { class: 'w-err', style: { display: 'none' } });
    const hOut = W.readout([['sci', 'Standard form'], ['best', 'With the best prefix']]);
    const hTable = W.h('table', { class: 'w-prefix-table' });
    const hNote = W.h('div', { class: 'w-note' }, 'Try 0.00047 m, 5.6e9 Hz or 2.2e-8 F. The best prefix puts the number between 1 and 1000. Prefixes on squared or cubed units are squared or cubed too: 1 mm² = 10⁻⁶ m².');
    const wrapT = (t) => W.h('div', { style: { overflowX: 'auto', maxWidth: '100%' } }, t);
    panels.prefix.append(wrapT(pTable), W.h('div', { class: 'w-row', style: { marginTop: '10px' } }, hNum.el, hUnit.el), hErr, hOut.el, wrapT(hTable), hNote);
    const hPref = PREFIXES.filter((p) => p[1] !== 'c' && p[1] !== 'd');
    function helper() {
      const p = parseNum(hNum.input.value);
      while (hTable.firstChild) hTable.removeChild(hTable.firstChild);
      if (p.err) { hErr.textContent = p.err; hErr.style.display = ''; hOut.set('sci', '–'); hOut.set('best', '–'); return; }
      hErr.style.display = 'none';
      const x = p.x, u = (hUnit.input.value || '').trim().slice(0, 12);
      hOut.set('sci', sciStr(x, u));
      let bestPow = null;
      if (x === 0) { hOut.set('best', '0 ' + u); } else {
        const e = Math.floor(Math.log10(Math.abs(Number(x.toPrecision(12)))));
        bestPow = Math.max(-12, Math.min(12, Math.floor(e / 3) * 3));
        const pf = hPref.filter((q) => q[2] === bestPow)[0];
        const val = x / Math.pow(10, bestPow);
        const vs = plainStr(val) || sciStr(val, '');
        hOut.set('best', vs + ' ' + (pf ? pf[1] : '') + u + (Math.abs(e) > 14 ? ' (beyond the usual prefixes)' : ''));
      }
      hTable.append(W.h('tr', {}, W.h('th', {}, 'Prefix'), W.h('th', {}, 'Value')));
      hPref.forEach((q) => {
        const val = x / Math.pow(10, q[2]);
        const vs = x === 0 ? '0' : (plainStr(val) || sciStr(val, ''));
        const tr = W.h('tr', {}, W.h('td', {}, q[1] ? q[1] + (u ? u : '') + ' (' + q[0] + ')' : (u || '(base unit)') + ' (no prefix)'), W.h('td', {}, vs));
        if (bestPow === q[2]) tr.style.fontWeight = '700';
        hTable.append(tr);
      });
    }
    hNum.input.addEventListener('input', helper);
    hUnit.input.addEventListener('input', helper);

    // ---------- Base units ----------
    const dSel = makeSelect('Derived unit', DERIVED.map((d) => d[0] + ' (' + d[1] + ')'), st.derived, (i) => { st.derived = i; baseUpdate(); });
    const dOut = W.readout([['eq', 'Defining equation'], ['work', 'Working'], ['base', 'SI base units']]);
    const dTable = W.h('table', { class: 'w-prefix-table' });
    const dRows = DERIVED.map((d, i) => {
      const tr = W.h('tr', { style: { cursor: 'pointer' }, onclick: () => { st.derived = i; dSel.sel.value = String(i); baseUpdate(); } },
        W.h('td', {}, d[0] + ' (' + d[1] + ')'), W.h('td', {}, expStr(d[4])));
      dTable.append(tr); return tr;
    });
    const dNote = W.h('div', { class: 'w-note' }, 'Method: start from an equation that defines the quantity, replace each symbol with its unit, and simplify. Click any row to select it.');
    panels.base.append(W.h('div', { class: 'w-row' }, dSel.el), dOut.el, wrapT(dTable), dNote);
    function baseUpdate() {
      const d = DERIVED[st.derived];
      dOut.set('eq', d[2]);
      dOut.set('work', d[3]);
      dOut.set('base', '1 ' + d[0] + ' = 1 ' + expStr(d[4]));
      dRows.forEach((tr, i) => { tr.style.fontWeight = i === st.derived ? '700' : ''; });
    }

    // ---------- start ----------
    showTab();
    convert();
    helper();
    baseUpdate();
  });
})();
