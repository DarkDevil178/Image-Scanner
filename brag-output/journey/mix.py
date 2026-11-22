# The 999 film's sound: the licensed track placed so its own last hit lands on the end flood (27.0 s) and rings out,
# Kokoro narration levelled to -17 dB RMS with the bed dipping under it, recorded Mixkit paper effects on the picture's
# cues, the #002 cooker whistle; mastered to -14 LUFS with a limiter under -1.5 dBTP.
import subprocess, numpy as np, soundfile as sf
J = '/home/user/Image-Scanner/brag-output/journey'; WH = '/home/user/Image-Scanner/brag-output/whistle'
KIT = '/home/user/Image-Scanner/brag-output/film/wardrobe/audio/kit'
SR, TOTAL, LAST_HIT, END_HIT = 48000, 32.0, 106.637, 27.0
def load(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def rms_db(x): return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
N = int(TOTAL * SR)
s0 = LAST_HIT - END_HIT; mus = load(f'{J}/audio/music/a_happy_child_mixkit.mp3')[int(s0 * SR):int(s0 * SR) + N]; mus = np.pad(mus, ((0, N - len(mus)), (0, 0)))
f = int(0.3 * SR); mus[:f] *= np.linspace(0, 1, f)[:, None]; g = int(0.8 * SR); mus[-g:] *= np.linspace(1, 0, g)[:, None]
VO = [('V1', 0.75), ('V2', 4.15), ('V3', 9.6), ('V4', 14.75), ('V5', 20.65), ('V6', 23.65)]
voice = np.zeros((N, 2), np.float32); vm = np.zeros(N, np.float32)
for v, t in VO:
    x = load(f'{J}/vo/{v}.wav'); x *= 10 ** ((-17 - rms_db(x[np.abs(x[:, 0]) > 0.01])) / 20); s = int(t * SR); m = min(len(x), N - s); voice[s:s + m] += x[:m]; vm[s:s + m] = 1
w = int(0.25 * SR); k = np.convolve(vm, np.ones(w) / w, 'same'); duck = 10 ** ((-9 * np.clip(k * 1.5, 0, 1)) / 20)
bed = mus * 10 ** (-5 / 20) * duck[:, None]
SFX = {'slide': f'{J}/audio/sfx/m1530.wav', 'move': f'{J}/audio/sfx/m2380.wav', 'pages': f'{J}/audio/sfx/m2386.wav', 'slice': f'{J}/audio/sfx/m2384.wav',
       'chime': f'{J}/audio/sfx/m3108.wav', 'whoosh': f'{J}/audio/sfx/m1464.wav', 'whistle': f'{WH}/sfx/cooker-whistle.wav', 'ignite': f'{WH}/sfx/gas-ignite.wav',
       'hit': f'{KIT}/real-hit_1.wav', 'tap': f'{KIT}/real-click_1.wav'}
CUES = [('pages', .35, .5), ('slide', .45, .45), ('slice', 2.35, .45), ('slice', 2.75, .4), ('slice', 3.1, .4), ('move', 3.3, .55),   # the sheet, the cut, the lift
        ('slide', 3.95, .4), ('tap', 4.25, .35), ('tap', 4.7, .35), ('tap', 5.15, .35), ('tap', 5.6, .35), ('tap', 6.05, .35),          # the rail, five hangers
        ('pages', 6.65, .5), ('whoosh', 9.04, .55), ('ignite', 9.4, .5), ('whistle', 11.0, .5, 1.0), ('whistle', 11.9, .5, 1.0), ('whistle', 12.78, .55, 1.3),
        ('move', 14.6, .45), ('pages', 14.9, .4), ('pages', 15.9, .35), ('pages', 16.9, .35), ('slice', 17.6, .3), ('hit', 18.15, .6),
        ('slide', 19.92, .6), ('whoosh', 19.95, .4), ('move', 20.4, .4), ('hit', 27.0, .55), ('chime', 27.05, .45)]
fx = np.zeros((N, 2), np.float32)
for e in CUES:
    kind, t, gain = e[:3]; x = load(SFX[kind])
    if len(e) > 3: L = int(e[3] * SR); x = x[:L].copy(); ff = min(len(x), int(.25 * SR)); x[-ff:] *= np.linspace(1, 0, ff)[:, None]
    x = x / (np.max(np.abs(x)) + 1e-9) * gain * .55; s = int(t * SR); m = min(len(x), N - s); fx[s:s + m] += x[:m]
sf.write(f'{J}/work/mix-raw.wav', bed + voice + fx, SR)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{J}/work/mix-raw.wav', '-af', 'loudnorm=I=-14:TP=-2:LRA=11,alimiter=limit=0.8', '-ar', '48000', f'{J}/work/mix.wav'], check=True)
print('mix written')
