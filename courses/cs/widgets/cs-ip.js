(function () {
  'use strict';

  // ---- pure arithmetic (also tested in Node: data/cs.ip_test.js) ----
  function parseIp(text) {
    const parts = String(text).trim().split('.');
    if (parts.length !== 4) return { error: 'An IPv4 address has four numbers separated by full stops, such as 192.168.1.20.' };
    let value = 0;
    for (let i = 0; i < 4; i++) {
      if (!/^\d{1,3}$/.test(parts[i])) return { error: 'Each part must be a whole number from 0 to 255 ("' + parts[i] + '" is not).' };
      const n = parseInt(parts[i], 10);
      if (n > 255) return { error: n + ' is greater than 255, so it is not a valid IPv4 number.' };
      value = value * 256 + n;
    }
    return { value: value };
  }

  function maskFromPrefix(prefix) {
    return prefix <= 0 ? 0 : (Math.pow(2, 32) - Math.pow(2, 32 - prefix));
  }

  function parseMask(text) {
    const r = parseIp(text);
    if (r.error) return { error: r.error.replace('IPv4 address', 'subnet mask') };
    const inverse = Math.pow(2, 32) - 1 - r.value;     // host bits as 1s
    const k = Math.round(Math.log2(inverse + 1));
    if (Math.pow(2, k) !== inverse + 1) return { error: 'A subnet mask is a block of 1s followed by a block of 0s, so this mask is not valid.' };
    const prefix = 32 - k;
    if (prefix < 8 || prefix > 30) return { error: 'This tool handles prefixes from /8 to /30.' };
    return { prefix: prefix };
  }

  function dotted(value) {
    return [Math.floor(value / 16777216) % 256, Math.floor(value / 65536) % 256, Math.floor(value / 256) % 256, value % 256].join('.');
  }

  function bits32(value) {
    let s = value.toString(2);
    while (s.length < 32) s = '0' + s;
    return s;
  }

  // AND of two 32-bit numbers held as non-negative numbers, done bit by bit
  function and32(a, b) {
    const x = bits32(a), y = bits32(b);
    let out = '';
    for (let i = 0; i < 32; i++) out += (x[i] === '1' && y[i] === '1') ? '1' : '0';
    return parseInt(out, 2);
  }

  function addressType(ip) {
    const a = Math.floor(ip / 16777216), b = Math.floor(ip / 65536) % 256;
    if (a === 10) return { kind: 'private', text: 'private (range 10.0.0.0 to 10.255.255.255, 10.0.0.0/8)' };
    if (a === 172 && b >= 16 && b <= 31) return { kind: 'private', text: 'private (range 172.16.0.0 to 172.31.255.255, 172.16.0.0/12)' };
    if (a === 192 && b === 168) return { kind: 'private', text: 'private (range 192.168.0.0 to 192.168.255.255, 192.168.0.0/16)' };
    if (a === 127) return { kind: 'loopback', text: 'loopback (this device talking to itself, not a public address)' };
    if (a === 169 && b === 254) return { kind: 'link-local', text: 'link-local (given when no DHCP server answers, not a public address)' };
    if (a === 0 || a >= 224) return { kind: 'reserved', text: 'reserved (not an address for an ordinary device)' };
    return { kind: 'public', text: 'public (not in a private range)' };
  }

  function calc(ipText, prefix) {
    const r = parseIp(ipText);
    if (r.error) return { error: r.error };
    const p = Math.round(Number(prefix));
    if (!isFinite(p) || p < 8 || p > 30) return { error: 'The prefix length must be from 8 to 30.' };
    const ip = r.value;
    const mask = maskFromPrefix(p);
    const network = and32(ip, mask);
    const hostBits = 32 - p;
    const size = Math.pow(2, hostBits);
    const broadcast = network + size - 1;
    return {
      ip: ip, prefix: p, mask: mask, network: network, broadcast: broadcast,
      first: network + 1, last: broadcast - 1, hostBits: hostBits,
      hosts: size - 2, type: addressType(ip),
      isNetwork: ip === network, isBroadcast: ip === broadcast
    };
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { calc: calc, parseIp: parseIp, parseMask: parseMask, dotted: dotted, bits32: bits32, maskFromPrefix: maskFromPrefix };
  }

  // ---- the widget ----
  W.register('cs-ip', function (el, opts) {
    const f = W.frame(el, 'IPv4 address and subnet mask', 'Change the address or the prefix and watch the network and host parts');
    const body = f.body;
    const mono = 'ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';

    let startIp = (opts && opts.ip) || '192.168.10.77';
    if (parseIp(startIp).error) startIp = '192.168.10.77';
    let startPrefix = parseInt(opts && opts.prefix, 10);
    if (!isFinite(startPrefix) || startPrefix < 8 || startPrefix > 30) startPrefix = 24;

    let syncing = false;
    const err = W.h('div', { class: 'w-err', style: { display: 'none' } });
    err.setAttribute('role', 'alert');

    const ipField = W.field({ label: 'IPv4 address', value: startIp, type: 'text', width: '150px', oninput: function () { update(); } });
    const slider = W.sliderNum({ label: 'Prefix length (/n)', min: 8, max: 30, step: 1, value: startPrefix, oninput: function () {
      if (syncing) return;
      const p = Number(slider.get());
      if (isFinite(p) && Math.round(p) >= 8 && Math.round(p) <= 30) syncMask();   // an invalid prefix leaves the mask at the last valid one
      update();
    } });
    const maskField = W.field({ label: 'Subnet mask', value: dotted(maskFromPrefix(startPrefix)), type: 'text', width: '150px', oninput: function () { fromMask(); } });

    body.appendChild(W.h('div', { class: 'w-row' }, ipField.el, maskField.el));
    body.appendChild(slider.el);
    body.appendChild(err);

    const summary = W.h('p', { class: 'w-note', style: { fontWeight: '600' } });
    summary.setAttribute('aria-live', 'polite');
    body.appendChild(summary);

    const list = W.h('dl', { style: { margin: '8px 0 0', display: 'grid', gap: '6px' } });
    body.appendChild(list);
    body.appendChild(W.h('p', { class: 'w-note', text: 'Bold coloured digits to the left of the bar | are the network part; the plain digits to the right are the host part. Usable hosts = 2 to the power of the host bits, minus 2 (the network address and the broadcast address cannot be given to devices).' }));

    function syncMask() {
      syncing = true;
      maskField.input.value = dotted(maskFromPrefix(Math.round(Number(slider.get()))));
      syncing = false;
    }

    function fromMask() {
      const m = parseMask(maskField.input.value);
      if (m.error) { show(m.error); return; }
      syncing = true;
      slider.set(m.prefix);
      syncing = false;
      update();
    }

    function show(message) {
      err.textContent = message;
      err.style.display = message ? '' : 'none';
      list.style.display = message ? 'none' : 'grid';
      if (message) summary.textContent = '';
    }

    // binary display: four octets, network bits bold, a bar at the split
    function binaryEl(value, prefix) {
      const s = bits32(value);
      const wrap = W.h('span', { style: { display: 'inline-flex', flexWrap: 'wrap', columnGap: '3px', fontFamily: mono, fontSize: '14px' } });
      for (let o = 0; o < 4; o++) {
        const start = o * 8;
        const oct = s.slice(start, start + 8);
        const cell = W.h('span', { style: { whiteSpace: 'nowrap' } });
        const split = prefix - start;               // number of network bits inside this octet
        const nets = Math.max(0, Math.min(8, split));
        if (nets > 0) cell.appendChild(W.h('span', { text: oct.slice(0, nets), style: { fontWeight: '700', color: 'var(--sc)' } }));
        if (split > 0 && split <= 8 && !(split === 8 && o === 3)) {
          const bar = W.h('span', { text: '|', style: { color: 'var(--ink-3)', margin: '0 1px' } });
          bar.setAttribute('aria-hidden', 'true');
          cell.appendChild(bar);
        }
        if (nets < 8) cell.appendChild(W.h('span', { text: oct.slice(nets), style: { color: 'var(--ink-2)' } }));
        if (o < 3) cell.appendChild(document.createTextNode('.'));
        wrap.appendChild(cell);
      }
      return wrap;
    }

    function row(label, content) {
      const dd = W.h('dd', { style: { margin: '0', overflowWrap: 'anywhere' } });
      if (typeof content === 'string') dd.textContent = content; else dd.appendChild(content);
      list.appendChild(W.h('div', {}, W.h('dt', { class: 'w-lab', text: label }), dd));
    }

    function update() {
      const r = calc(ipField.get(), slider.get());
      if (r.error) { show(r.error); return; }
      show('');
      list.textContent = '';
      row('Address in binary', binaryEl(r.ip, r.prefix));
      row('Subnet mask in binary (/' + r.prefix + ')', binaryEl(r.mask, r.prefix));
      row('Address AND mask = network address in binary', binaryEl(r.network, r.prefix));
      row('Network address', dotted(r.network));
      row('First usable host', dotted(r.first));
      row('Last usable host', dotted(r.last));
      row('Broadcast address', dotted(r.broadcast));
      row('Network bits and host bits', r.prefix + ' network bits, ' + r.hostBits + ' host bits');
      row('Usable hosts (2^' + r.hostBits + ' − 2)', String(r.hosts));
      row('Type of address', r.type.text);
      let s = dotted(r.ip) + '/' + r.prefix + ': network ' + dotted(r.network) + ', ' + r.hosts + ' usable hosts, ' + r.type.kind + '.';
      if (r.isNetwork) s += ' This is the network address, so it cannot be given to a device.';
      if (r.isBroadcast) s += ' This is the broadcast address, so it cannot be given to a device.';
      summary.textContent = s;
    }

    update();
  });
})();
