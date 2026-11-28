// node render.js <h|v> stills <t1,t2,...> | frames [workers]
const { chromium } = require('playwright'); const fs = require('fs');
const [, , ori, mode, arg] = process.argv;
const V = ori === 'v', W = V ? 1080 : 1920, H = V ? 1920 : 1080, FPS = 30;
(async () => {
  const rects = fs.readFileSync(__dirname + '/shots/rects.json', 'utf8'), script = fs.readFileSync(__dirname + '/script.json', 'utf8');
  fs.writeFileSync(__dirname + '/explainer.gen.html', fs.readFileSync(__dirname + '/explainer.html', 'utf8').replace('__RECTS__', rects).replace('__SCRIPT__', script));
  const url = 'file://' + __dirname + '/explainer.gen.html' + (V ? '?v=1' : '');
  const b = await chromium.launch();
  const open = async () => { const p = await b.newPage({ viewport: { width: W, height: H } }); p.on('pageerror', (e) => console.log('pageerror', e.message)); await p.goto(url); await p.evaluate(() => window.ready); return p; };
  const shoot = async (p, t, path) => {
    await p.evaluate(async (t) => { window.render(t); await Promise.all([...document.images].map((i) => (i.complete && i.naturalWidth ? (i.decode ? i.decode().catch(() => 0) : 0) : new Promise((r) => { i.onload = i.onerror = r; })))); await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))); }, t);
    await p.screenshot({ path, quality: 92, type: 'jpeg' });
  };
  if (mode === 'stills') {
    const p = await open(); const out = __dirname + `/stills-${ori}`; fs.mkdirSync(out, { recursive: true });
    const total = await p.evaluate(() => window.TOTAL); console.log('total', total.toFixed(2), 's');
    for (const t of arg.split(',').map(Number)) await shoot(p, t, `${out}/s-${t.toFixed(2)}.jpg`);
  } else {
    const nw = +(arg || 4); const out = __dirname + `/frames-${ori}`; fs.mkdirSync(out, { recursive: true });
    const p0 = await open(); const total = await p0.evaluate(() => window.TOTAL); const N = Math.round(total * FPS);
    console.log('frames', N, 'seconds', total.toFixed(2));
    const pages = [p0]; for (let i = 1; i < nw; i++) pages.push(await open());
    const per = Math.ceil(N / nw); let done = 0; const t0 = Date.now();
    await Promise.all(pages.map(async (p, w) => {
      for (let f = w * per; f < Math.min(N, (w + 1) * per); f++) {
        const path = `${out}/f${String(f).padStart(5, '0')}.jpg`;
        if (fs.existsSync(path)) { done++; continue; }
        await shoot(p, f / FPS, path); done++;
        if (done % 600 === 0) console.log(`${done}/${N} frames, ${((Date.now() - t0) / 1000).toFixed(0)} s`);
      }
    }));
  }
  await b.close();
})();
