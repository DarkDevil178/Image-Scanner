# The 30-day launch of @wierd_stuff_i_make and its first product, Wardrobe (#001).
# Writes: build/assets.json (every image to render) and build/plan.json (the calendar, captions, stickers, times).
import json, datetime, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'build'); os.makedirs(OUT, exist_ok=True)
START = datetime.date(2026, 11, 21)
ALL = ['tee', 'longsleeve', 'hoodie', 'denim', 'workjacket', 'trousers', 'skirt', 'boots', 'loafer', 'formal', 'sneakers2', 'briefcase', 'scarf', 'bag']
TOPS8 = ['tee', 'longsleeve', 'denim', 'workjacket', 'trousers', 'skirt', 'boots', 'loafer']
TAGS_CORE = '#wierdstuffimake #wardrobeapp #capsulewardrobe #whattowear #outfitplanner #closetorganization'
TAGS = {
    'page': '#wierdstuffimake #buildinpublic #madefromscratch #indiemaker #everydaytools #productdesign #makersgonnamake',
    'teaser': '#wierdstuffimake #nothingtowear #closetgoals #comingsoon #outfitideas #wardrobe #fashiontech',
    'launch': TAGS_CORE + ' #blackfriday #shopyourcloset #sustainablefashion #slowfashion #outfitideas',
    'feature': TAGS_CORE + ' #outfitideas #ootd #wardrobeorganizer #digitalwardrobe #fashionapp',
    'money': TAGS_CORE + ' #costperwear #slowfashion #sustainablefashion #mindfulspending #buylesschoosewell',
    'travel': TAGS_CORE + ' #packinglist #packingtips #travelwardrobe #holidaypacking #carryononly',
    'build': '#wierdstuffimake #buildinpublic #indiemaker #webdev #ondeviceai #privacyfirst #madefromscratch #productdesign',
}
TIMES = {'reel': '7:00 pm', 'carousel': '1:00 pm', 'post': '1:00 pm', 'video': '7:00 pm'}
STORY_TIME = '9:00 am (frame 1), the rest spread through the day'

def day(n): d = START + datetime.timedelta(days=n - 1); return d, d.strftime('%a %d %b')

assets, plan = [], []
def A(path, spec, W, H): assets.append({'out': path, 'W': W, 'H': H, **spec})

def slides(n, items, tag=None):
    """carousel slides: each a template spec; adds the counter and swipe hint"""
    out = []
    for i, s in enumerate(items):
        s = dict(s); s.setdefault('counter', f'{i + 1:02d}/{len(items):02d}')
        if i == 0: s.setdefault('swipe', True)
        if tag: s.setdefault('tag', tag)
        out.append(s)
    return out

D = {}
# ================= PHASE 1 · the page wakes up (days 1-6) =================
D[1] = dict(phase='1 · the page wakes up', kind='carousel', theme='page', title='hi. i make useful things from scratch.',
  feed=slides(1, [
    {'t': 'hook', 'title': 'hi. i make useful things from scratch.', 'sub': 'this page is where they live.', 'tag': 'hello', 'size': 128},
    {'t': 'hook', 'bg': 'ink', 'kicker': 'what you’ll find here', 'title': 'tools for everyday life. built by hand.', 'tag': 'hello'},
    {'t': 'list', 'title': 'every thing i make keeps 3 rules', 'items': ['it fixes one small, everyday problem.', 'you can just open it and use it.', 'it’s built from scratch, start to finish.'], 'tag': 'hello'},
    {'t': 'hook', 'kicker': 'product #001', 'title': 'lands friday,<br>27 november.', 'cutouts': TOPS8, 'tag': '#001 · soon', 'size': 110},
    {'t': 'hook', 'bg': 'ink', 'title': 'follow along.<br>it gets weird.', 'sub': 'turn on post notifications so you don’t miss #001.', 'tag': 'hello'}]),
  caption="hi. i'm starting a page for the things i make.\n\nuseful things, built from scratch, for everyday use. some of them will be a bit weird. all of them will be real.\n\nthe first one lands friday, 27 november. it's for a problem you probably had this morning.\n\nfollow along 👀",
  alt='Five slides introducing the page: useful things built from scratch for everyday use, three rules, and product #001 landing Friday 27 November.',
  first_comment='what\'s one everyday thing that annoys you enough that someone should build a fix? i read every reply.',
  stories=[
    {'t': 's_hook', 'title': 'new page.<br>new things.', 'sub': 'useful stuff, built from scratch.', 'tag': 'hello', 'center': True,
     'do': 'Post first thing. Add a "New post" share of today\'s carousel on top of this frame, or a link sticker to the post.'},
    {'t': 's_hook', 'title': 'what wastes more of your morning?', 'sticker': 'poll sticker goes here', 'tag': 'poll',
     'do': 'Add a POLL sticker in the marked space: "choosing clothes" / "finding my keys".'}])
D[2] = dict(phase='1 · the page wakes up', kind='reel', theme='teaser', title='teaser 1: nothing to wear?', reel='teaser1',
  cover={'t': 'cover', 'title': 'nothing to wear?', 'kicker': '#001 · 27.11', 'cutouts': ['tee', 'denim', 'boots'], 'size': 130},
  caption="you know the feeling. full closet, nothing to wear.\n\nproduct #001 is for exactly that.\nfriday, 27.11.",
  alt='Clothes drop around the words "Nothing to wear?", then a card: product #001, 27 November.',
  first_comment='be honest: how many things in your closet haven\'t you worn this year?',
  stories=[
    {'t': 's_hook', 'title': 'what\'s the weirdest thing you own but never wear?', 'sticker': 'question box goes here', 'tag': 'question',
     'do': 'Add a QUESTION sticker: "the thing i never wear is…". Share the best answers tomorrow (with permission).'}])
