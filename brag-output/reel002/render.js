// node render.js stills t1,t2 | node render.js frames
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [, , mode = 'frames', arg] = process.argv; const D = __dirname, TOTAL = 30.0, FPS = 30, W = '/home/user/Image-Scanner/brag-output/whistle';
(async () => {
  const html = fs.readFileSync(D + '/reel.html', 'utf8').replace('__RUN__', fs.readFileSync(W + '/shots/run.json', 'utf8')).replace('__LEARN__', fs.readFileSync(W + '/shots/learnrun.json', 'utf8'));
  fs.writeFileSync(D + '/reel.gen.html', html);
  const b = await chromium.launch();
  const open = async () => { const p = await b.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', (e) => console.log('pageerror', e.message)); await p.goto('file://' + D + '/reel.gen.html'); await p.evaluate(() => window.ready); return p; };
  const shoot = async (p, t, f) => { await p.evaluate(async (t) => { window.render(t); await Promise.all([...document.images].filter((i) => i.getAttribute('src')).map((i) => (i.complete && i.naturalWidth ? (i.decode ? i.decode().catch(() => 0) : 0) : new Promise((r) => { i.onload = i.onerror = r; })))); await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))); }, t); await p.screenshot({ path: f, type: 'jpeg', quality: 92 }); };
  if (mode === 'stills') { const p = await open(); fs.mkdirSync(D + '/work/stills', { recursive: true }); for (const t of arg.split(',').map(Number)) await shoot(p, t, `${D}/work/stills/r-${t.toFixed(2)}.jpg`); }
  else { const out = D + '/work/frames'; fs.rmSync(out, { recursive: true, force: true }); fs.mkdirSync(out, { recursive: true }); const N = Math.round(TOTAL * FPS), nw = 4, per = Math.ceil(N / nw);
    const pages = []; for (let i = 0; i < nw; i++) pages.push(await open());
    await Promise.all(pages.map(async (p, w) => { for (let f = w * per; f < Math.min(N, (w + 1) * per); f++) await shoot(p, f / FPS, `${out}/f${String(f).padStart(5, '0')}.jpg`); }));
    console.log('frames', N); }
  await b.close();
})();
