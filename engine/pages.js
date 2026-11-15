// pages.js — findable pages. The guide is one page with #hash routes, which search engines cannot index chapter by
// chapter. For the published site build.js also writes:
//   p/<chapter-id>.html   the chapter as a plain, static page (full text, maths, figures, answers folded away;
//                         quizzes and interactive tools are replaced by a note) with a link into the guide
//   p/index.html          every chapter, by course
//   p/page.css            the guide's stylesheet plus the few rules these pages add
//   sitemap.xml           (only when package.json "homepage" gives the public URL)
// The pages are not part of the offline app: the service worker neither precaches nor saves them.
'use strict';
const { escapeHtml, stripTags } = require('./lib');
const { plainText } = require('./site');

const EXTRA = `
/* static pages (engine/pages.js) */
body.static { margin: 0; background: var(--sheet); color: var(--ink); }
.p-bar { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 18px; padding: 12px max(16px, env(safe-area-inset-left)); border-bottom: 1px solid var(--rule); font-family: var(--f-ui); }
.p-brand { font-weight: 800; font-size: 1.15rem; color: var(--ink); text-decoration: none; }
.p-brand span { color: var(--accent, var(--sc)); }
.p-open { margin-left: auto; }
.p-main { max-width: 46rem; margin: 0 auto; padding: 8px 16px 72px; }
.p-main .chapter { display: block; }
.p-note { font-family: var(--f-ui); font-size: .95rem; padding: 12px 16px; border: 1px dashed var(--rule-ui, var(--rule)); border-radius: 10px; color: var(--ink-2); margin: 1.2em 0; }
.p-foot { margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--rule); font-family: var(--f-ui); display: grid; gap: 14px; }
.p-list h2 { margin-top: 1.8em; }
.p-list h3 { font-size: 1rem; margin: 1.2em 0 .3em; color: var(--ink-2); }
.p-list ul { margin: 0; padding-left: 1.2em; }
`;

