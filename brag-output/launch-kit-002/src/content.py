# The 6-day launch of product #002, Cooker Whistle Counter, on @wierd_stuff_i_make.
# Tease (Sat 28, Sun 29 Nov) · launch (Mon 30 Nov) · explain (Tue 1, Wed 2 Dec) · close (Thu 3 Dec).
# Writes build/assets.json (every image to render), build/plan.json (the calendar) and build/bonus.json (the library).
import json, datetime, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'build'); os.makedirs(OUT, exist_ok=True)
START = datetime.date(2026, 11, 28)
CORE = '#wierdstuffimake #pressurecooker #indiankitchen #cookinghacks #kitchentips #homecooking'
TAGS = {
    'teaser': '#wierdstuffimake #pressurecooker #cookerwhistle #indiankitchen #desikitchen #comingsoon #madefromscratch',
    'launch': CORE + ' #cookerwhistle #newapp #desikitchen #indianfood #madefromscratch',
    'explain': CORE + ' #cookerwhistle #howto #kitchenhacks #dalrice #indianfood',
    'close': CORE + ' #tamil #hindi #telugu #malayalam #kannada #desikitchen',
    'build': '#wierdstuffimake #buildinpublic #indiemaker #webdev #madefromscratch #everydaytools',
}
TIMES = {'reel': '7:00 pm', 'carousel': '1:00 pm', 'post': '1:00 pm'}
STORY_TIME = '9:00 am (frame 1), the rest spread through the day'
LANGS = ['English', 'தமிழ்', 'हिन्दी', 'తెలుగు', 'മലയാളം', 'ಕನ್ನಡ']
def day(n): d = START + datetime.timedelta(days=n - 1); return d, d.strftime('%a %d %b')
assets, plan = [], []
def A(path, spec, W, H): assets.append({'out': path, 'W': W, 'H': H, **spec})
def slides(items, tag=None):
    out = []
    for i, s in enumerate(items):
        s = dict(s); s.setdefault('counter', f'{i + 1:02d}/{len(items):02d}')
        if i == 0: s.setdefault('swipe', True)
        if tag: s.setdefault('tag', tag)
        out.append(s)
    return out

W = {}
# ================= day 1 · Sat 28 Nov · tease =================
W[1] = dict(phase='1 · tease', kind='carousel', theme='teaser', title='#002: the kitchen problem',
  feed=slides([
    {'t': 'hook', 'photo': 'cooker1', 'kicker': 'product #002', 'title': 'one whistle.<br>two.<br>was that three?', 'size': 124},
    {'t': 'hook', 'kicker': '01', 'title': 'you stand by the stove, counting.', 'sub': 'because if you walk away, you lose count.'},
    {'t': 'hook', 'kicker': '02', 'title': 'the mixie drowns one out.', 'sub': 'or the doorbell. or the phone. or the kids.'},
    {'t': 'hook', 'kicker': '03', 'title': 'one too many and the dal turns to paste.', 'sub': 'one too few and the rice is still hard.'},
    {'t': 'hook', 'bg': 'ink', 'title': 'so i built something that listens.'},
    {'t': 'hook', 'photo': 'flame2', 'kicker': 'product #002', 'title': 'monday,<br>30 november.', 'sub': 'follow so you see it first.', 'size': 130}], tag='#002 · soon'),
  caption="#001 was for your closet. #002 is for your kitchen.\n\nevery home with a pressure cooker knows this one. one whistle. two. was that three? you either stand by the stove counting, or you walk away and lose count.\n\nso i built something that listens.\n\nmonday, 30 november, 7 pm.",
  alt='Six slides: a pressure cooker on a gas stove, the problem of counting cooker whistles, and product #002 landing Monday 30 November.',
  first_comment='how many whistles for toor dal in your house? (this decides arguments)',
  stories=[
    {'t': 's_hook', 'photo': 'cooker1', 'title': '#002 is for your kitchen.', 'sub': 'guess what it does.', 'sticker': 'quiz sticker', 'tag': '#002 · soon',
     'do': 'Add a QUIZ sticker: "what does #002 do?" "counts cooker whistles" (correct) / "finds your keys" / "orders dinner".'},
    {'t': 's_hook', 'title': 'how do you count cooker whistles?', 'sticker': 'poll sticker', 'tag': 'poll',
     'do': 'Add a POLL: "i stand there and count" / "i guess 🙃".'},
    {'t': 's_countdown', 'big': '2', 'title': 'days to #002', 'sticker': 'countdown sticker',
     'do': 'Add a COUNTDOWN sticker named "product #002" ending Mon 30 Nov, 7:00 pm, so people can tap "remind me".'}])
