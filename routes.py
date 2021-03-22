import uuid
from flask import request, jsonify
from flask import current_app as app
from .models import db, Utility


@app.route('/dummy', methods=['GET'])
def dummy():
    u = Utility(
        type=2,
        image_url='https://upload.wikimedia.org/wikipedia/commons/f/fe/Bubbler.jpg',
        lat=38.89151086127753,
        lon=-77.02606859385605,
        description='Nice and warm',
        rating=4.35,
    )
    db.session.add(u)
    db.session.commit()
    return jsonify({})


@app.route('/list', methods=['GET'])
def list():
    # TODO: sending back dummy data for now
    return jsonify([
        {
            'id': 'abcde12345',
            'type': 2,
            'imageURL': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Bubbler.jpg',
            'lat': 38.89151086127753,
            'lon': -77.02606859385605,
            'description': 'Nice and warm',
            'rating': 4.35,
        },
        {
            'id': 'fghijk67890s',
            'type': 1,
            'imageURL': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Bubbler.jpg',
            'lat': 38.993452,
            'lon': -77.014709,
            'description': 'second one',
            'rating': 1.23,
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
