// data/cs-binary.test.js: checks the logic of widgets/cs-binary.js against Python for every 8-bit value
// and for every pair of 4-bit patterns. Run: node data/cs-binary.test.js
const { execFileSync } = require('child_process');
const path = require('path');
const L = require(path.join(__dirname, '..', 'widgets', 'cs-binary.js'));

const py = `
import json
def twos(p): v=int(p,2); return v-2**len(p) if p[0]=='1' else v
def inv(p): return ''.join('1' if c=='0' else '0' for c in p)
out={'eight':[], 'add4':[]}
for v in range(256):
    p=format(v,'08b')
    out['eight'].append([p, v, twos(p), (-int(inv(p),2) if p[0]=='1' else v), format(v,'02X')])
for a in range(16):
    for b in range(16):
        pa=format(a,'04b'); pb=format(b,'04b')
        t=a+b; r=format(t%16,'04b')
        out['add4'].append([pa,pb,r,1 if t>=16 else 0, twos(pa)+twos(pb), twos(r)])
print(json.dumps(out))
`;
const data = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8' }));
let checks = 0;
function eq(label, got, want) {
  checks++;
  if (got !== want) { console.error('FAIL ' + label + ': got ' + got + ', want ' + want); process.exit(1); }
}

data.eight.forEach(function (row) {
  const p = row[0], u = row[1], s = row[2], o = row[3], hex = row[4];
  eq('unsigned ' + p, L.unsignedOf(p), u);
  eq('twos ' + p, L.twosOf(p), s);
  eq('ones ' + p, L.onesOf(p), o);
  eq('hex ' + p, L.hexOf(p), hex);
  eq('toPattern unsigned ' + u, L.toPattern(u, 8), p);
  if (s >= -128 && s <= 127) eq('toPattern signed ' + s, L.toPattern(s, 8), p);
  // analyse a denary value in the two's complement range
  const a = L.analyse({ kind: 'value', v: s }, 8);
  eq('analyse pattern ' + s, a.pattern, p);
  eq('analyse twos ' + s, a.rows.twos, p);
  // analyse a typed pattern and a typed hex string
  const b = L.analyse(L.parse(p, '2', 8), 8);
  eq('typed binary ' + p, b.pattern, p);
  const h = L.analyse(L.parse(hex, '16', 8), 8);
  eq('typed hex ' + hex, h.pattern, p);
  // one's complement row for denary input
  if (s >= -127 && s <= 127) {
    const oc = L.analyse({ kind: 'value', v: s }, 8).rows.ones;
    eq('ones row ' + s, oc, s >= 0 ? p : L.invert(L.toPattern(-s, 8)));
  }
});

data.add4.forEach(function (row) {
  const r = L.addAnalyse(row[0], row[1]);
  eq('add result ' + row[0] + '+' + row[1], r.result, row[2]);
  eq('add carry ' + row[0] + '+' + row[1], r.carryOut, row[3]);
  const t = L.twosOf(row[0]) + L.twosOf(row[1]);
  eq('signed overflow ' + row[0] + '+' + row[1], r.sigOverflow, t < -8 || t > 7);
  eq('unsigned overflow ' + row[0] + '+' + row[1], r.unsOverflow, row[3] === 1);
});

// the chapter's worked examples
const e1 = L.addAnalyse('00101101', '01001110');
eq('45+78', e1.result + e1.carries, '01111011' + '00011000');
const e2 = L.addAnalyse('01100100', '00110010');
eq('100+50 overflow', e2.sigOverflow, true);
eq('100+50 carry', e2.carryOut, 0);
const e3 = L.addAnalyse('11111111', '11111111');
eq('-1+-1 overflow', e3.sigOverflow, false);
eq('-1+-1 carry', e3.carryOut, 1);
const e4 = L.addAnalyse('11001000', '01100100');
eq('200+100 unsigned overflow', e4.unsOverflow, true);

// range and error handling: no throws, and a message rather than a wrong pattern
eq('300 in 8 bits', L.analyse({ kind: 'value', v: 300 }, 8).pattern, null);
eq('300 error text', /out of range for 8 bits/.test(L.analyse({ kind: 'value', v: 300 }, 8).error), true);
eq('300 in 9 bits', L.analyse({ kind: 'value', v: 300 }, 9).pattern, '100101100');
eq('-129 in 8 bits', L.analyse({ kind: 'value', v: -129 }, 8).pattern, null);
eq('200 in 8 bits is unsigned', L.analyse({ kind: 'value', v: 200 }, 8).rows.uns, '11001000');
eq('-37 twos', L.analyse({ kind: 'value', v: -37 }, 8).rows.twos, '11011011');
eq('-37 hex', L.analyse({ kind: 'value', v: -37 }, 8).rows.hex.slice(0, 2), 'DB');
eq('bcd 2057', L.bcdOf(2057), '0010 0000 0101 0111');
['', 'abc', '1.5', '--3', '99999999999', '0x', '0b2'].forEach(function (t) {
  ['10', '2', '16'].forEach(function (base) {
    const a = L.analyse(L.parse(t, base, 8), 8);
    eq('no throw ' + t + '/' + base, typeof a, 'object');
  });
});
eq('too many bits', /needs 9 bits/.test(L.parse('100000000', '2', 8).error), true);
eq('hex too big', /more than 8 bits/.test(L.parse('1FF', '16', 8).error), true);
eq('leading zeros ok', L.parse('0000000001', '2', 8).p, '00000001');
eq('16-bit min', L.toPattern(-32768, 16), '1000000000000000');
eq('16-bit hex', L.hexOf('1000000000000000'), '8000');
eq('4-bit hex', L.hexOf('1011'), 'B');
eq('6-bit hex pads', L.hexOf('101101'), '2D');
const bad = L.toAddPattern(L.parse('300', '10', 8), 8, 'A');
eq('add out of range', /out of range/.test(bad.error), true);
console.log('cs-binary logic: ' + checks + ' checks ok');
