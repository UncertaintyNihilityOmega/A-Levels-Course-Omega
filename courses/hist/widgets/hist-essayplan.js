/* hist-essayplan: essay-plan builder. The reader puts each factor on one side (supports the view in the question, or challenges it),
   ranks the factors with up and down buttons, chooses a criterion and a judgement, then builds a paragraph outline as text to copy.
   <div class="widget" data-w="hist-essayplan" data-title="Plan the essay"
        data-question="'…' How far do you agree?"
        data-factors="factor | support | evidence hint | why it is on that side ;; factor | challenge | evidence hint"
        data-criteria="Necessary: … | Decisive: …"  data-judgements="The view is largely right | …"></div>
   Factors separated by " ;; ", fields by " | " (no " | " or " ;; " inside the text). Field 2 is the course's own side (support or
   challenge): the reader is told where their sorting differs. Fields 3 and 4 are optional. Criteria and judgements are optional lists. */
(function () {
  'use strict';

  const DEFAULT_CRITERIA = [
    'Necessary: without it the outcome could not have happened',
    'Decisive: it turned the situation from one outcome to another',
    'Widest in effect: it touched the most people or areas',
    'Most lasting: its effects did not go away',
    'Root cause: it explains the other factors'
  ];
  const DEFAULT_JUDGEMENTS = [
    'The view is largely right',
    'The view is partly right: it matters, but other factors matter more',
    'The view is largely wrong'
  ];

  function parseList(raw, fallback) {
    const out = [];
    String(raw || '').split('|').forEach(function (s) {
      const t = s.trim();
      if (t && out.indexOf(t) < 0) out.push(t);
    });
    return out.length >= 2 ? out : fallback.slice();
  }

  // "factor | support | hint | why ;; …" -> {factors:[{text, side, hint, why}], problems}
  function parseFactors(raw) {
    const factors = [];
    const problems = [];
    String(raw || '').split(';;').map(function (s) { return s.trim(); }).filter(Boolean).forEach(function (part, i) {
      const f = part.split('|').map(function (s) { return s.trim(); });
      const s = (f[1] || '').toLowerCase();
      const side = s.indexOf('support') === 0 ? 'support' : (s.indexOf('challenge') === 0 ? 'challenge' : '');
      if (!f[0] || !side) {
        problems.push('Factor ' + (i + 1) + ' ("' + part.slice(0, 40) + (part.length > 40 ? '…' : '') + '") needs text and "support" or "challenge".');
        return;
      }
      factors.push({ text: f[0], side: side, hint: f[2] || '', why: f[3] || '' });
    });
    if (factors.length > 8) { problems.push('At most eight factors are used; the extra ones were ignored.'); factors.length = 8; }
    return { factors: factors, problems: problems };
  }

  const SIDE_WORD = { support: 'supports the view', challenge: 'challenges the view' };

  // pure function: the plan text from the state (also used by the tests)
  function planText(question, factors, order, side, criterion, judgement) {
    const rank = {};
    order.forEach(function (fi, r) { rank[fi] = r + 1; });
    const sup = order.filter(function (fi) { return side[fi] === 'support'; });
    const cha = order.filter(function (fi) { return side[fi] === 'challenge'; });
    const lines = [];
    lines.push('QUESTION: ' + question);
    lines.push('');
    lines.push('INTRODUCTION (2 to 4 sentences, no story)');
    lines.push('- Line of argument: ' + judgement + '.');
    lines.push('- Criterion for the judgement: ' + criterion + '.');
    lines.push('- Say what you will weigh: ' + order.map(function (fi) { return factors[fi].text; }).join('; ') + '.');
    lines.push('');
    let n = 0;
    function para(fi, label) {
      n += 1;
      lines.push('PARAGRAPH ' + n + ' (' + label + '; ranked ' + rank[fi] + ' of ' + order.length + ')');
      lines.push('- Point: ' + factors[fi].text + ' ' + SIDE_WORD[side[fi]] + '.');
      if (factors[fi].hint) lines.push('- Evidence to use: ' + factors[fi].hint + '.');
      lines.push('- Explain: say how the evidence makes the point, and how far it meets the criterion.');
      const others = order.filter(function (o) { return o !== fi; });
      const nearest = others.length ? others.reduce(function (best, o) { return Math.abs(rank[o] - rank[fi]) < Math.abs(rank[best] - rank[fi]) ? o : best; }) : -1;
      lines.push('- Link: ' + (nearest >= 0 ? 'compare it with "' + factors[nearest].text + '" (ranked ' + rank[nearest] + ') and say which matters more.' : 'tie it back to the question.'));
      lines.push('');
    }
    sup.forEach(function (fi) { para(fi, 'for the view'); });
    cha.forEach(function (fi) { para(fi, 'against the view'); });
    lines.push('CONCLUSION');
    lines.push('- Weigh the factors by the criterion: the factor ranked 1 is "' + factors[order[0]].text + '". Does it meet the criterion better than the factor ranked 2' + (order.length > 1 ? ', "' + factors[order[1]].text + '"' : '') + '? Say why.');
    lines.push('- Judgement: ' + judgement + '.');
    lines.push('- Finish by saying what would have to be different for you to judge the other way.');
    if (!sup.length || !cha.length) {
      lines.push('');
      lines.push('NOTE: every factor is on one side. A top-level answer weighs an alternative; look again at your sorting.');
    }
    return lines.join('\n');
  }

  W.register('hist-essayplan', function (el, opts) {
    const get = function (k) { return el.getAttribute('data-' + k) || (opts && (opts[k] || opts['data-' + k])) || ''; };
    const frame = W.frame(el, get('title') || 'Plan the essay', 'Sort the factors, rank them, choose a criterion and a judgement, then build the plan.');
    const body = frame.body;

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

    const pf = parseFactors(get('factors'));
    const factors = pf.factors;
    const question = get('question') || 'Your question';
    const criteria = parseList(get('criteria'), DEFAULT_CRITERIA);
    const judgements = parseList(get('judgements'), DEFAULT_JUDGEMENTS);

    if (factors.length < 2) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'This planner needs data-factors (at least two) written as: factor | support or challenge | evidence hint ;; factor | support or challenge | evidence hint.' }));
      if (pf.problems.length) body.appendChild(mk('p', { class: 'w-err', text: pf.problems.slice(0, 3).join(' ') }));
      return;
    }
    if (pf.problems.length) body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: pf.problems.slice(0, 3).join(' ') }));

    const side = factors.map(function () { return ''; });          // '' (not sorted), 'support' or 'challenge'
    let order = factors.map(function (f, i) { return i; });         // most important first
    let criterion = -1;
    let judgement = -1;
    let built = '';

    body.appendChild(mk('p', { style: { margin: '0 0 10px', fontWeight: '600' } }, mk('span', { class: 'w-lab', text: 'Question: ' }), question));

    const status = mk('p', { class: 'w-lab', role: 'status', 'aria-live': 'polite', 'aria-atomic': 'true', style: { margin: '6px 0', color: 'var(--ink-2)', fontWeight: '600' } });
    function say(t) { status.textContent = t; }

    // 1. sort
    body.appendChild(mk('h4', { style: { margin: '8px 0 4px' }, text: '1. Sort: does each factor support the view or challenge it?' }));
    const sortList = mk('ul', { 'aria-label': 'Factors to sort', style: { listStyle: 'none', margin: '0', padding: '0' } });
    const sortRows = [];
    factors.forEach(function (f, i) {
      const tid = W.uid ? W.uid('hist-ep') : 'hist-ep-' + i;
      const group = mk('div', { class: 'w-tabs', role: 'group', 'aria-labelledby': tid });
      const btns = {};
      [['support', 'Supports the view'], ['challenge', 'Challenges the view']].forEach(function (p) {
        const b = mk('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false', text: p[1] });
        b.onclick = function () { setSide(i, p[0]); };
        btns[p[0]] = b;
        group.appendChild(b);
      });
      const li = mk('li', { style: { margin: '0 0 10px' } },
        mk('div', { id: tid, style: { fontWeight: '600' }, text: f.text }),
        f.hint ? mk('div', { style: { fontSize: '0.9em', color: 'var(--ink-2)' }, text: 'Evidence: ' + f.hint }) : null,
        mk('div', { class: 'w-row' }, group));
      sortRows[i] = btns;
      sortList.appendChild(li);
    });
    body.appendChild(sortList);

    // 2. rank
    body.appendChild(mk('h4', { style: { margin: '10px 0 4px' }, text: '2. Rank: most important first (by your own judgement)' }));
    const rankList = mk('ol', { 'aria-label': 'Factors from most to least important', style: { margin: '0', padding: '0 0 0 22px' } });
    body.appendChild(rankList);

    function sideLabel(fi) { return side[fi] === 'support' ? 'for' : (side[fi] === 'challenge' ? 'against' : 'not sorted'); }

    function renderRank(focusFi, focusDir) {
      rankList.textContent = '';
      let focusBtn = null;
      order.forEach(function (fi, r) {
        const up = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', 'aria-label': 'Move "' + factors[fi].text + '" up', text: '▲ Up' });
        const down = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', 'aria-label': 'Move "' + factors[fi].text + '" down', text: '▼ Down' });
        up.onclick = function () { move(fi, -1); };
        down.onclick = function () { move(fi, 1); };
        if (fi === focusFi) focusBtn = focusDir < 0 ? up : down;
        rankList.appendChild(mk('li', { style: { margin: '0 0 8px' } },
          mk('span', { text: factors[fi].text + ' (' + sideLabel(fi) + ') ' }),
          mk('div', { class: 'w-row', style: { gap: '6px', marginTop: '2px' } }, up, down)));
      });
      if (focusBtn && focusBtn.focus) focusBtn.focus();
    }

    // 3. criterion and judgement
    body.appendChild(mk('h4', { style: { margin: '10px 0 4px' }, text: '3. Choose a criterion and a judgement' }));
    function makeSelect(label, list, onpick) {
      const id = W.uid ? W.uid('hist-ep-s') : 'hist-ep-s-' + label;
      const sel = mk('select', { id: id });
      sel.appendChild(mk('option', { value: '-1', text: 'Choose…' }));
      list.forEach(function (t, i) { sel.appendChild(mk('option', { value: String(i), text: t })); });
      sel.value = '-1';
      sel.onchange = function () { onpick(Number(sel.value)); };
      return { sel: sel, el: mk('div', { class: 'w-ctl', style: { display: 'block', margin: '0 0 8px' } }, mk('label', { class: 'w-lab', for: id, text: label }), sel) };
    }
    const critSel = makeSelect('Criterion for judging which factor matters most', criteria, function (n) { setCriterion(n); });
    const judgSel = makeSelect('Your judgement on the question', judgements, function (n) { setJudgement(n); });
    body.appendChild(critSel.el);
    body.appendChild(judgSel.el);

    const buildBtn = mk('button', { type: 'button', class: 'btn btn-sm', text: 'Build plan' });
    const resetBtn = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset' });
    buildBtn.onclick = function () { build(); };
    resetBtn.onclick = function () { reset(); };
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, buildBtn, resetBtn));
    body.appendChild(status);

    const outBox = mk('div', { style: { display: 'none', marginTop: '6px' } });
    const outLabelId = W.uid ? W.uid('hist-ep-o') : 'hist-ep-o';
    const outArea = mk('textarea', { readonly: 'readonly', rows: '16', 'aria-labelledby': outLabelId, style: { width: '100%', boxSizing: 'border-box', fontFamily: 'var(--mono, monospace)', fontSize: '0.85em' } });
    const copyBtn = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Copy plan' });
    const compare = mk('div', { style: { marginTop: '8px', fontSize: '0.92em' } });
    copyBtn.onclick = function () {
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(built).then(function () { say('Plan copied.'); }, function () { say('Could not copy. Select the text in the box and copy it yourself.'); });
          return;
        }
      } catch (e) { /* fall through */ }
      try { outArea.focus(); outArea.select(); } catch (e2) { /* ignore */ }
      say('Select the text in the box and copy it yourself.');
    };
    outBox.appendChild(mk('div', { id: outLabelId, class: 'w-lab', text: 'Your essay plan' }));
    outBox.appendChild(outArea);
    outBox.appendChild(mk('div', { class: 'w-row', style: { marginTop: '4px' } }, copyBtn));
    outBox.appendChild(compare);
    body.appendChild(outBox);
    body.appendChild(mk('p', { class: 'w-note', text: 'Try: sort every factor first, then rank them by which matters most to the answer, not by which you know best. A strong plan has factors on both sides, and a criterion that decides between them.' }));

    function paintSide(i) {
      ['support', 'challenge'].forEach(function (s) { sortRows[i][s].setAttribute('aria-pressed', side[i] === s ? 'true' : 'false'); });
    }

    function setSide(i, s) {
      if (i < 0 || i >= factors.length) return;
      side[i] = (s === 'support' || s === 'challenge') && side[i] !== s ? s : '';
      paintSide(i);
      renderRank(-1, 0);
      say('Factor ' + (i + 1) + ': ' + (side[i] ? SIDE_WORD[side[i]] : 'not sorted') + '.');
    }

    function move(fi, dir) {
      const r = order.indexOf(fi);
      if (r < 0) return;
      const t = r + (dir < 0 ? -1 : 1);
      if (t < 0 || t >= order.length) {
        say(dir < 0 ? 'That factor is already ranked first.' : 'That factor is already ranked last.');
        return;
      }
      const tmp = order[t]; order[t] = order[r]; order[r] = tmp;
      renderRank(fi, dir);
      say('"' + factors[fi].text + '" is now ranked ' + (t + 1) + ' of ' + order.length + '.');
    }

    function setCriterion(n) { criterion = (n >= 0 && n < criteria.length) ? n : -1; critSel.sel.value = String(criterion); }
    function setJudgement(n) { judgement = (n >= 0 && n < judgements.length) ? n : -1; judgSel.sel.value = String(judgement); }

    function missing() {
      const m = [];
      const unsorted = side.filter(function (s) { return !s; }).length;
      if (unsorted) m.push(unsorted + ' factor' + (unsorted === 1 ? '' : 's') + ' not sorted');
      if (criterion < 0) m.push('no criterion');
      if (judgement < 0) m.push('no judgement');
      return m;
    }

    function build() {
      const m = missing();
      if (m.length) {
        say('Not yet: ' + m.join(', ') + '.');
        return '';
      }
      built = planText(question, factors, order, side, criteria[criterion], judgements[judgement]);
      outArea.value = built;
      outBox.style.display = '';
      compare.textContent = '';
      const diff = factors.map(function (f, i) { return i; }).filter(function (i) { return side[i] !== factors[i].side; });
      if (!diff.length) {
        compare.appendChild(mk('div', { text: 'Your sorting matches the course\'s on all ' + factors.length + ' factors.' }));
      } else {
        compare.appendChild(mk('div', { text: 'Your sorting matches the course\'s on ' + (factors.length - diff.length) + ' of ' + factors.length + ' factors. Look again at:' }));
        const ul = mk('ul', { style: { margin: '2px 0 0', paddingLeft: '20px' } });
        diff.forEach(function (i) {
          ul.appendChild(mk('li', { text: factors[i].text + ': the course puts it as ' + (factors[i].side === 'support' ? 'supporting' : 'challenging') + ' the view.' + (factors[i].why ? ' ' + factors[i].why : '') }));
        });
        compare.appendChild(ul);
      }
      say('Plan built: ' + (factors.length) + ' factors, ' + (diff.length ? diff.length + ' sorted differently from the course.' : 'sorted as in the course.'));
      return built;
    }

    function reset() {
      for (let i = 0; i < factors.length; i++) { side[i] = ''; paintSide(i); }
      order = factors.map(function (f, i) { return i; });
      setCriterion(-1);
      setJudgement(-1);
      built = '';
      outArea.value = '';
      outBox.style.display = 'none';
      renderRank(-1, 0);
      say('Reset.');
    }

    renderRank(-1, 0);
    say('0 of ' + factors.length + ' factors sorted.');

    // test hook for Node-style checks (no effect on readers)
    el.__histEssay = {
      parseFactors: parseFactors, parseList: parseList, planText: planText,
      setSide: setSide, move: move, setCriterion: setCriterion, setJudgement: setJudgement, build: build, reset: reset,
      state: function () { return { side: side.slice(), order: order.slice(), criterion: criterion, judgement: judgement, built: built, status: status.textContent }; }
    };
  });
})();
