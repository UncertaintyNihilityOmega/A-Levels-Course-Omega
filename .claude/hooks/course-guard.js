// course-guard.js — PreToolUse hook: keeps subagents inside one course folder.
// Only tool calls made by a subagent (input has agent_id) are checked; the Organizer's own calls pass.
// The allowed course comes from .run/guard-course.txt (e.g. "phys"); delete that file to switch the guard off.
// Run state lives in .run/, not .claude/: writes under .claude/ always ask for permission, even in Auto mode.
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const norm = (p) => path.resolve(p).replace(/\\/g, '/').toLowerCase();
const deny = (why) => {
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'PreToolUse', permissionDecision: 'deny',
    permissionDecisionReason: `Course guard: ${why}. Agents work only inside ${course ? 'courses/' + course : 'their course folder'}.` } }));
  process.exit(0);
};

let course = '';
try { course = fs.readFileSync(path.join(ROOT, '.run', 'guard-course.txt'), 'utf8').trim(); } catch (e) { process.exit(0); }
let input = {};
try { input = JSON.parse(fs.readFileSync(0, 'utf8') || '{}'); } catch (e) { process.exit(0); }
if (process.env.GUARD_LOG) fs.appendFileSync(process.env.GUARD_LOG, JSON.stringify({ keys: Object.keys(input), agent_id: input.agent_id, agent_type: input.agent_type, tool: input.tool_name }) + '\n');
if (!input.agent_id) process.exit(0);

const home = norm(require('os').homedir());
const COURSE = norm(path.join(ROOT, 'courses', course));
const ALLOWED = [COURSE, `${home}/.claude/projects/`, norm(require('os').tmpdir())];
const inside = (p) => { const n = norm(path.isAbsolute(p) ? p : path.join(input.cwd || ROOT, p)); return ALLOWED.some(a => n === a || n.startsWith(a + '/') || (a.endsWith('/') && n.startsWith(a))); };

const t = input.tool_name || '', ti = input.tool_input || {};
if (['Read', 'Write', 'Edit', 'NotebookEdit'].includes(t)) {
  const f = ti.file_path || ti.notebook_path || '';
  if (f && !inside(f)) deny(`${t} of ${f} is outside the course`);
} else if (t === 'Grep' || t === 'Glob') {
  const p = ti.path || input.cwd || ROOT;
  if (!inside(p)) deny(`${t} must be given path: the course folder (got ${p})`);
  if (/\.\.[\\/]/.test(ti.pattern || '') || /\.\.[\\/]/.test(ti.glob || '')) deny(`${t} pattern climbs out of the course`);
} else if (t === 'Bash' || t === 'PowerShell') {
  const c = String(ti.command || '');
  const lc = c.replace(/\\/g, '/').toLowerCase();
  if (/(^|[\s"'=;&|(])\.\.([/"'\s]|$)/.test(c)) deny('commands may not use ".." to leave the course folder');
  if (/(^|[\s;&|(])git(\s|$)/.test(lc)) deny('no git commands (the Organizer commits)');
  const others = ['math', 'phys', 'chem', 'bio', 'eng', 'bus', 'econ', 'acc', 'other'].filter(x => x !== course);
  if (new RegExp(`courses/(${others.join('|')})(/|\\b)`).test(lc)) deny('the command names another course');
  if (/(^|[\s"'/])(engine|core|archive|site|node_modules)\//.test(lc) && !lc.includes(`courses/${course}/`)) deny('the command names a project folder outside the course');
  const rootN = norm(ROOT);
  // absolute paths: c:/… on Windows, /Users/… on macOS
  for (const m of lc.matchAll(/(?:[a-z]:)?\/[^"'\s;&|]*/g)) if (m[0].startsWith(rootN) && !m[0].startsWith(COURSE)) deny(`the command names ${m[0]}`);
}
process.exit(0);
