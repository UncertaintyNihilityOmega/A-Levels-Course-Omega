// data/test_bio-codon.js: logic test for widgets/bio-codon.js (run from the course folder: node data/test_bio-codon.js)
const w = require(process.cwd() + '/widgets/bio-codon.js');
const T = 'TACCGAAAGTTTCCGATT';
const eq = (a, b, m) => { if (JSON.stringify(a) !== JSON.stringify(b)) throw new Error(m + ': ' + JSON.stringify(a) + ' != ' + JSON.stringify(b)); };
eq(Object.keys(w.CODE).length, 64, '64 codons');
eq(Object.values(w.CODE).filter(v => v === 'STOP').length, 3, '3 stop');
const m0 = w.comp(T); eq(m0, 'AUGGCUUUCAAAGGCUAA', 'mRNA');
const tr0 = w.translate(m0); eq(w.chain(tr0), ['Met', 'Ala', 'Phe', 'Lys', 'Gly'], 'chain'); eq(tr0.stop, true, 'stop');
const run = (kind, pos, base) => { const t1 = w.mutate(T, kind, pos, base); const tr1 = w.translate(w.comp(t1)); return { t1, tr1, v: w.verdict(kind, pos, T, t1, tr0, tr1) }; };
let r = run('sub', 4, 'A'); eq(r.v.kind, 'missense', 'sub 4 A'); console.log(r.v.text);
r = run('sub', 4, 'C'); eq(r.v.kind, 'same', 'same base');
r = run('sub', 10, 'A'); eq(r.v.kind, 'nonsense', 'nonsense'); eq(w.chain(r.tr1), ['Met', 'Ala', 'Phe'], 'nonsense chain'); console.log(r.v.text);
r = run('sub', 6, 'G'); console.log('sub 6 G', r.v.kind, r.v.text);
eq(r.v.kind, 'silent', 'silent');
r = run('sub', 18, 'A'); console.log('sub 18 A', r.v.kind, r.v.text);
r = run('sub', 17, 'A'); console.log('sub 17 A', r.v.kind, r.v.text);
r = run('ins', 4, 'A'); eq(r.v.kind, 'frameshift', 'ins'); console.log(r.v.text);
r = run('del', 4, 'A'); eq(r.v.kind, 'frameshift', 'del'); console.log(r.v.text);
r = run('sub', 1, 'G'); console.log('sub 1 G (start codon)', r.v.kind, r.v.text);
r = run('ins', 1, 'C'); console.log('ins 1 C', r.v.kind, r.v.text);
eq(w.validDna('ATCG'), true, 'valid'); eq(w.validDna('ATCU'), false, 'U invalid'); eq(w.validDna('AT'), false, 'short'); eq(w.validDna(''), false, 'empty');
eq(w.clean(' ta c-cg '), 'TACCG', 'clean');
eq(w.defaultBase('C'), 'A', 'default base'); eq(w.defaultBase('A'), 'T', 'default base A');
const kinds = {};
for (let p = 1; p <= T.length; p++) for (const b of 'ATCG') { const x = run('sub', p, b); kinds[x.v.kind] = (kinds[x.v.kind] || 0) + 1; }
console.log(JSON.stringify(kinds));
for (let p = 1; p <= T.length; p++) for (const k of ['ins', 'del']) for (const b of 'ATCG') run(k, p, b);
console.log('bio-codon logic ok');