# ================= day 2 · Sun 29 Nov · tease reel =================
W[2] = dict(phase='1 · tease', kind='reel', theme='teaser', title='teaser: who is counting the whistles?', reel='teaser',
  cover={'t': 'cover', 'photo': 'cooker1', 'title': "who's counting the whistles?", 'kicker': '#002 · 30.11', 'size': 124},
  caption="sunday lunch. the cooker's on. who's counting the whistles?\n\nfrom tomorrow, not you.\n\nproduct #002. monday 30.11, 7 pm. 🔔",
  alt='A pressure cooker on a gas stove with steam, a giant orange count going 1, 2, 3 over a blue gas flame as the cooker whistles, then a card: product #002, Monday 30.11.',
  first_comment='guess what #002 is. closest guess gets a shout-out tomorrow.',
  stories=[
    {'t': 's_hook', 'photo': 'flame2', 'title': 'tomorrow, 7 pm.', 'sub': 'it listens.', 'tag': '#002 · soon', 'center': True,
     'do': 'Share today\'s reel on top of this frame (paper-plane icon → add to story), or use this frame alone with a LINK sticker to the reel.'},
    {'t': 's_hook', 'title': 'how many whistles for rice?', 'sticker': 'question box', 'tag': 'question',
     'do': 'Add a QUESTION sticker: "rice in my house is __ whistles". Reshare the funniest answers tonight.'},
    {'t': 's_countdown', 'big': '1', 'title': 'day to #002', 'sticker': 'countdown sticker',
     'do': 'Re-add the "product #002" COUNTDOWN sticker.'}])
# ================= day 3 · Mon 30 Nov · launch =================
W[3] = dict(phase='2 · launch', kind='reel', theme='launch', title='launch: Cooker Whistle Counter', reel='launch',
  cover={'t': 'cover', 'title': 'it counts the whistles<br>for you.', 'kicker': '#002 · cooker whistle counter', 'screen': 'run/r0220', 'size': 104},
  caption="product #002 is here: Cooker Whistle Counter.\n\ntap start and it listens. it counts every whistle, so you don't have to, and when it's done it tells you: an alarm, a vibration, and \"whistles done! turn off the gas.\"\n\nit learns your own cooker's whistle, and it speaks your language: english, தமிழ், हिन्दी, తెలుగు, മലയാളം, ಕನ್ನಡ.\n\nno app store. no account. works offline. one link. link in bio.",
  alt='Launch reel: a cooker on a stove, the Cooker Whistle Counter app on a phone counting real whistles from 0 to 3, the "Whistles done! Turn off the gas." alarm, the Learn my whistle step, and the alarm in five Indian languages.',
  first_comment='tell me your dal + rice whistle numbers, i\'ll turn the most common ones into presets ideas 👇',
  stories=[
    {'t': 's_phone', 'title': '#002 is live.', 'sub': 'Cooker Whistle Counter.', 'screen': 'idle', 'tag': 'new',
     'do': 'Add a LINK sticker to the app (your bio link) over the lower part of the frame. Post at 7 pm with the reel.'},
    {'t': 's_phone', 'title': 'it counts. you cook.', 'screen': 'run/r0300', 'tag': 'poll',
     'do': 'Add a POLL: "trying it tonight" / "trying it tomorrow".'},
    {'t': 's_cta', 'title': 'Cooker Whistle<br>Counter', 'sub': 'one link. works offline.', 'sticker': 'link sticker',
     'do': 'Add a LINK sticker. Share the reel to your story right after this frame.'}])
