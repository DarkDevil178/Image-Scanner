# #002 reels: teaser, launch, how-to, languages. Picture: reel.html (photo plates, the real app's captured frames,
# type events, seams). Sound: the licensed track (its own last hit on the end card), the Kokoro narration, recorded
# Mixkit kitchen effects and the cooker whistle; the bed dips under the voice; mastered to -14 LUFS / -1.5 dBTP.
import json, subprocess, os, sys, numpy as np, soundfile as sf
W = '/home/user/Image-Scanner/brag-output/whistle'; SR = 48000; FPS = 30
KIT = '/home/user/Image-Scanner/brag-output/film/wardrobe/audio/kit'
MUSIC = f'{W}/music/just_keep_walking_mixkit.mp3'; LAST_HIT = 121.253
START, LEARN = (195, 801), (326, 729)

REELS = {
 'teaser': dict(total=11.0, end_hit=8.35, shots=[
   dict(at=0.0, photo='cooker1.jpg', z0=1.0, z1=1.18, steam=True, t1=dict(text="who's counting<br>the whistles?", y=700, size=118, **{'in': 0.4})),
   dict(at=3.4, photo='flame2.jpg', z0=1.05, z1=1.16, grade=0.8, big=[[0, '1'], [1.6, '2'], [3.2, '3']], bigY=420),
   dict(at=8.3, end=dict(tease='monday,<br>30.11'))],
   sfx=[('gas-ignite', 0.25, 0.8), ('gas-hum', 0.0, 0.35, 8.3), ('whistle', 3.25, 0.9, 1.4), ('whistle', 4.85, 0.9, 1.4), ('whistle', 6.45, 0.95, 1.6), ('hit', 8.32, 0.7)], vo=[]),
 'launch': dict(total=25.4, end_hit=20.3, shots=[
   dict(at=0.0, photo='cooker1.jpg', z0=1.0, z1=1.14, steam=True, t1=dict(text='lost count<br>again?', y=640, size=140, **{'in': 0.5})),
   dict(at=3.0, screen='idle.png', rise=True, taps=[[1.7, *START]], t1=dict(text='meet Cooker<br>Whistle Counter.', y=150, size=96)),
   dict(at=5.2, seam='cut', run=[0.4, 3.6], pre='idle.png', t1=dict(text='it listens.', y=180, size=96)),
   dict(at=6.6, run=[3.95, 5.25], zoom=[[0, 1.9, 172, 198]], ps=1.55, t1=dict(text='it counts<br>every whistle.', y=150, size=96, out=3.5)),
   dict(at=7.9, seam='whip', run=[10.95, 12.25], zoom=[[0, 1.9, 172, 198]]),
   dict(at=9.2, seam='whip', run=[17.95, 18.95], zoom=[[0, 1.9, 172, 198]]),
   dict(at=10.2, fill='run/r0300.png'),
   dict(at=12.8, seq=[[0, 'learnrun/l0010.png'], [0.9, 'learnrun/l0040.png'], [2.7, 'learn-ok.png']], taps=[[2.6, *LEARN]], zoom=[[0, 1.55, 195, 640]], t1=dict(text='it learns<br>your cooker.', y=150, size=96)),
   dict(at=16.1, fill='lang1-alarm.png', t1=dict(text='in your<br>language.', y=180, size=96, out=0.9)),
   dict(at=16.85, seam='whip', fill='lang2-alarm.png'), dict(at=17.6, seam='whip', fill='lang3-alarm.png'),
   dict(at=18.35, seam='whip', fill='lang4-alarm.png'), dict(at=19.1, seam='whip', fill='lang5-alarm.png'),
   dict(at=19.9, end=dict(fact='works offline. no app store.'))],
   sfx=[('whistle', 1.9, 0.6, 1.5), ('gas-hum', 3.0, 0.25, 7.2), ('tap', 4.7, 0.6), ('whistle', 6.65, 0.85, 1.25), ('whoosh', 7.8, 0.5), ('whistle', 7.95, 0.85, 1.25),
        ('whoosh', 9.1, 0.5), ('whistle', 9.25, 0.9, 1.0), ('alarm', 10.25, 0.8), ('whistle', 14.4, 0.6, 1.2), ('tap', 15.4, 0.6),
        ('ding', 16.15, 0.5), ('ding', 16.9, 0.45), ('ding', 17.65, 0.45), ('ding', 18.4, 0.45), ('ding', 19.15, 0.45), ('hit', 19.95, 0.75)],
   vo=[('L1', 0.4), ('L2', 3.1), ('L3', 6.7), ('L4', 9.2), ('L5', 12.9), ('L6', 20.4)]),
 'howto': dict(total=32.8, end_hit=28.2, shots=[
   dict(at=0.0, photo='cooker2.jpg', z0=1.0, z1=1.14, steam=True, t1=dict(text='set it up<br>in a minute.', y=680, size=130)),
   dict(at=2.8, icon=True, t1=dict(text='add it to your<br>home screen.', y=230, size=96), t2=dict(text='chrome → ⋮ → add to home screen', y=1330, size=44, **{'in': 0.6})),
   dict(at=6.1, screen='idle.png', zoom=[[0, 1.0], [0.8, 1.5, 290, 700]], taps=[[2.2, 287, 729]], t1=dict(text='allow the mic.<br>tap Learn my whistle.', y=140, size=84)),
   dict(at=8.9, seq=[[0, 'learnrun/l0005.png'], [1.6, 'learnrun/l0040.png'], [3.6, 'learn-ok.png']], taps=[[3.5, *LEARN]], zoom=[[0, 1.55, 195, 660]], t1=dict(text='quiet. whistle.<br>tap Done.', y=140, size=96)),
   dict(at=13.5, seq=[[0, 'idle.png'], [1.5, 'presets.png']], taps=[[1.2, 330, 422]], t1=dict(text='set the whistles.<br>save a preset.', y=140, size=88)),
   dict(at=18.1, screen='idle.png', zoom=[[0, 1.0], [0.6, 1.7, 195, 537]], t1=dict(text='a backup timer,<br>just in case.', y=140, size=88)),
   dict(at=20.8, run=[0.0, 4.5], r0=0.9, r1=4.6, pre='idle.png', taps=[[0.8, *START]], t1=dict(text='near the cooker.<br>screen on.', y=140, size=88)),
   dict(at=25.4, photo='dal.jpg', z0=1.04, z1=1.14, t1=dict(text='it counts.<br>you cook.', y=700, size=140)),
   dict(at=27.8, end=dict(fact='one link. no account. works offline.'))],
   sfx=[('gas-ignite', 0.3, 0.7), ('pot-lid', 2.85, 0.5), ('tap', 8.3, 0.6), ('whistle', 11.3, 0.8, 1.6), ('tap', 12.4, 0.6), ('tap', 14.7, 0.6),
        ('tap', 21.6, 0.6), ('whistle', 24.99, 0.85, 1.4), ('hit', 27.85, 0.75)],
   vo=[('H1', 0.4), ('H2', 2.9), ('H3', 6.2), ('H4', 9.0), ('H5', 13.6), ('H6', 18.2), ('H7', 20.9), ('H8', 25.5)]),
 'languages': dict(total=13.5, end_hit=9.9, shots=[
   dict(at=0.0, photo='cooker1.jpg', z0=1.0, z1=1.12, steam=True, t1=dict(text='in your<br>language.', y=700, size=140)),
   dict(at=2.0, fill='lang0-alarm.png'), dict(at=3.25, seam='whip', fill='lang1-alarm.png'), dict(at=4.5, seam='whip', fill='lang2-alarm.png'),
   dict(at=5.75, seam='whip', fill='lang3-alarm.png'), dict(at=7.0, seam='whip', fill='lang4-alarm.png'), dict(at=8.25, seam='whip', fill='lang5-alarm.png'),
   dict(at=9.5, end=dict(fact='english · தமிழ் · हिन्दी · తెలుగు · മലയാളം · ಕನ್ನಡ'))],
   sfx=[('whistle', 0.8, 0.8, 1.2), ('alarm', 2.05, 0.6)] + [('ding', 3.3 + 1.25 * i, 0.5) for i in range(5)] + [('hit', 9.55, 0.75)], vo=[]),
}

