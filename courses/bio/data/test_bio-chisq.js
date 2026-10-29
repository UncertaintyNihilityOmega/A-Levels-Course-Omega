// data/test_bio-chisq.js: tests the pure functions of widgets/bio-chisq.js. Run: node data/test_bio-chisq.js
const C = require('../widgets/bio-chisq.js');
let n = 0;
function eq(label, got, want) { n++; const a = JSON.stringify(got), b = JSON.stringify(want); if (a !== b) { console.error('FAIL ' + label + ': got ' + a + ', want ' + b); process.exit(1); } }
function near(label, got, want, tol) { n++; if (Math.abs(got - want) > (tol || 1e-9)) { console.error('FAIL ' + label + ': got ' + got + ', want ' + want); process.exit(1); } }
let o = C.parseObs('275, 98, 79, 28'), r = C.parseRatio('9:3:3:1', 4);
eq('parse obs', o.values, [275, 98, 79, 28]);
eq('parse ratio', r.values, [9, 3, 3, 1]);
let res = C.calc(o.values, r.values);
eq('expected', res.exp, [270, 90, 90, 30]);
near('chi tomato', res.chi, 2.2814814814814817);
eq('df', res.df, 3);
eq('crit', res.crit, 7.81);
eq('not significant', res.sig, false);
// linkage example
res = C.calc([84, 78, 22, 16], [1, 1, 1, 1]);
near('chi linkage', res.chi, 77.6, 1e-9);
eq('significant', res.sig, true);
// Mendel's counts (the widget default)
res = C.calc([315, 108, 101, 32], [9, 3, 3, 1]);
near('chi Mendel', res.chi, 0.47002398081534774);
// explicit expected numbers give the same answer as a ratio
res = C.calc([148, 52], [150, 50]);
near('chi 3:1 numbers', res.chi, 4 / 150 + 4 / 50);
eq('crit df1', res.crit, 3.84);
// validation
eq('empty', C.parseObs('').ok, false);
eq('letters', C.parseObs('12, x, 3').ok, false);
eq('negative', C.parseObs('12, -3').ok, false);
eq('decimal', C.parseObs('12, 3.5').ok, false);
eq('one class', C.parseObs('12').ok, false);
eq('zero total', C.parseObs('0, 0').ok, false);
eq('too many', C.parseObs('1,2,3,4,5,6,7,8,9,10,11,12').ok, false);
eq('ratio mismatch', C.parseRatio('9:3:3', 4).ok, false);
eq('ratio zero', C.parseRatio('9:0', 2).ok, false);
eq('ratio blank means equal', C.parseRatio('', 3).values, [1, 1, 1]);
eq('critical table', C.CRIT.length, 10);
eq('conclusion not sig', /no significant difference/.test(C.conclusion(C.calc([275, 98, 79, 28], [9, 3, 3, 1]))), true);
eq('conclusion sig', /null hypothesis is rejected/.test(C.conclusion(C.calc([84, 78, 22, 16], [1, 1, 1, 1]))), true);
eq('num', C.num(2.5), '2.5');
console.log('ok (' + n + ' checks)');
