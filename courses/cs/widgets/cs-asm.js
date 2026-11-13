/* widgets/cs-asm.js: a simulator of the Cambridge example assembly instruction set (FACTS.md "Assembly language").
   <div class="widget" data-w="cs-asm" data-program="sum" data-mode="fe" data-input="" data-bits="8"></div>
   data-program: sum, labels, countdown, indexed, mask, upper, times (a built-in program; anything else gives sum).
   data-mode: fe (Step shows every register transfer) or run (Step runs one instruction). data-input: the keyboard buffer
   for IN. data-bits: 8 or 16 (the size of ACC, IX and every memory word).
   Program text: one line per memory location; an optional leading address sets the location; an optional label with a colon;
   then an instruction or a data value (#n or n denary, Bn binary, &n hex); // starts a comment.
   The logic (object L) is pure and is exported for data/cs-asm.test.js, which compares it with data/cs.asmsim.py. */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure logic: a port of data/cs.asmsim.py
  // ---------------------------------------------------------------------------------------------
  const L = {};
  const set = function (s) { const o = {}; s.split(' ').forEach(function (k) { o[k] = true; }); return o; };
  const NOARG = set('IN OUT END');
  const REGARG = set('INC DEC MOV');
  const IMMONLY = set('LDM LDR LSL LSR');
  const ADDRONLY = set('LDD LDI LDX STO JMP CMI JPE JPN');
  const BOTH = set('ADD SUB CMP AND OR XOR');
  const isOp = function (s) { return !!(NOARG[s] || REGARG[s] || IMMONLY[s] || ADDRONLY[s] || BOTH[s]); };
  L.isOp = isOp;

  L.PROGRAMS = {
    sum: { title: 'sum: add two numbers (addresses)', input: '', text:
      '// Add the numbers in locations 200 and 201 and store the answer in 202.\n' +
      '100 LDD 200\n101 ADD 201\n102 STO 202\n103 END\n200 7\n201 5\n' },
    labels: { title: 'labels: the same sum with labels', input: '', text:
      '// The same sum, with labels instead of addresses.\n' +
      '100 START: LDD FIRST\n101 ADD SECOND\n102 STO TOTAL\n103 END\n104 FIRST: 7\n105 SECOND: 5\n106 TOTAL: 0\n' },
    countdown: { title: 'countdown: output 5 4 3 2 1', input: '', text:
      '// ASCII 53 is the character 5 and 48 is the character 0.\n' +
      '100 LDM #53\n101 LOOP: OUT\n102 DEC ACC\n103 CMP #48\n104 JPN LOOP\n105 END\n' },
    indexed: { title: 'indexed: add an array with IX', input: '', text:
      '// Add the numbers in ARRAY (the 0 marks the end) using the index register.\n' +
      '100 LDR #0\n101 LDM #0\n102 STO TOTAL\n103 LOOP: LDX ARRAY\n104 CMP #0\n105 JPE DONE\n106 ADD TOTAL\n107 STO TOTAL\n' +
      '108 INC IX\n109 JMP LOOP\n110 DONE: END\n111 ARRAY: 4\n112 9\n113 0\n114 TOTAL: 0\n' },
    mask: { title: 'mask: test bit 3 with AND', input: '', text:
      '// Output Y if bit 3 of STATUS is 1 and N if it is 0. ASCII 78 is N and 89 is Y.\n' +
      '100 LDD STATUS\n101 AND B00001000\n102 CMP #0\n103 JPN ISON\n104 LDM #78\n105 JMP SHOW\n106 ISON: LDM #89\n' +
      '107 SHOW: OUT\n108 END\n109 STATUS: B01101100\n' },
    upper: { title: 'upper: lower case to capital (IN, OUT)', input: 'q', text:
      '// Type a lower-case letter in the keyboard buffer. 97 - 65 = 32.\n' +
      '100 IN\n101 SUB #32\n102 OUT\n103 END\n' },
    times: { title: 'times: 6 x 2 by repeated addition', input: '', text:
      '// Location 200 holds 6, 201 the number of times to add, 202 the total.\n' +
      '100 LDM #0\n101 STO 202\n102 LOOP: LDD 202\n103 ADD 200\n104 STO 202\n105 LDD 201\n106 SUB #1\n107 STO 201\n' +
      '108 CMP #0\n109 JPN LOOP\n110 END\n200 6\n201 2\n202 0\n' }
  };
  L.ORDER = ['sum', 'labels', 'countdown', 'indexed', 'mask', 'upper', 'times'];

  function fail(msg) { throw new Error(msg); }

  L.valueOf = function (tok, bits) {
    const t = String(tok).trim();
    let v;
    let m = /^#?(-?\d+)$/.exec(t);
    if (m) v = parseInt(m[1], 10);
    else if (/^B[01]+$/.test(t)) v = parseInt(t.slice(1), 2);
    else if (/^&[0-9A-F]+$/.test(t)) v = parseInt(t.slice(1), 16);
    else fail('cannot read the number ' + tok + ' (use #25, B00011001 or &19)');
    const top = Math.pow(2, bits);
    if (v < 0) v += top;
    if (!(v >= 0 && v < top)) fail(tok + ' does not fit in ' + bits + ' bits (0 to ' + (top - 1) + ')');
    return v;
  };
  const isImm = function (t) { return t.charAt(0) === '#' || /^B[01]+$/.test(t) || /^&[0-9A-F]+$/.test(t); };

  // Pass 1 builds the symbol table and the location of every line; pass 2 resolves the operands.
  L.assemble = function (text, start, bits) {
    start = start == null ? 100 : start;
    bits = bits || 8;
    const items = [];
    const labels = {};
    const used = {};
    let loc = start;
    String(text).split('\n').forEach(function (raw, idx) {
      const n = idx + 1;
      let line = raw.split('//')[0].trim();
      if (!line) return;
      let m = /^(\d+)\s+(\S.*)$/.exec(line);
      if (m) { loc = parseInt(m[1], 10); line = m[2]; }
      m = /^([A-Za-z_]\w*)\s*:\s*(.*)$/.exec(line);
      if (m) {
        const label = m[1];
        line = m[2].trim();
        if (isOp(label.toUpperCase())) fail('line ' + n + ': ' + label + ' is an instruction name, not a label');
        if (Object.prototype.hasOwnProperty.call(labels, label)) fail('line ' + n + ': the label ' + label + ' is used twice');
        labels[label] = loc;
      }
      if (!line) fail('line ' + n + ': nothing after the label');
      if (used[loc]) fail('line ' + n + ': address ' + loc + ' is already used');
      used[loc] = true;
      items.push({ loc: loc, n: n, line: line });
      loc += 1;
    });
    const mem = {};
    let first = null;
    items.forEach(function (it) {
      const parts = it.line.split(/\s+/);
      const op = parts[0].toUpperCase();
      const n = it.n;
      if (isOp(op)) {
        const arg = parts.length > 1 ? parts[1] : null;
        if (parts.length > 2) fail('line ' + n + ': too many items after ' + op);
        let kind, val;
        if (NOARG[op]) {
          if (arg !== null) fail('line ' + n + ': ' + op + ' takes no operand');
          kind = 'none'; val = null;
        } else if (arg === null) {
          fail('line ' + n + ': ' + op + ' needs an operand');
        } else if (REGARG[op]) {
          const allowed = op === 'MOV' ? ['IX'] : ['ACC', 'IX'];
          if (allowed.indexOf(arg.toUpperCase()) < 0) fail('line ' + n + ': ' + op + ' needs ' + allowed.join(' or '));
          kind = 'reg'; val = arg.toUpperCase();
        } else if (IMMONLY[op] || (BOTH[op] && isImm(arg))) {
          if (!isImm(arg)) fail('line ' + n + ': ' + op + ' needs a number such as #5, B101 or &1F');
          try { val = L.valueOf(arg, bits); } catch (e) { fail('line ' + n + ': ' + e.message); }
          kind = 'imm';
        } else if (/^\d+$/.test(arg)) {
          kind = 'addr'; val = parseInt(arg, 10);
        } else if (/^[A-Za-z_]\w*$/.test(arg)) {
          if (!Object.prototype.hasOwnProperty.call(labels, arg)) fail('line ' + n + ': the label ' + arg + ' is never defined');
          kind = 'addr'; val = labels[arg];
        } else {
          fail('line ' + n + ': ' + arg + ' is not an address or a label');
        }
        mem[it.loc] = { t: 'I', op: op, kind: kind, val: val, src: it.line };
        if (first === null) first = it.loc;
      } else {
        if (parts.length !== 1) fail('line ' + n + ': ' + parts[0] + ' is not an instruction');
        let v;
        try { v = L.valueOf(parts[0], bits); } catch (e) { fail('line ' + n + ': ' + e.message); }
        mem[it.loc] = { t: 'D', val: v, src: it.line };
      }
    });
    if (first === null) fail('the program has no instructions');
    return { mem: mem, labels: labels, first: first };
  };

  // Run to END (or to an error). Returns {steps, final, error, asm}; each step has addr, text, acc, ix (new value or null),
  // mem {addr: value}, cmp (true/false/null), out (char or null) and micro [[text, {register: value}]].
  L.run = function (text, inputs, start, bits, maxSteps) {
    bits = bits || 8;
    maxSteps = maxSteps || 1000;
    let asm;
    try { asm = L.assemble(text, start, bits); } catch (e) { return { steps: [], final: null, error: e.message, asm: null }; }
    const mem = asm.mem;
    const data = {};
    Object.keys(mem).forEach(function (a) { if (mem[a].t === 'D') data[a] = mem[a].val; });
    const top = Math.pow(2, bits);
    let acc = 0, ix = 0, flag = null, pc = asm.first;
    const buf = String(inputs || '').split('');
    const steps = [];
    let error = null;
    const rd = function (a) {
      if (mem[a] && mem[a].t === 'I') fail('address ' + a + ' holds an instruction, not data');
      return Object.prototype.hasOwnProperty.call(data, a) ? data[a] : 0;
    };
    try {
      for (;;) {
        if (steps.length >= maxSteps) fail('step limit reached: the program may never reach END');
        const cell = mem[pc];
        if (!cell || cell.t !== 'I') fail('address ' + pc + ' does not hold an instruction');
        const op = cell.op, kind = cell.kind, val = cell.val;
        const ins = cell.src.replace(/^\w+\s*:\s*/, '');
        const st = { addr: pc, text: cell.src, acc: null, ix: null, mem: {}, cmp: null, out: null };
        const mi = [['MAR ← [PC]', { MAR: pc }], ['PC ← [PC] + 1', { PC: pc + 1 }],
          ['MDR ← [[MAR]]', { MDR: ins }], ['CIR ← [MDR]', { CIR: ins }]];
        let nxt = pc + 1;
        if (op === 'END') {
          mi.push(['stop the program', {}]);
          st.micro = mi; steps.push(st);
          break;
        }
        let p2, b, ea;
        if (op === 'LDM') {
          acc = val; st.acc = acc; mi.push(['ACC ← ' + val, { ACC: acc }]);
        } else if (op === 'LDD') {
          acc = rd(val); st.acc = acc;
          mi.push(['MAR ← ' + val, { MAR: val }], ['MDR ← [[MAR]]', { MDR: acc }], ['ACC ← [MDR]', { ACC: acc }]);
        } else if (op === 'LDI') {
          p2 = rd(val); acc = rd(p2); st.acc = acc;
          mi.push(['MAR ← ' + val, { MAR: val }], ['MDR ← [[MAR]]', { MDR: p2 }], ['MAR ← [MDR]', { MAR: p2 }],
            ['MDR ← [[MAR]]', { MDR: acc }], ['ACC ← [MDR]', { ACC: acc }]);
        } else if (op === 'LDX') {
          ea = val + ix; acc = rd(ea); st.acc = acc;
          mi.push(['MAR ← ' + val + ' + [IX]', { MAR: ea }], ['MDR ← [[MAR]]', { MDR: acc }], ['ACC ← [MDR]', { ACC: acc }]);
        } else if (op === 'LDR') {
          ix = val; st.ix = ix; mi.push(['IX ← ' + val, { IX: ix }]);
        } else if (op === 'MOV') {
          ix = acc; st.ix = ix; mi.push(['IX ← [ACC]', { IX: ix }]);
        } else if (op === 'STO') {
          data[val] = acc; st.mem[val] = acc;
          const w = {}; w[val] = acc;
          mi.push(['MAR ← ' + val, { MAR: val }], ['MDR ← [ACC]', { MDR: acc }], ['[[MAR]] ← [MDR]', { mem: w }]);
        } else if (op === 'ADD' || op === 'SUB' || op === 'AND' || op === 'OR' || op === 'XOR') {
          const sym = { ADD: '+', SUB: '-', AND: 'AND', OR: 'OR', XOR: 'XOR' }[op];
          if (kind === 'imm') {
            b = val; mi.push(['ACC ← [ACC] ' + sym + ' ' + val, {}]);
          } else {
            b = rd(val);
            mi.push(['MAR ← ' + val, { MAR: val }], ['MDR ← [[MAR]]', { MDR: b }], ['ACC ← [ACC] ' + sym + ' [MDR]', {}]);
          }
          let r;
          if (op === 'ADD') r = acc + b; else if (op === 'SUB') r = acc - b;
          else if (op === 'AND') r = acc & b; else if (op === 'OR') r = acc | b; else r = acc ^ b;
          acc = ((r % top) + top) % top; st.acc = acc;
          mi[mi.length - 1][1].ACC = acc;
        } else if (op === 'INC' || op === 'DEC') {
          const d = op === 'INC' ? 1 : -1;
          if (val === 'ACC') { acc = (((acc + d) % top) + top) % top; st.acc = acc; } else { ix = (((ix + d) % top) + top) % top; st.ix = ix; }
          const o = {}; o[val] = val === 'ACC' ? acc : ix;
          mi.push([val + ' ← [' + val + '] ' + (d === 1 ? '+' : '-') + ' 1', o]);
        } else if (op === 'LSL' || op === 'LSR') {
          acc = op === 'LSL' ? ((acc * Math.pow(2, val)) % top) : Math.floor(acc / Math.pow(2, val));
          st.acc = acc;
          mi.push(['ACC ← [ACC] shifted ' + (op === 'LSL' ? 'left' : 'right') + ' ' + val + ' place' + (val !== 1 ? 's' : ''), { ACC: acc }]);
        } else if (op === 'JMP') {
          nxt = val; mi.push(['PC ← ' + val, { PC: val }]);
        } else if (op === 'CMP' || op === 'CMI') {
          if (kind === 'imm') {
            b = val; mi.push(['compare [ACC] with ' + val, {}]);
          } else if (op === 'CMP') {
            b = rd(val);
            mi.push(['MAR ← ' + val, { MAR: val }], ['MDR ← [[MAR]]', { MDR: b }], ['compare [ACC] with [MDR]', {}]);
          } else {
            p2 = rd(val); b = rd(p2);
            mi.push(['MAR ← ' + val, { MAR: val }], ['MDR ← [[MAR]]', { MDR: p2 }], ['MAR ← [MDR]', { MAR: p2 }],
              ['MDR ← [[MAR]]', { MDR: b }], ['compare [ACC] with [MDR]', {}]);
          }
          flag = acc === b; st.cmp = flag;
          mi[mi.length - 1] = [mi[mi.length - 1][0] + '; status ← ' + (flag ? 'TRUE' : 'FALSE'), { SR: flag ? 'TRUE' : 'FALSE' }];
        } else if (op === 'JPE' || op === 'JPN') {
          if (flag === null) fail('address ' + pc + ': ' + op + ' before any compare');
          const go = flag === (op === 'JPE');
          mi.push(['test the status register: ' + (flag ? 'TRUE' : 'FALSE'), {}]);
          if (go) { nxt = val; mi.push(['PC ← ' + val, { PC: val }]); } else mi.push(['no jump: PC is unchanged', {}]);
        } else if (op === 'IN') {
          if (!buf.length) fail('IN: the keyboard buffer is empty');
          acc = buf.shift().charCodeAt(0);
          if (acc >= top) fail('IN: that character does not fit in ' + bits + ' bits');
          st.acc = acc; mi.push(['ACC ← ASCII code of the key pressed (' + acc + ')', { ACC: acc }]);
        } else if (op === 'OUT') {
          st.out = String.fromCharCode(acc);
          mi.push(['output the character whose code is [ACC] (' + acc + ')', {}]);
        }
        st.micro = mi;
        steps.push(st);
        pc = nxt;
      }
    } catch (e) { error = e.message; }
    let out = '';
    steps.forEach(function (s) { if (s.out !== null) out += s.out; });
    return { steps: steps, error: error, asm: asm,
      final: { acc: acc, ix: ix, mem: data, labels: asm.labels, out: out } };
  };

  // ---------------------------------------------------------------------------------------------
  // The widget
  // ---------------------------------------------------------------------------------------------
  function attrs(node, obj) { Object.keys(obj).forEach(function (k) { node.setAttribute(k, obj[k]); }); return node; }
  const MONO = 'ui-monospace, Menlo, Consolas, monospace';

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'Assembly language simulator', 'Step through a program and watch the registers and memory');
    const body = frame.body;
    let name = L.PROGRAMS[opts.program] ? opts.program : 'sum';
    let mode = opts.mode === 'run' ? 'run' : 'fe';
    let bits = opts.bits === '16' ? 16 : 8;
    let dirty = false;
    let timer = null;
    let run = null;      // result of L.run
    let regs = null, data = null, changed = null, si = 0, sj = 0, started = false, ended = false, count = 0, outText = '';

    // ---- controls
    const sel = W.h('select', {});
    L.ORDER.forEach(function (k) { sel.appendChild(W.h('option', { value: k, text: L.PROGRAMS[k].title })); });
    sel.appendChild(W.h('option', { value: 'own', text: 'your own program' }));
    sel.value = name;
    const selCtl = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Program' }), sel);

    const kbd = attrs(W.h('input', { type: 'text' }), { autocomplete: 'off', spellcheck: 'false', size: '8', maxlength: '40' });
    kbd.value = opts.input != null && opts.input !== '' ? String(opts.input).slice(0, 40) : L.PROGRAMS[name].input;
    const kbdCtl = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Keyboard buffer (read by IN)' }), kbd);

    const tabs = attrs(W.h('div', { 'class': 'w-tabs' }), { role: 'group', 'aria-label': 'Step size' });
    const tabFe = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Fetch-execute' });
    const tabRun = W.h('button', { 'class': 'w-tab', type: 'button', text: 'Whole instructions' });
    tabs.appendChild(tabFe); tabs.appendChild(tabRun);

    const ta = attrs(W.h('textarea', { style: { width: '100%', boxSizing: 'border-box', fontFamily: MONO, fontSize: '14px', minHeight: '190px', resize: 'vertical' } }),
      { 'aria-label': 'Assembly language program', spellcheck: 'false', rows: '12' });
    ta.value = L.PROGRAMS[name].text;

    const bReset = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Reset' });
    const bStep = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Step' });
    const bRun = W.h('button', { 'class': 'btn btn-sm', type: 'button', text: 'Run' });
    const buttons = W.h('div', { 'class': 'w-row' }, bReset, bStep, bRun);

    const err = attrs(W.h('div', { 'class': 'w-err' }), { 'aria-live': 'polite' });
    const status = attrs(W.h('div', { 'class': 'w-note' }), { 'aria-live': 'polite' });

    const ro = W.readout([['PC', 'Program counter (PC)'], ['MAR', 'MAR'], ['MDR', 'MDR'], ['CIR', 'CIR'],
      ['ACC', 'Accumulator (ACC)'], ['IX', 'Index register (IX)'], ['SR', 'Compare result (status)']]);
    const outEl = attrs(W.h('div', { style: { fontFamily: MONO, minHeight: '1.4em', wordBreak: 'break-all' } }), { 'aria-live': 'polite' });
    const outBox = W.h('div', {}, W.h('div', { 'class': 'w-lab', text: 'OUTPUT' }), outEl);
    const microList = W.h('ol', { style: { margin: '4px 0', paddingLeft: '22px', fontFamily: MONO, fontSize: '13px' } });
    const microBox = W.h('div', {}, W.h('div', { 'class': 'w-lab', text: 'Register transfers of this instruction' }), microList);
    const left = W.h('div', { style: { minWidth: '0' } }, ro.el, outBox, microBox);

    const memBody = W.h('tbody', {});
    const memTable = attrs(W.h('table', { style: { width: '100%', fontFamily: MONO, fontSize: '13px' } },
      W.h('thead', {}, W.h('tr', {}, W.h('th', { text: 'Address' }), W.h('th', { text: 'Label' }), W.h('th', { text: 'Contents' }), W.h('th', { text: 'Marker' }))), memBody),
      { 'aria-label': 'Memory: address, label and contents' });
    const memWrap = W.h('div', { style: { overflow: 'auto', maxHeight: '300px', minWidth: '0', maxWidth: '100%' } }, memTable);
    const right = W.h('div', { style: { minWidth: '0' } }, W.h('div', { 'class': 'w-lab', text: 'Memory' }), memWrap);
    const grid = W.h('div', { style: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(230px, 1fr))', gap: '12px', marginTop: '8px' } }, left, right);
    const note = W.h('div', { 'class': 'w-note', text: 'This simulator has 8-bit words (0 to 255) and one general purpose register, ACC. Try changing a number in the program, or write your own: an address, a label and an instruction on each line.' });

    body.appendChild(W.h('div', { 'class': 'w-row' }, selCtl, kbdCtl));
    body.appendChild(tabs);
    body.appendChild(ta);
    body.appendChild(buttons);
    body.appendChild(err);
    body.appendChild(status);
    body.appendChild(grid);
    body.appendChild(note);

    // ---- machine state
    function applyMicro(upd) {
      Object.keys(upd).forEach(function (k) {
        if (k === 'mem') {
          Object.keys(upd.mem).forEach(function (a) { data[a] = upd.mem[a]; changed[a] = true; });
        } else regs[k] = upd[k];
      });
    }

    function show(v) { return v === '' || v == null ? '–' : String(v); }

    function labelAt(addr) {
      const labs = run && run.asm ? run.asm.labels : {};
      const out = [];
      Object.keys(labs).forEach(function (k) { if (labs[k] === addr) out.push(k); });
      return out.join(', ');
    }

    function paint() {
      ['PC', 'MAR', 'MDR', 'CIR', 'ACC', 'IX', 'SR'].forEach(function (k) { ro.set(k, show(regs ? regs[k] : '')); });
      outEl.textContent = outText;
      // memory
      memBody.textContent = '';
      if (run && run.asm) {
        const addrs = {};
        Object.keys(run.asm.mem).forEach(function (a) { addrs[a] = true; });
        Object.keys(data || {}).forEach(function (a) { addrs[a] = true; });
        Object.keys(addrs).map(Number).sort(function (a, b) { return a - b; }).forEach(function (a) {
          const cell = run.asm.mem[a];
          let contents, mark = '';
          if (cell && cell.t === 'I') contents = cell.src.replace(/^\w+\s*:\s*/, '');
          else {
            const v = data[a] != null ? data[a] : (cell ? cell.val : 0);
            contents = String(v) + (bits === 8 ? ' (' + ('00000000' + v.toString(2)).slice(-8) + ')' : '');
          }
          if (regs && Number(regs.PC) === a) mark = '◄ PC';
          if (curAddr !== null && curAddr === a) mark = (mark ? mark + ', ' : '') + 'executing';
          if (changed && changed[a]) mark = (mark ? mark + ', ' : '') + 'changed';
          const tr = W.h('tr', {}, W.h('td', { text: String(a) }), W.h('td', { text: labelAt(a) }), W.h('td', { text: contents }), W.h('td', { text: mark }));
          if (mark.indexOf('PC') >= 0 || mark.indexOf('executing') >= 0) tr.style.fontWeight = '700';
          memBody.appendChild(tr);
        });
      }
      // micro list
      microList.textContent = '';
      const stp = run && run.steps[si];
      if (stp && mode === 'fe') {
        stp.micro.forEach(function (m, k) {
          const done = started && (k < sj);
          const li = W.h('li', { text: (done ? '✓ ' : (k === sj ? '▶ ' : '')) + m[0] });
          if (k === sj) li.style.fontWeight = '700';
          microList.appendChild(li);
        });
      }
      microBox.style.display = mode === 'fe' ? '' : 'none';
      tabFe.setAttribute('aria-pressed', mode === 'fe' ? 'true' : 'false');
      tabRun.setAttribute('aria-pressed', mode === 'run' ? 'true' : 'false');
      bRun.textContent = timer ? 'Pause' : 'Run';
      bRun.setAttribute('aria-pressed', timer ? 'true' : 'false');
    }
    let curAddr = null;

    function stop() { if (timer) { clearTimeout(timer); timer = null; } }

    function reset() {
      stop();
      err.textContent = ''; status.textContent = '';
      run = L.run(ta.value, kbd.value, 100, bits, 1000);
      dirty = false;
      if (run.error && !run.steps.length) {
        err.textContent = run.error;
        regs = null; data = {}; changed = {}; outText = ''; run.asm = null; curAddr = null;
        paint();
        return;
      }
      regs = { PC: run.asm.first, MAR: '', MDR: '', CIR: '', ACC: 0, IX: 0, SR: '' };
      data = {};
      Object.keys(run.asm.mem).forEach(function (a) { if (run.asm.mem[a].t === 'D') data[a] = run.asm.mem[a].val; });
      changed = {}; si = 0; sj = 0; started = false; ended = false; count = 0; outText = ''; curAddr = null;
      status.textContent = 'Ready. The program counter holds ' + regs.PC + '. Press Step.';
      paint();
    }

    function finishMessage() {
      if (run.error) { err.textContent = 'Stopped: ' + run.error + '.'; return 'Stopped: ' + run.error + '.'; }
      return 'The program has ended (END). Press Reset to run it again.';
    }

    // execute one register transfer (fe) or one whole instruction
    function advance(whole) {
      if (dirty || !run) reset();
      if (!run || !run.asm || ended) { if (ended) W.say(el, status.textContent); return false; }
      const stp = run.steps[si];
      if (!stp) { ended = true; status.textContent = finishMessage(); curAddr = null; paint(); W.say(el, status.textContent); return false; }
      started = true;
      changed = {};
      curAddr = stp.addr;
      let said = '';
      if (whole) {
        stp.micro.forEach(function (m) { applyMicro(m[1]); });
        sj = stp.micro.length;
        said = stp.text.replace(/^\w+\s*:\s*/, '');
      } else {
        const m = stp.micro[sj];
        applyMicro(m[1]);
        said = m[0];
        sj += 1;
      }
      if (sj >= stp.micro.length) {
        count += 1;
        if (stp.out !== null) outText += stp.out;
        said = whole ? 'Executed ' + stp.text.replace(/^\w+\s*:\s*/, '') + '.' : said + '. Instruction ' + count + ' is complete.';
        si += 1; sj = 0; curAddr = whole || sj === 0 ? null : curAddr;
        if (stp.out !== null) said += ' Output: ' + stp.out;
        if (!run.steps[si]) {
          if (stp.text.replace(/^\w+\s*:\s*/, '').toUpperCase() === 'END') { ended = true; said += ' ' + finishMessage(); }
          else if (run.error) { ended = true; said += ' ' + finishMessage(); }
        }
      }
      status.textContent = said;
      paint();
      W.say(el, said);
      return !ended;
    }

    bStep.addEventListener('click', function () { stop(); advance(mode === 'run'); });
    bReset.addEventListener('click', function () { reset(); W.say(el, status.textContent || err.textContent); });
    bRun.addEventListener('click', function () {
      if (timer) { stop(); paint(); W.say(el, 'Paused.'); return; }
      if (dirty || !run) reset();
      if (!run || !run.asm) return;
      if (ended) reset();
      if (W.reducedMotion && W.reducedMotion()) {
        let guard = 0;
        while (guard++ < 2000 && advance(true)) { /* run to the end at once */ }
        return;
      }
      const tick = function () {
        const more = advance(true);
        timer = more ? setTimeout(tick, 220) : null;
        paint();
      };
      timer = setTimeout(tick, 0);
      paint();
    });
    tabFe.addEventListener('click', function () { mode = 'fe'; paint(); });
    tabRun.addEventListener('click', function () { mode = 'run'; paint(); });
    sel.addEventListener('change', function () {
      if (sel.value !== 'own' && L.PROGRAMS[sel.value]) {
        name = sel.value;
        ta.value = L.PROGRAMS[name].text;
        kbd.value = L.PROGRAMS[name].input;
      }
      reset();
    });
    ta.addEventListener('input', function () { dirty = true; stop(); sel.value = 'own'; status.textContent = 'The program has changed: press Reset or Step to load it.'; });
    kbd.addEventListener('input', function () { dirty = true; stop(); });

    reset();
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-asm', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = L;
})();
