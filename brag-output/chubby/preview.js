const { chromium } = require('playwright'); const { pandaSVG, LIB } = require('./chubby.js');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2340, height: 1200 } });
  const names = Object.keys(LIB);
  await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600&display=block" rel="stylesheet"></head><body style="margin:0;background:#FBF1E4;display:flex;flex-wrap:wrap;width:2340px">${names.map((n) => `<div style="width:260px;text-align:center;font:20px sans-serif">${pandaSVG(LIB[n], 260, 300)}<div>${n}</div></div>`).join('')}</body></html>`);
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400); await p.screenshot({ path: 'work/preview.png', fullPage: true }); await b.close(); })();