D[3] = dict(phase='1 · the page wakes up', kind='carousel', theme='teaser', title='the "nothing to wear" problem',
  feed=slides(3, [
    {'t': 'hook', 'title': 'a full closet.<br>nothing to wear.', 'cutouts': TOPS8, 'tag': '#001 · soon'},
    {'t': 'hook', 'kicker': '01', 'title': 'you forget what you own.', 'sub': 'out of sight is out of mind. half of it hasn’t seen daylight in months.', 'tag': '#001 · soon'},
    {'t': 'hook', 'kicker': '02', 'title': 'you wear the same five things.', 'sub': 'because they’re on top of the pile, not because you love them most.', 'tag': '#001 · soon'},
    {'t': 'hook', 'kicker': '03', 'title': 'you buy what you already have.', 'sub': 'another black tee. another pair of jeans. sound familiar?', 'tag': '#001 · soon'},
    {'t': 'hook', 'bg': 'ink', 'title': 'so i built something for it.', 'tag': '#001 · soon'},
    {'t': 'hook', 'kicker': 'product #001', 'title': 'friday,<br>27 november.', 'sub': 'follow so you see it first.', 'tag': '#001 · soon'}]),
  caption="the 'nothing to wear' problem isn't about clothes. it's about not seeing what you have.\n\n01 you forget what you own\n02 you wear the same five things\n03 you buy what you already have\n\nso i built something for it. friday, 27 november.",
  alt='Six slides on why a full closet feels like nothing to wear, ending with product #001 on 27 November.',
  first_comment='which one is you: 01, 02 or 03? (mine is all three)',
  stories=[
    {'t': 's_hook', 'title': 'how full is your closet right now?', 'sticker': 'emoji slider goes here', 'tag': 'slider',
     'do': 'Add an EMOJI SLIDER sticker with 👕 (or 🫠): "how full is your closet?".'},
    {'t': 's_countdown', 'big': '4', 'title': 'days to #001', 'sticker': 'countdown sticker goes here',
     'do': 'Add a COUNTDOWN sticker named "product #001" ending Fri 27 Nov, 7:00 pm. Keep this frame for the Highlights later.'}])
D[4] = dict(phase='1 · the page wakes up', kind='post', theme='page', title='built from scratch. for everyday use.',
  feed=[{'t': 'hook', 'bg': 'ink', 'kicker': 'wierd_stuff_i_make', 'title': 'built from scratch.<br>for everyday use.', 'sub': 'no templates. no shortcuts. just things that help.', 'tag': 'manifesto', 'size': 120}],
  caption="that's the whole idea of this page.\n\nevery thing here starts as a blank file and ends as something you can use every day. no app store, no sign-up, no fluff.\n\n#001 lands friday.",
  alt='A dark poster reading: built from scratch, for everyday use.',
  first_comment='what would you want built from scratch?',
  stories=[
    {'t': 's_log', 'title': 'day 4 of 4 before launch', 'lines': ['the hardest part: making a photo lose its background', 'on your phone. not on a server.', 'it finally works.'],
     'do': 'Post as is. It builds curiosity without naming the product.'},
    {'t': 's_hook', 'title': 'guess what #001 does', 'sticker': 'quiz sticker goes here', 'tag': 'quiz',
     'do': 'Add a QUIZ sticker: "organises your closet" (correct) / "waters your plants" / "splits the bill".'}])
D[5] = dict(phase='1 · the page wakes up', kind='reel', theme='teaser', title='teaser 2: photo in, background out', reel='teaser2',
  cover={'t': 'cover', 'title': 'photo in.<br>background out.', 'kicker': '#001 · 27.11', 'screen': 'a-cut-done', 'size': 110},
  caption="take a photo of any piece of clothing. the background disappears. on your phone, in seconds.\n\nthat's one tiny part of #001.\n27.11.",
  alt='A photo of a white t-shirt on a carpet becomes a clean cut-out, then a card: product #001, 27 November.',
  first_comment='what would you photograph first?',
  stories=[
    {'t': 's_phone', 'title': 'sneak peek', 'sub': 'two days.', 'screen': 'w-home', 'blur': True, 'tag': 'sneak peek',
     'do': 'Post as is (the screen is blurred on purpose). Add an EMOJI SLIDER 🔥 "how excited?".'}])
D[6] = dict(phase='1 · the page wakes up', kind='carousel', theme='teaser', title='tomorrow: #001',
  feed=slides(6, [
    {'t': 'hook', 'kicker': 'tomorrow', 'title': 'product #001.', 'sub': 'here’s what it does. the name is tomorrow.', 'tag': '#001 · tomorrow'},
    {'t': 'phone', 'title': 'your whole closet. on your phone.', 'screen': 'w-home', 'tag': '#001 · tomorrow'},
    {'t': 'phone', 'title': 'snap it. the background disappears.', 'screen': 'a-cut-done', 'tag': '#001 · tomorrow'},
    {'t': 'phone', 'title': 'swipe outfits together.', 'screen': 't-style', 'tag': '#001 · tomorrow'},
    {'t': 'phone', 'title': 'plan the week.', 'screen': 'p-agenda', 'tag': '#001 · tomorrow'},
    {'t': 'hook', 'bg': 'ink', 'title': 'tomorrow,<br>7 pm.', 'sub': 'turn on post notifications.', 'tag': '#001 · tomorrow'}]),
  caption="tomorrow. 7 pm.\n\nyour whole closet on your phone. snap a piece, the background disappears. swipe outfits together. plan the week.\n\nthe name? tomorrow.",
  alt='Six slides previewing product #001: the closet on a phone, a photo cut-out, swiping outfits, a weekly plan, launching tomorrow at 7 pm.',
  first_comment='guess the name. closest guess gets a shout-out tomorrow.',
  stories=[
    {'t': 's_countdown', 'big': '1', 'title': 'day to go', 'sticker': 'share the countdown sticker here',
     'do': 'Re-add the "product #001" COUNTDOWN sticker so people can tap "remind me".'},
    {'t': 's_hook', 'title': 'turn on notifications', 'sub': 'tap my name → bell icon → posts, stories, reels.', 'tag': 'how to',
     'do': 'Post as is.'}])
# ================= PHASE 2 · launch week (days 7-13) =================
D[7] = dict(phase='2 · launch week', kind='reel', theme='launch', title='LAUNCH: Wardrobe is out', reel='launch',
  cover={'t': 'cover', 'title': 'it’s here.<br>Wardrobe.', 'kicker': 'product #001', 'screen': 'w-home', 'size': 120},
  caption="#001 is out. meet Wardrobe.\n\nyour whole closet on your phone. snap a photo, the background disappears. swipe outfits together, or tap Style me when you're stuck. plan the week, mark what you wore.\n\nit's one html file. no app store, no account. your photos never leave your phone.\n\nit's black friday. before you buy more clothes, see what you already own. link in bio.",
  alt='The Wardrobe launch film: clothes pile up around "Nothing to wear?", a phone shows the app, a t-shirt photo is cut out, outfits are swiped together, the week is planned.',
  first_comment='first 10 people to post their closet in Wardrobe and tag me get featured in my stories 🖤',
  stories=[
    {'t': 's_cta', 'title': 'it’s live.', 'sub': 'Wardrobe · product #001', 'sticker': 'link sticker goes here',
     'do': 'Add a LINK sticker to the app. Post at 7:00 pm right after the reel.'},
    {'t': 's_phone', 'title': 'shop your own closet first.', 'sub': 'it’s black friday.', 'screen': 'w-home', 'tag': 'black friday',
     'do': 'Add a POLL: "buying anything today?" "yes 🛍️" / "checking my closet first".'},
    {'t': 's_hook', 'bg': 'ink', 'title': 'tap the link. add one piece.', 'sub': 'that’s all for today.', 'sticker': 'link sticker goes here', 'center': True,
     'do': 'Add a LINK sticker again. Reshare the launch reel to stories later tonight.'}])
