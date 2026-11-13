// data/cs-sql.test.js: compares the cs-sql widget's query engine with sqlite (via Python) on every control combination.
// Run from the course folder:  py data/cs_sql_data.py --embed --cases && node data/cs-sql.test.js
const fs = require('fs');
const path = require('path');
global.W = { register() {} };
const w = require(path.join(process.cwd(), 'widgets', 'cs-sql.js'));
const raw = fs.readFileSync(path.join(process.cwd(), 'scratch', 'sql_cases.json'), 'utf8').replace(/^﻿/, '');
const cases = JSON.parse(raw);

function same(a, b) {
  if (a === null || a === undefined || b === null || b === undefined) return (a === null || a === undefined) && (b === null || b === undefined);
  if (typeof a === 'number' && typeof b === 'number') return Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(a), Math.abs(b));
  return String(a) === String(b);
}
function rowKey(r) { return JSON.stringify(r.map(function (v) { return typeof v === 'number' ? Math.round(v * 1e9) / 1e9 : v; })); }
function multisetEqual(a, b) {
  if (a.length !== b.length) return false;
  const x = a.map(rowKey).sort(), y = b.map(rowKey).sort();
  return x.every(function (v, i) { return v === y[i]; });
}

let bad = 0, checked = 0, withOrder = 0;
function problem(msg, c) { bad++; if (bad <= 15) console.log('MISMATCH', msg, '\n', c.sql); }

for (const c of cases) {
  const spec = {
    from: c.from,
    fields: c.select.filter(function (s) { return typeof s === 'string'; }),
    agg: (function () { const a = c.select.find(function (s) { return Array.isArray(s); }); return a ? { fn: a[0], field: a[1] } : null; })(),
    where: (c.where || []).map(function (x) {
      let v = x[2];
      const q = /^'(.*)'$/.exec(v);
      return { field: x[0], op: x[1], value: q ? q[1] : v };
    }),
    bool: c.bool || 'AND',
    group: c.group || '',
    order: c.order ? { key: c.order[0], dir: c.order[1] } : null
  };
  const r = w.evaluate(c.db, spec);
  if (c.error) { problem('sqlite refused but widget answered', c); continue; }
  if (r.error) { problem('widget refused: ' + r.error, c); continue; }
  checked++;
  if (r.cols.length !== c.cols.length) { problem('column count', c); continue; }
  if (!multisetEqual(r.rows, c.rows)) { problem('rows differ (' + r.rows.length + ' vs ' + c.rows.length + ')', c); continue; }
  if (c.order) {
    withOrder++;
    const k = r.cols.indexOf(c.order[0]);
    if (k < 0) { problem('order key not in output', c); continue; }
    const got = r.rows.map(function (row) { return row[k]; });
    const want = c.rows.map(function (row) { return row[k]; });
    if (!got.every(function (v, i) { return same(v, want[i]); })) problem('order differs', c);
  }
}

// invalid combinations must give a friendly error (and never throw)
const base = w.defaultSpec('school');
function refuses(name, patch, db) {
  const spec = Object.assign({}, base, patch);
  let r;
  try { r = w.evaluate(db || 'school', spec); } catch (e) { bad++; console.log('THREW', name, e.message); return; }
  if (!r.error) { bad++; console.log('should be refused:', name); }
}
refuses('nothing selected', { fields: [], agg: null });
refuses('plain field with aggregate and no group', { fields: ['Club.ClubName'], agg: { fn: 'COUNT', field: '*' }, from: 'join' });
refuses('plain field not in group', { fields: ['Student.FirstName'], agg: { fn: 'COUNT', field: '*' }, group: 'Student.Form', from: 'join' });
refuses('sum of text', { fields: [], agg: { fn: 'SUM', field: 'Student.FirstName' }, from: 'join' });
refuses('avg of date', { fields: [], agg: { fn: 'AVG', field: 'Student.BirthDate' }, from: 'join' });
refuses('number expected', { fields: ['Student.FirstName'], where: [{ field: 'Student.Points', op: '>', value: 'abc' }], from: 'join' });
refuses('empty value', { fields: ['Student.FirstName'], where: [{ field: 'Student.Points', op: '>', value: '' }], from: 'join' });
refuses('grouped order by hidden column', { fields: ['Club.ClubName'], agg: { fn: 'COUNT', field: '*' }, group: 'Club.ClubName', order: { key: 'Student.Points', dir: 'ASC' }, from: 'join' });
// odd input must not throw
for (const odd of [{}, { from: 'nonsense' }, { fields: ['nope'] }, { fields: null, where: null }, { agg: { fn: 'MAX', field: 'x' } }, { group: 'zzz', fields: ['Student.FirstName'] }, { order: { key: 'zzz', dir: 'ASC' } }]) {
  for (const db of ['school', 'shop', 'weird']) {
    try { w.evaluate(db, odd); } catch (e) { bad++; console.log('THREW on odd input', JSON.stringify(odd), db, e.message); }
  }
}
// the SQL text of one example
const ex = w.evaluate('school', { from: 'join', fields: ['Club.ClubName'], agg: { fn: 'COUNT', field: '*' }, where: [{ field: 'Student.Points', op: '>', value: '40' }], bool: 'AND', group: 'Club.ClubName', order: { key: 'COUNT(*)', dir: 'DESC' } });
const want = 'SELECT Club.ClubName, COUNT(*)\nFROM Student\nINNER JOIN Club ON Student.ClubCode = Club.ClubCode\nWHERE Student.Points > 40\nGROUP BY Club.ClubName\nORDER BY COUNT(*) DESC;';
if (ex.sql !== want) { bad++; console.log('SQL text differs:\n' + ex.sql); }
if (w.fmtValue(126, true) !== '126.00' || w.fmtValue(45.25, true) !== '45.25' || w.fmtValue(60.5, true) !== '60.50' || w.fmtValue(null) !== '(no value)') { bad++; console.log('fmtValue'); }


