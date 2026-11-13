// data/cs-check.click.js: browser test for the cs-check widget (flip, corrupt, options, check digits). Append it as a script to a copy of preview/widget.html, load that in headless Edge with --dump-dom and read the pre with id zta-click.
setTimeout(function () {
  var out = [];
  function log(s) { out.push(s); }
  try {
    var w = document.querySelector('.widget');
    var btns = Array.prototype.slice.call(w.querySelectorAll('button'));
    function byText(t) { return btns.filter(function (b) { return b.textContent.trim() === t; })[0]; }
    function result() { var rs = w.querySelectorAll('.w-read'); var r = rs[rs.length - 1]; if (document.querySelector('.w-tab[aria-pressed=true]').textContent.indexOf('Parity') === 0) r = rs[0]; return r ? r.innerText.replace(/\s+/g, ' ') : '(no readout)'; }
    var cells = Array.prototype.slice.call(w.querySelectorAll('table button'));
    log('cells ' + cells.length + ' first label: ' + cells[0].getAttribute('aria-label'));
    log('initial: ' + result());
    cells[3 * 8 + 3].click();
    log('after flip byte4 bit3: ' + result());
    log('cell label: ' + cells[3 * 8 + 3].getAttribute('aria-label'));
    cells[3 * 8 + 3].click();
    byText('Corrupt 1 random bit').click();
    log('corrupt 1: ' + result());
    byText('Reset the block').click();
    byText('Corrupt 2 random bits').click();
    log('corrupt 2: ' + result());
    byText('Reset the block').click();
    var sels = w.querySelectorAll('select');
    sels[0].value = 'odd'; sels[0].dispatchEvent(new Event('change'));
    log('odd, clean: ' + result());
    sels[1].value = 'right'; sels[1].dispatchEvent(new Event('change'));
    cells = Array.prototype.slice.call(w.querySelectorAll('table button'));
    cells[0].click();
    log('odd/right flip byte1 col0: ' + result());
    var tx = w.querySelector('input[type=text]');
    tx.value = '1111111 0000000'; tx.dispatchEvent(new Event('input'));
    log('bad data error: ' + (w.querySelector('.w-err').textContent));
    tx.value = '1111111 0000000 1010101 0101010 1100110 0011001 1000001'; tx.dispatchEvent(new Event('input'));
    log('good data error empty: ' + JSON.stringify(w.querySelector('.w-err').textContent));
    byText('Check digit').click();
    var inputs = w.querySelectorAll('input[type=text]');
    var code = inputs[inputs.length - 1];
    log('check initial: ' + result());
    code.value = '627093'; code.dispatchEvent(new Event('input'));
    log('627093: ' + result());
    var sel2 = Array.prototype.slice.call(w.querySelectorAll('select'));
    var taskSel = sel2[sel2.length - 1];
    taskSel.value = 'verify'; taskSel.dispatchEvent(new Event('change'));
    log('verify: code=' + code.value + ' ' + result());
    code.value = '48293614'; code.dispatchEvent(new Event('input'));
    log('swapped: ' + result());
    code.value = ''; code.dispatchEvent(new Event('input'));
    log('empty err: ' + w.querySelector('.w-err:not([style*="none"])').textContent);
  } catch (e) { log('EXCEPTION ' + e.message); }
  var pre = document.createElement('pre');
  pre.id = 'zta-click';
  pre.textContent = out.join('\n');
  document.body.appendChild(pre);
}, 800);
