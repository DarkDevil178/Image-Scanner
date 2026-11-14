# Cut the kit's reels from the finished films; every reel 1080x1920 30 fps, H.264 + AAC, -14 LUFS.
import json, subprocess, os
B = '/home/user/Image-Scanner/brag-output'; K = f'{B}/launch-kit'; O = f'{K}/out'; TMP = f'{K}/build/reels'; os.makedirs(TMP, exist_ok=True)
EXP = f'{B}/feature-explainer/wardrobe-features-9x16.mp4'; LAUNCH = f'{B}/combined/wardrobe-launch-9x16.mp4'
VB = f'{B}/film/wardrobe/out/vB.mp4'; MUSIC = f'{B}/film/wardrobe/audio/music/cat_walk_mixkit.mp3'
COLD = 727 / 30
TL = json.load(open(f'{B}/explainer/timeline.json'))['T']
start = {b['id']: b['start'] + COLD for b in TL}
plan = {p['reel']: p['folder'] for p in json.load(open(f'{K}/build/plan.json')) if p.get('reel')}
def run(args): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + args, check=True)
ENC = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', '30', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
       '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart']
def out(key): return f'{O}/{plan[key]}/feed/{key}.mp4'
END = f'{O}/_build/endcard.png'

# chapter reels: the chapter (card included) from the explainer, then 2.5 s of the end card over the next seconds of sound
CH = [('ch1', 'c1t', 'c2t'), ('ch2', 'c2t', 'c3t'), ('ch3', 'c3t', 'c4t'), ('ch4', 'c4t', 'c5t'), ('ch5', 'c5t', 'c6t'), ('ch6', 'c6t', 'c7t'), ('ch7', 'c7t', 'c8t')]
for key, a, z in CH:
    s, e = start[a], start[z]; d = e - s; tot = d + 2.5
    run(['-ss', f'{s:.3f}', '-t', f'{tot:.3f}', '-i', EXP, '-loop', '1', '-t', '2.5', '-i', END,
         '-filter_complex', f'[0:v]trim=0:{d:.3f},setpts=PTS-STARTPTS[a];[1:v]scale=1080:1920,format=yuv420p,fade=in:st=0:d=0.25,setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0[v];'
         f'[0:a]afade=in:st=0:d=0.15,afade=out:st={tot - 1.2:.3f}:d=1.2,loudnorm=I=-14:TP=-1.5[au]', '-map', '[v]', '-map', '[au]', *ENC, out(key)])
# make it yours: the last chapter runs into the film's own end card
s = start['c8t']; run(['-ss', f'{s:.3f}', '-i', EXP, '-af', 'afade=in:st=0:d=0.15,loudnorm=I=-14:TP=-1.5', *ENC, out('ch8')])
# launch and the full tour: the finished films as they are
run(['-i', LAUNCH, '-af', 'loudnorm=I=-14:TP=-1.5', *ENC, out('launch')])
run(['-i', EXP, '-af', 'loudnorm=I=-14:TP=-1.5', *ENC, out('tour')])
# teasers: a moment from the films (no name shown), then the #001 card, under the licensed track
def tease(key, src, ss, dur, card, cardlen, mus=88.61):
    tot = dur + cardlen
    run(['-ss', f'{ss:.3f}', '-t', f'{dur:.3f}', '-i', src, '-loop', '1', '-t', f'{cardlen}', '-i', card, '-ss', f'{mus}', '-t', f'{tot:.3f}', '-i', MUSIC,
         '-filter_complex', f'[0:v]scale=1080:1920,setpts=PTS-STARTPTS,format=yuv420p[a];[1:v]scale=1080:1920,format=yuv420p,fade=in:st=0:d=0.3,setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0[v];'
         f'[2:a]afade=in:st=0:d=0.05,afade=out:st={tot - 1.0:.3f}:d=1.0,loudnorm=I=-14:TP=-1.5[au]', '-map', '[v]', '-map', '[au]', *ENC, out(key)])
tease('teaser1', LAUNCH, 0.0, 2.3, f'{O}/_build/tease1.png', 3.6)          # the clothes pile up round "Nothing to wear?"
tease('teaser2', VB, 1.2, 2.8, f'{O}/_build/tease2.png', 3.6)              # the real photo is cut out, step by step
# the 30-day recap: the best moments, under the licensed track, ending on the #002 card and the end card
clips = [(LAUNCH, 0.0, 2.3), (VB, 1.2, 2.8), (EXP, start['c3c'] + 1.3, 3.0), (EXP, start['c4a'] + 2.4, 2.5), (EXP, start['c5b'] + 0.6, 2.6),
         (EXP, start['c6b'] + 3.8, 2.5), (EXP, start['c7b'] + 2.0, 2.6), (EXP, start['c8a'] + 2.4, 2.4)]
args, parts = [], []
for i, (src, ss, du) in enumerate(clips):
    args += ['-ss', f'{ss:.3f}', '-t', f'{du:.3f}', '-i', src]; parts.append(f'[{i}:v]scale=1080:1920,setpts=PTS-STARTPTS,format=yuv420p[v{i}]')
n = len(clips); args += ['-loop', '1', '-t', '2.6', '-i', f'{O}/_build/tease30.png', '-loop', '1', '-t', '2.8', '-i', END]
parts.append(f'[{n}:v]scale=1080:1920,format=yuv420p,setpts=PTS-STARTPTS[v{n}]'); parts.append(f'[{n + 1}:v]scale=1080:1920,format=yuv420p,setpts=PTS-STARTPTS[v{n + 1}]')
tot = sum(c[2] for c in clips) + 2.6 + 2.8
args += ['-ss', '88.61', '-t', f'{tot:.3f}', '-i', MUSIC]
fc = ';'.join(parts) + ';' + ''.join(f'[v{i}]' for i in range(n + 2)) + f'concat=n={n + 2}:v=1:a=0[v];[{n + 2}:a]afade=out:st={tot - 1.5:.3f}:d=1.5,loudnorm=I=-14:TP=-1.5[au]'
run(args + ['-filter_complex', fc, '-map', '[v]', '-map', '[au]', *ENC, out('recap')])
for k in plan:
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size', '-of', 'csv=p=0', out(k)], capture_output=True, text=True).stdout.strip()
    print(k, r)
