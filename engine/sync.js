// sync.js — refreshes every course folder from the engine (run after any engine, design or plan change):
//   - bundles engine/kit-src/zta.js (+ lib, plot, site, katex, markdown-it, page assets) into kit/zta.js
//   - copies kit/STYLE.md, kit/WIDGETS.md, kit/EXAMPLE.md (the model chapter) and kit/math.otf
//   - writes kit/LINKS.md (chapter ids of every other course) and CLAUDE.md (from engine/templates)
//   - writes .claude/launch.json (the "preview" server) and creates missing STATUS/REVIEW/REQUESTS/widgets files
//   node engine/sync.js [course ...]
'use strict';
const fs = require('fs');
const path = require('path');
const esbuild = require('esbuild');
const { readJson, loadCore } = require('./util');

const ROOT = path.join(__dirname, '..');
const ENGINE = __dirname;
const EXAMPLE = 'courses/math/chapters/math.p1.quadratics.md';
const PORTS = { math: 5101, phys: 5102, chem: 5103, bio: 5104, eng: 5105, bus: 5106, econ: 5107, acc: 5108, other: 5109 };
const only = process.argv.slice(2);

const { core } = loadCore(path.join(ROOT, 'core'));
const courseIds = fs.readdirSync(path.join(ROOT, 'courses')).filter(d => fs.existsSync(path.join(ROOT, 'courses', d, 'course.json')))
  .sort((a, b) => core.order.indexOf(a) - core.order.indexOf(b));
const courses = courseIds.map(id => readJson(path.join(ROOT, 'courses', id, 'course.json')));

// ---------- link data: every planned id in the project ----------
const links = { ids: {}, aliases: { ...(core.aliases || {}) }, ports: PORTS };
const sections = [...core.sections.map(s => ({ ...s, core: true })), ...courses];
sections.sort((a, b) => core.order.indexOf(a.id) - core.order.indexOf(b.id));
for (const s of sections) {
  for (const c of s.chapters) links.ids[c.id] = { t: c.title, s: s.id };
  Object.assign(links.aliases, s.aliases || {});
}
const isWritten = (s, id) => fs.existsSync(path.join(ROOT, s.core ? 'core' : `courses/${s.id}/chapters`, id + '.md'));

async function bundle() {
  const assets = require('./assets');
  const virtual = {
    name: 'zta-virtual',
    setup(b) {
      b.onResolve({ filter: /^zta:(assets|links)$/ }, a => ({ path: a.path, namespace: 'zta' }));
      b.onLoad({ filter: /.*/, namespace: 'zta' }, a => ({
        contents: `module.exports = ${JSON.stringify(a.path === 'zta:assets' ? assets : links)};`, loader: 'js'
      }));
    }
  };
  const r = await esbuild.build({
    entryPoints: [path.join(ENGINE, 'kit-src', 'zta.js')], bundle: true, platform: 'node', target: 'node18', format: 'cjs',
    minify: true, legalComments: 'none', write: false, plugins: [virtual], logLevel: 'error',
    banner: { js: `// Zero to A* course kit, built ${new Date().toISOString().slice(0, 10)} by engine/sync.js. Do not edit or read: run node kit/zta.js` }
  });
  return r.outputFiles[0].text;
}

function linksMd(self) {
  let out = `# LINKS: chapter ids outside ${self.title}\n\nLink with \`[Title](#id)\`. ✓ = written already; the others are planned and show as plain text until\nthey are written. Grep this file (e.g. \`grep -i "vector" kit/LINKS.md\`) rather than reading it all.\n`;
  for (const s of sections) {
    if (s.id === self.id) continue;
    out += `\n## ${s.title} (${s.id})\n`;
    for (const c of s.chapters) out += `- ${c.id} · ${c.title}${isWritten(s, c.id) ? ' ✓' : ''}\n`;
  }
  return out;
}

function render(tpl, vars) {
  const lead = vars.LEAD;
  tpl = tpl.replace(/\{\{#LEAD\}\}([\s\S]*?)\{\{\/LEAD\}\}/g, (m, x) => lead ? x : '')
    .replace(/\{\{#NOLEAD\}\}([\s\S]*?)\{\{\/NOLEAD\}\}/g, (m, x) => lead ? '' : x);
  return tpl.replace(/\{\{(\w+)\}\}/g, (m, k) => vars[k] !== undefined ? String(vars[k]) : m).replace(/\n{3,}/g, '\n\n');
}

const writeIfMissing = (p, text) => { if (!fs.existsSync(p)) { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, text); return true; } return false; };

(async () => {
  const kit = await bundle();
  const tpl = fs.readFileSync(path.join(ENGINE, 'templates', 'course-CLAUDE.md'), 'utf8');
  const example = `<!-- kit/EXAMPLE.md: the model chapter (${path.basename(EXAMPLE)}), copied by the Organizer. Match its tone, structure and formatting. -->\n\n` + fs.readFileSync(path.join(ROOT, EXAMPLE), 'utf8');
  let n = 0;
  for (const c of courses) {
    if (only.length && !only.includes(c.id)) continue;
    const dir = path.join(ROOT, 'courses', c.id);
    const kd = path.join(dir, 'kit');
    fs.mkdirSync(kd, { recursive: true });
    fs.writeFileSync(path.join(kd, 'zta.js'), kit);
    for (const f of ['STYLE.md', 'WIDGETS.md']) fs.copyFileSync(path.join(ENGINE, 'kit-src', f), path.join(kd, f));
    fs.writeFileSync(path.join(kd, 'EXAMPLE.md'), example);
    fs.writeFileSync(path.join(kd, 'LINKS.md'), linksMd(c));
    fs.copyFileSync(path.join(ENGINE, 'latinmodern-math.otf'), path.join(kd, 'math.otf'));
    const lead = c.lead !== false;
    fs.writeFileSync(path.join(dir, 'CLAUDE.md'), render(tpl, {
      TITLE: c.title, ID: c.id, PORT: PORTS[c.id] || 5199, LEAD: lead,
      OWNER: lead ? 'Specialist' : 'Organizer', REVIEWER: lead ? 'Specialist writes, Writer closes' : 'Organizer writes, Writer closes'
    }));
    fs.mkdirSync(path.join(dir, '.claude'), { recursive: true });
    fs.writeFileSync(path.join(dir, '.claude', 'launch.json'), JSON.stringify({
      version: '0.0.1',
      configurations: [{ name: 'preview', runtimeExecutable: 'node', runtimeArgs: ['kit/zta.js', 'serve', String(PORTS[c.id] || 5199)], port: PORTS[c.id] || 5199 }]
    }, null, 2) + '\n');
    for (const d of ['chapters', 'checks']) fs.mkdirSync(path.join(dir, d), { recursive: true });
    for (const f of ['STATUS.md', 'REVIEW.md', 'REQUESTS.md', 'widgets.js']) {
      writeIfMissing(path.join(dir, f), fs.readFileSync(path.join(ENGINE, 'templates', f), 'utf8').replace(/\{\{TITLE\}\}/g, c.title).replace(/\{\{ID\}\}/g, c.id));
    }
    n++;
  }
  console.log(`synced ${n} course(s); kit ${(kit.length / 1024).toFixed(0)} KB`);
})().catch(e => { console.error(e); process.exit(1); });
