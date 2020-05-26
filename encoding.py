import ffmpeg
import yaml


# ffmpeg -i input.avi -c:v libx264 -preset slow -crf 22 -c:a copy output.mkv


def parseCalculated(framerate, calculated):

    d = {}

    return d


with open("parameters.yaml", 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

x264 = parameters['x264-fast']
print(x264)

probe = ffmpeg.probe("introduction.mov")
video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
width = int(video_stream['width'])
height = int(video_stream['height'])
framerate = int(video_stream['avg_frame_rate'].split('/')[0])
print(width, height, framerate)



print(eval('5+5'))


# (
#     ffmpeg
#     .input('introduction.mov')
#     .output('test.mp4', **{'c:v': 'libx264', 'preset': 'fast', 'crf': 30, 'x264-params': 'keyint=125:min-keyint=20:deblock=0,0', })
#     .run()
# )
