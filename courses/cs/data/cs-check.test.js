// data/cs-check.test.js: checks the logic of widgets/cs-check.js against Python:
// parity blocks (every single flip located, random multi-bit errors, both parities, both parity-bit positions)
// and modulo-11 / modulo-10 check digits (every 4-digit code, random codes of 2 to 16 digits, verification).
// Run: node data/cs-check.test.js
const { execFileSync } = require('child_process');
const path = require('path');
const L = require(path.join(__dirname, '..', 'widgets', 'cs-check.js'));

const py = `
import json, random
rng = random.Random(2027)

def pb(bits, typ):
    o = bits.count('1') % 2
    return str(o if typ == 'even' else 1 - o)

def block(rows7, typ, pos):
    rows = [(r + pb(r, typ)) if pos == 'right' else (pb(r, typ) + r) for r in rows7]
    last = ''.join(pb(''.join(r[c] for r in rows), typ) for c in range(8))
    return rows + [last]

def analyse(blk, typ):
    want = 0 if typ == 'even' else 1
    br = [r for r in range(8) if blk[r].count('1') % 2 != want]
    bc = [c for c in range(8) if sum(int(blk[r][c]) for r in range(8)) % 2 != want]
    return br, bc

def flipall(blk, cells):
    b = [list(r) for r in blk]
    for r, c in cells:
        b[r][c] = '0' if b[r][c] == '1' else '1'
    return [''.join(r) for r in b]

parity = []
for case in range(240):
    rows7 = [''.join(rng.choice('01') for _ in range(7)) for _ in range(7)]
    typ = ['even', 'odd'][case % 2]
    pos = ['left', 'right'][(case // 2) % 2]
    blk = block(rows7, typ, pos)
    errs = []
    k = rng.choice([1, 2, 2, 3, 4])
    cells = rng.sample([(r, c) for r in range(8) for c in range(8)], k)
    br, bc = analyse(flipall(blk, cells), typ)
    parity.append({'rows7': rows7, 'typ': typ, 'pos': pos, 'block': blk, 'cells': cells, 'br': br, 'bc': bc})

def m11(code):
    n = len(code)
    total = sum(int(d) * (n + 1 - i) for i, d in enumerate(code))
    rem = total % 11
    raw = (11 - rem) % 11
    return [total, rem, 'X' if raw == 10 else str(raw)]

def m10(code):
    n = len(code)
    total = sum(int(d) * (3 if (n - 1 - i) % 2 == 0 else 1) for i, d in enumerate(code))
    rem = total % 10
    return [total, rem, str((10 - rem) % 10)]

def valid(full, method):
    if method == '11':
        n = len(full)
        total = sum((10 if ch == 'X' else int(ch)) * (n - i) for i, ch in enumerate(full))
        return total % 11 == 0
    n = len(full)
    total = sum(int(ch) * (1 if (n - 1 - i) % 2 == 0 else 3) for i, ch in enumerate(full))
    return total % 10 == 0

codes = []
for v in range(10000):
    c = '%04d' % v
    codes.append([c, m11(c), m10(c)])
for _ in range(600):
    n = rng.randint(2, 16)
    c = ''.join(str(rng.randint(0, 9)) for _ in range(n))
    codes.append([c, m11(c), m10(c)])

verify = []
for _ in range(1500):
    n = rng.randint(2, 16)
    c = ''.join(str(rng.randint(0, 9)) for _ in range(n))
    method = rng.choice(['11', '10'])
    full = c + (m11(c)[2] if method == '11' else m10(c)[2])
    if rng.random() < 0.6:
        i = rng.randrange(len(full))
        alphabet = '0123456789X' if method == '11' and i == len(full) - 1 else '0123456789'
        full = full[:i] + rng.choice(alphabet) + full[i + 1:]
    verify.append([full, method, valid(full, method)])
print(json.dumps({'parity': parity, 'codes': codes, 'verify': verify}))
`;
const data = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8', maxBuffer: 1 << 26 }));
let checks = 0;
function eq(label, got, want) {
  checks++;
  if (JSON.stringify(got) !== JSON.stringify(want)) {
    console.error('FAIL ' + label + ': got ' + JSON.stringify(got) + ', want ' + JSON.stringify(want));
    process.exit(1);
  }
}

