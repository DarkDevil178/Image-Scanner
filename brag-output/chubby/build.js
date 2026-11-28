// node build.js : the Chubby character sheet (3600x2400 PNG + PDF), avatars and every pose as a transparent PNG and SVG.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const { pandaSVG, P, LIB } = require('./chubby.js');
const O = path.join(__dirname, 'out'); fs.mkdirSync(O + '/poses', { recursive: true }); fs.mkdirSync(O + '/svg', { recursive: true });
const FONTS = `<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@600;700;800&family=Caveat:wght@700&display=block" rel="stylesheet">`;
const BR = '#6B3F1F', BRL = '#8A5A35', CREAM = '#FBF1E4', CARD = 'rgba(255,248,238,.88)', LINE = '#EBD5B8';
const pill = (t, size = 54) => `<div style="display:inline-block;background:${BR};color:#FFF7EC;font:600 ${size}px/1 Fredoka;padding:18px 44px 22px;border-radius:999px;box-shadow:0 6px 0 rgba(80,40,10,.18)">${t}</div>`;
const tag = (t) => `<div style="display:inline-block;background:#F3E2C8;color:${BR};font:600 34px/1 Fredoka;padding:12px 30px 14px;border-radius:999px;margin-top:6px">${t}</div>`;
const panel = (x, y, w, h, title, inner) => `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;background:${CARD};border:3px solid ${LINE};border-radius:48px;box-shadow:0 20px 50px -30px rgba(110,60,20,.35)">
  <div style="position:absolute;left:0;right:0;top:-42px;text-align:center">${pill(title)}</div>${inner}</div>`;
