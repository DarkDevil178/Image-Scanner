# The #002 kit's documents: brand guidelines (the page system + #002), the start-here playbook, the calendar
# (overview + one page per day + the library), calendar.csv and a caption.txt in every day's folder.
# Pages are 1600x1000 (pdf.js renders them to PDF).
import json, csv, html, os, glob
from PIL import Image
K = '/home/user/Image-Scanner/brag-output/launch-kit-002'; O = f'{K}/out'; BUILD = f'{K}/build'
P = json.load(open(f'{BUILD}/plan.json')); BON = json.load(open(f'{BUILD}/bonus.json'))
HANDLE = '@wierd_stuff_i_make'
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_css.py')).read())   # CSS (shared with the #001 kit, #002 accent)
# thumbnails for the documents
for f in glob.glob(f'{O}/**/*.png', recursive=True):
    t = f'{BUILD}/thumbs/{os.path.relpath(f, O)[:-4]}.jpg'
    if not os.path.exists(t) or os.path.getmtime(t) < os.path.getmtime(f):
        os.makedirs(os.path.dirname(t), exist_ok=True); im = Image.open(f).convert('RGB'); im.thumbnail((540, 960)); im.save(t, quality=85)
FILE = lambda p: f'file://{BUILD}/thumbs/{p[:-4]}.jpg'
SHOT = lambda n: f'file:///home/user/Image-Scanner/brag-output/whistle/shots/{n}.png'
def page(inner, cls='', n=None, label=''):
    return f'<div class="page {cls}">{inner}<div class="foot"><span>{HANDLE}</span><span>{label}{" · " + str(n) if n else ""}</span></div></div>'
def esc(s): return html.escape(s).replace('\n', '<br>')
OR, ORD, ORL = '#FF8A3D', '#D9600F', '#FFB07A'
mark = lambda size, cursor=OR, bg='#161922', fg='#ECEEF2': f"""<div style="width:{size}px;height:{size}px;border-radius:22%;background:{bg};display:grid;place-items:center">
 <div style="position:relative;font:800 {size*0.62}px/1 'Bricolage Grotesque';letter-spacing:-.04em;color:{fg};transform:translate(-{size*0.06}px,-{size*0.06}px)">w<span style="position:absolute;left:100%;bottom:{size*0.04}px;margin-left:{size*0.05}px;width:{size*0.2}px;height:{size*0.07}px;border-radius:{size*0.02}px;background:{cursor}"></span></div></div>"""
word = lambda size, color='#161922', cur=OR: f"""<span style="font:500 {size}px/1 'DM Mono';letter-spacing:-.02em;color:{color}">wierd_stuff_i_make<span style="display:inline-block;width:{size*0.5}px;height:{size*0.12}px;background:{cur};margin-left:{size*0.08}px;border-radius:2px"></span></span>"""
def cooker(size, mono=None):
    f = lambda c: mono or c
    return f'<svg width="{size}" height="{size}" viewBox="0 0 512 512"><g fill="none" stroke="{f("#A89A8C")}" stroke-width="16" stroke-linecap="round"><path d="M206 78c-14 14-14 34 0 48"/><path d="M256 78c-14 14-14 34 0 48"/><path d="M306 78c-14 14-14 34 0 48"/></g><rect x="236" y="140" width="40" height="52" rx="12" fill="{f("#F5EDE4")}"/><rect x="62" y="280" width="54" height="30" rx="15" fill="{f("#F5EDE4")}"/><rect x="396" y="280" width="54" height="30" rx="15" fill="{f("#F5EDE4")}"/><rect x="110" y="230" width="292" height="170" rx="46" fill="{f("#FF8A3D")}"/><rect x="96" y="190" width="320" height="52" rx="26" fill="{f("#FFB07A")}"/></svg>'
D = {p['day']: p for p in P}
def F(day, i=0): return D[day]['feed'][i]
def S(day, i=0): return D[day]['stories'][i]

