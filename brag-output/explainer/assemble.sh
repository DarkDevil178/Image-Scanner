#!/bin/bash
# assemble.sh h|v : cold open (with its last 0.3 s faded to brand blue) + the chapters, then the full mix
set -e
O=$1; D=/home/user/Image-Scanner/brag-output/explainer; W=/home/user/Image-Scanner/brag-output/work
if [ "$O" = h ]; then S=1920x1080; else S=1080x1920; fi
ffmpeg -v error -y -i $W/final-$O.mp4 -an -vf "fade=out:st=23.933:d=0.3:color=0x3D4FE0" -c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p $D/cold-$O.mp4
ffmpeg -v error -y -framerate 30 -i $D/frames-$O/f%05d.jpg -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p $D/body-$O.mp4
ffmpeg -v error -y -i $D/cold-$O.mp4 -i $D/body-$O.mp4 -i $D/mix.wav -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0[v]" -map "[v]" -map 2:a \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 -c:a aac -b:a 256k -shortest -movflags +faststart $D/explainer-$O.mp4
ffprobe -v error -show_entries stream=codec_type,width,height,nb_frames -show_entries format=duration,size -of compact $D/explainer-$O.mp4