D[8] = dict(phase='2 · launch week', kind='reel', theme='feature', title='how to add clothes', reel='ch1',
  cover={'t': 'cover', 'title': 'add clothes in seconds', 'kicker': 'how to · 01', 'screen': 'a-cut-done', 'size': 110},
  caption="how to add clothes to Wardrobe:\n\n1. tap +\n2. take a photo, or pick a few at once\n3. Smart AI cuts the background away (on your phone)\n4. touch up with eraser and restore if you need to\n5. add the details, save to wardrobe\n\nit even asks for the real length, so everything stays to scale when you try outfits on.",
  alt='A screen recording of adding a t-shirt to Wardrobe: the photo guide, the AI cut-out, touch-up brushes and the details form.',
  first_comment='what was the first thing you added? 👇',
  stories=[
    {'t': 's_cut', 'title': 'your first piece', 'sticker': 'question box goes here',
     'do': 'Add a QUESTION sticker: "what was the first thing you added?".'}])
D[9] = dict(phase='2 · launch week', kind='carousel', theme='feature', title='every feature in Wardrobe',
  feed=slides(9, [
    {'t': 'hook', 'kicker': 'save this', 'title': 'everything Wardrobe does, in 8 slides.', 'cutouts': TOPS8},
    {'t': 'phone', 'title': 'add clothes', 'sub': 'snap a piece. the background disappears. right on your phone.', 'screen': 'a-cut-done'},
    {'t': 'phone', 'title': 'your wardrobe', 'sub': 'everything you own, sorted and searchable.', 'screen': 'w-home'},
    {'t': 'phone', 'title': 'try on', 'sub': 'swipe tops, bottoms and shoes. at real size.', 'screen': 't-base'},
    {'t': 'phone', 'title': 'style me', 'sub': 'stuck? it picks colours that work together.', 'screen': 't-style'},
    {'t': 'phone', 'title': 'outfits', 'sub': 'arrange the board. save it. share it.', 'screen': 'o-board'},
    {'t': 'phone', 'title': 'plan', 'sub': 'outfits on your calendar, with the forecast.', 'screen': 'p-agenda'},
    {'t': 'phone', 'title': 'insights', 'sub': 'what you wear, and what each wear costs.', 'screen': 'i-top'},
    {'t': 'cta'}]),
  caption="everything Wardrobe does, in one post. save it for later 📌\n\nadd clothes · your wardrobe · try on · style me · outfits · plan · insights\n\nand it's all one html file. link in bio.",
  alt='Nine slides showing each Wardrobe feature on a phone: adding clothes, the wardrobe, try on, style me, outfits, plan and insights.',
  first_comment='which feature are you trying first?',
  stories=[
    {'t': 's_phone', 'title': 'which feature first?', 'screen': 't-style', 'tag': 'poll',
     'do': 'Add a POLL: "try on" / "plan the week". Add a link sticker to today\'s carousel.'}])
D[10] = dict(phase='2 · launch week', kind='reel', theme='feature', title='try on + style me', reel='ch3',
  cover={'t': 'cover', 'title': 'stuck? tap Style me.', 'kicker': 'how to · 03', 'screen': 't-style', 'size': 110},
  caption="try on in Wardrobe: tops, bottoms and shoes in rows, at their real size. swipe to mix and match.\n\nlock a piece you love and shuffle the rest. stuck? tap Style me: it picks a combination whose colours work together, suited to the season and the weather.\n\nnot for you? thumbs-down, and it steers away from that pairing.",
  alt='A screen recording of Try on: swiping rows of clothes, locking a top, and Style me picking an outfit.',
  first_comment='would you trust Style me to dress you tomorrow? 😅',
  stories=[
    {'t': 's_phone', 'title': 'which one did Style me pick?', 'screen': 't-style', 'tag': 'quiz',
     'do': 'Add a QUIZ sticker: "white tee + pleated skirt" (correct) / "hoodie + trousers" / "denim on denim".'}])
D[11] = dict(phase='2 · launch week', kind='carousel', theme='feature', title='how to take a photo for a perfect cut-out',
  feed=slides(11, [
    {'t': 'beforeafter', 'title': 'the perfect cut-out, in 5 rules.'},
    {'t': 'hook', 'kicker': 'rule 01', 'title': 'lay it flat.', 'sub': 'sleeves spread out, wrinkles smoothed, collar at the top.'},
    {'t': 'hook', 'kicker': 'rule 02', 'title': 'daylight. no flash.', 'sub': 'bright room light works too.'},
    {'t': 'hook', 'kicker': 'rule 03', 'title': 'phone flat, straight above.', 'sub': 'one item per photo, filling about 80% of the frame.'},
    {'t': 'hook', 'kicker': 'rule 04', 'title': 'a plain surface that contrasts.', 'sub': 'a dark tee on a light sheet. a light tee on a dark one.'},
    {'t': 'hook', 'kicker': 'rule 05', 'title': 'no hangers, folds or hands.', 'sub': 'and if something slips through: eraser and restore.'}]),
  caption="5 rules for a perfect cut-out in Wardrobe (straight from the app's own photo guide):\n\n01 lay it flat\n02 daylight, no flash\n03 phone flat, straight above\n04 a plain surface that contrasts\n05 no hangers, folds or hands\n\nsave this for your first big closet session 📌",
  alt='Six slides: a before-and-after cut-out of a white t-shirt and five rules for taking a good clothing photo.',
  first_comment='tip: do it in one go on a weekend morning with good light. 20 pieces takes less than a coffee.',
  stories=[
    {'t': 's_cut', 'title': 'try it on one piece today', 'sticker': 'emoji slider goes here',
     'do': 'Add an EMOJI SLIDER 🪄 "how clean was your cut-out?".'}])
D[12] = dict(phase='2 · launch week', kind='reel', theme='feature', title='plan the week', reel='ch5',
  cover={'t': 'cover', 'title': 'plan the week. with the forecast.', 'kicker': 'how to · 05', 'screen': 'p-agenda', 'size': 100},
  caption="plan in Wardrobe: put outfits on your calendar. add your city and every day shows its forecast.\n\nempty day? tap Style me and it plans one for you. when the day comes, mark as worn. every wear is logged.",
  alt='A screen recording of the Plan view: an agenda with forecasts, the month view, Style me planning a day, and Mark as worn.',
  first_comment='do you plan outfits the night before, or decide at the door?',
  stories=[
    {'t': 's_phone', 'title': 'do you plan outfits the night before?', 'screen': 'p-agenda', 'tag': 'poll',
     'do': 'Add a POLL: "always" / "at the door 🫠".'}])
