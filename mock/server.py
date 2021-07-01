from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.exceptions import BadRequest

class api_response:
    def __init__(self):
        self.success = True
        self.message = ''
        self.estimated_data = {}

    def to_json(self):
        response = {
            'success': self.success,
            'message': self.message,
            'estimated_data': self.estimated_data,
        }
        return jsonify(response)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():

    if 'image_path' not in request.files:
        raise BadRequest()

    # image_stream = request.files['upload_file'].stream
    # image_array = bytearray(image_stream.read())

    try:
        # 画像をAIで所属するクラスを分析
        # estimated_data = xxx(image_array)
        estimated_data = {'class': 3, 'confidence': '0.8683'}

        response = api_response()
        response.success = True
        response.message = 'success'
        response.estimated_data = estimated_data
    except:
        response = api_response()
        response.success = False
        response.message = 'Error:E50012'

    return response.to_json(), 200

if __name__ == '__main__':
    app.run(port=9999, debug=True)
