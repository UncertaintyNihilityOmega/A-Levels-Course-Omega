// icons.js — the app icons: the end of a log. Dark green bark around a white face with faint green tree rings, and
// "AΩ" in dark green Caudex Bold (glyph outlines in logo-glyphs.json, SIL Open Font License). Designed on a 100-unit
// square, centre (50,50). No image files or tools: rasterised here with supersampling and written as PNG (zlib only);
// the textures are seeded value noise, so every build gives the same pixels. Used by pwa.js at build time; LOGO_SVG is
// also the top-bar mark (shell.html). Preview: node engine/icons.js <dir> writes every icon into <dir>.
'use strict';
const zlib = require('zlib');
const GL = require('./logo-glyphs.json');

const GREEN = '#1E4D2B', BARK = '#123220', STREAK = '#0A2112', FACE = '#FFFFFF';
const FACE_R = 43.5;
const RINGS = [5, 9, 12.5, 15.5, 19, 22, 25.5, 28.5, 31.5, 34.5, 37.5, 40.5].map((r, i) => ({
  r, cx: 50 + ((i * 7) % 3 - 1) * 0.6, cy: 50 + ((i * 5) % 3 - 1) * 0.6, w: i % 3 ? 0.7 : 1.2
}));
const RING_ALPHA = 0.22;

// ---------- letters: polygons in the 100-unit square (font size 50, baseline y = 66, centred, Ω kerned −2) ----------
const S = 50 / GL.upm;
const X0 = 50 - ((GL.A.adv + GL.O.adv) * S - 2) / 2;
const LETTERS = [[GL.A, X0], [GL.O, X0 + GL.A.adv * S - 2]]
  .flatMap(([g, ox]) => g.polys.map((p) => p.map(([x, y]) => [ox + x * S, 66 - y * S])));
const EDGES = LETTERS.flatMap((p) => p.map((a, i) => [a, p[(i + 1) % p.length]]));

/** Sorted [x, winding] crossings of the letter outlines with the horizontal line at y (non-zero fill rule). */
function crossings(y) {
  const out = [];
  for (const [[x1, y1], [x2, y2]] of EDGES) {
    if ((y1 <= y) === (y2 <= y)) continue;
    out.push([x1 + (y - y1) * (x2 - x1) / (y2 - y1), y2 > y1 ? 1 : -1]);
  }
  return out.sort((a, b) => a[0] - b[0]);
}

// ---------- noise ----------
function hash(i, j, seed) {
  let h = (Math.imul(i, 374761393) + Math.imul(j, 668265263) + Math.imul(seed, 1442695041)) | 0;
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
}
function vnoise(x, y, seed) {
  const i = Math.floor(x), j = Math.floor(y), fx = x - i, fy = y - j;
  const u = fx * fx * (3 - 2 * fx), v = fy * fy * (3 - 2 * fy);
  const a = hash(i, j, seed), b = hash(i + 1, j, seed), c = hash(i, j + 1, seed), d = hash(i + 1, j + 1, seed);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}
/** Fractal noise around 0 (about −0.5…0.5), frequencies fx, fy per unit. */
function fbm(x, y, fx, fy, oct, seed) {
  let s = 0, amp = 1, tot = 0, f = 1;
  for (let o = 0; o < oct; o++) { s += amp * vnoise(x * fx * f, y * fy * f, seed + o * 17); tot += amp; amp /= 2; f *= 2; }
  return (s / tot - 0.5) * 1.8;
}

const hex = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
const C = { green: hex(GREEN), bark: hex(BARK), streak: hex(STREAK), face: hex(FACE) };
const mix = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];

/** Colour of the design at (x, y) in the 100-unit square; inLetter from the scanline. */
function colourAt(x, y, inLetter) {
  if (inLetter) return C.green;
  // the face's edge is ragged (fine noise), like a sawn log
  const d0 = Math.hypot(x - 50, y - 50);
  const out = d0 > FACE_R + 2 || (d0 > FACE_R - 2 && Math.hypot(x + fbm(x, y, 0.6, 0.6, 1, 11) * 1.6 - 50, y + fbm(x, y, 0.6, 0.6, 1, 12) * 1.6 - 50) >= FACE_R);
  if (out) {
    // bark: long darker streaks
    const n = fbm(x, y, 0.9, 0.08, 2, 3) + 0.5;
    return mix(C.bark, C.streak, Math.min(1, Math.max(0, 1.6 * n - 0.55)));
  }
  // tree rings, gently wobbling
  const qx = x + fbm(x, y, 0.045, 0.045, 2, 21) * 3.2, qy = y + fbm(x, y, 0.045, 0.045, 2, 22) * 3.2;
  for (const g of RINGS) if (Math.abs(Math.hypot(qx - g.cx, qy - g.cy) - g.r) < g.w / 2) return mix(C.face, C.green, RING_ALPHA);
  return C.face;
}

