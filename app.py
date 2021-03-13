import uuid
from flask import Flask, request, jsonify
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
            'lat': 38.893452,
            'lon': -77.014709,
            'description': 'Nice and warm',
            'rating': 4.35,
        },
    ]), 200


@app.route('/utility', methods=['POST'])
def add_utility():

    id = str(uuid.uuid4())
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    description = request.form['description']

    file = request.files['image']
    file.save(f'static/{id}.png')  # assume one image for now

    # TODO: save data into db
    utility = {
        'id': id,
        'lat': lat,
        'lon': lon,
        'description': description,
        'imageURL': f'static/{id}.png',
    }

    print(utility)

    return jsonify(utility), 200


@app.route('/utility/<id>', methods=['PUT'])
def edit_utility(id):
    # TODO
    return jsonify(f'Edit utility {id}'), 200


@app.route('/utility/<id>/rate', methods=['POST'])
def rate(id):
    # TODO
    return jsonify(f'Add rating for {id}'), 200
