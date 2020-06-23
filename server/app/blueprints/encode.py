from quart import Quart, make_response, render_template, send_from_directory, Blueprint, jsonify
from quart_cors import cors


encode = Blueprint('encode', __name__, url_prefix='/encode')
cors(encode)


@encode.route('/test', methods=['GET'])
async def test():
    return jsonify({'response': 'okay', 'code': 200})
