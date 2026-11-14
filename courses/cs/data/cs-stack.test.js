// data/cs-stack.test.js: checks the structures in widgets/cs-stack.js against an independent Python model.
// Python plays 600 random operation sequences (all four structures, array sizes 3 to 12, first index 0 or 1,
// numbers and words) on a dictionary-based model written from the chapter's pseudocode, and records the
// result and the full state after every operation. Node replays the same sequences and must match exactly.
// Run: node data/cs-stack.test.js
const { execFileSync } = require('child_process');
const path = require('path');
const S = require(path.join(__dirname, '..', 'widgets', 'cs-stack.js'));

const py = `
import json, random
random.seed(11)

NUM = __import__('re').compile(r'^-?\\d+(\\.\\d+)?$')
def less(a, b):
    if NUM.match(a) and NUM.match(b):
        return float(a) < float(b)
    return a < b

class Model:
    def __init__(self, kind, size, base):
        self.kind, self.size, self.base = kind, size, base
        self.mem = {}           # Data[index]
        self.ptr = {}           # Pointer[index] for the list
        nil = base - 1
        self.nil = nil
        if kind == 'stack':
            self.top = nil
        elif kind in ('queue', 'circular'):
            self.front, self.rear, self.count = base, nil, 0
        else:
            self.start, self.free = nil, base
            for i in range(base, base + size):
                self.ptr[i] = i + 1 if i < base + size - 1 else nil
        for i in range(base, base + size):
            self.mem[i] = ''

    def last(self): return self.base + self.size - 1

    def op(self, name, v):
        k = self.kind
        if name == 'push':
            if self.top == self.last(): return ('overflow', None)
            self.top += 1; self.mem[self.top] = v; return ('ok', self.top)
        if name == 'pop':
            if self.top == self.nil: return ('underflow', None)
            item = self.mem[self.top]; self.top -= 1; return ('ok', item)
        if name == 'peek':
            if self.top == self.nil: return ('underflow', None)
            return ('ok', self.mem[self.top])
        if name == 'enqueue':
            if k == 'circular':
                if self.count == self.size: return ('full', None)
                self.rear = (self.rear - self.base + 1) % self.size + self.base
                self.mem[self.rear] = v; self.count += 1; return ('ok', self.rear)
            if self.rear == self.last(): return ('full', None)
            self.rear += 1; self.mem[self.rear] = v; return ('ok', self.rear)
        if name == 'dequeue':
            if k == 'circular':
                if self.count == 0: return ('empty', None)
                item = self.mem[self.front]
                self.front = (self.front - self.base + 1) % self.size + self.base
                self.count -= 1; return ('ok', item)
            if self.front > self.rear: return ('empty', None)
            item = self.mem[self.front]; self.front += 1; return ('ok', item)
        if name == 'insert':
            if self.free == self.nil: return ('full', None)
            node = self.free; self.free = self.ptr[node]; self.mem[node] = v
            prev, cur = self.nil, self.start
            while cur != self.nil and less(self.mem[cur], v):
                prev, cur = cur, self.ptr[cur]
            self.ptr[node] = cur
            if prev == self.nil: self.start = node
            else: self.ptr[prev] = node
            return ('ok', node)
        if name == 'remove':
            prev, cur = self.nil, self.start
            while cur != self.nil and self.mem[cur] != v:
                prev, cur = cur, self.ptr[cur]
            if cur == self.nil: return ('notfound', None)
            nxt = self.ptr[cur]
            if prev == self.nil: self.start = nxt
            else: self.ptr[prev] = nxt
            self.ptr[cur] = self.free; self.free = cur
            return ('ok', cur)
        if name == 'find':
            cur, visits = self.start, 0
            while cur != self.nil:
                visits += 1
                if self.mem[cur] == v: return ('found', cur, visits)
                cur = self.ptr[cur]
            return ('notfound', None, visits)

    def state(self):
        d = [self.mem[i] for i in range(self.base, self.base + self.size)]
        s = {'data': d}
        if self.kind == 'stack': s['top'] = self.top
        elif self.kind in ('queue', 'circular'):
            s['front'], s['rear'] = self.front, self.rear
            if self.kind == 'circular': s['count'] = self.count
        else:
            s['ptr'] = [self.ptr[i] for i in range(self.base, self.base + self.size)]
            s['start'], s['free'] = self.start, self.free
        return s

    def order(self):
        k = self.kind
        if k == 'stack':
            return [self.mem[i] for i in range(self.top, self.base - 1, -1)]
        if k == 'queue':
            return [self.mem[i] for i in range(self.front, self.rear + 1) if self.base <= i <= self.last()]
        if k == 'circular':
            return [self.mem[(self.front - self.base + j) % self.size + self.base] for j in range(self.count)]
        out, cur = [], self.start
        while cur != self.nil:
            out.append(self.mem[cur]); cur = self.ptr[cur]
        return out

OPS = {'stack': ['push', 'pop', 'peek'], 'queue': ['enqueue', 'dequeue'], 'circular': ['enqueue', 'dequeue'],
       'list': ['insert', 'remove', 'find']}
NEEDS = {'push', 'enqueue', 'insert', 'remove', 'find'}
WORDS = ['Amara', 'Bilal', 'Chen', 'Dina', 'Emeka', 'Farah', 'Goran', 'Hana', 'amy', 'Zed', 'x']
def value(numeric):
    if numeric: return str(random.randint(-20, 120))
    if random.random() < 0.2: return str(random.randint(0, 30))
    return random.choice(WORDS)

trials = []
for t in range(600):
    kind = random.choice(['stack', 'queue', 'circular', 'list'])
    size = random.randint(3, 12); base = random.choice([0, 1])
    numeric = random.random() < 0.5
    m = Model(kind, size, base)
    steps = []
    n = random.choice([5, 15, 40, 80])
    for _ in range(n):
        name = random.choice(OPS[kind])
        # bias towards fill-then-drain so that full and empty happen
        if kind != 'list' and random.random() < 0.25:
            name = OPS[kind][-1] if kind != 'stack' else 'pop'
        v = value(numeric) if name in NEEDS else None
        if name in ('remove', 'find') and random.random() < 0.6:
            known = [m.mem[i] for i in range(base, base + size) if m.mem[i] != '']
            if known: v = random.choice(known)
        r = m.op(name, v)
        steps.append({'op': name, 'v': v, 'kind': r[0], 'value': r[1], 'visits': r[2] if len(r) > 2 else None,
                      'state': m.state(), 'order': m.order()})
    trials.append({'kind': kind, 'size': size, 'base': base, 'steps': steps})
print(json.dumps(trials))
`;

