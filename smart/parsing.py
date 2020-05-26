

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

def listPresets(configurations):
    
    print('---\nGLOBAL PRESETS\n')
    for preset in configurations['global-presets']:
        for (preset_name, preset_detail) in preset.items():
            print("Preset : " + preset_name)
            print("\tVideo preset : " + preset_detail['video-preset'])
            print("\tAudio preset : " + preset_detail['audio-preset'])

    print('\n---\nVIDEO PRESETS\n')
    for preset in configurations['video-presets']:
        print("\t- " + preset)

    print('\n---\nAUDIO PRESETS\n')
    for preset in configurations['audio-presets']:
        print("\t- " + preset)