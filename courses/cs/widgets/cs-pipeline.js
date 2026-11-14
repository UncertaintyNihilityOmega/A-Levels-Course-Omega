/* widgets/cs-pipeline.js
   <div class="widget" data-w="cs-pipeline" data-n="6" data-branch="3"></div>
   data-n: the number of instructions, 3 to 10 (default 6). data-branch: 0 for no jump, or the number of an instruction
   (1 to n - 1) that is a taken jump (default 0). A timing diagram of a five-stage pipeline (IF, ID, OF, EX, WB): rows are
   instructions, columns are clock cycles. Switch pipelining on and off, choose a jump, and look at any one cycle.
   Model (the same as cs.hardware2): a jump is settled at the end of its execute stage; the K - 2 = 3 instructions fetched
   behind it are flushed, and the real next instruction is fetched in the cycle after, so a jump costs K - 2 = 3 cycles. */
(function () {
  'use strict';

  const STAGES = ['IF', 'ID', 'OF', 'EX', 'WB'];
  const NAMES = ['IF instruction fetch', 'ID instruction decode', 'OF operand fetch', 'EX instruction execute', 'WB result write back'];
  const K = STAGES.length;
  const MIN_N = 3, MAX_N = 10;

  // ---- pure helpers (tested in Node: data/cs-pipeline.test.js) ----
  function clampN(v) {
    const n = Math.round(Number(v));
    if (!isFinite(n)) return 6;
    return Math.max(MIN_N, Math.min(MAX_N, n));
  }

  // The jump instruction (1 to n - 1), or 0 for none. Anything else becomes 0.
  function clampBranch(v, n) {
    const b = Math.round(Number(v));
    if (!isFinite(b) || b < 1 || b > n - 1) return 0;
    return b;
  }

  // The timing diagram: rows (label, jump flag, flushed flag, cells keyed by cycle number) and the total cycles.
  function layout(n, branch, pipelined) {
    const rows = [];
    let cycles;
    if (!pipelined) {
      for (let i = 1; i <= n; i++) {
        const cells = {};
        for (let s = 0; s < K; s++) cells[K * (i - 1) + s + 1] = STAGES[s];
        rows.push({ label: 'I' + i, jump: i === branch, flushed: false, cells: cells });
      }
      cycles = K * n;
    } else {
      const b = branch;
      const start = function (j) { return b && j > b ? j + (K - 2) : j; };
      for (let j = 1; j <= n; j++) {
        const cells = {};
        for (let s = 0; s < K; s++) cells[start(j) + s] = STAGES[s];
        rows.push({ label: 'I' + j, jump: j === b, flushed: false, cells: cells });
        if (b && j === b) {
          for (let f = 1; f <= K - 2; f++) {
            const fc = {};
            for (let s = 0; s < K - 1 - f; s++) fc[b + f + s] = STAGES[s];
            rows.push({ label: 'wrong ' + f, jump: false, flushed: true, cells: fc });
          }
        }
      }
      cycles = start(n) + K - 1;
    }
    return { rows: rows, cycles: cycles };
  }

  function counts(n, branch) {
    const piped = K + n - 1 + (branch ? K - 2 : 0);
    const seq = K * n;
    return { pipelined: piped, notPipelined: seq, noJump: K + n - 1, penalty: branch ? K - 2 : 0, speedup: seq / piped };
  }

  // Who is in which stage during cycle c.
  function inCycle(lay, c) {
    const out = [];
    lay.rows.forEach(function (r) {
      if (r.cells[c] !== undefined) out.push({ label: r.label, stage: r.cells[c], flushed: r.flushed });
    });
    return out;
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { K: K, STAGES: STAGES, clampN: clampN, clampBranch: clampBranch, layout: layout, counts: counts, inCycle: inCycle };
  }
  if (typeof W === 'undefined' || !W.register) return;

  // ---- the widget ----
  W.register('cs-pipeline', function (el, opts) {
    const f = W.frame(el, 'Pipeline timing diagram', 'Each row is an instruction and each column is a clock cycle');
    const body = f.body;
    opts = opts || {};

    const rawN = opts.n === undefined ? 6 : opts.n;
    let n = clampN(rawN);
    let branch = clampBranch(opts.branch === undefined ? 0 : opts.branch, n);
    let pipelined = true;
    let cycle = 1;

    const problems = [];
    if (opts.n !== undefined && (!isFinite(Number(rawN)) || Math.round(Number(rawN)) !== n)) problems.push('data-n must be a whole number from ' + MIN_N + ' to ' + MAX_N + ', so ' + n + ' is used.');
    if (opts.branch !== undefined && opts.branch !== '' && Number(opts.branch) !== 0 && clampBranch(opts.branch, n) === 0) problems.push('data-branch must be 0 or an instruction from 1 to ' + (n - 1) + ', so no jump is used.');
    if (problems.length) {
      const err = W.h('div', { class: 'w-err', text: problems.join(' ') });
      err.setAttribute('role', 'status');
      body.appendChild(err);
    }

    // controls
    const slider = W.h('input', { type: 'range', min: String(MIN_N), max: String(MAX_N), step: '1' });
    slider.value = String(n);
    slider.setAttribute('aria-label', 'Number of instructions');
    const nOut = W.h('span', { class: 'w-lab', text: String(n) });
    const nCtl = W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Instructions' }), slider, nOut);

    const select = W.h('select', {});
    select.setAttribute('aria-label', 'Which instruction is a jump');
    const selCtl = W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'A taken jump' }), select);

    const tabs = W.h('div', { class: 'w-tabs' });
    tabs.setAttribute('role', 'group');
    tabs.setAttribute('aria-label', 'Pipelined or not pipelined');
    const bPipe = W.h('button', { class: 'w-tab', type: 'button', text: 'Pipelined' });
    const bSeq = W.h('button', { class: 'w-tab', type: 'button', text: 'Not pipelined' });
    tabs.appendChild(bPipe);
    tabs.appendChild(bSeq);

    const cSlider = W.h('input', { type: 'range', min: '1', max: '1', step: '1' });
    cSlider.value = '1';
    cSlider.setAttribute('aria-label', 'Clock cycle to look at');
    const cOut = W.h('span', { class: 'w-lab', text: '1' });
    const cCtl = W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Look at cycle' }), cSlider, cOut);

    body.appendChild(W.h('div', { class: 'w-row' }, nCtl, selCtl));
    body.appendChild(W.h('div', { class: 'w-row' }, tabs, cCtl));

    const grid = W.h('div', { style: { overflowX: 'auto', margin: '6px 0' } });
    body.appendChild(grid);
    const result = W.h('p', { style: { margin: '4px 0' } });
    result.setAttribute('aria-live', 'polite');
    body.appendChild(result);
    const look = W.h('p', { style: { margin: '4px 0' } });
    look.setAttribute('aria-live', 'polite');
    body.appendChild(look);
    body.appendChild(W.h('p', { class: 'w-note', text: 'Key: ' + NAMES.join(', ') + '. In this model a jump is settled at the end of its EX stage, so the three instructions fetched behind it (marked ✗ and "flushed") are thrown away, and a jump costs 3 cycles. Try: switch between pipelined and not pipelined, then choose a jump and compare the totals.' }));

    function fillSelect() {
      select.textContent = '';
      const o0 = W.h('option', { value: '0', text: 'none' });
      select.appendChild(o0);
      for (let i = 1; i <= n - 1; i++) select.appendChild(W.h('option', { value: String(i), text: 'I' + i + ' is a jump' }));
      select.value = String(branch);
    }

    function render() {
      const lay = layout(n, branch, pipelined);
      const c = counts(n, branch);
      if (cycle > lay.cycles) cycle = lay.cycles;
      if (cycle < 1) cycle = 1;
      cSlider.max = String(lay.cycles);
      cSlider.value = String(cycle);
      cOut.textContent = String(cycle);
      nOut.textContent = String(n);
      bPipe.setAttribute('aria-pressed', pipelined ? 'true' : 'false');
      bSeq.setAttribute('aria-pressed', pipelined ? 'false' : 'true');
      bPipe.className = 'w-tab';
      bSeq.className = 'w-tab';

      const table = W.h('table', { style: { borderCollapse: 'collapse', fontSize: '13px', width: 'auto' } });
      table.appendChild(W.h('caption', { text: (pipelined ? 'Pipelined' : 'Not pipelined') + ': ' + lay.cycles + ' clock cycles for ' + n + ' instructions', style: { textAlign: 'left', fontWeight: '600', padding: '2px 0' } }));
      const head = W.h('tr', {}, W.h('th', { text: 'Cycle', scope: 'col', style: { textAlign: 'left', padding: '3px 6px', whiteSpace: 'nowrap' } }));
      for (let k = 1; k <= lay.cycles; k++) {
        head.appendChild(W.h('th', { text: k === cycle ? '[' + k + ']' : String(k), scope: 'col', style: { padding: '3px 4px', textAlign: 'center', minWidth: '42px', fontWeight: k === cycle ? '700' : '400', color: k === cycle ? 'var(--sc)' : 'var(--ink-2)' } }));
      }
      table.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      lay.rows.forEach(function (r) {
        const tr = W.h('tr', {});
        tr.appendChild(W.h('th', { text: r.label + (r.jump ? ' (jump)' : ''), scope: 'row', style: { textAlign: 'left', padding: '3px 6px', whiteSpace: 'nowrap', fontWeight: r.flushed ? '400' : '600', color: r.flushed ? 'var(--ink-3)' : 'var(--ink)' } }));
        for (let k = 1; k <= lay.cycles; k++) {
          const st = r.cells[k];
          const here = k === cycle;
          const style = { padding: '3px 2px', minWidth: '42px', textAlign: 'center', whiteSpace: 'nowrap', border: '1px solid var(--rule)' };
          if (st !== undefined) {
            style.background = r.flushed ? 'transparent' : 'var(--hl-soft)';
            style.fontFamily = 'ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
            if (r.flushed) { style.color = 'var(--red)'; style.borderStyle = 'dashed'; }
          }
          if (here) { style.borderColor = 'var(--sc)'; style.borderWidth = '2px'; }
          tr.appendChild(W.h('td', { text: st === undefined ? '' : (r.flushed ? st + ' ✗' : st), style: style }));
        }
        tb.appendChild(tr);
      });
      table.appendChild(tb);
      grid.textContent = '';
      grid.appendChild(table);

      if (pipelined) {
        result.textContent = 'With a pipeline: ' + K + ' + ' + n + ' − 1 = ' + c.noJump + ' cycles' + (branch ? ', plus ' + c.penalty + ' for the jump = ' + c.pipelined + ' cycles' : '') +
          '. Without: ' + K + ' × ' + n + ' = ' + c.notPipelined + ' cycles. The pipeline is ' + (Math.round(c.speedup * 100) / 100).toFixed(2) + ' times as fast.';
      } else {
        result.textContent = 'Without a pipeline: ' + K + ' × ' + n + ' = ' + c.notPipelined + ' cycles. With a pipeline it would be ' + c.pipelined + ' cycles. Each instruction waits for the one before to finish all ' + K + ' stages.';
      }
      const here = inCycle(lay, cycle);
      look.textContent = 'Cycle ' + cycle + ': ' + (here.length ? here.map(function (x) { return x.label + ' in ' + x.stage + (x.flushed ? ' (flushed)' : ''); }).join(', ') : 'nothing') + '.';
    }

    slider.addEventListener('input', function () {
      n = clampN(slider.value);
      branch = clampBranch(branch, n);
      fillSelect();
      render();
    });
    select.addEventListener('change', function () {
      branch = clampBranch(select.value, n);
      render();
    });
    bPipe.addEventListener('click', function () { pipelined = true; render(); });
    bSeq.addEventListener('click', function () { pipelined = false; render(); });
    cSlider.addEventListener('input', function () {
      cycle = Math.max(1, Math.round(Number(cSlider.value)) || 1);
      render();
    });

    fillSelect();
    cycle = Math.min(4, K + n - 1);
    render();
  });
})();
