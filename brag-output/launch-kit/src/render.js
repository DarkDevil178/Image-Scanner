// node render.js : renders build/assets.json through templates.html into ../out
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const OUT = path.join(__dirname, '..', 'out'); const A = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'build', 'assets.json')));
const only = process.argv[2] ? new RegExp(process.argv[2]) : null;
(async () => {
  const b = await chromium.launch(); const pages = [];
  for (let i = 0; i < 4; i++) { const p = await b.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', (e) => console.log('pageerror', e.message)); await p.goto('file://' + path.join(__dirname, 'templates.html')); await p.evaluate(() => window.ready); pages.push(p); }
  const list = A.filter((a) => !only || only.test(a.out)); let k = 0;
  await Promise.all(pages.map(async (p) => { for (;;) { const a = list[k++]; if (!a) break;
    const f = path.join(OUT, a.out); fs.mkdirSync(path.dirname(f), { recursive: true });
    await p.setViewportSize({ width: a.W, height: a.H }); await p.evaluate((s) => window.go(s), a); await p.waitForTimeout(60);
    await p.screenshot({ path: f, clip: { x: 0, y: 0, width: a.W, height: a.H } }); } }));
  console.log('rendered', list.length); await b.close();
})();
