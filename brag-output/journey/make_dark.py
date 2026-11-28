# Dark, cinematic, handmade pass over a built film (film.html or film-v.html):
#  - dark paper: every colour remapped to a dark paper set, text in light ink, deeper shadows with a lit top edge
#  - a key light from above that drifts, a vignette, dust in the light, a defocused back layer, live film grain
#  - stop-motion: the whole picture steps on twos (12 fps) and every paper layer "boils" a pixel per step
# usage: python3 make_dark.py film.html film-dark.html
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
V = 'width:1080px;height:1920px' in s
W, H = (1080, 1920) if V else (1920, 1080)

# ---- 1. colours: light paper -> dark paper (shapes), ink stays deep ----
cmap = {
    '#FFFFFF': '#2E333F',   # paper cards, tags, the sheet
    '#DFE2E8': '#2B303B', '#C9CED8': '#0C0D11', '#B9BFCC': '#3A404D', '#9AA1B2': '#1F232B',
    '#3C4150': '#14161C', '#161922': '#08090C',
}
for a, b in cmap.items():
    s = s.replace(a, b)
# the stage and the line colour
s = s.replace(':root{--ink:#161922;--paper:#ECEEF2;', ':root{--ink:#E9ECF3;--paper:#101217;').replace(':root{--ink:#08090C;--paper:#ECEEF2;', ':root{--ink:#E9ECF3;--paper:#101217;')
# product kickers on dark tags take the lifted accents
s = s.replace("font-size:44px;color:#3D4FE0", "font-size:44px;color:#A5BBFF").replace("font-size:44px;color:#D9600F", "font-size:44px;color:#FFB07A")
# wall tags: light ink on dark paper, dark ink on the bright accent tags
s = s.replace("dark = col === '#08090C' || col === '#3D4FE0';", "dark = !['#A5BBFF', '#FFB07A', '#FF8A3D'].includes(col);")
s = s.replace("color:${dark ? '#ECEEF2' : '#08090C'}\">#${String", "color:${dark ? '#E9ECF3' : '#08090C'}\">#${String")
# flag tag and wall/tag text written in deep ink -> light
s = s.replace("font-size:170px;color:#08090C\">#1000", "font-size:170px;color:#E9ECF3\">#1000")
# steam: pale paper, so it reads on the dark
s = s.replace("3, 14), '#2E333F'), 'pp')}</div>`; }", "3, 14), '#C9CFDB'), 'pp')}</div>`; }")
# the sun becomes a pale moon; the path is lit paper
s = s.replace("'#FFB07A'), 'pp')}</div>`;\n  hills.forEach", "'#D9DEE8'), 'pp', 'filter:drop-shadow(0 0 30px rgba(220,228,255,.55)) drop-shadow(0 0 90px rgba(200,212,255,.3))')}</div>`;\n  hills.forEach")
s = s.replace("Z', '#2E333F'), 'pp')}</div>`;", "Z', '#BFC6D4'), 'pp')}</div>`;")
# the cut line and the sheet's hole
s = s.replace('fill="none" stroke="#08090C" stroke-width="4" stroke-dasharray="18 14"', 'fill="none" stroke="#E9ECF3" stroke-width="4" stroke-dasharray="18 14"')
# shadows: real black, a lit top edge on every piece
s = s.replace(".pp{filter:drop-shadow(0 2px 0 rgba(22,25,34,.10)) drop-shadow(0 12px 14px rgba(22,25,34,.20))}",
              ".pp{filter:drop-shadow(0 -1.5px 0 rgba(255,255,255,.10)) drop-shadow(0 3px 0 rgba(0,0,0,.45)) drop-shadow(0 16px 18px rgba(0,0,0,.55))}")
s = s.replace(".pp2{filter:drop-shadow(0 3px 0 rgba(22,25,34,.12)) drop-shadow(0 26px 26px rgba(22,25,34,.26))}",
              ".pp2{filter:drop-shadow(0 -2px 0 rgba(255,255,255,.12)) drop-shadow(0 4px 0 rgba(0,0,0,.5)) drop-shadow(0 30px 30px rgba(0,0,0,.6))}")
s = s.replace('fill="url(#g)" opacity=".55" style="mix-blend-mode:multiply"', 'fill="url(#g)" opacity=".35" style="mix-blend-mode:overlay"')
s = s.replace(".grain{position:absolute;inset:0;background:url(work/grain.png);mix-blend-mode:multiply;opacity:.22", ".grain{position:absolute;inset:0;background:url(work/grain.png);mix-blend-mode:overlay;opacity:.5").replace('svg{overflow:visible;display:block}', 'svg{overflow:visible;display:block} body{color:#E9ECF3}')
# the flood: from the flag into deep black, the mark is lit paper
s = s.replace("background:var(--ink);opacity:0\"></div>", "background:#07080A;opacity:0\"></div>")
s = s.replace("color:#ECEEF2\">wierd_stuff_i_make", "color:#E9ECF3\">wierd_stuff_i_make")

