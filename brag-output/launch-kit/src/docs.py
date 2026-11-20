# The kit's documents: brand guidelines, the start-here playbook, the calendar (overview + one page per day),
# calendar.csv and a caption.txt in every day's folder. Pages are 1600x1000 (renders to PDF with pdf.js).
import json, csv, html, os
K = '/home/user/Image-Scanner/brag-output/launch-kit'; O = f'{K}/out'; BUILD = f'{K}/build'
P = json.load(open(f'{BUILD}/plan.json')); BON = json.load(open(f'{BUILD}/bonus.json'))
FILE = lambda p: f'file://{K}/build/thumbs/{p[:-4]}.jpg'
HANDLE = '@wierd_stuff_i_make'
CSS = """
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=DM+Mono:wght@400;500&display=block" rel="stylesheet">
<style>
@page{size:1600px 1000px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;color:#161922;background:#ECEEF2}
.page{width:1600px;height:1000px;padding:80px 96px;position:relative;overflow:hidden;page-break-after:always;background:#ECEEF2}
.page.ink{background:#161922;color:#ECEEF2}.page.acc{background:#3D4FE0;color:#fff}
h1{font:800 120px/0.95 'Bricolage Grotesque';letter-spacing:-.04em}
h2{font:800 72px/1 'Bricolage Grotesque';letter-spacing:-.035em;margin-bottom:34px}
h3{font:700 30px/1.15 'Bricolage Grotesque';letter-spacing:-.02em;margin:0 0 10px}
p,li{font-size:22px;line-height:1.5;color:#3C4150}.ink p,.ink li{color:#c9cdd8}.acc p{color:#e3e8ff}
.k{font:500 20px/1 'DM Mono';color:#3D4FE0;letter-spacing:.01em;margin-bottom:22px}.ink .k{color:#A5BBFF}.acc .k{color:#fff}
.foot{position:absolute;left:96px;right:96px;bottom:40px;display:flex;justify-content:space-between;font:500 16px 'DM Mono';color:#7C8494}
.cols{display:grid;gap:44px}.c2{grid-template-columns:1fr 1fr}.c3{grid-template-columns:1fr 1fr 1fr}.c4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border-radius:22px;padding:28px}.ink .card{background:#22252B}
.sw{height:150px;border-radius:18px;margin-bottom:14px}
.mono{font-family:'DM Mono';font-weight:500}
ul{padding-left:24px}li{margin-bottom:6px}
.pill{display:inline-block;font:500 16px 'DM Mono';padding:7px 14px;border-radius:999px;background:#fff;margin:0 6px 6px 0}
.do{border-left:0;}.tick{color:#14906d;font-weight:700}.cross{color:#d2413a;font-weight:700}
table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:9px 10px;border-bottom:1px solid #DFE2E8;font-size:16px;vertical-align:top}th{font:500 14px 'DM Mono';color:#7C8494}
img.th{border-radius:10px;box-shadow:0 10px 24px -14px rgba(22,25,34,.4)}
</style>"""
def page(inner, cls='', n=None, total=None, label=''):
    foot = f'<div class="foot"><span>{HANDLE}</span><span>{label}{" · " + str(n) if n else ""}</span></div>'
    return f'<div class="page {cls}">{inner}{foot}</div>'
def esc(s): return html.escape(s).replace('\n', '<br>')

# ======================= brand guidelines =======================
mark = lambda size, cursor='#3D4FE0', bg='#161922', fg='#ECEEF2': f"""<div style="width:{size}px;height:{size}px;border-radius:22%;background:{bg};display:grid;place-items:center">
 <div style="position:relative;font:800 {size*0.62}px/1 'Bricolage Grotesque';letter-spacing:-.04em;color:{fg};transform:translate(-{size*0.06}px,-{size*0.06}px)">w<span style="position:absolute;left:100%;bottom:{size*0.04}px;margin-left:{size*0.05}px;width:{size*0.2}px;height:{size*0.07}px;border-radius:{size*0.02}px;background:{cursor}"></span></div></div>"""
