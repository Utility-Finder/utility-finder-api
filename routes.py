import os
import uuid
from flask import request, jsonify
from flask import current_app as app
from sqlalchemy.sql import text
from models import db, Utility
from app import bucket


def upload_to_gcp(id, file):
    """Upload utility image to GCP cloud storage
    """
    img_url = f'static/{id}.png'
    file.save(img_url)
    blob = bucket.blob(img_url)
    blob.upload_from_filename(img_url)
    os.remove(img_url)


@app.route('/list', methods=['GET'])
def list():
    """List all utilities within a radius
    """

    lat = request.args.get('lat')
    if lat == None:
        return jsonify('lat parameter is required'), 400

    try:
        lat = float(lat)
    except ValueError:
        return jsonify('lat needs to be double'), 400

    lon = request.args.get('lon')
    if lon == None:
        return jsonify('lon parameter is required'), 400

    try:
        lat = float(lat)
    except ValueError:
        return jsonify('lon needs to be double'), 400

    radius = request.args.get('radius')
    if radius == None:
        radius = 100

    try:
        radius = float(radius)
    except ValueError:
        return jsonify('radius needs to be double'), 400

    utilities = Utility.query.from_statement(
        text("""
        SELECT * FROM utility
        WHERE earth_box(ll_to_earth(:lat, :lon), :radius) @> ll_to_earth(utility.lat, utility.lon)
        """)
    ).params(lat=lat, lon=lon, radius=radius).all()

    return jsonify([u.to_json() for u in utilities]), 200


@app.route('/utility', methods=['POST'])
def add_utility():
    """Upload a utility
    """

    lat = request.form.get('lat')
    if lat == None:
        return jsonify('lat parameter is required'), 400

    try:
        lat = float(lat)
    except ValueError:
        return jsonify('lat needs to be double'), 400

    lon = request.form.get('lon')
    if lon == None:
        return jsonify('lon parameter is required'), 400

    try:
        lat = float(lat)
    except ValueError:
        return jsonify('lon needs to be double'), 400

    description = request.form.get('description')
    if description == None:
        return jsonify('description parameter is required'), 400

    file = request.files.get('image')
    if file == None:
        return jsonify('image parameter is required'), 400

    # Upload image to GCP
    id = str(uuid.uuid4())
    upload_to_gcp(id, file)

    u = Utility(
        id=id,
        type=0,
        lat=lat,
        lon=lon,
        description=description,
    )
    db.session.add(u)
    db.session.commit()

    return jsonify(u.to_json()), 200


@app.route('/utility/<id>', methods=['PUT'])
def edit_utility(id):
    """Edit a utility
    """

    u = Utility.query.get(id)
    if u == None:
        return jsonify([]), 404

    description = request.form.get('description')
    if description != None:
        u.description = description

    file = request.files.get('image')
    if file != None:
        upload_to_gcp(id, file)

    db.session.commit()

    return jsonify(u.to_json()), 200


@app.route('/utility/<id>/rate', methods=['POST'])
def rate(id):
    """Rate a utility
    """

    # TODO
    return jsonify(f'Add rating for {id}'), 200
