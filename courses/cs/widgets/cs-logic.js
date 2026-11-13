/* widgets/cs-logic.js: logic gates, truth tables and logic expressions.
   <div class="widget" data-w="cs-logic" data-tab="expr" data-expr="(A AND B) OR NOT C" data-gate="XOR"></div>
   data-tab: gates or expr. data-gate: NOT AND OR NAND NOR XOR. data-expr: an expression in A to D and
   AND OR NOT NAND NOR XOR with brackets. Two different gates must be separated by brackets, as in the course.
   The logic (object L) is pure, with its own recursive-descent parser (no eval), and is exported for a Node
   test (data/cs-logic.test.js). */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure logic
  // ---------------------------------------------------------------------------------------------
  const L = {};
  L.VARS = ['A', 'B', 'C', 'D'];
  L.GATE_NAMES = ['NOT', 'AND', 'OR', 'NAND', 'NOR', 'XOR'];
  L.BIN = { AND: 1, OR: 1, NAND: 1, NOR: 1, XOR: 1 };
  L.fn = {
    NOT: function (a) { return 1 - a; },
    AND: function (a, b) { return a & b; },
    OR: function (a, b) { return a | b; },
    NAND: function (a, b) { return 1 - (a & b); },
    NOR: function (a, b) { return 1 - (a | b); },
    XOR: function (a, b) { return a ^ b; }
  };
  L.rule = {
    NOT: 'The output is the opposite of the input.',
    AND: 'The output is 1 only when both inputs are 1.',
    OR: 'The output is 1 when at least one input is 1.',
    NAND: 'The output is 0 only when both inputs are 1 (NOT AND).',
    NOR: 'The output is 1 only when both inputs are 0 (NOT OR).',
    XOR: 'The output is 1 when the inputs are different.'
  };
  L.gate = function (name, a, b) {
    if (name === 'NOT') return L.fn.NOT(a);
    return L.fn[name](a, b);
  };

  const HELP = 'Use the letters A, B, C, D and the words AND, OR, NOT, NAND, NOR, XOR with brackets.';

  function tokenize(text) {
    const toks = [];
    const s = String(text == null ? '' : text);
    let i = 0;
    while (i < s.length) {
      const ch = s.charAt(i);
      if (/\s/.test(ch)) { i++; continue; }
      if (ch === '(' || ch === ')') { toks.push(ch); i++; continue; }
      if (/[A-Za-z]/.test(ch)) {
        let j = i;
        while (j < s.length && /[A-Za-z]/.test(s.charAt(j))) j++;
        toks.push(s.slice(i, j).toUpperCase());
        i = j;
        continue;
      }
      return { error: 'The character "' + ch + '" is not allowed. ' + HELP };
    }
    return { toks: toks };
  }

  // Returns {ast, vars} or {error}. Never throws.
  L.parse = function (text) {
    const tk = tokenize(text);
    if (tk.error) return { error: tk.error };
    const toks = tk.toks;
    if (toks.length === 0) return { error: 'Type an expression, for example (A AND B) OR NOT C.' };
    if (toks.length > 200) return { error: 'That expression is too long for this tool.' };
    let pos = 0;
    const fail = function (msg) { const e = new Error(msg); e.userMessage = msg; throw e; };
    const isVar = function (t) { return t != null && L.VARS.indexOf(t) >= 0; };

    function operand() {
      const t = toks[pos];
      if (t === undefined) fail('The expression ends too soon: a value (A, B, C, D, NOT or a bracket) is missing at the end.');
      pos++;
      if (t === 'NOT') return { t: 'not', a: operand() };
      if (t === '(') {
        const inner = chain();
        if (toks[pos] !== ')') fail('A closing bracket is missing.');
        pos++;
        return inner;
      }
      if (t === ')') fail('A closing bracket has no opening bracket before it.');
      if (L.BIN[t]) fail(t + ' needs a value on its left, such as A or a bracket.');
      if (isVar(t)) return { t: 'var', n: t };
      fail('"' + t + '" is not a known word. ' + HELP);
    }

    function chain() {
      let left = operand();
      let op = null;
      while (toks[pos] !== undefined && L.BIN[toks[pos]]) {
        const o = toks[pos];
        pos++;
        if (op !== null && (o !== op || (o !== 'AND' && o !== 'OR'))) {
          fail('Add brackets to show the order of the gates, for example (A AND B) OR C, not A AND B OR C.');
        }
        op = o;
        left = { t: 'bin', op: o, a: left, b: operand() };
      }
      return left;
    }

    try {
      const ast = chain();
      if (pos < toks.length) {
        if (toks[pos] === ')') fail('A closing bracket has no opening bracket before it.');
        fail('Two values are side by side ("' + toks[pos - 1] + '" and "' + toks[pos] + '"). Put AND, OR or another gate between them.');
      }
      const vars = [];
      (function walk(n) {
        if (n.t === 'var') { if (vars.indexOf(n.n) < 0) vars.push(n.n); } else { walk(n.a); if (n.b) walk(n.b); }
      })(ast);
      vars.sort();
      return { ast: ast, vars: vars };
    } catch (e) {
      if (e && e.userMessage) return { error: e.userMessage };
      return { error: 'That expression could not be read. ' + HELP };
    }
  };

  L.evalNode = function (n, env) {
    if (n.t === 'var') return env[n.n];
    if (n.t === 'not') return 1 - L.evalNode(n.a, env);
    return L.fn[n.op](L.evalNode(n.a, env), L.evalNode(n.b, env));
  };

  L.show = function (n) {
    if (n.t === 'var') return n.n;
    if (n.t === 'not') {
      if (n.a.t === 'bin') return 'NOT (' + L.show(n.a) + ')';
      return 'NOT ' + L.show(n.a);
    }
    const wrap = function (x) { return x.t === 'bin' ? '(' + L.show(x) + ')' : L.show(x); };
    return wrap(n.a) + ' ' + n.op + ' ' + wrap(n.b);
  };

  // Every gate in the expression once, in evaluation order (inner gates first): [{text, node}].
  L.subexprs = function (ast) {
    const out = [];
    const seen = {};
    (function walk(n) {
      if (n.t === 'var') return;
      walk(n.a);
      if (n.b) walk(n.b);
      const text = L.show(n);
      if (!seen[text]) { seen[text] = 1; out.push({ text: text, node: n }); }
    })(ast);
    return out;
  };

  // The truth table: inputs in binary counting order, one value per sub-expression, and x (the final output).
  L.table = function (parsed) {
    const vars = parsed.vars;
    const subs = L.subexprs(parsed.ast);
    const n = vars.length;
    const rows = [];
    for (let i = 0; i < Math.pow(2, n); i++) {
      const env = {};
      const inputs = [];
      for (let k = 0; k < n; k++) {
        const v = (i >> (n - 1 - k)) & 1;
        env[vars[k]] = v;
        inputs.push(v);
      }
      rows.push({ inputs: inputs, work: subs.map(function (s) { return L.evalNode(s.node, env); }), x: L.evalNode(parsed.ast, env) });
    }
    return { vars: vars, subs: subs, rows: rows };
  };

  // Marks the reader's answers (array of 0, 1 or null per row) against the table.
  L.mark = function (table, answers) {
    let right = 0;
    const marks = table.rows.map(function (r, i) {
      const a = answers[i];
      const ok = a === r.x;
      if (ok) right++;
      return { ok: ok, answered: a === 0 || a === 1, want: r.x };
    });
    return { right: right, total: table.rows.length, marks: marks };
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  const SVGNS = 'http://www.w3.org/2000/svg';
  function svgEl(tag, attrs, parent) {
    const e = document.createElementNS(SVGNS, tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    if (parent) parent.appendChild(e);
    return e;
  }
  const PATHS = {
    AND: 'M0 0 H20 A20 20 0 0 1 20 40 H0 Z',
    NAND: 'M0 0 H20 A20 20 0 0 1 20 40 H0 Z',
    OR: 'M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z',
    NOR: 'M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z',
    XOR: 'M0 0 C14 0 32 6 42 20 C32 34 14 40 0 40 C7 28 7 12 0 0 Z',
    NOT: 'M0 0 L28 20 L0 40 Z'
  };
  const BUBBLE = { NAND: 44, NOR: 46, NOT: 32 };
  const OUTX = { AND: 40, OR: 42, XOR: 42, NAND: 48, NOR: 50, NOT: 36 };

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'Logic gates and truth tables', 'Try the gates, then type your own expression');
    const body = frame.body;
    let tab = opts.tab === 'gates' ? 'gates' : 'expr';
    let gate = L.GATE_NAMES.indexOf(String(opts.gate || '').toUpperCase()) >= 0 ? String(opts.gate).toUpperCase() : 'AND';
    const inputs = { A: 0, B: 0 };
    let parsed = null;
    let table = null;
    let testing = false;
    let answers = [];
    let result = null;
    let showWork = true;

    function btn(text, cls, onclick, aria) {
      const b = W.h('button', { 'class': cls || 'btn btn-sec btn-sm', type: 'button', text: text });
      b.addEventListener('click', onclick);
      if (aria) b.setAttribute('aria-label', aria);
      return b;
    }
    function group(label) {
      const g = W.h('div', { 'class': 'w-tabs' });
      g.setAttribute('role', 'group');
      g.setAttribute('aria-label', label);
      return g;
    }

    // tabs
    const tabs = group('Choose a tool');
    const tabGates = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Gates' });
    const tabExpr = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Expression' });
    tabs.appendChild(tabGates);
    tabs.appendChild(tabExpr);
    body.appendChild(tabs);

    // ----- Gates panel
    const gatePanel = W.h('div', { style: { minWidth: '0', maxWidth: '100%' } });
    const gateTabs = group('Choose a gate');
    const gateButtons = {};
    L.GATE_NAMES.forEach(function (g) {
      const b = W.h('button', { 'class': 'w-tab', type: 'button', text: g });
      b.addEventListener('click', function () { gate = g; paintGate(true); });
      gateButtons[g] = b;
      gateTabs.appendChild(b);
    });
    const inA = W.h('button', { 'class': 'btn btn-sm', type: 'button' });
    const inB = W.h('button', { 'class': 'btn btn-sm', type: 'button' });
    inA.addEventListener('click', function () { inputs.A = 1 - inputs.A; paintGate(false); });
    inB.addEventListener('click', function () { inputs.B = 1 - inputs.B; paintGate(false); });
    const outStat = W.stat('Output X', true);
    const gateRow = W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-end' } }, inA, inB, outStat.el);
    const ruleNote = W.h('div', { 'class': 'w-note' });
    const symbolWrap = W.h('div', { style: { maxWidth: '300px', margin: '4px 0' } });
    const gateTableWrap = W.h('div', { style: { overflowX: 'auto' } });
    gatePanel.appendChild(gateTabs);
    gatePanel.appendChild(gateRow);
    gatePanel.appendChild(symbolWrap);
    gatePanel.appendChild(ruleNote);
    gatePanel.appendChild(gateTableWrap);

    const sym = svgEl('svg', { viewBox: '0 0 220 100', width: '100%', role: 'img', 'aria-label': 'Logic gate' });
    sym.style.display = 'block';
    sym.style.maxWidth = '300px';
    symbolWrap.appendChild(sym);

    function paintSymbol() {
      while (sym.firstChild) sym.removeChild(sym.firstChild);
      const two = gate !== 'NOT';
      const a = inputs.A;
      const b = two ? inputs.B : 0;
      const out = L.gate(gate, a, b);
      const ink = 'var(--ink)';
      const stroke = function (v) { return v ? 'var(--sc)' : 'var(--ink-3)'; };
      const gx = 80;
      const gy = 30;
      const g = svgEl('g', { transform: 'translate(' + gx + ' ' + gy + ')' }, sym);
      svgEl('path', { d: PATHS[gate], fill: 'var(--card)', stroke: ink, 'stroke-width': '2' }, g);
      if (gate === 'XOR') svgEl('path', { d: 'M-6 0 C1 12 1 28 -6 40', fill: 'none', stroke: ink, 'stroke-width': '2' }, g);
      if (BUBBLE[gate]) svgEl('circle', { cx: BUBBLE[gate], cy: 20, r: 4, fill: 'var(--card)', stroke: ink, 'stroke-width': '2' }, g);
      const pinX = gate === 'XOR' ? gx - 2.1 : (gate === 'OR' || gate === 'NOR') ? gx + 3.9 : gx;
      const ins = two ? [[pinX, gy + 10, a, 'A'], [pinX, gy + 30, b, 'B']] : [[gx, gy + 20, a, 'A']];
      ins.forEach(function (p) {
        svgEl('line', { x1: 36, y1: p[1], x2: p[0], y2: p[1], stroke: stroke(p[2]), 'stroke-width': '3' }, sym);
        const t = svgEl('text', { x: 14, y: p[1] + 5, 'text-anchor': 'middle', fill: ink, 'font-size': '14', 'font-weight': '700' }, sym);
        t.textContent = p[3];
        const v = svgEl('text', { x: 42, y: p[1] - 5, fill: ink, 'font-size': '12' }, sym);
        v.textContent = String(p[2]);
      });
      const ox = gx + OUTX[gate];
      svgEl('line', { x1: ox, y1: gy + 20, x2: 190, y2: gy + 20, stroke: stroke(out), 'stroke-width': '3' }, sym);
      const xt = svgEl('text', { x: 200, y: gy + 25, fill: ink, 'font-size': '14', 'font-weight': '700' }, sym);
      xt.textContent = 'X';
      const xv = svgEl('text', { x: ox + 6, y: gy + 14, fill: ink, 'font-size': '12' }, sym);
      xv.textContent = String(out);
      sym.setAttribute('aria-label', gate + ' gate. ' + (two ? 'Input A is ' + a + ', input B is ' + b : 'Input A is ' + a) + '. Output X is ' + out + '.');
    }

    function paintGate(focusOnly) {
      const two = gate !== 'NOT';
      L.GATE_NAMES.forEach(function (g) { gateButtons[g].setAttribute('aria-pressed', g === gate ? 'true' : 'false'); });
      inA.textContent = 'A = ' + inputs.A;
      inA.setAttribute('aria-label', 'Input A is ' + inputs.A + '. Press to change it.');
      inA.setAttribute('aria-pressed', inputs.A ? 'true' : 'false');
      inB.textContent = 'B = ' + inputs.B;
      inB.setAttribute('aria-label', 'Input B is ' + inputs.B + '. Press to change it.');
      inB.setAttribute('aria-pressed', inputs.B ? 'true' : 'false');
      inB.style.display = two ? '' : 'none';
      const out = L.gate(gate, inputs.A, two ? inputs.B : 0);
      outStat.set(String(out));
      ruleNote.textContent = gate + ': ' + L.rule[gate];
      paintSymbol();
      // truth table with the current row marked
      gateTableWrap.textContent = '';
      const t = W.h('table', {});
      const head = W.h('tr', {});
      (two ? ['A', 'B', 'X', ''] : ['A', 'X', '']).forEach(function (h) { head.appendChild(W.h('th', { text: h, scope: 'col' })); });
      t.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      const combos = two ? [[0, 0], [0, 1], [1, 0], [1, 1]] : [[0], [1]];
      combos.forEach(function (c) {
        const x = two ? L.gate(gate, c[0], c[1]) : L.gate('NOT', c[0]);
        const now = two ? (c[0] === inputs.A && c[1] === inputs.B) : (c[0] === inputs.A);
        const cells = c.concat([x]).map(function (v) { return W.h('td', { text: String(v) }); });
        cells.push(W.h('td', { text: now ? '◀ now' : '', style: { fontWeight: '700' } }));
        const tr = W.h('tr', {}, cells);
        if (now) tr.setAttribute('aria-current', 'true');
        tb.appendChild(tr);
      });
      t.appendChild(tb);
      gateTableWrap.appendChild(t);
      if (!focusOnly) W.say(el, gate + ' with A = ' + inputs.A + (two ? ' and B = ' + inputs.B : '') + ' gives X = ' + out + '.');
    }

    // ----- Expression panel
    const exprPanel = W.h('div', { style: { minWidth: '0', maxWidth: '100%' } });
    const exprBox = W.h('input', { type: 'text', value: '' });
    exprBox.setAttribute('autocomplete', 'off');
    exprBox.setAttribute('spellcheck', 'false');
    exprBox.setAttribute('size', '30');
    exprBox.style.maxWidth = '100%';
    const exprLab = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Logic expression (A, B, C, D; AND, OR, NOT, NAND, NOR, XOR)' }), exprBox);
    const err = W.h('div', { 'class': 'w-err', 'aria-live': 'polite' });
    const heading = W.h('div', { 'class': 'w-note', style: { fontWeight: '700' } });
    const tableWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0' } });
    const testBtn = btn('Test me', 'btn btn-sm', function () { startTest(); });
    const checkBtn = btn('Check', 'btn btn-sm', function () { doCheck(); });
    const showBtn = btn('Show the answers', 'btn btn-sec btn-sm', function () { stopTest(); });
    const workChk = W.h('input', { type: 'checkbox' });
    workChk.checked = true;
    workChk.addEventListener('change', function () { showWork = workChk.checked; paintTable(); });
    workChk.style.width = 'auto';
    workChk.style.flex = 'none';
    workChk.style.margin = '0';
    const workLab = W.h('label', { style: { display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '8px', cursor: 'pointer' } }, workChk, W.h('span', { 'class': 'w-lab', text: 'Show working columns', style: { marginLeft: '6px' } }));
    const actions = W.h('div', { 'class': 'w-row', style: { alignItems: 'center' } }, testBtn, checkBtn, showBtn, workLab);
    const summary = W.h('div', { 'class': 'w-note', 'aria-live': 'polite' });
    const note = W.h('div', { 'class': 'w-note' });
    exprPanel.appendChild(exprLab);
    exprPanel.appendChild(err);
    exprPanel.appendChild(heading);
    exprPanel.appendChild(actions);
    exprPanel.appendChild(tableWrap);
    exprPanel.appendChild(summary);
    exprPanel.appendChild(note);

    exprBox.addEventListener('input', function () { testing = false; result = null; readExpr(); });

    function readExpr() {
      const p = L.parse(exprBox.value);
      if (p.error) {
        parsed = null;
        table = null;
        err.textContent = p.error;
        err.style.display = '';
        heading.textContent = '';
        tableWrap.textContent = '';
        summary.textContent = '';
        actions.style.display = 'none';
        note.textContent = 'Fix the expression to see its truth table.';
        return;
      }
      parsed = p;
      table = L.table(p);
      answers = table.rows.map(function () { return null; });
      err.textContent = '';
      err.style.display = 'none';
      actions.style.display = '';
      heading.textContent = 'X = ' + L.show(p.ast);
      paintTable();
    }

    function paintTable() {
      if (!table) return;
      tableWrap.textContent = '';
      summary.textContent = result ? result.right + ' of ' + result.total + ' rows are right.' : '';
      testBtn.style.display = testing ? 'none' : '';
      checkBtn.style.display = testing ? '' : 'none';
      showBtn.style.display = testing ? '' : 'none';
      workLab.style.display = '';
      const t = W.h('table', {});
      const head = W.h('tr', {});
      table.vars.forEach(function (v) { head.appendChild(W.h('th', { text: v, scope: 'col' })); });
      if (showWork) {
        table.subs.forEach(function (s, i) {
          if (i < table.subs.length - 1) head.appendChild(W.h('th', { text: s.text, scope: 'col' }));
        });
      }
      head.appendChild(W.h('th', { text: 'X', scope: 'col' }));
      if (result) head.appendChild(W.h('th', { text: 'Result', scope: 'col' }));
      t.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      table.rows.forEach(function (r, i) {
        const tr = W.h('tr', {});
        r.inputs.forEach(function (v) { tr.appendChild(W.h('td', { text: String(v) })); });
        if (showWork) {
          r.work.forEach(function (v, k) { if (k < r.work.length - 1) tr.appendChild(W.h('td', { text: String(v) })); });
        }
        if (testing) {
          const a = answers[i];
          const label = 'Row ' + (i + 1) + ', ' + table.vars.map(function (v, k) { return v + ' = ' + r.inputs[k]; }).join(', ') +
            '. Your answer for X is ' + (a === null ? 'not set' : a) + '. Press to change it.';
          const b = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: a === null ? '?' : String(a), style: { minWidth: '2.5em' } });
          b.setAttribute('aria-label', label);
          b.addEventListener('click', function () {
            answers[i] = answers[i] === 1 ? 0 : 1;
            result = null;
            paintTable();
            const again = tableWrap.querySelectorAll('button')[i];
            if (again) again.focus();
          });
          tr.appendChild(W.h('td', {}, b));
        } else {
          tr.appendChild(W.h('td', { text: String(r.x), style: { fontWeight: '700' } }));
        }
        if (result) {
          const m = result.marks[i];
          tr.appendChild(W.h('td', { text: m.ok ? '✓ right' : '✗ should be ' + m.want }));
        }
        tb.appendChild(tr);
      });
      t.appendChild(tb);
      tableWrap.appendChild(t);
      note.textContent = testing
        ? 'Press a ? button to set X to 0 or 1 for each row, then press Check. Tick "Show working columns" for help.'
        : 'Try (A NAND B) AND (A OR B), or NOT (A AND B), then press Test me.';
    }

    function startTest() {
      if (!table) return;
      testing = true;
      result = null;
      answers = table.rows.map(function () { return null; });
      showWork = false;
      workChk.checked = false;
      paintTable();
      const first = tableWrap.querySelector('button');
      if (first) first.focus();
      W.say(el, 'Test mode. Set X for each of the ' + table.rows.length + ' rows, then press Check.');
    }
    function doCheck() {
      if (!table) return;
      result = L.mark(table, answers);
      paintTable();
      W.say(el, result.right + ' of ' + result.total + ' rows are right.');
    }
    function stopTest() {
      testing = false;
      result = null;
      showWork = true;
      workChk.checked = true;
      paintTable();
      testBtn.focus();
    }

    function setTab(t) {
      tab = t;
      tabGates.setAttribute('aria-pressed', t === 'gates' ? 'true' : 'false');
      tabExpr.setAttribute('aria-pressed', t === 'expr' ? 'true' : 'false');
      gatePanel.style.display = t === 'gates' ? '' : 'none';
      exprPanel.style.display = t === 'expr' ? '' : 'none';
    }
    tabGates.addEventListener('click', function () { setTab('gates'); });
    tabExpr.addEventListener('click', function () { setTab('expr'); });

    body.appendChild(gatePanel);
    body.appendChild(exprPanel);
    const startExpr = opts.expr == null || String(opts.expr).trim() === '' ? '(A AND B) OR NOT C' : String(opts.expr);
    exprBox.value = startExpr;
    readExpr();
    paintGate(true);
    setTab(tab);
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-logic', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = L;
})();
