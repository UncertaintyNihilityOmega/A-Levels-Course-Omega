// data/test_bio-sav.js: run `node data/test_bio-sav.js` in the course folder; checks the maths of widgets/bio-sav.js.
const assert = require('assert');
const path = require('path');
const { geom, centreTime, uncoloured, sf } = require(path.join(process.cwd(), 'widgets', 'bio-sav.js'));
const near = (a, b, t = 1e-9) => assert(Math.abs(a - b) < t, a + ' vs ' + b);
let g = geom('cube', { a: 2 }); near(g.sa, 24); near(g.v, 8);
g = geom('cuboid', { a: 4, b: 2, c: 1 }); near(g.sa, 28); near(g.v, 8);
g = geom('cylinder', { r: 0.5, len: 4 }); near(g.sa / g.v, 4.5, 0.005); near(g.sa, 14.137, 0.001);
near(centreTime('cube', { a: 2 }), 10); near(centreTime('cuboid', { a: 4, b: 2, c: 1 }), 5); near(centreTime('cylinder', { r: 1, len: 3 }), 10);
near(uncoloured('cube', { a: 1 }, 3), 0.064);           // front 0.3 cm: (1 - 0.6)^3
near(uncoloured('cube', { a: 2 }, 3), 2.744 / 8);
near(uncoloured('cube', { a: 2 }, 25), 0);
near(uncoloured('cube', { a: 2 }, 0), 1);
assert.strictEqual(sf(3.14159), '3.14'); assert.strictEqual(sf(NaN), '–'); assert.strictEqual(sf(0), '0');
assert(!isNaN(uncoloured('cube', { a: 0 }, 5)));
console.log('bio-sav maths ok');
