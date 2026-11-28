const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const O = path.join(__dirname, '..', 'out', 'brand', 'logo'); fs.mkdirSync(O, { recursive: true });
const FONTS = `<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=DM+Mono:wght@500&display=block" rel="stylesheet"><style>*{margin:0}html,body{background:transparent}#c{display:inline-flex;align-items:center;gap:60px;padding:40px}</style>`;
const mark = (s, cur = '#3D4FE0', bg = '#161922', fg = '#ECEEF2') => `<div style="width:${s}px;height:${s}px;border-radius:22%;background:${bg};display:grid;place-items:center"><div style="position:relative;font:800 ${s * 0.62}px/1 'Bricolage Grotesque';letter-spacing:-.04em;color:${fg};transform:translate(-${s * 0.06}px,-${s * 0.06}px)">w<span style="position:absolute;left:100%;bottom:${s * 0.04}px;margin-left:${s * 0.05}px;width:${s * 0.2}px;height:${s * 0.07}px;border-radius:${s * 0.02}px;background:${cur}"></span></div></div>`;
const word = (s, c = '#161922', cur = '#3D4FE0') => `<span style="font:500 ${s}px/1 'DM Mono';letter-spacing:-.02em;color:${c};white-space:nowrap">wierd_stuff_i_make<span style="display:inline-block;width:${s * 0.5}px;height:${s * 0.12}px;background:${cur};margin-left:${s * 0.08}px;border-radius:3px"></span></span>`;
const hanger = (s, c = '#3D4FE0') => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7.5V6a2 2 0 1 0-2-2"/><path d="M12 7.5 3.5 14a1.5 1.5 0 0 0 .9 2.7h15.2a1.5 1.5 0 0 0 .9-2.7z"/></svg>`;
const wardrobe = (c, hc) => `${hanger(300, hc)}<span style="font:800 260px/1 'Bricolage Grotesque';letter-spacing:-.04em;color:${c}">Wardrobe</span>`;
const L = {
  'page-mark.png': mark(1000), 'page-mark-mono.png': mark(1000, '#ECEEF2'), 'page-mark-reversed.png': mark(1000, '#161922', '#ECEEF2', '#161922'),
  'wordmark-ink.png': word(160), 'wordmark-paper.png': word(160, '#ECEEF2', '#A5BBFF'),
  'lockup-ink.png': mark(260) + word(120), 'lockup-paper.png': mark(260, '#A5BBFF', '#ECEEF2', '#161922') + word(120, '#ECEEF2', '#A5BBFF'),
  'wardrobe-mark.png': hanger(1000), 'wardrobe-mark-white.png': hanger(1000, '#FFFFFF'),
  'wardrobe-lockup-ink.png': wardrobe('#161922', '#3D4FE0'), 'wardrobe-lockup-white.png': wardrobe('#FFFFFF', '#FFFFFF'),
};
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3200, height: 1200 } });
  for (const [f, h] of Object.entries(L)) { await p.setContent(`<html><head>${FONTS}</head><body><div id="c">${h}</div></body></html>`); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    await (await p.$('#c')).screenshot({ path: path.join(O, f), omitBackground: true }); }
  console.log('logos', Object.keys(L).length); await b.close(); })();
