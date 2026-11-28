# Builds src/templates.html for #002 from the #001 kit's templates: same page system (ink on paper, the w-with-cursor
# mark, the chrome), the product colour swapped to the app's orange, the cooker icon as the product mark, real kitchen
# photos as grounds, and two new layouts (a giant count on a photo, a row of phones in six languages).
import os
HERE = os.path.dirname(os.path.abspath(__file__))
s = open('/home/user/Image-Scanner/brag-output/launch-kit/src/templates.html').read()
R = [
 ("--acc:#3D4FE0;--accl:#A5BBFF", "--acc:#D9600F;--accbg:#FF8A3D;--accl:#FFB07A;--warm:#1c1816"),
 ("#c.accbg{background:var(--acc);color:#fff} #c.accbg .sub{color:#e3e8ff}", "#c.accbg{background:var(--accbg);color:var(--ink)} #c.accbg .sub{color:#3a2a1e}"),
 ("const SHOT = (n) => `${ROOT}explainer/shots/${n}.png`, CUT = (n) => `${ROOT}explainer/items/${n}.png`;",
  "const SHOT = (n) => `${ROOT}whistle/shots/${n}.png`, CUT = (n) => `${ROOT}whistle/shots/${n}.png`, PHOTO = (n) => `${ROOT}launch-kit-002/build/photos/${n}.jpg`;"),
 ("rgba(61,79,224,.10)", "rgba(255,138,61,.12)"), ("rgba(165,187,255,.25)", "rgba(255,176,122,.22)"),
 ("${s.tag || '#001 wardrobe'}", "${s.tag || '#002 whistle counter'}"),
 ("s.kicker || 'build log · #001'", "s.kicker || 'build log · #002'"),
 ("s.kicker || 'product #001'", "s.kicker || 'product #002'"),
 ("s.kicker || '#001 wardrobe'", "s.kicker || '#002 · cooker whistle counter'"),
 ('<div class="mono" style="font-size:40px;color:var(--accl)">product #001</div>', '<div class="mono" style="font-size:40px;color:var(--accl)">product #002</div>'),
 ("// Wardrobe's own mark: the app's hanger", """// #002's mark: the app's own cooker icon (steam, lid, handles, pot); mono = one colour for orange grounds
const cooker = (size, mono) => { const f = (c) => mono || c; return `<svg width="${size}" height="${size}" viewBox="0 0 512 512"><g fill="none" stroke="${f('#A89A8C')}" stroke-width="16" stroke-linecap="round"><path d="M206 78c-14 14-14 34 0 48"/><path d="M256 78c-14 14-14 34 0 48"/><path d="M306 78c-14 14-14 34 0 48"/></g><rect x="236" y="140" width="40" height="52" rx="12" fill="${f('#F5EDE4')}"/><rect x="62" y="280" width="54" height="30" rx="15" fill="${f('#F5EDE4')}"/><rect x="396" y="280" width="54" height="30" rx="15" fill="${f('#F5EDE4')}"/><rect x="110" y="230" width="292" height="170" rx="46" fill="${f('#FF8A3D')}"/><rect x="96" y="190" width="320" height="52" rx="26" fill="${f('#FFB07A')}"/></svg>`; };
// (Wardrobe's hanger, kept for reference)"""),
 ("${hanger(170, '#fff', 1.2)}<div class=\"disp\" style=\"font-size:${s.size || 120}px;color:#fff\">${s.title || 'Wardrobe'}</div>\n    <div class=\"sub\" style=\"font-size:42px\">${s.sub || 'one html file. no account. link in bio.'}</div>\n    <div class=\"tag\" style=\"background:#fff;color:var(--ink);font-size:30px;margin-top:20px\">",
  "${cooker(190, '#1c1816')}<div class=\"disp\" style=\"font-size:${s.size || 120}px\">${s.title || 'Cooker Whistle<br>Counter'}</div>\n    <div class=\"sub\" style=\"font-size:42px\">${s.sub || 'one link. works offline. link in bio.'}</div>\n    <div class=\"tag\" style=\"background:var(--ink);color:#fff;font-size:30px;margin-top:20px\">"),
 ("${hanger(200, '#fff', 1.2)}<div class=\"disp\" style=\"font-size:${s.size || 130}px;color:#fff\">${s.title || 'Wardrobe'}</div><div class=\"sub\" style=\"font-size:46px\">${s.sub || 'one html file. no account.'}</div>",
  "${cooker(220, '#1c1816')}<div class=\"disp\" style=\"font-size:${s.size || 130}px\">${s.title || 'Cooker Whistle<br>Counter'}</div><div class=\"sub\" style=\"font-size:46px\">${s.sub || 'one link. works offline.'}</div>"),
 ("${hanger(200, '#fff', 1.2)}<div class=\"disp\" style=\"font-size:150px;color:#fff\">Wardrobe</div><div class=\"sub\" style=\"font-size:48px\">one html file. no account.</div>\n    <div class=\"tag\" style=\"background:#fff;color:var(--ink);font-size:34px;margin-top:10px\">link in bio</div>\n    <div class=\"mono\" style=\"font-size:30px;color:rgba(255,255,255,.7);margin-top:30px\">",
  "${cooker(220, '#1c1816')}<div class=\"disp\" style=\"font-size:130px\">Cooker Whistle<br>Counter</div><div class=\"sub\" style=\"font-size:48px\">one link. works offline.</div>\n    <div class=\"tag\" style=\"background:var(--ink);color:#fff;font-size:34px;margin-top:10px\">link in bio</div>\n    <div class=\"mono\" style=\"font-size:30px;color:rgba(28,24,22,.7);margin-top:30px\">"),
 ("${s.bg === 'acc' ? 'background:#fff' : ''}", "${s.bg === 'acc' ? 'background:var(--ink)' : ''}"),
 ("background:${dark ? 'rgba(255,255,255,.08)' : '#fff'};color:${dark ? '#fff' : 'var(--ink)'}", "background:${s.bg === 'acc' ? 'rgba(255,255,255,.4)' : dark ? 'rgba(255,255,255,.1)' : '#fff'};color:${dark && s.bg !== 'acc' ? '#fff' : 'var(--ink)'}"),
 ("color:${dark ? '#fff' : 'var(--acc)'}\">swipe →", "color:${s.bg === 'acc' ? 'var(--ink)' : dark ? 'var(--accl)' : 'var(--acc)'}\">swipe →"),
 ("const g = dark ? '#9aa1b2' : 'var(--grey)';", "const g = s.bg === 'acc' ? 'rgba(28,24,22,.6)' : s.photo ? 'rgba(245,237,228,.8)' : dark ? '#9aa1b2' : 'var(--grey)';"),
 ("T.hook = (s) => { const dark = s.bg === 'ink' || s.bg === 'acc';\n  let h = glows(1080, 1350, dark);",
  "const photoBg = (s, W, H) => s.photo ? `<img class=\"abs\" src=\"${PHOTO(s.photo)}\" style=\"left:0;top:0;width:${W}px;height:${H}px;object-fit:cover;object-position:${s.pos || '50% 50%'}\"><div class=\"abs\" style=\"inset:0;background:linear-gradient(180deg,rgba(22,18,16,.6),rgba(22,18,16,.2) 38%,rgba(22,18,16,.8))\"></div>` : '';\n"
  "T.hook = (s) => { const dark = s.bg === 'ink' || s.bg === 'acc' || !!s.photo;\n  let h = s.photo ? photoBg(s, 1080, 1350) : glows(1080, 1350, dark);"),
 ("T.s_hook = (s) => { const dark = s.bg === 'ink' || s.bg === 'acc'; let h = glows(1080, 1920, dark);",
  "T.s_hook = (s) => { const dark = s.bg === 'ink' || s.bg === 'acc' || !!s.photo; let h = s.photo ? photoBg(s, 1080, 1920) : glows(1080, 1920, dark);"),
 ("T.cover = (s) => { let h = glows(1080, 1920, s.bg === 'ink');", "T.cover = (s) => { let h = s.photo ? photoBg(s, 1080, 1920) : glows(1080, 1920, s.bg === 'ink');"),
 ("<div class=\"mono\" style=\"font-size:34px;color:${s.bg === 'ink' ? 'var(--accl)' : 'var(--acc)'};margin-bottom:28px\">${s.kicker || '#002 · cooker whistle counter'}</div>\n    <div class=\"disp\" style=\"font-size:${s.size || 116}px\">",
  "<div class=\"mono\" style=\"font-size:34px;color:${s.bg === 'ink' || s.photo ? 'var(--accl)' : 'var(--acc)'};margin-bottom:28px\">${s.kicker || '#002 · cooker whistle counter'}</div>\n    <div class=\"disp\" style=\"font-size:${s.size || 116}px;${s.photo ? 'color:#F5EDE4' : ''}\">"),
 ("${s.kicker ? `<div class=\"mono\" style=\"font-size:30px;color:${dark ? '#fff' : 'var(--acc)'}\">${s.kicker}</div>` : ''}\n    <div class=\"disp\" style=\"font-size:${s.size || 118}px\">",
  "${s.kicker ? `<div class=\"mono\" style=\"font-size:30px;color:${s.bg === 'acc' ? 'var(--ink)' : dark ? 'var(--accl)' : 'var(--acc)'}\">${s.kicker}</div>` : ''}\n    <div class=\"disp\" style=\"font-size:${s.size || 118}px\">"),
 ("${s.kicker ? `<div class=\"mono\" style=\"font-size:34px;color:${dark ? 'var(--accl)' : 'var(--acc)'}\">${s.kicker}</div>` : ''}",
  "${s.kicker ? `<div class=\"mono\" style=\"font-size:34px;color:${s.bg === 'acc' ? 'var(--ink)' : dark ? 'var(--accl)' : 'var(--acc)'}\">${s.kicker}</div>` : ''}"),
 ("#c.ink{background:var(--ink);color:var(--paper)} #c.ink .sub{color:#c9cdd8}",
  "#c.ink{background:var(--ink);color:var(--paper)} #c.ink .sub{color:#c9cdd8} #c.photo{background:#161210;color:#F5EDE4} #c.photo .sub{color:#efe3d6}"),
 ("c.className = s.bg === 'ink'", "c.className = s.photo || s.t === 'count' ? 'photo' : s.bg === 'ink'"),
 ("// ---------- story 1080x1920", """T.count = (s) => { let h = photoBg(s, 1080, 1350);
  h += `<div class="abs disp" style="left:0;right:0;top:${s.bigY || 150}px;text-align:center;font-size:${s.bigSize || 760}px;line-height:1;color:var(--accbg);letter-spacing:-.06em">${s.big}</div>
    <div class="abs" style="left:72px;right:72px;bottom:150px;text-align:center"><div class="disp" style="font-size:${s.size || 96}px">${s.title}</div>${s.sub ? `<div class="sub" style="font-size:40px;margin-top:20px">${s.sub}</div>` : ''}</div>`;
  return h + chrome(s, 1080, 1350, 64, 60, true); };
T.langs = (s) => { const dark = s.bg === 'ink'; let h = glows(1080, 1350, dark); const y = 430;
  h += `<div class="abs" style="left:72px;right:72px;top:140px"><div class="disp" style="font-size:${s.size || 84}px">${s.title}</div>${s.sub ? `<div class="sub" style="font-size:34px;margin-top:16px">${s.sub}</div>` : ''}</div>`;
  s.screens.forEach((sc, i) => { h += phone(78 + i * 318, y, 290, sc, s.crop || 0); });
  if (s.labels) h += s.labels.map((l, i) => `<div class="abs mono" style="left:${78 + i * 318}px;top:${y + 625}px;width:290px;text-align:center;font-size:28px;color:${dark ? '#c9cdd8' : 'var(--grey)'}">${l}</div>`).join('');
  return h + chrome(s, 1080, 1350, 64, 60, dark); };
// ---------- story 1080x1920"""),
 ("window.parts = { pageMark, hanger };", "window.parts = { pageMark, hanger, cooker };"),
]
for a, b in R:
    assert a in s, a[:80]
    s = s.replace(a, b)
open(os.path.join(HERE, 'templates.html'), 'w').write(s)
print('templates.html written')
