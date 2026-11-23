// node render.js stills t1,t2,...  |  node render.js frames [half]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [, , mode = 'frames', arg] = process.argv; const V = process.env.V === '1', WW = V ? 1080 : 1920, HH = V ? 1920 : 1080; const D = __dirname, TOTAL = 32.0, FPS = 30;
(async () => {
  const b = await chromium.launch();
  const half = mode === 'frames' && arg === 'half';
  const open = async () => { const p = await b.newPage({ viewport: { width: WW, height: HH }, deviceScaleFactor: half ? 0.5 : 1 }); p.on('pageerror', (e) => console.log('pageerror', e.message)); await p.goto('file://' + D + '/' + (process.env.FILM || (V ? 'film-v.html' : 'film.html'))); await p.evaluate(() => window.ready); return p; };
  const shoot = async (p, t, f) => { await p.evaluate(async (t) => { window.render(t); await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))); }, t); await p.screenshot({ path: f, type: 'jpeg', quality: 93 }); };
  if (mode === 'stills') { const p = await open(); fs.mkdirSync(D + '/work/stills', { recursive: true }); for (const t of arg.split(',').map(Number)) await shoot(p, t, `${D}/work/stills/${process.env.TAG || (V ? 'v' : 's')}-${t.toFixed(2)}.jpg`); }
  else { const out = D + '/work/' + (process.env.OUT || (V ? 'frames-v' : 'frames')); fs.rmSync(out, { recursive: true, force: true }); fs.mkdirSync(out, { recursive: true }); const N = Math.round(TOTAL * FPS), nw = 4, per = Math.ceil(N / nw);
    const pages = []; for (let i = 0; i < nw; i++) pages.push(await open());
    await Promise.all(pages.map(async (p, w) => { for (let f = w * per; f < Math.min(N, (w + 1) * per); f++) await shoot(p, f / FPS, `${out}/f${String(f).padStart(5, '0')}.jpg`); }));
    console.log('frames', N); }
  await b.close();
})();
