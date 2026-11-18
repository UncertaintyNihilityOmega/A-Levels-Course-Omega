/* widgets/cs-path.js
   <div class="widget" data-w="cs-path" data-graph="town" data-algo="astar" data-from="A" data-to="G"></div>
   data-graph: "town" (7 towns with straight-line distances) or "grid" (a 6 x 6 grid with walls and Manhattan distance); default town.
   data-algo: "dijkstra" or "astar" (default astar). data-from, data-to: node names of that graph (A to G, or A1 to F6).
   Dijkstra's algorithm and A* exactly as chapter cs.ai applies them by hand: choose the open node with the lowest value (Dijkstra: g;
   A*: f = g + h), ties to the node that comes first alphabetically; update a neighbour only when the new g is strictly smaller; stop
   when the goal is chosen. Test: data/cs-path.test.js compares every start and goal pair with the Python in data/cs_ai_algos.py. */
(function () {
  'use strict';

  // ---- the two built-in graphs (same numbers as chapter cs.ai: the town of its worked examples; a 6 x 6 grid) ----
  const TOWN_POS = { A: [0, 4], B: [3, 7], C: [4, 1], D: [5, 5], E: [8, 7], F: [8, 2], G: [11, 4] };
  const TOWN_EDGES = [['A', 'B', 5], ['A', 'C', 9], ['A', 'D', 6], ['B', 'D', 3], ['B', 'E', 6], ['C', 'D', 9], ['C', 'F', 7],
    ['D', 'E', 4], ['D', 'F', 8], ['E', 'G', 5], ['F', 'G', 8]];
  const GRID_COLS = 'ABCDEF';
  const GRID_ROWS = 6;
  const GRID_WALLS = ['B1', 'B2', 'B3', 'B4', 'C6', 'D2', 'D5', 'F4'];

  function buildGraphs() {
    const town = { id: 'town', adj: {}, pos: TOWN_POS };
    Object.keys(TOWN_POS).forEach(function (n) { town.adj[n] = {}; });
    TOWN_EDGES.forEach(function (e) { town.adj[e[0]][e[1]] = e[2]; town.adj[e[1]][e[0]] = e[2]; });
    const grid = { id: 'grid', adj: {}, walls: GRID_WALLS.slice() };
    const open = {};
    for (let c = 0; c < GRID_COLS.length; c++) for (let r = 1; r <= GRID_ROWS; r++) {
      const name = GRID_COLS[c] + r;
      if (GRID_WALLS.indexOf(name) < 0) { open[name] = [c, r]; grid.adj[name] = {}; }
    }
    Object.keys(open).forEach(function (n) {
      const c = open[n][0], r = open[n][1];
      [[1, 0], [0, 1]].forEach(function (d) {
        const m = GRID_COLS[c + d[0]] !== undefined ? GRID_COLS[c + d[0]] + (r + d[1]) : null;
        if (m && grid.adj[m]) { grid.adj[n][m] = 1; grid.adj[m][n] = 1; }
      });
    });
    grid.cells = open;
    return { town: town, grid: grid };
  }

  const GRAPHS = buildGraphs();

  function names(graph) { return Object.keys(graph.adj).sort(); }

  // heuristic to the goal: town = straight-line distance in whole km (rounded down); grid = Manhattan distance
  function heuristic(graph, goal) {
    const h = {};
    names(graph).forEach(function (n) {
      if (graph.id === 'town') {
        h[n] = Math.floor(Math.hypot(graph.pos[n][0] - graph.pos[goal][0], graph.pos[n][1] - graph.pos[goal][1]) + 1e-9);
      } else {
        h[n] = Math.abs(graph.cells[n][0] - graph.cells[goal][0]) + Math.abs(graph.cells[n][1] - graph.cells[goal][1]);
      }
    });
    return h;
  }

  // The search. steps[0] is the start; steps[k] is the k-th node chosen. Each step keeps copies of g, previous and state.
  function search(graph, algo, start, goal) {
    const adj = graph.adj;
    const list = names(graph);
    const h = algo === 'astar' ? heuristic(graph, goal) : {};
    if (algo !== 'astar') list.forEach(function (n) { h[n] = 0; });
    const g = {}, prev = {}, state = {};
    list.forEach(function (n) { g[n] = Infinity; prev[n] = null; state[n] = 'unseen'; });
    g[start] = 0;
    state[start] = 'open';
    function snap(current, updates, done, found) {
      return { current: current, updates: updates, done: done, found: found, g: Object.assign({}, g), prev: Object.assign({}, prev), state: Object.assign({}, state) };
    }
    const steps = [snap(null, [], false, false)];
    let chosen = 0;
    for (;;) {
      let best = null, bestF = Infinity;
      list.forEach(function (n) {
        if (state[n] !== 'open') return;
        const f = g[n] + h[n];
        if (best === null || f < bestF || (f === bestF && n < best)) { best = n; bestF = f; }
      });
      if (best === null) { const s = snap(null, [], true, false); steps.push(s); break; }
      state[best] = 'closed';
      chosen++;
      const updates = [];
      if (best !== goal) {
        Object.keys(adj[best]).sort().forEach(function (v) {
          if (state[v] === 'closed') return;
          const ng = g[best] + adj[best][v];
          if (ng < g[v]) {
            updates.push({ node: v, g: ng, old: g[v], isNew: state[v] === 'unseen' });
            g[v] = ng; prev[v] = best; state[v] = 'open';
          }
        });
      }
      const s = snap(best, updates, best === goal, best === goal);
      steps.push(s);
      if (best === goal) break;
    }
    const last = steps[steps.length - 1];
    let path = [];
    if (last.found) {
      for (let n = goal; n !== null; n = last.prev[n]) path.push(n);
      path.reverse();
    }
    return { steps: steps, h: h, chosen: chosen, found: last.found, path: path, cost: last.found ? last.g[goal] : null };
  }

  function order(run) { return run.steps.filter(function (s) { return s.current; }).map(function (s) { return s.current; }); }

  // one line in words for step k
  function describeStep(run, k, algo) {
    const s = run.steps[k];
    if (k === 0) {
      return algo === 'astar'
        ? 'Start: the start node is on the open list with g = 0 and f = h. Press Next to expand the node with the lowest f.'
        : 'Start: the start node has distance 0 and every other node is unknown. Press Next to visit the unvisited node with the smallest distance.';
    }
    if (!s.current) return 'The open list is empty and the goal was never reached: there is no path.';
    const g = s.g[s.current];
    const verb = algo === 'astar' ? 'Expand ' + s.current + ' (g = ' + g + ', h = ' + run.h[s.current] + ', f = ' + (g + run.h[s.current]) + ')' : 'Visit ' + s.current + ' (distance ' + g + ')';
    if (s.done) {
      return 'Step ' + k + ': ' + verb + '. It is the goal, so the search stops. Path: ' + run.path.join(' → ') + ', cost ' + run.cost + '.';
    }
    const ups = s.updates.length === 0 ? 'No neighbour improves.' : s.updates.map(function (u) {
      return u.node + ' gets g = ' + u.g + (u.isNew ? '' : ' (was ' + u.old + ')') + ' via ' + s.current;
    }).join('; ') + '.';
    return 'Step ' + k + ': ' + verb + '. ' + ups;
  }

  function parseChoice(v, allowed, dflt) {
    const s = String(v === undefined ? '' : v).trim();
    const hit = allowed.filter(function (a) { return a.toLowerCase() === s.toLowerCase(); })[0];
    return hit === undefined ? dflt : hit;
  }

  const DEFAULT_ENDS = { town: ['A', 'G'], grid: ['A1', 'F6'] };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { GRAPHS: GRAPHS, names: names, heuristic: heuristic, search: search, order: order, describeStep: describeStep, parseChoice: parseChoice, DEFAULT_ENDS: DEFAULT_ENDS };
  }
  if (typeof W === 'undefined' || !W.register) return;

  // ---- the widget ----
  W.register('cs-path', function (el, opts) {
    const f = W.frame(el, 'Dijkstra and A* step by step', 'Pick a graph, an algorithm, a start and a goal, then press Next');
    const body = f.body;
    opts = opts || {};
    const problems = [];

    let graphId = parseChoice(opts.graph, ['town', 'grid'], 'town');
    if (opts.graph !== undefined && opts.graph !== '' && graphId !== String(opts.graph).trim().toLowerCase()) problems.push('data-graph must be "town" or "grid", so "' + graphId + '" is used.');
    let algo = parseChoice(opts.algo, ['dijkstra', 'astar'], 'astar');
    if (opts.algo !== undefined && opts.algo !== '' && algo !== String(opts.algo).trim().toLowerCase()) problems.push('data-algo must be "dijkstra" or "astar", so "' + algo + '" is used.');
    let from = parseChoice(opts.from, names(GRAPHS[graphId]), DEFAULT_ENDS[graphId][0]);
    if (opts.from !== undefined && opts.from !== '' && from.toLowerCase() !== String(opts.from).trim().toLowerCase()) problems.push('data-from is not a node of this graph, so ' + from + ' is used.');
    let to = parseChoice(opts.to, names(GRAPHS[graphId]), DEFAULT_ENDS[graphId][1]);
    if (opts.to !== undefined && opts.to !== '' && to.toLowerCase() !== String(opts.to).trim().toLowerCase()) problems.push('data-to is not a node of this graph, so ' + to + ' is used.');
    if (problems.length) {
      const err = W.h('div', { class: 'w-err', text: problems.join(' ') });
      err.setAttribute('role', 'status');
      body.appendChild(err);
    }

    let run = null;
    let k = 0;

    // ---- controls ----
    function selectOf(label, values, current, texts) {
      const sel = W.h('select', {});
      sel.setAttribute('aria-label', label);
      values.forEach(function (v, i) { sel.appendChild(W.h('option', { value: v, text: texts ? texts[i] : v })); });
      sel.value = current;
      return sel;
    }
    const selGraph = selectOf('Graph', ['town', 'grid'], graphId, ['Town (7 towns)', 'Grid (6 by 6)']);
    const selAlgo = selectOf('Algorithm', ['dijkstra', 'astar'], algo, ['Dijkstra', 'A*']);
    const selFrom = selectOf('Start node', names(GRAPHS[graphId]), from);
    const selTo = selectOf('Goal node', names(GRAPHS[graphId]), to);
    function ctl(text, sel) { return W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: text }), sel); }
    body.appendChild(W.h('div', { class: 'w-row' }, ctl('Graph', selGraph), ctl('Algorithm', selAlgo)));
    body.appendChild(W.h('div', { class: 'w-row' }, ctl('From', selFrom), ctl('To', selTo)));

    const back = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: 'Back' });
    const next = W.h('button', { class: 'btn btn-sm', type: 'button', text: 'Next' });
    const resetBtn = W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: 'Restart' });
    const lab = W.h('span', { class: 'w-step', text: 'Start' });
    body.appendChild(W.h('div', { class: 'w-row w-stepper' }, back, lab, next, resetBtn));

    const live = W.h('p', { style: { margin: '6px 0', minHeight: '3em' } });
    live.setAttribute('aria-live', 'polite');
    body.appendChild(live);

    let cv = null;
    const canvasHost = W.h('div', {});
    body.appendChild(canvasHost);
    const legend = W.h('p', { class: 'w-note' });
    body.appendChild(legend);
    const summary = W.h('p', { style: { margin: '6px 0' } });
    summary.setAttribute('aria-live', 'polite');
    body.appendChild(summary);
    const tableWrap = W.h('div', { style: { maxHeight: '220px', overflow: 'auto', margin: '6px 0' } });
    tableWrap.setAttribute('role', 'region');
    tableWrap.setAttribute('aria-label', 'Table of the nodes found so far');
    tableWrap.setAttribute('tabindex', '0');
    body.appendChild(tableWrap);
    body.appendChild(W.h('p', { class: 'w-note', text: 'Ties (two nodes with the same distance, or the same f) go to the node that comes first alphabetically, as in the chapter. Town: h is the straight-line distance to the goal in whole kilometres. Grid: h is the Manhattan distance, moves are up, down, left or right and cost 1, and solid squares are walls. Try: run Dijkstra and then A* on the same start and goal, and compare how many nodes each chooses.' }));

    function fillNodes() {
      [selFrom, selTo].forEach(function (sel) {
        sel.textContent = '';
        names(GRAPHS[graphId]).forEach(function (n) { sel.appendChild(W.h('option', { value: n, text: n })); });
      });
      selFrom.value = from;
      selTo.value = to;
    }

    // ---- drawing ----
    function stateLabel(name) {
      const s = run.steps[k];
      if (s.current === name) return algo === 'astar' ? 'just expanded' : 'just visited';
      if (s.state[name] === 'closed') return algo === 'astar' ? 'closed' : 'visited';
      if (s.state[name] === 'open') return algo === 'astar' ? 'open' : 'has a distance';
      return 'not seen';
    }

    function valueText(name) {
      const s = run.steps[k];
      if (s.g[name] === Infinity) return '';
      return algo === 'astar' ? String(s.g[name] + run.h[name]) : String(s.g[name]);
    }

    function pathEdges() {
      const out = [];
      if (run.found && run.steps[k].done) for (let i = 0; i + 1 < run.path.length; i++) out.push([run.path[i], run.path[i + 1]]);
      return out;
    }

    function drawTown(ctx, w, h, c) {
      const pad = 34;
      const sx = (w - 2 * pad) / 11, sy = (h - 2 * pad) / 6;
      const X = function (n) { return pad + GRAPHS.town.pos[n][0] * sx; };
      const Y = function (n) { return pad + (GRAPHS.town.pos[n][1] - 1) * sy; };
      const r = Math.max(8, Math.min(14, sx * 0.45));
      const s = run.steps[k];
      const onPath = {};
      pathEdges().forEach(function (e) { onPath[e[0] + e[1]] = true; onPath[e[1] + e[0]] = true; });
      ctx.font = '11px ' + c.font;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      names(GRAPHS.town).forEach(function (a) {
        Object.keys(GRAPHS.town.adj[a]).forEach(function (b) {
          if (a > b) return;
          ctx.beginPath();
          ctx.moveTo(X(a), Y(a)); ctx.lineTo(X(b), Y(b));
          ctx.strokeStyle = onPath[a + b] ? c.sc : c.ink3;
          ctx.lineWidth = onPath[a + b] ? 4 : 1.2;
          ctx.stroke();
        });
      });
      names(GRAPHS.town).forEach(function (a) {
        Object.keys(GRAPHS.town.adj[a]).forEach(function (b) {
          if (a > b) return;
          const mx = (X(a) + X(b)) / 2, my = (Y(a) + Y(b)) / 2;
          const t = String(GRAPHS.town.adj[a][b]);
          ctx.fillStyle = c.card;
          ctx.fillRect(mx - 6, my - 7, 12, 14);
          ctx.fillStyle = c.ink2;
          ctx.fillText(t, mx, my);
        });
      });
      names(GRAPHS.town).forEach(function (n) {
        const st = s.state[n];
        ctx.beginPath();
        ctx.arc(X(n), Y(n), r, 0, Math.PI * 2);
        ctx.fillStyle = st === 'closed' ? c.hl : c.card;
        ctx.fill();
        ctx.setLineDash(st === 'open' ? [4, 3] : []);
        ctx.lineWidth = s.current === n ? 4 : 2;
        ctx.strokeStyle = s.current === n ? c.sc : (st === 'unseen' ? c.ink3 : c.ink);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = c.ink;
        ctx.font = 'bold 12px ' + c.font;
        ctx.fillText(n, X(n), Y(n));
        const vt = valueText(n);
        if (vt) {
          ctx.font = '11px ' + c.font;
          const tw = ctx.measureText(vt).width + 6;
          ctx.fillStyle = c.card;
          ctx.fillRect(X(n) - tw / 2, Y(n) - r - 15, tw, 13);
          ctx.fillStyle = c.ink;
          ctx.fillText(vt, X(n), Y(n) - r - 8.5);
        }
        if (n === from || n === to) {
          ctx.font = 'bold 11px ' + c.font;
          ctx.fillStyle = c.sc;
          ctx.fillText(n === from ? 'start' : 'goal', X(n), Y(n) + r + 9);
        }
      });
    }

    function drawGrid(ctx, w, h, c) {
      const cell = Math.min((w - 8) / GRID_COLS.length, (h - 8) / GRID_ROWS);
      if (!(cell > 6)) return;
      const ox = (w - cell * GRID_COLS.length) / 2, oy = (h - cell * GRID_ROWS) / 2;
      const s = run.steps[k];
      const walls = GRAPHS.grid.walls;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      for (let ci = 0; ci < GRID_COLS.length; ci++) for (let r = 1; r <= GRID_ROWS; r++) {
        const n = GRID_COLS[ci] + r;
        const x = ox + ci * cell, y = oy + (r - 1) * cell;
        if (walls.indexOf(n) >= 0) {
          ctx.fillStyle = c.ink;
          ctx.fillRect(x + 1, y + 1, cell - 2, cell - 2);
          continue;
        }
        const st = s.state[n];
        ctx.fillStyle = st === 'closed' ? c.hl : c.card;
        ctx.fillRect(x + 1, y + 1, cell - 2, cell - 2);
        ctx.setLineDash(st === 'open' ? [4, 3] : []);
        ctx.lineWidth = s.current === n ? 4 : 1.5;
        ctx.strokeStyle = s.current === n ? c.sc : (st === 'unseen' ? c.rule2 : c.ink);
        ctx.strokeRect(x + 2, y + 2, cell - 4, cell - 4);
        ctx.setLineDash([]);
        ctx.fillStyle = c.ink3;
        ctx.font = Math.max(8, Math.round(cell * 0.2)) + 'px ' + c.font;
        ctx.textAlign = 'left';
        ctx.fillText(n, x + 4, y + cell * 0.2);
        ctx.textAlign = 'center';
        const vt = valueText(n);
        if (vt) {
          ctx.fillStyle = c.ink;
          ctx.font = 'bold ' + Math.max(10, Math.round(cell * 0.32)) + 'px ' + c.font;
          ctx.fillText(vt, x + cell / 2, y + cell * 0.58);
        }
        if (n === from || n === to) {
          ctx.fillStyle = c.sc;
          ctx.font = 'bold ' + Math.max(9, Math.round(cell * 0.22)) + 'px ' + c.font;
          ctx.fillText(n === from ? 'start' : 'goal', x + cell / 2, y + cell * 0.86);
        }
      }
      const pe = pathEdges();
      if (pe.length) {
        ctx.beginPath();
        pe.forEach(function (e, i) {
          const a = GRAPHS.grid.cells[e[0]], b = GRAPHS.grid.cells[e[1]];
          const ax = ox + (a[0] + 0.5) * cell, ay = oy + (a[1] - 0.5) * cell, bx = ox + (b[0] + 0.5) * cell, by = oy + (b[1] - 0.5) * cell;
          if (i === 0) ctx.moveTo(ax, ay);
          ctx.lineTo(bx, by);
        });
        ctx.strokeStyle = c.sc;
        ctx.lineWidth = Math.max(3, cell * 0.1);
        ctx.lineJoin = 'round';
        ctx.stroke();
      }
    }

    function canvasLabel() {
      return (graphId === 'town' ? 'Town graph with 7 towns' : 'Grid of 6 by 6 squares with walls') + ', searched with ' + (algo === 'astar' ? 'A*' : 'Dijkstra') + ' from ' + from + ' to ' + to + '.';
    }

    function buildCanvas() {
      canvasHost.textContent = '';
      cv = W.canvas(canvasHost, {
        height: graphId === 'town' ? 250 : 300,
        label: canvasLabel(),
        describe: function () { return describeStep(run, k, algo) + ' ' + legendText(); },
        draw: function (ctx, w, h, colors) {
          if (!(w > 40) || !(h > 40) || !run) return;
          if (graphId === 'town') drawTown(ctx, w, h, colors); else drawGrid(ctx, w, h, colors);
        }
      });
    }

    function legendText() {
      return 'Solid outline and shading: ' + (algo === 'astar' ? 'closed' : 'visited') + '. Dashed outline: ' + (algo === 'astar' ? 'open' : 'has a distance, not yet visited') + '. Thick outline: the node just chosen. Number: ' + (algo === 'astar' ? 'f = g + h' : 'distance g') + '. The finished path is drawn as a thick line.';
    }

    function renderTable() {
      const s = run.steps[k];
      const astar = algo === 'astar';
      const th = function (t) { return W.h('th', { text: t, scope: 'col', style: { textAlign: 'left', padding: '3px 8px', whiteSpace: 'nowrap' } }); };
      const table = W.h('table', { style: { borderCollapse: 'collapse', fontSize: '13px', width: 'auto' } });
      const headRow = W.h('tr', {});
      (astar ? ['Node', 'g', 'h', 'f', 'Previous', 'State'] : ['Node', 'g', 'Previous', 'State']).forEach(function (t) { headRow.appendChild(th(t)); });
      table.appendChild(W.h('thead', {}, headRow));
      const tb = W.h('tbody', {});
      let any = false;
      names(GRAPHS[graphId]).forEach(function (n) {
        if (s.g[n] === Infinity) return;
        any = true;
        const td = function (t, bold) { return W.h('td', { text: t, style: { padding: '2px 8px', whiteSpace: 'nowrap', fontWeight: bold ? '700' : '400' } }); };
        const here = s.current === n;
        const tr = W.h('tr', {});
        tr.appendChild(td(n, true));
        tr.appendChild(td(String(s.g[n])));
        if (astar) { tr.appendChild(td(String(run.h[n]))); tr.appendChild(td(String(s.g[n] + run.h[n]))); }
        tr.appendChild(td(s.prev[n] === null ? 'none' : s.prev[n]));
        tr.appendChild(td(stateLabel(n), here));
        tb.appendChild(tr);
      });
      if (!any) tb.appendChild(W.h('tr', {}, W.h('td', { text: '(nothing found yet)', colspan: '6', style: { padding: '2px 8px' } })));
      table.appendChild(tb);
      tableWrap.textContent = '';
      tableWrap.appendChild(table);
    }

    function other() {
      const alt = search(GRAPHS[graphId], algo === 'astar' ? 'dijkstra' : 'astar', from, to);
      return alt.chosen;
    }

    function show() {
      const last = run.steps.length - 1;
      k = Math.max(0, Math.min(last, k));
      back.disabled = k === 0;
      next.disabled = k === last;
      lab.textContent = k === 0 ? 'Start' : 'Step ' + k + ' of ' + last;
      live.textContent = describeStep(run, k, algo);
      legend.textContent = legendText();
      const chosenNow = run.steps.slice(1, k + 1).filter(function (s) { return s.current; }).length;
      let sum = 'Nodes ' + (algo === 'astar' ? 'expanded' : 'visited') + ' so far: ' + chosenNow + '.';
      if (k === last) {
        if (run.found) sum += ' Finished: path ' + run.path.join(' → ') + ', cost ' + run.cost + '. ' + (algo === 'astar' ? 'Dijkstra' : 'A*') + ' would choose ' + other() + ' nodes for this start and goal; this run chose ' + run.chosen + '.';
        else sum += ' Finished: no path.';
      }
      summary.textContent = sum;
      renderTable();
      if (cv) { cv.setLabel(canvasLabel()); cv.redraw(); }
      const a = document.activeElement;
      if (a && a.disabled && a.parentNode && a.parentNode.contains(next)) resetBtn.focus();
    }

    function rerun(resetStep) {
      run = search(GRAPHS[graphId], algo, from, to);
      if (resetStep) k = 0;
      show();
    }

    selGraph.addEventListener('change', function () {
      graphId = selGraph.value;
      from = DEFAULT_ENDS[graphId][0];
      to = DEFAULT_ENDS[graphId][1];
      fillNodes();
      buildCanvas();
      rerun(true);
    });
    selAlgo.addEventListener('change', function () { algo = selAlgo.value; rerun(true); });
    selFrom.addEventListener('change', function () { from = selFrom.value; rerun(true); });
    selTo.addEventListener('change', function () { to = selTo.value; rerun(true); });
    back.addEventListener('click', function () { k -= 1; show(); });
    next.addEventListener('click', function () { k += 1; show(); });
    resetBtn.addEventListener('click', function () { k = 0; show(); });
    f.root.setAttribute('tabindex', f.root.getAttribute('tabindex') || '-1');
    f.root.addEventListener('keydown', function (e) {
      if (/input|select|textarea/i.test(e.target.tagName)) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); k += 1; show(); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); k -= 1; show(); }
    });

    buildCanvas();
    run = search(GRAPHS[graphId], algo, from, to);
    k = Math.min(2, run.steps.length - 1);
    show();
  });
})();