D[13] = dict(phase='2 · launch week', kind='carousel', theme='feature', title='FAQ',
  feed=slides(13, [
    {'t': 'hook', 'kicker': 'you asked', 'title': 'Wardrobe, answered.', 'sub': 'the questions from launch week.'},
    {'t': 'qa', 'q': 'do i need an account?', 'a': 'no. there\'s no sign-up. you open it and start.'},
    {'t': 'qa', 'q': 'where are my photos stored?', 'a': 'on your device. they never leave your phone.'},
    {'t': 'qa', 'q': 'is it in the app store?', 'a': 'no. it\'s one html file. add it to your home screen and it works like an app.'},
    {'t': 'qa', 'q': 'does the ai send my photos anywhere?', 'a': 'no. it runs on your phone. it downloads once (about 45 MB, wi-fi recommended).'},
    {'t': 'qa', 'q': 'what if i change phones?', 'a': 'download a backup: one file with everything. restore it on the new phone.'},
    {'t': 'cta'}]),
  caption="your launch-week questions, answered:\n\nno account. photos stay on your device. not in the app store: it's one html file you add to your home screen. the ai runs on your phone. backups are one file.\n\nmore questions? drop them below.",
  alt='Seven slides answering questions about Wardrobe: no account, photos stay on the device, one HTML file, on-device AI, backup and restore.',
  first_comment='ask anything, i\'ll answer every one 👇',
  stories=[
    {'t': 's_hook', 'bg': 'ink', 'title': 'ask me anything about Wardrobe', 'sticker': 'question box goes here',
     'do': 'Add a QUESTION sticker "ask me anything". Answer 3-5 tonight as separate story frames.'}])
# ================= PHASE 3 · every feature, up close (days 14-23) =================
D[14] = dict(phase='3 · every feature, up close', kind='reel', theme='feature', title='your wardrobe', reel='ch2',
  cover={'t': 'cover', 'title': 'everything you own. in one place.', 'kicker': 'how to · 02', 'screen': 'w-home', 'size': 100},
  caption="your wardrobe in Wardrobe: tops, bottoms, shoes, jackets and accessories, with today's outfit at the top.\n\nsearch by name, brand or colour. tap any piece: how often you've worn it, and what it costs per wear.",
  alt='A screen recording of the Wardrobe view: scrolling categories, search, and a piece\'s details with cost per wear.',
  first_comment='what\'s the most-worn thing you own?',
  stories=[
    {'t': 's_phone', 'title': 'search by colour', 'sub': 'try "black". scary.', 'screen': 'w-q5', 'tag': 'tip',
     'do': 'Add an EMOJI SLIDER 🖤 "how much black do you own?".'}])
D[15] = dict(phase='3 · every feature, up close', kind='carousel', theme='feature', title='capsule wardrobe 101',
  feed=slides(15, [
    {'t': 'stat', 'kicker': 'capsule wardrobe 101', 'big': '7 → 8', 'title': 'pieces → outfits.', 'sub': 'a small set where everything works together.', 'size': 230},
    {'t': 'cutgrid', 'title': 'the 7 pieces', 'items': ['tee', 'longsleeve', 'trousers', 'skirt', 'loafer', 'formal', 'briefcase']},
    {'t': 'phone', 'title': 'Wardrobe counts the combinations for you.', 'screen': 'l-cap'},
    {'t': 'list', 'title': 'build your own', 'items': ['pick 2 tops, 2 bottoms, 2 shoes you love.', 'add one layer and one accessory.', 'make a capsule in Lists.', 'tap "Try on these" and mix.']},
    {'t': 'cta'}]),
  caption="capsule wardrobe 101: 7 pieces that make 8 outfits.\n\nin Wardrobe, open Lists → New capsule, add the pieces, and it counts every top, bottom and shoe combination for you. then tap 'Try on these'.\n\nshow me your capsule 👇",
  alt='Five slides: a capsule of seven pieces making eight outfits, the pieces, the capsule screen in Wardrobe, and how to build one.',
  first_comment='what would your 7 be?',
  stories=[
    {'t': 's_cuts', 'title': 'build a capsule this weekend', 'items': ['tee', 'longsleeve', 'trousers', 'skirt', 'loafer', 'formal'], 'sticker': 'poll sticker goes here',
     'do': 'Add a POLL: "doing it" / "too chaotic for capsules".'}])
D[16] = dict(phase='3 · every feature, up close', kind='reel', theme='feature', title='outfits + the board', reel='ch4',
  cover={'t': 'cover', 'title': 'make it an outfit.', 'kicker': 'how to · 04', 'screen': 'o-board', 'size': 116},
  caption="outfits in Wardrobe: tap Create outfit, move and resize every piece on the board, change the background, undo anything.\n\nsaved outfits live in Outfits: favourite them, tag them, duplicate one, or share it as an image.",
  alt='A screen recording of the outfit board: arranging pieces, picking a background, saving and opening the outfit sheet.',
  first_comment='share your board and tag me, i\'ll repost the best ones 🖤',
  stories=[
    {'t': 's_phone', 'title': 'share your board', 'sub': 'tag @wierd_stuff_i_make', 'screen': 'o-board', 'tag': 'ugc',
     'do': 'Add a MENTION sticker of your handle and a "Add yours" sticker: "my outfit board".'}])
D[17] = dict(phase='3 · every feature, up close', kind='post', theme='feature', title='before / after cut-out',
  feed=[{'t': 'beforeafter', 'title': 'your photo in.<br>background out.'}],
  caption="left: a t-shirt on a carpet.\nright: the same t-shirt, cut out by Wardrobe's Smart AI, on the phone.\n\nno upload, no server, no waiting for an email.",
  alt='Side by side: a photo of a white t-shirt on carpet, and the same t-shirt cleanly cut out.',
  first_comment='what\'s the hardest thing you\'d test it on? (lace? fur? a disco jacket?)',
  stories=[
    {'t': 's_hook', 'title': 'where do your photos go?', 'sticker': 'quiz sticker goes here', 'tag': 'quiz',
     'do': 'Add a QUIZ sticker: "nowhere, they stay on my phone" (correct) / "to the cloud" / "to a server".'}])
