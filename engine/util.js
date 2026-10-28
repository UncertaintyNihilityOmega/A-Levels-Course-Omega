// util.js — disk helpers shared by build.js, check.js, status.js, sync.js and the course kit.
'use strict';
const fs = require('fs');
const path = require('path');
const os = require('os');
const { spawnSync } = require('child_process');

const readJson = (p) => JSON.parse(fs.readFileSync(p, 'utf8'));
const readText = (p) => fs.existsSync(p) ? fs.readFileSync(p, 'utf8') : '';
const mdFiles = (dir) => fs.existsSync(dir) ? fs.readdirSync(dir).filter(f => f.endsWith('.md')).sort().map(name => ({ name, text: fs.readFileSync(path.join(dir, name), 'utf8') })) : [];

/** A course's widget code: widgets.js plus every widgets/<name>.js (one widget per file), in name order */
function courseWidgets(dir) {
  const parts = [readText(path.join(dir, 'widgets.js'))];
  const wd = path.join(dir, 'widgets');
  if (fs.existsSync(wd)) for (const f of fs.readdirSync(wd).filter(f => f.endsWith('.js')).sort()) parts.push(`/* widgets/${f} */\n` + fs.readFileSync(path.join(wd, f), 'utf8'));
  return parts.filter(s => s.trim()).join('\n;\n');
}

/** A course folder → a source for site.buildSite */
function loadCourse(dir) {
  const c = readJson(path.join(dir, 'course.json'));
  return {
    id: c.id, kind: 'course', title: c.title, short: c.short, code: c.code, years: c.years, desc: c.desc,
    chapters: c.chapters || [], aliases: c.aliases || {}, packages: c.packages || [], json: c,
    files: mdFiles(path.join(dir, 'chapters')), widgets: courseWidgets(dir), dir
  };
}

/** core/ → one source per core section + the core.json settings */
function loadCore(dir) {
  const core = readJson(path.join(dir, 'core.json'));
  const files = mdFiles(dir);
  const sources = core.sections.map(s => {
    const ids = new Set(s.chapters.map(c => c.id));
    return { id: s.id, kind: 'core', title: s.title, short: s.short, code: s.code, desc: s.desc, chapters: s.chapters, aliases: {}, files: files.filter(f => ids.has(f.name.replace(/\.md$/, ''))), widgets: '' };
  });
  // a core file that matches no section still has to be reported
  const known = new Set(core.sections.flatMap(s => s.chapters.map(c => c.id)));
  const stray = files.filter(f => !known.has(f.name.replace(/\.md$/, '')));
  if (stray.length) sources[0].files.push(...stray);
  sources[0].aliases = core.aliases || {};
  return { core, sources };
}

/** Run Python with UTF-8 output (the Windows console code page cannot print − or ²). Windows tries py, python3,
 *  python; macOS and Linux try python3 first (there `python` may be missing or Python 2) and never py. */
const PYTHONS = process.platform === 'win32' ? ['py', 'python3', 'python'] : ['python3', 'python'];
function runPython(args, opts = {}) {
  const env = { ...process.env, PYTHONUTF8: '1', PYTHONIOENCODING: 'utf-8' };
  for (const exe of PYTHONS) {
    const r = spawnSync(exe, args, { encoding: 'utf8', env, cwd: opts.cwd, timeout: opts.timeout || 60000 });
    if (r.error && r.error.code === 'ENOENT') continue;
    if (r.status === 9009) continue; // Windows Store alias stub
    return { ok: r.status === 0, code: r.status, out: (r.stdout || '') + (r.stderr || ''), exe };
  }
  return { ok: false, code: -1, out: `Python not found (tried ${PYTHONS.join(', ')})`, exe: null };
}

/** @font-face for the maths font: subset to the characters used (fontTools), or the whole font as a fallback. */
function mathFontFace(fontPath, chars) {
  if (!fs.existsSync(fontPath)) return '';
  const all = chars + '()[]{}|‖√∫∑∏0123456789+−=<>';
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'zta-font-'));
  try {
    fs.writeFileSync(path.join(tmp, 'chars.txt'), all);
    const out = path.join(tmp, 'math.woff2');
    const r = runPython(['-m', 'fontTools.subset', fontPath, `--text-file=${path.join(tmp, 'chars.txt')}`, '--layout-features=*', '--flavor=woff2', `--output-file=${out}`]);
    if (r.ok && fs.existsSync(out)) return `@font-face{font-family:"Guide Math";src:url(data:font/woff2;base64,${fs.readFileSync(out).toString('base64')}) format("woff2");font-display:swap}`;
  } catch (e) { /* fall through */ } finally { fs.rmSync(tmp, { recursive: true, force: true }); }
  return `@font-face{font-family:"Guide Math";src:url(data:font/otf;base64,${fs.readFileSync(fontPath).toString('base64')}) format("opentype");font-display:swap}`;
}

/** Write {relPath: content} into dir, removing stale chunk files. */
function writeSite(dir, files) {
  fs.mkdirSync(path.join(dir, 'c'), { recursive: true });
  const keep = new Set(Object.keys(files).filter(k => k.startsWith('c/')).map(k => k.slice(2)));
  for (const f of fs.readdirSync(path.join(dir, 'c'))) if (!keep.has(f)) fs.rmSync(path.join(dir, 'c', f));
  for (const [rel, content] of Object.entries(files)) fs.writeFileSync(path.join(dir, rel), content);
}

module.exports = { readJson, readText, mdFiles, courseWidgets, loadCourse, loadCore, runPython, mathFontFace, writeSite };
