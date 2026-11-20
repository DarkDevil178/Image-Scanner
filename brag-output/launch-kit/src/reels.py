# Cut the kit's reels from the finished films; every reel 1080x1920 30 fps, H.264 + AAC, -14 LUFS.
import json, subprocess, os
B = '/home/user/Image-Scanner/brag-output'; K = f'{B}/launch-kit'; O = f'{K}/out'; TMP = f'{K}/build/reels'; os.makedirs(TMP, exist_ok=True)
EXP = f'{B}/feature-explainer/wardrobe-features-9x16.mp4'; LAUNCH = f'{B}/combined/wardrobe-launch-9x16.mp4'
VB = f'{B}/film/wardrobe/out/vB.mp4'; MUSIC = f'{B}/film/wardrobe/audio/music/cat_walk_mixkit.mp3'
COLD = 727 / 30
TL = json.load(open(f'{B}/explainer/timeline.json'))['T']
start = {b['id']: b['start'] + COLD for b in TL}
plan = {p['reel']: p['folder'] for p in json.load(open(f'{K}/build/plan.json')) + json.load(open(f'{K}/build/bonus.json')) if p.get('reel')}
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
# the teaser: the clothes pile up round "Nothing to wear?", the real photo is cut out, then the #001 card, under the licensed track
cl = [(LAUNCH, 0.0, 2.3), (VB, 1.2, 2.8)]; card = f'{O}/_build/tease.png'; tot = sum(c[2] for c in cl) + 3.4
run(['-ss', '0', '-t', '2.3', '-i', LAUNCH, '-ss', '1.2', '-t', '2.8', '-i', VB, '-loop', '1', '-t', '3.4', '-i', card, '-ss', '88.61', '-t', f'{tot:.3f}', '-i', MUSIC,
     '-filter_complex', '[0:v]scale=1080:1920,setpts=PTS-STARTPTS,format=yuv420p[a];[1:v]scale=1080:1920,setpts=PTS-STARTPTS,format=yuv420p[b];'
     '[2:v]scale=1080:1920,format=yuv420p,fade=in:st=0:d=0.3,setpts=PTS-STARTPTS[c];[a][b][c]concat=n=3:v=1:a=0[v];'
     f'[3:a]afade=in:st=0:d=0.05,afade=out:st={tot - 1.0:.3f}:d=1.0,loudnorm=I=-14:TP=-1.5[au]', '-map', '[v]', '-map', '[au]', *ENC, out('teaser')])
for k in plan:
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size', '-of', 'csv=p=0', out(k)], capture_output=True, text=True).stdout.strip()
    print(k, r)
