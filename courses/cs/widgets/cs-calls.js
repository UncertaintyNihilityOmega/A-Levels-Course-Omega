/* widgets/cs-calls.js: the call stack of a recursive subroutine, step by step.
   <div class="widget" data-w="cs-calls" data-fn="factorial" data-n="4"></div>
   data-fn: factorial, power (base 2), sumdigits, fib, countdown (outputs before the call) or countup (outputs after it);
   anything else gives factorial. data-n: the argument; it must be a whole number inside the range of that function
   (factorial 0 to 8, power 0 to 8, sumdigits 0 to 99999, fib 0 to 6, countdown and countup 0 to 8); a missing or invalid
   value gives the default for that function.
   The model (object S) is pure and exported for a Node test (data/cs-calls.test.js, which compares it with Python
   functions that count calls). Nothing throws: bad input returns {error}. */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure model
  // ---------------------------------------------------------------------------------------------
  const S = {};
  S.ORDER = ['factorial', 'power', 'sumdigits', 'fib', 'countdown', 'countup'];

  S.FNS = {
    factorial: {
      name: 'Factorial', proc: false, min: 0, max: 8, def: 4, arg: 'N',
      label: function (n) { return 'Factorial(' + n + ')'; },
      param: function (n) { return 'N = ' + n; },
      base: function (n) { return n <= 1; },
      baseValue: function () { return 1; },
      baseWhy: 'N <= 1',
      children: function (n) { return [n - 1]; },
      combine: function (n, v) { const r = n * v[0]; return { value: r, text: n + ' × ' + v[0] + ' = ' + r }; },
      code: 'FUNCTION Factorial(N : INTEGER) RETURNS INTEGER\n   IF N <= 1 THEN\n      RETURN 1\n   ELSE\n      RETURN N * Factorial(N - 1)\n   ENDIF\nENDFUNCTION'
    },
    power: {
      name: 'Power', proc: false, min: 0, max: 8, def: 4, arg: 'Exp (Base is 2)',
      label: function (n) { return 'Power(2, ' + n + ')'; },
      param: function (n) { return 'Base = 2, Exp = ' + n; },
      base: function (n) { return n === 0; },
      baseValue: function () { return 1; },
      baseWhy: 'Exp = 0',
      children: function (n) { return [n - 1]; },
      combine: function (n, v) { const r = 2 * v[0]; return { value: r, text: '2 × ' + v[0] + ' = ' + r }; },
      code: 'FUNCTION Power(Base : INTEGER, Exp : INTEGER) RETURNS INTEGER\n   IF Exp = 0 THEN\n      RETURN 1\n   ELSE\n      RETURN Base * Power(Base, Exp - 1)\n   ENDIF\nENDFUNCTION'
    },
    sumdigits: {
      name: 'SumDigits', proc: false, min: 0, max: 99999, def: 274, arg: 'N',
      label: function (n) { return 'SumDigits(' + n + ')'; },
      param: function (n) { return 'N = ' + n; },
      base: function (n) { return n < 10; },
      baseValue: function (n) { return n; },
      baseWhy: 'N < 10',
      children: function (n) { return [Math.floor(n / 10)]; },
      combine: function (n, v) { const d = n % 10; const r = d + v[0]; return { value: r, text: d + ' + ' + v[0] + ' = ' + r }; },
      code: 'FUNCTION SumDigits(N : INTEGER) RETURNS INTEGER\n   IF N < 10 THEN\n      RETURN N\n   ELSE\n      RETURN (N MOD 10) + SumDigits(N DIV 10)\n   ENDIF\nENDFUNCTION'
    },
    fib: {
      name: 'Fib', proc: false, min: 0, max: 6, def: 4, arg: 'N',
      label: function (n) { return 'Fib(' + n + ')'; },
      param: function (n) { return 'N = ' + n; },
      base: function (n) { return n <= 1; },
      baseValue: function (n) { return n; },
      baseWhy: 'N <= 1',
      children: function (n) { return [n - 1, n - 2]; },
      combine: function (n, v) { const r = v[0] + v[1]; return { value: r, text: v[0] + ' + ' + v[1] + ' = ' + r }; },
      code: 'FUNCTION Fib(N : INTEGER) RETURNS INTEGER\n   IF N <= 1 THEN\n      RETURN N\n   ELSE\n      RETURN Fib(N - 1) + Fib(N - 2)\n   ENDIF\nENDFUNCTION'
    },
    countdown: {
      name: 'CountDown', proc: true, before: true, after: false, min: 0, max: 8, def: 3, arg: 'N',
      label: function (n) { return 'CountDown(' + n + ')'; },
      param: function (n) { return 'N = ' + n; },
      base: function (n) { return n <= 0; },
      baseValue: function () { return null; },
      baseWhy: 'N = 0',
      children: function (n) { return [n - 1]; },
      code: 'PROCEDURE CountDown(N : INTEGER)\n   IF N > 0 THEN\n      OUTPUT N\n      CALL CountDown(N - 1)\n   ENDIF\nENDPROCEDURE'
    },
    countup: {
      name: 'CountUp', proc: true, before: false, after: true, min: 0, max: 8, def: 3, arg: 'N',
      label: function (n) { return 'CountUp(' + n + ')'; },
      param: function (n) { return 'N = ' + n; },
      base: function (n) { return n <= 0; },
      baseValue: function () { return null; },
      baseWhy: 'N = 0',
      children: function (n) { return [n - 1]; },
      code: 'PROCEDURE CountUp(N : INTEGER)\n   IF N > 0 THEN\n      CALL CountUp(N - 1)\n      OUTPUT N\n   ENDIF\nENDPROCEDURE'
    }
  };

  S.fnOf = function (v) {
    const a = String(v == null ? '' : v).trim().toLowerCase();
    return S.FNS[a] ? a : 'factorial';
  };

  // Returns {n} or {error}
  S.parseN = function (fn, text) {
    const spec = S.FNS[S.fnOf(fn)];
    const s = String(text == null ? '' : text).trim();
    if (!/^\d{1,6}$/.test(s)) return { error: 'Type a whole number from ' + spec.min + ' to ' + spec.max + '.' };
    const n = parseInt(s, 10);
    if (n < spec.min || n > spec.max) return { error: spec.name + ' accepts a whole number from ' + spec.min + ' to ' + spec.max + '.' };
    return { n: n };
  };

  // Runs the function and records a snapshot after every event.
  // A snapshot: {stack: [{label, param, status}] (oldest first), outs: [text], calls, text}
  S.run = function (fn, n) {
    const name = S.fnOf(fn);
    const spec = S.FNS[name];
    if (typeof n !== 'number' || !isFinite(n) || n < spec.min || n > spec.max || Math.floor(n) !== n) n = spec.def;
    const st = { stack: [], outs: [], calls: 0, maxDepth: 0, steps: [] };

    function snap(text) {
      st.steps.push({
        stack: st.stack.map(function (f) { return { label: f.label, param: f.param, status: f.status }; }),
        outs: st.outs.slice(),
        calls: st.calls,
        depth: st.stack.length,
        text: text
      });
    }

    snap('Start. The main program is about to call ' + spec.label(n) + '. The stack is empty.');

    function exec(arg) {
      const frame = { label: spec.label(arg), param: spec.param(arg), status: 'running' };
      st.stack.push(frame);
      st.calls += 1;
      if (st.stack.length > st.maxDepth) st.maxDepth = st.stack.length;
      snap('Call ' + frame.label + ': a new frame is pushed (call number ' + st.calls + ', ' + st.stack.length + (st.stack.length === 1 ? ' frame' : ' frames') + ' on the stack).');
      let value = null;
      if (spec.base(arg)) {
        if (spec.proc) {
          frame.status = 'base case (' + spec.baseWhy + '): does nothing and returns';
          snap(frame.label + ' reaches the base case (' + spec.baseWhy + '). It does nothing and returns; its frame is popped next.');
        } else {
          value = spec.baseValue(arg);
          frame.status = 'base case (' + spec.baseWhy + '): returns ' + value;
          snap(frame.label + ' reaches the base case (' + spec.baseWhy + ') and returns ' + value + '; its frame is popped next.');
        }
      } else {
        if (spec.proc && spec.before) {
          st.outs.push(String(arg));
          frame.status = 'outputs ' + arg + ', then calls the next one';
          snap(frame.label + ' outputs ' + arg + ' before its recursive call.');
        }
        const kids = spec.children(arg);
        const vals = [];
        for (let k = 0; k < kids.length; k++) {
          frame.status = (k > 0 ? spec.label(kids[0]) + ' = ' + vals[0] + '; now ' : '') + 'waiting for ' + spec.label(kids[k]);
          const v = exec(kids[k]);
          vals.push(v);
        }
        if (spec.proc && spec.after) {
          st.outs.push(String(arg));
          frame.status = 'outputs ' + arg + ' after the call returned';
          snap(frame.label + ' outputs ' + arg + ' after its recursive call has returned.');
        }
        if (spec.proc) {
          frame.status = 'finishes';
          snap(frame.label + ' finishes; its frame is popped next.');
        } else {
          const c = spec.combine(arg, vals);
          value = c.value;
          frame.status = 'returns ' + c.text;
          snap(frame.label + ' returns ' + c.text + '; its frame is popped next.');
        }
      }
      st.stack.pop();
      return value;
    }

    const value = exec(n);
    snap('All frames are popped. ' + (spec.proc ? spec.label(n) + ' is finished after ' + st.calls + (st.calls === 1 ? ' call.' : ' calls.')
      : spec.label(n) + ' returns ' + value + ' to the main program after ' + st.calls + (st.calls === 1 ? ' call.' : ' calls.')));
    return { fn: name, n: n, steps: st.steps, value: value, outputs: st.outs.slice(), calls: st.calls, maxDepth: st.maxDepth };
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  function init(el, opts) {
    opts = opts || {};
    let fn = S.fnOf(opts.fn);
    let spec = S.FNS[fn];
    const given = S.parseN(fn, opts.n);
    let n = given.error ? spec.def : given.n;
    let model = S.run(fn, n);
    let k = 0;
    let timer = null;

    const frame = W.frame(el, 'The call stack', 'Step through a recursive call and watch the frames pile up and pop');
    const body = frame.body;

    // ----- controls
    const sel = W.h('select', {});
    S.ORDER.forEach(function (name) {
      const o = W.h('option', { value: name, text: S.FNS[name].name + (S.FNS[name].proc ? ' (procedure)' : '') });
      sel.appendChild(o);
    });
    sel.value = fn;
    const selLab = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Subroutine' }), sel);
    const nIn = W.h('input', { type: 'text', value: String(n) });
    nIn.setAttribute('inputmode', 'numeric');
    nIn.setAttribute('autocomplete', 'off');
    nIn.setAttribute('maxlength', '5');
    nIn.style.width = '6em';
    const nLabText = W.h('span', { 'class': 'w-lab', text: 'Argument N' });
    const nLab = W.h('label', { 'class': 'w-ctl' }, nLabText, nIn);
    const err = W.h('div', { 'class': 'w-err', role: 'alert', style: { display: 'none' } });
    body.appendChild(W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-end' } }, selLab, nLab));
    body.appendChild(err);

    const code = W.h('pre', { style: { margin: '8px 0', padding: '8px 10px', fontSize: '12.5px', lineHeight: '1.45', overflowX: 'auto', maxWidth: '100%', boxSizing: 'border-box', background: 'var(--card)', border: '1px solid var(--rule)', borderRadius: '6px', color: 'var(--ink)' } });
    code.setAttribute('aria-label', 'The pseudocode being run');
    body.appendChild(code);

    // ----- what is happening now, controls, stack
    const text = W.h('div', { 'aria-live': 'polite', style: { minHeight: '3.2em', margin: '8px 0' } });
    const back = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Back' });
    const next = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Next' });
    const run = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Run' });
    const reset = W.h('button', { 'class': 'btn btn-sm btn-sec', type: 'button', text: 'Reset' });
    const lab = W.h('span', { 'class': 'w-step', 'aria-live': 'off' });
    const bar = W.h('div', { 'class': 'w-row', style: { alignItems: 'center', flexWrap: 'wrap', gap: '6px' } }, back, next, run, reset, lab);
    body.appendChild(text);
    body.appendChild(bar);

    const stackBox = W.h('div', { role: 'list', 'aria-label': 'Call stack, newest call first', style: { display: 'flex', flexDirection: 'column', gap: '4px', margin: '10px 0', maxWidth: '100%', minWidth: '0' } });
    body.appendChild(stackBox);
    const outLine = W.h('div', { style: { margin: '4px 0', fontWeight: '600', color: 'var(--ink)', overflowWrap: 'anywhere' } });
    body.appendChild(outLine);
    const stCalls = W.stat('Calls made');
    const stFrames = W.stat('Frames on the stack');
    const stDeep = W.stat('Deepest so far');
    body.appendChild(W.h('div', { 'class': 'w-out' }, stCalls.el, stFrames.el, stDeep.el));
    const note = W.h('p', { 'class': 'w-note' });
    body.appendChild(note);

    function stopTimer() {
      if (timer) { clearTimeout(timer); timer = null; }
      run.textContent = 'Run';
      run.setAttribute('aria-label', 'Run the calls automatically');
    }
    function tick() {
      timer = null;
      if (!el.isConnected) return;
      if (k >= model.steps.length - 1) { stopTimer(); return; }
      go(k + 1);
      if (k >= model.steps.length - 1) { stopTimer(); return; }
      timer = setTimeout(tick, 700);
    }

    function draw() {
      const st = model.steps[k];
      stackBox.textContent = '';
      if (!st.stack.length) {
        stackBox.appendChild(W.h('div', { role: 'listitem', text: 'The stack is empty.', style: { border: '2px dashed var(--ink-2)', borderRadius: '6px', padding: '8px 10px', color: 'var(--ink-2)' } }));
      }
      for (let i = st.stack.length - 1; i >= 0; i--) {
        const f = st.stack[i];
        const top = i === st.stack.length - 1;
        const kids = [
          W.h('div', { style: { fontWeight: '700', color: 'var(--ink)', overflowWrap: 'anywhere' }, text: f.label + (top ? '   (newest, top of the stack)' : '') }),
          W.h('div', { style: { color: 'var(--ink)', fontSize: '13px', overflowWrap: 'anywhere' }, text: f.param + ': ' + f.status })
        ];
        stackBox.appendChild(W.h('div', { role: 'listitem', style: { border: top ? '3px solid var(--sc)' : '1px solid var(--rule)', borderRadius: '6px', padding: top ? '6px 10px' : '8px 12px', background: 'var(--card)', maxWidth: '100%', boxSizing: 'border-box' } }, kids[0], kids[1]));
      }
      text.textContent = st.text;
      lab.textContent = k === 0 ? 'Start' : 'Step ' + k + ' of ' + (model.steps.length - 1);
      if (spec.proc) outLine.textContent = 'OUTPUT so far: ' + (st.outs.length ? st.outs.join('  ') : '(nothing yet)');
      else outLine.textContent = k === model.steps.length - 1 ? 'Result: ' + spec.label(model.n) + ' = ' + model.value : '';
      stCalls.set(String(st.calls));
      stFrames.set(String(st.depth));
      let deep = 0;
      for (let i = 0; i <= k; i++) if (model.steps[i].depth > deep) deep = model.steps[i].depth;
      stDeep.set(String(deep));
      back.disabled = k === 0;
      next.disabled = k >= model.steps.length - 1;
      run.disabled = k >= model.steps.length - 1 && !timer;
      const a = document.activeElement;
      if (a && a.disabled && bar.contains(a)) reset.focus();
    }

    function go(i) {
      k = Math.max(0, Math.min(model.steps.length - 1, i));
      draw();
    }

    function rebuild() {
      stopTimer();
      spec = S.FNS[fn];
      model = S.run(fn, n);
      k = 0;
      nLabText.textContent = 'Argument ' + spec.arg + ' (' + spec.min + ' to ' + spec.max + ')';
      code.textContent = spec.code;
      if (fn === 'fib') note.textContent = 'Try: N = 4 makes 9 calls, N = 5 makes 15 and N = 6 makes 25. Fib(2) is worked out again and again, so the calls grow much faster than N.';
      else if (fn === 'countdown') note.textContent = 'CountDown outputs before the recursive call, so the output comes in the order the calls are made. Compare with CountUp.';
      else if (fn === 'countup') note.textContent = 'CountUp outputs after the recursive call returns, so nothing is output until the base case has been reached, and the output comes in reverse order. Compare with CountDown.';
      else if (fn === 'sumdigits') note.textContent = 'Try: SumDigits(274). Each call drops the last digit with DIV 10 and adds it back with MOD 10 on the way up.';
      else if (fn === 'power') note.textContent = 'Try: Exp = 5 needs 6 calls (Exp = 5, 4, 3, 2, 1, 0). The base case is Exp = 0, which returns 1.';
      else note.textContent = 'Try: N = 4. The frames pile up until N = 1 (the base case), then each is popped as its value is returned: 1, 2, 6, 24.';
      draw();
    }

    function readN() {
      const p = S.parseN(fn, nIn.value);
      if (p.error) { err.textContent = p.error; err.style.display = ''; return; }
      err.style.display = 'none';
      err.textContent = '';
      n = p.n;
      rebuild();
    }
    nIn.addEventListener('input', readN);

    sel.addEventListener('change', function () {
      fn = S.fnOf(sel.value);
      spec = S.FNS[fn];
      // the argument typed so far is converted to the new range instead of becoming an error
      n = Math.max(spec.min, Math.min(spec.max, n));
      nIn.value = String(n);
      err.style.display = 'none';
      err.textContent = '';
      rebuild();
    });

    back.addEventListener('click', function () { stopTimer(); go(k - 1); });
    next.addEventListener('click', function () { stopTimer(); go(k + 1); });
    reset.addEventListener('click', function () { stopTimer(); go(0); });
    run.addEventListener('click', function () {
      if (timer) { stopTimer(); draw(); return; }
      if (k >= model.steps.length - 1) return;
      if (W.reducedMotion && W.reducedMotion()) { go(model.steps.length - 1); return; }
      run.textContent = 'Pause';
      run.setAttribute('aria-label', 'Pause the automatic run');
      timer = setTimeout(tick, 700);
      draw();
    });
    bar.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); stopTimer(); go(k + 1); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); stopTimer(); go(k - 1); }
    });

    rebuild();
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-calls', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = S;
})();