const trials = JSON.parse(execFileSync('py', ['-c', py], { encoding: 'utf8', maxBuffer: 1 << 28 }));
let checks = 0;
function same(a, b, label) {
  const x = JSON.stringify(a), y = JSON.stringify(b);
  if (x !== y) { console.error('MISMATCH ' + label + '\n  node:   ' + x + '\n  python: ' + y); process.exit(1); }
  checks++;
}
function stateOf(st) {
  const s = { data: st.data.slice() };
  if (st.type === 'stack') s.top = st.top;
  else if (st.type === 'queue' || st.type === 'circular') { s.front = st.front; s.rear = st.rear; if (st.type === 'circular') s.count = st.count; }
  else { s.ptr = st.ptr.slice(); s.start = st.start; s.free = st.free; }
  return s;
}
const FN = { push: S.push, pop: S.pop, peek: S.peek, enqueue: S.enqueue, dequeue: S.dequeue, insert: S.insert, remove: S.remove, find: S.find };
const seen = { overflow: 0, underflow: 0, full: 0, empty: 0, notfound: 0, found: 0, wrap: 0 };
trials.forEach(function (t, ti) {
  const st = S.make(t.kind, t.size, t.base);
  t.steps.forEach(function (step, si) {
    const label = 'trial ' + ti + ' (' + t.kind + ', size ' + t.size + ', base ' + t.base + ') step ' + si + ' ' + step.op + ' ' + step.v;
    const before = t.kind === 'circular' ? st.rear : null;
    const r = FN[step.op](st, step.v);
    same(r.kind, step.kind, label + ' kind');
    same(r.ok, step.kind === 'ok' || step.kind === 'found', label + ' ok');
    if (step.op === 'pop' || step.op === 'peek' || step.op === 'dequeue' || step.kind === 'ok' || step.kind === 'found') same(r.value, step.value, label + ' value');
    if (step.visits !== null) same(r.visits, step.visits, label + ' visits');
    same(stateOf(st), step.state, label + ' state');
    same(S.order(st), step.order, label + ' order');
    if (typeof r.msg !== 'string' || r.msg === '' || /undefined|NaN|null\b.*null\b.*null/.test(r.msg)) { console.error('bad message ' + label + ': ' + r.msg); process.exit(1); }
    checks++;
    if (seen[step.kind] !== undefined) seen[step.kind]++;
    if (before !== null && step.kind === 'ok' && step.op === 'enqueue' && st.rear < before) seen.wrap++;
  });
});
// live / markers sanity: live slots count equals the item count; markers stay inside the array
trials.forEach(function (t) {
  const st = S.make(t.kind, t.size, t.base);
  t.steps.forEach(function (step) {
    FN[step.op](st, step.v);
    const live = S.live(st).filter(Boolean).length;
    same(live, step.order.length, 'live count');
    const marks = S.markers(st);
    same(marks.length, t.size, 'markers length');
  });
});
// every case the chapter relies on must have been exercised
['overflow', 'underflow', 'full', 'empty', 'notfound', 'found', 'wrap'].forEach(function (k) {
  if (!seen[k]) { console.error('test never reached: ' + k); process.exit(1); }
});

