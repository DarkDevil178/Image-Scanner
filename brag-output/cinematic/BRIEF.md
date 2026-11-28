# Wardrobe: launch film

Spec: 1920x1080@30, ~24s, format: launch, audio: licensed track + launch kit. Variants 9:16, 1:1, poster.

## Product
Wardrobe is a single-file mobile web app (one HTML file, no account, no app store) for the clothes you own.
- Add clothes: photograph a T-shirt, trousers or shoes. "The background is removed for you." Smart AI runs on the phone.
- Wardrobe: every piece in one closet, sorted by Tops, Bottoms, Shoes, Jackets, Accessories.
- Try on: swipe tops, bottoms and shoes into an outfit, kept to real scale. "Style me" picks a colour-matched outfit.
- Plan: put outfits on days of the week; "Mark as worn".
The product's own strings (use only these in UI): "Add clothes", "Take or choose a photo", "Cutting out…", "Save to wardrobe",
"Saved to wardrobe", "Try on", "Style me", "Create outfit", "Plan", "Mark as worn", "✓ Worn", "Tops", "Bottoms", "Shoes",
"Today: Weekend easy", "Tomorrow: Breton day", "Friday: Dinner out", "18 items and 6 outfits".

## Supplied brand (wins over house taste)
- Colours from the app's CSS: background #eceef2, surface #ffffff, ink #161922, secondary #3c4150, muted #7c8494,
  line #dfe2e8, accent #3d4fe0 (an indigo: the brand's own accent; supplied, so the house indigo ban does not apply).
- Type: Bricolage Grotesque (display, 700) + DM Sans (UI) as the app loads them.
- Mark: the app's own hanger icon (stroke SVG, accent).
- Screens: real captures of the app with a fictional demo wardrobe (brand-kit/screenshots).

## Supplied work
The /brag run (../../brag-plan.md, ../../work): seeded app captures, Try on row strips, the editor, the plan.
Demo data is fictional; no real user data.

## Hard bans
House bans apply except the supplied indigo accent. No generated music. No credits in the picture.
No emoji in our own lines (the app's "✨ Style me" button is its own string and appears only inside the UI).

## Deviations from the deal (with reasons)
- World: the collage direction dealt `blackField`; set to `nearWhite` by hand because the supplied brand is a light app
  (paper #eceef2, white cards) and its UI vanishes on black. `deck.py --redraw palette` does not move the world.
- Scene redraws (in src/spine.ts with `why`): closet -> card-rivers, outfit -> object-window, week -> phone-pullback.
- Brand-supplied markers: the indigo accent and the app's checkerboard colour (#eef0f3).