word = lambda size, color='#161922', cur='#3D4FE0': f"""<span style="font:500 {size}px/1 'DM Mono';letter-spacing:-.02em;color:{color}">wierd_stuff_i_make<span style="display:inline-block;width:{size*0.5}px;height:{size*0.12}px;background:{cur};margin-left:{size*0.08}px;border-radius:2px"></span></span>"""
hanger = lambda size, color='#3D4FE0': f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7.5V6a2 2 0 1 0-2-2"/><path d="M12 7.5 3.5 14a1.5 1.5 0 0 0 .9 2.7h15.2a1.5 1.5 0 0 0 .9-2.7z"/></svg>'
L = 'brand guidelines'
pages = []
pages.append(page(f"""<div style="display:flex;flex-direction:column;justify-content:center;height:100%;gap:40px">{mark(150)}
  <h1 style="color:#ECEEF2">brand<br>guidelines.</h1><div style="font:500 30px 'DM Mono';color:#A5BBFF">{HANDLE} · launching product #001: Wardrobe</div></div>""", 'ink', label=L))
pages.append(page("""<div class="k">01 · who we are</div><h2>useful things, built from scratch, for everyday use.</h2>
 <div class="cols c3" style="margin-top:50px">
 <div class="card"><h3>what the page is</h3><p>a maker's page. every product starts as a blank file and ends as a tool someone uses every day. Wardrobe is the first: #001.</p></div>
 <div class="card"><h3>the three rules</h3><p>1. it fixes one small, everyday problem.<br>2. you can just open it and use it.<br>3. it's built from scratch, start to finish.</p></div>
 <div class="card"><h3>the feeling</h3><p>honest, curious, a little weird, never loud. we show the real thing working, not a promise about it.</p></div></div>
 <div class="cols c2" style="margin-top:44px"><div><h3>positioning line</h3><p style="font-size:30px;color:#161922">useful things, built from scratch, for everyday use.</p></div>
 <div><h3>the series</h3><p>every product gets a number: <span class="mono">#001 Wardrobe</span>, <span class="mono">#002 …</span>. the number is part of the name on the page, in tags and covers.</p></div></div>""", label=L, n=2))
pages.append(page(f"""<div class="k">02 · the page mark</div><h2>w, with a cursor.</h2>
 <div class="cols c3" style="align-items:center;margin-top:30px"><div style="display:grid;place-items:center">{mark(300)}</div>
 <div style="display:grid;place-items:center">{mark(300, '#ECEEF2')}</div><div style="display:grid;place-items:center">{mark(300, '#161922', '#ECEEF2', '#161922')}</div></div>
 <div class="cols c3" style="margin-top:28px"><p>primary: ink tile, paper "w", the cursor in the colour of the product being launched (Wardrobe indigo now).</p>
 <p>between launches: the cursor goes paper. the page is ink on paper; products bring the colour.</p><p>on dark photos or ink grounds: the reversed tile. keep clear space of one cursor width all round.</p></div>""", label=L, n=3))
pages.append(page(f"""<div class="k">03 · the wordmark</div><h2>the handle is the wordmark.</h2>
 <div class="card" style="padding:60px;margin-top:20px">{word(64)}</div><div class="card" style="padding:60px;margin-top:24px;background:#161922">{word(64, '#ECEEF2', '#A5BBFF')}</div>
 <div class="cols c3" style="margin-top:40px"><p>set in DM Mono 500, lowercase, exactly as the handle is spelled: <b>wierd</b>_stuff_i_make. never correct it to "weird" in the wordmark.</p>
 <p>the trailing cursor bar takes the product colour. on ink it uses the lifted accent (#A5BBFF).</p><p>in the instagram name field use "weird stuff i make" so people who search the usual spelling find you.</p></div>""", label=L, n=4))
