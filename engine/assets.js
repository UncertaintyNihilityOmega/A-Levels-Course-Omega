// assets.js — the page template files. The course kit bundle replaces this module with the same files as strings.
'use strict';
const fs = require('fs');
const path = require('path');
const read = (f) => fs.readFileSync(path.join(__dirname, f), 'utf8');
module.exports = {
  shell: read('shell.html'), css: read('style.css'), core: read('core.js'), app: read('app.js'), study: read('widgets-study.js')
};