# ================= day 4 · Tue 1 Dec · explain: set it up =================
W[4] = dict(phase='3 · explain', kind='reel', theme='explain', title='how to: set it up in a minute', reel='howto',
  cover={'t': 'cover', 'title': 'set it up<br>in a minute.', 'kicker': 'how to · #002', 'screen': 'learn-ok', 'size': 116},
  caption="set it up once, in under a minute:\n\n1. open the link in chrome → ⋮ → add to home screen\n2. allow the microphone, tap \"Learn my whistle\"\n3. stay quiet for two seconds, let the cooker whistle, tap Done\n4. set how many whistles you need. save it as a preset (toor dal · 3)\n5. backup timer, just in case\n6. tap Start. phone near the cooker, away from fans, screen on.\n\nthat's it. it counts. you cook.\n\nsave this for the next time the cooker goes on.",
  alt='How-to reel: adding the app to the home screen, Learn my whistle, Done, setting whistles and saving a preset, the backup timer, and tapping Start, ending on a plate of dal.',
  first_comment='stuck on a step? ask here, i answer every one.',
  stories=[
    {'t': 's_phone', 'title': 'step 1: Learn my whistle.', 'sub': 'every cooker sounds different.', 'screen': 'learn-ok', 'tag': 'how to',
     'do': 'No sticker needed. Add today\'s reel on the next frame (share → add to story).'},
    {'t': 's_phone', 'title': 'save your dish as a preset.', 'screen': 'presets', 'tag': 'quiz',
     'do': 'Add a QUIZ: "where should the phone go?" "near the cooker, away from fans" (correct) / "next to the mixie" / "in the other room".'},
    {'t': 's_hook', 'title': 'set it up yet?', 'sticker': 'slider', 'tag': 'how to', 'center': True,
     'do': 'Add an EMOJI SLIDER with 🔔: "how easy was setup?". Add all of today\'s frames to the "how to" highlight.'}])
# ================= day 5 · Wed 2 Dec · explain: everything it does =================
W[5] = dict(phase='3 · explain', kind='carousel', theme='explain', title='everything it does (and the tips)',
  feed=slides([
    {'t': 'count', 'photo': 'flame2', 'big': '3', 'title': 'everything #002 does.', 'sub': 'and how to get a perfect count.'},
    {'t': 'phone', 'kicker': '01', 'title': 'it counts every whistle.', 'sub': 'tap Start. it listens and adds one each time the cooker whistles.', 'screen': 'run/r0220'},
    {'t': 'phone', 'kicker': '02', 'title': 'it tells you when it\'s done.', 'sub': 'an alarm, a vibration, and the words on screen.', 'screen': 'run/r0300'},
    {'t': 'phone', 'kicker': '03', 'title': 'it learns your cooker.', 'sub': 'Learn my whistle: two seconds of quiet, one whistle, tap Done.', 'screen': 'learn-ok'},
    {'t': 'phone', 'kicker': '04', 'title': 'presets for every dish.', 'sub': 'toor dal · 3. rice · 2. one tap next time.', 'screen': 'presets'},
    {'t': 'phone', 'kicker': '05', 'title': 'a backup timer.', 'sub': 'set minutes too, in case a whistle is missed. or use Timer on its own.', 'screen': 'timer-running'},
    {'t': 'langs', 'kicker': '06', 'title': 'it speaks your language.', 'sub': 'six of them, switched in settings.', 'screens': ['lang1-alarm', 'lang2-alarm', 'lang3-alarm'], 'labels': ['தமிழ்', 'हिन्दी', 'తెలుగు']},
    {'t': 'list', 'title': 'for a perfect count', 'items': ['phone near the cooker, away from fans and the mixie.', 'keep the screen on. counting pauses if it turns off.', 'Learn my whistle once on your own cooker.', 'missed one? tap +1. counted a clang? tap −1.'], 'isize': 38},
    {'t': 'cta', 'title': 'Cooker Whistle<br>Counter', 'sub': 'no app store. no account. works offline.'}], tag='#002 · how it works'),
  caption="everything Cooker Whistle Counter does, in one place:\n\n01 counts every whistle\n02 alarm + vibration when it's done\n03 learns your own cooker's whistle\n04 presets for every dish\n05 a backup timer (or Timer on its own)\n06 english, தமிழ், हिन्दी, తెలుగు, മലയാളം, ಕನ್ನಡ\n\nfor a perfect count: phone near the cooker, away from fans, screen on. missed one? tap +1.\n\nsave it. link in bio.",
  alt='Nine slides explaining Cooker Whistle Counter: counting, the alarm, Learn my whistle, presets, the backup timer, six languages, tips for a perfect count, and the link in bio.',
  first_comment='which language are you using it in? 🗣️',
  stories=[
    {'t': 's_phone', 'title': 'which dish gets a preset first?', 'screen': 'presets', 'tag': 'poll',
     'do': 'Add a POLL: "dal" / "rice" (or "chana" / "rajma").'},
    {'t': 's_hook', 'title': 'ask me anything about #002.', 'sticker': 'question box', 'tag': 'faq',
     'do': 'Add a QUESTION sticker. Answer the best ones as story frames tonight and add them to the "faq" highlight.'}])