def load(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
SFX = {'whistle': f'{W}/sfx/cooker-whistle.wav', 'gas-ignite': f'{W}/sfx/gas-ignite.wav', 'gas-hum': f'{W}/sfx/gas-hum.wav', 'pot-lid': f'{W}/sfx/pot-lid-close.wav',
       'alarm': f'{W}/sfx/stopwatch-alert.wav', 'ding': f'{W}/sfx/oven-ding.wav', 'tap': f'{KIT}/real-click_1.wav', 'whoosh': f'{KIT}/real-whoosh-short_1.wav', 'hit': f'{KIT}/real-hit_1.wav'}
def rms_db(x): return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)

def mix(name, R, out):
    N = int(R['total'] * SR)
    s0 = LAST_HIT - R['end_hit']; mus = load(MUSIC)[int(s0 * SR):int(s0 * SR) + N]; mus = np.pad(mus, ((0, N - len(mus)), (0, 0)))
    fi = int(0.4 * SR); mus[:fi] *= np.linspace(0, 1, fi)[:, None]; mus[-int(0.6 * SR):] *= np.linspace(1, 0, int(0.6 * SR))[:, None]
    voice = np.zeros((N, 2), np.float32); vm = np.zeros(N, np.float32)
    for vid, t in R['vo']:
        x = load(f'{W}/vo/{vid}.wav'); x *= 10 ** ((-17 - rms_db(x[np.abs(x[:, 0]) > 0.01])) / 20); s = int(t * SR); m = min(len(x), N - s); voice[s:s + m] += x[:m]; vm[s:s + m] = 1
    w = int(0.2 * SR); k = np.convolve(vm, np.ones(w) / w, 'same'); duck = 10 ** ((-10 * np.clip(k * 1.5, 0, 1)) / 20)
    bed = mus * 10 ** (-6 / 20) * duck[:, None]
    fx = np.zeros((N, 2), np.float32)
    for e in R['sfx']:
        kind, t, g = e[0], e[1], e[2]; x = load(SFX[kind])
        if len(e) > 3: L = int(e[3] * SR); x = x[:L].copy(); f = min(len(x), int(0.25 * SR)); x[-f:] *= np.linspace(1, 0, f)[:, None]
        x = x / (np.max(np.abs(x)) + 1e-9) * g * (0.35 if kind in ('gas-hum',) else 0.55)
        s = int(t * SR); m = min(len(x), N - s); fx[s:s + m] += x[:m]
    mixd = bed + voice + fx; sf.write(out + '.raw.wav', mixd, SR)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', out + '.raw.wav', '-af', 'loudnorm=I=-14:TP=-2:LRA=11,alimiter=limit=0.8', '-ar', '48000', out], check=True)

if __name__ == '__main__':
    os.makedirs(f'{W}/reels', exist_ok=True)
    names = sys.argv[1:] or list(REELS)
    for n in names:
        R = REELS[n]; json.dump(R, open(f'{W}/work/spec-{n}.json', 'w'))
        mix(n, R, f'{W}/work/{n}-audio.wav'); print('audio', n)
