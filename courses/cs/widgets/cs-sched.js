/* widgets/cs-sched.js: CPU scheduling: FCFS, SJF (non-pre-emptive), SRT and round robin on up to 6 processes.
   <div class="widget" data-w="cs-sched" data-algo="rr" data-q="2" data-procs="A:0:5,B:1:3,C:2:8,D:3:2"></div>
   data-algo: fcfs, sjf, srt or rr. data-q: quantum 1 to 5. data-procs: name:arrival:burst, comma separated.
   The logic (object S) is pure, matches data/cs_sched_model.py and is exported for data/cs-sched.test.js.
   Rules (shown under the widget): ties are broken by earlier arrival, then by name; SRT pre-empts only when the new
   process needs strictly less time than the running one has left; in RR a process arriving while another runs, or at the
   moment a slice ends, joins the queue before the pre-empted process; the CPU idles when nothing has arrived. */
(function () {
  'use strict';

  const S = {};
  S.MAX = 6;
  S.ALGOS = [['fcfs', 'First come first served'], ['sjf', 'Shortest job first'], ['srt', 'Shortest remaining time'], ['rr', 'Round robin']];

  S.merge = function (segs) {
    const out = [];
    segs.forEach(function (s) {
      const last = out[out.length - 1];
      if (last && last[0] === s[0] && last[2] === s[1]) last[2] = s[2];
      else out.push([s[0], s[1], s[2]]);
    });
    return out;
  };

  // procs: [[name, arrival, burst]]. Returns [[name or null, start, end]].
  S.schedule = function (procs, algo, q) {
    const order = procs.map(function (p) { return [p[0], p[1], p[2]]; })
      .sort(function (a, b) { return a[1] - b[1] || (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0); });
    const rem = {};
    const arr = {};
    procs.forEach(function (p) { rem[p[0]] = p[2]; arr[p[0]] = p[1]; });
    const segs = [];
    let t = 0;
    const cmpName = function (a, b) { return a < b ? -1 : a > b ? 1 : 0; };
    if (algo === 'fcfs') {
      order.forEach(function (p) {
        if (t < p[1]) { segs.push([null, t, p[1]]); t = p[1]; }
        segs.push([p[0], t, t + p[2]]);
        t += p[2];
      });
    } else if (algo === 'sjf') {
      let left = order.slice();
      while (left.length) {
        const ready = left.filter(function (p) { return p[1] <= t; });
        if (!ready.length) {
          const nxt = Math.min.apply(null, left.map(function (p) { return p[1]; }));
          segs.push([null, t, nxt]);
          t = nxt;
          continue;
        }
        ready.sort(function (a, b) { return a[2] - b[2] || a[1] - b[1] || cmpName(a[0], b[0]); });
        const p = ready[0];
        segs.push([p[0], t, t + p[2]]);
        t += p[2];
        left = left.filter(function (x) { return x !== p; });
      }
    } else if (algo === 'srt') {
      let current = null;
      const names = Object.keys(rem);
      const total = function () { return names.reduce(function (s, k) { return s + rem[k]; }, 0); };
      while (total() > 0) {
        const ready = names.filter(function (k) { return rem[k] > 0 && arr[k] <= t; });
        if (!ready.length) {
          const nxt = Math.min.apply(null, names.filter(function (k) { return rem[k] > 0; }).map(function (k) { return arr[k]; }));
          segs.push([null, t, nxt]);
          t = nxt;
          current = null;
          continue;
        }
        ready.sort(function (a, b) {
          return rem[a] - rem[b] || ((a === current ? 0 : 1) - (b === current ? 0 : 1)) || arr[a] - arr[b] || cmpName(a, b);
        });
        const n = ready[0];
        segs.push([n, t, t + 1]);
        rem[n] -= 1;
        t += 1;
        current = rem[n] > 0 ? n : null;
      }
    } else {
      const queue = [];
      const pending = order.slice();
      const admit = function (upto) {
        while (pending.length && pending[0][1] <= upto) queue.push(pending.shift()[0]);
      };
      while (pending.length || queue.length) {
        admit(t);
        if (!queue.length) {
          const nxt = pending[0][1];
          segs.push([null, t, nxt]);
          t = nxt;
          continue;
        }
        const n = queue.shift();
        const run = Math.min(q, rem[n]);
        segs.push([n, t, t + run]);
        t += run;
        rem[n] -= run;
        admit(t);
        if (rem[n] > 0) queue.push(n);
      }
    }
    return S.merge(segs);
  };

  S.gcd = function (a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { const r = a % b; a = b; b = r; } return a || 1; };
  S.frac = function (num, den) { const g = S.gcd(num, den); return [num / g, den / g]; };

  S.stats = function (procs, segs) {
    const done = {};
    segs.forEach(function (s) { if (s[0] !== null) done[s[0]] = s[2]; });
    const rows = {};
    let sumT = 0;
    let sumW = 0;
    procs.forEach(function (p) {
      const c = done[p[0]];
      rows[p[0]] = [c, c - p[1], c - p[1] - p[2]];
      sumT += c - p[1];
      sumW += c - p[1] - p[2];
    });
    return { rows: rows, avgT: S.frac(sumT, procs.length), avgW: S.frac(sumW, procs.length) };
  };

  S.switches = function (segs) {
    const runs = segs.filter(function (s) { return s[0] !== null; }).map(function (s) { return s[0]; });
    let n = 0;
    for (let i = 1; i < runs.length; i++) if (runs[i] !== runs[i - 1]) n++;
    return n;
  };

  // "5.75 (23/4)": the exact fraction beside the value to two decimal places.
  S.showFrac = function (f) {
    if (f[1] === 1) return String(f[0]);
    const v = Math.round(f[0] * 100 / f[1]) / 100;
    const exact = Math.round(f[0] * 100) % f[1] === 0;
    return (exact ? '' : '≈ ') + v.toFixed(2).replace(/0$/, '').replace(/\.$/, '') + ' (' + f[0] + '/' + f[1] + ')';
  };

  // "A:0:5,B:1:3" -> {procs} or {error}
  S.parseProcs = function (text) {
    const s = String(text == null ? '' : text).trim();
    if (!s) return { error: 'Type processes as name:arrival:burst, for example A:0:5,B:1:3.' };
    const parts = s.split(',');
    if (parts.length > S.MAX) return { error: 'At most ' + S.MAX + ' processes.' };
    const procs = [];
    for (let i = 0; i < parts.length; i++) {
      const f = parts[i].trim().split(':');
      if (f.length !== 3 || !/^[A-Za-z0-9]{1,3}$/.test(f[0].trim()) || !/^\d{1,2}$/.test(f[1].trim()) || !/^\d{1,2}$/.test(f[2].trim()) || parseInt(f[2], 10) < 1) {
        return { error: '"' + parts[i].trim() + '" is not name:arrival:burst with a burst of at least 1.' };
      }
      const name = f[0].trim();
      if (procs.some(function (p) { return p[0] === name; })) return { error: 'The name ' + name + ' is used twice.' };
      procs.push([name, parseInt(f[1], 10), parseInt(f[2], 10)]);
    }
    return { procs: procs };
  };

  function init(el, opts) {
    opts = opts || {};
    const frame = W.frame(el, 'CPU scheduling', 'Change the processes or the algorithm and watch the Gantt chart');
    const body = frame.body;
    let algo = ['fcfs', 'sjf', 'srt', 'rr'].indexOf(String(opts.algo || '').toLowerCase()) >= 0 ? String(opts.algo).toLowerCase() : 'rr';
    let q = parseInt(opts.q, 10);
    if (!(q >= 1 && q <= 5)) q = 2;
    const parsed = S.parseProcs(opts.procs == null || String(opts.procs).trim() === '' ? 'A:0:5,B:1:3,C:2:8,D:3:2' : opts.procs);
    let procs = parsed.procs || [['A', 0, 5], ['B', 1, 3], ['C', 2, 8], ['D', 3, 2]];

    const tabs = W.h('div', { 'class': 'w-tabs' });
    tabs.setAttribute('role', 'group');
    tabs.setAttribute('aria-label', 'Scheduling algorithm');
    const algoBtn = {};
    S.ALGOS.forEach(function (a) {
      const b = W.h('button', { 'class': 'w-tab', type: 'button', text: a[0].toUpperCase() });
      b.setAttribute('aria-label', a[1]);
      b.addEventListener('click', function () { algo = a[0]; paintAlgo(); update(); });
      algoBtn[a[0]] = b;
      tabs.appendChild(b);
    });
    body.appendChild(tabs);
    const algoName = W.h('div', { 'class': 'w-note', 'aria-live': 'polite' });
    body.appendChild(algoName);

    const qSel = W.h('select', {});
    [1, 2, 3, 4, 5].forEach(function (v) { qSel.appendChild(W.h('option', { value: String(v), text: String(v) })); });
    qSel.value = String(q);
    qSel.addEventListener('change', function () { q = parseInt(qSel.value, 10); update(); });
    const qCtl = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Time quantum (time units)' }), qSel);
    body.appendChild(qCtl);

    const tableWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0' } });
    body.appendChild(tableWrap);
    const addBtn = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Add a process' });
    body.appendChild(W.h('div', { 'class': 'w-row' }, addBtn));
    const err = W.h('div', { 'class': 'w-err', 'aria-live': 'polite' });
    err.style.display = 'none';
    body.appendChild(err);
    const ganttWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0', margin: '8px 0 4px' } });
    body.appendChild(ganttWrap);
    const resWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0' } });
    body.appendChild(resWrap);
    const summary = W.h('div', { 'aria-live': 'polite', style: { fontWeight: '700', margin: '4px 0' } });
    body.appendChild(summary);
    body.appendChild(W.h('div', { 'class': 'w-note', text: 'Rules used here: only CPU time is modelled (no waiting for input or output). Ties are broken by earlier arrival, then by name. In SRT a new process pre-empts the running one only if it needs strictly less time than the running one has left. In round robin a process that arrives while another is running, or at the moment a slice ends, joins the queue before the pre-empted process. Turnaround time = completion time − arrival time. Waiting time = turnaround time − burst time.' }));

    const inputs = [];

    function nextName() {
      const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      for (let i = 0; i < letters.length; i++) if (!procs.some(function (p) { return p[0] === letters[i]; })) return letters[i];
      return 'Z';
    }

    function buildTable() {
      tableWrap.textContent = '';
      inputs.length = 0;
      const t = W.h('table', {});
      const head = W.h('tr', {});
      ['Process', 'Arrival time', 'Burst time', ''].forEach(function (h) { head.appendChild(W.h('th', { text: h, scope: 'col' })); });
      t.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      procs.forEach(function (p, i) {
        const nameIn = W.h('input', { type: 'text', value: p[0] });
        nameIn.setAttribute('aria-label', 'Name of process ' + (i + 1));
        nameIn.setAttribute('maxlength', '3');
        nameIn.style.width = '4em';
        const arrIn = W.h('input', { type: 'number', value: String(p[1]) });
        arrIn.setAttribute('aria-label', 'Arrival time of ' + p[0]);
        arrIn.setAttribute('min', '0');
        arrIn.setAttribute('max', '99');
        arrIn.style.width = '5em';
        const burIn = W.h('input', { type: 'number', value: String(p[2]) });
        burIn.setAttribute('aria-label', 'Burst time of ' + p[0]);
        burIn.setAttribute('min', '1');
        burIn.setAttribute('max', '99');
        burIn.style.width = '5em';
        [nameIn, arrIn, burIn].forEach(function (inp) { inp.addEventListener('input', function () { readInputs(); }); });
        const rm = W.h('button', { 'class': 'btn btn-sec btn-sm', type: 'button', text: 'Remove' });
        rm.setAttribute('aria-label', 'Remove process ' + p[0]);
        if (procs.length <= 1) rm.disabled = true;
        rm.addEventListener('click', function () {
          procs.splice(i, 1);
          buildTable();
          update();
          const first = tableWrap.querySelector('input');
          if (first) first.focus();
        });
        inputs.push([nameIn, arrIn, burIn]);
        tb.appendChild(W.h('tr', {}, W.h('td', {}, nameIn), W.h('td', {}, arrIn), W.h('td', {}, burIn), W.h('td', {}, rm)));
      });
      t.appendChild(tb);
      tableWrap.appendChild(t);
      addBtn.disabled = procs.length >= S.MAX;
    }

    function readInputs() {
      const next = [];
      for (let i = 0; i < inputs.length; i++) {
        const name = inputs[i][0].value.trim();
        const a = inputs[i][1].value.trim();
        const b = inputs[i][2].value.trim();
        if (!/^[A-Za-z0-9]{1,3}$/.test(name)) return fail('Process ' + (i + 1) + ' needs a name of 1 to 3 letters or digits.');
        if (next.some(function (p) { return p[0] === name; })) return fail('The name ' + name + ' is used twice.');
        if (!/^\d{1,2}$/.test(a)) return fail('The arrival time of ' + name + ' must be a whole number from 0 to 99.');
        if (!/^\d{1,2}$/.test(b) || parseInt(b, 10) < 1) return fail('The burst time of ' + name + ' must be a whole number from 1 to 99.');
        next.push([name, parseInt(a, 10), parseInt(b, 10)]);
      }
      err.textContent = '';
      err.style.display = 'none';
      procs = next;
      update();
      return true;
    }
    function fail(msg) {
      err.textContent = msg + ' The chart shows the last valid processes.';
      err.style.display = '';
      return false;
    }

    function paintAlgo() {
      S.ALGOS.forEach(function (a) { algoBtn[a[0]].setAttribute('aria-pressed', a[0] === algo ? 'true' : 'false'); });
      qCtl.style.display = algo === 'rr' ? '' : 'none';
      const name = S.ALGOS.filter(function (a) { return a[0] === algo; })[0][1];
      algoName.textContent = name + (algo === 'rr' ? ' with a quantum of ' + q : algo === 'srt' ? ' (pre-emptive)' : ' (non-pre-emptive)') + '.';
    }

    function update() {
      paintAlgo();
      if (!procs.length) return;
      const segs = S.schedule(procs, algo, q);
      const st = S.stats(procs, segs);
      paintGantt(segs);
      paintResults(st, segs);
    }

    function paintGantt(segs) {
      ganttWrap.textContent = '';
      const total = segs.length ? segs[segs.length - 1][2] : 0;
      if (!(total > 0)) return;
      const unit = Math.max(10, Math.min(34, Math.floor(560 / total)));
      const width = total * unit;
      const box = W.h('div', { style: { position: 'relative', width: width + 'px', height: '64px', margin: '2px 14px 0' } });
      let lastLabel = -100;
      const labels = [];
      const times = segs.map(function (s) { return s[1]; });
      segs.forEach(function (s) {
        const idle = s[0] === null;
        const bar = W.h('div', { text: idle ? (s[2] - s[1] >= 2 ? 'idle' : '') : s[0], style: {
          position: 'absolute', left: (s[1] * unit) + 'px', width: ((s[2] - s[1]) * unit) + 'px', top: '0', height: '36px', boxSizing: 'border-box',
          display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', fontWeight: '700', fontSize: '0.9em',
          border: idle ? '1px dashed var(--ink-3)' : '2px solid var(--sc)', background: idle ? 'transparent' : 'var(--card)', color: idle ? 'var(--ink-2)' : 'var(--ink)'
        } });
        box.appendChild(bar);
      });
      times.forEach(function (tm) { if (tm * unit - lastLabel >= 18 && (total - tm) * unit >= 18) { labels.push(tm); lastLabel = tm * unit; } });
      labels.push(total);
      labels.forEach(function (tm) {
        box.appendChild(W.h('div', { text: String(tm), style: { position: 'absolute', left: (tm * unit - 10) + 'px', width: '20px', textAlign: 'center', top: '40px', fontSize: '0.8em', color: 'var(--ink-2)' } }));
      });
      ganttWrap.appendChild(W.h('div', { 'class': 'w-note', text: 'Gantt chart (time units along the bottom)' }));
      ganttWrap.appendChild(box);
      const spoken = segs.map(function (s) { return (s[0] === null ? 'idle' : s[0]) + ' from ' + s[1] + ' to ' + s[2]; }).join('; ');
      box.setAttribute('role', 'img');
      box.setAttribute('aria-label', 'Gantt chart: ' + spoken + '.');
    }

    function paintResults(st, segs) {
      resWrap.textContent = '';
      const t = W.h('table', {});
      const head = W.h('tr', {});
      ['Process', 'Arrival', 'Burst', 'Completion', 'Turnaround', 'Waiting'].forEach(function (h) { head.appendChild(W.h('th', { text: h, scope: 'col' })); });
      t.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      procs.forEach(function (p) {
        const r = st.rows[p[0]];
        tb.appendChild(W.h('tr', {}, W.h('td', { text: p[0] }), W.h('td', { text: String(p[1]) }), W.h('td', { text: String(p[2]) }), W.h('td', { text: String(r[0]) }), W.h('td', { text: String(r[1]) }), W.h('td', { text: String(r[2]) })));
      });
      tb.appendChild(W.h('tr', { style: { fontWeight: '700' } }, W.h('td', { text: 'Average' }), W.h('td', {}), W.h('td', {}), W.h('td', {}), W.h('td', { text: S.showFrac(st.avgT) }), W.h('td', { text: S.showFrac(st.avgW) })));
      t.appendChild(tb);
      resWrap.appendChild(t);
      summary.textContent = 'Average waiting time ' + S.showFrac(st.avgW) + '. Average turnaround time ' + S.showFrac(st.avgT) + '. Context switches: ' + S.switches(segs) + '.';
    }

    addBtn.addEventListener('click', function () {
      if (procs.length >= S.MAX) return;
      procs.push([nextName(), 0, 3]);
      buildTable();
      update();
      const rows = tableWrap.querySelectorAll('tbody tr');
      const lastRow = rows[rows.length - 1];
      const f = lastRow && lastRow.querySelector('input');
      if (f) f.focus();
    });

    buildTable();
    update();
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-sched', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = S;
})();
