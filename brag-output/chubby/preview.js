const { chromium } = require('playwright'); const { pandaSVG } = require('./chubby.js');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 640 } });
  const poses = [{ view: 'front' }, { view: 'side' }, { view: 'back' }, { expr: 'focused' }, { expr: 'proud', tag: { n: '#002', c: '#FF8A3D' } }, { expr: 'oops' }];
  await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@500&display=block" rel="stylesheet"></head><body style="margin:0;background:#ECEEF2;display:flex">${poses.map((o) => pandaSVG(o)).join('')}</body></html>`);
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300); await p.screenshot({ path: 'work/preview.png' }); await b.close(); })();