# ================= day 6 · Thu 3 Dec · close: in your language =================
W[6] = dict(phase='4 · close', kind='reel', theme='close', title='close: in your language (send it home)', reel='languages',
  cover={'t': 'cover', 'photo': 'cooker1', 'title': 'in your<br>language.', 'kicker': 'english · தமிழ் · हिन्दी · తెలుగు · മലയാളം · ಕನ್ನಡ', 'size': 140},
  caption="whistles done! turn off the gas.\nவிசில் முடிந்தது! கேஸை அணைக்கவும்.\nसीटियाँ पूरी! गैस बंद करें।\nవిజిల్స్ పూర్తయ్యాయి! గ్యాస్ ఆపండి.\n\nCooker Whistle Counter speaks six languages. send this to the person who runs the kitchen at home, in theirs.\n\nthank you for the first week of #002. link in bio, always.",
  alt='The alarm screen of Cooker Whistle Counter in English, Tamil, Hindi, Telugu, Malayalam and Kannada, cut on whips, ending on the app card with the six language names.',
  first_comment='send this to amma / mummy / paati / your flatmate who burns the dal 😄',
  stories=[
    {'t': 's_phone', 'title': 'send it home.', 'sub': 'in their language.', 'screen': 'lang1-alarm', 'tag': 'share',
     'do': 'Add a LINK sticker to the app and a MENTION sticker inviting people to tag someone they cook with.'},
    {'t': 's_hook', 'bg': 'acc', 'title': 'thank you for #002.', 'sub': 'Cooker Whistle Counter stays in my bio.', 'center': True, 'tag': 'thank you',
     'do': 'Add a LINK sticker. Reshare any story you were tagged in today.'},
    {'t': 's_hook', 'bg': 'ink', 'title': 'what should #003 fix?', 'sticker': 'question box', 'center': True, 'tag': 'next',
     'do': 'Add a QUESTION sticker: "build me something for…". Add to the "next" highlight.'}])
HIGHLIGHT_OF = {1: '#002', 2: '#002', 3: '#002', 4: 'how to', 5: 'faq', 6: 'next'}

def emit(n, x, folder, d=None, label=''):
    feed_files, story_files = [], []
    if x['kind'] in ('carousel', 'post'):
        for i, s in enumerate(x['feed']):
            p = f'{folder}/feed/{"slide" if x["kind"] == "carousel" else "post"}-{i + 1:02d}.png'; A(p, s, 1080, 1350); feed_files.append(p)
    else:
        A(f'{folder}/feed/cover.png', x['cover'], 1080, 1920); feed_files += [f'{folder}/feed/cover.png', f'{folder}/feed/{x["reel"]}.mp4']
    for i, s in enumerate(x.get('stories', [])):
        p = f'{folder}/story/story-{i + 1:02d}.png'; spec = {k: v for k, v in s.items() if k not in ('do', 'sticker')}
        if 'sticker' in s: spec['sticker'] = True
        A(p, spec, 1080, 1920); story_files.append(p)
    return {'day': n, 'date': d.isoformat() if d else '', 'label': label, 'folder': folder, 'phase': x['phase'], 'kind': x['kind'], 'title': x['title'],
            'time': TIMES[x['kind']], 'story_time': STORY_TIME, 'reel': x.get('reel'), 'feed': feed_files, 'stories': story_files,
            'story_do': [s['do'] for s in x.get('stories', [])], 'caption': x['caption'], 'hashtags': TAGS[x['theme']], 'alt': x['alt'],
            'first_comment': x['first_comment'], 'highlight': HIGHLIGHT_OF.get(n, '') if d else ''}