# ======================= brand guidelines =======================
L = 'brand guidelines · #002'
pages = [page(f"""<div style="display:flex;flex-direction:column;justify-content:center;height:100%;gap:40px">{mark(150)}
  <h1 style="color:#ECEEF2">brand<br>guidelines.</h1><div style="font:500 30px 'DM Mono';color:{ORL}">{HANDLE} · launching product #002: Cooker Whistle Counter</div></div>""", 'ink', label=L)]
pages.append(page(f"""<div class="k">01 · the page, unchanged</div><h2>ink on paper. each product brings its colour.</h2>
 <div class="cols c3" style="margin-top:40px">
 <div class="card"><h3>what stays the same</h3><p>the page mark (w with a cursor), the handle as wordmark, ink #161922 on paper #ECEEF2, Bricolage Grotesque / DM Sans / DM Mono, the chrome on every post: handle top-left, product tag top-right, counter bottom-right.</p></div>
 <div class="card"><h3>what #002 changes</h3><p>the cursor, the accent and the tag turn orange, the app's own colour. the product mark is the app's cooker icon. kitchen photos join cut-outs as the imagery.</p></div>
 <div class="card"><h3>the series</h3><p><span class="mono">#001 Wardrobe</span> indigo · <span class="mono">#002 Cooker Whistle Counter</span> orange · <span class="mono">#003 …</span> its own colour. the number is part of the name: in tags, kickers and covers.</p></div></div>
 <div style="display:flex;gap:60px;align-items:center;margin-top:50px">{mark(170, '#3D4FE0')}<div style="font:500 26px 'DM Mono';color:#7C8494">#001 →</div>{mark(170)}<div style="font:500 26px 'DM Mono';color:#7C8494">#002 · now</div>{mark(170, '#ECEEF2')}<div style="font:500 26px 'DM Mono';color:#7C8494">between launches</div></div>""", label=L, n=2))
pages.append(page(f"""<div class="k">02 · the marks</div><h2>the page mark and the product mark.</h2>
 <div class="cols c3" style="align-items:center;margin-top:20px"><div style="display:grid;place-items:center">{mark(280)}</div>
 <div style="display:grid;place-items:center;background:#1c1816;border-radius:28px;height:300px">{cooker(240)}</div><div style="display:grid;place-items:center;background:{OR};border-radius:28px;height:300px">{cooker(240, '#1c1816')}</div></div>
 <div class="cols c3" style="margin-top:28px"><p>the page mark during #002: ink tile, paper "w", orange cursor. it is the profile picture until the next launch.</p>
 <p>the product mark: the app's own icon (steam, lid, handles, pot), in full colour on ink or the app's warm dark.</p><p>on orange: the cooker in one colour, ink #1c1816. never put the full-colour cooker on orange; it disappears.</p></div>
 <div class="card" style="margin-top:34px;padding:34px;display:flex;align-items:center;gap:50px">{word(52)}<span style="font:800 64px/1 'Bricolage Grotesque';letter-spacing:-.04em">Cooker Whistle Counter</span></div>""", label=L, n=3))
sw = lambda c, n, h, note: f'<div><div class="sw" style="background:{c};{"border:2px solid #DFE2E8" if c in ("#FFFFFF", "#ECEEF2") else ""}"></div><h3>{n}</h3><div class="mono" style="font-size:18px;color:#7C8494">{h}</div><p style="font-size:18px">{note}</p></div>'
pages.append(page(f"""<div class="k">03 · colour</div><h2>orange, from the app itself.</h2>
 <div class="cols c4" style="gap:28px">{sw('#161922', 'ink', '#161922', 'type, the page mark, dark slides.')}{sw('#ECEEF2', 'paper', '#ECEEF2', 'the ground of text posts and stories.')}{sw('#FFFFFF', 'white', '#FFFFFF', 'cards and surfaces.')}{sw('#7C8494', 'grey', '#7C8494', 'handles, counters, secondary text.')}</div>
 <div class="cols c4" style="gap:28px;margin-top:30px">{sw(OR, '#002 orange', OR, 'the app\'s accent: CTA grounds, the count, the cursor. ink type on it, never white.')}{sw(ORD, 'orange, deep', ORD, 'orange as text on paper (kickers, numbers): passes contrast where #FF8A3D does not.')}{sw(ORL, 'orange, lifted', ORL, 'the accent on ink and on photos.')}{sw('#1c1816', 'app warm dark', '#1c1816', 'the app\'s own background: behind the cooker mark, in reels.')}</div>""", label=L, n=4))
