const { chromium } = require('playwright'); const path = require('path');
const B = path.join(__dirname, '..', 'build'), O = path.join(__dirname, '..', 'out');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  for (const [src, dst] of [['brand.html', 'brand/brand-guidelines-002.pdf'], ['playbook.html', '00_START_HERE.pdf'], ['calendar.html', 'calendar.pdf']]) {
    await p.goto('file://' + path.join(B, src)); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
    require('fs').mkdirSync(path.dirname(path.join(O, dst)), { recursive: true });
    await p.pdf({ path: path.join(O, dst), width: '1600px', height: '1000px', printBackground: true }); console.log('pdf', dst); }
  await b.close(); })();