D[18] = dict(phase='3 · every feature, up close', kind='carousel', theme='money', title='cost per wear, explained',
  feed=slides(18, [
    {'t': 'stat', 'kicker': 'cost per wear', 'big': '₹154', 'title': 'per wear.', 'cut': 'trousers', 'sub': 'the number that changes how you shop.'},
    {'t': 'hook', 'title': 'price ÷ wears = cost per wear.', 'sub': '₹1,999 trousers, worn 13 times: ₹154 a wear. (an example from my demo closet.)'},
    {'t': 'hook', 'title': 'cheap things can be expensive.', 'sub': 'a ₹500 top worn once costs ₹500 a wear.'},
    {'t': 'phone', 'title': 'Wardrobe works it out for you.', 'sub': 'add a price, log your wears.', 'screen': 'w-detail'},
    {'t': 'phone', 'title': 'and ranks your best value.', 'screen': 'i-top'},
    {'t': 'cta'}]),
  caption="cost per wear = price ÷ number of wears.\n\n₹1,999 trousers worn 13 times = ₹154 a wear. a ₹500 top worn once = ₹500 a wear.\n\nin Wardrobe, add a price and log what you wear. it works out the rest, and Insights ranks your best value.",
  alt='Six slides explaining cost per wear with an example, and how Wardrobe calculates it.',
  first_comment='what\'s your best-value piece? mine are these trousers.',
  stories=[
    {'t': 's_hook', 'title': 'what\'s the most-worn thing you own?', 'sticker': 'question box goes here', 'tag': 'question',
     'do': 'Add a QUESTION sticker. Share a few answers tomorrow.'}])
D[19] = dict(phase='3 · every feature, up close', kind='reel', theme='travel', title='capsules, trips & wish list', reel='ch6',
  cover={'t': 'cover', 'title': 'pack for december.', 'kicker': 'how to · 06', 'screen': 'l-trip', 'size': 120},
  caption="lists in Wardrobe:\n\ncapsules: a small set that all works together (it counts the combinations).\ntrips: a packing list with dates and a forecast. tick items off as you pack.\nwish list: what you want next, with the price.\n\ntravelling this december? this one's for you.",
  alt='A screen recording of Lists: a capsule with combinations, a trip packing list being ticked off, and the wish list.',
  first_comment='where are you going this december? ✈️',
  stories=[
    {'t': 's_phone', 'title': 'travelling this december?', 'screen': 'l-trip', 'tag': 'poll',
     'do': 'Add a POLL: "yes ✈️" / "staying put".'}])
D[20] = dict(phase='3 · every feature, up close', kind='carousel', theme='travel', title='pack for a trip in 5 steps',
  feed=slides(20, [
    {'t': 'hook', 'kicker': 'holiday packing', 'title': 'pack a whole trip in 5 steps.', 'cutouts': ['tee', 'longsleeve', 'trousers', 'sneakers2', 'denim', 'bag', 'scarf', 'boots']},
    {'t': 'hook', 'kicker': 'step 01', 'title': 'Lists → New trip.', 'sub': 'name it: "Lisbon weekend".'},
    {'t': 'hook', 'kicker': 'step 02', 'title': 'add the dates.', 'sub': 'Wardrobe shows the forecast for day one.'},
    {'t': 'hook', 'kicker': 'step 03', 'title': 'add items, or whole outfits.', 'sub': 'one tap adds every piece of an outfit.'},
    {'t': 'phone', 'title': 'step 04: tick off as you pack.', 'screen': 'l-trip2'},
    {'t': 'hook', 'bg': 'ink', 'kicker': 'step 05', 'title': 'share the list.', 'sub': 'with whoever always asks "did you pack…?"'}]),
  caption="holiday packing in 5 steps with Wardrobe:\n\n01 Lists → New trip\n02 add the dates (it shows the forecast)\n03 add items or whole outfits\n04 tick them off as you pack\n05 share the list\n\nsave this for your next trip 📌",
  alt='Six slides showing how to make a packing list in Wardrobe, with the trip checklist on a phone.',
  first_comment='overpacker or underpacker? be honest.',
  stories=[
    {'t': 's_phone', 'title': 'wish list before you shop', 'sub': 'note it. sleep on it.', 'screen': 'l-wish', 'tag': 'tip',
     'do': 'Add a POLL: "impulse buyer" / "list maker".'}])
D[21] = dict(phase='3 · every feature, up close', kind='reel', theme='money', title='insights', reel='ch7',
  cover={'t': 'cover', 'title': 'your closet, in numbers.', 'kicker': 'how to · 07', 'screen': 'i-top', 'size': 110},
  caption="insights in Wardrobe: your items, outfits, wears and wardrobe value. your colours. what you wear most, the best cost per wear, what's still waiting for a first wear, and what you might consider letting go.\n\nit's a closet audit that does itself.",
  alt='A screen recording of Insights: totals, colours, most worn, cost per wear and suggestions to let go.',
  first_comment='what colour do you think leads your closet? (mine: black, obviously)',
  stories=[
    {'t': 's_phone', 'title': 'guess my top colour', 'screen': 'i-top', 'tag': 'quiz',
     'do': 'Add a QUIZ: "black" (correct) / "navy" / "brown".'}])
D[22] = dict(phase='3 · every feature, up close', kind='post', theme='feature', title='dark mode',
  feed=[{'t': 'twophone', 'bg': 'ink', 'title': 'light, dark,<br>your colour.', 'screens': ['w-dark-rose', 't-dark-rose'], 'labels': ['dark + rose', 'try on, in dark']}],
  caption="Wardrobe has light and dark mode, five accent colours (indigo, emerald, rose, amber, graphite) and your own currency.\n\nsettings → appearance.",
  alt='Two phones showing Wardrobe in dark mode with a rose accent.',
  first_comment='light or dark? there is a correct answer.',
  stories=[
    {'t': 's_phone', 'title': 'light or dark?', 'screen': 's-rose', 'tag': 'poll',
     'do': 'Add a POLL: "light ☀️" / "dark 🌙".'}])
