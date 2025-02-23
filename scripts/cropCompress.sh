# crop w/ 30 MBit/s bitrate
ffmpeg -i output-pipeline.mp4 -vcodec libx264 -b:v 30M -vf "crop=1080:2400:10:10" output_cropped.mp4

# crop w/ default bitrate
ffmpeg -i output-pipeline.mp4 -vcodec libx264 -vf "crop=1080:2400:10:10" output_cropped.mp4

# demo gif
ffmpeg -i out/output-pipeline.mp4 -filter_complex "crop=1356:524:10:10,fps=16,split[s0][s1];[s0]palettegen=max_colors=4:reserve_transparent=0:stats_mode=single[p];[s1][p]paletteuse" out/demo.gif