/* hist-provenance: source-evaluation trainer. For each source the reader chooses its nature, origin and purpose from lists, judges
   whether it is stronger or weaker evidence for the question, then checks against a model judgement and reason. No dragging.
   <div class="widget" data-w="hist-provenance" data-title="Judge the sources"
        data-question="How far do these sources show … ?"
        data-sources="A | provenance line | short content ;; B | provenance | content"
        data-answers="A | stronger | reason | nature | origin | purpose ;; B | weaker | reason | nature | origin | purpose"
        data-natures="Speech | Law or treaty | …"  data-origins="…"  data-purposes="…"></div>
   Sources and answers are separated by " ;; " and fields by " | " (so none of the text may contain " | " or " ;; ").
   The nature, origin and purpose fields of an answer are optional; the three option lists are optional (defaults below). */
(function () {
  'use strict';

  const DEFAULT_NATURES = ['Speech', 'Law or treaty', 'Diary or private letter', 'Essay, article or pamphlet', 'Party programme or petition',
    'Cartoon or poster', 'Photograph', 'Official report', 'Memoir or later account', 'Poem or song'];
  const DEFAULT_ORIGINS = ['Leader or decision-maker', 'Participant or eyewitness', 'Group or party', 'Government or official body',
    'Outside observer', 'Written later'];
  const DEFAULT_PURPOSES = ['Persuade', 'Justify or defend', 'Protest or demand', 'Command or regulate', 'Record or inform', 'Mock or criticise'];
  const DIMS = [
    { key: 'nature', label: 'Nature' },
    { key: 'origin', label: 'Origin' },
    { key: 'purpose', label: 'Purpose' }
  ];

  // "a | b | c" -> ['a','b','c'] (blank entries and repeats dropped); falls back to the defaults
  function parseList(raw, fallback) {
    const out = [];
    String(raw || '').split('|').forEach(function (s) {
      const t = s.trim();
      if (t && out.indexOf(t) < 0) out.push(t);
    });
    return out.length >= 2 ? out : fallback.slice();
  }

  // "label | provenance | content ;; …" -> {sources:[{label, prov, text}], problems}
  function parseSources(raw) {
    const sources = [];
    const problems = [];
    String(raw || '').split(';;').map(function (s) { return s.trim(); }).filter(Boolean).forEach(function (part, i) {
      const f = part.split('|').map(function (s) { return s.trim(); });
      if (!f[0] || f.length < 3 || !f[2]) {
        problems.push('Source ' + (i + 1) + ' ("' + part.slice(0, 40) + (part.length > 40 ? '…' : '') + '") needs: label | provenance line | content.');
        return;
      }
      sources.push({ label: f[0], prov: f[1], text: f.slice(2).join(' | ') });
    });
    return { sources: sources, problems: problems };
  }

  // "label | stronger | reason | nature | origin | purpose ;; …" -> {answers:{lowercase label: {verdict, why, nature, origin, purpose}}, problems}
  function parseAnswers(raw, labels) {
    const answers = {};
    const problems = [];
    const known = labels.map(function (l) { return l.toLowerCase(); });
    String(raw || '').split(';;').map(function (s) { return s.trim(); }).filter(Boolean).forEach(function (part, i) {
      const f = part.split('|').map(function (s) { return s.trim(); });
      const key = (f[0] || '').toLowerCase();
      const v = (f[1] || '').toLowerCase();
      const verdict = v.indexOf('strong') === 0 ? 'stronger' : (v.indexOf('weak') === 0 ? 'weaker' : '');
      if (!key || known.indexOf(key) < 0 || !verdict) {
        problems.push('Answer ' + (i + 1) + ' ("' + part.slice(0, 40) + (part.length > 40 ? '…' : '') + '") needs a source label and "stronger" or "weaker".');
        return;
      }
      answers[key] = { verdict: verdict, why: f[2] || '', nature: f[3] || '', origin: f[4] || '', purpose: f[5] || '' };
    });
    return { answers: answers, problems: problems };
  }

  W.register('hist-provenance', function (el, opts) {
    const get = function (k) { return el.getAttribute('data-' + k) || (opts && (opts[k] || opts['data-' + k])) || ''; };
    const frame = W.frame(el, get('title') || 'Judge the sources', 'Say what each source is, and whether it is stronger or weaker evidence for the question.');
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

    const lists = {
      nature: parseList(get('natures'), DEFAULT_NATURES),
      origin: parseList(get('origins'), DEFAULT_ORIGINS),
      purpose: parseList(get('purposes'), DEFAULT_PURPOSES)
    };
    const ps = parseSources(get('sources'));
    const sources = ps.sources;
    const pa = parseAnswers(get('answers'), sources.map(function (s) { return s.label; }));
    const problems = ps.problems.concat(pa.problems);
    const question = get('question');

    if (!sources.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'This trainer needs data-sources written as: label | provenance line | content ;; label | provenance line | content.' }));
      if (problems.length) body.appendChild(mk('p', { class: 'w-err', text: problems.slice(0, 3).join(' ') }));
      return;
    }
    if (problems.length) body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: problems.slice(0, 3).join(' ') }));

    // model tags that are not in the lists are added so the model answer can always be chosen
    sources.forEach(function (s) {
      const a = pa.answers[s.label.toLowerCase()];
      if (!a) return;
      DIMS.forEach(function (d) { if (a[d.key] && lists[d.key].indexOf(a[d.key]) < 0) lists[d.key].push(a[d.key]); });
    });

    const state = sources.map(function () { return { nature: -1, origin: -1, purpose: -1, verdict: '' }; });
    let checked = false;

    if (question) {
      body.appendChild(mk('p', { style: { margin: '0 0 10px', fontWeight: '600' } }, mk('span', { class: 'w-lab', text: 'Question: ' }), question));
    }

    const rows = [];   // per source: {selects:{nature,origin,purpose}, btns:{stronger,weaker}, result}
    const score = mk('p', { class: 'w-lab', 'aria-live': 'polite', 'aria-atomic': 'true', style: { margin: '8px 0 0', color: 'var(--ink-2)', fontWeight: '600' } });

    function answeredCount() {
      return state.filter(function (s) { return s.verdict && s.nature >= 0 && s.origin >= 0 && s.purpose >= 0; }).length;
    }

    function updateScore(afterCheck) {
      if (afterCheck) {
        let jt = 0, jr = 0, tt = 0, tr = 0;
        sources.forEach(function (s, i) {
          const a = pa.answers[s.label.toLowerCase()];
          if (!a) return;
          jt++;
          if (state[i].verdict === a.verdict) jr++;
          DIMS.forEach(function (d) {
            if (!a[d.key]) return;
            tt++;
            if (state[i][d.key] >= 0 && lists[d.key][state[i][d.key]] === a[d.key]) tr++;
          });
        });
        score.textContent = 'Score: judgements ' + jr + ' of ' + jt + ' right' + (tt ? '; tags ' + tr + ' of ' + tt + ' right' : '') + '.';
      } else if (checked) {
        score.textContent = 'Choices changed. Press Check to see your score.';
      } else {
        score.textContent = answeredCount() + ' of ' + sources.length + ' sources fully answered.';
      }
    }

    function paintVerdict(i) {
      ['stronger', 'weaker'].forEach(function (v) { rows[i].btns[v].setAttribute('aria-pressed', state[i].verdict === v ? 'true' : 'false'); });
    }

    function paintResult(i) {
      const r = rows[i].result;
      r.textContent = '';
      if (!checked) { r.style.display = 'none'; return; }
      r.style.display = '';
      const s = sources[i];
      const a = pa.answers[s.label.toLowerCase()];
      if (!a) {
        r.appendChild(mk('div', { style: { color: 'var(--ink-2)' }, text: 'No model answer is given for this source.' }));
        return;
      }
      DIMS.forEach(function (d) {
        if (!a[d.key]) return;
        const c = state[i][d.key];
        const line = mk('div');
        if (c < 0) {
          line.appendChild(mk('strong', { text: '– ' + d.label + ': not answered. ' }));
          line.appendChild(document.createTextNode('Model: ' + a[d.key] + '.'));
        } else if (lists[d.key][c] === a[d.key]) {
          line.appendChild(mk('strong', { style: { color: 'var(--ok)' }, text: '✓ ' + d.label + ': ' }));
          line.appendChild(document.createTextNode(a[d.key] + '.'));
        } else {
          line.appendChild(mk('strong', { style: { color: 'var(--red)' }, text: '✗ ' + d.label + ': ' }));
          line.appendChild(document.createTextNode('you chose ' + lists[d.key][c] + '; model: ' + a[d.key] + '.'));
        }
        r.appendChild(line);
      });
      const vline = mk('div', { style: { marginTop: '2px' } });
      if (!state[i].verdict) {
        vline.appendChild(mk('strong', { text: '– Judgement: not answered. ' }));
        vline.appendChild(document.createTextNode('Model: ' + a.verdict + ' evidence for this question.'));
      } else if (state[i].verdict === a.verdict) {
        vline.appendChild(mk('strong', { style: { color: 'var(--ok)' }, text: '✓ Judgement: ' }));
        vline.appendChild(document.createTextNode(a.verdict + ' evidence for this question.'));
      } else {
        vline.appendChild(mk('strong', { style: { color: 'var(--red)' }, text: '✗ Judgement: ' }));
        vline.appendChild(document.createTextNode('you chose ' + state[i].verdict + '; model: ' + a.verdict + ' evidence for this question.'));
      }
      r.appendChild(vline);
      if (a.why) r.appendChild(mk('div', { style: { marginTop: '2px', color: 'var(--ink-2)' }, text: a.why }));
    }

    function setTag(i, dim, idx) {
      if (i < 0 || i >= sources.length || !lists[dim]) return;
      const n = Number(idx);
      state[i][dim] = (n >= 0 && n < lists[dim].length) ? n : -1;
      if (rows[i] && rows[i].selects[dim]) rows[i].selects[dim].value = String(state[i][dim]);
      afterChange(i);
    }

    function setVerdict(i, v) {
      if (i < 0 || i >= sources.length) return;
      state[i].verdict = (v === 'stronger' || v === 'weaker') && state[i].verdict !== v ? v : '';
      paintVerdict(i);
      afterChange(i);
    }

    function afterChange(i) {
      if (checked) rows[i].result.style.display = 'none';   // this source changed: its old result is stale
      updateScore(false);
    }

    function check() {
      checked = true;
      sources.forEach(function (s, i) { paintResult(i); });
      updateScore(true);
    }

    function reset() {
      checked = false;
      sources.forEach(function (s, i) {
        state[i] = { nature: -1, origin: -1, purpose: -1, verdict: '' };
        DIMS.forEach(function (d) { rows[i].selects[d.key].value = '-1'; });
        paintVerdict(i);
        paintResult(i);
      });
      updateScore(false);
    }

    sources.forEach(function (s, i) {
      const selects = {};
      const controls = DIMS.map(function (d) {
        const id = W.uid ? W.uid('hist-prov') : 'hist-prov-' + i + d.key;
        const sel = mk('select', { id: id });
        sel.appendChild(mk('option', { value: '-1', text: 'Choose…' }));
        lists[d.key].forEach(function (opt, oi) { sel.appendChild(mk('option', { value: String(oi), text: opt })); });
        sel.value = '-1';
        sel.onchange = function () { setTag(i, d.key, sel.value); };
        selects[d.key] = sel;
        return mk('div', { class: 'w-ctl' }, mk('label', { class: 'w-lab', for: id, text: d.label + ' of Source ' + s.label }), sel);
      });
      const gid = W.uid ? W.uid('hist-prov-g') : 'hist-prov-g-' + i;
      const gl = mk('div', { id: gid, class: 'w-lab', text: 'As evidence for the question, Source ' + s.label + ' is:' });
      const group = mk('div', { class: 'w-tabs', role: 'group', 'aria-labelledby': gid });
      const btns = {};
      [['stronger', 'Stronger evidence'], ['weaker', 'Weaker evidence']].forEach(function (p) {
        const b = mk('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false', text: p[1] });
        b.onclick = function () { setVerdict(i, p[0]); };
        btns[p[0]] = b;
        group.appendChild(b);
      });
      const result = mk('div', { style: { display: 'none', marginTop: '8px', paddingTop: '6px', borderTop: '1px solid var(--rule)', fontSize: '0.92em' } });
      const card = mk('div', { style: { border: '1px solid var(--rule)', borderRadius: '8px', padding: '10px 12px', margin: '0 0 12px', background: 'var(--card)' } },
        mk('div', { style: { fontWeight: '700' }, text: 'Source ' + s.label }),
        mk('p', { style: { margin: '4px 0', fontStyle: 'italic', color: 'var(--ink-2)' }, text: s.prov }),
        mk('p', { style: { margin: '4px 0 8px' }, text: s.text }),
        mk('div', { class: 'w-row' }, controls[0], controls[1], controls[2]),
        gl, mk('div', { class: 'w-row' }, group),
        result);
      rows[i] = { selects: selects, btns: btns, result: result };
      body.appendChild(card);
    });

    const checkBtn = mk('button', { type: 'button', class: 'btn btn-sm', text: 'Check' });
    const resetBtn = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Reset' });
    checkBtn.onclick = check;
    resetBtn.onclick = reset;
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, checkBtn, resetBtn));
    body.appendChild(score);
    body.appendChild(mk('p', { class: 'w-note', text: 'Try: choose all four answers for each source before you press Check. The verdict is for this question only: the same source can be stronger for one question and weaker for another. Pressing a chosen verdict again clears it.' }));
    updateScore(false);

    // test hook for Node-style checks (no effect on readers)
    el.__histProv = {
      parseList: parseList, parseSources: parseSources, parseAnswers: parseAnswers,
      setTag: setTag, setVerdict: setVerdict, check: check, reset: reset,
      lists: lists,
      state: function () { return { state: state.map(function (s) { return Object.assign({}, s); }), checked: checked, score: score.textContent }; }
    };
  });
})();
