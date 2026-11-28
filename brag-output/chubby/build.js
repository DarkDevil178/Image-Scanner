// node build.js : the Chubby character sheet (3600x2400 PNG + PDF), the profile avatars and single-pose PNGs.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const { panda, pandaSVG, K, tagShape, goggleRing } = require('./chubby.js');
const O = path.join(__dirname, 'out'); fs.mkdirSync(O + '/poses', { recursive: true });
const FONTS = `<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=DM+Mono:wght@400;500&display=block" rel="stylesheet">`;
const pose = (o, w, h, vb = '-200 -330 400 600') => pandaSVG(o, w, h, vb);
const card = (inner, style = '') => `<div style="background:#fff;border-radius:34px;padding:44px 50px;box-shadow:0 2px 0 rgba(22,25,34,.06),0 20px 40px -24px rgba(22,25,34,.25);${style}">${inner}</div>`;
const k = (t) => `<div style="font:500 26px 'DM Mono';color:${K.tealD};letter-spacing:.02em;margin-bottom:18px">${t}</div>`;
const sw = (c, n, h, note) => `<div style="display:flex;gap:22px;align-items:center;margin-bottom:12px"><div style="width:64px;height:64px;border-radius:16px;background:${c};box-shadow:inset 0 0 0 3px rgba(22,25,34,.12)"></div><div><div style="font:700 28px 'DM Sans'">${n}</div><div style="font:500 22px 'DM Mono';color:#7C8494">${h} · ${note}</div></div></div>`;
const label = (t) => `<div style="font:500 26px 'DM Mono';color:#7C8494;text-align:center;margin-top:6px">${t}</div>`;

