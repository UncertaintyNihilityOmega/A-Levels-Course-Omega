/* widgets/bio-punnett.js: a Punnett-square calculator. Used in bio.inheritance and bio.dihybrid.
   Four kinds of cross: mono (one gene, dominance), di (two unlinked genes, dominance), xlinked (an X-linked gene: mother X^H X^h..., father X^H Y or X^h Y),
   codom (two codominant alleles C^R and C^W). Model: complete dominance for mono and di, genes unlinked, equal numbers of each gamete from a parent.
   Attributes: data-type = mono | di | xlinked | codom (default mono); data-p1, data-p2 = the two genotypes ("Aa", "AaBb", "XHXh" and "XHY", "CRCW");
   data-ph = comma-separated phenotype labels (mono: dominant,recessive; di: dominant 1,recessive 1,dominant 2,recessive 2; codom: first homozygote,heterozygote,second homozygote).
   Pure functions are exported for data/test_bio-punnett.js. */
(function () {
  'use strict';

  const TYPES = ['mono', 'di', 'xlinked', 'codom'];
  const TYPE_NAME = { mono: 'One gene', di: 'Two genes', xlinked: 'X-linked', codom: 'Codominant' };

  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { const t = a % b; a = b; b = t; } return a || 1; }
  function al(t, sup, rank) { return { t: t, sup: sup || '', rank: rank }; }
  function akey(a) { return a.t + a.sup; }
  function sortGene(g) { return g.slice().sort(function (x, y) { return x.rank - y.rank; }); }
  function gkey(genes, sep) { return genes.map(function (g) { return g.map(akey).join(''); }).join(sep); }

  // ---- building a parent's genotype from the count of dominant alleles in each gene -------------------------------------------
  // letters: {L1, L2} (upper case letters for mono and di). dn: array with one count (0..2) per gene; for the xlinked father 1 = X^H Y, 0 = X^h Y.
  function build(type, who, dn, letters) {
    letters = letters || {};
    const L1 = letters.L1 || 'A', L2 = letters.L2 || 'B';
    function gene(up, dnum) {
      const out = [];
      for (let i = 0; i < 2; i++) out.push(i < dnum ? al(up, '', 0) : al(up.toLowerCase(), '', 1));
      return out;
    }
    if (type === 'mono') return [gene(L1, dn[0])];
    if (type === 'di') return [gene(L1, dn[0]), gene(L2, dn[1])];
    if (type === 'codom') {
      const g = [];
      for (let i = 0; i < 2; i++) g.push(i < dn[0] ? al('C', 'R', 0) : al('C', 'W', 1));
      return [g];
    }
    // xlinked
    if (who === 1) return [[dn[0] ? al('X', 'H', 0) : al('X', 'h', 1), al('Y', '', 2)]];
    const g = [];
    for (let i = 0; i < 2; i++) g.push(i < dn[0] ? al('X', 'H', 0) : al('X', 'h', 1));
    return [g];
  }

  // ---- gametes: every way of taking one allele from each gene; identical gametes are merged and counted ----------------------------
  function gametes(genotype) {
    let list = [[]];
    genotype.forEach(function (gene) {
      const next = [];
      list.forEach(function (pre) { gene.forEach(function (a) { next.push(pre.concat([a])); }); });
      list = next;
    });
    const total = list.length, map = {}, order = [];
    list.forEach(function (g) {
      const k = g.map(akey).join('|');
      if (!map[k]) { map[k] = { alleles: g, w: 0 }; order.push(k); }
      map[k].w++;
    });
    return { list: order.map(function (k) { return map[k]; }), total: total };
  }

  function fertilise(g1, g2) {   // two gametes (arrays of alleles) -> a genotype (array of genes)
    return g1.map(function (a, i) { return sortGene([a, g2[i]]); });
  }

  // ---- phenotype of a genotype -------------------------------------------------------------------------------------------------
  function phenoIndex(type, genotype) {
    if (type === 'mono') return genotype[0][0].rank === 0 ? 0 : 1;
    if (type === 'di') return (genotype[0][0].rank === 0 ? 0 : 2) + (genotype[1][0].rank === 0 ? 0 : 1);
    if (type === 'codom') return genotype[0][0].rank === 0 ? (genotype[0][1].rank === 0 ? 0 : 1) : 2;
    const g = genotype[0];                // xlinked: X X (female) or X Y (male)
    if (g[1].t === 'Y') return g[0].rank === 0 ? 3 : 4;
    return g[0].rank === 0 ? (g[1].rank === 0 ? 0 : 1) : 2;
  }
  function defaultLabels(type, letters) {
    if (type === 'mono') return ['dominant phenotype', 'recessive phenotype'];
    if (type === 'di') return ['dominant 1', 'recessive 1', 'dominant 2', 'recessive 2'];
    if (type === 'codom') return ['red', 'roan', 'white'];
    return ['unaffected female', 'carrier female', 'affected female', 'unaffected male', 'affected male'];
  }
  function phenoName(type, idx, labels) {
    if (type === 'di') {
      const a = idx < 2 ? labels[0] : labels[1], b = idx % 2 === 0 ? labels[2] : labels[3];
      return a + ', ' + b;
    }
    return labels[idx];
  }
  function phenoCount(type) { return type === 'mono' ? 2 : type === 'di' ? 4 : type === 'codom' ? 3 : 5; }

  // ---- a whole cross ------------------------------------------------------------------------------------------------------------
  // p1, p2: genotypes. For xlinked, the father (p2) goes along the top of the square and the mother (p1) down the side.
  function cross(type, p1, p2, labels) {
    const sep = (type === 'xlinked' || type === 'codom') ? ' ' : '';
    const G1 = gametes(p1), G2 = gametes(p2);
    const top = type === 'xlinked' ? G2 : G1, side = type === 'xlinked' ? G1 : G2;
    const cells = [], geno = {}, gorder = [], pheno = [];
    for (let i = 0; i < phenoCount(type); i++) pheno.push(0);
    side.list.forEach(function (s) {
      const row = [];
      top.list.forEach(function (t) {
        const gt = type === 'xlinked' ? fertilise(s.alleles, t.alleles) : fertilise(t.alleles, s.alleles);
        const w = s.w * t.w, k = gkey(gt, sep), pi = phenoIndex(type, gt);
        row.push({ geno: gt, pheno: pi, w: w });
        if (!geno[k]) { geno[k] = { geno: gt, w: 0, pheno: pi }; gorder.push(k); }
        geno[k].w += w;
        pheno[pi] += w;
      });
      cells.push(row);
    });
    const total = top.total * side.total;
    gorder.sort(function (a, b) {          // grouped by phenotype, dominant homozygote first, as in the usual textbook order
      if (geno[a].pheno !== geno[b].pheno) return geno[a].pheno - geno[b].pheno;
      const ra = geno[a].geno.map(function (g) { return g[0].rank + g[1].rank; }), rb = geno[b].geno.map(function (g) { return g[0].rank + g[1].rank; });
      for (let i = 0; i < ra.length; i++) if (ra[i] !== rb[i]) return ra[i] - rb[i];
      return 0;
    });
    return { top: top, side: side, cells: cells, geno: gorder.map(function (k) { return geno[k]; }), pheno: pheno, total: total, sep: sep };
  }

  function ratioOf(ws) {                    // whole-number ratio of a list of weights (zeros left out by the caller)
    let g = 0;
    ws.forEach(function (w) { g = gcd(g, w); });
    return ws.map(function (w) { return w / g; });
  }
  function frac(w, total) { const g = gcd(w, total); return (w / g) + '/' + (total / g); }

  function plainAllele(a) { return a.t + (a.sup ? '^' + a.sup : ''); }
  function plainGeno(genotype, sep) { return genotype.map(function (g) { return g.map(plainAllele).join(sep === ' ' ? ' ' : ''); }).join(sep === ' ' ? ' ' : ''); }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { build: build, gametes: gametes, fertilise: fertilise, cross: cross, phenoIndex: phenoIndex, phenoName: phenoName, phenoCount: phenoCount,
      ratioOf: ratioOf, frac: frac, defaultLabels: defaultLabels, plainGeno: plainGeno, gcd: gcd };
  }
  if (typeof W === 'undefined') return;

  // ---- the widget ------------------------------------------------------------------------------------------------------------------
  W.register('bio-punnett', function (el, opts) {
    opts = opts || {};
    const { body } = W.frame(el, 'Punnett square', 'Choose the parents and read the gametes, the square and the ratios');

    function caps(s) { return (s.match(/[A-Z]/g) || []).length; }
    function parseDn(type, s, who) {
      s = String(s || '');
      if (type === 'mono') { const l = s.match(/[A-Za-z]/g); if (l && l.length === 2) return { dn: [caps(l.join(''))], L1: l[0].toUpperCase() }; }
      if (type === 'di') { const l = s.match(/[A-Za-z]/g); if (l && l.length === 4) return { dn: [caps(l[0] + l[1]), caps(l[2] + l[3])], L1: l[0].toUpperCase(), L2: l[2].toUpperCase() }; }
      if (type === 'codom') { const m = /^C([RW])C([RW])$/.exec(s); if (m) return { dn: [(m[1] === 'R') + (m[2] === 'R')] }; }
      if (type === 'xlinked') {
        if (who === 0) { const m = /^X([Hh])X([Hh])$/.exec(s); if (m) return { dn: [(m[1] === 'H') + (m[2] === 'H')] }; }
        else { const m = /^X([Hh])Y$/.exec(s); if (m) return { dn: [m[1] === 'H' ? 1 : 0] }; }
      }
      return null;
    }
    const startType = TYPES.indexOf(opts.type) >= 0 ? opts.type : 'mono';
    const S = {
      type: startType, show: 'geno',
      letters: { L1: 'A', L2: 'B' },
      dn: { mono: [[1], [1]], di: [[1, 1], [1, 1]], xlinked: [[1], [1]], codom: [[1], [1]] },
      labels: {}
    };
    TYPES.forEach(function (t) { S.labels[t] = defaultLabels(t); });
    [opts.p1, opts.p2].forEach(function (s, who) {
      const r = parseDn(startType, s, who);
      if (r) { S.dn[startType][who] = r.dn; if (r.L1) S.letters.L1 = r.L1; if (r.L2) S.letters.L2 = r.L2; }
    });
    if (typeof opts.ph === 'string') {
      const parts = opts.ph.split(',').map(function (x) { return x.trim(); }).filter(Boolean);
      if (parts.length === phenoCount(startType) && startType !== 'xlinked') S.labels[startType] = parts;
    }

    const tabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'Kind of cross' });
    const tabBtn = {};
    TYPES.forEach(function (t) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': t === S.type ? 'true' : 'false', text: TYPE_NAME[t] });
      b.onclick = function () { S.type = t; TYPES.forEach(function (k) { tabBtn[k].setAttribute('aria-pressed', k === t ? 'true' : 'false'); }); buildControls(); update(); };
      tabBtn[t] = b; tabs.appendChild(b);
    });
    body.appendChild(tabs);

    const controls = W.h('div', { class: 'w-row' });
    const labelRow = W.h('div', { class: 'w-row' });
    const gameteBox = W.h('div', { class: 'w-note', style: { overflowWrap: 'anywhere' } });
    const showTabs = W.h('div', { class: 'w-tabs', role: 'group', 'aria-label': 'What the square shows' });
    const showBtn = {};
    [['geno', 'Genotypes'], ['pheno', 'Phenotypes']].forEach(function (p) {
      const b = W.h('button', { type: 'button', class: 'w-tab', 'aria-pressed': p[0] === S.show ? 'true' : 'false', text: p[1] });
      b.onclick = function () { S.show = p[0]; Object.keys(showBtn).forEach(function (k) { showBtn[k].setAttribute('aria-pressed', k === S.show ? 'true' : 'false'); }); update(); };
      showBtn[p[0]] = b; showTabs.appendChild(b);
    });
    const squareWrap = W.h('div', { style: { overflowX: 'auto', maxWidth: '100%' } });
    const results = W.h('div', { class: 'w-note', style: { overflowWrap: 'anywhere' } });
    const err = W.h('div', { class: 'w-err', role: 'status', 'aria-live': 'polite' });
    const note = W.h('div', { class: 'w-note', text: 'Each box of the square is one equally likely fertilisation. One gene or two: complete dominance, and two genes on different chromosomes. X-linked: the father’s gametes are along the top.' });
    [controls, labelRow, gameteBox, showTabs, squareWrap, results, err, note].forEach(function (n) { body.appendChild(n); });

    function sel(label, options, value, onchange) {
      const s = W.h('select', { 'aria-label': label }, options.map(function (o, i) { return W.h('option', { value: String(o[0]), text: o[1] }); }));
      s.value = String(value);
      s.onchange = function () { onchange(parseInt(s.value, 10)); };
      return s;
    }
    function ctl(label, node) { return W.h('label', { class: 'w-ctl' }, W.h('span', { class: 'w-lab', text: label }), node); }

    function geneOptions(up) { const lo = up.toLowerCase(); return [[2, up + up], [1, up + lo], [0, lo + lo]]; }

    function buildControls() {
      controls.textContent = ''; labelRow.textContent = '';
      const t = S.type, d = S.dn[t], L1 = S.letters.L1, L2 = S.letters.L2;
      function upd() { update(); }
      if (t === 'mono') {
        [0, 1].forEach(function (w) { controls.appendChild(ctl('Parent ' + (w + 1), sel('Genotype of parent ' + (w + 1), geneOptions(L1), d[w][0], function (v) { d[w][0] = v; upd(); }))); });
      } else if (t === 'di') {
        [0, 1].forEach(function (w) {
          controls.appendChild(ctl('Parent ' + (w + 1) + ', gene 1', sel('Parent ' + (w + 1) + ' gene 1', geneOptions(L1), d[w][0], function (v) { d[w][0] = v; upd(); })));
          controls.appendChild(ctl('Parent ' + (w + 1) + ', gene 2', sel('Parent ' + (w + 1) + ' gene 2', geneOptions(L2), d[w][1], function (v) { d[w][1] = v; upd(); })));
        });
      } else if (t === 'codom') {
        const o = [[2, 'C^R C^R'], [1, 'C^R C^W'], [0, 'C^W C^W']];
        [0, 1].forEach(function (w) { controls.appendChild(ctl('Parent ' + (w + 1), sel('Genotype of parent ' + (w + 1), o, d[w][0], function (v) { d[w][0] = v; upd(); }))); });
      } else {
        controls.appendChild(ctl('Mother', sel('Genotype of the mother', [[2, 'X^H X^H (no condition)'], [1, 'X^H X^h (carrier)'], [0, 'X^h X^h (affected)']], d[0][0], function (v) { d[0][0] = v; upd(); })));
        controls.appendChild(ctl('Father', sel('Genotype of the father', [[1, 'X^H Y (unaffected)'], [0, 'X^h Y (affected)']], d[1][0], function (v) { d[1][0] = v; upd(); })));
      }
      const lab = S.labels[t];
      const names = t === 'mono' ? ['Dominant phenotype is called', 'Recessive phenotype is called']
        : t === 'di' ? ['Gene 1 dominant', 'Gene 1 recessive', 'Gene 2 dominant', 'Gene 2 recessive']
        : t === 'codom' ? ['First homozygote is', 'Heterozygote is', 'Second homozygote is'] : [];
      names.forEach(function (nm, i) {
        const inp = W.h('input', { type: 'text', value: lab[i], maxlength: '24', 'aria-label': nm, style: { width: '12em', maxWidth: '100%' } });
        inp.oninput = function () { lab[i] = inp.value; update(); };
        labelRow.appendChild(ctl(nm, inp));
      });
    }

    function genoNodes(genotype, sep) {
      const span = W.h('span');
      genotype.forEach(function (gene, gi) {
        gene.forEach(function (a, ai) {
          if (sep === ' ' && (gi > 0 || ai > 0)) span.appendChild(document.createTextNode(' '));
          span.appendChild(document.createTextNode(a.t));
          if (a.sup) span.appendChild(W.h('sup', { text: a.sup }));
        });
      });
      return span;
    }
    function circle(alleles, sep) {
      const inner = W.h('span');
      alleles.forEach(function (a, i) { inner.appendChild(document.createTextNode(a.t)); if (a.sup) inner.appendChild(W.h('sup', { text: a.sup })); });
      return W.h('span', { style: { display: 'inline-block', border: '1.5px solid var(--ink-2)', borderRadius: '999px', padding: '1px 7px', minWidth: '1.6em', textAlign: 'center' } }, inner);
    }

    function update() {
      const t = S.type, d = S.dn[t];
      err.textContent = '';
      const p1 = build(t, 0, d[0], S.letters), p2 = build(t, 1, d[1], S.letters);
      const labels = S.labels[t].map(function (x, i) { return x && x.trim() ? x.trim().slice(0, 24) : defaultLabels(t)[i]; });
      const c = cross(t, p1, p2, labels);
      const sep = c.sep;

      // gametes
      gameteBox.textContent = '';
      const names = t === 'xlinked' ? ['Mother', 'Father'] : ['Parent 1', 'Parent 2'];
      [[p1, names[0]], [p2, names[1]]].forEach(function (pp) {
        const G = gametes(pp[0]);
        const line = W.h('div', {}, W.h('strong', { text: pp[1] + ' (' + plainGeno(pp[0], sep) + ') makes gametes: ' }));
        G.list.forEach(function (g) {
          line.appendChild(circle(g.alleles, sep));
          line.appendChild(document.createTextNode(' ' + frac(g.w, G.total) + '   '));
        });
        gameteBox.appendChild(line);
      });

      // the square
      squareWrap.textContent = '';
      const th = { style: { textAlign: 'center', padding: '3px 4px' } };
      const tbl = W.h('table', { style: { tableLayout: 'auto', fontSize: '12px', textAlign: 'center', margin: '4px 0', maxWidth: '100%' } });
      tbl.setAttribute('aria-label', 'Punnett square');
      const head = W.h('tr', {}, W.h('th', { scope: 'col', style: { padding: '3px 4px' } }, W.h('span', { class: 'sr-only', text: 'Gametes of the side parent, down' })));
      c.top.list.forEach(function (g) { head.appendChild(W.h('th', { scope: 'col', style: th.style }, circle(g.alleles, sep))); });
      tbl.appendChild(W.h('thead', {}, head));
      const tb = W.h('tbody');
      c.side.list.forEach(function (s, ri) {
        const row = W.h('tr', {}, W.h('th', { scope: 'row', style: th.style }, circle(s.alleles, sep)));
        c.cells[ri].forEach(function (cell) {
          const td = W.h('td', { style: { padding: '4px 5px', minWidth: '40px', overflowWrap: 'anywhere', textAlign: 'center' } });
          if (S.show === 'geno') td.appendChild(genoNodes(cell.geno, sep));
          else td.appendChild(W.h('span', { style: { fontSize: '11px' }, text: phenoName(t, cell.pheno, labels) }));
          row.appendChild(td);
        });
        tb.appendChild(row);
      });
      tbl.appendChild(tb);
      squareWrap.appendChild(tbl);

      // ratios
      results.textContent = '';
      const gl = c.geno.filter(function (g) { return g.w > 0; });
      const gr = ratioOf(gl.map(function (g) { return g.w; }));
      const gline = W.h('div', {}, W.h('strong', { text: 'Genotypes: ' }));
      gl.forEach(function (g, i) {
        if (i) gline.appendChild(document.createTextNode(' : '));
        gline.appendChild(document.createTextNode(gr[i] + ' '));
        gline.appendChild(genoNodes(g.geno, sep));
      });
      results.appendChild(gline);
      const pidx = [];
      c.pheno.forEach(function (w, i) { if (w > 0) pidx.push(i); });
      const pr = ratioOf(pidx.map(function (i) { return c.pheno[i]; }));
      const ptxt = pidx.map(function (i, k) { return pr[k] + ' ' + phenoName(t, i, labels); }).join(' : ');
      results.appendChild(W.h('div', {}, W.h('strong', { text: 'Phenotypes: ' }), document.createTextNode(ptxt)));
      const ftxt = pidx.map(function (i) { return phenoName(t, i, labels) + ' ' + frac(c.pheno[i], c.total) + ' (' + W.fmt(100 * c.pheno[i] / c.total, 3) + '%)'; }).join(', ');
      results.appendChild(W.h('div', {}, W.h('strong', { text: 'Probability of each child: ' }), document.createTextNode(ftxt)));
      W.say(el, 'Genotype ratio ' + gl.map(function (g, i) { return gr[i] + ' ' + plainGeno(g.geno, sep); }).join(', ') + '. Phenotype ratio ' + (ptxt.length > 90 ? pr.join(' : ') : ptxt) + '.');
    }

    buildControls();
    update();
  });
})();