# ---- 2. the cinematic layers (on top of everything, inside the stage) ----
fx = f"""<div id="dof" class="abs" style="width:{W}px;height:{H}px;pointer-events:none"></div>
<div id="key" class="abs" style="width:{W}px;height:{H}px;pointer-events:none;mix-blend-mode:soft-light"></div>
<div id="glow" class="abs" style="width:{W}px;height:{H}px;pointer-events:none;mix-blend-mode:screen"></div>
<div id="dust" class="abs" style="width:{W}px;height:{H}px;pointer-events:none"></div>
<div id="vig" class="abs" style="width:{W}px;height:{H}px;pointer-events:none;background:radial-gradient(ellipse {W * .75:.0f}px {H * .75:.0f}px at 50% 44%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)"></div>
<div id="fgrain" class="abs" style="width:{W}px;height:{H}px;pointer-events:none;background:url(work/grain.png);mix-blend-mode:overlay;opacity:.35"></div>
</div>"""
s = s.replace('<div id="end" class="abs"', '<div id="end" class="abs"', 1)
s = s.replace('</div>\n<script>', fx + '\n<script>', 1)
assert 'id="key"' in s

hook = f"""
// ---------- the handmade, cinematic layer ----------
const _render = window.render, FW = {W}, FH = {H};
const hsh = (n) => {{ const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }};
(function () {{ let d = ''; for (let i = 0; i < 46; i++) {{ const r = 1.2 + hsh(i) * 2.6; d += `<div class="abs mote" style="width:${{r * 2}}px;height:${{r * 2}}px;border-radius:50%;background:rgba(235,240,255,${{.25 + hsh(i + 50) * .45}});filter:blur(${{hsh(i + 9) > .7 ? 2 : .6}}px)"></div>`; }} $('#dust').innerHTML = d; }})();
window.render = function (t) {{
  const step = Math.floor(t * 12), tq = step / 12;                     // stop-motion: the picture moves on twos
  _render(tq);
  const j = (k, a) => ((hsh(step * 7.31 + k) - .5) * 2 * a);               // the paper boils a little every step
  [['#scenes', 1.4, .12], ['#tag', 1.6, .18], ['#tags', 1.2, .1], ['#lines', 1.1, .1], ['#end', .8, .06]].forEach(([q, a, r], k) => {{
    const el = $(q); if (!el) return; el.style.translate = `${{j(k * 3 + 1, a).toFixed(2)}}px ${{j(k * 3 + 2, a).toFixed(2)}}px`; el.style.rotate = `${{j(k * 3 + 3, r).toFixed(3)}}deg`; }});
  // the key light: a pool from above that drifts slowly (continuous, like a real lamp), breathing a touch
  const lx = .5 + .08 * Math.sin(t * .23 + .6), ly = {.28 if V else .22} + .03 * Math.sin(t * .17), br = .9 + .1 * Math.sin(t * 1.3) * Math.sin(t * .37);
  $('#key').style.background = `radial-gradient(ellipse ${{FW * .62}}px ${{FH * .55}}px at ${{lx * 100}}% ${{ly * 100}}%, rgba(225,232,255,${{.85 * br}}) 0%, rgba(225,232,255,.25) 40%, rgba(0,0,0,.4) 100%)`;\n  $('#glow').style.background = `radial-gradient(ellipse ${{FW * .5}}px ${{FH * .4}}px at ${{lx * 100}}% ${{ly * 100}}%, rgba(200,212,255,${{.10 * br}}), rgba(0,0,0,0) 70%)`;
  // dust drifting through the light (real time, not stepped: it is the air, not the paper)
  [...document.querySelectorAll('.mote')].forEach((m, i) => {{ const sp = 10 + hsh(i + 3) * 22, x = (hsh(i + 1) * FW + Math.sin(t * .4 + i) * 40 + t * sp * .6) % FW, y = (hsh(i + 2) * FH - t * sp + FH * 4) % FH;
    const near = Math.max(0, 1 - Math.hypot(x / FW - lx, y / FH - ly) * 1.6); m.style.transform = `translate(${{x}}px,${{y}}px)`; m.style.opacity = (.15 + .85 * near).toFixed(2); }});
  // live film grain
  $('#fgrain').style.backgroundPosition = `${{Math.floor(hsh(step) * 512)}}px ${{Math.floor(hsh(step + .5) * 512)}}px`;
  // depth: the far hills sit out of focus
  document.querySelectorAll('.hill').forEach((h, i) => {{ if (i < 2) h.style.filter = `blur(${{2.4 - i}}px)`; }});
}};
"""
s = s.replace("\nbuild();\n", "\nbuild();\n" + hook, 1)
assert '_render' in s
open(dst, 'w').write(s)
print('wrote', dst, 'vertical' if V else 'horizontal')
