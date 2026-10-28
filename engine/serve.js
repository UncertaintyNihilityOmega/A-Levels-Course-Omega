// serve.js — tiny static file server for viewing a built site in the Claude browser pane. It serves site/ at the
// root, so sw.js (site/sw.js) controls the whole origin, as it controls /<repo>/ on GitHub Pages.
//   node engine/serve.js [dir=site] [port=5100]
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');

const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.ico': 'image/x-icon', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.otf': 'font/otf' };

function serve(dir, port) {
  const root = path.resolve(dir);
  http.createServer((req, res) => {
    let rel = decodeURIComponent(req.url.split('?')[0]);
    if (rel.endsWith('/')) rel += 'index.html';
    const file = path.join(root, rel);
    if (!file.startsWith(root)) { res.writeHead(403); return res.end(); }
    fs.readFile(file, (err, data) => {
      if (err) { res.writeHead(404, { 'content-type': 'text/plain' }); return res.end('Not found: ' + rel); }
      res.writeHead(200, { 'content-type': TYPES[path.extname(file)] || 'application/octet-stream', 'cache-control': 'no-store' });
      res.end(data);
    });
  }).listen(port, '127.0.0.1', () => console.log(`Serving ${root} at http://localhost:${port}/`));
}

if (require.main === module) serve(process.argv[2] || path.join(__dirname, '..', 'site'), Number(process.argv[3]) || 5100);
module.exports = { serve };