// Bad input: S.size, S.baseOf, S.typeOf, S.items, S.check never throw
['abc', '', null, undefined, '99', '1', '-5', '7.9', NaN].forEach(function (v) { const n = S.size(v); if (!(n >= 3 && n <= 12)) throw new Error('size ' + v); checks++; });
['2', 'x', null, '0', ' 0 ', '1'].forEach(function (v) { const b = S.baseOf(v); if (b !== 0 && b !== 1) throw new Error('base'); checks++; });
['zzz', null, 'LIST', ' queue '].forEach(function (v) { if (S.TYPES.indexOf(S.typeOf(v)) < 0) throw new Error('type'); checks++; });
same(S.items(' a, ,b ,,c '), ['a', 'b', 'c'], 'items');
same(S.items('x'.repeat(30)), ['x'.repeat(12)], 'items long');
same(S.items(null), [], 'items null');
if (!S.check('').error || !S.check('   ').error || !S.check('y'.repeat(13)).error || S.check(' 7 ').value !== '7') throw new Error('check');

// The chapter's own examples
let st = S.build('stack', 5, 1, ['12', '7', '30']);
same(S.pop(st).value, '30', 'chapter stack pop');
S.push(st, '5');
same(S.order(st), ['5', '7', '12'], 'chapter stack order');
st = S.build('list', 7, 1, ['Dina', 'Farah', 'Bilal']);
same([st.start, st.free], [3, 4], 'chapter list start/free');
S.insert(st, 'Chen');
same([st.start, st.free, st.ptr[3 - 1], st.ptr[4 - 1], st.data[3]], [3, 5, 4, 1, 'Chen'], 'chapter list insert Chen');
S.insert(st, 'Amara');
S.remove(st, 'Dina');
same([st.start, st.free, st.ptr.slice()], [5, 1, [6, 0, 4, 2, 3, 7, 0]], 'chapter list delete Dina');
st = S.build('circular', 6, 1, ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']);
S.dequeue(st); S.dequeue(st); S.dequeue(st); S.enqueue(st, 'J7');
same([st.front, st.rear, st.count, st.data.slice()], [4, 1, 4, ['J7', 'J2', 'J3', 'J4', 'J5', 'J6']], 'chapter circular');
st = S.build('queue', 6, 1, ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']);
S.dequeue(st); S.dequeue(st); S.dequeue(st);
same(S.enqueue(st, 'J7').kind, 'full', 'chapter linear queue full with free front');

console.log('cs-stack: ' + checks + ' checks passed over ' + trials.length + ' sequences (' + JSON.stringify(seen) + ')');