const attr = (s) => escapeHtml(String(s || '')).replace(/"/g, '&quot;');
const clip = (s, n) => { s = String(s || '').replace(/\s+/g, ' ').trim(); return s.length <= n ? s : s.slice(0, s.lastIndexOf(' ', n - 1)).replace(/[,;:.\s]+$/, '') + '…'; };

/**
 * res: the result of site.buildSite; opts: { css, homepage: 'https://…/' | '', name: 'Zero to A*' }
 * returns { relPath: content } to add to the site files (after pwa.pwaFiles, so the offline cache leaves them out)
 */
function staticPages(res, opts) {
  const home = opts.homepage ? opts.homepage.replace(/\/*$/, '/') : '';
  const name = opts.name || 'Zero to A* Ω';
  const R = res.R;
  const subj = (id) => res.subjects.find(s => s.id === id) || { title: '' };
  const files = { 'p/page.css': opts.css + EXTRA };
  const list = res.chapters.filter(c => c.id !== 'home');
  const built = new Date().toISOString().slice(0, 10);

  const page = ({ file, title, desc, body, app, ld }) => `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>${escapeHtml(title)}</title>
<meta name="description" content="${attr(desc)}">
${home ? `<link rel="canonical" href="${attr(home + file)}">\n<meta property="og:url" content="${attr(home + file)}">\n<meta property="og:image" content="${attr(home + 'icon-512.png')}">` : ''}
<meta property="og:type" content="article">
<meta property="og:site_name" content="${attr(name)}">
<meta property="og:title" content="${attr(title)}">
<meta property="og:description" content="${attr(desc)}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="page.css">
${ld ? `<script type="application/ld+json">${JSON.stringify(ld).replace(/</g, '\\u003c')}</script>` : ''}
</head>
<body class="static">
<header class="p-bar"><a class="p-brand" href="../index.html">Zero to A<span>* Ω</span></a><a href="index.html">All chapters</a><a class="btn btn-sm p-open" href="../index.html#${attr(app)}">Open in the interactive guide</a></header>
<main class="p-main">${body}</main>
</body>
</html>
`;

  const staticIds = new Set(list.map(c => c.id));
  for (const c of list) {
    const s = subj(c.subject);
    const title = stripTags(R.inline(c.title));
    // links: #id → id.html, #id--section → id.html#id--section (a section of this page stays a #link)
    let html = c.html.replace(/<a href="#([^"]+)"/g, (m, href) => {
      const base = href.split('--')[0];
      if (base === c.id) return m;
      // a page with no static copy (Home, Settings) opens in the guide
      if (!staticIds.has(base)) return `<a href="../index.html#${attr(href)}"`;
      return `<a href="${attr(base)}.html${href.includes('--') ? '#' + attr(href) : ''}"`;
    });
    const openIt = `<a href="../index.html#${attr(c.id)}">open this chapter in the interactive guide</a>`;
    html = html
      .replace(/<div class="quiz"[^>]*><\/div>/g, `<p class="p-note">This chapter has a quick quiz with instant marking: ${openIt}.</p>`)
      .replace(/<div class="widget"[^>]*>\s*<\/div>/g, `<p class="p-note">An interactive tool sits here: ${openIt} to use it.</p>`);
    const desc = clip(c.meta.summary ? plainText(R.inline(c.meta.summary)) : plainText(c.html), 200);
    const chips = [c.meta.paper, c.meta.time].filter(Boolean).map(t => `<span class="chip">${escapeHtml(t)}</span>`).join('');
    const i = list.indexOf(c), prev = list[i - 1], next = list[i + 1];
    const body = `<article class="chapter s-${attr(c.subject)}">
<header class="ch-head"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html#${attr(c.subject)}">${escapeHtml(s.title)}</a><span aria-hidden="true">/</span><span>${escapeHtml(c.group || '')}</span></nav><h1>${R.inline(c.title)}</h1>${chips ? `<div class="chips">${chips}</div>` : ''}${c.meta.summary ? `<p class="lede">${R.inline(c.meta.summary)}</p>` : ''}</header>
<div class="prose">${html}</div>
<footer class="p-foot"><p><a class="btn" href="../index.html#${attr(c.id)}">Open this chapter in the interactive guide</a></p><p>The guide adds quizzes with instant marking, interactive tools, progress tracking, timed mock papers and offline use. It is free.</p>
<div class="pn">${prev ? `<a class="pn-prev" href="${attr(prev.id)}.html"><small>Previous</small><span>${stripTags(R.inline(prev.title))}</span></a>` : '<span></span>'}${next ? `<a class="pn-next" href="${attr(next.id)}.html"><small>Next</small><span>${stripTags(R.inline(next.title))}</span></a>` : '<span></span>'}</div></footer>
</article>`;
    files[`p/${c.id}.html`] = page({
      file: `p/${c.id}.html`, title: `${title} · ${s.title} · ${name}`, desc, body, app: c.id,
      ld: {
        '@context': 'https://schema.org', '@type': 'LearningResource', name: title, description: desc, inLanguage: 'en',
        isAccessibleForFree: true, learningResourceType: 'Study guide chapter', educationalLevel: 'A Level',
        isPartOf: { '@type': 'Course', name: `${s.title} · ${name}` }, dateModified: built, ...(home ? { url: home + `p/${c.id}.html` } : {})
      }
    });
  }

  // every chapter, by course and group
  let body = `<article class="chapter"><header class="ch-head"><h1>All chapters</h1><p class="lede">Every chapter of ${escapeHtml(name)} as a plain web page. The interactive guide has the same chapters with quizzes, tools, progress and offline use.</p></header><div class="prose p-list">`;
  for (const s of res.subjects) {
    const mine = list.filter(c => c.subject === s.id);
    if (!mine.length) continue;
    body += `<h2 id="${attr(s.id)}">${escapeHtml(s.title)}</h2>`;
    let group = null;
    for (const c of mine) {
      if (c.group !== group) { if (group !== null) body += '</ul>'; group = c.group; body += `<h3>${escapeHtml(group || '')}</h3><ul>`; }
      body += `<li><a href="${attr(c.id)}.html">${R.inline(c.title)}</a></li>`;
    }
    body += '</ul>';
  }
  body += '</div></article>';
  files['p/index.html'] = page({ file: 'p/index.html', title: `All chapters · ${name}`, desc: `Every chapter of ${name}, a free A Level guide from zero to A*: ${res.subjects.filter(s => list.some(c => c.subject === s.id) && s.kind === 'course').map(s => s.title).join(', ')}.`, body, app: 'home' });

  if (home) {
    files['sitemap.xml'] = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`
      + [home, home + 'p/index.html', ...list.map(c => home + `p/${encodeURIComponent(c.id)}.html`)].map(u => `<url><loc>${escapeHtml(u)}</loc><lastmod>${built}</lastmod></url>`).join('\n') + '\n</urlset>\n';
  }
  return files;
}

module.exports = { staticPages };