sw = lambda c, n, h, note: f'<div><div class="sw" style="background:{c};{"border:2px solid #DFE2E8" if c in ("#FFFFFF", "#ECEEF2") else ""}"></div><h3>{n}</h3><div class="mono" style="font-size:18px;color:#7C8494">{h}</div><p style="font-size:18px">{note}</p></div>'
pages.append(page(f"""<div class="k">04 · colour</div><h2>ink on paper. products bring the colour.</h2>
 <div class="cols c4" style="gap:28px">{sw('#161922', 'ink', '#161922', 'type, the page mark, dark slides.')}{sw('#ECEEF2', 'paper', '#ECEEF2', 'the ground of every post and story.')}{sw('#FFFFFF', 'white', '#FFFFFF', 'cards, item tiles, UI surfaces.')}{sw('#7C8494', 'grey', '#7C8494', 'handles, counters, secondary text.')}</div>
 <div class="cols c4" style="gap:28px;margin-top:30px">{sw('#3C4150', 'ink 2', '#3C4150', 'sub-lines on paper.')}{sw('#DFE2E8', 'line', '#DFE2E8', 'dividers in lists.')}{sw('#3D4FE0', '#001 Wardrobe indigo', '#3D4FE0', 'the product accent: one word per line at most, CTAs, the cursor.')}{sw('#A5BBFF', 'indigo, lifted', '#A5BBFF', 'the accent on ink.')}</div>""", label=L, n=5))
pages.append(page("""<div class="k">05 · type</div><h2>one display face, one text face, one mono.</h2>
 <div class="cols c3" style="margin-top:20px">
 <div class="card"><div style="font:800 96px/1 'Bricolage Grotesque';letter-spacing:-.04em">Aa</div><h3 style="margin-top:20px">Bricolage Grotesque 800</h3><p>headlines. tight (-3.5%), lowercase on the page, big: 84-130 px on a 1080 canvas. never under 64 px.</p></div>
 <div class="card"><div style="font:500 96px/1 'DM Sans'">Aa</div><h3 style="margin-top:20px">DM Sans 500</h3><p>sub-lines and body: 36-46 px on posts, 42-46 px on stories. the same face the Wardrobe app uses.</p></div>
 <div class="card"><div style="font:500 96px/1 'DM Mono'">Aa</div><h3 style="margin-top:20px">DM Mono 500</h3><p>the maker's voice: the handle, kickers ("rule 01", "build log"), numbers, counters, tags.</p></div></div>
 <p style="margin-top:36px">all three are free Google Fonts (OFL). install them for editing: fonts.google.com → Bricolage Grotesque, DM Sans, DM Mono.</p>""", label=L, n=6))
pages.append(page(f"""<div class="k">06 · layout</div><h2>the grid, the safe zones, the chrome.</h2>
 <div class="cols c3" style="gap:40px;align-items:start">
 <div><img class="th" src="{FILE('Day04_Tue-24-Nov/feed/slide-02.png')}" style="width:100%"><h3 style="margin-top:16px">feed 4:5 · 1080×1350</h3><p>72 px margins. handle top-left, product tag top-right, counter bottom-right, "swipe →" on slide 1.</p></div>
 <div><img class="th" src="{FILE('Day04_Tue-24-Nov/story/story-01.png')}" style="width:62%"><h3 style="margin-top:16px">story 9:16 · 1080×1920</h3><p>keep text between y 250 and 1640. the empty middle/lower band is where the day's sticker goes.</p></div>
 <div><img class="th" src="{FILE('Day07_Fri-27-Nov/feed/cover.png')}" style="width:62%"><h3 style="margin-top:16px">reel cover · 1080×1920</h3><p>title centred, inside the 1080×1350 middle so the grid crop keeps it.</p></div></div>""", label=L, n=7))
pages.append(page(f"""<div class="k">07 · imagery</div><h2>real things, cut out. real screens, in a phone.</h2>
 <div class="cols c2" style="align-items:start"><div><img class="th" src="{FILE('after-launch-library/13_post_before-after/feed/post-01.png')}" style="width:62%"></div>
 <div><h3>cut-outs</h3><p>clothes are real photos cut out by Wardrobe's own Smart AI, floating on paper with a soft shadow. no drawn clothes, no stock models.</p>
 <h3 style="margin-top:28px">screens</h3><p>always the real app, inside the dark phone frame. never mock up a screen that doesn't exist.</p>
 <h3 style="margin-top:28px">people</h3><p>hands and real moments only (photographing clothes, packing). no stock gestures.</p>
 <h3 style="margin-top:28px">never</h3><p>gradients as a style, neon, emoji in graphics, fake numbers, before/after that isn't real.</p></div></div>""", label=L, n=8))
