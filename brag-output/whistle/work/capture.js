// Drive the real Cooker Whistle Counter with a fake microphone (the kitchen hum + three whistles) and capture it.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const SH = path.join(__dirname, '..', 'shots'); fs.mkdirSync(SH + '/run', { recursive: true }); fs.mkdirSync(SH + '/learnrun', { recursive: true });
const URL = 'http://localhost:8123/index.html';
const launch = () => chromium.launch({ args: ['--use-fake-ui-for-media-stream', '--use-fake-device-for-media-stream', '--use-file-for-fake-audio-capture=' + path.join(__dirname, 'mic-feed.wav')] });
const ctxOf = async (b) => { const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, permissions: ['microphone'] }); const p = await c.newPage(); p.on('pageerror', (e) => console.log('err', e.message)); await p.goto(URL); await p.waitForTimeout(900); return p; };
const R = {};
const rect = (p, s) => p.evaluate((s) => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); return { x: b.x, y: b.y, w: b.width, h: b.height }; }, s);
(async () => {
  // ---- 1. the counting run: screenshots as fast as they come, with their times ----
  { const b = await launch(); const p = await ctxOf(b);
    await p.screenshot({ path: SH + '/idle.png' });
    for (const k of ['cnt', 'tgt', 'wGo', 'mbar', 'learn', 'p1', 'm1', 'tgP', 'tgM', 'bkP', 'gear', 'tabT', 'sens', 'pwName', 'pwSave', 'testMic']) R[k] = await rect(p, '#' + k);
    await p.click('#wGo'); const t0 = Date.now(); const frames = [];
    while (Date.now() - t0 < 24500) { const t = (Date.now() - t0) / 1000; const f = `run/r${String(frames.length).padStart(4, '0')}.png`; await p.screenshot({ path: SH + '/' + f }); frames.push({ t, f, n: await p.textContent('#cnt') }); }
    fs.writeFileSync(SH + '/run.json', JSON.stringify(frames)); console.log('run frames', frames.length, 'counts', [...new Set(frames.map((x) => x.n))].join(','));
    R.ov = await rect(p, '#ov'); R.ovStop = await rect(p, '#ovStop');
    await b.close(); }
  // ---- 2. learn my whistle (quiet first 2 s, whistle at 4 s) ----
  { const b = await launch(); const p = await ctxOf(b);
    await p.click('#learn'); const t0 = Date.now(); const frames = [];
    while (Date.now() - t0 < 8500) { const t = (Date.now() - t0) / 1000; const f = `learnrun/l${String(frames.length).padStart(4, '0')}.png`; await p.screenshot({ path: SH + '/' + f }); frames.push({ t, f, st: await p.textContent('#learnSt') }); }
    console.log('learn states', [...new Set(frames.map((x) => x.st))].join(' | '));
    R.learnSt = await rect(p, '#learnSt'); R.learnBtn = await rect(p, '#learn');
    const done = await p.$('#learn'); await done.click(); await p.waitForTimeout(800); await p.screenshot({ path: SH + '/learn-ok.png' });
    console.log('after done:', await p.textContent('#learnSt'));
    fs.writeFileSync(SH + '/learnrun.json', JSON.stringify(frames));
    // presets: name it and save
    await p.fill('#pwName', 'Toor dal'); await p.screenshot({ path: SH + '/preset-typed.png' }); await p.click('#pwSave'); await p.waitForTimeout(500);
    await p.fill('#pwName', 'Rice'); await p.click('#tgM'); await p.waitForTimeout(150); await p.click('#pwSave'); await p.waitForTimeout(400);
    await p.$eval('#pwList', (e) => e.scrollIntoView({ block: 'center' })); await p.waitForTimeout(300); await p.screenshot({ path: SH + '/presets.png' }); await p.evaluate(() => window.scrollTo(0, 0)); R.pwList = await rect(p, '#pwList');
    // the timer tab
    await p.click('#tabT'); await p.waitForTimeout(400); await p.screenshot({ path: SH + '/timer.png' }); R.quick = await rect(p, '#quick'); R.tGo = await rect(p, '#tGo');
    await p.click('#tGo'); await p.waitForTimeout(2300); await p.screenshot({ path: SH + '/timer-running.png' }); await p.click('#tGo').catch(() => {}); await p.waitForTimeout(300);
    await p.click('#tabW'); await p.waitForTimeout(300);
    // settings
    await p.click('#gear'); await p.waitForTimeout(500); await p.screenshot({ path: SH + '/settings.png' }); R.langs = await rect(p, '#langs');
    const langs = await p.$$eval('#langs button', (bs) => bs.map((b) => b.textContent.trim()));
    // every language: the home screen and the alarm
    for (let i = 0; i < langs.length; i++) {
      await p.click(`#langs button:nth-child(${i + 1})`); await p.waitForTimeout(300); await p.screenshot({ path: SH + `/lang${i}-settings.png` });
      await p.click('#closeSheet'); await p.waitForTimeout(350); await p.screenshot({ path: SH + `/lang${i}-home.png` });
      await p.evaluate(() => { const ov = document.querySelector('#ov'); if (ov) ov.hidden = false; });
      // reach the target the honest way: running, then +1 until it fires
      await p.click('#wGo'); await p.waitForTimeout(300); for (let k = 0; k < 4; k++) { if (await p.isVisible('#ovStop')) break; await p.click('#p1'); await p.waitForTimeout(250); }
      await p.waitForTimeout(400); await p.screenshot({ path: SH + `/lang${i}-alarm.png` }); console.log('alarm', langs[i], (await p.textContent('#ovmsg')).trim());
      if (await p.isVisible('#ovStop')) await p.click('#ovStop'); await p.waitForTimeout(300);
      if ((await p.textContent('#wGo')).match(/stop|रोकें|நிறுத்து|ఆపు|നിർത്ത|ನಿಲ್ಲಿಸ/i)) await p.click('#wGo');
      await p.click('#m1').catch(() => {}); await p.click('#m1').catch(() => {}); await p.click('#m1').catch(() => {}); await p.click('#m1').catch(() => {});
      await p.click('#gear'); await p.waitForTimeout(400);
    }
    R.langNames = langs;
    await p.click('#langs button:nth-child(1)'); await p.click('#closeSheet');
    await b.close(); }
  fs.writeFileSync(SH + '/rects.json', JSON.stringify(R, null, 1));
})();
