/* widgets/cs-rpn.js: infix to Reverse Polish notation (shunting-yard, step by step) and RPN evaluation with a stack.
   <div class="widget" data-w="cs-rpn" data-expr="(A + B) * (C - D) / E" data-vals="A=3,B=5,C=9,D=4,E=2"></div>
   data-expr: an infix expression (variables A to Z, numbers, + - * / ^, brackets); a missing or invalid one falls back
   to the example above. data-vals: values for the variables, "A=3,B=5"; a missing one gives every variable a value.
   The model (object R) is pure and exported for a Node test (data/cs-rpn.test.js, which compares it with a Python
   model that uses fractions). Nothing throws: bad input returns {error}. Division is exact (fractions, BigInt). */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure model
  // ---------------------------------------------------------------------------------------------
  const R = {};
  R.PREC = { '+': 1, '-': 1, '*': 2, '/': 2, '^': 3 };
  R.DEFAULT_EXPR = '(A + B) * (C - D) / E';
  R.DEFAULT_VALS = 'A=3,B=5,C=9,D=4,E=2';
  R.MAXLEN = 120;

  // Tokens: {k: 'num' | 'var' | 'op' | 'lp' | 'rp', s: text}
  R.tokenize = function (text) {
    const src = String(text == null ? '' : text);
    if (src.length > R.MAXLEN) return { error: 'That is too long: use at most ' + R.MAXLEN + ' characters.' };
    const tokens = [];
    let i = 0;
    while (i < src.length) {
      const c = src[i];
      if (/\s/.test(c)) { i += 1; continue; }
      if (/[0-9]/.test(c)) {
        let j = i;
        while (j < src.length && /[0-9]/.test(src[j])) j += 1;
        if (src[j] === '.' && /[0-9]/.test(src[j + 1] || '')) {
          j += 1;
          while (j < src.length && /[0-9]/.test(src[j])) j += 1;
        }
        tokens.push({ k: 'num', s: src.slice(i, j) });
        i = j;
        continue;
      }
      if (/[A-Za-z]/.test(c)) { tokens.push({ k: 'var', s: c.toUpperCase() }); i += 1; continue; }
      if (c === '+' || c === '-' || c === '*' || c === '/' || c === '^') { tokens.push({ k: 'op', s: c }); i += 1; continue; }
      if (c === '−') { tokens.push({ k: 'op', s: '-' }); i += 1; continue; }
      if (c === '×') { tokens.push({ k: 'op', s: '*' }); i += 1; continue; }
      if (c === '÷') { tokens.push({ k: 'op', s: '/' }); i += 1; continue; }
      if (c === '(') { tokens.push({ k: 'lp', s: '(' }); i += 1; continue; }
      if (c === ')') { tokens.push({ k: 'rp', s: ')' }); i += 1; continue; }
      return { error: 'Unknown symbol "' + c + '". Use the letters A to Z, whole numbers, + - * / ^ and brackets.' };
    }
    if (!tokens.length) return { error: 'Type an expression first.' };
    return { tokens: tokens };
  };

  // Checks the order of tokens in an infix expression. Returns an error string or ''.
  R.validateInfix = function (tokens) {
    let expectOperand = true;
    let depth = 0;
    for (let i = 0; i < tokens.length; i++) {
      const t = tokens[i];
      if (expectOperand) {
        if (t.k === 'num' || t.k === 'var') expectOperand = false;
        else if (t.k === 'lp') depth += 1;
        else if (t.k === 'op' && (t.s === '-' || t.s === '+')) {
          return 'A sign in front of a value is not supported here: write 0 ' + t.s + ' X instead.';
        } else if (t.k === 'op') return 'The operator ' + t.s + ' has no operand before it.';
        else return 'An empty pair of brackets: put an expression between ( and ).';
      } else {
        if (t.k === 'op') expectOperand = true;
        else if (t.k === 'rp') {
          if (depth === 0) return 'A closing bracket ) has no opening bracket ( before it.';
          depth -= 1;
        } else if (t.k === 'lp') return 'An operator is missing before the bracket ( (for example A * (B + C)).';
        else return 'Two operands in a row (' + tokens[i - 1].s + ' then ' + t.s + '): an operator is missing between them.';
      }
    }
    if (expectOperand) return 'The expression ends too soon: the last operator or bracket needs an operand after it.';
    if (depth > 0) return 'An opening bracket ( is never closed: a ) is missing.';
    return '';
  };

  function opNames(list) { return list.join(' '); }

  // Infix to RPN with every step. Step: {i: index of the token just read (-1 = none), text, output[], ops[]}
  R.toRPN = function (text) {
    const tk = R.tokenize(text);
    if (tk.error) return { error: tk.error };
    const tokens = tk.tokens;
    const bad = R.validateInfix(tokens);
    if (bad) return { error: bad };
    const output = [];
    const ops = [];
    const steps = [{ i: -1, text: 'Start: the output and the operator stack are both empty. Read the expression from left to right.', output: [], ops: [] }];
    function snap(i, msg) { steps.push({ i: i, text: msg, output: output.slice(), ops: ops.slice() }); }
    tokens.forEach(function (t, i) {
      if (t.k === 'num' || t.k === 'var') {
        output.push(t.s);
        snap(i, 'Read ' + t.s + ': an operand goes straight to the output.');
      } else if (t.k === 'lp') {
        ops.push('(');
        snap(i, 'Read (: push it on the operator stack. It marks where the bracketed part starts.');
      } else if (t.k === 'rp') {
        const popped = [];
        while (ops.length && ops[ops.length - 1] !== '(') popped.push(ops.pop());
        ops.pop();
        popped.forEach(function (o) { output.push(o); });
        snap(i, 'Read ): ' + (popped.length ? 'pop ' + opNames(popped) + ' to the output' : 'nothing to pop') + ', then discard the matching ( .');
      } else {
        const cur = t.s;
        const right = cur === '^';
        const popped = [];
        let why = '';
        while (ops.length) {
          const top = ops[ops.length - 1];
          if (top === '(') break;
          const pt = R.PREC[top];
          const pc = R.PREC[cur];
          if (pt > pc || (pt === pc && !right)) {
            popped.push(ops.pop());
            why = pt > pc ? 'higher' : 'same';
          } else break;
        }
        popped.forEach(function (o) { output.push(o); });
        const topNow = ops.length ? ops[ops.length - 1] : null;
        ops.push(cur);
        let msg = 'Read ' + cur + ': ';
        if (popped.length) {
          msg += 'the operator' + (popped.length > 1 ? 's' : '') + ' on the stack (' + opNames(popped) + ') ' + (popped.length > 1 ? 'have' : 'has') +
            (why === 'higher' ? ' higher or equal precedence' : ' the same precedence and operators of equal precedence work left to right') +
            ', so pop ' + (popped.length > 1 ? 'them' : 'it') + ' to the output, then push ' + cur + '.';
        } else if (topNow === null) {
          msg += 'the operator stack is empty, so push it.';
        } else if (topNow === '(') {
          msg += 'the top of the stack is (, so push it.';
        } else {
          msg += 'the operator on top (' + topNow + ') has lower precedence, so push ' + cur + ' on top of it.';
        }
        snap(i, msg);
      }
    });
    if (ops.length) {
      const rest = [];
      while (ops.length) rest.push(ops.pop());
      rest.forEach(function (o) { output.push(o); });
      snap(tokens.length, 'End of the expression: pop what is left on the operator stack (' + opNames(rest) + ') to the output, top first.');
    } else {
      snap(tokens.length, 'End of the expression: the operator stack is empty, so the output is the answer.');
    }
    return { tokens: tokens, steps: steps, rpn: output.slice(), rpnText: output.join(' ') };
  };

  // ----- exact arithmetic with BigInt fractions
  function gcd(a, b) {
    a = a < 0n ? -a : a; b = b < 0n ? -b : b;
    while (b) { const t = a % b; a = b; b = t; }
    return a;
  }
  function mk(n, d) {
    if (d < 0n) { n = -n; d = -d; }
    const g = gcd(n, d) || 1n;
    return { n: n / g, d: d / g };
  }
  const LIMIT = 10n ** 40n;
  function tooBig(f) { return (f.n < 0n ? -f.n : f.n) > LIMIT || f.d > LIMIT; }
  R.parseNumber = function (s) {
    const m = /^(-?)(\d+)(?:\.(\d+))?$/.exec(String(s).trim());
    if (!m) return null;
    const frac = m[3] || '';
    let n = BigInt(m[2] + frac);
    if (m[1] === '-') n = -n;
    return mk(n, 10n ** BigInt(frac.length));
  };
  R.fracText = function (f) { return f.d === 1n ? f.n.toString() : f.n.toString() + '/' + f.d.toString(); };
  R.decimal = function (f) {
    const x = Number(f.n) / Number(f.d);
    if (!isFinite(x)) return '';
    const t = parseFloat(x.toPrecision(6));
    return String(t);
  };
  R.apply = function (op, a, b) {
    if (op === '+') return { f: mk(a.n * b.d + b.n * a.d, a.d * b.d) };
    if (op === '-') return { f: mk(a.n * b.d - b.n * a.d, a.d * b.d) };
    if (op === '*') return { f: mk(a.n * b.n, a.d * b.d) };
    if (op === '/') {
      if (b.n === 0n) return { error: 'Division by zero: the divisor is 0.' };
      return { f: mk(a.n * b.d, a.d * b.n) };
    }
    if (op === '^') {
      if (b.d !== 1n || b.n > 20n || b.n < -20n) return { error: 'The power must be a whole number from -20 to 20.' };
      const e = Number(b.n < 0n ? -b.n : b.n);
      let n = 1n, d = 1n;
      for (let i = 0; i < e; i++) { n *= a.n; d *= a.d; if (tooBig({ n: n, d: d })) return { error: 'That number is too large for this tool.' }; }
      if (b.n < 0n) {
        if (n === 0n) return { error: 'Division by zero: 0 cannot be raised to a negative power.' };
        return { f: mk(d, n) };
      }
      return { f: mk(n, d) };
    }
    return { error: 'Unknown operator ' + op + '.' };
  };

  // "A=3, B=5" -> {A: frac} or {error}
  R.parseVals = function (text) {
    const out = {};
    const src = String(text == null ? '' : text).trim();
    if (src === '') return { vals: out };
    const parts = src.split(/[,;\n]+/);
    for (let i = 0; i < parts.length; i++) {
      const p = parts[i].trim();
      if (p === '') continue;
      const m = /^([A-Za-z])\s*=\s*(.+)$/.exec(p);
      if (!m) return { error: 'Write the values as A=3, B=5 (a letter, =, a number).' };
      const f = R.parseNumber(m[2]);
      if (!f) return { error: 'The value of ' + m[1].toUpperCase() + ' must be a number such as 4, -2 or 0.5.' };
      out[m[1].toUpperCase()] = f;
    }
    return { vals: out };
  };

  // Evaluate an RPN string. Step: {i, text, stack[] (bottom first, as text)}
  R.evalRPN = function (rpnText, valsText) {
    const tk = R.tokenize(rpnText);
    if (tk.error) return { error: tk.error };
    const tokens = tk.tokens;
    for (let i = 0; i < tokens.length; i++) {
      if (tokens[i].k === 'lp' || tokens[i].k === 'rp') return { error: 'Reverse Polish notation has no brackets. Convert the expression first, or remove them.' };
    }
    const pv = R.parseVals(valsText);
    if (pv.error) return { error: pv.error };
    const stack = [];
    function show() { return stack.map(R.fracText); }
    const steps = [{ i: -1, text: 'Start: the stack is empty. Read the tokens from left to right.', stack: [] }];
    for (let i = 0; i < tokens.length; i++) {
      const t = tokens[i];
      if (t.k === 'num') {
        stack.push(R.parseNumber(t.s));
        steps.push({ i: i, text: 'Read ' + t.s + ': a number, so push it.', stack: show() });
      } else if (t.k === 'var') {
        const v = pv.vals[t.s];
        if (!v) return { error: 'No value for ' + t.s + '. Add ' + t.s + '=… to the values.' };
        stack.push(v);
        steps.push({ i: i, text: 'Read ' + t.s + ': a variable with the value ' + R.fracText(v) + ', so push ' + R.fracText(v) + '.', stack: show() });
      } else {
        if (stack.length < 2) {
          return { error: 'The operator ' + t.s + ' (token ' + (i + 1) + ') needs two values but the stack holds ' + stack.length + '. An operand is missing before it.' };
        }
        const b = stack.pop();
        const a = stack.pop();
        const r = R.apply(t.s, a, b);
        if (r.error) return { error: r.error };
        if (tooBig(r.f)) return { error: 'That number is too large for this tool.' };
        stack.push(r.f);
        steps.push({
          i: i,
          text: 'Read ' + t.s + ': pop ' + R.fracText(b) + ' (the right-hand value), then pop ' + R.fracText(a) + ' (the left-hand value). ' +
            R.fracText(a) + ' ' + t.s + ' ' + R.fracText(b) + ' = ' + R.fracText(r.f) + '. Push ' + R.fracText(r.f) + '.',
          stack: show()
        });
      }
    }
    if (stack.length !== 1) {
      return { error: stack.length === 0 ? 'There is nothing to evaluate.' : 'The stack ends with ' + stack.length + ' values instead of one: an operator is missing.' };
    }
    const f = stack[0];
    const dec = f.d === 1n ? '' : R.decimal(f);
    steps.push({ i: tokens.length, text: 'End of the expression: one value is left, so the answer is ' + R.fracText(f) + (dec ? ' (' + dec + ' as a decimal)' : '') + '.', stack: show() });
    return { tokens: tokens, steps: steps, result: R.fracText(f), decimal: dec };
  };

  // Variables used by an infix or RPN token list, in order of first use
  R.variables = function (tokens) {
    const seen = [];
    tokens.forEach(function (t) { if (t.k === 'var' && seen.indexOf(t.s) < 0) seen.push(t.s); });
    return seen;
  };
  R.defaultVals = function (tokens) {
    return R.variables(tokens).map(function (v, i) { return v + '=' + (i + 2); }).join(',');
  };

  // ---------------------------------------------------------------------------------------------
  // Widget
  // ---------------------------------------------------------------------------------------------
  function init(el, opts) {
    opts = opts || {};
    let expr = String(opts.expr == null ? '' : opts.expr).trim();
    let probe = R.toRPN(expr);
    if (probe.error) { expr = R.DEFAULT_EXPR; probe = R.toRPN(expr); }
    let vals = String(opts.vals == null ? '' : opts.vals).trim();
    if (vals === '' || R.parseVals(vals).error) vals = (expr === R.DEFAULT_EXPR && vals === '') ? R.DEFAULT_VALS : R.defaultVals(probe.tokens);

    const frame = W.frame(el, 'Reverse Polish notation', 'Convert an infix expression, then evaluate it with a stack');
    const body = frame.body;
    let tab = 'convert';

    const tabsEl = W.h('div', { 'class': 'w-tabs', role: 'group', 'aria-label': 'Choose a mode' });
    const tabBtns = {};
    [['convert', 'Convert to RPN'], ['eval', 'Evaluate RPN']].forEach(function (p) {
      const b = W.h('button', { type: 'button', 'class': 'w-tab', text: p[1] });
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () { setTab(p[0]); });
      tabBtns[p[0]] = b;
      tabsEl.appendChild(b);
    });
    body.appendChild(tabsEl);

    // ----- shared pieces
    function makeInput(label, value, width) {
      const input = W.h('input', { type: 'text', value: value });
      input.setAttribute('autocomplete', 'off');
      input.setAttribute('spellcheck', 'false');
      input.setAttribute('maxlength', String(R.MAXLEN));
      input.style.maxWidth = '100%'; input.style.boxSizing = 'border-box';
      input.style.width = '100%';
      const lab = W.h('label', { 'class': 'w-ctl', style: { maxWidth: '100%', minWidth: '0', flex: '1 1 14em' } }, W.h('span', { 'class': 'w-lab', text: label, style: { whiteSpace: 'normal' } }), input);
      return { input: input, lab: lab };
    }
    function stackTable(caption, items, topLabel) {
      const t = W.h('table', {});
      t.appendChild(W.h('caption', { 'class': 'sr-only', text: caption + (items.length ? ', top first: ' + items.slice().reverse().join(', ') : ': empty') }));
      t.appendChild(W.h('thead', {}, W.h('tr', {}, W.h('th', { scope: 'col', text: caption }), W.h('th', { scope: 'col', text: '' }))));
      const tb = W.h('tbody', {});
      if (!items.length) tb.appendChild(W.h('tr', {}, W.h('td', { text: '(empty)', style: { fontStyle: 'italic' } }), W.h('td', { text: '' })));
      for (let k = items.length - 1; k >= 0; k--) {
        tb.appendChild(W.h('tr', {}, W.h('td', { text: items[k], style: { fontWeight: '700', fontFamily: 'var(--mono, monospace)' } }), W.h('td', { text: k === items.length - 1 ? '← ' + topLabel : '' })));
      }
      t.appendChild(tb);
      return t;
    }
    function tokenLine(tokens, current) {
      const line = W.h('div', { 'class': 'w-note', style: { fontFamily: 'var(--mono, monospace)', marginTop: '10px' } });
      line.appendChild(W.h('span', { text: 'Input: ' }));
      tokens.forEach(function (t, i) {
        const s = W.h('span', { text: t.s + ' ' });
        if (i === current) { s.style.fontWeight = '700'; s.style.textDecoration = 'underline'; s.setAttribute('aria-label', 'current token ' + t.s); }
        line.appendChild(s);
      });
      if (current >= tokens.length) line.appendChild(W.h('span', { text: '(end)', style: { fontWeight: '700' } }));
      return line;
    }

    // ----- a panel: inputs, an error line, a step viewer
    function makePanel(kind) {
      const root = W.h('div', {});
      const err = W.h('div', { 'class': 'w-err', role: 'alert', style: { display: 'none' } });
      const view = W.h('div', {});
      const back = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Back' });
      const next = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Next' });
      const first = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Restart' });
      const lab = W.h('span', { 'class': 'w-step', 'aria-live': 'off' });
      const bar = W.h('div', { 'class': 'w-row w-stepper', style: { alignItems: 'center' } }, back, lab, next, first);
      const text = W.h('div', { 'aria-live': 'polite', style: { minHeight: '3.2em' } });
      const result = W.h('div', { 'class': 'w-note', style: { fontWeight: '700' } });
      const panel = { root: root, err: err, view: view, bar: bar, text: text, result: result, back: back, next: next, first: first, lab: lab, model: null, k: 0, kind: kind };
      return panel;
    }
    const pc = makePanel('convert');
    const pe = makePanel('eval');

    const exprIn = makeInput('Infix expression (letters A to Z, numbers, + - * / ^, brackets)', expr, '20em');
    const rpnIn = makeInput('RPN expression (tokens in order)', probe.rpnText, '20em');
    const valsIn = makeInput('Values of the variables, e.g. A=3, B=5', vals, '20em');
    const useBtn = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Evaluate this RPN' });

    pc.root.appendChild(W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-end' } }, exprIn.lab, useBtn));
    pc.root.appendChild(pc.err);
    pc.root.appendChild(pc.view);
    pc.root.appendChild(pc.text);
    pc.root.appendChild(pc.bar);
    pc.root.appendChild(pc.result);
    pc.root.appendChild(W.h('p', { 'class': 'w-note', text: 'Try: change the expression, then use Next to follow the operator stack. Operands go straight to the output; an operator waits on the stack until an operator of lower precedence, a closing bracket or the end of the expression forces it out. Equal precedence works left to right (the power ^ works right to left).' }));

    pe.root.appendChild(W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-end' } }, rpnIn.lab, valsIn.lab));
    pe.root.appendChild(pe.err);
    pe.root.appendChild(pe.view);
    pe.root.appendChild(pe.text);
    pe.root.appendChild(pe.bar);
    pe.root.appendChild(pe.result);
    pe.root.appendChild(W.h('p', { 'class': 'w-note', text: 'Try: step through and watch the stack. A number or variable is pushed; an operator pops two values, the first popped is the right-hand operand (so for - and / the second value down is the left-hand operand), and the answer is pushed back.' }));

    body.appendChild(pc.root);
    body.appendChild(pe.root);

    function showStep(p) {
      const m = p.model;
      p.view.textContent = '';
      if (!m) return;
      const s = m.steps[p.k];
      p.back.disabled = p.k === 0;
      p.next.disabled = p.k === m.steps.length - 1;
      p.lab.textContent = p.k === 0 ? 'Start (' + (m.steps.length - 1) + ' steps)' : 'Step ' + p.k + ' of ' + (m.steps.length - 1);
      p.view.appendChild(tokenLine(m.tokens, s.i));
      if (p.kind === 'convert') {
        const wrap = W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-start', gap: '16px' } });
        wrap.appendChild(stackTable('Operator stack', s.ops, 'top'));
        const out = W.h('div', { 'class': 'w-note', style: { fontFamily: 'var(--mono, monospace)' } });
        out.appendChild(W.h('span', { text: 'Output so far: ' }));
        out.appendChild(W.h('span', { text: s.output.length ? s.output.join(' ') : '(nothing yet)', style: { fontWeight: '700' } }));
        wrap.appendChild(out);
        p.view.appendChild(wrap);
      } else {
        p.view.appendChild(stackTable('Stack', s.stack, 'top'));
      }
      p.text.textContent = s.text;
      const last = p.k === m.steps.length - 1;
      if (last) p.result.textContent = p.kind === 'convert' ? 'RPN: ' + m.rpnText : 'Result: ' + m.result + (m.decimal ? ' (' + m.decimal + ')' : '');
      else p.result.textContent = '';
      const a = document.activeElement;
      if (a && a.disabled && p.bar.contains(a)) p.first.focus();
    }
    function go(p, n) {
      if (!p.model) return;
      p.k = Math.max(0, Math.min(p.model.steps.length - 1, n));
      showStep(p);
    }
    [pc, pe].forEach(function (p) {
      p.back.addEventListener('click', function () { go(p, p.k - 1); });
      p.next.addEventListener('click', function () { go(p, p.k + 1); });
      p.first.addEventListener('click', function () { go(p, 0); });
    });

    function setError(p, msg) {
      p.model = null;
      p.view.textContent = '';
      p.text.textContent = '';
      p.result.textContent = '';
      p.err.textContent = msg;
      p.err.style.display = '';
      p.bar.style.display = 'none';
    }
    function clearError(p) { p.err.style.display = 'none'; p.err.textContent = ''; p.bar.style.display = ''; }

    function computeConvert(keepStep) {
      const m = R.toRPN(exprIn.input.value);
      if (m.error) { setError(pc, m.error); useBtn.disabled = true; return; }
      clearError(pc);
      useBtn.disabled = false;
      pc.model = m;
      go(pc, keepStep ? pc.k : 0);
    }
    function computeEval() {
      const m = R.evalRPN(rpnIn.input.value, valsIn.input.value);
      if (m.error) { setError(pe, m.error); return; }
      clearError(pe);
      pe.model = m;
      go(pe, 0);
    }
    exprIn.input.addEventListener('input', function () { computeConvert(false); });
    rpnIn.input.addEventListener('input', computeEval);
    valsIn.input.addEventListener('input', computeEval);
    useBtn.addEventListener('click', function () {
      const m = R.toRPN(exprIn.input.value);
      if (m.error) return;
      rpnIn.input.value = m.rpnText;
      const have = R.parseVals(valsIn.input.value);
      const need = R.variables(m.tokens);
      if (have.error || need.some(function (v) { return !have.vals[v]; })) valsIn.input.value = R.defaultVals(m.tokens);
      setTab('eval');
      computeEval();
      rpnIn.input.focus();
    });

    [pc, pe].forEach(function (p) {
      p.root.addEventListener('keydown', function (e) {
        if (/input|select|textarea/i.test(e.target.tagName)) return;
        if (e.key === 'ArrowRight') { e.preventDefault(); go(p, p.k + 1); }
        else if (e.key === 'ArrowLeft') { e.preventDefault(); go(p, p.k - 1); }
      });
    });

    function setTab(t) {
      tab = t;
      tabBtns.convert.setAttribute('aria-pressed', t === 'convert' ? 'true' : 'false');
      tabBtns.eval.setAttribute('aria-pressed', t === 'eval' ? 'true' : 'false');
      pc.root.style.display = t === 'convert' ? '' : 'none';
      pe.root.style.display = t === 'eval' ? '' : 'none';
    }

    computeConvert(false);
    computeEval();
    setTab(String(opts.tab || '').toLowerCase() === 'eval' ? 'eval' : 'convert');
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-rpn', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = R;
})();
