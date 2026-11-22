// node render_reel.js <name> [stills t1,t2|frames]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [, , name, mode = 'frames', arg] = process.argv; const D = __dirname;
(async () => {
  const spec = fs.readFileSync(`${D}/work/spec-${name}.json`, 'utf8');
  const html = fs.readFileSync(`${D}/reel.html`, 'utf8').replace('__SPEC__', spec).replace('__RUN__', fs.readFileSync(`${D}/shots/run.json`, 'utf8')).replace('__LEARN__', fs.readFileSync(`${D}/shots/learnrun.json`, 'utf8'));
  const gen = `${D}/reel-${name}.gen.html`; fs.writeFileSync(gen, html);
  const b = await chromium.launch(); const S = JSON.parse(spec);
  const open = async () => { const p = await b.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', (e) => console.log('pageerror', e.message)); await p.goto('file://' + gen); await p.evaluate(() => window.ready); return p; };
  const shoot = async (p, t, f) => { await p.evaluate(async (t) => { window.render(t); await Promise.all([...document.images].filter((i) => i.getAttribute('src')).map((i) => (i.complete && i.naturalWidth ? (i.decode ? i.decode().catch(() => 0) : 0) : new Promise((r) => { i.onload = i.onerror = r; })))); await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))); }, t); await p.screenshot({ path: f, type: 'jpeg', quality: 92 }); };
  if (mode === 'stills') { const p = await open(); fs.mkdirSync(`${D}/work/stills`, { recursive: true }); for (const t of arg.split(',').map(Number)) await shoot(p, t, `${D}/work/stills/${name}-${t.toFixed(2)}.jpg`); }
  else { const out = `${D}/work/frames-${name}`; fs.rmSync(out, { recursive: true, force: true }); fs.mkdirSync(out, { recursive: true }); const N = Math.round(S.total * 30), nw = 4, per = Math.ceil(N / nw);
    const pages = []; for (let i = 0; i < nw; i++) pages.push(await open());
    await Promise.all(pages.map(async (p, w) => { for (let f = w * per; f < Math.min(N, (w + 1) * per); f++) await shoot(p, f / 30, `${out}/f${String(f).padStart(5, '0')}.jpg`); }));
    console.log(name, 'frames', N); }
  await b.close();
})();
