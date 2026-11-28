#!/bin/bash
# Assemble and zip the #002 kit: reels into their day folders, docs, profile, brand, source.
set -e; K=/home/user/Image-Scanner/brag-output/launch-kit-002; WH=/home/user/Image-Scanner/brag-output/whistle
N=wierd_stuff_i_make_002_6-day-launch-kit; P=$K/package/$N; rm -rf $K/package; mkdir -p $P/days $P/source/reels $P/reels
cp $WH/reels/teaser.mp4 $K/out/Day02_*/feed/; cp $WH/reels/launch.mp4 $K/out/Day03_*/feed/; cp $WH/reels/howto.mp4 $K/out/Day04_*/feed/; cp $WH/reels/languages.mp4 $K/out/Day06_*/feed/
cp -r $K/out/Day0* $P/days/; cp -r $K/out/after-launch-library $K/out/profile $K/out/brand $P/
cp $K/out/00_START_HERE.pdf $K/out/calendar.pdf $K/out/calendar.csv $P/
cp $WH/reels/*.mp4 $P/reels/
cp $K/src/{content.py,docs.py,make_templates.py,_css.py,render.js,pdf.js,logos.js,package.sh} $P/source/
cp $WH/{reel.html,reels_w.py,render_reel.js} $WH/work/{capture.js,whistle_audio.py} $P/source/reels/
cat > $P/README.txt <<'T'
@wierd_stuff_i_make · product #002 · Cooker Whistle Counter
6-day Instagram launch · Sat 28 Nov – Thu 3 Dec 2026 · launch Mon 30 Nov, 7 pm

Open 00_START_HERE.pdf first.

  days/                 one folder per day: feed/ (slides, or reel mp4 + cover.png), story/, caption.txt
  reels/                the four cinematic reels on their own (teaser, launch, howto, languages)
  after-launch-library/ 5 finished posts for after 3 Dec
  profile/              profile picture (orange cursor), highlight covers, bio options
  brand/                #002 brand guidelines (PDF) + logo files
  calendar.pdf / .csv   the plan at a glance, with tracking columns
  source/               the generators (kit + reels)

Every screen in the reels and posts is the real app, captured while it counted real whistles.
Photos: public domain / CC0. Music: Mixkit licence. Sound effects: Mixkit, plus a cooker whistle built from Mixkit steam.
T
cd $K/package && rm -f ../$N.zip && zip -qr ../$N.zip $N && ls -la ../$N.zip
