// Usage: node _src/measure.cjs <base-url> <outdir>
// Screenshots key pages and measures the rules the design log asserts.
const { chromium } = require('playwright');
const [base, outdir] = process.argv.slice(2);
const pages = ['index.html', 'c/index.html', 'c/01-hello.html', 'c/07-pointers.html', 'c/08-structs.html', 'c/09-file-io.html', 'c/11-malloc.html', 'cpp.html', 'objc.html', 'csharp.html', 'holyc.html', 'rosetta.html', 'family.html', 'about.html', '404.html'];
const sizes = [[1280, 800], [375, 812]];
(async () => {
  const b = await chromium.launch();
  const report = [];
  for (const scheme of ['light', 'dark']) for (const [w, h] of sizes) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: scheme });
    const p = await ctx.newPage();
    for (const path of pages) {
      await p.goto(base + path, { waitUntil: 'networkidle' });
      await p.evaluate(() => document.fonts.ready);
      const m = await p.evaluate(() => {
        const vis = [...document.querySelectorAll('.hero-svg')].find(e => getComputedStyle(e).display !== 'none');
        const r = vis ? vis.getBoundingClientRect() : null;
        let minFont = 99, minEl = '';
        for (const el of document.querySelectorAll('body *')) {
          if (!el.childNodes.length || ![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
          const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
          const rr = el.getBoundingClientRect(); if (!rr.width) continue;
          let fs = parseFloat(cs.fontSize);
          if (el instanceof SVGElement && el.ownerSVGElement) { const s = el.ownerSVGElement; const vb = s.viewBox.baseVal; if (getComputedStyle(s).display === 'none') continue; fs = fs * s.getBoundingClientRect().width / vb.width; }
          if (fs < minFont) { minFont = fs; minEl = el.tagName + '.' + (el.getAttribute('class') || '') + ' "' + el.textContent.trim().slice(0, 20) + '"'; }
        }
        const wrap = document.querySelector('.wrap');
        return { scrollW: document.documentElement.scrollWidth, hero: r && { top: Math.round(r.top), bottom: Math.round(r.bottom), w: Math.round(r.width) },
          minFont: +minFont.toFixed(1), minEl, wrapW: wrap ? Math.round(wrap.getBoundingClientRect().width) : null };
      });
      report.push({ scheme, w, h, path, ...m, overflow: m.scrollW > w });
      if (path === 'index.html' || scheme === 'light') await p.screenshot({ path: `${outdir}/${path.replace(/\//g, '_')}-${w}-${scheme}.png`, fullPage: path !== 'index.html' });
    }
    await ctx.close();
  }
  await b.close();
  console.log(JSON.stringify(report, null, 0).replace(/},{/g, '},\n{'));
})();