for n in range(1, 7):
    d, label = day(n); plan.append(emit(n, W[n], f'Day{n:02d}_{d.strftime("%a-%d-%b")}', d, label))

# ================= the after-launch library: finished posts for the days after 3 Dec =================
B = [
 ('carousel_faq', dict(phase='library', kind='carousel', theme='explain', title='the questions, answered',
  feed=slides([
    {'t': 'hook', 'kicker': 'faq · #002', 'title': 'your questions, answered.', 'sub': 'the ones that came up most.'},
    {'t': 'qa', 'q': 'do i need to install anything?', 'a': 'no. open the link in chrome → ⋮ → add to home screen. it opens like an app.'},
    {'t': 'qa', 'q': 'does it work offline?', 'a': 'yes. once it\'s opened, it keeps working without internet.'},
    {'t': 'qa', 'q': 'is it recording me?', 'a': 'it listens for whistles on your phone. there\'s no account and nothing to sign in to.'},
    {'t': 'qa', 'q': 'it missed a whistle.', 'a': 'tap +1. then Learn my whistle again on your cooker, and move the phone away from fans.'},
    {'t': 'qa', 'q': 'can i lock the screen?', 'a': 'keep it on: counting pauses if the screen turns off.'},
    {'t': 'cta', 'title': 'Cooker Whistle<br>Counter', 'sub': 'one link. works offline.'}], tag='#002 · faq'),
  caption="the #002 questions that came up most:\n\n· install? no. chrome → ⋮ → add to home screen\n· offline? yes\n· account? none\n· missed a whistle? tap +1, then Learn my whistle again\n· lock the screen? keep it on, counting pauses if it turns off\n\nmore questions? ask below. link in bio.",
  alt='Seven slides answering common questions about Cooker Whistle Counter.', first_comment='what did i miss? ask here 👇')),
 ('post_count', dict(phase='library', kind='post', theme='launch', title='it counts. you cook.',
  feed=[{'t': 'hook', 'photo': 'dal', 'title': 'it counts.<br>you cook.', 'sub': 'Cooker Whistle Counter · link in bio', 'size': 150, 'tag': '#002 whistle counter'}],
  caption="it counts. you cook.\n\nCooker Whistle Counter listens for the whistles so you can chop, stir, answer the door, and still get the dal right.\n\nlink in bio.",
  alt='A plate of dal and rice with the words: it counts, you cook.', first_comment='what\'s on the stove today?')),
 ('carousel_build-log', dict(phase='library', kind='carousel', theme='build', title='build log: how #002 hears a whistle',
  feed=slides([
    {'t': 'log', 'title': 'how #002 hears a whistle.', 'lines': ['the mic listens on your phone.', 'it hears the band your cooker whistles in.', 'louder than the kitchen, for a moment: a clang won\'t count.', 'then it waits for quiet, so one whistle counts once.']},
    {'t': 'log', 'kicker': 'build log · learn my whistle', 'title': 'every cooker sounds different.', 'lines': ['two seconds of quiet: the kitchen\'s own noise.', 'one whistle: your cooker\'s pitch.', 'Done: it listens for that from now on.']},
    {'t': 'log', 'kicker': 'build log · rules', 'title': 'the three rules, again.', 'lines': ['fixes one small, everyday problem.', 'just open it and use it.', 'built from scratch, start to finish.']},
    {'t': 'cta', 'title': 'Cooker Whistle<br>Counter', 'sub': 'built from scratch. link in bio.'}], tag='#002 · build log'),
  caption="build log for #002.\n\nhow does a phone hear a cooker whistle? it listens in the band your cooker whistles in, needs the sound to stay above the kitchen's own noise for a moment (so a clang doesn't count), then waits for quiet, so one whistle counts once. Learn my whistle tunes that to your own cooker and kitchen.\n\nbuilt from scratch, like everything here.",
  alt='Four dark build-log slides explaining how the app detects a cooker whistle and how Learn my whistle works.', first_comment='want more build logs like this? 🛠️')),
 ('carousel_languages', dict(phase='library', kind='carousel', theme='close', title='six languages, side by side',
  feed=slides([
    {'t': 'hook', 'photo': 'cooker2', 'kicker': '#002 · in your language', 'title': 'whistles done!<br>turn off the gas.', 'size': 124},
    {'t': 'langs', 'title': 'six languages.', 'sub': 'english, then five more.', 'screens': ['run/r0300', 'lang1-alarm', 'lang2-alarm'], 'labels': ['English', 'தமிழ்', 'हिन्दी']},
    {'t': 'langs', 'title': 'switch in settings.', 'sub': 'the whole app changes, alarm included.', 'screens': ['lang3-alarm', 'lang4-alarm', 'lang5-alarm'], 'labels': ['తెలుగు', 'മലയാളം', 'ಕನ್ನಡ']},
    {'t': 'cta', 'title': 'Cooker Whistle<br>Counter', 'sub': 'send it home, in their language.'}], tag='#002 · languages'),
  caption="whistles done! turn off the gas. in six languages: english, தமிழ், हिन्दी, తెలుగు, മലയാളം, ಕನ್ನಡ.\n\nopen settings (the gear) and pick one. the whole app switches.\n\nwhich one should be next?",
  alt='The alarm screen in six languages, three phones per slide.', first_comment='which language should i add next? 👇')),
 ('post_offline', dict(phase='library', kind='post', theme='launch', title='no app store. works offline.',
  feed=[{'t': 'hook', 'bg': 'acc', 'kicker': '#002 · the facts', 'title': 'no app store.<br>no account.<br>works offline.', 'sub': 'one link. add it to your home screen.', 'size': 120}],
  caption="no app store. no account. works offline.\n\nCooker Whistle Counter is one link: open it in chrome, add it to your home screen, and it opens like an app, even without internet.\n\nlink in bio.",
  alt='An orange poster: no app store, no account, works offline.', first_comment='tag someone whose phone is full 😅')),
]
bonus = []
for i, (name, x) in enumerate(B):
    bonus.append(emit(i + 1, x, f'after-launch-library/{i + 1:02d}_{name}'))
