// icons.js — the app icons, drawn from the brand mark in the top bar (a red examiner's ring, turned −9°, around "A*").
// No image files or tools: the mark is a few shapes, rasterised here with 8×8 (4×4 for large sizes) supersampling and written as PNG
// (zlib only). Used by pwa.js at build time. Preview: node engine/icons.js <dir> writes every icon into <dir>.
'use strict';
const zlib = require('zlib');

const TURN = -9 * Math.PI / 180;   // .brand-mark { transform: rotate(-9deg) }

// The mark in units of the ring's outer radius, centre (0,0), y down, before the turn.
// "A": flat apex, legs and counter drawn as polygons (even-odd), like Atkinson Hyperlegible Next at weight 800.
const A_OUTER = [[-0.48, 0.31], [-0.23, -0.31], [-0.09, -0.31], [0.16, 0.31], [0.01, 0.31], [-0.05, 0.155], [-0.27, 0.155], [-0.33, 0.31]];
const A_COUNTER = [[-0.16, -0.112], [-0.091, 0.06], [-0.229, 0.06]];
// "*": five square-ended arms (superscript, upper right)
const STAR = { x: 0.31, y: -0.2, r: 0.16, w: 0.08, arms: 5 };
const ARMS = Array.from({ length: STAR.arms }, (_, k) => { const a = -Math.PI / 2 + k * 2 * Math.PI / STAR.arms; return [Math.cos(a), Math.sin(a)]; });
const COS = Math.cos(-TURN), SIN = Math.sin(-TURN);

function inPoly(x, y, poly) {
  let inside = false;
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const [xi, yi] = poly[i], [xj, yj] = poly[j];
    if ((yi > y) !== (yj > y) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}
/** Is the mark's point (x,y) red? ring = stroke width as a fraction of the radius */
function inMark(x, y, ring) {
  const d = Math.hypot(x, y);
  if (d <= 1 && d >= 1 - ring) return true;
  if (d > 0.62) return false;
  // undo the turn, then test the letters
  const u = x * COS - y * SIN, v = x * SIN + y * COS;
  if (u < 0.17 && inPoly(u, v, A_OUTER) && !inPoly(u, v, A_COUNTER)) return true;
  const sx = u - STAR.x, sy = v - STAR.y;
  if (sx * sx + sy * sy > STAR.r * STAR.r) return false;
  for (const [cx, cy] of ARMS) {
    const along = sx * cx + sy * cy;
    if (along >= 0 && along <= STAR.r && Math.abs(sy * cx - sx * cy) <= STAR.w / 2) return true;
  }
  return false;
}

const hex = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];

/**
 * RGBA pixels of one icon.
 * size: px; scale: ring radius as a fraction of half the size; ink, paper: '#RRGGBB';
 * square: fill the whole square with paper (app icons) or only the disc inside the ring (favicon, transparent corners).
 */
function draw(size, { scale, ink, paper, square, ring }) {
  const I = hex(ink), P = hex(paper), N = size > 200 ? 4 : 8, px = Buffer.alloc(size * size * 4);
  const R = scale * size / 2, cx = size / 2, cy = size / 2;
  for (let j = 0; j < size; j++) for (let i = 0; i < size; i++) {
    let red = 0, disc = 0;
    for (let b = 0; b < N; b++) for (let a = 0; a < N; a++) {
      const x = (i + (a + 0.5) / N - cx) / R, y = (j + (b + 0.5) / N - cy) / R;
      if (inMark(x, y, ring)) red++;
      else if (square || Math.hypot(x, y) <= 1) disc++;
    }
    const all = N * N, cover = (red + disc) / all, o = (j * size + i) * 4;
    if (!cover) continue;
    const t = red / (red + disc);
    for (let k = 0; k < 3; k++) px[o + k] = Math.round(P[k] + (I[k] - P[k]) * t);
    px[o + 3] = Math.round(255 * cover);
  }
  return px;
}

// ---------- PNG (RGBA, 8 bit) ----------
const CRC = new Int32Array(256).map((_, n) => { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; return c; });
const crc32 = (buf) => { let c = -1; for (const b of buf) c = CRC[(c ^ b) & 255] ^ (c >>> 8); return (c ^ -1) >>> 0; };
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length);
  const td = Buffer.concat([Buffer.from(type, 'ascii'), data]);
  const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(td));
  return Buffer.concat([len, td, crc]);
}
function png(size, px) {
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(size, 0); ihdr.writeUInt32BE(size, 4); ihdr[8] = 8; ihdr[9] = 6;
  const raw = Buffer.alloc(size * (size * 4 + 1));
  for (let j = 0; j < size; j++) px.copy(raw, j * (size * 4 + 1) + 1, j * size * 4, (j + 1) * size * 4);
  return Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), chunk('IHDR', ihdr), chunk('IDAT', zlib.deflateSync(raw, { level: 9 })), chunk('IEND', Buffer.alloc(0))]);
}

// ---------- SVG favicon (same shapes) ----------
function svg({ ink, paper, ring }) {
  const f = (n) => +n.toFixed(4);
  const pts = (p) => p.map(([x, y]) => `${f(x)} ${f(y)}`).join(' L');
  const arms = ARMS.map(([cx, cy]) => `M${f(STAR.x)} ${f(STAR.y)}L${f(STAR.x + cx * STAR.r)} ${f(STAR.y + cy * STAR.r)}`).join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1.02 -1.02 2.04 2.04"><circle r="${f(1 - ring / 2)}" fill="${paper}" stroke="${ink}" stroke-width="${ring}"/>`
    + `<g transform="rotate(${TURN * 180 / Math.PI})" fill="${ink}"><path fill-rule="evenodd" d="M${pts(A_OUTER)}Z M${pts(A_COUNTER)}Z"/>`
    + `<path d="${arms}" stroke="${ink}" stroke-width="${STAR.w}" fill="none"/></g></svg>\n`;
}

/** Every icon file: { relPath: Buffer | string }. ink = --red, paper = --sheet. */
function icons(ink, paper) {
  const app = (size, scale) => png(size, draw(size, { scale, ink, paper, square: true, ring: 0.12 }));
  return {
    'icon-192.png': app(192, 0.80),
    'icon-512.png': app(512, 0.80),
    'icon-maskable-512.png': app(512, 0.66),   // inside the 80% safe circle of a maskable icon
    'apple-touch-icon.png': app(180, 0.76),     // iOS rounds the corners; transparent pixels would turn black
    'favicon-32.png': png(32, draw(32, { scale: 0.98, ink, paper, square: false, ring: 0.15 })),
    'favicon.svg': svg({ ink, paper, ring: 0.12 })
  };
}

module.exports = { icons };

if (require.main === module) {
  const fs = require('fs'), path = require('path');
  const dir = process.argv[2] || '.';
  fs.mkdirSync(dir, { recursive: true });
  for (const [f, data] of Object.entries(icons('#C8102E', '#FFFFFF'))) fs.writeFileSync(path.join(dir, f), data);
  console.log('icons written to ' + path.resolve(dir));
}
