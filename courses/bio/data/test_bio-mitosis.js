// data/test_bio-mitosis.js: logic test for the counts in widgets/bio-mitosis.js (run from the course folder: node data/test_bio-mitosis.js)
const w = require(process.cwd() + '/widgets/bio-mitosis.js');
const eq = (a, b, m) => { if (JSON.stringify(a) !== JSON.stringify(b)) throw new Error(m + ': ' + JSON.stringify(a) + ' != ' + JSON.stringify(b)); };
eq(w.STAGES.length, 7, 'seven steps');
// the chapter's table for a cell with 46 chromosomes in G1 (n is the number of chromosomes in G1)
const want = [[46, 0, 1], [46, 92, 2], [46, 92, 2], [46, 92, 2], [92, 0, 2], [92, 0, 2], [46, 0, 1]];
want.forEach((r, i) => { const c = w.counts(i, 46); eq([c.chr, c.chd, c.dna], r, 'step ' + i); });
[2, 4, 6].forEach(n => {
  eq(w.chroms(n).length, n, 'chromosomes drawn for n=' + n);
  eq(w.counts(1, n).chd, 2 * n, 'G2 chromatids');
  eq(w.counts(4, n).chr, 2 * n, 'anaphase chromosomes');
  eq(w.counts(6, n).chr, n, 'daughter chromosomes');
});
eq(w.countLine(3, 4), 'chromosomes: 4 · chromatids: 8 · DNA content: 2× G1', 'spec example (metaphase, n = 4)');
eq(w.pickN('3'), 4, 'bad n falls back to 4'); eq(w.pickN('6'), 6, 'n = 6'); eq(w.pickN(undefined), 4, 'no n');
console.log('bio-mitosis counts ok');
