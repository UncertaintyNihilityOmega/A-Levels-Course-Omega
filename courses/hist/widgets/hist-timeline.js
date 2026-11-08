/* hist-timeline: an interactive timeline you can step through.
   <div class="widget" data-w="hist-timeline" data-title="…" data-lanes="Politics,Religion,War"
        data-events="1789-07-14 | Bastille stormed | detail ;; 1789-08-04 | August Decrees | detail | Politics"></div>
   Events are separated by " ;; ", fields by " | ": date (YYYY, YYYY-MM or YYYY-MM-DD) | label | detail | lane (optional). */
(function () {
  'use strict';

  const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const SHORT = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  function utc(y, mo, d) {
    const dt = new Date(0);
    dt.setUTCFullYear(y, mo - 1, d);
    dt.setUTCHours(0, 0, 0, 0);
    return dt;
  }

  // "1789-07-14" -> {y, mo, d, t, prec}; null when the date is not valid
  function parseDate(s) {
    const m = /^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$/.exec(String(s).trim());
    if (!m) return null;
    const y = +m[1];
    const mo = m[2] ? +m[2] : null;
    const d = m[3] ? +m[3] : null;
    if (mo !== null && (mo < 1 || mo > 12)) return null;
    if (d !== null) {
      const dt = utc(y, mo, d);
      if (dt.getUTCFullYear() !== y || dt.getUTCMonth() !== mo - 1 || dt.getUTCDate() !== d) return null;
    }
    const t = utc(y, mo || 1, d || 1).getTime();
    return { y, mo, d, t, prec: d !== null ? 'day' : (mo !== null ? 'month' : 'year') };
  }

  function fmtDate(e) {
    if (e.prec === 'day') return e.d + ' ' + MONTHS[e.mo - 1] + ' ' + e.y;
    if (e.prec === 'month') return MONTHS[e.mo - 1] + ' ' + e.y;
    return String(e.y);
  }

  // Parses the attributes. Returns {events, lanes, problems}.
  function parseEvents(raw, laneAttr) {
    const events = [];
    const problems = [];
    const parts = String(raw || '').split(';;').map(function (s) { return s.trim(); }).filter(Boolean);
    parts.forEach(function (part, i) {
      const f = part.split('|').map(function (s) { return s.trim(); });
      const dt = f.length >= 2 ? parseDate(f[0]) : null;
      if (!dt || !f[1]) {
        problems.push('Event ' + (i + 1) + ' ("' + part.slice(0, 40) + (part.length > 40 ? '…' : '') + '") needs a date like 1789-07-14 and a label.');
        return;
      }
      events.push({ y: dt.y, mo: dt.mo, d: dt.d, t: dt.t, prec: dt.prec, label: f[1], detail: f[2] || '', lane: f[3] || '', n: events.length });
    });
    events.sort(function (a, b) { return a.t - b.t || a.n - b.n; });
    const lanes = String(laneAttr || '').split(',').map(function (s) { return s.trim(); }).filter(Boolean);
    events.forEach(function (e) { if (e.lane && lanes.indexOf(e.lane) < 0) lanes.push(e.lane); });
    return { events: events, lanes: lanes, problems: problems };
  }

  // Tick marks along the axis: [{t, text}] with at most about six labels
  function makeTicks(tMin, tMax) {
    const ticks = [];
    const yr = 365.25 * 86400000;
    const span = (tMax - tMin) / yr;
    const y0 = new Date(tMin).getUTCFullYear();
    const y1 = new Date(tMax).getUTCFullYear();
    if (span >= 2) {
      const steps = [1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000];
      let step = steps[steps.length - 1];
      for (let i = 0; i < steps.length; i++) {
        if (Math.floor(y1 / steps[i]) - Math.ceil(y0 / steps[i]) + 1 <= 6) { step = steps[i]; break; }
      }
      for (let y = Math.ceil(y0 / step) * step; y <= y1; y += step) {
        const t = utc(y, 1, 1).getTime();
        if (t >= tMin && t <= tMax) ticks.push({ t: t, text: String(y) });
      }
    } else if (span > 0) {
      const months = Math.max(1, Math.ceil(span * 12));
      const mstep = months <= 6 ? 1 : (months <= 12 ? 2 : 4);
      let y = y0;
      let mo = new Date(tMin).getUTCMonth() + 1;
      for (let guard = 0; guard < 60; guard++) {
        const t = utc(y, mo, 1).getTime();
        if (t > tMax) break;
        if (t >= tMin && (mo - 1) % mstep === 0) ticks.push({ t: t, text: SHORT[mo - 1] + ' ' + y });
        mo += 1;
        if (mo > 12) { mo = 1; y += 1; }
      }
    }
    return ticks;
  }

  W.register('hist-timeline', function (el, opts) {
    const title = el.getAttribute('data-title') || (opts && (opts.title || opts['data-title'])) || 'Timeline';
    const frame = W.frame(el, title, 'Step through the events with Previous and Next, or with the left and right arrow keys.');
    const body = frame.body;
    const parsed = parseEvents(
      el.getAttribute('data-events') || (opts && (opts.events || opts['data-events'])),
      el.getAttribute('data-lanes') || (opts && (opts.lanes || opts['data-lanes']))
    );
    const events = parsed.events;
    const lanes = parsed.lanes;

    function mk(tag, props) {
      const n = document.createElement(tag);
      const p = props || {};
      Object.keys(p).forEach(function (k) {
        if (k === 'text') n.textContent = p[k];
        else if (k === 'style') Object.assign(n.style, p[k]);
        else if (k === 'class') n.className = p[k];
        else if (k.slice(0, 2) === 'on') n[k] = p[k];
        else n.setAttribute(k, p[k]);
      });
      for (let i = 2; i < arguments.length; i++) {
        const c = arguments[i];
        if (c) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
      }
      return n;
    }

    if (!events.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'This timeline needs events. Write them in data-events as: date | label | detail ;; date | label | detail. Dates look like 1789, 1789-07 or 1789-07-14.' }));
      if (parsed.problems.length) body.appendChild(mk('p', { class: 'w-err', text: parsed.problems.slice(0, 3).join(' ') }));
      return;
    }
    if (parsed.problems.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: parsed.problems.length + ' event(s) were skipped. ' + parsed.problems.slice(0, 2).join(' ') }));
    }

    const tMin = events[0].t;
    const tMax = events[events.length - 1].t;
    let filter = '';
    let visible = events.slice();
    let cur = events[0];

    function pos(t) { return tMax === tMin ? 50 : (t - tMin) / (tMax - tMin) * 100; }

    // Lane filter
    let filterBtns = [];
    if (lanes.length) {
      const group = mk('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Show events from one lane' });
      const names = [''].concat(lanes);
      filterBtns = names.map(function (name) {
        const b = mk('button', { type: 'button', class: 'w-tab', 'aria-pressed': name === '' ? 'true' : 'false', text: name === '' ? 'All' : name });
        b.onclick = function () { setFilter(name); };
        group.appendChild(b);
        return b;
      });
      body.appendChild(mk('div', { class: 'w-row' }, group));
    }

    // Axis: one row per lane, dots placed in proportion to date
    const hasNoLane = events.some(function (e) { return !e.lane; });
    const rows = lanes.length ? lanes.length + (hasNoLane ? 1 : 0) : 1;
    const ROW = lanes.length ? 32 : 30;
    const axisH = rows * ROW + 22;
    function rowOf(e) { const i = lanes.indexOf(e.lane); return i < 0 ? rows - 1 : i; }
    function rowY(r) { return r * ROW + (lanes.length ? 22 : 15); }
    const axisLabel = 'Axis from ' + fmtDate(events[0]) + ' to ' + fmtDate(events[events.length - 1]) + ', ' + events.length + ' events. Use the list below to choose an event.';
    const strip = mk('div', { style: { position: 'relative', height: axisH + 'px', margin: '10px 22px 4px', overflow: 'visible' }, role: 'img', 'aria-label': axisLabel });
    makeTicks(tMin, tMax).forEach(function (tk) {
      const p = pos(tk.t);
      strip.appendChild(mk('div', { style: { position: 'absolute', left: p + '%', top: '0', width: '1px', height: (rows * ROW) + 'px', background: 'var(--rule)' }, 'aria-hidden': 'true' }));
      strip.appendChild(mk('div', { style: { position: 'absolute', left: p + '%', top: (rows * ROW + 4) + 'px', transform: 'translateX(-50%)', fontSize: '11px', color: 'var(--ink-3)', whiteSpace: 'nowrap' }, 'aria-hidden': 'true', text: tk.text }));
    });
    for (let r = 0; r < rows; r++) {
      strip.appendChild(mk('div', { style: { position: 'absolute', left: '0', right: '0', top: (rowY(r) - 1) + 'px', height: '2px', background: 'var(--ink-3)', opacity: '0.45' }, 'aria-hidden': 'true' }));
      if (lanes.length && r < lanes.length) {
        strip.appendChild(mk('div', { style: { position: 'absolute', left: '0', top: (r * ROW) + 'px', fontSize: '11px', lineHeight: '12px', color: 'var(--ink-3)', whiteSpace: 'nowrap' }, 'aria-hidden': 'true', text: lanes[r] }));
      }
    }
    const dotLayer = mk('div', { style: { position: 'absolute', left: '0', right: '0', top: '0', height: (rows * ROW) + 'px' } });
    strip.appendChild(dotLayer);
    body.appendChild(strip);

    // Readout of the selected event
    const read = mk('div', { 'aria-live': 'polite', 'aria-atomic': 'true', style: { border: '1px solid var(--rule)', borderLeft: '4px solid var(--sc)', borderRadius: '8px', padding: '10px 12px', margin: '6px 0', background: 'var(--card)' } });
    body.appendChild(read);

    // Previous / Next
    const prev = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: '← Previous' });
    const next = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Next →' });
    const counter = mk('span', { class: 'w-lab', style: { color: 'var(--ink-2)' } });
    prev.onclick = function () { step(-1, false); };
    next.onclick = function () { step(1, false); };
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, prev, next, counter));

    // Scrollable list of events
    const listId = W.uid ? W.uid('hist-tl') : 'hist-tl';
    const list = mk('ol', { id: listId, 'aria-label': 'All events in date order', style: { listStyle: 'none', margin: '6px 0 0', padding: '0', maxHeight: '240px', overflowY: 'auto', position: 'relative', border: '1px solid var(--rule)', borderRadius: '8px' } });
    body.appendChild(list);
    body.appendChild(mk('p', { class: 'w-note', text: 'Try: choose one lane, then step through it with the arrow keys to follow a single thread of the story.' }));

    let items = [];

    function renderList() {
      list.innerHTML = '';
      items = visible.map(function (e) {
        const b = mk('button', {
          type: 'button',
          style: { display: 'block', width: '100%', textAlign: 'left', background: 'transparent', color: 'var(--ink)', border: '0', borderBottom: '1px solid var(--rule)', padding: '7px 10px', cursor: 'pointer', font: 'inherit', fontSize: '14px', lineHeight: '1.35' }
        });
        b.appendChild(mk('span', { style: { color: 'var(--ink-2)' }, text: fmtDate(e) + ': ' }));
        b.appendChild(mk('span', { text: e.label }));
        if (e.lane) b.appendChild(mk('span', { style: { color: 'var(--ink-3)', fontSize: '12px' }, text: ' (' + e.lane + ')' }));
        b.onclick = function () { select(e, false); };
        const li = mk('li', { style: { margin: '0', padding: '0' } }, b);
        list.appendChild(li);
        return { e: e, b: b };
      });
    }

    function renderDots() {
      dotLayer.innerHTML = '';
      visible.forEach(function (e) {
        const sel = e === cur;
        const size = sel ? 14 : 10;
        const d = mk('button', {
          type: 'button', tabindex: '-1', 'aria-hidden': 'true',
          style: {
            position: 'absolute', left: pos(e.t) + '%', top: (rowY(rowOf(e)) - size / 2) + 'px', width: size + 'px', height: size + 'px', padding: '0',
            marginLeft: (-size / 2) + 'px', borderRadius: '50%', border: '2px solid var(--sc)', cursor: 'pointer',
            background: sel ? 'var(--sc)' : 'var(--card)', zIndex: sel ? '3' : '1', boxSizing: 'border-box'
          }
        });
        d.onclick = function () { select(e, false); };
        dotLayer.appendChild(d);
      });
    }

    function renderRead() {
      read.innerHTML = '';
      const i = visible.indexOf(cur);
      read.appendChild(mk('div', { style: { fontSize: '13px', color: 'var(--ink-2)' }, text: fmtDate(cur) + (cur.lane ? ' · ' + cur.lane : '') }));
      read.appendChild(mk('div', { style: { fontWeight: '700', margin: '2px 0' }, text: cur.label }));
      if (cur.detail) read.appendChild(mk('div', { style: { fontSize: '14px', lineHeight: '1.45' }, text: cur.detail }));
      counter.textContent = 'Event ' + (i + 1) + ' of ' + visible.length + (i === 0 ? ' (first)' : (i === visible.length - 1 ? ' (last)' : ''));
    }

    function markList() {
      items.forEach(function (it) {
        const on = it.e === cur;
        if (on) it.b.setAttribute('aria-current', 'true'); else it.b.removeAttribute('aria-current');
        it.b.style.fontWeight = on ? '700' : '400';
        it.b.style.background = 'transparent';
        it.b.style.boxShadow = on ? 'inset 4px 0 0 var(--sc)' : 'none';
        const first = it.b.firstChild;
        if (first && first.textContent.charAt(0) === '▸') first.textContent = first.textContent.slice(2);
        if (on && first) first.textContent = '▸ ' + first.textContent;
      });
      const it = items.filter(function (x) { return x.e === cur; })[0];
      if (it && list.clientHeight > 0) {
        const top = it.b.parentNode.offsetTop;
        const h = it.b.parentNode.offsetHeight;
        if (top < list.scrollTop) list.scrollTop = top;
        else if (top + h > list.scrollTop + list.clientHeight) list.scrollTop = top + h - list.clientHeight;
      }
    }

    function select(e, focusItem) {
      cur = e;
      renderDots();
      renderRead();
      markList();
      if (focusItem) {
        const it = items.filter(function (x) { return x.e === cur; })[0];
        if (it) it.b.focus();
      }
    }

    function step(dir, fromKey) {
      const i = visible.indexOf(cur);
      const j = Math.max(0, Math.min(visible.length - 1, i + dir));
      const inList = fromKey && list.contains(document.activeElement);
      select(visible[j], inList);
    }

    function setFilter(name) {
      filter = name;
      visible = events.filter(function (e) { return !name || e.lane === name; });
      if (!visible.length) visible = events.slice();
      if (visible.indexOf(cur) < 0) {
        // nearest visible event in time
        cur = visible.reduce(function (best, e) { return Math.abs(e.t - cur.t) < Math.abs(best.t - cur.t) ? e : best; }, visible[0]);
      }
      filterBtns.forEach(function (b, k) { b.setAttribute('aria-pressed', ((k === 0 && name === '') || (k > 0 && lanes[k - 1] === name)) ? 'true' : 'false'); });
      renderList();
      select(cur, false);
    }

    el.addEventListener('keydown', function (ev) {
      if (ev.altKey || ev.ctrlKey || ev.metaKey) return;
      if (ev.key === 'ArrowRight') { ev.preventDefault(); step(1, true); }
      else if (ev.key === 'ArrowLeft') { ev.preventDefault(); step(-1, true); }
    });

    renderList();
    select(cur, false);

    // test hook for Node-style checks (no effect on readers)
    el.__histTimeline = { parseDate: parseDate, parseEvents: parseEvents, makeTicks: makeTicks, fmtDate: fmtDate, step: step, setFilter: setFilter, state: function () { return { cur: cur, visible: visible, filter: filter }; } };
  });
})();