// ---- parity ----
data.parity.forEach(function (t, i) {
  const label = 'case ' + i + ' ' + t.typ + ' ' + t.pos;
  const block = L.buildBlock(t.rows7, t.typ, t.pos);
  eq(label + ' block', block, t.block);
  const clean = L.analyse(block, t.typ);
  eq(label + ' clean rows', clean.badRows, []);
  eq(label + ' clean cols', clean.badCols, []);
  // random errors
  let bad = block;
  t.cells.forEach(function (p) { bad = L.flip(bad, p[0], p[1]); });
  const an = L.analyse(bad, t.typ);
  eq(label + ' bad rows', an.badRows, t.br);
  eq(label + ' bad cols', an.badCols, t.bc);
  eq(label + ' diff', L.diff(block, bad).length, t.cells.length);
  eq(label + ' located', !!an.located, t.br.length === 1 && t.bc.length === 1);
  if (an.located) eq(label + ' located cell', [an.located.row, an.located.col], [t.br[0], t.bc[0]]);
  // verdict text never has NaN or undefined, and says "no error" only when nothing fails
  const v = L.verdict(an, t.pos, t.cells.length);
  eq(label + ' verdict clean', /NaN|undefined/.test(v), false);
  eq(label + ' verdict none', /no error detected/.test(v), false);
  // every single flip is located exactly
  if (i < 16) {
    for (let r = 0; r < 8; r++) {
      for (let c = 0; c < 8; c++) {
        const one = L.analyse(L.flip(block, r, c), t.typ);
        eq(label + ' single ' + r + ',' + c, one.located, { row: r, col: c });
      }
    }
  }
});

// the default example (the word SECURED, even parity, left): the chapter's table
const def = L.parseBytes(L.DEFAULT_BYTES);
eq('default parse', def.bytes.length, 7);
eq('default block', L.buildBlock(def.bytes, 'even', 'left'),
  ['01010011', '11000101', '11000011', '01010101', '11010010', '11000101', '01000100', '01010011']);
const flipped = L.flip(L.buildBlock(def.bytes, 'even', 'left'), 3, 3);
const flippedAn = L.analyse(flipped, 'even');
eq('chapter example located', flippedAn.located, { row: 3, col: 3 });
eq('chapter example text', L.where(3, 3, 'left'), 'byte 4, data bit 3');
eq('where parity bit', L.where(0, 0, 'left'), 'byte 1, the parity bit');
eq('where right parity', L.where(2, 7, 'right'), 'byte 3, the parity bit');
eq('where right data', L.where(2, 0, 'right'), 'byte 3, data bit 1');
eq('where parity byte', L.where(7, 5, 'left'), 'the parity byte, data bit 5');
eq('verdict located', L.verdict(flippedAn, 'left', 1), 'One row and one column fail. Error at byte 4, data bit 3. Flip that bit to correct it.');
// four corners escape detection
let corners = L.buildBlock(def.bytes, 'even', 'left');
[[0, 2], [0, 5], [2, 2], [2, 5]].forEach(function (p) { corners = L.flip(corners, p[0], p[1]); });
eq('corners rows', L.analyse(corners, 'even').badRows, []);
eq('corners cols', L.analyse(corners, 'even').badCols, []);
eq('corners verdict', /escape detection/.test(L.verdict(L.analyse(corners, 'even'), 'left', 4)), true);

// pickCells: the right number of distinct cells, avoiding cells already changed
let s = 12345;
const rand = function () { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; };
for (let k = 1; k <= 6; k++) {
  const cells = L.pickCells(rand, k, [[0, 0], [7, 7]]);
  eq('pick count ' + k, cells.length, k);
  eq('pick distinct ' + k, new Set(cells.map(String)).size, k);
  eq('pick avoids ' + k, cells.some(function (p) { return (p[0] === 0 && p[1] === 0) || (p[0] === 7 && p[1] === 7); }), false);
}
eq('pick extreme rand', L.pickCells(function () { return 0.9999999; }, 1, []).length, 1);
eq('pick all 64', L.pickCells(rand, 64, []).length, 64);

// parseBytes errors
eq('parse empty', !!L.parseBytes('').error, true);
eq('parse six', !!L.parseBytes('1010101 1010101 1010101 1010101 1010101 1010101').error, true);
eq('parse bad bit', !!L.parseBytes('1010101 1010101 1010101 1010101 1010101 1010101 101010x').error, true);
eq('parse long byte', !!L.parseBytes('10101010 1010101 1010101 1010101 1010101 1010101 1010101').error, true);
eq('parse commas', L.parseBytes('1010101,1010101,1010101,1010101,1010101,1010101,1010101').bytes.length, 7);
eq('parse null', !!L.parseBytes(null).error, true);

