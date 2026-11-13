# The explainer's soundtrack: the cold open's finished mix (0-24.233 s), then "Pop" (Andrew Ev, Mixkit) under the
# chapters, started 0.963 s in so its own last hit (254.443 s) lands on the end card's name; the Kokoro narration on
# each beat; recorded Mixkit effects on the picture's actions. The bed dips 10 dB under the voice. Mastered to -14 LUFS.
import json, subprocess, numpy as np, soundfile as sf
SR = 48000
D = '/home/user/Image-Scanner/brag-output/explainer'
FILM = '/home/user/Image-Scanner/brag-output/film/wardrobe'
COLD = 727 / 30
TL = json.load(open(f'{D}/timeline.json'))
BODY = TL['total']; TOTAL = COLD + BODY; N = int(round(TOTAL * SR))

def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def rms_db(x): return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
def place(dst, x, t, g=1.0):
    s = int(round(t * SR))
    if s < 0: x = x[-s:]; s = 0
    m = min(len(x), len(dst) - s)
    if m > 0: dst[s:s + m] += x[:m] * g

cold = load('/home/user/Image-Scanner/brag-output/work/mix.wav')[:int(COLD * SR)]
body_n = N - int(COLD * SR)
music = load(f'{D}/music/pop_mixkit.mp3')[int(0.963 * SR):int(0.963 * SR) + body_n]
music = np.pad(music, ((0, body_n - len(music)), (0, 0)))
fi = int(0.6 * SR); music[:fi] *= np.linspace(0, 1, fi)[:, None]
music[-int(0.6 * SR):] *= np.linspace(1, 0, int(0.6 * SR))[:, None] ** 2

voice = np.zeros((body_n, 2), np.float32); vmask = np.zeros(body_n, np.float32)
for b in TL['T']:
    if b.get('voAt') is None or not b.get('vo'): continue
    x = load(f'{D}/vo/{b["id"]}.wav'); x *= 10 ** ((-17 - rms_db(x[np.abs(x[:, 0]) > 0.01])) / 20)
    s = int(b['voAt'] * SR); m = min(len(x), body_n - s); voice[s:s + m] += x[:m]; vmask[s:s + m] = 1
w = int(0.2 * SR); k = np.convolve(vmask, np.ones(w) / w, 'same')
duck = 10 ** ((-10 * np.clip(k * 1.5, 0, 1)) / 20)
bed = music * 10 ** (-5 / 20) * duck[:, None]

lock = json.load(open(f'{FILM}/audio/kit/real.lock.json'))['roles']
ROLE = {'whoosh': 'whoosh.short', 'sheet': 'land.light', 'scan': 'whoosh.long', 'click': 'click', 'swipe': 'whoosh.short', 'drop': 'land.light',
        'swell': 'swell', 'hit': 'hit', 'land': 'land', 'bell': 'bell', 'snap': 'snap'}
fx = np.zeros((body_n, 2), np.float32); used = 0
for n, e in enumerate(TL['ev']):
    role = ROLE.get(e['kind']); r = lock.get(role) if role else None
    if not r: continue
    tk = r['takes'][n % len(r['takes'])]
    x = load(f'{FILM}/audio/kit/{tk["file"]}')[: int(SR * (2.0 if role in ('swell', 'whoosh.long') else 0.9))]
    fl = min(len(x), int(0.08 * SR)); x[-fl:] *= np.linspace(1, 0, fl)[:, None]
    start = (e['t'] - tk['peak_s']) if role in ('swell',) else e['t'] - tk['onset_s']
    level = -27 + 8 * e['w'] - (3 if e['kind'] in ('swipe', 'drop') else 0)
    place(fx, x, start, 10 ** ((level - tk['lufs_m_max']) / 20)); used += 1

body = bed + voice + fx
out = np.concatenate([cold, body])[:N]
sf.write(f'{D}/mix-raw.wav', out, SR)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{D}/mix-raw.wav', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '48000', f'{D}/mix.wav'], check=True)
print(f'mixed {TOTAL:.2f} s: cold open {COLD:.2f} s + body {BODY:.2f} s, {used} effects')
