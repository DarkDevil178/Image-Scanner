const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const O = path.join(__dirname, '..', 'out', 'brand', 'logo'); fs.mkdirSync(O, { recursive: true });
const FONTS = `<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=DM+Mono:wght@500&display=block" rel="stylesheet"><style>*{margin:0}html,body{background:transparent}#c{display:inline-flex;align-items:center;gap:60px;padding:40px}</style>`;
const mark = (s, cur = '#FF8A3D', bg = '#161922', fg = '#ECEEF2') => `<div style="width:${s}px;height:${s}px;border-radius:22%;background:${bg};display:grid;place-items:center"><div style="position:relative;font:800 ${s * 0.62}px/1 'Bricolage Grotesque';letter-spacing:-.04em;color:${fg};transform:translate(-${s * 0.06}px,-${s * 0.06}px)">w<span style="position:absolute;left:100%;bottom:${s * 0.04}px;margin-left:${s * 0.05}px;width:${s * 0.2}px;height:${s * 0.07}px;border-radius:${s * 0.02}px;background:${cur}"></span></div></div>`;
const word = (s, c = '#161922', cur = '#FF8A3D') => `<span style="font:500 ${s}px/1 'DM Mono';letter-spacing:-.02em;color:${c};white-space:nowrap">wierd_stuff_i_make<span style="display:inline-block;width:${s * 0.5}px;height:${s * 0.12}px;background:${cur};margin-left:${s * 0.08}px;border-radius:3px"></span></span>`;
const cooker = (s, mono) => { const f = (c) => mono || c; return `<svg width="${s}" height="${s}" viewBox="0 0 512 512"><g fill="none" stroke="${f('#A89A8C')}" stroke-width="16" stroke-linecap="round"><path d="M206 78c-14 14-14 34 0 48"/><path d="M256 78c-14 14-14 34 0 48"/><path d="M306 78c-14 14-14 34 0 48"/></g><rect x="236" y="140" width="40" height="52" rx="12" fill="${f('#F5EDE4')}"/><rect x="62" y="280" width="54" height="30" rx="15" fill="${f('#F5EDE4')}"/><rect x="396" y="280" width="54" height="30" rx="15" fill="${f('#F5EDE4')}"/><rect x="110" y="230" width="292" height="170" rx="46" fill="${f('#FF8A3D')}"/><rect x="96" y="190" width="320" height="52" rx="26" fill="${f('#FFB07A')}"/></svg>`; };
const name = (c) => `<span style="font:800 200px/0.95 'Bricolage Grotesque';letter-spacing:-.04em;color:${c}">Cooker Whistle<br>Counter</span>`;
const L = {
  'page-mark-002.png': mark(1000), 'page-mark-mono.png': mark(1000, '#ECEEF2'), 'page-mark-reversed.png': mark(1000, '#161922', '#ECEEF2', '#161922'),
  'wordmark-ink.png': word(160), 'wordmark-paper.png': word(160, '#ECEEF2', '#FFB07A'),
  'lockup-ink.png': mark(260) + word(120), 'lockup-paper.png': mark(260, '#FFB07A', '#ECEEF2', '#161922') + word(120, '#ECEEF2', '#FFB07A'),
  'cooker-mark.png': cooker(1000), 'cooker-mark-ink.png': cooker(1000, '#1c1816'),
  'cooker-lockup-ink.png': cooker(320, '#1c1816') + name('#161922'), 'cooker-lockup-cream.png': cooker(320) + name('#F5EDE4'),
};
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3200, height: 1200 } });
  for (const [f, h] of Object.entries(L)) { await p.setContent(`<html><head>${FONTS}</head><body><div id="c">${h}</div></body></html>`); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    await (await p.$('#c')).screenshot({ path: path.join(O, f), omitBackground: true }); }
  console.log('logos', Object.keys(L).length); await b.close(); })();
