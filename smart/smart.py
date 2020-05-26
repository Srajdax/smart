import ffmpeg
import yaml
import re
import sys
import argparse
import parsing

CONFIGURATION_FILE = "configuration.yaml"
OUTPUT = "output"
MUX = "mp4"

parser = argparse.ArgumentParser(
    description="SMART - a simple encoding script to automate video processing")

# preset total
# preset video
# preset audio
# conteneur
# output file
# input file
# configuration file
# list preset
# resize

# Definig the arguments
parser.add_argument(
    "-i", "--input", help="The input file to be encoded", type=str, required=True)
parser.add_argument("-l", "--list-preset",
                    help="List all the presets available", required=False, action="store_true")
parser.add_argument(
    "-c", "--config", help="The .yaml configuration file for the presets, default file 'configuration.yaml' in the current directory", type=str, required=False)
parser.add_argument("-p", "--preset",
                    help="Select a global preset", required=False)
parser.add_argument("-vp", "--video-preset",
                    help="Select a video preset, default is 'x264-fast-crf'", required=False)
parser.add_argument("-ap", "--audio-preset",
                    help="Select an audio preset, default is 'aac-256'", required=False)
parser.add_argument("-m", "--mux",
                    help="Select container for the encoded file (available: mp4, mov, mkv), default is 'mp4'", required=False)
parser.add_argument(
    "-o", "--output", help="The output name of the encoded file, default name 'output'", type=str, required=False)
args = parser.parse_args()

if args.config:
    CONFIGURATION_FILE = args.config

with open(CONFIGURATION_FILE, 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if args.list_preset:
    parsing.listPresets(parameters)
    exit(0)

if args.mux:
    MUX = args.mux

if args.output:
    OUTPUT = args.output

OUTPUT += '.{}'.format(MUX) 

encoding = parameters['x264-lossless']

probe = ffmpeg.probe("introduction.mov")
video_stream = next(
    (stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
framerate = int(video_stream['avg_frame_rate'].split('/')[0])

injected = {'framerate': framerate}
calculated = parsing.parseCalculated(
    encoding['parameters']['calculated'], **injected)
constants = parsing.parseConstant(encoding['parameters']['constants'])
params = parsing.buildEncoderParams([calculated, constants])
encoder = parsing.buildEncoder(
    encoding['codec'], encoding['preset'], encoding['parameters']['name'], params)

(
    ffmpeg
    .input(args.input)
    .output(OUTPUT, **encoder)
    .run()
)
