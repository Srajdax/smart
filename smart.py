import ffmpeg
import yaml
import re
import sys
import argparse


try:
    inp = sys.argv[1]
except Exception as e:
    print("Please provide an input file")
    exit(1)


def parseCalculated(calculated, **injected):

    parameters = {}

    for (key, value) in calculated.items():
        calculate = value
        for (k, v) in injected.items():
            calculate = calculate.replace(k, str(v))
        injected.update({key: eval(calculate)})

    for key in calculated.keys():
        parameters.update({key: injected[key]})

    return parameters


def parseConstant(constant):

    d = {}
    for i in constant:
        d.update(i)
    return d


def buildEncoderParams(listOfDict):

    parameters = dict()
    for k in listOfDict:
        parameters.update(k)

    encoderParams = ""
    for (k, v) in parameters.items():
        s = "{}={}:".format(k, v)
        encoderParams += s

    return encoderParams.strip(':')


def buildEncoder(codec, preset, paramsName, params):

    d = {}
    d.update({'c:v': codec})

    if preset:
        d.update({'preset': preset})

    d.update({paramsName: params})
    return d


with open("configuration.yaml", 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

encoding = parameters['x264-lossless']

probe = ffmpeg.probe("introduction.mov")
video_stream = next(
    (stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
framerate = int(video_stream['avg_frame_rate'].split('/')[0])

injected = {'framerate': framerate}
calculated = parseCalculated(encoding['parameters']['calculated'], **injected)
constants = parseConstant(encoding['parameters']['constants'])
params = buildEncoderParams([calculated, constants])
encoder = buildEncoder(
    encoding['codec'], encoding['preset'], encoding['parameters']['name'], params)

(
    ffmpeg
    .input('introduction.mov')
    .output('test.mp4', **encoder)
    .run()
)