const sheet = `<html><head>${FONTS}<style>*{margin:0;padding:0;box-sizing:border-box}body{width:3600px;height:2400px;background:#ECEEF2;font-family:'DM Sans';color:#161922;overflow:hidden;
  background-image:linear-gradient(#DFE2E8 2px,transparent 2px),linear-gradient(90deg,#DFE2E8 2px,transparent 2px);background-size:80px 80px}
  .row{display:flex;gap:40px}</style></head><body>
<div style="position:absolute;left:110px;top:90px;right:110px;display:flex;justify-content:space-between;align-items:flex-end">
  <div><div style="font:500 30px 'DM Mono';color:${K.tealD}">@wierd_stuff_i_make · mascot #000 · character sheet v1</div><div style="font:800 150px/1 'Bricolage Grotesque';letter-spacing:-.04em;margin-top:14px">Chubby<span style="color:${K.teal}">.</span></div></div>
  <div style="font:500 30px 'DM Mono';color:#7C8494;text-align:right">chibi panda inventor<br>flat vector · ink line 7 px @ 400 px tall</div></div>

<!-- turnaround -->
<div style="position:absolute;left:110px;top:330px;width:2060px;height:1020px">${card(`${k('01 · turnaround')}
  <div style="position:relative;height:820px">
    ${[['head top', 136], ['goggles', 307], ['belt', 643], ['feet', 754]].map(([n, y]) => `<div style="position:absolute;left:0;right:0;top:${y}px;border-top:3px dashed #C9CED8"></div><div style="position:absolute;right:0;top:${y - 34}px;font:500 22px 'DM Mono';color:#9AA1B2">${n}</div>`).join('')}
    <div class="row" style="position:absolute;left:30px;top:0;gap:70px">${['front', 'side', 'back'].map((v) => `<div>${pose({ view: v }, 520, 780)}${label(v)}</div>`).join('')}</div></div>`, 'height:1020px')}</div>

<!-- bio -->
<div style="position:absolute;left:2210px;top:330px;width:1280px;height:1020px">${card(`${k('02 · bio')}
  <div style="display:flex;gap:40px;align-items:center"><div style="width:300px;height:300px;border-radius:50%;background:${K.teal};overflow:hidden;flex:none">${pose({ expr: 'focused' }, 300, 450, '-200 -300 400 600')}</div>
  <div><div style="font:800 96px/1 'Bricolage Grotesque';letter-spacing:-.04em">Chubby</div><div style="font:500 30px 'DM Mono';color:${K.tealD};margin-top:12px">product #000 · the one who builds the rest</div></div></div>
  <div style="margin-top:44px;display:grid;grid-template-columns:200px 1fr;row-gap:22px;font-size:32px;line-height:1.35">
   <div style="font:500 26px 'DM Mono';color:#7C8494;padding-top:6px">species</div><div>panda, chibi round. black-and-white, teal gear.</div>
   <div style="font:500 26px 'DM Mono';color:#7C8494;padding-top:6px">role</div><div>chaotic inventor. builds every product on the page, one number at a time, all the way to #999.</div>
   <div style="font:500 26px 'DM Mono';color:#7C8494;padding-top:6px">quirk</div><div>breaks things to see how they work, then puts them back better.</div>
   <div style="font:500 26px 'DM Mono';color:#7C8494;padding-top:6px">carries</div><div>round brass goggles, a tool belt: scissors and tape, pencil and ruler, a pouch of AI-token coins.</div>
   <div style="font:500 26px 'DM Mono';color:#7C8494;padding-top:6px">pose</div><div>mid-build, focused, tongue out.</div>
   <div style="font:500 26px 'DM Mono';color:#7C8494;padding-top:6px">story</div><div>"every useful thing starts as a broken one."</div></div>`, 'height:1020px')}</div>

<!-- expressions -->
<div style="position:absolute;left:110px;top:1390px;width:1500px;height:900px">${card(`${k('03 · expressions')}
  <div class="row" style="gap:20px">${[['focused', 'focused · tongue out'], ['proud', 'proud · ta-da'], ['oops', 'oops · it broke']].map(([e, l]) => `<div>${pose({ expr: e, tag: e === 'proud' ? { n: '#002', c: '#FF8A3D' } : null }, 440, 660)}${label(l)}</div>`).join('')}</div>`, 'height:900px')}</div>

<!-- props -->
<div style="position:absolute;left:1650px;top:1390px;width:1000px;height:900px">${card(`${k('04 · props, close up')}
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px 30px">
   <div><svg width="420" height="200" viewBox="-170 -80 340 160">${goggleRing(-62, 0)}${goggleRing(62, 0)}<rect x="-18" y="-8" width="36" height="14" rx="5" fill="${K.brass}" stroke="${K.ink}" stroke-width="5"/><rect x="-168" y="-11" width="52" height="22" fill="${K.teal}" stroke="${K.ink}" stroke-width="5"/><rect x="116" y="-11" width="52" height="22" fill="${K.teal}" stroke="${K.ink}" stroke-width="5"/></svg>${label('round brass goggles, teal strap')}</div>
   <div><svg width="420" height="200" viewBox="-150 -120 300 160">${[[-34, -40], [0, -56], [34, -36], [-60, 10], [60, 6]].map(([x, y]) => `<g transform="translate(${x},${y})"><circle r="26" fill="${K.tealL}" stroke="${K.ink}" stroke-width="6"/><text y="9" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="24" fill="${K.tealD}">AI</text></g>`).join('')}</svg>${label('AI-token coins, in the belt pouch')}</div>
   <div><svg width="420" height="220" viewBox="-200 0 400 220"><rect x="-190" y="70" width="380" height="40" fill="${K.teal}" stroke="${K.ink}" stroke-width="7"/><rect x="-24" y="64" width="48" height="52" rx="8" fill="${K.brass}" stroke="${K.ink}" stroke-width="7"/>
     <g transform="translate(-120,80)"><rect x="2" y="-58" width="13" height="66" rx="2" fill="${K.pencil}" stroke="${K.ink}" stroke-width="5"/><path d="M2 -58 L8.5 -76 L15 -58 Z" fill="#E9C9A0" stroke="${K.ink}" stroke-width="5"/><rect x="18" y="-48" width="16" height="58" rx="2" fill="#F3EBD8" stroke="${K.ink}" stroke-width="5"/><rect x="-6" y="0" width="48" height="56" rx="10" fill="${K.tealD}" stroke="${K.ink}" stroke-width="7"/></g>
     <g transform="translate(-50,124) rotate(8)"><path d="M0 0 L-8 46 M0 0 L8 46" stroke="#9AA1B2" stroke-width="9" stroke-linecap="round"/><circle cx="-11" cy="-12" r="11" fill="none" stroke="${K.teal}" stroke-width="7"/><circle cx="11" cy="-12" r="11" fill="none" stroke="${K.teal}" stroke-width="7"/></g>
     <g transform="translate(150,92)"><circle r="28" fill="${K.paper}" stroke="${K.ink}" stroke-width="7"/><circle r="11" fill="${K.fur}" stroke="${K.ink}" stroke-width="5"/></g></svg>${label('tool belt: pencil, ruler, scissors, tape')}</div>
   <div style="display:flex;flex-direction:column;align-items:center;justify-content:center"><svg width="420" height="200" viewBox="-200 -100 400 200"><g transform="translate(0,-40)">${tagShape('#001', '#3D4FE0', 1.05)}</g><g transform="translate(0,46) rotate(-4)">${tagShape('#002', '#FF8A3D', 1.05)}</g></svg>${label('the number tag, in the product colour')}</div>
  </div>`, 'height:900px')}</div>

<!-- palette + rules -->
<div style="position:absolute;left:2690px;top:1390px;width:800px;height:900px">${card(`${k('05 · palette')}
  ${sw(K.ink, 'ink', '#161922', 'fur, line')}${sw(K.fur, 'fur', '#F7F6F2', 'face, body')}${sw(K.teal, 'chubby teal', '#18A999', 'gear')}${sw(K.tealL, 'teal light', '#7FE0D3', 'lenses, coins')}${sw(K.tealD, 'teal deep', '#0E6B61', 'pouches, text')}${sw(K.brass, 'brass', '#C9A24A', 'goggles, buckle')}
  <div style="margin-top:18px">${k('06 · do / don’t')}
  <div style="font-size:23px;line-height:1.38"><b style="color:#14906d">✓</b> keep the teal gear and the brass goggles on, always<br><b style="color:#14906d">✓</b> in launch posts, Chubby holds the tag; the tag takes the product colour<br><b style="color:#14906d">✓</b> keep the 7 px ink line at 400 px (scale with the size)<br>
  <b style="color:#d2413a">✕</b> no recolouring the fur or the teal to a product colour<br><b style="color:#d2413a">✕</b> no stretching, no outlines removed, no extra limbs<br><b style="color:#d2413a">✕</b> never speaks as a real person; never a founder stand-in</div></div>`, 'height:900px')}</div>
</body></html>`;