pages.append(page(f"""<div class="k">04 · imagery</div><h2>real kitchens. the real app.</h2>
 <div class="cols" style="grid-template-columns:repeat(4,1fr);gap:24px;align-items:start">
 <img class="th" src="{FILE(F(1))}" style="width:100%"><img class="th" src="{FILE(F(5))}" style="width:100%"><img class="th" src="{FILE(F(5, 2))}" style="width:100%"><img class="th" src="{FILE(BON[1]['feed'][0])}" style="width:100%"></div>
 <div class="cols c3" style="margin-top:30px"><p><b>photos</b>: real pressure cookers, gas flames, dal and rice, graded warm-dark with a top and bottom shade so cream type reads. all public-domain / CC0, no credit needed.</p>
 <p><b>screens</b>: captured from the real app while it counted real whistles through a microphone, in a dark phone frame. never mock a screen.</p><p><b>never</b>: stock people pointing at phones, fake numbers, a language the app doesn't have, a feature it doesn't do.</p></div>""", label=L, n=5))
pages.append(page(f"""<div class="k">05 · reels</div><h2>cinematic, honest, short.</h2><div class="cols c2"><div>
 <h3>the language</h3><ul><li>open on a real cooker photo with a slow push-in and steam; the hook in big type.</li><li>the count is the hero: a giant orange 1 → 2 → 3, the real app counting, a full-bleed alarm.</li><li>seams: blur-through on cuts, whips between languages.</li><li>close on the orange card: cooker mark, name, one fact, "link in bio", the handle.</li></ul>
 <h3 style="margin-top:22px">sound</h3><p>a licensed track whose last hit lands on the end card; a recorded kitchen bed (gas, steam, the whistle); calm narration; mastered to -14 LUFS.</p></div>
 <div style="display:flex;gap:16px">{''.join(f'<img class="th" src="{FILE(D[d]["feed"][0])}" style="width:24%">' for d in (2, 3, 4, 6))}</div></div>""", label=L, n=6))
pages.append(page("""<div class="k">06 · voice</div><h2>how we write about #002.</h2><div class="cols c2">
 <div class="card"><h3><span class="tick">✓</span> do</h3><ul><li>lowercase captions, first person "i", short lines.</li><li>the kitchen's own words: dal, rice, whistles, gas, mixie.</li><li>the app's words, as in the app: Start, Learn my whistle, Done, Timer, "Whistles done! Turn off the gas."</li><li>the languages in their own scripts: தமிழ், हिन्दी, తెలుగు, മലയാളം, ಕನ್ನಡ.</li><li>end with a question anyone can answer: "how many whistles for toor dal?"</li></ul></div>
 <div class="card"><h3><span class="cross">✕</span> don't</h3><ul><li>hype words: revolutionary, game-changer, smart ai.</li><li>promise it never misses: say "missed one? tap +1".</li><li>say it works with the screen off: it pauses.</li><li>claim iphone support: it is made for chrome on android.</li><li>put a url in a caption: "link in bio".</li></ul></div></div>""", label=L, n=7))