pages.append(page(f"""<div class="k">08 · product #001</div><h2>Wardrobe.</h2>
 <div class="cols c2" style="align-items:center"><div class="card" style="display:flex;align-items:center;gap:40px;padding:60px">{hanger(180)}<div style="font:800 110px/1 'Bricolage Grotesque';letter-spacing:-.04em">Wardrobe</div></div>
 <div><h3>the mark</h3><p>the app's own hanger, outline, in indigo (or white on indigo). the name is always capitalised: Wardrobe.</p>
 <h3 style="margin-top:26px">the one-liner</h3><p style="font-size:28px;color:#161922">your whole closet, on your phone.</p>
 <h3 style="margin-top:26px">the facts we can always say</h3><p>one html file · no app store · no account · photos stay on your device · the ai runs on your phone · backup is one file.</p></div></div>""", label=L, n=9))
pages.append(page("""<div class="k">09 · voice</div><h2>how we write.</h2><div class="cols c2">
 <div class="card"><h3><span class="tick">✓</span> do</h3><ul><li>lowercase captions, first person "i". short lines.</li><li>say what it does, plainly: "the background disappears."</li><li>the app's own words, capitalised as in the app: Style me, Mark as worn, Try on.</li><li>end with one question people can answer in a word.</li><li>one or two emoji in a caption at most; none in graphics.</li></ul></div>
 <div class="card"><h3><span class="cross">✕</span> don't</h3><ul><li>hype words: revolutionary, game-changer, unleash, seamless, magic.</li><li>made-up numbers ("10,000 users!"). only real ones.</li><li>promises about features that don't exist.</li><li>"link in bio" plus a URL in the caption (instagram doesn't link it).</li><li>correcting the handle's spelling.</li></ul></div></div>""", label=L, n=10))
pages.append(page(f"""<div class="k">10 · templates in use</div><h2>the system, at a glance.</h2><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:18px">
 {''.join(f'<img class="th" src="{FILE(p)}" style="width:100%">' for p in ['Day01_Sat-21-Nov/feed/slide-01.png','Day01_Sat-21-Nov/feed/slide-02.png','Day04_Tue-24-Nov/feed/slide-01.png','Day04_Tue-24-Nov/feed/slide-02.png','Day06_Thu-26-Nov/feed/slide-03.png','after-launch-library/06_carousel_cost-per-wear/feed/slide-01.png','after-launch-library/10_carousel_build-log/feed/slide-02.png','after-launch-library/04_carousel_capsule-101/feed/slide-01.png','after-launch-library/14_post_dark-mode/feed/post-01.png','after-launch-library/15_post_10-piece-challenge/feed/post-01.png','after-launch-library/12_carousel_holiday-outfits/feed/slide-02.png','Day04_Tue-24-Nov/feed/slide-09.png'])}</div>""", label=L, n=11))
open(f'{BUILD}/brand.html', 'w').write('<html><head><meta charset="utf-8">' + CSS + '</head><body>' + ''.join(pages) + '</body></html>')

# ======================= playbook =======================
L = 'start here'
pb = []
pb.append(page(f"""<div style="display:flex;flex-direction:column;justify-content:center;height:100%;gap:36px">{mark(130)}
 <h1 style="color:#ECEEF2">the 7-day launch.<br>start here.</h1><div style="font:500 28px 'DM Mono';color:#A5BBFF">{HANDLE} × #001 Wardrobe · sat 21 nov – fri 27 nov 2026</div></div>""", 'ink', label=L))