const avatar = (bg) => `<html><head>${FONTS}</head><body style="margin:0;width:1080px;height:1080px;background:${bg};display:grid;place-items:center;overflow:hidden">
  <div style="width:1080px;height:1080px;position:relative">${pose({ expr: 'focused' }, 1080, 1080, '-245 -275 490 490').replace('<svg', '<svg style="position:absolute;left:0;top:0"')}</div></body></html>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3600, height: 2400 } });
  const go = async (html, out, w, h, transparent = false) => { await p.setViewportSize({ width: w, height: h }); await p.setContent(html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    await p.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h }, omitBackground: transparent }); };
  await go(sheet, O + '/chubby-character-sheet.png', 3600, 2400);
  await p.setViewportSize({ width: 3600, height: 2400 }); await p.setContent(sheet); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  await p.pdf({ path: O + '/chubby-character-sheet.pdf', width: '3600px', height: '2400px', printBackground: true });
  await go(avatar(K.teal), O + '/avatar-teal.png', 1080, 1080);
  await go(avatar('#ECEEF2'), O + '/avatar-paper.png', 1080, 1080);
  await go(avatar('#161922'), O + '/avatar-ink.png', 1080, 1080);
  const P = { front: { view: 'front' }, side: { view: 'side' }, back: { view: 'back' }, focused: { expr: 'focused' }, oops: { expr: 'oops' },
    'proud-002': { expr: 'proud', tag: { n: '#002', c: '#FF8A3D' } }, 'proud-001': { expr: 'proud', tag: { n: '#001', c: '#3D4FE0' } }, 'proud-003-blank': { expr: 'proud', tag: { n: '#003', c: '#ECEEF2' } } };
  for (const [n, o] of Object.entries(P)) await go(`<html><head>${FONTS}</head><body style="margin:0;background:transparent">${pose(o, 1200, 1800)}</body></html>`, `${O}/poses/chubby-${n}.png`, 1200, 1800, true);
  fs.writeFileSync(O + '/chubby.svg', pose({ view: 'front' }, 400, 600));
  fs.writeFileSync(O + '/chubby-focused.svg', pose({ expr: 'focused' }, 400, 600));
  console.log('built'); await b.close();
})();