// ---- check digits ----
data.codes.forEach(function (t) {
  const code = t[0];
  [['11', t[1]], ['10', t[2]]].forEach(function (pair) {
    const r = L.cdCompute(code, pair[0]);
    eq('cd ' + pair[0] + ' ' + code, [r.sum, r.rem, r.check], pair[1]);
    eq('cd products ' + code, r.rows.reduce(function (a, x) { return a + x.p; }, 0), r.sum);
    eq('cd weights ' + pair[0] + ' ' + code, r.rows.map(function (x) { return x.w; }),
      pair[0] === '11' ? code.split('').map(function (_, i) { return code.length + 1 - i; }) : code.split('').map(function (_, i) { return (code.length - 1 - i) % 2 === 0 ? 3 : 1; }));
    // the full code with its check digit verifies, in both methods
    const v = L.cdVerify(code + r.check, pair[0]);
    eq('verify own ' + pair[0] + ' ' + code, v.valid, true);
    eq('verify rem ' + code, v.rem, 0);
  });
});
data.verify.forEach(function (t, i) {
  const v = L.cdVerify(t[0], t[1]);
  eq('verify ' + i + ' ' + t[0] + ' m' + t[1], v.valid, t[2]);
  eq('verify expected ' + i, (v.expected === v.last) === t[2], true);
});

// the chapter's numbers
let r = L.cdCompute('4829316', '11');
eq('chapter 4829316', [r.rows.map(function (x) { return x.p; }), r.sum, r.rem, r.check], [[32, 56, 12, 45, 12, 3, 12], 172, 7, '4']);
eq('chapter 627093', L.cdCompute('627093', '11').check, 'X');
eq('chapter 7352', [L.cdCompute('7352', '11').sum, L.cdCompute('7352', '11').check], [66, '0']);
eq('chapter 3926175', [L.cdCompute('3926175', '11').sum, L.cdCompute('3926175', '11').check], [164, '1']);
eq('chapter 315806 mod 10', [L.cdCompute('315806', '10').sum, L.cdCompute('315806', '10').check], [53, '7']);
eq('chapter valid', L.cdVerify('48293164', '11').valid, true);
eq('chapter swapped', L.cdVerify('48293614', '11').valid, false);
eq('chapter 891360', [L.cdVerify('891360', '11').sum, L.cdVerify('891360', '11').valid], [118, false]);
eq('chapter 627093X', L.cdVerify('627093X', '11').valid, true);

// cdParse
eq('cdParse empty', !!L.cdParse('', '11', 'calculate').error, true);
eq('cdParse letters', !!L.cdParse('12a4', '11', 'calculate').error, true);
eq('cdParse X in calculate', !!L.cdParse('123X', '11', 'calculate').error, true);
eq('cdParse too short', !!L.cdParse('1', '11', 'calculate').error, true);
eq('cdParse too long', !!L.cdParse('12345678901234567', '11', 'calculate').error, true);
eq('cdParse spaces and hyphens', L.cdParse('48 29-316', '11', 'calculate').code, '4829316');
eq('cdParse verify X last', L.cdParse('627093x', '11', 'verify').code, '627093X');
eq('cdParse verify X middle', !!L.cdParse('62X0931', '11', 'verify').error, true);
eq('cdParse verify X mod 10', !!L.cdParse('627093X', '10', 'verify').error, true);
eq('cdParse null', !!L.cdParse(null, '10', 'verify').error, true);

// a swap of neighbours: modulo 11 always notices, modulo 10 misses exactly the digits that differ by 5
let missed11 = 0, missed10 = 0, shouldMiss10 = 0;
for (let a = 0; a < 10; a++) {
  for (let b = 0; b < 10; b++) {
    if (a === b) continue;
    ['11', '10'].forEach(function (m) {
      const base = '37' + a + b + '5';
      const good = base + L.cdCompute(base, m).check;
      const swapped = '37' + b + a + '5' + L.cdCompute(base, m).check;
      const ok = L.cdVerify(swapped, m).valid;
      if (m === '11' && ok) missed11++;
      if (m === '10') { if (ok) missed10++; if (Math.abs(a - b) === 5) shouldMiss10++; }
      eq('base valid ' + good, L.cdVerify(good, m).valid, true);
    });
  }
}
eq('mod 11 misses no swap', missed11, 0);
eq('mod 10 misses digits 5 apart', missed10, shouldMiss10);

console.log('ok: ' + checks + ' comparisons');