pb.append(page("""<div class="k">what's in this kit</div><h2>everything for 7 days, already made.</h2><div class="cols c2"><div>
 <h3>/days</h3><p>one folder per day (7): <span class="mono">feed/</span> (carousel slides, a single post, or a reel + its cover) and <span class="mono">story/</span> (that day's story frames), plus <span class="mono">caption.txt</span> with the caption, hashtags, alt text, first comment, posting time and exactly which story sticker to add.</p>
 <h3 style="margin-top:24px">/after-launch-library</h3><p>16 more finished posts (7 reels, 6 carousels, 3 single posts), each with its caption.txt, ready from day 8.</p><h3 style="margin-top:24px">/profile</h3><p>profile picture, 7 highlight covers, bio options.</p>
 <h3 style="margin-top:24px">/brand</h3><p>brand guidelines (PDF) and logo files.</p></div><div>
 <h3>calendar.pdf · calendar.csv</h3><p>the whole week at a glance, then one page per day with thumbnails. the csv opens in Sheets or Excel for tracking.</p>
 <h3 style="margin-top:24px">the totals</h3><p>7 feed posts (4 reels, 3 carousels) and 18 story frames: stories every day, a post or reel every day. plus 16 library posts for after the launch.</p>
 <h3 style="margin-top:24px">/source</h3><p>the generators, if you want to change copy and re-render.</p></div></div>""", label=L, n=2))
pb.append(page("""<div class="k">the strategy</div><h2>tease, launch, explain, close.</h2><div class="cols c4" style="gap:26px">
 <div class="card"><div class="k">days 1-2 · sat 21-sun 22</div><h3>tease</h3><p>introduce the page and its three rules. tease #001 without naming it: "nothing to wear?", a cut-out teaser, a countdown to monday.</p></div>
 <div class="card" style="background:#3D4FE0;color:#fff"><div class="k" style="color:#fff">day 3 · mon 23 nov</div><h3>launch</h3><p style="color:#e3e8ff">the launch film at 7 pm. stories with the link all evening. reply to everything.</p></div>
 <div class="card"><div class="k">days 4-6 · tue 24-thu 26</div><h3>explain</h3><p>every feature in one carousel, how to add clothes, the faq. the "how" turns curious people into users.</p></div>
 <div class="card"><div class="k">day 7 · fri 27 nov</div><h3>close on black friday</h3><p>"shop your own closet first" with Try on and Style me, a thank-you, and the first question about #002.</p></div></div>
 <p style="margin-top:40px;font-size:24px;color:#161922">why it works: two days of curiosity before anything is sold, a launch early in the week so it has room to travel, three days that answer "how", and a close on the one day everyone is thinking about buying clothes. then the library keeps the page busy for weeks.</p>""", label=L, n=3))
pb.append(page("""<div class="k">your daily routine · 20 minutes</div><h2>every single day.</h2><div class="cols c2"><div class="card"><table>
 <tr><th>when</th><th>what</th></tr>
 <tr><td class="mono">9:00 am</td><td>story frame 1 (from <span class="mono">story/</span>). add the sticker the caption.txt names.</td></tr>
 <tr><td class="mono">1:00 pm</td><td>carousel or single post days: post the <span class="mono">feed/</span> images in order, paste the caption, add alt text.</td></tr>
 <tr><td class="mono">7:00 pm</td><td>reel days: upload the mp4, set <span class="mono">cover.png</span> as the cover, paste the caption.</td></tr>
 <tr><td class="mono">+ 1 min</td><td>post the "first comment" from caption.txt under your post.</td></tr>
 <tr><td class="mono">+ 60 min</td><td>reply to every comment. share the new post to your story.</td></tr>
 <tr><td class="mono">evening</td><td>remaining story frames; reshare replies and poll results.</td></tr></table></div>
 <div><h3>how to post each format</h3><ul><li><b>carousel</b>: + → post → select slides in order (slide-01 first) → caption → advanced → alt text.</li><li><b>reel</b>: + → reel → upload the mp4 → cover → "add from camera roll" → cover.png → caption.</li><li><b>story sticker</b>: open the frame → sticker icon → poll / quiz / question / slider / countdown / link → place it in the empty band.</li><li><b>hashtags</b>: paste them at the end of the caption (or in the first comment if you prefer clean captions).</li></ul>
 <h3 style="margin-top:20px">posting times</h3><p>the times assume your audience is mostly in your time zone. after week 1, check insights → "most active times" and shift.</p></div></div>""", label=L, n=4))
