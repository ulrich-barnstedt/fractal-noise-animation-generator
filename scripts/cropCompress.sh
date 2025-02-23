# crop w/ 30 MBit/s bitrate
ffmpeg -i output-pipeline.mp4 -vcodec libx264 -b:v 30M -vf "crop=1080:2400:10:10" output_cropped.mp4

# crop w/ default bitrate
ffmpeg -i output-pipeline.mp4 -vcodec libx264 -vf "crop=1080:2400:10:10" output_cropped.mp4
