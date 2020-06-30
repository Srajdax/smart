from quart import Quart, make_response, render_template, send_from_directory, Blueprint, jsonify
from quart_cors import cors

from .. import factory
from ..models.mongo import Video, Preset, Model

encode = Blueprint('encode', __name__, url_prefix='/encode')
cors(encode)


@encode.route('/test', methods=['GET'])
async def test():

    x = Model()
    print(x.scheme)
    print(x.validate({}))

    x = Preset()
    print(x.scheme)
    print(x.validate({'title': 'mon titre'}))

    return jsonify({'response': 'okay', 'code': 200})


@encode.route('/populate', methods=['GET'])
async def populate():

    return jsonify({'response': 'populated', 'code': 200})
