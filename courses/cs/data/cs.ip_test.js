// data/cs.ip_test.js: compares the cs-ip widget's arithmetic with Python's ipaddress module.
// Run from the course folder: py data/cs.ip_expected.py > scratch/ip_expected.json && node data/cs.ip_test.js
const fs = require('fs');
const path = require('path');
global.W = { register() {} };
const w = require(path.join(process.cwd(), 'widgets', 'cs-ip.js'));
const raw = fs.readFileSync(path.join(process.cwd(), 'scratch', 'ip_expected.json'), 'utf8').replace(/^﻿/, '');
const expected = JSON.parse(raw);
let bad = 0;
for (const e of expected) {
  const r = w.calc(e.ip, e.prefix);
  const got = r.error ? { error: r.error } : {
    network: w.dotted(r.network), broadcast: w.dotted(r.broadcast), first: w.dotted(r.first), last: w.dotted(r.last),
    hosts: r.hosts, mask: w.dotted(r.mask), kind: r.type.kind
  };
  for (const k of ['network', 'broadcast', 'first', 'last', 'hosts', 'mask', 'kind']) {
    if (got[k] !== e[k]) { bad++; console.log('MISMATCH', e.ip, e.prefix, k, got[k], e[k]); }
  }
  const m = w.parseMask(e.mask);
  if (m.prefix !== e.prefix) { bad++; console.log('MASK', e.mask, m, e.prefix); }
}
// invalid input
for (const t of ['', '1.2.3', '1.2.3.256', 'a.b.c.d', '1.2.3.4.5', '1..2.3', '-1.2.3.4', '1.2.3.4 5']) {
  if (!w.calc(t, 24).error) { bad++; console.log('should be invalid', t); }
}
for (const t of ['255.0.255.0', '255.255.255.255', '0.0.0.0', '255.255.255.1', '255.255.255.253', '255.255.255.254', 'x']) {
  if (!w.parseMask(t).error) { bad++; console.log('mask should be invalid', t); }
}
if (!w.calc('1.2.3.4', 7).error || !w.calc('1.2.3.4', 31).error || !w.calc('1.2.3.4', NaN).error) { bad++; console.log('prefix range'); }
console.log(bad === 0 ? 'cs-ip arithmetic ok: ' + expected.length + ' cases' : bad + ' problems');
process.exit(bad ? 1 : 0);
