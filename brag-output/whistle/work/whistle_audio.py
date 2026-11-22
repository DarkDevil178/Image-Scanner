# The cooker whistle: Mixkit's recorded "Steam swoosh" as the body, a shaped whistle tone on top (no cooker-whistle
# recording with a usable licence was found). Writes sfx/cooker-whistle.wav and work/mic-feed.wav (the fake microphone
# that drives the real app: kitchen hum with three whistles).
import numpy as np, soundfile as sf, subprocess
SR = 48000
D = '/home/user/Image-Scanner/brag-output/whistle'
rng = np.random.default_rng(3)
def load(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def bandpass(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR); X *= 1 / np.sqrt(1 + (lo / np.maximum(f, 1)) ** 6) / np.sqrt(1 + (f / hi) ** 6)
    return np.fft.irfft(X, len(x))

def whistle(dur=2.4):
    n = int(dur * SR); t = np.arange(n) / SR
    # pitch: rises into the whistle, holds with a slow waver, sags as the pressure drops
    f = 1750 + 480 * (1 - np.exp(-t / 0.18)) + 14 * np.sin(2 * np.pi * 5.5 * t) - 120 * np.clip((t - (dur - 0.5)) / 0.5, 0, 1)
    ph = 2 * np.pi * np.cumsum(f) / SR
    tone = np.sin(ph) + 0.32 * np.sin(2 * ph + 0.4) + 0.12 * np.sin(3 * ph + 1.1)
    hiss = bandpass(rng.standard_normal(n), 1400, 7000)
    hiss /= np.max(np.abs(hiss))
    env = np.minimum(1, t / 0.12) * np.clip((dur - t) / 0.45, 0, 1) ** 1.2
    flutter = 1 + 0.08 * np.sin(2 * np.pi * 23 * t + 2 * np.sin(2 * np.pi * 3 * t))
    w = (0.55 * tone * flutter + 0.45 * hiss) * env
    steam = load(f'{D}/sfx/steam-swoosh.wav'); steam = steam / (np.max(np.abs(steam)) + 1e-9)
    steam = np.interp(np.linspace(0, len(steam) - 1, n), np.arange(len(steam)), steam)   # stretch the recorded steam under the whistle
    w = w + 0.6 * steam * np.clip((dur - t) / 0.6, 0, 1)
    return w / np.max(np.abs(w)) * 0.9

w = whistle()
sf.write(f'{D}/sfx/cooker-whistle.wav', np.stack([w, w], 1), SR)
# the fake microphone: 26 s of the recorded gas-stove hum, whistles at 4, 11 and 18 s
hum = load(f'{D}/sfx/gas-hum.wav'); feed = np.tile(hum, 3)[: 26 * SR] * 0.25
for t0 in (4.0, 11.0, 18.0):
    s = int(t0 * SR); feed[s:s + len(w)] += w * 0.9
feed = feed / np.max(np.abs(feed)) * 0.95
sf.write(f'{D}/work/mic-feed.wav', (feed * 32767).astype(np.int16), SR, subtype='PCM_16')
print('whistle', len(w) / SR, 's; mic feed 26 s')
