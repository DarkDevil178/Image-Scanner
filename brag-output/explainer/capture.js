// Drive the real Wardrobe app through every chapter and save each state (2x DPR) plus element rects.
const { chromium } = require('playwright'); const fs = require('fs');
const APP = '/home/user/Image-Scanner/brag-output/work/wardrobe.html';
const OUT = __dirname + '/shots'; fs.mkdirSync(OUT, { recursive: true }); fs.mkdirSync(OUT + '/strips', { recursive: true });
const R = {}; const log = (...a) => console.log(...a);
(async () => {
  fs.rmSync(__dirname + '/profile', { recursive: true, force: true });
  const ctx = await chromium.launchPersistentContext(__dirname + '/profile', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  await ctx.route(/huggingface/, (r) => r.abort());
  const p = ctx.pages()[0] || await ctx.newPage();
  p.on('console', (m) => { if (m.type() === 'error') log('console:', m.text().slice(0, 140)); });
  const rect = (sel) => p.evaluate((s) => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); return { x: b.x, y: b.y, w: b.width, h: b.height }; }, sel);
  const rects = async (name, sels) => { R[name] = {}; for (const [k, s] of Object.entries(sels)) R[name][k] = await rect(s); };
  const shot = async (name, sels = {}) => { await p.waitForTimeout(350); await p.screenshot({ path: `${OUT}/${name}.png` }); await rects(name, sels); log('shot', name); };
  const tall = async (name, h, sels = {}) => { await p.setViewportSize({ width: 390, height: h }); await p.waitForTimeout(500); await shot(name, sels); await p.setViewportSize({ width: 390, height: 844 }); await p.waitForTimeout(400); };
  const closeSheets = async () => { await p.evaluate(() => { const s = document.querySelector('#scrim'); if (s) s.click(); }); await p.waitForTimeout(450); };
  const go = async (v) => { await p.click(`nav.bottom [data-view=${v}]`); await p.waitForTimeout(700); };
  const step = async (label, fn) => { try { await fn(); } catch (e) { log('FAILED', label, e.message.split('\n')[0]); } };

  await p.goto('file://' + APP); await p.waitForTimeout(1200);
  await p.evaluate(() => { localStorage.setItem('wardrobe-ai', JSON.stringify({ asked: true, cut: true, type: false })); });
  await p.setInputFiles('#restore-in', __dirname + '/seed-backup.json');
  await p.waitForSelector('#modal.on'); await p.click('#m-ok'); await p.waitForTimeout(2500);
  await p.reload(); await p.waitForTimeout(2500);

  // ---------- chapter 2: the wardrobe ----------
  await step('home', () => shot('w-home', { header: 'header.top', nav: 'nav.bottom', add: '#btn-add', q: '#q', today: '#today', tabs: '#cat-tabs', lists: '#btn-lists', ins: '#btn-insights', set: '#btn-settings', trousers: '#cupboard [data-item=trousers]' }));
  await step('home tall', () => tall('w-tall', 2300, { header: 'header.top', nav: 'nav.bottom', main: 'main' }));
  await step('search', async () => {
    await p.click('#q'); for (const [i, ch] of [...'denim'].entries()) { await p.keyboard.type(ch); if (i === 1 || i === 4) await shot(`w-q${i + 1}`); }
    await p.fill('#q', ''); await p.keyboard.press('Escape'); await p.waitForTimeout(400);
  });
  await step('tab shoes', async () => { await p.click('#cat-tabs [data-cat=shoes]'); await shot('w-shoes', { tab: '#cat-tabs [data-cat=shoes]' }); await p.click('#cat-tabs [data-cat=all]'); });
  await step('detail', async () => {
    await p.click('#cupboard [data-item=trousers]'); await shot('w-detail', { wear: '#d-wear', wash: '#d-wash', arch: '#d-arch', stat: '#d-stat', facts: '#d-facts' });
    await p.click('#d-wear'); await shot('w-detail-worn', { wear: '#d-wear' });
    await p.click('#d-wear'); await closeSheets();
  });

  // ---------- chapter 3: try on ----------
  await step('tryon', async () => {
    await go('tryon'); const tst = await p.addStyleTag({ content: '#toast{visibility:hidden!important}' }); await p.waitForTimeout(300);
    await shot('t-base', { stage: '#stage', styleme: '#btn-styleme', create: '#btn-create', nope: '#btn-nope', shuffle: '#btn-shuffle', extras: '#btn-extras', board: '#btn-board', lockTop: '[data-lock=tops]' });
    R.rows = await p.evaluate(() => [...document.querySelectorAll('#stage .trow')].map((t) => { const b = t.getBoundingClientRect(); return { cat: t.dataset.cat, x: b.x, y: b.y, w: b.width, h: b.height, n: t.querySelectorAll('.slide').length }; }));
    const st = await p.addStyleTag({ content: '#stage .slide img{visibility:hidden} #stage .tmeta{visibility:hidden}' });
    await shot('t-bg');
    await p.evaluate((e) => e.remove(), st);
    const st2 = await p.addStyleTag({ content: 'html,body,.app,main,#view-tryon{background:transparent!important} #stage{background:transparent!important;box-shadow:none!important} #stage .tnav,#stage .lock,#stage .tmeta{visibility:hidden} header,nav,.tryon-bar,.tryon-acts,#btn-styleme,#btn-create,#btn-nope{visibility:hidden}' });
    for (let r = 0; r < R.rows.length; r++) for (let i = 0; i < R.rows[r].n; i++) {
      await p.evaluate(([r, i]) => { const t = document.querySelectorAll('#stage .trow .track')[r]; t.style.scrollSnapType = 'none'; t.scrollLeft = i * t.clientWidth; }, [r, i]);
      await p.waitForTimeout(80); const b = R.rows[r];
      await p.screenshot({ path: `${OUT}/strips/r${r}-${i}.png`, omitBackground: true, clip: { x: b.x, y: b.y, width: b.w, height: b.h } });
    }
    await p.evaluate((e) => e.remove(), st2);
    await p.evaluate(() => document.querySelectorAll('#stage .trow .track').forEach((t) => { t.scrollLeft = 0; t.style.scrollSnapType = ''; }));
  });
  await step('lock', async () => { await p.click('[data-lock=tops]'); await shot('t-lock', { lockTop: '[data-lock=tops]' }); await p.click('[data-lock=tops]'); await p.waitForTimeout(300); });
  await step('extras', async () => { await p.click('#btn-extras'); await shot('t-extras', { extras: '#btn-extras', stage: '#stage' }); await p.click('#btn-extras'); await p.waitForTimeout(300); });
  await step('style me', async () => { await p.evaluate(() => document.querySelectorAll('style').forEach((s) => { if (s.textContent.includes('#toast{visibility:hidden!important}')) s.remove(); })); await p.click('#btn-styleme'); await p.waitForTimeout(900); await shot('t-style'); R.styled = await p.evaluate(() => [...document.querySelectorAll('#stage .trow')].map((t) => t.querySelector('.cnt') && t.querySelector('.cnt').textContent)); });
  await step('nope', async () => { await p.click('#btn-nope'); await p.waitForTimeout(300); await shot('t-nope', { toast: '#toast' }); await p.waitForTimeout(2500); });

  // ---------- chapter 4: outfits ----------
  await step('board', async () => {
    await p.click('#btn-create'); await p.waitForTimeout(1200); await shot('o-board', { save: '#bs-save', color: '#bs-color', undo: '#bs-undo', area: '#bs-area' });
    const it = await rect('#board .bitem'); R.bitem = it;
    if (it) { await p.mouse.click(it.x + it.w / 2, it.y + it.h / 2); await shot('o-board-sel', { sel: '#board .bitem.sel' });
      await p.mouse.move(it.x + it.w / 2, it.y + it.h / 2); await p.mouse.down(); await p.mouse.move(it.x + it.w / 2 + 40, it.y + it.h / 2 - 30, { steps: 8 }); await p.mouse.up(); await shot('o-board-moved', { sel: '#board .bitem.sel' }); }
    await p.click('#bs-color'); await p.waitForTimeout(400); await shot('o-board-colour');
    await p.keyboard.press('Escape'); await p.evaluate(() => { const m = document.querySelector('#modal.on #m-cancel'); if (m) m.click(); }); await p.waitForTimeout(300);
    await p.click('#bs-save'); await p.waitForTimeout(600);
    if (await p.$('#modal.on')) { await p.fill('#m-extra input', 'Rust and white'); await p.click('#m-ok'); }
    await p.waitForTimeout(1200); await shot('o-grid');
  });
  await step('outfit sheet', async () => { await p.click('#outfits [data-open=o-weekend]'); await p.waitForTimeout(600); await shot('o-sheet', { share: '#o-share', plan: '#o-plan', wear: '#o-wear', dup: '#o-dup', fav: '#o-fav', tags: '#o-tags' }); await closeSheets(); });

  // ---------- chapter 5: plan (city first, for the forecast) ----------
  await step('city', async () => {
    await p.click('#btn-settings'); await p.waitForTimeout(500); for (let k = 0; k < 6; k++) { await p.fill('#set-city', 'Lisbon'); await p.click('#btn-city'); await p.waitForTimeout(4000); if (/°/.test(await p.textContent('#wx-status'))) break; log('weather retry', k); }
    await p.waitForTimeout(2500); if (await p.$('#modal.on [data-v]')) { await p.click('#modal.on [data-v]'); await p.waitForTimeout(2500); }
    log('weather:', await p.textContent('#wx-status').catch(() => '?')); await closeSheets();
  });
  await step('plan', async () => {
    await go('plan'); await p.waitForTimeout(800); await shot('p-agenda', { today: '#plan [id^=day-] .on, #plan [data-worn]', auto: '#plan [data-auto]' });
    await p.click('[data-pmode=month]'); await shot('p-month'); await p.click('[data-pmode=agenda]'); await p.waitForTimeout(600);
    const a = await rect('#plan [data-auto]'); R.auto = a;
    if (a) { await p.click('#plan [data-auto]'); await p.waitForTimeout(500); await shot('p-auto', { toast: '#toast' }); }
    await p.waitForTimeout(2600);
    const st = await p.evaluate(() => document.querySelector('#view-plan').scrollTop);
    const w = await rect('#day-2026-11-13 [data-worn]'); R.worn = w;
    await shot('p-before', { worn: '#day-2026-11-13 [data-worn]', month: '[data-pmode=month]' });
    await p.click('#day-2026-11-13 [data-worn]'); await p.waitForTimeout(500); await p.evaluate((s) => { document.querySelector('#view-plan').scrollTop = s; }, st); await shot('p-worn', { worn: '#day-2026-11-13 [data-worn]' });
  });

  // ---------- chapter 6: lists ----------
  await step('lists', async () => {
    await p.click('#btn-lists'); await shot('l-home', { cap: '[data-sopen=s-cap]', trip: '[data-sopen=s-trip]', wish: '[data-ltab=wish]' });
    await p.click('[data-sopen=s-cap]'); await shot('l-cap'); await p.click('[data-sback]'); await p.waitForTimeout(300);
    await p.click('[data-sopen=s-trip]'); await shot('l-trip', { item: '[data-sitem=sneakers2]' });
    await p.click('[data-sitem=sneakers2]'); await shot('l-trip2', { item: '[data-sitem=sneakers2]' });
    await p.click('[data-sback]'); await p.waitForTimeout(300); await p.click('[data-ltab=wish]'); await shot('l-wish');
    await p.click('[data-ltab=sets]'); await closeSheets();
  });

  // ---------- chapter 7: insights ----------
  await step('insights', async () => { await p.click('#btn-insights'); await shot('i-top'); await tall('i-tall', 2600); await closeSheets(); });

  // ---------- chapter 8: settings, theme, accent ----------
  await step('settings', async () => {
    await p.click('#btn-settings'); await shot('s-top', { theme: '#theme-seg', accent: '#accent-row', cur: '#set-cur' }); await tall('s-tall', 2400, { backup: '#btn-backup', restore: '[for=restore-in]' });
    await p.click('#theme-seg >> text=Dark'); await shot('s-dark');
    await p.click('#accent-row [data-accent=Rose]'); await shot('s-rose');
    await closeSheets(); await go('wardrobe'); await shot('w-dark-rose'); await go('tryon'); await shot('t-dark-rose');
    await p.click('#btn-settings'); await p.click('#accent-row [data-accent=Indigo]'); await p.click('#theme-seg >> text=Light'); await closeSheets(); await go('wardrobe');
  });

  // ---------- chapter 1: add clothes (last, so the new piece stays out of the other chapters) ----------
  await step('add', async () => {
    await p.click('#btn-add'); await shot('a-sheet', { guide: '#guide-track', pick: '#step-pick' });
    await p.evaluate(() => { const g = document.querySelector('#guide-track'); g.style.scrollBehavior = 'auto'; g.scrollLeft = g.scrollWidth; }); await shot('a-guide2');
    await p.evaluate(() => { const g = document.querySelector('#guide-track'); g.scrollLeft = 0; });
    await p.addStyleTag({ content: '#toast{visibility:hidden}' });
    await p.setInputFiles('#file-in', '/home/user/Image-Scanner/brag-output/film/wardrobe/public/assets/tee.jpg');
    const t0 = Date.now(); let k = 0;
    for (;;) { await p.waitForTimeout(250); const busy = await p.evaluate(() => document.querySelector('#busy').classList.contains('on'));
      if (k < 60) { await p.screenshot({ path: `${OUT}/a-cut-${String(k++).padStart(2, '0')}.png` }); }
      if (!busy && Date.now() - t0 > 2500) break; if (Date.now() - t0 > 180000) break; }
    await p.waitForTimeout(500); await shot('a-cut-done', { cwrap: '#cwrap', erase: '#b-erase', restore: '#b-restore', zin: '#z-in', bsize: '#bsize', smart: '#method-seg' });
    log('cut frames', k, 'in', (Date.now() - t0) / 1000, 's');
    await p.click('#z-in'); await p.click('#z-in'); await shot('a-zoom'); await p.click('#z-fit'); await p.waitForTimeout(300);
    await p.click('#b-restore'); await shot('a-restore', { restore: '#b-restore' }); await p.click('#b-erase');
    const body = '#edit-body';
    await p.evaluate((b) => { document.querySelector(b).scrollTop = document.querySelector('#step-form').offsetTop - 10; }, body);
    await shot('a-form1', { cat: '#f-cat', type: '#f-type', name: '#f-name', detected: '#detected' });
    await p.click('#f-cat >> text=Tops').catch(() => {}); await p.click('#f-type >> text=T-shirt').catch(() => {});
    await p.fill('#f-name', 'White tee'); await p.fill('#f-brand', 'Everyday'); await p.fill('#f-sizelabel', 'M'); await p.fill('#f-price', '799');
    await shot('a-form1b', { name: '#f-name', brand: '#f-brand', price: '#f-price' });
    await p.evaluate(() => { const b = document.querySelector('#edit-body'), s = document.querySelector('#f-size'); b.scrollTop = s.getBoundingClientRect().top - b.getBoundingClientRect().top + b.scrollTop - 120; });
    await shot('a-form2', { size: '#f-size', color: '#f-color', occ: '#f-occ' });
    await p.click('#f-occ >> text=Casual').catch(() => {}); await p.click('#f-occ >> text=Travel').catch(() => {});
    await p.evaluate(() => { const b = document.querySelector('#edit-body'); b.scrollTop = b.scrollHeight; }); await p.click('#f-season >> text=All-season').catch(() => {});
    await shot('a-form3', { season: '#f-season', occ: '#f-occ', save: '#btn-save-item' });
    await p.evaluate(() => { const s = document.querySelector('style:last-of-type'); }); await p.addStyleTag({ content: '#toast{visibility:visible!important}' });
    await p.click('#btn-save-item'); await p.waitForTimeout(700); await shot('a-saved', { toast: '#toast' });
  });

  fs.writeFileSync(OUT + '/rects.json', JSON.stringify(R, null, 1));
  await ctx.close();
})();