D[23] = dict(phase='3 · every feature, up close', kind='carousel', theme='build', title='build log: how #001 was made',
  feed=slides(23, [
    {'t': 'log', 'title': 'how #001 was built.', 'lines': ['a blank file', 'a closet problem', 'a lot of weird nights']},
    {'t': 'log', 'kicker': 'build log · 01', 'title': 'one html file.', 'lines': ['no app store. no install.', 'open it, add it to your home screen.']},
    {'t': 'log', 'kicker': 'build log · 02', 'title': 'no server.', 'lines': ['everything is stored on your device.', 'there is no account to hack.']},
    {'t': 'log', 'kicker': 'build log · 03', 'title': 'the ai runs on your phone.', 'lines': ['the cut-out model downloads once.', 'your photos never leave.']},
    {'t': 'log', 'kicker': 'build log · 04', 'title': 'backup is one file.', 'lines': ['download it, keep it anywhere,', 'restore it on any phone.']},
    {'t': 'log', 'kicker': 'build log · 05', 'title': 'why?', 'lines': ['because everyday tools should be', 'simple, private and yours.']},
    {'t': 'hook', 'bg': 'ink', 'title': '#002 is already a blank file.', 'tag': 'next', 'sub': 'stay weird. follow along.'}]),
  caption="build log: how #001 was made.\n\none html file. no server. the ai runs on your phone. backup is one file.\n\nwhy? because the tools you use every day should be simple, private and yours.\n\n#002 is already a blank file 👀",
  alt='Seven dark build-log slides about how Wardrobe was made: one HTML file, no server, on-device AI, one-file backup.',
  first_comment='makers: what\'s the weirdest constraint you\'ve built under?',
  stories=[
    {'t': 's_log', 'title': 'what should be weirder?', 'lines': ['i\'m planning #002.', 'tell me what bugs you every day.'], 'sticker': 'question box goes here',
     'do': 'Add a QUESTION sticker: "build me something for…".'}])
# ================= PHASE 4 · your closet, your december (days 24-30) =================
D[24] = dict(phase='4 · your closet, your december', kind='reel', theme='feature', title='make it yours', reel='ch8',
  cover={'t': 'cover', 'title': 'make it yours.', 'kicker': 'how to · 08', 'screen': 's-rose', 'size': 120},
  caption="make Wardrobe yours: light or dark, five accent colours, your own currency.\n\neverything is stored on your device. back it up to a single file and restore it on any phone.\n\nand the whole thing is one html file. no app store, no account.",
  alt='A screen recording of Settings: dark mode, accent colours, and the backup section, ending on the Wardrobe end card.',
  first_comment='which accent are you running?',
  stories=[
    {'t': 's_phone', 'title': 'which colour are you?', 'screen': 's-rose', 'tag': 'poll',
     'do': 'Add a POLL: "indigo" / "rose". Mention the other three in text.'}])
D[25] = dict(phase='4 · your closet, your december', kind='post', theme='feature', title='the 10-piece challenge',
  feed=[{'t': 'list', 'bg': 'ink', 'title': 'the 10-piece challenge', 'items': ['pick 10 pieces in Wardrobe.', 'make a capsule from them.', 'create 10 outfits this week.', 'post your favourite board.', 'tag @wierd_stuff_i_make.'], 'tag': 'challenge'}],
  caption="the 10-piece challenge 🧩\n\npick 10 pieces. make a capsule. create 10 different outfits from them this week. post your favourite board and tag me.\n\ni'll repost every single one.",
  alt='A dark poster with the 10-piece challenge rules: pick 10 pieces, make a capsule, create 10 outfits, post and tag.',
  first_comment='i\'m in. starting tonight. who\'s joining?',
  stories=[
    {'t': 's_cuts', 'title': '10 pieces. 10 outfits.', 'sub': 'this week.', 'items': ['tee', 'longsleeve', 'trousers', 'skirt', 'denim', 'boots'], 'sticker': '"add yours" sticker goes here',
     'do': 'Add an "ADD YOURS" sticker: "my 10-piece challenge".'}])
D[26] = dict(phase='4 · your closet, your december', kind='carousel', theme='feature', title='holiday outfits from what you own',
  feed=slides(26, [
    {'t': 'hook', 'kicker': 'december', 'title': 'holiday outfits from what you already own.', 'cutouts': ['tee', 'skirt', 'boots', 'longsleeve', 'trousers', 'loafer', 'formal', 'scarf']},
    {'t': 'cutgrid', 'title': 'night out', 'sub': 'white tee · pleated skirt · oxblood boots', 'items': ['tee', 'skirt', 'boots']},
    {'t': 'cutgrid', 'title': 'office party', 'sub': 'long-sleeve · rust trousers · tan loafers', 'items': ['longsleeve', 'trousers', 'loafer']},
    {'t': 'cutgrid', 'title': 'family lunch', 'sub': 'white tee · rust trousers · dress shoes', 'items': ['tee', 'trousers', 'formal']},
    {'t': 'cutgrid', 'title': 'cold morning walk', 'sub': 'long-sleeve · denim · boots · scarf', 'items': ['longsleeve', 'denim', 'boots', 'scarf']},
    {'t': 'cta', 'title': 'shop your closet.', 'sub': 'plan every december look in Wardrobe. link in bio.'}]),
  caption="holiday outfits from what you already own:\n\nnight out · office party · family lunch · cold morning walk\n\nall from one closet. plan them in Wardrobe and skip the panic buy.",
  alt='Six slides of holiday outfits made from the same few pieces: night out, office party, family lunch, cold morning walk.',
  first_comment='which look are you wearing first?',
  stories=[
    {'t': 's_cuts', 'title': 'which is the night out look?', 'items': ['tee', 'skirt', 'boots', 'longsleeve', 'trousers', 'loafer'], 'sticker': 'quiz sticker goes here',
     'do': 'Add a QUIZ: "tee + skirt + boots" (correct) / "long-sleeve + trousers + loafers".'}])
D[27] = dict(phase='4 · your closet, your december', kind='video', theme='feature', title='the full tour (4:43)', reel='tour',
  cover={'t': 'cover', 'title': 'every feature,<br>step by step.', 'kicker': 'the full tour · 4:43', 'cutouts': ['tee', 'denim', 'boots'], 'size': 116},
  caption="the full tour: every feature in Wardrobe, step by step, in under 5 minutes.\n\n0:00 the 24-second version\n0:35 add clothes\n1:30 your wardrobe\n2:01 try on\n2:35 outfits\n2:57 plan\n3:22 capsules, trips, wish list\n3:50 insights\n4:11 make it yours\n\nsave it, send it to the friend who always has 'nothing to wear'.",
  alt='A 4 minute 43 second narrated tour of every Wardrobe feature, chapter by chapter.',
  first_comment='if it\'s too long for you, the 24-second version is pinned 📌',
  stories=[
    {'t': 's_phone', 'title': 'the full tour is up', 'sub': '4:43. every feature.', 'screen': 'w-home', 'tag': 'new',
     'do': 'Share today\'s video to your story with the post sticker on top.'}])