bios = ["useful things, built from scratch, for everyday use.\n#001 Wardrobe: your closet on your phone ↓",
        "i make weird, useful stuff from scratch.\nnew: #001 Wardrobe. no app store, no account ↓",
        "everyday tools, built by hand.\n#001 Wardrobe is live ↓"]
pb.append(page(f"""<div class="k">profile setup · do this before day 1</div><h2>make the profile ready for strangers.</h2><div class="cols c2"><div>
 <h3>name field</h3><p class="mono" style="color:#161922">weird stuff i make</p><p>(instagram search reads the name field: this way "weird" finds you too.)</p>
 <h3 style="margin-top:22px">bio (pick one)</h3>{''.join(f'<div class="card" style="padding:18px 22px;margin-bottom:12px"><p style="color:#161922">{esc(b)}</p></div>' for b in bios)}
 <h3 style="margin-top:12px">link</h3><p>the Wardrobe link. until 23 nov, link to a "coming 23.11" page or leave it empty.</p></div><div>
 <h3>profile picture</h3><p><span class="mono">profile/profile-picture.png</span> (indigo cursor) during the launch; the mono version between launches.</p>
 <h3 style="margin-top:22px">highlights (in this order)</h3><p>#001 · how to · faq · next · hello (build log and you are ready for later). covers are in <span class="mono">profile/highlight-covers/</span>; caption.txt says which story goes where.</p>
 <h3 style="margin-top:22px">pinned posts</h3><p>until day 3: the day 1 intro. from day 3: the launch reel and the day 4 "every feature" carousel; later, the full tour from the library.</p>
 <h3 style="margin-top:22px">account</h3><p>switch to a creator or business account so you get insights and the link sticker on stories.</p></div></div>""", label=L, n=5))
pb.append(page("""<div class="k">engagement · the part that makes it massive</div><h2>show up in the comments.</h2><div class="cols c2"><div>
 <ul><li><b>first hour</b>: reply to every comment, with a question back. comments with replies count twice.</li><li><b>every day</b>: spend 10 minutes commenting (properly, not "nice!") on 10 posts in #capsulewardrobe, #outfitideas, #closetorganization and #buildinpublic.</li><li><b>stories</b>: reshare poll results and answer question-box replies. people who see their answer come back.</li><li><b>ugc</b>: repost every outfit board or closet that tags you (ask first in DMs).</li><li><b>collabs</b>: from day 3, DM 5 small fashion / organisation / maker creators a day with the before/after cut-out and offer a collab post on the capsule or 10-piece challenge.</li><li><b>dms</b>: answer every DM the same day; save good questions for the FAQ.</li></ul></div>
 <div><h3>reply templates</h3>
 <div class="card" style="margin-bottom:12px;padding:20px"><p><b>how do i install it?</b> it's one html file. open the link → iphone: share → "add to home screen". android: ⋮ → "add to home screen". then it opens like an app.</p></div>
 <div class="card" style="margin-bottom:12px;padding:20px"><p><b>where's my data?</b> on your device only. no account, no server. use settings → download backup to keep a copy.</p></div>
 <div class="card" style="margin-bottom:12px;padding:20px"><p><b>does it work on a laptop?</b> yes, it's a web page. your phone is the best for photos.</p></div>
 <div class="card" style="padding:20px"><p><b>is it free?</b> write your answer here before day 3 so every reply says the same thing.</p></div></div></div>""", label=L, n=6))