/**
 * RGBA pixels of one icon. size: px; zoom: the design's scale about the centre (below 1 leaves more bark round the
 * face, for maskable icons); round: transparent outside the circle (favicon), else the whole square is drawn.
 */
function draw(size, { zoom = 1, round = false } = {}) {
  const N = size > 200 ? 3 : size > 64 ? 5 : 8, px = Buffer.alloc(size * size * 4);
  const k = 100 / size / zoom, off = 50 - 50 / zoom;
  const acc = new Float64Array(size * 4);
  for (let j = 0; j < size; j++) {
    acc.fill(0);
    for (let b = 0; b < N; b++) {
      const y = off + (j + (b + 0.5) / N) * k;
      const xs = crossings(y);
      let p = 0, wind = 0;
      for (let i = 0; i < size; i++) for (let a = 0; a < N; a++) {
        const x = off + (i + (a + 0.5) / N) * k;
        while (p < xs.length && xs[p][0] <= x) wind += xs[p++][1];
        if (round && Math.hypot(x - 50, y - 50) > 50 / zoom) continue;
        const c = colourAt(x, y, wind !== 0);
        const o = i * 4;
        acc[o] += c[0]; acc[o + 1] += c[1]; acc[o + 2] += c[2]; acc[o + 3] += 1;
      }
    }
    for (let i = 0; i < size; i++) {
      const o = i * 4, n = acc[o + 3], q = (j * size + i) * 4;
      if (!n) continue;
      px[q] = Math.round(acc[o] / n); px[q + 1] = Math.round(acc[o + 1] / n); px[q + 2] = Math.round(acc[o + 2] / n);
      px[q + 3] = Math.round(255 * n / (N * N));
    }
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

// ---------- SVG (favicon and the top-bar mark): the same design without the noise textures ----------
const f1 = (n) => +n.toFixed(1);
const LETTER_PATH = LETTERS.map((p) => 'M' + p.map(([x, y]) => `${f1(x)} ${f1(y)}`).join('L') + 'Z').join('');
function svg(attrs) {
  const rings = RINGS.map((g) => `<circle cx="${f1(g.cx)}" cy="${f1(g.cy)}" r="${g.r}" stroke-width="${g.w}"/>`).join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"${attrs || ''}><circle cx="50" cy="50" r="50" fill="${BARK}"/>`
    + `<circle cx="50" cy="50" r="${FACE_R}" fill="${FACE}"/><g fill="none" stroke="${GREEN}" stroke-opacity="${RING_ALPHA}">${rings}</g>`
    + `<path fill="${GREEN}" d="${LETTER_PATH}"/></svg>`;
}
const LOGO_SVG = svg(' width="34" height="34" aria-hidden="true" focusable="false"');

/** Every icon file: { relPath: Buffer | string }. */
function icons() {
  return {
    'icon-192.png': png(192, draw(192)),
    'icon-512.png': png(512, draw(512)),
    'icon-maskable-512.png': png(512, draw(512, { zoom: 0.88 })),   // face inside the 80% safe circle of a maskable icon
    'apple-touch-icon.png': png(180, draw(180)),                     // iOS rounds the corners; no transparent pixels
    'favicon-32.png': png(32, draw(32, { round: true })),
    'favicon.svg': svg() + '\n'
  };
}

module.exports = { icons, LOGO_SVG };

if (require.main === module) {
  const fs = require('fs'), path = require('path');
  const dir = process.argv[2] || '.';
  fs.mkdirSync(dir, { recursive: true });
  const t = Date.now();
  for (const [f, data] of Object.entries(icons())) fs.writeFileSync(path.join(dir, f), data);
  console.log(`icons written to ${path.resolve(dir)} in ${Date.now() - t} ms`);
}
