# Handoff: @wierd_stuff_i_make launch work (from the Image-Scanner session)

Paste this into a new session or repo to carry the context over.

## The page
- Instagram page **@wierd_stuff_i_make**. Keep that spelling: "wierd", not "weird". In the name field, write "weird stuff i make" so people searching the usual spelling still find the page.
- The idea: useful things, built from scratch, for everyday use. Every product gets a number: **#001, #002, … up to #999**.
- Rules: no founder name, Instagram only, "link in bio" (never a URL in a caption), lowercase captions, no hype words, no made-up numbers.
- **Brand: ink on paper, and each product brings its own colour.**
  - Ink `#161922`, paper `#ECEEF2`, grey `#7C8494`.
  - Fonts: Bricolage Grotesque 800 for headlines, DM Sans 500 for text, DM Mono 500 for the handle, numbers and tags.
  - Page mark: a "w" on an ink tile with a cursor bar after it. The cursor takes the current product's colour. Between launches it goes paper-coloured.
- **#001 Wardrobe**: indigo `#3D4FE0` (lighter `#A5BBFF`), hanger mark. Your closet on your phone: one html file, no account.
- **#002 Cooker Whistle Counter**: the app's orange `#FF8A3D`. Use deep `#D9600F` for orange text on paper and lifted `#FFB07A` on dark. Cooker mark.
  - Counts pressure-cooker whistles through the microphone, then sounds an alarm and vibrates.
  - "Learn my whistle" tunes it to your own cooker. Also: presets, a backup timer and a separate Timer.
  - Six languages: English, தமிழ், हिन्दी, తెలుగు, മലയാളം, ಕನ್ನಡ.
  - Works offline, made for Chrome on Android. Live at https://darkdevil178.github.io/Whistle-counter-/
  - Honest limits: keep the screen on (counting pauses if it turns off), and keep the phone away from fans.

## What was made (all in `brag-output/`)
| Folder | What |
|---|---|
| `film/`, `cinematic/`, `combined/`, `feature-explainer/`, `explainer/` | #001 Wardrobe films: the /brag video, the cinetic film, a 24 s combined film with voiceover (16:9 and 9:16), and a 4:43 feature explainer (16:9 and 9:16). |
| `launch-kit/` | #001 7-day Instagram kit (Sat 21 – Fri 27 Nov 2026, launch Mon 23 Nov). Generators are in `src/`; the zip and `out/` stay local. |
| `whistle/` | #002 cinematic reels engine. `reel.html` is a frame-pure HTML engine; `reels_w.py` holds the specs and the mix; `render_reel.js` renders. Four reels: teaser (11 s), launch (25 s), how-to (33 s), languages (13.5 s). App captures were made with a fake microphone driving the real app (`work/capture.js`, `work/whistle_audio.py`). |
| `launch-kit-002/` | #002 6-day kit (Sat 28 Nov – Thu 3 Dec 2026, launch Mon 30 Nov, 7 pm). Tease 28–29, launch 30, explain 1–2 Dec, close 3 Dec. Built with `src/make_templates.py`, `content.py`, `render.js`, `docs.py`, `logos.js`, `pdf.js` and `package.sh`. |
| `journey/` | The "999" page film, in a paper-cut style. `film.html` is the 16:9 film; `make_vertical.py` builds `film-v.html` (9:16); `make_dark.py` adds the dark, cinematic, stop-motion pass; `mix.py` makes the sound (set `NOVO=1` for no narration); `render.js` renders, controlled by the `V`, `FILM`, `OUT` and `TAG` env settings. **Committed: `journey/out/wierd_stuff_i_make_999-journey_dark_9x16.mp4`.** |

## The "999" film (the latest)
- **Story:** one paper tag carries the whole film. It's cut from a sheet ("i make useful things." → "from scratch."), becomes #001 Wardrobe, then #002 Cooker Whistle Counter, then counts to "999 projects." inside a wall of tags, then becomes the #1000 flag at the end of a path ("be a part of the journey." / "what happens after that?" / "let's find out together."), then floods into the page mark. The end card says "#001 → #999 · follow along".
- **Final look:** dark paper, stop-motion on twos (12 fps steps with a slight boil), a key light that drifts, a vignette, dust in the light, film grain, and a moon instead of a sun.
- **Sound:**
  - Music: "A Happy Child" by Diego Nava (Mixkit, no credit needed), placed so its last hit lands on the end card at 27.0 s.
  - Effects: Mixkit paper sounds.
  - Narration: Kokoro TTS voice `af_heart`, which the user liked; keep it.
  - Mastered to -14 LUFS.
- **Rebuild the vertical dark version:**
  1. `python3 make_vertical.py && python3 make_dark.py film-v.html film-v-dark.html`
  2. `V=1 FILM=film-v-dark.html OUT=frames-vd node render.js frames`
  3. `python3 mix.py`
  4. `ffmpeg -framerate 30 -i work/frames-vd/f%05d.jpg -i work/mix.wav … out/…_dark_9x16.mp4`

## Tools and setup
- **Skills:**
  - `brag` is installed globally at `~/.agents/skills/brag`, linked into `~/.claude/skills`. Reinstall with `npx -y skills add https://github.com/latent-spaces/brag --skill brag -g -y`.
  - `cinetic` lives in `~/.claude/skills/cinetic`; it was installed from the user's cinetic zip (version 1.5.1).
- **Machine tools:**
  - Playwright Chromium is preinstalled.
  - The Kokoro model is at `/root/.cache/hyperframes/tts/models/kokoro-v1.0.onnx`, voices at `/root/.cache/hyperframes/tts/voices/voices-v1.0.bin` (Python package `kokoro-onnx`).
  - Indian-script fonts need `fonts-noto-core`.
- **Licensing:**
  - Photos are public domain or CC0, with private records in `whistle/assets/licences.json`.
  - Music and effects are from Mixkit (no credit needed).
  - Licensed audio files are never committed; only their licence `.json` files are.
- **Git:** work branch `ccr-4100c23f-r0lfmx` on DarkDevil178/Image-Scanner. Large outputs are gitignored.

## Open ideas
- Add the brag install to the cloud environment's setup script so it's there in every session.
- #003: the day-6 story of the #002 kit asks followers "what should #003 fix?". Use their answers.