pages.append(page(f"""<div class="k">07 · product #002</div><h2>Cooker Whistle Counter.</h2>
 <div class="cols c2" style="align-items:center"><div class="card" style="display:flex;align-items:center;gap:40px;padding:50px;background:#1c1816">{cooker(170)}<div style="font:800 76px/0.95 'Bricolage Grotesque';letter-spacing:-.04em;color:#F5EDE4">Cooker Whistle<br>Counter</div></div>
 <div><h3>the one-liner</h3><p style="font-size:30px;color:#161922">it counts the whistles, so you don't have to.</p>
 <h3 style="margin-top:24px">the facts we can always say</h3><p>counts cooker whistles through the mic · alarm and vibration at your number · learns your own cooker's whistle · presets (Toor dal · 3) · backup timer and a separate Timer · six languages: english, தமிழ், हिन्दी, తెలుగు, മലയാളം, ಕನ್ನಡ · no app store, no account, works offline.</p>
 <h3 style="margin-top:24px">the honest small print</h3><p>keep the screen on (counting pauses if it turns off) · phone near the cooker, away from fans · Learn my whistle once per cooker.</p></div></div>""", label=L, n=8))
open(f'{BUILD}/brand.html', 'w').write('<html><head><meta charset="utf-8">' + CSS + '</head><body>' + ''.join(pages) + '</body></html>')

# ======================= playbook =======================
L = 'start here · #002'
pb = [page(f"""<div style="display:flex;flex-direction:column;justify-content:center;height:100%;gap:36px">{mark(130)}
 <h1 style="color:#ECEEF2">the #002 launch.<br>start here.</h1><div style="font:500 28px 'DM Mono';color:{ORL}">{HANDLE} × #002 Cooker Whistle Counter · sat 28 nov – thu 3 dec 2026</div></div>""", 'ink', label=L)]
nst = sum(len(p['stories']) for p in P)
pb.append(page(f"""<div class="k">what's in this kit</div><h2>everything for 6 days, already made.</h2><div class="cols c2"><div>
 <h3>/days</h3><p>one folder per day: <span class="mono">feed/</span> (carousel slides, or a reel mp4 + its cover) and <span class="mono">story/</span> (that day's story frames), plus <span class="mono">caption.txt</span> with the caption, hashtags, alt text, first comment, posting time and which story sticker to add.</p>
 <h3 style="margin-top:24px">/after-launch-library</h3><p>{len(BON)} more finished posts (carousels and single posts), each with its caption.txt, for the days after 3 dec.</p>
 <h3 style="margin-top:24px">/profile</h3><p>profile picture with the orange cursor, highlight covers, bio options.</p></div><div>
 <h3>/brand</h3><p>brand guidelines for #002 (PDF) and logo files.</p>
 <h3 style="margin-top:24px">calendar.pdf · calendar.csv</h3><p>the six days at a glance, then one page per day with thumbnails. the csv has tracking columns.</p>
 <h3 style="margin-top:24px">the totals</h3><p>6 feed posts (4 cinematic reels, 2 carousels) and {nst} story frames: a story every day and a post or reel every day.</p>
 <h3 style="margin-top:24px">/source</h3><p>the generators, if you want to change copy and re-render.</p></div></div>""", label=L, n=2))
pb.append(page(f"""<div class="k">the strategy</div><h2>tease, launch, explain, close.</h2><div class="cols c4" style="gap:26px">
 <div class="card"><div class="k">days 1-2 · sat 28-sun 29</div><h3>tease</h3><p>the morning after #001 closes, turn the page to the kitchen: "one whistle. two. was that three?" then the teaser reel and a countdown to monday.</p></div>
 <div class="card" style="background:{OR}"><div class="k" style="color:#161922">day 3 · mon 30 nov</div><h3>launch</h3><p style="color:#3a2a1e">the launch reel at 7 pm: the real app counting real whistles. link stickers all evening. reply to everything.</p></div>
 <div class="card"><div class="k">days 4-5 · tue 1-wed 2 dec</div><h3>explain</h3><p>day 4: the set-up reel (a minute, once). day 5: everything it does, plus the tips for a perfect count.</p></div>
 <div class="card"><div class="k">day 6 · thu 3 dec</div><h3>close</h3><p>"in your language": six alarms. the most shareable post of the week: people send it home. then thank you, and ask about #003.</p></div></div>
 <p style="margin-top:40px;font-size:24px;color:#161922">why it works: #002 launches three days after #001's week ends, so the followers #001 brought are still warm. sunday lunch is when the cooker is on, so the teaser lands then. two explain days turn "nice" into "installed". the close is built to be forwarded to family, in their own language.</p>""", label=L, n=3))
