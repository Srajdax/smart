import sys

# Loading Quart and Blueprints
try:
    from quart import Quart, make_response, render_template, send_from_directory
    from quart_cors import cors
    from .database.factory import Factory
    from .models.mongo import *

    # Create the factory
    factory = Factory([Video, AudioPreset, VideoPreset, Video, Preset, Encode])

    # create and configure the app
    app = Quart(__name__)

    # Register blueprints
    from .blueprints.encode import encode
    app.register_blueprint(encode)

except Exception as e:
    print(e)
    sys.exit(1)