// ---- every query of the chapter that the widget can express, against the result table the chapter prints ----
{
  const lines = fs.readFileSync(path.join(process.cwd(), 'chapters', 'cs.sql.md'), 'utf8').split('\n');
  let covered = 0, skipped = 0, modified = false;
  for (let i = 0; i < lines.length; i++) {
    if (/^(#{1,6} |:::|Q:)/.test(lines[i])) modified = false;
    if (lines[i] !== '```text') continue;
    let j = i + 1; const body = [];
    while (!lines[j].startsWith('```')) body.push(lines[j++]);
    const sql = body.join(' ').replace(/\s+/g, ' ').trim();
    i = j;
    if (/^(INSERT|UPDATE|DELETE|ALTER)/.test(sql)) modified = true;
    if (!/^SELECT /.test(sql)) continue;
    if (modified) { skipped++; continue; }
    const m = /^SELECT (.+?) FROM (\w+)(?: INNER JOIN (\w+) ON [\w.]+ = [\w.]+)?(?: WHERE (.+?))?(?: GROUP BY ([\w.]+))?(?: ORDER BY ([\w.()*]+)(?: (ASC|DESC))?)?;$/.exec(sql);
    if (!m || (m[4] && /ORDER BY|,/.test(m[4])) || (m[4] && /[()]/.test(m[4])) || (m[4] && / AND /.test(m[4]) && / OR /.test(m[4])) || /,/.test(m[6] || '')) { skipped++; continue; }
    const items = m[1].split(',').map(function (x) { return x.trim(); });
    const plain = [], aggs = [];
    items.forEach(function (it) { const a = /^(COUNT|SUM|AVG)\((.+)\)$/.exec(it); if (a) aggs.push({ fn: a[1], field: a[2] }); else plain.push(it); });
    if (aggs.length > 1 || plain.includes('*')) { skipped++; continue; }
    const conds = m[4] ? m[4].split(/ AND | OR /).map(function (c) {
      const x = /^([\w.]+) (=|<>|<=|>=|<|>) (.+)$/.exec(c.trim());
      const v = x[3]; const q = /^'(.*)'$/.exec(v);
      return { field: x[1], op: x[2], value: q ? q[1] : v };
    }) : [];
    const db = /\b(Product|Sale)\b/.test(sql) ? 'shop' : 'school';
    if (/Contact/.test(sql)) { skipped++; continue; }
    const spec = { from: m[3] ? 'join' : m[2], fields: plain, agg: aggs[0] || null, where: conds, bool: / OR /.test(m[4] || '') ? 'OR' : 'AND', group: m[5] || '', order: m[6] ? { key: m[6], dir: m[7] || 'ASC' } : null };
    const r = w.evaluate(db, spec);
    // the printed table after the fence
    let k = i + 1, tbl = null;
    while (k < lines.length && !lines[k].startsWith('```') && !/^(#{1,6} |:::|Q:)/.test(lines[k])) { if (lines[k].startsWith('|')) { tbl = []; while (lines[k] && lines[k].startsWith('|')) { tbl.push(lines[k].trim().replace(/^\||\|$/g, '').split('|').map(function (c) { return c.trim(); })); k++; } break; } k++; }
    if (!tbl) { skipped++; continue; }
    const data = tbl.slice(2);
    covered++;
    if (r.error) { bad++; console.log('widget refused a chapter query:', sql, r.error); continue; }
    if (data.length !== r.rows.length) { bad++; console.log('row count', sql, data.length, r.rows.length); continue; }
    const strRows = r.rows.map(function (row) { return row.map(function (v, c) { return v === null ? '' : String(v); }); });
    const ok = data.every(function (row, a) { return row.every(function (cell, c) { const n = Number(cell); const g = r.rows[a][c]; return (cell !== '' && !isNaN(n) && typeof g === 'number') ? Math.abs(n - g) < 1e-9 : cell === strRows[a][c]; }); });
    if (!ok) { bad++; console.log('chapter table differs from widget for', sql); }
  }
  console.log('chapter queries checked against the widget: ' + covered + ' (not expressible or without a table: ' + skipped + ')');
}

console.log(bad === 0 ? 'cs-sql ok: ' + checked + ' queries match sqlite (' + withOrder + ' with ORDER BY), error rules and odd input fine' : bad + ' problems');
process.exitCode = bad === 0 ? 0 : 1;