pb.append(page("""<div class="k">your daily routine · 20 minutes</div><h2>every single day.</h2><div class="cols c2"><div class="card"><table>
 <tr><th>when</th><th>what</th></tr>
 <tr><td class="mono">9:00 am</td><td>story frame 1 (from <span class="mono">story/</span>). add the sticker caption.txt names.</td></tr>
 <tr><td class="mono">1:00 pm</td><td>carousel days (1 and 5): post the slides in order, paste the caption, add alt text.</td></tr>
 <tr><td class="mono">7:00 pm</td><td>reel days (2, 3, 4, 6): upload the mp4, set <span class="mono">cover.png</span> as the cover, paste the caption.</td></tr>
 <tr><td class="mono">+ 1 min</td><td>post the "first comment" from caption.txt.</td></tr>
 <tr><td class="mono">+ 60 min</td><td>reply to every comment. share the post to your story.</td></tr>
 <tr><td class="mono">evening</td><td>the remaining story frames; reshare answers and poll results.</td></tr></table></div>
 <div><h3>how to post each format</h3><ul><li><b>carousel</b>: + → post → select slides in order → caption → advanced → alt text.</li><li><b>reel</b>: + → reel → upload the mp4 → cover → add from camera roll → cover.png → caption. the reels already have their sound: don't add instagram music on top.</li><li><b>story sticker</b>: open the frame → sticker icon → poll / quiz / question / slider / countdown / link → place it in the empty band.</li><li><b>hashtags</b>: at the end of the caption, or in the first comment.</li></ul>
 <h3 style="margin-top:20px">try it on camera</h3><p>if you can, film 10 seconds of your own cooker whistling with the app counting on the counter, and post it as an extra story on day 3 or 4. a real kitchen beats any graphic.</p></div></div>""", label=L, n=4))
bios = ["useful things, built from scratch, for everyday use.\n#002 Cooker Whistle Counter: it counts, you cook ↓",
        "i make weird, useful stuff from scratch.\n#001 Wardrobe · #002 Cooker Whistle Counter ↓",
        "everyday tools, built by hand.\nnew: #002 counts your cooker's whistles ↓"]
pb.append(page(f"""<div class="k">profile · switch it to #002 on sat 28 nov</div><h2>the page turns orange.</h2><div class="cols c2"><div>
 <h3>profile picture</h3><p><span class="mono">profile/profile-picture.png</span>: the same mark, orange cursor. change it on day 1.</p>
 <h3 style="margin-top:22px">bio (pick one)</h3>{''.join(f'<div class="card" style="padding:18px 22px;margin-bottom:12px"><p style="color:#161922">{esc(b)}</p></div>' for b in bios)}</div><div>
 <h3>link</h3><p>until mon 30 nov, 7 pm: keep the Wardrobe link. at launch, switch to the Cooker Whistle Counter link, or use a link page with both (#001 and #002).</p>
 <h3 style="margin-top:22px">highlights</h3><p>add a <b>#002</b> highlight (cover: the cooker) in front of #001's. day 4's frames go to <b>how to</b>, day 5's to <b>faq</b>, day 6's to <b>next</b>. covers are in <span class="mono">profile/highlight-covers/</span>.</p>
 <h3 style="margin-top:22px">pinned posts</h3><p>from day 3: the #002 launch reel, the #002 how-to reel, and #001's launch reel.</p>
 <h3 style="margin-top:22px">reply templates</h3><p><b>install?</b> open the link in chrome → ⋮ → add to home screen.<br><b>it missed one?</b> tap +1, then Learn my whistle again, phone away from fans.<br><b>iphone?</b> it's made for chrome on android; say so honestly.<br><b>is it free?</b> write your answer here before day 3.</p></div></div>""", label=L, n=5))
