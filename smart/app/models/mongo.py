
from cerberus import Validator
from .const import EMAIL_REGEX, TEXT_REGEX


class Model:

    scheme = {}

    def validate(self, payload):
        validator = Validator()
        return validator.validate(payload, self.scheme)


class Preset(Model):
    name = "video"

    # Use the cerberus library to validate the dict
    scheme = {"name": {'type': 'string', 'required': True, 'nullable': False},
              "video_preset": {'type': 'string', 'required': True, 'nullable': False},
              "audio_preset": {'type': 'string', 'required': True, 'nullable': False}
              }


class VideoPreset(Model):
    name = "video"

    # Use the cerberus library to validate the dict
    scheme = {"name": {'type': 'string', 'nullable': False},
              "codec": {'type': 'string', 'nullable': False},
              "preset": {'type': 'string', 'nullable': True},
              "parameters": {'type': 'string', 'nullable': True},
              "calculated": {'type': 'list', 'nullable': True},
              "constants": {'type': 'list', 'nullable': True},
              }


class AudioPreset:
    name = "audio"

    # Use the cerberus library to validate the dict
    scheme = {"name": {'type': 'string', 'nullable': False},
              "codec": {'type': 'string', 'nullable': False},
              "preset": {'type': 'string', 'nullable': True},
              "parameters": {'type': 'string', 'nullable': True},
              "calculated": {'type': 'list', 'nullable': True},
              "constants": {'type': 'list', 'nullable': True},
              }


class Video:
    name = "video"

    # Use the cerberus library to validate the dict
    scheme = {}


class Encode:
    name = "encode"
