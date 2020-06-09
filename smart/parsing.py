import math


def parseVideoCalculated(calculated, **injected):

    parameters = {}
    if calculated:
        for (key, value) in calculated.items():
            calculate = value
            for (k, v) in injected.items():
                calculate = calculate.replace(k, str(v))
            injected.update({key: eval(calculate)})

        for key in calculated.keys():
            parameters.update({key: injected[key]})

    return parameters


def parseVideoConstant(constant):

    d = {}
    for i in constant:
        d.update(i)
    return d


def buildVideoEncoderParams(listOfDict):

    parameters = dict()
    for k in listOfDict:
        parameters.update(k)

    encoderParams = ""
    for (k, v) in parameters.items():
        s = "{}={}:".format(k, v)
        encoderParams += s

    return encoderParams.strip(':')


def buildVideoEncoder(codec, preset, paramsName, params):

    d = {}
    d.update({'c:v': codec})

    if preset:
        d.update({'preset': preset})

    d.update({paramsName: params})
    return d


def buildVideoChromaSubsampling(bit_depth, encoder):

    def parseYUV(yuv):

        if yuv == '420':
            return 'yuv420p'
        elif yuv == '422':
            return 'yuv422p'
        elif yuv == '444':
            return 'yuv444p'
        else:
            return 'yuv420p'

    def parseBitDepth(bit_depth):

        if bit_depth == '8':
            return ''
        elif bit_depth == '10':
            return '10le'

    yuv, bit_depth = bit_depth.split('-')
    bit_depth = '{}{}'.format(parseYUV(yuv), parseBitDepth(bit_depth))

    encoder['pix_fmt'] = bit_depth
    return encoder


def buildAudioEncoderParams(params):

    if params != None:
        return params
    else:
        return {}


def buildAudioEncoder(codec, params):
    d = {}
    d.update({'c:a': codec})

    for k, v in params.items():
        d.update({k: v})

    return d


def buildEncoder(videoEncoder, audioEncoder):

    return {**videoEncoder, **audioEncoder}


def parseResize(size, width, height):

    calculated = False
    if size != 'native':
        calculated = math.ceil((width / height) * int(size))
        return {'width': calculated, 'height': int(size)}

    return calculated


def listPresets(configurations):

    print('---\nGLOBAL PRESETS\n')
    for preset in configurations['global-presets']:
        for (preset_name, preset_detail) in preset.items():
            print("Preset : " + preset_name)
            print("\tVideo preset : " + preset_detail['video-preset'])
            print("\tAudio preset : " + preset_detail['audio-preset'])

    print('\n---\nVIDEO PRESETS\n')
    for preset in configurations['video']:
        print("\t- " + preset)

    print('\n---\nAUDIO PRESETS\n')
    for preset in configurations['audio']:
        print("\t- " + preset)
