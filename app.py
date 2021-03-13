from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CORS(app)


@app.route('/list', methods=['GET'])
def list():
    # TODO: sending back dummy data for now
    return jsonify([
        {
            'id': 'abcde12345',
            'type': 2,
            'imageURL': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            'lat': 0.0,
            'lon': 0.0,
            'description': 'Nice and warm',
            'rating': 4.35,
        },
    ]), 200


@app.route('/utility', methods=['POST'])
def add_utility():
    # TODO
    return jsonify('Add utility'), 200


@app.route('/utility/<id>', methods=['PUT'])
def edit_utility(id):
    # TODO
    return jsonify(f'Edit utility {id}'), 200
    

@app.route('/utility/<id>/rate', methods=['POST'])
def rate(id):
    # TODO
    return jsonify(f'Add rating for {id}'), 200
