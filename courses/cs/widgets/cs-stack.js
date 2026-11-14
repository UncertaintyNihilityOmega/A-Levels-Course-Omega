/* widgets/cs-stack.js: stacks, queues, circular queues and linked lists stored in arrays.
   <div class="widget" data-w="cs-stack" data-type="stack" data-size="8" data-base="1" data-items="12,7,30"></div>
   data-type: stack, queue, circular or list (the tab shown first). data-size: 3 to 12 elements (default 8).
   data-base: 0 or 1, the first array index (default 1). data-items: comma-separated values put in the starting
   structure (stack: pushed in order, queue: enqueued, list: inserted in order).
   The structures (object S) are pure, follow the course's pseudocode exactly, and are exported for a Node test
   (data/cs-stack.test.js, which compares them with a Python model). Operations never throw: a full, empty or
   missing case returns {ok: false, kind, msg}. */
(function () {
  'use strict';

  // ---------------------------------------------------------------------------------------------
  // Pure model
  // ---------------------------------------------------------------------------------------------
  const S = {};
  S.TYPES = ['stack', 'queue', 'circular', 'list'];
  S.NAMES = { stack: 'Stack', queue: 'Queue', circular: 'Circular queue', list: 'Linked list' };
  S.DEFAULTS = {
    stack: ['12', '7', '30'],
    queue: ['J1', 'J2', 'J3'],
    circular: ['J1', 'J2', 'J3'],
    list: ['Dina', 'Farah', 'Bilal']
  };
  S.MAXLEN = 12;

  S.size = function (v) {
    const n = parseInt(v, 10);
    if (!isFinite(n)) return 8;
    return Math.max(3, Math.min(12, n));
  };
  S.baseOf = function (v) { return String(v).trim() === '0' ? 0 : 1; };
  S.typeOf = function (v) {
    const t = String(v == null ? '' : v).trim().toLowerCase();
    return S.TYPES.indexOf(t) >= 0 ? t : 'stack';
  };
  S.items = function (text) {
    if (text == null) return [];
    return String(text).split(',').map(function (s) { return s.replace(/\s+/g, ' ').trim(); })
      .filter(function (s) { return s !== ''; })
      .map(function (s) { return s.slice(0, S.MAXLEN); });
  };
  // Returns {value} or {error}
  S.check = function (text) {
    const s = String(text == null ? '' : text).replace(/\s+/g, ' ').trim();
    if (s === '') return { error: 'Type a value first (a number or a short word).' };
    if (s.length > S.MAXLEN) return { error: 'Use at most ' + S.MAXLEN + ' characters.' };
    return { value: s };
  };

  S.make = function (type, size, base) {
    const nil = base - 1;
    const st = { type: type, size: size, base: base, data: [] };
    for (let i = 0; i < size; i++) st.data.push('');
    if (type === 'stack') {
      st.top = nil;
    } else if (type === 'queue') {
      st.front = base; st.rear = nil;
    } else if (type === 'circular') {
      st.front = base; st.rear = nil; st.count = 0;
    } else {
      st.ptr = [];
      for (let i = 0; i < size; i++) st.ptr.push(i < size - 1 ? base + i + 1 : nil);
      st.start = nil; st.free = base;
    }
    return st;
  };
  S.last = function (st) { return st.base + st.size - 1; };
  S.inRange = function (st, idx) { return idx >= st.base && idx <= S.last(st); };

  function res(ok, kind, value, msg, extra) {
    const r = { ok: ok, kind: kind, value: value, msg: msg };
    if (extra) for (const k in extra) r[k] = extra[k];
    return r;
  }

  // ----- stack
  S.push = function (st, v) {
    if (st.top === S.last(st)) return res(false, 'overflow', null, 'Stack overflow: the stack is full (TopPointer = ' + st.top + ', the last index), so ' + v + ' was not stored.');
    st.top += 1;
    st.data[st.top - st.base] = v;
    return res(true, 'ok', st.top, 'Pushed ' + v + ' at index ' + st.top + '; TopPointer = ' + st.top + '.');
  };
  S.pop = function (st) {
    if (st.top === st.base - 1) return res(false, 'underflow', null, 'Stack underflow: the stack is empty (TopPointer = ' + st.top + '), so there is nothing to pop.');
    const old = st.top;
    const v = st.data[old - st.base];
    st.top -= 1;
    return res(true, 'ok', v, 'Popped ' + v + ' from index ' + old + '; TopPointer = ' + st.top + '. The value stays in the array until a push writes over it.');
  };
  S.peek = function (st) {
    if (st.top === st.base - 1) return res(false, 'underflow', null, 'Stack empty: there is no top item to peek at (TopPointer = ' + st.top + ').');
    const v = st.data[st.top - st.base];
    return res(true, 'ok', v, 'Peek: the top item is ' + v + ' at index ' + st.top + '. TopPointer is unchanged (' + st.top + ').');
  };

  // ----- linear queue
  S.enqueue = function (st, v) {
    if (st.type === 'circular') {
      if (st.count === st.size) return res(false, 'full', null, 'Queue full: Count = ' + st.count + ', every element is in use, so ' + v + ' was not stored.');
      st.rear = (st.rear - st.base + 1) % st.size + st.base;
      st.data[st.rear - st.base] = v;
      st.count += 1;
      return res(true, 'ok', st.rear, 'Enqueued ' + v + ' at index ' + st.rear + '; RearPointer = ' + st.rear + ', Count = ' + st.count + '.');
    }
    if (st.rear === S.last(st)) {
      const freeFront = st.front - st.base;
      return res(false, 'full', null, 'Queue full: RearPointer = ' + st.rear + ' is the last index, so ' + v + ' was not stored' +
        (freeFront > 0 ? ' (the ' + freeFront + ' place' + (freeFront === 1 ? '' : 's') + ' before FrontPointer cannot be reused: that is the weakness of a linear queue).' : '.'));
    }
    st.rear += 1;
    st.data[st.rear - st.base] = v;
    return res(true, 'ok', st.rear, 'Enqueued ' + v + ' at index ' + st.rear + '; RearPointer = ' + st.rear + '.');
  };
  S.dequeue = function (st) {
    if (st.type === 'circular') {
      if (st.count === 0) return res(false, 'empty', null, 'Queue empty: Count = 0, so there is nothing to dequeue.');
      const old = st.front;
      const v = st.data[old - st.base];
      st.front = (st.front - st.base + 1) % st.size + st.base;
      st.count -= 1;
      return res(true, 'ok', v, 'Dequeued ' + v + ' from index ' + old + '; FrontPointer = ' + st.front + ', Count = ' + st.count + '.');
    }
    if (st.front > st.rear) return res(false, 'empty', null, 'Queue empty: FrontPointer (' + st.front + ') is past RearPointer (' + st.rear + '), so there is nothing to dequeue.');
    const old = st.front;
    const v = st.data[old - st.base];
    st.front += 1;
    return res(true, 'ok', v, 'Dequeued ' + v + ' from index ' + old + '; FrontPointer = ' + st.front + '.');
  };

  // ----- linked list
  const NUM = /^-?\d+(\.\d+)?$/;
  S.less = function (a, b) {
    if (NUM.test(a) && NUM.test(b)) return Number(a) < Number(b);
    return a < b;
  };
  S.nodes = function (st) {
    const out = [];
    const nil = st.base - 1;
    let cur = st.start;
    let guard = 0;
    while (cur !== nil && S.inRange(st, cur) && guard <= st.size) {
      out.push(cur);
      cur = st.ptr[cur - st.base];
      guard += 1;
    }
    return out;
  };
  S.insert = function (st, v) {
    const b = st.base;
    const nil = b - 1;
    if (st.free === nil) return res(false, 'full', null, 'List full: FreePointer = ' + nil + ' (the null pointer), so there is no free node for ' + v + '.');
    const node = st.free;
    st.free = st.ptr[node - b];
    st.data[node - b] = v;
    let prev = nil;
    let cur = st.start;
    while (cur !== nil && S.less(st.data[cur - b], v)) { prev = cur; cur = st.ptr[cur - b]; }
    st.ptr[node - b] = cur;
    let where;
    if (prev === nil) {
      st.start = node;
      where = 'at the front of the list; StartPointer = ' + node;
    } else {
      st.ptr[prev - b] = node;
      where = 'after ' + st.data[prev - b] + ' (index ' + prev + '); Pointer[' + prev + '] = ' + node;
    }
    const next = cur === nil ? 'null (' + nil + ')' : cur + ' (' + st.data[cur - b] + ')';
    return res(true, 'ok', node, 'Inserted ' + v + ' at index ' + node + ' ' + where + '. Pointer[' + node + '] = ' + next + '; FreePointer = ' + st.free + '.');
  };
  S.remove = function (st, v) {
    const b = st.base;
    const nil = b - 1;
    let prev = nil;
    let cur = st.start;
    while (cur !== nil && st.data[cur - b] !== v) { prev = cur; cur = st.ptr[cur - b]; }
    if (cur === nil) return res(false, 'notfound', null, v + ' is not in the list, so nothing was deleted.');
    const next = st.ptr[cur - b];
    let how;
    if (prev === nil) {
      st.start = next;
      how = 'StartPointer = ' + next;
    } else {
      st.ptr[prev - b] = next;
      how = 'Pointer[' + prev + '] = ' + next + ', so it skips the deleted node';
    }
    st.ptr[cur - b] = st.free;
    st.free = cur;
    return res(true, 'ok', cur, 'Deleted ' + v + ' from index ' + cur + '; ' + how + '. The node joins the free list: FreePointer = ' + cur + '.');
  };
  S.find = function (st, v) {
    const b = st.base;
    const nil = b - 1;
    if (st.start === nil) return res(false, 'notfound', null, 'The list is empty (StartPointer = ' + nil + '), so ' + v + ' is not there.', { visits: 0 });
    let cur = st.start;
    const seen = [];
    let guard = 0;
    while (cur !== nil && guard <= st.size) {
      seen.push(st.data[cur - b] + ' (' + cur + ')');
      if (st.data[cur - b] === v) {
        return res(true, 'found', cur, 'Found ' + v + ' at index ' + cur + ' after visiting ' + seen.length + ' node' + (seen.length === 1 ? '' : 's') + ': ' + seen.join(', ') + '.', { visits: seen.length });
      }
      cur = st.ptr[cur - b];
      guard += 1;
    }
    return res(false, 'notfound', null, v + ' is not in the list: all ' + seen.length + ' node' + (seen.length === 1 ? ' was' : 's were') + ' visited (' + seen.join(', ') + ') and the null pointer was reached.', { visits: seen.length });
  };

  // Which array slots are part of the structure? Returns a boolean array indexed by slot.
  S.live = function (st) {
    const live = [];
    for (let i = 0; i < st.size; i++) live.push(false);
    if (st.type === 'stack') {
      for (let idx = st.base; idx <= st.top; idx++) live[idx - st.base] = true;
    } else if (st.type === 'queue') {
      for (let idx = st.front; idx <= st.rear; idx++) if (S.inRange(st, idx)) live[idx - st.base] = true;
    } else if (st.type === 'circular') {
      for (let k = 0; k < st.count; k++) live[(st.front - st.base + k) % st.size] = true;
    } else {
      S.nodes(st).forEach(function (idx) { live[idx - st.base] = true; });
    }
    return live;
  };
  // Items in order (front first / top first / list order), as strings
  S.order = function (st) {
    const live = S.live(st);
    if (st.type === 'stack') {
      const out = [];
      for (let i = st.size - 1; i >= 0; i--) if (live[i]) out.push(st.data[i]);
      return out;
    }
    if (st.type === 'queue') {
      const out = [];
      for (let idx = st.front; idx <= st.rear; idx++) if (S.inRange(st, idx)) out.push(st.data[idx - st.base]);
      return out;
    }
    if (st.type === 'circular') {
      const out = [];
      for (let k = 0; k < st.count; k++) out.push(st.data[(st.front - st.base + k) % st.size]);
      return out;
    }
    return S.nodes(st).map(function (idx) { return st.data[idx - st.base]; });
  };
  S.markers = function (st) {
    const m = [];
    for (let i = 0; i < st.size; i++) m.push([]);
    function put(idx, text) { if (S.inRange(st, idx)) m[idx - st.base].push(text); }
    if (st.type === 'stack') put(st.top, 'Top');
    else if (st.type === 'queue' || st.type === 'circular') { put(st.front, 'Front'); put(st.rear, 'Rear'); }
    else { put(st.start, 'Start'); put(st.free, 'Free'); }
    return m;
  };
  S.summary = function (st) {
    const nil = st.base - 1;
    if (st.type === 'stack') return 'TopPointer = ' + st.top + ' (' + nil + ' means empty)';
    if (st.type === 'queue') return 'FrontPointer = ' + st.front + ', RearPointer = ' + st.rear + ' (the queue is empty when FrontPointer > RearPointer)';
    if (st.type === 'circular') return 'FrontPointer = ' + st.front + ', RearPointer = ' + st.rear + ', Count = ' + st.count + ' of ' + st.size;
    return 'StartPointer = ' + st.start + ', FreePointer = ' + st.free + ' (' + nil + ' is the null pointer)';
  };

  S.build = function (type, size, base, items) {
    const st = S.make(type, size, base);
    items.forEach(function (v) {
      if (type === 'stack') S.push(st, v);
      else if (type === 'queue' || type === 'circular') S.enqueue(st, v);
      else S.insert(st, v);
    });
    return st;
  };

  // ---------------------------------------------------------------------------------------------
  // Widget
  // ---------------------------------------------------------------------------------------------
  function init(el, opts) {
    opts = opts || {};
    const size = S.size(opts.size);
    const base = S.baseOf(opts.base);
    const first = S.typeOf(opts.type);
    const given = S.items(opts.items);
    const states = {};
    S.TYPES.forEach(function (t) {
      const items = t === first && given.length ? given : S.DEFAULTS[t];
      states[t] = S.build(t, size, base, items.slice(0, size));
    });
    let tab = first;

    const frame = W.frame(el, 'Stacks, queues and linked lists', 'The structures are stored in arrays, as in the exam');
    const body = frame.body;

    const tabsEl = W.h('div', { 'class': 'w-tabs', role: 'group', 'aria-label': 'Choose a structure' });
    const tabBtns = {};
    S.TYPES.forEach(function (t) {
      const b = W.h('button', { type: 'button', 'class': 'w-tab', text: S.NAMES[t] });
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () { setTab(t, true); });
      tabBtns[t] = b;
      tabsEl.appendChild(b);
    });

    const input = W.h('input', { type: 'text' });
    input.setAttribute('autocomplete', 'off');
    input.setAttribute('spellcheck', 'false');
    input.setAttribute('maxlength', String(S.MAXLEN + 4));
    input.style.maxWidth = '100%';
    const inputLab = W.h('label', { 'class': 'w-ctl' }, W.h('span', { 'class': 'w-lab', text: 'Value (a number or a short word)' }), input);
    const buttons = W.h('div', { 'class': 'w-row', style: { alignItems: 'center' } });
    const controls = W.h('div', { 'class': 'w-row', style: { alignItems: 'flex-end' } }, inputLab, buttons);
    const msg = W.h('div', { 'class': 'w-note', 'aria-live': 'polite', style: { minHeight: '2.6em' } });
    const summary = W.h('div', { 'class': 'w-note', style: { fontWeight: '700' } });
    const orderLine = W.h('div', { 'class': 'w-note' });
    const tableWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%', minWidth: '0' } });
    const hint = W.h('div', { 'class': 'w-note' });

    body.appendChild(tabsEl);
    body.appendChild(controls);
    body.appendChild(msg);
    body.appendChild(summary);
    body.appendChild(tableWrap);
    body.appendChild(orderLine);
    body.appendChild(hint);

    function say(text, isError) {
      msg.textContent = text;
      msg.className = isError ? 'w-err' : 'w-note';
      msg.style.minHeight = '2.6em';
    }

    function paint() {
      const st = states[tab];
      const live = S.live(st);
      const marks = S.markers(st);
      const isList = st.type === 'list';
      tableWrap.textContent = '';
      const t = W.h('table', {});
      t.appendChild(W.h('caption', { 'class': 'sr-only', text: S.NAMES[tab] + ' stored in an array of ' + st.size + ' elements. ' + S.summary(st) + '.' }));
      const head = W.h('tr', {});
      head.appendChild(W.h('th', { text: 'Index', scope: 'col' }));
      head.appendChild(W.h('th', { text: 'Data', scope: 'col' }));
      if (isList) head.appendChild(W.h('th', { text: 'Pointer', scope: 'col' }));
      head.appendChild(W.h('th', { text: isList ? 'Start / Free' : 'Pointers', scope: 'col' }));
      t.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody', {});
      for (let i = 0; i < st.size; i++) {
        const raw = st.data[i];
        const shown = raw === '' ? '' : (live[i] ? raw : '(' + raw + ')');
        const tr = W.h('tr', {});
        tr.appendChild(W.h('td', { text: String(st.base + i) }));
        const td = W.h('td', { text: shown });
        if (live[i]) td.style.fontWeight = '700';
        else if (shown !== '') td.style.fontStyle = 'italic';
        tr.appendChild(td);
        if (isList) tr.appendChild(W.h('td', { text: String(st.ptr[i]) }));
        tr.appendChild(W.h('td', { text: marks[i].length ? '← ' + marks[i].join(', ') : '' }));
        tb.appendChild(tr);
      }
      t.appendChild(tb);
      tableWrap.appendChild(t);
      summary.textContent = S.summary(st);
      const order = S.order(st);
      const label = st.type === 'stack' ? 'Items, top first: ' : st.type === 'list' ? 'List in order: ' : 'Items, front first: ';
      orderLine.textContent = label + (order.length ? order.join(st.type === 'list' ? ' → ' : ', ') : '(none)');
    }

    function btn(label, primary, fn) {
      const b = W.h('button', { type: 'button', 'class': primary ? 'btn btn-sm' : 'btn btn-sec btn-sm', text: label });
      b.addEventListener('click', fn);
      return b;
    }

    function withValue(op) {
      return function () {
        const c = S.check(input.value);
        if (c.error) { say(c.error, true); input.focus(); return; }
        const r = op(states[tab], c.value);
        say(r.msg, !r.ok);
        if (r.ok) input.value = '';
        paint();
        input.focus();
      };
    }
    function noValue(op) {
      return function () {
        const r = op(states[tab]);
        say(r.msg, !r.ok);
        paint();
      };
    }
    function reset() {
      states[tab] = S.build(tab, size, base, S.DEFAULTS[tab].slice(0, size));
      say('Reset to the starting example.', false);
      paint();
    }
    function clearAll() {
      states[tab] = S.make(tab, size, base);
      say('Emptied: every element is free again.', false);
      paint();
    }

    let primary = null;
    function setButtons() {
      buttons.textContent = '';
      if (tab === 'stack') {
        primary = withValue(S.push);
        buttons.appendChild(btn('Push', true, primary));
        buttons.appendChild(btn('Pop', false, noValue(S.pop)));
        buttons.appendChild(btn('Peek', false, noValue(S.peek)));
      } else if (tab === 'queue' || tab === 'circular') {
        primary = withValue(S.enqueue);
        buttons.appendChild(btn('Enqueue', true, primary));
        buttons.appendChild(btn('Dequeue', false, noValue(S.dequeue)));
      } else {
        primary = withValue(S.insert);
        buttons.appendChild(btn('Insert in order', true, primary));
        buttons.appendChild(btn('Delete', false, withValue(S.remove)));
        buttons.appendChild(btn('Find', false, withValue(S.find)));
      }
      buttons.appendChild(btn('Reset', false, reset));
      buttons.appendChild(btn('Empty', false, clearAll));
    }

    const HINTS = {
      stack: 'Push until you see an overflow, then pop until you see an underflow. A value in brackets is still in the array but is no longer part of the structure.',
      queue: 'Enqueue until the queue is full, dequeue two or three items, then enqueue again: the places freed at the front are wasted. A value in brackets is no longer in the queue.',
      circular: 'Fill the queue, dequeue some items, then enqueue again: RearPointer wraps round to the first index (MOD) and uses the freed places. Count tells full from empty.',
      list: 'Insert keeps the list in order by changing pointers; nothing moves. Delete a node, then insert again to see the freed node reused. Numbers are compared as numbers, so use all numbers or all words.'
    };

    function setTab(t, userClick) {
      tab = t;
      S.TYPES.forEach(function (k) { tabBtns[k].setAttribute('aria-pressed', k === t ? 'true' : 'false'); });
      setButtons();
      hint.textContent = HINTS[t];
      if (userClick) say(S.NAMES[t] + ' shown.', false);
      else say('Type a value and use the buttons.', false);
      paint();
    }

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); if (primary) primary(); }
    });

    setTab(first, false);
  }

  if (typeof W !== 'undefined' && W.register) W.register('cs-stack', init);
  if (typeof module !== 'undefined' && module.exports) module.exports = S;
})();