json.dump(bonus, open(f'{OUT}/bonus.json', 'w'), indent=1, ensure_ascii=False)

# ================= profile, highlight covers, cards =================
A('profile/profile-picture.png', {'t': 'avatar', 'cursor': '#FF8A3D'}, 1080, 1080)
ICON = lambda inner: {'t': 'highlight', 'icon': inner}
COOKER_SVG = '<svg width="420" height="420" viewBox="0 0 512 512"><g fill="none" stroke="#A89A8C" stroke-width="16" stroke-linecap="round"><path d="M206 78c-14 14-14 34 0 48"/><path d="M256 78c-14 14-14 34 0 48"/><path d="M306 78c-14 14-14 34 0 48"/></g><rect x="236" y="140" width="40" height="52" rx="12" fill="#F5EDE4"/><rect x="62" y="280" width="54" height="30" rx="15" fill="#F5EDE4"/><rect x="396" y="280" width="54" height="30" rx="15" fill="#F5EDE4"/><rect x="110" y="230" width="292" height="170" rx="46" fill="#FF8A3D"/><rect x="96" y="190" width="320" height="52" rx="26" fill="#FFB07A"/></svg>'
A('profile/highlight-covers/002.png', ICON(COOKER_SVG), 1080, 1920)
A('profile/highlight-covers/002-number.png', ICON('<div style="font:500 210px/1 \'DM Mono\';color:#FFB07A">#002</div>'), 1080, 1920)
A('profile/highlight-covers/how-to.png', ICON('<div style="font:500 230px/1 \'DM Mono\';color:#ECEEF2">1-2-3</div>'), 1080, 1920)
A('profile/highlight-covers/faq.png', ICON('<div style="font:800 380px/1 \'Bricolage Grotesque\';color:#ECEEF2">?</div>'), 1080, 1920)
A('profile/highlight-covers/next.png', ICON('<div style="font:500 210px/1 \'DM Mono\';color:#ECEEF2">#003</div>'), 1080, 1920)
A('_build/endcard.png', {'t': 'endcard'}, 1080, 1920)

json.dump(assets, open(f'{OUT}/assets.json', 'w'), indent=1, ensure_ascii=False)
json.dump(plan, open(f'{OUT}/plan.json', 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(len(assets), 'images;', Counter(p['kind'] for p in plan), sum(len(p['stories']) for p in plan), 'story frames;', len(bonus), 'library posts')
