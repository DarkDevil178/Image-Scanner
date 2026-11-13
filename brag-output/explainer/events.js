const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + __dirname + '/explainer.gen.html');
  const out = await p.evaluate(() => {
    const ev = []; const add = (t, kind, w = 0.5) => ev.push({ t: +t.toFixed(3), kind, w });
    for (const b of window.TIMELINE) {
      const s = (window.__B || {})[b.id];
      if (b.card) { add(b.start + 0.12, 'swell', 0.55); add(b.start + 0.7, 'hit', 0.5); }
      if (b.id === 'end') { add(b.start + 0.05, 'whoosh', 0.6); add(b.start + 0.45, 'hit', 0.85); }
      if (b.id === 'c0') { add(b.start + 0.05, 'whoosh', 0.5); for (let j = 0; j < 14; j++) add(b.start + 0.7 + j * 0.12, 'drop', 0.3); add(b.start + b.dur - 2.4, 'whoosh', 0.5); }
      if (!s) continue;
      for (const st of s.states || []) if (st.tr) add(b.start + st.t, { push: 'whoosh', sheet: 'sheet', sheetdown: 'sheet', scroll: 'whoosh', fade: 'soft', wipe: 'scan' }[st.tr] || 'soft', st.tr === 'fade' ? 0.25 : 0.45);
      for (const tp of s.taps || []) add(b.start + tp.t, tp.kind === 'swipe' || tp.to ? 'swipe' : 'click', 0.5);
      if (s.style) { const [a, z] = s.style; [z - 0.9, z - 0.45, z].forEach((t) => add(b.start + t, 'land', 0.5)); add(b.start + z + 0.2, 'bell', 0.45); }
      if (s.shuffle) { add(b.start + s.shuffle[1], 'land', 0.45); }
      if (b.id === 'c1b') add(b.start + 1.05, 'snap', 0.7);
      if (b.id === 'c1e') add(b.start + 7.4, 'bell', 0.5);
    }
    return { T: window.TIMELINE, total: window.TOTAL, ev };
  });
  fs.writeFileSync(__dirname + '/timeline.json', JSON.stringify(out, null, 1)); console.log(out.T.length, 'beats', out.ev.length, 'events', out.total.toFixed(2), 's');
  await b.close();
})();
