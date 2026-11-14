// data/cs-trace.run.js: node data/cs-trace.run.js <prog> : builds the probe page for a program, appends the click test, loads it in headless Edge, prints the result.
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const prog = process.argv[2] || 'total';
execSync('node kit/zta.js widget cs-trace "data-prog=\\"' + prog + '\\"" --probe', { stdio: 'ignore' });
let html = fs.readFileSync('preview/widget.html', 'utf8');
const test = fs.readFileSync('data/cs-trace.click.js', 'utf8');
html = html.replace('</body>', '<script>' + test + '</script></body>');
fs.mkdirSync('scratch', { recursive: true });
const f = path.resolve('scratch/trace-click.html');
fs.writeFileSync(f, html);
const edge = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const url = 'file:///' + f.split(path.sep).join('/');
const out = execSync('"' + edge + '" --headless=new --disable-gpu --virtual-time-budget=4000 --dump-dom "' + url + '"', { maxBuffer: 1e8, encoding: 'utf8' });
const m = out.match(/<pre id="zta-click">([\s\S]*?)<\/pre>/);
console.log(m ? m[1].replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&') : 'no result');
