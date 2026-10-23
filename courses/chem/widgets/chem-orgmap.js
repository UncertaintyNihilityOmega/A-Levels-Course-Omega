/* widgets/chem-orgmap.js: the organic reaction map. Click a functional group to see what makes it and what it turns into,
   or choose a start and a target to list the shortest routes (up to 4 steps, at most three).
   Attributes: data-level="as" (default) or "a2" (AS + A Level); data-focus="alkene" (a group name such as alkene, alcohol,
   halogenoalkane, phenol, carboxylic acid; "alcohol" opens the primary alcohol).
   Data: FACTS.md topics 14 to 21 and 29 to 36 (the reaction lists in packages/P12.md). DOM only: no canvas. */
(function () {
  'use strict';

  const FAM = {
    hydro: 'Hydrocarbons',
    hal: 'Halogen and nitrogen compounds',
    alc: 'Hydroxy compounds',
    carb: 'Carbonyl compounds, acids and derivatives',
    oth: 'Polymers and other products'
  };
  const FAM_ORDER = ['hydro', 'hal', 'alc', 'carb', 'oth'];

  // id, label, level, family, note
  const NODES = [
    ['alkane', 'alkane', 'as', 'hydro', 'Saturated: only C–C and C–H bonds. Unreactive except for combustion and free-radical substitution.'],
    ['alkene', 'alkene', 'as', 'hydro', 'Contains C=C. Decolourises bromine water (orange to colourless).'],
    ['polyalkene', 'poly(alkene)', 'as', 'hydro', 'Addition polymer: the repeat unit is the alkene with its double bond opened.'],
    ['arene', 'arene (benzene)', 'a2', 'hydro', 'Delocalised ring: electrophilic substitution, not addition.'],
    ['alkylbz', 'alkylbenzene', 'a2', 'hydro', 'A benzene ring with an alkyl side chain, such as methylbenzene. UV light and Cl₂ or Br₂ substitute in the side chain.'],
    ['cyclohexane', 'cyclohexane', 'a2', 'hydro', 'Made by adding hydrogen to the benzene ring.'],
    ['halo', 'halogenoalkane', 'as', 'hal', 'Polar C–X bond: the junction of the map. The halogen can be swapped for OH, CN or NH₂, or removed to give an alkene.'],
    ['nitrile', 'nitrile', 'as', 'hal', 'R–C≡N. One more carbon than the halogenoalkane it was made from.'],
    ['hnitrile', 'hydroxynitrile', 'as', 'hal', 'Has OH and CN on the same carbon. One more carbon than the carbonyl compound.'],
    ['amine', 'amine (primary)', 'as', 'hal', 'R–NH₂. A weak base.'],
    ['amine2', 'amine (secondary)', 'a2', 'hal', 'R–NH–R′.'],
    ['haloarene', 'halogenoarene', 'a2', 'hal', 'Halogen on the benzene ring. Very unreactive to nucleophiles.'],
    ['nitroarene', 'nitroarene', 'a2', 'hal', 'Nitrobenzene type. Reduced to a phenylamine.'],
    ['phamine', 'phenylamine', 'a2', 'hal', 'An aromatic primary amine, Ar–NH₂.'],
    ['brphamine', '2,4,6-tribromophenylamine', 'a2', 'hal', 'White precipitate from phenylamine and bromine water.'],
    ['diazo', 'diazonium salt', 'a2', 'hal', 'Ar–N₂⁺. Unstable above about 10 °C.'],
    ['azo', 'azo compound', 'a2', 'hal', 'Ar–N=N–Ar′: a coloured dye.'],
    ['amide', 'amide', 'a2', 'hal', 'R–CONH₂ or R–CONHR′.'],
    ['alc1', 'alcohol (primary)', 'as', 'alc', 'CH₂OH group. Oxidised to an aldehyde, then to a carboxylic acid.'],
    ['alc2', 'alcohol (secondary)', 'as', 'alc', 'CH(OH) group. Oxidised to a ketone only.'],
    ['alc3', 'alcohol (tertiary)', 'as', 'alc', 'C(OH) with no hydrogen on that carbon. Not oxidised by acidified dichromate(VI) or KMnO₄.'],
    ['diol', 'diol', 'as', 'alc', 'Two OH groups, as in ethane-1,2-diol.'],
    ['phenol', 'phenol', 'a2', 'alc', 'OH on a benzene ring. Weakly acidic; the ring is activated towards substitution.'],
    ['phenoxide', 'phenoxide', 'a2', 'alc', 'The anion of phenol, C₆H₅O⁻.'],
    ['brphenol', '2,4,6-tribromophenol', 'a2', 'alc', 'White precipitate from phenol and bromine water.'],
    ['nphenol', '2- and 4-nitrophenol', 'a2', 'alc', 'Made with dilute nitric acid at room temperature.'],
    ['ald', 'aldehyde', 'as', 'carb', 'R–CHO. Oxidised by Tollens’ and Fehling’s reagents.'],
    ['ket', 'ketone', 'as', 'carb', 'R–CO–R′. Not oxidised by Tollens’ or Fehling’s reagents.'],
    ['acid', 'carboxylic acid', 'as', 'carb', 'R–COOH. A weak acid that reacts with metals, alkalis and carbonates.'],
    ['salt', 'carboxylate salt', 'as', 'carb', 'R–COO⁻ with a metal ion (or ammonium).'],
    ['ester', 'ester', 'as', 'carb', 'R–COO–R′: sweet-smelling; made from an acid and an alcohol.'],
    ['acylcl', 'acyl chloride', 'a2', 'carb', 'R–COCl. Very reactive; reacts at room temperature.'],
    ['arylket', 'aryl ketone', 'a2', 'carb', 'A ketone with the C=O attached to the ring.'],
    ['benzoic', 'benzoic acid', 'a2', 'carb', 'C₆H₅COOH, made by oxidising a side chain.'],
    ['polyester', 'polyester', 'a2', 'oth', 'Condensation polymer with ester links.'],
    ['polyamide', 'polyamide', 'a2', 'oth', 'Condensation polymer with amide links.'],
    ['aminoacid', 'amino acid', 'a2', 'oth', 'Has both NH₂ and COOH groups.'],
    ['polypeptide', 'polypeptide', 'a2', 'oth', 'Amino acids joined by peptide (amide) links.'],
    ['co2', 'CO₂ + H₂O', 'a2', 'oth', 'The end of oxidation of methanoic acid and ethanedioic acid.']
  ];
  const NODE = {};
  NODES.forEach(n => { NODE[n[0]] = { id: n[0], label: n[1], level: n[2], fam: n[3], note: n[4] }; });

  const ALIASES = {
    alcohol: 'alc1', alcohols: 'alc1', 'primary alcohol': 'alc1', 'secondary alcohol': 'alc2', 'tertiary alcohol': 'alc2',
    'carboxylic acid': 'acid', 'carboxylic acids': 'acid', aldehydes: 'ald', ketones: 'ket', esters: 'ester', nitriles: 'nitrile',
    amines: 'amine', 'primary amine': 'amine', 'secondary amine': 'amine2', alkenes: 'alkene', alkanes: 'alkane',
    halogenoalkane: 'halo', halogenoalkanes: 'halo', haloalkane: 'halo', arenes: 'arene', benzene: 'arene', 'acyl chloride': 'acylcl',
    phenols: 'phenol', 'amino acid': 'aminoacid', 'diazonium': 'diazo', 'diazonium salt': 'diazo', 'hydroxynitrile': 'hnitrile',
    'poly(alkene)': 'polyalkene', polymer: 'polyalkene', 'carboxylate': 'salt', 'carboxylate salt': 'salt', diols: 'diol'
  };
  ALIASES['tertiary alcohol'] = 'alc3';

  const EDGES = [];
  // E(froms, tos, reagents, type, level, note)
  function E(f, t, reagents, type, level, note) {
    (Array.isArray(f) ? f : [f]).forEach(a => (Array.isArray(t) ? t : [t]).forEach(b => {
      EDGES.push({ from: a, to: b, reagents: reagents, type: type, level: level || 'as', note: note || '', addC: /Adds one carbon/.test(note || '') });
    }));
  }
  const OXI = 'acidified K₂Cr₂O₇ or KMnO₄, ';

  // ---- AS ----
  E('alkane', 'halo', 'Cl₂ or Br₂, ultraviolet light', 'free-radical substitution');
  E('alkane', 'alkene', 'heat with Al₂O₃', 'cracking', 'as', 'A long alkane gives a shorter alkane and an alkene.');
  E('alkene', 'alkane', 'H₂(g), Pt or Ni catalyst, heat', 'addition (hydrogenation)');
  E('alkene', 'halo', 'HX(g) at room temperature, or X₂', 'electrophilic addition');
  E('alkene', ['alc1', 'alc2'], 'steam, H₃PO₄ catalyst', 'electrophilic addition', 'as', 'Ethene gives a primary alcohol; other alkenes give mainly the secondary alcohol.');
  E('alkene', 'diol', 'cold, dilute, acidified KMnO₄', 'oxidation');
  E('alkene', ['ket', 'acid'], 'hot, concentrated, acidified KMnO₄', 'oxidation', 'as', 'The C=C bond is split: the products show where the double bond was, and a =CH₂ end gives CO₂.');
  E('alkene', 'polyalkene', 'many alkene molecules, no other reagent', 'addition polymerisation');
  E('halo', ['alc1', 'alc2', 'alc3'], 'NaOH(aq), heat', 'nucleophilic substitution (hydrolysis)', 'as', 'Gives the alcohol of the same class as the halogenoalkane.');
  E('halo', 'nitrile', 'KCN in ethanol, heat under reflux', 'nucleophilic substitution', 'as', 'Adds one carbon atom.');
  E('halo', 'amine', 'excess NH₃ in ethanol, heated under pressure', 'nucleophilic substitution');
  E('halo', 'alkene', 'NaOH in ethanol, heat', 'elimination');
  E(['alc1', 'alc2', 'alc3'], 'halo', 'HX(g); or KCl with concentrated H₂SO₄ or H₃PO₄; or PCl₃ and heat; or PCl₅; or SOCl₂', 'substitution');
  E('alc1', 'ald', OXI + 'heat, distil off the product', 'oxidation');
  E('alc1', 'acid', OXI + 'heat under reflux', 'oxidation');
  E('alc2', 'ket', OXI + 'heat, distil off the product', 'oxidation');
  E(['alc1', 'alc2', 'alc3'], 'alkene', 'heated Al₂O₃, or concentrated H₂SO₄ and heat', 'dehydration (elimination)');
  E(['alc1', 'alc2'], 'ester', 'with a carboxylic acid, concentrated H₂SO₄ catalyst, heat under reflux', 'condensation (esterification)');
  E('acid', 'ester', 'with an alcohol, concentrated H₂SO₄ catalyst, heat under reflux', 'condensation (esterification)');
  E('ald', 'acid', OXI + 'heat under reflux', 'oxidation');
  E('ald', 'alc1', 'NaBH₄ or LiAlH₄', 'reduction');
  E('ket', 'alc2', 'NaBH₄ or LiAlH₄', 'reduction');
  E(['ald', 'ket'], 'hnitrile', 'HCN with KCN catalyst, heat', 'nucleophilic addition', 'as', 'Adds one carbon atom.');
  E('acid', 'alc1', 'LiAlH₄ in dry ether (NaBH₄ is not strong enough)', 'reduction');
  E('acid', 'salt', 'reactive metal, alkali or carbonate', 'acid–base reaction');
  E('salt', 'acid', 'dilute strong acid', 'acid–base reaction (protonation)');
  E(['nitrile', 'hnitrile'], 'acid', 'dilute acid, heat; or dilute alkali, heat, then acidify', 'hydrolysis', 'as', 'A hydroxynitrile gives a hydroxy acid.');
  E('ester', ['acid', 'alc1', 'alc2'], 'dilute acid and heat', 'hydrolysis', 'as', 'Gives the carboxylic acid and the alcohol the ester was made from.');
  E('ester', 'salt', 'dilute alkali and heat', 'hydrolysis', 'as', 'The alcohol is also formed.');

  // ---- A Level ----
  E('arene', 'haloarene', 'Cl₂ or Br₂ with AlCl₃ or AlBr₃ catalyst', 'electrophilic substitution', 'a2');
  E('arene', 'nitroarene', 'concentrated HNO₃ + concentrated H₂SO₄, 25–60 °C', 'electrophilic substitution (nitration)', 'a2');
  E('arene', 'alkylbz', 'CH₃Cl with AlCl₃, heat', 'Friedel–Crafts alkylation', 'a2');
  E('arene', 'arylket', 'CH₃COCl with AlCl₃, heat', 'Friedel–Crafts acylation', 'a2');
  E('arene', 'cyclohexane', 'H₂, Pt or Ni, heat', 'addition (hydrogenation)', 'a2');
  E('alkylbz', 'benzoic', 'hot alkaline KMnO₄, then dilute acid', 'oxidation', 'a2');
  E('nitroarene', 'phamine', 'hot Sn + concentrated HCl, then NaOH(aq)', 'reduction', 'a2');
  E('phamine', 'diazo', 'HNO₂ (or NaNO₂ + dilute acid), below 10 °C', 'diazotisation', 'a2');
  E('diazo', 'phenol', 'warm with water', 'reaction with water (hydrolysis)', 'a2');
  E('diazo', 'azo', 'with phenol, in NaOH(aq)', 'coupling', 'a2');
  E('phenol', 'azo', 'with a diazonium salt, in NaOH(aq)', 'coupling', 'a2');
  E('phenol', 'phenoxide', 'NaOH(aq); or Na(s), giving H₂', 'acid–base reaction', 'a2');
  E('phenol', 'brphenol', 'Br₂(aq)', 'electrophilic substitution', 'a2');
  E('phenol', 'nphenol', 'dilute HNO₃, room temperature', 'electrophilic substitution', 'a2');
  E('phamine', 'brphamine', 'Br₂(aq), room temperature', 'electrophilic substitution', 'a2');
  E(['acid', 'benzoic'], 'acylcl', 'PCl₃ and heat; or PCl₅; or SOCl₂', 'substitution', 'a2');
  E('acylcl', 'acid', 'water, room temperature', 'hydrolysis', 'a2');
  E('acylcl', 'ester', 'an alcohol or phenol, room temperature', 'addition–elimination', 'a2');
  E('acylcl', 'amide', 'NH₃ or a primary or secondary amine, room temperature', 'addition–elimination', 'a2');
  E('amide', 'amine', 'LiAlH₄', 'reduction', 'a2');
  E('amide', 'acid', 'aqueous acid or alkali, heat', 'hydrolysis', 'a2');
  E('nitrile', 'amine', 'LiAlH₄ or H₂ with Ni catalyst', 'reduction', 'a2');
  E(['halo', 'amine'], 'amine2', 'with a primary amine in ethanol, heated in a sealed tube', 'nucleophilic substitution', 'a2');
  E('acid', 'co2', 'methanoic acid: Fehling’s or Tollens’ reagent, or acidified KMnO₄ or K₂Cr₂O₇', 'oxidation', 'a2', 'Only methanoic acid does this.');
  E('acid', 'co2', 'ethanedioic acid: warm acidified KMnO₄', 'oxidation', 'a2', 'Only ethanedioic acid does this.');
  E(['diol', 'acid'], 'polyester', 'a diol with a dicarboxylic acid (or dioyl chloride)', 'condensation polymerisation', 'a2');
  E(['amine', 'acid'], 'polyamide', 'a diamine with a dicarboxylic acid (or dioyl chloride)', 'condensation polymerisation', 'a2');
  E('aminoacid', 'polypeptide', 'heat many amino acid molecules together', 'condensation polymerisation', 'a2');

  const inLevel = (lvl, x) => lvl === 'a2' || x.level === 'as';

  W.register('chem-orgmap', function (el, opts) {
    const { body } = W.frame(el, 'Organic reaction map', 'Pick a functional group, or find a route between two');
    const get = k => (opts[k] === undefined ? '' : String(opts[k]).trim());
    let level = 'as';
    const msgs = [];
    if (get('level')) {
      const l = get('level').toLowerCase();
      if (l === 'as' || l === 'a2') level = l;
      else msgs.push('data-level "' + get('level').slice(0, 20) + '" is not as or a2, so the AS map is shown.');
    }
    let sel = 'halo';
    const f = get('focus').toLowerCase();
    if (f) {
      let id = NODE[f] ? f : ALIASES[f];
      if (!id) {
        const hit = NODES.find(n => n[1].toLowerCase() === f) || NODES.find(n => n[1].toLowerCase().indexOf(f) >= 0);
        if (hit) id = hit[0];
      }
      if (!id) {
        msgs.push('There is no group called "' + get('focus').slice(0, 24) + '" on the map. Showing halogenoalkane instead; click another group.');
      } else if (NODE[id].level === 'a2' && level === 'as') {
        level = 'a2';
        sel = id;
      } else {
        sel = id;
      }
    }
    let from = 'alkene', to = 'acid';
    if (sel !== 'halo' && f) from = sel;
    if (from === to) to = 'alc1';

    const err = W.h('div', { class: 'w-err', role: 'status', text: msgs.join(' ') });
    if (!msgs.length) err.style.display = 'none';
    body.appendChild(err);

    const levelSel = W.h('select', { 'aria-label': 'Level of the map' },
      W.h('option', { value: 'as', text: 'AS reactions only' }),
      W.h('option', { value: 'a2', text: 'AS and A Level reactions' }));
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Show' }), levelSel)));

    const grid = W.h('div');
    body.appendChild(grid);
    const detail = W.h('div', { style: { marginTop: '10px' } });
    body.appendChild(detail);

    // ---- route finder ----
    body.appendChild(W.h('div', { style: { fontWeight: '600', margin: '14px 0 4px' }, text: 'Route finder' }));
    const fromSel = W.h('select', { 'aria-label': 'Start group' });
    const toSel = W.h('select', { 'aria-label': 'Target group' });
    body.appendChild(W.h('div', { class: 'w-row' },
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Start' }), fromSel),
      W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: 'Target' }), toSel)));
    const carbonBox = W.h('input', { type: 'checkbox' });
    body.appendChild(W.h('div', { class: 'w-row' }, W.h('label', { class: 'w-ctl', style: { display: 'flex', alignItems: 'center', gap: '8px' } },
      carbonBox, W.h('span', { class: 'w-lab', text: 'Only routes with a step that adds one carbon atom (a cyanide step)' }))));
    const routes = W.h('div', { style: { marginTop: '6px' } });
    body.appendChild(routes);
    body.appendChild(W.h('div', { class: 'w-note', text: 'Try: start at alkene, target carboxylic acid; then start at alcohol (primary), target carboxylic acid, and tick the carbon box to see the routes that make an acid with one more carbon. A route on the map is possible in principle: check that the carbon skeleton fits your molecule, for example a ketone needs a secondary alcohol.' }));

    const chipStyle = { margin: '2px 4px 2px 0' };

    function visibleNodes() { return NODES.filter(n => inLevel(level, { level: n[2] })); }
    function visibleEdges() { return EDGES.filter(e => inLevel(level, e)); }

    function selectNode(id) { sel = id; draw(); }

    function chip(id, active) {
      const b = W.h('button', { class: 'btn btn-sm' + (active ? '' : ' btn-sec'), type: 'button', text: NODE[id].label, style: chipStyle, onclick: () => selectNode(id) });
      b.setAttribute('aria-pressed', active ? 'true' : 'false');
      return b;
    }

    function drawGrid() {
      grid.innerHTML = '';
      const nodes = visibleNodes();
      FAM_ORDER.forEach(fam => {
        const list = nodes.filter(n => n[3] === fam);
        if (!list.length) return;
        grid.appendChild(W.h('div', { class: 'w-lab', style: { margin: '8px 0 2px' }, text: FAM[fam] }));
        const row = W.h('div', { style: { display: 'flex', flexWrap: 'wrap' } });
        list.forEach(n => row.appendChild(chip(n[0], n[0] === sel)));
        grid.appendChild(row);
      });
    }

    // group edges that share reagents, type and note, joining the other ends
    function grouped(edges, otherKey) {
      const map = new Map();
      edges.forEach(e => {
        const k = e.reagents + '|' + e.type + '|' + e.note;
        if (!map.has(k)) map.set(k, { reagents: e.reagents, type: e.type, note: e.note, ids: [] });
        const g = map.get(k);
        if (g.ids.indexOf(e[otherKey]) < 0) g.ids.push(e[otherKey]);
      });
      return Array.from(map.values());
    }

    function listBlock(title, groups) {
      const box = W.h('div', { style: { marginTop: '6px' } }, W.h('div', { class: 'w-lab', text: title }));
      if (!groups.length) {
        box.appendChild(W.h('div', { style: { color: 'var(--ink-2)', fontSize: '13px' }, text: 'Nothing on this map.' }));
        return box;
      }
      groups.forEach(g => {
        const row = W.h('div', { style: { borderTop: '1px solid var(--rule)', padding: '5px 0' } });
        const names = W.h('div');
        g.ids.forEach(id => names.appendChild(chip(id, false)));
        row.appendChild(names);
        row.appendChild(W.h('div', { style: { fontSize: '13px' }, text: g.reagents }));
        row.appendChild(W.h('div', { style: { fontSize: '13px', color: 'var(--ink-2)' }, text: 'Type: ' + g.type + '.' + (g.note ? ' ' + g.note : '') }));
        box.appendChild(row);
      });
      return box;
    }

    function drawDetail() {
      detail.innerHTML = '';
      const n = NODE[sel];
      const edges = visibleEdges();
      detail.appendChild(W.h('div', { style: { fontWeight: '600' }, text: n.label }));
      detail.appendChild(W.h('div', { style: { fontSize: '13px', color: 'var(--ink-2)' }, text: n.note }));
      detail.appendChild(listBlock('Made from', grouped(edges.filter(e => e.to === sel), 'from')));
      detail.appendChild(listBlock('Turns into', grouped(edges.filter(e => e.from === sel), 'to')));
      const useRow = W.h('div', { class: 'w-row', style: { marginTop: '8px' } },
        W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: 'Use as route start', onclick: () => { from = sel; if (to === from) to = from === 'acid' ? 'alkene' : 'acid'; fillRoute(); } }),
        W.h('button', { class: 'btn btn-sm btn-sec', type: 'button', text: 'Use as route target', onclick: () => { to = sel; if (to === from) from = to === 'alkene' ? 'acid' : 'alkene'; fillRoute(); } }));
      detail.appendChild(useRow);
    }

    function fillSelects() {
      const nodes = visibleNodes();
      [fromSel, toSel].forEach(s => {
        s.innerHTML = '';
        nodes.forEach(n => s.appendChild(W.h('option', { value: n[0], text: n[1] })));
      });
      if (!nodes.some(n => n[0] === from)) from = 'alkene';
      if (!nodes.some(n => n[0] === to)) to = 'acid';
      fromSel.value = from; toSel.value = to;
    }

    // all simple paths of at most 4 steps, shortest first
    function findRoutes(a, b) {
      const edges = visibleEdges();
      const out = new Map();
      const found = [];
      (function dfs(node, path, seen) {
        if (path.length > 4) return;
        if (node === b && path.length > 0) { found.push(path.slice()); return; }
        if (path.length === 4) return;
        edges.forEach(e => {
          if (e.from !== node || seen.indexOf(e.to) >= 0) return;
          path.push(e); seen.push(e.to);
          dfs(e.to, path, seen);
          path.pop(); seen.pop();
        });
      })(a, [], [a]);
      const wantC = carbonBox.checked;
      const usable = (wantC ? found.filter(p => p.some(e => e.addC)) : found.slice());
      usable.sort((p, q) => p.length - q.length);
      found.length = 0;
      usable.forEach(p => found.push(p));
      // merge routes that use the same reagents in the same order (they differ only in the class of an intermediate)
      found.forEach(p => {
        const k = p.map(e => e.reagents + '|' + e.type).join('>');
        if (!out.has(k)) out.set(k, { steps: p.map(e => ({ from: [e.from], to: [e.to], e: e })) });
        else out.get(k).steps.forEach((s, i) => {
          if (s.from.indexOf(p[i].from) < 0) s.from.push(p[i].from);
          if (s.to.indexOf(p[i].to) < 0) s.to.push(p[i].to);
        });
      });
      return Array.from(out.values()).slice(0, 3);
    }

    const names = ids => ids.map(i => NODE[i].label).join(' or ');

    function drawRoutes() {
      routes.innerHTML = '';
      if (from === to) { routes.appendChild(W.h('div', { class: 'w-err', text: 'Choose two different groups.' })); return; }
      const rs = findRoutes(from, to);
      if (!rs.length) {
        routes.appendChild(W.h('div', { text: 'No route in the syllabus within 4 steps' + (carbonBox.checked ? ' that adds a carbon atom' : '') + ' from ' + NODE[from].label + ' to ' + NODE[to].label + '.' }));
        return;
      }
      rs.forEach((r, i) => {
        const box = W.h('div', { style: { borderTop: '1px solid var(--rule)', padding: '6px 0' } });
        box.appendChild(W.h('div', { style: { fontWeight: '600' }, text: 'Route ' + (i + 1) + ' (' + r.steps.length + (r.steps.length === 1 ? ' step)' : ' steps)') }));
        r.steps.forEach((s, j) => {
          const line = W.h('div', { style: { fontSize: '13px', margin: '3px 0' } });
          line.appendChild(W.h('b', { text: (j + 1) + '. ' + names(s.from) + ' → ' + names(s.to) + ': ' }));
          line.appendChild(document.createTextNode(s.e.reagents + '. Type: ' + s.e.type + '.' + (s.e.note ? ' ' + s.e.note : '')));
          box.appendChild(line);
        });
        routes.appendChild(box);
      });
    }

    function fillRoute() { fillSelects(); drawRoutes(); drawDetail(); }

    function draw() {
      if (!NODE[sel] || !inLevel(level, NODE[sel])) sel = 'halo';
      levelSel.value = level;
      drawGrid();
      fillRoute();
    }

    levelSel.addEventListener('change', () => { level = levelSel.value; draw(); });
    fromSel.addEventListener('change', () => { from = fromSel.value; drawRoutes(); });
    toSel.addEventListener('change', () => { to = toSel.value; drawRoutes(); });
    carbonBox.addEventListener('change', drawRoutes);
    draw();
  });
})();
