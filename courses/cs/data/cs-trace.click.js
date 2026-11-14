// data/cs-trace.click.js: browser test for cs-trace. Run: node data/cs-trace.run.js <prog>
setTimeout(function () {
  var out = [];
  function log(s) { out.push(s); }
  try {
    var w = document.querySelector('.widget');
    function btn(t) { return Array.prototype.filter.call(w.querySelectorAll('button'), function (b) { return b.textContent.trim() === t; })[0]; }
    function rows() { return Array.prototype.map.call(w.querySelectorAll('tbody tr'), function (r) { return Array.prototype.map.call(r.children, function (c) { return c.textContent; }).join('|'); }); }
    function marked() { var L = w.querySelector('[aria-label^="Pseudocode program"]'); return Array.prototype.filter.call(L.children, function (d) { return d.textContent.indexOf('▶') >= 0; }).map(function (d) { return d.textContent.trim(); }); }
    var next = btn('Next'), back = btn('Back'), reset = btn('Reset');
    log('start: back disabled=' + back.disabled + ' rows=' + JSON.stringify(rows()));
    var n = 0;
    while (!next.disabled && n < 200) { next.click(); n++; }
    log('after ' + n + ' Next clicks: next disabled=' + next.disabled + ' label=' + w.querySelector('.w-step').textContent);
    log('table: ' + rows().join(' / '));
    log('marked line: ' + JSON.stringify(marked()));
    log('live: ' + w.querySelector('[aria-live=polite]').textContent);
    back.click();
    log('after Back: ' + w.querySelector('.w-step').textContent + ' rows=' + rows().length);
    reset.click();
    log('after Reset: ' + w.querySelector('.w-step').textContent + ' rows=' + JSON.stringify(rows()) + ' marked=' + JSON.stringify(marked()));
    next.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    log('after ArrowRight: ' + w.querySelector('.w-step').textContent);
    var sel = w.querySelector('select');
    if (sel) {
      for (var i = 0; i < sel.options.length; i++) {
        sel.value = String(i); sel.dispatchEvent(new Event('change'));
        var m = 0; while (!btn('Next').disabled && m < 200) { btn('Next').click(); m++; }
        log('run ' + i + ' (' + sel.options[i].text + '): ' + m + ' steps; last rows: ' + rows().slice(-2).join(' / '));
      }
    }
  } catch (e) { log('EXCEPTION ' + e.message); }
  var pre = document.createElement('pre');
  pre.id = 'zta-click';
  pre.textContent = out.join('\n');
  document.body.appendChild(pre);
}, 600);
