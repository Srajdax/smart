
from app import app
from app.models import parsing
import argparse
import sys
import re
import yaml
import ffmpeg

PORT: int = 5000

CONFIGURATION_FILE = "configuration.yaml"
OUTPUT = "output"
MUX = "mp4"
YUV = '420-8'
VIDEO = 'x264-fast-crf'
AUDIO = 'aac256'

parser = argparse.ArgumentParser(
    description="SMART - a simple tool to ease and automate video encoding")


# Definig the arguments
parser.add_argument(
    "-s", "--server", help="Launch SMART as a server", action='store_true')
parser.add_argument(
    "-i", "--input", help="The input file to be encoded", type=str, required=('-s' or '--server') not in sys.argv)
parser.add_argument("-l", "--list-preset",
                    help="List all the presets available", required=False, action="store_true")
parser.add_argument(
    "-c", "--config", help="The .yaml configuration file for the presets, default file 'configuration.yaml' in the current directory", type=str, required=False)
parser.add_argument("-p", "--preset",
                    help="Select a global preset", required=False)
parser.add_argument("-v", "--video",
                    help="Select a video preset, default is 'x264-fast-crf'", required=False)
parser.add_argument("-a", "--audio",
                    help="Select an audio preset, default is 'aac-256'", required=False)
parser.add_argument("-yuv", "--chroma-subsampling",
                    help="Select the chroma subsampling and the bit depth, supports [420-8, 420-10, 422-8, 422-10, 444-8, 444-10], default is '420-8'", choices=["420-8", "420-10", "422-8", "422-10", "444-8", "444-10"], type=str, required=False)
parser.add_argument("-r", "--resize",
                    help="Provide a list to resize the video and output it in multiple size", required=False, nargs='+', type=str, choices=['360', '480', '720', '1080', '2160', 'native'])
parser.add_argument("-m", "--mux",
                    help="Select container for the encoded file (available: mp4, mov, mkv), default is 'mp4'", choices=["mp4", "mkv", "mov"], required=False)
parser.add_argument(
    "-o", "--output", help="The output name of the encoded file, default name 'output'", type=str, required=False)
args = parser.parse_args()

if args.server:
    app.run(host='0.0.0.0', port=PORT, debug=True)
else:

    if args.config:
        CONFIGURATION_FILE = args.config

    with open(CONFIGURATION_FILE, 'r') as stream:
        try:
            parameters = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    if args.chroma_subsampling:
        YUV = args.chroma_subsampling

    if args.list_preset:
        parsing.listPresets(parameters)
        exit(0)

    if args.mux:
        MUX = args.mux

    if args.output:
        OUTPUT = args.output

    if args.video:
        VIDEO = args.video

    if args.audio:
        AUDIO = args.audio

    OUT = OUTPUT + '.{}'.format(MUX)

    encoding = parameters['video'][VIDEO]

    probe = ffmpeg.probe("introduction.mov")
    video_stream = next(
        (stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    framerate = int(video_stream['avg_frame_rate'].split('/')[0])
    video_width, video_height = int(
        video_stream['width']), int(video_stream['height'])

    # Build Video Parameters
    injected = {'framerate': framerate}
    calculated = parsing.parseVideoCalculated(
        encoding['parameters'].get('calculated', None), **injected)
    constants = parsing.parseVideoConstant(encoding['parameters']['constants'])
    params = parsing.buildVideoEncoderParams([calculated, constants])
    encoder = parsing.buildVideoEncoder(
        encoding['codec'], encoding['preset'], encoding['parameters']['name'], params)
    videoEncoder = parsing.buildVideoChromaSubsampling(YUV, encoder)

    # Build Audio Parameters
    encoding = parameters['audio'][AUDIO]
    params = parsing.buildAudioEncoderParams(encoding['parameters'])
    audioEncoder = parsing.buildAudioEncoder(encoding['codec'], params)

    # Build Encoder
    encoder = parsing.buildEncoder(videoEncoder, audioEncoder)
    print(encoder)

    if args.resize:
        for size in args.resize:
            print(encoder)
            OUT = '{}-{}.{}'.format(OUTPUT, size, MUX)
            print(OUT)
            size = parsing.parseResize(size, video_width, video_height)
            print(size)

            if size:
                video = ffmpeg.input(args.input).video
                audio = ffmpeg.input(args.input).audio
                video = video.filter('scale', size['width'], size['height'])
                joined = ffmpeg.concat(video, audio, v=1, a=1)
                stream = joined.output(OUT, **encoder)
                stream.run()
            else:
                (
                    ffmpeg
                    .input(args.input)
                    .output(OUT, **encoder)
                    .run()
                )
        sys.exit(0)

    (
        ffmpeg
        .input(args.input)
        .output(OUT, **encoder)
        .run()
    )