D[28] = dict(phase='4 · your closet, your december', kind='post', theme='page', title='thank you',
  feed=[{'t': 'hook', 'bg': 'acc', 'kicker': 'three weeks of #001', 'title': 'thank you for making it weird.', 'sub': 'every question, every board, every closet you shared.', 'tag': 'thank you', 'size': 120}],
  caption="three weeks since #001.\n\nthank you for every question, every outfit board and every 'i didn't know i owned this' message. this page exists because you showed up.\n\n#002 is next. you're choosing it this weekend.",
  alt='A blue poster reading: thank you for making it weird.',
  first_comment='what should #002 fix? best idea goes into tomorrow\'s vote.',
  stories=[
    {'t': 's_hook', 'bg': 'ink', 'title': 'what should #002 be?', 'sticker': 'question box goes here', 'center': True,
     'do': 'Add a QUESTION sticker "build me something for…". Pick 4 ideas for tomorrow.'}])
D[29] = dict(phase='4 · your closet, your december', kind='carousel', theme='page', title='what should i build next?',
  feed=slides(29, [
    {'t': 'hook', 'kicker': 'product #002', 'title': 'you pick what i build next.', 'tag': '#002 · vote'},
    {'t': 'hook', 'kicker': 'idea a', 'title': 'a pantry that knows what\'s about to expire.', 'tag': '#002 · vote'},
    {'t': 'hook', 'kicker': 'idea b', 'title': 'a bill splitter for flatmates that never forgets.', 'tag': '#002 · vote'},
    {'t': 'hook', 'kicker': 'idea c', 'title': 'a plant journal that reminds you to water.', 'tag': '#002 · vote'},
    {'t': 'hook', 'kicker': 'idea d', 'title': 'a gift list for everyone you know.', 'tag': '#002 · vote'},
    {'t': 'hook', 'bg': 'ink', 'title': 'vote in my story.', 'sub': 'or pitch your own in the comments.', 'tag': '#002 · vote'}]),
  caption="you pick #002.\n\na) a pantry that knows what's about to expire\nb) a bill splitter for flatmates\nc) a plant journal that reminds you to water\nd) a gift list for everyone you know\n\nvote in my story. or pitch your own below.",
  alt='Six slides with four ideas for the next product, asking followers to vote in stories.',
  first_comment='or pitch your own 👇',
  stories=[
    {'t': 's_hook', 'title': '#002: round 1', 'sub': 'pantry vs bill splitter', 'sticker': 'poll sticker goes here', 'tag': 'vote',
     'do': 'Before posting, swap the four ideas in the slides and caption for your top four from yesterday\'s question box if you have better ones (edit src/content.py and re-render, or just change the text). Add a POLL: "pantry" / "bill splitter".'},
    {'t': 's_hook', 'title': '#002: round 2', 'sub': 'plants vs gift list', 'sticker': 'poll sticker goes here', 'tag': 'vote',
     'do': 'Add a POLL: "plants" / "gift list". Announce the final tomorrow.'}])
D[30] = dict(phase='4 · your closet, your december', kind='reel', theme='page', title='30 days of #001 (recap)', reel='recap',
  cover={'t': 'cover', 'title': '30 days of #001.', 'kicker': 'recap', 'cutouts': ['tee', 'denim', 'boots'], 'size': 130},
  caption="30 days of #001.\n\na closet on your phone. photos that lose their backgrounds. outfits from what you already own. one html file.\n\nthank you. #002 is coming. stay weird.",
  alt='A 30-second recap of the Wardrobe launch: the cut-out, try on, plan and insights, ending on the Wardrobe end card.',
  first_comment='pin this: Wardrobe is in the bio, always.',
  stories=[
    {'t': 's_cta', 'title': 'thank you.', 'sub': 'Wardrobe stays in my bio.', 'sticker': 'link sticker goes here',
     'do': 'Add a LINK sticker. Then post the #002 vote winner as text.'},
    {'t': 's_countdown', 'big': '#002', 'title': 'coming soon', 'kicker': 'next', 'size': 260, 'sticker': 'countdown sticker goes here',
     'do': 'Add a COUNTDOWN "#002" with no end date (or your real date). Save to the "next" highlight.'}])

# ================= the 7-day launch: tease (1-2), launch (3), features (4-6), black friday close (7) =================
import copy
C = copy.deepcopy
TAGS['launch3'] = TAGS_CORE + ' #shopyourcloset #sustainablefashion #slowfashion #outfitideas #newapp'
W = {}
W[1] = C(D[1]); W[1]['phase'] = '1 · tease'
W[1]['feed'][3]['title'] = 'lands monday,<br>23 november.'
W[1]['caption'] = W[1]['caption'].replace('the first one lands friday, 27 november.', 'the first one lands monday, 23 november.')
W[1]['stories'] = C(D[1]['stories']) + [dict(C(D[3]['stories'][1]), big='2', title='days to #001',
    do='Add a COUNTDOWN sticker named "product #001" ending Mon 23 Nov, 7:00 pm. Keep this frame for the Highlights later.')]
W[2] = dict(phase='1 · tease', kind='reel', theme='teaser', title='teaser: nothing to wear? photo in, background out', reel='teaser',
  cover={'t': 'cover', 'title': 'nothing to wear?', 'kicker': '#001 · 23.11', 'cutouts': ['tee', 'denim', 'boots'], 'size': 130},
  caption="you know the feeling. full closet, nothing to wear.\n\nso i built something: take a photo of any piece and the background disappears, right on your phone. that's one tiny part of it.\n\nproduct #001. tomorrow, monday 23.11, 7 pm.",
  alt='Clothes drop around the words "Nothing to wear?", a photo of a t-shirt becomes a clean cut-out, then a card: product #001, Monday 23 November.',
  first_comment='guess what #001 is. closest guess gets a shout-out tomorrow.',
  stories=[dict(C(D[5]['stories'][0]), sub='tomorrow.'), C(D[6]['stories'][0]), C(D[6]['stories'][1])])
W[2]['stories'][1]['do'] = 'Re-add the "product #001" COUNTDOWN sticker so people can tap "remind me".'
W[3] = C(D[7]); W[3]['phase'] = '2 · launch'; W[3]['theme'] = 'launch3'
W[3]['caption'] = W[3]['caption'].replace("\n\nit's black friday. before you buy more clothes, see what you already own. link in bio.", "\n\nbefore you buy more clothes, see what you already own. link in bio.")
W[3]['stories'][1] = {'t': 's_phone', 'title': 'your closet, on your phone.', 'sub': 'what will you add first?', 'screen': 'w-home', 'tag': 'poll',
                      'do': 'Add a POLL: "my favourite jacket" / "the thing i never wear".'}
