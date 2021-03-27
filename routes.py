import uuid
from flask import request, jsonify
from flask import current_app as app
from .models import db, Utility


@app.route('/list', methods=['GET'])
def list():

    # TODO: do geo query
    utilities = Utility.query.all()

    return jsonify([u.to_json() for u in utilities]), 200


@app.route('/utility', methods=['POST'])
def add_utility():

    id = str(uuid.uuid4())
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    description = request.form['description']

    # assume one image for now
    img_url = f'static/{id}.png'
    file = request.files['image']
    file.save(img_url)

    u = Utility(
        id=id,
        type=0,
        image_url=img_url,
        lat=lat,
        lon=lon,
        description=description,
    )
    db.session.add(u)
    db.session.commit()

    return jsonify(u.to_json()), 200


@app.route('/utility/<id>', methods=['PUT'])
def edit_utility(id):

    u = Utility.query.get(id)
    if u == None:
        return jsonify([]), 404

    if 'description' in request.form:
        description = request.form['description']
        u.description = description

    if 'image' in request.files:
        file = request.files['image']
        file.save(f'static/{u.id}.png')

    db.session.commit()

    return jsonify(u.to_json()), 200


@app.route('/utility/<id>/rate', methods=['POST'])
def rate(id):
    # TODO
    return jsonify(f'Add rating for {id}'), 200