pb.append(page("""<div class="k">engagement · the part that makes it travel</div><h2>let the kitchen talk.</h2><div class="cols c2"><div>
 <ul><li><b>the whistle-number debate</b>: "how many whistles for toor dal?" gets answers from everyone. reshare the funniest. it's the hook of the whole week.</li><li><b>send it home</b>: day 6 is built to be forwarded to parents and grandparents in their language. ask for it directly.</li><li><b>first hour</b>: reply to every comment with a question back.</li><li><b>every day</b>: 10 real comments on posts in #indiankitchen, #pressurecooker, #cookinghacks, #desikitchen and #buildinpublic.</li><li><b>collabs</b>: from day 3, DM 5 home-cooking or kitchen-hack creators a day with the launch reel; offer them the "for a perfect count" tips for a joint post.</li></ul></div>
 <div><h3>what to measure (sunday 6 dec)</h3><table><tr><th>metric</th><th>what it tells you</th></tr><tr><td>shares</td><td>the #002 signal: kitchen posts travel by being sent.</td></tr><tr><td>saves</td><td>day 4 and 5 should lead here.</td></tr><tr><td>link taps</td><td>how many people try it.</td></tr><tr><td>follows</td><td>did #002 bring new people beyond #001's?</td></tr></table>
 <h3 style="margin-top:22px">after day 6</h3><ul><li>post from /after-launch-library, one every day or two.</li><li>keep a story every day: answers, polls, people's own kitchens.</li><li>alternate #001 and #002 posts so both stay alive.</li></ul></div></div>""", label=L, n=6))
open(f'{BUILD}/playbook.html', 'w').write('<html><head><meta charset="utf-8">' + CSS + '</head><body>' + ''.join(pb) + '</body></html>')

# ======================= calendar =======================
L = 'calendar · #002'
cal = [page("""<div class="k">6 days · sat 28 nov – thu 3 dec 2026</div><h2>the calendar.</h2><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:14px">""" +
  ''.join(f"""<div class="card" style="padding:18px;height:600px;{f'background:{OR}' if p['day'] == 3 else ''}">
   <div class="mono" style="font-size:14px;color:{'#161922' if p['day'] == 3 else '#7C8494'}">day {p['day']:02d} · {p['label']}</div>
   <div style="font:700 22px/1.2 'Bricolage Grotesque';margin-top:10px;height:80px">{esc(p['title'])}</div><img class="th" src="{FILE(p['feed'][0])}" style="width:100%;margin-top:10px">
   <div class="mono" style="font-size:13px;margin-top:6px;color:{'#161922' if p['day'] == 3 else ORD}">{p['kind']} · {p['phase'].split(' · ')[1]} · {len(p['stories'])} stories</div></div>""" for p in P) + '</div>', label=L)]
for p in P:
    imgs = [f for f in p['feed'] if f.endswith('.png')]
    feedrow = ''.join(f'<img class="th" src="{FILE(f)}" style="height:{(140 if len(imgs) > 6 else 185) if p["kind"] in ("carousel", "post") else 280}px">' for f in imgs[:9])
    storyrow = ''.join(f'<img class="th" src="{FILE(f)}" style="height:250px">' for f in p['stories'])
    vid = f'<span class="pill">video: {p["feed"][-1].split("/")[-1]}</span>' if p['kind'] == 'reel' else ''
    cal.append(page(f"""<div style="display:flex;justify-content:space-between;align-items:baseline"><div class="k">day {p['day']:02d} · {p['label']} · phase {p['phase']}</div><div class="mono" style="font-size:18px">{p['folder']}/</div></div>
     <h2 style="font-size:56px;margin-bottom:22px">{esc(p['title'])}</h2>
     <div class="cols" style="grid-template-columns:1.25fr 1fr;gap:40px"><div>
       <div class="k" style="margin-bottom:10px">feed · {p['kind']} · {p['time']}</div><div style="display:flex;gap:10px;flex-wrap:wrap">{feedrow}</div>{vid}
       <div class="k" style="margin:18px 0 10px">stories · {p['story_time']}</div><div style="display:flex;gap:12px">{storyrow}</div></div>
     <div><h3>caption</h3><p style="font-size:16px;color:#161922">{esc(p['caption'])}</p><p class="mono" style="font-size:13px;margin-top:8px">{p['hashtags']}</p>
       <h3 style="margin-top:14px">story stickers</h3><ul>{''.join(f'<li style="font-size:15px">frame {i + 1}: {esc(d)}</li>' for i, d in enumerate(p['story_do']))}</ul>
       <h3 style="margin-top:10px">first comment</h3><p style="font-size:15px">{esc(p['first_comment'])}</p>
       {f'<h3 style="margin-top:10px">highlight</h3><p style="font-size:15px">add today\'s stories to "{p["highlight"]}"</p>' if p['highlight'] else ''}</div></div>""", label=L, n=p['day'] + 1))
