// assets.js — the page template files. The course kit bundle replaces this module with the same files as strings.
// The text fonts (engine/fonts, SIL Open Font Licence) are embedded in the CSS so the page works offline.
'use strict';
const fs = require('fs');
const path = require('path');
const read = (f) => fs.readFileSync(path.join(__dirname, f), 'utf8');
const face = (family, file, style, weight) =>
  `@font-face{font-family:"${family}";src:url(data:font/woff2;base64,${fs.readFileSync(path.join(__dirname, 'fonts', file)).toString('base64')}) format("woff2");font-style:${style};font-weight:${weight};font-display:swap}`;
const fonts = [
  face('Literata', 'literata.woff2', 'normal', '400 700'),
  face('Literata', 'literata-italic.woff2', 'italic', '400 700'),
  face('Atkinson Next', 'atkinson-next.woff2', 'normal', '400 800')
].join('\n');
module.exports = {
  shell: read('shell.html'), css: fonts + '\n' + read('style.css'), core: read('core.js'), app: read('app.js'), study: read('widgets-study.js')
};
