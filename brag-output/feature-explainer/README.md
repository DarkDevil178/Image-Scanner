# Wardrobe: every feature, step by step

| File | Format |
|---|---|
| `wardrobe-features-16x9.mp4` | 1920x1080, 30 fps, 4:42.8, H.264 BT.709, AAC, -15.8 LUFS / -1.6 dB peak |
| `wardrobe-features-9x16.mp4` | 1080x1920, the same film laid out for vertical |
| `poster-16x9.jpg`, `poster-9x16.jpg` | the intro frame, also baked in as frame 0 |

## Chapters
| Time | Chapter | What it shows |
|---|---|---|
| 0:00 | Cold open | the 24-second launch film (/brag + cinetic) |
| 0:24 | Every feature, step by step | the 14 real cutouts land, the app opens |
| 0:35 | 1. Add clothes | the photo guide, Smart AI cutting the background away on the phone, eraser and restore, the details form, real length for true scale, Save to wardrobe |
| 1:30 | 2. Your wardrobe | categories and today's outfit, search, a piece's details with cost per wear, Wore today |
| 2:01 | 3. Try on | rows at real size, swiping, lock, shuffle, jackets and accessories, Style me, the thumbs-down |
| 2:35 | 4. Outfits | the board (move, resize, background), saving, the outfit sheet |
| 2:57 | 5. Plan | agenda and month, the forecast per day, Style me on an empty day, Mark as worn |
| 3:22 | 6. Capsules, trips and wishes | a capsule and its combinations, a trip packing list, the wish list |
| 3:50 | 7. Insights | items, outfits, wears, wardrobe value, colours, most worn, cost per wear, letting go |
| 4:11 | 8. Make it yours | light and dark, accent colours, currency, backup to one file |
| 4:37 | End card | Wardrobe, one HTML file, no account |

## How it was made
- Every screen is the real app (`work/wardrobe.html`) driven by Playwright with a fictional demo wardrobe:
  14 photographs (public domain, CC0 and Burst), each cut out by Wardrobe's own Smart AI, five outfits,
  three weeks of logged wears, a capsule, a trip, a wish list. The forecast is a real Open-Meteo forecast for Lisbon.
- Motion: real screen states joined with the app's own pushes and sheets, finger taps and swipes, smooth scrolls of
  tall captures, a camera that zooms into the UI, Try on rows built from the app's own rendered strips.
- Narration: 25 lines, Kokoro-82M ("af_heart") via `hyperframes tts`, as /brag's voice option does.
- Music: "Pop" by Andrew Ev (Mixkit Stock Music Free License), started so its own last hit lands on the end card;
  the bed dips under the voice. Effects: Mixkit recordings on taps, swipes, sheets, cards and the end card.
- The cold open is the combined launch film from `../combined/`.
- Source: `../explainer/` (script.json, capture.js, seed.js, explainer.html, render.js, mix.py, assemble.sh).
