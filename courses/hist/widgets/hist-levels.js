/* hist-levels: mark-band explorer for Cambridge 9489 (level descriptors for 2027-2029).
   <div class="widget" data-w="hist-levels" data-parts="p1a,p1b" data-start="p1a"></div>
   data-parts (optional): which parts to offer, any of p1a p1b p2a p2b p3a p3b p4a p4b (default: all eight).
   data-start (optional): the part shown first.
   The reader ticks what an answer does; the widget shows the level it reaches (a strict guide), the mark range, the descriptor and what
   would take the answer up one level. Features are taken from the level descriptors in the 2027 specimen mark schemes.
   A level counts as "met" when the reader has ticked at least `need` of its features (default: all of them) AND the
   level below it is met too (the lowest level needs only its own features); the highest level met is shown. This is stricter than an examiner, who takes the best fit. */
(function () {
  'use strict';

  // ---- data: one entry per part; levels from the top level down ----
  // f = features (what the answer does); need = how many of them must be ticked (default all)
  var PARTS = [
    {
      key: 'p1a', tab: 'P1 (a)', name: 'Paper 1 part (a)', title: 'compare two sources as evidence', marks: 15, table: 'Table A', aos: 'AO1, AO3',
      levels: [
        { n: 4, lo: 12, hi: 15, head: 'Makes a developed comparison',
          desc: 'A developed comparison between the two sources; explains why points of similarity and difference exist through contextual awareness and/or source evaluation.',
          f: ['Develops the comparison between the two sources, not just a list of points',
              'Explains why the similarities and differences exist, through context and/or evaluation of the sources (nature, origin, purpose)'] },
        { n: 3, lo: 8, hi: 11, head: 'Compares views and identifies similarities and differences',
          desc: 'Compares the views expressed in the two sources, identifying similarities and differences and supporting them with source content.',
          f: ['Compares the views in the two sources',
              'Identifies both similarities and differences',
              'Supports each point with content from the sources'] },
        { n: 2, lo: 4, hi: 7, head: 'Compares views and identifies similarities or differences',
          desc: 'Identifies relevant similarities or differences between the two sources and may be one-sided, with only one aspect explained; OR identifies similarities and differences but asserts them rather than supporting them from the sources.',
          need: 1,
          f: ['Identifies relevant similarities or differences, supported from the sources, but one-sided (only one aspect explained)',
              'Identifies similarities and differences, but only asserts them, with no support from the sources'] },
        { n: 1, lo: 1, hi: 3, head: 'Describes content of each source',
          desc: 'Describes or paraphrases the content of the two sources; may make very simple comparisons (for example, one is from a letter and the other from a speech) that are not developed.',
          need: 1,
          f: ['Describes or paraphrases the content of each source',
              'Makes only very simple comparisons that are not developed (for example, one is a letter and the other a speech)'] }
      ]
    },
    {
      key: 'p1b', tab: 'P1 (b)', name: 'Paper 1 part (b)', title: 'how far do the sources support the statement', marks: 25, table: 'Table B', aos: 'AO1, AO3',
      levels: [
        { n: 5, lo: 21, hi: 25, head: 'Evaluates the sources to reach a judgement',
          desc: 'Understanding of all the sources and a detailed explanation of how they support and/or challenge the statement; specific contextual knowledge used to evaluate the sources (nature, origin or purpose in context); assesses whether each source is stronger or weaker as evidence in response to the question; reaches a judgement about which side of the argument is stronger, addressing the "how far" element.',
          f: ['Shows understanding of all the sources and explains in detail how they support and/or challenge the statement',
              'Uses specific contextual knowledge to evaluate the sources (nature, origin or purpose in context)',
              'Assesses whether each source is stronger or weaker as evidence for this question',
              'Reaches a judgement on which side is stronger, addressing "how far"'] },
        { n: 4, lo: 16, hi: 20, head: 'Developed response explaining how the sources support and challenge',
          desc: 'Detailed use of all the sources to support and challenge the statement; accurately represents the argument of the sources (may show nuance); makes explicit and well explained links to the question; uses contextual knowledge to help interpret the sources, which may include the nature, origin or purpose of the source in context.',
          f: ['Makes detailed use of all the sources to support and challenge the statement',
              'Represents the argument of each source accurately (may show nuance)',
              'Makes explicit, well-explained links to the question',
              'Uses contextual knowledge to help interpret the sources'] },
        { n: 3, lo: 11, hi: 15, head: 'Uses the sources to support and challenge',
          desc: 'Makes points from the sources to both challenge and support the statement; may misread one or two sources; may select appropriate material and make implicit links to the question; comments on nature, origin or purpose are in the form of bias or reliability comments not based on contextual understanding.',
          f: ['Makes points from the sources on both sides (support and challenge)',
              'Selects appropriate material from the sources and links it to the question, at least implicitly'] },
        { n: 2, lo: 6, hi: 10, head: 'Uses the sources to support or challenge',
          desc: 'Valid points from the sources to either support or challenge the statement; may attempt both, but the sources on one side are misread or misrepresented; may argue that all the sources support or all challenge the statement.',
          need: 1,
          f: ['Makes valid points from the sources on one side only (support or challenge)',
              'Attempts both sides, but the sources on one side are misread or misrepresented',
              'Argues that all the sources support (or all challenge) the statement'] },
        { n: 1, lo: 1, hi: 5, head: 'General use of the sources',
          desc: 'Describes the content of the sources without showing support or challenge; or presents an essay about the topic illustrated by the sources but not focused on the question; or asserts that sources support or challenge without reference to their content.',
          need: 1,
          f: ['Describes the content of the sources without showing how they support or challenge the statement',
              'Writes an essay about the topic, with the sources as illustration',
              'Asserts that sources support or challenge the statement without reference to their content'] }
      ]
    },
    {
      key: 'p2a', tab: 'P2 (a)', name: 'Paper 2 part (a)', title: 'explain why', marks: 10, table: 'Table A', aos: 'AO1, AO2',
      levels: [
        { n: 4, lo: 9, hi: 10, head: 'Connects factors to reach a reasoned conclusion',
          desc: 'Well focused and explains a range of factors supported by relevant information; demonstrates a clear understanding of the connections between causes; reaches a supported conclusion.',
          f: ['Stays well focused and explains a range of factors, supported by relevant information',
              'Shows clear understanding of the connections between the causes',
              'Reaches a supported conclusion'] },
        { n: 3, lo: 6, hi: 8, head: 'Explains factor(s)',
          desc: 'Demonstrates good knowledge and understanding of the demands of the question; includes explained factor(s) supported by relevant information.',
          f: ['Shows good knowledge and understanding of what the question demands',
              'Explains one or more factors, supported by relevant information'] },
        { n: 2, lo: 3, hi: 5, head: 'Describes factor(s)',
          desc: 'Shows some knowledge and understanding of the demands of the question (they address causation); may be entirely descriptive in approach, with description of factor(s).',
          f: ['Describes one or more factors, with some knowledge',
              'Addresses causation, even if the approach is entirely descriptive'] },
        { n: 1, lo: 1, hi: 2, head: 'Describes the topic or issue',
          desc: 'Contains some relevant material about the topic or issue but is descriptive in nature, with no reference to causation.',
          f: ['Describes the topic or issue, with relevant material but no reference to causation'] }
      ]
    },
    {
      key: 'p2b', tab: 'P2 (b)', name: 'Paper 2 part (b)', title: 'how far / to what extent', marks: 20, table: 'Table B', aos: 'AO1, AO2',
      levels: [
        { n: 5, lo: 17, hi: 20, head: 'A comparative judgement based on analysis of the alternative perspectives',
          desc: 'Well focused, with clear analysis that supports and challenges; consistently supported by relevant, detailed evidence; reaches a clear comparative judgement of the relative strength of the perspectives.',
          f: ['Stays well focused on the question throughout',
              'Analyses clearly, both supporting and challenging the view (alternative perspectives)',
              'Supports the analysis consistently with relevant, detailed evidence',
              'Reaches a clear comparative judgement of the relative strength of the perspectives'] },
        { n: 4, lo: 13, hi: 16, head: 'Explanation that considers alternative perspectives',
          desc: 'Supports and challenges the view, explaining alternative perspectives; mostly relevant, detailed evidence; may form a conclusion that lacks a clear comparative judgement.',
          f: ['Explains alternative perspectives, supporting and challenging the view',
              'Supports the explanation with mostly relevant, detailed evidence'] },
        { n: 3, lo: 9, hi: 12, head: 'Explanation of a single perspective',
          desc: 'Explains a single perspective, supporting or challenging the view, with mostly relevant evidence; other perspectives are described rather than explained.',
          f: ['Explains a single perspective, supporting or challenging the view',
              'Supports that single perspective with mostly relevant evidence'] },
        { n: 2, lo: 5, hi: 8, head: 'Considers aspects of the question without explanation',
          desc: 'Relevant description with few explicit links to the question; valid assertions with limited support.',
          need: 1,
          f: ['Describes relevant material about aspects of the question, with few explicit links to it',
              'Makes valid assertions with only limited support'] },
        { n: 1, lo: 1, hi: 4, head: 'General information loosely linked to the question',
          desc: 'General information that is loosely linked to the question; fragmentary points; unsupported assertions.',
          need: 1,
          f: ['Gives general information only loosely linked to the question',
              'Makes fragmentary points or unsupported assertions'] }
      ]
    },
    {
      key: 'p3a', tab: 'P3 A', name: 'Paper 3 Table A', title: 'interpretation and approach (AO4)', marks: 20, table: 'Table A', aos: 'AO4',
      pair: 'p3b', paper: 'Paper 3', paperMarks: 40,
      levels: [
        { n: 6, lo: 18, hi: 20, head: 'Complete understanding of the interpretation and approach',
          desc: 'Detailed, accurate use of the extract; complete understanding of the interpretation and of the approach(es); explains all elements of the interpretation.',
          f: ['Uses the extract in detail and accurately',
              'Shows complete understanding of the interpretation and the approach(es)',
              'Explains all elements of the interpretation'] },
        { n: 5, lo: 15, hi: 17, head: 'Sound understanding, engages with elements of the interpretation',
          desc: 'Detailed, accurate use of the extract; sound understanding of the interpretation and approach; engages with elements of the interpretation without explaining it as a whole (may cover less important sub-messages).',
          f: ['Uses the extract in detail and accurately',
              'Shows sound understanding of the interpretation and approach',
              'Engages with elements of the interpretation, though not yet explaining it as a whole'] },
        { n: 4, lo: 12, hi: 14, head: 'Partial understanding',
          desc: 'Uses the extract but shows partial understanding; identifies elements of the interpretation without adequately explaining them, often treating less important messages as equally or more important.',
          f: ['Uses the extract, with partial understanding of the interpretation',
              'Identifies elements of the interpretation without adequately explaining them'] },
        { n: 3, lo: 9, hi: 11, head: 'Understands that the extract contains interpretations, but explains only sub-messages',
          desc: 'Understands that the extract contains interpretations but explains only sub-messages; or uses part of the extract to argue for an interpretation that the whole does not support; or argues a different interpretation in each paragraph.',
          need: 1,
          f: ['Explains only sub-messages of the extract as interpretations',
              'Uses part of the extract to argue for an interpretation the whole does not support',
              'Argues a different interpretation in each paragraph'] },
        { n: 2, lo: 5, hi: 8, head: 'Summarises the main points',
          desc: 'Summarises the main points of the extract; explanations of the extract as an interpretation lack validity.',
          f: ['Summarises the main points of the extract, with explanations of it as an interpretation that lack validity'] },
        { n: 1, lo: 1, hi: 4, head: 'References to some aspects',
          desc: 'References to some aspects of the extract; fragments of relevant material.',
          f: ['Refers to some aspects of the extract, with fragments of relevant material'] }
      ]
    },
    {
      key: 'p3b', tab: 'P3 B', name: 'Paper 3 Table B', title: 'knowledge (AO1)', marks: 20, table: 'Table B', aos: 'AO1',
      pair: 'p3a', paper: 'Paper 3', paperMarks: 40,
      levels: [
        { n: 6, lo: 18, hi: 20, head: 'Detailed, accurate and entirely relevant knowledge',
          desc: 'Detailed and accurate knowledge that is entirely relevant.',
          f: ['Knowledge is detailed and accurate', 'Knowledge is entirely relevant'] },
        { n: 5, lo: 15, hi: 17, head: 'Detailed, mostly accurate, mainly relevant',
          desc: 'Detailed and mostly accurate knowledge, mainly relevant.',
          f: ['Knowledge is detailed and mostly accurate', 'Knowledge is mainly relevant'] },
        { n: 4, lo: 12, hi: 14, head: 'Mostly relevant and accurate',
          desc: 'Mostly relevant and accurate knowledge.',
          f: ['Knowledge is mostly accurate', 'Knowledge is mostly relevant'] },
        { n: 3, lo: 9, hi: 11, head: 'Generally accurate and relevant',
          desc: 'Generally accurate and relevant knowledge.',
          f: ['Knowledge is generally accurate', 'Knowledge is generally relevant'] },
        { n: 2, lo: 5, hi: 8, head: 'Some accurate and relevant knowledge',
          desc: 'Some accurate and relevant knowledge.',
          f: ['Some accurate and relevant knowledge'] },
        { n: 1, lo: 1, hi: 4, head: 'Limited knowledge',
          desc: 'Limited knowledge.',
          f: ['Limited knowledge'] }
      ]
    },
    {
      key: 'p4a', tab: 'P4 A', name: 'Paper 4 Table A', title: 'analysis and judgement (AO2)', marks: 15, table: 'Table A', aos: 'AO2',
      pair: 'p4b', paper: 'Paper 4', paperMarks: 30,
      levels: [
        { n: 5, lo: 13, hi: 15, head: 'Full understanding, balanced and analytical',
          desc: 'Valid, wide-ranging criteria; consistently analytical; a focused, balanced argument with sustained reasoning; a clear, sustained, supported judgement.',
          f: ['Shows full understanding and is consistently analytical',
              'Uses valid, wide-ranging criteria',
              'Argues in a focused, balanced way with sustained reasoning',
              'Reaches a clear, sustained, supported judgement'] },
        { n: 4, lo: 10, hi: 12, head: 'Good understanding, mostly analytical',
          desc: 'Valid criteria; analysis may be uneven; an attempted balance may lack coherence in places; a supported judgement, though some evaluations may be only partly substantiated.',
          f: ['Shows good understanding and is mostly analytical (the analysis may be uneven)',
              'Uses valid criteria',
              'Attempts a balanced argument (it may lack coherence in places)',
              'Reaches a supported judgement (some evaluations only partly substantiated)'] },
        { n: 3, lo: 7, hi: 9, head: 'Understanding with some analysis; argument lacks balance',
          desc: 'Attempts at criteria; some description; begins to form a judgement with weak substantiation; the argument lacks balance.',
          f: ['Shows understanding with some analysis (some description remains)',
              'Makes attempts at criteria',
              'Begins to form a judgement, though weakly substantiated'] },
        { n: 2, lo: 4, hi: 6, head: 'Some understanding, descriptive',
          desc: 'Implicit criteria; limited analysis; an inconsistent argument; assertion rather than judgement.',
          f: ['Shows some understanding but is mainly descriptive, with limited analysis',
              'Uses implicit criteria, and the argument is inconsistent',
              'Offers assertion rather than judgement'] },
        { n: 1, lo: 1, hi: 3, head: 'Addresses the topic, not the question',
          desc: 'Descriptive, with no analysis or argument and no relevant judgement.',
          f: ['Addresses the topic rather than the question: description, no analysis or argument, no relevant judgement'] }
      ]
    },
    {
      key: 'p4b', tab: 'P4 B', name: 'Paper 4 Table B', title: 'supporting knowledge (AO1)', marks: 15, table: 'Table B', aos: 'AO1',
      pair: 'p4a', paper: 'Paper 4', paperMarks: 30,
      levels: [
        { n: 5, lo: 13, hi: 15, head: 'High level of relevant detail',
          desc: 'A high level of relevant detail: carefully selected, fully focused on the argument, wide-ranging, consistently precise and accurate.',
          f: ['Detail is carefully selected and fully focused on the argument',
              'Knowledge is wide-ranging and consistently precise and accurate'] },
        { n: 4, lo: 10, hi: 12, head: 'Good level of relevant detail',
          desc: 'A good level of detail: appropriately selected, mostly focused; a range of points with uneven depth; mostly precise.',
          f: ['Detail is appropriately selected and mostly focused on the argument',
              'Covers a range of points, with uneven depth, and is mostly precise'] },
        { n: 3, lo: 7, hi: 9, head: 'Adequate level of relevant detail',
          desc: 'Adequate detail: mostly appropriate, descriptive in places, a narrow range, occasionally imprecise.',
          f: ['Detail is mostly appropriate, though descriptive in places',
              'Range is narrow, and the answer is occasionally imprecise'] },
        { n: 2, lo: 4, hi: 6, head: 'Some relevant detail',
          desc: 'Some relevant detail: narrative, not linked to the argument, limited range and depth, frequently imprecise.',
          f: ['Gives some relevant detail, but as narrative not linked to the argument',
              'Range and depth are limited and the answer is frequently imprecise'] },
        { n: 1, lo: 1, hi: 3, head: 'Limited knowledge',
          desc: 'Limited knowledge: limited relevance, inaccurate or vague.',
          f: ['Knowledge is limited, of limited relevance, inaccurate or vague'] }
      ]
    }
  ];

  var QUALITY = [
    { key: 'just', label: 'Just meets the level' },
    { key: 'adequately', label: 'Adequately meets it' },
    { key: 'convincingly', label: 'Convincingly meets it' }
  ];

  function partByKey(k) {
    for (var i = 0; i < PARTS.length; i++) if (PARTS[i].key === k) return PARTS[i];
    return null;
  }

  function need(level) { return typeof level.need === 'number' ? level.need : level.f.length; }

  // ticks: array of arrays of booleans, ticks[li][fi] (li = index in part.levels, top level first)
  function emptyTicks(part) { return part.levels.map(function (lv) { return lv.f.map(function () { return false; }); }); }

  // a level's own features: enough of them ticked (its `need`)
  function ownMet(part, ticks, i) {
    var count = 0;
    for (var j = 0; j < part.levels[i].f.length; j++) if (ticks[i] && ticks[i][j]) count++;
    return count >= need(part.levels[i]);
  }

  // best-fit level: the highest level that is met, where a level counts as met only when its own features are ticked
  // AND the level below it is met too (the lowest level needs only its own). Returns the index in part.levels, or -1 for Level 0
  function bestFit(part, ticks) {
    var best = -1;
    for (var i = part.levels.length - 1; i >= 0; i--) {
      if (!ownMet(part, ticks, i)) break;
      best = i;
    }
    return best;
  }

  // true when features of a level above index ni are ticked enough but cannot count because level ni (or one below) is not met
  function blockedAbove(part, ticks, ni) {
    for (var i = 0; i < ni; i++) if (ownMet(part, ticks, i)) return true;
    return false;
  }

  // marks [min, max] for a level index and quality key (specimen guidance: highest / middle / lowest mark)
  function markRange(part, li, q) {
    if (li < 0) return [0, 0];
    var lv = part.levels[li];
    if (q === 'just') return [lv.lo, lv.lo];
    if (q === 'convincingly') return [lv.hi, lv.hi];
    if (lv.hi - lv.lo < 2) return [lv.lo, lv.hi];     // no middle mark in a two-mark level
    return [lv.lo + 1, lv.hi - 1];
  }

  function rangeText(r) { return r[0] === r[1] ? String(r[0]) : r[0] + ' to ' + r[1]; }
  function rangeDash(lo, hi) { return lo === hi ? String(lo) : lo + '–' + hi; }

  // what the answer still needs to reach the level above li (li = -1 means Level 0: next is the lowest level)
  function nextUp(part, ticks, li) {
    var ni = li < 0 ? part.levels.length - 1 : li - 1;
    if (ni < 0) return null;
    var lv = part.levels[ni];
    var have = 0;
    var missing = [];
    lv.f.forEach(function (t, j) { if (ticks[ni][j]) have++; else missing.push(t); });
    return { level: lv, index: ni, missing: missing, still: Math.max(0, need(lv) - have), anyOf: need(lv) < lv.f.length };
  }

  // pseudo-random order of the features of a part, the same every time (so no level can be guessed from the order)
  function featureOrder(part) {
    var items = [];
    part.levels.forEach(function (lv, li) { lv.f.forEach(function (t, fi) { items.push({ li: li, fi: fi, text: t }); }); });
    var seed = 7;
    for (var c = 0; c < part.key.length; c++) seed = (seed * 31 + part.key.charCodeAt(c)) % 2147483647;
    function rnd() { seed = (seed * 48271) % 2147483647; return seed / 2147483647; }
    for (var i = items.length - 1; i > 0; i--) {
      var k = Math.floor(rnd() * (i + 1));
      var tmp = items[i]; items[i] = items[k]; items[k] = tmp;
    }
    return items;
  }

  function parseParts(raw) {
    var keys = [];
    var bad = [];
    String(raw || '').split(',').forEach(function (s) {
      var k = s.trim().toLowerCase();
      if (!k) return;
      if (partByKey(k)) { if (keys.indexOf(k) < 0) keys.push(k); } else bad.push(k);
    });
    return { keys: keys, bad: bad };
  }

  var core = { PARTS: PARTS, QUALITY: QUALITY, partByKey: partByKey, emptyTicks: emptyTicks, bestFit: bestFit, markRange: markRange, nextUp: nextUp, featureOrder: featureOrder, blockedAbove: blockedAbove, parseParts: parseParts, need: need };
  try { W.__histLevelsCore = core; } catch (e) { /* the helper object is only a test hook */ }

  W.register('hist-levels', function (el, opts) {
    var get = function (k) { return el.getAttribute('data-' + k) || (opts && (opts[k] || opts['data-' + k])) || ''; };
    var frame = W.frame(el, 'Mark-band explorer', 'Tick what an answer does, and see the level and marks the descriptors would give it.');
    var body = frame.body;

    function mk(tag, props) {
      var n = document.createElement(tag);
      var p = props || {};
      Object.keys(p).forEach(function (k) {
        if (k === 'text') n.textContent = p[k];
        else if (k === 'style') Object.assign(n.style, p[k]);
        else if (k === 'class') n.className = p[k];
        else if (k.slice(0, 2) === 'on') n[k] = p[k];
        else n.setAttribute(k, p[k]);
      });
      for (var i = 2; i < arguments.length; i++) {
        var c = arguments[i];
        if (c) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
      }
      return n;
    }

    var parsed = parseParts(get('parts'));
    var keys = parsed.keys.length ? parsed.keys : PARTS.map(function (p) { return p.key; });
    if (parsed.bad.length) {
      body.appendChild(mk('p', { class: 'w-err', role: 'alert', text: 'Unknown part ignored: ' + parsed.bad.slice(0, 4).join(', ') + '. Use p1a, p1b, p2a, p2b, p3a, p3b, p4a or p4b.' }));
    }
    var startKey = get('start').trim().toLowerCase();
    var current = keys.indexOf(startKey) >= 0 ? startKey : keys[0];

    // state per part: ticks and quality
    var state = {};
    keys.forEach(function (k) { state[k] = { ticks: emptyTicks(partByKey(k)), q: 'adequately' }; });
    // the partner table of a Paper 3 or 4 part is kept even when it is not offered, so the total always has both
    function stateOf(k) {
      if (!state[k]) state[k] = { ticks: emptyTicks(partByKey(k)), q: 'adequately' };
      return state[k];
    }

    // --- part tabs ---
    var tabGroup = mk('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Choose the paper and part' });
    var tabBtns = {};
    keys.forEach(function (k) {
      var part = partByKey(k);
      var b = mk('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false', 'aria-label': part.name + ': ' + part.title, text: part.tab });
      b.onclick = function () { current = k; render(); };
      tabBtns[k] = b;
      tabGroup.appendChild(b);
    });
    body.appendChild(mk('div', { class: 'w-row' }, tabGroup));

    var heading = mk('p', { style: { margin: '8px 0 4px', fontWeight: '600' } });
    body.appendChild(heading);

    // --- feature list ---
    var fs = mk('fieldset', { style: { border: '1px solid var(--rule)', borderRadius: '8px', padding: '8px 10px', margin: '6px 0', minWidth: '0' } });
    var legend = mk('legend', { class: 'w-lab', style: { padding: '0 4px', color: 'var(--ink-2)' }, text: 'Tick everything the answer does' });
    fs.appendChild(legend);
    var list = mk('div');
    fs.appendChild(list);
    body.appendChild(fs);

    // --- quality of fit ---
    var qLab = mk('span', { class: 'w-lab', style: { color: 'var(--ink-2)' }, text: 'Within its level, the answer:' });
    var qGroup = mk('div', { class: 'w-tabs', role: 'group', 'aria-label': 'How well the answer meets its level' });
    var qBtns = {};
    QUALITY.forEach(function (q) {
      var b = mk('button', { type: 'button', class: 'w-tab', 'aria-pressed': 'false', text: q.label });
      b.onclick = function () { stateOf(current).q = q.key; update(true); };
      qBtns[q.key] = b;
      qGroup.appendChild(b);
    });
    var resetBtn = mk('button', { type: 'button', class: 'btn btn-sec btn-sm', text: 'Clear the ticks' });
    resetBtn.onclick = function () {
      stateOf(current).ticks = emptyTicks(partByKey(current));
      renderList();
      update(true);
    };
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, qLab, qGroup));

    // --- results ---
    var summary = mk('p', { 'aria-live': 'polite', 'aria-atomic': 'true', style: { margin: '0 0 6px', fontWeight: '700', color: 'var(--sc)' } });
    var markLine = mk('p', { style: { margin: '0 0 6px' } });
    var descLine = mk('p', { style: { margin: '0 0 6px', color: 'var(--ink-2)' } });
    var upHead = mk('p', { style: { margin: '0 0 2px', fontWeight: '600' } });
    var upList = mk('ul', { style: { margin: '0 0 6px', paddingLeft: '20px' } });
    var totalLine = mk('p', { style: { margin: '6px 0 0', fontWeight: '600', display: 'none' } });
    var panel = mk('div', { style: { border: '1px solid var(--rule)', borderLeft: '4px solid var(--sc)', borderRadius: '8px', padding: '10px 12px', margin: '8px 0', background: 'var(--card)' } },
      summary, markLine, descLine, upHead, upList, totalLine);
    body.appendChild(panel);
    body.appendChild(mk('div', { class: 'w-row', style: { alignItems: 'center', gap: '8px' } }, resetBtn));
    body.appendChild(mk('p', { class: 'w-note', text: 'This explorer is stricter than an examiner: it counts a level only when every level below it is met too. A real examiner takes the best fit, judging the whole answer, so an answer strong on a higher feature may be placed higher. Use it to see which descriptors an answer lacks, not to predict an exact mark. Marks are whole numbers and are never deducted. Try: tick only the lowest-level features, then add features one at a time and watch the level change.' }));

    function renderList() {
      var part = partByKey(current);
      var st = stateOf(current);
      list.textContent = '';
      featureOrder(part).forEach(function (it) {
        var cb = mk('input', { type: 'checkbox', style: { flex: '0 0 auto', width: '18px', height: '18px', margin: '2px 0 0' } });
        cb.checked = !!st.ticks[it.li][it.fi];
        cb.onchange = function () { st.ticks[it.li][it.fi] = cb.checked; update(true); };
        var row = mk('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'flex-start', gap: '8px', margin: '4px 0', cursor: 'pointer' } }, cb, mk('span', { class: 'w-lab', style: { color: 'var(--ink)', fontWeight: '400', fontSize: '0.95em' }, text: it.text }));
        list.appendChild(row);
      });
    }

    function pairTotal(part) {
      if (!part.pair || keys.indexOf(part.pair) < 0) return null;
      var other = partByKey(part.pair);
      var a = partByKey(current), sa = stateOf(a.key);
      var sb = stateOf(other.key);
      var ra = markRange(a, bestFit(a, sa.ticks), sa.q);
      var rb = markRange(other, bestFit(other, sb.ticks), sb.q);
      return [ra[0] + rb[0], ra[1] + rb[1]];
    }

    function update(announce) {
      var part = partByKey(current);
      var st = stateOf(current);
      var li = bestFit(part, st.ticks);
      keys.forEach(function (k) { tabBtns[k].setAttribute('aria-pressed', k === current ? 'true' : 'false'); });
      QUALITY.forEach(function (q) { qBtns[q.key].setAttribute('aria-pressed', q.key === st.q ? 'true' : 'false'); });
      heading.textContent = part.name + ': ' + part.title + ' [' + part.marks + '] · ' + part.table + ' · ' + part.aos;

      upList.textContent = '';
      if (li < 0) {
        summary.textContent = 'Level 0 · 0 marks · no creditable response yet';
        markLine.textContent = 'Nothing is ticked that meets the lowest level, so this answer would get 0 of ' + part.marks + '.';
        descLine.textContent = 'Level 0: no creditable response; no engagement with the task.';
      } else {
        var lv = part.levels[li];
        var r = markRange(part, li, st.q);
        var qtext = st.q === 'just' ? 'just meets the level, so the lowest mark' : st.q === 'convincingly' ? 'convincingly meets the level, so the highest mark' : (lv.hi - lv.lo < 2 ? 'adequately meets the level; a two-mark level has no separate middle mark' : 'adequately meets the level, so a middle mark');
        summary.textContent = 'Level ' + lv.n + ' · ' + rangeText(r) + ' of ' + part.marks + ' marks · ' + lv.head;
        markLine.textContent = 'Level ' + lv.n + ' is worth ' + rangeDash(lv.lo, lv.hi) + ' marks. This answer ' + qtext + ': ' + rangeText(r) + '.';
        descLine.textContent = 'The level in the mark scheme: ' + lv.desc;
      }
      var nx = nextUp(part, st.ticks, li);
      if (!nx) {
        upHead.textContent = 'This is the top level. Within it, the mark depends on how fully the answer meets every feature.';
      } else {
        var lead = nx.anyOf
          ? 'To reach Level ' + nx.level.n + ' (' + rangeDash(nx.level.lo, nx.level.hi) + ') the answer needs ' + (nx.still === 1 ? 'at least one' : nx.still) + ' of:'
          : 'To reach Level ' + nx.level.n + ' (' + rangeDash(nx.level.lo, nx.level.hi) + ') the answer must also:';
        if (blockedAbove(part, st.ticks, nx.index)) lead = 'Features ticked in higher levels do not count here until the level below them is met (an examiner using best fit may still credit them). ' + lead;
        upHead.textContent = lead;
        var show = nx.anyOf ? nx.level.f : nx.missing;
        show.forEach(function (t) { upList.appendChild(mk('li', { text: t })); });
      }

      var tot = pairTotal(part);
      if (tot) {
        totalLine.style.display = '';
        totalLine.textContent = part.paper + ' question total, Table A + Table B (both tables mark the same answer): ' + rangeText(tot) + ' of ' + part.paperMarks + '. Switch tables to set the other half.';
      } else {
        totalLine.style.display = 'none';
        totalLine.textContent = '';
      }
    }

    function render() { renderList(); update(false); }
    render();

    // test hook (no effect on readers)
    el.__histLevels = {
      core: core,
      current: function () { return current; },
      select: function (k) { if (keys.indexOf(k) >= 0) { current = k; render(); } },
      tick: function (li, fi, on) { stateOf(current).ticks[li][fi] = !!on; renderList(); update(true); },
      quality: function (q) { stateOf(current).q = q; update(true); },
      text: function () { return summary.textContent; }
    };
  });
})();
