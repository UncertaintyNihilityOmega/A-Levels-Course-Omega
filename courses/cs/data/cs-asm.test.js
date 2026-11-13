// data/cs-asm.test.js: runs widgets/cs-asm.js (its pure logic) and data/cs.asmsim.py (the simulator the chapter checks use)
// on the built-in programs, on every ```text program in cs.processor and cs.assembly, and on edge cases, and compares
// every step: address, registers, memory writes, compare result, output and the register transfers.
// Run: node data/cs-asm.test.js
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const root = path.join(__dirname, '..');
const L = require(path.join(root, 'widgets', 'cs-asm.js'));

const cases = [];
function add(label, text, input, bits) { cases.push({ label: label, text: text, input: input || '', bits: bits || 8 }); }

L.ORDER.forEach(function (k) {
  add('built-in ' + k, L.PROGRAMS[k].text, L.PROGRAMS[k].input);
  ['A', 'q', ''].forEach(function (i) { add('built-in ' + k + ' with input ' + JSON.stringify(i), L.PROGRAMS[k].text, i); });
});
['cs.processor', 'cs.assembly'].forEach(function (id) {
  const md = fs.readFileSync(path.join(root, 'chapters', id + '.md'), 'utf8');
  const re = /^```text\n([\s\S]*?)^```/gm;
  let m, n = 0;
  while ((m = re.exec(md))) {
    n += 1;
    ['A', 'B', 'q'].forEach(function (i) { add(id + ' block ' + n + ' input ' + i, m[1], i); });
  }
});
[
  ['wrap sub', '100 LDM #0\n101 SUB #1\n102 INC ACC\n103 DEC ACC\n104 END'],
  ['wrap add', '100 LDM #200\n101 ADD #100\n102 LSL #2\n103 LSR #1\n104 END'],
  ['wrap add 16 bits', '100 LDM #200\n101 ADD #100\n102 LSL #2\n103 END', '', 16],
  ['indirect', '100 LDR #2\n101 LDI 200\n102 CMI 201\n103 JPE 105\n104 END\n105 LDX 200\n106 MOV IX\n107 LDX 200\n108 END\n200 205\n201 99\n205 99'],
  ['hex and binary', '100 LDM &1F\n101 AND B00001111\n102 OR &F0\n103 XOR #255\n104 ADD &A\n105 STO 150\n106 END'],
  ['lower case and comment', '100 ldm #5 // load\n101 inc acc\n102 end'],
  ['bad: unknown label', '100 JMP NOWHERE\n101 END'],
  ['bad: jpe before cmp', '100 JPE 100\n101 END'],
  ['bad: missing operand', '100 LDD\n101 END'],
  ['bad: duplicate label', '100 A: LDM #1\n101 A: END'],
  ['bad: infinite loop', '100 LOOP: JMP LOOP'],
  ['bad: data too big', '100 END\n101 300'],
  ['bad: in empty', '100 IN\n101 END'],
  ['bad: runs into data', '100 LDM #1\n101 5'],
  ['bad: operand on end', '100 END 5'],
  ['bad: no instruction', '100 5'],
  ['bad: ldm with address', '100 LDM 5\n101 END'],
  ['bad: reading an instruction', '100 LDD 100\n101 END']
].forEach(function (c) { add(c[0], c[1], c[2] || '', c[3]); });

const py = `
import json, sys, runpy
g = runpy.run_path(sys.argv[1])
cases = json.load(sys.stdin)
out = []
for c in cases:
    try:
        steps, fin = g['run'](c['text'], c['input'], 100, c['bits'])
        out.append({'ok': True, 'steps': steps, 'final': {'acc': fin['acc'], 'ix': fin['ix'], 'mem': fin['mem'], 'out': fin['out']}})
    except g['AsmError'] as e:
        out.append({'ok': False, 'error': str(e)})
print(json.dumps(out, ensure_ascii=False))
`;
const result = JSON.parse(execFileSync('py', ['-X', 'utf8', '-c', py, path.join(root, 'data', 'cs.asmsim.py')],
  { input: JSON.stringify(cases), encoding: 'utf8', env: Object.assign({}, process.env, { PYTHONUTF8: '1' }), maxBuffer: 1 << 28 }));

let checks = 0, runs = 0, errors = 0;
function eq(label, got, want) {
  checks++;
  if (JSON.stringify(got) !== JSON.stringify(want)) {
    console.error('FAIL ' + label + '\n  js: ' + JSON.stringify(got) + '\n  py: ' + JSON.stringify(want));
    process.exit(1);
  }
}
cases.forEach(function (c, i) {
  const want = result[i];
  const got = L.run(c.text, c.input, 100, c.bits, 1000);
  if (!want.ok) {
    errors++;
    eq(c.label + ': the JavaScript simulator reports an error too', got.error !== null, true);
    return;
  }
  runs++;
  eq(c.label + ': no error', got.error, null);
  eq(c.label + ': step count', got.steps.length, want.steps.length);
  got.steps.forEach(function (s, k) {
    const w = want.steps[k];
    const lab = c.label + ' step ' + k;
    eq(lab + ' address', s.addr, w.addr);
    eq(lab + ' acc', s.acc, w.acc);
    eq(lab + ' ix', s.ix, w.ix);
    eq(lab + ' mem', s.mem, w.mem);
    eq(lab + ' cmp', s.cmp, w.cmp);
    eq(lab + ' out', s.out, w.out);
    eq(lab + ' micro', s.micro, w.micro);
  });
  eq(c.label + ' final acc', got.final.acc, want.final.acc);
  eq(c.label + ' final ix', got.final.ix, want.final.ix);
  eq(c.label + ' final mem', got.final.mem, want.final.mem);
  eq(c.label + ' final out', got.final.out, want.final.out);
});
// the built-in programs do what their titles say
function out(k, i) { return L.run(L.PROGRAMS[k].text, i == null ? L.PROGRAMS[k].input : i, 100, 8, 1000).final; }
eq('sum', out('sum').mem[202], 12);
eq('labels', out('labels').mem[106], 12);
eq('countdown', out('countdown').out, '54321');
eq('indexed', out('indexed').mem[114], 13);
eq('mask', out('mask').out, 'Y');
eq('upper', out('upper').out, 'Q');
eq('times', out('times').mem[202], 12);
console.log('ok: ' + checks + ' comparisons, ' + runs + ' programs run, ' + errors + ' error cases');