pb.append(page("""<div class="k">measure · every sunday, 10 minutes</div><h2>what to track, and what to do about it.</h2><div class="cols c2"><div class="card"><table>
 <tr><th>metric</th><th>where</th><th>what it tells you</th></tr>
 <tr><td>reach & views</td><td>insights → overview</td><td>is the content travelling beyond followers?</td></tr>
 <tr><td>saves & shares</td><td>each post</td><td>the strongest signal: make more of whatever gets saved.</td></tr>
 <tr><td>profile visits</td><td>insights</td><td>are hooks working? visits without follows = fix the bio.</td></tr>
 <tr><td>link taps</td><td>insights → profile activity</td><td>how many people try Wardrobe.</td></tr>
 <tr><td>follows</td><td>insights</td><td>the page's growth.</td></tr>
 <tr><td>story taps-forward</td><td>each story</td><td>high = too many frames or a weak frame 1.</td></tr></table>
 <p style="margin-top:14px">log the numbers each sunday in calendar.csv (columns are ready).</p></div>
 <div><h3>if something flops</h3><ul><li>a reel under your average after 24 h: re-post the same video 7 days later with a new first-second hook and cover.</li><li>a carousel with low saves: turn its best slide into a single post.</li><li>polls with few taps: ask easier, funnier questions.</li></ul>
 <h3 style="margin-top:22px">after day 7</h3><ul><li>post from /after-launch-library: one a day for two weeks, or 3-4 a week. alternate a reel and a carousel.</li><li>keep a story every day: reshare replies, polls and ugc.</li><li>run the 10-piece challenge (library 15) in week 3.</li><li>start the #002 build log once you've picked it.</li></ul></div></div>""", label=L, n=7))
open(f'{BUILD}/playbook.html', 'w').write('<html><head><meta charset="utf-8">' + CSS + '</head><body>' + ''.join(pb) + '</body></html>')

# ======================= calendar =======================
L = 'calendar'
KIND = {'reel': 'reel', 'carousel': 'carousel', 'post': 'post', 'video': 'video'}
cal = [page("""<div class="k">7 days · sat 21 – fri 27 nov 2026</div><h2>the calendar.</h2><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:12px">""" +
  ''.join(f"""<div class="card" style="padding:18px 18px;height:560px;{'background:#3D4FE0;color:#fff' if p['day'] == 3 else ''}">
   <div class="mono" style="font-size:14px;color:{'#fff' if p['day'] == 3 else '#7C8494'}">day {p['day']:02d} · {p['label']}</div>
   <div style="font:700 22px/1.2 'Bricolage Grotesque';margin-top:10px">{esc(p['title'])}</div><img class="th" src="{FILE(p['feed'][0])}" style="width:100%;margin-top:14px">
   <div class="mono" style="font-size:13px;margin-top:6px;color:{'#e3e8ff' if p['day'] == 3 else '#3D4FE0'}">{KIND[p['kind']]} · {len(p['stories'])} story</div></div>""" for p in P) + '</div>', label=L)]
for p in P:
    imgs = [f for f in p['feed'] if f.endswith('.png')]
    feedrow = ''.join(f'<img class="th" src="{FILE(f)}" style="height:{(140 if len(imgs) > 6 else 185) if p["kind"] in ("carousel", "post") else 280}px">' for f in imgs[:9])
    storyrow = ''.join(f'<img class="th" src="{FILE(f)}" style="height:250px">' for f in p['stories'])
    vid = f'<span class="pill">video: {p["feed"][-1].split("/")[-1]}</span>' if p['kind'] in ('reel', 'video') else ''
    cal.append(page(f"""<div style="display:flex;justify-content:space-between;align-items:baseline"><div class="k">day {p['day']:02d} · {p['label']} · phase {p['phase']}</div><div class="mono" style="font-size:18px">{p['folder']}/</div></div>
     <h2 style="font-size:56px;margin-bottom:22px">{esc(p['title'])}</h2>
     <div class="cols" style="grid-template-columns:1.25fr 1fr;gap:40px"><div>
       <div class="k" style="margin-bottom:10px">feed · {p['kind']} · {p['time']}</div><div style="display:flex;gap:10px;flex-wrap:wrap">{feedrow}</div>{vid}
       <div class="k" style="margin:18px 0 10px">stories · {p['story_time']}</div><div style="display:flex;gap:12px">{storyrow}</div></div>
     <div><h3>caption</h3><p style="font-size:17px;color:#161922">{esc(p['caption'])}</p><p class="mono" style="font-size:14px;margin-top:8px">{p['hashtags']}</p>
       <h3 style="margin-top:16px">story stickers</h3><ul>{''.join(f'<li style="font-size:16px">frame {i + 1}: {esc(d)}</li>' for i, d in enumerate(p['story_do']))}</ul>
       <h3 style="margin-top:12px">first comment</h3><p style="font-size:16px">{esc(p['first_comment'])}</p>
       {f'<h3 style="margin-top:12px">highlight</h3><p style="font-size:16px">add today\'s stories to "{p["highlight"]}"</p>' if p['highlight'] else ''}</div></div>""", label=L, n=p['day'] + 1))