const fig = (name, w, h, vb, label) => `<div style="display:flex;flex-direction:column;align-items:center">${pandaSVG(LIB[name], w, h, vb)}${label ? tag(label) : ''}</div>`;
const pawIcon = (s, c = BR) => `<svg width="${s}" height="${s}" viewBox="0 0 100 100"><ellipse cx="50" cy="64" rx="24" ry="20" fill="${c}"/>${[[22, 38], [40, 24], [60, 24], [78, 38]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="10" ry="12" fill="${c}"/>`).join('')}</svg>`;
const heartIcon = (s, c = BR) => `<svg width="${s}" height="${s}" viewBox="0 0 60 60"><path d="M30 50 C4 32 6 10 22 10 C28 10 30 16 30 16 C30 16 32 10 38 10 C54 10 56 32 30 50 Z" fill="none" stroke="${c}" stroke-width="5"/></svg>`;
// bamboo leaves for the corners
const leaf = (x, y, r, s, c) => `<path transform="translate(${x},${y}) rotate(${r}) scale(${s})" d="M0 0 C40 -18 120 -14 170 0 C120 14 40 18 0 0 Z" fill="${c}"/>`;
const bamboo = (side) => { const X = side === 'L' ? 0 : 3600, d = side === 'L' ? 1 : -1; let s = '';
  for (let i = 0; i < 3; i++) s += `<rect x="${X + d * (30 + i * 70) - (d < 0 ? 26 : 0)}" y="${-40 + i * 60}" width="26" height="${1300 - i * 240}" rx="13" fill="rgba(160,190,90,${.28 - i * .07})"/>`;
  [[90, 120, -20], [60, 300, 30], [150, 520, -35], [40, 760, 20], [120, 980, -10]].forEach(([x, y, r], i) => { s += leaf(X + d * x, y, d > 0 ? r : 180 - r, 1.3 - i * .1, `rgba(120,170,60,${.55 - i * .06})`); });
  return s; };

const DETAILS = [['Name', 'Chubby'], ['Species', 'Panda'], ['Height', '~ 1.2 m (cute scale)'], ['Weight', '~ 30 kg (cuddly!)'], ['Personality', 'Calm, Cheerful,<br>Kind, Curious'], ['Likes', 'Peace, Good Food,<br>Nature, Happiness']];
const SW = [[P.black, 'Panda Black'], [P.white, 'Panda White'], [P.brown, 'Warm Brown'], [P.pink, 'Soft Pink'], [P.green, 'Leaf Green']];
const VIBES = ['Cute &amp; Friendly', 'Calm &amp; Positive', 'Brings Joy', 'Perfect for Reels,<br>Stories &amp; More!'];
const HEAD = '-235 -300 470 420';   // head-and-shoulders crop for the expressions

const sheet = `<html><head>${FONTS}<style>*{margin:0;padding:0;box-sizing:border-box}body{width:3600px;height:2400px;overflow:hidden;font-family:Nunito;color:${BR};
  background:radial-gradient(ellipse 1400px 900px at 18% 30%,#FFF3D9 0%,rgba(255,243,217,0) 70%),radial-gradient(ellipse 1600px 1000px at 80% 90%,#F9E6CC 0%,rgba(249,230,204,0) 70%),${CREAM}}</style></head><body>
<svg width="3600" height="2400" style="position:absolute;left:0;top:0">${bamboo('L')}${bamboo('R')}
  <path d="M0 2330 C600 2260 1200 2300 1800 2320 C2400 2340 3000 2280 3600 2320 L3600 2400 L0 2400 Z" fill="rgba(150,190,90,.35)"/></svg>
<!-- title and the hero -->
<div style="position:absolute;left:230px;top:50px;display:flex;align-items:flex-start;gap:20px"><div style="font:700 250px/1 Fredoka;letter-spacing:-.01em;color:${BR};text-shadow:0 8px 0 rgba(255,255,255,.7)">Chubby</div><div style="margin-top:30px">${pawIcon(120)}</div></div>
<div style="position:absolute;left:230px;top:320px;font:700 84px/1 Caveat;color:${BR};transform:rotate(-4deg)">Small Panda... Big Happiness!</div>
<div style="position:absolute;left:1110px;top:250px">${heartIcon(70)}</div>
<div style="position:absolute;left:160px;top:420px;width:1040px;height:1200px">
  <svg width="1040" height="160" style="position:absolute;left:0;top:1060px;z-index:0"><ellipse cx="520" cy="60" rx="480" ry="52" fill="rgba(139,195,74,.38)"/></svg>
  <div style="position:absolute;left:0;top:0;z-index:1">${pandaSVG(LIB.front, 1040, 1200, '-260 -300 520 600')}</div></div>
<div style="position:absolute;left:990px;top:620px">${pawIcon(0)}<svg width="140" height="120"><path d="M30 20 l18 40 M70 10 l0 44 M108 24 l-18 38" stroke="${P.gold}" stroke-width="12" stroke-linecap="round"/></svg></div>
<!-- key details -->
<div style="position:absolute;left:90px;top:1640px;width:1080px;height:660px;background:${CARD};border:3px solid ${LINE};border-radius:48px">
  <div style="position:absolute;left:50px;top:-42px">${pill('Key Details')}</div>
  <div style="position:absolute;left:60px;top:80px;display:grid;grid-template-columns:44px 270px 30px 1fr;row-gap:14px;align-items:start;font:700 38px/1.2 Nunito">
   ${DETAILS.map(([k, v]) => `<div style="padding-top:4px">${pawIcon(34)}</div><div>${k}</div><div>:</div><div style="font-weight:600;color:#3A2716">${v}</div>`).join('')}
   <div style="padding-top:4px">${pawIcon(34)}</div><div>Catchphrase</div><div>:</div><div style="font:700 62px/1 Caveat;color:${BR};transform:rotate(-3deg);margin-top:-6px">“Small Panda...<br>&nbsp;Big Happiness!”</div></div></div>
<!-- turnaround -->
${panel(1230, 140, 1360, 900, 'Character Turnaround', `<div style="position:absolute;left:10px;right:10px;top:200px;display:flex;justify-content:space-around">
  ${[['front', 'Front'], ['side', 'Side'], ['back', 'Back'], ['q34', '3/4']].map(([n, l]) => fig(n, 330, 440, '-210 -280 420 560', l)).join('')}</div>`)}
<!-- expressions -->
${panel(2640, 110, 880, 900, 'Expressions', `<div style="position:absolute;left:20px;right:20px;top:120px;display:grid;grid-template-columns:repeat(3,1fr);row-gap:70px;justify-items:center">
  ${[['happy', 'Happy'], ['excited', 'Excited'], ['wink', 'Wink'], ['thinking', 'Thinking'], ['surprised', 'Surprised'], ['sad', 'Sad']].map(([n, l]) => fig(n, 270, 241, HEAD, l)).join('')}</div>`)}
<!-- poses library -->
${panel(1230, 1140, 1360, 1150, 'Poses Library', `<div style="position:absolute;left:10px;right:10px;top:60px;display:grid;grid-template-columns:repeat(4,1fr);row-gap:10px;justify-items:center">
  ${[['meditating', 'Meditating'], ['jump', 'Happy Jump'], ['thinking', 'Thinking'], ['shy', 'Shy'], ['relaxing', 'Relaxing'], ['eating', 'Eating'], ['waving', 'Waving'], ['sleeping', 'Sleeping']].map(([n, l]) => fig(n, 320, 400, '-280 -320 560 640', l)).join('')}</div>`)}
<!-- palette -->
${panel(2640, 1140, 420, 1150, 'Color Palette', `<div style="position:absolute;left:46px;top:130px">${SW.map(([c, n]) => `<div style="display:flex;gap:26px;align-items:center;margin-bottom:56px"><div style="width:110px;height:110px;border-radius:50%;background:${c};box-shadow:inset 0 0 0 3px rgba(0,0,0,.08)"></div><div style="font:700 32px/1.25 Nunito">${n}<br><span style="font-weight:600;color:${BRL}">${c}</span></div></div>`).join('')}</div>`)}
<!-- vibes -->
${panel(3100, 1140, 420, 1150, 'Vibes', `<div style="position:absolute;left:40px;right:30px;top:150px">${VIBES.map((v) => `<div style="display:flex;gap:20px;align-items:flex-start;margin-bottom:56px"><div style="width:52px;height:52px;flex:none;border-radius:50%;background:${P.green};display:grid;place-items:center;color:#fff;font:800 32px Nunito">✓</div><div style="font:700 36px/1.25 Nunito">${v}</div></div>`).join('')}
  <div style="font:700 66px/1.05 Caveat;transform:rotate(-6deg);margin-top:70px">Let's spread<br>happiness together!</div><div style="position:absolute;right:10px;top:880px">${pawIcon(90)}</div></div>`)}
<div style="position:absolute;right:120px;bottom:22px;font:700 30px Nunito;color:${BRL}">@wierd_stuff_i_make</div>
</body></html>`;

const avatar = (bg, o = { arms: 'pray', face: 'happy' }) => `<html><head>${FONTS}</head><body style="margin:0;width:1080px;height:1080px;overflow:hidden;background:${bg}">
  ${pandaSVG(o, 1080, 1080, '-250 -290 500 500')}</body></html>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3600, height: 2400 } });
  const go = async (html, out, w, h, transparent = false) => { await p.setViewportSize({ width: w, height: h }); await p.setContent(html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
    await p.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h }, omitBackground: transparent }); };
  await go(sheet, O + '/chubby-character-sheet.png', 3600, 2400);
  await p.pdf({ path: O + '/chubby-character-sheet.pdf', width: '3600px', height: '2400px', printBackground: true });
  await go(avatar('radial-gradient(circle at 50% 40%,#FFF6E6,#F6E2C4)'), O + '/avatar-cream.png', 1080, 1080);
  await go(avatar('radial-gradient(circle at 50% 40%,#CFE7A6,#8BC34A)'), O + '/avatar-green.png', 1080, 1080);
  await go(avatar('radial-gradient(circle at 50% 40%,#FFE3E3,#F7C8C8)', LIB.meditating), O + '/avatar-pink-calm.png', 1080, 1080);
  for (const n of Object.keys(LIB)) { const lie = LIB[n].legs === 'lie';
    const vb = lie ? '-290 -40 580 340' : '-280 -320 560 640', [w, h] = lie ? [1450, 850] : [1120, 1280];
    await go(`<html><head>${FONTS}</head><body style="margin:0;background:transparent">${pandaSVG(LIB[n], w, h, vb)}</body></html>`, `${O}/poses/chubby-${n}.png`, w, h, true);
    fs.writeFileSync(`${O}/svg/chubby-${n}.svg`, pandaSVG(LIB[n], w / 2, h / 2, vb)); }
  console.log('built', Object.keys(LIB).length, 'poses'); await b.close();
})();
