# Builds film-v.html (1080x1920, the Instagram tall frame) from film.html (1920x1080): every scene laid out again
# for the tall frame, the same timeline, the same carried tag. Also teaches render.js the V=1 switch.
s = open('film.html').read()
R = [
("html,body{width:1920px;height:1080px;", "html,body{width:1080px;height:1920px;"),
(".line{position:absolute;left:0;width:1920px;", ".line{position:absolute;left:0;width:1080px;"),
('<div id="tags" class="abs" style="width:1920px;height:1080px">', '<div id="tags" class="abs" style="width:1080px;height:1920px">'),
('<div id="flood" class="abs" style="width:1920px;height:1080px;', '<div id="flood" class="abs" style="width:1080px;height:1920px;'),
('<div id="end" class="abs" style="width:1920px;height:1080px;', '<div id="end" class="abs" style="width:1080px;height:1920px;'),
# scene 1: the sheet in the middle, paper strips to the bottom
("${svg(2000, 260, paper(jag([[-40, 30], [500, 6], [1000, 34], [1500, 0], [2040, 28], [2040, 260], [-40, 260]], 9, 40), c))}",
 "${svg(2000, 900, paper(jag([[-40, 30], [500, 6], [1000, 34], [1500, 0], [2040, 28], [2040, 900], [-40, 900]], 9, 40), c))}"),
("s1.style.transform = `scale(${push(.37, 3.5, 1.03)})`;", "s1.style.transform = `translate(-420px,420px) scale(${.85 * push(.37, 3.5, 1.03)})`;"),
("const sk = ex(P(t, .37, 1.2)); x = 960; y = 175 + 200 + TH / 2 + (1 - sk) * 900; s = 1; r = -1.5;",
 "const sk = ex(P(t, .37, 1.2)); x = 540; y = 960 + (1 - sk) * 900 * .85; s = .85; r = -1.5;"),
# scene 2: rail and clothes on top, the tag in the middle, the phone below
('<div id="phone" class="abs" style="left:465px;top:1100px">', '<div id="phone" class="abs" style="left:355px;top:1940px">'),
('<div id="rail" class="abs" style="left:150px;top:150px">', '<div id="rail" class="abs" style="left:40px;top:200px">'),
('style="left:${220 + i * 190}px;top:250px;transform-origin:75px -78px"', 'style="left:${70 + i * 190}px;top:300px;transform-origin:75px -78px"'),
("const tx = i === 4 ? 650 : 570 + (i % 2) * 160, ty = 430 + Math.floor(i / 2) * 185, gx = tx - (295 + 190 * i), gy = ty - 172;",
 "const tx = i === 4 ? 540 : 460 + (i % 2) * 160, ty = 1270 + Math.floor(i / 2) * 185, gx = tx - (145 + 190 * i), gy = ty - 222;"),
# scene 3: the cooker centred and big, on a tall stove
("${svg(2000, 200, paper(jag([[-40, 20], [2040, 10], [2040, 200], [-40, 200]], 4, 50), '#161922'))}",
 "${svg(2000, 900, paper(jag([[-40, 20], [2040, 10], [2040, 900], [-40, 900]], 4, 50), '#161922'))}"),
("transform: `translate(${ex3}px,${120 + sink * 700}px) scale(1.32)`", "transform: `translate(${ex3 - 420}px,${560 + sink * 900}px) scale(1.32)`"),
("transform: `translate(${1330 + i * 0}px,", "transform: `translate(${1180 + i * 0}px,"),
# the tag's path in the tall frame
("const TK = [[3.3, 960, 540, 1, -1.5], [3.95, 960, 470, 1.04, 2], [4.7, 1380, 560, .92, -2], [9.0, 1380, 560, .92, -2], [9.5, 960, 300, .95, 1.5], [14.5, 960, 300, .95, 1.5], [15.2, 960, 540, 1.15, 0], [18.1, 960, 540, 1.15, 0], [18.45, 960, 540, 1.32, 0], [19.92, 960, 540, 1.32, 0]];",
 "const TK = [[3.3, 540, 960, .85, -1.5], [3.95, 540, 900, .9, 2], [4.7, 540, 900, .95, -2], [9.0, 540, 900, .95, -2], [9.5, 540, 700, .95, 1.5], [14.5, 540, 700, .95, 1.5], [15.2, 540, 960, 1.0, 0], [18.1, 540, 960, 1.0, 0], [18.45, 540, 960, 1.12, 0], [19.92, 540, 960, 1.12, 0]];"),
("x = lerp(960, 1560, k); y = lerp(540, 560, k); s = lerp(1.32, .3, k);", "x = lerp(540, 840, k); y = lerp(960, 1148, k); s = lerp(1.12, .3, k);"),
# scene 4: a tall wall of tags
("const cols = 14, rows = 9;", "const cols = 7, rows = 15;"),
("const x = (c + .5) / cols * 2040 - 60 + (rnd() - .5) * 70, y = (r + .5) / rows * 1160 - 40 + (rnd() - .5) * 60;\n    if (Math.abs(x - 960) < 520 && Math.abs(y - 540) < 250) continue;",
 "const x = (c + .5) / cols * 1180 - 50 + (rnd() - .5) * 60, y = (r + .5) / rows * 2000 - 40 + (rnd() - .5) * 50;\n    if (Math.abs(x - 540) < 500 && Math.abs(y - 960) < 230) continue;"),
("const bx = (g.x - 960) * burst * 1.8, by = (g.y - 540) * burst * 1.8;", "const bx = (g.x - 540) * burst * 1.8, by = (g.y - 960) * burst * 1.8;"),
# scene 5: hills low, a tall sky for the lines, the path up to the flag
('<div class="abs hill" data-z="${z}" style="top:${y - 140}px;transform-origin:960px 0">', '<div class="abs hill" data-z="${z}" style="top:${y - 140 + 700}px;left:-600px">'),
("${svg(2400, 700, paper(jag(pts, 5, 40), c), 'pp', 'margin-left:0')}", "${svg(2400, 900, paper(jag(pts.map(([a, b]) => [a, b === 700 ? 900 : b]), 5, 40), c), 'pp', 'margin-left:0')}"),
("${svg(1920, 1080, paper('M640 1080 C760 960 1180 960 1120 860 C1060 780 980 760 1180 700 C1320 660 1460 640 1540 626 L1556 634 C1480 652 1350 680 1230 716 C1060 770 1180 800 1250 870 C1350 980 1060 1010 1000 1080 Z', '#FFFFFF'), 'pp')}",
 "${svg(1080, 1920, paper('M300 1920 C420 1790 760 1760 700 1650 C640 1550 500 1510 620 1445 C680 1405 705 1370 698 1336 L714 1338 C728 1372 712 1415 650 1458 C548 1522 680 1560 742 1650 C830 1790 560 1810 520 1920 Z', '#FFFFFF'), 'pp')}"),
("e.style.transformOrigin = '1548px 630px'; });", "e.style.transformOrigin = `${706 + (e.style.left ? 600 : 0)}px ${1335 - (parseFloat(e.style.top) || 0)}px`; });"),
("set($('#flag'), { transform: `translate(1548px,${630 + (1 - fu) * 30}px)", "set($('#flag'), { transform: `translate(700px,${1335 + (1 - fu) * 30}px)"),
('<div id="sun" class="abs" style="left:250px;top:150px">', '<div id="sun" class="abs" style="left:110px;top:430px">'),
("'be a part of<br>the journey.', 250, 150,", "'be a part of<br>the journey.', 700, 132,"),
("'what happens<br>after that?', 250, 150,", "'what happens<br>after that?', 700, 132,"),
("'let’s find out<br>together.', 250, 150,", "'let’s find out<br>together.', 700, 132,"),
# the end card
("circle(${k * 2300}px at ${lerp(1640, 960, k)}px ${lerp(450, 540, k)}px)", "circle(${k * 2300}px at ${lerp(840, 540, k)}px ${lerp(1148, 960, k)}px)"),
("set($('#end'), { transform: `scale(${cr})`, transformOrigin: '960px 540px' });", "set($('#end'), { transform: `scale(${cr})`, transformOrigin: '540px 960px' });"),
('<div id="em" class="abs" style="left:810px;top:250px;', '<div id="em" class="abs" style="left:390px;top:680px;'),
('<div id="ew" class="mono line" style="top:610px;font-size:64px;', '<div id="ew" class="mono line" style="top:1040px;font-size:64px;'),
('<div id="ef" class="mono line" style="top:712px;font-size:34px;', '<div id="ef" class="mono line" style="top:1142px;font-size:34px;'),
]
for a, b in R:
    assert a in s, a[:80]
    s = s.replace(a, b)
open('film-v.html', 'w').write(s)
r = open('render.js').read()
if 'process.env.V' not in r:
    r = r.replace("const [, , mode = 'frames', arg] = process.argv;", "const [, , mode = 'frames', arg] = process.argv; const V = process.env.V === '1', WW = V ? 1080 : 1920, HH = V ? 1920 : 1080;")
    r = r.replace("viewport: { width: 1920, height: 1080 }", "viewport: { width: WW, height: HH }").replace("'/film.html'", "(V ? '/film-v.html' : '/film.html')")
    r = r.replace("`${D}/work/stills/s-${t.toFixed(2)}.jpg`", "`${D}/work/stills/${V ? 'v' : 's'}-${t.toFixed(2)}.jpg`").replace("const out = D + '/work/frames';", "const out = D + (V ? '/work/frames-v' : '/work/frames');")
    open('render.js', 'w').write(r)
print('film-v.html written')