cal.append(page('<div class="k">after the launch · ready from day 8</div><h2>the library.</h2><div style="display:grid;grid-template-columns:repeat(8,1fr);gap:14px">' +
  ''.join(f'<div><img class="th" src="{FILE(b["feed"][0])}" style="width:100%"><div class="mono" style="font-size:13px;margin-top:6px">{b["folder"].split("/")[-1]}</div></div>' for b in BON) + '</div>', label=L))
open(f'{BUILD}/calendar.html', 'w').write('<html><head><meta charset="utf-8">' + CSS + '</head><body>' + ''.join(cal) + '</body></html>')

# ======================= csv + caption.txt =======================
with open(f'{O}/calendar.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['day', 'date', 'weekday', 'phase', 'feed type', 'title', 'feed time', 'feed files', 'story frames', 'story stickers', 'caption', 'hashtags', 'alt text', 'first comment', 'highlight',
                                  'posted? (y/n)', 'reach', 'saves', 'shares', 'comments', 'link taps', 'follows'])
    for p in P + BON:
        w.writerow([p['day'] if p['date'] else f"library {p['day']:02d}", p['date'] or 'any day from day 8', p['label'][:3], p['phase'], p['kind'], p['title'], p['time'], ' | '.join(x.split('/', 1)[1] if p['date'] else x.split('/', 2)[2] for x in p['feed']), len(p['stories']),
                    ' | '.join(p['story_do']), p['caption'], p['hashtags'], p['alt'], p['first_comment'], p['highlight']] + [''] * 7)
for p in P + BON:
    lib = not p['date']
    files = [x.split('/', 2)[2] if lib else x.split('/', 1)[1] for x in p['feed']]
    head = f"AFTER-LAUNCH LIBRARY {p['day']:02d} · post any day from day 8" if lib else f"DAY {p['day']:02d} · {p['label']} 2026 · {p['phase']}"
    t = [head, p['title'], '', f"FEED: {p['kind']} at {p['time']}", '  files: ' + ', '.join(files),
         *(['  reel: upload the mp4, then set cover.png as the cover'] if p['kind'] in ('reel', 'video') else ['  post the slides in order'] if p['kind'] == 'carousel' else []),
         '', 'CAPTION (copy from here):', '', p['caption'], '', p['hashtags'], '', 'ALT TEXT:', p['alt'], '', 'FIRST COMMENT (post it yourself right after):', p['first_comment'], '',
         *([f"STORIES: {len(p['stories'])} frame(s), {p['story_time']}", *[f"  story-{i + 1:02d}.png: {d}" for i, d in enumerate(p['story_do'])]] if p['stories'] else ['STORY: share this post to your story with a poll or question about it.']),
         *([f"\nHIGHLIGHT: add today's stories to \"{p['highlight']}\""] if p['highlight'] else [])]
    open(f"{O}/{p['folder']}/caption.txt", 'w').write('\n'.join(t) + '\n')
open(f'{O}/profile/bio-options.txt', 'w').write('NAME FIELD: weird stuff i make\n\nBIO OPTIONS (pick one):\n\n' + '\n\n'.join(bios) + '\n\nLINK: the Wardrobe link (from day 3, Mon 23 Nov).\n\nHIGHLIGHT ORDER: #001 · how to · faq · next · hello\n')
print('docs written')