cal.append(page('<div class="k">after the launch · from fri 4 dec</div><h2>the library.</h2><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:20px">' +
  ''.join(f'<div><img class="th" src="{FILE(b["feed"][0])}" style="width:100%"><div class="mono" style="font-size:14px;margin-top:8px">{b["folder"].split("/")[-1]}</div></div>' for b in BON) + '</div>', label=L))
open(f'{BUILD}/calendar.html', 'w').write('<html><head><meta charset="utf-8">' + CSS + '</head><body>' + ''.join(cal) + '</body></html>')

# ======================= csv + caption.txt =======================
with open(f'{O}/calendar.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['day', 'date', 'weekday', 'phase', 'feed type', 'title', 'feed time', 'feed files', 'story frames', 'story stickers', 'caption', 'hashtags', 'alt text', 'first comment', 'highlight',
                                  'posted? (y/n)', 'reach', 'saves', 'shares', 'comments', 'link taps', 'follows'])
    for p in P + BON:
        w.writerow([p['day'] if p['date'] else f"library {p['day']:02d}", p['date'] or 'any day from 4 dec', p['label'][:3], p['phase'], p['kind'], p['title'], p['time'], ' | '.join(x.split('/', 1)[1] if p['date'] else x.split('/', 2)[2] for x in p['feed']), len(p['stories']),
                    ' | '.join(p['story_do']), p['caption'], p['hashtags'], p['alt'], p['first_comment'], p['highlight']] + [''] * 7)
for p in P + BON:
    lib = not p['date']
    files = [x.split('/', 2)[2] if lib else x.split('/', 1)[1] for x in p['feed']]
    head = f"AFTER-LAUNCH LIBRARY {p['day']:02d} · post any day from fri 4 dec" if lib else f"DAY {p['day']:02d} · {p['label']} 2026 · {p['phase']}"
    t = [head, p['title'], '', f"FEED: {p['kind']} at {p['time']}", '  files: ' + ', '.join(files),
         *(['  reel: upload the mp4 (it already has its sound), then set cover.png as the cover'] if p['kind'] == 'reel' else ['  post the slides in order'] if p['kind'] == 'carousel' else []),
         '', 'CAPTION (copy from here):', '', p['caption'], '', p['hashtags'], '', 'ALT TEXT:', p['alt'], '', 'FIRST COMMENT (post it yourself right after):', p['first_comment'], '',
         *([f"STORIES: {len(p['stories'])} frame(s), {p['story_time']}", *[f"  story-{i + 1:02d}.png: {d}" for i, d in enumerate(p['story_do'])]] if p['stories'] else ['STORY: share this post to your story with a poll or question about it.']),
         *([f"\nHIGHLIGHT: add today's stories to \"{p['highlight']}\""] if p['highlight'] else [])]
    open(f"{O}/{p['folder']}/caption.txt", 'w').write('\n'.join(t) + '\n')
open(f'{O}/profile/bio-options.txt', 'w').write('NAME FIELD: weird stuff i make\n\nBIO OPTIONS (pick one):\n\n' + '\n\n'.join(bios) +
  '\n\nLINK: keep the Wardrobe link until Mon 30 Nov, 7 pm; then the Cooker Whistle Counter link (or a link page with both).\n\nHIGHLIGHT ORDER: #002 · #001 · how to · faq · next · hello\n')
print('docs written')
