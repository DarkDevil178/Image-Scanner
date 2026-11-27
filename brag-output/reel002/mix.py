# #002 launch reel sound: "Funky Martian" (Mixkit) placed so its last hit lands on the stamp (27.0 s); the founder
# voice (Kokoro af_heart) levelled to -16 dB RMS, the funk ducking under it; the picked effects (riser, glitch zap,
# camera shutter, notification ding) plus the cooker whistle and a tape rewind on their picture cues; -14 LUFS.
import subprocess, numpy as np, soundfile as sf
R = '/home/user/Image-Scanner/brag-output/reel002'; WH = '/home/user/Image-Scanner/brag-output/whistle'; J = '/home/user/Image-Scanner/brag-output/journey'
KIT = '/home/user/Image-Scanner/brag-output/film/wardrobe/audio/kit'
SR, TOTAL, LAST_HIT, END_HIT = 48000, 30.0, 96.986, 27.0
def load(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def rms_db(x): return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
N = int(TOTAL * SR)
s0 = LAST_HIT - END_HIT; mus = load(f'{R}/audio/music/funky_martian_mixkit.mp3')[int(s0 * SR):int(s0 * SR) + N]; mus = np.pad(mus, ((0, N - len(mus)), (0, 0)))
# the hook plays the alarm first: the funk enters under the rewind, from 1.6 s, and drops out for the rewind's first half beat
env = np.ones(N, np.float32); a, b = int(1.4 * SR), int(1.9 * SR); env[:a] = .25; env[a:b] = np.linspace(.25, 1, b - a)
mus *= env[:, None]; g = int(.6 * SR); mus[-g:] *= np.linspace(1, 0, g)[:, None]
VO = [('R1', 1.75), ('R2', 3.95), ('R3', 8.0), ('R4', 10.15), ('R5', 12.15), ('R6', 16.25), ('R7', 18.4), ('R8', 20.4), ('R9', 24.55), ('R10', 27.15)]
voice = np.zeros((N, 2), np.float32); vm = np.zeros(N, np.float32)
for v, t in VO:
    x = load(f'{R}/vo/{v}.wav'); x *= 10 ** ((-16 - rms_db(x[np.abs(x[:, 0]) > 0.01])) / 20); s = int(t * SR); m = min(len(x), N - s); voice[s:s + m] += x[:m]; vm[s:s + m] = 1
w = int(.25 * SR); k = np.convolve(vm, np.ones(w) / w, 'same'); duck = 10 ** ((-9 * np.clip(k * 1.5, 0, 1)) / 20)
bed = mus * 10 ** (-4 / 20) * duck[:, None]
SFX = {'ding': f'{R}/audio/sfx/m2867.wav', 'tone': f'{R}/audio/sfx/m2866.wav', 'glitch': f'{R}/audio/sfx/m1031.wav', 'glitch2': f'{R}/audio/sfx/m1021.wav',
       'rewind': f'{R}/audio/sfx/m1092.wav', 'shutter': f'{R}/audio/sfx/m1133.wav', 'riser': f'{R}/audio/sfx/m790.wav', 'whistle': f'{WH}/sfx/cooker-whistle.wav',
       'whoosh': f'{J}/audio/sfx/m1464.wav', 'tap': f'{KIT}/real-click_1.wav', 'hit': f'{KIT}/real-hit_1.wav', 'alarm': f'{WH}/sfx/stopwatch-alert.wav'}
CUES = [('whistle', 0.0, .55, .9), ('ding', 0.08, .6), ('glitch', 1.55, .6), ('rewind', 1.6, .5), ('glitch2', 3.68, .45),
        ('whistle', 4.95, .4, .55), ('whistle', 5.7, .4, .55), ('whistle', 6.3, .45, .7), ('glitch', 7.84, .35),
        ('whoosh', 9.72, .5), ('shutter', 9.93, .7), ('tap', 12.85, .55), ('whistle', 14.38, .45, .6), ('whistle', 15.33, .45, .6), ('whistle', 16.0, .5, .8),
        ('ding', 16.2, .6), ('whoosh', 18.0, .5), ('riser', 17.7, .45), ('glitch2', 20.25, .35)] + \
       [('tone', 20.27 + .7 * i, .22) for i in range(6)] + [('glitch', 24.39, .35), ('hit', 27.0, .7), ('ding', 27.05, .45)]
fx = np.zeros((N, 2), np.float32)
for e in CUES:
    kind, t, gain = e[:3]; x = load(SFX[kind])
    if len(e) > 3: L = int(e[3] * SR); x = x[:L].copy(); ff = min(len(x), int(.2 * SR)); x[-ff:] *= np.linspace(1, 0, ff)[:, None]
    x = x / (np.max(np.abs(x)) + 1e-9) * gain * .55; s = int(t * SR); m = min(len(x), N - s); fx[s:s + m] += x[:m]
sf.write(f'{R}/work/mix-raw.wav', bed + voice + fx, SR)
print('raw written')
