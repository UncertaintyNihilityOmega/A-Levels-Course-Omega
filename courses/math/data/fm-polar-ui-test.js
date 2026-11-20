// Interaction test for widgets/fm-polar.js: fake DOM and fake W (run: node data/fm-polar-ui-test.js)
const PI = Math.PI;
let registered = null, lastBody = null;
const readout = {};
const mkEl = (tag) => ({ tag, children: [], listeners: {}, style: {}, attrs: {}, textContent: '', value: '', checked: false,
  append(...c) { this.children.push(...c); }, setAttribute(k, v) { this.attrs[k] = v; },
  addEventListener(t, f) { (this.listeners[t] = this.listeners[t] || []).push(f); },
  fire(t) { (this.listeners[t] || []).forEach((f) => f({})); } });
const find = (el, pred, out = []) => { if (pred(el)) out.push(el); (el.children || []).forEach((c) => typeof c === 'object' && find(c, pred, out)); return out; };
const sliders = [];
const W = {
  register(n, fn) { registered = fn; },
  frame() { lastBody = mkEl('div'); return { root: mkEl('div'), body: lastBody }; },
  h(tag, props, ...kids) { const e = mkEl(tag); if (props) for (const k of Object.keys(props)) { if (k === 'style') Object.assign(e.style, props[k]); else e.attrs[k] = props[k]; } e.append(...kids); if (typeof kids[0] === 'string') e.textContent = kids[0]; return e; },
  field(o) { const input = mkEl('input'); input.value = o.value; input.isExpr = true; const el = mkEl('div'); el.append(input); return { el, input, get: () => input.value }; },
  slider(o) { const input = mkEl('input'); const s = { el: mkEl('div'), input, value: o.value, oninput: o.oninput, get: () => s.value, set: (v) => { s.value = v; } }; sliders.push(s); return s; },
  canvas(body, o) {
    const c = { redraws: 0, redraw() {
      c.redraws++;
      const ctx = new Proxy({}, { get: (t, k) => (k in t ? t[k] : () => {}), set: (t, k, v) => { t[k] = v; return true; } });
      o.draw(ctx, 300, 300, { sc: 'a', sc2: 'b', red: 'r', ink2: 'i', ink3: 'i', rule: 'x', rule2: 'x', card: 'c', font: 'f' });
      o.draw(ctx, 0, 0, {});
    }, setLabel() {} };
    c.describe = o.describe; return c;
  },
  readout() { return { el: mkEl('div'), set(k, v) { readout[k] = v; } }; },
  animate(fn, o) { const a = { fn, still: o.still, started: 0, stopped: 0, start() { a.started++; }, stop() { a.stopped++; } }; global.__anim = a; return a; },
  reducedMotion: () => false,
  parse(src) {
    if (!/^[0-9+\-*\/().,\sTtcosinqrexpabMh^]*$/.test(src)) throw new Error('bad chars');
    const js = src.replace(/\^/g, '**').replace(/\b(sin|cos|tan|sqrt|exp|abs)\b/g, 'Math.$1').replace(/\bt\b/g, 'T');
    const f = new Function('T', 'return ' + js);
    return { f: (sc) => f(sc.t) };
  },
  fix: (v, d) => (+v).toFixed(d), fmt: (v, n) => String(+(+v).toPrecision(n || 3)),
};
global.window = { W };
let now = 0; global.performance = { now: () => now };
require('../widgets/fm-polar.js');
let bad = 0; const ok = (c, m) => { if (!c) { console.log('FAIL', m); bad++; } };
const btn = (txt) => find(lastBody, (e) => e.tag === 'button' && e.textContent === txt)[0];

registered(mkEl('div'), { r: '1+cos(t)', range: '0,2*pi' });
const box = find(lastBody, (e) => e.attrs && e.attrs.type === 'checkbox')[0];
const exprBox = find(lastBody, (e) => e.isExpr)[0];
ok(/2\.00π/.test(readout.th) && readout.r === '2.000' && readout.xy === '(2.000, 0.000)', 'default state: ' + JSON.stringify(readout));

btn('Circle').fire('click');
ok(/^0\.000/.test(readout.r), 'circle end r = 0: ' + readout.r);
ok(/0\.50π/.test(readout.th), 'theta 0.50π: ' + readout.th);
ok(btn('Circle').attrs['aria-pressed'] === 'true' && btn('Cardioid').attrs['aria-pressed'] === 'false', 'pressed states');
box.checked = true; box.fire('change');
ok(/≈ 3\.1416 = π/.test(readout.area), 'circle area = π: ' + readout.area);

exprBox.value = '3+cos(t)'; exprBox.fire('input');
ok(/2\.00π|0\.50π/.test(readout.th), 'typed expression accepted: ' + readout.th);
const before = readout.r;
exprBox.value = 'bad!!'; exprBox.fire('input');
ok(readout.r === before, 'bad expression leaves the curve alone: ' + readout.r);

// negative r gives no point: rose at theta = pi/2 (cos 2t = cos pi = -1)
btn('Rose').fire('click');
sliders[0].oninput(PI / 2);
ok(/no point/.test(readout.r) && readout.xy === 'no point', 'rose r<0: ' + readout.r + ' ' + readout.xy);
sliders[0].oninput(0.0);
ok(readout.r === '1.000', 'rose r(0) = 1: ' + readout.r);

btn('Reset').fire('click');
ok(/0\.00π/.test(readout.th), 'reset: ' + readout.th);
btn('Play').fire('click');
const a = global.__anim;
ok(a.started === 1 && btn('Pause'), 'play starts and the label says Pause');
let cont = true, steps = 0;
while (cont && steps < 2000) { now += 16; cont = a.fn(); steps++; }
ok(!cont && steps > 300 && steps < 700, 'animation lasts about 7 s: ' + steps + ' ticks');
ok(btn('Play') && !btn('Pause'), 'label back to Play at the end');
ok(/2\.00π/.test(readout.th), 'ends at 2π: ' + readout.th);

// spiral area with fixed start
btn('Spiral').fire('click');
box.checked = true; box.fire('change');
ok(/≈ 20\.67/.test(readout.area), 'spiral r = t/4 over 0..4π area 2π³/3 = 20.67: ' + readout.area);
console.log(bad ? bad + ' failures' : 'all ok');
process.exit(bad ? 1 : 0);