W[4] = C(D[9]); W[4]['phase'] = '3 · every feature'
W[4]['stories'] = C(D[9]['stories']) + C(D[8]['stories'])
W[5] = C(D[8]); W[5]['phase'] = '3 · every feature'
W[5]['stories'] = C(D[17]['stories']) + C(D[11]['stories'])
W[6] = C(D[13]); W[6]['phase'] = '3 · every feature'
W[6]['caption'] = W[6]['caption'].replace('your launch-week questions, answered:', 'your launch questions, answered:')
W[6]['feed'][0]['sub'] = 'the questions from launch.'
W[6]['stories'] = C(D[13]['stories']) + [dict(C(D[10]['stories'][0]), title='tomorrow: Style me', do='Add a QUIZ sticker: "white tee + pleated skirt" (correct) / "hoodie + trousers" / "denim on denim". Hints at tomorrow\'s reel.')]
W[7] = C(D[10]); W[7]['phase'] = '4 · black friday close'; W[7]['theme'] = 'launch'
W[7]['title'] = 'black friday: shop your own closet first'
W[7]['cover'] = {'t': 'cover', 'title': 'shop your closet first.', 'kicker': 'black friday · try on', 'screen': 't-style', 'size': 110}
W[7]['caption'] = ("it's black friday. before you buy another outfit, let your closet try first.\n\nin Try on, tops, bottoms and shoes sit in rows at their real size. swipe to mix and match, "
  "lock a piece you love, or tap Style me: it picks a combination whose colours work together, suited to the season and the weather.\n\nshop your own closet first. Wardrobe is in the bio.")
W[7]['first_comment'] = 'found an outfit you forgot you had? post it and tag me 🖤'
W[7]['stories'] = [dict(C(D[7]['stories'][1]), do='Add a POLL: "buying anything today?" "yes 🛍️" / "checking my closet first".'),
                   dict(C(D[30]['stories'][0]), title='thank you for week one.', sub='Wardrobe stays in my bio.', do='Add a LINK sticker to the app.'),
                   C(D[28]['stories'][0])]
HIGHLIGHT_OF = {1: 'hello', 2: '#001', 3: '#001', 4: 'how to', 5: 'how to', 6: 'faq', 7: 'next'}

def emit(n, x, folder, d=None, label=''):
    feed_files, story_files = [], []
    if x['kind'] in ('carousel', 'post'):
        for i, s in enumerate(x['feed']):
            p = f'{folder}/feed/{"slide" if x["kind"] == "carousel" else "post"}-{i + 1:02d}.png'; A(p, s, 1080, 1350); feed_files.append(p)
    else:
        A(f'{folder}/feed/cover.png', x['cover'], 1080, 1920); feed_files += [f'{folder}/feed/cover.png', f'{folder}/feed/{x["reel"]}.mp4']
    for i, s in enumerate(x.get('stories', [])):
        p = f'{folder}/story/story-{i + 1:02d}.png'; spec = {k: v for k, v in s.items() if k != 'do'}; A(p, spec, 1080, 1920); story_files.append(p)
    return {'day': n, 'date': d.isoformat() if d else '', 'label': label, 'folder': folder, 'phase': x['phase'], 'kind': x['kind'], 'title': x['title'],
            'time': TIMES[x['kind']], 'story_time': STORY_TIME, 'reel': x.get('reel'), 'feed': feed_files, 'stories': story_files,
            'story_do': [s['do'] for s in x.get('stories', [])], 'caption': x['caption'], 'hashtags': TAGS[x['theme']], 'alt': x['alt'],
            'first_comment': x['first_comment'], 'highlight': HIGHLIGHT_OF.get(n, '') if d else ''}

for n in range(1, 8):
    d, label = day(n); plan.append(emit(n, W[n], f'Day{n:02d}_{d.strftime("%a-%d-%b")}', d, label))

# the after-launch library: finished posts that didn't fit the week, ready to use from day 8 on
BONUS = [(14, 'reel_your-wardrobe'), (11, 'carousel_perfect-cutout'), (16, 'reel_outfits'), (15, 'carousel_capsule-101'), (12, 'reel_plan-the-week'),
         (18, 'carousel_cost-per-wear'), (19, 'reel_trips-and-lists'), (20, 'carousel_packing'), (21, 'reel_insights'), (23, 'carousel_build-log'),
         (24, 'reel_make-it-yours'), (26, 'carousel_holiday-outfits'), (17, 'post_before-after'), (22, 'post_dark-mode'), (25, 'post_10-piece-challenge'), (27, 'video_full-tour')]
bonus = []
for i, (k, name) in enumerate(BONUS):
    x = C(D[k]); x['stories'] = []; bonus.append(emit(i + 1, x, f'after-launch-library/{i + 1:02d}_{name}'))
json.dump(bonus, open(f'{OUT}/bonus.json', 'w'), indent=1, ensure_ascii=False)

# ---------- profile, highlights, reel end cards ----------
A('profile/profile-picture.png', {'t': 'avatar'}, 1080, 1080)
A('profile/profile-picture-mono.png', {'t': 'avatar', 'cursor': 'var(--paper)'}, 1080, 1080)
ICONS = {
  'hello': '<div style="font:800 300px/1 Bricolage Grotesque;color:#ECEEF2;letter-spacing:-.04em">hi</div>',
  '#001': '<svg width="360" height="360" viewBox="0 0 24 24" fill="none" stroke="#3D4FE0" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7.5V6a2 2 0 1 0-2-2"/><path d="M12 7.5 3.5 14a1.5 1.5 0 0 0 .9 2.7h15.2a1.5 1.5 0 0 0 .9-2.7z"/></svg>',
  'how to': '<div style="font:500 230px/1 DM Mono;color:#ECEEF2">1-2-3</div>',
  'faq': '<div style="font:800 380px/1 Bricolage Grotesque;color:#ECEEF2">?</div>',
  'build log': '<div style="font:500 300px/1 DM Mono;color:#A5BBFF">&gt;_</div>',
  'you': '<div style="font:800 300px/1 Bricolage Grotesque;color:#ECEEF2;letter-spacing:-.04em">you</div>',
  'next': '<div style="font:500 210px/1 DM Mono;color:#ECEEF2">#002</div>'}
for k, ic in ICONS.items():
    A(f'profile/highlight-covers/{k.replace("#", "").replace(" ", "-")}.png', {'t': 'highlight', 'icon': ic.replace('font:', 'font:').replace('Bricolage Grotesque', "'Bricolage Grotesque'").replace('DM Mono', "'DM Mono'")}, 1080, 1920)
A('_build/endcard.png', {'t': 'endcard'}, 1080, 1920)
A('_build/tease.png', {'t': 'teasecard', 'title': 'monday, 23.11', 'size': 120}, 1080, 1920)

json.dump(assets, open(f'{OUT}/assets.json', 'w'), indent=1)
json.dump(plan, open(f'{OUT}/plan.json', 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(len(assets), 'images;', Counter(p['kind'] for p in plan), sum(len(p['stories']) for p in plan), 'story frames;', len(bonus), 'library posts')
