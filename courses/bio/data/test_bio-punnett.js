// data/test_bio-punnett.js: tests the pure functions of widgets/bio-punnett.js. Run: node data/test_bio-punnett.js
const P = require('../widgets/bio-punnett.js');
let n = 0;
function eq(label, got, want) {
  n++;
  const a = JSON.stringify(got), b = JSON.stringify(want);
  if (a !== b) { console.error('FAIL ' + label + ': got ' + a + ', want ' + b); process.exit(1); }
}
function run(type, d1, d2, letters) {
  const p1 = P.build(type, 0, d1, letters), p2 = P.build(type, 1, d2, letters);
  const c = P.cross(type, p1, p2);
  const ws = P.ratioOf(c.geno.map(function (g) { return g.w; }));
  return { c: c, geno: c.geno.map(function (g, i) { return [P.plainGeno(g.geno, c.sep), ws[i]]; }) };
}
// mono Aa x Aa: 1 AA : 2 Aa : 1 aa, 3 dominant : 1 recessive
let r = run('mono', [1], [1]);
eq('mono geno', r.geno, [['AA', 1], ['Aa', 2], ['aa', 1]]);
eq('mono pheno', r.c.pheno, [3, 1]);
eq('mono total', r.c.total, 4);
// mono AA x aa: all Aa
r = run('mono', [2], [0]);
eq('mono F1', r.geno, [['Aa', 1]]);
eq('mono F1 pheno', r.c.pheno, [4, 0]);
eq('F1 side list', r.c.side.list.length, 1);
// mono Aa x aa: 1:1
r = run('mono', [1], [0]);
eq('test cross', r.geno, [['Aa', 1], ['aa', 1]]);
eq('test cross ratio', P.ratioOf(r.c.pheno), [1, 1]);
// letters
r = run('mono', [1], [1], { L1: 'T' });
eq('letters', r.geno, [['TT', 1], ['Tt', 2], ['tt', 1]]);
// di RrYy x RrYy: 9:3:3:1, 9 genotypes, 16 cells
r = run('di', [1, 1], [1, 1], { L1: 'R', L2: 'Y' });
eq('di total', r.c.total, 16);
eq('di pheno', r.c.pheno, [9, 3, 3, 1]);
eq('di classes', r.geno.length, 9);
eq('di RrYy', r.geno.filter(function (g) { return g[0] === 'RrYy'; })[0][1], 4);
eq('di grid size', [r.c.cells.length, r.c.cells[0].length], [4, 4]);
// di test cross AaBb x aabb: 1:1:1:1
r = run('di', [1, 1], [0, 0]);
eq('di test cross', P.ratioOf(r.c.pheno), [1, 1, 1, 1]);
eq('di test cross grid', [r.c.cells.length, r.c.cells[0].length], [1, 4]);
// di AABb x AaBb
r = run('di', [2, 1], [1, 1]);
eq('di AABb x AaBb pheno', P.ratioOf(r.c.pheno.filter(Boolean)), [3, 1]);
// codominant roan x roan: 1:2:1
r = run('codom', [1], [1]);
eq('codom', r.c.pheno, [1, 2, 1]);
eq('codom geno', r.geno, [['C^R C^R', 1], ['C^R C^W', 2], ['C^W C^W', 1]]);
r = run('codom', [1], [0]);
eq('roan x white', P.ratioOf(r.c.pheno.filter(Boolean)), [1, 1]);
// X-linked: carrier mother x unaffected father
r = run('xlinked', [1], [1]);
eq('xlinked pheno', r.c.pheno, [1, 1, 0, 1, 1]);
eq('xlinked geno', r.geno.map(function (g) { return g[0]; }), ['X^H X^H', 'X^H X^h', 'X^H Y', 'X^h Y']);
eq('xlinked top is the father', r.c.top.list.map(function (g) { return P.plainGeno([g.alleles], ' '); }), ['X^H', 'Y']);
// affected father x unaffected homozygous mother: carrier daughters, unaffected sons
r = run('xlinked', [2], [0]);
eq('affected father', P.ratioOf(r.c.pheno.filter(Boolean)), [1, 1]);
eq('affected father sexes', r.c.pheno.map(function (x) { return x > 0 ? 1 : 0; }), [0, 1, 0, 1, 0]);
// affected mother x unaffected father: carrier daughters, affected sons
r = run('xlinked', [0], [1]);
eq('affected mother sexes', r.c.pheno.map(function (x) { return x > 0 ? 1 : 0; }), [0, 1, 0, 0, 1]);
eq('frac', P.frac(2, 4), '1/2');
eq('ratio', P.ratioOf([6, 2, 4]), [3, 1, 2]);
// phenotype names for di
eq('pheno name di', P.phenoName('di', 1, ['round', 'wrinkled', 'yellow', 'green']), 'round, green');
console.log('ok (' + n + ' checks)');
